# B2 Saryd Seed Stewardship handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** READY for A3 review/integration  
**Authoritative main observed at selection:** `6dc761ac941794c8b1125978d7bcd6eb811e3951`  
**B1 parent:** `dadfb288911c3e6de14af4035d0dac85c6faa1df` (`agent/b1-saryd-civic-ecology-20260819-1022`)  
**B2 branch:** `agent/b2-saryd-seed-stewardship-20260819-1028`  
**Production commit:** `b273e40f8c41a28d4745516190d7ef371903ec59`  
**Validator commit:** `7d1d0031c461a62c6faf47f4b65ee7e9e53d114d`  
**Exact production/data/validator/handoff head validated by CI:** `b0cdc5f41f4b49a6cd0ddaead34c185441802ea4`

## Character / dynamic-content behavior

Adds a persistent three-mission Saryd character arc around the B1 Seed Lineage Exchange institution.

Two recurring Saryd are deliberately identified only through player-private shorthand:

- **Keeper** — usually checks old lineage labels against machine-readable seed records and argues for preserving provenance, uncertainty, and local varieties.
- **Grower** — usually arrives with growers, soil notes, and emergency requests from settlements whose harvests are failing and argues for timely access to useful seed.

The production text explicitly states that neither shorthand is a name or office supplied by the characters. This avoids inventing a centralized Saryd authority or canonical title.

### Offer

A fungal blight creates pressure to release a resistant archived strain before its lineage record is complete. The player may choose:

1. provenance-first;
2. access-first;
3. paired emergency release plus mandatory return records;
4. refusal.

All substantive routes persist independently under the `B2 Saryd Seed Stewardship:*` namespace.

### Review

A later exchange shows the second-order consequence: moving seed successfully can create more living diversity while making lineage relationships harder to reconstruct. The earlier route changes the review presentation.

The player resolves the system into one of two mutually exclusive persistent settlements:

- **portable seed passport** — origin, known crosses, field performance, retained local reserve, and uncertainty travel with distributed seed;
- **local reserve covenant** — working seed may be distributed and adapted freely, but each participating community preserves and periodically verifies an uncrossed local reference population.

### Later reader

`Keeper Remembers` consumes either terminal settlement once and records `aftermath seen`.

## B1 dependency and continuity

Consumes the B1 Saryd civic/ecology institutional-history slice, especially:

- Seed Lineage Exchange;
- forest/ecological recovery memory;
- climate adaptation and inter-world research practice.

Important invariants:

- shared records do not imply centralized political authority;
- a seed exchange is a living adaptation network, not a mandate to freeze local varieties unchanged;
- emergency distribution should not erase origin/uncertainty from the record;
- preserving local reference populations should not prohibit working populations from adapting.

## State ownership

All writes are namespaced `B2 Saryd Seed Stewardship:*`.

The slice intentionally does not write:

- `world:*` simulation state;
- credits;
- reputation;
- cargo;
- outfits;
- ships or fleets;
- combat rating;
- upstream B1/A1/A2 conditions.

## Files

- `data/coalition/b2 saryd seed stewardship.txt`
- `tools/story/validate_b2_saryd_seed_stewardship.py`
- `story/B2_SARYD_SEED_STEWARDSHIP_HANDOFF_20260819.md`

## Exact validation evidence

Repository-native validation was executed automatically on exact head `b0cdc5f41f4b49a6cd0ddaead34c185441802ea4` after draft PR creation.

### Fork simulation and story validation

Workflow run `32264564160` / run #87: **SUCCESS**.

- changed fork content style: **SUCCESS**;
- focused simulation and story contracts: **SUCCESS**;
- automatic focused story validator suite, including `validate_b2_saryd_seed_stewardship.py`: **SUCCESS**;
- A1 simulation contract tests: **SUCCESS**.

### Fork save-load integration smoke

Workflow run `32264564141` / run #76: **SUCCESS**.

- install build/headless runtime dependencies: **SUCCESS**;
- configure production executable: **SUCCESS**;
- build production executable: **SUCCESS**;
- stock save-load smoke cases: **SUCCESS**.

The B1 parent itself was also re-checked during this B2 run: its simulation/story/style workflow and save-load integration workflow both completed successfully.

## A3 / B3 integration notes

Integration order is B1 Saryd civic ecology institutional history first, then this B2 branch. Re-read current `main` immediately before integration because concurrent A/B work is expected. Preserve the distinction between shared ecological recordkeeping and centralized Saryd authority.

The commit that changes this handoff from PARTIAL to READY is handoff-only; production data and validator code are unchanged from exact validated head `b0cdc5f41f4b49a6cd0ddaead34c185441802ea4`.
