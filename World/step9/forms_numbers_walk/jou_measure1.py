import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 13 — THE JOURNEYS, Numbers 33:1-56 (2026-09-12): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED
# from the Tanakh DB, the snapshot store and the shelf's bytes, so that jou_ink.py's asserts are typed FROM THE PRINT (the standing lesson: the
# measurement pass first, then the asserts). Nothing asserted here. Sitting 12's form (gad_measure1.py).
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
C = 33; NV = 56
def words(b, c, v): return [x for x, _, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m, _ in by[(b, c, v)]]
def hits(sub, books=None, exact=True): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _, _ in ws)})
def phrase(seq, books=None):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books)))
def cnt_in(pred, c=C): return sum(1 for v in range(1, NV + 1) for x, m, _ in by[('Num', c, v)] if pred(x, m))
def seats_in(pred, c=C): return [(v, x) for v in range(1, NV + 1) for x, m, _ in by[('Num', c, v)] if pred(x, m)]
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']; onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
def aramaic(c, v): return [plain(x) for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']; sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
print('---- THE HEADING AND THE FRAME (33:1-2)')
print('אלה מסעי:', phrase(['אלה', 'מסעי']), '| מסע-tokens Bible:', sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() for x, _, _ in ws if re.match(r'^(ל|ו|ב)?מסע', x)}))
HEADS = sorted({f'{b} {c}:{v} {" ".join(w[:2])}' for (b, c, v), ws in by.items() if b in T for w in [[x for x, _, _ in ws]] if w[0] == 'אלה' and w[1] not in ('הדברים',) and len(w) > 1 and (b, c, v) not in ()})
print('verse-initial אלה + noun in the Torah (the heading form):', len(HEADS), HEADS)
print('ואלה:', len(sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T and [x for x, _, _ in ws][0] == 'ואלה'})))
print('לצבאתם seats:', U('לצבאתם'), '| Exod 12:41, 51:', words('Exod', 12, 41), words('Exod', 12, 51), '| Exod 6:26:', words('Exod', 6, 26), '| Exod 7:4:', words('Exod', 7, 4)[-6:])
print('ביד משה ואהרן:', phrase(['ביד', 'משה', 'ואהרן']), '| ביד משה count Torah:', len(phrase(['ביד', 'משה'], T)), phrase(['ביד', 'משה'], T), '| Ps 77:21:', words('Ps', 77, 21), '| Mic 6:4:', words('Mic', 6, 4))
print('ויכתב משה:', phrase(['ויכתב', 'משה']), '| ויכתב seats Torah:', U('ויכתב', books=T), '| Exod 24:4:', words('Exod', 24, 4)[:6], '| Deut 31:9:', words('Deut', 31, 9)[:5], '| Deut 31:22:', words('Deut', 31, 22)[:5], '| Exod 17:14:', words('Exod', 17, 14)[:8])
print('33:2 tokens:', words('Num', 33, 2), '| מוצאיהם:', U('מוצאיהם', 'למוצאיהם'), '| מסעיהם:', U('מסעיהם', 'למסעיהם'), '| Exod 40:36, 38:', words('Exod', 40, 36), words('Exod', 40, 38)[-3:], '| Num 10:12:', words('Num', 10, 12), '| Num 10:28:', words('Num', 10, 28))
print('על פי יהוה seats Bible:', len(phrase(['על', 'פי', 'יהוה'])), '| in Num:', [s for s in phrase(['על', 'פי', 'יהוה']) if s.startswith('Num')], '| in 33:', seats_in(lambda x, m: x == 'פי'), '| Torah:', len(phrase(['על', 'פי', 'יהוה'], T)))
print('Onkelos 33:2:', aramaic(33, 2), '| Onkelos 33:38:', aramaic(33, 38), '| מימרא tokens in Onkelos 33:', [(v, aramaic(33, v).count('מימרא')) for v in range(1, 57) if 'מימרא' in aramaic(33, v)])
print('---- THE DATE LINE (33:3-4)')
print('33:3 tokens:', words('Num', 33, 3), '| Exod 12:37:', words('Exod', 12, 37), '| 33:5:', words('Num', 33, 5), '| Exod 13:20:', words('Exod', 13, 20), '| 33:6:', words('Num', 33, 6))
print('רעמסס seats:', U('רעמסס', 'מרעמסס'), '| Gen 47:11:', words('Gen', 47, 11)[-5:], '| Exod 1:11:', words('Exod', 1, 11)[-5:])
print('בחמשה עשר יום לחדש הראשון:', phrase(['בחמשה', 'עשר', 'יום', 'לחדש', 'הראשון']), '| בחמשה עשר יום לחדש:', len(phrase(['בחמשה', 'עשר', 'יום', 'לחדש'])), phrase(['בחמשה', 'עשר', 'יום', 'לחדש']), '| Lev 23:6:', words('Lev', 23, 6)[:7], '| Num 28:17:', words('Num', 28, 17)[:6], '| Exod 12:18:', words('Exod', 12, 18))
print('ממחרת הפסח:', phrase(['ממחרת', 'הפסח']), '| Josh 5:10-12:', words('Josh', 5, 10), words('Josh', 5, 11), words('Josh', 5, 12), '| ממחרת seats Torah:', len(U('ממחרת', books=T)), U('ממחרת', books=T), '| Lev 23:11, 15:', words('Lev', 23, 11)[-3:], words('Lev', 23, 15)[:4])
print('ביד רמה:', phrase(['ביד', 'רמה']), '| Exod 14:8:', words('Exod', 14, 8), '| Num 15:30:', words('Num', 15, 30)[:8], '| Deut 32:27:', words('Deut', 32, 27)[-7:], '| Isa 26:11:', words('Isa', 26, 11)[:4], '| Onkelos 33:3:', aramaic(33, 3), '| Onkelos 15:30:', aramaic(15, 30))
print('לעיני כל מצרים:', phrase(['לעיני', 'כל', 'מצרים']), '| לעיני מצרים:', phrase(['לעיני', 'מצרים']), '| Exod 12:33:', words('Exod', 12, 33), '| Exod 11:8:', words('Exod', 11, 8)[:8])
print('33:4 tokens:', words('Num', 33, 4), '| מקברים:', U('מקברים'), '| Exod 12:29-30:', words('Exod', 12, 29), words('Exod', 12, 30))
print('ובאלהיהם עשה יהוה שפטים:', phrase(['ובאלהיהם', 'עשה', 'יהוה', 'שפטים']), '| Exod 12:12:', words('Exod', 12, 12), '| אעשה שפטים:', phrase(['אעשה', 'שפטים']), '| עשה שפטים:', phrase(['עשה', 'שפטים']), '| שפטים seats:', U('שפטים', 'ושפטים', 'בשפטים'), '| Exod 6:6, 7:4:', words('Exod', 6, 6)[-4:], words('Exod', 7, 4)[-4:], '| Onkelos 33:4:', aramaic(33, 4), '| Onkelos 12:12 not on the shelf (Exodus)')
print('הכה יהוה בהם:', phrase(['הכה', 'יהוה', 'בהם']), '| כל בכור in Exod 12-13:', [s for s in phrase(['כל', 'בכור']) if s.startswith('Exod 1')])
print('---- THE STATIONS AGAINST THEIR FIRST TELLINGS')
print('33:7 tokens:', words('Num', 33, 7), '| Exod 14:2:', words('Exod', 14, 2), '| Exod 14:9:', words('Exod', 14, 9), '| וישב seats 33:', seats_in(lambda x, m: x == 'וישב'), '| וישבו in Exod 14:2 morph:', [(x, m) for x, m, _ in by[('Exod', 14, 2)] if x.startswith('ויש')])
print('פי החירת:', phrase(['פי', 'החירת']), '| החירת:', U('החירת'), '| בעל צפון:', phrase(['בעל', 'צפון']), '| מגדל seats Torah:', U('מגדל', books=T))
print('33:8 tokens:', words('Num', 33, 8), '| Exod 14:22:', words('Exod', 14, 22), '| Exod 15:22:', words('Exod', 15, 22), '| ויעברו בתוך הים:', phrase(['ויעברו', 'בתוך', 'הים']), '| בתוך הים:', phrase(['בתוך', 'הים']), '| שלשת ימים במדבר:', phrase(['שלשת', 'ימים', 'במדבר']), '| דרך שלשת ימים:', phrase(['דרך', 'שלשת', 'ימים']), '| מדבר שור:', phrase(['מדבר', 'שור']), '| מדבר אתם:', phrase(['במדבר', 'אתם']), '| Exod 15:23:', words('Exod', 15, 23))
print('33:9 tokens:', words('Num', 33, 9), '| Exod 15:27:', words('Exod', 15, 27), '| שתים עשרה עינת מים:', phrase(['שתים', 'עשרה', 'עינת', 'מים']), '| ושבעים תמרים:', phrase(['ושבעים', 'תמרים']), '| אילם seats:', U('אילם', 'אילמה', 'מאילם', 'באילם', 'ובאילם'))
print('ים סוף seats Torah:', phrase(['ים', 'סוף'], T), '| ויחנו על ים סוף:', phrase(['ויחנו', 'על', 'ים', 'סוף']), '| Exod 16:1:', words('Exod', 16, 1), '| מדבר סין seats:', phrase(['מדבר', 'סין']), '| דפקה:', U('דפקה', 'בדפקה', 'מדפקה'), '| אלוש:', U('אלוש', 'באלוש', 'מאלוש'))
print('33:14 tokens:', words('Num', 33, 14), '| Exod 17:1:', words('Exod', 17, 1), '| ואין מים לשתת העם:', phrase(['ואין', 'מים', 'לשתת', 'העם']), '| מים לעם לשתות:', phrase(['מים', 'לעם', 'לשתות']), '| רפידם seats:', U('רפידם', 'ברפידם', 'מרפידם'))
print('Exod 19:1-2:', words('Exod', 19, 1), words('Exod', 19, 2), '| ויחנו במדבר סיני:', phrase(['ויחנו', 'במדבר', 'סיני']), '| מדבר סיני seats Bible:', len(phrase(['מדבר', 'סיני'])))
print('Num 11:34-35:', words('Num', 11, 34), words('Num', 11, 35), '| Num 12:16:', words('Num', 12, 16), '| Num 10:12:', words('Num', 10, 12), '| Num 13:3, 26:', words('Num', 13, 3)[:6], words('Num', 13, 26)[:9], '| קברות התאוה seats:', phrase(['קברות', 'התאוה']), phrase(['בקברת', 'התאוה']), phrase(['מקברת', 'התאוה']), '| Deut 9:22:', words('Deut', 9, 22), '| חצרות seats:', U('חצרות', 'בחצרות', 'מחצרות', 'חצרת', 'בחצרת', 'מחצרת'), '| רתמה:', U('רתמה', 'ברתמה', 'מרתמה'), '| מדבר פארן:', phrase(['מדבר', 'פארן']), phrase(['במדבר', 'פארן']))
STN = [(19, 'רמן', 'פרץ'), (20, 'לבנה',), (21, 'רסה',), (22, 'קהלתה',), (23, 'הר', 'שפר'), (24, 'חרדה',), (25, 'מקהלת',), (26, 'תחת',), (27, 'תרח',), (28, 'מתקה',), (29, 'חשמנה',), (30, 'מסרות',), (31, 'בני', 'יעקן'), (32, 'חר', 'הגדגד'), (33, 'יטבתה',), (34, 'עברנה',), (35, 'עציון', 'גבר')]
print('THE STATIONS 33:19-35 — each name\'s seats Bible-wide (the bare token and its prefixed forms):')
for t in STN:
    v = t[0]; name = t[-1]
    forms = sorted({x for (b, c, vv), ws in by.items() for x, _, _ in ws if x.endswith(name) and len(x) - len(name) <= 2 and (x == name or x[0] in 'במול')})
    print(f'  33:{v} {" ".join(t[1:])}: forms {forms} seats', sorted({f'{b} {c}:{vv}' for (b, c, vv), ws in by.items() for x, _, _ in ws if x in forms}))
