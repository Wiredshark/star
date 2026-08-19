#!/usr/bin/env python3
"""Contract test for A1 Republic displacement -> Southern Rim transit load."""

from pathlib import Path
import sys

DATA_PATH = Path("data/human/a1 republic displacement transit load.txt")


def require(text: str, snippet: str) -> None:
    if snippet not in text:
        raise AssertionError(f"missing required production-data snippet: {snippet!r}")


def apply_crossing(displacement: int, congestion: int, latched: bool) -> tuple[int, bool, bool]:
    """Mirror the production contract for one qualifying border crossing."""
    if displacement < 4 or congestion >= 6 or latched:
        return congestion, latched, False
    return min(6, congestion + 1), True, True


def apply_decay(congestion: int) -> int:
    return max(0, congestion - 1)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DATA_PATH
    text = path.read_text(encoding="utf-8")

    for snippet in (
        'event "ES A1: Republic Displacement Routing Load Ends"',
        '\tclear "world: republic displacement routing load"',
        'mission "ES A1: Republic Displacement Transit Load"',
        '\tentering',
        '\tnon-blocking',
        '\trepeat',
        '\t\tgovernment "Free Worlds"',
        '\t\tneighbor government "Republic"',
        '\t\thas "previous system government: Republic"',
        '\t\t"world: republic displacement pressure" >= 4',
        '\t\tnot "world: republic displacement routing load"',
        '\t\t"world: southern rim transit congestion" < 6',
        '\t\t"world: southern rim transit congestion" += 1',
        '\t\t"world: southern rim transit congestion" <?= 6',
        '\t\tevent "ES A1: Southern Rim Transit Congestion Decay" 3 3',
        '\t\tevent "ES A1: Republic Displacement Routing Load Ends" 4 4',
    ):
        require(text, snippet)

    # Below-threshold displacement does not create transit pressure.
    congestion, latched, scheduled = apply_crossing(3, 2, False)
    assert (congestion, latched, scheduled) == (2, False, False)

    # Acute displacement contributes one bounded unit and latches the source.
    congestion, latched, scheduled = apply_crossing(4, 2, False)
    assert (congestion, latched, scheduled) == (3, True, True)

    # Repeated crossings during the latch cannot stack additional pressure.
    for _ in range(20):
        congestion, latched, scheduled = apply_crossing(6, congestion, latched)
        assert not scheduled
        assert congestion == 3

    # Once the latch expires, repeated crisis crossings saturate at six, never above.
    trace = []
    scheduled_count = 0
    for _ in range(8):
        latched = False
        congestion, latched, scheduled = apply_crossing(6, congestion, latched)
        scheduled_count += int(scheduled)
        trace.append(congestion)
    assert trace == [4, 5, 6, 6, 6, 6, 6, 6], trace
    assert scheduled_count == 3, scheduled_count

    # Each accepted contribution has one matching decay; stale decays cannot underflow.
    for _ in range(scheduled_count + 10):
        congestion = apply_decay(congestion)
    assert congestion == 0

    print("PASS: Republic displacement transit load is thresholded, latched, bounded, and self-recovering")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
