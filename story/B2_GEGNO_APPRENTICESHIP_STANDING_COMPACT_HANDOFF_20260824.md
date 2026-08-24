# B2 Gegno Apprenticeship Standing Compact handoff — READY

## Authority
- Repository: `Wiredshark/star`
- Authoritative base observed and rechecked: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-gegno-apprenticeship-standing-20260824`
- Production commit: `c6fd8cca2e11cbb333e6eb6e03e5fb56b5223295`
- Focused validator commit: `8ecbff65e777d7aafa75e799261267dab1970461`
- Exact fully validated production/validator/handoff candidate: `f1fe75b468816de61f71322a001d38fa3c2af94b`
- Final READY handoff-only head: this commit

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

## Exact validation evidence
On exact candidate `f1fe75b468816de61f71322a001d38fa3c2af94b`:
- `Fork simulation and story validation` #523 / run `32707091341`: **SUCCESS**;
- focused Python validation compilation: **SUCCESS**;
- all focused story validators, including the new Gegno validator: **SUCCESS**;
- A1 simulation/state-ownership contracts: **SUCCESS**;
- changed-content style: **SUCCESS**;
- `Fork save-load integration smoke` #508 / run `32707091254`: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load integration smoke: **SUCCESS**.

Exact base-to-candidate isolation: **3 commits ahead / 0 behind**, exactly 3 added files, 388 additions, 0 deletions.

## Process / concurrency boundary
The live `agent/b2-global-dialogue-lifecycle-audit-20260823` branch was detected before authoring and was not touched. Four pre-existing service-owned host processes were observed and preserved. No destructive Git operation, process cleanup, unrelated workspace modification, or self-integration was performed.

## A3 / B3 integration notes
**Verdict: READY for A3 review/integration.** A3 retains integration authority. Re-read current `main`, ancestry, the active global B2 dialogue-lifecycle audit, and current Gegno/B2 work before integration. Preserve the existing Claim Records state as read-only and keep demonstrated skill, mentor lineage, faction identity, political allegiance, current task scope, and explicit renewal as distinct facts.
