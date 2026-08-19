# B2 Character and Dynamic-Content Packets

This file contains implementation-ready B2 character/content packets for the Endless Sky fork. B2 owns character definition, relationship pressure, dialogue-ready conflicts, and durable story-facing state design. Engine primitives remain A2/A1 territory and authoritative integration remains A3 territory.

## ES-STORY-0002 — Broken Compact

### Status

**B2 READY / STORY_CANON / IMPLEMENTATION-READY CONTENT PACKET**

### Primary domain

**PERSISTENT RELATIONSHIPS / LAW / OWNERSHIP**

This packet deliberately follows the freight/logistics-heavy `ES-STORY-0001` with a non-economic primary conflict. Money and ship value exist as stakes, but the core problem is testimony, ownership, prior promises, and whether a professional relationship survives a disputed transfer.

### Location

Primary proof location: **New Washington** and nearby Republic space.

The production builder may move the exact planet/system anchor if current integrated story data has a safer campaign window, but the packet assumes a Republic legal/institutional context and an accessible shipyard or port authority.

### Named characters

#### Nadia Kelm

Status: **STORY_CANON**

- Life stage: experienced human ship systems engineer.
- Current role: independent refit specialist who supervised the final major overhaul of the disputed vessel *Morrow Line*.
- Public position: argues that the vessel belongs to the surviving operating partnership because years of uncompensated labor were explicitly treated as equity.
- Personality: controlled, exact, professionally proud, reluctant to expose private agreements unless forced.
- Strengths: technical records, strong memory for verbal commitments, credible with mechanics and yard staff.
- Flaws: assumes competent people remember promises as precisely as she does; can mistake moral certainty for legal certainty.
- Fear: that labor treated as temporary sacrifice will be erased once the asset becomes valuable.
- Goal: preserve the operating partnership and obtain formal recognition of the equity agreement.
- Secret: she altered the overhaul schedule to keep the ship operating after a cash crisis, accepting safety-neutral deferred cosmetic/comfort work without documenting that concession in the formal yard packet.
- Independent trajectory: if ignored, Kelm petitions the local port authority and begins collecting mechanic testimony. She will not falsify evidence, but she may publicly accuse Elias Dorne of opportunism if the dispute drags on.

#### Elias Dorne

Status: **STORY_CANON**

- Life stage: middle-aged human logistics manager and executor for the late registered owner.
- Current role: administers the deceased owner's estate and claims the ship must be sold to satisfy explicit written obligations.
- Public position: the registry and debt documents are clear; informal promises cannot override creditors and heirs.
- Personality: formal, weary, skeptical of heroic narratives about sacrifice.
- Strengths: understands contracts, keeps records, notices when people use sentiment to blur ownership.
- Flaws: discounts informal institutions and labor relationships that were intentionally left undocumented.
- Fear: being remembered as the executor who gave away an estate asset and left dependents with the loss.
- Goal: settle the estate without fraud, favoritism, or a years-long legal fight.
- Secret: before the owner's death, Dorne received a private message acknowledging that Kelm and the operating crew were owed "a share of whatever the ship becomes," but the message never defines a percentage or legal instrument.
- Independent trajectory: if ignored, Dorne schedules a sale after a notice period. If credible testimony surfaces before then, he pauses the sale and seeks arbitration; if only rumor surfaces, he proceeds.

#### Mara Senn

Status: **STORY_CANON**

- Life stage: younger human pilot and former relief captain of the *Morrow Line*.
- Current role: neutral-seeming witness whose testimony can materially change the dispute.
- Personality: observant, conflict-averse, protective of people who gave her early work.
- Strengths: present for several key conversations; understands how the operating partnership functioned day to day.
- Flaws: delays difficult testimony until forced, especially if one side frames disclosure as betrayal.
- Fear: that any statement she makes will destroy one of the two relationships that built her career.
- Goal: keep the ship working and avoid becoming the public face of the dispute.
- Secret: she possesses a contemporaneous maintenance log annotation that references the equity promise obliquely, but she does not initially recognize its legal/story significance.
- Independent trajectory: if ignored, Senn leaves Republic space for a contract before the sale date, making later testimony harder but not impossible to recover.

### Premise

The registered owner of the *Morrow Line* has died. The legal registry points toward an estate sale, but Nadia Kelm and the operating crew spent years accepting reduced cash compensation because the owner repeatedly described their sacrifice as building an eventual shared stake in the vessel. Elias Dorne, acting for the estate, finds no formal equity agreement and has real obligations to heirs and creditors.

The dispute is designed so neither side is a disposable villain. The player can investigate what was promised, decide what evidence deserves weight, broker a compromise, exploit the ambiguity, or refuse involvement. The result should persist in later character reactions and access.

### Existing-state inputs

A static implementation can use ordinary persistent mission/global conditions for:

