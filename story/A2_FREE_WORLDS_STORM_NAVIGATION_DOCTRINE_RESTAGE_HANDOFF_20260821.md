# A2 Free Worlds Storm Navigation Doctrine Restage Handoff

## Verdict
PARTIAL pending exact-head repository-native validation on the current-main restage.

## Authority and ancestry
- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Restage branch: `agent/a2-free-worlds-storm-navigation-doctrine-restage-20260821-0605`.
- Historical validated source candidate: `34e49f06ac0f6159ce50a6ef2ccc876dd6b95671` from PR #135.
- Historical candidate workflows: simulation/story `32323350820` SUCCESS; save-load `32323350961` SUCCESS.
- PR #135 is no longer mergeable against current `main`, so this restage preserves validated semantics on fresh authoritative ancestry rather than rebasing or force-updating the old branch.

## RPG / dynamic narrative loop
During authoritative A1 geomagnetic storm activity with navigation strain `>= 3`, Rhea Solano asks the player to choose verified corridors, independent cross-checks, local autonomy, or explicit refusal.

Positive routes persist only `A2 Free Worlds Storm Navigation Doctrine:*` state and arm a recovery boundary. The boundary does not arm recurrence until the original A1 disturbance is inactive and authoritative navigation strain is `<= 1`. A later storm recurrence with strain `>= 3` produces doctrine-specific consequences, split into moderate and severe (`>= 5`) outcomes for six positive variants. Refusal remains respected and does not arm the later test.

## Invariants
- A1 remains sole writer of Free Worlds geomagnetic storm, cooldown, advisory, and navigation-strain state.
- No upstream A1 or prior A2 state is mutated.
- Repetition is not treated as independent corroboration.
- Historical doctrine success is not permanent authority.
- No centralized Free Worlds navigation bureaucracy is created.
- State-only dialogue terminals use `decline`, not `accept`, so no objective-less mission remains accepted.
- Save compatibility is additive through namespaced condition defaults only.

## Files
- `data/human/a2 free worlds storm navigation doctrine.txt`
- `tools/story/validate_a2_free_worlds_storm_navigation_doctrine.py`
- `story/A2_FREE_WORLDS_STORM_NAVIGATION_DOCTRINE_RESTAGE_HANDOFF_20260821.md`

## Validation required on this restage
Run and require terminal green on the exact final restage head for:
1. Fork simulation and story validation, including focused validator discovery, A1 ownership contracts, and changed-content style.
2. Fork save-load integration smoke, including production configure/build and stock persistence cases.

The focused validator additionally enforces the current dialogue-lifecycle invariant: no state-only `accept` endpoints, four briefing terminal declines, and recurrence decline.

## A3 integration instructions
Review only the exact current-main restage head after both workflows are terminal green. Preserve A1 ownership of storm/navigation state and the recovery-before-recurrence boundary. Do not self-integrate from A2. Historical PR #135 may remain as provenance but should not be integrated directly because GitHub reports it non-mergeable against current `main`.
