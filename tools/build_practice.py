#!/usr/bin/env python3
"""Rebuild everything that is generated from the practice-question bank.

    python3 tools/build_practice.py            # from the repo root

Reads tools/practice_bank_*.py and rewrites
  * the "Check yourself" blocks between <!--PQ:begin unitN--> ... <!--PQ:end unitN--> in index.html
  * the shared CSS / JS between the PQ-CSS and PQ-JS markers in index.html
  * quiz-review.html (the stand-alone quiz-prep page, includes every question)

To add a question: append it to the right tools/practice_bank_*.py with num(), mc() or selfq(),
then run this script. See CONTRIBUTING.md.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import practice_lib as L  # noqa: E402

for letter in "abcd":
    exec(compile(open(os.path.join(HERE, "practice_bank_%s.py" % letter)).read(), "practice_bank_%s.py" % letter, "exec"), {"__name__": "bank"})

# ---------------------------------------------------------------- inline subsets for the Field Guide
INLINE = {
    "unit1": ["gas-1", "gas-2", "gas-5", "gas-6", "bohr-1", "bohr-2", "bohr-3", "bohr-6"],
    "unit2": ["config-1", "config-2", "config-3", "config-4", "config-6", "trends-1", "trends-2", "trends-4", "trends-5", "trends-6"],
    "unit3": ["ionic-1", "ionic-2", "ionic-3", "ionic-4", "ionic-5", "ionic-7"],
    "unit4": ["lewis-1", "lewis-2", "lewis-7", "lewis-8"],
    "unit5": ["lewis-3", "lewis-4", "lewis-5", "lewis-9", "vsepr-1", "vsepr-2", "vsepr-3", "vsepr-4", "vsepr-6", "vsepr-7"],
    "unit6": ["hybmo-1", "hybmo-2", "hybmo-3", "hybmo-4", "hybmo-5", "hybmo-6", "hybmo-8", "hybmo-9"],
    "unit7": ["imf-1", "imf-2", "imf-3", "imf-4", "imf-5", "imf-7"],
    "unit8": ["bands-1", "bands-2", "bands-3", "bands-4", "bands-5", "bands-6", "bands-7", "bands-8"],
    "unit9": ["lattice-1", "lattice-2", "lattice-3", "lattice-5", "lattice-7", "lattice-9", "miller-1", "miller-3", "miller-5", "miller-7", "miller-9"],
    "unit10": ["defects-1", "defects-2", "defects-3", "defects-4", "defects-6", "defects-7", "defects-8", "defects-9"],
    "unit11": ["diffusion-1", "diffusion-3", "diffusion-4", "diffusion-5", "diffusion-6", "diffusion-7"],
}
LEADS = {
    "unit1": "Cover the solutions, write your answer on paper first, <em>then</em> press Check. Quiz 1 is exactly this kind of problem.",
    "unit2": "Quiz 2 mixes configurations, quantum numbers and trend arrows. If you miss one, re-read the recipe in the box above and retry tomorrow.",
    "unit3": "Quiz 3: ion charges, the NaCl picture, &ldquo;which structure?&rdquo; and the Born&ndash;Haber steps.",
    "unit4": "Count electrons, then draw. Get these right before moving to shapes.",
    "unit5": "Dipoles, bond strength and the Lewis &rarr; AXE &rarr; shape chain from Quiz 4.",
    "unit6": "Hybridization is a counting recipe; MO bond order is a subtraction. Practise both until they are automatic.",
    "unit7": "One-point quiz questions. Use the decision path: ions, H-bond, polar shape, otherwise dispersion.",
    "unit8": "Quiz 5: match the diagram, say what strain does to the gap, n- or p-type, and convert a gap to a wavelength.",
    "unit9": "Quiz 6 starts here: a from r, packing and density, then Miller indices and Bragg&rsquo;s law.",
    "unit10": "Mostly one-sentence reasons. Say <em>why</em>, because the rubrics award a point for the reason.",
    "unit11": "L20 is light on equations; these questions practise the logic (and the standard Arrhenius / &radic;(Dt) forms, tagged extra).",
}
QUIZ_PAGE = "quiz-review.html"

# ---------------------------------------------------------------- quiz-review extras
SLIPS = {
    "gas": ["Using 1 g/mol for H<sub>2</sub> / 16 for O<sub>2</sub> instead of the diatomic molar mass.", "Celsius in PV = nRT.", "Linear conversion factor for a volume (cube it)."],
    "bohr": ["Forgetting to square Z, or using the ion charge instead of Z.", "Swapping n<sub>i</sub> and n<sub>f</sub>: the sign flips.", "Thinking high energy = long wavelength."],
    "config": ["Putting 3d before 4s when removing electrons.", "Pairing electrons before every 3d box has one (Hund).", "Different m<sub>l</sub> for the two electrons in one orbital."],
    "trends": ["Reversing the radius direction.", "Forgetting Be &gt; B and N &gt; O.", "Comparing ions with different electron counts."],
    "ionic": ["Reading the subscript as the charge (K<sub>2</sub>O).", "Mixing up ionization energy (metal) and electron affinity (nonmetal).", "Forgetting the &frac12; for the diatomic."],
    "lewis": ["Missing the extra electrons of a negative charge.", "Expanding the octet of C, N, O or F.", "Calling a bond &ldquo;ionic&rdquo; when it is polar covalent."],
    "vsepr": ["Answering with the electron geometry instead of the shape.", "Counting a double bond as two groups.", "Placing lone pairs next to each other in a 6-group molecule."],
    "hybmo": ["Forgetting the &frac12; in bond order.", "Counting double/triple bonds as several groups for hybridization.", "Antibonding drawn below bonding."],
    "imf": ["Answering &ldquo;covalent bond&rdquo; (that is inside the molecule).", "Answering dipole&ndash;dipole when an N&ndash;H / O&ndash;H / H&ndash;F is present.", "Calling a symmetric molecule (CF<sub>4</sub>) polar."],
    "bands": ["Swapping germanium and diamond (compare gap sizes).", "Reversing n and p.", "eV with joules in &lambda; = hc/E."],
    "lattice": ["Using the wrong touching line (edge / body diagonal / face diagonal).", "Counting atoms instead of lattice points.", "Forgetting &radic;2 in the (110) area."],
    "miller": ["Calculator in radians.", "Using 2&theta; as &theta; (or the reverse).", "Using d = a instead of a/&radic;(h&sup2;+k&sup2;+l&sup2;)."],
    "defects": ["&ldquo;Softer&rdquo; after hammering (confusing it with annealing).", "Substitutional for a small atom like C.", "Thinking glass melts at one temperature."],
    "diffusion": ["Q in kJ with R in J.", "Reading &ldquo;steeper&rdquo; as &ldquo;faster&rdquo;.", "Forgetting that depth goes as the square root of time."],
}
QUIZMAP = [
    ("Quiz 1", "gas, bohr", "L01&ndash;L03", "PV = nRT &rarr; grams; hydrogen-like Rydberg energy; visible or not (10 pts)"),
    ("Quiz 2", "config, trends", "L04&ndash;L06", "configuration, box diagram, quantum numbers, cation charge, three trend arrows"),
    ("Quiz 3", "ionic, lewis", "L07&ndash;L09", "Lewis dots + oxidation states (K<sub>2</sub>O), NaCl picture, which solid is rock salt, Born&ndash;Haber labels"),
    ("Quiz 4", "vsepr, hybmo, imf", "L10&ndash;L13", "XeF<sub>4</sub> Lewis + AXE + shape; H<sub>2</sub> MO diagram + bond order; strongest IMF"),
    ("Quiz 5", "bands", "L14&ndash;L15", "match bands to Au / Ge / diamond; strained-Si gap; n- or p-type; LED wavelength"),
    ("Quiz 6", "lattice, miller, defects", "L16&ndash;L18", "BCC planar density; equivalent planes; Bragg&rsquo;s law; interstitial vs substitutional; work hardening"),
]

TOPIC_ORDER = ["gas", "bohr", "config", "trends", "ionic", "lewis", "vsepr", "hybmo", "imf", "bands", "lattice", "miller", "defects", "diffusion"]
UNIT_OF_TOPIC = {k: v["unit"] for k, v in L.TOPICS.items()}


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


def write(p, s):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
        f.write(s)


def replace_between(s, begin, end, new, keep_markers=True):
    i = s.index(begin)
    j = s.index(end, i)
    if keep_markers:
        return s[:i + len(begin)] + new + s[j:]
    return s[:i] + new + s[j + len(end):]


def build_index():
    s = read("index.html")
    byid = {q["id"]: q for q in L.BANK}
    for unit, ids in INLINE.items():
        qs = [byid[i] for i in ids]
        block = L.render_block("Check yourself", LEADS[unit] + ' <a href="%s">All questions on this topic and timed quizzes &rarr;</a>' % QUIZ_PAGE, qs)
        s = replace_between(s, "<!--PQ:begin %s-->" % unit, "<!--PQ:end %s-->" % unit, block)
    css = read("tools/practice.css")
    s = replace_between(s, "/*PQ-CSS-BEGIN*/", "/*PQ-CSS-END*/", "\n" + css + "\n  ")
    js = read("tools/practice.js")
    s = replace_between(s, "<!--PQ-JS-BEGIN-->", "<!--PQ-JS-END-->", "<script>\n" + js + "\n</script>")
    write("index.html", s)
    return len(INLINE), sum(len(v) for v in INLINE.values())


def build_quiz_page():
    idx = read("index.html")
    base_css = re.search(r"<style>(.*?)</style>", idx, re.S).group(1)
    # drop the generated practice css from the base (it is added again below) and the shell grid, which this page does not use
    base_css = re.sub(r"/\*PQ-CSS-BEGIN\*/.*?/\*PQ-CSS-END\*/", "", base_css, flags=re.S)
    css = base_css + "\n" + read("tools/practice.css") + """
  .qr-shell{max-width:880px;margin:0 auto;padding:20px 16px 90px;}
  .qr-shell .hero{margin-bottom:18px;}
  .qr-nav{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 4px;}
  .qr-nav a{font-family:"IBM Plex Mono",monospace;font-size:12px;padding:5px 11px;border:1px solid var(--line);border-radius:999px;color:var(--ink-soft);text-decoration:none;background:var(--raised);}
  .qr-nav a:hover{border-color:var(--accent);color:var(--accent-ink);}
  .qr-recipe{border-left:4px solid var(--c,var(--accent));padding:8px 14px;background:var(--raised);border-radius:0 10px 10px 0;margin:6px 0 10px;font-size:16px;}
  .qr-slips{font-size:15px;color:var(--ink-soft);margin:0 0 14px;}
  .qr-slips b{color:var(--warn);}
  .qr-map td,.qr-map th{vertical-align:top;}
  .qr-presets{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 10px;}
