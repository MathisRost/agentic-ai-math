# Review — nonexistence_2 / submission v01 / S0

- Reviewer: fresh independent reviewer, agent `/root/review_nonexistence_2_v01`, thread `session-05`, turn `turn-08`.
- Requested and verified model/effort: `gpt-6-astra`, `xhigh`. Verification used this reviewer's matching `session_meta` and `turn_context`, not a saved model configuration or the author's assertion.
- Session start: `2026-10-20T16:53:58.821Z`; review turn context: `2026-10-20T16:54:00.929Z`. Report freeze time and artifact hash are recorded in `review_freeze.json`.
- Setup root: `$SETUP`.
- Run root: the setup root followed by `/runs/20261020T164437Z_astra6`.
- Active statement: `statements/S0.md`; SHA-256 `3b5b5ad81bf56136bd79f0fde2d4aa39e3bed32aaf37511460007dfb0fc656f0`.
- Reviewed proof: `reviews/nonexistence_2_v01/proof_snapshot.md`; SHA-256 `4b15463c7115c2f0e56424e7ab2b293c0c33a10bb3a68d1d67a7c13074a2c14f`.
- Review packet: `packets/review_nonexistence_2_v01.json`; SHA-256 `d2524aca216c2e553ab7e2d32754997ce2e32b8dff1f0b3c55aa03f4018f8659`. Every enumerated allowed-file hash matched before mathematical work.
- Preflight: `reviews/nonexistence_2_v01/preflight.json`; SHA-256 `ee982a0ace5bccca87f0d7d8f044d444c9c912f745fcfc7ddae157f5f99c1681`.
- Type: fresh independent review of the whole frozen submission. No delegation, author repair, or target amendment was undertaken.

The received mathematical context consisted of the frozen S0, common context and source index, and this single proof snapshot. The frozen reviewer/accounting instructions, workflow, report/amendment templates, and proof-revision skill with both complete required references governed the review. No author conversation, author work or private notes, other track, prior review, starting information, old run, or other chat was read. The author's accounting and procedural assertions were not independently audited through excluded author records. Line references below refer to the frozen proof snapshot.

## Correctness verdict and scope

**The submission establishes a general obstruction to S0. S0 has no solution at any prescribed positive intensity.** Theorem 1 is a complete elementary argument using only the first moment measure and the full second factorial measure. Its scope includes S0's broad class, including processes with infinite fourth local count moments. It requires neither stationarity in law beyond the already prescribed first moment nor mixing, ergodicity, isotropy or a representation assumption.

The auxiliary results also hold as stated. Lemma 2 proves local integrability of the reciprocal-distance and reciprocal-area kernels. Theorem 3 proves reciprocal-volume divergence near ordinary coplanar quadruples, even with all edges and triangular faces uniformly nondegenerate. This gives a separate obstruction to finite fourth local moments. Theorem 4 constructs a stationary, simple, locally finite process of each prescribed positive intensity with finite third and infinite fourth local moments, and genuine full factorial densities finite on pairwise distinct tuples at every finite order. It correctly refutes a possible auxiliary inference; it is not offered as an S0 construction.

There is no blocking mathematical defect or unresolved essential dependency in these conclusions. The bounded-domain replacement questions remain unproved, as the author states. The outcome is **accepted general non-existence for the original target, plus an accepted separately scoped moment obstruction**. It is not an exact construction success, and this review adopts no replacement target.

## Reconstruction and detailed audit

### 1. Target, quantifiers and measure convention

S0 asks, for each prescribed $\lambda_0>0$, for a stationary simple almost surely locally finite process with first moment $\lambda_0\,dx$, and some fixed finite positive constants $a_2,a_3,a_4$. It requires identities of the full factorial expectation measures at orders two through four, with the displayed reciprocal kernels almost everywhere on all nondegenerate configurations. It allows infinite local higher moments and forbids an omitted singular component.

