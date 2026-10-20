# Critical review — final synthesis of the reciprocal-simplex rerun

- **Run / reviewer model / reasoning:** `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- **Review type:** fresh final synthesis. This is the authorised cross-approach comparison stage.
- **Problem hash:** `common/problem_statement.md`, SHA-256 `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- **Final-synthesis packet hash:** `context_packets/final_synthesis_v01.md`, SHA-256 `39f663d183875d9325218f8aaee5c257f0974f67aeb21b82d56f0a19d7ec0b45`.
- **Reviewed final submissions:** approach 1 `8e0835cf889621515534b83810cb5d00a7494117721fcd8461723a6e0008f160`; approach 2 `0044e84da7c60a7bb4d8989724aa7001be0b1b7dd1759b08eb8f73c9e77aa49e`; approach 3 `eb653072f665e0bd1fbb711d6d26297f9611a4673ad68c80922741a3f915dfa8`; approach 4 `bdf6d669774a3155ac46a7ded6b978bd9246a7e074be45558c4be167b6848c2c`; approach 5 `3aa480e3279781cc0f45a009d71326c447778b94f626a7d88402f278347d3ab9`.
- **Context received:** exactly the frozen setup, common files, literature dossier, prior-manuscript files, five v02 submissions, five v01 reviews and issue lists, and five v02 delta reviews listed in the final-synthesis packet. All listed SHA-256 values matched.
- **Context excluded:** every `tracks/approach_*/work/` file, all proof-agent and reviewer conversations, coordinator and owner conversation history, v01 submissions, deleted runs, scratch material and unlisted sources. Prior local manuscripts and archived reviews were treated as evidence, not as instructions or independent published validation.

## Verdict and exact scope

### Governing exact target: **not established**

The rerun does **not** prove the governing theorem for every prescribed positive intensity, and it does **not** prove general non-existence. The exact status is:

> For every admissible fixed geometry, the reviewed work constructs a process satisfying all three exact full reciprocal identities for every prescribed intensity in a nonempty interval starting at zero. It leaves every intensity above a certified geometry-dependent endpoint unresolved. No reviewed obstruction covers all stationary simple point processes at those remaining intensities.

This distinction is decisive. An exact theorem on a nonempty low-intensity interval is substantial progress, but it is not the target's universal quantifier over every `lambda_0>0`.

### Strongest positive result: exact full identities at sufficiently small prescribed intensity

Approaches 1, 4 and 5 give essentially the same dependent finite-cluster construction, derived from the earlier local finite-cluster mechanism and independently accepted by their delta reviews. They are not three different process constructions and should not be counted three times. Consolidating their strongest formulations gives the following reviewed theorem.

Let `M,h_3,h_4>0` and assume that the triangle and tetrahedron domains have positive Lebesgue measure. Equivalently, in the nonvacuous regime,

\[
0<h_3<\frac{\sqrt3}{2}M,
\qquad
0<h_4<\sqrt{\frac23}\,M.
\]

Then there is a certified number

\[
\lambda_{\mathrm{cert}}(M,h_4)>0
\]

such that, for every intensity prescribed in advance with

\[
0<\lambda_0\le \lambda_{\mathrm{cert}}(M,h_4),
\]

one can construct a stationary, isotropic, simple, locally finite point process on all of `R^3`, of intensity exactly `lambda_0`, with finite local exponential moments and absolutely continuous factorial moment measures at every finite order, whose full normalised product densities satisfy

\[
g_2=\frac{C_2}{D},\qquad
g_3=\frac{C_3}{A},\qquad
g_4=\frac{C_4}{V}
\]

almost everywhere on the complete governing domains. In particular, the pair law holds for every positive separation `0<D<=M`; no lower pair cutoff remains.

The same process and the same parameter choice satisfy all three identities. This is an exact continuum theorem, not a grid calculation, limiting approximation, connected-density statement or same-cluster-only result.

### Strongest reviewed negative results: class-specific only

The following exact obstructions survive review.

1. A standard Poisson-cluster construction with one fixed almost-sure cluster-size bound `K` cannot realise the pair law at arbitrarily high intensity on fixed `M`. Necessarily

   \[
   \lambda_0M^3\le \frac{3(K-1)}{2\pi}.
   \]

   For clusters of size at most four this is `lambda_0 M^3 <= 9/(2 pi)`. This does not cover unbounded clusters, a size cap allowed to grow with intensity, non-Poisson parents, Cox processes or general point processes.

2. No Cox process directed by the reviewed class of Poisson-centred, radius-only, uniformly weighted spherical carriers can satisfy the pair and triangle laws simultaneously, even with arbitrary nonnegative radial mixing. This is a shape obstruction at order three, not a general Cox obstruction.

3. No Cox process with an absolutely continuous stationary directing field $Z(x)\,dx$ satisfying $\mathbb E Z(0)^2<\infty$ can realise the no-cutoff pair singularity. Ordinary finite-variance log-Gaussian Cox processes are included and have an additional third-order shape obstruction.

4. The particular exact finite-cluster process in the earlier local manuscript is not Cox. This blocks the tempting shortcut of applying Cox mass scaling to that process law. It does not exclude another Cox law with the same restricted low-order product densities.

5. No finite-time spatial projection of a stationary scalar linear subcritical Hawkes process with nonnegative causal triggering density $\phi\in L^1\cap L^\infty$ can realise the pair law. Its projected pair correlation is essentially bounded, whereas `C_2/D` is essentially unbounded near the pair diagonal. Singular, marked, multitype, carrier, nonlinear and critical variants remain unresolved.

6. Stationary Hermitian determinantal processes are excluded because `g_2<=1`, while `C_2/D` diverges as `D` decreases to zero. This is again a subclass obstruction.

None of these results is general non-existence for the governing finite-domain, positive-altitude problem.

## The governing problem, with all quantifiers

For each prescribed tuple

\[
(\lambda_0,M,h_3,h_4),\qquad \lambda_0,M,h_3,h_4>0,
\]

whose geometric domains are nonempty with positive Lebesgue measure, the target asks for one point process `X` on all of `R^3` satisfying all of the following.

1. `X` is stationary, simple and locally finite, has intensity exactly `lambda_0`, and has finite local count moments through order four.
2. Its ordered factorial moment measures through order four are absolutely continuous. Writing their densities as `rho^(n)` and

   \[
   \alpha^{(n)}(B_1\times\cdots\times B_n)
   =\mathbb E\!\sum_{x_1,\ldots,x_n\in X}^{\ne}
   \prod_{i=1}^n\mathbf1\{x_i\in B_i\},
   \qquad
   \rho^{(n)}=\frac{d\alpha^{(n)}}{d(x_1,\ldots,x_n)},
   \]

   and then

   \[
   g_n=\rho^{(n)}/\lambda_0^n,
   \]

   these are full product densities: every allocation of the observed labels among parents or clusters contributes.
