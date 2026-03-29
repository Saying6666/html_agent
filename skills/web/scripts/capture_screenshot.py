#!/usr/bin/env python3
"""
Capture a full-page screenshot for a generated single-file HTML task.

Usage:
    python capture_screenshot.py --task fdu_012
    python capture_screenshot.py --task fdu_012 --width 1920

Requires:
    pip install playwright && playwright install chromium
"""

import argparse
import sys
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("[ERROR] Please install playwright: pip install playwright && playwright install chromium")


PREPARE_PAGE_FOR_CAPTURE_JS = r"""
() => {
    const revealClassNames = ["in", "is-visible", "visible", "show", "revealed", "active"];
    const revealSelectors = [
        ".reveal",
        ".stagger",
        ".scroll-reveal",
        "[data-reveal]",
        "[data-animate]",
        "[class*='reveal']"
    ];

    const makeVisible = (node) => {
        revealClassNames.forEach((name) => node.classList.add(name));
        node.style.opacity = "1";
        node.style.transform = "none";
        node.style.filter = "none";
        node.style.visibility = "visible";
        node.style.animationPlayState = "paused";
    };

    document.documentElement.style.scrollBehavior = "auto";
    document.body.style.scrollBehavior = "auto";

    revealSelectors.forEach((selector) => {
        document.querySelectorAll(selector).forEach(makeVisible);
    });

    document.querySelectorAll(".stagger > *").forEach(makeVisible);

    document.querySelectorAll("[data-count]").forEach((node) => {
        const target = node.getAttribute("data-count");
        if (target) {
            node.textContent = target;
        }
    });

    // Make sure at least one tab panel is visible in each tab set.
    document.querySelectorAll("[role='tabpanel']").forEach((panel) => {
        const isHidden = getComputedStyle(panel).display === "none";
        const looksActive = panel.classList.contains("active") || panel.classList.contains("is-active");
        if (!isHidden || looksActive) {
            panel.style.display = "block";
            return;
        }

        const siblings = panel.parentElement
            ? [...panel.parentElement.querySelectorAll("[role='tabpanel']")]
            : [];
        if (siblings.length && siblings[0] === panel) {
            panel.style.display = "block";
        }
    });

    // Open a couple of accordions so the screenshot shows more useful content.
    document.querySelectorAll(".accordion li, .faq-item").forEach((item, index) => {
        if (index >= 2) return;
        item.classList.add("open", "is-open", "active");
        const button = item.querySelector("button,[aria-expanded]");
        if (button) button.setAttribute("aria-expanded", "true");
        item.querySelectorAll(".panel,.faq-answer").forEach((panel) => {
            panel.style.maxHeight = "1000px";
            panel.style.display = "block";
            panel.style.opacity = "1";
            panel.style.visibility = "visible";
        });
    });

    // Hide transient overlays that would cover the page in a static capture.
    document.querySelectorAll(".toast,.modal-shell,.modal-backdrop,.backdrop,[role='dialog']").forEach((node) => {
        if (node.matches("[role='dialog']")) return;
        node.classList.remove("open", "show", "is-visible");
    });
    document.querySelectorAll("dialog[open]").forEach((node) => node.close());
}
"""


def capture_screenshot(task_dir: Path, width: int = 1920, wait: float = 5.0) -> Path:
    """Open index.html and capture a full-page screenshot."""
    html_path = task_dir / "src" / "index.html"
    if not html_path.exists():
        sys.exit(f"[ERROR] {html_path} does not exist")

    file_url = html_path.resolve().as_uri()
    output_path = task_dir / "preview.png"

    print(f"[INFO] Capturing screenshot for {html_path}")
    print(f"  URL: {file_url}")
    print(f"  Viewport width: {width}px")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": 1080})

        page.goto(file_url, wait_until="networkidle")
        time.sleep(wait)

        # Scroll through the page to trigger lazy/reveal logic first.
        page.evaluate(
            """
            () => new Promise((resolve) => {
                const totalHeight = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
                let scrolled = 0;
                const step = 300;
                const interval = setInterval(() => {
                    window.scrollBy(0, step);
                    scrolled += step;
                    if (scrolled >= totalHeight) {
                        clearInterval(interval);
                        setTimeout(() => {
                            window.scrollTo(0, 0);
                            setTimeout(resolve, 800);
                        }, 1200);
                    }
                }, 50);
            })
            """
        )

        time.sleep(1.5)
        page.evaluate(PREPARE_PAGE_FOR_CAPTURE_JS)
        time.sleep(0.5)

        page.screenshot(path=str(output_path), full_page=True)
        browser.close()

    file_size = output_path.stat().st_size
    print(f"[OK] Screenshot saved to {output_path} ({file_size / 1024:.1f} KB)")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Capture a full-page screenshot")
    parser.add_argument("--task", required=True, help="Task ID, for example fdu_012")
    parser.add_argument("--root", default=None, help="Project root directory")
    parser.add_argument("--width", type=int, default=1920, help="Viewport width (default 1920)")
    parser.add_argument("--wait", type=float, default=5.0, help="Extra page wait time in seconds")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    if not task_dir.exists():
        sys.exit(f"[ERROR] Task directory {task_dir} does not exist")

    capture_screenshot(task_dir, width=args.width, wait=args.wait)


if __name__ == "__main__":
    main()
