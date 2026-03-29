# Web Design Dataset Spec Summary

## Deliverables

Each task must ultimately contain exactly the required submission artifacts:

- `prompt.md`
- `src/index.html`
- `preview.png` or `preview/preview_01.png ...`
- `video.mp4`

## Naming

- Prefix: `fdu`
- Format: `fdu_001`, `fdu_002`, `fdu_003` ...
- Zip name must exactly match `taskid`

## Directory Layout

Single page:

```text
fdu_001/
├── prompt.md
├── preview.png
├── src/
│   └── index.html
└── video.mp4
```

Multi-state preview:

```text
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

## Quality Bar

Target a real modern product site, not a classroom exercise.

- coherent palette
- professional fonts
- strong hierarchy
- consistent spacing
- clear hero focal point
- meaningful motion and hover states
