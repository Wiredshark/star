# B2 Sheragi Context Compact Handoff — 2026-08-19

## Verdict

PARTIAL pending repository-native CI/build/save-load validation on the exact branch head.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration base observed at run start: `46d1afcf2e22e211b02f1615e863dae903f0778f`
- Base already contains integrated B1 Sheragi archaeological-memory work.
- Isolated branch: `agent/b2-sheragi-context-compact-20260819-1923`
- Production commit: `61aa8b1e654e74635f683ab9b448bc831bfc1213`
- Focused-validator commit: `d29215713accb694a37246364bef72a769ad47ac`
- B2 does not self-integrate.

The exposed private Fallout execution workspace was inspected before claiming host-side validation. Its GitHub remote points to `Wiredshark/fallout-test`, not `Wiredshark/star`, and the workspace was already dirty. It was therefore left untouched and is not counted as Endless Sky validation evidence.

## Character / dynamic-content slice

`B2 Sheragi Context Compact` turns the integrated B1 Sheragi provenance and site-context institutions into a persistent contemporary character dispute between two human researchers:

- **Nadia Rell** — conservation-first when physical evidence is at immediate risk.
- **Ivo March** — context-first when removal would destroy relationships around the object.

The arc does not assert new facts about ancient Sheragi motives, politics, or institutions. Its subject is modern archaeological practice after the existing Sheragi archaeology epilogue.

### Offer — `The Wall and the Weather`

A storm exposes a Sheragi wall fragment whose surface is physically endangered before its surrounding context is fully mapped. The player can choose:

1. emergency shelter/removal with explicit unresolved-context recording;
2. context-first survey under temporary protection and a hard weather threshold;
3. paired emergency protocol recording minimum site context before removal and linking conservation work back to that field record;
4. refusal.

Each substantive route persists independently and schedules a delayed Review after 7–11 days.

### Review — `A Reconstruction Without a Site`

A museum reconstruction remains useful while a copied teaching model drops the distinction between direct measurement, site relationships, inferred geometry, and interpretive additions.

The Review remembers the original route and resolves to one of exactly two persistent outcomes:

- **portable context packet** — every reconstruction carries source images, site relationships, measured geometry, inferred sections, conservation changes, and unresolved uncertainty;
- **reversible reconstruction** — interpretive additions remain separable so later researchers can strip a model back to the direct evidentiary state.

### Aftermath — `Nadia Remembers`

A one-shot later reader shows the selected settlement operating in practice without granting material rewards or mutating unrelated campaign state.

## Dependencies and ownership

The Offer requires:

- `Sheragi Archaeology: Epilogue: done`
- `Sheragi History: Evidence Provenance Register: offered`
- `Sheragi History: Site Context Registry: offered`

All persistent writes are namespaced under `B2 Sheragi Context Compact:*`.

B2 does **not** write:

- B1 Sheragi history conditions;
- A1 `world:*` state;
- credits or reputation;
- cargo, outfits, ships, fleets, or combat rating;
- ancient-Sheragi campaign conclusions.

Continuity invariant: physical object, excavation/site context, later conservation changes, reconstruction, and interpretation remain distinguishable. Missing or uncertain evidence remains explicitly missing/uncertain rather than silently converted into historical fact.

## Files

- `data/sheragi/b2 sheragi context compact.txt`
- `tools/story/validate_b2_sheragi_context_compact.py`
- `story/B2_SHERAGI_CONTEXT_COMPACT_HANDOFF_20260819.md`

## Focused validation contract

The new validator checks:

- exact three-mission graph;
- delayed Review event;
- Nadia Rell and Ivo March presence;
- Sheragi epilogue/B1 gates;
- three persistent substantive routes plus refusal;
- exactly two terminal settlements;
- one-shot aftermath reader;
- B2-only write ownership;
- no direct material/reputation/combat mutation surface;
- local conversation `goto`/`label` integrity;
- preservation of object/context/reconstruction/interpretation/uncertainty distinctions;
- no unsupported ancient-Sheragi motive/government claims.

Required focused command:

```bash
python3 tools/story/validate_b2_sheragi_context_compact.py "data/sheragi/b2 sheragi context compact.txt"
```

## Required acceptance before READY

A3 should promote this handoff to READY only after the exact final head passes the repository-native gates, including at minimum:

1. the focused validator above;
2. the complete story/simulation validation workflow and changed-content style checks;
3. normal Endless Sky configure/build validation;
4. stock save/load smoke coverage, including persistence through conversation/reload cases;
5. clean diff/status confirmation and no unexpected state-ownership violations.

If CI reveals a defect, repair it on this isolated B2 branch, rerun the exact-head gates, and update this handoff with the validated SHA. Do not integrate a PARTIAL head.

## A3 / B3 notes

A3 integration review should preserve the current authoritative B1 Sheragi archaeological-memory content and cherry-pick/merge only this isolated B2 slice after exact-head validation is green. B3 continuity review should specifically verify that no museum or researcher dialogue converts modern reconstruction practice into unsupported claims about what ancient Sheragi intended or believed.
