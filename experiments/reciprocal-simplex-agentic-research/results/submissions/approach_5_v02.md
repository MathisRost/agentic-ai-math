# Approach 5 — submission v02

- Run / model / reasoning: 20261019T114252Z_cox_rerun / gpt-5.6-sol / xhigh.
- Problem snapshot SHA-256: 4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a.
- Context packet and source dossier version: context_packets/proof_5_v02.md; frozen shared_literature/dossier.md, SHA-256 5d42ad11b6b55246e6a0eb098b3f09c1bf3751cd3add4a819f5e427017b659f5, checked 19 October 2026.
- Claim status: **restricted exact theorem plus a general necessary condition; the arbitrary-intensity target remains unresolved.**

## Claim and scope

Fix \(M,h_3,h_4>0\) such that the triangle and tetrahedron domains in the frozen problem have positive Lebesgue measure. The governing question asks, for every prescribed \(\lambda _0>0\), for one stationary simple process on all of \(\mathbb R^3\) having intensity \(\lambda _0\), finite local count moments through order four, absolutely continuous factorial moment measures through order four, and

\[
g_2=\frac{C_2}{D},\qquad g_3=\frac{C_3}{A},\qquad
g_4=\frac{C_4}{V}
\]

almost everywhere on the complete domains \(\mathcal D_2,\mathcal D_3,\mathcal D_4\). There is no lower pair-distance cutoff, and no identity is prescribed outside those domains.

I prove two results.

1. **Exact low-intensity theorem.** For every such \((M,h_3,h_4)\), there is a number \(\lambda _*(M,h_3,h_4)>0\) such that, for every prescribed \(0<\lambda _0\leq\lambda _*\), one stationary simple finite-cluster process satisfies all three exact identities on the full frozen domains. Its constants are positive outputs of the construction. Thus the positive lower pair cutoff in the earlier finite-cluster manuscript is not necessary for this construction. In particular, this theorem rules out the claim that no intensity admits a solution; existence and non-existence for prescribed intensities above \(\lambda _*\) remain unresolved.
2. **General pair-amplitude necessity.** Every solution at any prescribed intensity obeys local quadratic-form and integer-count inequalities involving only correlations at distances at most \(M\). In particular, with
   \[
   \mu=\frac{\pi\lambda _0M^3}{6},\qquad
   n=\lfloor\mu\rfloor,\qquad \theta=\mu-n,
   \]
   one has
   \[
   C_2\geq \frac{5M}{12}\,
   \frac{n(n-1)+2n\theta}{\mu^2}.
   \tag{1}
   \]
   The right side is zero when \(0<\mu<1\). A sharper version takes a supremum over all balls of radius at most \(M/2\), as stated below. Since \(C_2\) is not prescribed, this is a necessary amplitude condition, not a contradiction for any \((\lambda _0,M,h_3,h_4)\).

No claim below establishes existence for \(\lambda _0>\lambda _*\), or non-existence there. In particular, the governing quantifier “for every prescribed \(\lambda _0>0\)” is not proved.

## Relation to prior work

The frozen unpublished manuscript *Exact reciprocal simplex correlations on finite domains* proves a dependent finite-cluster theorem when the pair support is \(\delta\leq D\leq P\) with \(\delta>0\), and when intensity and amplitudes are selected together. The formulas reused here have the following precise locations in that source:

- Section “A finite-cluster construction” (sections/construction.tex, label sec:construction) defines the recursive same-parent kernels in equations q2–q4, the downward marginal inversion in equation Fkernels, and the Poisson parent rates, singleton rate, intensity calculation and full partition sums in the proof of Theorem thm:main.
- Appendix “Geometric bounds and positivity” (sections/appendix_bounds.tex, label app:bounds) proves the two marginal bounds in Lemma lem:marginal-bounds and the pointwise positivity bounds in Lemma lem:kernel-positive.
- Appendix “Cluster normalisation and parent partitions” (sections/appendix_partitions.tex, label app:partitions) derives the factor \(1/(j-r)!\), the identities \(b_1=\rho,b_2=q_2,b_3=q_3,b_4=q_4\), and the full set-partition formula.