- whether the player has previously assisted New Washington legal/port authorities;
- government reputation with the relevant Republic authority;
- prior mission outcomes involving Nadia Kelm or Elias Dorne once those characters are integrated;
- whether Mara Senn's log annotation has been discovered;
- whether the private Dorne message has been disclosed;
- whether the player gave testimony, brokered settlement, backed a sale, or walked away;
- whether the player has a relevant future background/skill flag exposed by A2, such as engineering, legal/professional history, or Contract Spacer institutional knowledge.

Future A1/A2 inputs may additionally include local labor pressure, shipyard congestion, legal enforcement posture, relationship tiers, and persistent named-character memory. Those remain authoritative in their owning systems; this packet must not create a duplicate dialogue-only truth source.

### Dialogue-ready player approaches

The production conversation should expose at least three materially different routes, with no universal best answer.

1. **Evidence-first investigation**
   - Ask Kelm, Dorne, and Senn for records separately.
   - Discover contradictions without immediately choosing a side.
   - Can reveal the private message and maintenance annotation.
   - Persistent identity: `ES-STORY-0002: evidence broker`.

2. **Professional/engineering interpretation**
   - Available only when an authoritative engineering/professional state exists.
   - Recognize that the deferred overhaul and operating sacrifices were economically substantive even though the legal form is weak.
   - Player-visible label target: `[Engineering: deferred refit records]`.
   - This route can strengthen Kelm's case but does not prove a specific ownership percentage.

3. **Institutional/legal interpretation**
   - Available when an authoritative legal/professional/reputation condition justifies it.
   - Separate evidence of obligation from evidence of title and push both sides toward arbitration or a structured settlement.
   - Player-visible label target: `[Republic procedure: preserve the claim before sale]`.
   - This route may protect both heirs and operators but can leave both characters dissatisfied.

4. **Relationship appeal**
   - Requires prior trust with Kelm, Dorne, or Senn once persistent character-memory support exists.
   - Uses remembered behavior rather than generic persuasion.
   - Can cause a character to disclose evidence earlier, accept a compromise, or refuse because the player's prior conduct damaged trust.

5. **Back the registered estate**
   - Support Dorne's sale plan and argue that unwritten promises cannot bind third parties.
   - Can produce a clean legal outcome while permanently damaging Kelm's relationship and dispersing the operating crew.

6. **Back the operating partnership**
   - Treat the accumulated labor/equity promise as controlling and pressure Dorne to transfer or sell at a discounted internal valuation.
   - Can preserve the crew but expose Dorne to creditor/heir criticism and later legal challenge.

7. **Exploit the ambiguity**
   - Seek to buy the vessel/claim cheaply, trade evidence for access, or use the conflict to acquire leverage.
   - Valid content, not a game-over choice.
   - Creates durable distrust even if financially successful.

8. **Decline involvement**
   - The story advances without the player.
   - Dorne schedules the sale; Kelm petitions; Senn may leave the region.
   - Later content should report which trajectory resolved first.

### Required branching characteristics

A production implementation should satisfy all of the following:

- at least three selectable approaches with distinct intent;
- at least two state-dependent approaches or result variants;
- at least one visible special-response requirement label once A2's reusable metadata support exists;
- at least one unavailable/hidden route that becomes available through evidence or relationship history;
- at least one non-optimal/refusal route that remains valid content;
- no branch that invents a hidden legal/relationship stat solely for this conversation.

### Persistent consequence states

Use stable conditions or the future generalized character-memory primitive; do not create both.

Story-level outcomes:

- `ES-STORY-0002: settlement operating partnership`
- `ES-STORY-0002: settlement estate sale`
- `ES-STORY-0002: settlement arbitration`
- `ES-STORY-0002: settlement player acquisition`
- `ES-STORY-0002: unresolved at departure`

Evidence/history:

- `ES-STORY-0002: found private message`
- `ES-STORY-0002: found senn annotation`
- `ES-STORY-0002: player testimony public`

Character consequences:

- `ES-STORY-0002: kelm trusts player`
- `ES-STORY-0002: kelm resents player`
- `ES-STORY-0002: dorne trusts player`
- `ES-STORY-0002: dorne resents player`
- `ES-STORY-0002: senn disclosed evidence`
- `ES-STORY-0002: senn left region`

If/when named-character memory becomes authoritative, these names become migration inputs rather than permanent duplicate flags.

### Later readers

The first production implementation is not complete until at least one later content reader consumes the outcome. Valid readers include:

- Kelm offering or refusing a later refit/engineering contract;
- Dorne acting as a legal/logistics contact who remembers the player's treatment of evidence;
- Senn providing a later witness introduction or refusing involvement because of prior pressure;
- a port-authority news/mission variant referencing the settlement;
- a later ship-ownership dispute using the outcome as precedent/reputation context without cloning the plot.

### Character-specific follow-up matrix

#### Kelm

