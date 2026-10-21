# Review — proof_4 submission v04 against unchanged S1

- Type: fresh independent extensive review of the final construction submission and consequential earlier dependencies.
- Reviewer: /root/review_proof_4_v04, session session-24, turn turn-36.
- Actual model and effort: gpt-6-astra, xhigh, verified in the reviewer's own runtime turn_context before mathematical work.
- Run: 20261020T164437Z_astra6.
- Preflight/research boundary: 2026-10-20T19:15:43.861271+00:00. Review freeze timestamp and measured token checkpoint are in freeze_record.json and accounting_record.json.
- Dispatch packet SHA-256: 720a63509f322cdb8bf5d25d9bfd9b31a43849b22b0b0b3895914cc4a2e818d5.
- Reviewed proof SHA-256: e3f403b4c55b69845e83ea74d7348026a86cd9b36691b1a4cdc9a6983ac3df5f.
- Active S1 SHA-256: 1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8.
- Submission allowance: v04 is submission four of four. No amendment or counter reset is assumed.
- Context received: the exact packet; frozen governing instructions, target history and proof-reviser skill/references; the current proof; supplied v01–v03 mathematical snapshots and concrete issue tables; two assigned seed extracts; the neutral realisability dossier. All 53 packet/input hash checks passed.
- Context excluded: other tracks, full prior review reports, author/coordinator conversations or deliberations, private work, unassigned seed material, other chats and old runs. No delegation occurred. Only own allowlisted runtime metadata were inspected for accounting.

## Correctness verdict and scope

**The reviewed informal mathematical argument establishes the exact active S1 statement. Submission v04 passes S1.** I found no unresolved mathematical obligation needed for its theorem. This verdict concerns the frozen submission above, including its whole-space law, every independently prescribed positive pair \((\lambda_0,M)\), the three exact full factorial densities on all the prescribed nondegenerate shape domains, global absolute continuity without singular mass, and globally finite-almost-everywhere densities through order four.

The proof also establishes finite third count moments on every bounded set and infinite fourth count moments in every nonempty open ball. These are compatible with almost-sure local finiteness and the definition of S1.

The decisive change is an actual sphere-based law with a freely adjustable internal scale. Its lower-density deficits become small in the anchored integrals needed by a finite-cluster correction, while its intensity and leading coefficients remain fixed. The internal scale does not shrink the prescribed domain or change the prescribed intensity. A whole-law mixture combines the two processes without superposition cross terms.

This is a natural-language proof review, not machine certification or a novelty assessment. It does not establish S0; S0's separately recorded verdict is unchanged. The unapproved low-intensity proposal is unnecessary to this proof and remains unadopted. The historical first three submissions are not retrospectively counted as S1 passes.

## Reconstruction and detailed audit

Equation numbers and section numbers below refer to proof_snapshot.md unless an earlier version is explicitly named.

### 1. Quantifiers and joint parameter feasibility

Start with arbitrary fixed \(\lambda=\lambda_0>0\) and \(M>0\). The definitions
\[
\kappa=(36e\pi M^3)^{-1},\qquad
\lambda_C=\min\{\lambda,\kappa/2\},\qquad
\lambda_Y=2\lambda-\lambda_C
\]
give strictly positive finite component intensities and \(\lambda_C\le\kappa/2\). They impose no upper bound on \(\lambda M^3\).

Choose finite \(K>0\) so that, with
\[
C_0=\frac{\pi^{3/2}}{3\sqrt3},\quad
c=\sqrt{\frac{C_0K^3}{\lambda_Y}},\quad
F=\frac{K^4}{c^3},
\]
we have \(FM\le10^{-4}\). Since \(F=\lambda_Y^{3/2}/(C_0^{3/2}\sqrt K)\), such a finite \(K\) exists for every original parameter pair. The displayed example in (4) indeed gives equality. The coefficients
\[
A_2=\frac{\pi K^2}{4c},\qquad A_3=\frac{K\sqrt\pi}{8}
\]
are already fixed, positive and finite before \(L\) is chosen.

The later choice
\[
L=\max\left\{M,\frac{128\pi^2A_3M^5}{\lambda_C},
M^2\sqrt{\frac{2\pi A_2}{\lambda_C}}\right\}
\]
is finite. In (41) its second entry bounds the first summand by \(\lambda_C/4\), and its third entry bounds the second summand by \(\lambda_C/4\). Thus \(Q_2\le\lambda_C/2\). The sphere probability budget is uniform over every \(L\ge M\), as checked next; consequently the order of these choices is legitimate. No parameter needed to define \(K,c,A_2,A_3\) depends on this later \(L\).

This is a finite-parameter construction for each prescribed pair. No limiting process or dilation argument is required.

