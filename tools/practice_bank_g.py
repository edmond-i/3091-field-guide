from practice_lib import *
import math

R = 8.314
T0 = 298.0

# ================================================================== EQUILIBRIUM (L24)
topic("equil", "Chemical equilibrium: K, Q &amp; &Delta;G&deg;", "unit14", "Quiz 8",
      "Quiz 8 (Fall 2024) asks for K or equilibrium amounts from a RICE table, and qualitative Le Ch&acirc;telier questions. Recipe: "
      "<b>K</b> = products over reactants, each raised to its coefficient, no units, no solids or liquids; "
      "<b>K &lt; 10<sup>&minus;3</sup></b> mostly reactants, <b>K &gt; 10<sup>3</sup></b> mostly products (L24); "
      "<b>Q</b> uses the same expression at any moment: <b>Q &lt; K &rarr; right, Q &gt; K &rarr; left</b>; "
      "&Delta;G&deg; = &minus;RT ln K (extra); only temperature changes K.")

mc("equil-1", "equil", 1, "L24 slide 8",
   "Write the equilibrium constant for <b>N<sub>2</sub>(g) + 3H<sub>2</sub>(g) &rlarr; 2NH<sub>3</sub>(g)</b>.",
   ["K = [NH<sub>3</sub>]&sup2; / ([N<sub>2</sub>][H<sub>2</sub>]&sup3;)", "K = [N<sub>2</sub>][H<sub>2</sub>]&sup3; / [NH<sub>3</sub>]&sup2;", "K = [NH<sub>3</sub>] / ([N<sub>2</sub>][H<sub>2</sub>])", "K = 2[NH<sub>3</sub>] / (3[H<sub>2</sub>] + [N<sub>2</sub>])"],
   "<p>Products on top, reactants on the bottom, each concentration raised to its coefficient: [NH<sub>3</sub>]<sup>2</sup> / ([N<sub>2</sub>]<sup>1</sup>[H<sub>2</sub>]<sup>3</sup>). The inverted form is K for the <em>reverse</em> reaction.</p>")

mc("equil-2", "equil", 2, "L24 slide 8 &middot; extra",
   "Which is the correct K for <b>CaCO<sub>3</sub>(s) &rlarr; CaO(s) + CO<sub>2</sub>(g)</b>?",
   ["K = P<sub>CO2</sub> (the pure solids are left out)", "K = [CaO][CO<sub>2</sub>] / [CaCO<sub>3</sub>]", "K = [CaCO<sub>3</sub>] / ([CaO][CO<sub>2</sub>])", "K = P<sub>CO2</sub> / 2"],
   "<p>A pure solid or liquid has a fixed &ldquo;concentration&rdquo;, so it is left out of K. Only the gas remains: K = P<sub>CO<sub>2</sub></sub> (in atm, dimensionless).</p>")

mc("equil-3", "equil", 1, "L24 slide 8",
   "A reaction has K = 5&times;10<sup>&minus;9</sup>. What does the equilibrium mixture look like?",
   ["Mostly reactants; almost no product forms", "Mostly products", "Roughly equal amounts of reactants and products", "The reaction has not started"],
   "<p>K &lt; 10<sup>&minus;3</sup> is the &ldquo;small&rdquo; zone of the L24 slide: the mixture is mostly reactants. (Like I<sub>2</sub> &rlarr; 2I at 800 K, K = 4.6&times;10<sup>&minus;7</sup>.)</p>")

mc("equil-4", "equil", 1, "L24 slide 8",
   "Which statement about K is true?",
   ["K has no units, because concentrations are measured relative to the standard state (1 mol/L or 1 atm)", "K has units of mol/L", "K has units of mol/L raised to (products &minus; reactants)", "K has units of kJ/mol"],
   "<p>L24 slide 8: &ldquo;no units because all the concentrations are referred to the standard state (1 mol/L or 1 atm)&rdquo;. K is a pure number that depends on temperature.</p>")

