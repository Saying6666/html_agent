    ## Round 1

    Create a production-grade 2025-2026 single-page website for **Brink Protocol**, an incident-readiness and continuity platform for infrastructure, logistics, and public-service teams. The page must feel like a real product or hospitality launch from 2025-2026, not a classroom demo and not a generic premium landing page.

    Audience:
    - logistics operators, infrastructure teams, and continuity planners
    - people who need to understand the offer quickly and trust the page enough to request access, book, or schedule a briefing

    This case must commit to a specific visual world:
    **runbook binder + signal tape**.

    This visual world is not a moodboard garnish.
    It must control:
    - palette
    - material language
    - typography pairing
    - chapter silhouette
    - interaction styling
    - motion grammar

    Structural mandate for this case:
    **Runbook Index + Drill Simulator**.

    Signature device that must be obvious in the first viewport or first major chapter:
    a drill simulator that changes the readiness plan summary, response tree, and alert strips through scenario inputs.

    Core technical constraints (non-negotiable):
    - Return one complete self-contained `index.html`
    - Single-file only
    - All CSS inside `<style>`
    - All JavaScript inside `<script>`
    - Inline CSS and inline JS only
    - No React, Vue, Svelte, jQuery, GSAP, Tailwind CDN, or external frameworks
    - No external libraries and no build step
    - Do not reference local images, local fonts, local CSS, or local JS
    - Prefer gradients, pure CSS texture, inline SVG, and built-in browser capabilities over stock media
    - Do not use `style=""` inline styles in markup

    Design system requirement:
    Define a complete CSS `:root` token system for:
    - background layers
    - surface tiers
    - border and separator tones
    - text hierarchy
    - muted copy and label text
    - accent, accent-soft, accent-strong
    - semantic states (success, warning, danger)
    - focus ring
    - radii
    - shadow system
    - spacing scale
    - content width and section padding
    - type scale
    - motion tokens (durations and easings)

    Material and composition rules:
    - Avoid the repeated batch-wide "dark glass dashboard" answer
    - Avoid purple startup gradients
    - Avoid hero-plus-three-cards startup layout
    - Avoid one repeated card container copied through the whole page
    - At least 3 major chapters must use different structural logic
    - At least 2 chapters must avoid card-grid logic entirely
    - At least 1 major module must break the normal centered-container pattern

    Content coverage.
    Treat this as ingredients rather than a literal HTML skeleton.
    You may merge, split, rename, reorder, or reinterpret sections if the result becomes more distinctive.

    Required content territory to cover somewhere in the page:
    - runbook cover
- index rail
- drill simulator
- field system overview
- response tree
- metrics
- case drill
- comparison runbook
- FAQ
- pilot modal
    - sticky masthead / nav with live status and primary CTA
    - opening thesis scene that feels specific to this case
    - proof / credibility strip with believable signals
    - a major interactive core module tied to the signature device
    - quantified outcomes presented as instrumentation, ledger, or evidence rather than vanity tiles
    - FAQ / objections handled with specific language
    - a final conversion area with a real form and clear next step
    - footer / appendix with governance, policy, provenance, contact, or credits

    Copy direction:
    - concise, specific, operationally believable
    - no empty AI hype
    - no fake luxury filler
    - use terminology that belongs to this domain
    - make the service or product sound bookable, procurable, or deployable

    Chapter pressure:
    - the first viewport must be unmistakably tied to Brink Protocol
    - the silhouette must not read like hero + features + metrics + FAQ + CTA
    - the signature device must matter to the narrative, not sit there as decoration

    ## Round 2

    Implement at least 8 meaningful interactions and explicitly include all of the following:
    1. **Modal**
    2. **Accordion**
    3. **Toast**
    4. **Tabs**
    5. **Scroll reveal**
    6. **Stagger animation**
    7. **Count-up**
    8. **Navbar scroll transition**

    These interactions must be real working behavior, not decorative placeholders.
    They must be styled to fit runbook binder + signal tape, not generic component-library UI.

    Required interaction mapping:
    - **Modal** must open from multiple CTAs and contain a credible request / booking / briefing flow
    - **Accordion** must handle FAQ, policy, governance, or protocol notes with clear expanded state
    - **Toast** must confirm a meaningful action and be announced through an `aria-live` region
    - **Tabs** must materially change a narrative block, stage, board, calendar, dial, map, or call sheet
    - **Scroll reveal** must use one authored reveal grammar instead of the same fade-up everywhere
    - **Stagger animation** must apply to rows, cues, nodes, evidence, itinerary items, or steps specific to this case
    - **Count-up** must activate when visible and be tied to believable product or hospitality metrics
    - **Navbar scroll transition** must change density, spacing, and utility emphasis after scrolling

    Add at least 3 extra case-specific behaviors:
    - severity selector