### 2. Uniform band probabilities and an actual stationary sphere law

For \(H=2M\), \(b_k=2^kM\), \(P_k=4b_k+2M\), and the bands (6), set
\[
\gamma(R)=\frac{2FR}{L^4}e^{-4R^2/L^2},\qquad
p_k=HP_k^3\sup_{I_k}\gamma.
\]
The bounds \(P_k\le6b_k\), \(R\le b_k\), and \(R>b_k/2\) for \(k\ge1\) give
\[
p_0\le864FM(M/L)^4,\qquad
p_k\le864FM\,t_k^4e^{-t_k^2},\quad t_k=b_k/L.
\]
For the dyadic terms at most one, the fourth powers sum to at most \(16/15\). If \(t_*>1\) is the first larger term, then
\[
\sum_{t_k>1}t_k^4e^{-t_k^2}
\le\sum_{j\ge0}\frac{6}{(2^jt_*)^2}
=\frac8{t_*^2}\le8.
\]
Here \(e^{t^2}\ge t^6/6\) suffices. Hence
\[
\sum_kp_k\le864FM(1+16/15+8)<9000FM\le0.9.
\]
The estimate is uniform in the subsequently selected \(L\). The empty alternative therefore has positive probability, and the thinning probabilities in (11) lie in \([0,1]\).

Conditional on a band, the randomly translated lattice and single uniform radial phase define a countable family of candidate spheres. For a nonnegative test \(g(z,R)\), the lattice average gives \(P_k^{-3}\int dz\), and the radial phase gives \(H^{-1}\int_{I_k}dR\). Multiplication by \(p_k\) and by the retention factor \(\gamma HP_k^3/p_k\) yields exactly
\[
\mathbb E\sum_{\text{retained }(z,R)}g(z,R)
=\int_{\mathbb R^3}\int_0^\infty g(z,R)\gamma(R)\,dR\,dz.
\]
This uses only the first sphere-parameter measure; it does not assert independence of sphere parameters.

The law is invariant under every spatial translation. A translation changes the uniform lattice shift modulo its period and permutes the indices of conditionally identically distributed independent retention marks. It does not change the radial phase law. A random orientation of the lattice is unnecessary because S1 requires stationarity, not isotropy.

Concentric candidate surfaces are separated by at least \(2M\). Surfaces with different centres in band \(k\) are separated by at least
\[
P_k-2b_k=2b_k+2M>M.
\]
Thus all points in any tuple of diameter below \(M\) must belong to one sphere. The assertion concerns surfaces, not just centres, and remains true after thinning.

The conditional point processes on the spheres have finite means \(2\pi a(R)R\) and nonatomic surface intensity. In a realised band, only finitely many centres and radial indices can influence a bounded spatial set. Their union is therefore simple and locally finite almost surely; countable exhaustion supplies the simultaneous whole-space statement. These observations justify an actual measurable point-process law without a moment realisability theorem.

The intensity computation is exact:
\[
\int_{\mathbb R^3}\sigma_{z,R}(B)\,dz=4\pi R^2|B|,
\]
\[
\frac{\mathbb E\Lambda(B)}{|B|}
=2\pi\int_0^\infty\gamma(R)a(R)R\,dR
=\frac{2\pi}{c^2}\int_0^\infty\sqrt q\,f(q)^3\,dq
=C_0K^3/c^2=\lambda_Y.
\]
All integrands are nonnegative; Tonelli applies before finiteness is concluded. The factors \(2R\) in the radius change and surface weighting are consistent.

### 3. Every sphere allocation and full global absolute continuity

Conditional on the sphere family, the union of its independent Poisson processes is a Poisson process with locally finite nonatomic directing measure \(\Lambda\). Thus the full ordered factorial measure is
\[
\alpha_Y^{(n)}=\mathbb E\Lambda^{\otimes n}.
\]
Expanding the sum defining \(\Lambda\) includes every ordered allocation of the labels to sphere indices, with repeated indices allowed. When an index is repeated, its retention indicator appears once after expectation, not to the number of its occurrences. The submission explicitly observes this distinction. It affects the allocation weight but not the rank argument.

For one band and one specified allocation, the positions are
\[
x_i=Z+P_km_i+(U+j_iH)\omega_i,\qquad \omega_i\in S^2.
\]
The parameter measure is a nonnegative measurable weight times Lebesgue measure in \(Z,U\) and product area measure in the directions. In angular coordinates, its weight contains the appropriate finite-radius factors from the surface measures; possible endpoints of phase cells or bands have parameter measure zero.

