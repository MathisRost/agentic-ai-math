# Approach 4 — submission v02

- Run / model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem snapshot SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Context packet and source dossier version: `context_packets/proof_4_v02.md`, SHA-256 `2dfca561d7fd7cc4aa14f63a5d7fe4395b0a3295f3d59c4a8a9355119dbbf27d`; `shared_literature/dossier.md`, dated 19 October 2026, SHA-256 `5d42ad11b6b55246e6a0eb098b3f09c1bf3751cd3add4a819f5e427017b659f5`.
- Claim status: **restricted theorem and scoped obstruction**. The theorem removes the positive pair-distance cutoff and realises every sufficiently small *prescribed* intensity, with exact full identities on all three governing domains. It does not cover arbitrary prescribed intensity. The obstruction shows that no Poisson-cluster construction with one fixed finite upper bound on cluster size can cover arbitrarily large intensities at fixed $M$.

## Claim and scope

Let $M,h_3,h_4>0$, and assume that the triangle and tetrahedron domains in the frozen problem statement have positive Lebesgue measure. There is a constant

\[
 \lambda_*(M,h_4)>0
\]

such that, for every prescribed intensity

\[
 0<\lambda_0\leq \lambda_*(M,h_4),
\]

there is one stationary, isotropic, simple, locally finite point process $X$ on all of $\mathbb R^3$, of intensity exactly $\lambda_0$, with finite local exponential moments and absolutely continuous factorial moment measures through order four, for which positive constants $C_2,C_3,C_4$ satisfy

\[
 g_2(x_1,x_2)=\frac{C_2}{D},\qquad
 g_3(x_1,x_2,x_3)=\frac{C_3}{A},\qquad
 g_4(x_1,x_2,x_3,x_4)=\frac{C_4}{V}
\]

Lebesgue-almost everywhere on the complete governing domains $\mathcal D_2,\mathcal D_3,\mathcal D_4$. In particular, the pair identity holds for every separation range $0<D\leq M$; no positive lower cutoff is imposed.

This establishes the exact target for a nonempty interval of prescribed intensities, not for every $\lambda_0>0$. The process and amplitudes depend on $(\lambda_0,M,h_3,h_4)$, as the governing problem permits.

There is also the following class-specific limitation. Under the standard independently marked homogeneous Poisson-parent definition of a stationary Poisson-cluster process, suppose that clusters have size at most $K<\infty$ almost surely, possibly with an additional independent homogeneous Poisson singleton process. If the exact pair identity holds on $0<D\leq M$, then necessarily

\[
 \lambda_0M^3\leq \frac{3(K-1)}{2\pi}. \tag{O}
\]

For the clusters of size at most four used below this becomes $\lambda_0M^3\leq9/(2\pi)$. This is not a non-existence result for general point processes, Cox processes, or Poisson-cluster processes whose cluster-size bound may grow with the requested intensity.

## Relation to prior work

The frozen local manuscript `common/prior_work/finite-cluster-reciprocal-laws/` proves an exact dependent-cluster theorem with clusters of sizes at most four. Its `sections/construction.tex`, `sections/appendix_bounds.tex` and `sections/appendix_partitions.tex` provide, respectively, the inverse cumulant construction, the positivity estimates and the complete parent-partition calculation. Its theorem has two mismatches with the present target: it assumes a lower pair cutoff $\delta>0$, and its intensity is coupled to the small amplitude parameter.

The present proof reuses that inverse-cluster mechanism and makes the following changes and explicit reformulations.

1. It sets the pair support to the whole punctured ball $0<D\leq M$. This is legitimate because $1/D$ is locally integrable in three dimensions. The resulting pair-cluster density is unbounded near the diagonal but has a finite anchored integral and no atom at the diagonal.
2. It sets the auxiliary triangle altitude threshold to $h=\min\{h_3,h_4\}$. This may enlarge the support on which the construction is exact, but it ensures that every face of a target tetrahedron belongs to the triangle support even when $h_4<h_3$. The required triangle identity still holds on the original, smaller domain with threshold $h_3$.
3. It treats $\lambda_0$ as the prescribed input and records a closed-form positive interval on which all residual kernels remain nonnegative. For fixed domains, the prior theorem's polynomial smallness condition in its amplitude already implied a sufficiently small prescribed-intensity interval after writing the amplitude in terms of the intensity. The interval below is an explicit reformulation and re-derivation of that implication for the zero-cutoff supports, not a claim of a new intensity mechanism.

