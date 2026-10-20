# Simulation report: expanded finite-cluster witness

Run completed 19 October 2026. This is an implementation study of the exact
dependent finite-cluster model, not a proof of its continuum identities and not
an earthquake-catalogue comparison.

## Main result

The translation-corrected estimators are numerically consistent with the
analytical model at the precision actually attained. The pooled pair and
triangle estimates meet the predeclared pointwise numerical goal. The
tetrahedron study does not: only 126 admissible unordered tetrahedra were
observed in 200,000 independent windows, leaving all four pooled fourth-order
bins and all fourth-order shape strata underpowered. These sparse results are
retained rather than replaced by a different estimand or parameter set.

The study used the expanded witness throughout:

| quantity | value |
|---|---:|
| delta = h | 0.49 km |
| H | 0.98 km |
| M | 36.21 km |
| P | 50.01 km |
| a2 | 1e-13 km^-5 |
| a3 | 9.659468220104731e-19 km^-7 |
| a4 | 3.141868710745654e-24 km^-9 |
| rho | 1.571273848878242e-9 km^-3 |
| C2 | 40503.84337695874 km |
| C3 | 248998981.41316935 km^2 |
| C4 | 515442830546.145 km^3 |

No constants were fitted to the simulated estimates.

## Design and estimators

The precision pilot used 10,000 independent 1,200 km cubes and 250,000
independent geometric proposals per higher order. It found 13,118 admissible
pairs, 322 admissible triangles and four admissible tetrahedra. The four area
and volume bins were then frozen at quartiles of the appropriate reciprocal
geometric measure. Shape cutoffs were frozen at the corresponding proposal
medians. The production design used 200,000 independent cubes with the same
side length and one million geometric proposals per order. The production
seed was 2026101903.

The numerical design goal was a pointwise 95% Monte Carlo interval half-width
of at most 10% of the fixed target in pooled central bins. This is a precision
goal, not a tolerance for the exact mathematical laws. Pilot scaling already
predicted that a feasible production run would leave g4 underpowered; reaching
the same goal at order four would require a multi-million-window run.

For every observed unordered tuple, the implementation applies the factors
2!, 3! or 4! and the cube translation correction

    product_q (L - (max_i h_iq - min_i h_iq)).

It enumerates every admissible tuple of observed points, irrespective of its
parent labels. Parent labels are saved and used only for sampler diagnostics.
Empty and low-count realisations contribute zeros to the replicate-level sums;
none are discarded. Monte Carlo standard errors are computed from the 200,000
independent realisation contributions. All displayed 95% intervals are
pointwise normal intervals. No simultaneous band or global curve claim is
made.

The pair shell volumes and reciprocal integrals are exact. For triangles and
tetrahedra, an independent geometric importance sampler uses proposal
densities 1/(J A) and 1/(J C V). It estimates both the relative-configuration
volume and the reciprocal integral, in 50 independent blocks. The resulting
finite-sample ratio normaliser is not exactly unbiased. Its standard error is
reported separately from the realisation-level error for both estimates and
targets.

The shape diagnostics split diameter and minimum-altitude/diameter at their
pilot medians. Tetrahedra also split minimum-edge/diameter. The isotropy
diagnostic splits triangles by the absolute vertical component of their unit
normal and tetrahedra by that of their longest-edge axis, both at 0.5. Matching
geometric normalisers include the same orientation strata.

## Controls

All deterministic tests passed: a 3-4-5 triangle, a coordinate tetrahedron of
volume one, an exact rectangular overlap calculation, ordered-tuple factors,
and continuity of the analytical K curve at delta.

A separate Poisson control used 200 independent 120 km cubes at known intensity
3e-5 km^-3. This deliberately higher intensity tests the estimators rather
than reproducing the sparse cluster-model count regime. Across the pooled
K, g2, g3 and g4 bins, estimates and compensated statistics were within 1.65
realisation-level standard errors of their Poisson targets. Fourth-order
Poisson bins were still labelled underpowered whenever their pointwise
half-width exceeded the 10% numerical goal.