At positive radii the angular derivatives supply \(2n\) independent tangent directions in the \(n\) separate position blocks. The remaining normal derivative matrix in \(Z,U\) has rows
\[
(\omega_i^{\mathsf T},1).
\]
For \(n\le4\) these rows have rank \(n\) for product-area-almost every direction tuple. Indeed distinct unit directions are almost surely distinct; three are almost surely not collinear; and the affine plane of three noncollinear directions meets \(S^2\) in an area-null circle. The fourth direction almost surely avoids it. The corresponding lower-order rank statements follow as well.

Consequently the position map has rank \(3n\) almost everywhere. Around each full-rank point, a nonzero maximal minor gives coordinates in which the map is a projection. The inverse-function theorem and Fubini show that the preimage of every position-space Lebesgue-null set has zero parameter measure in such a chart. A countable chart cover, followed by the null rank-failure set, proves absolute continuity for the allocation. Countably many allocations and bands preserve this property.

This establishes zero mass on all Lebesgue-null configuration sets, including coincidences, collinearity, coplanarity and the later resonance sets. It is a full-measure result, not a conclusion inferred from formulas on the nondegenerate local domain.

There is no invalid appeal to a Radon–Nikodym theorem for an arbitrary non-sigma-finite measure. For each fixed band, local count moments of every order are finite: the number of influencing spheres is bounded for that band and bounded observation set, and
\[
2\pi a(R)R\le2\pi b_k\sup_{0<R\le b_k}a(R)<\infty.
\]
Each fixed-band factorial measure is locally finite and absolutely continuous, so has a density. Their nonnegative countable sum is an extended density for the mixture. Its finiteness almost everywhere requires the additional arguments below.

### 4. Finite third moments, with constants uniform across bands

For a fixed ball \(B(x,r)\), a contributing centre is in \(B(x,b_k+r)\). Its lattice spacing is at least \(4b_k\), and \(b_k\ge M\), so a cubical packing bound gives a finite number of possible centres depending only on \(r/M\), uniformly in \(k\). At a fixed centre, relevant radii lie in an interval of length at most \(2r\); a grid of step \(H=2M\) supplies at most \(\lfloor2r/H\rfloor+2\) candidates. The uniform finite surface-count constant \(J_B\) therefore exists.

The area bound \(\sigma_{z,R}(B)\le4\pi r^2=:C_B\) is valid, including very large and very small radii. For \(R\le r\), the entire sphere suffices. For \(R>r\), a nonempty intersection is a cap whose maximum area is at most
\[
2\pi R^2\left(1-\sqrt{1-r^2/R^2}\right)\le2\pi r^2.
\]
The no-intersection case is immediate.

Writing \(m_{z,R}=a(R)\sigma_{z,R}(B)/(2R)\), use
\[
\left(\sum m_{z,R}\right)^3\le J_B^2\sum m_{z,R}^3,\qquad
\sigma_{z,R}(B)^3\le C_B^2\sigma_{z,R}(B).
\]
The first sphere intensity and the centre integration then give
\[
\mathbb E\Lambda(B)^3
\le\frac{\pi J_B^2C_B^2|B|}{2}
\int_0^\infty\frac{\gamma(R)a(R)^3}{R}\,dR
=\frac{\pi J_B^2C_B^2|B|}{2}K\sqrt\pi<\infty.
\]
The identity \(\gamma a^3/R=2f(R^2)\) verifies the cancellation. It handles the endpoint \(R\downarrow0\) as well as the large-radius tail. Conditional Poisson moment identities now give finite third count moments, and hence globally finite-a.e. densities of orders two and three by bounded-box exhaustion.

### 5. Global finite-a.e. fourth density: the separate resonance proof

Absolute continuity alone does not imply that the fourth density is finite almost everywhere. The supplied additional proof resolves precisely this issue.

Fix a noncoplanar quadruple and write \(u_i=x_i-x_1\), with \(W\) the invertible matrix of the three row vectors \(u_i\). In a bounded configuration neighbourhood choose a common diameter bound \(D\) and keep \(W^{-1}\) bounded. Bands for which \(2b_k+2M>D\) cannot allocate this tuple to different centres. Any allocation in such a band must be concentric.

Use \(R>0\) for the radius of the sphere containing \(x_1\), and write the other radii as \(R+Hm_i\). The reverse triangle inequality gives
\[
|Hm_i|\le|u_i|\le D.
\]
Thus one fixed finite set of integer triples \(m\) covers every possible concentric allocation throughout the neighbourhood; it is independent of the band and of the absolute radial index.

If \(z\) is the common centre relative to \(x_1\), then
\[
|z|=R,\qquad |u_i-z|^2=(R+Hm_i)^2.
\]
Put \(b_i=|u_i|^2-H^2m_i^2\). Subtraction yields
\[
Wz=b/2-RHm.
\]
Dividing by \(R\) and taking the reverse triangle inequality proves
\[
R\left|1-H|W^{-1}m|\right|\le\tfrac12|W^{-1}b|.
\]
There is no assumption of a uniform bound on \(m\) over all of configuration space; the finite bound is obtained separately in each bounded neighbourhood.

