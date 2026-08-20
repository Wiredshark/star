# A2 Syndicate Qualification Practice handoff — 2026-08-20

## Verdict

PARTIAL pending exact-head repository-native validation and actual-game acceptance.

## Authority

- Repository: `Wiredshark/star`
- Authoritative base: `main@95fdb069b0a56d990f75a59b0c44fe9d6401038d`
- Branch: `agent/a2-syndicate-qualification-practice-20260820-0307`
- Production commit: `ab574d1ef619d63d6160067c61f55ae1a9999a8f`
- Validator commit: `af85dac4d7322cdfecb67ab157539cda9c8a87f2`

## Scope

Consumes the integrated B2 Syndicate Qualification Compact after `aftermath seen`. Mara Venn asks what part of that resolved compact the player wants to carry into later labor-pressure advice.

Positive practices are:

1. evidence-first: carried evidence is the starting point and local review focuses on the job-specific gap;
2. boundaries-travel: scope, exclusions, supervision, and expiry context travel with the qualification;
3. local-only: preserve the compact as inspectable precedent without turning it into borrowed authority.

The player may also refuse to establish a standing doctrine. Refusal does not arm the later pressure test.

A later A1 labor rotation (`world: syndicate labor strain >= 2` plus `world: syndicate labor rotation active`) produces a route-specific one-shot consequence. The loop therefore connects resolved B2 institutional memory to a later recurrence of authoritative A1 world pressure.

## Invariants

- A1 remains sole writer of Syndicate labor strain / rotation state.
- B2 remains sole writer of Qualification Compact state.
- All new writes are `A2 Syndicate Qualification Practice:*`.
- Transferable qualification evidence is not blanket local job authority.
- The compact remains voluntary/practical among participating yards, not universal Syndicate labor law.
- This slice does not modify Tessa Marr maintenance state or the separate A2 parts-practice candidate.

## Files

- `data/human/a2 syndicate qualification practice.txt`
- `tools/story/validate_a2_syndicate_qualification_practice.py`
- `story/A2_SYNDICATE_QUALIFICATION_PRACTICE_HANDOFF_20260820.md`

## Validation required

Run the repository-native exact-head story/simulation/style workflow and save-load integration smoke. Then observe in game: B2 aftermath gating, all three positive practices plus refusal, later labor-rotation pressure test, save/reload persistence, one-shot suppression, and Syndicate offer-precedence behavior.

Do not self-integrate; A3 owns integration.
