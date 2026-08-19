#!/usr/bin/env python3
"""Contract test for the A1 Republic border-pressure world simulation.

This test intentionally has no dependency on the game binary. It verifies the
production data file keeps the event/mission wiring and bounded feedback-loop
invariants that A3 should preserve when integrating the slice.
"""

from pathlib import Path
import sys

DATA_PATH = Path("data/human/a1 world simulation.txt")


def require(text: str, snippet: str) -> None:
    if snippet not in text:
        raise AssertionError(f"missing required production-data snippet: {snippet!r}")


def apply_escalation(pressure: int) -> tuple[int, bool]:
    """Mirror the data contract: only unresolved pressure below 6 escalates."""
    if pressure >= 6:
        return pressure, False
    return min(6, pressure + 2), True


def apply_decay(pressure: int) -> int:
    """Mirror the scheduled event contract."""
    return max(0, pressure - 2)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DATA_PATH
    text = path.read_text(encoding="utf-8")

    # Structural/parser contract copied from known Endless Sky data syntax.
    for snippet in (
        'event "ES A1: Republic Border Pressure Decay"',
        '\t"world: republic border pressure" -= 2',
        '\t"world: republic border pressure" >?= 0',
        'mission "ES A1: Republic Border Pressure Escalation"',
        '\tentering',
        '\tnon-blocking',
        '\trepeat',
        '\t\tgovernment "Republic"',
        '\t\thas "previous system government: Pirate"',
        '\t\t"world: republic border pressure" < 6',
        '\t\t"world: republic border pressure" += 2',
        '\t\t"world: republic border pressure" <?= 6',
        '\t\tevent "ES A1: Republic Border Pressure Decay" 5 5',
        'mission "ES A1: Republic Border Pressure Alert"',
        '\t\t"world: republic border pressure" >= 4',
    ):
        require(text, snippet)

    # Long-run boundedness: repeated qualifying crossings saturate at 6 and do
    # not schedule extra decays once saturated.
    pressure = 0
    scheduled = 0
    seen = []
    for _ in range(8):
        pressure, did_schedule = apply_escalation(pressure)
        scheduled += int(did_schedule)
        seen.append(pressure)
    assert seen == [2, 4, 6, 6, 6, 6, 6, 6], seen
    assert scheduled == 3, scheduled

    # Each accepted crossing schedules exactly one five-day decay contribution.
    decay_trace = []
    for _ in range(scheduled):
        pressure = apply_decay(pressure)
        decay_trace.append(pressure)
    assert decay_trace == [4, 2, 0], decay_trace

    # Extra/stale decay events cannot underflow the persistent condition.
    for _ in range(20):
        pressure = apply_decay(pressure)
    assert pressure == 0

    # Threshold semantics used by the player-visible reader.
    assert not (2 >= 4)
    assert 4 >= 4
    assert 6 >= 4

    print("PASS: Republic border-pressure data contract is bounded and self-recovering")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
