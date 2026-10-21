# Review — proof_3 v04 against S1

- Review type: fresh independent extensive review of the fourth and final submission and its supplied dependencies; not cross-track final synthesis.
- Reviewer: `/root/review_proof_3_v04`, thread/session `session-22`, turn `turn-34`.
- Requested and independently verified own runtime: `gpt-6-astra`, `xhigh`. Own `turn_context` line 8, timestamp `2026-10-20T18:46:47.104Z`, supplies the model, effort and turn ID. Preflight evidence was saved and reported to the coordinator before mathematics. Review completion time and exposed usage checkpoint are recorded separately.
- Setup root: `$SETUP`.
- Run root: `runs/20261020T164437Z_astra6/` under that setup root. Relative paths below resolve against the run root unless stated otherwise.
- Packet: `packets/review_proof_3_v04.json`, SHA-256 `822a6208eafc5116c2e02d05e26e74c483ac053f758a3458a17fa7bd64416668`.
- Target: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Adopted change: `statements/S0_to_S1.md`, SHA-256 `b2534040520dfc63bf5c22ecc508257308e619a040a7c6c54ce44375742394de`. No subsequent amendment is supplied or inferred.
- Submission: `reviews/proof_3_v04/proof_snapshot.md`, SHA-256 `0cffc5a62fec3725f6cad6a839bb9cb2125b4ef8d9d6bfe89ca471635a4062db`.
- All packet-listed file hashes matched. The exact checks are in `input_hash_verification.json` beside this report. Frozen procedural inputs and the complete proof-reviser skill references were read.
- Context received: the target, adoption record, current proof, this track's three frozen prior proofs, their concrete issue tables, the explicitly assigned seed excerpts/provenance and local obstruction proof. Excluded: author conversations and private work, complete prior review reports, other construction tracks, coordinator deliberations, unassigned seeds and old runs. No delegation occurred. Only the assigned review directory was written.

## Correctness verdict and scope

**The submission does not pass S1. Its new restricted pair-and-triangle construction is mathematically supported, with an explicit correction to two missing plus signs in display (26).** The general partition formula (24) and the expanded formula (28) supply the correct mathematics independently of that defective display. The frozen submission has not been edited.

For every $\lambda,M>0$ with
\[
\lambda M^3\leq\frac1{64\pi},
\]
the construction gives one stationary, isotropic, simple, almost surely locally finite process on all of $\mathbb R^3$, with intensity exactly $\lambda$. Its full ordered factorial measures through order four are globally absolutely continuous and have finite-almost-everywhere densities. It has finite third local count moments on every bounded Borel set and infinite fourth local count moments on every nonempty open ball. On the complete pair and triangle domains below $M$,
\[
\rho^{(2)}=\frac{2\lambda^2M}{D},
\qquad
\rho^{(3)}=\frac{4\lambda^3M^2}{A}.
\]
There is no lower distance, area or shape cutoff in these two conclusions.

Its fourth same-parent density is $b_4/V$, where
\[
b_4=\frac{\lambda^4M^3}{48\pi}>0.
\]
Its **full** fourth density includes a strictly positive contribution from lower-block partitions. The submitted proof correctly excludes a full constant-over-volume identity for this process on $E_4(M)$. The same argument applies on any positive diameter domain for this process because it uses only a small ordinary planar square and local boundedness of the lower-block terms.

There are therefore two independent losses of S1 scope: the parameter restriction, and the failure of the full fourth identity even inside that restriction. No general impossibility result for S1 follows. The fourth submission exhausts this approach's allowance: record **unsuccessful for exact S1, with valid partial results**, without a fifth substantive repair or a counter reset.

## Reconstruction and detailed audit

### 1. Target, quantifiers and dependency structure

S1 requires every independently prescribed $\lambda_0,M>0$, one global process, all three full identities simultaneously, and global absence of singular factorial mass, including outside the prescribed diameter domains. It allows infinite fourth local moments. The present theorem retains these structural and measure conditions, but proves only the two lower identities under the displayed dimensionless bound. The author acknowledges both limitations.

The bound cannot be removed merely by spatial dilation: under $x\mapsto sx$, intensity becomes $\lambda/s^3$ and the diameter parameter becomes $sM$, leaving $\lambda M^3$ invariant. No separate all-intensity argument is supplied or inferred.

The substantive inherited construction is v03's spherical process. I checked its whole-space law, coarea derivations, constants, measure coverage and bounds from the supplied proof, rather than accepting its prior issue statuses. The new finite families are defined and proved directly in v04. The earlier v01 and v02 obstructions are not hypotheses needed to construct v04; their stated scope and relevant calculations were nevertheless checked against the supplied proofs. Seed excerpts supply provenance and comparison scope, not accepted construction theorems.

### 2. Actual spherical process and intensity

