# Review — proof_1 / submission v03 / S1

- Type: fresh independent extensive correctness audit, including the consequential supplied v01 and v02 dependencies.
- Reviewer: `/root/review_proof_1_v03`; own session `session-18`; current turn `turn-30`.
- Requested and verified runtime: `gpt-6-astra`, reasoning effort `xhigh`. Verification preceded mathematics. The own-session rollout is `[local path omitted]`: `session_meta` line 1 identifies this session, and `turn_context` line 8 identifies this turn, model and effort. Only allowlisted metadata fields were inspected.
- Session started: `2026-10-20T18:20:56.948Z`. Exact artifact freeze time is in `review_freeze.json`; final completed-turn time and usage are not available at manuscript freeze.
- Setup root: `$SETUP`.
- Run root: `runs/20261020T164437Z_astra6/` beneath that setup root. Paths below are relative to this run root unless stated otherwise.
- Dispatch packet: `packets/review_proof_1_v03.json`, SHA-256 `a81fa30526b3b3932d34835fc8c67e723acc6794ccf9828290b8b29bd3afee70`.
- Active target: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Reviewed submission: `reviews/proof_1_v03/proof_snapshot.md`, SHA-256 `33eb2d7a62132ed60f95833f244544f4bb9b9004c9eee76f194de47e5d81e8ec`.
- Supplied prior dependencies: `prior_dependency_v01.md`, SHA-256 `acf0c4de3dcd7ee1caeeff0da17e9d8d7d8144b5ecb984d0742bb1662fc52473`; `prior_dependency_v02.md`, SHA-256 `67605a81bb7fa19e16d3aad6ca6ae6c86af8b1112d8f27a165d9a1558200c21d`, both in the assigned review directory.
- All 24 allowed-file hashes and the packet hash were verified. The file-by-file evidence is in `preflight.json`.
- Received context: the explicit frozen instructions, workflow, target and amendment, skill and required references, common context/source index, templates, current proof, own-track prior proofs, concrete prior issue tables, and one explicitly assigned seed excerpt with provenance. Prior issue labels were treated as obligations to check.
- Excluded context: other tracks, author/coordinator conversations, private work, unassigned seed material, old runs, full prior reviews and other chats. No delegation occurred.

## Correctness verdict and scope

**Submission 3 does not establish exact S1. Its three new scoped results are supported by the supplied arguments and the independently rechecked dependencies. I found no consequential mathematical error in those results.**

The supported results are:

1. A Poisson-cluster S1 candidate cannot have fourth same-parent density
   \[
   k_4(\mathbf x)=V(\mathbf x)^{-1}
      \int_{(0,\infty)}F_R(\mathbf x)\,\mathcal A(dR)
   \]
   for the specified normalised finite-radius cylinder factors and a nonnegative amplitude measure. The proof derives finiteness of that measure from the target.
2. The specified expanding-radius cylinder mark law exists with finite intensity and finite third local moments. Its fourth same-parent kernel has a universal bounded-diameter small-volume residue. That property is incompatible with the exact lower full laws and the fourth full S1 law. Adding independent clusters of size at most three cannot repair it.
3. In the displayed low-intensity range, a fixed-amplitude sequence of genuine processes converges in total variation on each bounded window to the finite-cluster process \(X_0\), but its fourth factorial expectations on nonzero nonnegative tests in \(C_c(E_4(M))\) do not converge to those of \(X_0\). The explicit positive discrepancy proves failure of the needed moment passage for this sequence.

These are valid partial results, including representation-specific obstructions and a negative result about a particular limit. They do not prove general non-existence for S1. The exact joint cluster law and the all-intensity construction remain unresolved. Accordingly this is the **third unsuccessful exact-target submission**, with substantive valid progress; it is not a false proof presented as an S1 solution, and it is not a proof that S1 is false. The fourth submission remains available under the existing counter.

The review covers the complete current mathematical submission and every supplied earlier calculation used in its conclusions. It does not independently audit the historical S0 obstruction proofs named by the amendment, unassigned seed supplements, literature priority, or the author's telemetry claims.

## Reconstruction and detailed audit

### 1. Target, quantifiers and moment class

