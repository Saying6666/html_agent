## Round 1

Document type: HARBOR SIGNAL BOARD SPECIFICATION
Product: **Pelorus Tide**
Audience: ports, insurers, city operations teams
Deliverable: one single-file `index.html`

Intent:
Make a 2025-2026 launch page that looks like real civic/port infrastructure.
Do not look like a generic premium SaaS site.
Do not look like a moody glass dashboard.
This case must feel like enamel signage and operational wayfinding.

Case-specific visual world (commit):
Theme: enamel plates + riveted steel + hazard banding.
Palette constraints:
- enamel white and warm off-white as primary base
- deep navy as main ink field
- rescue orange as primary accent
- buoy yellow as secondary accent
- sea-glass teal only as a small technical highlight
Material language:
- painted steel depth (shadows, bevels, rivets)
- thick route strokes and arrowheads
- screen-printed pictograms
- warning chevrons and hazard bands
Typography:
- bold condensed caps for headings
- crisp utilitarian body sans
- mono for coordinates, timestamps, and codes

Layout archetype (must commit):
Operations corridor of sign panels.
Each major section is a distinct signboard with its own grid.
Avoid uniform rounded cards.
Prefer:
- boards
- strips
- tables
- route diagrams
- annotated schematics

Signature device (must be visible in hero):
An inline-SVG "harbor route board".
The board must contain:
- route lines and segment labels
- buoy markers and beacons
- tide window bands (safe / watch / warn)
- alert stamps and an action legend
The board must respond to user interaction later (tabs + filters + scrubber).

Design system requirements:
Define a complete CSS token system in `:root`.
Tokens must cover:
- enamel backgrounds and steel surfaces
- hazard bands and warning chevrons
- borders, separators, and line weights
- text hierarchy and label styles
- focus ring colors and thickness
- status colors: safe/watch/warn/critical
- spacing scale and content widths
- radii (mostly sharp) and shadow depth
- type scale and motion tokens
Use tokens consistently.
Avoid one-off color hacks.

Technical constraints (non-negotiable):
- Return one complete self-contained `index.html`
- Single-file only
- All CSS inside `<style>`
- All JS inside `<script>`
- Inline CSS and inline JS only
- Do not use React, Vue, Svelte
- Do not use jQuery
- Do not use GSAP
- No external libraries and no build step
- Do not reference local images, local fonts, local CSS, or local JS
- Prefer inline SVG and pure CSS construction
- Do not use `style=""` in markup

Content coverage (ingredients, not fixed order):
Include 10+ meaningful modules.
Reorder freely.
The silhouette must not be "hero + grid + metrics + FAQ + CTA".

Required coverage, expressed as signage modules:
1. Top rail: "Harbor Status" with live tide note and service note.
2. Hero: a strong thesis about incident coordination under tide windows.
3. Trust: data provenance and deployment credibility (not logo fluff).
4. "Route Board" capability story (diagram-first, not feature cards).
5. "Command Board" interactive area (tabs + filters + board state).
6. Metrics band with quantified outcomes (count-up required).
7. Response protocol timeline (roles, handoffs, time-to-action).
8. Comparison: fragmented workflow vs Pelorus Tide (operationally brutal, realistic).
9. Case file spotlight with timestamps and clear outcomes.
10. FAQ as "protocol notes" (accordion required).
11. Conversion: briefing request form and policy/compliance notes.
12. Footer: dense navigation and procurement-friendly language.

Copy direction:
- Sound like port ops and civic coordination, not AI hype.
- Use credible terms: windows, thresholds, staging, mutual aid, audit trail.
- Keep density high but legible.
- Avoid generic "empower" and "transform" language.

No-go list for this case:
- no purple gradients
- no full-page blur glass
- no soft blob backdrops
- no repeated rounded card grids

## Round 2

Deepen the page with meaningful interactions and controlled motion.
You must implement at least 8 real interactions.
You must explicitly include every required interaction below.
Each must feel like a harbor instrument.

Required interactions (must include all):
1. **Modal**
Label: "Request a coastal briefing".
Modal must open from hero CTA and from the command board.
It must trap focus.
Escape closes.
Return focus to the trigger.
It must look like a riveted panel or clipboard, not a generic dialog.

2. **Accordion**
Use for FAQ / protocol notes.
Expanded state must be obvious via icon and spacing, not only color.
ARIA and keyboard support required.

