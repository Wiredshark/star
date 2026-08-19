#!/usr/bin/env python3
"""Cross-file structural and state-ownership QA for fork-authored A1/A2/B2 data.

Focused per-slice validators are useful but cannot detect collisions between files.
This check deliberately stays conservative: it validates only invariants that are
supposed to hold across every fork-authored A1/A2/B2 slice.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

NODE_RE = re.compile(r'^(mission|event) "([^"]+)"$', re.MULTILINE)
MISSION_RE = re.compile(r'^mission "([^"]+)"$', re.MULTILINE)
LABEL_RE = re.compile(r'^\s*label\s+([A-Za-z0-9_ -]+?)\s*$', re.MULTILINE)
GOTO_RE = re.compile(r'^\s*goto\s+([A-Za-z0-9_ -]+?)\s*$', re.MULTILINE)
WORLD_WRITE_RE = re.compile(
    r'^\s*"(world:[^"]+)"\s*(?:\+=|-=|\+\+|--|<\?=|>\?=|\?=|=)(?:\s|$)',
    re.MULTILINE,
)
WORLD_SET_CLEAR_RE = re.compile(
    r'^\s*(?:set|clear)\s+"(world:[^"]+)"(?:\s|$)',
    re.MULTILINE,
)


@dataclass(frozen=True)
class ForkFile:
    path: Path
    layer: str

    @property
    def relative(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def discover_files() -> list[ForkFile]:
    result: list[ForkFile] = []
    for path in sorted(DATA.rglob("*.txt")):
        name = path.name.lower()
        layer = next((prefix.upper() for prefix in ("a1", "a2", "b2") if name.startswith(prefix)), None)
        if layer:
            result.append(ForkFile(path, layer))
    return result


def split_missions(text: str) -> list[tuple[str, str]]:
    starts = list(MISSION_RE.finditer(text))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        blocks.append((match.group(1), text[match.start():end]))
    return blocks


def find_world_writes(text: str) -> set[str]:
    return set(WORLD_WRITE_RE.findall(text)) | set(WORLD_SET_CLEAR_RE.findall(text))


def main() -> int:
    files = discover_files()
    if not files:
        print("FAIL: no fork-authored A1/A2/B2 data files discovered")
        return 1

    errors: list[str] = []
    nodes: dict[tuple[str, str], list[str]] = defaultdict(list)
    world_writers: dict[str, set[str]] = defaultdict(set)
    counts = defaultdict(int)

    for item in files:
        counts[f"files_{item.layer.lower()}"] += 1
        text = item.path.read_text(encoding="utf-8")

        for node_kind, node_name in NODE_RE.findall(text):
            nodes[(node_kind, node_name)].append(item.relative)
            counts[node_kind + "s"] += 1

        writes = find_world_writes(text)
        for condition in writes:
            world_writers[condition].add(item.relative)

        if item.layer in {"A2", "B2"} and writes:
            for condition in sorted(writes):
                errors.append(
                    f"{item.relative}: {item.layer} may read but not write A1 world authority {condition!r}"
                )

        for mission_name, block in split_missions(text):
            labels = set(LABEL_RE.findall(block))
            gotos = set(GOTO_RE.findall(block))
            missing = sorted(gotos - labels)
            if missing:
                errors.append(
                    f"{item.relative}: mission {mission_name!r} has local goto target(s) without labels: {missing}"
                )

    for (node_kind, node_name), paths in sorted(nodes.items()):
        unique_paths = sorted(set(paths))
        if len(paths) > 1:
            errors.append(
                f"duplicate {node_kind} name {node_name!r}: " + ", ".join(unique_paths)
            )

    # A world condition may have multiple A1 mutation sites when they are parts of
    # one simulation model (e.g. escalation and decay). The invariant here is that
    # every writer is A1-owned, not that there is exactly one physical write line.
    non_a1_world_writers = {
        condition: sorted(path for path in paths if not Path(path).name.lower().startswith("a1"))
        for condition, paths in world_writers.items()
    }
    for condition, paths in sorted(non_a1_world_writers.items()):
        if paths:
            errors.append(f"world authority {condition!r} has non-A1 writer(s): {', '.join(paths)}")

    print("Fork content contract summary")
    print(f"files={len(files)}")
    print(f"a1_files={counts['files_a1']}")
    print(f"a2_files={counts['files_a2']}")
    print(f"b2_files={counts['files_b2']}")
    print(f"missions={counts['missions']}")
    print(f"events={counts['events']}")
    print(f"a1_world_conditions_with_writers={len(world_writers)}")

    if errors:
        print(f"FAIL: violations={len(errors)}")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: mission/event names are unique across fork A1/A2/B2 data")
    print("PASS: every parsed mission goto target has a label in the same mission")
    print("PASS: A2/B2 do not mutate A1 world:* authority")
    print("PASS: all discovered world:* writers are A1-owned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
