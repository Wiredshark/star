from collections import defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "data"

TOP_LEVEL_RE = re.compile(r'^(?:mission|event|news|conversation|phrase|fleet|government|planet|system|ship|outfit)\b')
POSITIVE_WRITE_RE = re.compile(r'^\s*"(world: [^"]+)"\s*(\+=|\+\+)\s*(\d+)?\s*$')
CAP_RE_TEMPLATE = r'^\s*"{state}"\s*<\?=\s*(-?\d+(?:\.\d+)?)\s*$'
SCHEDULED_EVENT_RE = re.compile(r'^\s*event\s+"([^"]+)"(?:\s+\d+(?:\s+\d+)?)?\s*$')
NEGATIVE_WRITE_RE = re.compile(r'^\s*"(world: [^"]+)"\s*(?:-=|--)')


def a1_data_files():
    return sorted(
        path
        for path in DATA_ROOT.rglob("*.txt")
        if path.name.lower().startswith("a1 ")
    )


def top_level_blocks(text):
    """Yield `(kind, header, lines)` for top-level mission and event blocks."""
    lines = text.splitlines()
    start = None
    kind = None

    for index, line in enumerate(lines):
        is_target = line.startswith('mission "') or line.startswith('event "')
        if is_target:
            if start is not None:
                yield kind, lines[start].strip(), lines[start:index]
            start = index
            kind = "mission" if line.startswith('mission "') else "event"
            continue

        if start is not None and line and not line[0].isspace() and TOP_LEVEL_RE.match(line):
            yield kind, lines[start].strip(), lines[start:index]
            start = None
            kind = None

    if start is not None:
        yield kind, lines[start].strip(), lines[start:]


def event_name(header):
    match = re.match(r'^event\s+"([^"]+)"$', header)
    return match.group(1) if match else None


def event_negative_writes():
    mapping = defaultdict(set)
    provenance = {}
    for path in a1_data_files():
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for kind, header, block in top_level_blocks(text):
            if kind != "event":
                continue
            name = event_name(header)
            if not name:
                continue
            provenance[name] = (relative, header)
            for line in block:
                match = NEGATIVE_WRITE_RE.match(line)
                if match:
                    mapping[name].add(match.group(1))
    return mapping, provenance


def mission_positive_writes():
    results = []
    for path in a1_data_files():
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for kind, header, block in top_level_blocks(text):
            if kind != "mission":
                continue
            for line in block:
                match = POSITIVE_WRITE_RE.match(line)
                if match:
                    operator = match.group(2)
                    amount = int(match.group(3) or 1) if operator == "+=" else 1
                    results.append((relative, header, block, match.group(1), amount))
    return results


def caps_for_state(block, state):
    pattern = re.compile(CAP_RE_TEMPLATE.format(state=re.escape(state)))
    return [float(match.group(1)) for line in block if (match := pattern.match(line))]


def scheduled_events(block):
    return [match.group(1) for line in block if (match := SCHEDULED_EVENT_RE.match(line))]


def test_numeric_positive_writers_are_locally_capped():
    writers = mission_positive_writes()
    assert writers, "no positive numeric A1 world-state writers discovered"

    failures = []
    for relative, header, block, state, amount in writers:
        caps = caps_for_state(block, state)
        if not caps:
            failures.append((relative, header, state, amount, "missing local <?= cap"))
            continue
        if max(caps) < amount:
            failures.append((relative, header, state, amount, f"cap {max(caps)} below increment"))

    assert not failures, f"unbounded A1 positive numeric writers: {failures}"


def test_numeric_positive_writers_schedule_matching_negative_recovery():
    negative_by_event, event_provenance = event_negative_writes()
    writers = mission_positive_writes()

    failures = []
    for relative, header, block, state, amount in writers:
        events = scheduled_events(block)
        matching = [name for name in events if state in negative_by_event.get(name, set())]
        if not matching:
            failures.append(
                {
                    "file": relative,
                    "mission": header,
                    "state": state,
                    "increment": amount,
                    "scheduled_events": events,
                }
            )

    assert not failures, (
        "A1 positive numeric writers without a scheduled event that negatively "
        f"recovers the same state: {failures}"
    )


def test_shared_recovery_events_resolve_to_real_a1_event_definitions():
    negative_by_event, event_provenance = event_negative_writes()
    referenced_recovery_events = set()

    for _, _, block, state, _ in mission_positive_writes():
        for name in scheduled_events(block):
            if state in negative_by_event.get(name, set()):
                referenced_recovery_events.add(name)

    assert referenced_recovery_events, "no matched A1 recovery events were discovered"
    missing = sorted(name for name in referenced_recovery_events if name not in event_provenance)
    assert not missing, f"matched recovery events lack A1 definitions: {missing}"


def test_recovery_events_only_decrease_or_clamp_their_recovered_numeric_state():
    """Guard against a nominal recovery event secretly adding the same pressure back."""
    negative_by_event, _ = event_negative_writes()
    positive_event_write = re.compile(r'^\s*"(world: [^"]+)"\s*(?:\+=|\+\+)')
    failures = []

    for path in a1_data_files():
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for kind, header, block in top_level_blocks(text):
            if kind != "event":
                continue
            name = event_name(header)
            recovered = negative_by_event.get(name, set())
            if not recovered:
                continue
            for line in block:
                match = positive_event_write.match(line)
                if match and match.group(1) in recovered:
                    failures.append((relative, header, match.group(1), line.strip()))

    assert not failures, f"recovery events re-amplify their own numeric state: {failures}"