Put $\eta=\lambda/2$, $L=M/2$. The proposed positive radius weights are
\[
q_L(R)=
\begin{cases}
(16\pi L^3R)^{-1},&R\leq L,\\
L^3/(16\pi R^7),&R>L,
\end{cases}
\qquad
m(R)=
\begin{cases}
16\pi\eta L^{3/2}R^{3/2},&R\leq L,\\
16\pi\eta R^3,&R>L.
\end{cases}
\]
Although $\int q_L\,dR=\infty$, this is not a purely formal infinite-rate spatial construction. Retain only nonempty families, with parent intensity
\[
dz\,q_L(R)(1-e^{-m(R)})\,dR
\]
and positive-conditioned Poisson counts. The spatial rate is finite because it is at most $\int q_Lm\,dR=\eta$. Each family has finite size almost surely. The truncation preserves the factorial weight $q_Lm^n\,dR$ exactly.

For every bounded Borel $B$, translation gives
\[
\int_{\mathbb R^3}\sigma_{z,R}(B)\,dz=|B|.
\]
The integrals of $q_Lm$ over $(0,L]$ and $(L,\infty)$ are $2\eta/3$ and $\eta/3$. Thus all parent locations, including arbitrarily distant centres, contribute total expected observed count $\eta|B|$. Finite expectations and countable exhaustion establish almost-sure local finiteness. Conditional independent sphere-uniform positions are atomless; countability excludes collisions within and between these spherical families. Translation and rotation covariance give stationarity and isotropy.

There is no hidden finite fourth family-size or local-moment assumption in this argument.

### 3. Sphere coarea identities and singular-mass coverage

The probability surface measure is correctly normalised by
\[
\sigma_{z,R}(dx)=\frac{\delta(|x-z|^2-R^2)}{2\pi R}\,dx.
\]
Indeed the unnormalised delta integral is surface area divided by $2R$, namely $2\pi R$. This notation can be interpreted throughout against nonnegative test functions through coarea.

For two points, subtracting squared-radius constraints gives the linear centre Jacobian $2D$. The remaining two-dimensional radial delta integral equals $\pi$ above the threshold. Hence
\[
s_2(D)=\frac1{8\pi D}\int_{D/2}^{\infty}\frac{q_L(R)m(R)^2}{R^2}\,dR.
\]
The weight is $16\pi\eta^2$ below $L$, and $16\pi\eta^2L^3R^{-3}$ above it. Integration yields exactly v04 (5), including agreement of the two branches at $2L$.

For a noncollinear triple, the two centre constraints have Jacobian $8A$. On their normal line, the remaining equation is $t^2+r^2=R^2$. Summing both roots contributes $1/\sqrt{R^2-r^2}$, with no missing factor two. Thus
\[
s_3=\frac1{64\pi^3A}\int_r^\infty
\frac{q_L(R)m(R)^3}{R^3\sqrt{R^2-r^2}}\,dR
=\frac{4\eta^3}{\pi A}G_L(r).
\]

For a noncoplanar quadruple, the three linear centre constraints have Jacobian $48V$. Integration over positive radius contributes $1/(2R_*)$. The four surface normalisations then give
\[
s_4=\frac{q_L(R_*)m(R_*)^4}{1536\pi^4R_*^5V}.
\]
On both radius branches,
\[
q_L(R)m(R)^4=4096\pi^3\eta^4L^3R^5,
\]
so $s_4=8\eta^4L^3/(3\pi V)=\lambda^4M^3/(48\pi V)$. All factors and the volume convention $V=|\det E|/6$ agree.

The formulas cover the complementary nondegenerate configuration sets as measure identities. They are not merely pointwise evaluations overlooking a singular component. Conditional on fixed centre and radius, coincidences have probability zero; after fixing two distinct sphere points, their line meets the sphere in at most two points; after fixing three noncollinear sphere points, their plane cuts a surface-null circle. Consequently the conditional ordered measures put zero mass on the relevant degeneracy sets. Integrating these zero measures over the nonnegative radius/count weights leaves zero mass there. The continuously distributed radius is essential to the fourth coarea calculation and is present in the concrete law.

For the bound used later, $t=\sqrt{R^2-r^2}$ transforms the first integral in $G_L$ into an integral of $(r^2+t^2)^{-1/4}$, bounded by $2\sqrt L$. For $r<L$ the second integral is $\arcsin(r/L)/r\leq\pi/(2L)$; for $r\geq L$ it is $\pi/(2r)$. Thus
\[
s_2\leq 3\eta^2L/D,\qquad
s_3\leq (2+8/\pi)\eta^3L^2/A
\leq \frac3{16}\frac{\lambda^3M^2}{A}.
\]
The last inequality uses $\eta^3L^2=\lambda^3M^2/32$ and $2+8/\pi<6$. These bounds are valid globally off the respective degeneracies.

### 4. New kernels: positivity before process definition

On $0<D<M$, direct substitution of the spherical pair branch gives
\[
w_2=\lambda^2\left(\frac{13M}{8D}-\frac34\right).
\]
In particular $w_2\geq(7/8)\lambda^2M/D>0$. It vanishes outside its designated pair domain.

