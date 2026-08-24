# B2 Near Earth Earth Day Belonging — handoff

Verdict: PARTIAL pending repository-native exact-head validation.

## Authority
- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-near-earth-earth-day-belonging-20260824-1047`
- isolated worktree: `/opt/agent-workspace/star-b2-earth-day-20260824-1047`
- production: `data/human/b2 near earth earth day belonging.txt`
- focused validator: `tools/story/validate_b2_near_earth_earth_day_belonging.py`

## Character / dynamic-content behavior
Adds Near Earth parent Mara Quill and her adult son Leo Quill. B1's Earth Day Archive establishes that Earth Day can function as pilgrimage, civic holiday, or family storytelling after human expansion. This B2 slice turns that background into one family dispute about ancestry, inherited tradition, public observance, and where a living person locates home.

Offer routes:
- heritage invitation rather than inherited obligation;
- Leo's self-authored belonging;
- layered ancestry / family tradition / public observance / current-home model;
- refusal, which does not schedule Review.

Three substantive routes schedule Review after 7–11 days. Review resolves a public-program biography problem into either:
- voluntary heritage statement, where living identity claims come from the person and family history remains attributable; or
- plural belonging, where several compatible attachments can coexist without ranking one as the authentic home or treating nonparticipation as rejection.

`Leo Remembers` is the one-shot aftermath reader.

## Dependencies / ownership
- consumes `Near Earth Earth Day Archive: offered` read-only;
- all writes are `B2 Near Earth Earth Day Belonging:*`;
- no `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, or combat mutation;
- all seven dialogue/state-only terminal paths use `decline`;
- refusal does not arm Review.

## Persistence / canon assumptions
Ancestry, inherited family story, private tradition, public Earth Day participation, present home, and a living person's own identity statement remain separate facts. Declining pilgrimage is not proof of rejecting ancestry or family. Making a pilgrimage is not proof that Earth is a person's only authentic home. A family story may be attributed as family history without automatically becoming every living relative's identity statement. This local family compromise is not Republic policy or a universal definition of human identity.

## Validation so far
- focused validator: PASS
- all focused story validators: 49/49 PASS
- Python focused-code compilation: PASS
- A1 pytest suite: 128/128 PASS in isolated venv
- changed-content style: PASS on committed local candidate
- production build/save-load smoke: pending repository-native exact-head validation

## A3 / B3 integration notes
Do not self-integrate. Re-read current authoritative `main`, active B2/A2 work, ancestry, and workflow state immediately before integration. Preserve B1 Earth Day history as read-only and preserve the ancestry/tradition/home/public-observance distinction. No save-state migration should be needed because this slice only adds new namespaced state.
