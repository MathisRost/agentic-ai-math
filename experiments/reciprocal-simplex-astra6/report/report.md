# An exact point-process construction


## Page 1: An exact point-process construction

Architecture, mathematical development, independent reviews, token usage and elapsed time. Prepared for Mathis Rost on 21 October 2026 from the frozen records of run 20261020T164437Z_astra6.

3 h 00 m 20 s; research wall time
25 sessions; 37 recorded turns
4 of 4; winning track’s submission
S1 accepted; individual + final review
What the experiment established

The unrestricted reciprocal distance, area and volume laws are impossible at positive intensity. After independently reviewed general obstructions, the coordinator adopted a common upper diameter bound. The investigator-choice track then constructed a stationary point process satisfying all three exact full product-density laws for every prescribed positive intensity and diameter bound.

The construction chooses, with equal probabilities, between two whole processes. One puts Poisson points on separated random spherical surfaces and gives the exact reciprocal-volume law. The other has separated clusters of at most three points and corrects the pair and triangle densities. No lower distance, area, volume or shape cutoff is introduced.

What this report records

The account below reconstructs the public mathematical development from explicit proofs, saved decision summaries and reviews. It does not reproduce or infer private chain-of-thought. The archive preserves all 16 mathematical submissions, their 16 individual reviews, the final synthesis and the original statement history.

Acceptance means that the saved informal mathematical reviews found no blocking gap. It is not a proof-assistant certificate, an independent human certification or a novelty claim. The earlier-model experiment remains a separate folder; the two runs are not a controlled model comparison.

Reading guide: target and architecture, pp. 2–4; investigators and reviews, pp. 5–7; the resulting process, pp. 8–10; accounting and runtime, pp. 11–15; evidence and reproduction, p. 16.


## Page 2: The statement, before and after review

Let D be the distance between two points, A the area of a triangle and V the volume of a tetrahedron in three-dimensional Euclidean space. Write ρₙ for the full ordered factorial density: integrating it against a nonnegative test function gives the expected sum of that function over ordered tuples of n distinct process points. Full densities include every possible source of a tuple, not only points sharing a parent.

ρ₂ = a₂ / D      ρ₃ = a₃ / A      ρ₄ = a₄ / V

Condition | Initial S0 | Adopted S1
--- | --- | ---
Intensity | Every prescribed λ₀ > 0 | Every prescribed λ₀ > 0
Exact identities | All nondegenerate configurations | Nondegenerate tuples with diameter < M
Upper scale | None | Every prescribed M > 0; process may depend on M
Lower cutoffs | None | None; all nondegenerate shapes retained
Global process | Stationary, simple, a.s. locally finite on R³ | Same
Global densities | Orders 2, 3, 4 absolutely continuous; finite a.e. | Same, including outside the formula domains
Coefficients | Finite positive constants, chosen by construction | Same; independent of the configuration
Fourth moment | No finite fourth-moment assumption | Same
Outcome | False at every positive intensity | Existence accepted by two review stages

For S1 the quantifiers are: for every positive pair (λ₀, M), there exists a process and positive constants a₂, a₃, a₄. This does not assert that one process works for every M, or that the three coefficients can be prescribed independently. Ergodicity, mixing and isotropy are not requirements.

Authority for the change

S1 was adopted at 17:16:19 UTC after fresh reviews of general large-scale obstructions, including an additional fourth-order tail argument. The owner had authorised obstruction-driven domain revisions. A common diameter cap was one possible repair; no theorem made this particular cap unique, maximal or sufficient before construction.

A later S2 proposal would have restricted λ₀M³ to a small sufficient range. It was eligible after P4’s third unsuccessful reviewed submission, but the owner never approved it. S2 was never adopted, and no attempt count reset. P4’s fourth submission proved unchanged S1.

Primary records: archive/statements/S0.md, S1.md, S0_to_S1.md and ledger_v02.json. The older ledger.json is deliberately preserved as a historical snapshot.


## Page 3: How the agents were organised

[Figure: architecture; constructed from the adjacent architecture description or the recorded accounting timestamps.]
All 25 registered sessions verified gpt-6-astra with xhigh reasoning effort in runtime metadata. The coordinator controlled dispatch and statement versions. At most three delegated agents ran concurrently, so four construction tracks did not imply four simultaneous author sessions.

N1 investigated global non-existence and N2 investigated local geometry and moment classes. They began independently on S0 without the construction starting information. Each frozen submission went to a fresh reviewer before its obstruction could justify a target change.

P1 studied Poisson clusters; P2 Cox processes; P3 Hawkes or branching methods; P4 a method chosen by the investigator. Each received the same frozen starting packet after the obstruction phase. Its earlier proofs were leads to check, not accepted results of this run. Each track had four substantive submissions in total, including repairs.

A fresh reviewer received the frozen proof, target, permitted sources and review instructions, without the author’s conversation. Authors received their own feedback. New construction ideas were not circulated between tracks. One shared literature agent answered a precise source question. A coding role was configured but never dispatched.

