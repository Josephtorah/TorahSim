# ---- THE ASSERTS TYPED FROM THE PRINTS (block a: the dump's and the split's — the shelf by position, the divisions, the citations; the outside rows' facts COMPUTED) ----
DT = ('Deut',)
def PL(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def HB0(p, r): return PL(clean(sif_he[p - 1][r - 1]))
def ARM(c, v): return [PL(unicodedata.normalize('NFKC', x)).strip('.:()') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
# THE SHELF BY POSITION — THE SPINE IN FORCE on chapter 32: thirty-six heads 306-341 (the dump's window 300-345); 305 headless before, 342 headless after; the heads by chapter as sitting 19's dumps printed them (the same table)
assert NV == {32: 52} and VC[31] == 30 and VC[33] == 29 and VC[34] == 12 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[31], HC[32], HC[33], HC[34]) == (1, 36, 14, 1) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 14), (34, 1)], sorted(HC.items())
WIN = {300: (26, 4), 301: (26, 5), 302: (26, 12), 303: None, 304: (31, 14), 305: None, 306: (32, 1), 307: (32, 4), 308: (32, 5), 309: (32, 6), 310: (32, 7), 311: (32, 8), 312: (32, 9), 313: (32, 10), 314: (32, 11), 315: (32, 12), 316: (32, 13), 317: (32, 14), 318: (32, 15), 319: (32, 18), 320: (32, 19), 321: (32, 23), 322: (32, 26), 323: (32, 29), 324: (32, 34), 325: (32, 35), 326: (32, 36), 327: (32, 37), 328: (32, 35), 329: (32, 39), 330: (32, 40), 331: (32, 41), 332: (32, 42), 333: (32, 43), 334: (32, 44), 335: (32, 46), 336: (32, 47), 337: (32, 48), 338: (32, 49), 339: (32, 50), 340: (32, 51), 341: (32, 52), 342: None, 343: (33, 2), 344: (33, 3), 345: (33, 4)}
assert {p: heads[p] for p in range(300, 346)} == WIN, {p: heads[p] for p in range(300, 346) if heads[p] != WIN[p]}
assert heads[328] == (32, 35) and 'Who ate the fat of their sacrificial' in clean(sif[327][0]) and HB0(328, 1).startswith('(דברים לב לה) אשר חלב זבחימו יאכלו'), (heads[328], clean(sif[327][0])[:80], HB0(328, 1)[:60])   # 328's HEAD MISPRINTED IN THE HEBREW ROW ITSELF: the row's own marker reads (Deuteronomy 32:35) before 32:38's words ("who ate the fat of their sacrifices") — the export's verse marker wrong, the head computed from it (sitting 19's lesson 1 in a head); retyped from the first pass's print
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {32: [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 23, 26, 29, 34, 35, 36, 37, 35, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52]}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {32: [2, 3, 16, 17, 20, 21, 22, 24, 25, 27, 28, 30, 31, 32, 33, 38, 45]}, NOHEAD   # seventeen verses without a head of their own — inside the piskaot before them (38 by 328's misprint)
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 249 and len(READ_ROWS) == 249 and len(PISKAOT) == 36 and READ_ROWS[0] == (306, 1) and READ_ROWS[-1] == (341, 1) and SPINE_ROWS[306] == 37 and max(SPINE_ROWS.values()) == 37
# THE TAILS AND THE EDGES (the split's print): 305's rows carry no word of 32:1; 305:6 ends with Joshua weeping; 306:1 opens with 32:1's citation and R. Meir; 341:1 opens with 32:52's; 342:1 opens with 33:1's and names 32:24-25
assert not any(w in HB0(305, r) for r in range(1, 7) for w in ('האזינו',)) and HB0(305, 6).startswith('וכיון שמת משה היה יהושע בוכה') and HB0(306, 1).startswith('(דברים לב א) האזינו השמים ואדברה, רבי מאיר אומר') and HB0(341, 1).startswith('(דברים לב נב) כי מנגד תראה את הארץ ושמה לא תבא') and HB0(342, 1).startswith('(דברים לג, א) וזאת הברכה אשר ברך משה') and '(דברים לב כד-כה)' in HB0(342, 1)
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'Lend an ear, Heavens' in clean(sif[305][0]) and 'For only from afar shall you see the Land' in clean(sif[340][0]) and 'And this is the blessing' in clean(sif[341][0])   # the English rows open with the translator's apparatus before the text (sitting 19's lesson)
# THE CITATIONS PARSED FROM THE DUMP'S PRINT (the instrument's own lists read back): the row-citations per file, the union, the outside set; the divisions; the store
import ast as _ast
_t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch32_dump0.out'), encoding='utf-8').read()
_HE = _ast.literal_eval(re.search(r'^  HE rows citing Deut 32[^:]*: \d+ (\[.*\])$', _t, re.M).group(1)); _EN = _ast.literal_eval(re.search(r'^  EN rows citing Deut 32[^:]*: \d+ (\[.*\])$', _t, re.M).group(1))
_un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1)); _insp = int(re.search(r'\| in-spine rows of the union: (\d+)$', _t, re.M).group(1))
_two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-32: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
_mis = _ast.literal_eval(re.search(r'verses whose store token count differs from the DB: (\[.*?\])$', _t, re.M).group(1)); _tok = int(re.search(r'^  token count chapter 32 : (\d+)$', _t, re.M).group(1))
assert (len(_HE), len(_EN), _un, _insp) == (61, 368, 242, 231) and _out == OUTSIDE and len(_out) == 11, (len(_HE), len(_EN), _un, _insp, _out)
assert tuple(int(x) for x in _two.groups()[:3]) == (52, 52, 52) and _two.group(4) == '[(5, 30, 33)]' and _cost == 141, 'THE TWO DIVISIONS: the identity; chapter 5 the book\'s one split'
assert _mis == [(32, 13, 14, 13)] and _tok == 615, (_mis, _tok)   # THE STORE = THE DB except at 32:13 (the store one token more)
# THE OUTSIDE ROWS' FACTS COMPUTED from the dump's lists: the verses each row cites (the DB's numbering), the heads of their piskaot, the prior reads from the ledgers, the fresh rows
CITED = {}
for _p, _r, _e, _dbv in _HE + _EN:
    if (_p, _r) in OUTSIDE:
        for _d in _dbv: CITED.setdefault((_p, _r), set()).add((32, _d))
