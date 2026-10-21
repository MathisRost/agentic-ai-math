# Review — nonexistence_1 / submission v01 / target S0

- **Reviewer:** `/root/review_nonexistence_1_v01`, session `session-04`, turn `turn-07`.
- **Model and effort:** `gpt-6-astra`, `xhigh`, verified against this reviewer's own session metadata and `turn_context`; evidence is saved in `preflight.json`.
- **Session started:** 2026-10-20T16:53:34.336Z. **Report completed:** 2026-10-20T16:59:04.957304+00:00.
- **Type:** fresh independent review of one frozen submission, with no presumed verdict.
- **Setup root:** `$SETUP`.
- **Run root:** the setup root followed by `/runs/20261020T164437Z_astra6`.
- **Active target:** `statements/S0.md`, SHA-256 `3b5b5ad81bf56136bd79f0fde2d4aa39e3bed32aaf37511460007dfb0fc656f0`.
- **Reviewed proof:** `reviews/nonexistence_1_v01/proof_snapshot.md`, SHA-256 `15882b266ff83a90dacc1fd8cf19cab602bb0dde374b8d46451a16df40a24ec1`.
- **Review packet:** `packets/review_nonexistence_1_v01.json`, SHA-256 `0826bdf1236eb0fff5e9ebb2a76d9793870f4fb757e388dc8446657d5e196214`. Its hash and all 15 allowed-file hashes matched before the mathematical review.
- **Received context:** the packet's frozen instructions, workflow, common definitions and source index, review/change templates, target, proof snapshot, and frozen `mathis-proof-reviser` skill with its complete proof-standard and writing-style references.
- **Excluded context:** author conversation, author work/private notes, coordinator deliberations, other submissions, previous reviews, starting information, old runs, and other chats. No delegation occurred. The author's administrative claims about their own session/history were not independently inspected; they are not mathematical dependencies.

All paths below are run-relative unless stated otherwise. Line numbers refer to the frozen proof snapshot.

## Correctness verdict and scope

**The reviewed informal argument establishes general non-existence for S0, for every prescribed positive intensity.** The pair-density proof alone establishes a stronger statement: no simple, locally finite point process with homogeneous positive finite mean measure can have the stated full global second factorial measure, even without stationarity. It uses no unannounced moment, mixing, ergodicity, isotropy, or representation assumption. No correctness repair is required for that conclusion.

The three complementary results are also valid in their stated scopes:

| Result | Verified scope | Consequence |
|---|---|---|
| Global pair law | Homogeneous positive finite mean measure; full pair law at all positive distances | Impossible for every finite positive coefficient |
| Uniformly vanishing pair tail | Stationary positive finite-intensity process; tail measure domination, arbitrary short-range pair measure | A lower-distance cutoff alone cannot repair the global reciprocal pair tail |
| Global triangle law | Homogeneous positive finite mean measure; full triangle law at every noncollinear triple | Impossible independently of the pair law |
| Local reciprocal-volume law | The prescribed fourth measure on all noncoplanar quadruples in an open ball | Infinite fourth factorial and ordinary count moments in that ball |

The fourth result is **a moment-class obstruction**, not a second general proof against S0's extended-moment class. The submission keeps that distinction correct. The proposed finite-diameter question is well specified as a question; its feasibility is not established. This review neither adopts that proposal nor approves a target amendment.

The entire mathematical submission, including its amendment discussion and stated limitations, was audited. This is a mathematical correctness review, not a proof-assistant certification, a novelty search, or a cross-track synthesis.

## Reconstruction and detailed audit

### 1. The target, quantifiers, and measure convention

S0 asks, for each fixed $\lambda_0>0$, for one stationary, simple, locally finite process with mean measure $\lambda_0\,dx$ and some positive finite constants $a_2,a_3,a_4$ satisfying all three full factorial-density identities. The constants need not be prescribed independently of the process. A contradiction for every pair $(\lambda_0,a_2)$ with both entries positive and finite therefore suffices to refute S0 for each intensity; there is no need to derive an incompatible joint choice of all three constants.

The factorial measures are expectations of **ordered**, pairwise-distinct tuples. For a bounded ball $B_R$, their total masses on $B_R^n$ are exactly $\mathbb E(X(B_R))_n$, with no factor $1/n!$. The submission uses this convention consistently.

