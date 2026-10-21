# Reproducible simulation supplement

[Download all saved sample arrays](https://github.com/MathisRost/agentic-ai-math/releases/download/astra-paper-2026-10-21/astra_simulation_data.zip). Extract the archive here; it supplies the `data/*.npz` files described below. The binary arrays live in a GitHub release so the Overleaf project stays focused on editable source. `data/array_manifest.json` records every size and SHA256.

The current paper is `../00_main_draft/reciprocal_simplex.tex`; `simulation_section.tex` is the original frozen section before the reader's normalization clarifications.

This supplement concerns frozen approach4 v04 and S1. It contains an actual
ordinary-process experiment and a separate importance-sampled factorial-tuple
experiment. The latter estimates the bin-averaged `g2`, `g3`, `g4` reported in
the paper. It is not labelled ordinary iid process data.

## Reproduce

The run used Python 3.9.6, NumPy 2.0.2 and Matplotlib 3.9.4, already installed
under `/usr/bin/python3` on the task host. The suggested bundled Python was
inspected but lacked Matplotlib; no package installation was performed.
From this directory:

```sh
/usr/bin/python3 code/experiment.py
/usr/bin/python3 code/sample_windows.py
/usr/bin/python3 code/report.py
/usr/bin/python3 code/plot_configurations.py
```

On another machine, use a Python environment with NumPy and Matplotlib.
SciPy is not required. The code saves all outputs relative to its own directory,
so the current shell directory is immaterial. Explicit PCG64 seeds are recorded
in `data/results.json` and `data/ordinary_windows.json`. Changes to the sample
sizes regenerate outputs; running the same seeds does not constitute an
independent replication. For a short smoke run, use `experiment.py --n 4096
--reference-n 16384` and `sample_windows.py --n 10000` in a copy of this folder
to avoid overwriting the frozen publication data. `report.py` checks final-run
statistical sanity at a five-standard-error diagnostic threshold; a tiny
smoke run need not satisfy that arbitrary diagnostic.

## Outputs and data dictionary

* `simulation_section.tex`: self-contained paper section, requiring the
  article class plus amsmath, graphicx and booktabs. Its default `\simulationdir`
  is `coder`; override that command if the supplement is moved.
* `notes/estimator_derivation.md`: complete likelihood and rejection derivation,
  estimand, variance calculation, and full-window simulation algorithm.
* `notes/small_ball_sampler.md`: proof of the implemented exact restricted law.
* `figures/correlations.pdf` and `.png`: all 18 reported bins, with approximate
  pointwise 95% Monte Carlo error bars and the fourth-order radius guard.
* `figures/sampled_configurations_v02.pdf` and `.png`: final padded version
  of the actual saved coordinates, with ordinary, conditional and cluster-mark
  samples labelled distinctly. The original unversioned figure remains frozen.
  `plot_configurations.py` regenerates the layout revision; it changes no data.
* `results_table.tex`: nine representative rows for the paper.
* `data/results.json`, `results.csv`: every bin's actual estimated g value,
  standard error, theory bin average, separate reference integration error,
  ratio and its error, component integrals, exact input parameters and seeds.
* `data/sphere2.npz`, `sphere3.npz`, `sphere4.npz`: each contains `points`
  (rows by vertices by three coordinates, first vertex zero), sampled latent
  `radius`, raw `weight`, `bin_index` (`-1` means outside measured bins) and
  per-row/per-bin `contribution`. All 524,288 rows per order are retained.
* `data/correction_pairs.npz`: proposal `points`, auxiliary third vertex
  `auxiliary`, rejection result `accepted`, bin and contribution. The auxiliary
  vertex is not emitted. All 524,288 proposals, including rejections, are saved.
* `data/correction_triples.npz`: proposal `points`, `accepted`, `bin_index`,
  `pair_contribution` and `triple_contribution`. All three edges' second-order
  contributions are combined per row before variance estimation.
* `data/referenceN_sufficient_statistics.npz`: independent numerical-integration
  statistics, not process data. `raw_sums` columns are sums of volume weights,
  their squares, reciprocal-simplex weights, their squares, and cross products.
  `chunk_sums`, hit counts and n permit auditing aggregate calculations. The
  reference point coordinates can be regenerated exactly from seeds and code.
* `data/ordinary_windows.npz`: 5,000,000 component coin results and count values,
  all nonempty `point_coordinates`, their `point_realisation_id`, and sphere
  envelope candidates. Each candidate row is `[id,R,zx,zy,zz,intersects,mean]`.
  Empty windows are retained. The seven recorded points belong to seven
  distinct realisations; they must not be pooled into one process catalogue.
* `data/ordinary_windows.json`: counts and runtime for the actual ordinary run.
* `data/conditional_sphere_illustration.npz`: separate points given a fixed
  latent sphere and a count at least four; not an ordinary process realisation.
* `data/additional_checks.json`: analytic pair integrals, correction mass
  cancellation, finite errors and comparison diagnostics.
* Model and token records are in `../02_writing_record/`; public export hashes are in `../provenance/paper_release_manifest.json`.

## Study scope

Parameters are `M=1`, `lambda=6e-6`, the explicit accepted K choice, and `L=1`.
Every measured bin has diameter below one and a positive simplex lower edge.
Fourth-order bins also have circumsphere radius at most two. These are
restrictions on the observable only. Sphere proposals for orders two and
three have the full unbounded positive radius range; the underlying process
is never truncated. The five million ordinary restrictions have only seven
singleton points and cannot estimate any of the three requested correlations.

The quantitative experiment uses 524,288 proposals for each of three sphere
orders and each of two correction mark sizes, plus 2,097,152 reference
configurations per order. It uses the known prescribed intensity. It reports
bounded-weight independent-row Monte Carlo errors and separate reference
integration error. It does not estimate an unguarded divergent fourth integral,
provide an earthquake-data comparison, or certify the mathematical theorem.

Pilot and final logs are separate; no pilot data are included in final estimates.
The fourth-order bin edge 0.075 was chosen after the pilot showed that
near-maximal-volume tetrahedra were rare. All other recorded final bins are
reported, without selecting by agreement with theory.
