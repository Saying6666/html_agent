#!/usr/bin/env python3
"""
generate_prompt.py — Prompt 步骤说明器

说明:
    该步骤不再调用外部 API 生成 prompt.md。
    prompt.md 必须由当前读取 web skill 的 agent 手工编写，
    但 prompt 的 4 轮结构与原有要求保持不变。

用法:
    python generate_prompt.py --task fdu_012
"""

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "## round 1",
    "## round 2",
    "## round 3",
    "## round 4",
]

RECOMMENDED_KEYWORDS = [
    ":root",
    "modal",
    "accordion",
    "toast",
    "tabs",
    "scroll reveal",
    "stagger",
    "count-up",
    "navbar scroll transition",
    "aria",
    "default",
    "hover",
    "active",
    "focus",
    "reduced-motion",
    "generate the final code now",
]


GLOBAL_REQUIREMENT_GROUPS = [
    ("禁用框架要求", ["do not use react", "do not use vue", "do not use svelte", "no external libraries", "no gsap", "no jquery", "no build step", "external frameworks", "禁止框架"]),
    ("禁止本地资源要求", ["do not reference local images", "no local image", "禁止本地资源", "local fonts", "local css", "local js", "external resources", "do not reference local"]),
]

ROUND_REQUIREMENT_GROUPS = {
    1: [
        ("页面构建目标", ["create", "build", "design"]),
        ("页面结构描述", ["section", "sections", "page structure", "layout"]),
    ],
    2: [
        ("交互或动效要求", ["interaction", "interactions", "motion", "hover", "animation", "layout and content density", "deepen", "density"]),
    ],
    3: [
        ("响应式要求", ["responsive", "tablet", "mobile", "desktop", "breakpoint"]),
        ("可访问性或合规要求", ["accessibility", "a11y", "aria", "focus", "keyboard", "compliance"]),
    ],
    4: [
        ("最终打磨要求", ["final", "polish", "refinement", "quality assurance"]),
        ("最终交付要求", ["return one complete self-contained", "return only the final", "generate the final code now", "final code", "contained in a single `index.html`", "do not generate code if"]),
    ],
}


def _contains_any(text: str, candidates: list[str]) -> bool:
    return any(candidate in text for candidate in candidates)


def _has_single_file_requirement(text: str) -> bool:
    return (
        "index.html" in text and
        _contains_any(text, ["single-file", "single file", "contained in a single", "self-contained"])
    )


def _has_inline_css_js_requirement(text: str) -> bool:
    return (
        "inline" in text and
        _contains_any(text, ["css", "<style>", "`<style>`"]) and
        _contains_any(text, ["js", "javascript", "<script>", "`<script>`"])
    )


def _extract_round_blocks(content: str) -> dict[int, str]:
    pattern = re.compile(
        r"(?im)^##\s*round\s*([1-4]).*$"
    )
    matches = list(pattern.finditer(content))
    blocks: dict[int, str] = {}

    for index, match in enumerate(matches):
        round_no = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        blocks[round_no] = content[start:end].strip()

    return blocks


def _validate_prompt_content(content: str) -> tuple[list[str], list[str]]:
    """检查 prompt.md 是否满足手工模式下的最小结构要求。"""
    errors: list[str] = []
    warnings: list[str] = []
    normalized = content.lower()
    round_blocks = _extract_round_blocks(content)

    for heading in REQUIRED_HEADINGS:
        if heading not in normalized:
            errors.append(f"缺少章节标题: {heading.replace('## ', '## ').title()}")

    if len(round_blocks) != 4:
        errors.append(f"Round 区块数量不正确，期望 4 个，实际 {len(round_blocks)} 个")

    if len(content.strip()) < 1200:
        errors.append("prompt.md 内容过短，无法支撑完整的 4 轮渐进式提示")

    if not _has_single_file_requirement(normalized):
        errors.append("缺少全局要求: 单文件 index.html 要求")

    if not _has_inline_css_js_requirement(normalized):
        warnings.append("建议确认是否覆盖原有要求: 内联 CSS/JS 要求")

    for name, candidates in GLOBAL_REQUIREMENT_GROUPS:
        if not _contains_any(normalized, candidates):
            warnings.append(f"建议确认是否覆盖原有要求: {name}")

    for round_no, checks in ROUND_REQUIREMENT_GROUPS.items():
        block = round_blocks.get(round_no, "")
        if not block:
            continue

        if len(block) < 180:
            errors.append(f"Round {round_no} 内容过短，信息密度不足")

        block_normalized = block.lower()
        for name, candidates in checks:
            if not _contains_any(block_normalized, candidates):
                errors.append(f"Round {round_no} 缺少要求: {name}")

    for keyword in RECOMMENDED_KEYWORDS:
        if keyword not in normalized:
            warnings.append(f"建议确认是否覆盖原有要求: {keyword}")

    return errors, warnings


def generate_prompt(task_dir: Path, root: Path | None = None,
                    category: str = "", concept: str = "",
                    audience: str = "", style: str = "",
                    site_name: str = "", auto: bool = False) -> Path:
    """校验 prompt.md 是否已由当前 agent 手工编写。"""
    del root, category, concept, audience, style, site_name, auto

    prompt_path = task_dir / "prompt.md"

    print("[INFO] Prompt 步骤已切换为 agent 手工生成模式")
    print("[INFO] prompt.md 的结构与要求保持不变，仍需包含原来的 4 轮内容")
    print(f"[INFO] 最终文件路径: {prompt_path}")

    if not prompt_path.exists() or prompt_path.stat().st_size == 0:
        sys.exit(
            "[ERROR] 未检测到有效的 prompt.md。"
            "请先由当前 agent 按原有要求手工完成 prompt.md"
        )

    content = prompt_path.read_text(encoding="utf-8-sig")
    errors, warnings = _validate_prompt_content(content)
    if errors:
        joined = "\n".join(f"  - {error}" for error in errors)
        sys.exit(
            "[ERROR] prompt.md 存在，但未通过结构校验。\n"
            "请保持原有 prompt 要求不变，并补齐以下内容:\n"
            f"{joined}"
        )

    if warnings:
        print("[WARN] prompt.md 已通过最小结构校验，但建议再核对以下原有要求:")
        for warning in warnings:
            print(f"  - {warning}")

    print(f"[OK] 检测到现有 prompt.md: {prompt_path}")
    return prompt_path


def main():
    parser = argparse.ArgumentParser(description="校验 prompt.md 是否已手工生成")
    parser.add_argument("--task", required=True, help="任务 ID，如 fdu_012")
    parser.add_argument("--root", default=None, help="项目根目录")
    parser.add_argument(
        "--auto",
        action="store_true",
        help="兼容旧参数，现已忽略；prompt.md 需手工生成",
    )
    parser.add_argument("--category", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--concept", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--audience", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--style", default="", help="兼容旧参数，现已忽略")
    parser.add_argument("--site-name", default="", help="兼容旧参数，现已忽略")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent.parent

    task_dir = root / args.task
    if not task_dir.exists():
        task_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / "src").mkdir(exist_ok=True)
        print(f"[INFO] 创建任务目录 {task_dir}")

    generate_prompt(
        task_dir=task_dir,
        root=root,
        category=args.category,
        concept=args.concept,
        audience=args.audience,
        style=args.style,
        site_name=args.site_name,
        auto=args.auto,
    )


if __name__ == "__main__":
    main()
