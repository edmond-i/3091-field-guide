"""Figures for the 3.091 Field Guide: sigma/pi orbital pictures, MO energy diagrams, % ionic curve.
Phase colours: blue = +, red = -  (phase of the wavefunction, NOT electric charge).
"""
import math


def f(v):
    return f"{v:.1f}"


# ---------------------------------------------------------------- orbital lobes
def lobe(cx, cy, rx, ry, sign, label=True):
    cls = "ph-pos" if sign > 0 else "ph-neg"
    t = ""
    if label:
        t = f'<text class="ph-txt" x="{f(cx)}" y="{f(cy + 3.6)}" text-anchor="middle">{"+" if sign > 0 else "&minus;"}</text>'
    return f'<ellipse class="{cls}" cx="{f(cx)}" cy="{f(cy)}" rx="{rx}" ry="{ry}"/>{t}'


def nuc(x, y=55):
    return f'<circle class="ph-nuc" cx="{x}" cy="{y}" r="2.4"/>'


def node_v(x, y1=14, y2=96):
    return f'<line class="ph-node" x1="{x}" y1="{y1}" x2="{x}" y2="{y2}"/>'


def node_h(y=55, x1=6, x2=114):
    return f'<line class="ph-node" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>'


def panel(svg_inner, title, line1, line2, label):
    return (f'<div class="gp-cell op-cell"><svg viewBox="0 0 120 110" role="img" aria-label="{label}">{svg_inner}</svg>'
            f'<div class="vs-name">{title}</div><div class="vs-meta">{line1}</div><div class="op-note">{line2}</div></div>')


def sigma_s_bonding():
    inner = (lobe(38, 55, 26, 26, +1, False) + lobe(82, 55, 26, 26, +1, False)
             + '<text class="ph-txt" x="60" y="59" text-anchor="middle">+</text>' + nuc(38) + nuc(82))
    return panel(inner, "σ (bonding)", "1s + 1s, in phase", "density piles up <b>between</b> the nuclei",
                 "Sigma bonding orbital from two s orbitals added in phase")


def sigma_s_anti():
    inner = (lobe(32, 55, 20, 20, +1) + lobe(88, 55, 20, 20, -1) + node_v(60) + nuc(32) + nuc(88)
             + '<text class="op-lab" x="60" y="108" text-anchor="middle">node</text>')
    return panel(inner, "σ* (antibonding)", "1s − 1s, out of phase", "a <b>node</b> sits between the nuclei",
                 "Sigma antibonding orbital from two s orbitals out of phase, with a node between")


def sigma_p_bonding():
    inner = (lobe(17, 55, 12, 10, -1) + lobe(103, 55, 12, 10, -1)
             + lobe(47, 55, 16, 13, +1) + lobe(73, 55, 16, 13, +1) + nuc(32) + nuc(88))
    return panel(inner, "σ (bonding)", "p + p, head-on", "facing lobes match: one big lobe between",
                 "Sigma bonding orbital from two p orbitals overlapping head on")


def sigma_p_anti():
    inner = (lobe(17, 55, 12, 10, -1) + lobe(103, 55, 12, 10, +1)
             + lobe(47, 55, 12, 13, +1) + lobe(73, 55, 12, 13, -1) + node_v(60) + nuc(32) + nuc(88))
    return panel(inner, "σ* (antibonding)", "p − p, head-on", "node cuts across the bond",
                 "Sigma antibonding orbital from two p orbitals head on with a node across the bond")


def pi_bonding():
    inner = (lobe(38, 33, 24, 15, +1) + lobe(82, 33, 24, 15, +1)
             + lobe(38, 77, 24, 15, -1) + lobe(82, 77, 24, 15, -1) + node_h(55) + nuc(38) + nuc(82)
             + '<text class="op-lab" x="112" y="52" text-anchor="end">axis</text>')
    return panel(inner, "π (bonding)", "p + p, side-by-side", "density is <b>off</b> the bond axis",
                 "Pi bonding orbital from two p orbitals side by side, with a nodal plane along the bond axis")


