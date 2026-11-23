#!/usr/bin/env python3
"""Builds aid-sheet-exam3.html (two letter pages, front and back) for Exam 3 (L21-L28).
Reuses the stylesheet of aid-sheet-exam2.html. PDF: scripts/build-aid-sheet-exam3-pdf.sh"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base = open(os.path.join(ROOT, "aid-sheet-exam2.html"), encoding="utf-8").read()
head = base[:base.index("<body>")]
head = head.replace("<title>3.091 Exam 2 Aid Sheet</title>", "<title>3.091 Exam 3 Aid Sheet</title>")
extra_css = """
  .c-kin h2{background:#E2F3EE; color:#136F58;}
  .c-th h2{background:#FBEAE3; color:#9C3A22;}
  .c-eq h2{background:#EAEEFC; color:#2546B8;}
  .c-cat h2{background:#F0E9FB; color:#6B3FC2;}
  .c-sol h2{background:#DDF0F3; color:#176A7B;}
  .c-acid h2{background:#F9E6F0; color:#9A2F66;}
  .c-ksp h2{background:#F7EBDC; color:#9C5E24;}
  .trp{color:#9C3A22;}
  .trp b{color:#9C3A22;}
  .ln{font-size:7.15pt; line-height:1.33; margin-bottom:1.4pt;}
  .eqbox{font-size:7.3pt; padding:2pt 5pt; margin:1.2pt 0;}
  .blk{margin-bottom:5.5pt;}
  .blk h2{font-size:8.3pt; margin-bottom:2pt;}
  table.ref th, table.ref td{font-size:6.7pt; padding:0.8pt 2.2pt; line-height:1.22;}
"""
head = head.replace("</style>", extra_css + "</style>")

def blk(cls, title, *lines):
    out = ['<div class="blk %s"><h2>%s</h2>' % (cls, title)]
    for l in lines:
        if l.startswith("EQ:"):
            out.append('<div class="eqbox">%s</div>' % l[3:])
        elif l.startswith("TRAP:"):
            out.append('<div class="ln trp"><b>Trap:</b> %s</div>' % l[5:])
        else:
            out.append('<div class="ln">%s</div>' % l)
    out.append("</div>")
    return "".join(out)

# ============================ SIDE 1 ============================
a1 = "".join([
 blk("c-kin", "L21–22 · Rate &amp; rate law",
     "EQ:v = −(1/a) d[A]/dt = +(1/p) d[P]/dt &nbsp; (M/s)",
     "Instantaneous = slope of the tangent; average = Δ[ ]/Δt. Collision model: needs collisions with E ≥ E<sub>a</sub> <b>and</b> the right orientation. Rate ↑ with [ ], T, catalyst.",
     "EQ:v = k[A]<sup>α</sup>[B]<sup>β</sup> &nbsp; order = α + β",
     "Exponents come from <b>experiment</b> (initial rates), not coefficients, unless the step is <b>elementary</b>. Two runs: v₂/v₁ = ([A]₂/[A]₁)<sup>α</sup>; hold the other reactant fixed. k units = M<sup>1−n</sup>s<sup>−1</sup> (units of k reveal the order).",
     "TRAP: coefficients ≠ exponents for a multistep reaction; a rate-law exponent can be 0, fraction or negative."),
 blk("c-kin", "Integrated laws (table)",
     '<table class="ref"><tr><th>order</th><th>plot</th><th>slope</th><th>k units</th><th>t<sub>½</sub></th></tr>'
     '<tr><td>0</td><td>[A] vs t</td><td>−k</td><td>M/s</td><td>[A]₀/2k</td></tr>'
     '<tr><td>1</td><td>ln[A] vs t</td><td>−k</td><td>s⁻¹</td><td><b>ln2/k</b></td></tr>'
     '<tr><td>2</td><td>1/[A] vs t</td><td><b>+k</b></td><td>M⁻¹s⁻¹</td><td>1/(k[A]₀)</td></tr></table>',
     "EQ:[A] = [A]₀ − kt &nbsp; ln[A] = ln[A]₀ − kt &nbsp; 1/[A] = 1/[A]₀ + kt",
     "First order t<sub>½</sub> does <b>not</b> depend on [A]₀ (radioactive decay); after n half-lives [A]₀/2<sup>n</sup>. The plot that is straight gives the order."),
 blk("c-kin", "Arrhenius &amp; energy diagram",
     "EQ:k = A e<sup>−E<sub>a</sub>/RT</sup> &nbsp; ln k = ln A − (E<sub>a</sub>/R)(1/T)",
     "EQ:ln(k₂/k₁) = (E<sub>a</sub>/R)(1/T₁ − 1/T₂)",
     "ln k vs 1/T: slope = <b>−E<sub>a</sub>/R</b>, intercept ln A. <b>Steeper = larger E<sub>a</sub></b> (more T-sensitive), not “faster”. T in K, E<sub>a</sub> in J/mol (R in J).",
     "Diagram: E<sub>a</sub>(fwd) = TS − reactants; E<sub>a</sub>(rev) = TS − products; ΔE = products − reactants (&lt;0 exothermic). Peak = activated complex/TS; valley = <b>intermediate</b>. Catalyst: lower E<sub>a</sub> both ways, same ΔE.",
     "<b>Mechanism</b>: sum of elementary steps; slow step = rate-determining → sets the rate law; intermediates cancel in the overall equation; a catalyst is used then regenerated. Elementary step: exponents = coefficients (molecularity)."),
])

a2 = "".join([
 blk("c-th", "L23 · Gibbs free energy &amp; spontaneity",
     "EQ:ΔG = ΔH − TΔS &nbsp; (constant T, P)",
     "<b>ΔG &lt; 0</b> spontaneous · <b>ΔG = 0</b> equilibrium · <b>ΔG &gt; 0</b> not spontaneous as written (reverse is). <b>Spontaneous ≠ fast</b> (rate = E<sub>a</sub>, kinetics).",
     "Where it comes from: ΔS<sub>surr</sub> = −ΔH/T and ΔS<sub>univ</sub> = ΔS<sub>sys</sub> + ΔS<sub>surr</sub> ≥ 0 → <b>ΔG = −TΔS<sub>univ</sub></b>.",
     '<table class="ref"><tr><th>ΔH</th><th>ΔS</th><th>ΔG = ΔH−TΔS</th><th>example</th></tr>'
     '<tr><td>−</td><td>+</td><td>always &lt; 0</td><td>burning</td></tr>'
     '<tr><td>+</td><td>−</td><td>never &lt; 0</td><td>—</td></tr>'
     '<tr><td>−</td><td>−</td><td>&lt; 0 at <b>low T</b></td><td>freezing</td></tr>'
     '<tr><td>+</td><td>+</td><td>&lt; 0 at <b>high T</b></td><td>boiling, melting</td></tr></table>',
     "EQ:Crossover T = ΔH/ΔS (ΔG = 0)",
     "Example: ΔH = +44 kJ, ΔS = +118 J/K → T = 44000/118 = <b>373 K</b>. Above it spontaneous (+,+). At a phase change T<sub>b</sub>: ΔG = 0, ΔS = ΔH/T.",
     "ΔG vs T is a line: <b>slope = −ΔS</b>, intercept = ΔH. Max useful (non-PV) work = |ΔG| (w<sub>max</sub> = ΔG, system does work if ΔG &lt; 0). ΔG of coupled steps adds.",
     "TRAP: ΔH in kJ, ΔS in J/K: ×1000. Kelvin only. A ΔG&lt;0 reaction can still be slow."),
 blk("c-th", "Standard values &amp; Hess",
     "EQ:ΔH°<sub>rxn</sub> = ΣnΔH°<sub>f</sub>(prod) − ΣnΔH°<sub>f</sub>(react)",
     "EQ:ΔG°<sub>rxn</sub> = ΣnΔG°<sub>f</sub>(prod) − ΣnΔG°<sub>f</sub>(react)",
     "EQ:ΔS°<sub>rxn</sub> = ΣnS°(prod) − ΣnS°(react)",
     "ΔH°<sub>f</sub> and ΔG°<sub>f</sub> of an <b>element in its standard state = 0</b>; S° of an element is <b>not</b> 0 (only a perfect crystal at 0 K). Multiply by the coefficients. Hess: reverse a step → flip sign; ×n → ×n; add steps → add ΔH (or ΔG).",
     "ΔG° = ΔH° − TΔS° (standard) vs ΔG = ΔG° + RT ln Q (any conditions); <b>ΔH ≈ ΔH°, ΔS = ΔS° − R ln Q</b>."),
])

a3 = "".join([
 blk("c-th", "Rec 16 · Enthalpy, work, entropy",
     "EQ:ΔE = Q + W &nbsp; W = −PΔV",
     "<b>Q + / W +</b> = energy <b>into</b> the system. Expansion (ΔV &gt; 0) → W &lt; 0 (system does work); compression → W &gt; 0. Example: 2.0 atm, ΔV = −1.5 L → W = +3.0 L·atm = <b>+304 J</b>.",
     "Constant V: W = 0, ΔE = Q<sub>v</sub>. Isothermal ideal gas: ΔE = 0 → Q = −W. Adiabatic: Q = 0. Isolated: ΔE = 0.",
     "EQ:H = E + PV &nbsp; ΔH = ΔE + PΔV = <b>Q<sub>p</sub></b> &nbsp; (gases: ΔH = ΔE + Δn<sub>g</sub>RT)",
     "ΔH &lt; 0 exothermic (heat out), ΔH &gt; 0 endothermic. <b>State functions</b>: E, H, S, G (path-independent). <b>Path functions</b>: Q, W.",
     "EQ:S = k ln W &nbsp; ΔS<sub>univ</sub> = ΔS<sub>sys</sub> + ΔS<sub>surr</sub> ≥ 0",
     "<b>ΔS ↑</b> when: solid → liquid → gas; more moles of gas (Δn<sub>g</sub> &gt; 0); dissolving/mixing; heating; more particles. S: crystal &lt; amorphous &lt; liquid ≪ gas. Units J/(mol·K).",
     "<b>2nd law</b>: ΔS<sub>univ</sub> ≥ 0 (system may decrease if the surroundings gain more). <b>3rd law</b>: S = 0 for a perfect crystal at 0 K. <b>1st law</b>: energy conserved.",
     "TRAP: sign of W (on system = +); exothermic does not mean spontaneous; entropy of a system can fall in a spontaneous process."),
 blk("c-eq", "L24 · Equilibrium constant",
     "EQ:aA + bB ⇌ cC + dD &nbsp; K = [C]<sup>c</sup>[D]<sup>d</sup> / ([A]<sup>a</sup>[B]<sup>b</sup>)",
     "Products over reactants; coefficients are exponents; <b>solids and pure liquids left out</b>; K has no units (K<sub>p</sub> for gases in pressure). Reverse: <b>1/K</b>; ×n: <b>K<sup>n</sup></b>; add reactions: <b>K₁K₂</b>. K ≫ 1 products favoured; K ≪ 1 reactants.",
     "<b>Q vs K</b> (same form as K, any moment): Q &lt; K → <b>right</b> (forward); Q &gt; K → <b>left</b>; Q = K equilibrium.",
     "EQ:ΔG = ΔG° + RT ln Q &nbsp; ΔG° = −RT ln K &nbsp; K = e<sup>−ΔG°/RT</sup>",
     "ΔG° &lt; 0 ↔ K &gt; 1; ΔG° = 0 ↔ K = 1; at equilibrium ΔG = 0 and Q = K. Only <b>T</b> changes K (not P, [ ], catalyst)."),
 blk("c-atoms", "Constants",
     "R = <b>8.314 J/(mol·K)</b> = 0.0821 L·atm/(mol·K) &nbsp; 1 L·atm = <b>101.3 J</b> &nbsp; K = °C + 273.15",
     "K<sub>w</sub> = 10<sup>−14</sup> (25 °C) &nbsp; ln x = 2.303 log x &nbsp; N<sub>A</sub> = 6.022×10²³ &nbsp; <b>ΔH in kJ, ΔS in J/K, R in J: convert!</b>"),
])

# ============================ SIDE 2 ============================
b1 = "".join([
 blk("c-eq", "RICE · van't Hoff · Le Châtelier",
     "<b>RICE</b>: Reaction · Initial · Change (±coefficient·x) · Equilibrium → plug in K. If K tiny and x ≪ initial, drop x (check &lt;5%); else quadratic. Mixing/dilution: use <b>total</b> volume.",
     "EQ:ln K = −ΔH°/(RT) + ΔS°/R &nbsp; ln(K₂/K₁) = −(ΔH°/R)(1/T₂ − 1/T₁)",
     "ln K vs 1/T: slope = <b>−ΔH°/R</b>. <b>Exothermic: K falls as T rises</b>; endothermic: K rises. (Combine ΔG° = ΔH° − TΔS° = −RT ln K.)",
     '<table class="ref"><tr><th>stress</th><th>shift</th></tr>'
     '<tr><td>add reactant / remove product</td><td>right</td></tr>'
     '<tr><td>compress (↑P)</td><td>fewer moles of gas</td></tr>'
     '<tr><td>heat</td><td>endothermic direction (K changes)</td></tr>'
     '<tr><td>catalyst, inert gas at const V</td><td>none; K same</td></tr></table>',
     "TRAP: K changes only with T. Le Châtelier shifts Q, not K, for [ ] and P."),
 blk("c-cat", "L25 · Catalysis &amp; Haber–Bosch",
     "A catalyst gives an <b>alternative path with lower E<sub>a</sub></b> (forward and reverse equally). <b>Unchanged: ΔH, ΔG, K, equilibrium yield.</b> Not consumed; speeds approach to equilibrium. It cannot make ΔG &gt; 0 go.",
     "<b>Homogeneous</b>: same phase as reactants. <b>Heterogeneous</b>: different phase (solid surface). <b>Enzyme</b>: protein catalyst, active site, selective, mild conditions.",
     "EQ:N₂ + 3H₂ ⇌ 2NH₃ &nbsp; ΔH = −92 kJ (−46 per mol NH₃)",
     "<b>Fe catalyst, 400–500 °C, high P</b>. High P: 4 mol gas → 2 (Le Châtelier). Exothermic, so low T favours yield but is too slow → compromise. <b>Liquefy NH₃</b> (polar, H-bonds, higher bp) → removes product, shifts right; recycle N₂ + H₂. H₂ from <b>CH₄ + H₂O → CO + 3H₂</b> (≈1.8 % of world energy and CO₂).",
     "<b>Ertl (Fe surface)</b>: N₂, H₂ adsorb → N≡N splits on the surface; H₂ splits → N–H forms stepwise N → NH → NH₂ → NH₃ → NH₃ desorbs, surface freed.",
     "<b>Sabatier</b>: best catalyst binds <b>intermediately</b> (volcano plot, rate vs binding strength). Too strong: product stays stuck (desorption-limited). Too weak: reactant will not bind/activate. Better catalyst = lower T needed.",
     "<b>Nitrogenase</b>: Fe₇MoS₉C cluster, N₂ + 8H⁺ + 8e⁻ + 16 ATP → 2NH₃ + H₂ at room T, P. N: 0 → −3 (fixation)."),
])

b2 = "".join([
 blk("c-sol", "L26 · Solutions",
     "EQ:ΔH<sub>soln</sub> = ΔH₁(solvent–solvent broken, +) + ΔH₂(solute–solute broken, +) + ΔH₃(A–B formed, −)",
     "ΔS<sub>soln</sub> &gt; 0, so ΔH usually decides: |ΔH₃| &gt; ΔH₁ + ΔH₂ → exothermic. ΔG<sub>soln</sub> = ΔH<sub>soln</sub> − TΔS<sub>soln</sub> &lt; 0 dissolves. <b>Like dissolves like</b>: polar/ionic in water, non-polar in non-polar.",
     "Solubility vs T is not fixed by the sign of ΔH alone (NH₄NO₃ +25.7 kJ/mol rises; CaCl₂ −68.2 kJ/mol also rises).",
     "EQ:M = mol/L <u>solution</u> &nbsp; m = mol/kg <u>solvent</u> &nbsp; X = n/n<sub>tot</sub>",
     "mass % = mass solute/mass soln ×100; ppm = mass solute/mass soln ×10⁶ (dilute water: 1 ppm ≈ 1 mg/L); ppb ×10⁹. Only <b>M</b> changes with T. Dilution M₁V₁ = M₂V₂."),
 blk("c-acid", "L27 · Acids &amp; bases",
     "Brønsted: acid donates H⁺, base accepts. <b>Conjugate pair</b> differs by one H⁺ (HA/A⁻, BH⁺/B). Water and HCO₃⁻ are amphoteric. Strong acid → negligible conjugate base.",
     "EQ:pH = −log[H₃O⁺] &nbsp; pH + pOH = 14 &nbsp; K<sub>w</sub> = [H⁺][OH⁻] = 10⁻¹⁴ (25 °C)",
     "EQ:K<sub>a</sub> = [H⁺][A⁻]/[HA] &nbsp; pK<sub>a</sub> = −log K<sub>a</sub> &nbsp; K<sub>a</sub>K<sub>b</sub> = K<sub>w</sub> &nbsp; pK<sub>a</sub> + pK<sub>b</sub> = 14",
     "<b>Small pK<sub>a</sub> = strong acid</b>; stronger acid = weaker conjugate base. pK<sub>a</sub>: HI −9.3 · HNO₃ −1.4 · H₃O⁺ 0 · HF 3.2 · acetic 4.76 · HCN 9.2 · NH₄⁺ 9.25 · H₂O 14. Weaker X–H bond / more stable A⁻ → stronger (HF &lt; HCl &lt; HBr &lt; HI).",
     "Weak acid: K<sub>a</sub> = x²/(C − x) ≈ x²/C → [H⁺] = x ≈ √(K<sub>a</sub>C). From pH: [H⁺] = 10<sup>−pH</sup>.",
     "EQ:pH = pK<sub>a</sub> + log([A⁻]/[HA]) &nbsp; (base over acid)",
     "Buffer: weak acid + conjugate base, works at pK<sub>a</sub> ± 1; equal amounts → pH = pK<sub>a</sub>; ratio 10 → ±1. <b>Titration</b>: V<sub>eq</sub> = M<sub>A</sub>V<sub>A</sub>/M<sub>B</sub> moles match; midpoint (½V<sub>eq</sub>) pH = pK<sub>a</sub>; equivalence pH: strong/strong <b>7</b>, weak acid + strong base <b>&gt; 7</b>, weak base + strong acid <b>&lt; 7</b>. Polyprotic: lowest pK<sub>a</sub> leaves first (alanine COOH 2.34, NH₃⁺ 9.69).",
     "TRAP: pH 7 neutral and pH + pOH = 14 hold at 25 °C only; equivalence point ≠ midpoint."),
])

b3 = "".join([
 blk("c-ksp", "L28 · Solubility product K<sub>sp</sub>",
     "EQ:BaSO₄(s) ⇌ Ba²⁺ + SO₄²⁻ &nbsp; K<sub>sp</sub> = [Ba²⁺][SO₄²⁻]",
     "Solid left out; coefficients are exponents (Ca₃(PO₄)₂: [Ca²⁺]³[PO₄³⁻]²). Dissolution gives ions by coefficient × x.",
     '<table class="ref"><tr><th>type</th><th>K<sub>sp</sub> =</th><th>x =</th></tr>'
     '<tr><td>AB</td><td>x²</td><td>√K<sub>sp</sub></td></tr>'
     '<tr><td>AB₂ / A₂B</td><td>4x³</td><td>(K<sub>sp</sub>/4)<sup>1/3</sup></td></tr>'
     '<tr><td>A₃B₂</td><td>108x⁵</td><td>(K<sub>sp</sub>/108)<sup>1/5</sup></td></tr></table>',
     "x = <b>molar solubility</b>, not [ion]: Ca₃(PO₄)₂ [Ca²⁺] = 3x, [PO₄³⁻] = 2x. BaSO₄ 1.5×10⁻⁹ → 3.87×10⁻⁵ M. PbI₂ 7.9×10⁻⁹ → [Pb²⁺] 1.25×10⁻³, [I⁻] 2.5×10⁻³ M.",
     "<b>Compare K<sub>sp</sub> only for the same formula type</b>: AgCl 1.8×10⁻¹⁰ (x 1.3×10⁻⁵) vs Ag₂CrO₄ 1.1×10⁻¹² (x 6.5×10⁻⁵ — larger solubility).",
     "<b>Q vs K<sub>sp</sub></b>: Q &lt; K<sub>sp</sub> unsaturated (more dissolves) · = saturated · <b>Q &gt; K<sub>sp</sub> precipitates</b>. Mixing: dilute each ion by the <b>total volume</b> first.",
     "<b>Common ion</b> lowers solubility: PbI₂ in 0.1 M NaI → [I⁻] ≈ 0.1, [Pb²⁺] = K<sub>sp</sub>/0.01 = 7.9×10⁻⁷ M (1600× lower). <b>pH</b>: basic anions (OH⁻, CO₃²⁻, PO₄³⁻, F⁻) dissolve more in acid; Mg(OH)₂ less soluble at high pH.",
     "<b>Complexation</b>: ligand binds the metal ion → lowers free [M], Q &lt; K<sub>sp</sub>, solid dissolves (opposite of common ion). EQ:K<sub>f</sub> = K₁K₂K₃K₄",
     "Big K<sub>f</sub> = stable. Chelators (EDTA, 6 donor atoms) are extreme. AgBr + S₂O₃²⁻ → [Ag(S₂O₃)₂]³⁻ (K<sub>f</sub> 2.9×10¹³) fixes film; Nd/Dy magnet recycling: ligand holds Nd³⁺, Dy precipitates. Karst: CaCO₃ + CO₂ + H₂O ⇌ Ca²⁺ + 2HCO₃⁻ (reverse deposits stalactites)."),
 blk("c-ksp", "Order of attack for any problem",
     "① write the balanced equation · ② write K / K<sub>sp</sub> / rate law (solids out) · ③ units: K, J vs kJ, K not °C · ④ RICE or Q vs K · ⑤ sanity check (does the sign / direction match Le Châtelier?) · ⑥ “briefly explain” needs a <b>reason</b>, not just the answer."),
])

def sheet(title, sub, cols):
    return ('<div class="sheet"><div class="head"><div class="t1">%s</div><div class="t2">%s</div></div><div class="cols">%s</div></div>'
            % (title, sub, "".join('<div class="col">%s</div>' % c for c in cols)))

body = ('<body>\n<div class="screen-chrome"><h1>3.091 &mdash; Exam 3 Aid Sheet (front and back)</h1>'
        '<p>L21&ndash;L28 &middot; Rec 14&ndash;20. Print double-sided on letter paper at <span class="kbd">100%</span> scale, margins none, background graphics on. '
        'Check that this year&rsquo;s rules allow a double-sided sheet; side 1 (kinetics, thermodynamics, equilibrium) stands alone if only one side is allowed.</p></div>\n'
        + sheet("3.091 Exam 3 &middot; side 1", "<b>Kinetics &rarr; Gibbs free energy, enthalpy, entropy &rarr; equilibrium</b> (L21&ndash;L24, Rec 14&ndash;17)", [a1, a2, a3])
        + "\n"
        + sheet("3.091 Exam 3 &middot; side 2", "<b>Equilibrium tools &rarr; catalysis &rarr; solutions &rarr; acids &amp; bases &rarr; K<sub>sp</sub></b> (L24&ndash;L28, Rec 17&ndash;20)", [b1, b2, b3])
        + "\n</body>\n</html>\n")
open(os.path.join(ROOT, "aid-sheet-exam3.html"), "w", encoding="utf-8").write(head + body)
print("wrote aid-sheet-exam3.html")
