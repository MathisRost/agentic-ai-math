# Agent decision and work summary

## Scope

This document is a concise, auditable summary of the participating agents'
inputs, actions, decisions, evidence and conclusions. It does not reproduce or
infer private chain-of-thought. Exact token counts were not exposed by the
interfaces; the separate cost estimate is therefore approximate.

## Participants

| Role | Configuration | Responsibility |
|---|---|---|
| Coordinating writer | Exact model identifier unavailable | Owned and revised the manuscript, integrated verified results, commissioned the fresh-reader check and performed final QA |
| Simulation specialist | `gpt-5.6-sol`, `xhigh` | Implemented and ran the precision pilot, production study, controls and numerical diagnostics |
| Fresh reader | `gpt-5.6-sol`, `xhigh` | Independently checked whether the frozen paper could be understood without the writer's private context |

## 1. Coordinating writer

### Inputs and constraints

The writer read the sandbox instructions, paper structure, materials index,
architecture, simulation plan and the `mathis-writer` and PDF-verification
workflows. The governing target was the exact full-correlation problem, not the
earlier approximate empirical objective. Existing mathematical audits and the
bounded literature check were treated as verified inputs rather than reopened
without cause.

### Main decisions

- Preserve the checked analytical construction and proofs while revising their
  presentation.
- Separate three evidentiary layers throughout: the analytical existence
  theorem, numerical validation of its sampler and estimators, and the still
  unperformed comparison with historical earthquake data.
- Do not report any simulation result until its output artefacts existed.
- Use one fixed expanded-witness parameter set at every correlation order.
- Add a common translation-corrected estimator appendix so that full
  correlations, all parent allocations and edge corrections were explicit.
- Report the fourth-order experiment as underpowered rather than changing the
  estimand, dropping empty windows or choosing a more favourable parameter set.

### Manuscript outcome

The writer revised the title, abstract, introduction and preliminaries; added
the simulation and later-earthquake-comparison sections; integrated the
$K$-function, full-correlation, compensated, shape/orientation, Poisson-control
and normaliser-convergence results; and retained the checked analytical proof.
The final paper makes no claim that the simulation proves the continuum
identities and no claim that the model has been fitted to an earthquake
catalogue.

## 2. Simulation specialist

### Design rationale

The specialist used the same expanded witness at all orders. A 10,000-window
pilot measured runtime, tuple occupancy and realisation-level uncertainty before
the production design was frozen. The pilot indicated that pairs and triangles
could be estimated usefully but that tetrahedra would remain sparse. The frozen
production design therefore used 200,000 independent 1,200 km cubes, fixed bins
and shape/orientation splits, one million geometric proposals per higher order,
and a separate high-intensity Poisson control.

Every realisation was retained, including empty and low-count windows. Parent
labels were stored only for diagnostics and were excluded from the estimators,
which enumerated all admissible tuples and hence all parent allocations. The
known analytical intensity was used for the primary implementation check.

### Checks and repairs

The specialist checked known triangle and tetrahedron geometries, ordered-tuple
factors, rectangular translation overlap, continuity of the analytical
$K$-curve, count identities, Poisson $K/g_2/g_3/g_4$ targets and an independent
normaliser calculation. One proposed triangle shape/bin intersection was shown
analytically to have zero geometric volume and was excluded as empty rather
than treated as a zero-variance estimate. A filename collision that had
overwritten only a count summary was found during the final audit; both count
tables were regenerated from intact raw observation offsets, without changing
any estimator or numerical result.

### Numerical conclusions

- Production retained 200,000 realisations, including 47,055 empty cubes.
- The pooled $g_2$ estimate/target ratios were 0.9991--1.0060, with roughly 1%
  pointwise relative half-widths.
- The pooled $g_3$ ratios were 0.9968--1.0202, with roughly 5% half-widths.
- Only 126 admissible tetrahedra were observed. The pooled $g_4$ ratios were
  unstable and every fourth-order bin was classified as underpowered.
- The analytical $K$-curve lay in every pointwise interval at radii with
  observed pairs. The two smallest positive radii contained no pair and were
  labelled as providing no information.
- Every pooled Poisson-control interval contained its target.

The specialist therefore concluded that the implementation was numerically
consistent with the theorem at useful second- and third-order precision, while
the fourth-order study was inconclusive.

## 3. Fresh reader

### Independence protocol

The pre-reader paper was frozen with SHA-256 hashes. The reader received only
the frozen PDF, source, figures, references, a neutral brief and the reader
instructions. The reader did not see writer notes, simulation code or reports,
previous reviews, sibling work or external sources, and did not edit the
manuscript.

### Findings

The reader found the main theorem and construction followable and found the
distinction between proof, numerical validation and the absent catalogue
comparison clear. No mathematical defect was suspected in the scoped reading.
Two substantive comprehension failures were identified:

1. The physical scalar-bin edges, shape thresholds and pointwise interval
   formula were not recoverable from the paper.
2. The discussion referred to properties recorded only in inaccessible
   “accompanying research notes”.

The reader also suggested renaming the packet energy because $H$ was already
used for the tetrahedral altitude cutoff, and optionally moving the rooted Gibbs
representation to an appendix.

## 4. Writer integration and final verification

The writer added a complete numerical-design table, the $K$-grid rule, the
geometric-normaliser definition and the realisation-level interval formula.
The inaccessible-notes paragraph was removed, and the packet energy was renamed
$\mathcal E$. The rooted Gibbs representation remained in the main text because
it is short and self-contained; this optional structural suggestion was not a
comprehension failure.

The project then compiled successfully with `latexmk`. The final log contained
no LaTeX/package warnings, undefined references or box warnings. All 22 pages
were rendered with Poppler and visually inspected in contact sheets, with
full-size checks of the new design table, the simulation-to-earthquake boundary
and the estimator appendix. One visible missing backslash was repaired before
the final build. The app's separate single-file checker could not resolve the
project's relative `sections/...` inputs; this was recorded as a checker
limitation rather than a project-build failure.

## 5. Remaining limitations

- Finite-bin Monte Carlo checks do not prove continuum identities.
- Reported intervals are pointwise rather than simultaneous.
- Rare-event normal approximations are rough at fourth order.
- Geometric calculations use floating-point rather than interval-certified
  arithmetic.
- The witness intensity is extremely low and the model has no temporal,
  magnitude, fault or observation component.
- The historical observation mask and event-selection rule were not recovered,
  so no matched earthquake-data comparison was performed.
- Exact agent token totals and private chain-of-thought are unavailable.
