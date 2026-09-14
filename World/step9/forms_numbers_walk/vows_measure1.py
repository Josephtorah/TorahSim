#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 10 — THE VOWS, Numbers 30:1-17 (2026-09-12): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED
# from the Tanakh DB, the snapshot store and the shelf's bytes, so that vows_ink.py's asserts are typed FROM THE PRINT (sitting 8's lesson:
# the measurement pass first, then the asserts). Nothing asserted here.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = '<repo-old>'
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows: by.setdefault((b, c, v), []).append((plain(he), m, he))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
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
def cnt_in(c, pred): return sum(1 for v in range(1, 18) for x, m, _ in by[('Num', c, v)] if pred(x, m))
SPAN = [(30, v) for v in range(1, 18)]
print('---- THE FRAMES AND THE REGISTER')
print('narrative verbs:', [(v, x, m) for (c, v) in SPAN for x, m, _ in by[('Num', 30, v)] if m and re.search(r'V.w', m)])
print('"this is the thing which the LORD commanded" זה הדבר אשר צוה יהוה:', phrase(['זה', 'הדבר', 'אשר', 'צוה', 'יהוה']))
print('"the heads of the tribes" ראשי המטות:', phrase(['ראשי', 'המטות']), '| ראשי שבטי:', phrase(['ראשי', 'שבטי']), '| אל ראשי:', phrase(['אל', 'ראשי']))
print('"according to all that the LORD commanded Moses" ככל אשר צוה יהוה את משה:', phrase(['ככל', 'אשר', 'צוה', 'יהוה', 'את', 'משה']))
print('"and Moses said to the children of Israel" ויאמר משה אל בני ישראל:', phrase(['ויאמר', 'משה', 'אל', 'בני', 'ישראל']))
print('"these are the statutes" אלה החקים:', phrase(['אלה', 'החקים']), '| אלה החקים והמשפטים:', phrase(['אלה', 'החקים', 'והמשפטים']))
print('"between a man and his wife" בין איש לאשתו:', phrase(['בין', 'איש', 'לאשתו']), '| בין אב לבתו:', phrase(['בין', 'אב', 'לבתו']))
print('Numbers chapters whose law has NO divine frame: chapters of Num with וידבר יהוה / ויאמר יהוה:', sorted({c for (b, c, v), ws in by.items() if b == 'Num' and any(ws[i][0] in ('וידבר', 'ויאמר') and i + 1 < len(ws) and ws[i + 1][0] == 'יהוה' for i in range(len(ws)))}))
print('---- THE CASE STRUCTURE')
print('כי seats:', [(v, i) for (c, v) in SPAN for i, (x, m, _) in enumerate(by[('Num', 30, v)]) if x == 'כי'])
print('ואם seats:', [v for (c, v) in SPAN if 'ואם' in words('Num', 30, v)], 'count', cnt_in(30, lambda x, m: x == 'ואם'))
print('איש כי:', phrase(['איש', 'כי'], T), '| ואשה כי:', phrase(['ואשה', 'כי']), '| אשה כי:', phrase(['אשה', 'כי']))
print('---- THE ROOTS (tokens by morph)')
for v in range(1, 18):
    print(f'  30:{v}', [(x, m) for x, m, _ in by[('Num', 30, v)] if m and (m.startswith('HV') or '/V' in m)])
