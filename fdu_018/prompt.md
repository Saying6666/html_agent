# Harbor Nine: The Waterfront Mobility Operating System

## Visual & Thematic Direction: Modern Premium Glassmorphism & Glo UI

Create a production-grade single-page website for **Harbor Nine**, a private waterfront mobility and itinerary operating system for hotels, marina clubs, and coastal concierge teams. The page must utilize a "Modern Premium Glassmorphism & Glo UI" aesthetic. This means deep, dark immersive backgrounds layered with vibrant, ambient blurred orbs, soft luminous glows, and intricate frosted glass UI panels (`backdrop-filter: blur(20px)` and semi-transparent backgrounds). Borders should feature delicate gradients or `conic-gradient` treatments. The result should look ultra-modern, cutting-edge, and highly technical, yet luxurious enough for elite coastal operators.

Use a complete design system in CSS `:root` with variables for:
- Deep background colors (e.g., `#080c14`, `#040609`)
- Vibrant ambient glow colors (cyan, deep nautical blue, bio-luminescent teal, soft magenta)
- Surface layers (white and blue at 2-10% opacity)
- Glass wash (`rgba(255, 255, 255, 0.03)` to `0.08`)
- Conic gradient border stops
- Primary text (pure white), muted text, labels, inverse text, accent
- Success, warning, and alert colors
- Radii (large, smooth curves for panels, tight curves for buttons), spacing scale, content width
- Display, heading, body, label, and metric type sizes (sleek sans-serif, maybe highly geometric)
- Duration tokens and easing curves (`cubic-bezier(0.16, 1, 0.3, 1)`)

Technical requirements:
- Return one complete self-contained `index.html` (>600 lines)
- Single-file only, all CSS must be inside `<style>`
- All JavaScript must be inside `<script>`
- Inline CSS and inline JavaScript only
- Do not use React, Vue, Svelte, jQuery, GSAP, or external frameworks
- No external libraries and no build step. No placeholder text like "Lorem ipsum". Use rich, realistic copywriting.
- Provide a massive, deeply detailed page with at least 12 substantial sections.

## Content Coverage & 12+ Sections Requirements

1. **Floating Glass Navbar**: Sticky top, heavily blurred glass, containing glowing brand mark, route links, live fleet status indicator (blinking dot), and a glowing CTA.
2. **Hero Heroine**: Deep space, ambient orbs. Thesis statement on modern coastal logistics. Bold typography, dual CTAs with conic-gradient borders. Right-side 3D-like abstracted glass control tableau showing a live boat dispatch.
3. **Partner Consortium Strip**: High end hotel, marina, and residency logos (inline SVG or CSS typographics).
4. **The Command Nexus (Features)**: Grid of glassmorphic cards revealing core capabilities (Fleet routing, Guest itinerary, Dockside power, Crew coordination). Ambient glow on hover that tracks cursor.
5. **Interactive Operations Terminal**: Massive glass panel with tabs (Arrivals, Crew, Guest Requests). Changing tabs alters the internal glow and data displayed.
6. **Live Telemetry (Metrics)**: Band with count-up outcomes. Real-time feel. Glowing numbers.
7. **Nautical Journey Timeline**: A vertical or horizontal glowing path. Sequence of a guest's perfect journey from airport to suite to yacht, orchestrated by Harbor Nine.
8. **Legacy Dispatch vs. Harbor Nine Orchestration**: Comparison slider or side-by-side. Legacy is dull, static, grid-locked. Harbor Nine is fluid, glowing, connected.
9. **Global Fleet Radar**: A rich CSS-drawn abstracted map or radar interface showing vessel tracking. 
10. **Member Spotlight Case Study**: A rich quote from a premium hospitality operator. Elegant typography, large quotation marks, photo placeholder (CSS gradient).
11. **Security & Protocol**: Section emphasizing absolute private data control for VIP guests. Padlock icon, encrypted transit description.
12. **FAQ Accordion**: Blurred glass panels that expand with a smooth height transition. Glowing active state.
13. **Vessel Onboarding Form & Final CTA**: Intake form for a private demo. Inputs have glowing focus rings. 
14. **Precision Footer**: Deep background. Sitemap, contacting, compliance note, social links.

## Motion & Interaction (Real JS)

