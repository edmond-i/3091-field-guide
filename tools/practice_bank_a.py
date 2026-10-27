from practice_lib import *
import math

R = 8.314          # J/(mol K)
NA = 6.022e23
HC = 1240.0        # eV nm
RY = 13.6          # eV

# ================================================================== GAS
topic("gas", "Moles, gas law &amp; units", "unit1", "Quiz 1",
      "Quiz 1 starts with a unit-juggling problem. Recipe: (1) write PV = nRT and solve for n; (2) check units "
      "(kPa&middot;L = J, so R = 8.314 J/(mol&middot;K)); (3) convert moles to grams with the molar mass; "
      "(4) a diatomic gas (H<sub>2</sub>, O<sub>2</sub>, N<sub>2</sub>) has TWO atoms per molecule.")

P, V, T = 3000, 20, 290
n = P * V / (R * T)
m = n * 32.00
num("gas-1", "gas", 1, "Quiz 1 style",
    "An oxygen tank holds <b>20 L</b> at <b>3000 kPa</b> and <b>290 K</b>. Assuming the ideal gas law, how many <b>grams</b> of O<sub>2</sub> are in the tank? "
    "(Hint from the real quiz: kPa&middot;L = J.)",
    m, "g",
    "<ol><li>Solve for moles: n = PV/(RT).</li>"
    "<li>Units: 3000 kPa &times; 20 L = 60000 J, which matches R in J/(mol&middot;K). No conversion needed.</li>"
    "<li>n = 60000 / (8.314 &times; 290) = %s mol.</li>"
    "<li>O<sub>2</sub> has molar mass 2 &times; 16.00 = 32.00 g/mol. Mass = %s &times; 32.00 = <b>%s g</b>.</li></ol>"
    "<p class=\"pq-ansline\">Answer: about %s g.</p>"
    "<p><b>Typical slips:</b> using 16 g/mol (forgetting O<sub>2</sub> is two atoms), using &deg;C instead of kelvin, or using R = 0.0821 with kPa.</p>" % (fmt(n, 4), fmt(n, 4), fmt(m, 4), fmt(m, 3)),
    hint="n = PV/RT. What is the molar mass of O<sub>2</sub>, not O?", text="%s g" % fmt(m, 3))

rho, Vm3 = 2.70, 0.040
mass_kg = rho * Vm3 * 1e6 / 1000
num("gas-2", "gas", 1, "Quiz 1 style",
    "Aluminum has density <b>2.70 g/cm&sup3;</b>. What is the mass, in <b>kg</b>, of a block with volume <b>0.040 m&sup3;</b>?",
    mass_kg, "kg",
    "<ol><li>Convert the volume: 1 m = 100 cm, so 1 m&sup3; = 100&sup3; = 10<sup>6</sup> cm&sup3;. (Cube the conversion factor!)</li>"
    "<li>0.040 m&sup3; = 0.040 &times; 10<sup>6</sup> = 4.0&times;10<sup>4</sup> cm&sup3;.</li>"
    "<li>Mass = 2.70 g/cm&sup3; &times; 4.0&times;10<sup>4</sup> cm&sup3; = 1.08&times;10<sup>5</sup> g = <b>%s kg</b>.</li></ol>" % fmt(mass_kg, 4),
    hint="1 m&sup3; is NOT 100 cm&sup3;.", text="%s kg" % fmt(mass_kg, 4))

atoms = 10.0 / 28.09 * NA
num("gas-3", "gas", 1, "Quiz 1 style",
    "How many <b>atoms</b> are in <b>10.0 g</b> of silicon (molar mass 28.09 g/mol)? Give your answer in scientific notation, e.g. 2.1e23.",
    atoms, "atoms",
    "<ol><li>Moles = mass / molar mass = 10.0 / 28.09 = %s mol.</li>"
    "<li>Atoms = moles &times; N<sub>A</sub> = %s &times; 6.022&times;10<sup>23</sup> = <b>%s</b> atoms.</li></ol>" % (fmt(10.0 / 28.09, 4), fmt(10.0 / 28.09, 4), fmt(atoms, 3)),
    hint="grams &rarr; moles &rarr; atoms.", text=fmt(atoms, 3) + " atoms")

