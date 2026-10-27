from practice_lib import *
import math

R = 8.314

# ================================================================== DEFECTS
topic("defects", "Defects, glass &amp; polymers", "unit10", "Quiz 6",
      "Quiz 6 parts 4&ndash;5: interstitial or substitutional? Does hammering make a metal harder or softer? Recipe: <b>small</b> atom (C, H, N) in a metal &rarr; interstitial; "
      "<b>similar-size</b> atom (Zn in Cu) &rarr; substitutional; moving/tangled dislocations &rarr; plastic deformation / work hardening; "
      "no long-range order = amorphous; network modifiers (Na, Ca) break the silica network; crosslinks stop a polymer from melting.")

mc("defects-1", "defects", 1, "Quiz 6 style",
   "Carbon (radius about 0.77 &Aring;) is added to iron (radius about 1.24 &Aring;) to make steel. Does the carbon form a <b>substitutional</b> or an <b>interstitial</b> defect?",
   ["Interstitial: the small C atoms fit in the gaps between Fe atoms", "Substitutional: C takes the place of an Fe atom", "A vacancy", "A Schottky pair"],
   "<p>C is much smaller than Fe, so it sits in the holes between iron atoms (carbon steel = interstitial alloy). Substitutional alloys need atoms of similar size, like Zn in Cu (brass).</p>")

mc("defects-2", "defects", 1, "L18 slide 9",
   "Brass is made by replacing some Cu atoms in the lattice with Zn atoms. This is a&hellip;",
   ["substitutional point defect (substitutional alloy)", "interstitial point defect", "line defect", "Frenkel defect"],
   "<p>The foreign atom sits <b>on a lattice site</b> where a host atom would be: substitutional. Same idea as P in Si (a dopant is a substitutional point defect).</p>")

mc("defects-3", "defects", 2, "L18 slide 8",
   "Which statement is correct about <b>Schottky</b> and <b>Frenkel</b> defects in an ionic crystal?",
   ["Schottky = a missing cation + a missing anion (vacancy pair); Frenkel = a cation moves into a gap, leaving a vacancy", "Schottky = an extra atom in a gap; Frenkel = a missing pair", "Both are line defects", "Both involve foreign atoms"],
   "<p>Both keep the crystal electrically neutral. Schottky: two vacancies (+ and &minus;), the ions leave. Frenkel: a vacancy + an interstitial of the <em>same</em> ion (usually the small cation).</p>")

mc("defects-4", "defects", 1, "Quiz 6 style",
   "A block of low-carbon steel is hammered extensively into a new shape. Compared with before, it is&hellip;",
   ["Harder: hammering creates many dislocations that tangle and block each other (work hardening)", "Softer: hammering removes defects", "Unchanged", "Softer: hammering anneals it"],
   "<p>Plastic deformation multiplies dislocations; tangled dislocations cannot move easily, so further deformation needs more stress: <b>work (strain) hardening</b>. Annealing (heating) is what softens a metal again. L18 slide 16: &ldquo;Cold worked Ti&rdquo; shows the tangles.</p>")

mc("defects-5", "defects", 2, "L18 slide 15",
   "Why can a metal deform plastically at stresses 1000&ndash;10 000 times <b>lower</b> than the theoretical strength of a perfect crystal?",
   ["Dislocations glide one atom row at a time along slip planes, so only a few bonds break at once", "All the bonds across a plane break together", "The atoms vaporize", "Metals have no bonds"],
   "<p>Slide 15&rsquo;s cartoon: dragging a whole rug (all bonds at once) vs. pushing a wrinkle along it. A dislocation is the wrinkle: moving it only requires breaking and re-making bonds along one row.</p>")

