#!/usr/bin/env python3
"""
process_task.py — 处理单个任务的半自动流程

说明:
    prompt.md 可由脚本生成；
    src/index.html 必须由当前读取 web skill 的 agent 根据 prompt.md
    并结合 frontend-design skill 手工生成。

用法:
    python process_task.py fdu_012
    python process_task.py fdu_012 --auto-prompt
"""

import argparse
import sys
from pathlib import Path

# 导入现有模块
sys.path.insert(0, str(Path(__file__).resolve().parent))
from capture_screenshot import capture_screenshot
from capture_video import capture_video
from generate_prompt import generate_prompt


def _ensure_task_dirs(task_dir: Path):
    task_dir.mkdir(parents=True, exist_ok=True)
    (task_dir / "src").mkdir(exist_ok=True)


def _print_html_generation_instructions(task_dir: Path):
    prompt_path = task_dir / "prompt.md"
    html_path = task_dir / "src" / "index.html"

    print("[ACTION REQUIRED] index.html 需由当前 agent 手工生成。")
    print(f"  - 阅读 {prompt_path}")
    print("  - 结合 web skill 与 frontend-design skill 完成设计与实现")
    print(f"  - 将最终单文件 HTML 写入 {html_path}")


def process_task(task_id: str, root: Path, auto_prompt: bool = False):
    """处理单个任务的完整流程。"""
    task_dir = root / task_id
    _ensure_task_dirs(task_dir)

    print(f"\n{'=' * 60}")
    print(f"  处理任务: {task_id}")
    print(f"{'=' * 60}\n")

    prompt_path = task_dir / "prompt.md"
    if not prompt_path.exists() or prompt_path.stat().st_size == 0:
        if not auto_prompt:
            raise RuntimeError(
                "prompt.md 不存在。请先提供 prompt.md，或使用 --auto-prompt 生成 prompt"
            )

        print("--- [1/4] 生成 prompt.md ---")
        generate_prompt(task_dir=task_dir, root=root, auto=True)
    else:
        print("[SKIP] prompt.md 已存在")

    print("\n--- [2/4] 生成 index.html ---")
    _print_html_generation_instructions(task_dir)

    html_path = task_dir / "src" / "index.html"
    if not html_path.exists() or html_path.stat().st_size == 0:
        raise RuntimeError(
            "src/index.html 不存在或为空。请先由当前 agent 根据 prompt.md 完成 HTML 生成"
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
        help="当 prompt.md 不存在时，自动生成网站 brief 和 prompt.md",
    )
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    try:
        process_task(args.task_id, root, auto_prompt=args.auto_prompt)
    except Exception as e:
        print(f"[ERROR] {args.task_id} 失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
