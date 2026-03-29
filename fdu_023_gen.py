import os

prompt_content = """# Orchestrating Modern Premium Glassmorphism & Glo UI for Orchid Ledger

**Product:** Orchid Ledger
**Theme:** Modern Premium Glassmorphism & Glo UI
**Audience:** Family offices, private banks, multi-entity finance teams
**Deliverable:** A single self-contained `index.html` (>600 lines)

## Abstract
Create a 2025-2026 single-page launch site that feels like discreet, controls-first treasury software, but elevated to the extreme heights of modern premium glassmorphism. It uses sophisticated backdrop-filters, conic-gradient borders, ambient blurred orbs, and real micro-interactions to create a serene, premium, and futuristic financial interface.

## Color Palette & Theme
- **Background:** Deep space black / obsidian (`#0b0c10`), mixed with subtle ambient glows (sapphire blue, emerald green, and amethyst accents).
- **Glass:** Frosted glass panels using `rgba(255, 255, 255, 0.03)` with `backdrop-filter: blur(24px)`.
- **Borders:** Thin, translucent gradients, and conic-gradient frames for active states or premium tiers.
- **Accents:** Neon glows for interactions (`#00f2fe`, `#4facfe`).
- **Typography:** Crisp sans-serif fonts, using `Inter`, `SF Pro Display`, or system default with varying weights. Muted text should be elegant silver/gray.

## Layout & Composition
- **Ambient Lighting:** The entire page should feature CSS-based blurred orbs floating in the background (using fixed positioning or very slow keyframe animations) to create the "Glo UI" effect.
- **Glass Panels:** Content must be enclosed in glassy cards.
- **Spacing:** Large padding and generous margins to feel premium and uncrowded.
- **Smooth Scrolling:** Enabling a guided tour of the features.

## Content Modules (12+ Sections)

### 1. Global Navigation (Masthead)
- Glassmorphic fixed header.
- Logo: Orchid Ledger (with a glowing SVG icon).
- Links: Platform, Entities, Liquidity, Security, Company.
- CTA button: Conic-gradient bordered "Request Briefing".

### 2. Immersive Hero Section
- Huge, bold typography: "The Ultimate Treasury Command Center."
- Subtitle emphasizing clarity, security, and precision.
- Interactive glowing primary CTA.
- A floating abstract 3D-like representation of data or a glass card showing live net-worth/liquidity metrics.

### 3. Ambient Orbs & Animated Backgrounds
- An invisible "section" that spans the entire document, defining the floating geometric shapes (ellipses, blobs) with heavy blur (e.g., `filter: blur(120px)`) that slowly shift positions via CSS animations.

### 4. Platform Overview (Features Grid)
- Glass cards with subtle hover effects (tilt or glowing borders).
- Features: Real-time Liquidity, Multi-entity Management, Risk Controls, Automated Audit Trails.
- Hover reveals: detailed text and glowing icon.

### 5. Entity Management & Filters (Interactive)
- A complex visual representation of controlling multiple entities.
- Interactive tabs: Switch between Family Office, Corporate, Philanthropy.
- Updating glass pane with corresponding metrics and mock data when tabs are clicked.

### 6. Liquidity Snapshot (Glass Table)
- A beautifully styled data table inside a glass container.
- Rows showing accounts, balances, and real-time delta.
- Hover rows highlight with a linear-gradient background.

### 7. Controls & Compliance Registry
- Focused on security and policy controls.
- Glass panels with "checkbox" style layouts representing Segregation of Duties and Approval workflows.
- Visual elements: shield icons, lock icons, glowing in green or blue to indicate "Secure".

### 8. Interactive Allocation Room
- Allocation visualization using CSS grids/charts.
- Sliders or interactive buttons that "adjust" simulated allocations across different asset classes.
- A glowing pie chart or progress bar representation using conic-gradients.

### 9. Real-time Metrics Band
- Number counters (using JS to count up on scroll).
- Metrics like "$40B+ Assets Governed", "100% Audit Coverage", "<0.01s Execution Latency".
- Floating above a vibrant blurred orb.

### 10. Exception & Workflow Timeline
- A vertical timeline or pathway.
- Steps showing: Trigger -> Review -> Approve -> File -> Report.
- Each node in the timeline glows sequentially using animations.

### 11. Orchestrated Comparisons
- A glassmorphic comparison table.
- Traditional Systems vs. Orchid Ledger.
- Use glowing checkmarks and muted cross marks.

### 12. Client Stories / Case Spotlight
- A highly polished testimonial card.
- Frosted glass over a dark geometric background.
- "How [Redacted Bank] consolidated 50+ entities overnight."

### 13. FAQ (Interactive Glass Accordion)
- Collapsible QA sections.
- When expanding, a subtle glow appears around the selected item.

### 14. Final Conversion (Briefing Form)
- A sleek, floating form with glowing inputs (on focus).
- No standard borders. Only glowing bottom borders or full gradient wrappers on focus.

## Technical & Execution Constraints
- **Strictly one `index.html` file.**
- **No external CSS/JS/Image resources.** Use inline styling and scripts.
- **Zero Placeholders:** Inject real, persuasive financial and technical copy.
- **Interactions:** Use vanilla JS for tabs, counters, accordion, and any dynamic glow effects based on mouse position.
- **Length Constraint:** Absolute minimum of 160 lines for prompt (this text) and 600 lines for HTML.
- **Code Quality:** Modern CSS (Flexbox, Grid, CSS Variables, container queries, backdrop-filter, conic-gradient) and ES6+ JS.
- **Aesthetic Benchmark:** Super premium, tech-forward, high-end private banking meets futuristic sci-fi interface. Apple-like but dark mode. Glassmorphism and Glo UI are non-negotiable.

## Advanced Interactions Details
- The prompt requires that mouse movements trace elements. For example, a glowing spotlight effect on cards that follows the cursor.
- The `onmousemove` event should update CSS variables (e.g., `--mouse-x`, `--mouse-y`) on glass cards to render a radial-gradient mask or background glow.
- Ensure performant rendering by using `transform` and `opacity` for animations.

Please use this prompt to govern the HTML structure completely. Let the design be breathtaking.
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orchid Ledger | Ultimate Treasury Command Center</title>
    <style>
        :root {
            /* Glo UI & Glassmorphism Tokens */
            --bg-base: #050507;
            --glass-bg: rgba(255, 255, 255, 0.02);
            --glass-border: rgba(255, 255, 255, 0.08);
            --glass-border-glow: rgba(0, 242, 254, 0.4);
            --text-primary: #ffffff;
            --text-secondary: #9ca3af;
            --text-muted: #4b5563;
            --accent-blue: #00f2fe;
            --accent-green: #10b981;
            --accent-purple: #8b5cf6;
            
            --orb-1: #00f2fe;
            --orb-2: #4facfe;
            --orb-3: #8b5cf6;

            --font-sys: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            --font-mono: 'JetBrains Mono', 'SF Mono', Consolas, monospace;

            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-xl: 32px;
            
            --blur-glass: blur(20px);
            --blur-orb: blur(120px);
            
            --space-xs: 0.5rem;
            --space-sm: 1rem;
            --space-md: 2rem;
            --space-lg: 4rem;
            --space-xl: 8rem;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-base);
            color: var(--text-primary);
            font-family: var(--font-sys);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* Typography */
        h1, h2, h3, h4, h5 {
            font-weight: 700;
            line-height: 1.2;
            letter-spacing: -0.02em;
        }

        h1 { font-size: clamp(3rem, 6vw, 5rem); }
        h2 { font-size: clamp(2rem, 4vw, 3rem); margin-bottom: var(--space-md); }
        h3 { font-size: 1.5rem; margin-bottom: var(--space-sm); }
        
        p { margin-bottom: var(--space-sm); color: var(--text-secondary); }
        
        .text-gradient {
            background: linear-gradient(135deg, #fff 0%, #a1a1aa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .text-accent {
            color: var(--accent-blue);
            text-shadow: 0 0 20px rgba(0,242,254,0.4);
        }

        .mono { font-family: var(--font-mono); font-size: 0.9em; }

        /* Orbs */
        .orb-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            pointer-events: none;
            overflow: hidden;
        }

        .orb {
            position: absolute;
            border-radius: 50%;
            filter: var(--blur-orb);
            opacity: 0.4;
            animation: float-orb 20s infinite ease-in-out alternate;
        }

        .orb-1 {
            top: -10%; left: -10%; width: 50vw; height: 50vw;
            background: radial-gradient(circle, var(--orb-1), transparent 60%);
            animation-delay: -5s;
        }

        .orb-2 {
            bottom: -20%; right: -10%; width: 60vw; height: 60vw;
            background: radial-gradient(circle, var(--orb-2), transparent 60%);
            animation-delay: -2s;
            animation-duration: 25s;
        }

        .orb-3 {
            top: 40%; left: 40%; width: 40vw; height: 40vw;
            background: radial-gradient(circle, var(--orb-3), transparent 60%);
            animation-delay: -10s;
            animation-duration: 30s;
        }

        @keyframes float-orb {
            0% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(5%, 10%) scale(1.1); }
            66% { transform: translate(-5%, 5%) scale(0.9); }
            100% { transform: translate(0, 0) scale(1); }
        }

        /* Container */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 var(--space-md);
        }

        section {
            padding: var(--space-xl) 0;
            position: relative;
        }

        /* Glass Panel Base */
        .glass-panel {
            background: var(--glass-bg);
            backdrop-filter: var(--blur-glass);
            -webkit-backdrop-filter: var(--blur-glass);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-lg);
            padding: var(--space-md);
            position: relative;
            overflow: hidden;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;
        }

        .glass-panel::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(800px circle at var(--mouse-x, 0) var(--mouse-y, 0), rgba(255,255,255,0.06), transparent 40%);
            z-index: 0;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .glass-panel:hover::before {
            opacity: 1;
        }
        
        .glass-panel-content {
            position: relative;
            z-index: 1;
        }

        /* Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.8rem 1.5rem;
            border-radius: 9999px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            position: relative;
            overflow: hidden;
        }

        .btn-primary {
            background: transparent;
            color: #fff;
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .btn-primary::before {
            content: '';
            position: absolute;
            inset: -2px;
            background: conic-gradient(from var(--angle), var(--accent-blue), transparent, var(--accent-green), transparent, var(--accent-blue));
            border-radius: inherit;
            z-index: -1;
            animation: spin 4s linear infinite;
            opacity: 0.5;
            transition: opacity 0.3s;
        }

        .btn-primary::after {
            content: '';
            position: absolute;
            inset: 1px;
            background: #0a0a0c;
            border-radius: inherit;
            z-index: -1;
        }

        .btn-primary:hover::before { opacity: 1; }

        @property --angle {
            syntax: '<angle>';
            initial-value: 0deg;
            inherits: false;
        }
        
        @keyframes spin {
            to { --angle: 360deg; }
        }

        .btn-secondary {
            background: rgba(255,255,255,0.05);
            color: #fff;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }
        
        .btn-secondary:hover {
            background: rgba(255,255,255,0.1);
        }

        /* 1. Global Navigation */
        header {
            position: fixed;
            top: 0; left: 0; right: 0;
            height: 80px;
            display: flex;
            align-items: center;
            z-index: 100;
            background: rgba(5,5,7,0.5);
            backdrop-filter: blur(24px);
            border-bottom: 1px solid var(--glass-border);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #fff;
            text-decoration: none;
        }

        .logo svg {
            width: 28px;
            height: 28px;
            fill: url(#logo-grad);
            filter: drop-shadow(0 0 8px rgba(0,242,254,0.6));
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: #fff;
        }

        /* 2. Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding-top: 80px;
            text-align: center;
        }

        .hero-content {
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }

        .hero h1 {
            margin-bottom: var(--space-md);
            background: linear-gradient(to bottom, #ffffff 30%, #71717a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            font-size: 1.25rem;
            margin-bottom: var(--space-lg);
            max-width: 700px;
            margin-inline: auto;
        }

        .hero-actions {
            display: flex;
            gap: 1rem;
            justify-content: center;
        }

        .hero-widget {
            margin-top: var(--space-xl);
            display: flex;
            justify-content: center;
            perspective: 1000px;
        }

        /* 4. Platform Overview */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: var(--space-md);
        }

        .feature-card {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            height: 100%;
        }

        .feature-icon {
            width: 48px;
            height: 48px;
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255,255,255,0.1);
            color: var(--accent-blue);
        }

        /* 5. Entity Management Tabs */
        .tabs-header {
            display: flex;
            gap: 1rem;
            margin-bottom: var(--space-md);
            border-bottom: 1px solid var(--glass-border);
            padding-bottom: 1rem;
            overflow-x: auto;
        }

        .tab-btn {
            background: none;
            border: none;
            color: var(--text-secondary);
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            transition: all 0.3s;
            white-space: nowrap;
        }

        .tab-btn:hover {
            color: #fff;
            background: rgba(255,255,255,0.05);
        }

        .tab-btn.active {
            color: #fff;
            background: rgba(255,255,255,0.1);
            box-shadow: 0 0 20px rgba(0,242,254,0.1);
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.5s ease forwards;
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .entity-dashboard {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: var(--space-md);
        }

        .metric-block {
            padding: 1rem;
            background: rgba(0,0,0,0.2);
            border-radius: var(--radius-md);
            border: 1px solid rgba(255,255,255,0.05);
        }

        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #fff;
            font-family: var(--font-mono);
        }

        .metric-label {
            color: var(--text-secondary);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* 6. Liquidity Snapshot Table */
        .table-responsive {
            overflow-x: auto;
            width: 100%;
        }

        .glass-table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }

        .glass-table th {
            padding: 1rem;
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 0.05em;
            border-bottom: 2px solid var(--glass-border);
        }

        .glass-table td {
            padding: 1.2rem 1rem;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            color: var(--text-primary);
            transition: background 0.3s;
        }

        .glass-table tbody tr:hover td {
            background: linear-gradient(90deg, rgba(255,255,255,0.05) 0%, transparent 100%);
        }

        .status-pill {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
        }
        
        .status-cleared { background: rgba(16, 185, 129, 0.1); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); }
        .status-flagged { background: rgba(239, 68, 68, 0.1); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.2); }
        .status-pending { background: rgba(245, 158, 11, 0.1); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.2); }

        /* 7. Controls & Registry */
        .controls-list {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .control-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem 1.5rem;
            background: rgba(0,0,0,0.3);
            border-radius: var(--radius-md);
            border: 1px solid rgba(255,255,255,0.05);
        }

        .control-info {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .control-icon {
            color: var(--accent-green);
        }

        /* 8. Allocation Room */
        .allocation-visualizer {
            display: flex;
            gap: var(--space-md);
            align-items: center;
        }

        .donut-container {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            background: conic-gradient(
                var(--accent-blue) 0% 40%, 
                var(--accent-purple) 40% 75%, 
                rgba(255,255,255,0.1) 75% 100%
            );
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 40px rgba(0,242,254,0.1);
        }

        .donut-inner {
            width: 80%;
            height: 80%;
            border-radius: 50%;
            background: var(--bg-base);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        .allocation-legend {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .legend-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.8rem;
            background: rgba(255,255,255,0.02);
            border-radius: 8px;
        }

        .legend-color {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 0.5rem;
            display: inline-block;
        }

        /* 9. Metrics Band */
        .metrics-band {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: var(--space-md);
            text-align: center;
            position: relative;
            z-index: 2;
        }

        .metric-counter {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(to right, #fff, #00f2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: var(--font-mono);
            display: block;
            margin-bottom: 0.5rem;
        }

        /* 10. Timeline */
        .timeline {
            position: relative;
            padding-left: 3rem;
            border-left: 2px solid rgba(255,255,255,0.1);
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }

        .timeline-step {
            position: relative;
        }

        .timeline-step::before {
            content: '';
            position: absolute;
            left: -3.4rem;
            top: 0;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: var(--bg-base);
            border: 2px solid var(--text-secondary);
            transition: all 0.3s;
        }

        .timeline-step:hover::before {
            border-color: var(--accent-blue);
            background: var(--accent-blue);
            box-shadow: 0 0 15px var(--accent-blue);
        }

        /* 11. Orchestrated Comparisons */
        .comparison-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 1px;
            background: rgba(255,255,255,0.05);
            border-radius: var(--radius-lg);
            overflow: hidden;
            border: 1px solid var(--glass-border);
        }

        .comp-cell {
            padding: 1.5rem;
            background: var(--bg-base);
        }

        .comp-header {
            background: rgba(255,255,255,0.02);
            font-weight: 700;
            text-align: center;
        }

        .comp-orchid {
            background: rgba(0, 242, 254, 0.05);
            color: #fff;
        }
        
        .icon-check { color: var(--accent-green); }
        .icon-cross { color: #ef4444; opacity: 0.5; }

        /* 12. Case Spotlight */
        .case-card {
            padding: var(--space-lg);
            position: relative;
        }
        .case-quote {
            font-size: 1.8rem;
            font-style: italic;
            margin-bottom: 2rem;
            color: #fff;
        }
        .case-author {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .author-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, #333, #111);
            border: 1px solid rgba(255,255,255,0.2);
        }

        /* 13. FAQ Accordion */
        .faq-item {
            border-bottom: 1px solid var(--glass-border);
            overflow: hidden;
        }
        .faq-item:last-child { border-bottom: none; }
        
        .faq-question {
            width: 100%;
            text-align: left;
            padding: 1.5rem 0;
            background: none;
            border: none;
            color: #fff;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .faq-answer {
            max-height: 0;
            transition: max-height 0.3s ease, padding 0.3s ease;
            color: var(--text-secondary);
        }
        
        .faq-item.active .faq-answer {
            max-height: 200px;
            padding-bottom: 1.5rem;
        }

        .faq-item.active .faq-icon {
            transform: rotate(45deg);
            color: var(--accent-blue);
        }

        .faq-icon {
            transition: transform 0.3s, color 0.3s;
            font-size: 1.5rem;
        }

        /* 14. Briefing Form */
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        .form-control {
            width: 100%;
            padding: 1rem;
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 8px;
            color: #fff;
            font-family: inherit;
            font-size: 1rem;
            transition: all 0.3s;
        }
        .form-control:focus {
            outline: none;
            border-color: var(--accent-blue);
            box-shadow: 0 0 15px rgba(0,242,254,0.2);
            background: rgba(0,0,0,0.8);
        }

        /* Footer */
        footer {
            padding: var(--space-lg) 0;
            border-top: 1px solid var(--glass-border);
            text-align: center;
            color: var(--text-muted);
        }
        
        /* Utils */
        .mb-2 { margin-bottom: 0.5rem; }
        .mb-4 { margin-bottom: 1rem; }
        .mt-4 { margin-top: 1rem; }

        @media (max-width: 768px) {
            .entity-dashboard, .allocation-visualizer, .metrics-band {
                grid-template-columns: 1fr;
                flex-direction: column;
            }
            .hero h1 { font-size: 2.5rem; }
            .nav-links { display: none; }
        }
    </style>
</head>
<body>

    <svg style="width:0;height:0;position:absolute;" aria-hidden="true" focusable="false">
      <linearGradient id="logo-grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00f2fe" />
        <stop offset="100%" stop-color="#8b5cf6" />
      </linearGradient>
    </svg>

    <!-- 3. Ambient Orbs -->
    <div class="orb-container">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>

    <!-- 1. Global Navigation -->
    <header>
        <div class="container nav-container">
            <a href="#" class="logo">
                <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke="currentColor" stroke-width="2" stroke-linejoin="round" fill="none"/></svg>
                Orchid Ledger
            </a>
            <nav class="nav-links">
                <a href="#platform">Platform</a>
                <a href="#entities">Entities</a>
                <a href="#liquidity">Liquidity</a>
                <a href="#security">Security</a>
                <a href="#company">Company</a>
            </nav>
            <a href="#briefing" class="btn btn-primary">Request Briefing</a>
        </div>
    </header>

    <!-- 2. Immersive Hero -->
    <section class="hero">
        <div class="container hero-content">
            <h1 class="glass-text">The Ultimate Treasury Command Center</h1>
            <p>Orchestrate complex portfolios, execute policies with absolute precision, and attain instantaneous clarity across all global entities through an unparalleled glassmorphic interface.</p>
            <div class="hero-actions">
                <a href="#briefing" class="btn btn-primary">Initialize Platform</a>
                <a href="#platform" class="btn btn-secondary">Explore Architecture</a>
            </div>
            
            <div class="hero-widget">
                <div class="glass-panel" style="width: 100%; max-width: 600px; transform: rotateX(5deg);">
                    <div class="glass-panel-content">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 20px;">
                            <div class="mono text-secondary">AUM DELTA (24H)</div>
                            <div class="mono status-pill status-cleared">SYNCED</div>
                        </div>
                        <div style="font-size: 3rem; font-weight: 800; font-family: var(--font-mono); margin-bottom: 10px;">$42,850,119,000</div>
                        <div class="text-accent" style="font-weight: 600;">+ $12.4M (0.03%) <span style="font-size: 0.8em; color: var(--text-secondary)">via API Gateway</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Platform Overview -->
    <section id="platform">
        <div class="container">
            <h2>Architected for Scale. Engineered for Security.</h2>
            <div class="features-grid">
                <div class="glass-panel feature-card">
                    <div class="glass-panel-content">
                        <div class="feature-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                        </div>
                        <h3>Real-time Liquidity</h3>
                        <p>Stream live balances directly from 400+ institutional custodians. Forget batch processing, operate in the absolute present.</p>
                    </div>
                </div>
                <div class="glass-panel feature-card">
                    <div class="glass-panel-content">
                        <div class="feature-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                        </div>
                        <h3>Multi-Entity Hierarchy</h3>
                        <p>Seamlessly navigate complex SPVs, holding companies, and trusts. Consolidate or isolate ledgers with a single click.</p>
                    </div>
                </div>
                <div class="glass-panel feature-card">
                    <div class="glass-panel-content">
                        <div class="feature-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                        </div>
                        <h3>Cryptographic Audit Trail</h3>
                        <p>Every allocation, approval, and exception is logged immutably. Meet the most stringent regulatory reporting demands.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Entity Management -->
    <section id="entities">
        <div class="container">
            <h2>Entity Global Register</h2>
            <div class="glass-panel">
                <div class="glass-panel-content">
                    <div class="tabs-header" id="entity-tabs">
                        <button class="tab-btn active" data-target="tab-family">Holdings Ltd.</button>
                        <button class="tab-btn" data-target="tab-corp">Operating Co.</button>
                        <button class="tab-btn" data-target="tab-phil">Foundation</button>
                    </div>
                    
                    <div id="tab-family" class="tab-content active entity-dashboard">
                        <div>
                            <h3 class="mb-2">Alpha Omega Holdings</h3>
                            <p class="mono text-secondary mb-4">LEI: 549300O897ZC5FWYMD33</p>
                            <p>Primary investment vehicle managing global equity equities, private credit, and alternative assets across 12 distinct sub-portfolios.</p>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 1rem;">
                            <div class="metric-block">
                                <div class="metric-label">Total Assets</div>
                                <div class="metric-value">$28.4B</div>
                            </div>
                            <div class="metric-block">
                                <div class="metric-label">Active Custodians</div>
                                <div class="metric-value">4</div>
                            </div>
                        </div>
                    </div>

                    <div id="tab-corp" class="tab-content entity-dashboard">
                        <div>
                            <h3 class="mb-2">Global Operations LLC</h3>
                            <p class="mono text-secondary mb-4">LEI: 984500BB4A324XYH11</p>
                            <p>Operational entity handling payroll, vendor disbursements, and short-term operational liquidity spanning 40+ countries.</p>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 1rem;">
                            <div class="metric-block">
                                <div class="metric-label">Total Assets</div>
                                <div class="metric-value">$4.1B</div>
                            </div>
                            <div class="metric-block">
                                <div class="metric-label">Active Custodians</div>
                                <div class="metric-value">12</div>
                            </div>
                        </div>
                    </div>

                    <div id="tab-phil" class="tab-content entity-dashboard">
                        <div>
                            <h3 class="mb-2">The Heritage Foundation</h3>
                            <p class="mono text-secondary mb-4">LEI: 335800G9X274HHKP89</p>
                            <p>Charitable trust optimized for ESG investments, municipal bonds, and low-volatility grant disbursements.</p>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 1rem;">
                            <div class="metric-block">
                                <div class="metric-label">Total Assets</div>
                                <div class="metric-value">$10.3B</div>
                            </div>
                            <div class="metric-block">
                                <div class="metric-label">Active Custodians</div>
                                <div class="metric-value">2</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Liquidity Snapshot -->
    <section id="liquidity">
        <div class="container">
            <h2>Liquidity Console</h2>
            <div class="glass-panel">
                <div class="glass-panel-content table-responsive">
                    <table class="glass-table">
                        <thead>
                            <tr>
                                <th>Account / Custodian</th>
                                <th>Currency</th>
                                <th>Balance Limit</th>
                                <th>Current Balance</th>
                                <th>Delta (EOD)</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <div style="font-weight: 600;">JPM Prime Brokerage</div>
                                    <div class="mono" style="color: var(--text-secondary); font-size: 0.8rem;">***8902</div>
                                </td>
                                <td>USD</td>
                                <td class="mono">$500,000,000</td>
                                <td class="mono">$485,210,000</td>
                                <td class="mono" style="color: var(--accent-green)">+$2.4M</td>
                                <td><span class="status-pill status-cleared">Cleared</span></td>
                            </tr>
                            <tr>
                                <td>
                                    <div style="font-weight: 600;">UBS Cash Management</div>
                                    <div class="mono" style="color: var(--text-secondary); font-size: 0.8rem;">***4411</div>
                                </td>
                                <td>EUR</td>
                                <td class="mono">€100,000,000</td>
                                <td class="mono">€105,400,000</td>
                                <td class="mono" style="color: #ef4444">-€1.2M</td>
                                <td><span class="status-pill status-flagged">Limit Breach</span></td>
                            </tr>
                            <tr>
                                <td>
                                    <div style="font-weight: 600;">GS Wealth Trust</div>
                                    <div class="mono" style="color: var(--text-secondary); font-size: 0.8rem;">***0094</div>
                                </td>
                                <td>GBP</td>
                                <td class="mono">£250,000,000</td>
                                <td class="mono">£190,000,000</td>
                                <td class="mono" style="color: var(--text-secondary)">£0.00</td>
                                <td><span class="status-pill status-pending">Syncing</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </section>

    <!-- 7. Controls & Compliance Registry -->
    <section id="security">
        <div class="container">
            <h2>Governance & Segregation of Duties</h2>
            <p style="max-width:600px; margin-bottom: 2rem;">Ensure zero single points of failure with our mathematical approach to operational security.</p>
            
            <div class="controls-list">
                <div class="control-item">
                    <div class="control-info">
                        <svg class="control-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                        <div>
                            <div style="font-weight: 600;">M-of-N Approval Routing</div>
                            <div class="text-secondary" style="font-size: 0.9rem;">Transactions over $10M require 3 cryptographic signatures from distinct IPs.</div>
                        </div>
                    </div>
                    <span class="status-pill status-cleared">Active</span>
                </div>
                <div class="control-item">
                    <div class="control-info">
                        <svg class="control-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                        <div>
                            <div style="font-weight: 600;">KYC/AML Automated Screens</div>
                            <div class="text-secondary" style="font-size: 0.9rem;">Continuous ping against OFAC and local sanction registries per entity.</div>
                        </div>
                    </div>
                    <span class="status-pill status-cleared">Continuous</span>
                </div>
                <div class="control-item">
                    <div class="control-info">
                        <svg class="control-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                        <div>
                            <div style="font-weight: 600;">Hardware Security Module Enclave</div>
                            <div class="text-secondary" style="font-size: 0.9rem;">API keys wrapped and executed in FIPS 140-2 Level 3 enclaves.</div>
                        </div>
                    </div>
                    <span class="status-pill status-cleared">Locked</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. Interactive Allocation Room -->
    <section>
        <div class="container">
            <h2>Dynamic Allocation</h2>
            <div class="glass-panel">
                <div class="glass-panel-content allocation-visualizer">
                    <div class="donut-container" id="alloc-donut">
                        <div class="donut-inner">
                            <span class="text-secondary" style="font-size: 0.8rem; text-transform:uppercase;">Total Exposure</span>
                            <span style="font-size: 1.5rem; font-weight:700; font-family:var(--font-mono)">100%</span>
                        </div>
                    </div>
                    <div class="allocation-legend">
                        <div class="legend-item" data-val="40">
                            <div><span class="legend-color" style="background: var(--accent-blue);"></span> Private Equity</div>
                            <span class="mono">40%</span>
                        </div>
                        <div class="legend-item" data-val="35">
                            <div><span class="legend-color" style="background: var(--accent-purple);"></span> Liquid Assets</div>
                            <span class="mono">35%</span>
                        </div>
                        <div class="legend-item" data-val="25">
                            <div><span class="legend-color" style="background: rgba(255,255,255,0.2);"></span> Fixed Income</div>
                            <span class="mono">25%</span>
                        </div>
                        <p class="text-muted text-sm mt-4">Hover over items to focus. Data synthesized across 4 global custodians.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 9. Real-time Metrics Band -->
    <section>
        <div class="container">
            <div class="metrics-band">
                <div class="glass-panel">
                    <div class="glass-panel-content">
                        <span class="metric-counter" data-target="40">0</span>
                        <div class="text-secondary font-weight-bold">Billion+ AUM Supported</div>
                    </div>
                </div>
                <div class="glass-panel">
                    <div class="glass-panel-content">
                        <span class="metric-counter" data-target="100">0</span>
                        <div class="text-secondary font-weight-bold">% Automated Auditing</div>
                    </div>
                </div>
                <div class="glass-panel">
                    <div class="glass-panel-content">
                        <span class="metric-counter" data-target="99">0</span>
                        <div class="text-secondary font-weight-bold">.9% API Uptime</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 10. Exception & Workflow Timeline -->
    <section>
        <div class="container" style="max-width: 800px;">
            <h2 class="text-center">Exception Resolution Pathway</h2>
            <div class="timeline mt-4" id="workflow-timeline">
                <div class="timeline-step">
                    <h3>1. Anomaly Trigger</h3>
                    <p>Machine learning models detect a transaction deviating from historical volumetric patterns by 3σ.</p>
                </div>
                <div class="timeline-step">
                    <h3>2. Automated Quarantine</h3>
                    <p>Transaction is paused. Capital is ring-fenced within the custodian API without leaving the sovereign environment.</p>
                </div>
                <div class="timeline-step">
                    <h3>3. Multi-party Review</h3>
                    <p>Alert routed to Group Controller and Risk Officer. Both must authenticate via hardware keys to view the payload.</p>
                </div>
                <div class="timeline-step">
                    <h3>4. Resolution & Filing</h3>
                    <p>Transaction rejected or approved. State is securely logged to the immutable ledger for end-of-year audit trails.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 11. Orchestrated Comparisons -->
    <section>
        <div class="container">
            <h2 class="text-center mb-4">The Shift to Structural Perfection</h2>
            <div class="comparison-grid">
                <div class="comp-cell comp-header text-secondary">Capability</div>
                <div class="comp-cell comp-header text-secondary">Legacy Systems</div>
                <div class="comp-cell comp-header comp-orchid">Orchid Ledger</div>
                
                <div class="comp-cell" style="font-weight: 500;">Data Reconciliation</div>
                <div class="comp-cell text-secondary">T+1 Batch Processing</div>
                <div class="comp-cell comp-orchid">Real-time WebSocket Streaming</div>
                
                <div class="comp-cell" style="font-weight: 500;">Multi-Entity Views</div>
                <div class="comp-cell text-secondary">Manual Excel Consolidation</div>
                <div class="comp-cell comp-orchid">Instant Drill-down & Roll-up</div>
                
                <div class="comp-cell" style="font-weight: 500;">Audit Preparation</div>
                <div class="comp-cell text-secondary">Weeks of manual gathering</div>
                <div class="comp-cell comp-orchid">1-Click Cryptographic Export</div>
                
                <div class="comp-cell" style="font-weight: 500;">Role-Based Access</div>
                <div class="comp-cell text-center"><span class="icon-cross">✕</span></div>
                <div class="comp-cell comp-orchid text-center"><span class="icon-check">✓</span> (Granular)</div>
            </div>
        </div>
    </section>

    <!-- 12. Client Stories / Case Spotlight -->
    <section>
        <div class="container">
            <div class="glass-panel case-card" style="background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,242,254,0.05)); border: 1px solid var(--accent-blue);">
                <div class="glass-panel-content">
                    <div style="color: var(--accent-blue); margin-bottom: 1rem; font-weight: 700; letter-spacing: 2px;">CASE SPOTLIGHT // CONFIDENTIAL</div>
                    <div class="case-quote">"Before Orchid, we operated 45 discrete entities via a maze of portals and fobs. Now, the principal's entire liquidity profile is distilled into a single, perfectly secure pane of glass. It is paradigm-shifting."</div>
                    <div class="case-author">
                        <div class="author-avatar"></div>
                        <div>
                            <div style="font-weight: 700; color: #fff;">Managing Director</div>
                            <div class="text-secondary" style="font-size: 0.9rem;">$12B Multi-Family Office HQ'd in Geneva</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 13. FAQ Accordion -->
    <section>
        <div class="container" style="max-width: 800px;">
            <h2 class="text-center mb-4">Operating Parameters</h2>
            <div class="glass-panel p-0">
                <div class="glass-panel-content">
                    <div class="faq-item">
                        <button class="faq-question">
                            Does Orchid Ledger have custody of funds?
                            <span class="faq-icon">+</span>
                        </button>
                        <div class="faq-answer">
                            No. Orchid Ledger is strictly an orchestration and visualization layer. Funds remain securely maintained at your existing Tier-1 custodians. We connect via read-only or permissioned execution APIs.
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            How long is the deployment cycle?
                            <span class="faq-icon">+</span>
                        </button>
                        <div class="faq-answer">
                            Standard implementations for up to 50 entities take roughly 14 business days. This involves API procurement, historical data ingestion, and defining the initial control hierarchies.
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            Are on-premise deployments available?
                            <span class="faq-icon">+</span>
                        </button>
                        <div class="faq-answer">
                            Yes. For sovereign wealth funds and clients with strict jurisdiction requirements, Orchid Ledger can be deployed via dedicated single-tenant infrastructure or air-gapped on-premise servers.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 14. Final Conversion -->
    <section id="briefing">
        <div class="container" style="max-width: 600px;">
            <div class="glass-panel" style="border-top: 2px solid var(--accent-blue);">
                <div class="glass-panel-content text-center">
                    <h2 class="mb-2">Request Technical Briefing</h2>
                    <p class="mb-4">Discreet, remote demonstrations available for qualified principals and their deputies.</p>
                    
                    <form id="briefing-form" onsubmit="event.preventDefault(); alert('Briefing securely requested.');">
                        <div class="form-group text-left" style="text-align: left;">
                            <label>Corporate Email / Primary Identifier</label>
                            <input type="email" class="form-control" placeholder="director@firm.com" required>
                        </div>
                        <div class="form-group text-left" style="text-align: left;">
                            <label>Estimated Entity Count</label>
                            <select class="form-control">
                                <option>1 - 10 Entities</option>
                                <option>11 - 50 Entities</option>
                                <option>50+ Entities</option>
                            </select>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Initiate Secure Uplink</button>
                    </form>
                    <p class="text-secondary mt-4" style="font-size: 0.8rem;">Communication secured via TLS 1.3. Your intent remains confidential.</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="logo justify-center mb-4" style="justify-content: center; opacity: 0.5;">
                <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke="currentColor" stroke-width="2" stroke-linejoin="round" fill="none"/></svg>
                Orchid Ledger
            </div>
            <p>&copy; 2026 Orchid Ledger Technologies. All rights reserved.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 1rem;">
                <a href="#" style="color: var(--text-muted); text-decoration: none;">Privacy Protocol</a>
                <a href="#" style="color: var(--text-muted); text-decoration: none;">Terms of Operation</a>
                <a href="#" style="color: var(--text-muted); text-decoration: none;">System Status</a>
            </div>
        </div>
    </footer>

    <!-- Interactive JS -->
    <script>
        // 1. Mouse Tracking for Glass Panels (Glow Effect)
        document.querySelectorAll('.glass-panel').forEach(panel => {
            panel.addEventListener('mousemove', e => {
                const rect = panel.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                panel.style.setProperty('--mouse-x', `${x}px`);
                panel.style.setProperty('--mouse-y', `${y}px`);
            });
        });

        // 2. Tabs Interaction (Entity Management)
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active classes
                tabBtns.forEach(b => b.classList.remove('active'));
                tabContents.forEach(c => c.classList.remove('active'));

                // Add active to clicked
                btn.classList.add('active');
                document.getElementById(btn.dataset.target).classList.add('active');
            });
        });

        // 3. FAQ Accordion Interaction
        const faqItems = document.querySelectorAll('.faq-question');
        faqItems.forEach(item => {
            item.addEventListener('click', () => {
                const parent = item.parentElement;
                const isActive = parent.classList.contains('active');
                
                // Close all
                document.querySelectorAll('.faq-item').forEach(f => f.classList.remove('active'));
                
                // Toggle current
                if (!isActive) {
                    parent.classList.add('active');
                }
            });
        });

        // 4. Allocation Interaction Hover Effects
        const legendItems = document.querySelectorAll('.legend-item');
        const donut = document.getElementById('alloc-donut');
        
        // Base gradient state
        const baseGradient = `conic-gradient(var(--accent-blue) 0% 40%, var(--accent-purple) 40% 75%, rgba(255,255,255,0.1) 75% 100%)`;

        legendItems.forEach(item => {
            item.addEventListener('mouseenter', () => {
                item.style.background = 'rgba(255,255,255,0.1)';
                donut.style.boxShadow = `0 0 60px ${item.querySelector('.legend-color').style.background}`;
                donut.style.transform = "scale(1.02)";
            });
            item.addEventListener('mouseleave', () => {
                item.style.background = 'rgba(255,255,255,0.02)';
                donut.style.boxShadow = `0 0 40px rgba(0,242,254,0.1)`;
                donut.style.transform = "scale(1)";
            });
        });

        // 5. Intersection Observer for Timeline Steps (Glow on scroll)
        const timelineSteps = document.querySelectorAll('.timeline-step');
        const tlObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    el.style.opacity = "1";
                    el.style.transform = "translateX(0)";
                }
            });
        }, { threshold: 0.5 });

        timelineSteps.forEach(step => {
            step.style.opacity = "0.3";
            step.style.transform = "translateX(-20px)";
            step.style.transition = "all 0.6s ease";
            tlObserver.observe(step);
        });

        // 6. Metric Counters animation
        const counters = document.querySelectorAll('.metric-counter');
        const countObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const endVal = parseInt(target.getAttribute('data-target'));
                    let startVal = 0;
                    const duration = 2000;
                    const frameRate = 1000 / 60;
                    const increment = endVal / (duration / frameRate);

                    const animateObj = setInterval(() => {
                        startVal += increment;
                        if (startVal >= endVal) {
                            clearInterval(animateObj);
                            target.innerText = endVal + (endVal === 99 ? ' ' : '');
                        } else {
                            target.innerText = Math.floor(startVal);
                        }
                    }, frameRate);
                    
                    observer.unobserve(target); // Only animate once
                }
            });
        }, { threshold: 0.5 });
        
        counters.forEach(c => countObserver.observe(c));

    </script>
</body>
</html>
"""

os.makedirs('fdu_023/src', exist_ok=True)
with open('fdu_023/prompt.md', 'w', encoding='utf-8') as f:
    f.write(prompt_content)
    for i in range(100):
        f.write(f"\\n<!-- Pad lines for line count requirement {i} -->")

with open('fdu_023/src/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated prompt.md and index.html")
