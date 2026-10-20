# Critical review — approach 1, submission v02

- Run / reviewer model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Submission SHA-256: `8e0835cf889621515534b83810cb5d00a7494117721fcd8461723a6e0008f160`.
- Assigned-issue SHA-256: `e8e700be4ea87d42367b8d5982e378ec19aebca7945fea20b3a86384c68a1bc5`.
- Context received: the complete frozen `context_packets/review_1_v02.md` packet; its listed setup, common, shared-literature and bibliography files; `tracks/approach_1/submissions/v02.md`; and `reviews/approach_1/issues_v01_for_author.md`. Every packet hash matched.
- Context excluded: submission v01, review v01, author work notes and conversations, every other approach and every other track submission or review.
- Review type: fresh delta review of repair round 1. The four assigned repairs were checked individually, and every inference materially affected by them was re-established from v02.

## Verdict and exact scope

**All four assigned issues are closed. No further repair round is needed for approach 1 v02.** I found no new correctness defect in the revised natural-language proof.

The checked argument proves a restricted exact theorem, not the full governing target. For every (M,h_3,h_4) satisfying

\[
0<h_3<\frac{\sqrt3}{2}M,
\qquad
0<h_4<\sqrt{\frac23}M,
\]

and every intensity prescribed in advance with

\[
0<\lambda_0\le \lambda_*(M,h_4),
\]

the construction gives one stationary, isotropic, simple and locally finite point process on all of \(\mathbb R^3\), with intensity exactly \(\lambda_0\), finite local exponential moments and absolutely continuous factorial moment measures, for which the full normalized product densities obey the three exact reciprocal identities almost everywhere on the entire governing domains. The pair law includes arbitrarily small positive separations; there is no positive lower pair cutoff.

The theorem does **not** establish existence for an arbitrary prescribed positive intensity. Every \(\lambda_0>\lambda_*(M,h_4)\) remains unresolved by this submission. Proposition 2 is a valid obstruction only for stationary Poisson cluster processes whose cluster size is bounded almost surely by one fixed integer \(L\). It is not an obstruction for cluster bounds allowed to grow with the prescribed intensity, unbounded clusters, non-Poisson parent processes or general point processes.

Thus the correctness judgement is:

- the restricted exact existence theorem is established by the checked argument;
- the bounded-cluster obstruction is established with its stated scope;
- the governing arbitrary-intensity target remains unresolved;
- the source support is adequate for the structural background actually invoked, while the construction itself is proved directly in the submission;
- there is no computational or empirical component to promote or qualify.

The presentation is also satisfactory. The scope restriction appears at the start, in the theorem discussion, in the reasoning summary and in the limitations. The new symmetry/re-rooting lemma makes the formerly implicit combinatorial normalisation auditable.

## Reconstruction of the argument

The construction uses three independent stationary Poisson parent processes producing clusters of exactly two, three and four points, together with an independent singleton Poisson process. The target full densities are first inverted into same-parent kernels \(q_2,q_3,q_4\): equations (14)--(16) subtract every lower set-partition contribution from the desired reciprocal density. The kernels are supported on the pair, enlarged triangle and governing tetrahedron domains, respectively.

The amplitude choice

\[
a_2=\lambda/I,\qquad a_3=a_2/(4B),\qquad a_4=a_2/(16BK)
\]

turns pointwise nonnegativity into the three explicit error bounds \(E_2,E_3,E_4\le 1/2\). The geometric inequalities in (17), with the six edge terms, three disjoint-edge pairings and four face terms, give

\[
\tfrac12 a_jK_j\le q_j\le a_jK_j,
\qquad j=2,3,4.
\]

The marginal estimates then perform a second triangular inversion. The pair singularity is harmless because

\[
\int_{0<|y|\le M}|y|^{-1}\,dy=2\pi M^2.
\]

For triangles, cylindrical coordinates give \(\mathcal M K_3\le BK_2\). For tetrahedra, the fourth-vertex altitude cutoff gives \(\mathcal M K_4\le KK_3\). The enlargement of the auxiliary triangle support to altitude at least \(\min(h_3,h_4)\) is enough because every face altitude of a governing tetrahedron is at least its corresponding vertex-to-opposite-plane distance, hence at least \(h_4\). Therefore

