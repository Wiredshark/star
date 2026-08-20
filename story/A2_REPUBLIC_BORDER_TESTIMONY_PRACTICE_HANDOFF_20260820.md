# A2 Republic Border Testimony Practice handoff - 2026-08-20

## Verdict

**PARTIAL pending exact-head restaged repository validation.**

The production slice has been semantically repaired and restaged directly from current authoritative `main`; do not promote to READY until both exact-head workflows below are terminal green.

## Authority

- Repository: `Wiredshark/star`
- Restage base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-republic-border-testimony-practice-restage-20260820`
- Supersedes stale-base PR #194 branch ancestry from `27b5ddc9cbb084c4751ef52d185f13f62e825c27`.

## Production RPG/dialogue loop

After the integrated B2 Republic Border Testimony Compact aftermath and while authoritative A1 border pressure is recovered to `<= 2`, Talia Rook asks what evidence discipline should survive into the next alert.

The production conversation contains five valid responses:

1. `[Evidence: Portable provenance packet]` source-lineage practice, available only when the corresponding B2 settlement exists.
2. `[Verran trusts your evidence judgment]` independent-corroboration practice, available only from durable B2 named-character memory.
3. `[Settlement: Expiry and renewal]` closure/renewal practice, available only when that B2 settlement exists.
4. Local/context-only reuse, always valid.
5. Explicit refusal, always valid and does not arm recurrence.

A later authoritative A1 border-pressure recurrence at `>= 4` reads the persisted positive A2 choice and produces a route-specific one-shot consequence.

## Repairs in this restage

- restored the standard GPL content header;
- added `offer precedence 8` so the production A2 conversation outranks ambient institutional-history offers;
- changed dialogue-only outcomes from `accept` to state-write + `decline`, preventing a completed conversation from leaving a bogus active mission;
- added three player-visible special-response labels tied to real B2 persistent state;
- added three conditional response gates using existing conversation `to display` semantics rather than a dialogue-only shadow database;
- hardened the focused validator for precedence, labels, state-dependent choices, ownership, and dialogue-only lifecycle behavior;
- added headless production-game route tests for all four positive choices plus refusal, persistence across save/reload, later A1 recurrence, one-shot suppression, and no lingering active mission;
- added `tests/integration/a2_runtime_acceptance.txt` and taught the production save-load workflow to execute every listed A2 runtime scenario after the stock persistence regressions.

## Ownership / invariants

- A1 remains sole writer of `world: republic border pressure`.
- `B2 Republic Border Testimony Compact:*` is read-only production input.
- All new production writes remain `A2 Republic Border Testimony Practice:*`.
- Repeated copies never manufacture independent corroboration.
- Resolved warnings can remain searchable without remaining active accusations.
- Historical source presence is not guilt or motive.
- Local reuse does not create Republic-wide authority.
- Refusal remains refusal and does not arm the recurrence reader.

## Acceptance mapping

The slice now directly targets the A-loop dialogue-system production gate:

- named production NPC: Talia Rook, with durable Jace Verran trust memory;
- at least three materially different approaches: lineage, independence, closure, plus local-only and refusal;
- persistent-state-dependent responses: B2 provenance settlement, B2 Verran trust, B2 expiry/renewal settlement;
- player-visible requirement metadata: bracketed evidence/relationship/settlement labels;
- persistent consequence: A2 route condition;
- later reader: `A2 Republic Border Testimony Practice: Recurrence`;
- refusal path: durable and recurrence-suppressing;
- stock conversation/save regressions: retained in the same production workflow;
- actual-game runtime: headless `EndlessSky --test` drives the production spaceport conversation through keyboard input and save/reload.

No UI rendering code changed, so no new visual-layout screenshot gate is introduced by this slice.

## Files

- `data/human/a2 republic border testimony practice.txt`
- `tools/story/validate_a2_republic_border_testimony_practice.py`
- `tests/integration/config/plugins/integration-tests/data/tests/tests_a2_republic_border_testimony_practice.txt`
- `tests/integration/a2_runtime_acceptance.txt`
- `.github/workflows/fork-save-load-smoke.yml`
- `story/A2_REPUBLIC_BORDER_TESTIMONY_PRACTICE_HANDOFF_20260820.md`

## Required final gate

Before A3 integration, observe both workflows on the exact final restage head:

1. `Fork simulation and story validation` = SUCCESS.
2. `Fork save-load integration smoke` = SUCCESS, including all five A2 runtime acceptance cases from the manifest.

Then update this handoff to explicit READY, reread authoritative `main`, recheck ancestry/mergeability, and integrate only with an expected-head guard.
