# Review — proof_1 / submission v02 / S1

- Type: fresh independent extensive review of the second frozen submission and its consequential dependencies.
- Reviewer: `/root/review_proof_1_v02`; session `session-15`; turn `turn-27`.
- Requested and verified runtime: `gpt-6-astra`, `xhigh`. The reviewer's own `turn_context` at session line 8, timestamp `2026-10-20T17:53:38.584Z`, supplies both fields. Session start: `2026-10-20T17:53:36.262Z`. Review freeze time and the last available numerical usage checkpoint are recorded in `freeze.json`.
- Setup root: `$SETUP`.
- Run root: `runs/20261020T164437Z_astra6`.
- Active target: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Reviewed submission: `reviews/proof_1_v02/proof_snapshot.md`, SHA-256 `67605a81bb7fa19e16d3aad6ca6ae6c86af8b1112d8f27a165d9a1558200c21d`.
- Review packet: `packets/review_proof_1_v02.json`, SHA-256 `92dff51e8d63606da59e410ab38e461d9012bc2309768c6077ae17a91d87c919`.
- Prior mathematical dependency: `prior_dependency_v01.md`, SHA-256 `acf0c4de3dcd7ee1caeeff0da17e9d8d7d8144b5ecb984d0742bb1662fc52473`.
- Previous concrete issue list: `previous_issue_list_v01.md`, SHA-256 `9054eba7f105fd3314f82ddbb890d8422a60de6335c152102ec6a2210e708a9d`.
- Attempt under review: **2 of 4**. No counter reset.

All enumerated packet-file hashes matched before mathematics. The assigned frozen reviewer instructions, accounting instructions, common context, workflow, review and amendment templates, proof-reviser skill and both required skill references were read. Setup-relative references were resolved as directed to their frozen equivalents. The adopted S0-to-S1 amendment was read to identify the active target; its historical obstruction proofs were not supplied for a new audit.

The mathematical context comprised the current proof, the preceding proof, its concrete issue table, and the explicitly supplied seed excerpt and provenance record. No author conversation or private work, full previous review verdict, other construction track, unassigned seed material, other chat or old run was accessed. Only selected metadata and numerical token fields from the reviewer's own session were inspected. There was no delegation.

## Correctness verdict and scope

**The supplied informal argument establishes its stated partial theorem. It does not establish S1.** No invalid mathematical step or unresolved essential dependency was found in that partial theorem after auditing the entire v02 argument.

Precisely, for positive $\lambda,M$ satisfying
\[
2\pi\lambda M^3\leq\frac12,\qquad
8\pi^3(\lambda M^3)^2+12\pi^2\lambda M^3\leq\frac12,
\]
and each $0<\eta<1$, the construction gives a whole-space stationary isotropic simple locally finite point process of intensity exactly $\lambda$, with exact full pair and triangle laws on all of $E_2(M)$ and $E_3(M)$, and
\[
(1-\eta)\frac aV\leq\rho^{(4)}\leq(1+\eta)\frac aV
\quad\hbox{on }E_4(M)
\]
for a finite positive $a$ depending on $\eta$. Its full measures at orders two through four have globally finite-almost-everywhere Lebesgue densities and no singular components. Third local count moments are finite, whereas fourth moments are infinite on every nonempty open ball.

Two independent exact-target obligations remain:

1. The full fourth density must equal one constant divided by $V$ throughout the prescribed domain. The configuration-dependent disc-intersection integral plus the lower-partition terms has only been bounded, not made equal to that function.
2. A construction must cover every independently prescribed pair $(\lambda,M)$, not only the displayed small range of $\lambda M^3$.

These limitations are explicitly acknowledged by the submission. Thus attempt 2 is **unsuccessful against exact S1, with verified new partial progress**. This is not a non-existence theorem for S1, nor evidence that the intensity restriction is necessary. The supplied theorem's validity and its failure to answer the active question are separate judgements.

The review covers all new mathematics in v02 and the earlier facts actually needed for it: the parent-level construction, full partition identity, pair and triangle integrability estimates, residual positivity, finite-cluster normalisation, moment estimates and local reciprocal-height divergence. The preceding proof's unrelated subclass obstructions and the seed's altitude-restricted fourth-order theorem are not needed for this verdict and are not independently recertified here. This is a mathematical audit, not formal machine verification.

## Reconstruction and detailed audit

### 1. The process and measure framework

Submission lines 53–88, equations (4)–(7), correctly distinguish actual parent integrations from a potentially problematic product notation for image measures.

