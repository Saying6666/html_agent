import os

added_text = """
## Component Deep Dives and Constraints

### Typographic Scales & Hierarchy
All text elements must explicitly map to these variables to guarantee perfect resizing and scaling. Do not arbitrary define pixel or rem values inline without mapping to variables first.

1. **Heading 1**: 
   - Font: Playfair Display.
   - Use dynamic scaling `clamp(3rem, 8vw, 7rem)`. 
   - Letter-spacing: -0.02em. 
   - Used only inside the Hero section.
2. **Heading 2**: 
   - Font: Playfair Display.
   - Size: `clamp(2rem, 5vw, 4.5rem)`.
   - Used for structural section headers like "Therapy Suites" or "Telemetry".
3. **Heading 3 (Cards/Subheaders)**: 
   - Font: Playfair Display or Inter dependning on context.
   - Size: `1.5rem` to `2rem`.
   - Use inside Suite portals and Ritual cards.
4. **Body Text**:
   - Font: Inter.
   - Color: `var(--text-muted)`.
   - Line height: `1.6`.
5. **Mono Numerals**:
   - Font: JetBrains Mono or monospace fallback.
   - Specifically required for: telemetry reading digits, ledger dates, membership pricing, and suite durations.

### Micro-interactions & Affordances
Do not use standard flat `:hover` changes. Everything must mimic glass reacting to light.

- **Buttons**:
  - Should slide up by `2px` via `transform: translateY(-2px)`.
  - Add `box-shadow` with `var(--accent-glass)` on hover, to simulate the button radiating light.
  - Apply `border-color: var(--accent)`.
- **Card Hover Glows (The Flashlight Effect)**:
  - Inside the Ritual Library cards, use Javascript to track `mousemove`.
  - Update CSS variables `--mouse-x` and `--mouse-y`.
  - A pseudo-element `::before` with a `radial-gradient` must follow the user's mouse mimicking an inner glow inside the glass card.
- **Data Counting**:
  - The telemetry digits should not start at their final value. They must use JS Intersection Observer.
  - Count from 0 to the final value over exactly 2 seconds when they scroll into view.
- **Ambient Canvas**:
  - The background orbs are not static images. They are divs with massive border radius (`50%`) and blur (`filter: blur(120px)`).
  - Animate them using infinite alternating `@keyframes` with transform translate to create slow "breathing" or floating effects.

### Data Theme Mappings
Switching the `--theme` property on `html` MUST cascade through the entire UI flawlessly.
If the mode is **dusk**, use warm amber.
If the mode is **night**, use deep blue.
If the mode is **dawn**, invert the background to light grey, invert text to dark charcoal, change glass-borders to black with low opacity, and update orbs to peach and coral.

Ensure the banner text acknowledges this mode. The wheel SVG path should highlight the active arc.

### The Footrest
Do not neglect the footer. Use semantic grids (4 columns) that scale down to 1 column on mobile devices.
Opacity on links should be 0.8, transitioning to 1.0 on hover.
"""

with open('fdu_012/prompt.md', 'a', encoding='utf-8') as f:
    f.write(added_text)

print('Success')
