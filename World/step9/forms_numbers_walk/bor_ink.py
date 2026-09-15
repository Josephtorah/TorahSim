import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 14 — THE BORDERS, Numbers 34:1-29 (2026-09-12; the owner: "Go" after the #154 rereads, on the ruling READ THEN
# COMPILE): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 13's form
# (jou_ink.py): the heads found BY POSITION and asserted (NO piska on chapter 34 — the shelf silent from 31:25 to 35:8; the whole export scanned
# for a row citing the chapter in FOUR forms — the English's "(Bamidbar 34:n)" and "(Ibid. 34:n)", the Hebrew's chapter mark with the gershayim
# and the Hebrew's own "ibid.", the word "there" (שם) before the chapter mark: ONE row of another chapter cites it, 1:2 on 5:2 citing 34:2 — the
# one "command" that entails no expense, credited); coverage computed; every cut by consonants (the misses collected, asserted empty); the
# engine's numeral parser MEASURED on every verse (three number verses, every one read — 34:13's nine, 34:15's construct "two of", 34:18's
# distributive "one ... one"); the hand's facts as asserts, run all at once by assert_driver.py after the measurement passes (bor_dump.py,
# bor_measure1.py, bor_measure2.py) printed them; every gloss of a verb the STORE'S OWN (words.gloss); the piece-wise cutters HP / AP.
# Shared by bor_rows_onkelos_a.py / _b.py and write_bor_ledger.py.
# THE SPAN: ONE draft — num_34_borders 34:1-29 (the portion Masei's second chapter); the next draft (num_35_refuge_cities) opens at 35:1.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-12'
UID = 'num_34_borders'
PISKAOT = []
CREDITED = [(1, 2, (34, 2))]
TITLE = 'The borders — this is the land that shall fall to you as an inheritance, the land of Canaan by its borders: the south side from the wilderness of Zin along Edom, from the end of the Salt Sea eastward, turning to the ascent of Akrabbim, to Zin, south of Kadesh-barnea, Hazar-addar, Azmon, the brook of Egypt, to the sea; the west border the great sea; the north from the great sea to Mount Hor, to Lebo-hamath, Zedad, Ziphron, Hazar-enan; the east from Hazar-enan to Shepham, Riblah, east of Ain, down to the shoulder of the sea of Chinnereth, down the Jordan to the Salt Sea; Moses commands it to the nine tribes and the half tribe, the two and a half having taken theirs beyond the Jordan at Jericho; the LORD names the men who shall divide it — Eleazar the priest, Joshua son of Nun, and one prince from each tribe: Caleb son of Jephunneh for Judah and nine more'
OUT = f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md'

def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']
sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
heads = {}
for p, rows in enumerate(sif, 1):
    if not rows: continue
    m = re.search(r'\((Bamidbar|Devarim)\.? (\d+):(\d+)', clean(rows[0])[:60])
    heads[p] = (m.group(1), int(m.group(2)), int(m.group(3))) if m else None
# THE SHELF BY POSITION: piska 158 (31:22) is followed by 159 (35:9) — NO piska on chapter 34 (nor on 32 or 33): the shelf silent from 31:25 to
# 35:8, as sitting 11 computed (165 verses); this chapter is the FOURTH stretch of that silence read on the translation alone. THE "FOUND BY
# POSITION" CLAUSE run on the whole export in both files in FOUR FORMS — the English's "(Bamidbar 34:n)" and "(Ibid. 34:n)", the Hebrew's chapter
# mark with the gershayim (במדבר ל״ד, "Numbers 34") and the Hebrew's own ibid., the word "there" before the mark ((שם ל"ד), "ibid. 34" — sitting
# 13's scan had not looked for it, a lesson): "(Bamidbar 34:2)" ONE row — 1:2 (on 5:2, the sending out of the unclean): Rabbi Shimon ben Yochai's
# "command" everywhere entails expense (Leviticus 24:2 the oil, 35:2 the Levites' cities, 28:2 the offerings) EXCEPT ONE — 34:2 "command the
# children of Israel and say to them: when you come to the land of Canaan" — "impel them to the division of the land"; the Hebrew row cites it as
# (שם ל"ד) "ibid. 34". The English "Ibid. 34" hits are EXODUS 34:30 (1:8 — Aaron and all Israel afraid of Moses' shining face; the Hebrew row
# 1:7 carries the same citation as (שם ל"ד) after Exodus 24:17) and DEUTERONOMY 34:1-3 (135:1 on Deuteronomy 3:26 — the LORD showing Moses "all
# that is called the land of Israel"; the Hebrew names Deuteronomy 34:1 outright); the Hebrew's third "שם לד" (118:1, unparenthesized) is
# Exodus 34:20's firstborn donkey. Each read to its verse; the abbreviation's book is the row's last-named one. The credited row was READ WHOLE at
# sitting 2 (the Naso ledger num_05_camp_pure_theft — "four readings of 'command'", the exception 34:2 named there) and is CREDITED here with a
# QUICK LOOK (credit guard 1: opened again in both files — what it says of 34:2 is one clause). THE CENSUS MEETS THE ROW: "command the children
# of Israel" stands FIVE times in the Torah (Leviticus 24:2; Numbers 5:2, 28:2, 34:2, 35:2) — exactly the row's five.
assert heads[157] == ('Bamidbar', 31, 1) and heads[158] == ('Bamidbar', 31, 22) and heads[159] == ('Bamidbar', 35, 9) and len(sif) == 161
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (32, 33, 34)) == [] and [p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 35 and h[2] < 9] == []
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
CIT_A = [(p, r, re.findall(r'\(Bamidbar\.? 34:(\d+)', E(p, r))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(r'\(Bamidbar\.? 34:\d+', clean(row))]
CIT_B = [(p, r, re.findall(r'\(Ibid\.? 34:(\d+)', E(p, r))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(r'\(Ibid\.? 34:\d+', clean(row))]
CIT_C = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'במדבר ל[\"״]?ד\b', clean(row))]
CIT_D = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'שם ל[\"״]?ד[\)\s:]', clean(row))]
assert CIT_A == [(1, 2, ['2'])] and CIT_B == [(1, 8, ['30']), (135, 1, ['1'])] and CIT_C == [] and CIT_D == [(1, 2), (1, 7), (118, 1)], (CIT_A, CIT_B, CIT_C, CIT_D)
assert heads[1] == ('Bamidbar', 5, 1) and 'Except in one; and which is that? (Bamidbar 34:2) "Command the children of Israel and say to them: When you come to the land of Canaan, etc." — where the intent is: Impel them to the division of the land.' in E(1, 2)
assert 'חוץ מאחת, ואיזה זה צו את בני ישראל ואמרת אלהם כי אתם באים אל הארץ כנען (שם ל"ד) תזרזם לענין חילוק הארץ' in Hb(1, 2) and re.findall(r'\([^)]*\)', Hb(1, 2))[-4:] == ['(שם ל"ה)', '(שם כ"ח)', '(שם ל"ד)', "(בראשית ב')"]
assert '(Shemot 24:17)' in E(1, 8) and '(Ibid. 34:30) "And Aaron and all of Israel saw Moses, and, behold, the skin of his face shone' in E(1, 8) and re.findall(r'\([^)]*\)', Hb(1, 7))[-2:] == ['(שמות כ״ד:י״ז)', '(שם ל"ד)'] and 'וירא אהרן וכל בני ישראל את משה והנה קרן עור פניו' in Hb(1, 7)
assert heads[135] == ('Devarim', 3, 26) and '(Ibid. 34:1-3) "And the L-rd showed him' in E(135, 1) and Hb(135, 1).rstrip().endswith('שנאמר (דברים ל״ד:א׳) ויראהו ה\' את הארץ ואת נפתלי ואת הנגב ואת הככר:') and 'ת"ל עוד במקום אחר שם לד ופטר חמור תפדה בשה' in Hb(118, 1)
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
assert re.search(r'^- Sifrei Bamidbar 1:2 — MATERIAL\. FOUR READINGS OF "COMMAND"', LED['num_05_camp_pure_theft_2026-09-09.md'], re.M) and 'one exception, 34:2' in LED['num_05_camp_pure_theft_2026-09-09.md'] and re.search(r'^- Sifrei Bamidbar 1:8 ', LED['num_05_camp_pure_theft_2026-09-09.md'], re.M) and re.search(r'^- Sifrei Bamidbar 135:1 ', LED['num_27_zelophehad_joshua_2026-09-09.md'], re.M)
SIF_ROWS = {}
def head(p): return heads[p][1:]
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
# THE MARKS' ORDER (sitting 7's lesson): the DB's raw order of the points differs from the canonical at many tokens (the dagesh before or after
# the vowel) — every pointed comparison is made on NFC-normalized strings on BOTH sides (the meteg kept where the print shows it)
def NF(s): return unicodedata.normalize('NFC', s)
def PT(b, c, v, tok): return [NF(x) for x in byp[(b, c, v)] if plain(x) == tok]
ONK_LEN = {c: len(onk[c - 1]) for c in (33, 34, 35)}
assert ONK_LEN == {33: 56, 34: 29, 35: 34} and {c: len(onk_he[c - 1]) for c in (33, 34, 35)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: no ledger has read an Onkelos row of 34; TWO ledgers NAME a verse of the chapter (the sotah ledger 34:11 — the border's
# "reach" verb beside the sotah's "blot"; the vows' exam 34:18): names, not reads; FRESH.
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 34:\d', t, re.M)) == []
NAMING = sorted((f, sorted(set(re.findall(r'Num(?:bers)? 34:\d+', t)))) for f, t in LED.items() if re.search(r'Num(?:bers)? 34:\d+', t))
assert NAMING == [('num_05_sotah_2026-09-09.md', ['Num 34:11']), ('num_30_vows_exam_2026-09-12.md', ['Num 34:18'])], NAMING

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[33] == 56 and VC[34] == 29 and VC[35] == 34
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
assert steps(UID) == [(34, v) for v in range(1, 30)] and 'status: draft' in unit_text(UID) and 'operators:' not in unit_text(UID) and 'refs: "34:1-29"' in unit_text(UID)
assert steps('num_35_refuge_cities')[0] == (35, 1) and 'status: frozen' in unit_text('num_33_journeys')
SPAN = [(34, v) for v in range(1, 30)]
NV = 29

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byraw = {}, {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byraw.setdefault((b, c, v), []).append(he)
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
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def NP(*toks): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, m in ws if x in toks and m and 'Np' in m})
def NPX(name):
    """every seat of a proper name by its bare token and its prefixed forms (the morphology's Np)"""
    def bare(x):
        for p in ('ול', 'ו', 'ל', 'ב', 'מ'):
            if x.startswith(p) and len(x) > len(p) + 2: return x[len(p):]
        return x
    return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, m in ws if bare(x) == name and m and 'Np' in m})
