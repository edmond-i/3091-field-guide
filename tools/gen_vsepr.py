"""Generate the VSEPR shape diagrams (inline SVG) used in the 3.091 Field Guide.

Drawing convention (standard wedge/dash):
  plain line  = bond in the plane of the page
  solid wedge = bond coming toward you
  hashed wedge = bond going away from you
  teal lobe with two dots = lone pair
"""
import math

CX, CY, L = 60, 56, 33          # centre and bond length in the 120x110 cell
R_ATOM, R_CENTER = 8.5, 6.5


def pt(angle, dist):
    a = math.radians(angle)
    return CX + dist * math.cos(a), CY - dist * math.sin(a)


def f(v):
    return f"{v:.1f}"


def bond_plain(angle):
    x1, y1 = pt(angle, R_CENTER)
    x2, y2 = pt(angle, L - R_ATOM + 1)
    return f'<line class="sv-bond" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>'


def bond_wedge(angle):
    x1, y1 = pt(angle, R_CENTER)
    x2, y2 = pt(angle, L - R_ATOM + 1)
    px, py = -math.sin(math.radians(angle)), -math.cos(math.radians(angle))
    w = 4.2
    return (f'<polygon class="sv-wedge" points="{f(x1)},{f(y1)} '
            f'{f(x2 + px * w)},{f(y2 + py * w)} {f(x2 - px * w)},{f(y2 - py * w)}"/>')


def bond_dash(angle):
    parts = []
    px, py = -math.sin(math.radians(angle)), -math.cos(math.radians(angle))
    n = 5
    d0, d1 = R_CENTER + 1, L - R_ATOM + 1
    for i in range(n):
        d = d0 + (d1 - d0) * (i + 0.5) / n
        w = 1.0 + 3.4 * (i + 0.5) / n
        x, y = pt(angle, d)
        parts.append(f'<line class="sv-dash" x1="{f(x + px * w)}" y1="{f(y + py * w)}" '
                     f'x2="{f(x - px * w)}" y2="{f(y - py * w)}"/>')
    return "".join(parts)


def atom(angle):
    x, y = pt(angle, L)
    return f'<circle class="sv-atom" cx="{f(x)}" cy="{f(y)}" r="{R_ATOM}"/>'


def lone_pair(angle):
    x, y = pt(angle, 24)
    d1x, d1y = pt(angle, 20)
    d2x, d2y = pt(angle, 28)
    rot = -angle
    return (f'<ellipse class="sv-lp" cx="{f(x)}" cy="{f(y)}" rx="12" ry="7.5" '
            f'transform="rotate({rot:.0f} {f(x)} {f(y)})"/>'
            f'<circle class="sv-dot" cx="{f(d1x)}" cy="{f(d1y)}" r="1.9"/>'
            f'<circle class="sv-dot" cx="{f(d2x)}" cy="{f(d2y)}" r="1.9"/>')


def draw(items):
    """items: list of (angle, style, kind). style in plain/wedge/dash; kind atom/lp."""
    # draw back-to-front: dashes, plain, lone pairs, wedges, then atoms on top
    out = []
    for a, s, k in items:
        if k == "atom":
            out.append(bond_dash(a) if s == "dash" else bond_wedge(a) if s == "wedge" else bond_plain(a))
    for a, s, k in items:
        if k == "lp":
            out.append(lone_pair(a))
    out.append(f'<circle class="sv-center" cx="{CX}" cy="{CY}" r="{R_CENTER}"/>')
    for a, s, k in items:
        if k == "atom":
            out.append(atom(a))
    return "".join(out)


A, P, W, D = "atom", "plain", "wedge", "dash"
LP = "lp"

TET = [(90, P), (215, P), (325, W), (35, D)]

SHAPES = {
    # key: (items)
    "linear2": [(180, P, A), (0, P, A)],
    "trigplanar": [(90, P, A), (210, P, A), (330, P, A)],
    "bent3": [(210, P, A), (330, P, A), (90, P, LP)],
    "tetra": [(90, P, A), (215, P, A), (325, W, A), (35, D, A)],
    "pyramid": [(90, P, LP), (215, P, A), (325, W, A), (35, D, A)],
    "bent4": [(215, P, A), (325, P, A), (55, P, LP), (125, P, LP)],
    "tbp": [(90, P, A), (270, P, A), (180, P, A), (335, W, A), (25, D, A)],
    "seesaw": [(90, P, A), (270, P, A), (180, P, LP), (335, W, A), (25, D, A)],
    "tshape": [(90, P, A), (270, P, A), (180, P, A), (335, P, LP), (25, P, LP)],
    "linear5": [(90, P, A), (270, P, A), (180, P, LP), (335, P, LP), (25, P, LP)],
    "octa": [(90, P, A), (270, P, A), (180, P, A), (0, P, A), (225, W, A), (45, D, A)],
    "sqpyr": [(90, P, A), (270, P, LP), (180, P, A), (0, P, A), (225, W, A), (45, D, A)],
    "sqplanar": [(90, P, LP), (270, P, LP), (180, P, A), (0, P, A), (225, W, A), (45, D, A)],
}


