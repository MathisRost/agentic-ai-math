# Review — proof_3 / submission v02 / S1

- Reviewer: `/root/review_proof_3_v02`; session `session-17`; turn `turn-29`.
- Requested and verified runtime: `gpt-6-astra`, `xhigh`. Own-session `turn_context`, line 8, verifies both. The session metadata identifies this reviewer and the assigned working directory. Numeric token telemetry was verified before mathematics; see `preflight.json`.
- Type: fresh independent extensive review of the second frozen submission, including its consequential prior dependencies and the supplied concrete issue list. No author conversation or private work, full prior review, other construction track, or old chat was read. No delegation occurred.
- Review date: 20 October 2026. Exact preflight, freeze and accounting timestamps are recorded separately.
- Setup root: `$SETUP`.
- Run root: `runs/20261020T164437Z_astra6`. Paths below are relative to this run unless stated otherwise.
- The frozen reviewer instructions, accounting rules, workflow, proof-reviser skill and both complete skill references govern this review.

| Item | SHA-256 |
|---|---|
| Main review packet, `packets/review_proof_3_v02.json` | `4e18aa40d8527a4024ee60895b5742f4fd6da764e60506bc31d3709caf424a4c` |
| Active S1, `statements/S1.md` | `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8` |
| Adopted amendment, `statements/S0_to_S1.md` | `b2534040520dfc63bf5c22ecc508257308e619a040a7c6c54ce44375742394de` |
| Current proof, `reviews/proof_3_v02/proof_snapshot.md` | `8b111ffca00675eb5b0cd0e14dc5b8f041698d207630b687c8fbd9049ea181b8` |
| Prior proof dependency, `reviews/proof_3_v02/prior_dependency_v01.md` | `77ab351888c26bb524f694c8eb2f191e0775dfcdc152d8d077adca99a7363736` |
| Concrete prior issue list | `d164c32694a0f8172f65198ca9645cf79324a494fefcdae634202ae5260804a9` |
| Additional source packet, `packets/review_proof_3_v02_source_01.json` | `ba99ab141940c1421447746116222ba3f20569d8b60eefbd6511e7faaa203e1f` |
| Exact cited seed Section 5 | `33d1beb4f10940ad56067e341898fdb5ad5fd19b4bd11db8222f336de79a8432` |

All 25 allowed files in the main packet and the additional Section 5 excerpt were hash-verified. The original source outside the authorised excerpts was not opened. Prior approval labels were not used as evidence.

## Correctness verdict and scope

**The submission does not pass S1. It establishes a valid partial construction and valid obstructions confined to its specified marked branching family.** The supplied informal proofs of these results are complete after the elementary reconstructions given below. I found no invalid mathematical step affecting those stated results.

The concrete model is a stationary, isotropic, simple, locally finite process on all of \(\mathbb R^3\), with any prescribed positive intensity and any independently prescribed positive length \(L\). Its full factorial measures through order four are absolutely continuous with globally finite-almost-everywhere densities. Its third local count moments are finite, and its fourth moments are infinite on every nonempty open ball. Its four-children contribution has the exact **damped** reciprocal-volume formula (2); its full density is (18).

The submission also correctly proves that this concrete process fails the full reciprocal fourth law on every \(E_4(M)\), and that the larger radial-productivity family (26)–(27) fails the reciprocal pair law on every \(E_2(M)\). These negative statements hold for every positive prescribed intensity and every \(M>0\), within their respective model classes. They are not general non-existence results for S1.

This is substantive submission **2 of 4**, and the second unsuccessful exact-target submission. Two submissions remain under the unchanged counter. The correctness of its partial results does not convert it into an exact-target success. No amendment is requested or authorised by this review.

The review covers the entire mathematical argument in v02, its source attribution, the inherited partition and moment principles, the relevant v01 obstruction and projection clarification, and the comparison with the supplied seed scopes. It does not certify the full old seed construction theorems, inaccessible prior reviews, any literature-priority claim, or general S1 realisability.

