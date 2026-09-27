# THE IMPORT CHECK over ALL the rows of sitting 17 (LEAN, 2026-09-26): the fourteen Sifrei row files of chapters 22-25 (piskaot 222-296), the four Onkelos files
# (22, 23, 24, 25), the outside file (fourteen rows) — one process, the ink imported once; the counts by chapter against the spine's; the cuts' misses (FAIL)
# asserted empty; every key inside the spine's rows; the REREAD marks as computed (the twelve spine rows and the ten outside rows). Checks A and B's form.
import ch22_ink as I
import ch22_rows_sifrei_222_226 as A1, ch22_rows_sifrei_227_230 as A2, ch22_rows_sifrei_231_236 as A3, ch22_rows_sifrei_237_241 as A4, ch22_rows_sifrei_242_245 as A5
import ch22_rows_sifrei_246_253 as B1, ch22_rows_sifrei_254_261 as B2, ch22_rows_sifrei_262_267 as B3, ch22_rows_sifrei_268_270 as B4, ch22_rows_sifrei_271_277 as B5, ch22_rows_sifrei_278_285 as B6
import ch22_rows_sifrei_286_287 as C1, ch22_rows_sifrei_288_291 as C2, ch22_rows_sifrei_292_296 as C3
import ch22_rows_onkelos_22 as H1, ch22_rows_onkelos_23 as H2, ch22_rows_onkelos_24 as H3, ch22_rows_onkelos_25 as H4, ch22_rows_outside as K
from collections import Counter
MODS = [A1, A2, A3, A4, A5, B1, B2, B3, B4, B5, B6, C1, C2, C3]
S = {}
for m in MODS:
    assert not set(m.S) & set(S), 'a key typed twice'; S.update(m.S)
R = {**H1.R, **H2.R, **H3.R, **H4.R}; SO = K.SO
byc = Counter(I.HEAD_CH[p] if hasattr(I, 'HEAD_CH') else 0 for p, r in S)
want = set(I.READ_ROWS)
print('THE SIFREI ROWS TYPED (chapters 22-25):', len(S), 'in', len(MODS), 'files | typed == spine 222-296:', set(S) == want, '| missing:', sorted(want - set(S)), '| extra:', sorted(set(S) - want))
print('  by run:', sum(len(m.S) for m in MODS[:5]), sum(len(m.S) for m in MODS[5:11]), sum(len(m.S) for m in MODS[11:]))
print('  Onkelos typed:', len(R), '== SPAN:', sorted(R) == sorted(I.SPAN), '| outside typed:', len(SO), '== OUTSIDE:', sorted(SO) == sorted(I.OUTSIDE))
print('  the verdicts:', Counter(v for v, _ in S.values()), Counter(v for v, _ in R.values()), Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower()); rro = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks (spine, outside):', rr, rro, '| computed:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR}), sorted(I.PRIOR_READ))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(S) == want and len(S) == 434 and sorted(R) == sorted(I.SPAN) and len(R) == 96 and sorted(SO) == sorted(I.OUTSIDE) and len(SO) == 14
assert rr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR}) and rro == sorted(I.PRIOR_READ), (rr, rro)
print('THE IMPORT CHECK C GREEN — every row of the four chapters typed and cut')
