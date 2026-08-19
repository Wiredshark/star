from pathlib import Path
TEXT=(Path(__file__).resolve().parents[2]/"data/human/a1 syndicate maintenance backlog.txt").read_text()
def assist(v): return (v,False) if v>=6 else (min(6,v+1),True)
def recover(v): return max(0,v-1)
def mobilize(v,s,parts): return (v,s,parts,False) if s or v<4 else (max(0,v-3),True,min(6,parts+2),True)
def relieve(parts): return max(0,parts-1)
def test_all():
    for x in ['government "Syndicate"','"world: syndicate maintenance backlog" < 6','"world: syndicate maintenance backlog" += 1','event "ES A1: Syndicate Maintenance Backlog Recovery" 7 7','"world: syndicate maintenance backlog" >= 4','set "world: syndicate maintenance surge"','event "ES A1: Syndicate Maintenance Surge Ends" 6 6','"world: syndicate parts scarcity" += 2','"world: syndicate parts scarcity" <?= 6','event "ES A1: Syndicate Parts Scarcity Recovery" 4 4','event "ES A1: Syndicate Parts Scarcity Recovery" 8 8','mission "ES A1: Syndicate Parts Relief"','"world: syndicate parts scarcity" -= 1']:
        assert x in TEXT
    v=0;sched=0
    for _ in range(9):
        v,a=assist(v); sched+=a
    assert (v,sched)==(6,6)
    for _ in range(8): v=recover(v)
    assert v==0
    v=0;s=False;parts=0
    for _ in range(4): v,_=assist(v)
    v,s,parts,a=mobilize(v,s,parts); assert (v,s,parts,a)==(1,True,2,True)
    for _ in range(4): v,_=assist(v)
    assert mobilize(v,s,parts)==(5,True,2,False)
    s=False
    v,s,parts,a=mobilize(v,s,parts); assert (v,s,parts,a)==(2,True,4,True)
    assert relieve(relieve(parts))==2
    for _ in range(8): parts=recover(parts)
    assert parts==0
    parts=6
    _,_,parts,a=mobilize(4,False,parts); assert (parts,a)==(6,True)
if __name__=="__main__":
    test_all(); print("A1 Syndicate maintenance-backlog + parts-scarcity contract: PASS")
