# Critical review — approach 5, submission v02

- Run / reviewer model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Submission SHA-256: `3aa480e3279781cc0f45a009d71326c447778b94f626a7d88402f278347d3ab9`.
- Author issue-list SHA-256: `354e74711e6fceba016e7858bdb675aec3db989f3c1ab10002525467726445be`.
- Context received: the frozen reviewer instructions and templates; the frozen common problem, indices and definition audit; the frozen shared literature dossier, bibliography and open questions; submission v02; and the author-facing v01 issue list.
- Context excluded: submission v01, review v01, all proof work notes and conversations, every other approach's submissions and reviews, and coordinator/owner conversation history.
- Review type: fresh delta review of repair round 1. The four assigned repairs were checked individually, and the mathematical argument on which the unchanged restricted theorem depends was re-established from v02 rather than inherited from an earlier verdict.

## Verdict and exact scope

**Verdict on the governing target:** unresolved. Submission v02 does not prove the required theorem for every prescribed intensity \(\lambda _0>0\), and it does not claim to do so. Existence and non-existence above its explicit sufficient threshold \(\lambda _*(M,h_3,h_4)\) remain open within the scope of this submission.

**Verdict on the restricted theorem:** the self-contained informal argument establishes the following exact partial result. Whenever the frozen triangle and tetrahedron domains have positive Lebesgue measure, there is an explicit \(\lambda _*>0\) such that, for every independently prescribed
\[
0<\lambda _0\leq \lambda _*,
\]
one stationary, isotropic, simple, locally finite finite-cluster process on \(\mathbb R^3\) has intensity exactly \(\lambda _0\), finite local moments through order four, absolutely continuous factorial moment measures through order four, and the three exact **full** product-density identities on all of \(\mathcal D_2,\mathcal D_3,\mathcal D_4\). In particular, the pair identity covers every \(0<D\leq M\); no positive lower pair cutoff remains. The constants \(C_2,C_3,C_4\) are positive outputs of the construction.

**Verdict on the general obstruction component:** equations (26)--(30) give correct necessary second-order inequalities for any target process. They include the diagonal count contribution and use only pair correlations at distances at most \(M\). Because \(C_2\) is a free output, these inequalities do not exclude any prescribed input tuple.

**Delta decision:** all four author-facing v01 issues are closed. I found no new mathematical or source-hygiene defect requiring another scoped repair round. The submission is ready to enter final synthesis as a restricted exact theorem, not as a solution of the arbitrary-prescribed-intensity target.

**Presentation assessment:** the theorem, its restriction, the construction and the remaining gap are stated clearly. The source distinctions and the separation between full densities and same-parent densities are unusually careful. No presentation problem affects mathematical recoverability.

## Reconstruction of the argument

The construction enlarges the internal triangle support just enough to make the fourth-order recursion closed under taking faces. It sets
\[
h=\min(h_3,h_4),\qquad H=h_4,
\]
uses the complete pair domain as \(S_2\), a triangle support \(S_3\) with minimum altitude at least \(h\), and \(S_4=\mathcal D_4\). Thus \(\mathcal D_3\subseteq S_3\). If a tetrahedron lies in \(S_4\), then for any one of its faces and any vertex of that face, the opposite edge line is contained in the tetrahedral opposite-face plane for that vertex. Distance to the edge line is therefore at least the corresponding tetrahedral altitude. Every face of a supported tetrahedron consequently belongs to \(S_3\). This is the support-nesting fact needed in the fourth-order subtraction.

The kernels
\[
K_2=\frac{\mathbf 1_{S_2}}D,\qquad
K_3=\frac{\mathbf 1_{S_3}}A,\qquad
K_4=\frac{\mathbf 1_{S_4}}V
\]
obey the anchored marginal bounds
\[
\mathcal M K_3\leq B K_2,qquad
\mathcal M K_4\leq G K_3,
\]
where \(B=2\pi^2M^2\) and
\[
G=6\pi\left[M^2\log(M/H)-\frac{M^2-H^2}{2}\right]>0.
\]
The endpoint \(D=0\) causes no divergence because
\[
\int_{0<|y|\leq M}|y|^{-1}\,dy=2\pi M^2=I.
\]
The first marginal bound follows by integrating \(2/(d r)\) in cylindrical coordinates around a fixed pair line. The second follows by writing \(V=A|u|/3\), using \(H\leq |u|\leq M\), and integrating the two circular cross-sections in a radius-\(M\) ball. These are upper bounds, so discarding the remaining altitude and diameter constraints is legitimate.

