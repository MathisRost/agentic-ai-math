# Exact full laws on a domain containing arbitrarily flat tetrahedra

Revised supplement v02, 20 October 2026. The independent review's existential
pairing correction and constant-diameter example are incorporated below.
This changes the geometric domain explicitly. It does not assert the
fourth-order law on every nondegenerate tetrahedron of diameter at most M.

## The domain

For four vertices define

\[
e(x_1,x_2,x_3,x_4)=
\min_{ij|kl}\|x_i+x_j-x_k-x_l\|,
\]

where the minimum ranges over the three partitions into two pairs. This is
translation invariant, rotation invariant and symmetric in the four vertices.
It is zero when one pairing of the four vertices has the same midpoint
(a possibly degenerate parallelogram). Define

\[
U_4=\{V>0,\ d_{\max}\le M,\ e^2\le M h_4\}.
\]

The pair and triangle domains are still S2={0<D<=P}, P>=M, and
S3={A>0,dmax<=M}, without lower cutoffs.

**Claim.** For every M>0 and P>=M, and for every sufficiently small prescribed
rho>0, there is a stationary isotropic simple point process with finite local
exponential moments and exact full laws m2=a2/D on S2, m3=a3/A on S3 and
m4=a4/V on U4. The coefficients are fixed positive constants. This is the
coordinator finite-cluster theorem with the geometric marginal constant
C=18*pi*M^2. The precise sufficient intensity conditions are its E2,E3,E4<=1/2.

The domain U4 has positive measure and includes tetrahedra of fixed nonzero
diameter with h4/dmax tending to zero. Thus there is no uniform positive
absolute or relative lower tetrahedral altitude.

## Marginal estimate

Fix a noncollinear base x1,x2,x3 with area A. Write the fourth vertex as its
in-plane projection p and signed height u. Then V=A|u|/3 and h4<=|u|.

For at least one of the three pairings in e, the inequality e^2<=M h4
requires the fourth point z to lie within distance sqrt(M h4) of the
corresponding point in the following list

\[
x_1+x_2-x_3,\qquad x_1+x_3-x_2,\qquad x_2+x_3-x_1.
\]

All three lie in the base plane. Therefore, at any fixed nonzero signed
height u, the allowed in-plane projections lie in a union of three discs of
radius at most sqrt(M|u|). Their total area is at most 3*pi*M*|u|.
The diameter restriction implies |u|<=M. It follows by Tonelli that

\[
\begin{aligned}
\int {1_{U_4}(x_1,x_2,x_3,z)\over V(x_1,x_2,x_3,z)}\,dz
&\le {3\over A}\int_{-M}^{M}{3\pi M|u|\over |u|}\,du\\
&={18\pi M^2\over A}.
\end{aligned}
\]

The marginal is zero off S3 because every face of a nondegenerate tetrahedron
of diameter at most M is a noncollinear triangle of diameter at most M.
Thus $\mathcal M K_4\le C K_3$ with $C=18\pi M^2$. The proof of positivity, actual cluster
kernels, finite integrals, exact intensity and full parent partitions in the
coordinator submission applies without any other change.

## Positive measure and flattening at fixed diameter

Fix a desired diameter $0<R_0<M$. For $0<u<R_0$ set
$s=s(u)=\sqrt{(R_0^2-u^2)/2}$ and take the four vertices

\[
x_1=(0,0,0),\quad x_2=(s,0,0),\quad
x_3=(0,s,0),\quad x_4=(s,s,u),\qquad u>0.
\]

Here

\[
V=s^2u/6,\qquad
d_{\max}=\sqrt{2s^2+u^2}=R_0,\qquad
h_4={u\over\sqrt{1+2u^2/s^2}}.
\]

For the pairing 14|23 the vector sum difference is (0,0,u), so e<=u.
For all sufficiently small u>0, the diameter is strictly below M and

\[
e^2\le u^2
< {M u\over\sqrt{1+2u^2/s^2}}
=M h_4.
\]

Thus each such tetrahedron has an open neighbourhood in U4, and U4 has
positive measure. As $u$ decreases to zero, its diameter remains exactly
$R_0>0$ while $h_4/d_{\max}$ tends to zero. All four face areas tend to
$R_0^2/4>0$.
This is actual flattening, not merely a shrinking regular tetrahedron.

## Why there is no contradiction

At height u the permitted in-plane area shrinks at least as fast as |u|
in the upper bound above, cancelling the 1/|u| factor. The unrestricted
finite-diameter domain admits a fixed positive in-plane area at all small
heights and gives a divergent logarithmic integral instead.

U4 is a selected family of flat shapes, tending towards parallelograms.
It does not contain all arbitrary coplanar-limit shapes. The construction
therefore disproves necessity of a literal positive H for *every possible
admissible domain*, while leaving the non-existence result for the complete
diameter-bounded domain with finite fourth moments intact.
