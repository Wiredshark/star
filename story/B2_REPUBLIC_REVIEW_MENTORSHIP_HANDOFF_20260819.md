# B2 Republic Review Mentorship handoff — 2026-08-19

## Stage

- `LOOP_ID`: B2
- `PRIMARY_DOMAIN`: character / dynamic content
- `SECONDARY_DOMAINS`: Republic legal process, mentorship, persistent narrative memory
- `RUN_TYPE`: FEATURE / CONTENT
- `VERDICT`: PARTIAL pending repository CI/runtime gates

## Authoritative base

- Repository: `Wiredshark/star`
- Base branch: `main`
- Base SHA: `d485dea4c511964c1209d86dae15f5bcbf17a03b`
- Isolated branch: `agent/b2-republic-review-mentorship-20260819-0129`

## Concurrency check

A separate fresh B2 branch, `agent/b2-wanderer-stewardship-compact-20260819-0125`, already existed when this run began. This slice deliberately avoids Wanderer/stewardship content and instead consumes the newly integrated Republic customs-review chain.

## Input authorities

B2 reads only existing A2 legal-memory conditions from `data/human/a2 republic customs review.txt`, especially:

- `A2 Republic Customs Review: later reader seen`
- `A2 Republic Customs Review: precedent kept private`

The public/bounded-precedent path is the normal complementary A2 outcome. B2 does not mutate any `A2 Republic Customs Review:*` condition.

The upstream A1 crime/law simulation remains authoritative for:

- `world: republic customs scrutiny`
- `world: republic border pressure`

B2 does not read or write those world-state variables directly; the character arc occurs only after the A2 review/memory sequence is complete.

## Character/content behavior

Production file:

`data/human/b2 republic review mentorship.txt`

Named characters:

- **Sera Noll** — existing Republic port-rights observer from A2, now deepened beyond the original customs-review encounter.
- **Mara Keene** — new junior port-rights observer learning how to teach procedural safeguards without converting one captain's case into permanent unofficial precedent.

### Stage 1 — A Case Without a Captain

Offers after A2's later reader has been completed.

The opening remembers whether the player asked Noll to keep the earlier case private. The player may choose:

1. an anonymized casebook;
2. supervised live clinics;
3. private mentorship;
4. refusal to reuse the old case.

Accepted routes schedule `B2 Republic Review Mentorship: Practice Ready` after 5–7 days. Relationship-state writes are B2-prefixed only.

### Stage 2 — The Observer's Question

After the delay, Keene reports what failed in practice. Each original route produces a different problem statement, then the player chooses one of two durable training settlements:

- `settlement safeguards record` — an abstract review record separating evidence, inference, scope authority, consent, and escalation rationale;
- `settlement supervised review circle` — live current-case comparison with a shared reasoning rubric but no binding historical model file.

### Stage 3 — Keene Remembers

A later one-shot reader reflects the chosen settlement and records `aftermath seen`.

## Persistence and authority invariants

- All writable state is `B2 Republic Review Mentorship:*`.
- A1 and A2 state is read-only.
- No reputation, credits, cargo, outfits, ships, combat rating, or pirate-job history is mutated.
- Refusal does not schedule the later practice-review stage.
- Accepted routes use a delayed event rather than immediately chaining the next mission.

## Focused validator

`tools/story/validate_b2_republic_review_mentorship.py`

Checks:

- exact 3-mission + 1-event graph;
- two named characters;
- A2 dependency markers;
- 3 accepted routes + refusal;
- 2 terminal settlements;
- Republic non-station source scoping;
- local `goto` / `label` resolution;
- no A1/A2 assignments;
- no material/reputation mutation;
- persistent trust and later-reader state.

## Validation status

At handoff creation, repository-side CI had not yet run for this branch. A draft PR should remain PARTIAL until the new repository-native fork validation, changed-file style gate, stock save-load smoke, and any focused validator execution are observed.

The private Fallout execution host was inspected only for process/workspace availability. Its repository workspace was already dirty and is not treated as authoritative `Wiredshark/star` evidence for this B2 slice.

## A3 / B3 integration notes

- Integrate only after repository CI and content validation are green.
- Preserve A2 ownership of the customs-review and precedent/privacy state.
- Preserve A1 ownership of customs scrutiny and border pressure.
- B3 should check that Sera Noll's characterization remains consistent with A2: she treats review flags as administrative signals rather than findings, separates evidence from inference, and respects the player's privacy/precedent boundary.
- The new Keene material is deliberately a character mentorship consequence, not a second customs investigation.
