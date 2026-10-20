# Critical review — approach 4, submission v02

- Run / reviewer model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Submission SHA-256: `bdf6d669774a3155ac46a7ded6b978bd9246a7e074be45558c4be167b6848c2c`.
- Assigned issue-list SHA-256: `07cf35a4ed909095e29d216f29689fb348df52401965cb862594bc994ecb3f3e`.
- Context received: the frozen reviewer instructions and templates, frozen common problem and source indexes, the frozen shared-literature dossier, bibliography and open questions, submission v02, and the author-facing v01 issue list named in `context_packets/review_4_v02.md`. All packet hashes were checked and matched.
- Context excluded: submission v01, review v01, author work notes or conversations, other approaches' submissions or reviews, and coordinator or owner conversation history.
- Review type: fresh delta review of repair round 1. The repairs were checked against the assigned issue list, and the revised mathematical inferences were re-established from submission v02 and the frozen common sources.

## Verdict and exact scope

**The revised submission establishes its restricted theorem, but it does not establish the governing arbitrary-prescribed-intensity target.** More precisely, for every fixed admissible $(M,h_3,h_4)$ with positive-measure triangle and tetrahedron domains, the argument constructs the required stationary, isotropic, simple point process at every prescribed intensity

\[
0<\lambda_0\leq \lambda_*(M,h_4),
\]

where the displayed $\lambda_*$ is strictly positive. The process has intensity exactly $\lambda_0$, finite local exponential moments, and absolutely continuous factorial moment measures through order four. Its **full** product densities satisfy the three reciprocal identities almost everywhere on the complete governing domains, including every pair separation $0<D\leq M$.

The proof does not cover $\lambda_0>\lambda_*(M,h_4)$. This is stated consistently in the claim, conclusion, reasoning summary, limitations and response to review. Existence or non-existence for arbitrary prescribed positive intensity therefore remains unresolved.

The separate estimate

\[
\lambda_0M^3\leq \frac{3(K-1)}{2\pi}
\]

is a valid obstruction only for the stated class of standard Poisson-cluster constructions with one fixed almost-sure cluster-size bound $K$. It is not a general non-existence result and does not exclude Cox processes, unbounded clusters, intensity-dependent size bounds, Gibbs processes or other point processes.

All four issues in `issues_v01_for_author.md` are closed. I found no new defect requiring a further scoped repair round. The unresolved arbitrary-intensity question is a limitation of the theorem, not an unacknowledged repair defect in v02.

## Reconstruction of the argument

### Supports and singular kernels

The construction sets $\rho=\lambda_0$, $h=\min\{h_3,h_4\}$ and $H=h_4$. It uses the pair support $S_2=\mathcal D_2$, an auxiliary triangle support $S_3$ with minimum altitude $h$, and the target tetrahedron support $S_4=\mathcal D_4$. The enlargement of the triangle support is necessary when $h_4<h_3$: each face of a tetrahedron in $S_4$ has face altitude at least the corresponding distance to an opposite tetrahedral face plane, hence at least $h_4\geq h$. Therefore every face of an $S_4$ tetrahedron lies in $S_3$.

The geometric kernels are

\[
K_2=\frac{\mathbf 1_{S_2}}D,\qquad
K_3=\frac{\mathbf 1_{S_3}}A,\qquad
K_4=\frac{\mathbf 1_{S_4}}V.
\]

The absence of a lower pair cutoff causes no local-integrability problem in three dimensions:

\[
\int_{|y|\leq M}\frac{dy}{|y|}=4\pi\int_0^M r\,dr=2\pi M^2=:I.
\]

For the last-coordinate marginal operator $\mathcal M$, the submission proves

\[
\mathcal M K_3\leq BK_2,
\qquad
\mathcal M K_4\leq JK_3,
\]

with $B=2\pi^2M^2$ and

\[
J=6\pi\left[M^2\log(M/H)-\frac{M^2-H^2}{2}\right]>0.
\]

The first bound follows by cylindrical integration around a fixed edge. The second follows by slicing the fourth vertex by signed height $u$ above a fixed triangle plane, using $H\leq |u|\leq M$, $V=A|u|/3$, and cross-sectional area at most $\pi(M^2-u^2)$. These bounds are on the actual enlarged supports and are sufficient for all later marginal inversions.

