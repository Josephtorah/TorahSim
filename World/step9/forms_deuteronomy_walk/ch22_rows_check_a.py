# THE IMPORT CHECK of the rows typed in RUN 1 (sitting 17, LEAN, 2026-09-25): the five Sifrei row files of chapter 22 (piskaot 222-245), the Onkelos file (22),
# the outside file (fourteen rows over the four chapters) — one process, the ink imported once; the counts by piska against the spine's; the cuts' misses (FAIL)
# asserted empty; every key inside the spine's rows; the REREAD marks as computed. Sitting 16's form (ch19_rows_check_a.py), cut to the run's files.
import ch22_ink as I
import ch22_rows_sifrei_222_226 as A, ch22_rows_sifrei_227_230 as B, ch22_rows_sifrei_231_236 as C, ch22_rows_sifrei_237_241 as D, ch22_rows_sifrei_242_245 as E, ch22_rows_onkelos_22 as H, ch22_rows_outside as K
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S, **E.S}; R = dict(H.R); SO = K.SO
byp = Counter(p for p, r in S)
print('THE SIFREI ROWS TYPED (chapter 22):', len(S), '| by piska:', dict(sorted(byp.items())))
want = {(p, r) for p, r in I.READ_ROWS if p <= 245}
print('  typed == spine 222-245:', set(S) == want, '| missing:', sorted(want - set(S)), '| extra:', sorted(set(S) - want))
print('  Onkelos typed:', len(R), '== SPAN 22:', sorted(R) == [(c, v) for c, v in I.SPAN if c == 22], '| outside typed:', len(SO), '== OUTSIDE:', sorted(SO) == sorted(I.OUTSIDE))
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()), Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()); rro = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks (spine, outside):', rr, rro, '| computed:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR if p <= 245}), sorted(I.PRIOR_READ))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == want and len(S) == 157 and sorted(R) == [(c, v) for c, v in I.SPAN if c == 22] and sorted(SO) == sorted(I.OUTSIDE)
assert rr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR if p <= 245}) and rro == sorted(I.PRIOR_READ), (rr, rro)
print('THE RUN-1 IMPORT CHECK GREEN')
