# Review — proof_4 / submission v01 / S1

- Type: fresh independent review of one frozen submission; no delegation.
- Reviewer: `/root/review_proof_4_v01`; session `session-14`; turn `turn-26`.
- Model and effort: runtime `turn_context` verifies `gpt-6-astra`, `xhigh`, before mathematics. Session start: 2026-10-20T17:38:19.506Z. Exact preflight and later accounting checkpoints are separate assigned artifacts.
- Setup root: `$SETUP`.
- Run root: the setup root followed by `runs/20261020T164437Z_astra6`.
- Active statement: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Frozen submission: `reviews/proof_4_v01/proof_snapshot.md`, SHA-256 `57b1c58f13fa055c76cfec22c131b989b32bef3b1414cd710992ad6f081158b5`; substantive attempt 1 of 4.
- Dispatch packet: `packets/review_proof_4_v01.json`, SHA-256 `e7f0e460b4e6e545d51bda00708343e8dfc03d94dc8b6840782acdee8c9e7048`. All 19 allowed-file hashes were checked and matched before the audit.
- Received context: frozen run instructions, workflow, common statement/context/index, report and amendment templates, S0, S1 and its adoption document, the single submission, its explicitly cited seed excerpt and provenance, and the frozen proof-reviser skill with both required references. Setup-relative references were resolved to the authorised frozen copies.
- Excluded context: author conversations and private work, other construction tracks and reviews, prior review verdicts, all unassigned seed material, other chats and old runs. The amendment record was used to identify the target and authority; the obstruction proofs behind that record were not independently re-audited here.

## Correctness verdict and scope

**The submitted informal argument establishes Theorem 1 as a partial construction and Proposition 2 as a scoped obstruction. It does not establish S1.** The process has the exact full fourth-order reciprocal-volume density throughout the required local shape domain, for every independently prescribed pair $(\lambda_0,M)$. Its full second and third densities exist globally and are finite almost everywhere, but they provably fail the two corresponding S1 identities. Consequently this submission is an unsuccessful S1 construction attempt, with a valid partial theorem retained. It is neither an invalid partial construction nor a general non-existence result.

The audit covers the entire mathematical submission: construction of an actual whole-space law; stationarity and isotropy; simplicity and almost-sure local finiteness; exact intensity; all slab allocations; full factorial measures and absence of singular mass; determinant and lower-order Jacobians; global fourth-density finiteness away from a null resonance set; local count moments; both lower-order failures; and the exact class and domination argument in Proposition 2. No essential mathematical gap remains in those advertised partial claims under the natural canonical-density convention made explicit below. Two minor precision corrections are recorded separately from the target failures.

The final S1 question remains unresolved by this submission. In particular, neither the representation-specific obstruction nor failure of this law to have the lower identities warrants changing S1.

## Reconstruction and detailed audit

### 1. Statement and quantifiers

S1 requires one process for every prescribed $\lambda_0>0$ and $M>0$, chosen independently. All three *full* factorial densities must be globally absolutely continuous with finite-almost-everywhere densities. On every nondegenerate configuration of diameter less than $M$, the identities must hold simultaneously at orders two, three and four. Infinite fourth local moments are permitted.

Theorem 1 explicitly drops the two lower-order identities from its conclusion. That is a materially weaker theorem, accurately labelled by the author. It retains the whole-space law, global measure regularity, all prescribed intensities and diameters, and every noncoplanar shape below $M$ at order four. Its additional isotropy and finite third local moments are compatible with S1 but do not replace its missing identities.

There is no rescaling argument hidden in the quantifiers. For the given $M$, the construction first fixes $L=2M$, computes finite constants $Z,J$, and then sets $s=\lambda_0Z/J$. The mark law depends on $M$ while the multiplicative amplitude $s$ accommodates every positive $\lambda_0$. No upper bound on $\lambda_0M^3$ appears. Constants may deteriorate as parameters vary; S1 asks for existence at each fixed pair and imposes no uniform bounds.

### 2. Normalisation and actual random process

