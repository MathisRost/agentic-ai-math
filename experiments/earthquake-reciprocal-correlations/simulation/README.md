# Reproducibility map

Run commands from this directory. Set temporary cache locations if the host
does not permit writes to the default Python or Matplotlib cache.

## Source and fixed design

- `reciprocal_study.py`: sampler, geometry proposals, estimators, controls,
  summaries and plots.
- `production_design.json`: production design frozen after the precision pilot.
- `refresh_summaries.py`: regenerates CSV summaries and plots from preserved
  raw replicate contributions without rerunning the simulation.
- `check_normaliser_convergence.py`: independent lower-resolution normaliser
  comparison.

## Pilot

`pilot/` contains the actual 10,000-window pilot, not the temporary smoke run.
Its `geometry_pilot.json` and `run_metadata.json` justify the frozen production
design. `pilot_design_used.json` records the provisional bins used for that run.

## Production

- `observations.npz`: all observed coordinates, replicate offsets, parent IDs
  and stream codes. Parent IDs are diagnostics only.
- `counts.csv`: every replicate ID, including empty windows.
- `replicate_contributions.npz`: raw realisation-level K, g and compensated
  sums plus tuple counts.
- `run_metadata.json`: model, seed, sampler counts and parent-allocation counts.
- `geometric_normalisers.json`: independent 1,000,000-proposal normalisers and
  block standard errors.
- `normaliser_convergence.json`: comparison with a fresh 250,000-proposal run.
- `excluded_bins.json`: the analytically empty shape/bin intersection.
- `k_summary.csv`, `correlation_summary.csv`: final cluster-model summaries.
- `poisson_*`: separate Poisson observations, raw contributions, metadata,
  count table, summaries and plots.
- `*.png`, `*.pdf`: K, reciprocal-correlation, compensated, shape-stratified
  and Poisson-control figures.

## Commands

    python3 reciprocal_study.py --stage pilot --replications 10000 \
      --side 1200 --seed 2026101901 --geometry-samples 250000

    python3 reciprocal_study.py --stage production \
      --design production_design.json --replications 200000 --side 1200 \
      --seed 2026101903 --geometry-samples 1000000 \
      --poisson-replications 200

    python3 refresh_summaries.py
    python3 check_normaliser_convergence.py

The production command is deterministic given the recorded software and random
seed, subject to ordinary platform-level floating-point differences.
