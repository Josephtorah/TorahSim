# ---- THE ASSERTS TYPED FROM THE PRINTS (block a: the dump's and the split's — the shelf by position, the divisions, the citations; the outside rows' facts COMPUTED) ----
DT = ('Deut',)
def PL(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def HB0(p, r): return PL(clean(sif_he[p - 1][r - 1]))
def ARM(c, v): return [PL(unicodedata.normalize('NFKC', x)).strip('.:()') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def SEATS(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(ARM(c + 1, v + 1))]
# THE SHELF BY POSITION — THE SPINE IN FORCE on chapter 33: fifteen heads 342-356 (the dump's window 335-357, the export's end); 341 on 32:52 before, 357 on 34:1 after; the heads by chapter as sitting 20's table printed them but for (33, 15) — 342's comma head now read (sitting 20's instrument: (33, 14), 342 headless)
assert NV == {33: 29} and VC[32] == 52 and VC[34] == 12 and len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
HC = Counter(h[0] for h in heads.values() if h)
assert (HC[31], HC[32], HC[33], HC[34]) == (1, 36, 15, 1) and sorted(HC.items()) == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16), (16, 19), (17, 16), (18, 16), (19, 10), (20, 14), (21, 17), (22, 22), (23, 22), (24, 16), (25, 10), (26, 4), (31, 1), (32, 36), (33, 15), (34, 1)], sorted(HC.items())
WIN = {335: (32, 46), 336: (32, 47), 337: (32, 48), 338: (32, 49), 339: (32, 50), 340: (32, 51), 341: (32, 52), 342: (33, 1), 343: (33, 2), 344: (33, 3), 345: (33, 4), 346: (33, 5), 347: (33, 6), 348: (33, 7), 349: (33, 8), 350: (33, 9), 351: (33, 10), 352: (33, 11), 353: (33, 13), 354: (33, 18), 355: (33, 20), 356: (33, 27), 357: (34, 1)}
assert {p: heads[p] for p in range(335, 358)} == WIN, {p: heads[p] for p in range(335, 358) if heads[p] != WIN[p]}
assert heads[342] == (33, 1) and HB0(342, 1).startswith('(דברים לג, א) וזאת הברכה אשר ברך משה') and 'And this is the blessing' in clean(sif[341][0]), (heads[342], HB0(342, 1)[:60])   # THE COMMA HEAD: 342's marker "(Deuteronomy 33, 1) and this is the blessing which Moses blessed" carries a comma between the chapter and the verse — the export's one; sitting 20's strict regex read it as headless
HV = {c: [heads[p][1] for p in PISKAOT_BY[c] if heads[p]] for c in CHS}
assert HV == {33: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 18, 20, 27]}, HV
NOHEAD = {c: [v for v in range(1, NV[c] + 1) if v not in HV[c]] for c in CHS}
assert NOHEAD == {33: [12, 14, 15, 16, 17, 19, 21, 22, 23, 24, 25, 26, 28, 29]}, NOHEAD   # fourteen verses without a head of their own — 12 inside 352 (Benjamin in the piska of Levi's blessing), 14-17 inside 353 (Joseph), 19 inside 354 (Zebulun and Issachar), 21-26 inside 355 (Gad's piska carries Dan, Naphtali, Asher and the rider of the heavens), 28-29 inside 356
assert {p: (len(sif_he[p - 1]), len(sif[p - 1])) for p in PISKAOT} == {p: (n, n) for p, n in SPINE_ROWS.items()} and sum(SPINE_ROWS.values()) == 142 and len(READ_ROWS) == 142 and len(PISKAOT) == 15 and READ_ROWS[0] == (342, 1) and READ_ROWS[-1] == (356, 14) and SPINE_ROWS[355] == 30 and max(SPINE_ROWS.values()) == 30
# THE TAILS AND THE EDGES (the split's print): 341's one row carries no word of 33:1 ("and this is the blessing"); 342:1 opens with 33:1's citation and the hard words of 32:24-25; 356:14 ends on Joshua 10:24's necks ("and you shall tread on their high places"); 357:1 opens with 34:1's ascent; 357's rows carry no "happy are you, O Israel"
assert not any('וזאת הברכה' in HB0(341, r) for r in range(1, 2)) and HB0(341, 1).startswith('(דברים לב נב) כי מנגד תראה את הארץ') and HB0(342, 1).startswith('(דברים לג, א) וזאת הברכה אשר ברך משה, לפי שאמר משה לישראל דברים קשים תחלה (דברים לב כד-כה)') and HB0(356, 14).startswith('ואתה על במותימו תדרוך') and '(יהושע י כד)' in HB0(356, 14) and HB0(357, 1).startswith('(דברים לד א) ויעל משה מערבת מואב') and not any('אשריך ישראל' in HB0(357, r) for r in range(1, 45))
assert all(clean(sif[p - 1][0]).startswith('Pisqa’ %d' % p) for p in PISKAOT) and 'And this is the blessing' in clean(sif[341][0]) and 'The Primordial God is a refuge' in clean(sif[355][0]) and 'And Moses ascended' in clean(sif[356][0])   # the English rows open with the translator's apparatus before the text (sitting 19's lesson)
# THE CITATIONS PARSED FROM THE DUMP'S PRINT (the instrument's own lists read back): the row-citations per file, the union, the outside set; the divisions; the store
import ast as _ast
_t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch33_dump0.out'), encoding='utf-8').read()
_HE = _ast.literal_eval(re.search(r'^  HE rows citing Deut 33[^:]*: \d+ (\[.*\])$', _t, re.M).group(1)); _EN = _ast.literal_eval(re.search(r'^  EN rows citing Deut 33[^:]*: \d+ (\[.*\])$', _t, re.M).group(1))
_un = int(re.search(r'^  the union of rows \(both files\): (\d+) \[', _t, re.M).group(1)); _out = _ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', _t, re.M).group(1)); _insp = int(re.search(r'\| in-spine rows of the union: (\d+)$', _t, re.M).group(1))
_two = re.search(r'^  DB verses (\d+) \| export verses HE (\d+) EN (\d+) \| per-chapter export lengths vs DB, chapters 1-33: (\[.*\])$', _t, re.M); _cost = int(re.search(r'^  the alignment cost (\d+) \|', _t, re.M).group(1))
_mis = _ast.literal_eval(re.search(r'verses whose store token count differs from the DB: (\[.*?\])$', _t, re.M).group(1)); _tok = int(re.search(r'^  token count chapter 33 : (\d+)$', _t, re.M).group(1))
assert (len(_HE), len(_EN), _un, _insp) == (34, 203, 128, 123) and _out == OUTSIDE and len(_out) == 5, (len(_HE), len(_EN), _un, _insp, _out)
assert tuple(int(x) for x in _two.groups()[:3]) == (29, 29, 29) and _two.group(4) == '[(5, 30, 33)]' and _cost == 121, 'THE TWO DIVISIONS: the identity; chapter 5 the book\'s one split'
assert _mis == [(33, 2, 18, 16), (33, 9, 19, 18)] and _tok == 336, (_mis, _tok)   # THE STORE = THE DB except at 33:2 (the store two tokens more — the fiery law's ketiv one word, the qere two) and 33:9 (one more)
# THE OUTSIDE ROWS' FACTS COMPUTED from the dump's lists: the verses each row cites (the DB's numbering), the heads of their piskaot, the prior reads from the ledgers, the fresh rows
CITED = {}
for _p, _r, _e, _dbv in _HE + _EN:
    if (_p, _r) in OUTSIDE:
        for _d in _dbv: CITED.setdefault((_p, _r), set()).add((33, _d))
