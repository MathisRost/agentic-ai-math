# Approach 1 — submission v02

- Run / model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem snapshot SHA-256: `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`.
- Context packet and source dossier version: `context_packets/proof_1_v02.md`, repair round 1; shared dossier SHA-256 `5d42ad11b6b55246e6a0eb098b3f09c1bf3751cd3add4a819f5e427017b659f5`, dated 19 October 2026.
- Claim status: **restricted exact theorem and scoped obstruction**. The construction below removes the positive pair-distance cutoff and gives all three exact full identities on the governing domains at every sufficiently small *prescribed* intensity. It does not cover arbitrary prescribed intensity: every intensity above the certified endpoint \(\lambda_*\) remains open. The separate obstruction applies only to Poisson clusters with a fixed almost-sure upper bound on cluster size; it is not a general obstruction for unbounded clusters or arbitrary point processes.

## Claim and scope

Fix \(M,h_3,h_4>0\). Assume

\[
0<h_3<\frac{\sqrt3}{2}M,
\qquad
0<h_4<\sqrt{\frac23}\,M,
\tag{1}
\]

so the triangle and tetrahedron domains contain open families. Let

\[
h:=\min\{h_3,h_4\},\qquad H:=h_4.
\]

The auxiliary triangle support used in the construction is

\[
S_3=\{\operatorname{diam}\le M, \text{every triangle altitude}\ge h\},
\]

which contains the governing triangle domain
\(\mathcal D_3\). The other supports are exactly

\[
S_2=\{0<D\le M\},\qquad S_4=\mathcal D_4.
\tag{2}
\]

The enlargement of \(S_3\) is harmless: it asks the constructed process to obey the reciprocal-area law on a possibly larger set. Its purpose is to ensure that every face of a tetrahedron in \(S_4\) lies in \(S_3\), even when \(h_4<h_3\).

Define the geometric constants

\[
I=2\pi M^2,\qquad J=\frac{4\pi}{3}M^3,\qquad
B=2\pi^2M^2,
\tag{3}
\]

and

\[
K=6\pi\left[M^2\log\!\left(\frac{M}{H}\right)
-\frac{M^2-H^2}{2}\right]>0.
\tag{4}
\]

For a proposed intensity \(\lambda>0\), set

\[
a_2=\frac{\lambda}{I},\qquad
a_3=\frac{a_2}{4B},\qquad
a_4=\frac{a_2}{16BK}.
\tag{5}
\]

Introduce the dimensionless errors

\[
\begin{aligned}
E_2(\lambda)&=\lambda I M,\\
E_3(\lambda)&=2\lambda^2IBM^2+6\lambda BM,\\
E_4(\lambda)&=\frac83\lambda^3IBKM^3
+16\lambda^2BKM^2
+\frac{8\lambda BKM}{I}
+\frac{16}{3}\lambda KM.
\end{aligned}
\tag{6}
\]

Each is continuous and strictly increasing for \(\lambda>0\), vanishes at zero,
and \(E_2(t)\to\infty\) as \(t\to\infty\). Therefore

\[
\Lambda(M,h_4)
:=\{t\ge0:E_2(t),E_3(t),E_4(t)\le\tfrac12\}
=[0,\lambda_*(M,h_4)]
\tag{7}
\]

is a nonempty bounded closed interval. Indeed, continuity gives closedness,
monotonicity gives the interval property, continuity at zero gives a positive
feasible neighbourhood of zero, and the divergence of \(E_2\) gives boundedness.
Consequently its endpoint

\[
\lambda_*(M,h_4):=\max\Lambda(M,h_4)>0
\tag{7a}
\]

is attained.

### Theorem 1 (exact no-pair-cutoff finite-cluster theorem)

For every \(M,h_3,h_4\) satisfying (1), and for every **prescribed** intensity

\[
0<\lambda_0\le \lambda_*(M,h_4),
\]

there is one stationary, isotropic, simple, locally finite point process \(X\) on all of
\(\mathbb R^3\), of intensity exactly \(\lambda_0\), with finite local exponential
moments and absolutely continuous factorial moment measures at every finite order, such that

\[
g_2=\frac{C_2}{D}\quad\text{a.e. on }\mathcal D_2,
\qquad
g_3=\frac{C_3}{A}\quad\text{a.e. on }\mathcal D_3,
\qquad
g_4=\frac{C_4}{V}\quad\text{a.e. on }\mathcal D_4,
\tag{8}
\]

