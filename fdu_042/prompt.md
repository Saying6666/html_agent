## Round 1

Director's note: This page is a night logbook that occasionally snaps into a precision instrument panel.
It must feel like a field journal you could actually use under a red headlamp, not a generic "dark premium landing page".
Every scene should have a reason: sky conditions, timings, coordinates, and a clear invitation to book.

Design and build a distinctive 2025-2026 single-file website for **Nocturne Atlas**, a night-exploration studio curating astronomy retreats, observatory residencies, and guided dark-sky expeditions.

### Core Constraints (Must Keep)
- Return one complete self-contained `index.html` only
- Single-file only; all CSS inside `<style>`; all JS inside `<script>`
- Inline CSS/JS only; no build step
- No React/Vue/Svelte; no jQuery; no GSAP; no Tailwind CDN; no external libraries
- Do not reference local images, local fonts, local CSS, or local JS
- Do not rely on stock photography; prefer CSS gradients, inline SVG, and/or canvas
- Do not use `style=""` inline attributes in markup
- Keep HTML readable and multi-line
- Output only the final `index.html` code (no prose outside code)

### Theme + Visual Logic (Make This Case Recognizable)
Commit to a "red-lamp field journal + brass instrument" aesthetic:
- palette:
  - deep ink night
  - warm paper-ivory
  - dim red headlamp accents (for interactive highlights and warnings)
  - pale star-cyan highlights (for sky markers)
  - ban: purple startup gradients and generic neon gamer glow
- materials:
  - paper grain and subtle fibers
  - graphite scribbles and margin notes
  - stamped coordinates and timecodes
  - etched brass rings and lens markings
  - lens flare halos used sparingly (do not overdo)
- typography:
  - literary display for titles (journal/editorial vibe)
  - crisp UI sans for controls
  - monospaced micro labels for coordinates, times, IDs
- composition:
  - big negative space like a sky dome
  - dense micro labels near instruments
  - asymmetrical spreads like magazine pages
- motion language:
  - slow parallax drift
  - scan sweeps across star charts
  - gentle dial/needle easing
  - ban: repeating the same opacity+translate reveal for everything

Build a complete design system in CSS `:root` tokens:
- background layers (sky wash, paper texture), surfaces/panels, borders/dividers, shadows, highlight glows
- text hierarchy and muted text; semantic colors for status
- accent / accent-soft / accent-strong
- radii, spacing scale, content widths, section padding
- font stacks (display/body/mono), type scale (display, h1-h3, body, label, fine print)
- durations and easing curves

Token rules:
- include `--focus-ring` and `--tap-target` sizing tokens
- ensure all controls share consistent heights and rhythm
- include tabular numerals for instrument readouts

### Modules + Chapters (Structure As 4 Scenes, Not A Template)
Make at least 10 meaningful blocks total, but organize the page into 4 structurally distinct scenes:

Scene A: "Red Light Briefing" (Hero)
- sticky navbar that feels like an expedition header (brand, anchors, primary action)
- hero as a full-bleed "sky dome" with oversized thesis line + supporting paragraph + 2 CTAs
- a right-side (or overlay) "Instrument Stack": altitude dial, seeing quality, moon phase, next dark window

Scene A must include:
- a "Tonight's window" strip with:
  - start time
  - end time
  - moon illumination %
  - cloud cover %
- copy that reads like field notes, not marketing fluff

Scene B: "Star Chart Room" (The Signature Interaction)
- an interactive star chart rendered via canvas or inline SVG (no external assets)
- a time scrubber / slider (evening -> midnight -> dawn) that changes star density + highlights constellations
- a "route selector" that reconfigures recommended observation sets and updates 2-3 live numbers

Scene B plausibility hints:
- include a small legend: magnitude, horizon line, north marker
- star chart does not need to be astronomically perfect, but it must feel intentional and coherent

Scene C: "Programs As Constellations" (Tabs + Editorial Content)
- tabs for 3 modes: Retreat / Residency / Expedition
- each tab reveals a different layout silhouette (not just swapping text in the same card grid)
- a "Field Notes" band: short log entries, coordinates, and a credibility section (methodology, gear, safety protocol)

Scene C must include:
- a "gear + method" credibility module:
  - why the guides are credible
  - what safety measures exist
  - what weather contingency plan looks like

Scene D: "Booking + Proof + Objections"
- count-up metrics band (nights hosted, dark-sky hours, partner observatories)
- itinerary timeline that reads like a night sequence (civil twilight -> nautical -> astronomical -> dawn)
- FAQ with accordion
- booking/contact section with form + trust cues + a closing CTA
- footer with policy/contact

Scene D must include:
- a short "dark-sky etiquette" note
- a "what to bring" checklist that can be expanded/collapsed

Hard bans:
- no hero + 3 feature cards + metrics + FAQ silhouette
- no uniform card farm across the entire page
- no generic "dark glass dashboard" SaaS look; keep it journal-like and instrument-driven