CITED = {k: sorted(v) for k, v in sorted(CITED.items())}
assert sorted(CITED) == OUTSIDE, (sorted(set(OUTSIDE) - set(CITED)), sorted(set(CITED) - set(OUTSIDE)))
assert CITED == {(31, 6): [(33, 6)], (42, 9): [(33, 25)], (48, 9): [(33, 4)], (314, 1): [(33, 2)], (329, 3): [(33, 6)]}, CITED   # Reuben's repentance (31:6 on 33:6), the lands' surplus (42:9 on 33:25), all equal in the Torah (48:9 on 33:4), the eagle and the four winds (314:1 on 33:2), death and life in one (329:3 on 33:6)
HEADS_ON = {p: heads[p] for p in sorted({p for p, _ in OUTSIDE})}
assert HEADS_ON == {31: (6, 4), 42: (11, 14), 48: (11, 22), 314: (32, 11), 329: (32, 39)}, HEADS_ON
_TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{_TRI}/{f}', encoding='utf-8').read() for f in os.listdir(_TRI) if f.endswith('.md') and os.path.isfile(f'{_TRI}/{f}') and f != os.path.basename(OUT)}
SPINE_PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t) if int(a) in PISKAOT})
PRIOR_READ = {}
for f, t in LED.items():
    for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t):
        if (int(a), int(b)) in OUTSIDE: PRIOR_READ.setdefault((int(a), int(b)), []).append(f)
