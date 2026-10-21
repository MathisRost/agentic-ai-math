# Review — proof_1 submission v04 against S1

- Type: fresh independent extensive review of the final construction submission and its supplied consequential dependencies; not a cross-track synthesis.
- Reviewer: `/root/review_proof_1_v04`, thread `session-23`, turn `turn-35`.
- Requested and directly verified runtime: `gpt-6-astra`, `xhigh`. The reviewer's own `turn_context` at rollout line 8, timestamp `2026-10-20T18:55:47.314Z`, supplies both values. Session metadata at line 1 identifies this reviewer and the parent relationship.
- Review start: `2026-10-20T18:55:44.733Z`. The report freeze timestamp and hash are recorded in `review_freeze.json`; the completed-turn end time is NR at freeze.
- Setup root: `$SETUP`.
- Run root: `runs/20261020T164437Z_astra6/` under that setup root. Paths below are relative to the run root unless stated otherwise.
- Packet: `packets/review_proof_1_v04.json`, SHA-256 `10c68914eedd00f44cf025b86ba9efb49a2b7af6bbf6c9d08065bdd00f83519d`.
- Active target: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Reviewed submission: `reviews/proof_1_v04/proof_snapshot.md`, SHA-256 `e4df045aeec78209ceaf15e5fb8fe4011da15d1555b97ee3946efb15de58ce31`.
- All packet-listed input hashes were verified before mathematics. Their paths, expected hashes and measured hashes are in `input_hash_verification.json`.
- Received context: frozen instructions, workflow, target and adopted amendment, the complete v04 proof, this track's frozen v01–v03 submissions, concrete prior issue tables, the specifically supplied seed excerpt and its provenance, and the frozen proof-reviser skill with its complete required references.
- Excluded context: author conversations and private work, other construction tracks and reviews, complete prior review reports, coordinator deliberations, unassigned seed material, other chats and old runs. No delegation occurred.

## Correctness verdict and scope

**The submission does not establish exact S1. It establishes valid new partial construction results, including an exact fourth same-parent law, and correctly proves that its displayed full processes fail required parts of S1.**

The three principal results survive this audit:

1. The spherical mark law realises the full fourth **same-parent measure** with density \(a/V\) on all affinely independent quadruples, for any finite \(a>0\). Its first three population moment rates are finite, and its lower spatial densities can be made uniformly small relative to \(D^{-1}\) and \(A^{-1}\). After adding singletons it has any prescribed positive intensity. The full factorial measures through order four are globally absolutely continuous and have finite-almost-everywhere densities. Counts have finite third moments on bounded sets and infinite fourth moments on nonempty open balls.
2. Under the stated smallness conditions on \(\lambda M^3\), finite correction streams give the two exact full lower laws and the exact full fourth density \(a/V+B_4\), where all 14 remaining parent partitions are retained. This fourth density is not any constant multiple of \(1/V\) throughout the prescribed domain.
3. For every independently prescribed \(\lambda,M,\eta>0\), the cap/sphere/correction construction gives an exact full pair law and
   \[
   \frac aV\leq \rho^{(4)}\leq(1+\eta)\frac aV
   \quad\text{a.e. on }E_4(M),
   \]
   with the required global density regularity and finite-third/infinite-fourth local moment behaviour. Its full third density fails the reciprocal-area law near distinct collinear triples. The argument proving this failure handles the almost-everywhere qualification correctly.

I found no invalid step in these stated partial theorems after reconstructing the coarea calculations, parameter choices and measure arguments. This is an informal mathematical correctness assessment, not a proof-assistant certification. The exact-target obligations remain open; their absence is not concealed by the author's claims.

Submission v04 consumes the fourth and final substantive allowance for this approach. Its exact-S1 outcome is **unsuccessful with valid partial progress**. That outcome does not prove non-existence for general stationary processes or for the entire Poisson-cluster class, and it does not authorise a fifth submission or an attempt reset.

## Reconstruction and detailed audit

### 1. Target, quantifiers and the measure convention

S1 requires one whole-space stationary simple locally finite process for **each independent pair** \((\lambda,M)\) of positive numbers. All three full densities must have the specified reciprocal forms on every nondegenerate shape of diameter below \(M\), almost everywhere. Their coefficients are finite positive constants, independent of the configuration. Globally, including outside these domains, the full measures must have densities finite almost everywhere and no singular component. Fourth local integrals may be infinite.

The current submission uses this target without a lower geometric cutoff or a hidden finite-fourth-moment hypothesis. Its statements distinguish the small-intensity result from the all-intensity result and distinguish a same-parent measure from a full factorial measure.

The relevant unavoidable moment comparison can be checked directly. On a ball of diameter below \(M\), the kernels \(D^{-1}\) and \(A^{-1}\) are integrable: the pair integral is controlled by \(2\pi M^2\), and the third-point marginal of \(A^{-1}\) is bounded by \(2\pi^2M^2/D\). Hence an S1 solution would have finite third count moments there. Covering any bounded set by finitely many such balls extends this conclusion to every bounded set. In contrast, near a small planar square with separated vertices and nonzero face areas,
   \[
   V=A_{\mathrm{base}}|h|/3,
   \]
