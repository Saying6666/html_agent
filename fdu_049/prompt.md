## Round 1

Create a production-grade single-page website for **Signal Room**.
Signal Room is a live strategy cockpit for cultural teams planning:
- launches
- pop-ups
- city takeovers
- collaborations across venues and partners

This must feel like a real 2025-2026 product.
It must not look like a generic B2B landing page.

Art direction: **Showrunner Storyboard + Street Poster Kit**.
Treat the page like a production wall, not a product brochure.

Material cues (use them as composition rules):
- paste-up posters and wheatpaste textures (subtle)
- torn edges and paper layers
- gaffer tape strips and sticker labels
- stage call sheets and cue lists
- red pencil markup, underlines, strike-throughs
- glossy photo-contact sheets (as frames, not as images)

Color logic:
- neutral paper and ink base
- one aggressive accent (lacquer red OR electric chartreuse)
- avoid purple tech gradients
- avoid generic glassmorphism

Typography logic:
- Display: poster-grade, bold, commanding
- Editorial: readable narrative for story and proof
- Utility: timestamps, venue codes, cue IDs, labels

Structural mandate: **Acts + Storyboard Wall + Call Sheet Desk**.
- Divide the page into 4-6 ACTS.
- Each ACT has:
  - a named header (ACT 01, ACT 02...)
  - a distinct layout mode (no repeating the same wrapper)
  - a "scene" sub-rail
- Include a major Storyboard Wall module:
  - 8+ scenes
  - oversized numbering
  - clipped/cropped previews made with CSS/SVG (no stock images required)
  - pinning / selection behavior
- Include a Call Sheet Desk module:
  - a structured schedule table/rail with cues
  - timecodes, locations, owners, deadlines
- Avoid the default landing rhythm.
This is a production kit.

Act structure suggestion (use or refine, but keep the concept):
- ACT 01 POSTER / THESIS
- ACT 02 BOARD / SCENES
- ACT 03 CALL SHEET / SCHEDULE
- ACT 04 PLAYBOOK / PLAN B
- ACT 05 PROOF / AFTER ACTION
- ACT 06 ACCESS / REQUEST

Storyboard Wall spec:
- Scenes must include:
  - title
  - location code
  - time window
  - capacity or constraint
  - owner
  - status chip
- Provide at least 3 scene statuses:
  - Draft
  - Locked
  - Live
- Include one "pin" interaction that adds a scene to a summary strip.

Call Sheet Desk spec:
- Must present a schedule as structure, not a list of cards.
- Columns (example):
  - Timecode
  - Cue
  - Owner
  - Location
  - Dependencies
  - Notes
- Provide at least one filter/sort mode via Tabs.

Content modules (choose 10-14; rename/reorder freely; keep culture-ops specificity):
- Opening poster scene (not a generic hero):
  - one line manifesto
  - date + city
  - "tonight's run" chip
- Act index rail (for active highlighting).
- Storyboard Wall (signature module).
- Call Sheet Desk (signature module).
- Venue and partner proof as stamps, not a standard logo strip.
- Constraints ledger:
  - permits
  - load-in windows
  - noise
  - staffing
  - approvals
- Scenario board:
  - rain plan
  - overflow plan
  - plan B swap
- Results + after-action:
  - measurable outcomes
  - post-mortem notes
  - what changed next time
- Comparison:
  - chaotic toolchain vs Signal Room
  - staged as two boards on a wall
- FAQ:
  - terms
  - collaboration permissions
  - data handling
- Final CTA:
  - request a field plan (modal + compact form)
- Footer:
  - policy notes
  - contact

Poster-kit token system (CSS `:root` must be complete):
- paper layers and ink tones
- tape/sticker accents and edge treatments
- shadow rules and border rules
- text hierarchy and label system
- spacing scale and radii
- motion tokens (cut, cue, switch pacing)

Technical constraints (non-negotiable):
- Return one complete self-contained single-file `index.html`.
- All CSS inside `<style>`.
- All JS inside `<script>`.
- Inline CSS and inline JavaScript only.
- No React/Vue/Svelte.
- No jQuery/GSAP.
- No external libraries, no build step.
- No local assets (no local images/fonts/CSS/JS).
- Prefer CSS texture + inline SVG marks over stock art.
- Do not use `style=""` inline styles in markup.

