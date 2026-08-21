# B2 Avgi Allocation Compact lifecycle repair handoff — 2026-08-21

## Verdict

PARTIAL pending repository-native simulation/story/style and production build/save-load gates on the exact remote head.

## Authority and branch

- Repository: `Wiredshark/star`
- Authoritative base recovered for this slice: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-avgi-allocation-lifecycle-20260821-1123`
- Production lifecycle repair commit: `ab5829278f7816ffc249afb3840d42f959676547`
- Focused-validator hardening commit: `11618b826383a0b031643707677970ff6c342466`
- Current handoff head: this commit

B2 remains isolated and unmerged. A3 retains integration authority.

## Problem repaired

`B2 Avgi Allocation Compact` is a dialogue/state-only three-mission slice. Its three positive Offer routes, two Review settlements, and `Verdigris Remembers` aftermath path persisted conditions and then used `accept` despite creating no destination, cargo, NPC, waypoint, timer, or other gameplay objective. Those objective-less accepted missions can linger in the active mission list after their conversations end.

## Repair

- Converted all six positive state-only terminal `accept` commands to `decline`.
- Preserved the existing refusal `decline`, so all seven terminal paths now close cleanly.
- Preserved every dialogue line, route condition, trust condition, settlement condition, character beat, Consonance scope, Avgi written-language gate, and `avgi: lost in twilight` gate.
- Hardened `tools/story/validate_b2_avgi_allocation_compact.py` to reject any terminal `accept`, require exactly seven `decline` terminals, and reject gameplay-objective directives that would invalidate the state-only lifecycle assumption.
- Preserved existing validator checks for routes, settlements, Review fallthrough, one-shot aftermath, B2-only write authority, upstream Avgi/world state read-only ownership, material/reputation mutation guards, and local `goto`/`label` integrity.

## Validation evidence already executed in an isolated `Wiredshark/star` clone

The clone was pinned to the same authoritative base and contained byte-equivalent production and validator changes before publication.

- `python3 tools/story/validate_b2_avgi_allocation_compact.py` — PASS.
- `python3 tools/story/validate_story_repo.py` — PASS.
- `python3 tools/story/test_b2_character_packets.py` — PASS.
- `git diff --check` — PASS.
- `python3 utils/check_content_style.py "data/avgi/b2 avgi allocation compact.txt"` — could not start because the private host Python environment lacks third-party package `regex` (`ModuleNotFoundError`). No host-side style PASS is claimed.

Repository-native CI remains the acceptance authority for style/build/save-load.

## Persistence / canon / ownership

- All existing persistent writes remain under `B2 Avgi Allocation Compact:*`.
- B2 continues to treat `avgi:*` and `world:*` state as read-only.
- Verdigris and Ochre characterization and the Consonance/Twilight Guard authority split are unchanged.
- No credits, reputation, cargo, outfits, ships, fleets, or combat state are changed.

## A3 / B3 integration notes

- Integrate only after repository-native simulation/story/style and production build/save-load gates are terminal green on the exact candidate head.
- Preserve the lifecycle invariant: dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.
- No B1/A1 dependency ordering change is introduced by this repair; this is a lifecycle-only correction to already integrated B2 content.
