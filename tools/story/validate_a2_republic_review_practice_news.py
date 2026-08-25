#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PATH = Path("data/human/a2 republic review practice news.txt")
PREFIX = 'news "A2 Republic review practice '
EXPECTED = {
    "safeguards routine": (
        'has "B2 Republic Review Mentorship: settlement safeguards record"',
        '"world: republic customs scrutiny" < 3',
    ),
    "safeguards elevated": (
        'has "B2 Republic Review Mentorship: settlement safeguards record"',
        '"world: republic customs scrutiny" >= 3',
    ),
    "circles routine": (
        'has "B2 Republic Review Mentorship: settlement supervised review circle"',
        '"world: republic customs scrutiny" < 3',
    ),
    "circles elevated": (
        'has "B2 Republic Review Mentorship: settlement supervised review circle"',
        '"world: republic customs scrutiny" >= 3',
    ),
}
CANONICAL_HEADER = """# Copyright (c) 2026 by Wiredshark
#
# Endless Sky is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
"""


def split_news(text: str):
    starts = [m.start() for m in re.finditer(r'^news "A2 Republic review practice ', text, re.M)]
    blocks = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        blocks.append(text[start:end])
    return blocks


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else PATH
    text = path.read_text(encoding="utf-8")
    errors = []

    if not text.startswith(CANONICAL_HEADER):
        errors.append("missing canonical GPL header")
    if not text.endswith("\n"):
        errors.append("file must end with newline")

    blocks = split_news(text)
    if len(blocks) != 4:
        errors.append(f"expected exactly 4 Republic review-practice news groups, found {len(blocks)}")

    by_name = {}
    for block in blocks:
        first = block.splitlines()[0]
        match = re.fullmatch(r'news "A2 Republic review practice (.+)"', first)
        if not match:
            errors.append(f"malformed news declaration: {first}")
            continue
        by_name[match.group(1)] = block

    if set(by_name) != set(EXPECTED):
        errors.append(f"unexpected news groups: {sorted(set(by_name) ^ set(EXPECTED))}")

    common = [
        'has "B2 Republic Review Mentorship: aftermath seen"',
        'has "A2 Republic Customs Review: precedent use bounded"',
        'not "A2 Republic Customs Review: precedent kept private"',
        'government "Republic"',
        'phrase\n\t\t\t"merchant names"',
        "\tmessage\n",
    ]
    for name, (settlement, scrutiny) in EXPECTED.items():
        block = by_name.get(name, "")
        for token in common + [settlement, scrutiny]:
            if token not in block:
                errors.append(f"{name}: missing required gate/payload {token!r}")
        other_settlement = (
            'has "B2 Republic Review Mentorship: settlement supervised review circle"'
            if "safeguards" in name
            else 'has "B2 Republic Review Mentorship: settlement safeguards record"'
        )
        if other_settlement in block:
            errors.append(f"{name}: cross-settlement gate present")
        other_scrutiny = (
            '"world: republic customs scrutiny" >= 3'
            if "routine" in name
            else '"world: republic customs scrutiny" < 3'
        )
        if other_scrutiny in block:
            errors.append(f"{name}: conflicting scrutiny gate present")

    if text.count('has "B2 Republic Review Mentorship: aftermath seen"') != 4:
        errors.append("every group must require resolved B2 aftermath")
    if text.count('has "A2 Republic Customs Review: precedent use bounded"') != 4:
        errors.append("every group must require bounded precedent consent")
    if text.count('not "A2 Republic Customs Review: precedent kept private"') != 4:
        errors.append("every group must explicitly exclude private precedent")
    if text.count('"world: republic customs scrutiny" < 3') != 2:
        errors.append("expected exactly two routine-scrutiny variants")
    if text.count('"world: republic customs scrutiny" >= 3') != 2:
        errors.append("expected exactly two elevated-scrutiny variants")

    forbidden_directives = (
        "mission ", "conversation ", "action", "objective", "destination ",
        "waypoint ", "stopover ", "cargo ", "outfit ", "credits ", "reputation ",
        "fleet ", "ship ", "government attitude", "event ",
    )
    for line in text.splitlines():
        stripped = line.lstrip("\t")
        if line.startswith("\t") and any(stripped.startswith(token) for token in forbidden_directives):
            errors.append(f"forbidden gameplay/state directive: {stripped}")

    assignment = re.compile(r'^\s*"(?:world:|A2 Republic Customs Review:|B2 Republic Review Mentorship:)[^"]+"\s*(?:=|\+=|-=)\s*')
    for line in text.splitlines():
        if assignment.match(line):
            errors.append(f"forbidden upstream/world assignment: {line.strip()}")

    if 'has "A2 Republic Customs Review: precedent kept private"' in text:
        errors.append("private precedent must never positively authorize public News")

    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("PASS")
    print("news_groups=4")
    print("settlements=safeguards_record,supervised_review_circle")
    print("scrutiny_variants=routine,elevated")
    print("public_consent=bounded_only")
    print("private_precedent_publicized=no")
    print("state_writes=none")
    print("scope=Republic")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
