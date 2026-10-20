# Reciprocal-simplex agentic research experiment

This folder publishes the agent architecture and the auditable outputs from the
completed reciprocal-simplex point-process research run
`20261019T114252Z_cox_rerun`.

The run used one coordinator, one literature agent, five independent proof
tracks, separate critical-review passes, and a final synthesis reviewer. Every
role was configured for `gpt-5.6-sol` with `xhigh` reasoning, with no model
fallback. Fresh context packets and file-level hashes were used to separate the
proof tracks and preserve the reviewed versions.

## Start with these files

- [`agent-files/reciprocal-simplex-research/AGENTS.md`](agent-files/reciprocal-simplex-research/AGENTS.md) — project-wide rules.
- [`agent-files/reciprocal-simplex-research/instructions.md`](agent-files/reciprocal-simplex-research/instructions.md) — readable index to the coordinator and role instructions.
- [`agent-files/reciprocal-simplex-research/SKILL.md`](agent-files/reciprocal-simplex-research/SKILL.md) — reusable workflow entry point.
- [`architecture/research_agent_configuration.pdf`](architecture/research_agent_configuration.pdf) — architecture diagram.
- [`results/reasoning_summaries_and_audit.pdf`](results/reasoning_summaries_and_audit.pdf) — compiled reasoning summaries, decision records, provenance, runtime and token accounting.
- [`results/final_review_report.md`](results/final_review_report.md) — final mathematical synthesis.

## Directory map

```text
reciprocal-simplex-agentic-research/
├── agent-files/reciprocal-simplex-research/
│   ├── AGENTS.md
│   ├── instructions.md
│   ├── SKILL.md
│   ├── START.md
│   ├── workflow.json
│   ├── codex/                 # model and custom-role configuration
│   ├── role-instructions/     # coordinator, proof, review, literature, coder
│   └── templates/             # submission and review schemas
├── architecture/              # PDF, PNG and editable draw.io diagram
├── problem/                   # exact target and five approach assignments
└── results/
    ├── reasoning_summaries_and_audit.pdf
    ├── final_review_report.md
    ├── token_accounting.md
    ├── run_manifest_public.json
    ├── status.json
    ├── submissions/           # latest frozen proof submissions
    ├── reviews/               # latest frozen critical reviews
    └── literature/            # shared source dossier and open questions
```

## Mathematical status

The governing target required exact full normalized product densities
`g_2`, `g_3`, and `g_4` on their complete stated domains for every prescribed
positive intensity. That target remains unresolved.

The strongest reviewed positive result is an exact construction on the full
domains, including no positive lower pair cutoff, for every prescribed
intensity in a nonempty geometry-dependent interval beginning at zero. No
general construction or impossibility theorem was established above that
interval.

## What “reasoning summaries” means

The published material contains the structured reasoning summaries and
decision records that the workflow required each proof and review artifact to
save. It does **not** contain raw private chain-of-thought. The reported
reasoning-token counts measure usage, not a recoverable text transcript.

## Public-release scope

This bundle contains agent-generated configuration, mathematical submissions,
reviews, audit records and diagrams. It intentionally excludes the copied
third-party paper PDFs, private local paths, transient working notes, hidden
runtime traces and unrelated manuscript material. Historical source claims in
the dossier remain subject to the qualifications recorded there.
