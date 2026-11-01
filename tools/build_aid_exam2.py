#!/usr/bin/env python3
"""Builds aid-sheet-exam2.html (two letter pages, front and back) for Exam 2 (L10-L20).
Reuses the stylesheet of aid-sheet.html. PDF: scripts/build-aid-sheet-exam2-pdf.sh"""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base = open(os.path.join(ROOT, "aid-sheet.html"), encoding="utf-8").read()
head = base[:base.index("<body>")]
head = head.replace("<title>3.091 Aid Sheet</title>", "<title>3.091 Exam 2 Aid Sheet</title>")
extra_css = """
  .c-forces h2{background:#F5EDCF; color:#7A5C08;}
  .c-metal h2{background:#E4E9EF; color:#3E5266;}
  .c-crystal h2{background:#F1EAD6; color:#7C5F18;}
  .c-defect h2{background:#F5E2E9; color:#932E50;}
  .c-diff h2{background:#DDF0F3; color:#176A7B;}
  .sheet + .sheet{margin-top:22px;}
  .ln{font-size:7.35pt; line-height:1.36; margin-bottom:1.6pt;}
  .lbl{font-size:7pt;}
  .eqbox{font-size:7.5pt; padding:2.5pt 5pt;}
  table.ref th, table.ref td{font-size:6.9pt; padding:1pt 2.5pt; line-height:1.25;}
  .blk{margin-bottom:6.5pt;}
  .blk h2{font-size:8.6pt; margin-bottom:2.5pt;}
  .head .t1{font-size:17pt;} .head .t2{font-size:8.2pt;}
  @media print{
    .sheet{page-break-after:always; break-after:page;}
    .sheet:last-of-type{page-break-after:auto; break-after:auto;}
    .sheet + .sheet{margin-top:0;}
  }
"""
head = head.replace("</style>", extra_css + "</style>")

def blk(cls, title, *lines):
    out = ['<div class="blk %s"><h2>%s</h2>' % (cls, title)]
    for l in lines:
        if l.startswith("EQ:"):
            out.append('<div class="eqbox">%s</div>' % l[3:])
        else:
            out.append('<div class="ln">%s</div>' % l)
    out.append("</div>")
    return "".join(out)

