# Token accounting

Latest collection: 2026-10-21T06:46:58.298018+00:00.

| Role / turn | Input | Cached input | Output | Reasoning (included) | Total | Turn complete |
|---|---:|---:|---:|---:|---:|---|
| coordinator / 21c1ea36 | 10,699,569 | 10,437,760 | 36,515 | 12,742 | 10,736,084 | False |
| writer / 4156dca3 | 1,511,276 | 1,400,320 | 25,314 | 1,989 | 1,536,590 | True |
| writer / a27eec0d | 1,052,669 | 1,038,208 | 4,818 | 810 | 1,057,487 | True |
| coder / 89927020 | 2,936,776 | 2,855,296 | 38,566 | 10,123 | 2,975,342 | True |
| reader / d8a38927 | 792,138 | 719,360 | 9,139 | 3,071 | 801,277 | True |

Counts are runtime measurements, obtained as differences between successive distinct cumulative checkpoints within each explicitly registered session. Cached input is included in input; reasoning is included in output. Input includes repeated contexts and tool responses. These are not manuscript word counts.

Cross-session parent/child aggregation semantics are NR, so no billing grand total is asserted. Estimates and actual charges are NR. The active coordinator response and any tokens after the last observed checkpoint are not included. Completion events and counters may arrive asynchronously.

The preparation boundary is in preflight/coordinator.json and accounting_capability.json; delegated boundaries are in each role/preflight.json. The ledger includes preparation and writing, rather than silently excluding preparation. Metadata event timestamps permit separate inspection; no unsupported per-request phase attribution is asserted.

Only turn/model/token metadata were extracted. No private deliberation transcript is recorded. Explicit proofs and concise decisions are separate artifacts.
