#!/usr/bin/env python3
"""Builds exam2-prep.html: scope map, two-day plan, question types, last-hour facts, checklists.
Run from the repo root after index.html exists:  python3 tools/build_exam2_prep.py"""
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
    ("L10", "Properties of covalent compounds; % ionic, dipoles; Rec 7", "unit5", "lewis"),
    ("L11", "VSEPR; Rec 8", "unit5", "vsepr"),
    ("L12", "Hybridization, molecular orbitals; Rec 9", "unit6", "hybmo"),
    ("L13", "Intermolecular forces; Rec 9.5", "unit7", "imf"),
    ("L14", "Metals, bands, work function", "unit8", "bands"),
    ("L15", "Semiconductors, doping, compound semiconductors; Rec 10", "unit8", "bands"),
    ("L16", "Crystallography I: lattice, Bravais, cubic; Rec 11", "unit9", "lattice"),
    ("L17", "Crystallography II: holes, Miller, d-spacing, Bragg", "unit9", "miller"),
    ("L18", "Diffraction, point &amp; line defects; Rec 12", "unit10", "defects"),
    ("L19", "Noncrystalline solids: glass, polymers", "unit10", "defects"),
    ("L20", "Diffusion", "unit11", "diffusion"),
]
rows = "".join(
    '<tr><td><b>%s</b></td><td class="wrap">%s</td><td>%s &middot; %s</td></tr>' % (l, t, L(u), P(p)) for l, t, u, p in scope_rows)

types = [
    ("VSEPR chain", "Lewis &rarr; AXE &rarr; shape &rarr; bond angles &rarr; polar? (SF<sub>4</sub>, XeF<sub>4</sub>, IF<sub>5</sub>, SeO<sub>2</sub>)", "unit5", "vsepr", "Rec 8, Rec 15 p2, Quiz 4"),
    ("Strongest IMF and boiling-point reasoning", "HF, NO, CH<sub>3</sub>OH; SF<sub>4</sub> vs SF<sub>6</sub>; big molecule = more polarizable", "unit7", "imf", "Rec 9.5, Rec 15 p2&ndash;3"),
    ("Draw an MO diagram, bond order", "CO (10 e<sup>&minus;</sup>, N<sub>2</sub>-like, O lower), O<sub>2</sub>, N<sub>2</sub>, NO, HCl, H<sub>2</sub>", "unit6", "hybmo", "Rec 9, Rec 15 p4, Quiz 4"),
    ("Band gap &rarr; LED wavelength, doping, band diagram", "1240/E; GaN vs GaP; Ca on Ga is p-type; label VB, CB, gap, acceptor level", "unit8", "bands", "Rec 10, Rec 15 p5, Quiz 5"),
    ("Glass and cooling rate", "faster cooling &rarr; higher molar volume, higher T<sub>g</sub>; network modifiers", "unit10", "defects", "L19, Rec 15 p6"),
    ("Draw directions and planes", "&lt;100&gt; 6, &lt;110&gt; 12; {110} and {111} planes; Miller from intercepts", "unit9", "miller", "Rec 11, Rec 15 p7&ndash;8"),
    ("r, a and d; touching lines", "FCC face diagonal, BCC body diagonal, with a labelled sketch", "unit9", "lattice", "Rec 11, Rec 15 p9"),
    ("XRD pattern: label peaks, find a and r", "selection rules, sin&sup2;&theta; ratios, &theta; vs 2&theta;", "unit9", "miller", "Rec 12, Rec 15 p10, Quiz 6"),
    ("Point defects", "substitutional vs interstitial (compare sizes); Schottky, Frenkel", "unit10", "defects", "Rec 12, Rec 15 p11, Quiz 6"),
    ("Dislocations, work hardening, annealing", "why hammering hardens, why annealing fixes brittleness", "unit10", "defects", "Rec 12, Rec 15 p12"),
    ("Diffusion", "Fick&rsquo;s first law flux &times; area; Arrhenius slope; interstitial vs vacancy", "unit11", "diffusion", "L20, Rec 15 p1"),
]
trows = "".join(
    '<tr><td><b>%s</b></td><td class="wrap">%s</td><td class="wrap">%s</td><td>%s &middot; %s</td></tr>' % (a, b, e, L(u), P(p)) for a, b, u, p, e in types)

