# Review — proof_4 / submission v02 / target S1

- Reviewer: `/root/review_proof_4_v02`, fresh independent reviewer.
- Session: `session-16`; turn: `turn-28`.
- Requested and runtime-verified model/effort: `gpt-6-astra`, `xhigh`.
- Session start: `2026-10-20T18:00:46.544Z`. Review completion and freeze time are recorded in `review_freeze.json`.
- Active statement: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Reviewed submission: `reviews/proof_4_v02/proof_snapshot.md`, SHA-256 `9a3befd21f85424fea521c9c817837f2d943a1a0862c0e1586541b93c5d559ac`, substantive submission 2 of 4.
- Main dispatch: `packets/review_proof_4_v02.json`, SHA-256 `0662e1c5a6c683e557638b04a933e29514ccfd520a425a3d325cb82a10c5aece`.
- Source supplement: `packets/review_proof_4_v02_source_01.json`, SHA-256 `dbea889efc0861c1e43d0359d2262ee321722994980c2214797641b8a5035cab`.
- Consequential earlier proof: `prior_dependency_v01.md`, SHA-256 `57b1c58f13fa055c76cfec22c131b989b32bef3b1414cd710992ad6f081158b5`.
- Prior concrete issue table: `previous_issue_list_v01.md`, SHA-256 `42e491b8ba961496cacb8607d704bf2fd9c37a5f4070ed09048939eb6a9c33e5`.

All paths above are relative to the run root unless they name files in this review directory. Both packets and every enumerated allowed-file hash were checked. The review used the supplied frozen instructions, workflow, target and amendment, proof-reviser skill and its two required references, the complete current proof, the supplied earlier proof, the concrete issue table and the two exact seed excerpts. It did not use author conversations, private work, the full previous review, other construction tracks, other chats or old runs. Statements in the manuscripts that earlier work was “accepted” were not treated as mathematical evidence.

The own-session preflight preceded mathematics. The `turn_context` at runtime line 8 verifies the model, effort and turn identifier above; numeric `token_count` fields were exposed. `preflight.json` preserves the metadata-only evidence. No delegation occurred.

## Correctness verdict and scope

**The reviewed informal argument establishes Theorem 1 on its stated restricted parameter range and establishes the representation-specific obstruction in Theorem 2. It does not establish S1.**

More precisely, for every $M>0$ and every $\lambda>0$ with $\lambda M^3\leq\tau$, with exactly the positive constant $\tau$ in equation (1), the construction supplies one whole-space stationary, isotropic, simple, almost surely locally finite process of intensity $\lambda$. Its full factorial measures of orders two, three and four are globally absolutely continuous with finite-almost-everywhere densities, and all three required reciprocal formulas hold simultaneously on all of $E_n(M)$. The finite third and infinite fourth local moment assertions also follow.

Theorem 2 proves that a mixture of the particular slab law (5) with a process partitioned into separated clusters of at most three points, under its stated hypotheses, must satisfy
\[
a_2\geq 2\pi^2M^2a_3,
\qquad
\lambda M^3\leq18/\pi.
\]
These are necessary conditions for that representation. They are not necessary conditions established for an arbitrary S1 process. The proof does not classify the interval between the sufficient threshold $\tau$ and this representation ceiling, and neither constant is proved sharp.

The all-intensity requirement in S1 remains unresolved. Submission 2 is therefore a **valid partial construction plus a valid scoped obstruction, and an unsuccessful submission against the complete active target**. This distinction is already made accurately in the submission. No invalid essential inference or unresolved mathematical dependency was found in the two stated restricted theorems after re-establishing their inherited dependencies. This is a complete informal audit of the submitted mathematics needed for those conclusions, not formal verification or a review of the wider literature.

## Reconstruction and detailed audit

### 1. Exact quantifiers and dependency structure

S1 requires every independently prescribed pair $(\lambda_0,M)$, all three orders on the full nondegenerate domains below diameter $M$, an actual process on all of $\mathbb R^3$, and global full absolute continuity with finite-almost-everywhere densities. It does not require finite fourth local moments, a particular representation or ergodicity.

The present construction uses two actual laws with the same prescribed intensity. The slab component $Y$ supplies the fourth law and explicit lower densities. The component $C$ supplies residual second and third densities and has no eligible local quadruples. A single coin chooses the law on the whole space. This makes full factorial measures combine linearly.

