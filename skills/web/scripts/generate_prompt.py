#!/usr/bin/env python3
"""
generate_prompt.py — 生成 4 轮格式化 prompt.md

用法:
    python generate_prompt.py --task fdu_012 --category "SaaS Landing Page" \
        --concept "AI-powered code review tool" --audience "Software teams" \
        --style "Modern Minimal"

    python generate_prompt.py --task fdu_012 --auto
        (使用 AI 自动生成所有参数)
"""

import argparse
import json
import os
import sys
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def _load_env(env_path: Path) -> dict:
    """从 .env.local 加载环境变量。"""
    env = {}
    if env_path.exists():
        content = env_path.read_text(encoding="utf-8-sig")
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def _api_config(root: Path) -> tuple:
    """返回 (base_url, api_key, model)。"""
    env = _load_env(root / ".env.local")
    base_url = os.environ.get("X666_BASE_URL", env.get("X666_BASE_URL", ""))
    api_key = os.environ.get("X666_API_KEY", env.get("X666_API_KEY", ""))
    model = os.environ.get("X666_MODEL_GEMINI", env.get("X666_MODEL_GEMINI", ""))
    if not all([base_url, api_key, model]):
        sys.exit("[ERROR] 缺少 API 配置，请检查 .env.local")
    return base_url, api_key, model


import time as _time

def _chat_stream(base_url: str, api_key: str, model: str,
                messages: list, temperature: float = 0.9):
    """流式 chat completions，yield content chunks。"""
    url = f"{base_url.rstrip('/')}/chat/completions"
    max_retries = 5
    delay = 2
    resp = None

    for attempt in range(max_retries):
        try:
            resp = requests.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                },
                json={
                    "model": model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": 16000,
                    "stream": True,
                },
                stream=True,
                timeout=180,
                proxies={"http": None, "https": None},
            )
            if resp.status_code != 200:
                sys.exit(f"[ERROR] API {resp.status_code}: {resp.text[:500]}")
            break
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            if attempt < max_retries - 1:
                print(f"  [RETRY] 连接失败，{delay}s 后重试 ({attempt + 1}/{max_retries})...")
                _time.sleep(delay)
                delay *= 2
            else:
                raise e

    for line in resp.iter_lines(decode_unicode=True):
        if not line:
            continue
        line = line.strip()
        if not line.startswith("data:"):
            continue
        data_str = line[5:].strip()
        if data_str == "[DONE]":
            return
        try:
            data = json.loads(data_str)
            delta = data["choices"][0].get("delta", {})
            content = delta.get("content", "")
            if content:
                yield content
        except (json.JSONDecodeError, KeyError, IndexError):
            continue


# ---------------------------------------------------------------------------
# Prompt generation
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
你是一个专业的 Web Design Dataset 提示词工程师。
你需要为一个单页 HTML 网站生成高质量的 4 轮渐进式设计提示词 (prompt)。

生成规则：
1. 输出必须是纯 Markdown，包含 4 个 Round
2. Round 1: 角色定义 + 设计系统(CSS :root 变量) + 页面板块结构（至少10个section）
3. Round 2: 交互 + 动效（至少 8 种功能交互，包含四态定义）
4. Round 3: 响应式 + 无障碍（4 个断点 + ARIA + 键盘导航 + prefers-reduced-motion）
5. Round 4: 最终打磨 + 验收清单（checklist）
6. 设计系统必须包含完整的 CSS :root 变量定义（颜色、字体、布局、过渡）
7. 交互必须包含: Modal, Accordion, Toast, Tabs, Scroll Reveal, Stagger Animation, Count-up, Navbar scroll transition
8. 每种交互要有完整的 ARIA 说明
9. 所有按钮和卡片必须有 Default/Hover/Active/Focus 四态定义
10. 技术约束: 单文件 index.html，内联 CSS/JS，禁止框架，禁止本地资源
11. 风格必须对标真实 2025-2026 产品站，不是课堂 demo
12. Round 4 结尾必须要求模型生成最终代码

格式参考:
## Round 1 — Role + Design System + Page Structure
## Round 2 — Interaction + Motion
## Round 3 — Responsive + Accessibility
## Round 4 — Polish + Acceptance Self-Check

不要输出任何解释，只输出 prompt.md 的内容。"""


def _build_user_msg(category: str, concept: str, audience: str,
                    style: str, site_name: str) -> str:
    return f"""\
请为以下网站生成 4 轮渐进式提示词:

