# B2 Wanderer Return Home Choice Compact — handoff

Verdict: READY for A3 review/integration.

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-wanderer-return-home-choice-20260825`
- Exact fully validated production/validator/handoff candidate: `ea64e41ebc3faaf6464383ab280769bd698ad0c9`
- Integration authority: A3 only; B2 must not self-integrate.

## Scope
Adds a persistent post-evacuation family arc after integrated `B2 Wanderer Evacuation Recovery Compact: aftermath seen`.

A Wanderer parent and adult child disagree over whether the household's surviving prewar home and an old intention to return should determine the child's current residence after years spent building a life at an evacuation harbor.

Routes:
- present adult consent: old residence remains family history, current residence remains a current choice;
- right without duty: preserve a practical/family route back without turning it into an obligation to occupy the old home;
- paired records: household/property continuity separate from current residence/contact preference;
- refusal: no general rule and no Review chain.

Positive routes schedule a 7–11 day Review. Review resolves into either a portable home-choice packet or fresh-choice renewal. `Child Remembers` is one-shot aftermath.

## Dependencies and ownership
- Reads integrated `B2 Wanderer Evacuation Recovery Compact: aftermath seen` only.
- All new writes are `B2 Wanderer Return Home Choice Compact:*`.
- No `world:*`, A1/A2/B1/prior-B2, credits, reputation, cargo, equipment, ship, fleet, or combat mutation.
- All seven dialogue/state-only terminal paths use `decline`.
- Refusal cannot arm Review.

## Canon / persistence assumptions
The old household, property continuity, evacuation-era intention, family memory, current residence, current home preference, contact scope, and living-adult consent are separate facts. Survival and family continuity do not automatically create a permanent duty to return. A later decision to remain elsewhere does not erase the old home from family history. This is one household's correction, not centralized Wanderer residence law.

## Validation contract
`tools/story/validate_b2_wanderer_return_home_choice_compact.py` proves the exact three-mission graph, integrated prior-B2 dependency, route-local persistence, exactly three 7–11 day schedules, refusal suppression, Review lifecycle gates, settlement-local closure, one-shot aftermath, B2-only writes, seven `decline` terminals, absence of gameplay-objective directives, and the history/current-choice continuity boundary.

## Exact validation evidence
On exact candidate `ea64e41ebc3faaf6464383ab280769bd698ad0c9`:
- Fork simulation and story validation #596 / run `32837512420`: SUCCESS.
  - changed-content style: SUCCESS;
  - focused Python validation compilation: SUCCESS;
  - all focused story validators: SUCCESS;
  - A1 simulation/state-ownership contracts: SUCCESS.
- Fork save-load integration smoke #581 / run `32837512442`: SUCCESS.
  - dependency installation: SUCCESS;
  - production configuration: SUCCESS;
  - production build: SUCCESS;
  - stock save-load smoke: SUCCESS.

The READY promotion after this exact candidate changes only this durable handoff document; production and validator behavior are unchanged from the fully validated candidate.

## Isolation / safety
Exact candidate comparison against authoritative main: 1 commit ahead / 0 behind, exactly three added files, 293 additions, 0 deletions. Branch was created directly from authoritative main after reviewing current open B2 PRs and recent commits. The active `agent/b2-global-dialogue-lifecycle-audit-20260823` branch and unrelated B2 work were left untouched. Four pre-existing service-owned host processes were observed and preserved. No destructive Git operation or self-integration was performed.

## A3 / B3 notes
Before integration, re-read current `main`, open B2/A2/B1 work, ancestry, mergeability, and exact workflow status. Preserve the existing evacuation-recovery aftermath as read-only. Keep family history, property continuity, residence choice, contact preference, and current adult consent distinct.
