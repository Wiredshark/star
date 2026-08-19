# B2 Republic Displacement Compact — A3/B3 Handoff

## Verdict

**PARTIAL — isolated production candidate. Do not integrate until normal Endless Sky content/parser/runtime/save-load gates pass.**

## Repository state

- Repository authority: `Wiredshark/star`
- Authoritative `main` recovered before branching: `953629bd94aa7ef2e525f2f4bb4c08bc9cb62053`
- B2 branch: `agent/b2-republic-displacement-compact-20260818-2228`
- Production commit: `e3c86efcef00b8e8b81e25df1a36b9d01ac4a42e`
- Validator implementation/fix head before this handoff: `4aed150e5fa866163d8fafe46e49255d52569a9c`

## Scope

This B2 slice consumes the newly authoritative A1 Republic civilian-displacement simulation and turns it into persistent named-character content.

Authoritative A1 input:

- `world: republic displacement pressure`

B2 is read-only with respect to that signal. It never mutates any `world:*` condition.

Named characters:

- **Lena Ortiz** — Republic civil-relocation coordinator; prioritizes continuity of housing/passage responsibility so displaced residents cannot fall between offices.
- **Devin Hale** — independent transit operator; prioritizes explicit capacity, duration, transfer, and responsibility records so emergency reservations remain operationally legible.

## Production behavior

File: `data/human/b2 republic displacement compact.txt`

Three missions:

1. `B2 Republic Displacement Compact: Offer`
   - offers while displacement pressure is `>= 2`;
   - severe framing activates at `>= 4`;
   - three substantive persistent routes plus refusal:
     - continuity protection;
     - transfer ledger;
     - paired continuity compact;
     - decline.

2. `B2 Republic Displacement Compact: Review`
   - only offers after A1 naturally lowers displacement pressure below `2`;
   - remembers the original player route;
   - resolves to one of two terminal institutional outcomes:
     - `settlement continuity compact`;
     - `settlement bounded review`.

3. `B2 Republic Displacement Compact: Hale Remembers`
   - later one-shot reader of either terminal settlement.

## Ownership and persistence invariants

- A1 remains sole owner/writer of `world: republic displacement pressure`.
- B2 writes only `B2 Republic Displacement Compact:*` mission/global conditions.
- No credits, reputation, cargo, combat-rating, outfit, or simulation-state mutation is introduced.
- Old saves default to no B2 conditions and remain unaffected until the Offer conditions are met.
- The Review deliberately waits for A1 displacement pressure `< 2`; B2 does not force the simulation to recover.
- The later reader is one-shot via `B2 Republic Displacement Compact: aftermath seen`.

## Executed validation

A fresh clone of the exact B2 branch was created in an isolated administrator scratch directory on the private execution host. No unrelated repository workspace or service process was modified; command runs reported zero orphan processes.

Executed successfully:

```text
python3 tools/story/validate_b2_republic_displacement_compact.py "data/human/b2 republic displacement compact.txt"
```

Observed:

```text
PASS: B2 Republic Displacement Compact structure validated
PASS: missions=3
PASS: named_characters=2
PASS: a1_signal=read-only
PASS: initial_routes=3 + refusal
PASS: terminal_settlements=2
PASS: later_reader=Hale Remembers
```

Also executed successfully:

```text
python3 tools/story/validate_story_repo.py
```

Observed repository-contract PASS.

Also executed successfully:

```text
python3 tools/story/test_b2_character_packets.py
```

Observed existing B2 Broken Compact packet-contract PASS, confirming this slice did not break that durable story contract.

## Validation limitation

Attempted:

```text
python3 utils/check_content_style.py
```

The checker did **not** start because the execution environment lacks the third-party Python package `regex`:

```text
ModuleNotFoundError: No module named 'regex'
```

This is an environment limitation, not a content-style PASS or content failure.

No full configured Endless Sky parser/build/game runtime/save-load roundtrip is claimed in this handoff.

## Required A3 acceptance before integration

Run against the exact final candidate head:

1. `python3 tools/story/validate_b2_republic_displacement_compact.py "data/human/b2 republic displacement compact.txt"`
2. `python3 utils/check_content_style.py`
3. normal Endless Sky content parser/build validation;
4. runtime smoke-load on Republic inhabited ports;
5. verify Offer appears at displacement `2-3` with baseline framing and at `>= 4` with severe framing;
6. exercise continuity / ledger / compact / refusal routes and save/load each state;
7. verify Review remains unavailable while displacement pressure is `>= 2` and appears after A1 lowers it below `2`;
8. exercise both terminal settlements and verify only one can be recorded;
9. verify `Hale Remembers` consumes either settlement once;
10. verify A1 displacement pressure continues rising/decaying/resettling independently of all B2 conditions.

## A3/B3 integration notes

- This slice is based directly on the current authoritative `main` that introduced Republic civilian displacement pressure, so no additional B1 ancestry is required.
- Preserve the central continuity invariant: emergency relocation rules may react to displacement pressure, but B2 never owns or drives that pressure.
- B3 should reconcile any later Republic relocation/civil-defense content so protected continuity and auditable capacity are treated as competing operational values rather than proof that one institution is universally correct.
- A3 should integrate only after the required content/parser/runtime/save-load gates pass.
