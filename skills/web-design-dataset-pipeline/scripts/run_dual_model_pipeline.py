from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compatibility wrapper. The dual-model pipeline is replaced by the 4-step Anthropic flow."
    )
    parser.add_argument("task_path", help="Path to task directory, such as fdu_001")
    parser.add_argument("--model", default=None)
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--verbose-client", action="store_true")
    parser.add_argument("--winner", default=None)
    parser.add_argument("--max-repairs", type=int, default=None)
    parser.add_argument("--base-url", default=None)
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--gemini-model", default=None)
    parser.add_argument("--gpt-model", default=None)
    parser.add_argument("--keep-pipeline-dir", action="store_true")
    args = parser.parse_args()

    script_path = Path(__file__).resolve().parent / "run_claude_generation.py"
    command = [sys.executable, str(script_path), args.task_path]
    if args.model:
        command.extend(["--model", args.model])
    if args.max_output_tokens is not None:
        command.extend(["--max-output-tokens", str(args.max_output_tokens)])
    if args.verbose_client:
        command.append("--verbose-client")

    print("run_dual_model_pipeline.py is deprecated; forwarding to the 4-step Anthropic generator.")
    subprocess.run(command, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