Write $A(v)=1+|v|^2$ for the amplitude, distinct from triangle area. Direct polar integration verifies
\[
J=4\pi\int_0^\infty\frac{r^2}{(1+r^2)^3}\,dr=\frac{\pi^2}{4},
\]
\[
Z=4\pi\int_0^\infty\frac{r^2(2+Lr)}{(1+r^2)^4}\,dr
 =\frac{\pi^2}{4}+\frac{\pi L}{3}.
\]
For example, $r=\tan\theta$ gives the $r^2$ integrals; $y=r^2$ gives
$\int_0^\infty r^3(1+r^2)^{-4}dr=1/12$. Both normalising constants are finite and positive for every fixed $L>0$. Thus $p(v)=T(v)/(ZA(v)^4)$ is a probability density.

The measurable marks $W$ and $B\mid W=v\sim\mathrm{Unif}[0,T(v))$ define a single globally shared random intensity field. Since $T(v)\ge2$ and each slab has affine width one, their interiors never overlap. In fact the half-open convention also prevents endpoint double counting. Hence
\[
0\le\Lambda(x)\le s(1+|W|^2)<\infty
\]
for every realised finite mark and every $x$. The countable slab sum is jointly measurable. Thinning an independent Poisson random measure on $\mathbb R^3\times[0,\infty)$ yields a legitimate random measure, and its spatial projection is conditionally Poisson with diffuse locally finite intensity $\Lambda(x)\,dx$.

For each bounded cube, the conditional Poisson mean is finite. A countable exhaustion by cubes proves local finiteness simultaneously for all bounded sets. Diffuseness gives simplicity on each cube and then globally. These arguments require no unconditional fourth moment. The zero vector $W=0$ is a probability-zero mark but also gives a well-defined bounded field, so it causes no existence problem.

A translation shifts $B$ by a deterministic amount modulo its conditional period. The phase law is invariant under that shift, even though the shift depends on $W$. Rotations preserve the radial law of $W$ and its amplitude and period. Thus stationarity and isotropy follow without mixing or ergodicity. The global marks may carry long-range dependence; that is allowed.

Phase averaging gives mean occupancy $1/T(v)$ at each fixed spatial point. Therefore
\[
\mathbb E\Lambda(x)=\frac{s}{Z}\int_{\mathbb R^3}A(v)^{-3}\,dv
=\lambda_0.
\]
Tonelli gives $\mathbb EX(C)=\lambda_0|C|$ for every bounded Borel $C$. This checks the exact intensity, rather than just positivity or a proportionality constant.

### 3. Full factorial measures and all allocations

Conditional on the marks, the factorial moment formula for a diffuse Poisson process gives
\[
\mathbb E\!\left[\sum^{\ne}f(x_1,\ldots,x_n)\mid W,B\right]
=\int f(\mathbf x)\prod_i\Lambda(x_i)\,d\mathbf x.
\]
The submission supplies an adequate elementary derivation through finite partitions, Poisson factorial moments and monotone extension. Nonnegative $f$ permits Tonelli without integrability hypotheses. Consequently
\[
\alpha^{(n)}(d\mathbf x)=\mathbb E\!\left[\prod_i\Lambda(x_i)\right]d\mathbf x
\]
as an identity of extended nonnegative measures. A Lebesgue-null set has zero mass for every conditional product measure and therefore zero unconditional mass. This proves absence of singular mass everywhere, including collinear, coplanar and resonant configurations. It is stronger than identifying a density only on the prescribed domain.

The slab-index change in equation (9) is correct. For a fixed first index $k_1$, set $b'=b+k_1T-v\cdot x_1$ and $m_i=k_i-k_1$. Summing $k_1$ tiles the real line by the phase intervals. The product of $n$ amplitudes together with $p(v)/T(v)$ leaves exactly $s^nA(v)^{n-4}/Z$. The resulting sum over $m\in\mathbb Z^{n-1}$ includes all allocations to all slabs; the tuples remain ordered, so no factorial multiplicity is missing.

If the integrand is nonzero, comparison with the first point gives
\[
|v\cdot u_i-m_iT(v)|<1.
\]
For $|u_i|<M$ and $m_i\ne0$, the left side is at least
\[
T(v)-|v||u_i|=2+(L-|u_i|)|v|\ge2,
\]
a contradiction. Thus only $m=0$ survives on the prescribed local domains. The strict inequality printed in line 143 needs the harmless endpoint adjustment stated in R4-04; the exclusion itself is valid for every $v$.

