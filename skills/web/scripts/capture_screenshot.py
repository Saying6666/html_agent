#!/usr/bin/env python3
"""
capture_screenshot.py — 使用 Playwright 对 index.html 进行全页长截图

用法:
    python capture_screenshot.py --task fdu_012
    python capture_screenshot.py --task fdu_012 --width 1920

依赖: pip install playwright && playwright install chromium
"""

import argparse
import sys
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("[ERROR] 请先安装 playwright: pip install playwright && playwright install chromium")


def capture_screenshot(task_dir: Path, width: int = 1920, wait: float = 5.0) -> Path:
    """打开 index.html 并进行全页长截图。"""
    html_path = task_dir / "src" / "index.html"
    if not html_path.exists():
        sys.exit(f"[ERROR] {html_path} 不存在")

    file_url = html_path.resolve().as_uri()
    output_path = task_dir / "preview.png"

    print(f"[INFO] 正在截图 {html_path}")
    print(f"  URL: {file_url}")
    print(f"  视口宽度: {width}px")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": 1080})

        # 加载页面
        page.goto(file_url, wait_until="networkidle")

        # 等待字体、图片、动画加载
        time.sleep(wait)

        # 触发所有 scroll reveal 动画：滚动到底部再回到顶部
        page.evaluate("""
            () => new Promise(resolve => {
                const totalHeight = document.body.scrollHeight;
                let scrolled = 0;
                const step = 300;
                const interval = setInterval(() => {
                    window.scrollBy(0, step);
                    scrolled += step;
                    if (scrolled >= totalHeight) {
                        clearInterval(interval);
                        // 等待动画完成后回到顶部
                        setTimeout(() => {
                            window.scrollTo(0, 0);
                            setTimeout(resolve, 1000);
                        }, 1500);
                    }
                }, 50);
            })
        """)

        # 等待 count-up 等动画完成
        time.sleep(2)

        # 全页截图
        page.screenshot(path=str(output_path), full_page=True)

        browser.close()

    file_size = output_path.stat().st_size
    print(f"[OK] 截图已保存 {output_path} ({file_size / 1024:.1f} KB)")
    return output_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="全页长截图")
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument("--width", type=int, default=1920, help="视口宽度 (默认 1920)")
    parser.add_argument("--wait", type=float, default=5.0, help="页面加载等待秒数 (默认 5)")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    if not task_dir.exists():
        sys.exit(f"[ERROR] 任务目录 {task_dir} 不存在")

    capture_screenshot(task_dir, width=args.width, wait=args.wait)


if __name__ == "__main__":
    main()
