# THE IMPORT CHECK over all ten row files (sitting 15, LEAN, 2026-09-24): the Sifrei set == the ink's 181 spine rows, the Onkelos 42 == SPAN, the outside
# 11 == OUTSIDE, the REREAD marks as computed; the cuts' misses (FAIL) asserted empty. Sitting 14's form.
import ch17_ink as I
import ch17_rows_sifrei_147_149 as A, ch17_rows_sifrei_150_152 as B, ch17_rows_sifrei_153_156 as C, ch17_rows_sifrei_157_162 as D, ch17_rows_sifrei_163_166 as E, ch17_rows_sifrei_167_171 as F, ch17_rows_sifrei_172_178 as G, ch17_rows_onkelos_17 as H, ch17_rows_onkelos_18 as J, ch17_rows_outside as K
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S, **E.S, **F.S, **G.S}; R = {**H.R, **J.R}; SO = K.SO
print('ALL TYPED — Sifrei:', len(S), '| Onkelos:', len(R), '| outside:', len(SO))
print('  Sifrei == spine:', set(S) == set(I.READ_ROWS), '| Onkelos == SPAN:', sorted(R) == I.SPAN, '| outside == OUTSIDE:', sorted(SO) == sorted(I.OUTSIDE))
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()), Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()); rro = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks (spine, outside):', rr, rro, '| computed:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR}), sorted(I.PRIOR_READ))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == set(I.READ_ROWS) and sorted(R) == I.SPAN and sorted(SO) == sorted(I.OUTSIDE)
assert rr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR}) and rro == sorted(I.PRIOR_READ), (rr, rro)
print('THE FULL IMPORT CHECK GREEN')
