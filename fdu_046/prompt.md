## Round 1

Build a production-grade single-page website for **Ember Atlas**, an urban heat-risk intelligence platform used by real-estate operators, venue groups, civic teams, and infrastructure planners.
This must feel like a real 2025-2026 product experience.
It must not collapse into a generic B2B landing-page skeleton.

This case has a specific art direction: **Thermal Cartography Briefing**.
Think: a heat-risk bulletin laid over a live thermal field.
No "startup hero + nice cards" energy.

Material language (bind every choice to heat-risk operations):
- Asphalt grain and sun-bleached concrete as base textures.
- Caution stripes and hazard labeling as a functional accent.
- Paper report sheets layered on top of field data.
- Inked contour lines (isotherms) and district boundaries.
- Heat shimmer as a motion metaphor (subtle, not gimmicky).

Color logic:
- Define a calibrated temperature ramp as tokens (cold -> warm -> hot).
- Use the ramp as signal, not as decoration.
- Keep neutrals as paper/ink/terrain; reserve alert color for true states.
- Include semantic colors for success/warning/danger, but map them to the domain (advisory, watch, alert).

Typography logic:
- Display: condensed, urgent, operational (alerts, headers, siren lines).
- Reading: calm, high-legibility (briefing paragraphs, procurement copy).
- UI/Label: compact, technical (coordinates, timestamps, confidence).
- Do not ship with generic default type; choose intentional system-aware stacks.

Structural mandate (do not ignore): **Split Stage + Dossier Chapters**.
- Desktop must be two-track:
  - Left: sticky "Thermal Field" stage (inline SVG or canvas is allowed).
  - Right: numbered briefing chapters.
- The stage is not decoration.
- As the reader enters chapters, the stage must change state at least 4 times:
  - layer toggles
  - district focus
  - hotspot clustering
  - corridor overlays
  - confidence shading
- At least 3 chapters must use different layout logic.
- Avoid repeating a single container/card pattern across the whole page.

Chapter map (use codes to prevent generic sections):
- CH-01 DISPATCH (current state)
- CH-02 SIGNALS (what is measured)
- CH-03 DISTRICTS (where it bites)
- CH-04 CORRIDORS (how to route safety)
- CH-05 PLAYBOOK (detect/route/protect/report)
- CH-06 CASE FILE (a real incident narrative)
- CH-07 STACK FRACTURE (comparison theater)
- CH-08 PROCUREMENT (FAQ, policy, provenance)

Thermal Field stage spec:
- Must render:
  - contour lines
  - hotspots (clusters)
  - at least one corridor overlay (route ribbon)
  - at least one asset overlay (cooling sites / shade islands)
  - confidence mask (high/medium/low)
- Must have a clear legend and a compact scale indicator.
- Must have a mode label that changes with tabs and scroll.
- Must not rely on external images.

Content modules (choose 10-14; rename and reorder freely; must stay heat-risk specific):
- Dispatch header with city/date/time and a clear risk tier.
- "Risk at a glance" strip with 4-6 labeled metrics.
- Thermal Field stage (sticky).
- Signal inventory as annotated instruments (not a feature card grid).
- Role views (tabs) for:
  - Venue Ops
  - City Desk
  - Property Portfolio
- Response playbook as a decision tree + checklist.
- Cooling corridors as a diagram with callouts and constraints.
- Case file as evidence: timestamps, actions, outcomes.
- Stack fracture comparison as two briefing boards.
- Metrics as instrumentation with Count-up.
- FAQ / objections (procurement, privacy, data provenance).
- Final CTA to book a field review (modal trigger + compact form).
- Footer: compliance note + provenance.

Copy tone:
- Operational, credible, and specific.
- Avoid vague AI hype.
- Use city/venue language, not generic "optimize outcomes".

Token system requirement (CSS `:root`):
- `--temp-cold-*`, `--temp-warm-*`, `--temp-hot-*` ramp stops.
- `--terrain-*` for background layers and noise.
- `--contour-*` for line colors and weights.
- `--surface-paper-*`, `--surface-asphalt-*`, `--surface-alert-*`.
- `--text-*`, `--muted-*`, `--label-*`, `--focus-*`.
- `--shadow-*`, `--radius-*`, `--space-*`, `--container-*`.
- `--dur-*`, `--ease-*` for motion consistency.