Let $\nu$ be a measure on finite nonempty simple configurations with
\[
\int N(C)\,\nu(dC)<\infty.
\]
Then $\nu(\mathcal C)<\infty$, and $dz\,\nu(dC)$ is a $\sigma$-finite intensity measure for a Poisson random measure on parent locations and marks. Translating each finite mark constructs the process on all of $\mathbb R^3$. For a bounded Borel $B$,
\[
\int dz\int C(B-z)\,\nu(dC)
=|B|\int N(C)\,\nu(dC).
\]
Consequently the observed count in $B$ is almost surely finite. Applying this to a countable increasing family of bounded cubes gives local finiteness simultaneously on all bounded sets. This argument does not require a bound on the displacement radii.

The number of parents whose cluster meets $B$ is Poisson with finite parameter, since its intensity is at most the displayed integral. Within-mark simplicity is part of the mark law. For two different parents and fixed selected mark points, a coincidence imposes a Lebesgue-null equality on their independent translation variables. Tonelli, the distinct-parent factorial formula and a countable spatial exhaustion therefore exclude cross-parent coincidences. Translation invariance comes from $dz$. Rotation invariance will follow from the rotationally invariant mark measures below.

For every nonnegative tuple test, grouping an observed tuple by its parents is legitimate because the process is simple and every selected point has one parent. Ordering the blocks by their least labels counts each assignment once. The factorial measure of the distinct Poisson parents is the product of the underlying $\sigma$-finite parent intensity measures. This proves the partition identity directly in the form (5), even if the resulting image measures are not locally finite.

Once the block measures have finite-almost-everywhere densities, they are $\sigma$-finite and the ordinary density form (6) follows. The fourth-order terms are:

| Block sizes | Number of partitions | Contribution |
|---|---:|---|
| $1+1+1+1$ | 1 | $\lambda^4$ |
| $2+1+1$ | 6 | $\lambda^2 k_2$ for each edge |
| $2+2$ | 3 | $k_2(ij)k_2(kl)$ |
| $3+1$ | 4 | $\lambda k_3$ for each face |
| $4$ | 1 | $k_4$ |

Thus (7) contains all 15 partitions with their correct multiplicities. There is no hidden replacement of full densities by same-parent densities. The earlier notation issue P1V01-03 is repaired.

### 2. The cylindrical marks are actual finite configurations

Submission lines 92–165, equations (8)–(16), specify a measurable nonnegative mark measure, rather than only proposed factorial kernels.

The cylinder has volume $2\varepsilon\pi R^2$, so $f_{\varepsilon,n}$ integrates to one. The population
\[
N_T(\varepsilon)=4+\lceil T(\varepsilon/\ell+\ell/\varepsilon)\rceil
\]
is a measurable finite integer for every $\varepsilon>0$, with $N_T\geq6$ when $T\geq1$. Conditional iid sampling from the diffuse cylinder density yields a finite simple configuration almost surely. Pushing the product sampling law to the space of finite configurations supplies the mark kernel; multiplying it by (10) supplies $\nu$. A probability normalisation of (10) is not missing: it is explicitly a rate measure, whose finite total mass is the parent rate.

For $g=g_\ell(\varepsilon)$, all factors $N_T-j$, $0\leq j\leq3$, are at least $Tg$. Hence
\[
\frac{(N_T)_r}{(N_T)_4}\leq(Tg)^{-(4-r)}
\quad (r=1,2,3).
\]
The substitution $u=\varepsilon/\ell$ gives
\[
\int_0^\infty g^{-p}\frac{d\varepsilon}{\varepsilon}
=\int_0^\infty\frac{u^{p-1}}{(1+u^2)^p}\,du.
\]
The respective values for $p=1,2,3$ are $\pi/2$, $1/2$ and $\pi/16$. This proves the stated bounds
\[
m_3\leq\frac{\pi c}{2T},\qquad
m_2\leq\frac{c}{2T^2},\qquad
m_1\leq\frac{\pi c}{16T^3}.
\]
For completeness the $p=4$ integral is $1/12$, so the total parent rate is at most $c/(12T^4)$. It is positive and finite. At order four the factorial factors cancel exactly, leaving
\[
c\int_0^\infty\frac{d\varepsilon}{\varepsilon}=\infty.
\]
This is an infinite fourth *population moment rate*, not an infinite population for any individual cluster.

Equation (15) follows by counting the $(N_T)_r$ ordered distinct offspring selections and integrating their conditional iid densities. All integrands are nonnegative, so Tonelli establishes the full same-parent measure identity without first requiring fourth-moment finiteness. This is also why the unbounded mixture cannot create a singular component from these Lebesgue densities: every Lebesgue-null tuple set has zero integral at every type and therefore zero mixture measure.

