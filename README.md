# Agentic AI in mathematical research

A presentation about using LLMs and agentic systems in mathematical research,
including a case study in building an AI research team to write a paper.

**[Read the presentation (PDF)](agentic_ai_math_talk.pdf)**

The talk covers research examples, agent workflows, a point-process case study,
and personal reflections on mathematical understanding and PhD education.
Claims about model capabilities and research releases are dated and attributed
in the slides and source notes.

## Contents

- `agentic_ai_math_talk.pdf` — compiled presentation.
- `agentic_ai_math_talk.tex` — editable Beamer source, including speaker notes.
- `assets/` — diagrams, editable draw.io files, exports and attributed logos.
- `scripts/` — diagram builders, local draw.io exporter and QR-code builder.
- `sources/` — source records and provenance for the talk.
- `style/sketch/` — diagram style references and Kalam fonts with their licence.
- `experiments/` — reserved for experiments to be added later.

## Published research experiment

The [`experiments/reciprocal-simplex-agentic-research/`](experiments/reciprocal-simplex-agentic-research/README.md)
folder contains the complete public-facing architecture and audit bundle for a
multi-agent mathematical research run: reusable agent files, role instructions,
workflow configuration, the exact problem and approach assignments, frozen
proof submissions and reviews, a literature dossier, the final review report,
and a PDF of the saved reasoning summaries with per-agent runtime and token
accounting.

The bundle publishes structured reasoning summaries and decision records, not
raw private chain-of-thought or copied third-party source PDFs.

Other research-run logs and manuscript sources are not included. Some speaker
notes refer to additional local materials.

## Build the slides

Install a TeX distribution with Beamer, PGFPlots and `latexmk`, then run from
the repository root:

```sh
mkdir -p tmp/build
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=tmp/build agentic_ai_math_talk.tex
cp tmp/build/agentic_ai_math_talk.pdf agentic_ai_math_talk.pdf
```

The committed PDF graphics are sufficient to compile the talk. Diagram
regeneration is optional: install Python 3, draw.io Desktop and the supplied
Kalam fonts, run the relevant builder in `scripts/`, then export its `.drawio`
file with:

```sh
python3 scripts/export_drawio.py assets/personal_research_paths.drawio \
  --formats pdf svg png
```

Set `DRAWIO_BIN` if the exporter cannot find draw.io Desktop.
Regenerating `assets/repository_qr.pdf` requires the Python package `reportlab`
and `python3 scripts/build_repository_qr.py`.

## Attribution

References are linked in the slides; further provenance is recorded in
`sources/` and `assets/icons/sources.json`. Third-party logos belong to their
respective owners. Kalam is distributed under its included SIL Open Font
License. No additional licence is assigned to the presentation in this release.
