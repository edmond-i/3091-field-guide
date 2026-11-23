from practice_lib import *
import math

topic("ksp", "Solubility product &amp; complexation", "unit18", "Quiz 9",
      "Recipe: <b>K<sub>sp</sub></b> = product of the dissolved ion concentrations, each to its coefficient, <b>solid left out</b>. Molar solubility x: AB &rarr; x&sup2;, AB<sub>2</sub> &rarr; 4x&sup3;, A<sub>3</sub>B<sub>2</sub> &rarr; 108x<sup>5</sup> (ions = coefficient &times; x). "
      "<b>Q &lt; K<sub>sp</sub></b> unsaturated, <b>Q = K<sub>sp</sub></b> saturated, <b>Q &gt; K<sub>sp</sub></b> precipitates. Common ion: <b>less</b> soluble; acid on a basic anion or a complexing ligand: <b>more</b> soluble. K<sub>f</sub> = K<sub>1</sub>K<sub>2</sub>&hellip;")

mc("ksp-1", "ksp", 1, "Rec 20",
   "Write the solubility product for BaSO<sub>4</sub>(s) &rlarr; Ba<sup>2+</sup>(aq) + SO<sub>4</sub><sup>2&minus;</sup>(aq).",
   ["K<sub>sp</sub> = [Ba<sup>2+</sup>][SO<sub>4</sub><sup>2&minus;</sup>] (the solid is left out)", "K<sub>sp</sub> = [Ba<sup>2+</sup>][SO<sub>4</sub><sup>2&minus;</sup>] / [BaSO<sub>4</sub>]", "K<sub>sp</sub> = [BaSO<sub>4</sub>] / ([Ba<sup>2+</sup>][SO<sub>4</sub><sup>2&minus;</sup>])", "K<sub>sp</sub> = [Ba<sup>2+</sup>] + [SO<sub>4</sub><sup>2&minus;</sup>]"],
   "<p>Like any equilibrium constant (Unit 14) with the pure solid omitted: products over reactants, ions to the power of their coefficients.</p>")

mc("ksp-2", "ksp", 2, "Rec 20 problem 3b",
   "What is K<sub>sp</sub> for Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub>(s) &rlarr; 3Ca<sup>2+</sup> + 2PO<sub>4</sub><sup>3&minus;</sup>?",
   ["[Ca<sup>2+</sup>]&sup3;[PO<sub>4</sub><sup>3&minus;</sup>]&sup2;", "[Ca<sup>2+</sup>]&sup2;[PO<sub>4</sub><sup>3&minus;</sup>]&sup3;", "3[Ca<sup>2+</sup>] &times; 2[PO<sub>4</sub><sup>3&minus;</sup>]", "[Ca<sup>2+</sup>][PO<sub>4</sub><sup>3&minus;</sup>]"],
   "<p>Each ion concentration is raised to its coefficient in the dissolution equation: 3 for calcium, 2 for phosphate.</p>")

s1 = math.sqrt(1.5e-9)
num("ksp-3", "ksp", 1, "Rec 20 problem 1",
    "K<sub>sp</sub> of BaSO<sub>4</sub> at 25 &deg;C is 1.5&times;10<sup>&minus;9</sup>. What is its molar solubility in pure water (mol/L)?",
    s1, "M",
    "<p>x&sup2; = 1.5&times;10<sup>&minus;9</sup> &rArr; x = <b>%s M</b> (= [Ba<sup>2+</sup>] = [SO<sub>4</sub><sup>2&minus;</sup>]).</p>" % fmt(s1, 3), text="%s M" % fmt(s1, 3))

