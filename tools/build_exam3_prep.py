#!/usr/bin/env python3
"""Builds exam3-prep.html: scope map, two-day plan, question types, last-hour facts, checklists.
Run from the repo root after index.html exists:  python3 tools/build_exam3_prep.py"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
base_css = re.search(r"<style>(.*?)</style>", idx, re.S).group(1)
base_css = re.sub(r"/\*PQ-CSS-BEGIN\*/.*?/\*PQ-CSS-END\*/", "", base_css, flags=re.S)
fonts = re.search(r"(<link[^>]*fonts[^>]*>\s*)+", idx).group(0)

G = "index.html"
Q = "quiz-review.html"

css = base_css + """
  .ex-shell{max-width:900px;margin:0 auto;padding:20px 16px 80px;}
  .ex-shell .hero{margin-bottom:18px;}
  .ck{display:flex;gap:10px;align-items:flex-start;margin:0 0 7px;font-size:16px;line-height:1.45;}
  .ck input{margin-top:5px;accent-color:var(--accent);flex:none;width:17px;height:17px;}
  .ck span{min-width:0;}
  .ck input:checked + span{color:var(--ink-faint);text-decoration:line-through;text-decoration-color:var(--line);}
  .ck-bar{height:6px;border-radius:999px;background:var(--line-soft);overflow:hidden;margin:4px 0 12px;}
  .ck-bar > i{display:block;height:100%;width:0;background:var(--good);transition:width .25s;}
  .plan{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:12px 0;}
  .plan .box{margin:0;}
  .tl{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink-faint);}
  .go{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:12.5px;font-weight:600;padding:7px 13px;border-radius:9px;border:1px solid var(--accent);background:var(--accent);color:#fff;text-decoration:none;margin:2px 6px 2px 0;}
  :root[data-theme="dark"] .go{color:#10131c;}
  @media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .go{color:#10131c;}}
  .go.alt,:root[data-theme="dark"] .go.alt{background:transparent!important;color:var(--accent-ink)!important;}
  @media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .go.alt{background:transparent!important;color:var(--accent-ink)!important;}}
  .facts{columns:2 280px;column-gap:26px;}
  .facts .ck{break-inside:avoid;}
  td a, li a{overflow-wrap:anywhere;}
"""

def ck(key, html):
    return '<label class="ck"><input type="checkbox" data-k="%s"><span>%s</span></label>' % (key, html)

def box(kind, head, body):
    return '<div class="box %s"><div class="box-head">%s</div>%s</div>' % (kind, head, body)

def L(unit):
    return '<a href="%s#%s">%s</a>' % (G, unit, "guide")

def P(topic):
    return '<a href="%s#t-%s">practice</a>' % (Q, topic)

scope_rows = [
    ("L21", "Reactions and rates: rate, average vs instantaneous, collision model; Rec 14", "unit12", "kinetics"),
    ("L22", "Rate laws, integrated laws, Arrhenius, energy diagrams, mechanisms; Rec 14&ndash;15", "unit12", "kinetics"),
    ("L23", "Thermodynamics: spontaneity, &Delta;G = &Delta;H &minus; T&Delta;S, free energy as work; Rec 16 (heat, work, first law, enthalpy, entropy)", "unit13", "thermo"),
    ("L24", "Chemical equilibrium: K, Q vs K, RICE, &Delta;G&deg; and K, van&rsquo;t Hoff; Rec 17", "unit14", "equil"),
    ("L25", "Catalysis and ammonia production: Haber&ndash;Bosch, Sabatier volcano; Rec 17", "unit15", "catalysis"),
    ("L26", "Solutions: &Delta;H<sub>soln</sub> in three steps, like dissolves like, concentration units; Rec 19", "unit16", "solutions"),
    ("L27", "Acids and bases: conjugate pairs, pH, K<sub>a</sub>, titration, buffers; Rec 19", "unit17", "acidbase"),
    ("L28", "Solubility product and complexation: K<sub>sp</sub>, Q, common ion, K<sub>f</sub>; Rec 20", "unit18", "ksp"),
]
rows = "".join(
    '<tr><td><b>%s</b></td><td class="wrap">%s</td><td>%s &middot; %s</td></tr>' % (l, t, L(u), P(p)) for l, t, u, p in scope_rows)

types = [
    ("Rate law from initial-rate data", "ratios of rates vs ratios of concentrations; overall order; k with units", "unit12", "kinetics", "Rec 14, Quiz 7"),
    ("Order from a plot or from half-life", "[A], ln[A], 1/[A] vs t; t<sub>1/2</sub> = ln 2/k for first order; units of k", "unit12", "kinetics", "L22, Rec 15"),
    ("Arrhenius plot and activation energy", "ln k vs 1/T, slope = &minus;E<sub>a</sub>/R; label lines for E<sub>a</sub> and for a catalyst", "unit12", "kinetics", "Quiz 7"),
    ("Energy diagram", "E<sub>a</sub>, &Delta;E, activated complex; catalyst lowers E<sub>a</sub> only", "unit12", "kinetics", "L22, Rec 14"),
    ("Mechanism and rate-limiting step", "slow step sets the rate law; intermediates cancel; sum the steps", "unit12", "kinetics", "Rec 14&ndash;15"),
    ("Spontaneity and the crossover temperature", "sign table; T = &Delta;H/&Delta;S; kJ vs J/K; &Delta;H&deg; from &Delta;H&deg;<sub>f</sub>", "unit13", "thermo", "L23, Rec 16"),
    ("First law, work, entropy", "W = &minus;P&Delta;V sign; &Delta;E = Q + W; entropy ordering; 2nd and 3rd law in a sentence", "unit13", "laws", "Rec 16"),
    ("K, Q and the direction of a reaction", "write K; Q vs K; RICE table; Le Ch&acirc;telier (concentration, pressure, temperature)", "unit14", "equil", "Rec 17, Quiz 8"),
    ("K, &Delta;G&deg; and temperature", "&Delta;G&deg; = &minus;RT ln K; van&rsquo;t Hoff; exothermic K falls on heating", "unit14", "equil", "Rec 17"),
    ("Catalysts", "what changes (E<sub>a</sub>) and what does not (K); homogeneous vs heterogeneous; Sabatier volcano; Haber&ndash;Bosch conditions", "unit15", "catalysis", "L25, Rec 17, Quiz 8"),
    ("Solutions", "three-step &Delta;H<sub>soln</sub>; polar vs non-polar; molality vs molarity; ppm", "unit16", "solutions", "L26, Rec 19"),
    ("Acids and bases", "conjugate pairs; pH of strong and weak acids; K<sub>a</sub> from pH; Henderson&ndash;Hasselbalch; titration curve", "unit17", "acidbase", "L27, Rec 19"),
    ("Solubility product", "K<sub>sp</sub> expression; molar solubility; Q vs K<sub>sp</sub>; common ion; pH effect; complexation", "unit18", "ksp", "L28, Rec 20"),
]
trows = "".join(
    '<tr><td><b>%s</b></td><td class="wrap">%s</td><td class="wrap">%s</td><td>%s &middot; %s</td></tr>' % (a, b, e, L(u), P(p)) for a, b, u, p, e in types)

facts_a = [
    "Rate = &minus;(1/a)d[A]/dt; rate law v = k[A]<sup>&alpha;</sup>[B]<sup>&beta;</sup> with exponents from <b>experiment</b>, not from coefficients (unless elementary)",
    "Zeroth: [A] = [A]<sub>0</sub> &minus; kt (k in M/s); first: ln[A] = ln[A]<sub>0</sub> &minus; kt (s<sup>&minus;1</sup>); second: 1/[A] = 1/[A]<sub>0</sub> + kt (M<sup>&minus;1</sup>s<sup>&minus;1</sup>); only the 2nd order line has slope +k",
    "t<sub>1/2</sub> = ln 2/k for first order (independent of [A]<sub>0</sub>)",
    "Arrhenius: k = Ae<sup>&minus;E<sub>a</sub>/RT</sup>; ln k vs 1/T slope = &minus;E<sub>a</sub>/R; steeper = larger E<sub>a</sub>; R = 8.314 J/(mol&middot;K) so E<sub>a</sub> in J",
    "Catalyst: lower E<sub>a</sub> (forward and reverse), same &Delta;E, &Delta;G, K; not consumed",
    "Slow step sets the rate law; intermediates cancel from the overall equation",
    "&Delta;G = &Delta;H &minus; T&Delta;S: (&minus;,+) always, (+,&minus;) never, (&minus;,&minus;) low T, (+,+) high T; crossover T = &Delta;H/&Delta;S; spontaneous &ne; fast",
    "W = &minus;P&Delta;V (work on the system is +); &Delta;E = Q + W; &Delta;H = Q at constant P; H, S, G, U are state functions, Q and W path functions",
    "&Delta;H&deg;<sub>rxn</sub> = &Sigma;&Delta;H&deg;<sub>f</sub>(products) &minus; &Sigma;&Delta;H&deg;<sub>f</sub>(reactants); elements = 0",
    "Entropy: crystal &lt; amorphous &lt; liquid &lt; gas; &Delta;S<sub>universe</sub> &ge; 0; 3rd law: perfect crystal at 0 K",
]
facts_b = [
    "K = products over reactants (coefficients as exponents, no units, solids and liquids left out); two steps: K<sub>1</sub>K<sub>2</sub>; reverse: 1/K",
    "Q &lt; K goes right, Q &gt; K goes left, Q = K equilibrium (&Delta;G = 0); &Delta;G = &Delta;G&deg; + RT ln Q; &Delta;G&deg; = &minus;RT ln K",
    "Van&rsquo;t Hoff: ln K = &minus;&Delta;H&deg;/RT + &Delta;S&deg;/R; exothermic: K falls as T rises; only T changes K",
    "Le Ch&acirc;telier: add reactant &rarr; right; compress &rarr; fewer moles of gas; heat &rarr; endothermic direction; catalyst: no shift",
    "Haber&ndash;Bosch: Fe, 400&ndash;500 &deg;C, high P, liquefy NH<sub>3</sub>, recycle N<sub>2</sub> + H<sub>2</sub>; H<sub>2</sub> from CH<sub>4</sub> + H<sub>2</sub>O &rarr; CO + 3H<sub>2</sub>",
    "Homogeneous = same phase as reactants; heterogeneous = different phase (solid); Sabatier: intermediate binding is best (volcano)",
    "&Delta;H<sub>soln</sub> = (A&ndash;A broken +) + (B&ndash;B broken +) + (A&ndash;B formed &minus;); &Delta;S<sub>soln</sub> &gt; 0; molality = mol/kg <b>solvent</b>; only molarity depends on T",
    "pH = &minus;log[H<sub>3</sub>O<sup>+</sup>]; pH + pOH = 14; K<sub>w</sub> = 10<sup>&minus;14</sup>; K<sub>a</sub>K<sub>b</sub> = K<sub>w</sub>; small pK<sub>a</sub> = strong acid; stronger acid = weaker conjugate base",
    "pH = pK<sub>a</sub> + log([A<sup>&minus;</sup>]/[HA]); midpoint of a weak-acid titration pH = pK<sub>a</sub>; equivalence pH: strong/strong 7, weak acid &gt; 7, weak base &lt; 7",
    "K<sub>sp</sub> (solid left out): AB &rarr; x&sup2;, AB<sub>2</sub> &rarr; 4x&sup3;, A<sub>3</sub>B<sub>2</sub> &rarr; 108x<sup>5</sup>; Q &gt; K<sub>sp</sub> precipitates; common ion lowers solubility; acid on a basic anion or a ligand raises it; K<sub>f</sub> = K<sub>1</sub>K<sub>2</sub>&hellip;",
]
fa = "".join(ck("fa%d" % i, t) for i, t in enumerate(facts_a))
fb = "".join(ck("fb%d" % i, t) for i, t in enumerate(facts_b))

plan1 = [
    ("p1a", "<b>Unit 12 kinetics</b>: read, then the 17 &ldquo;Check yourself&rdquo; questions; redo rate-law, half-life and Arrhenius without looking", "90 min"),
    ("p1b", "<b>Unit 13 thermodynamics</b> (Rec 16 basics first, then &Delta;G) and the questions", "60 min"),
    ("p1c", "<b>Unit 14 equilibrium</b>: K, Q, RICE, van&rsquo;t Hoff, Le Ch&acirc;telier and the questions", "75 min"),
    ("p1d", "<b>Unit 15 catalysis</b> (short) and the questions", "30 min"),
]
plan2 = [
    ("p2a", "<b>Unit 16 solutions</b> and the questions", "35 min"),
    ("p2b", "<b>Unit 17 acids and bases</b>: pH arithmetic, K<sub>a</sub>, titration curve, Henderson&ndash;Hasselbalch and the questions", "80 min"),
    ("p2c", "<b>Unit 18 solubility product</b> and the questions (do all three molar-solubility types by hand)", "50 min"),
    ("p2d", "<b>Exam 3 mock</b> on the Quiz Review page (14 questions, 50 min, then read every solution)", "75 min"),
    ("p2e", "Retry list in &ldquo;My practice&rdquo;: redo every question you missed or peeked at", "40 min"),
]
plan3 = [
    ("p3a", "If the rules allow an aid sheet: write one from the cheat codes and the formula sheet (copying is a study session)", "40 min"),
    ("p3b", "Read the &ldquo;last-hour facts&rdquo; below out loud, tick each one only if you can say it without looking", "30 min"),
    ("p3c", "Re-read <a href='%s#traps'>Exam traps</a> and the &ldquo;typical slips&rdquo; for kinetics, equilibrium, acid&ndash;base" % G, "20 min"),
    ("p3d", "Calculator: <b>log, ln, e<sup>x</sup>, 10<sup>x</sup></b> keys checked (this exam is logs and exponentials); constants and periodic table packed", "&mdash;"),
]
def plist(items):
    return "".join('<label class="ck"><input type="checkbox" data-k="%s"><span>%s <span class="tl">&middot; %s</span></span></label>' % (k, t, m) for k, t, m in items)

body = """
<div class="ex-shell">
  <header class="hero">
    <div class="hero-eyebrow"><span class="dot"></span> MIT 3.091 &middot; Fall 2026 &middot; Exam 3 study guide</div>
    <h1>Exam 3 Prep: <em>Lectures 21&ndash;28 on one page</em></h1>
    <p class="sub">Scope: <b>Lectures 21&ndash;28</b> (reactions and rates through solubility product) with <b>Recitations 14&ndash;20</b>. A plan, what the exam is likely to ask, the facts to know cold, and links to the explanations and the practice questions. Everything on this page links into the Field Guide (Units 12&ndash;18) and the Quiz Review page.</p>
    <div class="hero-stats"><a class="go" href="%(Q)s#pq-quiz">&#9733; Start the Exam 3 mock</a><a class="go alt" href="%(G)s#unit12">Start the Field Guide at Unit 12</a><a class="go alt" href="%(Q)s">All practice questions</a></div>
  </header>

  <h3 class="topic" style="--c:var(--warn)">What I could and could not get</h3>
  <div class="box trap">
    <div class="box-head">Read this first</div>
    <ul style="margin-bottom:0">
      <li><b>In the guide:</b> L21&ndash;L28 slide by slide and Recitations 14, 15, 16, 17, 19 and 20 (Units 12&ndash;18). Items the slides do not state are tagged <span class="pill" style="--c:var(--ink-soft);--c-soft:var(--line-soft)">extra</span>.</li>
      <li><b>Not available to me:</b> <b>Recitations 13 and 18</b>, the problem sets for this stretch, and any <b>past Exam 3</b>. The Drive folder only has the Fall 2024 quizzes, so the &ldquo;likely question types&rdquo; below come from <b>2024 Quizzes 7, 8 and 9</b>, the recitation problems and the practice questions, not from a real exam. <b>Phase diagrams (2024 Quiz 9) are not in L21&ndash;L28</b> as far as the slides I have show; if your exam includes them I have not covered them.</li>
      <li><b>Check this year&rsquo;s rules</b> on aid sheets and equation sheets; I do not know them.</li>
      <li><b>Slide errors to know:</b> Rec 17 prints van&rsquo;t Hoff with &Delta;S&deg;/T (it should be &Delta;S&deg;/R); Rec 19 calls K<sub>w</sub> a &ldquo;solubility product&rdquo; (it is the water ion product); the L24 slide lists K = 2.7&times;10<sup>8</sup> for ammonia at 300 K while Unit 13&rsquo;s &Delta;G&deg; gives about 5&times;10<sup>5</sup>. Use the data the question gives.</li>
    </ul>
  </div>

  <h3 class="topic" style="--c:var(--accent)">The plan</h3>
  <p>About 8&ndash;9 hours in total; if you only have <b>3 hours</b>, do this order: the last-hour facts (30 min), the <b>Exam 3 mock</b> (50 min), then re-read the solutions of everything you missed and the matching &ldquo;typical slips&rdquo; (the rest). Rule for every block: <b>cover the solutions, answer on paper, then check</b>.</p>
  <div class="plan">
    %(box1)s
    %(box2)s
    %(box3)s
  </div>

  <h3 class="topic" style="--c:var(--accent)">What the exam is likely to ask</h3>
  <p>Built from the 2024 Quizzes 7&ndash;9 (kinetics and catalysis, equilibrium, and the Sabatier / hemoglobin questions), the recitation problems and the lecture slides. For each type: where to read it and where to practise it.</p>
  <div class="tscroll"><table class="data"><thead><tr><th>Type</th><th class="wrap">What they ask</th><th class="wrap">Seen in</th><th>Go to</th></tr></thead><tbody>%(trows)s</tbody></table></div>

  <h3 class="topic" style="--c:var(--accent)">Coverage map</h3>
  <div class="tscroll"><table class="data"><thead><tr><th>Lecture</th><th class="wrap">Topic</th><th>Go to</th></tr></thead><tbody>%(rows)s</tbody></table></div>

  <h3 class="topic" style="--c:var(--accent)">Last-hour facts: tick only what you can say without looking</h3>
  <div class="ck-bar"><i id="fbar"></i></div>
  <div class="facts">%(fa)s</div>
  <div class="facts">%(fb)s</div>

  <h3 class="topic" style="--c:var(--warn)">The twelve ways people lose points on this exam</h3>
  <ol>
    <li>Using the <b>coefficients</b> as rate-law exponents for a reaction that is not a single step.</li>
    <li>Forgetting that only the <b>second-order</b> plot (1/[A] vs t) has slope <b>+k</b>; or steeper Arrhenius line = &ldquo;faster&rdquo; (it means larger E<sub>a</sub>).</li>
    <li>Using kJ with R in J, or &Delta;S in J/K with &Delta;H in kJ; Celsius instead of kelvin.</li>
    <li>Thinking &Delta;G &lt; 0 means fast, or that a catalyst changes K, &Delta;G or the equilibrium yield.</li>
    <li>Getting the sign of W wrong (work done <em>on</em> the system is +).</li>
    <li>Writing K as reactants over products, including solids, or comparing Q and K the wrong way round.</li>
    <li>Forgetting that an exothermic reaction has a <b>smaller K at higher T</b> (van&rsquo;t Hoff).</li>
    <li>pH arithmetic: sign of the log, pH + pOH = 14 only at 25 &deg;C, lower pK<sub>a</sub> = <b>stronger</b> acid.</li>
    <li>Henderson&ndash;Hasselbalch upside down (it is [A<sup>&minus;</sup>]/[HA], base over acid); assuming every equivalence point is pH 7.</li>
    <li>Mixing molarity (L of solution) with molality (kg of solvent).</li>
    <li>In K<sub>sp</sub> problems: reporting x instead of [ion] (Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub>: 3x and 2x), forgetting to halve concentrations on mixing, or comparing K<sub>sp</sub> across different formula types.</li>
    <li>Not giving a <b>reason</b> in &ldquo;briefly explain&rdquo; parts, and eliminating units.</li>
  </ol>

  <h3 class="topic" style="--c:var(--accent)">Morning of the exam</h3>
  %(morning)s
</div>
""" % dict(
    Q=Q, G=G,
    box1=box("cheat", "Day 1 &middot; kinetics, thermodynamics, equilibrium", plist(plan1)),
    box2=box("cheat", "Day 2 &middot; solutions, acids, solubility, mock", plist(plan2)),
    box3=box("cheat", "Night before &middot; morning", plist(plan3)),
    trows=trows, rows=rows, fa=fa, fb=fb,
    morning="".join(ck("m%d" % i, t) for i, t in enumerate([
        "Aid sheet or equation sheet as the rules allow; name written if required",
        "Calculator checked: ln, log, e<sup>x</sup>, 10<sup>x</sup>, scientific notation entry; constants (R, K<sub>w</sub>) on your sheet",
        "Eat; read only the first three items of the facts list, then stop",
        "In the exam: start with the 1-point recall parts, write the formula and numbers even if unsure, check units on every line",
    ])))

js = """
(function(){
  var KEY='3091-exam3-prep-v1',st={};
  try{st=JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){st={};}
  var boxes=document.querySelectorAll('input[data-k]');
  function bar(){var f=document.querySelectorAll('input[data-k^="fa"],input[data-k^="fb"]'),n=0;
    Array.prototype.forEach.call(f,function(b){if(b.checked)n++;});
    var el=document.getElementById('fbar');if(el)el.style.width=Math.round(100*n/Math.max(1,f.length))+'%';}
  Array.prototype.forEach.call(boxes,function(b){
    b.checked=!!st[b.getAttribute('data-k')];
    b.addEventListener('change',function(){st[b.getAttribute('data-k')]=b.checked;try{localStorage.setItem(KEY,JSON.stringify(st));}catch(e){}bar();});
  });
  bar();
})();
"""
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>3.091 Exam 3 Prep</title>\n' + fonts + '<style>' + css + '</style>\n</head>\n<body>\n' + body + '<script>' + js + '</script>\n</body>\n</html>\n')
open(os.path.join(ROOT, "exam3-prep.html"), "w", encoding="utf-8").write(page)
print("wrote exam3-prep.html", len(page))