Independence is the recorded context and cooperation protocol, not operating-system isolation or evidence of statistical independence. The final synthesis was the first permitted cross-track mathematical comparison and was not fed back into a new construction attempt.

Role labels used throughout: N1/N2 = obstruction investigators; P1–P4 = construction investigators; R-P4.2, for example, is the fresh reviewer of P4’s second submission. There were 16 individual reviewer sessions and one final synthesis session.


## Page 4: Three hours, with overlapping work

The research gate opened at 16:46:33.978 UTC and the run completed at 19:46:53.601 UTC on 20 October 2026: 10,819.623 seconds. In Stockholm this was 18:46–21:46. Preflight began earlier; the coordinator session started at 16:42:39.998 UTC.

[Figure: timeline; constructed from the adjacent architecture description or the recorded accounting timestamps.]
UTC | Decision or checkpoint
--- | ---
16:46:34 | Model and token-accounting gate passed; independent S0 investigations released.
17:00:56 | First obstruction reviews accepted; fourth-order extension commissioned before revision.
17:16:20 | S1 adopted after the extension’s fresh review.
17:43:34 | Owner ended the Cox track at 1/4, leaving three submissions unused.
18:39:35 | Optional S2 question sent after P4’s third completed unsuccessful review.
19:14:22 | P4 v04 frozen by the author; the coordinator records this at 19:15:12.
19:24:43 | Fresh individual review accepted exact S1; final synthesis authorised.
19:46:54 | Final synthesis, integrity check and accounting snapshot complete.

P4’s recorded freeze at 19:14:22 precedes its reviewer’s 19:14:57 start; the 19:15:12 decision-log entry is later administration. Bars use task-turn boundaries, including preflight and tool waits. Gaps between turns are omitted from summed role durations. Parallel bars overlap; their durations cannot be added to obtain experiment wall time. Coordinator end-of-turn duration was unavailable at the frozen snapshot.


## Page 5: The obstruction phase

N1, submission 1: global growth is too slow

The exact pair law on all scales gives an expected ordered pair count of order R⁵ in a ball of radius R. Positive stationary intensity makes the squared mean count of order R⁶. Variance nonnegativity requires the pair count to dominate the squared mean minus the mean, so these growth rates conflict. The reciprocal-area law gives a related mismatch, R⁷ versus R⁹. The fresh R-N1.1 review accepted the global obstruction and checked its scope.

E[(N(B_R))₂] = O(R⁵),     E[(N(B_R))₂] ≥ (E N(B_R))² − E N(B_R)

N2, submission 1: singularity does not imply infinite counts

Near a planar tetrahedron, V = A_base |h| / 3. Integrating 1/V across normal height h gives a divergent integral of 1/|h|. Reciprocal distance and reciprocal triangle area remain locally integrable. The local analysis therefore separates finite third moments from necessarily infinite fourth moments. It also gives an example showing that finite counts almost surely are compatible with an infinite fourth expectation. R-N2.1 accepted the stated general obstruction and auxiliary moment-class results; the finite-moment argument alone was not treated as an impossibility theorem for all S0 processes.

N1, submission 2: check order four before changing it

The proposed common cap would weaken the fourth law too. The coordinator therefore requested a further global argument, rather than extrapolating from moment divergence. N1 used bounded occupancy indicators and nondegenerate quadruples to exclude the specified reciprocal-volume tail at positive intensity without assuming a finite fourth moment. Fresh R-N1.2 accepted this extension before S1 was adopted.

Why the review sequence mattered

The general obstructions justify weakening large-scale exactness. They do not justify excluding flat shapes, imposing a finite fourth moment or restricting the intensity. These distinctions were retained in S1. Each new construction track received the adopted target and its authority, and began with its original four-submission allowance.

All three obstruction submissions and all three reviews are in archive/tracks/nonexistence_*/submissions/ and archive/reviews/nonexistence_* /. The report summarises their explicit arguments; it is not a transcript of hidden deliberation.


## Page 6: Poisson clusters and Cox processes

P1: four reviewed submissions, exact S1 not attained

Attempt | Mathematical progress and reviewed limitation
--- | ---
1 / 4 | Exact pair and triangle laws in a sufficient small-intensity range, with scoped obstructions for specified finite-cluster representations. The fourth law is not attained. R-P1.1 accepts partial progress.
2 / 4 | Actual cylinder constructions give exact lower laws and an approximate fourth law at low intensity. Equality at order four and the all-intensity requirement remain open. R-P1.2 accepts the restricted result.
3 / 4 | Scoped cylinder-mixture obstructions and convergence results clarify why the proposed limiting route does not settle fourth factorial moments. R-P1.3 accepts the scoped results, not general non-existence.
4 / 4 | Sphere clusters produce an exact reciprocal-volume same-parent density. The full fourth density retains positive contributions from other parent partitions. Another construction achieves an exact pair law and arbitrarily small relative fourth error at any intensity, but fails the triangle law. R-P1.4 accepts the partial theorems.

