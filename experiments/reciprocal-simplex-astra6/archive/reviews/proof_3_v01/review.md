# Review — proof_3 / submission v01 / target S1

- Reviewer: `/root/review_proof_3_v01`; session `session-13`; turn `turn-25`.
- Requested and runtime-verified model/effort: `gpt-6-astra`, `xhigh`.
- Turn-context timestamp: `2026-10-20T17:36:39.581Z`. Preflight completed at `2026-10-20T17:37:24.656319+00:00`, before mathematical review. The separate freeze record gives the report completion timestamp.
- Active statement: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Adoption record: `statements/S0_to_S1.md`, SHA-256 `b2534040520dfc63bf5c22ecc508257308e619a040a7c6c54ce44375742394de`.
- Frozen submission: `reviews/proof_3_v01/proof_snapshot.md`, SHA-256 `77ab351888c26bb524f694c8eb2f191e0775dfcdc152d8d077adca99a7363736`.
- Initial review packet: `packets/review_proof_3_v01.json`, SHA-256 `c26544731955de474061c464847229ec989729c7a234c99248221b4f424b10d4`.
- Narrow source supplement: `packets/review_proof_3_v01_source_01.json`, SHA-256 `231ccbb1107cfe6a201d1d6f76f9784fdce01735032fca3fadea2c85074b0c13`.
- Type: fresh independent review of the complete frozen submission, including its ancillary claims. This is not a final synthesis or a review of another construction track.

All relative paths in this report refer to `runs/20261020T164437Z_astra6/`. The assigned output directory is `reviews/proof_3_v01/`. The initial packet and every listed allowed-file hash matched. The source-supplement and excerpt hashes also matched.

Received context comprised the frozen procedural and target files, the proof-reviser skill and both required references, this submission, the supplied `nonexistence_2` proof, and the expressly cited seed excerpts. I did not inspect author conversations, private work, prior review reports, other construction submissions, old runs or other chats. Statements that an earlier proof was approved were not used as mathematical evidence. Own-session inspection was restricted to session metadata, turn context and token fields. No delegation was used.

## Correctness verdict and scope

**The submission establishes its stated scoped obstruction. It is partial progress and does not pass the exact S1 construction target.** I found no invalid mathematical step in the stated obstruction, the full genealogy and immigrant-partition formulas, the finite-moment argument, or the specified finite-time spatial projection result. The compact projection-simplicity argument can be made more explicit, as recorded below; its missing sentence is supplied here and does not leave an unresolved proof gap.

The accepted obstruction concerns the following precise family:

1. Homogeneous Poisson immigrants of fixed rate $\nu>0$ on $\mathbb R^3$.
2. Independent identically distributed offspring counts $K$, finite almost surely, at every individual.
3. One fixed Lebesgue probability density $f$ for all child displacements, with independent displacements independent of the counts and all other reproduction events.
4. Independent families, with every immigrant and every descendant observed.

Within this family, finite positive intensity forces $m=\mathbb EK<1$. For every such model and every $M>0$, the full fourth factorial measure cannot equal $a_4/V$ on $E_4(M)$ for any $a_4>0$. The pair and triangle laws are not needed for this conclusion. Thus the theorem excludes every choice of the model parameters at every prescribed pair $(\lambda_0,M)$, not merely a restricted intensity range.

The proof does **not** exclude general branching constructions, marked models, count-dependent spatial laws, random kernels shared within a family, mixtures of different branching laws, interacting processes, or arbitrary stationary processes. It supplies no general non-existence theorem for S1. The author states these limitations correctly.

The attempt remains **submission 1 of 4, unsuccessful as an exact-target construction, with a valid subclass obstruction**. Three substantive submissions remain under the supplied workflow. Neither acceptance of this obstruction nor its proof completeness resets that count or justifies declaring the whole approach unsuccessful after one submission.

## Reconstruction and detailed audit

### 1. Active target and local moment requirements

S1 prescribes $\lambda_0>0$ and $M>0$ independently. It requires one stationary simple process on the whole of $\mathbb R^3$, finite almost surely on bounded sets, with actual full factorial measures of orders two through four. Their densities must be finite almost everywhere globally, with no singular part, and must equal the reciprocal-simplex expressions on every nondegenerate configuration of diameter less than $M$. Values outside those domains are free. No fourth count moment is imposed.

