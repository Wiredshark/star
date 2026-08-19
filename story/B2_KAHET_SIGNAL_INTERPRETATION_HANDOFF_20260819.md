# B2 Ka'het Signal Interpretation — handoff

## Verdict

**PARTIAL** pending exact-final save-load/build validation and completion of the required B1 dependency gate.

## Authority and isolation

- Repository authority: `Wiredshark/star`.
- Authoritative `main` observed before slice selection: `a4ba72896870d0b764272ef95d012b661b677c06`.
- Required B1 parent: `agent/b1-kahet-builder-archives-20260819-1517` @ `5d03f84306c5949227d321c3caed886a11243f31`.
- Isolated B2 branch: `agent/b2-kahet-provenance-compact-20260819-1528`.
- Production commit: `e50aac85362943f449b559a65e5af7e10bd8f25c`.
- Focused validator commit / production+validator validation head: `3879fd6995d2a3c1bf25581d3de8ca2afb339b87`.
- This handoff commit is documentation-only after that production+validator head.
- Draft PR: #109, base = B1 Ka'het/Builder archive branch.
- B2 did not merge or advance the authoritative integration branch.

## Concurrency review

Before authoring, recent authoritative commits, open B1/B2 PRs, and the new B1 Ka'het/Builder archive slice were inspected. No existing B2 Ka'het dynamic-content branch or open B2 Ka'het PR was found. This slice is intentionally separate from prior Remnant continuity/security/salvage content: it concerns evidence handling for translated Ka'het network traffic and present-day field surveys.

The exposed private execution service was also inspected rather than assumed to be an Endless Sky checkout. Its service process list reported five pre-existing service-owned orphan processes; they were left untouched. Its repository workspace remote is `Wiredshark/fallout-test`, not `Wiredshark/star`, and the workspace was already dirty. No host-side Endless Sky result is claimed from that unrelated workspace.

## B2 behavior added

Adds `data/kahet/b2 kahet signal interpretation.txt` with three persistent Remnant missions and one delayed event.

### Recurring characters

The player privately thinks of two recurring Remnant researchers as the **Interpreter** and **Scout**. Those are player-facing shorthand only, not formal Remnant offices or newly asserted canonical titles.

### Offer — The Signal and the Site

Consumes:

- `First Contact: Ka'het: Remnant 1B: offered`
- `Ka'het History: Lost Network Register: offered`
- `Ka'het History: Builder-Ka'het Distinction Ledger: offered`

The researchers disagree over how much present-day operational weight to assign translated Ka'het status traffic when old network destinations no longer match current surveys.

Persistent player routes:

1. **translation-first** — treat the translated network as the primary historical map while clearly dating/annotating current confirmation;
2. **field-first** — use current observation for operational routing while retaining old traffic as historical context;
3. **paired** — preserve original signal, translation/alternate readings, current survey evidence, and unresolved mismatches together;
4. **refusal** — records refusal and does not schedule the Review.

Each substantive route schedules `B2 Ka'het Signal Interpretation: Review Ready` after 7–11 days.

### Review — A Map That Learned Too Slowly

The second-order problem is information loss during copying/export: signal age, alternate readings, field contradictions, or historical context can disappear while a simplified conclusion survives.

The Review resolves to exactly one terminal settlement:

- **confidence atlas** — every operational waypoint carries observation date, evidence source type, translation confidence, and expiry/review for assumptions;
- **contradiction register** — translated claims and field observations remain distinct linked records, and unresolved mismatch must follow every downstream summary until explicitly closed.

### Later reader — Scout Remembers

One-shot aftermath content demonstrates that the chosen rule remains visible later without turning a historical hypothesis into an unquestioned current landmark.

## Canon and state invariants

Preserve all of the following:

- living Ka'het are distinct from their artificial exoskeletons;
- living Ka'het/exoskeletons are distinct from Builder facilities and automated servicing/communications machinery;
- old status traffic can establish that a connection, route, task, or destination was expected at the time of transmission;
- old status traffic does **not** prove a destination still exists now;
- automated reports do not provide omniscient Builder/Ka'het history;
- no unsupported Builder motive or exact collapse chronology is asserted;
- translation, alternate interpretation, historical reconstruction, current field observation, and operational route safety remain distinguishable evidence layers.

All persistent writes are restricted to `B2 Ka'het Signal Interpretation:*`.

The slice does not write:

- `world:*` simulation state;
- `First Contact: Ka'het:*`;
- `Ka'het History:*`;
- credits or reputation;
- cargo, outfits, ships, fleets, or combat rating;
- unrelated campaign state.

## Files added

- `data/kahet/b2 kahet signal interpretation.txt`
- `tools/story/validate_b2_kahet_signal_interpretation.py`
- `story/B2_KAHET_SIGNAL_INTERPRETATION_HANDOFF_20260819.md`

## Validation evidence

### Completed on production+validator head `3879fd6995d2a3c1bf25581d3de8ca2afb339b87`

GitHub Actions **Fork simulation and story validation** run #116 (`32293532470`) completed **SUCCESS** on the exact production+validator head. This is the repository-native gate that discovers focused story validators and changed-content style checks. The new focused validator was present on that exact head.

### Still pending at handoff creation

GitHub Actions **Fork save-load integration smoke** run #105 (`32293532429`) was still in progress on the same production+validator head when this handoff was written. No production build/save-load PASS is claimed until it reaches terminal green.

The required B1 parent also has **Fork simulation and story validation** green on exact B1 head `5d03f84306c5949227d321c3caed886a11243f31`, while its exact-head save-load workflow remained in progress at the latest check.

## Required A3 gate

Before integration:

1. confirm the B1 parent exact-head save-load workflow reaches terminal success;
2. confirm B2 exact production+validator save-load run #105 reaches terminal success, or rerun/repair against the final candidate if it fails;
3. verify the final B2 handoff-only commit changes documentation only relative to the validated production+validator head;
4. preserve integration order: B1 Ka'het/Builder archive history first, then B2 Ka'het Signal Interpretation;
5. run any additional A3 integration-head regression required by the shared integration protocol.

## A3/B3 notes

B3 should preserve the epistemic boundary between what a surviving signal literally reports, what a translator infers, what a field survey currently observes, and what an operator may safely treat as present-tense navigation truth.

A3 should not convert Interpreter/Scout into formal offices, should not promote old Ka'het traffic into current omniscient route data, and should not integrate B2 before the B1 dependency is accepted.