For a Poisson cluster process, a four-point tuple may come from one, two, three or four parents. Solving the one-parent formula does not solve the full density. This distinction is the central reason the final P1 construction did not pass, even though its spherical calculation was useful mathematical progress. The approach was closed as unsuccessful for exact S1 after four submissions; no theorem of general impossibility was inferred.

P2: a reviewed obstruction for the entire Cox class

P2 submitted one theorem ruling out every Cox process under S1, including Cox processes with singular diffuse directing measures. The exact triple law forces averaged squares of suitable dilation tests to vanish. The resulting local restrictions put the directing measure on planes, which conflicts with the required global absolute continuity of the fourth factorial measure. R-P2.1 independently accepted this class-specific obstruction.

The owner explicitly chose to end this track at 1/4 on 20 October. Three permitted submissions remained unused. This decision did not change S1 or transfer a class-specific obstruction into a general restriction. The sphere branch of the winning process can still be Cox: that branch alone does not satisfy S1’s exact triple identity.

Records: archive/tracks/proof_1/ and proof_2/; corresponding reviews; archive/proposals/proof_2_early_track_decision_owner_response.json. No exact-target pass is assigned to either track.


## Page 7: Branching and investigator choice

Track / attempt | Result and independent review
--- | ---
P3 / 1 | An obstruction for a fixed count-independent iid spatial branching subclass. R-P3.1 accepts that scope; broader branching constructions remain open.
P3 / 2 | A broader marked branching construction and exclusions for specified families. R-P3.2 accepts partial results without an exact all-intensity S1 pass.
P3 / 3 | A full-pair partial theorem and a scoped spherical-family obstruction. R-P3.3 accepts these; a separate frozen note corrects a transcription sign in its review.
P3 / 4 | Exact full pair and triangle laws when λ₀M³ ≤ 1/(64π), but a positive parent-partition remainder at order four. R-P3.4 accepts the restricted result and restores two missing plus signs in display (26). Four submissions used.
P4 / 1 | Separated slabs give an exact full reciprocal-volume law, but not the pair and triangle laws. R-P4.1 accepts the partial theorem with precision corrections.
P4 / 2 | All three exact full laws in an explicit sufficient low-intensity range. R-P4.2 confirms the range and a representation-specific ceiling; arbitrary prescribed intensity is unresolved.
P4 / 3 | Moment-class clarification and restrictions on specified slab mixtures and superpositions. R-P4.3 confirms their scope. A proposed low-intensity S2 amendment becomes eligible after this review, but receives no approval.
P4 / 4 | Separated random spheres plus a small separated-cluster correction, combined by a whole-law mixture. R-P4.4 accepts unchanged S1 for every prescribed (λ₀, M). The final synthesis independently confirms the conclusion.

Literature and final synthesis

The shared literature agent checked a precise question about point-process realisability theorems during P4’s final attempt. The inspected results required Radon or locally finite factorial measures, finite-valued moment functionals, or a stronger hierarchy. Those hypotheses do not directly fit this fourth-moment class. A proposed extension remained unproved; the final explicit construction did not rely on it.

The final reviewer compared all 16 mathematical submissions and recorded 45 findings. It accepted S0 impossibility and S1 existence, identified the stale statement-status ledger, and preserved limits on ancillary calculations and source-search coverage. The coordinator issued ledger_v02.json without altering the earlier ledger, target or attempt count.

The winning idea came from the investigator-choice role P4, using its fourth and final submission. P4 was not a different model: all roles used the same verified model and effort. P1 and P4 had common starting leads but did not receive one another’s new constructions.


## Page 8: First branch: points on separated spheres

Fix λ₀ and M. Set κ = 1/(36eπM³), λ_C = min{λ₀, κ/2} and λ_Y = 2λ₀ − λ_C. The first branch, Y, must carry mean intensity λ_Y. It places Poisson points on separated random spherical surfaces throughout R³.

A stationary family, with room between surfaces

First choose one radius band: (0, M], (M, 2M], (2M, 4M], and so on, with explicit positive probabilities; a remaining probability selects no spheres. For a band with upper radius b, choose a lattice of centres with spacing 4b + 2M and translate it uniformly within one lattice cell. At each centre use a common randomly shifted radial grid with spacing 2M, retaining each candidate sphere with a radius-dependent probability.

Different retained surfaces are more than M apart. The distance between centres is therefore not the D in the target law: D is the distance between observed process points. The random lattice translation gives stationarity. Each realised band has finitely many candidate radii, which helps ensure local finiteness. Across the whole ensemble all positive radii are available; the band choice is not a fixed shape cutoff in the target.

Sampling points and controlling the densities

