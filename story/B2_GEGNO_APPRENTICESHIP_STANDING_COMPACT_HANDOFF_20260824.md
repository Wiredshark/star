# B2 Gegno Apprenticeship Standing Compact handoff — PARTIAL

## Authority
- Repository: `Wiredshark/star`
- Authoritative base observed: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-gegno-apprenticeship-standing-20260824`
- Production commit: `c6fd8cca2e11cbb333e6eb6e03e5fb56b5223295`
- Focused validator commit: `8ecbff65e777d7aafa75e799261267dab1970461`
- Current handoff head: filled by this commit

## Scope
Adds a present-day Gegno mentorship / apprenticeship character arc on Tschyss after integrated `B2 Gegno Claim Records: aftermath seen`.

Recurring characters are a veteran Gegno Vi toolwright and younger Gegno Scin machinist whom the player privately thinks of as the **Mentor** and **Apprentice**. Those labels are shorthand only, not Gegno offices, titles, credentials, or evidence of political unification.

The dispute is whether a cross-faction mentorship record should be treated as evidence of demonstrated skill, a bounded reference, political allegiance, or some combination. Player routes:
1. demonstration-first skill evidence;
2. mentor reference bounded to work actually observed;
3. paired skill portfolio + mentorship lineage;
4. refusal to create a general rule.

Positive routes schedule a 7–11 day Review. The Review exposes two downstream failures: copied summaries turning a bounded demonstration into a universal credential, and copied mentor lineage turning training history into political suspicion or allegiance. Terminal settlements are:
- portable skill portfolio;
- challenge and renewal.

`Apprentice Remembers` is the one-shot aftermath reader.

## Dependencies / ownership
Reads only:
- `Gegno Asteroid Mining Prologue: done`;
- `B2 Gegno Claim Records: aftermath seen`.

Writes only `B2 Gegno Apprenticeship Standing Compact:*`.

No `world:*`, B1/A1/A2, Claim Records, material, reputation, cargo, equipment, ship, fleet, faction-attitude, or combat mutation.

## Lifecycle / persistence
- exactly 3 missions + one delayed Review-ready event;
- three substantive routes + refusal;
- positive routes schedule Review at 7–11 days;
- Review requires introduction + review-ready + not-reviewed;
- two terminal settlements each set reviewed exactly once;
- aftermath requires either settlement and is one-shot;
- all 7 dialogue/state-only terminals use `decline`;
- refusal does not schedule Review.

## Canon / continuity assumptions
- Practical shared measurement and record conventions can cross Vi/Scin rivalry without implying political union or friendship.
- Mentor lineage is history, not political allegiance.
- Demonstrated competence is task- and condition-specific, not a universal credential.
- A mentor can attest only to work actually observed; copying an endorsement does not create independent corroboration.
- A materially different task may justify a bounded new demonstration without converting faction identity into a personnel verdict.
- One local apprenticeship compromise is not centralized Gegno certification law.

## Files
- `data/gegno/b2 gegno apprenticeship standing compact.txt`
- `tools/story/validate_b2_gegno_apprenticeship_standing_compact.py`
- `story/B2_GEGNO_APPRENTICESHIP_STANDING_COMPACT_HANDOFF_20260824.md`

## Validation
Current verdict: **PARTIAL** pending repository-native exact-head workflows.

Required before READY:
- focused validator discovered and passes;
- full focused story suite passes;
- A1 simulation/state-ownership contracts pass;
- changed-content style passes;
- production configure/build passes;
- stock save-load integration smoke passes;
- final diff remains isolated to this B2 slice.

## A3 / B3 integration notes
A3 retains integration authority. Do not self-integrate. Re-read current `main`, ancestry, the active global B2 dialogue-lifecycle audit, and current Gegno/B2 work before integration. Preserve the existing Claim Records state as read-only and keep demonstrated skill, mentor lineage, faction identity, political allegiance, current task scope, and explicit renewal as distinct facts.
