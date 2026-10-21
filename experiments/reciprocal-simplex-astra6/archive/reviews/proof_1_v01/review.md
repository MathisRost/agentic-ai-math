# Review — proof_1 / submission v01 / target S1

- Type: fresh independent review of one frozen construction submission.
- Reviewer: `/root/review_proof_1_v01`; session `session-12`; turn `turn-24`.
- Requested and verified model/effort: `gpt-6-astra`, `xhigh`. Actual session metadata, environment identity, turn context and numeric token telemetry were verified before mathematical work; see `preflight.json`.
- Session began: `2026-10-20T17:33:31.682Z`. The report freeze time and final available accounting checkpoint are recorded separately in `review_freeze.json`.
- Active target: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Submission: `reviews/proof_1_v01/proof_snapshot.md`, SHA-256 `acf0c4de3dcd7ee1caeeff0da17e9d8d7d8144b5ecb984d0742bb1662fc52473`; construction attempt **1 of 4**.
- Dispatch packet: `packets/review_proof_1_v01.json`, SHA-256 `a63247fff2bf50c8fdfc1b3f22034a34aa5c54c0972b597c40a0e630d6c10692`.
- Adopted amendment: `statements/S0_to_S1.md`, SHA-256 `b2534040520dfc63bf5c22ecc508257308e619a040a7c6c54ce44375742394de`.
- Cited seed excerpt: `cited_coordinator_submission_v02.md`, SHA-256 `f0d755efa2b82343a5ff7f171c0ba69ccdcd92ba67a36106e9c47052197a2ac9`; its supplied provenance record has SHA-256 `84466d1ec8e8106752e5e634f0878d826d11940490a9404ea3ff3586279155a6`.

All 19 file hashes enumerated in the review packet, and the packet hash itself, matched. The frozen proof-reviser skill and both required references were read. The reviewer received only the allowed instructions, common context, target history, frozen submission and cited seed excerpt, together with the reviewer's own allowlisted runtime metadata. No author conversation, private work, other construction submission, other construction review, old run or other chat was inspected. The historical amendment record was accepted as the dispatch's target authority; the earlier obstruction proofs and their reviews were not independently re-audited here.

## Correctness verdict and scope

**Partial progress, with valid scoped Poisson-cluster obstructions. This submission does not pass exact S1.** The author accurately identifies that limitation. I found no material false assertion in the submitted mathematical results. The low-intensity pair-and-triangle construction is valid on its stated full lower-order domains, and the necessary conditions proved for the stated finite-cluster Poisson representation are valid.

S1 requires all three full factorial density identities, for every independently prescribed positive pair $(\lambda,M)$. The actual construction proves only the pair and triangle identities, and only under (3). Its fourth density is explicitly (32), and its finite local exponential moments preclude the required reciprocal-volume identity. Thus this is one unsuccessful exact-target construction submission, not an invalid partial theorem and not a proof that S1 is false. There is no attempt-counter reset.

The following claim-level conclusions were checked:

| Submitted claim | Verdict and exact scope |
|---|---|
| Lemma 1: finite local third moments and infinite fourth moments in every nonempty open ball | Established for any S1 solution, without a representation assumption. |
| Equations (9)–(11): all parent partitions and the residual coefficients | Correct in the S1 setting and in the actual construction; see the general extended-measure notation qualification below. |
| Equations (12)–(14): nonnegative residuals at every prescribed $(\lambda,M)$ | Established as an algebraic feasibility result. No joint cluster realisability follows. |
| Proposition 2 and (16): bounded populations or finite fourth population moment are impossible | Established within the specified Poisson-cluster representation; no radius bound is needed. |
| Proposition 3: iid offspring geometry independent of population is impossible | Established for the stated probability-density model, including a random density independent of population. The infinite-moment case uses S1's global finite-almost-everywhere requirement. |
| Proposition 4: divergent fourth population factorial moment among clusters of diameter at least $\delta$ | Established for every stated $0<\delta<M/\sqrt2$. It is a necessary condition within the representation, not a sufficient construction criterion. |
| Equation (22) and positivity of $k_3$ | Established, with the asserted almost-everywhere and bounded-ball qualifications. |
| Section 6: genuine whole-space pair-and-triangle construction | Established under (3), including probability normalisation, exact intensity, all parent allocations and global absence of singular mass. |
| Exact S1 existence or general non-existence | Unresolved by this submission. |

