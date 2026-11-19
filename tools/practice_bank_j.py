from practice_lib import *
import math

# ================================================================== SOLUTIONS (L26, Rec 19)
topic("solutions", "Solutions: dissolving &amp; concentration", "unit16", "Quiz 9",
      "Recipe: solution = solvent (major) + solute (minor); <b>&Delta;G<sub>soln</sub> = &Delta;H<sub>soln</sub> &minus; T&Delta;S<sub>soln</sub></b>; "
      "&Delta;H<sub>soln</sub> = (A&ndash;A broken, +) + (B&ndash;B broken, +) + (A&ndash;B formed, &minus;); &Delta;S<sub>soln</sub> &gt; 0 so &Delta;H usually decides; "
      "like dissolves like (polar/ionic = hydrophilic). Units: M = mol/L solution, m = mol/kg solvent, X = mole fraction, mass %, ppt/ppm/ppb (&times;10<sup>3</sup>/10<sup>6</sup>/10<sup>9</sup>); only M depends on T.")

mc("solutions-1", "solutions", 1, "L26 &middot; Rec 19",
   "In a solution of a small amount of salt in a lot of water, which is the solvent and which the solute?",
   ["Water is the solvent (major component); the salt is the solute (minor component)", "The salt is the solvent", "Both are solvents", "Water is the solute because it is a liquid"],
   "<p>The solvent is the major component and the solutes are the minor components, whatever their physical state.</p>")

mc("solutions-2", "solutions", 2, "L26 slide 3 &middot; Rec 19",
   "In the three-step picture of dissolving A in B, what are the signs of &Delta;H for (1) separating B particles, (2) separating A particles, (3) forming A&ndash;B attractions?",
   ["(1) positive, (2) positive, (3) negative", "(1) negative, (2) negative, (3) positive", "All three positive", "All three negative"],
   "<p>Breaking attractions costs energy (positive). Forming new A&ndash;B attractions releases energy (negative). &Delta;H<sub>soln</sub> is the sum, so the size of step 3 decides its sign.</p>")

mc("solutions-3", "solutions", 2, "L26 slide 3",
   "When is dissolving <b>exothermic</b> (&Delta;H<sub>soln</sub> &lt; 0)?",
   ["When forming the solute&ndash;solvent attractions releases more energy than separating the pure components costs", "When &Delta;S<sub>soln</sub> is positive", "When the solute is a gas", "When the solvent is non-polar"],
   "<p>&Delta;H<sub>soln</sub> = &Delta;H<sub>1</sub> + &Delta;H<sub>2</sub> + &Delta;H<sub>3</sub>. It is negative when |&Delta;H<sub>3</sub>| &gt; &Delta;H<sub>1</sub> + &Delta;H<sub>2</sub>.</p>")

mc("solutions-4", "solutions", 2, "Rec 19",
   "Why does &Delta;H<sub>soln</sub> usually decide whether something dissolves?",
   ["&Delta;S<sub>soln</sub> is generally positive (a solution has more arrangements than the pure components), so the entropy term favours mixing and the enthalpy term is the one that varies", "&Delta;S<sub>soln</sub> is always zero", "T&Delta;S is always larger than &Delta;H", "Because &Delta;G does not depend on &Delta;H"],
   "<p>Mixing always gains entropy, so the remaining question is whether &Delta;H<sub>soln</sub> is too positive to be overcome.</p>")

mc("solutions-5", "solutions", 1, "L26 &middot; Rec 19",
   "Which solute should dissolve readily in water?",
   ["NaCl or sugar (polar/ionic: hydrophilic)", "Oil or wax (non-polar: hydrophobic)", "Both equally", "Neither"],
   "<p>Polar solvents dissolve polar and ionic solutes through strong dipole&ndash;dipole, ion&ndash;dipole and hydrogen-bond attractions (large |&Delta;H<sub>3</sub>|). Non-polar solutes cannot pay for breaking water&rsquo;s hydrogen bonds.</p>")