3. For pairwise distinct points,

   \[
   D=\|x_2-x_1\|,
   \qquad
   A=\frac12\|(x_2-x_1)\times(x_3-x_1)\|,
   \]

   \[
   V=\frac16\left|\det[x_2-x_1,x_3-x_1,x_4-x_1]\right|.
   \]

4. The pair domain is

   \[
   \mathcal D_2=\{(x_1,x_2):0<D\le M\}.
   \]

   There is no positive lower cutoff on `D`.
5. The triangle domain `D_3` consists of every noncollinear triple of diameter at most `M` for which **each** vertex has distance at least `h_3` from the opposite affine line.
6. The tetrahedron domain `D_4` consists of every noncoplanar quadruple of diameter at most `M` for which **each** vertex has distance at least `h_4` from the opposite affine plane. The problem imposes no separate `h_3` condition on the four triangular faces of a target tetrahedron.
7. There must be positive constants `C_2,C_3,C_4`, allowed to depend on the prescribed tuple and the process but not on the configuration, such that one and the same process satisfies

   \[
   g_2(x_1,x_2)=\frac{C_2}{D},
   \quad
   g_3(x_1,x_2,x_3)=\frac{C_3}{A},
   \quad
   g_4(x_1,x_2,x_3,x_4)=\frac{C_4}{V}
   \]

   Lebesgue-almost everywhere on `D_2,D_3,D_4`, respectively.

The universal quantifier is over every admissible geometry and **every** prescribed `lambda_0>0`. Constants selected after the process is constructed are permitted; selecting the intensity after the geometry is fixed is not. Approximation, a finite grid, a smaller shape domain, a chosen rather than prescribed intensity, or equality only for connected densities does not meet the target.

## Reconstruction of the strongest exact construction

### 1. Nested internal supports

Put

\[
h=\min\{h_3,h_4\},\qquad H=h_4.
\]

The construction uses

\[
S_2=\{0<D\le M\},
\]

\[
S_3=\{A>0,\ \operatorname{diam}\le M,\ \text{all triangle altitudes}\ge h\},
\]

and `S_4=D_4`. Thus `S_2=D_2`, `D_3` is contained in `S_3`, and `S_4=D_4`.

The enlargement of `S_3` is not a hidden weakening. It makes the constructed area identity hold on a possibly larger domain. It is needed because a face of a tetrahedron in `D_4` need not satisfy the target threshold `h_3`. For a face vertex, however, the opposite edge line lies in the corresponding tetrahedral opposite-face plane. Distance to the line is at least distance to the plane, so every face altitude is at least `h_4`, and hence at least `h`. Every face used in the fourth-order recursion therefore lies in `S_3`.

Define

\[
K_2=\frac{\mathbf1_{S_2}}D,\qquad
K_3=\frac{\mathbf1_{S_3}}A,\qquad
K_4=\frac{\mathbf1_{S_4}}V.
\]

The key constants are

\[
I=2\pi M^2,\qquad L=\frac{4\pi}{3}M^3,\qquad B=2\pi^2M^2,
\]

\[
G=6\pi\left[M^2\log\!\left(\frac{M}{H}\right)
-\frac{M^2-H^2}{2}\right]>0.
\]

The no-cutoff pair singularity is locally and anchored integrable:

\[
\int_{0<|y|\le M}\frac{dy}{|y|}=2\pi M^2=I.
\]

If $\mathcal M$ denotes integration over one omitted coordinate, cylindrical and height-slice calculations give

\[
\mathcal M K_3\le BK_2,
\qquad
\mathcal M K_4\le GK_3.
\]

The second inequality uses `V=A|u|/3`, the two signs of the fourth-vertex height, `H<=|u|<=M`, and ball cross-sectional area at most `pi(M^2-u^2)`. The positive `H` is exactly what removes the logarithmic flattening divergence.

### 2. A certified low-intensity interval

For a proposed intensity `lambda`, set

\[
a_2=\frac{\lambda}{I},\qquad
a_3=\frac{a_2}{4B},\qquad
a_4=\frac{a_2}{16BG}.
\]

The pointwise subtraction bounds are

\[
E_2(\lambda)=IM\lambda,
\]

\[
E_3(\lambda)=6BM\lambda+2BIM^2\lambda^2,
\]

\[
E_4(\lambda)=\frac83IBGM^3\lambda^3
+16BGM^2\lambda^2
+\frac{8BGM}{I}\lambda
+\frac{16GM}{3}\lambda.
\]

Each is continuous and increasing on $[0,\infty)$, vanishes at zero, and $E_2$ diverges. Therefore

\[
\{t\ge0:E_2(t),E_3(t),E_4(t)\le1/2\}
=[0,\lambda_{\mathrm{cert}}]
\]

for an attained positive finite endpoint. This endpoint is a sufficient certificate, not a proved sharp realizability threshold.

Approach 4 also supplies a fully explicit, possibly smaller, sufficient endpoint by taking the minimum of

\[
(2IM)^{-1},\ (24BM)^{-1},\ (8BIM^2)^{-1/2},
\]

\[
\left(\frac{3}{64IBGM^3}\right)^{1/3},\
(128BGM^2)^{-1/2},\ \frac{I}{64BGM},\ \frac{3}{128GM}.
\]

This makes the dependence on `M` and `h_4` completely explicit. The threshold has the physical units of intensity. Its lack of `h_3` dependence reflects the enlarged internal triangle support; `h_3` still enters the admissibility condition for a nonvacuous target triangle domain.

### 3. Two triangular inversions

The first inversion defines the desired same-parent, or factorial-cumulant, kernels by subtracting every lower full-density partition:

\[
q_2(12)=\mathbf1_{S_2}(12)
\left(\frac{a_2}{D(12)}-\lambda^2\right),
\]

\[
q_3(123)=\mathbf1_{S_3}(123)
\left(\frac{a_3}{A(123)}-\lambda^3
-\lambda\sum_{i<j}q_2(ij)\right),
\]

and

\[
\begin{aligned}
q_4(1234)=\mathbf1_{S_4}(1234)\Bigg(&\frac{a_4}{V(1234)}-\lambda^4
-\lambda^2\sum_{i<j}q_2(ij)\\
&-\sum_{ij\mid k\ell}q_2(ij)q_2(k\ell)
-\lambda\sum_{|T|=3}q_3(T)\Bigg).
\end{aligned}
\]