For a proposed intensity \(s\), v02 chooses
\[
a_2=\frac{s}{I},\qquad a_3=\frac{a_2}{4B},\qquad
a_4=\frac{a_2}{16BG},\qquad \rho=s.
\]
It then defines same-parent kernels \(q_2,q_3,q_4\) recursively by subtracting every lower-order set-partition term from the desired full density. The explicit functions \(E_2,E_3,E_4\) bound the subtracted part, after division by \(a_jK_j\). On the interval where all three are at most \(1/2\), one obtains
\[
\frac12a_jK_j\leq q_j\leq a_jK_j,qquad j=2,3,4.
\]
The exact-size cluster kernels are obtained by downward marginal inversion:
\[
F_4=q_4,qquad F_3=q_3-\mathcal Mq_4,qquad
F_2=q_2-\mathcal Mq_3+\frac12\mathcal M^2q_4.
\]
The marginal bounds and the choices \(a_4G=a_3/4\), \(a_3B=a_2/4\) give
\[
F_4\geq \tfrac12a_4K_4,qquad
F_3\geq \tfrac14a_3K_3,qquad
F_2\geq \tfrac14a_2K_2.
\]
Hence these are non-negative, finite, non-zero cluster densities. Their anchored normalisers \(Z_j\) define independent Poisson parent streams of rates \(Z_j/j!\), with one anchored daughter and \(j-1\) absolutely continuously distributed offsets. An additional singleton Poisson stream supplies the remaining first-order mass.

For a type-\(j\) cluster, the same-parent ordered \(r\)-tuple density is
\[
b_r^{(j)}=\frac{1}{(j-r)!}\mathcal M^{j-r}F_j.
\]
The factorial is correct: integrating the ordered full \(j\)-tuple density orders the \(j-r\) omitted daughters in \((j-r)!\) ways. The downward inversion therefore gives total same-parent densities
\[
b_2=q_2,qquad b_3=q_3,qquad b_4=q_4.
\]
The singleton rate makes \(b_1=\rho\). Partitioning an observed ordered tuple by parents then gives all \(2,5,15\) set partitions at orders two, three and four. Substitution of the recursive \(q_j\) definitions cancels the lower partitions and leaves
\[
\rho^{(2)}=a_2/D,qquad
\rho^{(3)}=a_3/A,qquad
\rho^{(4)}=a_4/V
\]
on the declared supports. Since those supports contain the three frozen target domains in the required way, division by \(\lambda_0^j\) produces the stated \(C_j\).

The second component of the submission considers a bounded positive-measure window \(B_0\) of diameter at most \(M\). With \(N=X(B_0)\), the target pair density gives
\[
\mathbb E(N)_2=\lambda_0^2C_2J(B_0).
\]
For \(n=\lfloor\mathbb EN\rfloor\), the pointwise integer inequality \((N-n)(N-n-1)\geq0\) gives the sharp lower bound used in (28). The ball calculation follows from the exact overlap-volume integral. The signed-test-function inequality is simply non-negativity of the variance of \(\sum_{x\in X}f(x)\), with its diagonal term retained.

## Review reasoning summary

The following are the decisive audit checks. They are a structured account of the verification, not a transcript of private deliberation.