simultaneously, where

\[
C_2=\frac{a_2}{\lambda_0^2},\qquad
C_3=\frac{a_3}{\lambda_0^3},\qquad
C_4=\frac{a_4}{\lambda_0^4}
\tag{9}
\]

are positive. There is no lower cutoff in (8): the pair identity holds for almost every \(0<D\le M\).

This proves the governing exact target for the nonempty, geometry-dependent interval of prescribed intensities \(0<\lambda_0\le\lambda_*\), including its upper endpoint. It is partial because the governing quantifier asks for every \(\lambda_0>0\). In particular, the existence question remains open here for every prescribed \(\lambda_0>\lambda_*(M,h_4)\).

### Proposition 2 (bounded-cluster intensity obstruction)

Let \(X\) be any stationary Poisson cluster process with parent intensity
\(\kappa>0\), independent identically distributed finite simple clusters, and
cluster size \(N\le L\) almost surely for a fixed integer \(L\ge2\). Suppose
\(X\) has intensity \(\lambda>0\), an absolutely continuous second factorial
moment measure, and

\[
g_2(x,y)=\frac{C_2}{\lVert x-y\rVert}
\quad\text{for a.e. }0<\lVert x-y\rVert\le M.
\tag{10}
\]

Then necessarily

\[
\lambda\le \frac{3(L-1)}{2\pi M^3}.
\tag{11}
\]

In particular, a process with clusters of size at most four must satisfy

\[
\lambda\le\frac{9}{2\pi M^3}.
\tag{12}
\]

Thus no Poisson-cluster architecture with one fixed almost-sure upper bound on cluster size can solve the governing problem for all prescribed intensities. This proposition makes no claim about finite clusters whose size bound grows with \(\lambda\), unbounded but almost surely finite clusters, non-Poisson parent processes, or general point processes.

## Relation to prior work

The frozen local finite-cluster manuscript proves exact full reciprocal identities by two triangular inversions: first from target full densities to same-parent kernels, then from same-parent kernels to exact-size cluster densities. Its theorem assumes a positive pair cutoff δ and chooses intensity together with the amplitudes. I inspected its complete frozen source tree, including `sections/construction.tex`, `sections/appendix_bounds.tex`, `sections/appendix_partitions.tex`, both mathematical audits, and the sampler and obstruction appendices.

The new points here are:

1. setting the pair cutoff to zero and proving that every anchored integral and positivity estimate remains valid;
2. enlarging only the auxiliary triangle support to the altitude threshold
   \(\min(h_3,h_4)\), which handles either ordering of the two governing altitude thresholds;
3. solving explicitly for the amplitude \(a_2=\lambda_0/I\), so every intensity in the interval (7) is prescribed before the construction rather than selected afterwards; and
4. deriving the quantitative obstruction (11) for every bounded-size Poisson cluster process.

This revision also makes the endpoint attainment in (7)--(7a) explicit and
records the permutation and re-rooting lemma needed for the ordered-daughter
count below.

The spherical Cox manuscript was also inspected in full. Its one-sphere terms and full 2-, 5-, and 15-partition expansions are correct, but the result is approximate at finite parameters. No limit from that manuscript is used here.

For published structural support, Clark and Houssineau, Theorem 4.2 and equation (21), give the independent-cluster factorial-moment partition formula without requiring iid daughters inside a cluster. Last and Penrose, Exercise 8.2, give the stationary Poisson-cluster construction and its intensity; Exercises 9.10--9.12 identify the nonnegative same-cluster pair contribution. The proof below is nevertheless self-contained through order four.

## Process and existence

Write

\[
K_2(12)=\frac{\mathbf1_{S_2}(12)}{D(12)},\qquad
K_3(123)=\frac{\mathbf1_{S_3}(123)}{A(123)},\qquad
K_4(1234)=\frac{\mathbf1_{S_4}(1234)}{V(1234)},
\tag{13}
\]

with value zero on degenerate configurations. Put
\(\lambda=\lambda_0\). Define same-parent kernels recursively by

\[
q_2(12)=\mathbf1_{S_2}(12)
\left(\frac{a_2}{D(12)}-\lambda^2\right),
\tag{14}
\]

