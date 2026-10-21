# Usage and research-accounting rules

## Preflight before research

Inspect only this run's available telemetry, documented tool fields and
explicitly identified session records. Do not browse other chats, credentials
or private reasoning transcripts. A usage percentage is not a per-agent token
count. Determine whether per-agent/per-turn input, cached input, output,
reasoning and total tokens are exposed, and whether parent totals include
children. Record the evidence and scope in `accounting_capability.json`.

If exact per-agent token telemetry is unavailable, tell the owner BEFORE the
substantive run and ask whether to proceed with NR fields and labelled estimates.
The launch prompt requires this gate. Do not buy or switch to an API workflow
just to obtain accounting. Account access and token exposure remain untested
when a setup is only prepared.

## Ledger

Use `templates/accounting_record.json` for one JSONL record per agent turn,
plus final reconciliations. Record:

- run ID, role, agent/session/turn IDs, attempt and statement version;
- requested and verified model/effort, source of verification;
- start/end timestamps in UTC, elapsed seconds;
- runtime-reported input, cached-input, output, reasoning and total tokens;
- cumulative vs incremental semantics and whether child usage is included;
- source event/reference, coverage, missing fields;
- produced artifact paths, hashes and word counts;
- status, estimates if separately requested, and estimate method/uncertainty.

Unknown is `null` in JSON and `NR` in human tables, never zero. Do not add
reasoning tokens to output tokens when output already includes them. Do not
add child totals to an inclusive parent total. For cumulative telemetry use
documented differences between matching checkpoints, not a sum of snapshots.
Input accounting includes tool/context/repeated inputs where the runtime does;
document length does not reconstruct these.

Keep an explicit research-preparation boundary. This setup's configuration
work is not an agent research attempt and is not silently charged to the new
run. Later preflight and research costs should be distinguishable.

## Cost

Freeze the official pricing page, retrieval date, exact model, service tier,
context-length band and applicable rates when computing an API-equivalent
estimate. Recheck prices at launch; `setup_audit/model_configuration.md` is a
configuration reference, not a future invoice.

For simple telemetry, uncached input is total input minus cached input only
when that field's documented semantics permit it. Account for separately
reported cache-write categories, context multipliers and tool fees if used.
Reasoning/output overlap must not be double billed in the calculation.
If tier/cache semantics or fields are unknown, report a partial calculation or
range rather than a false exact dollar total. Subscription usage is not an
API invoice. Clearly distinguish measured tokens, estimated model cost and
actual account charge.

An owner-approved rough estimate may use documented visible-text tokenisation
or explicit scenario assumptions, but must state that hidden reasoning,
context reuse and tool inputs cannot be reconstructed. Never turn word counts
into an allegedly measured token total.

## Reasoning documentation

Save explicit human-readable mathematical proofs and concise summaries of
approaches, assumptions, decisive checks, failed routes at a high level,
review responses, decisions and unresolved obligations. Do not request, save
or claim access to raw private chain-of-thought. A complete mathematical proof
is welcome and is different from a private deliberation transcript.
