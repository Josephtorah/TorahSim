#!/usr/bin/env python3
# 13b docket D2 — THE D2 CHECK (ch15_docket_d1_check.py's form with the target set a LONG RANGE named on the command line): the parts named partition the range's
# addresses of D2_UNIQUE exactly (no overlap, no miss, none outside), every verdict among the five; the census PRINTED — verdicts by kind, LAW by cell (this
# docket's own notes), OUTSIDE by folio, the carried, the unresolved read here, the rows read whole here — computed, never typed.
import os, sys, re, importlib.util
from collections import Counter
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
from ch15_docket_common import D2_UNIQUE, KIND_FIRST, long_range
PARTS, RANGE = sys.argv[1], sys.argv[2]
TARGET = [a for a in D2_UNIQUE if long_range(a) == RANGE]
V = {}; STATS = []; per = {}
for p in PARTS:
    part = f'ch15_docket_{p}'
    spec = importlib.util.spec_from_file_location(part, f'{SP}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    STATS.append(m.WHOLE_STATS); per[p] = len(m.ROWS)
    for addr, vd, note in m.ROWS:
        assert vd in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'), (addr, vd)
        assert addr not in V, ('overlap', addr, p)
        V[addr] = (vd, note)
TS = set(TARGET)
missing = [a for a in TARGET if a not in V]; extra = [a for a in V if a not in TS]
print('range', RANGE, 'parts', per, 'verdicted', len(V), 'target', len(TARGET), 'missing', len(missing), missing[:15], 'extra', len(extra), extra[:15])
assert not missing and not extra
cnt = Counter(vd for vd, _ in V.values()); cl = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'LINK'); ct = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'TOPIC')
carried = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and '; carried) — ' in n[:200]); unres = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and 'read whole here' in n[:400] and '; carried) — ' not in n[:200])
LAWCELLS = Counter(mm.group(1) for vd, n in V.values() if vd == 'LAW' and not n.startswith('CREDITED (') for mm in [re.search(r'\b(F[1-7])\b', n)] if mm)
NOUT = Counter(a.rsplit(':', 1)[0] for a, (vd, _) in V.items() if vd == 'OUTSIDE')
print('link', sum(1 for a in V if KIND_FIRST[a] == 'LINK'), 'topic', sum(1 for a in V if KIND_FIRST[a] == 'TOPIC'))
print('verdicts', dict(sorted(cnt.items())), 'link', dict(sorted(cl.items())), 'topic', dict(sorted(ct.items())))
print('carried', carried, 'unresolved_read_here', unres, 'read_here', len(V) - carried, 'whole_stats', {k: sum(s[k] for s in STATS) for k in STATS[0]})
print('LAW by cell', dict(sorted(LAWCELLS.items()))); print('OUTSIDE by folio', dict(NOUT))