and integration in the fourth vertex's signed height gives \(\int dh/|h|=\infty\). Thus every nonempty open ball has infinite fourth count moment. This explains why the new moment class is appropriate but cannot alone constitute an S1 solution.

### 2. Actual cluster law, existence and all parent partitions

The underlying parent space has intensity \(dz\,\nu(dC)\), where each mark is a finite configuration. Finite total point-intensity rate
   \[
   \int |C|\,\nu(dC)<\infty
   \]
gives
   \[
   \int dz\int C(B-z)\,\nu(dC)
   =|B|\int |C|\,\nu(dC).
   \]
Consequently the number of parents contributing to a bounded \(B\) has finite rate, the expected count is finite, and \(X(B)<\infty\) almost surely. A countable exhaustion makes local finiteness simultaneous. This argument remains valid for unbounded sphere radii; a deterministic bounded range of influence is unnecessary.

The marks are simple because their surface measures are diffuse. Distinct parents cannot generate coincident observed points: for each selected pair of offspring, equality imposes a Lebesgue-null condition on the independent parent translations. Nonnegative integration and countable exhaustion justify this even with unbounded populations. Translation invariance gives stationarity. The new sphere and cap choices also give isotropy, although S1 does not require it.

The inherited v02 parent-level definition correctly avoids products of arbitrary non-\(\sigma\)-finite image measures. Its underlying parent measures are \(\sigma\)-finite, and each observed tuple has exactly one partition by parent. Once the same-parent densities \(k_r\) are established to be finite almost everywhere, the ordinary density products apply. At order four the terms are
   \[
   \lambda^4,\qquad
   \lambda^2\sum_{\text{6 edges}}k_2,\qquad
   \sum_{\text{3 pairings}}k_2k_2,\qquad
   \lambda\sum_{\text{4 faces}}k_3,\qquad k_4.
   \]
These account for all 15 partitions, with no extra factorial. At order three there are the singleton term, three edge-plus-singleton terms, and one triple term.

The finite-correction normalisation is also correct. A size-\(r\) stream with anchored rate density \(F_r(0,\mathbf y)/r!\) has \(r!/(r-s)!\) ordered \(s\)-point selections. Symmetry and the Jacobian-one change of translation anchor make their integrated densities equal. Thus its order-\(s\) density is \(\mathcal M^{r-s}F_r/(r-s)!\), and its point intensity is \(Z_r/(r-1)!\). This includes selections omitting the original anchor.

Empty cap marks, which can arise in the conditional Poisson sampling, cause no difficulty: they may be retained on the marked parent space or discarded. They contribute neither points nor factorial measures.

### 3. Spherical coarea identities and absence of singular mass

The delta notation in v04 (4)–(7) is shorthand for surface/coarea integration. Its content can be verified on nonnegative test functions; it is not a multiplication of unrelated distributions.

For two points at separation \(D\), the two-distance coordinates of the sphere centre have volume element
   \[
   \frac{2\pi r_1r_2}{D}\,dr_1\,dr_2
   \]
after integration in the azimuth. At \(r_1=r_2=R\), division by the two surface normalisations gives \(1/(8\pi R^2D)\) when \(D<2R\). For \(D>2R\) there is no overlap.

For a noncollinear triangle with area \(A\) and circumradius \(r\), the centres at fixed \(R>r\) lie a distance \(h=\sqrt{R^2-r^2}\) on either side of the planar circumcentre. The determinant of the three distance gradients has magnitude \(2Ah/R^3\). There are two centres. Their combined inverse Jacobian, divided by \((4\pi R^2)^3\), is
   \[
   \frac{1}{64\pi^3 R^3 A\sqrt{R^2-r^2}}.
   \]
The square-root singularity at \(R=r\) is integrable against the radius laws used here.

For an affinely independent quadruple, the circumcentre and positive circumradius are unique. In the variables \((z,R)\), the gradients of \(|x_i-z|-R\) form a \(4\times4\) matrix. Subtracting the first row from the remaining rows reduces its determinant to the tetrahedral determinant, with magnitude \(6V/R^3\). Therefore the weight \(m(R)\) produces
   \[
   \frac{m(R_*)}{(4\pi R_*^2)^4}\,
   \frac{R_*^3}{6V}
   =\frac{m(R_*)}{1536\pi^4 R_*^5V}.
   \]
The factor \(1536=6\cdot4^4\) is correct. Integrating in the continuous radius variable is essential: a fixed-radius four-point measure would generally be supported on a lower-dimensional set.

There is no unaccounted mass on the removed degeneracies. Conditional on a sphere, repeated sampled points have probability zero. Three distinct points on a sphere cannot lie on a line. Given three distinct points, their plane intersects the sphere in a surface-null circle, so a fourth independently sampled surface point lies in that plane with probability zero. The same reasoning holds for conditional cap sampling, whose intensity is absolutely continuous with respect to sphere surface measure. Each conditional factorial weight is finite; nonnegative integration of these zero masses remains zero, even when the mixed fourth population moment rate is infinite.

