# Review — proof_3 submission v03 against S1

- Review type: fresh independent extensive audit of submission 3/4, including the supplied earlier proof dependencies and concrete issue lists.
- Reviewer: `/root/review_proof_3_v03`; session `session-19`; turn `turn-31`.
- Requested and verified runtime: `gpt-6-astra`, `xhigh`. Own rollout `session_meta` line 1 identifies this reviewer; `turn_context` line 8, timestamp `2026-10-20T18:24:25.610Z`, reports the model, effort and current turn. Verification preceded mathematics. The rollout path and allowlisted evidence are in `runtime_preflight.json`.
- Setup root: `$SETUP`.
- Run root: the setup root followed by `/runs/20261020T164437Z_astra6`.
- Active target: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Supplied adoption record: `statements/S0_to_S1.md`, SHA-256 `b2534040520dfc63bf5c22ecc508257308e619a040a7c6c54ce44375742394de`. S1 is the adopted target specified by the coordinator, not a statement inferred from an earlier construction.
- Submission: `reviews/proof_3_v03/proof_snapshot.md`, SHA-256 `c6608c347db222f9cf91f55c8763ff2215462c21c110826a327a3cca6e097c0c`.
- Dispatch packet: `packets/review_proof_3_v03.json`, SHA-256 `1b51b943e5e4ac20c543847a0df43708abf8463a34b34ebb1fe1b9177e1b426e`.
- All 29 allowlisted file hashes matched. The complete verification is in `input_hash_verification.json`. Unless explicitly stated otherwise, line references below refer to the current frozen proof.
- Received context: frozen instructions, workflow, S0/S1 and the adoption record, proof-reviser skill and its two required references, the current proof, the supplied v01/v02 proofs and extracted issue lists, and the specifically assigned source passages. Excluded context was not inspected: author conversations/private work, other construction tracks, prior full review reports, unassigned seed files, old runs and other chats. No delegation occurred.
- Review start is the turn-context timestamp above. Review freeze time, final exposed accounting checkpoint and artifact hashes are recorded separately in `freeze.json` and `accounting_record.json`, avoiding a self-referential report hash.

## Correctness verdict and scope

**No exact S1 pass. The submission establishes valid partial construction results and a valid scoped obstruction.** The concrete process attains the entire full pair law for every independently prescribed intensity and diameter, but fails both the full triangle and full fourth-order laws. Its same-parent reciprocal-volume density is exact; identifying it does not make the full fourth density reciprocal-volume.

The strongest supported positive result is the following. For every $\lambda,L>0$, the submitted law gives one stationary, isotropic, simple, almost surely locally finite process on all of $\mathbb R^3$, with intensity exactly $\lambda$, no singular components in its full factorial measures of orders two through four, and densities finite Lebesgue-almost everywhere globally. It has finite third local count moments and infinite fourth count moments on every nonempty open ball. Its full pair density is
\[
\rho^{(2)}(D)=\frac{3\lambda^2L}{D},\qquad 0<D<2L.
\]
Its same-parent fourth density is
\[
c_4=\frac{8\lambda^4L^3}{3\pi V}
\]
on all noncoplanar quadruples. These statements, including their constants and measure interpretations, are supported by the proof.

The second theorem correctly excludes simultaneous full pair and triangle reciprocal laws for Poisson latent-parent families whose children, conditional on a common radius and finite count, are independent and uniform on the corresponding sphere. It allows arbitrary radius mixing and arbitrary dependence between radius and count. It does not exclude general branching, general Cox processes, dependent offspring directions, non-Poisson parents or arbitrary stationary point processes.

No essential mathematical gap was found in these narrower results. A scope clarification concerning arbitrary radius measures is recommended below; the concrete construction and the stated obstruction do not depend on an erroneous extension of the fourth-order formula.

This is unsuccessful exact-target submission **3/4**, with one substantive submission remaining under the supplied attempt policy. No target change or attempt reset follows.

## Reconstruction and detailed audit

### 1. Exact target and quantifiers

S1 requires, for every independently prescribed $\lambda_0,M>0$, one process of intensity $\lambda_0$ satisfying all three full-density identities on every nondegenerate configuration of diameter less than $M$. It also requires global absolute continuity and finite-almost-everywhere densities, including outside those diameter domains. It allows infinite fourth local moments and imposes no lower shape or distance cutoff.

