import os

html_content = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drift Ledger | Maritime Intelligence Platform</title>
    <style>
        :root {
            /* Oceanic Core Colors */
            --dl-abyssal: #020617;
            --dl-deep-navy: #0f172a;
            --dl-carbon: #1e293b;
            
            /* Glow and Accent */
            --dl-cyan: #06b6d4;
            --dl-turq: #2dd4bf;
            --dl-hazard: #f59e0b;
            --dl-magenta: #d946ef;
            --dl-success: #10b981;
            
            /* Glass system */
            --glass-bg: rgba(15, 23, 42, 0.6);
            --glass-bg-hover: rgba(30, 41, 59, 0.7);
            --glass-border: rgba(6, 182, 212, 0.2);
            --glass-border-bright: rgba(6, 182, 212, 0.5);
            --glass-blur: blur(16px);
            --glass-inset: inset 0 0 0 1px rgba(255, 255, 255, 0.05);

            /* Typography */
            --font-sans: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: "ui-monospace", "SFMono-Regular", Menlo, Monaco, Consolas, monospace;
            
            --text-primary: #f8fafc;
            --text-muted: #94a3b8;
            --text-inverse: #020617;
            
            /* Spacing and Radius */
            --space-1: 0.25rem;
            --space-2: 0.5rem;
            --space-3: 1rem;
            --space-4: 2rem;
            --space-5: 4rem;
            --space-6: 8rem;
            
            --radius-sm: 0.25rem;
            --radius-md: 0.5rem;
            --radius-lg: 1rem;
            --radius-xl: 1.5rem;
            --radius-full: 9999px;
            
            /* Motion */
            --bounce: cubic-bezier(0.175, 0.885, 0.32, 1.275);
            --fluid: cubic-bezier(0.4, 0, 0.2, 1);
            --duration-fast: 150ms;
            --duration-med: 300ms;
            --duration-slow: 700ms;
        }

        /* Reset */
        * { box-sizing: border-box; margin: 0; padding: 0; }
        html { scroll-behavior: smooth; }
        body {
            font-family: var(--font-sans);
            background-color: var(--dl-abyssal);
            color: var(--text-primary);
            line-height: 1.6;
            overflow-x: hidden;
            position: relative;
        }

        /* Skip link */
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: var(--dl-cyan);
            color: var(--dl-abyssal);
            padding: 8px;
            z-index: 9999;
            transition: top 0.2s;
        }
        .skip-link:focus { top: 0; }

        /* Ambient Orbs */
        .ambient-orbs {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: -1;
            overflow: hidden;
        }
        .orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(120px);
            opacity: 0.4;
            animation: drift 20s infinite alternate var(--fluid);
        }
        .orb-1 { width: 50vw; height: 50vw; background: var(--dl-cyan); top: -10%; left: -10%; }
        .orb-2 { width: 40vw; height: 40vw; background: var(--dl-turq); bottom: 10%; right: -10%; animation-delay: -5s; }
        .orb-3 { width: 30vw; height: 30vw; background: var(--dl-deep-navy); top: 40%; left: 40%; animation-duration: 25s; }
        
        @keyframes drift {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(10vw, 5vh) scale(1.1); }
        }

        @media (prefers-reduced-motion) {
            .orb { animation: none; opacity: 0.2; }
            html { scroll-behavior: auto; }
            * { transition-duration: 0.01ms !important; animation-duration: 0.01ms !important; }
        }

        /* Glass Panel Utility */
        .glass-panel {
            background: var(--glass-bg);
            backdrop-filter: var(--glass-blur);
            border: 1px solid var(--glass-border);
            box-shadow: var(--glass-inset), 0 10px 30px rgba(0,0,0,0.3);
            border-radius: var(--radius-lg);
            transition: all var(--duration-med) var(--fluid);
        }
        .glass-panel:hover {
            border-color: var(--glass-border-bright);
            box-shadow: var(--glass-inset), 0 15px 40px rgba(0,255,255,0.1);
        }

        /* Conic Borders */
        .conic-border {
            position: relative;
            z-index: 1;
        }
        .conic-border::before {
            content: "";
            position: absolute;
            inset: -2px;
            border-radius: inherit;
            background: conic-gradient(from var(--angle, 0deg), var(--dl-cyan), var(--dl-turq), transparent 60%);
            z-index: -1;
            opacity: 0;
            transition: opacity var(--duration-med);
            animation: rotate_border 4s linear infinite;
        }
        .conic-border:hover::before { opacity: 1; }
        
        @property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }
        @keyframes rotate_border { to { --angle: 360deg; } }

        /* Typography utils */
        .display-text { font-size: clamp(3rem, 6vw, 5.5rem); font-weight: 700; letter-spacing: -0.03em; line-height: 1.1; }
        .font-mono { font-family: var(--font-mono); font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.05em; }
        .text-glow { text-shadow: 0 0 20px rgba(6, 182, 212, 0.5); }
        .text-gradient {
            background: linear-gradient(to right, #fff, var(--dl-cyan));
            -webkit-background-clip: text; color: transparent;
        }

        /* Buttons */
        .btn {
            display: inline-flex; align-items: center; justify-content: center;
            padding: 0.75rem 1.5rem; font-weight: 600; text-decoration: none;
            border-radius: var(--radius-md); transition: all var(--duration-fast);
            cursor: pointer; font-family: var(--font-mono); border: none;
            position: relative; overflow: hidden;
        }
        .btn:focus-visible { outline: 2px solid var(--dl-cyan); outline-offset: 4px; }
        .btn-primary { background: var(--dl-cyan); color: var(--dl-abyssal); box-shadow: 0 0 15px rgba(6, 182, 212, 0.4); }
        .btn-primary:hover { background: #0891b2; box-shadow: 0 0 25px rgba(6, 182, 212, 0.6); transform: translateY(-2px); }
        .btn-glass { background: var(--glass-bg); color: var(--text-primary); border: 1px solid var(--glass-border); backdrop-filter: blur(8px); }
        .btn-glass:hover { background: var(--glass-bg-hover); border-color: var(--dl-cyan); }

        /* Focus trap */
        .focus-visible-only:focus:not(:focus-visible) { outline: none; }

        /* Layout & Sections */
        .container { max-width: 1440px; margin: 0 auto; padding: 0 5%; }
        section { padding: var(--space-6) 0; position: relative; }

        /* 1. Navbar */
        .navbar {
            position: fixed; top: 0; left: 0; width: 100%; z-index: 100;
            padding: 1.5rem 5%; transition: all var(--duration-med);
            border-bottom: 1px solid transparent;
        }
        .navbar.scrolled {
            padding: 0.75rem 5%; background: rgba(2, 6, 23, 0.85);
            backdrop-filter: var(--glass-blur); border-bottom-color: var(--glass-border);
        }
        .nav-inner { display: flex; justify-content: space-between; align-items: center; }
        .brand { font-weight: 700; font-size: 1.25rem; letter-spacing: 0.1em; display: flex; align-items: center; gap: 0.5rem; }
        .brand svg { width: 24px; height: 24px; fill: var(--dl-cyan); }
        .nav-links { display: flex; gap: 2rem; list-style: none; }
        .nav-links a { color: var(--text-muted); text-decoration: none; font-size: 0.875rem; transition: color var(--duration-fast); }
        .nav-links a:hover, .nav-links a.active { color: var(--dl-cyan); }
        .ocean-badge {
            display: inline-flex; align-items: center; gap: 0.5rem;
            padding: 0.25rem 0.75rem; border-radius: var(--radius-full);
            background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2);
            color: var(--dl-success); font-family: var(--font-mono); font-size: 0.75rem;
        }
        .ocean-badge .pulse {
            width: 6px; height: 6px; background: var(--dl-success); border-radius: 50%;
            animation: ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
        }
        @keyframes ping { 75%, 100% { transform: scale(2.5); opacity: 0; } }
        .menu-btn { display: none; background: transparent; border: none; color: white; cursor: pointer;}
        .menu-btn svg { width: 24px; height: 24px; }

        /* 2. Hero */
        .hero {
            min-height: 100vh; display: flex; align-items: center; padding-top: 6rem;
            position: relative; overflow: hidden;
        }
        .hero-content {
            max-width: 800px; position: relative; z-index: 10;
        }
        .hero-sub { color: var(--dl-cyan); font-family: var(--font-mono); margin-bottom: 1rem; display: block; }
        .hero-desc { font-size: 1.25rem; color: var(--text-muted); margin: 2rem 0; max-width: 600px; }
        .hero-actions { display: flex; gap: 1rem; }
        .hero-graphics {
            position: absolute; right: -5%; top: 50%; transform: translateY(-50%);
            width: 60%; height: 80%; pointer-events: none; opacity: 0.6;
        }
        .route-svg { width: 100%; height: 100%; overflow: visible; }
        .route-line {
            fill: none; stroke: var(--dl-cyan); stroke-width: 2;
            stroke-dasharray: 1000; stroke-dashoffset: 1000;
            animation: drawLine 4s ease-in-out forwards infinite;
        }
        @keyframes drawLine { to { stroke-dashoffset: 0; } }

        /* 3. Trust Strip */
        .trust-strip {
            padding: 3rem 0; background: linear-gradient(90deg, transparent, rgba(30,41,59,0.5), transparent);
            border-top: 1px solid var(--glass-border); border-bottom: 1px solid var(--glass-border);
            text-align: center;
        }
        .trust-logo-grid {
            display: flex; justify-content: center; gap: 4rem; flex-wrap: wrap; margin-top: 1rem;
        }
        .trust-item { font-family: var(--font-mono); color: var(--text-muted); font-size: 1.1rem; letter-spacing: 0.1em; opacity: 0.7;}
        .stagger-item { opacity: 0; transform: translateY(20px); transition: all 0.6s var(--fluid); }
        .stagger-item.visible { opacity: 1; transform: translateY(0); }

        /* 4. Signal Grid */
        .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; }
        .signal-card { padding: 2rem; display: flex; flex-direction: column; gap: 1rem; }
        .signal-icon { width: 40px; height: 40px; fill: var(--dl-cyan); background: rgba(6,182,212,0.1); padding: 8px; border-radius: 8px; }
        .signal-card h3 { font-size: 1.25rem; font-weight: 600; }
        .signal-card p { color: var(--text-muted); font-size: 0.9rem; }

        /* 5. Scrollytelling Dossier */
        .dossier-layout { display: flex; gap: 4rem; align-items: flex-start; }
        .dossier-sticky { flex: 1; position: sticky; top: 120px; height: calc(100vh - 160px); }
        .dossier-chart-view { width: 100%; height: 100%; background: var(--dl-carbon); border-radius: var(--radius-lg); position: relative; overflow: hidden;}
        /* grid overlay for dossier */
        .dossier-chart-view::after {
            content:''; position:absolute; inset:0;
            background-image: linear-gradient(var(--glass-border) 1px, transparent 1px), linear-gradient(90deg, var(--glass-border) 1px, transparent 1px);
            background-size: 20px 20px; opacity: 0.2; pointer-events: none;
        }
        .dossier-overlay { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s; }
        .dossier-overlay.active { opacity: 1; }
        .dossier-overlay span { font-family: var(--font-mono); font-size: 1.5rem; color: var(--dl-cyan); text-shadow: 0 0 10px var(--dl-cyan); background: rgba(0,0,0,0.5); padding: 1rem 2rem; border: 1px solid var(--dl-cyan); border-radius: 8px; }
        .dossier-scroll { flex: 1; display: flex; flex-direction: column; gap: 50vh; padding-top: 20vh; padding-bottom: 50vh; }
        .dossier-step { padding: 2rem; border-left: 2px solid var(--glass-border); transition: border-color 0.3s; }
        .dossier-step.active { border-color: var(--dl-cyan); }
        .dossier-step h4 { font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-muted); transition: color 0.3s; }
        .dossier-step.active h4 { color: white; }

        /* 6. Interactive Control Room (Tabs) */
        .control-room { display: flex; flex-direction: column; gap: 2rem; }
        .tabs-header { display: flex; gap: 1rem; border-bottom: 1px solid var(--glass-border); padding-bottom: 1rem; overflow-x: auto; }
        .tab-btn {
            background: transparent; color: var(--text-muted); border: 1px solid transparent;
            padding: 0.75rem 1.5rem; font-family: var(--font-mono); cursor: pointer; border-radius: var(--radius-md);
            transition: all 0.3s; white-space: nowrap;
        }
        .tab-btn:hover { color: white; background: rgba(255,255,255,0.05); }
        .tab-btn[aria-selected="true"] { color: var(--dl-cyan); background: rgba(6,182,212,0.1); border-color: var(--dl-cyan); box-shadow: 0 0 10px rgba(6,182,212,0.2); }
        .tab-panels { position: relative; min-height: 400px; }
        .tab-panel { position: absolute; inset: 0; opacity: 0; pointer-events: none; transition: opacity 0.4s ease; display:flex; flex-direction: column;}
        .tab-panel.active { opacity: 1; pointer-events: all; position: relative; }
        
        .route-replay-ctrl { display: flex; align-items: center; gap: 1rem; margin-top: 1rem; background: var(--dl-carbon); padding: 1rem; border-radius: var(--radius-md); }
        .replay-slider { flex: 1; accent-color: var(--dl-cyan); cursor: pointer; }
        #replay-value { font-family: var(--font-mono); color: var(--dl-hazard); width: 100px; text-align:right;}

        /* 7. Metrics Band */
        .metrics-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; }
        .metric-card { text-align: center; padding: 2rem 1rem; }
        .metric-val { font-size: 3.5rem; font-weight: 700; color: white; font-family: var(--font-mono); display: flex; justify-content: center; align-items: baseline; gap: 0.5rem;}
        .metric-unit { font-size: 1.2rem; color: var(--dl-cyan); font-weight: normal; }
        .metric-label { color: var(--text-muted); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0.5rem; }

        /* 8. Disruption Timeline */
        .timeline { max-width: 800px; margin: 0 auto; position: relative; padding-left: 2rem; }
        .timeline::before { content:''; position: absolute; left: 0; top:0; bottom:0; width: 2px; background: var(--glass-border); }
        .timeline-item { position: relative; margin-bottom: 3rem; padding-left: 2rem; }
        .timeline-node {
            position: absolute; left: -2.3rem; top: 0.2rem; width: 1rem; height: 1rem;
            border-radius: 50%; background: var(--dl-abyssal); border: 2px solid var(--text-muted);
            box-shadow: 0 0 10px rgba(0,0,0,0.5); z-index: 2; transition: all 0.5s;
        }
        .timeline-item.active .timeline-node { border-color: var(--dl-hazard); background: var(--dl-hazard); box-shadow: 0 0 15px var(--dl-hazard); }
        .time-label { font-family: var(--font-mono); color: var(--text-muted); margin-bottom: 0.25rem; font-size: 0.85rem; }
        .timeline-content { background: var(--glass-bg); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--glass-border); }
        
        /* 9. Comparison Memo */
        .comparison-wrapper { display: grid; grid-template-columns: 1fr 1fr; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--glass-border); }
        .comp-col { padding: 4rem; display: flex; flex-direction: column; gap: 2rem; }
        .comp-legacy { background: var(--dl-carbon); }
        .comp-drift { background: linear-gradient(135deg, var(--dl-abyssal), rgba(6,182,212,0.1)); position: relative; }
        .comp-drift::after { content:''; position:absolute; inset:0; border: 1px solid var(--dl-cyan); opacity:0.3; pointer-events:none;}
        .comp-list { list-style: none; display: flex; flex-direction: column; gap: 1.5rem; }
        .comp-list li { display: flex; gap: 1rem; align-items: flex-start; }
        .comp-list svg { width: 20px; height: 20px; flex-shrink:0; margin-top:4px;}
        .comp-legacy svg { fill: var(--dl-hazard); }
        .comp-drift svg { fill: var(--dl-cyan); }
        .comp-list h5 { font-size: 1.1rem; margin-bottom: 0.25rem; }
        .comp-list p { color: var(--text-muted); font-size:0.9rem;}

        /* 10. Forecast Bulletin */
        .bulletin-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
        .bulletin-card { position:relative; overflow:hidden;}
        .bulletin-card .tag { position:absolute; top: 1rem; right: 1rem; background: rgba(245, 158, 11, 0.2); color: var(--dl-hazard); padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.7rem; font-family: var(--font-mono); }
        
        /* 11. Compliance */
        .compliance-block { text-align: center; max-width: 800px; margin: 0 auto; }
        .compliance-block h2 { font-size: 2.5rem; margin-bottom: 1rem; }

        /* 12. FAQ Accordion */
        .faq-list { max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem; }
        .accordion-item { border: 1px solid var(--glass-border); border-radius: var(--radius-md); overflow: hidden; background: var(--glass-bg); }
        .accordion-header {
            width: 100%; text-align: left; padding: 1.5rem; background: transparent; border: none;
            color: white; font-size: 1.1rem; font-weight: 500; cursor: pointer; display: flex; justify-content: space-between; align-items: center;
        }
        .accordion-header:focus-visible { outline: 2px solid var(--dl-cyan); outline-offset:-2px;}
        .accordion-icon { width: 20px; height: 20px; transition: transform 0.3s; fill: var(--dl-cyan); }
        .accordion-item.open .accordion-icon { transform: rotate(180deg); }
        .accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.4s var(--fluid); }
        .accordion-inner { padding: 0 1.5rem 1.5rem 1.5rem; color: var(--text-muted); border-top: 1px solid rgba(255,255,255,0.05); margin-top: 0.5rem; padding-top: 1rem; }

        /* 13. Final CTA Form */
        .cta-container { max-width: 600px; margin: 0 auto; text-align: center; }
        .cta-form { display: flex; flex-direction: column; gap: 1rem; margin-top: 2rem; }
        .form-input {
            width: 100%; padding: 1rem; background: rgba(0,0,0,0.5); border: 1px solid var(--glass-border);
            border-radius: var(--radius-md); color: white; font-family: var(--font-mono); transition: all 0.3s;
        }
        .form-input:focus { outline: none; border-color: var(--dl-cyan); box-shadow: 0 0 15px rgba(6,182,212,0.3); }

        /* 14. Footer */
        .footer { padding: 4rem 5% 2rem; border-top: 1px solid var(--glass-border); background: var(--dl-abyssal); margin-top: 4rem; }
        .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 2rem; margin-bottom: 4rem; }
        .footer-links h4 { color: white; margin-bottom: 1.5rem; font-size: 1rem; }
        .footer-links ul { list-style: none; display: flex; flex-direction: column; gap: 0.75rem; }
        .footer-links a { color: var(--text-muted); text-decoration: none; font-size: 0.85rem; transition: color 0.3s; }
        .footer-links a:hover { color: var(--dl-cyan); }
        .footer-bottom { border-top: 1px solid rgba(255,255,255,0.05); padding-top: 2rem; display: flex; justify-content: space-between; color: var(--text-muted); font-size: 0.8rem; }

        /* Modal */
        .modal-overlay {
            position: fixed; inset: 0; background: rgba(2,6,23,0.8); backdrop-filter: blur(10px);
            z-index: 1000; display: flex; align-items: center; justify-content: center;
            opacity: 0; pointer-events: none; transition: opacity 0.3s;
        }
        .modal-overlay.open { opacity: 1; pointer-events: all; }
        .modal-content {
            background: var(--dl-carbon); width: 90%; max-width: 600px;
            border-radius: var(--radius-lg); border: 1px solid var(--glass-border); box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            transform: translateY(20px) scale(0.95); transition: all 0.3s var(--bounce); padding: 2rem; position:relative;
        }
        .modal-overlay.open .modal-content { transform: translateY(0) scale(1); }
        .modal-close { position: absolute; top: 1rem; right: 1rem; background: transparent; border: none; color: white; cursor: pointer; border-radius:4px; padding:4px;}
        .modal-close:focus-visible { outline: 2px solid var(--dl-cyan); }
        .modal-close svg { width: 24px; height: 24px; fill: currentColor; }
        
        .modal-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; margin: 1.5rem 0; }
        .modal-summary { background: rgba(0,0,0,0.3); padding: 1rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.8rem; color: var(--dl-cyan); border: 1px solid rgba(6,182,212,0.2);}

        /* Toast */
        .toast-container { position: fixed; bottom: 2rem; right: 2rem; z-index: 9999; display: flex; flex-direction: column; gap: 1rem; }
        .toast {
            background: var(--dl-carbon); border: 1px solid var(--dl-success); border-left: 4px solid var(--dl-success);
            color: white; padding: 1rem 1.5rem; border-radius: var(--radius-md); box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            display: flex; align-items: center; justify-content: space-between; gap: 2rem;
            transform: translateX(120%); transition: transform 0.4s var(--bounce), opacity 0.4s; pointer-events:all;
        }
        .toast.show { transform: translateX(0); }
        .toast-close { background: none; border: none; color: var(--text-muted); cursor: pointer; }
        .toast-close:hover { color: white; }

        /* Media Queries */
        @media (max-width: 1023px) { /* Tablet */
            .display-text { font-size: 3.5rem; }
            .grid-4 { grid-template-columns: repeat(2, 1fr); }
            .dossier-layout { flex-direction: column; gap: 2rem; }
            .dossier-sticky { position: relative; top: 0; height: 400px; width: 100%; order: -1; }
            .dossier-scroll { flex-direction: row; overflow-x: auto; gap: 2rem; padding: 2rem 0; scroll-snap-type: x mandatory; }
            .dossier-step { min-width: 80vw; scroll-snap-align: center; border-left: none; border-top: 2px solid var(--glass-border); padding-top: 1rem; padding-left: 0; }
            .metrics-grid { grid-template-columns: repeat(2, 1fr); }
            .bulletin-grid { grid-template-columns: repeat(2, 1fr); }
            .comparison-wrapper { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr 1fr; }
        }
        @media (max-width: 767px) { /* Mobile */
            .display-text { font-size: 2.5rem; }
            .nav-links { display: none; }
            .menu-btn { display: block; }
            .grid-4 { grid-template-columns: 1fr; }
            .metrics-grid { grid-template-columns: 1fr; }
            .bulletin-grid { grid-template-columns: 1fr; }
            .tabs-header { scroll-snap-type: x mandatory; margin-bottom: 2rem; }
            .tab-btn { scroll-snap-align: start; }
            .footer-grid { grid-template-columns: 1fr; }
            .hero-graphics { opacity: 0.2; width: 100%; left: 0; }
            .comp-col { padding: 2rem; }
        }
    </style>