The frozen spherical Cox manuscript `common/prior_work/reciprocal-simplex/`, especially Sections 3--5, supplies prescribed intensity and the correct full partition formulas, but only an arbitrarily accurate approximation. Its finite-radius pair and triangle terms retain curvature factors, and its full moments retain positive multi-sphere partitions. No exact limiting Cox directing measure is proved there.

The bounded literature dossier records that deterministic scaling of a Cox directing measure would preserve all normalised $g_n$ while changing intensity. That observation makes an exact Cox witness attractive, but the inspected material contains no random measure with the three required exact full moments. The present construction was selected because its exact cancellation can be proved directly.

No novelty claim is made. The two local manuscripts are unpublished sources. The zero-cutoff adaptation and the explicit formulas below are proved here, but their provenance is the finite-cluster framework just described.

## Process and existence

We give the construction first and prove all its properties below.

### 1. Supports and geometric constants

Write $\rho=\lambda_0$ and

\[
 h=\min\{h_3,h_4\},\qquad H=h_4.
\]

Define the nested supports

\[
\begin{aligned}
 S_2&=\{(x_1,x_2):0<|x_2-x_1|\leq M\},\\
 S_3&=\{(x_1,x_2,x_3):A>0,\ \operatorname{diam}\{x_i\}\leq M,
       \ h_{\min}\geq h\},\\
 S_4&=\{(x_1,x_2,x_3,x_4):V>0,\ \operatorname{diam}\{x_i\}\leq M,
       \ H_{\min}\geq H\}.
\end{aligned}
\]

Thus $S_2=\mathcal D_2$, $\mathcal D_3\subseteq S_3$, and $S_4=\mathcal D_4$. Every edge of a supported triangle lies in $S_2$. Every face of a supported tetrahedron lies in $S_3$: for a vertex of a face, its distance to the opposite edge line is at least its distance to the tetrahedral face plane containing that line, hence at least $H\geq h$.

Set

\[
 K_2=\frac{\mathbf1_{S_2}}{D},\qquad
 K_3=\frac{\mathbf1_{S_3}}{A},\qquad
 K_4=\frac{\mathbf1_{S_4}}{V},
\]

with arbitrary values on the null degenerate sets. Put

\[
\begin{aligned}
 I&=2\pi M^2,& L&=\frac{4\pi}{3}M^3,\\
 B&=2\pi^2M^2,&
 J&=6\pi\left[M^2\log(M/H)-\frac{M^2-H^2}{2}\right].
\end{aligned}
\]

The positive-measure assumption on $\mathcal D_4$ implies $0<H<M$. Writing $r=H/M$, the inequality $-\log r>(1-r^2)/2$ for $0<r<1$ shows that $J>0$. The anchored pair integrals are

\[
 \int_{\mathbb R^3}K_2(0,y)\,dy=I,
 \qquad
 \int_{\mathbb R^3}\mathbf1_{S_2}(0,y)\,dy=L.
\]

For a symmetric translation-invariant $r$-point kernel $f$, let

\[
 (\mathcal Mf)(x_1,\ldots,x_{r-1})
 =\int_{\mathbb R^3}f(x_1,\ldots,x_{r-1},z)\,dz.
\]

The geometric marginal estimates are

\[
 \mathcal MK_3\leq BK_2,
 \qquad
 \mathcal MK_4\leq JK_3. \tag{1}
\]

For the first inequality, fix a pair of length $d>0$ and write $r$ for distance to its affine line. Since $A=dr/2$, cylindrical coordinates in a radius-$M$ ball give

