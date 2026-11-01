from practice_lib import *
import math

R = 8.314
HC = 1240.0
OV = lambda s: '<span style="text-decoration:overline">%s</span>' % s

# ---- Exam 2 additions: Recitation 12 (XRD selection rules, defects) and the Fall 2024 Exam 2 review styles

# ---------------------------------------------------------------- XRD selection rules and peak analysis
mc("miller-14", "miller", 2, "Rec 12 style",
   "For a <b>BCC</b> crystal the selection rule is h + k + l = even. Which of these peaks is <b>absent</b> in a BCC powder pattern?",
   ["(111)", "(110)", "(200)", "(211)"],
   "<p>(110): 1+1+0 = 2 even &#10003;; (200): 2 even &#10003;; (211): 4 even &#10003;; <b>(111): 3 is odd, so it is selectively absent</b>. Extra atoms at the body centre make the waves from some planes cancel (destructive interference) at exactly those angles.</p>")

mc("miller-15", "miller", 2, "Rec 12 style",
   "For an <b>FCC</b> crystal the selection rule is h, k, l all even or all odd. Which peak is <b>absent</b>?",
   ["(210)", "(111)", "(200)", "(220)"],
   "<p>(111) all odd &#10003;; (200) all even (0 counts as even) &#10003;; (220) all even &#10003;; <b>(210) mixes odd and even</b>, so it is absent. Simple cubic has no rule: every (hkl) can appear.</p>")

lam = 0.154
tt = [38.19, 44.39, 64.59, 77.58, 81.74]
s2 = [math.sin(math.radians(t / 2)) ** 2 for t in tt]
ratios = [x / s2[0] for x in s2]
a111 = lam * math.sqrt(3) / (2 * math.sin(math.radians(tt[0] / 2)))
num("miller-16", "miller", 3, "Rec 12 problem 1",
    "A powder XRD pattern taken with Cu K&alpha; (&lambda; = 0.154 nm) shows peaks at 2&theta; = 38.19&deg;, 44.39&deg;, 64.59&deg;, 77.58&deg; and 81.74&deg;. The structure is FCC and the first peak is (111). Find the lattice parameter a in <b>nm</b>.",
    a111, "nm",
    "<ol><li>&theta; = 38.19/2 = 19.10&deg; (halve the peak angle).</li>"
    "<li>d<sub>111</sub> = &lambda;/(2 sin&theta;) = 0.154 / (2 &times; %s) = %s nm.</li>"
    "<li>a = d&radic;(1+1+1) = %s &times; 1.732 = <b>%s nm</b> (4.08 &Aring;).</li></ol>" % (
        fmt(math.sin(math.radians(tt[0] / 2)), 4), fmt(a111 / math.sqrt(3), 4), fmt(a111 / math.sqrt(3), 4), fmt(a111, 4)),
    hint="Use 2d sin&theta; = &lambda; with &theta; = (2&theta;)/2, then d = a/&radic;3.", tol=0.01, text="%s nm" % fmt(a111, 4))

mc("miller-17", "miller", 3, "Rec 12 problem 1",
   "Using the same five peaks (2&theta; = 38.19&deg;, 44.39&deg;, 64.59&deg;, 77.58&deg;, 81.74&deg;), the ratios sin&sup2;&theta; / sin&sup2;&theta;<sub>1</sub> come out as %s. What do you conclude?" % ", ".join(fmt(x, 3) for x in ratios),
   ["FCC: multiplying by 3 gives 3 : 4 : 8 : 11 : 12 = (111), (200), (220), (311), (222)", "BCC: the ratios 1 : 2 : 3 : 4 : 5 : 6", "Simple cubic: the ratios 1 : 2 : 3 : 4 : 5", "Hexagonal close packed"],
   "<p>Bragg gives sin&sup2;&theta; &prop; h&sup2;+k&sup2;+l&sup2;. So the ratio of the peaks tells you the ratio of (h&sup2;+k&sup2;+l&sup2;): here 1 : 1.33 : 2.67 : 3.67 : 4.0, which is <b>3 : 4 : 8 : 11 : 12</b> after multiplying by 3: the allowed FCC reflections (111), (200), (220), (311), (222). Fingerprints: SC 1:2:3:4:5:6:8; BCC 2:4:6:8:10:12 (= 1:2:3:4:5:6); FCC 3:4:8:11:12:16.</p>")

r_au = a111 / (2 * math.sqrt(2)) * 1000
num("miller-18", "miller", 2, "Rec 12 problem 1",
    "The FCC metal above has a = %s nm. What is its atomic radius, in pm? (Which metal does that match?)" % fmt(a111, 4),
    r_au, "pm",
    "<p>FCC: 4r = a&radic;2, so r = a/(2&radic;2) = %s nm / 2.828 = <b>%s pm</b>. That is gold (a = 0.408 nm, r = 144 pm), as in L16 slide 16.</p>" % (fmt(a111, 4), fmt(r_au, 4)),
    tol=0.01, text="%s pm" % fmt(r_au, 4))

