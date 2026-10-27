from practice_lib import *
import math

# ================================================================== IONIC
topic("ionic", "Ionic bonding, Born&ndash;Haber &amp; crystal structures", "unit3", "Quiz 3",
      "Quiz 3 = Lewis dots + ion charges (K<sub>2</sub>O), reading a rock-salt picture (which colour is Cl<sup>&minus;</sup>?), "
      "&ldquo;which solid has the NaCl structure?&rdquo; (check the charge ratio), and labelling a Born&ndash;Haber diagram. "
      "Recipe: group number &rarr; ion charge &rarr; balance the formula; Born&ndash;Haber steps = sublimation, ionization energy, &frac12; bond dissociation, electron affinity, lattice energy.")

mc("ionic-1", "ionic", 1, "Quiz 3 style",
   "What are the charges of the ions in <b>Al<sub>2</sub>O<sub>3</sub></b>?",
   ["Al<sup>3+</sup> and O<sup>2&minus;</sup>", "Al<sup>2+</sup> and O<sup>3&minus;</sup>", "Al<sup>6+</sup> and O<sup>6&minus;</sup>", "Al<sup>+</sup> and O<sup>&minus;</sup>"],
   "<p>Group 13 loses 3 electrons (Al<sup>3+</sup>); group 16 gains 2 (O<sup>2&minus;</sup>). Balance: 2 &times; (+3) + 3 &times; (&minus;2) = 0. <b>The subscripts are how many ions, not the charge</b> (same trap as K<sub>2</sub>O: K is +1, not +2).</p>")

mc("ionic-2", "ionic", 1, "Quiz 3 style",
   "What is the formula of the compound formed from Mg<sup>2+</sup> and N<sup>3&minus;</sup>?",
   ["Mg<sub>3</sub>N<sub>2</sub>", "Mg<sub>2</sub>N<sub>3</sub>", "MgN", "Mg<sub>2</sub>N"],
   "<p>Find the least common multiple of the charges: 6. Three Mg<sup>2+</sup> = +6 and two N<sup>3&minus;</sup> = &minus;6. <b>Mg<sub>3</sub>N<sub>2</sub></b> (cross the charges: the 2 of Mg goes to N, the 3 of N goes to Mg).</p>")

mc("ionic-3", "ionic", 2, "Quiz 3 style",
   "Which of these 1 : 1 ionic compounds does <b>not</b> have the rock-salt (NaCl) structure?",
   ["CsCl", "MgO", "CaO", "NaCl"],
   "<p>A 1 : 1 ratio is necessary but not sufficient. CsCl&rsquo;s big Cs<sup>+</sup> cation fits 8 Cl<sup>&minus;</sup> neighbours (simple cubic lattice with a two-ion motif), while Na<sup>+</sup>, Mg<sup>2+</sup>, Ca<sup>2+</sup> are small enough for 6 (octahedral). The real Quiz 3 answer (CaO, not CaF<sub>2</sub>) used the ratio test; CaF<sub>2</sub> is 1 : 2 so it can never be rock salt.</p>")

mc("ionic-4", "ionic", 2, "Quiz 3 style",
   "In a Born&ndash;Haber cycle for NaCl, which step <b>releases</b> energy (is exothermic) on its own?",
   ["Cl(g) + e<sup>&minus;</sup> &rarr; Cl<sup>&minus;</sup>(g) (electron affinity)", "Na(g) &rarr; Na<sup>+</sup>(g) + e<sup>&minus;</sup> (ionization energy)", "Na(s) &rarr; Na(g) (sublimation)", "&frac12; Cl<sub>2</sub>(g) &rarr; Cl(g) (bond breaking)"],
   "<p>Taking an electron off an atom, vaporizing a solid and breaking a bond all <b>cost</b> energy. Adding an electron to Cl is favourable (energy released). The big payoff is the lattice-energy step (Na<sup>+</sup>(g) + Cl<sup>&minus;</sup>(g) &rarr; NaCl(s)), which is also exothermic.</p>")

