## Round 1
You are a principal web product designer and senior frontend engineer.
Build a single-file `index.html` that looks launch-ready for a premium SaaS brand.
The visual language is modern glass surfaces, calm glow lighting, and sharp editorial typography.
The site must feel intentional, trustworthy, and conversion-oriented.
Keep all code in one HTML file with inline CSS and inline JavaScript.
Do not use external frameworks, external fonts, CDN assets, or local media files.
Use only semantic HTML tags and clear section landmarks.
Create a coherent brand story from top to bottom.
Write all copy with concrete business meaning and clear value statements.
Avoid thin marketing lines and avoid generic slogans.
Define design tokens in `:root` for color, spacing, radius, blur, and motion timing.
Set a dark but readable base theme with strong contrast.
Use at least one secondary light theme treatment inside a major module.
Add layered background effects using gradients and blurred blobs.
Make the glow subtle and controlled, never overexposed.
Ensure cards use translucent backgrounds with meaningful depth.
Use border, shadow, and backdrop blur together to shape hierarchy.
Create a strong header with logo, nav links, and a high-visibility CTA.
Header should become more opaque on scroll.
Hero must contain a bold headline, proof statement, and dual action row.
Add a metrics strip under hero with four operational KPIs.
Include a problem section that names pains in measurable terms.
Include a solution architecture section with three pillars.
Include a feature grid with at least six feature cards.
Each feature card must include title, short explanation, and business outcome.
Add an interactive workflow section with step switching.
Add a timeline section with milestones across one deployment quarter.
Add a case study section with before and after metrics.
Add a pricing section with three tiers and clear plan boundaries.
Add an FAQ accordion with at least six questions.
Add a final CTA block with urgency and confidence language.
Add a complete footer with product, company, legal, and contact columns.
Use copy that sounds like a real enterprise launch page.
Keep language specific, measurable, and professional.
All sections must have section labels and accessible headings.
Use `aria-label` where interactive controls need clarity.
Define content width constraints for comfortable reading.
Apply a clear spacing rhythm across all sections.
Use a 12-column mental grid and align modules consistently.
Keep line lengths moderate for readability.
Buttons must have default, hover, active, and focus-visible states.
Links must have visible hover and focus styles.
Inputs must have clear labels and validation hints.
The page must be fully usable by keyboard.
Do not trap focus in any component.
Support reduced motion users with a simplified animation path.
Ensure all text remains readable on small phones.
Use breakpoints for desktop, laptop, tablet, and mobile.
Keep navigation usable on mobile with a real toggle menu.
Mobile menu must open and close with animation and focus control.
Create high craft without visual clutter.
End Round 1 by restating that final output must be production-ready.

## Round 2
Implement rich interactions with vanilla JavaScript only.
Add scroll reveal for major sections using IntersectionObserver.
Use stagger timing for cards entering viewport.
Animate KPI counters when metrics strip enters view.
Build tabs for the workflow module with smooth panel transitions.
Add an accordion system for FAQ with single-open behavior.
Rotate chevron icons when FAQ items open.
Create a testimonial slider with previous and next controls.
Support swipe gestures for slider on touch screens.
Pause autoplay when user hovers or focuses slider.
Resume autoplay only when safe for user attention.
Add a sticky progress indicator for long page scroll.
Create a back-to-top control that appears after hero.
Use subtle parallax on background glow elements.
Throttle or use requestAnimationFrame for scroll-linked updates.
Prevent layout shift during animation.
Use transform and opacity for performant transitions.
Avoid costly paint-heavy effects on low-end devices.
Respect reduced motion and disable nonessential movement.
Animate CTA button shine only on hover, not continuously.
Use meaningful microcopy on interaction states.
Tab switches should update `aria-selected` and `tabindex`.
Accordion buttons should update `aria-expanded`.
Provide keyboard support for tabs and accordion.
Add form validation for email capture in footer.
Show inline validation messages with clear wording.
Avoid alert popups for normal validation flow.
Create a lightweight toast message for form success.
Toast must be dismissible and screen-reader friendly.
Implement header shadow intensification when scrolling.
Highlight active nav section as user scrolls.
Add smooth scrolling for anchor navigation.
Guard smooth scrolling for reduced motion users.
Ensure interaction timing feels responsive, not rushed.
Use one easing family consistently across components.
Document small JS modules with short comments.
Keep function names clear and purpose-driven.
No dead code and no unused selectors.
No console errors in normal operation.
No runtime exceptions during rapid clicks.
Protect against null selectors before binding events.
Run initialization after DOM content is ready.
Make every interaction feel intentional and reliable.
End Round 2 with instruction to keep JS readable and modular.