mc("miller-19", "miller", 2, "Rec 15 (Exam 2 review) style",
   "How many directions are in the <b>&lt;110&gt;</b> family of a cubic crystal (counting each sign separately)?",
   ["12", "6", "8", "4"],
   "<p>Permute and sign-flip (1, 1, 0): choose which axis is zero (3 ways) and the signs of the other two (4 ways): 3 &times; 4 = <b>12</b>. Compare &lt;100&gt; = 6 (the face normals) and &lt;111&gt; = 8 (the body diagonals).</p>")

mc("miller-20", "miller", 2, "Rec 15 (Exam 2 review) style",
   "How many <b>distinct</b> {111} planes does a cubic crystal have if parallel planes (such as (111) and (%s%s%s)) count once?" % (OV("1"), OV("1"), OV("1")),
   ["4", "8", "6", "3"],
   "<p>There are 8 sign combinations of (&plusmn;1, &plusmn;1, &plusmn;1) but they pair up as parallel planes: (111), (%s11), (1%s1), (11%s) are the 4 distinct orientations; the other 4 are parallel to these. Similar counts: {100} gives 3 and {110} gives 6 (the six faces of the cube in {100} are 3 pairs).</p>" % (OV("1"), OV("1"), OV("1")))

mc("miller-21", "miller", 2, "Rec 12 problem 3",
   "Dislocations slide on the <b>densest-packed plane</b>, parallel to the directions where atoms touch. What are the slip planes of FCC and BCC?",
   ["FCC: {111}; BCC: {110}", "FCC: {110}; BCC: {111}", "Both: {100}", "FCC: {100}; BCC: {111}"],
   "<p>FCC atoms touch along face diagonals &lt;110&gt;, and the plane that contains the most of them is the close-packed {111}. BCC atoms touch along body diagonals &lt;111&gt;, and the densest plane containing them is {110} (the one that passes through the body-centre atom). Slip plane + slip direction together: FCC {111}&lt;110&gt;, BCC {110}&lt;111&gt;.</p>")

# ---------------------------------------------------------------- defects and glass (2024 Exam 2 review)
mc("defects-15", "defects", 2, "Rec 12 / Rec 15 style",
   "A paper clip gets harder to bend each time you bend it, and finally snaps. What is happening in the crystal?",
   ["Each bend creates more dislocations; they tangle and block each other (work hardening), so the metal gets harder but more brittle until it fractures", "Each bend removes dislocations, so the metal becomes perfect and brittle", "The bends melt the metal slightly", "Bending adds interstitial carbon"],
   "<p>Plastic deformation happens by moving dislocations, and deformation also <b>creates</b> dislocations. A dense, tangled network of dislocations cannot move easily: work hardening. Eventually the metal cannot deform plastically any more and cracks (Rec 12, problem 2).</p>")

mc("defects-16", "defects", 2, "Rec 12 / Rec 15 style",
   "A hammered, hardened but brittle steel sword can be made less brittle by&hellip;",
   ["annealing: heating it (without melting) so diffusion lets atoms rearrange and removes dislocations", "hammering it more", "cooling it to liquid nitrogen temperature", "adding more carbon"],
   "<p><b>Annealing</b> = hold at high temperature so atoms can move (diffusion) into a neater lattice, undoing many dislocations. The metal becomes softer and tougher again (Rec 12 slide 17; Rec 15 problem 12). This is the link between diffusion (L20) and defects (L18).</p>")

mc("defects-17", "defects", 3, "Rec 15 (Exam 2 review) style",
   "Two samples of silica are cooled from the melt: glass A quickly and glass B slowly. Which statement is correct?",
   ["A has the higher molar volume and the higher glass-transition temperature T<sub>g</sub>", "B has the higher molar volume and the higher T<sub>g</sub>", "A has the lower molar volume and the lower T<sub>g</sub>", "They are identical because both are SiO<sub>2</sub>"],
   "<p>Fast cooling does not give the atoms time to settle into a dense arrangement, so the glass is frozen with a <b>larger molar volume</b>, and it stops following the liquid line sooner, at a <b>higher T<sub>g</sub></b>. Slow cooling lets the structure relax further, giving a smaller volume and lower T<sub>g</sub> (the limit is the crystal). The slide set shows viscosity vs temperature and not T<sub>g</sub>; the cooling-curve idea is from the Fall 2024 Exam 2 review. <span class=\"pill\" style=\"--c:var(--ink-soft);--c-soft:var(--line-soft)\">extra</span></p>")

