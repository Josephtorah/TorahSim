import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE SECOND MEASUREMENT PASS (sitting 9 — THE OFFERINGS CALENDAR, Numbers 28:1-29:39): every candidate fact PRINTED before it is typed as an
# assert in offerings_ink.py. The helpers as census_ink.py's (the Tanakh DB, the snapshot store, the parser).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
from fractions import Fraction
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byraw = {}, {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byraw.setdefault((b, c, v), []).append(he)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def count_tok(tok, books=None): return sum(1 for (b, c, v), ws in by.items() if (books is None or b in books) for x, _ in ws if x == tok)
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
def aramaic(c, v): return [plain(x) for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
def P(*a): print(*a)
SPAN = [(28, v) for v in range(1, 32)] + [(29, v) for v in range(1, 40)]

P('==== THE PARSER GAPS')
P('28:19 accents on each token:', [(plain(w), accents(w)) for w in byraw[('Num', 28, 19)]])
P('28:11 accents:', [(plain(w), accents(w)) for w in byraw[('Num', 28, 11)] if plain(w) in ('אחד', 'שנים', 'שבעה')])
P('28:27 accents:', [(plain(w), accents(w)) for w in byraw[('Num', 28, 27)] if plain(w) in ('אחד', 'שנים', 'שבעה')])
P('"one and seven" adjacent (אחד ושבעה) seats:', phrase(['אחד', 'ושבעה'], None), 'N at each:', [(s, N(*(s.split()[0], *map(int, s.split()[1].split(':'))))) for s in phrase(['אחד', 'ושבעה'], None) if s.split()[0] in T])
P('numeral + ו+numeral of different nouns — "ram one and-seven lambs": the verse_words tokens 28:19:', CS.verse_words('Num', 28, 19))
P('בעשור seats:', U('בעשור'), 'בעשר seats:', U('בעשר'), 'N Exod 12:3:', N('Exod', 12, 3), 'N Lev 16:29:', N('Lev', 16, 29), 'N Lev 23:27:', N('Lev', 23, 27), 'N Lev 25:9:', N('Lev', 25, 9), 'N Num 29:7:', N('Num', 29, 7))
P('pointed בעשור 29:7:', [byp[('Num', 29, 7)][i] for i, x in enumerate(words('Num', 29, 7)) if x == 'בעשור'], 'Exod 12:3 בעשר:', [byp[('Exod', 12, 3)][i] for i, x in enumerate(words('Exod', 12, 3)) if x == 'בעשר'])
P('עשתי עשר seats (eleven):', phrase(['עשתי', 'עשר'], None))

P('==== THE FRAMES AND THE REGISTER')
FR = [(c, v) for (c, v) in SPAN if words('Num', c, v)[0] in ('וידבר', 'ויאמר')]
P('frames:', FR, '30:1:', words('Num', 30, 1))
REG = {(c, v): [(x, m) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)] for (c, v) in SPAN}
P('register (narrative-past verbs) in 28-29:', {k: v for k, v in REG.items() if v})
P('"speak to Moses saying" 28:1 vs 30:1 "Moses spoke to the heads of the tribes":', words('Num', 28, 1), words('Num', 30, 1)[:6])

P('==== THE TAMID (28:1-8)')
P('28:2 tokens:', words('Num', 28, 2), '| possessives קרבני לחמי לאשי ניחחי:', [x for x in words('Num', 28, 2) if x.endswith('י') and x not in ('בני', 'לי')])
P('קרבני seats:', U('קרבני'), 'לחמי:', U('לחמי'), 'לאשי:', U('לאשי'), 'ניחחי:', U('ניחחי'))
P('במועדו seats:', U('במועדו'), 'במועדה:', U('במועדה'), 'במועדם:', U('במועדם'))
P('28:3 שנים ליום seats:', phrase(['שנים', 'ליום'], None), 'עלה תמיד:', phrase(['עלה', 'תמיד'], None), 'עלת תמיד:', phrase(['עלת', 'תמיד'], None), 'עלת התמיד:', phrase(['עלת', 'התמיד'], None))
P('28:4 vs Exod 29:39:', words('Num', 28, 4), '|', words('Exod', 29, 39))
P('28:5 vs Exod 29:40:', words('Num', 28, 5), '|', words('Exod', 29, 40))
P('שמן כתית seats:', phrase(['שמן', 'כתית'], None), 'בשמן כתית:', phrase(['בשמן', 'כתית'], None), 'כתית:', U('כתית'))
P('28:6 העשיה בהר סיני:', phrase(['העשיה', 'בהר', 'סיני'], None), 'העשיה:', U('העשיה'))
P('28:7 נסך שכר:', phrase(['נסך', 'שכר'], None), 'שכר seats Torah:', U('שכר', 'ושכר', 'לשכר', books=T), 'הסך:', U('הסך'), 'בקדש:', len(U('בקדש')))
P('28:8 כמנחת הבקר:', phrase(['כמנחת', 'הבקר'], None), 'Exod 29:41:', words('Exod', 29, 41))
P('Onkelos 28:2 arranged bread:', aramaic(28, 2), '| 28:5 three seahs:', aramaic(28, 5), '| 28:7 old wine:', aramaic(28, 7))

P('==== THE SABBATH AND THE NEW MOON (28:9-15)')
P('28:9 vs Lev 23:3:', words('Num', 28, 9), '|', words('Lev', 23, 3))
P('עלת שבת בשבתו:', phrase(['עלת', 'שבת', 'בשבתו'], None), 'עלת חדש בחדשו:', phrase(['עלת', 'חדש', 'בחדשו'], None), 'בשבתו:', U('בשבתו'), 'בחדשו:', U('בחדשו'))
P('ובראשי חדשיכם:', phrase(['ובראשי', 'חדשיכם'], None), 'ראשי חדשיכם 10:10:', words('Num', 10, 10)[:6], 'לחדשי השנה:', phrase(['לחדשי', 'השנה'], None))
P('28:12-14 the table: tenths', N('Num', 28, 12), N('Num', 28, 13), 'hins', N('Num', 28, 14), '| 15:4-10 the libation table:', [(v, N('Num', 15, v)) for v in range(4, 11)])
P('חצי ההין:', phrase(['חצי', 'ההין'], None), 'שלישת ההין:', phrase(['שלישת', 'ההין'], None), 'רביעת ההין:', phrase(['רביעת', 'ההין'], None))
P('28:15 לחטאת ליהוה:', phrase(['לחטאת', 'ליהוה'], None), '| the goats of 28-29 with their clause:', [(c, v, words('Num', c, v)[:6]) for (c, v) in SPAN if any(x in ('ושעיר', 'שעיר') for x in words('Num', c, v))])
P('שעיר עזים אחד seats:', phrase(['שעיר', 'עזים', 'אחד'], None), 'ושעיר חטאת אחד:', phrase(['ושעיר', 'חטאת', 'אחד'], None), 'שעיר חטאת אחד:', phrase(['שעיר', 'חטאת', 'אחד'], None))
P('Onkelos 28:14 at its renewal:', aramaic(28, 14), '| 28:15:', aramaic(28, 15))

P('==== PESACH AND SHAVUOT (28:16-31)')
P('28:16-17 vs Lev 23:5-6:', words('Num', 28, 16), '|', words('Lev', 23, 5), '||', words('Num', 28, 17), '|', words('Lev', 23, 6))
P('פסח ליהוה:', phrase(['פסח', 'ליהוה'], None), 'מצות יאכל:', phrase(['מצות', 'יאכל'], None), 'שבעת ימים מצות:', phrase(['שבעת', 'ימים', 'מצות'], None))
P('מקרא קדש seats:', phrase(['מקרא', 'קדש'], None), 'count in 28-29:', sum(1 for (c, v) in SPAN if 'מקרא' in words('Num', c, v)))
P('כל מלאכת עבדה לא תעשו:', phrase(['כל', 'מלאכת', 'עבדה', 'לא', 'תעשו'], None), '| כל מלאכה לא תעשו:', phrase(['כל', 'מלאכה', 'לא', 'תעשו'], None))
P('מלבד seats in 28-29:', [(c, v) for (c, v) in SPAN if 'מלבד' in words('Num', c, v)], 'Torah:', len(U('מלבד', books=T)))
P('כאלה תעשו ליום:', phrase(['כאלה', 'תעשו', 'ליום'], None), 'לחם אשה:', phrase(['לחם', 'אשה'], None))
P('28:26 vs Lev 23:16-17,21:', words('Num', 28, 26), '|', words('Lev', 23, 16), '|', words('Lev', 23, 21))
P('יום הבכורים:', phrase(['יום', 'הבכורים'], None), 'מנחה חדשה:', phrase(['מנחה', 'חדשה'], None), 'בשבעתיכם:', U('בשבעתיכם'), 'שבעתיכם:', U('שבעתיכם', 'שבעתכם'))
P('the three musaf tables (28:11, 28:19, 28:27):', N('Num', 28, 11), N('Num', 28, 19), N('Num', 28, 27), '| "as these" 28:24:', N('Num', 28, 24))
P('28:31 תמימם יהיו לכם ונסכיהם:', words('Num', 28, 31), 'תמימם יהיו לכם seats:', phrase(['תמימם', 'יהיו', 'לכם'], None))
P('Onkelos 28:26 in your assemblies:', aramaic(28, 26), '| 28:16:', aramaic(28, 16))

P('==== TISHRI (29:1-38)')
P('29:1 vs Lev 23:24:', words('Num', 29, 1), '|', words('Lev', 23, 24))
P('יום תרועה:', phrase(['יום', 'תרועה'], None), 'זכרון תרועה:', phrase(['זכרון', 'תרועה'], None), 'תרועה seats Torah:', U('תרועה', books=T))
P('29:6 מלבד עלת החדש:', words('Num', 29, 6), 'כמשפטם seats:', U('כמשפטם'), 'כמשפט seats Torah:', U('כמשפט', books=T))
P('29:7 vs Lev 23:27 / 16:29:', words('Num', 29, 7), '|', words('Lev', 23, 27), '|', words('Lev', 16, 29))
P('ועניתם את נפשתיכם:', phrase(['ועניתם', 'את', 'נפשתיכם'], None), 'תענו את נפשתיכם:', phrase(['תענו', 'את', 'נפשתיכם'], None))
P('29:11 חטאת הכפרים:', phrase(['חטאת', 'הכפרים'], None), 'Exod 30:10:', words('Exod', 30, 10)[:8])
P('29:12 vs Lev 23:34, 39, 41:', words('Num', 29, 12), '|', words('Lev', 23, 34), '|', words('Lev', 23, 41))
P('וחגתם חג ליהוה:', phrase(['וחגתם', 'חג', 'ליהוה'], None), 'תחגו אתו:', phrase(['תחגו', 'אתו'], None))
BULLS = {v: N('Num', 29, v) for v in (13, 17, 20, 23, 26, 29, 32)}
P('the seven days bulls/rams/lambs:', BULLS, 'sum bulls:', sum(BULLS[v][0] for v in BULLS), 'rams sum:', sum(BULLS[v][1] for v in BULLS), 'lambs sum:', sum(BULLS[v][2] for v in BULLS))
P('the goats per day:', [(v, N('Num', 29, v)) for v in (16, 19, 22, 25, 28, 31, 34, 38)])
P('the eighth day 29:36:', N('Num', 29, 36), '29:35 עצרת:', U('עצרת', books=T), 'עצרת all:', U('עצרת'))
P('THE WATER-LIBATION LETTERS — the libation and ordinance forms per day:', [(v, [x for x in words('Num', 29, v) if x.startswith('ונסכ') or x.startswith('כמשפט') or x.startswith('מנחת') or x.startswith('ומנחת')]) for v in range(16, 39)])
P('ונסכיהם seats:', U('ונסכיהם'), 'ונסכיה seats:', U('ונסכיה'), 'ונסכה seats:', U('ונסכה'), 'כמשפטם seats:', U('כמשפטם'))
P('במספרם כמשפט:', phrase(['במספרם', 'כמשפט'], None), 'במספרם כמשפטם:', phrase(['במספרם', 'כמשפטם'], None), 'במספרם:', U('במספרם'))
P('29:39 vs Lev 23:37-38:', words('Num', 29, 39), '|', words('Lev', 23, 37), '|', words('Lev', 23, 38))
P('לבד מנדריכם:', phrase(['לבד', 'מנדריכם'], None), 'מלבד שבתת יהוה:', phrase(['מלבד', 'שבתת', 'יהוה'], None), 'ונדבתיכם:', U('ונדבתיכם'))
P('Onkelos 29:1 wail:', aramaic(29, 1), '| 29:7 fast:', aramaic(29, 7), '| 29:35:', aramaic(29, 35), '| 29:39:', aramaic(29, 39), '| 29:33 as fit for them:', aramaic(29, 33), '| 29:18:', aramaic(29, 18))
P('Onkelos "to be accepted with favor" for pleasing aroma — count of לאתקבלא ברעוא in 28-29:', sum(1 for (c, v) in SPAN if 'לאתקבלא' in aramaic(c, v) or 'דמתקבל' in aramaic(c, v)), 'the ink ריח ניחח count:', sum(1 for (c, v) in SPAN if 'ניחח' in words('Num', c, v) or 'ניחחי' in words('Num', c, v)))

P('==== LEVITICUS 23 AT ITS SECOND SEAT — the shared tokens per festival verse pair')
def overlap(a, b):
    A, B = words('Num', *a), words('Lev', *b); return [x for x in A if x in B], [x for x in B if x not in A]
for a, b in (((28, 16), (23, 5)), ((28, 17), (23, 6)), ((28, 18), (23, 7)), ((28, 25), (23, 8)), ((28, 26), (23, 21)), ((29, 1), (23, 24)), ((29, 7), (23, 27)), ((29, 12), (23, 34)), ((29, 35), (23, 36)), ((29, 39), (23, 37))):
    sh, only_lev = overlap(a, b); P(f'  Num {a[0]}:{a[1]} vs Lev {b[0]}:{b[1]}: shared {len(sh)} of {len(words("Num", *a))}; Lev-only {only_lev}')
P('Lev 23 has "the Sabbath" offerings? 23:3:', words('Lev', 23, 3), '| new moon in Lev 23:', [v for v in range(1, 45) if any('חדש' in x for x in words('Lev', 23, v))])
P('the seventy bulls on the shelf: Sukkah 55b — outside the reading; the ink sum computed above')
P('the sum of the days\' offerings — the seven days: bulls 70, rams 14, lambs 98, goats 7; tenths: bulls 3/10 each, rams 2/10, lambs 1/10 ->', Fraction(3, 10) * 70, Fraction(2, 10) * 14, Fraction(1, 10) * 98, 'hins: bulls 1/2, rams 1/3, lambs 1/4 ->', Fraction(1, 2) * 70 + Fraction(1, 3) * 14 + Fraction(1, 4) * 98)
P('the year\'s tamid lambs (2 x days) — the calendar\'s: 354 or 365 days x 2 — not the ink\'s number; skipped')