### Residual kernels and positivity

The amplitudes

\[
a_2=\frac{\rho}{I},\qquad
a_3=\frac{a_2}{4B},\qquad
a_4=\frac{a_2}{16BJ}
\]

are inserted into recursively defined same-parent kernels $q_2,q_3,q_4$. Each $q_r$ is the target full density on $S_r$ minus all lower set-partition contributions. In particular, $q_4$ subtracts the all-singleton term, all six pair-plus-two-singleton terms, all three pair-pair terms, and all four triple-plus-singleton terms.

The dimensionless subtraction bounds $E_2,E_3,E_4$ are correctly obtained from the geometric inequalities

\[
A\leq \frac{M^2}{2},\quad \frac{A}{D_{ij}}\leq\frac M2,
\]

and

\[
V\leq\frac{M^3}{6},\quad
\frac{V}{D_{ij}}\leq\frac{M^2}{6},\quad
\frac{V}{D_{ij}D_{k\ell}}\leq\frac M6,
\quad
\frac{V}{A_{ijk}}\leq\frac M3.
\]

The seven entries in the displayed definition of $\lambda_*$ make the one term of $E_2$ at most $1/2$, the two terms of $E_3$ at most $1/4$ each, and the four terms of $E_4$ at most $1/8$ each. Hence, for $0<\rho\leq\lambda_*$,

\[
\frac12a_rK_r\leq q_r\leq a_rK_r,
\qquad r=2,3,4.
\]

The units of every threshold entry are $\mathrm{length}^{-3}$, as required for an intensity.

The exact-size cluster kernels are then obtained by the triangular marginal inversion

\[
F_4=q_4,\qquad
F_3=q_3-\mathcal Mq_4,\qquad
F_2=q_2-\mathcal Mq_3+\frac12\mathcal M^2q_4.
\]

The preceding lower bounds and marginal estimates give

\[
F_4\geq\tfrac12a_4K_4,
\quad
F_3\geq\left(\tfrac12a_3-a_4J\right)K_3
=\tfrac14a_3K_3,
\]

and, after discarding the nonnegative last term in $F_2$,

\[
F_2\geq\left(\tfrac12a_2-a_3B\right)K_2
=\tfrac14a_2K_2.
\]

Thus the $F_r$ are genuine nonnegative, integrable, nonzero anchored densities. This is the decisive existence step for the dependent cluster marks.

### Reanchoring and the process law

For each $r$, changing the distinguished daughter from point $1$ to point $i$ sends the relative-coordinate blocks to

\[
(-y_i,(y_k-y_i)_{k\ne1,i}),
\]

up to a permutation. The scalar block matrix is invertible with determinant $\pm1$; tensoring it with the $3\times3$ identity leaves absolute determinant one. Since $F_r$ is translation invariant and fully symmetric, the anchored integral and unlabelled cluster law do not depend on the chosen daughter. This closes the earlier missing Jacobian and preferred-anchor justification.

Type-$r$ parents form independent homogeneous Poisson processes of rates $Z_r/r!$, where $Z_r$ is the anchored mass of $F_r$. A parent emits an $r$-point cluster with relative density $F_r(0,\cdot)/Z_r$. The construction also adds an independent singleton Poisson process of rate

\[
\lambda_1=\rho^2L+\frac{Z_3}{2}+\frac{Z_4}{3}>0,
\qquad L=\frac{4\pi}{3}M^3.
\]

The integrated inversion relations are

\[
Z_4=Q_4,\qquad
Z_3=Q_3-Q_4,\qquad
Z_2=Q_2-Q_3+\frac12Q_4.
\]

Consequently the nonsingleton point intensity is $Q_2-Q_3/2+Q_4/6$, while the singleton term contributes $\rho^2L+Q_3/2-Q_4/6$. Since

\[
Q_2=a_2I-\rho^2L=\rho-\rho^2L,
\]

the total intensity is exactly $\rho$.

Clusters have at most four points and all offsets are bounded by $M$. A bounded observation window is therefore affected by only finitely many parents, and its point count is dominated by a finite-jump compound Poisson variable plus the singleton count. This gives local finiteness and finite local exponential moments. The relative marks have Lebesgue densities supported away from within-cluster coincidences; diffuse independent parents prevent inter-cluster collisions. Hence the process is simple. Translation and orthogonal invariance of the parent laws and geometric mark kernels give stationarity and isotropy.

