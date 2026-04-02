# Web Design Dataset Spec Summary

## Deliverables

Each task must ultimately contain exactly the required submission artifacts:

- `prompt.md`
- `src/index.html`
- `preview.png` or `preview/preview_01.png ...`
- `video.mp4`
- `descriptions/fdu_xxx.md` stored in the shared root-level `descriptions/` folder

## Naming

- Prefix: `fdu`
- Format: `fdu_001`, `fdu_002`, `fdu_003` ...
- Zip name must exactly match `taskid`

## Directory Layout

Single page:

```text
descriptions/
└── fdu_001.md

fdu_001/
├── prompt.md
├── preview.png
├── src/
│   └── index.html
└── video.mp4
```

Multi-state preview:

```text
descriptions/
└── fdu_002.md

fdu_002/
├── prompt.md
├── preview/
│   ├── preview_01.png
│   ├── preview_02.png
│   └── preview_03.png
├── src/
│   └── index.html
└── video.mp4
```

## Strictly Forbidden

- `.pen`
- `package.json`
- `node_modules`
- extra files under `src/`
- local asset references such as `./images/x.png`
- local CSS or JS includes
- system junk such as `__MACOSX`, `.DS_Store`, `Thumbs.db`

## Prompt Rules

- Minimum 3 rounds
- Prefer 4 rounds and require the final `prompt.md` to be at least 150 lines unless the user explicitly asks for a shorter format
- Include only prompts given to AI, not AI responses
- Specific and design-directed, not vague
- Prefer explicit content coverage, interaction behavior, information hierarchy, accessibility, responsive requirements, and technical constraints
- Do not hard-code style labels, palette identities, or mood-word stacks into the prompt
- Avoid repeated aesthetic trigger words that make many cases converge to the same look
- Let the model decide the final visual style from the case content instead of prescribing it in the prompt
- If a prompt can be summarized as “preset a moodboard, then fill content into it,” rewrite it
- Use prompt text to constrain content and capability coverage, not to force `midnight/editorial/luxury/glass/glow` style convergence
- Do not hit the line-count target with empty padding; use the extra space for stronger structural constraints, richer interaction details, responsive behavior, accessibility, state design, and differentiation tests
- Skill enforcement note: rewritten `prompt.md` files should default to `>= 150` meaningful lines, and blank filler does not count toward that target

## HTML Rules

- Single-file `index.html`
- Inline `<style>` and `<script>`
- No React/Vue/Svelte build flow
- Works by opening the file directly in a browser
- Use Google Fonts if needed
- Use remote images such as Unsplash URLs
- Use inline SVG icons

## Interaction Baseline

Final page should cover at least 5 interactive behaviors. Typical acceptable patterns:

- button hover
- button active press
- card hover lift
- navigation hover underline or color transition
- scroll reveal animation
- counter animation
- navbar scroll effect
- smooth anchor scrolling
- tabs, accordion, modal, carousel, tooltip, theme switch, form validation, or parallax

## Screenshot Rules

- PNG
- full-page long screenshot
- no browser UI
- no visible mouse cursor if possible
- all images loaded
- all animation elements visible
- counters show final values

## Video Rules

- MP4
- target 24 fps
- full-screen recording
- 4 to 60 seconds
- show full scroll and key interactions
- no tabs, address bar, taskbar, notifications, or unrelated windows

## Natural Language Description Rules

- Descriptions are written manually by the current agent, not by script
- Output path must be `descriptions/fdu_xxx.md`
- Write strictly in top-to-bottom page order
- Emphasize interactions, state changes, reveals, transitions, and post-action feedback
- Do not over-describe static visible content unless it is necessary for understanding
- Do not invent effects or behaviors that are not actually present
- Writing should feel vivid and natural, but still precise and faithful to the page

## QC Rules

- Every completed case should be reviewed by a dedicated QC subagent before delivery
- QC must verify that `prompt.md` still follows the required multi-round prompt structure
- QC must verify that `prompt.md` has at least 150 meaningful lines
- QC must reject prompts containing task placeholders such as `fdu_xxx`, `fdu_012`, `fdu_001`
- QC must verify that `src/index.html` exists, is non-empty, and appears structurally complete
- QC must reject HTML with placeholders, truncation, broken markup, obvious unfinished output, or encoding corruption
- QC result should be explicit: `PASS` or `FAIL` with concrete reasons

## Quality Bar

Target a real modern product site, not a classroom exercise.

- coherent palette
- professional fonts
- strong hierarchy
- consistent spacing
- clear hero focal point
- meaningful motion and hover states