mc("equil-5", "equil", 2, "L24 slide 8",
   "Order these by how far they go to products (largest K last): <b>I<sub>2</sub> &rlarr; 2I</b> (4.6&times;10<sup>&minus;7</sup>), <b>H<sub>2</sub> + I<sub>2</sub> &rlarr; 2HI</b> (0.29), <b>H<sub>2</sub> + Cl<sub>2</sub> &rlarr; 2HCl</b> (1.6&times;10<sup>33</sup>).",
   ["I<sub>2</sub> &rlarr; 2I &lt; H<sub>2</sub> + I<sub>2</sub> &rlarr; 2HI &lt; H<sub>2</sub> + Cl<sub>2</sub> &rlarr; 2HCl", "H<sub>2</sub> + Cl<sub>2</sub> &rlarr; 2HCl &lt; H<sub>2</sub> + I<sub>2</sub> &rlarr; 2HI &lt; I<sub>2</sub> &rlarr; 2I", "H<sub>2</sub> + I<sub>2</sub> &rlarr; 2HI &lt; I<sub>2</sub> &rlarr; 2I &lt; H<sub>2</sub> + Cl<sub>2</sub> &rlarr; 2HCl", "they are all equal"],
   "<p>A bigger K means more product at equilibrium. Compare the powers of ten: 10<sup>&minus;7</sup> &lt; 10<sup>&minus;1</sup> &lt; 10<sup>33</sup>. Making strong bonds (H&ndash;Cl) pays energy back; breaking I&ndash;I costs it.</p>")

Qa = 0.20 ** 2 / 0.50
num("equil-6", "equil", 1, "L24 slide 9",
    "For <b>N<sub>2</sub>O<sub>4</sub> &rlarr; 2NO<sub>2</sub></b> the concentrations at one moment are [N<sub>2</sub>O<sub>4</sub>] = 0.50 M and [NO<sub>2</sub>] = 0.20 M. Calculate the reaction quotient Q.",
    Qa, "",
    "<p>Q has the same form as K: Q = [NO<sub>2</sub>]&sup2; / [N<sub>2</sub>O<sub>4</sub>] = 0.20&sup2; / 0.50 = <b>%s</b> (no units).</p>" % fmt(Qa, 3),
    hint="Square the NO<sub>2</sub> (its coefficient is 2).", text=fmt(Qa, 3))

mc("equil-7", "equil", 2, "L24 slide 9",
   "For the reaction above K = 0.15 at the temperature used (Q = 0.080 from the previous question). Which way does the reaction proceed?",
   ["To the right (towards NO<sub>2</sub>), because Q &lt; K", "To the left, because Q &lt; K", "It does not move, because Q is small", "To the right, because Q &gt; K"],
   "<p>Q = 0.080 &lt; K = 0.15: there is too little product compared with equilibrium, so the net reaction runs forward (right) until Q rises to K.</p>")

mc("equil-8", "equil", 1, "L24 slide 9",
   "At equilibrium, which statement is correct?",
   ["Q = K, and the forward and reverse reactions continue at equal rates", "Q = 0 and all reactions have stopped", "All the reactant has been used up", "[reactants] = [products]"],
   "<p>Equilibrium is dynamic: both reactions go on, but at the same rate, so the amounts stay constant. It does <em>not</em> mean equal amounts of reactants and products (that depends on K).</p>")

mc("equil-9", "equil", 2, "L24 slide 9",
   "A reaction mixture has Q = 250 and the reaction has K = 40. The net reaction will&hellip;",
   ["run in the reverse direction (to the left) until Q falls to 40", "run forward until Q rises to 40", "stay put", "stop because K &lt; Q means the reaction is spontaneous"],
   "<p>Q &gt; K means too much product, so the reverse reaction wins until Q has dropped to K. On the L24 plot this is the upper curve falling toward the Q = K line.</p>")

