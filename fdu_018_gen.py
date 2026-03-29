import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Harbor Nine | Waterfront Mobility OS</title>
<style>
  :root {
    --bg-dark: #040609;
    --bg-surface: #0a0e14;
    --glow-nautical: rgba(0, 238, 255, 0.4);
    --glow-deep: rgba(0, 85, 255, 0.3);
    --glow-magenta: rgba(212, 0, 255, 0.2);
    --glass-bg: rgba(10, 14, 25, 0.4);
    --glass-border: rgba(255, 255, 255, 0.1);
    --text-primary: #ffffff;
    --text-muted: #94a3b8;
    --accent: #00eeff;
    --accent-soft: rgba(0, 238, 255, 0.1);
    --font-heading: 'Inter', system-ui, sans-serif;
    --font-body: 'Inter', system-ui, sans-serif;
    --font-mono: 'Fira Code', 'JetBrains Mono', monospace;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 32px;
    --space-xl: 64px;
    --space-xxl: 120px;
    --radius-sm: 8px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --transition: 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background-color: var(--bg-dark);
    color: var(--text-primary);
    font-family: var(--font-body);
    line-height: 1.6;
    overflow-x: hidden;
    position: relative;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.02em;
  }

  a { text-decoration: none; color: inherit; }
  ul { list-style: none; }
  button { font-family: inherit; cursor: pointer; border: none; outline: none; }

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
    filter: blur(80px);
    opacity: 0.6;
  }
  .orb-1 { top: -10%; left: -10%; width: 50vw; height: 50vw; background: var(--glow-deep); animation: float 20s ease-in-out infinite; }
  .orb-2 { bottom: -10%; right: -10%; width: 60vw; height: 60vw; background: var(--glow-nautical); animation: float 25s ease-in-out infinite reverse; }
  .orb-3 { top: 40%; left: 60%; width: 40vw; height: 40vw; background: var(--glow-magenta); animation: float 22s ease-in-out infinite; }

  @keyframes float {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(5%, -5%) scale(1.05); }
    66% { transform: translate(-5%, 5%) scale(0.95); }
  }

  .container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 var(--space-lg);
  }

  .glass-panel {
    background: var(--glass-bg);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    box-shadow: 0 8px 32px 0 rgba(0,0,0,0.3), inset 0 1px 0px rgba(255,255,255,0.05);
    transition: transform var(--transition), box-shadow var(--transition);
  }

  .glass-panel:hover {
    box-shadow: 0 12px 48px 0 rgba(0,0,0,0.5), inset 0 1px 0px rgba(255,255,255,0.1), 0 0 20px var(--accent-soft);
  }

  /* 1. Floating Glass Navbar */
  .navbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 100px;
    display: flex;
    align-items: center;
    z-index: 1000;
    transition: height var(--transition), background var(--transition), border-bottom var(--transition);
  }
  .navbar.scrolled {
    height: 70px;
    background: rgba(10, 14, 25, 0.7);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--glass-border);
  }
  .nav-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 var(--space-lg);
  }
  .brand {
    font-size: 1.5rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .brand-icon {
    width: 24px;
    height: 24px;
    background: conic-gradient(from 180deg, var(--accent), var(--text-primary));
    border-radius: 50%;
    box-shadow: 0 0 15px var(--accent);
  }
  .nav-links {
    display: flex;
    gap: var(--space-lg);
  }
  .nav-links a {
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-muted);
    transition: color var(--transition);
    position: relative;
    padding: 8px 0;
  }
  .nav-links a::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 100%; height: 2px;
    background: var(--accent);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform var(--transition);
  }
  .nav-links a:hover, .nav-links a.active {
    color: var(--text-primary);
  }
  .nav-links a:hover::after, .nav-links a.active::after {
    transform: scaleX(1);
  }
  .status-indicator {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.75rem;
    font-family: var(--font-mono);
    color: var(--text-primary);
    background: rgba(255,255,255,0.05);
    padding: 6px 12px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--glass-border);
  }
  .dot {
    width: 8px; height: 8px;
    background: var(--accent);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--accent);
    animation: blink 2s infinite;
  }
  @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
  .btn-primary {
    background: rgba(255,255,255,0.1);
    color: var(--text-primary);
    padding: 12px 24px;
    border-radius: var(--radius-md);
    font-size: 0.875rem;
    font-weight: 600;
    border: 1px solid transparent;
    background-clip: padding-box;
    position: relative;
    overflow: hidden;
    transition: transform 0.1s, box-shadow var(--transition);
  }
  .btn-primary::before {
    content: '';
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    z-index: -1;
    margin: -1px;
    border-radius: inherit;
    background: conic-gradient(from 90deg, var(--accent), var(--text-primary), var(--accent));
  }
  .btn-primary:hover {
    box-shadow: 0 0 20px var(--accent-soft);
  }
  .btn-primary:active {
    transform: scale(0.98);
  }
  .btn-secondary {
    background: transparent;
    color: var(--text-primary);
    padding: 12px 24px;
    border-radius: var(--radius-md);
    font-size: 0.875rem;
    font-weight: 600;
    border: 1px solid var(--glass-border);
    transition: background var(--transition);
  }
  .btn-secondary:hover {
    background: rgba(255,255,255,0.05);
  }

  /* Scroll Reveal Defaults */
  .reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .reveal.active {
    opacity: 1;
    transform: translateY(0);
  }

  /* 2. Hero Section */
  .hero {
    min-height: 100vh;
    padding-top: 150px;
    display: flex;
    align-items: center;
  }
  .hero-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-xl);
    align-items: center;
  }
  .hero-content h1 {
    font-size: clamp(3rem, 5vw, 5rem);
    margin-bottom: var(--space-md);
    background: linear-gradient(135deg, #fff, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .hero-content p {
    font-size: 1.25rem;
    color: var(--text-muted);
    margin-bottom: var(--space-lg);
    max-width: 500px;
  }
  .hero-actions {
    display: flex;
    gap: var(--space-md);
  }
  .hero-tableau {
    position: relative;
    height: 600px;
    perspective: 1000px;
  }
  .tableau-card {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%) rotateY(-15deg) rotateX(5deg);
    width: 100%; height: 100%;
    padding: var(--space-lg);
    display: flex;
    flex-direction: column;
    gap: var(--space-md);
    transform-style: preserve-3d;
  }
  .tableau-header {
    display: flex;
    justify-content: space-between;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--accent);
    border-bottom: 1px solid var(--glass-border);
    padding-bottom: 8px;
  }
  .vessel-track {
    background: rgba(255,255,255,0.03);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-sm);
    padding: var(--space-md);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transform: translateZ(30px);
    transition: background 0.3s;
  }
  .vessel-track:hover {
    background: rgba(0, 238, 255, 0.05);
  }
  .v-title { font-weight: 600; font-size: 1rem; }
  .v-meta { font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted); }
  .v-status { color: var(--accent); font-size: 0.875rem; }

  /* 3. Partner Consortium Strip */
  .partners {
    padding: var(--space-xl) 0;
    border-top: 1px solid var(--glass-border);
    border-bottom: 1px solid var(--glass-border);
    background: rgba(10, 14, 25, 0.2);
  }
  .partner-title {
    text-align: center;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: var(--space-lg);
  }
  .partner-logos {
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    gap: var(--space-lg);
    opacity: 0.6;
  }
  .partner-logos h3 {
    font-size: 1.5rem;
    color: var(--text-muted);
    transition: color var(--transition), transform var(--transition);
    cursor: default;
  }
  .partner-logos h3:hover {
    color: var(--text-primary);
    transform: scale(1.05);
  }

  /* 4. The Command Nexus (Features) */
  .section-intro {
    text-align: center;
    margin-bottom: var(--space-xl);
  }
  .section-intro .eyebrow {
    font-family: var(--font-mono);
    color: var(--accent);
    font-size: 0.875rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: var(--space-sm);
  }
  .section-intro h2 {
    font-size: clamp(2rem, 3vw, 3rem);
  }
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--space-lg);
    padding: var(--space-xxl) 0;
  }
  .feature-card {
    padding: var(--space-lg);
    position: relative;
    overflow: hidden;
  }
  .feature-card::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle, var(--accent-soft) 0%, transparent 60%);
    opacity: 0;
    transition: opacity var(--transition);
    pointer-events: none;
    z-index: 0;
  }
  .feature-card:hover::before { opacity: 1; }
  .feature-card:hover { border-color: var(--accent); }
  .f-icon {
    font-size: 2rem;
    margin-bottom: var(--space-md);
    position: relative; z-index: 1;
  }
  .f-title {
    font-size: 1.25rem;
    margin-bottom: var(--space-sm);
    position: relative; z-index: 1;
  }
  .f-desc {
    color: var(--text-muted);
    font-size: 0.875rem;
    position: relative; z-index: 1;
  }

  /* 5. Interactive Operations Terminal */
  .operations-section {
    padding: var(--space-xxl) 0;
  }
  .terminal-wrapper {
    display: flex;
    flex-direction: column;
    height: 500px;
  }
  .terminal-tabs {
    display: flex;
    border-bottom: 1px solid var(--glass-border);
    padding: 0 var(--space-lg);
    background: rgba(255,255,255,0.02);
  }
  .tab-btn {
    padding: var(--space-md) var(--space-lg);
    background: transparent;
    color: var(--text-muted);
    font-size: 1rem;
    font-weight: 500;
    position: relative;
    transition: color var(--transition);
  }
  .tab-btn.active {
    color: var(--text-primary);
  }
  .tab-btn::after {
    content: '';
    position: absolute;
    bottom: -1px; left: 0; width: 100%; height: 2px;
    background: var(--accent);
    transform: scaleX(0);
    transition: transform var(--transition);
  }
  .tab-btn.active::after {
    transform: scaleX(1);
    box-shadow: 0 0 10px var(--accent);
  }
  .terminal-content {
    flex: 1;
    padding: var(--space-xl);
    position: relative;
  }
  .tab-pane {
    position: absolute;
    top: var(--space-xl); left: var(--space-xl); right: var(--space-xl);
    opacity: 0; pointer-events: none;
    transition: opacity 0.4s ease;
  }
  .tab-pane.active {
    opacity: 1; pointer-events: auto;
  }
  .pane-data-row {
    display: grid;
    grid-template-columns: 100px 1fr 150px;
    gap: var(--space-md);
    padding: var(--space-md) 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-family: var(--font-mono);
  }
  .pane-time { color: var(--accent); }
  .pane-details strong { display: block; font-family: var(--font-body); font-size: 1.125rem; font-weight: 600; color: #fff;}
  .pane-details span { color: var(--text-muted); font-size: 0.875rem; }
  .pane-status { text-align: right; font-size: 0.875rem; }

  /* 6. Live Telemetry */
  .telemetry {
    padding: var(--space-xxl) 0;
    position: relative;
  }
  .telemetry::after {
    content: '';
    position: absolute;
    top: 50%; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    transform: translateY(-50%);
    opacity: 0.3;
    z-index: -1;
  }
  .metrics-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-lg);
    background: rgba(10,14,25,0.8);
    padding: var(--space-xl);
    border-radius: var(--radius-lg);
    border: 1px solid var(--glass-border);
  }
  .metric {
    text-align: center;
  }
  .metric-val {
    font-size: 3.5rem;
    font-weight: 800;
    font-family: var(--font-mono);
    color: #fff;
    text-shadow: 0 0 15px var(--accent-soft);
    margin-bottom: 8px;
  }
  .metric-label {
    font-size: 0.875rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  /* 7. Nautical Journey Timeline */
  .timeline-section {
    padding: var(--space-xxl) 0;
  }
  .timeline {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    padding-left: 40px;
  }
  .timeline::before {
    content: '';
    position: absolute;
    top: 0; bottom: 0; left: 19px;
    width: 2px;
    background: var(--glass-border);
  }
  .timeline-item {
    position: relative;
    margin-bottom: var(--space-xl);
  }
  .timeline-dot {
    position: absolute;
    left: -44px; top: 0;
    width: 20px; height: 20px;
    background: var(--bg-dark);
    border: 2px solid var(--accent);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--accent);
  }
  .timeline-content h3 {
    font-size: 1.5rem;
    margin-bottom: 8px;
  }
  .timeline-content p {
    color: var(--text-muted);
  }

  /* 8. Comparison Slider */
  .comparison {
    padding: var(--space-xxl) 0;
  }
  .comp-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: var(--radius-lg);
    overflow: hidden;
    border: 1px solid var(--glass-border);
  }
  .comp-panel {
    padding: var(--space-xl);
    position: relative;
    cursor: pointer;
    transition: background var(--transition);
  }
  .comp-legacy {
    background: rgba(20, 20, 20, 0.9);
    color: #888;
    border-right: 1px solid var(--glass-border);
  }
  .comp-legacy:hover { background: rgba(30, 30, 30, 0.9); }
  .comp-h9 {
    background: rgba(10, 14, 25, 0.9);
    position: relative;
    overflow: hidden;
  }
  .comp-h9::before {
    content: ''; position: absolute; inset:0;
    background: radial-gradient(circle at 50% 50%, var(--accent-soft), transparent 70%);
    opacity: 0.5;
  }
  .comp-panel h3 { font-size: 1.5rem; margin-bottom: var(--space-md); }
  .comp-panel p { font-size: 1rem; position: relative; z-index: 1;}

  /* 9. Global Fleet Radar */
  .radar-section { padding: var(--space-xxl) 0; overflow: hidden; }
  .radar-display {
    width: 600px; height: 600px;
    margin: 0 auto;
    position: relative;
    border-radius: 50%;
    border: 1px dashed rgba(0, 238, 255, 0.2);
    display: flex; align-items: center; justify-content: center;
  }
  .radar-display::before {
    content: ''; position: absolute; inset: 20%; border: 1px dashed rgba(0, 238, 255, 0.15); border-radius: 50%;
  }
  .radar-display::after {
    content: ''; position: absolute; inset: 40%; border: 1px dashed rgba(0, 238, 255, 0.1); border-radius: 50%;
  }
  .sweep {
    position: absolute; inset: 0; border-radius: 50%;
    background: conic-gradient(from 0deg, transparent 70%, rgba(0, 238, 255, 0.3) 100%);
    animation: rotate 4s linear infinite;
  }
  @keyframes rotate { 100% { transform: rotate(360deg); } }
  .blip {
    position: absolute;
    width: 12px; height: 12px;
    background: var(--accent);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--accent);
    cursor: pointer;
  }
  .blip-1 { top: 30%; left: 40%; animation: blink 2s infinite; }
  .blip-2 { top: 60%; left: 70%; animation: blink 2.5s infinite; }
  .blip-tooltip {
    position: absolute;
    top: 20px; left: 20px;
    width: max-content;
    padding: 8px 12px;
    font-size: 0.75rem;
    font-family: var(--font-mono);
    pointer-events: none;
    opacity: 0;
    transition: opacity var(--transition);
    z-index: 10;
  }
  .blip:hover .blip-tooltip { opacity: 1; }

  /* 10. Member Spotlight */
  .spotlight { padding: var(--space-xxl) 0; }
  .quote-card {
    padding: var(--space-xl);
    text-align: center;
    position: relative;
  }
  .quote-mark { font-size: 6rem; color: var(--accent-soft); position: absolute; top: 10px; left: 40px; font-family: serif;}
  .quote-text { font-size: 1.75rem; font-style: italic; line-height: 1.4; margin-bottom: var(--space-lg); position: relative; z-index: 1;}
  .quote-auth { font-weight: 600; font-size: 1rem; }
  .quote-role { color: var(--text-muted); font-size: 0.875rem; }

  /* 11. Security */
  .security { padding: var(--space-xxl) 0; text-align: center; }
  .sec-icon { font-size: 3rem; color: var(--accent); margin-bottom: var(--space-md); }
  .security p { max-width: 600px; margin: 0 auto var(--space-lg); color: var(--text-muted);}

  /* 12. FAQ Accordion */
  .faq { padding: var(--space-xxl) 0; }
  .faq-list { max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: var(--space-md); }
  .faq-item {
    border-bottom: 1px solid var(--glass-border);
    overflow: hidden;
  }
  .faq-q {
    width: 100%;
    text-align: left;
    padding: var(--space-md) 0;
    background: transparent;
    color: var(--text-primary);
    font-size: 1.125rem;
    font-weight: 600;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .faq-icon {
    transition: transform var(--transition);
    color: var(--accent);
  }
  .faq-item.active .faq-icon { transform: rotate(45deg); }
  .faq-a {
    display: grid;
    grid-template-rows: 0fr;
    transition: grid-template-rows var(--transition);
  }
  .faq-a-inner { overflow: hidden; color: var(--text-muted); padding-bottom: 0; transition: padding var(--transition); }
  .faq-item.active .faq-a { grid-template-rows: 1fr; }
  .faq-item.active .faq-a-inner { padding-bottom: var(--space-md); }

  /* 13. Form CTA */
  .cta-section { padding: var(--space-xxl) 0; }
  .cta-box {
    padding: var(--space-xl);
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
  }
  .cta-form {
    display: flex; flex-direction: column; gap: var(--space-md); margin-top: var(--space-lg);
  }
  .form-group { position: relative; }
  input, textarea {
    width: 100%;
    background: rgba(0,0,0,0.2);
    border: 1px solid var(--glass-border);
    padding: 16px;
    border-radius: var(--radius-sm);
    color: #fff;
    font-family: inherit;
    font-size: 1rem;
    transition: border-color var(--transition), box-shadow var(--transition);
  }
  input:focus, textarea:focus {
    border-color: var(--accent);
    box-shadow: 0 0 15px var(--accent-soft);
    outline: none;
  }

  /* 14. Footer */
  .footer {
    border-top: 1px solid var(--glass-border);
    padding: var(--space-xl) 0;
    margin-top: var(--space-xxl);
    background: #020304;
  }
  .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: var(--space-lg); }
  .f-about p { color: var(--text-muted); font-size: 0.875rem; margin-top: var(--space-md); max-width: 300px;}
  .f-links h4 { margin-bottom: var(--space-md); }
  .f-links ul { display: flex; flex-direction: column; gap: 8px; }
  .f-links a { color: var(--text-muted); font-size: 0.875rem; transition: color var(--transition); }
  .f-links a:hover { color: var(--accent); }
  .f-bottom {
    margin-top: var(--space-xl);
    text-align: center;
    font-size: 0.75rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }

  /* Modal */
  .modal-overlay {
    position: fixed; inset: 0;
    background: rgba(0,0,0,0.8);
    backdrop-filter: blur(10px);
    z-index: 9999;
    display: flex; align-items: center; justify-content: center;
    opacity: 0; pointer-events: none;
    transition: opacity var(--transition);
  }
  .modal-overlay.active { opacity: 1; pointer-events: auto; }
  .modal-content {
    background: var(--bg-surface);
    padding: var(--space-xl);
    width: 100%; max-width: 500px;
    transform: scale(0.9);
    transition: transform var(--transition);
    position: relative;
  }
  .modal-overlay.active .modal-content { transform: scale(1); }
  .close-modal { position: absolute; top: 16px; right: 16px; background: transparent; color: #fff; font-size: 1.5rem; }

  /* Toast */
  .toast {
    position: fixed;
    bottom: 30px; right: 30px;
    background: rgba(0, 238, 255, 0.1);
    border: 1px solid var(--accent);
    padding: 16px 24px;
    border-radius: var(--radius-sm);
    box-shadow: 0 0 20px rgba(0,238,255,0.2);
    transform: translateX(120%);
    transition: transform var(--transition);
    z-index: 10000;
    display: flex; align-items: center; gap: 12px;
  }
  .toast.active { transform: translateX(0); }
</style>
</head>
<body>

<div class="ambient-orbs">
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>
</div>

<nav class="navbar" id="navbar">
  <div class="nav-container">
    <div class="brand">
      <div class="brand-icon"></div>
      Harbor Nine
    </div>
    <ul class="nav-links">
      <li><a href="#features">Capabilities</a></li>
      <li><a href="#operations">Terminal</a></li>
      <li><a href="#radar">Fleet</a></li>
    </ul>
    <div style="display: flex; align-items: center; gap: 24px;">
      <div class="status-indicator">
        <div class="dot"></div>
        SYSTEM OPERATIONAL
      </div>
      <button class="btn-primary open-modal-btn">Initiate Demo</button>
    </div>
  </div>
</nav>

<section class="hero container reveal">
  <div class="hero-grid">
    <div class="hero-content">
      <h1>Orchestrate the Unforgettable.</h1>
      <p>Harbor Nine is the absolute waterfront mobility and coastal operations system for the world's most distinguished superyacht marinas and elite coastal resorts.</p>
      <div class="hero-actions">
        <button class="btn-primary open-modal-btn">Initiate Vessel Integration</button>
        <button class="btn-secondary">View Telemetry</button>
      </div>
    </div>
    <div class="hero-tableau glass-panel">
      <div class="tableau-card glass-panel">
        <div class="tableau-header">
          <span>LIVE DISPATCH</span>
          <span>14:02:45 UTC</span>
        </div>
        <div class="vessel-track">
          <div>
            <div class="v-title">M/Y Aurelia</div>
            <div class="v-meta">Tender Approach • 3nm</div>
          </div>
          <div class="v-status">INBOUND</div>
        </div>
        <div class="vessel-track">
          <div>
            <div class="v-title">S/Y Serene</div>
            <div class="v-meta">Berth 4A • 400A Pwr</div>
          </div>
          <div class="v-status">SECURED</div>
        </div>
        <div class="vessel-track">
          <div>
            <div class="v-title">P/Y Eclipse</div>
            <div class="v-meta">Heli-Transfer • VIP</div>
          </div>
          <div class="v-status">AIRBORNE</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="partners reveal">
  <div class="container">
    <div class="partner-title">Trusted by Elite Coastal Destinations</div>
    <div class="partner-logos">
      <h3>AURA MARINA</h3>
      <h3>THE PENINSULA CLUB</h3>
      <h3>VANGUARD RESORTS</h3>
      <h3>OCEANIS ESTATES</h3>
    </div>
  </div>
</section>

<section id="features" class="container reveal">
  <div class="section-intro">
    <div class="eyebrow">Core Systems</div>
    <h2>The Command Nexus</h2>
  </div>
  <div class="features-grid stagger-parent">
    <div class="feature-card glass-panel stagger-child">
      <div class="f-icon">⚓</div>
      <h3 class="f-title">Dynamic Mooring Allocation</h3>
      <p class="f-desc">Algorithmic slip assignment based on vessel LOA, draft, power requirements, and owner preferences. Eliminate dockside bottlenecks.</p>
    </div>
    <div class="feature-card glass-panel stagger-child">
      <div class="f-icon">👥</div>
      <h3 class="f-title">Autonomous Crew Manifests</h3>
      <p class="f-desc">Synchronized digital tracking for shore leave, provisioning runs, and dedicated transport logic. Keep crew movements silent and invisible to guests.</p>
    </div>
    <div class="feature-card glass-panel stagger-child">
      <div class="f-icon">🚁</div>
      <h3 class="f-title">VVIP Guest Synchronization</h3>
      <p class="f-desc">Seamlessly link private aviation arrivals with tender dispatch and suite readiness. Predictive ETA guarantees perfect timing.</p>
    </div>
    <div class="feature-card glass-panel stagger-child">
      <div class="f-icon">🚤</div>
      <h3 class="f-title">Bespoke Tender Dispatch</h3>
      <p class="f-desc">Uber-like routing but designed for multi-million dollar watercraft. Track locations, manage fuel, and optimize routes instantly.</p>
    </div>
  </div>
</section>

<section id="operations" class="operations-section container reveal">
  <div class="section-intro">
    <div class="eyebrow">Live Interface</div>
    <h2>Interactive Operations Terminal</h2>
  </div>
  <div class="terminal-wrapper glass-panel">
    <div class="terminal-tabs">
      <button class="tab-btn active" data-tab="tab-1">Dockside Arrivals</button>
      <button class="tab-btn" data-tab="tab-2">Crew Logistics</button>
      <button class="tab-btn" data-tab="tab-3">VVIP Requests</button>
    </div>
    <div class="terminal-content">
      <div class="tab-pane active" id="tab-1">
        <div class="pane-data-row">
          <div class="pane-time">14:00</div>
          <div class="pane-details">
            <strong>S/Y Serene (82m)</strong>
            <span>Berth 4A • 400A Power • Fresh Water • Line Handlers Required</span>
          </div>
          <div class="pane-status" style="color:var(--accent)">CONFIRMED</div>
        </div>
        <div class="pane-data-row">
          <div class="pane-time">15:30</div>
          <div class="pane-details">
            <strong>M/Y Oceanus (45m)</strong>
            <span>Fuel Dock • 5000L Diesel • Waste Pump Out</span>
          </div>
          <div class="pane-status" style="color:#d400ff">APPROACHING</div>
        </div>
      </div>
      <div class="tab-pane" id="tab-2">
        <div class="pane-data-row">
          <div class="pane-time">14:30</div>
          <div class="pane-details">
            <strong>M/Y Aurelia Crew Transport</strong>
            <span>12 Pax • 2 Luxury Vans Dispatched to Terminal C • Wait time: 3m</span>
          </div>
          <div class="pane-status" style="color:var(--accent)">EN ROUTE</div>
        </div>
      </div>
      <div class="tab-pane" id="tab-3">
        <div class="pane-data-row">
          <div class="pane-time">15:00</div>
          <div class="pane-details">
            <strong>Owner of P/Y Eclipse</strong>
            <span>Heli-transfer to private estate. Chilled Dom Perignon on arrival.</span>
          </div>
          <div class="pane-status" style="color:var(--accent)">COORDINATED</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="telemetry container reveal">
  <div class="metrics-grid">
    <div class="metric">
      <div class="metric-val count-up" data-target="14">0</div>
      <div class="metric-label">Nautical Miles (M)</div>
    </div>
    <div class="metric">
      <div class="metric-val count-up" data-target="99.9" data-decimals="1">0</div>
      <div class="metric-label">Mooring Efficiency %</div>
    </div>
    <div class="metric">
      <div class="metric-val count-up" data-target="2" data-prefix="$" data-suffix="B+">0</div>
      <div class="metric-label">Managed Assets</div>
    </div>
    <div class="metric">
      <div class="metric-val count-up" data-target="120">0</div>
      <div class="metric-label">Partner Marinas</div>
    </div>
  </div>
</section>

<section class="timeline-section container reveal">
  <div class="section-intro">
    <div class="eyebrow">Perfect Sequence</div>
    <h2>Nautical Journey Timeline</h2>
  </div>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content glass-panel" style="padding: 24px;">
        <h3>1. Airborne Telemetry</h3>
        <p>Guest touches down at the private airstrip. Flight data automatically pings the Harbor Nine system, adjusting ETA down to the second.</p>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content glass-panel" style="padding: 24px;">
        <h3>2. Silent Dispatch</h3>
        <p>A flagship tender is dispatched seamlessly to the waterfront terminal. Chauffeurs are notified without radio chatter.</p>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content glass-panel" style="padding: 24px;">
        <h3>3. Environmental Prep</h3>
        <p>Suite or stateroom temperature coordinates automatically with the arrival window. Lighting adjusts to evening settings.</p>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content glass-panel" style="padding: 24px;">
        <h3>4. Embarkation</h3>
        <p>Yacht readied with requested provisions. Guests step aboard flawlessly. Zero friction. Total command.</p>
      </div>
    </div>
  </div>
</section>

<section class="comparison container reveal">
  <div class="section-intro">
    <div class="eyebrow">The Evolution</div>
    <h2>Legacy vs. Harbor Nine</h2>
  </div>
  <div class="comp-wrapper">
    <div class="comp-panel comp-legacy">
      <h3>The Old Method</h3>
      <p>Radio static. Whiteboard schedules. Lost VHF calls. Missed ETA windows. Fragmented guest experiences and high crew stress.</p>
    </div>
    <div class="comp-panel comp-h9">
      <h3>Harbor Nine Orchestration</h3>
      <p>Synchronized telematics. Silent, instant terminal updates. Predictive shoreside readiness. Perfected arrival orchestration with luminous precision.</p>
    </div>
  </div>
</section>

<section id="radar" class="radar-section container reveal">
  <div class="section-intro">
    <div class="eyebrow">Macro View</div>
    <h2>Global Fleet Radar</h2>
  </div>
  <div class="radar-display">
    <div class="sweep"></div>
    <div class="blip blip-1">
      <div class="blip-tooltip glass-panel">M/Y Aurelia - 12kts</div>
    </div>
    <div class="blip blip-2">
      <div class="blip-tooltip glass-panel">S/Y Serene - Moored</div>
    </div>
  </div>
</section>

<section class="spotlight container reveal">
  <div class="quote-card glass-panel">
    <div class="quote-mark">"</div>
    <p class="quote-text">Before Harbor Nine, managing fifty superyacht arrivals felt like directing traffic in a storm. Now, it operates with the silent precision of a Swiss watch. It is fundamentally transformative.</p>
    <div class="quote-auth">Captain Elias Thorne</div>
    <div class="quote-role">Director of Maritime Operations, Vanguard Resorts</div>
  </div>
</section>

<section class="security container reveal">
  <div class="sec-icon">🔒</div>
  <h2>Absolute Protocol</h2>
  <p>VVIP data dictates military-grade encryption. Harbor Nine ensures that itineraries, fleet positions, and guest manifests are locked within an impregnable private network.</p>
</section>

<section class="faq container reveal">
  <div class="section-intro">
    <div class="eyebrow">Knowledge Base</div>
    <h2>System Queries</h2>
  </div>
  <div class="faq-list">
    <div class="faq-item glass-panel">
      <button class="faq-q">Can it integrate with our existing Property Management System? <span class="faq-icon">+</span></button>
      <div class="faq-a"><div class="faq-a-inner"><br>Yes. Harbor Nine connects via secure API hooks directly into major PMS platforms like Oracle Opera, synchronizing guest profiles with maritime operations seamlessly.</div></div>
    </div>
    <div class="faq-item glass-panel">
      <button class="faq-q">How does Shore Power tracking work? <span class="faq-icon">+</span></button>
      <div class="faq-a"><div class="faq-a-inner"><br>Smart pedestals report telemetry directly to the Harbor Nine terminal, automating billing and alerting engineers before a fault impacts the vessel.</div></div>
    </div>
    <div class="faq-item glass-panel">
      <button class="faq-q">Is the tender tracking hardware independent? <span class="faq-icon">+</span></button>
      <div class="faq-a"><div class="faq-a-inner"><br>We integrate with existing AIS transponders or provide discrete, battery-independent IoT beacons tailored for open water performance.</div></div>
    </div>
    <div class="faq-item glass-panel">
      <button class="faq-q">What is the training timeline for dockmasters? <span class="faq-icon">+</span></button>
      <div class="faq-a"><div class="faq-a-inner"><br>Our UI utilizes universal affordances. Competency is typically achieved in 4 hours, with mastery inside a 3-day operational cycle.</div></div>
    </div>
  </div>
</section>

<section class="cta-section container reveal">
  <div class="cta-box glass-panel">
    <h2>Initiate Integration</h2>
    <p style="color:var(--text-muted); margin-top:16px;">Request a private demonstration of the Harbor Nine command architecture.</p>
    <form class="cta-form" id="intake-form">
      <div class="form-group">
        <input type="text" placeholder="Marina or Resort Name" required>
      </div>
      <div class="form-group">
        <input type="email" placeholder="Official Email Dispatch" required>
      </div>
      <button type="submit" class="btn-primary" style="width:100%; margin-top:8px;">Request Protocol Demo</button>
    </form>
  </div>
</section>

<footer class="footer">
  <div class="container footer-grid">
    <div class="f-about">
      <div class="brand">
        <div class="brand-icon"></div> Harbor Nine
      </div>
      <p>The definitive waterfront mobility operating system for the world's elite coastal destinations.</p>
    </div>
    <div class="f-links">
      <h4>Platform</h4>
      <ul>
        <li><a href="#">Command Nexus</a></li>
        <li><a href="#">Telemetry</a></li>
        <li><a href="#">Security Protocol</a></li>
      </ul>
    </div>
    <div class="f-links">
      <h4>Company</h4>
      <ul>
        <li><a href="#">About</a></li>
        <li><a href="#">Careers</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </div>
  </div>
  <div class="container f-bottom">
    &copy; 2026 Harbor Nine Systems. All rights reserved. Maritime encryption active.
  </div>
</footer>

<!-- Modals & Toasts -->
<div class="modal-overlay" id="demo-modal">
  <div class="modal-content glass-panel">
    <button class="close-modal" id="close-modal">&times;</button>
    <h3>Private Demo Allocation</h3>
    <p style="color:var(--text-muted); margin-top:8px; margin-bottom: 24px;">Enter your credentials and our integration team will contact you within 20 minutes.</p>
    <form class="cta-form" id="modal-form">
      <div class="form-group"><input type="text" placeholder="Commander Name" required></div>
      <div class="form-group"><input type="email" placeholder="Secure Email" required></div>
      <button type="submit" class="btn-primary" style="width:100%;">Confirm Slot</button>
    </form>
  </div>
</div>

<div class="toast" id="success-toast">
  <div style="font-size:1.5rem;">✓</div>
  <div>
    <strong style="color:#fff;">Transmission Secured</strong><br>
    <span style="font-size:0.875rem; color:var(--text-muted);">Our team has received your request.</span>
  </div>
</div>

<script>
  // 1. Navbar Scroll Transition
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
  });

  // 2. Scroll Reveal & Stagger Animation
  const revealElements = document.querySelectorAll('.reveal');
  const staggerParents = document.querySelectorAll('.stagger-parent');
  
  const revealObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Handle stagger logic if applicable
        if (entry.target.classList.contains('stagger-parent')) {
          const children = entry.target.querySelectorAll('.stagger-child');
          children.forEach((child, index) => {
            child.style.transitionDelay = `${index * 0.15}s`;
            child.style.opacity = '1';
            child.style.transform = 'translateY(0)';
          });
        }
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  revealElements.forEach(el => revealObserver.observe(el));
  
  // Custom init for stagger children
  document.querySelectorAll('.stagger-child').forEach(child => {
    child.style.opacity = '0';
    child.style.transform = 'translateY(30px)';
    child.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  });

  // 3. Terminal Tabs
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      tabPanes.forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(btn.dataset.tab).classList.add('active');
    });
  });

  // 4. FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const q = item.querySelector('.faq-q');
    q.addEventListener('click', () => {
      item.classList.toggle('active');
    });
  });

  // 5. Modal
  const modal = document.getElementById('demo-modal');
  const openModalBtns = document.querySelectorAll('.open-modal-btn');
  const closeModalBtn = document.getElementById('close-modal');

  openModalBtns.forEach(btn => {
    btn.addEventListener('click', () => modal.classList.add('active'));
  });
  closeModalBtn.addEventListener('click', () => modal.classList.remove('active'));
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') modal.classList.remove('active');
  });

  // 6. Toast & Form handling
  const forms = [document.getElementById('intake-form'), document.getElementById('modal-form')];
  const toast = document.getElementById('success-toast');
  
  forms.forEach(form => {
    if(form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        modal.classList.remove('active'); // Close modal if open
        toast.classList.add('active');
        form.reset();
        setTimeout(() => toast.classList.remove('active'), 4000);
      });
    }
  });

  // 7. Count-up metrics
  const counters = document.querySelectorAll('.count-up');
  const countUpObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        animateValue(entry.target);
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(c => countUpObserver.observe(c));

  function animateValue(obj) {
    const target = parseFloat(obj.getAttribute('data-target'));
    const decimals = parseInt(obj.getAttribute('data-decimals') || 0);
    const prefix = obj.getAttribute('data-prefix') || '';
    const suffix = obj.getAttribute('data-suffix') || '';
    const duration = 2000;
    const start = 0;
    let startTimestamp = null;

    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      // easeOutExpo
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      const current = (easeProgress * (target - start) + start).toFixed(decimals);
      obj.innerHTML = prefix + current + suffix;
      if (progress < 1) {
        window.requestAnimationFrame(step);
      }
    };
    window.requestAnimationFrame(step);
  }

  // Mouse Glow tracking on feature cards
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
</script>
</body>
</html>
"""

os.makedirs('fdu_018/src', exist_ok=True)
with open("fdu_018/src/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
