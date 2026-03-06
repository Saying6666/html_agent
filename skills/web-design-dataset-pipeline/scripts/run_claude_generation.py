from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from pipeline_common import extract_html_document
from validate_task import INTERACTION_FEATURES


ANTHROPIC_HELPER_CANDIDATES = [
    Path.home() / ".codex" / "skills" / "anthropic-sdk-helper" / "scripts",
    Path.home() / ".claude" / "skills" / "anthropic-sdk-helper" / "scripts",
]
SYSTEM_PROMPT = (
    "You are an elite single-file web design generator. "
    "Always return one complete production-ready index.html document only."
)
DEFAULT_MODEL = "claude-sonnet-4-20250514"
DEFAULT_MAX_OUTPUT_TOKENS = 8192


def ensure_anthropic_helper_import() -> object:
    for helper_dir in ANTHROPIC_HELPER_CANDIDATES:
        if helper_dir.exists():
            sys.path.insert(0, str(helper_dir))
            break

    try:
        from claude_sdk_helper import get_anthropic_client
    except ImportError as exc:
        raise SystemExit(
            "Could not import anthropic-sdk-helper. "
            "Make sure the skill is installed and the `anthropic` package is available."
        ) from exc

    return get_anthropic_client


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_prompt_rounds(prompt_text: str) -> tuple[str, list[str]]:
    pattern = re.compile(r"^## Round \d+\s*$", re.MULTILINE)
    matches = list(pattern.finditer(prompt_text))
    if not matches:
        raise SystemExit("prompt.md does not contain any `## Round N` sections.")

    shared_context = prompt_text[: matches[0].start()].strip()
    rounds: list[str] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(prompt_text)
        round_body = prompt_text[start:end].strip()
        if round_body:
            rounds.append(round_body)

    if len(rounds) != 4:
        raise SystemExit(f"Expected exactly 4 prompt rounds, found {len(rounds)} in prompt.md.")

    return shared_context, rounds


def build_step_prompt(
    *,
    shared_context: str,
    round_text: str,
    step_number: int,
    current_html: str | None,
    validation_output: str | None,
) -> str:
    common_rules = (
        "Return only the full updated index.html document. "
        "Do not include markdown fences or any explanation."
    )
    if step_number == 1:
        return (
            f"{shared_context}\n\n"
            f"Step {step_number} of 4.\n"
            "Generate the first complete draft of the page.\n"
            f"{round_text}\n\n"
            f"{common_rules}"
        )

    parts = [
        f"Step {step_number} of 4.",
        "Revise the current HTML and return a stronger full document.",
        round_text,
    ]
    if validation_output:
        parts.extend(["Validator feedback to address:", validation_output.strip()])
    parts.extend(["Current HTML:", current_html or "", common_rules])
    return "\n\n".join(parts)


def extract_response_text(response: object) -> str:
    content = getattr(response, "content", None)
    if not content:
        raise SystemExit("Anthropic response did not include content blocks.")

    parts: list[str] = []
    for block in content:
        text = getattr(block, "text", None)
        if isinstance(text, str) and text.strip():
            parts.append(text)

    if not parts:
        raise SystemExit("Anthropic response did not include usable text output.")

    return "\n".join(parts).strip()


def build_candidate_root(task_root: Path, step_number: int) -> Path:
    return task_root / ".pipeline" / "claude" / f"step-{step_number:02d}" / task_root.name


def stage_candidate(task_root: Path, step_number: int, html: str) -> Path:
    candidate_root = build_candidate_root(task_root, step_number)
    write_text(candidate_root / "prompt.md", read_text(task_root / "prompt.md"))
    write_text(candidate_root / "src" / "index.html", html)
    return candidate_root


def run_validator(skill_root: Path, candidate_root: Path) -> subprocess.CompletedProcess[str]:
    validator = skill_root / "scripts" / "validate_task.py"
    return subprocess.run(
        [sys.executable, str(validator), str(candidate_root), "--stage", "final"],
        capture_output=True,
        text=True,
        check=False,
    )


def count_prefixed_lines(output: str, prefix: str) -> int:
    return sum(1 for line in output.splitlines() if line.startswith(prefix))


def analyze_html(html: str) -> dict[str, int]:
    lowered = html.lower()
    interaction_hits = sum(1 for pattern in INTERACTION_FEATURES.values() if pattern.search(html))
    return {
        "bytes": len(html.encode("utf-8")),
        "sections": lowered.count("<section"),
        "articles": lowered.count("<article"),
        "interaction_hits": interaction_hits,
    }