This is an informal mathematical correctness audit, not a proof-assistant certification. The report supplies the detailed checks below rather than relying on the cited seed's authority.

## Reconstruction and detailed audit

### 1. Target, quantifiers and the moment consequences

The reconstruction at submission lines 18–26 agrees with the frozen S1. In particular, the full measures must have globally finite-almost-everywhere densities, even outside the prescribed diameter domains. No positive distance, area, volume or altitude threshold is available. A locally infinite fourth factorial measure is allowed; a singular component or a non-$\sigma$-finite full fourth measure is not.

The pair integral in (4) is correct:
\[
\int_{\|u\|<M}\frac{du}{\|u\|}
=4\pi\int_0^M r\,dr=2\pi M^2.
\]
For a fixed pair of length $d$, the reciprocal triangle area is $2/(dr)$ in cylindrical coordinates around the pair line. Within a radius-$M$ ball centred at one endpoint,
\[
\int \frac{dz}{r}
=2\pi\int_0^M 2\sqrt{M^2-r^2}\,dr
=\pi^2M^2.
\]
Multiplying by $2/d$ yields precisely (5). This estimate handles both a short base edge and a nearly collinear third point; it does not assume a positive lower edge length. The support condition also implies that the marginal vanishes when the base edge has length at least $M$.

For a ball $B$ of diameter below $M$, the third factorial integral is at most
\[
2\pi^2M^2\int_{B^2}D^{-1}
\le 4\pi^3M^4|B|<\infty.
\]
The pair integral and the first moment are finite, so the stated identity for $N^3$ proves a finite third count moment. Full absolute continuity matters: it rules out additional mass on collinear triples that these integrals would miss. A finite cover by small balls and the displayed deterministic inequality then prove the same assertion for every bounded Borel set. Overlap in the cover causes no problem, since the covered count is bounded above by the sum.

The fourth-moment divergence is also correct. Choose a small square strictly inside the ball and with diagonal strictly below $M$. Small three-dimensional neighbourhoods of three vertices give a positive-measure set of noncollinear bases. On a sufficiently small base neighbourhood, an orthonormal frame in the base plane and a unit normal can be chosen continuously. The fourth vertex can range in a small in-plane patch near the remaining square vertex and a signed normal interval around zero. All six edge lengths and all four face areas remain bounded below by positive constants, while the diameter remains strictly below $M$.

For each fixed base, the coordinate transformation for the fourth point is orthonormal and has absolute Jacobian one. Its volume is $A|h|/3$, including the factor $1/6$ in the definition of tetrahedral volume. Thus the fourth-point integral contains
\[
\frac{3}{A}\int_{\text{patch}}du\,dv
\int_{0<|h|<\varepsilon}\frac{dh}{|h|}=\infty.
\]
No integration is taking place solely on the coplanar null set: the divergence comes from nonzero heights approaching it. Tonelli applies to the nonnegative integrand. The family can be placed inside every nonempty open ball, proving Lemma 1 exactly as stated.

The lemma gives a genuine general moment-class restriction. It does not turn infinite fourth moments into a contradiction with local finiteness or finite intensity. It also does not justify adding a lower altitude cutoff to S1.

### 2. Whole-space Poisson-cluster existence and simplicity

The framework at lines 90–105 is well defined. Nonempty finite marks and $\int N\,d\nu=\lambda<\infty$ imply $\nu(\mathcal C)\le\lambda$, so the underlying product intensity is $\sigma$-finite. For each bounded Borel $B$,
\[
\int_{\mathbb R^3}\int C(B-z)\,\nu(dC)\,dz
=|B|\int N\,d\nu=\lambda|B|.
\]
This follows by summing one translated indicator per mark point and using Tonelli. It does not require a bound on mark radii or diameters. The count is therefore finite almost surely, and a countable exhaustion gives simultaneous local finiteness on all bounded sets.

The restriction of the parent Poisson measure to clusters meeting $B$ has finite intensity at most $\lambda|B|$. Consequently there are almost surely only finitely many contributing parents in that window, although their original locations need not lie in a fixed bounded neighbourhood of $B$.

For two distinct parents, a coincidence between specified offspring fixes one translation difference and has zero six-dimensional Lebesgue measure in the two parent translations. Conditional on the finite marks, the union over their point pairs is finite. Integration over the marks and a countable exhaustion prove that all such coincidences have probability zero. Marks themselves are simple. This establishes simplicity without assuming that arbitrary mark laws have displacement densities.

