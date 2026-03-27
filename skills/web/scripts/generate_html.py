#!/usr/bin/env python3
"""
generate_html.py — HTML 生成步骤说明器

说明:
    该步骤不再调用外部 API 生成 index.html。
    src/index.html 必须由当前读取 web skill 的 agent 根据 prompt.md
    并结合 frontend-design skill 手工生成。

用法:
    python generate_html.py --task fdu_012
"""

import argparse
import sys
from pathlib import Path


def generate_html(task_dir: Path, root: Path | None = None) -> Path:
    """校验 index.html 是否已由当前 agent 生成。"""
    del root

    prompt_path = task_dir / "prompt.md"
    html_path = task_dir / "src" / "index.html"

    if not prompt_path.exists():
        sys.exit(f"[ERROR] {prompt_path} 不存在，请先生成 prompt.md")

    print("[INFO] HTML 步骤已切换为 agent 手工生成模式")
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


def main():
    parser = argparse.ArgumentParser(description="校验 index.html 是否已生成")
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    if not task_dir.exists():
        sys.exit(f"[ERROR] 任务目录 {task_dir} 不存在")

    generate_html(task_dir, root)


if __name__ == "__main__":
    main()