The one-million-proposal production normalisers were also compared with an
independent 250,000-proposal calculation using the frozen bins. For pooled
bins, the largest volume difference was 0.68% at order three and 1.95% at
order four; the largest reciprocal-average difference was 0.14% and 0.58%,
respectively. Every pooled volume difference was within 1.70 combined standard
errors. One sparse fourth-order altitude shape bin changed by 10.8% in volume,
but this was only 0.72 combined standard errors and its production volume
relative standard error was 5.5%; it is not suitable for a precise shape
claim.

One proposed triangle intersection is analytically empty and is excluded from
the CSV summaries and plots: the low-altitude-ratio stratum in the highest area
bin. Indeed, h_min/d_max <= 0.3281 implies
A = d_max h_min/2 <= 0.5*0.3281*M^2 = 215.10 km^2, below that bin's lower edge
223.24 km^2. It is classified as geometrically empty, not as a zero-variance
estimate.

## Production results

The simulation retained 200,000 realisations, including 47,055 empty windows,
and saved 543,698 observed points. The mean count was 2.71849 against the known
mean 2.715161; the difference was 0.64 realisation-level standard errors. The
sample count variance was 5.32744.

For K, no pair was observed below or at delta. The resulting zero empirical
variance is explicitly labelled as no information, not attained precision.
From r = 3.33 km onwards, the pointwise half-width was below 10% of the model
target. Over the radii with nonzero contributions, the largest absolute model
residual was 1.57 standard errors. K is only an integrated second-order check.

The pooled correlation results are:

| order | unordered tuples per bin | estimate/target range | compensated/constant range | pointwise half-width / target | status |
|---|---:|---:|---:|---:|---|
| 2 | 42,596--44,647 | 0.9991--1.0060 | 0.9995--1.0054 | 0.94%--1.05% | goal met |
| 3 | 1,598--1,649 | 0.9968--1.0202 | 0.9889--1.0184 | 4.9%--5.4% | goal met |
| 4 | 23--40 | 0.7048--1.2218 | 0.7082--1.1676 | 28.8%--39.1% | underpowered |

The g4 values should not be read as a stable shape or volume trend. One raw-g
pointwise interval ends just below its target (upper endpoint 0.993 times the
target), while the corresponding compensated interval includes the constant.
With four pooled bins, many shape bins and no simultaneous correction, this is
not evidence of a systematic discrepancy; the predeclared precision criterion
classifies every pooled fourth-order result as inconclusive.

Of 23 positive-volume third-order shape/bin intersections, 20 met the 10%
pointwise goal and three remained underpowered. All 31 populated fourth-order
shape/bin intersections were underpowered, and one positive-volume shape bin
had no observed tuple. Zero-tuple bins are labelled as having no information.

Although labels never enter an estimator, the diagnostic allocation counts
confirm that enumeration was not restricted to same-parent tuples:

| order | one parent | two parents | three parents | four parents |
|---|---:|---:|---:|---:|
| 2 | 260,549 | 247 | -- | -- |
| 3 | 6,501 | 34 | 0 | -- |
| 4 | 123 | 3 | 0 | 0 |

The absence of observed three- and four-parent local higher-order tuples is a
finite-sample consequence of the very low intensity, not an estimator filter.

## Files and reproducibility

`production/observations.npz` contains coordinates, optional parent labels,
stream codes, and an offsets array of length 200,001. Replicate b occupies
rows `offsets[b]:offsets[b+1]`; equal adjacent offsets preserve empty windows.
`production/replicate_contributions.npz` contains the realisation-level raw
translation-corrected sums used for uncertainty. The corresponding Poisson
files use the same format. CSV files contain the final summaries and counts;
JSON files contain parameters, normalisers and diagnostics. PNG and PDF plots
are both supplied.

Reproduction commands and the artifact map are in `README.md`. The source uses
floating-point geometry and is not interval-certified. No estimated-intensity
sensitivity analysis, simultaneous band, earthquake observation mask, event
selection, catalogue comparison, temporal model or magnitude model was added.
The 1,200 km cube is a numerical implementation window, not a recovered
historical footprint.

The recorded software environment was Python 3.9.6, NumPy 2.0.2, SciPy 1.13.1
and Matplotlib 3.9.4.
