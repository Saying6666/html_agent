#!/usr/bin/env python3
"""
process_task.py — 处理单个任务的半自动流程

说明:
    prompt.md 必须由当前读取 web skill 的 agent 手工生成；
    src/index.html 默认由当前读取 web skill 的 agent 根据 prompt.md
    并结合 frontend-design skill 手工生成；
    仅当用户明确要求时，才允许切换到外部 API 流式生成模式。

用法:
    python process_task.py fdu_012
    python process_task.py fdu_012 --html-mode api
"""

import argparse
import sys
from pathlib import Path

# 导入现有模块
sys.path.insert(0, str(Path(__file__).resolve().parent))
from capture_screenshot import capture_screenshot
from capture_video import capture_video
from generate_html import generate_html
from generate_prompt import generate_prompt


def _ensure_task_dirs(task_dir: Path):
    task_dir.mkdir(parents=True, exist_ok=True)
    (task_dir / "src").mkdir(exist_ok=True)


def _print_html_generation_instructions(task_dir: Path, html_mode: str):
    prompt_path = task_dir / "prompt.md"
    html_path = task_dir / "src" / "index.html"

    if html_mode == "manual":
        print("[ACTION REQUIRED] index.html 需由当前 agent 手工生成。")
        print(f"  - 阅读 {prompt_path}")
        print("  - 结合 web skill 与 frontend-design skill 完成设计与实现")
        print(f"  - 将最终单文件 HTML 写入 {html_path}")
        return

    print("[ACTION REQUIRED] index.html 将通过外部 API 流式生成。")
    print("[ACTION REQUIRED] 仅在用户明确要求时使用该模式。")
    print(f"  - 读取 {prompt_path}")
    print("  - 通过 OpenAI 兼容接口以 stream=true 获取 HTML")
    print(f"  - 将流式结果写入 {html_path}")


def process_task(
    task_id: str,
    root: Path,
    auto_prompt: bool = False,
    html_mode: str = "manual",
    api_provider: str = "openai-compatible",
    base_url_env: str = "X666_BASE_URL",
    api_key_env: str = "X666_API_KEY",
    model_env: str = "X666_MODEL_GEMINI",
    html_extra_instruction: str = "",
):
    """处理单个任务的完整流程。"""
    task_dir = root / task_id
    _ensure_task_dirs(task_dir)

    print(f"\n{'=' * 60}")
    print(f"  处理任务: {task_id}")
    print(f"{'=' * 60}\n")

    print("--- [1/4] 校验 prompt.md ---")
    if auto_prompt:
        print("[INFO] --auto-prompt 已废弃并被忽略；prompt.md 需由当前 agent 手工生成。")
    generate_prompt(task_dir=task_dir, root=root)

    print("\n--- [2/4] 生成 index.html ---")
    _print_html_generation_instructions(task_dir, html_mode)
    generate_html(
        task_dir=task_dir,
        root=root,
        mode=html_mode,
        api_provider=api_provider,
        base_url_env=base_url_env,
        api_key_env=api_key_env,
        model_env=model_env,
        extra_instruction=html_extra_instruction,
    )

    if not (task_dir / "preview.png").exists():
        print("\n--- [3/4] 全页截图 ---")
        capture_screenshot(task_dir=task_dir)
    else:
        print("[SKIP] preview.png 已存在")

    if not (task_dir / "video.mp4").exists():
        print("\n--- [4/4] 自动录屏 ---")
        capture_video(task_dir=task_dir, duration=35)
    else:
        print("[SKIP] video.mp4 已存在")

    print(f"\n[DONE] {task_id} 完成!")
    return True


def main():
    parser = argparse.ArgumentParser(description="处理单个任务")
    parser.add_argument("task_id", help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument(
        "--auto-prompt",
        action="store_true",
        help="兼容旧参数，现已忽略；prompt.md 需手工生成",
    )
    parser.add_argument(
        "--html-mode",
        choices=["manual", "api"],
        default="manual",
        help="manual=当前 agent 手工写 HTML；api=显式启用外部 API 流式生成",
    )
    parser.add_argument(
        "--api-provider",
        choices=["openai-compatible"],
        default="openai-compatible",
        help="HTML 外部 API 类型",
    )
    parser.add_argument("--base-url-env", default="X666_BASE_URL",
                        help="在 .env.local 中读取 base url 的变量名")
    parser.add_argument("--api-key-env", default="X666_API_KEY",
                        help="在 .env.local 中读取 API key 的变量名")
    parser.add_argument("--model-env", default="X666_MODEL_GEMINI",
                        help="在 .env.local 中读取 model 的变量名")
    parser.add_argument(
        "--html-extra-instruction",
        default="",
        help="附加到 prompt.md 之后的运行时 HTML 指令，仅影响本次生成",
    )
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    try:
        process_task(
            args.task_id,
            root,
            auto_prompt=args.auto_prompt,
            html_mode=args.html_mode,
            api_provider=args.api_provider,
            base_url_env=args.base_url_env,
            api_key_env=args.api_key_env,
            model_env=args.model_env,
            html_extra_instruction=args.html_extra_instruction,
        )
    except Exception as e:
        print(f"[ERROR] {args.task_id} 失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
