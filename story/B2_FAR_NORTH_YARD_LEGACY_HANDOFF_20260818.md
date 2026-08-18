# B2 Far North Yard Legacy Handoff — 2026-08-18

## Verdict

**PARTIAL / SPECIALIST CANDIDATE — NOT YET A3-READY**

This isolated B2 slice turns the B1 Far North shipwright/apprenticeship history into named-character production content at Prime. It is intentionally non-overlapping with the active `Broken Compact` B2 branch: this slice is about training capacity, professional succession, and institutional memory rather than law/ownership.

## Repository authority and ancestry

- Repository: `Wiredshark/star`
- B1 parent branch: `agent/b1-far-north-history-20260818-1518`
- B1 parent/base SHA: `362ff1e344e4b0d220e94073a8df19432bd9b83c`
- B2 branch: `agent/b2-far-north-yard-20260818-1527`
- Production data commit: `84f91becd8bd00de306e2941c89b84e053fcfc56`
- Initial validator commit: `da6e12662e21fc702916955114f6d766d9bc3df1`
- Validator correction/current pre-handoff head: `44e9892827f75b13b38bec6988fb1b1c41829a08`

## Concurrency / non-duplication

Open B2 PR #4 already owns the `Broken Compact` Nadia Kelm / Elias Dorne / Mara Senn legal-ownership production slice. This branch does not touch those files, states, characters, or domain.

This slice instead consumes the newly added Far North historical theme from B1 PR #6: apprenticeship, repair knowledge, and local fabrication capacity as a regional institution.

## Production content

File: `data/human/b2 far north yard legacy.txt`

Named characters:

- **Tessa Vale** — senior shipwright who treats apprenticeship capacity as part of the yard's long-term production system.
- **Rowan Pike** — younger mechanic who initially prioritizes clearing the immediate repair backlog but can revise that position when evidence changes.

Three production missions:

1. `B2 Far North Yard Legacy: Offer`
   - Anchored at `Prime`, already established in stock Far North/Betelgeuse content.
   - Presents balanced triage, Vale/training-first, Pike/backlog-first, and refusal routes.
   - Persists the chosen approach and character attitude where relevant.

2. `B2 Far North Yard Legacy: Review`
   - Reads the initial route later.
   - Shows consequences rather than treating the first conversation as self-contained.
   - Produces one of two terminal institutional outcomes: protected training blocks or supervised production training.

3. `B2 Far North Yard Legacy: Vale Remembers`
   - Later reader for the terminal settlement.
   - Records one-shot aftermath consumption.

## Dynamic-content / persistence contract

- Uses stock mission, conversation, branch, action, and global-condition mechanisms only.
- Adds no save schema.
- Old saves default the new condition names to absent/zero.
- Does not create a separate relationship/apprenticeship database.
- The initial route is persistent and affects later dialogue.
- The institutional settlement is persistent and affects a later named-character reader.
- Refusal is valid persistent content rather than a reload-only failure state.

## B1 / A2 / world-state dependencies

- Direct thematic/ancestry dependency: B1 Far North shipwright/apprenticeship history (`362ff1e...`).
- No new A1 world-simulation primitive is required for this static proof.
- No A2 engine primitive is required; stock condition state is sufficient.
- Future generalized character-memory or labor-capacity systems should treat these B2 flags as migration/content inputs rather than introduce duplicate truth sources.

## Validation actually executed

A fresh isolated clone of this exact branch was created on the private execution host.

Executed at head `44e9892827f75b13b38bec6988fb1b1c41829a08`:

`python3 tools/story/validate_b2_far_north_yard_legacy.py`

Result:

- PASS: missions=3
- PASS: named_characters=2
- PASS: initial_routes=3
- PASS: review_routing=balanced fallthrough + explicit Vale/Pike branches
- PASS: terminal_settlements=2
- PASS: later_reader=Vale Remembers
- PASS: persistence_model=stock mission/global conditions

The isolated checkout remained clean after the validator.

The first validator execution correctly failed because it incorrectly required the balanced route to have an explicit later `has` read. The content intentionally uses balanced as the Review conversation fallthrough while Vale/Pike are explicit branches. The validator was corrected in commit `44e9892...` and then passed.

## Validation limitation

Attempted:

`python3 utils/check_content_style.py 'data/human/b2 far north yard legacy.txt'`

The checker could not start because the host lacks the third-party Python `regex` package:

`ModuleNotFoundError: No module named 'regex'`

This is an environment dependency failure, not a content-style pass or failure.

A normal configured Endless Sky parser/build/runtime/save-load proof was not completed in this B2 run, so the branch remains PARTIAL rather than READY.

## A3 / B3 integration notes

Before promotion/integration:

1. run the repository's normal content parser/data-load gate on `data/human/b2 far north yard legacy.txt`;
2. run content style validation in an environment with the required Python dependencies;
3. smoke-load Prime and verify all three missions parse/offer under intended conditions;
4. verify each initial route survives save/load into the Review mission;
5. verify exactly one terminal settlement is written and Vale's aftermath reads it correctly;
6. confirm Tessa Vale / Rowan Pike do not collide with concurrent accepted named-character content;
7. review this branch after its B1 parent ancestry rather than cherry-picking without the Far North history context.

If those gates pass without semantic corrections, this is a suitable B2 integration candidate.
