#!/usr/bin/env python3
# 11b docket — the four parts loaded (each asserts its slice fully matched — no unmatched address); the counts computed, never typed. 10b's ch12_d1_check.py
# form with the shared unresolved file (ch13_docket_U.py) counted once at the end.
import importlib.util, sys, os, re
from collections import Counter
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
tot = Counter(); n = 0; unres = 0; carried = 0; cells = Counter(); used_all = set()
for p in 'ABCD':
    spec = importlib.util.spec_from_file_location(f'ch13_docket_{p}', f'{SP}/ch13_docket_{p}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    c = Counter(v for _, v, _ in m.ROWS); n += len(m.ROWS); tot += c
    car = sum(1 for _, _, nt in m.ROWS if nt.startswith('CREDITED (') and '; carried) — ' in nt[:200]); un = sum(1 for _, _, nt in m.ROWS if nt.startswith('CREDITED (') and 'read whole here' in nt[:400]); carried += car; unres += un
    for _, v, nt in m.ROWS:
        if v == 'LAW' and not nt.startswith('CREDITED ('):
            mm = re.search(r'\b(F[1-6])\b', nt)
            if mm: cells[mm.group(1)] += 1
    used = {a for a, _, _ in m.ROWS}; used_all |= used; extra = [a for a, _, _ in m.OWN if a not in used]
    print(p, 'rows', len(m.ROWS), dict(sorted(c.items())), 'carried', car, 'unresolved-read-here', un, 'own', len(m.OWN), m.WHOLE_STATS, ('OWN NOT USED: %s' % extra) if extra else '')
from ch13_docket_U import OWN_U
extra_u = [a for a, _, _ in OWN_U if a not in used_all]
print('U rows', len(OWN_U), 'used', len(OWN_U) - len(extra_u), ('U NOT USED: %s' % extra_u) if extra_u else '')
print('TOTAL', n, dict(sorted(tot.items())), 'carried', carried, 'unresolved read here', unres, 'read here', n - carried, 'LAW by cell (own notes)', dict(sorted(cells.items())))
