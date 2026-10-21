# Research and decision summary

This document records explicit proof ideas, conclusions and decisions. It is not a private deliberation transcript. The frozen proofs and extensive independent reviews are the mathematical record; this summary does not replace them.

## Target outcomes

**S0 is false at every positive prescribed intensity.** Two independent investigators began with the unrestricted exact statement, without construction seeds or each other's work. Separate fresh reviewers accepted their general obstructions. A further independently reviewed submission established the global fourth-order obstruction before the common finite-diameter revision was adopted.

**S1 is proved by the investigator-choice fourth submission, accepted by its fresh individual reviewer and the fresh final synthesis.** It establishes the complete unchanged statement for every independently prescribed positive intensity and diameter bound. The actual whole-space process has all three exact full identities and the required global measure regularity. Fresh review `reviews/proof_4_v04/review.md` (SHA-256 `680b32c05642871d0207ffe59e4bc04d65d6a3bca26a06d61d96e60a2d031e7c`) found no blocking mathematical gap. This is an informal proof review, not formal machine verification.

S1 requires
\[
\rho^{(2)}=\frac{a_2}{D},\qquad
\rho^{(3)}=\frac{a_3}{A},\qquad
\rho^{(4)}=\frac{a_4}{V}
\]
almost everywhere on the respective nondegenerate configurations of diameter below \(M\), for finite positive configuration-independent coefficients. The process is stationary, simple and almost surely locally finite on all of \(\mathbb R^3\), with prescribed mean intensity \(\lambda_0\). Globally, its full factorial expectation measures must have densities finite almost everywhere and no singular component. There are no lower geometric cutoffs or fourth-moment assumptions. Ergodicity and mixing are not required.

The move from S0 to S1 used reviewed general obstructions and the owner's advance authorisation for domain revisions. A common upper diameter cap was a non-unique operational choice; the obstruction did not prove this particular repair necessary, maximal or sufficient. No construction-specific obstruction was promoted into a general restriction.

The separate S2 proposal would restrict \(\lambda_0M^3\) to an explicit sufficient low-intensity range. It was proposed only after three unsuccessful independently reviewed submissions. No owner approval has been received, S2 has never been adopted, and no attempt count has reset. The owner-approved early closure of the Cox track is a separate administrative decision.

## Why the unrestricted statement fails

The full reciprocal pair law on all scales gives
\[
\mathbb E(N(B_R))_2
=a_2\int_{B_R^2}|x-y|^{-1}\,dx\,dy
=O(R^5).
\]
The pair integral itself is finite. Stationary positive intensity gives
\(\mathbb EN(B_R)=\lambda_0|B_R|\), so variance nonnegativity requires
\(\mathbb E(N(B_R))_2\geq(\mathbb EN(B_R))^2-\mathbb EN(B_R)
=\Theta(R^6)\). These growth rates contradict each other as \(R\) increases. No mixing or finite fourth moment is used.

The global investigator also proved a reciprocal pair-tail obstruction allowing arbitrary short-range behaviour, and a global reciprocal-area obstruction. Its second submission supplies a fourth-order-only tail obstruction using bounded occupancy indicators and nondegenerate quadruples, avoiding any finite fourth-moment premise. Thus weakening the large-configuration fourth law was supported by a general theorem, rather than inferred from the local moment divergence.

Locally, reciprocal distance and reciprocal triangle area are integrable on bounded configuration domains. Reciprocal tetrahedral volume is not: near a planar configuration with separated vertices and nonzero faces, \(V=A_{\rm base}|h|/3\), and integration in the fourth vertex's normal height contains \(\int dh/|h|\). Any S1 solution therefore has finite third moments on bounded sets and infinite fourth moments on every nonempty open ball. Infinite expectation is consistent with almost-sure finite counts. The local investigator provided an explicit example demonstrating that distinction before construction work began.

## The final investigator-choice construction

