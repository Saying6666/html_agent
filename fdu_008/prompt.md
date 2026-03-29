## Round 1

You are designing and building a 2025-2026 launch site for **Harborline Atlas**.
Harborline Atlas is a carbon-aware maritime operations platform for:
- luxury passenger terminals.
- expedition fleets.
- coastal logistics teams.

This page must feel like a funded product launch.
It must not feel like a classroom demo.
It must not feel like a generic SaaS template.
It must not recycle the same "dark dashboard + copper accents" formula from other cases.

Hard delivery constraints:
Output one complete self-contained `index.html` only.
All CSS must be inside a single `<style>`.
All JavaScript must be inside a single `<script>`.
No React.
No Vue.
No Svelte.
No external libraries (no GSAP, no jQuery).
No build step.
No local assets and no local file references.
No external images, fonts, CSS, or JS.
If visuals are needed, use pure CSS and inline SVG.
Do not use `style=""` attributes in markup.
Responsive and accessible are mandatory.

Target Aesthetic: "Modern Premium Glassmorphism & Glo UI"
Think: polished stone, deep ink, sea mist, and elegant transparency with ambient glows.
- Use `backdrop-filter: blur(20px)` and glasspane techniques to layer content beautifully over deep scenes.
- Employ conic-gradient borders with glass properties for an extremely high-end luminous look.
- Create ambient, blurred orbs floating slowly in the background to bring the page to life.
- Avoid "clubby cyber" aesthetics. Ensure the "Glo UI" feels like luxury technology (soft diffuse glows).
- Micro-interactions must be precise and tangible.

Typography direction:
Display type should feel like a high-end travel editorial cover.
Body type should be disciplined and highly readable.
Use tabular numerals for schedules and metrics.
Use small caps or label styling for signage-like microcopy.

Design system tokens required (define in CSS `:root` and use consistently):
- Background layers (ink, mist, stone).
- Glass layers (semi-transparent white, dark glass).
- Borders and rules (hairline glass edges).
- Text hierarchy (ink, muted, inverse).
- Accents (mist cyan, glowing amber, deep oceanic blue).
- Semantic status (on-time, watch, delay, reroute).
- Focus ring color.
- Spacing scale.
- Radius scale.
- Shadow scale.
- Motion durations and easings.
- Type scale.

Layout mandate (must be a distinct silhouette in 12+ sections):
Build the page as a "terminal journey" narrative.
Structure it like a passenger flow storyboard, not a product feature list.

Section 1: "Arrival Hall" Hero
A stunning introduction to Harborline Atlas, featuring blurred orbs in the background and a glassy, elevated search/input console. High-impact typography.

Section 2: Trust Strip & Global Footprint
Sleek typography highlighting global luxury terminals powered by Harborline.

Section 3: Product Mission: Carbon-Aware Routing
A glassmorphic statement piece explaining the sustainable, carbon-centered operational philosophy.

Section 4: "Concourse Board" Live Console
A full-bleed "Departure Board" module that looks like a premium LED signage wall.
It must show berth windows, turnaround slots, carbon intensity indicator, and service notes. Plausible fake data.

Section 5: "Terminal Map" Module (Operations Hub)
Map with selectable zones (berths, lounges, security, embarkation) using inline SVG.
Selecting a zone updates a detail panel. Must feel like a luxurious terminal blueprint.

Section 6: Passenger Flow & Boarding Analytics
Dynamic charts (using CSS/SVG) illustrating boarding speed and flow efficiency wrapped in glass cards.

Section 7: "Carbon Receipt" Ledger
Make it look like a receipt or ledger on ticket paper or frosted glass. Summarize scope signal, fuel mode assumptions, terminal energy window, per-guest carbon note.

Section 8: "Expedition Brief" For Fleets
A dedicated narrative spread for smaller luxury expedition vessels, showcasing remote route optimizations.

Section 9: Core Platform Capabilities
A grid of 4-6 beautiful glass cards with conic gradient borders detailing precise features (e.g. Route Analytics, Fleet Syndication).

Section 10: Count-Up Metrics Band
Live numerical metrics proving the impact of Harborline in millions of tons offset, guests served, and average transit time.

Section 11: Case Study Spotlight
An editorial layout focusing on a specific luxury line transitioning to Harborline operations.

Section 12: Accordion Specification & Compliance Detail
Expandable details covering maritime regulatory compliance, data security, and API integrations.

Section 13: Immersive Pre-Footer "Join the Atlas"
A massive emotional CTA with intersecting ambient orbs and a beautiful glass submission form.

Section 14: Luxury Terminal Footer
A deeply structured footer featuring site map, regulatory disclosures, global offices, and brand insignia.

Interactivity & JS Requirements:
- NO PLACEHOLDERS. Fill all 12+ sections with real, compelling maritime operations text.
- Wire all interactions with real JS inside `<script>`.
- Interactive Departure Board (auto-updating times or cycling statuses).
- Terminal Map tab system (click SVG zones to change active panel content).
- Accordions in Section 12 must naturally open/close with smooth height transitions.
- Count-Up Metrics must trigger via IntersectionObserver when entering viewport.
- Include a sleek "Toast" notification (e.g., successful CTA submission or simulating a system alert).
- Glass elements must have hover states (glow enhancements, slight scale).
- Ambient background orbs should drift smoothly via CSS keyframes.

Overall length:
The resulting `index.html` must be pristine, extensive (>600 lines), and a masterclass in modern, sophisticated UI design combining deep maritime aesthetics with premium glassmorphism.

