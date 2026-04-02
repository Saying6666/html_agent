## Round 1

You are a staff-level product designer and frontend engineer.
Create a premium single-page launch site for **Vectorlight Command**.
Vectorlight Command is a realtime decision surface for distributed operations teams.
The site should look like a real enterprise product launch from 2025-2026.
The site should feel distinct, intentional, and high craft.
The site must avoid generic SaaS page formulas.
The site must avoid repetitive visual blocks that feel templated.

Audience:
- operations leaders
- incident command managers
- program directors
- technical buyers evaluating platform rollout

Primary objective:
- explain value and workflow in minutes
- establish trust through concrete implementation detail
- convert qualified teams into briefing requests

Visual direction:
- modern premium glassmorphism and glow UI
- deep neutral base with controlled spectral accents
- layered frosted surfaces with precise edge treatment
- confident typography with clear hierarchy

Hard technical constraints:
- output one complete `index.html` file
- all CSS must be inside one `<style>` block
- all JavaScript must be inside one `<script>` block
- do not use React, Vue, Svelte, jQuery, GSAP, or Tailwind CDN
- do not use any external JavaScript library
- do not reference local files
- avoid external images; use inline SVG and CSS graphics
- do not use `style=""` inline attributes in markup
- final output must be readable and maintainable

Define and apply a complete `:root` token system:
- base backgrounds
- glass surfaces
- border and divider tones
- primary and muted text colors
- accent and alert colors
- semantic success/warning/error colors
- spacing scale
- radius scale
- shadow scale
- blur scale
- motion duration scale
- motion easing scale
- section width and padding scale

Required composition:
- minimum 12 substantial sections or modules
- at least one full-bleed storytelling section
- at least one data-dense operational section
- at least one asymmetrical section
- avoid a repeated card grid as the whole page language

Required content modules:
- sticky command navbar with live status chip
- hero thesis with two clear CTAs
- trust and deployment signal strip
- command board preview module
- orchestration timeline module
- region and squad coverage map module
- incident protocol module
- measurable outcomes module
- role-based workflow section
- field report or customer quote section
- governance and compliance FAQ
- conversion form module
- detailed footer with legal and contact blocks

Hero requirements:
- headline that clearly frames command and coordination value
- concise supporting copy with operational specificity
- one primary CTA and one secondary CTA
- visual center tied to command-state intelligence

Copy requirements:
- concrete, domain-relevant language
- no vague hype phrases
- no placeholder text
- no impossible claims
- no empty filler lines

Information architecture:
- start with mission context and pain
- move into product mechanics
- then provide evidence and trust
- finish with implementation and conversion

## Round 2

Implement at least 8 meaningful interactions using vanilla JavaScript.
You must include all of these:
- modal
- accordion
- toast
- tabs
- scroll reveal
- stagger animation
- count-up
- navbar transition on scroll

Interaction mapping requirements:
- modal opens from both hero and final CTA
- modal supports Escape close and focus handling
- accordion is used for governance and rollout concerns
- toast confirms a real submission or action
- tabs switch command views with meaningful content change
- scroll reveal introduces section groups with consistent pattern
- stagger animates grouped list items
- count-up starts on viewport entry and runs once
- navbar transitions compactness and surface on scroll

Add at least 3 domain-specific interactions:
- severity filter controls
- response mode switch
- region focus selector

State design requirements:
- explicit default state for all key controls
- explicit hover state
- explicit active state
- explicit focus-visible state
- state transitions should include depth or motion, not color only

Form behavior requirements:
- all fields have accessible labels
- inline validation messages are clear and actionable
- successful submit triggers toast confirmation
- disabled/loading states are visibly distinct

Motion requirements:
- smooth cubic-bezier timing
- avoid noisy decorative loops
- motion should reinforce reading and control feedback
- transitions should remain performant and consistent

Interaction quality requirements:
- no dead buttons
- no fake toggles
- no orphaned UI without logic

## Round 3

Implement responsive behavior for four breakpoints:
- 1440px and above
- 1024px to 1439px
- 768px to 1023px
- below 768px

Responsive requirements:
- preserve narrative intent on all breakpoints
- recompose at least two major modules on smaller screens
- avoid turning the page into repetitive stacked cards
- keep CTA hierarchy clear on mobile
- maintain readable line lengths and spacing

Accessibility requirements:
- use semantic landmarks throughout
- maintain proper heading hierarchy
- provide ARIA support for modal, tabs, accordion, and toast
- ensure all form controls have accessible names
- provide `aria-label` for icon-only controls
- support full keyboard navigation for major interactions
- provide visible focus indicators
- maintain adequate contrast for text and controls
- avoid color-only state communication

Reduced motion requirements:
- support `prefers-reduced-motion`
- reduce non-essential animations in reduced mode
- keep interaction clarity without motion
- allow count-up values to resolve immediately when reduced mode is active

Performance requirements:
- avoid continuous expensive repaint effects
- prefer transform and opacity where appropriate
- keep JavaScript modular and easy to follow
- avoid unnecessary event listener overhead

Technical integrity requirements:
- keep output as a single HTML file
- ensure no malformed tags
- ensure scripts close correctly
- avoid placeholder comments
- avoid inline style attributes in markup

## Round 4

Final polish requirements:
- tighten spacing and alignment across all modules
- verify typography hierarchy from hero to footer
- refine glass layering for legibility and depth
- keep glow accents strategic, not overwhelming
- remove any sections that feel duplicate or generic

Final acceptance checklist:
- one complete self-contained `index.html`
- all CSS in `<style>`
- all JS in `<script>`
- no framework runtime dependencies
- at least 12 meaningful modules
- all required interactions implemented and functional
- responsive behavior complete across all four breakpoints
- accessibility requirements covered
- reduced-motion behavior covered
- no placeholder copy or filler notes

Differentiation checks:
- first viewport should clearly signal command and response context
- mid-page modules should resemble real operational interfaces
- proof and metrics should read as credible evidence
- final conversion should feel like a realistic enterprise next step

Output instruction:
- return only final code for one complete `index.html`

GENERATE THE FINAL CODE NOW
