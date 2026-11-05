#!/usr/bin/env python3
"""Figures for Units 12-13 (kinetics, thermodynamics). Writes build/figs/*.svg.html.
Styles come from tools/figs_new.css (classes kx-*)."""
import math, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build", "figs")
os.makedirs(OUT, exist_ok=True)


def save(name, svg):
    open(os.path.join(OUT, name + ".svg.html"), "w").write(svg)


def f1(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


def axes(x0, y0, x1, y1):
    return '<path class="fm-ax" d="M%d,%d V%d M%d,%d H%d"/>' % (x0, y1, y0, x0, y1, x1)


def poly(pts, cls):
    return '<polyline class="%s" points="%s"/>' % (cls, " ".join("%s,%s" % (f1(x), f1(y)) for x, y in pts))


# ------------------------------------------------------------ energy profile with and without a catalyst
def fig_energy():
    x0, x1, y0, y1 = 60, 560, 20, 270
    out = [axes(x0, y0, x1, y1)]

    def bump(h, w, cx, ya, yb):
        """smooth profile from level ya (left) to yb (right) with a peak of height h above ya at cx."""
        pts = []
        for i in range(0, 101):
            x = x0 + 30 + (x1 - x0 - 60) * i / 100.0
            t = (x - cx) / w
            base = ya + (yb - ya) * (0.5 + 0.5 * math.tanh((x - cx) / (w * 0.9)))
            pts.append((x, base - h * math.exp(-t * t)))
        return pts

    ya, yb = 190, 235      # reactants and products levels (y grows downward: products lower in energy)
    out.append(poly(bump(120, 55, 300, ya, yb), "kx-curve"))
    out.append(poly(bump(62, 55, 300, ya, yb), "kx-cat"))
    out.append('<line class="fm-dim" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0 + 20, ya, x1 - 30, ya))
    out.append('<line class="fm-dim" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0 + 20, yb, x1 - 30, yb))
    # Ea arrow (uncatalysed)
    out.append('<path class="fm-dim2" d="M330,%d V%d" marker-start="url(#kxA)" marker-end="url(#kxA)"/>' % (ya, ya - 120))
    out.append('<text class="fm-h" x="340" y="%d">E<tspan class="fm-sub" dy="3">a</tspan></text>' % (ya - 56))
    out.append('<path class="kx-catline" d="M290,%d V%d" marker-start="url(#kxA)" marker-end="url(#kxA)"/>' % (ya, ya - 62))
    out.append('<line class="kx-curve" x1="90" y1="42" x2="124" y2="42"/><text class="fm-note" x="132" y="46">no catalyst</text><line class="kx-cat" x1="90" y1="62" x2="124" y2="62"/><text class="kx-cat-t" x="132" y="66">catalyst: lower E<tspan class="fm-sub" dy="3">a</tspan></text>')
    out.append('<path class="fm-dim2" d="M540,%d V%d" marker-start="url(#kxA)" marker-end="url(#kxA)"/>' % (ya, yb))
    out.append('<text class="fm-h" x="548" y="%d">&Delta;E&lt;0</text>' % ((ya + yb) // 2 + 4))
    out.append('<text class="fm-note" x="%d" y="%d">reactants</text><text class="fm-note" x="%d" y="%d" text-anchor="end">products</text>' % (x0 + 24, ya - 8, x1 - 30, yb + 18))
    out.append('<text class="fm-note" x="360" y="%d">activated complex</text>' % (ya - 128))
    out.append('<text class="ic-lab" x="%d" y="%d" text-anchor="middle">reaction coordinate</text><text class="ic-lab" transform="rotate(-90 20 150)" x="20" y="150" text-anchor="middle">potential energy</text>' % ((x0 + x1) // 2, y1 + 24))
    svg = ('<svg viewBox="0 0 600 310" role="img" aria-label="Energy profile of an exothermic reaction: reactants climb an activation-energy barrier to the activated complex, then fall to lower-energy products. A catalyst gives a lower barrier but the same overall energy change.">'
           '<defs><marker id="kxA" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>'
           + "".join(out) + '</svg>')
    save("kin_energy", svg)


# ------------------------------------------------------------ integrated laws: curves and straight lines
def fig_orders():
    out = []
    cols = [("Zeroth order", 20), ("First order", 250), ("Second order", 480)]
    W, H = 200, 110
    for ci, (title, ox) in enumerate(cols):
        out.append('<text class="fm-h" x="%d" y="16" text-anchor="middle">%s</text>' % (ox + W // 2, title))
        # top: concentration vs time
        top = 30
        out.append(axes(ox, top, ox + W, top + H))
        pts = []
        for i in range(0, 61):
            t = i / 60.0
            if ci == 0:
                a = max(0.0, 1 - 1.0 * t * 1.0)
            elif ci == 1:
                a = math.exp(-3 * t)
            else:
                a = 1 / (1 + 6 * t)
            pts.append((ox + t * W, top + H - a * (H - 8)))
        out.append(poly(pts, "kx-curve"))
        out.append('<text class="fm-note" x="%d" y="%d" text-anchor="middle">[A] vs t</text>' % (ox + W // 2, top + H + 16))
        # bottom: linearised
        bt = 185
        out.append(axes(ox, bt, ox + W, bt + H))
        if ci == 0:
            ln = [(ox + 4, bt + 12), (ox + W - 4, bt + H - 12)]
            lab, sl = "[A] vs t", "slope = &minus;k"
        elif ci == 1:
            ln = [(ox + 4, bt + 12), (ox + W - 4, bt + H - 12)]
            lab, sl = "ln[A] vs t", "slope = &minus;k"
        else:
            ln = [(ox + 4, bt + H - 12), (ox + W - 4, bt + 12)]
            lab, sl = "1/[A] vs t", "slope = +k"
        out.append(poly(ln, "kx-line"))
        out.append('<text class="kx-slope" x="%d" y="%d" text-anchor="middle">%s</text>' % (ox + W // 2, bt + 36 if ci < 2 else bt + H - 18, sl))
        out.append('<text class="fm-note" x="%d" y="%d" text-anchor="middle">%s</text>' % (ox + W // 2, bt + H + 16, lab))
    out.append('<text class="fm-cap-s" x="350" y="338" text-anchor="middle">the plot that comes out straight tells you the order</text>')
    svg = ('<svg viewBox="0 0 700 350" role="img" aria-label="Concentration against time for zeroth, first and second order reactions, and the straight-line plot for each: [A] against t, ln[A] against t, 1/[A] against t.">' + "".join(out) + '</svg>')
    save("kin_orders", svg)


# ------------------------------------------------------------ Arrhenius
def fig_arrhenius():
    out = []
    x0, y0, x1, y1 = 50, 30, 300, 230
    out.append(axes(x0, y0, x1, y1))
    pts = []
    for i in range(0, 61):
        T = 280 + 120 * i / 60.0
        k = math.exp(-5000 / T)
        pts.append((x0 + (T - 280) / 120.0 * (x1 - x0 - 10), y1 - (k / math.exp(-5000 / 400.0)) * (y1 - y0 - 10)))
    out.append(poly(pts, "kx-curve"))
    out.append('<text class="fm-h" x="175" y="18" text-anchor="middle">k = A e<tspan class="fm-sub" dy="-4">&minus;Ea/RT</tspan></text>')
    out.append('<text class="ic-lab" x="175" y="256" text-anchor="middle">temperature T</text><text class="ic-lab" transform="rotate(-90 14 130)" x="14" y="130" text-anchor="middle">k</text>')
    X0, X1 = 390, 640
    out.append(axes(X0, y0, X1, y1))
    out.append(poly([(X0 + 10, 70), (X1 - 10, 190)], "kx-line"))
    out.append(poly([(X0 + 10, 70), (X1 - 10, 135)], "kx-cat"))
    out.append('<text class="kx-slope" x="%d" y="218">slope = &minus;E<tspan class="fm-sub" dy="3">a</tspan><tspan dy="-3">/R (steeper: larger E</tspan><tspan class="fm-sub" dy="3">a</tspan><tspan dy="-3">)</tspan></text>' % (X0 + 6))
    out.append('<text class="kx-cat-t" x="%d" y="50">catalyst: smaller E<tspan class="fm-sub" dy="3">a</tspan><tspan dy="-3">, shallower</tspan></text>' % (X0 + 40))
    out.append('<text class="fm-h" x="515" y="18" text-anchor="middle">ln k = ln A &minus; (E<tspan class="fm-sub" dy="3">a</tspan><tspan dy="-3">/R)(1/T)</tspan></text>')
    out.append('<text class="ic-lab" x="515" y="256" text-anchor="middle">1/T  (hot on the left)</text><text class="ic-lab" transform="rotate(-90 360 130)" x="360" y="130" text-anchor="middle">ln k</text>')
    svg = ('<svg viewBox="0 0 680 275" role="img" aria-label="Left: the rate constant k rises steeply with temperature. Right: on a plot of ln k against 1/T the data fall on a straight line with slope minus Ea over R and intercept ln A; a catalyst gives a shallower line.">' + "".join(out) + '</svg>')
    save("kin_arrhenius", svg)


# ------------------------------------------------------------ DG = DH - T DS
def fig_gt():
    out = []
    x0, y0, x1, y1 = 60, 25, 560, 250
    out.append(axes(x0, y0, x1, y1))
    # y axis: kJ/mol 30..50 ; DH falls slightly, TDS rises (schematic for vaporisation)
    X = lambda T: x0 + (T - 300) / 150.0 * (x1 - x0 - 20)
    Y = lambda v: y1 - (v - 30) / 20.0 * (y1 - y0 - 10)
    out.append(poly([(X(300), Y(43.9)), (X(450), Y(36.5))], "kx-line"))
    out.append(poly([(X(300), Y(32.7)), (X(450), Y(48.9))], "kx-cat"))
    Tx = 373
    out.append('<line class="fm-dim" x1="%s" y1="%d" x2="%s" y2="%d"/>' % (f1(X(Tx)), y0, f1(X(Tx)), y1))
    out.append('<text class="fm-note" x="%s" y="%d" text-anchor="middle">&Delta;G = 0 (equilibrium)</text>' % (f1(X(Tx)), y0 - 6))
    out.append('<text class="kx-slope" x="%s" y="%s">&Delta;H</text>' % (f1(X(305)), f1(Y(45.0))))
    out.append('<text class="kx-cat-t" x="%s" y="%s">T&Delta;S</text>' % (f1(X(305)), f1(Y(31.0))))
    out.append('<text class="fm-cap-s" x="%s" y="%s">&Delta;G &gt; 0</text>' % (f1(X(308)), f1(Y(39.4))))
    out.append('<text class="fm-cap-s" x="%s" y="%s">&Delta;G &lt; 0</text>' % (f1(X(412)), f1(Y(42.4))))
    out.append('<text class="ic-lab" x="310" y="278" text-anchor="middle">temperature (K)</text><text class="ic-lab" transform="rotate(-90 18 140)" x="18" y="140" text-anchor="middle">kJ/mol</text>')
    svg = ('<svg viewBox="0 0 600 292" role="img" aria-label="Schematic of liquid water evaporating: the enthalpy term and the temperature-times-entropy term cross at about 373 K, where the free-energy change is zero; above that temperature the process is spontaneous.">' + "".join(out) + '</svg>')
    save("thermo_gt", svg)


if __name__ == "__main__":
    for fn in (fig_energy, fig_orders, fig_arrhenius, fig_gt):
        fn()
    print(sorted(os.listdir(OUT)))
