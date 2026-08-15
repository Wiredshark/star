#!/usr/bin/env python3
"""Exact-head in-game asset proof harness for the Endless Sky remaster pipeline.

The harness prevents a pre-commit or stale screenshot from being accepted as proof for
an asset at a later commit. A proof session is tied to a clean Git HEAD, a committed
candidate blob, a fresh capture directory, and hashes of all produced screenshots.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time
import uuid
from typing import Any, Iterable

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
RECEIPT_VERSION = 1


class VerificationError(RuntimeError):
    pass


def run(cmd: list[str], cwd: Path, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = run(["git", *args], repo)
    if check and result.returncode:
        raise VerificationError(result.stderr.strip() or result.stdout.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def normalize_rel(repo: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(repo.resolve()).as_posix()
    except ValueError as exc:
        raise VerificationError(f"candidate must be inside repository: {path}") from exc


def tracked_blob(repo: Path, rel: str, commit: str) -> str:
    entry = git(repo, "ls-tree", commit, "--", rel)
    if not entry:
        raise VerificationError(f"candidate is not tracked at {commit}: {rel}")
    parts = entry.split()
    if len(parts) < 3 or parts[1] != "blob":
        raise VerificationError(f"candidate is not a regular tracked blob at {commit}: {rel}")
    return parts[2]


def require_clean(repo: Path) -> str:
    # Ignore ignored build/evidence products; tracked or untracked non-ignored files make
    # exact-head proof ambiguous and are refused.
    status = git(repo, "status", "--porcelain", "--untracked-files=normal")
    if status:
        raise VerificationError("working tree is not clean; commit/stash/remove changes before proof:\n" + status)
    return status


def candidate_attestation(repo: Path, candidate: Path, head: str) -> dict[str, Any]:
    rel = normalize_rel(repo, candidate)
    if not candidate.is_file():
        raise VerificationError(f"candidate file is missing: {candidate}")
    blob = tracked_blob(repo, rel, head)
    working_blob = git(repo, "hash-object", "--", rel)
    if working_blob != blob:
        raise VerificationError(
            f"candidate bytes do not match HEAD {head}: expected blob {blob}, working blob {working_blob}"
        )
    return {
        "path": rel,
        "git_blob": blob,
        "sha256": sha256_file(candidate),
        "size": candidate.stat().st_size,
    }


def parse_command(value: str) -> list[str]:
    parsed = shlex.split(value)
    if not parsed:
        raise VerificationError("empty command")
    return parsed


def png_info(path: Path, session_start_ns: int) -> dict[str, Any]:
    stat = path.stat()
    if stat.st_size < 33:
        raise VerificationError(f"screenshot is too small to be a valid PNG: {path}")
    with path.open("rb") as handle:
        header = handle.read(24)
    if not header.startswith(PNG_SIGNATURE):
        raise VerificationError(f"screenshot is not a PNG: {path}")
    if stat.st_mtime_ns < session_start_ns:
        raise VerificationError(f"screenshot predates this proof session: {path}")
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if width <= 0 or height <= 0:
        raise VerificationError(f"screenshot has invalid dimensions: {path}")
    return {
        "path": path.name,
        "sha256": sha256_file(path),
        "size": stat.st_size,
        "width": width,
        "height": height,
        "mtime_ns": stat.st_mtime_ns,
    }


def run_command(
    label: str,
    command: list[str],
    repo: Path,
    env: dict[str, str],
    timeout: int,
) -> dict[str, Any]:
    started = time.time_ns()
    try:
        result = subprocess.run(
            command,
            cwd=repo,
            env=env,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        raise VerificationError(f"{label} command timed out after {timeout}s") from exc
    ended = time.time_ns()
    record = {
        "argv": command,
        "returncode": result.returncode,
        "started_ns": started,
        "ended_ns": ended,
        "stdout_sha256": sha256_text(result.stdout),
        "stderr_sha256": sha256_text(result.stderr),
        "stdout_tail": result.stdout[-4000:],
        "stderr_tail": result.stderr[-4000:],
    }
    if result.returncode:
        raise VerificationError(
            f"{label} command failed with exit {result.returncode}:\n{result.stderr[-2000:] or result.stdout[-2000:]}"
        )
    return record


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def receipt_core(receipt: dict[str, Any]) -> dict[str, Any]:
    core = dict(receipt)
    core.pop("receipt_sha256", None)
    return core


def receipt_digest(receipt: dict[str, Any]) -> str:
    canonical = json.dumps(receipt_core(receipt), sort_keys=True, separators=(",", ":"))
    return sha256_text(canonical)


def cmd_capture(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    if not (repo / ".git").exists() and not git(repo, "rev-parse", "--git-dir", check=False):
        raise VerificationError(f"not a Git repository: {repo}")

    head = git(repo, "rev-parse", "HEAD")
    branch = git(repo, "branch", "--show-current", check=False)
    require_clean(repo)
    candidate = candidate_attestation(repo, (repo / args.candidate).resolve(), head)

    evidence_root = Path(args.evidence_root).resolve()
    evidence_root.mkdir(parents=True, exist_ok=True)
    run_id = f"{head[:12]}-{int(time.time())}-{uuid.uuid4().hex[:8]}"
    run_dir = evidence_root / run_id
    run_dir.mkdir(parents=False, exist_ok=False)
    capture_dir = run_dir / "captures"
    capture_dir.mkdir()

    nonce = uuid.uuid4().hex
    session_start_ns = time.time_ns()
    env = os.environ.copy()
    env.update(
        {
            "ASSET_VERIFY_RUN_ID": run_id,
            "ASSET_VERIFY_NONCE": nonce,
            "ASSET_VERIFY_HEAD": head,
            "ASSET_VERIFY_BRANCH": branch,
            "ASSET_VERIFY_ASSET_ID": args.asset_id,
            "ASSET_VERIFY_CANDIDATE": candidate["path"],
            "ASSET_VERIFY_CANDIDATE_SHA256": candidate["sha256"],
            "ASSET_VERIFY_CAPTURE_DIR": str(capture_dir),
            "ASSET_VERIFY_SCENE_ID": args.scene_id,
        }
    )

    receipt: dict[str, Any] = {
        "schema": "endless-sky.asset-proof",
        "version": RECEIPT_VERSION,
        "status": "IN_PROGRESS",
        "run_id": run_id,
        "nonce": nonce,
        "repo_head": head,
        "branch": branch,
        "asset_id": args.asset_id,
        "scene_id": args.scene_id,
        "candidate": candidate,
        "session_start_ns": session_start_ns,
        "prepare": None,
        "capture": None,
        "binary": None,
        "screenshots": [],
        "worktree_clean_before": True,
        "worktree_clean_after": False,
        "acceptance": {"status": "PROOF_REQUIRED", "reasons": ["capture not completed"]},
    }
    atomic_json(run_dir / "receipt.json", receipt)

    if args.prepare_command:
        receipt["prepare"] = run_command(
            "prepare", parse_command(args.prepare_command), repo, env, args.timeout
        )
        require_clean(repo)

    if args.binary:
        binary = (repo / args.binary).resolve() if not Path(args.binary).is_absolute() else Path(args.binary).resolve()
        if not binary.is_file():
            raise VerificationError(f"binary file is missing: {binary}")
        receipt["binary"] = {
            "path": str(binary),
            "sha256": sha256_file(binary),
            "size": binary.stat().st_size,
            "mtime_ns": binary.stat().st_mtime_ns,
        }

    receipt["capture"] = run_command(
        "capture", parse_command(args.capture_command), repo, env, args.timeout
    )

    require_clean(repo)
    end_head = git(repo, "rev-parse", "HEAD")
    if end_head != head:
        raise VerificationError(f"HEAD changed during proof session: {head} -> {end_head}")
    # Re-attest after capture to catch any candidate mutation that was subsequently hidden.
    after_candidate = candidate_attestation(repo, (repo / args.candidate).resolve(), head)
    if after_candidate != candidate:
        raise VerificationError("candidate changed during proof session")

    screenshots: list[dict[str, Any]] = []
    for path in sorted(capture_dir.glob("*.png")):
        screenshots.append(png_info(path, session_start_ns))
    if not screenshots:
        raise VerificationError(
            "capture command succeeded but produced no fresh PNG in ASSET_VERIFY_CAPTURE_DIR"
        )

    receipt["screenshots"] = screenshots
    receipt["session_end_ns"] = time.time_ns()
    receipt["worktree_clean_after"] = True
    receipt["status"] = "PASS"
    receipt["acceptance"] = {
        "status": "PROOF_VERIFIED",
        "reasons": [
            "clean exact HEAD held for the full session",
            "candidate bytes matched the committed Git blob before and after capture",
            "capture command completed successfully",
            "at least one fresh PNG was created during this session",
        ],
    }
    receipt["receipt_sha256"] = receipt_digest(receipt)
    atomic_json(run_dir / "receipt.json", receipt)

    latest = evidence_root / "LATEST"
    latest.write_text(run_id + "\n", encoding="utf-8")
    print(f"PASS {args.asset_id} {head} {run_dir / 'receipt.json'}")
    return 0


def verify_screenshot(run_dir: Path, record: dict[str, Any]) -> None:
    path = run_dir / "captures" / record["path"]
    if not path.is_file():
        raise VerificationError(f"recorded screenshot is missing: {path}")
    if sha256_file(path) != record["sha256"]:
        raise VerificationError(f"screenshot hash mismatch: {path}")
    with path.open("rb") as handle:
        header = handle.read(24)
    if not header.startswith(PNG_SIGNATURE):
        raise VerificationError(f"recorded screenshot is not a PNG: {path}")
    if int.from_bytes(header[16:20], "big") != record["width"] or int.from_bytes(header[20:24], "big") != record["height"]:
        raise VerificationError(f"screenshot dimensions changed: {path}")


def cmd_verify(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    receipt_path = Path(args.receipt).resolve()
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt.get("schema") != "endless-sky.asset-proof" or receipt.get("version") != RECEIPT_VERSION:
        raise VerificationError("unsupported receipt schema/version")
    if receipt.get("status") != "PASS" or receipt.get("acceptance", {}).get("status") != "PROOF_VERIFIED":
        raise VerificationError("receipt is not a completed passing proof")
    expected_digest = receipt_digest(receipt)
    if receipt.get("receipt_sha256") != expected_digest:
        raise VerificationError("receipt integrity hash mismatch")

    proof_head = receipt["repo_head"]
    git(repo, "cat-file", "-e", f"{proof_head}^{{commit}}")
    if args.require_current_head:
        current_head = git(repo, "rev-parse", "HEAD")
        if current_head != proof_head:
            raise VerificationError(
                f"proof is stale for current HEAD: receipt={proof_head}, current={current_head}"
            )

    candidate = receipt["candidate"]
    if tracked_blob(repo, candidate["path"], proof_head) != candidate["git_blob"]:
        raise VerificationError("candidate Git blob does not match receipt")
    committed_bytes = subprocess.run(
        ["git", "show", f"{proof_head}:{candidate['path']}"], cwd=repo, capture_output=True
    )
    if committed_bytes.returncode:
        raise VerificationError("unable to read candidate bytes from proof commit")
    if hashlib.sha256(committed_bytes.stdout).hexdigest() != candidate["sha256"]:
        raise VerificationError("candidate SHA-256 does not match proof commit")

    run_dir = receipt_path.parent
    screenshots = receipt.get("screenshots", [])
    if not screenshots:
        raise VerificationError("receipt has no screenshots")
    for record in screenshots:
        verify_screenshot(run_dir, record)

    print(f"PASS {receipt['asset_id']} {proof_head} screenshots={len(screenshots)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    capture = sub.add_parser("capture", help="run a fresh exact-head capture and emit a proof receipt")
    capture.add_argument("--repo", default=".")
    capture.add_argument("--asset-id", required=True)
    capture.add_argument("--candidate", required=True, help="candidate path relative to repository root")
    capture.add_argument("--scene-id", required=True, help="stable scene/fixture identifier")
    capture.add_argument("--prepare-command", help="optional build/staging command executed first")
    capture.add_argument("--capture-command", required=True, help="command that launches/captures the actual game")
    capture.add_argument("--binary", help="optional built executable to hash into the receipt")
    capture.add_argument("--evidence-root", default="../asset-proof-evidence", help="must be outside Git worktree unless ignored")
    capture.add_argument("--timeout", type=int, default=600)
    capture.set_defaults(func=cmd_capture)

    verify = sub.add_parser("verify", help="verify an existing receipt and its evidence")
    verify.add_argument("--repo", default=".")
    verify.add_argument("--receipt", required=True)
    verify.add_argument("--require-current-head", action="store_true", default=False)
    verify.set_defaults(func=cmd_verify)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except VerificationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