The consequential dependency chain is:

1. Existence, full densities, global regularity and moment properties of the scaled slab component.
2. Positivity and finite anchored masses of the residual kernels.
3. A genuine stationary separated-parent process and a normalised independent mark law.
4. Correct ordered-selection factors for the offspring, local parent exclusion and global regularity of the resulting process.
5. Linear combination of the two full laws.
6. A separate deterministic cluster inequality, two coalescence limits and finite third-moment inequalities for Theorem 2.

Each of these was checked. In particular, the old partial theorem was not imported solely because a previous report approved it.

### 2. Re-establishing the slab probability law and normalisation

For fixed $M$, the mark density and phase distribution in (5) are bona fide probabilities. With $w=Mv$,
\[
\int_{\mathbb R^3}H_M(v)^{-3}\,dv=M^{-3}J,
\qquad
\int_{\mathbb R^3}T_M(v)H_M(v)^{-4}\,dv=M^{-3}Z_0.
\]
The constants are correct. In radial coordinates the needed integrals are
\[
\int_0^\infty\frac{r^2}{(1+r^2)^3}\,dr=\frac{\pi}{16},
\quad
\int_0^\infty\frac{r^2}{(1+r^2)^4}\,dr=\frac{\pi}{32},
\quad
\int_0^\infty\frac{r^3}{(1+r^2)^4}\,dr=\frac1{12}.
\]
Thus $J=\pi^2/4$ and the period $2+2|w|$ gives $Z_0=\pi^2/4+2\pi/3$.

For every realised finite mark, at most one interval indicator contributes at any spatial point. Therefore
\[
0\leq\Lambda_Y(x)\leq sH_M(W)<\infty.
\]
The countable indicator sum is measurable, and the conditional Poisson process has a diffuse locally finite intensity measure. The construction using an independent Poisson measure on space times a height coordinate in v01 gives a measurable whole-space law. Conditional local finiteness and simplicity, followed by a countable covering by bounded cubes, establish the corresponding almost-sure global properties.

A translation shifts the uniform phase modulo its period; a rotation rotates the radially distributed mark. These observations establish stationarity and isotropy without any mixing claim. Phase averaging contributes $1/T_M(v)$, so
\[
\mathbb E\Lambda_Y(x)
=\frac{s}{Z_M}\int H_M(v)^{-3}\,dv
=\frac{sJ}{Z_0}=\lambda.
\]
There is no intensity restriction on this component alone.

The asserted dilation is also correct: dilating the $M=1$ process of intensity $\lambda M^3$ by $M$ divides its spatial intensity by $M^3$ and changes the mark from $w$ to $v=w/M$. The physical amplitude becomes $sH_M(v)$ as in (5). This correctly transports the partial slab theorem but leaves the dimensionless product $\lambda M^3$ unchanged.

### 3. Full slab measures, local formulas and the scaling constants

For a nonnegative test function, conditional Poisson factorial moments give
\[
\alpha_Y^{(n)}(d\mathbf x)
=\mathbb E\!\left[\prod_{i=1}^n\Lambda_Y(x_i)\right]d\mathbf x.
\]
Conditional expectations and all subsequent sums/integrals are nonnegative, so Tonelli applies even at fourth order when local mass is infinite. This is an identity of full measures, not a cumulant formula. A Lebesgue-null configuration set receives zero mass; possible infinite values of the displayed density on that set create no singular component.

Re-expanding the phase and every slab index gives the scaled form of v01 equation (9):
\[
\frac{s^n}{Z_M}\sum_{m\in\mathbb Z^{n-1}}
\int_{\mathbb R^3}\int_{\mathbb R}
H_M(v)^{n-4}h(-b)
\prod_{i=2}^n h(v\cdot u_i-b-m_iT_M(v))\,db\,dv.
\]
Summing the first slab index tiles the entire phase line, and the density-to-period ratio is $1/(Z_MH_M^4)$. No allocation is omitted.

If the tuple diameter is less than $M$, any nonzero index difference would imply
\[
|v\cdot u_i-m_iT_M(v)|
\geq T_M(v)-|v|\,|u_i|
=2+(2M-|u_i|)|v|\geq2,
\]
whereas two nonzero interval indicators require that difference to have absolute value less than one. This eliminates every nonzero allocation. The non-strict final bound includes $v=0$ and repairs R4-04.

