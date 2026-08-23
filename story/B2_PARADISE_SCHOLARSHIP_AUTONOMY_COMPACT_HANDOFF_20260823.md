# B2 Paradise Scholarship Autonomy Compact — Handoff

LOOP_ID: B2
RUN_TYPE: CONTENT
PRIMARY_DOMAIN: education / patronage / personal autonomy
SECONDARY_DOMAINS: institutional history; dialogue persistence; consent / authority boundaries
RECENT_DOMAIN_WINDOW: pirate harbor law; family memory/privacy; Coalition rescue handoff
DIVERSITY_STATUS: PASS
CONCENTRATION_JUSTIFICATION: N/A
NEGLECTED_AREA_ADVANCED: education and patronage politics
CROSS_SYSTEM_CONNECTION: B1 Paradise Scholarship Trust Archive -> persistent B2 character consequences

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-paradise-scholarship-autonomy-20260823`
- B1 dependency: `Paradise Scholarship Trust Archive: offered`
- No self-integration; A3 retains integration authority.

## Character / dynamic-content behavior
Adds Paradise admissions officer **Leonie Harrow** and scholarship recipient **Darin Vale** in a three-mission persistent arc about donor conditions, academic authority, recipient consent, and the difference between recognition and control.

Offer routes:
1. recipient autonomy — new publicity/career obligations require fresh consent;
2. bounded donor conditions — prospective and explicit, never retroactive or converted into unrelated academic penalties;
3. layered records — academic selection, award terms, donor recognition, mentorship, and publicity consent stay distinct;
4. refusal — records refusal and does not schedule Review.

Each substantive route schedules Review after 7–11 days. Review resolves copied-template authority drift into one of two persistent settlements:
- **portable scholarship charter** — funding source, academic criteria, donor conditions, consent, duration, review points, and excluded authorities travel together;
- **admissions firewall and renewal** — academic selection remains independent and donor conditions expire unless knowingly renewed.

`Darin Remembers` is the one-shot aftermath reader.

## State ownership / persistence
- All writes are `B2 Paradise Scholarship Autonomy Compact:*`.
- B1 Paradise Scholarship Trust history is read-only.
- No `world:*`, credits, reputation, cargo, outfits, ships, fleets, combat, B1, or A2 writes.
- All seven dialogue/state-only terminal paths use `decline`; no objective-less accepted mission is introduced.
- Refusal does not arm Review.

## Canon / continuity assumptions
The B1 archive establishes Paradise scholarship trusts as opportunity-widening institutions still shaped by concentrated private wealth and founder conditions. This B2 slice does not claim donors control universities, admissions, student careers, or speech. It preserves the distinction among academic selection, financial support, disclosed conditions, later donor requests, recipient consent, recognition, mentorship, and public representation.

## DIVERSITY_CHECK
- Primary domain: education / patronage / personal autonomy.
- Recent same-lane domains considered: law/personal autonomy (Pirate harbor), family memory/privacy, rescue/medical handoff.
- Adjacent-lane work considered: B1 Paradise scholarship institutional history and active global B2 dialogue-lifecycle audit.
- Why this is not another iteration of the same subsystem: it is additive current-main character content and does not touch the global lifecycle audit or another freight/resource/capacity structure.
- Underrepresented area advanced: education and donor-recipient power.
- New cross-system connection: B1 Scholarship Trust Archive becomes a persistent player-facing dispute with delayed consequences.
- Persistent/player-visible capability added: three durable approaches, two terminal institutional compromises, trust flags, and one-shot aftermath.
- Concentration exception: N/A.

## Validation plan / evidence
Focused validator: `python3 tools/story/validate_b2_paradise_scholarship_autonomy.py`
Repository validation: `python3 tools/story/validate_story_repo.py`, focused validator discovery, A1 state-ownership contracts, changed-content style, production build, and stock save-load smoke through repository-native workflows.

Exact validation results and final candidate SHA must be added before READY. Until both repository-native workflows are terminal green on the exact production/validator candidate, verdict is **PARTIAL**.

## A3 / B3 notes
A3 should re-read current `main` immediately before integration and verify clean ancestry. Preserve the B1 read-only gate and all B2 persistence names. B3 should reject any later reuse that turns one donor-recipient compromise into universal Paradise law, or that treats repeated copies of a scholarship form as fresh consent.

## Verdict
PARTIAL pending repository-native exact-head simulation/story/style and production build/save-load validation.
