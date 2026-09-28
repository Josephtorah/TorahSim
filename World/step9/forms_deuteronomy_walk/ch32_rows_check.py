# THE IMPORT CHECK of the rows typed for chapter 32 (sitting 20, LEAN, 2026-09-28) — one process, the ink imported once. RUN 2's slice by default: Onkelos 32 (52),
# the eleven outside rows, PISKA 306 WHOLE (37); the later runs add their spine files by name on the command line (ch32_rows_p307_316 … ch32_rows_p339_341) and
# `--all` demands the whole spine (READ_ROWS, 249). Onkelos against SPAN (every row ends 'Fresh.'); the outside set against ch32_ink.OUTSIDE, its REREAD marks against
# PRIOR_READ and its fresh endings against FRESH; the spine slice against READ_ROWS restricted to the piskaot typed, its REREAD marks against SPINE_PRIOR (computed
# from the ledgers) restricted the same way, every other spine row ending 'Fresh.'; EXCLUDED empty; the cuts' misses (FAIL) asserted empty. Sitting 19's form
# (ch29_rows_check.py) made slice-aware. RUN FROM World/step9 with PYTHONPATH the scratchpad.
import sys, importlib
import ch32_ink as I
import ch32_rows_onkelos as ONK
import ch32_rows_outside as O
from collections import Counter
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
SPINE_MODS = ['ch32_rows_p306'] + ARGS
S = {}
for m in SPINE_MODS:
    mod = importlib.import_module(m); S.update(mod.S); print('spine file', m, ':', len(mod.S), 'rows', sorted({p for p, _ in mod.S}))
R = dict(ONK.R); SO = dict(O.SO)
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
print('  the cuts\' misses (FAIL):', len(I.FAIL), I.FAIL[:12])
assert not I.FAIL, I.FAIL
assert sorted(R) == I.SPAN and len(R) == 52
assert not [k for k, (v, t) in R.items() if not t.rstrip().endswith('Fresh.')], 'an Onkelos row not ending Fresh.'
assert sorted(S) == EXPECT_S, (sorted(set(EXPECT_S) - set(S)), sorted(set(S) - set(EXPECT_S)))
assert srr == sprior, (srr, sprior)
assert len(sfresh) + len(srr) == len(S) and not (set(sfresh) & set(srr)), 'a spine row neither Fresh. nor reread, or both'
assert set(SO) == set(I.OUTSIDE) and len(SO) == 11
assert rr == sorted(I.PRIOR_READ), (rr, sorted(I.PRIOR_READ))
assert fresh == sorted(I.FRESH), fresh
assert ex == sorted(I.EXCLUDED) == []
assert not [k for k, (v, t) in SO.items() if k in I.FRESH and 'reread whole' in t.lower()]
if '--all' in sys.argv: assert sorted(S) == I.READ_ROWS and len(S) == 249, len(S)
print('  bytes of prose:', sum(len(t.encode()) for _, t in R.values()) + sum(len(t.encode()) for _, t in S.values()) + sum(len(t.encode()) for _, t in SO.values()))
print('THE IMPORT CHECK GREEN —', 'RUN 2 slice' if not ARGS and '--all' not in sys.argv else ('THE WHOLE SPINE' if '--all' in sys.argv else 'slices ' + ' '.join(SPINE_MODS)))
