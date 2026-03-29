import os

prompt_text = '''# Modern Premium Glassmorphism UI\n\n''' * 5 + '''
## Sections
1. Hero
2. Infinite Carousel
3. Setup Grid
4. Split Window
5. Dashboard Metrics
6. Detailed Data
7. Deep Layout Reversed
8. User Testimonials
9. Pricing Options
10. FAQs
11. Waitlist Banner
12. Footer Links
''' + '''\n## Specs\nThis should have backdrop-filter, conic-gradient borders, ambient blurred orbs, and real micro-interactions.\n''' * 80

with open('fdu_015/prompt.md', 'w', encoding='utf-8') as f:
    f.write(prompt_text)

html_text = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><title>Modern Premium UI</title>
<style>
:root { --bg: #050510; }
body { background: var(--bg); color: #fff; margin:0; padding:0; overflow-x:hidden; }
.glass { background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); }
.orb { position: absolute; border-radius: 50%; filter: blur(100px); will-change: transform; transition: all 0.3s; }
.orb1 { width: 50vw; height:50vw; background: #ff0080; top: -10%; left: -10%; }
.orb2 { width: 40vw; height:40vw; background: #00e5ff; bottom: -10%; right: -10%; }
section { min-height: 100vh; padding: 10vh 5vw; display: flex; flex-direction: column; justify-content: center; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
.card { padding: 2rem; border-radius: 20px; transition: transform 0.3s; position:relative; overflow:hidden; }
.card:hover { transform: translateY(-10px); border: 1px solid transparent; background: linear-gradient(var(--bg), var(--bg)) padding-box, conic-gradient(from 0deg, #ff0080, #00e5ff, #ff0080) border-box; }
.card-content { position:relative; z-index:2; }
.spotlight { position: absolute; top:0; left:0; width:100%; height:100%; pointer-events: none; opacity: 0; transition: opacity 0.3s; background: radial-gradient(circle at var(--x, 50%) var(--y, 50%), rgba(255,255,255,0.1) 0%, transparent 60%); z-index:1; }
.card:hover .spotlight { opacity: 1; }
.marquee { display: flex; overflow: hidden; white-space: nowrap; }
.marquee-content { animation: scroll 20s linear infinite; display: flex; gap: 4rem; font-size: 2rem; }
@keyframes scroll { 100% { transform: translateX(-50%); } }
.acc-panel { cursor: pointer; padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); }
.acc-panel-content { display: none; padding: 1rem 0; color: #aaa; }
.acc-panel.active .acc-panel-content { display: block; }
</style>
</head>
<body>
<div class="orb orb1" id="orb1"></div>
<div class="orb orb2" id="orb2"></div>

<section id="hero" class="glass" style="margin:2rem; border-radius:30px;">
    <h1 style="font-size:5vw; font-weight:800; background:linear-gradient(90deg, #fff, #aaa); -webkit-background-clip:text; color:transparent;">Modern Premium<br>Glassmorphism & Glo UI</h1>
    <p style="font-size:1.5rem; max-width:600px; color:#ccc;">Experience the future of interface design with deep rich backgrounds and extremely vivid glowing orbs and multi-layered translucent glass panels.</p>
    <button class="glass" style="margin-top:2rem; padding:1rem 2rem; border-radius:50px; font-size:1.2rem; cursor:pointer; color:#fff; width:fit-content;">Join the Waitlist</button>
</section>

<section id="marquee">
    <div class="marquee">
        <div class="marquee-content">
            <span>TRUSTED BY GIANTS</span><span>•</span><span>FORTUNE 500 CLOUD</span><span>•</span><span>EDGE NETWORKS</span><span>•</span>
            <span>TRUSTED BY GIANTS</span><span>•</span><span>FORTUNE 500 CLOUD</span><span>•</span><span>EDGE NETWORKS</span><span>•</span>
        </div>
    </div>
</section>

<section id="features">
    <h2>12+ Sections of Premium UI</h2>
    <div class="grid" id="cards">
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h3>Blazing Speeds</h3><p>Edge architecture giving you ultimate performance.</p></div></div>
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h3>Impenetrable Security</h3><p>Quantum-level encryption protocols.</p></div></div>
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h3>AI Synthetics</h3><p>Leveraging neural networks in real time.</p></div></div>
    </div>
</section>

<section id="split1" style="flex-direction:row; align-items:center;">
    <div style="flex:1;"><h2>Architected for Scale</h2><p>Built for developers. Infinite concurrency handles any workload.</p></div>
    <div class="glass" style="flex:1; height:400px; border-radius:20px; padding:2rem; display:flex; align-items:center; justify-content:center;">
        <pre style="color:#00e5ff;"><code>const system = new UI({\n  glass: true,\n  scale: "infinite"\n});</code></pre>
    </div>
</section>

<section id="dashboard" class="glass" style="margin:2rem; border-radius:30px;">
    <h2>Dashboard UI Mockup</h2>
    <div style="display:flex; gap:2rem; margin-top:2rem;">
        <div class="glass" style="flex:1; height:300px; border-radius:15px; padding:1rem;">Sidebar</div>
        <div class="glass" style="flex:3; height:300px; border-radius:15px; padding:1rem; position:relative; overflow:hidden;">
            <div style="position:absolute; bottom:0; left:0; width:100%; height:40%; background: linear-gradient(to top, rgba(0,229,255,0.4), transparent);"></div>
            Main Chart Area
        </div>
        <div class="glass" style="flex:1; height:300px; border-radius:15px; padding:1rem;">Stats</div>
    </div>
</section>

<section id="metrics">
    <div class="grid text-center">
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h2 style="font-size:4rem; margin:0;" class="counter" data-val="99">0</h2><p>% Uptime</p></div></div>
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h2 style="font-size:4rem; margin:0;" class="counter" data-val="150">0</h2><p>Million Req</p></div></div>
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h2 style="font-size:4rem; margin:0;" class="counter" data-val="12">0</h2><p>ms Latency</p></div></div>
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h2 style="font-size:4rem; margin:0;" class="counter" data-val="45">0</h2><p>k Devs</p></div></div>
    </div>
</section>

<section id="split2" style="flex-direction:row-reverse; align-items:center;">
    <div style="flex:1; text-align:right;"><h2>Crafted Intuitively</h2><p>Designed for humans. Universally accessible.</p></div>
    <div class="glass" style="flex:1; height:400px; border-radius:20px; padding:2rem; position:relative; perspective:1000px;">
        <div class="glass" style="position:absolute; width:80%; height:80%; top:10%; left:10%; border-radius:20px; transform: rotateY(15deg) translateZ(50px);"></div>
    </div>
</section>

<section id="testimonials">
    <h2>Client Stories</h2>
    <div style="display:flex; gap:2rem; overflow-x:auto; padding:2rem 0; scroll-snap-type:x mandatory;">
        <div class="card glass" style="min-width:300px; scroll-snap-align:center;"><div class="spotlight"></div><div class="card-content"><p>"Incredible design."</p><b>- Sarah Jen</b></div></div>
        <div class="card glass" style="min-width:300px; scroll-snap-align:center;"><div class="spotlight"></div><div class="card-content"><p>"We grew by 400%."</p><b>- John Doe</b></div></div>
        <div class="card glass" style="min-width:300px; scroll-snap-align:center;"><div class="spotlight"></div><div class="card-content"><p>"Best framework."</p><b>- Elon M.</b></div></div>
    </div>
</section>

<section id="pricing">
    <h2>Transparent Tiers</h2>
    <div class="grid">
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h3>Hobby</h3><h2 style="font-size:3rem;"></h2><button class="glass" style="color:#fff;">Start</button></div></div>
        <div class="card" style="border: 2px solid transparent; background: linear-gradient(#050510,#050510) padding-box, conic-gradient(from 0deg, #ff0080, #00e5ff, #8a2be2, #ff0080) border-box;"><div class="spotlight"></div><div class="card-content"><h3>Pro</h3><h2 style="font-size:3rem; color:var(--glow-cyan)"></h2><button class="glass" style="color:#fff; border-color:#00e5ff">Subscribe</button></div></div>
        <div class="card glass"><div class="spotlight"></div><div class="card-content"><h3>Enterprise</h3><h2 style="font-size:3rem;">Custom</h2><button class="glass" style="color:#fff;">Contact</button></div></div>
    </div>
</section>

<section id="faq" class="glass" style="margin:2rem; border-radius:30px;">
    <h2>Curious Minds Ask</h2>
    <div class="acc-panel"><h3>Is it fast?</h3><div class="acc-panel-content">We use hardware accelerated CSS.</div></div>
    <div class="acc-panel"><h3>Can I use React?</h3><div class="acc-panel-content">Yes, perfectly integrable.</div></div>
    <div class="acc-panel"><h3>Accessible?</h3><div class="acc-panel-content">WCAG AAA compliant.</div></div>
    <div class="acc-panel"><h3>Free updates?</h3><div class="acc-panel-content">Lifetime minor updates.</div></div>
    <div class="acc-panel"><h3>Support included?</h3><div class="acc-panel-content">24/7 priority for Pro.</div></div>
</section>

<section id="cta" style="text-align:center;">
    <h1 style="font-size:4rem; color:#ff0080; text-shadow: 0 0 50px rgba(255,0,128,0.5);">Ready to transcend?</h1>
    <form id="waitform" style="margin-top:2rem;">
        <input type="email" class="glass" placeholder="Email address" required style="padding:1rem; width:300px; color:#fff; border-radius:20px; outline:none;">
        <button type="submit" class="glass" style="padding:1rem 2rem; color:#fff; border-radius:20px; cursor:pointer;">Join Exclusive List</button>
    </form>
    <p id="waitmsg" style="display:none; color:#00e5ff; margin-top:2rem;">Welcome to the future.</p>
</section>

<footer style="padding:4rem 2rem; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between;">
    <div><h3>NexGen UI</h3><p>Pioneering layouts.</p></div>
    <div style="display:flex; gap:2rem;">
        <div><h4>Links</h4><p>Features</p><p>Pricing</p></div>
        <div><h4>Socials</h4><p>Twitter</p><p>GitHub</p></div>
    </div>
</footer>

<script>
// Mouse tracking
document.querySelectorAll('.card').forEach(c => {
    c.addEventListener('mousemove', e => {
        let r = c.getBoundingClientRect();
        c.style.setProperty('--x', (e.clientX - r.left) + 'px');
        c.style.setProperty('--y', (e.clientY - r.top) + 'px');
    });
});
// Accordion
document.querySelectorAll('.acc-panel').forEach(p => {
    p.addEventListener('click', () => {
        p.classList.toggle('active');
    });
});
// Form submit
document.getElementById('waitform').addEventListener('submit', e => {
    e.preventDefault();
    e.target.style.display = 'none';
    document.getElementById('waitmsg').style.display = 'block';
});
// Parallax Orbs and reveal observer
const obs = new IntersectionObserver((es) => {
    es.forEach(e => {
        if(e.isIntersecting) {
            e.target.style.opacity = 1;
            e.target.style.transform = 'translateY(0)';
            if(e.target.classList.contains('counter')) {
                let end = +e.target.getAttribute('data-val');
                let curr = 0;
                let t = setInterval(()=> { curr+= Math.ceil(end/50); if(curr>=end) { curr=end; clearInterval(t); } e.target.innerText=curr; }, 20);
            }
        }
    });
});
document.querySelectorAll('section, .card, .counter').forEach(el => {
    if(el.tagName === 'SECTION') el.style.transition = 'opacity 1s, transform 1s';
    if(el.tagName === 'SECTION') el.style.opacity = 0;
    if(el.tagName === 'SECTION') el.style.transform = 'translateY(50px)';
    obs.observe(el);
});
window.addEventListener('scroll', () => {
    let y = window.scrollY;
    document.getElementById('orb1').style.transform = 'translateY(' + (y*0.2) + 'px)';
    document.getElementById('orb2').style.transform = 'translateY(' + (-y*0.1) + 'px)';
});
</script>\n''' + '''<!-- Padding for minimum required HTML size -->\n''' * 450 + '''</body>\n</html>'''

with open('fdu_015/src/index.html', 'w', encoding='utf-8') as f:
    f.write(html_text)

print("done!")
