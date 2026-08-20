# B2 Syndicate Qualification Compact handoff — 2026-08-20

## Verdict

PARTIAL pending repository-native exact-head workflow validation. Do not integrate until required simulation/story/style and production save-load gates are terminal green.

## Authority / base

- Repository: `Wiredshark/star`
- Authoritative base observed at selection: `37bf17aa303d7a9f284a5b2b433d560ddd0404c2`
- Required institutional-history dependency is already integrated on that base: B1 Syndicate dockyard labor history from `d605ca4dfd3f931a88b0ae967bd9a60f335eb99c`.
- Isolated branch: `agent/b2-syndicate-qualification-compact-20260820-0123`

## Exact commits

- Production: `bfcb2bacfad05249be6eb53dbfb577471a730a81`
- Focused validator: `c2d5f8bdd302a5917c1cee351d93cda1e10260eb`
- This handoff commit becomes the current candidate head.

## Scope

Adds a three-mission persistent B2 character arc around dock supervisor **Mara Venn** and contract technician **Ilias Rook**.

The arc consumes B1's distinction between labor headcount and transferable qualification memory, and reacts to A1's authoritative Syndicate labor strain / crew-rotation state without writing either world condition.

### Offer — `The Crew That Fits`

Appears while `world: syndicate labor strain >= 2` and `world: syndicate labor rotation active` is true.

Player positions:

1. **Local-signoff route** — prior evidence travels, but local yards retain job-specific sign-off authority.
2. **Portable route** — verified qualification transfers unless a yard documents a specific local exception.
3. **Paired route** — portable core qualification evidence plus narrow supervised local endorsement for genuinely different systems/hazards.
4. **Refusal** — no later institutional review is scheduled through B2 state.

### Review — `After the Rotation`

Appears after A1 naturally recovers labor strain to `<= 1` and the rotation-active flag is no longer present.

The review exposes a second-order problem: copied qualification summaries can preserve the word `qualified` while dropping equipment family, supervision level, scope, exclusions, or the local endorsement that made the statement true.

Two persistent terminal settlements:

- **portable qualification packet** — carries evidence source, scope, supervision level, limits, and later local endorsements together;
- **expiry-and-renewal** — transferred evidence remains reusable while contextual local endorsements expire only when equipment/hazard assumptions materially change.

### Later reader — `Venn Remembers`

A one-shot character consequence reader that consumes either terminal settlement.

## Ownership / invariants

- A1 remains sole owner/writer of `world: syndicate labor strain` and `world: syndicate labor rotation active`.
- All B2 writes are namespaced `B2 Syndicate Qualification Compact:*`.
- No credits, reputation, cargo, outfits, ships, fleets, or combat mutation.
- The compact is a voluntary/practical agreement among participating yards and contractors, **not** a universal Syndicate labor law or centralized personnel authority.
- Transferable qualification is evidence, not blanket job authority. Local context may legitimately constrain a carried qualification, but local review must not silently erase prior evidence.
- This slice is separate from the existing A2 Tessa Marr maintenance-triage/policy content: that arc concerns maintenance priorities under backlog pressure; this B2 arc concerns worker qualification evidence and local endorsement during/after crew rotation.

## Files

- `data/human/b2 syndicate qualification compact.txt`
- `tools/story/validate_b2_syndicate_qualification_compact.py`
- `story/B2_SYNDICATE_QUALIFICATION_COMPACT_HANDOFF_20260820.md`

## Required validation

1. Focused validator:
   - `python3 tools/story/validate_b2_syndicate_qualification_compact.py`
2. Repository story/simulation validator suite, including state-ownership contracts.
3. Changed-content style gate.
4. Production Endless Sky configure/build.
5. Stock save/load smoke (`Saving during conversation`, `Loading and Reloading`, `Loading and Saving`).
6. Actual-game acceptance should observe:
   - Offer only during active high labor strain + rotation;
   - all three routes plus refusal;
   - Review only after A1 recovers strain and rotation ends;
   - both terminal settlements;
   - save/reload persistence;
   - no unexpected overlap/regression with the Tessa Marr maintenance-triage arc.

## A3 / B3 integration note

If exact-head validation is green, A3 may integrate this isolated branch after confirming current main still contains the B1 Syndicate dockyard-labor history. B3 should preserve the distinction between qualification evidence, local endorsement authority, labor headcount, and actual job-specific competence.