Conditional on the surfaces, sample independent Poisson point processes on their area measures. The surface intensity depends on radius. Let γ(R) dz dR be the first intensity of sphere centres and radii, and let a(R)/(2R) be the density per unit surface area. With positive constants K, c and scale L, set

f(q) = (K/L) exp(−q/L²),     a(R) = c/f(R²),     γ(R) = 2R f(R²)⁴/c³.

Any tuple of diameter below M belongs to a single sphere. Four affinely independent points determine their circumsphere uniquely. Changing variables from the sphere parameters and four surface points to four spatial positions gives the inverse-volume Jacobian. The chosen weights make its coefficient constant:

ρ₄,Y = c/(48V),     ρ₂,Y = A₂ exp(−D²/(2L²))/D,
ρ₃,Y = A₃ exp(−R△²/L²)/A.

Here R△ is the triangle’s circumradius, A₂ = πK²/(4c), and A₃ = K√π/8. Put C₀ = π^(3/2)/(3√3), choose K large, and set c = √(C₀K³/λ_Y). Then Y has intensity C₀K³/c² = λ_Y. Taking K large enough that K⁴/c³ ≤ 1/(10000M) makes the total band probability at most 0.9, uniformly for L ≥ M (P4 v04, Sections 1–3). Thus K and c are fixed first; a finite large L can then reduce the correction costs without invalidating the sphere probabilities or changing λ_Y. Nearly flat triangles can have large circumradius, so the proof needs an integrated estimate, not a uniform shape bound.

The inverse-volume mechanism is a classical spherical change of variables. The exact separated-surface sampling and the remaining global regularity arguments are in P4 v04. The later source check is discussed on p. 10; it is not a novelty certificate.


## Page 9: Second branch: correcting pairs and triples

The second branch, C, has separated clusters containing zero, one, two or three points. It supplies exactly the lower-order deficits while contributing no four-point tuple of diameter below M.

Why thinning does not invalidate the local calculation

Start with Poisson candidate centres at intensity η = 1/(36πM³). Retain a centre only when no other candidate lies within 3M. Retained centres are dependent, but their first intensity is known: κ = η/e. Assign independent cluster marks after this thinning, keeping every offspring within M of its centre and every individual cluster of diameter below M. Points in different retained clusters are then more than M apart.

A local tuple must come from one cluster. Its expectation therefore uses only the retained centres’ first intensity κ and the cluster mark law. Higher product densities of the dependent centre process are unnecessary for these local identities. Outside diameter M the full densities include cross-cluster terms, but no reciprocal formula is required there.

Do triples first, then remove their pair contribution

q₃ = 1{diameter < M} A₃[1 − exp(−R△²/L²)]/A,
q₂ = 1{D < M}[δ + A₂(1 − exp(−D²/(2L²)))]/D.

Use the triple kernel F₃ = q₃. A triple also creates pairs, so write Mq₃(x,y) = ∫q₃(x,y,z) dz and use the pair kernel F₂ = q₂ − Mq₃. The proof bounds Mq₃ by B_L/D with B_L = 8πA₃M³/L and chooses δ = 2B_L. This makes F₂ nonnegative even near collinearity. A finite sufficiently large L makes the integrated pair and triple kernels fit the cluster probability and intensity budgets. These F_j are translation-invariant symmetric kernels for ordered tuples. Let Z_j be the integral of F_j(0, ·) over its j − 1 offsets. Choose a j-point mark with probability Z_j/(κ j!), and conditional offset density F_j(0, ·)/Z_j; omit zero-mass marks. A triple has 3! ordered pairs, so its pair contribution is exactly Mq₃. Singleton probability (λ_C − Z₂ − Z₃/2)/κ and the remaining empty probability complete the law (P4 v04, Section 7).

The fair coin combines whole laws

λ_C = min{λ₀, κ/2},     λ_Y = 2λ₀ − λ_C,
Law(X) = ½ Law(Y) + ½ Law(C).

Choose Y or C once for the entire realisation. There are no tuples crossing between these alternatives. Full factorial measures average linearly, giving intensity λ₀ and exact coefficients

a₂ = (A₂ + δ)/2,     a₃ = A₃/2,     a₄ = c/96.

This is a mixture, not simultaneous superposition. C can have distant tetrahedra involving several clusters; it has no tetrahedra in the prescribed local diameter domain. Its small intensity leaves Y free to carry any remaining prescribed mean intensity.


## Page 10: What still had to be proved

A local formula is not the whole theorem

P4 v04 separately proves stationarity, simplicity and almost-sure local finiteness. It also proves global absolute continuity of the full measures of orders two through four, including tuples on different surfaces or clusters outside the formula domains. For the sphere branch, the position maps have full differential rank almost everywhere for each assignment of points to surfaces.