def seats_in(pred): return [(v, x) for (c, v) in SPAN for x, m in by[('Num', 34, v)] if pred(x, m)]
def cnt_in(pred): return sum(1 for (c, v) in SPAN for x, m in by[('Num', 34, v)] if pred(x, m))
FAIL = []
def H(c, v, *cons):
    w, wp = words('Num', c, v), byp[('Num', c, v)]
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
def onk_seats(sub): return [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if sub in arm(c + 1, v + 1)]
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
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 34 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))
# THE STORE'S ONE WRITTEN-AND-READ PAIR IN THE CHAPTER (sitting 12's lesson — a pair is one token more in the store than in the DB; the DB writes
# the written form): 34:4 "and it shall be [its goings-out]" — WRITTEN singular (והיה, the DB's token, HC/Vqq3ms) and READ plural (והיו, the
# store's pointed ninth token); the chapter's four other seats of the clause are written plural (34:5, 8, 9, 12), 34:4 the one written singular.
# Joshua 15:4 carries the identical clause with the written singular (the DB's token); the store holds no Joshua, its reading unmeasured here.
assert [(v, n, len(by[('Num', 34, v)])) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34 GROUP BY v.verse").fetchall() if n != len(by[('Num', 34, v)])] == [(4, 19, 18)]
STORE44 = store.execute("SELECT w.idx, w.he_plain, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34 AND v.verse=4 AND w.idx IN (8, 9) ORDER BY w.idx").fetchall()
assert STORE44 == [(8, 'ו/היה', 'ו/היה'), (9, 'ו/היו', 'וְ/הָיוּ֙')] and [(x, m) for x, m in by[('Num', 34, 4)] if x == 'והיה'] == [('והיה', 'HC/Vqq3ms')] and [(x, m) for x, m in by[('Josh', 15, 4)] if x in ('והיה', 'והיו')] == [('והיה', 'HC/Vqp3ms')]
assert phrase(['והיה', 'תוצאתיו'], None) == ['Num 34:4'] and phrase(['והיו', 'תוצאתיו'], None) == ['Num 34:12', 'Num 34:5', 'Num 34:9'] and phrase(['והיו', 'תוצאת'], None) == ['Num 34:8'] and phrase(['והיה', 'תצאות'], None) == ['Josh 15:4'] and phrase(['והיו', 'תצאות'], None) == ['Josh 15:11', 'Josh 19:22'] and phrase(['והיה', 'תצאתיו'], None) == ['Josh 18:12', 'Josh 18:14']
assert store.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Josh'").fetchone() == (0,)

# THE ENGINE'S PARSER on every verse of the chapter — MEASURED before the compile is asked: THREE number verses in twenty-nine, every one read —
# 34:13 "to the nine tribes and the half tribe" [9] (the construct "nine of", rule 22's construct numeral); 34:15 "the two tribes and the half
# tribe" [2] — the construct "two of" by the points (rule 3: a sheva under the shin and a tsere under the nun, emitted with the caret); 34:18
# "one prince, one prince from a tribe" [1, 1] — THE DISTRIBUTIVE DOUBLING read as two ones (the same at 13:2's spies "one man, one man" and
# 7:11's "one prince a day, one prince a day"; 17:21's rods [1, 1, 12]; Joshua 3:12's stones [12, 1, 1], 22:14's embassy [10, 1, 1]); "half" is
# no numeral before a tribe (the fraction class reads only before a measure noun — 34:14 silent, 32:33 silent, Joshua 14:3-4 [2] each); no
# starred homograph; 35:1 empty. NO GAP — the walk's third reading with none. Joshua 13:7 and 14:2 read the nine as this chapter does.
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
PARSED = {v: N('Num', 34, v) for v in range(1, NV + 1) if N('Num', 34, v)}
assert PARSED == {13: [9], 15: [2], 18: [1, 1]}, PARSED
assert {v: O('Num', 34, v) for v in range(1, NV + 1) if O('Num', 34, v)} == {} and [(v, t) for v in range(1, NV + 1) for t in CS.verse_words('Num', 34, v) if t[-1] in '#~^%@|*'] == [(15, 'שני^')] and N('Num', 35, 1) == [] and O('Num', 35, 1) == []
assert N('Josh', 13, 7) == [9] and N('Josh', 14, 2) == [9] and N('Josh', 14, 3) == [2] and N('Josh', 14, 4) == [2] and N('Num', 32, 33) == [] and N('Num', 34, 14) == []
assert N('Num', 13, 2) == [1, 1] and N('Num', 7, 11) == [1, 1] and N('Num', 17, 21) == [1, 1, 12] and N('Num', 1, 44) == [12, 1] and N('Josh', 3, 12) == [12, 1, 1] and N('Josh', 4, 2) == [12, 1, 1] and N('Josh', 22, 14) == [10, 1, 1] and N('Deut', 1, 23) == [12, 1] and N('Ezek', 47, 13) == [12]
SEQ = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
assert [l for l in SEQ.split('\n') if 'Num 34' in l or "'Num', 34" in l] == []   # no line of the tape names the chapter

# THE FRAMES AND THE REGISTER: TWO divine frames — 34:1 (the borders, 34:2-12) and 34:16 (the dividers, 34:17-29), the same five words at both —
# with MOSES' OWN COMMAND between them (34:13-15, "and Moses commanded the children of Israel, saying": the form's two seats in the Torah are
# 34:13 and 36:5, both in the plains of Moab; "and Moses commanded" seven Torah seats); THREE narrative verbs in the chapter (the two "spoke" and
# the one "commanded"); the chapters of Numbers without a frame unchanged (22-24, 29, 30, 32, 36); twelve chapters carry exactly two frames.
# The border runs on TWENTY "and-it-shall" verbs (34:2-12, computed on the morphology): "and it shall be" 4 + "and they shall be" 4, "and it
# shall go down" 3, "and it shall turn" 2, "and it shall pass" 2 (both in 34:4), "and it shall go out" 2, "and you shall say", "and you shall mark
# out for yourselves", "and it shall reach" — and four second-person imperfects: "you shall mark out" twice (34:7, 8), "you shall inherit" (34:13),
# "you shall take" (34:18).
DIV = {}
for (b, c, v), ws in by.items():
    if b != 'Num': continue
    w = [x for x, _ in ws]
    if any(w[i] in ('ויאמר', 'וידבר') and w[i + 1] == 'יהוה' for i in range(len(w) - 1)): DIV.setdefault(c, []).append(v)
assert DIV[34] == [1, 16] and [c for c in range(1, 37) if c not in DIV] == [22, 23, 24, 29, 30, 32, 36] and DIV[33] == [50] and DIV[35] == [1, 9]
assert words('Num', 34, 1) == words('Num', 34, 16) == ['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'] and [c for c in range(1, 37) if len(DIV.get(c, [])) == 2] == [1, 6, 7, 9, 11, 12, 16, 21, 26, 31, 34, 35]
assert len([s for s in phrase(['וידבר', 'יהוה', 'אל', 'משה', 'לאמר']) if s.startswith('Num')]) == 32 and len(phrase(['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'])) == 70
assert phrase(['ויצו', 'משה', 'את', 'בני', 'ישראל']) == ['Num 34:13', 'Num 36:5'] and phrase(['ויצו', 'משה']) == ['Deut 27:1', 'Deut 27:11', 'Deut 31:10', 'Deut 31:25', 'Exod 36:6', 'Num 34:13', 'Num 36:5'] and words('Num', 36, 5)[:8] == ['ויצו', 'משה', 'את', 'בני', 'ישראל', 'על', 'פי', 'יהוה']
REG = [(v, x, m) for (c, v) in SPAN for x, m in by[('Num', 34, v)] if m and re.search(r'V.w', m)]
assert REG == [(1, 'וידבר', 'HC/Vpw3ms'), (13, 'ויצו', 'HC/Vpw3ms'), (16, 'וידבר', 'HC/Vpw3ms')]
WQ = [(v, x) for (c, v) in SPAN for x, m in by[('Num', 34, v)] if m and re.search(r'^HC/V.q', m)]
assert len(WQ) == 20 and Counter(x for _, x in WQ) == Counter({'והיה': 4, 'והיו': 4, 'וירד': 3, 'ונסב': 2, 'ועבר': 2, 'ויצא': 2, 'ואמרת': 1, 'והתאויתם': 1, 'ומחה': 1}) and all(2 <= v <= 12 for v, _ in WQ) and [x for v, x in WQ if v == 4] == ['ונסב', 'ועבר', 'והיה', 'ויצא', 'ועבר']
assert [(v, x, m) for (c, v) in SPAN for x, m in by[('Num', 34, v)] if m and re.search(r'V.i2mp', m)] == [(7, 'תתאו', 'HVpi2mp'), (8, 'תתאו', 'HVpi2mp'), (13, 'תתנחלו', 'HVti2mp'), (18, 'תקחו', 'HVqi2mp')]

# 34:2 THE HEADING: "COMMAND the children of Israel and say to them" — "command the children of Israel" FIVE Torah seats (Leviticus 24:2; Numbers
# 5:2, 28:2, 34:2, 35:2), with "and say to them" two (28:2, 34:2): the Sifrei 1:2's five are the ink's five. "WHEN YOU COME to the land of Canaan"
# — the participial form "you are coming" one seat (the refuge cities and 33:51 say "you are crossing the Jordan"; Leviticus 23:10, 25:2, Exodus
# 12:25 "when you come" in the imperfect); "THE LAND CANAAN" — the article on the land and none on Canaan, one seat (thirteen Torah seats of the
# bare "the land of Canaan", 34:2's second clause and 34:29 among them). "THIS IS THE LAND" three Torah seats — 34:2, 34:13 and Deuteronomy 34:4
# (the view from Nebo: "this is the land which I swore"). "WHICH SHALL FALL TO YOU AS AN INHERITANCE" — the lot's verb: "shall fall" with the
# inheritance at this one Torah seat (the token's other Torah seats: Exodus 15:16's terror that falls, Deuteronomy 1:1's place Tophel); Joshua
# 13:6 "cast it to Israel for an inheritance", 23:4, Judges 18:1 "no inheritance had fallen to Dan", Ezekiel 47:14 "this land shall fall to you
# as an inheritance" (34:2's clause with the verb), 48:29 "which you shall cause to fall", Psalm 16:6 "the lines have fallen to me"; ONKELOS
# "shall be DIVIDED to you" — the one Aramaic verb for 34:2's "fall" and for 26:53, 55, 56's "shall be divided" (four seats in Onkelos Numbers).
# "BY ITS BORDERS" (34:2, 34:12 — the chapter's inclusio) four Bible seats: Joshua 18:20 (Benjamin's border "round about") and 19:49 ("they
# finished dividing the land by its borders") the other two. The border-word SIXTEEN times in the chapter — half of the book's thirty-two (21
# has six, 20 four, 22 and 35 two, 32 and 33 one); sixty in the Torah. "As an inheritance" three Torah seats (26:53, 34:2, 36:2), all the land's.
assert words('Num', 34, 2) == ['צו', 'את', 'בני', 'ישראל', 'ואמרת', 'אלהם', 'כי', 'אתם', 'באים', 'אל', 'הארץ', 'כנען', 'זאת', 'הארץ', 'אשר', 'תפל', 'לכם', 'בנחלה', 'ארץ', 'כנען', 'לגבלתיה']
assert phrase(['צו', 'את', 'בני', 'ישראל']) == ['Lev 24:2', 'Num 28:2', 'Num 34:2', 'Num 35:2', 'Num 5:2'] and phrase(['צו', 'את', 'בני', 'ישראל', 'ואמרת', 'אלהם']) == ['Num 28:2', 'Num 34:2'] and U('צו', books=T) == ['Deut 2:4', 'Lev 24:2', 'Lev 6:2', 'Num 28:2', 'Num 34:2', 'Num 35:2', 'Num 5:2']
assert phrase(['כי', 'אתם', 'באים'], None) == ['Num 34:2'] and phrase(['כי', 'אתם', 'עברים'], None) == ['Deut 11:31', 'Num 33:51', 'Num 35:10'] and phrase(['כי', 'תבאו', 'אל', 'הארץ']) == ['Exod 12:25', 'Lev 23:10', 'Lev 25:2'] and phrase(['הארץ', 'כנען'], None) == ['Num 34:2'] and len(phrase(['ארץ', 'כנען'])) == 13 and words('Num', 34, 29)[-2:] == ['בארץ', 'כנען']
assert phrase(['זאת', 'הארץ']) == ['Deut 34:4', 'Num 34:13', 'Num 34:2'] and words('Deut', 34, 4)[:6] == ['ויאמר', 'יהוה', 'אליו', 'זאת', 'הארץ', 'אשר']
assert U('תפל', books=T) == ['Deut 1:1', 'Exod 15:16', 'Num 34:2'] and [(x, m) for x, m in by[('Num', 34, 2)] if x == 'תפל'] == [('תפל', 'HVqi3fs')] and words('Josh', 13, 6)[-6:] == ['רק', 'הפלה', 'לישראל', 'בנחלה', 'כאשר', 'צויתיך'] and words('Judg', 18, 1)[-8:] == ['לו', 'עד', 'היום', 'ההוא', 'בתוך', 'שבטי', 'ישראל', 'בנחלה']
assert words('Ezek', 47, 14)[-5:] == ['ונפלה', 'הארץ', 'הזאת', 'לכם', 'בנחלה'] and words('Ezek', 48, 29)[:5] == ['זאת', 'הארץ', 'אשר', 'תפילו', 'מנחלה'] and words('Ps', 16, 6)[:3] == ['חבלים', 'נפלו', 'לי'] and words('Josh', 23, 4)[:2] == ['ראו', 'הפלתי']
assert aramaic(34, 2)[12:17] == ['ארעא', 'די', 'תתפלג', 'לכון', 'באחסנא'] and onk_seats('תתפלג') == [(26, 53), (26, 55), (26, 56), (34, 2)] and words('Num', 26, 53)[:2] == ['לאלה', 'תחלק'] and words('Num', 26, 55)[:3] == ['אך', 'בגורל', 'יחלק']
assert U('לגבלתיה', 'לגבולתיה') == ['Josh 18:20', 'Josh 19:49', 'Num 34:12', 'Num 34:2'] and words('Josh', 19, 49)[:5] == ['ויכלו', 'לנחל', 'את', 'הארץ', 'לגבולתיה']
GB = lambda x, m: re.search(r'^(ו|ב|ל|מ|ה|וה|ול|ומ|וב)?(ה)?גב[ו]?ל', x) is not None and m is not None and 'Nc' in m
assert seats_in(GB) == [(2, 'לגבלתיה'), (3, 'גבול'), (4, 'הגבול'), (5, 'הגבול'), (6, 'וגבול'), (6, 'וגבול'), (6, 'גבול'), (7, 'גבול'), (8, 'הגבל'), (9, 'הגבל'), (9, 'גבול'), (10, 'לגבול'), (11, 'הגבל'), (11, 'הגבול'), (12, 'הגבול'), (12, 'לגבלתיה')] and cnt_in(GB) == 16
GBN = Counter(c for (b, c, v), ws in by.items() if b == 'Num' for x, m in ws if GB(x, m))
assert GBN == Counter({34: 16, 21: 6, 20: 4, 22: 2, 35: 2, 32: 1, 33: 1}) and sum(GBN.values()) == 32 and sum(1 for (b, c, v), ws in by.items() if b in T for x, m in ws if GB(x, m)) == 60
assert U('בנחלה', books=T) == ['Num 26:53', 'Num 34:2', 'Num 36:2'] and seats_in(lambda x, m: 'נחל' in x) == [(2, 'בנחלה'), (5, 'נחלה'), (13, 'תתנחלו'), (14, 'נחלתם'), (15, 'נחלתם'), (17, 'ינחלו'), (18, 'לנחל'), (29, 'לנחל')]

# 34:3-5 THE SOUTH SIDE — AND JOSHUA 15:1-4 (Judah's south border is the land's): twenty of the three verses' thirty-three distinct tokens stand in
# Joshua 15:1-4 — Edom, Zin, "from the end of the Salt Sea", "south of the ascent of Akrabbim", "and it shall pass to Zin", "south of
# Kadesh-barnea", Azmon, the brook of Egypt, "and it shall turn", "and it shall go out", the border; JOSHUA SPLITS HAZAR-ADDAR (one seat, 34:4)
# INTO TWO PLACES, "Hezron" and "Addar" (15:3), and adds "the bay that looks southward", "and it shall go up" twice and "Karka"; Azmon is written
# defective here (34:4 with the directional ending, 34:5 "from Azmon") and plene in Joshua (15:4) — three seats. "THE SOUTH SIDE" — the side-word
# is the TABERNACLE'S: eighteen Torah seats, twelve of them the court's and the boards' sides in Exodus 26-27, 36, 38 ("the south side" of the
# court, Exodus 27:9), four Leviticus's corners (the field's, the beard's), and Numbers 34:3, 35:5 (the Levite cities' four sides); Ezekiel gives
# every side that word (47:15-20, 48:28); Numbers gives it to the south alone and says "border" for the rest. "FROM THE WILDERNESS OF ZIN" with
# that prefix two seats — 13:21 ("they spied out the land from the wilderness of Zin to Rehob, to Lebo-hamath") and 34:3 — and "LEBO-HAMATH" in
# the defective spelling two seats, 13:21 and 34:8: THE SPIES WALKED THE BORDER'S LENGTH, its south start and its north point in the two words the
# chapter and the spies alone share (the plene "Lebo-hamath" at nine seats elsewhere); "the wilderness of Zin" seven Bible seats in all; "to Zin"
# (34:4, Joshua 15:3) shares its consonants with the shield at ten seats — the doubling dot in the nun tells the shield. "ALONG THE SIDES OF EDOM"
# — literally "on the hands of Edom", one seat; "on the hands of" three Torah seats (the other two the bracelets on Rebekah's hands, Genesis
# 24:30, and Reuben's "into my hands", 42:37); ONKELOS "on the BORDERS of Edom". "The south border" four seats (34:3; Joshua 15:2, 4, 18:19), "from
# the end of the Salt Sea" two (34:3, Joshua 15:2); THE SALT SEA nine Bible seats — Genesis 14:3 "the vale of Siddim, THAT IS the Salt Sea" (the
# identity idiom of "that is Kadesh"), Deuteronomy 3:17, Joshua's five and this chapter's two. "EASTWARD" four times in the chapter (34:3, 10, 11,
# 15), thirteen Torah seats; "EASTWARD, TOWARD THE SUNRISE" (34:15) five Bible seats — the court's east side (Exodus 27:13, 38:13), Judah's camp
# (2:3), the two and a half tribes' side, Joshua 19:13. "And it shall turn" ten Bible seats — this chapter's two and Joshua's five borders,
# Deuteronomy 2:1's turning about Mount Seir; "the ascent of Akrabbim" three seats (34:4; Joshua 15:3; Judges 1:36 the Amorite border); "and it
# shall pass to Zin" two (34:4, Joshua 15:3); KADESH-BARNEA ten seats (Numbers 32:8, 34:4; Deuteronomy 1:2, 19, 2:14, 9:23; Joshua 10:41, 14:6,
# 7, 15:3) — ONKELOS "Rekem Geah" at both Numbers seats (32:8, 34:4), the two-word name that sets it apart from bare Kadesh's "Rekem" (sitting
# 13's ten). "ITS GOINGS-OUT" — the border's outlet-word: the Torah's five seats ALL in this chapter (34:4, 5, 8, 9, 12); the Bible's other
# eighteen — fourteen in Joshua's border chapters, Ezekiel 48:30 (the city's), 1 Chronicles 5:16, Psalm 68:21, Proverbs 4:23. "THE BROOK OF EGYPT"
# with the directional ending one seat (34:5); the bare "brook of Egypt" five (Joshua 15:4, 47; 1 Kings 8:65 — Solomon's assembly "from
# Lebo-hamath to the brook of Egypt", THE BORDER'S TWO ENDS AS THE KINGDOM'S MEASURE; 2 Chronicles 7:8; Isaiah 27:12); the covenant's "RIVER of
# Egypt" (Genesis 15:18) is another word — the river-word stands nowhere in this chapter; "to the sea" with the article and the ending one
# Torah seat (34:5). ONKELOS: "the SIDE (wind) of the south" for the side-word (34:3 and 35:5), "from the ENDS of" for "from the end of".
assert words('Josh', 15, 1) == ['ויהי', 'הגורל', 'למטה', 'בני', 'יהודה', 'למשפחתם', 'אל', 'גבול', 'אדום', 'מדבר', 'צן', 'נגבה', 'מקצה', 'תימן'] and words('Josh', 15, 2) == ['ויהי', 'להם', 'גבול', 'נגב', 'מקצה', 'ים', 'המלח', 'מן', 'הלשן', 'הפנה', 'נגבה']
assert words('Josh', 15, 3) == ['ויצא', 'אל', 'מנגב', 'למעלה', 'עקרבים', 'ועבר', 'צנה', 'ועלה', 'מנגב', 'לקדש', 'ברנע', 'ועבר', 'חצרון', 'ועלה', 'אדרה', 'ונסב', 'הקרקעה'] and words('Josh', 15, 4) == ['ועבר', 'עצמונה', 'ויצא', 'נחל', 'מצרים', 'והיה', 'תצאות', 'הגבול', 'ימה', 'זה', 'יהיה', 'לכם', 'גבול', 'נגב']
S34 = {x for v in (3, 4, 5) for x in words('Num', 34, v)}; S15 = {x for v in (1, 2, 3, 4) for x in words('Josh', 15, v)}
assert len(S34) == 33 and sorted(S34 & S15) == ['אדום', 'ברנע', 'גבול', 'הגבול', 'המלח', 'והיה', 'ויצא', 'ונסב', 'ועבר', 'ים', 'לכם', 'למעלה', 'לקדש', 'מנגב', 'מצרים', 'מקצה', 'נגב', 'עקרבים', 'צן', 'צנה'] and len(S34 & S15) == 20
assert words('Num', 34, 3) == ['והיה', 'לכם', 'פאת', 'נגב', 'ממדבר', 'צן', 'על', 'ידי', 'אדום', 'והיה', 'לכם', 'גבול', 'נגב', 'מקצה', 'ים', 'המלח', 'קדמה']
assert phrase(['פאת', 'נגב'], None) == ['Ezek 48:28', 'Num 34:3', 'Num 35:5'] and len(U('פאת', 'לפאת', 'ולפאת', 'פאה', 'ופאת', books=T)) == 18 and [s for s in U('פאת', 'לפאת', 'ולפאת', 'ופאת') if s.startswith('Num')] == ['Num 34:3', 'Num 35:5'] and len([s for s in U('פאת', 'לפאת', 'ולפאת', 'ופאת', books=T) if s.startswith('Exod')]) == 12 and words('Exod', 27, 9)[4:7] == ['לפאת', 'נגב', 'תימנה']
assert phrase(['ממדבר', 'צן'], None) == ['Num 13:21', 'Num 34:3'] and words('Num', 13, 21) == ['ויעלו', 'ויתרו', 'את', 'הארץ', 'ממדבר', 'צן', 'עד', 'רחב', 'לבא', 'חמת'] and phrase(['לבא', 'חמת'], None) == ['Num 13:21', 'Num 34:8'] and phrase(['לבוא', 'חמת'], None) == ['1Chr 13:5', 'Ezek 47:20', 'Ezek 48:1', 'Josh 13:5', 'Judg 3:3'] and phrase(['מלבוא', 'חמת'], None) == ['1Kgs 8:65', '2Chr 7:8', '2Kgs 14:25', 'Amos 6:14']
assert sorted(phrase(['מדבר', 'צן'], None) + phrase(['ממדבר', 'צן'], None) + phrase(['במדבר', 'צן'], None)) == ['Deut 32:51', 'Josh 15:1', 'Num 13:21', 'Num 20:1', 'Num 27:14', 'Num 27:14', 'Num 33:36', 'Num 34:3'] and len(U('צנה')) == 12 and NP('צנה') == ['Josh 15:3', 'Num 34:4'] and PT('Num', 34, 4, 'צנה') == [NF('צִנָה')] and PT('Ps', 91, 4, 'צנה') == [NF('צִנָּה')]
assert phrase(['על', 'ידי', 'אדום'], None) == ['Num 34:3'] and phrase(['על', 'ידי']) == ['Gen 24:30', 'Gen 42:37', 'Num 34:3'] and aramaic(34, 3)[6:9] == ['על', 'תחומי', 'אדום'] and aramaic(34, 3)[2:4] == ['רוח', 'דרומא'] and onk_seats('רוח דרומא') == [(34, 3), (35, 5)] and aramaic(34, 3)[13] == 'מסיפי'
assert phrase(['גבול', 'נגב'], None) == ['Josh 15:2', 'Josh 15:4', 'Josh 18:19', 'Num 34:3'] and phrase(['מקצה', 'ים', 'המלח'], None) == ['Josh 15:2', 'Num 34:3'] and phrase(['ים', 'המלח'], None) == ['Deut 3:17', 'Gen 14:3', 'Josh 12:3', 'Josh 15:2', 'Josh 15:5', 'Josh 18:19', 'Josh 3:16', 'Num 34:12', 'Num 34:3'] and words('Gen', 14, 3)[-5:] == ['עמק', 'השדים', 'הוא', 'ים', 'המלח']
assert seats_in(lambda x, m: x == 'קדמה') == [(3, 'קדמה'), (10, 'קדמה'), (11, 'קדמה'), (15, 'קדמה')] and len(U('קדמה', books=T)) == 13 and phrase(['קדמה', 'מזרחה'], None) == ['Exod 27:13', 'Exod 38:13', 'Josh 19:13', 'Num 2:3', 'Num 34:15'] and words('Exod', 27, 13)[2:5] == ['לפאת', 'קדמה', 'מזרחה'] and words('Num', 2, 3)[:3] == ['והחנים', 'קדמה', 'מזרחה']
assert words('Num', 34, 4) == ['ונסב', 'לכם', 'הגבול', 'מנגב', 'למעלה', 'עקרבים', 'ועבר', 'צנה', 'והיה', 'תוצאתיו', 'מנגב', 'לקדש', 'ברנע', 'ויצא', 'חצר', 'אדר', 'ועבר', 'עצמנה'] and [(x, m) for x, m in by[('Num', 34, 4)] if x == 'ונסב'] == [('ונסב', 'HC/VNq3ms')]
assert U('ונסב') == ['2Chr 14:6', 'Deut 2:1', 'Jer 31:39', 'Josh 15:10', 'Josh 15:3', 'Josh 16:6', 'Josh 18:14', 'Josh 19:14', 'Num 34:4', 'Num 34:5'] and phrase(['למעלה', 'עקרבים'], None) == ['Josh 15:3', 'Num 34:4'] and words('Judg', 1, 36)[:4] == ['וגבול', 'האמרי', 'ממעלה', 'עקרבים'] and phrase(['ועבר', 'צנה'], None) == ['Josh 15:3', 'Num 34:4']
KB = sorted(set(phrase(['קדש', 'ברנע'], None) + phrase(['לקדש', 'ברנע'], None) + phrase(['מקדש', 'ברנע'], None) + phrase(['בקדש', 'ברנע'], None) + phrase(['וקדש', 'ברנע'], None)))
assert KB == ['Deut 1:19', 'Deut 1:2', 'Deut 2:14', 'Deut 9:23', 'Josh 10:41', 'Josh 14:6', 'Josh 14:7', 'Josh 15:3', 'Num 32:8', 'Num 34:4'] and onk_seats('רקם גיאה') == [(32, 8), (34, 4)] and aramaic(34, 4)[11:13] == ['לרקם', 'גיאה'] and len(onk_seats('רקם')) == 11
assert phrase(['חצר', 'אדר'], None) == ['Num 34:4'] and words('Josh', 15, 3)[12:15] == ['חצרון', 'ועלה', 'אדרה'] and U('עצמנה', 'מעצמון', 'עצמון', 'עצמונה') == ['Josh 15:4', 'Num 34:4', 'Num 34:5'] and PT('Num', 34, 4, 'עצמנה') == [NF('עַצְמֹֽנָה')] and words('Josh', 15, 4)[1] == 'עצמונה'
TOTS = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, _ in ws if re.search(r'^(ו|ה)?ת[ו]?צא[ו]?ת', x)})
assert [s for s in TOTS if s.split()[0] in T] == ['Num 34:12', 'Num 34:4', 'Num 34:5', 'Num 34:8', 'Num 34:9'] and len(TOTS) == 23 and len([s for s in TOTS if s.startswith('Josh')]) == 14 and [s for s in TOTS if s.split()[0] not in T and not s.startswith('Josh')] == ['1Chr 5:16', 'Ezek 48:30', 'Prov 4:23', 'Ps 68:21']
assert words('Num', 34, 5) == ['ונסב', 'הגבול', 'מעצמון', 'נחלה', 'מצרים', 'והיו', 'תוצאתיו', 'הימה'] and phrase(['נחלה', 'מצרים'], None) == ['Num 34:5'] and phrase(['נחל', 'מצרים'], None) == ['1Kgs 8:65', '2Chr 7:8', 'Isa 27:12', 'Josh 15:4', 'Josh 15:47'] and phrase(['נהר', 'מצרים'], None) == [] and words('Gen', 15, 18)[13:15] == ['מנהר', 'מצרים'] and words('1Kgs', 8, 65)[11:16] == ['מלבוא', 'חמת', 'עד', 'נחל', 'מצרים'] and U('הימה', books=T) == ['Num 34:5']
assert [x for (c, v) in SPAN for x, _ in by[('Num', 34, v)] if x in ('נהר', 'הנהר', 'פרת', 'הלבנון', 'לבנון', 'פלשתים', 'האחרון')] == [] and words('Deut', 11, 24)[12:16] == ['מן', 'הנהר', 'נהר', 'פרת'] and words('Josh', 1, 4)[4:8] == ['הנהר', 'הגדול', 'נהר', 'פרת'] and words('Exod', 23, 31)[3:8] == ['מים', 'סוף', 'ועד', 'ים', 'פלשתים']
assert [(x, m) for x, m in by[('Num', 34, 5)] if x == 'נחלה'] == [('נחלה', 'HNcmsc/Sh')] and [(x, m) for x, m in by[('Num', 34, 2)] if x == 'בנחלה'] == [('בנחלה', 'HR/Ncfsa')] and PT('Num', 34, 5, 'נחלה') == [NF('נַחְלָה')] and PT('Num', 34, 2, 'בנחלה') == [NF('בְּֽנַחֲלָה')] and aramaic(34, 5)[3:5] == ['לנחלא', 'דמצרים'] and aramaic(34, 2)[16] == 'באחסנא'

