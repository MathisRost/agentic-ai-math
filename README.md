# Agentic AI in mathematical research

## Start here

| Material | Read / edit |
|---|---|
| **Presentation** | [Slides PDF](agentic_ai_math_talk.pdf) · [Beamer source](agentic_ai_math_talk.tex) |
| **Astra paper — main draft** | [Paper PDF](experiments/reciprocal-simplex-astra6/00_main_draft/reciprocal_simplex.pdf) · [LaTeX source](experiments/reciprocal-simplex-astra6/00_main_draft/reciprocal_simplex.tex) |
| **Tutorial** | [Research setup guide PDF](02_tutorial/codex_research_setup_guide.pdf) · [Editable source](02_tutorial/codex_research_setup_guide.tex) |
| **Agent architecture** | [Research and writing teams](03_documentation/architecture.md) |
| **Reasoning and documentation** | [Proofs, decisions, reviews and tokens](03_documentation/reasoning.md) |
| **Overleaf** | [Editing and synchronisation](03_documentation/overleaf.md) |

The numbered folders keep the presentation, papers, tutorial and documentation at the beginning of the repository. The Astra folder begins with `00_main_draft/`, followed by the simulation and writing record. Original research archives remain in place.

The main Astra paper proves the diameter-capped reciprocal-simplex statement **S1**, using a fair-coin choice between separated spheres and a finite-cluster correction. The unrestricted exact S0 statement is false. The paper includes a simulation study and distinguishes ordinary process samples from weighted factorial-tuple estimates.

## Experiments and reproducibility

- [Astra experiment](experiments/reciprocal-simplex-astra6/README.md): main paper, full research archive, 16-page experiment report, all submissions/reviews, architecture and accounting.
- [Simulation code and results](experiments/reciprocal-simplex-astra6/01_simulation/README.md), including [all saved data](https://github.com/MathisRost/agentic-ai-math/releases/tag/astra-paper-2026-10-21).
- [Writer/coder/reader record](experiments/reciprocal-simplex-astra6/02_writing_record/README.md).
- [Earlier-model experiment](experiments/reciprocal-simplex-agentic-research/README.md), retained separately.

The repository publishes explicit proofs and concise reasoning/decision summaries, not private chain-of-thought, raw conversations or copied third-party papers. These are informal research case studies, not formal proof certification or a controlled model benchmark.

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