Translation invariance of the parent intensity proves stationarity. The displayed expectation gives exactly the intended intensity. None of these conclusions requires a fourth moment.

### 3. Parent allocations and the residual identities

Each ordered observed tuple has a unique set partition according to its parent labels. Ordering the blocks by their least tuple index lets the factorial identity for distinct Poisson parents be applied without an extra block factorial. All selections within one parent are ordered and distinct. Thus the relevant partition counts are:

| Order | Block types and multiplicities |
|---|---|
| 2 | $1+1$: 1; $2$: 1 |
| 3 | $1+1+1$: 1; $2+1$: 3; $3$: 1 |
| 4 | $1+1+1+1$: 1; $2+1+1$: 6; $2+2$: 3; $3+1$: 4; $4$: 1 |

These are exactly the terms in (10). In particular, there are three unordered pairings at order four, not six, and four choices for the triple block.

For the unrestricted framework before a candidate is assumed to meet S1, some $K_r$ may fail to be $\sigma$-finite, as Proposition 3 itself later shows. Equation (9) is unambiguous if its products are defined through the underlying integrals over distinct parents. Ordinary product-measure notation and the unrestricted invocation of Tonelli should not silently impose a product convention for arbitrary non-$\sigma$-finite image measures. This is a presentational qualification, not a failure of a consequential inference: when S1 is assumed, $K_r\le\alpha^{(r)}$ makes each $K_r$ $\sigma$-finite; the actual construction also has boundedly finite factorial measures. All density formulas used in the arguments therefore lie in the ordinary $\sigma$-finite setting. Finding P1V01-03 gives the small repair.

Finite-almost-everywhere Lebesgue densities do imply $\sigma$-finiteness, even when every nonempty open configuration set has infinite mass: intersect bounded boxes with density sublevel sets. A measure dominated by such a measure is $\sigma$-finite and absolutely continuous. This validates the passage from $K_r$ to $k_r$.

Substitution at order three gives
\[
k_3=\frac{a_3}{A}-\lambda a_2\sum D^{-1}+2\lambda^3.
\]
At order four, the lower terms simplify to
\[
\lambda a_3\sum A_J^{-1}
+a_2^2\sum (D_{ij}D_{kl})^{-1}
-2\lambda^2a_2\sum D_{ij}^{-1}+6\lambda^4.
\]
Here each edge occurs in two of the four face sums, and each edge occurs once among the three pairings. Subtracting gives exactly the signs and constants in (11). Every face and edge of a nondegenerate tetrahedron of diameter below $M$ is in its lower-order prescribed domain. Almost-everywhere lower-order identities lift to almost-everywhere identities on the higher-dimensional configuration space by Fubini; no simultaneous pointwise version is needed.

### 4. Algebraic feasibility at every intensity

All four geometric estimates in (13) hold with the stated constants. Triangle area is half an edge times an altitude, and that altitude is at most another edge length, hence below $M$. A tetrahedral altitude is at most an edge to a face vertex, giving $V/A_J\le M/3$. The determinant bound gives $V\le M^3/6$. For the pairing $12|34$,
\[
6V=|\det(x_2-x_1,x_3-x_1,x_4-x_3)|
\le D_{12}M D_{34}.
\]
Relabelling gives the other pairings.

For the constants in (12), these estimates yield
\[
Dq_2\ge a_2-\lambda^2M=a_2/2,
\qquad
Aq_3\ge a_3-\tfrac32\lambda a_2M\ge a_3/2.
\]
For the fourth residual, discard its positive edge term and use the four face, three pairing and constant estimates:
\[
Vq_4\ge a_4-
\left(\tfrac43\lambda a_3M+\tfrac12a_2^2M+\lambda^4M^3\right)
=a_4/2.
\]
Thus the asserted positive lower bounds are correct for every fixed positive $(\lambda,M)$.

This calculation establishes only a necessary sign condition for a possible Poisson-cluster solution. It gives neither a probability distribution on finite configurations nor simultaneous factorial consistency of its different orders. In particular, it does not make the infinite fourth marginal available for subtraction from a finite third measure. The author's limitation at lines 183 and 415 is essential and accurate.

### 5. Population moment obstructions