The submission preserves all of these distinctions. Its global theorem fixes an arbitrary $\lambda>0$ and an arbitrary finite $a>0$, and contradicts the first and second identities for that pair. Thus it excludes every possible choice of $a_2$ for each prescribed intensity, which is stronger than merely disproving a universal choice of constants. The constants are fixed as the observation radius grows. No assumption that $a_2$ is independent of $\lambda$ is used.

The process class need not initially have a locally finite second moment measure. That property follows on each bounded ball from the proposed pair density. This point closes the principal possible hidden-moment objection to the global proof. Conversely, the fourth-order measure need not be boundedly finite for the local calculation or the illustrative example. The review consistently uses S0's extended nonnegative measure convention.

### 2. Theorem 1: global count inequality, lines 61–99

Let $b=|B_1|$, $J_2=\int_{B_1^2}|u-v|^{-1}\,du\,dv$. The bound
\[
\int_{B_1}|u-v|^{-1}\,dv
\leq \int_{B_2}|z|^{-1}\,dz
=4\pi\int_0^2 r\,dr=8\pi
\]
holds for each $u\in B_1$. Consequently $0<J_2<\infty$. Values on the diagonal do not affect the Lebesgue integral. The full measure identity excludes an additional singular contribution that could invalidate the computed factorial moment.

Scaling both points by $R$ contributes $R^6$ from Lebesgue volume and $R^{-1}$ from the reciprocal distance. Therefore the asserted exact identity
\[
\mathbb E(N_R)_2=aJ_2R^5,\qquad
\mathbb EN_R=\lambda bR^3
\]
is correct. Together with $N_R^2=(N_R)_2+N_R$, it gives a finite second count moment for every finite $R$. The elementary second-moment inequality is therefore applicable without an extra hypothesis. It yields
\[
\lambda^2b^2R^6\leq aJ_2R^5+\lambda bR^3.
\]
Dividing by $R^6$ and taking the limit of this deterministic inequality contradicts $\lambda^2b^2>0$. There is no interchange of a random limit and expectation and no use of distant independence.

The sign, scaling exponent, ordered-tuple convention and diagonal contribution have all been checked. The diagonal term belongs to the raw second moment as $\mathbb EN_R$, not to the factorial measure. The strict positivity of intensity and finiteness of the fixed coefficient are the decisive parameter conditions. The proof applies to the full S0 class and, in particular, to its finite-fourth-moment subclass. The third and fourth identities play no role in this general contradiction.

### 3. Lemma 2: simultaneous coincidence and collinearity, lines 101–141

For bounded Borel $B$, choose $L>0$ bounding all differences of points in $B$. Empty or Lebesgue-null sets cause no exception to the integral estimates. The pair bound is
\[
\int_{B^2}D^{-1}\,d\mathbf x
\leq |B|\,4\pi\int_0^L r\,dr
=2\pi L^2|B|.
\]
For the triple integral, use $u=x_2-x_1$ and $v=x_3-x_1$. For $u\ne0$, write $v=ze+w$, $e=u/|u|$, and $s=|w|$. The volume element is $s\,d\theta\,ds\,dz$, whereas $|u\times v|=|u|s$. The cylinder used in the proof contains the relevant ball. Its integral is exactly bounded by $4\pi L^2/|u|$. Multiplying by the area-normalisation factor two and integrating $u$ gives
\[
\int_{B^3}A^{-1}\,d\mathbf x
\leq16\pi^2L^4|B|.
\]
Both factors and the powers of length are correct. The exceptional set $u=0$ is null. The estimate handles the neighbourhood of that set as well as neighbourhoods of collinearity; it does not assume a lower edge length.

All rearrangements use nonnegative integrands, so Tonelli applies before integrability has been proved. The resulting bound establishes finiteness rather than assuming it. With the intensity and second- and third-order full measure identities, the identity $N^3=(N)_3+3(N)_2+N$ gives finite third local count moments. This statement is a conditional local consequence and does not circumvent the separate global contradiction.

### 4. Theorem 3: stable coplanar family, lines 143–235

At the reference square, all six edges are positive and all four triangular areas equal $1/2$. The chosen base triple has nonzero cross product. Continuity permits sufficiently small base neighbourhoods and a uniform $\delta>0$ for which the cross-product norm $C$ stays in $[1/2,2]$, the fourth point remains near the fourth square vertex, and all the stated edge, face-area and diameter bounds hold. These are strict geometric margins, not merely a property of one null configuration.