mc("defects-6", "defects", 2, "L19 slide 9",
   "What happens when Na<sub>2</sub>O and CaO are added to silica (SiO<sub>2</sub>)?",
   ["Non-bridging oxygens form, the network breaks up, and the softening temperature drops (soda-lime glass)", "The silica becomes crystalline", "Si&ndash;O bonds become ionic and the glass gets harder", "The tetrahedra turn into octahedra"],
   "<p>Na<sup>+</sup> and Ca<sup>2+</sup> are <b>network modifiers</b>: each supplies an O that bonds to only one Si (non-bridging oxygen). Fewer links between tetrahedra &rarr; the glass softens at a much lower temperature (soda-lime is the leftmost curve on the viscosity plot) and is easy to work.</p>")

mc("defects-7", "defects", 1, "L19 slide 4",
   "Quartz and silica glass are both SiO<sub>2</sub>. What is the difference?",
   ["Both are SiO<sub>4</sub> tetrahedra sharing corners, but quartz repeats periodically and glass does not", "Quartz has different atoms", "Glass has no Si&ndash;O bonds", "Quartz has no oxygen bridges"],
   "<p>Same building block and same local bonding (Si&ndash;O 162 pm, O&ndash;Si&ndash;O 109.5&deg;); crystal = periodic, glass = random ring sizes, no long-range order (but the local tetrahedron is preserved). Amorphous solids form when the structure packs badly or is cooled quickly.</p>")

mc("defects-8", "defects", 1, "L19 slide 12&ndash;13",
   "Why can an ordinary (non-crosslinked) plastic bottle be melted and recycled but a vulcanized rubber tyre cannot?",
   ["In the tyre the chains are chemically crosslinked (by sulfur) into one network, so it does not melt", "Rubber has stronger covalent bonds inside each chain", "Plastics are ionic", "Rubber is crystalline"],
   "<p>Vulcanization links the chains with sulfur bridges into a 3D network. You cannot melt a network without breaking covalent bonds. Chains that are only entangled (HDPE, PET) slide past each other when heated.</p>")

mc("defects-9", "defects", 2, "L19 slide 10",
   "On the viscosity vs temperature plot, which glass reaches the <b>working viscosity at the lowest temperature</b>?",
   ["Soda-lime glass", "Fused silica", "96% silica glass", "Borosilicate glass"],
   "<p>Soda-lime (lots of network modifiers) is the leftmost curve; fused silica (pure SiO<sub>2</sub> network) is the rightmost, needing the highest temperature. Viscosity falls smoothly by many orders of magnitude: a glass has no sharp melting point.</p>")

mc("defects-10", "defects", 2, "L18 slide 12",
   "Which statement about doping silicon is correct?",
   ["Ga (group 13) makes p-type; its acceptor level sits just above the valence band", "Ga makes n-type", "P (group 15) makes p-type", "P adds an acceptor level just above the valence band"],
   "<p>Dopants are substitutional point defects. Group 15 (P) has an extra electron &rarr; donor level just below the conduction band &rarr; n-type. Group 13 (Ga) is one electron short &rarr; acceptor level just above the valence band &rarr; p-type.</p>")

selfq("defects-11", "defects", 2, "L18 slide 17",
      "Explain in 2&ndash;3 sentences why (a) 18-carat gold is harder than pure gold and (b) a hammered (wrought) steel is harder than the same steel before.",
      "<p><b>(a)</b> 18-carat gold has 25% Cu + Ag atoms in the gold lattice (substitutional point defects). These atoms differ slightly in size and make it harder for dislocations to glide past, so the alloy is harder (and stronger) than pure, soft gold.</p>"
      "<p><b>(b)</b> Hammering creates many new dislocations; they tangle and block each other&rsquo;s motion (work hardening), so it takes more stress to deform further.</p>"
      "<p>Same idea behind both: <b>anything that blocks dislocation motion makes a metal harder.</b> (Pure iron vs steel: carbon atoms are interstitial defects doing the same job.)</p>")

mc("defects-12", "defects", 1, "L19 slide 3",
   "How does a <b>polycrystalline</b> solid differ from a single crystal?",
   ["It is made of many small crystals (grains) with different orientations, separated by boundaries", "It has no order at all", "It is a liquid", "It has only one type of atom"],
   "<p>Inside each grain the atoms are perfectly ordered; neighbouring grains are rotated relative to each other (a grain boundary is a planar defect). Amorphous = no periodic order anywhere.</p>")

