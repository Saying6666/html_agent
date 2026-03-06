from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_AUDIENCE = "Design-conscious product teams evaluating a premium modern web experience"


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def infer_sections(category: str) -> list[str]:
    category_lower = category.lower()
    if "dashboard" in category_lower:
        return [
            "Sticky navbar",
            "Hero summary",
            "KPI cards",
            "Analytics modules",
            "Activity feed",
            "Integrations",
            "Pricing",
            "FAQ",
            "Footer",
        ]
    if "portfolio" in category_lower:
        return [
            "Navbar",
            "Hero intro",
            "Selected work grid",
            "Project spotlight",
            "Process",
            "Testimonials",
            "FAQ",
            "Contact footer",
        ]
    if "event" in category_lower or "conference" in category_lower:
        return [
            "Navbar",
            "Hero",
            "Speaker highlights",
            "Agenda",
            "Sponsor strip",
            "Ticketing",
            "FAQ",
            "CTA",
            "Footer",
        ]
    return [
        "Navbar",
        "Hero",
        "Trust logos",
        "Metrics",
        "Features",
        "Workflow or story section",
        "Integrations",
        "Pricing",
        "Testimonials",
        "FAQ",
        "CTA",
        "Footer",
    ]


def infer_interactions() -> list[str]:
    return [
        "button hover and active states",
        "navigation hover underline",
        "card hover lift",
        "scroll reveal animations",
        "animated counters",
        "tab switching or content toggle",
        "FAQ accordion",
        "sticky navbar background transition",
        "smooth scrolling",
    ]


def build_task_brief(task_id: str, category: str, style: str, concept: str, audience: str) -> dict[str, object]:
    brand_name = concept.strip().title()
    return {
        "taskid": task_id,
        "category": category,
        "style": style,
        "concept": concept,
        "brand_name": brand_name,
        "audience": audience,
        "sections": infer_sections(category),
        "interactions": infer_interactions(),
        "acceptance_notes": [
            "Return one complete src/index.html file only.",
            "Keep CSS and JS inline.",
            "Do not use React, Vue, Svelte, jQuery, or a build step.",
            "Use remote images only and inline SVG icons.",
            "Produce enough vertical content for a full-page screenshot.",
            "Implement at least 5 visible interaction patterns.",
        ],
        "risks": [
            "Do not reference local assets.",
            "Do not leave placeholder copy or TODO markers.",
            "Do not create extra files under src/.",
        ],
    }


def build_prompt(brief: dict[str, object]) -> str:
    sections = ", ".join(brief["sections"])
    interactions = ", ".join(brief["interactions"])
    return f"""# Shared Prompt Package

Task id: {brief['taskid']}
Category: {brief['category']}
Style: {brief['style']}
Concept: {brief['concept']}
Audience: {brief['audience']}
Required sections: {sections}
Required interactions: {interactions}

## Round 1
Create a premium {brief['category']} for "{brief['brand_name']}".
Design style: {brief['style']}.
Audience: {brief['audience']}.
Output a complete, content-rich, long-scroll single-file `index.html`.
Use inline `<style>` and inline `<script>` only.
Do not use React, Vue, Svelte, jQuery, or any build step.
Use Google Fonts if needed, remote images only, and inline SVG icons.
The page must feel like a real modern product website, not a short demo.
Required sections: {sections}.
Color direction: premium, brand-consistent, and modern; avoid harsh primary colors.
Typography direction: use a strong heading font pairing with a clean body font.

## Round 2
Expand the design so it has enough depth for a full-page screenshot.
Fill the page with meaningful content blocks, not empty placeholders.
Use high-quality remote imagery integrated into the layout.
Add strong visual hierarchy in the hero, richer section copy, and polished card layouts.
Required interactions to cover: {interactions}.
Make the page visually dense enough that the HTML is not short or minimal.

## Round 3
Polish all interactive states and compliance details.
Ensure hover, active, focus, and scroll-triggered behaviors are clearly visible.
Add responsive behavior for desktop and tablet.
Keep all CSS and JS inside `index.html`.
Do not reference any local assets, local CSS, local JS, or local images.
Return only the final HTML for `src/index.html`, with no extra explanation.

## Round 4
Final compliance pass.
Verify the result is suitable for task `{brief['taskid']}`.
The output must be a single self-contained `index.html` that opens directly in a browser.
Make sure there are at least 5 distinct interaction patterns, enough vertical content for long screenshot capture, and no placeholder TODO content.
"""


