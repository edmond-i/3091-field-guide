"""Figures for the hybridization walkthrough (Unit 06), intermolecular forces (Unit 07)
and metals / bands (Unit 08).  Usage:  python3 tools/gen_new_figures.py OUT_DIR
Writes one .html snippet per figure (inline SVG, themed with CSS variables).
Phase colours: blue = +, red = -  (phase of the wave, NOT electric charge).
"""
import math
import os
import sys


def f(v):
    return f"{v:.1f}"


def svg(w, h, label, inner, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}"{c}>{inner}</svg>'


def T(x, y, s, cls="fm-t", anchor="middle", extra=""):
    return f'<text class="{cls}" x="{f(x)}" y="{f(y)}" text-anchor="{anchor}"{extra}>{s}</text>'


def L(x1, y1, x2, y2, cls):
    return f'<line class="{cls}" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>'


def E(cx, cy, rx, ry, cls, extra=""):
    return f'<ellipse class="{cls}" cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}"{extra}/>'


def C(cx, cy, r, cls):
    return f'<circle class="{cls}" cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"/>'


def R(x, y, w, h, cls, rx=0):
    return f'<rect class="{cls}" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{rx}"/>'


MARK = ('<defs><marker id="{id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto"><path d="M0,0L10,5L0,10z" class="{c}"/></marker></defs>')


# ------------------------------------------------------------------ spin arrows
def spin_up(x, y):
    return f'<path class="fm-sp" d="M{f(x)},{f(y + 9)} V{f(y - 9)} M{f(x - 3.4)},{f(y - 5)} L{f(x)},{f(y - 9)} L{f(x + 3.4)},{f(y - 5)}"/>'


def spin_dn(x, y):
    return f'<path class="fm-sp" d="M{f(x)},{f(y - 9)} V{f(y + 9)} M{f(x - 3.4)},{f(y + 5)} L{f(x)},{f(y + 9)} L{f(x + 3.4)},{f(y + 5)}"/>'


def obox(x, y, spin, cls="fm-box"):
    out = R(x, y, 30, 30, cls, 4)
    cx, cy = x + 15, y + 15
    if spin == "ud":
        out += spin_up(cx - 5, cy) + spin_dn(cx + 5, cy)
    elif spin == "u":
        out += spin_up(cx, cy)
    return out


# =================================================================== HYBRIDIZATION
def hy_promote():
    W, H = 760, 300
    o = [MARK.format(id="hpA", c="fm-arrow-h")]
    o.append('<path class="fm-ax" d="M16,278 V40 M11,48 L16,38 L21,48"/>')
    o.append(T(6, 26, "energy", "fm-ax-t", "start"))
    c1, c2, c3 = 140, 390, 640
    yp, ys, yh = 82, 190, 136
    for c, t in ((c1, "1  Ground-state carbon"), (c2, "2  Promote one electron"), (c3, "3  Mix into four hybrids")):
        o.append(T(c, 30, t, "fm-h"))
    # column 1
    for i, sp in enumerate(("u", "u", "")):
        o.append(obox(c1 - 51 + 36 * i, yp, sp))
    o.append(obox(c1 - 15, ys, "ud"))
    o.append(T(c1 - 62, yp + 20, "2p", "fm-ao", "end") + T(c1 - 26, ys + 20, "2s", "fm-ao", "end"))
    for i, (t, cl) in enumerate((("only 2 unpaired electrons", "fm-cap"), ("so only 2 bonds?", "fm-cap-s"), ("(and p orbitals are 90&deg; apart)", "fm-cap-s"))):
        o.append(T(c1, 252 + 17 * i, t, cl))
    # column 2
    for i, sp in enumerate(("u", "u")):
        o.append(obox(c2 - 51 + 36 * i, yp, sp))
    o.append(obox(c2 + 21, yp, "u", "fm-box fm-box-hi"))
    o.append(obox(c2 - 15, ys, "u"))
    o.append(T(c2 - 62, yp + 20, "2p", "fm-ao", "end") + T(c2 - 26, ys + 20, "2s", "fm-ao", "end"))
    o.append(f'<path class="fm-curve" d="M{c2},{ys - 3} C{c2},{yp + 70} {c2 + 36},{yp + 78} {c2 + 36},{yp + 34}" marker-end="url(#hpA)"/>')
    for i, (t, cl) in enumerate((("4 unpaired electrons", "fm-cap"), ("promotion costs a little energy,", "fm-cap-s"), ("repaid by two extra bonds", "fm-cap-s"))):
        o.append(T(c2, 252 + 17 * i, t, cl))
    # column 3
    for i in range(4):
        o.append(obox(c3 - 69 + 36 * i, yh, "u", "fm-box fm-box-hy"))
    o.append(T(c3, yh + 52, "four identical sp&sup3; hybrids", "fm-hy-t"))
    for i, (t, cl) in enumerate((("4 equal bonds, 109.5&deg;", "fm-cap"), ("1 s + 3 p orbitals in", "fm-cap-s"), ("= 4 hybrid orbitals out", "fm-cap-s"))):
        o.append(T(c3, 252 + 17 * i, t, cl))
    o.append(f'<path class="fm-big-arrow" d="M{c1 + 84},150 H{c2 - 92}" marker-end="url(#hpA)"/>')
    o.append(f'<path class="fm-big-arrow" d="M{c2 + 84},150 H{c3 - 100}" marker-end="url(#hpA)"/>')
    return svg(W, H, "Carbon starts with two unpaired electrons; one 2s electron is promoted to give four unpaired electrons; the 2s and three 2p orbitals then mix into four identical sp3 hybrid orbitals each holding one electron.", "".join(o))


def _pill(cx, cy, flip=False):
    """polar molecule: red delta+ half, blue delta- half"""
    lp, rp = ("pl-neg", "pl-pos") if flip else ("pl-pos", "pl-neg")
    l = f'<path class="{lp}" d="M{cx},{cy - 9} H{cx - 13} a9,9 0 0 0 0,18 H{cx} Z"/>'
    r = f'<path class="{rp}" d="M{cx},{cy - 9} H{cx + 13} a9,9 0 0 1 0,18 H{cx} Z"/>'
    tl, tr = ("&delta;&minus;", "&delta;+") if flip else ("&delta;+", "&delta;&minus;")
    return l + r + T(cx - 12, cy + 3, tl, "pl-t") + T(cx + 12, cy + 3, tr, "pl-t")


