# THE IMPORT CHECK of the rows typed in RUN 2 (sitting 18, LEAN, 2026-09-26): the twenty-six outside rows, Onkelos 27 (one file) and Onkelos 28 (three files) — one
# process, the ink imported once; the outside set against ch26_ink.OUTSIDE, the REREAD marks against PRIOR_READ (computed from the ledgers), the EXCLUDED verdicts
# against ch26_ink.EXCLUDED, Onkelos 27-28 against SPAN; the cuts' misses (FAIL) asserted empty. Sitting 17's form (ch22_rows_check_b.py), cut to RUN 2's files.
import ch26_ink as I
import ch26_rows_outside as O
import ch26_rows_onkelos_27 as H27, ch26_rows_onkelos_28_a as A, ch26_rows_onkelos_28_b as B, ch26_rows_onkelos_28_c as C
from collections import Counter
SO = dict(O.SO); R = {**H27.R, **A.R, **B.R, **C.R}
print('THE OUTSIDE ROWS TYPED:', len(SO), '| == OUTSIDE:', set(SO) == set(I.OUTSIDE), '| missing:', sorted(set(I.OUTSIDE) - set(SO)), '| extra:', sorted(set(SO) - set(I.OUTSIDE)))
print('  the verdicts:', Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks:', len(rr), '| computed PRIOR_READ:', len(I.PRIOR_READ), '| equal:', rr == sorted(I.PRIOR_READ))
fresh = sorted(k for k, (v, t) in SO.items() if t.rstrip().endswith('Fresh.'))
print('  the fresh rows:', fresh, '| ink FRESH:', I.FRESH)
ex = sorted(k for k, (v, _) in SO.items() if v == 'EXCLUDED')
print('  the EXCLUDED rows:', ex, '| ink EXCLUDED:', sorted(I.EXCLUDED))
want = [(c, v) for c, v in I.SPAN if c in (27, 28)]
print('ONKELOS TYPED (27-28):', len(R), '| by chapter:', dict(Counter(c for c, v in R)), '| == SPAN 27-28:', sorted(R) == want)
print('  the verdicts:', Counter(v for v, _ in R.values()))
print('  the cuts\' misses (FAIL):', I.FAIL)
assert not I.FAIL, I.FAIL
assert set(SO) == set(I.OUTSIDE) and len(SO) == 26
assert rr == sorted(I.PRIOR_READ), (rr, sorted(I.PRIOR_READ))
assert fresh == sorted(I.FRESH), fresh
assert ex == sorted(I.EXCLUDED), (ex, I.EXCLUDED)
assert sorted(R) == want and len(R) == 95
print('  bytes of prose:', sum(len(t.encode()) for _, t in SO.values()) + sum(len(t.encode()) for _, t in R.values()))
print('THE RUN-2 IMPORT CHECK GREEN')