PRIOR_READ = {k: sorted(set(v)) for k, v in sorted(PRIOR_READ.items())}
FRESH = [k for k in OUTSIDE if k not in PRIOR_READ]
assert ('deu_09_ekev_2026-09-19.md', 342, 1) in SPINE_PRIOR and ('deu_32_haazinu_2026-09-27.md', 346, 2) in SPINE_PRIOR and ('gen_22_covenant_bow_2026-08-25.md', 343, 9) in SPINE_PRIOR and len(SPINE_PRIOR) >= 12, len(SPINE_PRIOR)   # spine rows READ BEFORE at earlier chapters (the dump's list) — REREAD WHOLE here under the whole-row rule and marked so
assert sorted(PRIOR_READ) == OUTSIDE and FRESH == [], (sorted(PRIOR_READ), FRESH)   # EVERY OUTSIDE ROW READ BEFORE — 31:6 at chapter 6, 42:9 and 48:9 at chapter 11 (48:9 again at 29-31), 314:1 and 329:3 at the song: none fresh
# THE FRAMES AND THE NAMES (the dump's D section): no 'saying' in the chapter; the one narrative frame 33:2 'and he said' with the Name its object (Moses speaking); Jeshurun at 33:5 (with the prefix) and 33:26; eleven tribes named, Simeon absent; 'for' (ki) at 33:9, 33:19, 33:21; no 'if', no 'lest'
assert [(c, v) for c, v in SPAN if 'לאמר' in W(c, v)] == [] and 'בישרון' in W(33, 5) and 'ישרון' in W(33, 26) and 'משה' in W(33, 1) and 'האלהים' in W(33, 1) and 'מותו' in W(33, 1)   # no "saying"; "in Jeshurun" 33:5; "Jeshurun" 33:26; "Moses", "God", "his death" at 33:1
assert 'ראובן' in W(33, 6) and 'יהודה' in W(33, 7) and 'וללוי' in W(33, 8) and 'לבנימן' in W(33, 12) and 'וליוסף' in W(33, 13) and 'אפרים' in W(33, 17) and 'מנשה' in W(33, 17) and 'ולזבולן' in W(33, 18) and 'ויששכר' in W(33, 18) and 'ולגד' in W(33, 20) and 'ולדן' in W(33, 22) and 'ולנפתלי' in W(33, 23) and 'ולאשר' in W(33, 24)   # Reuben, Judah, and-to-Levi, to-Benjamin, and-to-Joseph, Ephraim, Manasseh, and-to-Zebulun, and-Issachar, and-to-Gad, and-to-Dan, and-to-Naphtali, and-to-Asher
assert [(c, v) for c, v in SPAN if 'כי' in W(c, v)] == [(33, 9), (33, 19), (33, 21)] and [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v) or 'פן' in W(c, v)] == [] and not any('שמעון' in W(c, v) for c, v in SPAN)   # "for" thrice; no "if", no "lest"; Simeon named nowhere in the chapter
