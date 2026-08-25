# A2 Free Worlds Relief Policy News — Current-Main Hardening Handoff

Verdict: PARTIAL pending exact-head repository-native validation.

## Authority

- Authoritative repository: `Wiredshark/star`
- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-free-worlds-relief-policy-news-hardening-20260824-2305`
- Production hardening: `23ef05bcf17b8b50bbf1d086c0c5d76464a25518`
- Strengthened validator: `62cac4c4e951b15a844ebffad6af957adfa9996d`

## Scope

The Free Worlds Relief Policy News layer is already integrated on authoritative `main`. This branch does not duplicate the feature. It hardens the existing read-only downstream consumer to the current repository content/validation contract while preserving the six existing News outcomes and save-compatible upstream A2 condition names.

The six ambient outcomes remain:

- medical priority + clear backlog;
- medical priority + residual demand;
- throughput priority + clear backlog;
- throughput priority + residual demand;
- distributed routing + clear backlog;
- distributed routing + residual demand.

Every group continues to require `A2 Free Worlds Relief Coordination: followup seen` plus exactly one matching `Vale remembers ...` outcome. The refusal path remains deliberately private.

## Production hardening

`data/human/a2 free worlds relief policy news.txt` receives only the canonical 2026 Wiredshark/GPL content header and an explicit comment documenting refusal privacy. News names, conditions, messages, location scope, and player-facing semantics are unchanged.

## Validator hardening

`tools/story/validate_a2_free_worlds_relief_policy_news.py` now enforces:

- exactly six named News groups;
- exact one-to-one mapping from each News group to one `Vale remembers ...` outcome;
- `followup seen` exactly once in every group;
- exactly two upstream A2 gates per group: followup + matching outcome;
- Free Worlds-only location scope;
- required News name/message payloads;
- refusal and refusal-respected state never appear as public News gates;
- no mission, conversation, action, `world:*`, material, reputation, fleet, combat, navigation, or objective mutation tokens;
- no upstream or local persistent assignments;
- canonical GPL header and trailing newline.

## Ownership / persistence invariants

- `A2 Free Worlds Relief Coordination:*` remains read-only in this News layer.
- A1 remains sole writer of `world: free worlds relief demand`.
- This News layer writes no persistent state at all.
- Existing upstream condition names are preserved for save compatibility.
- Refusal remains private and is not reinterpreted as public authorization.
- No centralized Free Worlds relief authority is created by ambient reporting.

## Isolation / process boundary

This work is isolated from the current authoritative base and does not modify unrelated branches, open B2 work, or the actively unresolved Republic Border Testimony runtime slice. No destructive Git operation or self-integration is authorized.

## Validation boundary

Exact-head repository-native simulation/story/style and production build/save-load workflows must be terminal green before A3 review. Until then, this branch is PARTIAL.

## A3 instructions

If both exact-head workflows pass, A3 may review this hardening as the current-main replacement for historical PR #53. Do not integrate historical PR #53 together with this branch. Preserve the six exact outcome mappings, refusal privacy, Free Worlds-only scope, zero-persistent-write contract, and upstream A1/A2 read-only ownership.