\[
 \int_{B(0,M)}\frac{dz}{r}
 =4\pi\int_0^M\sqrt{M^2-r^2}\,dr=\pi^2M^2.
\]

Hence the marginal is at most $2\pi^2M^2/d=B/D$. There is no divergence at $d=0$ in the anchored pair integral because

\[
 4\pi\int_0^M\frac{r^2}{r}\,dr=2\pi M^2<\infty.
\]

For the second inequality, fix a triangle of area $A$, and let $u$ be signed height of the omitted vertex above its plane. A supported tetrahedron has $H\leq|u|\leq M$, $V=A|u|/3$, and an in-plane section of area at most $\pi(M^2-u^2)$. Therefore

\[
 \mathcal MK_4
 \leq\frac{6\pi}{A}\int_H^M\frac{M^2-u^2}{u}\,du
 =\frac{J}{A}.
\]

Outside the right-hand supports in (1), the left-hand marginals vanish by the nesting just proved.

### 2. An explicit low-intensity interval

Choose

\[
 a_2=\frac{\rho}{I},\qquad
 a_3=\frac{a_2}{4B},\qquad
 a_4=\frac{a_2}{16BJ}. \tag{2}
\]

Define

\[
\begin{aligned}
 E_2(\rho)&=IM\rho,\\
 E_3(\rho)&=6BM\rho+2BIM^2\rho^2,\\
 E_4(\rho)&=\frac83IBJM^3\rho^3+16BJM^2\rho^2
             +\frac{8BJM}{I}\rho+\frac{16JM}{3}\rho.
\end{aligned} \tag{3}
\]

Each is increasing on $[0,\infty)$ and vanishes at zero. One completely explicit sufficient threshold is

\[
\begin{aligned}
\lambda_*:=\min\Bigg\{
 &(2IM)^{-1},\ (24BM)^{-1},\ (8BIM^2)^{-1/2},\\
 &\left(\frac{3}{64IBJM^3}\right)^{1/3},\
 (128BJM^2)^{-1/2},\ \frac{I}{64BJM},\ \frac{3}{128JM}
\Bigg\}. \tag{4}
\end{aligned}
\]

Indeed, the first entry makes $E_2\leq1/2$, the next two make the two terms of $E_3$ at most $1/4$, and the last four make the four terms of $E_4$ at most $1/8$. Thus

\[
 E_2,E_3,E_4\leq\frac12
 \quad\text{whenever}\quad 0<\rho\leq\lambda_*. \tag{5}
\]

All quantities in (4) have physical units of intensity, $\mathrm{length}^{-3}$.

### 3. Same-parent and exact-size cluster kernels

For configurations abbreviated by their labels, define recursively

\[
 q_2(12)=\mathbf1_{S_2}(12)
 \left(\frac{a_2}{D(12)}-\rho^2\right), \tag{6}
\]

\[
 q_3(123)=\mathbf1_{S_3}(123)
 \left(\frac{a_3}{A(123)}-\rho^3
       -\rho\sum_{1\leq i<j\leq3}q_2(ij)\right), \tag{7}
\]

and

\[
\begin{aligned}
q_4(1234)=\mathbf1_{S_4}(1234)\Bigg(&\frac{a_4}{V(1234)}-\rho^4
 -\rho^2\sum_{1\leq i<j\leq4}q_2(ij)\\
&-\{q_2(12)q_2(34)+q_2(13)q_2(24)+q_2(14)q_2(23)\}\\
&-\rho\{q_3(123)+q_3(124)+q_3(134)+q_3(234)\}\Bigg).
\end{aligned} \tag{8}
\]

The kernels $q_r$ are intended to be the complete same-parent ordered densities, equivalently the factorial-cumulant densities of the eventual Poisson-cluster process. They are not yet cluster probability densities. Define the exact-size cluster kernels by downward marginal inversion:

\[
 F_4=q_4,\qquad
 F_3=q_3-\mathcal Mq_4,\qquad
 F_2=q_2-\mathcal Mq_3+\frac12\mathcal M^2q_4. \tag{9}
\]