The active target is the separately adopted and hashed S1, not an inference from the preceding partial proofs. The supplied `S0_to_S1.md` identifies the amendment authority and its scope; its SHA-256 is `b2534040520dfc63bf5c22ecc508257308e619a040a7c6c54ce44375742394de`. This audit accepts that dispatch as the target assignment and does not reopen or expand the amendment.

S1 quantifies over every independently prescribed \(\lambda>0\) and \(M>0\). One whole-space stationary simple locally finite process must have intensity exactly \(\lambda\), with full globally absolutely continuous factorial measures and finite-almost-everywhere densities through order four. The three reciprocal identities must hold almost everywhere on all nondegenerate configurations of diameter below \(M\), with finite positive configuration-independent coefficients. There is no lower geometric cutoff and no finite-fourth-moment assumption.

The current obstruction results are conditional exclusions at every positive intensity within their stated representations. The positive sequence theorem retains
\[
2\pi\lambda M^3\leq\tfrac12,\qquad
8\pi^3(\lambda M^3)^2+12\pi^2\lambda M^3\leq\tfrac12.
\]
It therefore does not cover S1's parameter quantifiers. Its two exact lower laws also do not supply the required exact fourth law.

The moment comparison is consistent throughout. On a ball of diameter below \(M\), \(D^{-1}\) is integrable, and, for a fixed base edge of length \(d\),
\[
\int_{\operatorname{diam}(x_1,x_2,z)<M}\frac{dz}{A(x_1,x_2,z)}
\leq \frac{2\pi^2M^2}{d}.
\]
Consequently the first three target factorial moments give finite third counts in such balls; a finite covering and
\((\sum_{i=1}^k n_i)^3\leq k^2\sum_i n_i^3\) extend this to every bounded set.

Conversely, near a small planar square with separated vertices and all face areas bounded below, write the fourth vertex in base-plane coordinates and signed height \(h\). Then \(V=A|h|/3\), and integration contains \(\int dh/|h|=\infty\). This proves the fourth-moment divergence on every nonempty open ball without conflicting with almost-sure local finiteness. Thus a finite-fourth-moment S1 comparison subclass is impossible; its exclusion does not justify imposing that hypothesis on the broad class.

### 2. Whole-space cluster construction and all parent partitions

The v02 parent-level definition repairs the earlier product-notation ambiguity. Its input measure \(dz\,\nu(dC)\) is sigma-finite, and \(\int N\,d\nu<\infty\) gives finite expected counts \(\lambda|B|\). A countable exhaustion proves simultaneous almost-sure local finiteness. Within-mark diffuseness, or the explicit simple anchored marks, prevents internal coincidences; independent translation variables make distinct-parent coincidences null.

For each set partition, integrate first over the distinct parents and their selected ordered offspring. This is a nonnegative integral over sigma-finite measures. Partitioning an observed tuple by its parents is unique, so no extra combinatorial factor is introduced. Once the image same-parent measures have finite-almost-everywhere densities, their ordinary product densities can be used. At order four the block types have multiplicities
\[
1\ (1+1+1+1),\quad6\ (2+1+1),\quad
3\ (2+2),\quad4\ (3+1),\quad1\ (4).
\]
All 15 terms are retained in the current submission.

The exact lower full laws consequently force
\[
q_2(ij)=\frac{a_2}{D_{ij}}-\lambda^2,\qquad
q_3(ijk)=\frac{a_3}{A_{ijk}}
 -\lambda a_2\sum_{\{u,v\}\subset\{i,j,k\}}D_{uv}^{-1}
 +2\lambda^3.
\]
Every edge and face of an affinely independent quadruple in \(E_4(M)\) lies in its lower-order domain. The 14 lower-block terms are exactly the displayed \(B_4\), so the remaining requirement is \(k_4+B_4=a_4/V\). In a genuine candidate the block measures are nonnegative. Their canonical lower-domain versions are continuous and nonnegative there, since a continuous version negative at a point would be negative on a set of positive measure.

Replacing lower block densities by these versions is legitimate almost everywhere in the higher-dimensional configuration space: null exceptional sets in a block pull back to null sets on bounded product boxes, hence on their countable union. When \(k_4\) is continuous, the full canonical difference is continuous on the open set \(E_4(M)\); an almost-everywhere equality therefore holds everywhere on that set. This justifies both explicit degeneration paths. No exceptional curve is substituted directly into an unqualified almost-everywhere equality.