Here the pair-pair sum has the three disjoint pairings and the final sum has the four faces. The geometric inequalities for diameter-`M` simplices, with exactly six edge terms, three pairings and four faces, show that

\[
\frac12a_jK_j\le q_j\le a_jK_j,
\qquad j=2,3,4,
\]

whenever the three `E_j` are at most `1/2`.

The second inversion obtains genuine exact-size cluster densities:

\[
F_4=q_4,
\qquad
F_3=q_3-\mathcal Mq_4,
\qquad
F_2=q_2-\mathcal Mq_3+\frac12\mathcal M^2q_4.
\]

The marginal bounds and amplitude ratios give

\[
F_4\ge\frac12a_4K_4,
\qquad
F_3\ge\frac14a_3K_3,
\qquad
F_2\ge\frac14a_2K_2.
\]

Thus the cluster laws are nonnegative, not signed formal kernels. Their anchored masses `Z_2,Z_3,Z_4` are finite and strictly positive.

### 4. Whole-space process, intensity and regularity

For `j=2,3,4`, take an independent homogeneous Poisson parent process of rate `Z_j/j!`. A type-`j` parent at `z` emits

\[
\{z,z+Y_2,\ldots,z+Y_j\},
\]

where the relative mark has density `F_j(0,.)/Z_j`. Add an independent singleton Poisson process with rate

\[
\lambda_1=\lambda^2L+\frac{Z_3}{2}+\frac{Z_4}{3}>0.
\]

Translation invariance and full permutation symmetry of every `F_j`, together with a determinant-one change of relative coordinates when the distinguished daughter is changed, make this an unlabelled cluster law with no preferred root.

Writing `Q_j` for the anchored mass of `q_j`, integration of the second inversion gives

\[
Z_4=Q_4,\qquad
Z_3=Q_3-Q_4,\qquad
Z_2=Q_2-Q_3+\frac12Q_4.
\]

Moreover

\[
Q_2=a_2I-\lambda^2L=\lambda-\lambda^2L.
\]

The non-singleton intensity plus `lambda_1` therefore equals exactly `lambda`. No post-construction scaling or intensity selection is hidden here.

Every cluster has at most four points and diameter at most `M`. Only parents in a bounded enlargement can hit a bounded observation window, so bounded-window counts have finite exponential moments. The relative mark laws and parent locations are diffuse, so collisions have probability zero. The process is stationary, simple and locally finite; the rotation-invariant kernels also give isotropy. Marginalised same-parent blocks have ordinary densities, and finite parent-partition sums give absolutely continuous factorial moment measures at every finite order.

### 5. Full product densities

For a type-`j` cluster, the same-parent ordered `r`-tuple density is

\[
b_r^{(j)}=\frac1{(j-r)!}\mathcal M^{j-r}F_j.
\]

The coefficient follows from `j!/(j-r)!` injective assignments of the observed ordered labels to the daughters against the labelled full-configuration density `F_j/j!`; permutation symmetry and determinant-one re-rooting make all assignments equal.

After summing cluster types, the same-parent block densities are `q_2,q_3,q_4`, while the first-order density is `lambda`. Allocating each observed label to its parent gives the complete full hierarchy

\[
\rho^{(2)}(12)=\lambda^2+q_2(12),
\]

\[
\rho^{(3)}(123)=\lambda^3+\lambda\sum_{i<j}q_2(ij)+q_3(123),
\]

\[
\begin{aligned}
\rho^{(4)}(1234)={}&\lambda^4+\lambda^2\sum_{i<j}q_2(ij)
+\sum_{ij\mid k\ell}q_2(ij)q_2(k\ell)\\
&+\lambda\sum_{|T|=3}q_3(T)+q_4(1234).
\end{aligned}
\]

These contain respectively all `2,5,15` set partitions. Substitution of the residual definitions cancels every lower partition and yields

\[
\rho^{(2)}=\frac{a_2}{D}\quad\hbox{on }S_2,
\qquad
\rho^{(3)}=\frac{a_3}{A}\quad\hbox{on }S_3,
\qquad
\rho^{(4)}=\frac{a_4}{V}\quad\hbox{on }S_4.
\]

The target constants can be taken as

\[
C_2=\frac1{I\lambda},\qquad
C_3=\frac1{4BI\lambda^2},\qquad
C_4=\frac1{16BGI\lambda^3}.
\]

This completes the restricted exact theorem.

## Approach-by-approach comparison

| Approach | Reviewed result | Exact target verdict | Principal remaining limitation |
|---|---|---|---|
| 1. Poisson clusters | Exact full identities with no lower pair cutoff for every prescribed `0<lambda_0<=lambda_cert`; fixed-bounded-cluster intensity obstruction | **Restricted exact theorem only** | Intensities above the certified endpoint; obstruction does not cover growing or unbounded clusters |
| 2. Cox processes | Exact directing-measure reformulation and intensity scaling; sphere, finite-pointwise-second-moment field and LGCP exclusions; prior finite-cluster law shown non-Cox | **General Cox case unresolved** | No stationary diffuse directing measure with all three exact tensor moments; subclass obstructions do not cover general Cox laws |
| 3. Hawkes processes | Full projected hierarchy and exact exclusion of scalar linear subcritical $L^1\cap L^\infty$ kernels | **Restricted negative theorem only** | Singular, marked, multitype, carrier, nonlinear and critical mechanisms; no exact Hawkes witness |
| 4. Agent-selected construction | Same finite-cluster exact theorem as approach 1, with an explicit conservative threshold and a measure-form fixed-`K` obstruction | **Restricted exact theorem only** | Same high-intensity gap; not a distinct construction from approach 1 |
| 5. Necessary conditions | Same finite-cluster exact theorem plus general Yamada/count and covariance inequalities | **Restricted exact theorem plus non-decisive necessities** | Pair-amplitude inequalities do not contradict the target because `C_2` is free; no high-intensity conclusion |

### Approach 1: Poisson clusters

This track supplies the strongest clean statement of the finite-cluster result. Its endpoint is the maximum of the common `E_j<=1/2` feasible set, so the endpoint is included rather than merely approached. It also gives the fixed-bounded-cluster obstruction

\[
\lambda\le\frac{3(K-1)}{2\pi M^3}.
\]

The proof is self-contained through the full fourth density. Its exact remaining gap is not a local proof defect: a different construction or a genuinely enlarged cluster class is needed above `lambda_cert`.