x2 = (7.9e-9 / 4) ** (1 / 3)
num("ksp-4", "ksp", 2, "Rec 20 problem 2a",
    "PbI<sub>2</sub> has K<sub>sp</sub> = 7.9&times;10<sup>&minus;9</sup>. In pure water, what is [I<sup>&minus;</sup>] in the saturated solution (M)?",
    2 * x2, "M",
    "<p>PbI<sub>2</sub> &rlarr; Pb<sup>2+</sup> + 2I<sup>&minus;</sup>: [Pb<sup>2+</sup>] = x, [I<sup>&minus;</sup>] = 2x. K<sub>sp</sub> = x(2x)&sup2; = 4x&sup3; = 7.9&times;10<sup>&minus;9</sup> &rArr; x = %s M, so [I<sup>&minus;</sup>] = 2x = <b>%s M</b>.</p>" % (fmt(x2, 3), fmt(2 * x2, 3)),
    hint="Don&rsquo;t forget the factor 2 for iodide.", text="%s M" % fmt(2 * x2, 3))

num("ksp-5", "ksp", 3, "Rec 20 problem 2b",
    "PbI<sub>2</sub> (K<sub>sp</sub> = 7.9&times;10<sup>&minus;9</sup>) is stirred into 0.1 M NaI. What is [Pb<sup>2+</sup>] at equilibrium (M)? (NaI is fully dissociated; assume the extra I<sup>&minus;</sup> from PbI<sub>2</sub> is negligible.)",
    7.9e-9 / 0.01, "M",
    "<p>[I<sup>&minus;</sup>] &asymp; 0.1 M (common ion). K<sub>sp</sub> = [Pb<sup>2+</sup>](0.1)&sup2; &rArr; [Pb<sup>2+</sup>] = 7.9&times;10<sup>&minus;9</sup>/0.01 = <b>7.9&times;10<sup>&minus;7</sup> M</b>, about 1600 times smaller than in pure water (1.25&times;10<sup>&minus;3</sup> M).</p>",
    text="7.9&times;10<sup>&minus;7</sup> M")

mc("ksp-6", "ksp", 1, "Rec 20",
   "What does adding a common ion (an ion already in the dissolved solid) do to the molar solubility?",
   ["Decreases it (Le Ch&acirc;telier: the equilibrium shifts toward the solid, which may precipitate)", "Increases it", "Does nothing", "Changes K<sub>sp</sub>"],
   "<p>Extra product ions shift the dissolution equilibrium to the left. K<sub>sp</sub> itself (set by temperature) is unchanged; the solubility falls.</p>")

xs = (3.091e-12 / 108) ** 0.2
num("ksp-7", "ksp", 3, "Rec 20 problem 3c",
    "Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> has K<sub>sp</sub> = 3.091&times;10<sup>&minus;12</sup>. What is [Ca<sup>2+</sup>] in a saturated solution in pure water (M)?",
    3 * xs, "M",
    "<p>[Ca<sup>2+</sup>] = 3x and [PO<sub>4</sub><sup>3&minus;</sup>] = 2x, so K<sub>sp</sub> = (3x)&sup3;(2x)&sup2; = 108x<sup>5</sup> &rArr; x = (3.091&times;10<sup>&minus;12</sup>/108)<sup>1/5</sup> = %s M. [Ca<sup>2+</sup>] = 3x = <b>%s M</b>.</p>" % (fmt(xs, 4), fmt(3 * xs, 3)),
    text="%s M" % fmt(3 * xs, 3))

num("ksp-8", "ksp", 3, "Rec 20 problem 3c",
    "For the same saturated Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> solution (K<sub>sp</sub> = 3.091&times;10<sup>&minus;12</sup>), what is [PO<sub>4</sub><sup>3&minus;</sup>] (M)?",
    2 * xs, "M",
    "<p>[PO<sub>4</sub><sup>3&minus;</sup>] = 2x = 2 &times; %s = <b>%s M</b>.</p>" % (fmt(xs, 4), fmt(2 * xs, 3)), text="%s M" % fmt(2 * xs, 3))

