#!/usr/bin/env python3
"""Reject accepted-mission leakage from dialogue-only A2 conversations.

A conversation endpoint named `accept` is not a generic close button in Endless
Sky: PlayerInfo::MissionCallback moves the offered mission into the accepted
mission list. A2 conversations that only write persistent conditions and have no
mission objective must therefore terminate with `decline` after applying state.
"""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
MISSION = re.compile(r'^mission "(A2 [^"]+)"\s*$')

# Mission-level keys that indicate this is a real gameplay mission rather than a
# conversation-only state transition. Keep this deliberately broad so the guard
# does not ban legitimate future A2 missions from using the ACCEPT endpoint.
OBJECTIVE_PREFIXES = (
    "cargo ",
    "passengers ",
    "destination",
    "waypoint",
    "stopover",
    "npc",
    "timer",
    "deadline",
    "complete at",
    "to complete",
    "on accept",
    "on complete",
    "on enter",
    "on land",
    "boarding",
    "assisting",
)


def mission_blocks(text: str):
    lines = text.splitlines()
    current_name = None
    current: list[str] = []
    for line in lines:
        match = MISSION.match(line)
        if match:
            if current_name is not None:
                yield current_name, current
            current_name = match.group(1)
            current = [line]
        elif current_name is not None:
            # Any unindented non-comment data object ends the current mission.
            if line and not line.startswith(("\t", "#")):
                yield current_name, current
                current_name = None
                current = []
            else:
                current.append(line)
    if current_name is not None:
        yield current_name, current


def has_real_objective(lines: list[str]) -> bool:
    for line in lines:
        if not line.startswith("\t") or line.startswith("\t\t"):
            continue
        token = line.strip()
        if token in {"boarding", "assisting"}:
            return True
        if any(token.startswith(prefix) for prefix in OBJECTIVE_PREFIXES):
            return True
    return False


def main() -> int:
    offenders: list[str] = []
    checked = 0
    for path in sorted(DATA.rglob("a2 *.txt")):
        text = path.read_text(encoding="utf-8")
        for name, lines in mission_blocks(text):
            accepts = [line for line in lines if line.strip() == "accept"]
            if not accepts:
                continue
            checked += 1
            if not has_real_objective(lines):
                offenders.append(f"{path.relative_to(ROOT).as_posix()}: {name}")

    if offenders:
        print("FAIL: dialogue-only A2 missions terminate with `accept` and would remain in the accepted mission list:")
        for offender in offenders:
            print(f"- {offender}")
        return 1

    print(f"PASS: no dialogue-only A2 accepted-mission leakage (accepted A2 missions inspected={checked})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