### Approach 2: Cox processes

For a Cox process directed by a random locally finite measure `Lambda`, the checked equivalence is

\[
\alpha_X^{(n)}=\mathbb E\Lambda^{\otimes n},\qquad n\le4.
\]

The target becomes a truncated random-measure moment problem: find a stationary, almost surely diffuse, locally finite `Lambda` with finite fourth local mass moments and absolutely continuous tensor moments whose densities equal the reciprocal targets on the frozen domains. Conversely, every Cox solution has such a directing law. Simplicity removes directing atoms, and the conditional fourth Touchard polynomial transfers finite fourth point-count moments back to `E Lambda(B)^4`.

This approach has one unusually useful property. If `Lambda` is an exact witness at intensity `lambda>0`, then

\[
\Lambda'=(\lambda_0/\lambda)\Lambda
\]

has intensity `lambda_0` and the same normalised `g_2,g_3,g_4` on exactly the same physical domains. Thus one exact positive-intensity Cox witness for a fixed geometry would solve the target at every prescribed intensity for that geometry. The missing object is the witness, not intensity tuning.

The reviewed spherical subclass is broader than the first local spherical manuscript. It allows a Poisson population of spheres with arbitrary nonnegative radius density `p(r)` and uniform radius-dependent surface weight `b(r)`. Its one-carrier terms have the form

\[
q_2(D)=\frac{2\pi}{D}\int_{D/2}^{L}p(r)b(r)^2r^2\,dr,
\]

\[
q_3=\frac1A\int_{R_3}^{L}
\frac{p(r)b(r)^3r^3}{\sqrt{r^2-R_3^2}}\,dr,
\]

\[
q_4=\frac{p(R_4)b(R_4)^4R_4^3}{6V}
\]

almost everywhere, with the complete Poisson-carrier partition expansion added afterwards. Exact pair matching alone is possible in this class: the submission gives an explicit nonnegative radial mixture producing `m_2=C_2/D` on all `0<D<=M` for any `C_2>=M` at unit intensity, and Cox scaling then gives any intensity. The obstruction appears at order three. `Aq_3` depends only on circumradius, whereas the full pair and triangle targets force

\[
C_3+2A-C_2A\sum_{i<j}D_{ij}^{-1}
\]

to be constant over triangle shape at fixed circumradius. An isosceles deformation shows that it is not.

Two further exclusions are exact but narrower. A finite-pointwise-second-moment intensity field cannot produce the pair blow-up. An ordinary LGCP also obeys

\[
g_n=\prod_{i<j}g_2(x_i,x_j),
\]

which at order three would force constant circumradius. Finally, the earlier exact finite-cluster law is not Cox: in one suitable bounded window its count has a compound-Poisson pgf with a positive fourth-jump coefficient, whose analytic continuation cannot be the Laplace transform of a nonnegative directing mass.

The general Cox moment tests remain necessary but non-decisive. For a ball of radius `R<=M/2`, Jensen's inequality gives

\[
C_2\ge\frac{5R}{6},
\]

and hence `C_2>=5M/12`. Truncated Stieltjes moment matrices and mixed test-function analogues must be positive semidefinite. They do not close because the target leaves positive-measure families of low-altitude triples and quadruples unspecified.

### Approach 3: Hawkes processes

This track first makes the spatialisation operation explicit. A stationary scalar linear Hawkes process is constructed on space-time `R x R^3`; events in a finite time interval of length `T` are retained and projected to space. Projection over all time would give infinite spatial intensity, while a deterministic time slice of a diffuse process is empty. The finite interval yields a stationary spatial process on all of `R^3`.

For a nonnegative causal density `phi` with branching mass `eta<1`, the immigrant rate

\[
\mu=\lambda_0(1-\eta)/T
\]

gives projected intensity exactly `lambda_0`. The Borel total-progeny law has an exponential moment in the subcritical regime, which yields finite local fourth moments. The revised measure-first argument retains the fixed-root Dirac mass until immigrant integration removes it, proving absolute continuity through order four before projecting in time.

The track then converts factorial cumulants to full products. If `Q_n^I` are the projected factorial-cumulant densities, then

\[
\rho_I^{(2)}=\lambda_0^2+Q_2^I,
\]

\[
\rho_I^{(3)}=\lambda_0^3+\lambda_0\sum Q_2^I+Q_3^I,
\]

and the fourth density contains the all-singleton term, six pair-singleton-singleton terms, three pair-pair terms, four triple-singleton terms and `Q_4^I`. The tree formulas are not substituted directly for `g_n`.

When $\phi\in L^1\cap L^\infty$, the descendant resolvent $\Psi=\sum_{m\ge1}\phi^{*m}$ belongs to both spaces and the exact second cumulant formula is essentially bounded. The projected `g_2` is therefore bounded, contradicting `C_2/D` on a positive-measure family of arbitrarily close pairs. This proves the advertised restricted negative theorem.

For singular scalar kernels, the track derives necessary residuals rather than a false general conclusion. Normalised nonnegative cumulants would have to obey

\[
c_2^I(i,j)=\frac{C_2}{D_{ij}}-1\ge0,
\]

so `C_2>=M`, and

\[
c_3^I(1,2,3)
=\frac{C_3}{A}+2-C_2\sum_{i<j}\frac1{D_{ij}}\ge0
\]

almost everywhere on `D_3`. At fourth order the triangle residual may be substituted for a tetrahedral face only on the intersection where that face itself lies in `D_3`. Dropping the nonnegative third- and fourth-cumulant terms gives a weaker pair-only inequality on all of `D_4`. No reviewed kernel realises these residuals.

### Approach 4: agent-selected construction

The selected route is the same dependent finite-cluster inversion as approach 1, not a new geometry. Its main independent value in synthesis is presentation: it supplies the explicit termwise threshold above, formulates the fixed-`K` obstruction as a reduced measure without assuming a global same-parent density, and makes reanchoring explicit. It reaches the same mathematical boundary as approach 1.

### Approach 5: necessary conditions

This track again verifies the no-cutoff finite-cluster theorem, then adds process-class-independent second-order inequalities. For every bounded positive-measure Borel set `B_0` with diameter at most `M`, put

\[
J(B_0)=\iint_{B_0^2}\frac{dx\,dy}{|x-y|},
\qquad
\mu_{B_0}=\lambda_0|B_0|,
\]

and write `n=floor(mu_B0)`, `theta=mu_B0-n`. The pair target fixes

\[
\mathbb E(N(B_0))_2=\lambda_0^2C_2J(B_0).
\]