Finite density almost everywhere at order four requires another argument. For a bounded configuration and sufficiently large radius bands, contributing surfaces must be concentric. The proof excludes a countable collection of nonzero polynomial zero sets; away from them, radii are locally bounded and only finitely many bands contribute. A finite-fourth-moment argument would not work here. The cluster branch is dominated by an ordinary finite-cluster process with all bounded-window moments.

Finite observations and infinite fourth expectation

Every bounded observation window contains finitely many points almost surely. Third count moments are finite on bounded sets, but fourth count moments are infinite on every nonempty open ball. Those statements coexist because rare configurations can have very large finite counts. Global absolute continuity also rules out exactly coplanar quadruples almost surely; the 1/V divergence arises from approaching the plane, not from mass on it.

The construction is deliberately non-ergodic. The global coin and the global radius-band selection retain randomness across the whole space. Prescribed λ₀ is the ensemble mean intensity; it is not a claim that each realisation has spatial density λ₀. No mixing, earthquake-data fit, simulation performance or ergodic construction was established.

How the geometric identity relates to literature

A later targeted lookup identified the Euclidean spherical Blaschke–Petkantschin formula in Chapron (2018), arXiv:1807.07384, p. 1, equation (1). Here z is the sphere centre, dω is unnormalised area on the unit sphere and R* is the unique circumradius of the four given points. In dimension three its Jacobian gives dx₁⋯dx₄ = 6V R⁵ dz dR dω₁⋯dω₄. With a sphere parameter intensity γ and surface density τ, the same-sphere contribution is γ(R*)τ(R*)⁴R*³/(6V). Substituting τ = a/(2R) and γa⁴/(2R) = c gives c/(48V).

This verifies a classical geometric ingredient, not publication of the complete process. The saved lookup was limited and did not certify novelty. Chapron’s attribution to Miles (1970) was indirect; the Miles source was not read in that check. The lookup occurred after completion and is excluded from the original experiment’s token table.

Primary proof: archive/tracks/proof_4/submissions/v04.md. Acceptance: archive/reviews/proof_4_v04/review.md and archive/review_report.md. Later source comparison: archive/followups/20261020_sphere_jacobian_sources_v01/comparison.json. Source URL: https://arxiv.org/abs/1807.07384.


## Page 11: Tokens, dollars and their limits

The preflight confirmed numeric runtime telemetry before research. The frozen ledger contains measured token counters for 25 registered sessions and 37 turns, including preflight. All 36 non-coordinator turns have completion boundaries. The coordinator row ends at its last observed token event, 19:46:32.086 UTC; its final response tail is unavailable. Later discussion, source lookup and this publication work are excluded.

Input includes cached input; output includes reasoning tokens. Neither subset is added again. Counts include repeated context sent across calls, not merely the words of the final artifacts. Counter differences are aggregated within each turn. Parent/child inclusion semantics remain unverified, so a sum across sessions is an unreconciled arithmetic total, not a deduplicated billed usage figure.

Session group | Measured total tokens | Standard estimate
--- | --- | ---
Coordinator | 48,419,330 | $62.45
Two obstruction investigators | 2,193,603 | $6.15
Poisson-cluster author | 5,065,884 | $15.42
Cox author | 1,449,077 | $3.19
Branching author | 5,908,067 | $16.26
Investigator-choice author | 6,704,527 | $17.56
16 individual reviewers | 19,445,629 | $43.36
Literature | 3,395,452 | $5.65
Final synthesis | 6,496,605 | $11.10
Raw arithmetic sum | 99,078,174 | $181.15

The standard-price scenario uses $10 per million uncached input tokens, $1 per million cached input tokens and $50 per million output tokens. Rates were retrieved from official OpenAI model/pricing information on 20 October, after the run. All observed call inputs were below the 272,000-token short-context threshold; the maximum was 237,725. Reported cache writes were zero.

Estimated USD = [10(input − cached) + 1(cached) + 50(output)] / 1,000,000.

The user recalled that Fast was not enabled; the saved telemetry does not independently establish the billed service tier. Standard pricing is therefore the working estimate. Applying double rates gives an alternative Fast/priority arithmetic scenario of $362.31. Neither number is an invoice or an inferred subscription charge; actual charges are NR. Tool fees, taxes, uplifts and the missing tail are excluded.

Raw column sums: 98,161,559 input, including 94,032,384 cached; 916,615 output, including 343,806 reasoning. The derived uncached input count is 4,129,175. The $181.15 scenario assumes the session counts are disjoint; that assumption has not been verified.


## Page 12: Measured usage for every agent session

Integer counts come from the frozen runtime ledger. “Reason.” is a subset of output; “Cached” is a subset of input. USD applies the standard-price scenario, with full precision retained in accounting/agents.json. NR means not reported. Labels are defined on p. 3.

