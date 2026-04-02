## Round 1

Create a production-grade 2025-2026 single-page site for Helio Harbor.
Helio Harbor is a members-only electric dayboat club with concierge coastal routing.
The page must feel like a premium mobility product, not a generic marketing template.
The experience should blend daylight leisure energy with precise operational detail.

Audience:
- private members booking coastal sessions
- concierge partners coordinating guest plans
- operations staff managing vessels and dock windows

Brand tone:
- refined
- confident
- bright without being playful
- service-oriented and specific

Technical constraints:
- return one complete self-contained index.html
- one file only
- CSS in one style block
- JavaScript in one script block
- no frameworks
- no external libraries
- no local assets
- no style attributes in markup

Visual direction:
- modern premium glass surfaces
- luminous accents inspired by morning sun and sea reflections
- layered atmospheric gradients with restrained glow
- high-clarity typography and data chips

Define a complete token system in CSS root variables:
- background primary
- background elevated
- glass surface levels
- glass border levels
- text primary
- text secondary
- text tertiary
- accent cyan
- accent coral
- accent gold
- status open
- status caution
- status closed
- radius scale
- spacing scale
- shadow scale
- type scale
- transition duration scale
- transition easing scale

Structural requirements:
- at least 12 substantial sections
- no repeated one-pattern card stack
- include at least two chapters with distinct layout logic
- include one oversized expressive chapter that breaks standard rhythm

Required section coverage:
- sticky glass navigation with capacity indicator
- hero with circadian-style sun path motif
- live operations strip for marina timing
- fleet showcase with detailed vessel cards
- tide and transit desk with tabbed data
- route journal with map-linked notes
- impact metrics with count-up behavior
- concierge planning module
- membership passes comparison
- compliance and policy accordion
- booking modal trigger region
- closing conversion section with form
- structured footer with policy and location links

Copy quality requirements:
- real service language
- believable boating and marina terms
- concise but specific operational details
- no vague filler statements
- no decorative text blocks without product meaning

Signature requirement:
- first viewport must clearly communicate Helio Harbor identity
- at least one hero instrument must look interactive and purposeful
- visual atmosphere must support readability and conversion

## Round 2

Implement at least 8 meaningful interactions with real behavior:
- modal
- accordion
- toast
- tabs
- scroll reveal
- stagger animation
- count-up
- navbar scroll transition

Interaction mapping:
- modal opens from primary hero CTA and secondary booking CTA
- modal includes practical intake fields for session planning
- modal supports close via button overlay and Escape key
- accordion handles policy and membership edge cases
- tabs power the tide and transit desk with real content switching
- toast confirms successful action with clear status wording
- scroll reveal applies chapter-aware motion rather than identical fade everywhere
- stagger animation applies to fleet cards or itinerary items
- count-up runs on viewport entry and does not loop endlessly
- navbar transitions to compact mode with preserved usability

Additional case-specific interactions:
- route card expansion showing stop-by-stop details
- session duration chips with active selection state
- fleet card tilt or glow response on pointer movement
- availability toggle that changes supporting copy

State requirements:
- explicit default hover active focus states for all clickable controls
- selected state for tabs and chips
- expanded state cues for accordion panels
- disabled state styling where applicable
- high-contrast keyboard focus visibility

Motion requirements:
- cubic-bezier timing for core transitions
- avoid excessive movement that harms clarity
- maintain smoothness in scrolling and panel transitions
- reduced motion mode must simplify nonessential effects

## Round 3

Responsive breakpoints:
- at and above 1440
- from 1024 to 1439
- from 768 to 1023
- below 768

Responsive behavior constraints:
- preserve identity of hero and operations strip at all sizes
- avoid collapsing every section into identical cards
- keep dock schedule and tide data scannable on mobile
- ensure CTA and booking paths remain obvious on small screens
- maintain balanced spacing and hierarchy across breakpoints
- keep primary controls reachable with thumb-friendly sizing

Accessibility requirements:
- semantic landmarks using header nav main section footer
- proper heading hierarchy
- labels for all form controls
- aria labels for icon-only controls
- keyboard navigation for modal tabs accordion and navigation
- visible focus indicators across components
- avoid color-only meaning for status
- maintain readable contrast for text and controls
- include reduced motion support for reveal and count-up effects

Form accessibility requirements:
- clear field labels and helper text where needed
- validation feedback that is understandable and specific
- success message behavior tied to toast and form state

Performance and maintainability:
- avoid unnecessary repaint-heavy effects
- keep script logic modular and readable
- keep CSS token usage consistent and centralized

## Round 4

Final polish checklist:
- all design tokens are applied consistently
- each major chapter has distinct visual structure
- interactions are complete and functionally meaningful
- content reads like a real premium service product
- navigation and booking flows are clear from first scroll
- no broken components or unfinished visual artifacts
- source remains readable and maintainable

Validation checklist:
- modal open and close behavior works in all trigger paths
- tabs update active state and corresponding content panel
- accordion panel states are synchronized with controls
- count-up values animate once when entering viewport
- navbar transition remains stable on repeated scroll
- toast messaging appears and dismisses predictably
- keyboard users can operate core features without traps

Quality bar:
- first screen feels unmistakably tied to Helio Harbor
- middle chapters demonstrate real operational utility
- final section presents a credible booking handoff
- overall craft level matches modern premium product sites

Return only the final code for one index.html.
GENERATE THE FINAL CODE NOW