facts_a = [
    "hc = 1240 eV&middot;nm; visible 400&ndash;750 nm (1.65&ndash;3.1 eV)",
    "% ionic = 1 &minus; exp(&minus;&Delta;&chi;&sup2;/4); &mu; = &delta;r; 1 D = 0.2082 e&middot;&Aring;",
    "VSEPR: groups = atoms + lone pairs; name the shape by atoms only; LP: 5 groups equatorial, 6 groups opposite",
    "Nonpolar needs identical groups placed symmetrically (XeF<sub>4</sub>, PCl<sub>5</sub>, CO<sub>2</sub>); HCN and CF<sub>2</sub>H<sub>2</sub> are polar",
    "Hybridization: 2 sp, 3 sp&sup2;, 4 sp<sup>3</sup>, 5 sp<sup>3</sup>d, 6 sp<sup>3</sup>d&sup2;; triple bond = 1 &sigma; + 2 &pi;",
    "Bond order = &frac12;(bonding &minus; antibonding): O<sub>2</sub> 2, N<sub>2</sub> 3, NO 2.5, CO 3, O<sub>2</sub><sup>+</sup> 2.5, He<sub>2</sub><sup>+</sup> 0.5",
    "&pi;2p below &sigma;2p for N<sub>2</sub> and lighter; O<sub>2</sub> and F<sub>2</sub> normal order",
    "IMF decision: ions? &rarr; H on N/O/F? &rarr; polar shape? &rarr; dispersion. Boiling point follows IMF strength; CaO &gt; NaCl",
    "E<sub>g</sub> (eV): C 5.4, Si 1.1, Ge 0.67, Sn 0.08, Pb 0; decreases down a group; longer bond = smaller gap",
    "n-type: more valence e<sup>&minus;</sup> than the atom replaced (donor level below CB). p-type: fewer (acceptor level above VB)",
    "Semiconductor conductivity rises with T; metal falls; &sigma; = 1/&rho;",
    "KE = h&nu; &minus; &phi;; no emission if h&nu; &lt; &phi;",
]
facts_b = [
    "Crystal = lattice + motif; 7 systems, 14 Bravais, 3 cubic; CsCl is simple cubic, NaCl FCC",
    "Points per cell 1, 2, 4; a = 2r, 4r/&radic;3, 2&radic;2 r; packing 0.52, 0.68, 0.74; # nn 6, 8, 12",
    "Density = (points &times; M)/(N<sub>A</sub>a&sup3;); planar density = atoms on plane / area (BCC (110): 2/(a&sup2;&radic;2))",
    "Miller: intercepts &rarr; reciprocals &rarr; clear fractions; &infin; = 0; (hkl) &perp; [hkl] only in cubic",
    "Family counts: &lt;100&gt; 6, &lt;110&gt; 12, &lt;111&gt; 8; {110} 6 planes, {111} 4 planes",
    "d = a/&radic;(h&sup2;+k&sup2;+l&sup2;) (cubic only); 2d sin&theta; = n&lambda;; peaks are at 2&theta;, so halve it",
    "Selection rules: BCC h+k+l even; FCC all odd or all even; sin&sup2;&theta; ratios FCC 3:4:8:11:12, BCC 1:2:3:4:5:6",
    "Interstitial = small atom in a gap; substitutional = similar size; Schottky = vacancy pair; Frenkel = vacancy + interstitial",
    "Dislocations give plastic deformation; blocking them hardens; hammering = work hardening; annealing softens",
    "Slip planes FCC {111}, BCC {110}",
    "Glass: no long-range order; modifiers (Na, Ca) lower the softening T; fast cooling = higher T<sub>g</sub> and volume; crosslinked polymers don&rsquo;t melt",
    "J = &minus;D dC/dx; D = D<sub>0</sub>e<sup>&minus;Q/RT</sup>; slope of ln D vs 1/T = &minus;Q/R; interstitial Q &lt; vacancy Q; depth &asymp; &radic;(Dt)",
]
fa = "".join(ck("fa%d" % i, t) for i, t in enumerate(facts_a))
fb = "".join(ck("fb%d" % i, t) for i, t in enumerate(facts_b))