- **网站名称**: {site_name}
- **类别**: {category}
- **概念**: {concept}
- **目标受众**: {audience}
- **视觉风格方向**: {style}

请确保:
- 设计系统配色与概念匹配，有完整的 CSS :root 变量
- 板块设计具体且丰富（至少 10 个 section）
- 交互设计炫酷且多样（至少 8 种功能交互）
- 每个 Round 的内容充实、专业
- Round 4 末尾必须要求 "GENERATE THE FINAL CODE NOW" 并列出完整验收清单"""


def _auto_brief(base_url: str, api_key: str, model: str) -> dict:
    """用 AI 自动生成网站 brief。"""
    messages = [
        {"role": "system", "content": (
            "你是创意总监。请生成一个独特的单页网站创意。"
            "输出纯 JSON，不要 markdown code fence。"
            "字段: category, concept, audience, style, site_name"
            "\n示例: {\"category\": \"SaaS Landing Page\", "
            "\"concept\": \"AI-powered code review tool for enterprise teams\", "
            "\"audience\": \"Engineering managers and CTOs\", "
            "\"style\": \"Clean Corporate with gradient accents\", "
            "\"site_name\": \"CodeSight\"}"
        )},
        {"role": "user", "content": (
            "生成一个新的、独特的网站创意。"
            "类别可以是: SaaS, Portfolio, Agency, E-commerce, Blog, "
            "Dashboard, Restaurant, Fitness, Travel, Education, "
            "Fintech, Healthcare, Music, NFT, AI Tool 等任意类别。"
            "确保概念具体、有创意，不要与常见模板雷同。"
        )}
    ]
    # 流式收集完整内容
    full_text = ""
    for chunk in _chat_stream(base_url, api_key, model, messages, temperature=1.0):
        full_text += chunk
    full_text = full_text.strip()
    if full_text.startswith("```"):
        full_text = full_text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(full_text)


def generate_prompt(task_dir: Path, root: Path,
                    category: str = "", concept: str = "",
                    audience: str = "", style: str = "",
                    site_name: str = "", auto: bool = False) -> Path:
    """生成 prompt.md 并写入 task_dir。"""
    base_url, api_key, model = _api_config(root)

    if auto:
        print("[INFO] 自动生成网站 brief...")
        brief = _auto_brief(base_url, api_key, model)
        category = brief.get("category", category)
        concept = brief.get("concept", concept)
        audience = brief.get("audience", audience)
        style = brief.get("style", style)
        site_name = brief.get("site_name", site_name)
        print(f"  类别: {category}")
        print(f"  概念: {concept}")
        print(f"  受众: {audience}")
        print(f"  风格: {style}")
        print(f"  名称: {site_name}")
        print("  [WAIT] 等待 3 秒后生成 prompt...")
        import time as _time
        _time.sleep(3)

    if not all([category, concept, audience, style, site_name]):
        sys.exit("[ERROR] 缺少必要参数。使用 --auto 或提供所有参数")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": _build_user_msg(
            category, concept, audience, style, site_name
        )},
    ]

    print("[INFO] 正在流式生成 prompt.md ...")
    content = ""
    char_count = 0
    for chunk in _chat_stream(base_url, api_key, model, messages):
        content += chunk
        char_count += len(chunk)
        if char_count % 500 < len(chunk):
            print(f"\r[STREAM] 已接收 {char_count} 字符...", end="", flush=True)
    print(f"\r[STREAM] 总计接收 {char_count} 字符      ")

    prompt_path = task_dir / "prompt.md"
    prompt_path.write_text(content, encoding="utf-8")
    print(f"[OK] prompt.md 已写入 {prompt_path}")
    return prompt_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="生成 4 轮 prompt.md")
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument("--auto", action="store_true", help="自动生成网站 brief")
    parser.add_argument("--category", default="", help="网站类别")
    parser.add_argument("--concept", default="", help="网站概念")
    parser.add_argument("--audience", default="", help="目标受众")
    parser.add_argument("--style", default="", help="视觉风格方向")
    parser.add_argument("--site-name", default="", help="网站名称")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    if not task_dir.exists():
        task_dir.mkdir(parents=True)
        (task_dir / "src").mkdir(exist_ok=True)
        print(f"[INFO] 创建任务目录 {task_dir}")

    generate_prompt(
        task_dir=task_dir,
        root=root,
        category=args.category,
        concept=args.concept,
        audience=args.audience,
        style=args.style,
        site_name=args.site_name,
        auto=args.auto,
    )


if __name__ == "__main__":
    main()