mc("solutions-6", "solutions", 2, "Rec 19",
   "Why is a non-polar solute generally immiscible in water?",
   ["The solvent&ndash;solvent forces (water&rsquo;s hydrogen bonds) are much stronger than the solvent&ndash;solute forces, so step 3 cannot repay step 1", "The solute is too heavy", "Water has no intermolecular forces", "Non-polar molecules are always solids"],
   "<p>Separating water molecules costs a lot, and the weak dispersion forces formed with a non-polar solute return little: &Delta;H<sub>soln</sub> is too positive.</p>")

mc("solutions-7", "solutions", 3, "L26 slide 4",
   "CaCl<sub>2</sub> dissolves exothermically (&Delta;H<sub>soln</sub> = &minus;68.2 kJ/mol) yet its solubility <b>increases</b> with temperature. What does the slide say about this?",
   ["There is more at play than van&rsquo;t Hoff: &Delta;H and &Delta;S themselves depend on T", "The data are wrong", "Exothermic dissolving always gets less soluble when heated", "Solubility never depends on T"],
   "<p>A simple van&rsquo;t Hoff argument would predict lower solubility on heating for an exothermic process, but the curve rises, so the temperature dependence of &Delta;H and &Delta;S matters.</p>")

mc("solutions-8", "solutions", 2, "L26 slide 4",
   "NH<sub>4</sub>NO<sub>3</sub> has &Delta;H<sub>soln</sub> = +25.7 kJ/mol and dissolves in water. What must be true?",
   ["T&Delta;S<sub>soln</sub> &gt; &Delta;H<sub>soln</sub> so that &Delta;G<sub>soln</sub> &lt; 0; the solution cools; and the solubility rises steeply with T", "&Delta;S<sub>soln</sub> is negative", "&Delta;G<sub>soln</sub> is positive", "It cannot dissolve"],
   "<p>An endothermic dissolving is driven by entropy: &Delta;G = &Delta;H &minus; T&Delta;S &lt; 0 needs T&Delta;S larger than +25.7 kJ/mol, and hotter water makes T&Delta;S bigger, so more dissolves.</p>")

mc("solutions-9", "solutions", 1, "L26 slide 5",
   "Which concentration unit changes when the temperature changes (the solution expands)?",
   ["Molarity", "Molality", "Mole fraction", "Mass percent"],
   "<p>Molarity uses the <b>volume</b> of solution, which depends on temperature. Molality, mole fraction and mass percent use masses or mole counts.</p>")

mm = (11.69 / 58.44) / 0.2500
num("solutions-10", "solutions", 2, "L26 slide 5",
    "11.69 g of NaCl (M = 58.44 g/mol) is dissolved in 250.0 g of water. Find the molality in mol/kg (treat NaCl as formula units).",
    mm, "m",
    "<p>n = 11.69/58.44 = 0.2000 mol. Molality = moles solute / <b>kg of solvent</b> = 0.2000/0.2500 = <b>%s m</b>.</p>" % fmt(mm, 3),
    text="%s m" % fmt(mm, 3))

num("solutions-11", "solutions", 1, "L26 slide 5",
    "A mixture has 2.0 mol of ethanol and 8.0 mol of water. What is the mole fraction of ethanol?",
    0.20, "",
    "<p>X = moles of ethanol / total moles = 2.0/(2.0 + 8.0) = <b>0.20</b> (no units).</p>", text="0.20")

num("solutions-12", "solutions", 1, "L26 slide 5",
    "10.0 g of sugar is dissolved in 90.0 g of water. What is the mass percentage of sugar?",
    10.0, "%",
    "<p>Mass % = (g solute / g <b>solution</b>) &times; 100 = 10.0/(10.0 + 90.0) &times; 100 = <b>10.0%</b>.</p>", text="10.0 %")

num("solutions-13", "solutions", 2, "L26 slide 5",
    "A 2.0 kg water sample contains 3.0 mg of lead. What is the lead concentration in ppm (mass of solute / mass of solution &times; 10<sup>6</sup>)?",
    1.5, "ppm",
    "<p>3.0 mg = 3.0&times;10<sup>&minus;6</sup> kg. ppm = (3.0&times;10<sup>&minus;6</sup>/2.0) &times; 10<sup>6</sup> = <b>1.5 ppm</b> (equivalently 3.0 mg / 2.0 kg = 1.5 mg per kg).</p>", text="1.5 ppm")

