# Agent instruction index

This is the human-readable entry point for the files that controlled the
research team. The exact executable configuration is in `codex/`, while the
long-form role protocols are in `role-instructions/`.

## Governing order

1. Read [`AGENTS.md`](AGENTS.md) for the target, isolation rules, evidence
   standard and output policy.
2. Read [`workflow.json`](workflow.json) for roles, context packets, stage order,
   concurrency, repair rounds and artifact paths.
3. Read [`role-instructions/coordinator.md`](role-instructions/coordinator.md)
   before launching any model work.
4. Freeze the exact problem and common inputs before the literature pass.
5. Give each proof agent only the common packet and its own approach assignment.
6. Review frozen submissions in fresh contexts, route scoped findings back only
   to the relevant author, and preserve every version.
7. Finish with a comparative review that states exact scope and unresolved gaps.

## Role instructions

- [`coordinator.md`](role-instructions/coordinator.md) — initialization,
  dispatch, freezing, repair routing and final synthesis.
- [`literature_agent.md`](role-instructions/literature_agent.md) — one shared
  source dossier for all proof tracks.
- [`proof_agent.md`](role-instructions/proof_agent.md) — common proof standard
  for all five independent approaches.
- [`reviewer.md`](role-instructions/reviewer.md) — adversarial review of frozen
  submissions and final comparison.
- [`coder.md`](role-instructions/coder.md) — reproducible checks requested by a
  reviewer; numerical agreement is not an exact proof.

The individual approach assignments are published under `../../problem/`.
The custom role definitions are under `codex/agents/`.

## Non-negotiable safeguards

- Exact full product densities are not connected densities or same-cluster
  contributions.
- A selected intensity is not the same as arbitrary prescribed intensity.
- Finite grids and simulations do not prove continuum identities.
- Proof agents do not read one another's new work.
- Reviewer contexts exclude author conversations and private work notes.
- The workflow records structured reasoning summaries and decisions, never raw
  private chain-of-thought.
- If the requested model is unavailable, stop instead of silently substituting
  another model.
