import os

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Helio Harbor | Coastal Mobility Terminal</title>
<style>
/* ==========================================================================
   CSS TOKENS & RESET
   ========================================================================== */
:root {
  /* Colors */
  --void-black: #0B0C10;
  --deep-indigo: #121420;
  --orb-teal: rgba(0, 255, 238, 0.4);
  --orb-magenta: rgba(255, 0, 170, 0.35);
  --orb-gold: rgba(255, 215, 0, 0.25);
  --sun-gold: #FFD700;
  --hyper-magenta: #FF00AA;
  --electric-teal: #00FFEE;
  --electric-cyan: #00E5FF;
  
  /* Glass Surfaces */
  --glass-surface: rgba(255, 255, 255, 0.03);
  --glass-surface-hover: rgba(255, 255, 255, 0.08);
  --glass-border: rgba(255, 255, 255, 0.1);
  --glass-border-highlight: rgba(255, 255, 255, 0.25);
  
  /* Typography */
  --pure-white: #FFFFFF;
  --silver-haze: #B0B5C0;
  --muted-glass: #767B88;
  
  /* Semantic */
  --open-cyan: #00E5FF;
  --closed-red: #FF3366;
  --waitlist-yellow: #FFD700;
  
  /* Radii */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-xl: 32px;
  --radius-pill: 9999px;
  
  /* Shadows & Blurs */
  --shadow-glow: 0 8px 32px rgba(0, 0, 0, 0.6);
  --shadow-neon: 0 0 15px rgba(0, 255, 238, 0.3);
  --blur-base: blur(24px);
  --blur-light: blur(12px);
  
  /* Typography Scale */
  --font-sans: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;
  --text-4xl: 3rem;
  --text-5xl: 4.5rem;
  --text-6xl: 6rem;
  
  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;
  --space-32: 8rem;
  
  /* Motion Constants */
  --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-slow: 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  
  /* Layout widths */
  --container-width: 1280px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--void-black);
  color: var(--pure-white);
  font-family: var(--font-sans);
  line-height: 1.6;
  overflow-x: hidden;
  position: relative;
  -webkit-font-smoothing: antialiased;
}

a {
  color: inherit;
  text-decoration: none;
}

ul {
  list-style: none;
}

button, input {
  font-family: inherit;
  border: none;
  background: none;
  outline: none;
}

button {
  cursor: pointer;
}

img, svg {
  display: block;
  max-width: 100%;
}

/* ==========================================================================
   AMBIENT ORBS & BACKGROUND
   ========================================================================== */
.ambient-bg {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
  opacity: 0.6;
  animation: float 20s infinite ease-in-out alternate;
  mix-blend-mode: screen;
}

.orb-1 {
  width: 600px;
  height: 600px;
  background: var(--orb-teal);
  top: -10%;
  left: -5%;
  animation-duration: 25s;
}

.orb-2 {
  width: 500px;
  height: 500px;
  background: var(--orb-magenta);
  bottom: 10%;
  right: -5%;
  animation-duration: 30s;
  animation-delay: -5s;
}

.orb-3 {
  width: 700px;
  height: 700px;
  background: var(--orb-gold);
  top: 40%;
  left: 30%;
  animation-duration: 28s;
  animation-delay: -12s;
  opacity: 0.4;
}

@keyframes float {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(50px, -50px) scale(1.1); }
  100% { transform: translate(-30px, 30px) scale(0.9); }
}

/* Mesh pattern overlay */
.ambient-bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: 
    radial-gradient(var(--glass-border) 1px, transparent 1px);
  background-size: 32px 32px;
  opacity: 0.15;
  pointer-events: none;
}

/* ==========================================================================
   COMMON GLASS & GRADIENT CLASSES
   ========================================================================== */
.container {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  position: relative;
  z-index: 10;
}

.glass-panel {
  background: var(--glass-surface);
  backdrop-filter: var(--blur-base);
  -webkit-backdrop-filter: var(--blur-base);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-glow);
  position: relative;
  overflow: hidden;
  transition: all var(--transition-base);
}

.glass-panel::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 50%, rgba(255,255,255,0.1) 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.glass-panel-hover:hover {
  background: var(--glass-surface-hover);
  border-color: var(--glass-border-highlight);
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,255,238,0.15);
}