On the complementary nondegenerate sets the coarea calculations give genuine Lebesgue densities. Together with the null-set calculation, they give the **full** same-parent measure identities, rather than only densities of an absolutely continuous part.

### 4. The spherical population law and Theorem 1

Let \(g(R)=R/\ell+\ell/R\), \(N=4+\lceil Tg(R)^8\rceil\), and \(c=1536\pi^4a\). These define measurable finite populations for every \(R>0\). Cancelling falling factorials gives
   \[
   \frac{(N)_r}{(N)_4}
   \leq T^{-(4-r)}g(R)^{-8(4-r)}
   \quad (0\leq r\leq3),
   \]
because every remaining factor is at least \(N-3\geq Tg(R)^8\).

For \(p=4-r\geq1\), the population-rate integral is bounded by a constant times
   \[
   \ell^6\int_0^\infty u^5(u+u^{-1})^{-8p}\,du.
   \]
Its integrand is at most \(u^{5+8p}\) near zero and \(u^{5-8p}\) near infinity. All required parent and first-three factorial population rates are finite, including the least-decaying case \(p=1\).

The explicit bounds in (11), (14) and (15) also check:

- For the first moment, the split at \(R=\ell\) gives \(1/30+1/18=4/45\), hence \(U_T=4c\ell^6/(45T^3)\).
- For the pair bound, the relevant split gives \(1/20+1/12=2/15\), hence \(S_T=c\ell^4/(60\pi T^2)\).
- For the triangle bound, substituting \(R=\sqrt{r^2+t^2}\) transforms the radius integral to \(\int_0^\infty Rg(R)^{-8}\,dt\). On \(0<t<\ell\) the integrand is at most \(\ell\), regardless of \(r\). On \(t\geq\ell\) it is at most \(\ell^8t^{-7}\). The resulting \(7\ell^2/6\) yields \(H_T=7c\ell^2/(384\pi^3T)\).

At fourth order the population factors cancel **exactly**, leaving \(m(R)=cR^5\) in the four-sphere formula. Thus \(p_4=a/V\), with no approximation and no limiting mark. This identity holds globally off degeneracy as a density version.

Finite raw third population rate follows from \(N^3=(N)_3+3(N)_2+N\). The inequality
   \[
   C(B-z)^3\leq N(C)^2C(B-z)
   \]
and integration over \(z\) yield the displayed bound by \(|B|\int N^3\,d\nu\). The compound Poisson sum in a bounded window therefore has finite third moment. The reciprocal-height calculation proves infinite fourth moment in every nonempty open ball.

The bounds for \(p_2,p_3,p_4\), and the partition formula, establish global finite-almost-everywhere densities through order four. Values on the degeneracy sets can be set to zero without changing any measure. This verifies the outside-domain requirement as well.

Finally, \(T\) can be chosen to make the spherical intensity at most any prescribed \(\lambda>0\), and nonnegative singleton intensity supplies the difference. Increasing \(T\) further drives the lower spherical contributions to zero without changing \(p_4\). Theorem 1 is therefore valid with its advertised same-parent scope. A total full fourth density is still obtained only after adding the other partitions.

### 5. Low-intensity lower-law corrections and Theorem 2

The required inherited inequalities were re-established, rather than accepted from an earlier review. For \(K_2=\mathbf1_{E_2(M)}/D\),
   \[
   \int K_2(0,y)\,dy=2\pi M^2=I.
   \]
For a base edge of length \(d\), cylindrical coordinates and \(A=dr/2\) give
   \[
   \int K_3(x_1,x_2,z)\,dz
   \leq \frac2d\int_{B(x_1,M)}
                  \frac{dz}{\operatorname{dist}(z,\operatorname{aff}(x_1,x_2))}
   =\frac{2\pi^2M^2}{d}.
   \]
The triangle support implies that this marginal vanishes outside the base pair domain. Thus \(\mathcal MK_3\leq JK_2\), \(J=2\pi^2M^2\).

With \(a_2=\lambda/I\), \(a_3=a_2/(4J)\), the pair relative subtraction is at most \(2\pi\lambda M^3\). Using \(A\leq M^2/2\) and \(A/D\leq M/2\), the triple relative subtraction is at most
   \[
   8\pi^3(\lambda M^3)^2+12\pi^2\lambda M^3.
   \]
Under (16), these prove precisely the two half-kernel lower bounds in (19). The conditions are sufficient conditions for this correction scheme, not necessary conditions for S1.

Every factor in the explicit choice (20) is correct. It ensures \(S_T\leq a_2/8\), \(H_T\leq a_3/4\), and \(m_1\leq\lambda^2W/2\). Consequently
   \[
   F_3\geq \frac{a_3}{4}K_3,\qquad
   F_2\geq
   \left(\frac{a_2}{2}-\frac{a_2}{8}-a_3J\right)K_2
   =\frac{a_2}{8}K_2.
   \]
