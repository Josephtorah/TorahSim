# THE IMPORT CHECK over all seven row files (sitting 14, LEAN, 2026-09-23): the Sifrei set == the ink's 111 spine rows, the Onkelos 22 == SPAN, the outside
# 3 == OUTSIDE, the REREAD marks as computed; the cuts' misses (FAIL) asserted empty.
import ch16_ink as I
import ch16_rows_sifrei_127_131 as A, ch16_rows_sifrei_132_136 as B, ch16_rows_sifrei_137_142 as C, ch16_rows_sifrei_143_146 as D, ch16_rows_onkelos_a as E, ch16_rows_onkelos_b as F, ch16_rows_outside as G
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S}; R = {**E.R, **F.R}; SO = G.SO
print('ALL TYPED — Sifrei:', len(S), '| Onkelos:', len(R), '| outside:', len(SO))
print('  Sifrei == spine:', set(S) == set(I.READ_ROWS), '| Onkelos == SPAN:', sorted(R) == I.SPAN, '| outside == OUTSIDE:', sorted(SO) == sorted(I.OUTSIDE))
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()), Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()); rro = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks (spine, outside):', rr, rro, '| computed:', sorted((p, r) for _, p, r in I.SPINE_PRIOR), sorted(I.PRIOR_READ))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == set(I.READ_ROWS) and sorted(R) == I.SPAN and sorted(SO) == sorted(I.OUTSIDE)
assert rr == sorted((p, r) for _, p, r in I.SPINE_PRIOR) and rro == sorted(I.PRIOR_READ), (rr, rro)
print('THE FULL IMPORT CHECK GREEN')
