#!/usr/bin/env python3
"""Figures for Units 16-17 (solutions, acids and bases). Writes build/figs/sol_*.svg.html and ab_*.svg.html. Classes sl-*, ab-* in tools/figs_new.css."""
import math, os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build", "figs")
os.makedirs(OUT, exist_ok=True)


def save(name, svg):
    open(os.path.join(OUT, name + ".svg.html"), "w").write(svg)


def fig_solvation():
    o = []
    marker = '<defs><marker id="slA" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" class="fm-arrow-h"/></marker></defs>'

    def panel(oy, title, y_sol, tag):
        y_start, y_top = oy + 150, oy + 50
        o.append('<text class="fm-h" x="240" y="%d" text-anchor="middle">%s</text>' % (oy + 14, title))
        for x1, x2, y, cls, lab in [(10, 90, y_start, "sl-lev", "pure solvent + pure solute"), (160, 240, y_top, "sl-lev", "separated particles"), (310, 390, y_sol, "sl-sol", "solution")]:
            o.append('<line class="%s" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (cls, x1, y, x2, y))
        o.append('<text class="fm-note" x="50" y="%d" text-anchor="middle">pure solvent</text><text class="fm-note" x="50" y="%d" text-anchor="middle">+ pure solute</text>' % (y_start + 14, y_start + 26))
        o.append('<text class="fm-note" x="200" y="%d" text-anchor="middle">separated</text><text class="fm-note" x="200" y="%d" text-anchor="middle">particles</text>' % (y_top - 18, y_top - 6))
        o.append('<text class="fm-note" x="350" y="%d" text-anchor="middle">solution</text>' % (y_sol + 16))
        o.append('<path class="ca-arr" d="M125,%d V%d" marker-end="url(#slA)"/><text class="kx-slope" x="133" y="%d">1 + 2: &Delta;H &gt; 0</text>' % (y_start - 4, y_top + 4, (y_start + y_top) // 2 - 2))
        o.append('<text class="fm-note" x="133" y="%d">(pull apart)</text>' % ((y_start + y_top) // 2 + 12))
        o.append('<path class="ca-arr" d="M275,%d V%d" marker-end="url(#slA)"/><text class="kx-slope" x="283" y="%d">3: &Delta;H &lt; 0</text>' % (y_top + 4, y_sol - 4, (y_top + y_sol) // 2 - 2))
        o.append('<text class="fm-note" x="283" y="%d">(A&ndash;B attract)</text>' % ((y_top + y_sol) // 2 + 12))
        o.append('<path class="ex-k" d="M430,%d V%d" marker-end="url(#slA)"/><text class="ex-kt" x="440" y="%d">&Delta;H<tspan class="fm-sub" dy="3">soln</tspan><tspan dy="-3"> %s</tspan></text>' % (y_start, y_sol, (y_start + y_sol) // 2 + 4, tag))
    panel(0, "Exothermic dissolving: step 3 wins", 190, "&lt; 0")
    panel(215, "Endothermic dissolving: steps 1 + 2 win", 215 + 125, "&gt; 0")
    svg = ('<svg viewBox="0 0 520 430" role="img" aria-label="Enthalpy diagrams for dissolving: pull the solvent apart and pull the solute apart (both cost energy), then let solvent and solute attract each other (releases energy). If the release is larger the solution ends lower than the start (exothermic); if smaller it ends higher (endothermic).">' + marker + "".join(o) + '</svg>')
    save("sol_solvation", svg)


def fig_titration():
    o = []
    x0, y0, x1, y1 = 60, 20, 400, 230
    X = lambda v: x0 + v / 50.0 * (x1 - x0)
    Y = lambda ph: y1 - ph / 14.0 * (y1 - y0)
    o.append('<path class="fm-ax" d="M%d,%d V%d M%d,%d H%d"/>' % (x0, y1, y0, x0, y1, x1))
    Ka = 10 ** -4.76
    Kw = 1e-14
    nA = 2.5  # mmol of acid in 25 mL of 0.100 M
    strong, weak = [], []
    for i in range(0, 501):
        v = i / 10.0
        tot = 25.0 + v
        nb = 0.1 * v
        # strong acid
        d = (nA - nb) / tot
        if abs(d) < 1e-12:
            ph = 7.0
        elif d > 0:
            ph = -math.log10(max(d, 1e-14) if d > 1e-7 else 1e-7)
        else:
            ph = 14 + math.log10(max(-d, 1e-7))
        if abs(v - 25) < 0.05:
            ph = 7.0
        strong.append((X(v), Y(ph)))
        # weak acid
        if v == 0:
            h = (-Ka + math.sqrt(Ka * Ka + 4 * Ka * 0.1)) / 2
            w = -math.log10(h)
        elif nb < nA - 1e-9:
            w = 4.76 + math.log10(nb / (nA - nb))
        elif abs(nb - nA) <= 1e-9:
            Kb = Kw / Ka
            w = 14 + math.log10(math.sqrt(Kb * nA / tot))
        else:
            w = 14 + math.log10((nb - nA) / tot)
        weak.append((X(v), Y(w)))
    f = lambda p: " ".join("%.1f,%.1f" % q for q in p)
    o.append('<polyline class="ab-s" points="%s"/><polyline class="ab-w" points="%s"/>' % (f(strong), f(weak)))
    o.append('<line class="fm-dim" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/><text class="fm-note" x="%d" y="%.1f">pH 7</text>' % (x0, Y(7), x1, Y(7), x1 - 28, Y(7) - 4))
    o.append('<line class="fm-dim" x1="%.1f" y1="%d" x2="%.1f" y2="%d"/><text class="fm-note" x="%.1f" y="%d">equivalence: 25 mL</text>' % (X(25), y0, X(25), y1, X(25) + 6, y0 + 10))
    o.append('<circle class="ab-dot" cx="%.1f" cy="%.1f" r="4.5"/><text class="kx-slope" x="%.1f" y="%.1f">midpoint: pH = pK<tspan class="fm-sub" dy="3">a</tspan></text>' % (X(12.5), Y(4.76), X(12.5) - 40, Y(4.76) + 24))
    o.append('<circle class="ab-dot2" cx="%.1f" cy="%.1f" r="4.5"/><text class="kx-slope" x="%.1f" y="%.1f">weak: pH &gt; 7</text>' % (X(25), Y(8.73), X(25) + 8, Y(8.73) - 4))
    o.append('<text class="ab-st" x="%.1f" y="%.1f">strong: pH = 7</text>' % (X(26), Y(7) + 14))
    for ph in (0, 2, 4, 6, 8, 10, 12, 14):
        o.append('<text class="fm-note" x="%d" y="%.1f" text-anchor="end">%d</text>' % (x0 - 4, Y(ph) + 4, ph))
    for v in (0, 10, 20, 30, 40, 50):
        o.append('<text class="fm-note" x="%.1f" y="%d" text-anchor="middle">%d</text>' % (X(v), y1 + 14, v))
    o.append('<text class="ic-lab" x="%d" y="%d" text-anchor="middle">volume of NaOH added (mL), 25 mL of 0.100 M acid</text><text class="ic-lab" transform="rotate(-90 18 125)" x="18" y="125" text-anchor="middle">pH</text>' % ((x0 + x1) // 2, y1 + 32))
    svg = ('<svg viewBox="0 0 420 268" role="img" aria-label="Titration curves for a strong acid and a weak acid (pKa 4.76) with strong base: the strong acid curve jumps at 25 mL through pH 7; the weak acid curve starts higher, has a buffer plateau whose midpoint pH equals pKa, and its equivalence point is above pH 7.">' + "".join(o) + '</svg>')
    save("ab_titration", svg)


if __name__ == "__main__":
    fig_solvation(); fig_titration()
    print("ok")