Integer-valuedness gives the sharp fixed-mean lower bound

\[
\mathbb E(N)_2\ge n(n-1)+2n\theta,
\]

and hence

\[
C_2\ge
\frac{n(n-1)+2n\theta}{\lambda_0^2J(B_0)}.
\]

For the ball of radius `M/2`, with

\[
\mu=\frac{\pi\lambda_0M^3}{6},
\]

this becomes

\[
C_2\ge \frac{5M}{12}
\frac{n(n-1)+2n\theta}{\mu^2}.
\]

The bound is zero when `mu<1`. It is weaker than the Cox Jensen bound at low count because a general simple point process has a diagonal count contribution. More generally, for bounded real `f` whose support has diameter at most `M`, covariance positivity gives

\[
\lambda_0\int f^2
+\lambda_0^2C_2\iint\frac{f(x)f(y)}{|x-y|}\,dx\,dy
-\lambda_0^2\left(\int f\right)^2\ge0.
\]

These are genuine general necessary conditions, but they constrain a free output amplitude and therefore exclude no prescribed tuple.

## Criterion-by-criterion assessment

| Criterion | Evidence | Final assessment |
|---|---|---|
| Correct target and quantifiers | Frozen problem; all v02 scope statements | **Not met globally.** The low-intensity theorem is exact, but the universal `lambda_0>0` quantifier remains unresolved. |
| Whole-space existence and stationarity | Finite-cluster parent construction; Cox and Hawkes reductions | **Met for the restricted construction.** The witness is on all of `R^3`, stationary and in fact isotropic. |
| Simplicity, local finiteness, prescribed intensity | Diffuse marks and parents; bounded cluster size/range; exact intensity algebra | **Met for every certified low intensity.** No post hoc rescaling is used. |
| Local fourth moments and density existence | Local exponential moments; block-density partition formula | **Met for the restricted construction.** Stronger all-finite-order absolute continuity is proved. |
| Full density hierarchy and combinatorial factors | Two triangular inversions and complete `2,5,15` partition sums | **Met.** The exact positive theorem concerns full product densities. Cox and Hawkes tracks also retain all partitions. |
| Exact identities on entire physical domains | `S_2=D_2`, `D_3 subset S_3`, `S_4=D_4` | **Met for certified low intensities.** The pair identity includes arbitrarily small positive distances. |
| One jointly feasible parameter choice | Common amplitudes, positive cluster kernels and singleton correction | **Met only on the certified interval.** No reviewed choice works at every prescribed intensity. |
| Source support and prior-work comparison | Frozen dossier, manuscript sources and audits | **Adequate but bounded.** No published exact target theorem was located; this is not a novelty or openness certificate. |

## Comparison with the two prior local manuscripts

### Reciprocal simplex correlations from random spherical surfaces

The frozen spherical manuscript constructs a stationary isotropic Cox process directed by a Poisson population of spheres. Its parent intensity is `tau r dc dr` for `0<r<L`, and a sphere of radius `r` carries surface intensity `(beta/r) H^2`. Its point intensity is

\[
\rho=\frac{4\pi}{3}\tau\beta L^3.
\]

The checked common-sphere terms are

\[
q_2=\pi\tau\beta^2\frac{L^2-D^2/4}{D}\mathbf1_{D<2L},
\]

\[
q_3=\tau\beta^3\frac{\sqrt{L^2-R_3^2}}{A}\mathbf1_{R_3<L},
\]

\[
q_4=\frac{\tau\beta^4}{6V}\mathbf1_{R_4<L}.
\]

The full densities add all carrier partitions. Thus even the exact `1/V` common-sphere term is not the full fourth density. The manuscript's genuine theorem is that, on bounded resolved geometry domains and at an independently prescribed positive intensity, one process can approximate all three reciprocal laws uniformly to any prescribed relative tolerance. Its construction has strong regularity properties, including local exponential moments and finite-range dependence.

This is a valuable prescribed-intensity approximation theorem, but it is not an exact result at any finite tolerance parameter. The finite-`L` pair and triangle terms retain curvature factors, while the full moments retain positive multi-sphere terms. The supplied manuscript and audit contain no nondegenerate locally finite limiting Cox process that turns the tolerance into zero. The present rerun does not change that verdict. Approach 2 strengthens the negative comparison: arbitrary nonnegative radial mixing of uniformly weighted Poisson spheres can repair the exact pair law, but not the simultaneous full triangle law.

### Exact reciprocal simplex correlations on finite domains

The earlier finite-cluster manuscript is the direct ancestor of the new positive theorem. It constructs a stationary isotropic simple Poisson superposition of dependent clusters of sizes at most four. Its two triangular inversions already cancel every cross-parent partition exactly. On compatible domains

\[
0<\delta\le h\le H<\sqrt{\frac23}M,
\qquad M\le P,
\]

it gives exact full identities, but its pair law is only asserted on `delta<=D<=P`. Its amplitudes and intensity are tied by

\[
a_2=a,\qquad a_3=\frac{a}{4B},\qquad
a_4=\frac{a}{16BC},\qquad
\rho=aI,
\]

with `a` sufficiently small. Thus, for fixed compatible geometry, it already implies a sufficiently small intensity interval after translating amplitude into intensity, but it does not meet the governing no-cutoff domain and does not cover arbitrary prescribed intensity.

The rerun makes three substantive clarifications or extensions of that earlier result:

1. it proves that the locally integrable `1/D` singularity permits `delta=0` without a limiting argument;
2. it uses the enlarged internal triangle threshold `min(h_3,h_4)` so that fourth-order face cancellation is valid for either ordering of the target thresholds; and
3. it solves explicitly for the prescribed low intensity and records a closed certified endpoint.

The prior manuscript's mathematical transcription audit had found three local presentation defects: insufficient hypotheses in the flattening proposition, confusion between the marked Poisson intensity density `F_j/j!` and the conditional mark probability density `F_j/Z_j`, and a false unqualified statement of global integrability for translation-invariant kernels. Its repair addendum records all three as corrected. Those repairs preserve the earlier restricted theorem; they do not supply the missing no-cutoff or arbitrary-intensity conclusions by themselves.

The two manuscripts therefore occupy complementary but distinct positions:

| Manuscript | Exactness | Intensity | Pair domain | Final relevance |
|---|---|---|---|---|
| Spherical Cox | Arbitrarily accurate relative approximation, not equality | Independently prescribed | Includes the required small-distance range in the approximation theorem | Shows prescribed intensity and reciprocal carrier Jacobians are compatible approximately; no exact witness |
| Finite dependent clusters | Exact full identities | Sufficiently small, coupled through amplitudes | Positive cutoff `delta>0` in the manuscript | Supplies the exact cancellation mechanism; the rerun removes the cutoff and states the low prescribed-intensity interval explicitly |

