## Round 1 â Role + Design System + Page Structure

**Role:** You are an elite Front-End Architect and UI/UX Designer specializing in Neobrutalist web design and GreenFintech. You are tasked with creating a production-grade, single-file HTML landing page for **CanopyCoin**, a dynamic dashboard that calculates real-time carbon footprints of digital subscriptions and micro-invests spare change into urban forestry. The target audience is environmentally conscious remote workers and digital nomads.

**Design System Requirements(CSS `:root` variables):**
Create a comprehensive design system that fuses Neobrutalism (harsh shadows, thick borders, geometric layouts) with organic earthy textures (grainy overlays, forest tones). 

Implement the following `:root` structure strictly:
```css
:root {/* Earthy Neobrutalist Color Palette */
  --bg-primary: #F4F0E6; /* Organic textured paper white */
  --bg-secondary: #D9E2D8; /* Pale sage green */
  --accent-green: #2E5C31; /* Deep forest green */
  --accent-lime: #D4F842; /* High-contrast tech lime */
  --border-dark: #1A1A1A; /* Harsh neobrutalist black */
  --text-main: #1A1A1A;
  --text-muted: #4A5D4E;
  
  /* Typography */
  --font-display: 'Clash Display', 'Space Grotesk', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
  
  /* Neobrutalist Layout & Shadows */
  --border-thick: 3px solid var(--border-dark);
  --border-thin: 1px solid var(--border-dark);
  --shadow-default: 6px 6px0px var(--border-dark);
  --shadow-hover: 2px 2px 0px var(--border-dark);
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;/* Transitions */
  --transition-snappy: 0.2s cubic-bezier(0.25, 1, 0.5, 1);
  --transition-smooth: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
```

**Page Structure (10 Sections):**
Construct the semantic HTML structure for the following 10 sections. Do not use any external frameworks (Tailwind, Bootstrap, etc.) or external resources (images/videos). Use inline SVG for all graphics.
1. **Dynamic Navbar:** Sticky header with logo, navigation links, and a "Connect Wallet/Bank" CTA.
2. **Hero Section:** High-contrast typography ("Offset Your Digital Life"), floating CSS-based 3D SVG leaves, and an interactive email capture.
3. **Live Dashboard Preview:** A Neobrutalist mock-dashboard card showing real-time carbon footprint calculation from mock subscriptions (Netflix, AWS, Spotify).
4. **How It Works (Tabs):** 3-step process (Connect, Calculate, Plant) utilizing an interactive tabbed interface.
5. **Impact Counter:** Large, starktypography numbers tracking global CO2 offset and trees planted.
6. **Nomad Integrations Grid:** A staggered grid of tools (Slack, Zoom, Figma, GitHub) supported by CanopyCoin.
7. **Urban Forestry Projects:** Horizontal scrolling cards or grid showing local projects (e.g., "Brooklyn Reforestation", "Berlin Tech Park Greening").
8. **Testimonials:** Asymmetric, thick-bordered cards featuring quotes from digital nomads.
9. **Interactive FAQ:** Accordion-style frequently asked questions.
10. **Footer:** Stark, high-contrast footer with a newsletter signup (Toast trigger), sociallinks, and legal disclaimers.

Implement the basic HTML structure, the `:root` variables, and the baseline CSS layout using CSS Grid and Flexbox.

***

## Round 2 â Interaction + Motion

**Objective:** Implement cutting-edge, native JavaScript interactions and CSS animations. The motion should feel mechanicalyet organic (Neobrutalism + Nature). You must implement **at least 8 distinct functional interactions** without using external libraries (no GSAP, no jQuery).

**Required Interactions & Motion:**
1. **Modal (Project Details):** Clicking a Forestry Project card opens a full-screen Neobrutalist modal.
   * *ARIA:* `role="dialog"`, `aria-modal="true"`, `aria-labelledby`, trap focus inside when open.
2. **Accordion (FAQ):** Smooth expansion/collapse of FAQ items calculating `scrollHeight` dynamically.
   * *ARIA:* `aria-expanded`,`aria-controls`, `role="region"`.
3. **Toast (Notification):** A slick, sliding toast notification triggered when the user submits a newsletter/signup form.
   * *ARIA:* `role="alert"`, `aria-live="polite"`.
4. **Tabs (How ItWorks):** Functional tab switching in the "How It Works" section without page reload.
   * *ARIA:* `role="tablist"`, `role="tab"`, `aria-selected`, `role="tabpanel"`.