# 34:6-7 THE WEST — THE SEA AS THE DIRECTION: "and the west border" is "and the SEA border" — one token, the sea, stands SEVEN times in the chapter
# and means the west twice (34:6's first and last words), the great sea twice (34:6, 7), the Salt Sea twice (34:3, 12) and the sea of Chinnereth
# once (34:11); ONKELOS SPLITS THE TOKEN — "the west" (34:6 twice) against "the sea" (the great sea "the great sea", 34:6, 7; the Salt Sea "the
# sea of salt", 34:3, 12; "the sea of Gennesar", 34:11). "And the west border" two seats — 34:6 and Joshua 15:12 (Judah's: "and the west border,
# the great sea and its border" — the same three-word tail); "the west border" bare one seat. "THE GREAT SEA" spelled PLENE at 34:6 and DEFECTIVE
# at 34:7, the same phrase in adjacent verses — the defective form's one seat; the plene phrase eight Bible seats (Joshua 1:4, 9:1; Ezekiel's
# five); the covenant's "great river" (Genesis 15:18) is written defective too. 34:6's second "and its border": Onkelos adds the possessive
# ("and ITS border") — the sea's own border read as a thing beside the sea, the suffix the translation's.
assert words('Num', 34, 6) == ['וגבול', 'ים', 'והיה', 'לכם', 'הים', 'הגדול', 'וגבול', 'זה', 'יהיה', 'לכם', 'גבול', 'ים'] and words('Num', 34, 7) == ['וזה', 'יהיה', 'לכם', 'גבול', 'צפון', 'מן', 'הים', 'הגדל', 'תתאו', 'לכם', 'הר', 'ההר']
YAM = [(v, x, words('Num', 34, v)[i + 1] if i + 1 < len(words('Num', 34, v)) else None) for (c, v) in SPAN for i, (x, m) in enumerate(by[('Num', 34, v)]) if x in ('ים', 'הים') and m and 'Nc' in m]
assert YAM == [(3, 'ים', 'המלח'), (6, 'ים', 'והיה'), (6, 'הים', 'הגדול'), (6, 'ים', None), (7, 'הים', 'הגדל'), (11, 'ים', 'כנרת'), (12, 'ים', 'המלח')] and len(YAM) == 7
assert aramaic(34, 6) == ['ותחום', 'מערבא', 'ויהי', 'לכון', 'ימא', 'רבא', 'ותחומיה', 'דין', 'יהי', 'לכון', 'תחום', 'מערבא'] and onk_seats('ימא רבא') == [(34, 6), (34, 7)] and onk_seats('ימא דמלחא') == [(34, 3), (34, 12)] and onk_seats('גנסר') == [(34, 11)]
assert phrase(['וגבול', 'ים'], None) == ['Josh 15:12', 'Num 34:6'] and phrase(['גבול', 'ים'], None) == ['Num 34:6'] and words('Josh', 15, 12)[:6] == ['וגבול', 'ים', 'הימה', 'הגדול', 'וגבול', 'זה']
assert phrase(['הים', 'הגדול'], None) == ['Ezek 47:10', 'Ezek 47:15', 'Ezek 47:19', 'Ezek 47:20', 'Ezek 48:28', 'Josh 1:4', 'Josh 9:1', 'Num 34:6'] and phrase(['הים', 'הגדל'], None) == ['Num 34:7'] and PT('Num', 34, 6, 'הגדול') == [NF('הַגָּדוֹל')] and PT('Num', 34, 7, 'הגדל') == [NF('הַגָּדֹל')] == PT('Gen', 15, 18, 'הגדל') and words('Gen', 15, 18)[16:20] == ['הנהר', 'הגדל', 'נהר', 'פרת']

