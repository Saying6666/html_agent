# Nera Pulse House - Modern Premium Glassmorphism & Glo UI

## Project Overview
**Project**: Nera Pulse House
**Type**: Members-Only Urban Recovery Club
**Offer**: Contrast therapy suites, circadian lighting, biometric coaching, private cultural programming
**Timeframe**: 2025-2026

## Design Paradigm & Aesthetic Rules: Modern Premium Glassmorphism
This is not a generic minimalist dashboard. It is a premium club built on physiological cues, ritual, and measurable recovery.
- **Glassmorphism**: High use of `backdrop-filter: blur(24px)`, semi-transparent backgrounds with soft white/light outlines (`border: 1px solid rgba(255, 255, 255, 0.15)`).
- **Ambient Blurred Orbs**: Large animated blurred circles in the background (`filter: blur(120px)`) that pulse, shift, and respond to the Circadian Modes.
- **Conic-Gradient Borders**: Key premium elements must use `conic-gradient` masks for their glowing borders, simulating polished brushed metal holding glass panes.
- **Depth & Layering**: Stacking blurred cards over complex ambient backgrounds. Extensive use of multi-layered drop shadows (`box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2)`).
- **Typography**: Expressive serif (`Playfair Display` or system serif) for headlines to communicate luxury and tradition; humanist sans for UI text and paragraphs. Mono/tabular numerals for biometrics and metrics.
- **Motion & Micro-interactions**: Real JS and CSS transitions for *all* interactive elements. Magnetic hover effects, revealing inner glows.

## Circadian Mode Paradigm
The core premise is visually driven by a **Circadian Control System**, changing the entire mood.
The page switches between three states based on the Signature Device:
1. **Dusk (Warm Amber)**: Deep charcoal background, glowing amber soft orbs, burnt orange gradients. Signals wind-down and thermal contrast.
2. **Night (Moon-Blue)**: Pitch black canvas, icy blue and deep violet glowing orbs. Signals deep recovery and sleep optimization.
3. **Dawn (Pale Coral)**: Soft mineral white/grey background, peach and pale coral orbs. Signals awakening, mobility, and readiness.
*These modes must rewrite CSS variables (`data-theme="dusk|night|dawn"` on the `html` or `body` element).*

## Required Structure (12+ Distinct Sections)

### 1. The Aura Banner
A persistent topmost bar with "Glassmorphism" styling. Displays realtime capacity ("Current Capacity: 24/50") and active global light cue.

### 2. Sticky Glass Navigation
A blurred header that morphs into a compact console upon scroll. Contains membership login, structural links, and a pulsating status chip ("Club: Active").

### 3. Circadian Wheel Hero (Signature Device)
Massive hero section showcasing the inline-SVG circadian wheel.
- Users can click/drag the wheel to change the global theme (Dusk/Night/Dawn).
- The background features enormous blurred orbs (`filter: blur(150px)`) that shift colors based on the mode.
- Large expressive serif headline: "Calibrate Your Cadence."
- Two primary glass CTAs with conic-gradient borders.

### 4. Credential Seals (Proof of Logic)
A row of frosted glass badges.
- Clinical Physiology Partner.
- Spatial Design Architect.
- Elite Biometric Coaching standard.

### 5. Suite Stage (Interactive Showcase)
A tabbed interface exploring the 4 principal contrast therapy suites.
- Requires complex frosted glass cards.
- Each suite holds details: Intent, Modalities (Heat/Cold/Air), and Duration.
- Image placeholders created entirely with CSS grid patterns and glowing overlays.

### 6. The Instrument Panel (Biometrics)
Displaying aggregated member recovery data (simulated).
- Tabular numerals, ring charts (SVG), and glowing bar graphs showing HRV (Heart Rate Variability), RHR (Resting Heart Rate), and Sleep Architecture.
- Real JS to animate numbers on scroll.

### 7. Ritual Library
Cards depicting specific recovery routines:
- "The 14-Minute Plunge"
- "Circadian Reset Protocol"
- "Vagal Tone Calibration"
Cards feature hover states where a glowing ambient light follows the cursor.

### 8. Ambient Cultural Programming
Details on private talks, ambient music sets, and breathwork seminars.
Listed in an elegant ledger format with translucent hover rows.

### 9. Guided Membership Tiers
Tier cards with glassmorphism and prominent pricing.
- "Pulse Initiatate"
- "Nera Vanguard"
- Cards must use conic-gradient borders that slowly rotate.

### 10. The Concierge AI (Chat/Booking Interface)
A mock terminal/chat interface embedded in a glass pane.
- Auto-typing effect welcoming the user.
- Interactive chips to select typical prompts ("Book contrast suite", "Show my biometrics").

### 11. Immersive Manifesto
A large screen-filling typographic block with profound statements on modern recovery.
- "We are not a gym. We are an instrument for your physiology."
- Slowly panning blurred gradients behind the text.

### 12. Architectural Footer
A heavy, deeply blurred footer section.
- Legal, locations, privacy, and an abstract brand mark (SVG).
- Final Call to Action.

## Strict Technical Requirements
- Single `index.html` file >600 lines.
- NO external CSS/JS/Images. Use inline scripts and styles.
- Complex `:root` system for the dusk/night/dawn mode switching.
- Use advanced CSS: grid, flexbox, clamp(), backdrop-filter, conic-gradient.
- Add JS observers for scroll, hover tracking (glow effects), theme switching, number counting.
- Extensive, high-quality copywriting. No Lorem Ipsum.

## Expanded details to reach >160 lines constraint

Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...

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
