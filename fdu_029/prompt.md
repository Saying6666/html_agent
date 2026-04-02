## Round 1
You are a lead product storyteller and senior frontend engineer.
Create a single-file `index.html` for an enterprise language readiness platform.
The page must communicate strategic value to operations leaders and executives.
Style direction is premium glass surfaces, disciplined glow, and precise typography.
All code must live in one file with inline CSS and inline JavaScript.
No external frameworks, no package imports, and no external media.
Use semantic HTML and clear structural landmarks.
Craft real copy with specific benefits and measurable outcomes.
Write concise, credible, and conversion-focused content.
Set design tokens in `:root` for spacing, color, motion, blur, and radii.
Build a deep dark canvas with restrained neon accents.
Blend translucent panels with border light and layered shadows.
Use backdrop blur where supported and graceful fallback where unsupported.
Introduce ambient gradient fields behind core modules.
Ensure effects enhance hierarchy instead of creating noise.
Create a sticky top navigation with clear section jump links.
Top navigation must include primary CTA and secondary navigation cluster.
Hero section must include positioning statement and operational proof.
Add a short evidence row with trusted customer names as text marks.
Add a KPI board with four metrics tied to business process health.
Add a pain map section describing communication friction points.
Add a solution framework section with three implementation pillars.
Add a feature matrix with six detailed feature cards.
Each feature card must include capability, impact, and owner persona.
Add an adoption timeline covering discovery to steady-state operation.
Add an interactive role view for HR, sales, support, and engineering.
Role view must switch content via tabs.
Add a readiness score section with explanatory legend.
Add a case story section with baseline and improved metrics.
Add an ROI estimator section with interactive inputs.
Add a pricing section with tier differentiation and governance notes.
Add a security and compliance section with policy highlights.
Add a FAQ section with practical buying and implementation questions.
Add a final CTA section framed as executive next step.
Add a footer with documentation, legal, and regional contact paths.
Keep copy mature and suitable for board-level review.
Avoid vague claims and avoid inflated promises.
Use consistent spacing rhythm and visual cadence.
Keep content width readable and scan-friendly.
Use meaningful labels on controls and forms.
Ensure keyboard users can reach every action.
Ensure focus indicators are highly visible on dark backgrounds.
Provide clear headings for all major modules.
Keep hierarchy consistent from top to bottom.
Define responsive behavior for desktop, tablet, and mobile.
Use a mobile nav drawer with proper state handling.
Keep mobile interactions smooth and understandable.
Ensure page still looks premium on low-resolution displays.
Close Round 1 by confirming production-grade standards.

## Round 2
Implement interaction logic with clean vanilla JavaScript.
Use IntersectionObserver for section reveal transitions.
Reveal cards with subtle stagger for readability.
Animate KPI values when their section becomes visible.
Build tab logic for role-based readiness with keyboard support.
Update ARIA states on every tab interaction.
Add accordion behavior for FAQ with one expanded item at a time.
Animate accordion height smoothly without jank.
Rotate disclosure icons based on open state.
Add a testimonial carousel with manual controls.
Allow touch drag navigation in the carousel.
Pause automatic movement on hover or focus.
Resume motion after interaction ends.
Add scroll spy behavior for top navigation links.
Highlight active section based on viewport position.
Add smooth anchor scrolling with reduced motion fallback.
Add a back-to-top control triggered by scroll depth.
Use requestAnimationFrame for scroll-linked visual updates.
Apply subtle parallax on ambient glow elements.
Keep parallax amplitude low for comfort.
Disable parallax when reduced motion is requested.
Add form validation for newsletter or contact capture.
Use inline helper text to explain invalid input.
Use polite toast messaging for success confirmation.
Ensure toast can be dismissed by keyboard.
Keep interaction timing between 160ms and 320ms where possible.
Use a consistent easing curve family across components.
Prevent click handlers from binding multiple times.
Check all query selectors before event binding.
Initialize scripts on DOMContentLoaded.
Modularize script by feature function blocks.
Avoid global variable pollution.
Ensure no console warnings during typical usage.
Ensure no uncaught exceptions during rapid interactions.
Add lightweight state management for tabs and accordion.
Use dataset attributes where this simplifies control mapping.
Avoid hidden state that cannot be inferred from DOM.
Keep JS comments short and practical.
Keep CSS transitions focused on transform and opacity.
Avoid expensive effects during scroll.
Use class toggles instead of inline style manipulation.
Preserve readable code structure in both CSS and JS.
End Round 2 by requiring stable and elegant behavior.

