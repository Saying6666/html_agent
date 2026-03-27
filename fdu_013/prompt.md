## Round 1 â Role + Design System + Page Structure

You are a Master Web Developer and UX-UI Engineer building a state-of-the-art, premium single-page application. You will generate a single `index.html` file containing HTML, inline CSS, and inline vanilla JavaScript. No external frameworks (e.g., React, Tailwind, Bootstrap) or local assets are allowed. Use high-quality placeholder images (e.g., Unsplash) and GoogleFonts. 

Your task is to build the landing page for **AuraScent**, an e-commerce AI tool. 
**Concept**: A hyper-personalized virtual perfumery that uses AI to analyze a user's Spotify listening history, favorite literature, and visual mood boards to formulate and physically ship a bespokesignature fragrance.
**Target Audience**: Gen Z consumers, luxury fragrance lovers, and personalized lifestyle enthusiasts.
**Visual Style**: Ethereal and high-editorial with fluid vapor animations, elegant serif typography, and muted pastel gradients.

**1. Design System (CSS `:root` Variables)**
Implement a comprehensive CSS`:root` system exactly as follows (or expanded):
```css
:root {
  /* Color Palette: Ethereal & Pastel Gradients */
  --bg-primary: #fcfbfaf0;
  --bg-secondary: #f4efed;
  --text-primary: #1a1a1c;
  --text-secondary: #5a5a60;
  --text-inverse: #ffffff;
  --accent-vapor-1: #d3cce3; /* Muted lavender */
  --accent-vapor-2: #e9e4f0; /* Soft pearl */
  --accent-vapor-3: #f1dfd1; /* Soft peach */
  --accent-glow: #e2d1c3;
  --border-light: rgba(26, 26, 28, 0.1);
  --error: #cf6679;
  --success: #a8b8a5;

  /* Typography */
  --font-serif: 'Playfair Display', serif; /* Elegant serif */
  --font-sans: 'Inter', sans-serif; /*Clean body text */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl:1.5rem;
  --text-2xl: 2rem;
  --text-4xl: 3.5rem;
  --text-6xl: 5rem;
  --line-height-tight: 1.1;
  --line-height-base: 1.6;

  /* Layout & Spacing */
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-4: 1rem;
  --spacing-8: 2rem;
  --spacing-12: 3rem;
  --spacing-16: 4rem;
  --spacing-24: 6rem;
  --spacing-32: 8rem;
  --container-max-width: 1440px;
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 16px;
  --border-radius-pill: 9999px;

  /* Transitions & Shadows */
  --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 0.6s cubic-bezier(0.22, 1, 0.36, 1);
  --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.05);--shadow-glow: 0 0 20px rgba(211, 204, 227, 0.5);
}
```

**2. Page Structure (10 Sections)**
Implement strict semantic HTML5. The page must include these 10 sections:
1. `<header>` / Navbar: Logo, Navigation links, "Craft My Aura" CTA.
2. `section#hero`: High-editorial ethereal hero banner with dynamic CSS vapor background, main headline ("Your Soul, Bottled"), and primary CTA.
3. `section#concept`: Introductionto the AI Olfactory Engine (storytelling).
4. `section#data-sources`: Data integration points (Spotify, Literature, Mood Boards).
5. `section#process`: The 4-step journey (Connect -> Analyze -> Formulate -> Ship).
6. `section#stats`: Impact/Data section (number of unique notes, formulas generated).
7. `section#gallery`: Editorial showcase of generated bespoke bottles and aesthetic packaging.
8. `section#pricing`: Tiers (e.g., "The Essential Aura", "The Signature Extrait").
9. `section#faq`: Frequentlyasked questions.
10. `<footer>`: Social links, legal, newsletter signup, and secondary navigation.

Acknowledge this structure. Do not output the code yet.

## Round 2 â Interaction + Motion

Now, define the sophisticated interactive layer for AuraScent using vanilla JavaScript and CSS.

