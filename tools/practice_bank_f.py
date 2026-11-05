from practice_lib import *
import math

R = 8.314
EXTRA = '<span class="pill" style="--c:var(--ink-soft);--c-soft:var(--line-soft)">extra</span>'

# ================================================================== KINETICS (L21, L22, Rec 14-15)
topic("kinetics", "Reaction rates &amp; mechanisms", "unit12", "Quiz 7",
      "Quiz 7 (Fall 2024) tests Arrhenius plots and catalysts; the 2026 lectures add rate laws and mechanisms. Recipe: "
      "<b>rate</b> = &minus;(1/a)d[A]/dt; <b>rate law</b> v = k[A]<sup>&alpha;</sup>[B]<sup>&beta;</sup> (exponents from experiment, equal to the coefficients only for an elementary step); "
      "integrated laws: zeroth [A] = [A]<sub>0</sub> &minus; kt, first ln[A] = ln[A]<sub>0</sub> &minus; kt, second 1/[A] = 1/[A]<sub>0</sub> + kt; "
      "Arrhenius k = Ae<sup>&minus;E<sub>a</sub>/RT</sup> so ln k vs 1/T has slope &minus;E<sub>a</sub>/R; the slowest step of a mechanism sets the rate law.")

rate_C = 0.90
rate_A = rate_C * 2 / 3
num("kinetics-1", "kinetics", 2, "Rec 14 style",
    "For the reaction <b>2A + B &rarr; 3C</b>, product C forms at <b>0.90 M/s</b>. How fast is A being consumed, as a positive number in M/s?",
    rate_A, "M/s",
    "<p>One reaction rate v describes everything: v = &minus;&frac12; d[A]/dt = &minus;d[B]/dt = +&#8531; d[C]/dt (divide each species&rsquo; rate by its coefficient).</p>"
    "<p>v = 0.90/3 = 0.30 M/s, so &minus;d[A]/dt = 2 &times; v = <b>%s M/s</b>. B is consumed at 0.30 M/s.</p>" % fmt(rate_A, 3),
    hint="v = (1/coefficient) &times; (rate for that species).", text="%s M/s" % fmt(rate_A, 3))

avg = (0.80 - 0.50) / 15
num("kinetics-2", "kinetics", 1, "L21 slide 5",
    "The concentration of a reactant falls from <b>0.80 M to 0.50 M</b> in 15 s. What is the <b>average rate</b> of reaction, in M/s?",
    avg, "M/s",
    "<p>Average rate = &minus;&Delta;[A]/&Delta;t = (0.80 &minus; 0.50) / 15 = <b>%s M/s</b>. (The <em>instantaneous</em> rate at one moment is the slope of the tangent to the curve; the average rate is the slope of the chord between two times, so it depends on the interval you pick: L21 slide 5 gives 2.0&times;10<sup>&minus;5</sup> M/h for the first 2 h but 8.2&times;10<sup>&minus;6</sup> M/h between 200 and 300 h.)</p>" % fmt(avg, 3),
    text="%s M/s" % fmt(avg, 3))

mc("kinetics-3", "kinetics", 3, "L22 slide 12",
   "Initial-rate data for A + B &rarr; products at constant temperature:<br>Exp 1: [A] = 0.10, [B] = 0.10 M, rate = 2.0&times;10<sup>&minus;3</sup> M/s<br>Exp 2: [A] = 0.20, [B] = 0.10 M, rate = 8.0&times;10<sup>&minus;3</sup> M/s<br>Exp 3: [A] = 0.10, [B] = 0.20 M, rate = 4.0&times;10<sup>&minus;3</sup> M/s<br>What is the rate law?",
   ["rate = k[A]&sup2;[B] (third order overall)", "rate = k[A][B] (second order)", "rate = k[A][B]&sup2;", "rate = k[A]&sup2;[B]&sup2;"],
   "<p>Change one concentration at a time and compare ratios: v<sub>2</sub>/v<sub>1</sub> = ([A]<sub>2</sub>/[A]<sub>1</sub>)<sup>&alpha;</sup>.</p>"
   "<ul><li>Exp 2 vs 1: [A] doubles, rate &times;4, so 2<sup>&alpha;</sup> = 4, &alpha; = 2.</li><li>Exp 3 vs 1: [B] doubles, rate &times;2, so &beta; = 1.</li></ul>"
   "<p>rate = k[A]&sup2;[B], total order 3. (The exponents come from the data, not from the equation&rsquo;s coefficients.)</p>",
   hint="Ratio of rates = (ratio of concentrations)<sup>order</sup>.")