mc("defects-13", "defects", 1, "L18",
   "Classify: (i) a vacancy, (ii) an edge dislocation, (iii) a grain boundary.",
   ["point, line, planar", "line, point, planar", "planar, line, point", "point, point, line"],
   "<p>Defects are classified by dimensionality (L20 concept map): <b>point</b> (0-D: vacancy, interstitial, substitutional), <b>line</b> (1-D: dislocation), <b>planar</b> (2-D: grain boundary).</p>")

mc("defects-14", "defects", 2, "L19 slide 15",
   "High-density polyethylene (HDPE) is called <b>semicrystalline</b>. What does that mean?",
   ["It contains ordered crystalline regions (aligned/folded chains) mixed with disordered amorphous regions", "Half the atoms are carbon, half are hydrogen", "It is fully crystalline", "It is fully amorphous"],
   "<p>Polymer chains are long and tangled, so they cannot all line up; real HDPE has small regions where chains pack periodically (unit cell about 0.741 &times; 0.494 &times; 0.255 nm) inside an amorphous tangle.</p>")

# ================================================================== DIFFUSION
topic("diffusion", "Diffusion (L20)", "unit11", "Quiz 6+",
      "Diffusion = particles moving from high to low concentration. <b>Fick&rsquo;s first law: J = &minus;D dC/dx</b>. "
      "D depends on temperature through the Arrhenius form <b>D = D<sub>0</sub> exp(&minus;Q/RT)</b>; on a plot of log D vs 1/T it is a straight line with slope &minus;Q/R. "
      "How far atoms get in time t is about &radic;(Dt). <span class=\"pill\" style=\"--c:var(--ink-soft);--c-soft:var(--line-soft)\">extra</span> The L20 slides print only the first law, the log D plot and the concept map; the Arrhenius form, Fick&rsquo;s second law and &radic;(Dt) were blank or spoken in lecture, so check your own lecture notes for the exact forms.")

mc("diffusion-1", "diffusion", 1, "L20 concept map",
   "Fick&rsquo;s first law is J = &minus;D dC/dx. What does the <b>minus sign</b> mean?",
   ["Net flux goes from high concentration to low concentration (down the gradient)", "Diffusion removes mass", "D is negative", "J always points toward higher concentration"],
   "<p>dC/dx is negative when concentration falls with distance; the minus sign makes J positive in that direction. The concept map: &ldquo;Particles move from high concentration to low concentration areas.&rdquo;</p>")

Q = 140e3
ratio = math.exp(Q / R * (1 / 1000 - 1 / 1100))
num("diffusion-2", "diffusion", 3, "Arrhenius &middot; extra",
    "A solid has activation energy Q = 140 kJ/mol for diffusion. By what factor does D increase when the temperature rises from <b>1000 K to 1100 K</b>? (R = 8.314 J/(mol&middot;K); D = D<sub>0</sub>exp(&minus;Q/RT).)",
    ratio, "&times;",
    "<ol><li>D<sub>2</sub>/D<sub>1</sub> = exp[(Q/R)(1/T<sub>1</sub> &minus; 1/T<sub>2</sub>)] (D<sub>0</sub> cancels).</li>"
    "<li>Q/R = 140000 / 8.314 = %s K. 1/1000 &minus; 1/1100 = 9.09&times;10<sup>&minus;5</sup> K<sup>&minus;1</sup>.</li>"
    "<li>Exponent = %s; D<sub>2</sub>/D<sub>1</sub> = e<sup>%s</sup> = <b>%s</b>. A 10%% rise in T makes diffusion over 4&times; faster.</li></ol>" % (fmt(Q / R, 4), fmt(Q / R * (1 / 1000 - 1 / 1100), 4), fmt(Q / R * (1 / 1000 - 1 / 1100), 4), fmt(ratio, 3)),
    hint="Use Q in J/mol, because R is in J/(mol&middot;K).", tol=0.02, text="%s&times;" % fmt(ratio, 3))

