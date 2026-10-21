# Proposed statement change P4-v03-conditional

- From target: **S1**, `statements/S1.md`, SHA-256 `1075eb6bd3d54d5e0ddec1a1adee1fd30e474accb715304f42c46f21176226e8`.
- Proposed target: **S2-P4-proposed**; complete statement file `tracks/proof_4/work/S2_P4_low_intensity_proposed.md`, SHA-256 `21cf343bc5d702a17e6e41cd10c3bf6482e7e1fec541a20ff60bc5e58c29f62b`.
- Date and proposer: 20 October 2026; construction investigator `/root/proof_4`.
- Affected roles: a global target amendment would affect every role and requires coordinator recording and broadcast. This investigator only proposes it; no other track has been consulted or changed.
- Authority: **owner_request_pending**, conditional on completion of this track's third unsuccessful independent review. No owner request has yet been sent for decision.
- Status: **proposed, not adopted or broadcast**. The provisional ID does not allocate or activate a new target version.
- Relevant attempts: v01 and v02 submitted and independently reviewed, both partial rather than S1 passes; v03 is the third substantive submission and awaits review. One original submission allowance remains after v03. There is no reset.

## Exact change

The sole mathematical weakening is the parameter quantifier. S1 asks for every independently prescribed pair `(lambda_0,M)` in `(0,infinity)^2`. The proposal asks for every prescribed pair satisfying `lambda_0 M^3 <= tau`, with the fixed explicit `tau` below. Every pair with `lambda_0 M^3 > tau` is removed. At a fixed M, arbitrary positive intensity is no longer covered; at a fixed positive intensity, arbitrary M is no longer covered. This loss is not removed by spatial rescaling, which preserves the product.

The process is still defined throughout R^3, stationary, simple and almost surely locally finite, with exactly the prescribed intensity. The complete full factorial measures of orders two, three and four must still have globally finite-almost-everywhere densities and no singular component anywhere. All three reciprocal identities remain simultaneous on every nondegenerate configuration of diameter below the prescribed M, with no lower scale or shape threshold. The constants remain finite, positive and independent of configurations. No moment assumption, mixing assumption, representation restriction or connected-density substitution is added. The acceptance wording and historical labels are adjusted only to reflect the new quantifier and the unchanged S0/S1 verdicts.

The complete proposed replacement statement follows verbatim from the separately hashed file:

---

# S2-P4-proposed — exact reciprocal-simplex identities on a prescribed low-intensity range

**Conditional proposal only. Not adopted, not broadcast as a target, and not an S1 pass.**

## Quantifiers and process class

Put
\[
 J=\frac{\pi^2}{4},\qquad Z_0=\frac{\pi^2}{4}+\frac{2\pi}{3},\qquad
 \tau=\min\left\{\frac{1}{36e\pi},\;\frac{J^2}{8\pi^2Z_0},\;\sqrt{\frac{J^3}{32\pi^4Z_0^2}}\right\}>0.
\]
For every prescribed pair $\lambda_0>0$ and $M>0$ satisfying
$\lambda_0M^3\leq\tau$, does there exist one stationary, simple,
locally finite point process $X$ on all of $\mathbb R^3$ such that
\[
\mathbb E X(B)=\lambda_0|B|
\]
for every bounded Borel set $B$, together with constants
$a_2,a_3,a_4\in(0,\infty)$ satisfying the requirements below?

The process and constants may depend on both $\lambda_0$ and $M$. The
constants may not depend on a point configuration. Stationarity means
invariance in law under all translations. Local finiteness means
almost-sure finiteness of counts on bounded sets. No mixing, ergodicity,
isotropy, particular process representation or finite fourth count moment
is assumed.

## Full factorial expectation measures

For $n=2,3,4$ and nonnegative measurable $f$, define
\[
\int f\,d\alpha^{(n)}
=\mathbb E\sum_{x_1,\ldots,x_n\in X}^{\ne}
 f(x_1,\ldots,x_n).
\]
Tuples are ordered and pairwise distinct. Require nonnegative measurable
densities $\rho^{(n)}$, finite Lebesgue-almost everywhere on
$(\mathbb R^3)^n$, with the full measure identities
\[
\alpha^{(n)}(d\mathbf x)=\rho^{(n)}(\mathbf x)\,d\mathbf x.
\]
These are identities of extended nonnegative measures. Integrals over
bounded configuration sets and higher count moments may be infinite.
There is no singular component anywhere, including on degenerate
configurations or outside the domains where formulas are prescribed.

## Geometry and exact formulas

