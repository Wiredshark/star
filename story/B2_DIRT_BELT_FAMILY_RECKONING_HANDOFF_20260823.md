# B2 Dirt Belt Family Reckoning Handoff — 2026-08-23

LOOP_ID: B2
RUN_TYPE: CONTENT
PRIMARY_DOMAIN: relationships and personal history
SECONDARY_DOMAINS: family privacy; memory/provenance; ownership of personal history
RECENT_DOMAIN_WINDOW: Coalition rescue/medical handoff; Unfettered lineage memory; Free Worlds volunteer command
DIVERSITY_STATUS: PASS
CONCENTRATION_JUSTIFICATION: N/A
NEGLECTED_AREA_ADVANCED: original STORY_CANON character continuity for Imani Velez and Tomas Rhyne
CROSS_SYSTEM_CONNECTION: durable STORY_CANON character records -> production mission/conversation persistence with delayed consequence reader

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-dirt-belt-family-reckoning-20260823`
- Production commit: `88b7d4a32b386b6f608879a01b86115a91fb3c33`
- Focused-validator commit: `12b0fce6fad9ff947eaf58454f8b16d7d20f6732`
- Integration authority: A3; B2 must not self-integrate.

## Character/dynamic-content behavior

This slice deliberately returns to the original Story Round 1 characters without repeating their freight crisis. Imani Velez and Tomas Rhyne are joined by Tomas's adult daughter, Lena Rhyne, in a conflict over whether an old family account should preserve Tomas's concealed risky decision and Imani's role in quietly containing the consequences.

The Offer supports three credible approaches plus refusal:

1. full disclosure with attribution;
2. Tomas's living privacy boundary, without permission to invent a false public history;
3. preservation/publication separation through a complete sealed record and negotiated release boundaries;
4. refusal to become the authority over the family's internal history.

Each substantive route persists distinct relationship state and schedules a 7–11 day Review. The Review resolves into exactly two persistent outcomes:

- `settlement layered family record` — verified events, attributed memories, disputed interpretations, and deliberate privacy boundaries remain separate;
- `settlement consent and release` — source material can be preserved without treating possession as publication permission.

`Lena Remembers` is a one-shot later reader demonstrating the settlement in ordinary family use.

All seven dialogue/state-only terminal paths use `decline`; the slice creates no objective-less accepted missions.

## Dependencies and ownership

- STORY_CANON input: `story/BUILDER_HANDOFF.md` definitions of Imani Velez and Tomas Rhyne, including Tomas's unofficial high-risk delivery and Imani's concealed cooperative support.
- B1/A2 state: inspected for overlap; this slice does not write or require a B1/A2 state key.
- A1/world state: no duplicate world-state shadow is created and no `world:*` key is written.
- B2 writes only `B2 Dirt Belt Family Reckoning:*` conditions.
- No credits, reputation, cargo, equipment, ship, fleet, or combat mutation.

## Files changed

- `data/human/b2 dirt belt family reckoning.txt`
- `tools/story/validate_b2_dirt_belt_family_reckoning.py`
- `story/B2_DIRT_BELT_FAMILY_RECKONING_HANDOFF_20260823.md`

## Validation contract

Focused validator:

`python3 tools/story/validate_b2_dirt_belt_family_reckoning.py`

Repository acceptance should also run:

- `python3 tools/story/validate_story_repo.py`
- changed-content style validation
- repository-wide story/state-ownership contracts
- normal production configure/build
- stock save/load smoke

Current verdict: **PARTIAL** pending repository-native CI on the exact candidate head after PR creation.

## Persistence/canon assumptions

- Lena Rhyne is a new B2 character and Tomas's adult daughter. This is a deliberate additive STORY_CANON relationship, not an inference about stock Endless Sky canon.
- Imani and Tomas retain the personalities and secrets already documented in the durable story repository.
- The production text never states Tomas's hidden motive as fact; his remembered explanation remains attributed interpretation.
- Preserving an account does not grant publication rights, and a privacy boundary does not authorize false history.
- Repetition of a family story is not independent corroboration.

## DIVERSITY_CHECK

- Primary domain: personal relationships / family memory / privacy.
- Recent same-lane domains considered: rescue/medical handoff, cultural lineage memory, volunteer command authority.
- Adjacent-lane work considered: A1 world-state systems and A2 dialogue/history consumers were inspected; no duplicate state writer is introduced.
- Why this is not another iteration of the same subsystem: the central pressure is trust among three named people over truthful memory and privacy, not freight, resource allocation, emergency logistics, or command procedure.
- Underrepresented area advanced: original Story Round 1 named-character continuity and family relationships.
- New cross-system connection: durable story-canon character secrets become production persistent dialogue with delayed relationship consequences.
- Persistent/player-visible capability added: route-specific trust, two durable family-record settlements, and a later memory reader.
- Concentration exception: N/A.

## A3/B3 integration notes

A3 should re-read current authoritative `main` before integration and confirm no newer Imani/Tomas implementation has landed. B3 should preserve the distinction among verified event, attributed memory, interpretation, privacy boundary, preservation, and publication consent. Do not rewrite the result as a universal Republic archival policy; it is one family's negotiated practice.