xp = math.sqrt(3.091e-12 / (0.749 ** 3 * 4))
num("ksp-9", "ksp", 3, "Rec 20 problem 3d",
    "75 g of CaCO<sub>3</sub> (M = 100.09 g/mol) dissolves in 1 L of water that is then equilibrated with solid Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> (K<sub>sp</sub> = 3.091&times;10<sup>&minus;12</sup>). Taking [Ca<sup>2+</sup>] &asymp; 0.749 M, find [PO<sub>4</sub><sup>3&minus;</sup>] (M).",
    2 * xp, "M",
    "<p>K<sub>sp</sub> &asymp; (0.749)&sup3;[PO<sub>4</sub><sup>3&minus;</sup>]&sup2; &rArr; [PO<sub>4</sub><sup>3&minus;</sup>]&sup2; = 3.091&times;10<sup>&minus;12</sup>/0.4202 = 7.36&times;10<sup>&minus;12</sup> &rArr; [PO<sub>4</sub><sup>3&minus;</sup>] = <b>%s M</b> (Rec 20: 2.71&times;10<sup>&minus;6</sup> M). The added common ion cut the phosphate by a factor of about 1400.</p>" % fmt(2 * xp, 3),
    hint="[Ca<sup>2+</sup>] is dominated by the CaCO<sub>3</sub>: the 3x from the phosphate is negligible.", text="%s M" % fmt(2 * xp, 3))

num("ksp-10", "ksp", 2, "Rec 20",
    "50.0 mL of 2.0&times;10<sup>&minus;3</sup> M Pb(NO<sub>3</sub>)<sub>2</sub> is mixed with 50.0 mL of 4.0&times;10<sup>&minus;3</sup> M NaI. Calculate the ion product Q = [Pb<sup>2+</sup>][I<sup>&minus;</sup>]&sup2; after mixing.",
    1.0e-3 * (2.0e-3) ** 2, "",
    "<p>The volume doubles, so each concentration halves: [Pb<sup>2+</sup>] = 1.0&times;10<sup>&minus;3</sup>, [I<sup>&minus;</sup>] = 2.0&times;10<sup>&minus;3</sup>. Q = (1.0&times;10<sup>&minus;3</sup>)(2.0&times;10<sup>&minus;3</sup>)&sup2; = <b>4.0&times;10<sup>&minus;9</sup></b>.</p>",
    hint="Use the total volume.", text="4.0&times;10<sup>&minus;9</sup>")

mc("ksp-11", "ksp", 2, "Rec 20",
   "In the previous mixture Q = 4.0&times;10<sup>&minus;9</sup> and K<sub>sp</sub>(PbI<sub>2</sub>) = 7.9&times;10<sup>&minus;9</sup>. What happens?",
   ["No precipitate forms: Q &lt; K<sub>sp</sub> (unsaturated)", "PbI<sub>2</sub> precipitates because Q is large", "The solution is supersaturated", "The solution is exactly saturated"],
   "<p>Q &lt; K<sub>sp</sub> means more solid <em>could</em> dissolve, so nothing precipitates. Precipitation needs Q &gt; K<sub>sp</sub>.</p>")

mc("ksp-12", "ksp", 1, "Rec 20",
   "A solution has an ion product Q greater than K<sub>sp</sub>. It is&hellip;",
   ["supersaturated: solid will precipitate until Q falls to K<sub>sp</sub>", "unsaturated: more solid will dissolve", "at equilibrium", "impossible"],
   "<p>Q &gt; K<sub>sp</sub>: too many dissolved ions, so solid forms. Q = K<sub>sp</sub>: saturated. Q &lt; K<sub>sp</sub>: unsaturated.</p>")

