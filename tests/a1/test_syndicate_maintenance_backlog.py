from pathlib import Path
TEXT=(Path(__file__).resolve().parents[2]/"data/human/a1 syndicate maintenance backlog.txt").read_text()
def assist(v): return (v,False) if v>=6 else (min(6,v+1),True)
def recover(v): return max(0,v-1)
def mobilize(v,s): return (v,s,False) if s or v<4 else (max(0,v-3),True,True)
def test_all():
    for x in ['government "Syndicate"','"world: syndicate maintenance backlog" < 6','"world: syndicate maintenance backlog" += 1','event "ES A1: Syndicate Maintenance Backlog Recovery" 7 7','"world: syndicate maintenance backlog" >= 4','set "world: syndicate maintenance surge"','event "ES A1: Syndicate Maintenance Surge Ends" 6 6']:
        assert x in TEXT
    v=0;sched=0
    for _ in range(9):
        v,a=assist(v); sched+=a
    assert (v,sched)==(6,6)
    for _ in range(8): v=recover(v)
    assert v==0
    v=0;s=False
    for _ in range(4): v,_=assist(v)
    v,s,a=mobilize(v,s); assert (v,s,a)==(1,True,True)
    for _ in range(4): v,_=assist(v)
    assert mobilize(v,s)==(5,True,False)
    s=False
    assert mobilize(v,s)==(2,True,True)
if __name__=="__main__":
    test_all(); print("A1 Syndicate maintenance-backlog contract: PASS")
