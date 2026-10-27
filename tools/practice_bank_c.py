from practice_lib import *
import math

R = 8.314
NA = 6.022e23
HC = 1240.0
OV = lambda s: '<span style="text-decoration:overline">%s</span>' % s   # overbar = negative index

# ================================================================== IMF
topic("imf", "Intermolecular forces &amp; boiling points", "unit7", "Quiz 4",
      "Quiz 4 problem 3: &ldquo;strongest intermolecular force for each of these molecules?&rdquo; (1 point each). Decision path: "
      "<b>(1)</b> ions? ion&ndash;ion / ion&ndash;dipole. <b>(2)</b> H on N, O or F plus a lone pair on N/O/F nearby? hydrogen bonding. <b>(3)</b> polar shape (draw it!)? dipole&ndash;dipole. <b>(4)</b> otherwise dispersion (bigger = stronger). "
      "Intermolecular means BETWEEN molecules, never the covalent bonds inside.")

mc("imf-1", "imf", 1, "Quiz 4 style",
   "What is the strongest intermolecular force in <b>liquid methanol, CH<sub>3</sub>OH</b>?",
   ["Hydrogen bonding", "Dipole&ndash;dipole", "London dispersion", "Ion&ndash;dipole"],
   "<p>Methanol has an O&ndash;H bond: H bonded to O, with lone pairs on O of the neighbouring molecule. Hydrogen bonding is the strongest. (It also has dipole&ndash;dipole and dispersion, but the question asks for the <em>strongest</em>.)</p>")

mc("imf-2", "imf", 1, "Quiz 4 style",
   "What is the strongest intermolecular force in <b>SO<sub>2</sub></b>?",
   ["Dipole&ndash;dipole", "Hydrogen bonding", "London dispersion only", "Ion&ndash;ion"],
   "<p>SO<sub>2</sub> is bent, so its S&ndash;O bond dipoles do not cancel: polar. It has no H, so no hydrogen bonding. Strongest = dipole&ndash;dipole.</p>")

mc("imf-3", "imf", 1, "Quiz 4 style",
   "What is the strongest intermolecular force in <b>O<sub>2</sub></b> (or N<sub>2</sub>, or CF<sub>4</sub>)?",
   ["London dispersion", "Dipole&ndash;dipole", "Hydrogen bonding", "Covalent bonding"],
   "<p>O<sub>2</sub> is a nonpolar homonuclear molecule. CF<sub>4</sub> has polar bonds but a symmetric tetrahedral shape, so it is nonpolar too. Only temporary (instantaneous) dipoles remain. <b>Covalent bonding is not an intermolecular force</b>: it is inside the molecule.</p>")

mc("imf-4", "imf", 2, "Rec 9.5 style",
   "Which has the <b>highest boiling point</b>?",
   ["NaF", "HF", "CH<sub>4</sub>", "Ne"],
   "<p>Boiling point rises with the strength of the attraction that must be overcome: Ne (weak dispersion) &lt; CH<sub>4</sub> (dispersion) &lt; HF (hydrogen bonds) &lt; NaF (ion&ndash;ion, much stronger). The same idea ranks Ne &lt; O<sub>2</sub> &lt; N(CH<sub>3</sub>)<sub>3</sub> &lt; NaCl &lt; CaO in Rec 9.5 (CaO&rsquo;s 2+/2&minus; charges beat NaCl&rsquo;s 1+/1&minus;).</p>")

mc("imf-5", "imf", 2, "Rec 9.5 style",
   "What is the strongest force <b>between</b> an HBr molecule and a CH<sub>4</sub> molecule?",
   ["Dipole&ndash;induced dipole", "Dipole&ndash;dipole", "Hydrogen bonding", "Ion&ndash;dipole"],
   "<p>HBr is polar; CH<sub>4</sub> is nonpolar. HBr&rsquo;s field distorts CH<sub>4</sub>&rsquo;s electron cloud and induces a dipole. Polar + nonpolar = dipole&ndash;induced dipole.</p>")

mc("imf-6", "imf", 2, "Rec 9.5 style",
   "Among HF, HCl, HBr and HI, HF has the highest boiling point even though it is the smallest. Why?",
   ["HF forms hydrogen bonds; the others only have dipole&ndash;dipole and (growing) dispersion forces", "HF has the strongest covalent bond so it takes more energy to boil", "HF is the largest and most polarizable", "HF is ionic"],
   "<p>Boiling breaks forces <b>between</b> molecules, not the H&ndash;F bond. HF&rsquo;s H bonds win. Among HCl, HBr, HI the boiling point rises with size because dispersion forces grow.</p>")

mc("imf-7", "imf", 2, "Rec 9.5 style",
   "Which of these molecules can form <b>hydrogen bonds with itself</b>?",
   ["CH<sub>3</sub>NH<sub>2</sub>", "CH<sub>3</sub>OCH<sub>3</sub>", "CH<sub>3</sub>Cl", "CH<sub>3</sub>F"],
   "<p>You need an H bonded to N, O or F in the molecule. CH<sub>3</sub>NH<sub>2</sub> has N&ndash;H. CH<sub>3</sub>OCH<sub>3</sub> has O but no O&ndash;H; CH<sub>3</sub>F has F but the H atoms are on carbon (C&ndash;H does not count).</p>")