## Reconstruction and detailed audit

### 1. Target and the relevant moment class

The active target is the adopted S1, with independently prescribed \((\lambda_0,M)\), all three full reciprocal densities, all nondegenerate configurations of diameter less than \(M\), and no lower geometric cutoff. Its global absolute-continuity and finite-almost-everywhere requirements apply even outside those formula domains. No finite-fourth-moment condition is present.

The necessary local moment distinction can be checked without accepting an earlier verdict. If a ball \(B\) has diameter below \(M\), then for almost every base triple in \(B^3\), its area \(A\) is positive. In orthogonal coordinates for the fourth point near the base plane,
\[
V=A|t|/3,\qquad dx_4=d\sigma\,dt.
\]
A small cylinder about an interior point of the base plane lies in \(B\). Its integral of \(1/V\) diverges as \(\int_{0<|t|<\delta}dt/|t|\). Tonelli yields an infinite fourth factorial moment. Every open ball contains a ball of diameter below \(M\).

In contrast, for bounded \(Q\) of diameter below \(M\),
\[
\int_{Q^2}D^{-1}\leq2\pi\,\operatorname{diam}(Q)^2|Q|,\qquad
\int_{Q^3}A^{-1}\leq16\pi^2\,\operatorname{diam}(Q)^4|Q|.
\]
For the triangle estimate, cylindrical coordinates about \(x_2-x_1\) cancel the transverse radial singularity. The identity \(N^3=(N)_3+3(N)_2+N\) and a finite cover by small sets then give finite third moments for every bounded set under S1. Thus the concrete model's moment class is appropriate, although this is far short of the required identities.

### 2. Actual marked process and arbitrary intensity

In v02 Section 1, \(Q_v=I+vv^T\) has eigenvalues \(1,1,1+|v|^2\). The density \(f_{v,L}\) in (5) is correctly normalised. The marked immigrant measure is finite on bounded spatial regions because
\[
\int_{\mathbb R^3}(1+|v|^2)^{-11/2}\,dv=64\pi/315.
\]
Conditional on a finite mark \(v\), the Poisson offspring count is finite almost surely. Its Gaussian covariance is \(L^2Q_v^{-1}/2\), so the count and the spatial thickness are indeed coupled through the mark. Conditional independence within each family is stated at the correct level; the unconditional offspring geometry is not one fixed count-independent density.

The two intensity integrals in (8) follow directly from the beta integral (7):
\[
\int a^{-11/2}=64\pi/315,\qquad \int a^{-9/2}=32\pi/105.
\]
Their sum is \(32\pi/63\). Integrating each translated child density over all root locations gives
\[
\mathbb EX(B)=c(32\pi/63)|B|.
\]
Consequently \(c=63\lambda_0/(32\pi)\) is correct. The separate root and child intensities are \(2\lambda_0/5\) and \(3\lambda_0/5\), respectively. No root population is lost.

Finite expectation of bounded counts implies their almost-sure finiteness. A countable exhaustion by balls gives simultaneous local finiteness on the whole space. This argument is needed because Gaussian displacements are unbounded; it does not assume a bounded set has only finitely many potentially contributing parents.

The immigrant process has countably many parents, and each family is finite. Root pairs are diffuse Poisson pairs; every pair involving a child has a diffuse remaining displacement after conditioning on the relevant marks, counts, parents and other displacements. A countable union gives simplicity. Translation covariance gives stationarity. Rotating both \(v\) and the spatial coordinates preserves the immigrant intensity and the conditional offspring law, giving isotropy.

Every step holds for every \(\lambda_0,L>0\). Setting \(L=M\) is legitimate for these structural properties, but does not establish the reciprocal identities.

### 3. Third moments and infinite fourth family size

For \(T=1+K\), direct Poisson moment expansion gives
\[
\mathbb E[T^3\mid v]=1+7a+6a^2+a^3.
\]
After multiplication by \(ca^{-11/2}\), the least decaying term is \(ca^{-5/2}\), integrable in three dimensions. Thus the immigrant-mark-integrated third family moment is finite.