def svg(key, label):
    return (f'<svg viewBox="0 0 120 110" role="img" aria-label="{label}">'
            f'{draw(SHAPES[key])}</svg>')


# (sn, lps, key, name, axe, angle, example, hybrid)
CELLS = [
    (2, 0, "linear2", "Linear", "AX₂", "180°", "CO₂, BeCl₂", "sp"),
    (3, 0, "trigplanar", "Trigonal planar", "AX₃", "120°", "BF₃, SO₃, NO₃⁻", "sp²"),
    (3, 1, "bent3", "Bent", "AX₂E", "&lt;120°", "SO₂, O₃", "sp²"),
    (4, 0, "tetra", "Tetrahedral", "AX₄", "109.5°", "CH₄, NH₄⁺", "sp³"),
    (4, 1, "pyramid", "Trigonal pyramidal", "AX₃E", "~107°", "NH₃, PCl₃", "sp³"),
    (4, 2, "bent4", "Bent", "AX₂E₂", "~104.5°", "H₂O, H₂S", "sp³"),
    (5, 0, "tbp", "Trigonal bipyramidal", "AX₅", "90° / 120°", "PCl₅, PF₅", "sp³d"),
    (5, 1, "seesaw", "See-saw", "AX₄E", "&lt;90° / &lt;120°", "SF₄", "sp³d"),
    (5, 2, "tshape", "T-shaped", "AX₃E₂", "&lt;90°", "ClF₃, BrF₃", "sp³d"),
    (5, 3, "linear5", "Linear", "AX₂E₃", "180°", "XeF₂, I₃⁻", "sp³d"),
    (6, 0, "octa", "Octahedral", "AX₆", "90°", "SF₆, PF₆⁻", "sp³d²"),
    (6, 1, "sqpyr", "Square pyramidal", "AX₅E", "&lt;90°", "BrF₅, IF₅", "sp³d²"),
    (6, 2, "sqplanar", "Square planar", "AX₄E₂", "90°", "XeF₄, ICl₄⁻", "sp³d²"),
]

ROW_NAMES = {2: "2 domains", 3: "3 domains", 4: "4 domains", 5: "5 domains", 6: "6 domains"}
GEOM = {2: "linear", 3: "trigonal planar", 4: "tetrahedral", 5: "trigonal bipyramidal", 6: "octahedral"}


def cell_html(c):
    sn, lps, key, name, axe, ang, ex, hyb = c
    label = f"{name} shape, {axe}, ideal angle {ang.replace('&lt;', 'less than ')}"
    return (f'<div class="vs-cell vs-lp{lps}">{svg(key, label)}'
            f'<div class="vs-name">{name}</div>'
            f'<div class="vs-meta"><span class="vs-axe">{axe}</span> &middot; {ang}</div>'
            f'<div class="vs-ex">{ex}</div></div>')


def grid_html():
    out = ['<div class="vs-grid" role="group" aria-label="VSEPR shapes by electron groups and lone pairs">']
    out.append('<div class="vs-corner"></div>')
    for lp in range(4):
        label = "0 lone pairs" if lp == 0 else f"{lp} lone pair{'s' if lp > 1 else ''}"
        out.append(f'<div class="vs-colhead">{label}</div>')
    for sn in range(2, 7):
        out.append(f'<div class="vs-rowhead"><b>{sn}</b><span>electron groups</span><em>{GEOM[sn]}</em></div>')
        for lp in range(4):
            c = next((c for c in CELLS if c[0] == sn and c[1] == lp), None)
            out.append(cell_html(c) if c else '<div class="vs-empty"></div>')
    out.append("</div>")
    return "\n".join(out)