### 3. The two full-density boundary residues

For the lifted square
\[
0,\quad se_1,\quad se_2,\quad s(e_1+e_2)+he_3
\]
with \(\sqrt2s<M\), all edges and faces stay uniformly nondegenerate as \(h\downarrow0\), while \(V=s^2h/6\). The lower blocks remain bounded, so \(VB_4\to0\). Any continuous candidate therefore requires \(Vk_4\to a_4\).

For the second path
\[
0,\quad se_1,\quad2se_1+\delta e_2,\quad te_3,
\qquad \sqrt{4s^2+t^2}<M,
\]
the distances have positive limits. The areas of faces 124, 134 and 234 have positive limits, whereas
\[
A_{123}=s\delta/2,\qquad V=s\delta t/6,\qquad
V/A_{123}=t/3.
\]
Every term of \(VB_4\) tends to zero except the \(a_3/A_{123}\) part of the face-123-plus-singleton term. Hence
\[
VB_4\longrightarrow\lambda a_3t/3,\qquad
Vk_4\longrightarrow a_4-\lambda a_3t/3.
\]
The signs and the factor \(1/3\) are correct. The difference is strictly positive because \(\lambda,a_3,t>0\). It arises from a required full factorial partition, not a cumulant reinterpretation.

Thus a continuous fourth same-parent kernel with one common residue along all bounded small-volume configurations is excluded. This is a condition on a kernel within the cluster representation. It is not a classification of arbitrary stationary processes or arbitrary cluster kernels.

### 4. Recheck of the width identity and fixed-radius normalisation

The supplied v02 proof of the width identity is self-contained. For the standard tetrahedron \(S=\operatorname{conv}(0,e_1,e_2,e_3)\), the polar of \(S-S\) is
\[
\{q:\max(0,q_1,q_2,q_3)-\min(0,q_1,q_2,q_3)\leq1\}.
\]
The part where zero is the minimum has volume one. For each of the three possible negative minimum coordinates \(q_i=-u\), \(0<u<1\), the other two coordinates range independently over an interval of length one; that part also has volume one. Ties are null. The total polar volume is four.

For a general tetrahedron with edge matrix \(U\), polar volume scales by \(|\det U|^{-1}=(6V)^{-1}\). Spherical integration gives polar volume \(\frac13\int w^{-3}\,dS\). Since \(\sigma=dS/(4\pi)\), these facts yield
\[
\int_{S^2}w_{\mathbf x}(n)^{-3}\,\sigma(dn)=\frac1{2\pi V}.
\]
The normal overlap integral is also correct:
\[
\int_0^\infty
\frac{(2\varepsilon-w)_+}{(2\varepsilon)^4}
\frac{d\varepsilon}{\varepsilon}
=\int_w^\infty\frac{s-w}{s^5}\,ds
=\frac1{12w^3}.
\]

For fixed radius, the parent-position integral is the disc-intersection area times the normal overlap, divided by the fourth power of cylinder volume. These constants give
\[
p_4=\frac{c}{24\pi^4R^6}\frac{F_R}{V}.
\]
Thus the submission's amplitude and its probability measure
\(\mu_{\mathbf x}(dn)=2\pi Vw_{\mathbf x}(n)^{-3}\sigma(dn)\)
are correctly normalised.

For diameter \(d<R\), the projected centre distances are at most \(d\), so the intersection contains the disc of radius \(R-d\) about one projected vertex. This gives \(F_R\geq(1-d/R)^2\), with \(F_R\leq1\). For a fixed nondegenerate tuple, minimum width is positive. Disc-intersection area is continuous in centres and plane orientation, using local orthonormal coordinates and dominated convergence outside circle boundaries. These facts prove the stated continuity of \(F_R\).

### 5. Theorem 1: every positive mixture of finite radii

The amplitude-finiteness step is essential and valid. In an S1 candidate, nonnegative lower partitions give \(Vk_4\leq a_4\) almost everywhere. For \(u\in(0,1)\), \(d_0<M\), and tuples of diameter below \(d_0\),
\[
\int F_R\,d\mathcal A
\geq(1-u)^2\mathcal A([d_0/u,\infty)).
\]
The configuration set has positive measure, so this inequality and the almost-everywhere candidate bound imply the displayed tail bound. Monotone continuity as \(d_0\downarrow0\), followed by \(u\downarrow0\), gives
\(\mathcal A((0,\infty))\leq a_4\).
This does not assume a finite amplitude measure in advance, nor interchange a limit against an uncontrolled measure.

