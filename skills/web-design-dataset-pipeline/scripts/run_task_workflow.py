from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from bootstrap_task import DEFAULT_AUDIENCE


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the Web Design task workflow. Defaults to prompt-only scaffolding."
    )
    parser.add_argument("task_id", help="Task id like fdu_001")
    parser.add_argument("--root", default=".", help="Output root directory")
    parser.add_argument("--category", default="SaaS landing page")
    parser.add_argument("--style", default="Dark Mode")
    parser.add_argument("--concept", default="AI productivity platform")
    parser.add_argument("--audience", default=DEFAULT_AUDIENCE)
    parser.add_argument("--multi-preview", action="store_true", help="Create preview/ for multi-state capture")
    parser.add_argument(
        "--mode",
        choices=["prompt-only", "generate"],
        default="prompt-only",
        help="Default is prompt-only; use generate to run the 4-step Anthropic flow.",
    )
    parser.add_argument("--claude-model", default=None)
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--verbose-client", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    bootstrap_script = script_dir / "bootstrap_task.py"
    pipeline_script = script_dir / "run_claude_generation.py"
    task_path = Path(args.root).resolve() / args.task_id

    bootstrap_command = [
        sys.executable,
        str(bootstrap_script),
        args.task_id,
        "--root",
        args.root,
        "--category",
        args.category,
        "--style",
        args.style,
        "--concept",
        args.concept,
        "--audience",
        args.audience,
    ]
    if args.multi_preview:
        bootstrap_command.append("--multi-preview")

    subprocess.run(bootstrap_command, check=True)

    if args.mode == "prompt-only":
        print(f"Prompt-only workflow complete for {task_path}")
        print("No API generation was run. Use the prompts/ files manually or rerun with --mode generate.")
        return 0

    pipeline_command = [
        sys.executable,
        str(pipeline_script),
        str(task_path),
    ]
    if args.claude_model:
        pipeline_command.extend(["--model", args.claude_model])
    if args.max_output_tokens is not None:
        pipeline_command.extend(["--max-output-tokens", str(args.max_output_tokens)])
    if args.verbose_client:
        pipeline_command.append("--verbose-client")

    subprocess.run(pipeline_command, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