def pi_anti():
    inner = (lobe(38, 33, 24, 15, +1) + lobe(82, 33, 24, 15, -1)
             + lobe(38, 77, 24, 15, -1) + lobe(82, 77, 24, 15, +1) + node_h(55) + node_v(60) + nuc(38) + nuc(82))
    return panel(inner, "π* (antibonding)", "p − p, side-by-side", "two nodal planes (axis + between atoms)",
                 "Pi antibonding orbital with a nodal plane along the axis and another between the atoms")


def orbital_panels():
    # rows = orbital type, columns = bonding | antibonding
    cells = [sigma_s_bonding(), sigma_s_anti(), sigma_p_bonding(), sigma_p_anti(), pi_bonding(), pi_anti()]
    return '<div class="gp-row op-row">' + "".join(cells) + '</div>'


# ---------------------------------------------------------------- MO energy diagrams
def e_up(x, y):
    return (f'<path class="mo-e" d="M{f(x)},{f(y + 1)} V{f(y - 11)} M{f(x - 2.6)},{f(y - 7.4)} L{f(x)},{f(y - 11)} L{f(x + 2.6)},{f(y - 7.4)}"/>')


def e_dn(x, y):
    return (f'<path class="mo-e" d="M{f(x)},{f(y - 11)} V{f(y + 1)} M{f(x - 2.6)},{f(y - 3.4)} L{f(x)},{f(y + 1)} L{f(x + 2.6)},{f(y - 3.4)}"/>')


def level(x1, x2, y, spin, cls="mo-lv"):
    """spin: '', 'u', 'ud'"""
    out = f'<line class="{cls}" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>'
    cx = (x1 + x2) / 2
    if spin == "ud":
        out += e_up(cx - 4, y) + e_dn(cx + 4, y)
    elif spin == "u":
        out += e_up(cx, y)
    return out


def dash(x1, y1, x2, y2):
    return f'<line class="mo-cn" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>'


def lab(x, y, t, anchor="middle", cls="mo-lab"):
    return f'<text class="{cls}" x="{f(x)}" y="{f(y)}" text-anchor="{anchor}">{t}</text>'