All formulas needed here are stated and proved again below. I do not invoke the earlier theorem at \(\delta=0\), which lies outside its hypotheses.

The new steps here are:

- set the pair endpoint to \(\delta=0\) and check every integrability, positivity, normalisation, simplicity and density step rather than invoking the prior theorem as stated;
- use the internal triangle threshold \(h=\min(h_3,h_4)\), so every face needed in the fourth-order cancellation lies in the internal triangle support even though the frozen target imposes no triangle condition on tetrahedral faces;
- set \(P=M\) and solve \(a_2I=\lambda _0\), giving an independently prescribed intensity throughout a nonempty interval \(0<\lambda _0\leq\lambda _*\);
- derive (1), including the diagonal count contribution, without imposing correlations beyond distance \(M\).

The spherical Cox manuscript was also inspected in full. Its Sections 4–5 give exact common-sphere kernels and all \(2,5,15\) parent partitions, but only a uniform approximation theorem for the full densities. No finite parameter choice there gives the exact target.

The frozen literature dossier verifies the general factorial moment/cumulant partition identity and the scope of the realizability literature. The construction and endpoint extension below are proved directly; no source is used as an existence black box. The prior manuscript audit files are historical records of checks made on earlier manuscripts. They are not independent theorem support and are not used to fill any step of this proof.

## Process and existence

Put

\[
h=\min(h_3,h_4),\qquad H=h_4,
\]

and define nested internal supports

\[
\begin{aligned}
S_2&=\{(x_1,x_2):0<D\leq M\},\\
S_3&=\{(x_1,x_2,x_3):A>0,\ \operatorname{diam}\{x_i\}\leq M,\
h_{\min}\geq h\},\\
S_4&=\mathcal D_4.
\end{aligned}
\tag{2}
\]

Then \(\mathcal D_3\subseteq S_3\). Every edge of a supported triangle is in \(S_2\). Every triangular face of a tetrahedron in \(S_4\) lies in \(S_3\): the distance from a face vertex to its opposite edge line is at least its distance to the tetrahedron's opposite face plane, hence at least \(H\geq h\).

Positive-measure nonemptiness of \(\mathcal D_4\) entails
\(H<\sqrt{2/3}\,M\). Indeed, if \(c\) is the centroid of four points of diameter at most \(M\), then

\[
\sum_{i=1}^4|x_i-c|^2
=\frac14\sum_{i<j}|x_i-x_j|^2\leq\frac32M^2.
\]

For some \(i\), \(|x_i-c|\leq\sqrt{3/8}\,M\). The centroid \(c_{-i}\) of the opposite face satisfies \(|x_i-c_{-i}|=(4/3)|x_i-c|\), and \(c_{-i}\) lies in that face plane. Thus the least tetrahedral altitude is at most \(\sqrt{2/3}\,M\). Equality cannot contain an open configuration family.

Define the finite geometric constants

\[
I=2\pi M^2,\qquad L=\frac{4\pi}{3}M^3,\qquad
B=2\pi^2M^2,
\tag{3}
\]

\[
G=6\pi\left[M^2\log\frac{M}{H}-\frac{M^2-H^2}{2}\right]>0.
\tag{4}
\]

For a proposed intensity \(s>0\), set

\[
a_2=\frac{s}{I},\qquad a_3=\frac{a_2}{4B},\qquad
a_4=\frac{a_2}{16BG},\qquad \rho=s.
\tag{5}
\]

The pointwise subtraction bounds used below become

\[
\begin{aligned}
E_2(s)&=IMs,\\
E_3(s)&=6BMs+2BIM^2s^2,\\
E_4(s)&=\frac{16}{3}GMs+\frac{8BGM}{I}s
       +16BGM^2s^2+\frac{8}{3}BGIM^3s^3.
\end{aligned}
\tag{6}
\]

Each is continuous, strictly increasing on \(s>0\), and tends to zero with \(s\). Let

\[
\lambda _*=\sup\{s>0:E_2(s)\leq\tfrac12,\
E_3(s)\leq\tfrac12,\ E_4(s)\leq\tfrac12\}.
\tag{7}
\]