selfq("imf-8", "imf", 2, "Rec 9.5 style",
      "Explain why methane (CH<sub>4</sub>) is a gas at room temperature but C<sub>24</sub>H<sub>50</sub> is a waxy solid, even though both are nonpolar hydrocarbons.",
      "<p>Both only have <b>dispersion forces</b>, but dispersion grows with the number of electrons and the contact surface (polarizability scales with molecular volume). A long C<sub>24</sub> chain has far more electrons and a much larger contact area, so each molecule is attracted far more strongly to its neighbours; it takes more thermal energy to separate them, so it is solid. CH<sub>4</sub> is tiny: only weak attractions, so thermal motion wins even at low temperature.</p>")

# ================================================================== BANDS
topic("bands", "Bands, semiconductors &amp; doping", "unit8", "Quiz 5",
      "Quiz 5: match three band diagrams to gold / germanium / diamond (3 pts); does strain make the gap bigger or smaller (3 pts); n-type or p-type (1 pt); gap &rarr; LED wavelength with hc = 1240 eV&middot;nm (3 pts). "
      "Recipe: overlap or half-filled = metal; small gap (about 1 eV) = semiconductor; big gap (&gt; 3 eV) = insulator; longer (weaker) bonds &rarr; smaller gap; "
      "group 15 dopant in group 14 host = n-type, group 13 = p-type; &lambda;(nm) = 1240 / E(eV).")

mc("bands-1", "bands", 1, "Quiz 5 style",
   "A band diagram shows a filled band that <b>overlaps</b> an empty band. Which of gold, germanium and diamond is this?",
   ["Gold (a metal)", "Germanium (a semiconductor)", "Diamond (an insulator)", "None of them"],
   "<p>Overlap means there is no gap at all: electrons can step into empty levels with no energy cost: a metal. Germanium (0.67 eV) and diamond (5.4 eV) both have a filled valence band, an empty conduction band and a gap (small vs large).</p>")

lam_ge = HC / 0.67
num("bands-2", "bands", 1, "Quiz 5 style",
    "A pure germanium LED emits light across the band gap, <b>0.67 eV</b>. What wavelength (nm) is emitted? (hc = 1240 eV&middot;nm)",
    lam_ge, "nm",
    "<p>&lambda; = hc/E = 1240 / 0.67 = <b>%s nm</b>, infrared (visible light is 400&ndash;750 nm). Smaller gap = longer wavelength.</p>" % fmt(lam_ge, 4),
    tol=0.015, text="%s nm" % fmt(lam_ge, 4))

lam_d = HC / 5.4
num("bands-3", "bands", 1, "Rec 10 style",
    "Diamond has a band gap of <b>5.4 eV</b>. What is the longest wavelength (nm) of light that can excite an electron across the gap? Is a pure diamond transparent to visible light?",
    lam_d, "nm",
    "<p>&lambda; = 1240 / 5.4 = <b>%s nm</b>: ultraviolet. Visible photons (400&ndash;750 nm) have less than 3.1 eV, not enough to cross the gap, so they pass through: pure diamond is transparent. (Rec 10&rsquo;s key says 229.4 nm; with the same constants it is 229.6 nm.)</p>" % fmt(lam_d, 4),
    tol=0.01, text="%s nm" % fmt(lam_d, 4))

mc("bands-4", "bands", 1, "Quiz 5 style",
   "Which dopant would make <b>germanium n-type</b>?",
   ["Antimony (Sb, group 15)", "Gallium (Ga, group 13)", "Aluminium (Al, group 13)", "Zinc (Zn, group 12)"],
   "<p>Ge is in group 14 (4 valence electrons). A group 15 atom brings 5: one extra electron, loosely held (a donor level just below the conduction band) &rarr; n-type. Groups 13 and 12 are short of electrons &rarr; p-type (acceptors). A dopant can also supply several carriers: Te (6 e<sup>&minus;</sup>) is n-type, Zn (2 e<sup>&minus;</sup>) is p-type.</p>")

atoms_ge = 5.32 / 72.63 * NA
n_ga = atoms_ge / 1e6
m_ga = n_ga / NA * 69.72
num("bands-5", "bands", 3, "Rec 10 style",
    "Germanium (density 5.32 g/cm&sup3;, M = 72.63 g/mol) is doped so that <b>1 in every 10<sup>6</sup></b> Ge atoms is replaced by gallium (M = 69.72 g/mol). What mass of Ga is needed for <b>1 cm&sup3;</b> of crystal? Answer in grams, e.g. 5e-6.",
    m_ga, "g",
    "<ol><li>Atoms of Ge in 1 cm&sup3; = 5.32 / 72.63 &times; 6.022&times;10<sup>23</sup> = %s.</li>"
    "<li>Ga atoms = that / 10<sup>6</sup> = %s.</li>"
    "<li>Mass = (%s / 6.022&times;10<sup>23</sup>) &times; 69.72 g/mol = <b>%s g</b> (about 5 &micro;g). Tiny amounts change conductivity a lot.</li></ol>" % (fmt(atoms_ge, 4), fmt(n_ga, 4), fmt(n_ga, 4), fmt(m_ga, 3)),
    hint="density &rarr; mass &rarr; moles &rarr; atoms; then divide by 10<sup>6</sup>; then back to mass.", tol=0.02, text="%s g" % fmt(m_ga, 3))