The first-moment rate is the spatial intensity because $\int f_{\varepsilon,n}(x-z)\,dz=1$. The construction is isotropic: rotating both $n$ and $y$ preserves (8), and $\sigma$ is rotationally invariant. Sampling both $n$ and $-n$ is harmless; $\sigma$ is a probability measure and the stated constants consistently use that convention.

For local third moments, write $H_B(z,C)=C(B-z)$. Pointwise,
\[
H_B^3\leq N(C)^2H_B,\qquad
\int H_B^3\,dz\leq |B|N(C)^3.
\]
Since $N^3=(N)_3+3(N)_2+N$, the above population bounds make the integral finite. If $A_j=\int H_B^j\,dz\,\nu(dC)$, the compound Poisson identity
\[
\mathbb E X(B)^3=A_3+3A_2A_1+A_1^3
\]
then proves finiteness. This independently justifies (16) and its consequence, including for unbounded cylinder heights.

### 3. The exact fourth-density calculation and its constants

Submission lines 169–246, equations (17)–(25), are correct.

For fixed $n$, the intersection conditions for the parent translation factor into a normal interval and a tangential intersection of discs. The interval length is $(2\varepsilon-w_{\mathbf x}(n))_+$, while the tangential area is $A_R(n;\mathbf x)$. The orthogonal coordinate decomposition has unit Jacobian. Dividing by $(2\varepsilon\pi R^2)^r$ proves (18).

At order four the population factor cancels. With $s=2\varepsilon$ and $d\varepsilon/\varepsilon=ds/s$,
\[
\int_0^\infty
\frac{(2\varepsilon-w)_+}{(2\varepsilon)^4}
\frac{d\varepsilon}{\varepsilon}
=\int_w^\infty(s^{-4}-ws^{-5})\,ds
=\frac{1}{3w^3}-\frac{1}{4w^3}
=\frac1{12w^3}.
\]
There is no missing factor of two in this substitution. Thus (20) is an exact same-parent density and is independent of $T$.

For an affinely independent quadruple, $w_{\mathbf x}$ is continuous and positive on $S^2$, hence has a strictly positive minimum. This observation proves pointwise finiteness for each such configuration; it does not claim a uniform lower width over all shapes.

The polar-volume computation gives the required uniform geometric identity without that stronger assumption. For the standard simplex $S=\operatorname{conv}(0,e_1,e_2,e_3)$ and $D_0=S-S$,
\[
h_{D_0}(q)=\max(0,q_1,q_2,q_3)-\min(0,q_1,q_2,q_3).
\]
The region in $D_0^\circ$ where zero is the minimum has volume one. If $q_i=-u$ is the minimum with $0<u<1$, the other two coordinates each range over an interval of length one, $[-u,1-u]$. Integrating over $u$ gives volume one for each of the three possible $i$. The tie sets are null. Therefore $|D_0^\circ|=4$.

Writing $U=[x_2-x_1,x_3-x_1,x_4-x_1]$, we have
\[
(UD_0)^\circ=U^{-\mathsf T}D_0^\circ,\qquad
|(UD_0)^\circ|=\frac4{|\det U|}=\frac2{3V}.
\]
Since the radial function of this polar is $1/w_{\mathbf x}(n)$, spherical coordinates give
\[
\frac13\int_{S^2}w_{\mathbf x}(n)^{-3}\,dS(n)
=\frac2{3V}.
\]
Using $d\sigma=dS/(4\pi)$ proves, with exactly the submission's normalisation,
\[
\int_{S^2}w_{\mathbf x}(n)^{-3}\,\sigma(dn)
=\frac1{2\pi V}.
\]

For diameter below $M<R$, each projected centre lies within $M$ of $P_nx_1$. The disc of radius $R-M$ about that point lies in every disc defining $A_R$, while the intersection is contained in any one radius-$R$ disc. Therefore
\[
\pi(R-M)^2\leq A_R(n;\mathbf x)\leq\pi R^2
\]
uniformly in $n$ and in every allowed shape. Combining this with (20) gives
\[
(1-M/R)^2\frac aV\leq p_4\leq\frac aV,\qquad
a=\frac{c}{24\pi^4R^6}.
\]
The upper bound also holds for every nondegenerate tetrahedron outside $E_4(M)$, because it only uses $A_R\leq\pi R^2$.

The disc-intersection factor is retained in the exact integral. The comparison is consequently uniform, including near arbitrary degeneracies, but it does not prove a reciprocal-volume identity. For example, under contraction of a fixed tetrahedron, $A_R(n;s\mathbf x)\to\pi R^2$ and $w_{s\mathbf x}=s w_{\mathbf x}$; the finite-radius intersection loss has not vanished at positive scale. Any cancellation with the lower partition contribution would require an additional exact argument.

