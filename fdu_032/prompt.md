## Round 1: Role + Design System + Sections

**Role:**
You are a master frontend developer, senior UI/UX engineer, and
tactical interface designer. You specialize in creating highly
immersive, data-dense, modern web applications that provide real-time
operational oversight. Your task is to build the comprehensive,
single-page landing and dashboard interface for "Relay Vault", an
elite command-readiness platform designed for high-stakes operational
environments, strategic global planning, mission-critical asset
tracking, and real-time data visibility.

**Design System & Theme:**
- **Visual Style:** The visual aesthetic must embody "Modern Premium
  Glassmorphism" combined with a highly specialized "Glo UI". This
  means utilizing dark mode as the default, emphasizing high contrast,
  crisp typography, and subtle neon glows against deep, expansive
  backgrounds.
- **Color Palette:**
-   **Background:** Primary background is a deep obsidian (#0D0E15)
  transitioning into a midnight atmospheric blue (#1A1C29). Use large,
  scattered, blurred radial gradients (in cyan and magenta) to serve
  as ambient light sources behind the glass panels.
-   **Primary Accent:** Cyberpunk Neon Cyan (#00F0FF). Use this for
  active states, critical path actions, buttons, and high-level hover
  effects.
-   **Secondary Accent:** Tactical Magenta (#FF007F) for alerts,
  active threat indicators, graphs, and high-priority secondary
  highlights.
-   **Typography & Foreground:** Pure white (#FFFFFF) for primary
  headers, titles, and active nav links. Soft, legible silver/gray
  (#A0AABF) for body text, metadata, and secondary descriptions.
-   **Tertiary Elements:** Soft amber (#FFB000) for warnings or
  standby modes.
-   **Glass Panels (The Core UI Element):** All main content
  containers, cards, and floating panels must be created using a
  translucent background (e.g., rgba(255, 255, 255, 0.03) to 0.07),
  accompanied by a 1px solid glossy border (rgba(255, 255, 255, 0.1)),
  an intense backdrop-filter: blur(24px), and a subtle internal drop
  shadow or inner glow.

**Typography:**
- **Headings:** Use a geometric, technical, sans-serif like
  'Orbitron', 'Rajdhani', or 'Syncopate' to invoke an operational,
  military-grade authoritative feel. Ensure font weights range from
  standard to bold based on priority.
- **Body Text:** Use a highly legible, clean sans-serif like 'Inter',
  'Roboto', or 'Manrope' to maximize legibility within data-dense
  table layouts and feature descriptions. Aim for highly structured
  visual hierarchy using careful font sizes and grayscales.

**Layout Structure:**
The entire layout must feel like an expansive, grid-oriented dashboard
mixed with high-impact hero marketing areas. Use asymmetrical,
floating glass cards that overlap slightly to create depth. Ensure
generous padding within the glass components but maintain a tight,
structured grid padding for the overall canvas.

**Core Sections to Implement:**

1. **Global Navigation (Glass Header):**
-    Must be fixed to the top of the viewport with a strong backdrop-
  filter blur. Setup with Flexbox padding.
-    **Identity / Logo:** Left-aligned. Text reading "RELAY VAULT"
  heavily stylized, perhaps featuring a glowing dot, chevron, or
  radar-pulse SVG icon.
-    **Main Links:** Operations, Intel, Assets, Protocols,
  Communications. These links should have precision hover effects to
  demonstrate instantaneous response.
-    **Action Area:** Right-aligned. A glowing, bordered secondary
  button reading "System Status" and a primary filled button reading
  "Initialize Link".

2. **Hero Section (The Command Center):**
-    **Headline:** Massive, impactful, uppercase typography reading:
  "TACTICAL OVERSIGHT. ABSOLUTE CONTROL." Adjust responsive typography
  using clamp().
-    **Subheadline:** "Relay Vault equips global command units with
  zero-latency synchronization, quantum-encrypted channels, and
  absolute operational readiness across all vectors."
-    **Dual Call-to-Action:**
-      Primary Action: "Deploy Secure Hub" (Filled neon cyan, glowing
  drop-shadow, inner shadow detail).
-      Secondary Action: "View Protocol Schematics" (Outlined, glass-
  like, pure white border).
-    **Visual Centerpiece:** To the right (or centered for mobile), a
  floating 3D-like, isometric display composed of several overlapping
  glassmorphic widgets giving a sense of "mock data" (e.g., a radar
  sweep animation, a server load chart using CSS bars, global link
  status indicators).

3. **Live Telemetry & Metrics (Data Ribbon):**
-    Immediately below the Hero section, implement a horizontal
  scrolling ribbon or cleanly spaced CSS Grid of live tactical
  statistics.
-    **Metrics to include:**
-      "Uptime: 99.999% (Secure)"
-      "Active Global Nodes: 14,024"
-      "Current Global Threat Level: LOW"
-      "Protocol Encryption: AES-256-GCM / QS-1"
-    Use deeply glowing typography for the metric numbers and a muted
  silver for the labels.

4. **Features Grid (The Arsenal):**
-    **Section Title:** "OPERATIONAL CAPABILITIES & ARSENAL" -
  centered header with glowing underline accent.
-    **Layout:** A robust CSS Grid layout featuring at least 4 to 6
  glass cards.
-    **Content per Card:**
-      An intricate, custom-designed inline SVG icon (e.g., a shield
  for security, a satellite for comms, crosshairs for targeting, a
  data-tree for analytics).
-      **Card Titles:** "Quantum Encryption", "Multi-Vector Analysis",
  "Real-Time Comms", "Automated Contingency", "Asset Tracking",
  "Threat Neutralization".
-      **Card Descriptions:** Two sentences detailing the
  sophisticated capability of that specific feature, e.g. "Maintains
  integrity via redundant quantum pathways across multi-cloud
  environments."
-    **Hover Effects:** Hovering over any card must intensify its
  glass border, shift the background shadow/glow to Neon Cyan, and
  perhaps rotate or scale the SVG slightly to indicate interaction.

5. **Interactive Readiness Map (Data Visualization):**
-    **Purpose:** Serve as a visual centerpiece midway down the page
  to show global reach.
-    **Layout:** A massive, full-width or wide-container section
  housing a stylized HTML/CSS/SVG map or geographic data visualization
  point node grid. Use subtle opacity gradients over the map area.
-    **Details:**
-      Render floating "tooltips" or glowing pulses over specific
  "nodes" or "sectors" on the map. Use keyframe animations for the
  pulses.
-      On the side of the map (or overlaid), build a semi-transparent
  data table / panel describing the "Active Sector Status" (e.g.,
  "Sector 7-Alpha: Secure, Ping: 12ms", "Sector Gamma: Warning, Ping:
  82ms").

6. **Testimonials / Briefing Logs:**
-    Command logs or endorsements stylized as encrypted transmissions.
  Display them linearly or via grid layout.
-    Cards showing authorization codes, avatars (abstract geometric
  shapes), and short endorsements like "Relay Vault shortened our
  global strike response latency by 84% without compromising localized
  security policies. Outstanding resilience under siege."

7. **Protocol Footer:**
-    Dark, minimal, highly structured using robust semantic areas.
-    **Columns:** Resources, Command Support, Legal Directives, System
  Status Log. Layout via CSS Flexbox or Grid.
-    A final, subtle glowing copyright text floating at the very
  bottom ("© 2077 Relay Vault Systems. Classified."). Ensure its
  opacity is dialed down to 40% until hovered.

## Round 2: Interactions + Animations

**Animation Strategy & Philosophy:**
The interface must feel alive, breathing, and technologically
advanced. It cannot be purely static. Every interaction should
reinforce the "command and control" tactical aesthetic. Animations
must be smooth, using appropriate easing curves (like cubic-
bezier(0.16, 1, 0.3, 1)) rather than basic linear movement. Ensure
performant rendering.

**Introductory Animations (Load-in Sequence):**
- **Navigation:** Staggered fade-up and slight translate-y negative
  offset for navigation items (logo first, then links cascading, then
  buttons). Use simple animation delays.
- **Hero Text:** The main headline should reveal via a sophisticated
  clipping mask, sliding up character by character or word by word, or
  typing out like a terminal. Subheadline fades in subtly alongside
  it.
- **Floating Elements:** The glass cards in the Hero visual MUST
  gently bob up and down along the Y-axis. Setup a continuous,
  infinite keyframe animation to simulate suspension in a low-gravity
  or 3D digital space, ensuring different elements bob with slightly
  offset delays to feel organic and non-synthetic.

**Micro-Interactions (Hover, Focus, & Select):**
- **Buttons:** Hovering over the "Deploy Secure Hub" button should
  trigger a sweeping sheen of neon light across the button surface
  (using a masked linear gradient translate animation), increase the
  drop-shadow glow size dynamically, and slightly scale up the element
  (transform: scale(1.02)).
- **Glass Feature Cards:** When a user hovers over the operational
  capability cards, the backdrop-filter blur should dynamically
  increase or shift, border color should transition seamlessly to
  Primary Neon Cyan or Tactical Magenta, and a subtle glowing gradient
  orb effect should follow the hover state or simply brightly
  illuminate the border.
- **Navigation Links:** Links should feature a small, sharp underline
  that expands outward from the center upon hovering, utilizing a fast
  transition (approx 200ms ease-out).

**Scroll-Triggered Reveals:**
- As the user scrolls down the page, major sections (like the Features
  Grid, Data Ribbon, and Readiness Map) must fade in and slide up from
  approx 30px below their final resting position.
- Since we are restricted from complex external libraries, you may use
  minimal Intersection Observer logic in a tiny Vanilla JS block to
  append .visible classes to structural elements.
- These .visible classes will simply trigger CSS transitions precisely
  as elements enter the viewport, giving the user a "revealing"
  tactical intelligence experience.

**Data Sweeps & Radar Effects (Ambient Motion):**
- Integrate subtle background animation: use a sweeping radar line (a
  conical gradient that rotates 360 degrees infinitely) or slowly
  pulsating concentric geometric circles behind the Hero section and
  inside the Readiness Map. Make sure it stays subtle so it is not
  distracting.
- Implement a blinking "recording" or "live" red/magenta dot next to
  headers like "Live Telemetry" to signify continuous data streaming
  (using simple keyframes toggling opacity from 0.2 to 1).
- For metric numbers in the Data Ribbon, write a small JavaScript
  incrementer to make the numbers rapidly count up to their target
  values on page load/scroll to look like live data calculations,
  adding immersion.

## Round 3: Responsive + Accessibility

**Responsive Engineering Architecture:**
Ensure absolute, flawless fluid responsiveness across all viewport
sizes and device types. The complex glassmorphic layout, while
performance-intensive, must degrade gracefully on smaller screens
without abruptly losing its premium atmosphere. Every pixel must be
deliberate.

- **Ultra-Wide Desktop (1440px+):**
-   Allow the background abstract gradients to expand fully without
  breaking their shape.
-   Implement side-by-side complex layouts for the Readiness Map and
  sector info table, allowing data to breathe.
-   Push grid gap implementations to their maximum aesthetic
  allowance.
- **Standard Desktop (1024px - 1439px):**
-   Provide an expansive grid, maintaining sprawling floating widgets
  properly padded.
-   Scale the Features grid comfortably at 3 columns.
- **Tablet (768px - 1023px):**
-   Adjust Features grid strictly to 2 columns. Check that margins and
  padding correctly accommodate the tighter constraints.
-   The Hero visual scales down. Ensure the floating mock-widgets
  remain clear but smaller, retaining their continuous animations
  without overflowing horizontal restraints.
-   Start collapsing Navigation links, reducing internal padding sizes
  to economize horizontal space efficiently.
- **Mobile (Under 767px):**
-   **Navigation:** The global navigation must collapse entirely into
  a beautifully styled Hamburger menu. The toggle animation should
  cleanly transform three distinct lines into an "X".
-   **Mobile Menu Overlay:** The mobile menu taking over the screen
  must itself be a full 100% viewport glassmorphic overlay, with
  navigational links sliding in staggering sequence upon activation.
-   **Hero Stack:** Make the Hero sections fully stack vertically (the
  text stack aligned top-center, and visual widgets stacking directly
  below it). Remove tight desktop horizontal padding.
-   **Data Ribbon:** Convert the Telemetry ribbon to become a stacked
  list or a structured 2x2 grid, maximizing touch target viability and
  ensuring the readable metric numbers are large enough.
-   **Feature Cards:** Adjust glass cards to span 100% width,
  collapsing to a single column block layout. Maintain generous touch
  areas for any interactive elements.
-   **Performance Safety Note:** Ensure backdrop-filter heavy effects
  are slightly reduced or highly optimized (utilizing will-change:
  transform, opacity) to prevent jitter and safely maintain 60fps
  scrolling on lower-end mobile GPU browsers.

**Accessibility Standards (A11y) & UX Directives:**
- **Contrast Ratios:** Despite the highly stylized dark theme, the
  text-to-background contrast ratio MUST meet or exceed WCAG AA
  standards. Ensure primary text is genuinely readable, never
  completely washed out by background glass lighting layers.
- **Semantic HTML Canvas:** Strictly enforce proper structural DOM
  tags. Establish a crystal clear outline: header, main, section,
  article, nav, aside, and footer. NO generic div-soup architectures
  where structural semantics are warranted. Provide clarity to screen
  readers.
- **Focus Outlines:** Comprehensive keyboard access is an absolute
  mandate. Rather than default browser blue outlines, implement a
  custom :focus-visible state that rings interactive elements in a
  crisp 2px solid Neon Cyan outline offset by 2-3px, to keep the UI
  theme brilliantly unbroken.
- **ARIA & Screen Readers:** Ensure all embedded inline SVG icons
  utilized have appropriate role="img" and aria-label or aria-
  hidden="true" attributes. This ensures screen readers do not read
  out excessively long strings of vector data. Buttons must declare
  clear text context if text is obscured or icon-only.
- **Prefers Reduced Motion:** Completely respect the user's OS-level
  accessibility motion settings. Include a @media (prefers-reduced-
  motion: reduce) block that explicitly disables or massively slows
  down the continuous radar sweeps, infinite floating bobs, scaling
  hover effects, and typing sequences, opting purely for simple
  opacity fades instead.

## Round 4: Final Polish + Generation

**Code Rules & Absolute Constraints:**
1. **Single File Delivery Only:** You are instructed to output the
  entirety of the application—markup, extensive styling, and
  functional logic—as a SINGLE unified integrated index.html file
  block.
2. **Strict Vanilla Tech Stack Enforcement:** Do NOT utilize any
  external frameworks to construct the layout under any circumstances.
-    Absolutely NO React, Vue, Svelte, or Angular.
-    Absolutely NO Tailwind CSS, Bootstrap, Foundation, Bulma, or any
  pre-packaged CSS library. You may write custom utility modifier
  classes if desired, but all underlying CSS must be raw, hand-crafted
  CSS3.
-    Absolutely NO jQuery or external JS animation engines (like GSAP,
  Anime.js, or Framer Motion). Handle all animations directly via
  native CSS keyframes and standard Vanilla JavaScript DOM
  manipulation (ES6+).
3. **No External Media Assets (Except Standard Web Fonts):**
-    DO NOT reference external images whatsoever (like Unsplash urls,
  Imgur links, or generic HTTP placeholders). Any graphical need
  (background textures, radar elements, technical charts, profile
  avatars) must be accomplished using pure, inventive CSS combinations
  (linear gradients, box-shadows, geometric shapes) or complex, fully
  embedded inline SVGs directly inside the markup.
-    Zero tolerance for external icon CDNs (FontAwesome, Phosphor,
  Heroicons). You must painstakingly draw or construct all necessary
  SVGs directly in the HTML.
-    **Allowed Exceptions:** It is permissible to pull Google Fonts
  via a standard explicit link tag or @import directive to load
  typography engines like 'Orbitron', 'Rajdhani', or 'Inter' to meet
  design goals.
4. **Professional, Immaculate Code Quality:**
-    Your code delivery must be impeccably clean, logically ordered by
  component architecture, and deeply commented providing architectural
  blueprints and explaining element structures.
-    Establish a comprehensive, robust Root CSS variable directory
  (:root) serving to standardize the complete Design System parameters
  (mapping all thematic colors, varied breakpoints, font scaling
  steps, baseline spacing units, glass opacities, and glow shadow
  coordinates) solidly instantiated right at the top of the CSS
  styling block.
-    Aggressively utilize modern CSS display paradigms everywhere
  applicable. Ensure the integrated JavaScript block is robustly and
  cleanly scoped.
5. **Enormous Length and Exacting Fidelity Depth:** The final
  resulting HTML payload delivery must be absolutely massive,
  stunningly extensive, and instantly production-ready straight out of
  the box.
-    Ensure it exceeds 700 to 1200+ detailed lines of high-quality
  code.
-    It is absolutely paramount that you natively reflect and capture
  the complete, unrelenting premium fidelity atmosphere of the
  described "Glo UI".

## Critical Developer Notes: Security & Operations Focus

**Scenario Details:**
This UI is not for casual consumer use; it represents an internal,
high-stakes military-grade or private-sector cybersecurity command
node. Therefore, the visual language must communicate unyielding
stability.

**Detailed SVG Integration Requirements:**
When constructing the SVG icons for the 'Arsenal' features, adhere
strictly to these architectural patterns:
- Use viewBox="0 0 24 24" consistently across all icons to ensure
  mathematical scaling.
- Utilize path data that builds sharp, acute geometric angles,
  avoiding overly soft or rounded consumer-style bubbles.
- Stroke widths (stroke-width) should remain precisely at 1.5 or 1 for
  that intricate, technical diagram look.
- Implement CSS classes explicitly on the SVG elements (e.g., .neon-
  icon-primary) to allow hover-state CSS variables to flawlessly
  transition the stroke or fill properties dynamically.
- For the animated radar, construct it using multiple superimposed
  circle layers wrapped in g tags. Use stroke-dasharray parameters to
  create dashed 'tracker' rings rotating independently of the sweeping
  gradient core.

**Advanced Layout Guidelines & Grid Matrices:**
The primary application main section should leverage a sophisticated
display: grid matrix.
- The grid-template-columns property must use repeat(12, 1fr) to
  provide a flawless 12-column foundation.
- For the main telemetry map section, grid-column: span 12 on mobile,
  but gracefully transition to grid-column: span 8 for the map,
  leaving span 4 for the active node side-panel.
- This creates structured visual tension, critical to dashboard
  design. Ensure gap: 1.5rem acts as the breathing room channel.

Maintain all specified structures exactly as provided. Deviation from
these detailed constraints will result in immediate rejection. Do not
simulate, output the entirety.