Then \(0<\lambda _*<\infty\), and continuity and monotonicity show that every \(0<s\leq\lambda _*\) satisfies the three bounds. In the rest of the construction take \(s=\lambda _0\).

For \(j=2,3,4\), write

\[
K_2=\frac{\mathbf1_{S_2}}D,\qquad
K_3=\frac{\mathbf1_{S_3}}A,\qquad
K_4=\frac{\mathbf1_{S_4}}V.
\]

The pair kernel remains integrable without a lower cutoff:

\[
\int_{0<|y|\leq M}\frac{dy}{|y|}=2\pi M^2=I.
\tag{8}
\]

Define same-parent kernels recursively by

\[
q_2(12)=\mathbf1_{S_2}(12)\left(\frac{a_2}{D(12)}-\rho^2\right),
\tag{9}
\]

\[
q_3(123)=\mathbf1_{S_3}(123)\left(
\frac{a_3}{A(123)}-\rho^3-\rho\sum_{i<j}q_2(ij)\right),
\tag{10}
\]

and

\[
\begin{aligned}
q_4(1234)=\mathbf1_{S_4}(1234)\bigg(&\frac{a_4}{V(1234)}-\rho^4
-\rho^2\sum_{i<j}q_2(ij)\\
&-\sum_{ij\mid k\ell}q_2(ij)q_2(k\ell)
-\rho\sum_{|J|=3}q_3(J)\bigg).
\end{aligned}
\tag{11}
\]

Here \(ij\mid k\ell\) runs over \(12\mid34,13\mid24,14\mid23\), and the final sum runs over all four faces.

Let \(\mathcal M\) integrate out one coordinate. The actual exact-size cluster kernels are the downward marginal inversion

\[
F_4=q_4,\qquad F_3=q_3-\mathcal Mq_4,\qquad
F_2=q_2-\mathcal Mq_3+\tfrac12\mathcal M^2q_4.
\tag{12}
\]

The factor \(1/2\) records the two orders of the two omitted daughters.

The required marginal estimates remain valid at \(\delta=0\):

\[
\mathcal MK_3\leq BK_2,\qquad \mathcal MK_4\leq GK_3.
\tag{13}
\]

For the first estimate, with pair length \(d\) and omitted-vertex distance \(r\) from the pair line, \(A=dr/2\), and

\[
\int_{B(0,M)}\frac{dz}{r}=\pi^2M^2.
\]

For the second, with signed height \(u\) above a fixed triangle of area \(A\), \(V=A|u|/3\), while \(H\leq |u|\leq M\); integrating the circular cross-section of \(B(0,M)\) gives (4). Support nesting makes each marginal vanish where the right side of (13) vanishes.

The elementary bounds

\[
A\leq\frac{M^2}{2},\quad \frac{A}{D_{ij}}\leq\frac M2,
\quad V\leq\frac{M^3}{6},\quad
\frac{V}{D_{ij}}\leq\frac{M^2}{6},
\]

\[
\frac{V}{D_{ij}D_{k\ell}}\leq\frac M6,\qquad
\frac{V}{A_J}\leq\frac M3
\tag{14}
\]

show successively from (9)–(11) and (6) that

\[
\frac12a_jK_j\leq q_j\leq a_jK_j,\qquad j=2,3,4.
\tag{15}
\]

Combining (13), (15), and \(a_3B=a_2/4\), \(a_4G=a_3/4\), gives

\[
F_4\geq\tfrac12a_4K_4,\qquad
F_3\geq\tfrac14a_3K_3,\qquad
F_2\geq\tfrac14a_2K_2.
\tag{16}
\]

The alternative identity
\(F_2=q_2-\mathcal MF_3-\tfrac12\mathcal M^2F_4\) also gives \(F_2\leq q_2\), and \(F_3\leq q_3\). Hence each anchored normaliser

\[
Z_j=\int F_j(0,y_2,\ldots,y_j)\,dy_2\cdots dy_j
\]