For a triangle of diameter below $M$, each edge satisfies $A/D_{ij}\leq M/2$, and $A\leq M^2/2$. With $a_2=2\lambda^2M$ and $a_3=4\lambda^3M^2$, these inequalities give
\[
\lambda a_2 A\sum D_{ij}^{-1}\leq 3\lambda^3M^2.
\]
Combining this with the spherical bound proves
\[
\frac{13}{16}\frac{\lambda^3M^2}{A}+2\lambda^3
\leq F_3\leq\frac{5\lambda^3M^2}{A}
\]
on its support. The signs of both subtracted terms in $F_3$ are justified. No signed cluster law is being used.

For fixed distinct $x,y$ with distance $D<M$, use a cylinder of length $2M$ and radius $M$ containing the allowed third positions. Since $A=Ds/2$ and $dz=s\,ds\,d\theta\,dt$,
\[
\int_{\operatorname{diam}<M}\frac{dz}{A}\leq\frac{8\pi M^2}{D},
\qquad
J_2(x,y)\leq\frac{40\pi\lambda^3M^4}{D}.
\]
This both proves marginal integrability and identifies the actual pair contribution of the triple family. Under $\lambda M^3\leq1/(64\pi)$, the upper bound on $J_2$ is $(5/8)\lambda^2M/D$. Therefore
\[
\frac14\frac{\lambda^2M}{D}
\leq F_2=w_2-J_2\leq\frac{13}{8}\frac{\lambda^2M}{D}.
\]
The bound includes the equality case of the permitted parameter range. Outside $D<M$, both $w_2$ and $J_2$ vanish. All kernels are measurable, symmetric and translation/rotation invariant; assigning arbitrary finite values on null degeneracies does not alter their measures.

The radial integral
\[
R_2=\int w_2(0,u)\,du
=4\pi\lambda^2\left(\frac{13M}{8}\frac{M^2}{2}
-\frac34\frac{M^3}{3}\right)
=\frac{9\pi}{4}\lambda^2M^3
\]
is correct. Tonelli gives $Z_2+Z_3=R_2$, with $0<Z_2,Z_3<\infty$. The singleton rate
\[
\zeta=\lambda/2-R_2+Z_3/2
\]
satisfies $\zeta\geq119\lambda/256>0$. Thus positivity and intensity feasibility are established jointly, before any parent stream is defined.

### 5. Actual anchored-family laws and ordered coefficients

The triple stream has rate $Z_3/6$ and probability density $F_3(0,u,v)/Z_3$ for its two offsets, emitting the observed root and both offsets. The pair stream has rate $Z_2/2$ and density $F_2(0,u)/Z_2$, emitting its root and one offset. Singletons have rate $\zeta$. All distributions normalise, all rates are finite, and all counts are specified.

For the triple stream, each of the six ordered selections of all three vertices gives, after parent integration, density $F_3/Z_3$. Symmetry and translation invariance identify the reanchored kernels, and the changes between root/offset coordinates have absolute Jacobian one. Multiplication by $Z_3/6$ yields third same-parent density $F_3$. Its pair density is exactly $J_2$: a fixed ordered pair in a three-point family has exactly one remaining vertex, so marginalising its third factorial measure introduces factor one. Its intensity is $3Z_3/6=Z_3/2$.

Likewise, the two ordered selections of a two-point family yield same-parent pair density $F_2$, and intensity $Z_2$. These families produce no same-parent fourth tuples. The spherical parent is unobserved by definition, so only its sibling selections occur. This fully specifies the relevant within-family genealogies.

The intensity of the superposition is
\[
\eta+Z_3/2+Z_2+\zeta=\lambda.
\]
The expectation calculation again integrates all parent locations. It proves local finiteness even though the spherical radii are unbounded. The anchored offsets have joint Lebesgue densities, so within-family collisions vanish. For different streams or families, conditioning on offsets and using the diffuse Poisson parent factorial measure excludes equal observed locations; countability makes this simultaneous. This also handles observed roots, which cannot be justified solely by atomlessness of spherical child positions.

### 6. All parent partitions and the defective display

The correct same-parent densities are
\[
c_1=\lambda,\qquad c_2=s_2+F_2+J_2=s_2+w_2,\qquad
c_3=s_3+F_3,\qquad c_4=s_4.
\]
An ordered observed tuple has a unique partition by parent. Ordering blocks by their least labels and using the factorial measure of distinct Poisson parents gives
\[
\rho^{(n)}=\sum_{\pi\in\mathcal P_n}\prod_{B\in\pi}c_{|B|}(x_B).
\tag{R1}
\]
There is no extra factorial for ordering the blocks. All terms are nonnegative. One may restrict parent positions, radii and family counts first and then exhaust them monotonically; Tonelli and monotone convergence establish the whole-space identity even when the fourth local measure is infinite.