ppm = 5e-3 / 2000 * 1e6
num("gas-4", "gas", 1, "Rec 1 style",
    "A 2.0 kg silicon wafer batch is doped with <b>5.0 mg</b> of boron (by mass). What is the dopant concentration in <b>ppm</b> (parts per million, by mass)?",
    ppm, "ppm",
    "<p>ppm = (mass of dopant / total mass) &times; 10<sup>6</sup>. Put both in the same unit first: 5.0 mg = 5.0&times;10<sup>&minus;3</sup> g and 2.0 kg = 2000 g.</p>"
    "<p class=\"mono\">(5.0&times;10<sup>&minus;3</sup> / 2000) &times; 10<sup>6</sup> = <b>%s ppm</b></p>" % fmt(ppm, 3),
    hint="Convert both masses to grams first.", text="%s ppm" % fmt(ppm, 3))

mc("gas-5", "gas", 1, "Quiz 1 style",
   "In the ideal gas law with pressure in <b>kPa</b> and volume in <b>L</b>, which value of R can you use with no unit conversion?",
   ["R = 8.314 J/(mol&middot;K), because 1 kPa&middot;L = 1 J",
    "R = 0.0821 L&middot;atm/(mol&middot;K), because kPa and atm are the same size",
    "R = 8.314 J/(mol&middot;K), but only if the pressure is first converted to Pa and the volume to m&sup3;&hellip; and then multiplied by 1000",
    "R = 1.987 cal/(mol&middot;K), because kPa&middot;L are calories"],
   "<p>1 kPa = 1000 Pa and 1 L = 10<sup>&minus;3</sup> m&sup3;, so 1 kPa&middot;L = 1000 &times; 10<sup>&minus;3</sup> Pa&middot;m&sup3; = 1 J. That is exactly why the quiz gives the hint &ldquo;J = kPa&middot;L&rdquo;.</p>"
   "<p><b>Rule:</b> before plugging in, make sure the units of R cancel the units of P, V and T.</p>",
   hint="Convert 1 kPa&middot;L into SI base units.")

P6 = 2.00 * R * 298.15 / 5.0
num("gas-6", "gas", 2, "Quiz 1 style",
    "<b>2.00 mol</b> of an ideal gas is held in a <b>5.0 L</b> container at <b>25 &deg;C</b>. What is the pressure in <b>kPa</b>?",
    P6, "kPa",
    "<ol><li>Temperature in kelvin: 25 + 273.15 = 298.15 K.</li>"
    "<li>P = nRT/V = (2.00 &times; 8.314 &times; 298.15) / 5.0 L = <b>%s kPa</b> (units: J/L = kPa).</li></ol>" % fmt(P6, 4),
    hint="Never put &deg;C into PV = nRT.", tol=0.02, text="%s kPa" % fmt(P6, 4))

# ================================================================== BOHR
topic("bohr", "Bohr model &amp; photons", "unit1", "Quiz 1",
      "Quiz 1 part 2: a hydrogen-like ion (one electron) jumps between levels. Recipe: (1) identify Z, n<sub>i</sub>, n<sub>f</sub>; "
      "(2) &Delta;E = &minus;13.6 eV &times; Z&sup2; &times; (1/n<sub>f</sub>&sup2; &minus; 1/n<sub>i</sub>&sup2;); (3) negative = emission, take the size for the photon; "
      "(4) &lambda; = 1240 eV&middot;nm / E; (5) visible light is roughly 1.65&ndash;3.1 eV (400&ndash;750 nm).")

dE = RY * 9 * (1 / 4 - 1 / 9)
num("bohr-1", "bohr", 1, "Quiz 1 style",
    "Li<sup>2+</sup> (Z = 3, only one electron left) drops from <b>n = 3 to n = 2</b>. How much energy does the emitted photon carry, in <b>eV</b>? (R = 13.6 eV.)",
    dE, "eV",
    "<ol><li>Identify: Z = 3, n<sub>i</sub> = 3, n<sub>f</sub> = 2.</li>"
    "<li>&Delta;E = &minus;13.6 &times; 3&sup2; &times; (1/2&sup2; &minus; 1/3&sup2;) = &minus;13.6 &times; 9 &times; (0.25 &minus; 0.1111) = &minus;13.6 &times; 9 &times; 0.1389 = &minus;%s eV.</li>"
    "<li>The minus sign means the ion <b>loses</b> energy, so a photon is emitted. The photon carries <b>%s eV</b>.</li></ol>"
    "<p><b>Typical slips:</b> forgetting to square Z (gives 1.89 eV), swapping n<sub>i</sub> and n<sub>f</sub> (flips the sign), or using Z = charge (+2) instead of the atomic number 3.</p>" % (fmt(dE, 4), fmt(dE, 4)),
    hint="Z&sup2; = 9. Compute 1/4 &minus; 1/9 first.", alt=[-dE], text="%s eV" % fmt(dE, 4))