is finite and strictly positive. Strict positivity follows from open neighbourhoods of a regular tetrahedron with side between \(\sqrt{3/2}\,H\) and \(M\), together with its faces and edges.

Take independent homogeneous Poisson parent processes of types \(j=2,3,4\), with respective rates \(Z_j/j!\). A type-\(j\) parent at \(z\) emits

\[
\{z,z+Y_2,\ldots,z+Y_j\},\qquad
(Y_2,\ldots,Y_j)\sim F_j(0,\cdot)/Z_j.
\]

Add an independent singleton Poisson process of rate

\[
\lambda _1=\rho^2L+\frac{Z_3}{2}+\frac{Z_4}{3}>0.
\tag{17}
\]

All offsets are bounded by \(M\), every cluster has at most four points, and every mark has a Lebesgue density. It follows that the superposition is stationary, isotropic, simple and locally finite; bounded-window counts have finite exponential moments. The same facts and the finite partition formula give absolutely continuous factorial moment measures at every finite order. No hard core has been introduced: (8) permits pairs at every positive distance.

To check the intensity, put \(Q_j=\int q_j(0,\cdot)\). Then

\[
Z_4=Q_4,\quad Z_3=Q_3-Q_4,\quad
Z_2=Q_2-Q_3+\tfrac12Q_4,
\]

and, by (8)–(9),

\[
Q_2=a_2I-\rho^2L=\rho-\rho^2L.
\]

The non-singleton intensity is \(Z_2+Z_3/2+Z_4/6\). Adding (17) leaves \(Q_2+\rho^2L=\rho=\lambda _0\). Thus the intensity is the prescribed input, not a later selected value.

## Full product-density calculation

For a type-\(j\) cluster, the ordered same-parent \(r\)-tuple density is

\[
b_r^{(j)}=\frac1{(j-r)!}\mathcal M^{j-r}F_j.
\tag{18}
\]

The \(j!\) assignments of an ordered full tuple cancel the parent-rate factor \(j!\), and marginalising the remaining daughters counts each ordered \(r\)-tuple \((j-r)!\) times. Summing the three cluster types and the singleton stream, (12) and (17) give the total same-parent densities

\[
b_1=\rho,\qquad b_2=q_2,\qquad b_3=q_3,\qquad b_4=q_4.
\]

Partitioning an ordered observed tuple according to its parent gives every full density. Explicitly, the complete \(2,5,15\) partition sums are

\[
m_2(12)=\rho^2+q_2(12),
\tag{19}
\]

\[
m_3(123)=\rho^3+\rho[q_2(12)+q_2(13)+q_2(23)]+q_3(123),
\tag{20}
\]

and

\[
\begin{aligned}
m_4(1234)={}&\rho^4
+\rho^2\sum_{1\leq i<j\leq4}q_2(ij)\\
&+[q_2(12)q_2(34)+q_2(13)q_2(24)+q_2(14)q_2(23)]\\
&+\rho[q_3(123)+q_3(124)+q_3(134)+q_3(234)]
+q_4(1234).
\end{aligned}
\tag{21}
\]

Thus (19) contains the singleton–singleton and pair blocks; (20) contains the all-singleton term, three pair–singleton terms and one triple term; and (21) contains the all-singleton term, six pair–singleton–singleton terms, three pair–pair terms, four triple–singleton terms and one quadruple term. These are full product densities, not merely connected densities.

Substitution of (9)–(11) into (19)–(21) gives

\[
m_2=\frac{a_2}{D}\quad\hbox{on }S_2,\qquad
m_3=\frac{a_3}{A}\quad\hbox{on }S_3,\qquad
m_4=\frac{a_4}{V}\quad\hbox{on }S_4.
\tag{22}
\]

Since \(\mathcal D_2=S_2\), \(\mathcal D_3\subseteq S_3\), and \(\mathcal D_4=S_4\), division by \(\lambda _0^j\) proves the frozen target with

\[
C_2=\frac{1}{I\lambda _0},\qquad
C_3=\frac{1}{4BI\lambda _0^2},\qquad
C_4=\frac{1}{16BGI\lambda _0^3}.
\tag{23}
\]