For each fixed base triple, $e,f,n$ form an orthonormal basis. The map
\[
(s,t,h)\longmapsto p+se+tf+hn
\]
therefore has absolute Jacobian one. Its dependence on the base triple causes no extra factor: Fubini/Tonelli integrate the fourth point conditional on that fixed base. Equivalently, the full change of variables has block triangular derivative with the same absolute determinant. Both $p-x_1$ and the two tangential basis vectors lie in the base plane. Hence
\[
|\det(x_2-x_1,x_3-x_1,x_4-x_1)|=C|h|,
\qquad V=C|h|/6.
\]
The factor six is correct. For every such base triple, the fourth-point integral contains
\[
\frac{6}{C}(2\delta)^2
\int_{0<|h|<\delta}\frac{dh}{|h|}=\infty.
\]
The base family has positive nine-dimensional measure. Its dependence on the base triple is continuous, hence measurable, so Tonelli establishes the claimed full divergence.

Translation and a sufficiently small positive dilation place the entire family inside any given nonempty open ball. The product measure scales by $r^{12}$ and $V^{-1}$ by $r^{-3}$, giving $r^9$. Multiplication by this finite positive factor preserves an infinite integral. The distance and area lower bounds remain positive after any one such dilation, though they depend on the ball, exactly as stated.

An almost-everywhere density identity is sufficient. Changing a nonnegative density on a Lebesgue-null set leaves every extended Lebesgue integral unchanged; no subtraction of infinite quantities is used. Removing exactly $h=0$ does not remove the divergent integral. Additional nonnegative factorial mass elsewhere cannot cancel it. Thus
\[
\mathbb E(X(B))_4=\infty,
\qquad \mathbb EX(B)^4=\infty,
\]
using $N^4\geq(N)_4$. This conclusion uses no independence or stationarity. It contradicts a finite-fourth-moment requirement and does not itself contradict an almost surely finite count with finite mean.

The remarks on other geometric thresholds are appropriately conditional. Lower bounds on edges or face areas do not help when they still admit the displayed family. The proof does not claim that every arbitrary numerical combination of thresholds admits it. An upper diameter bound by itself also allows a scaled copy if all sufficiently small scales remain admitted.

Finally, the null-set claims are correct. For a distinct pair, the collinearity locus for the third point is a line; for a noncollinear triple, the coplanarity locus for the fourth point is a plane. Handling the already-null lower-order exceptional sets first and then applying Fubini proves nullity in the full product spaces. Full absolute continuity makes the corresponding factorial measure zero. The nonnegative tuple count on each bounded ball then vanishes almost surely, and a countable ball exhaustion gives the asserted global absence. Infinite expected numbers of nearly coplanar tuples are consistent with this absence of exactly coplanar tuples.

### 5. Theorem 4: whole-space counterexample to a moment inference, lines 237–334

The mark distribution $\mathbb P(N=n)=cn^{-5}$ is normalised by a finite positive constant. Its first, second and third raw moments are finite; its fourth factorial moment is infinite because $n^{-5}(n)_4$ is comparable to $n^{-1}$ for large $n$. The chosen parent intensity $\kappa=\lambda/\mathbb EN$ is finite and positive for every prescribed $\lambda>0$.

A homogeneous Poisson process with finite intensity on $\mathbb R^3$ exists and is countable almost surely. Marking each parent independently with a finite integer and a finite sequence of independent diffuse displacements gives a well-defined whole-space cluster process. All cluster radii are at most $1/10$. Therefore only the finitely many parents in a bounded enlargement can contribute to a fixed bounded observation set, and each contributes a finite cluster. This proves local finiteness before any moment calculation. Conditional on parent positions and integer marks, every pair of offspring positions has zero probability of coincidence; the countable union over all pairs proves simplicity. Translation covariance with stationary parents proves strict stationarity.