The finite total mass and \(F_R\leq1\) now give continuity of the mixture on nondegenerate configurations. The square path can therefore be used pointwise.

As the square becomes planar, \(\mu_{\mathbf x}\) concentrates at its two unit normals. Outside any neighbourhood of those normals, the fixed base triangle gives a uniform positive width, and the mass is at most a constant times \(V\). Symmetry gives equal limiting masses. Joint continuity of the disc-intersection area identifies the limiting factor as
\[
j_R(s)=J_R(s)/(\pi R^2).
\]
For every finite positive \(R,s\), \(0\leq j_R(s)<1\), because already two distinct equal-radius discs lose a positive area of intersection. Also \(j_R(s)\to1\) as \(s\downarrow0\), including radii for which the intersection was initially empty.

Dominated convergence first in the height and then in \(s\) yields
\[
a_4=\int j_R(s)\,\mathcal A(dR),\qquad
a_4=\mathcal A((0,\infty)).
\]
The measure is finite and nonzero. Since \(1-j_R(s)>0\) at every finite radius, its integral against this nonzero measure is strictly positive, even without a uniform pointwise gap. The two equalities are incompatible.

This proves the advertised exclusion, including unbounded ranges of finite radii and initially unrestricted nonnegative amplitude measures. It does not include an atom at radius infinity, signed cancellation, arbitrary dependent marks, or a radius coupled to thickness in a way that changes the kernel formula.

### 6. Expanding radii: actual marks, regularity and Theorem 3

For any measurable positive finite \(R(\varepsilon)\) with \(R(\varepsilon)\to\infty\) as \(\varepsilon\downarrow0\), the specified iid uniform-cylinder marks have a finite integer population at each type. The ceiling is measurable, and every displacement law is diffuse. With
\[
u=(R/\ell)^6,\qquad p=4-r,
\]
cancellation of falling factorials gives, for \(r=0,1,2,3\),
\[
b\pi^3R^6\frac{(N_T)_r}{(N_T)_4}
\leq b\pi^3\ell^6T^{-p}g_\ell^{-p}
       \frac{u}{(1+u)^p}
\leq b\pi^3\ell^6T^{-p}g_\ell^{-p}.
\]
All four required integrals against \(d\varepsilon/\varepsilon\) converge: after \(v=\varepsilon/\ell\), the integrand is
\(v^{p-1}(1+v^2)^{-p}\).
This proves finite parent rate and finite first three factorial population rates without any upper-radius bound. The identity \(N^3=(N)_3+3(N)_2+N\) supplies finite raw third population rate.

For a bounded set \(B\), the parent-hit rate is at most its expected number of emitted points, and
\[
\int dz\int C(B-z)^3\,\nu(dC)
\leq |B|\int N^3\,d\nu.
\]
The finite compound Poisson count therefore has finite third moment. This proves the asserted process facts, not merely formal kernel consistency.

At order four, the type weight cancels both the factorial population factor and three powers of the lateral area, leaving precisely the submission's (23). The upper bound \(L_\varepsilon\leq1\), the height integral and the width identity give \(k_4\leq a/V\), with \(a=b/(24\pi)\). All same-parent measures are mixtures of Lebesgue densities. Finite local third moments make the first three such measures locally finite and their densities finite almost everywhere; the displayed fourth bound covers all affinely independent quadruples. Coplanarity is a null set, and the mixture has no singular measure on it. The full partition formula then gives globally diffuse finite-almost-everywhere full densities through order four. Increasing \(T\) makes intensity tend to zero while keeping \(k_4\) fixed; nonnegative singleton intensity can fill any prescribed positive amount.

