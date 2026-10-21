# Verified source notes for the manuscript

Checked 21 October 2026. Scope: the supplied primary PDFs, the frozen sphere-source follow-up, one targeted Undermind metadata lookup, and direct publisher/arXiv verification. No novelty or current-open-status search.

| Claim | Source and location | Support and limit |
|---|---|---|
| Approximate inverse-distance law motivated by earthquake hypocentres | Y. Y. Kagan and L. Knopoff (1980), *Spatial distribution of earthquakes: the two-point correlation function*, Geophys. J. R. astr. Soc. 62, 303–320, DOI 10.1111/j.1365-246X.1980.tb04857.x. Supplied PDF p.303 (index 0), summary and introduction. | Empirical comparison, especially shallow earthquakes; not an exact all-scale mathematical identity. |
| Approximate reciprocal triangle area | Y. Y. Kagan (1981), *Spatial distribution of earthquakes: the three-point moment function*, 67, 697–717, DOI 10.1111/j.1365-246X.1981.tb06948.x. Supplied PDF p.697 (index 0). | Ratio of observed triangle counts to a Poisson comparison catalogue with matching boundaries/depth distribution. Primary PDF and publisher page agree. |
| Approximate reciprocal tetrahedron volume and degeneracy concern | Y. Y. Kagan (1981), *Spatial distribution of earthquakes: the four-point moment function*, 67, 719–733, DOI 10.1111/j.1365-246X.1981.tb06949.x. Supplied PDF pp.719, 729–730 (indices 0,10,11). | Empirical model; p.730 explicitly discusses divergent integral in tetrahedral height and a lower-height regularisation. Our extended factorial measure convention is a distinct mathematical choice. |
| Classical compatibility question | Daley and Vere-Jones (2008), Vol. II, second ed., Exercise 12.6.11, printed p.249, zero-based PDF index 265; preceding context printed p.244/index260. | Uses proportional/asymptotic notation, asks compatibility and approximate fractal constructions. Its historical unresolved-status remark does not establish present novelty or open status. |
| Spherical coordinate Jacobian | Aurélie Chapron, *A local Blaschke-Petkantschin formula in a Riemannian manifold*, arXiv:1807.07384v1 (2018), printed p.1, equation (1); directly re-opened https://arxiv.org/pdf/1807.07384. | Explicit Euclidean identity with surface area measure. It is attributed there to Miles (1970), formula (70); that original article was not directly audited. We use the Euclidean identity, not Chapron's Riemannian small-radius expansion. |

For ambient dimension three, the last formula reads

\[
d x_1\cdots d x_4=6\Delta_3(u_1,\ldots,u_4)R^8\,dz\,dR\,\prod_i d\omega(u_i)
=6V(x_1,\ldots,x_4)R^5\,dz\,dR\,\prod_i d\omega(u_i).
\]

Here $x_i=z+Ru_i$, and $d\omega$ is unnormalised area on the unit sphere. The sphere-process parameter measure contributes $\gamma(R)[a(R)/(2R)]^4R^8$. Dividing by the displayed Jacobian gives $\gamma(R)a(R)^4/(96RV)=c/(48V)$. Surface separation is separately required to identify this same-sphere contribution with the full local fourth density. This is a short deduction from a published geometric identity, not a published existence theorem for the final process.

The frozen proof derived the coarea calculation internally; the Chapron source was identified in a later follow-up. The manuscript must not claim that the construction was historically inspired by that paper.

Undermind workspace used: `<runtime-id>`, *Kagan reciprocal simplex models*. Known-paper lookup returned `Cha18`, `Kag80`, `Kag81`. Its `Kag81` record incorrectly calls DOI ...06948.x a four-point paper, and its author fields for Kagan are unreliable. The supplied primary PDFs and the publisher page https://academic.oup.com/gji/article/67/3/697/675522 resolve these errors. No erroneous connector metadata is adopted. No Undermind reading/deep-search agents were launched; the writing team consists of the requested writer, coder and reader only.

Metadata and source text are evidence for attribution; the complete construction is proved in the manuscript. No external theorem is used to replace a missing point-process realisation argument.