S0 requires equality of the full measures and excludes singular mass. Consequently an a.e. density identity off the geometric degeneracy set accounts for the entire factorial measure: the diagonal, collinear triples, and coplanar quadruples are Lebesgue-null. For the pair and triangle upper estimates, a hidden positive singular component could defeat the estimate, so excluding one is a substantive use of the target. The fourth divergence is more robust: a positive extra singular part could not remove its nonnegative lower bound.

Almost-sure local finiteness gives finite integer-valued counts, not finite moments. The proof obtains each moment it uses from the relevant full density or avoids that moment through bounded occupancy indicators. It never treats a finite intensity as a finite variance assumption.

### 2. Direct pair contradiction, lines 17–21 and 33–72

Set $v=4\pi/3$ and $N_R=X(B(0,R))$. The full pair identity gives
\[
\mathbb E(N_R)_2=a_2\int_{B_R^2}\frac{dx\,dy}{\|y-x\|}.
\]
This identity follows directly from the definition with the indicator of $B_R^2$. Its validity does not presuppose a finite second moment.

For each $x\in B_R$, the translated set $B_R-x$ is contained in the radius-$2R$ ball. The integrand is nonnegative and radial, so
\[
\int_{B_R}\frac{dy}{\|y-x\|}
\leq 4\pi\int_0^{2R}r\,dr=8\pi R^2.
\]
The spherical factor $4\pi$, radial power $r$, and resulting power $R^2$ are correct in dimension three. Integrating in $x$ gives
\[
\mathbb E(N_R)_2\leq8\pi a_2vR^5<\infty.
\]
Tonelli and the domain enlargement are legitimate without prior integrability; the finite bound then establishes integrability. Since $N_R^2=(N_R)_2+N_R$ and $\mathbb E N_R=\lambda_0vR^3$, the variance inequality is now available with finite quantities. It yields
\[
\lambda_0^2v^2R^6
\leq8\pi a_2vR^5+\lambda_0vR^3,
\quad\text{hence}\quad
\lambda_0^2v\leq\frac{8\pi a_2}{R}+\frac{\lambda_0}{R^3}.
\]
All constants and powers in the division are correct. For any fixed positive finite $\lambda_0,a_2$, the right side tends to zero and the left side is strictly positive. This is a contradiction, not merely a bound on one admissible coefficient. Allowing $a_2$ to depend on $\lambda_0$ does not help: after that choice both are fixed while $R$ increases.

The availability of arbitrarily large deterministic balls is the global ingredient. Neither an empirical-density limit nor stationarity is required. There is no interchange of a stochastic limit and an expectation. No conclusion for a law specified only up to a finite diameter follows by repeating this $R\to\infty$ step.

### 3. Pair tails with arbitrary short-range behaviour, lines 74–118

The strengthened theorem assumes domination of the **restricted pair measure** on all sufficiently distant pairs by $\varepsilon\,dx\,dy$, for every $\varepsilon>0$. This is stronger than a statement about an absolutely continuous component alone. Its formulation correctly excludes an unaccounted singular tail.

The half-open cubes $Q_z=z+[0,1)^3$ form a disjoint partition. Stationarity gives a common occupancy probability
\[
p=\mathbb P(X(Q_z)>0)>0.
\]
The strict positivity follows from $\mathbb E X(Q_z)=\lambda>0$; no quantitative lower bound in terms of $\lambda$ and no second moment are needed. The bounded variables $I_z=\mathbf1\{X(Q_z)>0\}$ have all moments.

For $x=z+u$, $y=w+v$ with $u,v\in[0,1)^3$, we have $\|(v-u)\|\leq\sqrt3$. Thus $\|z-w\|>L>r_\varepsilon+\sqrt3$ ensures $\|y-x\|>r_\varepsilon$. For distinct cubes, every pair counted in $X(Q_z)X(Q_w)$ consists of distinct points. Therefore
\[
\mathbb E I_zI_w\leq\mathbb E[X(Q_z)X(Q_w)]
=\alpha^{(2)}(Q_z\times Q_w)\leq\varepsilon,
\]
where the last bound uses unit cube volumes and the full tail domination. Although near-cube count products might have infinite expectations, the proof never uses those products there.

