# B2 Free Worlds Volunteer Command Compact — handoff

## Verdict

**PARTIAL pending repository-native validation.** The production slice and focused validator are committed on an isolated B2 branch. Do not integrate until the simulation/story/style workflow and production build/save-load workflow are terminal green on the exact candidate head.

## Authority and branch

- Repository authority: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-free-worlds-volunteer-command-20260823`
- Production commit: `a609d3b657e4056c6e6677278e705f2322edd7d8`
- Focused-validator commit / pre-handoff candidate: `0485d63b00a6b0dc8be43879402b7bd44f1ec185`

## What B2 adds

This slice turns the Free Worlds Mutual Defense Registry's historical compromise into present-day character content during an A1 patrol mobilization.

Characters:

- **Elia Venn**, a Free Worlds defense liaison who needs volunteer tasking to remain operationally meaningful during a surge.
- **Mara Quill**, an independent rescue-tug captain who accepts temporary militia coordination but refuses to let emergency consent become permanent command over her ship.

The Offer reacts read-only to A1-owned `world: free worlds patrol surge` and `world: free worlds defense strain`. The player can choose:

1. **bounded activation** — purpose, scope, issuing authority, release condition, and unfinished-work ownership are explicit;
2. **captain discretion** — common defensive objectives remain binding inside the volunteered scope while ship-safety authority and out-of-scope refusal remain with the civilian captain;
3. **paired records** — a shared tactical task record is linked to a separate captain consent/scope/safety/withdrawal record;
4. **refusal** — no general command model is adopted from this emergency.

After the patrol surge ends and A1 defense strain naturally recovers to `<= 1`, the Review resolves the problem into one of two persistent settlements:

- **portable activation packet** — emergency purpose, volunteered scope, issuing authority, captain consent, safety limits, substitutions/refusals, release condition, and closure status travel together;
- **expiry and release** — a volunteer activation ends with the named emergency and cannot regain authority through copying or precedent; a later emergency requires a fresh activation and fresh consent.

`Quill Remembers` is the one-shot aftermath reader.

## Dependencies and ownership

- A1 is the **sole writer** of:
  - `world: free worlds defense strain`
  - `world: free worlds patrol surge`
- B2 reads those conditions only.
- B2 writes only `B2 Free Worlds Volunteer Command Compact:*` conditions.
- There are no direct credits, reputation, cargo, outfits, ships, fleets, combat-rating, or other material mutations.
- The slice intentionally does **not** modify A2 Free Worlds Patrol Doctrine. A2 owns patrol deployment doctrine; this B2 slice owns the character/institutional boundary between temporary militia coordination and the continuing autonomy of volunteer civilian captains.

## Canon and continuity invariants

- Free Worlds collective defense remains distributed coordination among member worlds and independent crews, not a centralized navy.
- Temporary militia coordination does not transfer permanent ownership or command of a civilian ship.
- A true historical order can become a false current order if copied without its release/closure context.
- Refusal outside an agreed volunteer scope is not automatically desertion or disobedience.
- A later emergency requires new authority evidence; historical consent is not permanent consent.
- Elia Venn and Mara Quill are local recurring characters, not proof of a universal Free Worlds bureaucracy.

## Lifecycle contract

All seven dialogue/state-only terminal branches use `decline`; there are no `accept` terminals and no gameplay-objective directives. The slice therefore does not create objective-less accepted missions.

## Files

- `data/human/b2 free worlds volunteer command compact.txt`
- `tools/story/validate_b2_free_worlds_volunteer_command_compact.py`
- `story/B2_FREE_WORLDS_VOLUNTEER_COMMAND_COMPACT_HANDOFF_20260823.md`

## Validation

A focused private-host scratch clone was attempted before opening the PR. The clone failed inside Git object-pack creation (`fetch-pack: invalid index-pack output`), so no host-side PASS is claimed from that attempt and no unrelated repository/process state was touched.

Required acceptance gates on the exact candidate head:

```text
python3 tools/story/validate_b2_free_worlds_volunteer_command_compact.py
python3 tools/story/validate_story_repo.py
python3 tools/story/test_b2_character_packets.py
Fork simulation and story validation
Fork save-load integration smoke
```

The focused validator additionally enforces 3 missions, both named characters, A1 read-only ownership, three routes plus refusal, exactly two settlements, one-shot aftermath, seven `decline` / zero `accept` terminals, B2-only persistent writes, local `goto` integrity, and the temporary-versus-permanent command boundary.

## A3 / B3 integration notes

A3 should re-read current `main` before integration. Integrate only if the exact candidate's repository-native workflows are terminal green and the branch remains cleanly based on the recorded authoritative base.

B3 should preserve the distinction among historical tasking, live authority, captain consent, volunteered scope, safety authority, refusal/substitution, release condition, and closure status. Repeated copies of a historical order do not make it live authority again.
