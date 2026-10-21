# S0 — unrestricted exact reciprocal-simplex existence question

Owner-approved starting statement, 20 October 2026. This version is immutable
once a run starts. It is a precise exact interpretation motivated by DVJ
Exercise 12.6.11, not its verbatim wording or a claim about current open status.

## Quantifiers and process class

For every prescribed number \(\lambda_0>0\), does there exist a stationary,
simple, locally finite point process \(X\) on \(\mathbb R^3\), with
\(\mathbb E X(B)=\lambda_0|B|\) for bounded Borel \(B\), and constants
\(a_2,a_3,a_4\in(0,\infty)\), satisfying the identities below simultaneously?

Stationarity is invariance in law under all translations. Local finiteness is
almost-sure finiteness of counts on bounded sets. No mixing, ergodicity,
isotropy, cluster representation or finite fourth count moment is assumed.
The constants are chosen with the process, not independently prescribed.

## Full factorial expectation measures

For nonnegative measurable \(f\), define the extended nonnegative measures by
\[
\int f\,d\alpha^{(n)}
=\mathbb E\sum_{x_1,\ldots,x_n\in X}^{\ne}f(x_1,\ldots,x_n),
\qquad n=2,3,4.
\]
Tuples are ordered and pairwise distinct. Require actual Lebesgue densities
\(\alpha^{(n)}(d\mathbf x)=\rho^{(n)}(\mathbf x)\,d\mathbf x\).
This is equality of the full measures, with no omitted singular component on
collinear/coplanar or other null sets. Local integrals and higher count moments
may be infinite; the process must nevertheless be locally finite almost surely.
An explicit measure identity is required, not merely formal functions.

## Geometry and exact identities

\[
D(x_1,x_2)=\|x_2-x_1\|,\qquad
A(x_1,x_2,x_3)=\tfrac12\|(x_2-x_1)\times(x_3-x_1)\|,
\]
\[
V(x_1,x_2,x_3,x_4)
=\tfrac16|\det[x_2-x_1,x_3-x_1,x_4-x_1]|.
\]

The target is
\[
\boxed{\rho^{(2)}=\frac{a_2}{D},\qquad
\rho^{(3)}=\frac{a_3}{A},\qquad
\rho^{(4)}=\frac{a_4}{V}.}
\]
The identities hold Lebesgue-almost everywhere on ALL configurations with,
respectively, \(D>0\), \(A>0\) and \(V>0\). No positive lower distance/altitude
threshold, upper diameter \(M\), or shape restriction is present in S0.
Values on Lebesgue-null degenerate sets may be chosen arbitrarily without
adding singular mass.

Equivalently \(g_n=\rho^{(n)}/\lambda_0^n=C_n/\Delta_n\), where
\((\Delta_2,\Delta_3,\Delta_4)=(D,A,V)\) and \(C_n=a_n/\lambda_0^n>0\).
These are full densities, NOT connected/factorial-cumulant densities.
For cluster constructions all partitions and parent allocations are required.

## Separate finite-moment question

Also record what happens in the subclass
\(\mathbb E[X(B)^4]<\infty\) for every bounded Borel \(B\).
This is a separate comparison to the usual boundedly finite moment-measure
convention in DVJ; it is NOT a hidden assumption of S0. Infinite fourth
moments alone do not contradict almost-sure local finiteness or finite intensity.

## Target revision and acceptance

The obstruction phase may establish that S0 is false. A reviewed general
obstruction can motivate a versioned replacement question, with exact domains,
moment conditions and quantifiers stated. It does not prove that a particular
replacement is necessary, sufficient, maximal or uniquely best.

Preserve S0 and distinguish its verdict from every later target. Do not drop
orders, replace equality by approximation, replace full densities by cumulants,
or relax prescribed intensity without explicit owner approval.
For any finite-domain replacement, specify whether geometry is prescribed
independently of intensity; a low-intensity construction on fixed domains does
not establish all prescribed intensities by rescaling unless the proof does so.

After three unsuccessful reviewed construction attempts, a precise proposed
amendment may be sent to the owner. Only explicit approval adopts it. Failure
to find a construction is not a non-existence proof.