print('נדר-tokens (noun+verb) in 30:', cnt_in(30, lambda x, m: 'נדר' in x), '| אסר-tokens:', cnt_in(30, lambda x, m: 'אסר' in x or 'איסר' in x), '| שבע oath-tokens:', cnt_in(30, lambda x, m: x in ('שבעה', 'בשבעה', 'שבעת', 'השבע')))
print('doubled verbs (infinitive absolute Vha/Vqa + finite):', [(v, by[("Num", 30, v)][i][0], by[("Num", 30, v)][i + 1][0]) for (c, v) in SPAN for i in range(len(by[('Num', 30, v)]) - 1) if by[('Num', 30, v)][i][1] in ('HVha', 'HVqa', 'HVNa') ])
print('הפר יפר:', phrase(['הפר', 'יפר']), '| החרש יחריש:', phrase(['החרש', 'יחריש']), '| היו תהיה:', phrase(['היו', 'תהיה']), '| השבע שבעה:', phrase(['השבע', 'שבעה']), '| לאסר אסר:', phrase(['לאסר', 'אסר']))
print('---- THE CLOCK WORDS')
print('ביום שמעו:', phrase(['ביום', 'שמעו']), '| ביום שמע:', phrase(['ביום', 'שמע']), '| אחרי שמעו:', phrase(['אחרי', 'שמעו']), '| מיום אל יום:', phrase(['מיום', 'אל', 'יום']), '| מיום ליום:', phrase(['מיום', 'ליום']))
print('שמעו tokens in 30:', [(v, x, m) for (c, v) in SPAN for x, m, _ in by[('Num', 30, v)] if x.startswith('שמע')])
print('---- THE FORGIVENESS AND THE INIQUITY')
print('ויהוה יסלח לה:', phrase(['ויהוה', 'יסלח', 'לה']), '| יסלח לה:', phrase(['יסלח', 'לה']), '| יסלח:', U('יסלח'))
print('ונשא את עונה:', phrase(['ונשא', 'את', 'עונה']), '| עונה (her iniquity):', U('עונה'), '| ונשא עונו:', phrase(['ונשא', 'עונו']))
print('---- THE PERSONS')
print('בנעריה:', U('בנעריה'), '| כנעוריה:', U('כנעוריה'), '| בנעוריה:', U('בנעוריה'), '| נעריה:', U('נעריה'))
print('בית אביה:', phrase(['בית', 'אביה']), '| בבית אביה:', phrase(['בבית', 'אביה']), '| בית אישה:', phrase(['בית', 'אישה']))
print('אלמנה וגרושה:', phrase(['אלמנה', 'וגרושה']), '| וגרושה:', U('וגרושה'), '| אלמנה:', len(U('אלמנה')), '| ואלמנה:', U('ואלמנה', books=T))
print('אישה (her husband) in 30:', [(v, x) for (c, v) in SPAN for x, m, _ in by[('Num', 30, v)] if x in ('אישה', 'ואישה', 'לאיש')], 'count', cnt_in(30, lambda x, m: x in ('אישה', 'ואישה')))
print('אביה (her father) in 30:', [(v, x) for (c, v) in SPAN for x, m, _ in by[('Num', 30, v)] if x in ('אביה',)], 'count', cnt_in(30, lambda x, m: x == 'אביה'))
print('נפשה / נפשו / נפש in 30:', [(v, x) for (c, v) in SPAN for x, m, _ in by[('Num', 30, v)] if x.startswith('נפש')])
print('---- THE UTTERANCE')
print('מבטא:', U('מבטא'), '| לבטא:', U('לבטא'), '| מוצא שפתיה:', phrase(['מוצא', 'שפתיה']), '| מוצא שפתיך:', phrase(['מוצא', 'שפתיך']), '| מוצא שפתי:', U('מוצא'))
print('לא יחל דברו:', phrase(['לא', 'יחל', 'דברו']), '| יחל:', U('יחל'), '| ככל היצא מפיו:', phrase(['ככל', 'היצא', 'מפיו']), '| היצא מפי:', [s for s in U('היצא') if True][:20], '| והיצא מפיכם:', phrase(['והיצא', 'מפיכם']), '| יצא מפיך:', phrase(['יצא', 'מפיך']))
print('לענת נפש:', phrase(['לענת', 'נפש']), '| לענת:', U('לענת'), '| תענו את נפשתיכם:', phrase(['תענו', 'את', 'נפשתיכם']))
print('הניא tokens:', U('הניא'), '| יניא:', U('יניא'), '| תניאון:', U('תניאון'), '| ויניאו:', U('ויניאו'), '| הניא-stem in Torah:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if x in ('הניא', 'יניא', 'תניאון', 'ויניאו', 'הניאו')}))
print('והחריש:', U('והחריש'), '| והחרש:', U('והחרש'), '| החרש יחריש:', phrase(['החרש', 'יחריש']), '| יחריש:', U('יחריש'))
print('יקום (shall stand) in 30:', [(v, x) for (c, v) in SPAN for x, m, _ in by[('Num', 30, v)] if x.startswith('יק') or x.startswith('וקמו') or x.startswith('הקים') or x.startswith('והקים')])
print('הפר / והפר / יפר / הפרם / יפרנו:', [(v, x, m) for (c, v) in SPAN for x, m, _ in by[('Num', 30, v)] if 'פר' in x and m.startswith('HV')])
print('---- THE SEVEN-STEM HOMOGRAPH (the parser)')
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
print('N per verse:', {v: N('Num', 30, v) for v in range(1, 18)}, '| O:', {v: O('Num', 30, v) for v in range(1, 18)})
print('starred:', [(v, t) for v in range(1, 18) for t in CS.verse_words('Num', 30, v) if t.endswith('*')])
print('---- THE SHELF CITATIONS, READ TO THEIR VERSES')
print('חי יהוה וחי נפשך אם אעזבך:', phrase(['חי', 'יהוה', 'וחי', 'נפשך', 'אם', 'אעזבך']), '| חי יהוה וחי נפשך:', phrase(['חי', 'יהוה', 'וחי', 'נפשך']))
print('Deut 23:22:', words('Deut', 23, 22), '| Deut 23:24:', words('Deut', 23, 24))
print('Lev 5:4 לבטא:', 'לבטא' in words('Lev', 5, 4), words('Lev', 5, 4)[:8])
print('Num 6:2 יפלא:', words('Num', 6, 2), '| כי יפלא:', phrase(['כי', 'יפלא']))
print('Num 10:3-4:', words('Num', 10, 3), words('Num', 10, 4))
print('Exod 11:4:', words('Exod', 11, 4)[:5], '| Exod 34:31-32:', words('Exod', 34, 31), words('Exod', 34, 32)[:6])
print('Lev 22:13 (the priest\'s daughter widowed/divorced returns to her father\'s house):', words('Lev', 22, 13))
print('Lev 21:14:', words('Lev', 21, 14))
print('Gen 38:11 (Tamar to her father\'s house):', words('Gen', 38, 11)[:12])
print('Deut 22:21 בית אביה:', 'אביה' in words('Deut', 22, 21))
print('---- ONKELOS 30 tokens (the Aramaic per verse)')
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']; onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
for v in range(1, 18):
    print(f'  30:{v}', [plain(x) for x in clean(onk_he[29][v - 1]).rstrip(':').split()])
print('---- THE STORE (words.gloss) for the narrative verbs and the key nouns')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=30 AND v.verse IN (1,2,3,6,14,16) ORDER BY v.id, w.idx"):
    if hp.replace('/', '') in ('ויאמר', 'וידבר', 'ידר', 'נדר', 'השבע', 'שבעה', 'לאסר', 'אסר', 'יחל', 'הניא', 'לענת', 'ונשא', 'עונה', 'יפרנו', 'יקימנו'): print(f'  {c}:{v} {hp}={g}')
print('---- THE VOWS ELSEWHERE (the compile\'s callees)')
print('Lev 27 opens:', words('Lev', 27, 2)[:6], '| Deut 23:22-24 vows:', [words('Deut', 23, v)[:4] for v in (22, 23, 24)])
print('Num 6:2 nazirite vow:', words('Num', 6, 2)[:10])
print('Lev 5:4 the oath of utterance:', words('Lev', 5, 4))
print('Num 21:2 (Israel vowed a vow):', words('Num', 21, 2)[:6], '| Gen 28:20 (Jacob vowed):', words('Gen', 28, 20)[:5])
print('ידר נדר seats:', phrase(['ידר', 'נדר']), '| תדר נדר:', phrase(['תדר', 'נדר']), '| וידר ... נדר:', phrase(['וידר', 'יעקב', 'נדר']), phrase(['וידר', 'ישראל', 'נדר']))
print('מומחים / experts — not in the ink; the Sifrei\'s "permitting of vows" (היתר נדרים): התר:', U('התר'), '| להתיר:', U('להתיר'))
print('נדר tokens Torah by book:', Counter(b for (b, c, v), ws in by.items() if b in T for x, m, _ in ws if x.startswith('נדר') or x.startswith('ונדר') or x.startswith('לנדר') or x.startswith('הנדר') or x.startswith('מנדר')))
