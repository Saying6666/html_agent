## Round 1
Document: AURELINE SLEEPER CLUB IMMERSIVE APP VIEW
Brand: Aureline Sleeper Club
Product: premium overnight rail membership with private cabins and concierge booking
Year feel: 2025-2026
Deliverable: one complete single-file `index.html`
Core intent: create a futuristic luxury booking folio with cinematic glass depth.
Primary tone: refined, intimate, technical, and editorially confident.
Visual language: modern premium glassmorphism with polished glo lighting.
Hard quality target: this must feel like a flagship digital experience.
Hard ban: no outdated commodity SaaS composition.
Hard ban: no flat feature cards without layered materials.
Hard ban: no thick solid borders around primary surfaces.
Hard ban: no generic drop shadows detached from glass logic.
Hard ban: no default serif fallback look.
Hard ban: no plain utility UI without brand atmosphere.
Background should use deep obsidian gradient range.
Introduce ambient blurred light orbs for atmospheric depth.
Use heavy backdrop blur on major floating panels.
Use conic or multi-stop gradient borders for premium edge lighting.
Use subtle inner highlight to simulate polished glass rim.
Define a robust token set in `:root`.
Token group: backgrounds, surfaces, and overlays.
Token group: text hierarchy from strong to tertiary.
Token group: accent glows and semantic status colors.
Token group: spacing rhythm and radius scale.
Token group: motion durations and easing curves.
Token group: blur intensity and elevation shadows.
Token group: z-index layers for background, content, and overlays.
Primary color anchor: obsidian family around `#050505` and adjacent dark tones.
Accent anchor: aureline gold family for premium action cues.
Support accent companions: indigo, crimson, and cyan atmospheric glows.
Typography guidance: elegant sans for headlines and narrative copy.
Typography guidance: mono style reserved for numbers and train codes.
Typography guidance: maintain compact letter spacing on large titles.
Layout archetype: immersive floating dashboard rather than linear brochure.
Use layered panes with intentional overlap and depth separation.
Ensure first viewport communicates the product thesis quickly.
Mandatory section 1: floating navigation capsule with core routes.
Mandatory section 2: hero dashboard spread with statement and visual ticket object.
Mandatory section 3: holographic route map using inline SVG nodes.
Mandatory section 4: active departure board with realistic values.
Mandatory section 5: itinerary desk with tabbed cabin modes.
Mandatory section 6: journal-style editorial panel with atmospheric copy.
Mandatory section 7: concierge service module with premium support framing.
Mandatory section 8: gastronomy preview with bespoke menu highlights.
Mandatory section 9: membership tier spotlight with elevated styling.
Mandatory section 10: cabin technical specification grid.
Mandatory section 11: booking or waitlist lightbox-style form.
Mandatory section 12: minimal footer with legal and coordinate details.
Data realism rule: departure table must use plausible city pairs and times.
Data realism rule: status chips should use meaningful operational labels.
Data realism rule: membership copy should feel specific and credible.
Data realism rule: no placeholder-like writing in content areas.
Composition rule: keep major surfaces floating over dynamic background.
Composition rule: avoid one-dimensional vertical block stacking.
Composition rule: preserve readability through controlled contrast.
Composition rule: maintain premium spacing rhythm and alignment precision.
Technical constraint: all CSS must be inside a single `<style>` tag.
Technical constraint: all JavaScript must be inside a single `<script>` tag.
Technical constraint: no external libraries or runtime dependencies.
Technical constraint: no local images, fonts, CSS files, or JS files.
Technical constraint: no inline `style=""` attributes.
Accessibility baseline: semantic landmarks across all major regions.
Accessibility baseline: logical heading progression and descriptive labels.
Accessibility baseline: visible keyboard focus states with offset.
Accessibility baseline: reduced-motion-safe behavior for all animations.
Return target: final response must be only the finished HTML code.
## Round 2
Implement cinematic interactions that feel smooth and intentional.
Background orbs must drift with slow multi-axis keyframe motion.
Orb drift duration should vary per orb to avoid mechanical sync.
Glass panel hover should brighten internal glow subtly.
Glass panel hover should avoid abrupt transitions.
Main booking card should show animated border energy on hover.
Primary buttons should use gentle magnetic scale response.
Primary buttons should use refined glow bloom on interaction.
Tab switching must cross-fade content instead of hard swapping.
Tab switching must update selection states accurately.
Departure board rows should reveal with staggered entrance timing.
Map station nodes should pulse with offset timing.
Text links should display underline emergence animation on hover.
Input focus should trigger luminous ring without overpowering contrast.
Add toast system for lightweight confirmations.
Toast must support auto-hide and manual close.
Toast must announce through live region semantics.
Add modal or lightbox behavior for booking flow emphasis.
Modal must trap focus while open.
Modal must close with Escape.
Modal must restore focus to origin control when dismissed.
Implement accordion for FAQ or policy details if included.
Accordion must have keyboard and ARIA support.
Use IntersectionObserver for on-view reveals where practical.
Gate animation triggers to avoid repeated heavy reflows.
Prefer transform and opacity for animation performance.
Avoid layout-thrashing animation properties.
Use cubic-bezier curves for premium motion feel.
Keep interaction durations coherent across system.
Provide graceful no-motion paths under reduced-motion preference.
Implement form validation on client side only.
Prevent default form submission page reload.
Display inline validation messages with clear contrast.
On successful validation, trigger polished feedback state.
Write JavaScript in small, readable functions inside single script scope.
Use null checks before attaching listeners.
Avoid console errors in normal flow.
## Round 3
Deliver responsive behavior across four breakpoint tiers.
Tier `>= 1440px`: centered canvas with expansive atmospheric depth.
Tier `1024px - 1439px`: preserved hierarchy with tighter spacing.
Tier `768px - 1023px`: stacked composition with clean content grouping.
Tier `< 768px`: refined mobile execution retaining premium identity.
On desktop, maintain balance between hero, map, and departure systems.
On tablet, collapse wide modules to vertical sequence intentionally.
On tablet, allow horizontal tab rail only where useful.
On mobile, enforce touch targets at minimum practical size.
On mobile, reduce headline scale while preserving drama.
On mobile, keep forms and controls easy to operate one-handed.
On mobile, avoid accidental horizontal overflow.
Use `-webkit-backdrop-filter` companion where blur is critical.
Provide stable fallback when blur support is limited.
Ensure all interactive elements are keyboard reachable.
Apply `:focus-visible` styles with clear outline and spacing.
Assign roles for tablist, tabs, and tabpanels correctly.
Update ARIA selected states dynamically in script.
Connect labels and form controls through proper `for` and `id`.
Use fieldset and legend for grouped booking controls.
Mark required inputs with explicit accessibility metadata.
Provide descriptive text for icon-only controls.
Maintain readable contrast on translucent backgrounds.
Respect `prefers-reduced-motion` by reducing transform animation.
Under reduced motion, stop decorative orb drifting.
Under reduced motion, disable stagger transitions.
Under reduced motion, reveal values instantly instead of animated counts.
Keep departure board legible on compact widths.
Keep route map useful without overwhelming small screens.
Maintain consistent spacing scale throughout breakpoints.
Validate that footer links remain clear and tappable on mobile.
Validate that toast placement does not block critical controls.
Validate that modal fits viewport with safe scroll behavior.
## Round 4
Perform full QA polish pass before final output.
Check material fidelity across all glass surfaces.
Check gradient border rendering for edge artifacts.
Check inner rim highlights for consistent intensity.
Check typography hierarchy and data mono usage.
Check line lengths and paragraph rhythm for readability.
Check map layering so glowing nodes remain visible.
Check orb layers stay behind interactive content.
Check tab transitions for smoothness and state correctness.
Check form focus order and keyboard traversal continuity.
Check toast lifecycle and live-region announcements.
Check modal open and close behavior under keyboard-only navigation.
Check reduced-motion behavior for every animated module.
Check responsive behavior at all target tiers.
Check for accidental horizontal scroll on narrow screens.
Check semantic landmarks for structural clarity.
Check script for defensive guards and clean execution.
Check all required sections are present with meaningful copy.
Check no placeholder-like content remains in the UI text.
Check no external assets or frameworks are referenced.
Check no inline style attributes are present.
Check final HTML includes complete `<style>` and `<script>` blocks.
Check final document closes all tags correctly.
Output rule: return only the complete `index.html` code.
Output rule: avoid preface text before the HTML payload.
Output rule: ensure production-ready formatting and consistency.
GENERATE THE FINAL CODE NOW.
