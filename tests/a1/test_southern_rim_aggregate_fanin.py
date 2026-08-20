from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
FILES = {
    "patrol": ROOT / "data/human/a1 free worlds patrol transit load.txt",
    "maintenance": ROOT / "data/human/a1 syndicate maintenance transit spillover.txt",
    "customs": ROOT / "data/human/a1 republic customs transit spillover.txt",
    "displacement": ROOT / "data/human/a1 republic displacement transit load.txt",
}
CAP = 6


def writes(text, state):
    return bool(re.search(
        rf'^\s*"{re.escape(state)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        text,
        re.M,
    ))


def add(congestion):
    if congestion >= CAP:
        return congestion, False
    return min(CAP, congestion + 1), True


def decay(congestion):
    return max(0, congestion - 1)


def test_all_fan_in_sources_preserve_upstream_authority():
    text = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}
    assert not writes(text["patrol"], "world: free worlds patrol surge")
    assert not writes(text["maintenance"], "world: syndicate maintenance backlog")
    assert not writes(text["customs"], "world: republic customs scrutiny")
    assert not writes(text["displacement"], "world: republic displacement pressure")
    for body in text.values():
        assert '"world: southern rim transit congestion" <?= 6' in body
        assert 'event "ES A1: Southern Rim Transit Congestion Decay" 3 3' in body


def simulate(days):
    congestion = 0
    latches = {"patrol": 0, "maintenance": 0, "customs": 0, "displacement": 0}
    recovery_due = []
    trace = []
    accepted = 0

    for day in range(days):
        for _ in range(recovery_due.count(day)):
            congestion = decay(congestion)
        recovery_due = [due for due in recovery_due if due > day]

        phase = day % 240
        patrol = phase < 70
        maintenance = phase < 90
        scrutiny = 5 if phase < 80 else 1
        displacement = 5 if phase < 100 else 1

        # Representative qualifying border crossing every two days. Producers are
        # applied sequentially to model the shared cap conservatively.
        if day % 2 == 0:
            conditions = {
                "patrol": patrol,
                "maintenance": maintenance,
                "customs": scrutiny >= 3,
                "displacement": displacement >= 4,
            }
            latch_lengths = {"patrol": 2, "maintenance": 6, "customs": 2, "displacement": 4}
            for name in ("patrol", "maintenance", "customs", "displacement"):
                if conditions[name] and latches[name] == 0:
                    congestion, added = add(congestion)
                    if added:
                        accepted += 1
                        recovery_due.append(day + 3)
                        latches[name] = latch_lengths[name]

        for name in latches:
            latches[name] = max(0, latches[name] - 1)
        assert 0 <= congestion <= CAP
        trace.append((congestion, tuple(latches.values())))

    return trace, congestion, recovery_due, accepted


def test_four_source_three_year_fan_in_is_bounded_deterministic_and_recovers():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    assert first[3] == second[3]
    assert first[3] > 0

    congestion = first[1]
    recovery_due = list(first[2])
    day = 365 * 3
    while recovery_due:
        for _ in range(recovery_due.count(day)):
            congestion = decay(congestion)
        recovery_due = [due for due in recovery_due if due > day]
        day += 1
    for _ in range(12):
        congestion = decay(congestion)
    assert congestion == 0


if __name__ == "__main__":
    test_all_fan_in_sources_preserve_upstream_authority()
    test_four_source_three_year_fan_in_is_bounded_deterministic_and_recovers()
    print("A1 Southern Rim aggregate fan-in contract: PASS")