## Round 3
Prioritize accessibility, responsiveness, and reliability.
Use one `main` landmark and one `h1` on the page.
Follow heading order without skipping logical levels.
Guarantee color contrast for text and controls.
Avoid tiny tap targets on mobile.
Set minimum target size for buttons and icon controls.
Use visible focus rings with offset for dark surfaces.
Never remove default focus without replacement.
Provide descriptive link text, not vague labels.
Add `aria-live` for toast status updates.
Ensure form fields have explicit labels.
Use `autocomplete` attributes where appropriate.
Keep reading order aligned with visual order.
Prevent horizontal scrolling at common mobile widths.
Test layout at 360px, 768px, 1024px, and 1440px.
Stack complex grids gracefully on narrow screens.
Reduce blur intensity on low power mobile profiles.
Keep critical actions above fold on phones.
Ensure menu toggle remains visible when keyboard appears.
Use safe-area padding for modern phone notches.
Set reasonable max-width for text-heavy sections.
Keep hero headline readable on two to four lines on mobile.
Shorten long labels at small breakpoints.
Maintain consistent vertical rhythm after wrapping.
Do not allow cards to overlap accidentally.
Keep z-index scale documented and controlled.
Avoid fixed heights for content-heavy panels.
Allow FAQ answers to expand naturally.
Ensure pricing cards align at varied content lengths.
Keep testimonial text legible at all sizes.
Prevent animation from obscuring core information.
Add fallback styles if backdrop-filter is unavailable.
Fallback must still look premium and readable.
Use feature queries for blur support when needed.
Avoid dependency on experimental APIs.
Guard slider logic when there is only one slide.
Guard tab logic when optional panels are missing.
Ensure no component breaks if copy length increases.
Keep CSS selectors scoped and maintainable.
Group related rules by section with short comments.
Use clear naming convention for utility classes.
Avoid overusing utility classes when semantic classes fit better.
Ensure footer links are keyboard reachable in logical order.
Confirm no hidden interactive elements receive focus.
Confirm all buttons have discernible text.
Confirm icon-only buttons have `aria-label`.
Confirm no duplicate IDs across document.
Confirm scripts run without blocking initial paint.
Keep first contentful paint feeling immediate.
End Round 3 by requiring robust cross-device behavior.

## Round 4
Perform a full quality pass before returning final HTML.
Check that all major sections are present and coherent.
Check that visual style remains consistent across modules.
Check that CTA hierarchy is clear and persuasive.
Check that copy is concrete and business-focused.
Check that every interactive control works by mouse and keyboard.
Check that reduced motion mode is respected globally.
Check that counters, tabs, accordion, and slider all behave correctly.
Check that no component causes console errors.
Check that no external asset requests are required.
Check that no inline `style` attributes are used.
Check that all CSS and JS stay inside the single file.
Check that nav links map to valid section anchors.
Check that focus order is logical from top to bottom.
Check that contrast remains strong in all states.
Check that mobile menu can be closed with Escape.
Check that form validation messages are clear and polite.
Check that toast does not block critical controls.
Check that page footer contains legal and contact essentials.
Check that hero and pricing sections support conversion goals.
Check that the page feels premium rather than generic.
Check that background effects never reduce readability.
Check that motion supports clarity instead of distraction.
Check that spacing remains clean at every breakpoint.
Check that typography scale is balanced and consistent.
Check that no section feels unfinished.
Check that no line of copy sounds robotic or repetitive.
Check that final document is complete and publication-ready.
Output only the final `index.html` code.
