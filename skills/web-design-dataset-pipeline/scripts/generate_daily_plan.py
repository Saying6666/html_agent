from __future__ import annotations

import argparse
import random
from pathlib import Path


CATEGORIES = [
    "SaaS landing page",
    "Corporate website",
    "Ecommerce product page",
    "Portfolio site",
    "Mobile app landing page",
    "Dashboard",
    "Media or editorial page",
    "Event or conference page",
    "Education platform",
    "Hospitality or travel page",
]

STYLES = [
    "Clean Corporate",
    "Dark Mode",
    "Gradient Mesh",
    "Glassmorphism",
    "Bento Grid",
    "Neo-Brutalism",
    "Minimalist",
    "Organic Warm",
]

CONCEPTS = [
    "AI observability platform",
    "Cloud file collaboration suite",
    "Developer API analytics dashboard",
    "Sustainable luggage brand",
    "Luxury tea subscription",
    "Photography portfolio",
    "Remote design sprint summit",
    "Language learning app",
    "Boutique hotel booking page",
    "Cybersecurity consulting studio",
    "Telehealth wellness app",
    "Creator newsletter platform",
    "Fintech invoicing product",
    "Robotics education academy",
    "Restaurant tasting menu launch",
]

AUDIENCES = [
    "Mid-market product teams",
    "Design-conscious founders",
    "Enterprise buyers",
    "Developers and operators",
    "Young premium consumers",
    "Creative professionals",
]

INTERACTION_PACKS = [
    "hover states, active states, counters, scroll reveal, sticky navbar",
    "hover states, tabs, accordion, scroll reveal, smooth scrolling",
    "hover states, pricing toggle, modal CTA, smooth scrolling, navbar blur",
    "hover states, active states, carousel, counters, FAQ accordion",
]


def task_id(prefix: str, number: int) -> str:
    return f"{prefix}_{number:03d}"


def diversity_score(index: int, category: str, style: str) -> int:
    return 100 - (index % 3) * 5 + len(set(category.split())) + len(set(style.split()))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a diversified daily Web Design task plan.")
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--prefix", default="fdu")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="daily-plan.md")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    concepts = CONCEPTS[:]
    rows = [
        "| taskid | category | style | concept | audience | interaction pack | score |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    for index in range(args.count):
        if not concepts:
            concepts = CONCEPTS[:]
        rng.shuffle(concepts)
        category = CATEGORIES[index % len(CATEGORIES)]
        style = STYLES[(index * 3) % len(STYLES)]
        concept = concepts.pop()
        audience = AUDIENCES[(index * 5) % len(AUDIENCES)]
        interaction_pack = INTERACTION_PACKS[(index * 7) % len(INTERACTION_PACKS)]
        score = diversity_score(index, category, style)
        rows.append(
            f"| {task_id(args.prefix, args.start + index)} | {category} | {style} | {concept} | {audience} | {interaction_pack} | {score} |"
        )

    output = Path(args.output)
    output.write_text("# Daily Web Design Plan\n\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"Wrote {args.count} tasks to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