D = 2.0e-7
t = 3600
x = math.sqrt(D * t) * 10  # cm -> mm
num("diffusion-3", "diffusion", 2, "L20 slide 8 &middot; extra",
    "Carbon diffuses into iron with D = 2.0&times;10<sup>&minus;7</sup> cm&sup2;/s. Estimate the characteristic distance &radic;(Dt) after <b>1 hour</b>, in <b>mm</b>.",
    x, "mm",
    "<ol><li>t = 3600 s. Dt = 2.0&times;10<sup>&minus;7</sup> &times; 3600 = 7.2&times;10<sup>&minus;4</sup> cm&sup2;.</li>"
    "<li>&radic;(Dt) = %s cm = <b>%s mm</b> (1 cm = 10 mm).</li></ol>"
    "<p>Because of the square root, 4&times; longer only doubles the depth. (L20 slide 8 leaves the &ldquo;characteristic distance&rdquo; formula blank; &radic;(Dt) is the standard form.)</p>" % (fmt(math.sqrt(D * t), 3), fmt(x, 3)),
    tol=0.02, text="%s mm" % fmt(x, 3))

mc("diffusion-4", "diffusion", 2, "L20 slide 5",
   "At the same temperature in iron, which diffuses <b>faster</b>?",
   ["C (interstitial), D about 10<sup>&minus;7</sup>&ndash;10<sup>&minus;6</sup> cm&sup2;/s", "Fe self-diffusion, D about 10<sup>&minus;12</sup> cm&sup2;/s", "They are about equal", "Fe, because it is bigger"],
   "<p>The L20 plot: H and C in iron sit far above Fe in Fe by 4&ndash;8 orders of magnitude. Small interstitial atoms hop between holes (low activation energy); Fe atoms need a neighbouring vacancy to move (self-diffusion, high Q).</p>")

mc("diffusion-5", "diffusion", 2, "L20 slide 5",
   "On a plot of log D against 1000/T, line A is <b>steeper</b> than line B. Which is true?",
   ["A has the larger activation energy", "A has the smaller activation energy", "A diffuses faster at every temperature", "The lines must be the same Q"],
   "<p>Slope = &minus;Q/R. A steeper (more negative) slope means a larger Q: D changes more with temperature. Steeper does not mean faster at every T: the lines can cross. In the plot, 1000/T grows to the right, so hot is on the left.</p>")

D1, D2 = 2.0e-14, 4.0e-12
T1, T2 = 800, 1000
Qcalc = R * math.log(D2 / D1) / (1 / T1 - 1 / T2) / 1000
num("diffusion-6", "diffusion", 3, "Arrhenius &middot; extra",
    "A diffusion coefficient is measured as 2.0&times;10<sup>&minus;14</sup> cm&sup2;/s at 800 K and 4.0&times;10<sup>&minus;12</sup> cm&sup2;/s at 1000 K. Find the activation energy Q in <b>kJ/mol</b>.",
    Qcalc, "kJ/mol",
    "<ol><li>From D = D<sub>0</sub>e<sup>&minus;Q/RT</sup>: ln(D<sub>2</sub>/D<sub>1</sub>) = (Q/R)(1/T<sub>1</sub> &minus; 1/T<sub>2</sub>).</li>"
    "<li>D<sub>2</sub>/D<sub>1</sub> = 200, ln 200 = %s. 1/800 &minus; 1/1000 = 2.5&times;10<sup>&minus;4</sup>.</li>"
    "<li>Q = 8.314 &times; %s / 2.5&times;10<sup>&minus;4</sup> = %s J/mol = <b>%s kJ/mol</b>.</li></ol>" % (fmt(math.log(200), 4), fmt(math.log(200), 4), fmt(Qcalc * 1000, 4), fmt(Qcalc, 3)),
    hint="Same as reading the slope of ln D vs 1/T between two points.", tol=0.03, text="%s kJ/mol" % fmt(Qcalc, 3))