For a realised finite family, \(N_z=C(B-z)\leq T\) and
\[
\int N_z^j\,dz\leq T^{j-1}\int N_z\,dz=|B|T^j .
\]
This is a translation identity, not a spatial-support bound. Integrating over marks and family randomness yields finite \(\Psi_1,\Psi_2,\Psi_3\). Expanding a finite-region Poisson family sum gives precisely
\[
\mathbb EX(B)^3=\Psi_3+3\Psi_2\Psi_1+\Psi_1^3.
\]
Increasing the parent regions and applying monotone convergence justifies the whole-space version. Formula (12) is valid.

The assertion that the unconditional fourth family-size moment is infinite also follows directly: its leading conditional term is \(a^4\), so the corresponding mark integral is proportional to \(\int a^{-3/2}dv=\infty\). This alone would not prove infinite fourth local moments; v02 correctly supplies a separate geometric argument for those moments.

### 4. All within-family genealogies and Gaussian factors

The one-generation family contains one observed root and sterile children. An ordered distinct \(n\)-tuple from one family therefore contains either \(n\) children, or one root at one of \(n\) specified labels and \(n-1\) children. These cases are exhaustive and disjoint.

The conditional child counts contribute \(\mathbb E(K)_n=a^n\), or \(\mathbb E(K)_{n-1}=a^{n-1}\). There is no extra \(n!\): labels are already ordered. In the root-containing case, summing over the \(n\) possible root labels is required and is present in (16).

For children only, completing the square in the root coordinate gives
\[
\int e^{-\sum_j(x_j-z)^TQ_v(x_j-z)/L^2}\,dz
=\pi^{3/2}L^3n^{-3/2}a^{-1/2}
 e^{-\operatorname{tr}(Q_vS_n)/L^2}.
\]
Combining the mark weight, the Poisson factorial moment, and all \(n\) Gaussian normalisations yields the exponent
\[
-11/2+n+n/2-1/2=3(n-4)/2.
\]
This verifies every power and prefactor in (15). For a root-containing tuple the exponent is
\[
-11/2+(n-1)+(n-1)/2=(3n-14)/2,
\]
which verifies (16). In particular, the formulas at \(n=1\) recover the distinct root and child intensities.

These are identities for nonnegative measures, proved before asserting finiteness. A fixed root inside one family does not cause singular mass in the global tuple measure: its location is integrated against spatial Lebesgue measure; the remaining selected positions have conditional densities. For children-only selections the unobserved root is also integrated. Tonelli therefore supplies genuine densities for all components.

### 5. All immigrant partitions and full measure identities

An observed ordered tuple has a unique partition by its parents. Ordering blocks by their least labels and using the Poisson factorial measure of distinct parents gives the product of the corresponding same-family densities. This produces (17), with no block-order factorial.

At order four the partition types have multiplicities
\[
1\quad(4),\qquad4\quad(3+1),\qquad3\quad(2+2),
\qquad6\quad(2+1+1),\qquad1\quad(1+1+1+1).
\]
Thus (18) contains all fifteen partitions. The block of size four is itself \(C_4+R_4\). Lower-order blocks similarly contain both genealogies. There is no missing parent allocation, root allocation or nonnegative background term.

All exchanges are nonnegative sums or integrals. The convention \(0\cdot\infty=0\) agrees with increasing bounded truncations and with the original nonnegative product integrals. The argument does not require locally finite fourth factorial mass. Each full measure assigns zero to every Lebesgue-null set because the identity is an integral of a density; a divergent local integral does not add a singular component.

### 6. Reciprocal-volume coefficient and global finite-a.e. regularity

