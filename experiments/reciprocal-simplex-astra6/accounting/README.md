# Accounting scope

`agents.json` / `agents.csv` contain 25 per-session records.
`turns.json` / `turns.csv` contain 37 per-turn records.
The [frozen original ledger](../archive/agent_accounting.jsonl) preserves fields
such as coverage, phase boundaries and artifact hashes. Sanitised
[numeric telemetry](../archive/preflight/telemetry/) supports the measurements;
it contains no message or private reasoning text.

Input includes cached input. Output includes reasoning output. Do not add either
subset again. The collector grouped differences between successive distinct
cumulative counters by turn, rather than summing cumulative snapshots. All
registered roles verified `gpt-6-astra / xhigh`. Reported cache-write counters
were zero. Missing fields use JSON null or NR, never invented numbers.

The snapshot was collected at 2026-10-20T19:46:54.126268 UTC. Coordinator tokens
extend through 19:46:32.086 UTC, before its final-response tail. All 36 delegated
turns were complete. Preflight is included; original per-phase splits remain in
the ledger where available. Later discussion and documentation are excluded.

## Runtime

`boundaries.json` defines the research start, completion and total wall time.
Per-turn elapsed seconds are runtime measurements, including tool waits.
Per-agent turn time is their arithmetic sum, excluding between-turn gaps.
Parallel durations overlap. These are not CPU/GPU timings. Coordinator
completed-turn duration is NR. The UTC timestamps and millisecond durations
come from different runtime fields, so subtracting rounded timestamps can
differ slightly from the duration value.

## Dollar scenarios

The [saved cost calculation](../archive/followups/20261020_cost_estimate_v01/cost_estimate.json)
applied official GPT-6-Astra short-context prices retrieved on 20 October 2026:

| Scenario | Uncached input / million | Cached input / million | Output / million |
|---|---:|---:|---:|
| Standard | $10 | $1 | $50 |
| Fast / priority | $20 | $2 | $100 |

Source: [official model documentation](https://developers.openai.com/api/docs/models/gpt-6-astra).
Pricing was checked after completion on the same date, not frozen at launch.
The maximum recorded call input was 237,725, below the 272,000 threshold.

Standard estimate = `((input - cached) * 10 + cached + output * 50) / 1,000,000`.
Exact decimal per-role estimates are stored as strings. Their raw arithmetic sum
is $181.154884; the alternative double-rate sum is $362.309768. Rounded displayed
rows need not sum to the rounded grand scenario.

**Parent/child inclusion semantics are unverified.** These sums assume disjoint
session counters; they are not a deduplicated experiment bill. The user recalled
Fast was off, but the runtime did not establish the actual billed tier. Actual
charges are NR. Subscription charges cannot be inferred from these estimates.
Tool fees, taxes, regional uplifts, the missing coordinator tail and later work
are excluded. `pricing.json` retains the assumptions in machine-readable form.