def o2_diagram():
    W, H = 520, 350
    yP, yS = 120, 290
    y_ss, y_s, y_pp, y_p, y_ps, y_s2 = 35, 85, 155, 205, 255, 325   # sig*2p, pi*, pi, sig2p, sig*2s, sig2s
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Molecular orbital diagram of O2: twelve valence electrons fill sigma2s, sigma-star 2s, sigma2p, pi2p, and put one electron in each of the two pi-star 2p orbitals. Bond order 2, two unpaired electrons.">']
    # axis
    o.append('<path class="mo-ax" d="M14,350 V30 M9,38 L14,28 L19,38"/>')
    o.append(lab(14, 18, "E"))
    # titles
    o.append(lab(71, 22, "O atom", cls="mo-title"))
    o.append(lab(260, 14, "O₂ molecule", cls="mo-title"))
    o.append(lab(449, 22, "O atom", cls="mo-title"))
    # AOs left
    o.append(level(40, 58, yP, "ud") + level(62, 80, yP, "u") + level(84, 102, yP, "u"))
    o.append(lab(71, yP + 20, "2p", cls="mo-ao"))
    o.append(level(58, 84, yS, "ud") + lab(71, yS + 20, "2s", cls="mo-ao"))
    # AOs right
    o.append(level(418, 436, yP, "ud") + level(440, 458, yP, "u") + level(462, 480, yP, "u"))
    o.append(lab(449, yP + 20, "2p", cls="mo-ao"))
    o.append(level(436, 462, yS, "ud") + lab(449, yS + 20, "2s", cls="mo-ao"))
    # connectors (draw first so levels sit on top)
    conn = []
    # 2s -> sigma2s & sigma*2s
    for ym in (y_s2, y_ps):
        conn.append(dash(84, yS, 232, ym)); conn.append(dash(436, yS, 288, ym))
    # 2p -> sigma2p, pi pair, pi* pair, sigma*2p
    conn.append(dash(102, yP, 232, y_p)); conn.append(dash(418, yP, 288, y_p))
    conn.append(dash(102, yP, 210, y_pp)); conn.append(dash(418, yP, 310, y_pp))
    conn.append(dash(102, yP, 210, 85)); conn.append(dash(418, yP, 310, 85))
    conn.append(dash(102, yP, 232, y_ss)); conn.append(dash(418, yP, 288, y_ss))
    o.append("".join(conn))
    # MO levels
    o.append(level(232, 288, y_s2, "ud"))
    o.append(level(232, 288, y_ps, "ud"))
    o.append(level(232, 288, y_p, "ud"))
    o.append(level(210, 248, y_pp, "ud") + level(272, 310, y_pp, "ud"))
    o.append(f'<rect class="mo-hi" x="204" y="{85 - 20}" width="112" height="26" rx="5"/>')
    o.append(level(210, 248, 85, "u", "mo-lv mo-lv-hi") + level(272, 310, 85, "u", "mo-lv mo-lv-hi"))
    o.append(level(232, 288, y_ss, ""))
    # labels (to the left of each level, with a halo so connectors don't cut them)
    o.append(lab(224, y_s2 + 4, "σ2s", "end"))
    o.append(lab(224, y_ps + 4, "σ*2s", "end"))
    o.append(lab(224, y_p + 4, "σ2p", "end"))
    o.append(lab(202, y_pp + 4, "π2p", "end"))
    o.append(lab(202, 89, "π*2p", "end"))
    o.append(lab(224, y_ss + 4, "σ*2p", "end"))
    o.append(lab(322, 66, "2 unpaired e⁻", "start", "mo-hi-t"))
    o.append("</svg>")
    return "".join(o)


def mo_small(title, aos_l, aos_r, sig, sig_star, bo_txt, note, cls=""):
    W, H = 200, 150
    yAO, yB, yA = 78, 118, 38
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{title}: {note}">']
    o.append(level(22, 62, yAO, aos_l) + level(138, 178, yAO, aos_r))
    o.append(lab(42, yAO + 18, "1s", cls="mo-ao") + lab(158, yAO + 18, "1s", cls="mo-ao"))
    o.append(dash(62, yAO, 80, yB) + dash(138, yAO, 120, yB) + dash(62, yAO, 80, yA) + dash(138, yAO, 120, yA))
    o.append(level(80, 120, yB, sig) + level(80, 120, yA, sig_star))
    o.append(lab(100, yB + 18, "σ1s", cls="mo-lab") + lab(100, yA - 17, "σ*1s", cls="mo-lab"))
    o.append("</svg>")
    return (f'<div class="gp-cell mo-mini {cls}">{"".join(o)}<div class="vs-name">{title}</div>'
            f'<div class="sq-ang">{bo_txt}</div><div class="vs-meta">{note}</div></div>')


def mo_small_row():
    cells = [
        mo_small("H₂", "u", "u", "ud", "", "bond order 1", "stable bond"),
        mo_small("He₂", "ud", "ud", "ud", "ud", "bond order 0", "does not exist", "mo-zero"),
        mo_small("He₂⁺", "ud", "u", "ud", "u", "bond order ½", "weak bond, exists"),
    ]
    return '<div class="gp-row">' + "".join(cells) + '</div>'


