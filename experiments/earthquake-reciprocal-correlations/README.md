# Exact reciprocal simplex correlations

This directory contains the manuscript and numerical study for the
earthquake-conjecture case study discussed in the presentation.

The analytical result constructs a simple stationary isotropic point process
whose full factorial correlations satisfy reciprocal distance, triangle-area
and tetrahedron-volume laws on explicit bounded nondegenerate domains. The
numerical study checks the finite-window sampler and translation-corrected
estimators against that already-proved model; it is not a substitute for the
proof and is not a comparison with a historical earthquake catalogue.

## Contents

- [`manuscript/main.pdf`](manuscript/main.pdf) — compiled final manuscript.
- [`manuscript/main.tex`](manuscript/main.tex) and `manuscript/sections/` —
  editable LaTeX source.
- [`simulation/reciprocal_study.py`](simulation/reciprocal_study.py) — pilot
  and production implementation.
- [`simulation/README.md`](simulation/README.md) — reproduction commands and
  output map.
- [`simulation/REPORT.md`](simulation/REPORT.md) — numerical design, checks,
  results and limitations.
- [`simulation/pilot/`](simulation/pilot/) and
  [`simulation/production/`](simulation/production/) — saved raw contributions,
  summaries, diagnostics and figures.
- [`review/AGENT_DECISION_SUMMARY.md`](review/AGENT_DECISION_SUMMARY.md) —
  auditable summary of agent inputs, decisions, evidence and conclusions. It
  does not reproduce private chain-of-thought.

## Main numerical outcome

The production study retained 200,000 independent realisations, including
47,055 empty windows. The pooled pair and triangle estimates reproduce their
targets at useful precision. Only 126 admissible tetrahedra were observed, so
the fourth-order estimates are explicitly classified as underpowered and
inconclusive. No matched earthquake-catalogue comparison has been performed.

## Build the manuscript

From this directory:

```sh
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

See `simulation/README.md` for the Python environment and commands used for the
pilot, production run and independent normaliser check.
