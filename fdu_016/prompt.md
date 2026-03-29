## Round 1

Document type: CAPITAL PLANNING WORKBOOK
Product: **Northstar Ledger**
Audience: portfolio owners, real-asset operators, infrastructure investors, resilience teams
Timeframe: 2025-2026
Deliverable: one self-contained single-file `index.html`

Goal statement:
Build a production-grade single-page website for Northstar Ledger.
Northstar Ledger is a climate-capital planning platform for building and infrastructure portfolios.
It helps teams move from climate exposure to funded retrofit sequencing.
The page must feel like a serious planning instrument.
It must not feel like a generic ESG dashboard.
It must not feel like a luxury landing page wearing sustainability copy.
It must read like a portfolio workbook that has been turned into a digital product.

Case-specific visual direction:
- daylight surfaces, technical paper, tinted overlays, and investment-marking color
- planning-board composition instead of floating startup blocks
- layered ledgers, asset strips, budget annotations, and sequencing rails
- clear, data-forward typography with a practical display voice
- measured motion that feels analytic, not theatrical
- no batch-wide midnight formula
- no default dark glass console
- no vague "future luxury" atmosphere standing in for structure

Layout archetype:
Use a portfolio planning wall.
The page should feel like a strategist's desk covered with asset sheets, budget tracks, and intervention markers.
One major chapter should behave like a scenario workbook.
One major chapter should behave like a capital sequencing board.
One major chapter should behave like an evidence appendix.
Do not reduce the experience to hero plus feature grid plus FAQ plus CTA.

Signature device:
Create a "retrofit ledger canvas" that becomes the recognizable centerpiece of the page.
This canvas should combine:
- asset rows
- intervention columns
- timing markers
- risk-to-capex relationships
- confidence notes
- scenario switching
Use CSS and inline SVG to make the canvas feel real.
Do not rely on stock photography to carry identity.

Design system requirements:
Define a full CSS `:root` token system.
Include tokens for:
- page background layers
- sheet surfaces
- inset surfaces
- planning accents
- neutral dividers
- text hierarchy
- muted labels
- semantic risk states
- semantic funding states
- radii
- shadows
- spacing scale
- content width
- section spacing
- type scale
- duration tokens
- easing curves
Use tokens consistently across the full page.
Avoid scattered hard-coded values.

Technical requirements:
- Return one complete self-contained `index.html`
- Single-file only
- All CSS must be inside `<style>`
- All JavaScript must be inside `<script>`
- Inline CSS and inline JS only
- Do not use React, Vue, Svelte, jQuery, GSAP, Tailwind CDN, or any external framework
- No build step
- Do not reference local images, local fonts, local CSS, or local JS
- Prefer gradients, inline SVG, CSS texture, and authored diagramming over stock-heavy art direction
- Do not use `style=""` inline styles in markup
- If `backdrop-filter` is used, include `-webkit-backdrop-filter` before `backdrop-filter`

Content coverage:
Treat the following as content ingredients, not a fixed HTML skeleton.
You may merge, split, rename, reorder, or reinterpret them.
The final composition should be more interesting than a standard marketing page.

Required content ingredients:
1. Sticky navigation with live portfolio status and a primary review CTA
2. Hero thesis that explains capital planning under climate pressure
3. Portfolio strip with asset count, risk horizon, and funded pipeline signal
4. Scenario workbook with Tabs for heat, water, power, and insurance pressure
5. Asset ledger canvas with intervention sequencing
6. Funding logic chapter showing capex, opex, incentives, and payback framing
7. Count-up proof area with quantified portfolio outcomes
8. Comparison between fragmented consultant workflow and Northstar Ledger
9. Case-study chapter with before/after planning timeline
10. FAQ and objection-handling area
11. Conversion area with request form and guided pilot framing
12. Footer appendix with legal, methodology, and model scope notes

Structure pressure:
- at least 3 major chapters must use clearly different structural logic
- at least 2 chapters must avoid card-grid logic entirely
- at least 1 chapter must break the normal max-width container
- at least 1 chapter must look like a planning instrument rather than a website section
- do not repeat identical wrapper spacing for every chapter

Copy direction:
- write like a credible portfolio planning product
- use believable nouns such as asset stack, retrofit lane, funding gap, incentive window, readiness threshold, replacement cycle, insurance pressure, and resilience budget
- avoid empty AI hype
- avoid generic sustainability slogans
- avoid filler luxury adjectives
- make numbers plausible and operational

Information hierarchy requirements:
- use compact labels and more explicit section naming than generic "features"
- show dependencies between risk, funding, and timing
- make the reader understand why sequencing matters
- expose caveats and assumptions rather than hiding them

Negative constraints:
- no hero-plus-three-cards startup layout
- no interchangeable feature farm
- no repeated glowing glass tiles
- no generic dark dashboard silhouette
- no decorative charts that do not explain a decision
- no visual effect used as a substitute for planning logic

## Round 2

Deepen the page with meaningful behavior.
Implement at least 8 real interactions.
The page must explicitly include the following capabilities.
They should feel native to the portfolio-planning concept.

Required interactions:
1. **Modal**
Use it for "Request a resilience review".
The modal should behave like a scoped planning intake sheet.
Open it from at least two different triggers.
Trap focus.
Support Escape to close.
Provide a visible close control.

2. **Accordion**
Use it for FAQ, modeling assumptions, or scope boundaries.
Expanded state must be obvious without relying on color alone.
Keyboard support must be correct.

3. **Toast**
Show a toast after form submission and after saving a scenario.
The toast should confirm that a review packet or scenario note has been logged.
Use an ARIA live region.
Auto-dismiss is allowed if it is respectful and interruptible.

