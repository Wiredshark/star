# B2 Bunrodea Cross-Rank Friendship Compact handoff — 2026-08-26

Verdict: PARTIAL pending repository-native validation.

## Authority / isolation
- Repository authority: `Wiredshark/star`.
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/b2-bunrodea-cross-rank-friendship-20260826`.
- Production commit: `a0893ecb97a734172446ddec306640abcebdb8ba`.
- Focused validator commit: `e9909b4f46b5638de85bc2dd650fa22742ee2c7d`.
- No self-integration. A3 retains integration authority.

## Character / dynamic-content behavior
Adds recurring Bunrodea characters Rii Kes, a Megasa maintenance supervisor, and Tava Rei, an Erabu archivist and longtime friend. A historically real household register still places Rii under an old retainer category from their youth. A copied petition file treats that old category as though Tava still has present representative authority over Rii.

Player routes:
1. preserve history and friendship while requiring present consent for present authority;
2. bind historical rank/status labels to the duties and time period they actually described;
3. maintain paired historical-household/current-relationship-and-authority records;
4. refusal, which neither introduces the arc nor schedules Review.

Each substantive route schedules Review after 7–11 days. Review resolves into either:
- a portable relationship-and-authority packet, carrying historical status, current relationship, current duties, explicit authority, source date, and closure together; or
- fresh-authority renewal, where present representation exists only through a current explicit delegation for a named purpose.

`Rii Remembers` is a one-shot aftermath reader.

## Dependencies / ownership
Read-only:
- `Bunrodea History: Megasa Freight Register: offered`.

Writes only:
- `B2 Bunrodea Cross-Rank Friendship Compact:*`.

No `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation is intended. All seven dialogue/state-only terminals use `decline`; zero `accept` terminals are intended.

## Files
- `data/bunrodea/b2 bunrodea cross rank friendship compact.txt`
- `tools/story/validate_b2_bunrodea_cross_rank_friendship.py`
- `story/B2_BUNRODEA_CROSS_RANK_FRIENDSHIP_COMPACT_HANDOFF_20260826.md`

## Focused validator contract
The validator checks:
- exactly three missions and both recurring characters;
- B1 history gate;
- route-local writes and exactly one delayed Review schedule per substantive route;
- refusal suppression of `introduced`, all substantive routes, and Review scheduling;
- Review lifecycle gates and deliberate present-consent fallthrough;
- two settlement-local writes with one Review closure each;
- two-settlement one-shot aftermath consumption;
- seven `decline` / zero `accept` terminals and no gameplay-objective directives;
- B2-only assignment ownership;
- local goto/label integrity;
- canon boundary between historical rank, genuine friendship, and present authority.

## Validation required before READY
Run repository-native gates on the exact production/validator/handoff candidate:
- `Fork simulation and story validation` (focused validators, A1 state-ownership/simulation contracts, changed-content style);
- `Fork save-load integration smoke` (production configure/build plus stock save-load smoke).

Do not promote READY until both are terminal green on an exact candidate whose production and validator files are unchanged afterward.

## Persistence / canon assumptions
- The old Bunrodea hierarchy remains historical fact; the slice does not pretend rank never mattered.
- Rii and Tava's friendship is also genuine history and present relationship.
- Historical household status does not automatically grant present representation, sponsorship, dependence, or command authority.
- Present authority requires explicit current evidence.
- This is one local Bunrodea dispute, not universal Bunrodea social law.

## A3 / B3 integration notes
- Re-read current `main`, ancestry, open B1/A2/B2 work, mergeability, and exact workflow state immediately before integration.
- Preserve B1 history as read-only.
- Preserve the distinction among historical status, friendship, current duties, current authority, and explicit closure.
- Do not integrate until exact repository-native gates are green.
