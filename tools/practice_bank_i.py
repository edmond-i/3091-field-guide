from practice_lib import *
import math

R = 8.314
# Recitation 17: extra questions for the topics defined in practice_bank_g.py (equil) and practice_bank_h.py (catalysis)

mc("equil-26", "equil", 2, "Rec 17 slide 5",
   "Step 1: A &rlarr; B + C (K<sub>1</sub>). Step 2: C + D &rlarr; E (K<sub>2</sub>). What is K for the net reaction A + D &rlarr; B + E?",
   ["K = K<sub>1</sub> &times; K<sub>2</sub> = [B][E] / ([A][D]) (the intermediate C cancels)", "K = K<sub>1</sub> + K<sub>2</sub>", "K = K<sub>1</sub> / K<sub>2</sub>", "K = [B][C][E] / ([A][C][D]) with [C] kept"],
   "<p>K<sub>1</sub> = [B][C]/[A] and K<sub>2</sub> = [E]/([C][D]). Multiplying, [C] cancels: K<sub>1</sub>K<sub>2</sub> = [B][E]/([A][D]), which is exactly the K of the net reaction.</p>")

Kov = 0.50 * 40.0
num("equil-27", "equil", 2, "Rec 17 slide 5",
    "Two consecutive steps have K<sub>1</sub> = 0.50 and K<sub>2</sub> = 40. What is K for the overall reaction?",
    Kov, "",
    "<p>K<sub>overall</sub> = K<sub>1</sub>K<sub>2</sub> = 0.50 &times; 40 = <b>%s</b>.</p>" % fmt(Kov, 3), text=fmt(Kov, 3))

mc("equil-28", "equil", 1, "Rec 17 slide 7",
   "Which three statements all describe a system at equilibrium?",
   ["Forward rate = reverse rate; Q = K; &Delta;G = 0", "Forward rate = 0; Q = 0; &Delta;G &lt; 0", "Q &gt; K; &Delta;G &gt; 0; reactants used up", "[reactants] = [products]; Q = 1; &Delta;G = &Delta;G&deg;"],
   "<p>Equilibrium is dynamic: both reactions run at equal rates, the quotient Q has reached K, and the free energy of the reaction is zero (nothing left to gain by moving either way).</p>")

dGn = 5000 + R * 298 * math.log(0.010)
num("equil-29", "equil", 3, "Rec 17 slide 10",
    "A reaction has &Delta;G&deg; = +5.0 kJ/mol. At 298 K the mixture has Q = 0.010. Find &Delta;G in kJ/mol. Which way does it run?",
    dGn / 1000.0, "kJ/mol",
    "<p>&Delta;G = &Delta;G&deg; + RT ln Q = 5000 + 8.314 &times; 298 &times; ln(0.010) = 5000 &minus; 11 410 = <b>%s kJ/mol</b>. Negative, so it runs <b>forward</b> even though &Delta;G&deg; &gt; 0: there is little product (Q &lt; K).</p>" % fmt(dGn / 1000.0, 3),
    hint="ln(0.010) = &minus;4.605; use joules with R.", text="%s kJ/mol" % fmt(dGn / 1000.0, 3))

dSn = 120 - R * math.log(0.10)
num("equil-30", "equil", 3, "Rec 17 slide 10",
    "&Delta;S&deg; = +120 J/(mol&middot;K) and Q = 0.10. Using &Delta;S = &Delta;S&deg; &minus; R ln Q, find &Delta;S in J/(mol&middot;K).",
    dSn, "J/(mol&middot;K)",
    "<p>&Delta;S = 120 &minus; 8.314 &times; ln(0.10) = 120 &minus; 8.314 &times; (&minus;2.303) = 120 + 19.1 = <b>%s J/(mol&middot;K)</b>. Q &lt; 1 (little product) means a larger entropy change than at standard state.</p>" % fmt(dSn, 4),
    text="%s J/(mol&middot;K)" % fmt(dSn, 4))

mc("equil-31", "equil", 2, "Rec 17 slide 10",
   "For ideal gases or ideal solutions, how does &Delta;H away from standard state compare with &Delta;H&deg;?",
   ["&Delta;H = &Delta;H&deg; (it does not depend on Q)", "&Delta;H = &Delta;H&deg; + RT ln Q", "&Delta;H = &Delta;H&deg; &minus; R ln Q", "&Delta;H = 0"],
   "<p>The slide lists &Delta;H = &Delta;H&deg; for ideal systems. It is the entropy (&Delta;S = &Delta;S&deg; &minus; R ln Q) and hence &Delta;G that carry the dependence on the mixture.</p>")