mc("bands-6", "bands", 2, "Quiz 5 style",
   "Silicon is squeezed so the bond distance <b>shrinks</b> slightly (compressive strain). The band gap should&hellip;",
   ["Get larger: shorter bonds are stronger, so electrons are more tightly bound and need more energy to be promoted", "Get smaller, because the atoms are closer together", "Stay the same; band gaps do not depend on bond length", "Vanish immediately"],
   "<p>Quiz 5 asked the opposite case (stretched bonds &rarr; weaker bonds &rarr; <b>smaller</b> gap). Mirror it: shorter bond &rarr; more overlap &rarr; bigger split between bonding and antibonding bands &rarr; larger gap. Always say <em>why</em>: the quiz gives 3 points mostly for the reasoning.</p>")

mc("bands-7", "bands", 2, "Rec 9.5 style",
   "Be is 2s<sup>2</sup>, so a lone 2s band would be completely full. Why is Be still a metal?",
   ["The 2s and 2p bands overlap, so there are empty levels right above the filled ones", "Be has a half-filled 2s band", "Be forms an ionic lattice", "The 1s band is partly filled"],
   "<p>A full band would mean bond order 0 (like He<sub>2</sub>) and no empty levels to move into. The overlapping 2p band solves both problems: some electrons occupy low-lying bonding levels of the p band, and plenty of empty levels sit right above.</p>")

mc("bands-8", "bands", 2, "Rec 10 style",
   "Heating a pure semiconductor generally makes its conductivity&hellip;",
   ["increase, because more electrons are thermally promoted across the gap (creating electron&ndash;hole pairs; both carry current)", "decrease, because the electrons slow down", "stay constant", "drop to zero"],
   "<p>Temperature sets how often electrons get across the gap. Each event creates a free electron <b>and</b> a hole; both conduct. (Metals behave the other way round: more thermal vibration scatters the electrons, so conductivity usually drops. <span class=\"pill\" style=\"--c:var(--ink-soft);--c-soft:var(--line-soft)\">extra</span>)</p>")

sig = 1 / 2.0e-8
num("bands-9", "bands", 1, "Rec 10 style",
    "A metal has resistivity &rho; = 2.0&times;10<sup>&minus;8</sup> &Omega;&middot;m. What is its conductivity in S/m? Give scientific notation, e.g. 5e7.",
    sig, "S/m",
    "<p>&sigma; = 1/&rho; = 1 / (2.0&times;10<sup>&minus;8</sup>) = <b>%s S/m</b> (a siemens is 1/&Omega;).</p>" % fmt(sig, 2),
    tol=0.01, text="%s S/m" % fmt(sig, 2))

ke = HC / 400 - 2.1
num("bands-10", "bands", 2, "Rec 10 style",
    "Caesium has work function 2.1 eV. Violet light of wavelength <b>400 nm</b> hits it. What is the maximum kinetic energy (eV) of an escaping electron?",
    ke, "eV",
    "<p>Photon energy E = 1240/400 = 3.10 eV. KE = h&nu; &minus; &phi; = 3.10 &minus; 2.1 = <b>%s eV</b>. (If h&nu; &lt; &phi; nothing is emitted, however bright the light.)</p>" % fmt(ke, 3),
    tol=0.03, text="%s eV" % fmt(ke, 3))

# ================================================================== LATTICE
topic("lattice", "Cubic lattices, packing &amp; crystal structures", "unit9", "Quiz 6",
      "Quiz 6 opens with a BCC iron cell: find a from the atomic radius, count atoms on a plane, divide by the area. "
      "Table to know cold: <b>SC</b> 1 point, a = 2r, 0.52; <b>BCC</b> 2 points, a = 4r/&radic;3, 0.68; <b>FCC</b> 4 points, a = 2&radic;2 r, 0.74. "
      "Atoms touch along the edge (SC), body diagonal (BCC) or face diagonal (FCC).")

mc("lattice-1", "lattice", 1, "Rec 11 style",
   "How many lattice points belong to one <b>face-centred cubic</b> unit cell?",
   ["4", "2", "6", "14"],
   "<p>8 corners &times; &#8539; = 1, plus 6 face centres &times; &frac12; = 3, total <b>4</b>. (SC = 1; BCC = 8 &times; &#8539; + 1 = 2.)</p>")

a_cu = 2 * math.sqrt(2) * 1.28
num("lattice-2", "lattice", 1, "Quiz 6 style",
    "Copper is FCC with atomic radius <b>1.28 &Aring;</b>. What is the lattice parameter a, in &Aring;?",
    a_cu, "&Aring;",
    "<p>In FCC the atoms touch along the <b>face diagonal</b>, which has length a&radic;2 and holds 4r. So a = 4r/&radic;2 = 2&radic;2 r = 2 &times; 1.414 &times; 1.28 = <b>%s &Aring;</b>.</p>" % fmt(a_cu, 4),
    tol=0.01, text="%s &Aring;" % fmt(a_cu, 4))