\[
q_3(123)=\mathbf1_{S_3}(123)
\left(\frac{a_3}{A(123)}-\lambda^3
-\lambda\sum_{i<j}q_2(ij)\right),
\tag{15}
\]

and

\[
\begin{aligned}
q_4(1234)=\mathbf1_{S_4}(1234)\Bigg(&\frac{a_4}{V(1234)}-\lambda^4
-\lambda^2\sum_{i<j}q_2(ij)\\
&-\sum_{ij\mid k\ell}q_2(ij)q_2(k\ell)
-\lambda\sum_{|T|=3}q_3(T)\Bigg).
\end{aligned}
\tag{16}
\]

The pair-pair sum in (16) has the three terms \(12\mid34\), \(13\mid24\), \(14\mid23\), and the last sum has the four faces.

### 1. Pointwise positivity of the same-parent kernels

On \(S_2\), the subtraction in (14), divided by \(a_2/D\), is at most

\[
\frac{\lambda^2M}{a_2}=E_2(\lambda).
\]

For any triangle of diameter at most \(M\),

\[
A\le\frac{M^2}{2},\qquad \frac{A}{d_{ij}}\le\frac M2.
\]

Using \(q_2\le a_2K_2\), the total subtraction in (15), divided by \(a_3/A\), is at most

\[
\frac{\lambda^3M^2}{2a_3}
+\frac{3\lambda a_2M}{2a_3}=E_3(\lambda).
\]

For any tetrahedron of diameter at most \(M\),

\[
V\le\frac{M^3}{6},\quad
\frac{V}{d_{ij}}\le\frac{M^2}{6},\quad
\frac{V}{d_{ij}d_{k\ell}}\le\frac M6,
\quad
\frac{V}{A_T}\le\frac M3.
\tag{17}
\]

The third inequality concerns disjoint edges and follows by expressing \(6V\) as the scalar triple product of those two edges and one connecting edge. Counting the six edges, three pairings and four faces in (16), the total relative subtraction is at most

\[
\frac{\lambda^4M^3}{6a_4}
+\frac{\lambda^2a_2M^2}{a_4}
+\frac{a_2^2M}{2a_4}
+\frac{4\lambda a_3M}{3a_4}=E_4(\lambda).
\]

Substitution of (5) gives exactly (6). Consequently, under (7),

\[
\frac12a_jK_j\le q_j\le a_jK_j,
\qquad j=2,3,4.
\tag{18}
\]

### 2. Marginal bounds, including the pair singularity at zero

Let
\(\mathcal M\) denote integration over one omitted coordinate. Fix a pair at distance \(d>0\), and let \(r\) be the distance of a third point from the affine line through the pair. Since \(A=dr/2\), cylindrical coordinates in the ball \(B(x_1,M)\) give

\[
\int_{B(x_1,M)}\frac{dz}{r}=\pi^2M^2.
\]

Therefore

\[
\mathcal M K_3\le BK_2,
\qquad B=2\pi^2M^2.
\tag{19}
\]

No lower bound on \(d\) was used. The right side behaves as \(1/d\), whose anchored integral is finite:

\[
\int_{0<|y|\le M}\frac{dy}{|y|}=4\pi\int_0^M r\,dr=2\pi M^2=I.
\tag{20}
\]

This is the decisive reason the former cutoff \(\delta\) can be removed.

For a fixed base triangle of area \(A\), write \(u\) for the signed height of an omitted fourth point. On \(S_4\),
\(|u|\ge H\), \(V=A|u|/3\), and the cross-section of \(B(x_1,M)\) at height \(u\) has area at most
\(\pi(M^2-u^2)\). Hence

\[
\mathcal M K_4
\le \frac{6\pi}{A}\int_H^M\left(\frac{M^2}{u}-u\right)du
=K K_3.
\tag{21}
\]

The support statements in (19)--(21) are valid because every edge of a triangle in \(S_3\) belongs to \(S_2\), and every face of a tetrahedron in \(S_4\) belongs to \(S_3\). For the latter claim, a face vertex's distance to the opposite edge is at least its distance to the tetrahedral plane containing that edge, hence at least \(H\ge h\).

### 3. Exact-size cluster kernels

Set

\[
F_4=q_4,\qquad
F_3=q_3-\mathcal Mq_4,\qquad
F_2=q_2-\mathcal Mq_3+\frac12\mathcal M^2q_4.
\tag{22}
\]

