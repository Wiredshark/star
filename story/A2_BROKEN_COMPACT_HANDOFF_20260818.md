# A2 Broken Compact specialist handoff — 2026-08-18

## Verdict

**PARTIAL — specialist candidate, not yet A3-ready.**

The production candidate is coherent and isolated, but this automation run did not have an authoritative `Wiredshark/star` checkout/build/runtime host on which to execute the validator, parser/build regressions, save/load, or actual-game runtime. GitHub reports no CI statuses for the candidate commit. A3 must not integrate this as a production slice until the gates below actually run and pass.

## Repository authority and isolation

- Repository: `Wiredshark/star`
- Authoritative A-loop staging branch recovered from live repository evidence: `agent/global-loop-diversity-20260815`
- Exact base SHA: `c6cb81fe47d00c25df9a3947db83eb930f872f35`
- Isolated A2 branch: `agent/a2-broken-compact-20260818-1623`
- Exact cumulative implementation candidate SHA: `f08482ca790618f686fd31a5a5c4801d4e607eb2`
- Candidate is exactly 2 commits ahead of the base and touches only the production data file plus its focused validator.
- No merge, reset, rebase, force push, destructive clean, or authoritative-branch update was performed.

## Concurrency / non-duplication check

Two other open A2 candidates were recovered before selecting this slice:

- PR #2 / `agent/a2-dialogue-vertical-20260818-1406`: Imani Rook persistent dialogue vertical slice.
- PR #5 / `agent/a2-reactive-news-20260818-1502`: persistent-history reactive port news.

This candidate does not modify either slice. It consumes the separate B2 `ES-STORY-0002 — Broken Compact` character/content packet (draft PR #1, head `514ce005c43def6903f01b9dd36364ad7b8bd845`) as narrative input and implements a distinct persistent relationships / law / ownership RPG loop.

## Implemented player-facing loop

Production data: `data/human/a2 broken compact.txt`

The slice adds four missions around New Washington and the disputed vessel *Morrow Line*:

1. **First Hearing**
   - Introduces Nadia Kelm and Elias Dorne.
   - Four player approaches: evidence-first, Republic-procedure route, back the estate sale, or refuse involvement.
   - The Republic-procedure route is gated by real existing `"reputation: Republic" > 0` state and carries a player-visible requirement label.
   - Refusal is valid content and writes a persistent unresolved outcome rather than requiring reload.

2. **Evidence Hearing**
   - Introduces Mara Senn's maintenance annotation and Dorne's private message.
   - Writes persistent evidence state.
   - Three materially different settlement outcomes: arbitration, operating partnership, or estate sale.
   - Writes named-character trust/resentment consequences through ordinary persistent conditions.

3. **Later Reader**
   - Reads the chosen settlement later.
   - Produces distinct Kelm/Dorne future-contact state, proving that the choice is not only stored at the originating conversation.

4. **Refusal Reader**
   - Reads the refusal route later and reports the independent trajectory: sale notice, Kelm petition, and Senn's departure before formal testimony.

## Persistence and state ownership

The proof slice uses ordinary Endless Sky mission/global conditions only. It introduces no engine save schema and no generic A2-owned dialogue/world-state database.

Old saves therefore default to absence of all `A2 Broken Compact:*` conditions and should remain unaffected. This must still be verified by an actual save/load roundtrip before A3 acceptance.

The B2 character packet remains narrative authority for Kelm, Dorne, Senn, and the Broken Compact conflict. If a generalized named-character-memory system later becomes authoritative, these proof flags are migration inputs; they must not remain a competing parallel truth source.

## Files

- `data/human/a2 broken compact.txt`
- `tools/story/validate_a2_broken_compact.py`

## Focused validator

`tools/story/validate_a2_broken_compact.py` checks:

- all four mission blocks exist;
- Kelm, Dorne, Senn, and Morrow Line are present;
- the Republic reputation input exists;
- the player-visible special-response label exists;
- all four first-hearing routes exist;
- all three evidence-hearing settlement writes exist;
- evidence, trust, and later-reader persistent states exist;
- settlement/refusal state is actually consumed by later readers;
- obvious generic A2 shadow-state/database patterns are absent.

## Validation actually observed this run

- Live GitHub repository metadata confirmed `Wiredshark/star` and push/admin access.
- Live compare confirmed base `c6cb81fe47d00c25df9a3947db83eb930f872f35` and candidate `f08482ca790618f686fd31a5a5c4801d4e607eb2` are related by exactly 2 forward commits, with only the two intended files changed.
- Live GitHub content reads confirmed both candidate files exist at the isolated branch.
- GitHub combined commit-status query for `f08482ca790618f686fd31a5a5c4801d4e607eb2` returned no statuses.

Not run, and therefore not claimed:

- `python3 tools/story/validate_a2_broken_compact.py`
- Endless Sky content parser / full build
- stock conversation regression suite
- actual-game mission/dialogue runtime
- save/load roundtrip
- visual proof (no UI implementation is changed, so screenshot proof is not expected unless runtime reveals a presentation issue)

The exposed private execution connector in this run is the Fallout renderer host and its exact-ref runnable harness; it is not evidence of a `Wiredshark/star` checkout/build environment. It was therefore not misused to fabricate Endless Sky execution evidence.

## Required A3 gates

Before integration, A3 should run and record:

1. `python3 tools/story/validate_a2_broken_compact.py`
2. the repository's authoritative story/data validators;
3. normal Endless Sky parser/build regressions;
4. actual-game exercise on New Washington proving all First Hearing routes;
5. Republic-reputation-gated response visibility using real player state;
6. all three Evidence Hearing settlement outcomes;
7. Later Reader and Refusal Reader behavior;
8. save before the first hearing, save after evidence, reload, and confirm no duplicate rewards/state reset;
9. stock conversation compatibility;
10. duplicate-state review against any integrated generalized named-character memory.

## A3 integration ordering

This A2 candidate depends narratively on the B2 Broken Compact character packet but does not require that documentation commit at runtime. For repository continuity, A3 should inspect PR #1 and this candidate together, resolve any wording/state-name changes once, and preserve a single character/history authority.

Do not integrate PR #2, PR #5, and this candidate simply because they are all A2. Each remains independently gated and should be selected according to A3's integration policy and current portfolio balance.

## Acceptance summary

The slice materially advances A2 beyond the existing Imani Rook and reactive-news candidates by adding a persistent named-character relationship/legal conflict with evidence discovery, state-gated dialogue, mutually exclusive settlement consequences, and later readers. It is structurally suitable for runtime validation but remains **PARTIAL** until the unexecuted repository/runtime/save gates pass.