a_fe = 4 * 1.24 / math.sqrt(3)
num("lattice-3", "lattice", 1, "Quiz 6 style",
    "&alpha;-iron is BCC with covalent radius <b>1.24 &Aring;</b>. What is a in &Aring;?",
    a_fe, "&Aring;",
    "<p>BCC atoms touch along the <b>body diagonal</b> (length a&radic;3), which holds 4r. a = 4r/&radic;3 = 4 &times; 1.24 / 1.732 = <b>%s &Aring;</b> (the value used in the real Quiz 6).</p>" % fmt(a_fe, 4),
    tol=0.01, text="%s &Aring;" % fmt(a_fe, 4))

pf = 2 * (4 / 3) * math.pi * (math.sqrt(3) / 4) ** 3
num("lattice-4", "lattice", 2, "Rec 11 style",
    "Derive the <b>packing fraction of BCC</b> (fraction of the cell volume filled by hard spheres). Enter a decimal like 0.52.",
    pf, "",
    "<ol><li>Atoms per cell = 2.</li><li>Touching along the body diagonal: a&radic;3 = 4r &rarr; r = (&radic;3/4) a.</li>"
    "<li>Packing = 2 &times; (4/3)&pi;r&sup3; / a&sup3; = 2 &times; (4/3)&pi; (&radic;3/4)&sup3; = <b>%s</b> (= &pi;&radic;3/8).</li></ol>" % fmt(pf, 3),
    tol=0.01, text="0.68")

rho_cu = 4 * 63.55 / (NA * (3.61e-8) ** 3)
num("lattice-5", "lattice", 2, "Rec 11 style",
    "FCC copper has a = 3.61 &Aring; and molar mass 63.55 g/mol. Compute its density in g/cm&sup3;.",
    rho_cu, "g/cm&sup3;",
    "<ol><li>FCC has 4 atoms per cell. Mass of cell = 4 &times; 63.55 / 6.022&times;10<sup>23</sup> = %s g.</li>"
    "<li>Volume = a&sup3; = (3.61&times;10<sup>&minus;8</sup> cm)&sup3; = %s cm&sup3; (1 &Aring; = 10<sup>&minus;8</sup> cm).</li>"
    "<li>&rho; = mass/volume = <b>%s g/cm&sup3;</b> (handbook: 8.96).</li></ol>" % (fmt(4 * 63.55 / NA, 4), fmt((3.61e-8) ** 3, 4), fmt(rho_cu, 4)),
    hint="Atoms per cell &times; mass per atom &divide; cell volume (in cm&sup3;).", tol=0.01, text="%s g/cm&sup3;" % fmt(rho_cu, 4))

rho_fe = 2 * 55.85 / (NA * (2.866e-8) ** 3)
num("lattice-6", "lattice", 2, "Rec 11 style",
    "BCC iron has a = 2.866 &Aring; and molar mass 55.85 g/mol. Compute its density in g/cm&sup3;.",
    rho_fe, "g/cm&sup3;",
    "<p>BCC has <b>2</b> atoms per cell. &rho; = 2 &times; 55.85 / (6.022&times;10<sup>23</sup> &times; (2.866&times;10<sup>&minus;8</sup>)&sup3;) = <b>%s g/cm&sup3;</b> (handbook: 7.87).</p>" % fmt(rho_fe, 4),
    tol=0.01, text="%s g/cm&sup3;" % fmt(rho_fe, 4))

mc("lattice-7", "lattice", 2, "Rec 11 style",
   "CsCl has a Cs<sup>+</sup> at the cube centre and Cl<sup>&minus;</sup> at the corners. What is its <b>lattice</b>?",
   ["Simple cubic with a two-ion motif (1 formula unit per cell)", "Body-centred cubic with 2 lattice points", "Face-centred cubic with 4 lattice points", "Hexagonal close packed"],
   "<p>Lattice points must all be <b>identical</b>. The centre ion differs from the corner ion, so the centre is not a lattice point: lattice = simple cubic (1 point), motif = one Cs<sup>+</sup> + one Cl<sup>&minus;</sup>. Crystal = lattice + motif.</p>")

mc("lattice-8", "lattice", 2, "Rec 11 style",
   "How many <b>ions in total</b> are inside one NaCl (rock-salt) unit cell, and what is the lattice?",
   ["8 ions (4 Na<sup>+</sup> + 4 Cl<sup>&minus;</sup>); FCC lattice with a Na&ndash;Cl motif", "2 ions; simple cubic", "4 ions; FCC", "14 ions; BCC"],
   "<p>FCC lattice has 4 points per cell, each carrying a motif of one Na<sup>+</sup> and one Cl<sup>&minus;</sup>: 4 NaCl units = 8 ions. (CaF<sub>2</sub>: FCC with a 1 Ca + 2 F motif = 12 ions; ZnS: 8 ions.)</p>")

