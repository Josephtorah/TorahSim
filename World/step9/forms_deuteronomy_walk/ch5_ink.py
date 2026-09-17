#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 3 — CHAPTER 5, Deuteronomy 5:1-33 (2026-09-16; the owner: "go" after the rereads, on the rulings READ THEN
# COMPILE PER PORTION and CHAPTER NUMBERS): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes —
# never typed. Sitting 2's form (ch4_ink.py). THE TWO DIVISIONS: the export's chapter 5 has THIRTY verses against the DB's THIRTY-THREE — the
# export's 17 is the DB's 17-20 (four negations, twelve tokens), its 18 the DB's 21, its 19-30 the DB's 22-33 — the map computed by a monotone
# alignment over token and negation counts (ch5_dump0.py) and asserted here; every export address (Onkelos rows, the Sifrei's citations) is
# mapped to the DB's. THE SIFREI ON DEUTERONOMY HAS NO PISKA ON CHAPTER 5 either — 30 heads on 3:29, 31 on 6:4; the whole export scanned in
# both files: FIVE Hebrew rows, SIX English (41:4 the English's alone — a continuation row citing 5:1 with no parenthesis in its Hebrew); one
# read at sitting 1 (20:1, the mob and the elders), FIVE FRESH. The parser MEASURED on every verse — three number verses, the third generation
# STARRED (not thirty), NO GAP. The two copies of the ten words DIFFED verse by verse (172 tokens / 620 letters against 189 / 708). The hand's
# facts as asserts, run all at once by assert_driver.py after the measurement passes (ch5_dump0.py, ch5_measure1.py) printed them.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-16'
CH = 5
UIDS = ['deu_05_decalogue']
SPANS = {'deu_05_decalogue': (5, 1, 33)}
PREFIX = {'deu_05_decalogue': 'DV05'}
PISKAOT = []
EXP2DB = {e: [e] for e in range(1, 17)}; EXP2DB[17] = [17, 18, 19, 20]; EXP2DB[18] = [21]; EXP2DB.update({e: [e + 3] for e in range(19, 31)})
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
OUTSIDE_HE = [(20, 1, (5, 20)), (41, 1, (5, 1)), (233, 1, (5, 12)), (306, 16, (5, 19)), (357, 40, (5, 28))]            # the EXPORT's verse numbers
OUTSIDE_EN = [(20, 1, (5, 20)), (41, 1, (5, 1)), (41, 4, (5, 1)), (233, 1, (5, 12)), (306, 16, (5, 19)), (357, 40, (5, 28))]
OUTSIDE = sorted({(p, r) for p, r, _ in OUTSIDE_HE} | {(p, r) for p, r, _ in OUTSIDE_EN})
CITED_DB = {(p, r): EXP2DB[v][0] for p, r, (c, v) in OUTSIDE_EN}     # the DB verse each row cites: 20:1 → 5:23, 41:1/41:4 → 5:1, 233:1 → 5:12, 306:16 → 5:22, 357:40 → 5:31
FRESH = [(41, 1), (41, 4), (233, 1), (306, 16), (357, 40)]
CREDITED = {(20, 1): 'read FRESH at sitting 1 (the deu_01_03 ledger, MATERIAL — the row on 1:22: the mob against 5:23\'s elders and heads)'}
TITLE = 'Chapter 5 — Moses called all Israel: hear the statutes and the judgments, learn them, keep them to do them; the LORD our God made a covenant with us at Horeb — not with our fathers but with us, alive here this day; face to face the LORD spoke with you from the midst of the fire, I standing between the LORD and you, for you feared the fire, saying: I am the LORD your God who brought you out of Egypt, the house of bondage; no other gods before me; no graven image, any form, in heaven above, earth beneath, the waters under the earth — bow not, serve not, for I am a jealous God visiting the fathers\' iniquity on the third and the fourth of those who hate me and doing kindness to thousands who love me; take not the Name in vain; KEEP the sabbath day as the LORD your God commanded you — six days labor, the seventh the sabbath, no work by you, your son, your daughter, your servants, your ox and your ass and all your cattle, your stranger, that your servants rest like you: remember you were a slave in Egypt and the LORD brought you out with a mighty hand and an outstretched arm; honor your father and your mother as the LORD your God commanded you, that your days be long and it go well with you; you shall not murder, and not commit adultery, and not steal, and not answer against your neighbor a vain witness, and not covet your neighbor\'s wife, and not desire his house, his field, his servants, his ox, his ass, all that is his. These words the LORD spoke to all your assembly in the mountain from the fire, the cloud and the thick darkness, a great voice, and added no more; he wrote them on two tablets of stone and gave them to me. When you heard the voice from the darkness, the mountain burning, you came near to me, the heads of your tribes and your elders: the LORD our God has shown us his glory and his greatness, we heard his voice from the fire — this day we saw that God speaks with man and he lives; now why should we die, this great fire will consume us; who of all flesh heard the living God speak from the fire as we and lived? You go near and hear, and speak to us, and we will hear and do. The LORD heard the voice of your words: they have well said — who would give that this their heart be theirs, to fear me and keep my commandments all the days, that it go well with them and their sons forever; go say to them: return to your tents; and you, stand here with me, and I will speak to you all the commandment, the statutes and the judgments you shall teach them to do in the land I give them. Keep to do as the LORD your God commanded you, turn not right or left; walk in all the way he commanded, that you may live and it be well with you and you prolong days in the land you shall possess'
OUT = f'{ROOT}/logic/oral_triage/deu_05_vaetchanan_{DATE}.md'

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
# THE SHELF BY POSITION — the two files' grains, the heads around the chapter, NO piska on chapter 5
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
assert {p: heads[p] for p in range(28, 35)} == {28: (3, 25), 29: (3, 26), 30: (3, 29), 31: (6, 4), 32: (6, 5), 33: (6, 6), 34: (6, 7)}, {p: heads[p] for p in range(28, 35)}
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 5] == [] and HC[5] == 0 and HC[4] == 0 and sorted(HC.items())[:8] == [(1, 24), (3, 4), (6, 6), (11, 21), (12, 20), (13, 14), (14, 14), (15, 16)], sorted(HC.items())[:8]
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
CIT_HE = [(p, r, (5, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 5]
CIT_EN = [(p, r, (5, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(5):(\d+)', E(p, r))]
assert CIT_HE == OUTSIDE_HE and CIT_EN == OUTSIDE_EN and len(OUTSIDE) == 6 and OUTSIDE == [(20, 1), (41, 1), (41, 4), (233, 1), (306, 16), (357, 40)], (CIT_HE, CIT_EN)
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?5:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE} == {20: (1, 22), 41: (11, 13), 233: (22, 11), 306: (32, 1), 357: (34, 1)}
assert CITED_DB == {(20, 1): 23, (41, 1): 1, (41, 4): 1, (233, 1): 12, (306, 16): 22, (357, 40): 31}
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE) and all(re.search(r'\(Dt\.5:\d+\)', E(p, r)) for p, r in OUTSIDE)
assert '(דברים ה כ)' in Hb(20, 1) and '(דברים ה א)' in Hb(41, 1) and [c for c in he_cites(Hb(41, 4)) if c[0] == 'דברים'] == [] and he_cites(Hb(41, 4)) == [('הושע', 4, 1)] and '(דברים ה יב)' in Hb(233, 1) and '(דברים ה יט)' in Hb(306, 16) and '(דברים ה כח)' in Hb(357, 40)
assert '(Dt.5:1)' in E(41, 4) and E(41, 4).startswith('2. “Study them and take care to observe them.” (Dt.5:1)') and Hb(41, 4).startswith('וּלְמַדְתֶּם אוֹתָם וּשְׁמַרְתֶּם לַעֲשׂוֹתָם')   # the continuation row: the Hebrew quotes 5:1 with no citation, the English cites it
assert '(שמות כ ח)' in Hb(233, 1) and '(Ex.20:8)' in E(233, 1) and 'בְּדִבּוּר אֶחָד' in Hb(233, 1) and Hb(233, 1).count('בְּדִבּוּר אֶחָד') == 2 and 'Mechilta Ishmael, bakhodesh, 7' in E(233, 1)   # "remember" and "keep" in one utterance — the pair of copies cited together
assert E(306, 16).count('words of Torah') == 3 and Hb(306, 16).count('דִּבְרֵי תוֹרָה') == 3 and Hb(357, 40).count('מֹשֶׁה לֹא הָיָה') == 3 and '(במדבר כד ד)' in Hb(357, 40)
assert 'בְּעִרְבּוּבְיָא' in Hb(20, 1) and Hb(20, 1).count('בְּעִרְבּוּבְיָא') == 2 and 'confused mob' in E(20, 1) and 'Sifre Nu 136' in E(20, 1)
# THE PRIOR READS — the strict row form over every ledger: one of the six rows read at sitting 1, the five FRESH
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE] == [('deu_01_03_devarim_2026-09-15.md', 20, 1)] and len(PRIOR) == 213, len(PRIOR)
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 5:', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod 20:', t, re.M)) == []   # neither copy of the ten words has an Onkelos row anywhere
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 5:\d+', t))
assert len(NAMING) == 10 and 'num_35_refuge_cities_2026-09-13.md' in NAMING and 'exodus_block_festivals_2026-09-04.md' in NAMING and 'gen_01_creation_boot_2026-07-30.md' in NAMING and 'deu_04_vaetchanan_2026-09-16.md' not in NAMING, NAMING
assert re.search(r'^- Sifrei Devarim 20:1 — MATERIAL', LED['deu_01_03_devarim_2026-09-15.md'], re.M)
assert 'exodus_block_decalogue_2026-09-04.md' in LED and LED['exodus_block_decalogue_2026-09-04.md'].startswith('# THE DECALOGUE — Exodus exam block 5 of 18 (round 29, 2026-09-04)') and len([f for f, t in LED.items() if re.search(r'Exod(?:us)? 20:\d+', t)]) == 20   # the first copy read EXAM-FIRST (2026-09-04), never spine-by-position
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5, 6)}
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30, 6: 25} and sum(len(c) for c in onk_he) == 956
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
assert VC[5] == 33 and VC[4] == 49 and VC[6] == 25 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]
# THE ALIGNMENT RECOMPUTED (ch5_dump0's A0): a monotone alignment of the export's thirty rows to the DB's thirty-three verses over token and negation counts
rows0 = db.execute("SELECT v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=5 ORDER BY v.id, w.idx").fetchall()
by5 = {}
for v, h in rows0: by5.setdefault(v, []).append(plain(h))
NEG = ('לא', 'ולא')
D_ = [(len(by5[v]), sum(1 for x in by5[v] if x in NEG)) for v in range(1, 34)]
E_ = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[4]]
def _cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
best = {(0, 0): (0, None)}
for i in range(1, 31):
    for j in range(i, 34):
        cands = [(best[(i - 1, k)][0] + _cost(E_[i - 1], D_[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best]
        if cands: best[(i, j)] = min(cands)
i, j, ALIGN = 30, 33, {}
while i > 0:
    k = best[(i, j)][1]; ALIGN[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
assert ALIGN == EXP2DB and best[(30, 33)][0] == 27 and E_[16] == (12, 4) and [D_[d - 1] for d in (17, 18, 19, 20)] == [(2, 1), (2, 1), (2, 1), (5, 1)] and Counter(ds[0] - e for e, ds in EXP2DB.items()) == Counter({0: 17, 3: 13}), best[(30, 33)]
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
assert unit_text('deu_05_decalogue').count('    comment: >\n') == 70 and unit_text('deu_05_decalogue').count('\n  - id: S') == 40   # two per step (33) and the four of the derivation log
assert 'deu_04_refuge_east' in unit_text('deu_05_decalogue') and 'exo_20_decalogue_altar' in unit_text('deu_05_decalogue') and steps('deu_06_shema')[0] == (6, 1)
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_')) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md', 'deu_04_vaetchanan_2026-09-16.md', 'deu_04_vaetchanan_exam_2026-09-16.md'] + ([os.path.basename(OUT)] if not FIRST else [])
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json') and f[:-12] not in UIDS)
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(5, v) for v in range(1, VC[5] + 1)]
NV = 33
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
def W5(v): return words('Deut', 5, v)
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 5 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=5 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
# THE WRITTEN-AND-READ PAIR at 5:10: the DB's one token מצותו ("his commandments", the written, wtype x-ketiv); the store carries the written AND the read
# (מצותי "my commandments" — Exodus 20:6's own word): the chapter's one pair; the DB's 1,268 ketiv tokens over the Bible
assert STORE_MISMATCH == [(5, 10, 7, 6)] and all([hp for _, hp, _ in SG[(5, v)]] == W5(v) for v in range(1, 34) if v != 10) and [(hp, g) for _, hp, g in SG[(5, 10)]][-2:] == [('מצותו', 'commandment-him/its'), ('מצותי', 'commandment-me/my')]
assert byw[('Deut', 5, 10)] == [None] * 5 + ['x-ketiv'] and W5(10)[-1] == 'מצותו' and words('Exod', 20, 6)[-1] == 'מצותי' and Counter(wt for v in range(1, 34) for wt in byw[('Deut', 5, v)]) == Counter({None: 471, 'x-ketiv': 1}) and sum(1 for ws in byw.values() for wt in ws if wt == 'x-ketiv') == 1268
TOK = sum(len(by[('Deut', 5, v)]) for v in range(1, 34))
assert TOK == 472, TOK

# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: THREE number verses, NO GAP — 5:13 "six days" [6], 5:14 "the seventh
# day" the ordinal [7], 5:22 "two tablets of stone" [2] (the construct "two" marked ^); 5:9's "the third generation" STARRED — not thirty (rule 15:
# no holam under the lamed; the pointed form שִׁלֵּשִׁים "third-generation ones" at all five seats); 5:10's "to thousands" a bare plural noun (no
# number — the 1b multiplication rule); the same phrases read the same at their other seats (six days [6] at twelve Torah seats; the seventh [7];
# 7:9's "to a thousand generations" [1000]; 9:10 and Exodus 31:18 [2]; 10:4 [10] with the ordinal "the first" [1]; 4:13 [10, 2]).
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {(c, v): N('Deut', c, v) for (c, v) in SPAN if N('Deut', c, v)}
assert PARSED == {(5, 13): [6], (5, 22): [2]} and {(c, v): O('Deut', c, v) for (c, v) in SPAN if O('Deut', c, v)} == {(5, 14): [7]}, PARSED
assert [((c, v), t) for (c, v) in SPAN for t in CS.verse_words('Deut', c, v) if t[-1] in '#~^%@|*'] == [((5, 9), 'שלשים*'), ((5, 22), 'שני^')]
assert N('Exod', 20, 5) == [] and N('Exod', 20, 9) == [6] and O('Exod', 20, 10) == [7] and N('Exod', 20, 11) == [6] and O('Exod', 20, 11) == [7] and N('Deut', 7, 9) == [1000] and N('Deut', 9, 10) == [2] and N('Deut', 10, 4) == [10] and O('Deut', 10, 4) == [1] and N('Exod', 31, 18) == [2] and N('Deut', 4, 13) == [10, 2]
assert len(P('ששת', 'ימים', books=T)) == 12 and all(N(*[s.split()[0], *map(int, s.split()[1].split(':'))]) == [6] for s in P('ששת', 'ימים', books=T))
assert LEMV('8029') == S_('Deut 5:9', 'Exod 20:5', 'Exod 34:7', 'Gen 50:23', 'Num 14:18') and all(PT(*[s.split()[0], *map(int, s.split()[1].split(':'))], 'שלשים') == ['שִׁלֵּשִׁים'] for s in LEMV('8029')) and lemma_of('Deut', 5, 10, 'לאלפים') == ['505'] and morphs('Deut', 5, 10)[2] == 'HR/Acbpa'

# THE FRAMES AND THE REGISTER: ONE divine frame — "and the LORD said to me" at 5:28 (the book's eleven seats of the form); ONE "saying" — 5:5's,
# opening the ten words (the chapter's only seat); the narrative verbs at 5:1 (Moses called, said), 5:15 (he brought you out), 5:22 (he wrote,
# he gave), 5:23-24 (you came near, you said), 5:26 (lived), 5:28 (the LORD heard, said); THE TEN WORDS IN THE SINGULAR — the singular only at 6-9,
# 11-21 (and 27, 31), the plural only at 4, 5, 22-24, 32, 33, both at 1, 28, 30, neither at 2, 3, 10, 25, 26, 29; THE IMPERATIVES "hear" (5:1),
# "go near" (5:27), "go", "say", "return" (5:30), "stand" (5:31); THE TWO INFINITIVE ABSOLUTES "keep" (5:12) and "honor" (5:16) — the form Exodus
# gives "remember" (20:8); TWELVE PROHIBITIONS (the negated second-person imperfect) at 8, 9 (two), 11, 14, 17, 18, 19, 20, 21 (two), 32; THE
# CASE TOKENS: "for" at eight seats (reasons), ONE "if" — 5:25's "if we continue to hear" (the people's, not a law's) — no "lest", no "or";
# "the LORD your God" singular eight tokens (6, 9, 11, 12, 15 twice, 16 twice), plural 32 and 33; "the LORD our God" 2, 24, 25, 27 twice; the Name
# twenty-four tokens; Moses named at 5:1 alone; THE REGISTER GATE: Deut 5:12, 5:16, 5:32 NONE declared ("the book not read" — the two receipts
# inside the ten words "as the LORD your God commanded you" and the closing "as the LORD your God commanded you" (plural), paid at the compile).
DIV = [(c, v) for (c, v) in SPAN if any(W5(v)[i] in ('ויאמר', 'וידבר') and W5(v)[i + 1] == 'יהוה' for i in range(len(W5(v)) - 1))]
assert DIV == [(5, 28)] and len(P('ויאמר', 'יהוה', 'אלי', books=('Deut',))) == 11 and [(c, v) for (c, v) in SPAN if 'לאמר' in W5(v)] == [(5, 5)]
REG = {v: [x for x, m in by[('Deut', 5, v)] if m and re.search(r'V.w', m)] for v in range(1, 34) if any(m and re.search(r'V.w', m) for x, m in by[('Deut', 5, v)])}
assert REG == {1: ['ויקרא', 'ויאמר'], 15: ['ויצאך'], 22: ['ויכתבם', 'ויתנם'], 23: ['ויהי', 'ותקרבון'], 24: ['ותאמרו'], 26: ['ויחי'], 28: ['וישמע', 'ויאמר']}, REG
CASE = {f'{c}:{v}': [x for x in W5(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן')] for (c, v) in SPAN if any(x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן') for x in W5(v))}
assert CASE == {'5:3': ['כי'], '5:5': ['כי'], '5:9': ['כי'], '5:11': ['כי'], '5:15': ['כי'], '5:24': ['כי'], '5:25': ['כי', 'אם'], '5:26': ['כי']} and Counter(x for l in CASE.values() for x in l) == Counter({'כי': 8, 'אם': 1}), CASE
NUM2 = {v: (sum(1 for _, m in by[('Deut', 5, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 5, v)] if m and '2ms' in m)) for v in range(1, 34)}
SG_ONLY = [v for v, (p, s) in NUM2.items() if s and not p]; PL_ONLY = [v for v, (p, s) in NUM2.items() if p and not s]; BOTH = [v for v, (p, s) in NUM2.items() if p and s]; NEITHER = [v for v, (p, s) in NUM2.items() if not p and not s]
assert SG_ONLY == [6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 27, 31] and PL_ONLY == [4, 5, 22, 23, 24, 32, 33] and BOTH == [1, 28, 30] and NEITHER == [2, 3, 10, 25, 26, 29], (SG_ONLY, PL_ONLY, BOTH, NEITHER)
assert NUM2[14] == (0, 15) and NUM2[1] == (3, 1) and NUM2[33] == (7, 0) and NUM2[30] == (3, 2)
IMPER = {v: [(x, m) for x, m in by[('Deut', 5, v)] if m and re.match(r'^HV.v', m)] for v in range(1, 34) if any(m and re.match(r'^HV.v', m) for _, m in by[('Deut', 5, v)])}
assert IMPER == {1: [('שמע', 'HVqv2ms')], 27: [('קרב', 'HVqv2ms')], 30: [('לך', 'HVqv2ms'), ('אמר', 'HVqv2ms'), ('שובו', 'HVqv2mp')], 31: [('עמד', 'HVqv2ms')]}, IMPER
INFA = {v: [(x, m) for x, m in by[('Deut', 5, v)] if m and re.match(r'^HV.a', m)] for v in range(1, 34) if any(m and re.match(r'^HV.a', m) for _, m in by[('Deut', 5, v)])}
assert INFA == {12: [('שמור', 'HVqa')], 16: [('כבד', 'HVpa')]} and wm('Exod', 20, 8)[0] == ('זכור', 'HVqa') and wm('Exod', 20, 12)[0] == ('כבד', 'HVpa'), INFA
assert [(s, m) for s, x, m in LEMT('8104') if x == 'שמור' and s.startswith('Deut')] == [('Deut 5:12', 'HVqa'), ('Deut 6:17', 'HVqa'), ('Deut 16:1', 'HVqa')] and [(s, m) for s, x, m in LEMT('2142') if x == 'זכור' and m == 'HVqa'] == [('Deut 24:9', 'HVqa'), ('Deut 25:17', 'HVqa'), ('Exod 13:3', 'HVqa'), ('Exod 20:8', 'HVqa'), ('Josh 1:13', 'HVqa'), ('Lam 3:20', 'HVqa')]
PROHIB = {v: [x for i, (x, m) in enumerate(by[('Deut', 5, v)]) if i and by[('Deut', 5, v)][i - 1][0] in ('לא', 'ולא') and m and m.startswith('HV') and 'i2' in m] for v in range(1, 34)}
PROHIB = {v: l for v, l in PROHIB.items() if l}
assert PROHIB == {8: ['תעשה'], 9: ['תשתחוה', 'תעבדם'], 11: ['תשא'], 14: ['תעשה'], 17: ['תרצח'], 18: ['תנאף'], 19: ['תגנב'], 20: ['תענה'], 21: ['תחמד', 'תתאוה'], 32: ['תסרו']} and sum(len(l) for l in PROHIB.values()) == 12, PROHIB
YG_SG = [v for v in range(1, 34) for i in range(len(W5(v)) - 1) if W5(v)[i:i + 2] == ['יהוה', 'אלהיך']]; YG_PL = [v for v in range(1, 34) for i in range(len(W5(v)) - 1) if W5(v)[i:i + 2] == ['יהוה', 'אלהיכם']]
assert YG_SG == [6, 9, 11, 12, 15, 15, 16, 16] and YG_PL == [32, 33] and [v for v in range(1, 34) for i in range(len(W5(v)) - 1) if W5(v)[i:i + 2] == ['יהוה', 'אלהינו']] == [2, 24, 25, 27, 27]
NAME = Counter(x for v in range(1, 34) for x in W5(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
assert NAME == Counter({'יהוה': 23, 'ליהוה': 1}) and sum(NAME.values()) == 24 and [v for v in range(1, 34) if 'משה' in W5(v)] == [1]
assert {v: [x for x in W5(v) if x in ('אלהים', 'האלהים')] for v in range(1, 34) if any(x in ('אלהים', 'האלהים') for x in W5(v))} == {7: ['אלהים'], 24: ['אלהים'], 26: ['אלהים']}
assert [(x, m) for x, m in by[('Deut', 5, 28)] if m and '1cs' in m] == [('אלי', 'HR/Sp1cs'), ('אלי', 'HR/Sp1cs'), ('שמעתי', 'HVqp1cs')] and [(x, m) for x, m in by[('Deut', 5, 31)] if m and '1cs' in m] == [('עמדי', 'HR/Sp1cs'), ('ואדברה', 'HC/Vph1cs'), ('אנכי', 'HPp1cs')]
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read(); RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
assert sorted(re.findall(r'^\s*Deut (5:\d+)\s+(\w+)\s+(\w+)', RI, re.M)) == [('5:12', 'NONE', 'declared'), ('5:16', 'NONE', 'declared'), ('5:32', 'NONE', 'declared')]
assert all(re.search(rf'^  Deut 5:{v}:\n    class: NONE\n    why: Deuteronomy is not on the tape \(the book not read\)', RD, re.M) for v in (12, 16, 32))

# 5:1-5 THE FRAME (computed): "and Moses called to all Israel" 5:1 and 29:1 (the two convocations of the book); "hear, O Israel" four seats, all
# this book's; "in your ears" 5:1 the Torah's one seat; "and you shall learn them" 5:1 and 11:19; "and keep to do them" one; "the LORD our God"
# twenty Deuteronomy seats, five this chapter's; "MADE A COVENANT WITH US" one; "NOT WITH OUR FATHERS" one — "our fathers" six Torah seats; "this
# covenant" 5:3, 29:8, 29:13 in the Torah; "all of us alive" one; "FACE TO FACE" (פנים בפנים, "face in face") THE BIBLE'S ONE SEAT of the form —
# the other form (פנים אל פנים, "face to face") five (Jacob's, Moses' at the tent 33:11, 34:10, Gideon's, Ezekiel's); "the LORD spoke with you"
# 5:4 and 9:10; "in the mountain from the midst of the fire" four seats (5:4, 5:22, 9:10, 10:4); "from the midst of the fire" eleven — four this
# chapter's; "I STOOD BETWEEN" one ("stood between" three: Zechariah's and the Chronicler's angel); "at that time" fifteen; "to tell you" one; "for
# you were afraid" one; "from before the fire" 5:5 and Micah 1:4; "you did not go up the mountain" one; "saying" 5:5 the chapter's one seat.
assert P('ויקרא', 'משה', 'אל', 'כל', 'ישראל') == S_('Deut 29:1', 'Deut 5:1') and len(P('ויקרא', 'משה')) == 7 and P('שמע', 'ישראל') == S_('Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1') and wm('Deut', 5, 1)[7] == ('שמע', 'HVqv2ms')
assert P('אשר', 'אנכי', 'דבר', 'באזניכם', 'היום') == ['Deut 5:1'] and U('באזניכם') == S_('Deut 5:1', 'Jer 26:11', 'Jer 26:15', 'Job 13:17') and P('ולמדתם', 'אתם') == S_('Deut 11:19', 'Deut 5:1') and P('ושמרתם', 'לעשתם') == ['Deut 5:1'] and sorted(set(P('ושמרתם', 'לעשות')) | set(P('ושמרת', 'לעשות'))) == S_('Deut 11:32', 'Deut 17:10', 'Deut 5:32', 'Deut 6:3')
assert len(P('יהוה', 'אלהינו', books=('Deut',))) == 20 and P('כרת', 'עמנו', 'ברית') == ['Deut 5:2'] and P('לא', 'את', 'אבתינו') == ['Deut 5:3'] and U('אבתינו', books=T) == S_('Deut 26:7', 'Deut 5:3', 'Gen 46:34', 'Num 20:15', 'Num 36:3', 'Num 36:4')
assert P('הברית', 'הזאת', books=T) == S_('Deut 29:13', 'Deut 29:8', 'Deut 5:3') and P('כי', 'אתנו') == ['Deut 5:3'] and P('פה', 'היום') == S_('Deut 12:8', 'Deut 5:3') and P('כלנו', 'חיים') == ['Deut 5:3'] and lemma_of('Deut', 5, 2, 'בחרב') == ['2722'] and morphs('Deut', 5, 2)[5] == 'HR/Np'
assert P('פנים', 'בפנים') == ['Deut 5:4'] and P('פנים', 'אל', 'פנים') == S_('Deut 34:10', 'Exod 33:11', 'Ezek 20:35', 'Gen 32:31', 'Judg 6:22') and P('דבר', 'יהוה', 'עמכם') == S_('Deut 5:4', 'Deut 9:10') and P('בהר', 'מתוך', 'האש') == S_('Deut 10:4', 'Deut 5:22', 'Deut 5:4', 'Deut 9:10') and len(P('מתוך', 'האש')) == 11
assert P('אנכי', 'עמד', 'בין') == ['Deut 5:5'] and P('עמד', 'בין') == S_('1Chr 21:16', 'Deut 5:5', 'Zech 1:8') and len(P('בעת', 'ההוא', books=('Deut',))) == 15 and P('להגיד', 'לכם') == ['Deut 5:5'] and P('כי', 'יראתם') == ['Deut 5:5'] and P('מפני', 'האש') == S_('Deut 5:5', 'Mic 1:4') and P('ולא', 'עליתם', 'בהר') == ['Deut 5:5']

# 5:6-21 THE TEN WORDS, THE SECOND COPY (computed): 5:6 = Exodus 20:2 VERBATIM (nine words); 5:7 = 20:3 verbatim; 5:8 "any form" for "AND any form"
# (one letter); 5:9 "fathers" plene for defective, "AND upon the third" for "upon the third"; 5:10 "HIS commandments" written where Exodus writes "MY"
# (the ketiv, the read form "my"); 5:11 = 20:7 verbatim; 5:12 "KEEP" for "REMEMBER" and the receipt "AS THE LORD YOUR GOD COMMANDED YOU" added (nine
# words for five); 5:13 = 20:9 verbatim; 5:14 "AND your servant", "YOUR OX AND YOUR ASS AND ALL your cattle", "THAT YOUR SERVANT AND MAIDSERVANT MAY
# REST LIKE YOU" added (twenty-six for eighteen); 5:15 THE GROUND CHANGED WHOLE — the slave in Egypt and the exodus for the six days of creation
# (twenty-three for twenty-six; "for" the one kept word); 5:16 the receipt and "AND THAT IT MAY GO WELL WITH YOU" added, "be long" a longer form
# (twenty-two for fifteen); 5:17 = 20:13; 5:18-20 "AND not" for "not"; 5:20 "a VAIN witness" for "a FALSE witness"; 5:21 THE WIFE FIRST, "DESIRE" for
# the second "covet", "HIS FIELD" added, "AND his ox" (sixteen for fifteen). The copies 172 tokens / 620 letters against 189 / 708. "I am the LORD
# your God" 5:6, 5:9, Exodus 20:2, 20:5, Psalm 81:11; "house of bondage" twelve seats; "other gods" nineteen Torah seats, seventeen this book's;
# "a graven image" nine Torah; "in heaven above" five; "in the waters under the earth" three (4:18 the third); "bow down nor serve" two; "a jealous
# God" five; "VISITING THE INIQUITY OF FATHERS UPON SONS" 5:9, Exodus 34:7, Numbers 14:18 — NOT Exodus 20:5 (its "fathers" defective breaks the
# phrase); "the third … the fourth" the lemma's five seats (Joseph's great-grandsons Genesis 50:23 the first); "to thousands" four; "keep his
# commandments" five (the ketiv's form); "in vain" nine; "will not hold guiltless" twelve; "KEEP the sabbath day" one, "REMEMBER the sabbath day"
# one — "keep" the infinitive absolute three Deuteronomy seats, "remember" six; "to sanctify it" six; "AS THE LORD YOUR GOD COMMANDED YOU" 5:12,
# 5:16, 20:17 — THE RECEIPT INSIDE THE TEN WORDS (the register's seats), its plural 5:32 one; "six days you shall labor" three; "your ox and your
# ass and all your cattle" one; "your stranger within your gates" three; "that your servant may rest" one; "like you" seven Torah; "REMEMBER THAT
# YOU WERE A SLAVE" five, all this book's (15:15, 16:12, 24:18, 24:22); "brought you out" the wayyiqtol with the suffix one; "a mighty hand and an
# outstretched arm" 5:15 and 26:8 in this spelling; "therefore the LORD your God commanded you" one; "to do the sabbath day" one; "honor your father
# and your mother" two — 5:16's "honor" the infinitive absolute (piel) as at Exodus 20:12; "that your days may be long" one each spelling; "and that
# it may go well with you" one; "on the ground which the LORD your God gives you" four; "a vain witness" one, "a false witness" five; "vain" four
# Torah seats (5:11, 5:20, Exodus 20:7, 23:1); "covet" 2ms four; "desire" the hitpael one — the root's twenty-five seats (Numbers 11:4, 34 the
# craving); "his field" six; "his ox and his ass" one; "your neighbor" four tokens.
assert DIFF(('Deut', 5, 6), ('Exod', 20, 2)) == [] and DIFF(('Deut', 5, 7), ('Exod', 20, 3)) == [] and DIFF(('Deut', 5, 11), ('Exod', 20, 7)) == [] and DIFF(('Deut', 5, 13), ('Exod', 20, 9)) == [] and DIFF(('Deut', 5, 17), ('Exod', 20, 13)) == []
assert DIFF(('Deut', 5, 8), ('Exod', 20, 4)) == [('replace', ['כל'], ['וכל'])] and DIFF(('Deut', 5, 9), ('Exod', 20, 5)) == [('replace', ['אבות'], ['אבת']), ('replace', ['ועל'], ['על'])] and DIFF(('Deut', 5, 10), ('Exod', 20, 6)) == [('replace', ['מצותו'], ['מצותי'])]
assert DIFF(('Deut', 5, 12), ('Exod', 20, 8)) == [('replace', ['שמור'], ['זכור']), ('delete', ['כאשר', 'צוך', 'יהוה', 'אלהיך'], [])] and DIFF(('Deut', 5, 14), ('Exod', 20, 10)) == [('replace', ['ועבדך'], ['עבדך']), ('replace', ['ושורך', 'וחמרך', 'וכל', 'בהמתך'], ['ובהמתך']), ('delete', ['למען', 'ינוח', 'עבדך', 'ואמתך', 'כמוך'], [])]
assert SHARED(('Deut', 5, 15), ('Exod', 20, 11)) == ['את', 'יום', 'השבת'] and [op for op, _, _ in DIFF(('Deut', 5, 15), ('Exod', 20, 11))] == ['delete', 'replace', 'replace', 'replace', 'delete', 'insert'] and DIFF(('Deut', 5, 16), ('Exod', 20, 12)) == [('delete', ['כאשר', 'צוך', 'יהוה', 'אלהיך'], []), ('replace', ['יאריכן'], ['יארכון']), ('delete', ['ולמען', 'ייטב', 'לך'], [])]
assert all(DIFF(('Deut', 5, v), ('Exod', 20, v - 4)) == [('replace', ['ולא'], ['לא'])] for v in (18, 19)) and DIFF(('Deut', 5, 20), ('Exod', 20, 16)) == [('replace', ['ולא'], ['לא']), ('replace', ['שוא'], ['שקר'])]
assert DIFF(('Deut', 5, 21), ('Exod', 20, 17)) == [('replace', ['ולא'], ['לא', 'תחמד', 'בית', 'רעך', 'לא']), ('delete', ['ולא', 'תתאוה', 'בית', 'רעך', 'שדהו'], []), ('replace', ['שורו'], ['ושורו'])]
def letters(b, c, lo, hi): return sum(len(x) for v in range(lo, hi + 1) for x in words(b, c, v))
assert (sum(len(words('Exod', 20, v)) for v in range(2, 18)), letters('Exod', 20, 2, 17)) == (172, 620) and (sum(len(W5(v)) for v in range(6, 22)), letters('Deut', 5, 6, 21)) == (189, 708)
assert P('אנכי', 'יהוה', 'אלהיך') == S_('Deut 5:6', 'Deut 5:9', 'Exod 20:2', 'Exod 20:5', 'Ps 81:11') and len(sorted(set(P('מבית', 'עבדים')) | set(P('בית', 'עבדים')))) == 12 and (len(P('אלהים', 'אחרים', books=T)), len(P('אלהים', 'אחרים', books=('Deut',)))) == (19, 17) and P('אלהים', 'אחרים', 'על', 'פני') == S_('Deut 5:7', 'Exod 20:3')
assert len(U('פסל', 'ופסל', books=T)) == 9 and P('פסל', 'וכל', 'תמונה') == ['Exod 20:4'] and P('פסל', 'כל', 'תמונה') == ['Deut 5:8'] and len(P('בשמים', 'ממעל')) == 5 and P('במים', 'מתחת', 'לארץ') == S_('Deut 4:18', 'Deut 5:8', 'Exod 20:4') and P('לא', 'תשתחוה', 'להם', 'ולא', 'תעבדם') == S_('Deut 5:9', 'Exod 20:5')
assert P('אל', 'קנא') == S_('Deut 4:24', 'Deut 5:9', 'Deut 6:15', 'Exod 20:5', 'Exod 34:14') and P('פקד', 'עון', 'אבות', 'על', 'בנים') == S_('Deut 5:9', 'Exod 34:7', 'Num 14:18') and P('על', 'שלשים', 'ועל', 'רבעים') == S_('Exod 20:5', 'Exod 34:7', 'Num 14:18') and U('לשנאי') == S_('Deut 5:9', 'Exod 20:5')
assert U('לאלפים') == S_('Deut 5:10', 'Exod 20:6', 'Exod 34:7', 'Jer 32:18') and P('לאהבי', 'ולשמרי', 'מצותי') == ['Exod 20:6'] and P('לאהבי', 'ולשמרי', 'מצותו') == ['Deut 5:10'] and U('מצותו') == S_('Deut 27:10', 'Deut 5:10', 'Deut 7:9', 'Deut 8:2', 'Num 15:31')
assert len(U('לשוא')) == 9 and len(P('לא', 'ינקה')) == 12 and P('שמור', 'את', 'יום', 'השבת') == ['Deut 5:12'] and P('זכור', 'את', 'יום', 'השבת') == ['Exod 20:8'] and len(U('לקדשו')) == 6
assert P('כאשר', 'צוך', 'יהוה', 'אלהיך') == S_('Deut 20:17', 'Deut 5:12', 'Deut 5:16') and P('כאשר', 'צוך') == S_('Deut 20:17', 'Deut 5:12', 'Deut 5:16') and P('כאשר', 'צוה', 'יהוה', 'אלהיכם', 'אתכם') == ['Deut 5:32']
assert P('ששת', 'ימים', 'תעבד') == S_('Deut 5:13', 'Exod 20:9', 'Exod 34:21') and P('ושורך', 'וחמרך', 'וכל', 'בהמתך') == ['Deut 5:14'] and P('וגרך', 'אשר', 'בשעריך') == S_('Deut 31:12', 'Deut 5:14', 'Exod 20:10') and P('למען', 'ינוח', 'עבדך', 'ואמתך') == ['Deut 5:14'] and len(U('ינוח')) == 8 and len(U('כמוך', books=T)) == 7
assert P('וזכרת', 'כי', 'עבד', 'היית') == S_('Deut 15:15', 'Deut 16:12', 'Deut 24:18', 'Deut 24:22', 'Deut 5:15') and U('ויצאך') == ['Deut 5:15'] and P('ביד', 'חזקה', 'ובזרע', 'נטויה') == S_('Deut 26:8', 'Deut 5:15') and P('על', 'כן', 'צוך', 'יהוה', 'אלהיך') == ['Deut 5:15'] and P('לעשות', 'את', 'יום', 'השבת') == ['Deut 5:15'] and P('כי', 'ששת', 'ימים', 'עשה', 'יהוה') == S_('Exod 20:11', 'Exod 31:17')
assert P('כבד', 'את', 'אביך', 'ואת', 'אמך') == S_('Deut 5:16', 'Exod 20:12') and P('למען', 'יאריכן', 'ימיך') == ['Deut 5:16'] and P('למען', 'יארכון', 'ימיך') == ['Exod 20:12'] and P('ולמען', 'ייטב', 'לך') == ['Deut 5:16'] and P('על', 'האדמה', 'אשר', 'יהוה', 'אלהיך', 'נתן', 'לך') == S_('Deut 25:15', 'Deut 4:40', 'Deut 5:16', 'Exod 20:12')
assert P('לא', 'תרצח') == S_('Deut 5:17', 'Exod 20:13') and U('תנאף') == S_('Deut 5:18', 'Exod 20:14') and U('תגנב') == S_('Deut 5:19', 'Exod 20:15') and P('לא', 'תגנבו') == ['Lev 19:11'] and P('עד', 'שוא') == ['Deut 5:20'] and P('עד', 'שקר') == S_('Deut 19:18', 'Exod 20:16', 'Prov 14:5', 'Prov 25:18', 'Prov 6:19') and U('שוא', 'לשוא', books=T) == S_('Deut 5:11', 'Deut 5:20', 'Exod 20:7', 'Exod 23:1')
assert U('תחמד') == S_('Deut 5:21', 'Deut 7:25', 'Exod 20:17', 'Prov 6:25') and P('ולא', 'תחמד') == ['Deut 5:21'] and P('אשת', 'רעך') == S_('Deut 5:21', 'Exod 20:17') and U('תתאוה') == ['Deut 5:21'] and len(LEMV('183')) == 25 and 'Num 11:4' in LEMV('183') and P('בית', 'רעך') == S_('Deut 5:21', 'Exod 20:17')
assert len(U('שדהו')) == 6 and P('שורו', 'וחמרו') == ['Deut 5:21'] and P('וכל', 'אשר', 'לרעך') == S_('Deut 5:21', 'Exod 20:17') and sum(W5(v).count(t) for v in range(1, 34) for t in ('רעך', 'ברעך', 'לרעך')) == 4

# 5:22-27 THE VOICE AND THE REQUEST (computed): "these words the LORD spoke" one; "to all your assembly" one — "your assembly" the Bible's one seat;
# "the fire, the cloud and the thick darkness" one; "a great voice" nine; "AND HE ADDED NO MORE" 5:22, Genesis 38:26 (Judah), Judges 13:21, 1 Samuel
# 15:35 — the qal perfect at four of the lemma's thirteen seats; "two tablets of stone" six seats, defective here (4:13 plene); "and gave them to me"
# one; "when you heard the voice" one; "from the midst of the darkness" one; "the mountain burning with fire" 4:11, 5:23, 9:15; "AND YOU CAME NEAR TO
# ME" 5:23 and 1:22 — the Sifrei 20:1's pair (the elders here, the mob there); "the heads of your tribes" 1:15 and 5:23; "and your elders" one; "and
# you said" five Deuteronomy seats (1:14, 22, 27, 41, 5:24); "has shown us" one; "his glory and his greatness" one; "his voice we heard from the midst
# of the fire" one; "that God speaks with man and he lives" one; "why should we die" 5:25 and Genesis 47:19; "this great fire" 5:25 and 18:16; "if we
# continue" one — the participle's one seat; "and we shall die" three; "who of all flesh" one — "all flesh" nine Torah seats (the flood's seven);
# "THE LIVING GOD" 5:26, 1 Samuel 17:26, 36, Jeremiah 10:10, 23:36; "speaking from the midst of the fire" 4:33 and 5:26; "go near and hear" one —
# "go near" the imperative four seats (Aaron's Leviticus 9:7); "and you speak to us" one; "WE WILL HEAR AND DO" one — Exodus 24:7's "WE WILL DO AND
# HEAR" reversed; "all that the LORD has spoken we will do" Exodus 19:8, 24:3, 24:7.
assert P('את', 'הדברים', 'האלה', 'דבר', 'יהוה') == ['Deut 5:22'] and P('אל', 'כל', 'קהלכם') == ['Deut 5:22'] and U('קהלכם') == ['Deut 5:22'] and P('האש', 'הענן', 'והערפל') == ['Deut 5:22'] and len(P('קול', 'גדול')) == 9
assert P('ולא', 'יסף') == S_('1Sam 15:35', 'Deut 5:22', 'Gen 38:26', 'Judg 13:21') and [(s, m) for s, x, m in LEMT('3254') if x == 'יסף' and m == 'HVqp3ms'] == [('1Sam 15:35', 'HVqp3ms'), ('Deut 5:22', 'HVqp3ms'), ('Gen 38:26', 'HVqp3ms'), ('Jer 45:3', 'HVqp3ms'), ('Judg 13:21', 'HVqp3ms')] and len(LEMV('3254')) >= 13
assert sorted(set(P('שני', 'לחת', 'אבנים')) | set(P('שני', 'לחת', 'האבנים')) | set(P('שני', 'לחות', 'אבנים'))) == S_('Deut 10:3', 'Deut 4:13', 'Deut 5:22', 'Deut 9:11', 'Exod 34:1', 'Exod 34:4') and P('ויתנם', 'אלי') == ['Deut 5:22'] and SHARED(('Deut', 5, 22), ('Deut', 4, 13)) == ['ויכתבם', 'על', 'שני'] and PT('Deut', 5, 22, 'לחת') == ['לֻחֹת']
assert P('כשמעכם', 'את', 'הקול') == ['Deut 5:23'] and P('מתוך', 'החשך') == ['Deut 5:23'] and P('וההר', 'בער', 'באש') == S_('Deut 4:11', 'Deut 5:23', 'Deut 9:15') and P('ותקרבון', 'אלי') == S_('Deut 1:22', 'Deut 5:23') and U('ותקרבון') == S_('Deut 1:22', 'Deut 4:11', 'Deut 5:23') and SHARED(('Deut', 5, 23), ('Deut', 1, 22)) == ['ותקרבון', 'אלי']
assert P('ראשי', 'שבטיכם') == S_('Deut 1:15', 'Deut 5:23') and U('וזקניכם') == ['Deut 5:23'] and U('ותאמרו', books=('Deut',)) == S_('Deut 1:14', 'Deut 1:22', 'Deut 1:27', 'Deut 1:41', 'Deut 5:24') and P('הן', 'הראנו', 'יהוה', 'אלהינו') == ['Deut 5:24'] and P('את', 'כבדו', 'ואת', 'גדלו') == ['Deut 5:24'] and len(U('גדלו')) == 12
assert P('ואת', 'קלו', 'שמענו', 'מתוך', 'האש') == ['Deut 5:24'] and P('כי', 'ידבר', 'אלהים', 'את', 'האדם', 'וחי') == ['Deut 5:24'] and len(U('וחי')) == 29 and P('למה', 'נמות') == S_('Deut 5:25', 'Gen 47:19') and P('האש', 'הגדלה', 'הזאת') == S_('Deut 18:16', 'Deut 5:25') and U('יספים') == ['Deut 5:25'] and U('ומתנו') == S_('1Kgs 17:12', '2Kgs 7:4', 'Deut 5:25')
assert P('כי', 'מי', 'כל', 'בשר') == ['Deut 5:26'] and len(P('כל', 'בשר', books=T)) == 9 and P('אלהים', 'חיים') == S_('1Sam 17:26', '1Sam 17:36', 'Deut 5:26', 'Jer 10:10', 'Jer 23:36') and P('מדבר', 'מתוך', 'האש') == S_('Deut 4:33', 'Deut 5:26') and P('כמנו', 'ויחי') == ['Deut 5:26'] and SHARED(('Deut', 5, 26), ('Deut', 4, 33)) == ['מדבר', 'מתוך', 'האש']
assert P('קרב', 'אתה', 'ושמע') == ['Deut 5:27'] and [s for s, x, m in LEMT('7126') if x == 'קרב' and m and m.startswith('HVqv')] == S_('2Sam 20:16', 'Deut 5:27', 'Isa 65:5', 'Lev 9:7') and P('ואת', 'תדבר', 'אלינו') == ['Deut 5:27'] and P('ושמענו', 'ועשינו') == ['Deut 5:27'] and P('נעשה', 'ונשמע') == ['Exod 24:7'] and P('אשר', 'דבר', 'יהוה', 'נעשה') == S_('Exod 19:8', 'Exod 24:3', 'Exod 24:7')

# 5:28-33 THE ANSWER AND THE CHARGE (computed): "AND THE LORD HEARD THE VOICE OF YOUR WORDS" 5:28 and 1:34 — the same five words open the wrath at
# Kadesh and the praise at Horeb; "and the LORD said to me" eleven Deuteronomy seats; "I have heard the voice of the words of this people" one;
# "THEY HAVE WELL SAID" 5:28 and 18:17 (the prophet's promise cites this verse's verdict); "who would give" seventeen seats (Job's ten); "to fear
# me" 4:10 and 5:29; "all the days" twelve; "forever" three (the short spelling); "go say to them" one; "return to your tents" one — "to your tents"
# 5:30 and Joshua 22:4; "AND YOU, HERE STAND WITH ME" one (the Sifrei 357:40: Moses spoke only standing); "with me" twenty Torah seats; "and I will
# speak to you" 5:31 and 2 Samuel 20:16; "all the commandment and the statutes and the judgments" one — 6:1 the same three without "all"; "all the
# commandment" eight; "which you shall teach them" one; "which I give them to possess it" one; "you shall observe to do as the LORD your God
# commanded you" one (the plural receipt); "YOU SHALL NOT TURN ASIDE RIGHT OR LEFT" one — "right or left" 5:32 and 17:11 (the judges' verdict);
# "in all the way" six; "that you may live" six; "and it be well with you" one; "and prolong days" one; "which you shall possess" the paragogic one.
assert P('וישמע', 'יהוה', 'את', 'קול', 'דבריכם') == S_('Deut 1:34', 'Deut 5:28') and SHARED(('Deut', 5, 28), ('Deut', 1, 34)) == ['וישמע', 'יהוה', 'את', 'קול', 'דבריכם'] and P('שמעתי', 'את', 'קול', 'דברי', 'העם', 'הזה') == ['Deut 5:28'] and P('היטיבו', 'כל', 'אשר', 'דברו') == ['Deut 5:28'] and U('היטיבו') == S_('Deut 18:17', 'Deut 5:28', 'Hos 10:1', 'Jer 26:13', 'Jer 7:3', 'Ps 33:3')
assert len(P('מי', 'יתן')) == 17 and len([s for s in P('מי', 'יתן') if s.startswith('Job')]) == 9 and P('מי', 'יתן', 'והיה', 'לבבם', 'זה', 'להם') == ['Deut 5:29'] and P('ליראה', 'אתי') == S_('Deut 4:10', 'Deut 5:29') and len(P('כל', 'הימים', books=('Deut',))) == 12 and U('לעלם', books=('Deut',)) == S_('Deut 32:40', 'Deut 5:29') and U('לעולם', books=('Deut',)) == ['Deut 23:7']
assert P('לך', 'אמר', 'להם') == ['Deut 5:30'] and P('שובו', 'לכם', 'לאהליכם') == ['Deut 5:30'] and U('לאהליכם') == S_('Deut 5:30', 'Josh 22:4') and P('ואתה', 'פה', 'עמד', 'עמדי') == ['Deut 5:31'] and len(U('עמדי', books=T)) == 20 and P('ואדברה', 'אליך') == S_('2Sam 20:16', 'Deut 5:31')
assert P('את', 'כל', 'המצוה', 'והחקים', 'והמשפטים') == ['Deut 5:31'] and P('המצוה', 'החקים', 'והמשפטים') == ['Deut 6:1'] and len(P('כל', 'המצוה', books=('Deut',))) == 8 and P('אשר', 'תלמדם') == ['Deut 5:31'] and P('אשר', 'אנכי', 'נתן', 'להם', 'לרשתה') == ['Deut 5:31'] and P('והחקים', 'והמשפטים') == S_('2Chr 33:8', 'Deut 4:45', 'Deut 5:31', 'Deut 6:20')
assert P('ושמרתם', 'לעשות', 'כאשר', 'צוה', 'יהוה', 'אלהיכם', 'אתכם') == ['Deut 5:32'] and P('לא', 'תסרו', 'ימין', 'ושמאל') == ['Deut 5:32'] and P('ימין', 'ושמאל') == S_('Deut 17:11', 'Deut 5:32') and U('תסרו') == ['Deut 5:32'] and SHARED(('Deut', 5, 32), ('Deut', 17, 11)) == ['ימין', 'ושמאל']
assert len(P('בכל', 'הדרך')) == 6 and P('אשר', 'צוה', 'יהוה', 'אלהיכם', 'אתכם', 'תלכו') == ['Deut 5:33'] and len(U('תחיון', 'תחיו')) == 6 and P('וטוב', 'לכם') == ['Deut 5:33'] and P('והארכתם', 'ימים') == ['Deut 5:33'] and U('תירשון') == ['Deut 5:33']

# ONKELOS CHAPTER 5 — THE RENDERINGS' SEATS over the whole book (computed on the plain Aramaic of every export row; the seats in the EXPORT'S
# numbering — chapter 5's 17 is the DB's 17-20 and 19-30 the DB's 22-33): 5:4 "FACE TO FACE" made "SPEECH WITH SPEECH" (one seat); 5:5 "between
# THE MEMRA OF THE LORD and you" (one — the Memra of the LORD twenty-four seats in the book), "the word of the LORD" for "the word"; 5:7 "another god
# EXCEPT ME" (one); 5:9 "visiting the sins of the fathers on REBELLIOUS children … WHEN THE CHILDREN COMPLETE TO SIN AFTER THEIR FATHERS" — the
# translation's supplied condition (one seat of each word), "the third GENERATION", "the fourth GENERATION"; 5:10 "to thousands OF GENERATIONS" (5:10,
# 7:9); 5:11 "swear … in vain … by his name IN A LIE" — the second "in vain" made a lie (one each); 5:12 "keep" and 5:15 "the day of the sabbath"
# (two seats); 5:14 "a sabbath BEFORE the LORD" (one); 5:17 "do not murder A SOUL" (one), "false testimony" (one); 5:21 "AND DO NOT DESIRE" (one);
# 5:22 "a great voice AND DID NOT CEASE" for "and added no more" (the Talmud's reading; one seat), "two tablets of stone" six; 5:24 "the voice of
# HIS MEMRA" (4:36, 5:24); 5:25 and 5:26 "the voice of THE MEMRA OF THE LORD" (4:33, 5:25, 5:26, 18:16); 5:27 "WE WILL ACCEPT AND DO" for "we will
# hear and do" (one); 5:28 "IT WAS HEARD BEFORE THE LORD" for "the LORD heard" (1:34, 5:28), "heard BEFORE ME", "they have done RIGHTLY" (5:28,
# 18:8); 5:29 "WOULD THAT" (5:29, 21:5, 31:9), "to fear BEFORE ME" (4:10, 5:29); 5:31 "stand BEFORE ME" (one); 5:32 "right and left" five seats.
ONK5 = {'ממלל': [(4, 33), (5, 1), (5, 4), (5, 23)], 'לחואה': [(5, 5)], 'דחלתון': [(5, 5)], 'סלקתון': [(5, 5)], 'הויתי': [(5, 5), (10, 10)], 'קאם': [(5, 5), (10, 10), (29, 14)], 'אפקתך': [(5, 6)], 'עבדותא': [(5, 6), (6, 12), (7, 8), (8, 14), (13, 6), (13, 11)], 'אחרן': [(5, 7), (20, 5), (20, 6), (20, 7), (24, 2), (28, 30), (28, 32)], 'מני': [(1, 41), (3, 26), (5, 7), (7, 17), (32, 39)], 'צלם': [(4, 16), (4, 23), (4, 25), (5, 8), (27, 15)], 'דמות': [(4, 15), (4, 16), (4, 17), (4, 18), (4, 23), (4, 25), (5, 8)], 'תסגוד': [(5, 9)], 'תפלחנון': [(5, 9)], 'מסער': [(5, 9)], 'חובי': [(5, 9)], 'אבהן': [(5, 9), (24, 16)], 'מרדין': [(5, 9)], 'דר': [(5, 9), (18, 6), (32, 7)], 'תליתי': [(5, 9)], 'רביעי': [(5, 9)], 'משלמין': [(5, 9)], 'למחטי': [(5, 9)], 'טיבו': [(5, 10)], 'לאלפי': [(5, 10), (7, 9)], 'דרין': [(5, 10), (7, 9)], 'לרחמי': [(5, 10)], 'ולנטרי': [(5, 10), (7, 9)], 'פקודי': [(5, 10), (5, 26)], 'תימי': [(5, 11)], 'למגנא': [(5, 11)], 'יזכי': [(5, 11)], 'ימי': [(5, 11)], 'לשקרא': [(5, 11)], 'טר': [(5, 12), (12, 28), (16, 1), (27, 1)], 'דשבתא': [(5, 12), (5, 15)], 'לקדשותיה': [(5, 12)], 'פקדך': [(4, 23), (5, 12), (5, 15), (5, 16), (6, 17), (13, 6), (20, 17), (28, 45)], 'שביעאה': [(5, 14), (16, 8)], 'שבתא': [(5, 14)], 'עבידא': [(5, 14), (16, 8)], 'בעירך': [(5, 14)], 'וגיורך': [(5, 14), (29, 10), (31, 12)], 'בקרוך': [(5, 14)], 'ינוח': [(5, 14)], 'כותך': [(5, 14), (18, 18)], 'ותדכר': [(5, 15), (8, 2), (8, 18), (15, 15), (16, 12), (24, 18), (24, 22)], 'ואפקך': [(4, 37), (5, 15)], 'ובדרעא': [(4, 34), (5, 15), (26, 8)], 'מרמא': [(4, 34), (5, 15)], 'יקר': [(5, 16)], 'אבוך': [(5, 16), (32, 6), (32, 7)], 'דיורכון': [(5, 16), (6, 2), (25, 15)], 'דיוטב': [(5, 16)], 'תקטול': [(5, 17), (32, 42)], 'תגוף': [(5, 17)], 'תגנוב': [(5, 17)], 'תסהד': [(5, 17)], 'סהדותא': [(4, 45), (5, 17), (6, 20)], 'דשקרא': [(5, 17)], 'תחמד': [(5, 18), (7, 25)], 'תרוג': [(5, 18)], 'חקליה': [(5, 18)], 'קהלכון': [(5, 19)], 'עננא': [(4, 11), (5, 19)], 'ואמיטתא': [(4, 11), (5, 19)], 'פסק': [(5, 19)], 'וכתבנון': [(4, 13), (5, 19)], 'לוחי': [(4, 13), (5, 19), (9, 9), (9, 10), (9, 11), (9, 15), (10, 1), (10, 3)], 'ויהבנון': [(5, 19), (10, 4)], 'חשוכא': [(4, 11), (5, 20)], 'וקרבתון': [(1, 22), (4, 11), (5, 20)], 'רישי': [(1, 15), (5, 20), (33, 5)], 'וסביכון': [(5, 20)], 'אחזינא': [(5, 21)], 'יקריה': [(5, 21), (33, 2)], 'רבותיה': [(5, 21), (11, 2)], 'שמענא': [(5, 21)], 'חזינא': [(1, 28), (5, 21)], 'ויתקים': [(4, 33), (4, 42), (5, 21), (19, 4), (19, 5)], 'תיכלננא': [(5, 22)], 'מוספין': [(5, 22)], 'ומיתין': [(5, 22)], 'כותנא': [(5, 23)], 'ואתקים': [(5, 23)], 'ונקבל': [(5, 24)], 'ונעבד': [(5, 24)], 'ושמיע': [(1, 34), (5, 25)], 'פתגמיכון': [(1, 34), (4, 21), (5, 25)], 'במללותכון': [(5, 25)], 'אתקינו': [(5, 25), (18, 8)], 'לוי': [(5, 26), (21, 5), (31, 9)], 'למדחל': [(4, 10), (5, 26), (6, 24), (10, 12), (14, 23), (17, 19), (28, 58), (31, 13)], 'תובו': [(5, 27)], 'למשכניכון': [(5, 27)], 'ואמלל': [(5, 28), (31, 28), (32, 1)], 'תסטון': [(5, 29), (28, 14)], 'ותורכון': [(5, 30)], 'תירתון': [(5, 30)], 'אבהתנא': [(5, 3)], 'הכא': [(5, 3), (5, 28), (12, 8), (29, 14)], 'ותלפון': [(5, 1), (11, 19)]}
assert all(onk_tok(t) == s for t, s in ONK5.items()), [t for t, s in ONK5.items() if onk_tok(t) != s]
ONK5P = {'ממלל עם ממלל': 1, 'בין מימרא דיי': 1, 'מימרא דיי': 24, 'קל מימרא דיי': 4, 'ית קל מימריה': 2, 'ולא פסק': 1, 'תקטול נפש': 1, 'לאלפי דרין': 2, 'כד משלמין': 1, 'בנין מרדין': 1, 'ונקבל ונעבד': 1, 'ושמיע קדם יי': 2, 'שמיע קדמי': 1, 'לוי די': 1, 'שבתא קדם יי': 1, 'סהדותא דשקרא': 1, 'בר מני': 3, 'אלהא אחרן': 1, 'לא עם אבהתנא': 1, 'אלהן עמנא': 1, 'למדחל קדמי': 2, 'קים קדמי': 1, 'תרין לוחי אבניא': 6, 'קל רב': 2, 'אל קנא': 3, 'בשמיה לשקרא': 1, 'יומא דשבתא': 2, 'כמא די פקדך יי אלהך': 3, 'בידא תקיפא ובדרעא מרמא': 2, 'ימינא ושמאלא': 5, 'אנא יי אלהך': 2, 'מארעא דמצרים מבית עבדותא': 4, 'דר תליתי': 1, 'דר רביעי': 1, 'ולא תרוג': 1, 'אתקינו כל די מלילו': 1}
assert all(len(onk_seats(k)) == n for k, n in ONK5P.items()), [(k, len(onk_seats(k))) for k, n in ONK5P.items() if len(onk_seats(k)) != n]
assert onk_seats('קל מימרא דיי') == [(4, 33), (5, 22), (5, 23), (18, 16)] and onk_seats('ית קל מימריה') == [(4, 36), (5, 21)] and onk_seats('ושמיע קדם יי') == [(1, 34), (5, 25)] and onk_seats('למדחל קדמי') == [(4, 10), (5, 26)] and onk_seats('בר מני') == [(4, 35), (5, 7), (32, 39)]
assert aramaic(5, 4)[:3] == ['ממלל', 'עם', 'ממלל'] and aramaic(5, 17)[:3] == ['לא', 'תקטול', 'נפש'] and aramaic(5, 22)[13:17] == ['קל', 'רב', 'ולא', 'פסק'] and aramaic(5, 27)[-2:] == ['ונקבל', 'ונעבד'] and aramaic(5, 28)[:3] == ['ושמיע', 'קדם', 'יי'] and aramaic(5, 29)[:2] == ['לוי', 'די']
assert len(aramaic(5, 9)) == 30 and len(W5(9)) == 21 and len(aramaic(5, 17)) == 12 and sum(len(W5(v)) for v in (17, 18, 19, 20)) == 11 and aramaic(5, 18) == aramaic(5, 17) and aramaic(5, 21)[:2] == ['ולא', 'תחמד']
BR = {e: re.findall(r'\[([^\]]+)\]', clean(onk[4][e - 1])) for e in range(1, 31)}
BR = {e: b for e, b in BR.items() if b}
assert BR == {3: ['only'], 4: ['speech', 'speech'], 5: ['the word of', 'before'], 7: ['except for Me'], 9: ['rebellious', 'when the children continue to sin after the fashion of their fathers,'], 10: ['of generations'], 11: ['in a lie'], 14: ['midst'], 17: ['a person'], 21: ['of His word'], 22: ['word of His'], 23: ['word of the'], 25: ['Before', 'was', 'Before Me', 'correct'], 28: ['before', 'them']}, BR

# THE STORE'S GLOSSES at the chapter's seats (words.gloss, read back): the families censused over the whole store (ch5_measure1 section G) —
# BY GLOSS where every token of the gloss is the one word, BY REFERENCE where the family is mixed (a homograph, two persons, an absolute beside
# a construct); 5:10's written-and-read pair carries both glosses ("his commandments", "my commandments").
assert sg(5, 1, 'ולמדתם') == 'and-goad' and sg(5, 1, 'החקים') == 'the-enactment' and sg(5, 1, 'המשפטים') == 'the-judgment' and sg(5, 1, 'אנכי') == '?' and sg(5, 1, 'באזניכם') == 'in-broadness.-i.e.--the-ear-you/your (pl)' and sg(5, 1, 'לעשתם') == 'to-make-them/their'
assert sg(5, 2, 'כרת') == 'cut' and sg(5, 3, 'פה') == 'this-place' and sg(5, 3, 'כלנו') == 'all-us/our' and sg(5, 4, 'בפנים') == 'in-face' and sg(5, 5, 'ההוא') == 'the-he/it' and sg(5, 5, 'להגיד') == 'to-tell' and sg(5, 6, 'הוצאתיך') == 'bring-forth-you/your' and sg(5, 6, 'עבדים') == 'servant'
assert sg(5, 7, 'אחרים') == 'hinder' and sg(5, 7, 'פני') == 'face-me/my' and sg(5, 8, 'פסל') == 'idol' and sg(5, 8, 'תמונה') == 'something-portioned--out' and sg(5, 8, 'מתחת') == 'from-under' and sg(5, 9, 'תשתחוה') == 'depress' and sg(5, 9, 'תעבדם') == 'work/serve-them/their' and sg(5, 9, 'אל') == 'strength'
assert sg(5, 9, 'פקד') == 'count/visit' and sg(5, 9, 'עון') == 'perversity' and sg(5, 9, 'שלשים') == 'descendant-of-the-third-degr' and sg(5, 9, 'רבעים') == 'descendant-of-the-fourth-gen' and sg(5, 9, 'לשנאי') == 'to-hate-me/my' and sg(5, 10, 'לאלפים') == 'to-thousand' and sg(5, 10, 'לאהבי') == 'to-have-affection-for-me/my' and sg(5, 10, 'ולשמרי') == 'and-to-keep/guard'
assert sg(5, 11, 'תשא') == 'lift/carry' and sg(5, 11, 'לשוא') == 'to-evil' and sg(5, 11, 'ינקה') == 'be--clean' and sg(5, 12, 'שמור') == 'keep/guard' and sg(5, 12, 'השבת') == 'the-intermission' and sg(5, 12, 'לקדשו') == 'to-sanctify-him/its' and sg(5, 14, 'שבת') == 'intermission' and sg(5, 14, 'ינוח') == 'rest' and sg(5, 14, 'כמוך') == "form-of-the-prefix-'k-'-you/your"
assert sg(5, 15, 'וזכרת') == 'and-mark' and sg(5, 15, 'נטויה') == 'stretch' and sg(5, 15, 'כן') == 'so' and sg(5, 16, 'כבד') == 'be-heavy' and sg(5, 16, 'יאריכן') == 'be--long-suffix' and sg(5, 16, 'ייטב') == 'be--make-well' and sg(5, 16, 'נתן') == 'set' and sg(5, 17, 'תרצח') == 'dash-in-pieces' and sg(5, 18, 'תנאף') == 'commit-adultery' and sg(5, 19, 'תגנב') == 'thieve'
assert sg(5, 20, 'תענה') == 'eye' and sg(5, 20, 'ברעך') == 'in-associate-you/your' and sg(5, 20, 'עד') == 'concretely' and sg(5, 20, 'שוא') == 'evil' and sg(5, 21, 'תחמד') == 'delight-in' and sg(5, 21, 'אשת') == 'woman' and sg(5, 21, 'רעך') == 'associate-you/your' and sg(5, 21, 'תתאוה') == 'wish-for' and sg(5, 21, 'שדהו') == 'field-him/its'
assert sg(5, 21, 'ועבדו') == 'and-servant-him/its' and sg(5, 21, 'ואמתו') == 'and-maidservant-him/its' and sg(5, 21, 'שורו') == 'bullock-him/its' and sg(5, 21, 'וחמרו') == 'and-male-ass-him/its' and sg(5, 21, 'לרעך') == 'to-associate-you/your' and sg(5, 22, 'הדברים') == 'the-word/thing' and sg(5, 22, 'קהלכם') == 'assemblage-you/your (pl)' and sg(5, 22, 'והערפל') == 'and-the-gloom'
assert sg(5, 22, 'יסף') == 'add' and sg(5, 22, 'ויכתבם') == 'and-grave-them/their' and sg(5, 22, 'לחת') == 'meaning-to-glisten' and sg(5, 22, 'ויתנם') == 'and-set-them/their' and sg(5, 23, 'כשמעכם') == 'like-hear-you/your (pl)' and sg(5, 23, 'בער') == 'kindle' and sg(5, 23, 'ותקרבון') == 'and-bring-near-suffix' and sg(5, 23, 'שבטיכם') == 'scion-you/your (pl)' and sg(5, 23, 'וזקניכם') == 'and-old-you/your (pl)'
assert sg(5, 24, 'הראנו') == 'see-us/our' and sg(5, 24, 'כבדו') == 'weight-him/its' and sg(5, 24, 'גדלו') == 'magnitude-him/its' and sg(5, 25, 'תאכלנו') == 'eat-us/our' and sg(5, 25, 'יספים') == 'add' and sg(5, 25, 'ומתנו') == 'and-die' and sg(5, 26, 'כמנו') == "form-of-the-prefix-'k-'-us/our" and sg(5, 27, 'קרב') == 'bring-near' and sg(5, 27, 'ואת') == 'and-thou-and-thee' and sg(5, 27, 'ועשינו') == 'and-make'
assert sg(5, 28, 'בדברכם') == 'in-speak-you/your (pl)' and sg(5, 28, 'היטיבו') == 'be--make-well' and sg(5, 29, 'יתן') == 'set' and sg(5, 29, 'לעלם') == 'to-forever' and sg(5, 30, 'לאהליכם') == 'to-tent-you/your (pl)' and sg(5, 31, 'עמדי') == 'along-with-me/my' and sg(5, 31, 'תלמדם') == 'goad-them/their' and sg(5, 31, 'לרשתה') == 'to-possess/inherit-her/its'
assert sg(5, 32, 'תסרו') == 'turn-aside' and sg(5, 32, 'ושמאל') == 'and-dark' and sg(5, 33, 'תחיון') == 'live-suffix' and sg(5, 33, 'וטוב') == 'and-be--good--in-the-widest-sens' and sg(5, 33, 'והארכתם') == 'and-be--long' and sg(5, 33, 'תירשון') == 'possess/inherit-suffix' and sg(5, 10, 'מצותו') == 'commandment-him/its' and sg(5, 10, 'מצותי') == 'commandment-me/my'
GLOSS_FAMILY = {'goad-them/their': [('תלמדם', 1)], 'and-the-enactment': [('והחקים', 3)], 'and-the-judgment': [('והמשפטים', 7)], 'commandment-him/its': [('מצותיו', 13), ('מצותו', 5)], 'commandment-me/my': [('מצותי', 10)], 'this-place': [('פה', 11)], 'in-face': [('בפנים', 1)], 'from-under': [('מתחת', 20)], 'depress': [('תשתחוה', 4), ('ישתחוו', 1), ('משתחוים', 1)], 'work/serve-them/their': [('תעבדם', 3)], 'descendant-of-the-third-degr': [('שלשים', 5)], 'descendant-of-the-fourth-gen': [('רבעים', 4)], 'to-hate-me/my': [('לשנאי', 2)], 'to-have-affection-for-me/my': [('לאהבי', 2)], 'to-evil': [('לשוא', 4)], 'the-intermission': [('השבת', 17)], 'intermission': [('שבת', 16), ('שבתת', 3), ('שבתות', 1)], 'to-sanctify-him/its': [('לקדשו', 5)], "form-of-the-prefix-'k-'-you/your": [('כמוך', 7), ('כמכה', 2)], "form-of-the-prefix-'k-'-us/our": [('כמנו', 2)], 'and-in-arm': [('ובזרע', 2), ('ובזרוע', 1)], 'in-associate-you/your': [('ברעך', 3)], 'delight-in': [('תחמד', 4), ('יחמד', 1), ('נחמד', 1)], 'associate-you/your': [('רעך', 13)], 'to-associate-you/your': [('לרעך', 3)], 'field-him/its': [('שדהו', 6)], 'bullock-him/its': [('שורו', 3)], 'and-male-ass-him/its': [('וחמרו', 2)], 'assemblage-you/your (pl)': [('קהלכם', 1)], 'and-the-gloom': [('והערפל', 1)], 'like-hear-you/your (pl)': [('כשמעכם', 1)], 'scion-you/your (pl)': [('שבטיכם', 5)], 'and-old-you/your (pl)': [('וזקניכם', 1)], 'see-us/our': [('הראנו', 1)], 'magnitude-him/its': [('גדלו', 2)], 'in-speak-you/your (pl)': [('בדברכם', 1)], 'to-forever': [('לעלם', 10), ('לעולם', 2)], 'along-with-me/my': [('עמדי', 19)], 'to-possess/inherit-her/its': [('לרשתה', 26)], 'live-suffix': [('תחיון', 3)], 'and-be--good--in-the-widest-sens': [('וטוב', 1)], 'and-be--long': [('והארכת', 1), ('והארכתם', 1)], 'to-make-them/their': [('לעשתם', 2), ('לעשותם', 1)], 'all-us/our': [('כלנו', 4)], 'to-tent-you/your (pl)': [('לאהליכם', 1)], 'and-bullock-you/your': [('ושורך', 1)], 'and-male-ass-you/your': [('וחמרך', 2)], 'livestock-you/your': [('בהמתך', 6)], 'and-sojourner-you/your': [('וגרך', 4)], 'in-gate-you/your': [('בשעריך', 17)], 'and-maidservant-you/your': [('ואמתך', 7)], 'maidservant-you/your': [('אמתך', 2)], 'day-you/your': [('ימיך', 9)], 'mother-you/your': [('אמך', 12)], 'and-goad': [('ולמדתם', 2), ('ולמדו', 1)], 'the-judgment': [('המשפטים', 9), ('המשפט', 6)], 'cut': [('כרת', 11), ('תכרת', 7), ('יכרת', 3), ('יכרית', 2), ('כרתי', 2), ('הכרת', 1), ('חצבת', 1), ('חצה', 1), ('חצובים', 1), ('כרתו', 1), ('נכרתה', 1), ('תחצב', 1), ('תכריתו', 1)], 'bring-forth-you/your': [('הוצאתיך', 3), ('הוצאך', 2), ('הוציאך', 2), ('צאתך', 2)], 'strength': [('אל', 32), ('אילי', 1)], 'perversity': [('עון', 17), ('עונת', 1), ('תהפכת', 1)], 'to-thousand': [('לאלפים', 3), ('לאלפי', 2), ('לאלף', 1)], 'and-to-keep/guard': [('ולשמר', 4), ('ולשמרי', 3)], 'be--clean': [('ינקה', 4), ('הנקי', 1), ('תנקה', 1)], 'and-mark': [('וזכרת', 7), ('ויזכר', 5), ('וזכרתי', 3), ('ואזכר', 1), ('וזכרתם', 1), ('ונזכרתם', 1)], 'be-heavy': [('כבד', 5), ('אכבד', 1), ('הכבדתי', 1), ('כבדה', 1), ('כבדו', 1), ('נכבד', 1), ('תכבד', 1)], 'be--long-suffix': [('תאריכן', 2), ('יאריכן', 1), ('יארכון', 1), ('יארכן', 1)], 'dash-in-pieces': [('רצח', 7), ('ירצח', 2), ('תרצח', 2), ('נפוץ', 1), ('נפצו', 1), ('רוצח', 1)], 'eye': [('עין', 17), ('עינים', 6), ('עיני', 5), ('עינת', 3), ('ענות', 3), ('תענה', 3), ('יענה', 2), ('ענה', 1), ('ענו', 1)], 'evil': [('עול', 4), ('שוא', 2)], 'wish-for': [('תאוה', 2), ('התאוו', 1), ('תתאוה', 1)], 'and-servant-him/its': [('ועבדיו', 3), ('ועבדו', 2)], 'and-maidservant-him/its': [('ואמתו', 2), ('ואמהתיו', 1)], 'add': [('יסף', 9), ('אסף', 4), ('תסף', 4), ('יסיף', 2), ('יספו', 2), ('יוסף', 1), ('יוספו', 1), ('יספה', 1), ('יספים', 1), ('תוסף', 1), ('תסיף', 1), ('תסיפו', 1), ('תספו', 1)], 'and-set-them/their': [('ונתנם', 5), ('ויתנם', 4)], 'weight-him/its': [('כבדו', 1), ('משקלו', 1)], 'eat-us/our': [('יאכלנו', 2), ('תאכלנו', 1)], 'and-thou-and-thee': [('ואת', 2), ('ואתנה', 1)], 'possess/inherit-suffix': [('ירשה', 1), ('תירשון', 1)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store
OVERRIDE_GLOSS = [('goad-them/their', 'you-shall-teach-them'), ('and-the-enactment', 'and-the-statutes'), ('and-the-judgment', 'and-the-judgments'), ('commandment-him/its', 'his-commandments'), ('commandment-me/my', 'my-commandments'), ('this-place', 'here'), ('in-face', 'to-face'), ('from-under', 'beneath'), ('depress', 'bow-down'), ('work/serve-them/their', 'serve-them'), ('descendant-of-the-third-degr', 'the-third-generation'), ('descendant-of-the-fourth-gen', 'the-fourth-generation'), ('to-hate-me/my', 'those-who-hate-me'), ('to-have-affection-for-me/my', 'those-who-love-me'), ('to-evil', 'in-vain'), ('the-intermission', 'the-sabbath'), ('intermission', 'sabbath'), ('to-sanctify-him/its', 'to-sanctify-it'), ("form-of-the-prefix-'k-'-you/your", 'like-you'), ("form-of-the-prefix-'k-'-us/our", 'like-us'), ('and-in-arm', 'and-with-an-arm'), ('in-associate-you/your', 'against-your-neighbor'), ('delight-in', 'covet'), ('associate-you/your', 'your-neighbor'), ('to-associate-you/your', 'to-your-neighbor'), ('field-him/its', 'his-field'), ('bullock-him/its', 'his-ox'), ('and-male-ass-him/its', 'and-his-ass'), ('assemblage-you/your (pl)', 'your-assembly'), ('and-the-gloom', 'and-the-thick-darkness'), ('like-hear-you/your (pl)', 'when-you-heard'), ('scion-you/your (pl)', 'your-tribes'), ('and-old-you/your (pl)', 'and-your-elders'), ('see-us/our', 'has-shown-us'), ('magnitude-him/its', 'his-greatness'), ('in-speak-you/your (pl)', 'when-you-spoke'), ('to-forever', 'forever'), ('along-with-me/my', 'with-me'), ('to-possess/inherit-her/its', 'to-possess-it'), ('live-suffix', 'you-may-live'), ('and-be--good--in-the-widest-sens', 'and-it-be-well'), ('and-be--long', 'and-you-shall-prolong'), ('to-make-them/their', 'to-do-them'), ('all-us/our', 'all-of-us'), ('to-tent-you/your (pl)', 'to-your-tents'), ('and-bullock-you/your', 'and-your-ox'), ('and-male-ass-you/your', 'and-your-ass'), ('livestock-you/your', 'your-cattle'), ('and-sojourner-you/your', 'and-your-stranger'), ('in-gate-you/your', 'within-your-gates'), ('and-maidservant-you/your', 'and-your-maidservant'), ('maidservant-you/your', 'your-maidservant'), ('day-you/your', 'your-days'), ('mother-you/your', 'your-mother')]
# BY REFERENCE — the family mixed (a homograph, two persons, an absolute beside a construct): the seat named
OVERRIDE_REF_SPEC = [(1, 'ולמדתם', 'and-you-shall-learn', 0), (1, 'המשפטים', 'the-judgments', 0), (1, 'אנכי', 'I', 0), (1, 'באזניכם', 'in-your-ears', 0), (2, 'כרת', 'made', 0), (3, 'כרת', 'made', 0), (5, 'אנכי', 'I', 0), (5, 'ההוא', 'that', 0), (6, 'אנכי', 'I', 0), (6, 'הוצאתיך', 'brought-you-out', 0), (6, 'עבדים', 'bondage', 0), (7, 'פני', 'my-face', 0), (8, 'פסל', 'a-graven-image', 0), (8, 'תמונה', 'form', 0), (9, 'אנכי', 'I', 0), (9, 'אל', 'God', 0), (9, 'פקד', 'visiting', 0), (9, 'עון', 'the-iniquity-of', 0), (10, 'ועשה', 'and-doing', 0), (10, 'לאלפים', 'to-thousands', 0), (10, 'ולשמרי', 'and-those-who-keep', 0), (11, 'תשא', 'take', 0), (11, 'ינקה', 'hold-guiltless', 0), (11, 'ישא', 'takes', 0), (12, 'שמור', 'keep', 0), (13, 'ועשית', 'and-you-shall-do', 0), (15, 'וזכרת', 'and-you-shall-remember', 0), (15, 'נטויה', 'outstretched', 0), (15, 'כן', 'therefore', 0), (16, 'כבד', 'honor', 0), (16, 'יאריכן', 'may-be-long', 0), (16, 'ייטב', 'it-may-go-well', 0), (16, 'נתן', 'gives', 0), (17, 'תרצח', 'murder', 0), (20, 'תענה', 'testify', 0), (20, 'שוא', 'vain', 0), (21, 'אשת', 'the-wife-of', 0), (21, 'תתאוה', 'desire', 0), (21, 'ועבדו', 'and-his-manservant', 0), (21, 'ואמתו', 'and-his-maidservant', 0), (22, 'הדברים', 'the-words', 0), (22, 'יסף', 'added', 0), (22, 'ויכתבם', 'and-he-wrote-them', 0), (22, 'ויתנם', 'and-he-gave-them', 0), (24, 'כבדו', 'his-glory', 0), (25, 'תאכלנו', 'will-consume-us', 0), (25, 'יספים', 'continue', 0), (25, 'ומתנו', 'and-we-shall-die', 0), (27, 'קרב', 'go-near', 0), (27, 'ואת', 'and-you', 0), (27, 'ועשינו', 'and-we-will-do', 0), (28, 'היטיבו', 'they-have-done-well', 0), (29, 'יתן', 'would-give', 0), (31, 'אנכי', 'I', 0), (31, 'נתן', 'give', 0), (31, 'ועשו', 'and-they-shall-do', 0), (32, 'תסרו', 'turn-aside', 0), (33, 'תירשון', 'you-shall-possess', 0)]
OVERRIDE_REF3 = [(f'Deut.5.{v}:{sidx(5, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == 58 and len({k for k, _ in OVERRIDE_REF}) == 58 and len(OVERRIDE_GLOSS) == 54 and len({k for k, _ in OVERRIDE_GLOSS}) == 54, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(5, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = ['goad', 'the-enactment', 'from-upper-part', 'meaning-to-glisten', 'kindle', 'and-bring-near-suffix', 'to-failure-of', 'be--make-well', 'in-time', 'hinder', 'and-dark', 'concretely', 'the-he/it']   # the rewrites of sittings 1 and 2 the chapter shares, left standing
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 3 (2026-09-16, Deuteronomy 5)' in OV
assert all(f'"{k}": ' in OV for k in ALREADY)
assert PATCHED or '"Deut.5.' not in OV
if not PATCHED: assert all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
else: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "circle-them/their": "round-about-them"') == 1 and OV.count('  "Deut.4.49:6": "the-sea-of"') == 1
