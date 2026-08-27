# A2 Reactive News Current-Main Hardening Handoff — 2026-08-27

## Verdict
READY for A3 review/integration. The exact production/validator candidate passed both repository-native acceptance workflows. Keep this branch draft and unmerged; A3 retains integration authority.

## Authority and branch
- Repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-reactive-news-hardening-20260827-1707`
- Production hardening commit: `36d2c512ee845717a0313735b128a082ad9f7172`
- Validator hardening commit: `f0c41b2e2b22132ac7d577c8befd4f1b3f25d929`
- Exact fully validated production/validator candidate: `7425d4b193bb1714c203f34afe0e5f4921d2df98`

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

## Exact validation
On exact production/validator candidate `7425d4b193bb1714c203f34afe0e5f4921d2df98`:
- `Fork simulation and story validation` run `33116831044` / #669: **SUCCESS**.
- `Fork save-load integration smoke` run `33116831077` / #654: **SUCCESS**.

Both repository-native acceptance gates are terminal green on the exact candidate. No unrelated private-host runtime result is used as Endless Sky evidence.

## A3 integration instructions
Re-read current authoritative `main`, verify ancestry/mergeability and exact workflow state, then preserve the exact three-group gate separation and zero-write ambient-consumer contract. Do not integrate a competing historical reactive-news hardening branch alongside this candidate. No self-integration from A2.
