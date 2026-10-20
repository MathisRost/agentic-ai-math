# Approach 1 — Poisson cluster process

**Motivation supplied by the owner:** independent clusters can simplify the
construction and calculations. Clusters are independent of one another; points
inside a cluster may be dependent and need not be i.i.d.

Seek the exact target in `common/problem_statement.md`. Start with a homogeneous
Poisson parent process and i.i.d. finite random clusters, independent across
parents. Specify whether the parent is included as an observed point. Allow a
dependent internal cluster law if it helps encode distances, areas and volumes.

For parent intensity \(\kappa\) and cluster \(C\), justify
\(\lambda_0=\kappa\mathbb E|C|\). If \(q_r\) denotes an appropriate cluster
factorial density, the connected contribution has the form

\[
c_r(x_1,\ldots,x_r)=\kappa\int q_r(x_1-z,\ldots,x_r-z)\,dz.
\]

Check the density and integrability assumptions; anchored/surface clusters may
need measure-level formulas before averaging. The full density is the partition
sum \(\rho^{(n)}(x_1,\ldots,x_n)=\sum_{\pi}\prod_{B\in\pi}c_{|B|}(x_B)\).
In particular, \(\rho^{(2)}=\lambda_0^2+c_2\). Explicitly account for the
1, 2, 5 and 15 partitions at orders 1–4. The same-cluster term alone is not
the target.

Inspect the dependent finite-cluster manuscript first: it claims exact laws,
but chooses intensity with its amplitudes. Determine whether parameter choices,
scaling or a new cluster law can attain any prescribed intensity on the fixed
domains. Prove positivity and normalisation of a proposed cluster law; reverse
engineering formal cumulants without such a law is not enough.

Explain any tension between compensating cross-cluster terms and keeping cluster
densities nonnegative. For thinning/superposition arguments derive the resulting
full hierarchy rather than asserting preservation. Include local moment control.
An exact construction for a restricted intensity range or a proved obstruction
within a subclass is useful, but label its scope precisely.

Starting material: `common/literature/02_poisson_cluster.md`, the exact manuscript,
and the shared literature agent's checked partition/existence results.
