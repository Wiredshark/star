# B2 Wanderer Machine Custody Compact — handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** PARTIAL pending exact-head repository-native validation  
**Authoritative main observed at run start:** `bdeb9c4ba6c9d0203ff75532e38cd7f4334dbdd8`  
**Required B1 parent:** `d6e2c557f0fdbb64f1b73182dff6ed9730414f7f` (`agent/b1-korath-machine-war-memory-20260819-1719`)  
**Isolated B2 branch:** `agent/b2-wanderer-machine-custody-20260819-1726`  
**Production commit:** `1caf96888b0eac4285fb4dd720ecf69b996ec7d0`  
**Focused-validator commit:** `16ddb57c20d81da93a903f6e5d25bc01a75de7d7`

## Scope

Adds one persistent three-mission Wanderer character arc after the Mereti/Sestor machine war. It consumes B1's `Factory Deactivation Provenance Ledger` and `Autonomous Weapon Custody Record` and turns those historical institutions into a present-day research/custody dispute.

Two recurring Wanderers are identified only through the player's private shorthand:

- **Curator** — prioritizes evidentiary provenance, sealed originals, and chain of custody;
- **Engineer** — prioritizes bounded isolated study of dangerous machine-control material.

These are not asserted as canonical Wanderer names, titles, offices, or political institutions.

## Player-facing behavior

### Offer — `The Core and the Copy`

A recovered autonomous-machine control core still contains partially readable control logic. The player can support:

1. **custody-first** — keep the original sealed and require provenance review before later study;
2. **sandbox-first** — permit an isolated working image while recording every transformation;
3. **paired evidence/research** — preserve an untouched original and a permanently linked derived image;
4. **refusal** — leave the Wanderers' disagreement unresolved rather than converting visitor preference into policy.

Each substantive route schedules a delayed Review after 7–11 days. Refusal does not schedule Review.

### Review — `A Copy With No Battlefield`

The second-order failure is information loss as machine-analysis results are copied: conclusions can survive while recovery context, unreadable regions, reconstruction steps, or uncertainty disappear.

The Review resolves into one of exactly two persistent settlements:

- **transferable custody packet** — recovery source, custody history, extraction method, transformations, uncertainty, and responsible research chain travel with every derivative;
- **two-key derivative review** — dangerous/historical claims based on derivatives require independent reexamination tied back to the sealed original.

### Later reader — `Engineer Remembers`

A one-shot aftermath scene demonstrates the selected settlement without creating a new campaign state owner.

## Dependencies / continuity

B1 parent requirements:

- `wanderers sestor done`;
- `Wanderer History: Factory Deactivation Provenance Ledger: offered`;
- `Wanderer History: Autonomous Weapon Custody Record: offered`.

Continuity invariant: this content may reason about recovered machine evidence, provenance, derivatives, uncertainty, and dangerous-technology custody, but it must not invent definitive Mereti/Sestor original directives, universal machine motives, Builder intent, or a new Wanderer political authority.

The historical fact that Korath exiles removed enough Sestor technology to begin producing their own war drones remains upstream B1/campaign context; this B2 slice does not transfer ownership of that fact or imply all machine technology is controlled by any one faction.

## State ownership

All new persistent writes are under:

`B2 Wanderer Machine Custody Compact:*`

The slice does **not** write:

- `world:*` simulation state;
- `wanderers sestor done`;
- `Wanderer History:*` B1 state;
- credits or reputation;
- cargo, outfits, ships, fleets, or combat rating.

No save-format/schema change is introduced; persistence uses ordinary mission/event conditions.

## Isolation evidence

At production+validator head `16ddb57c20d81da93a903f6e5d25bc01a75de7d7`, exact B1-parent-to-B2 comparison is:

- 2 commits ahead / 0 behind;
- exactly 2 added files;
- production content: 154 additions;
- focused validator: 171 additions;
- 0 deletions.

No unrelated files were modified.

## Validation added

Focused validator:

`python3 tools/story/validate_b2_wanderer_machine_custody_compact.py "data/wanderer/b2 wanderer machine custody compact.txt"`

It checks:

- exact 3-mission graph;
- 3 substantive routes + refusal;
- delayed Review scheduling only on substantive routes;
- exactly 2 terminal settlements;
- one-shot aftermath persistence;
- Wanderer/B1 gating;
- local `goto`/`label` integrity;
- B2-only write ownership;
- absence of material/reputation/world/B1 mutation;
- custody/provenance/derivative/uncertainty concepts;
- prohibition on unsupported machine-war motive certainty;
- Curator/Engineer player-private-shorthand boundary.

## Remaining acceptance gates

Before READY/A3 integration, require repository-native validation on the exact final B2 head:

1. `Fork simulation and story validation` terminal green, including changed-content style and focused validators;
2. `Fork save-load integration smoke` terminal green, including production Endless Sky build and stock persistence tests;
3. actual-game acceptance when available for:
   - B1 prerequisite gating;
   - all 3 substantive Offer routes;
   - refusal negative path;
   - delayed Review timing;
   - both terminal settlements;
   - one-shot `Engineer Remembers` aftermath;
   - save/reload between Offer and Review and after settlement;
   - offer-precedence/regression alongside existing Wanderer postwar content.

No validation success is claimed until the corresponding exact-head run is observed terminal green.

## A3 / B3 integration notes

- Integrate/accept the B1 Wanderer machine-war institutional-history parent first.
- Re-read then-current `main` before integration because concurrent A/B work is expected.
- Preserve the distinction between **sealed original evidence**, **derived research copies**, and **interpretive conclusions**.
- Preserve the distinction between machine behavior observed in the war and later guesses about original directives or motives.
- Curator/Engineer remain player-private shorthand.
- Do not self-integrate from B2.
