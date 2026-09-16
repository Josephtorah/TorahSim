import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK, sitting 2 — CHAPTER 4, Deuteronomy 4:1-49 (2026-09-16; the owner: "Go" after the rereads, on the rulings READ THEN
# COMPILE PER PORTION and CHAPTER NUMBERS): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes —
# never typed. Sitting 1's form (deu_ink.py): THE SIFREI ON DEUTERONOMY has NO PISKA ON CHAPTER 4 — piska 30 heads on 3:29, piska 31 on 6:4
# (the shelf's silence over the whole chapter, measured on the export's heads); the WHOLE export scanned in BOTH files for rows citing the
# chapter — SEVEN Hebrew rows, EIGHT English (301:21 English-only: the export's late piskaot carry an UNPOINTED Hebrew with abbreviations and an
# English citing "Devarim 4:34" with a space — a third citation form); two of the eight read at sitting 1 (30:2 fresh, 37:9 credited), SIX FRESH;
# the engine's numeral parser MEASURED on every verse — four number verses read, NO GAP; the hand's facts as asserts, run all at once by
# assert_driver.py after the measurement passes (ch4_dump0.py, ch4_measure1.py, ch4_measure2.py) printed them; every gloss the STORE'S OWN;
# the piece-wise cutters HP / AP / SP_. Shared by ch4_rows_onkelos_a/b.py, ch4_rows_sifrei.py, write_ch4_ledger.py, ch4_patch_overrides.py.
# THE SPAN: TWO drafts — deu_04_obey_horeb 4:1-40, deu_04_refuge_east 4:41-49 (the chapter as one sitting; the portion's grain crosses at 3:23).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata, subprocess
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-16'
CH = 4
UIDS = ['deu_04_obey_horeb', 'deu_04_refuge_east']
SPANS = {'deu_04_obey_horeb': (4, 1, 40), 'deu_04_refuge_east': (4, 41, 49)}
PREFIX = {'deu_04_obey_horeb': 'DV04A', 'deu_04_refuge_east': 'DV04B'}
PISKAOT = []   # no piska heads in chapter 4 — asserted below
OUTSIDE_HE = [(30, 2, (4, 1)), (37, 9, (4, 48)), (48, 2, (4, 9)), (49, 2, (4, 24)), (148, 8, (4, 19)), (306, 1, (4, 26)), (323, 1, (4, 44))]
OUTSIDE_EN = [(30, 2, (4, 1)), (37, 9, (4, 48)), (48, 2, (4, 9)), (49, 2, (4, 24)), (148, 8, (4, 19)), (301, 21, (4, 34)), (306, 1, (4, 26)), (323, 1, (4, 44))]
OUTSIDE = sorted({(p, r) for p, r, _ in OUTSIDE_HE} | {(p, r) for p, r, _ in OUTSIDE_EN})
FRESH = [(48, 2), (49, 2), (148, 8), (301, 21), (306, 1), (323, 1)]
CREDITED = {(30, 2): 'read FRESH at sitting 1 (the deu_01_03 ledger, MATERIAL — the span\'s last row, crossing from 3:29 into 4:1)', (37, 9): 'CREDITED at sitting 1 (the row on 11:10 — Hermon\'s four names, 3:9 with 4:48)'}
TITLE = 'Chapter 4 — and now, Israel, hear the statutes and the judgments: add nothing, take nothing away; your eyes saw Baal-peor; you who cleave to the LORD are all alive this day; taught as I was commanded, your wisdom before the peoples — what great nation has God so near, what nation such righteous statutes? Take heed lest you forget the day you stood at Horeb: the mountain burning to the heart of heaven, a voice of words and no form, the ten words on two tablets of stone; make no graven image of any form — male or female, beast, bird, creeping thing, fish — nor bow to the sun, moon and stars the LORD apportioned to all the peoples; you the LORD took from the iron furnace; the LORD was angry with me on your account and I die in this land; the LORD is a consuming fire, a jealous God. When you grow old in the land and corrupt yourselves, heaven and earth witness that you will perish, be scattered, serve wood and stone — and from there seek and find him, in the end of days return, for he is a merciful God who forgets not the covenant of the fathers. Ask of the former days since God created man: did a people hear the voice of God from the fire and live, did a god take a nation from a nation by trials, signs, wonders, war, a mighty hand, an outstretched arm and great terrors? You were shown to know that the LORD is God, none beside him; from heaven his voice, on earth his great fire; because he loved your fathers he chose their seed and brought you out with his presence; know this day and lay it to heart — the LORD is God in heaven above and on earth beneath, none else; keep his statutes that it go well with you and you prolong days. Then Moses set apart three cities beyond the Jordan toward the sunrise for the manslayer who slew unawares — Bezer, Ramoth, Golan; and this is the Torah Moses set before the children of Israel, the testimonies, statutes and judgments spoken when they came out of Egypt, beyond the Jordan in the valley opposite Beth-peor, in the land of Sihon and of Og, from Aroer on the Arnon to Mount Sion which is Hermon, all the Arabah to the sea of the Arabah under the slopes of Pisgah'
OUT = f'{ROOT}/logic/oral_triage/deu_04_vaetchanan_{DATE}.md'

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
# THE SHELF BY POSITION — the two files' grains, the heads around the chapter, NO piska on chapter 4
assert len(sif) == 357 and len(sif_he) == 357 and sum(len(s) for s in sif) == 2357 and sum(len(s) for s in sif_he) == 2357
assert [(p, len(sif_he[p - 1]), len(sif[p - 1])) for p in range(1, 358) if len(sif_he[p - 1]) != len(sif[p - 1])] == []
assert {p: heads[p] for p in range(24, 37)} == {24: (1, 27), 25: (1, 28), 26: (3, 23), 27: None, 28: (3, 25), 29: (3, 26), 30: (3, 29), 31: (6, 4), 32: (6, 5), 33: (6, 6), 34: (6, 7), 35: (6, 8), 36: (6, 9)}, {p: heads[p] for p in range(24, 37)}
HC = Counter(h[0] for h in heads.values() if h)
assert [p for p, h in heads.items() if h and h[0] == 4] == [] and HC[4] == 0 and HC[1] == 24 and HC[32] == 36 and HC[3] == 4, (HC[4], HC[1], HC[32], HC[3])
assert [p for p, h in heads.items() if h and h[0] == 3] == [26, 28, 29, 30] and [p for p, h in heads.items() if h and h[0] == 6][:1] == [31]
def he_cites(t): return [(b, hn(c), hn(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
CIT_HE = [(p, r, (4, c[2])) for p in range(1, 358) for r in range(1, len(sif_he[p - 1]) + 1) for c in he_cites(Hb(p, r)) if c[0] == 'דברים' and c[1] == 4]
CIT_EN = [(p, r, (4, int(m.group(2)))) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) for m in re.finditer(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(4):(\d+)', E(p, r))]
assert CIT_HE == OUTSIDE_HE and CIT_EN == OUTSIDE_EN and len(OUTSIDE) == 8 and OUTSIDE == [(30, 2), (37, 9), (48, 2), (49, 2), (148, 8), (301, 21), (306, 1), (323, 1)], (CIT_HE, CIT_EN)
assert [(p, r) for p in range(1, 358) for r in range(1, len(sif[p - 1]) + 1) if re.search(r'\((?:Ibid|ibid)\.? ?4:\d+\)', E(p, r))] == []
assert {p: heads[p] for p, _ in OUTSIDE} == {30: (3, 29), 37: (11, 10), 48: (11, 22), 49: (11, 22), 148: (17, 2), 301: (26, 5), 306: (32, 1), 323: (32, 29)}
# THE THIRD CITATION FORM: 301:21's Hebrew is UNPOINTED, abbreviated ("כמ"ש" — "as it is written"), and cites nothing in parentheses; its English
# cites "(Devarim 4:34)" WITH A SPACE — the late piskaot of the export are another stratum (sitting 1 measured "Dt." 3,292 times, "Deut." once).
def has_points(s): return any(0x05B0 <= ord(c) <= 0x05BD for c in s)
assert not has_points(Hb(301, 21)) and 'כמ"ש' in Hb(301, 21) and he_cites(Hb(301, 21)) == [] and '(Devarim 4:34)' in E(301, 21)
assert all(has_points(Hb(p, r)) for p, r in OUTSIDE if (p, r) != (301, 21)) and all(re.search(r'\(Dt\.4:\d+\)', E(p, r)) for p, r in OUTSIDE if (p, r) != (301, 21))
assert '(דברים ד א)' in Hb(30, 2) and '(דברים ד מח)' in Hb(37, 9) and '(דברים ד ט)' in Hb(48, 2) and '(דברים ד כד)' in Hb(49, 2) and '(דברים ד יט)' in Hb(148, 8) and '(דברים ד כו)' in Hb(306, 1) and '(דברים ד מד)' in Hb(323, 1)
assert len(Hb(306, 1)) > 2000 and Hb(306, 1).count('הֵעִיד בָּהֶם') == 11 and E(306, 1).count('to testify against them') == 10   # the witnesses' chain: the heavens (4:26) the third summoned
# THE PRIOR READS — the strict row form "Sifrei Devarim p:r" over every ledger: two of the eight rows read at sitting 1, the six FRESH
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
assert [(f, p, r) for f, p, r in PRIOR if (p, r) in OUTSIDE] == [('deu_01_03_devarim_2026-09-15.md', 30, 2), ('deu_01_03_devarim_2026-09-15.md', 37, 9)] and len(PRIOR) == 205, len(PRIOR)
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 4:', t, re.M)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 4:\d+', t))
assert len(NAMING) == 20 and 'num_35_refuge_cities_2026-09-13.md' in NAMING and 'num_35_refuge_cities_exam_2026-09-13.md' in NAMING and 'deu_01_03_devarim_exam_2026-09-15.md' in NAMING and 'num_12_miriam_2026-09-10.md' in NAMING, len(NAMING)
assert re.search(r'^- Sifrei Devarim 30:2 — MATERIAL\.', LED['deu_01_03_devarim_2026-09-15.md'], re.M) and re.search(r'^- Sifrei Devarim 37:9 — CREDITED', LED['deu_01_03_devarim_2026-09-15.md'], re.M)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
ONK_LEN = {c: len(onk[c - 1]) for c in (3, 4, 5)}   # THE EXPORT'S CHAPTER 5 HAS THIRTY VERSES against the DB's thirty-three — the Decalogue's verse division differs (the one chapter of the book where the export and the DB disagree, measured here for chapter 5's sitting)
assert len(onk) == 34 and len(onk_he) == 34 and ONK_LEN == {3: 29, 4: 49, 5: 30} and {c: len(onk_he[c - 1]) for c in (3, 4, 5)} == ONK_LEN and sum(len(c) for c in onk_he) == 956, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_deut = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Deuteronomy|Devarim', d))
outside = [d for d in shelf_deut if d not in ('Sifrei_Devarim', 'Onkelos_Deuteronomy')]
assert len(shelf_deut) == 28 and len(outside) == 26, len(outside)

# ---- THE DRAFTS' SPANS, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
assert VC[4] == 49 and VC[3] == 29 and VC[5] == 33 and sum(VC.values()) == 959 and len(VC) == 34
assert [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35) if len(onk_he[c - 1]) != VC[c]] == [(5, 30, 33)]   # the export's one disagreement with the DB's division: chapter 5
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Dt_(\d+)_(\d+)', unit_text(uid))})
FIRST = not os.path.exists(OUT)   # the first pass: the two units are drafts without operators or step E; after the seat and the ritual they are frozen
for uid, (c, lo, hi) in SPANS.items():
    t = unit_text(uid)
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and re.search(rf'refs: "?{c}:{lo}-{hi}"?', t) and '\nbinary_trees:' in t, uid
    if FIRST: assert 'status: draft' in t and 'operators:' not in t and '- step: E' not in t, uid
    assert t.count(f'  - id: STEP_Dt_{c}_{lo}\n') == 1 and t.count(f'  - id: STEP_Dt_{c}_{hi}\n') == 1, uid
assert unit_text('deu_04_obey_horeb').count('    comment: >\n') == 84 and unit_text('deu_04_refuge_east').count('    comment: >\n') == 22   # two per step (the step's and its map's) and the four of the derivation log
assert 'deu_03_moses_barred' in unit_text('deu_04_obey_horeb') and 'exo_20_decalogue_altar' in unit_text('deu_04_obey_horeb') and 'num_35_refuge_cities' in unit_text('deu_04_refuge_east') and 'deu_04_obey_horeb' in unit_text('deu_04_refuge_east')
assert steps('deu_05_decalogue')[0] == (5, 1)   # the next draft opens at 5:1 — the chapter's two drafts cover it whole (49 of 49, computed)
assert sorted(f for f in os.listdir(TRI) if f.startswith('deu_')) == ['deu_01_03_devarim_2026-09-15.md', 'deu_01_03_devarim_exam_2026-09-15.md'] + ([os.path.basename(OUT)] if not FIRST else [])
ALLTXT = ''.join(open(f'{ROOT}/logic/units/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/units') if f.endswith('.yaml') and f[:-5] not in UIDS) + ''.join(open(f'{ROOT}/logic/oral_audit/manifests/{f}', encoding='utf-8').read() for f in os.listdir(f'{ROOT}/logic/oral_audit/manifests') if f.endswith('.json') and f[:-12] not in UIDS)
assert all(f'"{p}-' not in ALLTXT and f'[claim {p}-' not in ALLTXT for p in PREFIX.values())
SPAN = [(4, v) for v in range(1, VC[4] + 1)]
NV = 49
assert len(SPAN) == NV

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byl = {}, {}, {}
for b, c, v, he, m, lem in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byl.setdefault((b, c, v), []).append((lem or '').split('/')[-1].strip())
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
def W4(v): return words('Deut', 4, v)
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
def DIFF(a, b_):
    import difflib
    A, B = words(*a), words(*b_)
    return [(op, A[i1:i2], B[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B).get_opcodes() if op != 'equal']
def SHARED(a, b_):
    """the longest run of tokens the two verses share, in order (the retelling's kept words)"""
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
        while j < len(ws) and plain(ws[j]) != k: j += 1
        if j >= len(ws): FAIL.append(('A', c, v, k, [plain(x) for x in ws])); out.append('⟨MISS⟩'); continue
        out.append(ws[j]); i = j + 1
    return ' '.join(out)
def aramaic(c, v): return [plain(x) for x in onk_ev(c, v)[1].rstrip(':').split()]
def arm(c, v): return plain(onk_ev(c, v)[1])
def onk_seats(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in arm(c + 1, v + 1)]
def onk_tok(tok): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if tok in aramaic(c + 1, v + 1)]
def HP(c, v, *pieces):
    """the Hebrew cut in GLOSSED PIECES — each piece a (tokens, gloss) pair of at most seven tokens, the gloss right after it (the lint's window)"""
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
    """a Sifrei Hebrew row cut by consonants — the shelf's own bytes (pointed in this export; 301:21 unpointed)"""
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
for c, v, idx, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter = 4 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((idx, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]
    if len(hit) <= nth: raise KeyError((c, v, tok, nth))
    return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]
    assert len(hit) > nth, (c, v, tok, nth, hit)
    return hit[nth]
STORE_MISMATCH = [(c, v, n, len(by[('Deut', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=4 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Deut', c, v)])]
assert STORE_MISMATCH == [] and all([hp for _, hp, _ in SG[(4, v)]] == W4(v) for v in range(1, 50)), STORE_MISMATCH   # no written-and-read pair in the chapter; the store's tokens the DB's

# THE ENGINE'S PARSER on every verse — MEASURED before the compile is asked: FOUR number verses read, NO GAP — 4:13 "the ten words … two tablets"
# [10, 2] (the construct "two" marked ^), 4:41 "three cities" [3], 4:42 "one of these cities" [1], 4:47 "the two kings" [2] (marked ^); no ordinals
# — 4:32's "former days" is the adjective (7223), not a count; the same phrases read the same at their other seats (10:4 [10]; Exodus 34:28
# [40, 40, 10]; 19:7 and 19:9 [3]; 19:5 and 19:11 [1]).
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {(c, v): N('Deut', c, v) for (c, v) in SPAN if N('Deut', c, v)}
assert PARSED == {(4, 13): [10, 2], (4, 41): [3], (4, 42): [1], (4, 47): [2]}, PARSED
assert {(c, v): O('Deut', c, v) for (c, v) in SPAN if O('Deut', c, v)} == {} and [((c, v), t) for (c, v) in SPAN for t in CS.verse_words('Deut', c, v) if t[-1] in '#~^%@|*'] == [((4, 13), 'שני^'), ((4, 47), 'שני^')]
assert N('Deut', 10, 4) == [10] and N('Exod', 34, 28) == [40, 40, 10] and N('Deut', 19, 7) == [3] and N('Deut', 19, 9) == [3] and N('Deut', 19, 5) == [1] and N('Deut', 19, 11) == [1] and N('Amos', 4, 8) == [5, 1]
assert lemma_of('Deut', 4, 32, 'ראשנים') == ['7223'] and PT('Deut', 4, 32, 'ראשנים') == ['רִֽאשֹׁנִים'] and O('Deut', 4, 32) == [] and lemma_of('Deut', 4, 31, 'נשבע') == ['7650']   # "former" the adjective; "swore" not "seven"
TOK = sum(len(by[('Deut', 4, v)]) for v in range(1, 50))
assert TOK == 813, TOK

# THE FRAMES AND THE REGISTER: ONE divine frame — "and the LORD spoke to you" at 4:12 (the Bible's one seat of that form; "the LORD spoke to
# you" without the vav 4:15 and 10:4); NO "saying" in the chapter; the narrative verbs at 4:11-13 (Horeb), 20-21, 33, 37, 47 — the speech in
# the SECOND PERSON, singular and plural by turns; the imperatives "hear" (4:1), "see" (4:5), "take heed" (4:9, the plural 4:23), God's "assemble"
# (4:10), "ask" (4:32); the prohibitions "you shall not add … nor diminish" (4:2), "lest you forget" (4:9, 23), "lest you corrupt" (4:16), "lest
# you lift your eyes" (4:19), "you shall not prolong" (4:26); THE CASE TOKENS: "for" at fifteen seats, "lest" four, "or" three, no "if"; THE
# REGISTER GATE: Deut 4:5 NONE declared ("the book not read" — this reading pays it at the compile), Deut 4:45 DAEMONS green (the footer of the
# block (Deut 1:1, Deut 4:45] since 1b).
DIV = [(c, v) for (c, v) in SPAN if any(W4(v)[i] in ('ויאמר', 'וידבר') and W4(v)[i + 1] == 'יהוה' for i in range(len(W4(v)) - 1))]
assert DIV == [(4, 12)] and P('וידבר', 'יהוה', 'אליכם') == ['Deut 4:12'] and P('דבר', 'יהוה', 'אליכם') == S_('Deut 10:4', 'Deut 4:15') and P('דבר', 'יהוה', 'אליכם', 'בחרב') == ['Deut 4:15'] and P('פנים', 'בפנים') == ['Deut 5:4']
assert [(c, v) for (c, v) in SPAN if 'לאמר' in W4(v)] == []
REG = {v: [x for x, m in by[('Deut', 4, v)] if m and re.search(r'V.w', m)] for v in range(1, 50) if any(m and re.search(r'V.w', m) for x, m in by[('Deut', 4, v)])}
assert REG == {11: ['ותקרבון', 'ותעמדון'], 12: ['וידבר'], 13: ['ויגד', 'ויכתבם'], 20: ['ויוצא'], 21: ['וישבע'], 33: ['ויחי'], 37: ['ויבחר', 'ויוצאך'], 47: ['ויירשו']}, REG
CASE = {f'{c}:{v}': [x for x in W4(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for (c, v) in SPAN if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in W4(v))}
assert CASE == {'4:3': ['כי'], '4:6': ['כי'], '4:7': ['כי'], '4:9': ['פן'], '4:15': ['כי'], '4:16': ['פן', 'או'], '4:22': ['כי'], '4:23': ['פן'], '4:24': ['כי'], '4:25': ['כי'], '4:26': ['כי', 'כי'], '4:29': ['כי'], '4:31': ['כי'], '4:32': ['כי', 'או'], '4:34': ['או'], '4:35': ['כי'], '4:37': ['כי'], '4:39': ['כי']}, CASE
assert Counter(x for l in CASE.values() for x in l) == Counter({'כי': 15, 'פן': 3, 'או': 3}) and 'אם' not in Counter(x for l in CASE.values() for x in l) and 'ופן' in W4(19) and 'ופן' in W4(9)
NUM2 = {v: (sum(1 for _, m in by[('Deut', 4, v)] if m and '2mp' in m), sum(1 for _, m in by[('Deut', 4, v)] if m and '2ms' in m)) for v in range(1, 50)}
SG_ONLY = [v for v, (p, s) in NUM2.items() if s and not p]; PL_ONLY = [v for v, (p, s) in NUM2.items() if p and not s]; BOTH = [v for v, (p, s) in NUM2.items() if p and s]; NEITHER = [v for v, (p, s) in NUM2.items() if not p and not s]
assert SG_ONLY == [10, 19, 24, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40] and PL_ONLY == [2, 4, 6, 8, 11, 12, 13, 14, 15, 16, 20, 22, 26, 27, 28] and BOTH == [1, 3, 5, 9, 21, 23, 25, 29, 34] and NEITHER == [7, 17, 18] + list(range(41, 50)), (SG_ONLY, PL_ONLY, BOTH, NEITHER)
assert NUM2[9] == (1, 10) and NUM2[40] == (0, 8) and NUM2[23] == (7, 2) and NUM2[1] == (6, 1)
IMPER = {v: [(x, m) for x, m in by[('Deut', 4, v)] if m and re.match(r'^HV.v', m)] for v in range(1, 50) if any(m and re.match(r'^HV.v', m) for _, m in by[('Deut', 4, v)])}
assert IMPER == {1: [('שמע', 'HVqv2ms')], 5: [('ראה', 'HVqv2ms')], 9: [('השמר', 'HVNv2ms')], 10: [('הקהל', 'HVhv2ms')], 23: [('השמרו', 'HVNv2mp')], 32: [('שאל', 'HVqv2ms')]}, IMPER
PROHIB = {v: [x for i, (x, m) in enumerate(by[('Deut', 4, v)]) if i and by[('Deut', 4, v)][i - 1][0] in ('לא', 'פן', 'ופן', 'ולא') and m and m.startswith('HV') and 'i2' in m] for v in range(1, 50)}
PROHIB = {v: l for v, l in PROHIB.items() if l}
assert PROHIB == {2: ['תספו', 'תגרעו'], 9: ['תשכח'], 16: ['תשחתון'], 19: ['תשא'], 23: ['תשכחו'], 26: ['תאריכן']}, PROHIB
YG_SG = [v for v in range(1, 50) for i in range(len(W4(v)) - 1) if W4(v)[i:i + 2] == ['יהוה', 'אלהיך']]; YG_PL = [v for v in range(1, 50) for i in range(len(W4(v)) - 1) if W4(v)[i:i + 2] == ['יהוה', 'אלהיכם']]
assert YG_SG == [3, 10, 19, 21, 23, 24, 25, 29, 30, 31, 40] and YG_PL == [2, 23, 34] and [v for v in range(1, 50) for i in range(len(W4(v)) - 1) if W4(v)[i:i + 2] == ['יהוה', 'אלהי']] == [1, 5] and [v for v in range(1, 50) for i in range(len(W4(v)) - 1) if W4(v)[i:i + 2] == ['יהוה', 'אלהינו']] == []
NAME = Counter(x for v in range(1, 50) for x in W4(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))
assert NAME == Counter({'יהוה': 26, 'ביהוה': 1, 'כיהוה': 1, 'ויהוה': 1}) and sum(NAME.values()) == 29
assert [v for v in range(1, 50) if 'משה' in W4(v)] == [41, 44, 45, 46] and [v for v in range(1, 50) for i in range(len(W4(v)) - 1) if W4(v)[i:i + 2] == ['בני', 'ישראל']] == [44, 45]
assert {v: [x for x in W4(v) if x in ('אלהים', 'האלהים')] for v in range(1, 50) if any(x in ('אלהים', 'האלהים') for x in W4(v))} == {7: ['אלהים'], 28: ['אלהים'], 32: ['אלהים'], 33: ['אלהים'], 34: ['אלהים'], 35: ['האלהים'], 39: ['האלהים']}
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read(); RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
assert sorted(re.findall(r'^\s*Deut (4:\d+)\s+(\w+)\s+(\w+)', RI, re.M)) == [('4:45', 'DAEMONS', 'green'), ('4:5', 'NONE', 'declared')] and re.search(r'^\s*Deut 4:45\s+DAEMONS\s+green\s+FOOTER testimonies stamp none block \(Deut 1:1, Deut 4:45\] daemons 1', RI, re.M)
assert re.search(r'^  Deut 4:5:\n    class: NONE\n    why: Deuteronomy is not on the tape \(the book not read\)', RD, re.M) and '  Deut 4:45:\n' not in RD

# 4:1-8 THE EXHORTATION (computed): "and now, Israel" this and 10:12; "hear, O Israel" four seats, all this book's (5:1, 6:4, 9:1, 20:3) — 4:1
# opens with the singular imperative and the PLURAL object ("I teach YOU"); "the statutes and the judgments" with the article three seats (Lev
# 26:46, 6:1, 12:1), the bare pair 4:5, 4:8, 4:14 and Malachi 3:22 — the chapter carries the pair four times; "which I teach you" one seat; the
# teach-root's Torah seats all this book's but none before 4:1 — sixteen, four in this chapter; "YOU SHALL NOT ADD … NOR DIMINISH" 4:2 (the
# plural) and 13:1 (the singular) — the pair's two seats; "Baal-peor" 4:3 and Hosea 9:10 — Peor at twelve seats; "you who cleave" the adjective's
# three seats; "alive all of you this day" one seat; "AS THE LORD MY GOD COMMANDED ME" 4:5 and 10:5 (the receipt form in Moses' own voice — the
# register's seat 4:5); "your wisdom and your understanding" one seat, "a wise and understanding people" one, "wise and understanding" this and
# Solomon's (1 Kings 3:12); "this great nation" one seat; "great nation" 4:7-8 only; "God near" one; "righteous statutes" one; "like all this
# Torah" one; "which I set before you this day" 4:8 and 11:32.
assert P('ועתה', 'ישראל') == S_('Deut 10:12', 'Deut 4:1') and P('שמע', 'ישראל') == S_('Deut 20:3', 'Deut 5:1', 'Deut 6:4', 'Deut 9:1') and wm('Deut', 4, 1)[2] == ('שמע', 'HVqv2ms') and wm('Deut', 4, 1)[10] == ('אתכם', 'HTo/Sp2mp')
assert P('החקים', 'והמשפטים') == S_('Deut 12:1', 'Deut 6:1', 'Lev 26:46') and P('חקים', 'ומשפטים') == S_('Deut 4:14', 'Deut 4:5', 'Deut 4:8', 'Mal 3:22') and P('ואל', 'המשפטים') == ['Deut 4:1'] and P('אשר', 'אנכי', 'מלמד', 'אתכם') == ['Deut 4:1']
assert LEMV('3925', T) == S_('Deut 11:19', 'Deut 14:23', 'Deut 17:19', 'Deut 18:9', 'Deut 20:18', 'Deut 31:12', 'Deut 31:13', 'Deut 31:19', 'Deut 31:22', 'Deut 4:1', 'Deut 4:10', 'Deut 4:14', 'Deut 4:5', 'Deut 5:1', 'Deut 5:31', 'Deut 6:1') and len(LEMV('3925', T)) == 16
assert P('לא', 'תספו', 'על', 'הדבר') == ['Deut 4:2'] and P('לא', 'תספו') == ['Deut 4:2'] and sorted(set(P('ולא', 'תגרעו')) | set(P('ולא', 'תגרע'))) == S_('Deut 13:1', 'Deut 4:2') and W4(2)[:2] == ['לא', 'תספו'] and words('Deut', 13, 1)[10:16] == ['לא', 'תסף', 'עליו', 'ולא', 'תגרע', 'ממנו']
assert P('לשמר', 'את', 'מצות', 'יהוה', 'אלהיכם') == ['Deut 4:2'] and P('למען', 'תחיו', books=T) == ['Deut 4:1'] and P('ובאתם', 'וירשתם', 'את', 'הארץ') == S_('Deut 11:8', 'Deut 4:1', 'Deut 8:1') and P('יהוה', 'אלהי', 'אבתיכם', books=('Deut',)) == ['Deut 4:1']
assert P('בעל', 'פעור') == S_('Deut 4:3', 'Hos 9:10') and P('בבעל', 'פעור') == ['Deut 4:3'] and len(U('פעור')) == 12 and P('בית', 'פעור') == S_('Deut 34:6', 'Deut 3:29', 'Deut 4:46') and P('עיניכם', 'הראת') == S_('Deut 11:7', 'Deut 4:3') and P('עיניך', 'הראת') == ['Deut 3:21']
assert P('השמידו', 'יהוה', 'אלהיך', 'מקרבך') == ['Deut 4:3'] and len(U('מקרבך', books=('Deut',))) == 11 and PT('Deut', 4, 3, 'הראת') == ['הָֽרֹאֹת'] and PT('Deut', 4, 35, 'הראת') == ['הָרְאֵתָ'] and morphs('Deut', 4, 3)[1] == 'HTd/Vqrfpa' and morphs('Deut', 4, 35)[1] == 'HVHp2ms'
assert LEMV('1695') == S_('2Chr 3:12', 'Deut 4:4', 'Prov 18:24') and P('ואתם', 'הדבקים', 'ביהוה') == ['Deut 4:4'] and P('חיים', 'כלכם', 'היום') == ['Deut 4:4']
assert P('כאשר', 'צוני', 'יהוה', 'אלהי') == ['Deut 4:5'] and P('כאשר', 'צוני', 'יהוה') == S_('Deut 10:5', 'Deut 4:5') and U('צוני') == S_('1Sam 21:3', '2Sam 14:19', 'Deut 10:5', 'Deut 4:5', 'Ezek 37:10') and P('ראה', 'למדתי', 'אתכם') == ['Deut 4:5'] and P('אשר', 'אתם', 'באים', 'שמה', 'לרשתה') == ['Deut 4:5']
assert P('חכמתכם', 'ובינתכם') == ['Deut 4:6'] and P('עם', 'חכם', 'ונבון') == ['Deut 4:6'] and P('חכם', 'ונבון') == S_('1Kgs 3:12', 'Deut 4:6') and P('הגוי', 'הגדול', 'הזה') == ['Deut 4:6'] and P('ושמרתם', 'ועשיתם') == S_('Deut 4:6', 'Deut 7:12') and P('לעיני', 'העמים') == ['Deut 4:6']
assert P('גוי', 'גדול') == S_('Deut 4:7', 'Deut 4:8') and P('כי', 'מי', 'גוי', 'גדול') == ['Deut 4:7'] and P('אלהים', 'קרבים') == ['Deut 4:7'] and P('חקים', 'ומשפטים', 'צדיקם') == ['Deut 4:8'] and P('ככל', 'התורה', 'הזאת') == ['Deut 4:8'] and P('אשר', 'אנכי', 'נתן', 'לפניכם', 'היום') == S_('Deut 11:32', 'Deut 4:8')
assert U('התורה', 'תורה', 'תורת', books=('Deut',)) == S_('Deut 17:11', 'Deut 17:18', 'Deut 17:19', 'Deut 1:5', 'Deut 27:26', 'Deut 27:3', 'Deut 27:8', 'Deut 28:58', 'Deut 28:61', 'Deut 29:20', 'Deut 29:28', 'Deut 30:10', 'Deut 31:11', 'Deut 31:12', 'Deut 31:24', 'Deut 31:26', 'Deut 31:9', 'Deut 32:46', 'Deut 33:4', 'Deut 4:44', 'Deut 4:8')

# 4:9-14 HOREB RETOLD (computed): "only take heed to yourself" one seat — "take heed to yourself" twelve (Genesis 24:6 the first), "take heed
# to yourselves" three (Exodus 19:12 at Sinai, 4:23, 11:16); "and keep your soul diligently" one; "lest you forget" the pair 4:9 and 4:23 among
# the forget-root's thirteen Deuteronomy seats; "which your eyes saw" five seats; "your sons and your sons' sons" one (the pair "sons and sons'
# sons" 4:25 and 1 Chronicles 8:40); "THE DAY YOU STOOD" one seat; "before the LORD your God at Horeb" one; HOREB by lemma seventeen seats, twelve
# Torah (Exodus 3:1 the first; this book's nine — 1:2, 6, 19, 4:10, 15, 5:2, 9:8, 18:16, 28:69); "assemble to me the people" one — the same verb
# at 31:12's Hakhel; "and they shall teach their sons" — 4:10's TWO ילמדון ("they shall learn" qal, "they shall teach" piel: one written form, two
# stems, the store glossing both "goad-suffix"); "and you came near and stood" one; "under the mountain" 4:11, Exodus 24:4, 32:19; "burning with
# fire" four (Exodus 3:2's bush first); "to the heart of heaven" one; "darkness, cloud and thick darkness" one — "cloud and thick darkness" five;
# "FROM THE MIDST OF THE FIRE" TEN Deuteronomy seats and Ezekiel 1:4 — five in this chapter (12, 15, 33, 36) and 5:4, 22, 24, 26, 9:10, 10:4; "a
# voice of words" one; "form" (8544) ten seats, five this chapter's; "save a voice" one; "his covenant" four Torah seats; "THE TEN WORDS" 4:13,
# 10:4, Exodus 34:28; "two tablets of stone" one — 4:13's "tablets" PLENE (three Bible seats: 4:13, 9:11, 1 Kings 8:9) where Exodus writes it
# defective at all its seats; "and me the LORD commanded at that time" one; "at that time" fifteen Deuteronomy seats; "to teach you statutes" one.
assert P('רק', 'השמר', 'לך') == ['Deut 4:9'] and len(P('השמר', 'לך')) == 12 and P('השמר', 'לך')[-3:] == S_('Gen 24:6', 'Gen 31:24', 'Gen 31:29') and P('השמרו', 'לכם') == S_('Deut 11:16', 'Deut 4:23', 'Exod 19:12') and P('ושמר', 'נפשך', 'מאד') == ['Deut 4:9']
assert LEMV('7911', ('Deut',)) == S_('Deut 24:19', 'Deut 25:19', 'Deut 26:13', 'Deut 31:21', 'Deut 32:18', 'Deut 4:23', 'Deut 4:31', 'Deut 4:9', 'Deut 6:12', 'Deut 8:11', 'Deut 8:14', 'Deut 8:19', 'Deut 9:7') and P('אשר', 'ראו', 'עיניך') == S_('Deut 10:21', 'Deut 29:2', 'Deut 4:9', 'Deut 7:19', 'Prov 25:7')
assert P('לבניך', 'ולבני', 'בניך') == ['Deut 4:9'] and P('בנים', 'ובני', 'בנים') == S_('1Chr 8:40', 'Deut 4:25') and P('כל', 'ימי', 'חייך') == S_('Deut 16:3', 'Deut 4:9', 'Deut 6:2', 'Gen 3:14', 'Gen 3:17', 'Josh 1:5', 'Ps 128:5') and U('והודעתם') == S_('Deut 4:9', 'Josh 4:22')
assert P('יום', 'אשר', 'עמדת') == ['Deut 4:10'] and P('לפני', 'יהוה', 'אלהיך', 'בחרב') == ['Deut 4:10'] and LEMV('2722') == S_('1Kgs 19:8', '1Kgs 8:9', '2Chr 5:10', 'Deut 18:16', 'Deut 1:19', 'Deut 1:2', 'Deut 1:6', 'Deut 28:69', 'Deut 4:10', 'Deut 4:15', 'Deut 5:2', 'Deut 9:8', 'Exod 17:6', 'Exod 33:6', 'Exod 3:1', 'Mal 3:22', 'Ps 106:19') and len(LEMV('2722', T)) == 12
assert P('הקהל', 'לי', 'את', 'העם') == ['Deut 4:10'] and 'Deut 31:12' in U('הקהל') and P('ליראה', 'אתי', 'כל', 'הימים') == ['Deut 4:10'] and P('ואת', 'בניהם', 'ילמדון') == ['Deut 4:10'] and P('ואשמעם', 'את', 'דברי') == ['Deut 4:10']
assert [(x, m) for x, m in by[('Deut', 4, 10)] if x == 'ילמדון'] == [('ילמדון', 'HVqi3mp/Sn'), ('ילמדון', 'HVpi3mp/Sn')] and PT('Deut', 4, 10, 'ילמדון') == ['יִלְמְדוּן', 'יְלַמֵּדֽוּן'] and sg(4, 10, 'ילמדון', 0) == 'goad-suffix' and sg(4, 10, 'ילמדון', 1) == 'goad-suffix'
assert P('ותקרבון', 'ותעמדון') == ['Deut 4:11'] and P('תחת', 'ההר') == S_('Deut 4:11', 'Exod 24:4', 'Exod 32:19') and P('בער', 'באש') == S_('Deut 4:11', 'Deut 5:23', 'Deut 9:15', 'Exod 3:2') and P('עד', 'לב', 'השמים') == ['Deut 4:11'] and P('לב', 'השמים') == ['Deut 4:11']
assert P('חשך', 'ענן', 'וערפל') == ['Deut 4:11'] and P('ענן', 'וערפל') == S_('Deut 4:11', 'Ezek 34:12', 'Joel 2:2', 'Ps 97:2', 'Zeph 1:15') and P('האש', 'הענן', 'והערפל') == ['Deut 5:22'] and len(U('ערפל', 'וערפל', 'הערפל', 'בערפל', 'והערפל')) == 14
assert P('מתוך', 'האש') == S_('Deut 10:4', 'Deut 4:12', 'Deut 4:15', 'Deut 4:33', 'Deut 4:36', 'Deut 5:22', 'Deut 5:24', 'Deut 5:26', 'Deut 5:4', 'Deut 9:10', 'Ezek 1:4') and P('קול', 'דברים') == ['Deut 4:12'] and P('זולתי', 'קול') == ['Deut 4:12']
assert LEMV('8544') == S_('Deut 4:12', 'Deut 4:15', 'Deut 4:16', 'Deut 4:23', 'Deut 4:25', 'Deut 5:8', 'Exod 20:4', 'Job 4:16', 'Num 12:8', 'Ps 17:15') and P('כל', 'תמונה') == S_('Deut 4:15', 'Deut 5:8') and P('לא', 'ראיתם', 'כל', 'תמונה') == ['Deut 4:15']
assert U('בריתו', books=T) == S_('Deut 17:2', 'Deut 4:13', 'Deut 8:18', 'Exod 2:24') and P('בריתו', 'אשר', 'צוה', 'אתכם') == ['Deut 4:13'] and P('עשרת', 'הדברים') == S_('Deut 10:4', 'Deut 4:13', 'Exod 34:28') and P('שני', 'לחות', 'אבנים') == ['Deut 4:13'] and P('ויכתבם', 'על') == S_('Deut 4:13', 'Deut 5:22')
assert U('לחות') == S_('1Kgs 8:9', 'Deut 4:13', 'Deut 9:11') and PT('Deut', 4, 13, 'לחות') == ['לֻחוֹת'] and U('לחת') == S_('Deut 10:3', 'Deut 5:22', 'Deut 9:11', 'Deut 9:15', 'Exod 24:12', 'Exod 27:8', 'Exod 31:18', 'Exod 32:15', 'Exod 34:1', 'Exod 34:29', 'Exod 34:4', 'Exod 38:7') and words('Deut', 5, 22)[-5:-2] == ['שני', 'לחת', 'אבנים']
assert P('ואתי', 'צוה', 'יהוה', 'בעת', 'ההוא') == ['Deut 4:14'] and len(P('בעת', 'ההוא', books=('Deut',))) == 15 and P('ללמד', 'אתכם', 'חקים') == ['Deut 4:14'] and P('ללמד', 'אתכם') == S_('Deut 4:14', 'Deut 6:1') and P('אשר', 'אתם', 'עברים', 'שמה', 'לרשתה') == S_('Deut 11:11', 'Deut 11:8', 'Deut 4:14', 'Deut 6:1')

# 4:15-24 NO IMAGE (computed): "and you shall take heed to your souls" 4:15 and Joshua 23:11; "on the day the LORD spoke to you" one; "lest you
# corrupt" one; "a graven image" twenty-three Bible seats, 4:16, 23, 25 among them; "a graven image, the form of any" THREE seats, all this
# chapter's (the Decalogue's "a graven image and any form", Exodus 20:4 / 5:8, recast); "figure" 4:16 and Ezekiel 8's two; "LIKENESS" (8403) ten
# seats — five in 4:16-18 (Exodus 25:9's tabernacle pattern the first); "male or female" 4:16 and Leviticus 3:6; "bird of wing" one; "that creeps
# on the ground" one; "fish" 4:18 the one seat of the form; "in the waters under the earth" three (the Decalogue's two); "lift your eyes
# heavenward" one; "the sun and the moon and the stars" one; "all the host of heaven" 4:19 and Isaiah 34:4; "and be drawn away" 4:19 and 30:17;
# "APPORTIONED" the qal perfect — 4:19 and 29:25 in the Torah (the Sifrei 148:8 reads the two together: not given to the nations for worship);
# "to all the peoples under the whole heaven" one; "the iron furnace" 4:20, 1 Kings 8:51, Jeremiah 11:4 (Ezekiel's furnace three); "a people of
# inheritance" one; "as this day" six Deuteronomy seats; "WAS ANGRY WITH ME" one — the hitpael's fourteen seats, 1:37 "for your sakes", 4:21 "ON
# YOUR ACCOUNT" (one seat of the phrase), 9:8, 9:20; "and swore that I should not cross" one; "the good land" five Deuteronomy seats (1:35, 3:25,
# 4:21, 4:22, 9:6); "for I am to die in this land" one; "I am not crossing the Jordan" one; "the covenant of the LORD your God" four; "A CONSUMING
# FIRE" 4:24 and 9:3 in the Torah (Joel's two); "a jealous God" five Torah seats (Exodus 20:5, 34:14, 4:24, 5:9, 6:15).
assert P('ונשמרתם', 'מאד', 'לנפשתיכם') == S_('Deut 4:15', 'Josh 23:11') and U('לנפשתיכם') == S_('Deut 4:15', 'Gen 9:5', 'Josh 23:11') and P('ביום', 'דבר', 'יהוה', 'אליכם') == ['Deut 4:15'] and P('פן', 'תשחתון') == ['Deut 4:16']
assert len(U('פסל', 'ופסל')) == 23 and P('פסל', 'תמונת', 'כל') == S_('Deut 4:16', 'Deut 4:23', 'Deut 4:25') and P('ועשיתם', 'לכם', 'פסל') == S_('Deut 4:16', 'Deut 4:23') and words('Exod', 20, 4)[:5] == ['לא', 'תעשה', 'לך', 'פסל', 'וכל'] and words('Deut', 5, 8)[:5] == ['לא', 'תעשה', 'לך', 'פסל', 'כל']
assert U('סמל') == S_('Deut 4:16', 'Ezek 8:3', 'Ezek 8:5') and U('תבנית') == S_('1Chr 28:11', 'Deut 4:16', 'Deut 4:17', 'Deut 4:18', 'Exod 25:9', 'Ezek 10:8', 'Ezek 8:10', 'Ezek 8:3', 'Josh 22:28', 'Ps 144:12') and sum(W4(v).count('תבנית') for v in range(1, 50)) == 5
assert P('זכר', 'או', 'נקבה') == S_('Deut 4:16', 'Lev 3:6') and P('צפור', 'כנף') == ['Deut 4:17'] and P('רמש', 'באדמה') == ['Deut 4:18'] and U('דגה') == ['Deut 4:18'] and P('במים', 'מתחת', 'לארץ') == S_('Deut 4:18', 'Deut 5:8', 'Exod 20:4') and P('תבנית', 'כל', 'בהמה') == ['Deut 4:17'] and P('אשר', 'תעוף', 'בשמים') == ['Deut 4:17']
assert P('תשא', 'עיניך', 'השמימה') == ['Deut 4:19'] and P('השמש', 'ואת', 'הירח', 'ואת', 'הכוכבים') == ['Deut 4:19'] and P('כל', 'צבא', 'השמים') == S_('Deut 4:19', 'Isa 34:4') and U('ונדחת') == S_('Deut 30:17', 'Deut 4:19')
assert [(s, x) for s, x, m in LEMT('2505 a') if m and m.startswith('HVqp3ms')] == [('2Chr 23:18', 'חלק'), ('2Chr 28:21', 'חלק'), ('Deut 4:19', 'חלק'), ('Deut 29:25', 'חלק'), ('Job 39:17', 'חלק')] and P('אשר', 'חלק', 'יהוה', 'אלהיך') == ['Deut 4:19'] and P('לכל', 'העמים', 'תחת', 'כל', 'השמים') == ['Deut 4:19'] and len(P('תחת', 'כל', 'השמים')) == 7
assert U('מכור', 'כור') == S_('1Kgs 8:51', 'Deut 4:20', 'Ezek 22:18', 'Ezek 22:20', 'Ezek 22:22', 'Jer 11:4') and PT('Deut', 4, 20, 'מכור') == ['מִכּוּר'] and P('לעם', 'נחלה') == ['Deut 4:20'] and P('להיות', 'לו', 'לעם') == S_('Deut 14:2', 'Deut 26:18', 'Deut 4:20', 'Deut 7:6') and P('כיום', 'הזה', books=('Deut',)) == S_('Deut 10:15', 'Deut 29:27', 'Deut 2:30', 'Deut 4:20', 'Deut 4:38', 'Deut 8:18') and P('ואתכם', 'לקח', 'יהוה') == ['Deut 4:20']
assert P('התאנף', 'בי') == ['Deut 4:21'] and len(LEMV('599')) == 14 and LEMV('599', T) == S_('Deut 1:37', 'Deut 4:21', 'Deut 9:20', 'Deut 9:8') and U('בגללכם') == S_('Deut 1:37', 'Mic 3:12') and P('על', 'דבריכם') == ['Deut 4:21'] and P('וישבע', 'לבלתי', 'עברי') == ['Deut 4:21'] and P('ולבלתי', 'בא', 'אל', 'הארץ', 'הטובה') == ['Deut 4:21']
assert P('הארץ', 'הטובה', books=('Deut',)) == S_('Deut 1:35', 'Deut 3:25', 'Deut 4:21', 'Deut 4:22', 'Deut 9:6') and len(P('הארץ', 'הטובה')) == 7 and P('כי', 'אנכי', 'מת') == ['Deut 4:22'] and P('אינני', 'עבר', 'את', 'הירדן') == ['Deut 4:22'] and P('ואתם', 'עברים') == ['Deut 4:22'] and len(P('נתן', 'לך', 'נחלה')) == 8
assert P('ברית', 'יהוה', 'אלהיכם') == S_('Deut 31:26', 'Deut 4:23', 'Josh 23:16', 'Josh 3:3') and P('פן', 'תשכחו', 'את', 'ברית') == ['Deut 4:23'] and P('אשר', 'כרת', 'עמכם') == ['Deut 4:23'] and P('אשר', 'צוך', 'יהוה', 'אלהיך') == S_('1Kgs 13:21', 'Deut 13:6', 'Deut 4:23')
assert P('אש', 'אכלה') == S_('Deut 4:24', 'Deut 9:3', 'Joel 1:19', 'Joel 2:5') and P('יהוה', 'אלהיך', 'אש', 'אכלה') == ['Deut 4:24'] and P('אל', 'קנא') == S_('Deut 4:24', 'Deut 5:9', 'Deut 6:15', 'Exod 20:5', 'Exod 34:14') and P('הוא', 'אל', 'קנא') == ['Deut 4:24'] and len(W4(24)) == 8

# 4:25-31 THE EXILE AND THE RETURN (computed): "when you beget sons" one; "grown old" — the hapax form of the sleep/old root; "do evil in the
# eyes of the LORD" the kings' formula (Judges and Kings fifty seats; the Torah's four — Numbers 32:13, 4:25, 9:18, 17:2, 31:29 five); "to provoke
# him" six seats, three this book's; "I CALL TO WITNESS" 4:26, 30:19, Jeremiah 42:19 — "heaven and earth" summoned at 4:26, 30:19, 31:28 (the
# Sifrei 306:1 reads the chain of witnesses: the heavens third); "you shall surely perish quickly" one — the doubled "perish" four Deuteronomy
# seats; "you shall not prolong days" 4:26 and 30:18 — the prolong-days family sixteen; "utterly destroyed" one; "scatter you among the peoples"
# one; "few in number" five seats (Genesis 34:30 Jacob's fear the first); "whither the LORD shall lead you" one; "THE WORK OF MEN'S HANDS, WOOD
# AND STONE" 4:28, 2 Kings 19:18 and Isaiah 37:19 (Hezekiah's prayer) — "wood and stone" seven; "see nor hear nor eat nor smell" one (Psalm 115's
# idols the kin); "seek the LORD from there" one; "WITH ALL YOUR HEART AND WITH ALL YOUR SOUL" seven, all this book's (6:5 the Shema's); "in
# distress to you" one; "in the end of days" thirteen seats, four Torah (Genesis 49:1, Numbers 24:14, 4:30, 31:29); "return to the LORD your God
# … and hearken to his voice" 4:30 and 30:2; "a merciful God" 4:31, Exodus 34:6, Psalm 86:15; "will not fail you" four; "the covenant of your
# fathers" one; "which he swore to them" 4:31 and Numbers 14:16.
assert P('כי', 'תוליד', 'בנים') == ['Deut 4:25'] and U('ונושנתם') == ['Deut 4:25'] and 'Deut 4:25' in LEMV('3462') and len(LEMV('3462')) == 21 and P('ונושנתם', 'בארץ') == ['Deut 4:25'] and U('והשחתם') == ['Deut 4:25']
assert P('הרע', 'בעיני', 'יהוה', books=T) == S_('Deut 17:2', 'Deut 31:29', 'Deut 4:25', 'Deut 9:18', 'Num 32:13') and len(P('הרע', 'בעיני', 'יהוה')) == 53 and U('להכעיסו') == S_('1Kgs 16:7', '2Chr 33:6', '2Kgs 17:17', 'Deut 31:29', 'Deut 4:25', 'Deut 9:18')
assert U('העידתי') == S_('Deut 30:19', 'Deut 4:26', 'Jer 42:19') and P('את', 'השמים', 'ואת', 'הארץ', books=('Deut',)) == S_('Deut 30:19', 'Deut 31:28', 'Deut 4:26') and P('העידתי', 'בכם', 'היום', 'את', 'השמים', 'ואת', 'הארץ') == S_('Deut 30:19', 'Deut 4:26') and words('Deut', 30, 19)[:7] == W4(26)[:7]
assert P('אבד', 'תאבדון', 'מהר') == ['Deut 4:26'] and P('אבד', 'תאבדון') == S_('Deut 12:2', 'Deut 30:18', 'Deut 4:26', 'Deut 8:19') and P('לא', 'תאריכן', 'ימים') == S_('Deut 30:18', 'Deut 4:26') and len(U('תאריך', 'תאריכו', 'תאריכן', 'יאריך', 'יאריכן', 'האריך')) == 16 and P('השמד', 'תשמדון') == ['Deut 4:26'] and P('מעל', 'הארץ', books=('Deut',)) == S_('Deut 11:17', 'Deut 4:26')
assert P('והפיץ', 'יהוה', 'אתכם', 'בעמים') == ['Deut 4:27'] and P('מתי', 'מספר') == S_('1Chr 16:19', 'Deut 4:27', 'Gen 34:30', 'Jer 44:28', 'Ps 105:12') and P('ינהג', 'יהוה', 'אתכם') == ['Deut 4:27'] and U('ונשארתם') == S_('Deut 28:62', 'Deut 4:27') and PT('Deut', 4, 27, 'מתי') == ['מְתֵי']
assert P('מעשה', 'ידי', 'אדם', 'עץ', 'ואבן') == S_('2Kgs 19:18', 'Deut 4:28', 'Isa 37:19') and P('עץ', 'ואבן') == S_('2Kgs 19:18', 'Deut 28:36', 'Deut 28:64', 'Deut 29:16', 'Deut 4:28', 'Ezek 20:32', 'Isa 37:19') and P('לא', 'יראון', 'ולא', 'ישמעון') == ['Deut 4:28'] and P('ועבדתם', 'שם', 'אלהים') == ['Deut 4:28'] and len(P('מעשה', 'ידי', 'אדם')) == 5
assert P('ובקשתם', 'משם') == ['Deut 4:29'] and P('בכל', 'לבבך', 'ובכל', 'נפשך') == S_('Deut 10:12', 'Deut 26:16', 'Deut 30:10', 'Deut 30:2', 'Deut 30:6', 'Deut 4:29', 'Deut 6:5') and P('כי', 'תדרשנו') == ['Deut 4:29'] and U('ומצאת') == S_('1Sam 10:2', 'Deut 4:29', 'Neh 9:8')
assert P('בצר', 'לך') == ['Deut 4:30'] and len(P('באחרית', 'הימים')) == 13 and P('באחרית', 'הימים', books=T) == S_('Deut 31:29', 'Deut 4:30', 'Gen 49:1', 'Num 24:14') and P('ושבת', 'עד', 'יהוה', 'אלהיך') == S_('Deut 30:2', 'Deut 4:30') and P('ושמעת', 'בקלו') == S_('Deut 30:2', 'Deut 4:30') and P('ומצאוך', 'כל', 'הדברים', 'האלה') == ['Deut 4:30']
assert P('אל', 'רחום') == S_('Deut 4:31', 'Exod 34:6', 'Ps 86:15') and U('ירפך') == S_('1Chr 28:20', 'Deut 31:6', 'Deut 31:8', 'Deut 4:31') and P('ברית', 'אבתיך') == ['Deut 4:31'] and P('אשר', 'נשבע', 'להם') == S_('Deut 4:31', 'Num 14:16') and P('לא', 'ירפך', 'ולא', 'ישחיתך') == ['Deut 4:31']

# 4:32-40 THE ONE GOD (computed): "ask now of the former days" one; "since the day God created man" one — the create-root's eleven Torah seats,
# this the book's ONE (Genesis's nine and Exodus 34:10, Numbers 16:30); "from the end of heaven to the end of heaven" one; "has it been heard like
# it" one; "has a people heard the voice of God" one; "voice of God speaking from the midst of the fire" one; "AND LIVED" 4:33 and 5:26 (the
# wayyiqtol of the live-root, Genesis 5's and 11's rhythm); "has God assayed" one; "a nation from the midst of a nation" one; "by trials" the noun's
# three seats, all this book's (4:34, 7:19, 29:2); "signs and wonders" the pair's twenty-three seats — 4:34's "by signs and by wonders" one; "A
# MIGHTY HAND AND AN OUTSTRETCHED ARM" 4:34, 5:15, 26:8, 1 Kings 8:42, Ezekiel 20:33-34, Psalm 136:12 (the mighty hand's sixteen); "and by great
# terrors" 4:34 and Jeremiah 32:21 (26:8's singular "great terror"); "YOU WERE SHOWN TO KNOW" one — the hophal, against 4:3's participle "that
# saw"; "THE LORD HE IS GOD" 4:35, 4:39 in the Torah, Elijah's and Solomon's outside; "there is none else" six, "none beside him" one; "out of
# heaven he made you hear his voice" one; "to instruct you" one; "his great fire" one; "because he loved your fathers" one; "and chose his seed
# after him" one — "his seed after him" Abraham's phrase (Genesis 17:7, 9, 10, 48:4); "with his presence" 4:37 (the store: "in-face-him/its");
# "with his great power" one; "to drive out nations greater and mightier" 4:38 and 9:1; "know this day and lay it to your heart" one; "in heaven
# above and on the earth beneath" 4:39, Joshua 2:11 (Rahab), 1 Kings 8:23 (Solomon); "his statutes and his commandments" one; "that it may go well
# with you" 4:40, 6:3, Ruth 3:1; "prolong days on the ground" one; "which I command you this day" eighteen Deuteronomy seats; "all the days" closes.
assert P('שאל', 'נא', 'לימים') == ['Deut 4:32'] and P('לימים', 'ראשנים') == ['Deut 4:32'] and P('אשר', 'ברא', 'אלהים', 'אדם') == ['Deut 4:32'] and LEMV('1254 a', T) == S_('Deut 4:32', 'Exod 34:10', 'Gen 1:1', 'Gen 1:21', 'Gen 1:27', 'Gen 2:3', 'Gen 2:4', 'Gen 5:1', 'Gen 5:2', 'Gen 6:7', 'Num 16:30') and P('אדם', 'על', 'הארץ') == ['Deut 4:32']
assert P('השמים', 'ועד', 'קצה', 'השמים') == ['Deut 4:32'] and P('הנשמע', 'כמהו') == ['Deut 4:32'] and P('כדבר', 'הגדול', 'הזה') == ['Deut 4:32'] and morphs('Deut', 4, 32)[21] == 'HTi/VNp3ms' and morphs('Deut', 4, 32)[26] == 'HTi/VNp3ms' and PT('Deut', 4, 32, 'הנהיה') == ['הֲנִֽהְיָה']
assert P('השמע', 'עם', 'קול', 'אלהים') == ['Deut 4:33'] and P('קול', 'אלהים', 'מדבר', 'מתוך', 'האש') == ['Deut 4:33'] and P('כאשר', 'שמעת', 'אתה') == ['Deut 4:33'] and [(s, x) for s, x, m in LEMT('2421', ('Deut',)) if m == 'HC/Vqw3ms'] == [('Deut 4:33', 'ויחי'), ('Deut 5:26', 'ויחי')] and words('Deut', 5, 26)[-1] == 'ויחי'
assert P('הנסה', 'אלהים') == ['Deut 4:34'] and P('גוי', 'מקרב', 'גוי') == ['Deut 4:34'] and P('לבוא', 'לקחת', 'לו', 'גוי') == ['Deut 4:34'] and LEMV('4531 b') == S_('Deut 29:2', 'Deut 4:34', 'Deut 7:19', 'Ps 95:8') and P('במסת', 'באתת', 'ובמופתים') == ['Deut 4:34'] and len(hits('מופת')) == 23
assert P('וביד', 'חזקה', 'ובזרוע', 'נטויה') == ['Deut 4:34'] and len(sorted(set(P('ביד', 'חזקה')) | set(P('וביד', 'חזקה')) | set(P('יד', 'חזקה')))) == 16 and sorted(set(P('ובזרוע', 'נטויה')) | set(P('ובזרע', 'נטויה')) | set(P('בזרוע', 'נטויה')) | set(P('בזרע', 'נטויה')) | set(P('זרוע', 'נטויה'))) == S_('2Kgs 17:36', 'Deut 26:8', 'Deut 4:34', 'Deut 5:15', 'Exod 6:6', 'Ezek 20:33', 'Ezek 20:34', 'Ps 136:12')
assert P('ובמוראים', 'גדלים') == ['Deut 4:34'] and sorted(set(P('ובמוראים', 'גדלים')) | set(P('ובמורא', 'גדל')) | set(P('ובמורא', 'גדול'))) == S_('Deut 4:34', 'Jer 32:21') and words('Deut', 26, 8)[-6:] == ['ובזרע', 'נטויה', 'ובמרא', 'גדל', 'ובאתות', 'ובמפתים'] and P('ככל', 'אשר', 'עשה', 'לכם', 'יהוה', 'אלהיכם') == ['Deut 4:34'] and P('במצרים', 'לעיניך') == ['Deut 4:34']
assert P('אתה', 'הראת', 'לדעת') == ['Deut 4:35'] and P('יהוה', 'הוא', 'האלהים') == S_('1Kgs 18:39', '1Kgs 8:60', '2Chr 33:13', 'Deut 4:35', 'Deut 4:39') and P('אין', 'עוד') == S_('1Kgs 8:60', '2Kgs 4:6', 'Deut 4:35', 'Deut 4:39', 'Jer 48:2', 'Ps 74:9') and P('אין', 'עוד', 'מלבדו') == ['Deut 4:35'] and U('מלבדו') == ['Deut 4:35']
assert P('מן', 'השמים', 'השמיעך') == ['Deut 4:36'] and U('ליסרך') == ['Deut 4:36'] and P('אשו', 'הגדולה') == ['Deut 4:36'] and P('ודבריו', 'שמעת') == ['Deut 4:36'] and P('ועל', 'הארץ', 'הראך') == ['Deut 4:36'] and words('Exod', 20, 22)[-5:] == ['כי', 'מן', 'השמים', 'דברתי', 'עמכם']
assert P('ותחת', 'כי', 'אהב') == ['Deut 4:37'] and P('ויבחר', 'בזרעו', 'אחריו') == ['Deut 4:37'] and sorted(set(P('זרעו', 'אחריו')) | set(P('בזרעו', 'אחריו')) | set(P('זרעך', 'אחריך')) | set(P('וזרעך', 'אחריך')) | set(P('לזרעך', 'אחריך')) | set(P('בזרעם', 'אחריהם')) | set(P('זרעם', 'אחריהם'))) == S_('1Chr 17:11', '2Sam 7:12', 'Deut 10:15', 'Deut 4:37', 'Gen 17:10', 'Gen 17:7', 'Gen 17:9', 'Gen 48:4')
assert U('בפניו') == S_('Deut 25:9', 'Deut 4:37', 'Hos 5:5', 'Hos 7:10', 'Prov 21:29') and PT('Deut', 4, 37, 'בפניו') == ['בְּפָנָיו'] and sg(4, 37, 'בפניו') == 'in-face-him/its' and P('בכחו', 'הגדל') == ['Deut 4:37'] and P('ויוצאך', 'בפניו') == ['Deut 4:37'] and len(U('אבתיך', books=('Deut',))) == 12
assert P('גוים', 'גדלים', 'ועצמים', 'ממך') == S_('Deut 4:38', 'Deut 9:1') and P('גדלים', 'ועצמים') == S_('Deut 11:23', 'Deut 4:38', 'Deut 9:1') and U('להביאך') == ['Deut 4:38'] and P('לתת', 'לך', 'את', 'ארצם', 'נחלה') == ['Deut 4:38'] and U('ארצם', books=('Deut',)) == S_('Deut 19:1', 'Deut 29:7', 'Deut 4:38', 'Deut 9:5')
assert P('וידעת', 'היום', 'והשבת', 'אל', 'לבבך') == ['Deut 4:39'] and P('וידעת', 'היום') == S_('Deut 4:39', 'Deut 9:3') and P('והשבת', 'אל', 'לבבך') == S_('Deut 30:1', 'Deut 4:39') and P('בשמים', 'ממעל', 'ועל', 'הארץ', 'מתחת') == S_('1Kgs 8:23', 'Deut 4:39', 'Josh 2:11') and P('בשמים', 'ממעל') == S_('1Kgs 8:23', 'Deut 4:39', 'Deut 5:8', 'Exod 20:4', 'Josh 2:11')
assert P('חקיו', 'ואת', 'מצותיו') == ['Deut 4:40'] and P('אשר', 'ייטב', 'לך') == S_('Deut 4:40', 'Deut 6:3', 'Ruth 3:1') and len(P('ייטב', 'לך')) == 9 and P('תאריך', 'ימים', 'על', 'האדמה') == ['Deut 4:40'] and len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))) == 18 and P('ולבניך', 'אחריך') == S_('Deut 12:25', 'Deut 12:28', 'Deut 4:40')
assert P('על', 'האדמה', 'אשר', 'יהוה', 'אלהיך', 'נתן', 'לך') == S_('Deut 25:15', 'Deut 4:40', 'Deut 5:16', 'Exod 20:12') and [v for v in range(1, 50) if W4(v)[-2:] == ['כל', 'הימים']] == [40] and len(P('כל', 'הימים', books=('Deut',))) == 12

# 4:41-43 THE THREE CITIES (computed): "THEN MOSES SET APART" one — "then" with the imperfect the Song's form (Exodus 15:1 "then sang", Numbers
# 21:17), fourteen Torah "then"s; the set-apart root twenty-one Torah seats (Genesis 1's four the first, the refuge law's 19:2, 7); "THREE CITIES"
# 4:41, 19:7, 19:9 and Amos 4:8 — Numbers 35:14's "THE three cities" with the article the one seat (the refuge runner's THREE_CITIES census);
# "beyond the Jordan toward the sunrise" one — "toward the sunrise" 4:41 and 4:47 in the Torah; "that the manslayer might flee there" one — "to flee
# there" 4:42 and Numbers 35:6; "manslayer" (7523) twenty-eight seats, Numbers 35's sixteen; "UNAWARES" 4:42, 19:4, Joshua 20:3, 5, Job 35:16;
# "and he hated him not" 4:42 and 19:4 — "in time past" seven seats (Exodus 21:29's ox); "and flee to one of these cities and live" one — "and live"
# the refuge's word (19:4, 5) and the serpent's (Numbers 21:8, 9); "these" the short form twelve Torah seats; BEZER, RAMOTH, GOLAN — 4:43, Joshua
# 20:8, 21:27-38, 1 Chronicles 6 (Golan four seats; Joshua 20:8 spells it "Gaulon"); "in the wilderness in the table-land" one — "the table-land"
# 3:10 and 4:43 in the Torah; "to the Reubenites" nine, "to the Gadites" and "to the Manassites" the gentilic datives ONE SEAT EACH.
assert P('אז', 'יבדיל') == ['Deut 4:41'] and len(U('אז', books=T)) == 14 and [(s, ws[i + 1][0]) for (b, c, v), ws in by.items() if b in T for i, (x, m) in enumerate(ws) if x == 'אז' and i + 1 < len(ws) and ws[i + 1][1] and ws[i + 1][1][:4] in ('HVqi', 'HVhi') for s in [f'{b} {c}:{v}']] == [('Deut 4:41', 'יבדיל'), ('Deut 29:19', 'יעשן'), ('Exod 15:1', 'ישיר'), ('Lev 26:34', 'תרצה'), ('Lev 26:34', 'תשבת'), ('Num 21:17', 'ישיר')]   # the DB's verse order is alphabetical by book
assert len(LEMV('914', T)) == 21 and LEMV('914', ('Deut',)) == S_('Deut 10:8', 'Deut 19:2', 'Deut 19:7', 'Deut 29:20', 'Deut 4:41') and P('שלש', 'ערים') == S_('Amos 4:8', 'Deut 19:7', 'Deut 19:9', 'Deut 4:41') and P('שלש', 'הערים') == ['Num 35:14']
assert P('בעבר', 'הירדן', 'מזרחה', 'שמש') == ['Deut 4:41'] and sorted(set(P('מזרחה', 'שמש', books=T)) | set(P('מזרח', 'שמש', books=T))) == S_('Deut 4:41', 'Deut 4:47') and len(P('בעבר', 'הירדן', books=('Deut',))) == 9
assert P('לנס', 'שמה', 'רוצח') == ['Deut 4:42'] and P('לנס', 'שמה') == S_('Deut 4:42', 'Num 35:6') and len(U('רוצח', 'רצח', 'הרצח', 'הרוצח')) == 28 and len([s for s in U('רוצח', 'רצח', 'הרצח', 'הרוצח') if s.startswith('Num 35')]) == 14 and PT('Deut', 4, 42, 'רוצח') == ['רוֹצֵחַ']
assert P('בבלי', 'דעת') == S_('Deut 19:4', 'Deut 4:42', 'Job 35:16', 'Josh 20:3', 'Josh 20:5') and P('והוא', 'לא', 'שנא', 'לו') == S_('Deut 19:4', 'Deut 4:42') and sorted(set(P('מתמול', 'שלשום')) | set(P('מתמל', 'שלשם')) | set(P('תמול', 'שלשום')) | set(P('תמל', 'שלשם'))) == S_('Deut 19:4', 'Deut 19:6', 'Deut 4:42', 'Exod 21:29', 'Josh 20:5', 'Josh 3:4', 'Ruth 2:11')
assert P('ונס', 'אל', 'אחת', 'מן', 'הערים') == ['Deut 4:42'] and sorted(set(P('אחת', 'מן', 'הערים')) | set(P('אחת', 'הערים'))) == S_('Deut 19:11', 'Deut 19:5', 'Deut 4:42') and U('וחי', books=('Deut', 'Num')) == S_('Deut 19:4', 'Deut 19:5', 'Deut 4:42', 'Deut 5:24', 'Num 21:8', 'Num 21:9') and len(U('האל', books=T)) == 12 and PT('Deut', 4, 42, 'האל') == ['הָאֵל']
assert U('גולן', 'גלון') == S_('1Chr 6:56', 'Deut 4:43', 'Josh 20:8', 'Josh 21:27') and 'Deut 4:43' in U('בצר') and 'Josh 20:8' in U('בצר') and 'Deut 4:43' in U('ראמת') and words('Josh', 20, 8)[17] == 'גלון' and W4(43)[11] == 'גולן' and PT('Deut', 4, 43, 'גולן') == ['גּוֹלָן'] and PT('Deut', 4, 43, 'ראמת') == ['רָאמֹת']
assert P('במדבר', 'בארץ', 'המישר') == ['Deut 4:43'] and U('המישר', books=T) == S_('Deut 3:10', 'Deut 4:43') and U('לראובני') == S_('1Chr 11:42', '1Chr 27:16', '1Chr 5:26', '1Chr 5:6', 'Deut 29:7', 'Deut 3:12', 'Deut 4:43', 'Josh 12:6', 'Josh 22:1') and U('לגדי') == ['Deut 4:43'] and U('למנשי') == ['Deut 4:43'] and U('בגלעד', books=T) == ['Deut 4:43'] and U('בבשן', books=T) == S_('Deut 3:10', 'Deut 3:4', 'Deut 4:43')
assert SHARED(('Deut', 4, 43), ('Josh', 20, 8)) == ['את', 'בצר', 'במדבר'] and DIFF(('Deut', 4, 42), ('Deut', 19, 4))[2:4] == [('replace', ['ירצח'], ['יכה']), ('replace', ['מתמול', 'שלשום', 'ונס', 'אל', 'אחת', 'מן', 'הערים', 'האל', 'וחי'], ['מתמל', 'שלשם'])] and SHARED(('Deut', 4, 42), ('Deut', 19, 4)) == ['את', 'רעהו', 'בבלי', 'דעת', 'והוא', 'לא', 'שנא', 'לו']

# 4:44-49 THE FRAME (computed): "AND THIS IS THE TORAH" one seat; "which Moses set before" one — "set before" the verb's seats are offerings and
# service (12:7, 14:26, 18:7), the Torah "set" here alone; "before the children of Israel" 4:44 the book's one seat of the form; "THESE ARE THE
# TESTIMONIES" one — "the testimonies and the statutes and the judgments" 4:45 and 6:20 (the son's question); the testimonies-word (5713 b) three
# Torah seats (4:45, 6:17, 6:20) and Psalms' nineteen; "which Moses spoke to the children of Israel" one — "which Moses spoke" 1:1 and 4:45 (THE
# TWO FRAMES: 1:1 "these are the words … to all Israel beyond the Jordan", 4:45 "these are the testimonies … to the children of Israel when they
# came out of Egypt"); "when they came out of Egypt" 4:45, 4:46, Joshua 5:4, 5, 2 Chronicles 5:10; "in the valley opposite Beth-peor" 3:29 and
# 4:46 — the valley named at 3:29, 4:46 and the grave's 34:6; "Sihon king of the Amorites who dwelt in Heshbon" 1:4 and 4:46 (Sihon DEFECTIVE
# here as at 1:4 and the whole speech but 2:26); "whom Moses smote" 4:46 and Joshua 13:21; "Moses and the children of Israel" the subject pair
# 4:46, Exodus 15:1 (the Song), Numbers 26:4; "and they possessed his land" 4:47 and Numbers 21:35; "the land of Og" 4:47 and Nehemiah 9:22; "the
# two kings of the Amorites" 3:8, 4:47, Joshua 24:12; "from Aroer on the bank of the valley of Arnon" 2:36 and 4:48 verbatim; "MOUNT SION" one —
# SION the fourth name (3:9's Sirion and Senir, Hermon; the Sifrei 37:9's four kingdoms); "all the Arabah" 4:49 and Joshua 12:1; "the sea of the
# Arabah" five (3:17 "the sea of the Arabah, the Salt Sea"); "the slopes of Pisgah" 3:17 and 4:49; "under the slopes" the two.
assert P('וזאת', 'התורה') == ['Deut 4:44'] and P('אשר', 'שם', 'משה', 'לפני') == ['Deut 4:44'] and P('שם', 'לפני', books=('Deut',)) == S_('Deut 12:7', 'Deut 14:26', 'Deut 18:7') and P('לפני', 'בני', 'ישראל', books=('Deut',)) == ['Deut 4:44'] and P('התורה', 'אשר', 'שם', 'משה') == ['Deut 4:44']
assert P('אלה', 'העדת') == ['Deut 4:45'] and P('העדת', 'והחקים', 'והמשפטים') == S_('Deut 4:45', 'Deut 6:20') and LEMV('5713 b', T) == S_('Deut 4:45', 'Deut 6:17', 'Deut 6:20') and len(LEMV('5713 b')) == 22 and PT('Deut', 4, 45, 'העדת') == ['הָֽעֵדֹת'] and sg(4, 45, 'העדת') == 'the-testimony'
assert P('אשר', 'דבר', 'משה', 'אל', 'בני', 'ישראל') == ['Deut 4:45'] and P('אשר', 'דבר', 'משה') == S_('Deut 1:1', 'Deut 4:45') and SHARED(('Deut', 4, 45), ('Deut', 1, 1)) == ['אשר', 'דבר', 'משה', 'אל'] and P('בצאתם', 'ממצרים') == S_('2Chr 5:10', 'Deut 4:45', 'Deut 4:46', 'Josh 5:4', 'Josh 5:5')
assert P('בגיא', 'מול', 'בית', 'פעור') == S_('Deut 3:29', 'Deut 4:46') and P('סיחן', 'מלך', 'האמרי', 'אשר', 'יושב', 'בחשבון') == S_('Deut 1:4', 'Deut 4:46') and P('סיחן', 'מלך', 'האמרי') == S_('Deut 1:4', 'Deut 4:46', 'Num 21:21', 'Num 21:26', 'Num 32:33') and U('סיחון', books=('Deut',)) == ['Deut 2:26'] and U('לסיחון', books=('Deut',)) == ['Deut 31:4'] and 'Deut 4:46' in U('סיחן')
assert P('אשר', 'הכה', 'משה') == S_('Deut 4:46', 'Josh 13:21') and P('משה', 'ובני', 'ישראל') == S_('Deut 4:46', 'Exod 15:1', 'Num 26:4') and P('בארץ', 'סיחן') == ['Deut 4:46'] and SHARED(('Deut', 4, 46), ('Deut', 1, 4)) == ['סיחן', 'מלך', 'האמרי', 'אשר', 'יושב', 'בחשבון']
assert P('ויירשו', 'את', 'ארצו') == S_('Deut 4:47', 'Num 21:35') and P('ארץ', 'עוג') == S_('Deut 4:47', 'Neh 9:22') and P('שני', 'מלכי', 'האמרי') == S_('Deut 3:8', 'Deut 4:47', 'Josh 24:12') and P('עוג', 'מלך', 'הבשן') == S_('Deut 1:4', 'Deut 3:1', 'Deut 3:11', 'Deut 3:3', 'Deut 4:47', 'Josh 12:4', 'Josh 13:30', 'Neh 9:22', 'Num 21:33', 'Num 32:33') and SHARED(('Deut', 4, 47), ('Deut', 3, 8)) == ['שני', 'מלכי', 'האמרי', 'אשר', 'בעבר', 'הירדן']
assert P('מערער', 'אשר', 'על', 'שפת', 'נחל', 'ארנן') == S_('Deut 2:36', 'Deut 4:48') and len(U('ערער', 'מערער', 'וערער', 'ערוער', 'בערער', 'ומערער')) == 11 and P('הר', 'שיאן') == ['Deut 4:48'] and U('שיאן') == ['Deut 4:48'] and U('שרין', 'שריון') == S_('1Sam 17:38', 'Dan 3:25', 'Deut 3:9') and U('שניר', 'ושניר') == S_('1Chr 5:23', 'Deut 3:9', 'Song 4:8') and len(U('חרמון', 'וחרמון')) == 13 and PT('Deut', 4, 48, 'שיאן') == ['שִׂיאֹן'] and P('הוא', 'חרמון') == ['Deut 4:48']
assert sorted(set(P('וכל', 'הערבה')) | set(P('כל', 'הערבה'))) == S_('Deut 4:49', 'Josh 12:1') and P('עבר', 'הירדן', 'מזרחה') == S_('Deut 4:49', 'Josh 13:27') and P('ים', 'הערבה') == S_('2Kgs 14:25', 'Deut 3:17', 'Deut 4:49', 'Josh 12:3', 'Josh 3:16') and P('אשדת', 'הפסגה') == S_('Deut 3:17', 'Deut 4:49') and P('תחת', 'אשדת') == S_('Deut 3:17', 'Deut 4:49') and U('אשדת', 'האשדות', 'אשדות', 'ואשדות') == S_('Deut 33:2', 'Deut 3:17', 'Deut 4:49', 'Josh 12:3', 'Josh 13:20') and len(U('הפסגה', 'פסגה')) == 8
assert words('Deut', 3, 17)[4:7] == ['ועד', 'ים', 'הערבה'] and words('Deut', 3, 17)[7:9] == ['ים', 'המלח'] and PT('Deut', 4, 49, 'אשדת') == ['אַשְׁדֹּת'] and words('Josh', 12, 3)[-2:] == ['אשדות', 'הפסגה']

# THE RETELLINGS DIFFED (computed): 4:3 against Numbers 25:3, 5 shares the name alone; 4:11 against Exodus 19:17-18 shares "the mountain"; 4:12
# against 5:4 — "the LORD spoke to you from the midst of the fire" the kept words (5:4 adds "face to face … in the mountain"); 4:13 against 5:22 —
# "and wrote them on two tablets of stone" kept, the tablets PLENE here and DEFECTIVE there; 4:16 against the Decalogue — "a graven image" kept,
# "the form of any figure, the likeness of male or female" for "and any form that is in heaven above"; 4:21 against 1:37 — "was angry" kept,
# "for your sakes" become "on your account"; against 3:26 — the wrath-verb changes (the hitpael of anger for the hitpael of crossing); 4:26
# against 30:19 the first seven words identical; 4:33 against 5:26 — "the voice of God speaking from the midst of the fire … and lived" kept,
# "a people" for "all flesh"; 4:34 against 26:8 — the mighty hand and the outstretched arm kept, the arm PLENE here and DEFECTIVE there; 4:35
# against 4:39 — "the LORD he is God … there is none else" kept twice; 4:38 against 9:1 — "nations greater and mightier than you" kept; 4:41 against
# Numbers 35:14 — "three" kept, Moses' act for the law's "you shall give"; 4:42 against 19:4 — "his neighbor unawares and he hated him not" kept,
# "slays" here for "smites" there, the tail "and flee to one of these cities and live" the ACT's; 4:43 against Joshua 20:8 — the three names kept,
# the tribes' datives become "of the tribe of"; 4:45 against 6:20 — "the testimonies and the statutes and the judgments which" kept; 4:46 against
# 1:4 — "Sihon king of the Amorites who dwelt in Heshbon" kept whole; 4:47 against 3:8 — "the two kings of the Amorites who were beyond the
# Jordan" kept; 4:48 against 2:36 — "from Aroer on the bank of the valley of Arnon" kept whole; 4:49 against 3:17 — "the sea of the Arabah" and
# "under the slopes of Pisgah" kept, "the Salt Sea" dropped.
assert SHARED(('Deut', 4, 12), ('Deut', 5, 4)) == ['מתוך', 'האש'] and SHARED(('Deut', 4, 13), ('Deut', 5, 22)) == ['ויכתבם', 'על', 'שני'] and DIFF(('Deut', 4, 13), ('Deut', 5, 22))[-2:] == [('replace', ['לחות'], ['לחת']), ('insert', [], ['ויתנם', 'אלי'])]
assert SHARED(('Deut', 4, 21), ('Deut', 1, 37)) == ['התאנף'] and DIFF(('Deut', 4, 21), ('Deut', 3, 26))[0] == ('replace', ['ויהוה', 'התאנף'], ['ויתעבר', 'יהוה']) and SHARED(('Deut', 4, 33), ('Deut', 5, 26)) == ['מדבר', 'מתוך', 'האש'] and DIFF(('Deut', 4, 33), ('Deut', 5, 26))[1] == ('insert', [], ['חיים'])
assert DIFF(('Deut', 4, 34), ('Deut', 26, 8))[1] == ('replace', ['ובזרוע'], ['ובזרע']) and SHARED(('Deut', 4, 35), ('Deut', 4, 39)) == ['כי', 'יהוה', 'הוא', 'האלהים'] and SHARED(('Deut', 4, 38), ('Deut', 9, 1)) == ['גוים', 'גדלים', 'ועצמים', 'ממך'] and SHARED(('Deut', 4, 41), ('Num', 35, 14)) == ['שלש']
assert SHARED(('Deut', 4, 45), ('Deut', 6, 20)) == ['העדת', 'והחקים', 'והמשפטים', 'אשר'] and SHARED(('Deut', 4, 48), ('Deut', 2, 36)) == ['מערער', 'אשר', 'על', 'שפת', 'נחל', 'ארנן'] and SHARED(('Deut', 4, 49), ('Deut', 3, 17)) == ['ועד', 'ים', 'הערבה'] and DIFF(('Deut', 4, 49), ('Deut', 3, 17))[1] == ('insert', [], ['ים', 'המלח'])
assert SHARED(('Deut', 4, 3), ('Num', 25, 3)) == ['יהוה'] and SHARED(('Deut', 4, 3), ('Num', 25, 5)) == ['פעור'] and SHARED(('Deut', 4, 11), ('Exod', 19, 17)) == ['ההר'] and SHARED(('Deut', 4, 16), ('Exod', 20, 4)) == ['פסל'] and SHARED(('Deut', 4, 26), ('Deut', 30, 19)) == W4(26)[:7]

# ONKELOS CHAPTER 4 — THE RENDERINGS' SEATS over the whole book (computed on the plain Aramaic of every verse): "the FEAR of the LORD" supplied at
# 4:4 ("you who cleave to the fear of the LORD"), 4:20 ("drew you near to his fear"), 4:29 ("seek the fear of the LORD"), 4:30 ("return to the fear
# of the LORD") — the phrase's twelve seats in the book; THE MEMRA at 4:24 ("the LORD your God, HIS MEMRA is a consuming fire" — the same form 20:1),
# 4:33 ("the voice of the Memra of the LORD" — four seats), 4:36 ("the voice of his Memra" — 4:36 and 5:21), 4:37 ("brought you out BY HIS MEMRA"
# for "with his presence"), 4:30 ("receive his Memra"); 4:7 "TO RECEIVE ITS PRAYER IN THE TIME OF ITS DISTRESS … whenever WE PRAY BEFORE HIM" —
# the translation's supplied clause (one seat of each phrase); 4:11 "at the foot of the mountain" (one seat), "to the height of heaven" (three:
# 1:28, 4:11, 9:1); 4:12 "and no likeness — you saw none, only a voice"; 4:17 "IN THE AIR OF THE FIRMAMENT OF HEAVEN" supplied (one seat); 4:19
# "which the LORD PREPARED for all the peoples" (one seat — "apportioned" made "prepared"; the Sifrei 148:8's question answered by the translation);
# 4:28 "and you shall serve there THE PEOPLES WHO SERVE IDOLS" — Israel made to serve the idolaters, not the idols (the same clause 28:36, 28:64);
# 4:34 "OR THE MIRACLES WHICH THE LORD DID TO REVEAL HIMSELF, to redeem for himself a people" — the question "has any god tried" made a statement
# (one seat of each phrase); 4:35 "there is none beside him" (one); 4:39 "GOD WHOSE SHEKHINAH IS IN THE HEAVENS ABOVE AND WHO RULES ON THE EARTH
# BENEATH" — 3:24's confession repeated (the Shekhinah clause three seats: 4:39, 33:16, 33:26; "and rules" 3:24 and 4:39); 4:41 "THEN Moses set
# apart" (2 seats of "then"); 4:42 "the slayer" four seats (19:3, 4, 6), "without knowledge" 4:42 and 19:4, "from yesterday and before it" 4:42, 19:4,
# 19:6; 4:43 "TO THE TRIBE OF" Reuben / Gad / Manasseh supplied (Manasseh's one seat); 4:44 "which Moses SET IN ORDER" (one seat); 4:45 "the
# testimonies" three; 4:47 Bashan MATNAN eight seats; 4:48 "the bank" 2:36, 2:37, 4:48; 4:49 "the sea of the plain" and "the slopes of the height"
# 3:17 and 4:49.
ONK4 = {'וכען': [(4, 1), (5, 22), (10, 12), (10, 22), (26, 10), (31, 19)], 'מאלף': [(4, 1), (8, 5)], 'תוספון': [(4, 2), (13, 1), (17, 16)], 'תמנעון': [(4, 2), (13, 1)], 'בדחלתא': [(4, 4), (18, 13)], 'דאלפית': [(4, 5)], 'לקבלא': [(4, 7), (10, 17), (17, 12), (23, 6), (30, 20)], 'צלותיה': [(4, 7), (33, 7)], 'בעדן': [(4, 7)], 'עקתיה': [(4, 7)], 'מצלין': [(4, 7)], 'קשיטין': [(4, 8)], 'אסתמר': [(4, 9), (6, 12), (8, 11), (12, 13), (12, 19), (12, 30), (15, 9), (24, 8)], 'תנשי': [(4, 9), (6, 12), (8, 19), (9, 7)], 'כנוש': [(4, 10), (31, 12)], 'למדחל': [(4, 10), (5, 26), (6, 24), (10, 12), (14, 23), (17, 19), (28, 58), (31, 13)], 'בשפולי': [(4, 11)], 'צית': [(1, 28), (4, 11), (9, 1)], 'ואמיטתא': [(4, 11), (5, 19)], 'ודמות': [(4, 12)], 'וחוי': [(4, 13)], 'לוחי': [(4, 13), (5, 19), (9, 9), (9, 10), (9, 11), (9, 15), (10, 1), (10, 3)], 'תחבלון': [(4, 16), (31, 29)], 'צלם': [(4, 16), (4, 23), (4, 25), (5, 8), (27, 15)], 'צורא': [(4, 16)], 'באור': [(4, 17)], 'רקיע': [(4, 17)], 'נוני': [(4, 18)], 'תזקוף': [(4, 19)], 'סיהרא': [(4, 19)], 'זמין': [(4, 19)], 'לדחלתיה': [(4, 20), (11, 22), (30, 20)], 'מכורא': [(4, 20)], 'דפרזלא': [(3, 11), (4, 20)], 'רגז': [(1, 37), (3, 26), (4, 21), (9, 8), (9, 19), (9, 20), (29, 27)], 'מאית': [(4, 22)], 'אשא': [(4, 24), (9, 3)], 'אכלא': [(4, 24), (9, 3)], 'ותתעתקון': [(4, 25)], 'אסהדית': [(4, 26), (8, 19), (30, 19)], 'אשתצאה': [(4, 26)], 'ויבדר': [(4, 27)], 'דמנין': [(4, 27)], 'לעממיא': [(4, 28), (28, 36), (28, 64)], 'טעותא': [(4, 28), (28, 36), (28, 64)], 'ייעוק': [(4, 30)], 'רחמנא': [(4, 31)], 'קדמאי': [(4, 32), (10, 2), (19, 14)], 'ההוה': [(4, 32)], 'האשתמע': [(4, 32)], 'ויתקים': [(4, 33), (4, 42), (5, 21), (19, 4), (19, 5)], 'נסין': [(4, 34), (7, 19), (16, 1)], 'לאתגלאה': [(4, 34)], 'למפרק': [(4, 34), (20, 4)], 'ובחזונין': [(4, 34)], 'אתחזיתא': [(4, 35)], 'לאלפותך': [(4, 36)], 'וחלף': [(4, 37)], 'רחים': [(4, 37)], 'ואתרעי': [(4, 37), (7, 7), (10, 15)], 'לתרכא': [(4, 38), (12, 29)], 'דשכנתיה': [(4, 39), (33, 16), (33, 26)], 'ושליט': [(3, 24), (4, 39)], 'בכן': [(4, 41), (29, 19)], 'תלת': [(4, 41), (14, 28), (16, 16), (19, 2), (19, 7), (19, 9)], 'קטולא': [(4, 42), (19, 3), (19, 4), (19, 6)], 'מנדעי': [(4, 42)], 'לשבטא': [(1, 23), (3, 12), (4, 43), (29, 7)], 'סדר': [(4, 44)], 'סהדותא': [(4, 45), (5, 17), (6, 20)], 'במפקהון': [(4, 45), (4, 46)], 'בחילתא': [(3, 29), (4, 46), (34, 6)], 'ויריתו': [(4, 47)], 'דמתנן': [(1, 4), (3, 1), (3, 3), (3, 10), (3, 11), (3, 13), (4, 47), (29, 6)], 'כיף': [(2, 36), (2, 37), (4, 48)], 'משפך': [(3, 17), (4, 49)], 'מרמתא': [(3, 17), (4, 49)]}
assert all(onk_tok(t) == s for t, s in ONK4.items()), [t for t, s in ONK4.items() if onk_tok(t) != s]
ONK4P = {'דחלתא דיי': 12, 'בדחלתא דיי אלהכון קימין': 1, 'קריב יי לדחלתיה': 1, 'ותתבעון מתמן דחלתא דיי': 1, 'ותתוב לדחלתא דיי': 2, 'ארי יי אלהך מימריה אשא אכלא': 1, 'ארי יי אלהך מימריה': 2, 'קל מימרא דיי': 4, 'ית קל מימריה': 2, 'ואפקך במימריה': 1, 'ותקבל למימריה': 2, 'לקבלא צלותיה בעדן עקתיה': 1, 'כל עדן דאנחנא מצלין קדמוהי': 1, 'עד צית שמיא': 3, 'ודמות ליתיכון חזן': 1, 'באור רקיע שמיא': 1, 'ותפלחנון די זמין יי': 1, 'לעממיא פלחי טעותא': 3, 'נסין די עבד יי': 1, 'לאתגלאה למפרק ליה עם': 1, 'לית עוד בר מניה': 1, 'לית עוד': 2, 'אלהא דשכנתיה': 1, 'דשכנתיה בשמיא מלעלא': 1, 'ושליט על ארעא מלרע': 1, 'בכן יפרש משה': 1, 'תלת קרוין': 4, 'בלא מנדעי': 2, 'מאתמלי ומדקמוהי': 2, 'לשבטא דמנשה': 1, 'לשבטא דראובן': 4, 'די סדר משה': 1, 'תרין מלכי': 3, 'ימא דמישרא': 2, 'משפך מרמתא': 2, 'מכורא דפרזלא': 1, 'לחוד עם חכים וסוכלתן': 1, 'מן קדם יי': 14}
assert all(len(onk_seats(k)) == n for k, n in ONK4P.items()), [(k, len(onk_seats(k))) for k, n in ONK4P.items() if len(onk_seats(k)) != n]
assert onk_seats('ושליט על ארעא') == [(4, 39)] and onk_tok('ושליט') == [(3, 24), (4, 39)] and onk_seats('לית עוד') == [(4, 35), (4, 39)] and onk_seats('דחלתא דיי')[:4] == [(1, 36), (4, 4), (4, 29), (4, 30)]
BR = {v: re.findall(r'\[([^\]]+)\]', onk_ev(4, v)[0]) for v in range(1, 50)}
BR = {v: b for v, b in BR.items() if b}
assert BR[4] == ['the fear of'] and BR[7] == ['to receive its prayers in time of tribulation', 'is', 'pray before'] and BR[24] == ['His word'] and BR[34] == ['miracles that He performed to become revealed,'] and BR[39] == ['Whose Shechinah is', 'Ruler'] and BR[43] == ['of the tribe'] * 3 and BR[28] == ['a nation who serves'] and BR[37] == ['by His word'] and len(BR) == 24, sorted(BR)
assert aramaic(4, 1)[:3] == ['וכען', 'ישראל', 'שמע'] and aramaic(4, 41)[:4] == ['בכן', 'יפרש', 'משה', 'תלת'] and aramaic(4, 44) == ['ודא', 'אוריתא', 'די', 'סדר', 'משה', 'קדם', 'בני', 'ישראל'] and aramaic(4, 24) == ['ארי', 'יי', 'אלהך', 'מימריה', 'אשא', 'אכלא', 'הוא', 'אל', 'קנא']
assert len(aramaic(4, 34)) == 29 and len(W4(34)) == 27 and len(aramaic(4, 7)) == 20 and len(W4(7)) == 14 and len(aramaic(4, 28)) == 19 and len(W4(28)) == 17

# THE STORE'S GLOSSES at the chapter's seats (words.gloss, read back): the families censused over the whole store (ch4_measure1 section G) —
# BY GLOSS where every token of the gloss is the one word, BY REFERENCE where the family is mixed (the two ילמדון of 4:10 the sharpest case:
# one written form, two stems, one gloss).
assert sg(4, 1, 'מלמד') == 'goad' and sg(4, 1, 'החקים') == 'the-enactment' and sg(4, 1, 'המשפטים') == 'the-judgment' and sg(4, 1, 'אנכי') == '?' and sg(4, 2, 'תגרעו') == 'scrape-off' and sg(4, 3, 'הראת') == 'the-see' and sg(4, 3, 'השמידו') == 'desolate-him/its' and sg(4, 3, 'בבעל') == 'in-?' and sg(4, 3, 'פעור') == 'Baal-peor'
assert sg(4, 4, 'הדבקים') == 'the-adhering' and sg(4, 5, 'למדתי') == 'goad' and sg(4, 6, 'רק') == 'leanness' and sg(4, 9, 'תשכח') == 'mislay' and sg(4, 9, 'נפשך') == 'living-being-you/your' and sg(4, 9, 'והודעתם') == 'and-know-them/their' and sg(4, 10, 'הקהל') == 'convoke' and sg(4, 10, 'ואשמעם') == 'and-hear-them/their' and sg(4, 10, 'באמר') == 'in-say'
assert sg(4, 11, 'ותקרבון') == 'and-bring-near-suffix' and sg(4, 11, 'בער') == 'kindle' and sg(4, 11, 'וערפל') == 'and-gloom' and sg(4, 12, 'ותמונה') == 'and-something-portioned--out' and sg(4, 12, 'זולתי') == 'scattering' and sg(4, 13, 'ויכתבם') == 'and-grave-them/their' and sg(4, 13, 'לחות') == 'meaning-to-glisten' and sg(4, 14, 'ההוא') == 'the-he/it'
assert sg(4, 16, 'תשחתון') == 'decay-suffix' and sg(4, 16, 'פסל') == 'idol' and sg(4, 16, 'סמל') == 'likeness' and sg(4, 16, 'תבנית') == 'structure' and sg(4, 17, 'צפור') == 'little-bird' and sg(4, 18, 'רמש') == 'creep' and sg(4, 19, 'השמימה') == 'the-heavens-suffix' and sg(4, 19, 'ונדחת') == 'and-push-off' and sg(4, 19, 'והשתחוית') == 'and-depress' and sg(4, 19, 'חלק') == 'be-smooth'
assert sg(4, 20, 'מכור') == 'from-pot' and sg(4, 21, 'התאנף') == 'breathe-hard' and sg(4, 21, 'לבלתי') == 'to-failure-of' and sg(4, 24, 'אל') == 'strength' and sg(4, 25, 'ונושנתם') == 'and-be-slack' and sg(4, 25, 'והשחתם') == 'and-decay' and sg(4, 25, 'להכעיסו') == 'to-trouble-him/its' and sg(4, 26, 'העידתי') == 'duplicate' and sg(4, 26, 'אבד') == 'wander-away' and sg(4, 26, 'תאבדון') == 'wander-away-suffix'
assert sg(4, 26, 'מהר') == 'hurrying' and sg(4, 26, 'תאריכן') == 'be--long-suffix' and sg(4, 26, 'השמד') == 'desolate' and sg(4, 26, 'תשמדון') == 'desolate-suffix' and sg(4, 27, 'והפיץ') == 'and-dash-in-pieces' and sg(4, 27, 'ונשארתם') == 'and-swell-up' and sg(4, 27, 'מתי') == 'adult' and sg(4, 27, 'ינהג') == 'drive-forth' and sg(4, 28, 'יריחן') == 'blow-suffix'
assert sg(4, 29, 'ובקשתם') == 'and-search-out' and sg(4, 29, 'תדרשנו') == 'tread-him/its' and sg(4, 30, 'בצר') == 'in-narrow' and sg(4, 30, 'באחרית') == 'in-last' and sg(4, 31, 'ירפך') == 'slacken-you/your' and sg(4, 31, 'ישחיתך') == 'decay-you/your' and sg(4, 32, 'שאל') == 'inquire' and sg(4, 32, 'ראשנים') == 'first' and sg(4, 32, 'למן') == 'to-from' and sg(4, 32, 'קצה') == 'extremity' and sg(4, 32, 'הנהיה') == 'the-be' and sg(4, 32, 'הנשמע') == 'the-hear'
assert sg(4, 33, 'השמע') == 'the-hear' and sg(4, 34, 'הנסה') == 'the-test' and sg(4, 34, 'במסת') == 'in-testing' and sg(4, 34, 'ובמוראים') == 'and-in-fear' and sg(4, 35, 'הראת') == 'see' and sg(4, 36, 'ליסרך') == 'to-chastise-you/your' and sg(4, 37, 'אהב') == 'have-affection-for' and sg(4, 37, 'ויבחר') == 'and-try' and sg(4, 37, 'ותחת') == 'and-under' and sg(4, 38, 'ועצמים') == 'and-powerful'
assert sg(4, 40, 'ייטב') == 'be--make-well' and sg(4, 40, 'תאריך') == 'be--long' and sg(4, 41, 'אז') == 'at-that-time' and sg(4, 41, 'יבדיל') == 'divide' and sg(4, 41, 'בעבר') == 'in-region-across' and sg(4, 42, 'רוצח') == 'dash-in-pieces' and sg(4, 42, 'ירצח') == 'dash-in-pieces' and sg(4, 42, 'רעהו') == 'associate-him/its' and sg(4, 42, 'בבלי') == 'in-failure' and sg(4, 42, 'שלשום') == 'trebly'
assert sg(4, 43, 'המישר') == 'the-level' and sg(4, 43, 'לגדי') == 'to-Gadite' and sg(4, 43, 'למנשי') == 'to-Menashshite' and sg(4, 44, 'התורה') == 'the-precept' and sg(4, 44, 'שם') == 'put/set' and sg(4, 45, 'בצאתם') == 'in-bring-forth-them/their' and sg(4, 46, 'בית') == '?' and sg(4, 46, 'פעור') == 'Bethpeor' and sg(4, 46, 'מול') == 'abrupt' and sg(4, 46, 'הכה') == 'strike' and sg(4, 46, 'האמרי') == 'the-Emorite'
assert sg(4, 47, 'מזרח') == 'sunrise' and sg(4, 48, 'שפת') == 'lip' and sg(4, 48, 'נחל') == 'stream' and sg(4, 48, 'שיאן') == 'Sion' and sg(4, 49, 'ים') == 'seas' and sg(4, 49, 'אשדת') == 'ravine' and sg(4, 49, 'עבר') == 'region-across' and sg(4, 49, 'הערבה') == 'the-desert' and sg(4, 36, 'אשו') == 'fire-him/its' and sg(4, 14, 'לעשתכם') == 'to-make-you/your (pl)'
GLOSS_FAMILY = {'goad': [('ילמדו', 2), ('תלמד', 2), ('ילמד', 1), ('למדתי', 1), ('מלמד', 1)], 'to-goad': [('ללמד', 2)], 'the-enactment': [('החקים', 15)], 'enactment-him/its': [('חקיו', 4)], 'scrape-off': [('יגרע', 4), ('תגרעו', 3), ('נגרע', 2), ('תגרע', 1)], 'desolate-him/its': [('השמידו', 2)], 'the-adhering': [('הדבקים', 1)], 'mislay': [('תשכח', 7), ('ישכח', 1), ('שכח', 1), ('שכחתי', 1), ('תשכחו', 1)], 'living-being-you/your': [('נפשך', 18)], 'and-know-them/their': [('והודעתם', 1)], 'convoke': [('הקהל', 3), ('הקהילו', 2)], 'and-hear-them/their': [('ואשמעם', 1)], 'and-bring-near-suffix': [('ותקרבון', 3)], 'and-stand-suffix': [('ותעמדון', 1)], 'kindle': [('בער', 4), ('בערתי', 2), ('יבער', 2), ('בערה', 1), ('תבער', 1), ('תבערו', 1)], 'and-gloom': [('וערפל', 1)], 'meaning-to-glisten': [('לחת', 15), ('לוחת', 4), ('לחות', 2)], 'decay-suffix': [('תשחתון', 2)], 'likeness': [('סמל', 1)], 'structure': [('תבנית', 7)], 'the-heavens-suffix': [('השמימה', 6)], 'from-pot': [('מכור', 1)], 'to-failure-of': [('לבלתי', 18)], 'and-to-failure-of': [('ולבלתי', 2)], 'to-trouble-him/its': [('להכעיסו', 3)], 'wander-away-suffix': [('תאבדון', 5)], 'desolate-suffix': [('תשמדון', 1)], 'blow-suffix': [('יריחן', 1)], 'in-narrow': [('בצר', 1)], 'in-last': [('באחרית', 4)], 'slacken-you/your': [('ירפך', 3)], 'decay-you/your': [('השחיתך', 1), ('ישחיתך', 1)], 'inquire': [('שאל', 5), ('ישאל', 1), ('שאול', 1), ('שאלת', 1), ('תשאל', 1)], 'to-from': [('למן', 3)], 'and-to-from-extremity': [('ולמקצה', 1)], "form-of-the-prefix-'k-'-him/its": [('כמהו', 9)], 'the-test': [('הנסה', 1)], 'in-testing': [('במסת', 1)], 'in-signs': [('באתת', 2)], 'and-in-miracle': [('ובמופתים', 1), ('ובמפתים', 1)], 'to-chastise-you/your': [('ליסרך', 1)], 'in-vigor-him/its': [('בכחו', 1)], 'and-powerful': [('ועצום', 3), ('ועצמים', 3), ('וחזק', 1), ('ועצומים', 1)], 'from-upper-part': [('ממעל', 7)], 'at-that-time': [('אז', 15)], 'in-region-across': [('בעבר', 11)], 'associate-him/its': [('רעהו', 28)], 'in-failure': [('בבלי', 2)], 'from-ago': [('מתמול', 4), ('מתמל', 2)], 'trebly': [('שלשם', 7), ('שלשום', 3)], 'to-Reubenite': [('לראובני', 3)], 'to-Gadite': [('לגדי', 1)], 'to-Menashshite': [('למנשי', 1)], 'in-bring-forth-them/their': [('בצאתם', 3)], 'the-Emorite': [('האמרי', 31)], 'region-across': [('עבר', 5)], 'hind-part-him/its': [('אחריו', 11)], 'hind-part-you/your': [('אחריך', 15)], 'from-nearest-part': [('מקרב', 18)], 'from-nearest-part-you/your': [('מקרבך', 12)], 'in-nearest-part': [('בקרב', 14)], 'fire-him/its': [('אשו', 1)], 'to-make-you/your (pl)': [('לעשתכם', 1)], 'word/thing-you/your (pl)': [('דבריכם', 5)], 'the-Pisgah': [('הפסגה', 6)], 'the-level': [('המישר', 2)], 'and-something-portioned--out': [('ותמונה', 1), ('ותמנת', 1)], 'something-portioned--out': [('תמונה', 3), ('תמונת', 3)], 'the-see': [('הראת', 3), ('הנראה', 2), ('הראים', 1)], 'goad-suffix': [('ילמדון', 2)], 'idol': [('פסל', 6), ('פסילי', 1)], 'and-push-off': [('ונדחת', 2), ('וידיחו', 1), ('ונדחה', 1)], 'be-smooth': [('המלט', 3), ('חלק', 2), ('יחלק', 2), ('תחלק', 2), ('אחלק', 1), ('אמלטה', 1)], 'and-be-slack': [('ויישן', 2), ('ונושנתם', 1)], 'and-decay': [('והשחתם', 1), ('ושחת', 1), ('ושחתם', 1), ('ותשחת', 1)], 'duplicate': [('העד', 3), ('העידתי', 2), ('העדתה', 1), ('העדתי', 1), ('מעיד', 1)], 'wander-away': [('אבד', 8), ('אבדנו', 2), ('אבדה', 1), ('אבדת', 1), ('מאביד', 1), ('תאבד', 1), ('תאבדו', 1)], 'hurrying': [('מהר', 9)], 'desolate': [('השמד', 2), ('השמיד', 2), ('ישמיד', 1), ('תשמידו', 1)], 'and-dash-in-pieces': [('ויפץ', 2), ('והפיץ', 1), ('ויפצו', 1), ('ורצח', 1)], 'and-swell-up': [('ונשארתם', 2), ('והדרת', 1), ('וישאר', 1), ('וישארו', 1)], 'drive-forth': [('ינהג', 1), ('נהג', 1)], 'and-search-out': [('ויבקש', 3), ('ובקשתם', 2)], 'tread-him/its': [('אדרשנו', 1), ('ידרשנו', 1), ('תדרשנו', 1)], 'first': [('ראשנה', 3), ('ראשנים', 3), ('ראשון', 1), ('ראשונה', 1)], 'extremity': [('קצה', 6), ('אצילי', 1), ('קץ', 1)], 'the-be': [('הנגשים', 1), ('הנהיה', 1)], 'the-hear': [('השמע', 2), ('הנשמע', 1), ('השמעים', 1)], 'and-in-fear': [('ובמוראים', 1), ('ובמרא', 1)], 'have-affection-for': [('אהב', 5), ('אהבת', 2), ('אהבתי', 2), ('אהבים', 1), ('אהובה', 1)], 'and-try': [('ויבחר', 5), ('ובחרת', 1)], 'be--make-well': [('ייטב', 10), ('היטב', 6), ('היטיבו', 2), ('תיטיב', 2), ('איטיב', 1), ('היטיב', 1), ('ייטיב', 1)], 'be--long': [('תאריכו', 2), ('ארכו', 1), ('יאריך', 1), ('יאריכו', 1), ('תאריך', 1)], 'divide': [('יבדיל', 3), ('הבדיל', 2), ('הבדלתי', 2), ('תבדיל', 2), ('בדד', 1), ('הבדלו', 1), ('מבדיל', 1)], 'dash-in-pieces': [('רצח', 7), ('ירצח', 2), ('תרצח', 2), ('נפוץ', 1), ('נפצו', 1), ('רוצח', 1)], 'the-testimony': [('העדת', 28), ('העדות', 8)], 'strike': [('הכה', 7), ('מכה', 7), ('יכה', 4), ('הכות', 3), ('הכית', 2), ('תכה', 2), ('הכו', 1), ('מכים', 1), ('נכה', 1), ('נכו', 1), ('נכתה', 1)], 'lip': [('שפת', 16), ('שפה', 3), ('שפתים', 2)], 'stream': [('נחל', 15), ('נהר', 4), ('שבלים', 4), ('נחלי', 2)], 'seas': [('ים', 24), ('ימים', 3)], 'and-under': [('ותחת', 3)], 'Bethpeor': [('פעור', 3)], 'Baal-peor': [('פעור', 4)], 'in-time': [('בעת', 20)], 'little-bird': [('צפור', 4), ('צפרים', 2)], 'creep': [('רומש', 2), ('רמש', 2), ('תרמש', 2)], 'and-grave-them/their': [('ויכתבם', 2), ('וכתבתם', 2)], 'be--long-suffix': [('תאריכן', 2), ('יאריכן', 1), ('יארכון', 1), ('יארכן', 1)]}
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall() for g in GLOSS_FAMILY}
assert all(sorted(GT[g]) == sorted(v) for g, v in GLOSS_FAMILY.items()), [g for g, v in GLOSS_FAMILY.items() if sorted(GT[g]) != sorted(v)]
# BY GLOSS — every token of the gloss the one word (or one family read the same at every seat): the rewrite covers the whole store
OVERRIDE_GLOSS = [('goad', 'teach'), ('to-goad', 'to-teach'), ('the-enactment', 'the-statutes'), ('enactment-him/its', 'his-statutes'), ('scrape-off', 'diminish'), ('desolate-him/its', 'destroyed-him'), ('the-adhering', 'who-cleave'), ('mislay', 'forget'), ('living-being-you/your', 'your-soul'), ('and-know-them/their', 'and-make-them-known'), ('convoke', 'assemble'), ('and-hear-them/their', 'and-I-will-make-them-hear'), ('and-stand-suffix', 'and-you-stood'), ('kindle', 'burn'), ('and-gloom', 'and-thick-darkness'), ('meaning-to-glisten', 'tablets'), ('decay-suffix', 'you-act-corruptly'), ('likeness', 'a-figure'), ('structure', 'the-likeness-of'), ('the-heavens-suffix', 'heavenward'), ('from-pot', 'from-the-furnace-of'), ('to-failure-of', 'so-as-not'), ('and-to-failure-of', 'and-so-as-not'), ('to-trouble-him/its', 'to-provoke-him'), ('wander-away-suffix', 'you-shall-perish'), ('desolate-suffix', 'you-shall-be-destroyed'), ('blow-suffix', 'they-smell'), ('in-narrow', 'in-distress'), ('in-last', 'in-the-end-of'), ('slacken-you/your', 'fail-you'), ('decay-you/your', 'destroy-you'), ('inquire', 'ask'), ('to-from', 'from'), ('and-to-from-extremity', 'and-from-the-end-of'), ("form-of-the-prefix-'k-'-him/its", 'like-it'), ('the-test', 'has-tried'), ('in-testing', 'by-trials'), ('in-signs', 'by-signs'), ('and-in-miracle', 'and-by-wonders'), ('to-chastise-you/your', 'to-instruct-you'), ('in-vigor-him/its', 'with-his-power'), ('and-powerful', 'and-mighty'), ('from-upper-part', 'above'), ('at-that-time', 'then'), ('in-region-across', 'beyond'), ('associate-him/its', 'his-neighbor'), ('in-failure', 'without'), ('from-ago', 'from-yesterday'), ('trebly', 'the-day-before'), ('to-Reubenite', 'to-the-Reubenites'), ('to-Gadite', 'to-the-Gadites'), ('to-Menashshite', 'to-the-Manassites'), ('in-bring-forth-them/their', 'when-they-came-out'), ('the-Emorite', 'the-Amorite'), ('region-across', 'beyond'), ('hind-part-him/its', 'after-him'), ('hind-part-you/your', 'after-you'), ('from-nearest-part', 'from-the-midst-of'), ('from-nearest-part-you/your', 'from-your-midst'), ('in-nearest-part', 'in-the-midst-of'), ('fire-him/its', 'his-fire'), ('to-make-you/your (pl)', 'for-you-to-do'), ('word/thing-you/your (pl)', 'your-words')]
# BY REFERENCE — the family mixed (two stems in one written form, an absolute beside a construct, a homograph): the seat named
OVERRIDE_REF_SPEC = [(1, 'אנכי', 'I', 0), (1, 'המשפטים', 'the-judgments', 0), (2, 'אנכי', 'I', 0), (2, 'אנכי', 'I', 1), (3, 'הראת', 'that-saw', 0), (3, 'בבעל', 'in-Baal', 0), (3, 'פעור', 'Peor', 0), (3, 'בעל', 'Baal', 0), (3, 'פעור', 'Peor', 1), (5, 'למדתי', 'I-have-taught', 0), (5, 'חקים', 'statutes', 0), (5, 'ומשפטים', 'and-judgments', 0), (8, 'חקים', 'statutes', 0), (8, 'ומשפטים', 'and-judgments', 0), (8, 'אנכי', 'I', 0), (9, 'השמר', 'take-heed', 0), (9, 'ושמר', 'and-keep', 0), (9, 'הדברים', 'the-things', 0), (10, 'באמר', 'when-said', 0), (10, 'ילמדון', 'they-may-learn', 0), (10, 'ילמדון', 'they-shall-teach', 1), (12, 'דברים', 'words', 0), (12, 'ותמונה', 'and-a-form', 0), (13, 'הדברים', 'the-words', 0), (13, 'ויכתבם', 'and-he-wrote-them', 0), (14, 'חקים', 'statutes', 0), (14, 'ומשפטים', 'and-judgments', 0), (14, 'ההוא', 'that', 0), (15, 'תמונה', 'form', 0), (16, 'פסל', 'a-graven-image', 0), (16, 'תמונת', 'the-form-of', 0), (17, 'צפור', 'bird', 0), (19, 'ונדחת', 'and-be-drawn-away', 0), (19, 'והשתחוית', 'and-bow-down', 0), (19, 'חלק', 'apportioned', 0), (22, 'אנכי', 'I', 0), (23, 'פסל', 'a-graven-image', 0), (23, 'תמונת', 'the-form-of', 0), (24, 'אל', 'God', 0), (25, 'ונושנתם', 'and-you-have-grown-old', 0), (25, 'והשחתם', 'and-you-act-corruptly', 0), (25, 'פסל', 'a-graven-image', 0), (25, 'תמונת', 'the-form-of', 0), (26, 'העידתי', 'I-call-to-witness', 0), (26, 'אבד', 'perish', 0), (26, 'מהר', 'quickly', 0), (26, 'השמד', 'utterly', 0), (27, 'והפיץ', 'and-will-scatter', 0), (27, 'ונשארתם', 'and-you-shall-be-left', 0), (27, 'ינהג', 'will-lead', 0), (29, 'ובקשתם', 'and-you-shall-seek', 0), (29, 'תדרשנו', 'you-seek-him', 0), (30, 'הדברים', 'the-things', 0), (31, 'אל', 'God', 0), (32, 'ראשנים', 'former', 0), (32, 'קצה', 'the-end-of', 0), (32, 'הנהיה', 'has-there-been', 0), (32, 'הנשמע', 'has-it-been-heard', 0), (33, 'השמע', 'has-heard', 0), (34, 'ובמוראים', 'and-by-terrors', 0), (35, 'הראת', 'were-shown', 0), (36, 'ודבריו', 'and-his-words', 0), (37, 'ותחת', 'and-because', 0), (37, 'אהב', 'he-loved', 0), (37, 'ויבחר', 'and-he-chose', 0), (40, 'אנכי', 'I', 0), (40, 'ייטב', 'it-may-go-well', 0), (40, 'תאריך', 'you-may-prolong', 0), (41, 'יבדיל', 'set-apart', 0), (42, 'רוצח', 'a-manslayer', 0), (42, 'ירצח', 'slays', 0), (44, 'שם', 'set', 0), (45, 'העדת', 'the-testimonies', 0), (45, 'והחקים', 'and-the-statutes', 0), (45, 'והמשפטים', 'and-the-judgments', 0), (46, 'בית', 'Beth', 0), (46, 'פעור', 'Peor', 0), (46, 'הכה', 'smote', 0), (48, 'שפת', 'the-bank-of', 0), (48, 'נחל', 'the-valley-of', 0), (49, 'ים', 'the-sea-of', 0)]
OVERRIDE_REF3 = [(f'Deut.4.{v}:{sidx(4, v, tok, nth)}', new, tok) for v, tok, new, nth in OVERRIDE_REF_SPEC]
OVERRIDE_REF = [(k, v) for k, v, _ in OVERRIDE_REF3]
assert len(OVERRIDE_REF) == 81 and len({k for k, _ in OVERRIDE_REF}) == 81 and len(OVERRIDE_GLOSS) == 63 and len({k for k, _ in OVERRIDE_GLOSS}) == 63, (len(OVERRIDE_REF), len(OVERRIDE_GLOSS))
assert all(g in GLOSS_FAMILY for g, _ in OVERRIDE_GLOSS) and all(sg(4, v, tok, nth) is not None for v, tok, _, nth in OVERRIDE_REF_SPEC)
ALREADY = ['and-bring-near-suffix', 'leanness', 'scattering', 'breathe-hard', 'adult', 'to-flit', 'and-flit', 'the-level', 'the-precept', 'in-gorge', 'abrupt', 'ravine', 'the-desert', 'in-time', 'hind-part', 'in-pasture', 'sunrise-suffix']   # the sitting-1 rewrites the chapter shares (their values: only, except, was-angry, men, to-flee, and-flee, the-tableland, the-Torah, in-the-valley, opposite, the-slopes-of, the-Arabah, at-the-time, after, in-the-wilderness, toward-the-sunrise)
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
PATCHED = 'THE DEUTERONOMY WALK sitting 2 (2026-09-16, Deuteronomy 4)' in OV
assert all(f'"{k}": ' in OV for k in ALREADY)
assert PATCHED or '"Deut.4.' not in OV
if not PATCHED: assert all(f'"{k}": ' not in OV for k, _ in OVERRIDE_GLOSS), [k for k, _ in OVERRIDE_GLOSS if f'"{k}": ' in OV]
else: assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV][:6]
assert OV.count('  "circle-them/their": "round-about-them"') == 1 and OV.count('  "Deut.3.29:3": "Beth"') == 1
