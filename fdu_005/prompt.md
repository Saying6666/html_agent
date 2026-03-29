# Modern Premium Glassmorphism & Glo UI Landing Page

## Overview
You are an elite frontend engineer and UI/UX designer tasked with creating a breathtaking, modern landing page.
The aesthetic must follow a strict "Modern Premium Glassmorphism & Glo UI" design language.
This design style is characterized by deep dark backgrounds, vibrant glowing elements (neon cyan, purple, and emerald), and elegant translucent glass panels that sit above the light sources.

## Core Constraints
1. Single File: The entire application must be contained within a single index.html file.
2. No External Assets: Do not use external images. Use placeholders or CSS-generated graphics.
3. Allowed Libraries: Tailwind CSS via CDN, Alpine.js via CDN, Google Fonts, Phosphor/Lucide Icons via CDN.
4. Code Quality: Clean, semantic, and well-structured HTML/CSS/JS.

## Visual Guidelines (Glassmorphism & Glo UI)
- Backgrounds: Use deep, dark, or rich gradients (e.g., conic-gradient), accented by glowing, blurred orbs.
- Glass Panels: Elements should use translucent backgrounds (e.g., gba(255, 255, 255, 0.05)) with ackdrop-filter: blur(16px) and subtle glowing borders (order: 1px solid rgba(255, 255, 255, 0.1)).
- Typography: Crisp, high-contrast text overlaying the glass elements. Sans-serif like Inter or Plus Jakarta Sans.
- Accents: Neon glows casting light behind primary structural elements.

---

### Round 1: Foundation, Styling, and 10+ Layout Sections
Define the precise root variables and construct the DOM structure. Ensure 10+ detailed sections.

#### CSS Root Variables
Inject the following custom properties into the <style> block:
:root {
  --glo-bg-dark: #0a0a0f;
  --glo-surface: rgba(15, 15, 20, 0.6);
  --glo-border: rgba(255, 255, 255, 0.12);
  --glo-glass-blur: blur(24px);
  --glo-accent-primary: #00f0ff;
  --glo-accent-secondary: #7000ff;
  --glo-accent-tertiary: #ff007b;
  --glow-spread-sm: 0 0 10px rgba(0, 240, 255, 0.3);
  --glow-spread-lg: 0 0 40px rgba(112, 0, 255, 0.4);
  --text-main: #f8f8f2;
  --text-muted: #a1a1aa;
}

#### Section 1: Navigation Header
- Sticky top, transitions to frosted glass on scroll.
- Logo on left, nav links center, "Get Started" CTA right.
- Copy: Links for "Features", "Pricing", "About", "Contact".

#### Section 2: Hero Section
- Massive, bold headline: "Welcome to the Future of Glo".
- Subtitle: "Experience premium glassmorphism blended with vibrant ambient lighting."
- Animated conic-gradient background elements.
- Two buttons: Primary (glowing neon) and Secondary (transparent glass border).

#### Section 3: Value Proposition / Stats
- 4-column layout displaying key metrics in glowing text.
- Large typography for numbers: "99.9%", "50M+", "24/7", "+".
- Subtle labels underneath.

#### Section 4: Features Grid
- 3x2 grid of glass cards.
- Each card contains a glowing neon icon, title, and descriptive text.
- Placeholders: "Lightning Fast", "Bank-grade Security", "Unlimited Scaling", "Global Reach", "Zero Downtime", "Developer Friendly".

#### Section 5: Interactive Product Showcase
- A central focal point (CSS shape or abstract visual) representing the product core.
- Floating UI tooltips originating from the central element pointing out features.

#### Section 6: User Testimonials
- Marquee or masonry layout of 6 review cards.
- Include star ratings (using Lucide icons), user names, and role text placeholders.

#### Section 7: Integration Partners
- A horizontal row of 6 muted icon placeholders representing trusted company logos.
- Hovering over a logo makes it glow in full color.

#### Section 8: Pricing Tiers
- 3 distinct pricing cards: Starter, Pro, Enterprise.
- Center card (Pro) enlarged and highlighted with a neon border and intense globe behind it.
- Features list with checkmark icons. CTA buttons at the bottom.