For Lemma 2, the displayed measure \(\mathbb P_{\mathbf x}\) has total mass one by the same two integrals. Its tail satisfies
\[
\mathbb P_{\mathbf x}\{\varepsilon\geq\delta\}
\leq24\pi V\int_\delta^\infty\frac{d\varepsilon}{8\varepsilon^4}
=\frac{\pi V}{\delta^3}.
\]
For diameters at most \(D_0\), the limit of \(R(\varepsilon)\) provides, for every \(\xi>0\), a single small \(\delta\) with \(L_\varepsilon\geq(1-\xi)^2\) for all such tuples, all directions, and \(\varepsilon<\delta\). Consequently
\[
(1-\xi)^2(1-\pi V/\delta^3)
\leq \mathbb E_{\mathbf x}L_\varepsilon\leq1.
\]
This proves \(Vk_4\to a\) for every bounded-diameter sequence with \(V\to0\), including the collapsing-face path.

Continuity follows independently: near a fixed nondegenerate tuple, width is bounded below by \(m>0\); the integrand vanishes for \(\varepsilon\leq m/2\) and is bounded by a constant times \(\varepsilon^{-4}\) above that threshold. This is an integrable dominating function even for merely measurable \(R\).

Independent marks of size at most three have zero fourth same-parent contribution. If the exact lower laws hold after adding them, the square path forces \(a_4=a\), while the collapsing-face path forces \(a_4=a+\lambda a_3t/3\). This proves Theorem 3. The universal-residue property is proved for the displayed family; it is not assumed for every possible cluster law.

### 7. The inherited lower-order construction and the sequence parameters

The constants \(I=2\pi M^2\), \(J=2\pi^2M^2\), \(W=4\pi M^3/3\), \(a_2=\lambda/I\), \(a_3=a_2/(4J)\) are consistent in all three submissions. The cylindrical-coordinate integral above gives
\(\mathcal MK_3^0\leq JK_2^0\) and \(\int K_2^0(0,y)\,dy=I\).
The two low-intensity inequalities give
\[
\tfrac12a_2K_2^0\leq q_2\leq a_2K_2^0,\qquad
\tfrac12a_3K_3^0\leq q_3\leq a_3K_3^0.
\]
In particular \(F_2^0=q_2-\mathcal Mq_3\geq(a_2/4)K_2^0\); \(F_3^0=q_3\) is nonnegative and both anchored integrals are finite.

The rate \(F_r(0,\mathbf y)/r!\) for an anchored size-\(r\) stream is correct. An ordered selection of \(s\) of its \(r\) points gives \(r!/(r-s)!\) choices. Symmetry and a change of translation anchor with Jacobian one make their integrals equal, including selections omitting the original anchor. The resulting same-parent density is \(\mathcal M^{r-s}F_r/(r-s)!\). Thus the size-two and size-three intensity is \(Z_2+Z_3/2\), and the displayed singleton rates give total intensity exactly \(\lambda\).

The inherited fixed-radius lower estimates have also been checked. For a pair, integrating its directional width gives the uniform bound \(1/(2\pi R^2D)\) for the conditional overlap. For a triangle with longest edge \(d\) and altitude \(h\), width below \(2\varepsilon\) forces
\(|n_1|<2\varepsilon/d\), \(|n_2|<4\varepsilon/h\).
For \(\varepsilon<h/16\), the two sphere graphs give probability at most \(16\varepsilon^2/(\pi A)\); above that threshold the first strip gives \(2\varepsilon/d\). Both yield the stated overlap bound \(4/(\pi^2R^4A)\). The population integrals at powers \(1,2,3\) are \(\pi/2,1/2,\pi/16\). It follows that
\[
p_2\leq\frac{c}{4\pi R^2T^2D},\qquad
p_3\leq\frac{2c}{\pi R^4TA},\qquad
m_1\leq\frac{\pi c}{16T^3}.
\]
These bounds apply near all allowed degeneracies.

Substituting \(c_j=24\pi^4R_j^6a\) and the explicit \(T_j\) gives exactly
\[
p_{2,j}\leq\frac{a_2}{8j^2D},\quad
p_{3,j}\leq\frac{a_3}{4jA},\quad
m_{1,j}\leq\frac{\lambda^2W}{2j^3}.
\]
There is no incompatible simultaneous parameter choice: every entry of the maximum defining \(T_j\) is finite and positive. The fourth amplitude remains the one fixed \(a>0\).

