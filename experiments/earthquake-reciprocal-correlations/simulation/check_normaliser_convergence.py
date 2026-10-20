#!/usr/bin/env python3
"""Repeat the production geometric normalisers at lower resolution.

This check is independent of the observed point-process realisations.  It
compares the 1,000,000-proposal production estimates with a fresh 250,000-
proposal run using the same frozen bins and shape strata.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from reciprocal_study import compute_normalisers, dump_json


HERE = Path(__file__).resolve().parent
design = json.loads((HERE / "production_design.json").read_text())
production = json.loads((HERE / "production" / "geometric_normalisers.json").read_text())

fresh = {
    3: compute_normalisers(3, design, 250_000, 2026101953),
    4: compute_normalisers(4, design, 250_000, 2026101954),
}

comparisons = []
for order in (3, 4):
    reference = {(r["family"], r["level"], r["scalar_bin"]): r
                 for r in production[str(order)]}
    for row in fresh[order]:
        key = (row["family"], row["level"], row["scalar_bin"])
        ref = reference[key]
        if ref["volume"] <= 0 or row["volume"] <= 0:
            continue
        volume_rel = (row["volume"] - ref["volume"]) / ref["volume"]
        recip_rel = ((row["reciprocal_average"] - ref["reciprocal_average"])
                     / ref["reciprocal_average"])
        joint_se = math.sqrt(ref["volume_se"]**2 + row["volume_se"]**2)
        comparisons.append({
            "order": order, "family": key[0], "level": key[1], "scalar_bin": key[2],
            "production_volume": ref["volume"], "fresh_volume": row["volume"],
            "volume_relative_difference": volume_rel,
            "volume_difference_in_joint_se": ((row["volume"] - ref["volume"]) / joint_se
                                               if joint_se > 0 else None),
            "reciprocal_average_relative_difference": recip_rel,
        })

summary = {
    "production_proposals_per_order": 1_000_000,
    "fresh_proposals_per_order": 250_000,
    "fresh_seeds": {"g3": 2026101953, "g4": 2026101954},
    "positive_volume_bins_compared": len(comparisons),
    "max_absolute_volume_relative_difference": max(abs(x["volume_relative_difference"]) for x in comparisons),
    "max_absolute_reciprocal_average_relative_difference": max(abs(x["reciprocal_average_relative_difference"]) for x in comparisons),
    "max_absolute_volume_difference_in_joint_se": max(abs(x["volume_difference_in_joint_se"]) for x in comparisons
                                                       if x["volume_difference_in_joint_se"] is not None),
    "comparisons": comparisons,
}
dump_json(HERE / "production" / "normaliser_convergence.json", summary)
