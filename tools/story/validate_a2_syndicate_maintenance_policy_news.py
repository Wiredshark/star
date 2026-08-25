#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PREFIX = 'news "A2 Syndicate maintenance policy '
EXPECTED = {
    "safety pressure": "Marr remembers safety under pressure",
    "safety stable": "Marr remembers safety stabilized",
    "contracts pressure": "Marr remembers contracts under pressure",
    "contracts stable": "Marr remembers contracts stabilized",
    "resilience pressure": "Marr remembers resilience under pressure",
    "resilience stable": "Marr remembers resilience stabilized",
}
FOLLOWUP = 'has "A2 Syndicate Maintenance Triage: followup seen"'


def split_news(text: str):
    blocks = {}
    matches = list(re.finditer(r'^news "A2 Syndicate maintenance policy ([^"]+)"$', text, re.MULTILINE))
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[match.group(1)] = text[start:end]
    return blocks


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 syndicate maintenance policy news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []

    blocks = split_news(text)
    if set(blocks) != set(EXPECTED):
        errors.append(f"expected exactly six named maintenance-policy News groups; got {sorted(blocks)}")

    for outcome, memory in EXPECTED.items():
        block = blocks.get(outcome, "")
        if not block:
            continue
        if block.count(FOLLOWUP) != 1:
            errors.append(f"{outcome}: must require followup seen exactly once")
        gate = f'has "A2 Syndicate Maintenance Triage: {memory}"'
        if block.count(gate) != 1:
            errors.append(f"{outcome}: missing or duplicate exact outcome gate: {memory}")
        triage_has = re.findall(r'^\s*has "A2 Syndicate Maintenance Triage: ([^"]+)"$', block, re.MULTILINE)
        if len(triage_has) != 2:
            errors.append(f"{outcome}: expected exactly followup + one outcome gate, got {triage_has}")
        if block.count('\n\tlocation\n\t\tgovernment "Syndicate"\n') != 1:
            errors.append(f"{outcome}: must be scoped to Syndicate locations")
        if '\n\tname\n' not in block or '\n\tmessage\n' not in block:
            errors.append(f"{outcome}: missing News name/message payload")

    if text.count(PREFIX) != 6:
        errors.append("expected exactly six maintenance-policy News declarations")

    privacy_tokens = [
        "A2 Syndicate Maintenance Triage: refused",
        "A2 Syndicate Maintenance Triage: refusal respected",
    ]
    for token in privacy_tokens:
        if token in text:
            errors.append(f"refusal must remain private; found public gate/reference: {token}")

    forbidden_tokens = [
        '\nmission "',
        '\nconversation\n',
        '\n\taction\n',
        '"world:',
        '\n\tcredits ',
        '\n\treputation ',
        '\n\tcargo ',
        '\n\toutfit ',
        '\n\tship ',
        '\n\tfleet ',
        '\n\tdestination ',
        '\n\twaypoint ',
        '\n\tnpc ',
    ]
    for token in forbidden_tokens:
        if token in text:
            errors.append(f"read-only News consumer contains forbidden gameplay/state token: {token!r}")

    if re.search(r'^\s*"(?:A2 Syndicate Maintenance Triage|A2 Syndicate maintenance policy)[^"]*"\s*(?:=|\+=|-=)', text, re.MULTILINE):
        errors.append("News consumer must not assign upstream or local persistent state")

    if not text.startswith("# Copyright (c) 2026 by Wiredshark\n"):
        errors.append("missing canonical project copyright header")
    if "GNU General Public License" not in text or "WITHOUT ANY" not in text:
        errors.append("incomplete GPL notice")
    if not text.endswith("\n"):
        errors.append("file must end with a trailing newline")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: Syndicate maintenance policy News has 6 exact read-only outcome consumers; refusal stays private")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