For $N(C)\le K$, the convexity estimate in Proposition 2 applies to the integer contribution $C(B-z)\in[0,K]$. The exponent in the Poisson exponential formula is bounded by
\[
\frac{e^{\theta K}-1}{K}\lambda|B|.
\]
Finite truncations and monotone convergence justify the formula and bound. Therefore all local exponential moments, and in particular fourth moments, are finite. This contradicts Lemma 1 under S1. The argument indeed does not require bounded cluster radius.

For the more general claim, $C(B-z)^4\le N(C)^3C(B-z)$ gives (16). The number of parents that contribute to $B$ is finite Poisson. Its jump measure has finite fourth moment by (16); lower jump moments are then finite because the jumps are positive integers. Expanding the fourth power of its compound Poisson sum by the number of distinct parent indices gives finite fourth count moment. This proves the stated exclusion under $\int N^4\,d\nu<\infty$.

These results exclude particular representations. They do not imply that an arbitrary stationary point process has finite fourth moments, nor that a different representation of a process must inherit a population bound.

### 6. Population-independent iid geometry

In Proposition 3, empty clusters can be discarded when embedding the model into the preceding nonempty-mark framework. The intensity remains $\kappa\mathbb EN$, which is finite and positive. Conditional iid sampling from a probability density produces a simple finite mark almost surely.

If $\mathbb EN^4<\infty$, the preceding moment argument applies. Otherwise $\mathbb E(N)_4=\infty$, since $N^4$ and $(N)_4$ have comparable positive growth for large integer $N$. Independence of the displacement density from $N$ gives the factorisation (18), including after averaging a random density.

The measure $\beta_4$ is nonzero and locally finite. In fact,
\[
\beta_4(B\times(\mathbb R^3)^3)
=\int\prod_i f(y_i)\,d\mathbf y
\int\mathbf1_B(z+y_1)\,dz=|B|.
\]
The same computation remains true after averaging $f$. It also bounds $\beta_4$ on bounded configuration sets.

Equation (18) can be obtained first with a truncated factorial population weight and then by monotone convergence. Its meaning is zero on $\beta_4$-null sets and infinity on every set of positive $\beta_4$-measure. If $K_4$ had a countable cover by finite-mass sets, every set in the cover would be $\beta_4$-null. That would contradict $\beta_4\ne0$. Thus $K_4$ is not $\sigma$-finite.

Under S1, $K_4\le\alpha^{(4)}$ and $\alpha^{(4)}$ is $\sigma$-finite, so this is a contradiction. The proof does not confuse infinite bounded-set mass with failure of local finiteness. It uses the stronger failure of $\sigma$-finiteness and uses S1's global finite-almost-everywhere condition. It does not require the displacement convolution to be positive everywhere.

The independence assumption is indispensable to this argument. Population-dependent displacement laws cannot be factored out in (18), and the proposition gives no obstruction for them. The assertion is not a theorem excluding all heavy-tailed Poisson clusters or all random geometric mark laws.

### 7. Separated coplanar configurations and cluster diameters

For every $0<\delta<M/\sqrt2$, there is a square side $s$ strictly between $\delta$ and $M/\sqrt2$. At the square, all six distances exceed $\delta$, the largest distance is below $M$, and all four triangular face areas are positive. Continuity gives the bounded family $F$ in (19), while signed fourth-vertex height can still approach zero through nonzero values.

The reciprocal-volume integral over $F$ diverges. On $F$, however, the pair same-parent density is bounded by $a_2/\delta$ and the triple same-parent density by $a_3/\eta$, outside harmless null sets. Consequently every one of the other fourteen partition terms has finite integral. The nonnegative decomposition forces $K_4(F)=\infty$; there is no subtraction of infinite quantities.

Any selected same-parent quadruple in $F$ belongs to a cluster of diameter at least $\delta$. For each such quadruple, requiring the first translated point to lie in a bounded first-coordinate envelope $B$ permits a set of translations of volume at most $|B|$. Summing over its $(N)_4$ ordered quadruples gives (21), hence the stated necessary divergence.

If every population-$n$ cluster has diameter at most a deterministic $r_n\to0$, the set of population sizes with diameter at least a fixed $\delta$ is finite. Since $\nu(\mathcal C)<\infty$, the weighted integral in (2) would then be finite. This verifies the shrinking-diameter exclusion.

