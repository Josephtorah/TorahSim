#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 13 — THE JOURNEYS (2026-09-12): THE THIRD MEASUREMENT PASS — the prints the second pass lacked: Onkelos's renderings
# on the PLAIN Aramaic (the second pass searched the pointed text and found nothing — the instrument, not the shelf), the remaining station names'
# seats by their exact token forms, the morph numbers at 33:54 against 26:54, the cross-citing scan with "Ibid." and the gershayim form, the
# ledgers that read Sifrei 133:3, the two lists' intersection (chapter 21's stations against 33's). Nothing asserted.
import json, os, re, html, sqlite3, sys
ROOT = '<repo-old>'
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows: by.setdefault((b, c, v), []).append((plain(he), m))
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m in by[(b, c, v)]]
def U(*toks): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() for x, _ in ws if x in toks})
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
def arm(c, v): return plain(clean(onk_he[c - 1][v - 1]))
def onk_seats(sub): return [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if sub in arm(c + 1, v + 1)]
print('ONKELOS NUMBERS (plain): רקם', onk_seats('רקם'), '| דמשאלי', onk_seats('דמשאלי'), '| הור טורא', onk_seats('הור טורא'), '| מישריא דמואב', onk_seats('מישריא דמואב'), '| מישר', onk_seats('מישר'), '| מגזת', onk_seats('מגזת'), '| בריש גלי', onk_seats('בריש גלי'), '| טעות', onk_seats('טעות'), '| מימרא count per chapter 33:', sum(arm(33, v).count('מימרא') for v in range(1, 57)), '| בית סגד', onk_seats('בית סגד'), '| עדבא', onk_seats('עדבא'), '| נטלן זין', onk_seats('נטלן זין'), '| חשבית', onk_seats('חשבית'), '| למטלניהון', onk_seats('מטלנ'), '| ונטלו count 33:', sum(1 for v in range(1, 57) if arm(33, v).startswith('ונטלו')), '| ושרו count 33:', sum(arm(33, v).count('ושרו') for v in range(1, 57)))
print('Onkelos 33:16 / 11:34 / 11:35 / 33:17:', arm(33, 16), '|', arm(11, 34), '|', arm(11, 35), '|', arm(33, 17))
print('Onkelos 33:44 / 21:11 / 33:45:', arm(33, 44), '|', arm(21, 11), '|', arm(33, 45))
print('Onkelos 33:36 / 20:1 / 13:26 / 32:8 / 34:4:', arm(33, 36), '|', arm(20, 1), '|', arm(13, 26), '|', arm(32, 8), '|', arm(34, 4))
print('Onkelos 33:52 / 33:55 / 33:8 / 33:10 / 33:1 / 33:7:', arm(33, 52), '|', arm(33, 55), '|', arm(33, 8), '|', arm(33, 10), '|', arm(33, 1), '|', arm(33, 7))
print('---- THE REMAINING NAMES BY EXACT FORMS')
for name, forms in (('Rimmon-perez', ('רמן', 'ברמן', 'מרמן')), ('Shepher', ('שפר', 'בשפר')), ('Haradah', ('חרדה', 'בחרדה', 'מחרדה')), ('Tahath-place', ('בתחת', 'מתחת')), ('Terah', ('תרח', 'בתרח', 'מתרח')), ('Libnah', ('לבנה', 'בלבנה', 'מלבנה', 'ולבנה', 'ללבנה')), ('Rissah', ('רסה', 'ברסה', 'מרסה')), ('Kadesh', ('קדש', 'בקדש', 'מקדש')), ('Etham', ('אתם', 'באתם', 'מאתם')), ('Marah', ('מרה', 'במרה', 'ממרה', 'מרתה')), ('Succoth', ('סכת', 'בסכת', 'מסכת', 'סכתה', 'סכות', 'בסכות')), ('Taberah', ('תבערה', 'ובתבערה')), ('Paran', ('פארן',)), ('Sinai-wilderness', ('סיני',)), ('Sin', ('סין',)), ('Hazeroth', ('חצרת', 'בחצרת', 'מחצרת', 'חצרות', 'בחצרות', 'מחצרות')), ('Rephidim', ('רפידם', 'ברפידם', 'מרפידם', 'ברפידים', 'מרפידים')), ('Ezion-geber', ('בעציון', 'מעציון', 'ומעצין', 'עציון'))):
    seats = U(*forms); print(f'  {name}: {seats} | morph Np seats:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for x, m in ws if x in forms and m and "Np" in m}))
print('Tahath as Np:', sorted({f"{b} {c}:{v} {x} {m}" for (b, c, v), ws in by.items() for x, m in ws if x in ('תחת', 'בתחת', 'מתחת') and m and 'Np' in m}))
print('Terah as Np:', sorted({f"{b} {c}:{v} {x}" for (b, c, v), ws in by.items() for x, m in ws if x in ('תרח', 'בתרח', 'מתרח') and m and 'Np' in m}))
print('---- 33:54 AGAINST 26:54 — THE MORPHS')
print('33:54:', list(zip(words('Num', 33, 54), morphs('Num', 33, 54))))
print('26:54:', list(zip(words('Num', 26, 54), morphs('Num', 26, 54))))
print('26:55:', list(zip(words('Num', 26, 55), morphs('Num', 26, 55))))
print('Exod 19:2:', list(zip(words('Exod', 19, 2), morphs('Exod', 19, 2))))
print('33:7 וישב morph:', [(x, m) for x, m in by[('Num', 33, 7)] if x == 'וישב'], '| Exod 14:2 וישבו:', [(x, m) for x, m in by[('Exod', 14, 2)] if x == 'וישבו'])
print('---- THE CROSS-CITING SCAN, REDONE (EN "Ibid. 33:" too; HE with the gershayim)')
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']; sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
EN = [(p, r, re.findall(r'\((?:Bamidbar|Ibid)\.? 33:(\d+)', clean(row))) for p, rows in enumerate(sif, 1) for r, row in enumerate(rows, 1) if re.search(r'\((?:Bamidbar|Ibid)\.? 33:\d+', clean(row))]
print('EN rows citing (Bamidbar|Ibid.) 33:', EN)
HE = [(p, r, re.findall(r'במדבר ל[״"\']?ג[״"\']?:?[א-ת״"\']*', clean(row))) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if re.search(r'במדבר ל[״"\']?ג\b', clean(row))]
print('HE rows citing במדבר לג:', HE)
for p, r, _ in EN:
    e = clean(sif[p - 1][r - 1]); i = e.find('33:'); print(f'  {p}:{r} context: ...{e[max(0, i - 200):i + 80]}...')
print('---- THE LEDGERS THAT READ 133:3 / 82:1')
TRI = f'{ROOT}/logic/oral_triage'
for f in sorted(os.listdir(TRI)):
    if not f.endswith('.md'): continue
    t = open(f'{TRI}/{f}', encoding='utf-8').read()
    for key in ('Sifrei Bamidbar 133:3', 'Sifrei Bamidbar 82:1'):
        if re.search(r'^- ' + re.escape(key), t, re.M): print('  ', f, 'READS', key)
print('---- CHAPTER 21\'S STATIONS AGAINST 33\'S (the Np tokens of 21:10-20 and of 33:41-49)')
n21 = {x for v in range(10, 21) for x, m in by[('Num', 21, v)] if m and 'Np' in m}; n33 = {x for v in range(41, 50) for x, m in by[('Num', 33, v)] if m and 'Np' in m}
print('21:10-20 names:', sorted(n21), '| 33:41-49 names:', sorted(n33), '| shared tokens:', sorted(n21 & n33))
def bare(x): return x[1:] if x[0] in 'במ' and len(x) > 3 else x
print('shared by bare form:', sorted({bare(x) for x in n21} & {bare(x) for x in n33}))
print('---- THE STATION COUNT FROM MOSEROTH TO MOUNT HOR, AND THE FORMULA COUNTS')
camps = [(v, words('Num', 33, v)[words('Num', 33, v).index('ויחנו') + 1]) for v in range(1, 57) if 'ויחנו' in words('Num', 33, v)]
print('camps:', len(camps), '| index of במסרות:', [i for i, (v, x) in enumerate(camps) if x == 'במסרות'], '| index of בהר (33:37):', [i for i, (v, x) in enumerate(camps) if v == 37], '| index of בערבת:', [i for i, (v, x) in enumerate(camps) if v == 48])
deps = [(v, words('Num', 33, v)[words('Num', 33, v).index('ויסעו') + 1]) for v in range(1, 57) if 'ויסעו' in words('Num', 33, v)]
print('departures:', len(deps), '| distinct after-tokens:', len({x for _, x in deps}), '| the doubled:', [x for x in {x for _, x in deps} if [y for _, y in deps].count(x) > 1], '| 33:5 after-token:', deps[1])
print('camps distinct after-tokens:', len({x for _, x in camps}), '| the doubled camp tokens:', [x for x in {x for _, x in camps} if [y for _, y in camps].count(x) > 1], '| 33:48 and 33:49 tokens:', words('Num', 33, 48), words('Num', 33, 49))
print('places = Rameses + camps by verse (33:49 restating 33:48):', 1 + len([c for c in camps if c[0] != 49]))
print('הר העברים / הרי:', U('העברים'), '| Deut 32:49 tokens:', words('Deut', 32, 49)[:7])
print('ויחנו על forms:', sorted({f"{b} {c}:{v}" for (b, c, v), ws in by.items() for w in [[x for x, _ in ws]] for i in range(len(w) - 1) if w[i] == 'ויחנו' and w[i + 1] == 'על'}))
print('מקברים morph:', [(x, m) for x, m in by[('Num', 33, 4)] if x == 'מקברים'], '| Ezek 39:14:', words('Ezek', 39, 14)[:8])
print('Josh 5:10-12 morphs check: ממחרת הפסח at Josh 5:11:', words('Josh', 5, 11))
ov = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
print('override by_gloss lines with elevation / pebble / grave:', [l for l in ov.split('\n') if 'elevation' in l or 'pebble' in l or 'grave' in l or 'pretermission' in l])
print('Sifrei piska 133 head and 82 head:', clean(sif[132][0])[:80], '|', clean(sif[81][0])[:80])