K_val = math.exp(20000.0 / (R * T0))
num("equil-10", "equil", 3, "Rec 17 slides 10&ndash;11",
    "A reaction has &Delta;G&deg; = &minus;20.0 kJ/mol at 298 K. Calculate K. (R = 8.314 J/(mol&middot;K).)",
    K_val, "",
    "<p>&Delta;G&deg; = &minus;RT ln K &rArr; ln K = 20 000 / (8.314 &times; 298) = %s, so K = <b>%s</b>. Use J with R, so convert &minus;20.0 kJ to &minus;20 000 J first.</p>" % (fmt(20000.0 / (R * T0), 4), fmt(K_val, 3)),
    hint="ln K = &minus;&Delta;G&deg;/(RT), with &Delta;G&deg; in joules.", tol=0.03, text=fmt(K_val, 3))

dG = -R * 300 * math.log(4.2e13) / 1000.0
num("equil-11", "equil", 3, "Rec 17 slides 10&ndash;11",
    "From the L24 table, 2NO + O<sub>2</sub> &rlarr; 2NO<sub>2</sub> has K = 4.2&times;10<sup>13</sup> at 300 K. Find &Delta;G&deg; in kJ/mol.",
    dG, "kJ/mol",
    "<p>&Delta;G&deg; = &minus;RT ln K = &minus;8.314 &times; 300 &times; ln(4.2&times;10<sup>13</sup>) = &minus;8.314 &times; 300 &times; %s = &minus;%s J, so <b>%s kJ/mol</b>. Very negative &Delta;G&deg; &harr; very large K.</p>" % (fmt(math.log(4.2e13), 4), fmt(-dG * 1000, 4), fmt(dG, 4)),
    tol=0.02, text="%s kJ/mol" % fmt(dG, 4))

dG3 = -R * T0 * math.log(1e3) / 1000.0
num("equil-12", "equil", 3, "Rec 17 slides 10&ndash;11",
    "What &Delta;G&deg; (in kJ/mol, at 298 K) corresponds to K = 10<sup>3</sup>, the boundary of the &ldquo;large K&rdquo; zone on the L24 slide?",
    dG3, "kJ/mol",
    "<p>&Delta;G&deg; = &minus;RT ln(10<sup>3</sup>) = &minus;8.314 &times; 298 &times; 6.908 = &minus;17 114 J = <b>%s kJ/mol</b>. So at room temperature, &ldquo;mostly products&rdquo; means &Delta;G&deg; more negative than about &minus;17 kJ/mol.</p>" % fmt(dG3, 3),
    text="%s kJ/mol" % fmt(dG3, 3))

dGq = -10.0 + R * T0 * math.log(0.01) / 1000.0
num("equil-13", "equil", 3, "Rec 17 slide 10",
    "A reaction has &Delta;G&deg; = &minus;10.0 kJ/mol. At 298 K the mixture has Q = 0.010. What is &Delta;G (kJ/mol) for the reaction under these conditions?",
    dGq, "kJ/mol",
    "<p>&Delta;G = &Delta;G&deg; + RT ln Q = &minus;10.0 + (8.314 &times; 298 / 1000) &times; ln(0.010) = &minus;10.0 + 2.478 &times; (&minus;4.605) = <b>%s kJ/mol</b>. Q is far below K, so the push to the right is even stronger than under standard conditions.</p>" % fmt(dGq, 3),
    hint="ln(0.010) = &minus;4.605.", text="%s kJ/mol" % fmt(dGq, 3))

num("equil-14", "equil", 2, "Rec 17 slide 8 (RICE)",
    "H<sub>2</sub> + I<sub>2</sub> &rlarr; 2HI has K = 64 (made-up value). Starting with 1.0 M H<sub>2</sub>, 1.0 M I<sub>2</sub> and no HI, find [HI] at equilibrium in M.",
    1.6, "M",
    "<p>RICE: change = &minus;x, &minus;x, +2x. K = (2x)&sup2;/(1.0 &minus; x)&sup2; = 64. Square root: 2x/(1.0 &minus; x) = 8, so 2x = 8 &minus; 8x, x = 0.80. [HI] = 2x = <b>1.6 M</b>; [H<sub>2</sub>] = [I<sub>2</sub>] = 0.20 M. Check: 1.6&sup2;/0.20&sup2; = 64.</p>",
    hint="K is a perfect square (64 = 8&sup2;): take the square root of both sides.", text="1.6 M")