Equations (18)--(21) and the choices in (5) give

\[
F_4\ge\frac12a_4K_4,\qquad
F_3\ge\left(\frac12a_3-a_4K\right)K_3
=\frac14a_3K_3,
\tag{23}
\]

and

\[
F_2\ge\left(\frac12a_2-a_3B\right)K_2
=\frac14a_2K_2.
\tag{24}
\]

Moreover \(F_3\le q_3\), and the equivalent identity

\[
F_2=q_2-\mathcal MF_3-\frac12\mathcal M^2F_4
\]

gives \(F_2\le q_2\). The kernels therefore have finite, strictly positive anchored integrals

\[
Z_j=\int F_j(0,y_2,\ldots,y_j)\,dy_2\cdots dy_j,
\qquad j=2,3,4.
\tag{25}
\]

The only unbounded kernel is \(K_2\sim1/D\) at the diagonal, and (20) proves its local and anchored integrability. The altitude cutoffs bound the triangle and tetrahedron kernels away from their degeneracies. Thus (22) defines genuine nonnegative probability densities after normalisation; no formal signed cluster law is used.

### Lemma 3 (translation invariance, symmetry and re-rooting)

For \(j=2,3,4\), both \(q_j\) and \(F_j\), regarded as kernels of
\((x_1,\ldots,x_j)\), are translation invariant and invariant under every
permutation of their \(j\) arguments. If a configuration is represented by
the anchored coordinates

\[
(y_2,\ldots,y_j)=(x_2-x_1,\ldots,x_j-x_1),
\]

then changing the root to any other daughter and permuting the remaining
daughters has absolute Jacobian one on \(\mathbb R^{3(j-1)}\).

**Proof.** The supports \(S_j\), the geometric functions \(D,A,V\), and the
partition sums in (14)--(16) depend only on the unlabelled translated
configuration. Induction through (14)--(16) therefore proves the assertion for
the \(q_j\). If \(G_j\) is a symmetric translation-invariant kernel, define

\[
(\mathcal M G_j)(x_1,\ldots,x_{j-1})
=\int_{\mathbb R^3}G_j(x_1,\ldots,x_{j-1},u)\,du.
\]

This marginal is symmetric in its remaining arguments and translation
invariant, the latter after the change of variable \(u\mapsto u+a\).
Consequently (22) gives the same properties for every \(F_j\).

For re-rooting, put \(x_1=0\) and \(x_k=y_k\) for \(k\ge2\). After a
permutation \(\pi\), the new anchored coordinates are

\[
y'_k=x_{\pi(k)}-x_{\pi(1)},\qquad k=2,\ldots,j.
\]

For one spatial coordinate this is an invertible integer linear map whose
inverse is the analogous re-rooting map for \(\pi^{-1}\); its determinant is
therefore \(\pm1\). Applying it independently to the three spatial coordinates
gives absolute Jacobian one. \(\square\)

### 4. The process

Take three independent homogeneous Poisson parent processes of types \(j=2,3,4\), with rates \(Z_j/j!\). A type-\(j\) parent at \(z\) emits

\[
\{z,z+Y_2,\ldots,z+Y_j\},
\]

where
\((Y_2,\ldots,Y_j)\) has density
\(F_j(0,\cdot)/Z_j\). Let

\[
Q_j=\int q_j(0,y_2,\ldots,y_j)\,dy_2\cdots dy_j.
\]

Integrating (22) gives

\[
Z_4=Q_4,\qquad Z_3=Q_3-Q_4,\qquad
Z_2=Q_2-Q_3+\frac12Q_4.
\tag{26}
\]

Since \(a_2I=\lambda\),

\[
Q_2=a_2I-\lambda^2J=\lambda-\lambda^2J.
\tag{27}
\]

Add an independent singleton Poisson process of rate

\[
\lambda_1=\lambda^2J+\frac{Z_3}{2}+\frac{Z_4}{3}>0.
\tag{28}
\]

All offsets have norm at most \(M\). A bounded observation set can therefore receive points only from a finite Poisson number of parents in its \(M\)-enlargement, and every parent emits at most four points. This proves local finiteness and finite local exponential moments. Translation and rotation invariance of the parent processes and kernels prove stationarity and isotropy.

