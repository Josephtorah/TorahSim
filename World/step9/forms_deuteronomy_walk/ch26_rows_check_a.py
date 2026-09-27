#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 18 — CHAPTERS 26-28 (LEAN, 2026-09-26): THE RUN-1 IMPORT CHECK — chapter 26's rows imported (the spine's 77 in four files, Onkelos's 19),
# the cuts' misses asserted empty; every key inside the spine's rows; the REREAD marks as computed. Sitting 17's form (ch22_rows_check_a.py), cut to the run's files.
import ch26_ink as I
import ch26_rows_sifrei_297_300 as A, ch26_rows_sifrei_301_a as B1, ch26_rows_sifrei_301_b as B2, ch26_rows_sifrei_302_303 as C, ch26_rows_onkelos_26 as H
from collections import Counter
S = {**A.S, **B1.S, **B2.S, **C.S}; R = dict(H.R)
byp = Counter(p for p, r in S)
print('THE SIFREI ROWS TYPED (chapter 26):', len(S), '| by piska:', dict(sorted(byp.items())))
want = set(I.READ_ROWS)
print('  typed == spine 297-303:', set(S) == want, '| missing:', sorted(want - set(S)), '| extra:', sorted(set(S) - want))
print('  Onkelos typed:', len(R), '== SPAN 26:', sorted(R) == [(c, v) for c, v in I.SPAN if c == 26])
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower())
print('  the REREAD marks (spine):', rr, '| computed:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR}))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == want and len(S) == 77 and sorted(R) == [(c, v) for c, v in I.SPAN if c == 26]
assert rr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR}), rr
print('  bytes of prose:', sum(len(t.encode()) for _, t in S.values()) + sum(len(t.encode()) for _, t in R.values()))
print('THE RUN-1 IMPORT CHECK GREEN')