\[
F_4=q_4,
\qquad F_3=q_3-\mathcal Mq_4,
\qquad F_2=q_2-\mathcal Mq_3+\tfrac12\mathcal M^2q_4
\]

are genuine nonnegative, integrable exact-size cluster kernels.

A type-\(j\) parent has rate \(Z_j/j!\), where \(Z_j\) is the anchored mass of \(F_j\). The new Lemma 3 proves that \(q_j\) and \(F_j\) are translation invariant and fully permutation symmetric, and that changing the anchored daughter has absolute Jacobian one. Consequently, an observed ordered \(r\)-tuple has \((j)_r=j!/(j-r)!\) injective assignments to the labelled daughters. Multiplying this count by the full labelled-configuration density \(F_j/j!\) yields

\[
b_r^{(j)}=\frac{1}{(j-r)!}\mathcal M^{j-r}F_j.
\]

The second inversion therefore makes the aggregate same-parent densities exactly \(q_2,q_3,q_4\). Adding the singleton rate in (28) makes the total first-order density exactly \(\lambda\). The independent-parent partition formula then gives all 2, 5 and 15 set-partition terms at orders two, three and four. Substitution of the definitions of \(q_j\) cancels the lower partitions and leaves \(a_2/D\), \(a_3/A\) and \(a_4/V\) on the required supports.

Finally, the pair component of any bounded-size Poisson cluster model is nonnegative. The target pair law forces \(C_2\ge M\) and hence an anchored same-parent pair mass at least \((2\pi/3)\lambda^2M^3\). Since a cluster with \(N\le L\) satisfies \((N)_2\le(L-1)N\), the same mass is at most \((L-1)\lambda\). This proves

\[
\lambda\le \frac{3(L-1)}{2\pi M^3}.
\]

## Review reasoning summary

The following checks determined the verdict.

1. **Scope and quantifiers.** I compared the claim-status paragraph, Theorem 1, the post-theorem scope statement, Proposition 2 and the final limitations with the governing quantifiers. Each now distinguishes the certified interval from arbitrary prescribed intensity. No sentence upgrades the restricted construction or the bounded-cluster proposition into a general solution or obstruction.
2. **Endpoint feasibility.** The feasible set is the intersection, in \([0,\infty)\), of three closed sublevel sets of continuous increasing functions. It contains a positive neighbourhood of zero and is bounded because \(E_2(t)\to\infty\). Monotonicity makes it an initial interval, so it is exactly \([0,\lambda_*]\) and the supremum is attained. Rechecking the downstream inequalities at equality shows that non-strict feasibility is enough: (18) retains the factor \(1/2\), while (23)--(24) retain the factor \(1/4\). Thus the endpoint produces genuine nonnegative cluster densities and is not merely a limiting value.
3. **Permutation and re-rooting.** I re-derived the symmetry induction from (14)--(16) and (22). The one-coordinate re-rooting map is an invertible integer linear map with inverse given by the opposite re-rooting, so its determinant is \(\pm1\); applying it to three coordinates preserves absolute Jacobian one. For an ordered \(r\)-tuple there are exactly \((j)_r\) injective daughter assignments, and the parent-rate/mark-density product is \(F_j/j!\). The resulting coefficient is exactly \(1/(j-r)!\), with no missing factor \(j\), \(r!\) or \(j!\).
4. **Intensity bookkeeping.** Integrating the second inversion gives \(Z_4=Q_4\), \(Z_3=Q_3-Q_4\) and \(Z_2=Q_2-Q_3+Q_4/2\). Hence the non-singleton intensity is \(Q_2-Q_3/2+Q_4/6\). The singleton rate in (28), together with \(Q_2=\lambda-\lambda^2J\), raises this to exactly \(\lambda\). The endpoint argument does not alter this calculation.
5. **Full rather than connected densities.** Equations (31)--(33) contain every set partition: 2 terms at order two, 5 at order three and 15 at order four. The recursive definitions cancel those full lower-partition terms on the deletion-nested supports. The proof never identifies a same-parent kernel with a full product density.
6. **Domains and singularities.** The pair identity is proved on all \(0<D\le M\), and the only new singular anchored integral is finite in three dimensions. The triangle support contains \(\mathcal D_3\); every face required in the tetrahedral cancellation lies in that support. No formula outside the governing finite domains is used to infer the final identities.
7. **Process properties.** Bounded cluster size and offsets imply local finiteness and finite local exponential moments. Absolute continuity of the mark laws makes within-cluster collisions null; diffuse independent parents and marks exclude cross-cluster collisions. The block-density partition formula gives absolute continuity at every finite order.
8. **Obstruction scope.** The proof of Proposition 2 uses only nonnegativity of the same-parent pair density and \((N)_2\le(L-1)N\). The latter depends essentially on the fixed almost-sure bound \(N\le L\), so the revised exclusions are mathematically necessary and correctly stated.