Role | Input | Cached | Output | Reason. | Total | USD est.
--- | --- | --- | --- | --- | --- | ---
Coordinator | 48,252,029 | 47,603,712 | 167,301 | 60,898 | 48,419,330 | 62.45
N1 | 1,436,832 | 1,270,784 | 29,038 | 9,401 | 1,465,870 | 4.38
N2 | 714,417 | 670,976 | 13,316 | 3,481 | 727,733 | 1.77
R-N1.1 | 755,997 | 698,368 | 13,303 | 2,757 | 769,300 | 1.94
R-N2.1 | 632,594 | 590,464 | 13,437 | 3,149 | 646,031 | 1.68
R-N1.2 | 826,611 | 776,704 | 13,942 | 2,964 | 840,553 | 1.97
P1 | 4,953,497 | 4,415,232 | 112,387 | 61,282 | 5,065,884 | 15.42
P2 | 1,430,149 | 1,339,264 | 18,928 | 7,543 | 1,449,077 | 3.19
P3 | 5,798,102 | 5,246,080 | 109,965 | 58,245 | 5,908,067 | 16.26
P4 | 6,563,725 | 6,124,416 | 140,802 | 76,686 | 6,704,527 | 17.56
R-P2.1 | 991,018 | 921,984 | 16,103 | 3,604 | 1,007,121 | 2.42
R-P1.1 | 962,759 | 907,904 | 15,839 | 4,242 | 978,598 | 2.25
R-P3.1 | 1,132,796 | 1,070,976 | 15,188 | 3,771 | 1,147,984 | 2.45
R-P4.1 | 644,410 | 596,864 | 15,173 | 4,747 | 659,583 | 1.83
R-P1.2 | 1,238,864 | 1,156,480 | 18,570 | 4,491 | 1,257,434 | 2.91
R-P4.2 | 1,193,112 | 1,120,896 | 16,663 | 2,520 | 1,209,775 | 2.68
R-P3.2 | 1,173,060 | 1,096,960 | 16,374 | 3,488 | 1,189,434 | 2.68
R-P1.3 | 1,362,513 | 1,275,008 | 18,906 | 4,263 | 1,381,419 | 3.10
R-P3.3 | 1,748,658 | 1,660,928 | 17,301 | 2,986 | 1,765,959 | 3.40
R-P4.3 | 1,178,572 | 1,102,592 | 16,063 | 1,293 | 1,194,635 | 2.67
Literature | 3,373,806 | 3,241,344 | 21,646 | 3,554 | 3,395,452 | 5.65
R-P3.4 | 2,361,509 | 2,253,952 | 19,456 | 2,381 | 2,380,965 | 4.30
R-P1.4 | 1,396,668 | 1,301,760 | 21,021 | 4,963 | 1,417,689 | 3.30
R-P4.4 | 1,579,252 | 1,443,968 | 19,897 | 4,597 | 1,599,149 | 3.79
Final review | 6,460,609 | 6,144,768 | 35,996 | 6,500 | 6,496,605 | 11.10

Coordinator coverage is partial; the other rows cover completed registered turns. There is one session per row, but construction authors and N1/N2 have multiple turns. These are measured per-session values, not a reconciled cross-session bill. No actual monetary charge is available for any row.

The winning author used 6,704,527 measured total tokens across four submissions. Its four individual reviewers are separate rows. Combining that author and those reviews gives a raw sum of 11,367,669 tokens; it excludes shared preparation, obstruction work, literature and final synthesis, and inherits the same aggregation limitation.


## Page 13: Recorded elapsed time for every agent

“Turn time” is the sum of the runtime-reported durations of completed turns for that role, including tool waits and role preflight. First start and last completion delimit a wider span for multi-turn agents; intervening gaps are not included in turn time. All times below are UTC on 20 October 2026.

Role | Turns | First start | Last completion | Turn time
--- | --- | --- | --- | ---
Coordinator | 1 | 16:42:39 | NR | NR
N1 | 3 | 16:44:50 | 17:07:48 | 0:14:00
N2 | 2 | 16:45:00 | 16:53:07 | 0:06:52
R-N1.1 | 1 | 16:53:34 | 17:00:03 | 0:06:29
R-N2.1 | 1 | 16:53:58 | 17:00:19 | 0:06:21
R-N1.2 | 1 | 17:08:28 | 17:14:58 | 0:06:29
P1 | 4 | 17:16:43 | 18:46:10 | 0:53:59
P2 | 1 | 17:16:54 | 17:25:55 | 0:09:01
P3 | 4 | 17:17:05 | 18:45:16 | 0:54:19
P4 | 4 | 17:26:23 | 19:14:42 | 1:19:25
R-P2.1 | 1 | 17:28:58 | 17:36:23 | 0:07:25
R-P1.1 | 1 | 17:33:31 | 17:41:01 | 0:07:29
R-P3.1 | 1 | 17:36:37 | 17:44:11 | 0:07:34
R-P4.1 | 1 | 17:38:19 | 17:45:21 | 0:07:02
R-P1.2 | 1 | 17:53:36 | 18:01:59 | 0:08:23
R-P4.2 | 1 | 18:00:46 | 18:08:09 | 0:07:23
R-P3.2 | 1 | 18:00:58 | 18:08:10 | 0:07:12
R-P1.3 | 1 | 18:20:56 | 18:29:15 | 0:08:18
R-P3.3 | 1 | 18:24:23 | 18:32:20 | 0:07:56
R-P4.3 | 1 | 18:31:24 | 18:38:22 | 0:06:58
Literature | 1 | 18:46:02 | 18:55:53 | 0:09:51
R-P3.4 | 1 | 18:46:44 | 18:55:32 | 0:08:47
R-P1.4 | 1 | 18:55:44 | 19:04:40 | 0:08:55
R-P4.4 | 1 | 19:14:57 | 19:24:05 | 0:09:08
Final review | 1 | 19:24:59 | 19:45:05 | 0:20:06

