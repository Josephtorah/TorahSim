# THE IMPORT CHECK of the rows typed in RUN 1 (sitting 16, LEAN, 2026-09-24): the five Sifrei row files of chapters 19-20 (piskaot 179-204), the two Onkelos
# files (19, 20), the outside file (eleven rows over the three chapters) — one process, the ink imported once; the counts by piska against the spine's;
# the cuts' misses (FAIL) asserted empty; every key inside the spine's rows; the REREAD marks as computed. Sitting 15's form, cut to the run's files.
import ch19_ink as I
import ch19_rows_sifrei_179_183 as A, ch19_rows_sifrei_184_188 as B, ch19_rows_sifrei_189_190 as C, ch19_rows_sifrei_191_197 as D, ch19_rows_sifrei_198_204 as E, ch19_rows_onkelos_19 as H, ch19_rows_onkelos_20 as J, ch19_rows_outside as K
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S, **E.S}; R = {**H.R, **J.R}; SO = K.SO
byp = Counter(p for p, r in S)
print('THE SIFREI ROWS TYPED (chapters 19-20):', len(S), '| by piska:', dict(sorted(byp.items())))
want = {(p, r) for p, r in I.READ_ROWS if p <= 204}
print('  typed == spine 179-204:', set(S) == want, '| missing:', sorted(want - set(S)), '| extra:', sorted(set(S) - want))
print('  Onkelos typed:', len(R), '== SPAN 19-20:', sorted(R) == [(c, v) for c, v in I.SPAN if c <= 20], '| outside typed:', len(SO), '== OUTSIDE:', sorted(SO) == sorted(I.OUTSIDE))
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()), Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()); rro = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks (spine, outside):', rr, rro, '| computed:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR if p <= 204}), sorted(I.PRIOR_READ))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == want and len(S) == 140 and sorted(R) == [(c, v) for c, v in I.SPAN if c <= 20] and sorted(SO) == sorted(I.OUTSIDE)
assert rr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR if p <= 204}) and rro == sorted(I.PRIOR_READ), (rr, rro)
print('THE RUN-1 IMPORT CHECK GREEN')
