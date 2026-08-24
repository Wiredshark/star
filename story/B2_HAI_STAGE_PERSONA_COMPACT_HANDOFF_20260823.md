# B2 Hai Stage Persona Compact Handoff — 2026-08-23

## Verdict
PARTIAL pending repository-native simulation/story/style and production build/save-load workflows on the exact candidate.

## Authority
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-hai-stage-persona-compact-20260823`
- Production commit: `ddb6ca3e2fa70ab926175ec3b909c5ef0e1473f4`
- Focused validator commit: `0e595ef95974666519f175f75f2e5b34ec3d062c`
- Handoff candidate: recorded by the commit containing this file.

## Character / dynamic-content slice
Adds Hai singer Kessa Riin and human songwriter Mara Dey. Their conflict is not whether stage personas are false, but how creative performance, authorship, publicity consent, revision, and private biographical claims remain distinguishable when promotional profiles are copied across labels, venues, languages, and cultures.

Initial routes:
- bounded performance with campaign/expiry context;
- artist revision authority with attributable version history;
- layered stage persona / creative credit / publicity consent / private-biography records;
- refusal.

The three substantive routes schedule a Review after 7–11 days. Review resolves into either:
- portable persona packet; or
- persona firewall.

`Kessa Remembers` is the one-shot aftermath reader.

## Canon / architecture dependencies
- Uses established Hai popular-entertainment canon from `data/hai/hai culture conversations.txt`, including long-lived theatrical reinterpretation and label-driven musical celebrity culture.
- Uses the integrated human-settlement-in-Hai-space premise from `data/hai/hai institutional history conversations.txt` as background canon, without inventing a centralized Hai entertainment regulator.
- Requires `language: Hai` so the player can follow the full dispute.
- Does not modify B1/A2/A1 state.

## Ownership / persistence
- All writes are `B2 Hai Stage Persona Compact:*`.
- No `world:*`, credits, reputation, cargo, outfits, ships, fleets, combat, or upstream story-state mutation.
- All 7 state-only dialogue terminal paths use `decline`.
- Refusal does not arm the later Review.
- No save-state migration is required because this is additive state.

## Continuity assumptions
- A stage persona can be genuine creative work without being a literal private biography.
- Promotional repetition is not independent corroboration.
- Creative credit, artist revision, publicity consent, campaign expiry, and private claims remain separate facts.
- A profile copied outside its original campaign must not silently turn performance into permanent personal truth.
- One label/artist compromise must not become universal Hai law or centralized cultural authority.

## Validation required before READY
1. Focused validator: `python3 tools/story/validate_b2_hai_stage_persona_compact.py`.
2. Repository-focused story validation / validator compilation.
3. A1 simulation/state-ownership contracts.
4. Changed-content style.
5. Production configure/build.
6. Stock save-load integration smoke.
7. Exact final diff/status and current-main ancestry recheck.

## A3 / B3 notes
A3 should re-read current authoritative `main` immediately before integration. Preserve the state-only `decline` lifecycle, B2-only persistence namespace, and the boundary between performance/publicity and private biographical claims. B3 may consume either settlement as a later entertainment-industry or cross-cultural consequence, but should treat copied publicity profiles as one source lineage rather than independent evidence.