print('Deut 10:6-7:', words('Deut', 10, 6), '|', words('Deut', 10, 7), '| Deut 10:6 morphs:', morphs('Deut', 10, 6), '| מוסרה:', U('מוסרה', 'מוסרות', 'מסרות', 'ממסרות', 'במסרות'), '| בארת בני יעקן:', phrase(['בארת', 'בני', 'יעקן']), '| הגדגדה / חר הגדגד:', U('הגדגדה', 'הגדגד'), '| יטבתה:', U('יטבתה', 'ביטבתה', 'מיטבתה'), '| Deut 2:8:', words('Deut', 2, 8), '| עציון גבר seats:', phrase(['עציון', 'גבר']), phrase(['בעציון', 'גבר']), phrase(['מעציון', 'גבר']), '| 1Kgs 9:26:', words('1Kgs', 9, 26)[:9], '| Deut 1:2:', words('Deut', 1, 2), '| Deut 1:19:', words('Deut', 1, 19))
print('33:36-37:', words('Num', 33, 36), words('Num', 33, 37), '| Num 20:1:', words('Num', 20, 1), '| Num 20:22-23:', words('Num', 20, 22), words('Num', 20, 23), '| מדבר צן seats:', phrase(['מדבר', 'צן']), phrase(['במדבר', 'צן']), phrase(['ממדבר', 'צן']), '| הוא קדש:', phrase(['הוא', 'קדש']), '| בקצה ארץ אדום:', phrase(['בקצה', 'ארץ', 'אדום']), '| על גבול ארץ אדום:', phrase(['על', 'גבול', 'ארץ', 'אדום']), '| הר ההר seats:', phrase(['הר', 'ההר']), phrase(['בהר', 'ההר']), phrase(['מהר', 'ההר']), '| Onkelos 33:36-37:', aramaic(33, 36), aramaic(33, 37))
print('Onkelos Numbers verses with רקם (Rekem):', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'רקם' in clean(onk_he[c][v])], '| with קברי דמשאלי:', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'דמשאלי' in clean(onk_he[c][v])], '| with הור טורא:', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'הור טורא' in clean(onk_he[c][v]) or 'להור טורא' in clean(onk_he[c][v]) or 'בהור טורא' in clean(onk_he[c][v]) or 'מהור טורא' in clean(onk_he[c][v])], '| with מישריא דמואב:', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'מישריא דמואב' in clean(onk_he[c][v])], '| with מגזת / מגזתא:', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'מגזת' in clean(onk_he[c][v])], '| with בריש גלי:', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'בריש גלי' in clean(onk_he[c][v])], '| with טעות:', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'טעות' in clean(onk_he[c][v]) or 'טעו' in clean(onk_he[c][v])][:20])
print('---- AARON\'S DEATH (33:38-39) AND ARAD (33:40)')
print('33:38 tokens:', words('Num', 33, 38), '| Num 20:23-28:', [words('Num', 20, v) for v in (23, 24, 25, 27, 28)], '| Num 20:29:', words('Num', 20, 29), '| Deut 32:50:', words('Deut', 32, 50), '| Deut 10:6:', words('Deut', 10, 6))
print('בשנת הארבעים:', U('הארבעים'), phrase(['בשנת', 'הארבעים']), '| Deut 1:3:', words('Deut', 1, 3), '| 1Kgs 6:1:', words('1Kgs', 6, 1)[:10], '| לצאת בני ישראל מארץ מצרים:', phrase(['לצאת', 'בני', 'ישראל', 'מארץ', 'מצרים']), '| Exod 16:1, 19:1, Num 1:1, 9:1:', words('Exod', 16, 1)[-6:], words('Exod', 19, 1)[:6], words('Num', 1, 1)[-9:], words('Num', 9, 1)[-8:], '| בחדש החמישי:', phrase(['בחדש', 'החמישי']), '| באחד לחדש seats Torah:', phrase(['באחד', 'לחדש'], T))
print('33:39 tokens:', words('Num', 33, 39), '| Exod 7:7:', words('Exod', 7, 7), '| Deut 34:7:', words('Deut', 34, 7), '| Deut 31:2:', words('Deut', 31, 2)[:7], '| במתו:', U('במתו'), '| Gen 50:26:', words('Gen', 50, 26)[:6])
print('33:40 tokens:', words('Num', 33, 40), '| Num 21:1:', words('Num', 21, 1), '| Num 21:2-3:', words('Num', 21, 2), words('Num', 21, 3), '| מלך ערד:', phrase(['מלך', 'ערד']), '| ערד seats:', U('ערד'), '| וישמע הכנעני:', phrase(['וישמע', 'הכנעני']), '| Onkelos 33:40:', aramaic(33, 40), '| Onkelos 21:1:', aramaic(21, 1))
print('---- THE LAST STATIONS (33:41-49) AGAINST CHAPTER 21 AND THE FORMULA')
print('צלמנה:', U('צלמנה', 'בצלמנה', 'מצלמנה'), '| פונן:', U('פונן', 'בפונן', 'מפונן'), '| אבת:', U('אבת', 'באבת', 'מאבת', 'אובת'), '| Num 21:10-11:', words('Num', 21, 10), words('Num', 21, 11), '| עיי העברים:', phrase(['עיי', 'העברים']), phrase(['בעיי', 'העברים']), '| עיים:', U('עיים', 'מעיים', 'ועיים'), '| Josh 15:29:', words('Josh', 15, 29))
print('Num 21:12-20 stations:', [words('Num', 21, v)[:8] for v in range(12, 21)])
print('דיבן גד:', phrase(['דיבן', 'גד']), phrase(['בדיבן', 'גד']), phrase(['מדיבן', 'גד']), '| דיבן seats:', U('דיבן', 'דיבון', 'ודיבן', 'בדיבן', 'מדיבן'), '| Num 21:30:', words('Num', 21, 30), '| Num 32:34:', words('Num', 32, 34))
print('עלמן דבלתימה:', phrase(['עלמן', 'דבלתימה']), phrase(['בעלמן', 'דבלתימה']), phrase(['מעלמן', 'דבלתימה']), '| דבלתים:', U('דבלתים', 'דבלתימה', 'דבלתי'), '| Jer 48:22:', words('Jer', 48, 22), '| Ezek 6:14:', words('Ezek', 6, 14))
print('הרי העברים:', phrase(['הרי', 'העברים']), phrase(['בהרי', 'העברים']), phrase(['מהרי', 'העברים']), '| הר העברים:', phrase(['הר', 'העברים']), '| Num 27:12:', words('Num', 27, 12), '| Deut 32:49:', words('Deut', 32, 49), '| Deut 34:1:', words('Deut', 34, 1)[:8], '| לפני נבו:', phrase(['לפני', 'נבו']), '| נבו seats:', U('נבו', 'ונבו'))
print('בערבת מואב seats:', phrase(['בערבת', 'מואב']), '| ערבות מואב על ירדן ירחו:', phrase(['בערבת', 'מואב', 'על', 'ירדן', 'ירחו']), '| על ירדן ירחו:', phrase(['על', 'ירדן', 'ירחו']), '| Num 22:1:', words('Num', 22, 1), '| Num 36:13:', words('Num', 36, 13), '| Deut 34:1, 8:', words('Deut', 34, 1)[:4], words('Deut', 34, 8)[:6])
print('33:49 tokens:', words('Num', 33, 49), '| בית הישמת:', phrase(['בית', 'הישמת']), phrase(['מבית', 'הישמת']), '| Josh 12:3, 13:20:', words('Josh', 12, 3), words('Josh', 13, 20), '| Ezek 25:9:', words('Ezek', 25, 9), '| אבל השטים:', phrase(['אבל', 'השטים']), '| השטים / שטים:', U('השטים', 'בשטים', 'השטין', 'שטים', 'מהשטים'), '| Num 25:1:', words('Num', 25, 1), '| Josh 2:1, 3:1:', words('Josh', 2, 1)[:6], words('Josh', 3, 1)[:6], '| Mic 6:5:', words('Mic', 6, 5), '| Onkelos 33:49:', aramaic(33, 49), '| Onkelos 25:1:', aramaic(25, 1))
print('---- THE COMMAND (33:50-56)')
print('33:50-51 tokens:', words('Num', 33, 50), words('Num', 33, 51), '| כי אתם עברים את הירדן:', phrase(['כי', 'אתם', 'עברים', 'את', 'הירדן']), '| Num 35:10:', words('Num', 35, 10), '| Deut 11:31:', words('Deut', 11, 31)[:8], '| Josh 1:11:', words('Josh', 1, 11)[-10:], '| וידבר יהוה אל משה בערבת מואב:', phrase(['וידבר', 'יהוה', 'אל', 'משה', 'בערבת', 'מואב']))
print('33:52 tokens:', words('Num', 33, 52), '| והורשתם את כל ישבי הארץ:', phrase(['והורשתם', 'את', 'כל', 'ישבי', 'הארץ']), '| והורשתם:', U('והורשתם'), '| ישבי הארץ seats Torah:', phrase(['ישבי', 'הארץ'], T), '| משכית tokens:', U('משכית', 'משכיתם', 'ומשכית', 'משכיות'), '| Lev 26:1:', words('Lev', 26, 1), '| צלמי מסכתם:', phrase(['צלמי', 'מסכתם']), '| צלמי seats:', U('צלמי'), '| מסכה tokens Torah:', U('מסכה', 'מסכתם', 'ומסכה', 'מסכת', books=T), '| במתם / במות:', U('במתם', 'במתיכם', 'במות', 'הבמות', 'במותיכם', books=T), '| Lev 26:30:', words('Lev', 26, 30), '| תשמידו:', U('תשמידו'), '| ואבדתם ... תאבדו:', U('ואבדתם', 'תאבדו', 'תאבדון'), '| Deut 12:2-3:', words('Deut', 12, 2), words('Deut', 12, 3), '| Exod 23:24:', words('Exod', 23, 24), '| Exod 34:13:', words('Exod', 34, 13), '| Deut 7:5:', words('Deut', 7, 5), '| Onkelos 33:52:', aramaic(33, 52))
print('33:53 tokens:', words('Num', 33, 53), '| והורשתם את הארץ:', phrase(['והורשתם', 'את', 'הארץ']), '| וישבתם בה:', phrase(['וישבתם', 'בה']), '| כי לכם נתתי את הארץ:', phrase(['כי', 'לכם', 'נתתי', 'את', 'הארץ']), '| לרשת אתה:', phrase(['לרשת', 'אתה']), '| Deut 1:8:', words('Deut', 1, 8)[-6:])
print('33:54 tokens:', words('Num', 33, 54), '| Num 26:52-56:', [words('Num', 26, v) for v in range(52, 57)], '| והתנחלתם:', U('והתנחלתם'), '| בגורל seats Torah:', U('בגורל', books=T), '| לרב תרבו:', phrase(['לרב', 'תרבו']), '| לרב תרבה:', phrase(['לרב', 'תרבה']), '| ולמעט תמעיט:', phrase(['ולמעט', 'תמעיט']), '| אל אשר יצא לו שמה הגורל:', phrase(['אל', 'אשר', 'יצא', 'לו', 'שמה', 'הגורל']), '| למטות אבתיכם:', phrase(['למטות', 'אבתיכם']), '| תתנחלו:', U('תתנחלו'), '| Num 34:13:', words('Num', 34, 13), '| Josh 14:2:', words('Josh', 14, 2), '| Onkelos 33:54:', aramaic(33, 54), '| Onkelos 26:54-56:', aramaic(26, 54), aramaic(26, 55), aramaic(26, 56))
print('33:55 tokens:', words('Num', 33, 55), '| ואם לא תורישו:', phrase(['ואם', 'לא', 'תורישו']), '| תורישו:', U('תורישו'), '| תותירו:', U('תותירו'), '| לשכים:', U('לשכים', 'שכים'), '| ולצנינם / צננים:', U('ולצנינם', 'צנינם', 'ולצננים', 'צננים', 'לצננים'), '| בצדיכם:', U('בצדיכם'), '| Josh 23:13:', words('Josh', 23, 13), '| Judg 2:3:', words('Judg', 2, 3), '| Ezek 28:24:', words('Ezek', 28, 24), '| וצררו:', U('וצררו', 'צררו', 'וצרר'), '| Num 25:18:', words('Num', 25, 18)[:4], '| Onkelos 33:55:', aramaic(33, 55))
print('33:56 tokens:', words('Num', 33, 56), '| דמיתי:', U('דמיתי'), '| כאשר דמיתי:', phrase(['כאשר', 'דמיתי']), '| Isa 14:24:', words('Isa', 14, 24), '| Deut 8:20:', words('Deut', 8, 20), '| Onkelos 33:56:', aramaic(33, 56))
print('---- THE REGISTER, THE FRAME, THE NAMES')
DIV = {}
for (b, c, v), ws in by.items():
    if b != 'Num': continue
    w = [x for x, _, _ in ws]
    if any(w[i] in ('ויאמר', 'וידבר') and w[i + 1] == 'יהוה' for i in range(len(w) - 1)): DIV.setdefault(c, []).append(v)
