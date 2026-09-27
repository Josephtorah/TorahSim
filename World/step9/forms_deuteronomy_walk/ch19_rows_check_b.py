# THE IMPORT CHECK B of ALL the rows (sitting 16, LEAN, 2026-09-24; RUN 2): the nine Sifrei row files of chapters 19-21 (piskaot 179-221), the three Onkelos
# files (19, 20, 21), the outside file (eleven rows over the three chapters) — one process, the ink imported once; the counts by piska against the spine's;
# the cuts' misses (FAIL) asserted empty; every key inside the spine's rows; the REREAD marks as computed. Check A's form widened to the ten files (RUN 1's
# eight + RUN 2's five; the outside file counted once).
import ch19_ink as I
import ch19_rows_sifrei_179_183 as A, ch19_rows_sifrei_184_188 as B, ch19_rows_sifrei_189_190 as C, ch19_rows_sifrei_191_197 as D, ch19_rows_sifrei_198_204 as E
import ch19_rows_sifrei_205_210 as F, ch19_rows_sifrei_211_215 as G, ch19_rows_sifrei_216_218 as H2, ch19_rows_sifrei_219_221 as J2
import ch19_rows_onkelos_19 as H, ch19_rows_onkelos_20 as J, ch19_rows_onkelos_21 as K2, ch19_rows_outside as K
from collections import Counter
S = {**A.S, **B.S, **C.S, **D.S, **E.S, **F.S, **G.S, **H2.S, **J2.S}; R = {**H.R, **J.R, **K2.R}; SO = K.SO
byp = Counter(p for p, r in S)
print('THE SIFREI ROWS TYPED (chapters 19-21):', len(S), '| by piska:', dict(sorted(byp.items())))
CH = {p: (I.heads[p][0] if I.heads[p] else 19) for p in byp}   # the headless piskaot (183, 187) are chapter 19's
print('  by chapter:', {c: sum(n for p, n in byp.items() if CH[p] == c) for c in (19, 20, 21)})
want = set(I.READ_ROWS)
print('  typed == spine 179-221:', set(S) == want, '| missing:', sorted(want - set(S)), '| extra:', sorted(set(S) - want))
print('  Onkelos typed:', len(R), '== SPAN:', sorted(R) == sorted(I.SPAN), '| outside typed:', len(SO), '== OUTSIDE:', sorted(SO) == sorted(I.OUTSIDE))
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()), Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()); rro = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks (spine, outside):', rr, rro, '| computed:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR}), sorted(I.PRIOR_READ))
print('  the cuts\' misses (FAIL):', I.FAIL)
print('  the rows\' sizes: spine chars', sum(len(t) for _, t in S.values()), '| Onkelos chars', sum(len(t) for _, t in R.values()), '| outside chars', sum(len(t) for _, t in SO.values()))
assert not I.FAIL, I.FAIL
assert set(S) == want and len(S) == 260 and sorted(R) == sorted(I.SPAN) and len(R) == 64 and sorted(SO) == sorted(I.OUTSIDE)
assert rr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR}) and rro == sorted(I.PRIOR_READ), (rr, rro)
print('THE IMPORT CHECK B GREEN — every row of the three chapters typed, every cut found')
