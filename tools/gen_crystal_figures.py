#!/usr/bin/env python3
"""Figures for Units 09-11 (crystals, defects & glass, diffusion).

Writes one SVG snippet per figure into OUT (default: ./build/figs). build_units.py
substitutes them for {{FIG:name}} placeholders. Colours come from CSS classes defined in
tools/figs_new.css so the figures follow the light/dark theme.
"""
import math, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "build", "figs")
os.makedirs(OUT, exist_ok=True)


def save(name, svg):
    with open(os.path.join(OUT, name + ".svg.html"), "w") as f:
        f.write(svg)


def f1(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


# ---------------------------------------------------------------- cubic cells
def cube(ox, oy, s, kind, label, count):
    """Oblique-projection unit cell. x right, z up, y back-right."""
    dx, dy = 0.42 * s, 0.42 * s

    def P(x, y, z):
        return (ox + x * s + y * dx, oy - z * s - y * dy)

    out = []
    corners = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    edges = []
    for a in corners:
        for b in corners:
            if a < b and sum(abs(a[i] - b[i]) for i in range(3)) == 1:
                edges.append((a, b))
    for a, b in edges:
        hidden = a[1] == 1 and b[1] == 1 and (a[0] == 0 or a[2] == 0) and (b[0] == 0 or b[2] == 0)
        hidden = (a[1] == 1 and b[1] == 1 and ((a[0] == 0 and b[0] == 0) or (a[2] == 0 and b[2] == 0))) or \
                 (a == (0, 0, 0) and b == (0, 1, 0))
        pa, pb = P(*a), P(*b)
        out.append('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
            "cx-edge cx-hid" if hidden else "cx-edge", f1(pa[0]), f1(pa[1]), f1(pb[0]), f1(pb[1])))
    pts = [(c, "cx-corner") for c in corners]
    if kind == "bcc":
        pts.append(((0.5, 0.5, 0.5), "cx-centre"))
    if kind == "fcc":
        for c in [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)]:
            pts.append((c, "cx-face"))
    # back to front so front atoms overlap
    pts.sort(key=lambda t: -t[0][1])
    for c, cls in pts:
        p = P(*c)
        out.append('<circle class="cx-atom %s" cx="%s" cy="%s" r="%s"/>' % (cls, f1(p[0]), f1(p[1]), f1(s * 0.095 if cls == "cx-corner" else s * 0.105)))
    cx = ox + s * 0.7
    out.append('<text class="fm-h" x="%s" y="%s" text-anchor="middle">%s</text>' % (f1(cx), f1(oy + 26), label))
    out.append('<text class="fm-note" x="%s" y="%s" text-anchor="middle">%s</text>' % (f1(cx), f1(oy + 44), count))
    return "".join(out)


def fig_cells():
    s = 110
    body = cube(40, 190, s, "sc", "Simple cubic (SC)", "8 &times; &frac18; = 1 lattice point") + \
        cube(300, 190, s, "bcc", "Body-centred (BCC)", "8 &times; &frac18; + 1 = 2 lattice points") + \
        cube(560, 190, s, "fcc", "Face-centred (FCC)", "8 &times; &frac18; + 6 &times; &frac12; = 4 lattice points")
    svg = ('<svg viewBox="0 0 820 270" role="img" aria-label="The three cubic unit cells. Simple cubic has atoms at the 8 corners only, body-centred cubic adds one atom in the middle, face-centred cubic adds an atom in the middle of each of the 6 faces.">'
           + body + '</svg>')
    save("cells", svg)


