from collections import defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "data"

TOP_LEVEL_RE = re.compile(r'^(?:mission|event|news|conversation|phrase|fleet|government|planet|system|ship|outfit)\b')
HAS_WORLD_RE = re.compile(r'^\s*has\s+"(world: [^"]+)"\s*$')
POSITIVE_NUMERIC_READ_RE = re.compile(r'^\s*"(world: [^"]+)"\s*(?:>=|>)\s*-?\d+(?:\.\d+)?\s*$')
SET_WORLD_RE = re.compile(r'^\s*set\s+"(world: [^"]+)"\s*$')
POSITIVE_NUMERIC_WRITE_RE = re.compile(r'^\s*"(world: [^"]+)"\s*(?:\+=|\+\+)')


def a1_data_files():
    return sorted(
        path
        for path in DATA_ROOT.rglob("*.txt")
        if path.name.lower().startswith("a1 ")
    )


def mission_blocks(text):
    """Yield top-level mission blocks without interpreting Endless Sky syntax."""
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.startswith('mission "'):
            if start is not None:
                yield lines[start:index]
            start = index
            continue
        if start is not None and line and not line[0].isspace() and TOP_LEVEL_RE.match(line):
            yield lines[start:index]
            start = None
    if start is not None:
        yield lines[start:]


def positive_reads(block):
    result = set()
    for line in block:
        match = HAS_WORLD_RE.match(line) or POSITIVE_NUMERIC_READ_RE.match(line)
        if match:
            result.add(match.group(1))
    return result


def positive_writes(block):
    result = set()
    for line in block:
        match = SET_WORLD_RE.match(line) or POSITIVE_NUMERIC_WRITE_RE.match(line)
        if match:
            result.add(match.group(1))
    return result


def build_graph():
    graph = defaultdict(set)
    provenance = defaultdict(set)

    for path in a1_data_files():
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for block in mission_blocks(text):
            if not block:
                continue
            mission_name = block[0].strip()
            reads = positive_reads(block)
            writes = positive_writes(block)
            for source in reads:
                for destination in writes:
                    if source == destination:
                        continue
                    graph[source].add(destination)
                    provenance[(source, destination)].add((relative, mission_name))

    # Include sink-only nodes so graph algorithms see the full state set.
    for destinations in tuple(graph.values()):
        for destination in destinations:
            graph.setdefault(destination, set())

    return graph, provenance


def find_cycle(graph):
    """Return one directed cycle, if any, using deterministic DFS ordering."""
    visited = set()
    active = set()
    stack = []
    stack_index = {}

    def visit(node):
        visited.add(node)
        active.add(node)
        stack_index[node] = len(stack)
        stack.append(node)

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                cycle = visit(neighbor)
                if cycle:
                    return cycle
            elif neighbor in active:
                start = stack_index[neighbor]
                return stack[start:] + [neighbor]

        stack.pop()
        stack_index.pop(node, None)
        active.remove(node)
        return None

    for node in sorted(graph):
        if node not in visited:
            cycle = visit(node)
            if cycle:
                return cycle
    return None


def describe_cycle(cycle, provenance):
    parts = []
    for source, destination in zip(cycle, cycle[1:]):
        locations = sorted(provenance.get((source, destination), ()))
        rendered = ", ".join(f"{path}::{mission}" for path, mission in locations)
        parts.append(f"{source!r} -> {destination!r} via {rendered or 'unknown'}")
    return "\n".join(parts)


def test_parser_discovers_current_cross_system_edges():
    graph, _ = build_graph()

    # These accepted edges span numeric and boolean-mediated propagation and keep
    # this test from silently becoming vacuous if the lightweight parser breaks.
    expected = {
        ("world: southern rim transit congestion", "world: free worlds relief demand"),
        ("world: free worlds defense strain", "world: free worlds patrol surge"),
        ("world: free worlds patrol surge", "world: southern rim transit congestion"),
        ("world: merchant rescue load", "world: merchant rescue reserve strain"),
        ("world: republic customs scrutiny", "world: republic inspection backlog"),
    }
    missing = sorted((source, destination) for source, destination in expected if destination not in graph[source])
    assert not missing, f"positive-dependency parser missed accepted edges: {missing}"


def test_a1_positive_world_dependency_graph_is_acyclic():
    graph, provenance = build_graph()
    assert graph, "no A1 positive world-state dependency graph was discovered"

    cycle = find_cycle(graph)
    assert cycle is None, (
        "A1 positive world-state dependency cycle detected. Positive cycles can "
        "self-amplify independently bounded counters and must be redesigned, "
        "made one-way, or justified with an explicit stronger stability model.\n"
        + describe_cycle(cycle, provenance)
    )


def test_previously_rejected_reverse_edges_remain_absent():
    graph, provenance = build_graph()
    forbidden = {
        # Current accepted direction is congestion -> relief demand.
        ("world: free worlds relief demand", "world: southern rim transit congestion"),
        # Defense can create patrol load that reaches rescue through congestion;
        # rescue must not close the loop by recreating defense strain.
        ("world: merchant rescue load", "world: free worlds defense strain"),
        # Maintenance already feeds congestion; transit must not recreate the
        # maintenance backlog and form a two-way infrastructure amplifier.
        ("world: southern rim transit congestion", "world: syndicate maintenance backlog"),
    }
    present = []
    for edge in sorted(forbidden):
        source, destination = edge
        if destination in graph[source]:
            present.append((edge, sorted(provenance.get(edge, ()))))
    assert not present, f"previously rejected reverse A1 edges reintroduced: {present}"
