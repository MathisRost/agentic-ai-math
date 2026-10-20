# Critical review — approach 3 submission v02

- Run / reviewer model / reasoning: `20261019T114252Z_cox_rerun` / `gpt-5.6-sol` / `xhigh`.
- Problem and submission hashes: `common/problem_statement.md` — `4c7a8b0ec361395179d7c6131e53b61bd312e028e552baa1a98fe6dc16eea84a`; `tracks/approach_3/submissions/v02.md` — `eb653072f665e0bd1fbb711d6d26297f9611a4673ad68c80922741a3f915dfa8`.
- Assigned issue-list hash: `reviews/approach_3/issues_v01_for_author.md` — `f56cee38283eb940c36c18ffb5d6f2ba15553171817e341032ace80588bc4b85`.
- Context received: `context_packets/review_3_v02.md`; the frozen setup/reviewer instructions and templates listed there; the frozen common problem, indices and definition audit; the shared literature dossier, bibliography and open questions; submission v02; and the author-facing v01 issue list.
- Context excluded: submission v01, review v01, proof work notes and conversations, other approaches' submissions and reviews, and coordinator/owner conversation history. The review is bound to the frozen v02 hash above.
- Review type: fresh delta review of repair round 1.

## Verdict and exact scope

**The governing exact reciprocal-simplex target is not established by this approach.** Submission v02 instead proves a valid scoped obstruction: after a finite-time spatial projection, no stationary scalar linear subcritical Hawkes process with a nonnegative causal triggering density

\[
\phi\in L^1(\mathbb R\times\mathbb R^3)\cap
L^\infty(\mathbb R\times\mathbb R^3)
\]

can have the required pair law on the complete domain $0<D\le M$. The projected pair correlation is essentially bounded, whereas $C_2/D$ is unbounded on every positive-measure neighbourhood of the pair diagonal. This excludes simultaneous satisfaction of the three target identities within that subclass, at every prescribed positive intensity.

The conclusion is deliberately and correctly narrower than general non-existence. Integrable unbounded triggering densities, genuinely singular triggering measures, marked or multitype mechanisms, random carriers, nonlinear and critical variants, and non-Hawkes point processes remain unresolved. Equations (30)--(33) are necessary residual conditions for the scalar linear density setting developed in the submission, not an inverse construction and not an obstruction for those wider classes.

All four author-facing v01 repair items are closed as revision items. In particular, H3-v01-F01 is closed because the restricted scope is now stated consistently; this does **not** mean that the governing existence problem is closed. I do not recommend another scoped author repair round for approach 3 v02. The submission is suitable for use in the final synthesis as a restricted negative theorem and a careful derivation of the full projected Hawkes density hierarchy.

## Reconstruction of the argument

The submission starts with a homogeneous Poisson process of immigrants on space--time $E=\mathbb R\times\mathbb R^3$. Each point produces a Poisson process of children with translation-invariant triggering density $\phi$, and descendants reproduce independently. The total offspring mass is

\[
\eta=\int_E\phi(z)\,dz<1.
\]

Thus each immigrant cluster is a subcritical Poisson Galton--Watson tree. The total progeny $S$ has the Borel distribution. Its generating series has radius $e^{\eta-1}/\eta>1$ for $0<\eta<1$, so $S$ has an exponential moment and, in particular, a finite fourth moment.

For a bounded space--time set $W$, the number $C_u(W)$ of points contributed by a cluster rooted at $u$ satisfies the pathwise translation integral bound

\[
\int_E C_u(W)^r\,du\le |W|S^r.
\]

The marked-Poisson exponential formula then yields finite ordinary cumulants of $N(W)$ through order four, and the ordinary moment--cumulant formula yields $\mathbb E N(W)^4<\infty$. This repairs the previously missing local fourth-moment argument.

The process is projected to space by retaining events in a bounded time interval $I$ of length $T$ and forgetting time. The resulting point process $X_I$ is stationary under spatial translations and has local fourth moments. Diffuseness of immigrant positions and offspring displacements implies that different space--time events have the same spatial coordinate with probability zero, so the projection is simple. Its spatial intensity is $\nu T$, where $\nu=\mu/(1-\eta)$. Choosing

\[
\mu=\lambda _0(1-\eta)/T
\]

therefore gives the prescribed intensity $\lambda _0$ without changing the physical spatial domains.