Writing \(E=[x_2-x_1,x_3-x_1,x_4-x_1]\), the scatter identity is
\[
S_4=E(I-\mathbf1\mathbf1^T/4)E^T.
\]
The middle matrix has determinant \(1/4\), while \(|\det E|=6V\). Hence
\[
\det S_4=9V^2,\qquad \sqrt{\det S_4}=3V.
\]
The \(a\)-power in (15) vanishes at \(n=4\). Gaussian integration then gives exactly
\[
C_4=\frac{c}{24\pi^3L^6}\frac{e^{-\operatorname{tr}(S_4)/L^2}}{V}.
\]
The factors \(4^{3/2}=8\), \(3V\), \(\pi^{3/2}\) and \(L^3\) all enter with the stated signs and powers. This is the children-only same-family contribution, not the full density.

For noncoplanar quadruples all \(T_{4,i}\) are positive definite, so their \(a^{-1}\)-weighted Gaussian integrals are finite. At order two the weights \(a^{-3}\) and \(a^{-4}\) are integrable even without Gaussian damping, giving a global bound. At order three the root weight \(a^{-5/2}\) is integrable. For a noncollinear triple, the two positive eigenvalues of \(S_3\) give the bound used in the proof, and
\[
\int_{\mathbb R}(1+|w|^2+t^2)^{-3/2}\,dt
=\frac{2}{1+|w|^2}.
\]
The remaining two-dimensional Gaussian integral is finite. Every face of a noncoplanar quadruple is noncollinear, so every term in (18) is finite there.

Coincidence, collinearity and coplanarity sets are Lebesgue-null in the appropriate product spaces. It follows that the full densities through order four are finite almost everywhere on the entire configuration spaces, including outside every prescribed diameter domain. Setting density values to zero on exceptional null sets does not change the measure. The process therefore meets S1's global density regularity requirement, although it fails its formulas.

### 7. Infinite fourth local moments

On \(B^4\) for a bounded nonempty open ball \(B\), \(\operatorname{tr}S_4\) is bounded above, so the exponential factor has a uniform strictly positive lower bound. The local reciprocal-volume calculation in subsection 1 therefore gives
\[
\int_{B^4}C_4=\infty.
\]
Since this is a nonnegative submeasure of the full fourth factorial measure, \(\mathbb E(X(B))_4=\infty\). The inequality \(X(B)^4\geq(X(B))_4\) gives the infinite raw fourth moment. Equation (20) states that both expectations are infinite; it is not an identity between falling and ordinary fourth powers in general.

This argument is compatible with both almost-sure local finiteness and finite third moments. It also proves divergence near ordinary coplanarity, not merely at repeated points. The construction genuinely avoids the too-large positive-measure infinite densities that obstructed the count-independent v01 model.

### 8. Full coplanar limit and failure of the fourth identity

At a coplanar quadruple with all four faces noncollinear, each \(T_{4,i}\) has rank two. Its two positive eigenvalues remain bounded below in a sufficiently small neighbourhood. Because the weight \(a(v)^{-1}\) is radial, diagonalising matrices that depend on the configuration causes no loss of uniformity:
\[
\int_{\mathbb R^2}\int_{\mathbb R}
\frac{e^{-\delta|w|^2}}{1+|w|^2+t^2}\,dt\,dw
=\pi\int_{\mathbb R^2}\frac{e^{-\delta|w|^2}}{\sqrt{1+|w|^2}}\,dw<\infty.
\]
This proves the uniform bound for \(R_4\). All faces remain noncollinear, giving uniform bounds for their \(C_3\) terms; \(R_3\) and \(c_2\) already have global bounds. Therefore the full remainder \(B_4\) in (21) is uniformly bounded. The proof does not improperly subtract infinities: the nonnegative expansion defines the remainder wherever needed.

Multiplication by \(V\) then kills every remainder term. The resulting limit (23) is a statement about the **full** fourth density and holds along every noncoplanar approach to the stated quadruple.