# -------------------------------------------------------------------- Bragg
def fig_bragg():
    th = math.radians(30)
    y1, y2 = 90, 190  # plane heights (d = 100)
    parts = []
    for y in (y1, y2):
        parts.append('<line class="cx-plane" x1="60" y1="%d" x2="460" y2="%d"/>' % (y, y))
        for x in range(80, 460, 40):
            parts.append('<circle class="cx-atom cx-corner" cx="%d" cy="%d" r="7"/>' % (x, y))
    # incoming rays hit top plane at x=200 and bottom plane at x=200+? choose points A (top) and C (bottom)
    ax = 330
    cx = ax - (y2 - y1) / math.tan(th) / 1.0  # lower ray hits bottom plane further left so that both reflect to the right
    # incident ray 1: reaches A on the top plane
    L = 150
    inx = lambda x, y, t: (x - L * math.cos(t), y - L * math.sin(t))
    # top ray: comes from the upper left, goes to A, leaves to upper right
    ex, ey = inx(ax, y1, th)
    parts.append('<path class="cx-ray" d="M%s,%s L%d,%d"/>' % (f1(ex), f1(ey), ax, y1))
    parts.append('<path class="cx-ray" d="M%d,%d L%s,%s" marker-end="url(#bgA)"/>' % (ax, y1, f1(ax + L * math.cos(th)), f1(y1 - L * math.sin(th))))
    # bottom ray: hits bottom plane at C
    cxp = ax - 0.0
    cxp = 250
    ex2, ey2 = inx(cxp, y2, th)
    parts.append('<path class="cx-ray cx-ray2" d="M%s,%s L%d,%d"/>' % (f1(ex2), f1(ey2), cxp, y2))
    parts.append('<path class="cx-ray cx-ray2" d="M%d,%d L%s,%s" marker-end="url(#bgA)"/>' % (cxp, y2, f1(cxp + L * math.cos(th)), f1(y2 - L * math.sin(th))))
    # angle arc at A
    parts.append('<path class="cx-arc" d="M%d,%d A34,34 0 0 0 %s,%s"/>' % (ax - 34, y1, f1(ax - 34 * math.cos(th)), f1(y1 - 34 * math.sin(th))))
    parts.append('<text class="fm-note" x="%d" y="%d" text-anchor="end">&theta;</text>' % (ax - 38, y1 - 6))
    # d marker
    parts.append('<line class="fm-dim2" x1="500" y1="%d" x2="500" y2="%d" marker-start="url(#bgA)" marker-end="url(#bgA)"/>' % (y1 + 3, y2 - 3))
    parts.append('<text class="fm-h" x="512" y="%d">d</text>' % ((y1 + y2) // 2 + 5))
    parts.append('<text class="fm-note" x="512" y="%d">spacing between</text><text class="fm-note" x="512" y="%d">neighbouring planes</text>' % ((y1 + y2) // 2 + 24, (y1 + y2) // 2 + 40))
    parts.append('<text class="fm-note" x="70" y="%d">atomic plane</text>' % (y1 - 12))
    parts.append('<text class="fm-note" x="70" y="%d">next plane</text>' % (y2 + 22))
    parts.append('<text class="fm-cap" x="400" y="262" text-anchor="middle">The lower ray travels 2 d sin&theta; farther than the upper ray.</text>')
    parts.append('<text class="fm-cap" x="400" y="284" text-anchor="middle">Constructive interference when that extra distance = n&lambda;:   2 d sin&theta; = n&lambda;</text>')
    svg = ('<svg viewBox="0 0 760 300" role="img" aria-label="Bragg diffraction: two X-ray beams reflect from two neighbouring atomic planes a distance d apart at glancing angle theta; the lower beam travels an extra 2 d sin theta.">'
           '<defs><marker id="bgA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>'
           + "".join(parts) + '</svg>')
    save("bragg", svg)


# ------------------------------------------------------------------- Miller
def planecube(ox, oy, s, plane, label, sub):
    dx, dy = 0.42 * s, 0.42 * s
    P = lambda x, y, z: (ox + x * s + y * dx, oy - z * s - y * dy)
    out = []
    corners = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    for a in corners:
        for b in corners:
            if a < b and sum(abs(a[i] - b[i]) for i in range(3)) == 1:
                hidden = (a[1] == 1 and b[1] == 1 and ((a[0] == 0 and b[0] == 0) or (a[2] == 0 and b[2] == 0))) or (a == (0, 0, 0) and b == (0, 1, 0))
                pa, pb = P(*a), P(*b)
                out.append('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % ("cx-edge cx-hid" if hidden else "cx-edge", f1(pa[0]), f1(pa[1]), f1(pb[0]), f1(pb[1])))
    poly = " ".join("%s,%s" % tuple(map(f1, P(*c))) for c in plane)
    out.append('<polygon class="cx-plane-fill" points="%s"/>' % poly)
    # axes labels at origin (0,0,0) is the front-bottom-left in this projection
    # NOTE: here the origin used for intercepts is (0,0,0) = front bottom-left corner
    o = P(0, 0, 0)
    out.append('<circle class="cx-origin" cx="%s" cy="%s" r="4"/>' % (f1(o[0]), f1(o[1])))
    ex = P(1.2, 0, 0); ey = P(0, 1.25, 0); ez = P(0, 0, 1.2)
    for e, t in ((ex, "x"), (ey, "y"), (ez, "z")):
        out.append('<text class="fm-note" x="%s" y="%s">%s</text>' % (f1(e[0] + 4), f1(e[1] + 4), t))
    out.append('<text class="fm-h" x="%s" y="%s" text-anchor="middle">%s</text>' % (f1(ox + s * 0.7), f1(oy + 30), label))
    out.append('<text class="fm-note" x="%s" y="%s" text-anchor="middle">%s</text>' % (f1(ox + s * 0.7), f1(oy + 48), sub))
    return "".join(out), P


def fig_miller():
    s = 120
    # (111): triangle through (1,0,0), (0,1,0), (0,0,1)
    a, P1 = planecube(60, 170, s, [(1, 0, 0), (0, 1, 0), (0, 0, 1)], "(111) plane", "intercepts 1, 1, 1  &rarr;  1/1, 1/1, 1/1")
    # normal arrow [111] from origin (0,0,0) towards (1,1,1)
    p0, p1 = P1(0, 0, 0), P1(1, 1, 1)
    a += '<path class="cx-normal" d="M%s,%s L%s,%s" marker-end="url(#mlA)"/><text class="fm-note cx-normal-t" x="%s" y="%s">[111]</text>' % (f1(p0[0]), f1(p0[1]), f1(p1[0]), f1(p1[1]), f1(p1[0] + 6), f1(p1[1] - 4))
    # (210): plane x=1/2 .. wait intercepts 1/2 on x, 1 on y, inf on z => plane through (0.5,0,z) and (0,1,z)
    b, P2 = planecube(420, 170, s, [(0.5, 0, 0), (0, 1, 0), (0, 1, 1), (0.5, 0, 1)], "(210) plane", "intercepts &frac12;, 1, &infin;  &rarr;  2, 1, 0")
    svg = ('<svg viewBox="0 0 780 250" role="img" aria-label="Two Miller-index examples in a cubic cell: the (111) plane through the points 1 on each axis, with the perpendicular direction [111]; and the (210) plane cutting x at one half and y at one, parallel to z.">'
           '<defs><marker id="mlA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="cx-normal-h"/></marker></defs>'
           + a + b + '</svg>')
    save("miller", svg)


# ------------------------------------------------------------ point defects
def lattice2d(cols, rows, x0, y0, step, missing=(), interstitial=None, moved_from=None):
    out = []
    for r in range(rows):
        for c in range(cols):
            x, y = x0 + c * step, y0 + r * step
            anion = (r + c) % 2 == 0
            if (r, c) in missing:
                out.append('<circle class="cx-vac" cx="%d" cy="%d" r="%d"/>' % (x, y, 15 if anion else 9))
                continue
            out.append('<circle class="%s" cx="%d" cy="%d" r="%d"/>' % ("ion-an" if anion else "ion-cat", x, y, 15 if anion else 9))
            out.append('<text class="ion-t" x="%d" y="%d" text-anchor="middle">%s</text>' % (x, y + 4, "&minus;" if anion else "+"))
    if interstitial:
        x, y = interstitial
        out.append('<circle class="ion-cat" cx="%d" cy="%d" r="9"/><text class="ion-t" x="%d" y="%d" text-anchor="middle">+</text>' % (x, y, x, y + 4))
    return "".join(out)


def fig_pointdef():
    step = 44
    a = lattice2d(5, 5, 40, 40, step, missing={(1, 2), (2, 3)})  # (1,2): r+c=3 odd -> cation; (2,3): odd -> cation ... fix below
    # choose one cation vacancy (odd) and one anion vacancy (even)
    a = lattice2d(5, 5, 40, 40, step, missing={(1, 2), (2, 2)})
    # Frenkel: cation leaves (2,3)... (r+c) odd -> cation; interstitial between sites
    b = lattice2d(5, 5, 380, 40, step, missing={(1, 2)}, interstitial=(380 + 2 * step + step // 2, 40 + 3 * step + step // 2 - 0))
    svg = ('<svg viewBox="0 0 700 290" role="img" aria-label="Two point defects in an ionic crystal. Schottky: one cation and one anion are both missing, leaving a pair of vacancies. Frenkel: a cation leaves its site, leaving a vacancy, and squeezes into a gap between sites.">'
           + a + b +
           '<text class="fm-h" x="130" y="240" text-anchor="middle">Schottky defect</text>'
           '<text class="fm-note" x="130" y="258" text-anchor="middle">a + and a &minus; both missing</text><text class="fm-note" x="130" y="274" text-anchor="middle">(a pair of vacancies)</text>'
           '<text class="fm-h" x="470" y="240" text-anchor="middle">Frenkel defect</text>'
           '<text class="fm-note" x="470" y="258" text-anchor="middle">a + left its site and squeezed into a gap</text><text class="fm-note" x="470" y="274" text-anchor="middle">(vacancy + interstitial)</text>'
           '</svg>')
    save("pointdef", svg)


# ------------------------------------------------------------- dislocation
def fig_dislocation():
    # rows of atoms; extra half plane inserted from the top, ending mid-crystal
    step = 34
    cols, rows = 9, 8
    x0, y0 = 60, 30
    out = []
    mid = 4  # column index of the extra half plane
    for r in range(rows):
        for c in range(cols + 1):
            # columns left of mid shifted left, right of mid shifted right in the lower half to make room
            if r < 4:
                x = x0 + c * step
            else:
                # lower part: only `cols` columns, squeezed around the dislocation core
                if c == cols:
                    continue
                x = x0 + (c + 0.5) * step * (cols + 1) / cols * 0.0 + c * step * (cols / cols) + step * 0.5 * 1
                x = x0 + c * step * (cols + 1 - 1) / (cols - 1) * (1.0)
                x = x0 + c * (cols * step) / (cols - 1)
            # bend rows around the core slightly
            y = y0 + r * step
            dist = abs(x - (x0 + mid * step))
            y += 7 * math.exp(-(dist / 55.0) ** 2) * (1 if r >= 4 else 0)
            out.append('<circle class="cx-atom cx-corner" cx="%s" cy="%s" r="8"/>' % (f1(x), f1(y)))
    cx = x0 + mid * step
    cy = y0 + 4 * step - 12
    out.append('<text class="cx-dis" x="%s" y="%s" text-anchor="middle">&perp;</text>' % (f1(cx), f1(cy + 26)))
    out.append('<text class="fm-note" x="%s" y="%s" text-anchor="middle">the extra half-plane of atoms ends at &perp;:</text><text class="fm-note" x="%s" y="%s" text-anchor="middle">an edge dislocation</text>' % (f1(x0 + 4.5 * step), f1(y0 + 8 * step + 14), f1(x0 + 4.5 * step), f1(y0 + 8 * step + 30)))
    svg = ('<svg viewBox="0 0 420 345" role="img" aria-label="An edge dislocation: an extra half-plane of atoms inserted from the top ends part-way into the crystal; the symbol for the dislocation line sits at its end.">'
           + "".join(out) + '</svg>')
    save("dislocation", svg)


# ------------------------------------------------------- viscosity vs temp
def fig_visc():
    # schematic log(viscosity) vs T (VFT-like) for 4 glasses; y: log10 eta [Pa s] from 0 to 16
    W, H = 760, 330
    x0, x1, y0, y1 = 70, 600, 20, 290  # plot box
    T0, T1 = 400, 1800
    X = lambda T: x0 + (T - T0) / (T1 - T0) * (x1 - x0)
    Y = lambda lg: y1 - lg / 16.0 * (y1 - y0)
    # each curve: T at which log eta = 14 and T at which log eta = 1.5
    curves = [("Soda-lime", 500, 1050, "vc-sl"), ("Borosilicate", 560, 1450, "vc-bo"), ("96% silica", 900, 1700, "vc-96"), ("Fused silica", 1100, 1780, "vc-fs")]
    out = ['<line class="ic-axis" x1="%d" y1="%d" x2="%d" y2="%d"/><line class="ic-axis" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0, y0, x0, y1, x0, y1, x1, y1)]
    for lg in range(0, 17, 2):
        out.append('<line class="fm-dim vc-grid" x1="%d" y1="%s" x2="%d" y2="%s"/><text class="ic-tick" x="%d" y="%s" text-anchor="end">10<tspan class="fm-sub" dy="-5">%d</tspan></text>' % (x0, f1(Y(lg)), x1, f1(Y(lg)), x0 - 6, f1(Y(lg) + 4), lg))
    for T in range(400, 1801, 200):
        out.append('<text class="ic-tick" x="%s" y="%d" text-anchor="middle">%d</text>' % (f1(X(T)), y1 + 16, T))
    # named viscosity points (log10 Pa s), schematic
    named = [("strain point", 13.5), ("annealing point", 12), ("softening point", 6.6), ("working point", 3), ("melting", 1)]
    for nm, lg in named:
        out.append('<line class="vc-ref" x1="%d" y1="%s" x2="%d" y2="%s"/><text class="fm-note" x="%d" y="%s" text-anchor="start">%s</text>' % (x0, f1(Y(lg)), x1, f1(Y(lg)), x1 + 8, f1(Y(lg) + 4), nm))
    for nm, Ta, Tb, cls in curves:
        pts = []
        for i in range(0, 41):
            lg = 14 - (14 - 1.5) * i / 40.0
            # interpolate temperature with a mild bow (viscosity drops fast then slower)
            u = i / 40.0
            T = Ta + (Tb - Ta) * (u ** 0.82)
            pts.append("%s,%s" % (f1(X(T)), f1(Y(lg))))
        out.append('<polyline class="vc %s" points="%s"/>' % (cls, " ".join(pts)))
    # labels
    lab = [("Soda-lime", "vc-sl", "vc-sl-t"), ("Borosilicate", "vc-bo", "vc-bo-t"), ("96% silica", "vc-96", "vc-96-t"), ("Fused silica", "vc-fs", "vc-fs-t")]
    for i, (nm, lc, cls) in enumerate(lab):
        yy = Y(5.6) + i * 20
        out.append('<line class="vc %s" x1="%d" y1="%s" x2="%d" y2="%s"/><text class="fm-cap %s" x="%d" y="%s">%s</text>' % (lc, x0 + 14, f1(yy), x0 + 44, f1(yy), cls, x0 + 52, f1(yy + 4), nm))
    out.append('<text class="ic-lab" x="%d" y="%d" text-anchor="middle">temperature, &deg;C</text>' % ((x0 + x1) // 2, H - 4))
    out.append('<text class="ic-lab" transform="rotate(-90 14 %d)" x="14" y="%d" text-anchor="middle">viscosity, Pa&middot;s (log scale)</text>' % ((y0 + y1) // 2, (y0 + y1) // 2))
    svg = ('<svg viewBox="0 0 %d %d" role="img" aria-label="Schematic viscosity against temperature for four glasses on a log scale: every curve falls smoothly by many powers of ten with no sudden melting; soda-lime glass is shifted to the lowest temperatures and fused silica to the highest.">' % (W, H)
           + "".join(out) + '</svg>')
    save("visc", svg)


# --------------------------------------------------------------- diffusion
def fig_diffusion():
    out = []
    # left panel: Arrhenius plot ln D vs 1/T
    x0, x1, y0, y1 = 50, 300, 30, 230
    out.append('<line class="ic-axis" x1="%d" y1="%d" x2="%d" y2="%d"/><line class="ic-axis" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0, y0, x0, y1, x0, y1, x1, y1))
    out.append('<line class="dif-a" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0 + 10, 60, x1 - 10, 130))
    out.append('<line class="dif-b" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0 + 10, 75, x1 - 10, 215))
    out.append('<text class="fm-note dif-a-t" x="%d" y="%d">interstitial (C, H in Fe):</text><text class="fm-note dif-a-t" x="%d" y="%d">shallow, small Q</text>' % (x0 + 70, 50, x0 + 70, 64))
    out.append('<text class="fm-note dif-b-t" x="%d" y="%d">self-diffusion (Fe in Fe):</text><text class="fm-note dif-b-t" x="%d" y="%d">steep, large Q</text>' % (x0 + 6, 196, x0 + 6, 210))
    out.append('<text class="ic-lab" x="%d" y="%d" text-anchor="middle">1/T  (hot on the left &rarr; cold on the right)</text>' % ((x0 + x1) // 2, y1 + 28))
    out.append('<text class="ic-lab" transform="rotate(-90 14 130)" x="14" y="130" text-anchor="middle">ln D</text>')
    out.append('<text class="fm-h" x="%d" y="18" text-anchor="middle">Arrhenius plot: slope = &minus;Q / R</text>' % ((x0 + x1) // 2))
    # right panel: concentration profile erfc at 3 times
    X0, X1, Y0, Y1 = 390, 640, 30, 230
    out.append('<line class="ic-axis" x1="%d" y1="%d" x2="%d" y2="%d"/><line class="ic-axis" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (X0, Y0, X0, Y1, X0, Y1, X1, Y1))

    def erfc(z):
        return math.erfc(z)

    for t, cls in ((1, "dif-t1"), (4, "dif-t2"), (16, "dif-t3")):
        pts = []
        for i in range(0, 61):
            x = i / 60.0 * 3.0  # distance
            c = erfc(x / (2 * math.sqrt(0.18 * t)))
            pts.append("%s,%s" % (f1(X0 + x / 3.0 * (X1 - X0)), f1(Y1 - c * (Y1 - Y0 - 10))))
        out.append('<polyline class="dif %s" points="%s"/>' % (cls, " ".join(pts)))
    out.append('<text class="fm-note" x="%d" y="%d">longer time</text><path class="fm-dim2" d="M%d,%d L%d,%d" marker-end="url(#dfA)"/>' % (X0 + 150, 112, X0 + 148, 106, X0 + 112, 80))
    out.append('<text class="fm-note" x="%d" y="%d">surface held at C<tspan class="fm-sub" dy="3">s</tspan></text>' % (X0 + 40, Y0 + 14))
    out.append('<text class="ic-lab" x="%d" y="%d" text-anchor="middle">distance into the solid, x</text>' % ((X0 + X1) // 2, Y1 + 28))
    out.append('<text class="ic-lab" transform="rotate(-90 366 130)" x="366" y="130" text-anchor="middle">concentration C</text>')
    out.append('<text class="fm-h" x="%d" y="18" text-anchor="middle">Diffusion in from a fixed surface</text>' % ((X0 + X1) // 2))
    out.append('<text class="fm-note" x="%d" y="%d" text-anchor="middle">reach &asymp; &radic;(D&middot;t)</text>' % ((X0 + X1) // 2 + 60, Y1 - 36))
    svg = ('<svg viewBox="0 0 680 280" role="img" aria-label="Left: on a plot of ln D against 1/T diffusion in a solid is a straight line whose slope is minus Q over R; interstitial diffusion has a shallow line and self-diffusion a steep one. Right: concentration against depth when atoms diffuse in from a surface held at fixed concentration; the profile spreads deeper as time passes, roughly as the square root of D times t.">'
           '<defs><marker id="dfA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>'
           + "".join(out) + '</svg>')
    save("diffusion", svg)


# ----------------------------------------------------- hole sites (sketch)
def fig_holes():
    out = []
    # three little coordination sketches: cubic (8), octahedral (6), tetrahedral (4)
    def atoms_around(cx, cy, pts, r=9):
        return "".join('<line class="cx-bond" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (cx, cy, x, y) for x, y in pts) + \
            "".join('<circle class="cx-atom cx-corner" cx="%d" cy="%d" r="%d"/>' % (x, y, r) for x, y in pts) + \
            '<circle class="cx-atom cx-centre" cx="%d" cy="%d" r="6"/>' % (cx, cy)

    # cubic hole: 8 corners of a small cube
    cx, cy = 110, 100
    pts = [(cx - 44, cy - 30), (cx + 28, cy - 30), (cx - 44, cy + 42), (cx + 28, cy + 42), (cx - 22, cy - 52), (cx + 50, cy - 52), (cx - 22, cy + 20), (cx + 50, cy + 20)]
    out.append(atoms_around(cx, cy, pts))
    out.append('<text class="fm-h" x="%d" y="190" text-anchor="middle">cubic hole</text><text class="fm-note" x="%d" y="208" text-anchor="middle">8 neighbours</text><text class="fm-note" x="%d" y="224" text-anchor="middle">centre of simple cubic (CsCl)</text>' % (cx, cx, cx))
    cx = 380
    pts = [(cx, cy - 56), (cx, cy + 56), (cx - 56, cy), (cx + 56, cy), (cx - 30, cy + 26), (cx + 30, cy - 26)]
    out.append(atoms_around(cx, cy, pts))
    out.append('<text class="fm-h" x="%d" y="190" text-anchor="middle">octahedral hole</text><text class="fm-note" x="%d" y="208" text-anchor="middle">6 neighbours</text><text class="fm-note" x="%d" y="224" text-anchor="middle">all filled in FCC &rarr; NaCl</text>' % (cx, cx, cx))
    cx = 650
    pts = [(cx - 50, cy + 40), (cx + 50, cy + 40), (cx, cy - 56), (cx + 18, cy + 8)]
    out.append(atoms_around(cx, cy, pts))
    out.append('<text class="fm-h" x="%d" y="190" text-anchor="middle">tetrahedral hole</text><text class="fm-note" x="%d" y="208" text-anchor="middle">4 neighbours</text><text class="fm-note" x="%d" y="224" text-anchor="middle">half filled in FCC &rarr; ZnS</text>' % (cx, cx, cx))
    svg = ('<svg viewBox="0 0 760 240" role="img" aria-label="Three kinds of gap between large atoms: a cubic hole surrounded by 8 atoms, an octahedral hole surrounded by 6, and a tetrahedral hole surrounded by 4.">' + "".join(out) + '</svg>')
    save("holes", svg)


if __name__ == "__main__":
    for fn in (fig_cells, fig_bragg, fig_miller, fig_pointdef, fig_dislocation, fig_visc, fig_diffusion, fig_holes):
        fn()
    print("wrote", sorted(os.listdir(OUT)))