print('divine-frame verses in 33:', DIV.get(33), '| Numbers chapters WITHOUT one:', [c for c in range(1, 37) if c not in DIV])
REG = [(v, x, m) for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if m and re.search(r'V.w', m)]
print('narrative verbs:', len(REG), '| verses:', len({v for v, _, _ in REG}), '| not journey/camp:', [(v, x) for v, x, _ in REG if x not in ('ויסעו', 'ויחנו')])
JV = [v for v in range(1, NV + 1) for x, _, _ in by[('Num', C, v)] if x == 'ויסעו']; CVv = [v for v in range(1, NV + 1) for x, _, _ in by[('Num', C, v)] if x == 'ויחנו']
print('ויסעו verses:', len(JV), JV, '| ויחנו verses:', len(CVv), CVv, '| both:', len(set(JV) & set(CVv)), '| journey only:', sorted(set(JV) - set(CVv)), '| camp only:', sorted(set(CVv) - set(JV)))
print('ויסעו tokens Bible-wide:', len(U('ויסעו')), '| in Num:', len([s for s in U('ויסעו') if s.startswith('Num')]), '| ויחנו Bible-wide:', len(U('ויחנו')), '| in Num:', len([s for s in U('ויחנו') if s.startswith('Num')]))
CAMPS = []
for v in range(1, NV + 1):
    w = words('Num', C, v)
    if 'ויחנו' in w:
        i = w.index('ויחנו'); CAMPS.append((v, ' '.join(w[i + 1:i + 4])))