The corrections are nonnegative. Indeed \(r_{3,j}\geq(a_3/2-a_3/(4j))K_3^0\), and
\[
F_{2,j}\geq
\left(\frac{a_2}{2}-\frac{a_2}{8j^2}-a_3J\right)K_2^0>0.
\]
Also \(F_{2,j}\leq r_{2,j}\leq q_2\). The singleton rate is at least
\(\lambda^2W-m_{1,j}>0\), since \(Q_3-\delta_{3,j}=\int r_{3,j}\geq0\).
With \(Q_2=\lambda-\lambda^2W\), the correction intensity is
\(Q_2-\delta_{2,j}-(Q_3-\delta_{3,j})/2\);
adding the cylinder and singleton intensities gives exactly \(\lambda\).

The restrictions in these corrections are necessary and correctly used: outside the prescribed domains the cylinder densities remain present. On the domains, same-parent orders two and three become exactly \(q_2,q_3\). Globally, the lower density bounds and nonnegative integrable correction kernels give the required regularity. At order four \(p_{4,j}\leq a/V\) off the null coplanar set. Each \(X_j\) consequently has the stated global density properties, finite third moments and infinite fourth moments on every nonempty open ball. The last claim follows from the positive lower bound \((1-1/j)^2a/V\) and the reciprocal-height divergence.

### 8. Theorem 4: local total variation and failure of fourth-measure convergence

The anchored integral bounds
\[
\delta_{2,j}\leq a_2I/(8j^2),\qquad
\delta_{3,j}\leq a_3JI/(4j)
\]
follow by nonnegative marginalisation. Subtracting the finite correction kernels gives
\[
F_{3,j}-F_3^0=-\mathbf1_{E_3}p_{3,j},\qquad
F_{2,j}-F_2^0=-\mathbf1_{E_2}p_{2,j}
 +\mathcal M(\mathbf1_{E_3}p_{3,j}),
\]
which proves all three bounds in (38), including the singleton difference.

Coupling the common parts of the finite parent-rate densities is legitimate. The correction clusters have diameter below \(M\), with one point at their anchor. Therefore a parent that affects \(B\) must lie in \(B_M\), a finite-volume set for bounded \(B\). The unmatched parent-rate mass is the anchored \(L^1\) difference divided by \(r!\) for each size, plus the singleton-rate difference. This proves the bound (40).

The cylinder stream is handled separately by
\[
\mathbb P\{X^{\rm cyl}_j(B)>0\}\leq m_{1,j}|B|,
\]
which does not impose a bounded radius or bounded thickness. Combining these estimates gives an explicit bound tending to zero for the total-variation distance of the restrictions. The claim is on each fixed bounded window; no global total-variation convergence is asserted.

For all quadruples in \(E_4(M)\), every lower block lies in its prescribed domain. Consequently \(B_4\) is independent of \(j\), and the exact full density there is
\[
\rho^{(4)}_{X_j}=\frac{aF_{R_j}}{V}+B_4.
\]
Since \(R_j=jM\),
\((1-1/j)^2\leq F_{R_j}\leq1\) throughout this domain. For compact support inside \(E_4(M)\), continuity of the geometric quantities supplies a positive volume minimum and positive minima for all relevant distances and face areas, and the spatial coordinates are bounded. Thus \((a/V+B_4)f\) is an integrable dominating function. Dominated convergence yields
\[
\lim_j\alpha^{(4)}_{X_j}(f)=
\int (a/V+B_4)f\,d\mathbf x
=\alpha^{(4)}_{X_0}(f)+a\int f/V\,d\mathbf x.
\]
For nonzero nonnegative continuous \(f\), the additional integral is strictly positive: \(f\) is positive on some open set, where \(V>0\).

The factorial sum for this test is a measurable function of the configuration in one bounded window, finite almost surely but unbounded as a random variable. Its distribution converges under local total variation. If these sums were uniformly integrable, truncation together with total-variation convergence of their bounded truncations would force convergence of expectations, contradicting the displayed discrepancy. The non-uniform-integrability conclusion is therefore justified.

This result is stronger than merely observing a missing compactness hypothesis: it identifies the actual limiting process and proves that its fourth factorial measure is different. It does not show that every conceivable construction limit has this defect. Moreover the formal density limit \(a/V+B_4\) is itself not the exact full reciprocal-volume target; the two boundary residues already distinguish those expressions.

