#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PREFIX = 'news "A2 Free Worlds relief policy '
EXPECTED = {
    "medical clear": "Vale remembers medical clear",
    "medical residual": "Vale remembers medical residual",
    "throughput clear": "Vale remembers throughput clear",
    "throughput residual": "Vale remembers throughput residual",
    "distribution clear": "Vale remembers distribution clear",
    "distribution residual": "Vale remembers distribution residual",
}
FOLLOWUP = 'has "A2 Free Worlds Relief Coordination: followup seen"'
UPSTREAM_PREFIX = "A2 Free Worlds Relief Coordination:"


def split_news(text: str):
    blocks = {}
    matches = list(re.finditer(r'^news "A2 Free Worlds relief policy ([^"]+)"$', text, re.MULTILINE))
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[match.group(1)] = text[start:end]
    return blocks


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 free worlds relief policy news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []

    blocks = split_news(text)
    if set(blocks) != set(EXPECTED):
        errors.append(f"expected exactly six named relief-policy News groups; got {sorted(blocks)}")

    for outcome, memory in EXPECTED.items():
        block = blocks.get(outcome, "")
        if not block:
            continue
        if block.count(FOLLOWUP) != 1:
            errors.append(f"{outcome}: must require followup seen exactly once")
        gate = f'has "{UPSTREAM_PREFIX} {memory}"'
        if block.count(gate) != 1:
            errors.append(f"{outcome}: missing or duplicate exact outcome gate: {memory}")
        relief_has = re.findall(r'^\s*has "A2 Free Worlds Relief Coordination: ([^"]+)"$', block, re.MULTILINE)
        expected_gates = {"followup seen", memory}
        if set(relief_has) != expected_gates or len(relief_has) != 2:
            errors.append(f"{outcome}: expected exactly followup + one matching outcome gate, got {relief_has}")
        if block.count('\n\tlocation\n\t\tgovernment "Free Worlds"\n') != 1:
            errors.append(f"{outcome}: must be scoped to Free Worlds locations")
        if '\n\tname\n' not in block or '\n\tmessage\n' not in block:
            errors.append(f"{outcome}: missing News name/message payload")

    if text.count(PREFIX) != 6:
        errors.append("expected exactly six relief-policy News declarations")

    privacy_tokens = [
        "A2 Free Worlds Relief Coordination: refused",
        "A2 Free Worlds Relief Coordination: refusal respected",
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

    if re.search(r'^\s*"A2 Free Worlds Relief Coordination:[^"]*"\s*(?:=|\+=|-=)', text, re.MULTILINE):
        errors.append("News consumer must not assign upstream persistent state")
    if re.search(r'^\s*"A2 Free Worlds relief policy[^"]*"\s*(?:=|\+=|-=)', text, re.MULTILINE):
        errors.append("News consumer must not create local persistent state")

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

    print("PASS: Free Worlds relief policy News has 6 exact read-only outcome consumers; refusal stays private")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