For the density calculation, the submission correctly avoids assigning a density to the fixed immigrant. The ordered factorial moment measures $\mathsf M_A^u$ of a cluster rooted at $u$ satisfy the partition recursion (10). After the one-block descendant term is separated, the recursion is solved using the descendant resolvent

\[
\mathsf R=\delta_0+\sum_{m\ge1}\phi^{*m}(z)\,dz.
\]

The induction following (16) shows that, for a fixed root, every term either has one root Dirac coordinate and densities in all remaining coordinates, or is absolutely continuous in every coordinate. Convolution against $\phi(v-u)\,dv$ removes a descendant root Dirac; integration over the immigrant location removes the final possible root Dirac. Consequently the space--time factorial cumulant measures through order four are absolutely continuous and locally finite. Tonelli's theorem then gives absolutely continuous finite-time spatial pushforwards.

The full spatial factorial moment densities are obtained only after the cumulant calculation. The submission includes the complete partition hierarchy:

\[
\rho_I^{(2)}=\lambda _0^2+Q_2^I,
\]

\[
\rho_I^{(3)}=\lambda _0^3+\lambda _0\sum_{i<j}Q_2^I(i,j)+Q_3^I,
\]

and at order four the baseline, six $2+1+1$ terms, three $2+2$ terms, four $3+1$ terms and the connected fourth term. Thus the term counts are $2,5,15$, and observations from distinct immigrant clusters are not discarded.

Finally, under $\phi\in L^1\cap L^\infty$, Young's inequality makes the descendant resolvent $\Psi=\sum_{m\ge1}\phi^{*m}$ both integrable and essentially bounded. Formula (18) then bounds the space--time second factorial cumulant density uniformly. Integration over $I^2$ preserves a finite essential bound for $Q_2^I$, hence for $g_2^I$. This contradicts $g_2=C_2/D$ on a positive-measure set of arbitrarily close pairs.

The residual formulas (30)--(33) then record what an unbounded integrable scalar triggering density would still have to achieve. Nonnegativity of Poisson-cluster factorial cumulants forces $C_2\ge M$, gives the stated nonnegative third-order residual on $\mathcal D_3$, and gives the fourth-order residual on $\mathcal D_4$. The triangle residual is used on a tetrahedral face only where that face itself lies in $\mathcal D_3$.

## Review reasoning summary

The following decisive checks were re-established from v02 rather than accepted from its response section.

1. **Quantifier and target check.** The governing target is an exact statement about full product densities for one process at every prescribed admissible $\lambda _0,M,h_3,h_4$. V02 does not claim to solve it. Its theorem quantifies only over the scalar linear subcritical $L^1\cap L^\infty$ Hawkes subclass and uses the full pair domain $0<D\le M$. The limitation appears in the theorem statement, remaining obligation, checks and response to review.

2. **Fourth-moment check.** The Borel coefficient asymptotics give radius $e^{\eta-1}/\eta>1$. The translation identity behind (5) is valid term by term, because each intersection of translates of $W$ has measure at most $|W|$. This supplies integrable domination for differentiating the marked-Poisson exponential formula through order four. Equation (7) then gives the ordinary fourth moment. The argument also covers $\eta=0$ separately.

3. **Measure-to-density check.** In recursion (10), the root factor can be differentiated at most once, so a fixed-root term has at most one Dirac coordinate. Every $\mathsf H_B^u$ occurring in the source term has $B\subsetneq A$; integrating its possible root coordinate against the offspring density makes it absolutely continuous. The $\delta_0$ part of the resolvent preserves the one fixed-root Dirac, while the $\Psi$-part smooths it. Immigrant integration removes the last Dirac. The local bound (16a) supplies local finiteness of the resulting Radon--Nikodym densities.

4. **Partition check.** Normalising (23)--(25) gives $g_3=1+\sum c_2+c_3$ and $g_4=1+\sum c_2+\sum c_2c_2+\sum c_3+c_4$. Substitution of the pair target reproduces exactly the constants and signs in (31), while rearrangement gives (32). The fourth-order formula contains all 15 set partitions.

5. **Boundedness contradiction.** From $\|\phi^{*m}\|_\infty\le\|\phi\|_\infty\eta^{m-1}$, one gets both bounds in (26). The overlap term in (18) is bounded by $\|\Psi\|_\infty\|\Psi\|_1$, giving (27). Fubini transfers the essential bound to almost every spatial pair after time integration. Intersecting its full-measure set with the target identity inside $0<D<d_*$ yields a positive-measure contradiction, so the argument is not merely pointwise at the diagonal.

