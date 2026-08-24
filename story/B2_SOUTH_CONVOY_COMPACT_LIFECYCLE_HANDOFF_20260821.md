# B2 South Convoy Compact lifecycle repair handoff — 2026-08-24

## Verdict

READY for A3 review/integration.

## Scope

Focused lifecycle repair only. This branch does not add a new South Convoy story arc and does not change the existing rescue-policy semantics.

The integrated `B2 South Convoy Compact` missions are dialogue/state-only: their terminal branches write persistent conditions but create no destination, cargo, passenger, NPC, waypoint, timer, or other gameplay objective. Six positive terminal paths nevertheless used `accept`, which could leave objective-less missions active after the conversation completed. The existing refusal route already used `decline`.

## Authority and exact commits

- repository: `Wiredshark/star`
- authoritative base/main at slice selection and completion recheck: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- isolated branch: `agent/b2-south-convoy-lifecycle-20260821-0526`
- production lifecycle repair: `864496d6e4116bb7dcf7df3a42a000b92aed0850`
- validator hardening: `1a4296a49dc9805007bdd875d8b1426312bfcb7e`
- exact fully validated production/validator/handoff candidate: `ced8a18e1aa11b29464473252283972da2165420`

## Production change

`data/human/b2 south convoy compact.txt`

- added the standard Endless Sky GPL header because changed-content style evaluates modified content files;
- changed the three positive Offer terminals, two Review settlement terminals, and the `Reeve Remembers` terminal from `accept` to `decline`;
- preserved all dialogue, source scope, route conditions, trust conditions, settlement conditions, and aftermath persistence exactly;
- retained the existing refusal `decline`, yielding seven clean dialogue-only terminal paths;
- added no objective-bearing mission directives.

## Validator change

`tools/story/validate_b2_south_convoy_compact.py`

The existing structural checks remain. Lifecycle assertions require:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing directives that would invalidate the dialogue-only lifecycle assumption.

## Exact validation evidence

On exact candidate `ced8a18e1aa11b29464473252283972da2165420`:

- `Fork simulation and story validation` run #318 / `32468092881`: SUCCESS;
  - changed fork content style: SUCCESS;
  - compile focused Python validation code: SUCCESS;
  - all focused story validators: SUCCESS;
  - A1 simulation contract tests: SUCCESS.
- `Fork save-load integration smoke` run #303 / `32468092867`: SUCCESS;
  - dependency installation: SUCCESS;
  - production configuration: SUCCESS;
  - production build: SUCCESS;
  - stock save-load smoke cases: SUCCESS.

The save-load workflow was still in progress when the original handoff was written. This completion pass recovered its terminal green result; no PASS is inferred from an in-progress state.

## State and canon boundaries

Unchanged:

- South, non-station source scope;
- Mira Dane / Tomas Reeve character continuity;
- three persistent Offer routes plus refusal;
- standing-rescue-compact and public-rescue-registry settlements;
- pledge route remains intentional Review fallthrough;
- no direct material/reputation/combat rewards;
- no new `world:*` ownership;
- no persistent condition names or values changed, so no save migration is required.

The rescue-policy semantics remain exactly the same. This repair changes only mission lifecycle termination.

## Process safety

At completion recheck, the private execution service reported four pre-existing service-owned processes. They were observed and preserved; none were killed, cancelled, or modified.

## A3 / B3 integration note

This is READY for A3 review/integration. Re-read current `main`, verify ancestry/mergeability, preserve all existing South Convoy state and canon semantics, and do not self-integrate from B2.

Preserve the lifecycle invariant:

> Dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.