#### Section 9: FAQ Accordion
- List of 5 frequently asked questions.
- Clickable headers that expand to reveal descriptive text.
- Use Alpine.js to handle the toggle state.

#### Section 10: Team / Creators
- 4 circular avatar placeholders with glowing rims.
- Names, roles, and social icons below each.

#### Section 11: Call to Action (CTA) Banner
- Full-width block with a vibrant conic-gradient overlay.
- Title: "Ready to step into the light?"
- Large glowing button: "Start Building Now".

#### Section 12: Footer
- 4 columns: Brand description, Product, Resources, Legal.
- Bottom border and copyright text.

---

### Round 2: 8+ Micro-interactions & Animations
Implement advanced, fluid interactions using CSS and JS/Alpine. Precision requires exact bezier curves.

1. **Primary Button Hover**:
   - Target: .btn-primary
   - Action: Scale up by 1.05, increase ox-shadow spread significantly.
   - Curve: 	ransition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);

2. **Glass Card Tilt/Glow on Mousemove**:
   - Target: .glass-card
   - Action: JS tracking cursor position to shift a radial gradient mask inside the card boundary.
   - Curve: 	ransition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);

3. **Scroll Reveal Fade-Up**:
   - Target: .reveal-on-scroll
   - Action: Opacity 0 to 1, TranslateY 40px to 0.
   - Curve: 	ransition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);

4. **Navbar Shrink & Frost**:
   - Target: header.navbar
   - Action: On scroll > 50px, add ackdrop-filter: blur(20px) and reduce vertical padding.
   - Curve: 	ransition: padding 0.4s ease, background 0.4s ease;

5. **FAQ Accordion Expansion**:
   - Target: .faq-content
   - Action: Max-height 0 to 500px, opacity 0 to 1.
   - Curve: 	ransition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease 0.1s;

6. **Ambient Background Orbs**:
   - Target: .ambient-orb
   - Action: Continuous slow translation and scale looping using @keyframes.
   - Timing: nimation: float-orb 20s infinite ease-in-out alternate;

7. **Pricing Card Highlight Focus**:
   - Target: .pricing-card:hover
   - Action: Desaturate non-hovered siblings, intensify border glow on the hovered card.
   - Curve: 	ransition: filter 0.4s ease, border-color 0.4s ease;

8. **Magnetic Icon Tooltips**:
   - Target: .tooltip-trigger
   - Action: Tooltip opacity 1, slight magnetic pull towards cursor.
   - Curve: 	ransition: transform 0.1s linear, opacity 0.2s ease-in;

---

### Round 3: Accessibility (A11y) & Responsive Strategy
Ensure the site is robust, fully accessible, and perfectly responsive.

#### ARIA Rules & Tabindex
- Use semantic landmarks: <main>, <header>, <footer>, <section>, and <nav>.
- All interactive elements must have a distinct focused state (e.g., ocus-visible:ring-2 focus-visible:ring-[color]).
- Accordion toggles must implement ria-expanded="true/false" and ria-controls="content-id".
- Buttons that only contain icons must have ria-label="description".
- Ensure logical 	abindex flows. Explicitly set 	abindex="0" on custom interactive elements (like the tilt cards if they act as links), and 	abindex="-1" on off-screen or hidden content.
- Contrast ratio of text must be at least 4.5:1 against the glass backgrounds. Avoid grey-on-grey.

#### Responsive Breakpoints (Tailwind)
- sm (640px): Convert mobile hamburger menu to top layout. Adjust hero text sizing (	ext-4xl).
- md (768px): Shift 1-column layouts to 2-columns (Features Grid, Stats, Footer columns).
- lg (1024px): Reveal desktop navigation, hide hamburger menu. Apply 3-column layout for Pricing and Testimonials.
- xl (1280px): Maximum container width enforcement (max-w-7xl mx-auto) to prevent over-stretching.
- 2xl (1536px): Increase border radii (ounded-3xl) and padding ratios for ultra-wide displays.

---

### Round 4: Thorough QA Checklist
Execute this extensive QA checklist before finalizing and delivering the code.

