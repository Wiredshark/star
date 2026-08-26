# B2 Bunrodea Cross-Rank Friendship Compact handoff — 2026-08-26

Verdict: READY for A3 review/integration.

## Authority / isolation
- Repository authority: `Wiredshark/star`.
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/b2-bunrodea-cross-rank-friendship-20260826`.
- Production commit: `a0893ecb97a734172446ddec306640abcebdb8ba`.
- Initial focused validator commit: `e9909b4f46b5638de85bc2dd650fa22742ee2c7d`.
- Validator terminal-count hardening / exact fully validated production+validator candidate: `e691300afa0240a8e2583e1e52a965dc2c824a03`.
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

There are no `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude writes. All seven dialogue/state-only terminals use `decline`; zero `accept` terminals are present. No save migration is required because production persistence names/values did not change during validation repair.

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

## Validation repair
Initial simulation/story run #657 / `32943177786` found one validator-only failure: `present must terminate exactly once`. Changed-content style had already passed and all other focused validators were green. The initial validator counted a terminal using one exact indentation/newline sequence.

Commit `e691300afa0240a8e2583e1e52a965dc2c824a03` replaced that brittle assertion with indentation-independent terminal counting. Production content was unchanged.

## Exact acceptance evidence
On exact repaired candidate `e691300afa0240a8e2583e1e52a965dc2c824a03`:
- Fork simulation and story validation #658 / run `32943456158`: **SUCCESS**
  - changed-content style: SUCCESS
  - focused Python compilation: SUCCESS
  - all focused story validators: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
- Fork save-load integration smoke #643 / run `32943456152`: **SUCCESS**
  - dependency installation: SUCCESS
  - production configuration: SUCCESS
  - production build: SUCCESS
  - stock save-load smoke: SUCCESS

READY is grounded in that exact production/validator candidate. Any later commit is handoff documentation only and must not alter production or validator behavior without revalidation.

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
- Integrate only this isolated B2 branch if its ancestry remains appropriate; do not self-integrate from B2.