The submission preserves each of these quantifiers and requirements. Its theorem is a negative result for a specified construction family; it does not offer a smaller-domain construction as an S1 solution.

The calculation in Section 1, equations (2)–(4), is correct. For a noncollinear triple in an open ball $B$, let $A>0$ be its area and write the fourth point in orthogonal coordinates relative to the base plane. The cylinder centred at $x_1$ with both planar radius and normal half-width $\delta$ stays inside $B$ because its distance from $x_1$ is less than $\sqrt2\,\delta$. The coordinate Jacobian is one and
\[
V=\frac{A|t|}{3}.
\]
The integral over that cylinder therefore contains
\[
\frac{3\pi\delta^2}{A}\int_{0<|t|<\delta}\frac{dt}{|t|}=\infty.
\]
The base triples that are collinear form a null set. Tonelli gives an infinite integral over $B^4\cap\{V>0\}$. With $\operatorname{diam}(B)<M$, this lies in the prescribed fourth-order domain. Equality almost everywhere is enough: removing a Lebesgue-null exceptional set does not change an integral with respect to Lebesgue measure. Consequently
\[
\mathbb E(X(B))_4=\infty,\qquad \mathbb EX(B)^4=\infty.
\]
These two expectations are both infinite; the displayed equality in the submission is not an assertion that the two finite random-variable expressions agree. Every nonempty open ball contains a sufficiently small ball, so the fourth-moment conclusion extends to every open ball.

The lower-order bounds in equation (5) also have the correct constants. At fixed $x_1$, the pair difference lies in the radius-$L$ ball, giving $\int |u|^{-1}\,du=2\pi L^2$. At fixed $u\ne0$, cylindrical coordinates for $v$ give
\[
\int_{|v|\le L}\frac{dv}{|u\times v|}
\le \frac{4\pi L^2}{|u|}.
\]
The factor two in $A^{-1}=2|u\times v|^{-1}$ produces $16\pi^2L^4|Q|$ after integrating $u$ and $x_1$. The degenerate sets are null, and full absolute continuity excludes additional measure there. The identity
\[
N^3=(N)_3+3(N)_2+N
\]
therefore gives a finite third moment on each small cube. A finite cube cover and $(\sum_i b_i)^3\le q^2\sum_i b_i^3$ extend that conclusion to any bounded Borel set. No information about the unprescribed large-diameter densities is being silently assumed in this extension.

These two conclusions are compatible: finite third local moments and infinite fourth local moments do not by themselves contradict almost-sure local finiteness. This distinction is preserved throughout the submission.

### 2. Whole-space construction, intensity and simplicity

The countable tree-label construction specifies a genuine reproduction law. Independent arrays of offspring counts and edge displacements can be assigned to the finite-word label space, then restricted to the realised family. Conditional on that tree, its edge displacements remain independent with density $f$. This last fact uses exactly the stated independence between counts and geometry.

For any realised family, including a potentially infinite one, the identity
\[
\int_{\mathbb R^3}C(B-z)\,dz=|B|T
\]
is a nonnegative sum of translated indicator integrals. It needs neither bounded cluster radius nor finite $T$. Campbell's first-moment formula for marked Poisson parents, or its elementary simple-function derivation given in the submission, now yields
\[
\mathbb EX(B)=\nu|B|\mathbb ET
             =\nu|B|\sum_{j\ge0}m^j.
\]
For finite $m$, the generation expectations follow by conditioning. If $m=\infty$, the first generation already has infinite expectation, which suffices for the intensity exclusion. At $m=1$ the sum diverges even if a particular critical offspring law dies out almost surely. Thus almost-sure extinction alone cannot replace the intensity calculation.

Finite positive intensity indeed forces $m<1$. Then $\mathbb ET=(1-m)^{-1}<\infty$, hence $T<\infty$ almost surely. Setting $\nu=\lambda_0(1-m)$ attains any positive intensity before asking for the reciprocal laws. In particular, the obstruction is not caused by a failure to tune the mean intensity.