lnK298 = 92000 / (R * 298) - 199 / R
num("equil-32", "equil", 3, "Rec 17 slides 11&ndash;12",
    "Van&rsquo;t Hoff: ln K = &minus;&Delta;H&deg;/(RT) + &Delta;S&deg;/R (the Rec 17 slide prints the last term as &Delta;S&deg;/T, but the units only work with R). Using &Delta;H&deg; = &minus;92 kJ and &Delta;S&deg; = &minus;199 J/K for N<sub>2</sub> + 3H<sub>2</sub> &rarr; 2NH<sub>3</sub>, find ln K at 298 K.",
    lnK298, "",
    "<p>Both terms must be dimensionless: &minus;&Delta;H&deg;/(RT) = 92 000/(8.314 &times; 298) = 37.13 and &Delta;S&deg;/R = &minus;199/8.314 = &minus;23.93. Sum: <b>%s</b>, so K &asymp; 5.4&times;10<sup>5</sup>. (It comes from &Delta;H&deg; &minus; T&Delta;S&deg; = &minus;RT ln K divided by &minus;RT.)</p>" % fmt(lnK298, 4),
    hint="&Delta;H&deg;/(RT) and &Delta;S&deg;/R, both dimensionless.", text=fmt(lnK298, 4))

K500 = math.exp(92000 / (R * 500) - 199 / R)
num("equil-33", "equil", 3, "Rec 17 slides 11&ndash;12",
    "For the same reaction (&Delta;H&deg; = &minus;92 kJ, &Delta;S&deg; = &minus;199 J/K, assumed constant), find K at 500 K.",
    K500, "",
    "<p>ln K = 92 000/(8.314 &times; 500) &minus; 199/8.314 = 22.13 &minus; 23.93 = &minus;1.80, so K = e<sup>&minus;1.80</sup> = <b>%s</b>. K fell from 5&times;10<sup>5</sup> (298 K) to about 0.16: for an exothermic reaction K shrinks as T rises.</p>" % fmt(K500, 3),
    tol=0.03, text=fmt(K500, 3))

mc("equil-34", "equil", 2, "Rec 17 slides 9, 12",
   "A reaction is <b>endothermic</b> (&Delta;H&deg; &gt; 0). What happens to K when the temperature is raised?",
   ["K increases (van&rsquo;t Hoff; Le Ch&acirc;telier: heating favours the endothermic direction)", "K decreases", "K is unchanged", "K changes only if pressure changes"],
   "<p>ln K = &minus;&Delta;H&deg;/(RT) + &Delta;S&deg;/T: with &Delta;H&deg; &gt; 0 the negative first term shrinks in size as T rises, so ln K, and K, increase. Same answer as Le Ch&acirc;telier&rsquo;s temperature rule.</p>")

slope = -50000 / R
num("equil-35", "equil", 3, "Rec 17 slide 12 &middot; extra",
    "A reaction has &Delta;H&deg; = +50 kJ/mol. What is the slope of a plot of ln K against 1/T, in kelvin?",
    slope, "K",
    "<p>From ln K = &minus;(&Delta;H&deg;/R)(1/T) + &Delta;S&deg;/R the slope is &minus;&Delta;H&deg;/R = &minus;50 000/8.314 = <b>%s K</b>. Negative for an endothermic reaction: ln K rises as 1/T falls (hotter).</p>" % fmt(slope, 4),
    text="%s K" % fmt(slope, 4))

mc("equil-36", "equil", 1, "Rec 17 slide 9",
   "N<sub>2</sub>O<sub>4</sub>(g) &rlarr; 2NO<sub>2</sub>(g) at equilibrium is compressed into a smaller volume. What happens?",
   ["It shifts toward N<sub>2</sub>O<sub>4</sub> (the side with fewer moles of gas: 1 versus 2)", "It shifts toward NO<sub>2</sub>", "K increases", "Nothing, because the temperature is constant"],
   "<p>Compressing raises the pressure of both sides; the system minimizes the change by favouring the side with <b>fewer moles of gas</b>, here N<sub>2</sub>O<sub>4</sub> (1 mol) over 2NO<sub>2</sub> (2 mol). K does not change (only T changes K).</p>")

num("equil-37", "equil", 2, "Rec 17 slide 8 (RICE)",
    "A + B &rlarr; 2C has K = 4.0. Starting with 1.0 M A, 1.0 M B and no C, find [C] at equilibrium in M.",
    1.0, "M",
    "<p>Change: &minus;x, &minus;x, +2x. K = (2x)&sup2;/(1.0 &minus; x)&sup2; = 4.0. Square root: 2x/(1.0 &minus; x) = 2.0, so 2x = 2.0 &minus; 2.0x, x = 0.50. [C] = 2x = <b>1.0 M</b>; [A] = [B] = 0.50 M. Check: 1.0&sup2;/0.50&sup2; = 4.</p>",
    text="1.0 M")

