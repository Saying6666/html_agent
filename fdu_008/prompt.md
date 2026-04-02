## Round 1

Create a production-grade 2025-2026 single-page site for Harborline Atlas.
Harborline Atlas is a carbon-aware maritime operations platform for luxury passenger terminals.
The page must feel like a real launch from a funded product team.
The page must not look like a generic classroom demo.
The page must be visually distinctive from common dark SaaS templates.

Audience:
- terminal operations directors
- fleet dispatch managers
- guest experience leads
- sustainability officers

Narrative intent:
- show how one system coordinates berth windows, boarding flow, and carbon impact
- keep language operational and concrete
- present the product as deployable now, not speculative

Core technical constraints:
- return one complete self-contained index.html
- single file only
- all CSS inside one style block
- all JavaScript inside one script block
- no frameworks
- no external libraries
- no local assets
- no style attributes in markup

Visual direction:
- premium glass surfaces with layered depth
- calm maritime palette with restrained neon accents
- atmospheric orbs that support hierarchy rather than distract
- strong typography with clear operational labeling

Define a complete tokenized design system in CSS root variables:
- background base
- background elevated
- glass surface levels
- glass border levels
- text primary
- text secondary
- text subtle
- status on-time
- status watch
- status reroute
- accent cyan
- accent amber
- accent deep blue
- shadow levels
- radius scale
- spacing scale
- type scale
- duration scale
- easing scale

Page architecture requirement:
- build at least 12 substantial sections
- avoid repeated card-only rhythm
- include at least two sections with asymmetric structure
- include one section that breaks centered container alignment

Required section coverage:
- sticky navigation with live status chip
- high-impact hero with dispatch console
- trust strip with partner signals
- operations thesis section
- full-width departure board module
- terminal map with zone switching
- passenger flow analytics
- carbon receipt ledger
- capability architecture grid
- count-up impact band
- case study spotlight
- policy and compliance accordion
- conversion section with real form
- structured footer with governance links

Content quality requirements:
- use believable marine operations vocabulary
- include realistic labels for berth, turnaround, and service windows
- include realistic short data snippets in tables and chips
- avoid vague marketing filler
- maintain clarity under visual complexity

Signature module requirement:
- departure board and terminal map must be central to the story
- they must drive downstream narrative sections
- they must not be decorative shells

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
- modal opens from at least two independent CTAs
- modal includes a credible scheduling flow
- modal supports close button, overlay close, and Escape close
- accordion controls policy and compliance details
- accordion updates expanded state indicators
- toast confirms a completed action with concise status copy
- tabs switch live operational content, not just style states
- scroll reveal is section-aware and not uniform copy-paste motion
- stagger animation applies to grouped operational items
- count-up starts only when visible in viewport
- navbar transitions from spacious to compact mode after scroll

Add additional case-specific interactions:
- departure status filter chips
- zone selector in terminal map panel
- board row focus highlight on hover and keyboard focus
- service flag toggle for special handling

State design requirements:
- define default hover active focus states for buttons and links
- define selected state for tabs and filter chips
- define expanded and collapsed states for accordion triggers
- define focus states with strong contrast and visible outlines
- include disabled treatment where actions are not available

Motion quality requirements:
- use modern cubic-bezier timing
- limit gratuitous motion
- align animation direction with information flow
- keep transitions performant on mid-range devices
- respect reduced motion preferences in behavior and timing

Data interaction realism:
- departure board rows include plausible times and gates
- map panel content updates with selected zone
- count-up values represent meaningful operational metrics
- toast copy reflects the exact action taken

## Round 3

Responsive targets:
- desktop wide at and above 1440
- desktop and laptop from 1024 to 1439
- tablet from 768 to 1023
- mobile below 768

Responsive behavior requirements:
- preserve signature module clarity at every breakpoint
- avoid collapsing into one repetitive card column
- keep navigation usable without crowding labels
- keep board data scannable with horizontal strategies if needed
- ensure map and detail panel remain understandable on mobile
- maintain spacing rhythm and clear section boundaries

Accessibility requirements:
- semantic landmarks with header nav main section footer
- logical heading hierarchy
- accessible names for all controls
- aria labels for icon-only buttons
- keyboard support for modal tabs accordion and key controls
- visible focus styles across the interface
- color is not the only status indicator
- maintain strong contrast for primary text and controls
- support reduced motion mode across reveal and counter behavior

Form accessibility requirements:
- every field has label and hint text where needed
- error and success feedback is explicit
- submit action has clear post-action status

Internationalization readiness:
- text containers avoid clipping with longer strings
- metric and time labels are structurally separable

## Round 4

Final polish checklist:
- design system tokens are used consistently
- all major sections have distinct silhouettes
- departure board and map module remain central
- interactions are complete and functional
- visual quality feels premium and product-grade
- code remains readable and maintainable
- no broken controls
- no dead links presented as actions
- no unfinished visual artifacts

Verification checklist:
- modal opens and closes correctly through all methods
- tabs switch content and update selected state
- accordion opens and closes smoothly
- count-up triggers only once per metric
- navbar transition is stable during rapid scroll
- toast appears and dismisses predictably
- keyboard navigation can reach and operate core controls

Quality bar:
- the first screen is unmistakably Harborline Atlas
- middle sections maintain operational depth
- closing section provides a credible next step for deployment
- final result looks like a modern maritime product launch

Return only the final code for one index.html.
GENERATE THE FINAL CODE NOW