Tonelli and $\int f_n(x-z)\,dz=1$ give the exact first moment $\kappa\mathbb EN\,|B|=\lambda|B|$. No limiting approximation or intensity restriction is involved.

For bounded $B$, a deterministic bounded parent region suffices for the domination by $Z=\sum_{j=1}^{M}N_j$. Expanding the cube by equal, double and distinct parent indices gives the three displayed terms with coefficients $1,3,1$. Finite mark third moment and finite Poisson moments imply $\mathbb EZ^3<\infty$. For a nonempty ball, all sufficiently small high-mark clusters centred in its concentric half-ball fit entirely inside it. Keeping only their within-cluster ordered quadruples gives the infinite harmonic-series lower bound. This argument works at every positive ball radius and every prescribed positive intensity.

The factorial density formula also checks out. Every ordered tuple of distinct offspring has a unique partition according to its parents. For a block of size $j$ and mark $n$, the ordered selection factor is $(n)_j$. Distinct blocks correspond to distinct parents. Ordering the blocks, for example by their least label, and using the Poisson factorial measure $\kappa^q\,dz_1\cdots dz_q$ produces exactly one factor $\kappa$ for each block. There is no missing or extra $q!$. Integrating independent marks and offspring gives the displayed $K_j$ and the sum over all set partitions. All operations are nonnegative sums or integrals and thus remain legitimate for infinite high-order moments.

For an explicit partition-count check, the fourth-order formula contains one four-point block, four triple-plus-singleton terms, three pair-plus-pair terms, six pair-plus-two-singleton terms and one all-singleton term. It therefore includes both within-cluster contributions and the full background contributions. In particular, the second-order density is $K_2+\lambda^2$ and the third-order density is $K_3+\lambda\sum K_2+\lambda^3$.

For a block of at least two distinct points with diameter $d>0$, a nonzero integrand requires $d\leq2r_n=1/(5n)$. Only finitely many positive integers $n$ can contribute. Each associated parent integral is finite, since
\[
\int\prod_{i\in I} f_n(x_i-z)\,dz
\leq\|f_n\|_\infty^{j-1}\int f_n(x_{i_0}-z)\,dz
=\|f_n\|_\infty^{j-1}.
\]
The singleton factor is $K_1=\lambda$. The finite partition sum is consequently finite at every pairwise distinct tuple, at each finite order. This proves the stronger pointwise-off-diagonal assertion, not merely finiteness almost everywhere. The explicit nonnegative measure identity proves full absolute continuity even though some bounded sets have infinite measure. Density values on diagonals may be reassigned without changing any measure.

The auxiliary example is not accidentally an S0 solution: for pair separation greater than $1/5$, $K_2=0$ and its full pair density equals $\lambda^2$. Its purpose and limitations are correctly stated. It disproves the implication from infinite fourth local moments to failure of local finiteness, finite intensity, finite third local moments, or existence of genuine finite-almost-everywhere full densities. It does not decide joint realisability of the reciprocal kernels on a bounded domain.

### 6. What was and was not checked

The whole mathematical submission, including its auxiliary construction and amendment discussion, was checked. Whole-space process existence, positive prescribed intensity, exact constants and geometric Jacobians, all partitions, null and singular sets, and justifications for sums and integrals were included. No simulation, empirical comparison, numerical continuum certification or formal proof assistant was used or needed. The report does not certify novelty, historical exercise wording, current open status, or the author's administrative/accounting record. It does not investigate a different construction track or prove a replacement problem.

## Finding register

