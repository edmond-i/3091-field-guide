# Contributing

Thanks for helping! The goal: a guide that someone with **very little chemistry background** can read once and actually understand, and that they can trust.

## What to contribute

- **Corrections.** Wrong number, wrong sign, unclear sentence, broken diagram. Please cite the lecture/slide (e.g. "L11 slide 12") or the source in the PR.
- **New lectures.** When a new lecture drops, add a unit (see "Adding a unit").
- **Better explanations and analogies.** If something confused you, it confused others; rewrite it in plain words.
- **Diagrams.** Inline SVG, theme-aware (see below).
- **Practice problems** with fully worked solutions, tagged by type (an "archetype").

## Ground rules

1. **Beginner first.** Define every term the first time it appears. Give the plain-language idea before the formula or notation. Always give units.
2. **Lecture vs. extra.** If a statement is not on the slides, label it `extra` (see the `.pill` examples in `index.html`), e.g. standard chemistry added to make a slide understandable. Do not present your own additions as lecture content.
3. **Flag slide typos** instead of silently "fixing" them (see the "L12 slide typos" note).
4. **No course materials.** Do not commit lecture slides, notes, exam questions, or graded work (psets/exams). Worked examples should be your own explanation of a standard problem type.
5. **Be careful with numbers.** Double-check constants and worked-example arithmetic; say how you got a value.
6. **No new dependencies.** The guide is plain HTML/CSS/inline SVG, with one tiny inline script for the mobile menu.

## How the page is built

Everything lives in `index.html`:

- `<style>` at the top: colour tokens in `:root` (light), `@media (prefers-color-scheme: dark)` and `:root[data-theme="dark"]`. **Use the tokens (`var(--ink)`, `var(--unit-covalent)`, ...), never hard-coded colours**, so dark mode keeps working. If you add a token, define it in all three places.
- Each unit is a `<section class="unit" id="unitN">` with a `.unit-head`, topics as `<h3 class="topic" id="...">`.
- Callouts: `.box.def` (definition), `.formula-box`, `.box.example` (worked example), `.box.trap` (common mistake), `.box.analogy`, `.box.cheat` (cheat code).
- Wide tables go in `<div class="tscroll">`; wide diagrams go in a `figure.fig-frame` or `.vs-wrap` so they scroll sideways on phones instead of shrinking.
- Every new topic needs a table-of-contents entry (the `#toc-desktop` list near the top; the mobile menu copies it automatically).

### Adding a unit (new lecture)

1. Add a `section.unit` with the next number and its own accent colour token (copy an existing `--unit-*` pair into the three token blocks).
2. Add it to the table of contents.
3. Add the new question types to **Practice archetypes**, new formulas to the **Formula cheat-sheet**, and new gotchas to **Exam traps**.
4. Add a one-liner to **Cheat codes** if the topic has a memory hook.
5. Update the coverage table in `README.md`.

### Diagrams

- Draw as inline `<svg>` with a `viewBox`, a `role="img"`, and an `aria-label` that states the point of the figure; put the explanation in the `<figcaption>`.
- Theme with CSS variables or `currentColor`. Text sizes below ~10px are unreadable on phones, so size the `viewBox` for the content.
- VSEPR convention used here: plain line = bond in the page, solid wedge = toward you, hashed wedge = away, teal lobe with two dots = lone pair. Orbital pictures: blue = positive phase, red = negative phase (phase, **not** charge).
- `tools/gen_vsepr.py` and `tools/gen_orbitals.py` generate the shape and orbital/MO figures. Run `python3 tools/gen_vsepr.py out/` then paste the produced `.html` snippets into `index.html`.

## Before you open a PR

- [ ] Open `index.html` in a browser: light mode **and** dark mode look right.
- [ ] Narrow the window to phone width: no sideways scrolling of the whole page.
- [ ] Everything not from the lecture is labelled `extra`.
- [ ] New terms are defined; units are given; numbers re-checked.
- [ ] Links and `#anchors` resolve; every new section is in the table of contents.
- [ ] If you touched `aid-sheet.html`: run `scripts/build-aid-sheet-pdf.sh` and confirm it says **1 page** (the aid sheet must stay one page; its columns are floats on purpose, because CSS grid/flex let text run off the printed page).

## Reviewing

Reviewers: prefer comments like "slide 14 says X, this says Y" over style opinions. If two people disagree about the chemistry, link the lecture slide or a textbook section and settle it there.