mc("ksp-13", "ksp", 3, "Rec 20 &middot; trap",
   "AgCl has K<sub>sp</sub> = 1.8&times;10<sup>&minus;10</sup> and Ag<sub>2</sub>CrO<sub>4</sub> has K<sub>sp</sub> = 1.1&times;10<sup>&minus;12</sup>. Which has the larger molar solubility?",
   ["Ag<sub>2</sub>CrO<sub>4</sub> (6.5&times;10<sup>&minus;5</sup> M versus 1.3&times;10<sup>&minus;5</sup> M), despite its smaller K<sub>sp</sub>", "AgCl, because its K<sub>sp</sub> is larger", "They are equal", "Cannot be compared"],
   "<p>Different formula types: AgCl x = &radic;K<sub>sp</sub> = 1.3&times;10<sup>&minus;5</sup>; Ag<sub>2</sub>CrO<sub>4</sub> x = (K<sub>sp</sub>/4)<sup>1/3</sup> = 6.5&times;10<sup>&minus;5</sup>. Only compare K<sub>sp</sub> directly for the same formula type.</p>")

Ag2 = (1.1e-12 / 4) ** (1 / 3)
num("ksp-14", "ksp", 3, "Rec 20 &middot; trap",
    "Ag<sub>2</sub>CrO<sub>4</sub> has K<sub>sp</sub> = 1.1&times;10<sup>&minus;12</sup> (value mine). Find its molar solubility (M).",
    Ag2, "M",
    "<p>Ag<sub>2</sub>CrO<sub>4</sub> &rlarr; 2Ag<sup>+</sup> + CrO<sub>4</sub><sup>2&minus;</sup>: (2x)&sup2;(x) = 4x&sup3; = 1.1&times;10<sup>&minus;12</sup> &rArr; x = <b>%s M</b>.</p>" % fmt(Ag2, 3), text="%s M" % fmt(Ag2, 3))

mc("ksp-15", "ksp", 2, "Rec 20",
   "Strong base is added to a saturated solution containing solid Mg(OH)<sub>2</sub>. What happens to the amount of solid?",
   ["More Mg(OH)<sub>2</sub> precipitates: added OH<sup>&minus;</sup> is a common ion, so solubility decreases", "The solid dissolves completely", "Nothing changes", "K<sub>sp</sub> increases"],
   "<p>Mg(OH)<sub>2</sub>(s) &rlarr; Mg<sup>2+</sup> + 2OH<sup>&minus;</sup>. More OH<sup>&minus;</sup> pushes the equilibrium left (Le Ch&acirc;telier).</p>")

mc("ksp-16", "ksp", 2, "Rec 20",
   "Strong acid is added to the same Mg(OH)<sub>2</sub> solution. What happens?",
   ["Solubility increases: H<sup>+</sup> consumes OH<sup>&minus;</sup>, so more solid dissolves to replace it", "Solubility decreases", "Nothing, because acids do not react with hydroxides", "Mg(OH)<sub>2</sub> precipitates more"],
   "<p>H<sup>+</sup> + OH<sup>&minus;</sup> &rarr; H<sub>2</sub>O removes a product ion (a &ldquo;sink&rdquo;), so the equilibrium shifts right and more Mg(OH)<sub>2</sub> dissolves.</p>")

xm = (5.6e-12 / 4) ** (1 / 3)
pHm = 14 + math.log10(2 * xm)
num("ksp-17", "ksp", 3, "Rec 20 &middot; Unit 17",
    "Mg(OH)<sub>2</sub> has K<sub>sp</sub> = 5.6&times;10<sup>&minus;12</sup> (value mine). What is the pH of a saturated solution in pure water at 25 &deg;C?",
    pHm, "",
    "<p>x = (K<sub>sp</sub>/4)<sup>1/3</sup> = %s M. [OH<sup>&minus;</sup>] = 2x = %s M, pOH = %s, pH = 14 &minus; pOH = <b>%s</b>.</p>" % (fmt(xm, 3), fmt(2 * xm, 3), fmt(-math.log10(2 * xm), 3), fmt(pHm, 4)),
    tol=0.01, text=fmt(pHm, 4))

