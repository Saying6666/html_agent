## Round 1

Project: **Helio Harbor**
Type: electric dayboat club (members-only marina access, guided coastal routes, concierge provisioning, sunset work lounges)
Audience: members, concierge partners, small teams that want effortless coastal mobility
Timeframe: 2025-2026

Deliverable: generate one complete single-file index.html (>600 lines)

North star:
This must feel like a daylight-meets-sunset ultra-premium mobility brand.
Bright, glowing, hyper-modern, and fluid.
Target "Modern Premium Glassmorphism & Glo UI".

Visual world (commit to a specific Glassmorphism & Glow language):
Theme: Modern Premium Glassmorphism & Glo UI.
Backgrounds should feature ambient blurred orbs, subtle gradients that shift and float.
Surfaces should use backdrop-filter: blur(20px) and semi-transparent backgrounds.
Borders should feature conic-gradient or linear-gradient treatments.

Palette constraints:
- Base: obsidian or deep space blue overlaid with ambient glows.
- Orbs/Glows: cyan mist, magenta flare, sun gold, electric teal, and deep coral.
- Glass panels: semi-transparent black or white (depending on theme, let's go with dark glass for maximum glow impact).
- Highlights: electric cyan and hyper pink.
- Texts: crisp white, icy silver, and subtle translucent whites.

Material motifs:
- Frosted glass cards and panels.
- Conic-gradient borders to suggest precision-machined edges glowing with energy.
- Ambient blurred orbs (filter: blur(100px)) floating behind the glass layout.
- Glow-infused icons and typography.

Typography:
- Display: ultra-modern sans-serif, tight tracking, crisp weights.
- Body: highly readable geometric sans.
- Numbers: tabular, razor-sharp numerals for tides, range, and times.

Layout archetype (do not drift):
A hyper-modern digital terminal for coastal exploration.
Build at least 12 distinct sections with different structural logic:
Section 1: "Hero Halo" (full-bleed, huge glowing titles, ambient orbs, primary CTAs).
Section 2: "Marquee Strip" (scrolling or static metrics band, frosted glass backdrop).
Section 3: "Harbor Overview" (a macroscopic view of electric mobility, glowing accents).
Section 4: "Glass Fleet" (vessels presented as floating cards with conic borders and specs).
Section 5: "Tide & Transit Desk" (interactive console with Tabs).
Section 6: "Glow Map & Route Journal" (story entries + map-linked notes, inline-SVG glowing map).
Section 7: "Metrics Band" (Count-ups, nautical miles hosted, response time, glowing digits).
Section 8: "Concierge Module" (provisioning checklist and itinerary support, glowing list items).
Section 9: "Vantage Points" (gallery of coastal destinations, glass frames).
Section 10: "Membership Passes" (tiered passes inside premium frosted glass panes).
Section 11: "Club Rules & FAQ" (Accordion binder within a glowing container).
Section 12: "Final Departure" (Booking/inquiry form and final CTA banner within a massive glass enclosure).

Signature devices (must be obvious in the first viewport):
1) Ambient floating orbs in the background.
2) Frosted glass hero card.
3) A sun path or navigation tracker in glowing SVG.
All three must be built with pure CSS and inline SVG.
No stock imagery.

Design system requirements (CSS :root tokens, use consistently):
- background tokens: void black, deep indigo, orb-teal, orb-magenta.
- glass tokens: glass-surface, glass-surface-hover, glass-border.
- text tokens: pure-white, silver-haze, muted-glass, electric-teal.
- accent tokens: sun-gold, hyper-magenta.
- semantic status tokens: open-cyan, closed-red, waitlist-yellow.
- radii scale: 16px, 24px, 32px for glass surfaces.
- shadow scale: soft glowing drop-shadows.
- blur scale: backdrop-filter: blur(24px).
- spacing scale and content width tokens.
- type scale tokens for display/h1/h2/h3/body/label/fine print.
- motion tokens: transitions for hover states, floating animations.

Hard technical constraints (non-negotiable):
- Output one complete self-contained index.html (>600 lines)
- All CSS must be inside a single <style>
- All JS must be inside a single <script>
- Inline CSS/JS only
- No React, no Vue, no Svelte
- No GSAP, no jQuery, no external libraries
- No build step
- Do not reference local images, local fonts, local CSS, or local JS
- Do not reference external images or external fonts
- If visuals are needed, use pure CSS and inline SVG only
- Do not use style="" attributes in markup
- Keep the final HTML multi-line, readable, and maintainable
- NO PLACEHOLDERS. Fill all 12+ sections with real text.
- Wire all interactions (Tabs, Modals, Accordions, Toasts, Count-ups) with REAL JS in <script>.

Content coverage (ingredients, not a fixed page skeleton):
Include 12 substantial sections.
Reorder and reinterpret freely.
Avoid the generic landing-page silhouette.

Required Helio Harbor content blocks:
1) Skip link and accessible landmarks.
2) Sticky navbar, frosted glass, harbor status chip, primary CTA.
3) Hero section with animated ambient orbs behind a massive glass card.
4) Operations strip: marina hours, weather window, range.
5) Fleet showcase (3+ vessels).
6) Route map & journal.
7) Tide & Transit desk (Tabs for Live Tides, Weekly, Seasonal).
8) Metrics (count-ups).
9) Concierge section.
10) Membership passes.
11) FAQ (Accordion).
12) Footer with marina details, policies, accessibility.

You must embrace Glassmorphism, conic-gradient borders on cards (e.g. border-image: conic-gradient(...) 1; or pseudo-element approaches), ambient orbs (absolute positioning with mix-blend-mode or filter: blur()), and real micro-interactions (e.g., hover states that shift gradients).
No empty tags, no lorem ipsum. Write actual marketing copy for a premium electric dayboat club.
Write complete JS for tabs, accordions, count-ups, and an onboarding toast.
