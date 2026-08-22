# B2 Successor Interface Provenance Compact handoff

## Stage

B2 — Story Characters + Dynamic Content

## Repository state

- Repository: `Wiredshark/star`
- Authoritative integration head rechecked during lifecycle recovery: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Required B1 parent branch: `agent/b1-successor-institutions-20260819-1626`
- Exact B1 parent SHA: `4c8cf4ea18370c7da5a04a919f6e6be91f086db9`
- B2 branch: `agent/b2-successor-interface-provenance-20260820-1725`
- Original production commit: `06d23d6b10e78427cdf88725132c23b2001d38f3`
- Original focused-validator commit: `f1e7a459c996ae370b7302deeffaf4effb0989b2`
- Prior PARTIAL handoff head: `e5b6b3f18c58221fde2a724a43018886bd94bb64`
- Dialogue-lifecycle production repair: `bd891fe311cd4e54dfcaf1796bef2f8edb5da630`
- Lifecycle-validator hardening: `78fd6dfb6f831f7722656c30fac6623139a307ca`

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

## Dialogue lifecycle repair

The three missions above are dialogue/state-only: they persist conditions and schedule the delayed Review, but they create no destination, NPC, cargo, passenger, waypoint, deadline, timer, or other gameplay objective.

The historical production slice nevertheless used terminal `accept` on six positive paths: three Offer routes, two Review settlements, and `Fitter Remembers`. Because `accept` moves an offered mission into the accepted mission list, those objective-less paths could remain as active missions after their conversations ended.

Commit `bd891fe311cd4e54dfcaf1796bef2f8edb5da630` changes exactly those six terminals from `accept` to `decline`. The refusal route already used `decline`, so all seven dialogue/state-only terminal paths now persist the same existing state and close cleanly.

No dialogue, route, trust state, settlement, condition name/value, delayed-event timing, source scope, B1 dependency, material state, or canon semantics changed. No save-state migration is required.

The focused validator was hardened in `78fd6dfb6f831f7722656c30fac6623139a307ca` to require:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no tab-indented gameplay-objective directive that would invalidate the state-only lifecycle assumption.

The objective-directive check is anchored to actual mission directives rather than prose, so ordinary dialogue words cannot create false positives.

## Files

- `data/successors/b2 successor interface provenance compact.txt`
- `tools/story/validate_b2_successor_interface_provenance_compact.py`
- `story/B2_SUCCESSOR_INTERFACE_PROVENANCE_COMPACT_HANDOFF_20260820.md`

## Persistence and authority

- All new writes remain namespaced under `B2 Successor Interface Provenance Compact:*`.
- The content does not mutate B1 history state, `world:*`, credits, reputation, cargo, outfits, ships, fleets, or combat state.
- The compact does not imply a centralized Successor engineering office or universal law.
- The core continuity invariant is that **matching geometry is not proof of matching operating context**. A reusable configuration must preserve the evidence that established what it was qualified to do.
- Qualification evidence remains distinct from physical shape, local installation observations, and later interpretation.

## Validation

Focused validator command:

```text
python3 tools/story/validate_b2_successor_interface_provenance_compact.py "data/successors/b2 successor interface provenance compact.txt"
```

Broader repository gates required before READY:

```text
python3 tools/story/validate_story_repo.py
python3 utils/check_content_style.py
```

Repository-native `Fork simulation and story validation` and `Fork save-load integration smoke` must both be terminal green on the exact production/validator/handoff candidate before A3 integration.

Current verdict remains **PARTIAL** until those exact-head repository-native gates are observed terminal green after the lifecycle repair. Earlier pre-repair success cannot be used as acceptance evidence for the lifecycle change.

## Concurrency / process safety

At recovery time:

- current open B2 work was inspected; no competing Successor Interface lifecycle repair was present;
- the existing stale PR was advanced rather than creating a duplicate branch;
- the private execution service reported four pre-existing service-owned processes; none were killed, cancelled, or modified;
- no unrelated branch, worktree, or dirty host workspace was reset, cleaned, rebased, or force-updated.

## A3 / B3 integration notes

1. Accept/integrate or otherwise reconcile the B1 Successor institutional-history parent first if it is not already authoritative.
2. Re-read current `main` immediately before integration because this branch descends from the older B1 dependency rather than current main.
3. Preserve the distinction among geometry, operating medium, pressure, electrical behavior, control convention, temperature, material limits, repair history, local installation observations, and actual qualification status.
4. Do not allow copied registry summaries to turn an old approval into permanent proof of compatibility.
5. Preserve the dialogue lifecycle invariant: state-only B2 dialogue missions close with `decline`; reserve `accept` for mission paths that actually create gameplay objectives.

## Verdict

**PARTIAL** — lifecycle production repair and validator hardening are committed; exact-head repository-native validation is required before READY.