Mo = (4.00 / 40.00) / 0.2500
num("solutions-14", "solutions", 2, "L26 slide 5",
    "4.00 g of NaOH (M = 40.00 g/mol) is dissolved in water to make 250.0 mL of solution. What is the molarity?",
    Mo, "M",
    "<p>n = 4.00/40.00 = 0.100 mol; V = 0.2500 L; M = 0.100/0.2500 = <b>%s M</b>.</p>" % fmt(Mo, 3), text="%s M" % fmt(Mo, 3))

mc("solutions-15", "solutions", 2, "L26 slides 7&ndash;9",
   "How can a layered plastic package be recycled by selective dissolution?",
   ["Choose a solvent and temperature that dissolve one polymer, filter off the rest, then precipitate the polymer and reuse the solvent", "Melt everything together", "Burn it", "Dissolve all the layers at once in water"],
   "<p>&ldquo;Dissolve &rarr; filter &rarr; precipitate&rdquo;: solubility differences between PE, EVOH and PET make the separation possible; solvent recovery and energy use are the next challenge.</p>")

selfq("solutions-16", "solutions", 3, "L26 slide 3 &middot; Rec 19",
      "Explain in terms of the three steps why a polar solute dissolves in water but a non-polar solute usually does not.",
      "<p><b>Model answer.</b> Dissolving A in B: step 1 separates B particles (cost, &Delta;H<sub>1</sub> &gt; 0), step 2 separates A particles (cost, &Delta;H<sub>2</sub> &gt; 0), step 3 forms A&ndash;B attractions (release, &Delta;H<sub>3</sub> &lt; 0). &Delta;H<sub>soln</sub> is the sum. For a polar or ionic solute in water, step 3 (ion&ndash;dipole, dipole&ndash;dipole, hydrogen bonds) is large, so &Delta;H<sub>soln</sub> is small or negative; add the positive &Delta;S<sub>soln</sub> and &Delta;G &lt; 0. For a non-polar solute, step 3 is only weak dispersion forces while step 1 (breaking water&rsquo;s hydrogen bonds) is large, so &Delta;H<sub>soln</sub> is too positive and the entropy gain cannot compensate: immiscible.</p>")

# ================================================================== ACIDS AND BASES (L27, Rec 19)
topic("acidbase", "Acids, bases &amp; pH", "unit17", "Quiz 9",
      "Recipe: <b>Br&oslash;nsted&ndash;Lowry</b> acid = proton donor, base = proton acceptor (Lewis: electron-pair acceptor/donor); conjugates differ by one H<sup>+</sup>; "
      "<b>pH = &minus;log[H<sub>3</sub>O<sup>+</sup>]</b>, pH + pOH = 14, K<sub>w</sub> = 10<sup>&minus;14</sup>; <b>K<sub>a</sub>K<sub>b</sub> = K<sub>w</sub></b>, pK<sub>a</sub> + pK<sub>b</sub> = 14, small pK<sub>a</sub> = strong acid; "
      "<b>pH = pK<sub>a</sub> + log([A<sup>&minus;</sup>]/[HA])</b>; titration: equivalence pH 7 (strong/strong), &gt;7 (weak acid), midpoint pH = pK<sub>a</sub>.")

mc("acidbase-1", "acidbase", 1, "Rec 19",
   "Which acid&ndash;base definition is the broadest?",
   ["Lewis (electron-pair acceptor / donor)", "Arrhenius", "Br&oslash;nsted&ndash;Lowry", "They are equally broad"],
   "<p>Arrhenius (H<sup>+</sup> or OH<sup>&minus;</sup> in water) is narrowest; Br&oslash;nsted&ndash;Lowry (proton transfer) is wider; Lewis (electron pairs) is broadest.</p>")