### 9. Prior results and unresolved obligations

The supplied earlier proofs were read; the mathematical dependencies just described were re-established without using the earlier reviews as evidence.

- The v01 finite-cluster construction is the valid \(X_0\) used here. Its bounded population gives finite local exponential moments, so it fails the fourth S1 law.
- The v01 finite-fourth-population and population-independent iid-geometry obstructions remain correctly scoped. In the latter case an infinite fourth population moment multiplies a nonzero locally finite offspring measure by infinity, producing a non-sigma-finite same-parent measure. This contradicts S1's finite-almost-everywhere full density, not almost-sure local finiteness.
- The earlier separated-square argument shows why infinite fourth population contribution confined to arbitrarily shrinking cluster diameters cannot suffice: the separated coplanar family has infinite fourth mass while all lower partitions are bounded there.
- The v02 finite-cylinder construction supplies real finite marks with controlled lower contributions and an approximate fourth full law. Its approximation, even arbitrarily accurate, does not establish exact S1. The old choice \(a=C/\eta\) also lacks a finite-amplitude limit; the present fixed-amplitude sequence addresses a different precisely specified limiting experiment.

The exact outstanding construction obligation is still a single nonnegative finite-configuration mark measure, of total point intensity \(\lambda\), simultaneously realising \(q_2,q_3\) and \(q_4=a_4/V-B_4\) on the full S1 domains, with the global density requirements, for every prescribed \((\lambda,M)\). Formal nonnegativity alone does not give that measure. The new boundary conditions constrain it but do not construct it. A successful route outside the present families remains unclassified.

## Finding register

| ID | Location | Precise mathematical issue | Consequence | Repair/status |
|---|---|---|---|---|
| **P1V03-01** | Current lines 18–35, 423–436; prior P1V02-01 and P1V01-02 | No process realising the simultaneous exact fourth residual is supplied. The new theorems exclude particular repairs or show a particular limit fails. | Exact S1 is unresolved; submission 3 is an unsuccessful exact-target attempt with valid partial results. | **Open.** Supply a joint actual mark law or another process construction meeting every active requirement. No invalid exact-success claim is made here. |
| **P1V03-02** | Current lines 293–323, 434; prior P1V02-02 | The positive construction and sequence retain a restriction on \(\lambda M^3\). All-intensity scope of negative results within a family does not provide all-intensity existence. | S1's independent prescribed-parameter quantifiers remain unmet. | **Open.** Prove the remaining parameter regimes. Dilation preserves \(\lambda M^3\) and cannot remove this restriction. |
| **P1V03-03** | Current Section 1, especially (6) and (8) | Full lower partitions require different \(Vk_4\) residues at square flattening and a collapsing face with fixed opposite altitude. | A common-residue continuous fourth same-parent kernel cannot satisfy S1. | **Verified scoped necessary condition.** The a.e.-to-pointwise passage is justified before the paths are used. Arbitrary kernels are not assumed to have a common residue. |
| **P1V03-04** | Current Theorem 1, lines 139–184 | A nonnegative mixture over finite radii cannot eliminate the planar intersection loss. Amplitude finiteness is derived before either dominated-convergence step. | Every representation of form (13) is excluded, including unbounded ranges of finite radii. | **Verified scoped obstruction.** It provides no general non-existence or amendment authority. |
| **P1V03-05** | Current Section 4, especially (22)–(27) and Theorem 3 | The expanding-radius family is a genuine finite-mark process and its fourth kernel has a universal residue incompatible with P1V03-03. | This radius/thickness repair with size-at-most-three additions fails exact S1. | **Verified scoped obstruction.** Actual marks, intensity, third moments, global diffuseness and the uniform residue were checked. |
| **P1V03-06** | Current Theorem 4 and lines 421–422; prior P1V02-03 | The fixed-amplitude sequence converges locally in total variation but retains a positive fourth-expectation discrepancy on compact tests away from degeneracy. | Fourth factorial measures do not converge to those of the process limit; uniform integrability fails for these factorial sums. | **Verified negative limit result.** The former limiting-route concern is resolved for this sequence. No universal prohibition on other limits follows. |
| **P1V03-07** | Current (29)–(41); v02 Sections 1–5; prior P1V02-04/05/06 | Inherited density constants, all parent partitions, positivity, intensity balance and moment/density regularity are essential dependencies. | The sequence is an actual sequence of processes with the advertised two exact laws, not a list of formal kernels. | **Verified.** The earlier notation repair and moment-class progress remain valid; neither closes P1V03-01 or P1V03-02. |
| **P1V03-08** | Current source paragraphs and accounting handoff; prior P1V02-07 | Mathematical dependencies are supplied and self-contained. Historical/provenance references and author-runtime assertions are separate from mathematical proof evidence. | No missing external theorem blocks the present results; no historical-source or author-telemetry certification is implied. | **No active source gap.** Own runtime and input hashes are recorded separately; unassigned historical material was not inspected. |