| ID | Location | Precise mathematical issue or checked obligation | Consequence | Repair/status |
|---|---|---|---|---|
| R2-01 | Theorem 1, lines 63–94 | The full pair identity itself yields finite second count moments, followed by an incompatible large-ball moment inequality. | General non-existence for every positive intensity in S0, with no hidden fourth-moment or mixing assumption. | Verified; no repair required. |
| R2-02 | Lemma 2, lines 103–139 | Coincidence and collinearity singularities are integrated together with the correct cylindrical Jacobian and area factor. | Finite second and third local moments follow under the corresponding full identities. | Verified; no repair required. |
| R2-03 | Theorem 3, lines 145–235 | A positive-measure family of nearly coplanar quadruples remains uniformly separated in edges and face areas, and has an infinite reciprocal-height integral. | A genuine finite-fourth-moment obstruction; no general local-finiteness contradiction follows from this calculation alone. | Verified; scope correctly qualified. |
| R2-04 | Theorem 4, lines 239–334 | The shrinking-cluster process is globally defined and its full measure formula contains every partition, despite infinite fourth moments. | The proposed auxiliary moment inference is false, including when genuine finite-almost-everywhere full densities are required. | Verified counterexample; no repair required. |
| R2-05 | Replacement discussion, lines 338–385 | A bounded geometric domain removes the premise of the proved global pair contradiction, but neither a particular cutoff nor existence on the retained domain follows. Restricting the third/fourth domains and adding moment or lower-threshold conditions are further choices. | No replacement-target success or uniquely necessary amendment can be certified. | Correctly labelled proposal; outstanding research/adoption obligations, not a defect in the non-existence proof. |
| R2-06 | Lemma 2 commentary, line 135 | “The first three S0 measure identities” can be read as referring to the three displayed factorial orders rather than intensity plus orders two and three. | Minor reading ambiguity; the deduction is valid under either stronger interpretation, but its minimal dependencies should be explicit. | Optional wording: “The intensity and the second- and third-order full measure identities imply ...”. No author edit made. |

## Amendment implications

The logically forced conclusion is that the unrestricted full pair identity $a_2/|x-y|$ cannot coexist with positive constant intensity. For every bounded observation set with finite second moment, any candidate must obey
\[
\alpha^{(2)}(B^2)\geq\lambda_0^2|B|^2-\lambda_0|B|.
\]
The exact global reciprocal pair measure violates this on large balls. Restricting only the fourth-order domain cannot repair that violation. To preserve S0's other fixed commitments, at least the domain on which the full pair identity is imposed must change. The theorem does not force an upper cutoff, a specific numerical value, or a common cutoff for all three orders; it does not exclude every unbounded prescribed domain.

The proposed statement at lines 364–373 is mathematically clear: for each prescribed pair $(\lambda_0,M)$ with both positive and $M$ finite, all three exact reciprocal identities are required on nondegenerate tuples of diameter less than $M$, and the full absolutely continuous densities elsewhere are left unprescribed. It retains positive prescribed intensity, full densities, all orders and exact equality. Its upper bound prevents the argument in Theorem 1 from computing the entire second factorial moment of arbitrarily large balls. This avoids that proof's premise, but is not a sufficiency result.

The common cutoff for orders three and four is a non-unique design decision. The global second-order proof directly necessitates no such change to those orders. Choice of $M$, the strict boundary convention, and whether to prescribe $M$ independently of intensity must be stated in an adopted question. The author does explicitly preserve the independently prescribed $M$ and all-intensity quantifiers. A future result at only some intensities or with $M$ dependent on intensity would not answer that proposal as written. Neither dilation nor the auxiliary example has been claimed to settle those quantifiers.

If the proposed bounded-domain law holds, Theorem 3 forces infinite fourth local moments on every sufficiently small ball. In fact the consequence extends to every nonempty open ball, since it contains a smaller ball of diameter below $M$ and counts are monotone. This strengthening does not create a contradiction in the proposal's stated broad moment class.

For a separate finite-fourth-moment question with retained fourth-order domain $E_4$, a necessary kernel condition is
\[
\int_{B^4\cap E_4}V^{-1}\,d\mathbf x<\infty
\quad\text{for every bounded }B.
\]
This only addresses the prescribed contribution: unspecified contributions must also have finite local integrals, and point-process realisability remains an additional obligation. A positive volume threshold ensures finiteness of the retained contribution on bounded products. Appropriate altitude restrictions or other narrowing of the domain can also do so. None is proved uniquely necessary. Local integrability of $1/D$ and $1/A$ means the present local analysis supplies no reason to require positive distance or triangle-area cutoffs. A lower edge or face-area bound alone fails when the stable square family remains allowed.