All are positive and configuration-independent. The same process and parameter set give all three identities. The construction imposes no target identity beyond diameter \(M\); its induced correlations there are simply whatever the cluster law gives.

For comparison, any candidate process with factorial-cumulant densities \(c_j\) must satisfy the same set-partition algebra:

\[
\rho^{(2)}=\lambda _0^2+c_2,
\]

\[
\rho^{(3)}=\lambda _0^3+\lambda _0\sum_{i<j}c_2(ij)+c_3,
\]

\[
\rho^{(4)}=\lambda _0^4+\lambda _0^2\sum_{i<j}c_2(ij)
+\sum_{ij\mid k\ell}c_2(ij)c_2(k\ell)
+\lambda _0\sum_{|J|=3}c_3(J)+c_4.
\tag{24}
\]

Writing \(a_j=\lambda _0^jC_j\), the target forces

\[
c_2(ij)=\frac{a_2}{D_{ij}}-\lambda _0^2
\quad\hbox{on }\mathcal D_2,
\]

and

\[
c_3(123)=\frac{a_3}{A}
-\lambda _0a_2\sum_{i<j}\frac1{D_{ij}}+2\lambda _0^3
\quad\hbox{on }\mathcal D_3.
\tag{25}
\]

On \(\mathcal D_4\), (24) determines \(c_4\) only after the four face values of \(c_3\) are known. Those faces need not lie in \(\mathcal D_3\), because the frozen problem deliberately places no triangle-altitude condition on tetrahedral faces. A general obstruction may not replace those unspecified values by (25). The construction avoids this gap by extending its internal triangle identity to \(S_3\), which contains every supported tetrahedral face.

## Proof or obstruction

The exact low-intensity theorem has been proved above. I now give the general necessary condition, which applies to every process class and uses no values outside the frozen pair domain.

Let \(B_0\subset\mathbb R^3\) be a bounded positive-measure Borel set with \(\operatorname{diam}B_0\leq M\), and write

\[
J(B_0)=\int_{B_0}\int_{B_0}\frac{dx\,dy}{|x-y|},\qquad
\mu_{B_0}=\lambda _0|B_0|.
\]

The local integrability of \(1/|x-y|\) in three dimensions gives \(0<J(B_0)<\infty\). For \(N=X(B_0)\), the pair identity gives exactly

\[
\mathbb E(N)_2=\lambda _0^2C_2J(B_0).
\tag{26}
\]

Put \(n=\lfloor\mu_{B_0}\rfloor\) and \(\theta=\mu_{B_0}-n\). Since
\((N-n)(N-n-1)\geq0\) for every integer \(N\), taking expectations yields

\[
\mathbb E(N)_2\geq n(n-1)+2n\theta.
\tag{27}
\]

Consequently every target process must obey

\[
C_2\geq
\frac{n(n-1)+2n\theta}{\lambda _0^2J(B_0)}
\quad\hbox{for every bounded positive-measure Borel }B_0
\quad\hbox{with }\operatorname{diam}B_0\leq M.
\tag{28}
\]

This is the sharp lower bound on the second factorial moment of an integer-valued random variable with a given mean; equivalently, it is the variance lower bound \(\operatorname{Var}N\geq\theta(1-\theta)\).

For the ball \(B_R\), \(0<R\leq M/2\),

\[
J(B_R)=4\pi\int_0^{2R}r\,|B_R\cap(B_R-re_1)|\,dr
=\frac{32\pi^2R^5}{15},
\]

and \(\mu_R=4\pi\lambda _0R^3/3\). Hence

\[
C_2\geq
\sup_{0<R\leq M/2}
\frac{5R}{6}\,
\frac{\lfloor\mu_R\rfloor
\bigl(\lfloor\mu_R\rfloor-1+
2(\mu_R-\lfloor\mu_R\rfloor)\bigr)}
{\mu_R^2}.
\tag{29}
\]

Taking \(R=M/2\) gives (1).

There is also a signed-test-function version. For every bounded real \(f\) with compact support of diameter at most \(M\), count covariance gives