k_val = 2.0e-3 / (0.10 ** 2 * 0.10)
num("kinetics-4", "kinetics", 3, "L22 slide 12",
    "Using the rate law rate = k[A]&sup2;[B] from the data above (Exp 1: [A] = [B] = 0.10 M, rate = 2.0&times;10<sup>&minus;3</sup> M/s), find k. Units: M<sup>&minus;2</sup>s<sup>&minus;1</sup>.",
    k_val, "M<sup>&minus;2</sup>s<sup>&minus;1</sup>",
    "<p>k = rate / ([A]&sup2;[B]) = 2.0&times;10<sup>&minus;3</sup> / (0.10&sup2; &times; 0.10) = 2.0&times;10<sup>&minus;3</sup> / 1.0&times;10<sup>&minus;3</sup> = <b>%s M<sup>&minus;2</sup>s<sup>&minus;1</sup></b>. The units of k always make k&middot;[conc]<sup>order</sup> come out as M/s.</p>" % fmt(k_val, 2),
    text="%s M<sup>&minus;2</sup>s<sup>&minus;1</sup>" % fmt(k_val, 2))

mc("kinetics-5", "kinetics", 1, "Rec 15 / L22",
   "Match the units of the rate constant k to the reaction order: zeroth, first, second.",
   ["zeroth: M/s &nbsp; first: s<sup>&minus;1</sup> &nbsp; second: M<sup>&minus;1</sup>s<sup>&minus;1</sup>", "zeroth: s<sup>&minus;1</sup> &nbsp; first: M/s &nbsp; second: M<sup>&minus;1</sup>s<sup>&minus;1</sup>", "zeroth: M<sup>&minus;1</sup>s<sup>&minus;1</sup> &nbsp; first: s<sup>&minus;1</sup> &nbsp; second: M/s", "all are s<sup>&minus;1</sup>"],
   "<p>Rate has units M/s. Zeroth: rate = k so k is M/s. First: rate = k[A] so k = (M/s)/M = s<sup>&minus;1</sup>. Second: rate = k[A]&sup2; so k = (M/s)/M&sup2; = M<sup>&minus;1</sup>s<sup>&minus;1</sup>. Shortcut: the unit of k tells you the order.</p>")

t_half = math.log(2) / 0.0231
num("kinetics-6", "kinetics", 1, "Rec 15 slide 25",
    "A first-order decay has k = 0.0231 s<sup>&minus;1</sup>. What is the half-life in seconds?",
    t_half, "s",
    "<p>For first order t<sub>1/2</sub> = ln 2 / k = 0.693 / 0.0231 = <b>%s s</b>. It does not depend on the starting concentration (that is how you recognise first order; radioactive decay is first order).</p>" % fmt(t_half, 3),
    tol=0.01, text="%s s" % fmt(t_half, 3))

A_t = 0.80 * math.exp(-0.050 * 20)
num("kinetics-7", "kinetics", 2, "L22 slide 10",
    "A first-order reaction has k = 0.050 min<sup>&minus;1</sup> and [A]<sub>0</sub> = 0.80 M. What is [A] after 20 min, in M?",
    A_t, "M",
    "<p>[A] = [A]<sub>0</sub>e<sup>&minus;kt</sup> = 0.80 &times; e<sup>&minus;0.050&times;20</sup> = 0.80 &times; e<sup>&minus;1</sup> = 0.80 &times; 0.3679 = <b>%s M</b>. (kt = 1 means one time constant, 63%% gone.)</p>" % fmt(A_t, 3),
    tol=0.01, text="%s M" % fmt(A_t, 3))

