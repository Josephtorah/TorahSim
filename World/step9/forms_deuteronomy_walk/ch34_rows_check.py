# THE IMPORT CHECK of the rows typed for chapter 34 (sitting 22, LEAN, 2026-09-30) — one process, the ink imported once. ONE slice: Onkelos 34 (12), the two outside
# rows, PISKA 357 WHOLE (44), and the testing shelf's one Tosefta row (Sotah 4:4 — read whole at this reading by 21b's leaving). Onkelos against SPAN (every row ends
# 'Fresh.'); the outside set against ch34_ink.OUTSIDE, its REREAD marks against PRIOR_READ and its fresh endings against FRESH; the spine against READ_ROWS, its REREAD
# marks against SPINE_PRIOR (computed from the ledgers), every other spine row ending 'Fresh.'; the Tosefta row against TOSEFTA_ROWS, ending 'Fresh.'; EXCLUDED empty;
# the cuts' misses (FAIL — the Sifrei's SP_, the verses' H and A, the Tosefta's TP_) asserted empty. Sitting 21's form (ch33_rows_check.py), the names and the counts
# moved, the Tosefta row added. RUN FROM World/step9 with PYTHONPATH the scratchpad.
import sys, importlib
import ch34_ink as I
import ch34_rows_onkelos as ONK
import ch34_rows_outside as O
from collections import Counter
SPINE_MODS = ['ch34_rows_p357']
S = {}
for m in SPINE_MODS:
    mod = importlib.import_module(m); S.update(mod.S); print('spine file', m, ':', len(mod.S), 'rows', sorted({p for p, _ in mod.S}))
R = dict(ONK.R); SO = dict(O.SO); TO = dict(O.TO)
PISK = sorted({p for p, _ in S})
EXPECT_S = [k for k in I.READ_ROWS if k[0] in PISK]
print('ONKELOS TYPED:', len(R), '| == SPAN:', sorted(R) == I.SPAN, '| verdicts:', Counter(v for v, _ in R.values()))
print('THE SPINE TYPED:', len(S), '| piskaot:', PISK, '| by piska:', dict(sorted(Counter(p for p, r in S).items())), '| == READ_ROWS on these piskaot:', sorted(S) == EXPECT_S, '| missing:', sorted(set(EXPECT_S) - set(S)), '| extra:', sorted(set(S) - set(EXPECT_S)), '| verdicts:', Counter(v for v, _ in S.values()))
srr = sorted(k for k, (v, t) in S.items() if 'reread whole' in t.lower())
sprior = sorted({(p, r) for _, p, r in I.SPINE_PRIOR if p in PISK})
print('  the spine REREAD marks:', len(srr), srr, '| computed SPINE_PRIOR on these piskaot:', len(sprior), '| equal:', srr == sprior)
sfresh = sorted(k for k, (v, t) in S.items() if t.rstrip().endswith('Fresh.'))
print('  the spine fresh rows:', len(sfresh), '| + reread == typed:', len(sfresh) + len(srr) == len(S), '| overlap:', sorted(set(sfresh) & set(srr)))
print('THE OUTSIDE ROWS TYPED:', len(SO), '| == OUTSIDE:', set(SO) == set(I.OUTSIDE), '| missing:', sorted(set(I.OUTSIDE) - set(SO)), '| extra:', sorted(set(SO) - set(I.OUTSIDE)), '| verdicts:', Counter(v for v, _ in SO.values()))
rr = sorted(k for k, (v, t) in SO.items() if 'reread whole' in t.lower())
print('  the REREAD marks:', len(rr), '| computed PRIOR_READ:', len(I.PRIOR_READ), '| equal:', rr == sorted(I.PRIOR_READ))
fresh = sorted(k for k, (v, t) in SO.items() if t.rstrip().endswith('Fresh.'))
print('  the fresh rows:', fresh, '| ink FRESH:', I.FRESH)
ex = sorted(k for k, (v, _) in SO.items() if v == 'EXCLUDED')
print('  the EXCLUDED rows:', ex, '| ink EXCLUDED:', sorted(I.EXCLUDED))
print('THE TOSEFTA ROW TYPED:', sorted(TO), '| == TOSEFTA_ROWS:', sorted(TO) == sorted(I.TOSEFTA_ROWS), '| verdicts:', Counter(v for v, _ in TO.values()), '| ends Fresh.:', all(t.rstrip().endswith('Fresh.') for _, t in TO.values()), '| Hebrew bytes', len(O.TOS_HE.encode()), 'English', len(O.TOS_EN.encode()))
print('  the cuts\' misses (FAIL):', len(I.FAIL), I.FAIL[:12])
CLAIMS = Counter(); import re as _re
for d in (R, S, SO, TO):
    for _, t in d.values(): CLAIMS.update(_re.findall(r'\bDV34-\d\d\b', t))
print('  the claim ids named in the rows:', dict(sorted(CLAIMS.items())), '| every row names exactly one:', all(len(set(_re.findall(r'\bDV34-\d\d\b', t))) == 1 for d in (R, S, SO, TO) for _, t in d.values()))
assert not I.FAIL, I.FAIL
assert sorted(R) == I.SPAN and len(R) == 12
assert not [k for k, (v, t) in R.items() if not t.rstrip().endswith('Fresh.')], 'an Onkelos row not ending Fresh.'
assert sorted(S) == EXPECT_S == I.READ_ROWS and len(S) == 44, (sorted(set(EXPECT_S) - set(S)), sorted(set(S) - set(EXPECT_S)))
assert srr == sprior == [(357, 27), (357, 28), (357, 40), (357, 44)], (srr, sprior)
assert len(sfresh) + len(srr) == len(S) and not (set(sfresh) & set(srr)), 'a spine row neither Fresh. nor reread, or both'
assert set(SO) == set(I.OUTSIDE) and len(SO) == 2
assert rr == sorted(I.PRIOR_READ), (rr, sorted(I.PRIOR_READ))
assert fresh == sorted(I.FRESH) == [], fresh
assert ex == sorted(I.EXCLUDED) == []
assert sorted(TO) == sorted(I.TOSEFTA_ROWS) == [('Sotah', 4, 4)] and all(t.rstrip().endswith('Fresh.') for _, t in TO.values())
assert all(len(set(_re.findall(r'\bDV34-\d\d\b', t))) == 1 for d in (R, S, SO, TO) for _, t in d.values()) and sorted(CLAIMS) == [f'DV34-0{i}' for i in range(1, 7)], sorted(CLAIMS)
print('  bytes of prose:', sum(len(t.encode()) for d in (R, S, SO, TO) for _, t in d.values()))
print('THE IMPORT CHECK GREEN — THE WHOLE SPINE (one slice), Onkelos, the outside rows and the Tosefta row')
