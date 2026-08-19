# A2 Beyond Patir Survey Review handoff — 2026-08-19

## Portfolio labels

- `LOOP_ID`: A2
- `RUN_TYPE`: FEATURE / CONTENT
- `PRIMARY_DOMAIN`: exploration / environmental hazards
- `SECONDARY_DOMAINS`: Deep science, evidence quality, privacy, persistent history
- `DIVERSITY_STATUS`: PASS
- `NEGLECTED_AREA_ADVANCED`: hazardous exploration after logistics- and law-heavy integration work
- `CROSS_SYSTEM_CONNECTION`: stock visited-system history across the Beyond Patir black-hole cluster

## Production content

File: `data/human/a2 beyond patir survey review.txt`

Named character: **Nadiya Voss**, Deep survey analyst.

The slice is scoped to inhabited Deep non-station sources and uses only engine-owned visited-system history as its prerequisite evidence.

### Stage 1 — Field Review

Requires recorded visits to:
- Athiri;
- Chanai;
- Ghila.

Routes:
1. conservative navigation corridors;
2. publish reproducible raw data and method;
3. wait for independent replication;
4. hidden extended-comparison response, available only after visits to Maithi, Mitera, and Thepa;
5. keep the route logs private.

The positive routes schedule a publication result. The privacy route schedules its own refusal/privacy reader instead.

### Stage 2 — Publication Result

Produces one of four durable outcomes:
- bounded navigation chart;
- reproducible dataset;
- replicated limits;
- layered hazard model separating recurring cluster effects from local black-hole effects.

The result explicitly narrows claims rather than treating one dramatic expedition as universal evidence.

### Stage 3 — Later Reader

Remembers the publication method and lets the player decide whether the precedent may travel anonymously or remain a named example only with the review record attached.

### Stage 4 — Privacy Reader

Confirms that withholding route logs remained a real consent boundary. The player can allow an anonymous methodological note that data was withheld or remove even that training example.

## Authority invariants

Read-only engine inputs:
- `visited system: Athiri`;
- `visited system: Chanai`;
- `visited system: Ghila`;
- `visited system: Maithi`;
- `visited system: Mitera`;
- `visited system: Thepa`.

Writable state is restricted to `A2 Beyond Patir Survey:*` conditions.

The slice does not write visited-system history, `world:*` simulation authority, reputation, credits, cargo, outfits, ships, or combat state.

## Focused validator

`tools/story/validate_a2_beyond_patir_survey_review.py` checks:
- exact four-stage mission graph;
- Deep non-station source scoping;
- core and extended visit gates;
- hidden extended-survey response;
- four positive routes plus privacy route;
- four publication outcomes;
- later-reader and privacy-reader state transitions;
- local `goto` / `label` resolution;
- no `on complete` lifecycle;
- read-only visited-system/world/material/reputation authority.

## Acceptance status

The branch was created while the new production build/parser CI was being completed. It must not be merged until it is rebased/transplanted onto the final parser-gate `main` and passes:

1. focused validator aggregate;
2. A1 pytest suite;
3. changed-file stock content-style gate;
4. real production `EndlessSky` compile;
5. stock `--parse-save` full-data/reference parse.

Save/load and actual gameplay runtime remain separate follow-up gates unless explicitly executed and recorded.
