# Approach 2 — Cox process

**Motivation supplied by the owner:** Cox processes turn the full factorial
moment problem into a moment problem for one stationary random directing
measure.  If \(X\mid\Lambda\) is Poisson with diffuse, locally finite random
measure \(\Lambda\), then

\[
\alpha_X^{(n)}=\mathbb E\Lambda^{\otimes n},\qquad 1\le n\le4.
\]

Investigate whether a stationary directing measure can realise the three exact
reciprocal densities simultaneously at every prescribed intensity.  Treat both
absolutely continuous random intensity fields and diffuse singular geometric
carriers as admissible candidates.  Do not assume that a density exists merely
because \(\Lambda\) is well defined: prove absolute continuity of
\(\mathbb E\Lambda^{\otimes n}\) through order four.

Inspect the spherical Cox manuscript first.  It gives a stationary, isotropic
process at independently prescribed intensity, but its theorem is an arbitrary
relative approximation on resolved domains rather than the governing exact
identity.  Determine precisely which limiting or inversion step would be needed
to make it exact, and whether that step preserves local fourth moments,
simplicity and the fixed physical domains.

Explore general Cox moment constraints as well as constructions.  In
particular, every proposed density hierarchy must come from the moments of one
nonnegative random measure, so test positivity of
\(\mathbb E(\int f\,d\Lambda)^k\), mixed-moment matrices, and consistency under
marginal integration where applicable.  For log-Gaussian Cox processes, check
the product identity \(g_n=\prod_{i<j}g_2(x_i,x_j)\) and determine its exact
scope.  For shot-noise or random-carrier models, include every carrier/parent
partition at orders three and four rather than retaining only the same-carrier
term.

A valid outcome may be an exact construction, a precise obstruction for a
clearly defined Cox subclass, or an explicit unresolved directing-measure
moment problem.  Do not turn failure of log-Gaussian, spherical, or shot-noise
Cox models into non-existence for all Cox processes.

Starting material: `common/literature/04_cox.md`, the spherical manuscript under
`common/prior_work/reciprocal-simplex/`, and the frozen literature agent's Cox
source section.