4. **Tabs**
Tabs must drive the scenario workbook.
Do not make them superficial.
Switching Tabs must update:
- the scenario narrative
- at least one risk metric
- at least one planning recommendation
- at least one element inside the ledger canvas

5. **Scroll reveal**
Use Scroll reveal in a way that feels like sheets, ledgers, and planning rails entering the board.
Avoid repeating the same opacity-plus-translate on every block.
Use one coherent reveal language.

6. **Stagger animation**
Use Stagger animation for asset rows, intervention lanes, or appendix entries.
Do not waste it on a generic feature-card grid.

7. **Count-up**
Use Count-up for proof metrics such as protected asset value, avoided downtime, accelerated approvals, or identified incentive value.
Counters should feel like measured readouts, not arcade effects.

8. **Navbar scroll transition**
Use Navbar scroll transition to compress the planning masthead as the user moves deeper into the workbook.
The navigation should gain tighter spacing and stronger document-like framing after scroll.

Additional interaction requirements:
- active nav highlighting based on reading position
- portfolio filter or asset-class toggle inside the ledger canvas
- scenario save action that changes interface state, not just color
- hover feedback on controls, asset rows, comparison surfaces, and timeline markers
- lightweight client-side form validation without network requests

Narrative behavior requirements:
At least 2 interactions must change the reading path or decision state.
Examples:
- switching scenario Tabs reorders the planning emphasis
- asset filters change which interventions rise to the top
- comparison toggle reframes the sequence of evidence
Do not treat every interaction as local decoration only.

State-design requirements:
Define strong Default, Hover, Active, and Focus states for:
- buttons
- links
- tabs
- accordions
- filters
- asset rows
- form fields
State changes must affect hierarchy, contrast, border treatment, elevation, underline, crop, or spacing.
Do not rely on tiny color shifts alone.

Motion direction:
- precise
- deliberate
- analytical
- steady rather than playful
- supportive of dense information
Use motion to reveal decision structure, not to perform empty spectacle.

Form behavior:
- label every field clearly
- show inline error states
- keep success feedback specific
- make the form feel like a real pilot intake, not a generic newsletter block

## Round 3

Make the page fully responsive across 4 breakpoints.
Recompose the planning wall intelligently at each size.

Breakpoint expectations:
- `>= 1440px`
Use an expansive planning-board composition.
Keep the ledger canvas prominent.
Allow multiple planning layers to coexist without looking cramped.

- `1024px - 1439px`
Preserve the workbook feel.
Tighten spacing.
Keep the scenario area and portfolio metrics readable without collapsing into generic cards.

- `768px - 1023px`
Turn large planning surfaces into stacked instruments.
Keep Tabs touch-friendly.
Ensure the ledger remains legible as a selective slice rather than a tiny unreadable matrix.

- `< 768px`
Prioritize scenario switching, asset logic, and CTA clarity.
Mobile does not need to mimic desktop literally.
You may transform major chapters into drawers, rails, stacked sheets, annotated lists, or mini-workbooks.
At least one bold planning gesture should survive on mobile.

Responsive recomposition rules:
- at least 2 major modules must genuinely change form between desktop and mobile
- at least 1 full-bleed or overflow gesture should survive below 768px
- do not collapse the page into one centered column of identical panels
- preserve the product's planning identity from the first mobile viewport

Accessibility requirements:
- use semantic landmarks: `header`, `nav`, `main`, `section`, `footer`
- maintain a correct heading hierarchy
- provide ARIA for Modal, Tabs, Accordion, Toast, and live status
- ensure accessible names for every form control
- provide `aria-label` for icon-only buttons
- support keyboard interaction for the modal, tabs, accordion, filters, and core controls
- Escape must close the modal
- use visible focus states throughout
- support `prefers-reduced-motion`
- do not rely on color alone for state, warning, selection, or validation
- maintain strong contrast even when using subtle planning tones

Technical integrity requirements:
- keep the page as one readable multi-line HTML file
- no framework bootstrapping
- no local assets
- no compressed one-line output
- keep CSS and JS maintainable
- keep interaction logic clear enough for handoff

## Round 4

Polish the experience until it feels launch-ready.
The result should feel authored by a serious product and design team.
Every chapter should contribute to the same planning worldview.

Final quality checklist:
- complete CSS `:root` token system used consistently
- at least 10 meaningful blocks or chapters
- all required interactions implemented: Modal, Accordion, Toast, Tabs, Scroll reveal, Stagger animation, Count-up, Navbar scroll transition
- additional useful interactions included where they strengthen the planning story
- strong Default, Hover, Active, and Focus states across major controls
- responsive behavior is deliberate at all 4 breakpoints
- accessibility is integrated from the beginning
- no frameworks
- no local resources
- no `style=""`
- final result is one readable self-contained `index.html`

Final differentiation test:
- if the page still reads like a generic SaaS hero followed by cards, redesign it
- if the ledger canvas could be removed without harming identity, the concept is too weak
- if the same palette, structure, and motion could be swapped into another case without much change, the result is too generic
- if risk, funding, and sequencing do not visibly connect, the information design has failed
- if the page feels like sustainability branding instead of capital-planning software, push it further

Editorial finishing rules:
- tighten label language
- keep legal notes compact but credible
- give sections purposeful names
- maintain believable ratios between narrative copy and data surfaces
- ensure the first viewport feels specific to Northstar Ledger

Before final output, verify:
- the layout does not collapse into repeated cards
- at least 3 chapters use different compositional logic
- at least 2 interactions materially change reading order, planning emphasis, or information depth
- the page looks distinct from other cases in the batch at a glance
- the product promise is understandable without reading every paragraph

Return only the final code in the HTML step.

GENERATE THE FINAL CODE NOW
