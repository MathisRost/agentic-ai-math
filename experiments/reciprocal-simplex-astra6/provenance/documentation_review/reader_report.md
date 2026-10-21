# Focused exposition review of draft_v01

I read the complete frozen draft, pages 1–16, including tables and the prose describing the planned figures, using FOCUSED_READER.md. Both supplied hashes match packet.json. Runtime metadata verified gpt-6-astra / xhigh before review. This review covers exposition for the packet’s mathematical audience; it does not certify proofs, source claims, accounting extraction or the unrendered figures. No earlier reviews or external material were consulted.

The first substantial stumble was on page 8: the text introduces three adjustable parameters without explaining their dependency order. Page 9 resolves why a mixture avoids unwanted cross-tuples, but sends the reader back to page 8 to understand why its prescribed branch intensity is attainable. The question about a global radius-band choice excluding shapes is answered naturally in page 8, lines 164–166; it needs no additional repair.

## Comprehension answers

1. **What is established? — Stated.** Page 2, lines 33–45, asserts existence for every prescribed positive pair (λ₀, M), with construction-chosen positive coefficients and exact identities on nondegenerate tuples of diameter below M. Global regularity remains required outside that domain. S0 is excluded, S1 is accepted after reviews, and S2 was never adopted (lines 43–51). The opening promise matches this scope; “accepted” is explicitly qualified on page 1.

2. **How do the components produce the three laws? — Stated, with elementary algebra recoverable.** Separation makes each local tuple belong to one surface or cluster. The sphere process supplies the fourth law and smaller pair/triple densities; clusters supply their deficits. A single global fair coin averages the full factorial measures (pages 8–9, lines 174–208). Adding the displayed densities and dividing by two recovers all three final coefficients without additional theory.

3. **Why is arbitrary intensity possible? — Stated, but the parameter-feasibility link is missing from this account.** Page 9, lines 203–210, assigns a small positive intensity to C and the remainder to Y. Page 8, line 179, says Y’s intensity can be fixed independently of L; page 9, line 199, says increasing L makes correction budgets fit. The text does not explain how those choices also realise the required sphere sampling probabilities.

## Highest-impact repairs

- **Pages 8–9, lines 164–179 and 199–203:** connect the parameter choices explicitly. The reader currently has to supply the link between the geometric sampling description, γ(R), and the all-intensity conclusion. State the order of choices, how K and c give the desired λ_Y, and why sufficiently large L leaves valid thinning probabilities while reducing correction costs. A short dependency paragraph, with a precise proof locator, would suffice; the full estimates need not be reproduced.

- **Page 9, line 199:** define what “kernel” means relative to the ordered factorial-density convention of page 2. Neither κ nor the factorial multiplicities appear in the conversion from F₂/F₃ to cluster probabilities, although that conversion is what makes this a process construction. Give the normalization convention and one short explanation of why marginalizing a three-point cluster contributes exactly Mq₃ to the pair density. This is an explanatory omission, not an identified incorrect coefficient.

- **Page 10, line 229:** define R*, z and dω explicitly, especially whether dω is unit-sphere area or probability measure. The power of R and constant 48 are otherwise difficult to follow from the stated prerequisites. The preceding description already supplies the geometric motivation.

- **Timing clarification, not a mathematical defect:** page 4, line 84, dates freezing P4’s fourth submission at 19:15:12, while page 13, line 330, starts its reviewer at 19:14:57. Explain whether the earlier interval was reviewer preflight or whether “frozen” denotes a later administrative checkpoint. The current presentation leaves the frozen-proof dispatch sequence ambiguous.

No specific mathematical defect was identified within this exposition review. Any inserted normalization or feasibility claim should be checked against the cited proof. For economy, label the detailed session and turn tables as an appendix from page 12 onward: page 11 already gives the aggregate interpretation, and the additional tables mainly serve audit and lookup.