"""
    topics = [t for t in TOPIC_ORDER if L.by_topic(t)]
    nav = "".join('<a href="#t-%s">%s</a>' % (t, L.TOPICS[t]["title"]) for t in topics)
    sections = []
    for t in topics:
        info = L.TOPICS[t]
        unit = info["unit"]
        qs = L.by_topic(t)
        slips = "".join("<li>%s</li>" % x for x in SLIPS.get(t, []))
        sections.append(
            '<section class="pq-topic" id="t-%s"><h3 class="topic" style="--c:var(--accent)">%s</h3>'
            '<div class="qr-recipe"><b>%s &middot; the recipe.</b> %s <a href="index.html#%s">Read the full explanation &rarr;</a></div>'
            '<p class="qr-slips"><b>Typical slips:</b></p><ul class="qr-slips">%s</ul>%s</section>' % (
                t, info["title"], info["quiz"], info["recipe"], unit, slips, "".join(L.render_question(q) for q in qs)))
    qmap_rows = "".join(
        '<tr><td><b>%s</b></td><td>%s</td><td class="wrap">%s</td></tr>' % (
            q, ", ".join('<a href="#t-%s">%s</a>' % (x.strip(), x.strip()) for x in tp.split(",")), desc + " <span class=\"small\">(" + lec + ")</span>")
        for q, tp, lec, desc in QUIZMAP)
    topic_checks = "".join('<label><input type="checkbox" value="%s"> %s</label>' % (t, L.TOPICS[t]["title"].split(":")[0]) for t in topics)
    topic_chips = '<button class="pq-chip on" data-f="topic" data-v="all" type="button">all</button>' + "".join(
        '<button class="pq-chip" data-f="topic" data-v="%s" type="button">%s</button>' % (t, t) for t in topics)
    total = len(L.BANK)
    nnum = sum(1 for q in L.BANK if q["kind"] != "self")
    body = """