mc("acidbase-2", "acidbase", 2, "Rec 19",
   "In BF<sub>3</sub> + :NH<sub>3</sub> &rarr; F<sub>3</sub>B&ndash;NH<sub>3</sub>, which is the Lewis acid, and what is the product called?",
   ["BF<sub>3</sub> is the Lewis acid (accepts an electron pair); the product is an adduct with a coordinate covalent bond", "NH<sub>3</sub> is the Lewis acid; the product is an ion pair", "BF<sub>3</sub> is the Lewis base", "Neither; there is no acid&ndash;base reaction"],
   "<p>NH<sub>3</sub> donates its lone pair (Lewis base); BF<sub>3</sub> has an empty orbital and accepts it (Lewis acid). Both electrons of the new bond come from the base: a coordinate covalent bond in an acid&ndash;base adduct.</p>")

mc("acidbase-3", "acidbase", 1, "Rec 19",
   "Which is amphiprotic (can donate or accept a proton)?",
   ["H<sub>2</sub>O", "Cl<sup>&minus;</sup>", "H<sub>3</sub>O<sup>+</sup> only", "CH<sub>4</sub>"],
   "<p>Water can donate H<sup>+</sup> (to give OH<sup>&minus;</sup>) or accept H<sup>+</sup> (to give H<sub>3</sub>O<sup>+</sup>): amphiprotic, and self-ionizing.</p>")

mc("acidbase-4", "acidbase", 1, "L27 slide 4",
   "What is the conjugate acid of NH<sub>3</sub>, and what is the conjugate base of HCl?",
   ["NH<sub>4</sub><sup>+</sup> and Cl<sup>&minus;</sup>", "NH<sub>2</sub><sup>&minus;</sup> and H<sub>2</sub>Cl<sup>+</sup>", "NH<sub>4</sub><sup>+</sup> and H<sub>3</sub>O<sup>+</sup>", "NH<sub>2</sub><sup>&minus;</sup> and Cl<sup>&minus;</sup>"],
   "<p>A conjugate acid has one more H<sup>+</sup> than its base: NH<sub>3</sub> + H<sup>+</sup> = NH<sub>4</sub><sup>+</sup>. A conjugate base has one fewer: HCl &minus; H<sup>+</sup> = Cl<sup>&minus;</sup>.</p>")

mc("acidbase-5", "acidbase", 2, "Rec 19 problem 1",
   "In CH<sub>3</sub>CO<sub>2</sub>H + NH<sub>3</sub> &rlarr; CH<sub>3</sub>CO<sub>2</sub><sup>&minus;</sup> + NH<sub>4</sub><sup>+</sup>, which are the two conjugate pairs?",
   ["CH<sub>3</sub>CO<sub>2</sub>H / CH<sub>3</sub>CO<sub>2</sub><sup>&minus;</sup> and NH<sub>4</sub><sup>+</sup> / NH<sub>3</sub>", "CH<sub>3</sub>CO<sub>2</sub>H / NH<sub>3</sub> and CH<sub>3</sub>CO<sub>2</sub><sup>&minus;</sup> / NH<sub>4</sub><sup>+</sup>", "CH<sub>3</sub>CO<sub>2</sub>H / NH<sub>4</sub><sup>+</sup> only", "There is only one pair"],
   "<p>Each pair differs by one proton: acetic acid gives up H<sup>+</sup> to become acetate; ammonia takes it to become ammonium. Every acid&ndash;base reaction has two conjugate pairs.</p>")

mc("acidbase-6", "acidbase", 2, "L27 slide 4",
   "In HA + H<sub>2</sub>O &rlarr; A<sup>&minus;</sup> + H<sub>3</sub>O<sup>+</sup>, what role does water play?",
   ["Base: it accepts a proton and H<sub>3</sub>O<sup>+</sup> is its conjugate acid", "Acid: H<sub>3</sub>O<sup>+</sup> is its conjugate base", "Neither; it is a spectator", "It is the conjugate base of HA"],
   "<p>Water accepts H<sup>+</sup> from HA, so it is the (Br&oslash;nsted) base; H<sub>3</sub>O<sup>+</sup> is the conjugate acid. The pairs are HA/A<sup>&minus;</sup> and H<sub>3</sub>O<sup>+</sup>/H<sub>2</sub>O.</p>")