selfq("defects-18", "defects", 3, "Rec 15 (Exam 2 review) style",
      "Sketch molar volume against temperature for a liquid that (a) crystallizes and (b) forms a glass when cooled slowly and when cooled quickly. Mark the melting temperature T<sub>m</sub> and the glass transition T<sub>g</sub>, and say how T<sub>g</sub> of the fast and slow glass compare. <span class=\"pill\" style=\"--c:var(--ink-soft);--c-soft:var(--line-soft)\">extra</span>",
      "<ol><li>Axes: temperature (horizontal, hot on the right) and molar volume (vertical). The liquid line slopes down as temperature falls.</li>"
      "<li><b>Crystallizing:</b> at T<sub>m</sub> the line drops vertically to a lower line (the crystal is denser), then continues down with a shallower slope.</li>"
      "<li><b>Glass:</b> no jump at T<sub>m</sub>. The liquid line just continues (the super-cooled liquid) until T<sub>g</sub>, where the slope bends to the shallower, solid-like slope. The curve ends at a volume <b>above</b> the crystal.</li>"
      "<li><b>Fast vs slow:</b> the fast-cooled glass leaves the liquid line earlier, so it has a <b>higher T<sub>g</sub></b> and a <b>larger final molar volume</b> than the slowly cooled glass.</li></ol>"
      "<p>Compare the L19 viscosity plot: no single melting temperature; viscosity changes smoothly by many powers of ten.</p>")

# ---------------------------------------------------------------- bands, LED, doping (Rec 15 problem 5)
e_hi = HC / 315
e_lo = HC / 400
num("bands-15", "bands", 1, "Rec 15 (Exam 2 review) style",
    "UV-curing LEDs should emit between 315 nm and 400 nm. What is the <b>upper</b> photon-energy limit (at 315 nm) in eV? (hc = 1240 eV&middot;nm)",
    e_hi, "eV",
    "<p>E = 1240 / 315 = <b>%s eV</b>. At the other end, 1240 / 400 = %s eV. So the gap must lie between %s and %s eV: GaN (3.4 eV) fits (365 nm); GaP (2.3 eV, 539 nm, green) does not.</p>" % (fmt(e_hi, 3), fmt(e_lo, 3), fmt(e_lo, 3), fmt(e_hi, 3)),
    tol=0.01, text="%s eV" % fmt(e_hi, 3))

mc("bands-16", "bands", 2, "Rec 15 (Exam 2 review) style",
   "Calcium (group 2) atoms substitute for Ga (group 13) atoms in GaN. Is Ca an n-type or p-type dopant, and what does the band diagram show?",
   ["p-type: Ca has fewer valence electrons than Ga, so it makes holes; an acceptor level appears just above the valence band", "n-type: Ca has more valence electrons, so a donor level appears below the conduction band", "n-type: Ca is a metal", "Neither: only group 14 dopants work"],
   "<p>Compare valence electrons with the atom being replaced: Ca has 2, Ga has 3: one short per atom &rarr; <b>acceptor, p-type</b>, charge carriers are holes. Draw: energy axis, valence band (full) at the bottom, conduction band at the top, band gap between, and a short dashed acceptor level just <em>above</em> the valence band.</p>")

# ---------------------------------------------------------------- diffusion (Rec 15 problem 1)
D_door, dC, dx = 0.1, 3.0, 0.10
J_door = D_door * dC / dx
tot = J_door * (1 * 2.5) * 4
num("diffusion-11", "diffusion", 2, "Rec 15 (Exam 2 review) style",
    "Students leaving a lecture hall: concentration 3 students/m&sup2; just inside a doorway and 0 just outside, across a doorway thickness of 0.10 m (linear drop). The diffusion coefficient is D = 0.1 m&sup2;/s. Each of the 4 doors is 1 m &times; 2.5 m. How many students per second pass through all 4 doors?",
    tot, "students/s",
    "<ol><li>Fick&rsquo;s first law, magnitude: J = D &middot; &Delta;C/&Delta;x = 0.1 &times; (3 &minus; 0) / 0.10 = <b>%s students/(m&sup2;&middot;s)</b>.</li>"
    "<li>Area of one door = 1 &times; 2.5 = 2.5 m&sup2;, four doors = 10 m&sup2;.</li>"
    "<li>Rate = J &times; area = %s &times; 10 = <b>%s students/s</b>.</li></ol>" % (fmt(J_door, 3), fmt(J_door, 3), fmt(tot, 3)),
    hint="Flux is per area per second; multiply by the total area.", tol=0.01, text="%s students/s" % fmt(tot, 3))

mc("diffusion-12", "diffusion", 2, "Rec 15 (Exam 2 review) style",
   "In the lecture-hall analogy a cat squeezes between people while a student from another class has to wait for a gap. Which diffuses faster, and which defect type does each represent?",
   ["The cat: like an interstitial atom (small, hops between sites). The other-class student: like a substitutional atom that needs a vacancy", "The student: like an interstitial atom", "They diffuse equally fast", "The cat: like a vacancy"],
   "<p>Small atoms (C, H) diffuse <b>interstitially</b>: they hop between gaps with a low activation energy and have a large D. Atoms the size of the host move by <b>vacancies</b> (substitutional or self-diffusion), which need a vacant neighbouring site and more energy, so D is smaller.</p>")
