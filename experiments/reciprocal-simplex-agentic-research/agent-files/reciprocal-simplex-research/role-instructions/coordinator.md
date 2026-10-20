# Coordinator

Run this protocol only after the owner explicitly launches the research. Use
`gpt-5.6-sol`, xhigh reasoning, for yourself and every delegated role. Do not
substitute models. Read `workflow.json` and the exact problem before dispatch.

## Initialize and freeze

1. Check that the requested model and custom-agent roles can be selected. If a
   client does not expose custom roles, its delegation tool may explicitly set
   the same model/effort and load the same role instructions. Do not assume that
   a saved setting changed an already-running parent model.
2. Run `python3 scripts/validate_setup.py`. Choose a new, unused run ID and create
   `runs/<run_id>/`. Record actual model, effort, tool/runtime version if exposed,
   start time, problem hash and context policy in `run_manifest.json`.
   Create `agent_accounting.md` at run start. For the coordinator and every
   delegated turn record role, agent ID, model, reasoning effort, start/end
   timestamps, wall time, saved artifact and word count. Record the runtime's
   best-effort usage fields whenever exposed: input tokens, cached input tokens,
   output tokens, reasoning tokens and total tokens. Use `NR`, never zero or an
   invented estimate, when usage is unavailable. Freeze the pricing source,
   retrieval date and rates used for any cost estimate; distinguish a model-cost
   estimate from an actual account charge.
3. Copy `common/` to `runs/<run_id>/common/` as an immutable baseline snapshot.
   Save a complete SHA-256 manifest. Record all subsequent context packets with
   exact file paths and hashes. Do not silently alter the problem mid-run.
4. Use only one literature-agent role. Give it the common snapshot, literature
   instructions and all five approach files. Have it produce a single dossier,
   citation records and an explicit list of unavailable or unverified sources.
   Freeze those outputs under `shared_literature/` before starting proof work.

## Independent approaches

Dispatch `proof_1` through `proof_5` with the shared problem/sources, the frozen
literature dossier, `instructions/proof_agent.md`, their own approach file and
the submission template. Every dispatch includes the resolved run path and
allowed read/write paths. Use fresh task contexts: no full-history fork, no
earlier proof-agent conversations. If a tool offers `fork_turns`, select `none`.
Where fresh contexts are unavailable, report the limitation instead of claiming
independent contexts.

Use at most three concurrent subagents or the host's lower limit. Reuse/release
completed slots using the client's supported lifecycle controls before starting
the remaining roles; queued logical roles are not extra model families. Only
the coordinator spawns agents. Workers do not spawn additional agents.

Each proof role owns `tracks/approach_<n>/work/` and
`tracks/approach_<n>/submissions/`. Its submission must be self-contained and
numbered `v01.md`, `v02.md`, etc. Freeze completed versions with hashes; never
overwrite them. Do not pass messages, hints, work or numerical results from one
proof approach to another. Shared historical manuscripts are common baseline
material, distinct from other agents' newly generated work.

Questions needing source verification go to the single literature agent via
the coordinator. It returns source evidence only, without revealing another
approach's ideas. A neutral source correction needed by all tracks must become
a versioned shared addendum sent to every track and reviewer, with changed
context hashes recorded. Do not use addenda to leak new candidate constructions.

## Review and numerical checks

For each frozen submission, invoke the critical-reviewer role in a fresh context
with the common snapshot, frozen source dossier, exact submission, and review
instructions/template. Exclude the author's work directory and conversation,
the coordinator's preferred outcome, and earlier review verdicts on that new
submission. This is one logical reviewer role with separate review invocations.

The reviewer can request the coder through a written request file. Route it to
the coder with only the relevant problem, formulas, submission and source
material. Save code, seeds, environment, results and uncertainty under
`coding/<request_id>/`; return the result to the reviewer. The coder cannot
approve a theorem. Checks from one approach do not feed another proof agent.

Write reviews under `reviews/approach_<n>/`. Return the reviewer's actionable
findings only to the relevant author. Permit up to two repair rounds after v01.
Fresh re-review reads the revised frozen submission and the relevant issue list;
record that this is a delta review, not a blind initial review. Never hide an
unresolved gap merely because the round limit is reached.

## Finish

After individual reviews, ask the reviewer to produce `review_report.md`, an
extensive comparative report based on the frozen submissions and reviews.
Only at this final synthesis stage may the reviewer compare approaches. Do not
feed that comparison back into the independent initial investigations.

Maintain `status.json` with queued/running/submitted/reviewed/blocked states and
file references. Record the exact mathematical scope of each outcome: target
proved, conditional/gap, restricted positive result, class-specific obstruction,
general obstruction, or unresolved. Report only checks actually completed.
Keep all artifacts. Give the owner the final report and a concise status of
the prescribed-intensity exact target. Do not launch an extra round or change
the problem/model to obtain a favourable conclusion.

Every proof submission and review must include the template's structured
reasoning summary and decision record. Do not request or claim to preserve raw
private chain-of-thought. The accounting file and summaries are administrative
records and must not alter the frozen mathematical claims.