t2 = (1 / 0.10 - 1 / 0.50) / 0.20
num("kinetics-8", "kinetics", 3, "L22 slide 10",
    "A second-order reaction (rate = k[A]&sup2;) has k = 0.20 M<sup>&minus;1</sup>s<sup>&minus;1</sup> and [A]<sub>0</sub> = 0.50 M. How long, in seconds, until [A] = 0.10 M?",
    t2, "s",
    "<p>Second order: 1/[A] = 1/[A]<sub>0</sub> + kt. So kt = 1/0.10 &minus; 1/0.50 = 10 &minus; 2 = 8 M<sup>&minus;1</sup>, and t = 8/0.20 = <b>%s s</b>.</p>" % fmt(t2, 3),
    hint="Use the 1/[A] form.", text="%s s" % fmt(t2, 3))

mc("kinetics-9", "kinetics", 2, "L22 slide 11",
   "Data for a reaction give a <b>straight line when you plot 1/[A] against time</b>. What is the order and what does the slope equal?",
   ["Second order; slope = +k", "First order; slope = &minus;k", "Zeroth order; slope = &minus;k", "Second order; slope = &minus;k"],
   "<p>Straight-line test: [A] vs t straight &rarr; zeroth (slope &minus;k); ln[A] vs t straight &rarr; first (slope &minus;k); 1/[A] vs t straight &rarr; second (slope <b>+k</b>, because 1/[A] grows).</p>")

ratio = math.exp(50000 / R * (1 / 300 - 1 / 310))
num("kinetics-10", "kinetics", 3, "L21 slide 6",
    "A reaction has activation energy E<sub>a</sub> = 50 kJ/mol. By what factor does its rate constant increase when the temperature goes from 300 K to 310 K? (R = 8.314 J/(mol&middot;K))",
    ratio, "&times;",
    "<p>k<sub>2</sub>/k<sub>1</sub> = exp[(E<sub>a</sub>/R)(1/T<sub>1</sub> &minus; 1/T<sub>2</sub>)] (A cancels). E<sub>a</sub>/R = 50000/8.314 = %s K. 1/300 &minus; 1/310 = 1.075&times;10<sup>&minus;4</sup> K<sup>&minus;1</sup>. Exponent = %s, so the ratio is e<sup>%s</sup> = <b>%s</b>: roughly doubling per 10 K near room temperature.</p>" % (fmt(50000 / R, 4), fmt(50000 / R * (1 / 300 - 1 / 310), 3), fmt(50000 / R * (1 / 300 - 1 / 310), 3), fmt(ratio, 3)),
    tol=0.02, text="%s&times;" % fmt(ratio, 3))

Ea_calc = R * math.log(8.0e-3 / 2.0e-3) / (1 / 300 - 1 / 330) / 1000
num("kinetics-11", "kinetics", 3, "Quiz 7 style",
    "A rate constant is 2.0&times;10<sup>&minus;3</sup> s<sup>&minus;1</sup> at 300 K and 8.0&times;10<sup>&minus;3</sup> s<sup>&minus;1</sup> at 330 K. Find the activation energy in <b>kJ/mol</b>.",
    Ea_calc, "kJ/mol",
    "<p>ln(k<sub>2</sub>/k<sub>1</sub>) = (E<sub>a</sub>/R)(1/T<sub>1</sub> &minus; 1/T<sub>2</sub>) (this is the slope &minus;E<sub>a</sub>/R of the Arrhenius plot between two points). ln 4 = 1.386; 1/300 &minus; 1/330 = 3.03&times;10<sup>&minus;4</sup>. E<sub>a</sub> = 8.314 &times; 1.386 / 3.03&times;10<sup>&minus;4</sup> = %s J/mol = <b>%s kJ/mol</b>.</p>" % (fmt(Ea_calc * 1000, 4), fmt(Ea_calc, 3)),
    tol=0.02, text="%s kJ/mol" % fmt(Ea_calc, 3))

mc("kinetics-12", "kinetics", 2, "Quiz 7 style",
   "On a plot of ln k against 1/T, two reactions give straight lines. Line 1 is <b>steeper</b> than line 2. Which is correct? What would removing a catalyst do to a line?",
   ["Reaction 1 has the larger E<sub>a</sub>; removing a catalyst raises E<sub>a</sub> and makes a line steeper", "Reaction 1 has the smaller E<sub>a</sub>; removing a catalyst makes the line shallower", "Reaction 1 is always faster; a catalyst changes only the intercept", "Slope equals ln A, so a catalyst changes the slope by changing A only"],
   "<p>Slope = &minus;E<sub>a</sub>/R, so steeper = larger E<sub>a</sub>. A catalyst lowers E<sub>a</sub> (shallower line, larger k at every T); take it away and E<sub>a</sub> rises: steeper line (the real Quiz 7 answer). Steeper does not mean faster. Also remember 1/T grows to the right, so hot is on the left.</p>")

