# THE IMPORT CHECK of the four Sifrei row files (sitting 14, LEAN, 2026-09-23): one process, the ink imported once; the counts by piska against the spine's;
# the cuts' misses (FAIL) asserted empty; every key inside the spine's rows.
import ch16_ink as I
import ch16_rows_sifrei_127_131 as A, ch16_rows_sifrei_132_136 as B, ch16_rows_sifrei_137_142 as C, ch16_rows_sifrei_143_146 as D
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S}
byp = Counter(p for p, r in S)
print('THE SIFREI ROWS TYPED:', len(S), '| by piska:', dict(sorted(byp.items())))
spine_rows = set(I.READ_ROWS)
print('  typed == spine:', set(S) == spine_rows, '| missing:', sorted(spine_rows - set(S)), '| extra:', sorted(set(S) - spine_rows))
print('  the verdicts:', Counter(v for v, _ in S.values()), '| the REREAD marks:', sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == spine_rows and len(S) == 111
print('THE SIFREI IMPORT CHECK GREEN')