def hy_shape():
    W, H = 640, 312
    o = []

    def row(y, sign, label):
        o.append(C(70, y, 26, "ph-pos"))
        o.append(T(70, y + 4, "s", "fm-orb-t"))
        o.append(T(128, y + 5, "+" if sign > 0 else "&minus;", "fm-op"))
        o.append(E(190, y, 23, 16, "ph-neg") + E(236, y, 23, 16, "ph-pos") + C(213, y, 2.4, "ph-nuc"))
        o.append(T(213, y + 38, "p", "fm-orb-t"))
        o.append(T(300, y + 5, "=", "fm-op"))
        dx = 1 if sign > 0 else -1
        nx = 420
        o.append(E(nx - dx * 18, y, 17, 11, "ph-neg") + E(nx + dx * 40, y, 44, 27, "ph-pos") + C(nx, y, 2.6, "ph-nuc"))
        o.append(T(nx, y + 50, label, "fm-orb-t"))

    row(62, +1, "sp hybrid #1 (points right)")
    row(176, -1, "sp hybrid #2 (points left)")
    o.append(T(320, 250, "Where the signs match the waves add: the big lobe.", "fm-cap-s"))
    o.append(T(320, 268, "Where they oppose they partly cancel: the small lobe.", "fm-cap-s"))
    o.append(T(320, 294, "2 orbitals in (s &plusmn; p) &rarr; 2 hybrids out, opposite directions: linear, 180&deg;", "fm-cap"))
    return svg(W, H, "An s orbital added to a p orbital gives an sp hybrid: a large lobe on one side where the signs match and a small lobe on the other where they oppose. Subtracting the p instead gives the mirror-image hybrid pointing the other way.", "".join(o))


def hy_ethene():
    W, H = 680, 300
    o = []
    # --- top view
    o.append(T(160, 24, "Top view: the flat sigma framework", "fm-h"))
    c1, c2, cy = (110, 210), (210, 210), 120
    x1, x2 = 105, 215
    pts = [(x1, cy, x2, cy)]
    for sx, sgn in ((x1, -1), (x2, +1)):
        for a in (60, -60):
            ex = sx + sgn * 52 * math.cos(math.radians(a))
            ey = cy - 52 * math.sin(math.radians(a))
            pts.append((sx, cy, ex, ey))
    for (a, b, c, d) in pts:
        o.append(L(a, b, c, d, "fm-sigma"))
    for (a, b, c, d) in pts[1:]:
        pass
    for sx in (x1, x2):
        o.append(C(sx, cy, 11, "sv-center"))
        o.append(T(sx, cy + 4, "C", "sv-txt-w"))
    for (a, b, c, d) in pts[1:]:
        o.append(C(c, d, 8, "at-h"))
        o.append(T(c, d + 3, "H", "fm-tiny"))
    o.append(T(160, 236, "each C: 3 sp&sup2; hybrids, 120&deg; apart", "fm-cap-s"))
    o.append(T(160, 254, "(2 C&ndash;H bonds + the C&ndash;C bond)", "fm-cap-s"))
    o.append(T(160, 278, "= sigma bonds, head-on overlap", "fm-cap"))
    # --- side view
    o.append(T(500, 24, "Side view: the leftover p orbitals", "fm-h"))
    ax, bx, sy = 430, 570, 130
    o.append(L(380, sy, 620, sy, "ph-node"))
    o.append(E(ax, sy - 42, 30, 38, "ph-pos") + E(bx, sy - 42, 30, 38, "ph-pos"))
    o.append(E(ax, sy + 42, 30, 38, "ph-neg") + E(bx, sy + 42, 30, 38, "ph-neg"))
    o.append(E((ax + bx) / 2, sy - 40, 82, 30, "ph-pos", ' fill-opacity="0.25"'))
    o.append(E((ax + bx) / 2, sy + 40, 82, 30, "ph-neg", ' fill-opacity="0.25"'))
    o.append(L(ax, sy, bx, sy, "fm-sigma"))
    for sx in (ax, bx):
        o.append(C(sx, sy, 10, "sv-center"))
        o.append(T(sx, sy + 4, "C", "sv-txt-w"))
    o.append(T(500, 236, "the unmixed p orbitals overlap sideways", "fm-cap-s"))
    o.append(T(500, 254, "density above and below the plane", "fm-cap-s"))
    o.append(T(500, 278, "= one pi bond", "fm-cap"))
    o.append(T(618, sy - 6, "plane", "fm-tiny", "end"))
    return svg(W, H, "Ethene: each carbon uses three sp2 hybrids to make three sigma bonds in one plane, and its one leftover unmixed p orbital overlaps sideways with the other carbon's to make a pi bond above and below the plane.", "".join(o))


# =================================================================== INTERMOLECULAR FORCES
def ip_dipoles():
    cells = []

    def mk(c, i):
        return (f'<defs><marker id="{c}-{i}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" '
                f'orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="{c}"/></marker></defs>')

    def arrows(kind, i, xs, ys):
        c = "fm-attr" if kind == "a" else "fm-rep"
        out = ""
        for (x1, y1, x2, y2) in xs:
            out += (f'<path class="{c}" d="M{x1},{y1} L{x2},{y2}" marker-end="url(#{c}-h-{i})" marker-start="url(#{c}-h-{i})"/>')
        return out

    specs = [
        ("Side by side, opposite ways", "attract", "a", [(60, 36, False), (60, 78, True)], [(48, 52, 48, 62), (72, 52, 72, 62)]),
        ("Head to tail", "attract", "a", [(32, 55, False), (88, 55, False)], [(52, 55, 66, 55)]),
        ("Side by side, same way", "repel", "r", [(60, 36, False), (60, 78, False)], [(48, 52, 48, 62), (72, 52, 72, 62)]),
        ("Head to head", "repel", "r", [(32, 55, False), (88, 55, True)], [(52, 55, 66, 55)]),
    ]
    for i, (title, verdict, kind, pills, arr) in enumerate(specs):
        c = "fm-attr" if kind == "a" else "fm-rep"
        defs = (f'<defs><marker id="{c}-h-{i}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" '
                f'orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="{c}-h"/></marker></defs>')
        body = defs + "".join(_pill(x, y, fl) for (x, y, fl) in pills) + arrows(kind, i, arr, None)
        cells.append(
            f'<div class="gp-cell"><svg viewBox="0 0 120 110" role="img" aria-label="{title}: {verdict}">{body}</svg>'
            f'<div class="vs-name">{title}</div><div class="dp-verdict {"dp-net" if kind == "a" else "dp-zero"}">{verdict}</div></div>')
    return '<div class="gp-row ip-row">' + "".join(cells) + '</div>'


