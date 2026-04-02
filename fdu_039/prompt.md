## Round 1

You are a principal product designer and frontend implementation lead.
Create a launch-ready single-page site for **AuraStack**.
AuraStack is an orchestration platform for AI-native workflow infrastructure.
The page must feel polished, premium, and technically credible.
The page must read like a real 2025-2026 software launch.
The page must avoid generic startup page patterns.
The page must avoid repetitive and interchangeable section styling.

Audience:
- platform engineering leads
- automation architects
- CTO office stakeholders
- enterprise implementation teams

Primary business objective:
- explain AuraStack value and architecture quickly
- build trust through concrete product mechanics
- drive qualified demos and implementation calls

Visual direction:
- modern premium glassmorphism and glow UI
- dark atmospheric background with restrained luminous accents
- frosted panels, layered depth, and precise border treatment
- typography that balances editorial impact and UI readability

Hard technical constraints:
- output exactly one complete `index.html`
- put all CSS in one `<style>` block
- put all JavaScript in one `<script>` block
- no React, Vue, Svelte, jQuery, GSAP, Tailwind CDN, or equivalent
- no external JavaScript dependencies
- no local asset references
- prefer inline SVG and CSS graphics over external images
- do not use `style=""` inline attributes in markup
- final code must be readable and maintainable

Define and use a full `:root` token system:
- background layers
- surface layers
- border and separator tokens
- text hierarchy tokens
- accent and accent-strong tokens
- semantic status tokens
- spacing scale
- radius scale
- shadow scale
- blur scale
- duration scale
- easing scale
- section width and rhythm tokens

Required page composition:
- minimum 12 meaningful sections or modules
- at least one full-bleed narrative section
- at least one high-density operations section
- at least one asymmetrical layout section
- avoid repeating one card recipe throughout

Required content blocks:
- sticky utility nav
- hero with strong thesis and two CTAs
- trust strip with customer-grade signals
- orchestration control module
- pipeline stage map
- reliability and uptime evidence module
- integration ecosystem module
- role-based outcomes section
- operator quote or case snapshot
- governance and security FAQ
- final conversion form
- detailed legal and contact footer

Hero section requirements:
- distinctive headline tied to orchestration intelligence
- concise and concrete supporting copy
- two clearly differentiated CTAs
- visual focal element that reinforces product mechanics

Copy quality requirements:
- specific and believable
- no vague hype stacks
- no placeholder text
- no impossible claims
- no generic filler

Information flow requirements:
- begin with pain and thesis
- move into product operation model
- then provide trust and proof
- end with implementation and conversion

## Round 2

Implement at least 8 meaningful interactions using vanilla JavaScript.
You must include:
- modal
- accordion
- toast
- tabs
- scroll reveal
- stagger animation
- count-up
- navbar transition on scroll

Interaction mapping requirements:
- modal opens from top and bottom conversion CTAs
- modal supports Escape and focus handling
- accordion presents governance and security answers
- toast confirms meaningful user action
- tabs switch between orchestration views or roles
- scroll reveal introduces major section groups
- stagger animates grouped items intentionally
- count-up triggers once when metrics enter viewport
- navbar compresses and changes surface treatment on scroll

Add at least 3 product-specific interactions:
- workflow complexity filter
- deployment mode switch
- region visibility toggle

State design requirements:
- explicit default states
- explicit hover states
- explicit active states
- explicit focus-visible states
- states must alter depth, shape, or movement in addition to color

Form behavior requirements:
- clear labels for every field
- inline validation guidance
- meaningful success feedback via toast
- visible disabled and loading states

Motion requirements:
- smooth cubic-bezier timing
- avoid excessive decorative motion
- keep transitions tied to hierarchy and readability
- ensure interaction feedback is immediate and clear

Interaction integrity requirements:
- no dead controls
- no fake toggles
- no missing event bindings

## Round 3

Implement responsive behavior at four breakpoints:
- 1440px and above
- 1024px to 1439px
- 768px to 1023px
- below 768px

Responsive behavior requirements:
- preserve narrative order and understanding
- recompose at least two major modules on tablet or mobile
- avoid repetitive one-column card walls
- keep key CTAs discoverable and legible
- maintain spacing rhythm and text readability

Accessibility requirements:
- semantic landmarks across the page
- coherent heading hierarchy
- ARIA patterns for modal, tabs, accordion, and toast
- accessible labels for all form controls
- `aria-label` for icon-only controls
- keyboard support for all major interactions
- visible focus indicators
- sufficient contrast for text and controls
- no color-only state communication

Reduced motion requirements:
- support `prefers-reduced-motion`
- reduce or remove non-essential animation
- preserve comprehension and navigation without motion
- allow count-up values to resolve immediately in reduced mode

Performance requirements:
- avoid constant expensive repaints
- favor transform and opacity where reasonable
- keep JavaScript modular and clear
- avoid unnecessary DOM churn

Technical guardrails:
- single-file output only
- no malformed HTML structure
- no broken script blocks
- no placeholder comments
- no inline style attributes

## Round 4

Final polish requirements:
- align spacing rhythm section to section
- sharpen typography hierarchy
- tune glass layers for clarity and contrast
- use glow accents deliberately and sparingly
- remove repeated motifs that make the page look generic

Final acceptance checklist:
- one complete self-contained `index.html`
- all CSS inside `<style>`
- all JS inside `<script>`
- no runtime dependency on external frameworks
- at least 12 substantial modules
- all required interactions implemented and testable
- responsive behavior complete for four breakpoints
- accessibility requirements covered
- reduced-motion behavior covered
- no placeholder text or filler notes

Differentiation checks:
- first viewport clearly communicates orchestration identity
- middle modules look like real platform workflows
- proof and metrics sections feel evidence-based
- final conversion section reads as a credible implementation handoff

Output instruction:
- return only final code for one complete `index.html`

GENERATE THE FINAL CODE NOW