| Check | Calculation or evidence | Result |
|---|---|---|
| Governing quantifier | Claim section, final reasoning summary, limitations 3--4, and response item 1 all restrict existence to \(0<\lambda_0\leq\lambda_*\). | The arbitrary-intensity target is not overstated. |
| Face-support closure | For a face vertex, its opposite face-edge line lies in that vertex's tetrahedral opposite-face plane; distance to the line is no smaller than distance to the plane. | Every \(S_4\) face lies in \(S_3\); equation (11) only uses defined internal triangle values. |
| Nonempty tetrahedral support | The centroid identity bounds the least altitude by \(\sqrt{2/3}M\); positive-measure nonemptiness gives strict inequality. A regular tetrahedron with a nearby admissible side length supplies an open positive set. | \(G>0\), and \(Z_4,Z_3,Z_2\) are strictly positive. |
| Endpoint integrability | \(4\pi\int_0^M r\,dr=2\pi M^2\). | Removing the positive pair cutoff does not destroy local integrability or normalisation. |
| First marginal coefficient | With pair length \(d\), \(A=dr/2\); integrating \(1/r\) over a radius-\(M\) ball gives \(\pi^2M^2\). | \(\mathcal MK_3\leq2\pi^2M^2K_2=BK_2\). |
| Second marginal coefficient | With signed height \(u\), \(V=A|u|/3\); integrating \(3/(A|u|)\) over both ball cross-sections for \(H\leq|u|\leq M\) gives \(G/A\). | \(\mathcal MK_4\leq GK_3\). |
| \(q_2\) positivity | The relative subtraction is at most \(\rho^2M/a_2=IMs=E_2(s)\). | The first bound in (15) follows when \(E_2\leq1/2\). |
| \(q_3\) positivity | Using \(A/D_{ij}\leq M/2\) gives the pair contribution \(6BMs\); using \(A\leq M^2/2\) gives \(2BIM^2s^2\). | Their sum is exactly \(E_3(s)\). |
| \(q_4\) positivity | The four triple terms, three pair-pair terms, six pair terms and baseline term are bounded respectively by \((16/3)GMs\), \((8BGM/I)s\), \(16BGM^2s^2\), and \((8/3)BGIM^3s^3\). | Their sum is exactly \(E_4(s)\); no partition type is omitted. |
| Exact-size kernel positivity | Use the upper marginal bounds on \(q_4,q_3\) together with \(a_4G=a_3/4\) and \(a_3B=a_2/4\). | The lower bounds (16) follow. The alternative expression for \(F_2\) also gives \(F_2\leq q_2\). |
| Prescribed intensity | From \(Q_2=a_2I-\rho^2L=\rho-\rho^2L\), \(Z_4=Q_4\), \(Z_3=Q_3-Q_4\), and \(Z_2=Q_2-Q_3+Q_4/2\), the non-singleton intensity plus (17) equals \(Q_2+\rho^2L=\rho\). | The input intensity is obtained exactly throughout the stated interval. |
| Full-density hierarchy | Direct enumeration gives the all-singleton, pair-singleton, pair-pair, triple-singleton and same-parent blocks in counts \(2,5,15\). | Equations (19)--(21) are full factorial/product densities, not cumulants alone. |
| Process properties | Parent rates and cluster normalisers are finite; offsets are bounded; cluster size is at most four; all mark laws are absolutely continuous. | Stationarity, isotropy, simplicity, local finiteness, local exponential moments and density existence follow. |
| Null-window repair | Equation (28) now quantifies only over bounded positive-measure Borel windows and establishes \(0<J(B_0)<\infty\) before division. | No undefined \(0/0\) case remains. |
| Count bound | Expanding \((N-n)(N-n-1)\geq0\) yields \(\mathbb E(N)_2\geq n(n-1)+2n\theta\). | Equations (27)--(29), including the zero bound for mean below one, are correct. |
| Covariance bound | The variance identity includes \(\lambda_0\int f^2\); diameter of the support ensures that every off-diagonal pair used lies in \(\mathcal D_2\). | Equation (30) is a general point-process condition and does not import a Cox-only Jensen inequality. |

## Criterion-by-criterion assessment