The frozen proof is `tracks/proof_4/submissions/v04.md`. It gives two actual stationary processes and chooses between their entire laws with a fair coin. This is a single probability law, so its full factorial measures are the averages of the two alternatives' full measures.

The first alternative \(Y\) is a Cox process on randomly retained spherical surfaces. A global random radius-band selection, uniformly translated centre lattice, uniformly shifted radial grid, and independent retention marks produce a prescribed first intensity of sphere centres and radii. Distinct surfaces are farther apart than \(M\). Conditional on the surfaces, independent Poisson samples use diffuse surface intensities. A local tuple of diameter below \(M\) must therefore lie on one sphere.

Four affinely independent points determine their sphere uniquely. The sphere-incidence Jacobian gives the exact full local fourth density \(c/(48V)\). The two lower coarea integrals give
\[
r_2(D)=\frac{A_2}{D}e^{-D^2/(2L^2)},\qquad
r_3=\frac{A_3}{A}e^{-R_\triangle^2/L^2}.
\]
The constants \(c,A_2,A_3\) and the intensity of \(Y\) can be fixed independently of the internal scale \(L\). Increasing \(L\) makes the lower-order deficits small in the anchored integrals needed for a correction process. The construction uses finite parameter choices, not a limit of point processes.

The second alternative \(C\) has separated clusters of at most three points. A Poisson centre process is thinned by retaining isolated centres. Positive symmetric triple and pair kernels supply the lower deficits, with the triple's pair marginal subtracted before defining the pair kernel. A uniform cylindrical-coordinate estimate controls that marginal even for triangles approaching collinearity. Singleton and empty-cluster probabilities complete the prescribed small intensity and the probability budget. The separated clusters contribute no local fourth tuples.

Let \(\kappa=(36e\pi M^3)^{-1}\). The proof assigns
\(\lambda_C=\min\{\lambda_0,\kappa/2\}\) and
\(\lambda_Y=2\lambda_0-\lambda_C\).
This gives intensity \(\lambda_0\) after mixing, while the correction process stays within its fixed capacity. All three full local identities then follow by linearity of expectation.

Global regularity is a separate part of the proof. For every assignment of up to four points to surfaces, the position map has full differential rank almost everywhere. This proves full absolute continuity, including allocations outside the local formula domains. A uniform bound on the number of surfaces meeting a bounded ball gives finite third moments. For fourth-order density finiteness, bounded-diameter configurations in sufficiently large bands can use only concentric spheres. Outside a countable union of explicitly nonzero polynomial zero sets, their radii are locally bounded, so only finitely many bands contribute on a neighbourhood. The correction process is dominated by an unthinned finite-cluster process with all local moments and full densities.

The construction is deliberately non-ergodic. No ergodic, mixing, empirical earthquake, asymptotic or numerical claim is part of the result. The final mixture need not be Cox merely because one alternative is Cox.

## Construction record and scope

| Approach | Submissions used | Final reviewed outcome |
|---|---:|---|
| Poisson clusters | 4/4 | Unsuccessful for exact S1; valid partial theorems and scoped obstructions preserved. |
| Cox processes | 1/4 | Entire Cox class excluded under S1; owner explicitly closed early, with three submissions unused. |
| Hawkes/branching | 4/4 | Unsuccessful for exact S1; valid partial constructions and scoped family obstructions preserved. |
| Investigator choice | 4/4 | Exact unchanged S1 proved; individual and final independent reviews accepted. |

The complete per-submission record is in `attempt_ledger.json`; `artifact_index.md` links each proof and its review.

The Poisson-cluster track established exact full pair and triangle laws in a sufficient small-intensity range, actual cylinder approximations, and failures of specified cylinder mixtures. Its final sphere construction attains an exact reciprocal-volume same-parent density, with all other parent partitions explicitly retained in the full density. Its all-intensity cap/sphere construction has an exact full pair law and arbitrarily small relative fourth error, but its triangle law fails. Neither approximation nor a same-parent identity is counted as exact S1.

