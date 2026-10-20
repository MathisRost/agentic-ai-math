# Recovered token accounting

This is a post-run administrative addendum. It does not modify any frozen
mathematical submission, review, or final report.

The collaboration interface did not expose token usage during the run, so
`agent_accounting.md` correctly recorded those live fields as `NR`. After the
run, cumulative `token_count` events were located in the owner's local Codex
rollout traces. The private machine-specific trace path is omitted here.

## Extraction rule

For every JSONL rollout whose `session_meta.agent_path` begins with
`/root/coordinator_rerun_cox`, take the final cumulative
`event_msg.payload.info.total_token_usage` object. Eighteen agent sessions
matched. In addition, isolate the parent chat's cumulative-usage delta between
the rerun request at `2026-10-19T11:39:10.882Z` and the next user message at
`2026-10-19T15:26:16.735Z`. Other root/user sessions that merely mentioned the
run ID were excluded.

The trace schema counts cached input inside `input_tokens`, and reasoning output
inside `output_tokens`. Thus the columns below are not additive across a row:

- uncached input = input - cached input;
- reasoning is a subset of output;
- total = input + output.

## Runtime and token table

| Agent / session | Runtime | Input | Cached input | Uncached input | Output | Reasoning output | Total | Standard API-equivalent cost |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Parent chat supervision and setup | 03:47:06 | 40,895,045 | 40,731,008 | 164,037 | 23,758 | 6,445 | 40,918,803 | $17.42 |
| Coordinator | 03:36:43 | 24,180,539 | 23,891,712 | 288,827 | 65,809 | 8,141 | 24,246,348 | $12.03 |
| Literature | 00:18:35 | 11,506,253 | 11,102,848 | 403,405 | 43,730 | 14,489 | 11,549,983 | $6.93 |
| Proof 1, Poisson cluster, v01 + repair | 00:21:47 | 7,190,086 | 6,714,112 | 475,974 | 53,236 | 25,732 | 7,243,322 | $5.65 |
| Proof 2, Cox, v01 + repair | 00:23:43 | 6,615,750 | 6,327,296 | 288,454 | 63,742 | 33,688 | 6,679,492 | $4.96 |
| Proof 3, Hawkes, v01 + repair | 00:22:05 | 6,999,088 | 6,700,800 | 298,288 | 64,778 | 31,021 | 7,063,866 | $5.17 |
| Proof 4, agent-selected, attempts + repair | 00:25:48 | 9,901,952 | 9,583,616 | 318,336 | 63,413 | 30,885 | 9,965,365 | $6.38 |
| Proof 5, necessary conditions, v01 + repair | 00:20:41 | 5,357,915 | 5,105,024 | 252,891 | 62,141 | 28,514 | 5,420,056 | $4.30 |
| Reviewer 1 v01 | 00:07:27 | 976,300 | 900,736 | 75,564 | 19,118 | 9,206 | 995,418 | $1.04 |
| Reviewer 1 v02 delta | 00:04:56 | 1,457,007 | 1,384,832 | 72,175 | 15,586 | 7,578 | 1,472,593 | $1.15 |
| Reviewer 2 v01 | 00:08:35 | 1,888,810 | 1,783,296 | 105,514 | 21,029 | 10,503 | 1,909,839 | $1.56 |
| Reviewer 2 v02 delta | 00:04:48 | 771,662 | 700,928 | 70,734 | 15,082 | 8,170 | 786,744 | $0.86 |
| Reviewer 3 v01 | 00:07:22 | 1,401,334 | 1,296,128 | 105,206 | 20,143 | 10,414 | 1,421,477 | $1.34 |
| Reviewer 3 v02 delta | 00:06:12 | 1,377,263 | 1,294,592 | 82,671 | 18,999 | 6,391 | 1,396,262 | $1.23 |
| Reviewer 4 v01 | 00:07:31 | 1,270,065 | 1,180,416 | 89,649 | 23,214 | 13,468 | 1,293,279 | $1.30 |
| Reviewer 4 v02 delta | 00:05:18 | 887,457 | 827,520 | 59,937 | 16,973 | 7,949 | 904,430 | $0.91 |
| Reviewer 5 v01 | 00:08:51 | 2,395,333 | 2,293,632 | 101,701 | 24,854 | 13,807 | 2,420,187 | $1.82 |
| Reviewer 5 v02 delta | 00:06:36 | 741,233 | 672,512 | 68,721 | 19,415 | 10,924 | 760,648 | $0.93 |
| Final synthesis reviewer | 00:10:10 | 6,053,589 | 5,838,464 | 215,125 | 31,685 | 9,134 | 6,085,274 | $3.83 |
| **All recorded model sessions** | **03:47:06 task-turn envelope** | **131,866,681** | **128,329,472** | **3,537,209** | **666,705** | **286,459** | **132,533,386** | **$78.81** |

The parent task turn includes initial setup revision and final verification. The
coordinator's research-run envelope itself is `03:36:43`. Both overlap all
delegated runtimes, so runtime values must not be added as though they were
serial.

## Cost interpretation

The displayed cost applies the pricing snapshot frozen at run start:

- $4.00 per million uncached input tokens;
- $0.40 per million cached input tokens;
- $20.00 per million output tokens.

The computation is

\[
3.537209\times4 + 128.329472\times0.4 + 0.666705\times20
= 78.8143896\text{ USD}.
\]

The traces report service tier `default`. This is an API-equivalent model-cost
calculation, not evidence of a separate charge to the user's Codex subscription.
No third-party or local-compute charges are included.
