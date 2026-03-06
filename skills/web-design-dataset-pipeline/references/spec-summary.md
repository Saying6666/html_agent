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
- Include only prompts given to AI, not AI responses
- Specific and design-directed, not vague
- Prefer explicit style, palette, font, sections, animation, and responsive requirements

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