For a noncoplanar quadruple the affine coordinate map has absolute determinant $6V$. The fourth amplitude power cancels the mark weight, and the product of four unit interval integrals equals one. This proves
\[
r_4=\frac{s^4}{6Z_MV}
\]
on the entire required local domain.

At order two, integration over the free two-dimensional normal coordinate gives
\[
\int_{\mathbb R^2}
(1+M^2\beta^2+M^2|z|^2)^{-2}\,dz
=\frac{\pi}{M^2(1+M^2\beta^2)}.
\]
Together with the Jacobian $1/d$ and $Z_M=M^{-3}Z_0$, this gives exactly $c_2=\pi s^2M/Z_0$ and $\Phi(d/M)$ in (6).

At order three, the affine coordinate Jacobian is $1/(2A)$ and the remaining line integral is
\[
\int_{\mathbb R}
(1+M^2|v_0|^2+M^2z^2)^{-1}\,dz
=\frac{\pi}{M\sqrt{1+M^2|v_0|^2}}.
\]
This gives exactly $c_3=\pi s^3M^2/(2Z_0)$ and $\Psi_M$ in (7). Both factors are positive and at most one. Symmetry of the resulting densities follows directly from the expected-product expression, even though the anchored formulas single out a vertex.

The two old failures remain genuine failures of $Y$: $\Phi(t)\to0$ as $t\downarrow0$, so $dr_2(d)\to0$; under a collapse of a noncollinear triangle, $\Psi_M$ tends to zero by bounded convergence. They are corrected in the mixed law, not disproved as statements about the old slab law.

### 4. Global slab regularity and count moments

Local reciprocal formulas do not suffice to check global finite-almost-everywhere densities. The separate resonance argument in v01 is valid and remains valid under scaling.

For an affinely independent quadruple, let $U$ have rows $u_i^\top$, put $L=2M$, and set $R=\max_i|u_i|$. A nonzero allocation term must satisfy
\[
|m_i|\leq\frac{|v|R+1}{L|v|+2}
\leq\max\{R/L,1/2\}.
\]
Hence only finitely many integer vectors can contribute at that fixed configuration. For one such vector, $w=U^{-1}m$ obeys
\[
|v-L|v|w|\leq 2|w|+\sqrt3\,\|U^{-1}\|.
\]
Unless $L|U^{-1}m|=1$, the reverse triangle inequality bounds $|v|$. The phase coordinate is also bounded by its indicator, and the fourth-order integrand is at most one. Each such term consequently has finite integral.

For each fixed nonzero $m$, the resonance equation is contained in the zero set of
\[
L^2|\operatorname{adj}(U)m|^2-(\det U)^2.
\]
This polynomial is not identically zero: at $U=tI$ it is $L^2t^4|m|^2-t^6$. Its zero set is null, as is $\det U=0$. The countable union over integer $m$ is null. The change from original coordinates to $(x_1,U)$ is an invertible linear map, so the nullity transfers to the original configuration space. This proves the global fourth-order assertion.

A local quadruple cannot be resonant: if $L|U^{-1}m|=1$, then $|m_i|\leq |u_i|/L<1$, forcing every integer component to vanish, which contradicts the resonance. Thus the optional reassignment of density values on the global exceptional set does not alter the local fourth formula.

For finite third count moments, the earlier slab slicing argument is also sound. For large radial mark $r$, only a bounded number, depending on the observation ball and $M$, of slabs meet the ball. Each intersection has volume bounded by a constant times $1/r$. The amplitude is of order $r^2$, so the conditional Poisson mean is bounded by a constant times $1+r$. The radial mark probability density has tail of order $r^{-5}$, and its third moment is finite. Conditional Poisson raw-moment identities then give a finite third count moment in each bounded set. This also makes the full densities of orders two and three locally integrable and finite almost everywhere globally.

For any open ball, choose a smaller ball of diameter below $M$. For almost every noncollinear base triple inside it, there is a planar disc and a nonzero normal interval for the fourth vertex still lying inside the ball. With base area $A$ and normal height $t$,
\[
V=A|t|/3.
\]
The fourth density therefore has an infinite fourth-vertex integral proportional to $\int_{0<|t|<\delta}|t|^{-1}\,dt$. Tonelli proves an infinite fourth factorial and raw count moment. This is compatible with almost-sure local finiteness and finite first three moments. The same argument independently rules out the additional finite-fourth-moment comparison subclass for any law with the local fourth reciprocal formula.