Finite expectation of each bounded count proves its almost-sure finiteness. A countable exhaustion by balls supplies simultaneous local finiteness; no finite interaction range is used. Translation covariance of the independently marked homogeneous immigrant process gives stationarity in law.

For simplicity, two different vertices in the same tree have a positional difference containing an edge variable with coefficient $+1$ or $-1$ that is absent from their common ancestral path. Conditioning on the tree and the other edge variables leaves that edge diffuse. For different families, an analogous independent edge works unless both vertices are roots, in which case Poisson simplicity applies. Countably many labels and parents permit a countable union of these null events. This argument is valid for irregular $f$ and unbounded displacements.

The endpoint $m=0$ causes no exception: $K=0$ almost surely, $T=1$, and the process is a Poisson process with finite fourth local moments. Infinite mean offspring counts and all $m\ge1$ have already been excluded by the finite-intensity requirement, not by an unstated assumption.

### 3. Complete genealogy and immigrant-partition formulas

Equations (10)–(12) correctly enumerate the whole family law. A finite rooted ordered tree $\tau$ has probability
\[
P_\tau=\prod_{v\in\tau}p_{d_v}.
\]
The numbering of children is part of the underlying probability construction. No additional factorial for reordering children belongs here. Since the tree is finite almost surely when $m<1$, these probabilities sum to one over the countable collection of such trees.

For a fixed tree and an ordered selection of $r$ distinct vertices, the transformation from the root coordinate and all edge displacements to all vertex coordinates is triangular in a parent-before-child ordering. Each diagonal block is the $3$-dimensional identity, so the absolute determinant is one. Fixing the selected coordinates and integrating every unselected coordinate gives exactly equation (11). Integrating the root when it is unobserved is essential and has been included.

Summing over every tree and every ordered selected vertex tuple counts all ancestor–descendant, sibling and more distant relationships. Unobserved leaves, intermediate vertices and ancestors are integrated out, not discarded. For $r=1$, each selected vertex has Lebesgue intensity one after integrating the root location and the edge increments, giving $c_1=\nu\mathbb ET=\lambda$.

For the full factorial measure, each observed tuple determines one partition of its labels according to immigrant. Ordering the blocks by their least elements produces a unique ordered list of distinct immigrants. The Poisson factorial measure of those immigrants is $\nu^{|\pi|}$ times product Lebesgue measure; independent cluster marks then produce one $c_{|I|}(x_I)$ factor per block. There is no missing block-order factorial. Equation (13) is therefore a full measure identity for nonnegative tests.

The fourth-order expansion has all $15$ partitions:

- one partition of type $1+1+1+1$, contributing $\lambda^4$;
- six of type $2+1+1$, contributing $\lambda^2\sum c_2$;
- three of type $2+2$, contributing $\sum c_2c_2$;
- four of type $3+1$, contributing $\lambda\sum c_3$;
- one of type $4$, contributing $c_4$.

The second- and third-order expansions also agree with their partition counts. These formulas are not substitutions of a reproduction kernel or a connected density for a full density.

All integrations and sums here are nonnegative. Tonelli and monotone convergence therefore apply even when the resulting measure is not locally finite. For products of extended factors, the stated $0\cdot\infty=0$ convention agrees with the nonnegative product-integral construction and with increasing truncations. Equivalently, zero-probability trees may be omitted before forming their weighted terms.

Every fixed-tree measure is represented by a Lebesgue density, and the countable sum still has zero mass on Lebesgue-null sets. Thus there is no omitted singular component. This does **not** prove that the resulting density is finite almost everywhere: the infinite-offspring-moment case shows why that additional distinction matters. The proof handles extended measures directly and does not invoke a Radon–Nikodym theorem under an unverified sigma-finiteness hypothesis.

### 4. Finite fourth offspring moment

For an arbitrary finite cluster of size $T$ and $N_z=C(B-z)$, the inequalities
\[
N_z^r\le T^{r-1}N_z,\qquad
\int N_z^r\,dz\le |B|T^r
\]
are valid for $1\le r\le4$, including empty counts. Thus $\mathbb ET^4<\infty$ makes all four parent-integrated raw moments $\Psi_r(B)$ finite.