dens110 = 2 / ((4 * 1.37 / math.sqrt(3)) ** 2 * math.sqrt(2))
num("lattice-9", "lattice", 3, "Quiz 6 style",
    "Tungsten is BCC with atomic radius <b>1.37 &Aring;</b>. Find the <b>planar density of the (110) plane</b> in atoms/&Aring;&sup2;. (The (110) plane is a rectangle with sides a and a&radic;2 holding 2 atoms.)",
    dens110, "atoms/&Aring;&sup2;",
    "<ol><li>a = 4r/&radic;3 = 4 &times; 1.37 / 1.732 = %s &Aring;.</li>"
    "<li>Atoms on the plane: 4 corners &times; &frac14; + 1 centre atom = <b>2</b>.</li>"
    "<li>Area = a &times; a&radic;2 = %s &Aring;&sup2;.</li>"
    "<li>Density = 2 / %s = <b>%s atoms/&Aring;&sup2;</b>.</li></ol>" % (fmt(4 * 1.37 / math.sqrt(3), 4), fmt((4 * 1.37 / math.sqrt(3)) ** 2 * math.sqrt(2), 4), fmt((4 * 1.37 / math.sqrt(3)) ** 2 * math.sqrt(2), 4), fmt(dens110, 3)),
    hint="a from the body diagonal, then area = a&middot;a&radic;2.", tol=0.02, text="%s atoms/&Aring;&sup2;" % fmt(dens110, 3))

dens100 = 2 / 4.05 ** 2
num("lattice-10", "lattice", 3, "Quiz 6 style",
    "Aluminium is FCC with a = 4.05 &Aring;. What is the planar density of the <b>(100)</b> plane (a face of the cube) in atoms/&Aring;&sup2;?",
    dens100, "atoms/&Aring;&sup2;",
    "<p>A cube face in FCC has 4 corner atoms &times; &frac14; = 1, plus 1 face-centre atom (whole) = <b>2 atoms</b>. Area = a&sup2; = 16.40 &Aring;&sup2;. Density = 2 / 16.40 = <b>%s atoms/&Aring;&sup2;</b>.</p>" % fmt(dens100, 3),
    tol=0.02, text="%s atoms/&Aring;&sup2;" % fmt(dens100, 3))

mc("lattice-11", "lattice", 2, "L17 slide 9",
   "In zinc blende (ZnS), the S<sup>2&minus;</sup> ions form an FCC array. Where do the Zn<sup>2+</sup> ions sit?",
   ["In 4 of the 8 tetrahedral holes (half of them)", "In all the octahedral holes", "In all 8 tetrahedral holes", "At the centre of the cube only"],
   "<p>An FCC array has 4 octahedral and 8 tetrahedral holes per cell. ZnS fills <b>half the tetrahedral</b> holes (4 Zn per 4 S = 1 : 1). Filling <em>all</em> octahedral holes gives rock salt (NaCl); filling all 8 tetrahedral holes with F<sup>&minus;</sup> gives fluorite (CaF<sub>2</sub>).</p>")

mc("lattice-12", "lattice", 2, "L17 slide 10",
   "In a perovskite cell, Ca is at the 8 corners, Ti at the body centre, and O at the 6 face centres. What is the formula?",
   ["CaTiO<sub>3</sub>", "CaTiO<sub>6</sub>", "Ca<sub>8</sub>TiO<sub>6</sub>", "CaTi<sub>2</sub>O<sub>3</sub>"],
   "<p>Count what belongs to the cell: Ca = 8 &times; &#8539; = 1; Ti = 1 (inside); O = 6 &times; &frac12; = 3. Formula CaTiO<sub>3</sub>.</p>")

mc("lattice-13", "lattice", 1, "L17 slide 6",
   "What stacking sequence gives <b>FCC (cubic close packing)</b>, and what gives hexagonal close packing?",
   ["FCC: ABCABC&hellip;; HCP: ABABAB&hellip;", "FCC: ABABAB&hellip;; HCP: ABCABC&hellip;", "Both are ABCABC&hellip;", "FCC: AAAA&hellip;; HCP: ABAB&hellip;"],
   "<p>Each layer sits in the hollows of the one below. HCP repeats after two layers (third layer directly over the first, A). FCC uses the other hollows (C) for the third layer, so it repeats after three. Both fill 74% of space and have 12 nearest neighbours.</p>")

a_al = 4.05
nn = a_al / math.sqrt(2)
num("lattice-14", "lattice", 2, "L17 slide 3",
    "What is the <b>nearest-neighbour distance</b> in FCC aluminium (a = 4.05 &Aring;)?",
    nn, "&Aring;",
    "<p>In FCC the atoms touch along the face diagonal. The diagonal (a&radic;2) holds two atom diameters, so one diameter, which is the nearest-neighbour distance, is a&radic;2/2 = a/&radic;2 = 4.05 / 1.414 = <b>%s &Aring;</b> (= 2r). Table: SC: a; BCC: a&radic;3/2; FCC: a/&radic;2.</p>" % fmt(nn, 4),
    tol=0.01, text="%s &Aring;" % fmt(nn, 4))