Implement **at least 8 real functional interactions**, explicitly including:
1. **Modal** for booking a private demo.
2. **Accordion** inside the FAQ or Security sections.
3. **Toast** notification upon form submission.
4. **Tabs** in the Interactive Operations Terminal.
5. **Scroll reveal** (IntersectionObserver) for major sections, fading up and blooming their glows.
6. **Stagger animation** for the features grid.
7. **Count-up** for the Live Telemetry metrics.
8. **Navbar scroll transition** (becomes blurred and shrunken when scrolled).

Also include:
- A comparison toggle in the Dispatch vs Orchestration section.
- Hover responses on cards: conic-gradient borders animate or rotate, glass gets frostier.
- Mouse-tracking ambient glow effect on the hero or features cards (a subtle radial-gradient following the mouse via JS).
- Lightweight client-side form handling.

## Visual Differentiation Guardrails

- `distinctiveness`: The aesthetic should scream "Modern Premium Glassmorphism & Glo UI". No flat, boring SaaS looks.
- `effects allowance`: Extensive use of `backdrop-filter`, `radial-gradient(circle at X Y, color, transparent)`, `box-shadow` for glows.
- `anti-repeat`: Ensure sections don't just look like the same 3 cards repeated. Use asymmetrical layouts, massive single panels, and text-driven layouts interchangeably.

The final HTML must be a masterpiece of frontend engineering, heavily stylized with CSS variables, rich interactions, and flawless responsiveness. Make it vast, immersive, and premium.
The code must be larger than 600 lines. All text must be real. Do not cut corners. Do not use place holders. The design language must be distinct and specific to a waterfront OS.
The glow should be deeply integrated into the layout, utilizing pseudo-elements to create ambient lighting behind glass layers.
Borders should leverage `border-image: conic-gradient(...) 1;` where possible, or use background padding techniques for gradients with border-radius.
Make the layout flow with large typographic moments interspersed with technical UI abstractions.

Ensure absolutely every rule is met.
1. >160 lines in this prompt (expand it by adding rich descriptive details of each section).
2. >600 lines in the generated index.html.
3. No placeholders under any circumstances. Everything crafted.
4. Glassmorphism + Glo UI focus.

## Extended Narrative & Copy Blueprint

To ensure rich content without placeholders, here is the detailed copy and narrative blueprint to guide the implementation:
- **Hero Statement**: "Orchestrate the Unforgettable. Harbor Nine is the absolute waterfront mobility and coastal operations system for the world's most distinguished superyacht marinas and elite coastal resorts."
- **Capabilities**: Features like 'Dynamic Mooring Allocation', 'Autonomous Crew Manifests', 'VVIP Guest Itinerary Synchronization', and 'Bespoke Tender Dispatch'.
- **Metrics**: 14M+ Nautical Miles Navigated, 99.9% Mooring Efficiency, $2B+ Managed Assets, 120+ Partner Marinas.
- **Timeline**: 1. Guest touches down at private airstrip. 2. Tender is dispatched seamlessly. 3. Suite temperature coordinates with arrival ETA. 4. Yacht readied with provisions.
- **Operations Terminal Data**: Mocking up real ship names "M/Y Aurelia", "S/Y Serene", with arrival times, slip assignments, and service requirements.

Expand this narrative thoroughly across the page. Every pixel should breathe luxury coastal tech.

## Technical Execution & Realism
The CSS must be incredibly well structured.
```css
:root {
  --glow-nautical: rgba(0, 238, 255, 0.4);
  --glow-deep: rgba(0, 85, 255, 0.3);
  --glass-bg: rgba(10, 14, 25, 0.4);
  --glass-border: rgba(255, 255, 255, 0.1);
}
.glass-panel {
  background: var(--glass-bg);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid var(--glass-border);
  box-shadow: 0 8px 32px 0 rgba(0,0,0,0.3);
}
```
Use this paradigm across the whole site. Ensure mobile responsiveness is handled flawlessly with CSS Grid and Flexbox.

No corners cut. Good luck.

## Line expansion mapping

We need the prompt to be truly larger than 160 lines, so let's continue by providing an exhaustive list of micro-interactions and explicit copywriting for every single section to be included:

### Expanded Brand Tone
Harbor Nine is not an app; it is a command center. Think of the bridge of a modern exploration vessel intersecting with a five-star hotel's private concierge desk. The language is sharp, confident, and service-oriented. We do not say "Click here to buy." We say "Initiate Vessel Integration." We do not say "See our features." We say "Operational Capabilities."

