from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path


TASK_PATTERN = re.compile(r"^fdu_\d{3}$")
ROUND_PATTERN = re.compile(r"^##\s*Round\s+\d+", re.IGNORECASE | re.MULTILINE)

FORBIDDEN_NAMES = {
    ".DS_Store",
    "__MACOSX",
    "Thumbs.db",
    "desktop.ini",
    "package.json",
}

FORBIDDEN_SEGMENTS = {
    "node_modules",
}

LOCAL_ASSET_PATTERN = re.compile(
    r"(?:src|href)=['\"](?!(?:https?:|data:|mailto:|tel:|#))[^'\"]+['\"]",
    re.IGNORECASE,
)
LOCAL_CSS_URL_PATTERN = re.compile(r"url\((?!['\"]?(?:https?:|data:))", re.IGNORECASE)
DISALLOWED_FRAMEWORK_PATTERN = re.compile(r"react|vue|svelte|jquery", re.IGNORECASE)
EXTERNAL_STYLESHEET_PATTERN = re.compile(r"<link[^>]+rel=['\"]stylesheet['\"][^>]+href=['\"]([^'\"]+)['\"]", re.IGNORECASE)

INTERACTION_FEATURES = {
    "hover": re.compile(r":hover|mouseenter|mouseover", re.IGNORECASE),
    "active": re.compile(r":active|mousedown|pointerdown", re.IGNORECASE),
    "focus": re.compile(r":focus|focus-visible", re.IGNORECASE),
    "scroll_reveal": re.compile(r"IntersectionObserver|visible", re.IGNORECASE),
    "counter": re.compile(r"requestAnimationFrame|counter", re.IGNORECASE),
    "smooth_scroll": re.compile(r"scroll-behavior|scrollIntoView", re.IGNORECASE),
    "nav_scroll": re.compile(r"addEventListener\(['\"]scroll|window\.scrollY", re.IGNORECASE),
    "accordion_tabs_modal": re.compile(r"accordion|tab|modal|toast|tooltip", re.IGNORECASE),
    "carousel_parallax_theme_form": re.compile(r"carousel|slider|parallax|theme|validate", re.IGNORECASE),
}


def list_files(root: Path) -> list[Path]:
    return [path for path in root.rglob("*") if path.is_file()]


def check_task_id(task_root: Path, errors: list[str]) -> None:
    if not TASK_PATTERN.fullmatch(task_root.name):
        errors.append(f"任务目录名不合法: {task_root.name}，应为 fdu_001 这类格式")


def check_forbidden_files(task_root: Path, errors: list[str]) -> None:
    for file_path in list_files(task_root):
        parts = set(file_path.parts)
        if file_path.name in FORBIDDEN_NAMES or any(part in FORBIDDEN_SEGMENTS for part in parts):
            errors.append(f"发现禁止文件或目录: {file_path}")
        if file_path.suffix.lower() == ".pen":
            errors.append(f"发现禁止的 .pen 文件: {file_path}")


def check_structure(task_root: Path, stage: str, errors: list[str], warnings: list[str]) -> None:
    prompt = task_root / "prompt.md"
    src_dir = task_root / "src"
    html = src_dir / "index.html"

    if not prompt.exists():
        errors.append("缺少 prompt.md")
    if not src_dir.exists():
        errors.append("缺少 src/ 目录")

    if stage == "final" and not html.exists():
        errors.append("final 阶段必须包含 src/index.html")
    if stage == "scaffold" and not html.exists():
        warnings.append("scaffold 阶段尚未生成 src/index.html；prompt-first 流程下这是正常情况")

    if src_dir.exists():
        extra = [path for path in src_dir.iterdir() if path.name != "index.html"]
        if extra:
            errors.append("src 目录中只能包含 index.html")

    if stage == "final":
        preview_png = task_root / "preview.png"
        preview_dir = task_root / "preview"
        has_preview_dir = preview_dir.exists() and any(preview_dir.glob("preview_*.png"))
        if not preview_png.exists() and not has_preview_dir:
            errors.append("最终交付必须包含 preview.png 或 preview/preview_*.png")
        if not (task_root / "video.mp4").exists():
            errors.append("最终交付必须包含 video.mp4")


def check_prompt(task_root: Path, errors: list[str]) -> None:
    prompt = task_root / "prompt.md"
    if not prompt.exists():
        return
    content = prompt.read_text(encoding="utf-8")
    rounds = len(ROUND_PATTERN.findall(content))
    if rounds < 3:
        errors.append(f"prompt.md 轮次不足，当前只有 {rounds} 轮")


def check_html(task_root: Path, stage: str, errors: list[str], warnings: list[str]) -> None:
    html = task_root / "src" / "index.html"
    if not html.exists():
        return

    if stage == "scaffold":
        warnings.append("scaffold 阶段检测到 src/index.html；完整 HTML 合规检查会在 final 阶段执行")
        return

    content = html.read_text(encoding="utf-8")
    lower = content.lower()

    if "<style" not in lower:
        errors.append("index.html 缺少内联 <style>")
    if "<script" not in lower:
        errors.append("index.html 缺少内联 <script>")

    stylesheets = EXTERNAL_STYLESHEET_PATTERN.findall(content)
    for url in stylesheets:
        if "fonts.googleapis.com" not in url:
            errors.append(f"发现不允许的外部样式表: {url}")

    if LOCAL_ASSET_PATTERN.search(content):
        errors.append("发现本地资源引用；只允许 http(s)、data、锚点、mailto、tel")

    if LOCAL_CSS_URL_PATTERN.search(content):
        errors.append("检测到 CSS 中的本地 url(...) 资源引用")

    if DISALLOWED_FRAMEWORK_PATTERN.search(content):
        errors.append("检测到疑似 React/Vue/Svelte/jQuery 等框架引用")

    matched = [name for name, pattern in INTERACTION_FEATURES.items() if pattern.search(content)]
    if len(matched) < 5:
        errors.append(f"交互特征不足，当前只检测到 {len(matched)} 项: {', '.join(matched) or '无'}")
    if "<nav" not in lower or "<section" not in lower:
        warnings.append("建议使用更完整的语义化标签，如 <nav>、<section>、<footer>")


def check_video(task_root: Path, warnings: list[str]) -> None:
    video = task_root / "video.mp4"
    if not video.exists():
        return

    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        warnings.append("未找到 ffprobe，无法自动校验 video.mp4 是否为 24fps")
        return

    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=r_frame_rate",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(video),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    rate = result.stdout.strip()
    if rate and rate != "24/1":
        warnings.append(f"video.mp4 帧率看起来不是 24fps，而是 {rate}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Web Design dataset task folder.")
    parser.add_argument("task_path", help="Path to fdu_001 task directory")
    parser.add_argument("--stage", choices=["scaffold", "final"], default="final")
    args = parser.parse_args()

    task_root = Path(args.task_path).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not task_root.exists() or not task_root.is_dir():
      print(f"任务目录不存在: {task_root}")
      return 1

    check_task_id(task_root, errors)
    check_forbidden_files(task_root, errors)
    check_structure(task_root, args.stage, errors, warnings)
    check_prompt(task_root, errors)
    check_html(task_root, args.stage, errors, warnings)
    if args.stage == "final":
        check_video(task_root, warnings)

    if errors:
        print("Validation failed:")
        for item in errors:
            print(f"- ERROR: {item}")
        for item in warnings:
            print(f"- WARN: {item}")
        return 1

    print(f"Validation passed for {task_root.name} [{args.stage}]")
    for item in warnings:
        print(f"- WARN: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
