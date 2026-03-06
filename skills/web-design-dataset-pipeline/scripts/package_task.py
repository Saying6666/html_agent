from __future__ import annotations

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path


def run_validation(skill_root: Path, task_root: Path) -> None:
    validator = skill_root / "scripts" / "validate_task.py"
    result = subprocess.run(
        [sys.executable, str(validator), str(task_root), "--stage", "final"],
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def delivery_file_paths(task_root: Path) -> list[Path]:
    paths = [
        task_root / "prompt.md",
        task_root / "src" / "index.html",
        task_root / "video.mp4",
    ]
    preview_dir = task_root / "preview"
    preview_png = task_root / "preview.png"
    if preview_dir.exists():
        paths.extend(sorted(preview_dir.glob("preview_*.png")))
    elif preview_png.exists():
        paths.append(preview_png)
    return [path for path in paths if path.exists()]


def build_zip(task_root: Path, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"{task_root.name}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in delivery_file_paths(task_root):
            archive.write(file_path, arcname=str(Path(task_root.name) / file_path.relative_to(task_root)))
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Package a validated Web Design task into a zip.")
    parser.add_argument("task_path", help="Path to fdu_001 task directory")
    parser.add_argument("--output-dir", default="dist")
    parser.add_argument("--skip-validate", action="store_true")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    task_root = Path(args.task_path).resolve()
    if not args.skip_validate:
        run_validation(skill_root, task_root)

    zip_path = build_zip(task_root, Path(args.output_dir).resolve())
    print(f"Created package: {zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
