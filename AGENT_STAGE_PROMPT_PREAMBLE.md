# Canonical Agent Stage-Prompt Preamble

Every generated or manually authored A/B/C/D stage prompt should include this requirement or explicitly state that it inherits it.

> Read `AGENT_BUILD_LOOP_POLICY.md` before selecting discretionary work. Recover the recent domain labels for this lane and materially overlapping adjacent lanes. Do not treat the lane name itself as the work domain. Classify the actual subsystem/content/visual/test/tooling area being advanced. Fix reproducible blockers and regressions first even when that repeats a domain, but label the repeat and preserve concentration debt. Otherwise prefer an underrepresented high-value domain and a cross-system connection over another iteration of the currently dominant subsystem.
>
> The A loop also has an explicit user-priority dialogue target in `A_LOOP_DIALOGUE_SYSTEM.md`. A2/A3 must inspect it before selecting discretionary RPG/integration work. Until A3 records `DIALOGUE_SYSTEM_STATUS: INTEGRATED_PRODUCTION_SLICE`, carry the priority forward and either advance it or record the concrete blocker/dependency that prevented advancement. Do not satisfy it with planning, parser-only scaffolding, or UI-only polish; the acceptance target requires a tested production conversation using real persistent state and producing a later persistent consequence/reader.
>
> Record these fields in the run report and handoff:
>
> `LOOP_ID`
>
> `RUN_TYPE`
>
> `PRIMARY_DOMAIN`
>
> `SECONDARY_DOMAINS`
>
> `RECENT_DOMAIN_WINDOW`
>
> `DIVERSITY_STATUS`
>
> `CONCENTRATION_JUSTIFICATION`
>
> `NEGLECTED_AREA_ADVANCED`
>
> `CROSS_SYSTEM_CONNECTION`
>
> `DIVERSITY_CHECK`
>
> If this is A2 or A3 while the dialogue priority is open, also record `DIALOGUE_SYSTEM_STATUS` and `DIALOGUE_SYSTEM_NEXT_GAP`.
>
> If this is A3 integration, also record `PORTFOLIO_BALANCE`. If this is D1 or D4, explicitly report unresolved concentration debt. If this is D2, preserve broad cross-system regression coverage rather than testing only the newest subsystem.

## Prompt-author rule

A stage prompt may specialize the allowed domain list for its lane, but it must not delete the anti-funneling gate, the mandatory-repeat exception, the open explicit-user-priority dialogue requirement, or the run labels above.

A prompt that asks an agent to complete "one isolated stage" still requires domain selection inside that specialty. For example:

- A1 chooses a specific simulation domain rather than repeatedly choosing economy/freight; for dialogue it exposes/reuses authoritative world-state inputs only when needed.
- A2 chooses a specific RPG/narrative domain rather than repeatedly choosing freight crises; while the dialogue priority is open, it owns the reusable implementation plus production consumer described in `A_LOOP_DIALOGUE_SYSTEM.md`.
- A3 integrates exact specialist work and must not declare the dialogue priority satisfied before the production acceptance gate is met.
- B1/B2/B3 vary regions, institutions, character roles, conflicts, and content structures.
- C1/C2/C3/C4 vary visual categories when proof/repair blockers do not force a repeat.
- D1/D2/D3/D4 vary architecture surfaces, QA scenarios, tooling targets, and verification concerns while preserving required regression gates.

## Handoff rule

The next agent should treat missing diversity labels as an incomplete handoff for discretionary work. Missing labels do not block an urgent reproducible repair, but the receiving agent must reconstruct the labels before closing the run.

While the dialogue priority remains open, an A2/A3 handoff that omits `DIALOGUE_SYSTEM_STATUS` or silently drops `A_LOOP_DIALOGUE_SYSTEM.md` is also incomplete. A genuine blocker is acceptable only when recorded with exact evidence and a next-gap statement.

The purpose is not random rotation. The purpose is to prevent local success in one system from silently becoming the entire development roadmap while ensuring explicit user-priority systems are not lost between autonomous rounds.