mc("kinetics-13", "kinetics", 2, "L21 slides 7 &amp; 12 &middot; Rec 15",
   "In collision theory, which set of conditions must all be met for a reaction to occur?",
   ["Particles collide, with the right orientation, with energy at least E<sub>a</sub>", "Particles collide and the reaction is exothermic", "Particles collide at any orientation with any energy", "Particles are in the same phase and &Delta;G &lt; 0"],
   "<p>Three requirements: <b>collision</b>, <b>orientation</b> (the steric factor p, between 0 and 1: fraction of collisions with a reactive orientation) and <b>energy &ge; E<sub>a</sub></b> (only the shaded tail of the Boltzmann distribution). Collision frequency and the steric factor are folded into the pre-exponential factor A. More mobile = more collisions: gas &gt; liquid &gt; solid. At higher T a much larger fraction exceeds E<sub>a</sub>.</p>")

Ea_rev = 9.6 + 200.8
num("kinetics-14", "kinetics", 2, "L21 slide 8 &middot; extra",
    "For NO + O<sub>3</sub> &rarr; NO<sub>2</sub> + O<sub>2</sub> the forward activation energy is 9.6 kJ/mol and &Delta;E = &minus;200.8 kJ/mol. What is the activation energy of the <b>reverse</b> reaction, in kJ/mol? %s" % EXTRA,
    Ea_rev, "kJ/mol",
    "<p>On the energy diagram the products sit 200.8 kJ/mol <em>below</em> the reactants, and the barrier is measured from the activated complex. Going backwards you must climb from the products to the same top: E<sub>a,rev</sub> = E<sub>a,fwd</sub> + |&Delta;E| = 9.6 + 200.8 = <b>%s kJ/mol</b>. (E<sub>a</sub> is always positive; &Delta;E&lt;0 means exothermic.)</p>" % fmt(Ea_rev, 4),
    tol=0.01, text="%s kJ/mol" % fmt(Ea_rev, 4))

mc("kinetics-15", "kinetics", 2, "L21 slide 11",
   "Which statement about a catalyst and an energy diagram is correct?",
   ["It lowers E<sub>a</sub> (a lower barrier) and leaves &Delta;E of the reaction unchanged", "It lowers &Delta;E so the products become more stable", "It raises the energy of the reactants", "It makes E<sub>a</sub> negative"],
   "<p>Kinetics vs energetics: <b>E<sub>a</sub></b> controls the rate and how it changes with temperature; <b>&Delta;E</b> (and &Delta;G) says whether the reaction is favourable. A catalyst offers a different path with a lower barrier (often several small humps, Rec 14) but the same reactants and products, so the same &Delta;E. E<sub>a</sub> is always greater than 0.</p>")

mc("kinetics-16", "kinetics", 2, "L22 slides 14&ndash;15",
   "For which reaction can you write the rate law straight from the coefficients, rate = k[A]&sup2;[B]?",
   ["2A + B &rarr; products, if it is stated to be a single elementary step", "2A + B &rarr; products, for any reaction with that equation", "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub> &rarr; 6CO<sub>2</sub> + 6H<sub>2</sub>O", "H<sub>2</sub> + Cl<sub>2</sub> &rarr; 2HCl"],
   "<p>Only for an <b>elementary reaction</b>, where the molecules really collide in the stoichiometric proportions, does order = molecularity = coefficients. Complex reactions (glucose oxidation) are surely non-elementary, and even &ldquo;simple&rdquo; ones deceive you: H<sub>2</sub> + Cl<sub>2</sub> &rarr; 2HCl goes by a chain mechanism and its rate is proportional to [Cl<sub>2</sub>]<sup>0.5</sup>[H<sub>2</sub>] (L22 slide 16).</p>")

