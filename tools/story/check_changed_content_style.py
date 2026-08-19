#!/usr/bin/env python3
"""Run Endless Sky content style checks only on changed fork A1/A2/B2 data.

The fork inherited a batch of pre-CI files without canonical copyright headers.
Blocking every PR on that historical debt would hide whether a new change is
clean. This wrapper makes the gate incremental: new or modified fork-authored
A/B data must pass the normal project style checker, while untouched debt can be
repaired separately.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
STYLE_CHECKER = ROOT / "utils" / "check_content_style.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="", help="base commit/ref for the diff")
    parser.add_argument("--head", default="HEAD", help="head commit/ref for the diff")
    return parser.parse_args()


def resolve_base(candidate: str, head: str) -> str:
    candidate = candidate.strip()
    if candidate and set(candidate) != {"0"}:
        return candidate
    result = subprocess.run(
        ["git", "rev-parse", f"{head}^"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        raise SystemExit(f"FAIL: unable to resolve fallback base for {head}: {result.stderr.strip()}")
    return result.stdout.strip()


def changed_paths(base: str, head: str) -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", base, head, "--", "data"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        raise SystemExit(f"FAIL: git diff failed: {result.stderr.strip()}")

    selected: list[Path] = []
    for raw in result.stdout.splitlines():
        relative = Path(raw)
        name = relative.name.lower()
        if (
            relative.suffix.lower() == ".txt"
            and name.startswith(("a1", "a2", "b2"))
            and (ROOT / relative).is_file()
        ):
            selected.append(relative)
    return sorted(set(selected))


def main() -> int:
    args = parse_args()
    head = args.head.strip() or "HEAD"
    base = resolve_base(args.base, head)
    files = changed_paths(base, head)

    print(f"Changed fork style range: {base}..{head}")
    if not files:
        print("PASS: no changed A1/A2/B2 data files require style validation")
        return 0

    print(f"Checking {len(files)} changed fork data file(s):")
    for path in files:
        print(f"- {path.as_posix()}")

    result = subprocess.run(
        [
            sys.executable,
            str(STYLE_CHECKER),
            "--no-correct",
            "--files",
            *(path.as_posix() for path in files),
        ],
        cwd=ROOT,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
