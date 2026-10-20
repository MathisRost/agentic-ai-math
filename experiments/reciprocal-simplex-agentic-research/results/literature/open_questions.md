# Open source and mathematical questions

These are unresolved obligations after the bounded literature check.  They are
not claims that the governing problem is open in the literature.

## Highest priority for Approach 2 (Cox)

1. **Does there exist a stationary diffuse random measure with the three exact
   moment densities?**  The Cox identity reduces the target to constructing
   `Lambda` such that `E Lambda^⊗n` has the prescribed normalized densities for
   `n=2,3,4`, with finite fourth local moments.  No checked source supplies such
   a random measure.  A proposal must verify the full moments, including all
   carrier partitions, not only same-carrier Jacobians.

2. **Can the spherical carrier model be altered exactly rather than taken to a
   singular limit?**  The finite-`L` common-sphere terms contain the curvature
   factors `L^2-D^2/4` and `sqrt(L^2-R_3^2)`, while the full moments contain
   positive multi-sphere terms.  Is there a positive distribution of radii,
   weights or dependent carriers that removes both effects simultaneously on
   the full domains?  Any proposed signed cancellation is inadmissible unless
   it is realized by a nonnegative random measure.

3. **Can a Cox directing measure reproduce the finite-cluster residual
   cancellation?**  The exact local finite-cluster construction uses
   alternating marginal inversion to obtain nonnegative cluster kernels.  It is
   not known from the checked material whether its law is Cox, infinitely
   divisible as a point process, or embeddable in a Cox family.  Establishing
   such a representation could combine exact cancellation with Cox intensity
   scaling; failure of Cox infinite divisibility would rule out that bridge.

4. **Use the Cox-specific intensity scaling immediately if an exact witness is
   found.**  If `Lambda` works at one positive intensity, multiplying it by a
   deterministic constant realizes every prescribed `lambda_0` without
   changing `g_n`.  Therefore Cox work should focus on exact geometry and
   positivity, not retune intensity separately.

5. **Check truncated moment positivity beyond single windows.**  The matrices
   formed from `E Lambda(B)^k` must be positive semidefinite for every bounded
   `B`, and mixed versions must hold for several test functions.  The pair law
   already forces `C_2>=5M/12` by using a ball of radius `M/2`.  Can mixed
   test-function choices use only configurations inside the specified
   triangle/tetrahedron domains and yield further constraints on
   `C_2,C_3,C_4`?  Tests may not assume values on excluded shapes.

6. **Survey non-Gaussian Cox subclasses only if their higher moments are
   explicit.**  Ordinary LGCPs are excluded by
   `g_n=prod_{i<j}g_2(x_i,x_j)`.  Potentially relevant remaining classes include
   permanental Cox processes, non-Gaussian transformed fields, completely
   random measure convolutions, and dependent shot-noise carriers.  A useful
   source must expose third and fourth product densities, not only `g_2`.

## Poisson-cluster questions

7. **Remove the positive pair cutoff in the exact finite-cluster construction.**
   Its current anchored integrals use `delta>0`.  Because `1/D` is locally
   integrable in three dimensions, the cutoff is not forced merely by second
   moments.  Which particular marginal bounds or positivity estimates fail as
   `delta` decreases to zero, and can they be replaced by sharp integrable
   estimates?

8. **Decouple intensity from residual-kernel positivity outside the Cox
   class.**  The exact finite-cluster theorem chooses `rho=aI` with small `a`.
   Superposition changes normalized higher product densities, and ordinary
   thinning preserves `g_n` but can only reduce intensity.  Is there a cluster
   operation that raises intensity while preserving all three normalized laws,
   or is there a realizability bound preventing it?

9. **Locate a four-order inverse cluster theorem, if one exists.**  The checked
   KLS and Caglioti--Kuna--Lebowitz--Speer sources treat pairs and limited
   triplet information.  A theorem for simultaneous prescribed full densities
   through order four with explicit positivity/moment hypotheses would be
   decisive; none appeared in the bounded search.

## Hawkes/ETAS questions

10. **Specify the spatialization operation before using Hawkes formulas.**  Is
    the desired catalogue a fixed-time slice, a finite-window projection, or
    a time-stationary spatial marginal?  For the chosen operation, derive the
    spatial full product densities by integrating the space-time products and
    retain all set partitions.

11. **Find kernels giving exact integrated simplex laws.**  The verified Hawkes
    literature gives branching cumulants as sums over trees.  No source was
    located whose temporal integrations collapse those sums to simultaneous
    exact `1/D,1/A,1/V` spatial products.  Stability, finite fourth cluster
    moments and spatial absolute continuity must be checked together.

## Other constructions and nonexistence

12. **Do not revisit ordinary LGCP or Hermitian DPP constructions without
    changing the class.**  LGCP higher products are forced products of `g_2`;
    DPPs have `g_2<=1`, while the target diverges near zero.  These are exact
    subclass obstructions.

13. **A Gibbs existence theorem is not an inverse-correlation theorem.**  A
    geometry-dependent potential may define a stationary Gibbs process, but
    environmental partition-function factors remain in every correlation.
    Progress needs an exact solution of the relevant Kirkwood--Salsburg/DLR
    correlation hierarchy, or a proved inverse theorem with the current
    domains and arbitrary intensity.

14. **Exploit the finite domains in any nonexistence proof.**  The known
    flattening obstruction is neutralized by `h_4>0`, and infinite-range
    occupancy obstructions are neutralized by finite `M`.  A valid obstruction
    must use only the values fixed by the problem.  In particular it cannot
    extend `1/D`, `1/A` or `1/V` beyond the prescribed domains.

15. **Clarify whether the triangle and tetrahedron domains can be empty for
    extreme cutoffs.**  If a domain is empty, its identity is vacuous.  Proofs
    and obstructions should separate those cases from the nonempty positive-
    measure regime rather than silently assume regular simplices fit.

## Source-access follow-ups

16. The full Hawkes--Oakes (1974) article, Møller's *Shot noise Cox processes*
    (2003), and the line/tessellation Cox chapter were not needed for a decisive
    theorem here and were not all checked at theorem level.  Retrieve them only
    for a specific formula or hypothesis; their abstracts do not establish the
    reciprocal identities.

17. A focused primary-source search for permanental and other explicit
    non-Gaussian Cox `rho_3,rho_4` formulas could materially improve the Cox
    comparison.  The search should stop unless those formulas are explicit
    enough to test the area and volume shape dependence.

18. If a purported exact match is found, compare all quantifiers before
    promotion: one process; full factorial densities; all three orders; almost
    every configuration in the exact physical domains; every prescribed
    admissible parameter tuple; exact positive intensity; simplicity,
    absolute continuity and finite fourth local moments.