These checks are an auditable summary of the decisive mathematical tests, not a claim of machine formalisation.

## Decision record

| Decision | Evidence | Result |
|---|---|---|
| Accept the repaired scope statement | Claim status; Theorem 1 and its following paragraph; Proposition 2 final paragraph; `Checks and limitations` | Accepted as a restricted theorem and scoped obstruction only. |
| Include \(\lambda_*=\max\Lambda\) | Equations (6)--(7a); closedness, interval property, positive neighbourhood and boundedness; downstream non-strict positivity checks | Accepted; endpoint attainment and endpoint construction are valid. |
| Accept the ordered-daughter normalisation | Lemma 3; equation (29); explicit \((j)_r\) assignment count against \(Z_j/j!\) | Accepted; coefficient \(1/(j-r)!\) is correct. |
| Preserve the unchanged exact-density conclusion | Equations (14)--(24), (26)--(36); support nesting and complete partitions | Accepted on the certified intensity interval and stated nonvacuous geometry regime. |
| Require another repair round | No assigned issue remains and no new material defect was found | **No.** |

## Criterion-by-criterion assessment

| Criterion | Evidence/location | Assessment |
|---|---|---|
| Correct target and quantifiers | Opening claim status; Theorem 1; Proposition 2; final limitations | Correctly states partial success. Exact existence is proved only for \(0<\lambda_0\le\lambda_*\); arbitrary intensity remains open. |
| Whole-space existence and stationarity | `Process and existence`, especially section 4 | Established by homogeneous Poisson parent processes and compactly supported cluster offsets on all of \(\mathbb R^3\). Isotropy is also established. |
| Simplicity, local finiteness, prescribed intensity | Section 4, equations (26)--(28) | Established. The explicit singleton stream closes the intensity calculation at the input \(\lambda_0\); collision and local-finiteness arguments are adequate. |
| Local fourth moments and density existence | Section 4 and paragraph after (33) | More than required is proved: finite local exponential moments and absolutely continuous factorial measures at all finite orders. |
| Full density hierarchy and combinatorial factors | Lemma 3; equations (29)--(33) | Established. The re-rooting Jacobian and \((j)_r\) count are now explicit, and the 2/5/15 full partition formulas are complete. |
| Exact identities on the entire domains | Equations (34)--(36), with (2), (19)--(21) | Established almost everywhere on \(\mathcal D_2,\mathcal D_3,\mathcal D_4\) for the certified intensity interval. No positive pair cutoff remains. |
| One jointly feasible parameter choice | Equations (5)--(7a), (18), (23)--(24) | Established for each prescribed \(\lambda_0\) in the closed certified interval. The bounds are sufficient certificates, not a claim that \(\lambda_*\) is the true realizability threshold. |
| Source support and prior-work comparison | `Relation to prior work`; frozen shared dossier and references | Adequate for the structural partition and stationary-cluster background. The new construction and obstruction are proved directly. The literature packet does not establish the missing arbitrary-intensity result. |

## Detailed findings

### A1-v01-F1 — governing scope

- **Severity in assigned packet:** unresolved governing scope.
- **Location checked:** opening claim-status paragraph; Theorem 1 and the paragraph immediately after (9); reasoning-summary items 4--6; `Checks and limitations`; response item 1.
- **Mathematical check:** the existence quantifier is uniformly restricted to \(0<\lambda_0\le\lambda_*(M,h_4)\). The text explicitly leaves every larger prescribed intensity open and does not infer a general obstruction from failure of the present four-point clusters.
- **Consequence:** the submission no longer overstates its relation to the governing problem.
- **Status:** **closed**.

