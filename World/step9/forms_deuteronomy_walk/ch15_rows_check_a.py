# THE IMPORT CHECK of RUN B1's four row files (sitting 13, 2026-09-22): one process, the ink imported once; the counts by piska read against the spine's;
# the cuts' misses (FAIL) asserted empty; every Sifrei key inside the spine's rows and every outside key inside OUTSIDE.
import ch15_ink as I
import ch15_rows_sifrei_111_116 as A, ch15_rows_sifrei_117_118 as B, ch15_rows_onkelos_a as C, ch15_rows_outside_a as D
from collections import Counter
S = {**A.S, **B.S}
byp = Counter(p for p, r in S)
print('RUN B1 TYPED — Sifrei rows:', len(S), '| by piska:', dict(sorted(byp.items())), '| Onkelos rows:', sorted(C.R), '| outside rows:', sorted(D.SO))
spine_rows = {(p, r) for p in range(111, 119) for r in range(1, len(I.sif_he[p - 1]) + 1)}
print('  the spine rows of 111-118 in the export:', len(spine_rows), '| typed == spine:', set(S) == spine_rows, '| missing:', sorted(spine_rows - set(S)), '| extra:', sorted(set(S) - spine_rows))
print('  the outside keys typed against OUTSIDE:', sorted(D.SO), 'all in OUTSIDE:', all(k in {(p, r) for p, r, *_ in I.OUTSIDE} or k in set(I.OUTSIDE) for k in D.SO) if hasattr(I, 'OUTSIDE') else 'no OUTSIDE')
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in C.R.values()), Counter(v for v, _ in D.SO.values()))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == spine_rows and len(C.R) == 11 and len(D.SO) == 4
print('RUN B1 IMPORT CHECK GREEN')
