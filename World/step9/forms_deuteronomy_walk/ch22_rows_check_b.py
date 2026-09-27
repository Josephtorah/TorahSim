# THE IMPORT CHECK of the rows typed in RUN 2 (sitting 17, LEAN, 2026-09-26): the six Sifrei row files of chapters 23 and 24 (piskaot 246-285), the two
# Onkelos files (23, 24) — one process, the ink imported once; the counts by piska against the spine's; the cuts' misses (FAIL) asserted empty; every key inside
# the spine's rows; the REREAD marks as computed. RUN 1's check A cut to RUN 2's files.
import ch22_ink as I
import ch22_rows_sifrei_246_253 as A, ch22_rows_sifrei_254_261 as B, ch22_rows_sifrei_262_267 as C, ch22_rows_sifrei_268_270 as D, ch22_rows_sifrei_271_277 as E, ch22_rows_sifrei_278_285 as F
import ch22_rows_onkelos_23 as H, ch22_rows_onkelos_24 as J
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S, **E.S, **F.S}; R = {**H.R, **J.R}
byp = Counter(p for p, r in S)
print('THE SIFREI ROWS TYPED (chapters 23-24):', len(S), '| by piska:', dict(sorted(byp.items())))
want = {(p, r) for p, r in I.READ_ROWS if 246 <= p <= 285}
print('  typed == spine 246-285:', set(S) == want, '| missing:', sorted(want - set(S)), '| extra:', sorted(set(S) - want))
print('  by chapter:', sum(1 for p, r in S if p <= 267), sum(1 for p, r in S if p >= 268))
print('  Onkelos typed:', len(R), '== SPAN 23-24:', sorted(R) == [(c, v) for c, v in I.SPAN if c in (23, 24)])
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower())
print('  the REREAD marks:', rr, '| computed:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR if 246 <= p <= 285}))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == want and len(S) == 198 and sorted(R) == [(c, v) for c, v in I.SPAN if c in (23, 24)] and len(R) == 48
assert rr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR if 246 <= p <= 285}), rr
print('THE RUN-2 IMPORT CHECK GREEN')
