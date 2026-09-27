# THE IMPORT CHECK of the seven Sifrei row files (sitting 15, LEAN, 2026-09-24): one process, the ink imported once; the counts by piska against the spine's;
# the cuts' misses (FAIL) asserted empty; every key inside the spine's rows. Sitting 14's form over seven files.
import ch17_ink as I
import ch17_rows_sifrei_147_149 as A, ch17_rows_sifrei_150_152 as B, ch17_rows_sifrei_153_156 as C, ch17_rows_sifrei_157_162 as D, ch17_rows_sifrei_163_166 as E, ch17_rows_sifrei_167_171 as F, ch17_rows_sifrei_172_178 as G
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S, **E.S, **F.S, **G.S}
byp = Counter(p for p, r in S)
print('THE SIFREI ROWS TYPED:', len(S), '| by piska:', dict(sorted(byp.items())))
spine_rows = set(I.READ_ROWS)
print('  typed == spine:', set(S) == spine_rows, '| missing:', sorted(spine_rows - set(S)), '| extra:', sorted(set(S) - spine_rows))
print('  the verdicts:', Counter(v for v, _ in S.values()), '| the REREAD marks:', sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == spine_rows and len(S) == 181
print('THE SIFREI IMPORT CHECK GREEN')
