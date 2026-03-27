# fdu_016

## Round 1
Create a premium long-scroll single-file `src/index.html` for a **health tech e-commerce** brand called **VitaPure**.
Concept: A next-generation wellness marketplace offering smart supplements, personalized nutrition plans, and biohacking devices. The site targets health-conscious millennials and Gen Z who value transparency, sustainability, and cutting-edge wellness technology.
Style direction: **Organic Modernism** - blending natural earthy aesthetics with sleek digital interfaces. Think living moss textures meeting precision glassmorphism, botanical illustrations fused with data visualization.
Color direction: Sage green (#7C9A6B) as primary, warm sand (#F5F0E8) as background, deep forest (#2D3E2F) for text, terracotta accents (#C17A5C), and crisp white for contrast.
Typography direction: Editorial serif headings (Playfair Display) paired with clean geometric sans-serif body text (Inter), creating a sophisticated yet approachable reading experience.
Motion direction: Fluid, breathing animations that mimic natural rhythms - gentle pulses, organic growth transitions, smooth parallax layers like wind through leaves.
Build a complete page with these sections:
1. Sticky navbar with glassmorphism effect and cart icon
2. Hero with dynamic particle system representing nutrients
3. Product categories with hover morphing cards
4. Featured smart supplements with 3D tilt effect
5. Personalization quiz teaser with progress indicator
6. Sustainability commitment with counter animations
7. Customer transformation stories with before/after slider
8. Expert endorsements with testimonial carousel
9. Subscription benefits with interactive pricing toggle
10. Blog/Insights preview with magnetic hover cards
11. Newsletter signup with animated input field
12. Footer with expanding accordion links
Required interactions: navbar scroll transformation, particle system, card 3D tilt, counter animation, before/after slider, pricing toggle, testimonial carousel, magnetic hover, accordion expansion, scroll reveal animations, smooth anchor scrolling.

## Round 2
Deepen the layout and content density to create a truly immersive shopping experience.
The hero should feature an animated particle system representing vitamins and nutrients floating organically, with a compelling value proposition about personalized wellness.
Product cards should display real supplement products with believable names like "Adaptogen Complex", "Omega-3 Algae Oil", "Sleep Support Melatonin+" with pricing, ratings, and "Add to Cart" functionality.
Add believable copy around ingredient transparency, third-party testing, sustainable sourcing, and personalized recommendations based on lifestyle quizzes.
Include a "Lab Results" section showing purity certifications with interactive verification badges.
Create a "Wellness Journey" timeline showing how customers progress from assessment to personalized routine.
Make the sustainability section show concrete impact metrics: plastic bottles saved, carbon offset, ethical sourcing percentages with animated counters.
Add a community section showing real customer photos (use Unsplash lifestyle imagery) with their wellness stories.
Ensure the personalization quiz teaser feels interactive with a mini step-indicator and benefit highlights.
The subscription toggle should show monthly vs annual pricing with savings calculation.
Keep enough vertical depth for a long full-page screenshot, with multiple strong section transitions and no thin filler sections. Each section should feel substantial and purposeful.

## Round 3
Polish all interaction states and compliance details to perfection.
Navbar: On scroll, transform from transparent to frosted glass with backdrop-filter and -webkit-backdrop-filter. Logo scales down slightly. Cart icon shows item count badge with pulse animation on update.
Particle system: Organic floating motion using canvas or CSS animations, particles gently pulse and drift like nutrients in a solution. Responds subtly to mouse movement.
Product cards: 3D tilt effect on hover using transform perspective, shadow shifts dynamically. Image zooms slightly within container. "Add to Cart" button reveals with slide-up animation.
Counter animations: Numbers count up from 0 when scrolling into view, using Intersection Observer. Easing function for natural deceleration.
Before/After slider: Draggable divider with smooth tracking, labels fade in/out based on position. Touch support for mobile.
Pricing toggle: Smooth transition between monthly and annual prices, savings badge animates in. Toggle switch has satisfying snap animation.
Testimonial carousel: Auto-advances every 5 seconds, manual navigation dots. Cross-fade transition between slides. Pause on hover.
Magnetic hover: Cards subtly follow cursor within bounds using CSS transforms, creating a "magnetic" attraction effect.
Accordion: Smooth height transition, icon rotates 180 degrees, content fades in. Only one section open at a time.
Scroll reveal: Elements fade in and slide up with staggered delays. Different directions for visual interest (left, right, up).
Form inputs: Floating labels, focus states with animated borders. Submit button shows loading state.
Ensure all form controls have associated labels for accessibility. All icon buttons have aria-label attributes.
Ensure responsive design works beautifully from 320px mobile to 4K desktop. Mobile hamburger menu with smooth slide-in panel.
Keep all CSS and JS inline inside `index.html`. No external CSS or JS files.
Do not use React, Vue, Svelte, jQuery, or any build step.
Do not reference local images, local fonts, local CSS, or local JS.
Use remote imagery from Unsplash only and inline SVG icons.
Return only the final `src/index.html` content with no explanation.

## Round 4
Final refinement pass for premium quality.
The result should feel like a real high-end wellness e-commerce site, not a template or demo.
Avoid generic stock photo energy - use specific, evocative Unsplash images that feel authentic.
Ensure all animations run at 60fps with will-change optimizations and transform/opacity only.
Check that all interactive elements have clear hover, active, and focus states.
Verify color contrast ratios meet WCAG AA standards.
Ensure the page has enough content depth for a substantial full-page screenshot (minimum 8000px height).
All buttons and links should feel tactile and responsive.
The particle system should not impact performance - optimize with requestAnimationFrame and limited particle count.
Final check: backdrop-filter has -webkit-backdrop-filter fallback, all forms have accessible labels, all icon buttons have aria-label.
Return one complete self-contained `index.html` that opens directly in a browser and immediately impresses with its polish and attention to detail.
