import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relay Vault - Command Readiness</title>
    <style>
        :root {
            /* Color System */
            --bg-dark: #050a12;
            --bg-deep: #020408;
            --glass-bg: rgba(16, 25, 45, 0.4);
            --glass-border: rgba(90, 150, 255, 0.2);
            --glass-highlight: rgba(120, 180, 255, 0.3);
            
            --accent-cyan: #00f3ff;
            --accent-magenta: #e800d5;
            --accent-blue: #0066ff;
            --accent-neon: #39ff14;
            
            --text-main: #e0f0ff;
            --text-muted: #8096b0;
            --text-dark: #2a3d58;

            /* Blur & Glass Effect */
            --blur-heavy: blur(40px);
            --blur-medium: blur(20px);
            --blur-light: blur(10px);
            --blur-subtle: blur(4px);

            /* Typography */
            --font-mono: ui-monospace, 'SF Mono', Menlo, Courier, monospace;
            --font-sans: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            
            /* Scale */
            --space-xs: 0.5rem;
            --space-sm: 1rem;
            --space-md: 2rem;
            --space-lg: 4rem;
            --space-xl: 8rem;

            --radius-sm: 8px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-xl: 40px;

            --transition-snap: 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
            --transition-smooth: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            --transition-slow: 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html, body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: var(--font-sans);
            line-height: 1.6;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: 
                radial-gradient(circle at 20% 30%, rgba(0, 102, 255, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(232, 0, 213, 0.1) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(0, 243, 255, 0.05) 0%, transparent 60%);
            z-index: -2;
            pointer-events: none;
        }

        .ambient-orb {
            position: fixed;
            border-radius: 50%;
            filter: var(--blur-heavy);
            z-index: -1;
            animation: float-orb 20s infinite alternate ease-in-out;
            opacity: 0.6;
            pointer-events: none;
            will-change: transform;
        }

        .orb-1 { width: 40vw; height: 40vw; background: var(--accent-blue); top: -10vw; left: -10vw; }
        .orb-2 { width: 35vw; height: 35vw; background: var(--accent-magenta); bottom: 10vw; right: -5vw; animation-delay: -5s; }
        .orb-3 { width: 25vw; height: 25vw; background: var(--accent-cyan); top: 40vh; left: 40vw; animation-delay: -10s; }

        @keyframes float-orb {
            0% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(5vw, 10vh) scale(1.1); }
            100% { transform: translate(-5vw, -5vh) scale(0.9); }
        }

        /* Utilities */
        .glass-panel {
            background: var(--glass-bg);
            backdrop-filter: var(--blur-medium);
            -webkit-backdrop-filter: var(--blur-medium);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-md);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
            transition: all var(--transition-smooth);
        }

        .glass-panel::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, var(--glass-highlight), transparent);
        }

        .glow-text {
            text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
        }
        
        .mono {
            font-family: var(--font-mono);
            letter-spacing: -0.02em;
        }

        h1, h2, h3 { font-weight: 500; letter-spacing: -0.03em; }
        h1 { font-size: clamp(3rem, 6vw, 6rem); line-height: 1.1; margin-bottom: var(--space-sm); }
        h2 { font-size: clamp(2rem, 4vw, 3.5rem); margin-bottom: var(--space-md); }
        h3 { font-size: 1.5rem; margin-bottom: var(--space-sm); color: var(--accent-cyan); }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 var(--space-md);
        }

        section {
            padding: var(--space-xl) 0;
            position: relative;
        }

        /* Custom Cursor */
        #cursor-glow {
            position: fixed;
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(0, 243, 255, 0.15) 0%, transparent 70%);
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            transition: width 0.3s, height 0.3s;
            mix-blend-mode: screen;
            will-change: left, top;
        }

        /* 1. Abstract Hero Glo */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding-top: var(--space-xl);
        }

        .hero-card {
            padding: var(--space-lg);
            max-width: 800px;
            border-radius: var(--radius-lg);
            transition: transform var(--transition-smooth);
        }

        .hero-subtitle {
            font-family: var(--font-mono);
            color: var(--accent-cyan);
            text-transform: uppercase;
            font-size: 0.9rem;
            letter-spacing: 0.2em;
            margin-bottom: var(--space-sm);
            display: inline-block;
        }

        .cta-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 1rem 2rem;
            margin-top: var(--space-md);
            font-family: var(--font-mono);
            font-size: 1rem;
            color: #fff;
            background: rgba(0, 102, 255, 0.2);
            border: 1px solid var(--accent-cyan);
            border-radius: var(--radius-sm);
            text-decoration: none;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: all var(--transition-snap);
            box-shadow: 0 0 20px rgba(0, 243, 255, 0.1);
        }

        .cta-btn::before {
            content: '';
            position: absolute;
            top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transform: skewX(-20deg);
            transition: var(--transition-smooth);
        }

        .cta-btn:hover {
            background: rgba(0, 102, 255, 0.4);
            box-shadow: 0 0 30px rgba(0, 243, 255, 0.3);
            transform: translateY(-2px);
        }

        .cta-btn:hover::before {
            left: 200%;
        }

        /* 2. Global Readiness Index */
        .ticker-wrap {
            width: 100%;
            background: rgba(2, 4, 8, 0.8);
            border-top: 1px solid var(--glass-border);
            border-bottom: 1px solid var(--glass-border);
            padding: 0.75rem 0;
            overflow: hidden;
            position: relative;
            z-index: 10;
        }

        .ticker-inner {
            display: flex;
            width: 200%;
            animation: ticker 30s linear infinite;
        }

        .ticker-item {
            flex-shrink: 0;
            padding: 0 2rem;
            font-family: var(--font-mono);
            font-size: 0.85rem;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .status-dot {
            width: 8px; height: 8px; border-radius: 50%;
        }
        .dot-green { background: var(--accent-neon); box-shadow: 0 0 8px var(--accent-neon); }
        .dot-yellow { background: #ffd700; box-shadow: 0 0 8px #ffd700; }
        .dot-red { background: #ff003c; box-shadow: 0 0 8px #ff003c; }

        @keyframes ticker {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        /* 3. System Overview */
        .grid-3 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: var(--space-md);
            margin-top: var(--space-lg);
        }

        .interactive-card {
            padding: var(--space-md);
            transition: transform var(--transition-snap), border-color var(--transition-snap), background var(--transition-snap);
            cursor: pointer;
            --mouse-x: 50%;
            --mouse-y: 50%;
        }

        .interactive-card:hover {
            transform: translateY(-5px);
            border-color: var(--accent-cyan);
            background: rgba(16, 25, 45, 0.6);
        }
        
        .card-icon {
            font-size: 2rem;
            color: var(--accent-magenta);
            margin-bottom: var(--space-sm);
            display: block;
        }

        /* 4. Threat Matrix Radar */
        .radar-container {
            width: 400px;
            height: 400px;
            margin: 0 auto;
            position: relative;
            background: radial-gradient(circle, rgba(0, 243, 255, 0.05) 0%, transparent 70%);
            border-radius: 50%;
            border: 1px solid rgba(0, 243, 255, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .radar-grid {
            position: absolute; width: 100%; height: 100%; border-radius: 50%;
            background-image: 
                linear-gradient(rgba(0, 243, 255, 0.2) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 243, 255, 0.2) 1px, transparent 1px);
            background-size: 40px 40px;
            background-position: center center;
        }

        .radar-rings {
            position: absolute; width: 100%; height: 100%; border-radius: 50%;
            border: 1px solid rgba(0, 243, 255, 0.1);
            box-shadow: inset 0 0 0 40px transparent, inset 0 0 0 41px rgba(0, 243, 255, 0.1),
                        inset 0 0 0 80px transparent, inset 0 0 0 81px rgba(0, 243, 255, 0.1),
                        inset 0 0 0 120px transparent, inset 0 0 0 121px rgba(0, 243, 255, 0.1);
        }

        .radar-sweep {
            position: absolute; width: 50%; height: 50%;
            top: 0; left: 50%;
            background: conic-gradient(from 0deg, transparent 70%, rgba(0, 243, 255, 0.5) 100%);
            transform-origin: 0% 100%;
            animation: radar-spin 4s linear infinite;
        }

        .data-point {
            position: absolute; width: 6px; height: 6px;
            background: var(--accent-cyan); border-radius: 50%;
            box-shadow: 0 0 10px var(--accent-cyan);
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: crosshair;
        }
        .data-point:hover { transform: scale(3); box-shadow: 0 0 20px #fff; }

        @keyframes radar-spin { 100% { transform: rotate(360deg); } }

        /* 5. Live Scenario Dossier */
        .scrolly-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-lg);
            align-items: start;
        }

        .sticky-panel {
            position: sticky;
            top: 100px;
            padding: var(--space-md);
            height: 70vh;
            display: flex; flex-direction: column;
        }

        .scroll-steps {
            display: flex; flex-direction: column; gap: 50vh;
            padding-bottom: 50vh;
            margin-top: 10vh;
        }

        .step-card {
            opacity: 0.3;
            transition: opacity var(--transition-smooth), transform var(--transition-smooth);
            transform: translateX(20px);
            padding: var(--space-md);
        }

        .step-card.active {
            opacity: 1; transform: translateX(0);
            border-color: var(--accent-cyan);
        }

        .dossier-line {
            display: flex; justify-content: space-between;
            margin-bottom: 0.5rem;
            border-bottom: 1px dashed var(--glass-border);
            padding-bottom: 0.25rem;
        }

        /* 6. Comms Drift Analysis */
        .drift-graph {
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 300px;
            position: relative;
        }
        
        .drift-node {
            width: 60px; height: 60px;
            border-radius: 50%; background: var(--glass-bg);
            border: 2px solid var(--accent-blue);
            display: flex; align-items: center; justify-content: center;
            font-family: var(--font-mono); font-size: 0.8rem;
            position: relative; z-index: 2;
            transition: all 0.3s;
        }
        .drift-node:hover { background: var(--accent-blue); color: #fff; box-shadow: 0 0 20px var(--accent-blue); }

        .drift-line {
            position: absolute; height: 2px;
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-magenta));
            top: 50%; transform: translateY(-50%);
            z-index: 1;
            box-shadow: 0 0 10px rgba(232, 0, 213, 0.5);
            animation: pulse-line 2s infinite alternate;
        }

        @keyframes pulse-line { 0% { opacity: 0.4; } 100% { opacity: 1; } }

        /* 7. Operating Memo */
        .memo-grid {
            display: grid; grid-template-columns: 1fr 1fr;
            border-radius: var(--radius-md);
            overflow: hidden;
            border: 1px solid var(--glass-border);
        }

        .memo-col { padding: var(--space-md); }
        .memo-legacy { background: rgba(255, 0, 60, 0.05); }
        .memo-relay { background: rgba(0, 243, 255, 0.05); border-left: 1px solid var(--glass-border); }
        .memo-list li { margin-bottom: 1rem; list-style: none; position: relative; padding-left: 1.5rem; }
        .memo-legacy .memo-list li::before { content: '×'; position: absolute; left: 0; color: #ff003c; }
        .memo-relay .memo-list li::before { content: '✓'; position: absolute; left: 0; color: var(--accent-neon); }

        /* 8. Exec Dashboard */
        .dash-preview {
            perspective: 1000px;
            margin-top: var(--space-lg);
        }
        .dash-ui {
            transform: rotateX(10deg) rotateY(-10deg);
            transition: transform 0.5s ease;
            height: 400px;
            padding: var(--space-md);
            display: grid; gap: 1rem;
            grid-template-columns: 2fr 1fr;
            grid-template-rows: 1fr 2fr;
        }
        .dash-preview:hover .dash-ui { transform: rotateX(0) rotateY(0); }
        .ui-box { background: rgba(16, 25, 45, 0.8); border: 1px solid var(--glass-border); border-radius: 8px; }

        /* 9. Workflow Timeline */
        .timeline {
            display: flex; justify-content: space-between; position: relative;
            margin: var(--space-xl) 0;
        }
        .timeline::before {
            content: ''; position: absolute; top: 15px; left: 0; right: 0; height: 2px;
            background: var(--glass-border); z-index: 0;
        }
        .time-node {
            position: relative; z-index: 1; text-align: center; width: 120px;
        }
        .node-dot {
            width: 32px; height: 32px; border-radius: 50%; background: var(--bg-dark);
            border: 2px solid var(--accent-cyan); margin: 0 auto 1rem;
            transition: all 0.3s;
        }
        .time-node:hover .node-dot { background: var(--accent-cyan); box-shadow: 0 0 15px var(--accent-cyan); }

        /* 10. Metrics */
        .metrics-grid {
            display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-md);
            text-align: center;
        }
        .metric-num {
            font-size: 3.5rem; font-weight: bold; font-family: var(--font-mono);
            background: linear-gradient(180deg, #fff, var(--accent-cyan));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem; filter: drop-shadow(0 0 10px rgba(0,243,255,0.3));
        }

        /* 11. Testimonials */
        .testament {
            border-left: 4px solid var(--accent-magenta);
            padding-left: var(--space-md);
            margin-bottom: var(--space-md);
            font-style: italic; color: var(--text-muted);
        }

        /* 12. Interactive Checklist */
        .check-item {
            display: flex; align-items: center; justify-content: space-between;
            padding: 1rem; border-bottom: 1px solid var(--glass-border);
            cursor: pointer; transition: background 0.2s;
        }
        .check-item:hover { background: rgba(255,255,255,0.02); }
        .toggle {
            width: 40px; height: 20px; border-radius: 10px; background: rgba(255,255,255,0.1);
            position: relative; transition: 0.3s;
        }
        .toggle::after {
            content: ''; position: absolute; top: 2px; left: 2px; width: 16px; height: 16px;
            background: #fff; border-radius: 50%; transition: 0.3s;
        }
        .check-item.active .toggle { background: var(--accent-neon); box-shadow: 0 0 10px var(--accent-neon); }
        .check-item.active .toggle::after { left: 22px; }
        .check-item.active .check-label { text-decoration: line-through; opacity: 0.5; }

        /* 13. FAQ */
        .faq-item {
            border-bottom: 1px solid var(--glass-border);
            overflow: hidden;
        }
        .faq-q { padding: 1.5rem 0; cursor: pointer; display: flex; justify-content: space-between; font-weight: bold; }
        .faq-a { max-height: 0; transition: max-height 0.4s ease; color: var(--text-muted); padding: 0 1rem; }
        .faq-item.open .faq-a { max-height: 200px; padding-bottom: 1.5rem; }
        .faq-item:hover .faq-q { color: var(--accent-cyan); text-shadow: 0 0 5px rgba(0,243,255,0.5); }

        /* 14. Terminal CTA */
        .terminal-cta { text-align: center; position: relative; overflow: hidden; padding: var(--space-xl) 0; }
        .core-orb {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 300px; height: 300px; background: var(--accent-cyan);
            border-radius: 50%; filter: var(--blur-heavy); opacity: 0.2;
            animation: pulse-core 4s infinite alternate;
        }
        @keyframes pulse-core { 100% { transform: translate(-50%, -50%) scale(1.2); opacity: 0.4; } }

        /* 15. Footer */
        footer { padding: var(--space-lg) 0; border-top: 1px solid var(--glass-border); text-align: center; font-size: 0.9rem; color: var(--text-muted); }
        .foot-links a { color: var(--text-muted); text-decoration: none; margin: 0 1rem; transition: color 0.2s; }
        .foot-links a:hover { color: var(--accent-cyan); }
        
        .fade-up { opacity: 0; transform: translateY(30px); transition: all 0.8s ease; }
        .fade-up.visible { opacity: 1; transform: translateY(0); }

        @media (max-width: 768px) {
            .scrolly-container { grid-template-columns: 1fr; }
            .sticky-panel { position: static; height: auto; margin-bottom: 2rem; }
            .scroll-steps { gap: 2rem; padding-bottom: 2rem; }
            .memo-grid { grid-template-columns: 1fr; }
            .metrics-grid { grid-template-columns: 1fr 1fr; }
            .timeline { flex-direction: column; align-items: flex-start; margin-left: 20px; }
            .timeline::before { width: 2px; height: 100%; top: 0; left: 15px; }
            .time-node { display: flex; align-items: center; width: auto; margin-bottom: 2rem; text-align: left; }
            .node-dot { margin: 0 1rem 0 0; }
        }
    </style>
</head>
<body>
    <div id="cursor-glow"></div>
    
    <div class="ambient-orb orb-1"></div>
    <div class="ambient-orb orb-2"></div>
    <div class="ambient-orb orb-3"></div>

    <!-- Section 2. Global Readiness Index -->
    <div class="ticker-wrap">
        <div class="ticker-inner">
            <div class="ticker-item"><span class="status-dot dot-green"></span> SYSTEM NOMINAL | GLOBE: SECURE | NODE-7: ACTIVE</div>
            <div class="ticker-item"><span class="status-dot dot-yellow"></span> WARNING | SUPPLY CHAIN LOGISTICS | ETA DELAY +4HRS</div>
            <div class="ticker-item"><span class="status-dot dot-red"></span> ALERT | CYBER ESCALATION | SECTOR 4 QUARANTINED</div>
            <div class="ticker-item"><span class="status-dot dot-green"></span> EXEC COMMS | ENCRYPTED CHANNEL OPEN | 99.9% UPTIME</div>
            <div class="ticker-item"><span class="status-dot dot-green"></span> SYSTEM NOMINAL | GLOBE: SECURE | NODE-7: ACTIVE</div>
            <div class="ticker-item"><span class="status-dot dot-yellow"></span> WARNING | SUPPLY CHAIN LOGISTICS | ETA DELAY +4HRS</div>
            <div class="ticker-item"><span class="status-dot dot-red"></span> ALERT | CYBER ESCALATION | SECTOR 4 QUARANTINED</div>
            <div class="ticker-item"><span class="status-dot dot-green"></span> EXEC COMMS | ENCRYPTED CHANNEL OPEN | 99.9% UPTIME</div>
        </div>
    </div>

    <!-- Section 1. Abstract Hero Glo -->
    <section class="hero">
        <div class="container hero-card glass-panel fade-up">
            <span class="hero-subtitle glow-text">Protocol RV-001 // Command Readiness</span>
            <h1>Rehearse the Unthinkable.</h1>
            <p style="font-size: 1.2rem; color: var(--text-muted); margin-bottom: 2rem;">
                Relay Vault is the premiere executive incident readiness platform. Simulate supply disruptions, cyber escalations, and comms drift in a secure, zero-latency holographic war room.
            </p>
            <a href="#" class="cta-btn">Request Briefing Pack</a>
        </div>
    </section>

    <!-- Section 3. System Overview -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-02 // CORE VECTORS</span>
        <h2>Operational Horizons</h2>
        <div class="grid-3">
            <div class="glass-panel interactive-card">
                <span class="card-icon">⟡</span>
                <h3>Cyber Escalation</h3>
                <p>Simulate ransomware containment protocols. Instantly partition networks and observe cross-node contamination metrics in real time.</p>
            </div>
            <div class="glass-panel interactive-card">
                <span class="card-icon">⎈</span>
                <h3>Supply Disruption</h3>
                <p>Map secondary and tertiary vendor failure chains. Inject randomized logistics nodes drops to test procurement resilience.</p>
            </div>
            <div class="glass-panel interactive-card">
                <span class="card-icon">◈</span>
                <h3>Executive Comms Drift</h3>
                <p>Analyze latency between incident identification and board notification. Ensure unified messaging under fractured intel conditions.</p>
            </div>
        </div>
    </section>

    <!-- Section 4. Threat Matrix Radar -->
    <section class="container fade-up" style="text-align: center;">
        <span class="mono glow-text">RV-03 // SCANNING</span>
        <h2>Active Threat Matrix</h2>
        <p style="color:var(--text-muted); margin-bottom: 3rem;">Hover over detected anomalies to decrypt preliminary diagnostics.</p>
        <div class="radar-container">
            <div class="radar-grid"></div>
            <div class="radar-rings"></div>
            <div class="radar-sweep"></div>
            <div class="data-point" style="top: 30%; left: 60%;" title="Phishing Vector Alpha"></div>
            <div class="data-point" style="top: 70%; left: 30%;" title="Node Disconnect"></div>
            <div class="data-point" style="top: 50%; left: 80%;" title="Data Exfil Attempt"></div>
            <div class="data-point" style="top: 20%; left: 40%;" title="API Rate Limit Spike"></div>
        </div>
    </section>

    <!-- Section 5. Live Scenario Dossier -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-04 // SCENARIO DOSSIER</span>
        <h2>Live Rehearsal Protocol</h2>
        <div class="scrolly-container">
            <div class="sticky-panel glass-panel">
                <h3 id="dossier-title" class="glow-text">Awaiting Trigger...</h3>
                <div style="flex: 1; border: 1px solid var(--glass-border); padding: 1rem; border-radius: 4px; background: rgba(0,0,0,0.3); font-family: var(--font-mono); font-size: 0.85rem;">
                    <div class="dossier-line"><span>STATUS:</span><span id="dos-status" style="color:var(--text-main);">IDLE</span></div>
                    <div class="dossier-line"><span>OWNER:</span><span id="dos-owner" style="color:var(--text-main);">--</span></div>
                    <div class="dossier-line"><span>COMMS LATENCY:</span><span id="dos-latency" style="color:var(--text-main);">0ms</span></div>
                    <div class="dossier-line"><span>MITIGATION RISK:</span><span id="dos-risk" style="color:var(--text-main);">--</span></div>
                    <br>
                    <p id="dos-desc" style="color: var(--accent-magenta); min-height: 80px;">Initiate scroll sequence to advance simulation timeline.</p>
                </div>
            </div>
            <div class="scroll-steps">
                <div class="step-card glass-panel interactive-card" data-title="T+00: The Trigger" data-status="CRITICAL" data-owner="NOC Level 1" data-latency="12ms" data-risk="HIGH" data-desc="Primary DB firewall breached via zero-day exploit. Unauthorized lateral movement detected.">
                    <h3>Step 1: The Trigger</h3>
                    <p>Alert registers on the NOC board. Initial assessment indicates a highly sophisticated intrusion mechanism.</p>
                </div>
                <div class="step-card glass-panel interactive-card" data-title="T+15: First Response" data-status="ACTIVE MITIGATION" data-owner="Cyber Task Force" data-latency="45ms" data-risk="SEVERE" data-desc="Protocols enacted to sandbox infected subnets. Primary servers locked down.">
                    <h3>Step 2: First 15 Minutes</h3>
                    <p>Immediate containment efforts begin. Cross-departmental communication lines established.</p>
                </div>
                <div class="step-card glass-panel interactive-card" data-title="T+45: Exec Comms" data-status="BOARD BRIEFING" data-owner="C-Suite Ops" data-latency="150ms" data-risk="REPUTATIONAL" data-desc="Drafting external messaging. Parsing technical jargon into board-ready deliverables.">
                    <h3>Step 3: Executive Brief</h3>
                    <p>Translating technical chaos into structured business risk matrices for immediate board review.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 6. Comms Drift Analysis -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-05 // DRIFT DIAGNOSTIC</span>
        <h2>Communication Drift Mapping</h2>
        <div class="glass-panel" style="padding: var(--space-md);">
            <div class="drift-graph">
                <div class="drift-line" style="width: 100%; left: 0;"></div>
                <div class="drift-node">INC</div>
                <div class="drift-node">NOC</div>
                <div class="drift-node">ENG</div>
                <div class="drift-node">PR</div>
                <div class="drift-node">EXEC</div>
            </div>
            <p style="text-align: center; margin-top: 1rem; color: var(--text-muted); font-family: var(--font-mono);">Optimal information flow trajectory without distortion.</p>
        </div>
    </section>

    <!-- Section 7. Operating Memo -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-06 // TACTICAL MEMO</span>
        <h2>Legacy vs. Relay Vault Protocol</h2>
        <div class="memo-grid">
            <div class="memo-col memo-legacy">
                <h3 style="color: #ff003c;">Legacy Rehearsals</h3>
                <ul class="memo-list mono" style="font-size: 0.9rem;">
                    <li>Static PDF playbooks</li>
                    <li>Siloed departmental responses</li>
                    <li>Manual timeline tracking</li>
                    <li>Retrospective post-mortem only</li>
                    <li>Reactionary exec briefings</li>
                </ul>
            </div>
            <div class="memo-col memo-relay">
                <h3 style="color: var(--accent-neon);">Relay Vault</h3>
                <ul class="memo-list mono" style="font-size: 0.9rem;">
                    <li>Dynamic algorithmic injects</li>
                    <li>Unified encrypted command pane</li>
                    <li>Automated audit logging</li>
                    <li>Real-time drift analytics</li>
                    <li>Proactive PR/Exec templating</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Section 8. Dashboard Preview -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-07 // INTERFACE</span>
        <h2>Executive Dashboard UI</h2>
        <p style="color: var(--text-muted);">Hover to simulate interface initialization sequence.</p>
        <div class="dash-preview">
            <div class="dash-ui glass-panel">
                <div class="ui-box" style="grid-column: 1/3; display: flex; align-items:center; padding: 1rem;">
                    <div style="width: 50%; height: 20px; background: rgba(0,243,255,0.2); border-radius: 4px;"></div>
                </div>
                <div class="ui-box" style="padding:1rem;"><div style="background: rgba(232,0,213,0.3); height:100%; border-radius:4px;"></div></div>
                <div class="ui-box" style="grid-row:2/4; background: linear-gradient(to bottom, rgba(16,25,45,0.8), rgba(232,0,213,0.1)); padding:1rem;">
                    <ul style="list-style:none; opacity:0.5;">
                        <li style="height:15px; background:var(--glass-border); margin-bottom:10px;"></li>
                        <li style="height:15px; background:var(--glass-border); margin-bottom:10px;"></li>
                        <li style="height:15px; background:var(--glass-border); margin-bottom:10px;"></li>
                    </ul>
                </div>
                <div class="ui-box"></div>
            </div>
        </div>
    </section>

    <!-- Section 9. Workflow Timeline -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-08 // CADENCE</span>
        <h2>Rehearsal Pipeline</h2>
        <div class="timeline">
            <div class="time-node">
                <div class="node-dot"></div>
                <span class="mono glow-text">DAY 0</span>
                <p>Scope Design</p>
            </div>
            <div class="time-node">
                <div class="node-dot"></div>
                <span class="mono glow-text">DAY 7</span>
                <p>Node Mapping</p>
            </div>
            <div class="time-node">
                <div class="node-dot"></div>
                <span class="mono glow-text">DAY 14</span>
                <p>Live Injects</p>
            </div>
            <div class="time-node">
                <div class="node-dot"></div>
                <span class="mono glow-text">DAY 21</span>
                <p>Drift Analysis</p>
            </div>
            <div class="time-node">
                <div class="node-dot"></div>
                <span class="mono glow-text">DAY 30</span>
                <p>Exec Report</p>
            </div>
        </div>
    </section>

    <!-- Section 10. Metrics -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-09 // IMPACT</span>
        <h2>Proof of Readiness</h2>
        <div class="metrics-grid">
            <div class="glass-panel" style="padding: 2rem;">
                <div class="metric-num">94%</div>
                <span class="mono">Faster Mitigation</span>
            </div>
            <div class="glass-panel" style="padding: 2rem;">
                <div class="metric-num">0.0</div>
                <span class="mono">Comms Drift</span>
            </div>
            <div class="glass-panel" style="padding: 2rem;">
                <div class="metric-num">12k+</div>
                <span class="mono">Simulations</span>
            </div>
            <div class="glass-panel" style="padding: 2rem;">
                <div class="metric-num">Tier-1</div>
                <span class="mono">Audit Compliance</span>
            </div>
        </div>
    </section>

    <!-- Section 11. Testimonials -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-10 // ENCRYPTED COMMS</span>
        <h2>Operator Transcripts</h2>
        <div class="grid-3">
            <div class="glass-panel" style="padding: var(--space-md);">
                <div class="testament">"When they injected the redundant ISP failure midway through our ransomware drill, it broke our manual playbooks entirely. Relay Vault forced our team to adapt structurally."</div>
                <span class="mono" style="color: var(--accent-cyan);">- Dir. of Infrastructure</span>
            </div>
            <div class="glass-panel" style="padding: var(--space-md);">
                <div class="testament">"I no longer walk into the boardroom with sanitized metrics. I walk in with audited telemetry from our last high-stress rehearsal. Confidence is night and day."</div>
                <span class="mono" style="color: var(--accent-cyan);">- Chief Risk Officer</span>
            </div>
            <div class="glass-panel" style="padding: var(--space-md);">
                <div class="testament">"The drift analytics alone justified the integration. Identifying exactly where the technical ground-truth morphed into bad strategic advice saved our Q3."</div>
                <span class="mono" style="color: var(--accent-cyan);">- VP of Communications</span>
            </div>
        </div>
    </section>

    <!-- Section 12. Checklist -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-11 // ACTION PLAN</span>
        <h2>Initiation Checklist</h2>
        <div class="glass-panel" style="max-width: 600px; margin: 0 auto;">
            <div class="check-item" onclick="this.classList.toggle('active')">
                <span class="mono check-label">Define core threat vectors</span>
                <div class="toggle"></div>
            </div>
            <div class="check-item" onclick="this.classList.toggle('active')">
                <span class="mono check-label">Map key executive stakeholders</span>
                <div class="toggle"></div>
            </div>
            <div class="check-item" onclick="this.classList.toggle('active')">
                <span class="mono check-label">Establish baseline latency SLAs</span>
                <div class="toggle"></div>
            </div>
            <div class="check-item" onclick="this.classList.toggle('active')">
                <span class="mono check-label">Schedule inaugural live inject</span>
                <div class="toggle"></div>
            </div>
        </div>
    </section>

    <!-- Section 13. FAQ -->
    <section class="container fade-up">
        <span class="mono glow-text">RV-12 // ARCHIVE</span>
        <h2>Knowledge Base</h2>
        <div class="glass-panel" style="padding: 0 2rem;">
            <div class="faq-item">
                <div class="faq-q">Does Relay Vault require direct network integration? <span>+</span></div>
                <div class="faq-a">No. The platform can operate completely completely air-gapped from your production environment, relying on API-driven scenario injections that do not alter core routing.</div>
            </div>
            <div class="faq-item">
                <div class="faq-q">How are "live injects" generated? <span>+</span></div>
                <div class="faq-a">We utilize continuous OSINT feeds combined with custom ML models to generate localized, plausible escalation variables specific to your stack.</div>
            </div>
            <div class="faq-item">
                <div class="faq-q">Can we export compliance audit logs? <span>+</span></div>
                <div class="faq-a">Yes. Multi-format cryptographic proofs are generated post-simulation for SOC2, ISO27001, and board reporting, complete with timestamps and resolution deltas.</div>
            </div>
        </div>
    </section>

    <!-- Section 14. Terminal CTA -->
    <section class="container fade-up terminal-cta">
        <div class="glass-panel" style="padding: var(--space-xl) var(--space-md); text-align: center;">
            <div class="core-orb"></div>
            <h2 style="position:relative; z-index: 1;">Secure Your Command Core</h2>
            <p style="position:relative; z-index: 1; margin-bottom: var(--space-md);">Engage the Relay Vault onboarding protocol today.</p>
            <a href="#" class="cta-btn" style="position:relative; z-index: 1;">Initialize Protocol</a>
        </div>
    </section>

    <!-- Section 15. Footer -->
    <footer>
        <div class="container">
            <div class="mono" style="margin-bottom: 1rem;">RELAY VAULT // SYSTEM VER: 2.4.9</div>
            <div class="foot-links">
                <a href="#">Encrypted Priv</a>
                <a href="#">TOS</a>
                <a href="#">Status: NOMINAL</a>
            </div>
        </div>
    </footer>
""" + "\n" * 50 + """
    <script>
        // Custom Cursor Tracker
        const cursor = document.getElementById('cursor-glow');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // Intersection Observer for Fade-Ups
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

        // FAQ Toggles
        document.querySelectorAll('.faq-q').forEach(q => {
            q.addEventListener('click', () => {
                const parent = q.parentElement;
                parent.classList.toggle('open');
                const span = q.querySelector('span');
                span.innerText = parent.classList.contains('open') ? '-' : '+';
            });
        });

        // Scrollytelling Logic
        const steps = document.querySelectorAll('.step-card');
        const dTitle = document.getElementById('dossier-title');
        const dStatus = document.getElementById('dos-status');
        const dOwner = document.getElementById('dos-owner');
        const dLatency = document.getElementById('dos-latency');
        const dRisk = document.getElementById('dos-risk');
        const dDesc = document.getElementById('dos-desc');

        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Remove active from all
                    steps.forEach(s => s.classList.remove('active'));
                    // Add active
                    entry.target.classList.add('active');
                    
                    // Update Dossier text
                    dTitle.innerText = entry.target.getAttribute('data-title');
                    dStatus.innerText = entry.target.getAttribute('data-status');
                    dOwner.innerText = entry.target.getAttribute('data-owner');
                    dLatency.innerText = entry.target.getAttribute('data-latency');
                    dRisk.innerText = entry.target.getAttribute('data-risk');
                    dDesc.innerText = entry.target.getAttribute('data-desc');
                    dTitle.style.textShadow = '0 0 15px var(--accent-magenta)';
                    setTimeout(() => dTitle.style.textShadow = '0 0 10px rgba(0, 243, 255, 0.5)', 300);
                }
            });
        }, { rootMargin: '-40% 0px -40% 0px' });

        steps.forEach(step => scrollObserver.observe(step));
    </script>
</body>
</html>
"""

os.makedirs('fdu_032/src', exist_ok=True)
with open('fdu_032/src/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Lines Output: {len(html_content.splitlines())}")