For completeness, the corrected old Proposition 2 was also rechecked. Its canonical radial pair density is an integral of $\omega(r)H(dr)$, with $H(z)=4\pi(1-z/2)$ up to one and $H(z)=2\pi/z$ thereafter. For fixed $r$, $dH(dr)$ is nondecreasing in $d$ and tends to zero as $d\downarrow0$. Finiteness of this canonical integral at $d_0$ supplies integrable domination by $\omega(r)d_0H(d_0r)$. This proves its limit and exclusion of an a.e. reciprocal law. Reading the premise in this canonical sense, as v02 expressly does, resolves R4-03. No arbitrary value of a density on one distance sphere is used.

### 5. Residual positivity and finite masses

The constants and the marginal inequality in (11)–(12) are correct. For a nondegenerate pair of length $d<M$, cylindrical coordinates about its line give
\[
\int_{B(x_1,M)}\frac{dz}{\operatorname{dist}(z,\ell)}
=4\pi\int_0^M\sqrt{M^2-r^2}\,dr
=\pi^2M^2.
\]
Since area is $d\,\operatorname{dist}(z,\ell)/2$, this gives $\mathcal MK_3\leq B_3K_2$ with $B_3=2\pi^2M^2$. Outside the pair support the triangle kernel is zero. Also $I_2=4\pi\int_0^M r\,dr=2\pi M^2$. Degenerate sets may be assigned zero throughout these computations.

Substitution of $s=\lambda Z_0/J$ shows that the second and third terms defining $\tau$ are exactly sufficient for $c_2\leq a_2$ and $c_3\leq a_3$. In particular, the latter condition is
\[
(\lambda M^3)^2\leq\frac{J^3}{32\pi^4Z_0^2};
\]
the square and every power of $M$ are correct.

Consequently
\[
a_jK_j\leq q_j\leq2a_jK_j,\qquad j=2,3.
\]
The choice $a_3=a_2/(4B_3)$ gives
\[
F_2=q_2-\mathcal Mq_3
\geq(a_2-2a_3B_3)K_2
=\tfrac12a_2K_2.
\]
Thus the subtraction is of finite functions on the nondegenerate local domain and defines a nonnegative kernel. Its anchored integral is finite. The same holds for $F_3=q_3$ by the marginal bound. These kernels retain translation invariance, rotational invariance and the needed permutation symmetry; marginalising a symmetric third kernel leaves a symmetric pair kernel.

Tonelli gives
\[
Z_3=Q_3,\qquad Z_2=Q_2-Q_3>0,
\quad Q_2\leq\lambda/2,\quad Q_3\leq\lambda/8.
\]
Strict positivity follows either from the pointwise lower bounds on nonempty open domains or by integrating $F_2\geq a_2K_2/2$. There is no subtraction of infinite masses and no zero normalising denominator.

### 6. Actual retained-parent process and probability normalisation

The retained process is well defined by a measurable local thinning of the initial Poisson process. The insertion identity (21) follows by the displayed finite-region Poisson calculation and extension of nonnegative tests. Applying it to the local void event yields
\[
\kappa=\eta e^{-\eta v_h}=\frac1{36e\pi M^3},
\qquad v_h=\frac{4\pi}{3}(3M)^3=36\pi M^3.
\]
Stationarity and isotropy are preserved. No pair of retained centres can have distance less than $3M$. Equality has probability zero by the diffuse two-point factorial measure of the original Poisson process, followed by a countable exhaustion. Thus the strict separation needed later holds almost surely throughout space.

The supplied marks really are probabilities. Writing
\[
\beta=\lambda-Z_2-Z_3/2=\lambda-Q_2+Q_3/2,
\]
we have $\beta\geq\lambda/2>0$. The total nonempty marking rate satisfies
\[
\kappa(p_1+p_2+p_3)
=\beta+Z_2/2+Z_3/6
=\lambda-Q_2/2+Q_3/6
\leq\lambda\leq\kappa.
\]
The penultimate inequality follows from $Q_3\leq Q_2$; the last is exactly the first condition in the minimum defining $\tau$. This proves $p_0\geq0$, with all other probabilities nonnegative. The endpoint $\lambda M^3=\tau$ is covered by these non-strict estimates.

