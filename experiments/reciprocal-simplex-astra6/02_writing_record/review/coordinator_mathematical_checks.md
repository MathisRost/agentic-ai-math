# Coordinator checks

These checks supplement the frozen historical review and the forthcoming independent exposition reading. They are not a formal proof certificate.

## Manuscript additions

The new short S0 argument uses the second density only. Its integral over a ball pair is bounded by $8\pi a_2 R^2|B_R|$, so the second count moment is finite. The variance inequality then contradicts quadratic mean-count growth for large $R$. No finite fourth moment is imported.

The additional explicit nonergodicity statement follows from the invariant event that the whole configuration is empty. The sphere branch gives it positive probability, while positive intensity prevents probability one. The underlying process remains locally finite and of positive ensemble intensity.

The correction proof preserves the anchored marginal $F_2=q_2-\mathcal Mq_3$, factors $2$ and $6$ for ordered cluster selections, and $\lambda_C=\beta+Z_2+Z_3/2$. Its global absolute continuity follows by domination by the full unthinned Poisson cluster process, including all parent partitions. The appendix retains the all-allocation rank calculation and the separate finite-band argument outside the polynomial exceptional set.

## Numerical estimator, code inspection

Inspected the initial complete `coder/code/experiment.py` and its reported results. For an anchored sphere tuple, the radial factorial measure is

\[
4\pi R^2\gamma(R)\left(\frac{a(R)}{2R}\right)^n S(R)^{n-1}\,dR,
\qquad S(R)=\pi\min(1,4R^2)
\]

at $M=1$. The cap sampler generates independent surface-area points relative to the anchor. Division by the code's radial proposal densities gives $2A_2S$ for pairs and $4\pi A_3S^2$ for triples. For quadruples, the proposal proportional to $64R^5$ below $1/2$ and $1/R$ above it, ending at $R_{\max}=2$, gives the constant weight
$\pi^4c[1/6+\log(2R_{\max})]/2$. These agree with the implementation. The fourth-order reference integral includes the same circumradius guard.

The cylindrical proposal for the triple residual has envelope mass $T=16\pi^2A_3J$, $J=2\varepsilon-\varepsilon^2$ at $M=1$, and rejection factor $q_3/E$. The augmented pair rejection has conditional probability $q_3/(q_2h)$; averaging the auxiliary variable gives the required marginal subtraction. Its pointwise upper bound is at most $1/2$. This avoids treating numerical quadrature as an exact marginal law.

The triple contribution to a pair bin averages all three edges. Symmetry and re-rooting justify the factor $1/3$. The code first sums those contributions within each sampled triple, retaining their dependence in the empirical variance. Sphere, pair-mark, triple-mark and reference streams are distinct. Delta-method errors for the ratio to theoretical bin averages include the independent reference integral error; the covariance between the two reference integrals is included where required.

The main estimate uses sampled factorial tuples and cluster marks with explicit weights, not ordinary point-process realisations. This distinction must remain visible in the manuscript and figures. Positive geometric bin bounds and the fourth-order circumradius guard define finite numerical estimands without changing the existence theorem.
