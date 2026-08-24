#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PATH = Path("data/human/a2 republic customs precedent news.txt")
GROUPS = {
    "bounded audit": "A2 Republic Customs Review: outcome bounded audit",
    "written uncertainty": "A2 Republic Customs Review: outcome written uncertainty",
    "contextualized routing": "A2 Republic Customs Review: outcome contextualized routing",
    "formal process": "A2 Republic Customs Review: outcome refusal preserved",
}


def fail(errors: list[str]) -> int:
    print("FAIL")
    for error in errors:
        print("-", error)
    return 1


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else PATH
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if text.count('news "A2 Republic customs precedent ') != 4:
        errors.append("expected exactly four Republic customs precedent News groups")

    for suffix, memory in GROUPS.items():
        header = f'news "A2 Republic customs precedent {suffix}"'
        if text.count(header) != 1:
            errors.append(f"expected exactly one News group: {suffix}")
        if text.count(f'has "{memory}"') != 1:
            errors.append(f"expected exactly one outcome-memory gate: {memory}")

    if text.count('government "Republic"') != 4:
        errors.append("all four News groups must remain Republic-scoped")
    if text.count('has "A2 Republic Customs Review: later reader seen"') != 4:
        errors.append("every News group must require later reader seen")
    if text.count('has "A2 Republic Customs Review: precedent use bounded"') != 4:
        errors.append("every public News group must require bounded precedent consent")
    if 'has "A2 Republic Customs Review: precedent kept private"' in text:
        errors.append("private precedent must never authorize public News")

    if '\taction\n' in text or '\tconversation\n' in text or '\tmission ' in text:
        errors.append("ambient News consumer must not contain action/conversation/mission blocks")

    assignment = re.compile(r'^\s*"(?:world:|A1 |A2 |B1 |B2 )[^\"]+"\s*(?:=|\+=|-=)', re.MULTILINE)
    if assignment.search(text):
        errors.append("ambient News consumer must not write persistent state")

    forbidden_material = [
        '\tcredits ', '\treputation ', '\tcargo ', '\toutfit ', '\tship ', '\tfleet ',
        '\tdestroy ', '\tcombat ', '\tpayment ', '\tobjective ', '\tdestination ', '\twaypoint '
    ]
    for token in forbidden_material:
        if token in text:
            errors.append(f"forbidden gameplay mutation/objective directive: {token.strip()}")

    if "declined" in text.lower() or "precedent kept private" in text:
        # The explanatory comments may mention private precedent; public gating must not.
        public_body = "\n".join(line for line in text.splitlines() if not line.startswith("#"))
        if "precedent kept private" in public_body or "declined" in public_body.lower():
            errors.append("declined/private route must not be publicized by News content")

    if not text.endswith("\n"):
        errors.append("file must end with newline")

    if errors:
        return fail(errors)

    print("PASS")
    print("news_groups=4")
    print("scope=Republic")
    print("bounded_consent_gate=4")
    print("private_precedent_publicized=no")
    print("persistent_writes=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