The Cox track's reviewed theorem applies to arbitrary locally finite random directing measures, including singular diffuse measures. The exact full triple law gives a vanishing averaged square for dilation tests; simultaneous test identities constrain the directing measure locally to planes. Full fourth absolute continuity is incompatible with the resulting nonzero directing mass. This does not exclude general non-Cox point processes.

The branching track excluded its initial count-independent iid spatial branching subclass and then constructed broader marked families. Its final dependent finite-cluster correction gives exact full pair and triangle laws when \(\lambda_0M^3\leq1/(64\pi)\), with finite third and infinite fourth moments and global full densities. A positive parent-partition remainder prevents its full fourth density from being reciprocal volume. Two missing plus signs in its final display are explicitly restored in the frozen review; the submitted proof is preserved unchanged. A separate earlier review transcription defect is likewise preserved with an accompanying note.

The investigator-choice track first obtained an exact full fourth law from separated slabs. Its second submission attained all three full identities in an explicit sufficient low-intensity range. Its third clarified the moment class and proved restrictions on specified superpositions and slab mixtures, without establishing a general intensity ceiling. The fourth replaces the slab component and lower-order error estimates with the spherical construction above.

## Source verification, independence and accounting

One shared literature agent checked a precise realisability-theorem gap against primary sources. The inspected results require locally finite/Radon factorial measures, finite-valued moment functionals, or stronger hierarchies that do not directly match the infinite-fourth-local-moment problem. A possible restricted-test extension remained unproved. These are identified hypothesis mismatches, not nonexistence theorems or an exhaustive novelty search. The final explicit construction invokes none of those realisability results. The source dossier and exact evidence are frozen in `literature/realisability_v01/`.

Every independent author and reviewer received a fresh context and an explicit hashed file packet. Only relevant own-track feedback was returned to construction agents. The final synthesis was the first permitted cross-track comparison; it was not fed back into another construction submission. All four original allowances remain fixed, including the owner-approved early Cox closure.

Actual runtime metadata verified `gpt-6-astra` and `xhigh` before mathematical work. Numeric input, cached-input, output, reasoning and total counters are recorded per registered agent turn. Counter increments, rather than cumulative snapshots, are aggregated within each turn. Cached input is a reported subset; reasoning is already included in output. Metadata collection excludes conversation and private reasoning content.

The accounting collector preserves all model observations and original turn timestamps across compactions. Its metadata correction leaves completed-turn numeric usage unchanged. Parent/child aggregation semantics, cache-write categories, applicable pricing and actual charges remain NR. No cross-session billed total, API-equivalent cost or word-count token estimate is asserted. The final coordinator response remains outside its preceding live snapshot. The full measured table, boundaries and limitations are in `usage_cost_summary.md` and `agent_accounting.jsonl`.

All new work remains under this run. Original setup files, frozen targets, source additions, submissions, reviews and dispatch packets are hash-checked. No publication, simulation campaign, earthquake-data comparison, external message campaign or original-project edit was performed.

## Final synthesis and preservation

The final independent report `review_report.md` (SHA-256 `68dfdad1db7e04203439ed15154f72294464165188577622ba620172dc1f33d2`) reconstructs the S0/S1 conclusions, the entire Cox-class exclusion and the consequential construction dependencies. Its 45 findings cover all 16 mathematical submissions. No blocking gap remains for exact S1. The report explicitly limits its audit of historical ancillary calculations, literature-search completeness and private reading behaviour. It is an informal mathematical audit, not formal machine certification or a novelty claim.

The stale original statement ledger is preserved unchanged; `statements/ledger_v02.json` is the current outcome record. The original proposal and absent owner response are preserved; S2 was not adopted and no response is needed to complete this experiment. Frozen original inputs and all assigned proof/review hashes were checked. The final evidence inventory and accounting snapshot identify their exact coverage.
