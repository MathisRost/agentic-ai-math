# Approach 5 — Try to prove non-existence

Investigate necessary conditions and obstructions for the exact problem. The
goal is to test the claim honestly, not to force a negative answer. First read
the shared exact finite-cluster manuscript: a valid construction at some
intensity would defeat a claim that no process exists at any intensity, while
leaving the arbitrary prescribed-intensity question to analyse.

Write every negative theorem with explicit quantifiers. To refute the general
target, exhibit admissible prescribed parameters for which no qualifying process
exists. A theorem limited to a DPP, a particular cluster distribution or an
extra mixing assumption is a class-specific result.

Possible routes include count-moment positivity, realizability inequalities,
compatibility across orders, and local integrability. For a bounded window W,
the covariance/variance condition includes the diagonal contribution:

\[
\operatorname{Var}X(W)=\lambda_0|W|
+\int_{W^2}(\rho^{(2)}(x,y)-\lambda_0^2)\,dx\,dy\ge0.
\]

Do not assume unspecified correlations outside the finite domains. The pair
singularity 1/D is locally integrable in three dimensions; its divergence at a
point alone is not an obstruction. Likewise, an unrestricted 1/V law can fail
local integrability through flattening, but the current tetrahedron domain has
the positive altitude cutoff h_4. An obstruction obtained by removing that
cutoff does not refute the assigned target.

Check whether the prescribed intensity, domain and lower-order densities impose
incompatible bounds on the positive constants. Those constants are outputs,
not independently fixed numbers. A proof must cover all choices of them in the
claimed excluded regime. Do not infer a global mixing limit from the finite
diameter condition.

If no general obstruction emerges, give the strongest proved necessary condition,
its exact class/domain, and why the general question remains unresolved by your
argument. Finding no contradiction is not a proof of existence or novelty.
Starting material: `common/literature/05_obstructions.md`, the exact manuscript's
obstruction section, and the primary sources checked by the literature agent.
