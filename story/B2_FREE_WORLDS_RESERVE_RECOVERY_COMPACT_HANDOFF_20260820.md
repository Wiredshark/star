# B2 Free Worlds Reserve Recovery Compact Handoff — 2026-08-20

## Verdict

**PARTIAL pending repository-native CI/build/save-load validation.**

This B2 slice is isolated and intentionally unmerged for A3 authority.

## Repository / branch

- Repository: `Wiredshark/star`
- Authoritative `main` observed at slice selection: `afde12845a8426df9e39edea0b6f58d10ef2c9e7`
- Required B1 parent branch: `agent/b1-free-worlds-relief-reserve-history-20260820-0120`
- Exact B1 parent SHA: `22d46608fe28e3a680239e620a94aeb95b14d3e3`
- B2 branch: `agent/b2-free-worlds-reserve-recovery-compact-20260820-1225`
- Production commit: `c3f4a3f681ebe8bafa23bb7012139f85ec369cd4`
- Focused-validator commit: `24178dc6a57f5d987f98a4195806d15fd4f84676`

## Slice

**B2 Free Worlds Reserve Recovery Compact** turns B1's reserve-stock rotation, surge-shelter capacity, replenishment, and contingency-margin history into a persistent character conflict that reacts to A1's live Free Worlds relief-reserve strain.

### Characters

- **Rina Sol** — relief depot manager; emphasizes explicit restoration targets and the physical reserve categories that must actually be rebuilt.
- **Cal Brenner** — volunteer coordinator; emphasizes the staff, transport, maintenance, and borrowed-equipment obligations hidden behind apparently recovered stock levels.

### Dynamic arc

1. **Offer — `The Empty Shelf Is Not the End`**
   - appears at `world: free worlds relief reserve strain >= 3`;
   - player can choose stock-target discipline, support-capacity-first recovery, a paired obligation model, or refuse involvement;
   - three substantive routes persist under the B2 namespace.
2. **Review — `When the Reserve Looks Full Again`**
   - appears only after A1 naturally recovers reserve strain to `<= 1`;
   - remembers the initial route;
   - exposes the failure mode where a copied summary says `restored` while stock, staffing, transport, fuel, maintenance, shelter, or borrowed-resource obligations remain unresolved;
   - resolves into exactly one of two persistent models: a portable reserve-status packet or a reconciliation cycle.
3. **Brenner Remembers**
   - one-shot later reader consuming either settlement.

## Dependency / ownership invariants

- B1 parent supplies the historical reserve institutions. Integrate/accept B1 first.
- A1 remains sole writer of `world: free worlds relief reserve strain`.
- B2 only reads A1 reserve strain as an Offer/Review gate.
- Every B2 condition write is under `B2 Free Worlds Reserve Recovery Compact:*`.
- No credits, reputation, cargo, outfit, ship, fleet, or combat mutations are introduced.
- A full shelf is not automatically restored emergency capacity: physical stock, trained staff, transport, shelter operation, fuel, maintenance, borrowed resources, and closure evidence remain distinct.
- Independent Free Worlds retain local operating-margin authority; the compact is a shared accounting/reconciliation practice, not a centralized government or mandatory reserve quota.

## Files

- `data/human/b2 free worlds reserve recovery compact.txt`
- `tools/story/validate_b2_free_worlds_reserve_recovery_compact.py`
- `story/B2_FREE_WORLDS_RESERVE_RECOVERY_COMPACT_HANDOFF_20260820.md`

## Validation intended

Focused validator:

```text
python3 tools/story/validate_b2_free_worlds_reserve_recovery_compact.py "data/human/b2 free worlds reserve recovery compact.txt"
```

Repository-native required gates before READY:

- focused story/simulation validation including changed-content style;
- A1/state-ownership regression contracts;
- normal Endless Sky content parser/build path;
- production build;
- stock save/load integration smoke.

Do not promote this handoff to READY until the exact production/validator candidate has terminal green evidence for the required repository-native gates.

## A3 / B3 integration notes

A3 should:

1. re-read current authoritative `main` immediately before integration;
2. integrate/accept B1 Free Worlds relief-reserve history first if it is still outstanding;
3. inspect ancestry and current A1 reserve-strain ownership;
4. require terminal green validation for the exact B2 candidate;
5. preserve the distinction between visible replenishment and genuinely restored reserve capacity.

B3 continuity should prevent downstream summaries from allowing one recovered category to erase another unresolved reserve obligation.
