# B2 Hai Chosen Family Recognition Compact Handoff — 2026-08-25

Verdict: READY for A3 review/integration.

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-hai-chosen-family-recognition-20260825`
- Production commit: `0036eae26c32535c407259b7e55b130c3f985771`
- Initial focused validator: `ed12fab16064d81d39ffd8d7eedc0602d7d5022c`
- Validator wording repair / exact fully validated candidate: `aacb6eb107139d1161e6e0c699864c3e484b06b1`

## Behavior
Adds Mara Hale, a long-term human resident in Hai space, and Teren, a Hai chosen sibling. Their relationship is socially real, but a copied civic record incorrectly turns that relationship plus one emergency-contact grant into general next-of-kin authority.

The player may:
- preserve chosen-family recognition while keeping formal authority separate;
- make formal powers purpose-specific, bounded, and revocable;
- keep paired social-relationship and formal-authority records;
- refuse to establish a general rule.

Three substantive routes schedule Review after 7–11 days. Review resolves into either a portable relationship-and-authority packet or fresh-context renewal. `Teren Remembers` is a one-shot aftermath reader.

## Dependencies / ownership
- Reads `First Contact: Hai: offered` and `Hai Guest Settlement Register: offered` only.
- All persistent writes are under `B2 Hai Chosen Family Recognition Compact:*`.
- No `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutations.
- All seven state-only terminal paths use `decline`; refusal does not schedule Review.

## Focused validation
`tools/story/validate_b2_hai_chosen_family_recognition_compact.py` proves:
- exact three-mission graph;
- Hai inhabited-source scope and history dependency;
- route-local state and exactly one 7–11 day Review schedule per substantive route;
- refusal suppression of Review;
- settlement-local writes and exactly one Review close per settlement;
- one-shot aftermath consuming either settlement;
- seven `decline` / zero `accept` state-only terminals;
- no gameplay-objective directives;
- B2-only persistent writes and no material/reputation mutation;
- relationship, formal authority, scope, expiry, and renewal remain distinct.

The first simulation/story run exposed one validator-only wording assertion: the comment phrase `chosen family bond` crossed a physical source-comment line boundary. Changed-content style was already green and production semantics were unchanged. The validator was hardened in `aacb6eb107139d1161e6e0c699864c3e484b06b1`.

## Exact validation evidence
On exact candidate `aacb6eb107139d1161e6e0c699864c3e484b06b1`:
- Fork simulation and story validation #587 / `32817142964`: **SUCCESS**;
- focused story validators: **SUCCESS**;
- A1 simulation/state-ownership contracts: **SUCCESS**;
- changed-content style: **SUCCESS**;
- Fork save-load integration smoke #572 / `32817142966`: **SUCCESS**;
- dependency installation: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load smoke: **SUCCESS**.

## Canon / continuity assumptions
The Hai Guest Settlement Register establishes long-term human residents and institutions adapting to cross-cultural families. This slice does not define universal Hai family law. Chosen-family status, inheritance, guardianship, finances, medical communication/decision authority, household access, and emergency contact remain separate facts unless explicitly granted.

## A3 / B3 notes
Do not infer that social family terminology creates legal power. Do not solve ambiguity by erasing the relationship. Copies of an old authority grant do not become current authority after purpose or expiry ends.

A3 retains integration authority. Do not self-integrate.