mc("kinetics-17", "kinetics", 3, "L22 slides 17&ndash;19",
   "Mechanism for NO<sub>2</sub> + CO &rarr; NO + CO<sub>2</sub>: step 1 NO<sub>2</sub> + NO<sub>2</sub> &rarr; NO<sub>3</sub> + NO (<b>slow</b>); step 2 NO<sub>3</sub> + CO &rarr; NO<sub>2</sub> + CO<sub>2</sub> (fast). What rate law does the mechanism predict?",
   ["rate = k[NO<sub>2</sub>]&sup2;", "rate = k[NO<sub>2</sub>][CO]", "rate = k[NO<sub>3</sub>][CO]", "rate = k[NO<sub>2</sub>]&sup2;[CO]"],
   "<p>The overall rate is set by the slow (rate-limiting) step, and that step is elementary, so its rate law follows its coefficients: rate = k[NO<sub>2</sub>]&sup2;. CO enters only after the bottleneck, so it does not appear. This matches the experimental rate law on slide 19. Check the mechanism: step 1 + step 2 adds up to NO<sub>2</sub> + CO &rarr; NO + CO<sub>2</sub> (NO<sub>3</sub> cancels: it is an <b>intermediate</b>).</p>")

mc("kinetics-18", "kinetics", 2, "L22 slide 18",
   "In a multi-step mechanism, what happens to the intermediates <b>made before</b> the rate-limiting step?",
   ["They accumulate, like water piling up above the narrow funnel", "They are used up instantly", "They are the products", "They have no effect on anything"],
   "<p>The slow step is the bottleneck: material produced by the fast steps before it waits (&ldquo;hold-up&rdquo; on the energy profile), while steps after it run quickly once material gets through. L22 slide 18 compares it to stacked funnels.</p>")

mc("kinetics-19", "kinetics", 1, "L22 slide 14",
   "An elementary step 2A + B &rarr; products is&hellip;",
   ["termolecular, third order overall (rate = k[A]&sup2;[B])", "bimolecular, second order", "unimolecular, first order", "bimolecular, rate = k[A][B]"],
   "<p>Molecularity = how many particles collide in the step: 3 here. Order equals molecularity for an elementary step. Three-body encounters are very rare, so third-order reactions are uncommon and none are higher.</p>")

mc("kinetics-20", "kinetics", 2, "L21 slide 15 (Future Five)",
   "Heated BaO + TiO<sub>2</sub> could form several Ba&ndash;Ti&ndash;O crystals. Why can the product at 1100&ndash;1700 K differ from the lowest-free-energy one?",
   ["Ion transport (diffusion, which follows an Arrhenius law) differs between candidate products, so kinetics decides which phase forms first", "Thermodynamics is wrong at high temperature", "The reaction has &Delta;G &gt; 0", "Catalysts change &Delta;G"],
   "<p>L21&rsquo;s Future Five: &ldquo;Thermodynamics tells us the destination. Kinetics controls the journey.&rdquo; D = D<sub>0</sub>exp(&minus;E<sub>a</sub>/RT) sets how fast ions cross the interface: below about 1100 K everything is slow, between 1100 and 1700 K ion mobility selects the phase, above 1700 K transport is fast and thermodynamics dominates.</p>")

num("kinetics-21", "kinetics", 1, "Rec 14 style",
    "Balance 4P + <b>?</b> O<sub>2</sub> &rarr; 2P<sub>2</sub>O<sub>5</sub> for the number of O<sub>2</sub> molecules, then state how many <b>moles of O<sub>2</sub></b> react with 2.0 mol of P.",
    2.5, "mol",
    "<p>Right side: 2 P<sub>2</sub>O<sub>5</sub> = 4 P and 10 O, so 5 O<sub>2</sub>: <b>4P + 5O<sub>2</sub> &rarr; 2P<sub>2</sub>O<sub>5</sub></b> (balance the most complex formula first). Ratio 5 O<sub>2</sub> : 4 P, so 2.0 mol P needs 2.0 &times; 5/4 = <b>2.5 mol O<sub>2</sub></b>.</p>",
    tol=0.0, atol=0.01, text="2.5 mol")

v = 0.50 * 0.20 * 0.30 ** 2
num("kinetics-22", "kinetics", 1, "Rec 14 style",
    "A reaction has rate law rate = k[A][B]&sup2; with k = 0.50 M<sup>&minus;2</sup>s<sup>&minus;1</sup>. Find the rate when [A] = 0.20 M and [B] = 0.30 M, in M/s.",
    v, "M/s",
    "<p>rate = 0.50 &times; 0.20 &times; (0.30)&sup2; = 0.50 &times; 0.20 &times; 0.090 = <b>%s M/s</b>.</p>" % fmt(v, 3),
    tol=0.01, text="%s M/s" % fmt(v, 3))