plan1 = [
    ("p1a", "<b>Unit 05 VSEPR</b> (read, then all 13 &ldquo;Check yourself&rdquo; questions)", "75 min"),
    ("p1b", "<b>Unit 06 hybridization + MO</b> (include the CO example), do the questions", "90 min"),
    ("p1c", "<b>Unit 07 intermolecular forces</b> and the questions", "40 min"),
    ("p1d", "<b>Unit 08 bands, semiconductors, doping</b> and the questions", "75 min"),
    ("p1e", "Quiz Review: timed 10-minute quiz for each of Quiz 4 and Quiz 5 style; redo every miss tomorrow", "30 min"),
]
plan2 = [
    ("p2a", "<b>Unit 09 crystals, Miller, Bragg, selection rules</b> and the questions", "100 min"),
    ("p2b", "<b>Unit 10 defects, glass, polymers</b> and the questions", "50 min"),
    ("p2c", "<b>Unit 11 diffusion</b> and the questions", "40 min"),
    ("p2d", "<b>Exam 2 mock</b> on the Quiz Review page (12 questions, 40 min, then read every solution)", "70 min"),
    ("p2e", "Retry list in &ldquo;My practice&rdquo;: redo every question you missed or peeked at", "40 min"),
]
plan3 = [
    ("p3a", "Open the aid sheet PDF; copy it by hand if the rules want handwriting (copying is a study session)", "40 min"),
    ("p3b", "Read the &ldquo;last-hour facts&rdquo; below out loud, tick each one only if you can say it without looking", "30 min"),
    ("p3c", "Re-read <a href='%s#traps'>Exam traps</a> and the &ldquo;typical slips&rdquo; for VSEPR, MO, XRD" % G, "20 min"),
    ("p3d", "Sleep. Calculator in <b>degree</b> mode; periodic table and constants table packed", "&mdash;"),
]
def plist(items):
    return "".join('<label class="ck"><input type="checkbox" data-k="%s"><span>%s <span class="tl">&middot; %s</span></span></label>' % (k, t, m) for k, t, m in items)