The fourth raw count moment in equation (16) has the correct Bell-polynomial coefficients:
\[
\Psi_4+4\Psi_3\Psi_1+3\Psi_2^2
       +6\Psi_2\Psi_1^2+\Psi_1^4.
\]
Here the factors use raw within-cluster powers, as appropriate when expanding the raw fourth power of the total count. First restricting parents to a bounded set avoids any question about an infinite sum of parent contributions. Increasing those sets and applying monotone convergence proves the whole-space formula. This controls distant parents without any cluster-radius assumption.

The implication $\mathbb EK^4<\infty\Rightarrow\mathbb ET^4<\infty$ is proved rather than merely quoted. At finite generation depth, grouping the factors in a power of the child sum by equal child labels gives equation (19). In the expansion of $\mathbb E(1+S)^r$, the only occurrence of the previous-depth $r$th moment is the one-block term with coefficient $m$. Every other factor has strictly smaller positive order. Induction over $r=2,3,4$ therefore supplies a depth-independent constant $C_r$ with
\[
M_r(\ell)\le mM_r(\ell-1)+C_r.
\]
Since $m<1$, the recurrence is uniformly bounded. Increasing generation depth then gives the claimed finite moments of $T$.

It follows that the full fourth count moment is finite on every bounded window in this branch of the dichotomy. This contradicts the local reciprocal-volume integral. No assumption that $f$ is bounded, smooth or compactly supported enters this argument.

### 5. Infinite fourth offspring moment and irregular displacement densities

This is the decisive second half of the theorem. For an integer-valued finite $K$, $\mathbb EK^4=\infty$ implies $\mathbb E(K)_4=\infty$ because the two functions are comparable for large $K$.

Ordered quadruples of distinct direct children of a single immigrant give a genuine submeasure of the full fourth factorial measure. Conditional on $K=k$ and the parent location $z$, its density is
\[
(k)_4\prod_{i=1}^4f(x_i-z).
\]
Independence from $K$ allows the same spatial kernel
\[
H_4(\mathbf x)=\int\prod_{i=1}^4f(x_i-z)\,dz
\]
to appear for every $k$. Therefore the nonnegative series in equation (21) is infinite wherever $H_4>0$. This inference would fail for a general count-dependent family of displacement densities; that is an actual hypothesis boundary, not a technical regularity preference.

The positivity argument for $H_4$ is sound for every Lebesgue probability density. For bounded $B$ with $|B|>0$,
\[
q_B(z)=\int_Bf(x-z)\,dx,\qquad
0\le q_B\le1,\qquad \int q_B=|B|.
\]
Hence $q_B>0$ on a set of positive measure and
\[
0<\int q_B(z)^4\,dz
 =\int_{B^4}H_4(\mathbf x)\,d\mathbf x
\le |B|<\infty.
\]
Thus $H_4$ is positive on a positive-measure subset of $B^4$ and finite almost everywhere there. No open set on which $f$ is positive is required. Disconnected support, support with empty interior, unbounded density and heavy displacement tails do not invalidate the argument.

Taking $\operatorname{diam}(B)<M$ and deleting coplanar configurations leaves a positive-measure set $S$ inside $E_4(M)$ on which the sibling density is infinite. On that set $a_4/V$ is finite pointwise. Some bounded level set
\[
S_j=S\cap\{a_4/V\le j\}
\]
has positive measure, because the countable union of the $S_j$ exhausts $S$. The sibling submeasure assigns $S_j$ infinite mass, while the required full measure assigns at most $j|B|^4$.

This is a measure contradiction, not an informal comparison of two pointwise representatives. It also avoids the false inference that a nonintegrable finite-a.e. density must be infinite on positive measure. All other genealogies and immigrant allocations are nonnegative and cannot cancel the sibling contribution.

After the finite-intensity reduction to $m<1$, the alternatives $\mathbb EK^4<\infty$ and $\mathbb EK^4=\infty$ exhaust the model. The accepted theorem therefore has no remaining offspring-moment case.

### 6. Poisson reproduction and temporal projection

