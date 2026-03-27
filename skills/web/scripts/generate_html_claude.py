#!/usr/bin/env python3
"""
generate_html_claude.py — 已废弃

说明:
    Web skill 的 HTML 步骤不再通过 Claude CLI 或任何外部模型调用生成。
    src/index.html 必须由当前读取 web skill 的 agent 根据 prompt.md
    并结合 frontend-design skill 直接编写。
"""

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="已废弃的 HTML 生成入口")
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    prompt_path = task_dir / "prompt.md"
    html_path = task_dir / "src" / "index.html"

    if not prompt_path.exists():
        sys.exit(f"[ERROR] {prompt_path} 不存在，请先生成 prompt.md")

    sys.exit(
        "[ERROR] generate_html_claude.py 已废弃。"
        f"请让当前 agent 阅读 {prompt_path}，并将最终 HTML 写入 {html_path}"
    )


if __name__ == "__main__":
    main()