num("equil-38", "equil", 3, "Rec 17 slide 8 (RICE)",
    "N<sub>2</sub>O<sub>4</sub> &rlarr; 2NO<sub>2</sub> has K = 0.20. Start with 1.0 M N<sub>2</sub>O<sub>4</sub> and no NO<sub>2</sub>. Find [NO<sub>2</sub>] at equilibrium in M. (Solve 4x&sup2; + 0.20x &minus; 0.20 = 0.)",
    0.4, "M",
    "<p>Change: N<sub>2</sub>O<sub>4</sub> &minus;x, NO<sub>2</sub> +2x. K = (2x)&sup2;/(1.0 &minus; x) = 0.20 &rArr; 4x&sup2; + 0.20x &minus; 0.20 = 0. Quadratic formula: x = (&minus;0.20 + &radic;(0.04 + 3.2))/8 = (&minus;0.20 + 1.80)/8 = 0.20. [NO<sub>2</sub>] = 2x = <b>0.40 M</b>; [N<sub>2</sub>O<sub>4</sub>] = 0.80 M. Check: 0.40&sup2;/0.80 = 0.20.</p>",
    hint="Use the quadratic formula, take the positive root.", text="0.40 M")

# ---------------- catalysis (Rec 17)
mc("catalysis-29", "catalysis", 1, "Rec 17 slides 13&ndash;14",
   "On a Sabatier volcano plot (rate vs bond strength to the catalyst), what limits the rate when the bond is <b>too strong</b> and when it is <b>too weak</b>?",
   ["Too strong: desorption of the product; too weak: activation of the reactant", "Too strong: activation of the reactant; too weak: desorption of the product", "Both are limited by the temperature", "Neither: the rate keeps rising with bond strength"],
   "<p>Strong binding keeps the product stuck on the surface (desorption-limited). Weak binding means the reactant will not bind or activate properly. The best catalysts sit in the middle: the Sabatier optimum.</p>")

mc("catalysis-30", "catalysis", 1, "Rec 17 slide 14",
   "Define adsorption and desorption on a heterogeneous catalyst.",
   ["Adsorption: a reactant binds to the catalyst surface; desorption: the product detaches from it", "Adsorption: a product leaves; desorption: a reactant binds", "Adsorption: the catalyst dissolves; desorption: it is rebuilt", "They are the same thing"],
   "<p>Adsorption = binding to the surface (reactant). Desorption = detaching from the surface (product).</p>")

mc("catalysis-31", "catalysis", 1, "Rec 17 slide 13",
   "A catalyst is added to a reaction already at equilibrium. According to Rec 17, what happens to the forward rate, the reverse rate and K?",
   ["Both rates increase equally; K is unchanged; equilibrium is reached faster if disturbed", "Only the forward rate increases; K increases", "Both rates decrease; K decreases", "Rates are unchanged; K increases"],
   "<p>A catalyst lowers E<sub>a</sub> for the forward and reverse reactions alike; it speeds both, so the system reaches equilibrium faster, but the equilibrium composition and K stay the same.</p>")

mc("catalysis-32", "catalysis", 2, "Rec 17 slide 13",
   "Pepsin dissolved in stomach acid breaks down dissolved proteins. In Rec 17&rsquo;s classification this is&hellip;",
   ["a homogeneous catalyst (same phase as the reactants)", "a heterogeneous catalyst (different phase)", "not a catalyst, because it is a protein", "a catalyst that changes K"],
   "<p>Rec 17 slide 13: homogeneous = catalyst in the same phase as the reactants, e.g. enzymes dissolved in the stomach breaking down dissolved food. Heterogeneous = a different phase, usually a solid catalyst.</p>")

mc("catalysis-33", "catalysis", 2, "Rec 17 slide 15",
   "On the slide-15 volcano (temperature needed vs metal &Delta;H<sub>f</sub>), Pt and Ir need about 350 K while Au and W need about 500&ndash;530 K. What does this show?",
   ["Metals with intermediate binding (Pt, Ir, Ru, Pd, Rh) are the best catalysts; Au (too weak) and W (too strong) are poor", "Au and W are the best catalysts", "The needed temperature does not depend on the metal", "Heavier metals are always better"],
   "<p>A lower needed temperature means a better catalyst. The best metals sit at intermediate &Delta;H<sub>f</sub> near the top of the volcano; very weak (Au, Ag) and very strong (Ni, Co, Fe, W) binders are less active (Sabatier&rsquo;s principle).</p>")

selfq("catalysis-34", "catalysis", 3, "Rec 17 slides 13&ndash;15",
      "Explain the Sabatier principle and why the volcano plot has a peak. Mention adsorption and desorption.",
      "<p><b>Model answer.</b> A heterogeneous catalyst first <b>adsorbs</b> the reactant onto its surface, the reaction happens there, and then the product must <b>desorb</b>. If the bond to the surface is too weak the reactant does not bind or become activated (rate limited by activation of the reactant). If the bond is too strong the product stays stuck (rate limited by desorption of the product). The rate is therefore highest at an intermediate bond strength, the Sabatier optimum, giving a volcano-shaped plot of rate against bond strength.</p>")
