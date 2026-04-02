## Round 1

You are a senior web product designer and implementation engineer.
Build a premium single-page website for **Harbor Pulse Grid**.
Harbor Pulse Grid coordinates shore power, berth timing, and electric fleet charging windows.
The page must look like a real, funded product launch.
The page must feel current with top-tier 2025-2026 product design.
The page must not read like a generic marketing template.
The page must not look like a dashboard pasted into a landing page.

Audience:
- marina operations directors
- electric fleet managers
- port modernization teams
- energy scheduling analysts

Business goal:
- communicate strategic value in under one minute
- show operational depth and credibility
- drive visitors to schedule a technical briefing

Visual direction:
- modern premium glassmorphism and glow UI
- dark maritime base with precise luminous accents
- frosted control surfaces with layered atmospheric lighting
- strong typographic hierarchy with measured contrast

Hard constraints:
- output a single complete `index.html`
- include all CSS in one `<style>` block
- include all JS in one `<script>` block
- no React, Vue, Svelte, jQuery, GSAP, Tailwind CDN, or similar frameworks
- no external JavaScript dependencies
- no local asset references
- avoid external imagery; prefer inline SVG and CSS graphics
- do not use `style=""` inline attributes in markup
- deliver readable and maintainable multi-line code

Define and use a robust `:root` design token system:
- base background palette
- glass surface palette
- border and separator tones
- text hierarchy colors
- accent and accent-strong colors
- semantic state colors
- spacing scale
- radius scale
- shadow scale
- blur scale
- animation durations
- animation easings
- section width and padding constraints

Required page structure:
- at least 12 sections or deep functional blocks
- each major block must have a distinct layout strategy
- at least one full-bleed section
- at least one section with high information density
- at least one section with narrative editorial pacing

Mandatory content areas:
- sticky utility nav with live status indicator
- hero thesis with two clear CTAs
- trust and signal strip
- berth-energy scheduling board
- charging corridor map with zone switching
- fleet readiness timeline
- energy anomaly response panel
- measurable outcomes module
- multi-role use-case section
- testimonial or operator field note
- compliance FAQ and policy details
- final conversion form and onboarding path
- governance-heavy footer

Hero requirements:
- immediate statement of electric port orchestration value
- concise supporting copy with operational language
- CTA labels that sound enterprise-ready
- visual centerpiece linked to scheduling intelligence

Content rules:
- specific and believable wording
- no shallow buzzword copy
- no placeholder copy
- no fake impossible metrics
- no irrelevant filler

Information flow:
- open with mission context
- progress to system capabilities
- then show evidence and outcomes
- close with implementation and next steps

## Round 2

Implement at least 8 meaningful interactions using vanilla JavaScript.
You must include:
- modal
- accordion
- toast
- tabs
- scroll reveal
- stagger animation
- count-up metrics
- navbar transition on scroll

Interaction behavior requirements:
- modal opens from both hero and final CTA
- modal supports Escape and focus trapping
- accordion is used for compliance and deployment concerns
- toast confirms a concrete action such as form submission
- tabs switch board views such as berth, power, and crew readiness
- scroll reveal introduces major sections with consistent grammar
- stagger animates grouped items with intentional sequence
- count-up activates on viewport entry and runs once
- navbar transitions density and spacing after scrolling

Add at least 3 additional domain-specific interactions:
- berth priority filter chips
- charging load threshold toggle
- schedule horizon selector

State design requirements:
- explicit default, hover, active, and focus-visible states
- focus states must be obvious and high-contrast
- state changes must alter shape, depth, or motion, not color only

Form interaction requirements:
- all fields have clear labels
- invalid inputs produce inline guidance
- successful submit triggers toast confirmation
- button disabled state is visually and semantically clear

Motion requirements:
- smooth cubic-bezier transitions
- subtle and intentional movement
- avoid decorative over-animation
- ensure motion supports clarity and hierarchy

Interaction integrity:
- no dead controls
- no fake toggle states
- no interactions that require missing external scripts

## Round 3

Build responsive behavior for four breakpoints:
- 1440px and above
- 1024px to 1439px
- 768px to 1023px
- below 768px

Responsive quality requirements:
- preserve core narrative in all sizes
- avoid repetitive stacked-card monotony on mobile
- recompose at least two major modules on tablet and mobile
- keep primary CTA discoverable without hunting
- maintain readable line lengths and spacing cadence

Accessibility requirements:
- semantic landmarks throughout
- correct heading hierarchy
- ARIA attributes for modal, tabs, accordion, and toast
- descriptive labels for every form control
- `aria-label` for icon-only buttons
- complete keyboard navigation for key interactions
- visible focus treatment in all states
- adequate text and UI contrast ratios
- state and status not color-only

Reduced motion requirements:
- support `prefers-reduced-motion`
- simplify non-essential transitions
- keep feature understanding intact without animation
- allow metrics to display final values immediately in reduced mode

Performance and reliability:
- avoid unnecessary heavy paint effects
- prefer transform and opacity for motion where suitable
- keep JS readable and modular
- ensure no malformed DOM or script fragments

Technical guardrails:
- single-file output only
- no broken tags
- no placeholder fragments
- no inline style attributes in elements

## Round 4

Polish and verification phase:
- tighten visual rhythm and vertical spacing
- ensure typographic hierarchy remains clear in every section
- refine glass layering to avoid muddy surfaces
- use glow accents sparingly and intentionally
- remove repeated motif patterns that make the page generic

Final acceptance checklist:
- complete self-contained `index.html`
- all CSS in `<style>`
- all JS in `<script>`
- no framework runtime dependencies
- no placeholder text or comments
- at least 12 substantial content blocks
- all required interactions implemented and functional
- four-breakpoint responsive behavior complete
- accessibility and reduced-motion handling complete

Differentiation checks:
- first viewport clearly expresses electric harbor orchestration
- no standard hero-feature-pricing clone silhouette
- operational modules look purpose-built for this domain
- conversion area feels like a real enterprise workflow

Output instruction:
- return only final code for one complete `index.html`

GENERATE THE FINAL CODE NOW