| Criterion | Evidence/location | Assessment |
|---|---|---|
| Correct target and quantifiers | Claim and scope; final paragraph of the claim; reasoning summary; limitations 3--4; response item 1 | **Partial only, accurately stated.** Exact existence is proved for every prescribed intensity in a nonempty low-intensity interval. The general quantifier over all \(\lambda_0>0\) remains unresolved. |
| Whole-space existence and stationarity | Process and existence after (16)--(17) | **Established for the restricted theorem.** Homogeneous parent streams on all of \(\mathbb R^3\) and translation-covariant bounded offset marks give a stationary whole-space process. |
| Simplicity, local finiteness, prescribed intensity | Process paragraph after (17); intensity calculation through \(Q_j,Z_j\) | **Established for \(0<\lambda_0\leq\lambda_*\).** Absolute continuity makes within- and between-cluster collisions null; bounded offsets and finite Poisson parent counts give local finiteness; the intensity calculation is exact. |
| Local fourth moments and density existence | Same process paragraph; bounds (8), (13), (15)--(16); finite-cluster partition formula | **Established.** Bounded-window counts in fact have finite exponential moments. Same-parent densities are locally integrable, and cross-parent partitions preserve absolute continuity. |
| Full density hierarchy and combinatorial factors | Equations (18)--(21) and the explicit block counts | **Established.** The \((j-r)!\) coefficient and every partition through order four are present. |
| Exact identities on the entire domains | Support definitions (2), recursion (9)--(11), substitution (22), constants (23) | **Established for the restricted theorem.** The pair endpoint \(D\downarrow0\) is included a.e.; \(\mathcal D_3\subseteq S_3\); \(S_4=\mathcal D_4\). |
| One jointly feasible parameter choice | Equations (3)--(7), (17), and (23) | **Established at each prescribed low intensity.** One parameter set and one process give all three positive constants simultaneously. No such conclusion is proved above \(\lambda_*\). |
| Source support and prior-work comparison | Relation to prior work; References; response item 4; frozen literature dossier sections 1, 5 and 6 | **Adequate.** Reused formula groups have exact local source section/label locators, the derivation is reproduced self-containedly, unpublished manuscripts are identified as such, and audits are not treated as proof certificates. |

## Detailed findings

### No new actionable defect

I found no invalid inference, missing essential hypothesis, uncounted partition, unsupported extension of a target formula, or source claim on which the restricted theorem depends. This conclusion is limited to the reviewed v02 hash and the packet listed above; it is an informal mathematical audit, not formal verification.

### A5-v01-01 — governing scope

- Prior severity: blocking if left ambiguous.
- Location checked: Claim and scope, the paragraph immediately following results 1--2; Reasoning summary; Checks and limitations items 3--4; Response item 1.
- Repair: v02 says explicitly that the theorem covers every prescribed \(0<\lambda_0\leq\lambda_*\), and that neither existence nor non-existence is established above \(\lambda_*\).
- Status: **closed**.
- Consequence: the restricted theorem may be used as exact partial progress, but the final synthesis must not report approach 5 as solving the governing arbitrary-intensity problem.

### A5-v01-07 — null windows

- Prior severity: local correctness defect in the displayed necessary condition.
- Location checked: paragraph before (26) and equation (28); Checks and limitations item 5.
- Repair: \(B_0\) is now a bounded positive-measure Borel set with diameter at most \(M\), and v02 proves \(0<J(B_0)<\infty\) before dividing by \(J(B_0)\).
- Status: **closed**.
- Consequence: equation (28) has a well-defined denominator on its entire stated range.

### A5-v01-08 — non-existence wording

- Prior severity: potentially material scope ambiguity.
- Location checked: exact low-intensity result 1; paragraph after the two headline results; Reasoning summary; Checks and limitations items 3--4; Response item 3.
- Repair: v02 now says that the result rules out only the universal statement that no intensity admits a solution. It expressly leaves both alternatives unresolved above \(\lambda_*\).
- Status: **closed**.
- Consequence: the positive construction is no longer liable to be read as a general obstruction or as arbitrary-intensity existence.

### A5-v01-09 — source hygiene

- Prior severity: source-traceability defect.
- Location checked: Relation to prior work; References; Checks and limitations item 8; Response item 4.
- Repair: the reused construction, positivity and partition formulas are tied to named sections, file names, labels, equations and lemmas in the unpublished finite-cluster manuscript. The submission rederives the mathematics rather than using the earlier theorem at the excluded endpoint. It labels prior audit files as historical records and denies them independent theorem status.
- Status: **closed**.
- Consequence: no essential step rests on an earlier audit verdict. The detailed local source locators were not separately reopened in this packet-restricted delta review, but the frozen literature dossier corroborates the prior manuscript's scope, and the present proof is self-contained.