### 4. Uniform lower-order bounds

Submission lines 252–301, equations (26)–(30), were checked in both regimes of each estimate.

For a pair of length $d$, $|n\cdot e|$ is uniform on $[0,1]$ under $\sigma$. Bounding the tangential intersection by $\pi R^2$ gives
\[
\frac1{2\varepsilon\pi R^2}
\int_0^1(1-ds/(2\varepsilon))_+\,ds.
\]
When $2\varepsilon\leq d$, the integral is $\varepsilon/d$ and the result is $1/(2\pi R^2d)$. Otherwise, with $v=d/(2\varepsilon)\in(0,1)$, the expression is
\[
\frac{v(1-v/2)}{\pi R^2d}\leq\frac1{2\pi R^2d},
\]
because $v-v^2/2\leq1/2$. Thus (26) holds for every $\varepsilon,d>0$.

For a noncollinear triangle, taking its longest edge as $de_1$ allows the third vector to be written $be_1+he_2$, with $h>0$, $|b|\leq d$ and $h\leq d$. Its area is $A=dh/2$. The event $w<2\varepsilon$ forces
\[
|n_1|<2\varepsilon/d,\qquad
|n_2|<4\varepsilon/h.
\]
Indeed, both projections of the two vectors have magnitude below $2\varepsilon$, and the second bound follows by subtracting $bn_1$.

If $\varepsilon<h/16$, this rectangle is contained in $|n_1|<1/8$, $|n_2|<1/4$. On both sphere graphs, $1/|n_3|<2$. Its planar area is $32\varepsilon^2/(dh)$; including the two graphs and dividing by $4\pi$ bounds its sphere probability by
\[
\frac{32\varepsilon^2}{\pi dh}
=\frac{16\varepsilon^2}{\pi A}.
\]
After bounding the normal overlap by $2\varepsilon$, the triple product integral is therefore at most $4/(\pi^3R^4A)$ in this regime.

If $\varepsilon\geq h/16$, the first strip alone has probability at most $2\varepsilon/d$, yielding
\[
\frac1{2\pi^2R^4\varepsilon d}
\leq\frac8{\pi^2R^4dh}
=\frac4{\pi^2R^4A}.
\]
This latter constant also dominates the first regime. There is no omitted case when the triangle has a short edge, is nearly collinear, or is small in all directions. Multiplying the bounds by $m_2,m_3$ proves (30):
\[
p_2\leq\frac{c}{4\pi R^2T^2D},\qquad
p_3\leq\frac{2c}{\pi R^4TA}.
\]
Together with $p_1=m_1$, this verifies that increasing $T$ makes all three lower contributions small while leaving $p_4$ fixed.

### 5. Residual positivity and finite correction laws

Submission lines 305–369, equations (31)–(37), correctly re-use the earlier finite-domain argument. The required earlier facts were re-established rather than accepted from a review label.

With $I=2\pi M^2$, $J=2\pi^2M^2$ and $a_2=\lambda/I$, $a_3=a_2/(4J)$, the relative pair subtraction is bounded by
\[
\frac{\lambda^2D}{a_2}\leq2\pi\lambda M^3.
\]
For triples, using $A\leq M^2/2$, $A/D_{ij}\leq M/2$ and $q_2\leq a_2/D$,
\[
\frac{\lambda^3A+\lambda A\sum q_2(ij)}{a_3}
\leq\frac{\lambda^3M^2}{2a_3}
+\frac{3\lambda a_2M}{2a_3}
=8\pi^3(\lambda M^3)^2+12\pi^2\lambda M^3.
\]
Condition (1) therefore gives both lower bounds in (33). It also makes all residuals nonnegative.

The anchored pair integral is $I$. For the triangle marginal, set the first vertex at the origin and use cylindrical coordinates around the fixed base line:
\[
\int_{B(0,M)}\frac{dz}{\operatorname{dist}(z,\text{line})}
=4\pi\int_0^M\sqrt{M^2-r^2}\,dr
=\pi^2M^2.
\]
Since $1/A=2/(dr)$, the marginal is at most $J/d$. The triangle support also requires the retained pair to lie in $E_2(M)$. Hence $\mathcal M K_3^0\leq J K_2^0$, including the support statement, not merely the pointwise bound on supported pairs.

