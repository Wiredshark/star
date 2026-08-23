# B2 Unfettered Lineage Memory Compact — handoff

VERDICT: READY for A3 review/integration.

LOOP_ID: B2
RUN_TYPE: CONTENT
PRIMARY_DOMAIN: culture/ideology + family/personal relationships
SECONDARY_DOMAINS: historical evidence, consent/privacy, campaign-state reaction
RECENT_DOMAIN_WINDOW: resource/ecological state; careers/backgrounds/skills; war/diplomacy/military authority
DIVERSITY_STATUS: PASS
CONCENTRATION_JUSTIFICATION: N/A
NEGLECTED_AREA_ADVANCED: family memory, cultural inheritance, intergenerational disagreement
CROSS_SYSTEM_CONNECTION: B1 Unfettered Lineage Recitation Archive + Unfettered campaign phase + persistent B2 relationship state

## Authority and isolation

- Repository authority: `Wiredshark/star`.
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/b2-unfettered-lineage-memory-compact-20260823`.
- Production commit: `384dd46491f1875b2b49d09cb5d4fda8f17ec2fc`.
- Focused-validator commit: `1ffd2ab61a47ea1723a8a21faf4110380a02c682`.
- Exact fully validated candidate: `e122e5a3b08a75d1783db6d903cf847e7fea17aa`.
- This READY promotion changes only this durable handoff; production and validator behavior are unchanged from the fully validated candidate.
- No self-integration.

## Character / dynamic-content slice

Adds a three-mission cultural/family arc centered on two relatives from one Unfettered lineage. The player privately thinks of them as the **Reciter** and **Descendant**; those are shorthand, not canonical Unfettered offices.

`The Story Inside the Story` consumes `Unfettered Lineage Recitation Archive: offered`, Unfettered first contact, and the pre-invasion campaign phase. A family recitation describes a disputed ancestor differently from an older recording. The player may:

1. preserve the recitation intact as living inheritance while attaching speaker/lineage/date/evidence-class provenance;
2. preserve contradictory versions side by side instead of choosing a master version without stronger evidence;
3. keep publication consent with the lineage while allowing the archive to index that a version exists;
4. refuse to turn one family dispute into general archival policy.

Each substantive route persists distinct trust/relationship state and schedules the Review after 7–11 days.

`When the Older Voice Returns` reacts to whether `event: wanderers: unfettered invasion starts` has become true before the Review. A third recording sharpens the disagreement. The player resolves the dispute into either:

- **layered recitation record** — recording/transcript, speaker/lineage, source chain, later retellings, contradictions, and evidence class remain separable; or
- **consent-and-citation ledger** — public excerpts carry origin, permission scope, allowed use, and whether the full recording remains private.

`Descendant Remembers` is the one-shot aftermath reader and demonstrates the selected model in later family/archive practice.

## Ownership / persistence

- Reads `First Contact: Unfettered: offered`.
- Reads `Unfettered Lineage Recitation Archive: offered`.
- Reads `event: wanderers: unfettered invasion starts` as context only.
- Does not mutate B1, campaign, `world:*`, credits, reputation, cargo, outfits, ships, fleets, or combat state.
- Every explicit persistent write is namespaced under `B2 Unfettered Lineage Memory Compact:*`.
- All seven dialogue/state-only terminal paths use `decline`; there is no objective-less `accept` lifecycle.
- No save migration is required because this is additive state.

## Canon / continuity invariants

- A living family inheritance is not identical to direct historical evidence.
- Repetition does not create independent corroboration.
- Contradictions remain attached to their speakers and source chains rather than being flattened into generic uncertainty.
- Preserving a recording does not automatically authorize public reproduction.
- The invasion may increase the social pressure placed on old stories, but it does not make one retelling more evidentially true.
- `Reciter` / `Descendant` are player-private shorthand, not Unfettered titles, offices, or centralized archival authority.
- One lineage's compromise does not become universal Unfettered archive law.

## Exact validation evidence

Exact candidate `e122e5a3b08a75d1783db6d903cf847e7fea17aa` passed both repository-native acceptance workflows:

- `Fork simulation and story validation` #494 / run `32658368261`: **SUCCESS**.
  - focused Python validation compilation: SUCCESS;
  - all focused story validators, including `validate_b2_unfettered_lineage_memory_compact.py`: SUCCESS;
  - A1 simulation/state-ownership contracts: SUCCESS;
  - changed-content style: SUCCESS.
- `Fork save-load integration smoke` #479 / run `32658368244`: **SUCCESS**.
  - dependency installation: SUCCESS;
  - production configure: SUCCESS;
  - production build: SUCCESS;
  - stock save-load smoke: SUCCESS.

Focused validator command:

`python3 tools/story/validate_b2_unfettered_lineage_memory_compact.py "data/hai/b2 unfettered lineage memory compact.txt"`

## DIVERSITY_CHECK

- Primary domain: cultural/ideological conflict + family/personal relationship.
- Recent same-lane domains considered: Dirt Belt irrigation/resource obligations; Career Principle command mentorship; Free Worlds volunteer command authority.
- Adjacent-lane work considered: B1 Unfettered lineage-memory archive; Unfettered campaign invasion state; active global dialogue-lifecycle audit.
- Why this is not another iteration of the same subsystem: no freight, market, supply-shortage, convoy, or repair-capacity premise; the player arbitrates inheritance, contradiction, consent, and intergenerational trust.
- Underrepresented area advanced: family ties and cultural memory.
- New cross-system connection: B1 historiography becomes a persistent family relationship conflict whose Review changes tone if the invasion starts.
- Persistent/player-visible capability added: route-specific trust, two durable cultural-memory settlement models, and a one-shot later character reader.
- Concentration exception: N/A.

## A3 / B3 integration notes

A3 should re-read current `main`, verify the branch still descends cleanly from the recorded authoritative base, inspect any intervening Unfettered content, and preserve the state/private-shorthand boundaries above. Do not self-integrate B2.

B3 should specifically check that later Unfettered content does not treat the layered record or consent ledger as a centralized political institution, and that wartime dialogue does not turn lineage tradition into proof of historical or territorial claims.