No separate Poisson-parent partition terms need to be added to this calculation. This model uses one shared random field, and its expected intensity product already is the full factorial density. The sum in (9) accounts for the possible slab allocations directly. Confusing this with the seed's fourth cumulant would be an error, but the submission does not do so.

### 4. Fourth-order determinant, constants and shape coverage

At order four the amplitude weight cancels exactly. The matrix of
\[
(v,b)\longmapsto(v\cdot x_1-b,\ldots,v\cdot x_4-b)
\]
has rows $(x_i^\top,-1)$. Subtracting its first row from the remaining rows shows that its determinant has absolute value
\[
|\det[x_2-x_1,x_3-x_1,x_4-x_1]|=6V.
\]
It is invertible at every noncoplanar configuration. The integral of the product of the four interval indicators is $|I|^4=1$, and hence
\[
\rho^{(4)}(\mathbf x)=\frac{s^4}{6ZV(\mathbf x)},\qquad
 a_4=\frac{s^4}{6Z}>0.
\]
The derivation uses only the diameter cap and noncoplanarity. It does not introduce a lower edge length, area, height, volume or shape cutoff. Arbitrarily flat noncoplanar tetrahedra are included. The factor is a full density, not a cumulant or an asymptotic statement.

### 5. Global finite-almost-everywhere fourth density

This obligation is essential because S1 restricts the fourth formula locally but requires global density regularity. The proof treats it separately and successfully.

For any fixed affinely independent quadruple, let $U$ have rows $u_i^\top$, set $r=|v|$, and let $R=\max_i|u_i|$. Each nonzero term satisfies
\[
|m_i|\le\frac{rR+1}{Lr+2}\le\max(R/L,1/2).
\]
There are therefore finitely many possible allocations $m$, with a bound independent of the integration variables. This is a genuine finite reduction for each configuration, not an unjustified truncation.

For such an $m$, let $w=U^{-1}m$. The support inequality gives
\[
|v-Lrw|\le2|w|+\sqrt3\|U^{-1}\|=:K.
\]
Thus $r|1-L|w||\le K$. Whenever $L|U^{-1}m|\ne1$, the integration variable $v$ is restricted to a finite-radius ball. The remaining $b$ interval has length one, and the order-four integrand is bounded by one. Each term is finite, and their finite sum is finite.

For $m\ne0$, a resonance on invertible $U$ satisfies the polynomial equation
\[
L^2|\operatorname{adj}(U)m|^2-(\det U)^2=0.
\]
It is a nonzero polynomial: at $U=tI$ it becomes $L^2t^4|m|^2-t^6$. The zero set of a nonzero real polynomial is Lebesgue-null; an induction on dimension using its coefficient polynomials and Fubini proves the fact needed here. Affine dependence is another polynomial null set. Taking the countable union over integer $m$ and applying the invertible linear configuration change $\mathbf x\mapsto(x_1,U)$ preserves nullity. The argument therefore establishes global finiteness almost everywhere. It deliberately does not establish boundedness or local integrability of the fourth density, neither of which is required.

There is no conflict between assigning finite values on exceptional null sets and the asserted pointwise local fourth formula. A resonance with nonzero $m$ cannot occur in $E_4(M)$: if $|U^{-1}m|=1/L$, then
\[
|m_i|=|u_i\cdot U^{-1}m|<M/L=1/2
\]
for every component, forcing the integer vector $m$ to be zero. Thus the noncoplanar local domain does not meet the resonance set. Null-set reassignment elsewhere changes no measure and adds no singular mass.

### 6. Local moments and lower-order global regularity

For a ball of radius $R$, the number of slabs that can intersect it is bounded by
\[
(2Rr+1)/(2+Lr)+1\le2R/L+2.
\]
For $r>1$, each intersection has volume at most $\pi R^2/r$. Consequently the conditional Poisson mean satisfies $\mu_R\le C_{R,L}s(1+r)$, with a finite constant. For $r\le1$ the direct amplitude bound suffices. These bounds hold uniformly over the phase.