- role filter chips
- save plan toast
    - at least one extra interaction must change content depth or chapter state, not just style

    State design requirements:
    - Define strong Default / Hover / Active / Focus states for buttons, links, tabs, chips, toggles, form fields, accordion triggers, modal controls, and key interactive objects
    - State changes must alter more than color: use weight, border, crop, depth, underline, marker, or panel treatment
    - Focus states must be visible, high-contrast, and consistent

    Motion direction:
    - motion must feel authored for this case, not generic app polish
    - do not rely only on opacity + translate
    - keep motion performant and readable
    - ensure the motion language matches the structural mandate `Runbook Index + Drill Simulator`

    Interaction quality bar:
    - at least 2 interactions must materially change navigation, reading order, content depth, or the main stage/device
    - no dead controls
    - no fake toggles
    - no ornamental-only flagship interaction

    ## Round 3

    Make the page responsive across 4 breakpoints:
    - `>= 1440px`: expansive desktop with the full Runbook Index + Drill Simulator silhouette intact
    - `1024px - 1439px`: refined desktop / laptop with tighter spacing and preserved hierarchy
    - `768px - 1023px`: tablet with recomposed modules and touch-first controls
    - `< 768px`: mobile that still reads as this specific case rather than a generic product page

    Responsive requirements:
    - mobile must not collapse into one centered max-width stack of repeated cards
    - at least 2 major modules should genuinely change form between desktop and mobile
    - at least 1 bold gesture should survive below 768px
    - turn the binder into indexed run cards with a pinned simulator summary instead of card grids

    Accessibility requirements:
    - semantic landmarks using `header`, `nav`, `main`, `section`, and `footer`
    - correct heading hierarchy
    - ARIA for modal, tabs, accordion, toast, and any live status labels
    - accessible names for all form controls
    - `aria-label` for icon-only buttons
    - keyboard support for modal, tabs, accordion, and major controls
    - Escape closes modal
    - visible focus states throughout
    - support `prefers-reduced-motion`
    - do not rely on color alone for state, selection, alert, or expanded state
    - maintain strong contrast

    Reduced motion requirements:
    - reduce or remove nonessential reveal and stagger motion
    - allow counters to snap to final values if needed
    - keep state changes legible without animation
    - preserve the main information hierarchy

    Technical constraints remain strict:
    - single-file `index.html`
    - inline CSS and inline JavaScript only
    - no frameworks
    - no local assets
    - no `style=""` inline styles
    - if `backdrop-filter` is used, include `-webkit-backdrop-filter` before `backdrop-filter`
    - final HTML must be normal multi-line, readable, and maintainable rather than compressed

    ## Round 4

    Polish until the result feels launch-ready and unmistakably specific to **Brink Protocol**.
    Tighten spacing rhythm, border logic, chapter transitions, state styling, and information density so every region belongs to one system.

    Final quality checklist:
    - one complete self-contained `index.html`
    - all CSS in `<style>` and all JavaScript in `<script>`
    - no frameworks, no external libraries, no local assets, no `style=""`
    - complete CSS `:root` token system used consistently
    - at least 10 meaningful sections or blocks
    - required interactions fully implemented: modal, accordion, toast, tabs, scroll reveal, stagger animation, count-up, navbar scroll transition
    - extra interactions included and useful
    - responsive behavior works across all 4 breakpoints
    - accessibility, keyboard support, and reduced-motion handling are careful and complete
    - the signature device remains central to the experience

    Final differentiation test:
    - if the first viewport could belong to another case in this batch, redesign it
    - if the wireframe still resembles a standard product landing page skeleton, redesign it
    - if the signature device feels decorative rather than structural, redesign it
    - if more than 2 major regions rely on the same container rhythm, redesign them
    - if the page can be mistaken for a dark dashboard, a glassmorphism landing page, or a generic editorial SaaS homepage, redesign it

    Return only the final code contained in one `index.html`.

    GENERATE THE FINAL CODE NOW
