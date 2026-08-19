# B2 Incipias License Compact handoff — 2026-08-19

## Stage
B2 STORY CHARACTERS + DYNAMIC CONTENT

## Verdict
PARTIAL pending exact-head repository-native validation.

## Repository state
- Authoritative repository: `Wiredshark/star`
- Authoritative `main` observed before selection: `0d6b4ad3ebe659bfff5bc85275ed2161ae9d67c0`
- B1 parent branch/head: `agent/b1-incipias-early-spaceflight-institutions-20260819-0819` @ `70a673bee11e66bec81d12a7e9efc2ecf1a10612`
- B2 branch: `agent/b2-incipias-license-compact-20260819-0823`
- Production commit: `325e3c7c85885b81b61af80b10e7243a21eff253`
- Validator commit: `9d8efae5d7d1876bcc890b1760aafd6ee80ee702`

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

## Validation status
At handoff creation time, repository-native PR validation has not yet completed on the exact B2 head. Do not promote this handoff to READY until:
1. `Fork simulation and story validation` succeeds on the exact production/validator/handoff head or an exact successor containing only handoff-status wording;
2. changed-content style succeeds;
3. the focused validator is included in the repository-wide story validator discovery and passes;
4. production build/save-load integration smoke succeeds or A3 explicitly documents and accepts a narrower non-persistence boundary.

## A3 integration notes
Integrate the B1 Incipias early-spaceflight institutional-history parent first, then this B2 branch. Preserve the rule that `Registrar` and `Pilot` are player-private descriptors only. Do not reinterpret portable endorsements as a galaxy-wide license treaty or centralized Incipias bureaucracy.

## B3 continuity notes
The important tension is not standards versus no standards. It is how a young spacefaring society can preserve common, legible rules while recognizing practical experience without allowing local exceptions to become invisible precedent.
