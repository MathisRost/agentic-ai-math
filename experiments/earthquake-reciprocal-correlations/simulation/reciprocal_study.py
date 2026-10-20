#!/usr/bin/env python3
"""Finite-window implementation study for the expanded reciprocal witness.

The observed-process estimators never use parent labels.  Labels are saved only
for sampler and parent-allocation diagnostics.  Empty realisations are retained
through the offsets array and contribute zero to every replicate-level sum.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import importlib.metadata
import json
import math
import platform
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import scipy
from scipy.spatial import cKDTree


ROOT = Path(__file__).resolve().parent
DELTA = HEIGHT3 = 0.49
HEIGHT4 = 0.98
M = 36.21
P = 50.01
A2 = 1.0e-13
I = 2.0 * math.pi * (P**2 - DELTA**2)
L0 = 4.0 * math.pi / 3.0 * (P**3 - DELTA**3)
B = 2.0 * math.pi**2 * M**2
C = 6.0 * math.pi * (M**2 * math.log(M / HEIGHT4) - (M**2 - HEIGHT4**2) / 2.0)
A3 = A2 / (4.0 * B)
A4 = A2 / (16.0 * B * C)
RHO = A2 * I
J = 2.0 * math.pi * M**2 * B
CK = {2: A2 / RHO**2, 3: A3 / RHO**3, 4: A4 / RHO**4}
STREAMS = ("pair", "triple", "quad", "singleton_direct", "singleton_triple", "singleton_quad")
STREAM_CODE = {name: i for i, name in enumerate(STREAMS)}
STREAM_CARDINALITY = {"pair": 2, "triple": 3, "quad": 4,
                      "singleton_direct": 1, "singleton_triple": 1,
                      "singleton_quad": 1}
STREAM_RATES = {
    "pair": A2 * I / 2.0,
    "triple": A3 * J / 6.0,
    "quad": A4 * J * C / 24.0,
    "singleton_direct": RHO**2 * L0,
    "singleton_triple": A3 * J / 2.0,
    "singleton_quad": A4 * J * C / 3.0,
}


def dump_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    def convert(x: object) -> object:
        if isinstance(x, np.generic):
            return x.item()
        raise TypeError(f"cannot serialise {type(x).__name__}")
    path.write_text(json.dumps(value, indent=2, sort_keys=True, default=convert) + "\n")


def unit_direction(rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=3)
    return x / np.linalg.norm(x)


def frame(v: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    e = v / np.linalg.norm(v)
    axis = np.eye(3)[np.argmin(np.abs(e))]
    f = np.cross(e, axis)
    f /= np.linalg.norm(f)
    return e, f, np.cross(e, f)


def triangle_geometry(x: np.ndarray) -> tuple[float, float, float, float]:
    area = float(np.linalg.norm(np.cross(x[1] - x[0], x[2] - x[0])) / 2.0)
    edges = [float(np.linalg.norm(x[i] - x[j])) for i in range(3) for j in range(i)]
    diam = max(edges)
    hmin = 2.0 * area / diam if diam else 0.0
    return area, diam, hmin, min(edges) / diam if diam else 0.0


def tetra_geometry(x: np.ndarray) -> tuple[float, float, float, float]:
    vol = float(abs(np.linalg.det((x[1:] - x[0]).T)) / 6.0)
    face_areas = [triangle_geometry(np.delete(x, i, axis=0))[0] for i in range(4)]
    edges = [float(np.linalg.norm(x[i] - x[j])) for i in range(4) for j in range(i)]
    diam = max(edges)
    hmin = 3.0 * vol / max(face_areas) if max(face_areas) else 0.0
    return vol, diam, hmin, min(edges) / diam if diam else 0.0


def r2(x: np.ndarray) -> float:
    d = float(np.linalg.norm(x[1] - x[0]))
    return 1.0 - RHO**2 * d / A2 if DELTA <= d <= P else 0.0


def r3(x: np.ndarray) -> float:
    area, diam, hmin, _ = triangle_geometry(x)
    if area == 0.0 or diam > M or hmin < HEIGHT3:
        return 0.0
    pair_q = 0.0
    for i in range(3):
        for j in range(i):
            d = float(np.linalg.norm(x[i] - x[j]))
            if DELTA <= d <= P:
                pair_q += A2 / d - RHO**2
    return 1.0 - area * (RHO**3 + RHO * pair_q) / A3


def r4(x: np.ndarray) -> float:
    vol, diam, hmin, _ = tetra_geometry(x)
    if vol == 0.0 or diam > M or hmin < HEIGHT4:
        return 0.0
    pair_q: dict[tuple[int, int], float] = {}
    for i in range(4):
        for j in range(i + 1, 4):
            d = float(np.linalg.norm(x[i] - x[j]))
            pair_q[i, j] = A2 / d - RHO**2 if DELTA <= d <= P else 0.0
    pair_pair = (pair_q[0, 1] * pair_q[2, 3] + pair_q[0, 2] * pair_q[1, 3]
                 + pair_q[0, 3] * pair_q[1, 2])
    triple_sum = 0.0
    for i in range(4):
        face = np.delete(x, i, axis=0)
        area = triangle_geometry(face)[0]
        rr = r3(face)
        if rr > 0.0 and area > 0.0:
            triple_sum += A3 * rr / area
    return 1.0 - vol * (RHO**4 + RHO**2 * sum(pair_q.values()) + pair_pair
                        + RHO * triple_sum) / A4


def propose3(x: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    e, f, g = frame(x[1] - x[0])
    rad = M * math.sqrt(rng.random())
    angle = math.pi * rng.random()
    azimuth = 2.0 * math.pi * rng.random()
    s, rr = rad * math.cos(angle), rad * math.sin(angle)
    return x[0] + s * e + rr * (math.cos(azimuth) * f + math.sin(azimuth) * g)


def propose4(x: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    e = (x[1] - x[0]) / np.linalg.norm(x[1] - x[0])
    normal = np.cross(x[1] - x[0], x[2] - x[0])
    normal /= np.linalg.norm(normal)
    f = np.cross(normal, e)
    while True:
        u = HEIGHT4 * math.exp(rng.random() * math.log(M / HEIGHT4))
        if rng.random() < 1.0 - u * u / (M * M):
            break
    u *= 1.0 if rng.random() < 0.5 else -1.0
    rad = math.sqrt((M * M - u * u) * rng.random())
    angle = 2.0 * math.pi * rng.random()
    return x[0] + u * normal + rad * (math.cos(angle) * e + math.sin(angle) * f)


def draw_mark(kind: str, rng: np.random.Generator) -> tuple[np.ndarray | None, bool, float]:
    if kind == "singleton_direct":
        return np.zeros((1, 3)), True, 1.0
    if kind == "pair":
        rad = math.sqrt(DELTA**2 + (P**2 - DELTA**2) * rng.random())
        x = np.array([np.zeros(3), rad * unit_direction(rng)])
        tri = np.vstack([x, propose3(x, rng)])
        rr3 = r3(tri)
        weight = r2(x)
        if rr3 > 0.0:
            weight += -rr3 / 4.0 + r4(np.vstack([tri, propose4(tri, rng)])) / 32.0
    else:
        x2 = np.array([np.zeros(3), M * math.sqrt(rng.random()) * unit_direction(rng)])
        tri = np.vstack([x2, propose3(x2, rng)])
        if kind in ("triple", "singleton_triple"):
            rr3 = r3(tri)
            if rr3 <= 0.0:
                return None, False, 0.0
            weight = rr3 - r4(np.vstack([tri, propose4(tri, rng)])) / 4.0
            x = tri
        elif kind in ("quad", "singleton_quad"):
            x = np.vstack([tri, propose4(tri, rng)])
            weight = r4(x)
        else:
            raise ValueError(kind)
    if weight < -2e-12 or weight > 1.0 + 2e-12:
        raise ArithmeticError(f"invalid thinning probability {weight} in {kind}")
    weight = min(1.0, max(0.0, weight))
    if rng.random() >= weight:
        return None, False, weight
    return (np.zeros((1, 3)) if kind.startswith("singleton_") else x), True, weight


@dataclass
class Observations:
    replications: int
    side: float
    offsets: np.ndarray
    xyz: np.ndarray
    parent: np.ndarray
    stream: np.ndarray


def simulate_cluster(replications: int, side: float, seed: int) -> tuple[Observations, dict]:
    rng = np.random.default_rng(seed)
    box_side = side + 2.0 * P
    reps: list[int] = []
    xyz: list[np.ndarray] = []
    parents: list[int] = []
    streams: list[int] = []
    proposed = {name: 0 for name in STREAMS}
    accepted = {name: 0 for name in STREAMS}
    visible = {name: 0 for name in STREAMS}
    weight_sum = {name: 0.0 for name in STREAMS}
    parent_id = 0
    started = time.perf_counter()
    for kind in STREAMS:
        number = int(rng.poisson(replications * STREAM_RATES[kind] * box_side**3))
        proposed[kind] = number
        for _ in range(number):
            rep = int(rng.integers(replications))
            centre = rng.uniform(-P, side + P, size=3)
            mark, ok, weight = draw_mark(kind, rng)
            weight_sum[kind] += weight
            if not ok:
                parent_id += 1
                continue
            accepted[kind] += 1
            assert mark is not None and mark.shape == (STREAM_CARDINALITY[kind], 3)
            points = centre + mark
            inside = np.all((points >= 0.0) & (points <= side), axis=1)
            for point in points[inside]:
                reps.append(rep)
                xyz.append(point)
                parents.append(parent_id)
                streams.append(STREAM_CODE[kind])
                visible[kind] += 1
            parent_id += 1
    if reps:
        order = np.argsort(np.asarray(reps), kind="stable")
        rep_array = np.asarray(reps, dtype=np.int64)[order]
        xyz_array = np.asarray(xyz, dtype=np.float64)[order]
        parent_array = np.asarray(parents, dtype=np.int64)[order]
        stream_array = np.asarray(streams, dtype=np.int8)[order]
        counts = np.bincount(rep_array, minlength=replications)
    else:
        xyz_array = np.empty((0, 3), dtype=float)
        parent_array = np.empty(0, dtype=np.int64)
        stream_array = np.empty(0, dtype=np.int8)
        counts = np.zeros(replications, dtype=np.int64)
    offsets = np.r_[0, np.cumsum(counts)].astype(np.int64)
    diagnostics = {
        "runtime_seconds": time.perf_counter() - started,
        "candidate_box_side_km": box_side,
        "proposed_candidates": proposed,
        "accepted_parent_marks": accepted,
        "visible_points_by_stream": visible,
        "mean_thinning_weight_over_candidates": {
            k: (weight_sum[k] / proposed[k] if proposed[k] else None) for k in STREAMS
        },
        "observed_points": int(len(xyz_array)),
        "empty_realisations": int(np.count_nonzero(counts == 0)),
        "mean_count": float(counts.mean()),
        "count_variance": float(counts.var(ddof=1)) if replications > 1 else None,
        "max_count": int(counts.max(initial=0)),
    }
    return Observations(replications, side, offsets, xyz_array, parent_array, stream_array), diagnostics


def save_observations(path: Path, obs: Observations) -> None:
    np.savez_compressed(path, replications=np.array([obs.replications]), side=np.array([obs.side]),
                        offsets=obs.offsets, xyz=obs.xyz, parent=obs.parent, stream=obs.stream,
                        stream_names=np.asarray(STREAMS))
    counts_name = "counts.csv" if path.stem == "observations" else path.stem.replace("observations", "counts") + ".csv"
    write_counts(path.with_name(counts_name), obs.offsets)


def write_counts(path: Path, offsets: np.ndarray) -> None:
    with path.open("w", newline="") as handle:
        out = csv.writer(handle)
        out.writerow(["replicate", "count"])
        out.writerows((i, int(offsets[i + 1] - offsets[i])) for i in range(len(offsets) - 1))


def poisson_observations(replications: int, side: float, intensity: float,
                         seed: int) -> Observations:
    rng = np.random.default_rng(seed)
    counts = rng.poisson(intensity * side**3, size=replications)
    offsets = np.r_[0, np.cumsum(counts)].astype(np.int64)
    xyz = rng.uniform(0.0, side, size=(int(offsets[-1]), 3))
    # Unique labels guarantee that allocation diagnostics would call every point a distinct parent.
    parent = np.arange(len(xyz), dtype=np.int64)
    stream = np.full(len(xyz), -1, dtype=np.int8)
    return Observations(replications, side, offsets, xyz, parent, stream)


def geometry_proposals(order: int, n: int, rng: np.random.Generator) -> dict[str, np.ndarray]:
    d = M * np.sqrt(rng.random(n))
    rad = M * np.sqrt(rng.random(n))
    ang = math.pi * rng.random(n)
    s, rr = rad * np.cos(ang), rad * np.sin(ang)
    az = 2.0 * math.pi * rng.random(n)
    x2 = np.column_stack((d, np.zeros(n), np.zeros(n)))
    x3 = np.column_stack((s, rr * np.cos(az), rr * np.sin(az)))
    e23 = np.linalg.norm(x3 - x2, axis=1)
    area = d * rr / 2.0
    diam3 = np.maximum.reduce([d, rad, e23])
    h3 = np.divide(2.0 * area, diam3, out=np.zeros_like(area), where=diam3 > 0)
    edge_ratio3 = np.minimum.reduce([d, rad, e23]) / diam3
    support3 = (diam3 <= M) & (h3 >= HEIGHT3)
    if order == 3:
        return {"G": area, "diameter": diam3, "altitude_ratio": h3 / diam3,
                "edge_ratio": edge_ratio3,
                # An independent uniform |cos(theta)| applies the global isotropic rotation.
                "orientation": rng.random(n), "support": support3}
    # The proposal draws height from the exact A/(C V) conditional law.
    u = np.empty(n)
    waiting = np.arange(n)
    while len(waiting):
        cand = HEIGHT4 * np.exp(rng.random(len(waiting)) * math.log(M / HEIGHT4))
        keep = rng.random(len(waiting)) < 1.0 - cand**2 / M**2
        u[waiting[keep]] = cand[keep]
        waiting = waiting[~keep]
    u *= np.where(rng.random(n) < 0.5, -1.0, 1.0)
    plane_rad = np.sqrt((M**2 - u**2) * rng.random(n))
    plane_ang = 2.0 * math.pi * rng.random(n)
    # For the canonical frame, normal=(0,-sin az,cos az) and f=normal x e1.
    normal = np.column_stack((np.zeros(n), -np.sin(az), np.cos(az)))
    f = np.column_stack((np.zeros(n), np.cos(az), np.sin(az)))
    x4 = (u[:, None] * normal + plane_rad[:, None]
          * (np.cos(plane_ang)[:, None] * np.array([1.0, 0.0, 0.0])
             + np.sin(plane_ang)[:, None] * f))
    points = np.stack((np.zeros_like(x2), x2, x3, x4), axis=1)
    edges = np.stack([np.linalg.norm(points[:, i] - points[:, j], axis=1)
                      for i in range(4) for j in range(i)], axis=1)
    diam4 = edges.max(axis=1)
    volume = area * np.abs(u) / 3.0
    face_areas = np.stack([
        np.linalg.norm(np.cross(points[:, b] - points[:, a], points[:, c] - points[:, a]), axis=1) / 2.0
        for a, b, c in ((1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2))
    ], axis=1)
    h4 = np.divide(3.0 * volume, face_areas.max(axis=1), out=np.zeros_like(volume),
                   where=face_areas.max(axis=1) > 0)
    support4 = (diam4 <= M) & (h4 >= HEIGHT4)
    return {"G": volume, "diameter": diam4, "altitude_ratio": h4 / diam4,
            "edge_ratio": edges.min(axis=1) / diam4,
            # The longest-edge axis is isotropic after a global random rotation.
            "orientation": rng.random(n), "support": support4}


def pilot_geometry(samples: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    result: dict[str, object] = {"samples_per_order": samples, "seed": seed}
    for order in (3, 4):
        f = geometry_proposals(order, samples, rng)
        ok = f["support"]
        scalar = f["G"][ok]
        max_scalar = (math.sqrt(3.0) * M**2 / 4.0 if order == 3
                      else M**3 / (6.0 * math.sqrt(2.0)))
        result[f"g{order}"] = {
            "proposal_support_fraction": float(ok.mean()),
            "accepted_proposals": int(ok.sum()),
            "scalar_reciprocal_measure_quartiles": np.quantile(scalar, [.25, .5, .75]).tolist(),
            "suggested_scalar_edges": [0.0, *np.quantile(scalar, [.25, .5, .75]).tolist(), max_scalar],
            "suggested_diameter_split": float(np.median(f["diameter"][ok])),
            "suggested_altitude_ratio_split": float(np.median(f["altitude_ratio"][ok])),
            "suggested_edge_ratio_split": float(np.median(f["edge_ratio"][ok])),
            "orientation_split": 0.5,
        }
    return result


def shape_specs(order: int, design: dict) -> list[dict]:
    block = design[f"g{order}"]
    specs = [{"family": "pooled", "level": "all", "feature": None, "op": None, "cut": None}]
    for feature in (("diameter", "altitude_ratio", "orientation")
                    + (("edge_ratio",) if order == 4 else ())):
        cut = float(block[f"{feature}_split"])
        specs.extend([
            {"family": feature, "level": "low", "feature": feature, "op": "le", "cut": cut},
            {"family": feature, "level": "high", "feature": feature, "op": "gt", "cut": cut},
        ])
    return specs


def spec_mask(features: dict[str, np.ndarray], spec: dict) -> np.ndarray:
    if spec["family"] == "pooled":
        return np.ones(len(features["G"]), dtype=bool)
    values = features[spec["feature"]]
    return values <= spec["cut"] if spec["op"] == "le" else values > spec["cut"]


def compute_normalisers(order: int, design: dict, samples: int, seed: int,
                        blocks: int = 50) -> list[dict]:
    rng = np.random.default_rng(seed)
    edges = np.asarray(design[f"g{order}"]["scalar_edges"], dtype=float)
    specs = shape_specs(order, design)
    constants = J if order == 3 else J * C
    nbin = len(edges) - 1
    block_values = np.zeros((blocks, len(specs), nbin, 3), dtype=float)
    sizes = np.full(blocks, samples // blocks, dtype=int)
    sizes[: samples % blocks] += 1
    for block, size in enumerate(sizes):
        f = geometry_proposals(order, int(size), rng)
        scalar = f["G"]
        scalar_bin = np.searchsorted(edges, scalar, side="right") - 1
        scalar_bin[scalar == edges[-1]] = nbin - 1
        for si, spec in enumerate(specs):
            base = f["support"] & spec_mask(f, spec)
            for bi in range(nbin):
                take = base & (scalar_bin == bi)
                block_values[block, si, bi] = [take.mean(), np.mean(scalar * take),
                                                np.mean(scalar**2 * take)]
    rows: list[dict] = []
    for si, spec in enumerate(specs):
        for bi in range(nbin):
            vals = constants * block_values[:, si, bi]
            mean = vals.mean(axis=0)
            se = vals.std(axis=0, ddof=1) / math.sqrt(blocks)
            ratios = np.divide(vals[:, 0], vals[:, 1], out=np.full(blocks, np.nan),
                               where=vals[:, 1] > 0)
            poisson_g_mean = np.divide(vals[:, 2], vals[:, 1], out=np.full(blocks, np.nan),
                                       where=vals[:, 1] > 0)
            valid = np.isfinite(ratios)
            target_ratio = float(mean[0] / mean[1]) if mean[1] > 0 else math.nan
            target_ratio_se = (float(np.nanstd(ratios[valid], ddof=1) / math.sqrt(valid.sum()))
                               if valid.sum() > 1 else math.nan)
            valid_g = np.isfinite(poisson_g_mean)
            rows.append({
                "order": order, "spec_index": si, "scalar_bin": bi,
                "family": spec["family"], "level": spec["level"],
                "lower": float(edges[bi]), "upper": float(edges[bi + 1]),
                "volume": float(mean[1]), "volume_se": float(se[1]),
                "reciprocal_integral": float(mean[0]), "reciprocal_integral_se": float(se[0]),
                "G_integral": float(mean[2]), "G_integral_se": float(se[2]),
                "reciprocal_average": target_ratio,
                "reciprocal_average_se": target_ratio_se,
                "poisson_G_average": (float(mean[2] / mean[1]) if mean[1] > 0 else math.nan),
                "poisson_G_average_se": (float(np.nanstd(poisson_g_mean[valid_g], ddof=1)
                                                       / math.sqrt(valid_g.sum()))
                                         if valid_g.sum() > 1 else math.nan),
                "geometry_samples": samples, "geometry_blocks": blocks,
            })
    return rows


def overlap_volume(points: np.ndarray, side: float) -> float:
    h = points - points[0]
    spans = h.max(axis=0) - h.min(axis=0)
    return float(np.prod(side - spans)) if np.all(spans < side) else 0.0


def pair_array(points: np.ndarray, max_distance: float) -> tuple[np.ndarray, np.ndarray]:
    n = len(points)
    if n < 2:
        return np.empty((0, 2), dtype=int), np.empty(0)
    if n <= 50:
        pairs = np.asarray(list(itertools.combinations(range(n), 2)), dtype=int)
        dist = np.linalg.norm(points[pairs[:, 1]] - points[pairs[:, 0]], axis=1)
        take = dist <= max_distance
        return pairs[take], dist[take]
    pairs = cKDTree(points).query_pairs(max_distance, output_type="ndarray")
    if len(pairs) == 0:
        return np.empty((0, 2), dtype=int), np.empty(0)
    return pairs, np.linalg.norm(points[pairs[:, 1]] - points[pairs[:, 0]], axis=1)


def cliques(n: int, pairs: np.ndarray, order: int) -> Iterable[tuple[int, ...]]:
    adj = [set() for _ in range(n)]
    for i, j in pairs:
        adj[int(i)].add(int(j))
        adj[int(j)].add(int(i))
    for i in range(n):
        for j in sorted(x for x in adj[i] if x > i):
            common = adj[i].intersection(adj[j])
            for k in sorted(x for x in common if x > j):
                if order == 3:
                    yield (i, j, k)
                else:
                    for ell in sorted(x for x in common.intersection(adj[k]) if x > k):
                        yield (i, j, k, ell)


def tuple_spec_indices(order: int, values: dict[str, float], design: dict) -> list[int]:
    selected = []
    for i, spec in enumerate(shape_specs(order, design)):
        if spec["family"] == "pooled":
            selected.append(i)
        elif spec["op"] == "le" and values[spec["feature"]] <= spec["cut"]:
            selected.append(i)
        elif spec["op"] == "gt" and values[spec["feature"]] > spec["cut"]:
            selected.append(i)
    return selected


def estimate_raw(obs: Observations, design: dict, output: Path) -> tuple[dict, dict]:
    rgrid = np.asarray(design["k_radii"], dtype=float)
    e2 = np.asarray(design["g2"]["scalar_edges"], dtype=float)
    e3 = np.asarray(design["g3"]["scalar_edges"], dtype=float)
    e4 = np.asarray(design["g4"]["scalar_edges"], dtype=float)
    n3 = (len(e3) - 1) * len(shape_specs(3, design))
    n4 = (len(e4) - 1) * len(shape_specs(4, design))
    arrays = {
        "k": np.zeros((obs.replications, len(rgrid))),
        "g2": np.zeros((obs.replications, len(e2) - 1)),
        "g2G": np.zeros((obs.replications, len(e2) - 1)),
        "g3": np.zeros((obs.replications, n3)),
        "g3G": np.zeros((obs.replications, n3)),
        "g4": np.zeros((obs.replications, n4)),
        "g4G": np.zeros((obs.replications, n4)),
    }
    counts = {name: np.zeros_like(value, dtype=np.int32) for name, value in arrays.items() if name in ("g2", "g3", "g4")}
    allocations = {"g2": np.zeros(2, dtype=np.int64), "g3": np.zeros(3, dtype=np.int64),
                   "g4": np.zeros(4, dtype=np.int64)}
    started = time.perf_counter()
    query_radius = max(float(rgrid[-1]), P)
    for rep in range(obs.replications):
        lo, hi = int(obs.offsets[rep]), int(obs.offsets[rep + 1])
        points = obs.xyz[lo:hi]
        labels = obs.parent[lo:hi]
        if len(points) < 2:
            continue
        pairs, distances = pair_array(points, query_radius)
        for (i, j), distance in zip(pairs, distances):
            two = points[[i, j]]
            ov = overlap_volume(two, obs.side)
            if ov <= 0.0:
                continue
            weight = 2.0 / ov
            first = int(np.searchsorted(rgrid, distance, side="left"))
            if first < len(rgrid):
                arrays["k"][rep, first:] += weight
            if DELTA <= distance <= P:
                bi = int(np.searchsorted(e2, distance, side="right") - 1)
                if distance == e2[-1]:
                    bi = len(e2) - 2
                if 0 <= bi < len(e2) - 1:
                    arrays["g2"][rep, bi] += weight
                    arrays["g2G"][rep, bi] += weight * distance
                    counts["g2"][rep, bi] += 1
                    allocations["g2"][len(set(labels[[i, j]])) - 1] += 1
        close_pairs, _ = pair_array(points, M)
        if len(points) >= 3:
            for inds in cliques(len(points), close_pairs, 3):
                tri = points[list(inds)]
                area, diam, hmin, edge_ratio = triangle_geometry(tri)
                if diam > M or hmin < HEIGHT3:
                    continue
                bi = int(np.searchsorted(e3, area, side="right") - 1)
                if area == e3[-1]:
                    bi = len(e3) - 2
                if not 0 <= bi < len(e3) - 1:
                    continue
                ov = overlap_volume(tri, obs.side)
                if ov <= 0.0:
                    continue
                weight = 6.0 / ov
                normal = np.cross(tri[1] - tri[0], tri[2] - tri[0])
                orientation = abs(float(normal[2])) / float(np.linalg.norm(normal))
                vals = {"diameter": diam, "altitude_ratio": hmin / diam,
                        "edge_ratio": edge_ratio, "orientation": orientation}
                for si in tuple_spec_indices(3, vals, design):
                    col = si * (len(e3) - 1) + bi
                    arrays["g3"][rep, col] += weight
                    arrays["g3G"][rep, col] += weight * area
                    counts["g3"][rep, col] += 1
                allocations["g3"][len(set(labels[list(inds)])) - 1] += 1
        if len(points) >= 4:
            for inds in cliques(len(points), close_pairs, 4):
                tet = points[list(inds)]
                vol, diam, hmin, edge_ratio = tetra_geometry(tet)
                if diam > M or hmin < HEIGHT4:
                    continue
                bi = int(np.searchsorted(e4, vol, side="right") - 1)
                if vol == e4[-1]:
                    bi = len(e4) - 2
                if not 0 <= bi < len(e4) - 1:
                    continue
                ov = overlap_volume(tet, obs.side)
                if ov <= 0.0:
                    continue
                weight = 24.0 / ov
                edge_vectors = [(tet[i] - tet[j]) for i in range(4) for j in range(i)]
                longest = max(edge_vectors, key=np.linalg.norm)
                orientation = abs(float(longest[2])) / float(np.linalg.norm(longest))
                vals = {"diameter": diam, "altitude_ratio": hmin / diam,
                        "edge_ratio": edge_ratio, "orientation": orientation}
                for si in tuple_spec_indices(4, vals, design):
                    col = si * (len(e4) - 1) + bi
                    arrays["g4"][rep, col] += weight
                    arrays["g4G"][rep, col] += weight * vol
                    counts["g4"][rep, col] += 1
                allocations["g4"][len(set(labels[list(inds)])) - 1] += 1
    np.savez_compressed(output, **arrays, **{f"{k}_tuple_count": v for k, v in counts.items()})
    diagnostics = {
        "runtime_seconds": time.perf_counter() - started,
        "parent_allocation_unordered_admissible_tuple_counts": {
            key: {str(i + 1): int(value) for i, value in enumerate(vals)}
            for key, vals in allocations.items()
        },
        "estimator_parent_label_policy": "Labels excluded from every estimator; used only for this allocation count.",
    }
    return arrays | {f"{k}_tuple_count": v for k, v in counts.items()}, diagnostics


def analytic_k(r: np.ndarray) -> np.ndarray:
    out = np.empty_like(r, dtype=float)
    low = r < DELTA
    middle = (r >= DELTA) & (r <= P)
    high = r > P
    out[low] = 4.0 * math.pi * r[low]**3 / 3.0
    out[middle] = (4.0 * math.pi * DELTA**3 / 3.0
                   + 2.0 * math.pi * CK[2] * (r[middle]**2 - DELTA**2))
    out[high] = (4.0 * math.pi * DELTA**3 / 3.0
                 + 2.0 * math.pi * CK[2] * (P**2 - DELTA**2)
                 + 4.0 * math.pi * (r[high]**3 - P**3) / 3.0)
    return out


def mean_se(x: np.ndarray, scale: float) -> tuple[np.ndarray, np.ndarray]:
    return x.mean(axis=0) * scale, x.std(axis=0, ddof=1) * scale / math.sqrt(len(x))


def summarise(arrays: dict, design: dict, normalisers: dict[int, list[dict]],
              intensity: float, process: str) -> tuple[list[dict], list[dict]]:
    z = 1.959963984540054
    kgrid = np.asarray(design["k_radii"], dtype=float)
    kmean, kse = mean_se(arrays["k"], 1.0 / intensity**2)
    ktarget = analytic_k(kgrid) if process == "cluster" else 4.0 * math.pi * kgrid**3 / 3.0
    krows = []
    for column, (r, m, se, target) in enumerate(zip(kgrid, kmean, kse, ktarget)):
        contributing = int(np.count_nonzero(arrays["k"][:, column]))
        rel_half = float(z * se / target) if target > 0 else math.nan
        status = ("origin_not_assessed" if target == 0 else
                  ("no_observed_pairs_zero_variance_is_not_precision" if contributing == 0 else
                   ("meets_10pct_pointwise_goal" if rel_half <= .10 else "underpowered_for_10pct_goal")))
        krows.append({"radius": float(r), "estimate": float(m), "mc_se": float(se),
                      "ci_low": float(m - z * se), "ci_high": float(m + z * se),
                      "target": float(target), "residual": float(m - target),
                      "contributing_realisations": contributing,
                      "relative_mc_halfwidth_vs_target": rel_half,
                      "precision_status": status,
                      "interval_scope": "pointwise realisation-level Monte Carlo",
                      "process": process})
    rows: list[dict] = []
    # Pair normalisers are exact.
    e2 = np.asarray(design["g2"]["scalar_edges"], dtype=float)
    for bi, (lo, hi) in enumerate(zip(e2[:-1], e2[1:])):
        volume = 4.0 * math.pi * (hi**3 - lo**3) / 3.0
        recip = 2.0 * math.pi * (hi**2 - lo**2)
        gint = math.pi * (hi**4 - lo**4)
        for weighted, key in ((False, "g2"), (True, "g2G")):
            mean, se = mean_se(arrays[key][:, bi], 1.0 / (intensity**2 * volume))
            target = ((CK[2] if process == "cluster" else gint / volume) if weighted
                      else (CK[2] * recip / volume if process == "cluster" else 1.0))
            tuples = int(arrays["g2_tuple_count"][:, bi].sum())
            rel_half = float(z * se / target) if target else math.nan
            status = ("no_observed_tuples" if tuples == 0 else
                      ("meets_10pct_pointwise_goal" if rel_half <= 0.10 else "underpowered_for_10pct_goal"))
            rows.append({"order": 2, "family": "pooled", "level": "all", "scalar_bin": bi,
                         "lower": float(lo), "upper": float(hi),
                         "statistic": "compensated" if weighted else "g",
                         "estimate": float(mean), "mc_se": float(se),
                         "ci_low": float(mean - z * se), "ci_high": float(mean + z * se),
                         "target": float(target), "ratio_to_target": float(mean / target),
                         "contributing_realisations": int(np.count_nonzero(arrays["g2"][:, bi])),
                         "unordered_tuple_count": tuples,
                         "normaliser_relative_se": 0.0, "estimate_normaliser_se": 0.0,
                         "combined_independent_se": float(se), "target_normaliser_se": 0.0,
                         "relative_mc_halfwidth_vs_target": rel_half, "precision_status": status,
                         "zero_variance_interpretation": ("no information; zero empirical variance is not precision"
                                                          if tuples == 0 else "not applicable"),
                         "interval_scope": "pointwise realisation-level Monte Carlo; normaliser error separate",
                         "process": process})
    for order in (3, 4):
        edges = np.asarray(design[f"g{order}"]["scalar_edges"], dtype=float)
        nbin = len(edges) - 1
        for norm in normalisers[order]:
            col = int(norm["spec_index"]) * nbin + int(norm["scalar_bin"])
            volume = float(norm["volume"])
            if not volume > 0.0:
                # This scalar/shape intersection is geometrically empty at the
                # normaliser resolution and is not a positive-volume bin.
                continue
            for weighted, key in ((False, f"g{order}"), (True, f"g{order}G")):
                scale = 1.0 / (intensity**order * volume) if volume > 0 else math.nan
                mean, se = mean_se(arrays[key][:, col], scale)
                if weighted:
                    target = CK[order] if process == "cluster" else float(norm["poisson_G_average"])
                else:
                    target = (CK[order] * float(norm["reciprocal_average"])
                              if process == "cluster" else 1.0)
                tuples = int(arrays[f"g{order}_tuple_count"][:, col].sum())
                normaliser_rel = float(norm["volume_se"] / volume) if volume > 0 else math.nan
                estimate_norm_se = abs(float(mean)) * normaliser_rel
                combined_se = math.sqrt(float(se)**2 + estimate_norm_se**2)
                if process == "cluster" and not weighted:
                    target_norm_se = float(CK[order] * norm["reciprocal_average_se"])
                elif process == "poisson" and weighted:
                    target_norm_se = float(norm["poisson_G_average_se"])
                else:
                    target_norm_se = 0.0
                rel_half = float(z * se / target) if target else math.nan
                status = ("no_observed_tuples" if tuples == 0 else
                          ("meets_10pct_pointwise_goal" if rel_half <= 0.10 else "underpowered_for_10pct_goal"))
                rows.append({"order": order, "family": norm["family"], "level": norm["level"],
                             "scalar_bin": int(norm["scalar_bin"]), "lower": norm["lower"],
                             "upper": norm["upper"], "statistic": "compensated" if weighted else "g",
                             "estimate": float(mean), "mc_se": float(se),
                             "ci_low": float(mean - z * se), "ci_high": float(mean + z * se),
                             "target": float(target), "ratio_to_target": float(mean / target),
                             "contributing_realisations": int(np.count_nonzero(arrays[f"g{order}"][:, col])),
                             "unordered_tuple_count": tuples,
                             "normaliser_relative_se": normaliser_rel,
                             "estimate_normaliser_se": estimate_norm_se,
                             "combined_independent_se": combined_se,
                             "target_normaliser_se": target_norm_se,
                             "relative_mc_halfwidth_vs_target": rel_half,
                             "precision_status": status,
                             "zero_variance_interpretation": ("no information; zero empirical variance is not precision"
                                                              if tuples == 0 else "not applicable"),
                             "interval_scope": "pointwise realisation-level Monte Carlo; normaliser error separate",
                             "process": process})
    return krows, rows


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    keys = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def deterministic_checks() -> dict:
    tri = np.array([[0., 0., 0.], [3., 0., 0.], [0., 4., 0.]])
    tet = np.array([[0., 0., 0.], [1., 0., 0.], [0., 2., 0.], [0., 0., 3.]])
    tri_g = triangle_geometry(tri)
    tet_g = tetra_geometry(tet)
    overlap_points = np.array([[0., 0., 0.], [2., -3., 5.], [-1., 4., 1.]])
    overlap = overlap_volume(overlap_points, 10.0)
    expected_overlap = (10.0 - 3.0) * (10.0 - 7.0) * (10.0 - 5.0)
    eps = 1e-11
    checks = {
        "triangle_area_3_4_5": {"actual": tri_g[0], "expected": 6.0, "pass": abs(tri_g[0] - 6.0) < eps},
        "triangle_diameter": {"actual": tri_g[1], "expected": 5.0, "pass": abs(tri_g[1] - 5.0) < eps},
        "triangle_min_altitude": {"actual": tri_g[2], "expected": 2.4, "pass": abs(tri_g[2] - 2.4) < eps},
        "tetrahedron_volume": {"actual": tet_g[0], "expected": 1.0, "pass": abs(tet_g[0] - 1.0) < eps},
        "box_overlap": {"actual": overlap, "expected": expected_overlap, "pass": abs(overlap - expected_overlap) < eps},
        "ordered_factors": {"pair": math.factorial(2), "triple": math.factorial(3), "quad": math.factorial(4),
                            "pass": [math.factorial(k) for k in (2, 3, 4)] == [2, 6, 24]},
        "K_endpoint_delta": {"left": float(4 * math.pi * DELTA**3 / 3),
                             "right": float(analytic_k(np.array([DELTA]))[0]),
                             "pass": abs(4 * math.pi * DELTA**3 / 3 - analytic_k(np.array([DELTA]))[0]) < eps},
    }
    checks["all_pass"] = all(v.get("pass", False) for v in checks.values())
    return checks


def model_metadata() -> dict:
    return {
        "delta_km": DELTA, "triangle_min_altitude_km": HEIGHT3,
        "tetrahedron_min_altitude_km": HEIGHT4, "max_simplex_diameter_km": M,
        "pair_max_distance_km": P, "a2_km_minus5": A2, "a3_km_minus7": A3,
        "a4_km_minus9": A4, "rho_km_minus3": RHO,
        "C2_km": CK[2], "C3_km2": CK[3], "C4_km3": CK[4],
        "I_km2": I, "B_km2": B, "C_km2": C, "J_km4": J,
        "stream_candidate_rates_per_km3": STREAM_RATES,
    }


def make_plots(folder: Path, krows: list[dict], rows: list[dict], poisson_k: list[dict] | None = None,
               poisson_rows: list[dict] | None = None) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
    r = np.array([x["radius"] for x in krows]); est = np.array([x["estimate"] for x in krows])
    lo = np.array([x["ci_low"] for x in krows]); hi = np.array([x["ci_high"] for x in krows])
    target = np.array([x["target"] for x in krows]); pois = 4 * math.pi * r**3 / 3
    fig, ax = plt.subplots(2, 1, figsize=(7.2, 6.2), sharex=True)
    ax[0].plot(r, target, color="black", label="model")
    ax[0].plot(r, pois, color="#888888", ls="--", label="Poisson")
    ax[0].plot(r, est, color="#007F7B", label="estimate")
    ax[0].fill_between(r, lo, hi, color="#007F7B", alpha=.2, label="pointwise 95% MC")
    ax[0].set_ylabel("K(r) [km³]"); ax[0].legend(frameon=False)
    ax[1].axhline(0, color="black", lw=.8); ax[1].plot(r, est - target, color="#D97706")
    ax[1].fill_between(r, lo - target, hi - target, color="#D97706", alpha=.2)
    ax[1].set_xlabel("r [km]"); ax[1].set_ylabel("estimate − model")
    fig.tight_layout(); fig.savefig(folder / "k_function.png", dpi=180); fig.savefig(folder / "k_function.pdf"); plt.close(fig)
    pooled = [x for x in rows if x["family"] == "pooled"]
    for statistic, filename in (("g", "correlations"), ("compensated", "compensated")):
        fig, axes = plt.subplots(2, 3, figsize=(11.2, 6.0))
        for col, order in enumerate((2, 3, 4)):
            rr = [x for x in pooled if x["order"] == order and x["statistic"] == statistic]
            x = np.arange(len(rr)); y = np.array([a["estimate"] for a in rr]); t = np.array([a["target"] for a in rr])
            se = np.array([a["mc_se"] for a in rr])
            axes[0, col].errorbar(x, y, yerr=1.96 * se, fmt="o", color="#007F7B", capsize=2)
            axes[0, col].plot(x, t, color="black", marker="_", ls="none", ms=12)
            if statistic == "g": axes[0, col].set_yscale("log")
            axes[0, col].set_title(f"order {order}"); axes[0, col].set_ylabel(statistic)
            ratio = y / t; ratio_se = se / t
            axes[1, col].axhline(1, color="black", lw=.8)
            axes[1, col].errorbar(x, ratio, yerr=1.96 * ratio_se, fmt="o", color="#D97706", capsize=2)
            axes[1, col].set_ylabel("estimate / target"); axes[1, col].set_xlabel("scalar bin")
        fig.tight_layout(); fig.savefig(folder / f"{filename}.png", dpi=180); fig.savefig(folder / f"{filename}.pdf"); plt.close(fig)
    shape = [x for x in rows if x["statistic"] == "compensated" and x["family"] != "pooled"
             and int(x["unordered_tuple_count"]) > 0]
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2))
    for ax, order in zip(axes, (3, 4)):
        subset = [x for x in shape if x["order"] == order]
        labels = sorted({(x["family"], x["level"]) for x in subset})
        for j, lab in enumerate(labels):
            rr = [x for x in subset if (x["family"], x["level"]) == lab]
            x = np.arange(len(rr)) + .05 * (j - len(labels) / 2)
            y = np.array([a["ratio_to_target"] for a in rr]); se = np.array([a["mc_se"] / a["target"] for a in rr])
            ax.errorbar(x, y, yerr=1.96 * se, fmt="o", ms=3, capsize=1.5, label=f"{lab[0]} {lab[1]}")
        ax.axhline(1, color="black", lw=.8); ax.set_title(f"order {order}")
        ax.set_xlabel("scalar bin"); ax.set_ylabel("compensated / Ck"); ax.legend(frameon=False, fontsize=7)
    fig.tight_layout(); fig.savefig(folder / "shape_strata.png", dpi=180); fig.savefig(folder / "shape_strata.pdf"); plt.close(fig)
    if poisson_k is not None and poisson_rows is not None:
        fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.0))
        pk = np.array([x["estimate"] / x["target"] if x["target"] else np.nan for x in poisson_k])
        axes[0].plot([x["radius"] for x in poisson_k], pk, color="#007F7B")
        axes[0].axhline(1, color="black", lw=.8); axes[0].set_xlabel("r [km]"); axes[0].set_ylabel("Poisson K estimate / target")
        pp = [x for x in poisson_rows if x["family"] == "pooled" and x["statistic"] == "g"]
        for order in (2, 3, 4):
            rr = [x for x in pp if x["order"] == order]
            axes[1].plot(np.arange(len(rr)), [x["estimate"] for x in rr], marker="o", label=f"g{order}")
        axes[1].axhline(1, color="black", lw=.8); axes[1].set_xlabel("bin"); axes[1].set_ylabel("Poisson g estimate"); axes[1].legend(frameon=False)
        fig.tight_layout(); fig.savefig(folder / "poisson_controls.png", dpi=180); fig.savefig(folder / "poisson_controls.pdf"); plt.close(fig)


def run_stage(stage: str, design_path: Path | None, replications: int, side: float,
              seed: int, geometry_samples: int, poisson_replications: int) -> None:
    folder = ROOT / stage
    folder.mkdir(parents=True, exist_ok=True)
    checks = deterministic_checks()
    dump_json(folder / "deterministic_checks.json", checks)
    if not checks["all_pass"]:
        raise AssertionError("deterministic checks failed")
    if stage == "pilot":
        geometry = pilot_geometry(geometry_samples, seed + 1)
        dump_json(folder / "geometry_pilot.json", geometry)
        q3, q4 = geometry["g3"], geometry["g4"]
        pair_edges = np.sqrt(np.linspace(DELTA**2, P**2, 7)).tolist()
        design = {
            "status": "pilot design; production design must be frozen separately",
            "replications": replications, "side_km": side,
            "k_radii": sorted(set([0.0, DELTA / 2, DELTA, P, 100.0]
                                   + np.linspace(0, 100, 31).tolist())),
            "g2": {"scalar_edges": pair_edges},
            "g3": {"scalar_edges": q3["suggested_scalar_edges"],
                   "diameter_split": q3["suggested_diameter_split"],
                   "altitude_ratio_split": q3["suggested_altitude_ratio_split"],
                   "edge_ratio_split": q3["suggested_edge_ratio_split"],
                   "orientation_split": 0.5},
            "g4": {"scalar_edges": q4["suggested_scalar_edges"],
                   "diameter_split": q4["suggested_diameter_split"],
                   "altitude_ratio_split": q4["suggested_altitude_ratio_split"],
                   "edge_ratio_split": q4["suggested_edge_ratio_split"],
                   "orientation_split": 0.5},
        }
        dump_json(folder / "pilot_design_used.json", design)
    else:
        if design_path is None:
            raise ValueError("production needs --design")
        design = json.loads(design_path.read_text())
        if int(design["replications"]) != replications or float(design["side_km"]) != side:
            raise ValueError("CLI production size must match the frozen design")
    normals = {order: compute_normalisers(order, design, geometry_samples, seed + 10 + order)
               for order in (3, 4)}
    dump_json(folder / "geometric_normalisers.json", {str(k): v for k, v in normals.items()})
    obs, sampler_diag = simulate_cluster(replications, side, seed)
    save_observations(folder / "observations.npz", obs)
    arrays, estimator_diag = estimate_raw(obs, design, folder / "replicate_contributions.npz")
    krows, rows = summarise(arrays, design, normals, RHO, "cluster")
    write_csv(folder / "k_summary.csv", krows); write_csv(folder / "correlation_summary.csv", rows)
    dump_json(folder / "run_metadata.json", {
        "stage": stage, "seed": seed, "replications": replications, "side_km": side,
        "known_intensity_used": RHO, "model": model_metadata(),
        "sampler": sampler_diag, "estimator": estimator_diag,
        "geometry_samples_per_order": geometry_samples,
        "software": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__,
                     "matplotlib": importlib.metadata.version("matplotlib")},
        "uncertainty": "Pointwise normal intervals from independent realisation contributions; geometric-normaliser error reported separately.",
    })
    poisson_k = poisson_rows = None
    if stage == "production":
        control_side = float(design["poisson_control"]["side_km"])
        control_rho = float(design["poisson_control"]["intensity_per_km3"])
        pobs = poisson_observations(poisson_replications, control_side, control_rho, seed + 1000)
        save_observations(folder / "poisson_observations.npz", pobs)
        parrays, pdiag = estimate_raw(pobs, design, folder / "poisson_replicate_contributions.npz")
        poisson_k, poisson_rows = summarise(parrays, design, normals, control_rho, "poisson")
        write_csv(folder / "poisson_k_summary.csv", poisson_k)
        write_csv(folder / "poisson_correlation_summary.csv", poisson_rows)
        dump_json(folder / "poisson_metadata.json", {"replications": poisson_replications,
                  "side_km": control_side, "intensity_per_km3": control_rho,
                  "seed": seed + 1000, "estimator": pdiag})
    make_plots(folder, krows, rows, poisson_k, poisson_rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("pilot", "production"), required=True)
    parser.add_argument("--design", type=Path)
    parser.add_argument("--replications", type=int, required=True)
    parser.add_argument("--side", type=float, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--geometry-samples", type=int, default=250_000)
    parser.add_argument("--poisson-replications", type=int, default=200)
    args = parser.parse_args()
    run_stage(args.stage, args.design, args.replications, args.side, args.seed,
              args.geometry_samples, args.poisson_replications)


if __name__ == "__main__":
    main()
