import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 14 — THE BORDERS, Numbers 34:1-29 (2026-09-12): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED
# from the Tanakh DB, the snapshot store and the shelf's bytes, so that bor_ink.py's asserts are typed FROM THE PRINT (the standing lesson: the
# measurement pass first, then the asserts; print the verse, then slice). Nothing asserted here. Sitting 13's form (jou_measure1.py).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows: by.setdefault((b, c, v), []).append((plain(he), m, he))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
C = 34; NV = 29
def words(b, c, v): return [x for x, _, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m, _ in by[(b, c, v)]]
def wm(b, c, v): return list(zip(words(b, c, v), morphs(b, c, v)))
def hits(sub, books=None, exact=True): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _, _ in ws)})
def phrase(seq, books=None):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books)))
def PF(name, pre=('', 'ו', 'ב', 'ל', 'מ', 'ול', 'וב', 'ומ', 'כ', 'ה', 'וה', 'לה', 'בה', 'מה')): return tuple(p + name for p in pre)
def cnt_in(pred, c=C): return sum(1 for v in range(1, NV + 1) for x, m, _ in by[('Num', c, v)] if pred(x, m))
def seats_in(pred, c=C): return [(v, x) for v in range(1, NV + 1) for x, m, _ in by[('Num', c, v)] if pred(x, m)]
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']; onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
def aramaic(c, v): return [plain(x) for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def onk_seats(sub): return [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if sub in ' '.join(aramaic(c + 1, v + 1))]
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']; sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
print('---- THE SHELF: the "שם" form of the Hebrew citation (the Ibid. in Hebrew) — a FOURTH citation form; the rows that cite 34 in any form')
HE_SHAM = [(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'שם ל[\"״]?ד[\)\s:]', clean(row))]
print('HE rows with (שם ל"ד):', HE_SHAM, '| the 1:2 Hebrew citations:', re.findall(r'\([^)]*\)', Hb(1, 2)))
print('EN 1:2 head:', E(1, 2)[:60], '| "Except in one" clause:', E(1, 2)[E(1, 2).find('Except'):E(1, 2).find('Except') + 200])
print('HE 1:2 the clause:', Hb(1, 2)[Hb(1, 2).find('חוץ מאחת'):Hb(1, 2).find('חוץ מאחת') + 120])
print('צו את בני ישראל seats Torah:', phrase(['צו', 'את', 'בני', 'ישראל'], T), '| with ואמרת אלהם:', phrase(['צו', 'את', 'בני', 'ישראל', 'ואמרת', 'אלהם']), '| צו tokens Torah:', U('צו', books=T))
print('the 1:2 row\'s list vs the census — the row names: Vayikra 24:2, Bamidbar 35:2, 28:2, 34:2, and its own 5:2')
TRI = f'{ROOT}/logic/oral_triage'
for f in sorted(os.listdir(TRI)):
    if not f.endswith('.md'): continue
    t = open(f'{TRI}/{f}', encoding='utf-8').read()
    for key in ('Sifrei Bamidbar 1:2', 'Sifrei Bamidbar 1:8', 'Sifrei Bamidbar 135:1', 'Sifrei Bamidbar 160:2', 'Sifrei Bamidbar 47:1', 'Sifrei Bamidbar 133:3'):
        if re.search(r'^- ' + re.escape(key) + r'\b', t, re.M): print('  ', f, 'READS', key)
print('135:1 HE end:', Hb(135, 1)[-160:], '| 1:8 EN Ibid context:', E(1, 8)[E(1, 8).find('(Shemot'):E(1, 8).find('(Shemot') + 260])
print('160:2 EN:', E(160, 2)[:400])
print('47:1 EN head:', E(47, 1)[:200], '| HE נשיא אחד context:', Hb(47, 1)[max(0, Hb(47, 1).find('נשיא אחד') - 60):Hb(47, 1).find('נשיא אחד') + 60])
print('---- THE FRAME AND THE REGISTER')
DIV = {}
for (b, c, v), ws in by.items():
    if b != 'Num': continue
    w = [x for x, _, _ in ws]
    if any(w[i] in ('ויאמר', 'וידבר') and w[i + 1] == 'יהוה' for i in range(len(w) - 1)): DIV.setdefault(c, []).append(v)
print('divine-frame verses in 34:', DIV.get(34), '| Numbers chapters WITHOUT one:', [c for c in range(1, 37) if c not in DIV], '| frames per chapter 33-36:', {c: DIV.get(c) for c in (33, 34, 35, 36)})
print('וידבר יהוה אל משה לאמר count Numbers:', len([s for s in phrase(['וידבר', 'יהוה', 'אל', 'משה', 'לאמר']) if s.startswith('Num')]), '| Torah:', len(phrase(['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'], T)))
print('ויצו משה את בני ישראל:', phrase(['ויצו', 'משה', 'את', 'בני', 'ישראל']), '| ויצו משה seats Torah:', phrase(['ויצו', 'משה'], T), '| Num 36:5:', words('Num', 36, 5)[:8], '| Num 32:28:', words('Num', 32, 28)[:6])
REG = [(v, x, m) for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if m and re.search(r'V.w', m)]
print('narrative verbs:', REG)
WQ = [(v, x, m) for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if m and re.search(r'^HC/V.q', m)]
print('weqatal (and-it-shall) verbs:', len(WQ), Counter(x for _, x, _ in WQ), '| by verse:', {v: [x for vv, x, _ in WQ if vv == v] for v in range(2, 13)})
print('IMPERFECTS 2mp (you shall):', [(v, x, m) for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if m and re.search(r'V.i2mp', m)])
print('---- 34:2 THE HEADING')
print('34:2:', wm('Num', 34, 2))
print('כי אתם באים:', phrase(['כי', 'אתם', 'באים']), '| כי אתם עברים:', phrase(['כי', 'אתם', 'עברים']), '| כי תבאו אל הארץ Torah:', phrase(['כי', 'תבאו', 'אל', 'הארץ'], T), '| אל הארץ כנען:', phrase(['אל', 'הארץ', 'כנען']), '| הארץ כנען:', phrase(['הארץ', 'כנען']), '| ארץ כנען Torah count:', len(phrase(['ארץ', 'כנען'], T)), '| in 34:', [(v, i) for v in range(1, NV + 1) for i in range(len(words('Num', 34, v)) - 1) if words('Num', 34, v)[i] == 'ארץ' and words('Num', 34, v)[i + 1] == 'כנען'], '| בארץ כנען 34:29:', words('Num', 34, 29)[-2:])
print('זאת הארץ seats Torah:', phrase(['זאת', 'הארץ'], T), '| Deut 34:4:', words('Deut', 34, 4)[:6], '| Ezek 47:14:', words('Ezek', 47, 14), '| Ezek 47:13:', words('Ezek', 47, 13), '| Ezek 47:21:', words('Ezek', 47, 21))
print('תפל seats:', U('תפל'), '| נפל + נחלה (the lot\'s falling): נפלה', U('נפלה', 'ונפלה'), '| הפלה / הפלתי / הפילו:', U('הפלה', 'הפלתי', 'הפילו', 'הפיל', 'ויפל', 'ויפילו'), '| Josh 13:6:', words('Josh', 13, 6)[-6:], '| Josh 23:4:', words('Josh', 23, 4)[:7], '| Judg 18:1:', words('Judg', 18, 1)[-8:], '| Ps 16:6:', words('Ps', 16, 6), '| Ezek 48:29:', words('Ezek', 48, 29), '| Onkelos 34:2:', aramaic(34, 2))
print('לגבלתיה seats:', U('לגבלתיה', 'לגבולתיה', 'גבלתיה'), '| גבול-tokens in 34:', [(v, x) for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if 'גבל' in x or 'גבול' in x], '| count:', cnt_in(lambda x, m: 'גבל' in x or 'גבול' in x), '| גבול-stem tokens in Numbers:', sum(1 for (b, c, v), ws in by.items() if b == 'Num' for x, _, _ in ws if re.search(r'גב[ו]?ל', x) and not x.startswith('גבל') is None), '| in Numbers by chapter:', Counter(c for (b, c, v), ws in by.items() if b == 'Num' for x, m, _ in ws if re.search(r'^(ו|ב|ל|מ|ה|וה|ול|ומ|וב)?(ה)?גב[ו]?ל', x) and m and 'Nc' in m), '| Torah total:', sum(1 for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if re.search(r'^(ו|ב|ל|מ|ה|וה|ול|ומ|וב)?(ה)?גב[ו]?ל', x) and m and 'Nc' in m))
print('בנחלה seats Torah:', U('בנחלה', books=T), '| נחלה-tokens in 34:', seats_in(lambda x, m: 'נחל' in x))
print('---- 34:3-5 THE SOUTH AGAINST JOSHUA 15:1-4')
for v in (1, 2, 3, 4): print(f'Josh 15:{v}:', words('Josh', 15, v))
S34 = {x for v in (3, 4, 5) for x in words('Num', 34, v)}; S15 = {x for v in (1, 2, 3, 4) for x in words('Josh', 15, v)}
print('shared tokens 34:3-5 ∩ Josh 15:1-4:', sorted(S34 & S15), '| count:', len(S34 & S15), '| 34:3-5 tokens distinct:', len(S34))
print('פאת נגב:', phrase(['פאת', 'נגב']), '| פאת tokens Torah:', U('פאת', 'לפאת', 'ולפאת', 'פאה', 'ופאת', books=T), '| פאת in Numbers:', [s for s in U('פאת', 'לפאת', 'ולפאת', 'ופאת') if s.startswith('Num')], '| Exod 27:9:', words('Exod', 27, 9)[:9], '| Num 35:5:', words('Num', 35, 5)[:10])
print('ממדבר צן / מדבר צן seats:', phrase(['מדבר', 'צן']), phrase(['ממדבר', 'צן']), phrase(['במדבר', 'צן']), '| צנה:', U('צנה'), '| Num 13:21:', words('Num', 13, 21), '| על ידי אדום:', phrase(['על', 'ידי', 'אדום']), '| על ידי seats Torah:', phrase(['על', 'ידי'], T), '| Onkelos 34:3:', aramaic(34, 3))
print('גבול נגב:', phrase(['גבול', 'נגב']), '| מקצה ים המלח:', phrase(['מקצה', 'ים', 'המלח']), '| ים המלח seats:', phrase(['ים', 'המלח']), '| Gen 14:3:', words('Gen', 14, 3), '| Deut 3:17:', words('Deut', 3, 17), '| Josh 15:2:', words('Josh', 15, 2), '| Josh 15:5:', words('Josh', 15, 5), '| Josh 18:19:', words('Josh', 18, 19)[-8:])
print('קדמה tokens in 34:', seats_in(lambda x, m: x == 'קדמה'), '| קדמה seats Torah:', U('קדמה', books=T), '| קדמה מזרחה:', phrase(['קדמה', 'מזרחה']), '| Exod 27:13:', words('Exod', 27, 13), '| Num 2:3:', words('Num', 2, 3)[:6])
print('34:4:', wm('Num', 34, 4))
print('ונסב seats:', U('ונסב'), '| מעלה עקרבים:', phrase(['למעלה', 'עקרבים']), phrase(['מעלה', 'עקרבים']), phrase(['ממעלה', 'עקרבים']), '| Judg 1:36:', words('Judg', 1, 36), '| ועבר צנה:', phrase(['ועבר', 'צנה']), '| קדש ברנע seats:', phrase(['קדש', 'ברנע']), '| count:', len(phrase(['קדש', 'ברנע'])), '| Torah:', phrase(['קדש', 'ברנע'], T))
print('חצר אדר:', phrase(['חצר', 'אדר']), '| חצרון seats:', U('חצרון', 'חצרונה', 'וחצרון'), '| אדרה / אדר:', U('אדרה', 'אדר'), '| Josh 15:3 wm:', wm('Josh', 15, 3), '| עצמנה / עצמון:', U('עצמנה', 'עצמון', 'מעצמון', 'ומעצמון'))
print('תוצאתיו / תוצאת seats (the outgoings):', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() for x, _, _ in ws if re.search(r'^(ו|ה)?ת[ו]?צא[ו]?ת', x)}), '| Torah:', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, _, _ in ws if re.search(r'^(ו|ה)?ת[ו]?צא[ו]?ת', x)}))
print('34:5:', wm('Num', 34, 5), '| נחלה מצרים:', phrase(['נחלה', 'מצרים']), '| נחל מצרים seats:', phrase(['נחל', 'מצרים']), '| נהר מצרים:', phrase(['נהר', 'מצרים']), '| Gen 15:18:', words('Gen', 15, 18), '| 1Kgs 8:65:', words('1Kgs', 8, 65), '| 2Kgs 14:25:', words('2Kgs', 14, 25)[:12], '| Isa 27:12:', words('Isa', 27, 12), '| הימה seats Torah:', U('הימה', books=T), '| Onkelos 34:5:', aramaic(34, 5))
# THE STORE'S PAIR AT 34:4
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
print('STORE 34:4 tokens:', store.execute("SELECT w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34 AND v.verse=4 ORDER BY w.idx").fetchall())
print('STORE 34:4 raw he (with points) idx 7-9:', store.execute("SELECT w.idx, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34 AND v.verse=4 AND w.idx BETWEEN 6 AND 10 ORDER BY w.idx").fetchall())
print('DB 34:4 idx 7 (והיה) raw:', [(x, m, raw) for x, m, raw in by[('Num', 34, 4)] if x == 'והיה'], '| DB Josh 15:4 raw והיה/והיו:', [(x, m, raw) for x, m, raw in by[('Josh', 15, 4)] if x in ('והיה', 'והיו')], '| Josh 15:4:', words('Josh', 15, 4))
print('STORE Josh 15:4 count vs DB:', store.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Josh' AND v.chapter=15 AND v.verse=4").fetchone(), len(by[('Josh', 15, 4)]))
print('34:4 store pairs — the other store/DB count differences in Num 34:', [(v, n, len(by[('Num', 34, v)])) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34 GROUP BY v.verse").fetchall() if n != len(by[('Num', 34, v)])], '| in Num 33-36:', [(c, v, n, len(by[('Num', c, v)])) for c, v, n in store.execute("SELECT v.chapter, v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter BETWEEN 33 AND 36 GROUP BY v.chapter, v.verse").fetchall() if n != len(by[('Num', c, v)])])
print('והיה תוצאתיו / והיו תוצאתיו / והיו תוצאת:', phrase(['והיה', 'תוצאתיו']), phrase(['והיו', 'תוצאתיו']), phrase(['והיו', 'תוצאת']), phrase(['והיה', 'תצאות']), phrase(['והיו', 'תצאות']), phrase(['והיו', 'תצאתיו']), phrase(['והיה', 'תצאתיו']))
print('---- 34:6 THE WEST')
print('34:6:', wm('Num', 34, 6), '| 34:7:', wm('Num', 34, 7))
print('וגבול ים:', phrase(['וגבול', 'ים']), '| גבול ים:', phrase(['גבול', 'ים']), '| Josh 15:12:', words('Josh', 15, 12), '| הים הגדול seats:', phrase(['הים', 'הגדול']), '| הים הגדל (defective):', phrase(['הים', 'הגדל']), '| הגדל token seats Torah:', U('הגדל', books=T), '| Ezek 47:20:', words('Ezek', 47, 20), '| Onkelos 34:6:', aramaic(34, 6), '| Onkelos 34:7:', aramaic(34, 7))
print('ים tokens in 34 with the next token:', [(v, x, words('Num', 34, v)[i + 1] if i + 1 < len(words('Num', 34, v)) else None) for v in range(1, NV + 1) for i, (x, m, _) in enumerate(by[('Num', C, v)]) if x in ('ים', 'הים') and m and 'Nc' in m], '| count:', cnt_in(lambda x, m: x in ('ים', 'הים') and m and 'Nc' in m), '| ימה / הימה:', seats_in(lambda x, m: x in ('ימה', 'הימה')))
print('---- 34:7-9 THE NORTH')
print('34:8:', wm('Num', 34, 8), '| 34:9:', wm('Num', 34, 9))
print('גבול צפון:', phrase(['גבול', 'צפון']), '| תתאו / והתאויתם seats:', U('תתאו', 'והתאויתם', 'תתאה', 'התאו'), '| the root תאה anywhere (tokens containing תא with ו/ה):', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() for x, m, _ in ws if re.search(r'תא[וה]', x) and m and m.startswith('HV') and not re.search(r'תאו[ה]?$', x) is None or x in ('תתאו', 'והתאויתם')}), '| ותאר seats (Joshua\'s marking verb):', U('ותאר', 'תאר', 'ויתאר'), '| Josh 15:9:', words('Josh', 15, 9)[:6], '| Josh 18:14:', words('Josh', 18, 14)[:4], '| Isa 44:13:', words('Isa', 44, 13)[:6])
print('הר ההר seats:', phrase(['הר', 'ההר']), phrase(['בהר', 'ההר']), phrase(['מהר', 'ההר']), phrase(['להר', 'ההר']), '| count all:', len(phrase(['הר', 'ההר']) + phrase(['בהר', 'ההר']) + phrase(['מהר', 'ההר']) + phrase(['להר', 'ההר'])), '| Torah 34 seats:', [s for s in phrase(['הר', 'ההר']) + phrase(['מהר', 'ההר']) if s.startswith('Num 34')], '| Onkelos 34:7 / 34:8 / 33:37 / 33:38 / 20:22:', aramaic(34, 7)[-2:], aramaic(34, 8)[:2], aramaic(33, 37)[-2:], aramaic(33, 38)[4:7], aramaic(20, 22)[-2:], '| Onkelos seats הור טורא:', onk_seats('הור טורא'), '| הר טורא:', onk_seats('הר טורא'))
print('לבא חמת seats:', phrase(['לבא', 'חמת']), phrase(['לבוא', 'חמת']), phrase(['מלבוא', 'חמת']), phrase(['מלבא', 'חמת']), '| Num 13:21:', words('Num', 13, 21), '| Josh 13:5:', words('Josh', 13, 5), '| 1Chr 13:5:', words('1Chr', 13, 5), '| Amos 6:14:', words('Amos', 6, 14)[-8:], '| Onkelos 34:8:', aramaic(34, 8), '| Onkelos 13:21:', aramaic(13, 21))
print('צדדה / צדד:', U('צדדה', 'צדד'), '| Ezek 47:15:', words('Ezek', 47, 15), '| זפרנה / זפרון:', U('זפרנה', 'זפרון'), '| חצר עינן:', phrase(['חצר', 'עינן']), phrase(['מחצר', 'עינן']), '| חצר עינון:', phrase(['חצר', 'עינון']), '| Ezek 47:17:', words('Ezek', 47, 17), '| Ezek 48:1:', words('Ezek', 48, 1), '| Onkelos 34:9:', aramaic(34, 9))
print('---- 34:10-12 THE EAST')
print('34:10:', wm('Num', 34, 10), '| 34:11:', wm('Num', 34, 11), '| 34:12:', wm('Num', 34, 12))
print('שפמה / משפם / שפם:', U('שפמה', 'משפם', 'שפם'), '| הרבלה:', U('הרבלה'), '| רבלה / רבלתה / ברבלה:', U('רבלה', 'רבלתה', 'ברבלה', 'ברבלתה'), '| Ezek 6:14:', words('Ezek', 6, 14), '| 2Kgs 23:33:', words('2Kgs', 23, 33)[:6], '| לעין seats:', U('לעין'), '| מקדם לעין:', phrase(['מקדם', 'לעין']), '| עין seats Torah as Np:', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if x in ('עין', 'לעין', 'ועין', 'מעין') and m and 'Np' in m}))
print('ומחה seats:', U('ומחה'), '| Isa 25:8:', words('Isa', 25, 8), '| the root מחה in the Torah (verbs):', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if re.search(r'מח[הי]', x) and m and m.startswith('HV') and not re.search(r'^(ו)?(מחר|מחנ|מחל|מחצ|מחש|מחס|מחת)', x)}), '| Exod 17:14:', words('Exod', 17, 14)[-6:], '| Deut 25:19:', words('Deut', 25, 19)[-8:], '| Onkelos 34:11:', aramaic(34, 11))
print('כתף tokens Torah:', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, _, _ in ws if 'כתף' in x or 'כתפ' in x}), '| count Torah:', sum(1 for (b, c, v), ws in by.items() if b in T for x, _, _ in ws if 'כתף' in x or 'כתפ' in x), '| כתף in Joshua (the border word):', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b == 'Josh' for x, _, _ in ws if 'כתף' in x or 'כתפ' in x}), '| Exod 27:14:', words('Exod', 27, 14), '| Exod 28:7:', words('Exod', 28, 7))
print('כנרת / כנרות seats:', U('כנרת', 'כנרות', 'וכנרת', 'כנרתה', 'מכנרת'), '| ים כנרת:', phrase(['ים', 'כנרת']), '| Deut 3:17:', words('Deut', 3, 17), '| Josh 13:27:', words('Josh', 13, 27)[-10:], '| Josh 19:35:', words('Josh', 19, 35), '| Onkelos seats גנסר:', onk_seats('גנסר'))
print('הירדנה seats:', U('הירדנה'), '| ירדנה:', U('ירדנה'), '| סביב seats in 34:', seats_in(lambda x, m: x == 'סביב'), '| Onkelos 34:12:', aramaic(34, 12), '| סחור סחור seats Onkelos Numbers:', onk_seats('סחור סחור'))
print('the loop: ים המלח at 34:3 and 34:12 — the tokens:', words('Num', 34, 3)[-3:], words('Num', 34, 12)[5:7])
print('---- EZEKIEL 47:13-20 AND 48:1, 28 AGAINST 34:3-12 (the tokens)')
for v in range(13, 21): print(f'Ezek 47:{v}:', words('Ezek', 47, v))
print('Ezek 48:28:', words('Ezek', 48, 28))
N34 = {x for v in range(3, 13) for x in words('Num', 34, v)}; EZ = {x for v in range(13, 21) for x in words('Ezek', 47, v)} | set(words('Ezek', 48, 28)) | set(words('Ezek', 48, 1))
print('shared tokens (34:3-12 ∩ Ezek 47:13-20 + 48:1, 28):', sorted(N34 & EZ), '| count:', len(N34 & EZ))
print('Ezekiel\'s order of sides (the פאת tokens with the next word) 47:15-20:', [(v, x, words('Ezek', 47, v)[i + 1]) for v in range(15, 21) for i, x in enumerate(words('Ezek', 47, v)) if x in ('פאת', 'ופאת', 'לפאת') and i + 1 < len(words('Ezek', 47, v))], '| Numbers\' order: 34:3 נגב, 34:6 ים, 34:7 צפון, 34:10 קדמה')
print('---- 34:13-15 MOSES\' RESTATEMENT')
print('34:13:', wm('Num', 34, 13), '| 34:14:', wm('Num', 34, 14), '| 34:15:', wm('Num', 34, 15))
print('תתנחלו / והתנחלתם seats:', U('תתנחלו', 'והתנחלתם', 'והתנחלום', 'התנחלו'), '| בגורל seats Torah:', U('בגורל', books=T), '| Bible:', len(U('בגורל')), '| אשר צוה יהוה לתת:', phrase(['אשר', 'צוה', 'יהוה', 'לתת']), '| צוה יהוה לתת:', phrase(['צוה', 'יהוה', 'לתת']), '| Num 36:2:', words('Num', 36, 2))
print('לתשעת המטות וחצי המטה:', phrase(['לתשעת', 'המטות', 'וחצי', 'המטה']), '| לתשעת השבטים וחצי השבט:', phrase(['לתשעת', 'השבטים', 'וחצי', 'השבט']), '| תשעת seats:', U('תשעת', 'לתשעת', 'ותשעת'), '| Josh 14:2:', words('Josh', 14, 2), '| Josh 13:7:', words('Josh', 13, 7), '| Josh 14:3-4:', words('Josh', 14, 3), words('Josh', 14, 4))
print('מטה-tokens in 34:', seats_in(lambda x, m: re.search(r'^(ו|ל|ב|מ|ול)?(ה)?(מטה|מטות)$', x) is not None and m and 'Nc' in m), '| count:', cnt_in(lambda x, m: re.search(r'^(ו|ל|ב|מ|ול)?(ה)?(מטה|מטות)$', x) is not None and m and 'Nc' in m), '| שבט-tokens in 34:', seats_in(lambda x, m: 'שבט' in x), '| שבט tokens in Numbers:', sorted({f'{c}:{v} {x}' for (b, c, v), ws in by.items() if b == 'Num' for x, _, _ in ws if 'שבט' in x}), '| מטה (tribe) tokens in Numbers count:', sum(1 for (b, c, v), ws in by.items() if b == 'Num' for x, m, _ in ws if re.search(r'^(ו|ל|ב|מ|ול)?(ה)?(מטה|מטות)$', x) and m and 'Nc' in m))
print('חצי מטה מנשה:', phrase(['חצי', 'מטה', 'מנשה']), phrase(['וחצי', 'מטה', 'מנשה']), phrase(['מחצי', 'מטה', 'מנשה']), phrase(['לחצי', 'מטה', 'מנשה']), '| חצי שבט מנשה / המנשה:', phrase(['חצי', 'שבט', 'מנשה']), phrase(['וחצי', 'שבט', 'מנשה']), phrase(['לחצי', 'שבט', 'מנשה']), phrase(['חצי', 'שבט', 'המנשה']), phrase(['וחצי', 'שבט', 'המנשה']), phrase(['לחצי', 'שבט', 'המנשה']), phrase(['ולחצי', 'שבט', 'המנשה']), phrase(['ולחצי', 'שבט', 'מנשה']), phrase(['מחצי', 'שבט', 'המנשה']), phrase(['וחצי', 'המטה']), '| Num 32:33:', words('Num', 32, 33)[7:11], '| Deut 3:13:', words('Deut', 3, 13)[:8], '| Josh 21:5-6:', words('Josh', 21, 5), words('Josh', 21, 6))
print('הראובני seats:', U('הראובני', 'והראובני', 'לראובני'), '| הגדי:', U('הגדי', 'והגדי', 'לגדי'), '| הראובני + הגדי in one verse:', sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if {'הראובני', 'והראובני', 'לראובני'} & {x for x, _, _ in ws} and {'הגדי', 'והגדי', 'לגדי'} & {x for x, _, _ in ws}}), '| Deut 3:12:', words('Deut', 3, 12), '| Josh 1:12:', words('Josh', 1, 12), '| Num 26:7:', words('Num', 26, 7)[:4])
print('לבית אבתם seats Torah count:', len(U('אבתם', books=T)), '| לבית אבתם in Numbers:', len([s for s in phrase(['לבית', 'אבתם']) if s.startswith('Num')]), '| לקחו נחלתם:', phrase(['לקחו', 'נחלתם']), '| מעבר לירדן ירחו:', phrase(['מעבר', 'לירדן', 'ירחו']), '| מעבר לירדן seats Torah:', phrase(['מעבר', 'לירדן'], T), '| על ירדן ירחו:', len(phrase(['על', 'ירדן', 'ירחו'])), '| Num 22:1:', words('Num', 22, 1), '| מזרחה seats Torah:', U('מזרחה', books=T), '| Onkelos 34:13 / 14 / 15:', aramaic(34, 13), aramaic(34, 14), aramaic(34, 15), '| Onkelos 32:33:', aramaic(32, 33)[6:11], '| Onkelos שבטא count 34:', sum(' '.join(aramaic(34, v)).count('שבט') for v in range(1, 30)), '| Onkelos 13:7-like (שבטין):', onk_seats('שבטין'))
print('---- 34:16-18 THE COMMISSION')
print('34:17:', wm('Num', 34, 17), '| 34:18:', wm('Num', 34, 18))
print('שמות האנשים seats:', phrase(['שמות', 'האנשים']), '| אלה שמות seats Torah:', phrase(['אלה', 'שמות'], T), '| ואלה שמות Torah:', phrase(['ואלה', 'שמות'], T), '| Num 1:5:', words('Num', 1, 5)[:6], '| Num 13:16:', words('Num', 13, 16)[:8], '| Num 13:4:', words('Num', 13, 4)[:4])
print('THE ROOT נחל IN 34 — the stems by morph:', seats_in(lambda x, m: 'נחל' in x), [(v, x, m) for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if 'נחל' in x], '| Piel נחל (Vp) seats Bible:', sorted({f'{b} {c}:{v} {x} {m}' for (b, c, v), ws in by.items() for x, m, _ in ws if 'נחל' in x and m and re.search(r'^H(C/|R/)?Vp', m)}), '| Qal נחל verbs Torah:', sorted({f'{b} {c}:{v} {x} {m}' for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if 'נחל' in x and m and re.search(r'Vq', m)}), '| Hitpael:', sorted({f'{b} {c}:{v} {x} {m}' for (b, c, v), ws in by.items() for x, m, _ in ws if 'נחל' in x and m and re.search(r'Vt', m)}), '| Hiphil Torah:', sorted({f'{b} {c}:{v} {x} {m}' for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if 'נחל' in x and m and re.search(r'Vh', m)}))
print('Josh 14:1:', wm('Josh', 14, 1), '| Josh 19:51:', wm('Josh', 19, 51), '| Josh 19:49:', words('Josh', 19, 49), '| Josh 13:32:', words('Josh', 13, 32)[:5])
print('אלעזר הכהן ויהושע בן נון:', phrase(['אלעזר', 'הכהן', 'ויהושע', 'בן', 'נון']), '| Num 32:28:', words('Num', 32, 28), '| Josh 21:1:', words('Josh', 21, 1), '| Josh 17:4:', words('Josh', 17, 4)[:9], '| Num 27:19-22 pairs:', words('Num', 27, 19)[:6], words('Num', 27, 21)[:5], words('Num', 27, 22)[-6:])
print('נשיא אחד נשיא אחד:', phrase(['נשיא', 'אחד', 'נשיא', 'אחד']), '| נשיא אחד seats:', phrase(['נשיא', 'אחד']), '| Num 17:21:', words('Num', 17, 21), '| Num 7:11:', words('Num', 7, 11), '| איש אחד איש אחד:', phrase(['איש', 'אחד', 'איש', 'אחד']), '| Num 13:2:', words('Num', 13, 2), '| Num 1:4:', words('Num', 1, 4), '| Deut 1:23:', words('Deut', 1, 23), '| Josh 3:12 / 4:2 / 4:4:', words('Josh', 3, 12), words('Josh', 4, 2), words('Josh', 4, 4)[-6:], '| Num 1:44:', words('Num', 1, 44), '| Ezek 45:7? no; 1Kgs 4:7:', words('1Kgs', 4, 7)[:6])
print('ממטה seats:', U('ממטה'), '| תקחו seats Torah:', U('תקחו', books=T), '| לנחל את הארץ:', phrase(['לנחל', 'את', 'הארץ']), '| לנחל את בני ישראל:', phrase(['לנחל', 'את', 'בני', 'ישראל']), '| Onkelos 34:17 / 18 / 29:', aramaic(34, 17), aramaic(34, 18), aramaic(34, 29), '| רבא seats Onkelos Numbers (count of verses):', len(onk_seats(' רבא ')), '| Onkelos 1:16:', aramaic(1, 16), '| Onkelos 7:11:', aramaic(7, 11))
print('---- 34:19-28 THE ROSTER')
ROST = [(v, words('Num', 34, v)) for v in range(19, 29)]
for v, w in ROST: print(f'  34:{v}: {w}')
print('the title נשיא per verse:', [(v, 'נשיא' in w) for v, w in ROST], '| בני per verse:', [(v, 'בני' in w) for v, w in ROST], '| the vav on the first word:', [(v, w[0]) for v, w in ROST])
print('למטה יהודה כלב בן יפנה:', phrase(['למטה', 'יהודה', 'כלב', 'בן', 'יפנה']), '| כלב בן יפנה seats:', phrase(['כלב', 'בן', 'יפנה']), '| Torah:', phrase(['כלב', 'בן', 'יפנה'], T), '| וכלב בן יפנה:', phrase(['וכלב', 'בן', 'יפנה']), '| הקנזי:', U('הקנזי'), '| Num 13:6:', words('Num', 13, 6), '| Josh 14:6:', words('Josh', 14, 6), '| Josh 14:13-14:', words('Josh', 14, 13), words('Josh', 14, 14), '| Judg 1:12? (Caleb alone):', words('Judg', 1, 12)[:4])
SPIES = {v: words('Num', 13, v) for v in range(4, 16)}
print('THE SPIES 13:4-15:', SPIES)
sp_names = {x for v in range(4, 16) for x, m, _ in by[('Num', 13, v)] if m and 'Np' in m}; pr_names = {x for v in range(17, 29) for x, m, _ in by[('Num', 34, v)] if m and 'Np' in m}
ch1_names = {x for v in range(5, 16) for x, m, _ in by[('Num', 1, v)] if m and 'Np' in m}
print('spies\' Np ∩ 34:17-28 Np:', sorted(sp_names & pr_names), '| chapter 1 princes\' Np ∩ 34:17-28:', sorted(ch1_names & pr_names), '| Num 1:5-15:', {v: words('Num', 1, v) for v in range(5, 16)})
def bare_name(x):
    for p in ('ול', 'ו', 'ל', 'ב', 'מ'):
        if x.startswith(p) and len(x) > len(p) + 2: return x[len(p):]
    return x