For $n=m^3$ cubes, the number of ordered neighbouring cube pairs is at most $nC_L$, where $C_L$ counts the finitely many nonzero lattice offsets of norm at most $L$. The diagonal contribution is at most $n$, every near-pair occupancy product is at most one, and every far-pair expectation is at most $\varepsilon$. Hence
\[
n^2p^2\leq\mathbb E S_m^2\leq(1+C_L)n+\varepsilon n^2.
\]
The overcount in the final $\varepsilon n^2$ bound is harmless. Crucially, the proof first fixes $\varepsilon$ (and therefore $C_L$), then sends $m$ to infinity, and only afterwards sends $\varepsilon$ to zero. It does not silently claim a uniform bound on $C_L$ as $\varepsilon$ decreases.

This proves the advertised impossibility. An exact reciprocal tail $a_2/D$ beyond any finite threshold satisfies the domination by choosing a further threshold larger than $a_2/\varepsilon$. The conclusion survives an arbitrary, even locally infinite, short-range factorial measure. Conversely, the proof says nothing about a reciprocal law on a sparse unbounded subset with substantial pair mass on its complement; the submission explicitly preserves that limitation. It also does not assert mixing or convergence of the pair density to $\lambda^2$.

### 4. Independent triangle contradiction, lines 120–157

The change of variables $(x_1,x_2,x_3)\mapsto(x_1,u,w)$ with $u=x_2-x_1$, $w=x_3-x_1$ has Jacobian one. On $B_R^3$, both displacements have norm at most $2R$. The area convention is $A=\|u\times w\|/2$, producing the numerator 2 in the enlarged displacement integral.

For fixed nonzero $u$, use spherical coordinates for $w$ with polar angle $\theta$ measured from $u$. Writing $r=\|u\|$, $s=\|w\|$, the integrand is $2/(rs\sin\theta)$. Multiplication by $r^2dr\,d\omega_u$ and $s^2\sin\theta\,ds\,d\theta\,d\phi$ gives $2rs\,dr\,ds\,d\omega_u\,d\theta\,d\phi$. Thus the integral is exactly
\[
2\,(4\pi)\,(2\pi)\,
\left(2R^2\right)^2\,\pi=64\pi^3R^4.
\]
The factor $\pi$ is $\int_0^\pi d\theta$, not $\int_0^\pi\sin\theta\,d\theta$. This cancellation is the reason collinearity is integrable for triples in dimension three. The radial integrals also handle coincidences. Coordinate exceptions and collinear triples have zero Lebesgue measure: for almost every pair of distinct anchors, the third point is restricted to a line. The use of nonnegative integration justifies the enlarged-domain calculation even before its finiteness is known.

It follows that
\[
\mathbb E(N_R)_3\leq64\pi^3a_3vR^7.
\]
For every nonnegative integer $N$, the deterministic inequality
\[
(N)_3\geq(N-2)_+^3
\]
is correct: both sides vanish for $N\leq2$, and for $N\geq3$ every factor on the left is at least $N-2$. The function $t\mapsto(t-2)_+^3$ is convex on the real line. Jensen applies because $\mathbb E N_R$ is finite; in fact the preceding bound also makes its nonnegative left-hand expectation finite. Therefore
\[
(\lambda vR^3-2)_+^3\leq64\pi^3a_3vR^7.
\]
After division by $R^9$, the two sides converge to $(\lambda v)^3>0$ and zero, respectively. No pair-density law is used. Unknown second moments of a hypothetical process have not been assumed away: the stated third measure bound already provides the required expectation. This validates the claim that repairing only the pair law while retaining the entire global triangle law cannot yield a process.

### 5. Reciprocal volume and the separate fourth-moment class, lines 159–193

Fix a noncollinear base triangle inside a nonempty open ball $B$. Its plane $P$ passes through an interior point $x_1$. A cylinder of the form displayed in the submission lies in $B$ for sufficiently small $\delta>0$; explicitly, any $\delta<\operatorname{dist}(x_1,B^c)/\sqrt2$ suffices. Its planar base has area $\pi\delta^2>0$.