\[
\lambda _0\int f^2
+\lambda _0^2C_2\iint\frac{f(x)f(y)}{|x-y|}\,dx\,dy
-\lambda _0^2\left(\int f\right)^2\geq0.
\tag{30}
\]

Both (28) and (30) retain the diagonal contribution \(\lambda _0\int f^2\). Dropping it would incorrectly turn a Cox-specific Jensen bound into a general point-process bound. Neither inequality uses, or constrains, correlations at distance greater than \(M\).

The necessary conditions do not refute the governing target. The constants \(C_j\) are outputs, and \(C_2\) can be chosen large. The low-intensity construction (23) has \(C_2=(2\pi M^2\lambda _0)^{-1}\), which grows as the intensity decreases.

Two exact subclass exclusions from the frozen dossier remain valid but do not imply general non-existence. A stationary Hermitian determinantal process has \(g_2\leq1\), whereas \(C_2/D\to\infty\) as \(D\downarrow0\). An ordinary finite-variance log-Gaussian Cox process has bounded \(g_2\), and its higher product densities also obey the rigid product formula \(g_n=\prod_{i<j}g_2(x_i,x_j)\). These facts exclude those subclasses only.

## Reasoning summary and decision record

- The pair singularity is locally integrable in three dimensions. The tetrahedral flattening divergence is removed by the prescribed \(h_4>0\), and large-separation occupancy arguments cannot be used because the identities stop at diameter \(M\).
- A direct attempt to infer fourth-order cumulants from the triangle target fails: faces of a target tetrahedron are not required to belong to \(\mathcal D_3\). Formula (24) keeps those values explicit.
- The finite-cluster source was tested at its excluded endpoint \(\delta=0\). The only newly singular integral is (8), which is finite. Every marginal estimate, pointwise positivity estimate, anchored normalisation, simplicity argument and parent-partition identity survives.
- Setting \(h=\min(h_3,h_4)\) resolves the face-support issue without shrinking the requested triangle domain. Setting \(a_2=\lambda _0/I\) prescribes the intensity. The residual kernels stay nonnegative when the explicit polynomials (6) are at most \(1/2\), which holds on a nonempty interval of prescribed intensities.
- The restricted theorem rules out the claim that no intensity admits a solution. It does not decide existence or non-existence for any prescribed \(\lambda _0>\lambda _*\). For arbitrary intensity, count positivity yields (28)–(30), but no contradiction because the reciprocal amplitudes are free.
- Determinantal and ordinary log-Gaussian Cox failures remain class-specific and were not promoted to statements about general point processes or general Cox processes.
- Reused formulas were traced to the exact manuscript sections and are rederived here. Prior audit documents were treated only as historical records, not as independent support.

## Checks and limitations

1. **Analytical checks.** The proof checks integrability at \(D=0\), nested supports, all marginal coefficients, the actual intensity, cluster multiplicities, and all 15 fourth-order parent partitions. The ball energy in (29) was evaluated from the exact overlap-volume integral. No numerical or empirical evidence is used.
2. **Exactness.** The restricted theorem is exact in the continuum and holds almost everywhere on the full frozen domains. It is not a grid check, approximation, limiting density, or same-parent-only statement.
3. **Intensity restriction.** The construction covers every prescribed \(0<\lambda _0\leq\lambda _*(M,h_3,h_4)\), not arbitrary positive intensity. The positivity proof supplies a sufficient small-intensity interval; it does not show that the threshold is necessary or optimal. Existence and non-existence above \(\lambda _*\) both remain unresolved.
4. **No general negative theorem.** Inequalities (28)–(30) constrain \(C_2\), but \(C_2\) is not an input. No admissible tuple \((\lambda _0,M,h_3,h_4)\) is excluded by this submission.
5. **Window scope.** Equation (28) is asserted only for bounded positive-measure Borel windows of diameter at most \(M\), so its denominator is finite and strictly positive. Null windows are excluded.
6. **Outside-domain correlations.** The constructed process has correlations everywhere, but only (22) on the declared supports is used. The necessary-condition proof likewise uses no unspecified tail or excluded triangle/tetrahedron value.
7. **Finite altitude cutoffs.** No flattening obstruction is claimed for the actual \(\mathcal D_4\). If the positive \(h_4\) cutoff were removed on a full-dimensional family, the familiar \(\int du/|u|\) divergence would return, but that is a different problem.
8. **Source status.** The two local manuscripts are unpublished prior work. Their complete frozen source trees were inspected. Published sources in the dossier support definitions and general structural formulas; none is cited as proving the endpoint construction. Prior local audit files are historical records, not independent proof certificates.
9. **Verification status.** This is a self-contained informal mathematical proof and self-review of a repaired submission, not a proof-assistant formalisation or an independent review.