# ---------- Figure: how the electron groups spread out (every group drawn as a lobe) ----------
def group_lobe(angle, dist=27):
    x, y = pt(angle, dist)
    d1x, d1y = pt(angle, dist - 4)
    d2x, d2y = pt(angle, dist + 4)
    return (f'<ellipse class="sv-lp" cx="{f(x)}" cy="{f(y)}" rx="12" ry="7.5" transform="rotate({-angle:.0f} {f(x)} {f(y)})"/>'
            f'<circle class="sv-dot" cx="{f(d1x)}" cy="{f(d1y)}" r="1.9"/><circle class="sv-dot" cx="{f(d2x)}" cy="{f(d2y)}" r="1.9"/>')


GROUP_ANGLES = {
    2: [180, 0],
    3: [90, 210, 330],
    4: [90, 215, 325, 35],
    5: [90, 270, 180, 335, 25],
    6: [90, 270, 180, 0, 225, 45],
}
GROUP_INFO = {
    2: ("Linear", "180°"),
    3: ("Trigonal planar", "120°"),
    4: ("Tetrahedral", "109.5°"),
    5: ("Trigonal bipyramidal", "90° and 120°"),
    6: ("Octahedral", "90°"),
}


def groups_figure():
    out = ['<div class="gp-row">']
    for n in range(2, 7):
        lobes = "".join(group_lobe(a) for a in GROUP_ANGLES[n])
        name, ang = GROUP_INFO[n]
        out.append(f'<div class="gp-cell"><svg viewBox="0 0 120 110" role="img" aria-label="{n} electron groups spread out as {name.lower()}, {ang}">'
                   f'{lobes}<circle class="sv-center" cx="{CX}" cy="{CY}" r="{R_CENTER}"/></svg>'
                   f'<div class="gp-n">{n}</div><div class="vs-name">{name}</div><div class="vs-meta">{ang}</div></div>')
    out.append('</div>')
    return "".join(out)


# ---------- Figure: lone pairs squeeze the bond angle ----------
def arc(r, a1, a2):
    x1, y1 = pt(a1, r)
    x2, y2 = pt(a2, r)
    return f'<path class="sv-arc" d="M{f(x1)},{f(y1)} A{r},{r} 0 0 1 {f(x2)},{f(y2)}"/>'


def squeeze_figure():
    """Real angles are 109.5 / 107 / 104.5. The drawing exaggerates the squeeze 4x and shows a
    dashed ghost of the 109.5-degree V so the shrinking is visible."""
    cases = [
        ("CH₄", "no lone pair", 109.5, [], "109.5°"),
        ("NH₃", "1 lone pair", 107, [90], "107°"),
        ("H₂O", "2 lone pairs", 104.5, [55, 125], "104.5°"),
    ]
    out = ['<div class="gp-row sq-row">']
    for mol, lp_txt, ang, lps, lab in cases:
        drawn = 109.5 - 4 * (109.5 - ang)
        a1, a2 = 270 - drawn / 2, 270 + drawn / 2
        g1, g2 = 270 - 109.5 / 2, 270 + 109.5 / 2
        body = ""
        if ang != 109.5:
            for g in (g1, g2):
                x, y = pt(g, L)
                body += f'<line class="sv-ghost" x1="{CX}" y1="{CY}" x2="{f(x)}" y2="{f(y)}"/>'
        body += "".join(bond_plain(a) for a in (a1, a2))
        body += "".join(lone_pair(a) for a in lps)
        body += f'<circle class="sv-center" cx="{CX}" cy="{CY}" r="{R_CENTER}"/>'
        body += atom(a1) + atom(a2)
        x1, y1 = pt(a1 + 5, 19)
        x2, y2 = pt(a2 - 5, 19)
        body += f'<path class="sv-arc" d="M{f(x1)},{f(y1)} A19,19 0 0 1 {f(x2)},{f(y2)}"/>'
        out.append(f'<div class="gp-cell"><svg viewBox="0 0 120 110" role="img" aria-label="{mol} bond angle {lab}">{body}</svg>'
                   f'<div class="vs-name">{mol}</div><div class="sq-ang">{lab}</div><div class="vs-meta">{lp_txt}</div></div>')
    out.append('</div>')
    return "".join(out)


# ---------- Figure: bond dipoles add as vectors ----------
def arrow(x1, y1, x2, y2, cls):
    ang = math.degrees(math.atan2(-(y2 - y1), x2 - x1))
    hx, hy = x2, y2
    a1x, a1y = hx - 6 * math.cos(math.radians(ang - 150) * -1) * -1, 0
    # arrow head as polygon
    ux, uy = (x2 - x1), (y2 - y1)
    n = math.hypot(ux, uy) or 1
    ux, uy = ux / n, uy / n
    px, py = -uy, ux
    tip = (x2, y2)
    b1 = (x2 - 7 * ux + 3.6 * px, y2 - 7 * uy + 3.6 * py)
    b2 = (x2 - 7 * ux - 3.6 * px, y2 - 7 * uy - 3.6 * py)
    shaft_end = (x2 - 5 * ux, y2 - 5 * uy)
    return (f'<line class="{cls}" x1="{f(x1)}" y1="{f(y1)}" x2="{f(shaft_end[0])}" y2="{f(shaft_end[1])}"/>'
            f'<polygon class="{cls}-h" points="{f(tip[0])},{f(tip[1])} {f(b1[0])},{f(b1[1])} {f(b2[0])},{f(b2[1])}"/>')