hh:mm:ss is rounded to the nearest second; exact milliseconds are retained in the machine-readable records. Coordinator duration is NR because its turn was still in flight at collection. Its observed token-event span was approximately 3:03:52; that is not a completed-turn runtime.

Whole-run research wall time was 3:00:20. Adding the 36 completed delegated turn durations measures overlapping agent-turn time, not elapsed wall time or CPU/GPU time. The detailed starts and completions on the following pages make that overlap auditable.


## Page 14: Turn-level record 1 of 2

Each row is one recorded turn. “Step” is the submission number for investigators and reviewers; “pre” marks preflight, “lit” literature and “final” synthesis. Coordinator input and output cover the partial frozen snapshot. Input includes cache; total = input + output. Exact cache, reasoning, timestamp and model fields are in accounting/turns.json and turns.csv.

# / role | Step | UTC start | UTC end | Elapsed | Input | Output
--- | --- | --- | --- | --- | --- | ---
01 Coordinator | all | 16:42:39 | NR | NR | 48,252,029 | 167,301
02 N1 | pre | 16:44:50 | 16:45:45 | 0:00:55 | 147,813 | 1,972
03 N1 | 1 | 16:46:44 | 16:53:07 | 0:06:22 | 622,532 | 12,823
04 N1 | 2 | 17:01:06 | 17:07:48 | 0:06:42 | 666,487 | 14,243
05 N2 | pre | 16:45:00 | 16:45:40 | 0:00:39 | 147,810 | 1,370
06 N2 | 1 | 16:46:55 | 16:53:07 | 0:06:13 | 566,607 | 11,946
07 R-N1.1 | 1 | 16:53:34 | 17:00:03 | 0:06:29 | 755,997 | 13,303
08 R-N2.1 | 1 | 16:53:58 | 17:00:19 | 0:06:21 | 632,594 | 13,437
09 R-N1.2 | 2 | 17:08:28 | 17:14:58 | 0:06:29 | 826,611 | 13,942
10 P1 | 1 | 17:16:43 | 17:28:25 | 0:11:42 | 1,592,849 | 23,961
11 P1 | 2 | 17:42:00 | 17:52:57 | 0:10:57 | 1,262,064 | 24,067
12 P1 | 3 | 18:03:42 | 18:18:35 | 0:14:53 | 1,255,566 | 28,287
13 P1 | 4 | 18:29:43 | 18:46:10 | 0:16:27 | 843,018 | 36,072
14 P2 | 1 | 17:16:54 | 17:25:55 | 0:09:01 | 1,430,149 | 18,928
15 P3 | 1 | 17:17:05 | 17:28:33 | 0:11:28 | 1,822,445 | 22,488
16 P3 | 2 | 17:44:46 | 18:00:09 | 0:15:23 | 1,970,009 | 32,370
17 P3 | 3 | 18:08:44 | 18:24:03 | 0:15:19 | 1,054,235 | 28,677
18 P3 | 4 | 18:33:08 | 18:45:16 | 0:12:09 | 951,413 | 26,430
19 P4 | 1 | 17:26:23 | 17:37:30 | 0:11:06 | 1,403,102 | 22,925

Ordering follows the frozen ledger, grouped by registered session, rather than sorting all turns globally by time. Displayed UTC boundaries are rounded in the original accounting record; the independently reported millisecond duration can therefore differ slightly from subtracting the displayed times.


## Page 15: Turn-level record 2 of 2

Each row is one recorded turn. “Step” is the submission number for investigators and reviewers; “pre” marks preflight, “lit” literature and “final” synthesis. Coordinator input and output cover the partial frozen snapshot. Input includes cache; total = input + output. Exact cache, reasoning, timestamp and model fields are in accounting/turns.json and turns.csv.

