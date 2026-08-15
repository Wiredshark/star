# Asset Verification Handoff

## Purpose

This is the mandatory C2/C3/C4 proof path for remastered Endless Sky assets. It closes the failure mode where a valid-looking screenshot is captured before the final asset commit and is then incorrectly reused as proof for a newer HEAD.

**Rule:** an asset may not become `ACCEPTED_2026` unless `tools/asset_verification/verify_asset.py capture` completes at the exact commit being accepted and the resulting receipt later passes `verify --require-current-head` on that same commit.

## What the verifier proves

A passing receipt proves all of the following mechanically:

1. The Git worktree was clean at capture start and remained clean.
2. The candidate file was tracked at the exact starting `HEAD`.
3. Candidate bytes matched the committed Git blob before and after the game capture.
4. The optional build/preparation step completed successfully without changing tracked files.
5. The actual capture command completed successfully.
6. At least one **fresh PNG created after the verification session began** exists in the new capture directory.
7. The receipt records hashes for the candidate, optional game binary, every screenshot, command output, exact HEAD, scene ID, and a unique nonce/run ID.
8. A later C4 verification detects screenshot tampering or use of a receipt from an older/newer commit.

The verifier does **not** decide whether the art is visually good. C4 still performs visual/style/registration review of the recorded screenshots. It prevents stale or unbound evidence from being counted as proof.

## C2/C3: create exact-head proof

Commit the candidate first. Do not capture before the candidate commit.

From a clean checkout of the candidate commit:

```bash
python3 tools/asset_verification/verify_asset.py capture \
  --asset-id "<stable asset id>" \
  --candidate "images/<candidate path>.png" \
  --scene-id "<stable fixture/scene id>" \
  --prepare-command "<project build/staging command>" \
  --capture-command "<actual-game launch/capture harness command>" \
  --binary "<path to built Endless Sky executable>" \
  --evidence-root "../asset-proof-evidence"
```

The capture harness receives these environment variables and should use them instead of inventing its own proof path:

- `ASSET_VERIFY_RUN_ID`
- `ASSET_VERIFY_NONCE`
- `ASSET_VERIFY_HEAD`
- `ASSET_VERIFY_BRANCH`
- `ASSET_VERIFY_ASSET_ID`
- `ASSET_VERIFY_CANDIDATE`
- `ASSET_VERIFY_CANDIDATE_SHA256`
- `ASSET_VERIFY_CAPTURE_DIR`
- `ASSET_VERIFY_SCENE_ID`

**Required capture behavior:** launch the real game/build under test and save one or more final in-game screenshots directly as `*.png` inside `$ASSET_VERIFY_CAPTURE_DIR`. A successful command that only emits logs is a verification failure.

A successful run prints:

```text
PASS <asset-id> <exact-head-sha> <receipt-path>
```

The receipt's acceptance state will be `PROOF_VERIFIED`.

## C4: re-verify before acceptance

C4 must check out the exact candidate/integration commit and run:

```bash
python3 tools/asset_verification/verify_asset.py verify \
  --receipt "../asset-proof-evidence/<run-id>/receipt.json" \
  --require-current-head
```

Only a `PASS` result is eligible for visual acceptance. If the branch moved after capture, `--require-current-head` fails. Re-run the capture on the new commit; never carry a screenshot forward.

## Acceptance state machine

- Candidate generated but not committed: `PROOF_REQUIRED`
- Candidate committed but no exact-head receipt: `PROOF_REQUIRED`
- Capture command emits logs but zero PNGs: `PROOF_REQUIRED`
- Receipt exists but current HEAD differs: `PROOF_STALE`
- Receipt or screenshot hash mismatch: `PROOF_INVALID`
- Exact-head receipt passes machine verification: `PROOF_VERIFIED`
- C4 visually approves the `PROOF_VERIFIED` screenshot(s): eligible for `ACCEPTED_2026`

`PROOF_VERIFIED` is necessary but not sufficient for `ACCEPTED_2026`.

## Agent handoff requirements

Every C2/C3 handoff for an asset must include:

```text
ASSET_ID: <id>
CANDIDATE_PATH: <repo-relative path>
CANDIDATE_HEAD: <40-char SHA>
SCENE_ID: <scene/fixture>
PROOF_RUN_ID: <run id>
PROOF_RECEIPT: <receipt path>
PROOF_RECEIPT_SHA256: <receipt_sha256 from receipt>
PROOF_SCREENSHOTS: <filenames + sha256>
PROOF_STATUS: PROOF_VERIFIED | PROOF_REQUIRED
```

C4 must never infer proof from prose, logs, or an earlier screenshot. The receipt is the machine authority for commit/evidence binding; the screenshot is the visual authority for style/registration.

## Failure recovery

- **Dirty tree:** commit/stash/remove changes, then start a new proof run.
- **Candidate mismatch:** commit the final candidate and start a new proof run.
- **No screenshot:** fix the actual-game capture harness so it writes PNGs to `ASSET_VERIFY_CAPTURE_DIR`; logs alone do not count.
- **HEAD changed:** start a new proof run at the new HEAD.
- **Screenshot changed or missing:** the receipt is invalid; recapture.
- **Build changed tracked files:** fix the build/staging command. Exact-head verification must not mutate tracked source/assets.

## Tests

Run the verifier regression tests with:

```bash
python3 -m unittest tests/test_asset_verification.py -v
```

The tests cover a passing exact-head capture, dirty-worktree refusal, uncommitted candidate refusal, stale-proof rejection after a new commit, and screenshot-tamper rejection.