</head>
<body>
    <a href="#main" class="skip-link">Skip to main content</a>
    
    <div class="ambient-orbs" aria-hidden="true">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>

    <!-- 1. Navbar -->
    <header class="navbar" id="navbar">
        <div class="nav-inner">
            <div class="brand">
                <svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2zm0 4.5l6.5 13h-13L12 6.5z"/></svg>
                DRIFT LEDGER
            </div>
            <nav>
                <ul class="nav-links">
                    <li><a href="#features" class="active">Features</a></li>
                    <li><a href="#dossier">Routing</a></li>
                    <li><a href="#control-room">Console</a></li>
                    <li><a href="#faq">Intel</a></li>
                </ul>
            </nav>
            <div class="ocean-badge">
                <span class="pulse"></span>
                Swell: Nominal
            </div>
            <button class="menu-btn" aria-label="Menu">
                <svg viewBox="0 0 24 24"><path fill="currentColor" d="M3 6h18v2H3V6m0 5h18v2H3v-2m0 5h18v2H3v-2z"/></svg>
            </button>
        </div>
    </header>

    <main id="main">
        <!-- 2. Hero -->
        <section class="hero container">
            <div class="hero-content scroll-reveal">
                <span class="hero-sub font-mono">SYS.VER 7.4.2 // ONLINE</span>
                <h1 class="display-text">Navigate Risk.<br><span class="text-gradient">Ensure Continuity.</span></h1>
                <p class="hero-desc">The premier climate-risk routing platform. Anticipate terminal congestion, bypass storm swells, and reduce carbon intensity with algorithmic maritime intelligence.</p>
                <div class="hero-actions">
                    <button class="btn btn-primary" onclick="openModal()">Request Review</button>
                    <a href="#control-room" class="btn btn-glass">View Console</a>
                </div>
            </div>
            <div class="hero-graphics" aria-hidden="true">
                <svg class="route-svg" viewBox="0 0 800 600">
                    <path class="route-line" d="M100,500 Q300,400 400,200 T700,100" />
                    <!-- Nav grid lines -->
                    <g stroke="rgba(255,255,255,0.1)" stroke-width="1">
                        <line x1="0" y1="100" x2="800" y2="100"/>
                        <line x1="0" y1="200" x2="800" y2="200"/>
                        <line x1="0" y1="300" x2="800" y2="300"/>
                        <line x1="0" y1="400" x2="800" y2="400"/>
                        <line x1="100" y1="0" x2="100" y2="600"/>
                        <line x1="300" y1="0" x2="300" y2="600"/>
                        <line x1="500" y1="0" x2="500" y2="600"/>
                        <line x1="700" y1="0" x2="700" y2="600"/>
                    </g>
                    <!-- Threat marker -->
                    <circle cx="280" cy="380" r="40" fill="rgba(245, 158, 11, 0.2)" stroke="var(--dl-hazard)"/>
                    <circle cx="280" cy="380" r="4" fill="var(--dl-hazard)"/>
                </svg>
            </div>
        </section>

        <!-- 3. Trust Strip -->
        <section class="trust-strip container scroll-reveal">
            <p class="font-mono" style="color:var(--text-muted); margin-bottom:1rem;">CLEARANCE RATING SECURED BY LEADING OPERATORS</p>
            <div class="trust-logo-grid" id="trust-marks">
                <div class="trust-item stagger-item">MAERSK INT.</div>
                <div class="trust-item stagger-item">LLOYD'S SYNDICATE</div>
                <div class="trust-item stagger-item">PORT OF ROTTERDAM</div>
                <div class="trust-item stagger-item">HAPAG-LLOYD</div>
            </div>
        </section>

        <!-- 4. Signal Grid -->
        <section id="features" class="container scroll-reveal">
            <h2 class="display-text" style="font-size:2.5rem; margin-bottom: 3rem;">Core Subsystems</h2>
            <div class="grid-4" id="signal-cards">
                <div class="glass-panel conic-border signal-card stagger-item">
                    <svg class="signal-icon" viewBox="0 0 24 24"><path d="M12 2L2 12l10 10 10-10L12 2zm0 3.5l6.5 6.5-6.5 6.5L5.5 12 12 5.5z"/></svg>
                    <h3>Meteo-Forecasting</h3>
                    <p>Integrates 14 global weather models to predict swells, squalls, and thermal expansions up to 21 days out.</p>
                </div>
                <div class="glass-panel conic-border signal-card stagger-item">
                    <svg class="signal-icon" viewBox="0 0 24 24"><path d="M21 3H3v18h18V3zm-2 16H5V5h14v14zm-5-9h-4v4h4v-4z"/></svg>
                    <h3>Dynamic Routing</h3>
                    <p>Algorithmic lane generation minimizing exposure to extreme weather while optimizing fuel usage and ETA variance.</p>
                </div>
                <div class="glass-panel conic-border signal-card stagger-item">
                    <svg class="signal-icon" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.5 3.8 10.7 9 12 5.2-1.3 9-6.5 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>
                    <h3>Underwriting View</h3>
                    <p>Granular risk exposure metrics satisfying insurer reporting needs and lowering premium multipliers.</p>
                </div>
                <div class="glass-panel conic-border signal-card stagger-item">
                    <svg class="signal-icon" viewBox="0 0 24 24"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
                    <h3>Compliance Index</h3>
                    <p>Automated EU ETS accounting and CII grade predictions per voyage based on route characteristics.</p>
                </div>
            </div>
        </section>

        <!-- 5. Scrollytelling Dossier -->
        <section id="dossier" class="container">
            <div class="dossier-layout">
                <div class="dossier-sticky glass-panel" aria-hidden="true">
                    <div class="dossier-chart-view" id="dossier-visual">
                        <div class="dossier-overlay active" id="ov-1"><span>STATUS: MONITORING</span></div>
                        <div class="dossier-overlay" id="ov-2"><span style="color:var(--dl-hazard); border-color:var(--dl-hazard);">ALERT: SWELL > 8M</span></div>
                        <div class="dossier-overlay" id="ov-3"><span style="color:var(--dl-magenta); border-color:var(--dl-magenta);">REROUTING COMPLETED</span></div>
                    </div>
                </div>
                <div class="dossier-scroll">
                    <div class="dossier-step active" data-step="1">
                        <span class="font-mono">T-48:00</span>
                        <h4>Continuous Baseline Monitoring</h4>
                        <p>Drift Ledger maintains a passive scan over the assigned oceanic corridor. The baseline model processes current fuel consumption and planned waypoints against historical averages. In this state, operational load is minimal, and metrics reflect a standard trajectory.</p>
                    </div>
                    <div class="dossier-step" data-step="2">
                        <span class="font-mono" style="color:var(--dl-hazard)">T-12:00</span>
                        <h4>Anomaly Detection & Flagging</h4>
                        <p>The system detects an impending anomalous swell configuration directly traversing the planned route. Watch thresholds are breeched. Insurers require a log of actionable alternatives. The system instantly generates risk profiles for remaining on course.</p>
                    </div>
                    <div class="dossier-step" data-step="3">
                        <span class="font-mono" style="color:var(--dl-magenta)">T-00:00</span>
                        <h4>Algorithmic Deviation Matrix</h4>
                        <p>A new route is compiled and transmitted. By altering heading by 12 degrees south, the asset avoids the critical high-swell band, adding only 4 hours to the voyage while eliminating 94% of cargo liability risk and satisfying port continuity windows.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 6. Interactive Control Room -->
        <section id="control-room" class="container scroll-reveal">
            <h2 class="display-text" style="font-size:2.5rem; margin-bottom: 2rem;">Operational Console</h2>
            <div class="glass-panel conic-border p-4" style="padding: 2rem;">
                <div role="tablist" class="tabs-header" aria-label="Control Room Views">
                    <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1" tabindex="0" class="tab-btn">Routing View</button>
                    <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2" tabindex="-1" class="tab-btn">Port Continuity</button>
                    <button role="tab" aria-selected="false" aria-controls="panel-3" id="tab-3" tabindex="-1" class="tab-btn">Underwriting</button>
                    <button role="tab" aria-selected="false" aria-controls="panel-4" id="tab-4" tabindex="-1" class="tab-btn">Compliance</button>
                </div>
                <div class="tab-panels">
                    <div id="panel-1" role="tabpanel" tabindex="0" class="tab-panel active" aria-labelledby="tab-1">
                        <h3 style="margin: 1rem 0; font-family:var(--font-mono); color:var(--dl-cyan);">LANE FORECAST AND ROUTE REPLAY</h3>
                        <p style="color:var(--text-muted); margin-bottom: 1.5rem;">Review the projected path interaction with meteorological anomalies. Drag the scrubber to advance time.</p>
                        <!-- Inline SVG Route Replay -->
                        <div style="width:100%; height: 250px; background:var(--dl-abyssal); border-radius:8px; position:relative; overflow:hidden;">
                            <svg viewBox="0 0 1000 250" style="width:100%; height:100%;">
                                <path d="M50,125 L950,125" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
                                <path id="replay-path" d="M50,125 Q250,50 500,125 T950,125" fill="none" stroke="var(--dl-cyan)" stroke-width="3" stroke-dasharray="1000" stroke-dashoffset="1000" />
                                <circle id="replay-ship" cx="50" cy="125" r="8" fill="var(--dl-magenta)" />
                            </svg>
                        </div>
                        <div class="route-replay-ctrl">
                            <span class="font-mono">T-MINUS</span>
                            <input type="range" class="replay-slider" id="scrubber" min="0" max="100" value="0" aria-label="Route Replay Scrubber">
                            <span id="replay-value">0%</span>
                        </div>
                        <div style="margin-top: 1rem;">
                            <button class="btn btn-glass" onclick="showToast('Route briefing parameters saved to local registry.')">Save Briefing</button>
                        </div>
                    </div>
                    <div id="panel-2" role="tabpanel" tabindex="0" class="tab-panel" aria-labelledby="tab-2" hidden>
                        <h3 style="margin: 1rem 0; font-family:var(--font-mono); color:var(--dl-turq);">PORT CONGESTION & BERTH LOGIC</h3>
                        <p style="color:var(--text-muted);">Anticipate downstream impacts of weather delays. When vessels arrive off-schedule, berth windows collapse. Drift Ledger models port queuing based on real-time macro vessel movements, suggesting speed adjustments to arrive exactly at newly opened windows, preventing wasteful anchorage idling.</p>
                    </div>
                    <div id="panel-3" role="tabpanel" tabindex="0" class="tab-panel" aria-labelledby="tab-3" hidden>
                        <h3 style="margin: 1rem 0; font-family:var(--font-mono); color:var(--dl-hazard);">UNDERWRITING & RISK EXPOSURE EXPORT</h3>
                        <p style="color:var(--text-muted);">Marine insurers require auditable proof of risk avoidance. Drift Ledger packages voyage data into cryptographic ledger entries detailing the exact sea state avoided and the decision matrix used. This satisfies clauses regarding "due diligence in routing" and protects against liability claims.</p>
                    </div>
                    <div id="panel-4" role="tabpanel" tabindex="0" class="tab-panel" aria-labelledby="tab-4" hidden>
                        <h3 style="margin: 1rem 0; font-family:var(--font-mono); color:var(--dl-success);">REGULATORY & EMISSIONS INDEXING</h3>
                        <p style="color:var(--text-muted);">Rerouting often implies longer distances, but not necessarily higher fuel consumption if headwinds and swells are avoided. The compliance view provides real-time EU ETS cost estimations and projects the end-of-voyage CII rating precisely, preventing regulatory fines.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 7. Metrics Band -->
        <section class="container scroll-reveal">
            <div class="glass-panel p-4" style="padding: 3rem 2rem;">
                <div class="metrics-grid" id="metrics">
                    <div class="metric-card">
                        <div class="metric-val"><span class="count-up" data-target="320">0</span> <span class="metric-unit">k</span></div>
                        <div class="metric-label">Voyages Analyzed</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val"><span class="count-up" data-target="94">0</span> <span class="metric-unit">%</span></div>
                        <div class="metric-label">Hazard Avoidance</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val"><span class="count-up" data-target="15">0</span> <span class="metric-unit">%</span></div>
                        <div class="metric-label">Fuel Reduction Vol.</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val"><span class="count-up" data-target="12">0</span> <span class="metric-unit">hrs</span></div>
                        <div class="metric-label">Avg. Port Delay Avoided</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 8. Disruption Timeline -->
        <section class="container scroll-reveal">
            <h2 class="display-text" style="font-size:2.5rem; text-align:center; margin-bottom: 4rem;">Incident Response Log</h2>
            <div class="timeline" id="timeline">
                <div class="timeline-item stagger-item">
                    <div class="timeline-node"></div>
                    <div class="timeline-content">
                        <div class="time-label">04:22 UTC | LAT 45.2, LON -30.1</div>
                        <h4>Cyclone Formation Detected</h4>
                        <p>Early stage low-pressure system identified. Confidence interval exceeds 85% for route intersection.</p>
                    </div>
                </div>
                <div class="timeline-item stagger-item">
                    <div class="timeline-node"></div>
                    <div class="timeline-content">
                        <div class="time-label">05:10 UTC | LOG: SYSTEM</div>
                        <h4>Threshold Breach: Watch to Warning</h4>
                        <p>Projected significant wave height (SWH) increased to 9.2 meters. System auto-escalates threat matrix.</p>
                    </div>
                </div>
                <div class="timeline-item stagger-item">
                    <div class="timeline-node"></div>
                    <div class="timeline-content">
                        <div class="time-label">05:15 UTC | ACTION: ALGORITHM</div>
                        <h4>Kinematic Avoidance Path Generated</h4>
                        <p>5 alternative routes computed. Optimal route selected minimizing fuel delta while ensuring SWH < 4m.</p>
                    </div>
                </div>
                <div class="timeline-item stagger-item">
                    <div class="timeline-node"></div>
                    <div class="timeline-content">
                        <div class="time-label">06:00 UTC | PORT: CONTINUITY</div>
                        <h4>ETA Adjusted & Berth Re-secured</h4>
                        <p>Destination terminal API queried. New ETA slots injected. Zero waiting time at anchorage confirmed.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 9. Comparison Memo -->
        <section class="container scroll-reveal">
            <div class="comparison-wrapper">
                <div class="comp-col comp-legacy">
                    <h3 class="font-mono text-muted mb-4">LEGACY WORKFLOWS</h3>
                    <ul class="comp-list">
                        <li>
                            <svg viewBox="0 0 24 24"><path d="M19 6.41L8.7 16.71l-3.3-3.3L4 14.83l4.7 4.7 11.7-11.7z"/></svg>
                            <div>
                                <h5>Static Weather Packets</h5>
                                <p>PDFs sent twice daily. Quickly outdated and lacking asset-specific granular data.</p>
                            </div>
                        </li>
                        <li>
                            <svg viewBox="0 0 24 24"><path d="M19 6.41L8.7 16.71l-3.3-3.3L4 14.83l4.7 4.7 11.7-11.7z"/></svg>
                            <div>
                                <h5>Manual Captain Discretion</h5>
                                <p>Onus entirely on the Master, heavily subjective without global optimization context.</p>
                            </div>
                        </li>
                        <li>
                            <svg viewBox="0 0 24 24"><path d="M19 6.41L8.7 16.71l-3.3-3.3L4 14.83l4.7 4.7 11.7-11.7z"/></svg>
                            <div>
                                <h5>Fragmented Port Coordination</h5>
                                <p>Arriving at port unaware of local queue states leading to expensive anchored idling.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="comp-col comp-drift">
                    <h3 class="font-mono mb-4" style="color:var(--dl-cyan)">DRIFT LEDGER PLATFORM</h3>
                    <ul class="comp-list">
                        <li>
                            <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                            <div>
                                <h5>Live Multi-Model Streaming</h5>
                                <p>Continuous ingest of global met-ocean APIs computing dynamic polygon hazard zones.</p>
                            </div>
                        </li>
                        <li>
                            <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                            <div>
                                <h5>Algorithmic Objective Execution</h5>
                                <p>System-derived directives balancing safety, fuel curve geometry, and exact time windows.</p>
                            </div>
                        </li>
                        <li>
                            <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                            <div>
                                <h5>Integrated Berth Sequencing</h5>
                                <p>Deep API ties to major terminals. Voids the queue entirely by managing speed offshore.</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 10. Forecast Bulletin -->
        <section class="container scroll-reveal" id="bulletins">
            <h2 class="display-text" style="font-size:2.5rem; margin-bottom: 2rem;">Intelligence Briefs</h2>
            <div class="bulletin-grid">
                <div class="glass-panel bulletin-card p-4 stagger-item" style="padding: 2rem;">
                    <span class="tag">WATCH</span>
                    <h4 style="margin-bottom: 1rem;">N. Atlantic Block Pattern</h4>
                    <p style="color:var(--text-muted); font-size:0.9rem;">Persistent high-pressure ridge forming. Expect severe cross-swells forming on southern edge. Recommended lane deflections active.</p>
                </div>
                <div class="glass-panel bulletin-card p-4 stagger-item" style="padding: 2rem;">
                    <span class="tag" style="background:rgba(16,185,129,0.2); color:var(--dl-success);">SECURE</span>
                    <h4 style="margin-bottom: 1rem;">Panama Transit Norm</h4>
                    <p style="color:var(--text-muted); font-size:0.9rem;">Draft limits remain stable. Lake Gatun reserves indicate no immediate impedance for neo-panamax capacity over next 30 days.</p>
                </div>
                <div class="glass-panel bulletin-card p-4 stagger-item" style="padding: 2rem;">
                    <span class="tag" style="background:rgba(217,70,239,0.2); color:var(--dl-magenta);">COMPLIANCE</span>
                    <h4 style="margin-bottom: 1rem;">Q4 CII Thresholds</h4>
                    <p style="color:var(--text-muted); font-size:0.9rem;">Algorithmic pacing enforced across Pacific routes averting C-grade drops for major operators in the previous fiscal quarter.</p>
                </div>
            </div>
        </section>

        <!-- 11. Compliance -->
        <section class="container scroll-reveal">
            <div class="compliance-block">
                <h2>Regulatory Integrity by Design</h2>
                <p style="color:var(--text-muted); font-size:1.1rem; max-width:600px; margin:0 auto 2rem;">
                    Operating internationally means facing stringent reporting standards. Drift Ledger automates emissions tracking, logging fuel burn estimates against route severities. Your ESG reports and underwriter datasets are generated concurrently with the voyage.
                </p>
                <button class="btn btn-glass" onclick="openModal()">Download Compliance Methods</button>
            </div>
        </section>

        <!-- 12. FAQ Accordion -->
        <section id="faq" class="container scroll-reveal">
            <h2 class="display-text" style="font-size:2.5rem; text-align:center; margin-bottom: 3rem;">Operational Parameters (FAQ)</h2>
            <div class="faq-list" id="accordion-group">
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false" aria-controls="faq-1" id="faq-btn-1">
                        <span>How frequently are weather models updated?</span>
                        <svg class="accordion-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </button>
                    <div class="accordion-content" id="faq-1" role="region" aria-labelledby="faq-btn-1">
                        <div class="accordion-inner">
                            We ingest data every hour from ECMWF, GFS, and proprietary satellite constellations, fusing them into a unified risk matrix that updates route parameters dynamically.
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false" aria-controls="faq-2" id="faq-btn-2">
                        <span>Can it integrate with existing vessel ECDIS?</span>
                        <svg class="accordion-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </button>
                    <div class="accordion-content" id="faq-2" role="region" aria-labelledby="faq-btn-2">
                        <div class="accordion-inner">
                            Yes. Route envelopes are exportable via secure satellite connection in standard RTZ formats for direct importation into the vessel's primary navigation systems.
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false" aria-controls="faq-3" id="faq-btn-3">
                        <span>Does the platform manage fleet-wide views?</span>
                        <svg class="accordion-icon" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </button>
                    <div class="accordion-content" id="faq-3" role="region" aria-labelledby="faq-btn-3">
                        <div class="accordion-inner">
                            Absolutely. The Fleet Overview module assesses port congestion globally, aligning arrivals across multiple assets to prevent simultaneous queuing.
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 13. Final CTA -->
        <section class="container scroll-reveal" style="padding-top: 6rem;">
            <div class="cta-container glass-panel conic-border" style="padding: 4rem 2rem;">
                <h2 class="display-text" style="font-size:3rem; margin-bottom:1rem;">Secure Your Routes</h2>
                <p style="color:var(--text-muted); margin-bottom: 2rem;">Schedule a technical resilience review. We analyze your historic lanes and quantify available risk reduction and fuel savings.</p>
                <form class="cta-form" onsubmit="event.preventDefault(); showToast('Review request queued. Our systems team will contact you.');">
                    <input type="email" class="form-input" placeholder="CORPORATE EMAIL ADDRESS" aria-label="Email Address" required>
                    <button type="submit" class="btn btn-primary" style="width:100%; padding: 1rem;">Initiate Review Protocol</button>
                </form>
            </div>
        </section>

    </main>

    <!-- 14. Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <div class="brand" style="margin-bottom: 1.5rem;">
                        <svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2zm0 4.5l6.5 13h-13L12 6.5z"/></svg>
                        DRIFT LEDGER
                    </div>
                    <p style="color:var(--text-muted); font-size:0.9rem; max-width: 300px;">
                        Algorithmic continuity for the world's commercial oceans. We turn uncertainty into calculated operational advantage.
                    </p>
                </div>
                <div class="footer-links">
                    <h4>PLATFORM</h4>
                    <ul>
                        <li><a href="#">Meteo-Engine</a></li>
                        <li><a href="#">Route Generation</a></li>
                        <li><a href="#">Insurer Exports</a></li>
                        <li><a href="#">API Documentation</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>COMPANY</h4>
                    <ul>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Engineering Log</a></li>
                        <li><a href="#">Press Reports</a></li>
                        <li><a href="#">Careers</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>COMPLIANCE</h4>
                    <ul>
                        <li><a href="#">Data Privacy</a></li>
                        <li><a href="#">Terms of Service</a></li>
                        <li><a href="#">Security Audits</a></li>
                        <li><a href="#">System Status</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 Drift Ledger Systems. All rights reserved.</span>
                <span class="font-mono">SYS_STATUS_GREEN</span>
            </div>
        </div>
    </footer>

    <!-- Modal: Resilience Review -->
    <div class="modal-overlay" id="review-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
        <div class="modal-content conic-border">
            <button class="modal-close" aria-label="Close modal" onclick="closeModal()">
                <svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
            </button>
            <h2 id="modal-title" style="font-size:2rem; margin-bottom:0.5rem; color:var(--dl-cyan);">Resilience Config</h2>
            <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom: 2rem;">Input primary lane vectors to observe potential variance.</p>
            
            <form onsubmit="event.preventDefault(); closeModal(); showToast('Calculation parameters locked. Generating brief.');">
                <div class="modal-grid">
                    <input type="text" class="form-input focus-visible-only" id="lane-input" placeholder="LANE/REGION (e.g. Trans-Pacific)" aria-label="Routing Lane" required>
                    <select class="form-input focus-visible-only" id="risk-select" aria-label="Risk Appetite">
                        <option value="watch">Risk Limit: WATCH (Standard)</option>
                        <option value="warning">Risk Limit: WARNING (Aggressive)</option>
                        <option value="avoid">Risk Limit: AVOID STRICT (Conservative)</option>
                    </select>
                </div>
                
                <div class="modal-summary" id="modal-summary">
                    > AWAITING INPUT
                </div>
                
                <div style="margin-top: 2rem; display:flex; justify-content: flex-end;">
                    <button type="submit" class="btn btn-primary focus-visible-only">Run Simulation</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Toast Notification Region -->
    <div class="toast-container" aria-live="polite" aria-atomic="true" id="toast-container"></div>

    <script>
        // --- 1. Navbar Scroll Transition ---
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.add('scrolled'); // keep for strict logic or remove
                if(window.scrollY < 10) navbar.classList.remove('scrolled');
            }
        });

        // --- 2. Modal Logic ---
        const modal = document.getElementById('review-modal');
        let lastFocusedElement;

        function openModal() {
            lastFocusedElement = document.activeElement;
            modal.classList.add('open');
            const firstInput = modal.querySelector('input');
            if (firstInput) firstInput.focus();
        }

        function closeModal() {
            modal.classList.remove('open');
            if (lastFocusedElement) lastFocusedElement.focus();
        }

        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('open')) {
                closeModal();
            }
        });

        // Modal Live Summary Update
        const laneInput = document.getElementById('lane-input');
        const riskSelect = document.getElementById('risk-select');
        const modalSummary = document.getElementById('modal-summary');
        
        function updateSummary() {
            const lane = laneInput.value || 'UNSPECIFIED';
            const risk = riskSelect.value.toUpperCase();
            modalSummary.innerHTML = `> TARGET: ${lane}<br>> RISK DELTA: ${risk}<br>> STATUS: READY TO COMPUTE`;
        }
        laneInput.addEventListener('input', updateSummary);
        riskSelect.addEventListener('change', updateSummary);

        // --- 3. Accordion ---
        const accordions = document.querySelectorAll('.accordion-header');
        accordions.forEach(acc => {
            acc.addEventListener('click', function() {
                const item = this.parentElement;
                const isExpanded = this.getAttribute('aria-expanded') === 'true';
                
                // close others if needed, but here we allow multiple
                const content = item.querySelector('.accordion-content');
                
                if (isExpanded) {
                    this.setAttribute('aria-expanded', 'false');
                    item.classList.remove('open');
                    content.style.maxHeight = null;
                } else {
                    this.setAttribute('aria-expanded', 'true');
                    item.classList.add('open');
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            });
        });

        // --- 4. Toast ---
        const toastContainer = document.getElementById('toast-container');
        function showToast(message) {
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.innerHTML = `
                <span>${message}</span>
                <button class="toast-close" aria-label="Close message" onclick="this.parentElement.remove()">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
                </button>
            `;
            toastContainer.appendChild(toast);
            
            // Trigger animation
            requestAnimationFrame(() => toast.classList.add('show'));
            
            setTimeout(() => {
                toast.classList.remove('show');
                toast.addEventListener('transitionend', () => toast.remove());
            }, 5000);
        }

        // --- 5. Tabs ---
        const tabs = document.querySelectorAll('[role="tab"]');
        const tabList = document.querySelector('[role="tablist"]');
        
        let tabFocus = 0;

        tabList.addEventListener('keydown', e => {
            if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
                tabs[tabFocus].setAttribute('tabindex', -1);
                if (e.key === 'ArrowRight') {
                    tabFocus++;
                    if (tabFocus >= tabs.length) tabFocus = 0;
                } else if (e.key === 'ArrowLeft') {
                    tabFocus--;
                    if (tabFocus < 0) tabFocus = tabs.length - 1;
                }
                tabs[tabFocus].setAttribute('tabindex', 0);
                tabs[tabFocus].focus();
            }
        });

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const target = tab.getAttribute('aria-controls');
                
                // Reset all
                document.querySelectorAll('[role="tabpanel"]').forEach(p => {
                    p.classList.remove('active');
                    p.hidden = true;
                });
                tabs.forEach(t => t.setAttribute('aria-selected', false));
                
                // Activate target
                tab.setAttribute('aria-selected', true);
                const panel = document.getElementById(target);
                panel.hidden = false;
                // tiny delay for fade in
                setTimeout(() => panel.classList.add('active'), 10);
            });
        });

        // --- 6. Scroll Reveal & Stagger Animation ---
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.15
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = 1;
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                    
                    // stagger children if exists
                    const staggers = entry.target.querySelectorAll('.stagger-item');
                    staggers.forEach((el, index) => {
                        setTimeout(() => {
                            el.classList.add('visible');
                        }, index * 100);
                    });
                    
                    // IF it is the dossier items
                    if(entry.target.classList.contains('timeline-item')) {
                        entry.target.classList.add('active');
                    }
                }
            });
        }, observerOptions);

        document.querySelectorAll('.scroll-reveal').forEach(el => {
            el.style.opacity = 0;
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.8s var(--fluid)';
            revealObserver.observe(el);
        });
        
        // Also observe individual timeline items
        document.querySelectorAll('.timeline-item').forEach(el => {
            revealObserver.observe(el);
        });

        // --- 7. Count-up Animation ---
        const countUpObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = parseFloat(el.getAttribute('data-target'));
                    const duration = 2000;
                    const startTime = performance.now();
                    
                    const updateCount = (currentTime) => {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        // ease out expo
                        const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
                        const currentVal = (target * easeProgress).toFixed(0);
                        el.innerText = currentVal;
                        if (progress < 1) requestAnimationFrame(updateCount);
                    };
                    requestAnimationFrame(updateCount);
                    observer.unobserve(el);
                }
            });
        });

        document.querySelectorAll('.count-up').forEach(c => countUpObserver.observe(c));

        // --- 8. Additional: Route Replay Scrubber ---
        const scrubber = document.getElementById('scrubber');
        const replayValue = document.getElementById('replay-value');
        const replayPath = document.getElementById('replay-path');
        const replayShip = document.getElementById('replay-ship');

        if(scrubber) {
            scrubber.addEventListener('input', (e) => {
                const val = e.target.value;
                replayValue.innerText = val + '%';
                
                // Update dash offset
                const dashLen = 1000;
                const offset = dashLen - (dashLen * (val / 100));
                replayPath.style.strokeDashoffset = offset;
                
                // Move ship (approximation using bounding box and percent if SVG path getTotalLength is available)
                try {
                    const pathLength = replayPath.getTotalLength();
                    const point = replayPath.getPointAtLength(pathLength * (val/100));
                    replayShip.setAttribute('cx', point.x);
                    replayShip.setAttribute('cy', point.y);
                } catch(err) {} 
            });
        }

        // --- Dossier scrollytelling interaction ---
        const dossierSteps = document.querySelectorAll('.dossier-step');
        const dossierOverlays = document.querySelectorAll('.dossier-overlay');
        
        const dossierObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting && entry.intersectionRatio > 0.5) {
                    // deactivate all
                    dossierSteps.forEach(s => s.classList.remove('active'));
                    dossierOverlays.forEach(o => o.classList.remove('active'));
                    
                    // activate current
                    entry.target.classList.add('active');
                    const stepNum = entry.target.getAttribute('data-step');
                    const targetOverlay = document.getElementById('ov-' + stepNum);
                    if(targetOverlay) targetOverlay.classList.add('active');
                }
            });
        }, { threshold: 0.6 });

        dossierSteps.forEach(step => dossierObserver.observe(step));

    </script>
</body>
</html>"""

with open("c:\\Users\\saying\\Desktop\\html_agent\\fdu_007\\src\\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {len(html_content.splitlines())} lines.")