5. **Scroll Reveal (Intersection Observer):** Sections scale up and bordersfade in sharply as they enter the viewport.
6. **Stagger Animation:** The Nomad Integrations Grid items slide in sequentially with a 0.1s delay between each card when scrolled into view.
7. **Count-up (Impact Stats):** JavaScript function to animate numbers from 0 to targetvalues (e.g., 2,504,120 CO2 lbs) when the Impact section is visible.
8. **Navbar Scroll Transition:** On scroll down (>50px), the navbar shrinks, gains a solid background, drops a `--shadow-default`, and a `--border-thick` bottomborder appears.

**Interactive 3D Leaf Micro-animations:**
Use pure CSS `transform: perspective(600px) rotateX(...) rotateY(...)` on inline SVG paths to create floating leaves in the Hero section that rotate naturally on hover or mouse move.

**Four-State Definitions (Applyto ALL Interactive Elements):**
Ensure every `<button>`, `<a>`, and interactive `.card` strictly implements these states:
* **Default:** `--shadow-default`, `--border-thick`, `transform: translate(0, 0)`.
* **Hover:** Sharp transition. Shadow reduces to `--shadow-hover`, element moves down/right `transform: translate(4px, 4px)`. Background shifts to `--accent-lime`.
* **Active:** Shadow drops to `0px`, element moves to `transform: translate(6px, 6px)` (pressed effect).
* **Focus:** `outline: 3px dashed var(--accent-green); outline-offset: 4px;`.

Write the comprehensive Vanilla JavaScript and the required CSS classes for these interactions.

***

## Round 3 â Responsive + Accessibility

**Objective:** Ensure the CanopyCoin platform is flawlessly responsive across all devices and achieves 100% WCAG compliance.

**Responsive Design (4 Breakpoints):**
Use CSS media queries to adapt the Neobrutalist layouts. The typography should scale fluidly (e.g., `clamp()`), and grids should collapse logically.
1. **Mobile (320px - 480px):** Single column layouts. Hero typography shrinks. Navbar converts to a sleek CSS-only hamburger menu. Accordion tap targets must be at least 48x48px.
2. **Tablet (481px - 768px):** 2-column grids for Integrations and Forestry Projects. Dashboard preview scales proportionally.
3. **Laptop (769px - 1024px):** 3-column grids. Hover effects activate fully.
4. **Desktop (1025px+):** Max-width constraints (`max-width: 1440px`),expansive whitespace, 4-column grids, full 3D leaf mouse-tracking depth effects.

**Accessibility (A11y) Requirements:**
1. **Semantic HTML:** Strict use of `<header>`, `<main>`, `<section>`, `<article>`, `<nav>`, `<footer>`.
2. **KeyboardNavigation:** Every interactive element must be reachable via `Tab`. The visual focus state (`--accent-green` dashed outline) must be undeniably clear. Provide a "Skip to Main Content" hidden link at the very top.
3. **ARIA Landmarks & Roles:** Ensure all tabs, accordions, and modals fromRound 2 are fully labeled. Use `aria-hidden="true"` on purely decorative SVG leaves.
4. **Color Contrast:** The high-contrast Neobrutalist design inherently aids visibility, but ensure `var(--text-muted)` against `var(--bg-secondary)` passes WCAG AA (4.5:1).
5. **Prefers-Reduced-Motion:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Implement the CSS media queries and refine the HTML structure to pass these strict accessibility and responsive constraints.

***

## Round 4â Polish + Acceptance Self-Check

**Objective:** Finalize the code. Inject an organic CSS SVG noise filter overlay to give the `--bg-primary` a subtle recycled-paper texture to contrast the harsh Neobrutalist borders. Polish all micro-interactions, ensure code is minified-ready, and verifyconstraints.

**Design Polish:**
*   Add a subtle grain overlay: `background-image: url("data:image/svg+xml,...noise...");` to the body.
*   Ensure all SVG icons (for tech stacks and UI elements) are visually consistent with the thick-bordered design system.*   Check that the typography hierarchy is dramatic (e.g., massive `h1`, highly legible `.body-text`).

**Acceptance Self-Check (Do not generate code if these are false):**
- [ ] Is the entire project contained in a single `index.html` file with `<style>` and `<script>` tags?
- [ ] Are there exactly 10 detailed sections?
- [ ] Are all 8 required functional interactions (Modal, Accordion, Toast, Tabs, Scroll Reveal, Stagger Animation, Count-up, Navbar) flawlessly implemented in Vanilla JS?
- [] Are Default, Hover, Active, and Focus states perfectly defined for all interactables?
- [ ] Is the color palette strictly adhering to the Earthy Neobrutalist `:root` variables?
- [ ] Are ARIA attributes and keyboard navigation fully operational?
- [ ] Is the page responsive across all