Both correction kernels have finite anchored integrals. Their support restriction is important: the spherical densities outside the prescribed domains are retained, not subtracted by negative correction kernels.

Writing \(R_3=Q_3-P_3\), the finite-stream point intensity is \(Q_2-P_2-R_3/2\), where \(Q_2=\lambda-\lambda^2W\). Adding the spherical stream and (22) gives total intensity exactly \(\lambda\). The singleton rate is at least \(\lambda^2W/2\), since \(P_2,R_3\geq0\) and \(m_1\leq\lambda^2W/2\).

On the lower domains the total same-parent densities are exactly \(q_2,q_3\); at order four only the spherical stream contributes a single-block term. Every edge and face of a nondegenerate tetrahedron of diameter below \(M\) lies in its appropriate lower domain. Therefore the full fourth density is exactly \(a/V+B_4\) with (23), and all the other claimed process and moment properties are preserved.

The proof that this is not an exact fourth law is valid. On \(E_4(M)\), the canonical \(B_4\) is continuous, since its ingredients there are the displayed reciprocal kernels and constants. The difference from a proposed \(a_4/V\) is continuous. An almost-everywhere equality would therefore hold everywhere on that open set. Along a lifted planar square, all edges and face areas remain positive, so \(VB_4\to0\). The identity would force \(a_4=a\), whereas \(B_4\geq\lambda^4>0\) on the whole domain. This contradiction is not merely a comparison on an exceptional curve.

### 6. Random spherical caps and the all-intensity pair law

The cap mark is an actual conditional Poisson process on a finite surface measure. With \(R\in[M,2M]\), \(\kappa(R)=KR^2\) is bounded for every fixed positive choice of parameters. All population moments are therefore finite. The parent rate is finite and positive.

For points on a common sphere, conditioning first on the direction \(v\) gives a threshold probability
   \[
   \frac{R-\max_i v\cdot(x_i-z)}{2R}.
   \]
Averaging removes the centre \(z\), since the mean direction is zero. This proves (27). The average maximum is nonnegative, so \(P_m\leq1/2\); nonnegativity follows from the original probability representation. For two points,
   \[
   \mathbb E\max(v\cdot x_1,v\cdot x_2)=D/4,
   \]
because \(\mathbb E|v\cdot(x_2-x_1)|=D/2\). Thus \(P_2=1/2-D/(8R)\).

For \(D<M\), every sampled radius exceeds \(D/2\), so there is no radius-dependent overlap truncation in the pair integral. The prescribed \(K,\gamma\) satisfy
   \[
   \frac{\gamma K\mu_2}{2}=w,\qquad
   \gamma K^2=\frac{64\pi\lambda^2}{\mu_1}.
   \]
Combining these identities with the pair coarea formula yields
   \[
   u_2(D)=\frac{4\lambda^2\mu_2/\mu_1}{D}-\lambda^2
          =\frac{(56/9)\lambda^2M}{D}-\lambda^2.
   \]
The negative constant is part of this actual nonnegative same-parent kernel; it is not a signed mark rate. Adding the full singleton partition \(\lambda^2\) gives the claimed exact pair law. The intensity parameter \(w\) may be arbitrarily small while \(K\) and \(\gamma\) remain finite for each fixed choice.

The cap probabilities are centre independent after averaging, so they may be inserted into the same triple and quadruple coarea formulas. This justifies (30) and (31), including their factors of \(h(R)\), \(\kappa(R)^m\) and \(\gamma\). The continuous radius distribution removes the potential fixed-radius singularity at order four.

For (32), the triple integral obeys
   \[
   \int_{\max(M,r)}^{2M}
       \frac{R^3\,dR}{\sqrt{R^2-r^2}}\leq8M^3.
   \]
Indeed, after \(t=\sqrt{R^2-r^2}\) it is \(\int R^2dt\), with \(R^2\leq4M^2\) and interval length at most \(2M\). Including \(h=1/M\) and \(P_3\leq1/2\) gives \(G_3=\gamma K^3M^2/(16\pi^3)\). At fourth order, \(P_4\leq1/2\), \(R_*^3\leq8M^3\) and \(h=1/M\) give \(G_4=\gamma K^4M^2/(384\pi^4)\). Both constants are correct.

The null-set argument in Section 3 applies to this conditional Poisson sampling as well. Hence these are full global densities, not merely their restrictions to the small-diameter domains. Finite population moments give finite local moments of every order for the cap stream.

### 7. All-intensity combination, fourth comparison and triangle failure

With \(w=\lambda/4\), \(S_*=\lambda/(8I)\) and \(H_*=\lambda/M^4\), all constants in (33)–(34) are finite and positive for every \(\lambda,M>0\). They are fixed before choosing the spherical amplitude \(a=C_0/\eta\), so there is no circular parameter dependence.

The given sufficient choice of \(T\) makes \(S_T\leq S_*\), \(H_T\leq H_*\), \(m_1\leq U_T\leq\lambda/8\). The pair correction
   \[
   F_2=\mathbf1_{E_2(M)}(S_T/D-p_2)
   \]