selfq("lattice-15", "lattice", 3, "Rec 11 style",
      "Derive the 74% packing fraction of an FCC lattice (Recitation 11, problem 3).",
      "<ol><li>FCC: atoms touch along the <b>face diagonal</b>. The diagonal of a square face is a&radic;2, and it holds r + 2r + r = 4r. So 4r = a&radic;2, r = (&radic;2/4)a.</li>"
      "<li>Atoms per cell: 4 (8 &times; &#8539; + 6 &times; &frac12;).</li>"
      "<li>Packing = 4 &times; (4/3)&pi;r&sup3; / a&sup3;. With r&sup3; = (2&radic;2/64)a&sup3; = (&radic;2/32)a&sup3;: 4 &times; (4/3)&pi; &times; &radic;2/32 = &pi;&radic;2/6 = <b>0.7405</b>.</li></ol>")

# ================================================================== MILLER
topic("miller", "Miller indices, d-spacing &amp; Bragg's law", "unit9", "Quiz 6",
      "Quiz 6 parts 2&ndash;3: name equivalent planes ({hkl} family) and use Bragg's law. "
      "Recipe: intercepts (in cell edges) &rarr; reciprocals &rarr; clear fractions &rarr; (hkl); &infin; becomes 0; a bar means negative. "
      "d<sub>hkl</sub> = a/&radic;(h&sup2;+k&sup2;+l&sup2;) for cubic; <b>2d sin&theta; = n&lambda;</b> with &theta; the glancing angle (the detector reads 2&theta;).")

mc("miller-1", "miller", 1, "L17 slide 11",
   "A plane cuts the x, y and z axes at 1, &frac12; and &#8531; of the cell edge. What are its Miller indices?",
   ["(123)", "(1 &frac12; &#8531;)", "(321)", "(632)"],
   "<p>Intercepts 1, &frac12;, &#8531; &rarr; reciprocals 1, 2, 3 &rarr; <b>(123)</b>. Small intercepts give big indices.</p>")

mc("miller-2", "miller", 2, "L17 slide 11",
   "A plane intercepts x at 1, runs parallel to y, and intercepts z at &minus;1. What are its Miller indices?",
   ["(1 0 %s)" % OV("1"), "(1 0 1)", "(1 &infin; %s)" % OV("1"), "(1 1 %s)" % OV("1")],
   "<p>Intercepts: 1, &infin;, &minus;1 &rarr; reciprocals 1, 0, &minus;1 &rarr; write the negative with a bar over the number: <b>(1 0 %s)</b>, never (10&minus;1).</p>" % OV("1"),
   whys={1: "That plane cuts z at +1, not at &minus;1.", 2: "&infin; is never written in an index: it becomes 0.", 3: "The plane is parallel to y, so the middle index is 0, not 1."})

d111 = 4.05 / math.sqrt(3)
num("miller-3", "miller", 1, "L17 slide 14",
    "Aluminium is FCC with a = 4.05 &Aring;. Find d<sub>111</sub> in &Aring;.",
    d111, "&Aring;",
    "<p>d = a / &radic;(h&sup2;+k&sup2;+l&sup2;) = 4.05 / &radic;3 = <b>%s &Aring;</b>. (Valid for cubic crystals only.)</p>" % fmt(d111, 4),
    tol=0.01, text="%s &Aring;" % fmt(d111, 4))

d220 = 3.61 / math.sqrt(8)
num("miller-4", "miller", 1, "L17 slide 14",
    "Copper has a = 3.61 &Aring;. Find the spacing d<sub>220</sub> in &Aring;.",
    d220, "&Aring;",
    "<p>d<sub>220</sub> = 3.61 / &radic;(4 + 4 + 0) = 3.61 / &radic;8 = <b>%s &Aring;</b>. Note d<sub>220</sub> = d<sub>110</sub> / 2: doubling every index halves the spacing.</p>" % fmt(d220, 4),
    tol=0.01, text="%s &Aring;" % fmt(d220, 4))

th = math.degrees(math.asin(1.54 / (2 * d111)))
num("miller-5", "miller", 2, "Quiz 6 style",
    "Cu K&alpha; X-rays (&lambda; = 1.54 &Aring;) diffract from the (111) planes of aluminium (d = %s &Aring;). Find the Bragg angle &theta; (first order), in degrees." % fmt(d111, 4),
    th, "&deg;",
    "<ol><li>Bragg: 2d sin&theta; = n&lambda; with n = 1.</li><li>sin&theta; = &lambda;/(2d) = 1.54 / (2 &times; %s) = %s.</li><li>&theta; = arcsin(%s) = <b>%s&deg;</b> (calculator in degree mode!). The detector would read 2&theta; = %s&deg;.</li></ol>" % (fmt(d111, 4), fmt(1.54 / (2 * d111), 4), fmt(1.54 / (2 * d111), 4), fmt(th, 4), fmt(2 * th, 4)),
    tol=0.01, text="%s&deg;" % fmt(th, 4))

