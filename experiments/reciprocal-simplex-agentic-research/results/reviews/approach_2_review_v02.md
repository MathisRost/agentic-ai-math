# Critical review — approach 2, submission v02

- Run / reviewer model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Submission SHA-256: `0044e84da7c60a7bb4d8989724aa7001be0b1b7dd1759b08eb8f73c9e77aa49e`.
- Assigned issue-list SHA-256: `dcc993bfdafbe33d3611608298c6e036782c2396fa9b0f564b6d32ec48bccc5f`.
- Context received: the complete frozen delta-review packet `context_packets/review_2_v02.md` and every file listed there.
- Context excluded: submission v01, review v01, author work notes and conversation, all other tracks, and all later or live revisions of common files.
- Review type: fresh delta review of repair round 1.

## Verdict and exact scope

The revised submission **does not establish the governing exact target for general Cox processes**, and it now states that limitation correctly and repeatedly. The existence or non-existence of a stationary diffuse directing random measure having all three prescribed tensor-moment densities remains unresolved. In particular, the submission provides neither a process satisfying the full exact $g_2,g_3,g_4$ hierarchy nor a general obstruction covering every stationary simple point process or every Cox process.

Within that limitation, the checked argument establishes the following restricted results.

1. The Cox-process version of the target is equivalent to a random-measure moment problem with stationary, almost surely diffuse and locally finite directing measure, finite fourth local mass moments, and absolutely continuous tensor moments through order four. Scaling a witness's directing measure supplies any prescribed positive intensity without changing the normalised product densities or the physical domains.
2. The pair and triangle targets cannot hold simultaneously in the stated Poisson-centred, radius-only, uniformly weighted spherical-carrier Cox class, even with arbitrary nonnegative radial mixing satisfying the submission's hypotheses.
3. A stationary absolutely continuous directing field with finite pointwise second moment cannot have the required no-cutoff pair singularity. Ordinary finite-variance log-Gaussian Cox processes are consequently excluded; their higher product identity gives a separate triangle-shape obstruction.
4. Subject to the stated defining properties of the frozen finite dependent-cluster construction, its count law in one suitable positive-measure bounded window is not mixed Poisson, so that particular process is not Cox.
5. The pair target implies the necessary Cox condition $C_2\geq 5M/12$, but this is not contradictory because $C_2$ is free.

All five assigned repair issues are closed. No new correctness defect was found in the changed arguments, and **another author repair round is not needed**. This decision is approval of the restricted reductions and obstructions only; it must not be recorded as a solution of the reciprocal-simplex existence problem.

Presentation assessment: the revision is self-contained at the level required by the assigned packet, distinguishes full densities from one-carrier contributions, and keeps its negative results attached to their precise subclasses. The response-to-review section makes the delta auditable without relying on the unavailable earlier review.

## Reconstruction of the argument

The submission begins from the standard Cox identity

\[
\alpha_X^{(n)}=\mathbb E\Lambda^{\otimes n}.
\]

It proves both directions of the claimed reduction. Starting from a stationary diffuse directing measure with finite fourth local mass moments, conditional Poisson sampling gives a stationary, simple, locally finite process; the Touchard polynomial for a Poisson count transfers the fourth-moment bound, and Tonelli gives the factorial moment measures. Conversely, the Cox probability generating functional determines the directing law, so stationarity of the Cox process yields stationarity of that law. Vanishing of the second factorial measure on the diagonal forces the sum of squared directing atoms to vanish almost surely. Finally, the conditional fourth-moment identity

\[
\mathbb E[X(B)^4\mid\Lambda]
=\Lambda(B)^4+6\Lambda(B)^3+7\Lambda(B)^2+\Lambda(B)
\]

transfers a finite fourth count moment back to the directing measure. This closes the earlier one-way-versus-equivalence ambiguity.

For the spherical subclass, the directing measure is a Poisson sum of surface measures on spheres with radius density $p(r)$ and uniform radius-dependent weight $b(r)$. The repaired incidence lemma parametrises every sphere through an affinely independent $j$-tuple by

\[
c=c_0+z,\qquad r=(R_j^2+|z|^2)^{1/2},\qquad z\in E^\perp.
\]

The ratio of the vertex normal Jacobian to the sphere-parameter normal Jacobian, including the fibre parametrisation, is

