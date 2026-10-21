# Realisability source check — v01

**Outcome D: verified related results with a decisive hypothesis mismatch. No inspected theorem establishes realisability in the requested non-Radon fourth-measure class.** The abstract restricted-test route remains F (an unproved bridge), not an impossibility result. Scope: two query batches, four primary full-text candidates, and the assigned DVJ convention passages. S1 is unchanged.

The runtime preflight independently verified `gpt-6-astra` / `xhigh`. Packet SHA-256: `0cd163c1ebe3b66c76d983c9e8db3cd9aa8e6a02dbdbf688bfc1b028bb7bcf0d`. All 28 allowlisted file hashes matched. No other track, seed, conversation, or prior run was read; no delegation occurred.

## Exact target and conventions

The complete original request is preserved in [request.md](request.md), SHA-256 `33196caad98ab485a82b6855c9315dcbfd7f5c2f1b6d36ddc56614cf372dbbfe`. The active adopted statement is copied verbatim to [target_statement_S1.md](target_statement_S1.md), SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`. Its amendment authority and hashes were read from the assigned S0-to-S1 record, without opening the referenced proof tracks.

We check full **ordered factorial expectation measures** \(\alpha^{(n)}\), not cumulants. Orders 1–3 are locally finite in the neutral request. The fourth has a nonnegative density finite almost everywhere and is sigma finite, but \(\alpha^{(4)}(B^4)=\infty\) for every sufficiently small nonempty spatial ball \(B\). The local test form is \(h_4=a_4/V+\ell\), \(\ell\in L^1_{\rm loc}\), with the whole expression nonnegative. This correction is only part of the source question: S1 still requires the exact \(a_4/V\) formula on \(E_4(M)\). A single process must meet every required order, prescribed intensity, stationarity, simplicity, global absolute continuity and almost-sure local finiteness. Neither a fourth-moment condition nor an altitude cutoff is introduced.

“Product ball” here means \(B^4\); it does not mean every neighbourhood of every noncoplanar tetrahedron. A finite density can be locally integrable away from the coplanarity locus while failing local integrability across it.

## Decisive inspected sources

All page numbers below are **the labels printed in the saved PDF**, with zero-based PDF indices in brackets. Reprint pagination is not silently identified with journal pagination. Full statements, relevant definitions and standing assumptions were inspected; this is not a complete proof audit.

### KLS2011 — Kuna, Lebowitz and Speer

[arXiv:0910.1710v2](https://arxiv.org/abs/0910.1710v2), 22 August 2011; *Ann. Appl. Probab.* 21, 1253–1281, DOI 10.1214/10-AAP703. Definitions §2 and Definition 3.1, reprint pp. 5–9 [4–8]; Theorems 3.6–3.7 p. 11 [10], 3.14 p. 15 [14], 3.17 p. 17 [16], 3.20 pp. 18–19 [17–18], 4.3 p. 23 [22].

Their \(\rho_n=E\eta^{\odot n}\) is our \(\alpha^{(n)}\). The base space is locally compact with a countable base; locally finite counting measures carry the vague topology. Definition 3.1 requires symmetric **Radon** measures through the prescribed order and explicitly entails finite local moments through that order. Positivity tests use finite real integrals. The extension theorem needs domination; Daniell representation additionally needs continuity from above. The noncompact pair criteria impose a finite weighted third moment or corresponding local conditions. The stationary criterion adds a translation-uniform bound.

**D:** order four already fails Definition 3.1. The stated general-order extension does not remove that condition. The pair criteria do not prescribe the third or fourth measures.

### LM2015 — Lachièze-Rey and Molchanov

[arXiv:1102.1950v5](https://arxiv.org/abs/1102.1950v5), 19 January 2015; *Ann. Appl. Probab.* 25, 116–149, DOI 10.1214/13-AAP990. §2.1–2.2, Assumption 2.4 and Definition 2.5, pp. 5–7 [4–6]; Theorem 2.6 p. 7 [6]; Theorems 2.8 and 2.10 pp. 9–10 [8–9]; §3.1 pp. 11–12 [10–11]; Theorem 3.10 p. 24 [23].

Theorem 2.6 uses a real-valued normalized linear functional \(\Phi\) on a space \(G\) containing constants and majorizing pairwise maxima. The state space is completely regular. A lower-semicontinuous regularity modulus \(\chi\) makes \(\{\chi\le g\}\) relatively compact; each \(g\) must be continuous there. Existence with \(E\chi\le r<\infty\) is equivalent to \(\sup_{g\in G,g\le\chi}\Phi(g)\le r\). Weak compactness and invariant extensions have additional continuity/invariance assumptions. The point-process application assumes locally finite second correlation measures; its stationary pair/intensity criterion requires \(\int_B|z|^{-d}\bar\rho(dz)<\infty\).

**D for direct application; F for a new restricted-test formulation.** Infinite quartic integrals cannot be values of \(\Phi:G\to\mathbb R\). The theorem itself does not forbid all infinite untested moments.

### IK2019 — Infusino and Kuna

[arXiv:1802.03582v2](https://arxiv.org/abs/1802.03582v2), 14 October 2019; journal version *J. Math. Anal. Appl.* 483 (2020), 123551, DOI 10.1016/j.jmaa.2019.123551. Definitions 1.2–1.3 pp. 4–5 [3–4]; Definition 2.1 and Radon convention p. 6 [5]; Definition 3.1 p. 14 [13]; Theorems 3.9–3.10 p. 17 [16], 3.13 p. 18 [17].

The correlation convention is the full factorial one. Theorems 3.9–3.10 take an entire sequence of nonnegative symmetric Radon measures, with a Stieltjes determining condition and almost-increasing normalized growth bounds. Their positivity conditions involve squares and factorial localizing polynomials; simplicity adds zero second-order diagonal mass. The representing class \(M^*\) has continuous local moments of **every** order. The absolutely continuous formulation in Theorem 3.13 retains these conditions. Smooth-test generalized moments are finite-valued distributions, not arbitrary extended positive integrals.

**D:** the fourth measure is not Radon and does not define the required positive distribution; orders above four and growth conditions are also unspecified. Absolute continuity alone does not repair either mismatch. No assertion is made about the full moment literature beyond these inspected results.

### KLS2007 — Kuna, Lebowitz and Speer

[arXiv:math-ph/0612075v2](https://arxiv.org/abs/math-ph/0612075v2), 20 March 2007; DOI 10.1007/s10955-007-9393-y. Equations (3.1)–(3.4), pp. 7–8 [6–7]; Theorem 3.1 and Remark 3.3 pp. 9–10 [8–9]; Proposition 4.1 pp. 13–14 [12–13].

Theorem 3.1 constructs a factorized hierarchy from a pair function \(g\), assuming \(C(g)=\int|g-1|<\infty\) and a uniform finite product bound \(\prod_i g(x_0-x_i)\le b\) on allowed configurations. It guarantees intensities \(0\le\rho\le(ebC(g))^{-1}\) and exponentially bounded local correlation densities. The displayed three-order extension additionally uses a positive hard-core distance and bounded finite-range triplet modification.

**D:** the product bound already fails for \(g(z)=a_2/(\lambda_0^2|z|)\) near zero (take one other point). The hard core also conflicts with the requested domain. The constructed higher hierarchy is not a freely prescribed fourth measure. This is a failure of these sufficient criteria, not a general obstruction.

### Assigned convention check — DVJ2008

The frozen second edition of Volume II, §9.5, printed pp. 65–68 [81–84], defines extended expectation first, then uses existence terminology when the expectation is boundedly finite (p. 65, equation (9.5.1)); Definition 9.5.I is on p. 66. Example 9.5(b), p. 67 [83], discusses infinite moments. This convention must not be imported as an additional hypothesis of S1. The supplied book was not uploaded. This source is convention support, not an existence theorem for the requested data.

## Explicit comparison deductions

These are short deductions for testing the hypotheses above, not a proposed point-process construction.

1. **Sigma finiteness is weaker than the needed local finiteness.** If \(h_4\) is nonnegative and finite almost everywhere, intersect growing compact boxes with \(\{h_4\le m\}\). These sets have finite \(h_4\,dx\)-mass and, together with a null exceptional set, exhaust the space. Nevertheless, infinite mass on \(B^4\) forces infinite mass on the compact set \(\overline B^4\), so the measure is not Radon. It cannot be made Radon by choosing different values on null sets.

2. **Integrable signed corrections cannot cure the divergence.** On a compact neighbourhood containing \(B^4\), if \(s=a_4/V+\ell\ge0\) and \(\int|\ell|<\infty\), then \(a_4/V\le s+|\ell|\). Thus infinite integral of \(a_4/V\) entails \(\int s=\infty\). No cancellation of two infinite quantities is legitimate here.

3. **The full quartic polynomial functional is not real-valued.** Choose \(\varphi\in C_c^\infty(\mathbb R^3)\), \(\varphi\ge0\), equal to one on \(\overline B\). The configuration observable \(Q(\eta)=\langle\varphi^{\otimes4},\eta^{\odot4}\rangle\) is finite for every locally finite configuration. Its prescribed expectation is nevertheless infinite. Any real vector space containing \(Q\) also contains \(-Q\); one cannot assign its integral as a finite linear functional or apply finite-valued positive-extension results directly. Finite-part distributional regularization would change the required positive measure identity.

4. **The finite-moment mismatch is exact.** For a bounded \(B\), \(\alpha^{(4)}(B^4)=E(N(B))_4\). Since \(N^4=(N)_4+6(N)_3+7(N)_2+N\), infinite fourth factorial mass entails an infinite fourth count moment, while the first three moments may remain finite. Almost-sure finite counts do not contradict this conclusion.

5. **LM's concrete stationary pair criterion also fails at order two.** In its normalization, the reduced measure for the requested pair law has density \(\bar\rho(dz)=a_2\lambda_0^{-2}|z|^{-1}\,dz\) near zero. In dimension three, the required weighted integral is proportional to \(\int_0^\epsilon r^2r^{-3}r^{-1}\,dr=\int_0^\epsilon r^{-2}\,dr=\infty\). This does not exclude use of another regularity modulus.

## What remains unproved

A restricted family of integrable fourth-order tests might avoid the infinite functional values. To turn that observation into an application, one still needs a fully defined test space and finite functional; positivity for all configuration-wise nonnegative tests and well-definedness under linear relations; the required majorization and regularity-modulus bound; measure identification on a sigma-finite determining class; and proof that the recovered fourth measure has no extra mass on excluded or degenerate sets. Nonnegative densities by themselves do not establish these conditions.

Compactness of process laws from intensity bounds would not by itself preserve quartic expectations. A limit argument requires appropriate integrability or a separate identification argument on every chosen test. If local laws are used, their compatibility and countable-additive extension must also be proved. Stationarity requires an invariant representation or a justified invariant-extension step. No such substantial bridge is supplied or claimed here.

For S1, global density extensions outside the specified domains must themselves meet any chosen theorem's hypotheses. Local formulas alone do not supply a globally positive moment functional.

## Coverage and limits

The six exact queries are in [search_log.json](search_log.json). Four serious primary PDFs were obtained and their relevant full statements and assumptions read; decisive pages were locally rendered where useful. Latest arXiv version metadata were checked. The publisher LM endpoint returned non-PDF content; the v5 arXiv reprint was used. Lenard I/II and other search leads were not promoted from references or snippets into verified theorem support. No fifth candidate or further query batch was needed to establish the reported mismatches. No claim of exhaustive coverage, novelty, present open status, nonexistence, or target authority is made.

Source bytes, extracted texts, provenance and locators are frozen in [source_manifest.json](source_manifest.json). Structured comparison is in [evidence.json](evidence.json); unresolved obligations are in [open_questions.md](open_questions.md). Accounting reports exposed own-thread telemetry only, with NR for unknown semantics and charges; the last checkpoint omits the later final-response tail pending coordinator reconciliation.