## References

- Frozen governing statement: common/problem_statement.md, version 19 October 2026, full text verified in this run.
- *Exact reciprocal simplex correlations on finite domains* (unpublished local manuscript, 18 October 2026). Reused recursive kernels, downward inversion, cluster law, intensity and full density formulas are in sections/construction.tex, “A finite-cluster construction” (sec:construction; equations q2–q4, Fkernels, singleton-rate and full-partitions; Theorem thm:main). The marginal and positivity estimates are in sections/appendix_bounds.tex, “Geometric bounds and positivity” (app:bounds; Lemmas lem:marginal-bounds and lem:kernel-positive). The multiplicity and set-partition derivation is in sections/appendix_partitions.tex, “Cluster normalisation and parent partitions” (app:partitions). These frozen source sections were checked in full.
- The local file review/manuscript_math_check.md belonging to that manuscript is a historical audit record. It is not cited as independent support for the theorem or for the endpoint extension.
- *Reciprocal simplex correlations from random spherical surfaces* (unpublished local manuscript, 27 September 2026), especially Sections 4–5. The complete frozen source tree was inspected. Its MATH_CHECK.md file is likewise only a historical audit record and is not theorem support.
- Daley and Vere-Jones, *An Introduction to the Theory of Point Processes*, Vol. II, 2nd ed. (2008), Exercise 12.6.11, printed p. 249. The frozen local excerpt and dossier verification were checked; the exercise poses the historical compatibility question and does not prove this result.
- Kuna, Lebowitz and Speer, *Necessary and Sufficient Conditions for Realizability of Point Processes* (2011), Section 5, formula (38), is full-text-verified in the frozen obstruction dossier for the Yamada count bound. Equations (27)–(29) above give the needed special case directly.
- Last and Penrose, *Lectures on the Poisson Process* (2017), equation (13.10), and Clark and Houssineau (2013), Theorems 4.1–4.2, are full-text-verified in the frozen literature dossier for Cox and cluster moment structure. The present formulas are derived above rather than imported.
- Møller, Syversveen and Waagepetersen (1998), Theorem 1, and Soshnikov (2000), determinant formula and operator condition, are full-text-verified in the frozen dossier for the scoped subclass exclusions.

## Response to review (v02 onward)

1. **A5-v01-01 — unresolved governing scope.** Preserved the theorem only for every prescribed \(0<\lambda _0\leq\lambda _*(M,h_3,h_4)\). The claim section, reasoning summary and limitations now state explicitly that the governing arbitrary-intensity quantifier is unproved and that both existence and non-existence above \(\lambda _*\) remain unresolved.
2. **A5-v01-07 — null windows.** Restricted (28) to bounded positive-measure Borel windows of diameter at most \(M\), and stated \(0<J(B_0)<\infty\) before dividing by \(J(B_0)\).
3. **A5-v01-08 — ambiguity.** Replaced the ambiguous wording by: “The restricted theorem rules out the claim that no intensity admits a solution. It does not decide existence or non-existence for any prescribed \(\lambda _0>\lambda _*\).” Equivalent explicit wording now appears wherever the scope is summarised.
4. **A5-v01-09 — source hygiene.** Added exact source sections, labels and equation/lemma names for every reused group of formulas. The local audit files are explicitly labelled as historical records and are not used as independent theorem support. All reused mathematics remains reproduced self-containedly in this submission.