The denominator can vanish only when \(H|W^{-1}m|=1\). For \(m=0\) this is impossible. For each fixed nonzero integer \(m\), after clearing denominators the condition is
\[
H^2|\operatorname{adj}(W)m|^2-(\det W)^2=0.
\]
This is a nonzero real polynomial: at \(W=tI\) it equals
\[
t^4(H^2|m|^2-t^2).
\]
Its zero set has Lebesgue measure zero, as follows from induction on dimension and Fubini applied to the coefficients of a one-variable polynomial. The coplanarity polynomial and the countably many nonzero \(m\)'s therefore give a null exceptional union in relative coordinates and hence in the original position coordinates.

At a quadruple outside this union, the finitely many relevant denominator gaps have a strictly positive minimum. Continuity permits one smaller bounded neighbourhood where they all remain bounded away from zero, \(W^{-1}\) is bounded, and each vector \(b\) is bounded. This proves one finite radius bound for every possible concentric allocation in every sufficiently large band on that entire neighbourhood. Since those bands have lower radius endpoints tending to infinity, all but finitely many bands assign the neighbourhood zero fourth measure. Different-centre allocations in those bands were already excluded.

The full fourth measure on this neighbourhood is therefore a finite sum of locally finite fixed-band measures. Its density is finite almost everywhere there. The family of these open neighbourhoods has a countable subcover of the good set by second countability; the corresponding union of exceptional density-null sets is still null. The original resonance/coplanarity union already has zero full measure by Section 3's independent absolute-continuity proof.

This establishes global finite-a.e. fourth density, including outside \(E_4(M)\). It does not claim finite fourth mass on a product ball that crosses the coplanarity locus. No pointwise-to-uniform shortcut, uncountable union of exceptional sets, or omitted large-band contribution is present.

### 6. Coarea formulas, constants, and the complete local laws

On \(E_n(M)\), separation eliminates every different-sphere allocation. The remaining full measure is exactly (27). With \(q=R^2\),
\[
\delta(|x-z|^2-q)\,dx=\frac{\sigma_{z,\sqrt q}(dx)}{2\sqrt q}
\]
in coarea notation, and the radius change gives
\[
w_n(q)=\frac{\gamma(\sqrt q)a(\sqrt q)^n}{2\sqrt q}.
\]
Substitution verifies \(w_1=f^3/c^2,\ w_2=f^2/c,\ w_3=f,\ w_4=c\).

The delta notation has an ordinary finite-dimensional change-of-variables interpretation on the regular incidence charts described in the submission. It is not an unspecified multiplication of distributions. One can localise the nonnegative tests with the radii bounded away from zero, use the nonzero constraint minors below, and exhaust the positive-radius domain. Every \(R>0\) is retained in that exhaustion, so it introduces no lower geometric cutoff.

For a pair of length \(d\), the first subtracted sphere equation fixes one centre coordinate with determinant \(2d\). The first constraint fixes \(q\) with determinant one. Polar coordinates in the two free centre directions supply \(\pi\,dq\), giving
\[
r_2(d)=\frac{\pi}{2d}\int_{d^2/4}^{\infty}\frac{f(q)^2}{c}\,dq
=\frac{\pi K^2}{4cd}e^{-d^2/(2L^2)}.
\]
For a triangle, the two subtracted constraints fix the in-plane centre at the circumcentre, with determinant \(4|u\times v|=8A\). The remaining centre coordinate is the signed normal height \(h\), giving
\[
r_3=\frac1{8A}\int_{\mathbb R}f(R_\triangle^2+h^2)\,dh
=\frac{K\sqrt\pi}{8A}e^{-R_\triangle^2/L^2}.
\]
This formula includes both signs of \(h\).

Four affinely independent positions determine one sphere, with strictly positive squared radius. The four constraints in \((z,q)\) have determinant
\[
8|\det(u_2,u_3,u_4)|=48V.
\]
Consequently \(r_4=c/(48V)\). The convention is ordered tuples throughout. No \(n!\), orientation factor, or additional sphere solution is missing.

Degenerate positions are handled by the independently proved full absolute continuity, rather than by assuming that the nondegenerate formulas determine all the measure.

### 7. The deficit bound remains uniform for degenerating triangles