For the squares \(\mathbf q_s\), the diameter is \(\sqrt2s\), every face is nondegenerate, and \(\operatorname{tr}S_4=2s^2\). Almost-everywhere equality on \(E_4(M)\) would force
\[
a_4=\frac{c}{24\pi^3L^6}e^{-2s^2/L^2}
\]
for every \(0<s<M/\sqrt2\). The argument correctly handles the fact that the square itself is outside \(E_4(M)\): every sufficiently small neighbourhood has a positive-measure open subset of noncoplanar configurations with diameter below \(M\), so sequences avoiding the exceptional null set exist. Two different \(s\) give a contradiction. No continuity of an arbitrary version of the full density is being assumed.

This is a complete proof that the concrete model fails the fourth identity by itself. Positivity of the remaining terms cannot repair the varying leading coefficient because those terms have just been proved bounded in these limits.

### 9. Pair bound, and a supplementary third-order diagnostic

The pair bound (25) is also exact as an upper bound. The integrals are
\[
\int a^{-3}\,dv=\pi^2/4,\qquad \int a^{-4}\,dv=\pi^2/8.
\]
Thus \(C_2\leq c\sqrt\pi/(8\sqrt2L^3)\) and \(R_2\leq c\sqrt\pi/(4L^3)\), with the independent-parent term \(\lambda_0^2\) added. A bounded density cannot agree almost everywhere with \(a_2/D\) for positive \(a_2\) at arbitrarily small separations.

For completeness, the concrete model also fails the triangle law individually. This additional diagnostic follows from its displayed formulas and is not needed for either submitted obstruction. Near any collinear triple of distinct points, \(S_3\) has at least one eigenvalue uniformly bounded below. Split \(v=(w,t)\in\mathbb R\times\mathbb R^2\) along that eigenvector. The children integral is uniformly bounded by
\[
\int_{\mathbb R}e^{-\delta w^2}
\left[\int_{\mathbb R^2}(1+w^2+|t|^2)^{-3/2}\,dt\right]dw
=2\pi\int_{\mathbb R}\frac{e^{-\delta w^2}}{\sqrt{1+w^2}}\,dw<\infty.
\]
Together with globally bounded \(R_3\) and \(c_2\), this bounds the full third density near that triple. Choosing the triple's diameter below \(M\), almost-everywhere equality with \(a_3/A\) contradicts \(A\to0\), by the same exceptional-set argument as above. The concrete model therefore does not accidentally satisfy one of the unexamined exact laws.

### 10. Arbitrary measurable radial productivity

Section 5 is a distinct theorem, not an assertion that all members of the larger family satisfy the concrete model's moment and density regularity properties. Its assumptions are explicit: the same Gaussian geometry, one sterile generation, Poisson parents and conditional offspring, finite-valued measurable radial \(b\geq1\), the precise mark weight (26), and \(0<J_\lambda<\infty\).

Condition (27) integrates the root and child intensities together, so it implies both finite immigrant rate and finite positive total intensity. The preceding whole-space existence and simplicity arguments apply. No uniform bound on \(b\), third moment or fourth moment has been assumed. The cancellation
\[
\mu_b(dv)b(|v|)^4a(v)^{3/2}=c\,dv
\]
preserves the stated \(C_4\) formula, with the new intensity normalisation \(c=\lambda_0/J_\lambda\). It does not by itself preserve finiteness of all full higher-order densities; the submission does not claim that it does.

For two children the remaining mark weight is \(b^{-2}a^{-1}\); for a root and a child it is \(b^{-3}a^{-1}\). The relative Gaussian exponents are respectively \(-D^2/(2L^2)\) and \(-D^2/L^2\). This verifies (28)–(29), including the factor two for the root label. The full pair measure has exactly the additional independent-parent term \(\lambda^2\).

The angular integration is \(2\pi F(\sqrt\gamma rd)\). The bounds on \(F\) follow by integration over \([-1,1]\), or its subinterval \([-1/u,1/u]\), and comparison with the whole real Gaussian integral. They are uniform upper and lower comparisons with \(\min(1,u^{-1})\).