num("ionic-5", "ionic", 3, "Rec 6 style",
    "Find the <b>lattice energy of NaCl</b> (energy released when gaseous ions form the solid, as a positive number in kJ/mol) from: &Delta;H<sub>f</sub>(NaCl) = &minus;411; sublimation of Na = +107; ionization energy of Na = +496; <b>&frac12;</b>&times;bond dissociation of Cl<sub>2</sub> = +122; electron affinity of Cl = &minus;349 (all kJ/mol).",
    787.0, "kJ/mol",
    "<p>Hess&rsquo;s law: the formation enthalpy equals the sum of all the steps. <br><span class=\"mono\">&Delta;H<sub>f</sub> = &Delta;H<sub>sub</sub> + IE + &frac12;BDE + EA + U<sub>lattice</sub></span></p>"
    "<p class=\"mono\">&minus;411 = 107 + 496 + 122 &minus; 349 + U &rarr; &minus;411 = 376 + U &rarr; U = &minus;787 kJ/mol</p>"
    "<p>So <b>787 kJ/mol</b> is released when the lattice forms. Remember the &frac12; for the diatomic: only half a mole of Cl<sub>2</sub> is needed per NaCl.</p>",
    hint="Add up the four steps before the lattice step: 107 + 496 + 122 &minus; 349.", alt=[-787.0], tol=0.005, text="787 kJ/mol")

r_ratio = (4 / 2.12) / (1 / 2.82)
num("ionic-6", "ionic", 3, "Rec 6 style",
    "Lattice energy scales roughly as |q<sub>+</sub>q<sub>&minus;</sub>| / r<sub>0</sub>. Estimate U(MgO)/U(NaCl) using r<sub>0</sub>(MgO) = 2.12 &Aring; and r<sub>0</sub>(NaCl) = 2.82 &Aring;.",
    r_ratio, "&times;",
    "<p>MgO: charge product (+2)(&minus;2) = 4, r<sub>0</sub> = 2.12 &Aring;. NaCl: product 1, r<sub>0</sub> = 2.82 &Aring;.</p>"
    "<p class=\"mono\">ratio &asymp; (4 / 2.12) / (1 / 2.82) = 4 &times; 2.82 / 2.12 = <b>%s</b></p>"
    "<p>(The real values, about 3800 vs 790 kJ/mol, give &asymp; 4.8; the simple proportion is close.) This is why MgO melts above 2800 &deg;C and NaCl at 801 &deg;C.</p>" % fmt(r_ratio, 3),
    tol=0.06, text="&asymp; %s" % fmt(r_ratio, 3))

mc("ionic-7", "ionic", 2, "Quiz 3 style",
   "Which compound should have the <b>largest</b> lattice energy (strongest ionic bonding)?",
   ["MgO", "NaCl", "KCl", "NaI"],
   "<p>Born&ndash;Land&eacute;: bigger charges and smaller ions &rarr; larger lattice energy. MgO has 2+/2&minus; (charge product 4) and small ions.</p>")

selfq("ionic-8", "ionic", 3, "Quiz 3 style",
      "Quiz 3 asks you to label missing steps on a Born&ndash;Haber diagram. List, <b>in order</b>, the steps that build K<sub>2</sub>O(s) from 2 K(s) and &frac12; O<sub>2</sub>(g), with the energy sign of each.",
      "<ol><li>2 K(s) &rarr; 2 K(g): <b>sublimation</b> (+).</li>"
      "<li>2 K(g) &rarr; 2 K<sup>+</sup>(g) + 2 e<sup>&minus;</sup>: <b>ionization energy</b> &times; 2 (+).</li>"
      "<li>&frac12; O<sub>2</sub>(g) &rarr; O(g): <b>&frac12; bond dissociation</b> (+).</li>"
      "<li>O(g) + e<sup>&minus;</sup> &rarr; O<sup>&minus;</sup>(g): <b>1st electron affinity</b> (&minus;).</li>"
      "<li>O<sup>&minus;</sup>(g) + e<sup>&minus;</sup> &rarr; O<sup>2&minus;</sup>(g): <b>2nd electron affinity</b> (<b>+</b>, because you push an electron onto an already-negative ion).</li>"
      "<li>2 K<sup>+</sup>(g) + O<sup>2&minus;</sup>(g) &rarr; K<sub>2</sub>O(s): <b>lattice energy</b> (large &minus;).</li></ol>"
      "<p>The sum of all six equals &Delta;H<sub>f</sub>(K<sub>2</sub>O). Typical mistakes: mixing up ionization energy (metal) with electron affinity (nonmetal), and forgetting the atomization step of the nonmetal.</p>")