The conclusion is a weighted moment restriction on a geometric subfamily. It does not assert that every large cluster has large diameter or provide a sufficient criterion for success. The displayed upper range $M/\sqrt2$ is a valid range for the square proof; no optimality of that range is claimed or required here.

For (22), fix a noncollinear base triple in an open ball of diameter below $M$. Its affine plane cuts the ball in a relatively open set. A small plane patch can be chosen away from the finitely many lines joining the base vertices, and away from the vertices. On a sufficiently small normal thickening, all other edge and face factors are bounded while $1/V$ has an infinite height integral. Fubini for the exceptional Lebesgue-null sets gives (22) for almost every base triple.

The marginal $K_4(d\mathbf x\times B)$ is obtained from the same selected-triple measure defining $K_3$ by the finite nonnegative weight
\[
C(B-z)-\sum_{i=1}^3\mathbf1_B(x_i),
\qquad x_i=z+y_i.
\]
Therefore it is absolutely continuous with respect to $K_3$ in the sense of null sets, even though this marginal need not itself be $\sigma$-finite. If $k_3$ vanished on a positive-Lebesgue-measure subset of $B^3$ off collinearity, the weighted marginal would vanish there, contrary to (22). Hence the claimed almost-everywhere strict positivity of $k_3$ is justified. Finiteness of each realised mark weight is compatible with an infinite mean under third-order sampling.

### 8. Actual pair-and-triangle construction

The construction's constants are a separate choice from (12). With
\[
I=2\pi M^2,\quad J=2\pi^2M^2,\quad L=4\pi M^3/3,
\quad
a_2=\lambda/I,\quad a_3=a_2/(4J),
\]
the marginal bounds in (23) are correct, including support outside the base-edge domain. The kernels can be assigned zero on all degenerate configurations, with no effect on their measures.

The pair relative error is at most $2\pi t$. For the triangle relative error, the exact constants are
\[
\frac{\lambda^3M^2}{2a_3}=8\pi^3t^2,
\qquad
\frac{3\lambda a_2M}{2a_3}=12\pi^2t.
\]
Using the upper bound $q_2\le a_2K_2^0$ and conditions (3) yields both sides of (25). This includes configurations with arbitrarily short edges or small positive triangle area.

The marginal subtraction is legitimate here because the triangle kernel has a finite marginal. In particular,
\[
F_2=q_2-\mathcal Mq_3
\ge (a_2/2-a_3J)K_2^0=(a_2/4)K_2^0,
\]
and $0\le F_2\le q_2$, while $F_3=q_3\ge(a_3/2)K_3^0$. Thus both $F_j$ are nonnegative, symmetric, translation and rotation invariant, with finite positive anchored integrals $Z_j$. There is no signed mark density.

The offset law $F_j(0,\mathbf y)/Z_j$ integrates to one. The parent rate $Z_j/j!$ is finite and positive. Since degenerate configurations form null sets, the emitted configurations are simple almost surely. Their diameters are below $M$.

The factor in (29) is correct. There are $(j)_r=j!/(j-r)!$ ordered selections of $r$ vertices. For any one selection, symmetry and translation invariance let the first selected vertex become the anchor; the associated linear changes of translation and offset variables have absolute Jacobian one. Integrating the unselected $j-r$ vertices therefore produces $\mathcal M^{j-r}F_j/Z_j$. Multiplication by the number of selections and the rate $Z_j/j!$ leaves
\[
\frac{\mathcal M^{j-r}F_j}{(j-r)!}.
\]
This also covers selections that omit the original parent point. No missing anchor multiplicity is present.

All quantities in the intensity calculation are finite. Tonelli gives
\[
Z_3=Q_3,\qquad Z_2=Q_2-Q_3,\qquad
Q_2=a_2I-\lambda^2L=\lambda-\lambda^2L.
\]
The size-two stream contributes $Z_2$ to intensity and the size-three stream contributes $Z_3/2$. Their total is $Q_2-Q_3/2$. The proposed singleton rate
\[
\beta=\lambda^2L+Q_3/2
\]
is finite and nonnegative, and the sum of all intensities is exactly $\lambda$. In particular, this construction does not merely produce an intensity proportional to the requested value.

Formula (29) now gives $k_2=q_2$, $k_3=q_3$, $k_r=0$ for $r\ge4$, and $k_1=\lambda$. Substituting into the full partition formulas proves (31) on all of the stated lower-order domains. The constants do not vary with configuration.

