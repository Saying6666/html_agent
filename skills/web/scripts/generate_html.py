#!/usr/bin/env python3
"""
generate_html.py — HTML 生成入口

默认模式下，本脚本只校验现有的 src/index.html 是否已经由当前 agent
根据 prompt.md 手工完成。

当用户明确要求使用外部 API 时，可切换到 --mode api：
- 使用 OpenAI 兼容接口
- 强制 stream=true
- 边接收边写入临时文件
- 结束后清洗并落盘为 src/index.html

用法:
    python generate_html.py --task fdu_012
    python generate_html.py --task fdu_012 --mode api
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests


DEFAULT_BASE_URL_ENV = "X666_BASE_URL"
DEFAULT_API_KEY_ENV = "X666_API_KEY"
DEFAULT_MODEL_ENV = "X666_MODEL_GEMINI"


def _load_env_file(env_path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        values[key] = value
    return values


def _require_config(env_values: dict[str, str], key: str) -> str:
    value = env_values.get(key, "").strip()
    if not value:
        sys.exit(f"[ERROR] .env.local 缺少配置项: {key}")
    return value


def _build_messages(prompt_content: str) -> list[dict[str, str]]:
    system_prompt = (
        "You are a senior frontend engineer and design-minded web builder. "
        "Generate one complete production-grade single-file index.html using "
        "inline <style> and inline <script>. "
        "Return only raw HTML with no markdown fences and no explanations. "
        "Follow the provided prompt precisely. "
        "Do not use local assets, React, Vue, Svelte, jQuery, Tailwind CDN, "
        "or any build step. Keep the final HTML readable and maintainable."
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt_content},
    ]


def _merge_prompt_with_extra_instruction(
    prompt_content: str,
    extra_instruction: str,
) -> str:
    extra_instruction = extra_instruction.strip()
    if not extra_instruction:
        return prompt_content

    return (
        f"{prompt_content.rstrip()}\n\n"
        "## Additional Runtime Direction\n"
        f"{extra_instruction}\n"
    )


def _extract_text_from_chunk(payload: dict) -> str:
    pieces: list[str] = []
    for choice in payload.get("choices", []):
        delta = choice.get("delta") or {}
        content = delta.get("content")
        if content is None:
            message = choice.get("message") or {}
            content = message.get("content")

        if isinstance(content, str):
            pieces.append(content)
        elif isinstance(content, list):
            for item in content:
                if isinstance(item, str):
                    pieces.append(item)
                    continue
                if not isinstance(item, dict):
                    continue
                text = item.get("text")
                if isinstance(text, str):
                    pieces.append(text)
    return "".join(pieces)


def _consume_sse_stream(response, output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        for raw_line in response.iter_lines(decode_unicode=True):
            if not raw_line:
                continue
            line = raw_line.strip()
            if not line or not line.startswith("data:"):
                continue

            payload_text = line[5:].strip()
            if payload_text == "[DONE]":
                break

            try:
                payload = json.loads(payload_text)
            except json.JSONDecodeError:
                continue

            chunk = _extract_text_from_chunk(payload)
            if chunk:
                handle.write(chunk)
                handle.flush()


def _strip_markdown_fences(content: str) -> str:
    text = content.strip()
    if text.startswith("```"):
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]
        if text.endswith("```"):
            text = text[:-3]
    return text.strip() + "\n"


def _validate_existing_html(prompt_path: Path, html_path: Path) -> Path:
    print("[INFO] HTML 步骤当前使用 agent 手工模式")
    print(f"[INFO] 请阅读 {prompt_path}")
    print("[INFO] 请结合 web skill 与 frontend-design skill 生成单文件 HTML")
    print(f"[INFO] 最终文件路径: {html_path}")

    if not html_path.exists() or html_path.stat().st_size == 0:
        sys.exit(
            "[ERROR] 未检测到有效的 src/index.html。"
            "请先由当前 agent 根据 prompt.md 完成 HTML 生成"
        )

    print(f"[OK] 检测到现有 index.html: {html_path}")
    return html_path


def _generate_html_via_api(
    task_dir: Path,
    root: Path,
    api_provider: str,
    base_url_env: str,
    api_key_env: str,
    model_env: str,
    extra_instruction: str = "",
) -> Path:
    if api_provider != "openai-compatible":
        sys.exit(f"[ERROR] 暂不支持的 API provider: {api_provider}")

    env_path = root / ".env.local"
    env_values = _load_env_file(env_path)
    base_url = _require_config(env_values, base_url_env).rstrip("/")
    api_key = _require_config(env_values, api_key_env)
    model = _require_config(env_values, model_env)

    prompt_path = task_dir / "prompt.md"
    html_path = task_dir / "src" / "index.html"
    temp_path = html_path.with_suffix(".streaming.tmp")
    html_path.parent.mkdir(parents=True, exist_ok=True)

    prompt_content = _merge_prompt_with_extra_instruction(
        prompt_path.read_text(encoding="utf-8-sig"),
        extra_instruction,
    )
    payload = {
        "model": model,
        "stream": True,
        "messages": _build_messages(prompt_content),
    }

    request_headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        ),
        "Origin": base_url.rsplit("/", 1)[0],
        "Referer": f"{base_url.rsplit('/', 1)[0]}/",
    }

    print("[INFO] HTML 步骤切换为外部 API 流式生成模式")
    print(f"[INFO] prompt: {prompt_path}")
    print(f"[INFO] output: {html_path}")
    print(f"[INFO] provider: {api_provider}")
    print(f"[INFO] base url env: {base_url_env}")
    print(f"[INFO] model env: {model_env}")
    if extra_instruction.strip():
        print("[INFO] 已附加额外运行时风格指令")
    print("[INFO] 正在以 stream=true 调用外部 API 并流式写入 HTML...")

    try:
        with requests.post(
            f"{base_url}/chat/completions",
            headers=request_headers,
            json=payload,
            stream=True,
            timeout=600,
        ) as response:
            if response.status_code >= 400:
                detail = response.text
                if temp_path.exists():
                    temp_path.unlink()
                sys.exit(f"[ERROR] 外部 API 请求失败: HTTP {response.status_code}\n{detail}")

            _consume_sse_stream(response, temp_path)
    except requests.RequestException as exc:
        if temp_path.exists():
            temp_path.unlink()
        sys.exit(f"[ERROR] 外部 API 请求失败: {exc}")

    if not temp_path.exists() or temp_path.stat().st_size == 0:
        sys.exit("[ERROR] 流式响应结束，但没有收到任何 HTML 内容")

    cleaned = _strip_markdown_fences(temp_path.read_text(encoding="utf-8"))
    if "<html" not in cleaned.lower() and "<!doctype" not in cleaned.lower():
        print("[WARN] 生成结果中未明显检测到完整 HTML 外壳，请人工检查输出")

    html_path.write_text(cleaned, encoding="utf-8", newline="\n")
    temp_path.unlink(missing_ok=True)

    print(f"[OK] 已通过流式 API 生成 index.html: {html_path}")
    return html_path


def generate_html(
    task_dir: Path,
    root: Path | None = None,
    mode: str = "manual",
    api_provider: str = "openai-compatible",
    base_url_env: str = DEFAULT_BASE_URL_ENV,
    api_key_env: str = DEFAULT_API_KEY_ENV,
    model_env: str = DEFAULT_MODEL_ENV,
    extra_instruction: str = "",
) -> Path:
    """在手工模式下校验 HTML，在 API 模式下流式生成 HTML。"""
    root = root or Path(__file__).resolve().parent.parent.parent.parent

    prompt_path = task_dir / "prompt.md"
    html_path = task_dir / "src" / "index.html"

    if not prompt_path.exists():
        sys.exit(f"[ERROR] {prompt_path} 不存在，请先生成 prompt.md")

    if mode == "manual":
        return _validate_existing_html(prompt_path, html_path)
    if mode == "api":
        return _generate_html_via_api(
            task_dir=task_dir,
            root=root,
            api_provider=api_provider,
            base_url_env=base_url_env,
            api_key_env=api_key_env,
            model_env=model_env,
            extra_instruction=extra_instruction,
        )

    sys.exit(f"[ERROR] 未知 HTML 模式: {mode}")


def main():
    parser = argparse.ArgumentParser(
        description="校验或流式生成 index.html",
    )
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument(
        "--mode",
        choices=["manual", "api"],
        default="manual",
        help="manual=仅校验现有 HTML；api=显式启用外部 API 流式生成",
    )
    parser.add_argument(
        "--api-provider",
        choices=["openai-compatible"],
        default="openai-compatible",
        help="外部 API 类型",
    )
    parser.add_argument(
        "--base-url-env",
        default=DEFAULT_BASE_URL_ENV,
        help=f"在 .env.local 中读取 base url 的变量名，默认 {DEFAULT_BASE_URL_ENV}",
    )
    parser.add_argument(
        "--api-key-env",
        default=DEFAULT_API_KEY_ENV,
        help=f"在 .env.local 中读取 api key 的变量名，默认 {DEFAULT_API_KEY_ENV}",
    )
    parser.add_argument(
        "--model-env",
        default=DEFAULT_MODEL_ENV,
        help=f"在 .env.local 中读取 model 的变量名，默认 {DEFAULT_MODEL_ENV}",
    )
    parser.add_argument(
        "--extra-instruction",
        default="",
        help="附加到 prompt.md 之后的运行时指令，仅影响本次生成",
    )
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    if not task_dir.exists():
        sys.exit(f"[ERROR] 任务目录 {task_dir} 不存在")

    generate_html(
        task_dir=task_dir,
        root=root,
        mode=args.mode,
        api_provider=args.api_provider,
        base_url_env=args.base_url_env,
        api_key_env=args.api_key_env,
        model_env=args.model_env,
        extra_instruction=args.extra_instruction,
    )


if __name__ == "__main__":
    main()
