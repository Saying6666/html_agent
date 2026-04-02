## Round 1

You are acting as a lead design engineer for a flagship product launch.
Create a one-page website for **NeuroDesign Studio**.
NeuroDesign Studio is an AI-assisted interface design environment for advanced teams.
The page should feel premium, modern, and unmistakably intentional.
The page must resemble a real 2025-2026 product site.
The page must avoid generic startup template patterns.
The page must avoid repetitive hero-feature-pricing skeletons.

Audience:
- design systems leads
- product designers
- frontend architects
- design tooling buyers

Primary page objective:
- communicate why NeuroDesign Studio is category-defining
- demonstrate trust through concrete capability framing
- drive qualified users to request early access

Visual direction:
- modern premium glassmorphism and glow UI
- high-contrast dark canvas with controlled luminous edges
- frosted layered surfaces and engineered micro-depth
- expressive display typography paired with precise UI body type

Hard output constraints:
- produce exactly one complete `index.html`
- keep all CSS in a single `<style>` block
- keep all JavaScript in a single `<script>` block
- no React, Vue, Svelte, jQuery, GSAP, or Tailwind CDN
- no external JavaScript libraries
- no local assets
- avoid external images; rely on inline SVG and CSS constructs
- do not use `style=""` inline attributes in markup
- keep output readable and maintainable

Define and apply a full token system under `:root`:
- background tiers
- glass surface tiers
- border and divider colors
- text hierarchy colors
- accent palette
- semantic status palette
- spacing tokens
- radius tokens
- shadow tokens
- blur tokens
- motion duration tokens
- motion easing tokens
- content width and section rhythm tokens

Required structure and coverage:
- at least 12 substantial sections or modules
- include at least one full-bleed section
- include at least one asymmetrical layout
- include at least one dense tooling panel
- avoid repeating identical card grids

Required sections:
- sticky nav with status chip and CTA
- hero with sharp value proposition and dual actions
- proof strip with customer-grade trust markers
- interactive product canvas module
- feature matrix with meaningful grouping
- workflow timeline from idea to shipped UI
- metrics section with evidence framing
- compatibility and integrations section
- case spotlight or user quote section
- governance and reliability FAQ
- final request-access module
- detailed footer with policies and legal links

Hero expectations:
- impactful headline tied to speed and quality of interface creation
- supporting copy with clear utility and outcomes
- primary and secondary CTA with distinct intent
- hero visual that signals tool intelligence, not generic decoration

Copy requirements:
- concrete and product-specific wording
- no empty hype language
- no placeholder text
- no impossible performance promises
- maintain a professional product tone

Information architecture:
- start with category problem and thesis
- move into product mechanics
- then provide trust and outcomes
- end with clear conversion path

## Round 2

Implement at least 8 meaningful interactions with vanilla JavaScript.
You must include these interaction families:
- modal
- accordion
- toast
- tabs
- scroll reveal
- stagger animation
- count-up metrics
- navbar transition on scroll

Interaction mapping requirements:
- modal opens from both hero and lower-page CTA
- modal supports Escape and focus management
- accordion answers objections around reliability, data, and rollout
- toast confirms a real event such as request submission
- tabs switch between concrete product views
- scroll reveal animates section entrances consistently
- stagger animates grouped feature or timeline items
- count-up activates when metrics enter viewport
- navbar transitions to compact state with scroll

Add at least 3 extra tool-specific interactions:
- component density toggle
- mode switch for drafting vs production
- timeline filter for design stage

State design requirements:
- explicit default state for all controls
- explicit hover state
- explicit active state
- explicit focus-visible state
- state changes must include depth, border, or motion cues

Form behavior requirements:
- all inputs use descriptive labels
- invalid states provide clear inline guidance
- successful submit triggers toast confirmation
- loading and disabled states are distinct

Motion requirements:
- use smooth cubic-bezier timing
- keep motion purposeful and restrained
- avoid ornamental noise animations
- align transitions with information flow

Interaction quality:
- no dead controls
- no fake toggles
- no interactions requiring missing dependencies

## Round 3

Implement responsive behavior at four breakpoints:
- 1440px and above
- 1024px to 1439px
- 768px to 1023px
- below 768px

Responsive requirements:
- preserve narrative order and comprehension
- recompose at least two major modules for smaller screens
- avoid collapsing into repetitive stacked cards
- keep CTAs visible and discoverable
- maintain balanced spacing and readable text widths

Accessibility requirements:
- semantic landmarks throughout the page
- valid heading hierarchy
- ARIA support for modal, tabs, accordion, and toast
- accessible labels for all form controls
- `aria-label` on icon-only controls
- full keyboard support for interactions
- visible focus indicators
- strong contrast in text and UI controls
- do not rely on color alone for state changes

Reduced motion requirements:
- support `prefers-reduced-motion`
- reduce non-essential animation in reduced mode
- keep interactions understandable without movement
- allow count-ups to resolve immediately when needed

Performance requirements:
- avoid expensive continuous repaints
- use transform and opacity strategically for animation
- keep scripting modular and readable
- avoid unnecessary DOM churn

Technical integrity checks:
- single-file output only
- no broken tags
- no malformed script blocks
- no placeholder comments
- no inline style attributes in elements

## Round 4

Final polish requirements:
- align typography and spacing rhythm across all sections
- refine glass surfaces to avoid muddy layering
- ensure accent glows support hierarchy, not clutter
- remove visual repetition that weakens differentiation
- check that key modules feel product-specific and ownable

Final acceptance checklist:
- one complete self-contained `index.html`
- all CSS in `<style>`
- all JS in `<script>`
- no framework runtime dependencies
- at least 12 substantial modules
- all required interactions implemented and working
- responsive behavior complete across four breakpoints
- accessibility requirements covered
- reduced-motion behavior covered
- no placeholder text or filler comments

Differentiation checks:
- first viewport should clearly signal AI-native design tooling
- mid-page modules should not look like generic SaaS cards
- workflow and metrics should feel like real product evidence
- final conversion section should feel credible for enterprise evaluation

Output instruction:
- return only the final code for a single `index.html`

GENERATE THE FINAL CODE NOW
