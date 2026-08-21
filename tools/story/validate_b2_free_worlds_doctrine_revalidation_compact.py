#!/usr/bin/env python3
from pathlib import Path
import re, sys
P=Path(sys.argv[1]) if len(sys.argv)>1 else Path('data/human/b2 free worlds doctrine revalidation compact.txt')
T=P.read_text(encoding='utf-8')
PREFIX='B2 Free Worlds Doctrine Revalidation Compact:'
MISSIONS={PREFIX+' Offer',PREFIX+' Review',PREFIX+' Keel Remembers'}
ROUTES={PREFIX+' route baseline',PREFIX+' route current',PREFIX+' route paired'}
SETTLE={PREFIX+' settlement portable doctrine packet',PREFIX+' settlement revalidation cycle'}
UPSTREAM={'world: free worlds patrol surge','world: free worlds repair backlog','A2 Free Worlds Patrol Doctrine: civilians future contact','A2 Free Worlds Patrol Doctrine: interdiction future contact','A2 Free Worlds Patrol Doctrine: mobility future contact'}
def fail(m): raise SystemExit('FAIL: '+m)
names=set(re.findall(r'^mission "([^"]+)"$',T,re.M))
if names!=MISSIONS: fail(f'missions {sorted(names)}')
for n in ('Anika Ro','Mira Keel'):
 if n not in T: fail('missing character '+n)
if T.count('government "Free Worlds"')!=3: fail('all missions must be Free Worlds scoped')
for c in UPSTREAM:
 if c not in T: fail('missing upstream input '+c)
 for line in T.splitlines():
  if c in line and any(op in line for op in (' = ',' += ',' -= ','set ','clear ')): fail('upstream mutation: '+line.strip())
for required in ('has "world: free worlds patrol surge"','not "world: free worlds patrol surge"','"world: free worlds repair backlog" >= 3','"world: free worlds repair backlog" <= 1'):
 if required not in T: fail('missing state gate '+required)
for r in ROUTES:
 if f'"{r}" = 1' not in T: fail('missing route '+r)
if f'"{PREFIX} declined" = 1' not in T: fail('missing refusal')
for s in SETTLE:
 if f'"{s}" = 1' not in T: fail('missing settlement '+s)
 if f'has "{s}"' not in T: fail('aftermath does not read '+s)
if f'"{PREFIX} aftermath seen" = 1' not in T: fail('missing one-shot aftermath')
for cond in re.findall(r'^\s*"([^"]+)"\s*(?:=|\+=|-=)\s*\d+',T,re.M):
 if not cond.startswith(PREFIX): fail('write outside B2 namespace: '+cond)
for line in T.splitlines():
 s=line.strip()
 if s.startswith(('credits ','reputation ','combat rating ','cargo ','outfit ','ship ','fleet ')): fail('material mutation: '+s)
low=T.lower()
for phrase in ('historical evidence','repair backlog','source lineage','revalidation','central order'):
 if phrase not in low: fail('missing continuity concept '+phrase)
if 'repetition of one source is not several sources' not in low: fail('missing source-independence safeguard')
labels=set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)$',T,re.M)); gotos=set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)$',T,re.M))
if gotos-labels: fail('missing labels '+repr(sorted(gotos-labels)))
print('PASS: B2 Free Worlds Doctrine Revalidation Compact structure validated')
print('PASS: missions=3; named_characters=2; routes=3+refusal; settlements=2')
print('PASS: A1 patrol surge/repair backlog read-only; A2 doctrine memory read-only')
print('PASS: write ownership=B2 namespace only; source lineage/revalidation explicit')