### Full product densities

A type-$j$ cluster has full labelled daughter density $F_j/j!$. For an ordered observed $r$-tuple there are $j!/(j-r)!$ injections into the daughter labels. Unit-Jacobian reanchoring and full symmetry make every injection contribute the same marginal. The total type-$j$ same-parent density is therefore

\[
\frac{1}{(j-r)!}\mathcal M^{j-r}F_j.
\]

This yields $b_2=q_2$, $b_3=q_3$, $b_4=q_4$. Partitioning an ordered observed tuple by parent then gives the complete moment-cumulant identities with respectively $2$, $5$ and $15$ set partitions. Substitution of the residual definitions produces

\[
\rho^{(2)}=\frac{a_2}{D}\quad\hbox{on }S_2,
\qquad
\rho^{(3)}=\frac{a_3}{A}\quad\hbox{on }S_3,
\qquad
\rho^{(4)}=\frac{a_4}{V}\quad\hbox{on }S_4.
\]

Because $S_2=\mathcal D_2$, $\mathcal D_3\subseteq S_3$, and $S_4=\mathcal D_4$, these identities cover every required configuration almost everywhere. Dividing by $\rho^r$ gives positive configuration-independent constants $C_2,C_3,C_4$. No connected density is substituted for a full density.

### Bounded-cluster obstruction

For a standard independently marked homogeneous Poisson-parent process, after discarding empty clusters and merging multiple parent types of finite total rate into a type mark, define the reduced same-parent ordered pair measure

\[
\nu_2(B)=\gamma\,\mathbb E\sum_{u,v\in C}^{\ne}
\mathbf1\{v-u\in B\}.
\]

If $1\leq N\leq K$ almost surely, its total mass satisfies

\[
Q_2=\gamma\mathbb E[N(N-1)]
\leq (K-1)\gamma\mathbb EN
\leq (K-1)\rho,
\]

where a separate singleton intensity is allowed in the last inequality. No global density for $\nu_2$ is assumed.

On the punctured target ball, the exact full pair law and the distinct-parent Poisson baseline imply

\[
\nu_2(du)=\rho^2\left(\frac{C_2}{|u|}-1\right)du.
\]

Nonnegativity of $\nu_2$ forces $C_2\geq M$. Integrating only over that ball then gives

\[
Q_2\geq\frac{2\pi}{3}\rho^2M^3.
\]

Combining the two mass bounds proves the advertised class-specific obstruction. The revised formulation no longer infers a global density from a possibly singular cluster law.

## Review reasoning summary

The verdict rests on the following auditable checks.

1. **Quantifier check.** The submission consistently quantifies over every prescribed $\lambda_0$ only in the interval $(0,\lambda_*]$. It never promotes this to all positive intensities. The geometric domains match the frozen target, and the auxiliary enlargement of $S_3$ does not shrink a required domain.
2. **Zero-cutoff check.** Direct radial integration gives finite anchored mass for $1/D$ at the origin. The $K_3$ and $K_4$ marginal estimates remain finite and dominate the marginal inversion with no positive pair cutoff.
3. **Positivity check.** Each coefficient in $E_2,E_3,E_4$ was recomputed from the stated geometric bounds and partition counts. The displayed $\lambda_*$ makes every residual kernel and every exact-size kernel nonnegative.
4. **Intensity check.** The relations among $Z_r$ and $Q_r$, the parent rates $Z_r/r!$, and the singleton correction were recombined. All $Q_3,Q_4$ terms cancel and the remaining intensity equals $\lambda_0$ exactly.
5. **Anchor and assignment check.** The reanchoring map is an invertible integer block map of absolute determinant one. Symmetry and translation invariance then justify equality of injection contributions, giving the coefficient $1/(j-r)!$ rather than an assumed combinatorial factor.
6. **Full-density check.** All set partitions at orders two through four are present. The recursively defined $q_r$ cancel precisely the lower partitions on the nested supports.
7. **Process-property check.** Bounded cluster size and range imply finite local exponential moments; diffuse parent positions and absolutely continuous nondegenerate relative marks imply simplicity and factorial-density absolute continuity.
8. **Obstruction check.** The global argument uses only the total mass of a finite reduced same-parent pair measure. Absolute continuity is introduced only on the target ball, where it follows from the assumed full pair identity after subtracting the Poisson baseline.
9. **Source and provenance check.** The frozen literature dossier supports the general Poisson-cluster partition calculus and identifies the local finite-cluster manuscript as exact only on its earlier restricted domain. V02 accurately labels its small-intensity statement as a reformulation and zero-cutoff re-derivation within that unpublished framework, not as an independent literature theorem or a new arbitrary-intensity mechanism.