\[
\frac{r^{j-1}}{(j-1)!\Delta_{j-1}}.
\]

The nonnegative area--coarea formula therefore produces an almost-everywhere density for each one-carrier tensor measure. The bounded carrier mass assumption gives local finiteness, and the special zero-dimensional fibre at $j=4$ is handled using one fixed Borel representative of $p b^4$.

The submission then retains all carrier partitions. At orders two, three and four the full moment densities contain respectively the $2$, $5$ and $15$ set-partition terms. This is essential: the same-sphere densities are cumulant-like building blocks, not the target densities themselves.

The sphere obstruction uses only orders two and three. The pair target forces

\[
q_2(ij)=\lambda^2\left(\frac{C_2}{d_{ij}}-1\right),
\]

and the full order-three partition formula then forces

\[
q_3(123)=\lambda^3\left(\frac{C_3}{A}+2-C_2\sum_{i<j}\frac1{d_{ij}}\right).
\]

But $Aq_3$ depends only on the circumradius in this spherical class. On a fixed-circumradius isosceles family, with $x=\sin(\theta/2)$, the allegedly shape-constant part becomes

\[
F(x)=8R^2x(1-x^2)^{3/2}-C_2R(1-x^2)(1+4x).
\]

If constant near the equilateral triangle, analyticity would make it constant on $(0,1)$, contradicting its two endpoint limits. The almost-everywhere premise is correctly converted to fixed-radius shape constancy using a nondegenerate local coordinate chart, Fubini, and continuity.

The explicit radial example following this obstruction shows that the pair equation alone is not the source of failure. Its piecewise nonnegative $f$ has exactly the required tail integral. The choices $b(r)=a/r$ and $p(r)=f(r)/a^2$ satisfy the class hypotheses, yield unit intensity, and give $m_2=C_2/D$ throughout $0<D\leq M$. Thus the obstruction genuinely enters when the full third-order identity is imposed.

The remaining propositions exclude two possible bridges. Finite pointwise second moment bounds $\mathbb E[Z(x)Z(y)]$ uniformly and is incompatible with the $1/D$ divergence on a positive-measure small-distance set. The particular finite-cluster witness has a bounded-jump compound-Poisson window count with a positive four-jump rate. If it were Cox, the transformed pgf would be a Laplace transform; analytic continuation would then make it agree for every positive transform parameter with an entire expression that diverges to infinity because of the positive quartic term. A Laplace transform of a nonnegative random variable cannot do so.

## Review reasoning summary

The following decisive checks were performed independently on the frozen v02 formulas.

1. **Cox converse.** I checked each recovered property separately: uniqueness of the directing law from the restricted Laplace functional; diagonal mass
   $M_2(\mathrm{diag}\cap B^2)=\mathbb E\sum_{x\in B}\Lambda\{x\}^2$; the exact fourth Touchard polynomial; and transfer of absolute continuity through $\alpha_X^{(n)}=M_n$. No converse condition is left asserted without a mechanism.
2. **Incidence constants.** For $j=2,3,4$, the fibre dimensions are $2,1,0$. Substituting these into the repaired coarea formula reproduces respectively
   \[
   \frac{2\pi}{D}\int_{D/2}^L p(r)b(r)^2r^2\,dr,
   \quad
   \frac1A\int_{R_3}^L\frac{p(r)b(r)^3r^3}{\sqrt{r^2-R_3^2}}\,dr,
   \quad
   \frac{p(R_4)b(R_4)^4R_4^3}{6V},
   \]
   with the last expression understood through the fixed Borel version. These checks confirm the factorial and polar factors in the general formula.
3. **Local finiteness and a.e. status.** The bound
   $Q_j(K^j)\leq |K^{+L}|\kappa^j\int_0^L p(r)\,dr$
   is sufficient for a locally integrable density. Equality of two almost-everywhere choices of $p b^4$ first gives the same measure and hence only an almost-everywhere equality of the resulting tuple-density versions, exactly as claimed.
4. **Full hierarchy.** Expanding the Poisson-carrier moments by labelled set partitions gives the displayed $2,5,15$ terms with no extra factorial. Substitution of the forced $q_2$ into the order-three expansion gives the constant $+2$ in equation (5.2); it is not a connected-density substitution.
5. **Shape obstruction.** I recomputed
   $A=4R^2x(1-x^2)^{3/2}$ and
   $A(1/a+1/b+1/c)=R(1-x^2)(1+4x)$
   for the fixed-$R$ isosceles family. The endpoint contradiction is valid for every $C_2>0$. Positive measure of the triangle domain gives the strict interval needed around equilateral configurations.