All $q_r$ and $F_r$ are symmetric under permutations of their arguments and invariant under a common translation. Both properties follow first from the geometric kernels and then recursively from (6)--(9).

### 4. Positivity and normalisation

The relative subtractions in (6)--(8) are bounded by (3). For (6),

\[
 \frac{\rho^2D}{a_2}\leq\frac{\rho^2M}{a_2}=E_2.
\]

For a triangle of diameter at most $M$, $A\leq M^2/2$ and $A/D_{ij}\leq M/2$. Using $q_2\leq a_2K_2$, the relative subtraction in (7) is at most $E_3$. For a tetrahedron of diameter at most $M$,

\[
 V\leq\frac{M^3}{6},\qquad
 \frac{V}{D_{ij}}\leq\frac{M^2}{6},\qquad
 \frac{V}{D_{ij}D_{k\ell}}\leq\frac M6,
 \qquad
 \frac{V}{A_{ijk}}\leq\frac M3. \tag{10}
\]

The middle bound with two denominators concerns opposite edges. Counting the six edges, three pairings and four faces in (8) gives $E_4$. Consequently (5) implies

\[
 \frac12a_rK_r\leq q_r\leq a_rK_r,
 \qquad r=2,3,4. \tag{11}
\]

Combining (1), (2), (9) and (11) gives

\[
 F_4\geq\frac12a_4K_4,
\]

\[
 F_3\geq\left(\frac{a_3}{2}-a_4J\right)K_3
 =\frac14a_3K_3,
\]

and

\[
 F_2\geq\left(\frac{a_2}{2}-a_3B\right)K_2
 =\frac14a_2K_2. \tag{12}
\]

Thus the $F_r$ are nonnegative, locally integrable and have finite positive anchored integrals

\[
 Z_r=\int F_r(0,y_2,\ldots,y_r)\,dy_2\cdots dy_r,
 \qquad r=2,3,4. \tag{13}
\]

Finiteness follows from (1), bounded supports, local integrability of $1/D$, and the positive altitude cutoff for $K_4$. Positivity follows from (12) and the assumed positive measure of the target domains.

### 5. Reanchoring and the whole-space process

Before defining the clusters, we record why an anchored density in (13) gives the required symmetric cluster law. For any $r\geq2$ and any proposed anchor $i\in\{2,\ldots,r\}$, changing relative coordinates from anchor $1$ to anchor $i$ has the form

\[
 (y_2,\ldots,y_r)
 \longmapsto
 (-y_i,\,y_2-y_i,\ldots,y_{i-1}-y_i,
   y_{i+1}-y_i,\ldots,y_r-y_i), \tag{14}
\]

up to a permutation of the output coordinates. Subtracting $y_i$ from the other coordinate blocks and replacing the $y_i$ block by $-y_i$ are elementary block operations; their scalar coefficient matrix has determinant $\pm1$, and tensoring with the $3\times3$ identity preserves absolute determinant one. The map is invertible, with inverse given by reanchoring at the original first point. Translation invariance and full symmetry of $F_r$ therefore give

\[
 F_r(0,y_2,\ldots,y_r)
 =F_r\!\left(0,-y_i,(y_k-y_i)_{k\in\{2,\ldots,r\}\setminus\{i\}}\right), \tag{15}
\]

with the arguments placed in the corresponding order. Thus the anchored integral $Z_r$ and the induced unlabelled cluster law do not depend on which daughter is chosen as anchor. Equations (14)--(15) also justify every later marginal and assignment count; no hidden Jacobian or preferred-daughter factor remains.

For each $r=2,3,4$, take an independent homogeneous Poisson process of type-$r$ parents of rate $Z_r/r!$. A parent at $z$ receives, independently of all parents and other marks, a labelled relative mark $(Y_2,\ldots,Y_r)$ with probability density $F_r(0,\cdot)/Z_r$, and emits the unlabelled cluster

\[
 \{z,z+Y_2,\ldots,z+Y_r\}.
\]