# ================================================================== LEWIS
topic("lewis", "Lewis structures, dipoles &amp; bond strength", "unit4", "Quiz 3&ndash;4",
      "Recipe for any Lewis structure: (1) total valence electrons (add for &minus; charge, subtract for +); (2) skeleton with the least electronegative atom in the middle (H is never central); "
      "(3) single bonds, then fill octets outside; (4) leftovers go on the centre (expanded octet only for period 3+); (5) compute formal charges. "
      "Dipole: &mu; = &delta;&middot;r with 1 D = 0.2082 e&middot;&Aring;. Stronger bond = smaller atoms, higher bond order.")

sulfate = 6 + 4 * 6 + 2
num("lewis-1", "lewis", 1, "Rec 7 style",
    "How many <b>valence electrons</b> must appear in the Lewis structure of the sulfate ion, SO<sub>4</sub><sup>2&minus;</sup>?",
    sulfate, "electrons",
    "<p>S: 6. Four O: 4 &times; 6 = 24. The 2&minus; charge adds <b>2</b> electrons: 6 + 24 + 2 = <b>32</b>.</p>", tol=0.0, atol=0.01, text="32")

num("lewis-2", "lewis", 2, "Rec 7 style",
    "In the Lewis structure <b>[ O&ndash;C&equiv;N ]<sup>&minus;</sup></b> (single bond O&ndash;C with three lone pairs on O; triple bond C&equiv;N with one lone pair on N), what is the <b>formal charge on oxygen</b>?",
    -1, "",
    "<p>Formal charge = valence electrons &minus; (lone-pair electrons + &frac12; bonding electrons) = 6 &minus; (6 + &frac12;&times;2) = 6 &minus; 7 = <b>&minus;1</b>. (N: 5 &minus; (2 + 3) = 0; C: 4 &minus; 4 = 0; the charges add up to the ion&rsquo;s &minus;1.)</p>",
    tol=0.0, atol=0.01, text="&minus;1")

dh = 1.82 * 0.2082 / 0.917
num("lewis-3", "lewis", 2, "Rec 7 style",
    "The H&ndash;F bond length is 0.917 &Aring; and its dipole moment is 1.82 D. What partial charge &delta; (in units of e) sits on the atoms? (1 D = 0.2082 e&middot;&Aring;.)",
    dh, "e",
    "<p>&mu; = &delta;&middot;r so &delta; = &mu; / r = (1.82 &times; 0.2082 e&middot;&Aring;) / 0.917 &Aring; = <b>%s e</b>. About 41%% of a full electron charge has shifted towards F (a polar covalent bond, not fully ionic).</p>" % fmt(dh, 3),
    tol=0.02, text="%s e" % fmt(dh, 3))

pi = (1 - math.exp(-((3.98 - 2.20) ** 2) / 4)) * 100
num("lewis-4", "lewis", 2, "Rec 7 style",
    "Use % ionic character = 1 &minus; exp(&minus;&frac14;(&Delta;&chi;)&sup2;) &times; 100 to find the percent ionic character of H&ndash;F (&chi;<sub>H</sub> = 2.20, &chi;<sub>F</sub> = 3.98).",
    pi, "%",
    "<p>&Delta;&chi; = 3.98 &minus; 2.20 = 1.78. (&Delta;&chi;)&sup2; = 3.17; &frac14; of that = 0.792; exp(&minus;0.792) = 0.453; 1 &minus; 0.453 = 0.547. <b>&asymp; %s %%</b> ionic. The bond is polar covalent, nearer the ionic end than Cl&ndash;Cl but not fully ionic.</p>" % fmt(pi, 3),
    tol=0.03, text="%s %%" % fmt(pi, 3))

mc("lewis-5", "lewis", 1, "Rec 7 style",
   "Which carbon&ndash;carbon bond is the <b>strongest</b> (highest bond energy)?",
   ["C&equiv;C in C<sub>2</sub>H<sub>2</sub>", "C=C in C<sub>2</sub>H<sub>4</sub>", "C&ndash;C in C<sub>2</sub>H<sub>6</sub>", "They are all equal"],
   "<p>Higher bond order = stronger (and shorter) bond: triple &gt; double &gt; single. Rec 7 ranks C<sub>2</sub>H<sub>6</sub> &lt; C<sub>2</sub>H<sub>4</sub> &lt; C<sub>2</sub>H<sub>2</sub>.</p>")