The anchored mark densities are absolutely continuous. Their diagonal sets have Lebesgue measure zero, including the \(D=0\) pair diagonal despite the integrable \(1/D\) singularity. Thus points within a cluster are distinct almost surely. Diffuse parent locations and continuous marks exclude collisions between different clusters, proving simplicity.

The non-singleton intensity is

\[
\frac{Z_2}{1!}+\frac{Z_3}{2!}+\frac{Z_4}{3!}
=Q_2-\frac12Q_3+\frac16Q_4.
\]

Adding (28), and using (26)--(27), gives exactly \(\lambda\). Hence the prescribed intensity is the actual intensity; no fixed-point or post-construction rescaling is used.

## Full product-density calculation

For a type-\(j\) cluster, the same-parent ordered \(r\)-tuple density is

\[
b_r^{(j)}=\frac{1}{(j-r)!}\mathcal M^{j-r}F_j,
\qquad 1\le r\le j.
\tag{29}
\]

Here is the count in full. Temporarily label the daughter positions by
\(X_1=z\) and \(X_k=z+Y_k\) for \(2\le k\le j\). The transformation

\[
(z,Y_2,\ldots,Y_j)\longmapsto(X_1,\ldots,X_j)
\]

has absolute Jacobian one. By translation invariance, the parent rate
\(Z_j/j!\) and the mark density \(F_j(0,Y_2,\ldots,Y_j)/Z_j\) therefore give
the labelled full configuration the density \(F_j(X_1,\ldots,X_j)/j!\).

For an observed ordered \(r\)-tuple, there are exactly

\[
(j)_r=j(j-1)\cdots(j-r+1)=\frac{j!}{(j-r)!}
\]

injective assignments of its ordered entries to the \(j\) daughter labels.
For each assignment, integration over the other \(j-r\) labelled daughters
gives \(\mathcal M^{j-r}F_j\): Lemma 3 permits the observed daughters to be
permuted and one of them to be used as root, with no Jacobian factor. Thus the
coefficient is \((j)_r/j!=1/(j-r)!\), which proves (29).

Summing (29) over cluster types, and including the singleton stream, gives

\[
b_1=\lambda,\qquad b_2=q_2,\qquad b_3=q_3,\qquad b_4=q_4.
\tag{30}
\]

Indeed, for orders two through four, (22) is equivalently

\[
F_2+\mathcal MF_3+\frac12\mathcal M^2F_4=q_2,
\qquad F_3+\mathcal MF_4=q_3,
\qquad F_4=q_4.
\]

The order-one identity is the intensity calculation preceding (29).

Each observed ordered tuple has a unique partition of its labels according to common parent. Distinct Poisson parents have product factorial intensity. The complete partition sums are therefore

\[
\rho^{(2)}(12)=\lambda^2+q_2(12),
\tag{31}
\]

\[
\rho^{(3)}(123)=\lambda^3
+\lambda\{q_2(12)+q_2(13)+q_2(23)\}+q_3(123),
\tag{32}
\]

and

\[
\begin{aligned}
\rho^{(4)}(1234)
={}&\lambda^4
+\lambda^2\sum_{i<j}q_2(ij)
+\{q_2(12)q_2(34)+q_2(13)q_2(24)+q_2(14)q_2(23)\}\\
&+\lambda\{q_3(123)+q_3(124)+q_3(134)+q_3(234)\}
+q_4(1234).
\end{aligned}
\tag{33}
\]

These are respectively the 2, 5 and 15 set partitions; order one has its single partition. In particular, (31)--(33) are full product densities, not connected densities or same-cluster approximations.

The identities also prove absolute continuity. More generally, at every order a nonzero partition block has size at most four, and each block measure has an ordinary density. Products and finite partition sums therefore give ordinary factorial densities at all finite orders.

## Proof or obstruction

### Proof of Theorem 1

The process and its properties were established above. It remains to verify the three identities.

On \(S_2\), substitute (14) into (31):

\[
\rho^{(2)}(12)=\lambda^2+\left(\frac{a_2}{D(12)}-\lambda^2\right)
=\frac{a_2}{D(12)}.
\tag{34}
\]

On \(S_3\), every pair is in \(S_2\). Substituting (15) into (32) cancels the four lower-partition contributions and gives