## Amendment implications

No amendment is proposed in v03, and none is adopted by this review. The finite-radius-mixture and expanding-radius results exclude representations while leaving the broad process class untouched. They do not prove that a distance/altitude cutoff, intensity restriction, approximation, or change from full densities to cumulants is necessary.

The exact S1 target, its hash and its independent parameter quantifiers remain unchanged. The supplied amendment preserves the separate historical S0 verdict; these scoped results neither strengthen nor reverse that verdict.

After this third unsuccessful exact-target review, the workflow allows the author to request owner approval of a precise amendment. That is an optional request, not an approval and not a reset. No such owner decision or replacement statement is present in this packet.

## Source and coding evidence

The proof-reviser skill and its complete required proof-standard and writing-style references were read in their frozen packet versions. The frozen reviewer/accounting instructions, workflow, common context, S0, S1, amendment and review/change templates were also read. File identity checks used SHA-256; the detailed manifest is in `preflight.json`.

The assigned seed excerpt, SHA-256 `f0d755efa2b82343a5ff7f171c0ba69ccdcd92ba67a36106e9c47052197a2ac9`, and its provenance JSON were inspected. The relevant pair/triangle construction agrees with the rederived v01 specialisation. Its separate fourth-order result has an explicit altitude restriction and is not imported into S1. Unassigned supplements and the full original seed were not read.

No published theorem is an unresolved mathematical premise of the current results. The polar calculation, overlap integrals, finite-mark laws, partition identity, coupling and limits have been checked directly. The common source index and DVJ context are context only; no primary PDF, historical attribution, novelty claim or present-open-status assertion is certified here. No additional literature or coding request is needed.

Shell/Python tools were used for file reads, input-hash verification, own-runtime metadata filtering and artifact/accounting work. No simulation, numerical quadrature, symbolic calculation or proof-assistant verification was used as mathematical evidence. This is an extensive informal mathematical audit, not a formal certificate.

## Presentation judgement

The submission clearly separates its scoped negative results from exact-target success. The two degeneration paths explain why the full third-plus-singleton term matters, and the actual mark specification prevents the expanding-radius argument from being mistaken for a purely formal kernel example. The fixed-amplitude coupling result is stated with an appropriately local convergence mode and a precise test class.

No presentation defect hides a consequential mathematical gap. For a standalone exposition, two small improvements would help: restate the size-\(r\) anchored-stream normalisation in the sequence section, and include the one-line lower bound
\(\mathbb E_{\mathbf x}L_\varepsilon\geq(1-\xi)^2(1-\pi V/\delta^3)\)
in Lemma 2. Both transitions are already recoverable and verified above. They are optional exposition improvements, not conditions for accepting the scoped results.

## Review summary and repairs

The decisive checks were the full partition residues, the finite-amplitude derivation in Theorem 1, the existence and regularity of the expanding-radius mark law, the uniform small-volume limit, the simultaneous low-intensity correction budget, and the explicit coupling/expectation discrepancy. Those checks support the three new results.

The exact fourth-order construction and all-intensity coverage remain open. No correction to the supplied scoped proofs is required by this audit. A further attempt must address those outstanding obligations with new mathematics; changing the target, invoking a prior acceptance label or taking a process limit without its factorial-measure control would not close them.

The assigned output directory contains the review, a concise proof-level decision summary, runtime/hash preflight, accounting capability and the observable usage checkpoint. Unknown end-of-turn usage and charges remain NR; cumulative snapshots are not summed, and reasoning tokens are not added again to output tokens.