3. **Toast**
After form submit or "Save playbook", show a toast: "Signal sent".
Toast must announce via polite live region.
Include dismiss action and auto-hide.

4. **Tabs**
Tabs must control the command board state.
Tab names should be operational:
Examples: "Routes", "Assets", "Alerts", "Resources".
Switching tabs must update:
- the SVG board view
- at least one KPI stack
- at least one timeline highlight

5. **Scroll reveal**
Panels should reveal like signage sliding onto brackets.
Avoid one-size fade-up everywhere.
Use a consistent reveal language.
Respect reduced motion.

6. **Stagger animation**
Use stagger for:
- buoy markers
- schedule rows
- protocol steps
Not for a generic feature grid.

7. **Count-up**
Metrics must count up when visible.
Style numbers like pier counters and milestone plaques.

8. **Navbar scroll transition**
Top rail must compress into a thin control strip after scrolling.
It should increase border contrast and add subtle elevation.
It must remain readable on all breakpoints.

Add at least 2 extra case-specific behaviors:
- Tide-window scrubber (range input).
Scrubbing updates the tide bands on the route board and changes copy.
- Segment filter chips for port types / asset classes.
Filters update what is visible in the board and case file list.

Interaction state requirements:
Define strong Default/Hover/Active/Focus for:
- buttons
- tabs
- chips
- accordion triggers
- form fields
- icon buttons
States must change weight, thickness, underline, or shape.
Do not rely on subtle color shifts only.

Motion direction:
- infrastructural, calm, confident
- no playful bounce
- no excessive blur
- emphasize clarity and orientation

## Round 3

Responsive requirements:
Support 4 breakpoints and recompose the signage system.
Do not collapse into a bland single-column card stack.

Breakpoints:
- `>= 1440px`
Wide corridor layout.
Persistent route board visible alongside panels.
Dense tables and clear grid alignment.

- `1024px - 1439px`
Route board becomes sticky.
Panels tighten and typography scales down carefully.

- `768px - 1023px`
Route board becomes collapsible.
Tabs become touch-first rail.
Tables become scrollable with sticky headers.

- `< 768px`
Convert panels into stacked sign plates.
Use thick separators and strong headings.
Keep the signature SVG visible early.
Keep CTAs reachable with thumb.

Accessibility requirements (mandatory):
- semantic landmarks: `header`, `nav`, `main`, `section`, `footer`
- correct heading hierarchy
- ARIA for modal, tabs, accordion, toast, and live status
- accessible names for all form controls and range inputs
- `aria-label` for icon-only buttons
- keyboard support for modal, tabs, accordion, chips, scrubber
- Escape closes modal
- visible focus states across the page
- support `prefers-reduced-motion`
- do not rely on color alone for status, selection, or expanded state

Reduced motion strategy:
- remove nonessential reveal and stagger
- keep state changes visible via contrast and layout
- replace count-up with instant numbers

Technical constraints remain strict:
- one single-file `index.html`
- inline CSS and inline JS only
- no local assets
- no frameworks
- if `backdrop-filter` is used, include `-webkit-backdrop-filter` before `backdrop-filter`
- no `style=""`
- final HTML readable and maintainable

## Round 4

Polish the final page as if it were going to procurement review.
Make it unmistakably Pelorus Tide and unmistakably signage-driven.

Polish targets:
- icon system coherence (stroke weight, corner treatment, arrowheads)
- consistent line weights across SVG and CSS
- crisp headings and label chips
- strong but not noisy hover/active states
- consistent focus ring tokens
- tabs and filters feel like instruments, not generic pills

QA checklist:
- single-file `index.html` only
- inline `<style>` and `<script>`
- no frameworks, no local assets, no `style=""`
- modal works (focus trap, Escape close, restore focus)
- accordion works (ARIA, keyboard, obvious expanded state)
- toast works (live region, dismiss, auto-hide)
- tabs work (ARIA, keyboard, SVG board updates)
- scroll reveal works and respects reduced motion
- stagger works and respects reduced motion
- count-up works and respects reduced motion
- navbar scroll transition works
- tide scrubber updates the route board
- segment filters update content
- responsive behavior works across 4 breakpoints

Return only the final production-ready HTML in one `index.html`.

GENERATE THE FINAL CODE NOW