The correction kernels (34)–(35) are symmetric, measurable and translation invariant, with diameter support below \(M\). For a pair \(0,de\), \(0<d<M\), let \(r\) be the perpendicular distance of the third point \(z\) to the pair line. The exact identities
\[
A(0,de,z)=dr/2,\qquad
R_\triangle=\frac{|z|\,|z-de|}{2r}
\]
give \(R_\triangle\le M^2/(2r)\) on the allowed triangle domain. For \(\varepsilon=M^2/(2L)\le M/2\),
\[
d\,q_3(0,de,z)
\le\frac{2A_3}{r}\min\{1,\varepsilon^2/r^2\}.
\]
Enlarge the domain to \(B(0,M)\). Its axial length at each cylindrical radius is at most \(2M\); the volume element is \(r\,dr\,d\theta\,dt\). Therefore
\[
d\int q_3(0,de,z)\,dz
\le8\pi A_3M\int_0^M\min\{1,\varepsilon^2/r^2\}\,dr
\le16\pi A_3M\varepsilon
=\frac{8\pi A_3M^3}{L}=B_L.
\]
The last integral is in fact \(2\varepsilon-\varepsilon^2/M\), so the stated bound is valid. This calculation includes arbitrarily small \(r\): the apparent \(1/r\) singularity is cancelled by the cylindrical volume element in that region. It is uniform in \(d\), including \(d\downarrow0\). The excluded collinear third points are a null set. For pairs outside \(E_2(M)\), the triangle kernel vanishes.

Thus \(\mathcal Mq_3\le B_LK_2\), whereas \(q_2\ge2B_LK_2\). It follows that
\[
F_3=q_3,\qquad F_2=q_2-\mathcal Mq_3\ge B_LK_2.
\]
No infinite quantities are subtracted. All the relevant anchored integrals are finite by this bound and by
\[
Q_2\le\frac{32\pi^2A_3M^5}{L}+\frac{\pi A_2M^4}{2L^2}.
\]
Positivity on positive-measure open configuration domains yields \(Z_3=Q_3>0\) and \(Z_2=Q_2-Q_3>0\). These are precisely the normalisations needed for the probability kernels.

### 8. Actual correction process, all parent factors, and its global measures

The retained-centre construction from v02 is restated and can be verified directly here. A Poisson parent process of intensity \(\eta=(36\pi M^3)^{-1}\) is thinned by the empty-ball condition of radius \(3M\). Poisson insertion and the void probability give intensity \(\eta e^{-1}=\kappa\). The centres are dependent, but have pairwise distance greater than \(3M\) almost surely.

With \(Q_2\le\lambda_C/2\) and \(0<Q_3<Q_2\),
\[
\beta=\lambda_C-Q_2+Q_3/2\ge\lambda_C/2>0.
\]
The size probabilities in (45) are valid, since
\[
\beta+Z_2/2+Z_3/6
=\lambda_C-Q_2/2+Q_3/6\le\lambda_C\le\kappa.
\]
The offset laws integrate to one. They are diffuse in all their relative coordinates and supported on clusters of diameter below \(M\). Different clusters have mutual point distance greater than \(M\).

For a \(j\)-point cluster, re-rooting at a selected point and permuting labels has absolute Jacobian one. Symmetry and translation invariance of \(F_j\) therefore give the same integrated density for each of the \(j!/(j-n)!\) ordered selections. In particular:

- Two-point clusters contribute \(2\kappa\pi_2F_2/Z_2=F_2\) at order two.
- Three-point clusters contribute \(6\kappa\pi_3\mathcal MF_3/Z_3=\mathcal MF_3\) at order two.
- Three-point clusters contribute \(6\kappa\pi_3F_3/Z_3=F_3\) at order three.
- There is no four-point selection from a cluster.

Since no local tuple can use different clusters, these are the full local densities \(q_2,q_3,0\). Only the retained-centre first intensity is used in these calculations; independent retained parents are not assumed. The first-order count is
\[
\kappa(\pi_1+2\pi_2+3\pi_3)
=\beta+Z_2+Z_3/2=\lambda_C.
\]

Outside the local domains the proof does not discard different-parent tuples. Attach the same independent marks to every original Poisson centre, and call the unthinned emitted process \(C^\sharp\). Then
\[
C\subseteq C^\sharp,\qquad C^\sharp(B)\le3\Pi(B^{+M}).
\]
The latter count has every finite moment. For \(C^\sharp\), label each tuple by its distinct parents; the Poisson parent factorial identity gives the sum over all set partitions in (52), with the same-parent kernels (51). This proves full absolute continuity. Finite local moments give finite-a.e. densities. The measure inequality \(\alpha_C^{(n)}\le\alpha_{C^\sharp}^{(n)}\) transfers both properties, globally, to \(C\).

The first intensity, size-mark construction, re-rooting factors, all-parent expansion and domination agree with the consequential v02 argument, independently of its earlier review status.

### 9. Full mixture identity, final coefficients and moment comparison