Add an independent homogeneous singleton Poisson process of rate

\[
 \lambda_1=\rho^2L+\frac{Z_3}{2}+\frac{Z_4}{3}>0. \tag{16}
\]

Let $X$ be the superposition of all emitted points.

Every cluster contains at most four points and all offsets have norm at most $M$. Hence only finitely many parents can affect a bounded window, and the window count is bounded by a compound Poisson variable with jumps at most four plus an independent Poisson count. It has a finite exponential moment for every finite positive argument. This proves local finiteness and, in particular, finite local moments through order four.

The joint offset laws have Lebesgue densities. They give no mass to coincidences within a cluster, while independent diffuse parent locations and marks give no collisions between clusters. Thus $X$ is simple. Translation invariance of the parent processes gives stationarity, and the distance/area/volume supports are invariant under orthogonal transformations, so $X$ is isotropic.

It remains to verify the intensity. Put

\[
 Q_r=\int q_r(0,y_2,\ldots,y_r)\,dy_2\cdots dy_r.
\]

Integrating (9), with the unit-Jacobian reanchoring above, yields

\[
 Z_4=Q_4,\qquad Z_3=Q_3-Q_4,\qquad
 Z_2=Q_2-Q_3+\frac12Q_4. \tag{17}
\]

The nonsingleton point intensity is therefore

\[
 Z_2+\frac{Z_3}{2}+\frac{Z_4}{6}
 =Q_2-\frac{Q_3}{2}+\frac{Q_4}{6}.
\]

Equation (16) contributes $\rho^2L+Q_3/2-Q_4/6$. Finally, (6) and (2) give

\[
 Q_2=a_2I-\rho^2L=\rho-\rho^2L.
\]

The total intensity is consequently

\[
 Q_2+\rho^2L=\rho=\lambda_0, \tag{18}
\]

the prescribed input.

The same construction gives absolutely continuous factorial moment measures at every finite order. A same-parent block can have size at most four and has a Lebesgue density obtained by marginalising one of the $F_r$. Every full ordered factorial measure is a finite sum over set partitions into such blocks, and each term is a product of their densities.

## Full product-density calculation

We now derive the complete ordered densities through order four. This also proves that the construction concerns the full $g_r$, not merely connected or same-parent terms.

Consider first the full labelled daughter tuple $(w_1,\ldots,w_j)$ of a type-$j$ cluster. The change of variables

\[
 (z,y_2,\ldots,y_j)\longmapsto
 (w_1,\ldots,w_j)=(z,z+y_2,\ldots,z+y_j)
\]

has absolute determinant one. The parent rate and mark density therefore give this labelled full tuple the intensity density

\[
 \frac{Z_j}{j!}\frac{F_j(0,w_2-w_1,\ldots,w_j-w_1)}{Z_j}
 =\frac{1}{j!}F_j(w_1,\ldots,w_j),
\]

where translation invariance gives the equality, and (14)--(15) together with symmetry show that no daughter labelling is preferred.

Now fix an ordered observed $r$-tuple, where $1\leq r\leq j$. There are $j!/(j-r)!$ injections of its labels into the $j$ daughter positions. For each injection, integrating the $j-r$ unobserved absolute daughter coordinates gives the same kernel $\mathcal M^{j-r}F_j/j!$ by full symmetry. Summing the injections gives the ordered same-parent $r$-tuple density

\[
 \frac{1}{(j-r)!}\mathcal M^{j-r}F_j. \tag{19}
\]

This is the exact-size assignment count; it uses both full symmetry and translation invariance, not merely the formal number of permutations. Equations (9) therefore give total same-parent densities

\[
 b_2=F_2+\mathcal MF_3+\frac12\mathcal M^2F_4=q_2,
\]

\[
 b_3=F_3+\mathcal MF_4=q_3,
 \qquad b_4=F_4=q_4,
\]

while (18) gives $b_1=\rho$.

Every ordered observed tuple has a unique partition of its labels according to parent. Distinct Poisson parents have product factorial intensities. Hence all partitions contribute with coefficient one:

\[
 \rho^{(2)}(12)=\rho^2+q_2(12), \tag{20}
\]

\[
 \rho^{(3)}(123)=\rho^3
 +\rho\{q_2(12)+q_2(13)+q_2(23)\}+q_3(123), \tag{21}
\]

and

\[
\begin{aligned}
\rho^{(4)}(1234)
={}&\rho^4
 +\rho^2\sum_{1\leq i<j\leq4}q_2(ij)\\
&+q_2(12)q_2(34)+q_2(13)q_2(24)+q_2(14)q_2(23)\\
&+\rho\{q_3(123)+q_3(124)+q_3(134)+q_3(234)\}
 +q_4(1234). \tag{22}
\end{aligned}
\]

Thus (20), (21) and (22) contain respectively all $2,5,15$ set partitions. There are six pair-plus-two-singleton terms, three pair-pair terms and four triple-plus-singleton terms at order four.

Substituting (6) into (20) gives, on $S_2=\mathcal D_2$,

\[
 \rho^{(2)}=\frac{a_2}{D}.
\]

Substituting (7) into (21) gives, on $S_3$,

\[
 \rho^{(3)}=\frac{a_3}{A}.
\]

Substituting (8) into (22) gives, on $S_4=\mathcal D_4$,

\[
 \rho^{(4)}=\frac{a_4}{V}.
\]

Since $\mathcal D_3\subseteq S_3$, all three governing domains are covered. Dividing by $\rho^r$ gives the exact target with

\[
 C_2=\frac{a_2}{\rho^2}=\frac{1}{I\rho},\qquad
 C_3=\frac{a_3}{\rho^3}=\frac{1}{4BI\rho^2},\qquad
 C_4=\frac{a_4}{\rho^4}=\frac{1}{16BJI\rho^3}. \tag{23}
\]

These constants are positive and independent of configuration. Their units are respectively length, area and volume.

## Proof or obstruction

### The restricted exact theorem

Steps 1--5 construct a probability law on all of $\mathbb R^3$, prove its stationarity, isotropy, simplicity, local exponential moments, prescribed intensity and factorial-density existence, and establish nonnegativity of every cluster kernel. Equations (20)--(23) then prove the three full reciprocal identities almost everywhere on the complete governing domains. This completes the restricted theorem for every $0<\lambda_0\leq\lambda_*$.

The pair diagonal $D=0$, degenerate triangles, degenerate tetrahedra and support boundaries may be assigned arbitrary density values; they are Lebesgue-null. The pair singularity is nevertheless included at every positive distance and is locally integrable. No identity is asserted outside the requested domains, although the construction happens to satisfy the triangle identity on the possibly larger set $S_3$.

### A reduced-measure obstruction for bounded cluster size

We now use the standard independently marked homogeneous Poisson-parent convention. Parents form a homogeneous Poisson process of finite rate $\gamma$, and each parent independently receives a finite relative point-cluster mark $C$ with size $N$. Empty clusters may be discarded: independently thinning to parents with $N>0$ and conditioning the mark on $N>0$ leaves the daughter process unchanged. Multiple independent homogeneous parent types with finite total rate may likewise be combined by adding an independent type mark to one parent process. An independent singleton Poisson component may either be included as a type with $N=1$ or kept separate. After these reductions, suppose $1\leq N\leq K$ almost surely for clustered parents; let $\rho$ be the total daughter intensity, including any separate singleton component.

Define the reduced same-parent ordered pair measure $\nu_2$ on displacement space by

\[
 \nu_2(B)
 :=\gamma\,\mathbb E\!\sum_{u,v\in C}^{\ne}
       \mathbf1\{v-u\in B\},
 \qquad B\subseteq\mathbb R^3\ \text{Borel}. \tag{24}
\]

No global density is assumed for $\nu_2$. Its total mass is

\[
 Q_2:=\nu_2(\mathbb R^3)
 =\gamma\,\mathbb E[N(N-1)]
 \leq(K-1)\gamma\,\mathbb EN
 \leq(K-1)\rho. \tag{25}
\]

