## Round 1: Role + Design System + Sections

﻿# Drift Ledger: The Next-Generation Maritime Intelligence Platform
# Project Brief & Requirements Document

## 1. Executive Summary
Create a 2025-2026 production-grade single-page website for **Drift Ledger**.
Drift Ledger is a climate-risk routing and port continuity platform. 
The core audience consists of ocean freight operators, marine insurers, port continuity teams, and resilience leaders.
The page must feel like a real maritime intelligence product, yet heavily modernized into an ultra-premium digital experience. 
Do not write a generic "hero + 3 cards + FAQ" template. 
Make this case recognizable at a glance.

## 2. Core Aesthetic: Modern Premium Glassmorphism & Glo UI
- **Glassmorphism:** Implement an ultra-premium glassmorphic aesthetic heavily leaning on backdrop-filter: blur(). Every major surface should feel like a frosted lens layered over a complex depth map.
- **Conic-Gradient Borders:** Use conic-gradient borders on cards and key elements to create a sharp, high-fidelity edge that reacts dynamically.
- **Ambient Blurred Orbs:** Create ambient blurred orbs in the background that drift slowly, reflecting a high-end Glo UI vibe. These orbs simulate deep ocean phenomena or bioluminescence.
- **High-Contrast Dark Mode:** Emphasize deep, rich, dark oceanic tones (abyssal blue, carbon) transitioning into vibrant cyan, hazard amber, or bioluminescent turquoise for the orbs.
- **Layered Depth:** Ensure all glass layers have multiple faint white/cyan inset borders (box-shadow: inset ...) to look incredibly realistic.
- **Mood:** A futuristic, hyper-advanced, premium maritime intelligence hub.

## 3. Deliverable Constraints (Non-Negotiable)
- Return exactly one complete self-contained index.html.
- All CSS must be inside one <style> tag.
- All JavaScript must be inside one <script> tag.
- No frameworks: no React, no Vue, no Svelte.
- No external libraries: no GSAP, no jQuery.
- No build step.
- No local assets and no local file references.
- No external images, no external fonts, no external CSS, no external JS.
- If visuals are needed, use pure CSS and inline SVG only.
- Do not use style attributes in markup. 
- Make it responsive across 4 breakpoints (Large Desktop, Desktop, Tablet, Mobile).
- Make it accessible and keyboard friendly.

## 4. Typographic Direction
- High-end sans-serif or geometric sans, sleek and modern.
- Incorporate monospace/tabular fonts specifically for coordinates, logs, and data readouts.
- Establish a deliberate typographic hierarchy with precise letter-spacing on subheadings.
- Dense but clear text layouts mimicking dense instrumentation panels.

## 5. Interaction & Animation Constraints (Precise Real Micro-interactions)
Implement at least 8 real functional interactions:
1. **Modal:** A highly polished "Resilience Review" modal with a glassmorphic background, featuring an interactive routing intake form. Live summary updates inside the modal. Accessible focus trap, keyboard closing.
2. **Accordion:** FAQ styled as premium intelligence foldouts. Smooth height transitions (via grid max-height or height calc).
3. **Toast:** Beautiful glowing toast notifications confirming actions like "Route brief saved" or "Calculating path variance". Use aria-live.
4. **Tabs:** Glowing control room tabs switching views (Routing, Port continuity, Underwriting, Compliance). Smooth fades without layout jumps.
5. **Scroll Reveal:** Elements floating up and fading in softly out of the glass background.
6. **Stagger Animation:** Delayed entrance for data grids, badges, and trust marks.
7. **Count-up:** Animated data counters (with units like hours, percent) when scrolling into view.
8. **Navbar Transition:** Glassmorphic navbar that condenses and becomes more opaque upon scroll.
- **Extra:** A "Route replay" scrubber. Pure CSS/JS scrubber that changes an inline SVG preview route path overlay.

## 6. Section Guidelines (12+ Sections)
The layout must be vast and comprehensive. Include at least the following 12 sections:

