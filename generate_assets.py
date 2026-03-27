#!/usr/bin/env python3
"""
Generate preview.png and video.mp4 for web design tasks using Playwright
"""
import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

async def capture_task(task_dir: Path, task_name: str):
    """Generate preview.png and video.mp4 for a task"""
    html_file = task_dir / "src" / "index.html"
    preview_file = task_dir / "preview.png"
    video_file = task_dir / "video.mp4"

    if not html_file.exists():
        print(f"[ERROR] {task_name}: index.html not found")
        return False

    print(f"[PROCESSING] {task_name}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Create context with video recording
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            record_video_dir=str(task_dir),
            record_video_size={'width': 1920, 'height': 1080}
        )

        page = await context.new_page()

        # Load the HTML file
        file_url = f"file:///{html_file.absolute().as_posix()}"
        await page.goto(file_url, wait_until='networkidle')

        # Wait for animations to settle
        await page.wait_for_timeout(3000)

        # Get full page height
        page_height = await page.evaluate('() => document.body.scrollHeight')
        print(f"   Page height: {page_height}px")

        # Capture full page screenshot
        await page.screenshot(path=str(preview_file), full_page=True)
        print(f"   Screenshot saved: {preview_file.name}")

        # Record 35 second scrolling video
        print(f"   Recording 35s video...")

        # Scroll animation over 35 seconds
        steps = 100
        step_duration = 35000 / steps  # 35 seconds total

        for i in range(steps + 1):
            progress = i / steps
            scroll_y = int(progress * (page_height - 1080))
            await page.evaluate(f'() => window.scrollTo(0, {scroll_y})')
            await asyncio.sleep(step_duration / 1000)

        # Scroll back to top
        await page.evaluate('() => window.scrollTo(0, 0)')
        await asyncio.sleep(1)

        # Close context to save video
        await context.close()
        await browser.close()

        # Find and rename the video file
        video_files = list(task_dir.glob("*.webm")) + list(task_dir.glob("*.mp4"))
        if video_files:
            # Get the most recent video file
            latest_video = max(video_files, key=lambda p: p.stat().st_mtime)
            if video_file.exists():
                video_file.unlink()
            latest_video.rename(video_file)
            print(f"   Video saved: {video_file.name}")
        else:
            print(f"   [WARNING] Video file not found")

        return True

async def main():
    base_dir = Path("C:/Users/saying/Desktop/html_agent")

    # Tasks to process (fdu_002, fdu_003, fdu_004, fdu_005)
    tasks = ["fdu_002", "fdu_003", "fdu_004", "fdu_005"]

    for task_name in tasks:
        task_dir = base_dir / task_name
        if task_dir.exists():
            try:
                await capture_task(task_dir, task_name)
            except Exception as e:
                print(f"   [ERROR] processing {task_name}: {e}")
        else:
            print(f"[ERROR] {task_name}: Directory not found")

    print("\nAll tasks completed!")

if __name__ == "__main__":
    asyncio.run(main())
