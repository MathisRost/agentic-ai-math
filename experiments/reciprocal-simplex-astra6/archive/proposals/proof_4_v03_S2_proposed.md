# S2-P4-proposed — exact reciprocal-simplex identities on a prescribed low-intensity range

**Conditional proposal only. Not adopted, not broadcast as a target, and not an S1 pass.**

## Quantifiers and process class

Put
\[
 J=\frac{\pi^2}{4},\qquad Z_0=\frac{\pi^2}{4}+\frac{2\pi}{3},\qquad
 \tau=\min\left\{\frac{1}{36e\pi},\;\frac{J^2}{8\pi^2Z_0},\;\sqrt{\frac{J^3}{32\pi^4Z_0^2}}\right\}>0.
\]
For every prescribed pair $\lambda_0>0$ and $M>0$ satisfying
$\lambda_0M^3\leq\tau$, does there exist one stationary, simple,
locally finite point process $X$ on all of $\mathbb R^3$ such that
\[
\mathbb E X(B)=\lambda_0|B|
\]
for every bounded Borel set $B$, together with constants
$a_2,a_3,a_4\in(0,\infty)$ satisfying the requirements below?

The process and constants may depend on both $\lambda_0$ and $M$. The
constants may not depend on a point configuration. Stationarity means
invariance in law under all translations. Local finiteness means
almost-sure finiteness of counts on bounded sets. No mixing, ergodicity,
isotropy, particular process representation or finite fourth count moment
is assumed.

## Full factorial expectation measures

For $n=2,3,4$ and nonnegative measurable $f$, define
\[
\int f\,d\alpha^{(n)}
=\mathbb E\sum_{x_1,\ldots,x_n\in X}^{\ne}
 f(x_1,\ldots,x_n).
\]
Tuples are ordered and pairwise distinct. Require nonnegative measurable
densities $\rho^{(n)}$, finite Lebesgue-almost everywhere on
$(\mathbb R^3)^n$, with the full measure identities
\[
\alpha^{(n)}(d\mathbf x)=\rho^{(n)}(\mathbf x)\,d\mathbf x.
\]
These are identities of extended nonnegative measures. Integrals over
bounded configuration sets and higher count moments may be infinite.
There is no singular component anywhere, including on degenerate
configurations or outside the domains where formulas are prescribed.

## Geometry and exact formulas

Put
\[
D(x_1,x_2)=\|x_2-x_1\|,\qquad
A(x_1,x_2,x_3)=\frac12\|(x_2-x_1)\times(x_3-x_1)\|,
\]
\[
V(x_1,x_2,x_3,x_4)
=\frac16\left|\det[x_2-x_1,x_3-x_1,x_4-x_1]\right|,
\qquad
(\Delta_2,\Delta_3,\Delta_4)=(D,A,V).
\]
For each $n=2,3,4$, let
\[
E_n(M)=
\left\{\mathbf x:
\max_{1\leq i<j\leq n}\|x_i-x_j\|<M,\quad
\Delta_n(\mathbf x)>0
\right\}.
\]
The required simultaneous identities are
\[
\boxed{\rho^{(n)}(\mathbf x)=\frac{a_n}{\Delta_n(\mathbf x)}
\quad\text{for Lebesgue-almost every }\mathbf x\in E_n(M),
\qquad n=2,3,4.}
\]
No positive lower distance, area, volume or altitude threshold is imposed.
All nondegenerate shapes with diameter less than $M$ are included.
Outside $E_n(M)$ the full densities are unprescribed, subject to the
global measure and process requirements above. Values on Lebesgue-null
sets may be chosen arbitrarily without adding singular mass.

The densities are full factorial densities. They are not connected
densities, factorial cumulants, same-parent densities or asymptotic
expressions. All partitions and parent allocations must be included in
any construction.

## Separate moment comparison and acceptance

The additional condition $\mathbb E X(B)^4<\infty$ for every bounded Borel
$B$ defines a separate comparison question. It is not a requirement of this proposed target.

A construction must meet every prescribed pair $(\lambda_0,M)$ satisfying
$\lambda_0M^3\leq\tau$ and all three domains simultaneously. A result for a
properly smaller parameter range, a smaller shape domain, or approximate or
connected densities is partial progress relative to this proposed target.
Rescaling must preserve the stated intensity and geometry quantifiers together.

This proposed target is weaker than S1: it excludes every pair with
$\lambda_0M^3>\tau$. The restriction is a sufficient range of a known
construction, not a proved necessary restriction for S1. Success for this
proposed target would not prove S1 or change the false verdict for unrestricted
S0. Adoption requires explicit owner approval, recording and broadcast;
until then S1 remains active. The original four-submission allowance does
not reset.