PR = [('יהודה', 'כלב', 'יפנה'), ('שמעון', 'שמואל', 'עמיהוד'), ('בנימן', 'אלידד', 'כסלון'), ('דן', 'בקי', 'יגלי'), ('מנשה', 'חניאל', 'אפד'), ('אפרים', 'קמואל', 'שפטן'), ('זבולן', 'אליצפן', 'פרנך'), ('יששכר', 'פלטיאל', 'עזן'), ('אשר', 'אחיהוד', 'שלמי'), ('נפתלי', 'פדהאל', 'עמיהוד')]
print('EACH PRINCE\'S AND FATHER\'S NAME — every seat Bible-wide (the bare token and its prefixed forms, morph Np):')
for tribe, man, father in PR:
    for nm in (man, father):
        seats = sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() for x, m, _ in ws if bare_name(x) == nm and m and 'Np' in m})
        print(f'  {tribe} {nm}: {len(seats)} {seats}')
print('Gen 22:21:', words('Gen', 22, 21), '| Exod 6:22:', words('Exod', 6, 22), '| Num 3:30:', words('Num', 3, 30), '| Lev 10:4:', words('Lev', 10, 4)[:7], '| 2Sam 3:15:', words('2Sam', 3, 15), '| 1Sam 25:44:', words('1Sam', 25, 44), '| 1Chr 5:31 (Bukki):', words('1Chr', 5, 31), '| 1Sam 1:20:', words('1Sam', 1, 20), '| 1Chr 7:2:', words('1Chr', 7, 2)[:8], '| 1Chr 7:39:', words('1Chr', 7, 39), '| 1Chr 8:7:', words('1Chr', 8, 7), '| 2Sam 13:37:', words('2Sam', 13, 37)[:8], '| 1Chr 27:17:', words('1Chr', 27, 17))
print('El-names among the ten princes (the token containing אל):', [m for _, m, _ in PR if 'אל' in m], '| among the fathers:', [f for _, _, f in PR if 'אל' in f], '| -הוד names:', [n for t in PR for n in t[1:] if n.endswith('הוד')])
# THE TRIBES' ORDER IN EVERY ROSTER
TRIBE = {'ראובן': 'Reuben', 'שמעון': 'Simeon', 'לוי': 'Levi', 'יהודה': 'Judah', 'יששכר': 'Issachar', 'זבולן': 'Zebulun', 'זבלון': 'Zebulun', 'זבולון': 'Zebulun', 'אפרים': 'Ephraim', 'מנשה': 'Manasseh', 'בנימן': 'Benjamin', 'בנימין': 'Benjamin', 'דן': 'Dan', 'אשר': 'Asher', 'גד': 'Gad', 'נפתלי': 'Naphtali', 'יוסף': 'Joseph'}
def order(b, c, v1, v2):
    seen = []
    for v in range(v1, v2 + 1):
        for x, m, _ in by[(b, c, v)]:
            bn = bare_name(x) if x not in TRIBE else x
            if bn in TRIBE and m and ('Np' in m or 'Ng' in m) and TRIBE[bn] not in seen: seen.append(TRIBE[bn])
    return seen