CITED = {k: sorted(v) for k, v in sorted(CITED.items())}
assert sorted(CITED) == OUTSIDE, (sorted(set(OUTSIDE) - set(CITED)), sorted(set(CITED) - set(OUTSIDE)))
assert CITED[(1, 1)] == [(32, 1), (32, 15)] and CITED[(37, 11)] == [(32, 49)] and CITED[(39, 11)] == [(32, 2)] and CITED[(43, 24)] == [(32, 23)] and CITED[(48, 2)] == [(32, 47)] and CITED[(48, 10)] == [(32, 47)], {k: CITED[k] for k in ((1, 1), (37, 11), (39, 11), (43, 24), (48, 2), (48, 10))}
HEADS_ON = {p: heads[p] for p in sorted({p for p, _ in OUTSIDE})}
assert HEADS_ON == {1: (1, 1), 37: (11, 10), 39: (11, 11), 43: (11, 15), 48: (11, 22), 342: None, 346: (33, 5), 355: (33, 20), 356: (33, 27), 357: (34, 1)}, HEADS_ON
_TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{_TRI}/{f}', encoding='utf-8').read() for f in os.listdir(_TRI) if f.endswith('.md') and os.path.isfile(f'{_TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
PRIOR_READ = {}
for f, t in LED.items():
    for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t):
        if (int(a), int(b)) in OUTSIDE: PRIOR_READ.setdefault((int(a), int(b)), []).append(f)
PRIOR_READ = {k: sorted(set(v)) for k, v in sorted(PRIOR_READ.items())}
FRESH = [k for k in OUTSIDE if k not in PRIOR_READ]
assert ('deu_04_vaetchanan_2026-09-16.md', 306, 1) in SPINE_PRIOR and ('deu_08_ekev_2026-09-18.md', 318, 1) in SPINE_PRIOR and len(SPINE_PRIOR) >= 12, len(SPINE_PRIOR)   # spine rows READ BEFORE at earlier chapters (the dump's list) — REREAD WHOLE here under the whole-row rule and marked so
assert (1, 1) in PRIOR_READ and (37, 11) in PRIOR_READ and (48, 2) in PRIOR_READ and (48, 10) in PRIOR_READ, sorted(PRIOR_READ)   # the dump's F list: 1:1 and 37:11 at chapters 1-3, 48:2 at chapter 4, 48:10 at chapter 8
# THE FRAMES AND THE NAMES (the dump's D section): the one divine frame and the one "saying" at 32:48; Hoshea's old name at 32:44; the case tokens
assert [(c, v) for c, v in SPAN if 'לאמר' in W(c, v)] == [(32, 48)] and 'והושע' in W(32, 44) and 'משה' in W(32, 44) and 'נון' in W(32, 44) and 'ישרון' in W(32, 15) and 'שאול' in W(32, 22)
assert [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('פן',)] == [(32, 27, 'פן'), (32, 27, 'פן')] and [(c, v) for c, v in SPAN if 'אם' in W(c, v)] == [(32, 30), (32, 41)] and [(c, v) for c, v in SPAN if 'לא' in W(c, v) and 'תבוא' in W(c, v)] == [(32, 52)]