For the orthonormal coordinates $x_4=z+t\nu$, the volume formula is
\[
V=\frac16|(x_2-x_1)\times(x_3-x_1)\cdot t\nu|
=\frac{A|t|}{3}.
\]
The Jacobian is one. Integration over the cylinder with $t\ne0$ therefore yields
\[
\int_{B\cap\{V>0\}}\frac{dx_4}{V}
\geq\frac{3\pi\delta^2}{A}
\int_{0<|t|<\delta}\frac{dt}{|t|}=\infty.
\]
The integral diverges through genuinely noncoplanar quadruples. Changing a representative of the density on the exactly coplanar set cannot help. Because the base is noncollinear and $t\ne0$, the four vertices are automatically distinct in this lower bound.

For almost every base triple this argument applies. Tonelli applied to the measurable nonnegative function $\mathbf1_{\{V>0\}}/V$ gives an infinite integral over $B^4$. No measurable choice of the auxiliary normal or cylinder is required: the pointwise fibre integral has been shown infinite for each noncollinear base, and the original integrand is measurable. The equality with the full fourth factorial measure and $a_4>0$ then gives
\[
\mathbb E(X(B))_4=\infty,
\qquad \mathbb E X(B)^4=\infty,
\]
the second statement following from $N^4\geq(N)_4$.

This conclusion does not contradict almost-sure finite counts or a finite first moment. The submission's count example has normalising constant $c=1/\sum_{k\geq1}k^{-5}$, and
\[
\mathbb E N^j=c\sum_{k\geq1}k^{j-5}.
\]
The series converges for $j=1,2,3$ and diverges for $j=4$. It correctly illustrates only the distinction between moments, not spatial realisability. Nor is failure of local integrability alone a failure to define an extended measure: $\mathbf1_{\{V>0\}}a_4/V$ is nonnegative, measurable and finite a.e., so its Lebesgue integral defines a measure, albeit with infinite mass on these bounded configuration sets. The unproved issue is whether it can be a factorial measure of a process satisfying the other requirements.

For a proposed finite-diameter domain, one may choose a ball with diameter strictly less than $M$. Every quadruple in that ball is then within the prescribed domain. The same local divergence proves that the proposed question would remain impossible if finite fourth count moments were added. This correctly handles the separate subclass required by S0.

### 6. Dependencies, limits, and checks of scope

All decisive integrations are nonnegative and use Tonelli or domain enlargement; no signed infinite expressions or unproved dominated-convergence step occurs. The large-radius limits are limits of deterministic inequalities. The occupancy proof uses a correctly ordered pair of limits. Coefficients are positive and finite whenever multiplied by a divergent integral or compared with a positive intensity term.

The proofs handle arbitrary coefficients chosen with the process. They exclude every positive prescribed intensity, rather than only a range of intensities. Zero intensity and zero coefficients are outside S0; infinite coefficients are also excluded. The use of balls and cubes introduces no isotropy assumption on the process.

There is no candidate process construction to verify, and no partition expansion or parent allocation is invoked. Accordingly there is no omitted disconnected contribution in these proofs: they use the full factorial measures directly. The proof does not replace full densities with cumulants. Whole-space existence is contradicted because such a process would have to satisfy the derived inequalities for all the test sets used.

## Finding register

The entries distinguish verified conclusions from nonblocking scope and presentation notes. No invalid inference or unresolved dependency was found in the asserted non-existence and divergence proofs.