If \(J_2=\infty\), its integral on every bounded radial interval is finite because \(b\geq1\). Its divergent tail, together with the lower angular bound, gives \(I_2(d;\gamma)=\infty\) for **every** \(d>0\). This is an extended pair density infinite on the full off-diagonal, not merely an infinite local integral. It violates S1.

If \(J_2<\infty\), the inequality
\[
d\,F(\sqrt\gamma rd)\leq C_\gamma r^{-1}\min(rd,1)
\]
for \(r>0\) gives (32). The dominating weight is \(r(1+r^2)^{-1}b(r)^{-2}\), integrable by assumption; for \(\beta=3\) it is only smaller. Dominated convergence proves both limits in (33), and the same inequality proves finiteness of both pair integrals for each \(d>0\). Restoring \(D=Ld\) and the finite baseline term gives \(D\rho_b^{(2)}(D)\to0\).

Stationarity and radiality make equality of the full configuration densities equivalent to the required radial equality outside a one-dimensional Lebesgue-null set on \(0<D<M\), by translation coordinates and polar integration. The limit zero is incompatible with a positive constant on almost every such radius. This completes the stated dichotomy without count-moment assumptions or a hidden continuity assumption on \(b\).

### 11. Re-established v01 dependencies and the supplied prior findings

The present proof does not merely cite v01 for its new formulas: it rederives them. Nevertheless the following inherited assertions were independently checked.

For arbitrary finite Poisson clusters, \(\int C(B-z)\,dz=|B|T\), the bound on integrated powers, and the Poisson parent partition formula hold independently of any bounded support or internal positional independence. These are precisely the principles used in v02.

The v01 fixed-kernel obstruction is also sound within its stated class. Finite positive intensity forces \(m=\mathbb EK<1\) because the integrated generation means are \(\nu|B|m^j\). When \(\mathbb EK^4<\infty\), the finite-generation moment recursion has only the coefficient \(m\) multiplying the same-order previous moment; all other terms involve lower moments. Induction and monotone convergence give \(\mathbb ET^4<\infty\), and the translation bound gives finite fourth local count moments. When \(\mathbb EK^4=\infty\), direct immigrant siblings contribute \(\nu\mathbb E(K)_4H_4\). For any positive-volume bounded \(B\),
\[
0<\int_{B^4}H_4=\int\left(\int_Bf(x-z)\,dx\right)^4dz\leq|B|.
\]
Thus \(H_4>0\) on positive measure, and the sibling submeasure has infinite density there. On a ball of diameter below \(M\), a positive-measure bounded-density sublevel set of \(a_4/V\) gives the precise measure contradiction. This uses independence of offspring counts and the common spatial kernel, which the marked v02 law lacks.

The v01 tree-density representation integrates unobserved root coordinates and all unobserved vertices with unit Jacobian; its set-partition expansion is consistent with the specialised v02 calculation. Its finite-time space-time projection conclusion also holds. The new clarification handles pairs of roots by the diffuse Poisson second factorial measure on equal-spatial-coordinate sets. For every other vertex pair a remaining edge has a diffuse spatial marginal. Countable exhaustion and the finite-window moment bound complete that projection argument.

The prior issue list is resolved or retained as follows:

| Prior ID | Independent outcome in this review |
|---|---|
| P3-R01 | Still open as the exact S1 obligation. New structural and negative results are established, but no target process is constructed. |
| P3-R02 | Scope remains explicit. The old fixed-kernel result and the new radial marked result exclude different specified subclasses; neither excludes general S1. |
| P3-R03 | Rechecked from the definitions: both within-family cases and all immigrant partitions are present, with correct ordered counts. |
| P3-R04 | Rechecked: finite third and infinite fourth local moments coexist with finite-a.e. full densities for the concrete law. The larger family's infinite-pair branch is kept separate. |
| P3-R05 | The root-pair clarification at v02 lines 575–583 is correct and closes the stated exposition omission. Projection is not used in the new construction. |
| P3-R06 | The authorised cluster-law excerpt explicitly states at most four points per parent. The finite-family moment bound verifies the resulting inability to extend that representation to all of S1. No approval of the complete seed theorem is inferred. |

