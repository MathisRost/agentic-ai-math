# Review — nonexistence_1 / submission v02 / active target S0

- Type: fresh independent, whole-submission correctness review and separate proposed-statement scope audit.
- Reviewer: `/root/review_nonexistence_1_v02`, session `session-06`.
- Requested and verified runtime: `gpt-6-astra`, `xhigh`. Before mathematical work, `CODEX_THREAD_ID` was matched to the reviewer's own `session_meta.id`; the corresponding `turn_context` explicitly reports `model: gpt-6-astra`, `effort: xhigh`.
- Own session record: `[local path omitted]`. Session start: `2026-10-20T17:08:28.729Z`; turn context: line 8, `2026-10-20T17:08:30.775Z`; turn ID: `turn-09`.
- Setup root: `$SETUP`.
- Run root: `runs/20261020T164437Z_astra6`, relative to that setup root.
- Active target: `statements/S0.md`; SHA-256 `3b5b5ad81bf56136bd79f0fde2d4aa39e3bed32aaf37511460007dfb0fc656f0`.
- Dispatch: `packets/review_nonexistence_1_v02.json`; SHA-256 `f40847b1bfe7fda0b0009548355919e0e60f9742eed17f7bd1f999178ad43453`.
- Reviewed cumulative proof: `reviews/nonexistence_1_v02/proof_snapshot.md`; SHA-256 `ad71fa86b829615c109ffaebd80b65c40298e12b59cb399b29a669096142754b`.
- Separately reviewed proposal: `proposals/S1_diameter_v01.md`; SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`; status supplied by the packet: **NOT ADOPTED**.
- All files listed in the dispatch were independently hash-verified. The frozen instructions, workflow, common mathematical context, templates, and complete proof-reviser skill and mandatory references were read.
- Excluded: other tracks, author/coordinator conversations, private notes, prior review files, starting information, old runs and other chats. The supplied cumulative proof itself contains references to favourable previous reviews and a response-to-review table. Those embedded assertions were not treated as evidence; all mathematical claims assessed here were re-established from the included arguments. Thus the review has a fresh context, but the supplied manuscript was not fully blinded to historical verdict language.
- Output ownership: only `reviews/nonexistence_1_v02/`. No delegation, source alteration or target adoption.

## Correctness verdict and scope

**The reviewed informal argument establishes the advertised general fourth-order tail obstruction and all the retained mathematical results. No unresolved correctness gap was found in the whole cumulative proof. S0 is false for every prescribed positive finite intensity.**

The principal theorem is stronger than the negation of S0's fourth-order requirement. For any stationary, simple, locally finite process on $\mathbb R^3$ with $0<\lambda<\infty$, no finite $a>0$ and $R_0\geq0$ can satisfy
\[
\alpha^{(4)}(E)\leq a\int_E V(\mathbf x)^{-1}\,d\mathbf x
\]
for **every** Borel subset of $\{V>0,\operatorname{diam}>R_0\}$. No lower-order density or finite higher count moment is assumed. The measure on coplanar configurations and on configurations below the diameter threshold is unrestricted by this theorem.

Independently, the full unrestricted pair and triangle identities are impossible even if stationarity is replaced by the homogeneous mean-measure condition. The pair-tail theorem also rules out uniformly vanishing full pair-measure bounds at large separation, regardless of unrestricted short-range moments. The local fourth-order calculation proves an infinite fourth count moment; by itself it does not prove failure of almost-sure local finiteness.

The proposed S1 is a clear and different existence question. A common finite upper diameter for the **formula domains** removes the hypotheses of the audited global obstructions. It is a non-unique domain choice, with neither existence nor optimality established. Its finite-fourth-moment comparison has a negative answer. This report does not adopt S1 or convert an S1 result into an S0 result.

## Reconstruction and detailed audit

### 1. Target, measures and quantifiers

S0 asks, for every prescribed $\lambda_0>0$, for one whole-space stationary simple locally finite process, with positive finite constants $a_2,a_3,a_4$ chosen with the process, satisfying all three full factorial-measure identities. Since the arguments exclude each law separately for every possible finite positive coefficient, dependence of the coefficients on the intensity does not evade the obstruction.

Here a factorial expectation measure means the expectation of the random counting measure on **ordered pairwise-distinct tuples**. It is an extended nonnegative measure. This definition does not require finite bounded-set mass, and neither does the new tail argument. Tonelli may therefore be used before proving integrability.

Equality of full measures is essential. A formula for an absolutely continuous component with additional singular mass would not justify the direct pair and triangle upper bounds. For Theorem 1, it is sufficient to dominate the restricted full fourth measure on its stated domain; singular mass outside that domain is harmless to the argument. In particular, allowing coplanar mass cannot invalidate the contradiction because every selected product of cubes consists entirely of noncoplanar configurations.

The proof constructs no candidate point process, so there is no construction-existence or representation claim to check. It begins with an arbitrary hypothetical process in the advertised class and obtains a contradiction. Cluster partitions, parent allocations and factorial-cumulant conversions are not used. The identity for products of counts on disjoint cubes includes all ordered tuples directly.

### 2. Fourth-order tail obstruction: bounded random variables

Theorem 1 is at proof lines 38–46; its argument is at lines 48–133.

Let $Q_z=z+[0,1)^3$ and $I_z=\mathbf1_{\{X(Q_z)>0\}}$. Homogeneous finite positive intensity gives $\mathbb E X(Q_0)=\lambda>0$, hence
\[
p=\mathbb P\{X(Q_0)>0\}>0.
\]
If $p=0$, the count would vanish almost surely and have expectation zero. Translation stationarity gives the same $p$ for every integer translate. No independence or ergodicity is inferred.

For integer $m$, the partition of $U=[0,1)^3$ into $m^3$ half-open cubes has cell volume $m^{-3}$. Thus
\[
Y_m=\int_U I_{\lfloor mu\rfloor}\,du
    =m^{-3}\sum_{z\in\{0,\ldots,m-1\}^3}I_z
\]
is exactly as stated, lies in $[0,1]$, and has mean $p$. Jensen gives $p^4\leq\mathbb E Y_m^4$. Expanding the fourth power as an integral over $U^4$ and interchanging expectation and integration is justified either by bounded Fubini or by Tonelli. The repeated-cube terms are present at this stage; they are not incorrectly treated as factorial tuples.

This replacement of counts by indicators is decisive. No fourth-moment bound for $X(Q_z)$, $X([0,m)^3)$, or a union of the selected cubes is required.

### 3. Small-volume set and the uniform geometric estimate

The determinant-zero set in $U^4$ is Lebesgue-null. The proof's fibre argument covers all possibilities: coincident first two vertices form a null set; conditional on a distinct pair, the collinear third vertex has a line as its possible locus; conditional on a noncollinear base, the fourth vertex must lie in a plane. Tonelli/Fubini on the bounded product space proves nullity.

The sets $B_\varepsilon=\{V\leq\varepsilon\}$ decrease to $\{V=0\}$ as $\varepsilon\downarrow0$. Since $|U^4|=1$, continuity from above gives $b_\varepsilon=|B_\varepsilon|\to0$. No estimate on $\int_{B_\varepsilon}1/V$ is asserted or needed; that integral may be infinite.

I independently checked the constant in (4). If all $u_i,w_i\in U$ and $\max_i\|w_i-u_i\|\leq\delta$, each edge vector has length at most $\sqrt3$ and each changed edge has length at most $2\delta$. The exact column-telescoping formula is
\[
\begin{aligned}
\det(b_1,b_2,b_3)-\det(a_1,a_2,a_3)
={}&\det(b_1-a_1,b_2,b_3)\\
&+\det(a_1,b_2-a_2,b_3)
+\det(a_1,a_2,b_3-a_3).
\end{aligned}
\]
Each term is bounded in absolute value by $6\delta$. After applying $||s|-|t||\leq|s-t|$ and dividing by six, the result is precisely
\[
|V(\mathbf w)-V(\mathbf u)|\leq3\delta.
\]
The half-open boundary convention does not alter the bound.

If $y_i\in Q_{\lfloor mu_i\rfloor}$, then $w_i=y_i/m\in U$ and $\|w_i-u_i\|\leq\sqrt3/m$. For $V(\mathbf u)>\varepsilon$ and $m>6\sqrt3/\varepsilon$,
\[
V(\mathbf y)=m^3V(\mathbf w)>\varepsilon m^3/2.
\]
This is uniform over **every point of the entire product of cubes**, not just their centres or almost every selected tuple.

Two selected cubes cannot coincide: choosing equal corresponding $y_i$ would give zero volume, contradicting the uniform bound. Distinct half-open lattice cubes are disjoint. Also,
\[
V(\mathbf y)\leq\operatorname{diam}(\mathbf y)^3/6,
\]
because each of the three edges based at $y_1$ has length at most the diameter. Therefore every selected tuple has diameter greater than $(3\varepsilon)^{1/3}m$. For fixed $\varepsilon$, one further lower bound on $m$ places all these products in the tail domain. Both size conditions are uniform in $\mathbf u\in G_\varepsilon$.

### 4. Full-measure bound and contradiction

On four distinct cubes, each choice of one point per cube is an ordered pairwise-distinct quadruple. Hence, as an identity of nonnegative expectations,
\[
\mathbb E\prod_{i=1}^4X(Q_{z_i})
=\alpha^{(4)}(Q_{z_1}\times\cdots\times Q_{z_4}).
\]
There is no missing diagonal correction or combinatorial factor. Each factor cube has volume one. Theorem 1's full restricted-measure domination, and the uniform volume lower bound, imply
\[
\mathbb E\prod_{i=1}^4I_{z_i}
\leq\frac{2a}{\varepsilon m^3}.
\]
An extended expectation is permissible before this inequality; the inequality itself establishes finiteness on the selected products.

On $B_\varepsilon$, the indicator product is at most one, including repeated-cube cases. Consequently
\[
p^4\leq b_\varepsilon+\frac{2a}{\varepsilon m^3}.
\]
The order of choices is correct: first choose a fixed $\varepsilon>0$ with $b_\varepsilon<p^4/2$, then let $m\to\infty$ through integers meeting the two uniform lower bounds. This contradicts $p>0$. No random-limit exchange, moment truncation, or uncountable almost-sure assertion is hidden in this final step.

Thus the fourth-order proof remains valid even if arbitrary fourth factorial mass is allowed near coplanarity, at short diameters, or on the coplanar set itself. What is ruled out is the stated uniform reciprocal-volume upper bound on the full noncoplanar tail.

### 5. Pair law and pair tail

For $v=4\pi/3$ and $N_R=X(B(0,R))$, the full pair density gives
\[
\mathbb E(N_R)_2
\leq a_2|B_R|\int_{|h|<2R}|h|^{-1}\,dh
=8\pi a_2vR^5.
\]
The constant is correct: $4\pi\int_0^{2R}r\,dr=8\pi R^2$. The integrable singularity at coincidence and the full-measure identity justify the finite bound. Therefore $\mathbb E N_R^2=\mathbb E(N_R)_2+\mathbb E N_R<\infty$, and Jensen yields
\[
\lambda^2v^2R^6\leq8\pi a_2vR^5+\lambda vR^3,
\]
which is impossible as $R\to\infty$. This argument requires homogeneous mean measure, not stationarity of the law.

For the separate pair-tail argument, at each fixed $\eta>0$ let $L_\eta$ be a separation beyond which the full pair measure is dominated by $\eta\,dx\,dy$. The number of ordered lattice cube pairs in an $m$-box with centre distance at most $L_\eta+\sqrt3$ is at most $C_\eta m^3$, where $C_\eta$ is a finite number of lattice offsets independent of $m$. Centre separation beyond this distance puts every point pair beyond $L_\eta$, since the difference of two offsets in unit cubes has norm at most $\sqrt3$.

The distant products have expected indicator product at most $\eta$; the remaining products have the bound one. Diagonal terms are covered by the displayed $(1+C_\eta)m^3$ bound, even if this harmlessly overcounts them. Jensen then gives
\[
p^2\leq (1+C_\eta)m^{-3}+\eta.
\]
Taking $m\to\infty$ at fixed $\eta$, and then $\eta\downarrow0$, proves the contradiction. For an exact reciprocal tail, choose the distance large enough that $a_2/D\leq\eta$. Arbitrary short-range second moments cause no problem because indicators are used there.

### 6. Triangle law

The triangle calculation is independently correct. With $u=x_2-x_1$ and $w=x_3-x_1$, the Jacobian of this translation is one and $A=|u\times w|/2$. After enlarging the relative-coordinate domains to balls of radius $2R$, polar coordinates give
\[
\begin{aligned}
\int_{B_R^3}\frac{d\mathbf x}{A}
&\leq |B_R|\,2(4\pi)(2\pi)
\left(\int_0^{2R}r\,dr\right)^2\int_0^\pi d\theta\\
&=64\pi^3vR^7.
\end{aligned}
\]
The angular factor $\sin\theta$ cancels its reciprocal, and each radial integral is $2R^2$. Coincident and collinear configurations are null. Tonelli justifies the nonnegative calculation before its finiteness is known.

For integers $N\geq0$, $(N)_3\geq(N-2)_+^3$; for $N\geq3$ this follows by comparing the three factors individually, and for $N\leq2$ both sides vanish. The map $t\mapsto(t-2)_+^3$ is convex. Its extended Jensen inequality is applicable to the integrable count $N_R$; the displayed finite factorial-moment upper bound also establishes the needed finiteness. Thus
\[
(\lambda vR^3-2)_+^3\leq64\pi^3a_3vR^7.
\]
Dividing by $R^9$ gives a positive limiting left side and zero right side. No pair law is used. The submission does not state a separate triangle-tail theorem; this review does not silently add one to the audited claims.

### 7. Local reciprocal-volume divergence

For any noncollinear triple in an open ball $B$, let its area be $A>0$, plane be $P$, and unit normal be $\nu$. The choice
\[
0<\delta<\operatorname{dist}(x_1,B^c)/\sqrt2
\]
ensures the cylinder $x_4=z+t\nu$, $|z-x_1|<\delta$, $|t|<\delta$ lies in $B$: its displacement from $x_1$ has length less than $\sqrt2\delta$. The orthogonal-coordinate Jacobian is one, and
\[
V=A|t|/3.
\]
On $t\ne0$, the fourth point is distinct from all three base vertices and the tetrahedron is noncoplanar. Hence
\[
\int_{B\cap\{V>0\}}\frac{dx_4}{V}
\geq \frac{3\pi\delta^2}{A}
\int_{0<|t|<\delta}\frac{dt}{|t|}=\infty.
\]
The base triples with positive area have full measure in $B^3$. Tonelli therefore gives $\alpha^{(4)}(B^4)=\mathbb E(X(B))_4=\infty$, and $N^4\geq(N)_4$ gives $\mathbb E X(B)^4=\infty$.

An almost-everywhere density identity is sufficient: equality of full measures lets one integrate the geometric function directly, and changing a density on a null set does not alter its Lebesgue integral. The divergence is from noncoplanar points approaching the plane; it does not arise from assigning a nonzero value on the plane.

The example $\mathbb P(N=k)=c k^{-5}$, $k\geq1$, is correct: it defines a finite integer-valued random variable with finite first three moments and infinite fourth moment. It demonstrates the logical distinction only; it is not a spatial realisation. The submission correctly keeps this finite-moment obstruction separate from its general fourth-order tail obstruction.

## Finding register

The register includes affirmative checks and scope obligations as well as presentation points; no invalid mathematical inference was identified.

| ID | Location | Precise issue or check | Consequence | Repair/status |
|---|---|---|---|---|
| RV2-01 | Proof lines 48–85 | The occupancy average is bounded, has positive stationary mean, and admits the stated fourth-power integral; coplanarity is Lebesgue-null. | No finite fourth count moment or mixing assumption enters. | Verified. |
| RV2-02 | Proof lines 87–111 | The $3\delta$ perturbation constant, $m>6\sqrt3/\varepsilon$ condition, distinctness of cubes, and diameter lower bound all hold uniformly. | Restricted tail domination applies to entire selected product sets. | Verified; determinant expansion supplied above. |
| RV2-03 | Proof lines 113–131 | Count products on disjoint cubes equal the ordered factorial count; the integral bound is $2a/(\varepsilon m^3)$; the limits have the proper order. | Establishes the general fourth-order tail theorem, including unrestricted coplanar and short-range mass. | Verified. |
| RV2-04 | Proof lines 135–171 | Pair integral constant and pair-tail near-cube count are correct. | Pair law alone excludes S0; short-range alterations alone cannot repair a reciprocal pair tail. | Verified independently of prior verdicts. |
| RV2-05 | Proof lines 173–203 | Triangle Jacobian, angular cancellation, $64\pi^3vR^7$ bound, and factorial Jensen inequality are correct. | Triangle law alone excludes S0 under homogeneous mean measure. | Verified. |
| RV2-06 | Proof lines 205–229 | Cylinder fits inside the ball; $V=A|t|/3$ gives logarithmic divergence. | Infinite fourth moments follow locally; almost-sure local finiteness is not contradicted by this calculation alone. | Verified; class distinction must remain explicit. |
| RV2-07 | Proof lines 231–258; S1 domains | Global obstructions require a change to each unrestricted law if the process class is retained; they do not single out a common cap. | S1 is an admissible candidate domain revision, not a necessary, sufficient or maximal repair. | No proof repair; document the non-unique decision at adoption. |
| RV2-08 | S1 lines 29–38 and 69–71 | Global finite-a.e. densities are explicit even outside formula domains. This is automatic in S0 but is stronger than merely allowing arbitrary extended-valued densities there. | The retained global measure regularity must be visible; it does not imply finite bounded-set fourth mass. | No hidden strengthening relative to S0; state the retention in the amendment record. |
| RV2-09 | S1 lines 5–19 and 83–88 | $\lambda_0$ and $M$ are independent universal parameters; process and coefficients may depend on both. | A low-intensity fixed-domain result or rescaling without joint parameter control is partial. | Quantifiers are clear; future construction obligation remains. |
| RV2-10 | S1 lines 67–81 | All nearly coplanar shapes occur inside sufficiently small balls. | The finite-fourth-moment comparison is false; extended-moment existence remains unresolved. | Record the negative comparison explicitly; do not introduce a shape cutoff by inference. |
| RV2-11 | Proof lines 7–11, 23, 262, 286–294 | Assigned manuscript contains previous-verdict labels and review responses. | Packet was not perfectly blinded, though no previous review was read or used. | Future fresh-review snapshots should separate administrative review history from mathematical text. |
| RV2-12 | S1 title and final paragraph | The proposal file itself lacks a prominent “proposed, not adopted” status and authority/hash record; the dispatch supplies that status. | No ambiguity in this review, but a standalone reader could mistake a filename/version for adoption. | Add status in a separately frozen proposal revision or companion change record; do not alter this reviewed snapshot. |

## Amendment implications

### What follows from the proof

With the original process class, positive finite prescribed intensity, finite positive coefficients and full-measure interpretation retained:

1. None of the three reciprocal laws can hold on its entire nondegenerate configuration space.
2. The pair reciprocal law cannot be repaired only at bounded separations while it is retained on all sufficiently distant pairs.
3. The fourth reciprocal law cannot be repaired only at bounded diameters while it is retained on all sufficiently large noncoplanar quadruples. The stronger upper-bound hypothesis is already impossible.
4. Prescribing $a_4/V$ throughout noncoplanar quadruples in a ball forces an infinite fourth count moment.

Items 1–3 are general obstructions, without finite higher moments or representation hypotheses. Item 4 is the local finite-moment obstruction. None proves that a positive lower distance, altitude, area, volume or shape threshold is necessary in the broader extended-moment class.

### What S1 changes and retains

S1 replaces the full nondegenerate domain at each order by
\[
E_n(M)=\{0<\Delta_n,\operatorname{diam}<M\}
\]
for every independently prescribed finite $M>0$. It removes the identity requirement on all configurations with diameter at least $M$, for all three orders. These configurations remain possible in the process; the cap concerns only where formulas are required. Whole-space stationarity and local finiteness are unchanged.

S1 retains simultaneous exact equalities, all three orders, full rather than connected measures, absence of singular mass everywhere, all nondegenerate small-scale shapes, arbitrary prescribed positive intensity, and coefficients chosen with the process. It imposes no finite fourth-moment assumption.

Using one common $M$, allowing every positive $M$, retaining all shapes below it, and leaving all values above it unprescribed are design choices. The proof does not prefer these choices over unequal cutoffs by order or suitable unbounded selected domains. It does not establish that those alternatives are possible either. The surface $\operatorname{diam}=M$ is Lebesgue-null, so choosing a strict rather than non-strict boundary does not change a full absolutely continuous measure identity.

The finite-a.e. clause deserves explicit treatment. Under S0, every density is already finite almost everywhere because the prescribed reciprocal geometric function is finite off a null degeneracy set. S1 preserves this qualitative feature globally, including the now unprescribed region. Thus it is **not an extra assumption relative to S0**, and S1 remains a weakening of the original formula requirements. It is nevertheless stronger than a different proposed variant that would allow density $+\infty$ on positive-measure sets outside $E_n(M)$. The obstruction does not prove that this retained restriction is necessary for any modified problem.

With the no-singular-mass requirement, finite-a.e. densities make the factorial measures $\sigma$-finite: exhaust configuration space by bounded sets on which the density is bounded, together with its null exceptional set. This does not make them boundedly finite. In particular, it is consistent at the measure-theoretic level with the logarithmic local fourth-mass divergence; no finite-fourth-moment requirement is being smuggled in.

The independent parameter requirement is substantive. If space is dilated by $c>0$, then
\[
\lambda'=\lambda c^{-3},\qquad M'=cM,\qquad
a_n'=a_n c^{(n-1)-3n}=a_n c^{-(2n+1)}.
\]
Thus $\lambda M^3$ is invariant under spatial dilation. A construction covering only a restricted range of this dimensionless parameter cannot establish all independently prescribed pairs merely by rescaling. S1 states this obligation correctly.

Finally, if S1 held and $B$ were any ball with diameter less than $M$, the local fourth-moment calculation would apply throughout its noncoplanar quadruples. Consequently the separate requirement of finite fourth moments on every bounded Borel set is impossible. This does not settle S1 itself.

### Authority and remaining decision

The frozen AGENTS rules and `workflow.json` authorise coordinator-led **domain revisions supported by reviewed general obstructions within their scope**. The audited proof supplies such general obstructions at every order, including a fourth-order obstruction which does not rely on a finite-moment subclass. Accordingly, the specific common finite-diameter replacement is within that delegated domain-revision route, provided the coordinator records the non-unique choice, all losses and retentions above, the supporting frozen proof/review hashes, and the exact adopted statement and broadcast.

There is no need to invoke the separate three-failed-construction owner-amendment route solely to choose this cap under the existing obstruction authority. This is an assessment of the authority supplied in the packet, not an adoption or an owner approval. As of this review, S0 remains active and S1 remains proposed.

The coordinator cannot claim that the proof forces a common finite cap, proves S1 feasible, or makes its scope maximal. Any later change to exactness, full densities, the three orders, or prescribed intensity requires explicit owner approval under the frozen workflow. A finite-moment restriction or an extra shape exclusion cannot be justified for the broad S0/S1 class merely by the local divergence calculation. A pragmatic change after failed constructions must follow its separate owner gate, with no automatic reset of attempts.

Before S1 can govern dispatches, the remaining action is an explicit coordinator adoption decision and the required frozen amendment/broadcast record. No such record was supplied, and none is inferred from the proposal, a previous proof, or this review.

## Source and coding evidence

The mathematical audit is self-contained. Its dependencies are the supplied factorial-measure definition, elementary Euclidean geometry, the determinant bound, nonnegative or bounded integration, continuity from above of finite Lebesgue measure, and Jensen's inequality with its hypotheses checked above.

The supplied neutral source index and DVJ context were read. No specialised external theorem, historical claim or present literature-status claim is needed for the proof. No primary PDF or external website was consulted, and no attribution to DVJ or Kagan is being certified by this report.

Tool use was limited to reading the assigned files, checking SHA-256 hashes, inspecting the reviewer's own identified runtime metadata, and writing/freezing this report and its accounting manifest. No numerical experiment, symbolic-package output or proof-assistant result supports the verdict. The constants and consequential inequalities were checked analytically as displayed above. No source or coding request is outstanding.

## Presentation judgement

The proof is readable and sufficiently detailed for the claimed result. It identifies the obstacle caused by local reciprocal-volume divergence and explains why bounded occupancy overcomes it. In particular, the uniformity over all points of each product cube, the order of limits, and the distinction between extended moments and almost-sure local finiteness are made visible.

Useful improvements are limited:

- Separate prior-review administration from future fresh mathematical snapshots. Section titles such as “pair obstruction” and “triangle obstruction” would be sufficient; the historical adjective “reviewed” is not mathematical support.
- Retain the explicit statement that the domain hypothesis concerns the restricted full measure, including any singular mass there.
- In an adopted-statement record, list global finite-a.e. density as a retained S0 property, and state the negative finite-fourth-moment comparison.
- Mark the S1 file or its inseparable companion record clearly as proposed until adoption, with authority and broadcast information.

These are presentation and audit-trail recommendations, not repairs to an invalid proof.

## Review summary and remaining obligations

The decisive fourth-order estimate is valid uniformly on a large subset of normalised cube locations, and the complementary subset has arbitrarily small Lebesgue measure. Bounded occupancy gives a positive fourth-power lower bound without any higher-moment assumption. The required tail domination makes the upper bound vanish, yielding a contradiction. The cumulative pair, pair-tail, triangle and local fourth-moment arguments are also valid with their advertised scopes.

No mathematical repair is required for the cumulative obstruction submission. The full S0 question has a negative answer for every prescribed positive finite intensity. Existence under S1, or under any other replacement, is not established. The finite-fourth-moment version of the displayed S1 is impossible. Selection, freezing and broadcast of a new target remain coordinator actions; no target has changed through this review.

## Accounting handoff

Own runtime telemetry exposes total and last usage fields for input, cached input, cache-write input, output, reasoning output and total tokens. An intermediate cumulative checkpoint, event line 69 at `2026-10-20T17:10:17.906Z`, reports:

| Runtime field | Exposed value |
|---|---:|
| `input_tokens` | 440738 |
| `cached_input_tokens` | 404608 |
| `cache_write_input_tokens` | 0 |
| `output_tokens` | 3361 |
| `reasoning_output_tokens` | 1569 |
| `total_tokens` | 444099 |

These are the runtime's cumulative values for this own session at that checkpoint, not completed-review totals and not values inferred from text length. Reasoning output is not added again to output. No children were launched; whether a parent session's counters include child usage is NR in this review. Completed-turn totals, final elapsed time and monetary charges are NR here and should be reconciled from the identified session after this turn ends. The freeze manifest records the final report hash and a later available metadata checkpoint without rewriting the frozen report.

This is an independent review, not a final cross-track synthesis. No other track or earlier review verdict has been assessed.