### Section 1: Navigation
- Sticky glass header, current ocean state badge (e.g., "Pacific Swell: Nominal").
- Dynamic scroll transition reducing height and increasing blur.

### Section 2: Immersive Hero
- Ambient background with drifting orbs.
- Glowing typography, primary CTAs.
- Abstract SVG data overlay representing global thermal anomalies.

### Section 3: Trust Strip
- High-end textual operator and insurer endorsements.

## Round 2: Interactions + Animations

- Ensure 8+ functional interactions using real JS.
- Add hover, active, focus states.
- Use smooth cubic-bezier animations.

- Glowing text slowly pulsing.

### Section 4: Signal Grid
- 4-column feature breakdown (Forecasting, Routing, Underwriting, Compliance).
- Fully rendered inside glass cards with conic borders.

### Section 5: Scrollytelling Dossier
- Sticky glass pane on the left, scrolling steps on the right updating the pane.
- Illustrates a complex routing decision process.

### Section 6: Interactive Control Room (Tabs)
- The core tabs section. Large glass panel switching operational contexts.
- Contains the Route Replay scrubber in one of the views.

### Section 7: Metrics Band
- Count-up numbers inside individual frosted capsules.
- Displays metrics like "Port Delays Avoided", "Carbon Intensity Output", etc.

### Section 8: Route Disruption Timeline
- A vertical logbook style timeline with glowing nodes.
- Shows timestamped events: "Storm Surge Detected", "Vessel Rerouted", "Port Continuity Initiated".

### Section 9: Comparison Memo
- 2-column comparison showing Legacy vs Drift Ledger.
- Full bleed gradients emphasizing the transition from traditional to modern.

### Section 10: Forecast Bulletin
- Insight cards styled as intelligence briefs.
- Stagger-revealed upon scroll.

### Section 11: Compliance & Reporting
- A dedicated block for environmental and regulatory compliance.
- Specifically highlighting EU ETS and CII metrics.

### Section 12: Knowledge Base (FAQ)
- Accordions using glassmorphic panels and conic borders.
- Detailed questions covering integration, forecasting accuracy, and data security.

### Section 13: Final CTA & Scheduling
- Form to schedule a resilience review.
- High-contrast inputs with glow on focus.

### Section 14: Comprehensive Footer
- Wide, deep-blur footer with compliance links, corporate routing, and strict policy texts.
- Glowing logo iteration.

## 7. Design System Tokens
- Define ambient background colors (deep navy, oceanic black).
- Define glow colors (cyan, magenta, turquoise, hazard orange).
- Define glass parameters (blur amounts, background colors with high transparency, border styles).
- Define typography scale, spacing variables, radii.
- Execute responsive scaling using rem or pure media queries.

## 8. State Design Requirements
- Define clear default, hover, active, and focus states for all interactive elements.
- Hover and active must change more than color (e.g. shadow spread, border gradient rotation).
- Focus ring must be visible on dark backgrounds.

## 9. Motion Tone
- Motion must feel like high-end electronic instruments and briefings.
- Precise, algorithmic, and smooth.
- Avoid playful bounces or springy effects.
- Prefer fluid cubic-bezier curves for all transitions.

## 10. Responsive Re-composition Constraints

## Round 3: Responsive + Accessibility

- Must support 4 responsive breakpoints.
- Include ARIA tags and keyboard navigation.
- Handle prefers-reduced-motion.

- At least 2 major modules must fundamentally change form on mobile.
- Keep the first mobile viewport unmistakably maritime and premium.
- Do not collapse into a single boring centered column of identical cards.

## 11. Accessibility Requirements (Mandatory)
- Semantic landmarks (header, nav, main, section, footer).
- Proper heading hierarchy.
- Include a skip-to-content link that becomes visible on focus.
- Full keyboard support.
- ARIA: role=tablist, aria-expanded, role=dialog, aria-live.
- Icon-only or graphic-heavy sections must have text alternatives.
- Reduce motion queries to disable heavy orbs and staggering.