The radial mark density is proportional to $r^2(2+Lr)/(1+r^2)^4$, which is $O(r^{-5})$ at infinity. Hence $\mathbb E(1+|W|)^3<\infty$ and $\mathbb E\mu_R^3<\infty$. The conditional Poisson identity
\[
\mathbb E[X(C_R)^3\mid W,B]=\mu_R^3+3\mu_R^2+\mu_R
\]
proves finite third count moments for every ball and then for every bounded Borel subset. In particular, the second and third factorial densities are integrable on every bounded product cube. Countable exhaustion proves their global finiteness almost everywhere. This argument concerns integrated counts; no finite third moment of the random intensity at an individual point is assumed or needed.

For the fourth moment, place all four vertices in a smaller ball of diameter below $M$. For every noncollinear base triple in that ball, a sufficiently small normal cylinder around its first vertex stays inside the ball. Writing the fourth point as $z+t\nu$, the volume is $A_\triangle|t|/3$. The integral of the verified fourth density over this cylinder contains a positive multiple of $\int_{0<|t|<\delta}dt/|t|=\infty$. With $t\ne0$ the fourth point is distinct from every base vertex. Almost every base triple is noncollinear, and Tonelli now gives infinite fourth factorial moment, hence infinite fourth raw count moment. Every nonempty open ball contains such a smaller ball.

The finite third moment, infinite fourth moment and almost-sure finite counts are therefore mutually consistent properties of the actual constructed law. The same local integral also excludes the separate finite-fourth-moment comparison class whenever that class is required to satisfy S1's fourth identity; it imposes no new restriction on broad S1.

### 7. Explicit lower-order identities and failure of S1

For a pair separated by $d\in(0,M)$, the coordinates $(t_1,t_2)$ fix the component of $v$ along the separation and $b$, with Jacobian $1/d$. Integrating the two perpendicular components gives
\[
\int_{\mathbb R^2}(c+|z|^2)^{-2}dz=\pi/c.
\]
Thus equation (18) is correct. The difference $t_2-t_1$ under Lebesgue integration on $I^2$ has density $(1-|t|)_+$, yielding
\[
\Phi(d)=2d\arctan(1/d)-d^2\log(1+d^{-2}).
\]
It follows that $\Phi(d)/d\to\pi$ and
\[
\rho^{(2)}(d)\longrightarrow\pi^2s^2/Z,\qquad
 d\rho^{(2)}(d)\longrightarrow0.
\]
The required positive constant $a_2$ cannot equal $d\rho^{(2)}(d)$ almost everywhere. Continuity on $(0,M)$ or simply a sequence from a full-measure set makes the contradiction rigorous. Polar integration transfers spatial almost-everywhere equality to almost-everywhere equality in $d$.

For a triangle, the three affine coordinates fix $b$ and the component of $v$ in the span of its edges. The Jacobian is $1/|u\times w|=1/(2A_\triangle)$. Integrating the remaining normal component gives $\pi/\sqrt{1+|v_0|^2}$, so equation (21), including its factor $1/2$, is also correct.

The scaling relation $v_0(\mathbf t;cu,cw)=c^{-1}v_0(\mathbf t;u,w)$ shows by dominated convergence that $\Psi(cu,cw)\to0$. Its integrand is strictly increasing in $c$ except on $t_1=t_2=t_3$, a null set, so the factor is not constant. Continuity on the open noncollinear domain follows from continuous dependence of the planar inverse and bounded convergence. Therefore spatial almost-everywhere equality to $a_3/A_\triangle$ would force equality throughout that domain and contradict the scaling limit. Both S1 failures are established, not merely unproved.

### 8. Proposition 2 and exact obstruction scope

For the stated radial finite-thickness periodic slab class, the same allocation exclusion applies below $M$. Spherical integration of the overlap function gives
\[
H(z)=4\pi\int_0^1(1-zt)_+\,dt
=\begin{cases}4\pi(1-z/2),&0\le z\le1,\\2\pi/z,&z\ge1.\end{cases}
\]
Together with the weight $\omega(r)=q_0(r)a(r)^2r^2/T(r)$, this verifies the full pair formula in (24); the spherical surface factor has not been omitted.

