# B2 Wanderer Evacuation Recovery Compact Handoff — 2026-08-20

## Stage / verdict
- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Verdict: PARTIAL pending exact-head repository-native workflow completion
- No self-integration. A3 retains integration authority.

## Repository authority
- Authoritative repository: `Wiredshark/star`
- Authoritative base observed at branch creation: `66766690c3c46c5f0c8b8d1c9bfb7781615c3e2c`
- Branch: `agent/b2-wanderer-evacuation-recovery-20260820-1428`
- Production commit: `b5cdcf3bf80c6da120d59a773c84ee86b3d28161`
- Focused validator commit: `842ea4e955866a66cecda63e1b26d88f40e96775`
- This handoff commit is the current candidate head when first written.

## Scope
Adds a three-mission Wanderer character/dynamic-content arc that consumes the newly integrated A1 `world: wanderer evacuation logistics strain` signal read-only.

Two recurring Wanderer specialists are described through player-private shorthand as the **Harbor Keeper** and **Route Tender**. The production comment explicitly states that these descriptions do not establish formal Wanderer offices.

### Initial dispute
At authoritative evacuation-logistics strain `>= 3`, after the existing Unfettered invasion has started, the player encounters a Wanderer harbor recovering from repeated evacuation runs. The core problem is that refugees can have arrived safely while shelter, berth, crew, transport, power, and maintenance capacity remains borrowed or degraded.

Player routes:
1. **obligation-first** — safe arrival closes the journey, not the borrowed-capacity obligations;
2. **current-risk-first** — retain only obligations that still affect present safety, but require explicit closure evidence;
3. **paired record** — keep completed evacuation outcome and still-open capacity restoration as linked but distinct records;
4. **refusal** — preserve local judgment and do not enter the review chain.

### Recovery review
When A1 naturally recovers evacuation-logistics strain to `<= 1`, the Review examines a copied-record failure mode: summaries can either erase unfinished recovery because "evacuation complete" sounds terminal, or preserve already-resolved deficits as permanent warnings.

Terminal settlements:
- **portable recovery packet** — completed arrival, borrowed capacity, responsible owner, current effect, review date, and closure evidence travel together;
- **reconciliation cycle** — arrival and recovery remain separate lightweight ledgers, and neither closes the other without explicit reconciliation.

`Keeper Remembers` is the one-shot aftermath reader.

## Ownership / canon invariants
- A1 remains sole writer of `world: wanderer evacuation logistics strain`.
- Existing Wanderer invasion campaign state is read-only.
- Every new persistent write is under `B2 Wanderer Evacuation Recovery Compact:*`.
- No credits, reputation, cargo, outfits, ships, fleets, combat rating, or other material-state mutation.
- Harbor Keeper / Route Tender are player-private shorthand, not formal offices or centralized Wanderer authority.
- A successful refugee arrival is an event; restored transport/reception capacity is a condition.
- Resolved obligations must be able to close; old emergency records must not become permanent false warnings.
- Operational normalization must not silently erase unresolved shelter, berth, crew, transport, power, or maintenance obligations.

## Non-overlap / concurrency review
Before branching, live `main`, recent commits, open PRs, and the B2 branch inventory were inspected. Existing/recent B2 Wanderer work covers machine custody/stewardship, not the newly integrated A1 wartime evacuation-logistics strain. Open A2 work at selection targets Dirt Belt drought practice. No active B2 slice was found consuming `world: wanderer evacuation logistics strain`.

The exposed private execution service reported four pre-existing service-owned orphan processes. They were preserved; no process was killed or modified.

## Files
- `data/wanderer/b2 wanderer evacuation recovery compact.txt`
- `tools/story/validate_b2_wanderer_evacuation_recovery_compact.py`
- `story/B2_WANDERER_EVACUATION_RECOVERY_COMPACT_HANDOFF_20260820.md`

## Validation requested
Focused validator:

```bash
python3 tools/story/validate_b2_wanderer_evacuation_recovery_compact.py "data/wanderer/b2 wanderer evacuation recovery compact.txt"
```

Repository-native gates required before READY:
- focused story/simulation validator discovery and execution;
- changed-content style;
- A1 world-state ownership/regression contracts;
- production Endless Sky configure/build;
- stock save/load integration smoke.

Actual-game acceptance should additionally exercise:
- high-strain Offer gating;
- all three substantive routes plus refusal;
- persistence across save/reload;
- Review availability only after A1 strain recovers to `<= 1`;
- both mutually exclusive terminal settlements;
- one-shot `Keeper Remembers` suppression after completion;
- no mutation of A1 Wanderer evacuation strain.

## A3 / B3 guidance
A3 should re-read current `main`, verify ancestry and conflicts, and integrate only after exact-head repository-native validation is terminal green. B3 should preserve the distinction among safe arrival, current operational effect, borrowed-capacity restoration, closure evidence, and historical emergency records.