## Round 3
Enforce accessibility and responsive quality gates.
Use one `h1` and maintain logical heading progression.
Include landmark roles for header, main, nav, and footer.
Ensure all control elements have discernible text.
Provide `aria-label` for icon-only buttons.
Never hide focus states without replacement.
Use high-contrast text on translucent surfaces.
Keep body text size comfortable across devices.
Maintain target sizes suitable for touch usage.
Support keyboard operation for all interactive modules.
Support Escape to close mobile navigation drawer.
Prevent background scroll when mobile drawer is open.
Restore focus to menu button when drawer closes.
Use `aria-expanded` on drawer and accordion toggles.
Use `aria-controls` where relationships need explicit mapping.
Ensure form fields are associated with labels.
Use descriptive error messages for validation.
Avoid color-only indicators for critical states.
Verify no horizontal overflow at 360px viewport width.
Adapt grid sections to one-column layouts on small screens.
Keep CTA blocks readable on narrow viewports.
Avoid clipping long words in cards and buttons.
Use clamp-based typography where appropriate.
Preserve spacing rhythm when modules stack vertically.
Reduce blur and heavy effects on weaker mobile devices.
Provide fallback colors when blur is unsupported.
Keep z-index layering documented and simple.
Avoid absolute positioning that breaks reading order.
Ensure tab panels remain accessible when hidden.
Hide inactive panels from assistive tech when appropriate.
Keep slider controls reachable in tab order.
Allow testimonial cards to wrap text naturally.
Keep pricing cards equalized without fixed text heights.
Ensure FAQ transitions do not block screen reader updates.
Keep script execution non-blocking for initial render.
Avoid synchronous heavy computation on load.
Prioritize quick first visual feedback.
Use clear class naming conventions.
Group CSS by module for maintainability.
Avoid excessive selector specificity.
Avoid duplicated declarations across components.
Validate there are no duplicate element IDs.
Confirm internal anchor targets all exist.
Confirm all section links scroll to intended destination.
Confirm reduced motion path still communicates hierarchy.
End Round 3 by confirming cross-device robustness.

## Round 4
Run final QA before outputting final HTML.
Verify every required section is present and complete.
Verify visual language stays coherent across the full page.
Verify copy remains professional and context-aware.
Verify no section reads like filler.
Verify all controls have clear interaction feedback.
Verify tab, accordion, slider, and form flows are stable.
Verify reduced motion mode disables decorative movement.
Verify no external resources are required for rendering.
Verify all CSS and JS remain inline in this file.
Verify no inline `style` attributes are present.
Verify keyboard-only navigation works end to end.
Verify focus order follows reading order.
Verify focus rings remain visible on dark surfaces.
Verify contrast is strong for text and controls.
Verify mobile drawer opens, traps correctly, and closes cleanly.
Verify anchor navigation points to valid section IDs.
Verify no dead links appear in nav or footer.
Verify all major CTA actions remain visible on mobile.
Verify pricing content is clear and non-ambiguous.
Verify ROI estimator updates numbers accurately.
Verify validation copy helps users recover quickly.
Verify toast behavior is non-intrusive and dismissible.
Verify footer includes legal and contact essentials.
Verify no console errors appear during interaction testing.
Verify no runtime failures occur during repeated toggles.
Verify spacing and typography remain polished at all breakpoints.
Verify final result feels premium and credible.
Verify the document is ready for immediate publishing.
Return only final `index.html` code.