Most importantly, Theorem 3 does not compel a finite-fourth-moment assumption or a positive lower altitude/volume threshold in S0's broad class. The author's finite-moment variant is a separate proposed question. Its adoption must be distinguished from a general necessity proved for S0. Theorem 4 explains why this distinction matters but does not show that the particular reciprocal-volume law is realisable locally.

Under the run's obstruction gate, the reviewed general contradiction can support consideration of a precisely documented domain revision within its scope. This review neither chooses nor adopts one. Changes to exactness, full-density interpretation, orders or prescribed intensity require the specified owner authority. A construction-driven amendment after unsuccessful attempts follows its separate approval route. No choice or approval can be inferred from this submission or from the review verdict. S0 remains the active hashed target until a new statement is properly adopted and broadcast.

## Source and coding evidence

The mathematical evidence is the frozen proof and the independent calculations recorded above. S0, the frozen common context, the source index, and the proof-standard and writing-style references were read. The review packet's allowed-file hashes were independently recomputed and matched. The report and proof hashes were rechecked when the review was frozen.

No external theorem citation is essential. The elementary inputs are nonnegative integration and change of variables, the raw/factorial count identities, the second-moment inequality, and elementary Poisson process facts. For the last, the parent factorial measure follows from independent Poisson counts on disjoint sets and $\mathbb E(M)_q=\theta^q$, with finite partitions and monotone extension. Independent marking then gives the displayed cluster formula. These dependencies and their use were reconstructed above. No unverified historical attribution or claim of novelty is used.

No additional primary source, literature-agent request or coding-agent request was necessary. No numerical or symbolic experiment was executed. Hashing and runtime metadata checks are administrative evidence rather than mathematical certification.

## Presentation judgement

The submission is readable and mathematically organised. It separates the decisive global obstruction from the local moment analysis, explains why the auxiliary example is included, and repeatedly identifies the limits of the proposed replacements. Constants, ordered tuples, full measures and almost-everywhere qualifications are sufficiently explicit. The full argument can be followed without the author's notes.

The only suggested wording repair is R2-06. It would also help a later statement-change document to distinguish in a short list the part of a proposed domain change motivated by the global pair obstruction from additional common-domain or finite-moment choices. That is a presentation aid to decision-making, not a missing hypothesis in the proved results. No presentation issue prevents acceptance of the mathematical obstruction.

## Review summary and remaining obligations

The global count inequality supplies the S0 verdict. The local geometric calculation and the full-density cluster example jointly establish that the fourth-moment issue has a different logical scope. The claimed theorems and lemma survive the full audit; no substantive author repair is required for this submission's non-existence conclusions.

The remaining obligations concern future work: adopt any replacement through the prescribed version/hash/authority/broadcast procedure; prove its joint cross-order realisability at every prescribed intensity and any independently prescribed geometry; and, if a finite-moment subclass is selected, justify the full local moment conditions rather than only the retained kernel's integrability. None of those obligations is represented as complete here. No amendment, new attempt, or cross-track synthesis has been performed.

## Accounting handoff

This reviewer's own session record is `[local path omitted]`. Only matching session metadata, turn metadata and token-count events were extracted. Private reasoning and conversation records were not inspected. Session metadata line 1 matches the reviewer's environment thread ID; turn-context line 8 reports `gpt-6-astra` and `xhigh`.

The preflight checkpoint, token-count event line 32 at `2026-10-20T16:54:24.635Z`, reports cumulative input 160327, cached input 150016, cache-write input 0, output 864, reasoning output 0, and total 161191. These are runtime values, not estimates. They cover the session prefix through that event, not the completed review. Subsequent available checkpoint data are recorded separately in the assigned review directory. Cumulative snapshots must not be summed; reasoning must not be added again to any inclusive output total. Child-usage inclusion semantics are NR; no child was spawned.

Final turn totals, the end timestamp and final elapsed duration are NR at manuscript freeze and should be reconciled by the coordinator after turn completion. No model-cost estimate or actual account charge is asserted. The frozen report records mathematical proof and decision summaries, not private chain-of-thought.