For the new construction, set $\lambda=\lambda_0$ and $L=M/2$. There is no smallness condition relating the two parameters, so the pair-law achievement respects the original independent quantifiers. The other two laws are not obtained for that choice, or for any other positive $L$ on any positive diameter domain. The constants are configuration-independent where claimed:
\[
a_2=3\lambda_0^2M/2,\qquad
b_4=\frac{8\lambda_0^4(M/2)^3}{3\pi}.
\]
Here $b_4$ is explicitly a same-parent coefficient, not an S1 full-density witness $a_4$.

The change from observed roots in v01/v02 to latent roots in v03 is a new, openly defined process law. S1 does not require roots to be observed or a Hawkes representation. This change is therefore permitted as a construction choice; it does not amend S1. Conversely, calling this a branching or Cox construction does not extend its conclusions to those entire model classes.

### 2. Whole-space probability law and intensity

Equations (3)–(7), lines 38–73, specify nonnegative measurable $q_L$ and finite positive $m_{\lambda,L}$ for every $R>0$. The parent intensity $dz\,q_L(R)dR$ is sigma finite. A convenient actual realisation uses only nonempty families: their parent rate is
\[
\nu=\int_0^\infty q_L(R)(1-e^{-m(R)})\,dR.
\]
The inequality $1-e^{-m}\leq m$ and the explicit first-moment calculation below give $0<\nu\leq\lambda<\infty$. A spatial Poisson process of rate $\nu$, the normalised radius mark law, a positive-conditioned Poisson count, and independent surface-uniform locations therefore define an ordinary countable family construction. This establishes existence without requiring an infinite collection of nonempty parents in a bounded spatial region.

For $n\geq1$, the zero-truncated count law has factorial moment $m(R)^n/(1-e^{-m(R)})$. Multiplying by the thinned parent intensity recovers exactly $q_L(R)m(R)^n$. Thus the untruncated formulas for the tuple measures refer to the same realised process.

The normalisation is correct:
\[
q_L(R)m(R)=
\begin{cases}
\lambda L^{-3/2}R^{1/2},&R\leq L,\\
\lambda L^3R^{-4},&R>L,
\end{cases}
\]
and the two integrals are $2\lambda/3$ and $\lambda/3$. Translation gives $\int\sigma_{z,R}(B)\,dz=|B|$, whence $\mathbb EX(B)=\lambda|B|$. This integrates every spatial parent, including distant centres of large spheres. No bounded-support argument is being used.

Finite expected counts imply finite counts almost surely for each bounded ball; a countable exhaustion gives local finiteness simultaneously. Conditional on all parent marks and counts, a pair of children has zero collision probability because surface-uniform distributions are atomless and the children are independent. The countable set of child pairs suffices to prove simplicity, including pairs from different spheres. Translation and rotation covariance give stationarity and isotropy.

The optional Cox description is also justified for the untruncated construction. Conditional on the parent process, each family is a Poisson process with finite diffuse intensity $m(R)\sigma_{z,R}$. Their sum has directing measure
\[
\Lambda=\sum_{\text{parents }(z,R)}m(R)\sigma_{z,R}.
\]
Its expected mass on a bounded set is $\lambda|B|$, so it is locally finite almost surely. It is diffuse as a countable sum of atomless measures. Conditional Poisson superposition then gives the stated Cox representation. It need not have a Lebesgue density conditionally; the unconditional factorial-measure calculation below proves the required absolute continuity.

### 3. Coarea factors and complete same-parent measures

The starting point (9) is an actual nonnegative measure integral, not a formal density prescription. The shorthand
\[
\sigma_{z,R}(dx)=\frac{\delta(|x-z|^2-R^2)}{2\pi R}\,dx
\]
has the correct normalisation: integrating the delta function gives surface area divided by $2R$, namely $2\pi R$.

For pairs, subtracting the squared-distance equations has derivative of magnitude $2D$ in the centre coordinate. The remaining two-dimensional radial integral is $\pi$ when $R>D/2$. Thus the coefficient is
\[
\frac{\pi}{2D(2\pi R)^2}=\frac{1}{8\pi D R^2},
\]
which gives (11).

For triples, the two linear constraint gradients have cross-product magnitude $4|(x_2-x_1)\times(x_3-x_1)|=8A$. The perpendicular centre coordinate contributes
\[
\int_{\mathbb R}\delta(r^2+t^2-R^2)\,dt
=\frac{1}{\sqrt{R^2-r^2}},
\qquad R>r.
\]
Both roots are included. Combining this with $(2\pi R)^{-3}$ gives precisely (12), with denominator $64\pi^3A R^3\sqrt{R^2-r^2}$.

