# B2 Merchant Salvage Claim Compact Handoff — 2026-08-21

## Stage
B2 STORY CHARACTERS + DYNAMIC CONTENT

## Verdict
READY for A3 review/integration. Do not self-integrate.

## Repository authority
- Repository: `Wiredshark/star`
- Authoritative base/main recovered at run start and rechecked after validation: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-merchant-salvage-claim-compact-20260821-0026`
- Production commit: `64d18015f3c54549dc0f6edf0b2340d255a1dd21`
- Focused validator commit: `c529616b260154df14f6d130ecc16d077b249fb8`
- Exact fully validated production/validator/handoff candidate: `d1736ad90ccf88c4cb64948736c4958755c7fe48`

## Scope
Adds a persistent Merchant salvage character arc grounded in two already-authoritative inputs:

1. B1 `Merchant Salvage Provenance Ledger: offered`, which records recovery location, ship identity, claimant history, custody, and repair provenance as the institutional response to duplicate claims, stripped identifiers, theft, and vanished repair history.
2. A1 `world: merchant salvage demand`, a bounded authoritative simulation signal raised by sustained rescue overload and independently recovered on an eight-day contribution horizon.

B2 reads those inputs but never writes them.

### Characters
- **Tessa Arlen** — Merchant salvage broker focused on claim/provenance continuity.
- **Bram Voss** — Merchant yard mechanic focused on emergency technical reuse during salvage scarcity.

### Initial conflict
At salvage demand `>= 3`, a recovered drive component can return another ship to service, but two claim records name different owners.

Player routes:
- provenance-first transfer discipline;
- emergency reuse after technical inspection while ownership remains explicitly unresolved;
- paired immutable provenance + operational-use records;
- refusal.

Each substantive route schedules a 7–11 day delayed Review.

### Review
After authoritative A1 salvage demand recovers to `<= 1`, Tessa and Bram discover that downstream copies can collapse distinct facts. A short yard summary may say a component is cleared for use while dropping temporary-custody status, unresolved ownership, repair assumptions, or later closure evidence.

Terminal settlements:
- **portable claim packet** — recovery source, claimants, custody transfers, identification, known repairs, technical-use status, compatibility assumptions, unresolved disputes, and closure evidence travel together;
- **custody reconciliation** — operational custody and ownership claims remain separate linked records until transfer, return, compensation, abandonment, or another explicit disposition closes the dispute.

`Tessa Remembers` is the later one-shot consequence reader.

## Ownership / canon invariants
- A1 remains sole writer of `world: merchant salvage demand`.
- B1 Merchant history remains read-only.
- Every new persistent write is `B2 Merchant Salvage Claim Compact:*`.
- No direct credits, reputation, cargo, outfit, ship, fleet, combat, or world-state mutation.
- Technical fitness does not prove ownership.
- Possession/custody does not prove entitlement.
- Successful emergency use does not silently close an unresolved claim.
- Scarcity may justify temporary use, but it makes provenance more important rather than less.
- Practical Merchant salvage conventions do not create a centralized Merchant salvage court, government, or universal law.
- Dialogue-only state missions terminate with `decline` rather than leaving objective-less accepted missions.

## Concurrency / process safety
Before branching, live main, recent commits, open B2/A2/A1 PRs, and existing Merchant B2 coverage were inspected. Existing Merchant B2 work covers recovery margin and route diversion; no Merchant salvage-claim/provenance B2 slice was found. The private execution service reported 4 pre-existing service-owned orphan processes; none were killed, cancelled, or modified.

## Files
- `data/human/b2 merchant salvage claim compact.txt`
- `tools/story/validate_b2_merchant_salvage_claim_compact.py`
- `story/B2_MERCHANT_SALVAGE_CLAIM_COMPACT_HANDOFF_20260821.md`

## Focused validator contract
`tools/story/validate_b2_merchant_salvage_claim_compact.py` checks:
- exact three-mission graph;
- both named characters;
- B1 provenance dependency;
- A1 salvage-demand high/recovery gating;
- A1 world-state read-only ownership;
- 7–11 day delayed Review;
- three substantive routes plus refusal;
- exactly two terminal settlements;
- one-shot aftermath reader;
- dialogue-only lifecycle uses `decline`;
- B2-only persistent writes;
- local goto/label integrity;
- provenance/custody/technical-fitness/ownership/closure distinctions;
- absence of invented centralized Merchant salvage authority.

## Exact validation evidence
On exact candidate `d1736ad90ccf88c4cb64948736c4958755c7fe48`:
- `Fork simulation and story validation` #298 / run `32447142254`: **SUCCESS**.
- `Changed fork content style`: **SUCCESS**.
- `Focused simulation and story contracts`: **SUCCESS**, including compile and automatic execution of the new Merchant salvage validator.
- A1 simulation/state-ownership contracts: **SUCCESS**.
- `Fork save-load integration smoke` #283 / run `32447142259`: **SUCCESS**.
- Production configure: **SUCCESS**.
- Production build: **SUCCESS**.
- Stock save-load smoke cases: **SUCCESS**.

The READY promotion commit changes only this durable handoff; production content and validator behavior are unchanged from the exact fully validated candidate above.

## Isolation evidence
Exact base-to-validated-candidate comparison:
- 3 commits ahead / 0 behind;
- exactly 3 added files;
- 428 additions / 0 deletions.

## A3 / B3 guidance
A3 should re-read current `main`, verify ancestry/mergeability, and integrate only if the validated candidate remains semantically clean. B3 should preserve the distinction among recovery provenance, operational custody, technical fitness, claimant status, and explicit disposition/closure evidence.
