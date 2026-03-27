#!/usr/bin/env python3
"""
capture_video.py — 使用 Playwright 对 index.html 进行自动录屏

功能:
    1. 打开页面，等待加载
    2. 平滑滚动到底部
    3. 滚动过程中尝试点击可交互控件 (tabs, accordion, modal 等)
    4. 录制 20-60 秒，24fps
    5. 输出 video.mp4

用法:
    python capture_video.py --task fdu_012
    python capture_video.py --task fdu_012 --duration 40

依赖:
    pip install playwright && playwright install chromium
    ffmpeg (需要在 PATH 中)
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("[ERROR] 请先安装 playwright: pip install playwright && playwright install chromium")


def _check_ffmpeg():
    """检查 ffmpeg 是否可用。"""
    if not shutil.which("ffmpeg"):
        sys.exit("[ERROR] 未找到 ffmpeg，请安装并确保在 PATH 中")


def _try_click_interactive(page, pause: float = 1.2):
    """尝试点击页面上的可交互控件。"""
    interactions = [
        # Tabs: 点击非激活的 tab
        {
            "selector": '[role="tab"]:not([aria-selected="true"]):not(.active)',
            "description": "tab 切换",
            "max_clicks": 2,
        },
        # Accordion: 点击折叠面板触发器
        {
            "selector": '[aria-expanded="false"], .accordion-trigger, .accordion-header, '
                        'details:not([open]) summary, .faq-question, [data-accordion]',
            "description": "accordion 展开",
            "max_clicks": 2,
        },
        # Modal: 尝试打开模态框然后关闭
        {
            "selector": '[data-modal-trigger], [data-lightbox], .modal-trigger, '
                        '.lightbox-trigger, .project-card img, .gallery-item',
            "description": "modal 打开",
            "max_clicks": 1,
            "close_after": True,
        },
        # Buttons with hover effects
        {
            "selector": 'button[type="button"]:not([aria-label*="close"]):not(.close)',
            "description": "按钮点击",
            "max_clicks": 1,
        },
    ]

    for interaction in interactions:
        try:
            elements = page.query_selector_all(interaction["selector"])
            if not elements:
                continue

            clicked = 0
            for el in elements:
                if clicked >= interaction["max_clicks"]:
                    break
                try:
                    if el.is_visible():
                        # 先滚动到元素位置
                        el.scroll_into_view_if_needed()
                        time.sleep(0.3)
                        el.click()
                        clicked += 1
                        print(f"  [CLICK] {interaction['description']}")
                        time.sleep(pause)

                        # 如果需要关闭 (modal)
                        if interaction.get("close_after"):
                            time.sleep(1.5)
                            # 尝试按 Escape 关闭
                            page.keyboard.press("Escape")
                            time.sleep(0.8)
                except Exception:
                    continue
        except Exception:
            continue


def capture_video(task_dir: Path, duration: int = 35, width: int = 1920,
                  height: int = 1080, fps: int = 24) -> Path:
    """录制页面浏览视频。"""
    _check_ffmpeg()

    html_path = task_dir / "src" / "index.html"
    if not html_path.exists():
        sys.exit(f"[ERROR] {html_path} 不存在")

    file_url = html_path.resolve().as_uri()
    output_path = task_dir / "video.mp4"

    # 约束时长在 20-60 秒
    duration = max(20, min(60, duration))

    print(f"[INFO] 正在录屏 {html_path}")
    print(f"  URL: {file_url}")
    print(f"  分辨率: {width}x{height}")
    print(f"  目标时长: {duration}s, {fps}fps")

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_video = Path(tmp_dir) / "raw.webm"

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": width, "height": height},
                record_video_dir=str(tmp_dir),
                record_video_size={"width": width, "height": height},
            )
            page = context.new_page()

            # 加载页面
            page.goto(file_url, wait_until="networkidle")
            time.sleep(3)  # 等待初始加载和动画

            # ---- 录制开始 ----
            start_time = time.time()

            # 阶段 1: 静态展示首屏 (3秒)
            time.sleep(3)

            # 阶段 2: 缓慢滚动到底部
            total_height = page.evaluate("document.body.scrollHeight")
            viewport_height = height
            scroll_distance = total_height - viewport_height

            # 计算滚动时间：留时间给交互
            scroll_time = duration * 0.5  # 50% 时间用于滚动
            if scroll_distance > 0:
                scroll_steps = int(scroll_time * 10)  # 100ms 间隔
                step_size = scroll_distance / scroll_steps

                for i in range(scroll_steps):
                    elapsed = time.time() - start_time
                    if elapsed > duration - 5:  # 留 5 秒给结尾
                        break
                    page.evaluate(f"window.scrollBy(0, {step_size})")
                    time.sleep(0.1)

            time.sleep(1)

            # 阶段 3: 滚动回中间，尝试交互
            page.evaluate("window.scrollTo({top: document.body.scrollHeight / 3, behavior: 'smooth'})")
            time.sleep(1.5)

            _try_click_interactive(page, pause=1.5)

            # 阶段 4: 滚动回顶部
            elapsed = time.time() - start_time
            remaining = duration - elapsed
            if remaining > 3:
                page.evaluate("window.scrollTo({top: 0, behavior: 'smooth'})")
                time.sleep(min(remaining - 1, 3))

            # 确保至少录制了 duration 秒
            elapsed = time.time() - start_time
            if elapsed < duration:
                time.sleep(duration - elapsed)

            # ---- 录制结束 ----
            actual_duration = time.time() - start_time
            print(f"[INFO] 录制完成，实际时长 {actual_duration:.1f}s")

            # 关闭上下文以保存视频
            page.close()
            context.close()
            browser.close()

        # 找到 Playwright 生成的视频文件
        video_files = list(Path(tmp_dir).glob("*.webm"))
        if not video_files:
            sys.exit("[ERROR] 未找到录制的视频文件")

        raw_video = video_files[0]
        print(f"[INFO] 原始视频: {raw_video} ({raw_video.stat().st_size / 1024 / 1024:.1f} MB)")

        # 用 ffmpeg 转换为 mp4, 24fps, 裁剪到目标时长
        print("[INFO] 正在用 ffmpeg 转码为 MP4 (24fps)...")
        cmd = [
            "ffmpeg", "-y",
            "-i", str(raw_video),
            "-t", str(duration),
            "-r", str(fps),
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-pix_fmt", "yuv420p",
            "-an",  # 无音频
            "-movflags", "+faststart",
            str(output_path),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[ERROR] ffmpeg 失败: {result.stderr[:500]}")
            sys.exit(1)

    file_size = output_path.stat().st_size
    print(f"[OK] 视频已保存 {output_path} ({file_size / 1024 / 1024:.1f} MB)")
    return output_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="自动录屏")
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument("--duration", type=int, default=35, help="目标时长秒数 (默认 35, 范围 20-60)")
    parser.add_argument("--width", type=int, default=1920, help="视口宽度 (默认 1920)")
    parser.add_argument("--height", type=int, default=1080, help="视口高度 (默认 1080)")
    parser.add_argument("--fps", type=int, default=24, help="帧率 (默认 24)")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    if not task_dir.exists():
        sys.exit(f"[ERROR] 任务目录 {task_dir} 不存在")

    capture_video(task_dir, duration=args.duration, width=args.width,
                  height=args.height, fps=args.fps)


if __name__ == "__main__":
    main()
