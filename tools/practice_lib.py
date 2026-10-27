"""Tiny DSL + renderer for the practice questions (see practice_bank_*.py).

Every question is an HTML <article class="pq"> that tools/practice.js enhances.
Numeric answers are computed in Python inside the bank files so the worked solution text
and the auto-checker can never disagree.
"""
import html
import random

TOPICS = {}   # key -> dict(title=, unit=, recipe=, quiz=)
BANK = []     # ordered list of question dicts


def topic(key, title, unit, quiz, recipe):
    TOPICS[key] = dict(title=title, unit=unit, quiz=quiz, recipe=recipe)


def _add(q):
    ids = [b["id"] for b in BANK]
    assert q["id"] not in ids, "duplicate id " + q["id"]
    assert q["topic"] in TOPICS, "unknown topic " + q["topic"]
    BANK.append(q)


def num(id, topic, diff, tag, q, answer, unit, sol, hint="", tol=0.02, atol=0.0, alt=(), text=None):
    _add(dict(kind="num", id=id, topic=topic, diff=diff, tag=tag, q=q, answer=answer, unit=unit,
              sol=sol, hint=hint, tol=tol, atol=atol, alt=list(alt), text=text))


def mc(id, topic, diff, tag, q, choices, sol, hint="", whys=None):
    """choices[0] is the correct one; the renderer shuffles deterministically."""
    _add(dict(kind="mc", id=id, topic=topic, diff=diff, tag=tag, q=q, choices=choices, sol=sol, hint=hint, whys=whys or {}))


def selfq(id, topic, diff, tag, q, sol, hint=""):
    _add(dict(kind="self", id=id, topic=topic, diff=diff, tag=tag, q=q, sol=sol, hint=hint))


def fmt(x, sig=3):
    """Format a float for answer text without trailing noise."""
    s = ("%." + str(sig) + "g") % x
    if "e" in s:
        m, e = s.split("e")
        return "%s&times;10<sup>%d</sup>" % (m, int(e))
    return s


def _label(q):
    return "%s &middot; %s" % (TOPICS[q["topic"]]["title"].split(" &middot; ")[0], q["id"].split("-")[-1])


def render_question(q, label_override=None):
    a = html.escape  # only for attribute values
    short = q["id"].upper()
    stars = "&#9679;" * q["diff"] + "&#9675;" * (3 - q["diff"])
    attrs = 'id="q-%s" data-id="%s" data-type="%s" data-topic="%s" data-topic-title="%s" data-diff="%d" data-label="%s"' % (
        q["id"], q["id"], q["kind"], q["topic"], a(TOPICS[q["topic"]]["title"], quote=True), q["diff"],
        a(label_override or ("%s" % short), quote=True))
    if q["kind"] == "num":
        attrs += ' data-answer="%r" data-tol="%r" data-unit="%s"' % (q["answer"], q["tol"], a(q["unit"], quote=True))
        if q["atol"]:
            attrs += ' data-atol="%r"' % q["atol"]
        if q["alt"]:
            attrs += ' data-alt="%s"' % ";".join(repr(x) for x in q["alt"])
        if q["text"]:
            attrs += ' data-text="%s"' % a(q["text"], quote=True)
    out = ['<article class="pq" %s>' % attrs]
    out.append('<div class="pq-head"><span class="pq-id">%s</span><span class="pq-diff" title="difficulty">%s</span><span class="pq-tag">%s</span><span class="pq-state"></span></div>' % (short, stars, q["tag"]))
    out.append('<div class="pq-q">%s</div>' % q["q"])
    if q["kind"] == "mc":
        idx = list(range(len(q["choices"])))
        random.Random(q["id"]).shuffle(idx)
        out.append('<div class="pq-choices" role="radiogroup">')
        for i in idx:
            c = q["choices"][i]
            why = q["whys"].get(i, "")
            out.append('<label class="pq-choice"><input type="radio" name="r-%s"%s%s><span>%s</span></label>' % (
                q["id"], " data-correct" if i == 0 else "", (' data-why="%s"' % a(why, quote=True)) if why else "", c))
        out.append('</div><div class="pq-ans"><button class="pq-btn pq-check" type="button">Check</button></div>')
    elif q["kind"] == "num":
        out.append('<div class="pq-ans"><input class="pq-input" type="text" inputmode="decimal" autocomplete="off" aria-label="Your numeric answer" placeholder="your answer"><span class="pq-unit">%s</span><button class="pq-btn pq-check" type="button">Check</button></div>' % q["unit"])
    out.append('<div class="pq-fb" hidden aria-live="polite"></div>')
    if q["hint"]:
        out.append('<details class="pq-hint"><summary>Hint</summary><div>%s</div></details>' % q["hint"])
    out.append('<details class="pq-sol"><summary>Worked solution</summary><div>%s</div></details>' % q["sol"])
    if q["kind"] == "self":
        out.append('<div class="pq-self" hidden><span>After comparing with the solution:</span><button type="button" data-r="c">I got it</button><button type="button" data-r="m">I missed something</button></div>')
    out.append('</article>')
    return "".join(out)


def render_block(title, lead, qs):
    parts = ['<div class="pq-block"><div class="pq-bhead"><h4>%s</h4><span class="pq-sum"></span></div><div class="pq-bar"><i></i></div>' % title]
    if lead:
        parts.append('<p class="pq-lead">%s</p>' % lead)
    parts.extend(render_question(q) for q in qs)
    parts.append('</div>')
    return "".join(parts)


def by_topic(key):
    return [q for q in BANK if q["topic"] == key]
