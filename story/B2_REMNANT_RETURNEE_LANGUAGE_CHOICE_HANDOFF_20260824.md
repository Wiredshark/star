# B2 Remnant Returnee Language Choice — handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** READY for A3 review/integration  
**Authoritative base:** `a17a89fb4779200a0634a6dade1811c4dc9cc2be`  
**Branch:** `agent/b2-remnant-returnee-language-choice-20260824`  
**Production commit:** `223d8c8aa59e06d3c53d7be8a6f6d9143529a1aa`  
**Initial validator commit:** `f2c024dda553057d63ddf6c5beaa555359d38b13`  
**Validator wording hardening:** `701da09b139c8eb3fc9cd71786716919cc49f39d`  
**Exact fully validated production/validator candidate:** `0d76c0f0057dfb45e3c773f52da2ed22e999b0a0`

## Scope
Adds Remnant siblings Mira Pell and Eren Pell after `Remnant: Cognizance 4: done`. Mira spent years in Republic space and returned speaking ordinary speech in some contexts while remaining fluent in Remnant sign and song. A copied profile turns that communication preference into an assimilation/loyalty/competence judgment.

Player routes:
- communication autonomy unless a task genuinely requires a shared mode;
- context-specific task requirements without identity inference;
- paired communication-preference / task-requirement records separated from cultural interpretation;
- refusal.

The three substantive routes schedule a Review after 7–11 days. Review resolves copied-scope failures into either a portable communication packet or fresh-context renewal. `Mira Remembers` is the one-shot aftermath reader.

## Ownership / lifecycle
- reads `Remnant: Cognizance 4: done` only;
- all writes are `B2 Remnant Returnee Language Choice:*`;
- no `world:*`, B1/A1/A2, material, reputation, cargo, equipment, ship, fleet, or combat mutation;
- all seven dialogue/state-only terminal paths use `decline`;
- refusal does not arm Review;
- Review requires introduced + delayed-ready + not-yet-reviewed state;
- both settlements close Review once and feed one-shot aftermath.

## Canon / continuity
Remnant canon establishes everyday sign communication with voices normally reserved for song/chant, while at least one older Remnant traveler is shown using ordinary speech after time in Republic space. This slice treats Mira's returnee experience as a local family/personnel conflict, not a definition of Remnant language law, purity, competence, loyalty, or a new office. Communication preference, demonstrated capability, task-specific requirements, cultural interpretation, loyalty, competence, identity, and current review status remain separate facts.

## Files
- `data/remnant/b2 remnant returnee language choice.txt`
- `tools/story/validate_b2_remnant_returnee_language_choice.py`
- `story/B2_REMNANT_RETURNEE_LANGUAGE_CHOICE_HANDOFF_20260824.md`

## Validation
Two early simulation/story attempts failed only in the new focused validator because literal continuity assertions expected wording not present in the production comments. Production changed-content style and repository-wide story/state-ownership contracts were green in those runs. The validator was made formatting/wording-independent without changing production content or weakening the canon boundary.

On exact candidate `0d76c0f0057dfb45e3c773f52da2ed22e999b0a0`:
- Fork simulation and story validation #561 / run `32774174861`: **SUCCESS**;
- focused story validators, including the Remnant returnee validator: **SUCCESS**;
- A1 simulation/state-ownership contracts: **SUCCESS**;
- changed-content style: **SUCCESS**;
- Fork save-load integration smoke #546 / run `32774174873`: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load smoke: **SUCCESS**.

## A3 / B3 integration notes
A3 retains integration authority. Re-read current `main`, open B2/A2 work, ancestry, mergeability, and exact workflow state before integration. Preserve `Remnant: Cognizance 4: done` as read-only, preserve B2-only persistence, preserve refusal suppression of Review, and do not generalize this local sibling compromise into a universal Remnant rule or office.