Neither prior local manuscript is a published theorem, and neither alone establishes the governing target.

## Literature and source verdict

The frozen literature search located no source proving the complete governing target. This is a bounded non-discovery statement, not a novelty claim and not a certificate that the problem is open in the entire literature.

The historical earthquake sources support the interpretation in terms of conditional or full factorial moments, not connected cumulants. Kagan's empirical pair, triangle and tetrahedron relations are approximate finite-catalogue statements. Daley and Vere-Jones explicitly formulate the compatibility question using factorial moment densities. None supplies the present exact construction or universal quantifiers.

The following structural source uses were adequately supported in the frozen dossier.

- Last and Penrose support stationary Poisson-cluster and Cox identities, including `alpha_X^(n)=E Lambda^otimes n`.
- Clark and Houssineau support the complete partition formula for dependent clusters.
- Moller, Syversveen and Waagepetersen support the LGCP product hierarchy.
- Jovanovic, Hertz and Rotter support Hawkes cumulant trees and the separate moment-cumulant conversion.
- Kuna, Lebowitz and Speer give pair and limited triplet realizability results, not a simultaneous order-four inverse theorem for the present target.
- Gibbs existence and cluster-expansion theorems show that geometric interactions can define processes; they do not invert the correlation hierarchy to the required exact `1/D,1/A,1/V` full densities.
- Soshnikov's determinantal formula gives the reviewed Hermitian DPP exclusion.

Sources available only at metadata or partial-text level were not used for delicate theorem hypotheses. No literature result was promoted beyond its verified scope.

## Detailed findings and complete repair register

The table entries below preserve every identified initial-review finding and every named delta-review finding. “Closed” means closed as an author-repair item; it does not mean that the broader mathematical target became solved.

### Approach 1 register

| Finding | Initial assessment | Delta disposition / synthesis status |
|---|---|---|
| A1-v01-F1 | Governing arbitrary-intensity quantifier unresolved | **Closed as a scope repair; mathematical gap remains.** V02 consistently restricts existence to `0<lambda_0<=lambda_cert`; all larger intensities remain unresolved. |
| A1-v01-F2 | Fixed-bounded-cluster obstruction only | **Closed.** Proposition remains restricted to one fixed a.s. cluster-size bound and is not extended to unbounded clusters or general processes. |
| A1-v01-F3 | Endpoint inclusion needed justification | **Closed.** Continuity, monotonicity, a positive neighbourhood of zero and divergence of `E_2` make the feasible set a compact interval with attained endpoint. |
| A1-v01-F4 | Re-rooting and ordered-assignment coefficient compressed | **Closed.** V02 proves full symmetry, translation invariance, determinant-one re-rooting and the `(j)_r` count. |
| A1-v01-F5 | All-orders absolute continuity stronger than required | **Verified; no repair.** Same-parent blocks have size at most four and densities; finite partition sums give every finite order. |
| A1-v01-F6 | Whole-space process properties | **Verified; no repair.** Bounded cluster range and size give local exponential moments; diffuse laws give simplicity. |
| A1-v01-F7 | Auxiliary altitude support | **Verified; no repair.** Enlarged `S_3` strengthens the triangle identity and adds no target condition to `D_4`. |
| A1-v01-F8 | Geometric and amplitude constants | **Verified; no repair.** Marginal constants and all order-four partition coefficients check. |
| A1-v01-F9 | Source support | **Verified; no repair.** Published sources support structure; local manuscripts are identified as unpublished. |
| A1 v02 new findings | Delta review found no new defect | **None.** No further repair round requested. |

### Approach 2 register

| Finding | Initial assessment | Delta disposition / synthesis status |
|---|---|---|
| R2-V01-01 / R2-V02-01 | General Cox existence unresolved | **Closed as a scope repair; mathematical gap remains.** No general directing measure or general Cox obstruction was found. |
| R2-V01-02 | Radial Poisson-sphere pair/triangle obstruction correct | **Verified and preserved.** It remains confined to Poisson-centred, radius-only uniform sphere weights. |
| R2-V01-03 / R2-V02-02 | Incidence and absolute-continuity passage too compressed | **Closed.** Lemma 2 supplies measurable weights, orthogonal fibres, Jacobian, local finiteness, a.e. interpretation and the order-four version convention. |
| R2-V01-04 / R2-V02-03 | Cox “equivalence” proved only forward | **Closed.** V02 proves stationarity of the directing law, diffuseness, fourth mass moments and tensor-density recovery in the reverse direction. |
| R2-V01-05 / R2-V02-04 | Pair-only radial repair needed explicit `L` and tail | **Closed.** V02 gives `L>M/2` when needed and an explicit nonnegative integrable tail. |
| R2-V01-06 | Finite-pointwise-second-moment and LGCP obstructions | **Verified and preserved.** They are not extended to irregular fields with infinite pointwise second moment. |
| R2-V01-07 | Particular finite-cluster witness is not Cox | **Verified and preserved.** The conclusion concerns that law, not all laws with the same low-order moments. |
| R2-V01-08 | General Cox moment tests non-decisive; window wording too broad | **Closed as wording; mathematical limitation remains.** V02 uses positive-measure bounded windows and still draws no non-existence conclusion. |
| R2-V01-09 | No fourth-order generalisation from sphere obstruction | **Verified and preserved.** Failure at pair/triangle level excludes the subclass but says nothing general about Cox fourth moments. |
| R2-V02-05 | Repaired finite-cluster window test | **Closed verification finding.** One explicitly nontrivial bounded window suffices. |
| R2 v02 new defects | Delta review found none | **None.** The standing headline is the unresolved general Cox moment problem. |

### Approach 3 register

