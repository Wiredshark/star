# B2 Heliarch Evidence Handoff — 2026-08-19

## Stage

B2 STORY CHARACTERS + DYNAMIC CONTENT

## Repository state

- Repository: `Wiredshark/star`
- Authoritative `main` observed at selection: `45841e29941fb0b720031a4c0cbc70e8bc32c890`
- B1 dependency branch: `agent/b1-heliarch-institutions-20260819-1016`
- Exact B1 dependency head: `05862cbfa893b03d16960cd0cb38bee988bd7043`
- B2 branch: `agent/b2-heliarch-evidence-handoff-20260819-1124`
- Production commit: `8f3be3502c5cacf241b76a78f222a0bb57bf6819`
- Focused validator commit: `3a8ee56c405d1e01d047624c9180be2b046bd1e8`
- Draft PR: #95, base `agent/b1-heliarch-institutions-20260819-1016`

## Implemented slice

`B2 Heliarch Evidence Handoff` turns B1's Heliarch evidence-custody and investigative-review history into a recurring present-day character conflict.

Two recurring Heliarchs are deliberately identified only through player-private shorthand:

- **Clerk** — normally encountered beside custody records, seals, and transfer logs.
- **Investigator** — normally encountered during active investigations where incomplete information must still be acted on.

The text explicitly states that neither shorthand is a name or office supplied by the Heliarchs.

The Offer centers on a seized navigation processor whose evidentiary chain crosses several Coalition jurisdictions while an active field team needs its information quickly. The player can choose:

1. custody-first — seal the original and wait for a verified diagnostic copy;
2. field-first — release the original temporarily under an emergency custody log;
3. paired handoff — retain the sealed original while immediately creating a witnessed working image whose transformations are logged;
4. refusal — persist refusal without entering the review chain.

The later Review remembers the chosen route and exposes the distinction between untouched evidence, derived analysis products, and interpretation. It resolves into exactly one of two persistent settlements:

- **portable provenance packet** — every copy/derived result carries source seal, extraction method, transformations, uncertainty, and responsible analyst;
- **independent reexamination** — field analysis may guide operations, but critical conclusions used for sanctions/tribunals are reproduced from the sealed original by a second team.

`Clerk Remembers` consumes either terminal state once.

## Files

- `data/coalition/b2 heliarch evidence handoff.txt`
- `tools/story/validate_b2_heliarch_evidence_handoff.py`
- `story/B2_HELIARCH_EVIDENCE_HANDOFF_20260819.md`

## State ownership and continuity invariants

- All persistent writes are under `B2 Heliarch Evidence Handoff:*`.
- No `world:*`, credits, reputation, cargo, outfit, ship, fleet, or combat state is mutated.
- Coalition license state is read-only gating.
- Clerk/Investigator are player-private shorthand, not canonical Heliarch offices or titles.
- B1's key institutional principle is preserved: custody records limit Heliarch authority by preserving an inspectable administrative trail.
- B1's investigative-review principle is preserved: observation and conclusion remain distinguishable, alternative explanations survive, and methods remain open to criticism/revision.
- Working analysis products are never silently promoted to untouched original evidence.

## Validation

Focused validator command:

```text
python3 tools/story/validate_b2_heliarch_evidence_handoff.py "data/coalition/b2 heliarch evidence handoff.txt"
```

Broader expected repository gates before READY:

```text
python3 tools/story/validate_story_repo.py
python3 tools/story/test_b2_character_packets.py
python3 utils/check_content_style.py
```

Repository-native simulation/story CI and production build/save-load smoke should also be green on the exact content/validator head or a descendant that changes only this handoff.

## A3 integration notes

Integration order is B1 Heliarch institutional history first, then this B2 branch. A3 should verify the exact B1 parent and preserve the private-shorthand and evidence-provenance invariants when reconciling later Heliarch content.

## Verdict

**PARTIAL** pending executable validation/CI on the exact B2 content + validator head. Do not integrate until the focused validator, repository story/style checks, and normal build/persistence gates are confirmed green.