num("acidbase-7", "acidbase", 1, "L27 slide 2",
    "What is the pH of 0.0010 M HCl (a strong acid)?",
    3.0, "",
    "<p>Strong acid: fully dissociated, [H<sub>3</sub>O<sup>+</sup>] = 1.0&times;10<sup>&minus;3</sup> M. pH = &minus;log(10<sup>&minus;3</sup>) = <b>3.00</b>.</p>", text="3.00")

pH_b = 14 + math.log10(0.050)
num("acidbase-8", "acidbase", 2, "Rec 19",
    "What is the pH of 0.050 M NaOH (strong base) at 25 &deg;C?",
    pH_b, "",
    "<p>[OH<sup>&minus;</sup>] = 0.050 M. pOH = &minus;log 0.050 = 1.30; pH = 14.00 &minus; 1.30 = <b>%s</b>.</p>" % fmt(pH_b, 4), text=fmt(pH_b, 4))

H4 = 10 ** -4.50
num("acidbase-9", "acidbase", 1, "L27 slide 2",
    "Black coffee has pH 4.50. Find [H<sub>3</sub>O<sup>+</sup>] in M.",
    H4, "M",
    "<p>[H<sub>3</sub>O<sup>+</sup>] = 10<sup>&minus;pH</sup> = 10<sup>&minus;4.50</sup> = <b>%s M</b>.</p>" % fmt(H4, 3), text="%s M" % fmt(H4, 3))

pHo = 14 + math.log10(2.0e-4)
num("acidbase-10", "acidbase", 2, "Rec 19",
    "A solution has [OH<sup>&minus;</sup>] = 2.0&times;10<sup>&minus;4</sup> M at 25 &deg;C. What is its pH?",
    pHo, "",
    "<p>pOH = &minus;log(2.0&times;10<sup>&minus;4</sup>) = 3.70, so pH = 14 &minus; 3.70 = <b>%s</b> (basic).</p>" % fmt(pHo, 4), text=fmt(pHo, 4))

mc("acidbase-11", "acidbase", 1, "L27 slide 2",
   "How much more acidic (in [H<sup>+</sup>]) is a solution of pH 3 than a solution of pH 5?",
   ["100 times", "2 times", "10 times", "1000 times"],
   "<p>The pH scale is logarithmic: each unit is a factor of 10, so two units is 10<sup>2</sup> = 100.</p>")

Hf = 1e-14 / 2.5e-3
num("acidbase-12", "acidbase", 2, "Rec 19",
    "At 25 &deg;C, [H<sub>3</sub>O<sup>+</sup>] = 2.5&times;10<sup>&minus;3</sup> M. Find [OH<sup>&minus;</sup>] using K<sub>w</sub> = 1.0&times;10<sup>&minus;14</sup>.",
    Hf, "M",
    "<p>[OH<sup>&minus;</sup>] = K<sub>w</sub>/[H<sub>3</sub>O<sup>+</sup>] = 10<sup>&minus;14</sup>/(2.5&times;10<sup>&minus;3</sup>) = <b>%s M</b>.</p>" % fmt(Hf, 3), text="%s M" % fmt(Hf, 3))

Ka2 = (2.0e-3) ** 2 / (0.20 - 2.0e-3)
num("acidbase-13", "acidbase", 3, "Rec 19 problem 3",
    "A 0.20 M solution of a weak acid HA has pH 2.70 at 25 &deg;C. Find K<sub>a</sub>.",
    Ka2, "",
    "<p>[H<sup>+</sup>] = 10<sup>&minus;2.70</sup> = 2.0&times;10<sup>&minus;3</sup> M = [A<sup>&minus;</sup>]. [HA] &asymp; 0.20 &minus; 0.0020 &asymp; 0.20. K<sub>a</sub> = (2.0&times;10<sup>&minus;3</sup>)<sup>2</sup>/0.20 = <b>%s</b>.</p>" % fmt(Ka2, 3),
    tol=0.05, text=fmt(Ka2, 3))

pKa_ = -math.log10(1.8e-5)
num("acidbase-14", "acidbase", 1, "L27 slide 5",
    "An acid has K<sub>a</sub> = 1.8&times;10<sup>&minus;5</sup>. What is its pK<sub>a</sub>?",
    pKa_, "",
    "<p>pK<sub>a</sub> = &minus;log(1.8&times;10<sup>&minus;5</sup>) = <b>%s</b> (acetic acid is about 4.76).</p>" % fmt(pKa_, 3), tol=0.01, text=fmt(pKa_, 3))

