# THE IMPORT CHECK of every row typed in RUN 2 (sitting 19, LEAN, 2026-09-27): Onkelos 29, 30, 31 (four files — 78), the spine 304-305 (8), the nineteen outside
# rows — one process, the ink imported once; Onkelos against SPAN, the spine against READ_ROWS, the outside set against ch29_ink.OUTSIDE, the REREAD marks against
# PRIOR_READ and SPINE_PRIOR (computed from the ledgers), the fresh endings against FRESH, EXCLUDED empty; the cuts' misses (FAIL) asserted empty. Sitting 18's
# forms (ch26_rows_check_a.py, ch26_rows_check_b.py) joined — one run, the rows all typed in RUN 2.
import ch29_ink as I
import ch29_rows_onkelos_29 as H29, ch29_rows_onkelos_30 as H30, ch29_rows_onkelos_31_a as H31A, ch29_rows_onkelos_31_b as H31B
import ch29_rows_sifrei_304_305 as SPN
import ch29_rows_outside as O
from collections import Counter
R = {**H29.R, **H30.R, **H31A.R, **H31B.R}; S = dict(SPN.S); SO = dict(O.SO)
print('ONKELOS TYPED:', len(R), '| by chapter:', dict(Counter(c for c, v in R)), '| == SPAN:', sorted(R) == I.SPAN, '| verdicts:', Counter(v for v, _ in R.values()))
print('THE SPINE TYPED:', len(S), '| by piska:', dict(Counter(p for p, r in S)), '| == READ_ROWS:', sorted(S) == I.READ_ROWS, '| verdicts:', Counter(v for v, _ in S.values()))
srr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower())
print('  the spine REREAD marks:', srr, '| computed SPINE_PRIOR:', sorted({(p, r) for _, p, r in I.SPINE_PRIOR}))
print('THE OUTSIDE ROWS TYPED:', len(SO), '| == OUTSIDE:', set(SO) == set(I.OUTSIDE), '| missing:', sorted(set(I.OUTSIDE) - set(SO)), '| extra:', sorted(set(SO) - set(I.OUTSIDE)), '| verdicts:', Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks:', len(rr), '| computed PRIOR_READ:', len(I.PRIOR_READ), '| equal:', rr == sorted(I.PRIOR_READ))
fresh = sorted(k for k, (v, t) in SO.items() if t.rstrip().endswith('Fresh.'))
print('  the fresh rows:', fresh, '| ink FRESH:', I.FRESH)
ex = sorted(k for k, (v, _) in SO.items() if v == 'EXCLUDED')
print('  the EXCLUDED rows:', ex, '| ink EXCLUDED:', sorted(I.EXCLUDED))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert sorted(R) == I.SPAN and len(R) == 78
assert sorted(S) == I.READ_ROWS and len(S) == 8 and srr == sorted({(p, r) for _, p, r in I.SPINE_PRIOR}) == []
assert set(SO) == set(I.OUTSIDE) and len(SO) == 19
assert rr == sorted(I.PRIOR_READ), (rr, sorted(I.PRIOR_READ))
assert fresh == sorted(I.FRESH), fresh
assert ex == sorted(I.EXCLUDED) == []
assert not [k for k, (v, t) in SO.items() if k in I.FRESH and 'reread whole' in t.lower()] and not [k for k, (v, t) in R.items() if not t.rstrip().endswith('Fresh.')] and not [k for k, (v, t) in S.items() if not t.rstrip().endswith('Fresh.')]
print('  bytes of prose:', sum(len(t.encode()) for _, t in R.values()) + sum(len(t.encode()) for _, t in S.values()) + sum(len(t.encode()) for _, t in SO.values()))
print('THE RUN-2 IMPORT CHECK GREEN')
