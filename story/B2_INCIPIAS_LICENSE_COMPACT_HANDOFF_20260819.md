# B2 Incipias License Compact handoff — 2026-08-19

## Stage
B2 STORY CHARACTERS + DYNAMIC CONTENT

## Verdict
READY for A3 review/integration.

## Repository state
- Authoritative repository: `Wiredshark/star`
- Authoritative `main` observed before selection: `0d6b4ad3ebe659bfff5bc85275ed2161ae9d67c0`
- B1 parent branch/head: `agent/b1-incipias-early-spaceflight-institutions-20260819-0819` @ `70a673bee11e66bec81d12a7e9efc2ecf1a10612`
- B2 branch: `agent/b2-incipias-license-compact-20260819-0823`
- Production commit: `325e3c7c85885b81b61af80b10e7243a21eff253`
- Initial validator commit: `9d8efae5d7d1876bcc890b1760aafd6ee80ee702`
- Validator wording fixes: `4f1ee33dca578a5d6243015cb7cea5e57907f9da`, `d6da91c9994f973799388632c00cf4b9e08acb46`
- Exact repository-native validated production/data/validator/handoff head: `d6da91c9994f973799388632c00cf4b9e08acb46`

## Scope
Adds a three-mission recurring Incipias character arc that consumes B1's crew-license/private-spaceflight institutional history.

The player privately refers to two recurring Incipias as the **Registrar** and **Pilot**. Those are explicitly player-facing shorthands, not canonical Incipias names, titles, or offices.

### Offer
A veteran private pilot's safe work history does not map cleanly to a newer ship-license category. The player can favor:
1. strict category compliance;
2. demonstrated experience;
3. a provisional supervised renewal;
4. refusal.

### Review
The original decision produces a broader scaling problem as private spacecraft become common. The later choice resolves to one of two persistent models:
- **portable endorsement** — accepted evidence, supervision, ship class, and limits travel with the credential;
- **tiered renewal** — local discretion may keep an experienced crew flying, but portability requires a second independent review.

### Later reader
`Registrar Remembers` consumes either terminal settlement and records one-shot aftermath state.

## Ownership and canon invariants
- All persistent writes are namespaced under `B2 Incipias License Compact:*`.
- No `world:*`, credits, reputation, combat, cargo, outfit, ship, or fleet mutation.
- Uses existing `Conlatio` government scoping.
- Does not invent Incipias personal names, formal offices, hard chronology, government hierarchy, or Quarg/first-contact outcomes.
- Preserves B1's central continuity: Incipias are recently spacefaring, private spacecraft are becoming common, and formal institutions are still catching up with practical experience.
- Refusal does not set `introduced` and therefore does not enter the Review chain.

## Files
- `data/incipias/b2 incipias license compact.txt`
- `tools/story/validate_b2_incipias_license_compact.py`
- `story/B2_INCIPIAS_LICENSE_COMPACT_HANDOFF_20260819.md`

## Validation implemented
Focused validator checks:
- exact three-mission structure;
- Registrar/Pilot private-shorthand continuity;
- `Conlatio` scoping for all missions;
- three persistent initial routes plus refusal;
- exactly two terminal settlements;
- one-shot later reader;
- B2-only assignment writes;
- no direct material/reputation/combat/world mutation;
- local `goto`/`label` integrity;
- explicit B1 crew-license/private-spaceflight continuity;
- refusal isolation from the Review chain.

## Validation evidence
Exact validated head `d6da91c9994f973799388632c00cf4b9e08acb46`:
- `Fork simulation and story validation` run `32252843359`: **SUCCESS**.
- changed fork content style: **SUCCESS**.
- focused story validator discovery: **33 checks, all passed**, including `validate_b2_incipias_license_compact.py` after CI-driven wording repair.
- A1 simulation contract tests in the same repository-native workflow: **SUCCESS**.
- `Fork save-load integration smoke` run `32252843353`: **SUCCESS**.
- production executable configure/build: **SUCCESS**.
- stock save-load smoke cases: **SUCCESS**.

The B1 parent exact head `70a673bee11e66bec81d12a7e9efc2ecf1a10612` is also repository-native green for both simulation/story validation and save-load integration smoke.

## CI-driven repair history
The first two exact-head story runs correctly caught validator assertions that were stricter than the actual production wording (`private ships`, then `private spacecraft`). No production content was changed in response. The validator was corrected to test the exact production concept (`privately owned ship`) while retaining the intended B1 continuity check. The third exact-head run passed fully.

## A3 integration notes
Integrate the B1 Incipias early-spaceflight institutional-history parent first, then this B2 branch. Preserve the rule that `Registrar` and `Pilot` are player-private descriptors only. Do not reinterpret portable endorsements as a galaxy-wide license treaty or centralized Incipias bureaucracy.

## B3 continuity notes
The important tension is not standards versus no standards. It is how a young spacefaring society can preserve common, legible rules while recognizing practical experience without allowing local exceptions to become invisible precedent.