def label(x, y, txt, cls="sv-txt"):
    return f'<text class="{cls}" x="{f(x)}" y="{f(y + 3.2)}" text-anchor="middle">{txt}</text>'


def dipole_cell(name, center, outers, net, verdict, shape_note):
    """outers: list of (angle, symbol, toward) where toward='out' means bond dipole points to the outer atom,
    'in' means it points toward the central atom. net: angle of net dipole or None."""
    body = ""
    for a, sym, toward, style in outers:
        body += bond_dash(a) if style == "dash" else bond_wedge(a) if style == "wedge" else bond_plain(a)
    # bond dipole arrows sit beside each bond
    for a, sym, toward, style in outers:
        off = 5.5
        px, py = -math.sin(math.radians(a)), -math.cos(math.radians(a))
        sx, sy = pt(a, 13)
        ex, ey = pt(a, 25)
        sx += px * off; sy += py * off; ex += px * off; ey += py * off
        if toward == "in":
            sx, sy, ex, ey = ex, ey, sx, sy
        body += arrow(sx, sy, ex, ey, "sv-bd")
    body += f'<circle class="sv-ctr" cx="{CX}" cy="{CY}" r="9"/>' + label(CX, CY, center, "sv-txt-w")
    for a, sym, toward, style in outers:
        x, y = pt(a, L)
        body += f'<circle class="sv-atom" cx="{f(x)}" cy="{f(y)}" r="8.5"/>' + label(x, y, sym, "sv-txt-w")
    if net is not None:
        x1, y1 = pt(net, 9)
        x2, y2 = pt(net, 46)
        body += arrow(x1, y1, x2, y2, "sv-net")
    return (f'<div class="gp-cell dp-cell {"dp-net" if net is not None else "dp-zero"}">'
            f'<svg viewBox="0 0 120 110" role="img" aria-label="{name}: {verdict}">{body}</svg>'
            f'<div class="vs-name">{name}</div><div class="vs-meta">{shape_note}</div>'
            f'<div class="dp-verdict">{verdict}</div></div>')


def dipole_figure():
    P_, W_, D_ = "plain", "wedge", "dash"
    cells = [
        dipole_cell("CO₂", "C", [(180, "O", "out", P_), (0, "O", "out", P_)], None, "cancel → nonpolar", "linear"),
        dipole_cell("BF₃", "B", [(90, "F", "out", P_), (210, "F", "out", P_), (330, "F", "out", P_)], None, "cancel → nonpolar", "trigonal planar"),
        dipole_cell("CCl₄", "C", [(90, "Cl", "out", P_), (215, "Cl", "out", P_), (325, "Cl", "out", W_), (35, "Cl", "out", D_)], None, "cancel → nonpolar", "tetrahedral"),
        dipole_cell("H₂O", "O", [(215, "H", "in", P_), (325, "H", "in", P_)], 90, "add up → polar", "bent"),
        dipole_cell("NH₃", "N", [(215, "H", "in", P_), (325, "H", "in", W_), (35, "H", "in", D_)], 90, "add up → polar", "trigonal pyramidal"),
        dipole_cell("CHCl₃", "C", [(90, "H", "in", P_), (215, "Cl", "out", P_), (325, "Cl", "out", W_), (35, "Cl", "out", D_)], 270, "add up → polar", "tetrahedral, but not identical"),
    ]
    return '<div class="gp-row dp-row">' + "".join(cells) + '</div>'


if __name__ == "__main__":
    import sys
    out_dir = sys.argv[1]
    open(out_dir + "/vsepr_grid.html", "w", encoding="utf-8").write(grid_html())
    open(out_dir + "/groups_fig.html", "w", encoding="utf-8").write(groups_figure())
    open(out_dir + "/squeeze_fig.html", "w", encoding="utf-8").write(squeeze_figure())
    open(out_dir + "/dipole_fig.html", "w", encoding="utf-8").write(dipole_figure())
    print("wrote figures to", out_dir)
