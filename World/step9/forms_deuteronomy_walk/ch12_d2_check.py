#!/usr/bin/env python3
# 10b docket D2 — the D2 parts loaded (each asserts its slice fully matched — no unmatched address); the counts computed, never typed. The parts by argv
# (D2a: D; D2b: E F …); ch12_d1_check.py's form.
import importlib.util, sys, os, re
from collections import Counter
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
PARTS = sys.argv[1] if len(sys.argv) > 1 else 'D'
tot = Counter(); n = 0; unres = 0; carried = 0; cells = Counter()
for p in PARTS:
    spec = importlib.util.spec_from_file_location(f'ch12_docket_{p}', f'{SP}/ch12_docket_{p}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    c = Counter(v for _, v, _ in m.ROWS); n += len(m.ROWS); tot += c
    car = sum(1 for _, _, nt in m.ROWS if nt.startswith('CREDITED (') and '; carried) — ' in nt[:200]); un = sum(1 for _, _, nt in m.ROWS if nt.startswith('CREDITED (') and 'read whole here' in nt[:400]); carried += car; unres += un
    for _, v, nt in m.ROWS:
        if v == 'LAW' and not nt.startswith('CREDITED ('):
            mm = re.search(r'\b(F[1-6])\b', nt)
            if mm: cells[mm.group(1)] += 1
    used = {a for a, _, _ in m.ROWS}; extra = [a for a, _, _ in m.OWN if a not in used]
    print(p, 'rows', len(m.ROWS), dict(sorted(c.items())), 'carried', car, 'unresolved-read-here', un, 'own', len(m.OWN), m.WHOLE_STATS, ('OWN NOT USED: %s' % extra) if extra else '')
print(PARTS, 'TOTAL', n, dict(sorted(tot.items())), 'carried', carried, 'unresolved read here', unres, 'read here', n - carried, 'LAW by cell (own notes)', dict(sorted(cells.items())))