Select one complete whole-space law by a fair coin:
\[
\mathcal L(X)=\tfrac12\mathcal L(Y)+\tfrac12\mathcal L(C).
\]
Its stationarity, simplicity and almost-sure local finiteness follow from the two actual alternatives. Its intensity is
\[
\tfrac12(\lambda_Y+\lambda_C)=\lambda.
\]
For every nonnegative ordered-tuple test, conditioning on the coin gives the extended full-measure identity
\[
\alpha_X^{(n)}=\tfrac12\alpha_Y^{(n)}+\tfrac12\alpha_C^{(n)}.
\]
There are no cross-component tuples because this is a choice of law. Each selected law's internal allocations have already been included.

Adding the exact local densities gives
\[
\rho_X^{(2)}=\frac{A_2+2B_L}{2D},\qquad
\rho_X^{(3)}=\frac{A_3}{2A},\qquad
\rho_X^{(4)}=\frac{c}{96V}.
\]
These constants are configuration-independent, positive and finite. The finite mixture also preserves full global absolute continuity and finite-a.e. densities, so the formulas do not leave an unresolved singular component or an uncontrolled outside domain.

The moment conclusions follow independently of any finite-fourth convention. The two component laws have finite third local moments. For the fourth order, choose a smaller ball of diameter below \(M\) and a positive-measure family of base triangles with areas bounded above and away from zero. A uniformly small normal cylinder around an interior planar region stays inside that ball. In its normal coordinate \(h\), \(V=A|h|/3\); hence integration of the strictly positive coefficient times \(1/V\) contains \(\int_0^\varepsilon dh/h=\infty\). Tonelli proves infinite fourth factorial and raw moments in every nonempty open ball.

In particular the finite-fourth-local-moment comparison subclass is impossible, even though the broad S1 class has the construction above.

## Finding register

The register includes decisive verified checks as well as scope and presentation findings. No correctness defect requiring a repair was found.

| ID | Location | Precise mathematical finding | Consequence | Repair/status |
|---|---|---|---|---|
| P4v04-01 | (2)–(4), (30)–(31), (43), (54) | All parameters are finite and can be chosen in the stated order for every independently prescribed positive pair. | The earlier missing high-intensity regime is covered. | Verified exact S1 quantifiers. |
| P4v04-02 | (7)–(11) | The full dyadic probability sum is bounded by \(9000FM\le0.9\), uniformly in the later \(L\ge M\). | Sphere probabilities remain valid after making the deficits small. | Verified; no circular choice. |
| P4v04-03 | Sections 2–3 | The band law gives an actual stationary simple locally finite process and exact intensity \(\lambda_Y\); all sphere allocations are in \(\mathbb E\Lambda^{\otimes n}\). | A formal density hierarchy is not being used as a substitute for existence. | Verified. |
| P4v04-04 | (20)–(21) | The position map has rank \(3n\) almost everywhere for every allocation at \(n\le4\). | Full global absolute continuity, including zero mass on degenerate sets. | Verified by the chart argument. |
| P4v04-05 | (22)–(23) | Uniform surface-count and surface-area bounds give finite third local moments. | Orders two and three have finite-a.e. global densities. | Verified at small and large radii. |
| P4v04-06 | (24)–(26) and ensuing neighbourhood argument | Bounded diameter leaves finitely many integer differences; away from a countable polynomial-null union the radius bound is uniform on a neighbourhood. | Only finitely many bands contribute there, proving global finite-a.e. fourth density. | Verified separately from absolute continuity. |
| P4v04-07 | (27)–(32) | The exact constraint determinants are \(2D,8A,48V\), with ordered tuple and radius factors as stated. | The full sphere densities, including \(c/(48V)\), are correct. | Verified; no missing permutation factor. |
| P4v04-08 | (34)–(42) | Cylindrical integration bounds the triangle deficit uniformly through triangle degeneration and pair coalescence. | The residual kernels are nonnegative and have finite positive normalisations. | Verified; no geometric cutoff. |
| P4v04-09 | (44)–(52) | Mark probabilities, retained-parent intensity, ordered selection coefficients, and unthinned all-parent domination are valid. | Actual correction law has local densities \(q_2,q_3,0\) and all global regularity. | Consequential v02 dependency independently re-established. |
| P4v04-10 | (53)–(56) | The convex mixture gives an exact full-measure sum, prescribed intensity, and three positive reciprocal coefficients. | Exact S1 pass. | Verified; no independent-superposition cross terms. |
| P4v04-11 | End of Section 8 | The local reciprocal-volume law has infinite fourth mass in every open ball, while third local moments are finite. | Separate finite-fourth comparison is negative; local finiteness is unaffected. | Verified distinction. |
| P4v04-12 | Prior-work and response sections | Slab-specific obstructions retain their old hypotheses; the new sphere component is outside them. The old formal residual hierarchy remains unrealised but unused. | No contradiction or hidden old realisation premise. | Scope verified. |
| P4v04-13 | Section 3 and Section 4 transition | Countable allocation/band sums first give an extended density; finite-a.e. finiteness comes later. The proof supplies both arguments. | Correct, but readers must keep the two conclusions separate. | Optional exposition: introduce fixed-band densities explicitly before their countable sum. |
| P4v04-14 | Section 4 neighbourhood paragraph | The bounded diameter determines a finite relevant integer set before denominator gaps are minimised. | The required uniformity is valid. | Optional exposition: name this finite set and its positive minimum explicitly, as done in this report. |

