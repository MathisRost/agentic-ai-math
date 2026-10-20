---
name: reciprocal-simplex-research
description: Run or audit the published multi-agent reciprocal-simplex point-process research workflow, preserving exact quantifiers, independent proof tracks, frozen artifacts, and scoped mathematical verdicts.
---

# Reciprocal-simplex research workflow

Use this skill only for the exact point-process problem published with this
bundle or for a deliberately adapted research run whose governing target is
supplied explicitly. Creating or editing these files is not authorization to
launch agents; begin model work only after the owner explicitly requests a run.

## Required inputs

Read, in order:

1. [`AGENTS.md`](AGENTS.md).
2. [`workflow.json`](workflow.json).
3. [`instructions.md`](instructions.md) and the linked coordinator protocol.
4. The exact problem statement and the relevant approach assignments under
   `../../problem/`.

Verify the requested model and reasoning effort before dependent work. Do not
silently substitute another model.

## Run shape

Create a new run directory and freeze the common inputs with hashes. Dispatch
one literature pass first and freeze its dossier. Then dispatch independent
proof tracks in fresh contexts that receive the common packet plus only their
own assignment. Require self-contained versioned submissions with a structured
reasoning summary and decision record.

Review each frozen submission in a fresh reviewer context without the author's
conversation or work notes. Route actionable findings only to the relevant
author, preserve earlier versions, and complete the configured repair rounds.
Use reproducible code only for a specific reviewer-requested check; save code,
parameters, seeds, versions, raw output and uncertainty, and never treat
numerical agreement as proof of an exact identity.

Finish with an extensive comparison that distinguishes:

- the complete target;
- a restricted exact theorem;
- a conditional result or unresolved gap;
- a class-specific obstruction;
- a general obstruction; and
- literature non-discovery.

## Mathematical invariants

Preserve all definitions, quantifiers and domains in the governing problem.
Work with full factorial/product densities, including every partition
contribution. Prove the process law, stationarity, simplicity, local finiteness,
the prescribed intensity, finite local moments, density existence and the exact
identities on the complete requested domains. Do not infer unrestricted claims
from approximate fits, finite grids, selected intensities or subclass failures.

## Audit and privacy boundary

Record model selection, timestamps, wall time, artifact paths, hashes and every
usage field the runtime exposes. Use `NR` rather than inventing unavailable
values. Preserve structured reasoning summaries and decision records, not raw
private chain-of-thought. A reasoning-token count is usage metadata, not a text
transcript.

Do not publish copied source papers, credentials, private local paths, transient
runtime traces or unrelated user material when exporting a run.