a_f = 2.866
d110 = a_f / math.sqrt(2)
th2 = math.degrees(math.asin(1.54 / (2 * d110)))
num("miller-6", "miller", 3, "Quiz 6 style",
    "&alpha;-Fe (BCC, a = 2.866 &Aring;) is measured with Cu K&alpha; (&lambda; = 1.54 &Aring;). At what <b>2&theta;</b> (the angle the detector reports) is the first-order {110} peak?",
    2 * th2, "&deg;",
    "<ol><li>d<sub>110</sub> = a/&radic;2 = %s &Aring; (<b>not</b> a: the real Quiz 6 key used 2.86 &Aring; for d<sub>110</sub>, which is the lattice parameter).</li>"
    "<li>sin&theta; = 1.54 / (2 &times; %s) = %s, &theta; = %s&deg;.</li>"
    "<li>2&theta; = <b>%s&deg;</b>, matching the real iron (110) peak near 44.7&deg;.</li></ol>" % (fmt(d110, 4), fmt(d110, 4), fmt(1.54 / (2 * d110), 4), fmt(th2, 4), fmt(2 * th2, 4)),
    tol=0.01, text="%s&deg;" % fmt(2 * th2, 4))

mc("miller-7", "miller", 2, "Quiz 6 style",
   "An XRD pattern lists a peak at <b>2&theta; = 38.2&deg;</b>. Which angle goes into Bragg&rsquo;s law 2d sin&theta; = n&lambda;?",
   ["&theta; = 19.1&deg;", "&theta; = 38.2&deg;", "&theta; = 76.4&deg;", "&theta; = 90&deg; &minus; 38.2&deg;"],
   "<p>The x-axis of a diffraction pattern is <b>2&theta;</b> (the angle between the incoming and the diffracted beams). Halve it before using Bragg&rsquo;s law. (If a problem just says &ldquo;a peak at 13.56&rdquo; with no unit, ask whether it is &theta; or 2&theta;; the real Quiz 6 treated it as &theta;.)</p>")

ak = 1.54 / (2 * math.sin(math.radians(22.4)))
a_from = ak * math.sqrt(2)
num("miller-8", "miller", 3, "Quiz 6 style",
    "A BCC metal shows its first-order {110} peak at <b>&theta; = 22.4&deg;</b> with &lambda; = 1.54 &Aring;. Find the lattice parameter a (&Aring;).",
    a_from, "&Aring;",
    "<ol><li>d<sub>110</sub> = &lambda; / (2 sin&theta;) = 1.54 / (2 &times; sin 22.4&deg;) = %s &Aring;.</li><li>d<sub>110</sub> = a/&radic;2, so a = d&radic;2 = <b>%s &Aring;</b> (that is iron).</li></ol>" % (fmt(ak, 4), fmt(a_from, 4)),
    tol=0.01, text="%s &Aring;" % fmt(a_from, 4))

mc("miller-9", "miller", 1, "L17 slide 13",
   "In a <b>cubic</b> crystal, which direction is perpendicular to the (111) plane?",
   ["[111]", "[100]", "[110]", "[1 1 %s]" % OV("1")],
   "<p>In cubic crystals only: the plane (hkl) is perpendicular to the direction [hkl]. Check with the dot product: the vectors lying in (111), such as (&minus;1, 1, 0), have zero dot product with (1, 1, 1).</p>")

mc("miller-10", "miller", 1, "L17 slide 12",
   "How many faces does the {001} family describe for a cube?",
   ["6", "3", "8", "12"],
   "<p>{001} = (001), (00%s), (100), (%s00), (010), (0%s0): all <b>six</b> faces of the cube. Curly braces = every symmetry-equivalent plane.</p>" % (OV("1"), OV("1"), OV("1")))

mc("miller-11", "miller", 2, "L17 slide 14",
   "Compared with d<sub>111</sub>, the spacing d<sub>222</sub> in the same cubic crystal is&hellip;",
   ["exactly half as large", "twice as large", "the same", "one third as large"],
   "<p>d<sub>222</sub> = a/&radic;12 and d<sub>111</sub> = a/&radic;3, so the ratio is &radic;3/&radic;12 = &frac12;. (Doubling all the indices halves the spacing: the planes of (222) include the (111) planes plus a plane midway between each pair.)</p>")

mc("miller-12", "miller", 2, "L17 slide 11",
   "A plane cuts x at 1 and y at 1 and is parallel to z. What are its Miller indices?",
   ["(110)", "(111)", "(100)", "(011)"],
   "<p>Intercepts 1, 1, &infin; &rarr; reciprocals 1, 1, 0: <b>(110)</b>. Parallel to an axis means intercept &infin; and index 0.</p>")

mc("miller-13", "miller", 3, "L17 slide 16 &middot; extra",
   "A powder XRD pattern of an FCC metal shows peaks indexed (111), (200), (220), (311), (222). Which of these peaks would you <b>not</b> expect for an FCC metal? <span class=\"pill\" style=\"--c:var(--ink-soft);--c-soft:var(--line-soft)\">extra</span>",
   ["(100)", "(111)", "(200)", "(220)"],
   "<p>On the L17 slide every indexed peak has indices that are <b>all odd or all even</b>: (111), (200), (220), (311), (222), (400), (331), (420). That is the signature of an FCC lattice (an extra, not stated on the slide). (100) is mixed odd/even, so it is absent for FCC.</p>")

