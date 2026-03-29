import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canopy Ledger | The Sourcing Intelligence OS</title>
    <style>
        :root {
            --bg-base: #030508;
            --bg-soft: rgba(10, 15, 25, 0.6);
            --bg-glass: rgba(255, 255, 255, 0.03);
            --bg-glass-hover: rgba(255, 255, 255, 0.07);
            --bg-panel: rgba(15, 20, 35, 0.5);
            --bg-inset: rgba(0, 0, 0, 0.3);
            
            --border-glass: rgba(255, 255, 255, 0.08);
            --border-glow: rgba(0, 240, 255, 0.3);
            
            --text-main: #f0f4f8;
            --text-muted: #8a9bb3;
            --text-label: #546885;
            --text-inverse: #030508;
            
            --accent-cyan: #00f0ff;
            --accent-emerald: #00ff88;
            --accent-magenta: #ff00ea;
            --accent-indigo: #4d00ff;
            
            --status-success: #00ffaa;
            --status-warn: #ffaa00;
            --status-alert: #ff0055;
            
            --radius-sm: 8px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-pill: 999px;
            
            --space-xs: 4px;
            --space-sm: 12px;
            --space-md: 24px;
            --space-lg: 48px;
            --space-xl: 96px;
            --space-xxl: 160px;
            
            --font-display: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            --font-body: "Inter", "SF Pro Display", sans-serif;
            --font-mono: "JetBrains Mono", "SF Mono", monospace;
            
            --nav-height: 80px;
            --content-width: 1280px;
            
            --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
            --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
            --duration-fast: 0.2s;
            --duration-med: 0.5s;
            --duration-slow: 1s;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-body);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* Ambient Blurred Orbs */
        .ambient-orbs {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: -1;
            overflow: hidden;
            background: var(--bg-base);
        }
        .orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(120px);
            opacity: 0.4;
            animation: float 20s infinite alternate var(--ease-in-out);
        }
        .orb-1 { width: 600px; height: 600px; background: var(--accent-indigo); top: -100px; left: -100px; animation-delay: 0s; }
        .orb-2 { width: 500px; height: 500px; background: var(--accent-cyan); bottom: -100px; right: -50px; animation-delay: -5s; }
        .orb-3 { width: 400px; height: 400px; background: var(--accent-emerald); top: 40%; left: 50%; animation-delay: -10s; }
        .orb-4 { width: 800px; height: 300px; background: var(--accent-magenta); bottom: 10%; left: -200px; animation-delay: -15s; }
        
        @keyframes float {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(50px, 50px) scale(1.1); }
        }

        .container {
            max-width: var(--content-width);
            margin: 0 auto;
            padding: 0 var(--space-md);
        }

        /* Typography */
        h1, h2, h3, h4, .display-text { font-family: var(--font-display); font-weight: 600; letter-spacing: -0.02em; line-height: 1.1; }
        h1 { font-size: clamp(3rem, 6vw, 5.5rem); margin-bottom: var(--space-md); }
        h2 { font-size: clamp(2rem, 4vw, 3.5rem); margin-bottom: var(--space-md); }
        h3 { font-size: clamp(1.5rem, 2.5vw, 2rem); margin-bottom: var(--space-sm); }
        .subtitle { font-size: clamp(1.1rem, 2vw, 1.5rem); color: var(--text-muted); font-weight: 400; margin-bottom: var(--space-lg); }
        .mono { font-family: var(--font-mono); font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; }

        /* Generic Glass Panel */
        .glass-panel {
            background: var(--bg-panel);
            -webkit-backdrop-filter: blur(24px);
            backdrop-filter: blur(24px);
            border: 1px solid var(--border-glass);
            border-radius: var(--radius-lg);
            box-shadow: 0 24px 48px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
            position: relative;
            overflow: hidden;
        }

        /* Section 1: Sticky Glass Navbar */
        .navbar {
            position: fixed;
            top: 0; left: 0; width: 100%;
            height: var(--nav-height);
            z-index: 1000;
            display: flex;
            align-items: center;
            transition: all var(--duration-med) var(--ease-out);
            border-bottom: 1px solid transparent;
        }
        .navbar.scrolled {
            background: rgba(3, 5, 8, 0.7);
            -webkit-backdrop-filter: blur(20px);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-glass);
            height: 70px;
        }
        .nav-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }
        .brand {
            font-size: 1.5rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .brand-icon {
            width: 24px; height: 24px;
            background: conic-gradient(from 180deg, var(--accent-cyan), var(--accent-indigo), var(--accent-magenta), var(--accent-cyan));
            border-radius: 50%;
            animation: spin 4s linear infinite;
        }
        @keyframes spin { 100% { transform: rotate(360deg); } }
        
        .nav-links { display: flex; gap: var(--space-md); }
        .nav-links a {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            transition: color var(--duration-fast);
        }
        .nav-links a:hover { color: var(--text-main); }
        
        .status-pill {
            display: flex; align-items: center; gap: 8px;
            padding: 6px 12px;
            background: rgba(0, 255, 170, 0.1);
            border: 1px solid rgba(0, 255, 170, 0.2);
            border-radius: var(--radius-pill);
            font-size: 0.8rem;
            color: var(--status-success);
        }
        .status-dot {
            width: 8px; height: 8px;
            background: var(--status-success);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--status-success);
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
            100% { opacity: 1; transform: scale(1); }
        }
        
        .btn {
            padding: 12px 24px;
            border-radius: var(--radius-pill);
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            transition: all var(--duration-fast) var(--ease-out);
            border: none;
            outline: none;
        }
        .btn-primary {
            background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.2), 0 0 20px rgba(0, 240, 255, 0.2);
            border: 1px solid rgba(255,255,255,0.1);
            color: var(--text-main);
            -webkit-backdrop-filter: blur(10px);
            backdrop-filter: blur(10px);
        }
        .btn-primary:hover {
            background: rgba(255,255,255,0.1);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.3), 0 0 30px rgba(0, 240, 255, 0.4);
            transform: translateY(-2px);
        }
        .btn-outline {
            background: transparent;
            border: 1px solid var(--border-glass);
            color: var(--text-main);
        }
        .btn-outline:hover {
            background: var(--bg-glass-hover);
        }
        
        section { padding: var(--space-xxl) 0; position: relative; }

        /* Section 2: Hero */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding-top: var(--nav-height);
        }
        .hero-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-xl);
            align-items: center;
        }
        .hero-content {
            position: relative;
            z-index: 10;
        }
        .hero-actions { display: flex; gap: var(--space-md); margin-top: var(--space-lg); }
        
        .hero-visual {
            position: relative;
            perspective: 1000px;
        }
        .dashboard-widget {
            background: var(--bg-panel);
            -webkit-backdrop-filter: blur(24px);
            backdrop-filter: blur(24px);
            border: 1px solid var(--border-glass);
            border-radius: var(--radius-lg);
            padding: var(--space-md);
            transform: rotateY(-15deg) rotateX(5deg);
            box-shadow: -20px 20px 60px rgba(0,0,0,0.5), 0 0 40px rgba(0, 240, 255, 0.1);
            animation: hover-dashboard 6s ease-in-out infinite alternate;
        }
        @keyframes hover-dashboard {
            0% { transform: rotateY(-15deg) rotateX(5deg) translateY(0); }
            100% { transform: rotateY(-10deg) rotateX(2deg) translateY(-20px); }
        }
        .dash-header { display: flex; justify-content: space-between; margin-bottom: var(--space-md); border-bottom: 1px solid var(--border-glass); padding-bottom: var(--space-sm); }
        .dash-row { display: flex; justify-content: space-between; margin-bottom: var(--space-sm); font-family: var(--font-mono); font-size: 0.85rem; }
        .dash-bar-bg { width: 100%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px; margin-top: 5px; overflow: hidden; }
        .dash-bar-fill { height: 100%; width: 75%; background: var(--accent-cyan); box-shadow: 0 0 10px var(--accent-cyan); }
        .dash-row:nth-child(3) .dash-bar-fill { width: 92%; background: var(--accent-emerald); box-shadow: 0 0 10px var(--accent-emerald); }
        .dash-row:nth-child(4) .dash-bar-fill { width: 45%; background: var(--accent-magenta); box-shadow: 0 0 10px var(--accent-magenta); }

        /* Section 3: Trust Strip */
        .trust-strip {
            padding: var(--space-lg) 0;
            border-top: 1px solid var(--border-glass);
            border-bottom: 1px solid var(--border-glass);
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.02), transparent);
            overflow: hidden;
            white-space: nowrap;
            display: flex;
            align-items: center;
        }
        .trust-label { font-size: 0.85rem; color: var(--text-label); margin-right: var(--space-xl); font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; padding-left: 5vw; }
        .marquee {
            display: inline-flex;
            gap: var(--space-xl);
            animation: scroll-left 30s linear infinite;
        }
        @keyframes scroll-left { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
        .trust-logo { font-size: 1.2rem; font-weight: 700; color: var(--text-muted); opacity: 0.6; transition: opacity var(--duration-fast); }
        .trust-logo:hover { opacity: 1; color: var(--text-main); }

        /* Section 4: Capability Grid (Reveal & Stagger) */
        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: var(--space-md);
        }
        .feature-card {
            padding: var(--space-lg);
            display: flex;
            flex-direction: column;
            gap: var(--space-sm);
            transition: transform var(--duration-med);
        }
        /* Glow-tracking variables set by JS */
        .feature-card::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(800px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(255,255,255,0.06), transparent 40%);
            z-index: 1; pointer-events: none;
            border-radius: inherit;
        }
        .feature-card::after {
            content: ''; position: absolute; inset: -1px;
            background: conic-gradient(from var(--border-angle, 0deg) at 50% 50%, transparent, var(--border-glow), transparent 30%);
            z-index: -1; border-radius: var(--radius-lg); opacity: 0; transition: opacity var(--duration-med);
        }
        .feature-card:hover { transform: translateY(-5px); }
        .feature-card:hover::after { opacity: 1; animation: rotate-border 4s linear infinite; }
        @keyframes rotate-border { 100% { --border-angle: 360deg; } }
        /* A little houdini trick for conic gradients if supported, else fallback to static or partial */
        @property --border-angle { syntax: "<angle>"; inherits: true; initial-value: 0turn; }
        .feature-icon {
            width: 48px; height: 48px;
            border-radius: 12px;
            background: rgba(255,255,255,0.05);
            display: flex; align-items: center; justify-content: center;
            margin-bottom: var(--space-sm);
            border: 1px solid var(--border-glass);
            color: var(--accent-cyan);
        }
        
        .reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s var(--ease-out); }
        .reveal.active { opacity: 1; transform: translateY(0); }

        /* Section 5: Platform View (Tabs) */
        .platform-section { text-align: center; }
        .platform-tabs {
            display: inline-flex;
            background: var(--bg-inset);
            padding: 4px;
            border-radius: var(--radius-pill);
            margin: var(--space-lg) auto;
            border: 1px solid var(--border-glass);
        }
        .tab-btn {
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 10px 24px;
            border-radius: var(--radius-pill);
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: all var(--duration-fast);
        }
        .tab-btn.active {
            background: rgba(255,255,255,0.1);
            color: var(--text-main);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        .platform-window {
            height: 500px;
            display: flex;
            text-align: left;
        }
        .tab-content { display: none; padding: var(--space-lg); width: 100%; width: 100%; height: 100%; animation: fade-in var(--duration-med); }
        .tab-content.active { display: flex; flex-direction: column; }
        @keyframes fade-in { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        .data-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-md); margin-top: var(--space-md); }
        .data-cell { background: rgba(0,0,0,0.2); padding: var(--space-sm); border-radius: var(--radius-sm); border: 1px solid var(--border-glass); }
        .data-value { font-size: 1.5rem; font-weight: 600; margin-top: 8px; color: var(--accent-cyan); font-family: var(--font-mono); }

        /* Section 6: Metrics Band */
        .metrics-band { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-md); text-align: center; }
        .metric-card { padding: var(--space-xl) var(--space-md); }
        .metric-num { font-size: clamp(3rem, 5vw, 4.5rem); font-weight: 700; color: var(--text-main); line-height: 1; margin-bottom: 8px; }
        .metric-label { color: var(--accent-emerald); font-family: var(--font-mono); text-transform: uppercase; letter-spacing: 0.05em; }

        /* Section 7: Journey Timeline */
        .timeline-container { position: relative; margin: var(--space-xl) auto; max-width: 800px; }
        .timeline-line { position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, transparent, var(--accent-indigo), var(--accent-cyan), transparent); transform: translateX(-50%); }
        .timeline-node { position: relative; width: 100%; display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-xl); cursor: pointer; }
        .timeline-node:nth-child(even) { flex-direction: row-reverse; }
        .timeline-dot { width: 20px; height: 20px; border-radius: 50%; background: var(--bg-base); border: 2px solid var(--accent-cyan); position: absolute; left: 50%; transform: translateX(-50%); box-shadow: 0 0 15px var(--accent-cyan); transition: all var(--duration-fast); }
        .timeline-node:hover .timeline-dot { transform: translateX(-50%) scale(1.5); background: var(--accent-cyan); }
        .timeline-content { width: 45%; padding: var(--space-md); transition: opacity var(--duration-med); }
        .node-title { font-size: 1.25rem; font-weight: 600; margin-bottom: 8px; }
        .node-desc { color: var(--text-muted); font-size: 0.95rem; }

        /* Section 8: Comparison Tool */
        .compare-section { display: flex; flex-direction: column; align-items: center; }
        .compare-toggle { display: flex; background: var(--bg-inset); border-radius: var(--radius-pill); padding: 4px; border: 1px solid var(--border-glass); margin-bottom: var(--space-lg); }
        .compare-btn { padding: 12px 32px; border-radius: var(--radius-pill); border: none; background: transparent; color: var(--text-muted); font-weight: 600; cursor: pointer; transition: all var(--duration-fast); }
        .compare-btn.active { background: var(--bg-glass); border: 1px solid var(--border-glass); color: var(--text-main); }
        .compare-view { width: 100%; height: 400px; position: relative; border-radius: var(--radius-lg); overflow: hidden; }
        
        .compare-pane { position: absolute; top: 0; left: 0; width: 100%; height: 100%; padding: var(--space-xl); transition: opacity var(--duration-med); display: flex; flex-direction: column; justify-content: center;}
        .pane-legacy { background: repeating-linear-gradient(45deg, #110505, #110505 10px, #1a0808 10px, #1a0808 20px); border: 1px solid #331111; opacity: 1; z-index: 2;}
        .pane-legacy .alert-text { color: var(--status-alert); font-family: var(--font-mono); font-size: 1.2rem; }
        .pane-canopy { background: var(--bg-panel); -webkit-backdrop-filter: blur(20px); backdrop-filter: blur(20px); border: 1px solid var(--accent-cyan); box-shadow: inset 0 0 50px rgba(0, 240, 255, 0.1); opacity: 0; z-index: 1;}
        .pane-canopy .success-text { color: var(--accent-cyan); font-family: var(--font-mono); font-size: 1.2rem; text-shadow: 0 0 10px rgba(0,240,255,0.5); }

        /* Section 9: Spotlight Feed */
        .spotlight-feed { display: flex; gap: var(--space-md); overflow-x: hidden; padding: var(--space-md) 0; }
        .feed-track { display: flex; gap: var(--space-md); animation: scroll-feed 20s linear infinite; }
        @keyframes scroll-feed { from { transform: translateX(0); } to { transform: translateX(-50%); } }
        .feed-card { min-width: 350px; padding: var(--space-md); border-left: 3px solid var(--accent-magenta); }
        .feed-tag { display: inline-block; padding: 2px 8px; border-radius: 4px; background: rgba(255,0,234,0.1); color: var(--accent-magenta); font-size: 0.75rem; margin-bottom: 12px; }

        /* Section 10 & 11: Governance & FAQ Accordion */
        .accordion { display: flex; flex-direction: column; gap: var(--space-sm); max-width: 800px; margin: 0 auto; }
        .accordion-item { border: 1px solid var(--border-glass); border-radius: var(--radius-md); background: rgba(255,255,255,0.01); overflow: hidden; transition: background var(--duration-fast); }
        .accordion-header { padding: var(--space-md); width: 100%; text-align: left; background: transparent; border: none; color: var(--text-main); font-weight: 600; font-size: 1.1rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
        .accordion-header:hover { background: rgba(255,255,255,0.03); }
        .accordion-icon { width: 24px; height: 24px; position: relative; }
        .accordion-icon::before, .accordion-icon::after { content: ''; position: absolute; background: var(--text-muted); top: 50%; left: 50%; transform: translate(-50%, -50%); transition: transform var(--duration-fast); }
        .accordion-icon::before { width: 12px; height: 2px; }
        .accordion-icon::after { width: 2px; height: 12px; }
        .accordion-item.open .accordion-icon::after { transform: translate(-50%, -50%) rotate(90deg); opacity: 0; }
        .accordion-content { padding: 0 var(--space-md); max-height: 0; opacity: 0; transition: all var(--duration-med) var(--ease-out); overflow: hidden; color: var(--text-muted); }
        .accordion-item.open .accordion-content { padding: 0 var(--space-md) var(--space-md); max-height: 500px; opacity: 1; }

        /* Section 12: Final Gateway Form */
        .gateway-portal { text-align: center; max-width: 600px; margin: 0 auto; padding: var(--space-xl); border: 1px solid rgba(0, 240, 255, 0.3); background: radial-gradient(circle at center, rgba(0,240,255,0.05), transparent 70%); border-radius: var(--radius-lg); box-shadow: 0 0 100px rgba(0, 240, 255, 0.1); }
        .form-group { margin-bottom: var(--space-md); text-align: left; }
        .form-label { display: block; font-size: 0.85rem; color: var(--text-label); margin-bottom: 8px; font-family: var(--font-mono); }
        .form-input { width: 100%; padding: 16px; border-radius: var(--radius-sm); background: rgba(0,0,0,0.5); border: 1px solid var(--border-glass); color: var(--text-main); font-family: var(--font-body); font-size: 1rem; transition: border var(--duration-fast); }
        .form-input:focus { outline: none; border-color: var(--accent-cyan); box-shadow: 0 0 0 3px rgba(0,240,255,0.1); }
        .submit-btn { width: 100%; padding: 16px; font-size: 1.1rem; margin-top: var(--space-sm); }

        /* Section 13: Footer */
        .footer { padding: var(--space-xl) 0 var(--space-md); border-top: 1px solid var(--border-glass); margin-top: var(--space-xxl); }
        .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: var(--space-xl); margin-bottom: var(--space-xl); }
        .footer-title { color: var(--text-main); font-weight: 600; margin-bottom: var(--space-md); }
        .footer-links { list-style: none; }
        .footer-links li { margin-bottom: 12px; }
        .footer-links a { color: var(--text-muted); text-decoration: none; transition: color var(--duration-fast); }
        .footer-links a:hover { color: var(--accent-cyan); }
        .footer-bottom { display: flex; justify-content: space-between; align-items: center; padding-top: var(--space-md); border-top: 1px solid var(--border-glass); color: var(--text-muted); font-size: 0.85rem; }

        /* Modal */
        .modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px); z-index: 2000; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity var(--duration-fast); }
        .modal-overlay.active { opacity: 1; pointer-events: all; }
        .modal-content { background: var(--bg-base); border: 1px solid var(--border-glass); border-radius: var(--radius-lg); padding: var(--space-xl); max-width: 500px; width: 90%; transform: translateY(20px) scale(0.95); transition: all var(--duration-med) var(--ease-out); position: relative; }
        .modal-overlay.active .modal-content { transform: translateY(0) scale(1); }
        .modal-close { position: absolute; top: 20px; right: 20px; background: transparent; border: none; color: var(--text-muted); cursor: pointer; font-size: 1.5rem; }

        /* Toast */
        .toast-container { position: fixed; bottom: 24px; right: 24px; z-index: 3000; display: flex; flex-direction: column; gap: 12px; }
        .toast { background: var(--bg-panel); -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px); border-left: 4px solid var(--accent-emerald); border-radius: var(--radius-sm); padding: 16px 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); color: var(--text-main); display: flex; align-items: center; gap: 12px; transform: translateX(120%); transition: transform var(--duration-med) var(--ease-out); }
        .toast.show { transform: translateX(0); }

        /* Responsive */
        @media (max-width: 1024px) {
            .hero-grid { grid-template-columns: 1fr; text-align: center; }
            .hero-actions { justify-content: center; }
            .grid-3 { grid-template-columns: repeat(2, 1fr); }
            .metrics-band { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr 1fr; gap: var(--space-lg); }
        }
        @media (max-width: 768px) {
            h1 { font-size: 2.5rem; }
            .nav-links { display: none; }
            .grid-3 { grid-template-columns: 1fr; }
            .data-grid { grid-template-columns: 1fr 1fr; }
            .footer-grid { grid-template-columns: 1fr; }
            .trust-label { display: none; }
            .timeline-node { flex-direction: column !important; text-align: center; }
            .timeline-line { left: 20px; }
            .timeline-dot { left: 20px; }
            .timeline-content { width: 100%; padding-left: 50px; }
            .compare-view { height: 500px; }
        }
        @media (prefers-reduced-motion: reduce) {
            * { animation-play-state: paused !important; transition: none !important; }
        }
    </style>