The choice of $T$ in (35) is feasible for every already fixed finite $c,R$ because all three requirements are lower bounds on $T$. They give
\[
r_3\geq\frac{a_3}{4}K_3^0,\qquad
r_2\geq\frac{3a_2}{8}K_2^0,\qquad
\mathcal M r_3\leq a_3J K_2^0=\frac{a_2}{4}K_2^0.
\]
Thus
\[
F_2=r_2-\mathcal M r_3\geq\frac{a_2}{8}K_2^0,\qquad
F_3=r_3\geq\frac{a_3}{4}K_3^0.
\]
Moreover $F_2\leq q_2$, $F_3\leq q_3$. Their anchored integrals $Z_2,Z_3$ are finite and strictly positive; $Z_3\leq a_3JI$ is an explicit finite upper bound. Symmetry, measurability and translation and rotation invariance are preserved by the subtraction and marginalisation.

The domain restrictions in $r_2,r_3$ are essential and correctly placed. Outside the prescribed domains, the cylinder contributions remain in the final process; they are not subtracted by a kernel that must be nonnegative.

For a size-$j$ cluster, the rate $Z_j/j!$ and offset density $F_j(0,\mathbf y)/Z_j$ give the claimed lower same-parent density
\[
\frac{\mathcal M^{j-r}F_j}{(j-r)!}.
\]
To check this directly, take any ordered selection of $r$ of the $j$ labelled points. Reanchoring at its first selected point and relabelling the remaining points preserves Lebesgue measure, with Jacobian absolute value one. Symmetry and translation invariance make the resulting integral the same for every selection. There are $j!/(j-r)!$ selections, which cancel the parent-rate factor $1/j!$. This includes the selections that omit the initially anchored point. The correction clusters are simple because the offset laws are absolutely continuous and the coincidence sets have zero Lebesgue measure.

As a harmless convention, values of $p_r$ on null degeneracy sets can be set to zero before writing restrictions such as $\mathbf1_E(q_r-p_r)$. This avoids interpreting a symbolic $0\cdot\infty$ there. The submission already permits arbitrary null-set values and describes these expressions as restrictions, so this is not a missing mathematical hypothesis or a defect in the constructed measures.

### 6. Exact intensity and exact lower full densities

Submission lines 371–389, equations (38)–(39), have the correct coefficients and signs.

Write $Z_3=R_3$. The definitions imply
\[
Z_2=Q_2-P_2-R_3,\qquad
Q_2=a_2I-\lambda^2W=\lambda-\lambda^2W.
\]
The size-two stream has intensity $Z_2$, and the size-three stream has intensity $Z_3/2$. Thus their combined intensity is
\[
Q_2-P_2-\frac{R_3}{2}.
\]
Adding the cylindrical intensity $m_1$ and the singleton rate
\[
\beta=\lambda^2W+P_2+\frac{R_3}{2}-m_1
\]
gives exactly $\lambda$. From (35),
\[
m_1\leq\lambda^2W/2,\qquad
\beta\geq\lambda^2W/2>0.
\]
All quantities used in these finite subtractions are finite. There is no subtraction of infinite fourth marginals.

Globally the second same-parent density is $p_2+F_2+\mathcal MF_3=p_2+r_2$, and the third is $p_3+F_3=p_3+r_3$. They equal $q_2,q_3$ on the appropriate domains. Every pair of a noncollinear diameter-$M$ triangle lies in $E_2(M)$. Consequently substitution into
\[
\rho^{(2)}=\lambda^2+k_2,\qquad
\rho^{(3)}=\lambda^3+\lambda\sum k_2+k_3
\]
proves both exact lower-order identities. The quantities $\lambda^2,\lambda^3$ here are indeed formed from the final total intensity, not from the intensity of only one stream.

### 7. Full fourth density and joint parameter choice

Submission lines 393–424, equations (40)–(42), correctly account for the fourth density and give the stated uniform comparison.

The correction streams have at most three points, so the total fourth same-parent density is $p_4$. A nondegenerate tetrahedron has nondegenerate triangular faces and nonzero edges, and all of its lower blocks remain below the same diameter cap. Therefore on $E_4(M)$ the lower same-parent blocks are precisely $q_2,q_3$, and the complete fourth density is $p_4+B_4$ as written in (40).

The determinant estimates are uniform over all such shapes:
\[
V\leq M^3/6,\qquad
V/D_{ij}\leq M^2/6,\qquad
V/(D_{ij}D_{kl})\leq M/6,\qquad
V/A_J\leq M/3.
\]
The first two follow by taking an appropriate edge and two other edges from an endpoint as determinant vectors. For disjoint edges $12|34$,
\[
6V=|\det(x_2-x_1,x_3-x_1,x_4-x_3)|
\leq D_{12}M D_{34};
\]
relabel for the other pairings. The face bound follows from $V=A_Jh/3$ and $h<M$.

Counting six edges, three pairings and four faces gives exactly
\[
VB_4\leq
C=\frac{\lambda^4M^3}{6}
+\lambda^2a_2M^2
+\frac{a_2^2M}{2}
+\frac{4\lambda a_3M}{3}.
\]
Every term is nonnegative, and $0<C<\infty$.

