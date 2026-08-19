# B2 Rulei Exposure Accountability Handoff — 2026-08-19

## Stage

B2 — Story Characters + Dynamic Content

## Verdict

PARTIAL pending exact-head `Fork save-load integration smoke`. Exact-head simulation/story/style validation is green after one validator-only repair. Do not integrate until the save-load workflow reaches terminal green.

## Repository authority and concurrency

- Repository: `Wiredshark/star`
- Authoritative `main` observed at B2 slice selection: `60ce97cc68a1b2643649896335f5b9ae6418f28e`
- Required B1 dependency branch: `agent/b1-rulei-contact-memory-20260819-1421`
- Required B1 dependency SHA: `6decd04d051c04abf50ed75cf32f65076f4dd11f`
- B1 dependency is 1 commit ahead / 0 behind the observed main and adds `data/rulei/rulei contact memory conversations.txt`.
- No pre-existing B2 Rulei branch was found when the slice was selected. Existing B2 Pug uncertainty work was treated as adjacent but non-overlapping scope.
- Private Fallout execution workspace was inspected before use. Its `github` remote points to `Wiredshark/fallout-test`, not `Wiredshark/star`; the workspace was already dirty and was left untouched. No Endless Sky validation is claimed from that host.

## Isolated B2 branch

- Branch: `agent/b2-rulei-contact-accountability-20260819-1426`
- Base: `6decd04d051c04abf50ed75cf32f65076f4dd11f`
- Draft PR: #106, base `agent/b1-rulei-contact-memory-20260819-1421`

## Commits

- Production character/content slice: `63b6272c934b0ec9771e913a4ba8f0e80c52b86f`
- Focused validator: `03cb2bdcbb50a475f6a6bba99e46a0791f00f964`
- Validator repair allowing explicit negation of unsupported Rulei causation: `caa4d364e0b5d153f88b056c94008f42ad7aff58`

## Files

- `data/rulei/b2 rulei exposure accountability.txt`
- `tools/story/validate_b2_rulei_exposure_accountability.py`
- `story/B2_RULEI_EXPOSURE_ACCOUNTABILITY_HANDOFF_20260819.md`

## Character / dynamic-content behavior

The slice consumes B1's `Rulei History: Exposure Register` and `Rulei History: Testimony Protocol`, which preserve observed Rulei-contact effects separately from causal and motive assumptions.

It introduces two recurring human characters:

- **Dr. Sena Orlov** — physician maintaining exposure and follow-up records.
- **Eli Verran** — veteran navigator whose own Rulei-contact testimony appears in the archive.

The initial dispute concerns how a crew member's Rulei-contact exposure history should follow them after acute symptoms fade. Three substantive routes plus refusal are persistent:

1. **Clinical threshold** — portable observed symptom/recovery/follow-up record with a mandatory expiry/review boundary.
2. **Witness control** — routine operational records carry current fitness and direct observations while testimony/interpretation remains separately controlled.
3. **Paired records** — medical continuity and testimony continuity remain linked but have different access/authority.
4. **Refusal** — no review event and no `introduced` state.

A delayed Review remembers the initial route and exposes a second-order problem: downstream systems can copy a warning while dropping its expiry, context, consent boundary, or uncertainty. The Review resolves into exactly two persistent terminal settlements:

- **bounded exposure certificate** — current fitness, observed exposure history, follow-up, and explicit expiry/review date travel together; raw testimony remains sealed;
- **consent escrow** — secondary use names purpose, audience, and expiry; interpretive claims require renewed consent or a fresh clinical finding.

`Orlov Remembers` is the one-shot aftermath reader for either settlement.

## State ownership and continuity invariants

- Every persistent write is namespaced `B2 Rulei Exposure Accountability:*`.
- B2 reads but does not write `First Contact: Rulei:*` or `Rulei History:*` state.
- No `world:*`, credits, reputation, combat rating, cargo, outfit, ship, or fleet mutation is introduced.
- Observed symptoms, testimony, interpretation, operational fitness, and causal claims remain distinct concepts.
- Rulei-contact exposure may be recorded as an observed correlation/pattern, but the content does not establish that Rulei psionics caused permanent injury or that the Rulei intended harm.
- A medical/operational warning must not become an unbounded permanent identity merely because downstream systems copied it.

## Validation evidence

### Initial exact head `03cb2bdcbb50a475f6a6bba99e46a0791f00f964`

`Fork simulation and story validation` run #109 / `32287631006`:

- Changed fork content style: PASS.
- Focused story runner discovered 36 checks; 35 passed and the new Rulei validator failed.
- Failure was validator-only: its forbidden substring `the rulei caused lasting damage` matched production text that explicitly said the record was **not** such a claim.
- A1 simulation contracts were skipped because the focused-story job stopped at the validator failure.

The validator was repaired in `caa4d364e0b5d153f88b056c94008f42ad7aff58` to reject affirmative unsupported causal/motive statements while allowing explicit negation.

### Repaired exact head `caa4d364e0b5d153f88b056c94008f42ad7aff58`

`Fork simulation and story validation` run #110 / `32287892936`: **SUCCESS**.

- Focused simulation and story contracts: PASS.
- Run all focused story validators: PASS.
- Run A1 simulation contract tests: PASS.
- Changed fork content style: PASS.

`Fork save-load integration smoke` run #99 / `32287893061`: **IN PROGRESS** at handoff creation. No production build or save/load PASS is claimed until this reaches terminal green.

B1 dependency exact head `6decd04d051c04abf50ed75cf32f65076f4dd11f` is already green on both repository-native workflows:

- `Fork simulation and story validation` run #108 / `32287167277`: SUCCESS.
- `Fork save-load integration smoke` run #97 / `32287167176`: SUCCESS.

## A3 integration instructions

1. Do not integrate this B2 slice before the B1 Rulei contact-memory dependency.
2. Require terminal green exact-head simulation/story/style and save-load workflows for the B2 candidate.
3. Preserve all B2-only state ownership and the observation-vs-causation boundary during conflict resolution.
4. Do not convert the exposure record into an authoritative statement about Rulei motives or permanent biological causation.
5. If the B2 save-load workflow fails, repair on the B2 branch and revalidate before promotion to READY.

## B3 continuity notes

- Dr. Sena Orlov and Eli Verran are human characters; no new Rulei person, office, or internal institution is invented.
- B1 archives describe human handling of Rulei-contact evidence, not authoritative Rulei history.
- The slice should remain compatible with the broader Rulei canon in which direct contact can produce invasive voices/headaches while the cause, mechanism, and ancient scarred-world history remain uncertain.
