import os

prompt_content = """# BentoLingo - Enterprise Language Readiness Platform (Premium Glassmorphism & Glo UI)

## Overview
Design and implement a production-grade single-file website for **BentoLingo**, an enterprise language readiness platform for globally distributed teams. The target aesthetic is "Modern Premium Glassmorphism & Glo UI". The user experience should feel like an executive-ready instrument panel and rollout planner: measurable, credible, operational, and calm with highly sophisticated visual fidelity.

## Technical Constraints (Non-negotiable)
- Single self-contained index.html file (placed in src/index.html).
- All CSS strictly inside <style> and JavaScript inside <script>.
- Fully inline code ¡ª NO build steps.
- ZERO external dependencies (no React, Vue, jQuery, Tailwind CDN, Bootstrap, FontAwesome, etc.).
- NO external assets like web fonts (use native system fonts), local images, or external scripts.
- No inline style="" attributes.
- Use raw vanilla JavaScript and semantic HTML5 natively.

## Design System: Modern Premium Glassmorphism & Glo UI
- **Color Palette & Glo Effects:**
  - Background: Deep, immersive dark space (#0a0a0f).
  - Ambient Orbs: Large blurred, slow-moving radial gradients (cyan, purple, deep blue) placed strategically in the background to provide a glowing atmosphere without overwhelming the content.
  - Accents & Glo: Use soft neon glows around primary elements and buttons (#5a67d8, #00d2ff, #f0abfc).
  - Typography: Crisp white, off-white, and muted slate tones for strong contrast against the dark background.
- **Glassmorphism Elements:**
  - Cards, panels, and navigation must use ackdrop-filter: blur(20px) with subtle semi-transparent backgrounds (e.g., gba(255, 255, 255, 0.05)).
  - Borders: implement conic-gradient or linear-gradient semi-transparent borders to catch the virtual light.
  - Drop Shadows: Soft, diffuse, colored drop-shadows to enhance depth.
- **Typography & Details:**
  - Use system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif.
  - Letter spacing, crisp font-weight variations, uppercase headers with low opacity for section labels.
- **Interactions & Micro-interactions:**
  - Hover states should slightly increase brightness or shift border gradients smoothly.
  - Entrance animations using IntersectionObserver fading and sliding in gracefully.
  - Interactive components: Data visualizations that update on hover, tabs, sliders, toggles that glide into place.
  - Smooth parallax effect on ambient background orbs.

## Information Architecture (12+ Sections)
The platform must flow intelligently as an executive briefing and interactive control panel. ALL SECTIONS MUST FEATURE REAL, CREDIBLE TEXT. No placeholder "lorem ipsum".

1. **Global Navigation (Glass Header)**
   - Fixed, glassmorphism header with a subtle bottom border.
   - Logo, Products, Solutions, Customers, Pricing, and a glowing CTA ("Get Access").
2. **Hero Heroic Setup (Hero Section)**
   - Title: "Measure & Master Global Language Readiness"
   - Subtitle: "BentoLingo turns cultural divides into strategic advantages. Deploy premium language upskilling that connects global workforces seamlessly."
   - Ambient floating orbs in the background. Glowing CTA and secondary text link. Dashboard preview graphic represented via CSS and HTML layout (Not an image).
3. **Enterprise Validation (Trust Strip)**
   - Logos of global conglomerates mocked up purely via CSS typography and geometric shapes (e.g., NexusCorp, Quantum Dynamics, Horizon Logistics, Vertex).
4. **The Readiness Scoreboard (Interactive Dashboard Module)**
   - A magnificent glass-bento-grid display of language readiness signals.
   - Interactive metric cards showing score changes.
   - Mocked data charts built natively in CSS (e.g., proficiency vs tenure).
5. **Role-based Readiness (Tabbed Interface)**
   - Breakdowns for Sales, Engineering, Leadership, and Operations.
   - Clickable tabs that change the displayed metric and description smoothly.
6. **Risk Analysis Panel (Diagnostic Module)**
   - Highlights communication bottlenecks across regions with glowing amber and blue indicators.
   - "Identified friction points in APAC to EMEA technical handoffs".
7. **The Program Builder (Interactive Planning Interface)**
   - An operational planner. Let users click through steps to map out a rollout.
   - e.g., Step 1: Audit, Step 2: Target Selection, Step 3: Deployment.
8. **Coaching Route Map (Visual Timeline)**
   - A vertical or horizontal glowing line showing the employee journey from onboarding to fluency.
9. **Core Offerings (Grid Module)**
   - 4-column glass layout detailing features: Live Coaching, Asynchronous Micro-learning, Accent Localization, Enterprise Analytics.
10. **Testimonials / Executive Endorsement (Quote Section)**
    - Glowing glass cards featuring deep quotes from fictional executives on ROI and communication alignment.
11. **Technical Integration & Security (Infographic Module)**
    - Details on SSO, API features, and data privacy standard compliance.
12. **ROI Calculator (Interactive Interactive Component)**
    - Sliders natively built with HTML inputs that adjust calculated savings in meeting time and project alignment.
13. **Final Call to Action (Glo Poster)**
    - Huge, gradient-heavy section. Give it an ethereal neon light treatment. 
    - "Ready to sync the world?"
14. **Granular Footer**
    - Multi-column footer. Links to product, legal, careers, resources, investors.

## Content & Data Fidelity
- Use real, highly professional corporate language.
- Every metric, label, tooltip, and button must contain meaningful text.
- Over 600 lines of highly crafted HTML/CSS/JS.
- DO NOT use placeholders. Every element must be deeply considered to reflect an elite product.

## Execution Checklist
- [ ] 12+ unique sections.
- [ ] Extensive Glassmorphism (backdrop-filter, transparent backgrounds).
- [ ] Authentic, executive copy.
- [ ] Substantial, interactive JS (IntersectionObserver, dynamic tabs, ROI calculator).
- [ ] No external assets, pure inline code.
- [ ] Absolute perfection in aesthetic pacing.
"""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BentoLingo | Enterprise Language Readiness</title>
    <style>
        :root {
            --bg-color: #050508;
            --text-primary: #f0f0f5;
            --text-secondary: #9ba0af;
            --accent-blue: #00d2ff;
            --accent-purple: #c440ff;
            --accent-coral: #ff5e91;
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.08);
            --glass-highlight: rgba(255, 255, 255, 0.12);
            --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            --glow-spread: 30px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: var(--font-main);
            overflow-x: hidden;
            line-height: 1.6;
            scroll-behavior: smooth;
        }

        /* Ambient Orbs */
        .ambient-orbs {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: -1;
            overflow: hidden;
        }
        .orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(120px);
            opacity: 0.4;
            animation: float 20s infinite ease-in-out alternate;
        }
        .orb-1 {
            width: 600px;
            height: 600px;
            background: var(--accent-blue);
            top: -10%;
            left: -10%;
        }
        .orb-2 {
            width: 500px;
            height: 500px;
            background: var(--accent-purple);
            bottom: -20%;
            right: -10%;
            animation-delay: -5s;
        }
        .orb-3 {
            width: 400px;
            height: 400px;
            background: var(--accent-coral);
            top: 40%;
            left: 50%;
            animation-delay: -10s;
            opacity: 0.2;
        }

        @keyframes float {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(50px, 80px) scale(1.1); }
        }

        /* Utility Classes */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 5%;
        }
        .glass-panel {
            background: var(--glass-bg);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 2rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            position: relative;
            overflow: hidden;
        }
        .glass-panel::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            opacity: 0.5;
        }
        .text-gradient {
            background: linear-gradient(135deg, #fff, var(--text-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .text-glow {
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
        }
        
        .section-header {
            text-align: center;
            margin-bottom: 4rem;
        }
        .section-tag {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--accent-blue);
            font-weight: 600;
            margin-bottom: 1rem;
            display: inline-block;
        }
        .section-title {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }
        .section-desc {
            font-size: 1.2rem;
            color: var(--text-secondary);
            max-width: 800px;
            margin: 0 auto;
        }

        /* Buttons */
        .btn {
            display: inline-block;
            padding: 1rem 2.5rem;
            border-radius: 100px;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            border: none;
        }
        .btn-primary {
            background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
            color: #fff;
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.4);
        }
        .btn-primary:hover {
            box-shadow: 0 0 30px rgba(196, 64, 255, 0.6);
            transform: translateY(-2px);
        }
        .btn-secondary {
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--glass-highlight);
            color: #fff;
        }
        .btn-secondary:hover {
            background: rgba(255,255,255,0.1);
        }

        /* 1. Global Navigation */
        nav {
            position: fixed;
            top: 0; left: 0; right: 0;
            z-index: 1000;
            background: rgba(5, 5, 8, 0.6);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--glass-border);
            padding: 1rem 0;
            transition: transform 0.3s;
        }
        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            color: #fff;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo-icon {
            width: 24px; height: 24px;
            background: linear-gradient(45deg, var(--accent-blue), var(--accent-purple));
            border-radius: 6px;
        }
        .nav-links {
            display: flex;
            gap: 2.5rem;
        }
        .nav-link {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-link:hover {
            color: #fff;
        }

        /* 2. Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding-top: 100px;
            position: relative;
        }
        .hero-content {
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }
        .hero-badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: rgba(0, 210, 255, 0.1);
            border: 1px solid rgba(0, 210, 255, 0.3);
            border-radius: 100px;
            color: var(--accent-blue);
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 2rem;
        }
        .hero-title {
            font-size: 5.5rem;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 2rem;
            letter-spacing: -2px;
        }
        .hero-desc {
            font-size: 1.3rem;
            color: var(--text-secondary);
            margin-bottom: 3rem;
        }
        .hero-actions {
            display: flex;
            gap: 1.5rem;
            justify-content: center;
        }

        /* 3. Enterprise Validation */
        .trust-strip {
            padding: 4rem 0;
            border-top: 1px solid var(--glass-border);
            border-bottom: 1px solid var(--glass-border);
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.01), transparent);
        }
        .trust-title {
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 2rem;
        }
        .logos-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            opacity: 0.6;
        }
        .mock-logo {
            font-size: 1.5rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
            filter: grayscale(100%);
        }
        .ml-icon {
            width: 20px; height: 20px;
            border: 2px solid currentColor;
            border-radius: 4px;
        }

        /* 4. Scoreboard Bento Grid */
        .readiness-section {
            padding: 8rem 0;
        }
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            grid-auto-rows: minmax(200px, auto);
        }
        .bento-item {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .bento-large {
            grid-column: span 2;
            grid-row: span 2;
        }
        .metric-value {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #fff, var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .metric-label {
            font-size: 1rem;
            color: var(--text-secondary);
            margin-top: 0.5rem;
        }
        .trend-up { color: #00e676; display: flex; align-items: center; gap: 5px; font-size: 0.9rem; margin-top: 1rem;}
        
        .chart-css {
            display: flex;
            align-items: flex-end;
            gap: 10px;
            height: 120px;
            margin-top: 2rem;
        }
        .bar {
            flex: 1;
            background: linear-gradient(to top, rgba(0,210,255,0.1), var(--accent-blue));
            border-radius: 4px 4px 0 0;
            transition: height 1s ease;
        }

        /* 5. Role-based Readiness (Tabs) */
        .role-section {
            padding: 8rem 0;
            background: radial-gradient(circle at center, rgba(196, 64, 255, 0.05) 0%, transparent 70%);
        }
        .tabs-header {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 3rem;
        }
        .tab-btn {
            background: transparent;
            border: 1px solid var(--glass-border);
            color: var(--text-secondary);
            padding: 1rem 2rem;
            border-radius: 100px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 600;
            transition: all 0.3s;
        }
        .tab-btn.active {
            background: rgba(255,255,255,0.1);
            color: #fff;
            border-color: var(--glass-highlight);
        }
        .tab-content {
            display: none;
            opacity: 0;
            transition: opacity 0.5s;
        }
        .tab-content.active {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            opacity: 1;
        }
        .role-detail h3 { font-size: 2rem; margin-bottom: 1rem; }
        .role-stat-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-top: 2rem;
        }

        /* 6. Risk Analysis */
        .risk-section {
            padding: 8rem 0;
        }
        .diagnostic-map {
            display: flex;
            gap: 2rem;
            padding: 2rem;
        }
        .risk-node {
            flex: 1;
            padding: 1.5rem;
            border: 1px solid rgba(255, 94, 145, 0.3);
            border-radius: 16px;
            background: rgba(255, 94, 145, 0.05);
            position: relative;
        }
        .risk-node.safe {
            border-color: rgba(0, 210, 255, 0.3);
            background: rgba(0, 210, 255, 0.05);
        }
        .risk-node h4 { margin-bottom: 0.5rem; }
        .pulse-dot {
            position: absolute;
            top: 1rem; right: 1rem;
            width: 10px; height: 10px;
            border-radius: 50%;
            background: var(--accent-coral);
            box-shadow: 0 0 10px var(--accent-coral);
            animation: pulse-op 2s infinite;
        }
        .risk-node.safe .pulse-dot { background: var(--accent-blue); box-shadow: 0 0 10px var(--accent-blue);}
        
        @keyframes pulse-op {
            0% { opacity: 0.4; } 50% { opacity: 1; } 100% { opacity: 0.4; }
        }

        /* 7. Program Builder */
        .builder-section {
            padding: 8rem 0;
        }
        .builder-stepper {
            display: flex;
            justify-content: space-between;
            margin-bottom: 3rem;
            position: relative;
        }
        .builder-stepper::before {
            content:'';
            position: absolute;
            top: 15px; left: 0; width: 100%; height: 2px;
            background: var(--glass-border);
            z-index: 0;
        }
        .step {
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
            cursor: pointer;
        }
        .step-num {
            width: 32px; height: 32px;
            border-radius: 50%;
            background: var(--bg-color);
            border: 2px solid var(--glass-highlight);
            display: flex; align-items: center; justify-content: center;
            font-weight: 700;
            transition: all 0.3s;
        }
        .step.active .step-num {
            border-color: var(--accent-blue);
            background: var(--accent-blue);
            color: var(--bg-color);
            box-shadow: 0 0 15px rgba(0,210,255,0.5);
        }

        /* 8. Timeline */
        .timeline {
            margin: 4rem 0;
            padding-left: 2rem;
            border-left: 2px solid var(--glass-border);
        }
        .timeline-item {
            position: relative;
            padding-bottom: 3rem;
            padding-left: 2rem;
        }
        .timeline-item::before {
            content: ''; position: absolute;
            left: -27px; top: 0;
            width: 12px; height: 12px;
            border-radius: 50%;
            background: var(--accent-purple);
            box-shadow: 0 0 10px var(--accent-purple);
        }

        /* 9. Core Offerings */
        .offerings-section { padding: 8rem 0; }
        .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; }
        
        /* 10. Quotes */
        .quotes-section { padding: 8rem 0; }
        .quote-card {
            font-size: 1.2rem;
            font-style: italic;
            border-left: 4px solid var(--accent-blue);
        }

        /* 11. Security */
        .security-section { padding: 8rem 0; text-align: center; }
        .security-badges {
            display: flex; justify-content: center; gap: 3rem; margin-top: 3rem;
        }
        .sec-badge {
            width: 120px; height: 120px;
            border-radius: 50%;
            border: 1px dashed rgba(255,255,255,0.2);
            display: flex; align-items: center; justify-content: center;
            flex-direction: column; font-size: 0.8rem; color: var(--text-secondary);
        }

        /* 12. ROI Calculator */
        .roi-section { padding: 8rem 0; }
        .calc-panel {
            display: flex; gap: 4rem; align-items: center;
        }
        .calc-controls { flex: 1; }
        .input-group { margin-bottom: 2rem; }
        .input-group label { display: block; margin-bottom: 0.5rem; font-weight: 500;}
        input[type=range] {
            width: 100%; -webkit-appearance: none; background: transparent;
        }
        input[type=range]::-webkit-slider-runnable-track {
            height: 6px; background: var(--glass-border); border-radius: 3px;
        }
        input[type=range]::-webkit-slider-thumb {
            -webkit-appearance: none; height: 20px; width: 20px;
            border-radius: 50%; background: var(--accent-blue);
            margin-top: -7px; cursor: pointer; box-shadow: 0 0 10px var(--accent-blue);
        }
        .calc-result {
            flex: 1; text-align: center;
            padding: 4rem; border-radius: 24px;
            background: radial-gradient(circle, rgba(0,210,255,0.1) 0%, transparent 70%);
        }

        /* 13. Final CTA */
        .cta-section {
            padding: 12rem 0;
            text-align: center;
            position: relative;
        }
        .cta-glow {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 800px; height: 800px;
            background: radial-gradient(circle, rgba(196,64,255,0.2) 0%, transparent 60%);
            z-index: -1;
        }

        /* 14. Footer */
        footer {
            padding: 6rem 0 2rem;
            border-top: 1px solid var(--glass-border);
            font-size: 0.9rem;
        }
        .footer-grid {
            display: grid; grid-template-columns: 2fr repeat(4, 1fr); gap: 4rem;
            margin-bottom: 4rem;
        }
        .footer-col h4 { margin-bottom: 1.5rem; color: #fff; }
        .footer-col a {
            display: block; color: var(--text-secondary);
            text-decoration: none; margin-bottom: 0.8rem;
        }
        .footer-col a:hover { color: var(--accent-blue); }

        /* Animations */
        .fade-in {
            opacity: 0; transform: translateY(30px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }
        .fade-in.visible { opacity: 1; transform: translateY(0); }

        @media(max-width: 1024px) {
            .hero-title { font-size: 4rem; }
            .bento-grid { grid-template-columns: 1fr; }
            .bento-large { grid-column: span 1; grid-row: span 1; }
            .tab-content.active { grid-template-columns: 1fr; }
            .calc-panel { flex-direction: column; }
            .grid-4 { grid-template-columns: 1fr 1fr; }
            .footer-grid { grid-template-columns: 1fr 1fr; }
            .diagnostic-map { flex-direction: column; }
        }
    </style>
</head>
<body>

    <!-- Ambient Background -->
    <div class="ambient-orbs">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>

    <!-- 1. Global Navigation -->
    <nav id="navbar">
        <div class="container nav-container">
            <a href="#" class="logo">
                <div class="logo-icon"></div>
                BentoLingo
            </a>
            <div class="nav-links">
                <a href="#platform" class="nav-link">Platform</a>
                <a href="#readiness" class="nav-link">Solutions</a>
                <a href="#roi" class="nav-link">ROI</a>
                <a href="#security" class="nav-link">Security</a>
            </div>
            <a href="#" class="btn btn-primary" style="padding: 0.6rem 1.5rem;">Access Dashboard</a>
        </div>
    </nav>

    <!-- 2. Hero Section -->
    <section class="hero">
        <div class="container hero-content fade-in">
            <div class="hero-badge">Enterprise Edition v2.4</div>
            <h1 class="hero-title text-gradient">Measure & Master Global Language Readiness.</h1>
            <p class="hero-desc">BentoLingo turns cultural divides into strategic advantages. Deploy premium language upskilling that connects global workforces seamlessly, backed by actionable data.</p>
            <div class="hero-actions">
                <a href="#demo" class="btn btn-primary">Initialize Program</a>
                <a href="#platform" class="btn btn-secondary">View Architecture</a>
            </div>
        </div>
    </section>

    <!-- 3. Enterprise Validation -->
    <section class="trust-strip">
        <div class="container">
            <p class="trust-title">Trusted by Global Operations Teams At</p>
            <div class="logos-container fade-in">
                <div class="mock-logo"><div class="ml-icon" style="border-radius: 50%;"></div> NexusCorp</div>
                <div class="mock-logo"><div class="ml-icon" style="transform: rotate(45deg);"></div> Quantum</div>
                <div class="mock-logo"><div class="ml-icon"></div> Horizon</div>
                <div class="mock-logo"><div class="ml-icon" style="border-radius: 50% 0 50% 0;"></div> Vertex Sys</div>
            </div>
        </div>
    </section>

    <!-- 4. Scoreboard Bento Grid -->
    <section id="platform" class="readiness-section">
        <div class="container">
            <div class="section-header fade-in">
                <span class="section-tag">Signal Intelligence</span>
                <h2 class="section-title">The Readiness Scoreboard</h2>
                <p class="section-desc">Real-time telemetry on aggregate language capability across your organization. Monitor readiness indices before deploying technical handoffs.</p>
            </div>
            
            <div class="bento-grid fade-in">
                <!-- Large Central Chart -->
                <div class="glass-panel bento-large">
                    <h3>Global Proficiency Index</h3>
                    <p class="text-secondary">Aggregate operational fluency score across top 5 operational hubs.</p>
                    <div class="metric-value">84.2/100</div>
                    <div class="trend-up">¡ü 12% Quarterly Growth</div>
                    
                    <div class="chart-css" id="mainChart">
                        <div class="bar" style="height: 40%;"></div>
                        <div class="bar" style="height: 55%;"></div>
                        <div class="bar" style="height: 65%;"></div>
                        <div class="bar" style="height: 45%;"></div>
                        <div class="bar" style="height: 80%;"></div>
                        <div class="bar" style="height: 90%;"></div>
                        <div class="bar" style="height: 85%;"></div>
                    </div>
                </div>
                
                <!-- Small Cards -->
                <div class="glass-panel bento-item">
                    <h4>Active Learners</h4>
                    <div class="metric-value" style="font-size: 2.5rem;">12,450</div>
                    <div class="metric-label">Cross-functional staff currently enrolled</div>
                </div>
                
                <div class="glass-panel bento-item">
                    <h4>Risk Factor</h4>
                    <div class="metric-value" style="font-size: 2.5rem; background: linear-gradient(135deg, #fff, var(--accent-coral)); -webkit-background-clip: text;">Low</div>
                    <div class="metric-label">Critical communication bottleneck probability</div>
                </div>
                
                <div class="glass-panel bento-item">
                    <h4>Session Hours</h4>
                    <div class="metric-value" style="font-size: 2.5rem;">45K</div>
                    <div class="metric-label">Total synchronous coaching hours logged</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Role-based Readiness (Tabs) -->
    <section id="readiness" class="role-section">
        <div class="container">
            <div class="section-header fade-in">
                <span class="section-tag">Departmental Fidelity</span>
                <h2 class="section-title">Role-Specific Calibration</h2>
                <p class="section-desc">Different roles require distinct linguistic vectors. We map technical, persuasive, and leadership vocabularies independently.</p>
            </div>
            
            <div class="tabs-header fade-in">
                <button class="tab-btn active" data-target="tab-1">Engineering</button>
                <button class="tab-btn" data-target="tab-2">Sales & GTM</button>
                <button class="tab-btn" data-target="tab-3">Leadership</button>
            </div>
            
            <div class="glass-panel fade-in" style="min-height: 400px;">
                <div id="tab-1" class="tab-content active">
                    <div class="role-detail">
                        <h3>Technical Documentation & Handoffs</h3>
                        <p class="text-secondary">Engineers focus on precise vocabulary necessary for asynchronous PR reviews, exact bug descriptions, and cross-timezone deployment strategies.</p>
                        <div class="role-stat-grid">
                            <div>
                                <div style="font-size: 2rem; font-weight:700; color: var(--accent-blue);">94%</div>
                                <div class="text-secondary" style="font-size:0.9rem;">Tech Sync Rate</div>
                            </div>
                            <div>
                                <div style="font-size: 2rem; font-weight:700; color: var(--accent-purple);">1.2H</div>
                                <div class="text-secondary" style="font-size:0.9rem;">Saved per Sprint</div>
                            </div>
                        </div>
                    </div>
                    <div style="background: rgba(0,0,0,0.3); border-radius: 16px; padding: 2rem; border: 1px solid var(--glass-border);">
                        <h4>Active Focus Areas</h4>
                        <ul style="list-style: none; margin-top: 1rem;">
                            <li style="margin-bottom: 1rem; display:flex; align-items:center; gap:10px;">
                                <div style="width:8px; height:8px; border-radius:50%; background:var(--accent-blue);"></div>
                                Agile Ceremony Articulation
                            </li>
                            <li style="margin-bottom: 1rem; display:flex; align-items:center; gap:10px;">
                                <div style="width:8px; height:8px; border-radius:50%; background:var(--accent-purple);"></div>
                                Incident Post-Mortem Writing
                            </li>
                            <li style="display:flex; align-items:center; gap:10px;">
                                <div style="width:8px; height:8px; border-radius:50%; background:var(--accent-blue);"></div>
                                Architecture Proposal Presentation
                            </li>
                        </ul>
                    </div>
                </div>
                
                <div id="tab-2" class="tab-content">
                    <div class="role-detail">
                        <h3>Persuasion & Negotiation</h3>
                        <p class="text-secondary">Sales teams require high-fidelity idiomatic localization and pacing. We drill on objection handling, executive presence, and regional colloquialisms.</p>
                        <div class="role-stat-grid">
                            <div>
                                <div style="font-size: 2rem; font-weight:700; color: var(--accent-blue);">+22%</div>
                                <div class="text-secondary" style="font-size:0.9rem;">Close Rate Delta</div>
                            </div>
                        </div>
                    </div>
                    <div style="background: rgba(0,0,0,0.3); border-radius: 16px; padding: 2rem; border: 1px solid var(--glass-border);">
                        <h4>Active Focus Areas</h4>
                        <p class="text-secondary">Idiom Integration, High-stakes Pitch Delivery, Cross-cultural Nuance Sensing.</p>
                    </div>
                </div>
                
                <div id="tab-3" class="tab-content">
                    <div class="role-detail">
                        <h3>Inspiring Global Orgs</h3>
                        <p class="text-secondary">Executives need to project vision seamlessly across distinct cultural landscapes. Focus on clarity, empathy, and broadcast communication.</p>
                    </div>
                    <div style="background: rgba(0,0,0,0.3); border-radius: 16px; padding: 2rem; border: 1px solid var(--glass-border);">
                        <h4>Core Metrics</h4>
                        <p class="text-secondary">Employee Sentiment Alignment, All-Hands Retention Rate.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Risk Analysis Panel -->
    <section class="risk-section">
        <div class="container fade-in">
            <div class="section-header">
                <h2 class="section-title">Global Diagnostic Heatmap</h2>
            </div>
            <div class="diagnostic-map glass-panel">
                <div class="risk-node">
                    <div class="pulse-dot"></div>
                    <h4>APAC to EMEA Handoff</h4>
                    <p class="text-secondary" style="font-size: 0.9rem;">Identified friction: Context loss in asynchronous tickets due to passive phrasing. Recommended intervention: Direct framing module.</p>
                </div>
                <div class="risk-node safe">
                    <div class="pulse-dot"></div>
                    <h4>NA to LATAM Integration</h4>
                    <p class="text-secondary" style="font-size: 0.9rem;">Nominal friction. Cohort has completed advanced colloquial alignment. Alignment score: 92%.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 7. Program Builder -->
    <section class="builder-section">
        <div class="container fade-in">
            <div class="section-header">
                <span class="section-tag">Deployment</span>
                <h2 class="section-title">The Rollout Architect</h2>
            </div>
            
            <div class="glass-panel">
                <div class="builder-stepper">
                    <div class="step active" onclick="activateStep(1)">
                        <div class="step-num">1</div>
                        <span>Diagnostic Audit</span>
                    </div>
                    <div class="step" onclick="activateStep(2)">
                        <div class="step-num">2</div>
                        <span>Cohort Mapping</span>
                    </div>
                    <div class="step" onclick="activateStep(3)">
                        <div class="step-num">3</div>
                        <span>Coaching Allocation</span>
                    </div>
                    <div class="step" onclick="activateStep(4)">
                        <div class="step-num">4</div>
                        <span>Go Live</span>
                    </div>
                </div>
                
                <div id="step-content" style="padding: 2rem; background: rgba(0,0,0,0.4); border-radius: 12px; min-height: 150px;">
                    <h4>Step 1: AI-Powered Diagnostic Audit</h4>
                    <p class="text-secondary">Distribute 15-minute voice and text assessments to target departments. Our engine processes vocabulary breadth, grammatical precision, and industry-specific jargon accuracy to establish baselines.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. Coaching Route Map -->
    <section class="container fade-in">
        <h3 style="margin-bottom: 2rem;">Typical Employee Route Map</h3>
        <div class="timeline">
            <div class="timeline-item glass-panel" style="margin-bottom: 2rem;">
                <h4>Month 1: Calibration</h4>
                <p class="text-secondary">Diagnostic completion and assignment to asynchronous micro-learning tracks tailored to specific gaps.</p>
            </div>
            <div class="timeline-item glass-panel" style="margin-bottom: 2rem;">
                <h4>Month 3: Active Synthesis</h4>
                <p class="text-secondary">Integration of 1:1 live coaching sessions parsing real work artifacts (emails, presentations).</p>
            </div>
            <div class="timeline-item glass-panel">
                <h4>Month 6: Native Operational Flow</h4>
                <p class="text-secondary">Graduation. Shift to maintenance mode and peer mentoring frameworks.</p>
            </div>
        </div>
    </section>

    <!-- 9. Core Offerings -->
    <section class="offerings-section">
        <div class="container">
            <div class="grid-4 fade-in">
                <div class="glass-panel">
                    <div style="font-size: 2rem; margin-bottom: 1rem;">???</div>
                    <h4>Live Coaching</h4>
                    <p class="text-secondary" style="font-size: 0.9rem; margin-top:0.5rem;">Elite instructors from global business sectors available 24/7 for targeted intervention.</p>
                </div>
                <div class="glass-panel">
                    <div style="font-size: 2rem; margin-bottom: 1rem;">??</div>
                    <h4>Micro-learning</h4>
                    <p class="text-secondary" style="font-size: 0.9rem; margin-top:0.5rem;">Contextual 5-minute modules pushed directly to Slack/Teams integrating daily vocabulary.</p>
                </div>
                <div class="glass-panel">
                    <div style="font-size: 2rem; margin-bottom: 1rem;">???</div>
                    <h4>Accent Nav</h4>
                    <p class="text-secondary" style="font-size: 0.9rem; margin-top:0.5rem;">AI-driven pronunciation modeling that preserves identity while ensuring strict intelligibility.</p>
                </div>
                <div class="glass-panel">
                    <div style="font-size: 2rem; margin-bottom: 1rem;">??</div>
                    <h4>Exec Analytics</h4>
                    <p class="text-secondary" style="font-size: 0.9rem; margin-top:0.5rem;">Board-ready reporting linking language fluency metrics directly to project delivery timelines.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 10. Quotes -->
    <section class="quotes-section">
        <div class="container fade-in">
            <div class="glass-panel quote-card">
                "Prior to BentoLingo, we lost an estimated 40 hours a week across engineering trying to clarify async PR comments. Resolving the language barrier resolved our deployment pipeline bottleneck. The ROI was visible in quarter one."
                <div style="margin-top: 1.5rem; font-style: normal;">
                    <strong>Sarah Jenkins</strong><br>
                    <span class="text-secondary">VP of Engineering, Horizon Logistics</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 11. Security -->
    <section id="security" class="security-section">
        <div class="container fade-in">
            <div class="section-header">
                <h2 class="section-title">Enterprise Security Posture</h2>
                <p class="section-desc">We do not compromise on data integrity. Audio processing is localized, and PII is scrubbed before analysis. SOC-2 Type II Certified.</p>
            </div>
            <div class="security-badges">
                <div class="sec-badge">
                    <strong>SOC 2</strong>
                    <span>Type II</span>
                </div>
                <div class="sec-badge">
                    <strong>GDPR</strong>
                    <span>Compliant</span>
                </div>
                <div class="sec-badge">
                    <strong>SSO</strong>
                    <span>SAML / OIDC</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 12. ROI Calculator -->
    <section id="roi" class="roi-section">
        <div class="container fade-in">
            <div class="glass-panel calc-panel">
                <div class="calc-controls">
                    <h3>Projected Efficiency ROI</h3>
                    <p class="text-secondary" style="margin-bottom: 2rem;">Adjust the parameters to estimate the time and cost savings of aligning your global teams.</p>
                    
                    <div class="input-group">
                        <label>Global Team Size: <span id="teamVal">500</span> employees</label>
                        <input type="range" id="teamSize" min="50" max="5000" step="50" value="500">
                    </div>
                    <div class="input-group">
                        <label>Avg. Async Touchpoints / Day: <span id="touchVal">10</span></label>
                        <input type="range" id="touchpoints" min="1" max="50" value="10">
                    </div>
                </div>
                <div class="calc-result">
                    <div class="text-secondary" style="margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 1px;">Estimated Annual Savings</div>
                    <div id="savingsResult" class="metric-value" style="font-size: 4rem;">.2M</div>
                    <p class="text-secondary" style="margin-top: 1rem;">Calculated via reduction in clarification cycles and meeting overruns.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 13. Final CTA -->
    <section class="cta-section fade-in">
        <div class="cta-glow"></div>
        <div class="container">
            <h2 class="text-glow" style="font-size: 4rem; margin-bottom: 2rem;">Ready to sync the world?</h2>
            <p class="text-secondary" style="font-size: 1.2rem; margin-bottom: 3rem; max-width: 600px; margin-inline: auto;">
                Provision your instance of BentoLingo and run a diagnostic snapshot on your core teams today.
            </p>
            <a href="#" class="btn btn-primary" style="font-size: 1.2rem; padding: 1.2rem 3rem;">Request Executive Briefing</a>
        </div>
    </section>

    <!-- 14. Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <a href="#" class="logo" style="margin-bottom: 1rem;">
                        <div class="logo-icon"></div>
                        BentoLingo
                    </a>
                    <p class="text-secondary" style="max-width: 250px;">The enterprise standard for global language readiness and operational alignment.</p>
                </div>
                <div class="footer-col">
                    <h4>Platform</h4>
                    <a href="#">Scoreboard</a>
                    <a href="#">Diagnostic</a>
                    <a href="#">Micro-learning</a>
                    <a href="#">API Documentation</a>
                </div>
                <div class="footer-col">
                    <h4>Solutions</h4>
                    <a href="#">For Engineering</a>
                    <a href="#">For Sales</a>
                    <a href="#">For Leadership</a>
                    <a href="#">Case Studies</a>
                </div>
                <div class="footer-col">
                    <h4>Company</h4>
                    <a href="#">About Us</a>
                    <a href="#">Careers</a>
                    <a href="#">Investors</a>
                    <a href="#">Contact</a>
                </div>
                <div class="footer-col">
                    <h4>Legal</h4>
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Service</a>
                    <a href="#">Security</a>
                    <a href="#">DPA</a>
                </div>
            </div>
            <div style="text-align: center; color: var(--text-secondary); border-top: 1px solid var(--glass-border); padding-top: 2rem;">
                &copy; 2026 BentoLingo Corporation. All rights reserved.
            </div>
        </div>
    </footer>

    <script>
        // Intersection Observer for fade-in animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: "0px 0px -50px 0px"
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    
                    // Trigger chart animation if it's the chart
                    if(entry.target.querySelector('#mainChart')) {
                        setTimeout(() => animateChart(), 200);
                    }
                }
            });
        }, observerOptions);

        document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

        // Navbar blur on scroll
        window.addEventListener('scroll', () => {
            const nav = document.getElementById('navbar');
            if (window.scrollY > 50) {
                nav.style.background = 'rgba(5, 5, 8, 0.85)';
                nav.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
            } else {
                nav.style.background = 'rgba(5, 5, 8, 0.6)';
                nav.style.boxShadow = 'none';
            }
        });

        // Tab Logic
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.getAttribute('data-target');
                
                tabBtns.forEach(b => b.classList.remove('active'));
                tabContents.forEach(c => c.classList.remove('active'));
                
                btn.classList.add('active');
                document.getElementById(targetId).classList.add('active');
            });
        });

        // Chart Animation Logic
        function animateChart() {
            const bars = document.querySelectorAll('.bar');
            const heights = ['60%', '75%', '50%', '85%', '95%', '70%', '90%'];
            bars.forEach((bar, index) => {
                setTimeout(() => {
                    bar.style.height = heights[index];
                }, index * 100);
            });
        }

        // Stepper Logic
        function activateStep(num) {
            const steps = document.querySelectorAll('.step');
            steps.forEach((s, idx) => {
                if(idx + 1 === num) {
                    s.classList.add('active');
                } else {
                    s.classList.remove('active');
                }
            });

            const contentDiv = document.getElementById('step-content');
            const content = {
                1: { title: "Step 1: AI-Powered Diagnostic Audit", desc: "Distribute 15-minute voice and text assessments to target departments. Our engine processes vocabulary breadth, grammatical precision, and industry-specific jargon accuracy to establish baselines." },
                2: { title: "Step 2: Cohort Mapping", desc: "Group employees algorithmically based on shared deficiencies and operational proximity. This ensures peer-learning dynamics and relevant contextual curricula." },
                3: { title: "Step 3: Coaching Allocation", desc: "Automatically match cohorts with specialized human coaches possessing relevant industry backgrounds (e.g., matching fintech devs with ex-fintech tech leads)." },
                4: { title: "Step 4: Go Live & Monitor", desc: "Deploy micro-learning modules to Slack/Teams and initiate the synchronous schedule. The Scoreboard begins receiving telemetry within 48 hours." }
            };

            contentDiv.innerHTML = <h4></h4><p class="text-secondary" style="margin-top:0.5rem;"></p>;
        }

        // ROI Calculator Logic
        const teamSize = document.getElementById('teamSize');
        const touchpoints = document.getElementById('touchpoints');
        const teamVal = document.getElementById('teamVal');
        const touchVal = document.getElementById('touchVal');
        const savingsResult = document.getElementById('savingsResult');

        function calculateROI() {
            teamVal.textContent = teamSize.value;
            touchVal.textContent = touchpoints.value;
            
            // Artificial formula for demonstration: (Team * Touchpoints * arbitrary cost factor)
            const baseHoursSavedPerWeek = (teamSize.value * touchpoints.value * 0.15); // hours saved
            const weeksPerYear = 48;
            const avgHourlyRate = 65; // assumed loaded cost
            
            const totalSavings = baseHoursSavedPerWeek * weeksPerYear * avgHourlyRate;
            
            if (totalSavings >= 1000000) {
                savingsResult.textContent = "$" + (totalSavings / 1000000).toFixed(1) + "M";
            } else {
                savingsResult.textContent = "$" + Math.round(totalSavings).toLocaleString();
            }
        }

        teamSize.addEventListener('input', calculateROI);
        touchpoints.addEventListener('input', calculateROI);
        
        // Initial init
        calculateROI();

    </script>
</body>
</html>
"""

with open('fdu_029/prompt.md', 'w', encoding='utf-8') as f:
    f.write(prompt_content)

os.makedirs('fdu_029/src', exist_ok=True)
with open('fdu_029/src/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"prompt.md lines: {len(prompt_content.splitlines())}")
print(f"index.html lines: {len(html_content.splitlines())}")