# 34:7-9 THE NORTH — THE BORDER'S OWN VERB: "YOU SHALL MARK OUT" (34:7, 8) and "you shall mark out for yourselves" (34:10) — the verb's THREE Bible
# seats, all in this chapter (the Piel twice, the Hitpael once); the consonants of "you shall mark out" are Proverbs' "do not DESIRE" at three
# seats (23:3, 23:6, 24:1 — the Hitpael of the desire-verb, the morphology and the points telling them apart); Joshua's borders use another verb
# for marking a line ("and the border was drawn", 15:9, 11, 18:14, 17). ONKELOS renders all three "direct yourselves" (the chapter's three seats
# of that verb). "The north border" two seats, both here (34:7, 9 — the north's own inclusio). MOUNT HOR — twelve Torah seats: ten the mountain of
# Aaron's death on Edom's border (20:22-27, 21:4, 33:37-41, Deuteronomy 32:50) and TWO the north border's (34:7, 8) — a second Mount Hor, the
# chukat runner's data row; ONKELOS SPELLS THE NAME TWO WAYS IN ADJACENT VERSES — "Hor" with the vav at 34:8 and 33:37-41, without it at 34:7 and
# in chapter 20-21: the split is the export's, not the mountains'. "ZEDAD" two seats (34:8; Ezekiel 47:15, both with the directional ending);
# "ZIPHRON" one seat; "HAZAR-ENAN" 34:9, 10 and Ezekiel 48:1, with Ezekiel 47:17's other spelling "Hazar-enon" — four seats, two spellings.
assert words('Num', 34, 8) == ['מהר', 'ההר', 'תתאו', 'לבא', 'חמת', 'והיו', 'תוצאת', 'הגבל', 'צדדה'] and words('Num', 34, 9) == ['ויצא', 'הגבל', 'זפרנה', 'והיו', 'תוצאתיו', 'חצר', 'עינן', 'זה', 'יהיה', 'לכם', 'גבול', 'צפון']
assert phrase(['גבול', 'צפון'], None) == ['Num 34:7', 'Num 34:9'] and U('תתאו', 'והתאויתם') == ['Num 34:10', 'Num 34:7', 'Num 34:8', 'Prov 23:3', 'Prov 23:6', 'Prov 24:1']
assert [(x, m) for x, m in by[('Num', 34, 7)] if x == 'תתאו'] == [('תתאו', 'HVpi2mp')] and [(x, m) for x, m in by[('Num', 34, 10)] if x == 'והתאויתם'] == [('והתאויתם', 'HC/Vtq2mp')] and [(x, m) for x, m in by[('Prov', 23, 3)] if x == 'תתאו'] == [('תתאו', 'HVtj2ms')] and PT('Num', 34, 7, 'תתאו') == [NF('תְּתָאוּ')] and PT('Prov', 23, 3, 'תתאו') == [NF('תִּתְאָו')]
assert U('ותאר', books=None) == ['Josh 15:11', 'Josh 15:9', 'Josh 18:14', 'Josh 18:17'] and words('Josh', 18, 14)[:2] == ['ותאר', 'הגבול'] and onk_seats('תכונון') == [(34, 7), (34, 8), (34, 10)]
HOR = sorted(phrase(['הר', 'ההר'], None) + phrase(['בהר', 'ההר'], None) + phrase(['מהר', 'ההר'], None))
assert HOR == ['Deut 32:50', 'Num 20:22', 'Num 20:23', 'Num 20:25', 'Num 20:27', 'Num 21:4', 'Num 33:37', 'Num 33:38', 'Num 33:39', 'Num 33:41', 'Num 34:7', 'Num 34:8'] and len(HOR) == 12
assert onk_seats('הור טורא') == [(33, 37), (33, 38), (33, 39), (33, 41), (34, 8)] and onk_seats('הר טורא') == [(20, 22), (20, 23), (20, 25), (20, 27), (21, 4), (34, 7)] and aramaic(34, 7)[-2:] == ['להר', 'טורא'] and aramaic(34, 8)[:2] == ['מהור', 'טורא']
assert aramaic(34, 8)[3:5] == ['למטי', 'חמת'] and onk_seats('למטי חמת') == [(13, 21), (34, 8)] and U('צדדה') == ['Ezek 47:15', 'Num 34:8'] and U('זפרנה', 'זפרון') == ['Num 34:9'] and phrase(['חצר', 'עינן'], None) == ['Ezek 48:1', 'Num 34:9'] and phrase(['מחצר', 'עינן'], None) == ['Num 34:10'] and phrase(['חצר', 'עינון'], None) == ['Ezek 47:17']