Kb_F = 10 ** -(14 - 3.20)
num("acidbase-15", "acidbase", 3, "L27 slide 6",
    "HF has pK<sub>a</sub> = 3.20. Find K<sub>b</sub> of its conjugate base F<sup>&minus;</sup>.",
    Kb_F, "",
    "<p>pK<sub>b</sub> = 14.00 &minus; 3.20 = 10.80, so K<sub>b</sub> = 10<sup>&minus;10.80</sup> = <b>%s</b>. (Equivalently K<sub>a</sub>K<sub>b</sub> = K<sub>w</sub>.) A weak acid gives a weak but non-negligible conjugate base.</p>" % fmt(Kb_F, 3),
    tol=0.04, text=fmt(Kb_F, 3))

mc("acidbase-16", "acidbase", 2, "L27 slide 5 &middot; Rec 19",
   "Rank by <b>increasing</b> acid strength: HCN (pK<sub>a</sub> 9.21), HNO<sub>3</sub> (&minus;1.37), HF (3.20), H<sub>2</sub>O (14.00).",
   ["H<sub>2</sub>O &lt; HCN &lt; HF &lt; HNO<sub>3</sub>", "HNO<sub>3</sub> &lt; HF &lt; HCN &lt; H<sub>2</sub>O", "HF &lt; HCN &lt; H<sub>2</sub>O &lt; HNO<sub>3</sub>", "HCN &lt; H<sub>2</sub>O &lt; HF &lt; HNO<sub>3</sub>"],
   "<p>Smaller pK<sub>a</sub> means stronger acid: H<sub>2</sub>O (14.00) is weakest, then HCN (9.21), HF (3.20), and HNO<sub>3</sub> (&minus;1.37) is strongest.</p>")

mc("acidbase-17", "acidbase", 2, "Rec 19 problem 2",
   "Using K<sub>a</sub> values (H<sub>2</sub>O 1.8&times;10<sup>&minus;16</sup>, H<sub>2</sub>S 1.0&times;10<sup>&minus;7</sup>, HF 7.2&times;10<sup>&minus;4</sup>, HCl 1&times;10<sup>6</sup>), rank the acids from weakest to strongest.",
   ["H<sub>2</sub>O &lt; H<sub>2</sub>S &lt; HF &lt; HCl", "HCl &lt; HF &lt; H<sub>2</sub>S &lt; H<sub>2</sub>O", "H<sub>2</sub>S &lt; H<sub>2</sub>O &lt; HF &lt; HCl", "HF &lt; HCl &lt; H<sub>2</sub>O &lt; H<sub>2</sub>S"],
   "<p>A larger K<sub>a</sub> means a stronger acid. Order of K<sub>a</sub>: 10<sup>&minus;16</sup> &lt; 10<sup>&minus;7</sup> &lt; 10<sup>&minus;3.1</sup> &lt; 10<sup>6</sup>.</p>")

mc("acidbase-18", "acidbase", 2, "L27 slide 6",
   "Which conjugate base is the <b>weakest</b>: F<sup>&minus;</sup>, CN<sup>&minus;</sup>, Cl<sup>&minus;</sup>, OH<sup>&minus;</sup>?",
   ["Cl<sup>&minus;</sup> (conjugate of the strongest acid, HCl)", "F<sup>&minus;</sup>", "CN<sup>&minus;</sup>", "OH<sup>&minus;</sup>"],
   "<p>The strength of an acid is opposite to that of its conjugate base. HCl is the strongest of the four parent acids (HCl, HF, HCN, H<sub>2</sub>O), so Cl<sup>&minus;</sup> is the weakest base.</p>")

mc("acidbase-19", "acidbase", 2, "L27 slide 7",
   "Why can water not distinguish the strengths of HCl, HBr and HNO<sub>3</sub>?",
   ["Leveling effect: any acid stronger than H<sub>3</sub>O<sup>+</sup> simply converts into the stoichiometric amount of H<sub>3</sub>O<sup>+</sup>", "They are all weak acids", "They have the same bond strength", "Water is not a base"],
   "<p>In water the strongest acid that can exist is H<sub>3</sub>O<sup>+</sup>. Anything stronger fully transfers its proton, so all give the same [H<sub>3</sub>O<sup>+</sup>].</p>")