| Finding | Initial assessment | Delta disposition / synthesis status |
|---|---|---|
| H3-v01-F01 / H3-v02-C02 | Governing target unresolved outside regular scalar Hawkes class | **Closed as a scope repair; mathematical gap remains.** Singular, marked, multitype, carrier, nonlinear and critical cases remain open. |
| H3-v01-F02 | Local fourth-moment proof compressed | **Closed.** V02 proves an exponential progeny moment and applies the marked-Poisson cumulant formula with the translation integral bound. |
| H3-v01-F03 | Fixed-root measure to density passage compressed | **Closed.** V02 keeps Dirac terms at measure level until immigrant integration removes them and uses Tonelli for spatial pushforwards. |
| H3-v01-F04 | Residual equations needed a.e. and face-domain qualifiers | **Closed.** V02 uses compatible versions and restricts face substitution to the appropriate intersection. |
| H3-v01-F05 / H3-v02-C01 | Bounded-kernel Hawkes obstruction sound | **Verified and preserved.** It is an exact negative theorem for the stated $L^1\cap L^\infty$ scalar subcritical class. |
| H3-v01-F06 | Full products and tetrahedral-face scope correct | **Verified and preserved.** All partitions are present; no hidden face condition is introduced. |
| H3-v02-C03 | Source verification intentionally bounded | **Recorded.** The dossier supports the structural claims; the delta review is not a fresh primary-source audit of every citation. |
| H3 v02 new defects | Delta review found none | **None.** No further author repair round requested. |

### Approach 4 register

| Finding | Initial assessment | Delta disposition / synthesis status |
|---|---|---|
| A4-V01-01 | Arbitrary-intensity target unresolved | **Closed as a scope repair; mathematical gap remains.** V02 states the certified interval throughout. |
| A4-V01-02 | Bounded-cluster obstruction should use a reduced measure | **Closed.** V02 assumes no global same-parent density and invokes a density only on the target ball. |
| A4-V01-03 | Provenance of prescribed-low-intensity reformulation overstated | **Closed.** V02 describes changes and explicit reformulations within the earlier unpublished framework. |
| A4-V01-04 | Reanchoring step implicit | **Closed.** Determinant-one reanchoring, symmetry and the exact assignment count now precede the density formula. |
| A4 v01 unnumbered verification checks | No-cutoff integrability, face support, kernel positivity, exact intensity, full partitions and obstruction scope were tested for possible failure | **Verified with no adverse finding.** These checks support the restricted theorem but do not enlarge its intensity range. |
| A4 v02 new findings | Delta review found none | **None.** The remaining issue is new research on high intensity, not repair. |

### Approach 5 register

| Finding | Initial assessment | Delta disposition / synthesis status |
|---|---|---|
| A5-v01-01 | Arbitrary prescribed intensity unresolved | **Closed as a scope repair; mathematical gap remains.** V02 leaves both existence and non-existence above `lambda_*` open. |
| A5-v01-02 | `delta=0` endpoint extension | **Verified; no repair.** `1/D` and every required marginal remain integrable. |
| A5-v01-03 | Non-nested target domains | **Verified; no repair.** Internal `S_3` handles faces without changing the governing domains. |
| A5-v01-04 | Full partitions and multiplicities | **Verified; no repair.** The `1/(j-r)!` factors and all `2,5,15` partitions are correct. |
| A5-v01-05 | Prescribed intensity and process regularity | **Verified; no repair.** The singleton correction, local moments, simplicity and density existence check. |
| A5-v01-06 | Yamada and covariance necessities | **Verified; no repair.** They are general but non-obstructive because `C_2` is free. |
| A5-v01-07 | Null windows made the quotient undefined | **Closed.** V02 restricts to positive-measure Borel windows and proves $0<J(B_0)<\infty$. |
| A5-v01-08 | “Rules out non-existence” wording ambiguous | **Closed.** V02 says only that at least some intensities admit solutions and leaves the rest open. |
| A5-v01-09 | Prior audits were presented too much like theorem support | **Closed.** Exact manuscript locators were added, audits were demoted to historical records, and the proof remains self-contained. |
| A5 v02 new findings | Delta review found none | **None.** No further scoped repair round requested. |

### Cross-approach finding

The low-intensity theorem appears in approaches 1, 4 and 5 with essentially identical kernels, marginal estimates and process law. Their agreement and separate reviews increase confidence in the shared derivation, but they do not give three distinct solutions or any additional intensity range. The strongest synthesis combines approach 1's attained endpoint, approach 4's explicit conservative certificate and measure-form obstruction, and approach 5's general count inequalities.

## Coder and source verification

No coder request was made. Each of the five individual reviewers explicitly found no useful specific numerical check to dispatch. Accordingly, there are no coder artefacts, coding requests, simulation reruns or numerical certificates in this run, and this synthesis does not claim any.

The decisive checks are exact analytic ones: the `1/D` anchored integral, the cylindrical and height-slice marginals, the finite set-partition coefficients, determinant-one reanchoring, intensity cancellation, the ball overlap integral, the integer-count inequality, Cox tensor scaling, the spherical fixed-circumradius contradiction, the mixed-Poisson window contradiction, and the Hawkes resolvent bound. Floating-point agreement would not strengthen these continuum conclusions.

Source assessment used only the frozen dossier and the listed manuscript materials. The dossier distinguishes fully checked primary sources from metadata-only sources. No fresh web search was performed at synthesis, and no unlisted source was used to change a verdict.

## Review reasoning summary

The synthesis rests on the following auditable tests.

1. **Quantifier test.** Every claimed theorem was compared with the order `for every admissible geometry, for every prescribed lambda_0>0`. Only a closed interval starting at zero is proved. This alone prevents a favourable governing-target verdict.
2. **Domain test.** The pair law includes every `0<D<=M`; the triangle and tetrahedron domains use absolute altitude cutoffs; no triangle threshold is imposed on tetrahedral faces. The positive construction uses a larger internal triangle support rather than shrinking the target.
3. **Full-density test.** The positive construction, Cox carrier expansion and Hawkes hierarchy each include all `2,5,15` set partitions. Same-parent kernels and factorial cumulants are never substituted directly for `rho^(n)`.
4. **No-cutoff test.** `1/D` is locally integrable in three dimensions, and the exact marginal estimates remain proportional to the lower-order reciprocal kernels. This validates removal of the earlier `delta>0` cutoff.
5. **Kernel-positivity test.** Every lower partition at orders two through four is included in the residuals. The explicit error bounds imply nonnegative same-parent kernels, and the marginal inversion gives nonnegative exact-size cluster densities.
6. **Process-law test.** Parent rates, mark normalisation, reanchoring, singleton correction, local exponential moments, simplicity and factorial-density existence were checked before accepting the restricted theorem.
7. **Intensity test.** The finite-cluster intensity equals the prescribed input throughout the certified interval. Above the interval there is neither a construction nor a general obstruction. Cox mass scaling would solve intensity only after the missing exact directing measure is constructed.
8. **Subclass-boundary test.** Every negative result was traced to the hypothesis that makes it work: fixed cluster-size cap, Poisson uniform spheres, finite pointwise second moment, Hermitian determinantal structure, or essentially bounded Hawkes kernel. None was generalised beyond that class.
9. **Excluded-shape test.** Moment and covariance arguments were not allowed to fill low-altitude triangles, flat tetrahedra or separations beyond `M` with reciprocal formulas. This prevents spurious non-existence proofs.
10. **Prior-work test.** The spherical manuscript is approximate at prescribed intensity; the earlier finite-cluster manuscript is exact on a smaller domain and low intensity. Neither title or old audit verdict was treated as a solution of the frozen target.
11. **Evidence test.** No simulation, empirical catalogue scatter or finite grid was allowed to replace an exact continuum proof. Literature non-discovery was kept distinct from novelty or openness.