lam = HC / dE
num("bohr-2", "bohr", 2, "Quiz 1 style",
    "What is the <b>wavelength in nm</b> of the photon from the previous question (use hc = 1240 eV&middot;nm)?",
    lam, "nm",
    "<p>&lambda; = hc / E = 1240 eV&middot;nm / %s eV = <b>%s nm</b>. That is extreme ultraviolet.</p>" % (fmt(dE, 4), fmt(lam, 3)),
    hint="High energy means SHORT wavelength.", tol=0.015, text="%s nm" % fmt(lam, 3))

mc("bohr-3", "bohr", 1, "Quiz 1 style",
   "A transition emits a photon of <b>17 eV</b>. Could you see it with an optical spectrometer (visible light is about 1.65&ndash;3.1 eV)?",
   ["No. It is far above the visible range (ultraviolet or beyond, about 73 nm).",
    "Yes. Any emission from an atom is visible.",
    "No. It is below the visible range, in the infrared.",
    "Yes. Higher energy means a longer wavelength, which is easier to see."],
   "<p>&lambda; = 1240/17 &asymp; 73 nm, well below the 400 nm violet end of the visible range, so it is <b>ultraviolet</b>. High energy &harr; short wavelength.</p>",
   hint="Convert to nm: 1240 / E.",
   whys={2: "Infrared photons have LOW energy (below ~1.65 eV).", 3: "High energy means short wavelength, not long."})

n4 = RY * (1 / 4 - 1 / 16)
l4 = HC / n4
num("bohr-4", "bohr", 2, "Rec 2/3 style",
    "In hydrogen, an electron falls from <b>n = 4 to n = 2</b> (a Balmer line). What is the <b>wavelength in nm</b> of the emitted light?",
    l4, "nm",
    "<ol><li>Z = 1: E = 13.6 &times; (1/4 &minus; 1/16) = 13.6 &times; 0.1875 = %s eV.</li><li>&lambda; = 1240 / %s = <b>%s nm</b>, blue-green visible light.</li></ol>" % (fmt(n4, 4), fmt(n4, 4), fmt(l4, 4)),
    tol=0.015, text="%s nm" % fmt(l4, 4))

ie = RY * 4
num("bohr-5", "bohr", 1, "Rec 3 style",
    "What is the ionization energy of He<sup>+</sup> (Z = 2, one electron) from its ground state, in <b>eV</b>? (Ionization means n = 1 &rarr; n = &infin;.)",
    ie, "eV",
    "<p>Z&sup2; = 4 and 1/n<sub>f</sub>&sup2; &minus; 1/n<sub>i</sub>&sup2; with n = 1 &rarr; &infin; is 1 &minus; 0 = 1 in size, so E = 13.6 &times; 4 = <b>%s eV</b>. Compare hydrogen, 13.6 eV: the doubled nuclear charge holds the electron 4&times; tighter.</p>" % fmt(ie, 3),
    text="%s eV" % fmt(ie, 3))

mc("bohr-6", "bohr", 1, "Quiz 1 style",
   "In hydrogen, which transition emits the highest-energy photon?",
   ["n = 2 &rarr; n = 1", "n = 3 &rarr; n = 2", "n = 4 &rarr; n = 2", "n = 5 &rarr; n = 4"],
   "<p>E &prop; (1/n<sub>f</sub>&sup2; &minus; 1/n<sub>i</sub>&sup2;): 2&rarr;1 gives 0.75, 3&rarr;2 gives 0.139, 4&rarr;2 gives 0.188, 5&rarr;4 gives 0.0306. The biggest drop is into the lowest level.</p>",
   hint="Compute 1/n<sub>f</sub>&sup2; &minus; 1/n<sub>i</sub>&sup2; for each.")

nu = 3.00e8 / 500e-9
Eev = HC / 500
num("bohr-7", "bohr", 2, "Rec 2 style",
    "Green light has wavelength <b>500 nm</b>. What is the photon energy in <b>eV</b>? (Also try: its frequency is &nu; = c/&lambda; = %s Hz.)" % fmt(nu, 2),
    Eev, "eV",
    "<p>E = hc/&lambda; = 1240 eV&middot;nm / 500 nm = <b>%s eV</b>. Check with frequency: E = h&nu; = 4.136&times;10<sup>&minus;15</sup> eV&middot;s &times; %s Hz = %s eV.</p>" % (fmt(Eev, 3), fmt(nu, 2), fmt(4.136e-15 * nu, 3)),
    text="%s eV" % fmt(Eev, 3))