### Remaining scope, not an author-repair defect

The quantity \(\lambda_*\) is only a sufficient positivity threshold for this construction. The argument neither proves that this threshold is optimal nor gives a necessary upper-intensity obstruction. This is the central unsolved part of the governing problem, not a defect in the theorem as now stated. Rewording the same proof cannot close it; a new construction, a positivity improvement that covers all intensities, or a valid general obstruction would be needed.

## Coder/source verification

- No coder request was made. The disputed points were exact identities and inequalities that could be checked directly from the frozen formulas; floating-point work would not strengthen them.
- The packet hashes were checked with `shasum -a 256`; every supplied file matched the digest in `context_packets/review_5_v02.md`.
- The endpoint integral, both marginal coefficients, every term in \(E_2,E_3,E_4\), the downward inversion, the intensity cancellation, the \(2,5,15\) partition enumeration, the ball-energy coefficient and the integer-count inequality were re-evaluated analytically.
- No simulation, finite grid, empirical tolerance, or external search was used as proof evidence.
- Published and unpublished source scope was assessed from the frozen source dossier and bibliography. The review does not elevate source summaries into a proof: the endpoint construction and count inequalities were checked from the self-contained derivations in v02.

## Revision history

| Issue | v02 disposition | Delta-review result |
|---|---|---|
| A5-v01-01: arbitrary intensity unresolved | Explicit restriction to \(0<\lambda_0\leq\lambda_*\); both possibilities above it left open | Closed |
| A5-v01-07: null windows | Positive-measure hypothesis and \(0<J(B_0)<\infty\) inserted | Closed |
| A5-v01-08: ambiguous non-existence statement | Replaced by the logically exact limited conclusion | Closed |
| A5-v01-09: source hygiene | Exact manuscript locators added; prior audits demoted to historical records; proof kept self-contained | Closed |
| New v02 issues | None found | No further scoped repair round required |

## Decision record

- **Reviewed artefact:** `tracks/approach_5/submissions/v02.md`, SHA-256 `3aa480e3279781cc0f45a009d71326c447778b94f626a7d88402f278347d3ab9`.
- **Restricted-theorem decision:** accepted as a correct self-contained informal proof at every prescribed \(0<\lambda_0\leq\lambda_*(M,h_3,h_4)\), under the frozen positive-measure admissibility assumptions.
- **Governing-target decision:** not established; arbitrary prescribed positive intensity remains unresolved.
- **Necessary-condition decision:** equations (28)--(30) are valid but non-obstructive because \(C_2\) is free.
- **Prior-issue decision:** A5-v01-01, A5-v01-07, A5-v01-08 and A5-v01-09 are all closed.
- **Further repair decision:** no additional author repair round is needed for this submission. Any continuation should be new research on the intensity gap, not another wording or local-proof repair.
- **Permitted synthesis statement:** approach 5 supplies an exact continuum construction with no lower pair cutoff for a nonempty interval of independently prescribed low intensities, together with general second-order necessary inequalities; it does not solve or refute the problem for all prescribed intensities.

## Remaining mathematical questions

1. Can the non-negative residual-kernel construction be modified so that its exact full identities survive at every prescribed intensity, rather than only where the sufficient bounds \(E_j\leq1/2\) hold?
2. Is there a general realizability inequality, using only correlations on the frozen finite domains, that excludes some high intensities even though \(C_2,C_3,C_4\) are free?
3. If the present construction cannot be extended, is its obstruction intrinsic to finite clusters, or only to these particular recursive kernels and coarse positivity estimates?
4. Can one combine the exact cancellation mechanism with a Cox representation, where deterministic scaling of the directing measure would remove the intensity restriction without changing the normalized \(g_j\)?

These questions concern the remaining exact theorem. Empirical fit, numerical approximation and optimisation of the displayed sufficient threshold are separate matters and do not change the verdict above.
