# B2 Southern Rim Overflow Recovery Compact handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** READY for A3 review/integration  
**Current authoritative `main` rechecked during lifecycle recovery:** `a17a89fb4779200a0634a6dade1811c4dc9cc2be`  
**Historical required B1 parent:** `39a189069031cd8673362ea7d04b664ebac7db14`  
**Branch:** `agent/b2-southern-rim-overflow-recovery-20260820-1324`  
**Original production commit:** `4a9f5536c708f894d44c9aba4b0ba0012d3cdcbb`  
**Original focused-validator commit:** `08a512bcc752faec53e4cfd977963a4676094e9b`  
**Lifecycle production repair:** `33e4407f2b9c273ce133a4b6a72d11aed0caaa7e`  
**Lifecycle validator hardening / exact fully validated candidate:** `48ff28a7adc68d7be9f7d54e609064090c702378`

## Scope

This three-mission Southern Rim character/dynamic-content arc consumes:

- B1 `Southern Rim Overflow Berth Compact Archive` history;
- the completed A2 Rhea Solano traffic-coordination aftermath;
- authoritative A1 `world: southern rim transit congestion` as read-only live state.

The arc uses returning traffic coordinator **Rhea Solano** and overflow-port yardmaster **Jo Kessler**. Their conflict is the capacity debt created when major Southern Rim queues are relieved by shifting work onto secondary ports.

Initial routes remain:

1. make berth/tug/repair/fuel/crew/maintenance displacement a visible capacity obligation;
2. keep overflow routing flexible but assign restoration owner and deadline;
3. pair diversion results with receiving-port capacity use and closure evidence;
4. refuse to create a regional practice.

When A1 naturally recovers congestion to `<= 1`, the Review resolves into exactly one of:

- a **portable borrowed-capacity packet** carrying origin, receiving capacity used, deferred obligation, restoration owner, review point, and closure evidence;
- a **reconciliation cycle** that preserves local capacity ledgers while preventing the network from calling borrowed capacity restored before participating ports actually close remaining deficits.

`Kessler Remembers` remains the one-shot later reader.

## Lifecycle recovery

The slice is dialogue/state-only. It creates no destination, stopover, waypoint, NPC, cargo, passenger, deadline, timer, or other gameplay objective.

The original production used terminal `accept` on the three positive Offer routes, both Review settlements, and `Kessler Remembers`. Those six objective-less accepts could leave missions active after the conversation closed.

Lifecycle repair `33e4407f...` changes exactly those six terminal commands to `decline`; refusal already used `decline`. All **7/7 state-only terminal paths now persist their existing state and close cleanly**.

No dialogue, route condition, trust condition, settlement condition, A1/B1/A2 dependency, or persistent condition name/value changed.

Validator hardening `48ff28a7...` now requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing mission directives;
- all pre-existing mission, route, settlement, ownership, material-mutation, continuity, and `goto`/`label` invariants.

## Continuity / ownership invariants

- A1 remains sole writer of `world: southern rim transit congestion`.
- B1 history and A2 traffic-coordination state are read-only.
- Every B2 write remains `B2 Southern Rim Overflow Recovery Compact:*`.
- No credits, reputation, cargo, outfit, ship, fleet, or combat mutation.
- Clearing the major traffic queue is not the same condition as restoring secondary-port berth, tug, repair, fuel, crew, and maintenance capacity.
- A diversion result and its downstream capacity cost may both be true and must remain separately visible.
- A restoration deadline is not closure evidence by itself.
- Resolved obligations should close rather than becoming permanent warnings.
- Shared overflow/reconciliation records do not create a centralized Southern Rim traffic authority; local port authority remains explicit.

## Validation evidence

On exact lifecycle candidate `48ff28a7adc68d7be9f7d54e609064090c702378`:

- `Fork simulation and story validation` #479 / run `32639342867`: **SUCCESS**
- `Fork save-load integration smoke` #464 / run `32639342876`: **SUCCESS**
- focused `validate_b2_southern_rim_overflow_recovery_compact.py`: **PASS** in a fresh isolated private-host clone
- `tools/story/validate_story_repo.py`: **PASS** in the same isolated clone
- `tools/story/test_b2_character_packets.py`: **PASS** in the same isolated clone
- production configure/build and stock save-load smoke: **SUCCESS** through repository-native CI

A direct local `utils/check_content_style.py` attempt on the private host could not start because that host lacks the third-party Python `regex` module. This is not a blocker because the repository-native simulation/story workflow completed successfully and includes changed-content style on the exact candidate.

## Isolation / ancestry

Current-main comparison for lifecycle candidate `48ff28a7...`:

- **7 commits ahead / 55 behind** current `main`;
- merge base `7c8009bd1a26b09d464ab9a2dae11fb69c7f95e2`;
- branch diff includes the historical B1 dependency plus this B2 slice.

GitHub currently reports the PR mergeable, but A3 must re-read current-main ancestry and reconcile/accept the B1 Southern Rim transit history first if it remains outstanding. Do not mechanically merge a historical branch merely because the platform reports it mergeable.

## A3 / B3 integration guidance

A3 should preserve the lifecycle repair and integrate only after rechecking current `main`, B1 dependency status, and semantic overlap with later Southern Rim work.

B3 should preserve the distinction among:

- primary queue clearance;
- diverted traffic success;
- receiving-port physical capacity used;
- deferred maintenance / crew / tug / fuel obligations;
- promised restoration;
- actual closure evidence.

Practical interoperability among independent ports must not become a centralized Southern Rim traffic government.