Poisson reproduction with any finite mean has a finite fourth moment. At $m<1$ the preceding finite-moment argument applies; at $m\ge1$ the positive-rate immigrant representation has infinite mean measure. Taking $m$ close to one changes neither conclusion for an individual process. The author correctly makes no claim that a limiting construction or a parameter mixture inherits a suitable moment bound.

The separate space-time construction in Section 6 is also valid under its stated hypotheses: homogeneous Poisson immigrants on $\mathbb R^3\times\mathbb R$, absolutely continuous offspring displacements with positive time lags, Poisson reproduction and $m<1$. The count in $B$ after restriction to a finite interval $I$ and spatial projection is the original count in $B\times I$, provided spatial coincidences are absent.

That absence can be checked fully as follows. Distinct space-time immigrant roots have distinct spatial coordinates almost surely: in each bounded space-time box, the Poisson second factorial measure gives zero mass to pairs with equal spatial coordinates; a countable exhaustion handles all roots. For every other pair of vertices, condition on its finite trees and the other edge variables. A noncancelled edge has an absolutely continuous spatial marginal, so its spatial difference has no atom at zero. Countably many pairs finish the argument. Restricting to a time slab cannot create a spatial coincidence that was absent beforehand. This supplies an explicit justification for the compressed sentence at submission lines 480–481.

The dimensional version of the translation bound is
\[
\int_{\mathbb R^4}C(B\times I-z)^r\,dz
\le |B||I|T^r.
\]
Consequently all projected bounded-window fourth moments are finite, including contributions from parents arbitrarily far away in space or time. The projected intensity is $\nu_{\mathrm{st}}|I|/(1-m)$, and spatial stationarity follows from the translation invariance of the space-time construction.

Because projection is injective on the retained countable configuration almost surely, projected distinct tuples correspond to retained space-time distinct tuples. Integrating their full densities over $I^n$ therefore gives the full projected factorial measures. Absolute continuity is preserved by this marginalisation; finite fourth local moments give finiteness almost everywhere through order four. The projected process cannot satisfy S1's fourth law.

Projecting all times instead gives infinite expected counts in every positive-volume bounded spatial set by nonnegative integration of the constant space-time intensity. This is already incompatible with prescribed finite intensity. No assertion about equivalence with arbitrary temporal, marked or nonlinear Hawkes models is needed or established.

### 7. Cited boundary example and seed scope

The supplied `nonexistence_2` Theorems 3 and 4 can be checked directly. The near-coplanar integral is the same local mechanism used above. Its shrinking-cluster example uses $\mathbb P(N=n)=cn^{-5}$ and offspring radius $r_n=1/(10n)$. It has finite first and third offspring moments, infinite fourth factorial offspring moment, and bounded cluster radius. The resulting process has the claimed finite intensity and local finiteness. For a fixed distinct tuple of positive diameter $d$, its same-parent density receives contributions only from $n\le1/(5d)$, so the displayed density is a finite sum. The partition expansion then gives full densities finite on distinct tuples, despite infinite fourth local moments.

This example supports precisely the logical boundary claimed in the submission. Its geometry depends on $N$, and it is not the fixed count-independent spatial reproduction law in the theorem. It does not give reciprocal-simplex laws. I did not use its prior review status as evidence.

The three initial seed excerpts directly establish their different fourth-order domains and their sufficiently-small-intensity quantifiers. A positive altitude threshold, a relative-altitude threshold, and the displayed selected flattening condition each leave out nondegenerate configurations admitted by $E_4(M)$. For the flattening condition, for example, a generic coplanar quadrilateral has a positive value of $e$ while its small noncoplanar perturbations have $h_4\to0$; after scaling to diameter below $M$, these perturbations violate $e^2\le Mh_4$. Thus permitting some arbitrarily flat shapes does not make that domain the whole S1 domain.

The initially supplied excerpts did not show the cluster-size law. I requested the exact passage through the coordinator. The authorised supplement contains the original coordinator seed's lines 131–149, explicitly specifying Poisson parent streams emitting at most four points, plus singleton parents. The already supplied supplements expressly reuse that construction. This closes the narrow attribution issue.