mc("lewis-6", "lewis", 1, "Rec 7 style",
   "Which hydrogen halide has the <b>strongest</b> H&ndash;X bond?",
   ["HF", "HCl", "HBr", "HI"],
   "<p>Smaller atom &rarr; better orbital overlap &rarr; stronger bond. Ranking: HI &lt; HBr &lt; HCl &lt; HF.</p>")

mc("lewis-7", "lewis", 2, "Rec 7 style",
   "Which of these molecules needs an <b>expanded octet</b> on its central atom?",
   ["SF<sub>4</sub>", "BF<sub>3</sub>", "CF<sub>4</sub>", "NF<sub>3</sub>"],
   "<p>SF<sub>4</sub>: S has 4 bonds + 1 lone pair = 10 electrons, allowed because S is in period 3 (it can use d orbitals). BF<sub>3</sub> is electron-deficient (6), CF<sub>4</sub> and NF<sub>3</sub> obey the octet. Period 2 atoms (C, N, O, F) can <b>never</b> exceed 8.</p>")

selfq("lewis-8", "lewis", 3, "Rec 7 style",
      "Draw the Lewis structure of the nitrate ion, NO<sub>3</sub><sup>&minus;</sup>. How many resonance forms are there and what are the formal charges?",
      "<ol><li>Valence electrons: 5 + 3 &times; 6 + 1 = <b>24</b>.</li>"
      "<li>N in the centre, three O around it, three N&ndash;O single bonds (6 e<sup>&minus;</sup>), then octets on each O (18 e<sup>&minus;</sup>) = 24 total, but N has only 6.</li>"
      "<li>Make one lone pair on an O into an N=O double bond: N now has 8.</li>"
      "<li>Formal charges: N = +1, the double-bonded O = 0, the two single-bonded O = &minus;1 each (total &minus;1).</li>"
      "<li>The double bond can be on any of the three O atoms: <b>3 equivalent resonance forms</b>; the real ion is a blend (all N&ndash;O bonds equal, bond order 1&#8531;).</li></ol>")

mc("lewis-9", "lewis", 2, "Rec 7 style",
   "Why are ionic solids typically more <b>brittle</b> than covalent solids?",
   ["Ionic bonding is non-directional electrostatics: shifting a layer lines up like charges, and repulsion splits the crystal",
    "Ionic bonds are weaker than covalent bonds",
    "Ionic solids contain no electrons that can move",
    "Covalent bonds are always more flexible than ionic bonds"],
   "<p>Rec 7 says exactly this: a one-lattice-spacing shift puts + next to + and &minus; next to &minus;, so repulsion cascades into fracture (chalk is an example). Covalent bonds are directional and tolerate a few broken bonds. These are relative trends: quartz and graphite are brittle covalent solids.</p>")

# ================================================================== VSEPR
topic("vsepr", "VSEPR: Lewis &rarr; AXE &rarr; shape &rarr; polarity", "unit5", "Quiz 4",
      "Quiz 4 problem 1: draw the Lewis structure (3 pts), give the AXE number (1 pt), name the shape (1 pt). "
      "Recipe: count groups on the centre = atoms attached (X) + lone pairs (E). 2 &rarr; linear, 3 &rarr; trigonal planar, 4 &rarr; tetrahedral, 5 &rarr; trigonal bipyramidal, 6 &rarr; octahedral; "
      "then <b>name the shape by the atoms only</b>. Lone pairs: 5 groups &rarr; equatorial; 6 groups &rarr; opposite each other.")

mc("vsepr-1", "vsepr", 1, "Quiz 4 style",
   "What is the AXE notation for <b>XeF<sub>4</sub></b>?",
   ["AX<sub>4</sub>E<sub>2</sub>", "AX<sub>4</sub>E", "AX<sub>6</sub>", "AX<sub>4</sub>"],
   "<p>Xe: 8 valence electrons + 4 &times; 7 (F) = 36. Four Xe&ndash;F bonds use 8; F lone pairs use 24; the last 4 electrons are <b>two lone pairs on Xe</b>. A = Xe, X = 4 F atoms, E = 2 lone pairs: AX<sub>4</sub>E<sub>2</sub>.</p>")

