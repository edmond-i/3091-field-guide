#!/usr/bin/env python3
"""Figures for Unit 15 (catalysis, ammonia). Writes build/figs/cat_*.svg.html. Classes ca-* in tools/figs_new.css."""
import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build", "figs")
os.makedirs(OUT, exist_ok=True)


def save(name, svg):
    open(os.path.join(OUT, name + ".svg.html"), "w").write(svg)


def sub(t):
    return t


def fig_loop():
    o = []
    def box(x, y, w, h, l1, l2=""):
        o.append('<rect class="ca-box" x="%d" y="%d" width="%d" height="%d" rx="8"/>' % (x, y, w, h))
        o.append('<text class="fm-h" x="%d" y="%d" text-anchor="middle">%s</text>' % (x + w // 2, y + (20 if l2 else h // 2 + 5), l1))
        if l2:
            o.append('<text class="fm-note" x="%d" y="%d" text-anchor="middle">%s</text>' % (x + w // 2, y + 38, l2))
    box(10, 60, 100, 56, "N<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> + H</tspan><tspan class=\"fm-sub\" dy=\"3\">2</tspan>", "feed gases")
    box(145, 60, 110, 56, "Compressor", "high pressure")
    box(290, 40, 170, 96, "Reactor", "Fe catalyst, 400&ndash;500 &deg;C")
    box(495, 60, 130, 56, "Condenser", "cool: NH<tspan class=\"fm-sub\" dy=\"3\">3</tspan><tspan dy=\"-3\"> &rarr; liquid</tspan>")
    for (a, b) in [(110, 145), (255, 290), (460, 495)]:
        o.append('<path class="ca-arr" d="M%d,88 H%d" marker-end="url(#caA)"/>' % (a + 2, b - 2))
    o.append('<path class="ca-arr" d="M560,116 V176" marker-end="url(#caA)"/>')
    o.append('<rect class="ca-prod" x="495" y="178" width="130" height="40" rx="8"/><text class="fm-h" x="560" y="203" text-anchor="middle">NH<tspan class="fm-sub" dy="3">3</tspan><tspan dy="-3">(l): product</tspan></text>')
    o.append('<path class="ca-rec" d="M495,104 H478 V232 H200 V116" marker-end="url(#caA)"/>')
    o.append('<text class="kx-slope" x="340" y="252" text-anchor="middle">unreacted N<tspan class="fm-sub" dy="3">2</tspan><tspan dy="-3"> and H</tspan><tspan class="fm-sub" dy="3">2</tspan><tspan dy="-3"> are recycled</tspan></text>')
    svg = ('<svg viewBox="0 0 650 270" role="img" aria-label="Haber-Bosch loop: nitrogen and hydrogen are compressed, pass over an iron catalyst at 400 to 500 degrees Celsius, the mixture is cooled so ammonia condenses to a liquid and is removed, and the unreacted nitrogen and hydrogen are recycled back to the reactor.">'
           '<defs><marker id="caA" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>' + "".join(o) + '</svg>')
    save("cat_loop", svg)


def fig_ertl():
    o = []
    # levels (kJ per mol NH3, relative to 1/2 N2 + 3/2 H2 = 0), read approximately from L25 slide 5
    L = [("&frac12;N<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> + 3/2H</tspan><tspan class=\"fm-sub\" dy=\"3\">2</tspan>", "(gas)", 0),
         ("&frac12;N<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\">(ad)</tspan>", "+ 3/2H<tspan class=\"fm-sub\" dy=\"3\">2</tspan>", -17),
         ("N(ad)", "+ 3H(ad)", -276),
         ("NH(ad)", "+ 2H(ad)", -170),
         ("NH<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\">(ad)</tspan>", "+ H(ad)", -137),
         ("NH<tspan class=\"fm-sub\" dy=\"3\">3</tspan><tspan dy=\"-3\">(ad)</tspan>", "", -50),
         ("NH<tspan class=\"fm-sub\" dy=\"3\">3</tspan><tspan dy=\"-3\">(g)</tspan>", "", -46)]
    x0, y0, k = 60, 50, 0.6
    Y = lambda e: y0 - e * k
    xs = [x0 + 62 + i * 88 for i in range(len(L))]
    o.append('<path class="fm-ax" d="M%d,%d V%d"/>' % (x0, 24, 232))
    o.append('<line class="fm-dim" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0, Y(0), 690, Y(0)))
    pts = []
    for i, (a, b, e) in enumerate(L):
        x = xs[i]
        o.append('<line class="ca-lev" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>' % (x - 26, Y(e), x + 26, Y(e)))
        o.append('<text class="fm-note" x="%d" y="%d" text-anchor="middle">%s</text>' % (x, 250, a))
        if b:
            o.append('<text class="fm-note" x="%d" y="%d" text-anchor="middle">%s</text>' % (x, 264, b))
        o.append('<text class="kx-slope" x="%d" y="%.1f" text-anchor="middle">%s</text>' % (x, Y(e) - 8, ("&asymp;%d" % e) if e else "0"))
        pts.append((x - 26, Y(e))); pts.append((x + 26, Y(e)))
    # connecting curve with small humps (barriers are small on the slide)
    d = "M%.1f,%.1f" % pts[0]
    for i in range(1, len(pts)):
        px, py = pts[i - 1]; cx, cy = pts[i]
        if i % 2 == 1:
            d += " L%.1f,%.1f" % (cx, cy)
        else:
            top = min(py, cy) - 7
            d += " C%.1f,%.1f %.1f,%.1f %.1f,%.1f" % (px + 10, top, cx - 10, top, cx, cy)
    o.append('<path class="ca-curve" d="%s"/>' % d)
    o.append('<text class="ic-lab" transform="rotate(-90 22 130)" x="22" y="130" text-anchor="middle">kJ per mol NH<tspan class="fm-sub" dy="3">3</tspan></text>')
    o.append('<text class="fm-note" x="%d" y="%d" text-anchor="end">free atoms N + 3H would sit at +1129 (off the chart)</text>' % (700, 18))
    svg = ('<svg viewBox="0 0 710 280" role="img" aria-label="Approximate energy levels for ammonia formation on an iron surface from the L25 slide: separated atoms adsorbed on the surface are far lower in energy than the gases, then successive N-H bond formation climbs in small steps up to adsorbed NH3 and finally gaseous NH3 about 46 kJ per mole below the starting gases.">' + "".join(o) + '</svg>')
    save("cat_ertl", svg)


def fig_volcano():
    o = []
    x0, y0, x1, y1 = 60, 20, 560, 220
    mid = 300
    o.append('<rect class="ca-zs" x="%d" y="%d" width="%d" height="%d"/><rect class="ca-zw" x="%d" y="%d" width="%d" height="%d"/>' % (x0, 70, mid - x0, y1 - 70, mid, 70, x1 - mid, y1 - 70))
    o.append('<path class="fm-ax" d="M%d,%d V%d M%d,%d H%d"/>' % (x0, y1, y0, x0, y1, x1))
    pts = []
    for i in range(0, 101):
        t = i / 100.0
        x = x0 + 8 + t * (x1 - x0 - 16)
        y = y1 - 8 - 170 * (1 - ((t - 0.46) / 0.54 if t > 0.46 else (0.46 - t) / 0.46) ** 2) * 1.0
        pts.append("%.1f,%.1f" % (x, y))
    o.append('<polyline class="ex-curve" points="%s"/>' % " ".join(pts))
    o.append('<text class="fm-h" x="%d" y="%d" text-anchor="middle">Sabatier optimum</text>' % (x0 + 8 + 0.46 * (x1 - x0 - 16), 28))
    o.append('<text class="kx-slope" x="%d" y="%d" text-anchor="middle">limited by desorption</text><text class="kx-slope" x="%d" y="%d" text-anchor="middle">of the product</text>' % ((x0 + mid) // 2 - 10, 178, (x0 + mid) // 2 - 10, 194))
    o.append('<text class="kx-slope" x="%d" y="%d" text-anchor="middle">limited by activation</text><text class="kx-slope" x="%d" y="%d" text-anchor="middle">of the reactant</text>' % ((mid + x1) // 2 + 20, 178, (mid + x1) // 2 + 20, 194))
    o.append('<text class="fm-note" x="%d" y="%d">strong</text><text class="fm-note" x="%d" y="%d" text-anchor="end">weak</text>' % (x0 + 4, y1 + 16, x1, y1 + 16))
    o.append('<text class="ic-lab" x="%d" y="%d" text-anchor="middle">bond strength of reactant to the catalyst surface</text><text class="ic-lab" transform="rotate(-90 22 120)" x="22" y="120" text-anchor="middle">rate</text>' % ((x0 + x1) // 2, y1 + 34))
    svg = ('<svg viewBox="0 0 600 262" role="img" aria-label="Volcano plot: reaction rate against how strongly the reactant binds to the catalyst surface. Very strong binding is limited by the product leaving the surface, very weak binding is limited by activating the reactant, and the rate peaks at an intermediate binding strength, the Sabatier optimum.">' + "".join(o) + '</svg>')
    save("cat_volcano", svg)


if __name__ == "__main__":
    fig_loop(); fig_ertl(); fig_volcano()
    print("ok")