selfq("kinetics-23", "kinetics", 3, "Rec 15 problem 1",
      "Fill in the table for zeroth, first and second order: differential rate law, integrated rate law, units of k, shape of [A] vs t, and the linearised plot with its slope.",
      "<div class=\"tscroll\"><table class=\"data\"><thead><tr><th></th><th>zeroth</th><th>first</th><th>second</th></tr></thead><tbody>"
      "<tr><td>d[A]/dt</td><td>&minus;k</td><td>&minus;k[A]</td><td>&minus;k[A]&sup2;</td></tr>"
      "<tr><td>integrated</td><td>[A] = [A]<sub>0</sub> &minus; kt</td><td>[A] = [A]<sub>0</sub>e<sup>&minus;kt</sup></td><td>1/[A] = 1/[A]<sub>0</sub> + kt</td></tr>"
      "<tr><td>units of k</td><td>M/s</td><td>s<sup>&minus;1</sup></td><td>M<sup>&minus;1</sup>s<sup>&minus;1</sup></td></tr>"
      "<tr><td>[A] vs t</td><td>straight line down</td><td>exponential decay</td><td>faster-then-slower decay (hyperbola)</td></tr>"
      "<tr><td>linearised</td><td>[A] vs t, slope &minus;k</td><td>ln[A] vs t, slope &minus;k</td><td>1/[A] vs t, slope +k</td></tr>"
      "<tr><td>half-life</td><td>[A]<sub>0</sub>/2k</td><td>ln 2 / k</td><td>1/(k[A]<sub>0</sub>)</td></tr></tbody></table></div>"
      "<p class=\"small\">Only the first-order half-life is on the slides (Rec 15 slide 25); the other two follow from the integrated laws. %s</p>" % EXTRA)

# ================================================================== THERMODYNAMICS (L23)
topic("thermo", "Thermodynamics: spontaneity &amp; free energy", "unit13", "Exam 3",
      "L23: <b>&Delta;G = &Delta;H &minus; T&Delta;S</b>. &Delta;G &lt; 0 spontaneous, &Delta;G = 0 equilibrium, &Delta;G &gt; 0 not spontaneous. "
      "Sign table: &Delta;H &lt; 0, &Delta;S &gt; 0 always spontaneous; &Delta;H &gt; 0, &Delta;S &lt; 0 never; the mixed cases flip at T = &Delta;H/&Delta;S. "
      "&minus;&Delta;G is the maximum useful (non-PV) work. Spontaneous does not mean fast (that is kinetics).")

mc("thermo-1", "thermo", 1, "L23 slide 7",
   "A reaction has &Delta;H &lt; 0 and &Delta;S &gt; 0. When is it spontaneous?",
   ["At all temperatures", "Only at high temperature", "Only at low temperature", "At no temperature"],
   "<p>&Delta;G = &Delta;H &minus; T&Delta;S: &Delta;H is negative and &minus;T&Delta;S is negative too, so &Delta;G is negative whatever T is.</p>")

mc("thermo-2", "thermo", 2, "L23 slide 7",
   "A reaction has &Delta;H &lt; 0 and &Delta;S &lt; 0. It is spontaneous&hellip;",
   ["only at low temperature (the &minus;T&Delta;S term becomes positive and wins when T is high)", "only at high temperature", "at all temperatures", "at no temperature"],
   "<p>&minus;T&Delta;S is positive, growing with T. At low T the negative &Delta;H dominates (spontaneous); at high T the entropy penalty dominates. The other mixed case (&Delta;H &gt; 0, &Delta;S &gt; 0) is spontaneous only at high T, like boiling; &Delta;H &gt; 0, &Delta;S &lt; 0 never.</p>")

