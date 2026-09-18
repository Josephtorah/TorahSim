#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 5 — CHAPTER 7, Deuteronomy 7:1-26 (2026-09-17; the owner: "Go"; RUN 1 of four — the rereads, the measurements, the ink,
# the design): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 4's form
# (ch6_ink.py): the scaffold by hand, the constants and every assert chapter 7's own, typed FROM THE PRINTS (ch7_dump0.out, ch7_measure1.out). THE TWO
# DIVISIONS AGREE (26 = 26; the alignment the identity, cost 20). THE SPINE IS SILENT ON THE CHAPTER: no piska heads in chapter 7 (36 on 6:9, 37 on 11:10 —
# chapters 7 to 10 have none); THREE rows elsewhere cite it — 37:1 (the English translator's own "(Dt.7:12)" naming the portion's opening, with the note that the
# Sifrei does not expound it — an interpolation), 50:4 on 11:23 citing 7:1 (one of the seven nations greater than all Israel), 61:7 on 12:3 citing 7:26 (the
# shrines' names changed to derogatory ones). The parser MEASURED on every verse — TWO number verses, 7:1 "seven nations" [7] (the seven gentilic tokens of the
# verse the count's own witness) and 7:9 "a thousand generations" [1000]; the seven-stem homograph "the oath" (7:8) STARRED; NO GAP. THE STORE = THE DB at every
# verse but 7:9, where the store carries the written AND the read form of "His commandments" — the chapter's one written/read pair (5:10's kin). The hand's facts
# as asserts, run all at once by assert_driver.py after the measurement passes printed them.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-17'
CH = 7
UIDS = ['deu_07_nations_cherem']
SPANS = {'deu_07_nations_cherem': (7, 1, 26)}
PREFIX = {'deu_07_nations_cherem': 'DV07'}
PISKAOT = []   # NO piska head on the chapter (typed from ch7_dump0's A print: the heads by chapter (6, 6), (11, 21); the nearest 36 on 6:9, 37 on 11:10)
EXP2DB = {e: [e] for e in range(1, 27)}   # the identity — 26 = 26 (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
OUTSIDE_HE = [(50, 4, (7, 1)), (61, 7, (7, 26))]   # the Hebrew's book-named citations of chapter 7 — two rows, both outside any piska on the chapter
OUTSIDE_EN = [(37, 1, (7, 12)), (50, 4, (7, 1)), (61, 7, (7, 26))]   # the English's — three: 37:1's is the translator's own (the portion's opening verse named, the Hebrew citing 11:10 alone)
OUTSIDE = [(37, 1), (50, 4), (61, 7)]   # the three rows READ: the union of both files (no piska on the chapter, so the union is the spine's whole contribution — chapter 4's form)
INTERPOLATION = [(37, 1)]   # the English's "(Dt.7:12)" with its footnote: "This verse initiates parashat `Eqev in the MT, but is not subject to midrashic exegesis in Sifre Dt."
EXCLUDED = []   # no slip this chapter (chapter 6's 62:4 form checked: no cited verse beyond 26)
CITED_DB = {(37, 1): 12, (50, 4): 1, (61, 7): 26}   # the DB verse each outside row cites (the export's numbering = the DB's here)
FRESH = OUTSIDE[:]   # none of the three read before (the prior-reads census)
CREDITED = {}
TITLE = 'Chapter 7 — When the LORD your God brings you into the land and clears away seven nations greater than you: utterly destroy them, no covenant, no favor, no marriage, their altars torn down; for you are a holy people, chosen for love and for the oath, not for number; the faithful God keeps covenant and kindness to a thousand generations and repays His haters to their face; because you hear: love, blessing, fruit, no barrenness, no disease of Egypt; consume the peoples, do not pity, do not serve their gods; do not fear them — remember Pharaoh; the hornet; little by little; their kings given, their name destroyed; their images burned, the silver and gold not coveted; no abomination into your house — it is devoted'
OUT = f'{ROOT}/logic/oral_triage/deu_07_vaetchanan_ekev_{DATE}.md'

def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/en.json', encoding='utf-8'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
HN = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400}
def hn(s): return sum(HN[c] for c in s if c in HN)
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
heads = {}
for p in range(1, 358):
    m = re.match(r'\(דברים ([א-ת]+) ([א-ת]+)(?:-[א-ת]+)?\)', Hb(p, 1))
    heads[p] = (hn(m.group(1)), hn(m.group(2))) if m else None
def head(p): return heads[p]
# THE SHELF BY POSITION — the two files' grains, the heads around chapter 7: NONE on the chapter; 34-36 on 6:7-9 before it, 37-38 on 11:10 and 39 on 11:11 after
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
assert {p: heads[p] for p in range(34, 40)} == {34: (6, 7), 35: (6, 8), 36: (6, 9), 37: (11, 10), 38: (11, 10), 39: (11, 11)}, {p: heads[p] for p in range(34, 40)}
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 7] == [] and HC[7] == 0 and HC[8] == 0 and HC[9] == 0 and HC[10] == 0 and sorted(HC.items())[:8] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16)], sorted(HC.items())[:8]
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
CIT_HE = [(p, r, (7, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 7]
CIT_EN = [(p, r, (7, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(7):(\d+)', E(p, r))]
assert CIT_HE == OUTSIDE_HE and CIT_EN == OUTSIDE_EN, (CIT_HE, CIT_EN)
UNION = sorted({(p, r) for p, r, _ in CIT_HE} | {(p, r) for p, r, _ in CIT_EN})
assert UNION == OUTSIDE and len(UNION) == 3 and all(1 <= v <= 26 for _, _, (_, v) in CIT_HE + CIT_EN)   # a cited verse beyond the chapter's length would be a slip (chapter 6's lesson): none
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?7:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE} == {37: (11, 10), 50: (11, 23), 61: (12, 3)}, {p: heads[p] for p, _ in OUTSIDE}
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE)
# THE TRANSLATOR'S NOTE: 37:1 (the first row of Ekev's first piska, on 11:10) — the English prefixes "(Dt.7:12)" as the portion's opening and says in its own note that the
# Sifrei does not expound the verse; the Hebrew cites 11:10 alone: an interpolation, read and marked (chapter 6's 104:8 the form)
assert he_cites(Hb(37, 1)) == [('דברים', 11, 10)] and '(Dt.7:12)' in E(37, 1) and 'not subject to midrashic exegesis' in E(37, 1) and E(37, 1).count('(Dt.11:10)') == 2 and 'לֹא כְאֶרֶץ מִצְרַיִם' in Hb(37, 1)
# 50:4 (on 11:23 "greater and mightier than you") cites 7:1 "seven nations greater and mightier than you" — one of the seven greater than all Israel, Amos 2:9 the proof
assert '(דברים ז א)' in Hb(50, 4) and '(עמוס ב ט)' in Hb(50, 4) and 'שִׁבְעָה גוֹיִם' in Hb(50, 4) and '(Dt.7:1)' in E(50, 4) and '(Dt.11:23)' in E(50, 4) and '(Am.2:9)' in E(50, 4)
# 61:7 (on 12:3 "you shall destroy their name") cites 7:26 "utterly detest it, utterly abhor it" — R. Akiva: the shrines' names changed for the worse, never for the better
assert '(דברים ז כו)' in Hb(61, 7) and 'שַׁקֵּץ תְּשַׁקְּצֶנּוּ' in Hb(61, 7) and '(Dt.7:26)' in E(61, 7) and '(Dt.12:3)' in E(61, 7) and '(Dt.12:2)' in E(61, 7) and 'R. Akiva' in E(61, 7) and 'R. Eliezer' in E(61, 7)
# THE PRIOR READS — the strict row form over every ledger: none of the three rows read before; no Onkelos row of chapter 7 anywhere; the kin's Onkelos read at the Exodus and Numbers sittings
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE] == [] and len(PRIOR) == 294, len(PRIOR)
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 7:', t, re.M)) == []
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (23|34):', t, re.M)) == ['erection_docket_2026-09-06.md', 'exo_23_escort_land_2026-09-01.md', 'exo_23_justice_calendar_2026-09-01.md', 'exo_34_second_tablets_2026-09-01.md']
assert sum(len(re.findall(r'Mekhilta[^\n]{0,40}(?:23|34):\d+', t)) for t in LED.values()) == 21 and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 33:', t, re.M)) == ['num_33_journeys_2026-09-12.md']
assert len(re.findall(r'^- Onkelos Exod 23:(?:2\d|3[0-3])', LED['exo_23_escort_land_2026-09-01.md'], re.M)) == 8 and len(re.findall(r'^- Onkelos Num 33:5\d', LED['num_33_journeys_2026-09-12.md'], re.M)) == 7   # the kin's rows: the angel's clauses 23:21-33 (eight rows), the dispossession 33:50-56 (seven)
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 7:\d+', t))
assert NAMING == ['erection_docket_2026-09-06.md', 'num_06_nazir_2026-09-09.md', 'num_18_priest_levite_dues_2026-09-10.md', 'num_21_snakes_conquest_2026-09-11.md', 'num_33_journeys_2026-09-12.md', 'num_35_refuge_cities_2026-09-13.md'], NAMING
assert 'Deut 7:25' in LED['erection_docket_2026-09-06.md'] and 'Mishnah Avodah Zarah 3:5' in LED['erection_docket_2026-09-06.md']   # the idols' silver and gold graded at the Exodus 34 sitting — a CREDIT at the compile
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5, 6, 7)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30, 6: 25, 7: 26} and sum(len(c) for c in onk_he) == 956
def onk_ev(c, v):
    """an Onkelos row by the DB's verse — the export's row found through the map (chapter 5's 17-20 share the export's 17)"""
    e = DB2EXP[v] if c == 5 else v
    return clean(onk[c - 1][e - 1]), clean(onk_he[c - 1][e - 1])