mc("ksp-18", "ksp", 2, "L28 slide 4",
   "How does limestone dissolve in CO<sub>2</sub>-rich rainwater, and how do stalactites form?",
   ["CaCO<sub>3</sub> + CO<sub>2</sub> + H<sub>2</sub>O &rarr; Ca<sup>2+</sup> + 2HCO<sub>3</sub><sup>&minus;</sup>; in the cave CO<sub>2</sub> escapes so the reverse reaction deposits CaCO<sub>3</sub>", "CaCO<sub>3</sub> dissolves because water is basic; stalactites are frozen water", "CaCO<sub>3</sub> + O<sub>2</sub> &rarr; CaO + CO<sub>2</sub>", "Stalactites are made of CaCl<sub>2</sub>"],
   "<p>Dissolving: CaCO<sub>3</sub>(s) + CO<sub>2</sub>(aq) + H<sub>2</sub>O(l) &rarr; Ca<sup>2+</sup>(aq) + 2HCO<sub>3</sub><sup>&minus;</sup>(aq). Precipitating: Ca<sup>2+</sup> + 2HCO<sub>3</sub><sup>&minus;</sup> &rarr; CaCO<sub>3</sub>(s) + CO<sub>2</sub>(g) + H<sub>2</sub>O. Removing CO<sub>2</sub>(g) pulls the reaction to the right (Le Ch&acirc;telier).</p>")

mc("ksp-19", "ksp", 2, "L28 slide 5",
   "In black-and-white photography, unreacted AgBr is washed off the film with thiosulfate. Why does it work?",
   ["Thiosulfate forms a complex with Ag<sup>+</sup>, a second &ldquo;reservoir&rdquo; that shifts the AgBr solubility equilibrium toward dissolving", "Thiosulfate raises K<sub>sp</sub> of AgBr", "Thiosulfate is a common ion", "It oxidizes the film"],
   "<p>Complexing the metal ion lowers its free concentration, so Q &lt; K<sub>sp</sub> and more solid dissolves. A complexing ligand has the opposite effect of a common ion.</p>")

Kfv = 1e4 * 1e3 * 1e2 * 10
num("ksp-20", "ksp", 2, "Rec 20",
    "A metal ion binds four ligands in four steps with K<sub>1</sub> = 1&times;10<sup>4</sup>, K<sub>2</sub> = 1&times;10<sup>3</sup>, K<sub>3</sub> = 1&times;10<sup>2</sup> and K<sub>4</sub> = 10. What is the overall formation constant K<sub>f</sub>?",
    Kfv, "",
    "<p>K<sub>f</sub> = K<sub>1</sub>K<sub>2</sub>K<sub>3</sub>K<sub>4</sub> = 10<sup>4</sup> &times; 10<sup>3</sup> &times; 10<sup>2</sup> &times; 10 = <b>1&times;10<sup>10</sup></b> (exponents add).</p>",
    text="1&times;10<sup>10</sup>")

mc("ksp-21", "ksp", 1, "L28 slide 5",
   "Why do chelating agents such as EDTA form very strong complexes (high K<sub>f</sub>)?",
   ["One molecule binds the metal ion through several donor atoms (EDTA: six)", "They are strong acids", "They are insoluble", "They have no lone pairs"],
   "<p>A chelator wraps around the metal with multiple donor atoms, so it is much harder to remove than several separate single-site ligands.</p>")

mc("ksp-22", "ksp", 2, "L28 slides 6&ndash;7",
   "Gadolinium is extremely toxic, yet it is given to patients as an MRI contrast agent. How?",
   ["Gd(III) is chelated: binding to a chelating ligand makes it about 50 times safer", "It is converted to Gd(0)", "It is diluted until it has no effect", "It is not toxic"],
   "<p>Chelation keeps the toxic metal ion from reacting with the body; the slide states safety increases 50-fold when Gd is chelated.</p>")

mc("ksp-23", "ksp", 1, "L28 slide 6",
   "Why do detergents contain chelating agents?",
   ["To bind Ca<sup>2+</sup> and Mg<sup>2+</sup> in hard water so they do not precipitate with soap", "To make water acidic", "To raise the K<sub>sp</sub> of soap", "To oxidize dirt"],
   "<p>Complexation displaces the calcium and magnesium ions that would precipitate (soap scum) in hard water.</p>")