For quadruples, the three linear centre equations have determinant $8|\det E|=48V$. The unique positive radius integration contributes $1/(2R_*)$. Hence
\[
\frac{1}{48V}\frac{1}{2R_*}\frac{1}{(2\pi R_*)^4}
=\frac{1}{1536\pi^4R_*^5V},
\]
as in (13). No factor from ordered tuples or from the two signs of an orientation is missing. A noncoplanar quadruple has a unique circumsphere; the absolute determinant already handles orientation.

These calculations are valid against nonnegative test functions. One can restrict first to bounded parent/mark ranges and compact subsets where the stated Jacobians do not vanish, apply the ordinary changes of variables/coarea formula, and exhaust the relevant open configuration sets by monotone convergence. The fourth-order centre-radius Jacobian is nonzero on every noncoplanar quadruple. This makes the delta notation a concise representation of a measure proof.

Degenerate tuple sets have zero same-parent measure. Conditional on a fixed sphere, pairs coincide with probability zero, a third point is collinear with two given distinct points with probability zero, and a fourth point lies in the plane of a given noncollinear triple with probability zero. Nonnegative integration of those zero probabilities remains zero. Together with the coarea densities on the complements, this excludes residual singular parts for the concrete continuous-radius model.

For the larger theorem, only the pair and triple versions are needed for arbitrary radius mixing. At fixed $R$, pair distance $2R$ is the antipodal event and has probability zero. The triple threshold $r=R$ means the triangle's plane passes through the sphere centre. Given two non-antipodal children, the third must then lie on a great circle, a surface-null event. The fixed-radius pair and triple measures therefore have the stated densities off their thresholds and no threshold mass. Integrating such absolutely continuous measures against an arbitrary nonnegative radius measure preserves absolute continuity, even if some resulting densities are infinite.

The sentence at line 107 should specify this distinction: arbitrary radius mixing preserves the pair/triple calculation, but an atomic radius distribution can give a singular **fourth** same-parent measure on a fixed-circumradius hypersurface. The proof itself says this at lines 169–173, and the concrete radius law is continuous. This is a wording clarification, not an essential defect in either theorem.

### 4. Genealogies, ordered labels and all parent allocations

Within one family the only observed points are sterile children. There is no root term or later-generation term to add to this defined law. Conditional Poisson counts give $(K)_n$ expectation $m(R)^n$, already present in (9).

Every ordered tuple has a unique partition of its labels according to parent. Ordering blocks by their least label pairs them with the ordered factorial measure of distinct Poisson parents, producing exactly one product of same-parent measures per set partition. There is no further block factorial. Thus (14) is correct as an extended nonnegative measure identity.

At order four the counts are $1+4+3+6+1=15$: one four-child block, four triple-plus-single partitions, three two-pair partitions, six one-pair-plus-two-single partitions, and the all-singleton partition. Equation (15) includes all of them with the right powers of $\lambda$. Finite restrictions and monotone convergence justify the global formula without a fourth-moment assumption. Products involve disjoint coordinate blocks, so the resulting full measures inherit absolute continuity.

The interpretation of $c_n$ as a same-parent coefficient is sufficient throughout. No finite ordinary fourth cumulant or analytic generating-function expansion is being assumed.

### 5. Exact evaluation and positivity

The pair weight is
\[
\frac{q_L(R)m(R)^2}{R^2}
=16\pi\lambda^2
\begin{cases}
1,&R\leq L,\\
L^3R^{-3},&R>L.
\end{cases}
\]
Its total integral is $24\pi\lambda^2L$. Subtracting the integral from $0$ to $D/2$ when $D<2L$ yields
\[
c_2(D)=\frac{3\lambda^2L}{D}-\lambda^2.
\]
This is positive on the entire stated branch. Adding the independent-parent term $\lambda^2$ proves the full reciprocal pair law. The apparent negative constant arises from evaluating a positive integral; there is no signed parent measure.

For $D\geq2L$, the tail integral gives $c_2(D)=4\lambda^2L^3/D^3$, with agreement at $D=2L$. The bound $0\leq c_2(D)\leq3\lambda^2L/D$ holds on both branches. The outside-domain full density is finite and approaches $\lambda^2$ at large separation; it is not a global reciprocal law.