**Literal defect in v04 (26).** The source omits the plus signs before the pairing sum and before the $\lambda^2$ pair sum. As printed, juxtaposition would multiply three sums and is incorrect. The complete corrected formula is
\[
\boxed{
\rho^{(4)}(x_1,x_2,x_3,x_4)
=c_{4,1234}
+\lambda\sum_{\substack{I\subset\{1,2,3,4\}\\|I|=3}}c_{3,I}
+\sum_{\{ij\mid kl\}}c_{2,ij}c_{2,kl}
+\lambda^2\sum_{1\leq i<j\leq4}c_{2,ij}
+\lambda^4 .
}
\tag{R2}
\]
The pairing sum has exactly the three terms $12\mid34$, $13\mid24$, $14\mid23$. The five groups contain $1+4+3+6+1=15$ partitions.

This correction is determined by v04 (24), which is correct as written, by the independently rederived parent allocation argument, and by the correctly additive v03 (15). The expanded v04 (28) also agrees with (R2), not with the literal (26). Consequently this is a repairable display error, not an unresolved probability-law or coefficient gap. Every use of “(26)” in the supported theorem and in the audit below means (R2). This report supplies the editorial correction without modifying v04 or requiring another substantive submission.

### 7. Exact lower full identities and fourth expansion

On their prescribed domains the actual same-parent terms reduce to
\[
c_2=a_2/D-\lambda^2,\qquad
c_3=a_3/A-\lambda a_2\sum_{\rm edges}D_{ij}^{-1}+2\lambda^3.
\]
Substitution in $\rho^{(2)}=c_2+\lambda^2$ and
$\rho^{(3)}=c_3+\lambda\sum c_2+\lambda^3$ proves both claimed full identities. The correction for the triple marginal has already been incorporated; it is not lost when full partitions are restored.

On $E_4(M)$, all faces and pairs satisfy their corresponding lower-domain conditions. Expanding (R2) gives exactly
\[
\rho^{(4)}
=\frac{b_4}{V}
+\lambda a_3\sum_{|I|=3}\frac1{A_I}
+a_2^2\sum_{\{ij\mid kl\}}\frac1{D_{ij}D_{kl}}
-2\lambda^2a_2\sum_{i<j}\frac1{D_{ij}}
+6\lambda^4.
\tag{R3}
\]
Every edge occurs in two faces and in one of the three pairing products. Its linear coefficient is therefore $-2-1+1=-2$ in units of $\lambda^2a_2$. The constant coefficient is $8+3-6+1=6$. The negative term in (R3) causes no positivity problem because (R2) is the underlying sum of nonnegative terms.

Choose a sufficiently small planar square whose diameter is below $M$. In a neighbourhood of it, all pair distances and all face areas have uniform positive lower bounds. The global estimates for $c_2,c_3$ make the lower-block remainder
\[
B=\rho^{(4)}-b_4/V
\]
uniformly bounded on noncoplanar configurations in that neighbourhood, while (R2) gives $B\geq\lambda^4>0$. Therefore $V\rho^{(4)}\to b_4$ along every noncoplanar approach.

If an a.e. identity $\rho^{(4)}=a_4/V$ held on $E_4(M)$, each sufficiently small neighbourhood contains a positive-measure open set of eligible noncoplanar configurations. A sequence can be chosen outside its exceptional null set and tending to the square, forcing $a_4=b_4$. The strict lower bound then contradicts that identity. This is a proof of failure of the particular constructed law, not an inference from merely displaying one same-parent term.

The stated extension of this failure mechanism is also appropriately conditional: adding independent families of size at most three leaves the fourth same-parent term fixed. If their lower terms are locally bounded near an ordinary planar configuration, they cannot remove the positive full remainder. This does not classify other fourth-family laws, dependent parent processes or arbitrary stationary processes.

### 8. Global measures and local moments

The added anchored families are joint Lebesgue-density constructions, and their coordinate marginals after parent integration are Lebesgue densities. The spherical same-parent measures were checked above on the whole space. Products over disjoint coordinate blocks in (R1) are product density integrals. Thus no singular mass remains on coincident, collinear, coplanar, fixed-radius or outside-domain sets.

At every distinct pair, $c_2$ is finite. At every noncollinear triple, $c_3$ is finite. At every noncoplanar quadruple, $c_4$ and all its lower-block factors are finite. The exceptional sets are Lebesgue null. This proves global finite-a.e. full densities through order four, without pretending that their integrals over bounded configuration sets are all finite.

For any bounded $B$ of diameter $H$, the verified inequalities
\[
\int_{B^2}D^{-1}\leq2\pi H^2|B|,
\qquad
\int_{B^3}A^{-1}\leq16\pi^2H^4|B|
\]
combine with $c_2\leq C_2/D$ and $c_3\leq C_3/A$ to give finite first, second and third factorial moments. The third partition terms integrate to finite quantities too: a pair block supplies its finite pair integral and an extra factor $|B|$. Then $N^3=(N)_3+3(N)_2+N$ proves finite third raw moments. For zero-volume sets the first moment is zero, so the same conclusion holds without a geometric ambiguity.

