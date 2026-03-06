from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from pipeline_common import chat_completion, extract_html_document, load_runtime_settings
from validate_task import INTERACTION_FEATURES


SYSTEM_PROMPT = "You are an elite single-file web design generator. Return only production-ready HTML."


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_candidate_root(task_root: Path, provider: str) -> Path:
    return task_root / ".pipeline" / provider / task_root.name


def stage_candidate(task_root: Path, provider: str, html: str) -> Path:
    candidate_root = build_candidate_root(task_root, provider)
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


def render_repair_prompt(template: str, validation_output: str, html: str) -> str:
    return template.replace("{VALIDATION_OUTPUT}", validation_output.strip()).replace("{CURRENT_HTML}", html.strip())


def generate_candidate(
    *,
    task_root: Path,
    skill_root: Path,
    provider: str,
    model: str,
    settings_base_url: str,
    settings_api_key: str,
    max_repairs: int,
) -> dict[str, object]:
    prompt_path = task_root / "prompts" / f"builder-{provider}.md"
    repair_template = read_text(task_root / "prompts" / "repair.md")
    prompt_text = read_text(prompt_path)
    raw_response = chat_completion(
        base_url=settings_base_url,
        api_key=settings_api_key,
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text},
        ],
    )
    html = extract_html_document(raw_response)
    candidate_root = stage_candidate(task_root, provider, html)
    write_text(task_root / ".pipeline" / provider / "initial-response.txt", raw_response + "\n")

    validation = run_validator(skill_root, candidate_root)
    attempts = 0
    while validation.returncode != 0 and attempts < max_repairs:
        attempts += 1
        repair_prompt = render_repair_prompt(repair_template, validation.stdout + validation.stderr, html)
        repaired_response = chat_completion(
            base_url=settings_base_url,
            api_key=settings_api_key,
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": repair_prompt},
            ],
            temperature=0.3,
        )
        html = extract_html_document(repaired_response)
        candidate_root = stage_candidate(task_root, provider, html)
        write_text(task_root / ".pipeline" / provider / f"repair-{attempts}.txt", repaired_response + "\n")
        validation = run_validator(skill_root, candidate_root)

    return {
        "provider": provider,
        "model": model,
        "candidate_root": str(candidate_root),
        "html": html,
        "attempts": attempts,
        "validation_stdout": validation.stdout,
        "validation_stderr": validation.stderr,
        "validation_returncode": validation.returncode,
        "metrics": score_candidate(validation, html),
    }


def choose_winner(results: list[dict[str, object]], preferred: str) -> dict[str, object]:
    if preferred in {"gemini", "gpt"}:
        for result in results:
            if result["provider"] == preferred:
                return result
        raise SystemExit(f"Requested winner '{preferred}' was not generated.")

    return max(
        results,
        key=lambda result: (
            bool(result["metrics"]["passed"]),
            int(result["metrics"]["score"]),
            -int(result["metrics"]["error_count"]),
            -int(result["metrics"]["warning_count"]),
            int(result["metrics"]["interaction_hits"]),
            int(result["metrics"]["sections"]),
            int(result["metrics"]["bytes"]),
        ),
    )


def write_judge_report(task_root: Path, results: list[dict[str, object]], winner: dict[str, object]) -> None:
    lines = [
        "# Judge Report",
        "",
        f"Winner: `{winner['provider']}` using `{winner['model']}`",
        "",
        "## Candidate Summary",
        "",
    ]
    for result in results:
        metrics = result["metrics"]
        lines.extend(
            [
                f"### {result['provider']}",
                f"- model: `{result['model']}`",
                f"- passed: `{metrics['passed']}`",
                f"- score: `{metrics['score']}`",
                f"- errors: `{metrics['error_count']}`",
                f"- warnings: `{metrics['warning_count']}`",
                f"- interaction hits: `{metrics['interaction_hits']}`",
                f"- sections: `{metrics['sections']}`",
                f"- size bytes: `{metrics['bytes']}`",
                f"- repair attempts: `{result['attempts']}`",
                "",
                "Validator output:",
                "```text",
                result["validation_stdout"].strip() or "(no validator output)",
                "```",
                "",
            ]
        )
    write_text(task_root / "judge-report.md", "\n".join(lines).rstrip() + "\n")
    write_text(
        task_root / ".pipeline" / "summary.json",
        json.dumps({"winner": winner["provider"], "results": results}, indent=2, ensure_ascii=False) + "\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a dual-model HTML generation pipeline for a task scaffold.")
    parser.add_argument("task_path", help="Path to task directory, such as fdu_001")
    parser.add_argument("--winner", choices=["auto", "gemini", "gpt"], default="auto")
    parser.add_argument("--max-repairs", type=int, default=1)
    parser.add_argument("--base-url", default=None)
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--gemini-model", default=None)
    parser.add_argument("--gpt-model", default=None)
    parser.add_argument("--keep-pipeline-dir", action="store_true")
    args = parser.parse_args()

    task_root = Path(args.task_path).resolve()
    skill_root = Path(__file__).resolve().parents[1]
    if not task_root.exists():
        raise SystemExit(f"Task directory does not exist: {task_root}")

    settings = load_runtime_settings(
        base_url=args.base_url,
        api_key=args.api_key,
        gemini_model=args.gemini_model,
        gpt_model=args.gpt_model,
    )

    results = [
        generate_candidate(
            task_root=task_root,
            skill_root=skill_root,
            provider="gemini",
            model=settings.gemini_model,
            settings_base_url=settings.base_url,
            settings_api_key=settings.api_key,
            max_repairs=args.max_repairs,
        ),
        generate_candidate(
            task_root=task_root,
            skill_root=skill_root,
            provider="gpt",
            model=settings.gpt_model,
            settings_base_url=settings.base_url,
            settings_api_key=settings.api_key,
            max_repairs=args.max_repairs,
        ),
    ]
    winner = choose_winner(results, args.winner)
    write_text(task_root / "src" / "index.html", str(winner["html"]).strip() + "\n")
    write_judge_report(task_root, results, winner)

    if not args.keep_pipeline_dir:
        for result in results:
            candidate_dir = Path(str(result["candidate_root"])).parents[1]
            if candidate_dir.exists():
                shutil.rmtree(candidate_dir)

    print(f"Winner: {winner['provider']} ({winner['model']})")
    print(f"Wrote final HTML to {task_root / 'src' / 'index.html'}")
    print(f"Wrote judge report to {task_root / 'judge-report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