6. **Pair-only construction.** Integrating the two pieces of $f$ gives
   $2\pi\int_{D/2}^L f=C_2-D$ for all $0<D\leq M$. The repaired requirement $L>M/2$ removes the zero-denominator problem when the positive tail is present. The definitions of $a,b,p$ give $p b^2r^2=f$, intensity one, integrable $p$, and bounded carrier mass.
7. **Window argument.** Only one sufficiently large bounded positive-measure window is needed. Bounded offsets and positive type-four rate yield $0<\nu_4(B)<\infty$. The compound-Poisson pgf is entire, while a mixed-Poisson representation gives a holomorphic Laplace transform on the right half-plane. The identity theorem and the positive quartic leading term give the contradiction.
8. **Global scope.** None of these calculations constrains every diffuse directing measure, every irregular density field, dependent or non-spherical carriers, or the full fourth-order target. Section 8 correctly leaves densities on excluded low-altitude configurations free, so its moment-matrix discussion supplies necessary conditions only.

## Criterion-by-criterion assessment

| Criterion | Evidence/location | Assessment |
|---|---|---|
| Correct target and quantifiers | Claim and scope; Corollary 1; Sections 5--8; Checks and limitations | The governing target is stated correctly but remains unresolved. The submission's positive claims and exclusions have the right restricted quantifiers. |
| Whole-space existence and stationarity | Proposition 1; Section 2 | The Cox lifting and the spherical class are defined on all of $\mathbb R^3$ and stationarity is justified. No whole-space target witness is supplied. |
| Simplicity, local finiteness, prescribed intensity | Proposition 1; equations (2.1)--(2.3); Corollary 1 | Diffuseness gives simplicity, bounded local carrier counts and masses give local finiteness, and deterministic scaling gives arbitrary prescribed intensity if an exact Cox witness exists. This remains conditional because the witness is missing. |
| Local fourth moments and density existence | Proposition 1; Lemma 2 and (2.7) | Correct for the abstract Cox equivalence and for the spherical subclass. The repaired coarea argument establishes a.e. absolute continuity through order four. |
| Full density hierarchy and combinatorial factors | Equation (3.1) | All labelled set partitions through order four are present, with correct coefficients. The sphere obstruction uses the full $m_3$, not merely $q_3$. |
| Exact identities on the entire domains | Proposition 3; equations (5.6)--(5.8) | The pair-only example is exact on all $0<D\leq M$; the spherical subclass is exactly obstructed already at order three. No general simultaneous $g_2,g_3,g_4$ identities are obtained. |
| One jointly feasible parameter choice | Throughout; exact remaining gap | None is claimed or produced for the governing problem. This criterion remains unresolved. |
| Source support and prior-work comparison | Relation to prior work; References; frozen dossier and definition audit | Structural Cox and LGCP identities are supported by the frozen verified dossier. Prior manuscripts are treated as unpublished evidence and are not promoted to independent theorems. No empirical result is used. |

## Detailed findings

### R2-V02-01 — governing Cox existence remains unresolved

- **Severity:** scope limitation, not a defect in v02.
- **Location:** claim status and Claim and scope; Section 8; Exact remaining gap.
- **Mathematical reason:** the proved propositions cover an equivalence and particular subclasses. They do not quantify over all stationary diffuse random measures. The moment matrices in Section 8 are necessary only and cannot be evaluated completely from the target because third- and fourth-order densities are free on excluded low-altitude configurations.
- **Consequence:** v02 cannot be cited as constructing the requested process or proving general non-existence.
- **Required action:** none in another repair round. Preserve this scope exactly in synthesis.

### R2-V02-02 — no new defect in the repaired incidence lemma

- **Severity:** closed verification finding.
- **Location:** Lemma 2, equations (2.4)--(2.9), and equations (4.1)--(4.3).
- **Mathematical reason:** the normal-Jacobian ratio, orthogonal fibre dimension, local-finiteness bound, a.e. density interpretation and order-four version issue are all now explicit. Direct specialisation reproduces the known $j=2,3,4$ constants.
- **Consequence:** the absolute-continuity step used by the spherical partition expansion is justified under the stated class assumptions.
- **Required action:** none.