# 34:10-12 THE EAST: "SHEPHAM" two seats (34:10, 11), its consonants the leper's covered "upper lip" (Leviticus 13:45; Ezekiel 24:17, 22; Micah
# 3:7) — the shin's dot against the sin's tells the place from the lip; "the Riblah" with the article one seat (the exile's Riblah "in the land
# of Hamath" ten seats without it, in Kings and Jeremiah); "east of AIN" one seat — Ain a proper name at two Torah seats (34:11 and Genesis 14:7's
# En-mishpat), the consonants "the eye" at Ezekiel 12:12; "AND IT SHALL REACH upon the shoulder of the sea of Chinnereth" — the verb is the
# BLOTTING verb: the token's four Bible seats are the sotah's "he shall blot [the curses] into the water of bitterness" (5:23), "the LORD shall
# blot out his name" (Deuteronomy 29:19), "the Lord GOD shall wipe away tears" (Isaiah 25:8) and this border's reaching — one pointing at all
# four; ONKELOS "and it shall REACH" here against "and he shall BLOT" at 5:23. "THE SHOULDER" — fifteen Torah tokens: the court's gate-sides
# (Exodus 27:14, 15; 38:14, 15), the ephod's shoulder-pieces (Exodus 28, 39 — nine), the Kohathites' "on the shoulder they carry" (7:9), and this
# one shore; Joshua's border chapters say it eight times (15:8, 10, 11; 18:12, 13, 16, 18, 19). "THE SEA OF CHINNERETH" two seats (34:11; Joshua
# 13:27), the name seven (Deuteronomy 3:17, Joshua 11:2, 12:3, 19:35 a city, 1 Kings 15:20 — "Chinneroth" thrice); ONKELOS "the sea of GENNESAR",
# its one seat in Onkelos Numbers. "TO THE JORDAN" with the article and the ending — the Torah's one seat (Judges 8:4, 2 Kings 2:6, 6:4 the
# others). THE LOOP: the south began "from the end of the Salt Sea eastward" (34:3) and the east ends "its goings-out shall be the Salt Sea"
# (34:12) — the border closes on its first two tokens; "round about" — ONKELOS doubles it ("round, round", fifteen seats in Onkelos Numbers).
assert words('Num', 34, 10) == ['והתאויתם', 'לכם', 'לגבול', 'קדמה', 'מחצר', 'עינן', 'שפמה'] and words('Num', 34, 11) == ['וירד', 'הגבל', 'משפם', 'הרבלה', 'מקדם', 'לעין', 'וירד', 'הגבול', 'ומחה', 'על', 'כתף', 'ים', 'כנרת', 'קדמה'] and words('Num', 34, 12) == ['וירד', 'הגבול', 'הירדנה', 'והיו', 'תוצאתיו', 'ים', 'המלח', 'זאת', 'תהיה', 'לכם', 'הארץ', 'לגבלתיה', 'סביב']
assert U('שפמה', 'משפם', 'שפם') == ['Ezek 24:17', 'Ezek 24:22', 'Lev 13:45', 'Mic 3:7', 'Num 34:10', 'Num 34:11'] and PT('Num', 34, 10, 'שפמה') == [NF('שְׁפָֽמָה')] and PT('Lev', 13, 45, 'שפם') == [NF('שָׂפָם')] and U('הרבלה') == ['Num 34:11'] and len(U('רבלה', 'רבלתה', 'ברבלה', 'ברבלתה')) == 10 and words('2Kgs', 23, 33)[3:6] == ['ברבלה', 'בארץ', 'חמת']
assert U('לעין') == ['Ezek 12:12', 'Num 34:11'] and sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, m in ws if x in ('עין', 'לעין', 'ועין', 'מעין') and m and 'Np' in m}) == ['Gen 14:7 עין', 'Num 34:11 לעין'] and PT('Num', 34, 11, 'לעין') == [NF('לָעָיִן')] and PT('Ezek', 12, 12, 'לעין') == [NF('לַעַיִן')]
assert U('ומחה') == ['Deut 29:19', 'Isa 25:8', 'Num 34:11', 'Num 5:23'] and all(PT(b, c, v, 'ומחה') == [NF('וּמָחָה')] for b, c, v in (('Num', 34, 11), ('Num', 5, 23), ('Deut', 29, 19), ('Isa', 25, 8))) and words('Num', 5, 23)[6:10] == ['ומחה', 'אל', 'מי', 'המרים'] and aramaic(5, 23)[6] == 'וימחוק' and aramaic(34, 11)[8] == 'וימטי'
KTF = sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, _ in ws if x.startswith(('כתף', 'כתפ', 'לכתף', 'ולכתף', 'הכתף', 'בכתף'))})
assert KTF == ['Exod 27:14 לכתף', 'Exod 27:15 ולכתף', 'Exod 28:12 כתפיו', 'Exod 28:12 כתפת', 'Exod 28:25 כתפות', 'Exod 28:27 כתפות', 'Exod 28:7 כתפת', 'Exod 38:14 הכתף', 'Exod 38:15 ולכתף', 'Exod 39:18 כתפת', 'Exod 39:20 כתפת', 'Exod 39:4 כתפת', 'Exod 39:7 כתפת', 'Num 34:11 כתף', 'Num 7:9 בכתף'] and len(KTF) == 15
assert [s for s in U('כתף') if s.startswith('Josh')] == ['Josh 15:10', 'Josh 15:11', 'Josh 15:8', 'Josh 18:12', 'Josh 18:13', 'Josh 18:16', 'Josh 18:18', 'Josh 18:19'] and 'Num 34:11' in U('כתף') and len(U('כתף')) == 28 and words('Exod', 27, 14)[3:5] == ['קלעים', 'לכתף'] and words('Num', 7, 9)[-3:] == ['עלהם', 'בכתף', 'ישאו']
assert phrase(['ים', 'כנרת'], None) == ['Josh 13:27', 'Num 34:11'] and U('כנרת', 'כנרות', 'מכנרת', 'וכנרת') == ['1Kgs 15:20', 'Deut 3:17', 'Josh 11:2', 'Josh 12:3', 'Josh 13:27', 'Josh 19:35', 'Num 34:11'] and words('Deut', 3, 17)[3] == 'מכנרת' and aramaic(34, 11)[11:13] == ['ים', 'גנסר']
assert U('הירדנה') == ['2Kgs 2:6', '2Kgs 6:4', 'Judg 8:4', 'Num 34:12'] and words('Num', 34, 3)[14:16] == words('Num', 34, 12)[5:7] == ['ים', 'המלח'] and aramaic(34, 12)[-2:] == ['סחור', 'סחור'] and len(onk_seats('סחור סחור')) == 15
assert phrase(['זה', 'יהיה', 'לכם', 'גבול'], None) == ['Josh 15:4', 'Num 34:6', 'Num 34:9'] and phrase(['וזה', 'יהיה', 'לכם', 'גבול'], None) == ['Num 34:7'] and words('Josh', 15, 4)[-5:] == ['זה', 'יהיה', 'לכם', 'גבול', 'נגב'] and sum(1 for (c, v) in SPAN for x in words('Num', 34, v) if x == 'לכם') == 12 and [(v, words('Josh', 15, v).count('לכם')) for v in range(1, 64) if ('Josh', 15, v) in by and 'לכם' in words('Josh', 15, v)] == [(4, 1)]

# EZEKIEL'S BORDERS AGAINST THE CHAPTER'S (47:13-20, 48:1, 28 — the tokens): twenty-three tokens shared (the border, the great sea, the side-word,
# the south, the north, Hamath, Hazar-enan, Zedad, "from the end of", the brook, "this is the land"...); Ezekiel's opening "this is the border by
# which you shall INHERIT the land" carries 34:13's Hitpael, and 47:14 "this land shall fall to you as an inheritance" carries 34:2's clause;
# EZEKIEL RUNS THE SIDES FROM THE NORTH (47:15-17), then east (47:18), south (47:19), west (47:20) — Numbers from the south (34:3), west (34:6),
# north (34:7), east (34:10): the two orders, OBSERVED.
N34 = {x for v in range(3, 13) for x in words('Num', 34, v)}; EZ = {x for v in range(13, 21) for x in words('Ezek', 47, v)} | set(words('Ezek', 48, 28)) | set(words('Ezek', 48, 1))
assert len(N34 & EZ) == 23 and {'גבול', 'הגדול', 'פאת', 'נגב', 'צפון', 'חמת', 'עינן', 'צדדה', 'מקצה', 'נחלה'} <= (N34 & EZ)
assert words('Ezek', 47, 13)[4:10] == ['גה', 'גבול', 'אשר', 'תתנחלו', 'את', 'הארץ'] and [(v, x, words('Ezek', 47, v)[i + 1]) for v in range(15, 21) for i, x in enumerate(words('Ezek', 47, v)) if x in ('פאת', 'ופאת', 'לפאת') and i + 1 < len(words('Ezek', 47, v))] == [(15, 'לפאת', 'צפונה'), (17, 'פאת', 'צפון'), (18, 'ופאת', 'קדים'), (18, 'פאת', 'קדימה'), (19, 'ופאת', 'נגב'), (19, 'פאת', 'תימנה'), (20, 'ופאת', 'ים'), (20, 'פאת', 'ים')]

# 34:13-15 MOSES' RESTATEMENT — ONE TRIBE-NOUN: the chapter says "tribe" with the staff-word EIGHTEEN times (34:13 twice, 34:14 three, 34:15
# twice, 34:18, and the roster's ten) and the other tribe-word NEVER — where 32:33 gave "the half tribe of Manasseh" with the other word (the
# book's six seats of that word: 4:18, 18:2, 24:2, 24:17, 32:33, 36:3; the staff-word 103 times as "tribe" in Numbers); Joshua carries both —
# 14:2 QUOTES 34:13's six words "to the nine tribes and the half tribe" whole under the receipt "as the LORD commanded by the hand of Moses" (the
# run citing the spec outside the Torah), 13:7 says the same with the other word; "NINE" in the construct stands THREE times in the Bible, every
# one of the nine tribes (34:13; Joshua 13:7, 14:2). "YOU SHALL INHERIT" — the Hitpael's Torah seats: Leviticus 25:46 (the slaves held), 32:18,
# 33:54 twice, 34:13; Ezekiel 47:13 and Isaiah 14:2 outside; "by lot" four Torah seats (26:55, 33:54, 34:13, 36:2), fifteen in the Bible; "which
# the LORD commanded to give" Leviticus 7:36 (the priests' portion) and 34:13; 36:2 "my lord was commanded by the LORD to give". "THE REUBENITE
# ... THE GADITE" (34:14) — the two gentilics in one verse: the pair's FIRST seat, then Deuteronomy 3:12, 16, 4:43, 29:7, Joshua 1:12, 12:6, 13:8,
# 22:1 and four in Kings and Chronicles (thirteen); "the half tribe of Manasseh" with the staff-word here, Joshua 21:5, 6, 27 and 1 Chronicles
# 6:56 (the Levite cities' rows), with the other word at 32:33 and Joshua's narrative; "by their fathers' houses" twice — the census formula
# (thirty-nine Torah seats, twenty-eight in Numbers); "THEY TOOK THEIR INHERITANCE" four Bible seats — 34:14, 34:15 and Joshua's two (13:8 the
# Reubenite and the Gadite, 18:7 Gad and Reuben and the half tribe): always the two and a half; "beyond the Jordan at Jericho" two seats — 22:1's
# arrival and this; "eastward, toward the sunrise" the court's phrase (above). ONKELOS: one Aramaic tribe-word for both Hebrew words (18 here;
# 32:33's "half tribe" rendered as 34:14's), "two tribes" at 34:13 and 34:15 alone.
assert words('Num', 34, 13) == ['ויצו', 'משה', 'את', 'בני', 'ישראל', 'לאמר', 'זאת', 'הארץ', 'אשר', 'תתנחלו', 'אתה', 'בגורל', 'אשר', 'צוה', 'יהוה', 'לתת', 'לתשעת', 'המטות', 'וחצי', 'המטה'] and words('Num', 34, 14) == ['כי', 'לקחו', 'מטה', 'בני', 'הראובני', 'לבית', 'אבתם', 'ומטה', 'בני', 'הגדי', 'לבית', 'אבתם', 'וחצי', 'מטה', 'מנשה', 'לקחו', 'נחלתם'] and words('Num', 34, 15) == ['שני', 'המטות', 'וחצי', 'המטה', 'לקחו', 'נחלתם', 'מעבר', 'לירדן', 'ירחו', 'קדמה', 'מזרחה']
MT = lambda x, m: re.search(r'^(ו|ל|ב|מ|ול)?(ה)?(מטה|מטות)$', x) is not None and m is not None and 'Nc' in m
assert cnt_in(MT) == 18 and seats_in(MT) == [(13, 'המטות'), (13, 'המטה'), (14, 'מטה'), (14, 'ומטה'), (14, 'מטה'), (15, 'המטות'), (15, 'המטה'), (18, 'ממטה'), (19, 'למטה'), (20, 'ולמטה'), (21, 'למטה'), (22, 'ולמטה'), (23, 'למטה'), (24, 'ולמטה'), (25, 'ולמטה'), (26, 'ולמטה'), (27, 'ולמטה'), (28, 'ולמטה')] and seats_in(lambda x, m: 'שבט' in x) == []
assert sorted({f'{c}:{v} {x}' for (b, c, v), ws in by.items() if b == 'Num' for x, _ in ws if 'שבט' in x}) == ['18:2 שבט', '24:17 שבט', '24:2 לשבטיו', '32:33 שבט', '36:3 שבטי', '4:18 שבט'] and sum(1 for (b, c, v), ws in by.items() if b == 'Num' for x, m in ws if MT(x, m)) == 103 and words('Num', 32, 33)[7:10] == ['ולחצי', 'שבט', 'מנשה']
assert phrase(['לתשעת', 'המטות', 'וחצי', 'המטה'], None) == ['Josh 14:2', 'Num 34:13'] and phrase(['לתשעת', 'השבטים', 'וחצי', 'השבט'], None) == ['Josh 13:7'] and U('תשעת', 'לתשעת', 'ותשעת') == ['Josh 13:7', 'Josh 14:2', 'Num 34:13'] and words('Josh', 14, 2) == ['בגורל', 'נחלתם', 'כאשר', 'צוה', 'יהוה', 'ביד', 'משה', 'לתשעת', 'המטות', 'וחצי', 'המטה']
assert sorted({f'{b} {c}:{v} {x} {m}' for (b, c, v), ws in by.items() if b in T for x, m in ws if 'נחל' in x and m and re.search(r'Vt', m)}) == ['Lev 25:46 והתנחלתם HC/Vtq2mp', 'Num 32:18 התנחל HVtc', 'Num 33:54 והתנחלתם HC/Vtq2mp', 'Num 33:54 תתנחלו HVti2mp', 'Num 34:13 תתנחלו HVti2mp'] and U('תתנחלו', 'והתנחלתם', 'והתנחלום') == ['Ezek 47:13', 'Isa 14:2', 'Lev 25:46', 'Num 33:54', 'Num 34:13']
assert U('בגורל', books=T) == ['Num 26:55', 'Num 33:54', 'Num 34:13', 'Num 36:2'] and len(U('בגורל')) == 15 and phrase(['אשר', 'צוה', 'יהוה', 'לתת']) == ['Lev 7:36', 'Num 34:13'] and words('Num', 36, 2)[1:6] == ['את', 'אדני', 'צוה', 'יהוה', 'לתת']
RG = sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if {'הראובני', 'והראובני', 'לראובני', 'ולראובני'} & {x for x, _ in ws} and {'הגדי', 'והגדי', 'לגדי', 'ולגדי'} & {x for x, _ in ws}})
assert RG == ['1Chr 12:38', '1Chr 26:32', '1Chr 5:26', '2Kgs 10:33', 'Deut 29:7', 'Deut 3:12', 'Deut 3:16', 'Deut 4:43', 'Josh 12:6', 'Josh 13:8', 'Josh 1:12', 'Josh 22:1', 'Num 34:14'] and len(RG) == 13 and [(x, m) for x, m in by[('Num', 34, 14)] if x in ('הראובני', 'הגדי')] == [('הראובני', 'HTd/Ngmsa'), ('הגדי', 'HTd/Ngmsa')] and words('Num', 26, 7)[:3] == ['אלה', 'משפחת', 'הראובני']
assert phrase(['וחצי', 'מטה', 'מנשה'], None) == ['Num 34:14'] and words('Josh', 21, 5)[8:11] == ['ומחצי', 'מטה', 'מנשה'] and words('Josh', 21, 6)[9:12] == ['ומחצי', 'מטה', 'מנשה'] and phrase(['מחצי', 'מטה', 'מנשה'], None) == ['Josh 21:27'] and phrase(['חצי', 'מטה', 'מנשה'], None) == ['1Chr 6:56'] and phrase(['וחצי', 'שבט', 'המנשה'], None) == ['Josh 18:7', 'Josh 22:10', 'Josh 22:11', 'Josh 22:21', 'Josh 22:9', 'Josh 4:12']
assert len(U('אבתם', books=T)) == 39 and len([s for s in phrase(['לבית', 'אבתם']) if s.startswith('Num')]) == 28 and phrase(['לקחו', 'נחלתם'], None) == ['Josh 13:8', 'Josh 18:7', 'Num 34:14', 'Num 34:15'] and phrase(['מעבר', 'לירדן', 'ירחו'], None) == ['Num 22:1', 'Num 34:15'] and phrase(['מעבר', 'לירדן']) == ['Num 22:1', 'Num 32:19', 'Num 32:32', 'Num 34:15', 'Num 35:14'] and len(phrase(['על', 'ירדן', 'ירחו'])) == 7
assert sum(1 for v in range(1, 30) for x in aramaic(34, v) if 'שבט' in x) == 18 and onk_seats('שבטין') == [(34, 13), (34, 15)] and aramaic(32, 33)[7:10] == ['ולפלגות', 'שבטא', 'דמנשה'] and aramaic(34, 14)[12:15] == ['ופלגות', 'שבטא', 'דמנשה'] and onk_seats('פלגות שבטא') == [(32, 33), (34, 13), (34, 14), (34, 15)] and aramaic(34, 15)[:2] == ['תרין', 'שבטין']