mc("acidbase-20", "acidbase", 2, "L27 slide 7",
   "Why is a solution of Al<sup>3+</sup> in water acidic?",
   ["The small, highly charged ion polarizes coordinated water molecules, weakening their O&ndash;H bonds so H<sup>+</sup> is released", "Al<sup>3+</sup> is itself a proton donor", "Al<sup>3+</sup> reacts with OH<sup>&minus;</sup> to make water", "It is not acidic"],
   "<p>Metal ions with high charge density pull on the water&rsquo;s oxygen, making the O&ndash;H bond easier to break. Na<sup>+</sup> &lt; Mg<sup>2+</sup> &lt; Al<sup>3+</sup> in acidifying power.</p>")

mc("acidbase-21", "acidbase", 2, "L27 slide 8",
   "Why is HI a much stronger acid than HF?",
   ["The H&ndash;I bond (298 kJ/mol) is much weaker than H&ndash;F (570 kJ/mol), so it gives up H<sup>+</sup> far more easily", "F is larger than I", "HF is a stronger bond, so more acidic", "HI has fewer electrons"],
   "<p>The stronger the X&ndash;H bond, the less acidic: HF (570, pK<sub>a</sub> 3.20) &lt; HCl (432) &lt; HBr (366) &lt; HI (298, pK<sub>a</sub> &minus;9.3).</p>")

mc("acidbase-22", "acidbase", 2, "L27 slide 11 &middot; Rec 19",
   "A weak acid is titrated with a strong base. Where is the equivalence point, and why?",
   ["At pH &gt; 7, because what remains after neutralizing all the weak acid is its conjugate base", "Exactly at pH 7", "At pH &lt; 7, because the acid is still there", "There is no equivalence point"],
   "<p>At equivalence all HA has become A<sup>&minus;</sup>, a weak base that makes the solution basic (use its pK<sub>b</sub>). For strong acid + strong base the equivalence pH is exactly 7; for a weak base + strong acid it is below 7.</p>")

Pm = 4.76 + math.log10(3.0)
num("acidbase-23", "acidbase", 3, "Rec 19",
    "A buffer contains acetic acid (pK<sub>a</sub> = 4.76) and acetate with [A<sup>&minus;</sup>]/[HA] = 3.0. What is its pH?",
    Pm, "",
    "<p>Henderson&ndash;Hasselbalch: pH = pK<sub>a</sub> + log([A<sup>&minus;</sup>]/[HA]) = 4.76 + log 3.0 = 4.76 + 0.48 = <b>%s</b>.</p>" % fmt(Pm, 3), text=fmt(Pm, 3))

ratio = 10 ** (4.00 - 3.75)
num("acidbase-24", "acidbase", 3, "Rec 19",
    "What ratio [HCOO<sup>&minus;</sup>]/[HCOOH] gives a pH of 4.00 in a formic acid buffer (pK<sub>a</sub> = 3.75)?",
    ratio, "",
    "<p>4.00 = 3.75 + log(ratio) &rArr; log(ratio) = 0.25 &rArr; ratio = 10<sup>0.25</sup> = <b>%s</b>.</p>" % fmt(ratio, 3), text=fmt(ratio, 3))

mc("acidbase-25", "acidbase", 2, "L27 slide 12",
   "On the titration curve of a weak acid with a strong base, what does the midpoint of the plateau tell you?",
   ["The pH there equals the pK<sub>a</sub> of the acid, and the solution resists pH change (a buffer)", "The equivalence point", "The pH is 7", "The acid is fully neutralized"],
   "<p>Half way to equivalence [HA] = [A<sup>&minus;</sup>], so the Henderson&ndash;Hasselbalch log term is 0 and pH = pK<sub>a</sub>. The flat region is the buffer region.</p>")