6. **Almost-everywhere and domain check.** A pair-null set pulls back to a null set in triple or quadruple space. A triangle-null set can be used for a face only on
   $\mathcal E_A=\mathcal D_4\cap\{x_A\in\mathcal D_3\}$. V02 makes precisely this restriction and does not impose the triangle-altitude condition on every tetrahedral face. Formula (33), which drops nonnegative third- and fourth-cumulant terms, remains valid throughout $\mathcal D_4$ without that substitution.

7. **Scope of evidence.** No numerical or empirical approximation is used in the theorem. The structural source claims are consistent with the frozen literature dossier, but the obstruction and repair arguments are self-contained enough that no unavailable source theorem carries a decisive proof step.

## Criterion-by-criterion assessment

| Criterion | Evidence/location | Assessment |
|---|---|---|
| Correct target and quantifiers | “Claim and scope”; Theorem 1; “Remaining exact obligation”; “Checks and limitations” | Correctly distinguishes the exact governing problem from a bounded-kernel scalar Hawkes obstruction. The target remains unresolved. |
| Whole-space existence and stationarity | “Process and existence”, sections 1--2 | The space--time cluster construction is on all of $E$, and the finite-time projection is a process on all of $\mathbb R^3$. Spatial stationarity follows from translation covariance. |
| Simplicity, local finiteness, prescribed intensity | Equations (3)--(8) and the collision argument | Established for the projected process. The immigrant rate in (8) attains arbitrary prescribed $\lambda _0>0$ at fixed $T$. |
| Local fourth moments and density existence | Equations (1)--(7), (9)--(18), (16a), (22) | Established through order four. The revised proof handles both the progeny tail and the fixed-root Dirac mass. |
| Full density hierarchy and combinatorial factors | Equations (19)--(25) | Correct complete $2,5,15$ hierarchy; cumulants are not substituted for full product densities. |
| Exact identities on the entire domains | Equations (27)--(28) and the $d_*$ contradiction | Proves impossibility of the exact pair identity on all $0<D\le M$ within the stated regular subclass. It supplies no exact construction outside that class. |
| One jointly feasible parameter choice | Equation (8); Theorem 1 | The process parameters meet prescribed intensity, but no parameters in the subclass can meet the reciprocal pair law. Hence no target witness is produced. |
| Source support and prior-work comparison | “Relation to prior work”; references; frozen dossier | Accurate at the level supported by the supplied dossier. Prior empirical and local approximate results are not promoted to exact theorems. |

## Detailed findings

### H3-v02-C01 — restricted theorem is supported

- **Severity:** positive conclusion / scope limitation.
- **Location:** Theorem 1; equations (18), (26)--(28).
- **Mathematical reason:** the descendant resolvent of an $L^1\cap L^\infty$ subcritical kernel is essentially bounded, and the overlap term is controlled by $\|\Psi\|_\infty\|\Psi\|_1$. The time-integrated pair correlation is therefore essentially bounded. The target $C_2/D$ exceeds any fixed bound on a positive-measure family of sufficiently close pairs.
- **Consequence:** the scalar linear subcritical bounded-density Hawkes subclass is rigorously excluded. This is a genuine exact negative theorem, but only for that subclass.
- **Repair:** none required. Preserve the restrictions whenever the theorem is cited.

### H3-v02-C02 — governing exact problem remains unresolved

- **Severity:** unresolved target, not a defect in the stated restricted theorem.
- **Location:** end of “Claim and scope”; “Remaining exact obligation”; “Checks and limitations”.
- **Mathematical reason:** the essential-boundedness step does not apply to an integrable unbounded triggering density and says still less about marked, carrier, nonlinear, critical or non-Hawkes processes. The nonnegative residual equations (30)--(33) are necessary conditions only; no triggering mechanism realising them is constructed.
- **Consequence:** approach 3 cannot be recorded as establishing general existence or general non-existence for the reciprocal-simplex target.
- **Repair:** no further prose repair is needed. Further progress would require a new construction or a new obstruction that covers a precisely enlarged class.

### H3-v02-C03 — source verification is intentionally bounded