def table(headers, rows, cls="ref"):
    t = ['<table class="%s"><tr>%s</tr>' % (cls, "".join("<th>%s</th>" % h for h in headers))]
    for r in rows:
        t.append("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r))
    t.append("</table>")
    return "".join(t)

OV = lambda t: '<span style="text-decoration:overline">%s</span>' % t

# ---------------------------------------------------------------- PAGE 1
c1 = "".join([
 blk("c-atoms", "Constants",
     "hc = <b>1240 eV·nm</b> &nbsp; 1 eV = 1.602×10⁻¹⁹ J &nbsp; N<sub>A</sub> = 6.022×10²³",
     "R = 8.314 J/(mol·K) &nbsp; 1 D = 0.2082 e·Å &nbsp; c = 2.998×10⁸ m/s",
     "Visible: 1.65–3.1 eV (400–750 nm). E(eV) = 1240/λ(nm)"),
 blk("c-covalent", "Bond type &amp; strength",
     "EQ:% ionic = 100·[1 − exp(−Δχ²/4)] &nbsp; μ = δ·r",
     "Δχ &lt;0.4 nonpolar · 0.4–1.7 polar covalent · &gt;1.7 ionic",
     "Stronger bond: <b>smaller atoms</b>, <b>higher bond order</b> (C≡C &gt; C=C &gt; C–C; HF &gt; HCl &gt; HBr &gt; HI)",
     "Ionic solid: brittle (shift → like charges repel), conducts only molten/dissolved. Covalent network: hard, high mp. Molecular: low mp (IMF)."),
 blk("c-covalent", "Lewis recipe",
     "① valence e⁻ (+1 per − charge) ② centre = least EN, H never ③ singles, octets outside, leftovers on centre ④ FC = V − L − B/2 ⑤ expanded octet only period ≥ 3 (C,N,O,F never); BF₃, AlH₃, BeF₂ electron-poor ⑥ resonance = average"),
 blk("c-covalent", "VSEPR: groups = atoms + lone pairs (=bond counts 1)",
     table(["grp","0 LP","1 LP","2 LP","3 LP"],
           [["2","linear 180°","","",""],
            ["3","trig-plan 120°","bent &lt;120°","",""],
            ["4","tetrah 109.5°","trig-pyr &lt;109.5°","bent 104.5°",""],
            ["5","TBP 90/120°","seesaw","T-shape","linear"],
            ["6","octah 90°","sq-pyr","sq-planar",""]]),
     "LP–LP &gt; LP–BP &gt; BP–BP. 5 groups: LP <b>equatorial</b>; 6 groups: 2nd LP <b>opposite</b>. Name the shape by <b>atoms only</b>.",
     "<b>Nonpolar</b>: identical atoms, symmetric (CO₂ BF₃ CCl₄ PCl₅ SF₆ XeF₄ AlH₃ XeF₂). <b>Polar</b>: LP breaking symmetry or unlike groups (NH₃ H₂O SF₄ IF₅ IF₃ SeO₂ CF₂H₂ HCN)."),
])
c2 = "".join([
 blk("c-orbital", "Hybridization &amp; σ/π",
     "groups on centre: <b>2 sp · 3 sp² · 4 sp³ · 5 sp³d · 6 sp³d²</b> (lone pairs count; double/triple = 1 group)",
     "σ: 1 per bond (head-on); π: bond order − 1 (side-on p). Triple = 1σ + 2π. #hybrids = #AOs mixed. Label gives parent shape, not exact angle (NH₃ 107°, H₂O 104.5°).",
     "C₂H₄: C sp², HOMO = π, LUMO = π*. C₂H₂: C sp."),
 blk("c-orbital", "Molecular orbitals",
     "n AOs → n MOs (bonding + antibonding pair). Fill lowest first, Hund.",
     "EQ:BO = ½(e⁻ bonding − e⁻ antibonding)",
     "Order O₂, F₂: σ2s σ*2s <b>σ2p π2p π*2p σ*2p</b>. <b>N₂ and lighter (B₂ C₂ N₂): π2p below σ2p.</b> Core 1s cancel.",
     table(["species","e⁻","BO","note"],
           [["H₂","2","1",""],["He₂ / He₂⁺","4 / 3","0 / 0.5",""],["N₂","10","3","diamagn."],["O₂","12","2","2 unpaired π*"],["O₂⁺","11","2.5",""],["F₂ / Ne₂","14 / 16","1 / 0",""],["NO","11","2.5","1 e⁻ in π*"],["CO","10","3","like N₂; O lower"],["HCl","8","1","H1s+Cl3p; 3 LP nonbonding"]]),
     "More electronegative atom has <b>lower</b> AO energy (draw it lower). Nonbonding e⁻ don't count in BO. Unpaired e⁻ = paramagnetic."),
])
c3 = "".join([
 blk("c-metal", "Bands &amp; conductivity",
     "n AOs → n levels → band. <b>Metal</b>: partly filled or overlapping (Na ½ full; Mg, Be: s–p overlap). <b>Semiconductor</b>: full VB, small gap ~1 eV. <b>Insulator</b>: gap &gt; ~3 eV.",
     "E<sub>g</sub>(eV): C 5.4 · Si 1.1 · Ge 0.67 · Sn 0.08 · Pb 0 <b>(decreases down a group)</b>. Longer/weaker bonds → <b>smaller gap</b> (tensile strain).",
     "σ = 1/ρ (S/m; Ω·m). Cu, Ag, Au (s¹d¹⁰) best; alloys worse. Metals: σ ↓ with T. Semiconductors: σ ↑ with T (e⁻ <b>and</b> holes carry).",
     "Photon crosses gap if hν ≥ E<sub>g</sub>; LED λ = 1240/E<sub>g</sub> (Si 1127 nm IR; GaN 365 nm UV). Work function KE = hν − φ."),
 blk("c-metal", "Doping",
     "<b>n-type</b>: dopant has <b>more</b> valence e⁻ than the atom it replaces (group 15 in Si; Te) → donor level just <b>below</b> CB. <b>p-type</b>: <b>fewer</b> (group 13: B Al Ga; Zn; Ca on Ga) → acceptor level just <b>above</b> VB (holes).",
     "Pure Si ≈ 1 carrier/10¹² atoms; doped 1 per 10²–10⁷. Dopant fixed, carrier mobile. Too much dopant: saturation + scattering.",
     "Dopant mass: atoms = (ρ/M)·N<sub>A</sub>·V → ÷ (atoms per carrier, e.g. 10⁵) → ÷N<sub>A</sub> × M<sub>dopant</sub>.",
     "Compound: III–V, II–VI average 4 e⁻. E<sub>g</sub>: GaN 3.4 · GaP 2.3 · GaAs 1.4 · GaSb 0.7 · AlN 6.3 · InSb 0.2 · ZnO 4.4 · ZnSe 2.7 · CdSe 1.7 · SiC 3.0; mixing tunes E<sub>g</sub>."),
 blk("c-forces", "Intermolecular forces",
     "Strength: ion–ion &gt; ion–dipole &gt; <b>H-bond</b> &gt; dipole–dipole &gt; dispersion. Decision: ions? → H on N/O/F + LP? → polar shape? → else dispersion. Polar + nonpolar = dipole–induced dipole.",
     "Dispersion ↑ with size/polarizability (CH₄ gas → C₁₇H₃₆ solid). BP rises with IMF: Ne &lt; O₂ &lt; N(CH₃)₃ &lt; NaCl &lt; CaO (2+/2− beats 1+/1−). HF high BP = H-bonds. IMF are <b>between</b> molecules, never covalent bonds.",
     "V(r): ion–ion ∝ 1/r, ion–dipole 1/r², dipole–dipole 1/r³."),
])

# ---------------------------------------------------------------- PAGE 2
d1 = "".join([
 blk("c-crystal", "Crystal = lattice + motif",
     "Lattice: periodic array of <b>equivalent</b> points; motif/basis: what sits at each. Honeycomb = hex lattice + 2-atom motif. 7 systems / <b>14 Bravais</b> (3 cubic, 2 tetr., 4 orthorh., 2 monocl., 1 hex., 1 rhombo., 1 tricl.). 2D: oblique, rect., square, hex.",
     "Cubic a=b=c, 90°. Tetr. a=b≠c. Hex γ=120°. Rhombo a=b=c, α=β=γ≠90°."),
 blk("c-crystal", "Cubic cells",
     table(["","SC","BCC","FCC"],
           [["pts/cell","1","2","4"],["atoms touch along","edge","body diag.","face diag."],["a(r)","2r","4r/√3","2√2 r"],["packing","0.52","0.68","0.74"],["nn dist.","a","a√3/2","a/√2"],["# nn","6","8","12"]]),
     "EQ:ρ = (points·M) / (N<sub>A</sub>·a³) &nbsp; packing = N·(4/3)πr³ / a³",
     "Corner 1/8, face 1/2, edge 1/4, body 1. FCC = ABCABC (CCP), HCP = ABAB; both 74%, 12 nn."),
 blk("c-crystal", "Structures",
     "<b>NaCl</b>: FCC, 4Na+4Cl (8 ions), oct. holes. <b>CsCl</b>: <b>simple cubic</b>, 2-ion motif, 8-fold. <b>ZnS</b>: FCC S, Zn in ½ tetr. holes (8 ions). <b>CaF₂</b>: FCC, 4Ca+8F (12). <b>CaTiO₃</b> perovskite: Ca corners, Ti centre, O faces. Per FCC cell: 4 oct., 8 tetr. holes. 1:1 ratio necessary, not sufficient for rock salt.",
     "Au: a = 407 pm → r = 144 pm. Fe BCC a = 2.86 Å (r 1.24). Cu FCC a = 3.61 Å."),
])
d2 = "".join([
 blk("c-crystal", "Miller indices &amp; families",
     "Intercepts (in a,b,c) → reciprocals → clear fractions → (hkl). ∞→0. Negative: bar. (hkl) plane, {hkl} family, [uvw] direction, &lt;uvw&gt; family, point x,y,z. Cubic only: (hkl) ⊥ [hkl].",
     table(["family","count"],[["&lt;100&gt;","6 dirs"],["&lt;110&gt;","12 dirs"],["&lt;111&gt;","8 dirs"],["{100}","6 faces (3 orient.)"],["{110}","6 planes"],["{111}","4 planes"]]),
     "Planar density: sketch plane, atoms inside (corner ¼, edge ½), ÷ area. BCC (110): 2 atoms / (a·a√2). FCC (100): 2 / a². FCC (111) densest, BCC (110) densest.",
     "Slip: FCC {111}&lt;110&gt;; BCC {110}&lt;111&gt;."),
 blk("c-crystal", "Diffraction",
     "EQ:d<sub>hkl</sub> = a/√(h²+k²+l²) (cubic) &nbsp; 2d sinθ = nλ",
     "θ = glancing angle; patterns plot <b>2θ</b> → halve! Cu Kα 1.54 Å = 0.154 nm. Calc in degree mode. d<sub>220</sub> = d<sub>110</sub>/2. r (atom), a (cell edge), d (plane spacing) are different.",
     "<b>Selection rules</b>: SC all · <b>BCC h+k+l even</b> (110, 200, 211, 220…) · <b>FCC all odd or all even</b> (111, 200, 220, 311, 222…).",
     "sin²θ ∝ h²+k²+l²: SC 1:2:3:4:5:6:8 · BCC 2:4:6:8:10:12 · FCC <b>3:4:8:11:12:16</b>. Powder peaks give structure; peak angle gives a.",
     "Example: λ=1.54 Å, Fe BCC a=2.866 → d₁₁₀=2.03, θ=22.3°, 2θ=44.7°."),
])
d3 = "".join([
 blk("c-defect", "Defects",
     "<b>Point (0D)</b>: vacancy · interstitial (small atom, C in Fe) · substitutional (similar size, Zn in Cu, dopants). Ionic: <b>Schottky</b> = cation + anion vacancy pair; <b>Frenkel</b> = ion moves to a gap (vacancy + interstitial, usually cation). <b>Line (1D)</b>: edge dislocation ⊥ = extra half-plane; moves along slip plane → plastic deformation at 10³–10⁴× lower stress. <b>Planar (2D)</b>: grain boundary; polycrystal vs single crystal.",
     "<b>Work hardening</b>: more, tangled dislocations → harder, more brittle. <b>Anything blocking dislocations hardens</b> (alloy atoms, C in steel, hammering). <b>Annealing</b>: heat (no melting) → diffusion removes dislocations → softer, tougher."),
 blk("c-defect", "Glass &amp; polymers",
     "Amorphous: no long-range order; forms if structure packs badly or cools fast. SiO₄ tetrahedron: Si–O 162 pm, 109.5°; quartz periodic, glass random. <b>Network modifiers</b> (Na, Ca) → non-bridging O → lower softening T (soda-lime &lt; borosilicate &lt; 96% silica &lt; fused silica). No sharp melting: viscosity falls smoothly.",
     "Faster cooling → <b>higher molar volume, higher T<sub>g</sub></b>; crystal drops suddenly at T<sub>m</sub>. Polymers: monomers → chains; crosslink (S, vulcanization) → does not melt; HDPE semicrystalline."),
 blk("c-diff", "Diffusion",
     "EQ:J = −D dC/dx &nbsp; D = D₀ exp(−Q/RT) &nbsp; x ≈ √(Dt)",
     "ln D vs 1/T: slope = <b>−Q/R</b> (steeper = larger Q; use J/mol). Q = R ln(D₂/D₁)/(1/T₁−1/T₂). D ↑ strongly with T. <b>Interstitial</b> (C, H in Fe): low Q, fast. <b>Vacancy / self</b> (Fe in Fe): high Q, Q<sub>v</sub> ↑ with T<sub>m</sub>. Fick 2nd: ∂C/∂t = D ∂²C/∂x² (profile changes with time); surface at fixed C → erfc profile; depth ∝ √t.",
     "Flux ×area = rate (doors: D·ΔC/Δx·A)."),
])

def sheet(title, sub, cols):
    return ('<div class="sheet"><div class="head"><div class="t1">%s</div><div class="t2">%s</div></div><div class="cols">%s</div></div>'
            % (title, sub, "".join('<div class="col">%s</div>' % c for c in cols)))

body = ('<body>\n<div class="screen-chrome"><h1>3.091 &mdash; Exam 2 Aid Sheet (front and back)</h1>'
        '<p>L10&ndash;L20 &middot; Rec 7&ndash;13. Print double-sided on letter paper at <span class="kbd">100%</span> scale, margins none, background graphics on. '
        'Check that this year&rsquo;s rules allow a double-sided sheet; page 1 stands alone if only one side is allowed.</p></div>\n'
        + sheet("3.091 Exam 2 &middot; side 1", "<b>Covalent bonding &rarr; VSEPR &rarr; orbitals &rarr; forces &rarr; bands &amp; semiconductors</b> (L10&ndash;L15)", [c1, c2, c3])
        + "\n"
        + sheet("3.091 Exam 2 &middot; side 2", "<b>Crystals &rarr; diffraction &rarr; defects &rarr; glass &amp; polymers &rarr; diffusion</b> (L16&ndash;L20)", [d1, d2, d3])
        + "\n</body>\n</html>\n")
open(os.path.join(ROOT, "aid-sheet-exam2.html"), "w", encoding="utf-8").write(head + body)
print("wrote aid-sheet-exam2.html")