def score_candidate(validation: subprocess.CompletedProcess[str], html: str) -> dict[str, int | bool]:
    analysis = analyze_html(html)
    error_count = count_prefixed_lines(validation.stdout, "- ERROR:")
    warning_count = count_prefixed_lines(validation.stdout, "- WARN:")
    passed = validation.returncode == 0
    numeric_score = (
        (1000 if passed else 0)
        - error_count * 200
        - warning_count * 20
        + analysis["interaction_hits"] * 25
        + analysis["sections"] * 10
        + analysis["articles"] * 5
        + min(analysis["bytes"] // 400, 80)
    )
    return {
        "passed": passed,
        "score": numeric_score,
        "error_count": error_count,
        "warning_count": warning_count,
        **analysis,
    }


def write_generation_report(task_root: Path, model: str, steps: list[dict[str, object]]) -> None:
    final_step = steps[-1]
    lines = [
        "# Claude Generation Report",
        "",
        f"- model: `{model}`",
        f"- steps: `{len(steps)}`",
        f"- final passed: `{final_step['metrics']['passed']}`",
        f"- final score: `{final_step['metrics']['score']}`",
        "",
    ]
    for step in steps:
        metrics = step["metrics"]
        lines.extend(
            [
                f"## Step {step['step_number']}",
                f"- passed: `{metrics['passed']}`",
                f"- score: `{metrics['score']}`",
                f"- errors: `{metrics['error_count']}`",
                f"- warnings: `{metrics['warning_count']}`",
                f"- interaction hits: `{metrics['interaction_hits']}`",
                f"- sections: `{metrics['sections']}`",
                f"- size bytes: `{metrics['bytes']}`",
                "",
                "Validator output:",
                "```text",
                str(step["validation_stdout"]).strip() or "(no validator output)",
                "```",
                "",
            ]
        )
    report = "\n".join(lines).rstrip() + "\n"
    write_text(task_root / "generation-report.md", report)
    write_text(task_root / "judge-report.md", report)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a 4-step Anthropic HTML generation pipeline for a task.")
    parser.add_argument("task_path", help="Path to task directory, such as fdu_001")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--max-output-tokens", type=int, default=DEFAULT_MAX_OUTPUT_TOKENS)
    parser.add_argument("--verbose-client", action="store_true")
    args = parser.parse_args()

    task_root = Path(args.task_path).resolve()
    skill_root = Path(__file__).resolve().parents[1]
    prompt_path = task_root / "prompt.md"
    if not task_root.exists():
        raise SystemExit(f"Task directory does not exist: {task_root}")
    if not prompt_path.exists():
        raise SystemExit(f"Missing prompt.md: {prompt_path}")

    get_anthropic_client = ensure_anthropic_helper_import()
    client = get_anthropic_client(verbose=args.verbose_client)

    shared_context, rounds = parse_prompt_rounds(read_text(prompt_path))
    pipeline_dir = task_root / ".pipeline" / "claude"
    pipeline_dir.mkdir(parents=True, exist_ok=True)

    messages: list[dict[str, str]] = []
    current_html: str | None = None
    validation_output: str | None = None
    step_results: list[dict[str, object]] = []

    for step_number, round_text in enumerate(rounds, start=1):
        prompt = build_step_prompt(
            shared_context=shared_context,
            round_text=round_text,
            step_number=step_number,
            current_html=current_html,
            validation_output=validation_output,
        )
        messages.append({"role": "user", "content": prompt})
        response = client.messages.create(
            model=args.model,
            max_tokens=args.max_output_tokens,
            system=SYSTEM_PROMPT,
            messages=messages,
        )
        raw_text = extract_response_text(response)
        html = extract_html_document(raw_text)
        messages.append({"role": "assistant", "content": html})

        write_text(pipeline_dir / f"step-{step_number:02d}-prompt.txt", prompt + "\n")
        write_text(pipeline_dir / f"step-{step_number:02d}-raw.txt", raw_text + "\n")
        write_text(pipeline_dir / f"step-{step_number:02d}.html", html + "\n")

        candidate_root = stage_candidate(task_root, step_number, html)
        validation = run_validator(skill_root, candidate_root)
        metrics = score_candidate(validation, html)
        validation_output = validation.stdout.strip()
        current_html = html
        step_results.append(
            {
                "step_number": step_number,
                "candidate_root": str(candidate_root),
                "validation_stdout": validation.stdout,
                "validation_stderr": validation.stderr,
                "metrics": metrics,
            }
        )

    write_text(task_root / "src" / "index.html", (current_html or "").strip() + "\n")
    write_generation_report(task_root, args.model, step_results)

    final_metrics = step_results[-1]["metrics"]
    print(f"Claude generation complete with model {args.model}")
    print(f"Final validation passed: {final_metrics['passed']}")
    print(f"Wrote final HTML to {task_root / 'src' / 'index.html'}")
    print(f"Wrote report to {task_root / 'generation-report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