### R2-V02-03 — no new defect in the repaired Cox equivalence

- **Severity:** closed verification finding.
- **Location:** Proposition 1 and Corollary 1.
- **Mathematical reason:** the reverse implications for stationarity of the directing law, diffuseness, fourth local mass moments and tensor-moment densities are now supplied. Scaling acts homogeneously on every tensor moment and does not rescale space.
- **Consequence:** “equivalent” is now justified for the Cox subclass, while existence of a suitable directing measure remains an explicit separate obligation.
- **Required action:** none.

### R2-V02-04 — no new defect in the repaired pair-only radial example

- **Severity:** closed verification finding.
- **Location:** equations (5.6)--(5.8).
- **Mathematical reason:** the positive tail is given an explicit constant density, $L>M/2$ is stated where its denominator is used, and the zero-tail case is harmless. The resulting $p$ and $b$ satisfy the class hypotheses and the exact integral identity.
- **Consequence:** the example correctly prevents an overbroad claim that finite-radius curvature alone obstructs exact pair matching.
- **Required action:** none.

### R2-V02-05 — no new defect in the repaired finite-cluster window test

- **Severity:** closed verification finding.
- **Location:** Proposition 5.
- **Mathematical reason:** non-Coxness is deduced from one expressly chosen positive-measure bounded window with positive four-daughter contribution. No universal assertion about null or arbitrary bounded windows is needed.
- **Consequence:** the conclusion remains limited to the particular finite-cluster law and does not exclude another Cox process with the same restricted correlations.
- **Required action:** none.

## Coder/source verification

No coding request was needed. Every decisive repair can be checked symbolically from the displayed formulas, and no numerical or simulation evidence is used.

The review used the frozen source dossier, bibliography, open-question register, prior-work index, paper index and definition audit supplied in the packet. I did not browse or reopen excluded author material or another track. The standard Cox and log-Gaussian identities are supported at the cited primary-source locations recorded in the dossier. The coarea constants and the finite-cluster count-law implication were checked from the submission's reproduced arguments. This review does not add a new literature non-discovery claim beyond the bounded frozen dossier.

## Revision history

| Assigned issue | Delta-review result | Status |
|---|---|---|
| R2-V01-01 — unresolved governing scope | v02 consistently labels the general Cox problem unresolved and confines its theorems to reductions and subclasses. | Closed; preserve as a standing scope limitation. |
| R2-V01-03 — incidence/absolute continuity | Lemma 2 supplies measurable weights, orthogonal fibres, the full Jacobian, local finiteness, a.e. interpretation and the $p b^4$ version convention. | Closed. |
| R2-V01-04 — equivalence wording | Proposition 1 now proves the reverse direction and Corollary 1 separately handles intensity scaling. | Closed. |
| R2-V01-05 — pair-only repair choices | Equations (5.7)--(5.8) state $L>M/2$ where needed and give an explicit nonnegative integrable tail. | Closed. |
| R2-V01-08 — window qualification | Proposition 5 uses one sufficiently large bounded positive-measure Borel window and disclaims a universal window assertion. | Closed. |
| Validated subclass scopes | Sphere mixtures, finite-pointwise-second-moment fields/LGCPs, and the one frozen finite-cluster law remain distinct. | Preserved. |

**Decision record:** accept v02 as a correct restricted Cox analysis with all assigned repairs closed. Do not request another repair round. Carry forward one unresolved headline obligation: construction or general obstruction for a stationary diffuse directing random measure with the exact full second-, third- and fourth-order tensor-moment densities on the frozen domains.

## Remaining mathematical questions

1. Does any stationary diffuse locally finite random measure, outside the excluded subclasses, have the exact three tensor-moment densities with finite fourth local mass moments?
2. Can dependent, nonuniform or non-spherical carriers create the missing shape dependence while retaining nonnegativity of the directing measure and all full partition terms?
3. Can mixed test-function moment positivity use only configurations inside the prescribed altitude-truncated domains to obtain an obstruction stronger than $C_2\geq5M/12$?
4. Can the cancellation mechanism of the exact finite-cluster construction be embedded in a genuinely Cox law other than by identifying that particular non-Cox process with a Cox process?

Empirical fits and simulations remain separate from all four questions and cannot close the exact existence gap.