print('THE CAMPS (the tokens after each ויחנו, three wide):', CAMPS)
DEPS = []
for v in range(1, NV + 1):
    w = words('Num', C, v)
    if 'ויסעו' in w:
        i = w.index('ויסעו'); DEPS.append((v, ' '.join(w[i + 1:i + 4])))
print('THE DEPARTURES (the tokens after each ויסעו, three wide):', DEPS)
print('name tokens (Np) in 33:', cnt_in(lambda x, m: m and 'Np' in m), '| distinct:', len({x for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if m and 'Np' in m}))
# THE STATIONS BY CHAPTER: which of the 42 places are named in Exodus 12-19, Numbers 10-21 and Deuteronomy — the bare consonants of each camp's head token
HEADS_C = []
for v, s in CAMPS:
    tok = s.split()[0]
    bare = tok[1:] if tok[0] in 'ב' and tok not in ('בני',) else tok
    HEADS_C.append((v, tok, bare))
print('camp head tokens and their bare forms:', HEADS_C)
print('---- THE HEBREW ROW CENSUS OF THE SIFREI (the cross rows named by the dump: 133:3, 112:2, 82:1, 86:1, 98:1, 136:2) — both files, whole')
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
for p, r in ((133, 3), (112, 2), (82, 1), (86, 1), (98, 1), (136, 2)):
    print(f'\n## Sifrei {p}:{r}\n{E(p, r)[:1800]}\n-- HE: {Hb(p, r)[:1200]}')