# ================================================================== CONFIG
topic("config", "Electron configurations &amp; quantum numbers", "unit2", "Quiz 2",
      "Quiz 2 asks you to (a) write a configuration, (b) draw the box diagram, (c) give the four quantum numbers for the boxed electrons, (d) pick a cation charge. "
      "Recipe: fill 1s 2s 2p 3s 3p <b>4s 3d</b> 4p; spread electrons one per box before pairing (Hund); quantum numbers (n, l, m<sub>l</sub>, m<sub>s</sub>) with l = 0,1,2,3 for s,p,d,f, "
      "m<sub>l</sub> from &minus;l to +l, m<sub>s</sub> = &plusmn;&frac12;; cations lose <b>4s before 3d</b>.")

mc("config-1", "config", 1, "Quiz 2 style",
   "What is the ground-state electron configuration of iron (Z = 26)?",
   ["[Ar] 3d<sup>6</sup> 4s<sup>2</sup>", "[Ar] 3d<sup>8</sup>", "[Ar] 3d<sup>4</sup> 4s<sup>2</sup>", "[Ar] 4s<sup>2</sup> 3d<sup>4</sup> 4p<sup>2</sup>"],
   "<p>[Ar] has 18 electrons, so iron needs 8 more: 4s fills first (2), then 6 go into 3d. <b>[Ar] 3d<sup>6</sup> 4s<sup>2</sup></b>.</p>",
   hint="26 &minus; 18 = 8 electrons after the argon core.")

num("config-2", "config", 1, "Quiz 2 style",
    "How many <b>unpaired</b> electrons does a ground-state iron atom have? (Think of the five 3d boxes.)",
    4, "unpaired",
    "<p>3d<sup>6</sup>: put one arrow in each of the 5 boxes first (Hund&rsquo;s rule), then the 6th electron pairs with one of them. That leaves 5 &minus; 1 = <b>4</b> boxes with a single arrow. (The 4s<sup>2</sup> pair is full.)</p>",
    tol=0.0, atol=0.01, text="4")

mc("config-3", "config", 2, "Quiz 2 style",
   "Which set of quantum numbers (n, l, m<sub>l</sub>, m<sub>s</sub>) is <b>allowed</b>?",
   ["(3, 2, &minus;2, +&frac12;)", "(2, 2, 0, +&frac12;)", "(3, 1, 2, &minus;&frac12;)", "(4, 3, 0, +1)"],
   "<ul><li>(3, 2, &minus;2, +&frac12;): l = 2 &lt; n = 3 &#10003;, |m<sub>l</sub>| = 2 &le; l &#10003;, spin &plusmn;&frac12; &#10003;. <b>Allowed (a 3d electron).</b></li>"
   "<li>(2, 2, 0, +&frac12;): l must be less than n (max l = n &minus; 1 = 1). &#10007;</li>"
   "<li>(3, 1, 2, &minus;&frac12;): m<sub>l</sub> must lie between &minus;l and +l = &minus;1..+1. &#10007;</li>"
   "<li>(4, 3, 0, +1): spin is only &plusmn;&frac12;. &#10007;</li></ul>",
   hint="Check each rule: l &lt; n, |m<sub>l</sub>| &le; l, m<sub>s</sub> = &plusmn;&frac12;.")

mc("config-4", "config", 2, "Quiz 2 style",
   "Which of these ions has a <b>half-filled</b> 3d subshell (3d<sup>5</sup>)?",
   ["Fe<sup>3+</sup>", "Fe<sup>2+</sup>", "Co<sup>2+</sup>", "Zn<sup>2+</sup>"],
   "<p>Cations lose 4s electrons first. Fe is [Ar]3d<sup>6</sup>4s<sup>2</sup>: Fe<sup>2+</sup> = [Ar]3d<sup>6</sup>; Fe<sup>3+</sup> loses one more (from 3d) = <b>[Ar]3d<sup>5</sup></b>. Co<sup>2+</sup> is 3d<sup>7</sup>; Zn<sup>2+</sup> is 3d<sup>10</sup>.</p>"
   "<p><b>Watch out:</b> the real Quiz 2 answer key justified Co<sup>2+</sup> with &ldquo;half-full 3d&rdquo;, but Co<sup>2+</sup> is 3d<sup>7</sup>. The +2 charge is right (lose both 4s electrons); the stated reason is not.</p>",
   hint="Remove 4s electrons first, then 3d.")

