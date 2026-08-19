# B2 Republic Tracing Compact handoff — 2026-08-18

## Verdict

**PARTIAL — isolated production candidate. Do not integrate until focused validator plus normal Endless Sky content/parser/runtime/save-load gates pass.**

## Authority and ancestry

- Repository: `Wiredshark/star`
- Authoritative `main` recovered during this run: `b21d71ce67fa3473bda1e075714d9c486fef734d`
- B1 parent branch: `agent/b1-republic-displacement-institutions-20260818-2316`
- B1 parent commit: `1485c138befd76f9d3481634c235ccf9937a132d`
- B2 branch: `agent/b2-republic-tracing-compact-20260818-2326`
- Production commit: `6dc3c4b97dc07806837c083dfc4cf77c1faa7bf9`
- Validator commit: `18779ff13f1b4e1236bc2efff50c72c5784b4622`

## Scope

Consumes two already-defined layers without taking ownership of either:

1. B1 Republic displacement institutional history:
   - evacuation manifests and family tracing;
   - return/resettlement ledgers that distinguish route reopening from individual recovery.
2. A1 authoritative world state:
   - `world: republic displacement pressure`;
   - `world: republic resettlement surge`.

Adds two named characters:

- **Anika Saye** — Republic reunification caseworker.
- **Corin Vell** — host-world records registrar.

The story dispute is specifically about **portable family tracing, records custody, consent, and the distinction between tracing status and residence/return choice**. This intentionally avoids duplicating the existing `B2 Republic Displacement Compact`, which focuses on protected housing/passage and administrative handoff of capacity.

## Production behavior

### Offer — `Names That Did Not Return`

Offers during an A1 resettlement surge while displacement pressure remains at least 2.

Player routes:

1. portable tracing — family-tracing cases remain open across moves;
2. accountable registry — every transfer records address, consent, and records custodian;
3. dual track — tracing remains portable while return/local settlement remains a separate voluntary decision;
4. refusal.

B2 writes only `B2 Republic Tracing Compact:*` memory.

### Review — `The File That Followed`

Offers after the A1 backlog has eased below 2 and the resettlement surge is no longer active.

Resolves to one of two terminal settlements:

- **portable family file** — tracing follows the resident across moves and every transfer names the next records custodian;
- **consent ledger** — address, custodian, contact-sharing consent, and tracing status are recorded independently.

### Later reader — `Saye Remembers`

Consumes either settlement once and records one-shot aftermath state.

## Ownership and persistence invariants

- A1 remains sole writer of every `world:*` condition used here.
- B2 reads `world: republic displacement pressure` and `world: republic resettlement surge` only.
- B2 writes only its own ordinary persistent mission/global conditions.
- No direct credits, reputation, combat-rating, cargo, or outfit mutation is intended.
- Tracing status is distinct from residence, return, housing, employment, and reunification outcome.
- Local settlement must not silently close a family-tracing case.

## Files

- `data/human/b2 republic tracing compact.txt`
- `tools/story/validate_b2_republic_tracing_compact.py`
- `story/B2_REPUBLIC_TRACING_COMPACT_HANDOFF_20260818.md`

## Validation evidence

Performed:

- recovered current authoritative `main` and recent open B1/B2/A2 work;
- verified no existing `Anika Saye` or `Corin Vell` content before authoring;
- inspected exact current A1 displacement/resettlement implementation;
- inspected exact B1 displacement-history parent content;
- inspected the existing B2 Republic Displacement Compact to keep this slice non-overlapping;
- fetched the committed production file and focused validator back from GitHub at exact validator head `18779ff13f1b4e1236bc2efff50c72c5784b4622`;
- attempted to execute the validator against raw GitHub content in an isolated local scratch directory, but that execution environment could not resolve `raw.githubusercontent.com`, so no validator PASS is claimed.

Not claimed:

- focused-validator execution success;
- `utils/check_content_style.py` success;
- normal Endless Sky content parser/build success;
- game runtime/smoke-load success;
- save/load roundtrip success;
- CI success.

## Required acceptance before READY

Run from an exact checkout of this branch head:

```bash
python3 tools/story/validate_b2_republic_tracing_compact.py "data/human/b2 republic tracing compact.txt"
python3 utils/check_content_style.py
```

Then run the normal Endless Sky parser/build/content validation and exercise:

1. Offer appears only while resettlement surge is active and displacement pressure is `>= 2`;
2. all three substantive routes and refusal persist across save/load;
3. Review remains unavailable while pressure is elevated or surge remains active;
4. Review becomes available after pressure falls below 2 and surge ends;
5. exactly one terminal settlement becomes authoritative;
6. `Saye Remembers` consumes either settlement once;
7. no B2 action changes A1 world-state conditions.

## A3/B3 integration notes

- Integrate only after the B1 displacement-institutions parent is accepted or otherwise preserve the intended history dependency.
- Keep this slice separate from the existing B2 Republic Displacement Compact: that branch governs protected placement/capacity handoffs; this branch governs family-tracing continuity and records consent/custody.
- Preserve the A1 hysteresis invariant: the resettlement surge is a recovery response after border pressure recedes, not evidence that all displaced residents have already recovered.