For order four, direct multiplication gives
\[
q_L(R)m(R)^4=4096\pi^3\lambda^4L^3R^5
\]
on both radius regimes. Inserting this into the checked factor $1536\pi^4R_*^5V$ gives $8\lambda^4L^3/(3\pi V)$. The cancellation is exact for the actual law, without a damping limit.

For triples the weight in (12) is exactly that displayed before (20), and (21) follows. If $r\geq L$,
\[
\int_r^\infty \frac{dR}{R\sqrt{R^2-r^2}}=\frac{\pi}{2r}.
\]
If $r<L$, the tail starting at $L$ is $\arcsin(r/L)/r\leq\pi/(2L)$. Substituting $s=\sqrt{R^2-r^2}$ in the lower integral gives $(r^2+s^2)^{-1/4}\,ds\leq s^{-1/2}\,ds$, with upper endpoint below $L$. This proves the uniform bound (23).

Using $r=abc/(4A)$ in the branch $r\geq L$ yields
\[
c_3=\frac{8\lambda^3L^3}{abc},
\]
including its factor eight. All these coefficients have the appropriate spatial dimensions for factorial densities.

### 6. Global regularity and the moment distinction

The pair formula is finite at every positive distance. The triple formula is finite on every noncollinear triple. On a noncoplanar quadruple all pairs are distinct and all faces noncollinear; therefore every partition term and $c_4$ are finite there. Coincidence, collinearity and coplanarity sets are Lebesgue-null. The measure proofs above, not merely pointwise formulas on these complements, establish global absolute continuity.

A finite-almost-everywhere density need not be locally integrable. The fourth measure here is still sigma finite: it can be exhausted by bounded coordinate sets where its finite density is bounded, with the remaining null set carrying zero measure. Infinite mass of a bounded neighbourhood is not a singular component.

The third-moment argument is valid even though a radius-averaged third family-size moment need not be finite. The submitted spatial bounds give
\[
\int_{B^2}D^{-1}\leq2\pi H^2|B|,
\qquad
\int_{B^3}A^{-1}\leq16\pi^2H^4|B|
\]
for bounded $B$ of diameter $H$. In cylindrical coordinates around a fixed pair line, $A=Ds/2$ and the volume factor $s$ cancels $1/s$. Equations (18), (23) and the full third partition formula then make the first three factorial count moments finite. The falling-factorial identity for $N^3$ proves the raw third moment claim.

For every nonempty open ball, a positive-measure family of base triples admits a small cylinder for the fourth vertex within the ball. With normal coordinate $t$, $V=A|t|/3$ and the volume Jacobian is one. The integral of $1/|t|$ diverges; Tonelli yields an infinite fourth factorial moment because $\rho^{(4)}\geq b_4/V$. The raw fourth moment is also infinite. Equality of these two extended expectations in (26) is used correctly, not as an identity between the corresponding random variables.

The moment class agrees with what S1 would require, but is not sufficient for S1. In S1 itself, finite third moments first follow on sufficiently small sets and extend to arbitrary bounded sets by a finite cover and $(\sum_{i=1}^qN_i)^3\leq q^2\sum_iN_i^3$. This justifies the necessary-moment statement cited from the earlier proof.

### 7. Both concrete exact-target failures

**Triangle law.** Near any three distinct collinear points of diameter below $M$, the three side lengths remain bounded away from zero. As noncollinear triples flatten, $r=abc/(4A)$ tends to infinity and eventually exceeds $L$. The explicit expression $8\lambda^3L^3/(abc)$ then bounds $c_3$ uniformly, and the pair terms in the full third density are uniformly bounded as well. For every candidate $a_3>0$, $a_3/A$ exceeds this common bound on an open, positive-measure set of sufficiently flat noncollinear triples still below diameter $M$. This is a contradiction to almost-everywhere equality, not an argument based only on a null collinear set.

**Fourth law.** Choose a small planar square with diameter below $M$. In a neighbourhood of it, all distances and all four face areas stay positive and bounded away from zero. Equations (18) and (23) uniformly bound every lower-block term of (15). Thus
\[
V\rho^{(4)}\longrightarrow b_4
\]
along every noncoplanar approach. An a.e. reciprocal-volume law would permit sequences approaching this square outside its exceptional null set, forcing $a_4=b_4$. But at every noncoplanar configuration the full density satisfies
\[
\rho^{(4)}\geq b_4/V+\lambda^4>b_4/V.
\]
This excludes the full fourth law. Positivity alone would not have excluded a larger constant $a_4$; the bounded-remainder limit is the essential step fixing that constant first. The submission supplies it correctly.