The parameters can be selected without circular dependence:

1. Fix $\lambda,M$ satisfying (1), which fixes $a_2,a_3,C$.
2. Fix $\eta\in(0,1)$ and choose a finite $R\geq2M/\eta$.
3. Set $c=24\pi^4R^6C/\eta$, so $a=C/\eta$.
4. Choose a finite $T\geq1$ large enough for all three inequalities (35), and set $\ell=M$.

For example the last step is satisfied by taking $T$ at least the maximum of
\[
1,\quad
\left(\frac{2c}{\pi R^2a_2}\right)^{1/2},\quad
\frac{8c}{\pi R^4a_3},\quad
\left(\frac{\pi c}{8\lambda^2W}\right)^{1/3}.
\]
This explicit choice confirms that the large fourth-order amplitude does not conflict with the small lower contributions or with the intensity budget.

Finally,
\[
Vp_4\geq(1-M/R)^2a\geq(1-\eta)a,\qquad
V(p_4+B_4)\leq a+C=(1+\eta)a.
\]
The lower bound uses only $B_4\geq0$. Thus the theorem's comparison is for the **full** fourth density, and it is uniform on the whole nondegenerate domain.

### 8. Global regularity and the distinction between third and fourth moments

Submission lines 426–428 establish the remaining process requirements.

The cylindrical stream has finite intensity and finite local third moments, as checked above. Each bounded-population correction stream has finite local exponential moments: for $0\leq h\leq3$,
\[
e^{\theta h}-1\leq\frac{e^{3\theta}-1}{3}\,h,
\]
so the Poisson exponential formula and finite intensity bound its moment generating function on every bounded window. Singletons pose no further issue. The finite superposition is therefore stationary, isotropic, simple, locally finite and has finite third local count moments.

The fourth local divergence needs the local lower bound, not merely the fact that the population fourth moment is infinite. Inside any nonempty open ball, place a sufficiently small square, with diameter strictly below $M$. Allow the first three vertices to vary in small three-dimensional neighbourhoods. For each resulting base triangle, use orthonormal in-plane coordinates and a signed normal coordinate $h$ for the fourth vertex near the fourth corner. Shrinking the neighbourhoods preserves the ball and diameter conditions; the base area remains positive and bounded, all edges remain nonzero, and
\[
V=A_{\rm base}|h|/3.
\]
The fourth-coordinate transformation has Jacobian one. An in-plane patch of positive area and a normal interval containing $h=0$ therefore contribute
\[
\int_{0<|h|<\delta}\frac{dh}{|h|}=\infty.
\]
The base triples vary over positive Lebesgue measure. Tonelli and $(1-\eta)a>0$ show that $\alpha^{(4)}(B^4)=\infty$, hence $\mathbb E X(B)^4=\infty$. This re-establishes the consequential part of the earlier moment lemma and explains why no finite-fourth-moment assumption has been introduced.

Global absolute continuity is also established. The cylinder same-parent measures are integrals of Lebesgue densities. Their bounds prove $p_2,p_3,p_4$ finite off, respectively, coincident, collinear and coplanar null sets, including outside the prescribed domains. The correction measures have the displayed densities, whose marginals are bounded by the finite reciprocal pair and triangle bounds. The full measures then follow from the partition formula.

A null exceptional set for any block pulls back to a null set in the complete tuple space; this follows by Tonelli and a countable exhaustion of the other coordinates. Each partition product is therefore finite almost everywhere. A finite sum preserves that property. There is no additional singular mass on coincidences, collinear triples, coplanar quadruples or any unprescribed outside-domain configuration.

The fourth density is not locally integrable near suitable coplanar families, but it is finite almost everywhere and defines a $\sigma$-finite measure. For instance, its intersections with bounded coordinate boxes and finite density sublevel sets give a countable finite-measure cover, after assigning zero on the null exceptional set. There is no conflict between this fact, infinite bounded-window fourth moments and almost-sure local finiteness.

### 9. Why the result remains partial

The unresolved equation (43) is exactly the required full fourth-order condition for this constructed family:
\[
\frac{c}{12(\pi R^2)^4}
\int_{S^2}\frac{A_R(n;\mathbf x)}{w_{\mathbf x}(n)^3}\,\sigma(dn)
+B_4(\mathbf x)=\frac{a_4}{V(\mathbf x)}.
\]
The proof neither solves this equation nor constructs another actual mark measure producing its residual. Positivity of a proposed residual alone would not supply the joint finite-configuration law or the required lower marginals.

