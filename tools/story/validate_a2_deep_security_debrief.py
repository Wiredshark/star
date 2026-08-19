#!/usr/bin/env python3
from pathlib import Path
import sys

def main():
    p=Path(sys.argv[1]) if len(sys.argv)>1 else Path("data/human/a2 deep security debrief.txt")
    t=p.read_text(encoding="utf-8")
    req=[
        'mission "A2 Deep Debrief: First Meeting"',
        'mission "A2 Deep Debrief: Later Reader"', 'Mara Venn',
        '[Convoy record: Deep Syndicate escort]', '[Combat record: veteran escort]',
        'to display\n\t\t\t\t\t\thas "Deep: Syndicate Convoy: done"',
        'to activate\n\t\t\t\t\t\t"combat rating" >= 80',
        'label convoy','label veteran','label procedure','label refuse',
        '"A2 Deep Debrief: approach convoy precedent" = 1',
        '"A2 Deep Debrief: approach threat judgment" = 1',
        '"A2 Deep Debrief: approach procedure" = 1',
        '"A2 Deep Debrief: refused" = 1',
        '"A2 Deep Debrief: refusal respected" = 1',
        '"A2 Deep Debrief: venn future field contact" = 1',
        '"A2 Deep Debrief: venn future security contact" = 1',
        '"A2 Deep Debrief: venn future review contact" = 1',
    ]
    missing=[x for x in req if x not in t]
    if missing:
        print('FAIL')
        print('\n'.join('- '+x for x in missing))
        return 1
    if any(x in t.lower() for x in ('dialogue world state','dialogue_state','dialogue memory database')):
        print('FAIL shadow state')
        return 1
    print('PASS')
    print('missions=2')
    print('named_character=Mara Venn')
    print('first_meeting_routes=4')
    print('persistent_state_sources=Deep: Syndicate Convoy: done, combat rating')
    print('requirement_labels=2; hidden=1; disabled-visible=1')
    print('later_reader_routes=4')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
