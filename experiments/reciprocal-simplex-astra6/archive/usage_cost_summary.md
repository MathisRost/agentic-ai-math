# Usage and cost record

Snapshot: 2026-10-20T19:46:54.126268+00:00

These are measured runtime counters for explicitly registered sessions and turns. Completed turns are distinguished from active snapshots. Input counts include repeated context and tool inputs as reported by the runtime. Cached input is a reported subset, and reasoning is already included in output. Counts are differences of successive distinct cumulative counters, not sums of snapshots.

Parent/child inclusion semantics are unverified. Accordingly, no cross-session grand total is asserted. API-equivalent estimates, applicable service-tier pricing and actual account charges are **NR**. No word-count estimate is substituted for measured tokens. Source evidence, timestamps, complete session/turn IDs and artifact hashes are in `agent_accounting.jsonl` and `preflight/telemetry/`.

The compact table groups nonoverlapping turns within each single identified agent session. It does not aggregate across sessions. A partial session has an in-flight turn whose later usage is absent from this snapshot.

| Agent role | Turns | Input | Cached input | Output | Reasoning (within output) | Total | Actual charge | Coverage |
|---|---:|---:|---:|---:|---:|---:|---|---|
| coordinator | 1 | 48,252,029 | 47,603,712 | 167,301 | 60,898 | 48,419,330 | NR | partial |
| nonexistence_1 | 3 | 1,436,832 | 1,270,784 | 29,038 | 9,401 | 1,465,870 | NR | complete |
| nonexistence_2 | 2 | 714,417 | 670,976 | 13,316 | 3,481 | 727,733 | NR | complete |
| review_nonexistence_1_v01 | 1 | 755,997 | 698,368 | 13,303 | 2,757 | 769,300 | NR | complete |
| review_nonexistence_2_v01 | 1 | 632,594 | 590,464 | 13,437 | 3,149 | 646,031 | NR | complete |
| review_nonexistence_1_v02 | 1 | 826,611 | 776,704 | 13,942 | 2,964 | 840,553 | NR | complete |
| proof_1 | 4 | 4,953,497 | 4,415,232 | 112,387 | 61,282 | 5,065,884 | NR | complete |
| proof_2 | 1 | 1,430,149 | 1,339,264 | 18,928 | 7,543 | 1,449,077 | NR | complete |
| proof_3 | 4 | 5,798,102 | 5,246,080 | 109,965 | 58,245 | 5,908,067 | NR | complete |
| proof_4 | 4 | 6,563,725 | 6,124,416 | 140,802 | 76,686 | 6,704,527 | NR | complete |
| review_proof_2_v01 | 1 | 991,018 | 921,984 | 16,103 | 3,604 | 1,007,121 | NR | complete |
| review_proof_1_v01 | 1 | 962,759 | 907,904 | 15,839 | 4,242 | 978,598 | NR | complete |
| review_proof_3_v01 | 1 | 1,132,796 | 1,070,976 | 15,188 | 3,771 | 1,147,984 | NR | complete |
| review_proof_4_v01 | 1 | 644,410 | 596,864 | 15,173 | 4,747 | 659,583 | NR | complete |
| review_proof_1_v02 | 1 | 1,238,864 | 1,156,480 | 18,570 | 4,491 | 1,257,434 | NR | complete |
| review_proof_4_v02 | 1 | 1,193,112 | 1,120,896 | 16,663 | 2,520 | 1,209,775 | NR | complete |
| review_proof_3_v02 | 1 | 1,173,060 | 1,096,960 | 16,374 | 3,488 | 1,189,434 | NR | complete |
| review_proof_1_v03 | 1 | 1,362,513 | 1,275,008 | 18,906 | 4,263 | 1,381,419 | NR | complete |
| review_proof_3_v03 | 1 | 1,748,658 | 1,660,928 | 17,301 | 2,986 | 1,765,959 | NR | complete |
| review_proof_4_v03 | 1 | 1,178,572 | 1,102,592 | 16,063 | 1,293 | 1,194,635 | NR | complete |
| literature | 1 | 3,373,806 | 3,241,344 | 21,646 | 3,554 | 3,395,452 | NR | complete |
| review_proof_3_v04 | 1 | 2,361,509 | 2,253,952 | 19,456 | 2,381 | 2,380,965 | NR | complete |
| review_proof_1_v04 | 1 | 1,396,668 | 1,301,760 | 21,021 | 4,963 | 1,417,689 | NR | complete |
| review_proof_4_v04 | 1 | 1,579,252 | 1,443,968 | 19,897 | 4,597 | 1,599,149 | NR | complete |
| final_synthesis | 1 | 6,460,609 | 6,144,768 | 35,996 | 6,500 | 6,496,605 | NR | complete |