def _water(cx, cy, hs, cls_o="at-o"):
    out = ""
    for (hx, hy) in hs:
        out += L(cx, cy, hx, hy, "fm-bond")
    out += C(cx, cy, 10, cls_o) + T(cx, cy + 3.5, "O", "sv-txt-w")
    for (hx, hy) in hs:
        out += C(hx, hy, 6.5, "at-h")
    return out


def ip_hbond():
    W, H = 640, 256
    o = []
    o.append(_water(120, 120, [(188, 120), (92, 62)]))
    ox, oy = 340, 120
    o.append(E(ox - 34, oy - 20, 15, 9, "sv-lp", ' transform="rotate(-30 %s %s)"' % (f(ox - 34), f(oy - 20))))
    o.append(E(ox - 34, oy + 20, 15, 9, "sv-lp", ' transform="rotate(30 %s %s)"' % (f(ox - 34), f(oy + 20))))
    o.append(_water(ox, oy, [(ox + 52, oy - 52), (ox + 52, oy + 52)]))
    o.append(L(196, 120, ox - 14, 120, "hb-dot"))
    o.append(L(120, 170, 188, 170, "fm-dim") + T(154, 190, "X&ndash;H &asymp; 1.1 &Aring;", "fm-note"))
    o.append(L(196, 170, ox - 14, 170, "fm-dim hb-dim") + T(268, 190, "H&middot;&middot;&middot;Y &asymp; 1.5&ndash;2.0 &Aring;", "fm-note"))
    o.append(T(120, 34, "donor", "fm-h") + T(120, 50, "the H sits on N, O or F", "fm-note"))
    o.append(T(ox, 34, "acceptor", "fm-h") + T(ox, 50, "has a lone pair to point at", "fm-note"))
    o.append(T(236, 104, "hydrogen bond", "fm-hb-t"))
    o.append(T(320, 218, "dots = hydrogen bond;  solid line = covalent bond", "fm-cap-s"))
    o.append(T(320, 236, "It is directional: the H points straight at the lone pair.", "fm-cap-s"))
    return svg(W, H, "A hydrogen bond: the hydrogen on one molecule (the donor, attached to N, O or F) is attracted to a lone pair on a neighbor (the acceptor). The H to lone-pair distance is about 1.5 to 2.0 angstroms, compared with about 1.1 for the covalent X to H.", "".join(o))


def ip_water4():
    W, H = 420, 360
    o = []
    cx, cy = 210, 170
    o.append(E(186, 140, 16, 9, "sv-lp", ' transform="rotate(-40 186 140)"') + E(234, 140, 16, 9, "sv-lp", ' transform="rotate(40 234 140)"'))
    o.append(_water(cx, cy, [(158, 222), (262, 222)]))
    o.append(_water(92, 284, [(56, 260), (120, 318)]))
    o.append(_water(328, 284, [(364, 260), (300, 318)]))
    o.append(L(153, 229, 100, 277, "hb-dot") + L(267, 229, 320, 277, "hb-dot"))
    o.append(_water(88, 52, [(122, 86), (62, 24)]))
    o.append(_water(332, 52, [(298, 86), (358, 24)]))
    o.append(L(127, 91, 172, 130, "hb-dot") + L(293, 91, 248, 130, "hb-dot"))
    o.append(T(210, 36, "receives 2 (on its lone pairs)", "fm-note", "middle", ' fill="var(--unit-forces)"'))
    o.append(T(210, 352, "gives 2 (from its two H atoms)", "fm-note", "middle", ' fill="var(--unit-forces)"'))
    return svg(W, H, "One water molecule can donate two hydrogen bonds from its two hydrogens and accept two hydrogen bonds on its two lone pairs, so up to four hydrogen bonds per molecule.", "".join(o))


def _chart_frame(W, H, L_, R_, T_, B_, xticks, yticks, xmap, ymap, xlab, ylab, ysuffix=""):
    o = []
    for v in yticks:
        y = ymap(v)
        o.append(L(L_, y, W - R_, y, "ic-grid" if v != 0 else "ic-axis"))
        o.append(T(L_ - 8, y + 4, f"{v}{ysuffix}", "ic-tick", "end"))
    for v, lbl in xticks:
        o.append(T(xmap(v), H - B_ + 18, lbl, "ic-tick"))
    o.append(T((L_ + W - R_) / 2, H - 6, xlab, "ic-lab"))
    o.append(f'<text class="ic-lab" x="14" y="{f((T_ + H - B_) / 2)}" text-anchor="middle" transform="rotate(-90 14 {f((T_ + H - B_) / 2)})">{ylab}</text>')
    return "".join(o)