The relative-coordinate densities $F_j(0,\cdot)/Z_j$ have total mass one and are diffuse. Every emitted cluster has diameter less than $M$ and contains its parent, so all its points lie within distance $M$ of the parent. Two different retained clusters therefore have mutual point distance greater than $3M-2M=M$. This proves the exclusion for actual point configurations, not just for their formal kernels.

### 7. Ordered selections, all parent allocations and global regularity of \(C\)

The factors in (25)–(28) are correct despite the fact that one emitted point is the distinguished parent. For a size-$j$ mark, integration over the parent location and all offsets has joint density
\[
\frac{\eta p_j}{Z_j}F_j(x_1,\ldots,x_j)
\]
in the full labelled positions, where the first coordinate initially denotes the parent. Re-rooting at any selected point and relabelling has absolute Jacobian one; translation invariance and permutation symmetry preserve $F_j$. Each of the $j!/(j-k)!$ ordered selections of $k$ points therefore gives the same marginal. This justifies (25), including selections that do not include the original parent.

Assigning tuple labels to distinct original Poisson parents yields exactly the partition sum (26). For clarity, through order four this includes the following types:

| Order | Parent block types in \(U\) |
|---|---|
| 2 | one block of size 2; two blocks of size 1 |
| 3 | one block of size 3; three choices of types \(2+1\); type \(1+1+1\) |
| 4 | four choices of types \(3+1\); three choices of types \(2+2\); six choices of types \(2+1+1\); type \(1+1+1+1\); the single size-4 block is zero |

These are all partitions, with the usual labelled arguments in their products. The multi-parent terms are retained in the global formula for $U$; they are not incorrectly discarded on the basis of the thinning.

Attaching marks before thinning couples $C$ as a subset of $U$. For a bounded observation set $B$, at most the finitely many original Poisson centres in its $M$ enlargement can contribute, and
\[
U(B)\leq3\Pi(B^{+M}).
\]
The right-hand side has moments of every order. Relative-coordinate diffuseness and diffuse parent positions also give simplicity, including possible inter-cluster coincidences, by a countable pair argument.

Equation (26) proves full absolute continuity of $U$; the local moment bound implies its densities are finite almost everywhere on bounded product cubes and hence globally. For every nonnegative tuple test,
\[
\alpha_C^{(n)}\leq\alpha_U^{(n)}.
\]
Domination by this locally finite absolutely continuous measure gives globally absolutely continuous, finite-almost-everywhere densities for $C$. This also checks the unrestricted region outside $E_n(M)$. It neither presumes independent retained parents nor transfers their Poisson factorial measures incorrectly.

On $E_n(M)$ every tuple belongs to one retained cluster. Only the first intensity $\kappa$ is therefore needed, with marks independent of the retention test. Substituting the probabilities into the ordered-selection factors gives
\[
\kappa p_2\frac{2!}{Z_2}=1,\qquad
\kappa p_3\frac{3!}{Z_3}=1.
\]
Hence
\[
\rho_C^{(2)}=F_2+\mathcal MF_3=q_2,\quad
\rho_C^{(3)}=F_3=q_3,\quad
\rho_C^{(4)}=0
\]
on the respective local domains. The intensity is
\[
\kappa(p_1+2p_2+3p_3)
=\beta+Z_2+Z_3/2=\lambda.
\]
This confirms both the factorial combinatorics and the singleton compensation.

### 8. Simultaneous identities and moments of the mixture

The whole-space mixture in (29) is a valid law. For every nonnegative tuple test, conditioning on its single coin gives the extended measure identity
\[
\alpha_X^{(n)}
=\tfrac12\alpha_Y^{(n)}+\tfrac12\alpha_C^{(n)}.
\]
There are no tuples joining the alternative laws because they are alternatives in the probability space. Each alternative was already audited as a full process, including its own allocations.

Consequently the local second and third densities are exactly $a_2K_2$ and $a_3K_3$. The fourth coefficient is
\[
a_4=\frac12\frac{s^4}{6Z_M}
=\frac{s^4M^3}{12Z_0}>0.
\]
All three coefficients are finite, positive and independent of the configuration. The same law and the same parameters give all three identities. The finite union of the exceptional sets for the three orders causes no simultaneous-version issue.

The mixture preserves stationarity, isotropy, simplicity, local finiteness, the prescribed intensity and global full absolute continuity with finite-almost-everywhere densities. Finite third moments follow componentwise. Positive probability of selecting $Y$ transfers its infinite fourth moments to $X$ by nonnegative expectation. Thus every assertion of Theorem 1, including its absence of lower shape cutoffs, is established on its stated range.