## Round 2

Interactions must feel like editing a show plan.
Not generic web UI polish.

Required functional interactions (all must work and be accessible):
1. **Modal**: "Request a field plan".
   - Open from multiple CTAs.
   - Modal must feel like a ticket / call-sheet insert.
   - Include selection steps:
     - campaign type
     - city
     - time window
   - Update a live summary before submit.
2. **Accordion**: FAQ as folded notes with clear state.
3. **Toast**:
   - after pinning a scene
   - after submitting the request
   - must announce via aria-live
4. **Tabs**:
   - switch modes (Launch / Pop-up / Takeover)
   - must reshape the Storyboard Wall or Call Sheet Desk
   - not just swap a paragraph
5. **Scroll reveal**:
   - reveal ACTS with a consistent poster/tear grammar
6. **Stagger animation**:
   - storyboard scenes appear like cards being pinned
7. **Count-up**:
   - show stats (doors, capacity, press hits, signups)
   - present with label rails, not KPI tiles
8. **Navbar scroll transition**:
   - compress into a cue rail
   - show active ACT + live run chip

Mandatory narrative behaviors:
- At least 2 interactions must materially change:
  - reading order
  - layout structure
  - or content depth
- Mode Tabs must reshape a major module.
- Scene pinning must update a visible summary strip.

State design rules:
- Default: paper/ink calm.
- Hover: reveal markup and underline motion.
- Active: pin/stamp confirmation.
- Focus: visible and consistent across all controls.

Motion rules:
- Use one reveal grammar across the page.
- Avoid opacity+translate everywhere.
- Respect `prefers-reduced-motion`.

## Round 3

Responsive behavior must preserve the "production kit" feeling.

Breakpoints:
- `>= 1440px`:
  - storyboard wall and call sheet desk can be wide
  - annotation rails can exist
- `1024px - 1439px`:
  - tighten but keep big numbering dramatic
- `768px - 1023px`:
  - call sheet can become a horizontal rail
  - storyboard becomes compact but still numbered
- `< 768px`:
  - do not collapse into a generic centered list
  - storyboard becomes swipeable scene cards with persistent act index
  - call sheet becomes a vertical docket with sticky day header

Accessibility requirements:
- semantic landmarks: `header`, `nav`, `main`, `section`, `footer`.
- correct heading hierarchy.
- ARIA for Modal, Tabs, Accordion, Toast, and active act/scene indicators.
- accessible names for all form controls.
- `aria-label` for icon-only buttons.
- keyboard support for modal/tabs/accordion; Escape closes modal.
- visible focus states; do not rely on color alone for selected scene/mode.
- support `prefers-reduced-motion`.

Implementation notes for a11y:
- Tabs: proper roles and `aria-selected`.
- Accordion: `aria-expanded` and `aria-controls`.
- Toast: `aria-live="polite"`.
- Modal: focus trap and focus restore.

Technical constraints remain strict:
- single-file `index.html`
- inline CSS/JS only
- no local assets
- no frameworks
- include `-webkit-backdrop-filter` before `backdrop-filter` if used
- no inline `style=""`
- readable, maintainable multi-line code

## Round 4

Polish until this feels like a showrunner's production kit turned into software.
Not a generic app with artsy colors.

Final acceptance checklist:
- One complete self-contained single-file `index.html`.
- Inline `<style>` and `<script>` only.
- Complete poster/tape/storyboard `:root` token system.
- 10+ meaningful modules organized as ACTS with:
  - Storyboard Wall
  - Call Sheet Desk
- Required interactions all work:
  - Modal
  - Accordion
  - Toast
  - Tabs
  - Scroll reveal
  - Stagger animation
  - Count-up
  - Navbar scroll transition
- Mode Tabs reshape a major module.
- Scene pinning updates a visible summary strip.
- Strong responsive behavior across 4 breakpoints.
- Accessibility with keyboard support and reduced-motion.

Final differentiation test (non-negotiable):
- If it resembles a standard hero + features page, redesign around ACTS + storyboard/call-sheet.
- If Tabs do not reshape a major module, rebuild them.
- If the storyboard is just a normal card grid, rebuild it until it reads like a production wall.
- If the call sheet is not a structured schedule, rebuild it.

GENERATE THE FINAL CODE NOW