### 8. Arbitrary-radius/count sphere-family obstruction

The theorem in Section 7 does not assume Poisson offspring counts. Let $\mu(dR)$ be the parent radius intensity and $k_j(R)=\mathbb E[(K)_j\mid R]$. The independent surface-uniform locations give the same pair/triple kernels with $q(R)m(R)^j\,dR$ replaced by $k_j(R)\mu(dR)$. Finite positive intensity is $\lambda=\int k_1\,d\mu$. If a sigma-finite marked parent intensity is used, deleting empty families leaves nonempty-parent rate at most $\lambda$.

The fixed-radius threshold discussion in Section 3 above makes (30) a genuine triple measure identity for arbitrary radius mixing:
\[
c_3=\frac{F(r)}{A},
\qquad
F(r)=\frac{1}{64\pi^3}\int_{(r,\infty)}
\frac{k_3(R)}{R^3\sqrt{R^2-r^2}}\,\mu(dR).
\]
Extended values are permitted before the desired identities are assumed. No fourth factorial moment or fourth density enters this theorem.

Poisson parent allocations give $\rho^{(2)}=c_2+\lambda^2$ and $\rho^{(3)}=c_3+\lambda\sum c_2+\lambda^3$. Substituting the proposed full pair identity into the full triangle identity yields, almost everywhere,
\[
F(r)=a_3-\lambda a_2A(1/a+1/b+1/c)+2\lambda^3A.
\]
The sign and factor two are correct: three pair baselines are subtracted, and the independent triple baseline adds one back.

The reduction to shape variables is legitimate. Away from degeneracy, translation, a local orientation chart and side lengths give smooth coordinates with positive Jacobian. Side lengths are in smooth bijection with $(r,\alpha,\beta)$ in the open angle simplex through the sine rule, with smooth inverse from the cosine rule and the circumradius formula. Pullbacks of pair null sets to triple space are null by Fubini. Therefore the a.e. configuration identities imply the displayed shape identity for almost every $(r,\alpha,\beta)$.

For every $0<r<M/2$, all triangle angles yield side lengths less than $M$. Fubini selects almost every such $r$ for which $F(r)$ is finite and the equation holds for almost every angle pair. The right side is continuous on the open angle simplex; equality to a constant almost everywhere therefore implies equality everywhere there. This is why evaluation on the null subfamily of right triangles is valid.

For a right triangle on that circumcircle, write the legs as $2r\sin\theta$ and $2r\cos\theta$, and the hypotenuse as $2r$. With $p=\sin\theta+\cos\theta$,
\[
F(r)=a_3-\lambda a_2r\,p
\frac{-\lambda a_2r+4\lambda^3r^2}{2}(p^2-1),
\qquad 1<p<\sqrt2.
\]
A polynomial constant on a nontrivial interval has zero linear coefficient. Here that coefficient is $-\lambda a_2r<0$. This proves the incompatibility. It is not a finite numerical check or an assumption of continuity of the unknown $F$; only the explicit angle expression is continued.

### 9. Consequential earlier dependencies and prior findings

The complete supplied v01 and v02 proofs were read. Their specific exclusion theorems are not premises of the new sphere construction. Their consequential shared ingredients are the whole-space translation argument, nonnegative Poisson partition expansion, moment distinctions, and the statement of what earlier models could not do. Those ingredients were independently re-established above.

The earlier fixed-displacement theorem has the stated narrow scope. In its finite fourth offspring-moment branch, subcriticality follows from the total-generation intensity, and the truncated progeny recursion gives finite fourth total-family moments. The bound $\int C(B-z)^jdz\leq |B|T^j$ then gives finite fourth local moments. In the infinite fourth offspring-moment branch, the direct-sibling submeasure factors as $\nu\mathbb E(K)_4 H_4$, and $\int_{B^4}H_4=\int q_B(z)^4dz\in(0,|B|]$ makes the infinite density occur on positive measure. This is different from merely having an infinite integral of a finite density. None of these hypotheses can be silently transferred to the radius-dependent sphere model.

