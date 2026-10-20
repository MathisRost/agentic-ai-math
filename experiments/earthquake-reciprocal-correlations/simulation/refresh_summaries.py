#!/usr/bin/env python3
"""Regenerate summaries and plots from preserved raw contributions."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from reciprocal_study import RHO, dump_json, make_plots, summarise, write_counts, write_csv


HERE = Path(__file__).resolve().parent


def load_npz(path: Path) -> dict:
    with np.load(path) as data:
        return {key: data[key] for key in data.files}


for stage in ("pilot", "production"):
    folder = HERE / stage
    design_path = (folder / "pilot_design_used.json" if stage == "pilot"
                   else HERE / "production_design.json")
    design = json.loads(design_path.read_text())
    normalisers_raw = json.loads((folder / "geometric_normalisers.json").read_text())
    normalisers = {int(key): value for key, value in normalisers_raw.items()}
    arrays = load_npz(folder / "replicate_contributions.npz")
    with np.load(folder / "observations.npz") as observations:
        write_counts(folder / "counts.csv", observations["offsets"])
    krows, rows = summarise(arrays, design, normalisers, RHO, "cluster")
    write_csv(folder / "k_summary.csv", krows)
    write_csv(folder / "correlation_summary.csv", rows)
    poisson_k = poisson_rows = None
    if stage == "production":
        control = design["poisson_control"]
        parrays = load_npz(folder / "poisson_replicate_contributions.npz")
        with np.load(folder / "poisson_observations.npz") as observations:
            write_counts(folder / "poisson_counts.csv", observations["offsets"])
        poisson_k, poisson_rows = summarise(parrays, design, normalisers,
                                            float(control["intensity_per_km3"]), "poisson")
        write_csv(folder / "poisson_k_summary.csv", poisson_k)
        write_csv(folder / "poisson_correlation_summary.csv", poisson_rows)
        dump_json(folder / "excluded_bins.json", {
            "policy": "Correlation summaries require a positive finite estimated geometric volume.",
            "excluded": [{
                "order": 3, "family": "altitude_ratio", "level": "low", "scalar_bin": 3,
                "reason": "Analytically empty: A=d_max*h_min/2 and h_min/d_max<=0.3281 imply A<=0.5*0.3281*M^2=215.10 km^2, below this bin's lower edge 223.24 km^2.",
                "classification": "geometrically empty, not an unobserved positive-volume bin and not evidence of precision"
            }]
        })
    make_plots(folder, krows, rows, poisson_k, poisson_rows)