In every nonempty open ball, a positive-measure set of noncollinear base triples permits fourth-point cylinders crossing its base plane. With signed height $t$, $V=A|t|/3$. Tonelli and $\int_{0<|t|<\varepsilon}dt/|t|=\infty$ prove $\int_{B^4}V^{-1}=\infty$. Since the full density contains $b_4/V$, both fourth factorial and fourth raw moments are infinite. Almost-sure local finiteness was established independently by the first moment and is not contradicted.

### 9. Arbitrary-radius clarification and earlier mathematical scope

The v04 clarification correctly repairs the potential overreading of v03's introductory coarea sentence. At each fixed radius, centre integration already gives diffuse pair and triple measures, except on threshold sets that themselves have zero conditional measure. Mixing such measures with arbitrary nonnegative radius weights preserves absolute continuity at these orders; the resulting density may have extended values.

The fourth evaluation formula instead requires the fourth-factorial-weighted radius measure to be absolutely continuous. An atom at $R_0$ with positive fourth weight yields nonzero same-parent mass supported on the null set of noncoplanar quadruples with circumsphere radius $R_0$. Atoms with no fourth factorial weight contribute no such mass. The concrete $q_Lm^4\,dR$ is continuous and unaffected.

I also checked the v03 pair/triangle obstruction independently: conditional iid common-sphere offspring imply $c_3=F(r)/A$, while the assumed full pair law and the partition identity force
\[
F(r)=a_3-\lambda a_2 A(1/a+1/b+1/c)+2\lambda^3A.
\]
Smooth triangle coordinates and Fubini select an $r\in(0,M/2)$ for which the right side is constant for almost every shape. Its continuity then makes it constant for every nondegenerate shape at that radius. On right triangles, $p=\sin\theta+\cos\theta$ varies over an interval and gives the polynomial
\[
a_3-\lambda a_2rp
+\frac{-\lambda a_2r+4\lambda^3r^2}{2}(p^2-1).
\]
Its nonzero linear coefficient excludes constancy. The dependent anchored triple family in v04 is outside those hypotheses, so its new triangle success does not contradict this theorem.

For v01, the relevant dichotomy remains valid in its stated fixed-displacement iid branching class. Finite intensity forces mean reproduction below one; finite fourth offspring moment then yields finite fourth family and local moments. If the fourth offspring moment is infinite, the direct-sibling density factors through one fixed $H_4$; $\int_{B^4}H_4=\int q_B^4\in(0,|B|]$ makes it positive on positive measure, giving an infinite density there. Count–geometry coupling in the later models removes the factorisation hypothesis.

For v02, the Gaussian normalisation and observed-root contributions agree with the supplied formulas. Completing the square yields its exponents $3(n-4)/2$ and $(3n-14)/2$; $\det S_4=9V^2$ gives coefficient $c/(24\pi^3L^6)$ with the stated damping. Two positive scatter eigenvalues bound every other fourth term near ordinary coplanarity, leaving a configuration-dependent coefficient. The radial-productivity pair obstruction follows from the displayed angular comparison with $\min(1,u^{-1})$ and dominated convergence when $J_2<\infty$, and divergence when $J_2=\infty$. These are scoped results, not general restrictions on S1.

The v02 triangle-failure issue can also be reconstructed without an earlier verdict: near a fixed distinct collinear triple, $S_3$ has one uniformly positive eigenvalue. In coordinates $(t,w)\in\mathbb R\times\mathbb R^2$,
\[
\int_{\mathbb R^2}(1+t^2+|w|^2)^{-3/2}\,dw
=\frac{2\pi}{\sqrt{1+t^2}}.
\]
The remaining Gaussian integral in $t$ is uniformly finite. The root and pair terms are bounded by their integrable weights, so the full third density stays bounded where $a_3/A$ diverges. This historical failure is overcome by v04's different dependent triple family, within its parameter range.

## Finding register