- **Operating partnership settlement:** becomes an available engineering/refit contact; future dialogue acknowledges that the player treated labor history as evidence.
- **Estate sale:** leaves the *Morrow Line* project and may refuse ordinary favors while still accepting safety-critical work.
- **Arbitration:** respects procedural fairness if the player disclosed all evidence; distrusts the player if evidence was selectively withheld.
- **Player acquisition:** relationship depends on whether the player honored crew claims after purchase.

#### Dorne

- **Estate sale:** trusts the player's institutional reliability unless the player exploited the sale.
- **Operating partnership settlement:** may accept the result if the private message was disclosed honestly; resents coercion if the player threatened reputation without evidence.
- **Arbitration:** becomes a future procedural/legal contact when the player preserved both claims.
- **Player acquisition:** becomes hostile if evidence was used primarily to depress the sale price.

#### Senn

- **Evidence handled carefully:** becomes more willing to provide later testimony or introductions.
- **Publicly pressured:** leaves sooner and resists future involvement.
- **Annotation ignored after discovery:** remembers that the player chose a conclusion before evidence.

### Failure and compromised outcomes

Failure is content:

- The player backs Kelm before finding the private message, then discovers the promise was vaguer than claimed.
- The player backs Dorne before discovering Senn's annotation, damaging a legitimate claim.
- Senn departs before the player seeks her evidence.
- The sale proceeds while arbitration is being arranged, producing a later claim against the buyer.
- The player purchases the ship but inherits the unresolved crew claim.
- Both parties accept a compromise but neither relationship becomes warm.

None of these should require reload to continue the campaign.

### Production-data implementation path

B2 authoring can supply the dialogue/character packet now. A2/A3 should implement the first production slice using existing Endless Sky mission/conversation conditions plus any already-integrated reusable dialogue metadata mechanism.

Recommended content shape:

1. port/spaceport trigger introduces Dorne's sale notice;
2. first Kelm conversation establishes the labor-equity claim;
3. optional evidence missions/conversations expose Senn and Dorne records;
4. final multi-route conversation records settlement and character consequences;
5. at least one short later reader conversation or mission checks the chosen consequence.

Do not require a new generic dynamic-story scheduler for this static vertical slice.

### Save/persistence assumptions

- All static proof state must use existing save-persistent condition/mission mechanisms or an already-integrated generalized character-memory primitive.
- Old saves must default to no `ES-STORY-0002:*` conditions and therefore remain unaffected.
- Re-entering the content after save/load must not re-award evidence, duplicate the settlement, or reset character attitude.
- The packet assumes no irreversible engine schema change.

### A2 dependencies

A2 may consume this packet for the modern dialogue priority. In particular:

- response requirement/presentation metadata should be generic, not hard-coded for Kelm/Dorne/Senn;
- professional/legal/relationship checks must read authoritative player/character state;
- ordinary mission/global conditions are acceptable for the static proof when richer systems are not integrated yet;
- at least one consequence must be read by later production content.

### A1/world-state dependencies

No new A1 system is required for the static proof. Future systemic variants may consume local legal posture, shipyard labor stress, or other world facts only after A1 exposes authoritative values.

### A3 integration notes

A3 should reject the content as `INTEGRATED_PRODUCTION_SLICE` unless actual game data demonstrates:

- distinct Kelm/Dorne/Senn routes in a real conversation;
- persistent evidence/settlement consequences;
- a later reader;
- save/load stability;
- stock conversation compatibility;
- no duplicate character-memory authority;
- runtime exercise and, if UI presentation metadata is changed, actual-game visual proof.

### B3 continuity notes

B3 should specifically check:

- whether Nadia Kelm / Elias Dorne already exist in another active packet with conflicting roles;
- whether *Morrow Line* ownership history contradicts any later accepted New Washington content;
- whether Senn's departure/survival/location remains consistent after the resolution;
- whether relationship outcomes have one authoritative persistence representation;
- whether later content treats arbitration, sale, transfer, and player acquisition as mutually exclusive terminal states.

### Diversity check

- **Primary domain:** persistent relationships / law / ownership.
- **Recent domain avoided:** economy/logistics/freight crisis from `ES-STORY-0001`.
- **Non-economic inputs:** testimony, evidence discovery, professional memory, legal procedure, prior trust, character location.
- **Persistent consequences:** named-character trust/resentment, ownership resolution, evidence history, access to later contacts, future testimony.
- **Structural distinction:** no shortage, convoy, cargo-loss, route-security, or market-stabilization loop.

### Acceptance verdict

**READY for A2/A3 production implementation as a B2 character/content packet.**

This verdict does not claim that the production conversation already exists. The packet is intentionally a specialist handoff: it defines named characters, state-dependent approaches, durable consequences, later-reader obligations, continuity risks, and implementation constraints without taking A2 engine ownership or A3 integration authority.