def ip_hydride_bp():
    W, H = 640, 380
    L_, R_, T_, B_ = 60, 56, 20, 48
    xm = lambda p: L_ + 50 + (p - 2) * ((W - L_ - R_ - 110) / 3)
    ym = lambda v: T_ + (H - T_ - B_) * (150 - v) / 350
    o = [_chart_frame(W, H, L_, R_, T_, B_, [(p, f"period {p}") for p in (2, 3, 4, 5)],
                      [150, 100, 50, 0, -50, -100, -150, -200], xm, ym, "period of the element bonded to hydrogen", "boiling point (&deg;C)")]
    data = [
        ("Group 14", "hy-g14", [("CH&#8324;", -161), ("SiH&#8324;", -112), ("GeH&#8324;", -88), ("SnH&#8324;", -52)]),
        ("Group 15", "hy-g15", [("NH&#8323;", -33), ("PH&#8323;", -88), ("AsH&#8323;", -62), ("SbH&#8323;", -17)]),
        ("Group 16", "hy-g16", [("H&#8322;O", 100), ("H&#8322;S", -60), ("H&#8322;Se", -41), ("H&#8322;Te", -2)]),
        ("Group 17", "hy-g17", [("HF", 20), ("HCl", -85), ("HBr", -66), ("HI", -36)]),
    ]
    for name, cls, pts in data:
        pl = " ".join(f"{f(xm(2 + i))},{f(ym(v))}" for i, (_, v) in enumerate(pts))
        o.append(f'<polyline class="hy-line {cls}" points="{pl}"/>')
        for i, (lab, v) in enumerate(pts):
            o.append(f'<circle class="hy-pt {cls}" cx="{f(xm(2 + i))}" cy="{f(ym(v))}" r="4"/>')
    # labels for period-2 outliers and group tags at period 5
    for name, cls, pts in data:
        tcls = "hy-t" + cls[-2:]
        lab, v = pts[0]
        o.append(T(xm(2) - 10, ym(v) + 4, lab, f"hy-lab {tcls}", "end"))
        lab5, v5 = pts[3]
        o.append(T(xm(5) + 10, ym(v5) + 4, lab5, f"hy-lab {tcls}", "start"))
    for i, (name, cls, _) in enumerate(data):
        yy = ym(140) + i * 17
        o.append(L(W - R_ - 112, yy, W - R_ - 88, yy, f"hy-line {cls}"))
        o.append(T(W - R_ - 80, yy + 4, name, "fm-note", "start"))
    o.append(T(xm(2) + 24, ym(128), "NH&#8323;, H&#8322;O, HF: hydrogen bonding", "fm-note", "start"))
    o.append(T(xm(3.0), ym(-172), "no H bond: smooth rise with size", "fm-note", "start"))
    return svg(W, H, "Boiling points of hydrogen compounds of groups 14 to 17 by period. Group 14 rises smoothly with size, while NH3, H2O and HF are far above the trend because of hydrogen bonding.", "".join(o))


def ip_alkane_bp():
    W, H = 640, 340
    L_, R_, T_, B_ = 64, 28, 18, 52
    xm = lambda m: L_ + (W - L_ - R_) * m / 180
    ym = lambda v: T_ + (H - T_ - B_) * (250 - v) / 460
    data = [("CH&#8324;", 16, -161.5), ("C&#8322;H&#8326;", 30, -88.6), ("C&#8323;H&#8328;", 44, -42.1),
            ("C&#8324;H&#8321;&#8320;", 58, -0.5), ("C&#8325;H&#8321;&#8322;", 72, 36.1), ("C&#8326;H&#8321;&#8324;", 86, 68.7),
            ("C&#8327;H&#8321;&#8326;", 100, 98.4), ("C&#8328;H&#8321;&#8328;", 114, 125.7), ("C&#8329;H&#8322;&#8320;", 128, 150.8),
            ("C&#8321;&#8320;H&#8322;&#8322;", 142, 174.1), ("C&#8321;&#8322;H&#8322;&#8326;", 170, 216.3)]
    o = [R(L_, ym(25), W - L_ - R_, ym(-210) - ym(25), "ic-band"),
         _chart_frame(W, H, L_, R_, T_, B_, [(m, str(m)) for m in range(20, 181, 20)],
                      [250, 200, 150, 100, 50, 0, -50, -100, -150, -200], xm, ym, "molecular weight (g/mol)", "boiling point (&deg;C)")]
    o.append(L(L_, ym(25), W - R_, ym(25), "fm-dim"))
    o.append(T(W - R_ - 6, ym(25) - 6, "room temperature (25 &deg;C)", "fm-note", "end"))
    o.append(T(W - R_ - 8, ym(-185), "gases at room temperature", "fm-note", "end"))
    o.append(T(L_ + 12, ym(235), "liquids, then waxy solids (above the dashed line)", "fm-note", "start"))
    pl = " ".join(f"{f(xm(m))},{f(ym(v))}" for _, m, v in data)
    o.append(f'<polyline class="ic-curve" points="{pl}"/>')
    for i, (lab, m, v) in enumerate(data):
        o.append(f'<circle class="ic-pt" cx="{f(xm(m))}" cy="{f(ym(v))}" r="4"/>')
        if i == 10:
            o.append(T(xm(m) - 10, ym(v) - 8, lab, "ic-pt-t", "end"))
        elif i in (0, 1, 2, 3, 4, 6, 8):
            o.append(T(xm(m) + 8, ym(v) + (14 if i < 5 else 16), lab, "ic-pt-t", "start"))
    return svg(W, H, "Boiling points of straight-chain alkanes rise steadily with molecular weight: methane to butane are gases at room temperature, pentane and heavier are liquids, and the heaviest become waxy solids.", "".join(o))


def ip_shape():
    W, H = 600, 250
    o = [T(150, 24, "Compact: neopentane, 72 g/mol", "fm-h"), T(450, 24, "Long: n-pentane, 72 g/mol", "fm-h")]
    # neopentane x2 (touch at a point)
    def neo(cx, cy):
        r = ""
        for dx, dy in ((0, -22), (0, 22), (-22, 0), (22, 0)):
            r += L(cx, cy, cx + dx, cy + dy, "fm-bond")
        r += C(cx, cy, 9, "at-c")
        for dx, dy in ((0, -22), (0, 22), (-22, 0), (22, 0)):
            r += C(cx + dx, cy + dy, 9, "at-c")
        return r

    o.append(neo(150, 85) + neo(150, 165))
    o.append(C(150, 125, 7, "fm-contact"))
    o.append(T(150, 215, "small contact area", "fm-cap-s"))
    o.append(T(150, 234, "boils at 9.5 &deg;C", "fm-cap"))
    # n-pentane zig-zag x2 (long contact)
    def pent(x0, y0):
        pts = [(x0 + i * 26, y0 + (0 if i % 2 == 0 else 12)) for i in range(5)]
        r = ""
        for a, b in zip(pts, pts[1:]):
            r += L(a[0], a[1], b[0], b[1], "fm-bond")
        for p in pts:
            r += C(p[0], p[1], 9, "at-c")
        return r

    o.append(pent(385, 90) + pent(385, 130))
    o.append(f'<rect class="fm-contact-bar" x="372" y="103" width="126" height="14" rx="7"/>')
    o.append(T(450, 215, "long contact area", "fm-cap-s"))
    o.append(T(450, 234, "boils at 36.1 &deg;C", "fm-cap"))
    return svg(W, H, "Two isomers of C5H12 with the same mass: compact neopentane touches a neighbor at one point and boils at 9.5 C, while the long n-pentane lies alongside a neighbor over its whole length and boils at 36.1 C.", "".join(o))


