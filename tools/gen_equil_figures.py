#!/usr/bin/env python3
"""Figures for Unit 14 (chemical equilibrium). Writes build/figs/eq_*.svg.html. Classes: ex-* in tools/figs_new.css."""
import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build", "figs")
os.makedirs(OUT, exist_ok=True)


def save(name, svg):
    open(os.path.join(OUT, name + ".svg.html"), "w").write(svg)


def fig_kscale():
    out = []
    zones = [(30, 230, "ex-zl", "K &lt; 10<tspan class=\"fm-sub\" dy=\"-5\">&minus;3</tspan>", "mostly reactants"),
             (240, 440, "ex-zm", "10<tspan class=\"fm-sub\" dy=\"-5\">&minus;3</tspan><tspan dy=\"5\"> &le; K &le; 10</tspan><tspan class=\"fm-sub\" dy=\"-5\">3</tspan>", "some of each"),
             (450, 650, "ex-zr", "K &gt; 10<tspan class=\"fm-sub\" dy=\"-5\">3</tspan>", "mostly products")]
    for x0, x1, cls, lab, sub in zones:
        out.append('<rect class="%s" x="%d" y="46" width="%d" height="92" rx="8"/>' % (cls, x0, x1 - x0))
        out.append('<text class="fm-h" x="%d" y="34" text-anchor="middle">%s</text>' % ((x0 + x1) // 2, lab))
        out.append('<text class="fm-note" x="%d" y="156" text-anchor="middle">%s</text>' % ((x0 + x1) // 2, sub))
    out.append('<path class="fm-dim2" d="M30,176 H650" marker-end="url(#exA)"/><text class="ic-lab" x="340" y="194" text-anchor="middle">magnitude of K increases (schematic, not to scale)</text>')
    dots = [(80, "F<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> &rlarr; 2F</tspan>", "7.4&times;10<tspan class=\"fm-sub\" dy=\"-5\">&minus;13</tspan>"),
            (180, "I<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> &rlarr; 2I</tspan>", "4.6&times;10<tspan class=\"fm-sub\" dy=\"-5\">&minus;7</tspan>"),
            (290, "H<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\">+I</tspan><tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> &rlarr; 2HI</tspan>", "0.29"),
            (390, "H<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\">+D</tspan><tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> &rlarr; 2HD</tspan>", "1.92"),
            (500, "N<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\">+3H</tspan><tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> &rlarr; 2NH</tspan><tspan class=\"fm-sub\" dy=\"3\">3</tspan>", "2.7&times;10<tspan class=\"fm-sub\" dy=\"-5\">8</tspan>"),
            (600, "2H<tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\">+O</tspan><tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\"> &rarr; 2H</tspan><tspan class=\"fm-sub\" dy=\"3\">2</tspan><tspan dy=\"-3\">O</tspan>", "2.4&times;10<tspan class=\"fm-sub\" dy=\"-5\">47</tspan>")]
    for i, (x, name, kv) in enumerate(dots):
        out.append('<text class="kx-slope" x="%d" y="74" text-anchor="middle">%s</text>' % (x, name))
        out.append('<text class="fm-note" x="%d" y="92" text-anchor="middle">K = %s</text>' % (x, kv))
        out.append('<circle class="ex-dot" cx="%d" cy="116" r="6"/>' % x)
    svg = ('<svg viewBox="0 0 680 210" role="img" aria-label="Scale of the equilibrium constant: K below 10 to the minus 3 means mostly reactants, K between 10 to the minus 3 and 10 cubed means significant amounts of both, K above 10 cubed means mostly products, with example reactions from the L24 slide placed on it.">'
           '<defs><marker id="exA" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>' + "".join(out) + '</svg>')
    save("eq_kscale", svg)


def fig_qk():
    out = []
    x0, y0, x1, y1 = 60, 20, 520, 250
    out.append('<path class="fm-ax" d="M%d,%d V%d M%d,%d H%d"/>' % (x0, y1, y0, x0, y1, x1))
    ky = 135
    out.append('<line class="ex-k" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x0, ky, x1 + 6, ky))
    n = 60
    up, dn = [], []
    for i in range(n + 1):
        t = i / float(n)
        e = 2.718281828 ** (-4.2 * t)
        up.append((x0 + 12 + t * (x1 - x0 - 24), ky - 100 * e))
        dn.append((x0 + 12 + t * (x1 - x0 - 24), ky + 95 * e))
    f = lambda p: " ".join("%.1f,%.1f" % q for q in p)
    out.append('<polyline class="ex-curve" points="%s"/><polyline class="ex-curve" points="%s"/>' % (f(up), f(dn)))
    out.append('<text class="fm-h" x="%d" y="%d">Q &gt; K</text><text class="fm-note" x="%d" y="%d">too many products: reaction runs left</text>' % (x0 + 90, y0 + 32, x0 + 90, y0 + 50))
    out.append('<text class="fm-h" x="%d" y="%d">Q &lt; K</text><text class="fm-note" x="%d" y="%d">too few products: reaction runs right</text>' % (x0 + 90, y1 - 38, x0 + 90, y1 - 20))
    out.append('<text class="ex-kt" x="%d" y="%d">Q = K</text><text class="fm-note" x="%d" y="%d">equilibrium</text>' % (x1 + 12, ky + 2, x1 + 12, ky + 18))
    out.append('<text class="ic-lab" x="%d" y="%d" text-anchor="middle">time</text><text class="ic-lab" transform="rotate(-90 16 135)" x="16" y="135" text-anchor="middle">reaction quotient Q</text>' % ((x0 + x1) // 2, y1 + 22))
    svg = ('<svg viewBox="0 0 620 280" role="img" aria-label="Reaction quotient Q against time: starting above K it falls toward K, starting below K it rises toward K, and the two curves meet the line Q equals K at equilibrium.">' + "".join(out) + '</svg>')
    save("eq_qk", svg)


if __name__ == "__main__":
    fig_kscale()
    fig_qk()
    print(sorted(os.listdir(OUT)))