for label, (b, c, v1, v2) in {'Num 1:5-15': ('Num', 1, 5, 15), 'Num 1:20-43': ('Num', 1, 20, 43), 'Num 2:3-31': ('Num', 2, 3, 31), 'Num 7:12-83': ('Num', 7, 12, 83), 'Num 10:14-27': ('Num', 10, 14, 27), 'Num 13:4-15': ('Num', 13, 4, 15), 'Num 26:5-50': ('Num', 26, 5, 50), 'Num 34:19-28': ('Num', 34, 19, 28), 'Gen 49:3-27': ('Gen', 49, 3, 27), 'Deut 33:6-25': ('Deut', 33, 6, 25), 'Gen 46:9-24': ('Gen', 46, 9, 24), 'Exod 1:2-4': ('Exod', 1, 2, 4), 'Deut 27:12-13': ('Deut', 27, 12, 13), 'Ezek 48:1-7': ('Ezek', 48, 1, 7), 'Ezek 48:23-27': ('Ezek', 48, 23, 27), 'Josh 15-19 (lots)': ('Josh', 15, 1, 1)}.items():
    print(f'  ORDER {label}: {order(b, c, v1, v2)}')
print('  Joshua\'s lot chapters: 15 Judah; 16-17 Joseph (Ephraim 16:5, Manasseh 17:1); 18:11 Benjamin; 19:1 Simeon; 19:10 Zebulun; 19:17 Issachar; 19:24 Asher; 19:32 Naphtali; 19:40 Dan — the heads:', [(c, v, words('Josh', c, v)[:7]) for c, v in ((15, 1), (16, 1), (17, 1), (18, 11), (19, 1), (19, 10), (19, 17), (19, 24), (19, 32), (19, 40))])
print('Manasseh before Ephraim seats (the two names in one roster with Manasseh first):', [(label) for label in ('Num 26:28-37', 'Num 34:23-24') ], '| Num 26:28:', words('Num', 26, 28), '| Num 1:10:', words('Num', 1, 10), '| Gen 48:1 / 48:5 / 48:20:', words('Gen', 48, 1)[-4:], words('Gen', 48, 5)[-4:], words('Gen', 48, 20)[-4:], '| Zebulun before Issachar: Gen 49:13-14 heads:', words('Gen', 49, 13)[:2], words('Gen', 49, 14)[:2], '| Deut 33:18:', words('Deut', 33, 18))
print('לבני יוסף seats Torah:', phrase(['לבני', 'יוסף'], T), '| Num 1:10:', words('Num', 1, 10), '| Num 26:28:', words('Num', 26, 28), '| Josh 16:1 / 17:1:', words('Josh', 16, 1)[:5], words('Josh', 17, 1)[:5])
print('---- 34:29 THE CLOSER')
print('34:29:', wm('Num', 34, 29), '| אלה אשר צוה יהוה:', phrase(['אלה', 'אשר', 'צוה', 'יהוה']), '| Num 30:17 / 36:13 / Lev 27:34 / Lev 26:46:', words('Num', 30, 17)[:5], words('Num', 36, 13)[:6], words('Lev', 27, 34)[:5], words('Lev', 26, 46)[:5], '| כאשר צוה יהוה seats in Num 34:', [s for s in phrase(['כאשר', 'צוה', 'יהוה']) if s.startswith('Num 34')], '| ביד משה receipts Josh 14:2:', words('Josh', 14, 2), '| Onkelos 34:29:', aramaic(34, 29))
print('---- ONKELOS 34 — the renderings on the plain Aramaic')
for v in range(1, NV + 1): print(f'  ONK {v}: {" ".join(aramaic(34, v))}')
print('רקם גיאה seats Onkelos Numbers:', onk_seats('רקם גיאה'), '| רקם seats:', onk_seats('רקם'), '| למטי חמת:', onk_seats('למטי חמת'), onk_seats('מטי חמת'), '| ימא רבא:', onk_seats('ימא רבא'), '| ימא דמלחא:', onk_seats('ימא דמלחא'), '| רוח דרומא:', onk_seats('רוח דרומא'), '| רוח:', onk_seats(' רוח '), '| תתפלג:', onk_seats('תתפלג'), '| עדבא:', onk_seats('עדב'), '| פלגות שבטא:', onk_seats('פלגות שבטא'), '| מימרא in 34:', [(v, aramaic(34, v).count('מימרא')) for v in range(1, 30) if 'מימרא' in aramaic(34, v)], '| מפקנוהי:', onk_seats('מפקנוהי'), '| תכונון:', onk_seats('תכונון'), '| ויסחר:', onk_seats('ויסחר'), '| מסיפי:', onk_seats('מסיפי'), '| אחסנ tokens in 34:', [(v, x) for v in range(1, 30) for x in aramaic(34, v) if 'אחסנ' in x or 'חסנ' in x])
print('---- THE STORE\'S GLOSSES AT THE CHAPTER\'S SEATS (the display layer; the worst read back)')
for v, tok in ((3, 'פאת'), (3, 'גבול'), (3, 'המלח'), (3, 'ממדבר'), (4, 'ונסב'), (4, 'למעלה'), (4, 'לקדש'), (4, 'חצר'), (4, 'ויצא'), (4, 'תוצאתיו'), (5, 'נחלה'), (7, 'צפון'), (7, 'תתאו'), (8, 'לבא'), (10, 'והתאויתם'), (11, 'ומחה'), (11, 'כתף'), (11, 'הרבלה'), (11, 'לעין'), (12, 'סביב'), (12, 'הירדנה'), (13, 'תתנחלו'), (13, 'בגורל'), (13, 'המטות'), (15, 'מעבר'), (15, 'קדמה'), (15, 'מזרחה'), (17, 'ינחלו'), (17, 'נון'), (18, 'לנחל'), (22, 'דן'), (2, 'תפל'), (2, 'לגבלתיה'), (13, 'לתשעת')):
    print('  ', v, tok, store.execute("SELECT w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=34 AND v.verse=? AND REPLACE(w.he_plain,'/','')=? ORDER BY w.idx", (v, tok)).fetchall())
ov = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
print('override rows naming Num.34:', re.findall(r'"Num\.34\.[^"]+"', ov), '| by_gloss keys present among the chapter\'s bad glosses:', [k for k in ('in-pebble', 'cord', 'the-cord', 'the-powder', 'mouth-in-a-figurative-sense', 'and-revolve', 'hidden', 'and-stroke', 'circle', 'Daniel', 'Non', 'from-pasture', 'and-bring-forth', 'inherit--mode-of-descent)', 'to-inherit--mode-of-descent)', 'front-suffix', 'sunrise-suffix', 'the-Jordan-suffix', 'from-region-across', 'to-?', 'from-?', '?', 'come/bring', 'the-seas', 'seas', 'mark-off', 'and-extend', 'exit-him/its') if f'"{k}"' in ov or f' {k}:' in ov or f"'{k}'" in ov])
print('override file head (the two forms):', ov[:600])
# THE REGISTER GATE'S NUM 34 SEATS
rd = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read()
print('register_dispositions entries naming Num 34:', [l for l in rd.split('\n') if 'Num 34' in l][:12])