The intensity condition is also genuine scope in the theorem, not removable by the displayed rescaling. Under $x\mapsto sx$, intensity becomes $\lambda/s^3$ and the diameter cap becomes $sM$, so $\lambda M^3$ is unchanged.

Nor does taking $\eta\downarrow0$ prove exact S1. Here $a=C/\eta$ diverges, while the cluster law and its type rates change with $\eta$. The comparison does not give convergence to a reciprocal-volume density with a finite fixed coefficient. Even if a subsequential point-process limit were obtained, convergence in distribution with these finite intensities would not justify passage of fourth factorial expectations, which need additional control absent from the proof. The author correctly makes no such limit claim.

## Finding register

| ID | Location in frozen v02 | Precise mathematical issue | Consequence | Repair/status |
|---|---|---|---|---|
| **P1V02-01** | Lines 35–45, 194–246, 393–424 and equation (43) | Only a relative bound is established for the full fourth density. The disc-intersection factor and the 14 lower-block contributions have not been made to satisfy an exact constant-over-volume identity. | Exact fourth-order S1 is unresolved; the validated approximation cannot count as a pass. | **Open exact-target obligation.** Prove (43) for a finite constant, or supply and verify a different actual process law. No invalidity of the stated approximate theorem was found. |
| **P1V02-02** | Lines 23–28, equations (31)–(37), line 445 | Residual positivity and the correction intensity budget are proved only under (1), a restriction on $\lambda M^3$. | The theorem does not cover every independently prescribed $(\lambda,M)$. | **Open exact-target obligation.** Remove the restriction by proof or construct the missing parameter regimes. Dilation alone cannot do so. |
| **P1V02-03** | Line 447 and parameter choice (42) | Arbitrarily small relative error is obtained with $a=C/\eta\to\infty$ and a changing law. No finite-coefficient limit or convergence of fourth factorial measures is proved. | A limiting argument is not presently a route from the theorem to S1. | **Acknowledged limitation.** Any future limit argument must establish its own existence, nontriviality, coefficient and measure convergence claims. |
| **P1V02-04** | Equations (8)–(16), (30), (35)–(39); prior P1V01-02 | The previously absent actual mark law is now supplied, and its first three contributions can be controlled without changing its fourth density. It realises (20), not the exact fourth residual. | The former construction gap is closed for the partial theorem, while its exact-S1 portion remains open. | **Partial closure, independently verified.** Do not label P1V01-02 fully solved for the active target. |
| **P1V02-05** | Equations (5)–(7); prior P1V01-03 | The earlier unrestricted product-measure notation has been replaced by a $\sigma$-finite parent-level definition, with the density version used after image $\sigma$-finiteness is available. | No non-$\sigma$-finite product ambiguity affects this theorem. | **Closed.** All parent partitions and multiplicities rechecked. |
| **P1V02-06** | Lines 158–165, 244, 426–428; prior P1V01-01 | The former finite-fourth-moment construction has been replaced by one with finite third and infinite fourth local moments, while retaining global full absolute continuity and finite-almost-everywhere densities. | The moment-class and regularity part of the earlier shortfall is resolved; exact equality and all-intensity coverage are not. | **Closed for these requirements.** Local reciprocal-height divergence and global absence of singular mass independently verified. |
| **P1V02-07** | Lines 312, 451 and the source paragraphs; prior P1V01-04 | References to “accepted” earlier results are provenance labels, not mathematical premises. The needed earlier estimates and normalisation are supplied and can be rederived. | No unavailable historical verdict is needed for the partial theorem. Historical obstruction and broader seed claims are outside this review's certification. | **No active source gap.** Prefer naming the precise frozen lemma or calculation over relying on an acceptance label. |

## Amendment implications

No new general obstruction is proved by v02. The low-intensity condition is a sufficient condition for this correction construction, not a necessity theorem for Poisson clusters or for S1. Approximation at fourth order is a limitation of the submitted result, not evidence that exact equality is impossible.

The moment calculation does prove, independently, that a positive reciprocal-volume lower bound on all sufficiently small shapes forces infinite fourth moments on every ball. It does not exclude the broad S1 process class and does not justify an altitude cutoff. The current construction demonstrates that this moment behaviour can coexist with almost-sure local finiteness, finite intensity, finite third local moments and global finite-almost-everywhere fourth densities.

S1 remains the active target at its supplied hash. No change of equality to approximation, restricted intensity, geometric domain, process class or moment requirement is adopted or approved in this review. Attempt 2 remains consumed; two substantive submissions remain within the stated four-submission policy. The optional owner-amendment checkpoint after three unsuccessful reviewed submissions has not yet been reached by this track.