The supplied v02 Gaussian model uses a normalisable mark-dependent displacement density, includes observed roots, and has the checked relation $\det S_4=9V^2$. Its damped four-child coefficient and bounded remainder near ordinary coplanarity have the consequences stated in the supplied issue list. Its radial-productivity pair obstruction rests on the exact angular integral bounds and dominated-convergence dichotomy, not a formal expansion. These are independent scoped failures; they neither obstruct nor certify the new sphere construction. The v02 source's plane-field example is a prior diagnostic lead, not a theorem used to prove v03.

Disposition of every supplied prior issue is as follows. “Retained” means the scope or obligation remains; it does not treat a previous verdict as proof evidence.

| Prior ID | Current disposition |
|---|---|
| P3-R01 / P3-V02-01 | Exact S1 obligation remains open. A full pair-law achievement is new, but Sections 6–7 prove the present law/class cannot supply the simultaneous target. |
| P3-R02 / P3-V02-02 | Prior exclusions remain limited to their stated models. The new theorem has its own sphere-family hypotheses and gives no general S1 non-existence result. |
| P3-R03 / P3-V02-04 | Ordered selections and all parent partitions have been rechecked for the new law. Latent parents are excluded by the definition of the observed process, not omitted from an observed-root density. |
| P3-R04 / P3-V02-06 | Global full absolute continuity, finite-a.e. densities, local third-moment finiteness and fourth-moment divergence have each been re-established. |
| P3-R05 | The supplied v02 clarification correctly treats equal spatial locations of distinct space-time roots through the Poisson second factorial measure and countable exhaustion. No time projection is used in v03. |
| P3-R06 / P3-V02-09 | The precise supplied seed cluster-law passage supports the bounded-size/source-scope attribution. Complete seed construction theorems and historical approval labels are not dependencies or newly certified results. |
| P3-V02-03 | Existence and intensity have been checked over all spatial parents for the new unbounded-radius law. |
| P3-V02-05 | The new coarea constants were independently recomputed; the earlier Gaussian determinant is not reused as a sphere Jacobian. |
| P3-V02-07 | Every full fourth-order remainder is bounded near the selected coplanar square. The constant leading coefficient is fixed first, then the strictly positive remainder excludes exactness. |
| P3-V02-08 | The new arbitrary-radius/count theorem treats extended integrals and a.e. identities through actual measure formulas and smooth shape coordinates. |
| P3-V02-10 | Failure of the concrete triangle law is proved explicitly. The broader theorem additionally rules out repairing both pair and triangle laws solely by changing radius/count mixing within the stated class. |
| v02 minor: configuration dependence | The new fourth same-parent coefficient is constant. The report preserves its distinction from the earlier configuration-dependent Gaussian coefficient. |
| v02 minor: family-wide regularity | The concrete law's third/fourth regularity is not asserted for arbitrary radius/count laws. The broader obstruction only requires its stated hypotheses. |

## Finding register