For any such finite-rate Poisson superposition, the general argument in Section 4 gives finite fourth local moments, independently of internal geometry. Therefore retaining that cluster-size bound cannot yield S1 on the full fourth-order domain. This is a conditional structural conclusion about the stated model; it does not require acceptance of the seed's positivity estimates or its complete restricted-domain existence proof. Those complete seed proofs were neither supplied nor audited here.

## Finding register

| ID | Location | Precise mathematical issue or checked obligation | Consequence | Repair/status |
|---|---|---|---|---|
| P3-R01 | Exact claim; remaining obligations; submission lines 575–615 | No process satisfying the simultaneous S1 identities is constructed. | This submission does not pass S1. It is one unsuccessful exact-target construction submission with valid partial results. | Open target obligation. A later submission must supply an actual full construction or an independently proved broader obstruction. |
| P3-R02 | Theorem hypotheses, lines 41–78; limitations, lines 559–568 | The dichotomy depends on Poisson immigrants, iid reproduction and one fixed displacement density independent of the counts. The infinite-moment branch factors out the common kernel $H_4$. | The result excludes this subclass, not the whole Hawkes/branching approach or the general S1 class. It cannot authorise a target restriction. | Scope is correctly stated. Preserve these qualifiers in any summary or later use. |
| P3-R03 | Equations (10)–(14), submission Section 3 | Complete genealogies, ordered labels, integrated unobserved root, all immigrant partitions, extended products and singular-mass exclusion require verification. | An omitted allocation would invalidate use as full densities. | Checked and closed: the tree probabilities, unit Jacobian, ordered selections and all 15 fourth-order partitions are correct. |
| P3-R04 | Equations (15)–(22), submission Sections 4–5 | A finite fourth moment and an infinite fourth moment must be handled without silently narrowing the class; irregular $f$ must not defeat positive-measure positivity. | Merely proving divergence of a bounded-window integral would not contradict S1. | Checked and closed: the finite branch gives finite fourth count moments; the infinite branch gives an infinite density on positive measure and a direct submeasure contradiction. |
| P3-R05 | Submission lines 480–483 | The projection-simplicity sentence does not explicitly separate pairs of space-time roots, whose distinct space-time coordinates alone do not imply distinct spatial coordinates. | A small exposition omission in the projection argument, with no remaining mathematical gap after reconstruction. | Closed in this review by the Poisson second-factorial-measure null-set argument and countable exhaustion. Add that sentence for clarity. |
| P3-R06 | Submission lines 511–528 | The initial source packet showed restricted domains and low-intensity quantifiers, but not the asserted at-most-four-points parent law. | The source attribution initially lacked its exact cited passage; the core obstruction did not depend on it. | Closed by source supplement `review_proof_3_v01_source_01.json` and the verified cluster-law excerpt. No full-seed theorem approval is implied. |

No false mathematical statement or invalid consequential inference was found in the submitted theorem under its stated hypotheses. P3-R01 remains the substantive gap relative to the active target. P3-R02 is an essential scope boundary, not a defect to be removed by changing the theorem's wording.

## Amendment implications

The reviewed result proves that an S1 construction cannot belong to this fixed iid count-independent branching family. It also independently verifies the already relevant general fact that the full small-scale fourth reciprocal-volume law requires infinite fourth local count moments.

It does not prove that a lower altitude cutoff is necessary in S1's broader class, that a finite-fourth-moment assumption should be added, or that any restricted seed domain is sufficient at every prescribed intensity. It proves no need to change exactness, full-density interpretation, any order, or the independently prescribed pair $(\lambda_0,M)$.

Consequently **no target amendment is justified by this class-specific failure**. No amendment was proposed in submission 1. The separate owner-amendment checkpoint after three unsuccessful reviewed submissions has not been reached. S1 remains the acceptance target, and this report does not change the adopted statement or the original S0 verdict.

The supplied `nonexistence_2` global pair calculation is independently consistent with S0's negative status: on radius-$R$ balls, its prescribed second factorial moment scales as $R^5$, while the square of its positive mean scales as $R^6$. This is distinct from the present subclass theorem. I have not re-audited the unprovided global triangle or fourth-order arguments referenced in the amendment record, and do not use their previous approval labels in reaching this review's conclusions.

## Source and coding evidence

