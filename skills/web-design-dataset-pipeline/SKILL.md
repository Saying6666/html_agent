---
name: web-design-dataset-pipeline
description: Delivery-first workflow for Web Design dataset tasks. Use when Codex needs to define page style, prompt rounds, final folder structure, and optional automation for `fdu_xxx` submissions.
---

# Web Design Dataset Pipeline

Use this skill when the goal is to produce a Web Design dataset submission that is ready to hand off as `fdu_xxx`. This skill is delivery-first: lock the brief, define style clearly, generate prompts, produce a runnable single-file page, capture assets, and only use validation or packaging scripts if the user wants them.

If the workflow is not prompt-only, the generation route should use `anthropic-sdk-helper` and a fixed 4-step Claude conversation that ends by writing the final `src/index.html`.

## Default Mode

Default to **manual-first delivery mode**.

- Start from the final deliverable structure, not the automation pipeline.
- Default to prompt-only scaffolding when starting a task.
- Treat local validation as optional by default.
- Treat packaging scripts as optional by default.
- Use automated generation only when the user wants final HTML output from a scripted 4-step Claude generation flow.

If the user does not explicitly ask for validator-driven checks, do not make validation a required step in the workflow.

## Final Deliverable First

Every task should be planned backward from the final submission folder.

### Single-page preview delivery

```text
fdu_001/
├── prompt.md
├── preview.png
├── src/
│   └── index.html
└── video.mp4
```

### Multi-preview delivery

```text
fdu_001/
├── prompt.md
├── preview/
│   ├── preview_01.png
│   ├── preview_02.png
│   └── preview_03.png
├── src/
│   └── index.html
└── video.mp4
```

### Packaging rule

- The outer archive should be `fdu_001.zip`.
- The folder inside the zip should be `fdu_001/`.
- Do not ship `.pen` files.
- Do not ship prompt working folders, hidden pipeline folders, or model scratch files unless the user explicitly asks for an internal workflow package instead of the final submission package.

## Lock The Brief Before Building

Before generating or refining prompts, always lock these fields:

- `taskid`
- `category`
- `visual style`
- `concept`
- `audience`
- `required sections`
- `required interactions`

Do not accept vague inputs like `modern landing page` as a finished brief. Push the brief toward something concrete such as `AI observability SaaS`, `dark mode`, `glassmorphism`, `DevOps audience`, `pricing + FAQ + integrations`, and `scroll reveal + counter + accordion`.

## Style Must Be Explicit

Each task must specify style direction clearly inside the brief and prompts.

### Style stack

Every task should define all of the following:

1. **Primary style reference**
   - Choose one or two directions such as `Awwwards`, `Godly`, `Land-book`, `Bento Grid`, `Dark Mode`, `Neo-Brutalism`, `Clean Corporate`, or `Gradient Mesh`.
2. **Component reference**
   - Choose a UI language such as `Aceternity UI`, `Magic UI`, or `Shadcn/ui`.
3. **Color direction**
   - Define palette mood, contrast level, and accent behavior.
4. **Typography direction**
   - Define heading feel and body feel.
5. **Motion direction**
   - Define whether motion should feel subtle, product-like, dramatic, playful, or editorial.

### Style guidance

- Reference style families, not exact branded clones.
- Borrow visual language and interaction patterns, not copyrighted compositions.
- Keep the design aligned with the target audience.
- Make the page feel like a real 2025-2026 product site rather than a classroom demo.

## Prompt Rules

`prompt.md` is part of the final delivery and must follow these rules:

- Include exactly 4 rounds of prompts.
- Include prompts only, not AI responses.
- Keep prompts concrete and design-directed.
- Explicitly mention style, palette, typography, sections, interactions, motion, and compliance constraints.
- Keep the later rounds focused on depth, polish, and compliance rather than restating the same high-level idea.

Good prompt progression:

- Round 1: define concept, audience, structure, and visual direction.
- Round 2: deepen layout, content density, hierarchy, and section detail.
- Round 3: polish interaction states, responsiveness, and compliance.
- Round 4: final refinement and compliance pass.

## HTML Rules

`src/index.html` must meet the delivery spec directly.

- Single-file HTML only.
- Inline `<style>` and inline `<script>`.
- Opens directly in a browser with no build step.
- No React, Vue, Svelte, jQuery, or compile step.
- No local images, local fonts, local CSS, or local JS.
- Use remote imagery such as Unsplash or placeholder services if needed.
- Use inline SVG icons or approved icon sources translated into inline SVG.

The page should look complete without relying on any local project assets.