def ip_instant():
    W, H = 760, 310
    o = [MARK.format(id="idA", c="fm-arrow-h")]
    rows = [
        (60, 0, 0, "1  Neutral atoms", ["On average each electron cloud is centered", "on its nucleus: no dipole."]),
        (158, 10, 0, "2  A fluctuation", ["Atom A's cloud sloshes to one side:", "an instantaneous dipole."]),
        (256, 10, 10, "3  An induced dipole", ["A's &delta;&minus; end pushes B's electrons away, so B's", "near side turns &delta;+. The two dipoles attract."]),
    ]
    for y, sa, sb, title, notes in rows:
        ax, bx = 100, 230
        o.append(C(ax + sa, y, 30, "cl-cloud") + C(ax, y, 3, "ph-nuc"))
        o.append(C(bx + sb, y, 30, "cl-cloud") + C(bx, y, 3, "ph-nuc"))
        if sa:
            o.append(T(ax - 20, y - 38, "&delta;+", "fm-note") + T(ax + 42, y - 38, "&delta;&minus;", "fm-note"))
        if sb:
            o.append(T(bx - 20, y - 38, "&delta;+", "fm-note") + T(bx + 42, y - 38, "&delta;&minus;", "fm-note"))
        o.append(T(340, y - 8, title, "fm-h", "start"))
        for i, n in enumerate(notes):
            o.append(T(340, y + 10 + 16 * i, n, "fm-note", "start"))
    o.append('<path class="fm-attr" d="M168,256 H196" marker-end="url(#idA)"/>')
    return svg(W, H, "Dispersion forces in three steps: neutral atoms, then a momentary fluctuation of one electron cloud creating an instantaneous dipole, then that dipole inducing an opposite dipole in the neighboring atom so they attract.", "".join(o))


# =================================================================== METALS & BANDS
def mt_band():
    W, H = 820, 420
    o = []
    y0, k = 160, 62     # y of zero energy, and pixels per unit of |beta|
    o.append('<path class="fm-ax" d="M24,300 V20 M19,28 L24,18 L29,28"/>')
    o.append(T(10, 12, "energy", "fm-ax-t", "start"))
    for n, x in [(1, 80), (2, 170), (4, 260), (6, 350), (10, 440)]:
        o.append(T(x, 318, f"{n}", "ic-tick"))
        for kk in range(1, n + 1):
            # simple chain model: E_k = -2cos(k*pi/(n+1)); k=1 is the lowest (most bonding) level
            e = -2 * math.cos(kk * math.pi / (n + 1)) if n > 1 else 0.0
            y = y0 - k * e
            filled = (n == 1) or (kk <= n / 2)
            cls = "bd-lv bd-fill" if filled else "bd-lv"
            o.append(f'<line class="{cls}" x1="{x - 18}" y1="{f(y)}" x2="{x + 18}" y2="{f(y)}"/>')
    o.append(T(260, 345, "number of atoms in the chain  &rarr;", "ic-lab"))
    bx, bw = 600, 70
    top, bot = y0 - 2 * k - 6, y0 + 2 * k + 6
    o.append(R(bx, top, bw, y0 - top, "bd-empty") + R(bx, y0, bw, bot - y0, "bd-filled"))
    o.append(T(bx + bw / 2, (top + y0) / 2 + 4, "empty", "bd-blk-t"))
    o.append(T(bx + bw / 2, (y0 + bot) / 2 + 4, "filled", "bd-blk-t"))
    o.append(T(bx + bw / 2, 318, "~10&sup2;&sup3;", "ic-tick"))
    o.append(T(bx + bw / 2, top - 8, "a band", "fm-h"))
    o.append(f'<path class="fm-dim" d="M{bx + bw + 14},{f(top)} V{f(bot)}"/>')
    o.append(T(bx + bw + 20, y0 + 4, "bandwidth", "fm-note", "start"))

    def chain(y, signs, label):
        r = ""
        for i, sgn in enumerate(signs):
            r += C(190 + i * 30, y, 11, "ph-pos" if sgn > 0 else "ph-neg")
        for i in range(len(signs) - 1):
            if signs[i] != signs[i + 1]:
                r += L(190 + i * 30 + 15, y - 15, 190 + i * 30 + 15, y + 15, "ph-node")
        r += T(30, y + 4, label, "fm-note", "start")
        return r

    o.append(chain(375, [1, 1, 1, 1, 1, 1], "lowest level:"))
    o.append(T(400, 379, "all in phase, no nodes: most bonding", "fm-note", "start"))
    o.append(chain(405, [1, -1, 1, -1, 1, -1], "highest level:"))
    o.append(T(400, 409, "signs alternate, a node between every pair: most antibonding", "fm-note", "start"))
    return svg(W, H, "Molecular orbitals of a chain of n atoms with one s electron each: the n levels spread out as n grows, and for a macroscopic crystal they merge into a continuous band whose lower half is filled and upper half empty.", "".join(o))


def mt_namgal():
    W, H = 700, 360
    o = []
    o.append('<path class="fm-ax" d="M20,336 V40 M15,48 L20,38 L25,48"/>')
    o.append(T(8, 26, "energy", "fm-ax-t", "start"))
    cx = 84
    o.append(T(cx + 40, 204, "core bands (full)", "fm-note"))
    for lbl, y, h in (("2p", 216, 52), ("2s", 278, 18), ("1s", 306, 14)):
        o.append(R(cx, y, 80, h, "bd-filled") + T(cx + 40, y + h / 2 + 4, lbl, "bd-blk-t"))
    o.append(T(cx + 40, 340, "narrow, deep, with gaps", "fm-note"))
    top, bot = 44, 184
    sp = bot - top
    for name, ne, x in (("Na", 1, 260), ("Mg", 2, 390), ("Al", 3, 520)):
        o.append(R(x, top, 100, sp * 0.62, "bd-3p"))
        o.append(R(x, top + sp * 0.38, 100, sp * 0.62, "bd-3s"))
        fh = sp * ne / 8
        o.append(R(x, bot - fh, 100, fh, "bd-filled-hi"))
        o.append(T(x + 50, bot + 22, name, "fm-h"))
        o.append(T(x + 50, bot + 40, f"{ne} e&#8315; / atom", "fm-note"))
    o.append(T(630, top + 12, "3p", "fm-note", "start"))
    o.append(T(630, (top + bot) / 2 + 4, "overlap", "fm-note", "start"))
    o.append(T(630, bot - 6, "3s", "fm-note", "start"))
    o.append(T(440, 292, "3s and 3p overlap, so the 1, 2 or 3 valence electrons per atom", "fm-cap-s"))
    o.append(T(440, 309, "just fill the bottom of one merged band (dark = occupied):", "fm-cap-s"))
    o.append(T(440, 330, "there are always empty levels right above &rarr; metal", "fm-cap"))
    return svg(W, H, "Schematic energy bands of sodium, magnesium and aluminium: narrow filled core bands separated by gaps, and a merged overlapping 3s and 3p valence band that is only partly filled by one, two or three valence electrons per atom, so there are always empty states just above.", "".join(o))