num("equil-15", "equil", 2, "Rec 17 slide 8 (RICE)",
    "A &rlarr; B has K = 4.0. Start with [A] = 1.0 M and no B. What is [B] at equilibrium (M)?",
    0.8, "M",
    "<p>Change: A &minus;x, B +x. K = x/(1.0 &minus; x) = 4.0 &rArr; x = 4.0 &minus; 4.0x &rArr; 5.0x = 4.0 &rArr; x = <b>0.80 M</b>, so [A] = 0.20 M. Check: 0.80/0.20 = 4.0.</p>",
    text="0.80 M")

Kc = 0.60 / (0.20 * 0.30)
num("equil-16", "equil", 2, "Rec 17 slide 8 (RICE)",
    "For A + B &rlarr; C the equilibrium concentrations are [A] = 0.20 M, [B] = 0.30 M and [C] = 0.60 M. Find K.",
    Kc, "",
    "<p>K = [C]/([A][B]) = 0.60 / (0.20 &times; 0.30) = 0.60 / 0.060 = <b>%s</b>. Each exponent is 1 because every coefficient is 1.</p>" % fmt(Kc, 3),
    text=fmt(Kc, 3))

num("equil-17", "equil", 2, "extra",
    "The reaction A &rlarr; B has K = 2.5&times;10<sup>&minus;2</sup>. What is K for the <b>reverse</b> reaction B &rlarr; A?",
    1 / 2.5e-2, "",
    "<p>Reversing a reaction inverts K: K<sub>reverse</sub> = 1/K = 1/0.025 = <b>40</b>.</p>",
    text="40")

num("equil-18", "equil", 2, "extra",
    "For A &rlarr; B, K = 3.0. What is K for the doubled equation <b>2A &rlarr; 2B</b>?",
    9.0, "",
    "<p>Multiplying all coefficients by n raises K to the n<sup>th</sup> power: K = 3.0<sup>2</sup> = <b>9.0</b>. (Check with the expression: [B]&sup2;/[A]&sup2; = (K)&sup2;.)</p>",
    text="9.0")

mc("equil-19", "equil", 2, "Rec 17 slides 9, 12",
    "For the exothermic reaction N<sub>2</sub> + 3H<sub>2</sub> &rlarr; 2NH<sub>3</sub> (&Delta;H = &minus;92 kJ), what does <b>raising the temperature</b> do?",
   ["K decreases, so less NH<sub>3</sub> at equilibrium", "K increases, so more NH<sub>3</sub>", "K is unchanged because only pressure matters", "K is unchanged but equilibrium is reached more slowly"],
   "<p>Heating favours the endothermic direction, here the reverse (NH<sub>3</sub> &rarr; N<sub>2</sub> + H<sub>2</sub>). So K gets smaller. A catalyst plus a moderate temperature gives a workable rate without losing too much equilibrium yield.</p>")

mc("equil-20", "equil", 2, "Rec 17 slide 9",
    "For N<sub>2</sub> + 3H<sub>2</sub> &rlarr; 2NH<sub>3</sub>, what does <b>raising the pressure</b> (squeezing the container) do?",
    ["Shifts the equilibrium to the right (4 mol gas &rarr; 2 mol gas); K is unchanged", "Shifts it to the left; K is unchanged", "Shifts it to the right and increases K", "Nothing, because the reaction is exothermic"],
    "<p>Le Ch&acirc;telier: the system relieves the pressure by moving toward the side with fewer gas molecules. The reactant side has 4 mol of gas and the product side 2 mol, so it moves right. Only temperature changes K.</p>")