print('\n---- THE STORE\'S GLOSSES AT THE CHAPTER\'S SEATS (the display layer; the worst read back)')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
for v, tok in ((2, 'ויכתב'), (3, 'הפסח'), (3, 'רמה'), (4, 'שפטים'), (6, 'המדבר'), (44, 'בגבול'), (52, 'ואבדתם'), (52, 'משכיתם'), (52, 'מסכתם'), (52, 'במתם'), (52, 'תשמידו'), (54, 'בגורל'), (55, 'תותירו'), (55, 'לשכים'), (55, 'וצררו'), (56, 'דמיתי'), (1, 'לצבאתם'), (9, 'עינת'), (16, 'בקברת'), (7, 'פי'), (7, 'בעל'), (49, 'מבית'), (49, 'אבל')):
    print('  ', v, tok, store.execute("SELECT w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=33 AND v.verse=? AND REPLACE(w.he_plain,'/','')=? ORDER BY w.idx", (v, tok)).fetchall())
ov = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
print('override rows naming Num.33:', re.findall(r'"Num\.33\.[^"]+"', ov), '| by_gloss keys for the-pretermission / in-pebble / and-grave:', [k for k in ('the-pretermission', 'in-pebble', 'and-grave', 'and-cramp', 'jut-over', 'compare', 'in-cord', 'desolate', 'elevation', 'pouring-over') if f'"{k}"' in ov or f' {k}:' in ov])