mc("diffusion-7", "diffusion", 2, "L20 slide 7",
   "When do you need <b>Fick&rsquo;s second law</b> instead of the steady-state first law?",
   ["When the concentration at a point changes with time (non-steady-state diffusion)", "When the temperature is constant", "When D = 0", "Only for gases"],
   "<p>Steady state: the profile does not change, flux is the same everywhere (first law). Non-steady-state: flux in at x differs from flux out at x + dx, so the concentration builds up or drains with time. The second law (&part;C/&part;t = D &part;&sup2;C/&part;x&sup2;, <span class=\"pill\" style=\"--c:var(--ink-soft);--c-soft:var(--line-soft)\">extra</span> not printed on the slide) relates that change to D.</p>")

mc("diffusion-8", "diffusion", 1, "L20 slide 6",
   "The activation energy for self-diffusion Q<sub>v</sub> of FCC metals rises with melting point. Which order is right (smallest to largest Q<sub>v</sub>)?",
   ["Pb &lt; Al &lt; Cu &lt; Fe", "Fe &lt; Cu &lt; Al &lt; Pb", "Al &lt; Pb &lt; Fe &lt; Cu", "They are all the same"],
   "<p>Stronger bonding (higher melting point) means more energy needed to open a vacancy and hop in: Pb (327 &deg;C) &asymp; 25 000 cal/mol, Al &asymp; 33 000, Cu &asymp; 50 000, Fe (1538 &deg;C) &asymp; 68 000 (read from the slide plot, approximate).</p>")

Dd, dC = 3.0e-8, (5.0e20 - 1.0e20) / 0.2
J = Dd * dC
num("diffusion-9", "diffusion", 2, "L20 slide 11",
    "Atoms diffuse through a thin plate. The concentration is 5.0&times;10<sup>20</sup> atoms/cm&sup3; on one side and 1.0&times;10<sup>20</sup> on the other, 0.20 cm apart, and D = 3.0&times;10<sup>&minus;8</sup> cm&sup2;/s. Find the steady-state flux |J| in atoms/(cm&sup2;&middot;s).",
    J, "atoms/(cm&sup2;&middot;s)",
    "<ol><li>|dC/dx| = (5.0&times;10<sup>20</sup> &minus; 1.0&times;10<sup>20</sup>) / 0.20 cm = 2.0&times;10<sup>21</sup> atoms/cm&sup4;.</li>"
    "<li>|J| = D |dC/dx| = 3.0&times;10<sup>&minus;8</sup> &times; 2.0&times;10<sup>21</sup> = <b>%s atoms/(cm&sup2;&middot;s)</b>, flowing from the high side to the low side.</li></ol>" % fmt(J, 3),
    tol=0.02, text="%s" % fmt(J, 3))

selfq("diffusion-10", "diffusion", 2, "L20 slide 5&ndash;6",
      "L20 asks: &ldquo;What do we mean by Fe diffusing in Fe?&rdquo; and &ldquo;Do you think interstitial diffusion has a higher or lower activation energy than this?&rdquo; Answer both.",
      "<p><b>Self-diffusion:</b> the atoms of a pure crystal are identical, but they still move. Imagine a few Fe atoms labelled with a different isotope: over time they spread through the lattice. The mechanism is by <b>vacancies</b>: an atom jumps into a neighbouring empty site. That requires (1) a vacancy to exist and (2) energy to push through the gap, so Q is large (Q<sub>v</sub> rising with melting point: Fe is about 68 000 cal/mol).</p>"
      "<p><b>Interstitial diffusion</b> (C or H in Fe) needs no vacancy: the small atom hops between holes. The activation energy is <b>lower</b>, which is why those lines on the L20 plot are shallower and sit orders of magnitude above self-diffusion.</p>")