mc("equil-21", "equil", 2, "Rec 17 slide 9",
    "Extra N<sub>2</sub> is added to an equilibrium mixture of N<sub>2</sub>, H<sub>2</sub> and NH<sub>3</sub> at constant temperature. What happens?",
    ["Q drops below K, so the reaction shifts right and makes more NH<sub>3</sub>; K is unchanged", "K increases", "Q rises above K and the reaction shifts left", "Nothing: equilibrium cannot be disturbed"],
    "<p>More N<sub>2</sub> makes the denominator of Q larger, so Q &lt; K. The reaction runs to the right until Q = K again. K itself never changes at fixed temperature.</p>")

mc("equil-22", "equil", 1, "Rec 17 slide 13",
    "What does adding a catalyst do to an equilibrium?",
    ["It reaches equilibrium faster, but K and the equilibrium amounts do not change", "It increases K", "It decreases K", "It moves the equilibrium toward products"],
    "<p>A catalyst lowers E<sub>a</sub> for forward <em>and</em> reverse reactions equally. The rate of approach increases; the destination (K, set by &Delta;G&deg;) does not.</p>")

mc("equil-23", "equil", 2, "L24 slide 8 &middot; L23",
    "N<sub>2</sub> + 3H<sub>2</sub> &rlarr; 2NH<sub>3</sub> has K = 2.7&times;10<sup>8</sup> at 300 K, yet it is not useful at room temperature without a catalyst. Why?",
    ["K says where the reaction ends up, not how fast it gets there; the activation energy makes the rate negligible", "K is too small", "&Delta;G&deg; is positive", "Large K means the reaction needs high pressure"],
    "<p>Thermodynamics (K, &Delta;G) and kinetics (E<sub>a</sub>, k) are separate questions. Haber&rsquo;s process combines a catalyst and elevated temperature so that equilibrium is approached in reasonable time.</p>")

mc("equil-24", "equil", 2, "Rec 17 slide 10",
    "&Delta;G&deg; for a reaction is +5 kJ/mol at 298 K. What does that say about K?",
    ["K &lt; 1, but some product still forms at equilibrium", "K &gt; 1", "K = 1", "No product can ever form"],
    "<p>&Delta;G&deg; = &minus;RT ln K &gt; 0 means ln K &lt; 0, so K &lt; 1. Here K = e<sup>&minus;5000/(8.314&times;298)</sup> &asymp; 0.13: not zero, so some product exists at equilibrium.</p>")

selfq("equil-25", "equil", 2, "L24 slide 9",
      "In two or three sentences explain how you would use Q and K to tell which way a reaction mixture will move, and what is &ldquo;dynamic&rdquo; about equilibrium.",
      "<p><b>Model answer.</b> Write Q with the K expression (products over reactants, coefficients as exponents) using the concentrations now. If Q &lt; K there is too little product, so the reaction proceeds to the right; if Q &gt; K it proceeds to the left; at Q = K there is no net change. Equilibrium is dynamic because forward and reverse reactions both keep going at the <em>same</em> rate, so the amounts stay constant without anything having stopped.</p>")

# ================================================================== THERMODYNAMICS FOUNDATIONS (Rec 16)
topic("laws", "Thermodynamics foundations: heat, work, H &amp; S", "unit13", "Rec 16",
      "Recitation 16 recap. Recipe: <b>&Delta;E = Q + W</b> with <b>W = &minus;P&Delta;V</b> (work done <em>on</em> the system is +); "
      "<b>&Delta;H = Q</b> at constant pressure; <b>&Delta;H&deg;<sub>rxn</sub> = &Sigma;&Delta;H&deg;<sub>f</sub>(products) &minus; &Sigma;&Delta;H&deg;<sub>f</sub>(reactants)</b> (elements = 0); "
      "state functions (U, H, S, G, P, V, T) vs path functions (Q, W); entropy: crystal &lt; amorphous &lt; liquid &lt; gas, &Delta;S<sub>universe</sub> &ge; 0.")