## Screenshot Rules

For preview assets:

- Use long full-page screenshots.
- Remove browser tabs, address bars, and popups.
- Hide the cursor if possible, or keep it off to the side.
- Use `preview.png` for a single-page preview.
- Use `preview/preview_01.png`, `preview/preview_02.png`, and so on for multi-state or multi-screen delivery.
- Ensure the preview matches the prompt and final HTML exactly.

## Video Rules

For `video.mp4`:

- Record the full screen.
- Use MP4.
- Target 24 fps.
- Keep duration between 4 and 60 seconds.
- Show the full interaction story: scrolling, hover states, toggles, accordions, tabs, counters, or similar behaviors.
- Avoid browser chrome, system popups, unrelated windows, and partial-window capture.

## Quality Bar

The result should feel like a polished modern website.

- strong visual hierarchy
- coherent spacing and rhythm
- professional typography
- clear hover and active states
- believable product copy and section depth
- natural animation and interaction timing
- enough vertical content for long screenshot capture

## Recommended Working Sequence

Use this order unless the user wants a different workflow:

1. Lock the brief.
2. Lock the style stack.
3. Write `prompt.md` with exactly 4 rounds.
4. Generate or refine `src/index.html`.
5. Capture `preview.png` or `preview/preview_*.png`.
6. Record `video.mp4`.
7. Review against the checklist.
8. Optionally validate or package.

## Delivery Checklist

Before handoff, verify:

- file structure is correct
- naming is correct
- `src/index.html` opens directly
- preview matches the page and prompt
- all images load correctly
- hover and active states exist
- there is no copyright risk
- video is full-screen MP4 and intended for 24 fps delivery
- browser zoom changes do not break the layout badly

## Optional Automation

These tools are available, but they are optional unless the user asks for them.

### Planning and scaffolding

- `python skills/web-design-dataset-pipeline/scripts/generate_daily_plan.py`
- `python skills/web-design-dataset-pipeline/scripts/run_task_workflow.py fdu_001 --category "SaaS landing page" --style "Dark Mode" --concept "AI observability platform"`
- `python skills/web-design-dataset-pipeline/scripts/bootstrap_task.py fdu_001 --category "SaaS landing page" --style "Dark Mode" --concept "AI observability platform"`

The `run_task_workflow.py` entry defaults to `--mode prompt-only`, which creates the prompt package and task scaffold without calling any external model API.

### Anthropic generation

- `python skills/web-design-dataset-pipeline/scripts/run_claude_generation.py fdu_001`
- `python skills/web-design-dataset-pipeline/scripts/run_task_workflow.py fdu_001 --mode generate --category "SaaS landing page" --style "Dark Mode" --concept "AI observability platform"`

Use this only when the user wants the final HTML generated automatically. The script should use `anthropic-sdk-helper`, read Claude credentials from ccswitch or Claude config, and run exactly 4 conversation steps based on `prompt.md` before writing the final `src/index.html`.

### Validation

- `python skills/web-design-dataset-pipeline/scripts/validate_task.py fdu_001 --stage scaffold`
- `python skills/web-design-dataset-pipeline/scripts/validate_task.py fdu_001 --stage final`

Validation is an optional self-check. Do not present it as mandatory unless the user asks for strict local QA.

### Packaging

- `python skills/web-design-dataset-pipeline/scripts/package_task.py fdu_001`

Packaging is optional during production. Use it when the user wants a final zip or batch handoff artifact.

## Team Mode

If the user wants a team-style or subagent workflow, use these roles:

### Planner

- locks category, style, concept, audience, sections, and interactions
- defines the style stack clearly
- writes the 4 prompt rounds

### Builder

- turns the prompt package into a single polished `src/index.html`
- keeps CSS and JS inline
- keeps assets remote-only
- uses the 4-step Anthropic conversation when generation is automated

### QA Packager

- checks the final delivery structure
- confirms preview and video completeness
- optionally runs validation and packaging scripts

Use `references/team-playbook.md` when the user specifically asks for handoff schema or team coordination.

## Operating Rules

- Never hardcode API keys in prompts or tracked files.
- Never ship `.pen`, `package.json`, `node_modules`, or extra files under `src/`.
- Never use local asset paths.
- Never treat validator output as required by default.
- Never accept weak placeholder-heavy pages as final.
- Never bypass `anthropic-sdk-helper` when the task uses automated Claude generation.
- Prefer English prompts unless the user asks otherwise.

## References

- `references/spec-summary.md`: condensed acceptance criteria.
- `references/team-playbook.md`: team workflow and handoff contract.
