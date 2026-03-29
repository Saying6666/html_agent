## Round 1

Create a 2025-2026 single-page product site for **Northline Harbor**, an urban ferry membership service for commuters, hotel concierges, event hosts, and waterfront residents who want a calmer way to move through a coastal city.

Hard technical constraints:
- Return one complete self-contained single-file `index.html`.
- All CSS must be inside `<style>`.
- All JS must be inside `<script>`.
- Inline CSS/JS only; no build step.
- No React/Vue/Svelte.
- No jQuery, GSAP, or external libraries.
- Do not reference local images/fonts/CSS/JS.
- Use pure CSS + inline SVG for route maps and pier schematics.
- Do not use `style=""` inline styles in markup.

This case must be timetable-first.
Do not start with a generic hero and then cards.
The skeleton must feel like a transport artifact: schedule board + pier map + pass object.

Page structure requirement:
- The page structure must be timetable-first and sectioned into distinct chapters (board, map, pass, flow, policy) rather than repeating one generic section wrapper.

Art direction tied to harbors and ferries:
- Materials: harbor navy enamel, fog ivory paper, brass ticketing, tide charts, pier signage paint, nautical rule lines, subtle water caustics.
- Palette: deep navy, fog/ivory, brass/gold, sea-glass teal, restrained coral as "signal".
- Typography:
  - refined display for brand moments,
  - clear sans for reading and UI,
  - mono for times, piers, route codes, and fare rules.

Design system requirements (CSS `:root`):
- Background layers:
  - calm gradient sky to water,
  - subtle caustics texture,
  - faint chart grid.
- Surface tiers:
  - timetable board paper,
  - glass overlay,
  - brass badge.
- Lines:
  - timetable rules,
  - map route strokes,
  - pier markers.
- Text hierarchy and spacing scale.
- Accent and semantic tokens (success/warning/danger).
- Focus ring token.
- Motion tokens: durations and easing.

Mandatory page skeleton (must be obvious):
1. First viewport is a **Timetable Board**:
   - a real schedule table (rows/columns),
   - next sailings with status (on time, boarding, delayed),
   - and the primary CTA living inside the board.
2. A **Pier Map** chapter:
   - inline SVG harbor map with labeled piers.
   - selecting a pier updates:
     - timetable rows,
     - membership perks for that pier,
     - and recommended boarding windows.
3. A **Pass Artifact** chapter:
   - membership presented as a pass/ticket object.
   - show tier selection and "save pass" action.
4. A **Boarding Flow** chapter:
   - displayed as a lane/flow or signage steps, not a marketing timeline.
5. A **Policy and Weather** chapter:
   - accordion of harbor policies (cancellations, bikes, accessibility, concierge holds).
6. Final conversion:
   - membership request / concierge setup form.
   - must feel like ticket office intake, not a generic CTA banner.

Content coverage requirements (10+ blocks; order is free):
- sticky navbar with live route chip + CTA.
- timetable board hero.
- service strip: what membership changes.
- pier map selection chapter.
- timetable tabs for modes (weekday/weekend/late).
- metrics band (count-up) framed as transit outcomes.
- membership comparison (day-pass vs member) as a ledger-like comparison.
- boarding flow lane.
- partner proof (hotels/venues) as stamps/marks.
- FAQ/policy accordion.
- modal membership request + toast feedback + footer.

Concrete content requirements (write actual sample content):
- At least 10 timetable rows with realistic times and pier names.
- At least 6 pier names and 2 route names with short descriptors.
- At least 6 policy items (weather, bikes, ADA, concierge, luggage, refunds).
- At least 3 membership tiers with constraints and benefits.
- At least 3 testimonials from concierge/commuter/event host roles.

## Round 2

Deepen behavior with real interactions (at least 8).
Explicitly implement all required interactions:
1. Modal
2. Accordion
3. Toast
4. Tabs
5. Scroll reveal
6. Stagger animation
7. Count-up
8. Navbar scroll transition

Interaction binding to the timetable-first skeleton:
- Tabs:
  - must switch timetable modes (Weekday / Weekend / Late).
  - switching tabs must re-render the timetable rows (not only swap text).
- Modal:
  - membership request / concierge setup.
  - must open from at least two CTAs.
  - must trap focus; Escape closes; overlay click closes; close button.
  - fields must include:
    - rider type,
    - home pier,
    - preferred sailing window,
    - accessibility needs,
    - concierge notes,
    - notification preference.
- Accordion:
  - harbor policy and weather rules.
  - expanded state must be obvious without using color alone.
- Toast:
  - ticket-office receipt style confirmations.
  - aria-live announcements required.
  - trigger on:
    - pass saved,
    - request submitted,
    - pier pinned.
- Scroll reveal:
  - reveal should feel like signage plates and boards entering, not generic fade-up.
- Stagger animation:
  - use stagger for timetable rows, boarding steps, or pier markers.
- Count-up:
  - on-time percentage, average wait minutes, sailings per week, minutes saved.
  - trigger once when visible.
- Navbar scroll transition:
  - shift from airy brand header to compact route rail after scroll.
  - route chip becomes more prominent and readable.

Interactive state requirements:
- Provide Default, Hover, Active, Focus states for:
  - buttons,
  - links,
  - tabs,
  - pier selectors,
  - chips,
  - accordion triggers,
  - modal controls,
  - form fields.
- Focus must be visible and consistent.
- Active must feel pressed.

Motion direction:
- calm and nautical.
- avoid neon tech.
- avoid gimmicks.
- prefer:
  - subtle caustic drift,
  - board slide-ins,
  - route-line emphasis.

Reduced motion:
- Respect `prefers-reduced-motion`.
- In reduced-motion mode:
  - disable caustic drift and parallax,
  - simplify reveals,
  - keep layout and contrast strong.

## Round 3

Responsive requirements across 4 breakpoints:
- `>= 1440px`:
  - timetable and pier map can sit in a composed two-region layout.
  - pass artifact is large and tactile.
- `1024px - 1439px`:
  - keep timetable readable; map remains usable; reduce ornament.
- `768px - 1023px`:
  - map becomes a collapsible panel.
  - timetable stays primary.
  - pass artifact becomes a swipeable card.
- `< 768px`:
  - timetable board remains the first experience.
  - pier selection is thumb-friendly and high contrast.
  - boarding flow becomes a compact numbered lane.
  - avoid collapsing into generic repeated cards.

Accessibility requirements:
- semantic landmarks + correct heading hierarchy + skip link.
- ARIA for modal, tabs, accordion, toast live region, and pier selector states.
- accessible names for all form controls; `aria-label` for icon-only buttons.
- keyboard support for modal/tabs/accordion and pier selection.
- visible focus states.
- sufficient contrast on navy/fog palette.
- respect `prefers-reduced-motion`.

## Round 4

Polish until it feels like a real harbor membership brand and timetable-first product page.

Final acceptance checklist:
- one complete self-contained single-file `index.html`.
- CSS in `<style>`, JS in `<script>`.
- no frameworks, no external libraries, no local assets, no `style=""`.
- complete CSS `:root` token system used consistently.
- required interactions implemented:
  - Modal, Accordion, Toast, Tabs,
  - Scroll reveal, Stagger animation,
  - Count-up, Navbar scroll transition.
- first viewport is a timetable board (not a generic hero).
- pier map selection updates the timetable and related content.
- pass artifact exists and does not resemble a generic pricing table.
- responsive across 4 breakpoints.
- accessibility, keyboard, and reduced-motion correct.

Return only the final code contained in a single `index.html`.

GENERATE THE FINAL CODE NOW
