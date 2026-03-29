import os

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atelier Meridian | Modern Premium Glassmorphism</title>
    <style>
        :root {
            /* Colors */
            --bg-void: #030305;
            --glass-bg-light: rgba(255, 255, 255, 0.03);
            --glass-bg-medium: rgba(255, 255, 255, 0.06);
            --glass-bg-heavy: rgba(255, 255, 255, 0.1);
            --glass-border: rgba(255, 255, 255, 0.15);
            /* Accent Glo */
            --glo-gold: rgba(212, 175, 55, 0.6);
            --glo-magenta: rgba(255, 0, 128, 0.6);
            --glo-sapphire: rgba(15, 82, 186, 0.6);
            --glo-amethyst: rgba(153, 102, 204, 0.6);
            --glo-azure: rgba(0, 127, 255, 0.6);
            /* Semantic */
            --status-ready: #00e5ff;
            --status-risk: #ffab00;
            --status-delayed: #ff1744;
            --status-recovered: #00e676;
            /* Typography */
            --text-primary: rgba(255, 255, 255, 0.95);
            --text-secondary: rgba(255, 255, 255, 0.65);
            --text-tertiary: rgba(255, 255, 255, 0.4);
            /* Radii */
            --radius-sm: 8px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-xl: 32px;
            --radius-pill: 9999px;
            /* Layout */
            --space-xs: 8px;
            --space-sm: 16px;
            --space-md: 32px;
            --space-lg: 64px;
            --space-xl: 128px;
            /* Fonts */
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-serif: 'Playfair Display', 'Georgia', serif;
            --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: var(--bg-void);
            color: var(--text-primary);
            font-family: var(--font-sans);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* Ambient Orbs */
        .ambient-orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(100px);
            z-index: -1;
            opacity: 0.5;
            animation: float 20s infinite alternate cubic-bezier(0.4, 0, 0.2, 1);
        }
        .orb-1 { width: 600px; height: 600px; background: var(--glo-amethyst); top: -200px; left: -200px; }
        .orb-2 { width: 400px; height: 400px; background: var(--glo-sapphire); bottom: 100px; right: -100px; animation-delay: -5s; }
        .orb-3 { width: 500px; height: 500px; background: var(--glo-gold); top: 40%; left: 30%; opacity: 0.3; animation-delay: -10s; }

        @keyframes float {
            0% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(50px, 50px) scale(1.1); }
            100% { transform: translate(-50px, 100px) scale(0.9); }
        }

        /* Glass Utility */
        .glass-panel {
            background: var(--glass-bg-light);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-lg);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }

        .conic-border {
            position: relative;
        }
        .conic-border::before {
            content: '';
            position: absolute;
            inset: -1px;
            border-radius: inherit;
            padding: 1px;
            background: conic-gradient(from var(--angle, 0deg), transparent 0%, var(--glo-gold) 50%, transparent 100%);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            animation: spin 4s linear infinite;
        }

        @property --angle {
            syntax: '<angle>';
            initial-value: 0deg;
            inherits: false;
        }
        @keyframes spin {
            to { --angle: 360deg; }
        }

        /* Container */
        .container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 0 var(--space-md);
        }

        section {
            padding: var(--space-xl) 0;
            position: relative;
        }

        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary);
            font-weight: 400;
        }
        .serif {
            font-family: var(--font-serif);
        }

        /* Section 1: Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 100;
            padding: var(--space-sm) var(--space-md);
            transition: all 0.3s ease;
        }
        .glass-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--glass-bg-medium);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-pill);
            padding: var(--space-sm) var(--space-md);
            max-width: 1200px;
            margin: 0 auto;
        }
        .nav-logo {
            font-size: 1.2rem;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .nav-links {
            display: flex;
            gap: var(--space-md);
        }
        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.9rem;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: var(--text-primary);
        }
        .nav-cta button {
            background: var(--text-primary);
            color: var(--bg-void);
            border: none;
            padding: 10px 24px;
            border-radius: var(--radius-pill);
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .nav-cta button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px var(--glass-border);
        }

        /* Section 1: Ambient Hero */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding-top: 100px;
        }
        .hero h1 {
            font-size: clamp(3rem, 6vw, 6rem);
            line-height: 1.1;
            margin-bottom: var(--space-md);
            background: linear-gradient(to right, #fff, var(--text-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            font-size: 1.25rem;
            color: var(--text-secondary);
            max-width: 700px;
            margin: 0 auto var(--space-lg);
        }
        .hero-ctas {
            display: flex;
            gap: var(--space-sm);
            justify-content: center;
        }
        .btn-primary {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid var(--glass-border);
            color: #fff;
            padding: 16px 36px;
            border-radius: var(--radius-pill);
            font-size: 1rem;
            cursor: pointer;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        .btn-primary:hover {
            background: rgba(255, 255, 255, 0.2);
            box-shadow: 0 0 20px rgba(255,255,255,0.1);
        }
        .btn-secondary {
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-secondary);
            padding: 16px 36px;
            border-radius: var(--radius-pill);
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .btn-secondary:hover {
            color: #fff;
        }

        /* Section 2: Proof Strip */
        .proof-strip {
            padding: var(--space-md) 0;
            border-top: 1px solid var(--glass-border);
            border-bottom: 1px solid var(--glass-border);
            background: var(--glass-bg-light);
            backdrop-filter: blur(10px);
            overflow: hidden;
        }
        .proof-track {
            display: flex;
            gap: var(--space-xl);
            white-space: nowrap;
            align-items: center;
            opacity: 0.6;
        }
        .proof-item {
            font-size: 1.5rem;
            letter-spacing: 4px;
            text-transform: uppercase;
            font-weight: 300;
        }

        /* Section 3: Ritual Grid (Bento Box) */
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: var(--space-sm);
            margin-top: var(--space-xl);
        }
        .bento-item {
            padding: var(--space-lg);
            border-radius: var(--radius-lg);
            background: var(--glass-bg-medium);
            border: 1px solid var(--glass-border);
            position: relative;
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .bento-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.5);
            border-color: rgba(255,255,255,0.3);
        }
        .bento-item.large { grid-column: span 8; }
        .bento-item.medium { grid-column: span 4; }
        .bento-item.tall { grid-column: span 4; grid-row: span 2; }
        @media (max-width: 1024px) {
            .bento-item.large, .bento-item.medium, .bento-item.tall { grid-column: span 12; grid-row: auto; }
        }
        .bento-item h3 { font-size: 1.5rem; margin-bottom: 1rem; }
        .bento-item p { color: var(--text-secondary); font-size: 0.95rem; }
        .bento-icon { width: 40px; height: 40px; margin-bottom: var(--space-sm); fill: var(--text-primary); }

        /* Section 4: The Glo Console (Tabs) */
        .glo-console {
            margin-top: var(--space-xl);
        }
        .console-header { text-align: center; margin-bottom: var(--space-lg); }
        .console-header h2 { font-size: 2.5rem; }
        .console-window {
            background: rgba(10, 10, 12, 0.7);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-lg);
            backdrop-filter: blur(30px);
            overflow: hidden;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
        }
        .console-nav {
            display: flex;
            border-bottom: 1px solid var(--glass-border);
            background: rgba(255,255,255,0.02);
            padding: 0 var(--space-sm);
        }
        .console-tab {
            padding: 20px 30px;
            color: var(--text-secondary);
            cursor: pointer;
            border-bottom: 2px solid transparent;
            transition: all 0.3s;
            font-weight: 500;
            letter-spacing: 1px;
            text-transform: uppercase;
            font-size: 0.85rem;
        }
        .console-tab:hover { color: var(--text-primary); }
        .console-tab.active {
            color: var(--text-primary);
            border-bottom-color: var(--glo-gold);
            background: linear-gradient(to top, rgba(212, 175, 55, 0.1), transparent);
        }
        .console-body {
            padding: var(--space-lg);
            position: relative;
            min-height: 400px;
        }
        .tab-content { display: none; animation: fadeIn 0.5s ease; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .dashboard-mockup {
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: var(--space-md);
        }
        .mock-sidebar ul { list-style: none; }
        .mock-sidebar li { padding: 10px; margin-bottom: 5px; border-radius: var(--radius-sm); color: var(--text-secondary); }
        .mock-sidebar li.active { background: var(--glass-bg-medium); color: #fff; }
        .mock-main { display: flex; flex-direction: column; gap: var(--space-md); }
        .mock-card { background: var(--glass-bg-light); border: 1px solid var(--glass-border); padding: var(--space-md); border-radius: var(--radius-md); }
        .mock-card-title { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-tertiary); margin-bottom: 10px; }

        /* Section 5: Choreography Flow (Timeline) */
        .choreography { margin-top: var(--space-xl); position: relative; }
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
            padding: var(--space-xl) 0;
        }
        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 1px;
            background: linear-gradient(to bottom, transparent, var(--glass-border), transparent);
            transform: translateX(-50%);
        }
        .timeline-item {
            display: flex;
            justify-content: flex-end;
            padding-right: 50%;
            position: relative;
            margin-bottom: var(--space-md);
            opacity: 0.5;
            transition: opacity 0.5s, transform 0.5s;
        }
        .timeline-item:nth-child(even) {
            justify-content: flex-start;
            padding-right: 0;
            padding-left: 50%;
        }
        .timeline-item.in-view { opacity: 1; transform: scale(1.02); }
        .timeline-content {
            width: 80%;
            padding: var(--space-md);
            background: var(--glass-bg-medium);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-md);
            backdrop-filter: blur(10px);
        }
        .timeline-item::after {
            content: '';
            position: absolute;
            right: calc(50% - 6px);
            top: 40px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--bg-void);
            border: 2px solid var(--glo-sapphire);
            box-shadow: 0 0 10px var(--glo-sapphire);
        }
        .timeline-item:nth-child(even)::after {
            left: calc(50% - 6px);
        }

        /* Section 6: Guest Recovery (Accordion) */
        .recovery-grid {
            max-width: 800px;
            margin: var(--space-lg) auto;
            display: flex;
            flex-direction: column;
            gap: var(--space-sm);
        }
        .accordion-item {
            background: var(--glass-bg-light);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-md);
            overflow: hidden;
            transition: all 0.3s;
        }
        .accordion-header {
            padding: var(--space-md);
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            background: transparent;
            user-select: none;
        }
        .accordion-title {
            font-size: 1.1rem;
            font-weight: 500;
        }
        .accordion-icon {
            transition: transform 0.3s;
        }
        .accordion-item.open .accordion-icon {
            transform: rotate(180deg);
        }
        .accordion-body {
            padding: 0 var(--space-md);
            max-height: 0;
            overflow: hidden;
            transition: all 0.3s ease;
            color: var(--text-secondary);
        }
        .accordion-item.open .accordion-body {
            padding: 0 var(--space-md) var(--space-md) var(--space-md);
            max-height: 200px;
        }
        .status-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: var(--radius-pill);
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }
        .status-ready { background: rgba(0, 229, 255, 0.1); color: var(--status-ready); border: 1px solid rgba(0,229,255,0.3); }
        .status-risk { background: rgba(255, 171, 0, 0.1); color: var(--status-risk); border: 1px solid rgba(255,171,0,0.3); }

        /* Section 7: Event Readiness (Conic Border Banner) */
        .event-banner {
            margin-top: var(--space-xl);
            padding: var(--space-xl);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0,0,0,0.4);
        }
        .event-banner h2 { font-size: 3rem; margin-bottom: 1rem; }
        .event-banner p { font-size: 1.2rem; color: var(--text-secondary); max-width: 500px; }

        /* Section 8: Leadership Visibility (Stats) */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: var(--space-md);
            margin-top: var(--space-lg);
        }
        .stat-card {
            background: var(--glass-bg-medium);
            border: 1px solid var(--glass-border);
            padding: var(--space-md);
            border-radius: var(--radius-md);
            text-align: center;
        }
        .stat-value {
            font-size: 3rem;
            font-family: var(--font-mono);
            font-weight: 300;
            margin: var(--space-sm) 0;
            color: var(--glo-gold);
            text-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
        }
        .stat-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-secondary);
        }
        
        /* Bar Chart CSS */
        .css-chart {
            height: 150px;
            display: flex;
            align-items: flex-end;
            gap: 10px;
            padding-top: var(--space-lg);
            border-bottom: 1px solid var(--glass-border);
            margin-top: var(--space-md);
        }
        .chart-bar {
            flex: 1;
            background: linear-gradient(to top, var(--glo-azure), transparent);
            border-radius: var(--radius-sm) var(--radius-sm) 0 0;
            transition: height 1.5s cubic-bezier(0.1, 0.8, 0.2, 1);
            position: relative;
        }
        .chart-bar:hover::after {
            content: attr(data-val);
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--glass-bg-heavy);
            padding: 4px 8px;
            border-radius: var(--radius-sm);
            font-size: 0.8rem;
            font-family: var(--font-mono);
        }

        /* Section 9: Service Call Sheet */
        .call-sheet {
            background: var(--glass-bg-light);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-lg);
            padding: var(--space-lg);
            margin-top: var(--space-xl);
        }
        .sheet-row {
            display: grid;
            grid-template-columns: 100px 200px 1fr 100px;
            align-items: center;
            padding: var(--space-sm) 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            cursor: pointer;
            transition: background 0.3s;
        }
        .sheet-row:hover {
            background: rgba(255,255,255,0.02);
        }
        .sheet-row.hidden-details .sheet-detail { opacity: 0.3; filter: blur(4px); }
        .sheet-time { font-family: var(--font-mono); color: var(--text-secondary); }
        .sheet-role { text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; color: var(--glo-sapphire); }

        /* Section 10: Ambient Alert Gallery */
        .alert-gallery {
            display: flex;
            flex-direction: column;
            gap: var(--space-sm);
            position: fixed;
            right: var(--space-md);
            bottom: var(--space-md);
            z-index: 1000;
        }
        .toast {
            background: rgba(20,20,25,0.8);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-left: 3px solid var(--status-ready);
            padding: var(--space-sm) var(--space-md);
            border-radius: var(--radius-md);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            width: 300px;
            transform: translateX(120%);
            transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .toast.show { transform: translateX(0); }
        .toast-title { font-size: 0.9rem; font-weight: 600; margin-bottom: 4px; }
        .toast-desc { font-size: 0.8rem; color: var(--text-secondary); }

        /* Section 11: Testimonials */
        .testimonials {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: var(--space-lg);
            margin-top: var(--space-xl);
        }
        .quote-card {
            background: var(--glass-bg-light);
            border-left: 1px solid var(--glass-border);
            padding: var(--space-lg);
            position: relative;
        }
        .quote-card::before {
            content: '"';
            font-family: var(--font-serif);
            font-size: 4rem;
            position: absolute;
            top: 10px;
            left: 20px;
            color: rgba(255,255,255,0.1);
        }
        .quote-text {
            font-family: var(--font-serif);
            font-size: 1.2rem;
            font-style: italic;
            margin-bottom: var(--space-md);
            color: var(--text-primary);
        }
        .quote-author {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-tertiary);
        }

        /* Section 12: Footer */
        footer {
            margin-top: var(--space-xl);
            padding: var(--space-xl) 0 var(--space-md);
            border-top: 1px solid var(--glass-border);
            text-align: center;
            background: linear-gradient(to top, rgba(15, 82, 186, 0.05), transparent);
        }
        .footer-cta {
            font-size: 3rem;
            margin-bottom: var(--space-lg);
        }
        .glow-btn {
            background: transparent;
            border: 1px solid rgba(255,255,255,0.2);
            color: #fff;
            font-size: 1.2rem;
            padding: 20px 50px;
            border-radius: var(--radius-pill);
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: all 0.3s;
        }
        .glow-btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, var(--glo-gold) 0%, transparent 60%);
            transform: translate(-50%, -50%) scale(0);
            transition: transform 0.5s;
            z-index: -1;
            opacity: 0.4;
        }
        .glow-btn:hover::before {
            transform: translate(-50%, -50%) scale(1);
        }
        .glow-btn:hover { border-color: rgba(255,255,255,0.8); }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: var(--space-md);
            margin-bottom: var(--space-md);
        }
        .footer-links a { color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; }
        .copyright { color: var(--text-tertiary); font-size: 0.8rem; }

        /* Modal */
        .modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            backdrop-filter: blur(10px);
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
        }
        .modal-overlay.active { opacity: 1; pointer-events: auto; }
        .modal {
            background: var(--glass-bg-heavy);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-lg);
            padding: var(--space-lg);
            width: 90%;
            max-width: 600px;
            transform: translateY(20px) scale(0.95);
            transition: all 0.3s;
        }
        .modal-overlay.active .modal { transform: translateY(0) scale(1); }
        .close-modal {
            position: absolute;
            top: 20px; right: 20px;
            background: none; border: none; color: #fff;
            font-size: 1.5rem; cursor: pointer;
        }

    </style>