| ID | Location | Precise mathematical issue or checked obligation | Consequence | Repair/status |
|---|---|---|---|---|
| P3-V04-01 | Theorem, (1)–(3), Sections 5–6 | S1 requires arbitrary independent $\lambda_0,M$ and all three full identities. The proved theorem restricts $\lambda M^3$ and fails order four. | No exact S1 pass; fourth unsuccessful exact-target submission. | Open general target; retain the supported partial theorem. |
| P3-V04-02 | Display (26) and references to it | Two plus signs are absent, making the literal expression a product of sums rather than the partition sum. | The display is false as printed; its literal use is invalid. | Complete corrected formula (R2) supplied. The proof is recoverable from correct (24), v03 (15) and (28); editorial correction only, no fifth attempt. |
| P3-V04-03 | Section 1, v03 Sections 1–2 | Infinite latent radius mass and unbounded spatial influence need an actual law and all-parent first moment. | Formal finite-neighbourhood reasoning would be insufficient. | Closed: finite-rate nonempty families, preserved factorial weights, intensity $\eta$, local finiteness and simplicity verified. |
| P3-V04-04 | (5)–(9), inherited coarea | Surface normalisation, linear Jacobians, two triple roots and radius derivative determine exact constants. | Errors would invalidate the new positivity budget and fourth coefficient. | Closed: $2\pi R$, $2D$, $8A$, $48V$, $2R_*$ and $b_4$ checked independently. |
| P3-V04-05 | (11)–(18) | A triple kernel and its pair marginal cannot be added without subtracting that marginal from the separate pair-family law. The subtraction must be nonnegative. | Otherwise the pair law or process positivity would fail. | Closed: $F_3>0$, finite $J_2$, and $F_2\geq\lambda^2M/(4D)$ under the stated range. |
| P3-V04-06 | (19)–(22), family definition | Parent rates, offset normalisation and singleton residual must be simultaneously feasible. | A density calculation alone would not produce the prescribed process. | Closed: $Z_2+Z_3=9\pi\lambda^2M^3/4$, $\zeta\geq119\lambda/256$, and total intensity $\lambda$. |
| P3-V04-07 | Sections 3–5 | Ordered root/sibling selections, reanchoring Jacobians and all fifteen parent partitions are required. | Missing factors would change full rather than same-parent laws. | Closed: six triple selections, two pair selections, marginal factor one and full partition sum verified; use corrected (R2). |
| P3-V04-08 | (25), (27) | Both target lower densities must be full measures on all eligible shapes, including arbitrarily small and flat triangles. | A cumulant-only or truncated-domain result would be weaker. | Closed within the displayed parameter range: cancellation is exact and no lower cutoff is used. |
| P3-V04-09 | (28)–(29) | The full fourth remainder must be controlled before identifying a singular coefficient. | A same-parent formula alone cannot prove fourth success or failure. | Closed: expansion (R3), local boundedness and $B\geq\lambda^4$ prove failure of this process. |
| P3-V04-10 | Section 7 | Pointwise densities on nondegenerate configurations do not by themselves exclude other singular mass or outside-domain defects. | S1 imposes a global measure requirement. | Closed: conditional degeneracy-zero arguments, coarea and anchored marginal densities cover all measure components globally. |
| P3-V04-11 | (30)–(32) | Finite third and infinite fourth local moments must be distinguished from a.s. local finiteness and finite-a.e. densities. | An invalid moment inference would narrow or misclassify S1. | Closed by spatial integrals and independent first-moment control. |
| P3-V04-12 | Section 8, v03 arbitrary mixing sentence | Atomic fourth-factorial-weighted radius laws can produce singular fourth mass, although fixed-radius pair/triple measures are diffuse. | An unrestricted order-four extension would be false. | Closed by the weighted-radius clarification; concrete law has the required density. |
| P3-V04-13 | Sections 9–11, prior scopes | Fixed-kernel, Gaussian and iid-sphere obstructions rely on specific representation hypotheses. | None authorises a general S1 restriction or theorem-false verdict. | Scope retained; the new dependent families leave the earlier classes explicitly. |
| P3-V04-14 | Section 9, source assertions | Historical seed leads and earlier approval labels cannot certify a new theorem. | A source dependency could remain unverified if imported implicitly. | No essential source gap: current finite-family law is proved directly; source excerpts used only at their stated scope. |

## Disposition of every supplied prior issue

Prior issue statuses were treated as obligations to check, not as mathematical authority.

### From v01

| Prior ID | Current disposition |
|---|---|
| P3-R01 | Still unresolved for exact S1. The new pair-and-triangle theorem is partial; order four fails and the parameter range is restricted. |
| P3-R02 | Scope preserved. The fixed count-independent displacement theorem does not apply to the radius-coupled sphere law or dependent anchored triple law. Its finite/infinite moment alternatives were reconstructed above. |
| P3-R03 | Relevant partition principle re-established for the actual v04 family types, including observed roots where present. The historical tree expansion has a unit root/edge Jacobian and all ordered selections; it is not used to omit any new term. |
| P3-R04 | Moment/density distinction preserved and verified anew. Infinite fourth local mass of a finite-a.e. density is permitted; the old infinite fixed-kernel sibling density on positive measure is a different obstruction. |
| P3-R05 | No spacetime projection is used in v04. The supplied v02 clarification correctly handles projected root pairs by the Poisson second factorial measure of the spatial-coincidence null set and countable exhaustion. No current projection gap remains. |
| P3-R06 | The supplied cluster-law excerpt explicitly gives families of at most four points. It supports that limited attribution; complete seed construction theorems are neither supplied in full nor assumed valid here. |

### From v02