is nonnegative and has point intensity \(Q\leq S_TI\leq\lambda/8\). Thus all nonsingleton streams together cost at most \(\lambda/2\), leaving a nonnegative singleton rate. The total intensity is exactly the independently prescribed \(\lambda\).

The same-parent pair density on the target domain is
   \[
   q_2^*=(A_{\mathrm{cap}}+S_T)/D-\lambda^2.
   \]
The full pair law follows exactly. The higher same-parent densities are \(k_3=p_3+u_3\) and \(k_4=a/V+u_4\); the pair correction has no higher contributions.

Every geometric estimate in (39) is valid over the whole tetrahedron domain. For example,
   \[
   6V=\left|\det(x_j-x_i,x_k-x_i,x_l-x_k)\right|
       \leq D_{ij}\,M\,D_{kl}
   \]
for opposite edges \(ij,kl\), proving the pairing bound. Multiplying the complete partition expansion by \(V\) gives the five error bounds
   \[
   G_4,\quad \lambda^4M^3/6,\quad
   \lambda^2\overline A M^2,\quad
   \overline A^2M/2,\quad
   4\lambda\overline H M/3.
   \]
Their sum is exactly \(C_0\). All error terms are nonnegative. Hence (40), and therefore the stated relative comparison, hold uniformly over all nondegenerate shapes in \(E_4(M)\), without a lower distance, area or altitude threshold.

The failure of the triangle law is also proved, rather than merely left unverified. Near a fixed triple of distinct collinear points with diameter below \(M\), its three side lengths stay bounded below and
   \[
   r=\frac{abc}{4A}\longrightarrow\infty.
   \]
The cap contribution vanishes once \(r>2M\). For the spherical contribution, \(g(R)\geq R/M\) gives
   \[
   A p_3\leq\frac{cM^8}{64\pi^3T}
             \int_r^\infty
                \frac{R^{-6}\,dR}{\sqrt{R^2-r^2}}
           =\frac{cM^8}{120\pi^3T\,r^6}.
   \]
The substitution \(R=r\cosh u\) reduces the integral to
   \(r^{-6}\int_0^\infty\operatorname{sech}^6u\,du
     =(8/15)r^{-6}\), which verifies the coefficient.
The singleton and edge terms in \(\rho^{(3)}\) are bounded near that triple, so multiplying them by \(A\) gives zero in the limit. Thus \(A\rho^{(3)}\to0\).

The bounds hold uniformly in sufficiently small neighbourhoods with separated edges. Every such neighbourhood contains a positive-measure nondegenerate set. A full-measure equality set for a proposed positive constant \(a_3\) would have a sequence approaching the collinear triple; along that sequence \(A\rho^{(3)}=a_3\), contradicting the uniform bound. No continuity of the population-floor function, or evaluation of an a.e. identity on a preselected exceptional curve, is needed.

Finally, taking \(\eta\downarrow0\) does not give an exact construction: the displayed coefficient \(a=C_0/\eta\) diverges, the law changes, and no fourth-measure limit is supplied. The triangle defect persists independently. The submission correctly makes no limiting-existence claim.

### 8. Supplied earlier dependencies and scoped negative results

The current positive theorems depend on the v01 triangle marginal and finite-correction estimates, the v02 parent-level partition convention, and the elementary lifted-square argument from v03. These have been checked directly above.

I also checked the mathematical mechanisms behind the prior issue dispositions against the supplied proofs:

- In v01, bounded population gives finite local exponential moments, and finite fourth population moment gives finite fourth local moments. Population independent of a fixed, or randomly selected, displacement density with infinite fourth factorial moment produces a nonzero measure multiplied by infinity, which is not \(\sigma\)-finite. These arguments are properly restricted to the stated representation assumptions. The separated-square divergence also proves the required infinite fourth population weight at every fixed diameter threshold in the stated range. None excludes the population-dependent spherical construction.
- In v02, the cylinder height integral is \(1/(12w^3)\). The polar of the standard tetrahedron's difference body has volume \(4\), so normalised spherical integration gives \(\int w^{-3}\,d\sigma=1/(2\pi V)\). The finite disc-intersection factor remains present. The inherited lower-density and correction estimates are consistent with the current use of the same finite correction mechanism.
- In v03, the lifted-square residue of \(Vk_4\) required by exact S1 is \(a_4\), while a single collapsing face with fixed opposite altitude \(t\) requires \(a_4-\lambda a_3t/3\). The continuous canonical densities justify the path arguments. A finite-radius positive mixture has a strict intersection loss at each fixed square size; the proof first derives finite total amplitude before using dominated convergence. The expanding-radius family instead has a common residue, using the displayed probability measure and tail bound \(\pi V/\delta^3\), so it fails the two-residue test. Both remain scoped obstructions.
- The v03 fixed-amplitude sequence has an explicit common-rate coupling of the finite corrections, while the cylinder component affects a bounded window with probability at most its expected count. Thus local total-variation convergence is compatible with the positive fourth-expectation discrepancy on tests compactly supported inside \(E_4(M)\). This proves failure of uniform integrability for that sequence, not a universal obstruction to process limits.