## Per-turn measured detail

| Role | Turn | Target / submission | Input | Cached input | Cache write | Output | Reasoning (within output) | Total | Coverage |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| coordinator | 01a15a31-8d43 | S0 / — | 48,252,029 | 47,603,712 | 0 | 167,301 | 60,898 | 48,419,330 | active snapshot |
| nonexistence_1 | 01a15a33-8e1e | NR / — | 147,813 | 107,648 | 0 | 1,972 | 234 | 149,785 | complete |
| nonexistence_1 | 01a15a35-4bea | S0 / 1 | 622,532 | 591,872 | 0 | 12,823 | 4,220 | 635,355 | complete |
| nonexistence_1 | 01a15a42-7087 | S0 / 2 | 666,487 | 571,264 | 0 | 14,243 | 4,947 | 680,730 | complete |
| nonexistence_2 | 01a15a33-b630 | NR / — | 147,810 | 135,680 | 0 | 1,370 | 24 | 149,180 | complete |
| nonexistence_2 | 01a15a35-748f | S0 / 1 | 566,607 | 535,296 | 0 | 11,946 | 3,457 | 578,553 | complete |
| review_nonexistence_1_v01 | 01a15a3b-8c71 | S0 / 1 | 755,997 | 698,368 | 0 | 13,303 | 2,757 | 769,300 | complete |
| review_nonexistence_2_v01 | 01a15a3b-ebf4 | S0 / 1 | 632,594 | 590,464 | 0 | 13,437 | 3,149 | 646,031 | complete |
| review_nonexistence_1_v02 | 01a15a49-3223 | S0 / 2 | 826,611 | 776,704 | 0 | 13,942 | 2,964 | 840,553 | complete |
| proof_1 | 01a15a50-bd1f | S1 / 1 | 1,592,849 | 1,470,592 | 0 | 23,961 | 10,677 | 1,616,810 | complete |
| proof_1 | 01a15a67-e4ff | S1 / 2 | 1,262,064 | 1,132,672 | 0 | 24,067 | 12,024 | 1,286,131 | complete |
| proof_1 | 01a15a7b-c144 | S1 / 3 | 1,255,566 | 1,058,432 | 0 | 28,287 | 15,261 | 1,283,853 | complete |
| proof_1 | 01a15a93-94d3 | S1 / 4 | 843,018 | 753,536 | 0 | 36,072 | 23,320 | 879,090 | complete |
| proof_2 | 01a15a50-e8cf | S1 / 1 | 1,430,149 | 1,339,264 | 0 | 18,928 | 7,543 | 1,449,077 | complete |
| proof_3 | 01a15a51-1565 | S1 / 1 | 1,822,445 | 1,723,264 | 0 | 22,488 | 8,835 | 1,844,933 | complete |
| proof_3 | 01a15a6a-6ceb | S1 / 2 | 1,970,009 | 1,825,792 | 0 | 32,370 | 19,483 | 2,002,379 | complete |
| proof_3 | 01a15a80-5d36 | S1 / 3 | 1,054,235 | 846,336 | 0 | 28,677 | 15,342 | 1,082,912 | complete |
| proof_3 | 01a15a96-b332 | S1 / 4 | 951,413 | 850,688 | 0 | 26,430 | 14,585 | 977,843 | complete |
| proof_4 | 01a15a59-9910 | S1 / 1 | 1,403,102 | 1,312,384 | 0 | 22,925 | 10,311 | 1,426,027 | complete |
| proof_4 | 01a15a6b-9837 | S1 / 2 | 1,520,564 | 1,477,120 | 0 | 28,801 | 15,437 | 1,549,365 | complete |
| proof_4 | 01a15a80-81c1 | S1 / 3 | 1,645,090 | 1,438,464 | 0 | 40,268 | 23,631 | 1,685,358 | complete |
| proof_4 | 01a15a9e-5c35 | S1 / 4 | 1,994,969 | 1,896,448 | 0 | 48,808 | 27,307 | 2,043,777 | complete |
| review_proof_2_v01 | 01a15a5b-f574 | S1 / 1 | 991,018 | 921,984 | 0 | 16,103 | 3,604 | 1,007,121 | complete |
| review_proof_1_v01 | 01a15a60-20f3 | S1 / 1 | 962,759 | 907,904 | 0 | 15,839 | 4,242 | 978,598 | complete |
| review_proof_3_v01 | 01a15a62-f6bd | S1 / 1 | 1,132,796 | 1,070,976 | 0 | 15,188 | 3,771 | 1,147,984 | complete |
| review_proof_4_v01 | 01a15a64-84e2 | S1 / 1 | 644,410 | 596,864 | 0 | 15,173 | 4,747 | 659,583 | complete |
| review_proof_1_v02 | 01a15a72-82aa | S1 / 2 | 1,238,864 | 1,156,480 | 0 | 18,570 | 4,491 | 1,257,434 | complete |
| review_proof_4_v02 | 01a15a79-1343 | S1 / 2 | 1,193,112 | 1,120,896 | 0 | 16,663 | 2,520 | 1,209,775 | complete |
| review_proof_3_v02 | 01a15a79-415a | S1 / 2 | 1,173,060 | 1,096,960 | 0 | 16,374 | 3,488 | 1,189,434 | complete |
| review_proof_1_v03 | 01a15a8b-8ae6 | S1 / 3 | 1,362,513 | 1,275,008 | 0 | 18,906 | 4,263 | 1,381,419 | complete |
| review_proof_3_v03 | 01a15a8e-b2e1 | S1 / 3 | 1,748,658 | 1,660,928 | 0 | 17,301 | 2,986 | 1,765,959 | complete |
| review_proof_4_v03 | 01a15a95-1d82 | S1 / 3 | 1,178,572 | 1,102,592 | 0 | 16,063 | 1,293 | 1,194,635 | complete |
| literature | 01a15aa2-8367 | S1 / — | 3,373,806 | 3,241,344 | 0 | 21,646 | 3,554 | 3,395,452 | complete |
| review_proof_3_v04 | 01a15aa3-2998 | S1 / 4 | 2,361,509 | 2,253,952 | 0 | 19,456 | 2,381 | 2,380,965 | complete |
| review_proof_1_v04 | 01a15aab-66c8 | S1 / 4 | 1,396,668 | 1,301,760 | 0 | 21,021 | 4,963 | 1,417,689 | complete |
| review_proof_4_v04 | 01a15abc-fde9 | S1 / 4 | 1,579,252 | 1,443,968 | 0 | 19,897 | 4,597 | 1,599,149 | complete |
| final_synthesis | 01a15ac6-2b55 | S1 / — | 6,460,609 | 6,144,768 | 0 | 35,996 | 6,500 | 6,496,605 | complete |

The coordinator turn spans S0 and S1; its initial target label identifies the launch rather than allocating every token to S0. Research/preflight boundaries are retained separately in each applicable JSONL record. Boundary allocation uses event timestamps and does not split an individual model call. The final in-flight coordinator response cannot be measured from a preceding snapshot. Earlier project-setup sessions are excluded.

All registered mathematical roles are required to verify `gpt-6-astra` with `xhigh` effort before mathematics. Verification is attached to each turn record. This accounting file does not certify mathematical correctness; the independent reviews and attempt ledger record those judgements.