</head>
<body>

    <!-- Ambient Orbs -->
    <div class="ambient-orbs" aria-hidden="true">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
        <div class="orb orb-4"></div>
    </div>

    <!-- 1. Sticky Navbar -->
    <header class="navbar" id="navbar">
        <div class="container nav-inner">
            <div class="brand">
                <div class="brand-icon"></div>
                Canopy Ledger
            </div>
            <nav class="nav-links" aria-label="Main Navigation">
                <a href="#platform">Platform</a>
                <a href="#solutions">Solutions</a>
                <a href="#compliance">Compliance</a>
                <div class="status-pill">
                    <span class="status-dot"></span>
                    100% Verified
                </div>
            </nav>
            <button class="btn btn-primary demo-trigger" aria-haspopup="dialog">Request Demo</button>
        </div>
    </header>

    <main>
        <!-- 2. Hero Component -->
        <section class="hero container">
            <div class="hero-grid">
                <div class="hero-content reveal">
                    <div class="mono" style="color: var(--accent-cyan); margin-bottom: 16px;">The OS for Luxury Operations</div>
                    <h1>The Infinite Ledger of Luxury Sourcing.</h1>
                    <p class="subtitle">Trace, verify, and scale sustainable supply chains with crystalline clarity. Cryptographically secured material passports from farm to flagship.</p>
                    <div class="hero-actions">
                        <button class="btn btn-primary demo-trigger">Initialize Audit</button>
                        <button class="btn btn-outline">Explore Architecture</button>
                    </div>
                </div>
                <div class="hero-visual reveal" style="transition-delay: 0.2s;">
                    <div class="dashboard-widget">
                        <div class="dash-header">
                            <span class="mono">Live Network Flow</span>
                            <span style="color: var(--status-success)">● Syncing</span>
                        </div>
                        <div class="dash-row"><span>Lot #4409 Validation</span><span>99.9%</span></div>
                        <div class="dash-bar-bg"><div class="dash-bar-fill"></div></div>
                        <div style="height: 20px;"></div>
                        <div class="dash-row"><span>Mill Tier 2 Trace</span><span>Verified</span></div>
                        <div class="dash-bar-bg"><div class="dash-bar-fill"></div></div>
                        <div style="height: 20px;"></div>
                        <div class="dash-row"><span>Scope 3 Emissions</span><span>Calculating</span></div>
                        <div class="dash-bar-bg"><div class="dash-bar-fill"></div></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. Trust Strip -->
        <div class="trust-strip">
            <div class="trust-label">Securing the supply chains of</div>
            <div class="marquee">
                <span class="trust-logo">LVMH</span>
                <span class="trust-logo">KERING</span>
                <span class="trust-logo">PRADA GROUP</span>
                <span class="trust-logo">ZEGNA</span>
                <span class="trust-logo">BRUNELLO CUCINELLI</span>
                <span class="trust-logo">BURBERRY</span>
                <span class="trust-logo">LVMH</span>
                <span class="trust-logo">KERING</span>
                <span class="trust-logo">PRADA GROUP</span>
                <span class="trust-logo">ZEGNA</span>
            </div>
        </div>

        <!-- 4. Capability Grid -->
        <section id="solutions" class="container">
            <h2 class="reveal" style="text-align: center; margin-bottom: var(--space-xl);">Orchestrate Complexity.</h2>
            <div class="grid-3">
                <div class="glass-panel feature-card reveal stagger">
                    <div class="feature-icon">M</div>
                    <h3>Immutable Material Passports</h3>
                    <p class="text-muted">Generate cryptographic tokens for every yard of fabric. Bind fiber origin, dye chemistry, and mill certifications into a single unbroken record.</p>
                </div>
                <div class="glass-panel feature-card reveal stagger" style="transition-delay: 0.1s;">
                    <div class="feature-icon">G</div>
                    <h3>Geo-Tagged Fiber Origins</h3>
                    <p class="text-muted">Ingest satellite and agricultural data to verify raw material origins at the GPS coordinate level. Defend against commingling risks.</p>
                </div>
                <div class="glass-panel feature-card reveal stagger" style="transition-delay: 0.2s;">
                    <div class="feature-icon">A</div>
                    <h3>Automated Tier 3 Audits</h3>
                    <p class="text-muted">Push compliance questionnaires down the chain automatically. Flag anomalous labor records or missing documentation before issuance.</p>
                </div>
                <div class="glass-panel feature-card reveal stagger">
                    <div class="feature-icon">E</div>
                    <h3>Scope 3 Emissions Engine</h3>
                    <p class="text-muted">Calculate exact carbon impact per SKU by aggregating primary energy data from spinners, weavers, and dyers rather than industry averages.</p>
                </div>
                <div class="glass-panel feature-card reveal stagger" style="transition-delay: 0.1s;">
                    <div class="feature-icon">C</div>
                    <h3>Digital Product Twinning</h3>
                    <p class="text-muted">Pass compliance data gracefully to the consumer layer. Enable compliant DPPs (Digital Product Passports) readable via NFC woven into the garment.</p>
                </div>
                <div class="glass-panel feature-card reveal stagger" style="transition-delay: 0.2s;">
                    <div class="feature-icon">Z</div>
                    <h3>Zero-Knowledge Proofs</h3>
                    <p class="text-muted">Allow mills to prove compliance with brand standards without revealing sensitive supplier relationships to competitors.</p>
                </div>
            </div>
        </section>

        <!-- 5. Platform View (Tabs) -->
        <section id="platform" class="container platform-section reveal">
            <h2>The Nerve Center.</h2>
            <p class="subtitle" style="text-align: center; max-width: 700px; margin: 0 auto;">One pane of glass over the most opaque global networks.</p>
            
            <div class="platform-tabs" role="tablist">
                <button class="tab-btn active" role="tab" aria-selected="true" data-target="tab-fibers">Fibers</button>
                <button class="tab-btn" role="tab" aria-selected="false" data-target="tab-mills">Mills & Nodes</button>
                <button class="tab-btn" role="tab" aria-selected="false" data-target="tab-claims">Claims</button>
                <button class="tab-btn" role="tab" aria-selected="false" data-target="tab-emissions">Emissions</button>
            </div>

            <div class="glass-panel platform-window">
                <div id="tab-fibers" class="tab-content active" role="tabpanel">
                    <div class="mono" style="color: var(--text-label); border-bottom: 1px solid var(--border-glass); padding-bottom: 8px; margin-bottom: 16px;">Global Fiber Ingestion Streams</div>
                    <div class="data-grid">
                        <div class="data-cell">
                            <div style="font-size: 0.8rem; color: var(--text-muted)">Organic Cotton Yield</div>
                            <div class="data-value">4,028 MT</div>
                        </div>
                        <div class="data-cell">
                            <div style="font-size: 0.8rem; color: var(--text-muted)">GOTS Certificates</div>
                            <div class="data-value" style="color: var(--status-success)">142 Valid</div>
                        </div>
                        <div class="data-cell">
                            <div style="font-size: 0.8rem; color: var(--text-muted)">Merino Trace</div>
                            <div class="data-value">88.4%</div>
                        </div>
                        <div class="data-cell">
                            <div style="font-size: 0.8rem; color: var(--text-muted)">Risk Alerts</div>
                            <div class="data-value" style="color: var(--status-alert)">2 Flagged</div>
                        </div>
                    </div>
                </div>
                <div id="tab-mills" class="tab-content" role="tabpanel">
                    <div class="mono" style="color: var(--text-label); border-bottom: 1px solid var(--border-glass); padding-bottom: 8px; margin-bottom: 16px;">Supplier Node Topology</div>
                    <p style="color: var(--text-muted); margin-top: 16px;">Displaying 412 active supplier nodes across Tier 1, 2, and 3. Network graph processing optimized routing for Fall/Winter 26.</p>
                </div>
                <div id="tab-claims" class="tab-content" role="tabpanel">
                    <div class="mono" style="color: var(--text-label); border-bottom: 1px solid var(--border-glass); padding-bottom: 8px; margin-bottom: 16px;">Marketing Claims Verification</div>
                    <p style="color: var(--status-warn); margin-top: 16px;">Warning: "100% Recycled" claim on SKU 8810 lacks required transaction certificates from Weaver node.</p>
                </div>
                <div id="tab-emissions" class="tab-content" role="tabpanel">
                    <div class="mono" style="color: var(--text-label); border-bottom: 1px solid var(--border-glass); padding-bottom: 8px; margin-bottom: 16px;">Scope 3 Carbon Accounting</div>
                    <div class="data-value" style="font-size: 3rem; margin-top: 24px;">12.4kg <span style="font-size: 1rem; color: var(--text-muted)">CO2e / Garment</span></div>
                </div>
            </div>
        </section>

        <!-- 6. Metrics Band (Count-Up) -->
        <section class="container reveal">
            <div class="glass-panel metrics-band">
                <div class="metric-card">
                    <div class="metric-num" data-count="2400000">0</div>
                    <div class="metric-label">Tons Traced Globally</div>
                </div>
                <div class="metric-card">
                    <div class="metric-num">$<span data-count="1.2">0</span>B</div>
                    <div class="metric-label">Compliance Risk Mitigated</div>
                </div>
                <div class="metric-card">
                    <div class="metric-num" data-count="0">100</div>
                    <div class="metric-label">Greenwashing Incidents</div>
                </div>
            </div>
        </section>

        <!-- 7. Journey Timeline -->
        <section class="container reveal">
            <h2 style="text-align: center;">The Anatomy of a Thread.</h2>
            <div class="timeline-container">
                <div class="timeline-line"></div>
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="node-title">1. Raw Material Primary Source</div>
                        <div class="node-desc">GPS boundary tracing of organic cotton farms in Izmir, linking yield data to exact land parcels.</div>
                    </div>
                </div>
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="node-title">2. Aggregation & Ginning</div>
                        <div class="node-desc">Volume balancing equations mathematically prove that output volumes match certified input mass.</div>
                    </div>
                </div>
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="node-title">3. Spinning & Dyeing</div>
                        <div class="node-desc">Integration of OEKO-TEX chemical compliance protocols. Zero discharge of hazardous chemicals verified.</div>
                    </div>
                </div>
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="node-title">4. Cut & Sew Assembly</div>
                        <div class="node-desc">Labor conditions and social audit reports mapped over final assembly plants via API integration.</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 8. Comparison Tool -->
        <section class="container reveal">
            <div class="compare-section">
                <h2 style="text-align: center; margin-bottom: 24px;">Upgrade Your Primitives.</h2>
                <div class="compare-toggle">
                    <button class="compare-btn active" id="btn-legacy">Legacy Spreadsheets</button>
                    <button class="compare-btn" id="btn-canopy">Canopy OS</button>
                </div>
                <div class="compare-view">
                    <div class="compare-pane pane-legacy" id="pane-legacy">
                        <h3 class="alert-text">ERROR: DATA SILO DETECTED</h3>
                        <p style="font-family: monospace; opacity: 0.6;">Row 842: Supplier_Name_V3_FINAL.xlsx</p>
                        <p style="font-family: monospace; opacity: 0.6;">MISSING: Transaction Certificate</p>
                        <p style="font-family: monospace; opacity: 0.6;">STATUS: Unverified Origin Risk</p>
                        <p style="font-family: monospace; opacity: 0.6;">ACTION: Manual Email Follow-up Required</p>
                    </div>
                    <div class="compare-pane pane-canopy" id="pane-canopy">
                        <h3 class="success-text">NODE SYNCHRONIZED</h3>
                        <div class="data-grid" style="grid-template-columns: 1fr 1fr;">
                            <div class="data-cell">Chain Validated</div>
                            <div class="data-cell">Cert Auth Active</div>
                            <div class="data-cell">Trace Immutable</div>
                            <div class="data-cell">Ready for DPP</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 9. Spotlight Feed -->
        <section class="reveal" style="padding-top: var(--space-xl);">
            <div class="container">
                <h3 class="mono" style="color: var(--text-muted); margin-bottom: var(--space-md);">Live Minted Passports</h3>
            </div>
            <div class="spotlight-feed">
                <div class="feed-track">
                    <!-- Duplicate to loop -->
                    <div class="glass-panel feed-card">
                        <div class="feed-tag">Validated</div>
                        <h4>Lot #8849: Scottish Cashmere</h4>
                        <p class="mono text-muted" style="margin-top: 8px;">Origin: Inner Mongolia<br>Processing: Elgin, Scotland</p>
                    </div>
                    <div class="glass-panel feed-card" style="border-color: var(--accent-cyan);">
                        <div class="feed-tag" style="background: rgba(0,240,255,0.1); color: var(--accent-cyan);">Minted</div>
                        <h4>Lot #9012: ECONYL® Nylon</h4>
                        <p class="mono text-muted" style="margin-top: 8px;">Origin: Recovered Nets<br>Processing: Ljubljana, IT</p>
                    </div>
                    <div class="glass-panel feed-card" style="border-color: var(--accent-emerald);">
                        <div class="feed-tag" style="background: rgba(0,255,136,0.1); color: var(--accent-emerald);">Audited</div>
                        <h4>Lot #7731: Supima Wool</h4>
                        <p class="mono text-muted" style="margin-top: 8px;">Origin: AU Farm 88A<br>Processing: Biella, IT</p>
                    </div>
                    <!-- Clones -->
                    <div class="glass-panel feed-card">
                        <div class="feed-tag">Validated</div>
                        <h4>Lot #8849: Scottish Cashmere</h4>
                        <p class="mono text-muted" style="margin-top: 8px;">Origin: Inner Mongolia<br>Processing: Elgin, Scotland</p>
                    </div>
                    <div class="glass-panel feed-card" style="border-color: var(--accent-cyan);">
                        <div class="feed-tag" style="background: rgba(0,240,255,0.1); color: var(--accent-cyan);">Minted</div>
                        <h4>Lot #9012: ECONYL® Nylon</h4>
                        <p class="mono text-muted" style="margin-top: 8px;">Origin: Recovered Nets<br>Processing: Ljubljana, IT</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 10 & 11. FAQ & Governance Accordion -->
        <section id="compliance" class="container reveal">
            <h2 style="text-align: center; margin-bottom: var(--space-xl);">Legislative Intelligence.</h2>
            <div class="accordion">
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">
                        Does Canopy OS support the EU ESPR & Digital Product Passport directives?
                        <div class="accordion-icon"></div>
                    </button>
                    <div class="accordion-content">
                        <p style="padding-top: 16px;">Yes. Canopy Ledger inherently structures its graph data to comply with the European Ecodesign for Sustainable Products Regulation (ESPR). It automatically exposes formatted data interfaces for consumer-facing QR/NFC Digital Product Passports.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">
                        How does the platform integrate with SAP and legacy ERPs?
                        <div class="accordion-icon"></div>
                    </button>
                    <div class="accordion-content">
                        <p style="padding-top: 16px;">We supply native REST and GraphQL APIs, alongside deep connectors for SAP S/4HANA, Microsoft Dynamics, and Centric PLM. Purchase orders trigger tracing events automatically—no double data entry.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">
                        Can it track Scope 3 GHG emissions?
                        <div class="accordion-icon"></div>
                    </button>
                    <div class="accordion-content">
                        <p style="padding-top: 16px;">The OS uses primary data from energy meters at Tier 2/3 processing sites. It calculates ISO 14064 compliant carbon footprints per PO, moving away from flawed industry-average estimates.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">
                        What happens if a supplier refuses to onboard?
                        <div class="accordion-icon"></div>
                    </button>
                    <div class="accordion-content">
                        <p style="padding-top: 16px;">Our Cascading Invite protocol makes supplier onboarding frictionless. If hard refusals occur, the platform uses available proxy data or flags the node for executive intervention, locking specific compliance claims.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 12. Final Gateway -->
        <section class="container reveal">
            <div class="gateway-portal">
                <h2>Deploy the Ledger.</h2>
                <p class="text-muted" style="margin-bottom: var(--space-lg);">Secure an architectural review for your sourcing infrastructure.</p>
                <form id="lead-form" onsubmit="event.preventDefault();">
                    <div class="form-group">
                        <label class="form-label" for="form-name">Executive Name</label>
                        <input type="text" id="form-name" class="form-input" required placeholder="e.g. Jane Doe">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="form-house">Fashion House / Brand</label>
                        <input type="text" id="form-house" class="form-input" required placeholder="e.g. Acme Group">
                    </div>
                    <button type="submit" class="btn btn-primary submit-btn">Request Secure Gateway Link</button>
                </form>
            </div>
        </section>
    </main>

    <!-- 13. Footer -->
    <footer class="footer container reveal">
        <div class="footer-grid">
            <div>
                <div class="brand" style="margin-bottom: 24px;">Canopy Ledger</div>
                <p class="text-muted" style="max-width: 300px;">Cryptographic operations systems for the future of global luxury sourcing.</p>
            </div>
            <div>
                <div class="footer-title">Platform</div>
                <ul class="footer-links">
                    <li><a href="#">Tracing Engine</a></li>
                    <li><a href="#">Emissions Calculus</a></li>
                    <li><a href="#">Supplier Portal</a></li>
                    <li><a href="#">APIs</a></li>
                </ul>
            </div>
            <div>
                <div class="footer-title">Intelligence</div>
                <ul class="footer-links">
                    <li><a href="#">EU ESPR Briefing</a></li>
                    <li><a href="#">NY Fashion Act</a></li>
                    <li><a href="#">Zero-Knowledge Proofs</a></li>
                </ul>
            </div>
            <div>
                <div class="footer-title">Legal</div>
                <ul class="footer-links">
                    <li><a href="#">Privacy Protocol</a></li>
                    <li><a href="#">Terms of Service</a></li>
                    <li><span class="status-pill" style="display:inline-block; margin-top:8px;">SOC2 Type II Certified</span></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <span>&copy; 2026 Canopy Ledger OS. All rights reserved.</span>
            <span>Operating Region: GLOBAL / EU-US</span>
        </div>
    </footer>

    <!-- Modal -->
    <div class="modal-overlay" id="demo-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
        <div class="modal-content">
            <button class="modal-close" aria-label="Close modal">&times;</button>
            <h3 id="modal-title">Initialize Sandbox Environment</h3>
            <p class="text-muted" style="margin-bottom: var(--space-md);">Enter your corporate credentials to access a secure instance of the Canopy OS.</p>
            <form id="modal-form" onsubmit="event.preventDefault();">
                <div class="form-group">
                    <label class="form-label">Corporate Email</label>
                    <input type="email" class="form-input" required>
                </div>
                <button type="submit" class="btn btn-primary submit-btn">Provision Sandbox</button>
            </form>
        </div>
    </div>

    <!-- Toast Container -->
    <div class="toast-container" id="toast-container"></div>

    <!-- Micro-Interactions & App Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            
            // 1. Navbar Scroll Transition
            const navbar = document.getElementById('navbar');
            window.addEventListener('scroll', () => {
                if (window.scrollY > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }
            });

            // 2. Glow Tracking on Cards
            const cards = document.querySelectorAll('.feature-card');
            cards.forEach(card => {
                card.addEventListener('mousemove', e => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    card.style.setProperty('--mouse-x', `${x}px`);
                    card.style.setProperty('--mouse-y', `${y}px`);
                });
            });

            // 3. Platform Tabs
            const tabBtns = document.querySelectorAll('.tab-btn');
            const tabContents = document.querySelectorAll('.tab-content');
            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Reset all
                    tabBtns.forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
                    tabContents.forEach(c => c.classList.remove('active'));
                    // Activate target
                    btn.classList.add('active');
                    btn.setAttribute('aria-selected', 'true');
                    const targetId = btn.getAttribute('data-target');
                    document.getElementById(targetId).classList.add('active');
                });
            });

            // 4. Comparison Tool
            const btnLegacy = document.getElementById('btn-legacy');
            const btnCanopy = document.getElementById('btn-canopy');
            const paneLegacy = document.getElementById('pane-legacy');
            const paneCanopy = document.getElementById('pane-canopy');
            
            btnLegacy.addEventListener('click', () => {
                btnLegacy.classList.add('active');
                btnCanopy.classList.remove('active');
                paneLegacy.style.opacity = '1';
                paneLegacy.style.zIndex = '2';
                paneCanopy.style.opacity = '0';
                paneCanopy.style.zIndex = '1';
            });
            btnCanopy.addEventListener('click', () => {
                btnCanopy.classList.add('active');
                btnLegacy.classList.remove('active');
                paneCanopy.style.opacity = '1';
                paneCanopy.style.zIndex = '2';
                paneLegacy.style.opacity = '0';
                paneLegacy.style.zIndex = '1';
            });

            // 5. Accordion Logic
            const accordions = document.querySelectorAll('.accordion-header');
            accordions.forEach(acc => {
                acc.addEventListener('click', () => {
                    const item = acc.parentElement;
                    const isOpen = item.classList.contains('open');
                    
                    // Close all
                    document.querySelectorAll('.accordion-item').forEach(i => {
                        i.classList.remove('open');
                        i.querySelector('.accordion-header').setAttribute('aria-expanded', 'false');
                    });
                    
                    // Open if it wasn't open
                    if (!isOpen) {
                        item.classList.add('open');
                        acc.setAttribute('aria-expanded', 'true');
                    }
                });
            });

            // 6. Modal Logic
            const modal = document.getElementById('demo-modal');
            const demoTriggers = document.querySelectorAll('.demo-trigger');
            const modalClose = document.querySelector('.modal-close');
            
            function openModal() {
                modal.classList.add('active');
                document.body.style.overflow = 'hidden'; // prevent bg scroll
            }
            function closeModal() {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
            
            demoTriggers.forEach(t => t.addEventListener('click', openModal));
            modalClose.addEventListener('click', closeModal);
            modal.addEventListener('click', e => {
                if(e.target === modal) closeModal();
            });
            document.addEventListener('keydown', e => {
                if(e.key === 'Escape' && modal.classList.contains('active')) closeModal();
            });

            // 7. Toast Notification & Form Logic
            function showToast(message) {
                const container = document.getElementById('toast-container');
                const toast = document.createElement('div');
                toast.className = 'toast';
                toast.innerHTML = `<div class="status-dot"></div> ${message}`;
                container.appendChild(toast);
                
                // Trigger reflow
                void toast.offsetWidth;
                toast.classList.add('show');
                
                setTimeout(() => {
                    toast.classList.remove('show');
                    setTimeout(() => toast.remove(), 500);
                }, 4000);
            }

            document.getElementById('lead-form').addEventListener('submit', () => {
                showToast("Secure Gateway Link Sent. Check your inbox.");
                document.getElementById('lead-form').reset();
            });
            document.getElementById('modal-form').addEventListener('submit', () => {
                closeModal();
                showToast("Sandbox provisioning initiated.");
                document.getElementById('modal-form').reset();
            });

            // 8. Scroll Reveal & Count-Up Observers
            const revealElements = document.querySelectorAll('.reveal');
            
            const revealObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        revealObserver.unobserve(entry.target);
                        
                        // Check if it has count-up
                        if(entry.target.querySelector('.metric-num')) {
                            const counters = entry.target.querySelectorAll('.metric-num');
                            counters.forEach(counter => {
                                const target = parseFloat(counter.getAttribute('data-count'));
                                const duration = 2000;
                                const step = target / (duration / 16); // 60fps
                                let current = 0;
                                
                                const update = () => {
                                    current += step;
                                    if(current < target) {
                                        // format nicely
                                        let val = 0;
                                        if(target % 1 !== 0) {
                                            val = current.toFixed(1);
                                        } else {
                                            val = Math.floor(current).toLocaleString();
                                        }
                                        if(target === 0) val = 0; // The zero greenwashing exception
                                        counter.innerText = val;
                                        requestAnimationFrame(update);
                                    } else {
                                        counter.innerText = (target % 1 !== 0) ? target.toFixed(1) : target.toLocaleString();
                                    }
                                };
                                requestAnimationFrame(update);
                            });
                        }
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: "0px 0px -50px 0px"
            });

            revealElements.forEach(el => revealObserver.observe(el));
        });
    </script>
</body>
</html>
"""
with open('fdu_020/src/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