## Prior-issue disposition

Prior issue tables were treated as questions to check. Their old status labels were not used as evidence. The new sphere law and the correction law were audited in full above.

### v01 issue table

| Earlier ID | Current disposition |
|---|---|
| R4-01 | The slab's vanishing reciprocal pair coefficient remains a failure of that old law. The new sphere law has \(d r_2(d)\to A_2>0\), and its residual is exactly corrected in the final mixture. It is not an adjustment within the old excluded slab class. |
| R4-02 | The old slab triangle factor remains nonconstant. The new triangle deficit is exactly (34), and the actual cluster law supplies it. Closed for the current process on all S1 parameters. |
| R4-03 | The old pointwise finiteness premise is meaningful for its canonical expected-product density. The current proof obtains explicit coarea versions and full measure identities; it does not rely on selecting arbitrary density values on a null ray. |
| R4-04 | The corrected non-strict slab estimate is valid at the endpoint. It is not used by the new sphere construction; current surface separation has its own strict bound \(>M\). |

### v02 issue table

| Earlier ID | Current disposition |
|---|---|
| R4-01, R4-02 | Current lower corrections are independently verified for every positive \((\lambda,M)\); no low-intensity domain is inherited. |
| R4-03, R4-04 | Canonical-version and endpoint corrections remain local to the replaced slab argument. No affected inference is imported into v04. |
| R4-05 | The all-intensity obligation is closed by the independently verified parameter construction and finite-probability law in v04. Historical v02 remains a restricted result. |
| R4-06 | The old ceiling applies to the specified slab plus separated small-cluster representation. Changing the base to the sphere law removes a stated hypothesis, rather than refuting that theorem or changing S1. |
| R4-07 | The consequential finite-cluster law is restated and re-established with current kernels and \(\lambda_C\). Dependence of retained centres causes no independence gap. |
| R4-08 | Current global regularity is proved afresh for the sphere component, and by all-parent domination for the correction. It is not inferred from the old slab result. |
| R4-09 | Exact mathematical sections and frozen hashes identify the reused correction argument; the current text also reproduces it. Approval labels are not premises. |
| R4-10 | The finite-third/infinite-fourth distinction remains valid and is proved directly for the current process. |

### v03 issue table

| Earlier ID | Current disposition |
|---|---|
| P4v03-01 | Closed for v04: every independent positive pair is covered. Historical submission three remains unsuccessful as an S1 construction. |
| P4v03-02 | The prior automatic-third-moment result is consistent with the new explicit finite-third calculation. Its coefficient inequality does not impose a universal intensity ceiling because the coefficient ratio is free. |
| P4v03-03 | The reciprocal-volume divergence is re-established by a positive-measure family of base triangles and normal integration. |
| P4v03-04 | The current process is a whole-law mixture, not either excluded independent superposition. The correct full allocations for its actual law are verified. |
| P4v03-05 | The old slab construction is not an essential v04 dependency. Its global resonance idea is replaced by a derived concentric-sphere equation and current radius bound. |
| P4v03-06, P4v03-07 | The prior arbitrary finite-fourth correction theorem retains both its specific slab base and its fourth-law assumptions. Here \(d r_2(d)\to A_2>0\), so its disappearing-slab coalescence premise cannot be substituted. No general S1 ceiling follows from that theorem. |
| P4v03-08 | The formal hierarchy remains a separate analytic result; it is not used to define the current process. |
| P4v03-09 | Realisation of that particular old hierarchy is still not proved by v04. It is an unused route, not a remaining obligation for the different explicit construction. |
| P4v03-10 | All consequential finite-cluster details have been rechecked with the new kernels, normalisations, probabilities and component intensity. |
| P4v03-11 | Dependencies are explicitly identified; no prior verdict is mathematical authority. |
| P4v03-12 | S1 is unchanged. The owner proposal is unapproved, supplies no premise and gives no attempt reset. |