| Prior ID | Current disposition |
|---|---|
| P3-V02-01 | Exact-target obligation remains open. The historical Gaussian law's failures are not converted into general nonexistence by subsequent attempts. |
| P3-V02-02 | The radial-productivity obstruction retains its Gaussian geometry, weight, Poisson-parent and sterile-generation hypotheses. v04 lies outside it. |
| P3-V02-03 | Whole-space law and intensity rechecked for v04; no bounded influence assumption is used for its spherical component. |
| P3-V02-04 | Both family types with observed roots and the latent-parent spherical type are fully enumerated. All fifteen fourth partitions are in (R2); the display correction is explicit. |
| P3-V02-05 | The historical Gaussian determinant and coefficient check out. The current spherical coefficient is separately derived and not inherited from the Gaussian calculation. |
| P3-V02-06 | Global finite-a.e. density, zero singular mass and the local moment class are verified for the new law, not transferred merely from v02. |
| P3-V02-07 | The full current remainder is locally bounded near ordinary coplanarity. Here the leading coefficient is constant but the positive remainder prevents equality; the historical damped coefficient was configuration dependent. |
| P3-V02-08 | The earlier arbitrary measurable radial-productivity dichotomy is correctly scoped and supported by its angular bound and dominated-convergence calculation. No unjustified limit from that theorem enters v04. |
| P3-V02-09 | Assigned source excerpts establish attribution/scope only. No old approval label or full-seed theorem is a current premise. |
| P3-V02-10 | The old Gaussian triangle failure is consistent with the boundedness reconstruction above. v04 obtains exact triangle attainment with a different dependent family and proves that attainment directly. |

### From v03

| Prior ID | Current disposition |
|---|---|
| P3-V03-01 | Partly advanced, still open for S1: the full triangle law is now attained in the specified range; the full fourth law is not. |
| P3-V03-02 | Closed after independent reconstruction of nonempty-parent thinning, count conditioning, intensity and whole-space existence. |
| P3-V03-03 | Closed: all sphere normalisations and Jacobians checked, plus the new anchored-family coefficients. |
| P3-V03-04 | Closed: global measure coverage and finite-a.e. regularity checked for the inherited and added components. |
| P3-V03-05 | Closed mathematically by (R1)–(R2), with the new display defect recorded separately. All within-family selections are specified. |
| P3-V03-06 | Exact full pair attainment survives in v04's allowed range with its new coefficient; positivity and total-intensity bookkeeping are proved together. This does not inherit v03's all-parameter scope for the new simultaneous theorem. |
| P3-V03-07 | Fourth-law failure remains. The new full expansion and the bounded-positive-remainder argument were checked independently. |
| P3-V03-08 | The old concrete triangle failure is overcome by $F_3$ in the permitted range. Finite third local moments are proved from the actual new spatial density bounds. |
| P3-V03-09 | Infinite fourth local mass remains compatible with a.s. local finiteness and finite-a.e. full densities; all three properties were rechecked. |
| P3-V03-10 | The prior arbitrary-count iid-sphere obstruction remains valid. Fubini, continuity in shape and the right-triangle polynomial justify its a.e. contradiction; v04 changes its iid common-sphere hypothesis. |
| P3-V03-11 | No extension to all branching or all stationary processes is made or supported. No target change follows. |
| P3-V03-12 | Clarification supplied and accepted: unrestricted mixing statements concern pairs/triples; the fourth formula needs an absolutely continuous fourth-factorial-weighted radius measure. Atoms with zero fourth weight are harmless. |
| P3-V03-13 | Consequential dependencies checked from their proofs, and source leads separated from premises. No essential mathematical source request remains outstanding. |

## Amendment implications

No amendment is proposed or adopted by this review. S1 remains the hashed active target. The v04 parameter bound is sufficient for this positive kernel construction; it is not proved necessary for S1. The fourth obstruction is for the constructed Poisson-family law and the stated fixed-fourth-kernel addition mechanism, not a general no-go theorem.

The local reciprocal-volume integral does exclude the separate finite-fourth-local-moment comparison class whenever the full small nondegenerate domain is retained. It does not justify imposing such a moment hypothesis, deleting flat tetrahedra, or relaxing full densities in the broad S1 question.

The S0 record is preserved. Its global pair impossibility is independently consistent with the supplied `nonexistence_2` proof: large-ball first moments scale as $R^3$, the reciprocal pair factorial moment as $R^5$, and variance nonnegativity fails after division by $R^6$. The complete separate global order-three/order-four obstruction evidence named in the adoption record was not included for re-review here and is not re-certified. The adopted S1 authority is received through its frozen record; no new authority is inferred from this construction.

The coordinator explicitly requested the corrected additive display in this report while preserving v04 unchanged. This editorial correction neither adds a fifth substantive submission nor changes any target or counter.

## Source and coding evidence

The precise input inventory and SHA-256 verification are saved beside this report. Principal mathematical inputs checked were:

| Input | Verification and use |
|---|---|
| Current v04 proof, SHA `0cffc5a62fec3725f6cad6a839bb9cb2125b4ef8d9d6bfe89ca471635a4062db` | Entire current mathematical argument and conclusions audited. Two missing plus signs identified. |
| Prior v03 proof, SHA `c6608c347db222f9cf91f55c8763ff2215462c21c110826a327a3cca6e097c0c` | Spherical law, coarea, global measures, moments and its iid-sphere incompatibility theorem rechecked. |
| Prior v02 proof, SHA `8b111ffca00675eb5b0cd0e14dc5b8f041698d207630b687c8fbd9049ea181b8` | Gaussian and radial-productivity calculations, model scope, projection clarification and relevant historical claims checked; not used as a new construction premise. |
| Prior v01 proof, SHA `77ab351888c26bb524f694c8eb2f191e0775dfcdc152d8d077adca99a7363736` | Fixed-kernel dichotomy, translation/moment and partition principles checked; its scope is retained. |
| Assigned local obstruction proof, SHA `4b15463c7115c2f0e56424e7ab2b293c0c33a10bb3a68d1d67a7c13074a2c14f` | Pair/area integrability, near-coplanarity divergence and broad moment-class distinction checked. No other obstruction track was opened. |
| Six assigned seed/provenance excerpts | Restricted geometric/intensity scope, at-most-four-point parent law and labelled plane-field diagnostic inspected. No complete seed theorem or external priority claim accepted. |
| Three previous issue tables | All individual obligations disposed of above. Their former verdict labels were not premises. |
| Frozen common context and primary-source index | Read for conventions and available sources. No book exercise wording, historical novelty or current-open-status claim is made. |

The coordinator transcription note named by the author was not in this review packet and was not opened. No mathematical conclusion depends on its content: the supplied v03 polynomial is correct directly. The current (26) defect is a separate observed issue.

No primary PDF, external web source, symbolic-algebra package, simulation, numerical fit, earthquake data or proof assistant was needed to settle a consequential inference. The proof uses explicitly reconstructed Poisson factorial identities, elementary coarea/change of variables, Gaussian and cylindrical integration, Tonelli/monotone convergence and the stated dominated-convergence bound. This is an informal mathematical audit, not formal machine certification or a literature search. Scripts were used for allowlisted own-runtime metadata, input integrity and artifact/accounting records only. No source or coding request remains outstanding.

## Presentation judgement

The submission clearly separates its partial theorem from S1, defines every observed family vertex, and exposes the positivity and intensity budgets before claiming existence. Its fourth-order failure and moment distinctions are readable and appropriately qualified.

Display (26) needs the two explicit plus signs in (R2). Because later prose repeatedly cites it, the correction should accompany any reused excerpt even though no new author submission is required. The exact expanded formula (28) is correct.

For a future consolidated exposition, “the v03 construction” would be preferable to “the accepted v03 law” when introducing a dependency: acceptance is administrative evidence, while the supplied formulas and proof are the mathematical evidence. Repeated accounting and attempt-history paragraphs can remain in the research record but need not appear in a mathematical theorem statement. These are exposition suggestions, not additional mathematical requirements.

## Review summary and remaining obligations

The decisive new step is valid: a positive symmetric dependent triple kernel corrects the full triangle law, its pair marginal is subtracted from a separately positive pair kernel, and a positive singleton rate restores exactly the prescribed intensity. The smallness condition makes those requirements jointly feasible. Every same-parent and different-parent contribution has been accounted for.

The spherical component supplies a genuine reciprocal-volume same-parent measure with finite-a.e. density and infinite fourth local mass. Restoring all parent partitions leaves a bounded positive remainder near ordinary coplanarity. This proves the constructed law's fourth failure despite its exact lower-order progress.

The supported final record is therefore:

- **Correctness:** valid restricted partial construction, after the explicit editorial restoration of the two plus signs; no substantive gap found in that partial theorem.
- **Exact-target outcome:** S1 not achieved, and not proved false generally by this track.
- **Allowance:** four substantive submissions used; approach unsuccessful for exact S1, with its partial results preserved.
- **Unresolved mathematics:** a global law satisfying all three full identities for every independent $(\lambda_0,M)$, or a valid general obstruction under S1's actual broad hypotheses.
- **Coverage limits:** no cross-track synthesis, complete-seed certification, literature-priority investigation, re-audit of omitted global obstruction evidence, formal verification or empirical testing.

## Usage and artifact accounting

Own runtime identity/model evidence is in `runtime_preflight.json`; capability/scope in `accounting_capability.json`. Only own `session_meta`, allowlisted `turn_context` fields and `token_count.info` were inspected. No raw conversation or private reasoning was used as evidence.

The exposed cumulative counters and their latest checkpoint are recorded in `accounting_record.json` and `usage_evidence.json`. A cumulative snapshot is not added to earlier snapshots. Reasoning output is not added again to the output field. No children were spawned; parent aggregation semantics are NR. Final completed-turn usage, final elapsed duration at the instant of turn completion, pricing/tier information and actual monetary charges are NR at review freeze. No token or cost estimates substitute for missing measurements. `freeze.json` records the report hash, byte and word counts, and UTC freeze time.