- **Severity:** documentation limitation.
- **Location:** “Relation to prior work”, “References”, and “Source-tree check”.
- **Mathematical reason:** this delta review was authorised to inspect the frozen shared dossier and bibliography, not the source PDFs or local manuscript trees themselves. The dossier supports the cited distinctions between cumulants and moments and the stated prior-work scope. The central v02 arguments are supplied self-contained.
- **Consequence:** the present approval is mathematical approval of the self-contained restricted theorem and repairs, not a new primary-source audit of every bibliographic sentence.
- **Repair:** none required for v02. The final synthesis should retain the dossier's source-access qualifications.

No new mathematical defect was found that warrants an additional author-facing repair item.

## Coder/source verification

No coder request was needed. The relevant checks were exact analytic checks: Borel-series radius and moment consequence; the translation integral bound (5); the fixed-root measure recursion and Dirac removal; the $2,5,15$ partition expansion; normalised residual algebra; Young bounds for the resolvent; and Fubini pullbacks of null sets.

The context-packet hashes were checked before review. All listed frozen files matched their prescribed SHA-256 values. No simulation, floating-point calculation, finite grid or empirical fit was used. Source support was assessed only through the authorised frozen definition audit, literature dossier, bibliography and open-questions file. No external browsing was performed.

## Revision history

| Prior issue | Status in v02 | Evidence and assessment |
|---|---|---|
| H3-v01-F01 — unresolved governing scope | **Closed as a revision item; limitation remains mathematically open** | Theorem 1 and every summary/limitation section restrict the result to scalar linear subcritical $L^1\cap L^\infty$ triggering densities. Wider Hawkes and non-Hawkes classes are expressly unresolved. |
| H3-v01-F02 — fourth local moment | **Closed** | Equations (1)--(3) prove an exponential progeny moment; (5)--(6) justify the Poisson-cluster cumulants; (7) yields the fourth local count moment. |
| H3-v01-F03 — measure to density | **Closed** | Equations (9)--(18) remain at measure level until immigrant integration removes the root Dirac; (16a) proves local finiteness; (22) gives the spatial pushforward densities by Tonelli. |
| H3-v01-F04 — a.e. versions | **Closed** | Equations (29)--(33) are explicitly almost-everywhere statements for compatible versions. Face use is restricted to $\mathcal E_A$, with the positive-measure qualification made explicit. |

**Repair-round decision:** all assigned v01 issues are closed in v02. No second scoped repair round is needed. Preserve v02 and this report for final synthesis.

## Decision record

| Decision | Outcome | Basis |
|---|---|---|
| Does v02 establish the governing exact target at arbitrary prescribed intensity? | **No** | It supplies no exact witness and no general non-existence theorem. |
| Does v02 establish a correct restricted result? | **Yes** | The bounded pair-correlation argument excludes the stated $L^1\cap L^\infty$ scalar subcritical Hawkes subclass. |
| Is prescribed intensity handled within the restricted construction? | **Yes** | Equation (8) chooses the immigrant rate so that the finite-time projection has intensity exactly $\lambda _0$. |
| Are local fourth moments and absolute continuity through order four justified? | **Yes** | Equations (1)--(7), the measure induction after (16), (16a), and (22). |
| Are full product densities, rather than connected densities alone, used? | **Yes** | Equations (19)--(25) include every set partition through order four. |
| Are all prior author-facing issues closed? | **Yes, as revision issues** | Each requested repair is present and survives rechecking. The broad existence question remains unresolved. |
| Is another author repair round required? | **No** | No new mathematical or scope defect was found in the revised restricted theorem. |

## Remaining mathematical questions

1. Can an integrable but unbounded nonnegative causal triggering density produce the pair residual $c_2^I=C_2/D-1$ on all $0<D\le M$ while remaining subcritical and retaining finite local fourth moments?
2. If the pair residual is realisable, can one mechanism simultaneously realise the nonnegative third- and fourth-order residuals (31)--(32) on exactly $\mathcal D_3$ and $\mathcal D_4$, including every disconnected partition?
3. Can marked, multitype or random-carrier Hawkes constructions alter the geometry without introducing singular projected factorial measures or losing simplicity and local moment control?
4. Is there a broader obstruction, using only values fixed on the finite target domains, that excludes a larger Hawkes class without assuming essential boundedness or extending the reciprocal identities outside those domains?
5. How should genuinely singular triggering measures be formulated so that existence, stationarity, projected simplicity and the absolute continuity of factorial moment measures through order four can all be checked before any density calculation?

These are exact continuum questions. Numerical fits or finite-grid experiments may guide candidates but would not close them.