# ---- added from L15 (semiconductors), L16 (crystallography)
lam_gan = HC / 3.4
num("bands-11", "bands", 1, "L15 style",
    "GaN is a III&ndash;V semiconductor with band gap <b>3.4 eV</b> (L15 slide 15). What wavelength does a GaN LED emit, in nm? Is it visible?",
    lam_gan, "nm",
    "<p>&lambda; = 1240 / 3.4 = <b>%s nm</b>: ultraviolet (visible is about 400&ndash;750 nm). Blue LEDs use GaN mixed with In to lower the gap a little.</p>" % fmt(lam_gan, 4),
    tol=0.015, text="%s nm" % fmt(lam_gan, 4))

mc("bands-12", "bands", 2, "L15 slide 15",
   "Among GaN, GaP, GaAs and GaSb (all with gallium), which has the <b>largest</b> band gap, and why?",
   ["GaN (3.4 eV): the gap shrinks going down the group-15 column (N &gt; P &gt; As &gt; Sb)", "GaSb (0.7 eV): the largest atom has the largest gap", "GaAs (1.4 eV): it is the most common", "They all have the same gap"],
   "<p>L15 slide 15: GaN 3.4, GaP 2.3, GaAs 1.4, GaSb 0.7 eV; the same decrease down a column appears for Al (AlN 6.3 &rarr; AlSb 1.5) and In (InN 2.1 &rarr; InSb 0.2). Smaller atoms hold their electrons more tightly and give a bigger gap.</p>")

mc("bands-13", "bands", 2, "L15 slide 15",
   "Which of these semiconductors has a band gap that corresponds to <b>visible</b> light (about 1.65&ndash;3.1 eV)?",
   ["ZnSe (2.7 eV, about 460 nm, blue)", "GaAs (1.4 eV, about 890 nm)", "AlN (6.3 eV, about 200 nm)", "InSb (0.2 eV, about 6200 nm)"],
   "<p>Convert each with &lambda; = 1240/E. ZnSe gives 459 nm (blue, visible). GaAs and InSb are infrared; AlN is deep ultraviolet. (The gap in a compound can be tuned by mixing, e.g. Ga(P,As) between GaP and GaAs, which L15 poses as an open question.)</p>")

mc("bands-14", "bands", 2, "L15 slide 14",
   "Pure Si has about 1 conducting electron per 10<sup>12</sup> atoms at room temperature. About how many atoms per conducting electron does <b>doped (extrinsic)</b> Si have (L15 slide 14)?",
   ["between 10<sup>2</sup> and 10<sup>7</sup> atoms per conducting electron", "10<sup>15</sup> atoms", "exactly 1 per atom", "the same 10<sup>12</sup>"],
   "<p>Doping puts a carrier in every 10<sup>2</sup>&ndash;10<sup>7</sup> atoms: a million to ten orders of magnitude more carriers than the pure crystal. (Rec 10 problem 4 works one of these numbers out.)</p>")

a_au = 407.0
r_au = a_au / (2 * math.sqrt(2))
num("lattice-16", "lattice", 1, "L16 slide 16",
    "Gold is FCC with lattice parameter <b>a = 407 pm</b> (L16 slide 16). Find the atomic radius r in pm.",
    r_au, "pm",
    "<p>In FCC the atoms touch along the face diagonal: 4r = a&radic;2, so r = a/(2&radic;2) = 407 / 2.828 = <b>%s pm</b> (the gold radius, 144 pm).</p>" % fmt(r_au, 4),
    tol=0.01, text="%s pm" % fmt(r_au, 4))

mc("lattice-17", "lattice", 1, "L16 slide 12",
   "How many Bravais lattices does the <b>cubic</b> system have, and how many are there in total across all seven crystal systems?",
   ["3 (SC, BCC, FCC); 14 in total", "1; 7 in total", "4 (SC, BCC, FCC, HCP); 14 in total", "3; 7 in total"],
   "<p>Cubic has three: simple, body-centred, face-centred. Counting all systems on L16 slide 12: cubic 3, tetragonal 2, orthorhombic 4, hexagonal 1, rhombohedral 1, monoclinic 2, triclinic 1 = <b>14</b>. (HCP is a stacking pattern with a hexagonal lattice, not a cubic one.)</p>")

mc("lattice-18", "lattice", 3, "L16 slide 11 &middot; extra",
   "L16 shows a Penrose tiling of two rhombus shapes that covers the plane but never repeats by translation, and asks &ldquo;Is this a crystal?&rdquo; With the definition <b>crystal = lattice + motif</b>, the answer is&hellip;",
   ["No: it has no lattice (no translational periodicity), even though it is ordered", "Yes: any ordered pattern is a crystal", "Yes: it has a motif of two tiles", "No: it has no motif"],
   "<p>A lattice requires that sliding the pattern by a repeat vector maps it exactly onto itself. A Penrose tiling is ordered but never does that. (The slide does not print the answer; such structures exist in materials as <em>quasicrystals</em>.)</p>")
