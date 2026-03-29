## Round 1

Document: AURELINE SLEEPER CLUB IMMERSIVE APP VIEW
Brand: **Aureline Sleeper Club**
Product: premium overnight rail membership (private cabins, concierge booking, slow-luxury hospitality)
Year feel: 2025-2026
Deliverable: one single-file index.html with INLINE CSS and JS.

Core promise:
This should feel like an ultra-premium, futuristic travel booking app interface.
A modern booking folio wrapped in futuristic, cinematic glassmorphism.

Case-specific art direction (commit):
Theme: Modern Premium Glassmorphism & Glo UI (Vercel/Linear/Apple style).
Materials:
- Deep glassmorphism (`backdrop-filter: blur(40px) saturate(120%)`)
- Glowing gradient borders via conic-gradient masks
- Glass rim highlights (`box-shadow: inset 0 1px 0 rgba(255,255,255,0.15), inset 0 -1px 0 rgba(255,255,255,0.05)`)
- High-contrast obsidian backgrounds, ambient space vibes

Color Palette & Hex Codes:
- Primary Obsidian Background: `#050505` to `#09090b`
- Secondary Background Tone: `#0e0e11`
- Ambient Orb 1 (Aureline Gold): `#D4AF37`
- Ambient Orb 2 (Midnight Indigo): `#1A1B41`
- Ambient Orb 3 (Crimson Silk): `#8B0000`
- Ambient Orb 4 (Ethereal Cyan): `#124E5A`
- Glass Panel Fill: `rgba(25, 25, 25, 0.4)`
- Glass Panel Secondary Fill: `rgba(40, 40, 45, 0.25)`
- Primary Text: `#FAFAFA`
- Secondary Text: `#A1A1A8`
- Tertiary Text: `#616168`
- Accent Glow / Buttons: `linear-gradient(135deg, #D4AF37, #FFDF73)`
- Alert / Status Ongoing: `#00E676`
- Alert / Status Delayed: `#FF3D00`

CSS Variables (Root definitions required):
- `--bg-obsidian`: #050505;
- `--text-main`: #FAFAFA;
- `--text-muted`: #A1A1A8;
- `--text-tertiary`: #616168;
- `--glass-bg`: rgba(25, 25, 25, 0.4);
- `--glass-bg-hover`: rgba(40, 40, 45, 0.35);
- `--glass-border`: rgba(255, 255, 255, 0.1);
- `--gold-glow`: #D4AF37;
- `--indigo-glow`: #1A1B41;
- `--blur-heavy`: blur(40px);
- `--blur-medium`: blur(20px);
- `--transition-silky`: all 0.6s cubic-bezier(0.22, 1, 0.36, 1);
- `--transition-bounce`: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);

Atmosphere:
- Ambient floating blurred orbs (`filter: blur(120px)`) in background
- Fluid, silky animations and glossy reflections
- Sleek, tech-luxury precision
- Extremely tight spacing and pixel-perfect alignments
- Soft inner shadows mimicking volumetric lighting

Typography:
- Refined sans-serif (Inter, SF Pro) with high contrast weights (300, 400, 600)
- Monospaced fonts for technical data (departure times, carriage codes) e.g., JetBrains Mono, SF Mono.
- Make highly legible font stacks: `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;`
- Title scale: H1 `4.5rem`, H2 `3rem`, H3 `2rem`.
- Base body size: `1.125rem` (18px) for comfortable reading.
- Extra tight tracking (`letter-spacing: -0.02em`) for large headers.