The last inequality permits a separate nonnegative singleton intensity. The reduced second factorial moment measure of a Poisson-cluster process is the sum of the distinct-parent baseline $\rho^2\,du$ and $\nu_2(du)$. We invoke a density only on the punctured target ball

\[
 B_M^\times=\{u:0<|u|\leq M\},
\]

where the assumed exact pair identity supplies the full density. On this ball, therefore,

\[
 \nu_2(du)
 =\rho^2\left(\frac{C_2}{|u|}-1\right)du. \tag{26}
\]

Because $\nu_2$ is a nonnegative measure, (26) implies $C_2\geq M$: if $C_2<M$, its displayed density would be negative on the positive-measure shell $C_2<|u|<M$. Hence the mass of the target ball alone gives

\[
\begin{aligned}
Q_2
&\geq\nu_2(B_M^\times)
 =4\pi\rho^2\int_0^M
 \left(\frac{C_2}{r}-1\right)r^2\,dr\\
&\geq4\pi\rho^2\left(\frac{M^3}{2}-\frac{M^3}{3}\right)
 =\frac{2\pi}{3}\rho^2M^3. \tag{27}
\end{aligned}
\]

Combining (25) and (27), then dividing by $\rho>0$, proves (O). Thus a construction with one fixed finite cluster-size cap cannot establish the governing theorem for every prescribed intensity. Equation (O) does not exclude unbounded clusters, a size cap depending on $\lambda_0M^3$, Cox directing measures, Gibbs processes, or general point processes.

## Reasoning summary and decision record

1. **Selected route.** The dependent finite-cluster inversion was selected because it is the only fully inspected local route whose existing proof already gives exact *full* densities through order four. The construction explicitly subtracts every lower partition and then inverts the marginal hierarchy to obtain genuine nonnegative cluster laws.
2. **Zero-cutoff check.** The previous lower pair cutoff was checked against the actual estimates. It is not needed for integrability: in three dimensions $1/D$ has finite anchored mass at zero, and the positivity and marginal estimates remain valid with $S_2=\{0<D\leq M\}$.
3. **Support-nesting check.** Using the target triangle threshold directly fails when $h_4<h_3$, because a target tetrahedron's faces need only have altitude at least $h_4$. Enlarging the auxiliary triangle support to threshold $\min\{h_3,h_4\}$ repairs this without shrinking any requested domain or changing the target identity.
4. **Prescribed-intensity check and provenance.** Setting $a_2=\lambda_0/I$ makes the final intensity identity exact. The residual positivity errors are the explicit polynomials (3), whose vanishing at zero yields (4). This quantifies, for the zero-cutoff supports, the small-prescribed-intensity interval already implicit in the prior polynomial-in-amplitude theorem; it is not an arbitrary-intensity transformation.
5. **Reanchoring and full-density check.** The unit-Jacobian map (14), together with symmetry and translation invariance, makes the anchored cluster law independent of the distinguished daughter and validates the coefficient in (19). The order-four calculation then includes all fifteen set partitions. The $q_4$ definition cancels six pair-singleton-singleton terms, three pair-pair terms, four triple-singleton terms and the all-singleton term.
6. **Alternatives not promoted.** The spherical Cox route preserves arbitrary prescribed intensity but remains approximate at finite parameters; no valid exact directing-measure limit was found. A Gibbs existence theorem would not identify its interaction weight with the full correlation hierarchy. The truncated-slab construction appears only as a summary in the inspected frozen notes, not as a complete source supplied in this packet, and its arbitrary prescribed-intensity quantifier was not established here.
7. **Why the theorem stops.** The positivity proof is a small-intensity argument. The reduced-measure estimate (O) shows that fixed bounded cluster size is itself incompatible with arbitrarily high intensity at fixed $M$. Claiming the unrestricted target would require a genuinely different intensity mechanism, such as an exact Cox directing measure or clusters whose size grows without a fixed cap.

## Checks and limitations