# 34:16-18 THE COMMISSION: "THESE ARE THE NAMES OF THE MEN" — the roster heading at four Bible seats, all Numbers': the census's standing men
# (1:5), the spies (13:16), the dividers (34:17) and the dividers again (34:19). THE ONE ROOT IN THREE STEMS — "inherit" in the chapter eight
# times: the Hitpael "you shall inherit for yourselves" (34:13), the Qal "who shall divide the land for you" (34:17) and "to divide the land"
# (34:18), the PIEL "to give the children of Israel their inheritance" (34:29), and the nouns (34:2, 14, 15 — and 34:5's BROOK, the inheritance's
# consonants with a masculine noun's points: the homograph the morphology decides, Onkelos giving it another word); THE PIEL'S FOUR BIBLE SEATS —
# 34:29 and three RUNS in Joshua: 13:32 "which Moses divided", 14:1 "which Eleazar the priest and Joshua son of Nun and the heads of the fathers
# divided to them", 19:51 "which Eleazar the priest and Joshua son of Nun and the heads of the fathers divided by lot in Shiloh before the LORD";
# the Qal's "to divide the land" runs at Joshua 19:49 ("they finished dividing the land by its borders" — 34:18's and 34:12's words); THE OBJECT
# SWITCHES WITH THE STEM — the land at 34:17-18, the people at 34:29 (one seat). "ELEAZAR THE PRIEST AND JOSHUA SON OF NUN" as one phrase three
# seats — 34:17 and Joshua's two runs (14:1, 19:51); 32:28 and Joshua 21:1 name the pair with the object marker and "to" between. "ONE PRINCE,
# ONE PRINCE from a tribe" — THE DISTRIBUTIVE DOUBLING: the same form sends the spies ("one man, one man for a tribe", 13:2), gives the rods ("a
# rod for one prince, a rod for one prince", 17:21), orders the altar's dedication ("one prince a day, one prince a day", 7:11), and in Joshua
# takes the twelve stones (3:12, 4:2, 4:4) and the embassy's ten princes ("one prince, one prince for a father's house", 22:14); the parser reads
# each doubling as two ones. "You shall take" — the appointing verb; "from a tribe" three Torah seats (34:18; 36:7, 9). ONKELOS: "one chief, one
# chief from a tribe" (34:18) as at 7:11 and 17:21 — and ONE ARAMAIC WORD, "great", for the great sea (34:6, 7) and for the prince (34:18, 22-28).
assert words('Num', 34, 17) == ['אלה', 'שמות', 'האנשים', 'אשר', 'ינחלו', 'לכם', 'את', 'הארץ', 'אלעזר', 'הכהן', 'ויהושע', 'בן', 'נון'] and words('Num', 34, 18) == ['ונשיא', 'אחד', 'נשיא', 'אחד', 'ממטה', 'תקחו', 'לנחל', 'את', 'הארץ'] and words('Num', 34, 29) == ['אלה', 'אשר', 'צוה', 'יהוה', 'לנחל', 'את', 'בני', 'ישראל', 'בארץ', 'כנען']
assert phrase(['שמות', 'האנשים'], None) == ['Num 13:16', 'Num 1:5', 'Num 34:17', 'Num 34:19'] and phrase(['אלה', 'שמות']) == ['Gen 36:10', 'Num 13:16', 'Num 34:17', 'Num 3:3'] and len(phrase(['ואלה', 'שמות'])) == 10 and words('Num', 1, 5)[:6] == ['ואלה', 'שמות', 'האנשים', 'אשר', 'יעמדו', 'אתכם'] and words('Num', 13, 16)[:5] == ['אלה', 'שמות', 'האנשים', 'אשר', 'שלח']
assert [(v, x, m) for (c, v) in SPAN for x, m in by[('Num', 34, v)] if 'נחל' in x] == [(2, 'בנחלה', 'HR/Ncfsa'), (5, 'נחלה', 'HNcmsc/Sh'), (13, 'תתנחלו', 'HVti2mp'), (14, 'נחלתם', 'HNcfsc/Sp3mp'), (15, 'נחלתם', 'HNcfsc/Sp3mp'), (17, 'ינחלו', 'HVqi3mp'), (18, 'לנחל', 'HR/Vqc'), (29, 'לנחל', 'HR/Vpc')]
assert sorted({f'{b} {c}:{v} {x} {m}' for (b, c, v), ws in by.items() for x, m in ws if 'נחל' in x and m and re.search(r'^H(C/|R/)?Vp', m)}) == ['Josh 13:32 נחל HVpp3ms', 'Josh 14:1 נחלו HVpp3cp', 'Josh 19:51 נחלו HVpp3cp', 'Num 34:29 לנחל HR/Vpc']
assert wm('Josh', 14, 1)[:15] == [('ואלה', 'HC/Pdxcp'), ('אשר', 'HTr'), ('נחלו', 'HVqp3cp'), ('בני', 'HNcmpc'), ('ישראל', 'HNp'), ('בארץ', 'HR/Ncbsc'), ('כנען', 'HNp'), ('אשר', 'HTr'), ('נחלו', 'HVpp3cp'), ('אותם', 'HTo/Sp3mp'), ('אלעזר', 'HNp'), ('הכהן', 'HTd/Ncmsa'), ('ויהושע', 'HC/Np'), ('בן', 'HNcmsc'), ('נון', 'HNp')] and words('Josh', 19, 51)[:9] == ['אלה', 'הנחלת', 'אשר', 'נחלו', 'אלעזר', 'הכהן', 'ויהושע', 'בן', 'נון'] and words('Josh', 13, 32)[:4] == ['אלה', 'אשר', 'נחל', 'משה']
assert phrase(['לנחל', 'את', 'הארץ'], None) == ['Josh 19:49', 'Num 34:18'] and phrase(['לנחל', 'את', 'בני', 'ישראל'], None) == ['Num 34:29'] and phrase(['אלעזר', 'הכהן', 'ויהושע', 'בן', 'נון'], None) == ['Josh 14:1', 'Josh 19:51', 'Num 34:17'] and words('Num', 32, 28)[:10] == ['ויצו', 'להם', 'משה', 'את', 'אלעזר', 'הכהן', 'ואת', 'יהושע', 'בן', 'נון'] and words('Josh', 21, 1)[5:11] == ['אלעזר', 'הכהן', 'ואל', 'יהושע', 'בן', 'נון']
assert phrase(['נשיא', 'אחד'], None) == ['Josh 22:14', 'Num 34:18', 'Num 7:11'] and phrase(['נשיא', 'אחד', 'נשיא', 'אחד'], None) == ['Josh 22:14'] and words('Num', 7, 11)[4:10] == ['נשיא', 'אחד', 'ליום', 'נשיא', 'אחד', 'ליום'] and words('Num', 17, 21)[9:15] == ['מטה', 'לנשיא', 'אחד', 'מטה', 'לנשיא', 'אחד'] and phrase(['איש', 'אחד', 'איש', 'אחד'], None) == ['Josh 3:12', 'Josh 4:2', 'Josh 4:4', 'Num 13:2'] and words('Num', 13, 2)[12:17] == ['איש', 'אחד', 'איש', 'אחד', 'למטה'] and words('Josh', 22, 14)[3:9] == ['נשיא', 'אחד', 'נשיא', 'אחד', 'לבית', 'אב']
assert U('ממטה', books=T) == ['Num 34:18', 'Num 36:7', 'Num 36:9'] and len(U('תקחו', books=T)) == 12 and aramaic(34, 18)[:5] == ['ורבא', 'חד', 'רבא', 'חד', 'משבטא'] and aramaic(7, 11)[3:7] == ['רבא', 'חד', 'ליומא', 'רבא'] and aramaic(17, 21)[9:12] == ['חטרא', 'לרבא', 'חד'] and aramaic(13, 2)[12:16] == ['גברא', 'חד', 'גברא', 'חד']
assert [(v, x) for v in range(1, 30) for x in aramaic(34, v) if x == 'רבא'] == [(6, 'רבא'), (7, 'רבא'), (18, 'רבא'), (22, 'רבא'), (23, 'רבא'), (24, 'רבא'), (25, 'רבא'), (26, 'רבא'), (27, 'רבא'), (28, 'רבא')] and aramaic(34, 17)[3:7] == ['די', 'יחסנון', 'לכון', 'ית'] and aramaic(34, 18)[6] == aramaic(34, 29)[4] == 'לאחסנא' and [(v, x) for v in range(1, 30) for x in aramaic(34, v) if 'חסנ' in x] == [(2, 'באחסנא'), (13, 'תתחסנון'), (14, 'אחסנתהון'), (15, 'אחסנתהון'), (17, 'יחסנון'), (18, 'לאחסנא'), (29, 'לאחסנא')]