The old slab and independent-superposition obstructions are not being promoted to general nonexistence. Conversely, the present pass does not assert that every previously excluded representation is now possible. The current proof uses a different base law.

## Amendment implications

No target amendment is needed for this result. The final theorem addresses the exact adopted S1 domains and full-measure requirements, with prescribed independent intensity and diameter and no lower geometric cutoff. The internal scale \(L\) is a construction parameter only.

The fourth-moment divergence does prove failure of the separately defined finite-fourth-local-moment comparison subclass. It does not prove any further lower-distance or altitude restriction necessary for the broad class.

The supplied S0-to-S1 record gives the historical authority and distinction between S0 and S1. This review does not re-audit unassigned obstruction reports, change their verdicts, or adopt the separate low-intensity proposal on the owner's behalf. No fifth submission is required or authorised by this review.

## Source and coding evidence

The central theorem is self-contained apart from standard elementary analytic and probability facts whose needed forms are supplied: Poisson factorial and insertion/void identities, Tonelli and monotone extension, finite-dimensional change of variables, local inverse-function coordinates, Gaussian integrals, and nullity of a nonzero polynomial's zero set. The review reconstructs the fragile applications explicitly.

The consequential earlier dependency is the finite-cluster mechanism in the supplied v02 snapshot, SHA-256 9a3befd21f85424fea521c9c817837f2d943a1a0862c0e1586541b93c5d559ac. Its law, probability budget, selection coefficients and global domination are all reproduced and verified in v04. The supplied v01/v03 snapshots and concrete issue tables were inspected to establish the scope of replaced arguments and previous obligations; full prior review reports were not read.

The two assigned seed extracts were read as historical leads. Neither an unproved seed claim nor the seed's cumulant formula supplies an existence premise here.

The neutral dossier, its evidence summary and open-questions file were read. They describe mismatches of inspected sufficient realisability criteria, rather than a nonexistence result. The v04 proof does not invoke those criteria. I have not independently repeated that dossier's primary-literature search or certified exhaustiveness, current open status, priority or novelty. None is needed for this construction verdict.

No numerical experiment, symbolic package, external search, simulation, or proof assistant was used to support the mathematical verdict. No source or computational request remains outstanding. Programmatic work was confined to file hashes, assigned report production, and own metadata/accounting extraction.

## Presentation judgement

The submission is sufficiently explicit and self-contained to support this review. Its order—actual law, global measures, exact local formulas, residual law, mixture—makes the main dependencies recoverable. It correctly distinguishes a singular conditional surface measure from an absolutely continuous averaged factorial measure.

The two optional improvements in P4v04-13 and P4v04-14 would make the most fragile regularity passage easier to read: write the fixed-band densities and their countable sum explicitly, and name the finite integer set and denominator minimum used in the local radius bound. The proof already contains the mathematical reasons; these are exposition improvements, not repairs needed for the verdict. A separate schematic of parameter dependencies could also help a longer manuscript, but is not needed here.

## Review summary and remaining obligations

The decisive checks all close: a uniform band probability budget; a genuine stationary sphere process with exact intensity; full-rank pushforwards for every allocation; an independent finite-band argument proving global finite-a.e. fourth density; the \(2D,8A,48V\) constraint determinants; a deficit estimate uniform through degenerate triangles; valid finite-cluster probabilities and all-parent domination; and the final exact whole-law mixture.

There is no unresolved mathematical obligation for the stated v04 theorem. Realising the unused v03 formal hierarchy, proving an isotropic or ergodic variant, classifying other domains or constructions, and establishing novelty are not part of this pass. This is not a final cross-track synthesis.

## Accounting and review limitations

Before mathematics, own runtime session_meta identified this reviewer and own turn_context line 8 recorded gpt-6-astra/xhigh. The identified rollout is:

[local path omitted]

Only allowlisted session_meta, turn_context, token_count and task_complete metadata were considered; conversation or private reasoning contents were not read or retained. The preflight token event at line 32, timestamp 2026-10-20T19:15:29.072Z, exposes cumulative input 110997, cached input 67072, cache-write input 0, output 938, reasoning output 67 and total 111935. These are measured runtime counters, not estimates.

The checkpoint precedes the operational research boundary; it does not provide an exact preparation-versus-mathematics token partition. The latest available measured checkpoint and its coverage are saved in accounting_record.json. Cumulative snapshots are not summed; reasoning tokens are not added again to inclusive output. No children were spawned. General parent/child aggregation semantics, completed-turn totals before the final response, monetary charges and API-equivalent costs are NR. The coordinator must reconcile the final response tail after completion from the identified own rollout's permitted metadata.

Hash validation and review freeze records are separate assigned artifacts, avoiding a self-referential report hash. No usage estimates or private chain-of-thought are included.
