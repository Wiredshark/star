# A2 Republic Customs Review handoff — 2026-08-19

## Portfolio labels

- `LOOP_ID`: A2
- `RUN_TYPE`: FEATURE / CONTENT
- `PRIMARY_DOMAIN`: crime / investigation / law
- `SECONDARY_DOMAINS`: modern dialogue, persistent history, border-security state
- `DIVERSITY_STATUS`: PASS
- `NEGLECTED_AREA_ADVANCED`: legal process / investigation rather than freight or institutional logistics
- `CROSS_SYSTEM_CONNECTION`: A1 Republic customs scrutiny + A1 Republic border pressure + stock pirate-job history

## Production content

File: `data/human/a2 republic customs review.txt`

Named characters:
- **Elian Ward** — Republic customs examiner;
- **Sera Noll** — port-rights observer.

### Stage 1 — Secondary Review

Offers on inhabited Republic worlds while `world: republic customs scrutiny >= 3`.

The opening changes when `world: republic border pressure >= 4`, distinguishing the broad security posture from evidence about the individual captain.

Four persistent response routes:
1. bounded document-only audit;
2. written factual basis / challengeable record;
3. visible-disabled underworld-context response at `pirate jobs >= 5`;
4. refusal of an informal interview pending formal process or counsel.

Every route schedules a later disposition but does not alter the A1 scrutiny signal.

### Stage 2 — Disposition

Offers only after A1 naturally reduces `world: republic customs scrutiny` below 3.

Each route produces a distinct durable outcome:
- bounded audit;
- written uncertainty;
- contextualized routing analysis;
- preserved refusal / no adverse inference.

A2 does not clear scrutiny to make this stage appear; A1 recovery remains authoritative.

### Stage 3 — Noll Remembers

Consumes the disposition outcome later and lets the player decide whether the procedure may be reused as a bounded precedent or whether the case should remain private.

## Authority invariants

Read-only inputs:
- `world: republic customs scrutiny`;
- `world: republic border pressure`;
- `pirate jobs`.

Writable state is limited to `A2 Republic Customs Review:*` persistent conditions.

No reputation, credits, cargo, outfits, ships, combat state, pirate-job history, border pressure, or customs scrutiny is mutated by A2.

## Focused validator

`tools/story/validate_a2_republic_customs_review.py` checks:
- exact three-stage mission graph;
- Republic non-station source scoping;
- two named characters;
- high-scrutiny offer gate and low-scrutiny disposition gate;
- border-pressure reader;
- visible-disabled underworld response;
- all four route writes and four outcomes;
- later-reader consumption and privacy choice;
- local `goto` / `label` resolution;
- no `on complete` lifecycle;
- no meta/developer wording marker;
- no writes to A1/stock authorities or material/reputation actions.

The exact repository checkout could not be executed locally because the environment cannot resolve `github.com`, so the focused validator, content-style checker, normal parser/build, actual-game runtime, and save/load roundtrip are not claimed as executed. The production file and validator were reviewed through the GitHub connector before integration.
