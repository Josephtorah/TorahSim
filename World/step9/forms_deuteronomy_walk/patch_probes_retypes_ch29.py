import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — RUN B: THE READBACK PROBES THAT COUNT THE MARKERS RETYPED BEFORE THE TAPE'S SECOND RUN — the grep decided (18b's lesson 9
# in the marker's form: the reuses moved the counts, THE MARKER moves the count of markers): every earlier probe asserting `172` markers (Q14 … Q47 — fifteen `return got ==`
# lines, found by grep on the literal; every line read) retyped 172 -> 173 after the stitcher's print (seq_stitch_ch29.out — markers 173) and the tape's first run; Q48's own
# KIN literal retyped at its forty-third count barred_from_the_land 1 -> 2 (Moses' AND Aaron's entries at Numbers 20:12 — the recon read Moses' ledger alone; count_scan and
# the tape count the world's: READ FROM THE FAST CHECKER'S FIRST PRINT). Each edit asserted on its own line; a 19b comment line above each return. --check prints only.
import re, sys, os, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
F = f'{ROOT}/World/step9/readback_probes.py'; L = open(F, encoding='utf-8').read().split('\n')
M = '# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): '
pr = open(f'{SP}/seq_stitch_ch29.out', encoding='utf-8').read()
assert re.search(r'markers: 173\b', pr) or '173' in re.search(r'^  CENSUS tuple .*?: (\(.*\))$', pr, re.M).group(1), 'the stitcher\'s print carries 173 markers'
E = []
for i, l in enumerate(L):
    if l.lstrip().startswith('return got ==') and ', 172,' in l and 'def q48' not in l:
        E.append((i + 1, ', 172,', ', 173,', "markers 172 -> 173 (THE ONE MARKER at Deut 31:1 — Moses' last day (40, 12, 7), sitting 19b's; retyped BEFORE the tape's second run, the stitcher's print and the tape's first run decided)"))
assert len(E) == 15, [(ln, L[ln - 1][:50]) for ln, *_ in E]
q48 = next(i for i, l in enumerate(L) if l.startswith('def q48():'))
r48 = next(i for i in range(q48, len(L)) if L[i].lstrip().startswith('return got =='))
old48 = ', 3, 1, 1, 3, 1)'   # the KIN tuple's tail — witness_declared 1, covenant_remembered 1, great_nation_promised 3, barred_from_the_land 1
assert L[r48].count(old48) == 1, L[r48][-200:]
E.append((r48 + 1, old48, ', 3, 1, 1, 3, 2)', "barred_from_the_land 1 -> 2 in Q48's KIN tuple (the forty-third count — Moses' AND Aaron's entries at Numbers 20:12: the recon read Moses' ledger alone, the world holds two; READ FROM THE FAST CHECKER'S FIRST PRINT — the spec module retyped with it)"))
for ln, old, new, note in E:
    l = L[ln - 1]; assert l.count(old) == 1 and l.lstrip().startswith('return got =='), (ln, l.count(old), l[:60])
    L[ln - 1] = l.replace(old, new)
for ln, old, new, note in sorted(E, key=lambda e: -e[0]):
    ind = L[ln - 1][:len(L[ln - 1]) - len(L[ln - 1].lstrip())]; L.insert(ln - 1, ind + M + note)
print('readback_probes.py: %d lines to retype (%d marker counts 172 -> 173 and Q48\'s kin count), %d comment lines' % (len(E), len(E) - 1, len(E)), '| CHECK' if CHECK else '| WRITTEN')
if not CHECK: open(F, 'w', encoding='utf-8').write('\n'.join(L))
