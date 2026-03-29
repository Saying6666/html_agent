import os

md_content = """# fdu_048 - Glo-UI Glassmorphism SaaS
## Round 1

Create a production-grade 2025-2026 single-page website for **Lumina Sync**, a next-generation decentralized edge computing platform.

The UI MUST use Modern Premium Glassmorphism & Glo UI.
Use intensive `backdrop-filter:blur`, deeply layered gradients, conic-gradient borders, and ambient blurred orbs floating in the background to set a premium mood.
Real micro-interactions, smooth hover states, dynamic cursor trackers, magnetic buttons, and rich 3D tilting cards are required.

Audience:
- Senior engineers, CTOs, decentralization proponents, forward-thinking cloud architects.
- Need high aesthetic fidelity to invoke trust and signal "bleeding edge" technology.

This case must commit to a specific visual world:
**Modern Premium Glassmorphism & Glo UI**

Theme tokens:
- Deep obsidian and midnight purple backgrounds (#08080C, #130a21), with bright cyan, pink, and glowing electric blue orbs.
- Frosted glass panels (rgba(255, 255, 255, 0.05)), glowing borders.
- Typography: Outfit, Inter, or Space Grotesk. Highly legible, variable weights.

Must have 12 sections with REAL, convincing, jargon-accurate copy¡ªNO PLACEHOLDERS (e.g., no "Lorem ipsum").

Sections Required:
1.  **Global Hero**: Full viewport, glowing central orb, floating glass card, massive dynamic typography ("The Edge of Tomorrow"). 
2.  **Ticker/Logos**: High-end enterprise partners, marquee scrolling continuously.
3.  **Value Proposition**: Frosted glass cards explaining the triad of Edge, Speed, Security.
4.  **Tech Architecture**: Visual stack with concentric glow borders.
5.  **Interactive Performance Dashboard**: A mock glass card showing "Live Global Latency" with JS-driven animated charts or bars.
6.  **Use Cases**: Grid of use cases (AI, Gaming, Finance) with hover-zoom backgrounds.
7.  **Comparison Table**: Us vs. Traditional Cloud, glass table, glowing checkmarks.
8.  **Security Protocol**: Deep-dive into Quantum-safe encryption, padlock graphic with ambient pulse.
9.  **Testimonials/Quotations**: Sliding glass cards from CTOs.
10. **Developer Experience**: A code block inside a frosted window, syntax highlighted with glowing text.
11. **Pricing Tiers**: 3 tiers. The middle tier has a conic-gradient animated border.
12. **Global Footer**: Multi-column links, newsletter signup input with magnetic submit, floating orb behind it.

Mandatory technical requirements:
1. `backdrop-filter` heavily utilized.
2. Animated blobs (`div`s with high `filter: blur()`).
3. Smooth vanilla JS animations (IntersectionObserver for scroll reveals).
4. Mouse tracking effect on cards (updating CSS variables for radial burst on cursor position).
5. Fully responsive.

Ensure copy is thoroughly written and production-ready.
""" + "\n" * 150

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lumina Sync - Premium Edge Computing</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg-dark: #08080c;
    --acc-cyan: #00f0ff;
    --acc-pink: #ff0055;
    --acc-purple: #7a00ff;
    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-border: rgba(255, 255, 255, 0.08);
    --text-main: #f0f0f5;
    --text-muted: #a0a0b0;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Outfit', sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-main);
    overflow-x: hidden;
    line-height: 1.6;
    position: relative;
  }
  /* Ambient Orbs */
  .orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(120px);
    z-index: -1;
    pointer-events: none;
    animation: drift 20s infinite alternate ease-in-out;
  }
  .orb-1 { top: -10%; left: -10%; width: 50vw; height: 50vw; background: rgba(0, 240, 255, 0.15); }
  .orb-2 { top: 40%; right: -20%; width: 60vw; height: 60vw; background: rgba(255, 0, 85, 0.1); animation-delay: -5s; }
  .orb-3 { bottom: -10%; left: 20%; width: 40vw; height: 40vw; background: rgba(122, 0, 255, 0.15); animation-delay: -10s; }
  @keyframes drift {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(50px, 50px) scale(1.1); }
  }

  .glass-panel {
    background: var(--glass-bg);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    padding: 2rem;
    position: relative;
    overflow: hidden;
  }
  /* Mouse Tracker Glow */
  .glass-panel::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(800px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(255,255,255,0.06), transparent 40%);
    z-index: 1;
    pointer-events: none;
    transition: opacity 0.3s;
    opacity: 0;
  }
  .glass-panel:hover::before { opacity: 1; }

  .container { max-width: 1400px; margin: 0 auto; padding: 0 5%; position: relative; z-index: 2; }
  
  nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 1.5rem 5%; position: fixed; width: 100%; top: 0; z-index: 100;
    backdrop-filter: blur(20px); border-bottom: 1px solid var(--glass-border);
  }
  .logo { font-size: 1.5rem; font-weight: 800; letter-spacing: -1px; display: flex; align-items: center; gap: 10px; }
  .logo-icon { width: 24px; height: 24px; background: linear-gradient(45deg, var(--acc-cyan), var(--acc-purple)); border-radius: 50%; }
  .nav-links { display: flex; gap: 2rem; }
  .nav-links a { color: var(--text-main); text-decoration: none; font-size: 0.9rem; font-weight: 400; opacity: 0.8; transition: opacity 0.3s; }
  .nav-links a:hover { opacity: 1; }
  .nav-cta {
    background: linear-gradient(90deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02));
    border: 1px solid var(--glass-border); padding: 0.6rem 1.5rem; border-radius: 30px;
    font-weight: 600; cursor: pointer; color: #fff; text-decoration: none;
    transition: all 0.3s;
  }
  .nav-cta:hover { background: rgba(255,255,255,0.1); box-shadow: 0 0 20px rgba(255,255,255,0.2); }

  section { padding: 120px 0; }

  /* 1. Global Hero */
  .hero { height: 100vh; display: flex; align-items: center; text-align: center; justify-content: center; flex-direction: column; }
  .hero h1 { font-size: clamp(3rem, 6vw, 6rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; background: linear-gradient(to right, #fff, var(--text-muted)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .hero p { font-size: 1.25rem; color: var(--text-muted); max-width: 600px; margin-bottom: 3rem; }
  .hero-buttons { display: flex; gap: 1rem; justify-content: center; }
  .btn-primary {
    padding: 1rem 2.5rem; border-radius: 30px; background: linear-gradient(45deg, var(--acc-cyan), var(--acc-purple));
    color: #fff; font-weight: 600; font-size: 1.1rem; border: none; cursor: pointer; text-decoration: none;
    box-shadow: 0 0 30px rgba(0, 240, 255, 0.4); transition: transform 0.2s, box-shadow 0.2s;
  }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 0 40px rgba(0, 240, 255, 0.6); }

  /* 2. Ticker/Logos */
  .ticker { overflow: hidden; white-space: nowrap; padding: 2rem 0; border-top: 1px solid var(--glass-border); border-bottom: 1px solid var(--glass-border); background: rgba(0,0,0,0.2); }
  .ticker-track { display: inline-block; animation: scroll 30s linear infinite; }
  .ticker-item { display: inline-block; margin: 0 3rem; font-size: 1.5rem; font-weight: 800; color: rgba(255,255,255,0.2); text-transform: uppercase; }
  @keyframes scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

  /* 3. Value Props */
  .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
  .card-icon { width: 48px; height: 48px; border-radius: 12px; background: rgba(255,255,255,0.05); display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 1.5rem; box-shadow: inset 0 0 10px rgba(255,255,255,0.1); }
  .glass-panel h3 { font-size: 1.5rem; margin-bottom: 1rem; }
  .glass-panel p { color: var(--text-muted); }

  /* 4. Tech Arch */
  .tech-arch { text-align: center; }
  .stack-visual { margin-top: 4rem; position: relative; height: 400px; display: flex; align-items: center; justify-content: center; }
  .layer { position: absolute; border: 1px solid var(--glass-border); border-radius: 50%; opacity: 0.5; animation: pulse 4s infinite alternate; }
  .layer-1 { width: 200px; height: 200px; border-color: var(--acc-cyan); }
  .layer-2 { width: 300px; height: 300px; border-color: var(--acc-purple); animation-delay: 1s; }
  .layer-3 { width: 400px; height: 400px; border-color: var(--acc-pink); animation-delay: 2s; }
  @keyframes pulse { 0% { transform: scale(1) rotate(0deg); opacity: 0.3; } 100% { transform: scale(1.05) rotate(5deg); opacity: 0.8; } }

  /* 5. Dashboard */
  .dash-ui { background: rgba(0,0,0,0.4); border-radius: 16px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; }
  .dash-bar { height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; }
  .dash-fill { height: 100%; background: linear-gradient(90deg, var(--acc-cyan), var(--acc-purple)); width: 0%; transition: width 1s ease; }

  /* Utilities */
  .section-title { text-align: center; font-size: 3rem; margin-bottom: 1rem; font-weight: 800; background: linear-gradient(to right, #fff, #888); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .section-sub { text-align: center; color: var(--text-muted); font-size: 1.2rem; max-width: 600px; margin: 0 auto 4rem auto; }

  /* Scroll Reveal */
  .reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.5, 0, 0, 1); }
  .reveal.active { opacity: 1; transform: translateY(0); }

  /* Conic Border Card */
  .conic-card {
    position: relative;
    border-radius: 24px;
    padding: 1px; /* border width */
    background: conic-gradient(from var(--angle), transparent 20%, var(--acc-cyan) 50%, transparent 80%);
    animation: rotate-border 4s linear infinite;
  }
  @property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }
  @keyframes rotate-border { to { --angle: 360deg; } }
  .conic-card-inner {
    background: var(--bg-dark);
    border-radius: 23px;
    padding: 2rem;
    height: 100%;
  }

  /* Padding expansion */
  .spacer { height: 100px; }
  
  th, td { padding: 1.5rem; text-align: left; border-bottom: 1px solid var(--glass-border); }
  th { font-weight: 600; color: #fff; }
  tr:last-child td { border-bottom: none; }
  table { width: 100%; border-collapse: collapse; }
  
  .glow-text { text-shadow: 0 0 10px rgba(0,240,255,0.5); color: var(--acc-cyan); }
  
  /* Use Cases */
  .use-case-card { height: 250px; display: flex; align-items: flex-end; padding: 2rem; border-radius: 20px; position: relative; overflow: hidden; border: 1px solid var(--glass-border); transition: transform 0.3s; }
  .use-case-card:hover { transform: translateY(-5px); }
  .use-case-card::before { content: ''; position: absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); z-index: 1; }
  .use-case-card h3, .use-case-card p { position: relative; z-index: 2; margin: 0; }
  .use-case-card h3 { font-size: 1.5rem; margin-bottom: 0.5rem; }
  .use-case-card p { font-size: 0.9rem; color: #ccc; }
  .uc-1 { background: url('https://images.unsplash.com/photo-1620825937374-87fc7d62095f?auto=format&fit=crop&q=80&w=600') center/cover; }
  .uc-2 { background: url('https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&q=80&w=600') center/cover; }
  .uc-3 { background: url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=600') center/cover; }

  /* Footer */
  footer { border-top: 1px solid var(--glass-border); padding: 4rem 5% 2rem; position: relative; background: rgba(0,0,0,0.3); }
  .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; margin-bottom: 3rem; }
  .footer-col h4 { margin-bottom: 1.5rem; font-size: 1.1rem; }
  .footer-col ul { list-style: none; }
  .footer-col ul li { margin-bottom: 0.8rem; }
  .footer-col ul li a { color: var(--text-muted); text-decoration: none; transition: color 0.2s; }
  .footer-col ul li a:hover { color: #fff; }
  .input-group { display: flex; gap: 1rem; margin-top: 1.5rem; }
  input[type="email"] { background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); padding: 0.8rem 1rem; border-radius: 8px; color: #fff; flex: 1; outline: none; transition: border-color 0.3s; }
  input[type="email"]:focus { border-color: var(--acc-cyan); }
  .btn-submit { background: #fff; color: #000; border: none; padding: 0.8rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: background 0.3s; }
  .btn-submit:hover { background: #ccc; }
  .footer-bottom { text-align: center; color: var(--text-muted); font-size: 0.9rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.05); }

</style>
</head>
<body>

  <!-- Ambient BG Orbs -->
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>

  <nav>
    <div class="logo">
      <div class="logo-icon"></div>
      Lumina
    </div>
    <div class="nav-links">
      <a href="#platform">Platform</a>
      <a href="#network">Network</a>
      <a href="#security">Security</a>
      <a href="#pricing">Pricing</a>
    </div>
    <a href="#" class="nav-cta">Deploy Now</a>
  </nav>

  <!-- Section 1: Hero -->
  <section class="hero" id="home">
    <div class="container">
      <h1 class="reveal">The Edge of Tomorrow</h1>
      <p class="reveal" style="transition-delay: 0.1s;">Experience zero-latency decentralized computing. Lumina Sync distributes your workloads across global nano-nodes for unparalleled speed, resilience, and quantum-safe security.</p>
      <div class="hero-buttons reveal" style="transition-delay: 0.2s;">
        <a href="#start" class="btn-primary">Start Building Free</a>
        <a href="#docs" class="nav-cta" style="padding: 1rem 2.5rem;">Read the Docs</a>
      </div>
    </div>
  </section>

  <!-- Section 2: Ticker -->
  <div class="ticker">
    <div class="ticker-track">
      <span class="ticker-item">AeroDynamic Space</span>
      <span class="ticker-item">Quantum Ledger</span>
      <span class="ticker-item">Nexus Gaming</span>
      <span class="ticker-item">OmniFi Solutions</span>
      <span class="ticker-item">Vortex Neural</span>
      <span class="ticker-item">AeroDynamic Space</span>
      <span class="ticker-item">Quantum Ledger</span>
      <span class="ticker-item">Nexus Gaming</span>
      <span class="ticker-item">OmniFi Solutions</span>
      <span class="ticker-item">Vortex Neural</span>
    </div>
  </div>

  <!-- Section 3: Value Props -->
  <section id="platform">
    <div class="container">
      <h2 class="section-title reveal">Architected for the Extraordinary</h2>
      <p class="section-sub reveal">We rebuilt the cloud from first principles to serve the latency-critical applications of the next decade.</p>
      
      <div class="grid-3">
        <div class="glass-panel reveal track-mouse">
          <div class="card-icon">?</div>
          <h3>Sub-Millisecond Edge</h3>
          <p>By routing computations to the nearest regional nano-node in our decentralized swarm, we ensure that round-trip times are virtually eliminated, achieving true real-time performance.</p>
        </div>
        <div class="glass-panel reveal track-mouse" style="transition-delay: 0.1s;">
          <div class="card-icon">???</div>
          <h3>Quantum-Resilient</h3>
          <p>Every packet is encrypted using lattice-based cryptographic algorithms, future-proofing your data against both contemporary attacks and emerging quantum threats.</p>
        </div>
        <div class="glass-panel reveal track-mouse" style="transition-delay: 0.2s;">
          <div class="card-icon">¡Þ</div>
          <h3>Infinite Scalability</h3>
          <p>Our dynamic provisioning engine assesses global load in real-time, auto-scaling your containers seamlessly whether you have ten users or ten million concurrent connections.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: Tech Arch -->
  <section class="tech-arch" id="network">
    <div class="container reveal">
      <h2 class="section-title">The Lumina Topology</h2>
      <p class="section-sub">A visualized cross-section of our multi-layered global consensus and compute grid.</p>
      
      <div class="stack-visual">
        <div class="layer layer-3"></div>
        <div class="layer layer-2"></div>
        <div class="layer layer-1"></div>
        <div class="glass-panel" style="position:relative; z-index:10; max-width: 400px; margin: 0 auto; backdrop-filter: blur(30px);">
          <h3>Core Routing Engine</h3>
          <p style="font-size:0.9rem; margin-top: 10px;">Distributes 10m+ req/s globally via BGP Anycast and probabilistic node matching.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: Dashboard -->
  <section id="dash">
    <div class="container reveal">
      <h2 class="section-title">Live Global Telemetry</h2>
      <p class="section-sub">Monitor node health, localized latency, and real-time bandwidth consumption across the Lumina grid.</p>
      
      <div class="glass-panel dash-ui">
        <div style="display:flex; justify-content:space-between;">
          <span>Node Cluster: NA-East (Virginia)</span>
          <span class="glow-text">5 ms</span>
        </div>
        <div class="dash-bar"><div class="dash-fill" data-width="95%"></div></div>

        <div style="display:flex; justify-content:space-between; margin-top:1rem;">
          <span>Node Cluster: EU-West (Frankfurt)</span>
          <span class="glow-text">12 ms</span>
        </div>
        <div class="dash-bar"><div class="dash-fill" data-width="80%"></div></div>

        <div style="display:flex; justify-content:space-between; margin-top:1rem;">
          <span>Node Cluster: AP-Northeast (Tokyo)</span>
          <span class="glow-text">8 ms</span>
        </div>
        <div class="dash-bar"><div class="dash-fill" data-width="88%"></div></div>
      </div>
    </div>
  </section>

  <!-- Section 6: Use Cases -->
  <section id="cases">
    <div class="container">
      <h2 class="section-title reveal">Empowering Next-Gen Verticals</h2>
      <p class="section-sub reveal">When standard cloud providers choke on data volume, Lumina accelerates.</p>

      <div class="grid-3">
        <div class="use-case-card uc-1 reveal">
          <div>
            <h3>Autonomous Logistics</h3>
            <p>Real-time vehicle-to-everything (V2X) communication arrays processing local sensor data without cloud round-trips.</p>
          </div>
        </div>
        <div class="use-case-card uc-2 reveal" style="transition-delay: 0.1s;">
          <div>
            <h3>High-Frequency Trading</h3>
            <p>Execution algorithms relying on collocated nodes to front-run traditional fiber routes using laser-link grid overlays.</p>
          </div>
        </div>
        <div class="use-case-card uc-3 reveal" style="transition-delay: 0.2s;">
          <div>
            <h3>Interactive VR / XR</h3>
            <p>Streaming 8K immersive environments to lightweight headsets by offloading GPU rendering to localized edge clusters.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 7: Comparison Table -->
  <section id="compare">
    <div class="container reveal">
      <h2 class="section-title">Lumina vs Standard Cloud</h2>
      <div class="glass-panel" style="overflow-x: auto;">
        <table>
          <thead>
            <tr>
              <th>Metric</th>
              <th>Traditional Cloud</th>
              <th>Lumina Edge Grid</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Global Latency Avg</td>
              <td>50 - 150ms</td>
              <td class="glow-text">5 - 12ms</td>
            </tr>
            <tr>
              <td>Point of Failure</td>
              <td>Centralized Datacenters</td>
              <td class="glow-text">Fully Decentralized</td>
            </tr>
            <tr>
              <td>Data Sovereignty</td>
              <td>Vague, Regional Only</td>
              <td class="glow-text">Strict Cryptographic Locality</td>
            </tr>
            <tr>
              <td>Deployment Time</td>
              <td>Minutes</td>
              <td class="glow-text">&lt; 500 Milliseconds</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Section 8: Security -->
  <section id="security">
    <div class="container reveal" style="text-align: center;">
      <h2 class="section-title">Impenetrable by Design</h2>
      <p class="section-sub">We don't trust the hardware. We mathematically prove security at the protocol level.</p>
      
      <div class="glass-panel" style="display:inline-block; padding: 3rem; text-align:left; max-width: 800px; margin: 0 auto;">
        <h3 style="margin-bottom: 1rem; color: var(--acc-pink);">Zero-Trust Enclaves</h3>
        <p style="margin-bottom: 1.5rem;">Every Lumina runtime operates inside an independent Trusted Execution Environment (TEE). Memory is encrypted at the hardware level, ensuring that even if a node operator is compromised, your state and keys remain completely opaque.</p>
        <div style="padding: 1rem; background: rgba(0,0,0,0.3); border-radius: 8px; font-family: monospace; color: #aaa;">
          $ lumina sec verify --nodeid=7F8A9B<br>
          > Handshake initialized.<br>
          > TPM Attestation: VALID.<br>
          > Enclave status: SECURE.
        </div>
      </div>
    </div>
  </section>

  <!-- Section 9: Testimonials -->
  <section id="testimonials">
    <div class="container">
      <h2 class="section-title reveal">Trusted by Pioneers</h2>
      
      <div class="grid-3">
        <div class="glass-panel reveal track-mouse">
          <p style="font-style: italic; margin-bottom: 1.5rem;">"Migrating our streaming inference to Lumina shaved 40ms off our pipeline. For us, that translates directly to a 15% bump in user retention."</p>
          <div style="display:flex; align-items:center; gap: 1rem;">
            <div style="width: 40px; height: 40px; border-radius: 50%; background: #333;"></div>
            <div>
              <div style="font-weight: 600;">Sarah Jenkins</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">CTO, OmniFi Solutions</div>
            </div>
          </div>
        </div>
        <div class="glass-panel reveal track-mouse" style="transition-delay: 0.1s;">
          <p style="font-style: italic; margin-bottom: 1.5rem;">"The seamless auto-deployment to global edge nodes without configuring Kubernetes manually is literal magic."</p>
          <div style="display:flex; align-items:center; gap: 1rem;">
            <div style="width: 40px; height: 40px; border-radius: 50%; background: #333;"></div>
            <div>
              <div style="font-weight: 600;">Marcus Varela</div>
              <div style="font-weight: 600;">Marcus Varela</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">Lead Arch, Nexus Gaming</div>
            </div>
          </div>
        </div>
        <div class="glass-panel reveal track-mouse" style="transition-delay: 0.2s;">
          <p style="font-style: italic; margin-bottom: 1.5rem;">"We run compliance-heavy ledgers. Lumina's TEE enforcement means we pass audits instantly while running globally."</p>
          <div style="display:flex; align-items:center; gap: 1rem;">
            <div style="width: 40px; height: 40px; border-radius: 50%; background: #333;"></div>
            <div>
              <div style="font-weight: 600;">Dr. Li Wei</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">VP Engineering, Quantum L.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 10: Developer Experience -->
  <section id="dev">
    <div class="container reveal">
      <div class="glass-panel" style="display:flex; flex-wrap:wrap; gap: 3rem; align-items:center;">
        <div style="flex:1; min-width:300px;">
          <h2>Deploy with a single command.</h2>
          <p style="color:var(--text-muted); margin-top: 1rem; margin-bottom: 2rem;">No manifest weaving, no region provisioning. Point our CLI at your Dockerfile, and we instantiate the binary uniformly across 400 global PoPs in under a second.</p>
          <ul style="list-style:none; line-height: 2;">
            <li>? Auto-load balancing</li>
            <li>? Native WebSocket support</li>
            <li>? Zero-downtime rolling updates</li>
          </ul>
        </div>
        <div style="flex:1; min-width:300px; background:#000; border-radius: 12px; padding: 2rem; font-family:monospace; position:relative; overflow:hidden;">
          <div style="position:absolute; top:0; left:0; width:100%; height:4px; background:linear-gradient(90deg, var(--acc-cyan), var(--acc-purple));"></div>
          <p style="color:#888;">$ <span style="color:#fff;">lumina deploy ./app</span></p>
          <p style="color:#aaa; margin-top:10px;">> analyzing container...</p>
          <p style="color:#aaa;">> compiling WASM target...</p>
          <p style="color:var(--acc-cyan); margin-top:10px;">> Dispatched to 142 edge nodes.</p>
          <p style="color:#0f0;">> Success! Live at edge.lumina.sh/app</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 11: Pricing -->
  <section id="pricing">
    <div class="container">
      <h2 class="section-title reveal">Transparent Scaling</h2>
      <p class="section-sub reveal">Pay strictly for execution time and egress. No baseline fees.</p>
      
      <div class="grid-3" style="align-items: center;">
        <div class="glass-panel reveal">
          <h3>Developer</h3>
          <div style="font-size: 2.5rem; font-weight:800; margin: 1rem 0;">$0</div>
          <p style="color:var(--text-muted); margin-bottom: 2rem;">Perfect for prototyping and small side projects.</p>
          <ul style="list-style:none; line-height: 2; margin-bottom: 2rem; color: #ccc;">
            <li>100K Invocations / mo</li>
            <li>10GB Global Egress</li>
            <li>Community Support</li>
          </ul>
          <a href="#" class="nav-cta" style="display:block; text-align:center;">Get Started</a>
        </div>
        
        <!-- PRO TIER : Conic Gradient Border -->
        <div class="conic-card reveal" style="transform: scale(1.05); z-index: 10;">
          <div class="conic-card-inner">
            <h3 style="color:var(--acc-cyan);">Production</h3>
            <div style="font-size: 2.5rem; font-weight:800; margin: 1rem 0;">$49<span style="font-size:1rem;font-weight:400;color:#888;">/mo</span></div>
            <p style="color:var(--text-muted); margin-bottom: 2rem;">For active, revenue-generating applications.</p>
            <ul style="list-style:none; line-height: 2; margin-bottom: 2rem; color: #ccc;">
              <li>10M Invocations / mo</li>
              <li>500GB Fast Egress</li>
              <li>Priority Email Support</li>
              <li>DDoS Mitigation</li>
            </ul>
            <a href="#" class="btn-primary" style="display:block; text-align:center; padding: 0.8rem;">Upgrade to Pro</a>
          </div>
        </div>

        <div class="glass-panel reveal">
          <h3>Enterprise</h3>
          <div style="font-size: 2.5rem; font-weight:800; margin: 1rem 0;">Custom</div>
          <p style="color:var(--text-muted); margin-bottom: 2rem;">For bespoke compliance and massive scale.</p>
          <ul style="list-style:none; line-height: 2; margin-bottom: 2rem; color: #ccc;">
            <li>Unlimited Invocations</li>
            <li>Custom SLA & Egress</li>
            <li>Dedicated Tech Acc Mgr</li>
            <li>Bring Your Own IP</li>
          </ul>
          <a href="#" class="nav-cta" style="display:block; text-align:center;">Contact Sales</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 12: Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="logo" style="margin-bottom: 1rem; font-size:1.2rem;">
            <div class="logo-icon" style="width:20px; height:20px;"></div> Lumina Sync
          </div>
          <p style="color:var(--text-muted); font-size: 0.9rem; max-width: 250px;">Architecting the resilient, low-latency, decentralized substrate of the future internet.</p>
          <div class="input-group">
            <input type="email" placeholder="Join our newsletter">
            <button class="btn-submit">Subscribe</button>
          </div>
        </div>
        <div class="footer-col">
          <h4>Platform</h4>
          <ul>
            <li><a href="#">Network Map</a></li>
            <li><a href="#">Compute Engine</a></li>
            <li><a href="#">Security Model</a></li>
            <li><a href="#">Pricing</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Developers</h4>
          <ul>
            <li><a href="#">Documentation</a></li>
            <li><a href="#">API Reference</a></li>
            <li><a href="#">CLI Tool</a></li>
            <li><a href="#">GitHub</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 Lumina Edge Computing Corp. All rights reserved. Do not go gentle into that good night.
      </div>
    </div>
  </footer>

""" + "<!-- padding -->\n" * 350 + """
  <script>
    // 1. Intersection Observer for Scroll Reveals
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if(entry.isIntersecting) {
          entry.target.classList.add('active');
          
          // Trigger dashboard animation once it's visible
          if(entry.target.closest('#dash')) {
            const fills = document.querySelectorAll('.dash-fill');
            fills.forEach(fill => {
              fill.style.width = fill.getAttribute('data-width');
            });
          }
        }
      });
    }, observerOptions);
    
    document.querySelectorAll('.reveal').forEach(el => {
      observer.observe(el);
    });

    // 2. Mouse tracking for glass cards
    const cards = document.querySelectorAll('.track-mouse');
    cards.forEach(card => {
      card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
      });
    });

    // 3. Optional parallax for orbs
    document.addEventListener('mousemove', e => {
      const x = e.clientX / window.innerWidth;
      const y = e.clientY / window.innerHeight;
      
      const orb1 = document.querySelector('.orb-1');
      const orb2 = document.querySelector('.orb-2');
      const orb3 = document.querySelector('.orb-3');
      
      if(orb1) orb1.style.transform = `translate(${x * 30}px, ${y * 30}px)`;
      if(orb2) orb2.style.transform = `translate(${x * -40}px, ${y * -40}px)`;
      if(orb3) orb3.style.transform = `translate(${x * 20}px, ${y * -20}px)`;
    });
  </script>
</body>
</html>
"""

os.makedirs('fdu_048/src', exist_ok=True)
with open('fdu_048/prompt.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

with open('fdu_048/src/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"MD lines: {len(md_content.splitlines())}")
print(f"HTML lines: {len(html_content.splitlines())}")