.text-gradient {
  background: linear-gradient(to right, #fff, var(--electric-cyan));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}

.text-gradient-magenta {
  background: linear-gradient(to right, #fff, var(--hyper-magenta));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Conic Border Wrap */
.conic-border {
  position: relative;
  border-radius: var(--radius-lg);
  background: var(--glass-surface);
  backdrop-filter: var(--blur-base);
  z-index: 1;
}

.conic-border::before {
  content: "";
  position: absolute;
  z-index: -1;
  inset: -1px;
  border-radius: inherit;
  background: conic-gradient(
    from var(--conic-angle, 0deg), 
    rgba(255,255,255,0.1) 0%, 
    var(--electric-teal) 25%, 
    rgba(255,255,255,0.1) 50%, 
    var(--hyper-magenta) 75%, 
    rgba(255,255,255,0.1) 100%
  );
  animation: conicSpin 10s linear infinite;
  opacity: 0.5;
  transition: opacity var(--transition-base);
}

.conic-border:hover::before {
  opacity: 1;
}

@property --conic-angle {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}

@keyframes conicSpin {
  0% { --conic-angle: 0deg; }
  100% { --conic-angle: 360deg; }
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4) var(--space-8);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: var(--text-sm);
  border-radius: var(--radius-pill);
  transition: all var(--transition-fast);
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background: var(--pure-white);
  color: var(--void-black);
}

.btn-primary:hover {
  background: var(--electric-cyan);
  box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
  transform: scale(1.05);
}

.btn-glass {
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  color: var(--pure-white);
  backdrop-filter: var(--blur-light);
}

.btn-glass:hover {
  background: var(--glass-surface-hover);
  border-color: var(--pure-white);
  transform: scale(1.05);
}

/* ==========================================================================
   BLOCK 1 & 2: SKIP LINK, MARQUEE & NAVBAR
   ========================================================================== */
.skip-link {
  position: absolute;
  top: -100px;
  left: 20px;
  z-index: 1000;
  background: var(--electric-teal);
  color: var(--void-black);
  padding: 10px 20px;
  border-radius: var(--radius-sm);
  font-weight: bold;
}
.skip-link:focus { top: 20px; }

.header-nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  background: rgba(11, 12, 16, 0.6);
  backdrop-filter: var(--blur-base);
  border-bottom: 1px solid var(--glass-border);
  padding: var(--space-4) 0;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand {
  font-size: var(--text-2xl);
  font-weight: 800;
  letter-spacing: -1px;
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.brand svg {
  width: 32px;
  height: 32px;
  fill: none;
  stroke: var(--electric-cyan);
  stroke-width: 2;
  stroke-linejoin: round;
}

.nav-links {
  display: flex;
  gap: var(--space-8);
}

.nav-links a {
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--silver-haze);
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: color var(--transition-fast);
}

.nav-links a:hover {
  color: var(--pure-white);
  text-shadow: 0 0 8px rgba(255,255,255,0.5);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.status-chip {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: var(--text-xs);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  background: rgba(0, 229, 255, 0.1);
  border: 1px solid rgba(0, 229, 255, 0.3);
  color: var(--electric-cyan);
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--electric-cyan);
  box-shadow: 0 0 8px var(--electric-cyan);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 1; box-shadow: 0 0 0 0 rgba(0, 229, 255, 0.4); }
  70% { opacity: 0.5; box-shadow: 0 0 0 6px rgba(0, 229, 255, 0); }
  100% { opacity: 1; box-shadow: 0 0 0 0 rgba(0, 229, 255, 0); }
}

/* ==========================================================================
   BLOCK 3: HERO HALO
   ========================================================================== */
.hero-sec {
  padding-top: var(--space-32);
  padding-bottom: var(--space-24);
  min-height: 100vh;
  display: flex;
  align-items: center;
}

.hero-content {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}

.hero-title {
  font-size: var(--text-6xl);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -2px;
  margin-bottom: var(--space-6);
  position: relative;
}

.hero-subtitle {
  font-size: var(--text-xl);
  color: var(--silver-haze);
  margin-bottom: var(--space-12);
  line-height: 1.8;
}

.hero-actions {
  display: flex;
  justify-content: center;
  gap: var(--space-6);
  margin-bottom: var(--space-24);
}

.hero-glass-visual {
  position: relative;
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  aspect-ratio: 16/7;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sun-tracker-svg {
  width: 100%;
  height: 100%;
  position: absolute;
  inset: 0;
  padding: var(--space-8);
}

.sun-path {
  fill: none;
  stroke: var(--glass-border-highlight);
  stroke-width: 1;
  stroke-dasharray: 4 8;
}

.sun-node {
  fill: var(--sun-gold);
  filter: drop-shadow(0 0 10px var(--sun-gold));
  animation: trackOrb 15s linear infinite;
  offset-path: path("M100,200 C300,50 700,50 900,200");
}

@keyframes trackOrb {
  0% { offset-distance: 0%; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { offset-distance: 100%; opacity: 0; }
}

/* ==========================================================================
   BLOCK 4: MARQUEE OPERATIONS STRIP
   ========================================================================== */
.ops-strip {
  width: 100%;
  overflow: hidden;
  background: var(--glass-surface);
  border-top: 1px solid var(--glass-border);
  border-bottom: 1px solid var(--glass-border);
  padding: var(--space-4) 0;
  backdrop-filter: var(--blur-light);
  position: relative;
  z-index: 5;
}

.ops-track {
  display: flex;
  white-space: nowrap;
  animation: marquee 30s linear infinite;
}

.ops-item {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: 0 var(--space-8);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--silver-haze);
  text-transform: uppercase;
  letter-spacing: 2px;
}

.ops-item span {
  color: var(--electric-cyan);
}

@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ==========================================================================
   BLOCK 5: HARBOR OVERVIEW 
   ========================================================================== */
.section {
  padding: var(--space-24) 0;
  position: relative;
  z-index: 10;
}

.sec-header {
  margin-bottom: var(--space-16);
  text-align: center;
}

.sec-label {
  display: inline-block;
  font-size: var(--text-xs);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--hyper-magenta);
  margin-bottom: var(--space-4);
}

.sec-title {
  font-size: var(--text-4xl);
  font-weight: 800;
  letter-spacing: -1px;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-8);
}

.overview-card {
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.card-icon {
  width: 48px;
  height: 48px;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--electric-cyan);
}

.card-icon svg {
  width: 24px;
  height: 24px;
  stroke: currentColor;
  fill: none;
  stroke-width: 1.5;
}

.overview-card h3 {
  font-size: var(--text-xl);
  font-weight: 700;
}

.overview-card p {
  color: var(--silver-haze);
  font-size: var(--text-sm);
}

/* ==========================================================================
   BLOCK 6: GLASS FLEET
   ========================================================================== */
.fleet-scroll {
  display: flex;
  gap: var(--space-8);
  overflow-x: auto;
  padding: var(--space-4) 0 var(--space-12);
  scrollbar-width: none;
}
.fleet-scroll::-webkit-scrollbar { display: none; }

.fleet-card {
  flex: 0 0 380px;
  height: 480px;
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
}

.fleet-card-img {
  flex: 1;
  border-radius: var(--radius-md);
  background: linear-gradient(180deg, transparent, rgba(0,0,0,0.4));
  margin-bottom: var(--space-6);
  position: relative;
  overflow: hidden;
  border: 1px solid var(--glass-border);
  display: flex;
  align-items: center;
  justify-content: center;
}

.blueprint-svg {
  width: 80%;
  height: 80%;
  stroke: var(--electric-teal);
  stroke-width: 1;
  fill: none;
  opacity: 0.6;
}

.fleet-meta {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.fleet-name {
  font-size: var(--text-2xl);
  font-weight: 800;
  margin-bottom: var(--space-2);
}

.fleet-specs {
  display: flex;
  gap: var(--space-4);
  font-family: monospace;
  font-size: var(--text-xs);
  color: var(--silver-haze);
  letter-spacing: 1px;
}

/* ==========================================================================
   BLOCK 7: TIDE & TRANSIT DESK (TABS)
   ========================================================================== */
.tide-desk {
  padding: var(--space-8);
  min-height: 500px;
}

.tabs-nav {
  display: flex;
  gap: var(--space-4);
  border-bottom: 1px solid var(--glass-border);
  margin-bottom: var(--space-8);
  padding-bottom: var(--space-4);
}

.tab-btn {
  font-size: var(--text-sm);
  color: var(--muted-glass);
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 600;
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-pill);
  transition: all var(--transition-fast);
}

.tab-btn.active {
  color: var(--pure-white);
  background: rgba(255,255,255,0.1);
  box-shadow: 0 0 15px rgba(255,255,255,0.05);
}

.tab-btn:hover:not(.active) {
  color: var(--silver-haze);
}

.tab-content {
  display: none;
  animation: fadeIn 0.4s ease;
}

.tab-content.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.tide-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-4);
}