# / role | Step | UTC start | UTC end | Elapsed | Input | Output
--- | --- | --- | --- | --- | --- | ---
20 P4 | 2 | 17:46:03 | 17:59:28 | 0:13:25 | 1,520,564 | 28,801
21 P4 | 3 | 18:08:53 | 18:30:34 | 0:21:41 | 1,645,090 | 40,268
22 P4 | 4 | 18:41:30 | 19:14:42 | 0:33:12 | 1,994,969 | 48,808
23 R-P2.1 | 1 | 17:28:58 | 17:36:23 | 0:07:25 | 991,018 | 16,103
24 R-P1.1 | 1 | 17:33:31 | 17:41:01 | 0:07:29 | 962,759 | 15,839
25 R-P3.1 | 1 | 17:36:37 | 17:44:11 | 0:07:34 | 1,132,796 | 15,188
26 R-P4.1 | 1 | 17:38:19 | 17:45:21 | 0:07:02 | 644,410 | 15,173
27 R-P1.2 | 2 | 17:53:36 | 18:01:59 | 0:08:23 | 1,238,864 | 18,570
28 R-P4.2 | 2 | 18:00:46 | 18:08:09 | 0:07:23 | 1,193,112 | 16,663
29 R-P3.2 | 2 | 18:00:58 | 18:08:10 | 0:07:12 | 1,173,060 | 16,374
30 R-P1.3 | 3 | 18:20:56 | 18:29:15 | 0:08:18 | 1,362,513 | 18,906
31 R-P3.3 | 3 | 18:24:23 | 18:32:20 | 0:07:56 | 1,748,658 | 17,301
32 R-P4.3 | 3 | 18:31:24 | 18:38:22 | 0:06:58 | 1,178,572 | 16,063
33 Literature | lit | 18:46:02 | 18:55:53 | 0:09:51 | 3,373,806 | 21,646
34 R-P3.4 | 4 | 18:46:44 | 18:55:32 | 0:08:47 | 2,361,509 | 19,456
35 R-P1.4 | 4 | 18:55:44 | 19:04:40 | 0:08:55 | 1,396,668 | 21,021
36 R-P4.4 | 4 | 19:14:57 | 19:24:05 | 0:09:08 | 1,579,252 | 19,897
37 Final review | final | 19:24:59 | 19:45:05 | 0:20:06 | 6,460,609 | 35,996

Ordering follows the frozen ledger, grouped by registered session, rather than sorting all turns globally by time. Displayed UTC boundaries are rounded in the original accounting record; the independently reported millisecond duration can therefore differ slightly from subtracting the displayed times.

All rows verified gpt-6-astra / xhigh. No token estimate from word counts has been substituted. Missing billing information and the coordinator final tail remain unavailable. This appendix covers the original experiment, not the documentation reader or subsequent repository work.


## Page 16: Reading and reproducing the evidence

Path in this experiment folder | Purpose
--- | ---
archive/inputs/ | Frozen launch prompt, workflow, role instructions, native model configuration, common context and construction starting proofs.
archive/statements/ | S0, adopted S1, amendment history and both historical/current ledgers.
archive/tracks/*/submissions/ | All 16 mathematical submissions; four original allowances are preserved.
archive/reviews/ | All 16 individual reviews, final synthesis and the transcription correction note.
archive/packets/ | Sanitised dispatch packets, allowed-file lists and historical hashes.
archive/proposals/ | Owner-approved Cox closure and the unapproved, unadopted S2 proposal.
accounting/ | Per-agent and per-turn JSON/CSV, timing boundaries and pricing assumptions.
report/ | This PDF, editable content and a reproducible ReportLab build script.
provenance/ | Original-to-export SHA-256 mapping, release checksums and documentation review.

Public copies replace machine-specific paths and session identifiers with portable placeholders. Mathematical content is preserved. The export manifest records each original hash and the hash of its public copy; embedded historical hashes still refer to the original evidence. A changed hash after sanitisation is not represented as byte-identical preservation.

The archive is curated, not a complete executable replay. Third-party books and papers, raw runtime conversations, private working notes and personal skill bodies are excluded. Some historical references therefore point to material that is intentionally absent. Source bibliographic records and mathematical reviews remain available. Proof headers saying “pending review” describe the original submission time; current acceptance is recorded in the later reviews and ledger_v02.json.

To rebuild the report, install Python with ReportLab and DejaVu Sans fonts, then run python report/build_report.py from this experiment folder. The script uses its adjacent report.json and the accounting JSON files. It does not rerun research, call a model or contact an external service. release_manifest.json records the final public file hashes; the local verification script checks them.

Source and review limits

The mathematical record is the frozen proof-and-review collection. The original shared literature dossier concerns a narrow realisability question, and the later spherical-Jacobian check concerns a classical ingredient. Neither is an exhaustive literature or novelty assessment. Pricing provenance is the 20 October saved official-source lookup, available through the rates and assumptions in accounting/pricing.json; the official model page is https://developers.openai.com/api/docs/models/gpt-6-astra.

A fresh exposition reader reviewed this documentation separately from the research. Four clarification requests were addressed in the final text. Its report and accounting are stored under provenance/documentation_review/. It does not change the original 25-session, 37-turn accounting or the four-attempt result.