mc("vsepr-2", "vsepr", 1, "Quiz 4 style",
   "What is the molecular geometry (shape) of XeF<sub>4</sub>?",
   ["Square planar", "Octahedral", "Tetrahedral", "See-saw"],
   "<p>6 groups &rarr; octahedral electron arrangement; the two lone pairs sit opposite each other (180&deg;) to minimize repulsion, leaving four F in one flat square. Octahedral is the <b>electron</b> geometry, not the shape.</p>")

mc("vsepr-3", "vsepr", 2, "Quiz 4 style",
   "What is the shape of SF<sub>4</sub> (AX<sub>4</sub>E)?",
   ["See-saw", "Tetrahedral", "Square planar", "Trigonal pyramidal"],
   "<p>5 groups &rarr; trigonal bipyramid. The lone pair goes <b>equatorial</b> (fewest 90&deg; repulsions), leaving 2 axial + 2 equatorial F: a see-saw.</p>")

mc("vsepr-4", "vsepr", 2, "Quiz 4 style",
   "Which of these molecules is <b>polar</b>?",
   ["NH<sub>3</sub>", "CO<sub>2</sub>", "BF<sub>3</sub>", "CCl<sub>4</sub>"],
   "<p>CO<sub>2</sub> (linear), BF<sub>3</sub> (trigonal planar) and CCl<sub>4</sub> (tetrahedral) have polar bonds, but their shapes are symmetric so the bond dipoles cancel. NH<sub>3</sub> is trigonal <b>pyramidal</b> with a lone pair: the dipoles do not cancel.</p>",
   hint="Draw the shape before drawing the arrows.")

mc("vsepr-5", "vsepr", 3, "Quiz 4 style",
   "What is the shape of ClF<sub>3</sub>?",
   ["T-shaped", "Trigonal planar", "Trigonal pyramidal", "See-saw"],
   "<p>Cl: 7 + 3 &times; 7 = 28 electrons: 3 bonds + 2 lone pairs = AX<sub>3</sub>E<sub>2</sub>. 5 groups &rarr; both lone pairs equatorial, leaving one equatorial and two axial F: <b>T-shaped</b>.</p>")

mc("vsepr-6", "vsepr", 2, "Quiz 4 style",
   "Why is the H&ndash;O&ndash;H angle in water (about 104.5&deg;) smaller than the ideal tetrahedral 109.5&deg;?",
   ["Lone pairs repel more strongly than bonding pairs and squeeze the bonds together", "Oxygen is less electronegative than hydrogen", "Water has a double bond", "Hydrogen atoms are larger than oxygen"],
   "<p>A lone pair is held by one nucleus only, so its cloud is fatter and pushes the bonding pairs closer. Order of repulsion: lone&ndash;lone &gt; lone&ndash;bond &gt; bond&ndash;bond.</p>")

selfq("vsepr-7", "vsepr", 3, "Quiz 4 style",
      "For <b>BrF<sub>5</sub></b>: draw the Lewis structure, give the AXE notation, the electron geometry, the molecular shape, and say whether it is polar.",
      "<ol><li>Valence electrons: 7 + 5 &times; 7 = <b>42</b>. Five Br&ndash;F bonds use 10; 15 lone pairs on F use 30; the remaining 2 e<sup>&minus;</sup> are one lone pair on Br.</li>"
      "<li><b>AX<sub>5</sub>E</b>.</li><li>6 groups: <b>octahedral</b> electron geometry.</li>"
      "<li>Shape (atoms only): <b>square pyramidal</b>.</li>"
      "<li><b>Polar</b>: the lone pair breaks the symmetry, so the bond dipoles do not cancel.</li></ol>")

mc("vsepr-8", "vsepr", 2, "Quiz 4 style",
   "SO<sub>2</sub> has AXE notation AX<sub>2</sub>E. What is its shape and approximate bond angle?",
   ["Bent, a bit less than 120&deg;", "Linear, 180&deg;", "Bent, about 90&deg;", "Trigonal planar, 120&deg;"],
   "<p>3 groups = trigonal planar arrangement; one is a lone pair, so the atoms form a bent shape with an angle slightly under 120&deg; (the lone pair squeezes it).</p>")