The existence and simplicity checks in Section 2 apply to the combined mark measure. Rotation invariance also gives isotropy, although S1 does not require it. With at most three points per mark, Proposition 2 establishes finite local exponential moments. At any fixed factorial order, there are finitely many partitions with nonzero block sizes only one, two and three. Each block has a genuine finite-almost-everywhere density; their products are densities on disjoint coordinate blocks. Therefore the entire factorial measure is absolutely continuous, finite almost everywhere, and has no hidden diagonal, collinear or coplanar component. Anchoring one observed point at the parent does not introduce a singular component after the continuous translation and remaining offsets are integrated.

The fourth density is exactly (32). Its finite fourth local moments rule out equality with $a_4/V$ on all of $E_4(M)$ for any positive $a_4$. This is a proved failure of this particular partial construction at the fourth requirement.

Solving the second inequality in (3) gives the positive root in (33):
\[
t\le
\frac{\sqrt{9\pi+1}-3\sqrt\pi}{4\pi^{3/2}}.
\]
The numerator is positive, so there is a nonempty range of positive parameters. The additional pair inequality can be imposed as stated. Under spatial dilation by a factor $c$, intensity becomes $\lambda/c^3$ and diameter scale becomes $cM$, leaving $\lambda M^3$ unchanged. Hence the given rescaling observation is correct: the theorem does not reach arbitrary independent prescribed intensity and geometry.

## Finding register

The first two entries are substantive unresolved obligations, already acknowledged by the author. They are not defects in the proved partial results. The third is a local clarification in the framework statement. No material invalid inference was found in the claims accepted above.

| ID | Location in frozen submission | Precise issue | Consequence | Repair/status |
|---|---|---|---|---|
| **P1V01-01** | Lines 28–46; Section 6, especially (3), (31) and (32) | The actual construction gives two identities in a restricted intensity range, while S1 requires three identities for every prescribed $(\lambda,M)$. Its fourth moments are finite. | Exact S1 is not established; this is an unsuccessful exact-target attempt with valid partial progress. | **Open for exact S1.** A successful repair must establish every active requirement. Merely changing the target or citing the partial theorem cannot close this item. |
| **P1V01-02** | Lines 140–183 and 415; residuals (11)–(14) | Pointwise nonnegative residuals have not been realised simultaneously as (8) for any single nonnegative finite-configuration mark measure with $\int N\,d\nu=\lambda$. The fourth local marginal is infinite, so finite-kernel marginal subtraction cannot supply that missing construction. | The all-intensity algebraic result is not a process existence theorem. | **Open, acknowledged.** Supply an actual joint mark law and prove all factorial measures, outside-domain regularity, intensity and local finiteness. The scoped obstructions identify constraints on such a law but do not construct it. |
| **P1V01-03** | Lines 107–125, equation (9) before the density assumption | The general framework permits non-$\sigma$-finite $K_r$, so abstract product notation should specify its meaning before a blanket Tonelli argument is invoked. | No downstream theorem fails: all density applications have $\sigma$-finite factors, and parent-level integrals are well defined. | **Minor clarification.** Define (9) through the underlying distinct-parent integrations, then state the ordinary product-measure/density version under $\sigma$-finiteness; alternatively place that qualification before (9). |
| **P1V01-04** | Lines 48, 86, 231, 264 and 399–403 | Historical obstruction verdicts, the full shrinking-ball example and seed supplements are mentioned, but the review packet supplies only the target amendment and the cited seed excerpt. | This review does not independently certify those historical works or source-provenance claims beyond the supplied hashes. The present mathematical conclusions do not depend on their authority, because the needed arguments are rederived. | **Scope limitation, no mathematical repair required.** Keep historical references distinct from the self-contained claims reviewed here; request further frozen passages only if a future proof actually depends on them. |

The model-independent moment statement in Lemma 1, the four restricted population conclusions, the residual algebra and the partial construction require no corrective mathematical changes on the evidence checked. In particular, no missing partition, wrong factorial, intensity deficit, non-normalised offset law, unjustified negative kernel or overlooked singular component was found.

## Amendment implications

No target amendment is proposed in the submission, and none is approved by this review.

Lemma 1 confirms that a hypothetical S1 solution must have infinite fourth moments on every nonempty open ball while retaining finite third moments on bounded sets. The finite-fourth-moment comparison subclass is therefore excluded. This does not exclude S1's broader class or justify silently adding a lower altitude cutoff.