| ID | Location | Precise mathematical issue | Consequence | Repair/status |
|---|---|---|---|---|
| R1-01 | Lines 17–21, 33–72; equations (1)–(4) | The pair law yields a finite second moment locally, then an $R^5$ factorial upper bound incompatible with the $R^6$ mean-square lower bound | General contradiction to S0 at every positive intensity | Verified; no repair |
| R1-02 | Lines 76–116; equations (5)–(7) | Bounded occupancy indicators bypass any short-range infinite second moments; the hypothesis is full tail measure domination | A lower-distance modification alone cannot save the reciprocal tail in the stationary class | Verified; retain the full-measure tail qualification when summarising |
| R1-03 | Lines 122–155; equations (8)–(11) | The angular singularity cancels, the displacement integral is $64\pi^3R^4$, and the falling-factorial/Jensen lower bound grows as $R^9$ | Independent general triangle-law obstruction | Verified; no repair |
| R1-04 | Lines 161–190; equations (12)–(13) | Reciprocal volume has a logarithmically divergent normal-height integral on noncoplanar configurations | Excludes finite fourth count moments in every affected open ball; does not alone exclude S0's extended class | Verified with the stated limited scope |
| R1-05 | Lines 192–193 | The heavy-tailed count example is a moment example, not a process realisation | It justifies the logical distinction, not feasibility of reciprocal spatial laws | Correctly qualified; no repair |
| R1-06 | Lines 197–215 | A finite upper diameter is an available way to remove the hypotheses of the global contradictions, but is neither proved necessary nor proved sufficient | Proposed finite-domain question remains unresolved | Scope note; preserve the provisional status |
| R1-07 | Lines 205–215 | The common cap also removes fourth-order large-diameter requirements, although no independent fourth-order large-scale obstruction was proved here | This extra domain loss must be acknowledged as a choice, rather than attributed to Proposition (12) | Nonblocking clarification for any amendment record |
| R1-08 | Lines 205–217 | The intensity and diameter are prescribed independently; coefficients may depend on both | A low-intensity construction at fixed geometry is insufficient without a proof handling these quantifiers | Correctly stated; remains a construction obligation |
| R1-09 | Lines 170–174 | The cylinder inclusion is routine but may be made explicit with $\delta<\operatorname{dist}(x_1,B^c)/\sqrt2$ | Makes the geometric localisation immediately checkable | Optional exposition improvement, not a gap |

## Amendment implications

### What the proof establishes as necessary

If positive finite homogeneous intensity and full-density interpretation are retained, the unrestricted reciprocal pair requirement must change. In the stationary class, allowing arbitrary short-range behaviour while keeping the exact reciprocal law at every sufficiently large separation is still impossible. The tail theorem gives this stronger logical conclusion without any finite second-moment assumption.

Independently, the unrestricted full triangle requirement must change. Removing only the pair requirement would leave that contradiction intact. The submission does not establish a triangle analogue of its arbitrary-short-range tail theorem, so that stronger statement should not be inferred from this report.

If finite fourth count moments are imposed, the reciprocal-volume identity cannot remain on every noncoplanar quadruple in an open ball. Altering only a null degeneracy set is insufficient. Enough of the positive-measure near-coplanar requirement must be changed to make the relevant local integral finite, or the finite-moment condition must be dropped. This necessity belongs to the **finite-moment subclass**. S0 deliberately does not impose that condition.

### What the proof does not select

A finite upper diameter is not proved logically necessary. Neither are a specific numerical diameter, a hard threshold, a lower distance cutoff, a lower altitude cutoff, a shape restriction, or any maximal admissible domain. Selected unbounded domains with unconstrained complements are not excluded by the arguments as stated. Those alternatives are not thereby shown feasible.

The proposed question quantifies over every independently prescribed pair $(\lambda_0,M)\in(0,\infty)^2$, keeps exact formulas at all three orders, requires full absolute continuity globally, and permits infinite higher moments. It specifies the strict domain $\operatorname{diam}<M$ and leaves densities outside that domain free. These choices are precise and do not silently lower the intensity quantifier.

The pair and triangle general obstructions adequately justify reconsidering their all-scale domains. The use of one common finite cap for all three orders is a non-unique design choice. In particular, restricting the fourth-order large-diameter domain is not independently forced by the local fourth-moment proposition. A statement-change record should explicitly identify this loss of scope; describing the whole proposal as a uniquely necessary consequence would overstate the proof.

The packet permits reviewed general obstructions to motivate coordinator-led domain revisions within their scope. This report supplies verified evidence, not an adoption decision. Choices outside those proved implications, including adding a finite-moment hypothesis or asserting that S0 generally requires a positive lower altitude, need separate justification or explicit owner choice. Changes to exactness, full-density interpretation, retained orders, or prescribed intensity remain subject to the packet's explicit owner-approval rule. The reviewer cannot approve them on the owner's behalf.