</head>
<body>

    <!-- Ambient Background -->
    <div class="ambient-orb orb-1"></div>
    <div class="ambient-orb orb-2"></div>
    <div class="ambient-orb orb-3"></div>

    <!-- Section 1: Navigation -->
    <nav id="navbar">
        <div class="glass-nav">
            <div class="nav-logo serif">Atelier Meridian</div>
            <div class="nav-links">
                <a href="#platform">Platform</a>
                <a href="#rituals">Service Rituals</a>
                <a href="#console">The Glo Console</a>
                <a href="#leadership">Leadership</a>
            </div>
            <div class="nav-cta">
                <button onclick="openModal()">Request Access</button>
            </div>
        </div>
    </nav>

    <!-- Section 1: Ambient Hero -->
    <section class="hero">
        <div class="container">
            <h1 class="serif">The Symphony of<br>Invisible Service</h1>
            <p>A hospitality operations platform for design-led hotels, private residences, and members clubs. Master your service rituals with the precision of a Swiss timepiece.</p>
            <div class="hero-ctas">
                <button class="btn-primary" onclick="openModal()">Experience the Console</button>
                <button class="btn-secondary">Read the Manifesto</button>
            </div>
        </div>
    </section>

    <!-- Section 2: Proof Strip -->
    <section class="proof-strip">
        <div class="proof-track" id="proof-track">
            <!-- Populated via JS for continuous scroll -->
            <span class="proof-item">Aman</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">Soho House</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">Rosewood</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">The Ned</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">Six Senses</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">Edition Hotels</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">Aman</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">Soho House</span>
            <span class="proof-item">&bull;</span>
            <span class="proof-item">Rosewood</span>
        </div>
    </section>

    <!-- Section 3: Ritual Grid -->
    <section id="rituals" class="container">
        <h2 class="serif" style="text-align:center; font-size: 2.5rem; margin-bottom: 2rem;">Choreograph Every Touchpoint</h2>
        <div class="bento-grid">
            <div class="bento-item large glass-panel">
                <svg class="bento-icon" viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2zm0 4.5l6.5 13.5h-13L12 6.5z"/></svg>
                <h3>The Grand Arrival</h3>
                <p>Track guest transit in real-time. Valet, reception, and luggage teams are perfectly synchronized before the vehicle pulls into the driveway. Welcome drinks are prepared at optimal temperature.</p>
            </div>
            <div class="bento-item medium glass-panel">
                <svg class="bento-icon" viewBox="0 0 24 24"><path d="M4 4h16v16H4z"/></svg>
                <h3>Housekeeping Stealth</h3>
                <p>Invisible turnover. Rooms are restored to perfection while guests are dining, triggered automatically by system geofences and reservations.</p>
            </div>
            <div class="bento-item tall glass-panel">
                <h3>Event Readiness</h3>
                <p>From private boardroom dinners to full-scale ballroom galas. Track floral deliveries, catering timelines, and AV setups with down-to-the-minute precision. Staffing levels automatically adjust based on guest density.</p>
                <div style="margin-top: 2rem; border-top: 1px solid var(--glass-border); padding-top: 1rem;">
                    <span class="status-badge status-ready">All Systems Online</span>
                </div>
            </div>
            <div class="bento-item large glass-panel">
                <h3>VVIP Preferences</h3>
                <p>Deep profiles built intuitively. Remember exactly how they prefer their coffee, their required pillow firmness, and their favorite reading chair placement. Turn raw data into legendary service moments.</p>
            </div>
        </div>
    </section>

    <!-- Section 4: The Glo Console -->
    <section id="console" class="container glo-console">
        <div class="console-header">
            <h2 class="serif">The Glo Console</h2>
            <p style="color:var(--text-secondary)">A command center designed not for data entry, but for fluid operational mastery.</p>
        </div>
        <div class="console-window conic-border">
            <div class="console-nav">
                <div class="console-tab active" onclick="switchTab(event, 'tab-overview')">Live Overview</div>
                <div class="console-tab" onclick="switchTab(event, 'tab-dispatch')">Staff Dispatch</div>
                <div class="console-tab" onclick="switchTab(event, 'tab-incident')">Incident Recovery</div>
            </div>
            <div class="console-body">
                <div id="tab-overview" class="tab-content active">
                    <div class="dashboard-mockup">
                        <div class="mock-sidebar">
                            <ul>
                                <li class="active">Today's Arrivals (14)</li>
                                <li>In-House VIPs (3)</li>
                                <li>Departures (12)</li>
                                <li>Event Roster</li>
                            </ul>
                        </div>
                        <div class="mock-main">
                            <div class="mock-card">
                                <div class="mock-card-title">Pending Arrival: Mr. Sterling</div>
                                <h3 style="font-size:1.5rem; margin-bottom: 10px;">ETA: 14 Mins</h3>
                                <div style="display:flex; gap: 10px;">
                                    <span class="status-badge status-risk">Luggage team short 1</span>
                                    <span class="status-badge status-ready">Suite 402 Inspected</span>
                                </div>
                            </div>
                            <div class="mock-card">
                                <div class="mock-card-title">General Sentiment Analysis</div>
                                <div style="height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow:hidden; margin-top:10px;">
                                    <div style="height: 100%; width: 92%; background: var(--status-ready);"></div>
                                </div>
                                <p style="font-size:0.8rem; margin-top:5px; color:var(--text-secondary)">92% of interactions rated 'Exceptional' today.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="tab-dispatch" class="tab-content">
                    <h3 style="margin-bottom:20px;">Active Units</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div class="mock-card"><div class="mock-card-title">Housekeeping Team Alpha</div><p>Floor 4 - 80% Complete</p></div>
                        <div class="mock-card"><div class="mock-card-title">Valet Stand</div><p>High volume expected at 18:00</p></div>
                    </div>
                </div>
                <div id="tab-incident" class="tab-content">
                    <h3 style="margin-bottom:20px;">Open Anomalies</h3>
                    <div class="mock-card" style="border-left: 3px solid var(--status-delayed);">
                        <div class="mock-card-title">Room Service Delay (Suite 501)</div>
                        <p>Order running 12 mins late. Recovery protocol activated. Comped dessert assigned to order.</p>
                        <button style="margin-top: 10px; background: rgba(255,255,255,0.1); border:none; color:#fff; padding: 5px 15px; border-radius:4px; font-size:0.8rem; cursor:pointer;">Authorize Apology Amenity</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 5: Choreography Flow -->
    <section class="container choreography">
        <h2 class="serif" style="text-align:center; font-size: 2.5rem; margin-bottom: 2rem;">The Guest Timeline</h2>
        <div class="timeline" id="timeline">
            <div class="timeline-item">
                <div class="timeline-content">
                    <span style="color:var(--glo-gold); font-family:var(--font-mono)">14:00 (T-120 mins)</span>
                    <h3 style="margin: 10px 0;">Pre-Arrival Inspection</h3>
                    <p style="font-size:0.9rem; color:var(--text-secondary)">Director of Rooms conducts final visual sweep. Climate control set to 21°C.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-content">
                    <span style="color:var(--glo-gold); font-family:var(--font-mono)">15:45 (T-15 mins)</span>
                    <h3 style="margin: 10px 0;">Proximity Alert Triggered</h3>
                    <p style="font-size:0.9rem; color:var(--text-secondary)">Guest vehicle passes geofence. Doorman, Luggage Porter, and Reception manager move to positions.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-content">
                    <span style="color:var(--glo-gold); font-family:var(--font-mono)">16:00 (Zero Hour)</span>
                    <h3 style="margin: 10px 0;">The Touchdown</h3>
                    <p style="font-size:0.9rem; color:var(--text-secondary)">Door opened within 3 seconds of parking. Address by name. Immediate escort to suite. Zero front-desk friction.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-content">
                    <span style="color:var(--glo-gold); font-family:var(--font-mono)">16:15 (T+15 mins)</span>
                    <h3 style="margin: 10px 0;">Luggage Placement</h3>
                    <p style="font-size:0.9rem; color:var(--text-secondary)">Baggage staged in dressing area unseen by guest during welcome tour.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 6: Guest Recovery -->
    <section class="container">
        <h2 class="serif" style="text-align:center; font-size: 2.5rem; margin-bottom: 2rem;">Algorithmic Empathy</h2>
        <p style="text-align:center; color:var(--text-secondary); max-width:600px; margin: 0 auto 3rem;">When friction occurs, execution must be flawless. Our workflows guide staff through high-stress recovery scenarios with grace.</p>
        
        <div class="recovery-grid" id="accordion">
            <div class="accordion-item glass-panel open">
                <div class="accordion-header" onclick="toggleAccordion(this)">
                    <span class="accordion-title">Noise Complaint Protocol</span>
                    <svg class="accordion-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
                </div>
                <div class="accordion-body">
                    <p style="padding-bottom: 15px;">Step 1: Security dispatched to assess (SLA: 3 mins).<br>
                    Step 2: If verified, polite intervention.<br>
                    Step 3: Affected guest contacted via preferred channel. Soft move offered if inventory allows. Complimentary breakfast automatically flagged for next morning.</p>
                </div>
            </div>
            <div class="accordion-item glass-panel">
                <div class="accordion-header" onclick="toggleAccordion(this)">
                    <span class="accordion-title">Luggage Delay Sequence</span>
                    <svg class="accordion-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
                </div>
                <div class="accordion-body">
                    <p style="padding-bottom: 15px;">If airline loses baggage: Concierge opens emergency overnight kit workflow. Custom sizing profile pulled from CRM. Fresh attire procured from boutique partners within 2 hours. Frequent updates pushed to guest app discreetly.</p>
                </div>
            </div>
            <div class="accordion-item glass-panel">
                <div class="accordion-header" onclick="toggleAccordion(this)">
                    <span class="accordion-title">Dining Allergy Strike</span>
                    <svg class="accordion-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
                </div>
                <div class="accordion-body">
                    <p style="padding-bottom: 15px;">If a known restriction is flagged near a dish, Kitchen Display System instantly flashes red. Expo chief must enter override code. Manager alerted to verify with table. Total fail-safe against severe reactions.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 7: Event Readiness Banner -->
    <section style="padding:0; margin: var(--space-xl) 0;">
        <div class="event-banner glass-panel conic-border">
            <div>
                <h2 class="serif">Banqueting & Beyond</h2>
                <p>Synchronize hundreds of moving parts. Manage culinary drops, floral load-ins, and talent rehearsals on a unified master clock visible to every earpiece in the building.</p>
            </div>
            <div>
                <button class="btn-primary" style="background:var(--glo-magenta); border:none;">Explore Event Ops</button>
            </div>
        </div>
    </section>

    <!-- Section 8: Leadership Visibility -->
    <section id="leadership" class="container">
        <h2 class="serif" style="font-size: 2.5rem; margin-bottom: 1rem;">The C-Suite Perspective</h2>
        <p style="color:var(--text-secondary); max-width:500px; margin-bottom: 2rem;">Move from retrospective reporting to proactive governance. Real-time metrics that signify operational health.</p>
        
        <div class="stats-grid" id="stats">
            <div class="stat-card">
                <div class="stat-label">Avg Speed of Service</div>
                <div class="stat-value"><span class="count-up" data-target="4">0</span>.<span class="count-up" data-target="2">0</span>m</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Recovery Success</div>
                <div class="stat-value"><span class="count-up" data-target="98">0</span>%</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Guest Retention</div>
                <div class="stat-value"><span class="count-up" data-target="86">0</span>%</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Task Efficiency</div>
                <div class="stat-value">+<span class="count-up" data-target="32">0</span>%</div>
            </div>
        </div>

        <div class="css-chart" id="bar-chart">
            <div class="chart-bar" style="height: 0%" data-target="40%" data-val="Mon: 42"></div>
            <div class="chart-bar" style="height: 0%" data-target="55%" data-val="Tue: 58"></div>
            <div class="chart-bar" style="height: 0%" data-target="45%" data-val="Wed: 47"></div>
            <div class="chart-bar" style="height: 0%" data-target="70%" data-val="Thu: 73"></div>
            <div class="chart-bar" style="height: 0%" data-target="95%" data-val="Fri: 98"></div>
            <div class="chart-bar" style="height: 0%" data-target="100%" data-val="Sat: 105"></div>
            <div class="chart-bar" style="height: 0%" data-target="80%" data-val="Sun: 84"></div>
        </div>
        <p style="text-align:center; font-size:0.8rem; color:var(--text-tertiary); margin-top:10px;">7-Day Volume Intensity Index</p>
    </section>

    <!-- Section 9: Service Call Sheet -->
    <section class="container">
        <h2 class="serif" style="font-size: 2.5rem; margin-bottom: 2rem;">Live Run of Show</h2>
        <div class="call-sheet">
            <div style="display:flex; justify-content:space-between; margin-bottom: 20px; border-bottom: 1px solid var(--glass-border); padding-bottom: 10px;">
                <span style="font-weight:bold; letter-spacing:2px;">OPERATIONS LOG</span>
                <span style="color:var(--status-ready)">&#9679; LIVE</span>
            </div>
            <div class="sheet-row hidden-details" onclick="this.classList.toggle('hidden-details')">
                <div class="sheet-time">08:00</div>
                <div class="sheet-role">Concierge</div>
                <div class="sheet-detail">Procure rare vintage wine for Penthouse arrival. Vendor contacted.</div>
                <div><span class="status-badge status-ready">Done</span></div>
            </div>
            <div class="sheet-row hidden-details" onclick="this.classList.toggle('hidden-details')">
                <div class="sheet-time">11:15</div>
                <div class="sheet-role">Engineering</div>
                <div class="sheet-detail">HVAC anomaly in Ballroom B. Replacing filter unit. Est 20 mins.</div>
                <div><span class="status-badge status-risk">Active</span></div>
            </div>
            <div class="sheet-row hidden-details" onclick="this.classList.toggle('hidden-details')">
                <div class="sheet-time">14:30</div>
                <div class="sheet-role">Housekeeping</div>
                <div class="sheet-detail">VIP Turndown sequence initiated. Specific essential oil placement.</div>
                <div><span class="status-badge status-ready">Done</span></div>
            </div>
            <div class="sheet-row hidden-details" onclick="this.classList.toggle('hidden-details')">
                <div class="sheet-time">19:00</div>
                <div class="sheet-role">F&B Director</div>
                <div class="sheet-detail">Pre-service briefing in main restaurant. Focus on allergy mapping.</div>
                <div><span class="status-badge" style="background:rgba(255,255,255,0.1)">Pending</span></div>
            </div>
            <p style="font-size:0.8rem; color:var(--text-tertiary); text-align:center; margin-top:20px;">Click rows to unmask restricted details.</p>
        </div>
    </section>

    <!-- Section 10: Ambient Alerts -->
    <!-- Displayed dynamically via JS on bottom right -->
    <div class="alert-gallery" id="alert-gallery">
        <!-- Toasts injected via JS -->
    </div>

    <!-- Section 11: Testimonials -->
    <section class="container">
        <h2 class="serif" style="text-align:center; font-size: 2.5rem; margin-bottom: 2rem;">Voices of Hospitality</h2>
        <div class="testimonials">
            <div class="quote-card glass-panel">
                <p class="quote-text">Atelier Meridian finally gave our staff the digital equivalent of a finely tailored uniform. It moves with them.</p>
                <div class="quote-author">GM, Five Star Resort, London</div>
            </div>
            <div class="quote-card glass-panel">
                <p class="quote-text">We dropped our response times by forty percent simply because the system predicts the request before the guest dials the phone.</p>
                <div class="quote-author">VP Operations, Global Luxury Brand</div>
            </div>
            <div class="quote-card glass-panel">
                <p class="quote-text">It possesses an elegance I didn\'t think was possible in backend software. Our team actually enjoys looking at it.</p>
                <div class="quote-author">Director of IT, Private Members Club</div>
            </div>
        </div>
    </section>

    <!-- Section 12: Footer & Final CTA -->
    <footer>
        <div class="container">
            <h2 class="serif footer-cta">Elevate Your Standard.</h2>
            <button class="glow-btn" onclick="openModal()">Initialize Trial Protocol</button>
            
            <div style="margin-top: var(--space-xl);">
                <div class="nav-logo serif" style="margin-bottom: 20px;">Atelier Meridian</div>
                <div class="footer-links">
                    <a href="#">Manifesto</a>
                    <a href="#">Security</a>
                    <a href="#">Careers</a>
                    <a href="#">Press</a>
                    <a href="#">Contact Desk</a>
                </div>
                <p class="copyright">&copy; 2025-2026 Atelier Meridian Ops LLC. Designed for the exceptional.</p>
            </div>
        </div>
    </footer>

    <!-- Modal Form -->
    <div class="modal-overlay" id="access-modal">
        <div class="modal conic-border">
            <button class="close-modal" onclick="closeModal()">&times;</button>
            <h2 class="serif" style="font-size:2rem; margin-bottom:10px;">Request Access</h2>
            <p style="color:var(--text-secondary); margin-bottom:20px;">For qualified portfolios only.</p>
            <form id="contact-form" onsubmit="event.preventDefault(); submitForm();">
                <div style="margin-bottom: 15px;">
                    <label style="display:block; font-size:0.8rem; margin-bottom:5px; text-transform:uppercase; letter-spacing:1px; color:var(--text-tertiary)">Property Name</label>
                    <input type="text" required style="width:100%; padding:12px; background:rgba(0,0,0,0.5); border:1px solid var(--glass-border); color:#fff; border-radius:4px; font-family:inherit;">
                </div>
                <div style="margin-bottom: 15px;">
                    <label style="display:block; font-size:0.8rem; margin-bottom:5px; text-transform:uppercase; letter-spacing:1px; color:var(--text-tertiary)">Work Email</label>
                    <input type="email" required style="width:100%; padding:12px; background:rgba(0,0,0,0.5); border:1px solid var(--glass-border); color:#fff; border-radius:4px; font-family:inherit;">
                </div>
                <button type="submit" class="btn-primary" style="width:100%; margin-top:10px;">Transmit Request</button>
            </form>
            <div id="form-success" style="display:none; text-align:center; padding: 20px 0;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--status-recovered)" stroke-width="2" style="margin-bottom:10px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/></svg>
                <h3 style="color:var(--status-recovered)">Request Received</h3>
                <p style="font-size:0.9rem; color:var(--text-secondary);">An associate will review your portfolio.</p>
            </div>
        </div>
    </div>

    <!-- Script wiring -->
    <script>
        // 1. Sticky Nav Shrink
        window.addEventListener('scroll', () => {
            const nav = document.getElementById('navbar');
            if(window.scrollY > 50) {
                nav.style.padding = '8px 16px';
                nav.firstElementChild.style.background = 'rgba(255, 255, 255, 0.08)';
            } else {
                nav.style.padding = '16px 32px';
                nav.firstElementChild.style.background = 'rgba(255, 255, 255, 0.06)';
            }
        });

        // 2. Tabs logic
        function switchTab(evt, tabId) {
            const tabs = document.querySelectorAll('.console-tab');
            const contents = document.querySelectorAll('.tab-content');
            
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));
            
            evt.currentTarget.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        }

        // 3. Accordion logic
        function toggleAccordion(header) {
            const item = header.parentElement;
            const isOpen = item.classList.contains('open');
            
            // Close all
            document.querySelectorAll('.accordion-item').forEach(acc => {
                acc.classList.remove('open');
            });

            // Open clicked if it wasn't open
            if(!isOpen) {
                item.classList.add('open');
            }
        }

        // 4. Modal logic
        const modal = document.getElementById('access-modal');
        function openModal() {
            modal.classList.add('active');
            document.getElementById('contact-form').style.display = 'block';
            document.getElementById('form-success').style.display = 'none';
            document.getElementById('contact-form').reset();
        }
        function closeModal() {
            modal.classList.remove('active');
        }
        function submitForm() {
            document.getElementById('contact-form').style.display = 'none';
            document.getElementById('form-success').style.display = 'block';
            setTimeout(() => { closeModal(); }, 2500);
        }

        // Close modal on outside click
        modal.addEventListener('click', (e) => {
            if(e.target === modal) closeModal();
        });

        // 5. Timeline Intersection Observer
        const observerOpts = { threshold: 0.5 };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                }
            });
        }, observerOpts);

        document.querySelectorAll('.timeline-item').forEach(item => {
            observer.observe(item);
        });

        // 6. Count-up and Bar Chart Animation on scroll
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    // Trigger charts
                    document.querySelectorAll('.chart-bar').forEach(bar => {
                        bar.style.height = bar.getAttribute('data-target');
                    });
                    
                    // Trigger counters
                    if(!entry.target.classList.contains('counted')) {
                        document.querySelectorAll('.count-up').forEach(counter => {
                            const target = +counter.getAttribute('data-target');
                            const duration = 2000; // 2 seconds
                            const step = target / (duration / 16);
                            let current = 0;
                            
                            const updateCounter = () => {
                                current += step;
                                if(current < target) {
                                    counter.innerText = Math.ceil(current);
                                    requestAnimationFrame(updateCounter);
                                } else {
                                    counter.innerText = target;
                                }
                            };
                            updateCounter();
                        });
                        entry.target.classList.add('counted');
                    }
                }
            });
        }, { threshold: 0.2 });
        
        const statsSection = document.getElementById('stats');
        if(statsSection) {
            statsObserver.observe(statsSection.parentElement);
        }

        // 7. Ambient Alert Gallery (Toasts)
        const mockAlerts = [
            { title: 'VIP Arrival: T-10 Mins', desc: 'Mr. & Mrs. Vance approaching Geofence.', status: 'ready' },
            { title: 'Housekeeping Sync', desc: 'Turndown started for Penthouse A.', status: 'recovered' },
            { title: 'Inventory Warning', desc: 'Sparkling water stock below threshold at Pool Bar.', status: 'risk' },
            { title: 'Maintenance Closed', elevator: 'Elevator 4 restored to service.', status: 'ready' }
        ];

        let alertIndex = 0;
        function showNextAlert() {
            if(alertIndex >= mockAlerts.length) alertIndex = 0;
            const alertData = mockAlerts[alertIndex];
            
            const toast = document.createElement('div');
            toast.className = 'toast';
            
            let borderColor = 'var(--status-ready)';
            if(alertData.status === 'risk') borderColor = 'var(--status-risk)';
            if(alertData.status === 'recovered') borderColor = 'var(--status-recovered)';
            toast.style.borderLeftColor = borderColor;

            toast.innerHTML = 
                <div class="toast-title"></div>
                <div class="toast-desc"></div>
            ;
            
            const gallery = document.getElementById('alert-gallery');
            gallery.appendChild(toast);
            
            // Trigger animation
            setTimeout(() => { toast.classList.add('show'); }, 100);
            
            // Remove after 4s
            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => { toast.remove(); }, 500);
            }, 4000);

            alertIndex++;
        }

        // Cycle alerts every 6 seconds
        setInterval(showNextAlert, 6000);
        // Show first alert after 2 seconds
        setTimeout(showNextAlert, 2000);

    </script>
</body>
</html>'''

with open('fdu_009/src/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content.strip())
