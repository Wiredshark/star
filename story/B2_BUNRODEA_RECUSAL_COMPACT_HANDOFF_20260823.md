# B2 Bunrodea Recusal Compact — Handoff

LOOP_ID: B2
RUN_TYPE: CONTENT
PRIMARY_DOMAIN: institutional ethics / personal ties / decision authority
SECONDARY_DOMAINS: petition review; character trust; recusal / disclosure boundaries
RECENT_DOMAIN_WINDOW: Paradise education/patronage; Pirate harbor law; Dirt Belt family memory
DIVERSITY_STATUS: PASS
NEGLECTED_AREA_ADVANCED: conflict-of-interest ethics and personal ties inside civic decision-making
CROSS_SYSTEM_CONNECTION: integrated B2 Bunrodea Review Queue aftermath -> new B2 character consequences

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-bunrodea-recusal-compact-20260823`
- Production commit: `73dbd42a29fd554dc058b85004aa74f31925dce6`
- Validator commit: `ce9cdd9756e573413c15a49a8de95cce0f288401`
- Dependency: integrated `B2 Bunrodea Review Queue Compact: aftermath seen`
- No self-integration; A3 retains integration authority.

## Character / dynamic-content behavior
Adds Bunrodea petition reviewer **Tavi Rell** and independent case observer **Nema Oss** in a persistent three-mission arc about conflicts of interest, family ties, disclosure, recusal, and the distinction between evidence work and final decision authority.

Offer routes:
1. direct recusal — close family or material ties move final authority elsewhere while preserving why;
2. disclosure plus second review — weaker ties remain disclosed but require genuine independent confirmation;
3. layered authority — a conflicted reviewer may help organize evidence but may not own the final ruling;
4. refusal — records refusal and does not schedule Review.

Each substantive route schedules Review after 7–11 days. Review resolves copied-disclosure drift into one of two persistent settlements:
- **portable recusal record** — relationship, disclosure, allowed role, excluded authority, substitute decision-maker, independent review, and closure travel together;
- **tiered conflict screen** — direct conflicts force recusal, weaker ties trigger independent review when relevant, and stale/irrelevant ties stop propagating as active warnings.

`Nema Remembers` is the one-shot aftermath reader.

## State ownership / persistence
- All writes are `B2 Bunrodea Recusal Compact:*`.
- Integrated B2 Bunrodea Review Queue aftermath is read-only.
- No `world:*`, A1/A2/B1, credits, reputation, cargo, outfit, ship, fleet, or combat mutation.
- All seven dialogue/state-only terminal paths use `decline`.
- Refusal does not arm Review.

## Canon / continuity assumptions
This slice does not assert that personal ties prove corruption. It distinguishes a disclosed relationship from a finding of misconduct, evidence expertise from final authority, direct material/family conflicts from weaker social ties, and historical conflict notes from active current restrictions. The compact is a local Bunrodea review practice rather than a centralized ethics code or universal law.

## DIVERSITY_CHECK
- Primary domain: institutional ethics / personal ties / decision authority.
- Recent B2 domains considered: education/patronage, pirate harbor neutrality, family memory/privacy, rescue handoff, volunteer command, irrigation capacity.
- Why this is distinct: it is not another freight-throughput or queue-capacity arc; the integrated queue aftermath is only the trigger for a new character problem about who may legitimately decide a case.
- Persistent/player-visible capability: three durable ethical approaches, two terminal recusal models, route-specific trust, and one-shot aftermath.

## Validation status
Current verdict: **PARTIAL** pending repository-native exact-head validation.

Required gates:
- focused validator and Python compile;
- repository-wide focused story validation;
- A1 simulation/state-ownership contracts;
- changed-content style;
- production configure/build;
- stock save-load smoke.

Do not promote to READY until exact candidate validation is terminal green.

## A3 / B3 notes
A3 should re-read current `main` immediately before integration and verify ancestry/mergeability. Preserve the integrated Bunrodea Review Queue aftermath as read-only and preserve every `B2 Bunrodea Recusal Compact:*` persistence name. B3 should reject later reuse that treats disclosure as proof of guilt, lets copied conflict notes manufacture new evidence, or turns a local recusal compromise into centralized Bunrodea authority.

## Verdict
**PARTIAL** until exact repository-native validation completes successfully. B2 remains unmerged; A3 retains integration authority.