Technical constraints (non-negotiable):
- Output one complete self-contained single-file `index.html`.
- All CSS inside `<style>`, all JavaScript inside `<script>`.
- Inline CSS/JS only.
- Do not use React, Vue, Svelte.
- Do not use jQuery, GSAP.
- No external libraries, no build step.
- Do not reference local images, local fonts, local CSS, or local JS.
- Prefer pure CSS texture, inline SVG, and procedural noise over stock art.
- Do not use `style=""` inline styles in markup.

## Round 2

Interaction and motion must feel like an instrumented briefing.
Not generic web UI polish.

Required functional interactions (all must be implemented and actually work):
1. **Modal**: "Book a field review".
   - Open from multiple CTAs.
   - Include selection steps (site type / district / time window).
   - Update a live summary inside the modal before submit.
2. **Accordion**: procurement objections and policy notes.
3. **Toast**: after submit and after saving a setting.
4. **Tabs**: role/layer switching that changes the Thermal Field stage.
5. **Scroll reveal**: a single consistent heat-field reveal grammar.
6. **Stagger animation**: evidence rows or incident steps.
7. **Count-up**: metrics count up when visible (instrument style).
8. **Navbar scroll transition**: compress into an alert rail showing:
   - active chapter code
   - risk tier chip
   - minimal legend indicator

Mandatory narrative behaviors:
- On chapter enter, update the stage state (district + layer).
- On tabs change, update the stage and the right-side content panel.
- At least 2 interactions must materially change navigation or content depth.

Interaction styling rules:
- Hover must change structure (stroke weight, label exposure, crop, depth), not only color.
- Active must feel pressed/confirmed (stamp or latch).
- Focus must be visible and consistent on all controls.

Motion rules:
- Prefer mask/contour wipe, legend draw, and field shimmer.
- Avoid using opacity+translate as the only motion language.
- Support `prefers-reduced-motion`:
  - disable continuous shimmer
  - keep reveals instant or minimal
  - keep state transitions clear via styling, not animation

## Round 3

Responsive behavior must preserve the briefing concept.

Breakpoints:
- `>= 1440px`: true Split Stage; generous annotation rails; wide dossier columns.
- `1024px - 1439px`: keep Split Stage but tighter; stage may become smaller but still sticky.
- `768px - 1023px`: stage becomes a top "field strip" that updates with scroll; tabs become a rail.
- `< 768px`: do not collapse into a generic centered column.
  - Use a briefing-native mobile mode:
    - compact stage
    - numbered dispatch cards
    - persistent alert chip
    - clear active chapter indicator

Accessibility requirements:
- semantic landmarks: `header`, `nav`, `main`, `section`, `footer`.
- correct heading hierarchy.
- ARIA for Modal, Tabs, Accordion, Toast, and live status labels.
- accessible names for all form controls.
- `aria-label` for icon-only buttons.
- keyboard support for modal/tabs/accordion.
- Escape closes the modal.
- visible focus states throughout.
- support `prefers-reduced-motion`.
- do not rely on color alone to communicate risk tiers or selection.

Implementation notes for a11y:
- Tabs must use proper roles and `aria-selected`.
- Accordion triggers must use `aria-expanded` and `aria-controls`.
- Toast must be announced via an `aria-live` region.
- Modal must manage focus and restore focus on close.

Technical constraints remain strict:
- single-file `index.html`
- inline CSS and inline JavaScript only
- no local assets
- no frameworks
- if `backdrop-filter` is used, include `-webkit-backdrop-filter` before `backdrop-filter`
- no `style=""` inline styles
- readable multi-line HTML and JS (not minified)

## Round 4

Polish until this reads like a shipped heat-risk product, not a template.

Final acceptance checklist:
- One complete self-contained single-file `index.html`.
- Inline `<style>` and `<script>` only.
- Complete `:root` token system with a temperature ramp.
- 10+ meaningful modules and chapters with codes.
- Required interactions implemented:
  - Modal
  - Accordion
  - Toast
  - Tabs
  - Scroll reveal
  - Stagger animation
  - Count-up
  - Navbar scroll transition
- Thermal Field stage changes state at least 4 times and reacts to Tabs.
- Default/Hover/Active/Focus states are strong and consistent.
- Keyboard and reduced-motion behaviors are correct.
- No local resources and no external libraries.

Final differentiation test (non-negotiable):
- If it still looks like hero + features + metrics + FAQ + CTA, redesign the skeleton.
- If the stage is decorative, redesign until it drives the narrative.
- If motion is only opacity + translate, replace with contour/mask/field-driven reveals.
- If "Signals" reads like generic feature cards, rebuild as instruments and annotations.

GENERATE THE FINAL CODE NOW
