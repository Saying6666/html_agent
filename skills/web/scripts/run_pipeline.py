#!/usr/bin/env python3
"""
run_pipeline.py — Web Design Dataset 流水线入口

用法:
    # 手工模式：prompt 与 HTML 都由当前 agent 编写
    python run_pipeline.py --task fdu_012 --steps prompt,html

    # 显式启用外部 API 流式生成 HTML
    python run_pipeline.py --task fdu_012 --steps html --html-mode api

    # 仅执行某些步骤
    python run_pipeline.py --task fdu_012 --steps prompt
    python run_pipeline.py --task fdu_012 --steps html
    python run_pipeline.py --task fdu_012 --steps screenshot,video

    # 批量校验 prompt / HTML 是否已就绪
    python run_pipeline.py --batch fdu_012,fdu_013,fdu_014 --steps prompt,html
    python run_pipeline.py --range 12-20 --steps prompt,html
"""

import argparse
import sys
import time
from pathlib import Path

# 添加当前脚本目录到 path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_prompt import generate_prompt
from generate_html import generate_html
from capture_screenshot import capture_screenshot
from capture_video import capture_video

ALL_STEPS = ["prompt", "html", "screenshot", "video"]


def _print_prompt_generation_instructions(task_dir: Path):
    """提示 prompt 步骤改为由当前 agent 手工完成。"""
    prompt_path = task_dir / "prompt.md"

    print("[ACTION REQUIRED] Prompt 步骤不再调用外部 API 或脚本模型。")
    print("[ACTION REQUIRED] 请由当前 agent 执行以下工作：")
    print("  1. 按原有要求手工编写 4 轮渐进式 prompt")
    print("  2. 保持原 prompt 结构和约束不变")
    print(f"  3. 将最终内容写入 {prompt_path}")
    print("  4. 完成后再继续 HTML / screenshot / video 步骤")


def _print_html_generation_instructions(task_dir: Path, html_mode: str):
    """提示 HTML 步骤的当前执行模式。"""
    prompt_path = task_dir / "prompt.md"
    html_path = task_dir / "src" / "index.html"

    if html_mode == "manual":
        print("[ACTION REQUIRED] HTML 步骤当前为 agent 手工模式。")
        print("[ACTION REQUIRED] 请由当前 agent 执行以下工作：")
        print(f"  1. 阅读 {prompt_path}")
        print("  2. 结合 web skill 与 frontend-design skill 设计并编写单文件 HTML")
        print(f"  3. 将最终代码写入 {html_path}")
        print("  4. 完成后再继续 screenshot / video 步骤")
        return

    print("[ACTION REQUIRED] HTML 步骤当前为外部 API 流式模式。")
    print("[ACTION REQUIRED] 仅在用户明确要求时使用该模式。")
    print(f"  1. 读取 {prompt_path}")
    print("  2. 通过 OpenAI 兼容接口以 stream=true 生成 HTML")
    print(f"  3. 将流式结果落盘到 {html_path}")
    print("  4. 完成后再继续 screenshot / video 步骤")


def _resolve_tasks(args) -> list:
    """解析任务列表。"""
    tasks = []
    if hasattr(args, "batch") and args.batch:
        tasks = [t.strip() for t in args.batch.split(",")]
    elif hasattr(args, "range") and args.range:
        parts = args.range.split("-")
        start, end = int(parts[0]), int(parts[1])
        tasks = [f"fdu_{i:03d}" for i in range(start, end + 1)]
    elif args.task:
        tasks = [args.task]
    return tasks


def run_pipeline(task_id: str, root: Path, steps: list,
                 auto: bool = False, category: str = "",
                 concept: str = "", audience: str = "",
                 style: str = "", site_name: str = "",
                 video_duration: int = 35,
                 html_mode: str = "manual",
                 api_provider: str = "openai-compatible",
                 base_url_env: str = "X666_BASE_URL",
                 api_key_env: str = "X666_API_KEY",
                 model_env: str = "X666_MODEL_GEMINI",
                 html_extra_instruction: str = ""):
    """对单个任务执行流水线。"""
    task_dir = root / task_id
    if not task_dir.exists():
        task_dir.mkdir(parents=True)
        (task_dir / "src").mkdir(exist_ok=True)
        print(f"[INFO] 创建任务目录 {task_dir}")

    print(f"\n{'='*60}")
    print(f"  任务: {task_id}")
    print(f"  步骤: {', '.join(steps)}")
    print(f"  HTML 模式: {html_mode}")
    print(f"{'='*60}\n")

    start = time.time()

    # Step 1: 校验 prompt
    if "prompt" in steps:
        print(f"\n--- [1/4] 校验 prompt.md ---")
        _print_prompt_generation_instructions(task_dir)
        generate_prompt(
            task_dir=task_dir, root=root,
            category=category, concept=concept,
            audience=audience, style=style,
            site_name=site_name, auto=auto,
        )

    # Step 2: 生成 HTML
    if "html" in steps:
        print(f"\n--- [2/4] 生成 index.html ---")
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

    # Step 3: 截图
    if "screenshot" in steps:
        print(f"\n--- [3/4] 全页截图 ---")
        capture_screenshot(task_dir=task_dir)

    # Step 4: 录屏
    if "video" in steps:
        print(f"\n--- [4/4] 自动录屏 ---")
        capture_video(task_dir=task_dir, duration=video_duration)

    elapsed = time.time() - start
    print(f"\n[DONE] {task_id} 完成，耗时 {elapsed:.1f}s")

    # 检查交付物完整性
    _check_deliverables(task_dir, task_id)