shelf_deut = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Deuteronomy|Devarim', d))
outside = [d for d in shelf_deut if d not in ('Sifrei_Devarim', 'Onkelos_Deuteronomy')]
assert len(shelf_deut) == 28 and len(outside) == 26, len(outside)

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
assert VC[5] == 33 and VC[6] == 25 and VC[7] == 26 and VC[8] == 20 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
# THE ALIGNMENT RECOMPUTED (ch7_dump0's A0): the export's twenty-six rows against the DB's twenty-six verses over token and negation counts — the identity, cost 20
by7 = {v: [plain(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=7 AND v.verse=? ORDER BY w.idx", (v,))] for v in range(1, 27)}
NEG = ('לא', 'ולא')
D_ = [(len(by7[v]), sum(1 for x in by7[v] if x in NEG)) for v in range(1, 27)]
E_ = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[6]]
def _cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
INF = 10 ** 9; best = {(0, 0): (0, None)}
for i in range(1, 27):
    for j in range(i, 27):
        cands = [(best[(i - 1, k)][0] + _cost(E_[i - 1], D_[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best and j - k <= 4]
        best[(i, j)] = min(cands) if cands else (INF, None)
i, j, ALIGN = 26, 26, {}
while i > 0:
    k = best[(i, j)][1]; ALIGN[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
assert ALIGN == EXP2DB and best[(26, 26)][0] == 20 and Counter(ds[0] - e for e, ds in EXP2DB.items()) == Counter({0: 26}) and len(onk_he[6]) == 26 == VC[7], (best[(26, 26)][0], ALIGN)
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
UT7 = unit_text('deu_07_nations_cherem')
assert UT7.count('\n    comment:') + UT7.count('\n      comment:') == 30 and UT7.count('\n  - id: S') == 33   # typed from ch7_dump0's G print (the draft's comment lines and scenarios)
assert 'deu_06_shema' in UT7 and steps('deu_08_manna_humility')[0] == (8, 1) and steps('deu_08_manna_humility')[-1] == (8, 20)
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_') and f != os.path.basename(OUT)) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md', 'deu_04_vaetchanan_2026-09-16.md', 'deu_04_vaetchanan_exam_2026-09-16.md', 'deu_05_vaetchanan_2026-09-16.md', 'deu_05_vaetchanan_exam_2026-09-16.md', 'deu_06_vaetchanan_2026-09-17.md', 'deu_06_vaetchanan_exam_2026-09-17.md']
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json') and not f.startswith('deu_07'))
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(7, v) for v in range(1, VC[7] + 1)]
NV = 26
assert len(SPAN) == NV

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma, w.wtype FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byl, byw = {}, {}, {}, {}
for b, c, v, he, m, lem, wt in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byl.setdefault((b, c, v), []).append((lem or '').split('/')[-1].strip()); byw.setdefault((b, c, v), []).append(wt)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m in by[(b, c, v)]]
def wm(b, c, v): return list(zip(words(b, c, v), morphs(b, c, v)))
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def P(*seq, books=None): return phrase(list(seq), books)
def S_(*x): return sorted(x)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def LEMT(lem, books=None): return [(f'{b} {c}:{v}', x, m) for (b, c, v), ws in by.items() if (books is None or b in books) for (x, m), l in zip(ws, byl[(b, c, v)]) if l == lem]
def LEMV(lem, books=None): return sorted({s for s, _, _ in LEMT(lem, books)})
def lemma_of(b, c, v, tok): return [l for (x, m), l in zip(by[(b, c, v)], byl[(b, c, v)]) if x == tok]
def W7(v): return words('Deut', 7, v)
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
def DIFF(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return [(op, A[i1:i2], B[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op != 'equal']
def SHARED(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    m = difflib.SequenceMatcher(None, A, B).find_longest_match(0, len(A), 0, len(B))
    return A[m.a:m.a + m.size]
FAIL = []
def H(c, v, *cons):
    w, wp = words('Deut', c, v), byp[('Deut', c, v)]
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(w) and w[j] != k: j += 1
        if j >= len(w): FAIL.append(('H', c, v, k)); out.append('⟨MISS⟩'); continue
        out.append(wp[j]); i = j + 1
    return ' '.join(out)
def A(c, v, *cons):
    ws = onk_ev(c, v)[1].rstrip(':').split()
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(ws) and plain(ws[j]).strip('.:') != k: j += 1
        if j >= len(ws): FAIL.append(('A', c, v, k, [plain(x) for x in ws])); out.append('⟨MISS⟩'); continue
        out.append(ws[j].rstrip('.:')); i = j + 1
    return ' '.join(out)
def aramaic(c, v): return [plain(x).strip('.:') for x in onk_ev(c, v)[1].rstrip(':').split()]
def arm(c, v): return plain(onk_ev(c, v)[1])
def arm_e(c, e): return plain(clean(onk_he[c - 1][e - 1]))
def onk_seats(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in arm_e(c + 1, v + 1)]      # EXPORT verse numbers (chapter 5's 17 = the DB's 17-20; 18+ = the DB's verse minus three)
def onk_tok(tok): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if tok in [plain(x).strip('.:') for x in clean(onk_he[c][v]).rstrip(':').split()]]
def HP(c, v, *pieces):
    out = []
    for toks, gloss in pieces:
        assert len(toks) <= 7, (c, v, toks)
        out.append(f'"{H(c, v, *toks)}" ({gloss})')
    return ' '.join(out)
def AP(c, v, *pieces):
    out = []
    for toks, gloss in pieces:
        assert len(toks) <= 7, (c, v, toks)
        out.append(f'{A(c, v, *toks)} ({gloss})')
    return ' '.join(out)
def SP_(p, r, *cons):
    ws = Hb(p, r).split()
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(ws) and plain(ws[j]).strip('.,:;?!"()–-״׳') != k: j += 1
        if j >= len(ws): FAIL.append(('S', p, r, k)); out.append('⟨MISS⟩'); continue
        out.append(ws[j].rstrip('.,:;?!')); i = j + 1
    return ' '.join(out)
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 7 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=7 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
# THE STORE = THE DB at every verse but ONE: 7:9 — the store carries the written מצותו ("His commandments", the ketiv, wtype x-ketiv in the DB) AND the read מצותיו (the qere,
# the plural with its yod): THE CHAPTER'S ONE WRITTEN/READ PAIR, the same written form as 5:10's (there the read form is Exodus 20:6's "MY commandments"); no large letter in the
# chapter; 412 tokens, 1,637 letters (176 in 7:1-11, 236 in 7:12-26 — the portion's edge at 7:12); the one unglossed token "I" (אנכי, 7:11).
assert STORE_MISMATCH == [(7, 9, 17, 16)] and [(v, hp) for v in range(1, 27) for i, (_, hp, _) in enumerate(SG[(7, v)]) if v != 9 and hp != W7(v)[i]] == [] and [hp for _, hp, _ in SG[(7, 9)]][13:15] == ['מצותו', 'מצותיו']
assert byw[('Deut', 7, 9)][13] == 'x-ketiv' and W7(9)[13] == 'מצותו' and Counter(wt for v in range(1, 27) for wt in byw[('Deut', 7, v)]) == Counter({None: 411, 'x-ketiv': 1}) and byw[('Deut', 5, 10)][-1] == 'x-ketiv' and words('Deut', 5, 10)[-1] == 'מצותו' and words('Exod', 20, 6)[-1] == 'מצותי'
assert sum(1 for ws in byw.values() for wt in ws if wt == 'x-ketiv') == 1268
TOK = sum(len(W7(v)) for v in range(1, 27)); LET = sum(len(x) for v in range(1, 27) for x in W7(v))
assert TOK == 412 and LET == 1637 and {v: len(W7(v)) for v in range(1, 27)} == {1: 27, 2: 14, 3: 11, 4: 14, 5: 14, 6: 20, 7: 14, 8: 22, 9: 16, 10: 12, 11: 12, 12: 20, 13: 22, 14: 10, 15: 17, 16: 21, 17: 10, 18: 13, 19: 25, 20: 12, 21: 10, 22: 18, 23: 9, 24: 15, 25: 19, 26: 15}, TOK
assert (sum(len(W7(v)) for v in range(1, 12)), sum(len(W7(v)) for v in range(12, 27))) == (176, 236)
assert [(v, hp) for (c, v), g in sorted(SG.items()) for _, hp, gl in g if gl == '?'] == [(11, 'אנכי')]
# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: TWO number verses, 7:1 "seven nations" [7] and 7:9 "to a thousand generations" [1000]; the
# seven-stem homograph "the oath" (השבעה, 7:8, the lemma 7621) STARRED; "swore" (נשבע, 7:8, 12, 13 — the lemma 7650) not a number at all; no ordinal; NO GAP. The same
# phrase reads the same at its other seats: "to a thousand generations" [1000] at 1 Chronicles 16:15 and Psalm 105:8; "to thousands" (Exodus 20:6, 5:10, 34:7) NO number
# (the bare plural — the 1b multiplication rule); the six-name lists (Exodus 23:23, 34:11; 20:17) and the seven-name lists (Joshua 3:10, 24:11) carry no numeral — 7:1 alone
# COUNTS its list: "seven nations" beside seven gentilic tokens.
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
def MARKS(c, v): return [t for t in CS.verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSED = {(c, v): N('Deut', c, v) for (c, v) in SPAN if N('Deut', c, v)}
assert PARSED == {(7, 1): [7], (7, 9): [1000]} and {(c, v): O('Deut', c, v) for (c, v) in SPAN if O('Deut', c, v)} == {} and [((c, v), t) for (c, v) in SPAN for t in MARKS(c, v)] == [((7, 8), 'השבעה*')], PARSED
assert N('1Chr', 16, 15) == [1000] and N('Ps', 105, 8) == [1000] and N('Exod', 20, 6) == [] and N('Deut', 5, 10) == [] and N('Exod', 34, 7) == [] and N('Exod', 23, 29) == [1] and N('Exod', 23, 30) == [] and N('Deut', 20, 17) == [] and N('Josh', 3, 10) == [] and N('Josh', 24, 11) == [] and N('Exod', 23, 23) == [] and N('Exod', 34, 11) == []
assert lemma_of('Deut', 7, 8, 'השבעה') == ['7621'] and PT('Deut', 7, 8, 'השבעה') == ['הַשְּׁבֻעָה'] and lemma_of('Deut', 7, 8, 'נשבע') == ['7650'] and lemma_of('Deut', 7, 1, 'שבעה') == ['7651'] and lemma_of('Deut', 7, 9, 'לאלף') == ['505'] and morphs('Deut', 7, 1)[22] == 'HAcmsa' and morphs('Deut', 7, 9)[14] == 'HR/Acbsa'
NG7 = [x for x, m in wm('Deut', 7, 1) if 'Ng' in m]
assert NG7 == ['החתי', 'והגרגשי', 'והאמרי', 'והכנעני', 'והפרזי', 'והחוי', 'והיבוסי'] and len(NG7) == 7 == PARSED[(7, 1)][0]   # the numeral's witness in the verse itself
SEVEN = {'2850', '1622', '567', '3669 a', '6522', '2340', '2983'}   # the seven nations' lemmas (Hittite, Girgashite, Amorite, Canaanite, Perizzite, Hivite, Jebusite) — from 7:1's DB row
assert [lemma_of('Deut', 7, 1, x)[0] for x in NG7] == ['2850', '1622', '567', '3669 a', '6522', '2340', '2983']
NAT = {f'{b} {c}:{v}': set(l for l in byl[(b, c, v)] if l in SEVEN) for (b, c, v) in by}
assert {s for s, ls in NAT.items() if len(ls) == 7} == {'Deut 7:1', 'Josh 3:10', 'Josh 24:11'}   # the seven-name lists: this verse and Joshua's two (with the Girgashite)
assert {s for s, ls in NAT.items() if len(ls) == 6} == {'Deut 20:17', 'Exod 3:8', 'Exod 3:17', 'Exod 23:23', 'Exod 33:2', 'Exod 34:11', 'Josh 9:1', 'Josh 11:3', 'Josh 12:8', 'Judg 3:5', 'Neh 9:8'}, {s for s, ls in NAT.items() if len(ls) == 6}
assert LEMV('1622') == ['1Chr 1:14', 'Deut 7:1', 'Gen 10:16', 'Gen 15:21', 'Josh 24:11', 'Josh 3:10', 'Neh 9:8']   # the Girgashite's seven seats — absent from every Exodus list and from 20:17
# THE FRAMES AND THE REGISTER: NO divine frame, NO "saying" — the whole chapter Moses' voice; the narrative verbs TWO, both God's past acts inside the reason (7:7 "and He
# chose", 7:8 "and He redeemed you"); NO imperative; FIVE INFINITIVE ABSOLUTES — "utterly destroy" (7:2), "quickly" twice (7:4, 7:22 — the adverb's form), "surely remember"
# (7:18), "utterly detest … utterly abhor" (7:26, two); the law's form the consecutive perfect in fourteen verses; the PROHIBITIONS eleven in the second person (7:2 two, 7:3
# three, 7:16 "you shall not serve", 7:18, 7:21, 7:22 "you will not be able", 7:25, 7:26) and five in the third (7:10, 14, 15, 16 "your eye shall not pity", 24); the second person SINGULAR in nineteen verses, PLURAL in
# two (7:5 the altars, 7:7 the fewest), BOTH in four (7:4, 8, 12, 25 — "you shall burn" plural inside a singular verse), NEITHER in 7:10; the first person God's (7:4 "from
# after Me", 7:11 "I command") and the doubter's (7:17 "than I … how can I"); "for/when" twelve seats and "lest" two (22, 25), "but rather" once (7:5) — no "or".
NUM = {v: (sum(1 for m in morphs('Deut', 7, v) if m and '2mp' in m), sum(1 for m in morphs('Deut', 7, v) if m and '2ms' in m)) for v in range(1, 27)}
assert [v for v, (p, s) in NUM.items() if s and not p] == [1, 2, 3, 6, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26] and [v for v, (p, s) in NUM.items() if p and not s] == [5, 7] and [v for v, (p, s) in NUM.items() if p and s] == [4, 8, 12, 25] and [v for v, (p, s) in NUM.items() if not p and not s] == [10]
assert [x for v in range(1, 27) for x, m in wm('Deut', 7, v) if m and '2mp' in m] == ['בכם', 'תעשו', 'תתצו', 'תשברו', 'תגדעון', 'תשרפון', 'מרבכם', 'בכם', 'בכם', 'אתם', 'אתכם', 'לאבתיכם', 'אתכם', 'תשמעון', 'ושמרתם', 'ועשיתם', 'תשרפון']
assert [v for v in range(1, 27) if any(V in ('ויאמר', 'וידבר') and W7(v)[i + 1] == 'יהוה' for i, V in enumerate(W7(v)[:-1]))] == [] and [v for v in range(1, 27) if 'לאמר' in W7(v)] == [] and [v for v in range(1, 27) if 'משה' in W7(v) or 'ישראל' in W7(v)] == []
assert {v: [x for x, m in wm('Deut', 7, v) if m and re.search(r'^HC/V.w', m)] for v in range(1, 27) if any(m and re.search(r'^HC/V.w', m) for _, m in wm('Deut', 7, v))} == {7: ['ויבחר'], 8: ['ויפדך']}
assert {v: [x for x, m in wm('Deut', 7, v) if m and re.match(r'^HV.?.?v', m)] for v in range(1, 27) if any(m and re.match(r'^HV.?.?v', m) for _, m in wm('Deut', 7, v))} == {}
assert {v: [(x, m) for x, m in wm('Deut', 7, v) if m and re.match(r'^H(?:C/)?V.a$', m)] for v in range(1, 27) if any(m and re.match(r'^H(?:C/)?V.a$', m) for _, m in wm('Deut', 7, v))} == {2: [('החרם', 'HVha')], 4: [('מהר', 'HVpa')], 18: [('זכר', 'HVqa')], 22: [('מהר', 'HVpa')], 26: [('שקץ', 'HVpa'), ('ותעב', 'HC/Vpa')]}
assert sorted(v for v in range(1, 27) if any(m and re.search(r'^HC/V.q', m) for _, m in wm('Deut', 7, v))) == [1, 2, 4, 9, 11, 12, 13, 15, 16, 22, 23, 24, 25, 26] and [x for x, m in wm('Deut', 7, 13) if re.search(r'^HC/V.q', m)] == ['ואהבך', 'וברכך', 'והרבך', 'וברך']
PRO = {v: [(W7(v)[i + 1], morphs('Deut', 7, v)[i + 1]) for i, x in enumerate(W7(v)[:-1]) if x in NEG and morphs('Deut', 7, v)[i + 1] and morphs('Deut', 7, v)[i + 1].startswith('HV')] for v in range(1, 27) if any(x in NEG for x in W7(v))}
assert PRO == {2: [('תכרת', 'HVqi2ms'), ('תחנם', 'HVqi2ms/Sp3mp')], 3: [('תתחתן', 'HVti2ms'), ('תתן', 'HVqi2ms'), ('תקח', 'HVqi2ms')], 7: [], 10: [('יאחר', 'HVpi3ms')], 14: [('יהיה', 'HVqi3ms')], 15: [('ישימם', 'HVqi3ms/Sp3mp')], 16: [('תחס', 'HVqi3fs'), ('תעבד', 'HVqi2ms')], 18: [('תירא', 'HVqi2ms')], 21: [('תערץ', 'HVqi2ms')], 22: [('תוכל', 'HVqi2ms')], 24: [('יתיצב', 'HVti3ms')], 25: [('תחמד', 'HVqi2ms')], 26: [('תביא', 'HVhi2ms')]}, PRO
assert sum(1 for v in PRO for _, m in PRO[v] if 'i2' in m) == 11 and sum(1 for v in PRO for _, m in PRO[v] if 'i3' in m) == 5   # eleven in the second person; five in the third (7:16's "your eye shall not pity" the eye's — 3fs)
assert {f'7:{v}': [x for x in W7(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 27) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W7(v))} == {'7:1': ['כי'], '7:4': ['כי'], '7:5': ['כי', 'אם'], '7:6': ['כי'], '7:7': ['כי'], '7:8': ['כי'], '7:9': ['כי'], '7:16': ['כי'], '7:17': ['כי'], '7:21': ['כי'], '7:22': ['פן'], '7:25': ['פן', 'כי'], '7:26': ['כי']}
assert {v: [(x, m) for x, m in wm('Deut', 7, v) if m and '1cs' in m] for v in range(1, 27) if any(m and '1cs' in m for _, m in wm('Deut', 7, v))} == {4: [('מאחרי', 'HR/R/Sp1cs')], 11: [('אנכי', 'HPp1cs')], 17: [('ממני', 'HR/Sp1cs'), ('אוכל', 'HVqi1cs')]} and not any('1cp' in (m or '') for v in range(1, 27) for _, m in wm('Deut', 7, v))
assert Counter(x for v in range(1, 27) for x in W7(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה')) == Counter({'יהוה': 19, 'ליהוה': 1}) and [v for v in range(1, 27) for i in range(len(W7(v)) - 1) if W7(v)[i:i + 2] == ['יהוה', 'אלהיך']] == [1, 2, 6, 9, 12, 16, 18, 19, 19, 20, 21, 22, 23, 25] and [v for v in range(1, 27) for i in range(len(W7(v)) - 1) if W7(v)[i:i + 2] == ['יהוה', 'אלהיכם']] == []
assert [v for v in range(1, 27) for i in range(len(W7(v))) if W7(v)[i] == 'יהוה' and (i + 1 >= len(W7(v)) or W7(v)[i + 1] not in ('אלהיך', 'אלהיכם'))] == [4, 7, 8, 8, 15] and {v: [x for x in W7(v) if x in ('פרעה', 'לפרעה', 'מצרים')] for v in (8, 15, 18)} == {8: ['פרעה', 'מצרים'], 15: ['מצרים'], 18: ['לפרעה', 'מצרים']}
# THE KIN DIFFED (the DB's tokens): 7:1-2 against Exodus 23:23, 23:32 and 34:11-12, 15 — the angel's clauses "no covenant with them" (the six-name lists there; here SEVEN with the
# Girgashite); 7:3 against Exodus 34:16 — the daughters taken THERE, both directions barred HERE; 7:5 against Exodus 34:13 and 12:3 — the four objects (altars, pillars, Asherim,
# images); 7:6 against 14:2 (one letter and one word apart — "and in you" / "your God" dropped) and Exodus 19:5-6 ("treasure … holy"); 7:9 against Exodus 20:6 and 5:10 — ONE
# token shared with 20:6 ("and those who keep"), TWO with 5:10 (the ketiv "His commandments" both) — "to thousands" there, "to a thousand generations" here; 7:11 against 6:1
# and 5:31 (the triad's third seat — 5:31, 6:1, 7:11 in that order); 7:13 against 28:4 ("the fruit of your womb and the fruit of your ground" shared); 7:16 against Exodus
# 23:33 ("serve their gods, for" shared; "a snare"); 7:18 against 20:1 ("you shall not fear them"); 7:19 against 29:2 ("great which your eyes saw" shared) and 4:34; 7:20
# against Exodus 23:28 ("the hornet"); 7:21 against 6:15 ("the LORD your God in your midst"); 7:22 against Exodus 23:30 ("little by little" — the two seats); 7:24 against
# Joshua 1:5 ("no man shall stand"); 7:25 against Exodus 20:17 and 5:21 ("YOU SHALL NOT COVET" — the tenth word's verb on the idols' silver and gold, the phrase's two seats);
# 7:26 against 13:18 and Joshua 6:18, 7:12 (the devoted thing).
assert DIFF(('Deut', 7, 6), ('Deut', 14, 2)) == [('replace', ['בך'], ['ובך']), ('delete', ['אלהיך'], [])] and SHARED(('Deut', 7, 6), ('Deut', 14, 2)) == ['להיות', 'לו', 'לעם', 'סגלה', 'מכל', 'העמים', 'אשר', 'על', 'פני', 'האדמה']
assert SHARED(('Deut', 7, 9), ('Exod', 20, 6)) == ['ולשמרי'] and SHARED(('Deut', 7, 9), ('Deut', 5, 10)) == ['ולשמרי', 'מצותו'] and SHARED(('Deut', 7, 2), ('Exod', 23, 32)) == ['לא', 'תכרת', 'להם'] and SHARED(('Deut', 7, 3), ('Exod', 34, 16)) == []
assert SHARED(('Deut', 7, 22), ('Exod', 23, 30)) == ['מעט', 'מעט'] and SHARED(('Deut', 7, 20), ('Exod', 23, 28)) == ['את', 'הצרעה'] and SHARED(('Deut', 7, 24), ('Josh', 1, 5)) == ['לא', 'יתיצב', 'איש'] and SHARED(('Deut', 7, 25), ('Exod', 20, 17)) == ['לא', 'תחמד'] and SHARED(('Deut', 7, 25), ('Deut', 5, 21)) == ['תחמד']
assert SHARED(('Deut', 7, 13), ('Deut', 28, 4)) == ['פרי', 'בטנך', 'ופרי', 'אדמתך'] and SHARED(('Deut', 7, 5), ('Deut', 12, 3)) == ['תשרפון', 'באש'] and SHARED(('Deut', 7, 19), ('Deut', 29, 2)) == ['הגדלת', 'אשר', 'ראו', 'עיניך'] and SHARED(('Deut', 7, 21), ('Deut', 6, 15)) == ['יהוה', 'אלהיך', 'בקרבך']
assert SHARED(('Deut', 7, 4), ('Deut', 11, 17)) == ['וחרה', 'אף', 'יהוה', 'בכם'] and SHARED(('Deut', 7, 16), ('Exod', 23, 33)) == ['תעבד', 'את', 'אלהיהם', 'כי'] and SHARED(('Deut', 7, 18), ('Deut', 20, 1)) == ['לא', 'תירא', 'מהם'] and SHARED(('Deut', 7, 11), ('Deut', 6, 1)) == ['המצוה'] and SHARED(('Deut', 7, 23), ('Deut', 7, 2)) == ['ונתנם', 'יהוה', 'אלהיך', 'לפניך']
# THE PHRASE CENSUSES (the crowns): "seven nations" ONE seat; "greater and mightier than you" three, all this book's (4:38, 7:1, 9:1); "you shall utterly destroy" 7:2 and 20:17;
# "you shall not make a covenant with them" 7:2 and Exodus 23:32 (34:12, 15 "lest"); "nor show them favor" ONE (the verb's six Torah seats — Jacob's "graciously given",
# Joseph's blessing, "I will be gracious"); "you shall not intermarry" 7:3 the Torah's ONE seat of the verb (Saul's "be my son-in-law" thrice; Joshua 23:12; Ezra 9:14);
# "the anger of the LORD will burn against you" 7:4, 11:17, Joshua 23:16; "their altars you shall tear down" 7:5 and Exodus 34:13; "Asherim" 7:5, 12:3 and Exodus 34:13 in the
# Torah; "burn with fire" the images 7:5, 7:25, 12:3; "holy people" five, all this book's (7:6, 14:2, 14:21, 26:19) and Daniel; "treasure" six (Exodus 19:5 the first;
# 7:6, 14:2, 26:18; Malachi; 1 Chronicles); "chose you" ONE; "the fewest of all peoples" ONE; "set His love" eight (10:15 the fathers; 21:11 the captive woman; Shechem);
# "because of the LORD's love for you" ONE; "the oath which He swore to your fathers" ONE — "the oath" (the noun) ten Torah seats (Genesis 26:3 "the oath"; Exodus 22:10 "the
# oath of the LORD"; the vows' chapter); "redeemed you from the house of bondage" ONE (the verb's six Deuteronomy seats); "from the hand of Pharaoh king of Egypt" ONE;
# "the faithful God" ONE; "the LORD your God, He is God" six (4:35, 39; 7:9; Solomon, Elijah, Manasseh); "keeps the covenant and the kindness" four (7:9; Solomon's prayer,
# Daniel's) — 7:12 the pair again; "to a thousand generations" 7:9, 1 Chronicles 16:15, Psalm 105:8; "to thousands" four (the ten words twice, 34:7, Jeremiah); "and repays
# those who hate Him to their face" ONE; "He will not delay" 7:10 and Habakkuk; "those who hate Me/Him" four Torah (the ten words twice, 7:10, Rebekah's blessing); "the
# commandment, the statutes and the judgments" — the triad 5:31, 6:1, 7:11; "which I command you today" eighteen; "because you hear" ONE (the noun "heel" as a conjunction:
# 7:12, 8:20, Genesis 22:18, 26:5, Numbers 14:24); "the fruit of your womb and the fruit of your ground" 7:13, 28:4, 28:18; "your grain, your wine and your oil" 7:13, 11:14,
# 12:17; "the increase of your cattle and the young of your flock" 7:13 and 28:51 (the flock word the goddess's name in the DB's morph — 7:13, 28:4, 18, 51); "barren" five
# Torah (Sarah, Rebekah, Rachel; Exodus 23:26); "the diseases of Egypt" 7:15 and 28:60; "your eye shall not pity" five, all this book's; "a snare" four Torah (Exodus 10:7,
# 23:33, 34:12; 7:16); "you shall not serve their gods" 7:16 and Exodus 23:33; "if you say in your heart" ONE (8:17 "and you say"); "how can I" ONE; "you shall not fear
# them" 7:18 and 20:1; "surely remember" ONE (the infinitive absolute 7:18 and Jeremiah 31:20); "the great trials" ONE ("trials" 4:34, 7:19, 16:10 — the freewill offering's
# homograph); "the signs and the wonders" five; "the strong hand and the outstretched arm" 5:15, 7:19, 26:8; "the hornet" Exodus 23:28, 7:20, Joshua 24:12 (the town Zorah
# the homograph); "those who hide" ONE; "you shall not be terrified" 7:21 (the verb 1:29, 20:3, 31:6); "a great and awesome God" ONE (10:17 "the great, the mighty and the
# awesome"); "in your midst" with "the LORD your God" 6:15, 7:21, Zephaniah; "little by little" 7:22 and Exodus 23:30; "the beasts of the field" eight Torah (Eden's; Exodus
# 23:29 the kin); "and He will give them before you" 7:2 and 7:23; "great confusion" ONE; "until they are destroyed" twelve; "destroy their name from under heaven" ONE (the
# phrase "from under heaven" eight — Amalek, the calf, the curse); "no man shall stand before you" 7:24 and Joshua 1:5; "YOU SHALL NOT COVET" 7:25 and Exodus 20:17 (5:21
# "and you shall not covet"); "silver and gold" with covet/take 7:25 and Zechariah 6:11 (Achan's "I coveted them and took them" the verb's kin, Joshua 7:21); "an abomination
# to the LORD your God" five and "abomination to the LORD" eight, all this book's (Proverbs' "abomination to the LORD" eleven); "abomination" thirteen Deuteronomy seats, 7:25-26 the first two; "you shall
# not bring an abomination into your house" ONE; "devoted like it" ONE; "utterly detest … utterly abhor" ONE (the detesting verb Leviticus 11's; the abhorring 23:8's "you
# shall not abhor an Edomite … an Egyptian"); "for it is devoted" ONE.
assert P('שבעה', 'גוים') == ['Deut 7:1'] and U('שבעה', books=('Deut',)) == ['Deut 16:9', 'Deut 7:1'] and P('רבים', 'ועצומים', 'ממך') + P('גדלים', 'ועצמים', 'ממך') == ['Deut 7:1', 'Deut 4:38', 'Deut 9:1'] and len(P('גוים', 'רבים')) == 15
assert U('ונשל') == ['Deut 19:5', 'Deut 7:1', 'Deut 7:22'] and P('החרם', 'תחרים') + P('החרם', 'תחרימם') == ['Deut 7:2', 'Deut 20:17'] and P('לא', 'תכרת', 'להם', 'ברית') + P('לא', 'תכרת', 'להם', 'ולאלהיהם', 'ברית') == ['Deut 7:2', 'Exod 23:32'] and P('פן', 'תכרת', 'ברית') == ['Exod 34:12', 'Exod 34:15']
assert U('תחנם') == ['Deut 7:2'] and len([1 for s, x, m in LEMT('2603 a', books=T) if m.startswith('HV')]) == 6 and lemma_of('Deut', 7, 2, 'תחנם') == ['2603 a']
assert U('תתחתן', 'התחתנו', 'התחתן', 'ותתחתנו', 'התחתנתם', 'תתחתנו') == ['1Sam 18:21', '1Sam 18:22', '1Sam 18:23', 'Deut 7:3'] and LEMV('2859 b', books=T) == ['Deut 7:3', 'Gen 34:9'] and P('בתך', 'לא', 'תתן', 'לבנו') == ['Deut 7:3'] and P('ולקחת', 'מבנתיו', 'לבניך') == ['Exod 34:16']
assert P('כי', 'יסיר', 'את', 'בנך', 'מאחרי') == ['Deut 7:4'] and P('וחרה', 'אף', 'יהוה', 'בכם') == ['Deut 11:17', 'Deut 7:4', 'Josh 23:16'] and P('והשמידך', 'מהר') == ['Deut 7:4'] and U('מהר', books=('Deut',)) == ['Deut 28:20', 'Deut 33:2', 'Deut 4:26', 'Deut 7:22', 'Deut 7:4', 'Deut 9:12', 'Deut 9:16', 'Deut 9:3']
assert P('מזבחתיהם', 'תתצו') + P('מזבחתם', 'תתצון') == ['Deut 7:5', 'Exod 34:13'] and U('ואשירהם', 'ואשריהם', 'אשריהם', 'ואשריו', 'אשריו', books=T) == ['Deut 12:3', 'Deut 7:5', 'Exod 34:13'] and U('תגדעון', 'תגדע', 'וגדעתם', 'תגדעו', books=T) == ['Deut 12:3', 'Deut 7:5'] and P('תשרפון', 'באש') == ['Deut 12:3', 'Deut 7:25', 'Deut 7:5']
assert sorted(LEMV('6456', books=T) + LEMV('6459', books=T)) == ['Deut 12:3', 'Deut 27:15', 'Deut 4:16', 'Deut 4:23', 'Deut 4:25', 'Deut 5:8', 'Deut 7:25', 'Deut 7:5', 'Exod 20:4', 'Lev 26:1']
assert P('עם', 'קדוש') + P('עם', 'קדש') == ['Deut 14:2', 'Deut 14:21', 'Deut 7:6', 'Dan 12:7', 'Deut 26:19'] and U('סגלה', 'לסגלה', 'וסגלה') == ['1Chr 29:3', 'Deut 14:2', 'Deut 26:18', 'Deut 7:6', 'Exod 19:5', 'Mal 3:17'] and P('בך', 'בחר', 'יהוה', 'אלהיך') == ['Deut 7:6'] and P('מכל', 'העמים', 'אשר', 'על', 'פני', 'האדמה') == ['Deut 14:2', 'Deut 7:6']
assert U('מרבכם') == ['Deut 7:7'] and LEMV('2836 a') == ['1Kgs 9:19', '2Chr 8:6', 'Deut 10:15', 'Deut 21:11', 'Deut 7:7', 'Gen 34:8', 'Isa 38:17', 'Ps 91:14'] and P('ויבחר', 'בכם') == ['Deut 7:7'] and P('אתם', 'המעט', 'מכל', 'העמים') == ['Deut 7:7'] and U('מעט', 'המעט', 'מעטים', 'ומעט', books=('Deut',)) == ['Deut 26:5', 'Deut 28:38', 'Deut 28:62', 'Deut 7:22', 'Deut 7:7']
assert P('מאהבת', 'יהוה', 'אתכם') == ['Deut 7:8'] and P('השבעה', 'אשר', 'נשבע', 'לאבתיכם') == ['Deut 7:8'] and [(s, x) for s, x, m in LEMT('7621', books=T)] == [('Deut 7:8', 'השבעה'), ('Exod 22:10', 'שבעת'), ('Gen 24:8', 'משבעתי'), ('Gen 26:3', 'השבעה'), ('Lev 5:4', 'בשבעה'), ('Num 5:21', 'בשבעת'), ('Num 5:21', 'ולשבעה'), ('Num 30:3', 'שבעה'), ('Num 30:11', 'בשבעה'), ('Num 30:14', 'שבעת')]
assert P('הוציא', 'יהוה', 'אתכם', 'ביד', 'חזקה') == ['Deut 7:8'] and P('ויפדך', 'מבית', 'עבדים') == ['Deut 7:8'] and [(s, x) for s, x, m in LEMT('6299', books=('Deut',))] == [('Deut 7:8', 'ויפדך'), ('Deut 9:26', 'פדית'), ('Deut 13:6', 'והפדך'), ('Deut 15:15', 'ויפדך'), ('Deut 21:8', 'פדית'), ('Deut 24:18', 'ויפדך')] and P('מיד', 'פרעה', 'מלך', 'מצרים') == ['Deut 7:8']
assert P('האל', 'הנאמן') == ['Deut 7:9'] and P('יהוה', 'אלהיך', 'הוא', 'האלהים') + P('יהוה', 'הוא', 'האלהים') == ['Deut 7:9', '1Kgs 18:39', '1Kgs 8:60', '2Chr 33:13', 'Deut 4:35', 'Deut 4:39'] and P('שמר', 'הברית', 'והחסד') == ['1Kgs 8:23', '2Chr 6:14', 'Dan 9:4', 'Deut 7:9'] and P('הברית', 'ואת', 'החסד') == ['Deut 7:12']
assert P('לאהביו', 'ולשמרי', 'מצותו') == ['Deut 7:9'] and P('לאהבי', 'ולשמרי', 'מצותי') == ['Exod 20:6'] and P('לאלף', 'דור') == ['1Chr 16:15', 'Deut 7:9', 'Ps 105:8'] and U('לאלפים') == ['Deut 5:10', 'Exod 20:6', 'Exod 34:7', 'Jer 32:18'] and U('אלף', 'לאלף', 'ואלף', books=('Deut',)) == ['Deut 1:11', 'Deut 32:30', 'Deut 7:9']
assert P('ומשלם', 'לשנאיו', 'אל', 'פניו') == ['Deut 7:10'] and U('להאבידו') == ['2Kgs 24:2', 'Deut 7:10'] and P('לא', 'יאחר') == ['Deut 7:10', 'Hab 2:3'] and U('לשנאי', 'לשנאיו', 'שנאיו', 'לשנאו', 'ולשנאיו', 'משנאיו', books=T) == ['Deut 5:9', 'Deut 7:10', 'Exod 20:5', 'Gen 24:60'] and P('פקד', 'עון', 'אבת') + P('פקד', 'עון', 'אבות') == ['Exod 20:5', 'Deut 5:9', 'Exod 34:7', 'Num 14:18']
assert P('ושמרת', 'את', 'המצוה', 'ואת', 'החקים', 'ואת', 'המשפטים') == ['Deut 7:11'] and [s for s in U('המצוה', books=('Deut',)) if s in U('והמשפטים', 'המשפטים', books=('Deut',))] == ['Deut 5:31', 'Deut 6:1', 'Deut 7:11'] and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18
assert P('והיה', 'עקב', 'תשמעון') == ['Deut 7:12'] and [(s, m) for s, x, m in LEMT('6118') if s.startswith(('Deut', 'Gen', 'Num'))] == [('Deut 7:12', 'HNcmsc'), ('Deut 8:20', 'HNcmsc'), ('Gen 22:18', 'HNcmsa'), ('Gen 26:5', 'HNcmsa'), ('Num 14:24', 'HC')] and U('תשמעון', books=('Deut',)) == ['Deut 18:15', 'Deut 1:17', 'Deut 7:12', 'Deut 8:20'] and P('ושמר', 'יהוה', 'אלהיך', 'לך', 'את', 'הברית') == ['Deut 7:12']
assert P('ואהבך', 'וברכך', 'והרבך') == ['Deut 7:13'] and P('פרי', 'בטנך', 'ופרי', 'אדמתך') == ['Deut 28:18', 'Deut 28:4', 'Deut 7:13'] and P('דגנך', 'ותירשך', 'ויצהרך') == ['Deut 11:14', 'Deut 12:17', 'Deut 7:13'] and P('שגר', 'אלפיך', 'ועשתרת', 'צאנך') == ['Deut 28:51', 'Deut 7:13'] and U('שגר', 'ושגר') == ['Deut 28:18', 'Deut 28:4', 'Deut 28:51', 'Deut 7:13', 'Exod 13:12']
assert [(s, x, m) for s, x, m in LEMT('6251')] == [('Deut 7:13', 'ועשתרת', 'HC/Np'), ('Deut 28:4', 'ועשתרות', 'HC/Np'), ('Deut 28:18', 'ועשתרות', 'HC/Np'), ('Deut 28:51', 'ועשתרת', 'HC/Np')]   # the flock's "young" tagged a NAME (Np) at its four seats — the goddess's homograph in the DB's morph
assert P('ברוך', 'תהיה', 'מכל', 'העמים') == ['Deut 7:14'] and P('לא', 'יהיה', 'בך', 'עקר', 'ועקרה') == ['Deut 7:14'] and U('עקר', 'עקרה', 'ועקרה', 'ועקר', books=T) == ['Deut 7:14', 'Exod 23:26', 'Gen 11:30', 'Gen 25:21', 'Gen 29:31'] and P('לא', 'תהיה', 'משכלה', 'ועקרה') == ['Exod 23:26']
assert P('והסיר', 'יהוה', 'ממך', 'כל', 'חלי') == ['Deut 7:15'] and P('מדוי', 'מצרים', 'הרעים') == ['Deut 7:15'] and U('מדוי', 'מדוה', 'ומדוה', 'במדוה') == ['Deut 28:60', 'Deut 7:15'] and P('כל', 'המחלה', 'אשר', 'שמתי', 'במצרים') == ['Exod 15:26'] and P('אשר', 'ידעת', books=('Deut',)) == ['Deut 7:15']
assert P('ואכלת', 'את', 'כל', 'העמים') == ['Deut 7:16'] and sorted(P('לא', 'תחס', 'עינך') + P('ולא', 'תחס', 'עינך') + P('לא', 'תחוס', 'עינך') + P('ולא', 'תחוס', 'עינך') + P('לא', 'תחס', 'עינכם')) == ['Deut 13:9', 'Deut 19:13', 'Deut 19:21', 'Deut 25:12', 'Deut 7:16'] and P('כי', 'מוקש', 'הוא', 'לך') == ['Deut 7:16'] and U('מוקש', 'למוקש', 'ולמוקש', 'מוקשים', books=T) == ['Deut 7:16', 'Exod 10:7', 'Exod 23:33', 'Exod 34:12'] and P('תעבד', 'את', 'אלהיהם') == ['Deut 7:16', 'Exod 23:33']
assert P('כי', 'תאמר', 'בלבבך') == ['Deut 7:17'] and P('ואמרת', 'בלבבך') == ['Deut 8:17', 'Isa 49:21'] and P('רבים', 'הגוים', 'האלה', 'ממני') == ['Deut 7:17'] and P('איכה', 'אוכל') == ['Deut 7:17'] and U('להורישם', books=T) == ['Deut 7:17'] and U('להורישם') == ['Deut 7:17', 'Josh 15:63']
assert P('לא', 'תירא', 'מהם') == ['Deut 20:1', 'Deut 7:18'] and U('תיראום') + P('אל', 'תיראו', 'מהם') == ['Deut 3:22', 'Jer 10:5'] and P('זכר', 'תזכר') == ['Deut 7:18'] and [(s, m) for s, x, m in LEMT('2142') if x == 'זכר' and m == 'HVqa'] == [('Deut 7:18', 'HVqa'), ('Jer 31:20', 'HVqa')] and P('עשה', 'יהוה', 'אלהיך', 'לפרעה', 'ולכל', 'מצרים') + P('עשה', 'יהוה', 'לפרעה') == ['Deut 7:18', 'Exod 18:8']
assert P('המסת', 'הגדלת') == ['Deut 7:19'] and U('מסת', 'המסת', 'במסת', 'ומסת') == ['Deut 16:10', 'Deut 4:34', 'Deut 7:19'] and lemma_of('Deut', 7, 19, 'המסת') == ['4531 b'] and lemma_of('Deut', 16, 10, 'מסת') != ['4531 b']   # the freewill offering's "measure" (16:10) the homograph
assert sorted(P('והאתת', 'והמפתים') + P('האתת', 'והמפתים') + P('האתות', 'והמופתים') + P('באתות', 'ובמופתים') + P('אתת', 'ומפתים')) == ['Deut 29:2', 'Deut 34:11', 'Deut 7:19', 'Jer 32:21', 'Neh 9:10'] and P('והיד', 'החזקה', 'והזרע', 'הנטויה') == ['Deut 7:19'] and P('ביד', 'חזקה', 'ובזרע', 'נטויה') == ['Deut 26:8', 'Deut 5:15'] and P('כן', 'יעשה', 'יהוה', 'אלהיך', 'לכל', 'העמים') == ['Deut 7:19'] and P('אשר', 'אתה', 'ירא', 'מפניהם') == ['Deut 7:19']
assert U('הצרעה', 'צרעה') == ['2Chr 11:10', 'Deut 7:20', 'Exod 23:28', 'Josh 19:41', 'Josh 24:12', 'Judg 13:25', 'Judg 16:31', 'Judg 18:8'] and P('ושלחתי', 'את', 'הצרעה', 'לפניך') == ['Exod 23:28'] and P('עד', 'אבד', 'הנשארים', 'והנסתרים') == ['Deut 7:20'] and U('הנסתרים', 'והנסתרים', 'נסתרים') == ['Deut 7:20']
assert P('לא', 'תערץ', 'מפניהם') == ['Deut 7:21'] and LEMV('6206', books=T) == ['Deut 1:29', 'Deut 20:3', 'Deut 31:6', 'Deut 7:21'] and P('יהוה', 'אלהיך', 'בקרבך') == ['Deut 6:15', 'Deut 7:21', 'Zeph 3:17'] and P('אל', 'גדול', 'ונורא') == ['Deut 7:21'] and P('האל', 'הגדל', 'הגבר', 'והנורא') == ['Deut 10:17']
assert P('מעט', 'מעט') == ['Deut 7:22', 'Exod 23:30'] and P('לא', 'תוכל', 'כלתם', 'מהר') == ['Deut 7:22'] and P('פן', 'תרבה', 'עליך', 'חית', 'השדה') == ['Deut 7:22'] and P('חית', 'השדה', books=T) == ['Deut 7:22', 'Exod 23:11', 'Exod 23:29', 'Gen 2:19', 'Gen 2:20', 'Gen 3:1', 'Gen 3:14', 'Lev 26:22'] and P('בשנה', 'אחת') == ['1Kgs 10:14', '2Chr 9:13', 'Exod 23:29']
assert P('ונתנם', 'יהוה', 'אלהיך', 'לפניך') == ['Deut 7:2', 'Deut 7:23'] and P('והמם', 'מהומה', 'גדלה') == ['Deut 7:23'] and len(U('השמדם', 'השמדך', 'השמדו', 'להשמידם', 'להשמידך')) == 12 and P('ונתן', 'מלכיהם', 'בידך') == ['Deut 7:24'] and P('והאבדת', 'את', 'שמם', 'מתחת', 'השמים') == ['Deut 7:24']
assert P('מתחת', 'השמים') == ['2Kgs 14:27', 'Deut 25:19', 'Deut 29:19', 'Deut 7:24', 'Deut 9:14', 'Exod 17:14', 'Gen 1:9', 'Gen 6:17'] and P('לא', 'יתיצב', 'איש', 'בפניך') + P('לא', 'יתיצב', 'איש', 'לפניך') == ['Deut 7:24', 'Josh 1:5'] and P('תמחה', 'את', 'זכר') + P('מחה', 'אמחה', 'את', 'זכר') + P('ומחה', 'יהוה', 'את', 'שמו') == ['Deut 25:19', 'Exod 17:14', 'Deut 29:19']
assert P('פסילי', 'אלהיהם', 'תשרפון', 'באש') == ['Deut 7:25'] and P('לא', 'תחמד') == ['Deut 7:25', 'Exod 20:17'] and P('ולא', 'תחמד') + P('ולא', 'תתאוה') == ['Deut 5:21', 'Deut 5:21'] and [s for s in P('כסף', 'וזהב') if s in U('תחמד', 'ואחמדם', 'ולקחת', 'ואקחם')] == ['Deut 7:25', 'Zech 6:11'] and P('פן', 'תוקש', 'בו') == ['Deut 7:25']
assert sorted(set(P('תועבת', 'יהוה', 'אלהיך'))) == ['Deut 17:1', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 7:25'] and sorted(set(P('תועבת', 'יהוה', books=T))) == ['Deut 12:31', 'Deut 17:1', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25'] and len(set(P('תועבת', 'יהוה'))) == 19 and U('תועבה', 'תועבת', 'התועבה', 'התועבת', 'תועבות', 'התועבות', 'ותועבת', books=('Deut',)) == ['Deut 12:31', 'Deut 13:15', 'Deut 14:3', 'Deut 17:1', 'Deut 17:4', 'Deut 18:12', 'Deut 22:5', 'Deut 23:19', 'Deut 24:4', 'Deut 25:16', 'Deut 27:15', 'Deut 7:25', 'Deut 7:26']
assert P('ולא', 'תביא', 'תועבה', 'אל', 'ביתך') == ['Deut 7:26'] and P('והיית', 'חרם', 'כמהו') == ['Deut 7:26'] and P('שקץ', 'תשקצנו', 'ותעב', 'תתעבנו') == ['Deut 7:26'] and [(s, x) for s, x, m in LEMT('8262', books=T)] == [('Deut 7:26', 'שקץ'), ('Deut 7:26', 'תשקצנו'), ('Lev 11:11', 'תשקצו'), ('Lev 11:13', 'תשקצו'), ('Lev 11:43', 'תשקצו'), ('Lev 20:25', 'תשקצו')] and [(s, x) for s, x, m in LEMT('8581', books=T)] == [('Deut 7:26', 'ותעב'), ('Deut 7:26', 'תתעבנו'), ('Deut 23:8', 'תתעב'), ('Deut 23:8', 'תתעב')] and P('כי', 'חרם', 'הוא') == ['Deut 7:26']
assert lemma_of('Deut', 7, 26, 'חרם') == ['2764 a', '2764 a'] and lemma_of('Deut', 7, 2, 'החרם') == ['2763 a'] and lemma_of('Deut', 7, 2, 'תחרים') == ['2763 a'] and lemma_of('Deut', 20, 17, 'תחרימם') == ['2763 a']
# ONKELOS CHAPTER 7 — THE RENDERINGS' SEATS over the whole book (computed on the plain Aramaic of every export row; the export's chapter 7 = the DB's): 7:2 "utterly destroy" MADE
# "utterly annihilate" (7:2 and 20:17 — the two seats of the ban's verb), "nor show them favor" MADE "have no MERCY on them" (7:2, 13:9 the enticer); 7:4 "from after Me" MADE
# "from after MY SERVICE", "other gods" MADE "the IDOLS of the peoples" (eight); 7:5 "their altars" the idolaters' word (7:5, 12:3), "their graven images" MADE "the images of their
# idols" (7:5, 7:25, 12:3); 7:6 "a treasured people" MADE "a BELOVED people" (7:6, 14:2, 26:18); 7:7 "set His love" MADE "desired" (7:7, 10:15); 7:8 "the oath which He swore"
# MADE "the covenant which He established" — the oath's noun and verb both the covenant's word; 7:9 "the faithful God" MADE "the faithful God" (7:9, 32:4), "TO A THOUSAND
# GENERATIONS" MADE "TO THOUSANDS OF GENERATIONS" — the plural of the ten words' "to thousands" at 5:10, the two seats; 7:10 THE SUPPLIED DOCTRINE: "He repays those who hate Him
# THE GOOD THEY DO BEFORE HIM IN THEIR LIFETIME, to destroy them; He does not delay THE GOOD DEED of those who hate Him …" — the verse doubled in length, the six bracketed
# supplements of the English; 7:12 "because" MADE "in exchange for" (six seats, 1:36 Caleb's the first); 7:13 the cattle's "increase" and the flock's "young" MADE "the herds
# of your oxen and the flocks of your sheep" (7:13, 28:4, 18, 51); 7:15 "diseases" MADE "plagues" (7:15, 28:60); 7:16 "consume" MADE "finish off", "a snare" MADE "a
# stumbling-block" (one); 7:18 "surely remember" doubled as in the ink; 7:19 "the trials" MADE "the MIRACLES" (4:34, 7:19, 16:1 — the trial's word for the wonder; 6:16's
# Massah "the trial" another word); 7:20 "the hornet" ONE seat; 7:21 "in your midst" MADE "HIS SHEKHINAH IS AMONG YOU" (6:15, 7:21 — the pair; twelve seats of the word);
# 7:22 "little by little" ONE; 7:23 "confusion" ONE; 7:24 "no man shall stand" (7:24, 11:25); 7:25 "an abomination to the LORD" MADE "a thing DISTANCED before the LORD"
# (7:25, 24:4, 27:15), 7:26 "devoted" the same word (7:26, 13:18), "detest … abhor" MADE "detest … keep far" — the abhorring verb the distancing's; the English's eleven
# bracketed supplements over nine verses, six of them at 7:10; no parenthesised variant in the chapter's Hebrew rows.
assert onk_tok('גמרא') == [(7, 2), (20, 17)] and onk_tok('תרחם') == [(7, 2), (13, 9)] and onk_tok('פלחני') == [(7, 4)] and len(onk_tok('לטעות')) == 8 and onk_tok('אגוריהון') == [(7, 5), (12, 3)] and onk_tok('טעותהון') == [(7, 5), (7, 16), (7, 25), (12, 2), (12, 3), (12, 30), (29, 16)] and onk_seats('צלמי טעותהון') == [(7, 5), (7, 25), (12, 3)]
assert onk_tok('חביב') == [(7, 6), (14, 2), (26, 18)] and onk_tok('צבי') == [(7, 7), (10, 15), (25, 7)] and onk_tok('זערין') == [(7, 7)] and onk_seats('ית קימא די קיים') == [(7, 8)] and onk_tok('מהימנא') == [(7, 9), (32, 4)] and onk_seats('לאלפי דרין') == [(5, 10), (7, 9)] and onk_tok('לאלפי') == [(5, 10), (7, 9)]
assert onk_seats('טבן די אנון עבדין קדמוהי בחייהון') == [(7, 10)] and onk_tok('בחייהון') == [(7, 10)] and len(aramaic(7, 10)) == 22 and len(W7(10)) == 12 and onk_tok('חלף') == [(1, 36), (7, 12), (8, 20), (19, 21), (21, 14), (22, 29), (28, 47), (28, 62)]
assert onk_seats('בקרי תוריך') == [(7, 13), (28, 4), (28, 18), (28, 51)] and onk_seats('ועדרי ענך') == [(7, 13), (28, 4), (28, 18), (28, 51)] and onk_tok('מכתשי') == [(7, 15), (28, 60), (32, 23)] and onk_tok('ותגמר') == [(7, 16)] and onk_tok('לתקלא') == [(7, 16)] and onk_seats('מדכר תדכר') == [(7, 18)]
assert onk_tok('נסין') == [(4, 34), (7, 19), (16, 1)] and onk_tok('ערעיתא') == [(7, 20)] and onk_seats('שכנתיה בינך') == [(6, 15), (7, 21)] and len(onk_tok('שכנתיה')) == 12 and onk_seats('זער זער') == [(7, 22)] and onk_tok('שגוש') == [(7, 23)] and onk_seats('לא יתעתד אנש') == [(7, 24), (11, 25)]
assert onk_tok('מרחקא') == [(7, 25), (24, 4), (27, 15)] and onk_tok('חרמא') == [(7, 26), (13, 18)] and onk_seats('שקצא תשקצניה') == [(7, 26)] and onk_seats('ורחקא תרחקניה') == [(7, 26)] and onk_tok('דמרחק') == [(7, 26), (12, 31), (14, 3)]
assert [(v + 1) for v in range(len(onk_he[6])) if '(' in clean(onk_he[6][v])] == [] and len([(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if '(' in clean(onk_he[c][v])]) == 10
BR = {e: re.findall(r'\[([^\]]+)\]', clean(onk[6][e - 1])) for e in range(1, 27)}
BR = {e: b for e, b in BR.items() if b}
assert BR == {2: ['show mercy on'], 4: ['My service', 'idols of the nations'], 5: ['idols'], 10: ['for the good that they have done before Him', 'in their lifetime', 'to do good', 'for the good that they have done before Him', 'in their lifetime', 'them'], 12: ['in exchange for'], 16: ['idols'], 20: ['set upon'], 21: ['His Shechinah'], 25: ['idols'], 26: ['lest', 'distance']}, BR
assert sum(len(b) for b in BR.values()) == 17 and "tzir’oh" in clean(onk[6][19]) and clean(onk[6][25]).count('cheirem') == 2
# THE STORE'S GLOSSES at the chapter's seats (words.gloss, read back): the families censused over the whole store (ch7_measure1.py G) — the rewrite planned BY GLOSS where every
# token of the gloss is the one word (or one family read the same at every seat), BY REFERENCE where the family is mixed; applied at run 3 (the display layer), asserted here as the plan.
assert sg(7, 1, 'ונשל') == 'and-pluck-off' and sg(7, 1, 'שבעה') == 'seven' and sg(7, 1, 'ועצומים') == 'and-powerful' and sg(7, 2, 'החרם') == 'seclude' and sg(7, 2, 'תחרים') == 'seclude' and sg(7, 2, 'תחנם') == 'bend-them/their' and sg(7, 2, 'והכיתם') == 'and-strike-them/their' and sg(7, 2, 'ונתנם') == 'and-set-them/their'
assert sg(7, 3, 'תתחתן') == 'give--away-in-marriage' and sg(7, 4, 'יסיר') == 'turn-aside' and sg(7, 4, 'מאחרי') == 'from-hind-part-me/my' and sg(7, 4, 'אחרים') == 'hinder' and sg(7, 4, 'וחרה') == 'and-glow' and sg(7, 4, 'אף') == 'nose' and sg(7, 4, 'מהר') == 'hurrying' and sg(7, 4, 'והשמידך') == 'and-desolate-you/your'
assert sg(7, 5, 'כי') == 'very-widely-used-as-a-relati' and sg(7, 5, 'אם') == 'as-demonstrative' and sg(7, 5, 'כה') == 'like-this' and sg(7, 5, 'ומצבתם') == 'and-something-stationed-them/their' and sg(7, 5, 'תשברו') == 'burst' and sg(7, 5, 'תגדעון') == 'fell-a-tree-suffix' and sg(7, 5, 'ופסיליהם') == 'and-idol-them/their' and sg(7, 5, 'תשרפון') == 'be--on-fire-suffix'
assert sg(7, 6, 'בחר') == 'try' and sg(7, 6, 'סגלה') == 'wealth' and sg(7, 6, 'קדוש') == 'sacred' and sg(7, 7, 'חשק') == 'cling' and sg(7, 7, 'ויבחר') == 'and-try' and sg(7, 7, 'המעט') == 'the-little' and sg(7, 7, 'מרבכם') == 'from-abundance-you/your (pl)' and sg(7, 7, 'העמים') == 'the-people'
assert sg(7, 8, 'השבעה') == 'the-something-sworn' and sg(7, 8, 'ויפדך') == 'and-sever-you/your' and sg(7, 9, 'האל') == 'the-strength' and sg(7, 9, 'הנאמן') == 'the-build-up' and sg(7, 9, 'לאהביו') == 'to-have-affection-for-him/its' and sg(7, 9, 'מצותו') == 'commandment-him/its' and sg(7, 9, 'מצותיו') == 'commandment-him/its'
assert sg(7, 10, 'ומשלם') == 'and-be-safe' and sg(7, 10, 'ישלם') == 'be-safe' and sg(7, 10, 'להאבידו') == 'to-wander-away-him/its' and sg(7, 10, 'יאחר') == 'loiter' and sg(7, 11, 'אנכי') == '?' and sg(7, 12, 'עקב') == 'heel' and sg(7, 12, 'תשמעון') == 'hear-suffix'
assert sg(7, 13, 'ואהבך') == 'and-have-affection-for-you/your' and sg(7, 13, 'דגנך') == 'increase-you/your' and sg(7, 13, 'ותירשך') == 'and-must-you/your' and sg(7, 13, 'שגר') == 'fetus' and sg(7, 13, 'אלפיך') == 'family-you/your' and sg(7, 13, 'ועשתרת') == "and-'Ashtᵉrah" and sg(7, 14, 'עקר') == 'sterile' and sg(7, 14, 'ועקרה') == 'and-sterile' and sg(7, 14, 'ובבהמתך') == 'and-in-livestock-you/your'
assert sg(7, 15, 'והסיר') == 'and-turn-aside' and sg(7, 15, 'חלי') == 'malady' and sg(7, 15, 'מדוי') == 'sickness' and sg(7, 16, 'תחס') == 'cover' and sg(7, 16, 'מוקש') == 'noose' and sg(7, 17, 'להורישם') == 'to-possess/inherit-them/their' and sg(7, 17, 'הגוים') == 'the-nation' and sg(7, 18, 'זכר') == 'mark' and sg(7, 18, 'תזכר') == 'mark'
assert sg(7, 19, 'המסת') == 'the-testing' and sg(7, 19, 'הנטויה') == 'the-stretch' and sg(7, 20, 'הצרעה') == 'the-wasp' and sg(7, 20, 'הנשארים') == 'the-swell-up' and sg(7, 20, 'והנסתרים') == 'and-the-hide' and sg(7, 21, 'תערץ') == 'awe' and sg(7, 21, 'אל') == 'strength' and sg(7, 21, 'ונורא') == 'and-fear' and sg(7, 21, 'בקרבך') == 'in-nearest-part-you/your'
assert sg(7, 22, 'ונשל') == 'and-pluck-off' and sg(7, 22, 'כלתם') == 'be-complete-them/their' and sg(7, 22, 'חית') == 'living' and sg(7, 23, 'והמם') == 'and-put-in-commotion-them/their' and sg(7, 23, 'מהומה') == 'confusion' and sg(7, 23, 'השמדם') == 'desolate-them/their' and sg(7, 24, 'יתיצב') == 'place' and sg(7, 24, 'השמדך') == 'desolate-you/your'
assert sg(7, 25, 'פסילי') == 'idol' and sg(7, 25, 'תחמד') == 'delight-in' and sg(7, 25, 'תוקש') == 'ensnare' and sg(7, 25, 'תועבת') == 'something-disgusting' and sg(7, 26, 'תועבה') == 'something-disgusting' and sg(7, 26, 'חרם') == 'physical--a-net' and sg(7, 26, 'כמהו') == "form-of-the-prefix-'k-'-him/its" and sg(7, 26, 'שקץ') == 'be-filthy' and sg(7, 26, 'תשקצנו') == 'be-filthy-him/its' and sg(7, 26, 'ותעב') == 'and-loathe' and sg(7, 26, 'תתעבנו') == 'loathe-him/its'
GLOSS_FAMILY = {'seclude': [('החרם', 4), ('יחרם', 3), ('חרם', 1), ('תחרים', 1)], 'bend-them/their': [('תחנם', 1)], 'try': [('יבחר', 25), ('בחר', 5), ('אבחר', 1), ('בחור', 1), ('בחרו', 1)], 'and-try': [('ויבחר', 5), ('ובחרת', 1)], 'wealth': [('סגלה', 4)], 'the-something-sworn': [('השבעה', 2)], 'and-sever-you/your': [('ויפדך', 3)], 'the-strength': [('האל', 4)], 'the-build-up': [('האמן', 1), ('הנאמן', 1)], 'to-have-affection-for-him/its': [('לאהביו', 1)], 'and-have-affection-for-you/your': [('ואהבך', 1)], 'to-wander-away-him/its': [('להאבידו', 1)], 'loiter': [('תאחר', 2), ('אחר', 1), ('יאחר', 1), ('תאחרו', 1)], 'increase-you/your': [('דגנך', 5)], 'and-must-you/your': [('ותירשך', 3)], 'fetus': [('שגר', 5)], 'family-you/your': [('אלפיך', 4)], "and-'Ashtᵉrah": [('ועשתרות', 2), ('ועשתרת', 2)], 'sterile': [('עקרה', 3), ('עקר', 1)], 'and-sterile': [('ועקרה', 2)], 'malady': [('חלי', 2)], 'noose': [('מוקש', 1)], 'the-testing': [('המסות', 1), ('המסת', 1)], 'the-stretch': [('הנטויה', 3)], 'the-wasp': [('הצרעה', 2)], 'the-swell-up': [('הנשאר', 1), ('הנשארים', 1), ('הנשארת', 1)], 'and-the-hide': [('והנסתרים', 1)], 'awe': [('תערצו', 2), ('תערץ', 1)], 'be-complete-them/their': [('כלתם', 1)], 'and-put-in-commotion-them/their': [('והמם', 1)], 'ensnare': [('תוקש', 1)], 'something-disgusting': [('תועבת', 11), ('תועבה', 6)], 'physical--a-net': [('חרם', 6)], 'be-filthy': [('תשקצו', 4), ('שקץ', 1)], 'be-filthy-him/its': [('תשקצנו', 1)], 'and-loathe': [('ותעב', 1)], 'loathe-him/its': [('תתעבנו', 1)], 'and-something-stationed-them/their': [('ומצבתם', 1)], 'burst': [('תשברו', 3), ('ישבר', 2), ('שברת', 2), ('ישברו', 1), ('נשבר', 1), ('שבור', 1), ('שבר', 1), ('תשבר', 1)], 'fell-a-tree-suffix': [('תגדעון', 2)], 'be--on-fire-suffix': [('תשרפון', 3)], 'hurrying': [('מהר', 9)], 'from-hind-part-me/my': [('מאחרי', 1)], 'from-abundance-you/your (pl)': [('מרבכם', 1)], 'and-in-livestock-you/your': [('ובבהמתך', 1)], 'to-possess/inherit-them/their': [('להורישם', 1)], 'and-idol-them/their': [('ופסיליהם', 1)], 'idol': [('פסל', 6), ('פסילי', 1)], 'altar-them/their': [('מזבחתם', 2), ('מזבחתיהם', 1)], 'and-pluck-off': [('ונשל', 3), ('וגזול', 1), ('וטרף', 1)], 'cling': [('חשק', 2), ('מחשקים', 2), ('חשקה', 1)], 'and-be-safe': [('ומשלם', 1), ('ושלם', 1)], 'heel': [('עקב', 7), ('עקבי', 1)], 'the-little': [('המעט', 6), ('הצעירה', 4), ('הצעיר', 1)], 'hear-suffix': [('ישמעון', 4), ('תשמעון', 4)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store
OVERRIDE_GLOSS = [('seclude', 'ban'), ('bend-them/their', 'show-them-favor'), ('try', 'choose'), ('and-try', 'and-choose'), ('wealth', 'treasure'), ('the-something-sworn', 'the-oath'), ('and-sever-you/your', 'and-redeemed-you'), ('the-strength', 'the-God'), ('the-build-up', 'the-faithful'), ('to-have-affection-for-him/its', 'to-those-who-love-him'), ('and-have-affection-for-you/your', 'and-he-will-love-you'), ('to-wander-away-him/its', 'to-destroy-him'), ('loiter', 'delay'), ('increase-you/your', 'your-grain'), ('and-must-you/your', 'and-your-wine'), ('fetus', 'the-increase-of'), ('family-you/your', 'your-cattle'), ("and-'Ashtᵉrah", 'and-the-young-of'), ('sterile', 'barren'), ('and-sterile', 'and-barren'), ('malady', 'sickness'), ('noose', 'a-snare'), ('the-testing', 'the-trials'), ('the-stretch', 'the-outstretched'), ('the-wasp', 'the-hornet'), ('the-swell-up', 'the-remaining'), ('and-the-hide', 'and-those-who-hide'), ('awe', 'be-terrified'), ('be-complete-them/their', 'to-finish-them'), ('and-put-in-commotion-them/their', 'and-throw-them-into-confusion'), ('ensnare', 'be-snared'), ('something-disgusting', 'abomination'), ('physical--a-net', 'devoted'), ('be-filthy', 'detest'), ('be-filthy-him/its', 'detest-it'), ('and-loathe', 'and-abhor'), ('loathe-him/its', 'abhor-it'), ('and-something-stationed-them/their', 'and-their-pillars'), ('burst', 'break'), ('fell-a-tree-suffix', 'you-shall-cut-down'), ('be--on-fire-suffix', 'you-shall-burn'), ('hurrying', 'quickly'), ('from-hind-part-me/my', 'from-following-me'), ('from-abundance-you/your (pl)', 'because-of-your-multitude'), ('and-in-livestock-you/your', 'and-among-your-livestock'), ('to-possess/inherit-them/their', 'to-dispossess-them'), ('and-idol-them/their', 'and-their-graven-images'), ('idol', 'graven-image'), ('altar-them/their', 'their-altars')]
# BY REFERENCE — the family mixed (a homograph, two persons, a singular beside a plural): the seat named
OVERRIDE_REF_SPEC = [(1, 'ונשל', 'and-he-will-clear-away', 0), (22, 'ונשל', 'and-he-will-clear-away', 0), (1, 'גוים', 'nations', 0), (1, 'גוים', 'nations', 1), (17, 'הגוים', 'the-nations', 0), (22, 'הגוים', 'the-nations', 0), (2, 'והכיתם', 'and-you-shall-smite-them', 0), (2, 'ונתנם', 'and-he-will-give-them', 0), (23, 'ונתנם', 'and-he-will-give-them', 0), (15, 'ונתנם', 'and-he-will-give-them', 0), (4, 'יסיר', 'he-will-turn-away', 0), (4, 'וחרה', 'and-will-burn', 0), (4, 'אף', 'the-anger', 0), (5, 'כי', 'but', 0), (5, 'אם', 'rather', 0), (5, 'כה', 'thus', 0), (6, 'העמים', 'the-peoples', 0), (7, 'העמים', 'the-peoples', 0), (7, 'העמים', 'the-peoples', 1), (14, 'העמים', 'the-peoples', 0), (16, 'העמים', 'the-peoples', 0), (19, 'העמים', 'the-peoples', 0), (7, 'חשק', 'set-his-love', 0), (7, 'המעט', 'the-fewest', 0), (10, 'ומשלם', 'and-he-repays', 0), (10, 'ישלם', 'he-repays', 0), (11, 'אנכי', 'I', 0), (12, 'עקב', 'because', 0), (12, 'תשמעון', 'you-hear', 0), (15, 'והסיר', 'and-he-will-remove', 0), (16, 'תחס', 'shall-pity', 0), (18, 'זכר', 'remember', 0), (18, 'תזכר', 'you-shall-remember', 0), (21, 'אל', 'God', 0), (21, 'ונורא', 'and-awesome', 0), (24, 'יתיצב', 'shall-stand', 0)]
OVERRIDE_REF3 = [(f'Deut.7.{v}:{sidx(7, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == 36 and len({k for k, _ in OVERRIDE_REF}) == 36 and len(OVERRIDE_GLOSS) == 49 and len({k for k, _ in OVERRIDE_GLOSS}) == 49, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(7, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = ['hinder', 'delight-in', "form-of-the-prefix-'k-'-him/its", 'desolate-them/their', 'and-desolate-you/your', 'in-nearest-part-you/your']   # the rewrites of sittings 1-4 the chapter shares, left standing ("other", "covet", "like-it", "destroyed-them", "and-destroy-you", "in-your-midst")
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)' in OV
assert all(f'"{k}": ' in OV for k in ALREADY) and all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS if not PATCHED) and (PATCHED or '"Deut.7.' not in OV), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
if PATCHED: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "Deut.6.20:5": "what"') == 1