### 9. Theorem 2: cluster inequality and coalescence limits

The proof covers $\theta=0$ as well as $0<\theta<1$. At $\theta=1$, the canonical slab pair formula excludes the required pair law. For $\theta<1$, domination by the mixed factorial measure transfers absolute continuity to $C$ at the needed orders. On the local domains the mixed reciprocal densities are finite and locally integrable at orders two and three, so no undefined subtraction of infinite quantities is needed.

In a realised $C$, an ordered pair of distance less than $M$ must belong to the same cluster. There is at most one additional point in that cluster, and a point from another cluster cannot form a triple of diameter less than $M$. Thus the number of eligible third extensions of the pair is at most one. Integration against a pair test and expectation gives (33) as an inequality of measures and hence of densities almost everywhere. No independence or stationarity of the cluster partition is needed for this deterministic implication.

Substituting the two local density identities for the mixture yields (34). The resulting expression is translation invariant and radial in the pair separation. Fubini in the translation coordinate and polar coordinates in the separation therefore justify an almost-everywhere statement in $d$. The proof does not evaluate arbitrary Radon–Nikodym versions on a single fixed ray.

For the pure geometric term,
\[
dL_M(d)=2\int_{B(0,M)\cap B(de,M)}|z_\perp|^{-1}\,dz.
\]
The integrand is dominated by an integrable function on $B(0,M)$, whose integral was computed above. Boundary points and the line $z_\perp=0$ form null sets. Dominated convergence gives the exact limit $B_3$.

For the slab triangle term, the constraint $v_0\cdot de=q_2-q_1$ yields $|v_0|\geq|q_2-q_1|/d$. For almost every phase triple this tends to infinity. Bounded convergence in phase variables proves $\Psi_M(de,z)\to0$ for fixed $z_\perp\neq0$. The spatial integrand then obeys
\[
0\leq d\,\mathbf1_{E_3(M)}r_3(0,de,z)
\leq 2c_3\mathbf1_{B(0,M)}(z)|z_\perp|^{-1}.
\]
A second justified dominated-convergence application gives $dR_M(d)\to0$. This argument requires neither a uniform triangle-shape cutoff nor finite fourth moments. The pair formula gives $dr_2(d)\to0$ independently.

Taking (34) along a sequence from its full-measure distance set tending to zero therefore yields $a_2\geq B_3a_3$. The factors $\theta$ and $1-\theta$ have been handled correctly: the former contributions vanish in the limit, and the latter was removed by multiplying the deterministic component inequality before substitution.

### 10. Theorem 2: count inequality and exact ceiling

For a ball of radius $r<M/2$, every pair and every noncollinear triple in the ball lies in the local formula domains. The pair kernel is integrable, and the triangle marginal bound proves integrability of the triangle kernel. Thus the actual count $N$ has finite first three moments under the hypotheses of Theorem 2.

Write $\mu=\mathbb EN=\lambda(4\pi/3)r^3$ and use $F_2,F_3$ here for its second and third factorial moments, as in the submission. The geometric bound and the newly established coefficient inequality imply
\[
F_3
\leq a_3B_3\int_{B(0,r)^2}D^{-1}
\leq a_2\int_{B(0,r)^2}D^{-1}=F_2.
\]
This is where the representation-specific coefficient restriction enters; it is not a general S1 inequality.

Since $F_2>0$ and all quantities are finite, Cauchy–Schwarz gives
\[
F_2^2
\leq\mathbb EN\,\mathbb E[N(N-1)^2]
=\mu(F_3+F_2)
\leq2\mu F_2.
\]
The algebraic identity $N(N-1)^2=(N)_3+(N)_2$ is exact, including $N=0,1$. Dividing by $F_2$ and using nonnegative variance gives
\[
\mu^2\leq\mathbb EN^2=F_2+\mu\leq3\mu,
\]
so $\mu\leq3$. Finally $r\uparrow M/2$ yields
\[
\lambda\frac{\pi M^3}{6}\leq3,
\qquad\lambda M^3\leq18/\pi.
\]
Only a limit of deterministic inequalities is used in the last step. No limiting process construction, finite fourth moment or assertion at the diameter boundary is hidden there.

