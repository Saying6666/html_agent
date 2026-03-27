#!/usr/bin/env python3
"""
Generate preview.png and video.mp4 for all FDU tasks using Playwright
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

# Task directories
TASKS = ["fdu_006", "fdu_007", "fdu_008", "fdu_009", "fdu_010"]
BASE_DIR = Path("C:/Users/saying/Desktop/html_agent")

async def capture_task(page, task_dir: Path, task_name: str):
    """Capture screenshot and video for a single task"""
    html_path = task_dir / "src" / "index.html"
    preview_path = task_dir / "preview.png"

    if not html_path.exists():
        print(f"  [WARN] {task_name}: index.html not found, skipping")
        return False

    file_url = f"file:///{html_path.as_posix()}"
    print(f"  [INFO] Loading {file_url}")

    try:
        # Navigate to the page
        await page.goto(file_url, wait_until="networkidle")
        await asyncio.sleep(2)  # Wait for animations to settle

        # Get full page height
        height = await page.evaluate("document.body.scrollHeight")
        width = await page.evaluate("document.body.scrollWidth")
        print(f"  [INFO] Page dimensions: {width}x{height}")

        # Capture full page screenshot
        await page.screenshot(path=str(preview_path), full_page=True)
        print(f"  [OK] Screenshot saved: {preview_path}")

        return True

    except Exception as e:
        print(f"  [ERROR] Error processing {task_name}: {e}")
        return False


async def generate_video_with_playwright(task_dir: Path, task_name: str):
    """Generate video using Playwright's video recording feature"""
    html_path = task_dir / "src" / "index.html"
    video_output = task_dir / "video.mp4"

    if not html_path.exists():
        return False

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Create browser context with video recording
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=str(task_dir),
            record_video_size={"width": 1920, "height": 1080}
        )

        page = await context.new_page()

        try:
            file_url = f"file:///{html_path.as_posix()}"
            await page.goto(file_url, wait_until="networkidle")
            await asyncio.sleep(2)

            # Get page dimensions
            height = await page.evaluate("document.body.scrollHeight")
            viewport_height = 1080

            # Scroll down slowly over ~30 seconds
            scroll_steps = 60
            step_delay = 0.5  # 30 seconds total

            for i in range(scroll_steps + 1):
                scroll_y = (height - viewport_height) * (i / scroll_steps)
                await page.evaluate(f"window.scrollTo(0, {scroll_y})")
                await asyncio.sleep(step_delay)

            # Scroll back to top
            await asyncio.sleep(1)
            await page.evaluate("window.scrollTo(0, 0)")
            await asyncio.sleep(2)

            # Close context to save video
            await context.close()
            await browser.close()

            # Find and rename the video file
            video_files = list(task_dir.glob("*.webm"))
            if video_files:
                video_files[0].rename(video_output)
                print(f"  [OK] Video saved: {video_output}")
                return True

        except Exception as e:
            print(f"  [ERROR] Video error for {task_name}: {e}")
            await context.close()
            await browser.close()
            return False

    return False


async def main():
    print("=" * 60)
    print("Generating Web Design Dataset Deliverables")
    print("=" * 60)

    for task_name in TASKS:
        task_dir = BASE_DIR / task_name
        print(f"\n[PROCESSING] {task_name}...")

        # First pass: screenshot
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})

            success = await capture_task(page, task_dir, task_name)

            await browser.close()

        if success:
            # Second pass: video
            await generate_video_with_playwright(task_dir, task_name)

    print("\n" + "=" * 60)
    print("Generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
