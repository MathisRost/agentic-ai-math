# Cutoffs: precise claims and a finite-moment distinction

Revised coordinator submission v02, 20 October 2026. This is a self-contained
mathematical argument for independent review, not a manuscript revision.
The constants in the reciprocal laws are chosen by the construction.

## 1. Pair and triangle cutoffs are unnecessary at sufficiently small intensity

Write D for distance, A for triangle area, V for tetrahedral volume and h4
for the minimum vertex-to-opposite-affine-plane distance. Fix

\[
0<M\le P<\infty,\qquad 0<H<\sqrt{2/3}\,M.
\]

Use the domains

\[
S_2=\{0<D\le P\},\qquad S_3=\{A>0,\ d_{\max}\le M\},
\qquad S_4=\{V>0,\ d_{\max}\le M,\ h_4\ge H\}.
\]

For every sufficiently small prescribed rho>0, there is a stationary isotropic
simple point process of intensity rho, with finite local exponential moments
and absolutely continuous factorial moment measures at every order, such that
its full densities satisfy

\[
m_2=a_2/D\ \text{on }S_2,\qquad
m_3=a_3/A\ \text{on }S_3,\qquad
m_4=a_4/V\ \text{on }S_4
\]

for positive configuration-independent a2,a3,a4. Equalities are a.e.; the
displayed versions satisfy them at every nondegenerate point of the domains.
In particular, neither a positive lower pair distance nor a positive lower
triangle altitude is needed, even while retaining the fourth-order identity.
This does not assert existence at every prescribed intensity.

### Explicit sufficient conditions

Set

\[
I=2\pi P^2,\quad L=4\pi P^3/3,\quad B=2\pi^2M^2,
\quad C=6\pi\{M^2\log(M/H)-(M^2-H^2)/2\}.
\]

For prescribed rho define a2=rho/I, a3=a2/(4B), a4=a2/(16BC).
It suffices that all three numbers below are at most 1/2:

\[
E_2=\rho^2P/a_2,\quad
E_3=\rho^3M^2/(2a_3)+3\rho a_2M/(2a_3),
\]
\[
E_4=\rho^4M^3/(6a_4)+\rho^2a_2M^2/a_4+
a_2^2M/(2a_4)+4\rho a_3M/(3a_4).
\]

Each is a polynomial in rho with positive coefficients and zero constant
term, so this defines a nonempty interval of permitted positive intensities.

### Integrability and nesting

Define Kj as the reciprocal content times the domain indicator, zero on
degenerate configurations. For a pair of length d, cylindrical coordinates
about its line give

\[
\int K_3(x_1,x_2,z)\,dz
\le {2\over d}\int_{B(x_1,M)}{dz\over
 \operatorname{dist}(z,\operatorname{aff}(x_1,x_2))}
={2\pi^2M^2\over d}.
\]

Indeed the cylindrical integral is
4pi integral_0^M sqrt(M^2-r^2)dr=pi^2 M^2.
Every edge in S3 has length in (0,P], so this marginal is zero outside S2.
Consequently $\mathcal M K_3\le B K_2$, where $\mathcal M$ denotes integration over one omitted coordinate.
Also integral K2(0,y)dy=I<infinity, so the anchored integral of K3 is finite.
This includes simultaneous short-edge and flattening limits.

For a noncollinear base of area A, use signed height u and in-plane coordinates
for the fourth vertex. On S4, |u|>=H and V=A|u|/3. Thus

\[
\int K_4(x_1,x_2,x_3,z)\,dz
\le {6\pi\over A}\int_H^M {M^2-u^2\over u}\,du={C\over A}.
\]

Every face of a supported tetrahedron belongs to S3 because it is
noncollinear and has diameter at most M. No positive triangle-altitude
condition is used. Therefore $\mathcal M K_4\le C K_3$, and its anchored integral is finite.

### Residuals and actual cluster kernels

Define

\[
q_2=1_{S_2}(a_2/D-\rho^2),
\quad
q_3=1_{S_3}(a_3/A-\rho^3-\rho\sum_{i<j}q_2(ij)),
\]
\[
q_4=1_{S_4}(a_4/V-\rho^4-\rho^2\sum_{i<j}q_2(ij)
-\sum_{ij|kl}q_2(ij)q_2(kl)-\rho\sum_{|J|=3}q_3(J)).
\]

