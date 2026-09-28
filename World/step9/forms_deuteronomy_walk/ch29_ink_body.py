# ---- THE ASSERTS TYPED FROM THE PRINTS (block a: the dumps' and the split's — the shelf by position, the divisions, the citations; the outside rows' facts COMPUTED) ----
DT = ('Deut',)
def PL(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def HB0(p, r): return PL(clean(sif_he[p - 1][r - 1]))
def ARM(c, v): return [PL(unicodedata.normalize('NFKC', x)).strip('.:()') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
# THE SHELF BY POSITION — the spine ON chapter 31 alone: 304 on 31:14 and 305 HEADLESS; NO piska heads in 29 and 30 (the Sifrei runs 303 on 26:15 to 304 on 31:14); 306 on 32:1 after; the heads by chapter and the window 295-320 as the dumps printed them
assert NV == {29: 28, 30: 20, 31: 30} and VC[28] == 69 and VC[32] == 52 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[29], HC[30], HC[31]) == (0, 0, 1) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 14), (34, 1)], sorted(HC.items())
assert {p: heads[p] for p in range(295, 321)} == {295: None, 296: (25, 17), 297: (26, 1), 298: None, 299: None, 300: (26, 4), 301: (26, 5), 302: (26, 12), 303: None, 304: (31, 14), 305: None, 306: (32, 1), 307: (32, 4), 308: (32, 5), 309: (32, 6), 310: (32, 7), 311: (32, 8), 312: (32, 9), 313: (32, 10), 314: (32, 11), 315: (32, 12), 316: (32, 13), 317: (32, 14), 318: (32, 15), 319: (32, 18), 320: (32, 19)}, {p: heads[p] for p in range(295, 321)}
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {29: [], 30: [], 31: [14]}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {29: list(range(1, 29)), 30: list(range(1, 21)), 31: [v for v in range(1, 31) if v != 14]}, NOHEAD   # chapters 29 and 30 whole without a piska; 31:1-13 the charge, the reading and the ark HEADLESS; 31:15-30 inside 304-305 or uncited
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and [sum(SPINE_ROWS[p] for p in PISKAOT_BY[c]) for c in CHS] == [0, 0, 8] and sum(SPINE_ROWS.values()) == 8 and len(READ_ROWS) == 8 and len(PISKAOT) == 2 and READ_ROWS[0] == (304, 1) and READ_ROWS[-1] == (305, 6)
# THE TAILS AND THE EDGES (the split's print): 303's rows carry no word of 31:14; 303:20 cites 26:15; 304:1 opens with 31:14's citation; 305:1 opens with Numbers 27:18's; 305:6 ends with Joshua weeping; 306:1 opens with 32:1's
assert not any(w in HB0(303, r) for r in range(1, 21) for w in ('הן קרבו ימיך', 'קרבו ימיך למות')) and HB0(303, 20).startswith('(דברים כו טו) השקיפה ממעון קדשך') and HB0(304, 1).startswith('(דברים לא יד) ויאמר ה׳ אל משה הן קרבו ימיך למות') and HB0(305, 1).startswith('(במדבר כז יח) ויאמר ה׳ אל משה קח לך את יהושע בן נון') and HB0(305, 6).startswith('וכיון שמת משה היה יהושע בוכה') and HB0(306, 1).startswith('(דברים לב א) האזינו השמים ואדברה')
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'your days are dwindling' in clean(sif[303][0]) and 'Take for yourself Joshua' in clean(sif[304][0]) and 'Lend an ear, Heavens' in clean(sif[305][0])   # the English rows open with the translator's apparatus (H:293-294; JN2:289-290) before the text — the first pass read [:160] and fell on 305:1 (retyped from the print), (clean(sif[303][0])[:100], clean(sif[304][0])[:100])
# THE CITATIONS PARSED FROM THE THREE DUMPS' PRINTS (the instrument's own lists read back): the row-citations per file, the union, the outside sets; the divisions
import ast as _ast
_DUMP = {}; _HE = {}; _EN = {}
for _c in CHS:
    _t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'ch{_c}_dump0.out'), encoding='utf-8').read()
    _HE[_c] = _ast.literal_eval(re.search(r'^  HE rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1)); _EN[_c] = _ast.literal_eval(re.search(r'^  EN rows citing Deut %d[^:]*: \d+ (\[.*\])$' % _c, _t, re.M).group(1))
    _un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1))
    _two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-31: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
    _mis = _ast.literal_eval(re.search(r'verses whose store token count differs from the DB: (\[.*?\])$', _t, re.M).group(1))
    _DUMP[_c] = (len(_HE[_c]), len(_EN[_c]), _un, _out, tuple(int(x) for x in _two.groups()[:3]), _two.group(4), _cost, _mis)