mc("laws-1", "laws", 1, "Rec 16 slide 5",
   "A sealed, <b>un</b>insulated flask of reacting gases sits on a bench. It can exchange heat with the room but no matter. What kind of system is it?",
   ["Closed", "Open", "Isolated", "Adiabatic and open"],
   "<p>Closed = energy exchange allowed, no matter exchange. Open = both. Isolated = neither (a perfect sealed thermos).</p>")

W_pv = -2.0 * (-1.5) * 101.325
num("laws-2", "laws", 2, "Rec 16 slide 7",
    "A gas is compressed against a constant external pressure of 2.0 atm, and its volume falls by 1.5 L. Calculate the work done on the gas in joules (1 L&middot;atm = 101.3 J).",
    W_pv, "J",
    "<p>W = &minus;P<sub>ext</sub>&Delta;V = &minus;(2.0 atm)(&minus;1.5 L) = +3.0 L&middot;atm = 3.0 &times; 101.3 = <b>%s J</b>. Positive because work is done <em>on</em> the system.</p>" % fmt(W_pv, 3),
    hint="&Delta;V is negative for a compression.", text="%s J" % fmt(W_pv, 3))

mc("laws-3", "laws", 2, "Rec 16 slide 7",
   "A gas expands against a constant external pressure. What are the signs of &Delta;V and of W (work done on the system)?",
   ["&Delta;V &gt; 0 and W &lt; 0", "&Delta;V &gt; 0 and W &gt; 0", "&Delta;V &lt; 0 and W &lt; 0", "&Delta;V &lt; 0 and W &gt; 0"],
   "<p>Expansion means &Delta;V &gt; 0, so W = &minus;P&Delta;V &lt; 0: the system does work on its surroundings, and its energy drops by that amount.</p>")

dE = 250 - 80
num("laws-4", "laws", 1, "Rec 16 slide 12",
    "A system absorbs 250 J of heat and does 80 J of work on its surroundings. What is &Delta;E for the system in joules?",
    dE, "J",
    "<p>&Delta;E = Q + W. Heat absorbed: Q = +250 J. Work done <em>by</em> the system: W = &minus;80 J. &Delta;E = 250 &minus; 80 = <b>+170 J</b>.</p>",
    text="170 J")

mc("laws-5", "laws", 1, "Rec 16 slide 10",
   "Which of these is a <b>path function</b> (depends on how the change happened)?",
   ["Heat (Q)", "Enthalpy (H)", "Entropy (S)", "Internal energy (U)"],
   "<p>State functions (path-independent): U, H, S, G, P, V, T, mass, composition. Path functions: <b>work and heat</b>. Analogy: height gained climbing a hill is a state function, the distance walked is a path function.</p>")

mc("laws-6", "laws", 2, "Rec 16 slides 12&ndash;13",
   "For a process at constant pressure where only PV work is done, &Delta;H equals&hellip;",
   ["the heat transferred, Q", "the work done, W", "&Delta;E exactly", "zero"],
   "<p>H = U + PV, so &Delta;H = &Delta;U + P&Delta;V (P constant) = Q. Most reactions run in open flasks at 1 atm, so &Delta;H is the heat you measure.</p>")

mc("laws-7", "laws", 1, "Rec 16 slide 14",
   "Which substance has a standard enthalpy of formation of exactly zero?",
   ["O<sub>2</sub>(g)", "O<sub>3</sub>(g)", "H(g)", "H<sub>2</sub>O(l)"],
   "<p>A pure element in its standard state has &Delta;H&deg;<sub>f</sub> = 0 (H<sub>2</sub>(g), O<sub>2</sub>(g), Hg(l), C(graphite), Na(s)). O<sub>3</sub> and atomic H are not the standard state of those elements, and water is a compound.</p>")