## Finding register

| ID | Location | Precise mathematical issue | Consequence | Repair/status |
|---|---|---|---|---|
| P3-V02-01 | Exact claim; Sections 4–5; lines 594–651 | No simultaneous reciprocal full-density construction is supplied. The concrete process fails the pair and fourth laws, and the larger family fails the pair law. | No S1 pass; attempt 2/4 is unsuccessful for the exact target. | Open target obligation; valid partial results retained. |
| P3-V02-02 | Section 5, (26)–(27), lines 606–612 | The new obstruction uses radial productivity, one specified Gaussian geometry and mark weight, Poisson parents, and one sterile generation. | It cannot exclude general marked branching, all Hawkes-type routes, or general stationary S1 processes. | Correctly scoped and closed; preserve every qualifier. No target change follows. |
| P3-V02-03 | Sections 1–2, (5)–(12) | Whole-space local finiteness, simplicity and exact prescribed intensity require integration over all parents despite Gaussian tails. | A bounded-parent-neighbourhood argument would be invalid here. | Checked and closed by finite expectation, countability, diffuse displacements and the exact mark integrals. |
| P3-V02-04 | (14)–(18) | Both same-family genealogies and all fifteen fourth-order immigrant partitions are essential. | Omitting any root or lower-block term would change the full law. | Checked and closed; all coefficients, mark powers and allocation counts are correct. |
| P3-V02-05 | Section 3, (19) and (2) | The determinant normalisation and Gaussian factors must match \(V=|\det E|/6\). | An error would alter both the construction and its limiting coefficient. | Checked and closed: \(\det S_4=9V^2\), coefficient \(c/(24\pi^3L^6)\). |
| P3-V02-06 | Section 3, lines 298–332 | Infinite fourth local mass must be distinguished from density infinite on positive measure or singular mass. | The former is allowed and required in S1; the latter would fail its regularity conditions. | Checked and closed for the concrete law: full densities finite a.e. globally, no singular component, finite third and infinite fourth local moments. |
| P3-V02-07 | Section 4, (21)–(24) | A same-family singular term alone would not determine the full limiting coefficient. | Additional contributions could invalidate the proposed contradiction unless controlled. | Checked and closed: every remainder is uniformly bounded near ordinary coplanarity; the full coefficient varies with configuration, excluding the exact fourth law. |
| P3-V02-08 | Section 5, (28)–(33) | The radial dichotomy must allow arbitrary measurable \(b\), both infinite and finite integrals, and a.e. target equality. | A formal small-distance expansion or pointwise-only contradiction would be insufficient. | Checked and closed using uniform angular bounds, an integrable dominating weight and radial null-set reduction. |
| P3-V02-09 | Source attribution and prior responses | Seed excerpts are leads and scope evidence; their old approval labels are not proof dependencies. | Full-seed correctness and any historical claim cannot be certified from these excerpts. | Attribution and relevant local statements checked; complete seed theorems intentionally not reviewed or used. |
| P3-V02-10 | Concrete third-order formulas (15)–(17) | The submission does not claim exact triangle attainment, and none should be inferred from its moment class. | No hidden order-three success accompanies the reciprocal-volume singularity. | Reviewer reconstruction above also excludes its triangle law by boundedness near a nontrivial collinear triple. |

There is no unresolved correctness gap in the submitted partial theorems. The unresolved mathematical obligation is the general exact S1 construction or a genuinely broader obstruction, not a missing routine computation in this model.

## Amendment implications

The active S1 version and its recorded adoption authority remain unchanged. The supplied nonexistence_2 proof also independently confirms S0's failure from the global pair law: the second factorial moment in a radius-\(R\) ball grows as \(R^5\), whereas the square of its positive mean grows as \(R^6\), contradicting nonnegative variance for large \(R\). This does not settle S1, whose large-distance densities are free.