| ID | Location | Precise mathematical issue | Consequence | Repair/status |
|---|---|---|---|---|
| P3-V03-01 | Exact claim; Sections 6–7, 9 | The process does not satisfy the simultaneous full third and fourth reciprocal identities. | No S1 pass; third unsuccessful exact-target submission. | Open target obligation, explicitly acknowledged by the author. |
| P3-V03-02 | Section 1, (3)–(8) | Infinite latent radius mass and unbounded spatial influence require an actual process and whole-space intensity calculation. | A purely formal cluster sum or bounded-neighbourhood argument would be insufficient. | Checked: nonempty-parent rate is finite, intensity is exactly $\lambda$, local finiteness and simplicity follow. |
| P3-V03-03 | Sections 2.1–2.3, (10)–(13) | Sphere normalisation, centre Jacobians, two triple roots and the fourth radius derivative must all be included. | Wrong factors would change every exact coefficient. | Checked: $2D$, $8A$, $48V$, $2R_*$ and $2\pi R$ yield the displayed constants. |
| P3-V03-04 | Sections 2.4 and 5 | Densities on nondegenerate configurations alone do not exclude singular mass. | S1's global measure requirement would otherwise remain unproved. | Checked: conditional degeneracy probabilities vanish and coarea covers the complement; all full densities are finite a.e. globally. |
| P3-V03-05 | Section 3, (14)–(15) | Every ordered genealogy and all fifteen parent partitions are required. | Same-parent attainment cannot be mistaken for a full-density theorem. | Checked: all partitions and powers of $\lambda$ are correct; no observed root is part of this defined law. |
| P3-V03-06 | Section 4.1 | Exact cancellation of the independent-parent pair baseline must arise from a positive law for every prescribed parameter pair. | A signed residual or low-intensity restriction would not establish the claimed pair result. | Checked: positive radius-tail integral gives $c_2=3\lambda^2L/D-\lambda^2$ on $D<2L$; choose $L=M/2$. |
| P3-V03-07 | Sections 4.2 and 6.2 | Exact $c_4=b_4/V$ leaves positive lower-block terms in $\rho^{(4)}$. | The full fourth law fails despite the correct singular coefficient. | Checked: bounded remainder near coplanarity forces $a_4=b_4$, then $\lambda^4>0$ contradicts equality. |
| P3-V03-08 | Sections 4.3, 5 and 6.1 | Local third-moment finiteness and triangle-law failure need the actual spatial third density, not a total-family moment bound. | An infinite family-size moment does not settle either local claim. | Checked: the $1/A$ bound gives finite local third moments; the large-circumradius branch is bounded near distinct collinear triples and excludes $a_3/A$. |
| P3-V03-09 | Section 5, (26) | Infinite fourth local mass must remain compatible with a.s. local finiteness and finite-a.e. densities. | It is a necessary S1 moment feature, not a general obstruction to its broad class. | Checked by the transverse $1/|t|$ integral and the independently proved first-moment bound. |
| P3-V03-10 | Section 7, (30)–(33) | Arbitrary radius/count mixing, threshold atoms, a.e. equality and evaluation on right triangles require justification. | Without these steps the larger incompatibility theorem would be incomplete. | Checked: fixed-radius threshold mass is zero; Fubini and continuity in shape variables justify the polynomial contradiction. |
| P3-V03-11 | Section 7 theorem; Section 9 | The obstruction depends on Poisson parents and conditionally iid uniform common-sphere children. | It cannot exclude S1 generally or authorise a target-domain revision. | Scope correctly retained; no general amendment consequence. |
| P3-V03-12 | Line 107, read with lines 169–173 | “The following calculations also apply” to arbitrary radius measures can be read as extending the fourth density formula to atomic mixing. | Such an extension would be false: fixed radius can give singular fourth same-parent mass. Neither proved result uses it. | Minor clarification: restrict the arbitrary-measure density statement to pairs/triples and state continuous-radius necessity for (13). |
| P3-V03-13 | Sections 8 and 11; supplied prior proofs and source excerpts | Historical leads and earlier issue statuses must not substitute for proof dependencies. | No full-seed approval, other-track inference or inherited desired verdict is justified. | Checked consequential dependencies independently; no essential external source is outstanding. |

## Amendment implications

The new results prove no restriction on the general S1 process class or geometry. They show that a successful construction cannot remain inside the exact Poisson/iid-common-sphere family of Section 7 while satisfying both full pair and triangle laws. Departing from that family is a model choice, not a necessary change to S1.

The finite-fourth-moment comparison remains impossible if the full reciprocal-volume law holds on all sufficiently small nondegenerate quadruples. This is the already relevant local moment obstruction, and v03 supplies a process demonstrating compatibility of infinite fourth moments with all the basic process and density regularity requirements. It does not justify adding a lower altitude cutoff.

The supplied S0-to-S1 record is the authority for the current target; this review does not newly audit unassigned global-obstruction proofs or change the preserved S0 verdict. No amendment is proposed in v03. After this third unsuccessful exact-target review, the author may use the protocol's optional owner checkpoint for a precise proposal, but none has been requested here and no approval is inferred. One submission remains; there is no reset.

## Source and coding evidence

The frozen proof-reviser skill, proof standard and writing-style reference were applied. Packet hashes and every allowed-file hash were verified before mathematics; the evidence is saved separately.

The mathematical source/dependency audit has the following scope:

| Material | Use and verified scope |
|---|---|
| Current `proof_snapshot.md` | Entire submission read and audited, including actual law, all measure calculations, both failure proofs, larger theorem, response table and limits of scope. |
| `prior_dependency_v01.md` / `prior_dependency_v02.md` | Both entire supplied texts read. Consequential partition, translation, moment and model-scope statements independently checked; their specific model formulas were reconstructed where relevant to the current attribution and response obligations. |
| `previous_issue_list_v01.md` / `previous_issue_list_v02.md` | Used only as obligations to re-establish; every supplied item is addressed above. Prior status labels were not evidence of correctness. |
| Assigned `nonexistence_2/submissions/v01.md` | Lemma 2, Theorems 3–4 and the cited shrinking-cluster example checked for the local-integrability/moment distinction and the count-dependent geometry boundary case. No general conclusion beyond those uses is imported. |
| `cited_coordinator_submission_v02.md`, `cited_flattening_domain_supplement_v02.md`, `cited_relative_shape_supplement_v01.md` and provenance | The displayed domain and low-intensity qualifications support the claimed limitations of those leads. The relative-shape excerpt ends before a full proof; no complete seed theorem is certified. |
| `cited_seed_cluster_law.md` | Confirms the stated at-most-four-points family law and all-partition interpretation used for the earlier source-scope discussion. The general finite-family moment inequality explains its inability to satisfy unrestricted local reciprocal volume. |
| `cited_seed_section_5.md` | Confirms the plane-field example is explicitly a same-parent/factorial-cumulant diagnostic and includes positive full-density partition terms. It is not a premise of the sphere construction. |
| Common context and primary-source index | Background only. No DVJ quotation, present open-status statement, priority claim or specialised external theorem is used to reach this verdict. |

No missing essential mathematical source was identified, so no additional source request was necessary. The new arguments reduce to the displayed coarea/change-of-variable calculations, elementary Poisson factorial moments, Tonelli, monotone convergence, a basic smooth coordinate argument and continuity. No external PDF or website, numerical fit, simulation, coding service or proof assistant was used. Hash and telemetry scripts are administrative checks, not mathematical certification.

## Presentation judgement

The proof is readable and candid about what it establishes. It distinguishes full densities from same-parent terms before presenting the attractive reciprocal-volume formula, derives the law before the density calculations, and proves the failure statements instead of treating them as unexplained limitations. Its separation of local moment finiteness, almost-sure local finiteness, finite-a.e. densities and absence of singular mass is particularly useful.

Only a small scope clarification is needed at line 107: “For pairs and triples, the formulas below also hold with arbitrary nonnegative radius mixing; the fourth-order density formula uses an absolutely continuous radius law.” Retain the existing explanation at lines 169–173. It would also help to state explicitly once that the independent-parent lower-block remainder is nonnegative and is uniformly bounded only in the chosen nondegenerate coplanar neighbourhood, rather than globally.

The long review-response table is appropriate for the experiment record. It is not needed for a future standalone mathematical presentation. No manuscript rewrite or change to a frozen source was made.

## Review summary and repairs

The decisive positive checks are the finite-rate nonempty-parent realisation, exact intensity integral, sphere coarea factors, positive radius-tail cancellation of the pair baseline, and globally valid full partition formula. They establish the claimed partial law with the permitted infinite-fourth-moment behaviour for every prescribed intensity and diameter.

The decisive negative checks are different at the two higher orders. Near distinct collinear triples, the full third density stays bounded and therefore cannot be $a_3/A$. Near ordinary coplanarity, the full fourth density has coefficient $b_4$ but retains strictly positive lower-block terms, preventing exact $a_4/V$. The larger sphere-family theorem additionally shows that adjusting only radius mixing or count laws cannot repair simultaneous pair and triangle exactness.

The remaining S1 obligation is an actual process satisfying all three full identities simultaneously, with global regularity and the independent $(\lambda_0,M)$ quantifiers. This submission does not supply such a process or prove general non-existence. No unresolved essential gap remains in the narrower results accepted here. The only recommended local repair is the arbitrary-radius wording clarification; it does not change the verdict.

This is an independent review of one track's third submission, not a cross-track final synthesis. It preserves the previous targets and attempt outcomes, records no amendment and makes no claim of machine-verified proof.

## Accounting scope

Only this reviewer's own `session_meta`, `turn_context` and `token_count` metadata fields were extracted. No session conversation or private reasoning payload was exposed. Numeric per-event and cumulative input, cached input, cache-write input, output, reasoning-output and total counters are available; preflight capability and checkpoints were saved before substantive work.

`accounting_record.json` records the latest exposed checkpoint and its coverage. Cumulative snapshots are not summed, and reasoning-output tokens are not added again to output. No subagent was dispatched. Runtime child-inclusion semantics, completed-turn tail usage and monetary charges are NR where not exposed. The final checkpoint is a measured session prefix, not an invented completed-turn total or a document-length estimate.
