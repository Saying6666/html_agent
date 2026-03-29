## Round 1

Document: FIELD DISPATCH + SIGNAL ROOM PLAYBOOK
Name on page: **FDU Signal Room**
Framing: Next-gen command center for a university-linked urban futures lab
Deliverable: one single-file 'index.html'

Non-negotiable intent:
This must feel like a Modern Premium Glassmorphism & Glo UI experience.
It must embody the sleek, dark-mode, high-fidelity aesthetics seen in Vercel, Linear, or Apple's premium presentations.
It must NOT feel like an old SaaS layout.
It must NOT feel like flat boring cards or a generic vertical webpage.

Case-specific art direction (commit):
Theme: Immersive floating glossy dashboard. 
Deep space dark mode with ambient light bleed.
Palette:
- deep void black (#000000 to #0a0a0a) background
- ambient glowing orbs in electric cyan, ultra-violet, and neon lime
- brilliant white and silver typography
- translucent surface layers with ultra-subtle color tints
Materials:
- Deep glassmorphism panels
- Glowing gradient borders via 'conic-gradient'
- Glass rim highlights ('inset 0 1px 0 rgba(255,255,255,0.15)')
- High-contrast glows and fluid lighting effects
Typography:
- Inter / SF Pro-style pristine sans-serif
- Monospaced fonts for data, coordinates, and metrics
- Ultra-tracked, refined caps for labels
Hard bans (strictly enforced):
- NO old SaaS layouts
- NO flat boring cards
- NO white backgrounds as primary canvas
- NO solid, un-blurred background layers for cards

Layout archetype (must commit):
Immersive, floating glossy dashboard and app-like view.
Do not stack simple horizontal bands. Construct an app-like shell.
Build 3 main spatial zones with different structural logic:
Zone A: Floating Sidebar / Navigation Hub (controls and status).
Zone B: Central Glass "Dispatch" Stage (dynamic hero and data visual).
Zone C: Data Grid / Signal Board (glass cards floating in space).

Signature device (must be obvious in hero):
Ambient floating blurred orbs ('filter: blur(100px)') moving slowly in the background beneath the glass layers.
A central glowing visualization, such as a "spectrum waterfall" or "city signal mesh" using SVG masks and gradient strokes, shining brightly.

Design system requirements:
Define a rigorous CSS ':root' token system.
Tokens must include:
- glowing ambient colors (cyan, violet, lime)
- surface layers ('rgba(255,255,255,0.03)' to '0.08')
- intense blurs ('backdrop-filter: blur(30px)')
- borders/separators ('rgba(255,255,255,0.1)')
- text hierarchy
- shadows (dense dark shadows + colored glow shadows)
- motion tokens (smooth spring-like durations, fluid ease) 
Use tokens consistently.

Technical constraints (non-negotiable):
- Return one complete self-contained 'index.html'
- Single-file only
- All CSS must be inside '<style>'
- All JavaScript must be inside '<script>'
- Inline CSS and inline JS only
- Do not use React, Vue, Svelte, jQuery, GSAP
- No external frameworks, no libraries, no build step
- Do not reference local images/assets
- Prefer advanced pure CSS: 'conic-gradient', 'backdrop-filter', mask-images
- Do not use 'style=""' in markup

Content coverage (ingredients; reorder freely into an app layout):
1. Glassy floating masthead/sidebar.
2. Hero dashboard stage with glowing metrics.
3. Live operations strip/ticker in a glass pill.
4. Research pillars as glowing glass grids.
5. Metrics band with count-up.
6. Program timeline hovering in space.
7. Tabbed command panel for "Lab Notes / Scenarios / Methods".
8. Editorial story cards with gradient glowing borders on hover.
9. Accordion for governance / FAQ inside a frosted sheet.
10. Application panel with deep glossy form inputs.

## Round 2

Deepen into a genuinely interactive fluid experience.
Implement at least 8 meaningful interactions.
They must feel hyper-responsive and premium.

Required interactions (must include all):
1. **Modal**
Purpose: "Preview report" / "Open dossier".
Open from hero and from at least one dispatch card.
Must be a stunning glass pane dropping from above or blooming from center.
Trap focus, Escape closes, return focus to opener.

2. **Accordion**
Governance/FAQ inside a frosted sheet.
Fluid height transition. Glowing icon rotation.
ARIA and keyboard support required.

3. **Toast**
Trigger on saving or submitting.
A floating glass pill at bottom center.
Neon glowing border, polite live region. Allow dismiss/auto-hide.

4. **Tabs**
"Lab Notes / Scenarios / Methods".
An active marker that glides smoothly behind the active tab (using fluid CSS transitions).
Switching must update the central panel layout.

5. **Scroll / Scroll-Snap Reveal**
Make reveals feel like widgets waking up in an OS.
Use subtle scale-up and fade-in, paired with the glass border glowing up.
Respect reduced motion.

6. **Stagger animation**
Use smooth, fluid spring-like stagger for dispatch cards and metrics.
Avoid a generic load.

7. **Count-up**
Count-up metrics. Glow brilliantly as they count.
Trigger once. Respect reduced motion.

8. **Glow Tracking (Hover effect)**
Implement a mouse-following glow effect on the research pillar cards. 
The gradient border or background glow should follow the cursor position over the card.

Add at least 2 extra case-specific interactions:
- Filter chips (glass pills) that sort the dispatch grid with layout animations.
- A glowing dynamic "live status" dot pulsing eternally.

State design requirements:
Define Default/Hover/Active/Focus for all controls.
Focus states must use sharp glowing rings (e.g., 'box-shadow: 0 0 0 2px var(--cyan)').

Motion direction:
- liquid, fluid, Apple-like springs.
- zero jank.
- background orbs must drift perpetually softly.

## Round 3

Responsive requirements:
Shift from fluid multi-column floating dash to a stacked, app-like mobile view.

Breakpoints:
- >= 1440px
Expansive immersive dashboard. Ambient orbs heavily visible.
Sidebar + Main Stage + Side Panel grid.

- 1024px - 1439px
Tightened floating panels. 
Maintain complex grid.

- 768px - 1023px
Collapse to 2 columns or stack gracefully.
Bottom or top sticky glass bar replaces sidebar.

- < 768px
Mobile app view.
Bottom sticky glass navigation tab bar.
Vertical scroll of frosted cards over the dark, orb-lit void.

Accessibility requirements (mandatory):
- semantic landmarks: 'header', 'nav', 'main', 'section', 'footer', 'dialog'
- correct heading hierarchy
- ARIA for modal, tabs, accordion, toast, live status
- accessible names for form controls, 'aria-label' for icons
- keyboard support for all interactive pieces
- visible high-contrast focus rings (cyan/white glow)
- support 'prefers-reduced-motion'

Reduced motion strategy:
- disable orbs, replace with static gradients
- disable count-up
- crossfade cards instead of scaling

Technical constraints remain strict:
- single-file 'index.html', inline CSS/JS only
- MUST use '-webkit-backdrop-filter' along with 'backdrop-filter'

## Round 4

Polish until it feels like a top-tier design engineering portfolio piece or a Vercel flagship launch.

Polish targets:
- Ensure the 'backdrop-filter: blur(30px)' is striking with the 'filter: blur(100px)' ambient orbs behind them.
- Check that the 'inset 0 1px 0 rgba(255,255,255,0.15)' rim highlight creates a 3D glass edge on all cards.
- Confirm glowing gradient borders ('conic-gradient' masks or 'before' pseudoelements) look precise and not blurry on the edge.
- Fluid, frictionless motion.
- Token consistency across glowing text, muted text, surface layers.

QA checklist:
- single-file 'index.html', inline 'style' and 'script'
- no frameworks, no local assets, no 'style=""'
- ambient orbs drifting in background
- hard bans respected (no old SaaS layouts, no flat boring cards)
- glassmorphism heavily utilized
- modal works (focus trap, Escape, restore focus)
- accordion works
- toast works
- tabs glide smoothly
- scroll reveal and staggers work
- count-up works
- filter chips work
- responsive layout adapts properly (mobile bottom tab bar)

Return only the final production-ready HTML.
GENERATE THE FINAL CODE NOW
