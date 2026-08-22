# B2 Korath Recovery Compact — handoff

## Status

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** READY for A3 review/integration  
**Authoritative `main` rechecked during lifecycle recovery:** `a17a89fb4779200a0634a6dade1811c4dc9cc2be`  
**Required B1 parent:** `2a1ca58ac0dc1156b1409fff229e0fd4d3210f1c` (`agent/b1-korath-exile-institutions-20260819-1819`)  
**B2 branch:** `agent/b2-korath-recovery-compact-20260819-1828`  
**Original production commit:** `d3faaf94071f98741a2292c0646587ad7a7d342d`  
**Original pre-recovery head:** `5ac396ad823c74ca69c8af87e07730f1fe60ece1`  
**Lifecycle production repair:** `700773a18d1357c22e61e8cc68ed48e532d761ba`  
**Lifecycle validator / exact fully validated candidate:** `cf10da285217a18fdf4725dee0cf496ad6f923e5`

## Scope

Adds a persistent three-mission Remnant character arc that consumes the B1 Korath Exile Raid Ledger and Recovery and Containment Ledger.

Two recurring Remnant specialists are referred to only through player-private shorthand:

- **Medic** — prioritizes lifesaving treatment and the humanitarian obligations of recovery work.
- **Analyst** — prioritizes provenance, evidence continuity, restitution, and preserving what was actually recovered.

The initial dispute supports treatment-first, provenance-first, paired recovery/humanitarian records, or refusal. The later Review resolves to either a linked recovery packet or reconciliation checkpoint. `Medic Remembers` is the one-shot aftermath reader.

## Lifecycle recovery

The original content used six terminal `accept` commands in state-only dialogue paths: three positive Offer routes, two Review settlements, and the aftermath reader. Those missions create no destination, cargo, NPC, timer, waypoint, passenger, or other gameplay objective, so the accepted mission lifecycle could leave objective-less missions active.

Commit `700773a18d1357c22e61e8cc68ed48e532d761ba` changes exactly those six terminals to `decline`. Refusal already declined, so the slice now has exactly seven clean state-only terminal paths.

`tools/story/validate_b2_korath_recovery_compact_lifecycle.py` was added to require:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing destination/stopover/waypoint/NPC/cargo/passenger/deadline/timer directives;
- preservation of the three-mission graph and both terminal settlements.

The original focused structural validator remains in place.

## B1 / canon dependencies

Requires:

- `Remnant: Cognizance 2: done`;
- `Remnant History: Korath Exile Raid Ledger: offered`;
- `Remnant History: Korath Recovery and Containment Ledger: offered`.

Preserve these boundaries:

1. stolen mundane supplies can be evidence of material pressure without proving one universal Korath exile motive or excusing raid harm;
2. rescue, evidence preservation, technical study, disposal, restitution, ownership claims, and medical use remain distinct aftermath facts;
3. Medic/Analyst are player-private shorthand rather than formal Remnant offices;
4. no centralized Remnant policy for every Korath encounter is implied.

## State ownership / persistence

All writes remain namespaced under `B2 Korath Recovery Compact:*`.

B2 does not write B1 gates, `Remnant: Cognizance 2: done`, `world:*`, credits, reputation, cargo, outfits, ships, fleets, combat rating, or Korath campaign state. No persistent condition names or values changed during the lifecycle repair, so no save-state migration is required.

## Exact validation

Required B1 parent `2a1ca58ac0dc1156b1409fff229e0fd4d3210f1c` is terminal green:

- `Fork simulation and story validation` run `32308429839` / #136: **SUCCESS**
- `Fork save-load integration smoke` run `32308429869` / #125: **SUCCESS**

Original B2 head `5ac396ad823c74ca69c8af87e07730f1fe60ece1` also later reached green on both original workflows.

Exact lifecycle-repaired candidate `cf10da285217a18fdf4725dee0cf496ad6f923e5` is terminal green:

- `Fork simulation and story validation` run `32593931814` / #421: **SUCCESS**
- `Fork save-load integration smoke` run `32593931813` / #406: **SUCCESS**

The repaired diff from the prior B2 head is isolated: six production `accept -> decline` replacements plus the focused lifecycle validator.

## A3 / B3 integration notes

Integration order remains **B1 Korath exile institutional history first, then B2 Korath Recovery Compact**.

Preserve these invariants:

- humanitarian treatment does not settle ownership;
- provenance does not authorize delaying lifesaving care indefinitely;
- evidence of material shortages does not prove a single Korath motive or erase raid harm;
- a recovered-cargo record and a medical-use record can be linked without becoming the same record;
- dialogue/state-only B2 missions terminate with `decline`; `accept` is reserved for mission paths that create actual gameplay objectives.

A3 should still perform actual-game acceptance when practical: post-Cognizance/B1 gating, all three routes, refusal, both Review settlements, save/reload between stages, aftermath one-shot suppression, and Remnant/Korath offer-precedence regression.

Do not self-integrate from B2.
