# A relative tetrahedral cutoff instead of a fixed altitude

Frozen supplement to coordinator_submission_v01.md for independent review.

Fix M>0 and 0<eta<sqrt(2/3). Replace S4 in the coordinator theorem by

\[
T_4=\{V>0,\ R=d_{\max}\le M,\ h_4\ge\eta R\}.
\]

Keep S2={0<D<=P}, P>=M, and S3={A>0,dmax<=M}.
The same finite-cluster construction proves all three exact full reciprocal
laws at every sufficiently small prescribed positive intensity. No positive
absolute lower pair distance, triangle altitude, or tetrahedron altitude
is imposed. The restriction here excludes relatively flat tetrahedral shapes;
it admits arbitrarily small tetrahedra of any fixed permitted shape.

To justify the construction, only the omitted-vertex bound changes. Fix a
noncollinear base of area A and diameter d>0. If an extension belongs to T4,
each base-triangle altitude is at least h4: the opposite base edge lies in the
opposite tetrahedron face plane, and distance to a subset is at least distance
to its containing plane. Hence h4<=d. Writing R for the extended tetrahedron's
diameter and u for its signed apex height, we obtain

\[
R\le d/\eta,\qquad |u|\ge h_4\ge\eta R\ge\eta d.
\]

The apex lies in B(x1,d/eta). Its planar cross-section has area at most
pi(d/eta)^2. Consequently

\[
\int {1_{T_4}(123z)\over V(123z)}\,dz
\le {6\pi\over A}(d/\eta)^2
       \int_{\eta d}^{d/\eta}{du\over u}
\le {C_\eta\over A},
\qquad
C_\eta={12\pi M^2\over\eta^2}\log(1/\eta)<\infty.
\]

The integral is zero outside S3. Replace C by C_eta in all amplitudes and
positivity conditions of the coordinator submission. Every subsequent
inequality and intensity calculation is unchanged. A regular tetrahedron of
side s<M has h4/R=sqrt(2/3)>eta, so T4 has positive measure and Z4>0.

This proves that a fixed positive H is not the only way to obtain an exact
fourth-order law with finite fourth moments. It does not permit every
nondegenerate tetrahedron of diameter<=M, nor arbitrary relative flattening.
The obstruction to that unrestricted domain remains valid.