dG = -92 - 298 * (-0.199)
num("thermo-3", "thermo", 2, "L23 slide 9",
    "For N<sub>2</sub> + 3H<sub>2</sub> &rarr; 2NH<sub>3</sub>: &Delta;H&deg; = &minus;92 kJ and &Delta;S&deg; = &minus;199 J/K. Find &Delta;G&deg; at 298 K in kJ.",
    dG, "kJ",
    "<p>Convert &Delta;S to kJ/K: &minus;0.199. &Delta;G&deg; = &Delta;H&deg; &minus; T&Delta;S&deg; = &minus;92 &minus; 298(&minus;0.199) = &minus;92 + 59.3 = <b>%s kJ</b>: spontaneous at 298 K. (Units! J/K vs kJ is the usual slip.)</p>" % fmt(dG, 4),
    hint="Put &Delta;S in kJ/K before multiplying.", tol=0.02, text="%s kJ" % fmt(dG, 4))

Tcross = 92 / 0.199
num("thermo-4", "thermo", 3, "L23 slide 7",
    "For the same reaction (&Delta;H = &minus;92 kJ, &Delta;S = &minus;199 J/K), at what temperature does &Delta;G change sign? Give the answer in kelvin; the reaction is spontaneous <b>below</b> it.",
    Tcross, "K",
    "<p>&Delta;G = 0 at T = &Delta;H/&Delta;S = (&minus;92)/(&minus;0.199) = <b>%s K</b>. Below that temperature the enthalpy term wins (spontaneous); above it the entropy term wins (not spontaneous).</p>" % fmt(Tcross, 3),
    tol=0.02, text="%s K" % fmt(Tcross, 3))

T_vap = 44.0 / 0.118
num("thermo-5", "thermo", 2, "L23 slide 8",
    "Evaporating water has &Delta;H<sub>vap</sub> = +44.0 kJ/mol and &Delta;S<sub>vap</sub> = +118 J/(mol&middot;K). At what temperature (K) are liquid and vapour in equilibrium?",
    T_vap, "K",
    "<p>Equilibrium means &Delta;G<sub>vap</sub> = 0, so T = &Delta;H/&Delta;S = 44000/118 = <b>%s K</b> (about 100 &deg;C). On the L23 plot the &Delta;H and T&Delta;S lines cross at that point; above it &Delta;G &lt; 0 and liquid water evaporates; below it &Delta;G &gt; 0 and the vapour condenses.</p>" % fmt(T_vap, 4),
    tol=0.01, text="%s K" % fmt(T_vap, 4))

mc("thermo-6", "thermo", 1, "L23 slide 8",
   "At the temperature where &Delta;G = 0 for a phase change, the two phases are&hellip;",
   ["in equilibrium", "both unstable", "converting only in one direction", "at 0 K"],
   "<p>&Delta;G &lt; 0: the forward process is spontaneous; &Delta;G &gt; 0: the reverse is spontaneous; &Delta;G = 0: neither direction is favoured, which is equilibrium (like liquid water and vapour at the boiling point).</p>")

dS = (-286 + 237) / 298 * 1000
num("thermo-7", "thermo", 3, "L23 slide 13",
    "For H<sub>2</sub>(g) + &frac12;O<sub>2</sub>(g) &rarr; H<sub>2</sub>O(l) at 25 &deg;C: &Delta;H&deg; = &minus;286 kJ/mol and &Delta;G&deg; = &minus;237 kJ/mol. Find &Delta;S&deg; in J/(mol&middot;K).",
    dS, "J/(mol&middot;K)",
    "<p>From &Delta;G = &Delta;H &minus; T&Delta;S: T&Delta;S = &Delta;H &minus; &Delta;G = &minus;286 &minus; (&minus;237) = &minus;49 kJ/mol. &Delta;S = &minus;49000 / 298 = <b>%s J/(mol&middot;K)</b>. It is negative because three moles of gas become one mole of liquid. That is why only 237 of the 286 kJ can be turned into work.</p>" % fmt(dS, 4),
    tol=0.03, text="%s J/(mol&middot;K)" % fmt(dS, 4))

mc("thermo-8", "thermo", 2, "L23 slides 10&ndash;13",
   "Why can a fuel cell + heat pump deliver <b>more heat</b> (572 kJ per mole of H<sub>2</sub>) than burning it (286 kJ)?",
   ["The fuel cell turns part of the free energy into work (143 kJ), and the heat pump uses that work to bring in 429 kJ of heat from outside", "Burning H<sub>2</sub> releases less energy than the fuel cell", "A heat pump creates energy", "&Delta;G is larger than &Delta;H"],
   "<p>Burning wastes the fuel&rsquo;s capacity to do work. Fuel cell at 50% of 286 kJ = 143 kJ of electricity. A heat pump with COP<sub>h</sub> = 4 delivers 4 kJ of heat per 1 kJ of work: 4 &times; 143 = 572 kJ = 143 kJ work + <b>429 kJ outdoor heat</b>. Energy is conserved; the heat pump just moves heat.</p>")

