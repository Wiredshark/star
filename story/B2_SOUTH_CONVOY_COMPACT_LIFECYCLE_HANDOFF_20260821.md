# B2 South Convoy Compact lifecycle repair handoff — 2026-08-21

## Verdict

PARTIAL pending repository-native simulation/story/style and production build/save-load validation on the exact candidate head.

## Scope

Focused lifecycle repair only. This branch does not add a new South Convoy story arc and does not change the existing rescue-policy semantics.

The integrated `B2 South Convoy Compact` missions are dialogue/state-only: their terminal branches write persistent conditions but create no destination, cargo, passenger, NPC, waypoint, timer, or other gameplay objective. Six positive terminal paths nevertheless used `accept`, which could leave objective-less missions active after the conversation completed. The existing refusal route already used `decline`.

## Authoritative base

- repository: `Wiredshark/star`
- authoritative base/main at slice selection: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- isolated branch: `agent/b2-south-convoy-lifecycle-20260821-0526`

## Commits

- production lifecycle repair: `864496d6e4116bb7dcf7df3a42a000b92aed0850`
- validator hardening: `1a4296a49dc9805007bdd875d8b1426312bfcb7e`

## Production change

`data/human/b2 south convoy compact.txt`

- added the standard Endless Sky GPL header because changed-content style evaluates modified content files;
- changed the three positive Offer terminals, two Review settlement terminals, and the `Reeve Remembers` terminal from `accept` to `decline`;
- preserved all dialogue, source scope, route conditions, trust conditions, settlement conditions, and aftermath persistence exactly;
- retained the existing refusal `decline`, yielding seven clean dialogue-only terminal paths.

No objective-bearing mission directives were added.

## Validator change

`tools/story/validate_b2_south_convoy_compact.py`

The existing structural checks remain. New lifecycle assertions require:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing directives that would invalidate the dialogue-only lifecycle assumption.

## State and canon boundaries

Unchanged:

- South, non-station source scope;
- Mira Dane / Tomas Reeve character continuity;
- three persistent Offer routes plus refusal;
- standing-rescue-compact and public-rescue-registry settlements;
- pledge route remains intentional Review fallthrough;
- no direct material/reputation/combat rewards;
- no new world-state ownership.

The rescue-policy semantics remain exactly the same. This repair changes only mission lifecycle termination.

## Process safety

The private execution service reported six pre-existing service-owned orphan processes. They were observed and preserved; none were killed, cancelled, or modified.

## Required validation before READY

Run on the exact branch head:

1. focused South Convoy validator;
2. complete focused story validator suite;
3. A1/state-ownership regression contracts;
4. changed-content style;
5. production Endless Sky configure/build;
6. stock save/load smoke.

## A3 / B3 integration note

If all exact-head gates are green, this is a low-risk focused repair suitable for A3 integration. Preserve the lifecycle invariant:

> Dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.