.tide-cell {
  padding: var(--space-6);
  background: rgba(0,0,0,0.2);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  text-align: center;
}

.tide-time {
  font-family: monospace;
  font-size: var(--text-xl);
  color: var(--sun-gold);
  margin-bottom: var(--space-2);
}

.tide-level {
  font-size: var(--text-sm);
  color: var(--silver-haze);
}

/* ==========================================================================
   BLOCK 8: GLOW MAP & ROUTE JOURNAL
   ========================================================================== */
.map-layout {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: var(--space-8);
  height: 600px;
}

.map-container {
  padding: var(--space-6);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.map-svg {
  width: 100%;
  height: 100%;
  fill: none;
  stroke: rgba(255,255,255,0.1);
  stroke-width: 2;
}

.map-point {
  fill: var(--void-black);
  stroke: var(--electric-cyan);
  stroke-width: 3;
  cursor: pointer;
  transition: all 0.3s;
}

.map-point:hover, .map-point.active {
  fill: var(--electric-cyan);
  filter: drop-shadow(0 0 10px var(--electric-cyan));
  transform: scale(1.5);
  transform-origin: center;
}

.route-svg {
  stroke: var(--hyper-magenta);
  stroke-width: 2;
  stroke-dasharray: 6 6;
  opacity: 0.5;
  animation: dashMove 20s linear infinite;
}

@keyframes dashMove {
  to { stroke-dashoffset: 200; }
}

.journal-container {
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
}

.journal-header {
  font-size: var(--text-xs);
  color: var(--electric-teal);
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: var(--space-4);
}

.journal-entries {
  flex: 1;
  position: relative;
}

.journal-entry {
  position: absolute;
  top: 0; left: 0; width: 100%;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s ease;
}

.journal-entry.active {
  opacity: 1;
  pointer-events: auto;
}

.journal-title {
  font-size: var(--text-3xl);
  font-weight: 800;
  margin-bottom: var(--space-4);
}

.journal-desc {
  color: var(--silver-haze);
  font-size: var(--text-base);
  margin-bottom: var(--space-6);
}

.journal-meta-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  font-family: monospace;
  font-size: var(--text-sm);
  color: var(--pure-white);
}

.journal-meta-list span {
  color: var(--muted-glass);
}

/* ==========================================================================
   BLOCK 9: METRICS BAND (COUNT-UPS)
   ========================================================================== */
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-6);
  padding: var(--space-12) var(--space-8);
  text-align: center;
}

.metric-item {
  position: relative;
}

.metric-item:not(:last-child)::after {
  content: '';
  position: absolute;
  right: -#text;
  top: 20%;
  bottom: 20%;
  width: 1px;
  background: var(--glass-border);
}

.metric-val {
  font-family: monospace;
  font-size: var(--text-5xl);
  font-weight: 800;
  color: var(--pure-white);
  margin-bottom: var(--space-2);
  text-shadow: 0 0 20px rgba(255,255,255,0.2);
}

.metric-label {
  font-size: var(--text-xs);
  color: var(--silver-haze);
  text-transform: uppercase;
  letter-spacing: 2px;
}

/* ==========================================================================
   BLOCK 10: CONCIERGE & VANTAGE POINTS (Combined for brevity)
   ========================================================================== */
.split-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-8);
}

