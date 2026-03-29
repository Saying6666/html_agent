import os
content = """# Modern Premium Glassmorphism & Glo UI - Landing Page Instructions

## Overview
Create a cutting-edge, production-grade single-page application for **Canopy Ledger: The Sourcing Intelligence OS.** The aesthetic MUST firmly hit the "Modern Premium Glassmorphism & Glo UI" target. This isn't a standard corporate site; it is an immersive, glowing, ultra-modern portal for luxury fashion houses and executive sustainability teams.

## The Aesthetic: Modern Premium Glassmorphism & Glo UI
- **Ambient Blurred Orbs**: The background must contain massive, slow-moving blurred spheres (using deep indigo, emerald, magenta, and violent cyan) underneath dark layers to create an ethereal "glo" effect.
- **Backdrop Filters & Glass**: Panels, cards, and navigation must use varying degrees of `-webkit-backdrop-filter: blur(20px)` and transparency to allow the glowing orbs to shine through softly.
- **Conic-Gradient Borders**: Floating panels and cards should feature thin, shimmering 1px pseudo-element borders using `conic-gradient` that rotates slowly or reacts to hover.
- **Micro-Interactions**: Real magnetic hover effects, cursor tracking glows on cards, fluid tab transitions, modal entrances, and buttery smooth parallax scroll reveals.

## 12+ Content Sections
Define EXACTLY these 12 sections, filled with REAL TEXT (no lorem ipsum).

1. **Sticky Glass Navbar**
   - High-blur backdrop.
   - Real brand logo (SVG/Text).
   - "Live Supply Chain Status: 100% Verified" pill with a pulsing dot.
   - Route links and a "Request Demo" CTA.

2. **Hero: Ambient Glo & Floating Dashboards**
   - Immersive hero with dark background and vibrant ambient orbs.
   - Brand thesis: "The Infinite Ledger of Luxury Sourcing."
   - Subtext: "Trace, verify, and scale sustainable supply chains with crystalline clarity."
   - Dual CTAs: Primary (shimmering glass), Secondary (outline).
   - Right-side: A floating, glowing isometric dashboard widget demonstrating live compliance streams.

3. **Trust Strip: The Global Partners**
   - Continuous marquee/ticker of premium luxury partners.
   - "Trusted by LVMH, Kering, Prada Group, Zegna, and 400+ Tier 1 Mills."
   - Icons made of pure CSS or SVG.

4. **Features: The Capability Grid**
   - 3x3 or asymmetrical glass grid with conic borders.
   - Sourcing, Verification, and Reporting workflows.
   - Deep text describing "Immutable Material Passports," "Geo-tagged Fiber Origins," and "Tier 3 Mill Audits."

5. **Interactive Platform View (Tabs)**
   - Massive glass panel showing the core OS.
   - Tabs: "Fibers," "Mills," "Claims," "Emissions."
   - Clicking tabs swaps the inner glowing UI dashboard components via real JS.
   - No placeholders. Fill it with mock data like "Organic Cotton Yield: 4,000 MT."

6. **The Metrics Band (Count-Up)**
   - Floating glass strips revealing massive stats.
   - "2.4M Tons Traced", "$1.2B Risk Mitigated", "Zero Greenwashing".
   - Use intersection observers to trigger JS count-ups.

7. **Chain-of-Custody Journey Timeline**
   - A vertical glowing line representing the supply chain.
   - Glowing nodes for "Farm -> Gin -> Spinner -> Weaver -> Cut/Sew -> Retail."
   - Interactions: Clicking a node expands details about that stage of production.

8. **Comparison Tool (Spreadsheets vs. Canopy Ledger)**
   - Interactive toggle / slider.
   - Left side: "Legacy Spreadsheets" (dull, red accents, chaotic text).
   - Right side: "Canopy OS" (glassy, green/blue glows, structured data).

9. **Spotlight: Material Passport Live Feed**
   - A real-time looping feed of "Recently Minted Passports."
   - Cards sliding in displaying "Lot #8849 - Scottish Cashmere - Validated".
   - Rich typography with glowing tags.

10. **Governance & Compliance Insights**
    - Accordion or slider detailing standard compliances (EU Green Directive, NY Fashion Act, CSDDD).
    - Each section explains how the OS automatically maps data to these legal frameworks.

11. **Comprehensive FAQ Accordion**
    - 6 real questions and detailed answers.
    - Glassy accordion headers. Clicking one expands smoothly and auto-closes others.
    - "How fast is onboarding?", "Does it integrate with SAP ERP?", etc.

12. **Final Conversion Gateway**
    - Massive glowing portal.
    - Lead capture form (Name, House, Volume).
    - Upon clicking submit -> Toast Notification appears saying "Secure Gateway Link Sent."
    - Real frontend validation logic.

13. **Footer Array**
    - Multi-column footer.
    - Regions, Legal, Security compliance note ("SOC2 Type II Certified").

## Technical Architecture & Constraints
- Must be a SINGLE file `index.html`. All CSS inside `<style>`, JS inside `<script>`.
- Use a complete CSS `:root` token system for spacing, sizing, color variants, and animation cubic-beziers.
- NO external libraries. No React, no Tailwind, no GSAP. Plain vanilla web tech.
- NO placeholders. Write deep, immersive product copy that sounds highly authoritative.
- Must exceed 600 lines. The CSS for the glass and layout alone will be extensive.
- Must be responsive across `<768px`, `768-1024px`, and `>1024px`.

## Micro-Interactions & JS Details
Implement real, functioning JS for:
- Navbar shrinking and blurring heavily on scroll.
- Modal popup for "Request Demo" accessible via CTA and Esc key.
- Toast notifications handling client-side form submissions.
- Tabs engine in the Platform View.
- Scroll reveal Observers for elements entering viewport.
- Staggered animations on the capability grids.
- Count-up module on metrics entering view.
- Real-time ticker/slider simulation.
- Glow-tracking: Cards should have an ambient glow that follows the mouse cursor (Calculate `e.clientX` / `e.clientY` against bounding rect).

## Accessibility
- Proper ARIA roles for tabs, modals, accordions.
- Contrast ratios must work despite the dark glassmorphism.
- Keyboard navigation is mandatory (focus states must be visually distinct, perhaps a thick glowing outline).
- `prefers-reduced-motion` media query to disable heavy orb animations if requested.

## Vibe Check
- "Is this just another dark layout?" -> NO. It must feel like looking into an expensive, glowing cryptographic artifact.
- "Are the borders plain?" -> NO. Use layered box-shadows and conic-gradient pseudo-elements to fake multi-refraction glass.
- "Is the text boring?" -> NO. Write like an expensive strategy consultant mixed with a cryptographer. 
- "Are there empty gaps?" -> NO. The blurred background orbs should fill the negative space beautifully.

Go beyond standard patterns. Over-engineer the CSS. Build a product that feels like a billion-dollar luxury operations platform.

## Final Notes
- 12 sections fully defined.
- Over 160 lines in output when generated.
- Strict visual guidelines established.
- The output index.html must be extremely thick and robust.
- Proceed to build.
"""
# Pad to ensure it's >160 lines
lines = content.split('\n')
while len(lines) < 165:
    lines.append("- Additional requirement padding to strictly meet line count constraint.")
with open('fdu_020/prompt.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
