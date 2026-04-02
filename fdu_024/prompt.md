## Round 1

You are a principal product designer and frontend engineer.
Create a launch-grade single page for **Lumen Trench Cloud**.
Lumen Trench Cloud is a deep-ocean data and routing platform for autonomous submersibles.
The visual language must feel premium, technical, and editorial.
The page must look like a real product site from 2025-2026.
The page must not look like a classroom demo.
The page must not look like a generic startup template.

Primary audience:
- robotics CTOs
- marine infrastructure operators
- subsea research labs
- compliance and risk teams

Primary outcome:
- help a visitor understand the product quickly
- communicate trust and technical depth
- move qualified teams to request a live mission review

Design direction:
- modern premium glassmorphism and glow UI
- deep-water darkness with restrained luminous accents
- layered frosted surfaces over atmospheric gradients
- precise typography with clear information hierarchy

Hard technical rules:
- output exactly one complete `index.html`
- include all CSS inside one `<style>` block
- include all JavaScript inside one `<script>` block
- do not use React, Vue, Svelte, jQuery, GSAP, or Tailwind CDN
- do not use local assets
- do not use external JavaScript libraries
- if imagery is needed, use inline SVG and CSS gradients
- do not use `style=""` attributes in markup
- final code must be readable, multi-line, and maintainable

Define a full token system in `:root`:
- background tiers
- surface tiers
- border and separator colors
- primary and secondary text colors
- accent colors
- semantic status colors
- spacing scale
- radius scale
- shadow scale
- blur strengths
- transition durations
- easing functions
- content width limits
- section paddings

Content and layout requirements:
- build at least 12 meaningful sections
- each section must have a distinct structure
- avoid repeating one card style everywhere
- include both data-dense and editorial sections
- at least one section must break the centered container rhythm

Required section coverage:
- sticky mission navbar
- hero with mission statement and two CTAs
- trust strip with partner-grade proof points
- live trench dashboard module
- mission timeline module
- autonomous fleet map module
- anomaly response playbook
- metrics with instrumentation framing
- use-case matrix by operator type
- customer quote or field report section
- compliance and data governance FAQ
- final conversion section with form
- detailed footer with policy links and contacts

Hero expectations:
- strong headline tied to subsea intelligence
- concise subheadline with concrete value
- one primary CTA and one secondary CTA
- atmospheric background with soft motion
- visual focal point that cannot be mistaken for another case

Copy requirements:
- use specific language
- avoid vague hype
- avoid filler adjectives
- avoid fake or impossible claims
- ensure terminology matches marine operations context

Information architecture requirements:
- progress from mission context to system capabilities
- then move to evidence and operational trust
- then close with implementation path and conversion

Quality constraints:
- no placeholders
- no unfinished notes
- no omitted blocks
- no fake controls
- no dead links disguised as interactions

## Round 2

Implement at least 8 meaningful interactions with real JavaScript logic.
You must include all of the following interaction types:
- modal
- accordion
- toast
- tabs
- scroll reveal
- stagger animation
- count-up numbers
- navbar transition on scroll

Interaction mapping requirements:
- modal opens from at least two CTAs
- modal supports keyboard close with Escape
- modal includes a believable request flow
- accordion is used for compliance or policy details
- toast confirms a real action
- tabs switch mission contexts or operator views
- scroll reveal is applied to major section entrances
- stagger applies to lists, not random decorative elements
- count-up starts when metrics become visible
- navbar compacts or changes glass density after scroll

Add at least 3 additional case-specific interactions:
- anomaly severity filter chips
- fleet status toggles
- mission window selector

State design requirements:
- define clear default states
- define clear hover states
- define clear active states
- define clear focus-visible states
- state changes must involve more than color only
- include border, shadow, transform, or content changes where appropriate

Form behavior requirements:
- validate required fields
- show inline feedback for invalid entries
- submit path triggers a toast
- ensure labels are present and explicit

Motion direction:
- motion should feel precise and instrument-like
- avoid gimmicky bouncing
- avoid excessive looping distractions
- prioritize smooth transitions with cubic-bezier easing
- ensure motion supports comprehension rather than decoration

Interaction reliability:
- controls must be clickable and testable
- no non-functional demo controls
- no hidden logic dependencies on external libraries

## Round 3

Build responsive behavior across four breakpoints:
- desktop wide: 1440px and above
- desktop standard: 1024px to 1439px
- tablet: 768px to 1023px
- mobile: below 768px

Responsive requirements:
- preserve narrative structure at all sizes
- avoid collapsing everything into identical stacked cards
- ensure at least two major modules materially reflow on mobile
- keep hero impact and mission clarity on small screens
- maintain readable line lengths and spacing rhythm

Accessibility requirements:
- use semantic landmarks: `header`, `nav`, `main`, `section`, `footer`
- maintain a valid heading hierarchy
- provide ARIA attributes for modal, tabs, accordion, and toast
- provide accessible names for all inputs
- provide `aria-label` for icon-only buttons
- ensure keyboard navigation for all major interactions
- ensure visible focus outlines
- ensure adequate color contrast
- ensure status and state are not conveyed by color alone

Reduced motion requirements:
- support `prefers-reduced-motion`
- minimize or remove non-essential animation in reduced mode
- keep interactions understandable without motion
- allow count-up values to snap to final values if needed

Performance and robustness:
- avoid expensive continuous layout thrashing
- keep animation properties GPU-friendly where possible
- avoid giant unbounded shadows that hurt readability
- keep JS modular and readable

Technical integrity checks:
- keep everything in one HTML file
- no broken closing tags
- no malformed scripts
- no inline style attributes in HTML elements

## Round 4

Polish pass requirements:
- tighten spacing consistency across sections
- align typography scale with hierarchy intent
- refine glass layering so panels feel physically coherent
- ensure accent usage is intentional and limited
- remove any repetitive visual motifs that feel templated

Final acceptance checklist:
- one complete `index.html`
- all CSS in `<style>`
- all JS in `<script>`
- no external framework runtime
- no placeholder comments or text
- at least 12 meaningful sections
- all required interactions implemented
- responsive behavior validated across four breakpoints
- accessibility requirements covered
- reduced motion behavior covered

Differentiation checks:
- first screen should clearly communicate subsea mission intelligence
- main modules should not mirror generic SaaS hero-feature-pricing flow
- data modules should look purpose-built, not copied dashboard tiles
- conversion area should feel like a real enterprise handoff

Output requirements:
- return only the final code
- return code only for one single `index.html`

GENERATE THE FINAL CODE NOW
