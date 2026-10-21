# Coordinator protocol

Preparation is not launch. Execute this workflow only after the owner sends
START in the new project. Use `gpt-6-astra`, `xhigh`; no silent fallback.
All paths below are relative to the setup or resolved new run, as specified.
Use the mathis-prover and mathis-proof-reviser skills for proof/audit work,
and math-literature-check for precise citation dependencies as needed.

## 1. Preflight and freezing

Run `python3 scripts/validate_setup.py` (Python >=3.11). Resolve the setup path.
Check actual coordinator model and effort using available runtime evidence
or an explicit owner confirmation of the model/effort selector;
saved config alone is not evidence of the running model. Record what is
requested and what can be verified. Report a mismatch or inaccessible model
before dependent work; do not silently use the old Sol custom roles.

Follow `instructions/accounting.md` before substantive model work. If exact
per-agent telemetry is unavailable, disclose that BEFORE launching the research
and ask whether the owner accepts NR fields plus labelled estimates. Do not
promise exact billing or counts from word lengths. No API experiment, model
switch, external job or new subscription is authorised to bypass this gate.

Create a unique `runs/<UTC timestamp>_astra6/`, with `run_manifest.json`,
`status.json`, `agent_accounting.jsonl`, `reasoning_summary.md`, `decisions.md`
and `statements/`. Copy/freeze `common/`, `starting_information/`, instructions,
templates, approaches and workflow/config as run inputs. Record path hashes,
runtime metadata if exposed, model/effort evidence and accounting capability.
The construction seed exists in the run but is excluded from obstruction
packets. Do not import previous runs or their statuses.

Copy S0 into `statements/S0.md`, hash it, and initialise a statement ledger.
Each dispatch names its statement ID/path/hash, packet hashes, role, output
ownership and attempt allowance. A live baseline file is not a substitute.

## 2. Independent obstruction phase comes first

Dispatch `nonexistence_1` and `nonexistence_2` in separate fresh contexts
(`fork_turns: none`). Both receive S0, neutral common sources, their role and
approach instructions and the submission template. Neither receives old
proofs, another agent's work, coordinator proof suggestions or review verdicts.
Run at most three subagents concurrently, or the lower host limit.

The first emphasis is global stationarity/intensity compatibility; the second
is local degeneracy, moment classes and measure-level consistency. Both must
distinguish a general obstruction from an ansatz-specific failure, and both
can investigate the entire statement. They should not assume a negative result.

A single literature role may answer specific source requests, using only
neutral primary evidence. Do not let literature communication carry proof
ideas between tracks. Preserve and hash literature additions.

Freeze each obstruction submission, then dispatch a fresh reviewer for that
submission only. Review uses the fixed target, sources and proof, not the
author's history or desired verdict. Keep extensive reports. Route concrete
coding checks to the coder if needed. Allow at most four numbered submissions
per obstruction track (initial plus three genuine repairs); do not endlessly
rewrite an unclosed gap.

## 3. Adopt and broadcast the strongest justified working target

If no general obstruction has been verified, S0 remains active. An unresolved
negative search grants no permission to narrow it.

For a verified obstruction, preserve S0's verdict and create a versioned
amendment using `templates/statement_change.md`. Record:

- the exact impossibility theorem and its assumptions;
- the reviewed proof/report hashes;
- which portion of S0 is contradicted;
- what change the theorem actually forces, and what it does NOT force;
- the chosen replacement statement and any non-unique operational choice;
- all geometry/intensity quantifiers, required moment class and remaining gaps.

The owner permits obstruction-driven restrictions of domains. Do not pretend
a particular cutoff is uniquely necessary merely because the unrestricted
domain is impossible. Keep arbitrary prescribed intensity, exactness, all three
orders and full densities unless the owner explicitly approves changing them.
Do not add a positive altitude restriction to the broad infinite-moment class
solely because a finite-fourth-moment subclass is ruled out.

If there are incomparable material choices or no defensible broadly scoped
replacement, ask the owner rather than silently selecting an easy theorem.
An unrestricted non-existence result may be complete even when a replacement
existence question remains unsettled. Do not skip construction work merely
because the deliberately broad S0 was disproved if a replacement is adopted.

Freeze the amendment and a complete self-contained replacement `S1.md`, etc.
The coordinator sends the same adopted version, proof scope and authority to
ALL logical roles, including queued ones, and records delivery in the ledger.
Construction work starts only after this gate; provisional statements do not
count as acceptance targets.

## 4. Four independent construction tracks

Dispatch the four roles `proof_1` through `proof_4` with the adopted statement,
reviewed obstruction packet, frozen neutral literature, their individual
approach file and the SAME labelled construction seed packet. Use fresh
contexts. No track may read another construction track's new work or feedback.
Do not use a shared live brainstorming context.

Each track owns `tracks/<role>/work/` and `tracks/<role>/submissions/`.
It has FOUR substantive submissions total (v01, v02, v03, v04), not four
additional repair rounds. Each is frozen and independently reviewed. Initial
reviews use fresh contexts; delta reviews may use the explicit earlier issue
list but not the author's private deliberation.

Return only the relevant reviewer's actionable findings to the author.
Technical interruptions before a substantive submission do not automatically
consume an attempt; record them. A repeated restatement without a new argument
is not a repaired proof. If a proved obstruction rules out the fixed approach,
do not manufacture four identical submissions: report it and ask the owner whether to end that track
early or use the remaining allowance on permissible alternatives. Do not
unilaterally label it exhausted before four submissions. Otherwise use the
remaining genuine attempts before declaring the approach exhausted.

Success requires the EXACT active statement. A narrower intensity interval,
shape class or approximate/cumulant identity is partial progress, not a pass.
Do not transfer a successful proof to another track and count it as independent.

## 5. Owner checkpoint after three attempts

After three unsuccessful reviewed submissions on a construction track, it may
request an owner-approved amendment. Send a concise question with:

1. the current target and unresolved obstruction/gap;
2. the EXACT proposed new statement and changed quantifiers/domains;
3. what mathematical content would be lost;
4. whether necessity is proved or this is only a pragmatic weaker question;
5. why the change gives a plausible path; one substantive attempt remains.

Use `templates/statement_change.md` with authority `owner_request_pending`.
Do not imply that failure after three attempts proves impossibility. Combine
overlapping requests into one clear question when useful.
Until explicit approval, the statement is unchanged. While awaiting a reply,
other independent work may continue. If no reply arrives, the remaining attempt
may address the unchanged target; never treat silence as consent.

On approval, record the user's exact decision and timestamp, create/hash a new
statement version and broadcast it to ALL roles. Mark authority
`owner_approved`, not `proved_necessary`, unless both apply independently.
The existing attempt count remains; only the owner can authorise a reset or
additional attempts. A prior theorem is evaluated against its original target;
do not retroactively relabel it a success for S0.

## 6. Final report and handoff

After individual reviews, the reviewer may receive the frozen comparison packet
for an extensive final synthesis. This is the first stage permitting comparison
of construction approaches; do not feed synthesis back into initial work.

Report separately: S0 verdict; each later target and authority; successes;
restricted theorems; class-specific obstructions; invalid steps; unresolved
claims; source checks; computational evidence; and the status after each of
the four attempts. Distinguish mathematical falsity from approach exhaustion.

Provide `review_report.md`, a readable `reasoning_summary.md` (proof/decision
summaries, not raw chain-of-thought), `target_history.md`, and an accounting/cost
table with measured, estimated and unavailable fields clearly separated.
Save hashes and limitations. No publication, git push, manuscript overhaul or
simulation campaign is part of this launch unless separately requested.