.checklist-item {
  padding: var(--space-4);
  border-bottom: 1px solid var(--glass-border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.checklist-item:hover {
  background: rgba(255,255,255,0.02);
}

.chk-status {
  width: 20px; height: 20px;
  border-radius: 50%;
  border: 2px solid var(--electric-teal);
  display: inline-block;
  box-shadow: 0 0 10px rgba(0,255,238,0.2);
}

.vantage-gallery {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}

.vantage-frame {
  aspect-ratio: 1;
  background: linear-gradient(45deg, rgba(255,255,255,0.05), transparent);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  position: relative;
  overflow: hidden;
}

.vantage-frame::after {
  content: 'COASTAL CAMERA 0' counter(frame);
  counter-increment: frame;
  position: absolute;
  bottom: 10px; left: 10px;
  font-family: monospace;
  font-size: var(--text-xs);
  color: var(--muted-glass);
}

/* ==========================================================================
   BLOCK 11: MEMBERSHIP PASSES
   ========================================================================== */
.passes-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-8);
}

.pass-card {
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  height: 100%;
}

.pass-tier {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--silver-haze);
  margin-bottom: var(--space-2);
}

.pass-price {
  font-size: var(--text-4xl);
  font-weight: 800;
  margin-bottom: var(--space-6);
  font-family: monospace;
}

.pass-features {
  flex: 1;
  margin-bottom: var(--space-8);
}

.pass-feature {
  padding: var(--space-2) 0;
  border-bottom: 1px dashed var(--glass-border);
  font-size: var(--text-sm);
  color: var(--silver-haze);
}

.pass-card.premium {
  border-color: var(--electric-teal);
  box-shadow: inset 0 0 20px rgba(0, 255, 238, 0.05), 0 0 30px rgba(0, 255, 238, 0.1);
}

/* ==========================================================================
   BLOCK 12: CLUB RULES (ACCORDION)
   ========================================================================== */
.accordion {
  max-width: 800px;
  margin: 0 auto;
}

.acc-item {
  border: 1px solid var(--glass-border);
  margin-bottom: var(--space-4);
  border-radius: var(--radius-md);
  background: var(--glass-surface);
  backdrop-filter: var(--blur-base);
  overflow: hidden;
}

.acc-header {
  padding: var(--space-6);
  width: 100%;
  text-align: left;
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--pure-white);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.acc-header::after {
  content: '+';
  font-size: 24px;
  color: var(--hyper-magenta);
  transition: transform 0.3s;
}

.acc-item.active .acc-header::after {
  transform: rotate(45deg);
}

.acc-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.acc-content {
  padding: 0 var(--space-6) var(--space-6);
  color: var(--silver-haze);
  font-size: var(--text-base);
}

/* ==========================================================================
   BLOCK 13: FINAL DEPARTURE (FORM)
   ========================================================================== */
.departure-sec {
  text-align: center;
  padding: var(--space-24) 0;
}

.inquiry-form {
  max-width: 600px;
  margin: var(--space-8) auto 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}

.form-group-full {
  grid-column: 1 / -1;
}

.inquiry-form input,
.inquiry-form select {
  width: 100%;
  padding: var(--space-4);
  background: rgba(0,0,0,0.3);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  color: var(--pure-white);
}

.inquiry-form input:focus {
  border-color: var(--electric-cyan);
}

/* ==========================================================================
   BLOCK 14: FOOTER
   ========================================================================== */
.site-footer {
  border-top: 1px solid var(--glass-border);
  padding: var(--space-12) 0 var(--space-6);
  background: rgba(0,0,0,0.4);
  position: relative;
  z-index: 10;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: var(--space-8);
  margin-bottom: var(--space-12);
}

.footer-col h4 {
  font-size: var(--text-sm);
  color: var(--pure-white);
  margin-bottom: var(--space-4);
  letter-spacing: 2px;
}

.footer-col ul li {
  margin-bottom: var(--space-2);
}

.footer-col ul li a {
  color: var(--silver-haze);
  font-size: var(--text-sm);
  transition: color var(--transition-fast);
}

.footer-col ul li a:hover {
  color: var(--electric-teal);
}

.footer-legal {
  border-top: 1px solid var(--glass-border);
  padding-top: var(--space-6);
  display: flex;
  justify-content: space-between;
  color: var(--muted-glass);
  font-size: var(--text-xs);
}

/* ==========================================================================
   TOAST NOTIFICATION
   ========================================================================== */
.toast {
  position: fixed;
  bottom: 30px;
  right: -400px;
  background: var(--glass-surface);
  backdrop-filter: var(--blur-base);
  border: 1px solid var(--glass-border-highlight);
  padding: var(--space-4) var(--space-6);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-glow);
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: var(--space-4);
  transition: right 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.toast.show {
  right: 30px;
}

