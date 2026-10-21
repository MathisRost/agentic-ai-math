# Review — proof_4 submission 3 of 4 against S1

- Type: fresh independent extensive audit of the entire submission and its consequential frozen dependencies. Previous concrete issue tables were checks to revisit, not mathematical authority.
- Reviewer: `/root/review_proof_4_v03`, thread `session-20`, turn `turn-32`.
- Actual runtime: `gpt-6-astra`, effort `xhigh`, verified before mathematics in own rollout `turn_context`, line 8. Own `session_meta`, line 1, identifies this reviewer and thread. Rollout: `[local path omitted]`.
- Runtime session start: `2026-10-20T18:31:24.181Z`. Preflight, timestamped usage evidence and scope are saved in `accounting_capability.json`; the final available checkpoint and freeze time are recorded separately. Only allowlisted own metadata and numeric token fields were extracted.
- Setup root: `$SETUP`; run root: its `runs/20261020T164437Z_astra6/` directory.
- Active statement: `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Current proof: `reviews/proof_4_v03/proof_snapshot.md`, SHA-256 `11cb3a169173b26dd8d9b8b0ef734bd375632adcd1468337c4c9b4612f26ad29`.
- Main dispatch: `packets/review_proof_4_v03.json`, SHA-256 `ffa33ddf5542fb5e27008300426f75cbb2578aa43de42766945eb8357996f868`.
- Scope-only proposal supplement: `packets/review_proof_4_v03_proposal_01.json`, SHA-256 `3cc830b55d32d17a99966ace0a0850fec86ca32ffba054c5bb403d12d99caacb`.
- Frozen dependencies: v01 `57b1c58f13fa055c76cfec22c131b989b32bef3b1414cd710992ad6f081158b5`; v02 `9a3befd21f85424fea521c9c817837f2d943a1a0862c0e1586541b93c5d559ac`.
- All 29 dispatched packet/content hash comparisons matched. Exact paths, expected hashes and actual hashes appear in `input_hash_verification.json`.
- Received: the assigned governing and accounting documents, workflow, target history, proof-reviser skill and complete mandatory proof/style references, the three frozen mathematical submissions, two concrete issue lists, the two specifically cited seed passages and provenance, and the two formal proposal files. Excluded: author conversation and private work, other tracks, full previous reviews, unassigned seed material, old runs and other chats. No delegation occurred. Only the assigned review directory was written.

## Correctness verdict and scope

**Submission 3 does not pass S1. It gives valid partial progress and valid obstructions within explicitly restricted representations. The all-intensity existence question remains unresolved.** The inherited whole-space construction proves all three exact full-density identities when
\[
0<\lambda M^3\leq\tau,
\qquad
\tau=\min\left\{\frac1{36e\pi},\frac{J^2}{8\pi^2Z_0},
\sqrt{\frac{J^3}{32\pi^4Z_0^2}}\right\},
\quad J=\frac{\pi^2}{4},\quad Z_0=\frac{\pi^2}{4}+\frac{2\pi}{3}.
\]
S1 requires every independently prescribed positive pair $(\lambda,M)$. No process for the omitted range, and no general obstruction to that range, is established here. Dilation preserves $\lambda M^3$ and cannot close this gap.

The new Theorem 1, Theorem 2, Theorem 3 and Proposition 4 are supported by their proofs, with the scopes explained below. In particular:

- Any process satisfying S1 has finite third moments on every bounded set and infinite fourth moments in every nonempty ball. These are compatible conclusions, with no additional moment hypothesis on S1.
- The independent-superposition obstructions are valid for their stated component classes.
- The slab mixture with an arbitrary finite-fourth-moment correction has the stated necessary ceiling $\lambda M^3\leq18/\pi$. This is not a general S1 ceiling.
- The residual functions can be made nonnegative for every parameter pair. Their joint realisation as full factorial densities of an actual process is unproved. The author explicitly distinguishes these two claims.

I found no new invalid inference in these stated theorems or the inherited restricted construction. This is an informal mathematical audit, not a proof-assistant certificate. The proposed S2 was examined only for its precise loss of scope and evidence. It remains unapproved and inactive; this review does not enact it or reset the four-submission allowance.

## Reconstruction and detailed audit

### 1. The target and the dependency structure

The active target requires one stationary, simple, almost surely locally finite process on all of $\mathbb R^3$, prescribed homogeneous intensity, and full factorial measures of orders two through four with globally finite-almost-everywhere densities. The reciprocal formulas are prescribed on every nondegenerate configuration of diameter less than $M$. Absolute continuity is required everywhere, including degenerate configurations and regions outside these formula domains. A formal local hierarchy is therefore insufficient even if every displayed function is nonnegative.

The current proof has three logically separate parts. The v01 slab law supplies a genuine exact-fourth process, its global regularity and its lower coalescence behaviour. The v02 separated-cluster mixture supplies the existing simultaneous construction in the stated small parameter range. The new v03 arguments prove moment consequences, rule out specified ways of extending that construction, and derive a different formal hierarchy. The new obstructions do not replace the missing existence argument.

I reconstructed the consequential v01 and v02 mathematics from their frozen texts. Their previous review labels played no role in these deductions. The supplied S0-to-S1 amendment identifies the active target and historical authority; the other tracks' underlying obstruction proofs were not assigned and have not been re-audited here. None of the new S1 deductions depends on importing an unproved assertion from them.

### 2. Inherited slab law: probability law, exact density and global regularity

The v01 law, and its v02 scaled form, sample one random vector $W$ and one phase, then a Poisson process conditional on the resulting bounded-in-space intensity field. In the scaled notation,
\[
H_M(v)=1+M^2|v|^2,\quad T_M(v)=2+2M|v|,
\quad Z_M=M^{-3}Z_0,
\]
\[
p_M(v)=\frac{T_M(v)}{Z_MH_M(v)^4},\qquad
\Lambda(x)=sH_M(W)\sum_{k\in\mathbb Z}
\mathbf1_{[-1/2,1/2)}(W\cdot x-B-kT_M(W)).
\]
The substitution $w=Mv$ and the radial integrals in v01 give
\[
\int\frac{T_M}{H_M^4}=M^{-3}Z_0,
\qquad \int H_M^{-3}=M^{-3}J.
\]
Thus the mark law is normalised, and averaging the uniform phase gives intensity $sJ/Z_0$. The conditional intensity is at most $sH_M(W)<\infty$ for every realised mark. Conditional Poisson sampling supplies a measurable whole-space law, simplicity and local finiteness. Phase invariance proves translation invariance; radial mark dependence also proves isotropy. The choice $s=\lambda Z_0/J$ gives the required component intensity.

The conditional Poisson factorial identity and Tonelli establish, for every nonnegative tuple test, the full measure identity with density $\mathbb E\prod_i\Lambda(x_i)$. This argument excludes singular mass before any restriction to nondegenerate configurations. It remains valid when a fourth moment is infinite.

The all-allocation formula in v01 (9) is obtained by expanding every slab index, absorbing the first index into the phase integral and retaining every relative index $m\in\mathbb Z^{n-1}$. Below diameter $M$, a nonzero relative index forces an indicator-argument difference at least
\[
T_M(v)-|v|\,|x_i-x_1|=2+(2M-|x_i-x_1|)|v|\geq2,
\]
whereas two arguments in the unit interval differ by less than one. Thus only the zero relative index remains on the local domain. The corrected non-strict inequality includes $v=0$ and resolves the old endpoint slip.

For four affinely independent points the affine map from $(v,b)$ to their four slab coordinates has absolute determinant $6V$. At order four the amplitude power cancels the mark-density weight, and the four indicator integrals have total integral one. This gives $s^4/(6Z_MV)$ with the correct ordered-tuple convention. No factorial coefficient is missing.

Global finite-almost-everywhere regularity needs more than this local calculation. In v01, write $U$ for the matrix of the three relative vertex rows and $L=2M$ for the period coefficient in the unscaled construction. The support condition bounds every index $m_i$ by $\max\{R/L,1/2\}$, where $R$ is the largest row norm. Only finitely many indices contribute at a fixed nondegenerate quadruple. For each index the support satisfies
\[
|v-L|v|U^{-1}m|\leq K(U,m),
\qquad
|v|\,|1-L|U^{-1}m||\leq K(U,m).
\]
Except when $L|U^{-1}m|=1$, this bounds $v$; the phase coordinate is also bounded. The fourth integral is then finite. For fixed nonzero $m$, the exceptional condition is the zero set of
\[
L^2|\operatorname{adj}(U)m|^2-(\det U)^2,
\]
a nonzero polynomial, as the substitution $U=tI$ verifies. The countable union of these zero sets and the affine-dependence set is null. Scaling transfers this result to $H_M$. This is a valid global proof, not an extrapolation of the local formula. Null-set reassignment does not add a singular component; the prior full measure identity already precludes one. A local resonance would force every integer $m_i$ to have magnitude less than $M/L<1$, hence $m=0$, which cannot resonate.

The third moment calculation is also valid: a bounded ball intersects only a bounded number of slabs, each of physical width $1/|W|$. Its conditional Poisson mean is $O(1+|W|)$, and the radial mark density is $O(r^{-5})$. Consequently its third moment is finite. Countable exhaustion gives finite-almost-everywhere lower densities globally. The fourth moment divergence is checked independently below.

Finally, integration over the two free normal coordinates at order two yields the factor $\pi/[M^2(1+M^2\beta^2)]$; integration over the one free coordinate at order three yields $\pi/[M\sqrt{1+M^2|v_0|^2}]$. Together with $Z_M=M^{-3}Z_0$, these give precisely the current $c_2=\pi s^2M/Z_0$ and $c_3=\pi s^3M^2/(2Z_0)$. Thus the inherited lower formulas and constants are correct. Their nonconstant factors explain why this slab law alone never met both lower reciprocal identities.

The v01 broader radial-slab proposition is also sound with the explicitly repaired convention that the density at $d_0$ is the canonical expected-product/integral version. Its dominating function is $\omega(r)d_0H(d_0r)$, because $dH(dr)$ is nondecreasing in $d$ and tends to zero as $d\downarrow0$. One cannot instead use an arbitrarily reassigned Radon–Nikodym value on a null distance sphere. The current proof maintains this distinction.

### 3. Inherited simultaneous construction and its exact parameter range

I rechecked v02 Sections 3–5, since both the current retained theorem and the proposed amendment depend on them. The geometric marginal bound is
\[
\mathcal M K_3\leq B_3K_2,
\quad I_2=2\pi M^2,\quad B_3=2\pi^2M^2.
\]
It follows by enlarging the third-vertex region to the ball of radius $M$ centred at the first vertex and integrating inverse distance to the pair line. All integrals are nonnegative, and the anchored integrals are finite.

With
\[
a_2=\frac{\lambda}{8\pi M^2},\qquad
a_3=\frac{\lambda}{64\pi^3M^4},
\]
the second and third bounds defining $\tau$ give $c_2\leq a_2$ and $c_3\leq a_3$. Hence $q_j=2a_jK_j-\mathbf1_{E_j}r_j$ satisfy
\[
a_jK_j\leq q_j\leq2a_jK_j,
\qquad F_3=q_3,\quad F_2=q_2-\mathcal Mq_3\geq\tfrac12a_2K_2.
\]
The subtraction is between finite anchored integrals, and positivity is proved before any probability density is defined.

The actual correction law starts with Poisson centres of intensity $\eta=(36\pi M^3)^{-1}$ and retains isolated centres at separation greater than $3M$. The Poisson insertion/void calculation gives retained intensity
\[
\kappa=\eta e^{-\eta36\pi M^3}=(36e\pi M^3)^{-1}.
\]
The first bound in $\tau$ gives $\lambda\leq\kappa$. The probabilities for sizes zero through three in v02 (22) are nonnegative and sum to one: $Z_2=Q_2-Q_3>0$, $Z_3=Q_3>0$, $\beta=\lambda-Q_2+Q_3/2>0$, and
\[
\beta+Z_2/2+Z_3/6=\lambda-Q_2/2+Q_3/6\leq\lambda\leq\kappa.
\]
Offsets use the normalised densities $F_j(0,\cdot)/Z_j$. They remain within $M$ of the centre. Thus any two different clusters are more than $M$ apart, and every local eligible tuple belongs to one cluster.

The ordered selection factor $j!/(j-k)!$ is justified by symmetry and a unit-Jacobian change of root. In particular, $2\kappa p_2/Z_2=1$ and $6\kappa p_3/Z_3=1$, giving exactly
\[
\rho_C^{(2)}=F_2+\mathcal MF_3=q_2,
\quad\rho_C^{(3)}=F_3=q_3,
\quad\rho_C^{(4)}=0
\]
on the appropriate local domains. The intensity is $\beta+Z_2+Z_3/2=\lambda$.

Dependent retained centres do not cause an independence gap. Only their first intensity enters this local same-cluster calculation. For global regularity, assign the same independent marks to all original Poisson centres before thinning. The correction process is a subset of this unthinned process. Its full factorial density is obtained by summing over all parent partitions; v02 (25)–(26) include them all. Every bounded observation count is bounded by three times a Poisson count in its $M$ enlargement, so it has every finite local moment. Domination then proves full absolute continuity and finite-almost-everywhere densities for the correction at every required order, including outside the formula domains. It also proves almost-sure local finiteness; diffuse offsets and centres prove simplicity.

The final law is a half-and-half choice of these two whole-space laws. The full factorial measures combine linearly, rather than acquiring superposition cross terms. This gives the two corrected densities and $a_4=s^4M^3/(12Z_0)>0$. Global regularity and finite third moments pass to the mixture; infinite fourth moments persist with positive mixture probability. This establishes every retained geometric and measure requirement on $\lambda M^3\leq\tau$, including the endpoint. It establishes no further parameter range.

I also rechecked v02's smaller-class obstruction. Separation and cluster size at most three imply the third-extension inequality over the entire lens $B(0,M)\cap B(de,M)$. Multiplication by $d$ and dominated convergence give the coefficient restriction $a_2\geq2\pi^2M^2a_3$. The two slab terms vanish in this limit. The subsequent count inequality proves the stated ceiling $18/\pi$ (not asserted to be sharp). The stronger coefficient restriction in that older, narrower theorem is not automatically inherited by the broader v03 correction class.

### 4. New Theorem 1: lower moments and a necessary coefficient inequality

Current lines 49–65 prove the sharp ball/line integral bound. A slice of a ball perpendicular to the line is a disk, and layer-cake bounds its inverse-distance integral by $2\pi R$ regardless of the line's offset. Integration over slices gives
\[
\int_{B(c,r)}\operatorname{dist}(z,\ell)^{-1}\,dz\leq\pi^2r^2,
\]
with equality for a central line. The proof uses only nonnegative integrals and is valid at the integrable line singularity. Since $A(x,y,z)=D(x,y)\operatorname{dist}(z,\ell_{xy})/2$, the factor $2\pi^2r^2/D$ is correct.

For a ball of radius $r<M/2$, full absolute continuity and the target formulas yield finite $f_2$ and $f_3$ with
\[
0<f_2<\infty,
\qquad f_3\leq q_rf_2,
\quad q_r=2\pi^2r^2a_3/a_2.
\]
Degenerate triples cannot carry extra mass. The identity $N^3=(N)_3+3(N)_2+N$ proves the raw third moment is finite. Finite covering and $(\sum_iN_i)^3\leq k^2\sum_iN_i^3$ extend this conclusion to every bounded set; no formula outside $E_n(M)$ is used.

Cauchy–Schwarz with $\sqrt N$ and $\sqrt N(N-1)$ gives $f_2^2\leq\mu(f_3+f_2)$; the second moment is $f_2+\mu$. Both steps use established finite moments, and division by $f_2$ and $\mu$ is justified by positivity. Thus $\mu\leq2+q_r$. Taking the deterministic limit $r\uparrow M/2$ gives exactly
\[
\lambda\pi M^3/6\leq2+(a_3/a_2)\pi^2M^2/2.
\]
This imposes no universal ceiling while the coefficient ratio remains free. The theorem in fact only needs homogeneous intensity, not stationarity, as its statement correctly allows.

### 5. Reciprocal-volume divergence and new superposition obstructions

Current Section 2 gives a valid positive-measure family of base triangles whose areas stay bounded above and away from zero, with an interior fourth-vertex planar disk and uniform short normal interval. The fourth-vertex coordinate map is orthonormal with Jacobian one; $V=A|h|/3$. The integral over nonzero normal heights is a positive multiple of $\int_0^\varepsilon dh/h$, hence infinite. Tonelli over the base neighbourhoods proves infinite fourth factorial mass in any small nonempty ball. Coincidence and exact-coplanarity sets are null, so removing them does not remove this divergence. A smaller ball proves the assertion for every nonempty ball. This is a fourth-moment obstruction, not a contradiction to almost-sure finite counts.

Theorem 2 first ensures that independent diffuse-intensity processes have no common points. The expected cross-count on a bounded spatial diagonal is zero under the product of their first measures; countable exhaustion makes this global. Their union is simple and locally finite.

At order four, allocation by component gives all $2^4$ subsets. Removing the two pure allocations leaves 14 mixed terms: four $3+1$, six $2+2$ and four $1+3$. In part (a), keep the pure $C$ term with the mixed terms to form $Q$. All its masses on bounded product balls are finite by the assumed third moments of $Y$ and fourth moments of $C$. If the resulting union satisfies the required full absolute continuity, $C$'s needed absolute continuity follows by domination, even if it was not separately assumed.

On $E_4(M)$, equality of finite pointwise densities gives $q=(a-b)/V$. Nonnegativity excludes $a<b$, and the preceding divergence excludes $a>b$. With $a=b$, absolute continuity implies $Q(B^4)=0$ for a ball of diameter less than $M$: its exceptional configurations form a null set. Yet the mixed $3+1$ terms contribute
\[
4\mathbb E(Y(B))_3\,\mathbb EC(B)>0.
\]
The first factor is finite by hypothesis and strictly positive because the fourth factorial moment of $Y(B)$ is infinite, forcing positive probability of at least four points. The second is positive by homogeneous positive intensity. This is a contradiction. No infinite measure masses have been subtracted.

In part (b) both pure fourth measures are retained, and the finite mixed density is $(a-b-c)/V$. The same argument forces $a=b+c$ and then contradicts the positive mixed allocations. Theorem 1 supplies the third-moment hypothesis whenever both components are S1 solutions. These are sound restrictions on independent superposition; they do not exclude dependent modifications or a base whose fourth density already includes other terms.

### 6. New Theorem 3: arbitrary finite-fourth-moment corrections

The two endpoints of the mixture parameter are excluded for valid reasons: a pure finite-fourth-moment law contradicts the local volume singularity, and the pure slab law has $dr_2(d)\to0$ rather than a positive constant. For $0<\theta<1$, domination transfers full absolute continuity to $C$.

The full mixture identity gives
\[
(1-\theta)\rho_C^{(4)}=(a_4-\theta b)/V
\]
on the local domain. Nonnegativity and finite fourth moments force $a_4=\theta b$ and zero correction density there. Global absolute continuity is essential to the next step: it also rules out mass on coplanar quadruples. Counting ordered quadruples in bounded windows and then exhausting space proves that, almost surely, $C$ has no four distinct points of diameter less than $M$.

For fixed $R<M/2$ and a pair with separation $d<M-R$, two other correction points in $B(x,R)$ would create such a quadruple; all six distances are strictly below $M$. Therefore there is at most one extension in this ball. Integration against arbitrary nonnegative pair tests proves the density inequality (27) for almost every pair. This is a measure argument and makes no pointwise assertion about exceptional pairs.

The target expressions and canonical slab expressions are translation invariant and radial in the pair separation. Fubini in the translation coordinate and polar coordinates therefore turn the inequality into an almost-everywhere statement in $d$. The central-line integral equals $2\pi^2R^2/d$ exactly. The limits of the slab terms follow from dominated convergence: the phase bound $|v_0|\geq|q_2-q_1|/d$ makes $\Psi_M(de,z)\to0$, while the spatial bound $2c_3/|z_\perp|$ is integrable on the ball. Taking a sequence from the full-measure set of valid distances is sufficient. There is no assumption that a general Radon–Nikodym version agrees along a chosen ray.

The resulting inequality is $2\pi^2R^2a_3\leq a_2$. Letting $R\uparrow M/2$ gives the stated bound $(a_3/a_2)\pi^2M^2/2\leq1$. Theorem 1 then yields $\lambda M^3\leq18/\pi$.

The representation restriction is consequential. The theorem imposes finite fourth moments on the auxiliary law, not on $X$ or on the general S1 class. It includes the earlier separated finite-cluster corrections, and it covers other possible corrections as well. It is broader for S1 mixture applications, but it is not a literal strengthening of every hypothesis of v02 Theorem 2: the older theorem needed only the lower two laws and its cluster geometry, whereas the new theorem uses the fourth law to force the no-quadruple property. Its coefficient inequality is correspondingly weaker. The stated common ceiling remains valid in both settings.

### 7. Proposition 4: exact inversion, nonnegativity and the unresolved realisation

For an actual independent union with a Poisson process of intensity $\nu$, the full factorial density is the subset sum in (30), including $\rho^{(0)}=1$ and $\rho^{(1)}=\lambda-\nu$. Subset convolution with the powers of $-\nu$ is its inverse, since the coefficient of a fixed subtuple is the binomial sum $(\nu-\nu)^{n-|J|}$. Thus the coefficients and signs in (31)–(33) are correct: three pair terms and three intensity terms at order three, then four face terms, six pair terms and four intensity terms at order four. All faces of a nondegenerate simplex are nondegenerate and have smaller diameter. Pulling lower-dimensional almost-everywhere equalities back to a bounded higher-dimensional product preserves nullity by Fubini, so this use of face formulas is legitimate.

The positivity choices are sufficient. For $D<M$, (34) gives nonnegative $r_2$. Every triangle altitude is below $M$, so $A\sum D_{ij}^{-1}\leq3M/2$, proving the asserted domination in $r_3$. Every tetrahedral altitude is below $M$, so $V\sum A_I^{-1}\leq4M/3$. Hadamard's determinant inequality gives $V\leq M^3/6$. Multiplying $r_4$ by $V$ therefore shows that (36) dominates both negative contributions; its pair contribution is nonnegative. The remaining constants have the stated signs because $0<\nu<\lambda$. All choices are finite and can be made successively for every positive parameter pair.

The integrability claims also hold. The inverse-distance and inverse-area kernels are integrable on bounded products; inverse area follows from the ball/line estimate already proved, and unused coordinates add only finite volume factors. Hence $r_4-a_4/V$ is integrable on every sufficiently small product ball. Adding this finite-mass signed correction cannot remove the infinite integral of $a_4/V$; the nonnegative candidate $r_4$ still has infinite fourth mass there.

This does not construct $Y_*$. Positivity of each prescribed density is only one necessary condition on a factorial moment hierarchy. The submitted argument supplies no consistent joint laws for counts, no whole-space law, and no global extension with finite-almost-everywhere full densities outside the local domains. There is no unverified realisability theorem silently filling this gap. If an actual law with all those properties were supplied, the independent Poisson union would indeed give S1; component absolute continuity and finite-almost-everywhere densities would pass through the finite allocation sum. That conditional statement is correct, but its antecedent is the main open obligation.

## Finding register

| ID | Location | Precise mathematical issue or verified finding | Consequence | Repair/status |
|---|---|---|---|---|
| P4v03-01 | Current lines 21–30, 412–416; inherited v02 Theorem 1 | The actual simultaneous construction remains restricted to $\lambda M^3\leq\tau$; S1 requires every positive pair. | Third submission is unsuccessful as an S1 attempt, with valid partial progress. | Open. Supply an all-parameter construction or a general obstruction; a different target requires its own valid adoption. |
| P4v03-02 | Current Section 1, especially (3)–(8) | The ball/line bound, finite-cover argument and count Cauchy–Schwarz prove finite third moments and the coefficient inequality. | No hidden third-moment assumption is needed for later S1 applications. No universal intensity ceiling follows alone. | Verified. |
| P4v03-03 | Current Section 2, (9) | The reciprocal-volume integral diverges on a positive-measure family of almost-coplanar configurations. | Every S1 solution has infinite fourth moment in each nonempty ball; the finite-fourth comparison subclass is impossible. | Verified; do not confuse this with failure of almost-sure local finiteness. |
| P4v03-04 | Current Theorem 2, (11)–(15) | All 14 mixed allocations are included and locally integrable; they cannot be a nonzero multiple of $1/V$ and cannot all vanish. | Both stated independent-superposition procedures are excluded. | Verified within the stated component and independence hypotheses. |
| P4v03-05 | Current Section 4, (16)–(22); inherited v01 Sections 2–7 | The actual slab law, affine determinant, global resonance argument, lower constants and canonical coalescence limits are valid. | The new mixture theorem rests on a genuine law with full global densities, not a local formal formula. | Independently re-established; old canonical-version and endpoint corrections maintained. |
| P4v03-06 | Current Theorem 3, (25)–(28) | Finite fourth correction moments force no local quadruples only after full absolute continuity excludes coplanar singular mass. | The local extension inequality is valid for an arbitrary correction in this class. | Verified; full measure regularity is essential. |
| P4v03-07 | Current Theorem 3, (24), (28); line 40 comparison with v02 | The a.e.-distance argument and two dominated-convergence limits prove the ceiling $18/\pi$. The new theorem uses the fourth law, unlike the older narrower theorem. | A broader correction class is excluded for S1 mixture applications, not arbitrary S1 processes or all lower-law mixtures. | Verified. Optional presentation clarification: explicitly retain this distinction when describing the extension of v02. |
| P4v03-08 | Current Proposition 4, (30)–(38) | Subset inversion, all coefficients, signs and geometric positivity bounds are correct for every parameter pair. | Establishes nonnegative candidate functions and their stated local integrability. | Verified analytic result only. |
| P4v03-09 | Current lines 408–410 | No actual process realises the residual hierarchy; joint count consistency and global measure extension are unproved. | Proposition 4 cannot supply an S1 construction. | Open and accurately disclosed; positivity alone is no repair. |
| P4v03-10 | Inherited v02 Sections 3–5; current (1) | The residual kernels, mark probabilities, retained-centre intensity, ordered factors, global domination and whole-law mixing all check. | All three identities and global process requirements are simultaneously proved on the stated range. | Verified; prior pair and triangle failures repaired only on this range. |
| P4v03-11 | Current lines 199, 420; old issue R4-09 | Exact prior mathematical sections now replace approval labels as the cited dependencies. | The inherited argument is identifiable and auditable. | Presentation issue closed; dependent mathematics rechecked here. |
| P4v03-12 | Formal proposal, lines 11–15 and 126–158; complete proposed statement | The sole substantive target weakening is restriction to $\lambda M^3\leq\tau$. No general theorem proves this restriction necessary. | Proposal is precise and supported as a sufficient-range choice, but does not change S1 or turn this attempt into a pass. | Scope audit passed; owner decision absent. No adoption, broadcast or counter reset authorised by this review. |

## Amendment implications

The scope-only supplement contains two frozen formal files:

- `proposals/proof_4_v03_conditional_statement_change.md`, SHA-256 `2bcd9289fd84e2506dd7b682368bf5f6bb7e0bcb6d41816ae7055a3832ba81c9`.
- `proposals/proof_4_v03_S2_proposed.md`, SHA-256 `21cf343bc5d702a17e6e41cd10c3bf6482e7e1fec541a20ff60bc5e58c29f62b`.

I checked the complete proposed statement against S1 and verified that its embedded copy in the change proposal is textually identical. The mathematical weakening is precisely the restriction of the quantified parameter pairs to $\lambda_0M^3\leq\tau$. At fixed $M$ it abandons arbitrary intensity; at fixed intensity it abandons arbitrary $M$. It retains exact prescribed intensity within the range, all three full factorial identities, all smaller nondegenerate shapes, the entire-space law, stationarity, simplicity, almost-sure local finiteness, global finite-almost-everywhere densities and absence of singular mass. It adds no finite-fourth-moment condition or representation restriction. The remaining wording changes concern acceptance and historical status.

The inherited v02 theorem, independently reconstructed above, proves the mathematical existence claim on this proposed range. This is support for a possible owner choice, not evidence that the restriction is necessary, optimal or maximal. In particular, the representation-specific ceiling $18/\pi$ is not a proved sufficient range, and neither it nor three unsuccessful submissions justifies a coordinator-led general-obstruction amendment. The general moment consequences prove no restriction of the form $\lambda M^3\leq\tau$.

The proposal accurately presents the alternatives: retain S1 and use the last submission on its open obligation, or retain the partial theorem without changing the target; a different weaker target would need its own precise statement and authority. This review completes the third unsuccessful exact-S1 assessment. The coordinator may now consider the optional owner checkpoint under the governing workflow, but the reviewer neither sends that question nor approves the amendment. Until an explicit owner decision is recorded, hashed and broadcast through the required adoption procedure, S1 remains active. Three of four submissions are used, one remains, and there is no reset. Earlier S0 and S1 verdicts remain separate from any future target.

## Source and coding evidence

The mathematical proof was audited from the three assigned frozen submissions. Exact consequential locations are v01 Argument Sections 2–8; v02 Argument Sections 2–6; and every mathematical section of v03. The two earlier issue lists were read and each consequential issue was rechecked independently.

The specifically assigned seed Section 5 is a diagnostic Poisson shot-noise example whose reciprocal-volume expression is a fourth factorial cumulant. Its warning about additional full-density partition contributions is consistent with the submitted use: v01 takes an affine determinant lead and then proves a different full-density law directly. No seed cumulant identity is treated as a full density. The assigned seed Section 2 concerns a pair/triangle residual construction with abbreviated references to other definitions. Those omitted definitions are not needed here because v02 rederives its own kernels, normalisations, probability law and partition identities in full. No theorem is imported from that abbreviated passage to realise the new residual hierarchy.

The common README, S0/S1 statement history, DVJ context and primary-source index were read as assigned. No published specialised theorem, claim of novelty, current open-status assertion or precise bibliographic attribution is required for the audited constructions and obstructions. The proof uses elementary Poisson factorial/void identities with their needed forms justified in the submissions, conditional expectation, Tonelli, dominated convergence, layer-cake integration, Cauchy–Schwarz, linear changes of variables, polynomial null sets and determinant geometry. Their hypotheses have been matched in the audit above. No primary PDF was consulted and no claim of primary-source verification is made. No source gap remains necessary for the supported conclusions, so no literature request was needed.

Executed programmatic checks were administrative: hashes, own runtime/accounting metadata, exact proposal embedding, and the S1/proposed-statement textual difference. No numerical experiment, simulation, symbolic package or formal verifier was used to certify the mathematics. No coding request was needed. The review preserves all supplied snapshots and does not modify any author file.

## Presentation judgement

The current submission is readable and unusually explicit about its limited conclusion. Its separation of actual laws, representation obstructions and formal residual functions makes the status recoverable without relying on a prior verdict. The a.e.-distance explanation, the no-singular-mass step in Theorem 3, and the avoidance of infinite-measure subtraction are useful and correct clarifications.

For a standalone presentation, include the retained slab and restricted-mixture proofs as identified appendices rather than relying on multiple version names. Also describe Theorem 3 as broadening the correction class for S1 applications while using the fourth law; it should not be summarised as strengthening all hypotheses of the earlier lower-order theorem. These are exposition improvements, not unresolved proof defects in the stated results. Preserve the prominent warning that residual nonnegativity does not prove realisability.

## Review summary and repairs

The decisive inherited check is that the small-parameter theorem is an actual whole-space process construction with all allocations and global full measure regularity. The decisive new check is that a locally finite correction measure cannot contribute a nonzero multiple of the nonintegrable reciprocal-volume density. This proves the new superposition obstructions and forces a finite-fourth-moment mixture correction to have no local quadruples. The resulting coalescence argument and count inequalities correctly give the scoped ceiling.

The remaining mathematical obligations are explicit:

1. Establish or refute S1 for parameter pairs outside the proved range, without adding a representation or moment assumption to the general target.
2. If the independent-Poisson route is pursued, construct an actual stationary simple locally finite $Y_*$ with the stated intensity and joint full densities, including consistent count laws and global finite-almost-everywhere extensions. The residual functions and their positivity do not discharge this obligation.
3. Do not replace either obligation by a claim that the finite-moment mixture ceiling is a universal obstruction, or that a proposed target has already been adopted.

No repair is required for the correctness of the stated new scoped results or the inherited restricted theorem. A substantive new argument is required for an S1 pass. This is the third unsuccessful exact-target submission, with valid partial progress; it is not a proof that S1 is false. The scope audit finds the conditional amendment precise, but approval remains absent.

## Accounting

Own token-count events expose input, cached input, cache-write input, output, reasoning output and total usage. Cumulative checkpoints are not summed. Reported total tokens equal input plus output, so reasoning output is not added again. No children were spawned; this report does not infer the coordinator's child-aggregation semantics. The ledger in `accounting.jsonl` records the latest observed cumulative prefix, source event, coverage and missing tail. Completed-turn usage after the final response is NR pending coordinator reconciliation. Monetary estimates, pricing/tier evidence and actual charges are NR; no estimate is presented as measured usage. This report records proofs and concise decisions, not private chain-of-thought.
