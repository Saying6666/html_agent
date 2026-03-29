#!/usr/bin/env python3
"""
generate_html_claude.py — 兼容旧入口

说明:
    该文件保留为兼容入口，不再绑定特定模型。
    如需外部模型流式生成 HTML，请改用:

    python generate_html.py --task fdu_012 --mode api
"""

import argparse
from pathlib import Path

from generate_html import generate_html


def main():
    parser = argparse.ArgumentParser(description="兼容旧的 HTML 外部生成入口")
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument(
        "--api-provider",
        choices=["openai-compatible"],
        default="openai-compatible",
        help="外部 API 类型",
    )
    parser.add_argument("--base-url-env", default="X666_BASE_URL",
                        help="在 .env.local 中读取 base url 的变量名")
    parser.add_argument("--api-key-env", default="X666_API_KEY",
                        help="在 .env.local 中读取 API key 的变量名")
    parser.add_argument("--model-env", default="X666_MODEL_GEMINI",
                        help="在 .env.local 中读取 model 的变量名")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    print(
        "[WARN] generate_html_claude.py 仅作为兼容入口保留；"
        "当前将转发到 generate_html.py 的 API 流式模式。"
    )

    generate_html(
        task_dir=root / args.task,
        root=root,
        mode="api",
        api_provider=args.api_provider,
        base_url_env=args.base_url_env,
        api_key_env=args.api_key_env,
        model_env=args.model_env,
    )


if __name__ == "__main__":
    main()
