## Round 1
Document: LAUNCH-OPS FLIGHT PLAN
Brand: Aster Fold
Product: AI launch-operations platform for product, research, lifecycle, and revenue teams
Year feel: 2025-2026
Deliverable: one single-file `index.html`
Core outcome: this should feel like an operating system for launches, not a generic landing page.
Visual direction: Modern Premium Glassmorphism with strong glo accents.
Primary mood: decisive, technical, cinematic, and calm under pressure.
Design references in spirit: Vercel polish, Linear clarity, Apple material precision.
Hard ban: no old SaaS hero plus three-card plus bland footer composition.
Hard ban: no flat cards with weak depth cues.
Hard ban: no thick opaque borders that kill glass realism.
Hard ban: no muddy shadows that read as legacy UI.
Use deep glass panels with layered blur and saturation.
Use glowing gradient border treatments through pseudo-elements.
Use inner rim highlights for crisp edge definition.
Use ambient blurred orbs behind main surfaces.
Use dark, premium, high-contrast base tones.
Use subtle parallax-friendly layering without motion sickness.
Typography split: geometric display sans for headings.
Typography split: neutral system sans for body copy.
Typography split: mono for telemetry labels and timestamps.
Macro layout must feel spatial, floating, and intentional.
Structure the page as three narrative chapters.
Chapter A: Ambient Thesis with command-level framing and product stance.
Chapter B: Mission Dashboard with tabs, console logic, and state feedback.
Chapter C: Proof Packet with evidence, objections, and conversion controls.
First viewport must show a signature visual device immediately.
Signature device: inline SVG launch ladder diagram inside frosted glass.
Launch ladder phases must be vertical and ordered.
Phase list: Discovery, Build, Launch, Stabilize, Expand.
Draw animated connectors between phase nodes.
Show directional flow cues that imply readiness progression.
Create a complete CSS token system in `:root`.
Define background gradient tokens for depth planes.
Define glass fill tokens for light and heavy panel variants.
Define border glow tokens for cool and warm accents.
Define text tokens for primary, secondary, muted, and inverse.
Define semantic tokens for success, warning, danger, and neutral.
Define spacing scale tokens with consistent rhythm.
Define radius scale tokens for panel families.
Define shadow tokens for outer elevation and inner rim polish.
Define motion duration tokens for micro, short, medium, and long.
Define easing tokens for standard, entrance, and deceleration curves.
Define blur tokens for backdrop tiers and decorative orbs.
Define z-index tokens for background, content, overlays, and modal layer.
Keep all styles in one `<style>` block.
Keep all logic in one `<script>` block.
Use only vanilla HTML, CSS, and JavaScript.
No framework, no library, no CDN dependency.
No local assets and no external font loading.
No inline `style=""` attributes in markup.
Build semantic regions with clear landmark roles.
Required sections list item 1: floating cockpit status bar.
Required sections list item 2: thesis hero with dual CTA and command preview.
Required sections list item 3: credibility strip in frosted pill format.
Required sections list item 4: signal mesh capability diagram.
Required sections list item 5: mission control dashboard window.
Required sections list item 6: metrics band with count-up behavior.
Required sections list item 7: launch ladder timeline overlay.
Required sections list item 8: comparison panel old stack versus Aster Fold.
Required sections list item 9: case study spotlight with measurable outcome.
Required sections list item 10: FAQ objection handling with interaction.
Required sections list item 11: final CTA app window containing form.
Required sections list item 12: minimal glass footer with confidence tone.
Information density rules: include micro labels and timestamps.
Information density rules: include at least one compact mini-table.
Information density rules: include one risk indicator set.
Information density rules: include one operator note block.
Content quality rules: write specific and realistic platform copy.
Content quality rules: avoid generic filler language.
Content quality rules: maintain product-operator vocabulary.
Composition rule: avoid a plain vertical stack from top to bottom.
Composition rule: overlap select glass surfaces for depth reveal.
Composition rule: keep focus zones obvious through contrast and spacing.
Composition rule: preserve breathing room despite dense content.
Accessibility baseline: semantic headings and logical order.
Accessibility baseline: keyboard-visible focus and strong outline offset.
Accessibility baseline: clear labels for every form control.
Accessibility baseline: reduced-motion friendly animation fallback.
Accessibility baseline: sufficient contrast against translucent layers.
Deliver only the final production-ready HTML in your response.
## Round 2
Expand interaction quality until it feels native to a high-end product OS.
Include an immersive frosted modal window for pilot clearance request.
Modal must trap focus while open.
Modal must close on Escape key.
Modal must return focus to triggering control on close.
Include a glass accordion for FAQ objections and responses.
Accordion must support keyboard activation.
Accordion must expose accurate ARIA state attributes.
Expanded accordion state should elevate glow intensity.
Include toast feedback with text `Command acknowledged`.
Toast must announce through an ARIA live region.
Toast must allow manual dismiss.
Toast must auto-hide after a sensible duration.
Include tabs for mission control workstreams.
Tab set values: Research, Lifecycle, Revenue, Incidents.
Tab switch must update ARIA semantics correctly.
Tab switch should cross-fade KPI and chart content.
Include scroll reveal transitions for major modules.
Reveal motion should combine opacity and slight translate.
Include staggered entrance for repeated card groups.
Include metric count-up when metric band enters viewport.
Count-up must trigger once per page session.
Count-up must honor reduced-motion settings.
Include navbar transition on scroll.
Navbar on scroll should shrink footprint.
Navbar on scroll should increase blur and rim clarity.
Hover system must change glow and border energy subtly.
Active states must remain readable and not flicker.
Button states must include hover, active, focus-visible, and disabled.
Form behavior must remain client-side only.
Form behavior must prevent default submission reload.
Form behavior must validate required fields and show inline errors.
Form behavior must send success feedback through toast system.
Use transform and opacity for animated movement.
Avoid animation of layout-heavy properties.
Keep interaction timings coherent across all modules.
Prefer cubic-bezier curves over default browser easing.
Use event delegation where practical for maintainability.
Guard against focus loss when dynamic panels update.
Prevent hidden panel content from being tab-focusable.
Use defensive JS checks for missing nodes.
Keep script readable and modular inside single file constraints.
## Round 3
Make the experience robust across four breakpoint tiers.
Tier one: `>= 1440px` with expansive layered composition.
Tier two: `1024px - 1439px` with compact but still spatial layout.
Tier three: `768px - 1023px` with stacked command plates.
Tier four: `< 768px` with refined mobile glass execution.
On ultra-wide, maintain centered max width with peripheral ambiance.
On desktop, tighten gutters while preserving hierarchy.
On tablet, collapse two-column regions to intentional stacks.
On small tablet, convert heavy dashboards into scroll-snap blocks where needed.
On mobile, keep touch targets at or above 44px.
On mobile, keep critical KPI content above fold without clutter.
On mobile, maintain glow identity while reducing GPU pressure.
Apply `-webkit-backdrop-filter` for Safari compatibility.
Use progressive fallback where backdrop filtering is unsupported.
Implement visible `:focus-visible` treatment on all interactives.
Maintain strict heading hierarchy from h1 downward.
Use landmarks: header, nav, main, section, aside, footer.
Use descriptive button labels and avoid vague action text.
Provide ARIA labels for icon-only buttons.
Give tablist and tabpanel correct role mapping.
Ensure accordion buttons expose expanded state.
Ensure modal has accessible title and description mapping.
Support `prefers-reduced-motion: reduce` for all animated systems.
When reduced motion is enabled, stop drifting orbs.
When reduced motion is enabled, disable stagger transforms.
When reduced motion is enabled, switch count-up to instant values.
Ensure mini-table remains readable on narrow screens.
Ensure comparison pane wraps without horizontal overflow.
Avoid horizontal scrolling except intentional tab rails.
Test color contrast against translucent surfaces, not only base background.
Check that CTA remains prominent at every breakpoint.
Check that form labels never detach from inputs.
Check that toast remains reachable on small viewports.
Keep line lengths controlled for readability.
Keep spacing rhythm consistent via token scale.
## Round 4
Polish this build to launch-grade quality for a premium product reveal.
Audit visual consistency across all panel radii and border glows.
Audit typography rhythm from hero headline to tiny telemetry text.
Audit icon and label alignment in dense data areas.
Audit orbital glow placement so they never obscure foreground text.
Audit depth stack so overlays always sit above base layers.
Audit motion timing so sequences feel cohesive, not random.
Audit focus states so keyboard navigation feels intentional.
Audit semantic structure for clear assistive-technology traversal.
Audit script for null-safe event binding and no console noise.
QA checklist item: single-file output only.
QA checklist item: no frameworks and no external dependencies.
QA checklist item: no local assets and no inline style attributes.
QA checklist item: modal, tabs, accordion, and toast all function.
QA checklist item: scroll reveal, stagger, and count-up all function.
QA checklist item: reduced-motion behavior is fully respected.
QA checklist item: responsive behavior is stable at all four tiers.
QA checklist item: ladder diagram is present and visibly animated.
QA checklist item: at least one compact mini-table is included.
QA checklist item: no placeholder-like copy appears in user-facing text.
QA checklist item: narrative voice stays precise and confident.
QA checklist item: call-to-action form feels integrated with glass system.
QA checklist item: footer is minimal yet polished.
Final instruction: return only the complete final `index.html` code.
Final instruction: ensure all tags are properly closed.
Final instruction: ensure CSS and JS are both included inline.
Final instruction: do not prepend explanations before the HTML.
GENERATE THE FINAL CODE NOW.