## Criterion-by-criterion assessment

| Criterion | Evidence/location | Assessment |
|---|---|---|
| Correct target and quantifiers | `Claim and scope`; restricted-theorem conclusion; limitations; response item 1 | **Partial relative to the governing target, correct for the stated theorem.** Exact identities are proved for every prescribed $0<\lambda_0\leq\lambda_*$; arbitrary positive intensity remains unresolved. |
| Whole-space existence and stationarity | `Reanchoring and the whole-space process` | **Established.** Homogeneous Poisson parents on $\mathbb R^3$ with translated finite marks define the process on the whole space; translation invariance is explicit. |
| Simplicity, local finiteness, prescribed intensity | Process section, equations (16)--(18) | **Established on the restricted intensity interval.** The intensity cancellation was checked; simplicity and bounded-range compound-Poisson control are justified. |
| Local fourth moments and density existence | Process section following (18) | **Established.** Local exponential moments are stronger than required. Same-parent marginals and finite parent partitions give absolute continuity through order four. |
| Full density hierarchy and combinatorial factors | Reanchoring (14)--(15), assignment formula (19), partition formulas (20)--(22) | **Established.** The factors $1/(j-r)!$ are justified and all $2,5,15$ set partitions are included. |
| Exact identities on the entire domains | Support nesting; substitutions after (20)--(22) | **Established on the governing geometric domains.** The pair identity includes all $0<D\leq M$; the triangle and tetrahedron identities cover the full altitude-restricted domains almost everywhere. |
| One jointly feasible parameter choice | Equations (2)--(5), (11)--(13), (16) | **Established for each $0<\lambda_0\leq\lambda_*$.** The same amplitudes, cluster kernels and singleton rate work simultaneously at orders two through four. |
| Source support and prior-work comparison | `Relation to prior work`; frozen dossier sections 2 and 6 | **Adequate and properly limited.** The construction is self-contained; the unpublished finite-cluster framework is credited, and approximate Cox work is not presented as exact evidence. |

## Detailed findings

### A4-V01-01 — closed: governing scope is now explicit

- **Previous severity:** major, because the governing theorem requires every prescribed positive intensity.
- **Location checked:** claim status and `Claim and scope`; restricted-theorem conclusion; reasoning-summary items 4 and 7; `Checks and limitations`; response item 1.
- **Assessment:** closed.
- **Reason:** every headline statement now restricts the positive result to $0<\lambda_0\leq\lambda_*(M,h_4)$. The arbitrary-intensity question is expressly left unresolved. The bounded-cluster obstruction is not used to convert the restricted theorem into general non-existence.
- **Consequence:** readers can distinguish a valid exact small-intensity theorem from the unmet governing quantifier.
- **Further repair:** none.

### A4-V01-02 — closed: the obstruction is formulated in measure form

- **Previous severity:** major, because a singular within-cluster displacement law need not have a global density.
- **Location checked:** equations (24)--(27) and surrounding reductions; response item 2.
- **Assessment:** closed.
- **Reason:** the proof defines the finite reduced same-parent ordered pair measure and bounds its total mass without assuming absolute continuity. It states the independently marked homogeneous Poisson-parent convention, removes empty clusters, explains the combination of multiple parent types, and permits an independent singleton component. A density is used only on $B_M^\times$, where the exact full pair law minus the diffuse distinct-parent baseline forces the restriction of $\nu_2$ to have that density.
- **Consequence:** the bound $\lambda_0M^3\leq3(K-1)/(2\pi)$ is valid for the advertised class.
- **Further repair:** none.

### A4-V01-03 — closed: provenance is accurately qualified

