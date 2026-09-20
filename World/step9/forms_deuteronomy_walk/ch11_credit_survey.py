#!/usr/bin/env python3
# 9b docket — the credited addresses by ledger, and each ledger's row FORM (one sample line per ledger) so the credited verdicts can be carried by script.
import re, os, subprocess, sys
from collections import Counter, defaultdict
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
dump = open(f'{SP}/ch11_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
CRED = {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = [x.strip() for x in m.group(1).split(',')]
byled = defaultdict(list)
for a, ls in CRED.items():
    for l in ls: byled[l].append(a)
print('credited', len(CRED), 'ledgers', len(byled))
def find(ledger):
    for d in ('logic/oral_triage', 'logic/findings', 'logic/law_era', 'logic'):
        p = f'{ROOT}/{d}/{ledger}'
        if os.path.exists(p): return p
    hits = subprocess.run(['find', ROOT, '-name', ledger, '-not', '-path', '*/elijah_docket/*'], capture_output=True, text=True).stdout.split()
    return hits[0] if hits else None
for l, addrs in sorted(byled.items(), key=lambda kv: -len(kv[1])):
    p = find(l)
    if not p: print(f'\n== {l}: {len(addrs)} addrs — FILE NOT FOUND'); continue
    t = open(p, encoding='utf-8').read()
    a = addrs[0]
    lines = [x for x in t.split('\n') if a in x]
    print(f'\n== {l}: {len(addrs)} addrs; path {p.replace(ROOT, "<repo>")}; sample {a}: {len(lines)} line(s)')
    for x in lines[:2]: print('   ', x[:260])