\[
\rho^{(3)}(123)=\frac{a_3}{A(123)}.
\tag{35}
\]

On \(S_4\), all six pairs lie in \(S_2\) and all four faces lie in \(S_3\). Substituting (16) into the full fifteen-term formula (33) cancels the four-singleton term, all six pair-singleton-singleton terms, all three pair-pair terms, and all four triple-singleton terms, leaving

\[
\rho^{(4)}(1234)=\frac{a_4}{V(1234)}.
\tag{36}
\]

Since
\(\mathcal D_2=S_2\),
\(\mathcal D_3\subseteq S_3\), and
\(\mathcal D_4=S_4\), division by
\(\lambda^n\) yields (8)--(9) on the entire governing domains. Boundaries and degenerate configurations are null sets for the asserted a.e. identities. This completes the proof.

### Proof of Proposition 2

For a Poisson cluster process, the second full density is

\[
\rho^{(2)}(x,y)=\lambda^2+c_2(x,y),
\]

where \(c_2\) is the nonnegative same-parent pair density. Equation (10) therefore gives, for almost every \(0<|y|\le M\),

\[
c_2(0,y)=\lambda^2\left(\frac{C_2}{|y|}-1\right)\ge0.
\tag{37}
\]

If \(C_2<M\), the right side is negative on the positive-measure shell \(C_2<|y|\le M\), a contradiction. Thus \(C_2\ge M\). The total anchored same-parent pair mass consequently satisfies

\[
\begin{aligned}
Q_2:=\int_{\mathbb R^3}c_2(0,y)\,dy
&\ge4\pi\lambda^2\int_0^M
\left(\frac{C_2}{r}-1\right)r^2\,dr\\
&=4\pi\lambda^2\left(\frac{C_2M^2}{2}-\frac{M^3}{3}\right)
\ge\frac{2\pi}{3}\lambda^2M^3.
\end{aligned}
\tag{38}
\]

On the other hand, direct integration of the one-cluster ordered pair measure gives

\[
Q_2=\kappa\,\mathbb E(N)_2,
\qquad
\lambda=\kappa\,\mathbb EN.
\tag{39}
\]

Since \(N\le L\),
\((N)_2=N(N-1)\le(L-1)N\). Hence \(Q_2\le(L-1)\lambda\). Combining this with (38) and dividing by \(\lambda\) proves (11). Taking \(L=4\) proves (12).

## Reasoning summary and decision record

1. **Starting point.** The exact finite-cluster manuscript already solves both triangular inverse problems on a domain with
   \(\delta>0\), but its intensity and amplitudes are selected together. The spherical carrier manuscript supplies prescribed intensity but only approximate identities.
2. **Pair-cutoff test.** Every place where \(\delta\) entered the finite-cluster proof was checked. The only potentially singular integral is
   \(\int_{|y|\le M}|y|^{-1}dy\), which equals
   \(2\pi M^2\). The positivity and marginal estimates are uniform down to \(D=0\). Thus setting \(\delta\) to zero is legitimate; no limiting process is needed.
3. **Altitude-order test.** Directly using the target triangle support fails to be deletion-nested when \(h_4<h_3\). Enlarging the auxiliary triangle support to altitude at least
   \(\min(h_3,h_4)\) repairs nesting and strengthens, rather than weakens, the triangle identity.
4. **Prescribed-intensity choice.** Setting \(a_2=\lambda_0/I\) makes the exact bookkeeping intensity equal to the input
   \(\lambda_0\). The remaining positivity conditions become the explicit polynomials (6). Their common feasible set is the compact interval (7), so the upper endpoint is included rather than merely approached.
5. **Alternatives rejected.** Independent thinning preserves normalized \(g_n\) but can only lower intensity. Independent superposition changes every connected-to-full partition coefficient. Spatial rescaling preserves reciprocal form but also preserves the dimensionless obstruction scale
   \(\lambda M^3\); it cannot turn the present small-intensity theorem into an arbitrary-intensity theorem on the same physical domain.
6. **Why the result stops.** The pair law forces a same-parent pair mass of order
   \(\lambda^2M^3\). Within the class covered by Proposition 2, a cluster containing at most \(L\) points supplies at most \(L-1\) same-parent partners per point, yielding (11). Therefore the present max-four refinement cannot meet the missing arbitrary-intensity quantifier. The argument does not decide whether a growing or unbounded cluster size, or a different process class, can do so.