mc("ksp-24", "ksp", 2, "L28 slide 8",
   "Hemoglobin can complex four O<sub>2</sub> molecules and shows cooperativity. What does that mean?",
   ["The binding constant for each further O<sub>2</sub> is higher than for the first", "Each further O<sub>2</sub> binds more weakly", "It binds only one O<sub>2</sub>", "It does not form complexes"],
   "<p>Cooperativity: once one O<sub>2</sub> is bound, the next binds more strongly (K<sub>2</sub> &gt; K<sub>1</sub>, and so on).</p>")

mc("ksp-25", "ksp", 3, "L28 slides 11&ndash;13",
   "How can Nd<sup>3+</sup> and Dy<sup>3+</sup> be separated from old magnets using a ligand and bicarbonate?",
   ["A selective ligand binds Nd<sup>3+</sup>, lowering its free concentration so it stays dissolved, while Dy<sub>2</sub>(CO<sub>3</sub>)<sub>3</sub> precipitates", "The ligand binds both, so both precipitate", "Bicarbonate precipitates Nd first", "Only filtration works"],
   "<p>The ligand acts as a sink for Nd<sup>3+</sup>, so Q for the neodymium carbonate stays below K<sub>sp</sub> and Nd remains in solution; Dy<sup>3+</sup> is unbound, Q &gt; K<sub>sp</sub> and its carbonate precipitates.</p>")

Ks = 1.3e-5 ** 2
num("ksp-26", "ksp", 2, "Rec 20 &middot; reverse",
    "The molar solubility of AgCl is 1.3&times;10<sup>&minus;5</sup> M. Calculate K<sub>sp</sub> (AgCl &rlarr; Ag<sup>+</sup> + Cl<sup>&minus;</sup>).",
    Ks, "",
    "<p>[Ag<sup>+</sup>] = [Cl<sup>&minus;</sup>] = 1.3&times;10<sup>&minus;5</sup>, so K<sub>sp</sub> = (1.3&times;10<sup>&minus;5</sup>)&sup2; = <b>%s</b>.</p>" % fmt(Ks, 3), text=fmt(Ks, 3))

mc("ksp-27", "ksp", 1, "Rec 20",
   "Which statement about K<sub>sp</sub> is true?",
   ["It has no units, excludes the pure solid, and changes only with temperature", "It depends on how much solid is present", "It has units of mol/L always", "A bigger K<sub>sp</sub> always means smaller solubility"],
   "<p>K<sub>sp</sub> is an equilibrium constant: dimensionless, solids omitted, temperature-dependent. Greater K<sub>sp</sub> means more soluble for the same formula type.</p>")

selfq("ksp-28", "ksp", 3, "Rec 20",
      "Explain three different ways to change how much of a sparingly soluble salt such as Mg(OH)<sub>2</sub> or Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> dissolves, and say which direction each moves the solubility. Use Le Ch&acirc;telier and Q vs K<sub>sp</sub>.",
      "<p><b>Model answer.</b> (1) <b>Common ion</b>: adding an ion already in the solid (Ca<sup>2+</sup> from CaCl<sub>2</sub>, or OH<sup>&minus;</sup> from NaOH) makes Q &gt; K<sub>sp</sub>, the equilibrium shifts toward the solid, and solubility <b>decreases</b>. (2) <b>pH / a sink</b>: strong acid removes OH<sup>&minus;</sup> (or reacts with phosphate or carbonate), so Q &lt; K<sub>sp</sub> and the solid <b>dissolves more</b>. (3) <b>Complexation</b>: a ligand that binds the metal ion (thiosulfate with Ag<sup>+</sup>, EDTA with Ca<sup>2+</sup>) lowers the free metal concentration, so Q &lt; K<sub>sp</sub> and solubility <b>increases</b>. Temperature is the only thing that changes K<sub>sp</sub> itself.</p>")