dH_ch4 = (-393.5 + 2 * (-285.8)) - (-74.8)
num("laws-8", "laws", 2, "Rec 16 slide 15",
    "Using &Delta;H&deg;<sub>f</sub> (kJ/mol): CH<sub>4</sub>(g) &minus;74.8, CO<sub>2</sub>(g) &minus;393.5, H<sub>2</sub>O(l) &minus;285.8, O<sub>2</sub>(g) 0, find &Delta;H&deg; for CH<sub>4</sub> + 2O<sub>2</sub> &rarr; CO<sub>2</sub> + 2H<sub>2</sub>O(l), in kJ.",
    dH_ch4, "kJ",
    "<p>&Delta;H&deg; = &Sigma;(products) &minus; &Sigma;(reactants) = [&minus;393.5 + 2(&minus;285.8)] &minus; [&minus;74.8 + 0] = &minus;965.1 + 74.8 = <b>%s kJ</b>. Multiply by the coefficient (2 H<sub>2</sub>O), and products minus reactants.</p>" % fmt(dH_ch4, 4),
    hint="Don&rsquo;t forget the factor 2 for water.", text="%s kJ" % fmt(dH_ch4, 4))

dH2 = 2 * (-285.8)
num("laws-9", "laws", 2, "Rec 16 slide 15",
    "&Delta;H&deg;<sub>f</sub> of H<sub>2</sub>O(l) is &minus;285.8 kJ/mol. Find &Delta;H&deg; (kJ) for <b>2H<sub>2</sub>(g) + O<sub>2</sub>(g) &rarr; 2H<sub>2</sub>O(l)</b>.",
    dH2, "kJ",
    "<p>The elements contribute 0, so &Delta;H&deg; = 2 &times; (&minus;285.8) = <b>%s kJ</b>. Twice the equation, twice the &Delta;H (it is per equation as written).</p>" % fmt(dH2, 4),
    text="%s kJ" % fmt(dH2, 4))

mc("laws-10", "laws", 1, "Rec 16 slide 16",
   "Which ordering of entropy is correct?",
   ["crystal &lt; amorphous solid &lt; liquid &lt; gas", "gas &lt; liquid &lt; amorphous solid &lt; crystal", "liquid &lt; crystal &lt; gas &lt; amorphous solid", "crystal &lt; liquid &lt; amorphous solid &lt; gas"],
   "<p>More disorder = more entropy: an ordered crystal is lowest, an amorphous solid has frozen-in disorder, a liquid more, a gas the most. Mixing two different kinds of atoms also raises entropy.</p>")

mc("laws-11", "laws", 2, "Rec 16 slide 17",
   "Water freezes into ice, which has <b>lower</b> entropy than the liquid. Why doesn&rsquo;t this break the second law?",
   ["The heat released raises the entropy of the surroundings by more than the water loses, so &Delta;S<sub>universe</sub> &ge; 0", "The second law only applies to gases", "Freezing is reversible, so entropy does not change", "Entropy is not a state function for water"],
   "<p>The 2nd law is about the <b>universe</b>. A local decrease is allowed if the surroundings make up for it. Here heat Q flows out to the colder surroundings and their entropy rises more than the water&rsquo;s fell.</p>")

mc("laws-12", "laws", 1, "Rec 16 slide 18",
   "For a <b>reversible</b> process, &Delta;S<sub>universe</sub> is&hellip;",
   ["0 (the system stays at equilibrium throughout, infinitely slowly)", "negative", "positive", "infinite"],
   "<p>Reversible: &Delta;S<sub>universe</sub> = 0. Irreversible (all real, natural-direction processes, such as heat flowing from hot to cold): &Delta;S<sub>universe</sub> &gt; 0. It is never &lt; 0.</p>")

mc("laws-13", "laws", 1, "Rec 16 slide 19",
   "The third law of thermodynamics says that&hellip;",
   ["a perfect crystal at 0 K has S = 0, but 0 K can never actually be reached", "entropy of a gas is always zero at 298 K", "the energy of the universe is constant", "entropy of the universe can only decrease"],
   "<p>Third law: S = 0 for a perfect crystal at T = 0 K; in practice unreachable (infinitely many steps). First law: energy of the universe constant. Second: entropy of the universe never decreases.</p>")