- **Analytical checks.** All physical dimensions in (1)--(4) and (23) match. The pair singularity was integrated explicitly. The tetrahedral marginal uses the prescribed positive $h_4$, so no $du/|u|$ divergence occurs. The intensity calculation includes every cluster type and the singleton correction.
- **Reanchoring and partition checks.** Equations (14)--(15) establish the unit-Jacobian anchor change. Equations (20)--(22) list all set partitions at orders two, three and four. No connected density is substituted for a full density.
- **Obstruction check.** The global object in (24)--(25) is a finite reduced measure, not an assumed density. Absolute continuity is used only after restricting to $B_M^\times$, where the exact pair law provides (26).
- **Boundary and excluded configurations.** Density values on diagonals, degenerate simplices and equality boundaries are immaterial to the a.e. claims. Outside the governing domains the full densities are those generated by the process, with no additional reciprocal identity asserted.
- **Computation.** No numerical grid, simulation or symbolic output is used as proof. The explicit threshold (4) is obtained by termwise analytical bounds.
- **Unresolved exact-target gap.** The construction proves the result only for $0<\lambda_0\leq\lambda_*(M,h_4)$. Existence or non-existence for larger prescribed intensities remains open in this submission. The obstruction (O) concerns only standard Poisson clusters with one fixed finite cluster-size cap.
- **Review status.** The inherited finite-cluster theorem was audited in the frozen local materials. This revision responds to the v01 review issues but is not a formal verification or a proof of the unrestricted target.

## References

1. *Exact reciprocal simplex correlations on finite domains*, frozen unpublished local manuscript, `common/prior_work/finite-cluster-reciprocal-laws/`. Full source tree inspected, especially `sections/construction.tex`, `sections/appendix_bounds.tex`, `sections/appendix_partitions.tex`, and the two mathematical audit files. This is the source of the inverse finite-cluster framework, not an external publication.
2. *Reciprocal simplex correlations from random spherical surfaces*, frozen unpublished local manuscript, `common/prior_work/reciprocal-simplex/`. Full source tree inspected, especially Sections 3--5 and `MATH_CHECK.md`. It proves prescribed-intensity approximation, not exact equality.
3. `shared_literature/dossier.md`, frozen 19 October 2026. The dossier's structural Poisson-cluster and Cox formulas were checked there against Clark--Houssineau and Last--Penrose. The proof in this submission is self-contained and does not depend on an unquoted external theorem.
4. Daley and Vere-Jones, *An Introduction to the Theory of Point Processes*, Vol. II, 2nd ed., Exercise 12.6.11, printed p. 249. The frozen local source audit verifies that the historical statement concerns factorial moment densities; it does not supply the present construction.

## Response to review (v02 onward)

1. **A4-V01-01 — unresolved governing scope.** Preserved. The theorem is explicitly restricted to $0<\lambda_0\leq\lambda_*(M,h_4)$, and the claim status, proof conclusion, decision record and limitations all state that arbitrary prescribed intensity remains unresolved.
2. **A4-V01-02 — measure-form obstruction.** Repaired in (24)--(27). The obstruction now starts from the reduced same-parent pair measure, assumes no global density for it, states the independently marked homogeneous Poisson-parent convention, discards empty clusters, combines multiple parent types, and accommodates an independent singleton process. A density is invoked only on the punctured target ball, where the exact pair identity supplies it.
3. **A4-V01-03 — provenance.** Repaired in `Relation to prior work` and item 4 of the decision record. The presentation now says “changes and explicit reformulations”. It identifies the low prescribed-intensity interval as an explicit reformulation and zero-cutoff re-derivation of what the prior polynomial-in-$a_2$ theorem already implied, rather than calling it a new conceptual result.
4. **A4-V01-04 — reanchoring.** Repaired in (14)--(15) and in the derivation of (19). The revision proves that reanchoring is an invertible determinant-one map, uses translation invariance and full symmetry of $F_r$, and only then counts the $j!/(j-r)!$ assignments leading to the coefficient $1/(j-r)!$.