These earlier arguments are not used as authority for a desired verdict, and no other track has been compared. The current spherical construction bypasses the cylinder representation assumptions; its exact same-parent residue still leaves the full lower-partition defect.

## Finding register

| ID | Location | Precise mathematical issue or verified finding | Consequence | Repair/status |
|---|---|---|---|---|
| **P1V04-01** | Exact target/result; Sections 4, 6–7 and (44) | No displayed process has all three required full identities for every independently prescribed \((\lambda,M)\). The low-intensity process has a positive fourth partition defect, and the all-intensity process fails the triangle law. | No exact S1 pass; fourth and final substantive attempt is unsuccessful. | **Open exact-target obligation.** No fifth submission or counter reset is authorised. Exhaustion is not non-existence. |
| **P1V04-02** | Section 2, (5)–(7); Section 3, (8)–(15) | Radius mixing and the four-sphere determinant give an actual fourth same-parent density \(a/V\); population-dependent weights control lower rates. Constants, measurability and parameter integrability check out. | New valid partial construction, with any positive prescribed intensity after singleton addition. | **Verified.** Keep “same-parent” explicit wherever this result is quoted. |
| **P1V04-03** | Section 4, (16)–(23), Theorem 2 | Lower corrections are nonnegative and correctly normalised only in the stated sufficient parameter range. Their full fourth density is exactly \(a/V+B_4\). | Two exact full laws in that range; no exact fourth law for any coefficient. | **Verified partial theorem and failure proof.** The remaining subtraction of \(B_4\) is a joint-law problem, not an omitted algebraic term. |
| **P1V04-04** | Section 5, (24)–(32) | The cap probability has the exact affine pair-distance factor, and the chosen rate/count parameters give intensity \(w\) and constant term \(-\lambda^2\). | Exact full pair law is available for every prescribed intensity and diameter within this broad cluster class. | **Verified.** This closes the all-intensity gap only for the pair law. |
| **P1V04-05** | Section 6, (33)–(40), Theorem 3 | All parameter choices are finite; the stream-intensity budget is nonnegative; all 15 partitions obey the displayed uniform bound. | Valid all-intensity pair-law and fourth-comparison theorem on the full shape domains. | **Verified partial theorem.** Relative comparison is not exact fourth equality. |
| **P1V04-06** | Section 7, (41)–(43) | Near separated collinearity, \(u_3=0\), \(Ap_3=O(r^{-6})\), and the lower partition terms vanish after multiplication by \(A\). Uniform bounds justify an equality sequence from an a.e. identity. | The all-intensity displayed process cannot satisfy any positive reciprocal-area coefficient. | **Verified scoped failure.** It is a failure of this process, not all cluster processes. |
| **P1V04-07** | Sections 2–6; inherited v02 Section 1 | Coarea densities are supplemented by conditional null-set arguments; parent products are used only after density/\(\sigma\)-finiteness is established. | Global full absolute continuity and finite-almost-everywhere densities, including outside prescribed domains, are justified. | **Closed regularity concern.** No omitted singular component was found through order four. |
| **P1V04-08** | Sections 3 and 6; end of Section 7 | Finite third population rates give finite third local moments; \(a/V\) gives infinite fourth local moments. No limit is used to create the law, and the \(\eta\)-limit has divergent amplitude. | Moment-class progress is valid; it provides no automatic passage from approximation to S1. | **Verified, with stated limitation.** No finite-fourth-moment assumption or unjustified moment limit is introduced. |
| **P1V04-09** | Response to v03 review; supplied prior dependencies | Previous cylinder and limiting arguments are representation- or sequence-specific. The new spherical law does not contradict them. | Prior scoped results remain compatible with the new partial theorems. | **Verified within scope.** They cannot justify a general target amendment. |
| **P1V04-10** | Sources and accounting handoff | Mathematical claims needed here are supplied and rederivable; historical verdicts and author-runtime statements are not mathematical premises. Own telemetry was verified separately. | No missing specialised source blocks the current partial results. | **No active source gap.** Final completed-turn usage and actual charges remain NR at freeze. |
| **P1V04-11** | Section 2 and theorem statements | The shorthand \(s_R(x_i-z)\) is readable only with its explicit coarea interpretation; “full same-parent measure” can be mistaken for the full factorial measure when excerpted. | Exposition risk, not a mathematical defect in the complete submission. | **Presentation suggestion.** Retain a nonnegative-test formulation near (7), and label later quotations “fourth same-parent factorial measure”. |

### Disposition of every supplied prior issue