# 34:19-28 THE ROSTER — TEN PRINCES: "FOR THE TRIBE OF JUDAH, CALEB SON OF JEPHUNNEH" — 34:19's five words are 13:6's five, the spy's line
# repeated at the dividers' (the phrase's two seats); Caleb son of Jephunneh eight Torah seats (13:6, 14:6, 30, 38, 26:65, 32:12, 34:19,
# Deuteronomy 1:36), Caleb thirty-six in the Bible, "the Kenizzite" his at 32:12 and Joshua 14:6, 14 (Genesis 15:19 the people); THE TWO SURVIVORS
# OF THE SPIES are the only persons of chapter 13's roster in this chapter's — Joshua son of Nun (34:17; 13:8 "Hoshea son of Nun") and Caleb —
# the two of 14:30, 14:38, 26:65, 32:12; NO PRINCE OF CHAPTER 1 is among the ten (their sons' generation), and one father's name is shared:
# AMMIHUD — Elishama's father (Ephraim, 1:10 and its four repeats), Shemuel's (Simeon, 34:20) and Pedahel's (Naphtali, 34:28): three tribes, nine
# Bible seats (Chronicles' two the rest). THE NAMES' SEATS (the morphology's proper nouns, computed): EIGHT stand nowhere else in the Bible —
# Elidad, Jogli, Ephod, Shiphtan, Parnach, Azzan, Ahihud, Pedahel; SHEMUEL (Simeon's prince) is the FIRST seat of the prophet's name (one hundred
# twenty verses, the prophet's but for this prince's and an Issacharite's, 1 Chronicles 7:2); Kemuel is Nahor's son's name (Genesis 22:21) and a Levite ruler's; Elizaphan the Kohathite prince's
# (3:30, Uzziel's son); Bukki a priest's (1 Chronicles 5:31; Ezra 7:4); Paltiel Michal's husband's (2 Samuel 3:15); Hanniel an Asherite's;
# Shelomi a Nethinim family's; CHISLON (Benjamin's prince's father) is a place on Judah's north border — "Mount Jearim, THAT IS Chesalon" (Joshua
# 15:10, the identity idiom). SEVEN of the ten princes carry God's name (the -el names: Shemuel, Elidad, Hanniel, Kemuel, Elizaphan, Paltiel,
# Pedahel), none of the fathers; "son" eleven times (Joshua's and the ten). THE TITLE DROPPED FOR THREE: "prince" is written at seven rows
# (Dan through Naphtali, 34:22-28) and not at Judah's, Simeon's or Benjamin's (34:19-21); "the children of" absent at Judah's and Benjamin's
# rows alone; the conjunction absent at Benjamin's (34:21) and at Joseph's heading (34:23 "of the children of Joseph", the form of 1:10 and
# 1:32). THE ORDER — Judah, Simeon, Benjamin, Dan, Manasseh, Ephraim, Zebulun, Issachar, Asher, Naphtali — matches NO other roster of the Torah
# (computed on every one: the census's two, the camp's, the dedication's, the march's, the spies', the second census's, Genesis 46, 49, Exodus
# 1, Deuteronomy 27, 33): Manasseh before Ephraim as in the second census (26:28-37) and Genesis 46:20 (Joseph's sons by birth) alone, Zebulun before Issachar as in Jacob's blessing (Genesis
# 49:13-14) and Moses' (Deuteronomy 33:18) alone, and the four northern tribes in the order Joshua's lots fall — Zebulun (19:10), Issachar
# (19:17), Asher (19:24), Naphtali (19:32); the cause unnamed, the declared shelf silent.
ROST = {v: words('Num', 34, v) for v in range(19, 29)}
assert ROST == {19: ['ואלה', 'שמות', 'האנשים', 'למטה', 'יהודה', 'כלב', 'בן', 'יפנה'], 20: ['ולמטה', 'בני', 'שמעון', 'שמואל', 'בן', 'עמיהוד'], 21: ['למטה', 'בנימן', 'אלידד', 'בן', 'כסלון'], 22: ['ולמטה', 'בני', 'דן', 'נשיא', 'בקי', 'בן', 'יגלי'], 23: ['לבני', 'יוסף', 'למטה', 'בני', 'מנשה', 'נשיא', 'חניאל', 'בן', 'אפד'], 24: ['ולמטה', 'בני', 'אפרים', 'נשיא', 'קמואל', 'בן', 'שפטן'], 25: ['ולמטה', 'בני', 'זבולן', 'נשיא', 'אליצפן', 'בן', 'פרנך'], 26: ['ולמטה', 'בני', 'יששכר', 'נשיא', 'פלטיאל', 'בן', 'עזן'], 27: ['ולמטה', 'בני', 'אשר', 'נשיא', 'אחיהוד', 'בן', 'שלמי'], 28: ['ולמטה', 'בני', 'נפתלי', 'נשיא', 'פדהאל', 'בן', 'עמיהוד']}
assert [v for v, w in ROST.items() if 'נשיא' in w] == [22, 23, 24, 25, 26, 27, 28] and [v for v, w in ROST.items() if 'בני' not in w] == [19, 21] and [v for v, w in ROST.items() if not w[0].startswith('ו')] == [21, 23] and sum(1 for v in range(17, 29) for x in words('Num', 34, v) if x == 'בן') == 11
assert phrase(['למטה', 'יהודה', 'כלב', 'בן', 'יפנה']) == ['Num 13:6', 'Num 34:19'] and words('Num', 13, 6) == ['למטה', 'יהודה', 'כלב', 'בן', 'יפנה'] and sorted(phrase(['כלב', 'בן', 'יפנה']) + phrase(['וכלב', 'בן', 'יפנה'])) == ['Deut 1:36', 'Num 13:6', 'Num 14:30', 'Num 14:38', 'Num 14:6', 'Num 26:65', 'Num 32:12', 'Num 34:19'] and len(NPX('כלב')) == 36 and U('הקנזי') == ['Gen 15:19', 'Josh 14:14', 'Josh 14:6', 'Num 32:12']
SP_NP = {x for v in range(4, 16) for x, m in by[('Num', 13, v)] if m and 'Np' in m}; PR_NP = {x for v in range(17, 29) for x, m in by[('Num', 34, v)] if m and 'Np' in m}; C1_NP = {x for v in range(5, 16) for x, m in by[('Num', 1, v)] if m and 'Np' in m}
TRIBES = {'אפרים', 'אשר', 'בנימן', 'דן', 'זבולן', 'יהודה', 'יוסף', 'יששכר', 'מנשה', 'נפתלי', 'שמעון'}
assert sorted((SP_NP & PR_NP) - TRIBES) == ['יפנה', 'כלב', 'נון'] and words('Num', 13, 8) == ['למטה', 'אפרים', 'הושע', 'בן', 'נון'] and sorted((C1_NP & PR_NP) - TRIBES) == ['עמיהוד'] and words('Num', 1, 10)[2:6] == ['לאפרים', 'אלישמע', 'בן', 'עמיהוד']
assert NPX('עמיהוד') == ['1Chr 7:26', '1Chr 9:4', 'Num 10:22', 'Num 1:10', 'Num 2:18', 'Num 34:20', 'Num 34:28', 'Num 7:48', 'Num 7:53'] and [nm for nm in ('אלידד', 'יגלי', 'אפד', 'שפטן', 'פרנך', 'עזן', 'אחיהוד', 'פדהאל') if NPX(nm) != [f'Num 34:{v}' for v in (21, 22, 23, 24, 25, 26, 27, 28) if nm in words('Num', 34, v)]] == []
assert len(NPX('שמואל')) == 120 and NPX('שמואל')[:1] == ['1Chr 11:3'] and [s for s in NPX('שמואל') if not s.startswith('1Sam')] == ['1Chr 11:3', '1Chr 26:28', '1Chr 29:29', '1Chr 6:13', '1Chr 6:18', '1Chr 7:2', '1Chr 9:22', '2Chr 35:18', 'Jer 15:1', 'Num 34:20', 'Ps 99:6'] and words('1Sam', 1, 20)[10] == 'שמואל'
assert NPX('קמואל') == ['1Chr 27:17', 'Gen 22:21', 'Num 34:24'] and NPX('אליצפן') == ['1Chr 15:8', '2Chr 29:13', 'Num 34:25', 'Num 3:30'] and words('Num', 3, 30)[5:8] == ['אליצפן', 'בן', 'עזיאל'] and NPX('בקי') == ['1Chr 5:31', '1Chr 6:36', 'Ezra 7:4', 'Num 34:22'] and NPX('פלטיאל') == ['2Sam 3:15', 'Num 34:26'] and NPX('חניאל') == ['1Chr 7:39', 'Num 34:23'] and NPX('שלמי') == ['Neh 7:48', 'Num 34:27'] and NPX('כסלון') == ['Josh 15:10', 'Num 34:21'] and words('Josh', 15, 10)[10:15] == ['הר', 'יערים', 'מצפונה', 'היא', 'כסלון'] and NPX('יפנה')[:3] == ['1Chr 4:15', '1Chr 6:41', '1Chr 7:38'] and len(NPX('יפנה')) == 16
assert [x for v in range(19, 29) for x, m in by[('Num', 34, v)] if m and 'Np' in m and 'אל' in x and x != 'ישראל'] == ['שמואל', 'אלידד', 'חניאל', 'קמואל', 'אליצפן', 'פלטיאל', 'פדהאל'] and [f for _, _, f in ((19, 'כלב', 'יפנה'), (20, 'שמואל', 'עמיהוד'), (21, 'אלידד', 'כסלון'), (22, 'בקי', 'יגלי'), (23, 'חניאל', 'אפד'), (24, 'קמואל', 'שפטן'), (25, 'אליצפן', 'פרנך'), (26, 'פלטיאל', 'עזן'), (27, 'אחיהוד', 'שלמי'), (28, 'פדהאל', 'עמיהוד')) if 'אל' in f] == []
TRIBE = {'ראובן': 'Reuben', 'שמעון': 'Simeon', 'לוי': 'Levi', 'יהודה': 'Judah', 'יששכר': 'Issachar', 'זבולן': 'Zebulun', 'זבלון': 'Zebulun', 'זבולון': 'Zebulun', 'אפרים': 'Ephraim', 'מנשה': 'Manasseh', 'בנימן': 'Benjamin', 'בנימין': 'Benjamin', 'דן': 'Dan', 'אשר': 'Asher', 'גד': 'Gad', 'נפתלי': 'Naphtali', 'יוסף': 'Joseph'}
def order(b, c, v1, v2):
    seen = []
    for v in range(v1, v2 + 1):
        for x, m in by[(b, c, v)]:
            bn = x
            for p in ('ול', 'ו', 'ל', 'ב', 'מ'):
                if x not in TRIBE and x.startswith(p) and len(x) > len(p) + 2: bn = x[len(p):]; break
            if bn in TRIBE and m and ('Np' in m or 'Ng' in m) and TRIBE[bn] not in seen: seen.append(TRIBE[bn])
    return seen
ORD34 = order('Num', 34, 19, 28)
assert ORD34 == ['Judah', 'Simeon', 'Benjamin', 'Dan', 'Joseph', 'Manasseh', 'Ephraim', 'Zebulun', 'Issachar', 'Asher', 'Naphtali']
ROSTERS = {'Num 1:5-15': ('Num', 1, 5, 15), 'Num 1:20-43': ('Num', 1, 20, 43), 'Num 2:3-31': ('Num', 2, 3, 31), 'Num 7:12-83': ('Num', 7, 12, 83), 'Num 10:14-27': ('Num', 10, 14, 27), 'Num 13:4-15': ('Num', 13, 4, 15), 'Num 26:5-50': ('Num', 26, 5, 50), 'Gen 46:9-24': ('Gen', 46, 9, 24), 'Gen 49:3-27': ('Gen', 49, 3, 27), 'Exod 1:2-4': ('Exod', 1, 2, 4), 'Deut 27:12-13': ('Deut', 27, 12, 13), 'Deut 33:6-25': ('Deut', 33, 6, 25)}
ORDERS = {k: order(*a) for k, a in ROSTERS.items()}
assert all(o != ORD34 for o in ORDERS.values()) and ORDERS['Num 26:5-50'] == ['Reuben', 'Simeon', 'Gad', 'Judah', 'Issachar', 'Zebulun', 'Joseph', 'Manasseh', 'Ephraim', 'Benjamin', 'Dan', 'Asher', 'Naphtali'] and ORDERS['Num 1:5-15'] == ['Reuben', 'Simeon', 'Judah', 'Issachar', 'Zebulun', 'Joseph', 'Ephraim', 'Manasseh', 'Benjamin', 'Asher', 'Naphtali'] and ORDERS['Num 13:4-15'] == ['Reuben', 'Simeon', 'Judah', 'Issachar', 'Joseph', 'Ephraim', 'Benjamin', 'Zebulun', 'Manasseh', 'Dan', 'Asher', 'Naphtali', 'Gad']
def before(o, a, b): return a in o and b in o and o.index(a) < o.index(b)
assert [k for k, o in ORDERS.items() if before(o, 'Manasseh', 'Ephraim')] == ['Num 26:5-50', 'Gen 46:9-24'] and [k for k, o in ORDERS.items() if before(o, 'Zebulun', 'Issachar')] == ['Gen 49:3-27', 'Deut 33:6-25'] and before(ORD34, 'Manasseh', 'Ephraim') and before(ORD34, 'Zebulun', 'Issachar')
assert ORD34[-4:] == ['Zebulun', 'Issachar', 'Asher', 'Naphtali'] and [(c, v, words('Josh', c, v)[:4]) for c, v in ((19, 10), (19, 17), (19, 24), (19, 32))] == [(19, 10, ['ויעל', 'הגורל', 'השלישי', 'לבני']), (19, 17, ['ליששכר', 'יצא', 'הגורל', 'הרביעי']), (19, 24, ['ויצא', 'הגורל', 'החמישי', 'למטה']), (19, 32, ['לבני', 'נפתלי', 'יצא', 'הגורל'])] and words('Josh', 19, 10)[3:5] == ['לבני', 'זבולן'] and words('Josh', 19, 24)[4:6] == ['בני', 'אשר']
assert phrase(['לבני', 'יוסף']) == ['Num 1:10', 'Num 1:32', 'Num 34:23'] and words('Num', 26, 28) == ['בני', 'יוסף', 'למשפחתם', 'מנשה', 'ואפרים'] and words('Gen', 49, 13)[0] == 'זבולן' and words('Gen', 49, 14)[0] == 'יששכר' and words('Deut', 33, 18)[3:6] == ['זבולן', 'בצאתך', 'ויששכר']
assert aramaic(34, 19) == ['ואלין', 'שמהת', 'גבריא', 'לשבטא', 'דיהודה', 'כלב', 'בר', 'יפנה'] and aramaic(34, 28) == ['ולשבטא', 'דבני', 'נפתלי', 'רבא', 'פדהאל', 'בר', 'עמיהוד']