# ---------------------------------------------------------------- percent ionic character
def ionic_chart():
    W, H = 560, 300
    L_, R_, T_, B_ = 52, 16, 22, 44
    pw, ph = W - L_ - R_, H - T_ - B_

    def X(d):
        return L_ + pw * d / 3.5

    def Y(p):
        return T_ + ph * (1 - p / 100)

    pts = " ".join(f"{f(X(d / 20))},{f(Y(100 * (1 - math.exp(-(d / 20) ** 2 / 4))))}" for d in range(0, 71))
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Percent ionic character rises smoothly with electronegativity difference, following 1 minus exp of minus delta chi squared over 4. About 6 percent at 0.5, 43 percent at 1.5, 90 percent at 3.">']
    # bands
    o.append(f'<rect class="ic-band" x="{f(X(0.4))}" y="{T_}" width="{f(X(1.8) - X(0.4))}" height="{ph}"/>')
    for p in (0, 25, 50, 75, 100):
        o.append(f'<line class="ic-grid" x1="{L_}" y1="{f(Y(p))}" x2="{W - R_}" y2="{f(Y(p))}"/>')
        o.append(f'<text class="ic-tick" x="{L_ - 8}" y="{f(Y(p) + 4)}" text-anchor="end">{p}%</text>')
    for d in (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5):
        o.append(f'<text class="ic-tick" x="{f(X(d))}" y="{H - 24}" text-anchor="middle">{d:g}</text>')
    o.append(f'<line class="ic-axis" x1="{L_}" y1="{T_ + ph}" x2="{W - R_}" y2="{T_ + ph}"/>')
    o.append(f'<text class="ic-lab" x="{f(L_ + pw / 2)}" y="{H - 6}" text-anchor="middle">electronegativity difference, Δχ</text>')
    o.append(f'<text class="ic-lab" x="14" y="{f(T_ + ph / 2)}" text-anchor="middle" transform="rotate(-90 14 {f(T_ + ph / 2)})">percent ionic character</text>')
    o.append(f'<polyline class="ic-curve" points="{pts}"/>')
    # band labels
    o.append(f'<text class="ic-band-t" x="{f((X(0) + X(0.4)) / 2)}" y="{T_ + 12}" text-anchor="middle">covalent</text>')
    o.append(f'<text class="ic-band-t" x="{f((X(0.4) + X(1.8)) / 2)}" y="{T_ + 12}" text-anchor="middle">polar covalent</text>')
    o.append(f'<text class="ic-band-t" x="{f((X(1.8) + X(3.5)) / 2)}" y="{T_ + 12}" text-anchor="middle">mostly ionic</text>')
    # landmark points on the formula curve
    for d in (0.5, 1.5, 3.0):
        p = 100 * (1 - math.exp(-d * d / 4))
        o.append(f'<circle class="ic-pt" cx="{f(X(d))}" cy="{f(Y(p))}" r="4"/>')
        if p > 85:   # near the top edge: label below the point instead
            o.append(f'<text class="ic-pt-t" x="{f(X(d))}" y="{f(Y(p) + 28)}" text-anchor="middle">Δχ {d:g} → {p:.0f}%</text>')
        else:
            o.append(f'<text class="ic-pt-t" x="{f(X(d) - 9)}" y="{f(Y(p) - 8)}" text-anchor="end">Δχ {d:g} → {p:.0f}%</text>')
    # two real compounds as read (by eye) from the lecture plot: hollow
    for name, d, p in (("HF", 1.78, 41), ("NaCl", 2.23, 79)):
        o.append(f'<circle class="ic-real" cx="{f(X(d))}" cy="{f(Y(p))}" r="4.5"/>')
        o.append(f'<text class="ic-real-t" x="{f(X(d) - 9)}" y="{f(Y(p) + 4)}" text-anchor="end">{name}</text>')
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    import sys
    d = sys.argv[1]
    open(d + "/orbital_panels.html", "w", encoding="utf-8").write(orbital_panels())
    open(d + "/o2_mo.html", "w", encoding="utf-8").write(o2_diagram())
    open(d + "/mo_small.html", "w", encoding="utf-8").write(mo_small_row())
    open(d + "/ionic_chart.html", "w", encoding="utf-8").write(ionic_chart())
    print("ok")
