# B2 Kor Efret Shrine Offering Boundaries — Handoff

## Verdict

PARTIAL pending exact-head repository-native validation.

## Authority

- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-kor-efret-shrine-offering-boundaries-20260824`
- Production commit: `b087fc01a82590b13ed86a2efc81307771c268be`
- Focused-validator commit: `4b37f23132e125eddbeec956687a912012929f8e`
- Current handoff head: this commit

B2 remains isolated and unmerged; A3 retains integration authority.

## Scope

This slice moves into ritual practice, family property, memory, and material reuse rather than another logistics, housing, employment, or global lifecycle repair.

It consumes two existing pieces of canon/read-only state:

- `Korath Far'en Lai Prayer: offered` — the established Kor Efret remembrance rite where personal objects are left at a shrine;
- `B2 Kor Efret Passage Continuity Compact: aftermath seen` — integrated family/resettlement continuity proving the player has already encountered Kor Efret family-record practice.

The new conflict concerns a deceased mechanic's calibrated cutter that a family once placed at a Far'en Lai shrine and now wants to use in a reopened workshop. The surviving record does not prove whether the old placement was permanent, temporary, reclaimable, or a transfer of ownership.

## Character / dynamic-content structure

### Offer

A recurring local Kor Efret whom the player privately calls the **Caretaker** disputes the cutter with a younger family relative.

Three substantive routes plus refusal:

1. **Intent first** — preserve explicit donor/family instruction when it exists; uncertainty does not become invented permanent surrender or automatic retrieval.
2. **Family reuse with history** — practical reuse is allowed when no permanent gift was recorded, while offering/removal context stays attached.
3. **Paired ritual/custody status** — ritual meaning and present physical custody remain separate linked facts.
4. **Refusal** — the player does not turn one family's ritual/property dispute into a general rule and does not arm the later Review.

Each substantive route schedules a delayed Review after 7–11 days.

### Review

A copied shrine catalog labels the cutter simply `missing`, while another family treats the earlier retrieval as proof that all shrine offerings are reclaimable. The Review exposes the failure mode: one true fact can become an unsupported general rule when donor intent, ritual meaning, family claim, and current custody are collapsed.

Two terminal settlements:

- **Portable offering history** — donor/family source, intended permanence if known, ritual meaning, current custodian, removal/return reason, unresolved claims, and closure travel together.
- **Dual closure** — ritual status and physical custody remain separate records, and neither silently overwrites the other.

### Aftermath

`Caretaker Remembers` is a one-shot reader demonstrating that the cutter can remain part of a truthful remembrance history even while physically serving the reopened workshop.

## Ownership / lifecycle

All persistent writes are under:

`B2 Kor Efret Shrine Offering Boundaries:*`

Read-only dependencies remain read-only. The slice does not write `world:*`, B1/A1/A2, prior-B2, credits, reputation, cargo, equipment, ships, fleets, or combat state.

All seven dialogue/state-only terminal paths use `decline`; there are zero objective-less `accept` terminals. Refusal does not write `introduced` and does not schedule the Review.

## Canon boundaries

- Far'en Lai remembrance is established canon; this slice does not define a universal theology, shrine office, or sacred-property code.
- `Caretaker` is player-private shorthand, not a canonical Korath title or office.
- Ritual meaning, donor/family intent, ownership history, current physical custody, practical need, and explicit closure are separate facts.
- A later practical need does not retroactively erase an offering.
- An old offering does not automatically erase every later family claim.
- One local family compromise must not become universal Kor Efret law.

## Files

- `data/korath/b2 kor efret shrine offering boundaries.txt`
- `tools/story/validate_b2_kor_efret_shrine_offering_boundaries.py`
- `story/B2_KOR_EFRET_SHRINE_OFFERING_BOUNDARIES_HANDOFF_20260824.md`

## Validation plan

Required before READY:

- focused validator for this slice;
- all focused story validators / repository story contracts;
- A1 simulation and state-ownership regressions;
- changed-content style;
- production configure/build;
- stock save-load integration smoke;
- exact branch/base diff and final status recheck.

## A3 / B3 notes

A3 should re-read current authoritative `main`, active B2/A2 work, ancestry, mergeability, and exact workflow state immediately before integration. Do not self-integrate from B2. Preserve the local-family scope and the distinction among ritual history, intent, ownership claim, custody, practical use, and closure.