The theorem establishes exactly its stated necessary ceiling. It leaves processes using larger clusters, different slab laws, other geometrical mechanisms or an entirely different representation outside its scope. It also leaves sufficiency below that ceiling unresolved.

## Finding register

| ID | Location | Precise mathematical issue or verified finding | Consequence | Repair/status |
|---|---|---|---|---|
| R4-01 | v01 lower pair formula; v02 (6), (14), (27), (30) | The slab law still has \(dr_2(d)\to0\), but the valid residual component exactly adds the missing pair term in the mixed law when \(\lambda M^3\leq\tau\). | The old pair-law failure is repaired for the new process in the proved range only. | Closed on the stated range; all-intensity scope remains under R4-05. |
| R4-02 | v01 lower triangle formula; v02 (7), (14), (27), (30) | The nonconstant slab factor is exactly corrected by the nonnegative residual triangle kernel in the same mixed law. | The triangle identity and the fourth identity now hold simultaneously with the pair identity in the proved range. | Closed on the stated range; not a proof for all S1 parameters. |
| R4-03 | v02 Section 2 and response table; v01 Proposition 2 | The finiteness premise is explicitly interpreted using the canonical expected-product/integral density. | The domination argument is not based on an arbitrary value on a null distance sphere. | Precision correction verified; the scoped old proposition remains valid. |
| R4-04 | v02 Section 2, slab-index bound | The replacement bound is \(2+(2M-|u_i|)|v|\geq2\), which includes \(v=0\). | Every unwanted local slab allocation is excluded without the old strict-endpoint slip. | Correction verified; dependent formulas rechecked. |
| R4-05 | Theorem 1, (1)–(2), Section 7; S1 acceptance | The construction imposes \(\lambda M^3\leq\tau\), whereas S1 quantifies over every independently prescribed positive pair. Dilation preserves this product. | Submission 2 is not an exact-target pass; the missing parameter regime is a substantive unresolved target obligation. | Open for S1. A new argument or an explicitly authorised amendment would be needed; none is supplied or adopted. |
| R4-06 | Theorem 2, (32)–(37) | The coefficient restriction and ceiling follow from the specific slab-plus-separated-small-cluster representation. | Valid obstruction within that representation; no general upper-intensity obstruction for S1 follows. | Scoped theorem verified. No coordinator-led target restriction is justified by it. |
| R4-07 | Section 4, (20)–(28) | The retained centres are dependent, but only their first intensity is used locally; global regularity follows from domination by the unthinned marked Poisson cluster process. The mark probabilities and ordered factors are correct. | The residual hierarchy is realised by an actual process, with the prescribed intensity and full measures. | Critical construction check closed; no independence gap found. |
| R4-08 | Section 2 and v01 Sections 3–6; Section 5 | Local formulas are supplemented by a valid global resonance argument for \(Y\), domination for \(C\), and the full measure mixture identity. | No omitted singular mass or unproved outside-domain density assertion remains in Theorem 1. | Global requirements verified, including finite-almost-everywhere fourth density despite infinite local fourth mass. |
| R4-09 | “accepted v01” wording in Sections 1–2 and sources | Earlier approval labels do not supply proof of the inherited assertions. The current packet contains the earlier mathematical argument, which was independently re-established here. | No outstanding dependency gap in this review; standalone readers still need the stated earlier lemmas or the supplied appendix. | Exposition improvement: cite exact prior theorem/sections as dependencies and avoid using acceptance as their justification. |
| R4-10 | Moment assertions and finite-moment comparison | The local reciprocal-volume law forces infinite fourth moment in every nonempty ball; this is compatible with the actual construction’s almost-sure local finiteness. | The finite-fourth-moment comparison subclass is impossible, while the broad local target remains meaningful. | Verified distinction; no fourth-moment hypothesis may be silently added to S1. |

## Amendment implications

No amendment is proposed in v02, and this review adopts none. S1 remains the active target with its recorded hash. Theorem 1's restricted intensity range is a valid partial theorem, not a replacement statement.

Theorem 2 cannot justify a general intensity cap under the coordinator's general-obstruction authority. Its decisive inequality comes from separated clusters of at most three points together with the particular slab component. Failure or bounded capacity of that representation does not establish non-existence for the unrestricted S1 process class.

The local fourth-moment divergence rules out only the separately stated finite-fourth-moment comparison subclass. It does not force a lower altitude cutoff in the broad target. The present audit accepts the frozen S0-to-S1 amendment as supplied target authority; it does not independently re-audit the unassigned historical global obstruction proofs or revise the historical S0 record.