Distinctiveness alarms:
- if it looks like any random "dark luxury" site
- if the star chart is decorative and not interactive
- if all sections use the same container and card style

## Round 2

Deepen the interface with real interactions and authored motion. Implement at least 8 meaningful functional interactions, and explicitly include all of the following capabilities:
- **Modal**: "Request a Route" (opened from hero CTA and from a program section)
- **Accordion**: FAQ
- **Toast**: after saving a star chart preset or submitting the request form
- **Tabs**: program modes (Retreat / Residency / Expedition)
- **Scroll reveal**: scene cues (mask reveal / scan sweep / page-turn) rather than only opacity+translate
- **Stagger animation**: for log entries, gear items, or constellation highlights
- **Count-up**: metrics band (only when visible)
- **Navbar scroll transition**: header compacts; a small "sky status" chip persists

Important: explicitly keep these words in your implementation notes:
- Modal
- Accordion
- Toast
- Tabs
- Scroll reveal
- Stagger animation
- Count-up
- Navbar scroll transition

Case-specific interaction focus (must materially change content depth):
1. "Time Scrubber" updates the star chart AND swaps the recommended plan snippet (narrative behavior).
2. Hover/focus on constellation labels to reveal a detail popover (myth/coordinates/visibility window).

Additional optional interactions (choose 2-4):
- "Brightness mode" toggle (red light mode vs normal) that changes the UI palette
- "Altitude threshold" slider that filters recommended targets
- "Save kit list" button that triggers a Toast and updates a small saved state
- "Jump to chapter" contents rail with active section highlight

Interaction personality rules:
- default/hover/active/focus states must change depth, crop, or hierarchy (not only color)
- include keyboard support for all required widgets; do not hide important content behind hover only

Keyboard and ARIA specifics (must implement):
- Modal:
  - `role="dialog"` + `aria-modal="true"`
  - focus trap; Escape closes; restore focus
- Tabs:
  - `role="tablist"`, `role="tab"`, `role="tabpanel"`
  - arrow keys to move
- Accordion:
  - `aria-expanded`, `aria-controls`, button semantics
- Toast:
  - `aria-live="polite"`; dismiss button

Reduced motion:
- respect `prefers-reduced-motion: reduce`
- scan sweeps become static; reveals become instant; count-up becomes immediate

## Round 3

Responsive requirements (4 breakpoints):
- `>= 1440px`: big sky dome composition; instrument stack sits like a side panel; star chart has real room
- `1024px - 1439px`: keep asymmetry; tighten spacing; preserve the editorial spread feeling
- `768px - 1023px`: instruments become a horizontal rail; star chart becomes the main focal panel
- `< 768px`: simplify star chart density; keep time scrubber thumb-friendly; tabs become a compact segmented control

Breakpoint-specific behavior:
- mobile:
  - star chart becomes a single focal panel with large tap targets
  - instrument rail becomes swipeable (still keyboard accessible)
- tablet:
  - time scrubber remains visible near the chart
  - program tabs can become sticky within the scene

Accessibility requirements:
- semantic landmarks (`header`, `nav`, `main`, `section`, `footer`)
- correct heading hierarchy
- ARIA + keyboard support for modal, tabs, accordion, toast; Escape closes modal; focus management in dialog
- `aria-label` for icon-only controls; accessible names for all form inputs
- visible focus states; sufficient contrast even in dark theme
- `prefers-reduced-motion` supported (scan/reveal/stagger/count-up become instant or softened)
- do not rely on color alone for status/selection (use labels/icons)

Accessibility nuance:
- constellation popovers must be reachable by keyboard
- star chart controls must have labels (not icon-only without `aria-label`)
- ensure tap targets are comfortable and not tiny micro text

## Round 4

Polish until it feels like a real 2025-2026 boutique studio:
- tighten typography rhythm (editorial titles + mono coordinates)
- keep motion slow, deliberate, and instrument-like
- ensure the star chart interaction feels central and unique to this case

Final polish prompts:
- copy:
  - replace generic text with field-journal microcopy
  - include realistic timing, location hints, and safety guidance
- visuals:
  - paper grain should be subtle, not noisy
  - brass lines should not turn into kitsch
- interactions:
  - every state is readable in reduced motion mode
  - keyboard-only flow is smooth

Final acceptance checklist (must all be true):
- one complete self-contained `index.html`
- inline `<style>` and `<script>` only; no frameworks; no local resources; no `style=""`
- responsive across 4 breakpoints; accessible semantics + ARIA + keyboard + reduced motion
- required capabilities implemented: modal, accordion, toast, tabs, scroll reveal, stagger, count-up, navbar scroll transition
- 10+ meaningful blocks with at least 3 structurally different chapters

Before printing the final HTML, sanity-check:
- does the first viewport feel like sky + journal + instruments?
- does the time scrubber change multiple things (chart + plan + numbers)?
- can I complete the booking flow with keyboard only?

GENERATE THE FINAL CODE NOW