# 34:29 THE CLOSER: "THESE ARE THEY WHOM THE LORD COMMANDED to give the children of Israel their inheritance in the land of Canaan" — the closer's
# form without a noun, one seat (30:17 "these are the statutes which", 36:13 "these are the commandments and the ordinances which", Leviticus
# 27:34 "these are the commandments which"); NO RECEIPT "as the LORD commanded" in the chapter — the run's receipt is Joshua 14:2's "as the LORD
# commanded BY THE HAND OF MOSES", outside the Torah, quoting 34:13. ONKELOS: one Aramaic form for the Qal (34:18) and the Piel (34:29).
assert phrase(['אלה', 'אשר', 'צוה', 'יהוה'], None) == ['Num 34:29'] and [s for s in phrase(['כאשר', 'צוה', 'יהוה'], None) if s.startswith('Num 34')] == [] and words('Num', 30, 17)[:5] == ['אלה', 'החקים', 'אשר', 'צוה', 'יהוה'] and words('Num', 36, 13)[:6] == ['אלה', 'המצות', 'והמשפטים', 'אשר', 'צוה', 'יהוה'] and words('Lev', 27, 34)[:5] == ['אלה', 'המצות', 'אשר', 'צוה', 'יהוה'] and aramaic(34, 29) == ['אלין', 'די', 'פקיד', 'יי', 'לאחסנא', 'ית', 'בני', 'ישראל', 'בארעא', 'דכנען']

# THE FOUR PROMISED EXTENTS AGAINST THE CHAPTER: the covenant's "from the river of Egypt to the great river, the river Euphrates" (Genesis 15:18),
# "from the Red Sea to the sea of the Philistines and from the wilderness to the river" (Exodus 23:31), "to the great river, the river Euphrates"
# (Deuteronomy 1:7), "from the river, the river Euphrates, to the western sea" (Deuteronomy 11:24; Joshua 1:4) — not one of the river's, the
# Euphrates', Lebanon's, the Philistines' or "the western sea"'s tokens stands in chapter 34 (computed above); its north stops at Lebo-hamath and
# Hazar-enan, its west is "the great sea". Deuteronomy 34:1-3 (the Sifrei 135:1's citation) shows Moses the land BY TRIBES — Gilead to Dan,
# Naphtali, Ephraim and Manasseh, Judah "to the western sea", the Negeb, the plain — the other description, OBSERVED.
assert phrase(['הים', 'האחרון'], None) == ['Deut 11:24', 'Deut 34:2', 'Joel 2:20', 'Zech 14:8'] and phrase(['הנהר', 'הגדל', 'נהר', 'פרת']) == ['Deut 1:7', 'Gen 15:18'] and words('Deut', 34, 2) == ['ואת', 'כל', 'נפתלי', 'ואת', 'ארץ', 'אפרים', 'ומנשה', 'ואת', 'כל', 'ארץ', 'יהודה', 'עד', 'הים', 'האחרון']

# THE STORE'S GLOSSES READ BACK (the display layer; the frozen unit untouched): the override file's rows — by reference for the chapter's seats,
# by gloss where every token of the gloss is the one word (censused below) — RESEARCH_LOG.md
assert sg(34, 3, 'פאת') == 'mouth-in-a-figurative-sense' and sg(34, 3, 'גבול') == 'cord' and sg(34, 3, 'המלח') == 'the-powder' and sg(34, 3, 'ממדבר') == 'from-pasture' and sg(34, 4, 'ונסב') == 'and-revolve' and sg(34, 4, 'למעלה') == 'to-?' and sg(34, 4, 'לקדש') == 'to-?' and sg(34, 4, 'חצר') == '?' and sg(34, 4, 'ויצא') == 'and-bring-forth' and sg(34, 4, 'תוצאתיו') == 'exit-him/its'
assert sg(34, 5, 'נחלה') == 'stream-suffix' and sg(34, 7, 'צפון') == 'hidden' and sg(34, 8, 'לבא') == 'come/bring' and sg(34, 11, 'ומחה') == 'and-stroke' and sg(34, 12, 'סביב') == 'circle' and sg(34, 12, 'הירדנה') == 'the-Jordan-suffix' and sg(34, 13, 'תתנחלו') == 'inherit--mode-of-descent)' and sg(34, 13, 'בגורל') == 'in-pebble' and sg(34, 18, 'לנחל') == 'to-inherit--mode-of-descent)' and sg(34, 22, 'דן') == 'Daniel' and sg(34, 17, 'נון') == 'Non' and sg(34, 15, 'מעבר') == 'from-region-across' and sg(34, 15, 'קדמה') == 'front-suffix' and sg(34, 15, 'מזרחה') == 'sunrise-suffix' and sg(34, 6, 'הים') == 'the-seas' and sg(34, 6, 'ים') == 'seas'
# THE BY-GLOSS CENSUS: every token of each gloss rewritten by gloss is the one word (sitting 11's rule — by gloss where the seats are one word,
# by reference where not)
GT = {g: store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1", (g,)).fetchall() for g in ('cord', 'the-cord', 'and-cord', 'to-cord', 'from-cord', 'in-cord', 'the-powder', 'hidden', 'Daniel', 'Non', 'from-pasture', 'front-suffix', 'sunrise-suffix', 'from-region-across', 'exit-him/its', 'in-pebble', 'the-seas', 'the-Jordan-suffix', 'to-boundary-her/its', 'Kadeshbarnea')}
assert GT['cord'] == [('גבול', 19)] and GT['the-cord'] == [('הגבול', 5), ('הגבל', 3)] and GT['and-cord'] == [('וגבול', 2), ('וגבל', 2)] and GT['to-cord'] == [('לגבול', 3)] and GT['from-cord'] == [('מגבול', 1)] and GT['the-powder'] == [('המלח', 4)] and GT['hidden'] == [('צפון', 8)] and GT['Daniel'] == [('דן', 25)] and GT['Non'] == [('נון', 16)] and GT['from-pasture'] == [('ממדבר', 8)] and GT['front-suffix'] == [('קדמה', 13)] and GT['sunrise-suffix'] == [('מזרחה', 9)] and GT['from-region-across'] == [('מעבר', 8)] and GT['exit-him/its'] == [('תוצאתיו', 4)] and GT['in-pebble'] == [('בגורל', 4)] and GT['the-seas'] == [('הים', 35)] and GT['the-Jordan-suffix'] == [('הירדנה', 1)] and GT['to-boundary-her/its'] == [('לגבלתיה', 2)] and GT['Kadeshbarnea'] == [('ברנע', 6)]
assert all(t.startswith(('גבל', 'גבול', 'הגבל', 'הגבול', 'וגבל', 'וגבול', 'בגבל', 'בגבול', 'לגבל', 'לגבול', 'מגבל', 'מגבול')) for g in ('cord', 'the-cord', 'and-cord', 'to-cord', 'from-cord', 'in-cord') for t, _ in GT[g])   # every token of the six rewritten 'cord' glosses is the border-word ('according' carries the letters too — the six alone are rewritten)
assert store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss='inherit--mode-of-descent)' GROUP BY 1").fetchall() == [('התנחל', 1), ('ינחיל', 1), ('ינחלו', 5), ('מנחיל', 1), ('ננחל', 1), ('תנחל', 2), ('תתנחלו', 2)] and store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss='to-inherit--mode-of-descent)' GROUP BY 1").fetchall() == [('לנחל', 2)]
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
OVERRIDE_REF = [('Num.34.3:2', 'the-side-of'), ('Num.34.3:7', 'alongside'), ('Num.34.3:13', 'from-the-end-of'), ('Num.34.3:14', 'the-sea-of'), ('Num.34.4:0', 'and-shall-turn'), ('Num.34.4:4', 'to-the-ascent-of'), ('Num.34.4:5', 'Akrabbim'), ('Num.34.4:7', 'to-Zin'), ('Num.34.4:12', 'to-Kadesh-'), ('Num.34.4:14', 'and-shall-go-out'), ('Num.34.4:15', 'Hazar-'), ('Num.34.4:16', 'addar'), ('Num.34.4:18', 'to-Azmon'), ('Num.34.5:0', 'and-shall-turn'), ('Num.34.5:3', 'the-brook-of'), ('Num.34.5:7', 'to-the-sea'), ('Num.34.6:1', 'the-west'), ('Num.34.6:11', 'the-west'), ('Num.34.8:3', 'Lebo-'), ('Num.34.8:6', 'the-goings-out-of'), ('Num.34.8:8', 'to-Zedad'), ('Num.34.9:0', 'and-shall-go-out'), ('Num.34.9:2', 'to-Ziphron'), ('Num.34.9:5', 'Hazar-'), ('Num.34.10:4', 'from-Hazar-'), ('Num.34.10:6', 'to-Shepham'), ('Num.34.11:8', 'and-shall-reach'), ('Num.34.11:11', 'the-sea-of'), ('Num.34.12:5', 'the-sea-of'), ('Num.34.12:12', 'round-about'), ('Num.34.13:15', 'to-give')]
OVERRIDE_GLOSS = [('cord', 'border'), ('the-cord', 'the-border'), ('and-cord', 'and-the-border'), ('to-cord', 'to-the-border'), ('from-cord', 'from-the-border'), ('in-cord', 'in-the-border-of'), ('the-powder', 'the-salt'), ('hidden', 'north'), ('Daniel', 'Dan'), ('Non', 'Nun'), ('from-pasture', 'from-the-wilderness-of'), ('front-suffix', 'eastward'), ('sunrise-suffix', 'toward-the-sunrise'), ('from-region-across', 'from-beyond'), ('exit-him/its', 'its-goings-out'), ('in-pebble', 'by-lot'), ('the-seas', 'the-sea'), ('the-Jordan-suffix', 'to-the-Jordan'), ('to-boundary-her/its', 'by-its-borders'), ('Kadeshbarnea', 'barnea'), ('inherit--mode-of-descent)', 'inherit'), ('to-inherit--mode-of-descent)', 'to-apportion'), ('and-inherit--mode-of-descent)', 'and-inherit'), ('and-inherit--mode-of-descent)-us/our', 'and-take-us-as-inheritance'), ('in-inherit--mode-of-descent)', 'when-he-apportioned'), ('inherit--mode-of-descent)-her/its', 'cause-to-inherit-it'), ('inherit--mode-of-descent)-him/its', 'causes-to-inherit'), ('inherit--mode-of-descent)-you/your', 'gives-you-to-inherit')]
STORE_IDX = {(v, idx): tok for v, idx, tok in store.execute("SELECT v.verse, w.idx, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34")}
assert {k: STORE_IDX[(int(k.split('.')[2].split(':')[0]), int(k.split(':')[1]))] for k, _ in OVERRIDE_REF} == {'Num.34.3:2': 'פאת', 'Num.34.3:7': 'ידי', 'Num.34.3:13': 'מקצה', 'Num.34.3:14': 'ים', 'Num.34.4:0': 'ונסב', 'Num.34.4:4': 'למעלה', 'Num.34.4:5': 'עקרבים', 'Num.34.4:7': 'צנה', 'Num.34.4:12': 'לקדש', 'Num.34.4:14': 'ויצא', 'Num.34.4:15': 'חצר', 'Num.34.4:16': 'אדר', 'Num.34.4:18': 'עצמנה', 'Num.34.5:0': 'ונסב', 'Num.34.5:3': 'נחלה', 'Num.34.5:7': 'הימה', 'Num.34.6:1': 'ים', 'Num.34.6:11': 'ים', 'Num.34.8:3': 'לבא', 'Num.34.8:6': 'תוצאת', 'Num.34.8:8': 'צדדה', 'Num.34.9:0': 'ויצא', 'Num.34.9:2': 'זפרנה', 'Num.34.9:5': 'חצר', 'Num.34.10:4': 'מחצר', 'Num.34.10:6': 'שפמה', 'Num.34.11:8': 'ומחה', 'Num.34.11:11': 'ים', 'Num.34.12:5': 'ים', 'Num.34.12:12': 'סביב', 'Num.34.13:15': 'לתת'}
assert all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_REF) and all(f'"{k}": "{v}"' in OV for k, v in OVERRIDE_GLOSS), [k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'"{k}": "{v}"' not in OV]
