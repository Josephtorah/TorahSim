#!/usr/bin/env python3
# 13b docket D1 — THE D1 CHECK (before the writer, which runs once at D2's end on 12b's form): the parts A-F partition D1 exactly (no overlap, no miss, no address
# outside D1), every verdict among the five; the census PRINTED — verdicts by kind, LAW by cell (this docket's own notes), OUTSIDE by work, the carried, the
# unresolved read here, the rows read whole here — computed, never typed.
import os, sys, re, importlib.util
from collections import Counter
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
from ch15_docket_common import D1_UNIQUE, KIND_FIRST
PARTS = sys.argv[1] if len(sys.argv) > 1 else 'ABCDEF'
V = {}; STATS = []; per = {}
for p in PARTS:
    part = f'ch15_docket_{p}'
    spec = importlib.util.spec_from_file_location(part, f'{SP}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    STATS.append(m.WHOLE_STATS); per[p] = len(m.ROWS)
    for addr, vd, note in m.ROWS:
        assert vd in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'), (addr, vd)
        if addr in V: assert V[addr] == (vd, note), ('overlap with a different verdict', addr, p); continue
        V[addr] = (vd, note)
D1S = set(D1_UNIQUE)
missing = [a for a in D1_UNIQUE if a not in V]; extra = [a for a in V if a not in D1S]
print('parts', per, 'verdicted', len(V), 'D1', len(D1_UNIQUE), 'missing', len(missing), missing[:15], 'extra', len(extra), extra[:15])
if PARTS == 'ABCDEF': assert not missing and not extra
cnt = Counter(vd for vd, _ in V.values()); cl = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'LINK'); ct = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'TOPIC')
carried = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and '; carried) — ' in n[:200]); unres = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and 'read whole here' in n[:400] and '; carried) — ' not in n[:200])
LAWCELLS = Counter(mm.group(1) for vd, n in V.values() if vd == 'LAW' and not n.startswith('CREDITED (') for mm in [re.search(r'\b(F[1-7])\b', n)] if mm)
NOUT = Counter(a.rsplit(' ', 1)[0] for a, (vd, _) in V.items() if vd == 'OUTSIDE')
print('verdicts', dict(sorted(cnt.items())), 'link', dict(sorted(cl.items())), 'topic', dict(sorted(ct.items())))
print('carried', carried, 'unresolved_read_here', unres, 'read_here', len(V) - carried, 'whole_stats', {k: sum(s[k] for s in STATS) for k in STATS[0]})
print('LAW by cell', dict(sorted(LAWCELLS.items()))); print('OUTSIDE by work', dict(NOUT))