## Checks and limitations

- **Analytical checks.** The proof explicitly includes the 1, 2, 5 and 15 partition contributions; checks support nesting; proves nonnegativity and normalisation of every cluster density; computes the actual intensity; treats the \(D\downarrow0\) singularity by an exact integral; verifies endpoint attainment; and records the full \((j)_r\) ordered-daughter count together with its determinant-one re-rooting. No value outside the governing finite domains is used in the final identities.
- **Source checks.** Both complete frozen local manuscript source trees were inspected. The shared literature dossier records full-text verification of the cited Clark--Houssineau and Last--Penrose locations. Archived reviews were treated as evidence and reconciled with the final source, not as instructions.
- **No computational dependence.** No numerical grid, simulation, symbolic algebra output or empirical catalogue is used in the theorem or obstruction.
- **Exact remaining gap.** For every prescribed
  \(\lambda_0>\lambda_*(M,h_4)\), no construction is supplied. Proposition 2 applies only when one fixed finite \(L\) bounds the cluster size almost surely; it says nothing about unbounded cluster sizes, non-Poisson parent processes, or general point processes. The arbitrary-intensity target therefore remains unresolved.
- **Review status.** This is a repaired natural-language proof responding to the complete author-facing v01 issue list. It is not a proof-assistant formalisation, and the repair has not yet received an independent reviewer verdict.

## References

1. D. E. Clark and J. Houssineau, *Faà di Bruno's formula and spatial cluster modelling*, **Spatial Statistics** 6 (2013), 109--117. The shared dossier records full-text verification of Theorems 4.1--4.2, equations (19)--(22), especially the factorial-moment partition formula (21).
2. G. Last and M. Penrose, *Lectures on the Poisson Process* (2017), Exercise 8.2 and Exercises 9.10--9.12. The shared dossier records full-text verification of the stationary cluster construction, intensity, and the Poisson baseline plus nonnegative same-cluster pair term.
3. Frozen local manuscript, `common/prior_work/finite-cluster-reciprocal-laws/`: `sections/construction.tex`, `sections/appendix_bounds.tex`, and `sections/appendix_partitions.tex`, plus the reconciled final mathematical audits. Full frozen source inspected.
4. Frozen local manuscript, `common/prior_work/reciprocal-simplex/`: Sections 3--5 for the spherical Cox construction and its exact full partition formulas and approximation theorem. Full frozen source inspected.
5. Frozen problem and literature sources: `common/problem_statement.md`, `common/literature/02_poisson_cluster.md`, and `shared_literature/dossier.md` in this run.

## Response to review (v02 onward)

1. **A1-v01-F1 — unresolved governing scope.** The claim-status paragraph, Theorem 1 discussion, reasoning record and limitations now all state the exact restricted quantifier \(0<\lambda_0\le\lambda_*(M,h_4)\). They also state explicitly that every prescribed intensity above \(\lambda_*\) remains open. No arbitrary-intensity existence or general non-existence claim is made.
2. **A1-v01-F2 — obstruction scope.** Proposition 2 remains restricted to stationary Poisson cluster processes whose cluster size has one fixed almost-sure upper bound \(L\). The optional v01 observation about an unbounded-size moment condition has been removed. The proposition and limitations explicitly exclude any inference about unbounded clusters, non-Poisson parents or general point processes.
3. **A1-v01-F3 — endpoint inclusion.** Equation (7) now defines the extended feasible set with \(t\ge0\). Continuity makes it closed, strict monotonicity makes it an interval, continuity at zero supplies a positive feasible neighbourhood, and \(E_2(t)\to\infty\) makes it bounded. Hence it equals \([0,\lambda_*]\), the maximum in (7a) is attained, and Theorem 1 legitimately includes \(\lambda_0=\lambda_*\).
4. **A1-v01-F4 — re-rooting/permutation count.** Lemma 3 proves translation invariance and full permutation symmetry of every \(q_j\) and \(F_j\), and proves that anchored re-rooting has absolute Jacobian one. The product-density section now counts the \((j)_r=j!/(j-r)!\) injective ordered assignments explicitly against the parent rate \(Z_j/j!\), yielding \(b_r^{(j)}=(j-r)!^{-1}\mathcal M^{j-r}F_j\).