The local inverse-volume integral excludes S1's separate finite-fourth-moment comparison subclass. It imposes no lower altitude cutoff and no finite-moment restriction on S1's broader class.

Neither new model-specific obstruction proves that S1 requires a new geometric domain, a changed intensity quantifier, fewer orders, a cumulant interpretation or approximation. No such change is authorised. The optional construction-driven owner checkpoint occurs after three unsuccessful reviewed submissions; this is only the second, and there is no pending owner amendment in the submitted text.

## Source and coding evidence

The mathematics was checked from the frozen proof and authorised excerpts, using elementary Poisson factorial identities, Gaussian and beta integrals, linear algebra, Tonelli, monotone convergence and dominated convergence. No specialised external theorem is needed. No website, external PDF, simulation, numerical fit, symbolic package or proof assistant was used to establish a conclusion.

The additional seed Section 5 was supplied through the coordinator and hash-verified. Its relevant Gaussian lead is independently sound: the matrix with rows \((x_i,-1)\) has absolute determinant \(6V\), so the four-variable Gaussian integral gives the stated inverse-volume fourth cumulant. Its mean integral and first-three-local-moment tail bound also check. The excerpt explicitly distinguishes its cumulant from a full density. Its construction is not substituted for the present branching law.

The three earlier scope excerpts explicitly impose, respectively, a positive tetrahedral altitude cutoff, a selected flattening condition, or a relative-shape condition, with sufficiently small prescribed intensity. The separate cluster-law excerpt explicitly bounds family size by four. These facts justify the scope comparison and finite-moment consequence only. The full old constructions are neither necessary dependencies nor certified results of this review.

The supplied nonexistence_2 shrinking-cluster example was also checked as a logical boundary example: finite third size moment, divergent fourth factorial size moment, bounded cluster radius, and diameter-dependent truncation of the density sum on each distinct tuple establish its stated process properties. Its count-dependent spatial law lies outside v01 and does not satisfy the reciprocal target.

Executed tools verified hashes, read authorised text, and extracted own-session metadata/token fields. They did not provide mathematical numerical evidence. There is no outstanding mathematical source or coding request.

## Presentation judgement

The submission is readable and unusually clear about its limitations. It separates the actual process, full measure identities, singular contribution, full limiting coefficient and class-specific obstruction. The distinction between conditional independence and unconditional count–geometry coupling is explicit. Formula (18) makes the full-density interpretation easy to inspect.

Two small exposition improvements would help without changing the proof. First, refer to the coefficient in (23) as depending on the configuration, including its scale and shape: the square argument varies scale. Second, label the general radial-family theorem separately from the concrete model's stronger third-moment and finite-a.e. density assertions, to prevent a reader from transferring those assertions to every \(b\) satisfying (27). The current wording already keeps the claims logically distinct.

The long administrative provenance could be moved to an appendix in a future manuscript. It is useful in the present experimental record. No mathematical revision is required for acceptance of the stated partial results.

## Review summary and repairs

The marked construction successfully couples large families with thin spatial profiles while preserving an actual locally finite process, exact intensity, and globally diffuse finite-a.e. factorial densities. Its Gaussian cancellation produces the stated damped reciprocal-volume contribution with the correct constant. The full expansion proves that this contribution creates infinite fourth local moments.

The same full calculation proves the failure of exactness: the remaining fourth-order terms stay bounded near ordinary coplanarity, leaving a configuration-dependent leading coefficient. The broader radial-productivity family is independently excluded by its actual full pair density. Both are complete, useful negative results within their advertised scopes.

No repair of an invalid step is required. To pass S1, a later substantive submission must provide a different fully specified law with all three exact full densities for every independently prescribed \((\lambda_0,M)\), or establish an appropriately broader obstruction with explicit scope. Repeating the singular contribution, deleting its damping, discarding positive partition terms, or relabelling a limit as equality would not meet that obligation.

The review remains tied to the current frozen proof and S1 hashes. Its own hash, word count and exposed accounting checkpoint are stored separately to avoid a self-referential digest.
