# Astra paper: complete saved simulation data

This data-only branch holds all 11 saved NPZ arrays from the 21 October 2026 study. It keeps large binary observations outside the main branch synchronised to Overleaf. The code, full-precision results, derivations, main paper, review and token records are on `main`, under `experiments/reciprocal-simplex-astra6/`.

Download this branch as a ZIP from GitHub. Extract `data/*.npz` into `experiments/reciprocal-simplex-astra6/01_simulation/data/` in the main checkout. `data/array_manifest.json` records all file sizes and SHA256 hashes. NumPy can read the arrays directly; the simulation README on main gives a full data dictionary and exact regeneration commands/seeds.

`astra_overleaf.zip` is a standalone paper-only Overleaf upload snapshot with the canonical manuscript and required figures. Select `reciprocal_simplex.tex` as its main document. The existing shared Overleaf project instead uses `01_papers/astra_main.tex` from main.

These are synthetic process samples, not earthquake observations. Ordinary samples and importance-sampled factorial tuples are labelled separately. Private runtime conversations and third-party source PDFs are excluded.
