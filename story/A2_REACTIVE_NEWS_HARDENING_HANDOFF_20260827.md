# A2 Reactive News Current-Main Hardening Handoff — 2026-08-27

## Verdict
PARTIAL — production ownership/style hardening and focused validator hardening are committed on an isolated branch; repository-native exact-head workflows must reach terminal green before A3 integration.

## Authority and branch
- Repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-reactive-news-hardening-20260827-1707`
- Production hardening commit: `36d2c512ee845717a0313735b128a082ad9f7172`
- Validator hardening commit: `f0c41b2e2b22132ac7d577c8befd4f1b3f25d929`

## Implemented narrative surface
This is a hardening pass over the already-integrated A2 ambient reactive-news layer. The player-facing behavior remains three read-only Republic News groups:
1. Deep convoy veteran — gated by `Deep: Syndicate Convoy: done`.
2. Deep convoy command veteran — gated by the Deep convoy completion plus `combat rating >= 5`.
3. Experienced Republic captain — gated by `combat rating >= 5` and intentionally independent of Deep convoy history.

No new state machine or save condition is introduced. Existing News text and gating semantics are preserved.

## Files changed
- `data/human/a2 reactive news.txt`
  - adds the canonical GPL content header;
  - documents the read-only ownership contract;
  - preserves all three existing News groups and their conditions/messages.
- `tools/story/validate_a2_reactive_news.py`
  - enforces canonical header and trailing newline;
  - requires exactly three News groups and exact scope/gating separation;
  - proves the combined Deep+combat gate while keeping the generic veteran item independent of Deep history;
  - rejects directive-shaped persistent/gameplay mutations while ignoring ordinary quoted prose;
  - rejects `world:*` dependencies and shadow `A2 Reactive News:*` state.

## Invariants
- `Deep: Syndicate Convoy: done` remains read-only.
- `combat rating` remains read-only.
- This ambient News layer writes no persistent state.
- There are no `world:*`, material, reputation, cargo, equipment, fleet, combat, destination, waypoint, or objective mutations.
- Republic/Deep/non-station geographic and audience scope remains unchanged.
- The general experienced-captain item must not silently acquire the Deep convoy gate.

## Persistence / save compatibility
No persistent names, values, or writes are introduced or changed. Save compatibility is unaffected by production semantics.

## Validation
Repository-native exact-head validation is pending after PR creation. Do not claim simulation/story/style or build/save-load success until GitHub workflows attach to the exact candidate head and become terminal green.

## A3 integration instructions
Integrate only after both repository-native workflows are terminal green on the exact production/validator candidate SHA. Preserve the three-group gate separation and zero-write ambient-consumer contract. Do not integrate a competing historical reactive-news hardening branch alongside this candidate.