For fixed finite $r$, $dH(dr)$ increases up to its constant value $2\pi/r$ and tends to zero as $d\downarrow0$. More explicitly its derivative before the threshold is $4\pi(1-rd)\ge0$; the two expressions agree at the threshold. At $r=0$ it is simply $4\pi d$.

Finiteness at a distance $d_0$ of the canonical mixture density makes $\omega(r)d_0H(d_0r)$ integrable. It dominates $\omega(r)dH(dr)$ for every $0<d\le d_0$. Dominated convergence gives the limit in (23) and finiteness at every such smaller distance. The contradiction with an almost-everywhere reciprocal law follows by selecting $d_0$ and a sequence decreasing to zero from its full-measure set. This does not require continuity of a general radial mark density.

The obstruction uses one global slab family, radial marks, the specified nonnegative finite amplitudes, the fixed interval profile, the separated periods and the canonical mixture interpretation. It is not an obstruction to all Cox processes, arbitrary carriers, general stationary processes or S1. The finiteness convention in R4-03 is a useful statement clarification; the formula and argument already provide that convention internally.

## Finding register

| ID | Location in frozen submission | Precise mathematical finding | Consequence | Repair/status |
|---|---|---|---|---|
| R4-01 | Lines 254–278; Theorem 1 and S1 acceptance | The full pair density tends to a finite limit as $d\downarrow0$, so $d\rho^{(2)}(d)\to0$. | No positive $a_2$ gives the required reciprocal-distance law. This process cannot pass S1. | Verified, author-acknowledged target failure. A complete S1 construction must change the law beyond the class excluded by Proposition 2. |
| R4-02 | Lines 280–303; Theorem 1 and S1 acceptance | The factor $\Psi(u,w)$ multiplying $1/A_\triangle$ is continuous, changes strictly under scaling and tends to zero under collapse. | No positive configuration-independent $a_3$ gives the required reciprocal-area law. | Verified, author-acknowledged target failure. Any repair must also preserve the fourth law and global measure requirements. |
| R4-03 | Proposition 2, lines 309–320 and 338–340 | Pointwise finiteness at one distance is not invariant under changing a Radon–Nikodym density on a null set. The proof uses the canonical radial expected-product density in (24). | A purely arbitrary-density-version reading would not justify the domination premise. This does not affect Theorem 1 or exclusion of an a.e. reciprocal law. | Minor precision correction: explicitly write $\rho^{(2)}(d)=\mathbb E[\Lambda(0)\Lambda(de_1)]$ or the integral in (24) in the hypothesis. Under this natural convention, the proposition is proved. |
| R4-04 | Lines 141–145, especially the strict inequality in line 143 | At $v=0$, the printed strict inequality $T(v)-|v||u_i|>2+(L-M)|v|$ becomes equality. | No mathematical consequence: the lower bound $\ge2$ already contradicts support condition $<1$, including at $v=0$. | Harmless endpoint correction. Replace the displayed strict chain by $T(v)-|v||u_i|=2+(L-|u_i|)|v|\ge2$. No dependent argument changes. |

These are not findings of a false partial theorem. R4-01 and R4-02 are the substantive reasons for unsuccessful S1 status; R4-03 and R4-04 are closed statement/algebra precision points with explicit repairs. No further unresolved correctness defect was identified in the partial construction.

## Amendment implications

The submitted construction demonstrates that the exact local full reciprocal-volume identity, with all small nondegenerate shapes and arbitrary independently prescribed intensity and diameter, is compatible with the broad process class and global density requirements. It does not demonstrate simultaneous realisability with the two lower identities.

Proposition 2 proves a restriction of the selected representation only. It cannot justify a coordinator-led weakening of S1. The local fourth-moment divergence excludes the separately imposed finite-fourth-moment subclass, while S1 itself permits those infinite moments. Neither conclusion permits an altitude cutoff, dropping an order, switching to cumulants, restricting intensity or changing the diameter quantifier.

No amendment was requested in this first submission. This review preserves S1 and the attempt count. Attempt 1 of 4 is unsuccessful against S1; the established partial result remains available to this track. A later construction-driven amendment would require the stipulated attempt and owner-approval procedure. No approval is supplied or inferred here.

