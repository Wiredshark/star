# B2 Drak Memorial Custody Compact — handoff

## Verdict

PARTIAL pending repository-native validation. This branch is isolated and must not be integrated by B2.

## Repository state

- Repository: `Wiredshark/star`
- Authoritative `main` observed at B2 start: `6f4e270c71ceffe7403252bcc404f0ec91651cc8`
- B1 parent branch: `agent/b1-drak-stewardship-institutions-20260819-0616`
- B1 parent SHA: `3b614ce0c8c518d68856acbd9c3120b383ff7797`
- B2 branch: `agent/b2-drak-memorial-custody-20260819-0627`
- Production commit: `62ffc6da46a26db13e22ac8e6c13d98e455bdf67`
- Focused-validator commit: `a667d810588315efdf2849374ebdd945333fb95a`

## Slice

The B1 Drak history establishes four recurring stewardship tensions: extinction prevention, memorial custody, intervention restraint, and remembering failed peacekeeping without converting those memories into triumphalist doctrine. B2 turns the memorial-custody tension into a persistent recurring-character arc.

The recurring presence is described only as **the Custodian**, explicitly as the player's private shorthand for a distinct Drak mental cadence. The content does not claim that this is a Drak name, title, office, bureaucracy, or self-description.

### Offer — Sayaiban

A preserved machine from an extinct species retains cultural records but also an autonomous defensive routine capable of repeating an old harm. The player can:

1. preserve the original intact under strict quarantine;
2. permanently disable the dangerous routine while documenting the intervention;
3. separate custody from operation by isolating the original and exposing a controlled reconstruction;
4. refuse to judge a culture/artifact the player barely understands.

The chosen route persists under the `B2 Drak Memorial Custody Compact:*` namespace.

### Review — Peresedersi

Generations later, the Custodian returns with a second-order problem: safe reconstructions have begun replacing the dangerous original in younger observers' understanding. The initial route changes the Review framing. The player resolves the policy into exactly one of two persistent settlements:

- `settlement bounded memorial`: preserve the original under operational containment, while every reconstruction must disclose omissions, translations, substitutions, and provenance;
- `settlement severed function archive`: public/research copies cannot execute the dangerous behavior, but the original function, historical consequences, and exact intervention remain permanently bound to the safe copy.

### Custodian Remembers — Fasitopfar

A one-shot aftermath reader consumes either settlement and shows the resulting stewardship principle in practice.

## Continuity and authority invariants

- B2 does not invent a formal Drak bureaucracy or title. "Custodian" is player shorthand only.
- B2 preserves B1's distinction between preservation and approval.
- Extinction memory does not imply that every surviving artifact should remain operational.
- Safety intervention must not be rewritten as if it were part of the vanished culture's original design.
- The player affects the form of the precedent but does not gain command authority over the Drak.
- Every persistent write is namespaced under `B2 Drak Memorial Custody Compact:*`.
- No `world:*`, credits, reputation, cargo, outfits, ships, fleets, or combat state is written by this slice.
- B1 Drak history should integrate before this B2 branch so the conceptual stewardship precedent is present first.

## Files

- `data/drak/b2 drak memorial custody compact.txt`
- `tools/story/validate_b2_drak_memorial_custody_compact.py`
- `story/B2_DRAK_MEMORIAL_CUSTODY_COMPACT_HANDOFF_20260819.md`

## Validation

Focused validator intended command:

```bash
python3 tools/story/validate_b2_drak_memorial_custody_compact.py "data/drak/b2 drak memorial custody compact.txt"
```

Repository-wide expected gates:

```bash
python3 tools/story/run_focused_validators.py
python3 tools/story/validate_story_repo.py
python3 tools/story/check_changed_content_style.py
```

Normal Endless Sky parser/build and stock save/load smoke should also pass before A3 integration.

At handoff creation time these repository-native gates have not yet returned green evidence for the exact B2 head, so the verdict remains PARTIAL. Do not promote this handoff to READY based only on the branch being mergeable.

## A3 / B3 notes

- Integrate B1 Drak stewardship history first, then review this B2 branch.
- Preserve the player-shorthand nature of `Custodian`; do not convert it into canonical Drak organizational terminology without separate canon evidence.
- B3 should check the new arc against existing `Drak Revelations` imagery and avoid contradictions about Drak grief, intervention, or stewardship.
- A3 should require green focused/story/style validation plus parser/build/save-load evidence before integration.