.toast-icon {
  color: var(--open-cyan);
}
</style>
</head>
<body>

  <!-- Ambient Background -->
  <div class="ambient-bg" aria-hidden="true">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
  </div>

  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- 1. Sticky Navbar -->
  <header class="header-nav">
    <div class="container nav-container">
      <a href="#" class="brand">
        <svg viewBox="0 0 24 24"><path d="M12 2L2 22L12 18L22 22L12 2Z"/></svg>
        HELIO
      </a>
      <nav class="nav-links">
        <a href="#fleet">Fleet</a>
        <a href="#map">Routes</a>
        <a href="#passes">Membership</a>
        <a href="#desk">Desk</a>
      </nav>
      <div class="nav-actions">
        <div class="status-chip">
          <span class="status-dot"></span>
          Harbor Open
        </div>
        <button class="btn btn-primary" onclick="showToast()">Member Login</button>
      </div>
    </div>
  </header>

  <!-- 2. Marquee Strip -->
  <div class="ops-strip">
    <div class="ops-track">
      <!-- Repeated for continuous scrolling -->
      <div class="ops-item">NEXT TIDE <span>H 14:00</span></div>
      <div class="ops-item">WIND <span>12KT SSE</span></div>
      <div class="ops-item">RANGE <span>+45NM</span></div>
      <div class="ops-item">WAITLIST <span>OPEN</span></div>
      <div class="ops-item">CONCIERGE <span>ONLINE</span></div>
      
      <div class="ops-item">NEXT TIDE <span>H 14:00</span></div>
      <div class="ops-item">WIND <span>12KT SSE</span></div>
      <div class="ops-item">RANGE <span>+45NM</span></div>
      <div class="ops-item">WAITLIST <span>OPEN</span></div>
      <div class="ops-item">CONCIERGE <span>ONLINE</span></div>
    </div>
  </div>

  <main id="main-content">
    
    <!-- 3. Hero Halo -->
    <section class="container hero-sec">
      <div class="hero-content conic-border glass-panel">
        <div style="padding: 60px 40px; text-align: center;">
          <h1 class="hero-title">Electric Coastlines.<br><span class="text-gradient">Zero Emissions.</span></h1>
          <p class="hero-subtitle">Helio Harbor is an exclusive access point for premium electric dayboats. Quietly navigate untouched coves with guided precision.</p>
          <div class="hero-actions">
            <a href="#passes" class="btn btn-primary">Reserve Anchor</a>
            <a href="#fleet" class="btn btn-glass">Explore Fleet</a>
          </div>
          
          <!-- SVG Signature Visual -->
          <div class="hero-glass-visual glass-panel" style="margin-top: 40px;">
            <svg class="sun-tracker-svg" viewBox="0 0 1000 300" preserveAspectRatio="none">
              <path class="sun-path" d="M50,250 Q500,-50 950,250" />
              <circle class="sun-node" cx="0" cy="0" r="8" />
              <rect x="400" y="240" width="200" height="4" fill="rgba(255,255,255,0.2)"/>
              <text x="410" y="230" fill="var(--electric-teal)" font-family="monospace" font-size="12">HARBOR POINT ALPHA</text>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Harbor Overview -->
    <section class="container section" id="overview">
      <div class="sec-header">
        <span class="sec-label">The Concept</span>
        <h2 class="sec-title text-gradient-magenta">Pristine Architecture</h2>
      </div>
      <div class="overview-grid">
        <div class="overview-card glass-panel glass-panel-hover">
          <div class="card-icon">
            <svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3>Silent Propulsion</h3>
          <p>Advanced axial-flux motors provide instant torque without the vibration, fume, or noise of internal combustion engines.</p>
        </div>
        <div class="overview-card glass-panel glass-panel-hover" style="border-color: var(--electric-cyan);">
          <div class="card-icon">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <h3>Turnkey Prep</h3>
          <p>Our concierge stewards prepare provisions, charge the battery to 100%, and map your safety zones before you enter the dock.</p>
        </div>
        <div class="overview-card glass-panel glass-panel-hover">
          <div class="card-icon">
            <svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          </div>
          <h3>Automated Berths</h3>
          <p>Return is effortless. Engage the hover-dock sequence, and the slip magnetic plates align the hull perfectly in seconds.</p>
        </div>
      </div>
    </section>

    <!-- 5. Glass Fleet -->
    <section class="section" id="fleet" style="position: relative;">
      <div class="container">
        <div class="sec-header" style="text-align: left;">
          <span class="sec-label">Our Vessels</span>
          <h2 class="sec-title">The Electric Fleet</h2>
        </div>
      </div>
      <div class="fleet-scroll" style="padding-left: max(var(--space-6), calc((100vw - var(--container-width))/2));">
        
        <!-- Vessel 1 -->
        <div class="fleet-card glass-panel conic-border">
          <div class="fleet-card-img">
            <svg class="blueprint-svg" viewBox="0 0 100 100">
              <path d="M50 10 L80 50 L50 90 L20 50 Z" />
              <circle cx="50" cy="50" r="15" fill="var(--electric-teal)" opacity="0.2"/>
            </svg>
          </div>
          <div class="fleet-meta">
            <div>
              <h3 class="fleet-name">Aero Six</h3>
              <div class="fleet-specs">
                <span>R: 40NM</span>
                <span>C: 6 PAX</span>
                <span>V: 24KT</span>
              </div>
            </div>
            <button class="btn btn-primary" style="padding: 10px 20px;">Spec</button>
          </div>
        </div>

        <!-- Vessel 2 -->
        <div class="fleet-card glass-panel conic-border" style="--conic-angle: 90deg;">
          <div class="fleet-card-img">
            <svg class="blueprint-svg" viewBox="0 0 100 100">
              <path d="M50 5 L90 50 L50 95 L10 50 Z" />
              <rect x="40" y="40" width="20" height="20" fill="var(--hyper-magenta)" opacity="0.2"/>
            </svg>
          </div>
          <div class="fleet-meta">
            <div>
              <h3 class="fleet-name">Lumina X</h3>
              <div class="fleet-specs">
                <span>R: 60NM</span>
                <span>C: 10 PAX</span>
                <span>V: 32KT</span>
              </div>
            </div>
            <button class="btn btn-primary" style="padding: 10px 20px;">Spec</button>
          </div>
        </div>

        <!-- Vessel 3 -->
        <div class="fleet-card glass-panel conic-border" style="--conic-angle: 180deg;">
          <div class="fleet-card-img">
            <svg class="blueprint-svg" viewBox="0 0 100 100">
              <polygon points="50,10 85,30 85,70 50,90 15,70 15,30" />
              <circle cx="50" cy="50" r="10" fill="var(--sun-gold)" opacity="0.3"/>
            </svg>
          </div>
          <div class="fleet-meta">
            <div>
              <h3 class="fleet-name">Nova Core</h3>
              <div class="fleet-specs">
                <span>R: 85NM</span>
                <span>C: 12 PAX</span>
                <span>V: 40KT</span>
              </div>
            </div>
            <button class="btn btn-primary" style="padding: 10px 20px;">Spec</button>
          </div>
        </div>

      </div>
    </section>

    <!-- 6. Tide & Transit Desk -->
    <section class="container section" id="desk">
      <div class="sec-header">
        <span class="sec-label">Operations Console</span>
        <h2 class="sec-title">Harbor Desk</h2>
      </div>
      
      <div class="tide-desk glass-panel conic-border">
        <div class="tabs-nav">
          <button class="tab-btn active" data-target="tab-live">Live Tides</button>
          <button class="tab-btn" data-target="tab-weather">Weather</button>
          <button class="tab-btn" data-target="tab-range">Range Limits</button>
        </div>

        <div class="tab-content active" id="tab-live">
          <p style="margin-bottom: var(--space-6); color: var(--silver-haze);">Estuary observation data. Syncing with regional buoys.</p>
          <div class="tide-grid">
            <div class="tide-cell">
              <div class="tide-time">06:24</div>
              <div class="tide-level">Low Tide (-0.2m)</div>
            </div>
            <div class="tide-cell">
              <div class="tide-time">12:15</div>
              <div class="tide-level">High Tide (+2.4m)</div>
            </div>
            <div class="tide-cell">
              <div class="tide-time">18:42</div>
              <div class="tide-level">Low Tide (+0.1m)</div>
            </div>
            <div class="tide-cell" style="border-color: var(--hyper-magenta);">
              <div class="tide-time">00:30</div>
              <div class="tide-level">High Tide (+2.6m)</div>
            </div>
          </div>
        </div>

        <div class="tab-content" id="tab-weather">
          <p style="margin-bottom: var(--space-6); color: var(--silver-haze);">Offshore and nearshore predictions.</p>
          <div style="font-family: monospace; font-size: 24px;">WIND: 12KT SSE <br> SWELL: 0.8M <br> VISIBILITY: 10NM CLEAR</div>
        </div>

        <div class="tab-content" id="tab-range">
          <p style="margin-bottom: var(--space-6); color: var(--silver-haze);">Current battery envelope boundaries.</p>
          <div style="font-family: monospace; font-size: 24px; color: var(--electric-cyan);">SAFE ROUND TRIP: 45NM<br>EMERGENCY RESERVE: 15%</div>
        </div>
      </div>
    </section>

    <!-- 7. Glow Map & Route Journal -->
    <section class="container section" id="map">
      <div class="sec-header">
        <span class="sec-label">Wayfinding</span>
        <h2 class="sec-title">Curated Vectors</h2>
      </div>

      <div class="map-layout">
        <!-- SVG Map Area -->
        <div class="map-container glass-panel">
          <svg class="map-svg" viewBox="0 0 500 500">
            <!-- Topography lines -->
            <path d="M50 450 Q 150 200 450 50" class="route-svg"/>
            <path d="M100 400 Q 250 300 400 150" class="route-svg" style="stroke:var(--electric-teal); stroke-dasharray:4 4;"/>
            
            <!-- Nodes -->
            <circle cx="50" cy="450" r="12" class="map-point active" data-point="pt-1"/>
            <circle cx="200" cy="300" r="10" class="map-point" data-point="pt-2"/>
            <circle cx="450" cy="50" r="14" class="map-point" data-point="pt-3"/>
            <circle cx="400" cy="150" r="8" class="map-point" data-point="pt-4"/>
          </svg>
        </div>

        <!-- Interactive Journal -->
        <div class="journal-container glass-panel">
          <div class="journal-header">Waypoint Logic</div>
          <div class="journal-entries">
            
            <div class="journal-entry active" id="pt-1">
              <h3 class="journal-title text-gradient">Harbor Base</h3>
              <p class="journal-desc">The primary docking array. All fleets terminate and charge here. Constant concierge presence and premium lounge.</p>
              <div class="journal-meta-list">
                <div><span>DEPTH:</span> 4.5M</div>
                <div><span>STATUS:</span> CLEAR</div>
                <div><span>FACILITY:</span> CHARGE ALPHA</div>
              </div>
            </div>

            <div class="journal-entry" id="pt-2">
              <h3 class="journal-title text-gradient">Silent Cove</h3>
              <p class="journal-desc">A deep, protected anchorage perfectly suited for dropping hook, swimming, and utilizing the zero-noise profile.</p>
              <div class="journal-meta-list">
                <div><span>DEPTH:</span> 12.0M</div>
                <div><span>STATUS:</span> WILDLIFE ZONE</div>
                <div><span>RESTRICTION:</span> 5KT IDLE</div>
              </div>
            </div>

            <div class="journal-entry" id="pt-3">
              <h3 class="journal-title text-gradient-magenta">Outer Spire</h3>
              <p class="journal-desc">The furthest recommended vector. High cliff faces block the prevailing western winds. Optimal sunset vantage.</p>
              <div class="journal-meta-list">
                <div><span>DEPTH:</span> 35.0M</div>
                <div><span>STATUS:</span> OPEN WATER</div>
                <div><span>DISTANCE:</span> 22NM OUT</div>
              </div>
            </div>

            <div class="journal-entry" id="pt-4">
              <h3 class="journal-title text-gradient">Reef Gate</h3>
              <p class="journal-desc">A narrow natural channel requiring precise navigation. The electric drive's immediate response makes transit trivial.</p>
              <div class="journal-meta-list">
                <div><span>DEPTH:</span> 2.5M WARNING</div>
                <div><span>STATUS:</span> CURRENT HEAVY</div>
                <div><span>TIDE REQ:</span> MID-TO-HIGH</div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- 8. Metrics Band -->
    <section class="container section">
      <div class="metrics-grid glass-panel conic-border">
        <div class="metric-item">
          <div class="metric-val" data-count="14500">0</div>
          <div class="metric-label">Nautical Miles Logged</div>
        </div>
        <div class="metric-item">
          <div class="metric-val" data-count="100">0</div>
          <div class="metric-label">% Zero Emission</div>
        </div>
        <div class="metric-item">
          <div class="metric-val" data-count="32">0</div>
          <div class="metric-label">Vessels in Hub</div>
        </div>
        <div class="metric-item">
          <div class="metric-val" data-count="5">0</div>
          <div class="metric-label">Min. Docking Time</div>
        </div>
      </div>
    </section>

    <!-- 9. Concierge & Vantage -->
    <section class="container section">
      <div class="sec-header">
        <span class="sec-label">Service Layer</span>
        <h2 class="sec-title">Unseen Effort</h2>
      </div>
      
      <div class="split-section">
        <!-- Checklist -->
        <div class="glass-panel" style="padding: var(--space-8);">
          <h3 style="margin-bottom: var(--space-6); font-size: var(--text-2xl);">Pre-Departure Routine</h3>
          <div class="checklist">
            <div class="checklist-item">
              <span>High-voltage battery verification (100%)</span>
              <span class="chk-status"></span>
            </div>
            <div class="checklist-item">
              <span>Hull anomaly scanning</span>
              <span class="chk-status" style="border-color: var(--hyper-magenta);"></span>
            </div>
            <div class="checklist-item">
              <span>Chilled beverage & hamper load</span>
              <span class="chk-status"></span>
            </div>
            <div class="checklist-item">
              <span>Navigational chart sync for selected route</span>
              <span class="chk-status"></span>
            </div>
          </div>
        </div>

        <!-- Cameras -->
        <div class="vantage-gallery">
          <div class="vantage-frame"></div>
          <div class="vantage-frame" style="background: linear-gradient(135deg, rgba(0,255,238,0.1), transparent);"></div>
          <div class="vantage-frame" style="background: linear-gradient(200deg, rgba(255,0,170,0.1), transparent);"></div>
          <div class="vantage-frame"></div>
        </div>
      </div>
    </section>

    <!-- 10. Membership Passes -->
    <section class="container section" id="passes">
      <div class="sec-header" style="text-align: center;">
        <span class="sec-label">Access control</span>
        <h2 class="sec-title">Charter Tiers</h2>
      </div>

      <div class="passes-grid">
        <div class="pass-card glass-panel">
          <div class="pass-tier">Seasonal</div>
          <div class="pass-price">$2,500<span style="font-size:16px;">/yr</span></div>
          <div class="pass-features">
            <div class="pass-feature">12 Days of Access</div>
            <div class="pass-feature">Aero Six Vessel</div>
            <div class="pass-feature">Standard Provisioning</div>
          </div>
          <button class="btn btn-glass">Apply Now</button>
        </div>

        <div class="pass-card glass-panel premium">
          <div style="position: absolute; top:0; right:0; background: var(--electric-teal); color: var(--void-black); padding: 4px 12px; font-weight: bold; border-bottom-left-radius: var(--radius-md);">WAITLIST</div>
          <div class="pass-tier" style="color: var(--electric-cyan);">Core Network</div>
          <div class="pass-price">$5,800<span style="font-size:16px;">/yr</span></div>
          <div class="pass-features">
            <div class="pass-feature">Unlimited Weekday Access</div>
            <div class="pass-feature">Full Fleet Access</div>
            <div class="pass-feature">Premium Wine & Hamper</div>
            <div class="pass-feature">Route Planning Concierge</div>
          </div>
          <button class="btn btn-primary" onclick="showToast('Added to priority waitlist for Core Network.')">Join Waitlist</button>
        </div>

        <div class="pass-card glass-panel">
          <div class="pass-tier">Syndicate</div>
          <div class="pass-price">$12,000<span style="font-size:16px;">/yr</span></div>
          <div class="pass-features">
            <div class="pass-feature">Guaranteed Availability</div>
            <div class="pass-feature">Nova Core Priority</div>
            <div class="pass-feature">Overnight Docking Privileges</div>
            <div class="pass-feature">Private Event Hosting</div>
          </div>
          <button class="btn btn-glass">Contact Office</button>
        </div>
      </div>
    </section>

    <!-- 11. FAQ Accordion -->
    <section class="container section">
      <div class="sec-header">
        <span class="sec-label">Directives</span>
        <h2 class="sec-title">Operations Manual</h2>
      </div>

      <div class="accordion glass-panel" style="padding: var(--space-8);">
        
        <div class="acc-item active">
          <button class="acc-header">Do I need a captain's license?</button>
          <div class="acc-body" style="max-height: 200px;">
            <div class="acc-content">For the Aero Six, no formal license is required. Only a 45-minute safety orientation session. For Lumina X and Nova Core, we require a state boating certification or verification of prior offshore experience.</div>
          </div>
        </div>

        <div class="acc-item">
          <button class="acc-header">What happens if the battery gets low?</button>
          <div class="acc-body">
            <div class="acc-content">Our software enforces geofencing based on state-of-charge. The vessel will automatically notify the harbor desk at 20%, and at 10% it will limit top speed to ensure a safe return. You cannot be stranded.</div>
          </div>
        </div>

        <div class="acc-item">
          <button class="acc-header">Can I bring non-members?</button>
          <div class="acc-body">
            <div class="acc-content">Absolutely. As the piloting member, you assume liability, but your guests are completely welcome to enjoy the club facilities and the vessel's capacity limits.</div>
          </div>
        </div>

      </div>
    </section>

    <!-- 12. Final Departure -->
    <section class="container section departure-sec glass-panel conic-border" style="margin-bottom: var(--space-24);">
      <h2 class="sec-title">File Float Plan</h2>
      <p style="color: var(--silver-haze); margin-top: var(--space-4);">Submit an inquiry for terminal tours or trial voyages.</p>
      
      <form class="inquiry-form" onsubmit="event.preventDefault(); showToast('Float plan securely transmitted to desk.');">
        <input type="text" placeholder="Call sign / Name" required>
        <input type="email" placeholder="Comms link / Email" required>
        <select class="form-group-full">
          <option value="">Select Vessel Interest</option>
          <option value="aero">Aero Six</option>
          <option value="lumina">Lumina X</option>
          <option value="nova">Nova Core</option>
        </select>
        <button type="submit" class="btn btn-primary form-group-full">Transmit Request</button>
      </form>
    </section>

  </main>

  <!-- 13. Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>HELIO HARBOR</h4>
          <p style="color: var(--silver-haze); font-size: var(--text-sm);">The zero-emission transit authority.<br>Precision mobility for the modern coast.</p>
        </div>
        <div class="footer-col">
          <h4>SYSTEMS</h4>
          <ul>
            <li><a href="#">Network Map</a></li>
            <li><a href="#">Vessel Specs</a></li>
            <li><a href="#">Tide API</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>STATION</h4>
          <ul>
            <li><a href="#">Concierge Desk</a></li>
            <li><a href="#">Waitlist Status</a></li>
            <li><a href="#">Security</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>LEGAL</h4>
          <ul>
            <li><a href="#">Terms of Fleet</a></li>
            <li><a href="#">Privacy Protocol</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-legal">
        <span>&copy; 2026 Helio Harbor Electric Mobility Group.</span>
        <span>NODE: ALPHA-7 // OP-NORMAL</span>
      </div>
    </div>
  </footer>

  <!-- Toast Element -->
  <div class="toast" id="sys-toast">
    <div class="toast-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
    </div>
    <div class="toast-msg" id="toast-msg">Action confirmed.</div>
  </div>