def build_builder_prompt(brief: dict[str, object], provider: str) -> str:
    provider_hint = {
        "gemini": "Bias toward strong layout completeness, richer content density, and premium visual direction.",
        "gpt": "Bias toward polished micro-interactions, semantic HTML, accessibility, and cleaner final code.",
    }[provider]
    sections = "\n".join(f"- {section}" for section in brief["sections"])
    interactions = "\n".join(f"- {interaction}" for interaction in brief["interactions"])
    acceptance = "\n".join(f"- {item}" for item in brief["acceptance_notes"])
    risks = "\n".join(f"- {item}" for item in brief["risks"])
    return f"""You are building a submission candidate for a strict web design dataset.

Provider track: {provider}
Task id: {brief['taskid']}
Category: {brief['category']}
Style: {brief['style']}
Concept: {brief['concept']}
Brand: {brief['brand_name']}
Audience: {brief['audience']}

Required sections:
{sections}

Required interactions:
{interactions}

Acceptance notes:
{acceptance}

Risks to avoid:
{risks}

Provider-specific emphasis:
{provider_hint}

Instructions:
1. Return only the final `index.html`.
2. Keep all CSS and JS inline.
3. Keep the page runnable by directly opening the file in a browser.
4. Use Google Fonts only if needed and remote imagery only.
5. Use inline SVG icons.
6. Include enough content depth for a full-page screenshot.
7. Make the page feel like a premium real product site rather than a demo.
8. Do not include Markdown code fences or explanations.
"""


def build_repair_prompt(task_id: str) -> str:
    return f"""You are repairing a generated HTML candidate for task `{task_id}`.

Fix the candidate so it passes the validator and still looks premium.

Validation output:
{{VALIDATION_OUTPUT}}

Current HTML:
{{CURRENT_HTML}}

Rules:
- Return only the corrected full `index.html`.
- Keep all CSS and JS inline.
- Keep remote assets only.
- Preserve or improve visual quality while fixing compliance issues.
"""


def build_judge_prompt(task_id: str) -> str:
    return f"""You are judging two HTML candidates for task `{task_id}`.

Score both candidates on:
- compliance
- visual hierarchy
- interaction richness
- content completeness
- semantic structure

Return:
1. winner: gemini or gpt
2. concise rationale
3. risky weaknesses in the losing candidate

Candidate A (Gemini):
{{GEMINI_HTML}}

Candidate B (GPT):
{{GPT_HTML}}
"""


def build_generation_notes(task_id: str) -> str:
    return f"""# Generation Notes

## Automated route

1. Set `X666_API_KEY` and optionally `X666_BASE_URL`, `X666_MODEL_GEMINI`, and `X666_MODEL_GPT`.
2. Run `python skills/web-design-dataset-pipeline/scripts/run_dual_model_pipeline.py {task_id}`.
3. Review `judge-report.md` and the final `src/index.html`.
4. Capture `preview.png` or `preview/preview_*.png`, plus `video.mp4`.
5. Run `python skills/web-design-dataset-pipeline/scripts/package_task.py {task_id}`.

## Manual route

1. Use `prompts/builder-gemini.md` or `prompts/builder-gpt.md` in your target generator.
2. Save the chosen final HTML into `src/index.html`.
3. Run `python skills/web-design-dataset-pipeline/scripts/validate_task.py {task_id} --stage final`.
4. Add preview assets and video before packaging.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a dual-model Web Design dataset task scaffold.")
    parser.add_argument("task_id", help="Task id like fdu_001")
    parser.add_argument("--root", default=".", help="Output root directory")
    parser.add_argument("--category", default="SaaS landing page")
    parser.add_argument("--style", default="Dark Mode")
    parser.add_argument("--concept", default="AI productivity platform")
    parser.add_argument("--audience", default=DEFAULT_AUDIENCE)
    parser.add_argument("--multi-preview", action="store_true", help="Create preview/ for multi-state capture")
    args = parser.parse_args()

    task_root = Path(args.root).resolve() / args.task_id
    src_dir = task_root / "src"
    prompts_dir = task_root / "prompts"

    task_root.mkdir(parents=True, exist_ok=True)
    src_dir.mkdir(parents=True, exist_ok=True)
    prompts_dir.mkdir(parents=True, exist_ok=True)
    if args.multi_preview:
        (task_root / "preview").mkdir(exist_ok=True)

    brief = build_task_brief(args.task_id, args.category, args.style, args.concept, args.audience)

    write_if_missing(task_root / "task-brief.json", json.dumps(brief, indent=2, ensure_ascii=False) + "\n")
    write_if_missing(task_root / "prompt.md", build_prompt(brief))
    write_if_missing(task_root / "generation-notes.md", build_generation_notes(args.task_id))
    write_if_missing(prompts_dir / "builder-gemini.md", build_builder_prompt(brief, "gemini"))
    write_if_missing(prompts_dir / "builder-gpt.md", build_builder_prompt(brief, "gpt"))
    write_if_missing(prompts_dir / "repair.md", build_repair_prompt(args.task_id))
    write_if_missing(prompts_dir / "judge.md", build_judge_prompt(args.task_id))

    print(f"Created dual-model scaffold at {task_root}")
    print("Next steps:")
    print("- Run the automated dual-model pipeline or use prompts/ manually")
    print("- Review judge-report.md after generation")
    print("- Capture preview assets and video before final packaging")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
