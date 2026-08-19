# B2 Korath Recovery Compact — handoff

## Status

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** PARTIAL pending exact-head repository-native simulation/story/style and production save-load validation.  
**Authoritative `main` observed at slice selection:** `5928089939e8dc7806deb2775a9030a3ba5bf9bb`  
**Required B1 parent:** `2a1ca58ac0dc1156b1409fff229e0fd4d3210f1c` (`agent/b1-korath-exile-institutions-20260819-1819`)  
**B2 branch:** `agent/b2-korath-recovery-compact-20260819-1828`  
**Production commit:** `d3faaf94071f98741a2292c0646587ad7a7d342d`  
**Focused validator commit / pre-handoff head:** `f0c61068066e017493366b028127d63f393f6fb5`

## Scope

Adds a persistent three-mission Remnant character arc that consumes the B1 Korath Exile Raid Ledger and Recovery and Containment Ledger.

Two recurring Remnant specialists are referred to only through player-private shorthand:

- **Medic** — prioritizes lifesaving treatment and the humanitarian obligations of recovery work.
- **Analyst** — prioritizes provenance, evidence continuity, restitution, and preserving what was actually recovered.

The first dispute concerns medical supplies recovered from a disabled Korath exile ship while a wounded Korath survivor is being treated. Some containers may also be stolen civilian property or evidence of earlier raids. The player may choose:

1. treatment-first emergency use;
2. provenance-first emergency release records;
3. paired recovery + humanitarian-use records;
4. refusal.

The later Review exposes a second-order records problem: medical and evidentiary copies can each remain individually accurate while becoming misleading when separated. The player resolves that into one of two persistent terminal settlements:

- **linked recovery packet** — downstream copies carry recovery origin, humanitarian releases, remaining quantity, unresolved ownership claims, and a source-ledger reference;
- **reconciliation checkpoint** — medical and evidence records remain institutionally separate, but restitution/prosecution/technical-transfer closure requires both records to be compared and unresolved disagreement preserved.

`Medic Remembers` is the one-shot later reader.

## B1 / canon dependencies

This slice requires:

- `Remnant: Cognizance 2: done`;
- `Remnant History: Korath Exile Raid Ledger: offered`;
- `Remnant History: Korath Recovery and Containment Ledger: offered`.

The B1 parent establishes two important continuity rules that B2 preserves:

1. stolen mundane supplies can be evidence of material pressure without proving one universal Korath exile motive or excusing raid harm;
2. rescue, evidence preservation, technical study, disposal, and restitution are distinct aftermath obligations.

B2 does not invent a unified Korath exile command structure, a new Korath political institution, or a single centralized Remnant policy for every Korath encounter.

## State ownership / persistence

All new writes are namespaced under `B2 Korath Recovery Compact:*`.

The slice does not write:

- B1 history gates;
- `Remnant: Cognizance 2: done`;
- any `world:*` variable;
- credits or reputation;
- cargo, outfits, ships, fleets, or combat rating;
- Korath campaign state.

The B2 state is ordinary mission/global-condition state and therefore follows the existing persistence model; no save schema is introduced.

## Files

- `data/korath/b2 korath recovery compact.txt`
- `tools/story/validate_b2_korath_recovery_compact.py`
- `story/B2_KORATH_RECOVERY_COMPACT_HANDOFF_20260819.md`

## Focused validator contract

`tools/story/validate_b2_korath_recovery_compact.py` checks:

- exact three-mission graph;
- Medic/Analyst private-shorthand continuity;
- Remnant scoping and exact B1/campaign gates;
- three persistent routes plus refusal;
- exactly two terminal settlements;
- one-shot later reader;
- B2-only write ownership;
- no direct material/reputation/world-state mutations;
- local `goto`/`label` integrity;
- presence of rescue/provenance/restitution/ownership/evidence concepts;
- no universal unsupported Korath-motive claim;
- decline path does not set `introduced`.

## Concurrency / non-overlap

Live open PRs and B2 branch inventory were inspected before authoring. No Korath-exile-specific B2 branch was present. The newly opened B1 Korath exile institutional-history branch is the intended dependency. Existing B2 work covers other human/alien institutional slices and is not modified here.

The current A1 and A2 work on `main` was also inspected. This B2 slice does not touch Republic customs, Hicemus contact practice, or other active A-lane state.

## Validation status

At handoff creation time, repository-native exact-head workflows have not yet been observed on the B2 candidate. No PASS is claimed yet.

Required before READY / A3 integration:

1. `Fork simulation and story validation` must succeed on the exact B2 head, including focused-validator discovery and changed-content style.
2. `Fork save-load integration smoke` must succeed on the exact B2 head, including production configure/build and stock persistence smoke.
3. The required B1 parent must itself be accepted/green before B2 integration.
4. A3 should still perform actual-game acceptance when practical: post-Cognizance/B1 gating, all three routes, refusal, both Review settlements, save/reload between stages, aftermath one-shot suppression, and Remnant/Korath offer-precedence regression.

## A3 / B3 integration notes

Integration order is **B1 Korath exile institutional history first, then B2 Korath Recovery Compact**.

Preserve these invariants:

- humanitarian treatment does not settle ownership;
- provenance does not authorize delaying lifesaving care indefinitely;
- evidence of material shortages does not prove a single Korath motive or erase raid harm;
- a recovered-cargo record and a medical-use record can be linked without becoming the same record;
- Medic/Analyst remain player-private shorthand, not formal Remnant offices.

Do not self-integrate from B2.