The proof is self-contained at the level of ordinary informal mathematical proof. Its dependencies are nonnegative integration, change of variables, elementary Poisson factorial identities, independent reproduction and elementary moment recurrences. Each consequential use has been reconstructed above. No specialised external theorem, historical attribution, literature-priority assertion or current-open-status claim is needed.

The frozen proof-reviser skill and both required references were read. The initial packet supplied the neutral context and primary-source index, but no primary PDF was needed as a mathematical dependency. The only additional source request was for the exact cluster-law passage; it has been answered and hash-verified:

- Supplement packet SHA-256: `231ccbb1107cfe6a201d1d6f76f9784fdce01735032fca3fadea2c85074b0c13`.
- `reviews/proof_3_v01/cited_seed_cluster_law.md` SHA-256: `1cb61df738cfdcc5bef547c206d08d1ae9bde1ac9ef067d0d2b4670961e6aaca`.
- Original seed source SHA-256, recorded in the supplement: `932923bd0632cabe575e4eb826744dfdd5e7c6c367cb1dd853c63d4a54ceb384`; exact source lines 131–149.

The initial excerpt hashes and their provenance remain in the initial review packet and `cited_seed_provenance.json`. No unavailable source passage remains essential to the verdict.

Executed scripts checked SHA-256 values and extracted only authorised runtime metadata. No simulation, numerical continuum check, symbolic-computation claim or formal proof-assistant certification is part of this review. The finite combinatorial partition and coefficient checks are explained mathematically above.

## Presentation judgement

The submission is readable and unusually explicit about the distinction between an exact-target pass and a useful obstruction. Its main mechanism is easy to recover: finite fourth offspring moments give too little local fourth-order mass, while an infinite fourth offspring moment combined with one fixed iid spatial law gives an infinite density on positive measure.

The full tree formula gives a reliable account of all genealogies without hiding unobserved ancestors. Its length is appropriate for establishing a full measure identity, although a final paper could put this expansion after the shorter direct-sibling obstruction, since the latter needs only a genuine submeasure and positivity.

Two small improvements would help:

1. Add the explicit space-time root-pair argument identified in P3-R05.
2. In brief summaries, retain “fixed iid offspring-count-independent spatial branching family” or an equivalent precise description. “The Hawkes/branching approach fails” on its own would overstate the theorem.

The source supplement need not be incorporated into the original frozen proof to preserve its content, but future versions should give an exact pointer to the parent-law passage when asserting the four-point bound. No mathematical rewriting is required to repair the accepted scoped theorem.

## Review summary and remaining obligations

The whole-space process exists with the claimed intensity for $m<1$. Its genealogical and immigrant-partition expansions give actual full extended densities and exclude singular mass. Finite fourth offspring moments imply finite fourth local moments. Infinite fourth offspring moments, with the fixed count-independent displacement law, instead make the direct-sibling density infinite on a positive-measure subset inside every small fourth-order domain. Both alternatives contradict the required fourth reciprocal-volume law. The specified finite-time Poisson space-time projection is also excluded by its finite fourth local moments.

The theorem is therefore accepted within its stated class. The original S1 construction question remains unresolved by this submission. Any subsequent construction must specify a law outside the excluded hypotheses, prove whole-space stationarity, simplicity and local finiteness at every independently prescribed $(\lambda_0,M)$, and obtain all three exact full densities globally without singular components. It must reconcile finite third local moments with infinite fourth local moments while keeping its fourth density finite almost everywhere. Finding one reciprocal-looking genealogical term is insufficient; all other contributions remain part of the target.

## Accounting and freeze

`preflight.json` records the actual session identity and the matching runtime `turn_context` model and effort before mathematics. Numeric runtime fields for input, cached input, cache-write input, output, reasoning output and total tokens are exposed. The separate `review_freeze.json` records the latest available checkpoint, the report hash, word count and freeze timestamp.

Reported token checkpoints cover the session prefix, not the still-unavailable completed-turn total. Reasoning output is not added to the inclusive output counter. No child agent was spawned. Parent/child aggregation semantics, final post-response usage and monetary charges are NR here; no estimate is substituted. The coordinator can reconcile completed-turn telemetry after this response. No raw private reasoning transcript was read, saved or requested.