selfq("config-5", "config", 2, "Quiz 2 style",
      "For <b>nickel (Z = 28)</b>: (a) write the configuration; (b) sketch the box diagram of 3d and 4s; (c) give the four quantum numbers for the <b>unpaired</b> 3d electrons; (d) is Ni more likely +1 or +2, and why?",
      "<ol><li><b>[Ar] 3d<sup>8</sup> 4s<sup>2</sup></b> (18 + 2 + 8 = 28).</li>"
      "<li>4s: &uarr;&darr;. 3d (five boxes): &uarr;&darr; &uarr;&darr; &uarr;&darr; &uarr; &uarr; (3 boxes paired, 2 boxes with one arrow, total 8).</li>"
      "<li>Two unpaired electrons, both n = 3, l = 2, <b>different</b> m<sub>l</sub> (two of &minus;2..+2), both with the same spin m<sub>s</sub> = +&frac12; (Hund). e.g. (3, 2, 1, +&frac12;) and (3, 2, 2, +&frac12;).</li>"
      "<li><b>+2</b>: the two 4s electrons (the outermost) are lost first, giving [Ar]3d<sup>8</sup>. A +1 ion would have to keep a lone 4s electron, which is not a stable arrangement.</li></ol>",
      hint="Hund: one arrow per box first.")

mc("config-6", "config", 1, "Quiz 2 style",
   "When a transition metal such as Mn becomes a cation, which electrons are removed first?",
   ["The 4s electrons (outermost shell), before any 3d", "The 3d electrons, because they have the highest energy once the atom is built", "Electrons are removed at random from 4s and 3d", "The 1s electrons, because they are the closest to the nucleus"],
   "<p>Fill order and ionization order are different: 4s fills first but it is the <b>outermost</b> shell (n = 4), so it is the first to go. Mn<sup>2+</sup> = [Ar]3d<sup>5</sup>.</p>")

cl_p = 6 + 5
num("config-7", "config", 2, "Quiz 2 style",
    "How many electrons in a ground-state chlorine atom (Z = 17) have <b>l = 1</b>?",
    cl_p, "electrons",
    "<p>Cl: 1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>5</sup>. l = 1 means p electrons: 2p has 6 and 3p has 5, total <b>11</b>.</p>",
    tol=0.0, atol=0.01, text="11")

mc("config-8", "config", 2, "Quiz 2 style",
   "Chromium is [Ar]3d<sup>5</sup>4s<sup>1</sup>, not [Ar]3d<sup>4</sup>4s<sup>2</sup>. What is the usual explanation?",
   ["A half-filled d subshell plus a half-filled s subshell is extra stable, so one 4s electron moves to 3d",
    "4s is higher in energy than 3d in every atom",
    "Chromium has 5 valence electrons, so it must use five d orbitals",
    "The Pauli exclusion principle forbids two electrons in 4s"],
   "<p>Cr and Cu are the classic exceptions: half-filled (Cr, 3d<sup>5</sup>4s<sup>1</sup>) or filled (Cu, 3d<sup>10</sup>4s<sup>1</sup>) d subshells are especially stable. The exam asks you to derive configurations from the periodic table, so know these two as exceptions.</p>")

selfq("config-9", "config", 2, "Quiz 2 style",
      "Is <b>Zn</b> more likely to form a +1 or a +2 cation? Write the configuration of the ion you choose and give the reason in one sentence.",
      "<p>Zn = [Ar]3d<sup>10</sup>4s<sup>2</sup>. <b>+2</b>: removing both 4s electrons leaves <b>[Ar]3d<sup>10</sup></b>, a full, stable d subshell. A +1 ion would keep a lone 4s electron, which is easy to lose as well, so it is not stable.</p>")

# ================================================================== TRENDS
topic("trends", "Periodic trends &amp; PES", "unit2", "Quiz 2",
      "Quiz 2 part 2 gives three points for three arrows: <b>electronegativity and ionization energy increase up and to the right; atomic radius is the opposite</b> (increases down and to the left). "
      "Know the exceptions (Be &gt; B, N &gt; O), the isoelectronic rule (more protons = smaller), and how to read PES (position = binding energy, height = number of electrons).")

mc("trends-1", "trends", 1, "Quiz 2 style",
   "Which atom is the <b>largest</b>: Na, Mg, Al or Si?",
   ["Na", "Mg", "Al", "Si"],
   "<p>Same period, so the electrons are in the same shell but the nuclear charge grows from Na (+11) to Si (+14). More pull = smaller. <b>Na</b> is largest.</p>")