<div class="qr-shell">
  <header class="hero">
    <div class="hero-eyebrow"><span class="dot"></span> MIT 3.091 &middot; Fall 2026 &middot; quiz prep</div>
    <h1>Quiz Review: <em>the page to open before any quiz</em></h1>
    <p class="sub">%d practice questions with worked solutions, grouped by what the quizzes actually ask. Every answer can be checked instantly, wrong answers go on your retry list, and a timed mode runs a 10-minute mock quiz drawn from the topics you choose. Modelled on the six past quizzes in your Drive folder (Fall 2024, Q1&ndash;Q6) and on the recitations. The questions are written for this guide with new numbers (a few are close variants of a recitation problem and say so in their tag).</p>
    <div class="hero-stats"><span class="stat-pill"><b>%d</b> questions</span><span class="stat-pill"><b>%d</b> auto-checked</span><span class="stat-pill"><b>%d</b> topics</span><a class="stat-pill stat-link" href="index.html">&larr; the Field Guide</a></div>
  </header>

  <div class="pq-intro">
    <h3 class="topic" style="--c:var(--accent)">How a 3.091 quiz works (and how to score)</h3>
    <ul>
      <li><b>10 minutes, about 10 points, 4&ndash;5 parts.</b> Most parts are worth 1&ndash;3 points. Lowest quiz is dropped, but you do not know which one yet.</li>
      <li><b>Rubrics give points for steps</b>: &ldquo;identify the values&rdquo;, &ldquo;correct equation&rdquo;, &ldquo;answer&rdquo;. A wrong final answer with the right steps still scores. <b>Write the formula and the numbers, even if you are unsure.</b></li>
      <li><b>About half the points are recall in one line</b>: AXE number, shape, n- or p-type, strongest force, interstitial or substitutional, harder or softer. These are the cheapest points; drill them first.</li>
      <li>&ldquo;Briefly explain&rdquo; parts need a <em>reason</em>, not only the answer (strained Si has a smaller gap <em>because</em> longer bonds are weaker).</li>
      <li>Three habits fix most lost points: (1) units in every line, (2) degrees mode and &theta; vs 2&theta;, (3) answer exactly what was asked (shape vs electron geometry; charge vs subscript).</li>
    </ul>
    <h4>The six past quizzes at a glance</h4>
    <div class="tscroll"><table class="data qr-map"><thead><tr><th>Quiz</th><th>Topics here</th><th class="wrap">What was asked</th></tr></thead><tbody>%s</tbody></table></div>
    <p class="small">Quizzes 7&ndash;9 in the same Drive folder (kinetics and catalysis, equilibrium, phase diagrams) cover material after Lecture 20 and are not covered here yet. The Fall 2024 files also contain a few answer-key slips (Quiz 2 &ldquo;half-full 3d&rdquo; for Co<sup>2+</sup>, Quiz 6 d<sub>110</sub>); the questions below flag them.</p>
  </div>

  <div class="pq-quizbox" id="pq-quiz">
    <h3>Timed mock quiz</h3>
    <p style="margin:0 0 6px">Random questions from the topics you tick (only auto-checked ones), solutions hidden until you submit or the clock ends. Real quizzes give you 10 minutes.</p>
    <div class="qr-presets"><button class="pq-chip" type="button" data-preset="gas,bohr">Quiz 1 style</button><button class="pq-chip" type="button" data-preset="config,trends">Quiz 2 style</button><button class="pq-chip" type="button" data-preset="ionic,lewis">Quiz 3 style</button><button class="pq-chip" type="button" data-preset="vsepr,hybmo,imf">Quiz 4 style</button><button class="pq-chip" type="button" data-preset="bands">Quiz 5 style</button><button class="pq-chip" type="button" data-preset="lattice,miller,defects">Quiz 6 style</button><button class="pq-chip" type="button" data-preset="all">everything</button></div>
    <div class="qz-row"><div id="qz-topics">%s</div></div>
    <div class="qz-row"><label>Questions <select id="qz-n"><option>4</option><option selected>5</option><option>8</option><option>10</option></select></label><label>Minutes <select id="qz-min"><option>5</option><option selected>10</option><option>15</option><option>20</option></select></label><button class="pq-btn" id="qz-start" type="button">Start</button><span id="qz-msg" class="small"></span></div>
  </div>

  <div class="qz-bar" id="pq-stage"><b id="qz-clock">10:00</b><span>Write each answer, then press Check. Solutions appear after you submit.</span><button class="pq-btn" id="qz-submit" type="button">Submit</button><button class="pq-btn" id="qz-quit" type="button">Quit</button></div>
  <div id="qz-result" hidden></div>

  <div class="pq-filters" id="pq-filters" data-topic="all" data-diff="all" data-state="all">
    <div class="pq-fgroup"><span class="pq-flabel">topic</span>%s</div>
    <div class="pq-fgroup"><span class="pq-flabel">level</span><button class="pq-chip on" data-f="diff" data-v="all" type="button">all</button><button class="pq-chip" data-f="diff" data-v="1" type="button">&#9679;&#9675;&#9675; warm-up</button><button class="pq-chip" data-f="diff" data-v="2" type="button">&#9679;&#9679;&#9675; quiz level</button><button class="pq-chip" data-f="diff" data-v="3" type="button">&#9679;&#9679;&#9679; harder</button></div>
    <div class="pq-fgroup"><span class="pq-flabel">show</span><button class="pq-chip on" data-f="state" data-v="all" type="button">all</button><button class="pq-chip" data-f="state" data-v="todo" type="button">not yet done</button><button class="pq-chip" data-f="state" data-v="retry" type="button">to retry</button></div>
  </div>
  <div class="qr-nav pq-nav"><span class="pq-flabel" style="align-self:center">jump to</span>%s</div>
  %s
  <p class="small">Progress is saved in this browser only (nothing is sent anywhere). The &ldquo;My practice&rdquo; button, bottom right, shows your progress by topic and your retry list.</p>