S0 is a separate frozen historical target. Its existing verdict and amendment authority are not reopened by this review; this partial local result would in any event not establish the unrestricted S0 identities.

## Source and coding evidence

The only mathematical seed excerpt supplied was `cited_seed_section_5.md`, SHA-256 `33d1beb4f10940ad56067e341898fdb5ad5fd19b4bd11db8222f336de79a8432`, with provenance JSON SHA-256 `5e9017cd19d28947680730c5e7ddbee4e70311c83759e6670ac343b1088a2aa3`. Its explicitly invoked lead is the affine-coordinate determinant $6V$. That determinant has been independently checked above. The excerpt itself states that its shot-noise expression is a factorial cumulant, with additional full-density terms; the present submission does not treat that old construction as a full-density solution.

No theorem about the old shot-noise process is needed for the new law. The seed's entire separate construction has therefore not been certified in this review, and its provenance metadata has not been used as a substitute for mathematical verification. The historical DVJ and Kagan claims were not needed to prove the present assertions; no literature-status, priority or novelty conclusion is made.

The dependencies actually used are conditional Poisson factorial moments, Tonelli, dominated convergence, elementary Euclidean slicing, elementary linear changes of variables and polynomial zero-set nullity. Their needed forms and hypotheses were checked directly. No missing specialised source passage was identified, so no coordinator source request was necessary.

Tools were used to verify input hashes, read only the authorised packet, extract own-session metadata and numeric token telemetry, and create/freeze assigned review artifacts. No numerical experiment, simulation, symbolic-package check or proof-assistant certification was used. The mathematical checks in this report are analytic.

## Presentation judgement

The submission is readable and unusually clear about the distinction between its partial theorem and S1. It defines the actual law before calculating densities, gives the full allocation formula before discarding any terms, and separately handles global fourth-density finiteness and local count moments. Those choices make the consequential dependencies recoverable.

The main improvements are small: specify the canonical density convention in Proposition 2; repair the strict endpoint inequality; and add the short observation that resonance configurations cannot intersect $E_4(M)$ if the pointwise local claim and the null-set reassignment are retained together. The amplitude/area distinction is already stated and maintained. Administrative history and accounting can be kept outside a future mathematical exposition, while remaining appropriate in the experimental submission record.

## Review summary and repairs

The finite slab width supplies a diffuse conditional Poisson law. A global random phase gives stationarity. Separation eliminates distinct-slab allocations only where the local diameter condition permits that elimination, and cancellation of the fourth amplitude power then gives the exact inverse determinant. Away from that local domain, finite allocation bounds and a countable polynomial resonance set supply global finite-almost-everywhere fourth densities. Integrated count estimates prove finite third moments, while the reciprocal-volume identity forces infinite fourth moments locally.

The lower-order amplitude powers do not cancel. Their verified explicit formulas fail both missing target identities, and the radial slab proposition shows that merely changing the stated radial marks, finite amplitudes and separated periods cannot fix the pair law within that class. Obtaining all three full identities simultaneously remains the substantive unresolved obligation. Independent superposition is not an established repair because its extra full-density allocations would need a new exact analysis.

The two precision repairs do not require weakening Theorem 1 or changing S1. This report approves the advertised partial theorem and scoped obstruction as informal mathematics, subject to the stated canonical-density convention, while recording an unsuccessful first attempt against the complete S1 target. It supplies no final cross-track synthesis.

## Accounting and freeze

`preflight.json` contains verified own-session/model/effort evidence and the first exposed numeric token checkpoints. `usage_checkpoint.json` records the later exposed checkpoint and its exact session line. Cumulative snapshots are not summed. Runtime-reported reasoning output is not added a second time to inclusive output. No children were dispatched. Parent aggregation semantics and actual monetary charges are NR.

The current turn's completed totals, including text after the final extracted checkpoint, are NR at report freeze and require coordinator reconciliation after turn completion. No estimates are presented as measurements. `review_freeze.json` records the report's SHA-256, size, word count and freeze timestamp externally, avoiding a self-referential hash.
