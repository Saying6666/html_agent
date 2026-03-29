import os

path = "c:/Users/saying/Desktop/html_agent/fdu_007/prompt.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

extra = """
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
- The background consists of 3 to 4 massive `<div class="orb">` elements fixed the viewport.
- They must use intense CSS `filter: blur(150px)` to create soft, shifting color pools.
- The animation must be a slow drift (15 to 30 second loops) across the screen margins.
- These orbs interact with the `backdrop-filter: blur(20px)` on foreground glass panels to create dynamic illumination as the user scrolls.
- The layering dictates that the ambient orbs are z-index: -1, ensuring no interaction blockages.

## 16. Technical Quality Assurance and Validation Loop
Before delivering the final asset, the following structural checks must be guaranteed:
- No deprecated tags.
- Every `role` must be paired with appropriate `aria-*` tags (vital for Tabs and Modal).
- The `index.html` structure must be perfectly indented to allow another engineer to jump in and immediately understand the nested component structure of the glass cards and scrollytelling.
- Transitions must exclusively use `cubic-bezier` timing functions for professional elasticity.
- Zero horizontal scroll artifacts (ensure `overflow-x: hidden` is applied securely).
- At all four breakpoints, the "Drift Ledger" narrative flow must hold. Mobile experience must prioritize the route log and timeline over decorative graphics.

## 17. Animation & Interactive Timeline Precision
- Scrollytelling requires careful IntersectionObserver settings.
- The active states must sync perfectly across visual and textual logs.
- Provide a robust focus-trap on the modal.
- Include a visual scrubber element that manipulates DOM directly to reflect temporal adjustments.

## 18. Extensibility
Ensure the HTML is structured so adding another tab or accordion item is copy-paste trivial. Maintain atomic CSS classes where possible but prioritize a strict bespoke BEM-style where things get complex like `.dossier-step--active`.
"""

with open(path, "w", encoding="utf-8") as f:
    f.write(text + extra)

"""