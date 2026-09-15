import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 12 — GAD AND REUBEN, Numbers 32:1-42 (2026-09-12): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED
# from the Tanakh DB, the snapshot store and the shelf's bytes, so that gad_ink.py's asserts are typed FROM THE PRINT (the standing lesson: the
# measurement pass first, then the asserts). Nothing asserted here. Sitting 11's form (midian_measure1.py).
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
C = 32; NV = 42
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
def accents(w): return [unicodedata.name(ch).replace('HEBREW ACCENT ', '') for ch in w if 0x0591 <= ord(ch) <= 0x05AE]
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']; onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
def aramaic(c, v): return [plain(x) for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
print('---- THE FRAMES AND THE REGISTER')
REG = [(v, x, m) for v in range(1, NV + 1) for x, m, _ in by[('Num', C, v)] if m and re.search(r'V.w', m)]
print('narrative verbs:', REG, '| count', len(REG), '| verses', len({v for v, _, _ in REG}), sorted({v for v, _, _ in REG}))
print('speech verbs in 32:', [(v, x) for v, x, _ in REG if x in ('ויאמר', 'ויאמרו', 'וידבר', 'ויענו', 'ויצו')])
DIV = {}
for (b, c, v), ws in by.items():
    if b != 'Num': continue
    w = [x for x, _, _ in ws]
    if any(w[i] in ('ויאמר', 'וידבר') and w[i + 1] == 'יהוה' for i in range(len(w) - 1)): DIV.setdefault(c, []).append(v)
print('Numbers chapters WITHOUT a divine speech frame (ויאמר/וידבר יהוה anywhere):', [c for c in range(1, 37) if c not in DIV])
print('divine-frame verses per chapter 30-36:', {c: DIV.get(c, []) for c in range(30, 37)})
print('יהוה tokens in 32:', seats_in(lambda x, m: x in ('יהוה', 'ליהוה', 'מיהוה', 'ביהוה')), '| count', cnt_in(lambda x, m: 'יהוה' in x))
print('לפני יהוה in 32:', [(v, i) for v in range(1, NV + 1) for i in range(len(words('Num', C, v)) - 1) if words('Num', C, v)[i:i + 2] == ['לפני', 'יהוה']], '| count', len(phrase(['לפני', 'יהוה'])), 'seats in Bible')
print('ONKELOS on לפני יהוה per verse (קדם עמא דיי / קדם יי):', {v: (aramaic(C, v).count('עמא'), sum(1 for i in range(len(aramaic(C, v)) - 1) if aramaic(C, v)[i:i + 2] == ['קדם', 'יי'])) for v in (4, 20, 21, 22, 27, 29, 32)})
for v in (20, 21, 22, 27, 29, 32): print(f'   ARM {C}:{v}', aramaic(C, v))
print('---- THE CATTLE AND THE LAND (32:1-5)')
print('ומקנה רב:', phrase(['ומקנה', 'רב']), '| מקנה רב:', phrase(['מקנה', 'רב']), '| מקנה tokens 32:', seats_in(lambda x, m: 'מקנ' in x), '| Deut 3:19:', words('Deut', 3, 19), '| 1Chr 5:9:', words('1Chr', 5, 9), '| 2Chr 26:10:', words('2Chr', 26, 10)[-8:])
print('עצום מאד:', phrase(['עצום', 'מאד']), '| Exod 1:7:', words('Exod', 1, 7), '| Gen 13:2:', words('Gen', 13, 2), '| Exod 12:38:', words('Exod', 12, 38))
print('ארץ יעזר:', phrase(['ארץ', 'יעזר']), '| ארץ גלעד:', phrase(['ארץ', 'גלעד']), '| ארץ הגלעד:', phrase(['ארץ', 'הגלעד']), '| יעזר seats:', U('יעזר', 'ויעזר', 'ביעזר', 'מיעזר', 'יעזיר'), '| Num 21:32:', words('Num', 21, 32))
print('מקום מקנה:', phrase(['מקום', 'מקנה']), '| ארץ מקנה:', phrase(['ארץ', 'מקנה']), '| והנה המקום:', phrase(['והנה', 'המקום']))
print('Gen 13:5-6, 10-11:', words('Gen', 13, 5), words('Gen', 13, 6), words('Gen', 13, 10)[:9], words('Gen', 13, 11)[:8], '| Gen 13:13:', words('Gen', 13, 13))
print('ואל נשיאי העדה:', phrase(['ואל', 'נשיאי', 'העדה']), '| נשיאי העדה:', phrase(['נשיאי', 'העדה']), '| Num 27:2:', words('Num', 27, 2)[:12], '| Num 31:13:', words('Num', 31, 13)[:8])
print('32:3 names:', [(x, m) for x, m, _ in by[('Num', C, 3)]], '| Onkelos 32:3:', aramaic(C, 3), '| Onkelos 32:38:', aramaic(C, 38), '| Onkelos 32:35:', aramaic(C, 35))
print('32:4 הכה יהוה:', phrase(['הכה', 'יהוה']), '| לפני עדת ישראל:', phrase(['לפני', 'עדת', 'ישראל']), '| Onkelos 32:4:', aramaic(C, 4))
print('אם מצאנו חן בעיניך:', phrase(['אם', 'מצאנו', 'חן', 'בעיניך']), '| מצאנו חן:', phrase(['מצאנו', 'חן']), '| לאחזה tokens Num:', [s for s in U('לאחזה') if s.startswith('Num')], '| אחזה-tokens 32:', seats_in(lambda x, m: 'אחז' in x), '| Num 27:4, 7:', words('Num', 27, 4)[-4:], words('Num', 27, 7)[-9:])
print('אל תעברנו את הירדן:', phrase(['אל', 'תעברנו', 'את', 'הירדן']), '| תעברנו:', U('תעברנו'), '| Onkelos 32:5:', aramaic(C, 5))
print('---- MOSES\' REBUKE (32:6-15)')
print('האחיכם:', U('האחיכם'), '| ואתם תשבו פה:', phrase(['ואתם', 'תשבו', 'פה']), '| תשבו פה:', phrase(['תשבו', 'פה']), '| שבו לכם פה:', phrase(['שבו', 'לכם', 'פה']), '| יבאו למלחמה:', phrase(['יבאו', 'למלחמה']))
print('THE HINDER-ROOT (the vows\' verb): tokens with ניא/נוא as verbs:', sorted({f"{b} {c}:{v} {x} {m}" for (b, c, v), ws in by.items() for x, m, _ in ws if m and 'V' in m and (re.search(r'ני?א', x) and re.match(r'^(ו|ה|י|ת|וי|וה|ות)?(ה)?נ[יו]א', x))}))
print('  Num 30 tokens:', [(v, x, m) for v in range(1, 18) for x, m, _ in by[('Num', 30, v)] if 'ניא' in x or 'נוא' in x], '| 32:7, 32:9:', [(v, x, m) for v in (7, 9) for x, m, _ in by[('Num', C, v)] if 'ניא' in x or 'נוא' in x], '| Ps 141:5:', words('Ps', 141, 5), '| Ps 33:10:', words('Ps', 33, 10))
print('תנואון KETIV/QERE in the store:')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
print('  store 32:7 tokens:', store.execute("SELECT w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=32 AND v.verse=7 ORDER BY w.idx").fetchall())
print('  store 32:7 token count:', store.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=32 AND v.verse=7").fetchone(), '| DB 32:7 count:', len(words('Num', C, 7)), '| DB 32:7 raw:', [raw for _, _, raw in by[('Num', C, 7)]][:3])
print('  store 1:16 tokens (the known pair):', store.execute("SELECT w.idx, w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=1 AND v.verse=16 ORDER BY w.idx").fetchall()[:6])
print('  store verses in Num 32 whose token count differs from the DB:', [(v, n) for v, n in store.execute("SELECT v.verse, COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=32 GROUP BY v.verse").fetchall() if n != len(words('Num', C, v))])
print('לב בני ישראל:', phrase(['לב', 'בני', 'ישראל']), '| מעבר אל הארץ:', phrase(['מעבר', 'אל', 'הארץ']), '| Deut 1:28:', words('Deut', 1, 28)[:6])
print('כה עשו אבתיכם:', phrase(['כה', 'עשו', 'אבתיכם']), '| מקדש ברנע:', U('מקדש'), '| קדש ברנע seats:', phrase(['קדש', 'ברנע']), '| Num seats:', [s for s in phrase(['קדש', 'ברנע']) if s.startswith('Num')], '| ברנע all:', U('ברנע'))
print('THE SPIES\' VERB at each seat: Num 13:2:', words('Num', 13, 2)[:6], '| 13:16-17:', words('Num', 13, 16)[:6], words('Num', 13, 17)[:8], '| 32:8:', words('Num', C, 8)[-4:], '| Deut 1:22:', words('Deut', 1, 22)[:12], '| Deut 1:24:', words('Deut', 1, 24), '| Josh 2:1:', words('Josh', 2, 1)[:9])
print('לראות את הארץ:', phrase(['לראות', 'את', 'הארץ']), '| לתור את הארץ:', phrase(['לתור', 'את', 'הארץ']), '| לרגל את הארץ:', phrase(['לרגל', 'את', 'הארץ']), '| ויחפרו:', U('ויחפרו'))
print('נחל אשכול:', phrase(['נחל', 'אשכול']), '| ויראו את הארץ:', phrase(['ויראו', 'את', 'הארץ']), '| לבלתי בא:', phrase(['לבלתי', 'בא']))
print('ויחר אף יהוה:', len(phrase(['ויחר', 'אף', 'יהוה'])), 'seats; in 32:', seats_in(lambda x, m: x == 'ויחר'), '| in Num:', [s for s in phrase(['ויחר', 'אף', 'יהוה']) if s.startswith('Num')])
print('ביום ההוא וישבע:', phrase(['ביום', 'ההוא', 'וישבע']), '| וישבע seats Torah:', U('וישבע', books=T), '| Deut 1:34:', words('Deut', 1, 34), '| Num 14:21:', words('Num', 14, 21), '| Num 14:23:', words('Num', 14, 23), '| Num 14:28:', words('Num', 14, 28), '| חי אני in Num:', [s for s in phrase(['חי', 'אני']) if s.startswith('Num')])
print('אם יראו:', phrase(['אם', 'יראו']), '| האנשים העלים ממצרים:', phrase(['האנשים', 'העלים', 'ממצרים']), '| מבן עשרים שנה ומעלה seats:', len(phrase(['מבן', 'עשרים', 'שנה', 'ומעלה'])), [s for s in phrase(['מבן', 'עשרים', 'שנה', 'ומעלה']) if not s.startswith('Num 1:') and not s.startswith('Num 26:')], '| Num 14:29:', words('Num', 14, 29))
print('אשר נשבעתי לאברהם ליצחק וליעקב:', phrase(['נשבעתי', 'לאברהם', 'ליצחק', 'וליעקב']), '| לאברהם ליצחק וליעקב:', len(phrase(['לאברהם', 'ליצחק', 'וליעקב'])), '| Exod 33:1:', words('Exod', 33, 1)[-10:], '| Deut 34:4:', words('Deut', 34, 4)[:10])
print('מלא אחרי (the fill-root + after):', sorted({f"{b} {c}:{v} {' '.join(w[i:i+3])}" for (b, c, v), ws in by.items() for w in [[x for x, _, _ in ws]] for i in range(len(w) - 1) if w[i] in ('מלא', 'מלאו', 'מלאתי') and w[i + 1] in ('אחרי', 'אחר')}), '| Num 14:24:', words('Num', 14, 24), '| Deut 1:36:', words('Deut', 1, 36), '| Josh 14:8-9, 14:', words('Josh', 14, 8)[-4:], words('Josh', 14, 9)[-6:], words('Josh', 14, 14)[-6:], '| 1Kgs 11:6:', words('1Kgs', 11, 6))
print('בלתי כלב:', phrase(['בלתי', 'כלב']), '| כלב בן יפנה seats:', phrase(['כלב', 'בן', 'יפנה']), '| הקנזי:', U('הקנזי', 'קנזי', 'הקנזי'), '| Gen 15:19:', words('Gen', 15, 19), '| Josh 14:6:', words('Josh', 14, 6)[-8:], '| Josh 15:17:', words('Josh', 15, 17)[:6], '| Caleb + Joshua in one verse:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if 'כלב' in [x for x, _, _ in ws] and 'ויהושע' in [x for x, _, _ in ws] or ('כלב' in [x for x, _, _ in ws] and 'יהושע' in [x for x, _, _ in ws])}))
print('Onkelos 32:11-12 (the fear buffer):', aramaic(C, 11)[-4:], aramaic(C, 12)[-4:], '| Onkelos 32:15:', aramaic(C, 15)[:4])
print('ויחר אף יהוה בישראל:', phrase(['ויחר', 'אף', 'יהוה', 'בישראל']), '| וינעם:', U('וינעם'), '| נוע-hiphil tokens:', sorted({f"{b} {c}:{v} {x} {m}" for (b, c, v), ws in by.items() for x, m, _ in ws if m and m.startswith('HVh') and re.match(r'^(ו)?(י|ה|א|ת)?נ[יו]ע', x)}), '| Num 14:33:', words('Num', 14, 33), '| Ps 59:12:', words('Ps', 59, 12)[:6], '| Gen 4:12:', words('Gen', 4, 12)[-3:])
print('ארבעים שנה in Num:', [s for s in phrase(['ארבעים', 'שנה']) if s.startswith('Num')], '| Torah:', phrase(['ארבעים', 'שנה'], T), '| במדבר ארבעים שנה:', phrase(['במדבר', 'ארבעים', 'שנה']))
print('עד תם כל:', phrase(['עד', 'תם', 'כל']), '| Deut 2:14:', words('Deut', 2, 14), '| Josh 5:6:', words('Josh', 5, 6)[:9], '| כל הדור:', phrase(['כל', 'הדור']), '| העשה הרע בעיני יהוה:', phrase(['העשה', 'הרע', 'בעיני', 'יהוה']), '| הרע בעיני יהוה count:', len(phrase(['הרע', 'בעיני', 'יהוה'])), '| Torah:', phrase(['הרע', 'בעיני', 'יהוה'], T))
print('קמתם תחת:', phrase(['קמתם', 'תחת']), '| תחת אבתיכם:', phrase(['תחת', 'אבתיכם']), '| קם תחת:', phrase(['קם', 'תחת']), '| 1Kgs 8:20:', words('1Kgs', 8, 20)[:9], '| תרבות:', U('תרבות'), '| אנשים חטאים:', phrase(['אנשים', 'חטאים']), '| חטאים Torah:', U('חטאים', 'וחטאים', books=T), '| Gen 13:13:', words('Gen', 13, 13), '| Onkelos 32:14:', aramaic(C, 14))
print('לספות:', U('לספות', 'ספות', 'ספו'), '| Isa 30:1:', words('Isa', 30, 1)[-6:], '| Deut 29:18:', words('Deut', 29, 18)[-5:], '| חרון אף יהוה seats:', phrase(['חרון', 'אף', 'יהוה']), '| in Num:', [s for s in phrase(['חרון', 'אף', 'יהוה']) if s.startswith('Num')], '| Num 25:4:', words('Num', 25, 4)[-6:])
print('כי תשובן מאחריו:', phrase(['תשובן', 'מאחריו']), '| להניחו במדבר:', phrase(['להניחו', 'במדבר']), '| להניחו:', U('להניחו'), '| ושחתם:', U('ושחתם'), '| ושחתם לכל העם:', phrase(['ושחתם', 'לכל', 'העם']), '| Onkelos 32:15:', aramaic(C, 15))
print('---- THE OFFER AND THE CONDITION (32:16-32)')
print('ויגשו אליו:', phrase(['ויגשו', 'אליו']), '| גדרת צאן:', phrase(['גדרת', 'צאן']), '| 32:16 order:', words('Num', C, 16), '| 32:24 order:', words('Num', C, 24), '| 32:26 order:', words('Num', C, 26), '| Deut 3:19 order:', words('Deut', 3, 19), '| Josh 1:14 order:', words('Josh', 1, 14)[:5])
print('ערים לטפנו:', phrase(['וערים', 'לטפנו']), phrase(['ערים', 'לטפכם']), '| ערי המבצר:', phrase(['בערי', 'המבצר']), '| ערי מבצר:', phrase(['ערי', 'מבצר']), '| Num 13:19:', words('Num', 13, 19)[-4:])
print('THE ARM-ROOT in 32:', seats_in(lambda x, m: re.match(r'^(ו|נ|ת)?חל(ו|)צ', x) or x.startswith('חלוצ') or x == 'חלוץ'), '| count', cnt_in(lambda x, m: re.match(r'^(ו|נ|ת)?חל(ו|)צ', x) is not None or x == 'חלוץ'), '| חשים:', U('חשים'), '| נחלץ חשים:', phrase(['נחלץ', 'חשים']), '| חלוץ צבא:', phrase(['חלוץ', 'צבא']), '| חלוצי הצבא:', phrase(['חלוצי', 'הצבא']), '| כל חלוץ:', phrase(['כל', 'חלוץ']), '| חמשים (armed) seats:', U('חמשים', 'וחמשים'), '| Exod 13:18:', words('Exod', 13, 18)[-4:], '| Josh 1:14:', words('Josh', 1, 14)[-9:], '| Josh 4:12-13:', words('Josh', 4, 12), words('Josh', 4, 13), '| Josh 6:7:', words('Josh', 6, 7)[-6:], '| Josh 6:13:', words('Josh', 6, 13)[8:14])
print('עד אשר אם:', phrase(['עד', 'אשר', 'אם']), '| הביאנם:', U('הביאנם'), '| אל מקומם:', phrase(['אל', 'מקומם']), '| מפני ישבי הארץ:', phrase(['מפני', 'ישבי', 'הארץ']))
print('לא נשוב אל בתינו:', phrase(['לא', 'נשוב', 'אל', 'בתינו']), '| עד התנחל:', phrase(['עד', 'התנחל']), '| התנחל:', U('התנחל'), '| איש נחלתו:', phrase(['איש', 'נחלתו']), '| Deut 3:20:', words('Deut', 3, 20), '| Josh 1:15:', words('Josh', 1, 15), '| Josh 22:4:', words('Josh', 22, 4))
print('מעבר לירדן והלאה:', phrase(['מעבר', 'לירדן', 'והלאה']), '| מעבר לירדן:', len(phrase(['מעבר', 'לירדן'])), '| מעבר הירדן מזרחה:', phrase(['מעבר', 'הירדן', 'מזרחה']), '| מעבר לירדן מזרחה:', phrase(['מעבר', 'לירדן', 'מזרחה']), '| באה נחלתנו:', phrase(['באה', 'נחלתנו']), '| כי לא ננחל אתם:', phrase(['לא', 'ננחל', 'אתם']))
print('אם tokens in 32:', seats_in(lambda x, m: x in ('אם', 'ואם')), '| אם תעשון את הדבר הזה:', phrase(['אם', 'תעשון', 'את', 'הדבר', 'הזה']), '| אם תחלצו:', phrase(['אם', 'תחלצו']), '| ואם לא תעשון כן:', phrase(['ואם', 'לא', 'תעשון', 'כן']), '| ואם לא יעברו:', phrase(['ואם', 'לא', 'יעברו']), '| אם יעברו:', phrase(['אם', 'יעברו']))
print('ועבר לכם כל חלוץ:', phrase(['ועבר', 'לכם', 'כל', 'חלוץ']), '| עד הורישו את איביו מפניו:', phrase(['עד', 'הורישו', 'את', 'איביו']), '| הורישו:', U('הורישו'), '| Josh 23:5:', words('Josh', 23, 5)[:9])
print('ונכבשה הארץ:', phrase(['ונכבשה', 'הארץ']), '| נכבשה:', U('נכבשה', 'ונכבשה'), '| 1Chr 22:18:', words('1Chr', 22, 18), '| Josh 18:1:', words('Josh', 18, 1), '| Gen 1:28:', words('Gen', 1, 28)[6:9])
print('ואחר תשבו:', phrase(['ואחר', 'תשבו']), '| והייתם נקיים:', phrase(['והייתם', 'נקיים']), '| נקיים מיהוה ומישראל:', phrase(['נקיים', 'מיהוה', 'ומישראל']), '| נקי + מיהוה:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for w in [[x for x, _, _ in ws]] if 'מיהוה' in w and any(x.startswith('נקי') for x in w)}), '| 2Sam 3:28:', words('2Sam', 3, 28), '| Gen 24:41:', words('Gen', 24, 41)[:6], '| Gen 44:10:', words('Gen', 44, 10)[-5:], '| Onkelos 32:22:', aramaic(C, 22))
print('והיתה הארץ הזאת לכם לאחזה:', phrase(['הארץ', 'הזאת', 'לכם', 'לאחזה']), '| לאחזה לפני יהוה:', phrase(['לאחזה', 'לפני', 'יהוה']))
print('הנה חטאתם ליהוה:', phrase(['הנה', 'חטאתם', 'ליהוה']), '| חטאתם ליהוה:', phrase(['חטאתם', 'ליהוה']), '| ודעו חטאתכם:', phrase(['ודעו', 'חטאתכם']), '| חטאתכם אשר תמצא אתכם:', phrase(['חטאתכם', 'אשר', 'תמצא', 'אתכם']), '| תמצא אתכם:', phrase(['תמצא', 'אתכם']), '| Gen 44:16:', words('Gen', 44, 16), '| מצא את עון:', phrase(['מצא', 'את', 'עון']), '| Onkelos 32:23:', aramaic(C, 23))
print('THE UTTERANCE RULE: והיצא מפיכם תעשו:', phrase(['והיצא', 'מפיכם', 'תעשו']), '| היצא מפיו:', phrase(['היצא', 'מפיו']), '| ככל היצא מפיו יעשה:', phrase(['ככל', 'היצא', 'מפיו', 'יעשה']), '| יצא מפיך:', phrase(['יצא', 'מפיך']), '| Judg 11:36:', words('Judg', 11, 36), '| Deut 23:24:', words('Deut', 23, 24), '| Num 30:3:', words('Num', 30, 3), '| Num 30:13:', words('Num', 30, 13)[:6], '| מוצא שפתיך:', phrase(['מוצא', 'שפתיך']), '| Ps 89:35:', words('Ps', 89, 35), '| Onkelos 32:24:', aramaic(C, 24), '| Onkelos 30:3:', aramaic(30, 3)[-6:])
print('בנו לכם ערים:', phrase(['בנו', 'לכם', 'ערים']), '| וגדרת לצנאכם:', phrase(['וגדרת', 'לצנאכם']), '| לצנאכם:', U('לצנאכם'))
print('עבדיך יעשו כאשר אדני מצוה:', phrase(['עבדיך', 'יעשו', 'כאשר', 'אדני', 'מצוה']), '| כאשר אדני מצוה:', phrase(['כאשר', 'אדני', 'מצוה']), '| כאשר אדני דבר:', phrase(['כאשר', 'אדני', 'דבר']), '| אדני (my lord, to Moses) in Num:', [s for s in U('אדני') if s.startswith('Num')], '| Num 11:28:', words('Num', 11, 28)[-4:], '| Num 12:11:', words('Num', 12, 11)[:5], '| Num 36:2:', words('Num', 36, 2)[:4])
print('32:26 the four:', words('Num', C, 26)[:5], '| טפנו נשינו מקננו:', phrase(['טפנו', 'נשינו', 'מקננו']), '| בערי הגלעד:', phrase(['בערי', 'הגלעד']), '| ערי הגלעד:', phrase(['ערי', 'הגלעד']))
print('ויענו בני גד:', phrase(['ויענו', 'בני', 'גד']), '| את אשר דבר יהוה אל עבדיך:', phrase(['את', 'אשר', 'דבר', 'יהוה', 'אל', 'עבדיך']), '| אשר דבר יהוה אל:', len(phrase(['אשר', 'דבר', 'יהוה', 'אל'])), '| כן נעשה:', phrase(['כן', 'נעשה']), '| Onkelos 32:31:', aramaic(C, 31))
print('נחנו (we):', U('נחנו'), '| נחנו נעבר:', phrase(['נחנו', 'נעבר']), '| אחזת נחלתנו:', phrase(['אחזת', 'נחלתנו']), '| אחזת נחלה:', phrase(['אחזת', 'נחלה']), phrase(['אחזת', 'נחלתו']), phrase(['אחזת', 'נחלתם']), '| Num 27:7:', words('Num', 27, 7))
print('ויצו להם משה:', phrase(['ויצו', 'להם', 'משה']), '| ויצו להם:', phrase(['ויצו', 'להם']), '| ראשי אבות המטות:', phrase(['ראשי', 'אבות', 'המטות']), '| ראשי אבות המטות לבני ישראל:', phrase(['ראשי', 'אבות', 'המטות', 'לבני', 'ישראל']), '| Josh 14:1:', words('Josh', 14, 1), '| Josh 19:51:', words('Josh', 19, 51)[:9], '| Josh 21:1:', words('Josh', 21, 1)[:8], '| Num 36:1:', words('Num', 36, 1)[-8:], '| Onkelos 32:28:', aramaic(C, 28))
print('ונאחזו בתככם:', phrase(['ונאחזו', 'בתככם']), '| ונאחזו:', U('ונאחזו'), '| Gen 34:10, 47:27:', words('Gen', 34, 10)[-2:], words('Gen', 47, 27)[-4:], '| בארץ כנען in 32:', seats_in(lambda x, m: x == 'כנען'))
print('---- THE GRANT AND THE CITIES (32:33-42)')
print('ויתן להם משה:', phrase(['ויתן', 'להם', 'משה']), '| ולחצי שבט מנשה:', phrase(['ולחצי', 'שבט', 'מנשה']), '| חצי שבט מנשה all forms:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for w in [[x for x, _, _ in ws]] for i in range(len(w) - 2) if w[i] in ('חצי', 'לחצי', 'ולחצי', 'וחצי') and w[i + 1] == 'שבט' and w[i + 2] in ('מנשה', 'המנשה')}), '| מנשה tokens in 32:', seats_in(lambda x, m: x == 'מנשה'), '| Num 34:13-15:', words('Num', 34, 13)[-6:], words('Num', 34, 14), words('Num', 34, 15))
print('ממלכת סיחן:', phrase(['ממלכת', 'סיחן']), '| ממלכת עוג:', phrase(['ממלכת', 'עוג']), '| Num 21:24-26, 33-35:', words('Num', 21, 24), words('Num', 21, 26), words('Num', 21, 33)[:8], words('Num', 21, 35), '| Deut 3:8:', words('Deut', 3, 8), '| Josh 13:12:', words('Josh', 13, 12)[:9], '| Onkelos 32:33:', aramaic(C, 33))
print('הארץ לעריה:', phrase(['הארץ', 'לעריה']), '| לעריה:', U('לעריה'), '| בגבלת:', U('בגבלת'), '| ערי הארץ סביב:', phrase(['ערי', 'הארץ', 'סביב']))
NAMES = {v: [(x, m) for x, m, _ in by[('Num', C, v)] if m and ('Np' in m)] for v in (3, 34, 35, 36, 37, 38, 39, 40, 41, 42)}
print('NAME TOKENS per verse:', NAMES)
print('Gad built (32:34-36) words:', words('Num', C, 34), words('Num', C, 35), words('Num', C, 36), '| Reuben built (32:37-38):', words('Num', C, 37), words('Num', C, 38))
print('Num 33:45-46:', words('Num', 33, 45), words('Num', 33, 46), '| דיבן גד:', phrase(['דיבן', 'גד']), phrase(['מדיבן', 'גד']))
print('Josh 13:15-28 (Reuben, Gad):'); [print(f'  Josh 13:{v}', words('Josh', 13, v)) for v in range(15, 29)]
print('Josh 13:29-31 (half Manasseh):', words('Josh', 13, 29), words('Josh', 13, 30), words('Josh', 13, 31))
print('Isa 15:2, 4, 6; 16:8-9:', words('Isa', 15, 2), words('Isa', 15, 4)[:4], words('Isa', 15, 6)[:3], words('Isa', 16, 8), words('Isa', 16, 9))
print('Jer 48:1-2, 18-24, 32-34:'); [print(f'  Jer 48:{v}', words('Jer', 48, v)) for v in (1, 2, 18, 19, 21, 22, 23, 24, 32, 33, 34)]
print('Ezek 25:9:', words('Ezek', 25, 9), '| 1Chr 5:8:', words('1Chr', 5, 8))
print('Judg 8:11:', words('Judg', 8, 11), '| יגבהה:', U('יגבהה', 'ויגבהה'), '| נבח:', U('נבח', 'ונבח'), '| קנת:', U('קנת'))
print('name seats: עטרות/עטרת:', U('עטרות', 'ועטרות', 'עטרת', 'ועטרת'), '| דיבן:', U('דיבן', 'ודיבן', 'דיבון', 'מדיבן'), '| נמרה:', U('נמרה', 'ונמרה'), '| נמרים:', U('נמרים'), '| חשבון:', len(U('חשבון', 'וחשבון', 'בחשבון', 'מחשבון')), '| אלעלה:', U('אלעלה', 'ואלעלה', 'אלעלא', 'ואלעלא'), '| שבם/שבמה:', U('שבם', 'ושבם', 'שבמה', 'ושבמה'), '| נבו:', U('נבו', 'ונבו'), '| בען:', U('בען', 'ובען'), '| בעל מעון:', phrase(['בעל', 'מעון']), phrase(['בית', 'בעל', 'מעון']), phrase(['בית', 'מעון']), '| קריתים:', U('קריתים', 'וקריתים', 'קריתימה'), '| ערער:', U('ערער', 'וערער', 'מערער', 'בערער'), '| שופן:', U('שופן'), '| בית הרן/הרם:', phrase(['בית', 'הרן']), phrase(['בית', 'הרם']), '| בית נמרה:', phrase(['בית', 'נמרה']))
print('מוסבת שם:', phrase(['מוסבת', 'שם']), '| מוסבת:', U('מוסבת'), '| ויקראו בשמת:', phrase(['ויקראו', 'בשמת']), '| בשמת:', U('בשמת'), '| שמות הערים:', phrase(['שמות', 'הערים']), '| Onkelos 32:38:', aramaic(C, 38))
print('בני מכיר בן מנשה:', phrase(['בני', 'מכיר', 'בן', 'מנשה']), '| מכיר בן מנשה:', phrase(['מכיר', 'בן', 'מנשה']), '| מכיר seats:', U('מכיר', 'למכיר', 'ומכיר', 'המכירי'), '| Gen 50:23:', words('Gen', 50, 23), '| Num 26:29:', words('Num', 26, 29), '| Josh 17:1:', words('Josh', 17, 1), '| Deut 3:15:', words('Deut', 3, 15), '| Judg 5:14:', words('Judg', 5, 14)[:8])
print('גלעדה:', U('גלעדה'), '| וילכדה:', U('וילכדה'), '| ויורש את האמרי:', phrase(['ויורש', 'את', 'האמרי']), '| ויורש:', U('ויורש'), '| ויתן משה את הגלעד:', phrase(['ויתן', 'משה', 'את', 'הגלעד']), '| וישב בה:', phrase(['וישב', 'בה']))
print('יאיר seats:', U('יאיר', 'ויאיר'), '| יאיר בן מנשה:', phrase(['יאיר', 'בן', 'מנשה']), '| חות יאיר:', phrase(['חות', 'יאיר']), '| חותיהם:', U('חותיהם'), '| הלך וילכד:', phrase(['הלך', 'וילכד']), '| Deut 3:14:', words('Deut', 3, 14), '| Judg 10:3-4:', words('Judg', 10, 3), words('Judg', 10, 4), '| 1Kgs 4:13:', words('1Kgs', 4, 13), '| 1Chr 2:21-23:', words('1Chr', 2, 21), words('1Chr', 2, 22), words('1Chr', 2, 23), '| Josh 13:30:', words('Josh', 13, 30))
print('ויקרא לה נבח בשמו:', phrase(['ויקרא', 'לה', 'נבח', 'בשמו']), '| בשמו (after his name):', phrase(['ויקרא', 'לה']), '| בנתיה seats:', U('בנתיה', 'ובנתיה'), '| Num 21:25, 32:', words('Num', 21, 25), words('Num', 21, 32), '| Onkelos 32:41-42:', aramaic(C, 41), aramaic(C, 42))
print('---- THE ORDER OF THE TWO TRIBES')
def order(b, c, v):
    w = words(b, c, v); r = [i for i, x in enumerate(w) if 'ראובן' in x or x in ('לראובני', 'ולראובני', 'הראובני', 'והראובני', 'הראובני')]; g = [i for i, x in enumerate(w) if x in ('גד', 'לגדי', 'ולגדי', 'הגדי', 'והגדי')]
    return ('R<G' if r[0] < g[0] else 'G<R') if r and g else None
print('order in 32:', {v: order('Num', C, v) for v in range(1, NV + 1) if order('Num', C, v)}, '| Deut 3:12, 16, 29:8:', order('Deut', 3, 12), order('Deut', 3, 16), order('Deut', 29, 7), '| Josh 1:12, 4:12, 12:6, 13:8, 22:1, 22:9-10, 22:21, 22:25, 22:30-34:', [order('Josh', c, v) for c, v in ((1, 12), (4, 12), (12, 6), (13, 8), (22, 1), (22, 9), (22, 10), (22, 21), (22, 25), (22, 30), (22, 31), (22, 32), (22, 33), (22, 34))], '| Num 34:14:', order('Num', 34, 14), '| 1Chr 5:18, 26:', order('1Chr', 5, 18), order('1Chr', 5, 26), '| 2Kgs 10:33:', order('2Kgs', 10, 33))
print('---- THE RETELLINGS, WHOLE'); [print(f'  Deut 3:{v}', words('Deut', 3, v)) for v in range(12, 21)]
[print(f'  Josh 1:{v}', words('Josh', 1, v)) for v in range(12, 19)]
[print(f'  Josh 22:{v}', words('Josh', 22, v)) for v in range(1, 10)]
[print(f'  Deut 1:{v}', words('Deut', 1, v)) for v in range(34, 41)]
[print(f'  Num 14:{v}', words('Num', 14, v)) for v in (21, 22, 23, 24, 28, 29, 30, 31, 32, 33, 34, 35)]
print('  Deut 33:20-21:', words('Deut', 33, 20), words('Deut', 33, 21), '| Deut 34:1, 5-6:', words('Deut', 34, 1), words('Deut', 34, 5), words('Deut', 34, 6), '| Deut 32:49:', words('Deut', 32, 49), '| Josh 13:20:', words('Josh', 13, 20))
print('  Judg 5:15-17:', words('Judg', 5, 15), words('Judg', 5, 16), words('Judg', 5, 17), '| Ps 60:9:', words('Ps', 60, 9), '| 1Chr 5:18:', words('1Chr', 5, 18), '| 1Chr 5:25-26:', words('1Chr', 5, 25)[:6], words('1Chr', 5, 26), '| 2Kgs 10:33:', words('2Kgs', 10, 33))
print('---- THE PARSER on the retellings')
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
print('N in 32:', {v: N('Num', C, v) for v in range(1, NV + 1) if N('Num', C, v)}, '| O:', {v: O('Num', C, v) for v in range(1, NV + 1) if O('Num', C, v)}, '| starred:', [(v, t) for v in range(1, NV + 1) for t in CS.verse_words('Num', C, v) if t.endswith('*')], '| 33:1:', N('Num', 33, 1))
print('Josh 4:13:', N('Josh', 4, 13), '| 1Chr 5:18:', N('1Chr', 5, 18), '| Num 26:7 Reuben:', N('Num', 26, 7), '| 26:18 Gad:', N('Num', 26, 18), '| 26:34 Manasseh:', N('Num', 26, 34), '| sum R+G+M/2:', N('Num', 26, 7)[0] + N('Num', 26, 18)[0] + N('Num', 26, 34)[0] / 2, '| 1Chr 2:22-23:', N('1Chr', 2, 22), N('1Chr', 2, 23), '| Judg 10:4:', N('Judg', 10, 4), '| Deut 3:4:', N('Deut', 3, 4), '| Num 14:33-34:', N('Num', 14, 33), N('Num', 14, 34))
print('---- THE STORE (words.gloss) for the flagged words')
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=32 ORDER BY v.id, w.idx"):
    if hp.replace('/', '') in ('ויענו', 'ויגשו', 'ומקנה', 'מקנה', 'לאחזה', 'במדבר', 'וינעם', 'לספות', 'ושחתם', 'תרבות', 'ויחר', 'מקדש', 'עטרת', 'בית', 'בעל', 'חות', 'תנואון', 'תניאון', 'ויניאו', 'התנחל', 'ננחל', 'נחלץ', 'חלוץ', 'חלוצים', 'תחלצו', 'ונכבשה', 'נקיים', 'והיצא', 'מוסבת', 'בנתיה', 'ויורש', 'האחיכם', 'עצום', 'לאחזה', 'אחזת', 'ונאחזו'): print(f'  {c}:{v} {hp}={g}')
print('override file forms:', open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()[:1500])
print('---- ONKELOS 32 tokens (the Aramaic per verse)')
for v in range(1, NV + 1): print(f'  32:{v}', aramaic(C, v))
print('---- PRIOR LEDGER LINES NAMING Num 32')
TRI = f'{ROOT}/logic/oral_triage'
for f in sorted(os.listdir(TRI)):
    if not f.endswith('.md'): continue
    t = open(f'{TRI}/{f}', encoding='utf-8').read()
    for m in re.finditer(r'Num(?:bers)? 32:\d+(?:-\d+)?', t):
        print(f'  {f}: ...{t[max(0, m.start() - 150):m.end() + 100].replace(chr(10), " ")}...')
