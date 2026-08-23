# B2 Pirate Harbor Peace Compact Handoff — 2026-08-23

## Verdict
READY for A3 review/integration.

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-pirate-harbor-peace-compact-20260823`
- Production commit: `c46ce020039e5754e0837ce51785ec93304129cf`
- Initial focused-validator commit: `6bb813d89e8e572086c87b7e186b8a155392ee45`
- Validator wording repair / exact fully validated candidate: `937104d6274e304e4c374bb1055da6f20e23e590`
- Final READY handoff-only commit: this document update; PR #271 records the exact final tip.

## PRIMARY_DOMAIN
Law / personal autonomy / feud boundaries.

## RECENT_DOMAIN_WINDOW
Recent B2 work emphasized family memory/privacy, rescue handoffs, cultural lineage, volunteer command, command-principle mentorship, irrigation/resource obligations, and lifecycle repairs.

## DIVERSITY_STATUS
DIVERSE. This slice deliberately avoids freight, market, resource scarcity, another archival-family dispute, medical handoff, and military deployment. Its core question is whether limited pirate harbor neutrality protects a person's exit from a crew without turning departure into immunity, custody, or permanent suspicion.

## NEGLECTED_AREA_ADVANCED
Pirate interpersonal law-like practice, crew autonomy, defection, feud boundaries, and local safe-harbor norms.

## CROSS_SYSTEM_CONNECTION
Consumes B1 `Pirate Safe Harbor Register: offered` read-only. No world-state write. The content uses existing mission/conversation/event/condition support only.

## Behavior
Adds recurring harbor mediator Rhea Corbin, pirate captain Jory Kade, and gunner Sima Voss.

Offer routes:
1. protect Sima's right to exit while inside neutral harbor;
2. allow a bounded safety delay with explicit end conditions;
3. separate freedom of movement from a narrow expiring information obligation;
4. refusal.

Each substantive route schedules a 7–11 day Review. Review addresses copied safe-harbor records that collapse movement protection, temporary precautions, later accusations, and evidentiary status. It resolves to either:
- a portable harbor-status packet; or
- expiry plus fresh-cause review.

`Sima Remembers` is the one-shot aftermath reader.

## Persistence / ownership
All direct writes are `B2 Pirate Harbor Peace Compact:*`.

B1 `Pirate Safe Harbor Register: offered` is read-only. No `world:*`, credits, reputation, cargo, outfits, ships, fleets, combat, or unrelated story-state mutation.

All 7 state-only terminal paths use `decline`; no objective-less `accept` mission is introduced.

## Canon assumptions
- Pirate safe-harbor conventions remain local, contingent, and commercially enforced rather than universal law.
- A captain does not own a crew member merely because the crew is under repair or feud pressure.
- A protected departure does not prove innocence of later accusations.
- A temporary precaution does not prove guilt and must not become permanent inherited suspicion after its trigger expires.
- Movement restrictions, information obligations, accusations, evidence, and disposition remain separate facts.

## Validation
The first simulation/story run on the pre-repair candidate failed only because the focused validator demanded the literal phrase `does not automatically prove`; production already expressed the intended invariant as `None of those entries automatically proves another.` The validator wording was repaired without changing production behavior.

Exact fully validated candidate `937104d6274e304e4c374bb1055da6f20e23e590`:
- `Fork simulation and story validation` #501 / run `32667727732`: SUCCESS.
- focused story validators: SUCCESS.
- A1 simulation/state-ownership contracts: SUCCESS.
- changed-content style: SUCCESS.
- `Fork save-load integration smoke` #486 / run `32667727729`: SUCCESS.
- production configure/build: SUCCESS.
- stock save-load integration smoke: SUCCESS.

Exact base-to-validated-candidate comparison: 4 commits ahead / 0 behind, with exactly three changed files and no deletions.

## Files changed
- `data/human/b2 pirate harbor peace compact.txt`
- `tools/story/validate_b2_pirate_harbor_peace_compact.py`
- `story/B2_PIRATE_HARBOR_PEACE_COMPACT_HANDOFF_20260823.md`

## Risks / deferred work
No manual actual-game narrative walkthrough is claimed beyond repository-native validation. The characters are new B2 local Pirate characters and do not create a central pirate office or universal legal authority.

## A3 / B3 integration notes
Re-read current `main` immediately before integration. Preserve B1 read-only ownership, B2 namespace isolation, the 7/7 state-only `decline` lifecycle, and the distinction among protected movement, temporary precaution, later accusation, fresh evidence, expiry, and disposition. Do not self-integrate from B2.