def mt_gap():
    W, H = 760, 290
    o = ['<defs><marker id="gapA" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>']
    panels = [(40, "Metal", "no gap: filled and empty", "levels touch or overlap", "e.g. Na, Cu"),
              (290, "Semiconductor", "small gap", "", "e.g. Si, 1.1 eV"),
              (540, "Insulator", "large gap", "", "e.g. diamond, 5.4 eV")]
    for x, name, n1, n2, ex in panels:
        o.append(T(x + 100, 24, name, "fm-h"))
        o.append('<path class="fm-ax" d="M%d,230 V44 M%d,52 L%d,42 L%d,52"/>' % (x, x - 4, x, x + 4))
        o.append(T(x + 100, 252, n1, "fm-cap-s"))
        o.append(T(x + 100, 268 if n2 else 268, n2 if n2 else ex, "fm-cap-s"))
        if n2:
            o.append(T(x + 100, 284, ex, "fm-cap-s"))
    x = 40
    o.append(R(x + 20, 120, 160, 100, "bd-filled") + R(x + 20, 70, 160, 50, "bd-empty"))
    o.append(R(x + 20, 112, 160, 16, "bd-overlap"))
    o.append(T(x + 100, 176, "filled", "bd-blk-t") + T(x + 100, 96, "empty", "bd-blk-t") + T(x + 100, 124, "overlap", "bd-blk-t"))
    x = 290
    o.append(R(x + 20, 126, 160, 94, "bd-filled") + R(x + 20, 62, 160, 52, "bd-empty"))
    o.append(T(x + 100, 176, "filled", "bd-blk-t") + T(x + 100, 92, "empty", "bd-blk-t"))
    o.append(f'<path class="fm-dim2" d="M{x + 196},114 V126" marker-start="url(#gapA)" marker-end="url(#gapA)"/>')
    o.append(f'<text class="fm-note" x="{x + 204}" y="124">E<tspan class="fm-sub" dy="3">g</tspan></text>')
    x = 540
    o.append(R(x + 20, 170, 160, 50, "bd-filled") + R(x + 20, 56, 160, 40, "bd-empty"))
    o.append(T(x + 100, 200, "filled", "bd-blk-t") + T(x + 100, 80, "empty", "bd-blk-t"))
    o.append(f'<path class="fm-dim2" d="M{x + 196},96 V170" marker-start="url(#gapA)" marker-end="url(#gapA)"/>')
    o.append(f'<text class="fm-note" x="{x + 204}" y="136">E<tspan class="fm-sub" dy="3">g</tspan></text>')
    return svg(W, H, "Band pictures of a metal, a semiconductor and an insulator: a metal has filled and empty states touching or overlapping; a semiconductor has a small gap; an insulator has a large gap between the filled and empty bands.", "".join(o))


def mt_group14():
    W, H = 700, 250
    data = [("C (diamond)", 5.4, "insulator", "gp-ins"), ("Si", 1.1, "semiconductor", "gp-semi"),
            ("Ge", 0.67, "semiconductor", "gp-semi"), ("Sn", 0.08, "semiconductor / metal", "gp-semi"),
            ("Pb", 0.0, "metal", "gp-met")]
    o = []
    x0, sc = 130, 50
    for i, (el, eg, kind, cls) in enumerate(data):
        y = 20 + i * 42
        o.append(T(x0 - 12, y + 18, el, "fm-lab-r", "end"))
        w = max(eg * sc, 2)
        o.append(R(x0, y + 4, w, 26, f"gp-bar {cls}", 4))
        o.append(f'<text class="fm-note" x="{f(x0 + w + 10)}" y="{y + 22}">E<tspan class="fm-sub" dy="3">g</tspan><tspan dy="-3"> = {eg:g} eV &middot; {kind}</tspan></text>')
    o.append(L(x0, 12, x0, 232, "ic-axis"))
    o.append(T(x0, 246, "0 eV", "ic-tick"))
    return svg(W, H, "Band gaps down group 14: carbon as diamond 5.4 eV, insulator; silicon 1.1 eV and germanium 0.67 eV, semiconductors; tin 0.08 eV semiconductor or metal; lead 0 eV, a metal.", "".join(o))


def mt_resist():
    rows = [("Silver", 1.6), ("Copper", 1.67), ("Gold", 2.3), ("Aluminum", 2.69), ("Magnesium", 4.4), ("Sodium", 4.61),
            ("Tungsten", 5.5), ("Zinc", 5.92), ("Cobalt", 6.24), ("Nickel", 6.84), ("Cadmium", 7.4), ("Iron", 9.71),
            ("Tin", 12.8), ("Lead", 20.6), ("Uranium", 29), ("Zirconium", 41), ("Manganin (alloy)", 44), ("Titanium", 55),
            ("Lanthanum", 59), ("96% Fe &ndash; 4% Si (alloy)", 62), ("Cerium", 78), ("Nichrome (alloy)", 100)]
    W = 640
    rh = 21
    H = 20 + rh * len(rows) + 34
    x0, sc = 190, 3.6
    o = []
    for i, (nm, v) in enumerate(rows):
        y = 14 + i * rh
        alloy = "alloy" in nm
        cls = "rs-alloy" if alloy else ("rs-top" if i < 3 else "rs-bar")
        o.append(T(x0 - 8, y + 13, nm, "fm-lab-r", "end"))
        o.append(R(x0, y + 2, v * sc, 15, f"gp-bar {cls}", 3))
        o.append(T(x0 + v * sc + 6, y + 14, f"{v:g}", "ic-pt-t", "start"))
    yb = 14 + rh * len(rows) + 6
    o.append(L(x0, 8, x0, yb, "ic-axis"))
    o.append(T(x0 + 150, yb + 20, "resistivity, 10&#8315;&#8312; &Omega;&middot;m  (smaller = better conductor)", "ic-lab"))
    return svg(W, H, "Electrical resistivity of metals and alloys in units of 10 to the minus 8 ohm-metres, sorted from silver 1.6 and copper 1.67 up to nichrome 100; the alloys sit far above the pure metals.", "".join(o))


