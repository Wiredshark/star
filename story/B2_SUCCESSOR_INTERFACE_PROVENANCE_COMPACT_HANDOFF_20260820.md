# B2 Successor Interface Provenance Compact handoff

## Stage

B2 — Story Characters + Dynamic Content

## Repository state

- Repository: `Wiredshark/star`
- Required B1 parent branch: `agent/b1-successor-institutions-20260819-1626`
- Exact B1 parent SHA: `4c8cf4ea18370c7da5a04a919f6e6be91f086db9`
- B2 branch: `agent/b2-successor-interface-provenance-20260820-1725`
- Production commit: `06d23d6b10e78427cdf88725132c23b2001d38f3`
- Focused-validator commit: `f1e7a459c996ae370b7302deeffaf4effb0989b2`

## Slice

This B2 slice consumes B1's Successor Morphic Interface Registry and Transaction and Dispute Ledger institutional history. It turns the registry's engineering-memory concept into a persistent character conflict about what a reusable morphic configuration actually proves.

The recurring characters are represented through player-private shorthand:

- **Archivist** — prioritizes preservation of the test conditions, limits, repairs, and provenance that made a configuration safe.
- **Fitter** — prioritizes rapid practical reuse of known configurations while recording what was actually measured or changed in the new installation.

These labels are not canonical Successor titles, House offices, or evidence of a centralized engineering authority.

## Player-facing behavior

`B2 Successor Interface Provenance Compact: Offer` provides three substantive routes plus refusal:

1. **Provenance-first** — reuse requires the original qualification conditions and limits to travel with the configuration.
2. **Field-first** — crews may begin from a known successful shape but must record the new operating conditions, deviations, and assumptions.
3. **Paired records** — keep the immutable tested-interface record separate from the installation-specific qualification record.
4. **Refusal** — no general procedure is adopted and no later Review is scheduled.

Each substantive route schedules a delayed Review after 7–11 days.

`B2 Successor Interface Provenance Compact: Review` exposes the downstream-copy failure mode: geometry can survive while working fluid, pressure cycle, electrical behavior, control convention, temperature, repairs, and qualification limits disappear. The Review resolves into exactly two persistent outcomes:

- **portable qualification packet** — geometry and full qualification context travel together;
- **expiry and revalidation** — prior successful configurations remain reusable starting points, but assumptions expire when operating context materially changes.

`Fitter Remembers` is a one-shot aftermath reader for either terminal outcome.

## Files

- `data/successors/b2 successor interface provenance compact.txt`
- `tools/story/validate_b2_successor_interface_provenance_compact.py`
- `story/B2_SUCCESSOR_INTERFACE_PROVENANCE_COMPACT_HANDOFF_20260820.md`

## Persistence and authority

- All new writes are namespaced under `B2 Successor Interface Provenance Compact:*`.
- The content does not mutate B1 history state, `world:*`, credits, reputation, cargo, outfits, ships, fleets, or combat state.
- The compact does not imply a centralized Successor engineering office or universal law.
- The core continuity invariant is that **matching geometry is not proof of matching operating context**. A reusable configuration must preserve the evidence that established what it was qualified to do.

## Validation

Focused validator command:

```text
python3 tools/story/validate_b2_successor_interface_provenance_compact.py "data/successors/b2 successor interface provenance compact.txt"
```

Broader repository gates expected before READY:

```text
python3 tools/story/validate_story_repo.py
python3 utils/check_content_style.py
```

Repository-native fork simulation/story validation and production build/save-load smoke should be terminal green on the exact candidate head before A3 integration.

At handoff creation time these asynchronous repository-native gates have not yet been observed on the exact candidate head, so the current verdict is **PARTIAL** rather than READY.

## A3 / B3 integration notes

1. Accept/integrate the B1 Successor institutional-history parent first if it is not already authoritative.
2. Re-read current `main` before integrating this B2 branch because the B1 parent is older than current main and may need dependency-order reconciliation.
3. Preserve the distinction among geometry, operating medium, pressure, electrical behavior, control convention, temperature, material limits, repair history, local installation observations, and actual qualification status.
4. Do not allow copied registry summaries to turn an old approval into permanent proof of compatibility.

## Verdict

**PARTIAL** — isolated production content and focused validator are committed; exact-head repository-native validation is still required before READY.