| Prior ID | Current disposition and independently checked basis |
|---|---|
| **P1V01-01** | **Partly resolved, exact-target portion open.** Current processes have the correct finite-third/infinite-fourth behaviour. The two-law construction still uses (16); the all-intensity construction does not have the triangle law. P1V04-01, 03, 05, 06 and 08. |
| **P1V01-02** | **Actual-law gap closed for the partial theorems; exact joint residual remains open.** Explicit sphere/cap mark laws and correction streams now exist, but no single mark law realises all of (44). P1V04-02–06. |
| **P1V01-03** | **Closed.** The v02 parent-level definition is retained, and ordinary density products are used only after proving the relevant \(\sigma\)-finiteness. P1V04-07. |
| **P1V01-04** | **Scope limitation retained, no active dependency gap.** The supplied source excerpt and own prior proofs suffice for current calculations. No full historical-obstruction or unassigned-seed certification is claimed. P1V04-10. |
| **P1V02-01** | **Partly improved, exact-target portion open.** The spherical law removes the cylinder intersection error in the fourth same-parent kernel. The complete \(B_4\) defect remains, and is proved incompatible with an exact full reciprocal-volume law for Theorem 2's process. P1V04-02–03. |
| **P1V02-02** | **Partly improved, exact-target portion open.** The cap law removes the intensity restriction for the exact pair law. The simultaneous three-law all-intensity problem remains unmet. P1V04-04–06. |
| **P1V02-03** | **No unproved limit passage in v04.** The current relative comparison uses \(a=C_0/\eta\); its divergent amplitude and absent fourth-measure convergence are explicitly acknowledged. The supplied v03 negative limit result remains scoped. P1V04-08–09. |
| **P1V02-04** | **Retained and strengthened partial closure.** The new law is on actual finite marks and gives exact \(p_4=a/V\), rather than the cylinder kernel. It still does not realise the full fourth residual. P1V04-02–03. |
| **P1V02-05** | **Closed.** Parent-level products, all multiplicities and finite-stream factorial factors were rechecked. P1V04-07. |
| **P1V02-06** | **Closed for moment and regularity requirements.** Both relevant combined processes have finite third local moments, infinite fourth moments on nonempty open balls, and global full absolute continuity with finite-a.e. densities through order four. P1V04-07–08. |
| **P1V02-07** | **No active source gap.** Needed prior inequalities and normalisations were read and reconstructed; a prior “accepted” label is not used as a premise. P1V04-10. |
| **P1V03-01** | **Open for exact S1.** Exact spherical \(p_4=a/V\) does not supply \(a_4/V-B_4\) jointly with the two target lower residuals. The current partial constructions are correctly labelled. P1V04-01–03. |
| **P1V03-02** | **Partly improved, exact-target portion open.** All-intensity pair existence and the fourth comparison are now valid. The current third law is demonstrably wrong, so all-intensity S1 existence is still unresolved. P1V04-04–06. |
| **P1V03-03** | **Scoped necessary condition retained.** The two different required boundary residues follow from the complete lower partitions. The current constant same-parent residue cannot resolve that requirement. P1V04-03 and 09. |
| **P1V03-04** | **Scoped obstruction retained.** Finite-radius cylinder mixing remains excluded by its strict planar intersection loss after deriving finite amplitude. The spherical representation lies outside that family. P1V04-09. |
| **P1V03-05** | **Scoped obstruction retained.** The supplied expanding-cylinder law and its common-residue argument remain valid for that family and size-at-most-three additions. They do not rule out the present sphere law as a partial construction. P1V04-09. |
| **P1V03-06** | **Verified negative result for the supplied sequence; no new limit claim.** Local total-variation convergence does not pass its fourth expectations to the limit. Current constructions use finite parameters directly. P1V04-08–09. |
| **P1V03-07** | **Retained and rechecked.** All current correction factors, positivity estimates, intensity balances, global density properties and parent partitions were verified; none closes the exact-target gap. P1V04-03, 05, 07 and 08. |
| **P1V03-08** | **No active source gap; accounting remains separate.** Own runtime verification and hashes are recorded without reading author or other-track sessions. Completed-turn usage and charges are not fabricated. P1V04-10. |

## Amendment implications

No amendment is proposed or adopted by this review. S1 remains the target at the specified hash. The supplied adopted S0-to-S1 record establishes which target this dispatch uses; this review does not reopen or independently certify the complete historical obstruction dossiers, which were not assigned.

The current failure proofs concern explicit processes or restricted kernel representations. They do not justify a restriction on intensity, shape, process class or order in the general target. In particular, the new all-intensity pair construction demonstrates why the earlier smallness condition should not be treated as a general pair-law necessity.

The local reciprocal-height divergence does exclude the separately stated finite-fourth-moment subclass. It does not exclude the broad S1 class, whose fourth moments are allowed to be infinite. The spherical construction gives a concrete example of why finite local third moments and infinite local fourth moments can coexist with a.s. local finiteness and globally finite-a.e. factorial densities.

An owner amendment after failed submissions would be a separate authority route. None is present here, and attempt exhaustion supplies no such authority. No reset is permitted.

## Source and coding evidence

The full input hash verification is saved alongside this report. The consequential mathematical sources inspected were:

