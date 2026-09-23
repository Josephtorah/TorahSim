# THE IMPORT CHECK of ALL EIGHT row files (sitting 13, RUN B2, 2026-09-22): one process, the ink imported once; the Sifrei set against READ_ROWS (99), the
# Onkelos rows against SPAN (23), the outside rows against OUTSIDE (10); the cuts' misses (FAIL) asserted empty; ch15_rows_check_a.py's form.
import ch15_ink as I
import ch15_rows_sifrei_111_116 as A, ch15_rows_sifrei_117_118 as B, ch15_rows_sifrei_119_123 as C, ch15_rows_sifrei_124_126 as D
import ch15_rows_onkelos_a as OA, ch15_rows_onkelos_b as OB, ch15_rows_outside_a as XA, ch15_rows_outside_b as XB
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S}; R = {**OA.R, **OB.R}; SO = {**XA.SO, **XB.SO}
byp = Counter(p for p, r in S)
print('RUN B2 TYPED — Sifrei rows:', len(S), '| by piska:', dict(sorted(byp.items())), '| Onkelos rows:', len(R), sorted(R)[0], sorted(R)[-1], '| outside rows:', sorted(SO))
print('  Sifrei == READ_ROWS:', sorted(S) == sorted(I.READ_ROWS), '| missing:', sorted(set(I.READ_ROWS) - set(S)), '| extra:', sorted(set(S) - set(I.READ_ROWS)))
print('  Onkelos == SPAN:', sorted(R) == sorted(I.SPAN), '| outside == OUTSIDE:', sorted(SO) == sorted(I.OUTSIDE))
print('  the verdicts:', dict(Counter(v for v, _ in S.values())), dict(Counter(v for v, _ in R.values())), dict(Counter(v for v, _ in SO.values())))
print('  the REREAD marks (case-blind) on the spine:', sorted(k for k in S if 'reread whole' in S[k][1].lower()), '| on the outside rows:', sorted(k for k in SO if 'reread whole' in SO[k][1].lower()))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert sorted(S) == sorted(I.READ_ROWS) and sorted(R) == sorted(I.SPAN) and sorted(SO) == sorted(I.OUTSIDE)
print('RUN B2 IMPORT CHECK GREEN')