### Interactive Operations Terminal (Copy & Structure)
- **Tab 1: Dockside Arrivals.** Data: 14:00 - S/Y Serene (82m) - Berth 4A - Requires shoreside power (400A), fresh water, and provisioning team.
- **Tab 2: Crew Logistics.** Data: 14:30 - M/Y Aurelia (55m) - Transport 12 crew to central terminal. Two luxury vans dispatched. Wait time: 3 mins.
- **Tab 3: VVIP Requests.** Data: 15:00 - Owner of P/Y Eclipse - Helicopter transfer to private estate + chilled champagne on arrival. Status: Coordinated and Airborne.

### Global Fleet Radar (Visual details)
The radar should use concentric circles with `border-style: dashed`, `border-width: 1px`, and `border-color: rgba(0, 238, 255, 0.2)`. It should have a sweeping conic-gradient animation simulating a radar sweep. On the radar map, place 3 pulsing dots representing active vessels, using `animation: pulse 2s infinite`. Hovering on a dot opens a small glass tooltip with vessel data.

### Comparison Section (Details)
- **Legacy Approach**: "Radio static. Whiteboard schedules. Lost VHF calls. Missed ETA windows. Fragmented guest experiences." (Use a muted, static UI block, maybe slightly glitchy or gray).
- **Harbor Nine Edge**: "Synchronized telematics. Silent, instant terminal updates. Predictive shoreside readiness. Perfected arrival orchestration." (Use vibrant cyan/teal glows, fluid animations).

### Final Checklist for the Developer
1. **Modal**: Needs a dark overlay backdrop with heavy blur, an elegant entrance animation (scale up and fade in), and a working close button.
2. **Accordion**: Needs exact height calculation or grid `1fr` trick for smooth opening. Plus/minus icon must rotate beautifully.
3. **Toast**: Slide in from bottom-right. Green/cyan glow indicating success. Auto-dismiss after 4 seconds.
4. **Tabs**: Glowing underline indicator that shifts to the active tab. Content panel fades out and in smoothly.
5. **Scroll Reveal**: Elements start translated down by 30px with 0 opacity. As they enter viewport, transform to 0 and opacity 1. Stagger the children.
6. **Card Stagger**: The grid of Command Nexus features should cascade in 1, 2, 3, 4 upon scrolling into view.
7. **Count-up**: An IntersectionObserver detects the metrics band. The numbers tick up rapidly using requestAnimationFrame to their final values (14M, 99.9, 2B, 120).
8. **Navbar Scroll**: On load it is transparent and 100px tall. On scroll > 50px, it shrinks to 60px, gains a heavy `backdrop-filter`, and a subtle bottom border.

Ensure you follow this strictly. Overwrite `fdu_018/prompt.md` and generate `fdu_018/src/index.html`.

### Typography Constraints
- Headings: Use a highly geometric tech sans-serif (e.g., system-UI, Inter, or Roboto with tight tracking).
- Body: Neutral, highly legible sans-serif.
- Monospace: Use a true monospace font (e.g., Fira Code, JetBrains Mono, or SF Mono) for numeric data, telemetry stats, and system variables.
- Letter-spacing on eyebrows and subheadings should be elevated (e.g.,  .1em to  .2em) for luxury feel.

### Deep Interaction Focus
- Forms must use :focus-within effectively to dim the surrounding elements or glow the container heavily.
- For buttons, implement an expansive ripple effect on click, or a subtle 	ransform: scale(0.98) on :active.
- Navigation items should feature an underline animation 	ransform-origin: left expanding to scaleX(1).
- Cards should have 	ransform: translateY(-4px) with increased ox-shadow depth.
- Glass panels should have a refined inset shadow ox-shadow: inset 0 1px 0px rgba(255,255,255,0.1) to simulate light reflecting off the top edge of the glass.

### Further Content Breakdown
- Add a "Testimonials from Fleet Captains" slider or grid.
- Add a dedicated "Connectivity" section that discusses integrations with AIS, radar, terminal operating systems, and hotel property management systems (PMS).
- Expand the FAQ to 4 specific, detailed questions.
- Include a decorative code block or telemetry read-out in the Hero or Operations tab that looks like raw JSON or YAML data for a true tech feel.