mc("laws-14", "laws", 1, "Rec 16 slide 20",
   "Match each law: (1st, 2nd, 3rd).",
   ["1st: energy of the universe is constant; 2nd: entropy of the universe never decreases; 3rd: there is no such thing as zero entropy", "1st: entropy of the universe never decreases; 2nd: energy is constant; 3rd: heat flows from cold to hot", "1st: no zero entropy; 2nd: energy is constant; 3rd: entropy never decreases", "1st: &Delta;G &lt; 0; 2nd: &Delta;H &lt; 0; 3rd: &Delta;S &lt; 0"],
   "<p>The Rec 16 summary slide gives exactly these three one-liners.</p>")

mc("laws-15", "laws", 2, "Rec 16 slide 21",
   "When NaCl dissolves in water the entropy of the system generally&hellip;",
   ["increases: the ordered crystal becomes free-moving hydrated ions", "decreases: ions are surrounded by water", "stays exactly the same", "becomes zero"],
   "<p>The rigid crystal lattice (low entropy) breaks apart into Na<sup>+</sup> and Cl<sup>&minus;</sup> ions free to move in solution. Mixing increases entropy. The ordering of water around the ions works against this, but the net effect for NaCl is an increase.</p>")

dS_surr = 890.3e3 / 298.0
num("laws-16", "laws", 3, "Rec 16 &middot; extra",
    "Burning methane has &Delta;H&deg; = &minus;890.3 kJ. At constant T and P the surroundings absorb that heat. Find &Delta;S<sub>surroundings</sub> in J/K at 298 K (use &Delta;S<sub>surr</sub> = &minus;&Delta;H/T).",
    dS_surr, "J/K",
    "<p>&Delta;S<sub>surr</sub> = &minus;&Delta;H/T = +890 300 J / 298 K = <b>%s J/K</b>. A large increase in the entropy of the surroundings is part of why combustion is so strongly spontaneous (&Delta;S<sub>universe</sub> = &Delta;S<sub>sys</sub> + &Delta;S<sub>surr</sub>).</p>" % fmt(dS_surr, 4),
    hint="Convert kJ to J first.", text="%s J/K" % fmt(dS_surr, 4))

mc("laws-17", "laws", 2, "Rec 16 slide 15",
   "Which statement about &Delta;H&deg;<sub>f</sub> is correct?",
   ["It is the heat for forming 1 mol of a compound from its elements in their standard states", "It is the heat of any reaction at 25 &deg;C", "It is always negative", "It is the heat of burning 1 mol of the compound"],
   "<p>Formation reactions start from <b>elements</b> and make <b>1 mol</b> of one substance. Some &Delta;H&deg;<sub>f</sub> values are positive (endothermic formation), and burning is a different reaction.</p>")

mc("laws-18", "laws", 2, "Rec 16 slide 3",
   "&ldquo;Thermodynamics is time-independent&rdquo; means&hellip;",
   ["it tells you where a system ends up at equilibrium, not how fast it gets there", "it only applies to fast reactions", "it predicts reaction rates from &Delta;G", "it is limited to gases"],
   "<p>Thermodynamics gives the end state (&ldquo;this is how it should end up&rdquo;), with no rates; kinetics gives the speed. A glass below its melting point should become a crystal, but may take forever.</p>")

selfq("laws-19", "laws", 2, "Rec 16 slide 10",
      "Explain the difference between a state function and a path function, and give two examples of each.",
      "<p><b>Model answer.</b> A state function depends only on the present state of the system, not on how it got there (path-independent): e.g. internal energy U, enthalpy H, entropy S, free energy G, T, P, V. A path function depends on the route taken: work and heat. Hill analogy: the height gained is a state function (it is the same for every path to the top); the distance walked is a path function. For work, the route sets the volume change; for heat, the initial temperature difference.</p>")