mc("trends-2", "trends", 2, "Quiz 2 style",
   "Which has the <b>higher first ionization energy</b>, Be or B?",
   ["Be: its 2s<sup>2</sup> electrons are in a full subshell, harder to remove than B&rsquo;s lone 2p electron", "B: it has more protons, so it always has the higher IE", "They are equal because they are neighbours", "B: its electron is closer to the nucleus"],
   "<p>This is one of the exceptions to &ldquo;IE increases left to right&rdquo;. Be = 2s<sup>2</sup>; B = 2s<sup>2</sup>2p<sup>1</sup>. The 2p electron sits higher in energy and is shielded by the 2s pair, so it comes off more easily. <b>Be &gt; B</b>. (Same story for N &gt; O.)</p>",
   whys={1: "More protons usually wins, but here a new subshell (2p) starts, which breaks the pattern."})

mc("trends-3", "trends", 1, "Quiz 2 style",
   "Which element has the <b>highest electronegativity</b>: S, Se, Cl or Br?",
   ["Cl", "S", "Se", "Br"],
   "<p>Electronegativity rises to the right and <b>up</b>. Cl is right of S and above Br, so Cl is the winner.</p>")

mc("trends-4", "trends", 2, "Quiz 2 style",
   "Which of these isoelectronic species (all 10 electrons) has the <b>largest radius</b>: O<sup>2&minus;</sup>, F<sup>&minus;</sup>, Na<sup>+</sup>, Mg<sup>2+</sup>?",
   ["O<sup>2&minus;</sup>", "F<sup>&minus;</sup>", "Na<sup>+</sup>", "Mg<sup>2+</sup>"],
   "<p>Same number of electrons, so the one with the <b>fewest protons</b> pulls least: O<sup>2&minus;</sup> (8 p) &gt; F<sup>&minus;</sup> (9) &gt; Na<sup>+</sup> (11) &gt; Mg<sup>2+</sup> (12).</p>")

mc("trends-5", "trends", 3, "Rec 4 style",
   "A PES spectrum of a neutral atom shows five peaks with relative heights 2 : 2 : 6 : 2 : 1 (the 1s, 2s, 2p, 3s and 3p electrons). Which element is it?",
   ["Aluminum (Al)", "Magnesium (Mg)", "Silicon (Si)", "Sodium (Na)"],
   "<p>Peak heights = number of electrons in each subshell: 1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>1</sup> = 13 electrons = <b>Al</b>.</p>")

mc("trends-6", "trends", 2, "Quiz 2 style",
   "Which has the higher first ionization energy, nitrogen or oxygen?",
   ["Nitrogen: its half-filled 2p<sup>3</sup> is extra stable", "Oxygen: more protons", "They are the same", "Oxygen: its 2p electrons are all unpaired"],
   "<p>O is 2p<sup>4</sup>: one of its p electrons is <b>paired</b>, and the pair repels, so that electron is easier to remove. N (2p<sup>3</sup>, one electron in each box) is more stable: <b>N &gt; O</b>.</p>")

selfq("trends-7", "trends", 1, "Quiz 2 style",
      "On a blank periodic table, draw the direction of the arrow(s) for (i) electronegativity, (ii) ionization energy, (iii) atomic radius, and give a one-sentence reason for each (the real quiz gives 1 point each).",
      "<ul><li><b>Electronegativity:</b> increases to the <b>right</b> and <b>up</b>. Reason: more protons across a period with the same shell; fewer shells up a group, so the pull is stronger.</li>"
      "<li><b>Ionization energy:</b> same directions as electronegativity (right and up). Reason: a tighter-held electron costs more energy to remove.</li>"
      "<li><b>Atomic radius:</b> the <b>opposite</b>: increases to the <b>left</b> and <b>down</b>. Reason: more shells down a group; weaker pull to the left.</li></ul>"
      "<p>You need two arrows per trend: one along a period (&rarr;/&larr;) and one down a group (&uarr;/&darr;).</p>")

mc("trends-8", "trends", 3, "Rec 4 style",
   "The successive ionization energies of an element are (kJ/mol) 738, 1451, 7733, 10543. Which group is it in?",
   ["Group 2 (two valence electrons)", "Group 1", "Group 13", "Group 14"],
   "<p>There is a huge jump (1451 &rarr; 7733) after the <b>second</b> electron: the third electron comes from a stable inner shell. Two easy electrons = group 2 (this is Mg).</p>")
