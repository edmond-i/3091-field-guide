# 3.091 Field Guide

An unofficial, student-built study guide for **MIT 3.091: Introduction to Solid-State Chemistry (Fall 2026)**.

It is written for people who are starting from close to zero chemistry: every term is defined before it is used, every formula comes with the plain-language idea behind it, and the hard parts are drawn, not just described.

> Not affiliated with or endorsed by MIT or the 3.091 staff. The lectures, slides, and problem sets belong to their authors. This repo contains our own explanations, diagrams, and notes only. **Please never commit course PDFs, slides, exams, or graded work** (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## What is here

| File | What it is |
|---|---|
| [`index.html`](index.html) | The Field Guide: one scrollable page with a table of contents, diagrams, worked examples, practice archetypes, a formula sheet, and an exam-traps list. Light and dark mode, works on phones. |
| [`aid-sheet.html`](aid-sheet.html) / [`aid-sheet.pdf`](aid-sheet.pdf) | A dense one-page recall card sized for the course's allowed 8.5×11" exam aid sheet. |
| [`scripts/build-aid-sheet-pdf.sh`](scripts/build-aid-sheet-pdf.sh) | Rebuilds the PDF from the HTML (headless Chrome) and checks it is exactly one page. |
| [`tools/`](tools) | Small Python scripts that generate the VSEPR and orbital/MO diagrams as inline SVG. Optional. |

## View it

No build step and no dependencies. Open `index.html` in a browser. (Web fonts load from Google Fonts; offline, the page falls back to system fonts.)

## Coverage

| Lectures | Topic | Guide section |
|---|---|---|
| L01-L03 | Atoms, history of atomic models, light, Bohr model | 01 |
| L04-L06 | Quantum numbers, orbitals, electron configurations, PES, periodic trends | 02 |
| L07-L08 | Octet rule, ionic bonding, Born-Haber, lattice energy, crystal structures | 03 |
| L09 | Covalent bonding, Lewis structures | 04 |
| L10-L11 | Covalent compound properties, VSEPR, polarity | 05 |
| L12 | Hybridization, molecular orbitals | 06 |
| all | Cheat codes, practice archetypes, formula sheet, exam traps | end of page |

Recitations 01-06 and practice problem sets 01-03 are folded in as worked examples and "archetypes" (the question types that keep coming back).

## Contributing

Corrections, new lectures, better explanations, extra diagrams, and practice problems are all welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first; the short version is: **explain it so a beginner could follow it, cite the lecture/slide, and label anything that is not from the course as "extra".**

## License

None chosen yet. Until one is added, treat the contents as "all rights reserved by the contributors".