No new target has been written, adopted, hashed, or broadcast by this review. S0 remains the assigned target. The original S0 non-existence verdict must be retained under any later amendment, and a later restricted construction cannot be counted as an S0 construction success.

## Source and coding evidence

The argument is self-contained apart from elementary measure integration and inequalities. The precise dependencies used are:

1. S0's definition of the full ordered factorial expectation measures and its allowance of extended nonnegative values.
2. Tonelli's theorem for nonnegative measurable functions on products of Euclidean Lebesgue spaces.
3. The unit-Jacobian translation change of variables, spherical-coordinate integration, and the base-area-times-height formula for tetrahedral volume.
4. $\mathbb E Z^2\geq(\mathbb E Z)^2$ for square-integrable random variables, applied only after integrability has been established or to bounded indicators.
5. Jensen's inequality for the specified convex function and the explicitly verified integer-count inequalities.

No specialised theorem, attribution, or historical claim from a primary paper is a dependency. The neutral source index and DVJ context were read as supplied context. No primary PDF or external web source was needed or consulted, and no source-check request was necessary. This report makes no claim of novelty or about the current status of a literature problem.

Filesystem tools checked SHA-256 integrity, supplied numbered source text, and extracted this reviewer's own permitted runtime metadata. No numerical simulation, symbolic package, coding-agent request, or proof assistant was used. The constants, Jacobians, inequalities, and limit arguments above were independently recomputed in the mathematical audit. Tool output was not used to certify a continuum theorem.

## Presentation judgement

**Presentation passes.** The main conclusion is stated before the argument; each supporting theorem has a distinct purpose; moment assumptions and the absence of mixing are explained at their relevant steps. The provisional nature and limitations of the replacement question are clear. The submission uses S0's normalisations and maintains a readable distinction between full factorial measures and count moments.

Two optional improvements would help a subsequent statement-change record or publication version: spell out the cylinder-radius choice in R1-09, and explicitly distinguish the evidenced pair/triangle domain changes from the additional fourth-order domain choice in R1-07. Neither affects the validity of the frozen proof. No author text was edited.

## Review summary and remaining obligations

The decisive comparison is $R^5$ versus $R^6$ for the pair law, after deriving the needed finite second moment. The bounded-occupancy theorem extends the tail obstruction to processes with arbitrary short-range pair moments. The independent triangle comparison is $R^7$ versus $R^9$. The fourth-order calculation proves a local infinite-moment conclusion through noncoplanar configurations and is correctly confined to its moment scope.

**There are no remaining proof obligations for the stated S0 non-existence result or the three complementary results as formulated.** The following questions remain open in this submission and are not approved by this review:

- Existence or non-existence for the displayed finite-diameter replacement in the extended-moment class.
- Cross-order realisability, including compatibility of the reciprocal fourth density with the lower-order laws on a proposed common domain.
- Any general local obstruction beyond the finite-fourth-moment conclusion proved here.
- A sufficient or maximal replacement domain, and the merits of one particular cutoff or shape condition.
- A construction valid for every prescribed intensity at fixed independently prescribed geometry.

These are limitations of the proposed follow-on question, not gaps in the S0 contradiction. A later submission asserting any of them would require its own proof and review.

## Accounting and freeze handoff

`preflight.json` records the verified model/effort and a pre-research checkpoint from this reviewer's own session. Runtime token events expose cumulative and last-event fields for input, cached input, cache-write input, output, reasoning output and total tokens. The evidence was obtained from metadata only; no reasoning transcript or other session was inspected. There are no child agents. Parent/child inclusion semantics and monetary charges remain NR.

A separate `accounting_checkpoint.json` records the last exposed checkpoint available before handoff. It is explicitly a checkpoint, not a claim to include the final response or later runtime events. Cumulative snapshots must not be summed; reasoning-output tokens must not be added again to output. Completed-turn reconciliation remains with the coordinator using this identified session and turn. No estimate or charge is inferred from report length.

The frozen report's final SHA-256 and word count are recorded externally in `review_manifest.json` and `review.sha256`, avoiding a self-referential file hash. All writes were confined to the assigned review directory; the frozen proof and target were not changed. No final-synthesis comparison with another track was performed.