**1.Mandatory 8 Functional Interactions:**
1. **Navbar Scroll Transition**: Nav transforms from transparent with white text to a frosted glass background (`backdrop-filter: blur(10px)`) with dark text upon scrolling down.
2. **Scroll Reveal**: Elements smoothly fade in and translate slightly upward as they enter the viewport using`IntersectionObserver`.
3. **Stagger Animation**: Inside the `#process` and `#gallery` sections, cards must load sequentially with a 150ms delay between each element when revealed.
4. **Tabs**: In the `#data-sources` section, use a tabbed interface to switch between"Spotify History", "Literary Analysis", and "Visual Moodboard" explanations without page reload. Include `role="tablist"`, `role="tab"`, and `role="tabpanel"`.
5. **Count-up**: In the `#stats` section, numbers (e.g., "1,000,000+ Scent Notes") animate from 0 to their final value when scrolled into view.
6. **Modal**: Clicking "Connect Spotify" opens a centered modal with an ethereal backdrop overlay simulating an integration step. Must include `aria-modal="true"`, `role="dialog"`, trap focus, and close on 'Escape' or outside click.
7. **Accordion**: In the `#faq` section, smooth height transition for answers. Only one open at a time. Include `aria-expanded` attributes.
8. **Toast Notification**: Trigger a custom floating toast ("â¨ Aura analysis complete! Formula added to cart.") when the user clicks a specific formulation CTA. It must auto-dismiss after 3000ms.

**2. State Definitions (Buttons, Cards, Links)**
Every interactive element must strictly define 4 states:
- **Default**: Base styles using `:root` variables.
- **Hover**: Cursor transforms, slight scale up (`transform: translateY(-2px)`), enhanced shadow/glow, background color shift.
- **Active**: Scale down (`transform: scale(0.98)`), shadow reduction.
- **Focus**: High-contrast outline (`outline: 2px solidvar(--text-primary); outline-offset: 4px;`) for accessibility.

Acknowledge these interactive requirements. Do not output the code yet.

## Round 3 â Responsive + Accessibility

Ensure the AuraScent platform provides a flawless experience across all devices and meets modern accessibility standards.

**1. Breakpoints (Media Queries)**
Implement responsive design using these 4 breakpoints (Mobile-first approach):
- Mobile (Base): 320px - 480px (Stack columns, adjust typography to smaller variables, hide complex vapor backgrounds to save performance).
- Tablet (`@media (min-width: 481px)`): Adjust padding, 2-column grids for cards.
- Laptop (`@media (min-width: 769px)`): Full vapor animations, horizontal tab layouts, 3/4-column grids.
- Desktop (`@media (min-width:1025px)`): Max-container constraints (`max-width: var(--container-max-width)`), enhanced hover states, larger editorial typography.

**2. Accessibility (a11y)**
- **ARIA & Semantics**: Use `<button>` for actions, `<a>` for navigation. Apply `aria-label`, `aria-hidden`, `aria-controls`, and `aria-live="polite"` (for the Toast).
- **Keyboard Navigation**: The entire site must be navigable via the `Tab` key. Accordions, Tabs, and Modals must respond properly to `Enter` and `Space` keys. Focus must be managed (e.g., trapped inside the open modal, returned to trigger on close).
- **Reduced Motion (`@media (prefers-reduced-motion: reduce)`)**: 
  - Disable scroll reveals, count-up animations, and the fluid vapor backgroundanimations. 
  - Replace CSS transitions with instant state changes or extremely fast fades.

Acknowledge these responsive and a11y constraints. Do not output the code yet.

## Round 4 â Polish + Acceptance Self-Check

It is time to synthesize all previous rounds into the final, production-ready deliverable. The code must be polished, visually stunning, and highly performant. The CSS fluid vapor animation should use an elegant `@keyframes` setup manipulating `background-position` and gradients to simulate ethereal smoke/mist.

**Pre-Flight Acceptance Checklist:**
1. [ ] Is the output a single`index.html` file containing HTML, inline CSS (`<style>`), and inline JS (`<script>`)?
2. [ ] Are there zero external frameworks (No Tailwind, No React, No jQuery)?
3. [ ] Does the design system use the precise CSS `:root` variables specified?
4. [ ] Are all 10 semantic sections present (`hero`, `concept`, `data-sources`, etc.)?
5. [ ] Are all 8 functional interactions implemented flawlessly in Vanilla JS? (Modal, Accordion, Toast, Tabs, Scroll Reveal, Stagger, Count-up, Navbar transition).
6. [ ] Do all interactive elements have 4 clearly defined CSS states (Default/Hover/Active/Focus)?
7. [ ] Are the 4 required breakpoints handled with `@media` queries?
8. [ ] Is accessibility fully compliant (ARIA roles, keyboard nav, `prefers-reduced-motion`)?
9. [ ] Does the visual output match an ethereal, 2025-2026 high-editorial e-commerce platform?

GENERATE THE FINAL CODE NOW. Ensure you output the complete, uninterrupted HTML document.