num("thermo-9", "thermo", 2, "L23 slides 11&ndash;12",
    "Using 50% fuel-cell efficiency on 286 kJ of H<sub>2</sub> and a heat pump with COP = 4, how much of the delivered heat comes from <b>outside</b> (kJ)?",
    429.0, "kJ",
    "<p>Work = 0.50 &times; 286 = 143 kJ. Heat delivered = 4 &times; 143 = 572 kJ. Of that, 143 kJ is the work itself and 572 &minus; 143 = <b>429 kJ</b> is pumped in from outdoors (each 1 kJ of work moves 3 kJ).</p>",
    tol=0.01, text="429 kJ")

mc("thermo-10", "thermo", 2, "L21 slide 15 &middot; L23",
   "Diamond turning into graphite has &Delta;G &lt; 0 at room temperature, yet diamonds last for ages. What does this show?",
   ["Spontaneous (thermodynamically favourable) does not mean fast: the activation energy barrier makes the rate negligible", "&Delta;G is wrong", "Diamond is the more stable form", "Catalysts reverse &Delta;G"],
   "<p>&Delta;G tells the <b>direction</b> (the destination); the activation energy and rate constant tell the <b>speed</b> (the journey). A reaction can be strongly downhill and extremely slow.</p>")

mc("thermo-11", "thermo", 2, "L23 slide 9",
   "What is the <b>standard free energy of formation</b>, &Delta;G&deg;<sub>f</sub>?",
   ["The free-energy change when 1 mol of a compound in its standard state forms from its elements in their standard states", "The energy needed to break all bonds", "The heat released on combustion", "Always equal to &Delta;H&deg;<sub>f</sub>"],
   "<p>&Delta;G&deg;<sub>f</sub> = &Delta;H&deg;<sub>f</sub> &minus; T&Delta;S&deg;<sub>f</sub>, for 1 mol formed from the elements (which have &Delta;G&deg;<sub>f</sub> = 0 by definition).</p>")

T_calc = 178 / 0.161
num("thermo-12", "thermo", 3, "L23 slide 7",
    "CaCO<sub>3</sub>(s) &rarr; CaO(s) + CO<sub>2</sub>(g) has &Delta;H&deg; = +178 kJ and &Delta;S&deg; = +161 J/K. Above what temperature (K) does it become spontaneous?",
    T_calc, "K",
    "<p>&Delta;H &gt; 0 and &Delta;S &gt; 0: spontaneous only at high T. &Delta;G = 0 at T = 178 / 0.161 = <b>%s K</b>. (Entropy increases because a gas is released.)</p>" % fmt(T_calc, 4),
    tol=0.02, text="%s K" % fmt(T_calc, 4))

selfq("thermo-13", "thermo", 2, "L23 slide 7",
      "Fill in the spontaneity table for the four sign combinations of &Delta;H and &Delta;S, with one example reasoning for each.",
      "<div class=\"tscroll\"><table class=\"data\"><thead><tr><th></th><th>&Delta;H &lt; 0</th><th>&Delta;H &gt; 0</th></tr></thead><tbody>"
      "<tr><td><b>&Delta;S &gt; 0</b></td><td class=\"wrap\">spontaneous at <b>all</b> T</td><td class=\"wrap\">spontaneous at <b>high</b> T (melting, boiling, CaCO<sub>3</sub> decomposition)</td></tr>"
      "<tr><td><b>&Delta;S &lt; 0</b></td><td class=\"wrap\">spontaneous at <b>low</b> T (freezing, N<sub>2</sub> + 3H<sub>2</sub> &rarr; 2NH<sub>3</sub>)</td><td class=\"wrap\">spontaneous at <b>no</b> T</td></tr></tbody></table></div>"
      "<p>All four follow from &Delta;G = &Delta;H &minus; T&Delta;S: only the mixed cases change sign, at T = &Delta;H/&Delta;S.</p>")
