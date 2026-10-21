# Integrated revision outcome

The independent reader read the complete frozen `review/draft_v01.tex`, SHA256 `2cd01584032ac721ceb65a4eefcccec93287ae44f97b375171b4a23da2c00af2`, and both assigned figures in a fresh context. The report is `reader/review_v01.md`, SHA256 `f5b55b410d811b8903094f541dea8a86b82beb1bdc53b80b96de3ae5c3851cf7`. Access was limited by an explicit file packet, not operating-system isolation. The reader used no author conversations, simulation code, prior reviews or desired verdict.

The coordinator accepted and repaired all four actionable findings:

1. Stated that rejection estimates and their variances use all proposals, with rejected rows contributing zero. Added the expectation identity. Inspection of the code and saved contributions confirmed that this convention was already implemented; numerical results did not change.
2. Specified uniform reference draws from the product of unit balls, its `(4*pi/3)^(n-1)` volume factor, and both reference estimators. These match the existing code and reference statistics.
3. Replaced the angular tetrahedron symbol `Delta_3` by `V`, preserving the established convention in which `Delta_3` is triangle area. No Jacobian or other mathematical constant changed.
4. Used the coder's padded v02 configuration figure. Saved coordinates and captions retain the distinction between ordinary windows, a conditional illustration and a sampled cluster mark.

Also removed a redundant simulation disclaimer, added PDF title metadata and prevented figures from interrupting the appendix's opening paragraph. The optional suggestion to relocate probability-budget arithmetic was not adopted: it is a short explicit verification directly beside the definition of the sphere law, and changing the proof order offered little benefit.

These were local clarification, notation and layout changes. No target, theorem, proof dependency, sample, reported result or estimator changed. The coordinator checked the mathematical diff and nearby references. The final manuscript was not independently reread; there was no substantial replacement of a central argument requiring another first-reader cycle.

Validation: two-pass local LaTeX compilation succeeds without warnings, overfull boxes or undefined references. The resulting 23-page PDF was rendered and visually inspected: pages 1–16 were unchanged by the final float-placement adjustment; revised pages 17–23 were inspected after it. Figures, tables, formulas and references are legible and unclipped. The coordinator separately checked the sphere/cluster sampling weights and small-ball law, and recomputed every empirical factorial-integral mean from the saved arrays. Ordinary counts agree with all saved coordinates. The maximum displayed discrepancy is 1.82011185 estimated standard errors.

No suspected theorem defect was identified by this exposition reader; this does not certify the proof. There are no unresolved reader repair requests. The scientific limits remain explicit: S1 rather than S0, constructed coefficients, nonergodicity, infinite fourth moments, importance-sampled correlation estimates, restricted finite observables, and no empirical earthquake fit or novelty claim.
