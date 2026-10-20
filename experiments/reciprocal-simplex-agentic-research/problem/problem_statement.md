# Exact reciprocal-simplex problem

**Governing version: 19 October 2026.** The owner explicitly selected the exact
version. This document supersedes approximate targets and empirical acceptance
gates in the archived material for this workflow. It is an operational
mathematical question motivated by the literature, not a verbatim historical
conjecture or a claim that the question is unresolved in all existing work.

## Parameters and process

Given a prescribed intensity \(\lambda_0>0\), maximum diameter \(M>0\), and
altitude thresholds \(h_3,h_4>0\), seek one stationary, simple, locally finite
point process \(X\) on \(\mathbb R^3\) with intensity \(\lambda_0\), finite local
count moments through order four, and absolutely continuous factorial moment
measures through order four. Choose geometric parameters with nonempty
admissible domains; a nonvacuous density question requires domains of positive
Lebesgue measure.

Stationarity means invariance in law under translations. Isotropy is not a
requirement; it may be proved as an additional property of a construction.

For bounded Borel sets \(B\), write \(X(B)\) for the number of points in \(B\).
The ordered factorial moment measure is

\[
\alpha^{(n)}(B_1\times\cdots\times B_n)
=\mathbb E\!\sum_{x_1,\ldots,x_n\in X}^{\ne}
\prod_{i=1}^n\mathbf1\{x_i\in B_i\},
\qquad
\rho^{(n)}=\frac{d\alpha^{(n)}}{d(x_1,\ldots,x_n)}.
\]

Here \(\sum^{\ne}\) ranges over ordered, pairwise distinct points. Set
\(g_n=\rho^{(n)}/\lambda_0^n\). Superscripts \((n)\) indicate order.

## Geometry and domains

For pairwise distinct points, define

\[
D=\|x_2-x_1\|,\qquad
A=\frac12\|(x_2-x_1)\times(x_3-x_1)\|,
\]
\[
V=\frac16\left|\det[x_2-x_1,\ x_3-x_1,\ x_4-x_1]\right|.
\]

The determinant is of the matrix with the three edge vectors as columns.
Distances to opposite lines/planes below mean distances to their affine
extensions, not to the bounded side or face.

- \(\mathcal D_2=\{(x_1,x_2):0<D\le M\}\).
- \(\mathcal D_3\): noncollinear triples of diameter at most \(M\), for which
  each vertex has distance at least \(h_3\) from the opposite affine line.
- \(\mathcal D_4\): noncoplanar quadruples of diameter at most \(M\), for which
  each vertex has distance at least \(h_4\) from the opposite affine plane.

The triangle condition belongs to \(\mathcal D_3\). It is not an extra condition
on the faces of tetrahedra in \(\mathcal D_4\). There is no positive lower cutoff
on pair distance. The identities are not requested beyond diameter \(M\).

## Exact target

There must exist constants \(C_2,C_3,C_4>0\) such that, simultaneously,

\[
\boxed{\quad
g_2(x_1,x_2)=\frac{C_2}{D},\qquad
g_3(x_1,x_2,x_3)=\frac{C_3}{A},\qquad
g_4(x_1,x_2,x_3,x_4)=\frac{C_4}{V}.
\quad}
\]

Each equality holds Lebesgue-almost everywhere on its respective domain.
One process must satisfy all three equalities on all the prescribed scales
and shapes. The constants may depend on the process and prescribed parameters,
but not on the configuration. They are not independently prescribed inputs.

Equivalently, \(\rho^{(n)}=a_n/\Delta_n\), where
\((\Delta_2,\Delta_3,\Delta_4)=(D,A,V)\) and
\(a_n=\lambda_0^n C_n>0\). Using \(g_n\) or \(\rho^{(n)}\) with this rescaling
does not change the stationary existence question.

The general target is: **for every prescribed admissible tuple
\((\lambda_0,M,h_3,h_4)\), construct such a process or identify the precise
obstruction.** A theorem only at some intensities or for a smaller domain must
state that restriction and is partial progress. Scaling a construction is
acceptable only if the proof shows that all prescribed physical domains and
the target intensity can be met simultaneously.

## What does not establish this target

An arbitrarily accurate approximation, a finite numerical grid, or a construction
with intensity selected after the domain is fixed does not by itself prove the
stated exact theorem at prescribed intensity. Additional assumptions such as
mixing, isotropy, a minimum pair distance, or restricted shapes cannot be silently
added. A negative result for one process class is not general non-existence.

These are full densities. In particular, the off-diagonal covariance density is
\(c_2=\rho^{(2)}-\lambda_0^2\), which is a different object. For general bounded
\(B_1,B_2\),

\[
\operatorname{Cov}(X(B_1),X(B_2))
=\lambda_0|B_1\cap B_2|
+\int_{B_1\times B_2}(\rho^{(2)}(x,y)-\lambda_0^2)\,dx\,dy.
\]

Higher connected/factorial-cumulant densities likewise cannot replace the full
product densities. Independent clusters do not make all observed points
independent; tuples may come from several clusters.

Finite domain refers to where the identities are required, not to finite-range
dependence. A fit to earthquake observations is a separate optional study.

## Existing work to inspect first

Read `prior_work/README.md` and the two copied local manuscripts. The spherical
construction claims arbitrary relative approximation at prescribed intensity.
The dependent finite-cluster construction claims exact identities with intensity
and amplitudes chosen together. Check their actual theorems, transformations,
and assumptions before claiming either a new solution or a contradiction.
Neither manuscript's old review status is a new proof audit.

For the historical meaning of the densities, start with
`source_notes/definition_audit_2026_10_18.json` and the primary PDFs indexed in
`papers/INDEX.md`. The exercise and empirical papers do not themselves supply
all the quantifiers and cutoffs in this operational formulation.