body = """
<div class="ex-shell">
  <header class="hero">
    <div class="hero-eyebrow"><span class="dot"></span> MIT 3.091 &middot; Fall 2026 &middot; Exam 2 &middot; Monday Nov 2</div>
    <h1>Exam 2 Prep: <em>everything on one page</em></h1>
    <p class="sub">Scope: <b>Lectures 10&ndash;20, Recitations 7&ndash;13, Problem Sets 4&ndash;7</b> (covalent bonding through diffusion). A plan for the two days left, what the exam is likely to ask, the facts to know cold, and links to the explanations and practice. Progress ticks are saved in this browser.</p>
    <div class="hero-stats"><a class="go" href="%(Q)s#pq-quiz">&#9733; Start the Exam 2 mock</a><a class="go alt" href="%(G)s">The Field Guide</a><a class="go alt" href="%(Q)s">All practice questions</a></div>
  </header>

  <h3 class="topic" style="--c:var(--warn)">What I could and could not get</h3>
  <div class="box trap">
    <div class="box-head">Read this first</div>
    <ul style="margin-bottom:0">
      <li><b>In the guide:</b> every lecture L10&ndash;L20 (slide by slide) and Recitations 7, 8, 9, 9.5, 10, 11, 12. Recitation 12 is a slide deck (XRD selection rules, defects, work hardening, slip planes); all of it is in Unit 09/10.</li>
      <li><b>Not available to me:</b> <b>Problem Sets 4&ndash;7</b> (only PP1&ndash;3 are in your folder), <b>Recitation 13</b>, and any <b>past exams</b>. The shared Drive folder contains only the Fall 2024 quizzes and recitations, not exams or problem sets. If you drop PP4&ndash;7 and Rec 13 into the chat, I add them with matching practice questions.</li>
      <li><b>Closest thing to a past Exam 2:</b> the Fall 2024 <b>Recitation 15 &ldquo;Exam 2 Review&rdquo;</b> (covering the same lectures). Its twelve problems are the &ldquo;question types&rdquo; table below, and the Exam 2 mock uses the same styles.</li>
      <li><b>Aid sheet:</b> the 2024 exam allowed one 8.5&times;11&Prime; sheet, <b>double-sided</b>, plus periodic table, constants table and a calculator. Check this year&rsquo;s rules. A two-sided Exam 2 aid sheet is in the repo (<code>aid-sheet-exam2.pdf</code>).</li>
    </ul>
  </div>

  <h3 class="topic" style="--c:var(--accent)">The two-day plan</h3>
  <p>About 8&ndash;9 hours of work in total, split so you never read for more than 90 minutes without answering questions. Rule for every block: <b>cover the solutions, answer on paper, then check</b>.</p>
  <div class="plan">
    %(box1)s
    %(box2)s
    %(box3)s
  </div>

  <h3 class="topic" style="--c:var(--accent)">What the exam is likely to ask</h3>
  <p>From the twelve problems of the Fall 2024 Exam 2 review, which covers the same material. For each type: where to read it and where to practise it.</p>
  <div class="tscroll"><table class="data"><thead><tr><th>Type</th><th class="wrap">What they ask</th><th class="wrap">Seen in</th><th>Go to</th></tr></thead><tbody>%(trows)s</tbody></table></div>

  <h3 class="topic" style="--c:var(--accent)">Coverage map</h3>
  <div class="tscroll"><table class="data"><thead><tr><th>Lecture</th><th class="wrap">Topic</th><th>Go to</th></tr></thead><tbody>%(rows)s</tbody></table></div>

  <h3 class="topic" style="--c:var(--accent)">Last-hour facts: tick only what you can say without looking</h3>
  <div class="ck-bar"><i id="fbar"></i></div>
  <div class="facts">%(fa)s</div>
  <div class="facts">%(fb)s</div>

  <h3 class="topic" style="--c:var(--warn)">The ten ways people lose points on this exam</h3>
  <ol>
    <li>Answering with the <b>electron geometry</b> when asked for the <b>shape</b> (XeF<sub>4</sub> is square planar, not octahedral).</li>
    <li>Calling a molecule nonpolar because it has polar bonds, or polar because it has a lone pair (XeF<sub>4</sub>, XeF<sub>2</sub> are nonpolar).</li>
    <li>Forgetting the &frac12; in bond order, or filling N<sub>2</sub> with the O<sub>2</sub> orbital order.</li>
    <li>Using the wrong touching line for r &harr; a (edge, body diagonal, face diagonal).</li>
    <li>Using <b>2&theta;</b> in Bragg&rsquo;s law, or a calculator in radian mode.</li>
    <li>Using d = a/&radic;(h&sup2;+k&sup2;+l&sup2;) on a non-cubic crystal, or confusing r, a and d.</li>
    <li>Forgetting that a peak must satisfy the <b>selection rule</b> (FCC: all odd or all even).</li>
    <li>Not giving a <b>reason</b> in &ldquo;briefly explain&rdquo; parts (strained Si: longer bond, weaker, smaller gap).</li>
    <li>Reversing n and p (compare the dopant&rsquo;s valence electrons with the atom it replaces).</li>
    <li>Eliminating units: eV with J, Q in kJ with R in J, cm&sup3; vs m&sup3;.</li>
  </ol>

  <h3 class="topic" style="--c:var(--accent)">Morning of the exam</h3>
  %(morning)s
</div>
""" % dict(
    Q=Q, G=G,
    box1=box("cheat", "Saturday &middot; molecules and bands", plist(plan1)),
    box2=box("cheat", "Sunday &middot; solids, then the mock", plist(plan2)),
    box3=box("cheat", "Sunday night &middot; Monday morning", plist(plan3)),
    trows=trows, rows=rows, fa=fa, fb=fb,
    morning="".join(ck("m%d" % i, t) for i, t in enumerate([
        "Aid sheet printed or copied, with your name if required",
        "Calculator in <b>degree</b> mode, fresh batteries; periodic table and constants table",
        "Eat; read only the first two items of the facts list, then stop",
        "In the exam: start with the 1-point recall parts, write the formula and numbers even if unsure, check the units on every line",
    ])))

js = """
(function(){
  var KEY='3091-exam2-prep-v1',st={};
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
        '<title>3.091 Exam 2 Prep</title>\n' + fonts + '<style>' + css + '</style>\n</head>\n<body>\n' + body + '<script>' + js + '</script>\n</body>\n</html>\n')
open(os.path.join(ROOT, "exam2-prep.html"), "w", encoding="utf-8").write(page)
print("wrote exam2-prep.html", len(page))