This is attempt 2 of 4. A possible owner checkpoint after three unsuccessful reviewed submissions has not yet been reached, and an eventual proposal would not itself constitute approval. No attempt counter resets or silent changes of quantifiers follow from these results.

## Source and coding evidence

The mathematical proof is self-contained after including the supplied v01 dependency. The external facts used are elementary conditional Poisson factorial identities, the explicitly justified Poisson insertion identity, linear changes of variables, Tonelli, dominated convergence, polynomial zero-set nullity and Cauchy–Schwarz. Their relevant hypotheses and applications were checked above.

The exact seed Section 5 excerpt, SHA-256 `33d1beb4f10940ad56067e341898fdb5ad5fd19b4bd11db8222f336de79a8432`, supplies historical provenance for the affine determinant idea. It explicitly concerns a fourth factorial cumulant. This review did not transfer its formula to a full density; the actual full slab formula was independently rederived.

The exact seed Section 2 excerpt, SHA-256 `3ffdfb4275aa3432569d79eef60e2bcce6559c766c468b78c190e75f2a2ad658`, supplies provenance for residual-kernel algebra. Its brief reference to earlier notation is not needed to establish the new result: equations (11)–(28) in v02 specify and justify all kernels, bounds and probabilities afresh. No broader seed theorem is approved through that excerpt.

The neutral source index and DVJ context were read. No source-specific theorem, current literature-status assertion, priority claim or unverified published result is needed for the verdict. No additional source request or coder request was necessary. Administrative packet/file hashes and own telemetry were checked programmatically. No numerical continuum test, simulation, symbolic proof package or proof assistant was used or claimed.

## Presentation judgement

The submission states its restricted scope clearly, explains why a mixture is used, and separates the sufficient construction range from the necessary ceiling for its representation. The explicit mark probabilities and global domination argument make the new law substantially easier to audit than a purely formal density prescription.

The main useful improvement is to present the retained slab facts as a named dependency with exact prior sections, or reproduce them in an appendix, rather than repeatedly describing them as “accepted”. The reader needs the global resonance and moment lemmas as well as the local formulas. This review has checked those supplied lemmas, so this is an exposition recommendation rather than an unresolved correctness issue.

A compact display of the one-cluster ordered-selection coefficients, and an explicit reference to the all-partition formula for the dominating process, would further help readers unfamiliar with anchored clusters. The mathematical content for both is already present. Reusing \(F_2,F_3\) for factorial moments in Theorem 2 is locally defined and unambiguous, though separate notation could ease reading.

## Review summary and repairs

The old lower-order failures are corrected by a genuine alternative process on the stated small-intensity range. The residual kernels are positive and integrable; the parent thinning and marks have the claimed intensity; re-rooting gives the correct factorial factors; separation proves the local exclusion; and domination establishes the full global measure requirements. The fourth formula survives the whole-law mixture exactly.

The separate obstruction also holds: coalescing a pair removes both slab lower-order contributions at the relevant scale, forcing a coefficient inequality from the small-cluster count restriction. Integrability of the local pair and triangle kernels then permits a finite third-moment argument yielding the exact ceiling \(18/\pi\). Its scope remains representation-specific.

No mathematical repair is required for Theorems 1 and 2 as stated. The unresolved task is the general S1 existence question beyond the sufficient range, not an unproved step inside these restricted theorems. Neither optimisation of the present constants, dilation, nor an asserted independent superposition supplies that missing result. There is no general non-existence conclusion from this attempt.

## Accounting and freeze evidence

`preflight.json` records the exact own-session model/effort and numeric token evidence available before mathematics. `usage_evidence.json` records the latest exposed checkpoint used at review freeze, its event timestamp and runtime line, and the coverage limits. `review_freeze.json` records this report's SHA-256, byte/word counts and freeze time.

Runtime cumulative checkpoints are not summed. Reported reasoning output is a subset of the exposed output and is not added again. No children were launched; parent aggregation semantics remain NR. Completed-turn totals after the final response, actual monetary charges and unavailable accounting fields remain NR/null pending coordinator reconciliation. No estimate is substituted for a measurement.

## Final synthesis only

Not applicable. This report reviews only the assigned track's second submission and its explicit dependencies; it does not compare other tracks.