def mt_workfn():
    W, H = 720, 300
    o = [MARK.format(id="wfA", c="fm-arrow-h")]
    o.append(R(40, 190, 170, 90, "bd-filled") + R(40, 150, 170, 40, "bd-empty"))
    o.append(T(125, 240, "filled levels", "bd-blk-t"))
    o.append(T(125, 174, "empty levels", "bd-blk-t"))
    o.append(L(210, 190, 480, 190, "fm-dim"))
    o.append(L(30, 60, 560, 60, "fm-dim"))
    o.append(T(36, 52, "outside the metal: electron is free (E = 0)", "fm-note", "start"))
    o.append(T(220, 208, "top of the filled levels", "fm-note", "start"))
    o.append('<path class="fm-big-arrow" d="M250,188 V64" marker-end="url(#wfA)"/>')
    o.append(T(262, 120, "&phi;  (work function)", "fm-h", "start"))
    o.append(T(262, 138, "energy to pull the least-bound", "fm-note", "start"))
    o.append(T(262, 154, "electron out of the solid", "fm-note", "start"))
    # photon: starts at the top of the filled levels, longer than phi
    o.append('<path class="fm-photon" d="M480,190 q8,-12 0,-24 q-8,-12 0,-24 q8,-12 0,-24 q-8,-12 0,-24 q8,-12 0,-24 q-8,-12 0,-24 q8,-12 0,-24" marker-end="url(#wfA)"/>')
    o.append(T(480, 214, "photon of energy h&nu;", "fm-h"))
    o.append(T(512, 36, "leftover becomes kinetic", "fm-note", "start"))
    o.append(T(512, 53, "energy:  KE = h&nu; &minus; &phi;", "fm-h", "start"))
    return svg(W, H, "Work function: the energy needed to remove an electron from the solid to outside the metal. A photon of energy h nu supplies it, and any leftover energy appears as the electron's kinetic energy.", "".join(o))


# =================================================================== RECITATION 9 ADDITIONS
def _mo_up(x, y):
    return f'<path class="mo-e" d="M{f(x)},{f(y + 1)} V{f(y - 11)} M{f(x - 2.6)},{f(y - 7.4)} L{f(x)},{f(y - 11)} L{f(x + 2.6)},{f(y - 7.4)}"/>'


def _mo_dn(x, y):
    return f'<path class="mo-e" d="M{f(x)},{f(y - 11)} V{f(y + 1)} M{f(x - 2.6)},{f(y - 3.4)} L{f(x)},{f(y + 1)} L{f(x + 2.6)},{f(y - 3.4)}"/>'


def _mo_level(x1, x2, y, spin, cls="mo-lv"):
    out = f'<line class="{cls}" x1="{f(x1)}" y1="{f(y)}" x2="{f(x2)}" y2="{f(y)}"/>'
    cx = (x1 + x2) / 2
    if spin == "ud":
        out += _mo_up(cx - 4, y) + _mo_dn(cx + 4, y)
    elif spin == "u":
        out += _mo_up(cx, y)
    return out


def _mo_cn(x1, y1, x2, y2):
    return f'<line class="mo-cn" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>'


def _mo_lab(x, y, t, anchor="middle", cls="mo-lab"):
    return f'<text class="{cls}" x="{f(x)}" y="{f(y)}" text-anchor="{anchor}">{t}</text>'


def mo_f2():
    """F2: 14 valence electrons; sigma2p below pi2p; no hybrids used (Recitation 9)."""
    W, H = 560, 380
    yP, yS = 130, 292
    y_ss, y_ps, y_pp, y_p, y_ss2, y_s = 36, 78, 164, 214, 262, 330
    o = ['<path class="mo-ax" d="M14,356 V28 M9,36 L14,26 L19,36"/>', _mo_lab(8, 16, "E", "start")]
    o.append(_mo_lab(78, 22, "F atom", cls="mo-title") + _mo_lab(280, 14, "F&#8322; molecule", cls="mo-title") + _mo_lab(482, 22, "F atom", cls="mo-title"))
    for x0 in (46, 440):
        o.append(_mo_level(x0, x0 + 24, yP, "ud") + _mo_level(x0 + 28, x0 + 52, yP, "ud") + _mo_level(x0 + 56, x0 + 80, yP, "u"))
        o.append(_mo_lab(x0 + 40, yP + 20, "2p", cls="mo-ao"))
    o.append(_mo_level(62, 98, yS, "ud") + _mo_lab(80, yS + 20, "2s", cls="mo-ao"))
    o.append(_mo_level(456, 492, yS, "ud") + _mo_lab(474, yS + 20, "2s", cls="mo-ao"))
    for ym in (y_s, y_ss2):
        o.append(_mo_cn(98, yS, 250, ym) + _mo_cn(456, yS, 310, ym))
    for (ym, xl, xr) in ((y_p, 250, 310), (y_ss, 250, 310)):
        o.append(_mo_cn(126, yP, xl, ym) + _mo_cn(440, yP, xr, ym))
    o.append(_mo_cn(126, yP, 226, y_pp) + _mo_cn(440, yP, 334, y_pp))
    o.append(_mo_cn(126, yP, 226, y_ps) + _mo_cn(440, yP, 334, y_ps))
    o.append(_mo_level(250, 310, y_s, "ud") + _mo_level(250, 310, y_ss2, "ud") + _mo_level(250, 310, y_p, "ud"))
    o.append(_mo_level(226, 262, y_pp, "ud") + _mo_level(298, 334, y_pp, "ud"))
    o.append(_mo_level(226, 262, y_ps, "ud") + _mo_level(298, 334, y_ps, "ud"))
    o.append(_mo_level(250, 310, y_ss, ""))
    o.append(_mo_lab(242, y_s + 4, "&sigma;2s", "end") + _mo_lab(242, y_ss2 + 4, "&sigma;*2s", "end") + _mo_lab(242, y_p + 4, "&sigma;2p", "end"))
    o.append(_mo_lab(218, y_pp + 4, "&pi;2p", "end") + _mo_lab(218, y_ps + 4, "&pi;*2p", "end") + _mo_lab(242, y_ss + 4, "&sigma;*2p", "end"))
    o.append(_mo_lab(350, y_ps + 4, "both full", "start", "mo-hi-t"))
    return svg(W, H, "Molecular orbital diagram of F2 with 14 valence electrons: sigma2s, sigma-star 2s, sigma2p, pi2p and pi-star 2p are all full and sigma-star 2p is empty, giving bond order 1 and no unpaired electrons.", "".join(o))