<script>
/* ==========================================================================
   REAL JAVASCRIPT INTERACTIONS
   ========================================================================== */

// 1. Tabs Logic
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    // Remove active from siblings
    const parent = btn.closest('.tide-desk');
    parent.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    
    // Add active to clicked
    btn.classList.add('active');
    document.getElementById(btn.dataset.target).classList.add('active');
  });
});

// 2. Map Journal Interaction
document.querySelectorAll('.map-point').forEach(point => {
  point.addEventListener('mouseenter', () => {
    // Clear all active points and journals
    document.querySelectorAll('.map-point').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.journal-entry').forEach(e => e.classList.remove('active'));
    
    // Activate current
    point.classList.add('active');
    document.getElementById(point.dataset.point).classList.add('active');
  });
});

// 3. Accordion Logic
document.querySelectorAll('.acc-header').forEach(header => {
  header.addEventListener('click', () => {
    const item = header.parentElement;
    const body = item.querySelector('.acc-body');
    const isActive = item.classList.contains('active');
    
    // Close all
    document.querySelectorAll('.acc-item').forEach(i => {
      i.classList.remove('active');
      i.querySelector('.acc-body').style.maxHeight = null;
    });

    // Toggle current
    if (!isActive) {
      item.classList.add('active');
      body.style.maxHeight = body.scrollHeight + "px";
    }
  });
});

// 4. Count-Up Metrics on scroll
const observerOptions = { threshold: 0.1 };
let metricsAnimated = false;

const metricsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !metricsAnimated) {
      metricsAnimated = true;
      document.querySelectorAll('.metric-val').forEach(el => {
        const target = parseInt(el.dataset.count, 10);
        let current = 0;
        const inc = target / 50; 
        const tick = setInterval(() => {
          current += inc;
          if (current >= target) {
            el.innerText = target;
            clearInterval(tick);
          } else {
            el.innerText = Math.floor(current);
          }
        }, 30);
      });
    }
  });
}, observerOptions);

const metricsSection = document.querySelector('.metrics-grid');
if (metricsSection) {
  metricsObserver.observe(metricsSection);
}

// 5. Toast Notification System
let toastTimeout;
function showToast(msg = "System authenticated.") {
  const toast = document.getElementById('sys-toast');
  const toastMsg = document.getElementById('toast-msg');
  
  toastMsg.innerText = msg;
  toast.classList.add('show');
  
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 4000);
}
</script>
</body>
</html>
"""

with open(r"c:\Users\saying\Desktop\html_agent\fdu_010\src\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated index.html successfully.")