Put
\[
D(x_1,x_2)=\|x_2-x_1\|,\qquad
A(x_1,x_2,x_3)=\frac12\|(x_2-x_1)\times(x_3-x_1)\|,
\]
\[
V(x_1,x_2,x_3,x_4)
=\frac16\left|\det[x_2-x_1,x_3-x_1,x_4-x_1]\right|,
\qquad
(\Delta_2,\Delta_3,\Delta_4)=(D,A,V).
\]
For each $n=2,3,4$, let
\[
E_n(M)=
\left\{\mathbf x:
\max_{1\leq i<j\leq n}\|x_i-x_j\|<M,\quad
\Delta_n(\mathbf x)>0
\right\}.
\]
The required simultaneous identities are
\[
\boxed{\rho^{(n)}(\mathbf x)=\frac{a_n}{\Delta_n(\mathbf x)}
\quad\text{for Lebesgue-almost every }\mathbf x\in E_n(M),
\qquad n=2,3,4.}
\]
No positive lower distance, area, volume or altitude threshold is imposed.
All nondegenerate shapes with diameter less than $M$ are included.
Outside $E_n(M)$ the full densities are unprescribed, subject to the
global measure and process requirements above. Values on Lebesgue-null
sets may be chosen arbitrarily without adding singular mass.

The densities are full factorial densities. They are not connected
densities, factorial cumulants, same-parent densities or asymptotic
expressions. All partitions and parent allocations must be included in
any construction.

## Separate moment comparison and acceptance

The additional condition $\mathbb E X(B)^4<\infty$ for every bounded Borel
$B$ defines a separate comparison question. It is not a requirement of this proposed target.

A construction must meet every prescribed pair $(\lambda_0,M)$ satisfying
$\lambda_0M^3\leq\tau$ and all three domains simultaneously. A result for a
properly smaller parameter range, a smaller shape domain, or approximate or
connected densities is partial progress relative to this proposed target.
Rescaling must preserve the stated intensity and geometry quantifiers together.

This proposed target is weaker than S1: it excludes every pair with
$\lambda_0M^3>\tau$. The restriction is a sufficient range of a known
construction, not a proved necessary restriction for S1. Success for this
proposed target would not prove S1 or change the false verdict for unrestricted
S0. Adoption requires explicit owner approval, recording and broadcast;
until then S1 remains active. The original four-submission allowance does
not reset.

---

## Evidence and loss of scope

The sufficient range is already proved by this track's v02 Theorem 1, `tracks/proof_4/submissions/v02.md`, SHA-256 `9a3befd21f85424fea521c9c817837f2d943a1a0862c0e1586541b93c5d559ac`. The independent review `reviews/proof_4_v02/review.md`, SHA-256 `d08c9735cc498750b1b6f695a7f907369a07f005c71a995487921d44c7deb2d1`, verifies the actual construction and its restricted scope. No presentation-only new proof is being offered as the third submission: v03 contains new representation obstructions and a different formal residual hierarchy, with its unresolved realisability obligation stated explicitly.

There is **no proved general obstruction requiring the proposed intensity restriction**, either at tau or at any finite universal product bound. The v02 ceiling and the wider v03 correction-class obstruction are representation-specific. The latter remains subject to its independent review. They cannot justify a coordinator-led general-obstruction amendment to S1. Three failed construction attempts would likewise not prove the restriction necessary.

This is therefore a pragmatic possible owner amendment: it selects the exact parameter range for which this track already has a reviewed whole-space construction. It gives up the original unresolved all-intensity demand. The unrestricted S1 question would remain open in this track's record, and S0's false verdict would remain unchanged.

## Alternatives and decision

One alternative is to keep S1 unchanged and use the fourth and last allowed submission on its remaining realisability problem. The current partial construction can be reported without changing the target. Another is to choose a different weaker range or domain, but that would need an exact statement, explicit approval and a new proof against that statement. The class-specific ceiling 18/pi is not a proved sufficient range and is not proposed as an existence range. No one repair is mathematically forced by these results.

If the third independent review is complete and unsuccessful for S1, the coordinator may present this exact question to the owner:

> Do you approve replacing S1 by the complete proposed low-intensity target S2-P4-proposed above, restricting the parameter pairs to lambda_0 M^3 <= tau while preserving every other stated requirement, all prior verdicts, and the original four-submission allowance?

This is a prepared question, **not a record of a request already sent**. Owner response: NR, not yet requested. Response timestamp: NR. Approval scope: none. Silence is not approval. The coordinator may instead decline to present this optional proposal and continue with the unchanged target.

## Attempt and broadcast ledger

| Item | Current recorded status |
|---|---|
| Active target | S1, hash stated above; unchanged. |
| proof_4 v01 | Frozen and independently reviewed; partial fourth-order construction; no S1 pass. |
| proof_4 v02 | Frozen and independently reviewed; simultaneous identities on the sufficient range only; no S1 pass. |
| proof_4 v03 | Third substantive submission; independent review pending when this proposal is frozen. |
| proof_4 allowance | Three substantive submissions used upon v03 freeze; one remains; third completed review is still required before the optional owner checkpoint. |
| Other tracks' attempts | NR here: their files and reviews are not assigned. Coordinator maintains the global ledger. No count is inferred. |
| Proposed target delivery | Only prepared in proof_4's assigned work directory and reported to the coordinator; not adopted or broadcast to roles. |
| Role acknowledgements | None for a new active target. Current S1 acknowledgement is unchanged. |
| Counter reset | None, before or after any possible approval. |

If approval is later given, the coordinator must preserve this proposal and all earlier statement/submission/review hashes, record the actual owner response and scope, assign and hash the adopted statement, and broadcast it to every role including queued roles. No such step is authorised or claimed by this proposal alone.