- [ ] 1. DOM Structure: Is all code cleanly contained within <html> ... </html> in a single block without external file links?
- [ ] 2. CSS Delivery: Are all custom variables and keyframes strictly in <style> tags within the <head>?
- [ ] 3. Library Integration: Are the Tailwind UI CDN, Alpine.js CDN, and Phosphor/Lucide Icon CDNs correctly referenced?
- [ ] 4. Visual Identity 1: Is the background color true to --glo-bg-dark to support neon glows?
- [ ] 5. Visual Identity 2: Are glass borders distinct but subtle? (Using rgba white at 0.1 to 0.15 opacity).
- [ ] 6. Visual Identity 3: Does every section completely map to the 12 sections defined in Round 1?
- [ ] 7. Typography: Do headings use an elegant sans-serif font like Inter and track correctly?
- [ ] 8. Micro-interaction 1: Does the primary CTA button scale and glow with the exact cubic-bezier(0.34, 1.56, 0.64, 1)?
- [ ] 9. Micro-interaction 2: Is the JS logic for the mousemove tilt reliably tracking the cursor on .glass-card elements?
- [ ] 10. Micro-interaction 3: Do scroll-reveal elements stay 100% hidden until they enter the viewport?
- [ ] 11. Micro-interaction 4: Does the sticky navbar successfully frost and shrink when scrolling past 50px?
- [ ] 12. Micro-interaction 5: Do the accordions cleanly transition their max-height without sudden snapping?
- [ ] 13. Micro-interaction 6: Are the conic-gradient ambient orbs moving continuously and smoothly across the hero background?
- [ ] 14. Micro-interaction 7: Do pricing cards correctly desaturate their sibling cards upon hover?
- [ ] 15. Micro-interaction 8: Are tooltips appearing accurately with a slight magnetic pull and fade?
- [ ] 16. A11y 1: Are ria-expanded and ria-controls explicitly defined and updated by Alpine.js inside the FAQ Accordion?
- [ ] 17. A11y 2: Can a keyboard-only user tab through every single interactive button and link on the page?
- [ ] 18. A11y 3: Are focus rings visibly using a matching neon color rather than the default browser blue?
- [ ] 19. A11y 4: Are contrast ratios strictly maintained (no #333 text on #0a0a0f glass)?
- [ ] 20. Responsive 1: Are 3-column feature grids cleanly broken down into a 1-column stack below the md (768px) breakpoint?
- [ ] 21. Responsive 2: Is the massive Hero headline scaled securely to prevent horizontal scrolling/overflow on 320px screens?
- [ ] 22. Responsive 3: Is the mobile menu fully accessible and toggleable using Alpine logic out of the box?
- [ ] 23. Asset Check: Confirm exactly 0 external .jpg, .png, or .svg files are used (all placeholders are CSS/divs).

### Final Delivery
Ensure that the final output provides exceptional polish, accurate DOM hints, correctly implemented bezier curves, robust accessibility, and an immersive Premium Glassmorphism UI experience.

### Round 5: Performance Optimization & Developer Experience
Ensure the final code is polished for performance and easily maintainable.

#### Performance Requirements
- CSS Minimization: Utilize Tailwind CSS utility classes aggressively instead of custom CSS blocks, outside of crucial theme variables and keyframes.
- Script Load: If script tags are utilized for Alpine or other CDN utilities, ensure they use the defer attribute.
- Paint Optimization: Heavily animated elements (like the rotating conic gradients or orbs) must use will-change: transform; or will-change: filter; to push the animation computations to the GPU.
- Box Shadow Cost: Limit stacked large blurred box shadows directly over one another to prevent unneeded recalculations and jank on scroll.

#### Maintainability Guidelines
- Code Commenting: Add semantic HTML comments marking the beginning and end of each of the 12 primary structural sections.
- Predictable Spacing: Rely on standard Tailwind spacing scales (py-12, gap-8) sequentially rather than arbitrary absolute pixels.
- Variable Reusability: Ensure all neon colors exclusively trace back to the custom CSS root variables defined in Round 1.