Hard Bans:
- NO old SaaS layouts
- NO flat boring cards
- NO standard "hero + features + pricing" scroll
- NO basic material design shadows or thick solid borders
- NO absolute black (#000000) for text backgrounds.
- NO default browser scrollbars (style them).
- NO times new roman or default serif fallbacks.

Layout archetype (must commit):
Immersive, floating glossy dashboard or premium immersive app view.
A layered, spatially deep UI layout with floating modal panes over an ambient dynamic background.

Detailed Sections (10+ required sections):
1. **Global App Navigation**: Floating pill-shaped header (`border-radius: 99px`). Links: [Voyages], [Cabins], [Dining], [The Club]. Right side: [Member Sign In] (glowing border button).
2. **Hero Dashboard Spread**: Two-column layout. Left: "The Return of Slow Luxury" typography (H1), right: holographic abstract ticket graphic with QR code simulation.
3. **Immersive Holographic Ticket Map**: An inline SVG map with glowing nodes (Paris, Vienna, Venice, Istanbul), connected by animated dashed glowing lines.
4. **Active Departure Board**: A horizontal scrolling or sleek grid view of upcoming trains. Columns: [Train No., Route, Departs, Status]. Monospaced fonts here for numeric data.
5. **Itinerary Desk (Tabbed Interface)**: Glass tabs for "The Suite", "The Grand Suite", "The Observation Car". Content fades in/out based on selection. Include small icons.
6. **Journal Excerpt / Editorial Mode**: A masonry style grid of premium imagery (use CSS gradients if no images) overlaid with poetic copy about the European nightscape ("The moonlit Alps passing by...").
7. **Concierge Service Module**: A frosted glass panel detailing "24/7 White-Glove Service" with an intricate glowing bell icon. Include "Summon Attendant" mock button.
8. **Gastronomy Preview**: A split section showing a bespoke dining menu. Text placeholders: "Midnight Caviar Service", "Breakfast in Bed", "Vintage Champagne Reserve".
9. **Exclusive Membership Tier Panel**: A heavily glowing card showcasing the "Aureline Black Card" benefits. It should tilt on hover using CSS 3D transforms.
10. **Cabin Geometry Specifications**: A small technical blueprint section displaying room dimensions (`6m x 3m`), bed sizes, and amenities in a rigid grid format.
11. **Booking / Waitlist Lightbox**: A seamless inline booking form. Inputs for [Destination], [Departure Date], [Guests]. A glowing "Request Suite" submit button.
12. **App Footer**: Minimalistic, monospaced legal links, coordinate data of the headquarters (`48.8566° N, 2.3522° E`), and a subtle glowing brand mark.

Take a deep breath and emit the complete HTML file up to the end of the styling and basic structural shell, focusing entirely on the immersive Glassmorphic UI foundation and the background orbs. DO NOT output the exact same code repeatedly.

## Round 2

Now, implement the complex cinematic UI interactions, motion, and structural modules.

Micro-Interactions (8+ required):
1. **Orb Drift Animation**: Background `.ambient-orb` elements must use a slow 20s-40s infinite keyframe animation. `animation: drift 30s cubic-bezier(0.25, 0.1, 0.25, 1) infinite alternate;` Move them across X and Y axes.
2. **Glass Panel Hover**: When hovering `.glass-panel`, background transitions from `rgba(25, 25, 25, 0.4)` to `rgba(40, 40, 45, 0.35)` with `transition: var(--transition-silky);`. Increase inner shadow opacity.
3. **Conic Border Glow Track**: On the main `.booking-card` hover, a pseudo-element with a conic-gradient spins around the border using `@keyframes spin { 100% { transform: rotate(360deg); } }`.
4. **Button Magnetic Pull**: Add a subtle scale effect to primary buttons on hover `transform: scale(1.04);` and slight box-shadow bloom using `var(--transition-bounce)`.
5. **Tab Switching Crossfade**: Using vanilla JS, when a `.tab-btn` is clicked, `.tab-content` elements drop opacity to 0, transform Y by 10px, change content, and fade back to opacity 1, transform Y 0, using a 0.5s ease-out curve.
6. **Departure Board Stagger**: As `.departure-row` elements appear, apply an animation delay staggered by `.1s`, animating opacity from 0 and translateY from `20px` to `0`. Use IntersectionObserver if possible, or just a load animation.
7. **Form Input Focus Rings**: On focusing `.modern-input`, the bottom border or box-shadow expands from center to 100% width using a vibrant gold glow gradient (`box-shadow: 0 2px 10px rgba(212, 175, 55, 0.4)`).
8. **Holographic Map Ping**: The SVG station nodes `.map-node` pulse with `animation: ping 2.5s cubic-bezier(0, 0, 0.2, 1) infinite;`. Delay each node slightly.
9. **Link Underline Emerge**: On inline text links, an underline expands from left to right on hover. `transform-origin: left; transform: scaleX(1);`.

Content Implementation:
- Construct the hero dashboard with the "Aureline Sleeper Club" branding and Holographic Ticket Map.
- Flesh out the Horizontal Departure Board with realistic times (`23:45`, `01:15`), cities, and status indicators (`ON TIME`, `BOARDING`).
- Build the Itinerary Desk tabs with real descriptions of the Sleeper Cabins, Concierge, and Dining Cart.
- Ensure the editorial/journal section provides narrative context for the slow-luxury experience.
- Implement the 12 sections defined in Round 1.
- Maintain the Vercel/Linear/Apple extreme polish throughout.

Code constraint: Add the necessary JavaScript within a `<script>` tag at the end of the body, and expand the CSS with all the intricate hover states and keyframes. No external libraries.

## Round 3

Responsive Refinement & Accessibility

We need to make this floating dashboard work brilliantly on all screen sizes, from mobile to ultra-wide displays.

Detailed Accessibility (ARIA & keyboard):
- Every interactive button must have `role="button"` and `tabindex="0"`.
- Tab interfaces require `role="tablist"`, `role="tab"`, `aria-selected` (true/false), and `aria-controls`. Content panes need `role="tabpanel"` and `aria-labelledby`. The JS must update these attributes dynamically.
- The booking form inputs must be linked to labels via `id` and `for`, or wrap the input in a `<label>`. 
- Use `<fieldset>` and `<legend>` for grouped form controls.
- Add `aria-required="true"` to mandatory fields and provide clear error contrast if needed.
- Contrast ratios must remain accessible. Ensure the gold (`#D4AF37`) text on dark backgrounds (`#050505`) meets WCAG AA standards (at least 4.5:1).
- Add screen-reader-only text `.sr-only` class: `position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0;` for visual iconic buttons.
- Implement a visible focus state for keyboard navigation: `:focus-visible { outline: 2px solid var(--gold-glow); outline-offset: 4px; border-radius: inherit; }` on all interactive elements.

Responsive Breakpoints & Layouts:
- **Ultra-wide (min-width: 1440px)**: The dashboard max-widths at 1280px, centering in the viewport. Orbs spread wider, using `vw` and `vh` coordinates for keyframes.
- **Desktop (max-width: 1024px)**: Departure board shrinks padding. Holographic map scales down proportionally. Grid gaps reduce from `3rem` to `2rem`.
- **Tablet (max-width: 768px)**: Hero section goes from two-column to stacked (single column, image on top). Itinerary tabs become a scrollable horizontal list (`overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch;`). Hide complex background gradients that cause lag.
- **Mobile (max-width: 480px)**: Mobile optimizations trigger. 
  - The floating panels should consume 95vw, minimizing outer margins to 2.5vw. 
  - Typographic scale drops: H1 from `4.5rem` to `2.5rem`, H2 to `1.75rem`. 
  - Button hit targets strictly `min-height: 48px; min-width: 48px;`. 
  - Stack footer links vertically.

Do not break the premium feel on smaller screens; the glassmorphism should still perform well without crashing mobile GPUs (ensure `will-change: transform, backdrop-filter` on heavy elements).

## Round 4

QA, Detail Pass, and Perfect Delivery

Extensive QA Checklist:
[ ] Visual Bans Check: Are there any completely flat backgrounds without subtle noise/gradients? (If yes, fix). Are there generic drop shadows? (Must use glass highlights).
[ ] Typographic Check: Is JetBrains/SF Mono correctly applied only to numbers, codes, and data? Is the Sans-Serif tracking/kerning elegantly tight?
[ ] Layering Check: Do the floating orbs clip above the content? (They must remain behind the `z-index: 10` glass panels). Map nodes above borders?
[ ] Sections Check: Are all 12 sections from Round 1 present, thoroughly filled with realistic copy (not lorem ipsum), and structured gracefully?
[ ] Micro-interaction Check: Are all 8+ motion requirements (drifting orbs, conic borders, tab crossfades, map pings) functioning?
[ ] Responsiveness Check: Under 480px, does the layout stack gracefully without horizontal scrolling (except explicitly intended areas like tabs)? Is padding maintained inside panels?
[ ] Accessibility Check: Are ARIA labels, tab index, role mappings, and contrast ratios applied correctly?
[ ] Focus Management Check: Does tab key navigation show the custom focus-visible ring?
[ ] Color Accuracy Check: Is the Aureline Gold `#D4AF37` and Obsidian `#050505` used exactly as defined in the palette?
[ ] Performance Check: Are `cubic-bezier` timing functions applied to transitions instead of default `ease`? Are `transform` and `opacity` used for animations instead of layout-triggering properties?
[ ] Semantic Check: Are `<article>`, `<section>`, `<nav>`, `<aside>`, `<main>`, `<header>`, `<footer>` used properly?
[ ] Form Submission Check: Ensure the form cannot submit and reload the page by default (`e.preventDefault()` if implementing a fake submit animation).

Final Polish Tasks:
- Refine the spacing (padding/margin rhythms) using a consistent 8px/16px/24px/32px/48px/64px/128px scale.
- Check semantic HTML tags for strict compliance.
- Verify the vanilla JS logic for the tabs, ensuring no console errors.
- Ensure the form input placeholder text color is subdued but readable (`#616168`).

Output the ENTIRE FINAL single-file HTML, completely self-contained. Double-check all closing tags, script scopes, and line formatting. Deliver the ultimate high-fidelity Vercel/Linear/Apple style booking folio.