mc("vsepr-9", "vsepr", 3, "Quiz 4 style",
   "XeF<sub>2</sub> has three lone pairs on Xe. What is its shape?",
   ["Linear", "Bent", "T-shaped", "Trigonal planar"],
   "<p>AX<sub>2</sub>E<sub>3</sub>: 5 groups, trigonal bipyramid. All three lone pairs go in the equatorial plane (120&deg; apart), so the two F are axial: <b>linear</b> (180&deg;). &ldquo;Linear&rdquo; appears twice in the table; tell them apart by group count.</p>")

# ================================================================== HYBMO
topic("hybmo", "Hybridization &amp; molecular orbitals", "unit6", "Quiz 4",
      "Quiz 4 problem 2: draw the H<sub>2</sub> MO diagram (3 pts) and compute bond order (1 pt). "
      "Hybridization recipe: count groups on the centre (atoms + lone pairs): 2 = sp, 3 = sp&sup2;, 4 = sp&sup3;, 5 = sp&sup3;d, 6 = sp&sup3;d&sup2;. Double/triple bonds still count as ONE group. "
      "MO recipe: n AOs make n MOs; fill lowest first; bond order = &frac12;(bonding &minus; antibonding).")

mc("hybmo-1", "hybmo", 1, "Rec 9 style",
   "What is the hybridization of the central atom in NH<sub>3</sub>?",
   ["sp<sup>3</sup>", "sp<sup>2</sup>", "sp", "sp<sup>3</sup>d"],
   "<p>3 N&ndash;H bonds + 1 lone pair = <b>4 groups</b> &rarr; sp<sup>3</sup> (tetrahedral arrangement, trigonal pyramidal shape).</p>")

mc("hybmo-2", "hybmo", 2, "Rec 9 style",
   "What is the hybridization of Se in SeF<sub>4</sub>?",
   ["sp<sup>3</sup>d", "sp<sup>3</sup>", "sp<sup>3</sup>d<sup>2</sup>", "sp<sup>2</sup>"],
   "<p>4 bonds + 1 lone pair = 5 groups &rarr; sp<sup>3</sup>d (see-saw shape).</p>")

mc("hybmo-3", "hybmo", 2, "Rec 9 style",
   "In ethyne (acetylene, HC&equiv;CH), what is the hybridization of each carbon and how many &sigma; and &pi; bonds does the C&equiv;C triple bond contain?",
   ["sp; 1 &sigma; + 2 &pi;", "sp<sup>2</sup>; 2 &sigma; + 1 &pi;", "sp; 3 &sigma;", "sp<sup>3</sup>; 1 &sigma; + 2 &pi;"],
   "<p>Each C has 2 groups (one H, one C) &rarr; sp. The triple bond is one &sigma; (head-on overlap of sp hybrids) plus <b>two &pi;</b> bonds (side-on overlap of the two leftover p orbitals).</p>")

o2p = (8 - 3) / 2
num("hybmo-4", "hybmo", 3, "Rec 9 style",
    "What is the <b>bond order of O<sub>2</sub><sup>+</sup></b>? (O<sub>2</sub> has 12 valence electrons; fill &sigma;2s, &sigma;*2s, &sigma;2p, &pi;2p, &pi;*2p in that order.)",
    o2p, "",
    "<p>O<sub>2</sub><sup>+</sup> has 11 valence electrons: &sigma;2s<sup>2</sup> &sigma;*2s<sup>2</sup> &sigma;2p<sup>2</sup> &pi;2p<sup>4</sup> &pi;*2p<sup>1</sup>. Bonding = 2 + 2 + 4 = 8; antibonding = 2 + 1 = 3. Bond order = &frac12;(8 &minus; 3) = <b>2.5</b>. Removing an antibonding electron from O<sub>2</sub> (BO 2) makes the bond <em>stronger</em> and shorter.</p>",
    tol=0.01, text="2.5")

he2p = (2 - 1) / 2
num("hybmo-5", "hybmo", 2, "Rec 9 style",
    "What is the bond order of He<sub>2</sub><sup>+</sup> (3 electrons)?",
    he2p, "",
    "<p>He<sub>2</sub><sup>+</sup>: &sigma;1s<sup>2</sup> &sigma;*1s<sup>1</sup>. Bond order = &frac12;(2 &minus; 1) = <b>0.5</b>. A weak bond exists. (Neutral He<sub>2</sub> would have BO = &frac12;(2 &minus; 2) = 0: no bond, which is why helium is a monatomic gas.)</p>",
    tol=0.01, text="0.5")