This is a structured account of the decisive checks and dependencies, not raw private chain-of-thought or a formal proof certificate.

## Decision record

| Decision | Final outcome | Basis |
|---|---|---|
| Does the rerun establish the exact target for every prescribed `lambda_0>0`? | **No** | All exact constructions stop at a finite certified low-intensity endpoint. |
| Does it establish exact existence for any nonempty intensity range? | **Yes** | The reviewed finite-cluster theorem covers every prescribed intensity in a closed nonempty interval starting at zero, with no pair cutoff and full `g_2,g_3,g_4`. |
| Is the restricted result merely approximate or numerical? | **No** | It is an exact analytic continuum construction with nonnegative cluster laws and complete partition cancellation. |
| Is general non-existence proved above the endpoint? | **No** | All obstructions are class-specific or constrain free amplitudes only. |
| Can the current size-at-most-four Poisson-cluster architecture cover all intensities? | **No** | The fixed-`K` pair-mass obstruction gives a finite intensity ceiling at fixed `M`. |
| Is prescribed intensity automatic in the Cox class? | **Conditionally yes** | Deterministic scaling works once one exact positive-intensity directing measure exists; no such general witness is known here. |
| Do the prior manuscripts settle the target? | **No** | One is approximate at prescribed intensity; the other is exact on a cutoff domain and at low intensity. |
| Was any coder or simulation evidence used? | **No** | All five reviewers found no useful specific numerical check; no coder was dispatched. |
| Is another prose-repair round needed for any v02 submission? | **No** | All assigned v01 repair items are closed and no delta review found a new actionable defect. |
| What remains? | **New mathematics, not wording repair** | Extend exact existence to arbitrary intensity or prove a valid general obstruction on only the frozen domains. |

## Remaining mathematical questions and proof obligations

### Highest-priority exact obligations

1. **Close the arbitrary-intensity quantifier.** For each admissible fixed `(M,h_3,h_4)` and each `lambda_0>lambda_cert`, either construct a process with all three exact full identities or prove non-existence for a clearly quantified class broad enough to answer the governing question. Improving prose or rerunning the same smallness estimate is not enough.

2. **Go beyond a fixed cluster-size cap.** The pair-mass obstruction shows that no one fixed `K` works at all intensities. A plausible next route is an inverse-cluster construction whose maximum or typical cluster size grows with `lambda_0 M^3`, or an unbounded but almost surely finite cluster law. It must retain finite local fourth moments, genuine nonnegative cluster probabilities, marginal consistency and the complete full-density partition identities.

3. **Determine whether the certified endpoint is only an artefact of coarse positivity bounds.** The current `E_j<=1/2` conditions are sufficient. One should either construct sharper residual kernels or prove an intrinsic positivity ceiling for this particular downward-inversion family. This would clarify the construction even if it did not settle general realizability.

4. **Construct an exact Cox directing measure, or obstruct all such measures.** One exact witness at any positive intensity would solve prescribed intensity by deterministic mass scaling. The measure must be stationary, diffuse and locally finite, have finite fourth local mass moments and absolutely continuous tensor moments, and satisfy all three full moment identities. Uniform sphere mixtures, finite-pointwise-second-moment fields and ordinary LGCPs have been excluded, but dependent carriers, nonuniform or non-spherical singular carriers, permanental-type models and irregular density fields remain candidates.

5. **Test whether the finite-cluster cancellation can be embedded in a different Cox law.** The particular finite-cluster process is not Cox, but low-order moment equivalence with another Cox law is not excluded. A successful embedding would combine exact residual cancellation with Cox intensity scaling; a rigorous moment or infinite-divisibility obstruction could close this bridge.

6. **Enlarge the Hawkes analysis beyond bounded triggering densities.** A candidate must specify the spatialisation, prove stationarity and finite fourth moments, retain absolute continuity after projection, and realise the nonnegative residual cumulants with one causal subcritical genealogy. Matching only the pair resolvent or a single tree topology is insufficient.

7. **Develop mixed realizability inequalities confined to the prescribed domains.** Useful tests must couple `C_2,C_3,C_4` without assigning reciprocal values to low-altitude or overly large configurations. At fourth order they must keep the four face values of the third cumulant free whenever a target tetrahedron face lies outside `D_3`.

8. **Locate or prove a four-order inverse theorem.** The checked realizability literature treats pairs and limited third-order information but does not provide a ready theorem for simultaneous full densities through order four with the present singularities, finite domains, positivity and arbitrary intensity.

### Source and status obligations

Any later claim that the governing problem is solved, impossible, novel or open must compare exact hypotheses and quantifiers with primary sources. The present literature dossier supports only a bounded non-discovery statement. Hawkes--Oakes, general shot-noise Cox and line-carrier sources that were not checked at theorem level should be retrieved only for a concrete formula or hypothesis.

### Optional empirical work, kept separate

Empirical earthquake comparison is not part of the acceptance criterion. If pursued, it needs an explicit catalogue selection rule, spatial observation mask, time window, location-error model and reference process. Published-summary scatter is not a confidence band for `g_n`; catalogue-normalised ratios are not automatically ensemble product densities; and a simulation match cannot repair an exact existence gap. The earlier spherical and finite-cluster simulations remain model diagnostics, not proof of the governing identities.

## Final conclusion

The rerun materially improves the mathematical position. It gives a reviewed exact continuum construction for all three **full** reciprocal-simplex product densities on the complete finite physical domains, with no lower pair cutoff, at every prescribed intensity in a nonempty geometry-dependent low-intensity interval. It also identifies several precise class obstructions and general necessary inequalities.

The governing theorem is nevertheless **unresolved**. No reviewed argument covers every prescribed positive intensity, and no reviewed obstruction rules out all eligible stationary simple point processes above the certified interval. The next step is new mathematics on the intensity gap—most plausibly growing or unbounded clusters, an exact Cox directing measure, or domain-faithful mixed realizability inequalities—not another approximation, simulation or wording repair.