## 12. Conclusion & Delivery
- Do not include standard templates.
- Ensure the output is purely HTML, scoped to one file.
- Push the boundaries of inline CSS capabilities, utilizing modern custom properties deeply.
- Validate all micro-interactions before finalizing the markup.
- Execute this as the absolute pinnacle of front-end engineering in 2025.
## 13. Deep Dive into Metric Instrumentation
The metrics band must provide actual numeric data visualization that looks entirely real.
- **Voyage Delay:** Show a count indicating the number of hours saved per standard route calculation phase. Emphasize that these hours correspond to real berth windows.
- **Hazard Probability:** Showcase the reduction delta in safety incidents. This should pulse or glow indicating a continuous scanning process is active.
- **Port Operations Synchronization:** This is a crucial metric demonstrating how Drift Ledger aligns offshore speeds with port intake rates. Every minute saved idling is a massive carbon reduction.
- **System Confidence Score:** Display a dynamic variable indicating the algorithm's confidence level based on current meteorological input fidelity.
- **Model Refresh Rate:** Number of times weather models are injected into the calculations per voyage hour.
- **Underwriting Savings:** Average premium reduction per fleet utilizing the predictive model.

## 14. Typography Detailed Specifications
The typographic experience must separate Drift Ledger from consumer-grade software completely.
- Body Copy: Must use a highly structured, medium-weight geometric sans. Line height should be generous enough for long reading sessions by insurance reviewers (1.6 to 1.75). No condensed body type.
- Headings: Employ a slight negative letter-spacing for large titles to give them gravity. All primary section headers must carry a subtle text-shadow simulating a digital readout.
- Micro-labels: Crucial for real-world application feel. Use a highly legible monospace font for all operational metadata like timestamps (e.g., T-04:00, latitudes, longitudes, confidence intervals). Small caps or strict uppercase with track letter-spacing (+0.1em).
- Status Indicators: Text within status chips should not just rely on color. The text itself must be explicit (e.g. "WATCH_ACTIVE", "SWELL_ANOMALY").
- Button Text: All interactive primary calls-to-action should utilize the primary sans-serif but have strong weight.

## 15. The Science of the Ambient Glow
To truly sell the Glo UI and Glassmorphism, the background cannot just be flat navy.
- The background consists of 3 to 4 massive <div class="orb"> elements fixed the viewport.
- They must use intense CSS filter: blur(150px) to create soft, shifting color pools.
- The animation must be a slow drift (15 to 30 second loops) across the screen margins.
- These orbs interact with the backdrop-filter: blur(20px) on foreground glass panels to create dynamic illumination as the user scrolls.
- The layering dictates that the ambient orbs are z-index: -1, ensuring no interaction blockages.

## 16. Technical Quality Assurance and Validation Loop
Before delivering the final asset, the following structural checks must be guaranteed:
- No deprecated tags.
- Every role must be paired with appropriate aria-* tags (vital for Tabs and Modal).
- The index.html structure must be perfectly indented to allow another engineer to jump in and immediately understand the nested component structure of the glass cards and scrollytelling.
- Transitions must exclusively use cubic-bezier timing functions for professional elasticity.
- Zero horizontal scroll artifacts (ensure overflow-x: hidden is applied securely).
- At all four breakpoints, the "Drift Ledger" narrative flow must hold. Mobile experience must prioritize the route log and timeline over decorative graphics.

## 17. Animation & Interactive Timeline Precision
- Scrollytelling requires careful IntersectionObserver settings.
- The active states must sync perfectly across visual and textual logs.
- Provide a robust focus-trap on the modal.
- Include a visual scrubber element that manipulates DOM directly to reflect temporal adjustments.

## 18. Extensibility

## Round 4: Final Polish + Generation

- Review against final checklist.
GENERATE THE FINAL CODE NOW.

Ensure the HTML is structured so adding another tab or accordion item is copy-paste trivial. Maintain atomic CSS classes where possible but prioritize a strict bespoke BEM-style where things get complex like .dossier-step--active.

## 19. Additional Constraints
- Make sure to review color contrast ratios.
- The minimum contrast ratio must be 4.5:1.