There are three pairings ij|kl and four faces J. Bounds valid for diameter<=M
are A<=M^2/2, A/d<=M/2, V<=M^3/6, V/d<=M^2/6,
V/(dij dkl)<=M/6 for disjoint edges, and V/Aface<=M/3.
For disjoint edges, use
6V=|det(x2-x1,x3-x1,x4-x3)|<=d12 M d34.
They give a_j Kj/2 <= qj <= a_j Kj from the E bounds.

Set $F_4=q_4$, $F_3=q_3-\mathcal M q_4$, and
$F_2=q_2-\mathcal M q_3+\tfrac12\mathcal M^2q_4$. Then

\[
F_4\ge a_4K_4/2,\quad
F_3\ge(a_3/2-a_4C)K_3=a_3K_3/4,\quad
F_2\ge(a_2/2-a_3B)K_2=a_2K_2/4.
\]

They are integrable; F3<=q3 and
$F_2=q_2-\mathcal M F_3-\tfrac12\mathcal M^2F_4\le q_2$. Their anchored integrals Zj are positive:
take small neighbourhoods of a regular tetrahedron with side strictly between
sqrt(3/2)H and M, its faces and its edges.

Use independent Poisson parent streams of rates Zj/j!, j=2,3,4. A j-parent
at z emits z and j-1 offsets with density Fj(0,.)/Zj. Add singleton parents
of rate rho^2 L+Z3/2+Z4/3. All offsets are bounded by P. Finitely many
parents can influence each bounded window, and each emits at most four points,
giving finite local exponential moments and local finiteness. Absolute
continuity gives simplicity. Translation and rotation invariance of Fj
give stationarity and isotropy.

Writing Qj=integral qj(0,.), we have
Z4=Q4, Z3=Q3-Q4, Z2=Q2-Q3+Q4/2 and Q2=rho-rho^2L.
Non-singleton intensity is Q2-Q3/2+Q4/6, so the stated singleton rate
makes total intensity exactly rho.

A j-cluster contributes $\mathcal M^{j-r}F_j/(j-r)!$ to the same-parent ordered r-point
density. The total same-parent densities are rho,q2,q3,q4. Distinct Poisson
parents multiply their densities, so full densities are the partition sums
used above to define the residuals. Substitution proves all identities.
This also establishes absolute continuity of all finite-order factorial
measures; higher orders use blocks of size at most four.

## 2. Pair--triangle result with an explicit dimensionless threshold

Drop the fourth-order identity and use $F_3=q_3$, $F_2=q_2-\mathcal M q_3$, with the same I,B,
a2,a3. Add singleton rate rho^2 L+Q3/2. The E2,E3 bounds suffice by the
same proof. It still gives finite local exponential moments, including a
finite fourth moment, although no reciprocal-volume identity is asserted.

For P=M write t=rho M^3. Then

\[
E_2=2\pi t,\qquad E_3=8\pi^3t^2+12\pi^2t.
\]

A sufficient threshold is

\[
0<t\le t_*=
{\sqrt{9\pi+1}-3\sqrt\pi\over4\pi^{3/2}}
\simeq0.00418503.
\]

For the all-orders theorem with P=M and eta=H/M, write
J=log(1/eta)-(1-eta^2)/2. Its additional bound is

\[
E_4=J[64\pi^4t^3+192\pi^3t^2+(48\pi^2+32\pi)t]\le1/2.
\]

These bounds are sufficient and are not claimed optimal.

## 3. Unbounded-scale impossibility

For k=2,3,4, a stationary locally finite process with 0<rho<infinity cannot
have its entire kth factorial moment measure represented by the Lebesgue
density $m_k=a_k/\Delta_k$, $a_k>0$, on the following domain: for k=2,
all pairs with distance exceeding any fixed finite lower threshold; for k=3
or k=4, all nondegenerate tuples whose minimum vertex altitude exceeds any
fixed finite absolute lower threshold, with no upper diameter constraint.
No additional singular part is allowed on this domain. Here Delta2=D, Delta3=A,
Delta4=V. No finite local kth moment is needed for this assertion.

Take a fixed bounded cube B of positive volume and p=P{X(B)>0}>0. Given n,
choose centres ci=(i,i^2,i^3), i=1,...,n, and boxes Bi=Tci+B. Every subset
of k centres is nondegenerate. For fixed n, taking T large makes all
corresponding simplex contents and altitudes uniformly large. Thus the
integral of m_k over any product of k distinct boxes is at most p^k/2.
Their occupancy indicators Ii consequently have E product Ii<=p^k/2.
For S=sum Ii, stationarity and Jensen give