def _check_deliverables(task_dir: Path, task_id: str):
    """检查交付物完整性。"""
    required = {
        "prompt.md": task_dir / "prompt.md",
        "src/index.html": task_dir / "src" / "index.html",
        "preview.png": task_dir / "preview.png",
        "video.mp4": task_dir / "video.mp4",
    }

    print(f"\n--- 交付物检查 ({task_id}) ---")
    all_ok = True
    for name, path in required.items():
        if path.exists() and path.stat().st_size > 0:
            size = path.stat().st_size
            unit = "KB" if size < 1024 * 1024 else "MB"
            val = size / 1024 if unit == "KB" else size / 1024 / 1024
            print(f"  [OK] {name:20s} ({val:.1f} {unit})")
        else:
            print(f"  [!!] {name:20s} 缺失或为空")
            all_ok = False

    if all_ok:
        print(f"  >>> {task_id} 交付物完整!")
    else:
        print(f"  >>> {task_id} 交付物不完整，请检查")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Web Design Dataset 全流水线",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # 任务选择
    task_group = parser.add_mutually_exclusive_group(required=True)
    task_group.add_argument("--task", help="单个任务 ID，如 fdu_012")
    task_group.add_argument("--batch", help="批量任务，逗号分隔，如 fdu_012,fdu_013")
    task_group.add_argument("--range", help="任务范围，如 12-20")

    # 步骤选择
    parser.add_argument("--steps", default=None,
                        help="执行步骤，逗号分隔 (prompt,html,screenshot,video)")

    # prompt 参数（保留兼容，现已忽略）
    parser.add_argument("--auto", action="store_true", help="兼容旧参数，现已忽略")
    parser.add_argument("--category", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--concept", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--audience", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--style", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--site-name", default="", help="兼容旧参数，现已忽略")

    # 其他参数
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument("--video-duration", type=int, default=35,
                        help="视频目标时长 (默认 35s)")
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

    # 解析根目录
    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    # 解析步骤
    if args.steps:
        steps = [s.strip() for s in args.steps.split(",")]
        for s in steps:
            if s not in ALL_STEPS:
                sys.exit(f"[ERROR] 未知步骤 '{s}'，可选: {ALL_STEPS}")
    else:
        steps = ALL_STEPS

    # 解析任务列表
    tasks = _resolve_tasks(args)
    if not tasks:
        sys.exit("[ERROR] 未指定任务")

    print(f"[INFO] 共 {len(tasks)} 个任务: {', '.join(tasks)}")
    print(f"[INFO] 步骤: {', '.join(steps)}")
    print(f"[INFO] HTML 模式: {args.html_mode}")

    for i, task_id in enumerate(tasks):
        print(f"\n{'#'*60}")
        print(f"  [{i+1}/{len(tasks)}] {task_id}")
        print(f"{'#'*60}")

        try:
            run_pipeline(
                task_id=task_id, root=root, steps=steps,
                auto=args.auto,
                category=args.category, concept=args.concept,
                audience=args.audience, style=args.style,
                site_name=getattr(args, "site_name", ""),
                video_duration=args.video_duration,
                html_mode=args.html_mode,
                api_provider=args.api_provider,
                base_url_env=args.base_url_env,
                api_key_env=args.api_key_env,
                model_env=args.model_env,
                html_extra_instruction=args.html_extra_instruction,
            )
        except Exception as e:
            print(f"[ERROR] {task_id} 失败: {e}")
            if len(tasks) == 1:
                raise
            print("[INFO] 继续处理下一个任务...")
            continue

    print(f"\n{'='*60}")
    print(f"  全部完成! 共 {len(tasks)} 个任务")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