mc("hybmo-6", "hybmo", 2, "Rec 9 style",
   "O<sub>2</sub> has two unpaired electrons. Where are they in the MO diagram?",
   ["One in each of the two degenerate &pi;*2p orbitals (same spin)", "Both in &sigma;2p", "In the &sigma;2s and &sigma;*2s", "Both in one &pi;*2p orbital"],
   "<p>The last two electrons of O<sub>2</sub> go into the two degenerate &pi;* orbitals, one each, with the same spin (Hund&rsquo;s rule). That makes O<sub>2</sub> <b>paramagnetic</b>, which the Lewis structure O=O cannot explain.</p>")

mc("hybmo-7", "hybmo", 3, "Rec 9 style",
   "For which molecule is the &pi;2p level drawn <b>below</b> the &sigma;2p level (the &ldquo;flipped&rdquo; order)?",
   ["N<sub>2</sub>", "O<sub>2</sub>", "F<sub>2</sub>", "Ne<sub>2</sub>"],
   "<p>For the lighter diatomics (B<sub>2</sub>, C<sub>2</sub>, N<sub>2</sub>) the s and p orbitals mix, pushing &sigma;2p above &pi;2p. For O<sub>2</sub> and F<sub>2</sub> the normal order (&sigma;2p below &pi;2p) is used. Rec 9 says: &ldquo;you don&rsquo;t need to know why&rdquo;, only that N<sub>2</sub> flips.</p>")

selfq("hybmo-8", "hybmo", 2, "Quiz 4 style",
      "Draw how the 1s orbitals of two hydrogen atoms form the MOs of H<sub>2</sub>. Label everything, fill in the electrons, and give the bond order (this is 4 points on Quiz 4).",
      "<ol><li>Energy axis. Two H 1s levels, one on the left and one on the right at the same height, each with one electron (&uarr;).</li>"
      "<li>Between them: <b>&sigma;<sub>1s</sub></b> (bonding) <b>below</b> and <b>&sigma;*<sub>1s</sub></b> (antibonding) <b>above</b>. Dashed lines connect each 1s to both MOs. The antibonding one is higher by the same amount the bonding one is lower.</li>"
      "<li>Both electrons go into &sigma;<sub>1s</sub> with opposite spins (&uarr;&darr;). &sigma;*<sub>1s</sub> stays empty.</li>"
      "<li>Bond order = &frac12;(2 &minus; 0) = <b>1</b>: a single bond.</li></ol>"
      "<p>Common mistakes: antibonding below bonding; two electrons with the same spin; forgetting the energy axis or the orbital labels.</p>")

selfq("hybmo-9", "hybmo", 3, "Rec 9 style",
      "<b>Carbon monoxide, CO</b> (10 valence electrons). Outline its MO diagram, find the bond order, and say which atom&rsquo;s orbitals are lower in energy and why. <span class=\"pill\" style=\"--c:var(--unit-orbital);--c-soft:var(--unit-orbital-soft)\">extra</span>",
      "<ol><li><b>Two different atoms:</b> O is more electronegative, so its 2s and 2p levels sit <b>lower</b> than C&rsquo;s. Draw O on one side lower, C on the other side higher (like NO in Rec 9).</li>"
      "<li>Valence electrons: C 4 + O 6 = 10. Fill the MOs bottom to top: &sigma;2s<sup>2</sup> &sigma;*2s<sup>2</sup> &pi;2p<sup>4</sup> &sigma;2p<sup>2</sup> (the &pi;-below-&sigma; order applies, as for N<sub>2</sub>, because CO is isoelectronic with N<sub>2</sub>).</li>"
      "<li>Bonding electrons = 2 + 4 + 2 = 8; antibonding = 2. <b>Bond order = &frac12;(8 &minus; 2) = 3</b>, matching the Lewis triple bond C&equiv;O.</li>"
      "<li>The &pi;*2p and &sigma;*2p levels are empty; the highest filled orbital (HOMO) is the &sigma;2p, which has most of its density on carbon, which is why CO binds to metals through carbon.</li></ol>")