\[
(np)^k\le E S^k\le(n)_k p^k/2+n^k-(n)_k.
\]

Dividing by n^k and letting n increase is a contradiction. The same proof
excludes uniform decay to zero on these scaled families. It does not address
every sparse or specially selected unbounded shape domain.

Thus some large-scale restriction or modification of the exact full law is
necessary. A sharp upper cutoff M is one choice, not itself a uniquely necessary
geometric form; the process is not required to have bounded spatial extent.
This statement concerns full densities, not connected correlations tending
to zero.

## 4. Flattening and fourth moments

If all nondegenerate tetrahedra of diameter<=M are admitted, fix an open
positive-measure family of noncollinear bases and in-plane apex coordinates,
and let the apex height satisfy 0<|u|<epsilon. Choose the family in one bounded
window, with base areas bounded above and below. The identity m4=a4/V gives
an integral proportional to integral du/|u|=infinity. It contradicts
$\mathbb E[(X(W))_4]<\infty$, where $(n)_4=n(n-1)(n-2)(n-3)$. Local finiteness alone does not imply that moment condition.

No corresponding obstruction applies to triangles in R3: the transverse
measure about a line is r dr dtheta and 1/A is proportional to 1/r.
The construction in section 1 is stronger evidence than integrability alone:
it supplies an actual point process with the full triangle identity.

Removing the fourth-moment assumption while retaining exact full
m4=a4/V everywhere on the finite diameter domain is not resolved by these
arguments.

## 5. An explicit diagnostic example with infinite fourth moments

This example has an inverse-volume *fourth factorial cumulant*, not the full
fourth density. It is not a solution of the full reciprocal-simplex problem.
It shows that the singularity itself is compatible with a simple stationary
locally finite process and finite first three local count moments.

In fixed coordinate units let a(v)=1+|v|^2, v in R3. Let N be a Poisson random
measure on R3 x R with intensity a(v)^(-4) dv db, and define the random field

\[
\Lambda(x)=\int a(v)\exp(-(v\cdot x-b)^2)\,N(dv,db).
\]

Its mean is finite:

\[
E\Lambda(x)=\sqrt\pi\int_{\mathbb R^3}a(v)^{-3}dv
=\pi^{5/2}/4.
\]

Consequently it is locally integrable almost surely by Tonelli. Conditional
on this field, take a Poisson process with intensity Lambda(x)dx. This is a
simple locally finite Cox process with positive finite intensity. Translating
x shifts b by v dot translation, preserving the mark intensity; rotations
preserve |v|, so the law is stationary and isotropic.

The factorial cumulant densities are

\[
c_k(x_1,\ldots,x_k)=\int a(v)^{k-4}
\exp(-\sum_i(v\cdot x_i-b)^2)\,dv\,db,\qquad k\le4.
\]

For four affinely independent points the 4 by 4 matrix with rows (xi,-1)
has absolute determinant 6V. A linear change of four variables therefore gives

\[
c_4=\frac{\pi^2}{6V}.
\]

For a ball W of radius R define JW(v,b)=integral_W exp(-(v dot x-b)^2)dx.
It obeys JW<=CR min(1,1/|v|) and integral JW db=sqrt(pi)|W|. Hence the
kth cumulant of the random mass integral_W Lambda, for k=1,2,3, is finite:
its radial tail is bounded by a constant times
r^2 r^{2(k-4)}r^{-(k-1)}=r^{k-5}. The Poisson-integral moment formulas give
finite first three moments of the random mass and thus of the Cox count.
At k=4 the inverse-volume calculation forces infinite local fourth moments
for windows containing an open family of nearly coplanar configurations.

The full m4 adds c4 to the positive contributions of every partition with
smaller blocks. Dropping those terms would invalidate the claimed full law.

## Decision record and sources

The extended finite-cluster argument removes delta and h, with H fixed.
It changes the domains; it does not retain the old numerical simulation
results for the new model. The conclusions above are analytical.

For standard Poisson ingredients, checked 20 October 2026: Last and Penrose,
*Lectures on the Poisson Process*, Corollary 4.10 (Poisson factorial moment
measure), Exercise 5.6 (cluster construction), and Chapter 13 (Cox processes):
https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf .
These references support the probabilistic ingredients, not a literature
priority claim for the cutoff results. The concrete arguments are supplied here.

Model: coordinator selected as Astra by owner; exact runtime effort and token
usage are not exposed. This submission contains mathematical proofs and
decision summaries, not private deliberation.