assert {c: v[:3] for c, v in _DUMP.items()} == {29: (4, 4, 4), 30: (2, 4, 3), 31: (16, 23, 17)}, {c: v[:3] for c, v in _DUMP.items()}
assert {c: v[4] for c, v in _DUMP.items()} == {29: (28, 28, 28), 30: (20, 20, 20), 31: (30, 30, 30)} and {c: v[6] for c, v in _DUMP.items()} == {29: 19, 30: 18, 31: 30} and all(v[5] == '[(5, 30, 33)]' for v in _DUMP.values()), 'THE TWO DIVISIONS: the identity in all three; chapter 5 the book\'s one split'
assert {c: v[7] for c, v in _DUMP.items()} == {29: [(29, 22, 25, 24)], 30: [], 31: []}, 'THE STORE = THE DB except at 29:22 (the store one token more — Sodom and Gomorrah, Admah and Zeboiim)'
assert _DUMP[29][3] == [(43, 29), (48, 9), (148, 8), (345, 2)] and _DUMP[30][3] == [(53, 1), (306, 2), (306, 15)] and len(_DUMP[31][3]) == 16 and {(305, 2), (305, 6)} <= set(_DUMP[31][3])
# THE OUTSIDE ROWS' FACTS COMPUTED from the dumps' lists: the verses each row cites (the DB's numbering), the heads of their piskaot, the prior reads from the ledgers, the fresh rows
CITED = {}
for _c in CHS:
    for _p, _r, _e, _dbv in _HE[_c] + _EN[_c]:
        if (_p, _r) in OUTSIDE:
            for _d in _dbv: CITED.setdefault((_p, _r), set()).add((_c, _d))
CITED = {k: sorted(v) for k, v in sorted(CITED.items())}
assert sorted(CITED) == OUTSIDE, (sorted(set(OUTSIDE) - set(CITED)), sorted(set(CITED) - set(OUTSIDE)))
assert CITED[(48, 9)] == [(29, 9), (31, 21)] and CITED[(306, 15)] == [(30, 19), (31, 19), (31, 21)] and CITED[(43, 29)] == [(29, 27)] and CITED[(1, 1)] == [(31, 9), (31, 22)], (CITED[(48, 9)], CITED[(306, 15)], CITED[(1, 1)])
HEADS_ON = {p: heads[p] for p in sorted({p for p, _ in OUTSIDE})}
assert HEADS_ON[1] == (1, 1) and HEADS_ON[2] == (1, 2) and HEADS_ON[29] == (3, 26) and HEADS_ON[43] == (11, 15) and HEADS_ON[48] == (11, 22) and HEADS_ON[53] == (11, 26) and HEADS_ON[109] == (14, 28) and HEADS_ON[111] == (15, 1) and HEADS_ON[148] == (17, 2) and HEADS_ON[157] == (17, 15) and HEADS_ON[160] == (17, 18) and HEADS_ON[302] == (26, 12) and HEADS_ON[306] == (32, 1) and HEADS_ON[318] == (32, 15) and HEADS_ON[334] == (32, 44) and HEADS_ON[345] == (33, 4) and HEADS_ON[357] == (34, 1), HEADS_ON   # 334 heads on 32:44 (the song's close), not on 33 — the first pass guessed the chapter, the print corrected it
_TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{_TRI}/{f}', encoding='utf-8').read() for f in os.listdir(_TRI) if f.endswith('.md') and os.path.isfile(f'{_TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
PRIOR_READ = {}
for f, t in LED.items():
    for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t):
        if (int(a), int(b)) in OUTSIDE: PRIOR_READ.setdefault((int(a), int(b)), []).append(f)
PRIOR_READ = {k: sorted(set(v)) for k, v in sorted(PRIOR_READ.items())}
FRESH = [k for k in OUTSIDE if k not in PRIOR_READ]
assert SPINE_PRIOR == [], SPINE_PRIOR   # no spine row of 304-305 read before (the Sifrei's rows on Moses' death and Joshua's commission are new to the ledgers)
assert FRESH == [(306, 2), (306, 15), (334, 1), (345, 2), (357, 28)] and (318, 1) in PRIOR_READ, (FRESH, PRIOR_READ.get((318, 1)))   # FIVE fresh rows from Haazinu's and Vezot Habrachah's piskaot; 318:1 (on 32:15) READ BEFORE — the first pass counted it fresh, the ledgers corrected it