num("acidbase-26", "acidbase", 2, "L27 slides 10&ndash;11",
    "25.0 mL of 0.100 M weak acid HA is titrated with 0.200 M NaOH. What volume of NaOH (mL) reaches the equivalence point?",
    12.5, "mL",
    "<p>Moles of HA = 0.0250 L &times; 0.100 = 2.50&times;10<sup>&minus;3</sup> mol. Equivalence needs the same moles of base: V = 2.50&times;10<sup>&minus;3</sup>/0.200 = 0.0125 L = <b>12.5 mL</b>. (The midpoint, pH = pK<sub>a</sub>, is at half that, 6.25 mL.)</p>",
    text="12.5 mL")

mc("acidbase-27", "acidbase", 2, "L27 slides 5, 12",
   "To buffer a solution near pH 7.4, which weak acid from the L27 table is the best choice?",
   ["HOCl (pK<sub>a</sub> 7.40)", "HF (3.20)", "Acetic acid (4.76)", "HCN (9.21)"],
   "<p>A buffer works best within about &plusmn;1 pH unit of the acid&rsquo;s pK<sub>a</sub>, where [A<sup>&minus;</sup>] and [HA] are comparable. HOCl matches pH 7.4.</p>")

mc("acidbase-28", "acidbase", 2, "Rec 19 problem 4",
   "Alanine has an O&ndash;H proton (pK<sub>a</sub> 2.34) and an amine N&ndash;H proton (pK<sub>a</sub> 9.69). Which is deprotonated first as base is added?",
   ["The carboxylic acid O&ndash;H (lower pK<sub>a</sub>, more acidic)", "The amine N&ndash;H (higher pK<sub>a</sub>)", "Both at the same pH", "Neither"],
   "<p>The lower the pK<sub>a</sub>, the more acidic the proton and the earlier it is removed (already at pH of about 2). The amine proton leaves only in strongly basic solution (pH about 10).</p>")

mc("acidbase-29", "acidbase", 2, "L27 slides 14&ndash;16",
   "In the drought-stress plant sensor, how does the plant&rsquo;s vascular fluid change, and why does the sensor work?",
   ["It becomes less acidic (pH rises); a COF coating on silk microneedles changes colour with pH in a window tuned to pK<sub>a</sub> 5.6&ndash;7.6", "It becomes more acidic; the needle dissolves", "pH stays the same; the needle measures temperature", "It becomes pure water"],
   "<p>The colour-changing molecules react with protons; the molecular environment sets their pK<sub>a</sub>, so the colour transition happens in the pH range of plant fluid. Result: warning up to 48 hours earlier.</p>")

mc("acidbase-30", "acidbase", 3, "Rec 19",
   "At 25 &deg;C pH + pOH = 14. At 50 &deg;C, where K<sub>w</sub> is larger, which statement is correct?",
   ["pH + pOH = pK<sub>w</sub>, which is below 14 there, so the &ldquo;14&rdquo; shortcut no longer holds and neutral water has pH below 7", "pH + pOH is still exactly 14", "Water becomes acidic", "K<sub>w</sub> does not depend on T"],
   "<p>K<sub>w</sub> is an equilibrium constant, so it changes with temperature (the autoionization is endothermic). pH + pOH = pK<sub>w</sub>; the value 14 and neutral pH 7 are for 25 &deg;C. This is the &ldquo;14&rdquo; trap.</p>")

selfq("acidbase-31", "acidbase", 3, "L27 slides 10&ndash;12",
      "Sketch (in words) the titration curve of a weak acid with a strong base. Mark the starting pH, the buffer region, the midpoint, the equivalence point and the pH after it.",
      "<p><b>Model answer.</b> It starts at a pH above that of a strong acid of the same concentration (the weak acid is only partly dissociated). The pH rises steeply at first, then enters a <b>plateau</b> (buffer region) where adding a lot of base changes pH only slowly. The <b>midpoint</b> of the plateau (half the equivalence volume) has pH = pK<sub>a</sub>. At the <b>equivalence point</b> the curve rises sharply through pH above 7 (only the conjugate base A<sup>&minus;</sup> is left, a weak base). After that, excess strong base levels the pH off toward the pH of the base solution (about 12&ndash;13).</p>")