- **Previous severity:** moderate, because the earlier wording overstated what was conceptually new.
- **Location checked:** `Relation to prior work`, especially item 3; reasoning-summary item 4; response item 3.
- **Assessment:** closed.
- **Reason:** v02 uses “changes and explicit reformulations” and says directly that the small prescribed-intensity interval was already implicit in the prior polynomial-in-$a_2$ theorem after expressing amplitude through intensity. It presents the current threshold as an explicit reformulation and re-derivation for zero-cutoff supports.
- **Consequence:** the contribution is described without an unsupported novelty claim.
- **Further repair:** none.

### A4-V01-04 — closed: reanchoring precedes and justifies assignment counting

- **Previous severity:** major, because the cluster law and exact combinatorial coefficient require anchor independence and the correct Jacobian.
- **Location checked:** equations (14)--(15), the paragraph preceding the cluster definition, and the derivation of (19); response item 4.
- **Assessment:** closed.
- **Reason:** the submission exhibits the relative-coordinate reanchoring map, proves absolute determinant one and invertibility, and invokes both translation invariance and full symmetry of $F_r$. Only after this does it count the $j!/(j-r)!$ injections and derive $\mathcal M^{j-r}F_j/(j-r)!$.
- **Consequence:** the parent rates, same-parent marginals, intensity calculation and full partition formulas use the correct coefficients.
- **Further repair:** none.

### New findings

No new correctness, source or presentation defect was found that changes the restricted theorem or warrants another author repair round. The remaining arbitrary-intensity gap is already stated accurately and should remain open unless a genuinely different construction or a broader obstruction is supplied.

## Coder/source verification

No coding request was needed. The decisive calculations are short analytical bounds and exact combinatorial identities, and no numerical or symbolic output is used as proof.

The packet SHA-256 values were checked locally and all matched. Source support was limited to the supplied frozen common snapshot and shared dossier. The structural external claims used by the submission—Poisson-cluster construction and the set-partition form of factorial moments—are recorded in the dossier as checked against Last--Penrose and Clark--Houssineau. The restricted construction itself is proved in the submission and does not depend on an unquoted external existence theorem.

## Revision history

| Issue | v02 status | Review conclusion |
|---|---|---|
| A4-V01-01 | Restricted scope retained throughout | Closed |
| A4-V01-02 | Reduced-measure obstruction, with conventions and local density use | Closed |
| A4-V01-03 | Corrected provenance and reformulation language | Closed |
| A4-V01-04 | Unit-Jacobian reanchoring plus symmetry before assignment count | Closed |

Outstanding mathematical scope: the governing problem for $\lambda_0>\lambda_*(M,h_4)$ is unresolved. This is not a carry-over repair item because v02 makes no claim to solve it.

## Decision record

- **Exact governing target at every prescribed positive intensity:** not established; unresolved above the explicit threshold.
- **Restricted exact theorem for every prescribed $0<\lambda_0\leq\lambda_*$:** established by the checked argument.
- **Full rather than connected densities:** established; all parent partitions through order four are included.
- **No-lower-cutoff pair domain:** established; the $1/D$ singularity is locally integrable and is included for every positive distance up to $M$.
- **Bounded-cluster obstruction:** established only for the explicitly defined Poisson-cluster class with fixed finite $K$.
- **All assigned v01 issues closed:** yes.
- **New actionable issues:** none.
- **Another scoped repair round:** no. Further work would be new research on the arbitrary-intensity gap, not repair of this submission.

## Remaining mathematical questions

1. Can an exact construction cover $\lambda_0>\lambda_*(M,h_4)$ while retaining the same fixed physical domains and the full three-order hierarchy?
2. Can an exact Cox directing measure be found? Deterministic rescaling would then preserve $g_2,g_3,g_4$ and remove the intensity restriction, but the frozen sources contain no such witness.
3. Can Poisson clusters with unbounded size, or with a size cap allowed to grow with $\lambda_0M^3$, retain nonnegative inverse kernels and finite fourth local moments while realising the same exact identities?
4. Is there a broader realizability obstruction using only the values fixed on the finite target domains? The present reduced-measure estimate does not extend beyond the bounded-cluster class.

Empirical fit and numerical approximation are separate questions and do not affect this verdict.