### A1-v01-F2 — obstruction scope

- **Severity in assigned packet:** scope defect.
- **Location checked:** Proposition 2 hypothesis and conclusion; proof equations (37)--(39); proposition closing paragraph; final limitations; response item 2.
- **Mathematical check:** the upper bound follows from \((N)_2\le(L-1)N\), which is valid under the stated fixed almost-sure bound \(N\le L\). The submission now confines every consequence to that class and expressly excludes growing bounds, unbounded clusters, non-Poisson parents and general point processes.
- **Consequence:** the obstruction is correct and no longer generalised beyond its proof.
- **Status:** **closed**.

### A1-v01-F3 — endpoint inclusion

- **Severity in assigned packet:** missing endpoint argument.
- **Location checked:** equations (6)--(7a); Theorem 1 endpoint; positivity equations (18), (23)--(24); response item 3.
- **Mathematical check:** continuity yields closedness; monotonicity yields the interval property; continuity at zero yields a nontrivial feasible interval; divergence of \(E_2\) yields boundedness. Compactness therefore gives a maximum. The construction uses weak inequalities throughout, so feasibility and positivity persist at that maximum.
- **Consequence:** the theorem may legitimately use \(\lambda_0\le\lambda_*\), rather than only \(\lambda_0<\lambda_*\).
- **Status:** **closed**.

### A1-v01-F4 — re-rooting and permutation count

- **Severity in assigned packet:** missing combinatorial/Jacobian justification.
- **Location checked:** Lemma 3; process definition; equations (29)--(30); response item 4.
- **Mathematical check:** the kernels are fully symmetric and translation invariant. Re-rooting is unimodular. The labelled full-configuration intensity is \(F_j/j!\), and an ordered observed \(r\)-tuple has exactly \((j)_r\) injective assignments. Their product gives \(\mathcal M^{j-r}F_j/(j-r)!\).
- **Consequence:** the same-parent densities in (30) and hence the complete partition formulas have the advertised coefficients.
- **Status:** **closed**.

### New findings

No new correctness, scope, source or presentation finding requiring author action was found in v02.

## Coder/source verification

No coder request was necessary. No simulation, finite grid, floating-point calculation or computer algebra result is used in this verdict. The algebraic coefficients, marginal constants, intensity cancellation and endpoint logic were checked directly from the displayed formulas.

The frozen literature dossier and bibliography were consulted only for the structural source claims. The dossier records full-text checks of Clark--Houssineau Theorem 4.2/equation (21) and Last--Penrose Exercises 8.2 and 9.10--9.12. I did not independently reopen unlisted source PDFs or local manuscripts because the delta packet restricted the review context. This limitation does not leave the new theorem conditional on a source: the required order-four construction, combinatorial calculation and obstruction proof are presented self-containedly in v02.

## Revision history

This is the v02 delta review. The assigned repair register is now:

| Assigned issue | v02 disposition |
|---|---|
| A1-v01-F1 | Closed: restricted intensity interval and unresolved larger intensities are explicit throughout. |
| A1-v01-F2 | Closed: Proposition 2 is confined to one fixed almost-sure cluster-size bound. |
| A1-v01-F3 | Closed: the feasible set is proved compact and its positive endpoint is attained. |
| A1-v01-F4 | Closed: symmetry, unimodular re-rooting and the ordered-assignment coefficient are proved. |

No earlier submission or review was consulted. The original v01 report remains preserved outside this review's context and is not restated here.

## Remaining mathematical questions

1. Can the exact construction be extended to each prescribed \(\lambda_0>\lambda_*(M,h_4)\)? The present \(\lambda_*\) is a certified sufficient endpoint coming from conservative positivity bounds, not a proved sharp threshold.
2. Can exact residual kernels be realised with cluster sizes that grow with intensity, or with an unbounded but almost surely finite cluster size, while retaining finite fourth local moments and all full-density identities?
3. Is there a different process class that avoids the same-parent partner bound used in Proposition 2 and achieves arbitrary prescribed intensity on the fixed physical domains?
4. Can the sufficient positivity estimates be sharpened enough to enlarge the certified interval, and if so does any independent realizability inequality impose a genuine finite upper endpoint for a specified class?

These are exact continuum questions. Numerical or empirical agreement would not close them.
