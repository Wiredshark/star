#!/usr/bin/env python3
"""Run all focused fork story validators with one deterministic command.

This runner intentionally executes each validator as its own process. That keeps
legacy validators isolated from one another, preserves their existing default
CLI behavior, and makes the failing script obvious in CI output.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
STORY_TOOLS = ROOT / "tools" / "story"
EXTRA_CHECKS = (STORY_TOOLS / "test_b2_character_packets.py",)


def discover() -> list[Path]:
    validators = sorted(STORY_TOOLS.glob("validate_*.py"))
    checks = validators + [path for path in EXTRA_CHECKS if path.is_file()]
    return checks


def run_one(path: Path) -> tuple[bool, float, str]:
    started = time.monotonic()
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    elapsed = time.monotonic() - started
    return result.returncode == 0, elapsed, result.stdout.rstrip()


def main() -> int:
    checks = discover()
    if not checks:
        print("FAIL: no focused story validators discovered")
        return 1

    failures: list[str] = []
    print(f"Focused story validation: discovered {len(checks)} checks")

    for path in checks:
        relative = path.relative_to(ROOT).as_posix()
        ok, elapsed, output = run_one(path)
        status = "PASS" if ok else "FAIL"
        print(f"\n[{status}] {relative} ({elapsed:.2f}s)")
        if output:
            print(output)
        if not ok:
            failures.append(relative)

    print("\nFocused story validation summary")
    print(f"checks={len(checks)}")
    print(f"passed={len(checks) - len(failures)}")
    print(f"failed={len(failures)}")

    if failures:
        print("failing_checks:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