def mo_ethene():
    """Partial MO diagram for the C=C unit of ethene (sp2 hybrids -> sigma, leftover 2p -> pi)."""
    W, H = 700, 400
    y_sp2, y_2p = 250, 170
    y_sig, y_pi, y_pis, y_sigs = 345, 222, 118, 36
    cl, cr = 290, 410          # centre levels x-range
    o = ['<path class="mo-ax" d="M14,380 V26 M9,34 L14,24 L19,34"/>', _mo_lab(8, 14, "E", "start")]
    o.append(_mo_lab(100, 22, "C atom", cls="mo-title") + _mo_lab(350, 14, "C=C bonds", cls="mo-title") + _mo_lab(590, 22, "C atom", cls="mo-title"))
    for x0 in (50, 550):
        o.append(_mo_level(x0, x0 + 22, y_sp2, "u") + _mo_level(x0 + 26, x0 + 48, y_sp2, "u") + _mo_level(x0 + 52, x0 + 74, y_sp2, "u"))
        o.append(_mo_lab(x0 + 37, y_sp2 + 20, "sp&sup2;", cls="mo-ao"))
        o.append(_mo_level(x0 + 26, x0 + 48, y_2p, "u"))
        o.append(_mo_lab(x0 + 37, y_2p + 20, "2p", cls="mo-ao"))
    o.append(_mo_cn(124, y_sp2, cl, y_sig) + _mo_cn(550, y_sp2, cr, y_sig))
    o.append(_mo_cn(124, y_sp2, cl, y_sigs) + _mo_cn(550, y_sp2, cr, y_sigs))
    o.append(_mo_cn(98, y_2p, cl, y_pi) + _mo_cn(576, y_2p, cr, y_pi))
    o.append(_mo_cn(98, y_2p, cl, y_pis) + _mo_cn(576, y_2p, cr, y_pis))
    pi_cls = "mo-lv fm-pi"
    o.append(_mo_level(cl, cr, y_sig, "ud") + _mo_level(cl, cr, y_pi, "ud", pi_cls) + _mo_level(cl, cr, y_pis, "", pi_cls) + _mo_level(cl, cr, y_sigs, ""))
    o.append(_mo_lab(cl - 8, y_sig + 4, "&sigma; (C&ndash;C bonding)", "end"))
    o.append(_mo_lab(cl - 8, y_pi + 4, "&pi; bonding", "end", "mo-lab fm-pi-t"))
    o.append(_mo_lab(cl - 8, y_pis + 4, "&pi;* antibonding", "end", "mo-lab fm-pi-t"))
    o.append(_mo_lab(cl - 8, y_sigs + 4, "&sigma;* (C&ndash;C antibonding)", "end"))
    o.append(_mo_lab(cr + 8, y_pi + 4, "HOMO", "start", "mo-hi-t"))
    o.append(_mo_lab(cr + 8, y_pis + 4, "LUMO", "start", "mo-hi-t"))
    o.append(f'<path class="fm-dim2" d="M458,{y_pi} V{y_pis}" marker-start="url(#gapA2)" marker-end="url(#gapA2)"/>')
    o.append(_mo_lab(468, (y_pi + y_pis) / 2 - 2, "&Delta;E (&pi;&rarr;&pi;*)", "start", "fm-note fm-halo"))
    o.append(_mo_lab(468, (y_pi + y_pis) / 2 + 14, "small", "start", "fm-note fm-halo"))
    o.append(f'<path class="fm-dim2" d="M676,{y_sig} V{y_sigs}" marker-start="url(#gapA2)" marker-end="url(#gapA2)"/>')
    o.append(_mo_lab(666, 70, "&Delta;E (&sigma;&rarr;&sigma;*)", "end", "fm-note fm-halo") + _mo_lab(666, 86, "much larger", "end", "fm-note fm-halo"))
    o.append('<defs><marker id="gapA2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>')
    return svg(W, H, "Partial molecular orbital diagram for ethene: each carbon contributes three sp2 electrons and one 2p electron. The sigma bonding orbital and the pi bonding orbital are filled; the pi bonding orbital is the HOMO and the pi-star orbital is the LUMO, separated by a much smaller gap than sigma to sigma-star.", "".join(o))


ALL = {
    "hy_promote": hy_promote, "hy_shape": hy_shape, "hy_ethene": hy_ethene,
    "ip_dipoles": ip_dipoles, "ip_hbond": ip_hbond, "ip_water4": ip_water4, "ip_hydride_bp": ip_hydride_bp,
    "ip_alkane_bp": ip_alkane_bp, "ip_shape": ip_shape, "ip_instant": ip_instant,
    "mt_band": mt_band, "mt_namgal": mt_namgal, "mt_gap": mt_gap, "mt_group14": mt_group14,
    "mt_resist": mt_resist, "mt_workfn": mt_workfn,
    "mo_f2": mo_f2, "mo_ethene": mo_ethene,
}

if __name__ == "__main__":
    out = (sys.argv[1] if len(sys.argv) > 1 else "out").rstrip("/")
    os.makedirs(out, exist_ok=True)
    for k, fn in ALL.items():
        open(f"{out}/{k}.html", "w", encoding="utf-8").write(fn())
    print("wrote", len(ALL), "figures to", out)