| Source | SHA-256 | Use and audit status |
|---|---|---|
| Current proof snapshot | `e4df045aeec78209ceaf15e5fb8fe4011da15d1555b97ee3946efb15de58ce31` | Entire submission audited, including all three partial theorems, failure proofs, parameter choices and claimed global measure properties. |
| `prior_dependency_v01.md` | `acf0c4de3dcd7ee1caeeff0da17e9d8d7d8144b5ecb984d0742bb1662fc52473` | Entire supplied proof read; lower marginal bounds, finite corrections, moment arguments and representation-specific obligations checked. |
| `prior_dependency_v02.md` | `67605a81bb7fa19e16d3aad6ca6ae6c86af8b1112d8f27a165d9a1558200c21d` | Entire supplied proof read; parent-level measure definition, partition formula, correction machinery and cylinder calculations checked as described above. |
| `prior_dependency_v03.md` | `33eb2d7a62132ed60f95833f244544f4bb9b9004c9eee76f194de47e5d81e8ec` | Entire supplied proof read; lifted-square argument is a direct current dependency. Scoped boundary, cylinder and limit arguments checked for prior-issue dispositions. |
| Supplied seed excerpt in `reviews/proof_1_v01/` | `f0d755efa2b82343a5ff7f171c0ba69ccdcd92ba67a36106e9c47052197a2ac9` | Lower-order marginal and finite-stream mechanism checked. Its separate shape-restricted fourth-order theorem is not imported as an S1 result or independently certified here. |
| Seed provenance JSON | `84466d1ec8e8106752e5e634f0878d826d11940490a9404ea3ff3586279155a6` | Verifies the assigned excerpt metadata; the unassigned full seed was not opened. |
| Concrete prior issue tables | Hashes in packet and `input_hash_verification.json` | Used to ensure every earlier issue receives a disposition, not as proof authority. Complete earlier reviews were not opened. |

The frozen proof-reviser skill, proof standard and writing-style reference were read completely. The frozen common context and primary-source index were read. No historical book quotation, novelty claim, present-open-status attribution or specialised external theorem is needed for the conclusions of this review. The decisive geometric and probabilistic calculations are supplied and were reconstructed directly. No primary PDF was required or inspected, and no literature request remains outstanding.

Tools were used for input hashing, permitted runtime-metadata extraction and artifact production. No numerical quadrature, simulation, symbolic package, theorem prover or coder result supports the mathematical verdict. No numerical evidence has been promoted to a continuum proof.

Own usage evidence comes only from the explicitly identified reviewer rollout:

`[local path omitted]`.

Only allowlisted `session_meta`, `turn_context` and `event_msg/token_count` fields were extracted. No raw messages or private reasoning were emitted or saved. `runtime_preflight.json` records the pre-mathematics checkpoint; `accounting_capability.json`, `accounting.jsonl` and `review_freeze.json` document the exposed fields and later checkpoint. Cumulative snapshots are not summed. Reasoning tokens are not added again to output. Final completed-turn totals, final end time, parent-inclusive accounting semantics and monetary charges are NR where not exposed.

## Presentation judgement

The submission is readable and unusually explicit about its limited conclusion. Its opening makes clear that no S1 solution is claimed, and its theorem statements distinguish parameter ranges, full laws, same-parent laws and approximations. The response table is consistent with the mathematical body.

Two small changes would make later reuse safer. First, put the four-sphere identity in nonnegative-test form immediately after the coarea calculation, so that the meaning of the surface-delta shorthand remains clear even when the section is quoted alone. Second, consistently use “fourth same-parent factorial measure” for Theorem 1; a shortened phrase such as “exact reciprocal-volume law” would lose a decisive qualification.

The low-intensity theorem and all-intensity theorem should remain separate when summarised. Their strengths cannot be combined to infer a single all-intensity process with both exact lower laws. No substantive mathematical repair is needed for the partial theorems as stated.

## Review summary and remaining obligations

The decisive new mechanism is valid: the radius-mixed sphere constraints have Jacobian \(6V/R^3\), so a fourth factorial radius weight proportional to \(R^5\) produces exactly \(a/V\). Large but finite radius-dependent populations make the lower rates small without changing that identity. Random caps supply a separate exact affine pair factor that cancels the full \(\lambda^2\) baseline at any prescribed intensity.

The full target still requires one actual process to realise all three residuals simultaneously. Within this Poisson-cluster framework that means
   \[
   k_2=a_2/D-\lambda^2,\qquad
   k_3=a_3/A-\lambda a_2\sum D_{ij}^{-1}+2\lambda^3,\qquad
   k_4=a_4/V-B_4
   \]
on the respective entire domains, with a common nonnegative finite-mark law of total point intensity \(\lambda\) and the global measure requirements. Pointwise residual positivity alone is insufficient.

The final submission does not provide that law. It instead proves exact lower laws in a restricted intensity range with an uncancelled fourth defect, and a different all-intensity construction with a provable triangle failure. These are substantive partial achievements. The final exact-S1 verdict is unsuccessful for this approach after four submissions; general S1 remains unresolved by this track.
