# fdu_015

## Round 1

Create a premium long-scroll single-file `src/index.html` for a **creative design studio portfolio** called **NOIR/ATELIER**.

Concept: A dark-mode brutalist creative studio showcasing bold typography, experimental layouts, and immersive digital experiences. The studio specializes in brand identity, web experiences, and motion design for avant-garde clients.

Audience: Art directors, creative agencies, luxury brands, and forward-thinking companies seeking unconventional design partnerships.

Style direction: **Neo-Brutalism meets Dark Mode** - raw geometric shapes, high contrast, aggressive typography, exposed grid systems, with refined dark aesthetics and subtle glow accents.

Component language: Oversized display typography, asymmetric grid layouts, glitch text effects, magnetic buttons, scroll-triggered reveals, custom cursor, noise texture overlays, and dramatic section transitions.

Color direction: Deep black (#0A0A0A), charcoal (#1A1A1A), electric lime (#CCFF00), stark white (#FFFFFF), subtle grays for hierarchy, with occasional blood red (#FF0040) accents for dramatic moments.

Typography direction: Brutalist sans-serif display fonts (Space Grotesk/Archivo Black) for headlines, monospace for technical details, with extreme scale contrasts (120px+ headlines vs 12px body).

Motion direction: Aggressive, unexpected, and deliberate - sharp easing curves, staggered reveals, parallax layers, text scramble effects, and smooth scroll hijacking for narrative pacing.

Build a complete page with these sections:
1. **Preloader** - Text scramble animation revealing studio name
2. **Navigation** - Fixed minimal nav with magnetic hover states
3. **Hero** - Full viewport with massive typography, glitch effects, and custom cursor
4. **Manifesto** - Scrolling marquee text + studio philosophy statement
5. **Selected Works** - Asymmetric project grid with hover distortion effects
6. **Services** - Accordion-style service list with expanding details
7. **Process** - Horizontal scroll section showing workflow stages
8. **Stats** - Counter animations with brutalist number display
9. **Testimonials** - Draggable carousel with bold quote typography
10. **Team** - Hover-reveal portrait grid with glitch transitions
11. **Contact** - Large CTA with animated form fields
12. **Footer** - Minimal with social links and copyright

Required interactions (minimum 8):
1. Custom cursor that transforms on hover states
2. Text scramble/decode effects on headlines
3. Magnetic button hover with physics-based attraction
4. Scroll-triggered parallax layers
5. Project card hover with image distortion/glitch
6. Service accordion expand/collapse
7. Horizontal scroll section with drag/scroll control
8. Animated counter numbers on scroll into view
9. Testimonial carousel with drag and snap
10. Form field focus animations with label floating
11. Preloader exit animation with page reveal
12. Smooth scroll navigation with anchor offset

The page should feel like an immersive art experience rather than a conventional portfolio - challenging, memorable, and unmistakably bold.

## Round 2

Deepen the visual impact and content density.

**Hero Section:** Create a dramatic full-viewport experience with layered parallax. Background: subtle animated noise texture. Foreground: Massive "NOIR" text (200px+) with CSS clip-path reveal animation. Secondary "ATELIER" text with character-by-character scramble effect on load. Include a pulsing scroll indicator with custom cursor interaction.

**Manifesto Section:** Full-width infinite horizontal marquee with duplicated studio philosophy text. Below: Large statement text (48px+) with word-by-word fade-in on scroll. Add floating geometric shapes (lime green rectangles) with parallax movement.

**Selected Works:** 4 project case studies in asymmetric 2-column layout. Each project: oversized number (01-04), project title with hover text scramble, category tags, year, and thumbnail with RGB split glitch effect on hover. Projects should overlap slightly for depth. Include view case study button with magnetic hover.

**Services:** 6 service categories (Brand Identity, Web Design, Motion Design, Art Direction, Creative Strategy, Development). Each as horizontal bar with service name, expandable description, and related tools/technologies. Hover reveals lime accent bar sliding in from left.

**Process:** Horizontal scroll container with 4 stages (Discovery, Concept, Creation, Delivery). Each stage: large number, title, description, and associated deliverables. Progress indicator showing current stage. Navigation arrows and drag support.

**Stats:** 4 key metrics in brutalist display - "127 Projects", "48 Awards", "12 Years", "∞ Ideas". Each number counts up from 0 with easing when scrolled into view. Large monospace typography with lime accent underlines.

**Testimonials:** 3 client testimonials in draggable slider. Each: large quote marks, testimonial text (24px), client name, company, and project type. Background color shifts subtly between slides.

**Team:** 4 core team members in grid. Default state: name + role. Hover: reveals portrait (use Unsplash placeholder), bio text, and social links with glitch transition effect.

**Contact:** Massive "LET'S CREATE" headline with text fill animation on scroll. Below: minimalist contact form (name, email, project type, budget range, message) with animated focus states. Large submit button with magnetic hover and loading state animation.

Ensure all sections have substantial vertical depth for a long full-page screenshot. Transitions between sections should feel intentional and dramatic.

## Round 3

Polish all interaction states and technical implementation details.

**Custom Cursor:** Implement with CSS transforms for performance. Default: small circle. Hover on links: expand + blend mode difference. Hover on projects: display "VIEW" text inside. Hide on mobile/touch devices via media query.

**Text Scramble Effect:** Create reusable JavaScript class using character set (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789). Trigger on: page load for main headline, hover for project titles, scroll reveal for section headers. Duration: 800-1200ms with easing.

**Magnetic Buttons:** Use mouse position tracking with CSS transform translate. Attraction radius: 50px. Movement range: 20px max. Apply to all CTA buttons and nav links. Spring-back animation on mouse leave.

**Scroll-Triggered Animations:** Use Intersection Observer with threshold 0.2. Elements animate once when entering viewport. Stagger delays for grouped elements (0.1s between items). Use transform and opacity only for GPU acceleration.

**Project Card Effects:** On hover: thumbnail scales 1.05, RGB split filter activates, title text scrambles. Overlay slides up from bottom with project details. Transition duration: 400ms with cubic-bezier(0.16, 1, 0.3, 1).

**Service Accordion:** Click to expand. Only one open at a time. Content height animation using max-height technique. Chevron icon rotates 180deg. Active state: lime left border, white background shift.

**Horizontal Scroll Section:** Track container width vs viewport. Map vertical scroll progress to horizontal translate. Add grab cursor and mouse drag support. Progress bar at top showing section completion.

**Counter Animation:** Animate from 0 to target value over 2000ms. Use easing function for realistic counting. Trigger once when 50% visible. Special handling for "∞" symbol.

**Form Interactions:** Floating labels - placeholder becomes label on focus. Input underline expands from center on focus. Submit button shows loading spinner, then success checkmark on completion.

**Preloader:** Full screen black overlay. Text: "NOIR/ATELIER" with character scramble. Progress bar (lime) across bottom. Exit: curtain split animation revealing content. Total duration: 2500ms.

**Accessibility:** All buttons have aria-label. Form inputs have associated labels. Focus states visible. Reduced motion media query respected. Skip to content link included.

**Performance:** No external libraries. CSS animations use transform/opacity. Will-change applied sparingly. Images lazy loaded. No layout thrashing in scroll handlers.

## Round 4

Final refinement and quality assurance pass.

**Visual Polish:**
- Ensure lime accent color (#CCFF00) used strategically, not excessively
- Verify all text has sufficient contrast (WCAG AA minimum)
- Check spacing consistency - use 8px grid system
- Validate typography scale creates clear hierarchy
- Confirm all hover states feel responsive and intentional

**Animation Quality:**
- All animations run at 60fps
- No jank or stutter during scroll
- Preloader doesn't block too long
- Text scramble feels purposeful, not gimmicky
- Magnetic buttons don't feel laggy

**Content Completeness:**
- All 12 sections present and visually distinct
- No placeholder text - all copy feels authentic
- Project descriptions evoke real case studies
- Contact form includes all specified fields
- Footer has actual social links and copyright

**Technical Compliance:**
- Single file HTML with inline CSS and JS
- No external dependencies except Google Fonts
- No local image references - use Unsplash URLs
- All SVG icons inline
- File size optimized but >10KB

**Interaction Count Verification:**
1. Custom cursor with state transformations ✓
2. Text scramble/decode effects ✓
3. Magnetic button physics ✓
4. Scroll-triggered parallax ✓
5. Project card RGB glitch hover ✓
6. Service accordion expand/collapse ✓
7. Horizontal scroll process section ✓
8. Animated stat counters ✓
9. Draggable testimonial carousel ✓
10. Form field focus animations ✓
11. Preloader with page reveal ✓
12. Smooth scroll navigation ✓

**Final Check:**
- Open file directly in browser - works immediately
- All images load from remote URLs
- No console errors
- Responsive behavior acceptable (desktop-first, tablet adapts)
- Dark mode only - no light variant needed

Return one complete self-contained `src/index.html` file with no external dependencies.