Propositions 2–4 restrict the chosen Poisson-cluster representation. A possible solution in that framework needs unbounded population, an infinite fourth population moment, geometry outside the population-independent iid class, and the stated divergent fourth population moment among clusters with nontrivial diameter. These are necessary conditions within the framework. They neither force a change to the general target nor prove that any proposed replacement target would be achievable.

S0's historical verdict is preserved as recorded in the authorised amendment; this review does not replace it with the partial S1 result. The prescribed positive intensity, independence of the prescribed diameter, all three orders and full-measure interpretation remain unchanged. Attempt 1 has been used; three construction submissions remain under the manifest. The owner-amendment checkpoint after three unsuccessful reviewed attempts has not been reached.

## Source and coding evidence

The review independently reconstructed every substantive mathematical argument in the frozen submission. The supplied seed excerpt was used only to identify the claimed provenance and scope of the lower-order construction. Its stated low-intensity result and the submitted rederivation agree. The seed's full shape-restricted fourth-order theorem was not adopted as a theorem of this experiment and was not needed to establish any verdict here.

The source index and neutral DVJ context were read. No present-open-status, novelty or precise historical source claim is made in this review. No primary PDF was needed for the self-contained Euclidean, finite-moment and elementary Poisson calculations. No source request or coding request is outstanding.

Executed tool checks were limited to file/hash verification, the reviewer's allowed runtime metadata/accounting extraction, and writing/freezing the review artifacts. No simulation, numerical continuum certification, symbolic-package calculation or formal proof check was performed. The partition enumeration, determinant bounds, positive-root calculation and cluster normalisation were checked directly in the mathematical audit above.

The review did not examine excluded historical proofs or other tracks. It gives no conclusion about other submitted approaches, and it does not assess whether S1 has a solution outside the reviewed construction framework.

## Presentation judgement

The submission makes its partial status explicit at the beginning, states the exact target, and consistently distinguishes algebraic positivity from process realisation. Its explicit fourth density and intensity calculation are useful because they expose the precise limitations of the construction. The argument is readable and the equations use consistent ordered-tuple conventions.

The principal exposition improvement is P1V01-03: state the parent-integral interpretation of the general partition formula before using ordinary product-measure notation. The marginal discussion at lines 273–277 would also be easier to read if it explicitly wrote $x_i=z+y_i$, so that the selected observed points and the untranslated mark cannot be confused. Neither point changes the conclusions.

The historical references should remain clearly labelled as context. The self-contained proofs, rather than the earlier review status or seed description, carry the mathematical conclusions of this submission.

## Review summary and remaining obligations

The full parent allocation coefficients, all-intensity residual inequalities, finite-third/infinite-fourth moment claim, bounded-population exclusion, population-independent iid exclusion, separated-configuration diameter restriction and low-intensity partial construction have been checked and are supported.

The decisive unresolved obligation is a joint realisation of the residuals by one admissible cluster measure, for every independently prescribed $(\lambda,M)$, with all three full factorial identities and the required global absolute continuity. The fourth-order residual's infinite local marginal is a real constraint, not a licence to subtract infinities from the locally finite third-order measure. Population-dependent heavy tails remain possible in principle, but the submission supplies no law satisfying the required compatibility.

The appropriate recorded outcome is therefore **valid partial progress and scoped obstructions; exact S1 unresolved; construction attempt 1/4 does not pass**. Failure of this attempt is not evidence sufficient to declare the general theorem false.

## Accounting and freeze

The reviewer's actual environment session identity matched `session_meta.id`. The session's `turn_context` at line 8 reported `model: gpt-6-astra`, `effort: xhigh`. Numeric `token_count` events expose cumulative and last-use fields for input, cached input, cache-write input, output, reasoning output and total tokens. The metadata scope, session path and pre-mathematics evidence are preserved in `preflight.json`.

The latest available measured checkpoint, report hash, word count and freeze timestamp are stored in `review_freeze.json`. It is a checkpoint rather than a completed-turn total; final post-response usage is **NR** at freeze and can be reconciled by the coordinator. Cumulative snapshots must not be summed. Reasoning output is reported separately and must not be added again to the output total. No child agents were launched; parent inclusion semantics are **NR**. Actual charges and estimated costs are **NR**. No private deliberation transcript or invented usage estimate is included.