</div>
""" % (total, total, nnum, len(topics), qmap_rows, topic_checks, topic_chips, nav, "\n".join(sections))
    preset_js = """
(function(){
  var presets=document.querySelectorAll('[data-preset]');
  Array.prototype.forEach.call(presets,function(b){b.addEventListener('click',function(){
    var v=b.getAttribute('data-preset'),all=v==='all',set=v.split(',');
    Array.prototype.forEach.call(document.querySelectorAll('#qz-topics input'),function(i){i.checked=all?false:set.indexOf(i.value)>-1;});
    var n=document.getElementById('qz-n');n.value='5';document.getElementById('qz-start').click();
  });});
})();
"""
    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>3.091 Quiz Review</title>\n'
            + re.search(r"(<link[^>]*fonts[^>]*>\s*)+", idx).group(0) +
            '<style>' + css + '</style>\n</head>\n<body>\n' + body +
            '<script>\n' + read("tools/practice.js") + '\n' + preset_js + '</script>\n</body>\n</html>\n')
    write("quiz-review.html", page)
    return total


if __name__ == "__main__":
    nb, nq = build_index()
    total = build_quiz_page()
    print("index.html: %d check-yourself blocks, %d inline questions" % (nb, nq))
    print("quiz-review.html: %d questions in %d topics" % (total, len([t for t in TOPIC_ORDER if L.by_topic(t)])))
