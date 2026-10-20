# Action log

Date: 19 October 2026. Role: simulation specialist. Model configuration:
gpt-5.6-sol with xhigh reasoning. No token counts are recorded.

## Decisions

- Used the expanded witness (0.49, 0.49, 0.98, 36.21, 50.01 km; a2=1e-13)
  for every order and every cluster-model run.
- Used known rho for the primary study. Did not perform an estimated-intensity
  sensitivity analysis.
- Chose 1,200 km cubes after checking that the largest estimated displacement
  (100 km for K) retains positive, moderate translation overlap and that the
  expected point count remains computationally small.
- Treated the initial 200-replicate run as a temporary smoke test only. It was
  overwritten by the 10,000-replicate precision/computational pilot and has no
  inferential role.
- Froze `production_design.json` after the pilot: 200,000 realisations, fixed
  scalar bins, fixed shape/orientation splits, and a separate high-intensity
  Poisson estimator control.
- Retained the predicted g4 underpower instead of changing parameters, dropping
  empty windows, using same-parent-only tuples or changing estimands.
- Excluded one analytically empty triangle shape/bin intersection from summaries;
  recorded the reason in `production/excluded_bins.json`.

## Commands and checks

    PYTHONPYCACHEPREFIX=/tmp/reciprocal_pycache MPLCONFIGDIR=/tmp/reciprocal_mpl \
      python3 reciprocal_study.py --stage pilot --replications 10000 \
      --side 1200 --seed 2026101901 --geometry-samples 250000

    PYTHONPYCACHEPREFIX=/tmp/reciprocal_pycache MPLCONFIGDIR=/tmp/reciprocal_mpl \
      python3 reciprocal_study.py --stage production \
      --design production_design.json --replications 200000 --side 1200 \
      --seed 2026101903 --geometry-samples 1000000 \
      --poisson-replications 200

    PYTHONPYCACHEPREFIX=/tmp/reciprocal_pycache MPLCONFIGDIR=/tmp/reciprocal_mpl \
      python3 refresh_summaries.py

    PYTHONPYCACHEPREFIX=/tmp/reciprocal_pycache \
      python3 check_normaliser_convergence.py

Checks completed: source compilation, deterministic geometry and ordered-factor
tests, K endpoint continuity, exact known-count mean check, Poisson K/g2/g3/g4
controls, independent geometric-normaliser resolution check, positive-volume
summary guard, inspection of sparse-bin statuses, and a final raw-offset/count
table consistency audit. That audit found and repaired a filename collision in
which the Poisson save step overwrote only the cluster `counts.csv`; both count
tables were regenerated from their intact raw observation offsets. No estimator
or numerical result was affected.

## Recorded runtime

- 10,000-window pilot: sampler 2.65 s; estimator 0.37 s. The encompassing tool
  call took about 5.3 s including normalisers and plots.
- 200,000-window production: sampler 56.16 s; cluster estimator 7.74 s;
  Poisson estimator 4.26 s. An exact encompassing wall time was not captured.
- Summary refresh plus the independent 250,000-proposal normaliser check took
  about 4.4 s in the encompassing tool call.

Software: Python 3.9.6, NumPy 2.0.2, SciPy 1.13.1 and Matplotlib 3.9.4. SciPy
supplied the large-count spatial index and Matplotlib generated plots.

## Limitations

- Every interval is pointwise; there is no simultaneous band.
- Rare-event normal intervals are rough at g4, whose bins have only 23--40
  unordered tuples. All pooled g4 bins are marked underpowered.
- A zero empirical variance from no observed pair/tuple is labelled no
  information, never precision.
- Higher-order volumes and integrated targets use finite independent geometric
  Monte Carlo; its uncertainty is reported separately.
- Floating-point geometry is not interval-certified.
- No earthquake catalogue comparison or historical observation mask was used.