The supplied S0-to-S1 amendment records the historical S0 decision. This construction review does not reopen or recertify its underlying obstruction proofs, and an S1 partial result does not alter the S0 record.

## Source and coding evidence

The mathematical dependencies used here are supplied in the frozen packet or are explicitly reconstructed above. The relevant earlier proof passages are:

- `prior_dependency_v01.md`, lines 58–84: local pair and triangle integrability and reciprocal-height divergence;
- lines 90–136: whole-space finite-mark construction and parent partitions, with the v02 notation repair;
- lines 187–210: bounded-population local moment control;
- lines 283–376: residual positivity, marginal domination, finite-cluster normalisation and intensity.

The supplied seed excerpt, SHA-256 `f0d755efa2b82343a5ff7f171c0ba69ccdcd92ba67a36106e9c47052197a2ac9`, contains the corresponding pair-and-triangle calculation. Its provenance file, SHA-256 `84466d1ec8e8106752e5e634f0878d826d11940490a9404ea3ff3586279155a6`, records where that excerpt came from. Its altitude-restricted fourth-order theorem is not imported into the current theorem.

The polar identity has a complete elementary proof with all constants, so no specialised citation is needed. The basic Poisson factorial rule follows from independent Poisson counts on disjoint finite-measure sets, followed by nonnegative approximation and $\sigma$-finite exhaustion. Its uses here have the required hypotheses. No source attribution, novelty assertion or present-open-status claim was needed.

No external source or coder request was necessary. Executed code was restricted to reading assigned files, SHA-256 verification, selected own-session metadata and numerical usage extraction, and saving the review artifacts. No mathematical simulation, numerical quadrature, symbolic package, proof assistant or finite sampling was used to certify continuum assertions.

## Presentation judgement

The submission is readable and unusually clear about its actual scope. It states the two exact lower laws and the approximate fourth law separately, keeps the disc-intersection factor in the exact formula, retains the full partition terms, and explicitly rejects an unjustified limiting passage to S1.

The most useful small improvements are:

- Give the explicit maximum defining a sufficient $T$, as above, immediately after the final choices of $R,c$. This makes the simultaneous intensity and lower-kernel requirements easy to verify.
- State a finite version of each density on degeneracy sets before defining the restricted residual kernels. This avoids superficial ambiguity in products of indicators with expressions that have infinite null-set values.
- Replace “accepted v01 construction” as mathematical justification by an exact reference to its displayed estimate, while retaining the current self-contained derivation.
- Expand the final fourth-moment sentence into a short reciprocal-height argument, since the finite-third/infinite-fourth distinction is central to this construction.

These are exposition improvements; none is an unresolved essential gap in the partial theorem.

## Review summary and repairs

The population-dependent cylindrical mark law resolves a substantive construction issue from v01. The fourth factorial population factor cancels exactly, its inverse-width integral has the stated normalisation, and its lower contributions admit uniform bounds on every allowed near-degenerate shape. The finite correction streams are nonnegative, the singleton rate fixes the intensity exactly, and the full partition calculation establishes the claimed exact pair and triangle laws and uniform fourth comparison. Whole-space existence, local finiteness, simplicity, moment claims and global full absolute continuity all survive this audit.

For a further exact-S1 submission, the indispensable repairs are mathematical: establish the exact fourth identity with a finite configuration-independent coefficient, and cover every prescribed intensity at fixed $M$. Repeating the approximation, proving a smaller-domain identity, or proposing a formal nonnegative residual without an actual compatible process law would not close these obligations.

Prior-item disposition: P1V01-01 is partially resolved in its moment-class component and remains open in exactness and intensity; P1V01-02 is resolved for the new partial law but not for the exact residual; P1V01-03 is closed; P1V01-04 causes no active dependency gap in this self-contained theorem.

## Accounting and freeze

`preflight.json` records the setup/run roots, packet verification, all assigned input hashes, own session identity, actual current model and effort, and the numerical preflight usage checkpoint. Its SHA-256 is `5840bcfd976080e36118bd79cd21c9eedb083553d4c6dde35194a75682094608`.

The own-session evidence path is
`[local path omitted]`.
`freeze.json` records this report's hash and word count and the last exposed numerical token event at freeze. Input, cached-input, cache-write-input, output, reasoning-output and total-token fields are available as runtime counters. Cumulative snapshots are not summed, and reasoning-output tokens are not added again to output.

Final completed-turn totals and end time are **NR at report freeze** and require post-turn reconciliation by the coordinator. Parent/child inclusion semantics and actual account charge are NR; this reviewer launched no children. No estimated tokens, inferred costs or private deliberation transcript is included.

This is a single-track construction review. No cross-track final synthesis was performed.
