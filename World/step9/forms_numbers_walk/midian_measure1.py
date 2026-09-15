import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 11 — MIDIAN, Numbers 31:1-54 (2026-09-12): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED from
# the Tanakh DB, the snapshot store and the shelf's bytes, so that midian_ink.py's asserts are typed FROM THE PRINT (the standing lesson: the
# measurement pass first, then the asserts). Nothing asserted here. Sitting 10's form (vows_measure1.py).
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
C = 31
def words(b, c, v): return [x for x, _, _ in by[(b, c, v)]]
def hits(sub, books=None, exact=True): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _, _ in ws)})
def phrase(seq, books=None):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books)))
def cnt_in(pred, c=C): return sum(1 for v in range(1, 55) for x, m, _ in by[('Num', c, v)] if pred(x, m))
def seats_in(pred, c=C): return [(v, x) for v in range(1, 55) for x, m, _ in by[('Num', c, v)] if pred(x, m)]
SPAN = [(C, v) for v in range(1, 55)]
print('---- THE FRAMES AND THE REGISTER')
REG = [(v, x, m) for (c, v) in SPAN for x, m, _ in by[('Num', C, v)] if m and re.search(r'V.w', m)]
print('narrative verbs:', REG, '| count', len(REG), '| verses', len({v for v, _, _ in REG}))
print('divine frames in 31:', [(v, words('Num', C, v)[:5]) for v in range(1, 55) if words('Num', C, v)[:2] in (['וידבר', 'יהוה'], ['ויאמר', 'יהוה'])])
print('ויאמר יהוה אל משה לאמר seats:', phrase(['ויאמר', 'יהוה', 'אל', 'משה', 'לאמר']), '| וידבר יהוה אל משה לאמר count Torah:', len(phrase(['וידבר', 'יהוה', 'אל', 'משה', 'לאמר'])))
print('וידבר משה אל העם:', phrase(['וידבר', 'משה', 'אל', 'העם']), '| ויאמר אלעזר הכהן:', phrase(['ויאמר', 'אלעזר', 'הכהן']), '| אלעזר הכהן in 31:', seats_in(lambda x, m: x in ('אלעזר', 'ואלעזר', 'לאלעזר')))
print('זאת חקת התורה:', phrase(['זאת', 'חקת', 'התורה']), '| חקת התורה:', phrase(['חקת', 'התורה']), '| אשר צוה יהוה את משה after זאת חקת:', words('Num', 19, 2)[:9])
R1 = phrase(['כאשר', 'צוה', 'יהוה', 'את', 'משה'])
print('receipt form 1 seats in 31:', [s for s in R1 if s.startswith('Num 31:')], '| total', len(R1), '| per chapter top:', Counter(s.rsplit(':', 1)[0] for s in R1).most_common(8))
print('ויקצף משה:', phrase(['ויקצף', 'משה']), '| ויקצף all:', U('ויקצף'), '| קצף-tokens Torah:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if x in ('ויקצף', 'קצף', 'הקצף', 'יקצף', 'קצפו', 'הקצפתם')}))
print('אחר תאסף אל עמיך:', phrase(['אחר', 'תאסף', 'אל', 'עמיך']), '| תאסף אל עמיך:', phrase(['תאסף', 'אל', 'עמיך']), '| ונאספת אל עמיך:', phrase(['ונאספת', 'אל', 'עמיך']), '| והאסף אל עמיך:', phrase(['והאסף', 'אל', 'עמיך']), '| ויאסף אל עמיו:', phrase(['ויאסף', 'אל', 'עמיו']), '| Num 27:13:', words('Num', 27, 13))
print('נקם נקמת:', phrase(['נקם', 'נקמת']), '| נקמת יהוה:', phrase(['נקמת', 'יהוה']), '| נקמת בני ישראל:', phrase(['נקמת', 'בני', 'ישראל']), '| נקם-root tokens in 31:', seats_in(lambda x, m: 'נקמ' in x or x == 'נקם'))
print('החלצו:', U('החלצו'), '| חלוצי:', U('חלוצי'), '| חלוצים:', U('חלוצים'), '| חלץ-root Torah seats:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if re.match(r'^(ו|ה|כ|מ)?חל(ו|)צ', x) and 'חלצה' not in x}), '| Deut 3:18:', words('Deut', 3, 18))
print('אלף למטה:', phrase(['אלף', 'למטה']), '| אלף למטה אלף למטה:', phrase(['אלף', 'למטה', 'אלף', 'למטה']), '| לכל מטות ישראל:', phrase(['לכל', 'מטות', 'ישראל']), '| שנים עשר אלף:', phrase(['שנים', 'עשר', 'אלף']), '| מאלפי ישראל:', phrase(['מאלפי', 'ישראל']), '| וימסרו:', U('וימסרו'), '| מסר-root Torah:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if x in ('וימסרו', 'למסר', 'ימסר', 'נמסר')}))
print('כלי הקדש:', phrase(['כלי', 'הקדש']), '| וכלי הקדש:', phrase(['וכלי', 'הקדש']), '| חצצרות התרועה:', phrase(['וחצצרות', 'התרועה']), phrase(['חצצרות', 'התרועה']), '| חצצר-tokens Torah:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if 'חצצר' in x}), '| בידו in 31:', seats_in(lambda x, m: x == 'בידו'), '| Num 10:9:', words('Num', 10, 9))
print('פינחס in 31:', seats_in(lambda x, m: x == 'פינחס'), '| פינחס Torah seats:', U('פינחס', books=T), '| ואת פינחס בן אלעזר הכהן:', phrase(['פינחס', 'בן', 'אלעזר', 'הכהן']))
print('---- THE WAR')
print('ויצבאו:', U('ויצבאו'), '| צבא-verb tokens 31:', seats_in(lambda x, m: m and 'V' in m and 'צבא' in x), '| הצבאים:', U('הצבאים'), '| לצבא in 31:', cnt_in(lambda x, m: x == 'לצבא'), '| צבא-tokens in 31:', cnt_in(lambda x, m: 'צבא' in x))
print('כל זכר in 31:', seats_in(lambda x, m: x == 'זכר'), '| ויהרגו כל זכר:', phrase(['ויהרגו', 'כל', 'זכר']), '| הרג-tokens 31:', seats_in(lambda x, m: x.startswith('הרג') or x.startswith('ויהרג') or x == 'הרגו'))
print('מלכי מדין:', phrase(['מלכי', 'מדין']), '| חמשת מלכי מדין:', phrase(['חמשת', 'מלכי', 'מדין']), '| מלך מדין:', phrase(['מלך', 'מדין']), '| נשיאי מדין:', phrase(['נשיאי', 'מדין']))
print('the five: אוי', U('אוי'), '| רקם:', U('רקם'), '| צור (name, HNp):', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for x, m, _ in ws if x == 'צור' and m == 'HNp'}), '| חור:', U('חור'), '| רבע:', U('רבע'))
print('Num 25:15:', words('Num', 25, 15), '| Josh 13:21:', words('Josh', 13, 21), '| Josh 13:22:', words('Josh', 13, 22))
print('חלליהם:', U('חלליהם'), '| על חלליהם:', phrase(['על', 'חלליהם']), '| אל חלליהם:', phrase(['אל', 'חלליהם']))
print('Gen 36:35:', words('Gen', 36, 35), '| בשדה מואב:', phrase(['בשדה', 'מואב']))
print('Gen 37:28 tokens:', words('Gen', 37, 28)[:6], '| Gen 37:36:', words('Gen', 37, 36), '| מדנים:', U('מדנים', 'והמדנים'), '| מדינים tokens:', U('מדינים', 'המדינים', 'מדינים'))
print('Gen 25:2:', words('Gen', 25, 2), '| Gen 25:4:', words('Gen', 25, 4))
print('בלעם בן בעור:', phrase(['בלעם', 'בן', 'בעור']), '| הרגו בחרב:', phrase(['הרגו', 'בחרב']), '| בחרב in Num:', [s for s in U('בחרב') if s.startswith('Num')], '| חרב in Num 22:', [(v, x) for v in range(1, 42) for x, m, _ in by[('Num', 22, v)] if 'חרב' in x], '| הקוסם:', U('הקוסם'))
print('booty nouns in 31: שלל', seats_in(lambda x, m: 'שלל' in x), '| מלקוח', seats_in(lambda x, m: 'מלקוח' in x), '| שבי', seats_in(lambda x, m: x in ('השבי', 'שבי', 'ושביכם', 'שביכם')), '| בז/בזז', seats_in(lambda x, m: x in ('בזזו', 'הבז', 'בז')), '| וישבו:', U('וישבו'))
print('מלקוח all seats:', U('מלקוח', 'המלקוח'), '| מכס all:', U('מכס', 'המכס', 'ומכסם'), '| מכס-tokens 31:', seats_in(lambda x, m: 'מכס' in x))
print('טירת seats:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for x, m, _ in ws if x.startswith('טיר') or x.startswith('בטיר') or x.startswith('וטיר')}), '| Gen 25:16:', words('Gen', 25, 16))
print('ערבת מואב:', phrase(['ערבת', 'מואב']), '| בערבת מואב:', phrase(['בערבת', 'מואב']), '| ירדן ירחו:', phrase(['ירדן', 'ירחו']))
print('מחוץ למחנה in 31:', seats_in(lambda x, m: x == 'מחוץ'), '| מחוץ למחנה Torah count:', len(phrase(['מחוץ', 'למחנה'], T)), '| אל מחוץ למחנה:', phrase(['אל', 'מחוץ', 'למחנה']))
print('---- THE WRATH AND THE WOMEN')
print('שרי האלפים ושרי המאות:', phrase(['שרי', 'האלפים', 'ושרי', 'המאות']), '| שרי אלפים:', phrase(['שרי', 'אלפים']), '| שרי האלפים והמאות:', phrase(['שרי', 'האלפים', 'והמאות']), '| Exod 18:21:', words('Exod', 18, 21)[-6:], '| Exod 18:25:', words('Exod', 18, 25)[-6:], '| Deut 1:15:', words('Deut', 1, 15)[-8:])
print('פקודי החיל:', phrase(['פקודי', 'החיל']), '| הפקדים אשר לאלפי הצבא:', phrase(['הפקדים', 'אשר', 'לאלפי', 'הצבא']), '| פקד-tokens 31:', seats_in(lambda x, m: 'פקד' in x))
print('החייתם:', U('החייתם'), '| החיו:', U('החיו'), '| ותחיין:', U('ותחיין'), '| Exod 1:17:', words('Exod', 1, 17)[-4:], '| Deut 20:16:', words('Deut', 20, 16), '| כל נקבה:', phrase(['כל', 'נקבה']), '| נקבה Torah:', U('נקבה', 'ונקבה', books=T))
print('הן הנה:', phrase(['הן', 'הנה']), '| בדבר בלעם:', phrase(['בדבר', 'בלעם']), '| דבר פעור:', phrase(['דבר', 'פעור']), '| למסר מעל:', phrase(['למסר', 'מעל']), '| מעל ביהוה:', phrase(['מעל', 'ביהוה']))
print('המגפה seats Num:', [s for s in U('המגפה', 'מגפה', 'במגפה') if s.startswith('Num')], '| בעדת יהוה:', phrase(['בעדת', 'יהוה']), '| עדת יהוה:', phrase(['עדת', 'יהוה']))
print('משכב זכר:', phrase(['משכב', 'זכר']), '| למשכב זכר:', phrase(['למשכב', 'זכר']), '| משכבי אשה:', phrase(['משכבי', 'אשה']), '| ידעת איש:', phrase(['ידעת', 'איש']), '| ידעו משכב:', phrase(['ידעו', 'משכב']), '| Judg 21:11:', words('Judg', 21, 11), '| Judg 21:12:', words('Judg', 21, 12)[:12])
print('31:17 tokens:', words('Num', 31, 17), '| הרגו first/last:', words('Num', 31, 17)[1], words('Num', 31, 17)[-1], '| החיו לכם:', phrase(['החיו', 'לכם']), '| בטף:', U('בטף'), '| הטף בנשים:', phrase(['הטף', 'בנשים']))
print('Deut 20:13:', words('Deut', 20, 13), '| Deut 20:14:', words('Deut', 20, 14), '| Deut 21:10:', words('Deut', 21, 10), '| Deut 21:11:', words('Deut', 21, 11))
print('---- THE PURIFICATION')
print('שבעת ימים in 31:', seats_in(lambda x, m: x == 'שבעת'), '| ביום השלישי וביום השביעי:', phrase(['ביום', 'השלישי', 'וביום', 'השביעי']), '| Num 19:12:', words('Num', 19, 12), '| Num 19:19:', words('Num', 19, 19))
print('תתחטאו:', U('תתחטאו'), '| יתחטא:', U('יתחטא'), '| חטא-hitpael tokens Num 19+31:', sorted({f"{b} {c}:{v} {x}" for (b, c, v), ws in by.items() if b == 'Num' and c in (8, 19, 31) for x, m, _ in ws if m and m.startswith('HVt')}))
print('הרג נפש:', phrase(['הרג', 'נפש']), '| נגע בחלל:', phrase(['נגע', 'בחלל']), '| בחלל חרב:', phrase(['בחלל', 'חרב']), '| בחלל seats:', U('בחלל'), '| Num 19:16:', words('Num', 19, 16), '| אתם ושביכם:', phrase(['אתם', 'ושביכם']))
print('Lev 11:32:', words('Lev', 11, 32), '| Num 31:20:', words('Num', 31, 20), '| מעשה עזים:', phrase(['מעשה', 'עזים']), '| כלי עור:', phrase(['כלי', 'עור']), '| שק Torah seats:', U('שק', 'ושק', 'בשק', books=T))
print('metals: בדיל', U('בדיל', 'הבדיל'), '| עפרת:', U('עפרת', 'העפרת', 'כעופרת', 'ועופרת', 'עופרת'), '| ברזל Torah:', len(U('ברזל', 'הברזל', 'וברזל', 'ברזלו', 'בברזל', books=T)), '| הזהב ואת הכסף:', phrase(['הזהב', 'ואת', 'הכסף']), '| the six in one verse: verses with זהב+כסף+נחשת+ברזל:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if all(any(k in x for x, _, _ in ws) for k in ('זהב', 'כסף', 'נחשת', 'ברזל'))}))
print('אך in 31:', seats_in(lambda x, m: x == 'אך'), '| אך Torah count:', len(U('אך', books=T)))
print('מי נדה:', phrase(['מי', 'נדה']), '| במי נדה:', phrase(['במי', 'נדה']), '| למי נדה:', phrase(['למי', 'נדה']), '| Num 19:9:', words('Num', 19, 9)[-8:])
print('תעבירו באש:', phrase(['תעבירו', 'באש']), '| יבא באש:', phrase(['יבא', 'באש']), '| תעבירו במים:', phrase(['תעבירו', 'במים']), '| העביר באש (Molech) Torah:', phrase(['להעביר', 'למלך'], T), phrase(['באש', 'למלך'], T), '| וטהר seats Num:', [s for s in U('וטהר') if s.startswith('Num')])
print('וכבסתם בגדיכם:', phrase(['וכבסתם', 'בגדיכם']), '| וכבסו בגדיהם:', phrase(['וכבסו', 'בגדיהם']), '| וכבס בגדיו:', len(phrase(['וכבס', 'בגדיו'])), '| ביום השביעי וטהרתם:', phrase(['ביום', 'השביעי', 'וטהרתם']), '| וטהר בערב:', phrase(['וטהר', 'בערב']), '| ואחר תבאו אל המחנה:', phrase(['ואחר', 'תבאו', 'אל', 'המחנה']), '| ואחר יבוא אל המחנה:', phrase(['ואחר', 'יבוא', 'אל', 'המחנה']), phrase(['ואחר', 'יבא', 'אל', 'המחנה']))
print('Num 19:11:', words('Num', 19, 11), '| Num 19:13:', words('Num', 19, 13)[:8], '| Num 19:20:', words('Num', 19, 20)[:9])
print('---- THE DIVISION AND THE TRIBUTE')
print('שא את ראש:', phrase(['שא', 'את', 'ראש']), '| שאו את ראש:', phrase(['שאו', 'את', 'ראש']), '| נשאו את ראש:', phrase(['נשאו', 'את', 'ראש']), '| נשא את ראש:', phrase(['נשא', 'את', 'ראש']), '| Exod 30:12:', words('Exod', 30, 12))
print('וראשי אבות העדה:', phrase(['וראשי', 'אבות', 'העדה']), '| ראשי אבות:', len(phrase(['ראשי', 'אבות'])), '| Num 1:2-4 staff:', words('Num', 1, 3)[-6:], words('Num', 1, 4), '| Num 26:1-2:', words('Num', 26, 1), words('Num', 26, 2)[:6])
print('half-root tokens 31:', seats_in(lambda x, m: 'חצ' in x and 'חצצר' not in x), '| וחצית:', U('וחצית'), '| המחצה:', U('המחצה'), '| מחצת:', U('מחצת', 'ממחצת', 'וממחצת'), '| מחצית:', U('מחצית', 'וממחצית', 'ממחציתם'))
print('תפשי המלחמה:', phrase(['תפשי', 'המלחמה']), '| היצאים לצבא:', phrase(['היצאים', 'לצבא']), '| אנשי המלחמה:', phrase(['אנשי', 'המלחמה'], T), '| אנשי הצבא:', phrase(['אנשי', 'הצבא']), '| עם הצבא:', phrase(['עם', 'הצבא']))
print('אחד נפש מחמש המאות:', phrase(['אחד', 'נפש', 'מחמש', 'המאות']), '| מחמש המאות:', phrase(['מחמש', 'המאות']), '| אחד אחז מן החמשים:', phrase(['אחד', 'אחז', 'מן', 'החמשים']), '| מן החמשים:', phrase(['מן', 'החמשים']), '| האחז:', U('האחז'), '| אחז (participle) seats:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for x, m, _ in ws if x == 'אחז' and m and 'Vqs' in m}))
print('תרומת יהוה:', phrase(['תרומת', 'יהוה']), '| מכס תרומת יהוה:', phrase(['מכס', 'תרומת', 'יהוה']), '| והרמת מכס:', phrase(['והרמת', 'מכס']), '| הרימו ליהוה:', phrase(['הרימו', 'ליהוה']))
print('שמרי משמרת משכן יהוה:', phrase(['שמרי', 'משמרת', 'משכן', 'יהוה']), '| משמרת משכן:', phrase(['משמרת', 'משכן']), '| Num 1:53:', words('Num', 1, 53)[-6:], '| Num 18:3:', words('Num', 18, 3)[:6])
print('31:28 classes:', words('Num', 31, 28)[11:], '| 31:30 classes:', words('Num', 31, 30)[8:18], '| מכל הבהמה:', phrase(['מכל', 'הבהמה']), '| ומן הצאן:', phrase(['ומן', 'הצאן']))
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
tot = {k: N('Num', 31, v)[0] for k, v in (('sheep', 32), ('cattle', 33), ('donkeys', 34), ('persons', 35))}
half = {k: N('Num', 31, v)[0] for k, v in (('sheep', 36), ('cattle', 38), ('donkeys', 39), ('persons', 40))}
trib = {k: N('Num', 31, v)[-1] for k, v in (('sheep', 37), ('cattle', 38), ('donkeys', 39), ('persons', 40))}
cong = {k: N('Num', 31, v)[0] for k, v in (('sheep', 43), ('cattle', 44), ('donkeys', 45), ('persons', 46))}
print('THE ARITHMETIC: totals', tot, '| halves', half, '| tributes', trib, '| congregation halves', cong)
print('  half == total/2:', {k: (tot[k] / 2 == half[k], tot[k] / 2) for k in tot}, '| cong == half:', {k: cong[k] == half[k] for k in tot})
print('  tribute == half/500:', {k: (half[k] / 500 == trib[k], half[k] / 500) for k in tot}, '| sum tributes:', sum(trib.values()), '| the Levites\' UNSTATED shares half/50:', {k: half[k] / 50 for k in tot}, 'sum', sum(half[k] / 50 for k in tot))
print('  total spoil (heads):', sum(tot.values()), '| every total divisible by 1000:', {k: tot[k] % 1000 == 0 for k in tot}, '| 31:52 shekels:', N('Num', 31, 52), '| 31:5:', N('Num', 31, 5), '| 31:4:', N('Num', 31, 4), '| 1000*12:', 1000 * 12)
print('ולא נפקד ממנו איש:', phrase(['ולא', 'נפקד', 'ממנו', 'איש']), '| נפקד seats:', U('נפקד'), '| לא נפקד:', phrase(['לא', 'נפקד']))
print('---- THE OFFICERS\' GOLD')
print('ויקרבו אל משה:', phrase(['ויקרבו', 'אל', 'משה']), '| קרבן יהוה:', phrase(['קרבן', 'יהוה']), '| ונקרב את קרבן יהוה:', phrase(['ונקרב', 'את', 'קרבן', 'יהוה']))
print('אצעדה:', U('אצעדה', 'ואצעדה'), '| צמיד:', U('צמיד', 'וצמיד', 'צמידים', 'וצמידים'), '| טבעת seats count:', len(U('טבעת', 'וטבעת')), '| עגיל:', U('עגיל', 'ועגיל', 'עגילים', 'ועגילים'), '| כומז:', U('כומז', 'וכומז'), '| Exod 35:22:', words('Exod', 35, 22), '| 2Sam 1:10:', words('2Sam', 1, 10)[-8:], '| Gen 24:22:', words('Gen', 24, 22)[-8:])
print('לכפר על נפשתינו:', phrase(['לכפר', 'על', 'נפשתינו']), '| לכפר על נפשתיכם:', phrase(['לכפר', 'על', 'נפשתיכם']), '| על נפשתיכם:', phrase(['על', 'נפשתיכם']), '| Exod 30:12:', words('Exod', 30, 12), '| Exod 30:15:', words('Exod', 30, 15), '| Exod 30:16:', words('Exod', 30, 16))
print('זכרון לבני ישראל לפני יהוה:', phrase(['זכרון', 'לבני', 'ישראל', 'לפני', 'יהוה']), '| לזכרון לפני יהוה:', phrase(['לזכרון', 'לפני', 'יהוה']), '| זכרון לפני יהוה:', phrase(['זכרון', 'לפני', 'יהוה']), '| לבני ישראל לזכרון:', phrase(['לבני', 'ישראל', 'לזכרון']), '| זכרון seats Torah:', U('זכרון', 'לזכרון', 'זכרון', books=T))
print('כל כלי מעשה:', phrase(['כל', 'כלי', 'מעשה']), '| כלי זהב:', phrase(['כלי', 'זהב']), '| איש לו:', phrase(['איש', 'לו']), '| בזזו איש לו:', phrase(['בזזו', 'איש', 'לו']), '| אהל מועד in 31:', seats_in(lambda x, m: x == 'מועד'), '| שקל in 31:', seats_in(lambda x, m: 'שקל' in x))
print('מאת שרי:', phrase(['מאת', 'שרי']), '| ומאת שרי:', phrase(['ומאת', 'שרי']), '| מאת (from-with) in 31:', seats_in(lambda x, m: x in ('מאת', 'ומאת', 'מאתם', 'מאתכם')))
print('---- THE PARSER: numbers | ordinals per verse; the FRACTION class corpus-wide')
print('N:', {v: N('Num', 31, v) for v in range(1, 55) if N('Num', 31, v)}, '| O:', {v: O('Num', 31, v) for v in range(1, 55) if O('Num', 31, v)}, '| starred:', [(v, t) for v in range(1, 55) for t in CS.verse_words('Num', 31, v) if t.endswith('*')])
CARD = ['עשרה', 'עשר', 'עשרים', 'שלשים', 'ארבעים', 'חמשים', 'ששים', 'שבעים', 'שמנים', 'תשעים', 'מאה', 'מאות', 'מאתים', 'אלף', 'אלפים', 'חמש', 'חמשת', 'חמשה', 'שלש', 'שלשת', 'שלשה', 'ארבע', 'ארבעת', 'ארבעה', 'שש', 'ששת', 'ששה', 'שבע', 'שבעת', 'שבעה', 'שמנה', 'שמנת', 'תשע', 'תשעת', 'תשעה', 'עשרת', 'שנים', 'שתים']
def denom(t): return (t.startswith('ה') and t[1:] in CARD) or (t.startswith('מה') and t[2:] in CARD) or (t.startswith('מ') and t[1:] in CARD and t[1:] not in ('שנים',))
FR = []
for (b, c, v), ws in by.items():
    w = [x for x, _, _ in ws]
    for i, x in enumerate(w):
        if x in ('אחד', 'אחת', 'האחד', 'האחת') and any(denom(t) for t in w[i + 1:i + 5]):
            FR.append((f'{b} {c}:{v}', w[i:i + 5], N(b, c, v))); break
print('FRACTION candidates (one ... of the N):', len(FR))
for s, ctx, n in FR: print('   ', s, ctx, n)
print('---- ONKELOS 31 tokens (the Aramaic per verse)')
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']; onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
for v in range(1, 55):
    print(f'  31:{v}', [plain(x) for x in clean(onk_he[30][v - 1]).rstrip(':').split()])
print('---- THE STORE (words.gloss) for the flagged words')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=31 ORDER BY v.id, w.idx"):
    if hp.replace('/', '') in ('בחרב', 'המלקוח', 'מלקוח', 'ויקצף', 'תתחטאו', 'יתחטא', 'וכבסתם', 'טירתם', 'מועד', 'ושביכם', 'השבי', 'נקם', 'נקמת', 'וישבו', 'החלצו', 'וימסרו', 'ויצבאו', 'אצעדה', 'וכומז', 'עגיל', 'מכס', 'המכס', 'והרמת', 'וחצית', 'האחז', 'אחז', 'נפקד', 'ונקרב', 'זכרון'): print(f'  {c}:{v} {hp}={g}')
print('---- THE RETELLINGS')
print('Judg 8:5:', words('Judg', 8, 5), '| Judg 8:12:', words('Judg', 8, 12), '| Judg 8:26:', words('Judg', 8, 26)[:12], '| מלכי מדין all:', phrase(['מלכי', 'מדין']))
print('1Sam 30:24:', words('1Sam', 30, 24), '| 1Sam 30:25:', words('1Sam', 30, 25), '| יחדו יחלקו:', phrase(['יחדו', 'יחלקו']))
print('Ps 106:28-31:', words('Ps', 106, 28), words('Ps', 106, 29), words('Ps', 106, 30), words('Ps', 106, 31))
print('Num 25:16-18:', words('Num', 25, 17), words('Num', 25, 18), '| צרור את המדינים:', phrase(['צרור', 'את', 'המדינים']), '| המדינים seats:', U('המדינים'))
print('Num 11:21 600,000:', words('Num', 11, 21)[:5], N('Num', 11, 21), '| Exod 12:37:', N('Exod', 12, 37))
print('Num 27:12-14:', words('Num', 27, 12), words('Num', 27, 13), '| Deut 32:50:', words('Deut', 32, 50)[:8], '| Deut 34:5:', words('Deut', 34, 5))
print('Num 10:8-9:', words('Num', 10, 8), words('Num', 10, 9), '| והרעתם בחצצרת:', phrase(['והרעתם', 'בחצצרת']))
print('the plague count 25:9:', N('Num', 25, 9), '| Num 25:9:', words('Num', 25, 9))
