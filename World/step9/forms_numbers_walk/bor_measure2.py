import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 14 — THE BORDERS (2026-09-12): THE THIRD MEASUREMENT PASS — the prints the second pass lacked: the Hebrew "(שם ל"ד)"
# hits read to their books, the pointed forms of the chapter's consonantal homographs (Shepham / the lip; the brook / the inheritance; "mark out" /
# "desire"; "reach" / "blot"), Kadesh-barnea's and Azmon's full seat lists, the Reubenite-and-Gadite pair with every prefix, the "to you" formula
# Joshua keeps, the four promised extents against the chapter's tokens, Onkelos on the sotah's blotting verb, the store's 'cord' glosses, the
# roster's counts. Nothing asserted. Sitting 13's form (jou_measure2.py).
import json, os, re, html, sqlite3, sys
from collections import Counter
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows: by.setdefault((b, c, v), []).append((plain(he), m, he))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _, _ in by[(b, c, v)]]
def raw(b, c, v): return [(x, m, pointed(r)) for x, m, r in by[(b, c, v)]]
def U(*toks, books=None): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if books is None or b in books for x, _, _ in ws if x in toks})
def phrase(seq, books=None):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
def arm(c, v): return [plain(x) for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']; sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
print('---- THE HEBREW "(שם ל"ד)" HITS READ TO THEIR BOOKS')
for p, r in ((1, 7), (118, 1)):
    h = Hb(p, r); i = h.find('שם ל"ד') if 'שם ל"ד' in h else h.find('שם לד')
    print(f'  {p}:{r} head: {E(p, r)[:50]!r} | HE context: {h[max(0, i - 220):i + 30]!r}')
    print(f'     the Hebrew citations in the row in order: {re.findall(r"[(][^)]*[)]", h)}')
print('---- THE POINTED HOMOGRAPHS')
print('Shepham 34:10 / 34:11 vs the lip Lev 13:45 / Ezek 24:17 / Mic 3:7:', [t for t in raw('Num', 34, 10) if t[0] == 'שפמה'], [t for t in raw('Num', 34, 11) if t[0] == 'משפם'], [t for t in raw('Lev', 13, 45) if 'שפם' in t[0]], [t for t in raw('Ezek', 24, 17) if 'שפם' in t[0]], [t for t in raw('Mic', 3, 7) if 'שפם' in t[0]])
print('the brook 34:5 vs the inheritance 34:2 / 26:53 / 36:2:', [t for t in raw('Num', 34, 5) if t[0] == 'נחלה'], [t for t in raw('Num', 34, 2) if t[0] == 'בנחלה'], [t for t in raw('Num', 26, 53) if 'נחלה' in t[0]], '| נחלה bare token seats (the two senses):', sorted({f'{b} {c}:{v} {m}' for (b, c, v), ws in by.items() for x, m, _ in ws if x == 'נחלה'})[:40])
print('"mark out" 34:7 / 34:8 / 34:10 vs "desire" Prov 23:3 / 23:6 / 24:1 / Deut 5:21 (תתאוה):', [t for t in raw('Num', 34, 7) if t[0] == 'תתאו'], [t for t in raw('Num', 34, 8) if t[0] == 'תתאו'], [t for t in raw('Num', 34, 10) if t[0] == 'והתאויתם'], [t for t in raw('Prov', 23, 3) if t[0] == 'תתאו'], [t for t in raw('Prov', 23, 6) if t[0] == 'תתאו'], [t for t in raw('Prov', 24, 1) if t[0] == 'תתאו'], [t for t in raw('Deut', 5, 21) if 'תתאוה' in t[0]])
print('"reach" 34:11 vs "blot" Num 5:23 / Deut 29:19 / Isa 25:8:', [t for t in raw('Num', 34, 11) if t[0] == 'ומחה'], [t for t in raw('Num', 5, 23) if t[0] == 'ומחה'], [t for t in raw('Deut', 29, 19) if t[0] == 'ומחה'], [t for t in raw('Isa', 25, 8) if t[0] == 'ומחה'], '| Num 5:23:', words('Num', 5, 23), '| Onkelos 5:23:', arm(5, 23), '| Onkelos 34:11:', arm(34, 11))
print('the great sea plene / defective 34:6 / 34:7 / Gen 15:18:', [t for t in raw('Num', 34, 6) if t[0] == 'הגדול'], [t for t in raw('Num', 34, 7) if t[0] == 'הגדל'], [t for t in raw('Gen', 15, 18) if t[0] == 'הגדל'])
print('Zin with the directional heh 34:4 vs the shield Ps 91:4 / 1Kgs 10:16:', [t for t in raw('Num', 34, 4) if t[0] == 'צנה'], [t for t in raw('Ps', 91, 4) if t[0] == 'צנה'], [t for t in raw('1Kgs', 10, 16) if t[0] == 'צנה'])
print('Ain 34:11 / Gen 14:7 vs the eye Ezek 12:12:', [t for t in raw('Num', 34, 11) if t[0] == 'לעין'], [t for t in raw('Gen', 14, 7) if t[0] == 'עין'], [t for t in raw('Ezek', 12, 12) if t[0] == 'לעין'])
print('---- THE FULL SEAT LISTS')
print('Kadesh-barnea (every prefix):', sorted(set(phrase(['קדש', 'ברנע']) + phrase(['לקדש', 'ברנע']) + phrase(['מקדש', 'ברנע']) + phrase(['בקדש', 'ברנע']) + phrase(['וקדש', 'ברנע']) + phrase(['ומקדש', 'ברנע']))), '| count:', len(set(phrase(['קדש', 'ברנע']) + phrase(['לקדש', 'ברנע']) + phrase(['מקדש', 'ברנע']) + phrase(['בקדש', 'ברנע']) + phrase(['וקדש', 'ברנע']) + phrase(['ומקדש', 'ברנע']))), '| Onkelos רקם גיאה seats:', [(c + 1, v + 1) for c in range(36) for v in range(len(onk_he[c])) if 'רקם גיאה' in ' '.join(arm(c + 1, v + 1))], '| Onkelos 32:8:', arm(32, 8))
print('Azmon (עצמנה / מעצמון / עצמונה / ועצמונה):', U('עצמנה', 'מעצמון', 'עצמון', 'עצמונה', 'ועצמונה', 'לעצמון'))
print('the Reubenite + the Gadite in one verse (every prefix):', sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if {'הראובני', 'והראובני', 'לראובני', 'ולראובני'} & {x for x, _, _ in ws} and {'הגדי', 'והגדי', 'לגדי', 'ולגדי'} & {x for x, _, _ in ws}}), '| Deut 3:16 / 29:7 / Josh 22:1:', words('Deut', 3, 16)[:3], words('Deut', 29, 7)[-6:], words('Josh', 22, 1))
print('"this shall be for you the border" — זה יהיה לכם גבול / וזה יהיה לכם גבול:', phrase(['זה', 'יהיה', 'לכם', 'גבול']), phrase(['וזה', 'יהיה', 'לכם', 'גבול']), '| והיה לכם:', phrase(['והיה', 'לכם']), '| לכם tokens in 34:', sum(1 for v in range(1, 30) for x in words('Num', 34, v) if x == 'לכם'), '| by verse:', {v: words('Num', 34, v).count('לכם') for v in range(1, 30) if 'לכם' in words('Num', 34, v)}, '| Josh 15:4 tail:', words('Josh', 15, 4)[-5:], '| לכם tokens in Josh 15:', sum(1 for v in range(1, 64) if ('Josh', 15, v) in by for x in words('Josh', 15, v) if x == 'לכם'), [(v, words('Josh', 15, v).count('לכם')) for v in range(1, 64) if ('Josh', 15, v) in by and 'לכם' in words('Josh', 15, v)])
print('---- THE FOUR PROMISED EXTENTS AGAINST THE CHAPTER (the river, the Euphrates, Lebanon, the sea of the Philistines, the western sea)')
for b, c, v in (('Gen', 15, 18), ('Exod', 23, 31), ('Deut', 1, 7), ('Deut', 11, 24), ('Josh', 1, 4), ('Deut', 34, 1), ('Deut', 34, 2), ('Deut', 34, 3)): print(f'  {b} {c}:{v}:', words(b, c, v))
print('  פרת / הנהר / לבנון / פלשתים / האחרון tokens in 34:', [(v, x) for v in range(1, 30) for x in words('Num', 34, v) if x in ('פרת', 'הנהר', 'הלבנון', 'לבנון', 'פלשתים', 'האחרון', 'נהר')], '| הים האחרון seats:', phrase(['הים', 'האחרון']), '| ים פלשתים:', phrase(['ים', 'פלשתים']), '| הנהר הגדל נהר פרת:', phrase(['הנהר', 'הגדל', 'נהר', 'פרת']), phrase(['הנהר', 'הגדול', 'נהר', 'פרת']))
print('---- THE ROSTER\'S COUNTS AND CHESALON')
print('בן tokens 34:17-28:', sum(1 for v in range(17, 29) for x in words('Num', 34, v) if x == 'בן'), '| Josh 15:10:', words('Josh', 15, 10), '| הוא כסלון:', phrase(['הוא', 'כסלון']), '| הוא + place in Josh 15 (the identity idiom):', [(v, words('Josh', 15, v)[i + 1]) for v in range(1, 64) if ('Josh', 15, v) in by for i, x in enumerate(words('Josh', 15, v)[:-1]) if x in ('הוא', 'היא')])
print('the princes\' names with אל: count 7 of 10 — the tokens:', [x for v in range(19, 29) for x, m, _ in by[('Num', 34, v)] if m and 'Np' in m and 'אל' in x and x not in ('ישראל',)], '| chapter 1\'s princes with אל (1:5-15):', [x for v in range(5, 16) for x, m, _ in by[('Num', 1, v)] if m and 'Np' in m and 'אל' in x and x not in ('ישראל',)], '| the spies with אל (13:4-15):', [x for v in range(4, 16) for x, m, _ in by[('Num', 13, v)] if m and 'Np' in m and 'אל' in x and x not in ('ישראל',)])
print('Josh 22:14:', words('Josh', 22, 14), '| Josh 22:13-14 the ten princes:', words('Josh', 22, 13))
print('the tribes\' four northern in 34:25-28 and Joshua 19:10-39 — Joshua\'s lot heads in order: Zebulun 19:10, Issachar 19:17, Asher 19:24, Naphtali 19:32, Dan 19:40 (printed at pass 2)')
print('---- THE STORE\'S "cord" GLOSSES — is every seat גבול? and the broken "inherit--mode-of-descent)" gloss')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
for g in ('cord', 'the-cord', 'and-cord', 'to-cord', 'from-cord', 'to-boundary-her/its'):
    rr = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1", (g,)).fetchall()
    print(f'  gloss {g!r}: tokens', rr)
print('  glosses containing "cord":', store.execute("SELECT w.gloss, COUNT(*) FROM words w WHERE w.gloss LIKE '%cord%' GROUP BY 1").fetchall())
print('  glosses containing "mode-of-descent":', store.execute("SELECT w.gloss, REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss LIKE '%mode-of-descent%' GROUP BY 1, 2").fetchall())
print('  glosses "the-powder" / "hidden" / "circle" / "Daniel" / "Non" / "mouth-in-a-figurative-sense" / "and-revolve" / "from-pasture" / "and-stroke" / "front-suffix" / "sunrise-suffix":', [(g, store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1", (g,)).fetchall()) for g in ('the-powder', 'hidden', 'circle', 'Daniel', 'Non', 'mouth-in-a-figurative-sense', 'and-revolve', 'from-pasture', 'and-stroke', 'front-suffix', 'sunrise-suffix', 'the-Jordan-suffix', 'from-region-across', 'exit-him/its', 'come/bring', 'and-bring-forth', 'in-pebble', 'Maaleh-accrabim', 'Kadeshbarnea', 'Hazar-addar', 'the-seas', 'seas')])
print('---- THE FIVE "COMMAND" SEATS AND THE SIFREI\'S LIST — the census')
print('צו את בני ישראל Torah:', phrase(['צו', 'את', 'בני', 'ישראל'], T), '| the row 1:2 names (EN): Vayikra 24:2, Bamidbar 35:2, Bamidbar 28:2, Bamidbar 34:2 + its own 5:2 — five = five')
print('---- ONKELOS: the one Aramaic tribe-word at 32:33 and in 34; the 18 שבטא; the princes\' רבא')
print('Onkelos 32:33:', arm(32, 33), '| שבט-tokens in Onkelos 34 by verse:', {v: [x for x in arm(34, v) if 'שבט' in x] for v in range(13, 29) if any('שבט' in x for x in arm(34, v))}, '| רבא tokens in Onkelos 34:', [(v, x) for v in range(1, 30) for x in arm(34, v) if x == 'רבא'], '| Onkelos 13:2 (the spies\' distributive):', arm(13, 2), '| Onkelos 17:21:', arm(17, 21))
print('Onkelos 34:2 תתפלג — the Hebrew תפל rendered "divided"; Onkelos 26:53 / 26:55 / 26:56 (the Hebrew יחלק / תחלק) for comparison:', arm(26, 53), arm(26, 55), arm(26, 56), '| Hebrew 26:53 / 55 / 56:', words('Num', 26, 53), words('Num', 26, 55), words('Num', 26, 56))
print('---- THE TWO FRAMES AND MOSES\' OWN: the speech spans by the frames — 34:1 (2-12), 34:13 Moses (13-15), 34:16 (17-29)')
print('34:1 / 34:16 identical?', words('Num', 34, 1) == words('Num', 34, 16), '| the count of "וידבר יהוה אל משה לאמר" verses in Numbers 30-36:', [f'{c}:{v}' for c in range(30, 37) for v in range(1, 60) if ('Num', c, v) in by and words('Num', c, v) == ['וידבר', 'יהוה', 'אל', 'משה', 'לאמר']])
print('the chapters of Numbers whose frame count is exactly 2:', [c for c in range(1, 37) if sum(1 for v in range(1, 90) if ('Num', c, v) in by and any(words('Num', c, v)[i] in ('ויאמר', 'וידבר') and words('Num', c, v)[i + 1] == 'יהוה' for i in range(len(words('Num', c, v)) - 1))) == 2])
print('---- THE NUMBERS BY THE PARSER, AGAIN (the print the asserts are typed from)')
sys.path.insert(0, f'{ROOT}/World/step9')
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
for b, c, v in (('Num', 34, 13), ('Num', 34, 14), ('Num', 34, 15), ('Num', 34, 18), ('Josh', 13, 7), ('Josh', 14, 2), ('Josh', 14, 3), ('Josh', 14, 4), ('Num', 32, 33), ('Num', 13, 2), ('Num', 7, 11), ('Num', 17, 21), ('Num', 1, 44), ('Josh', 3, 12), ('Josh', 4, 2), ('Ezek', 47, 13), ('Deut', 1, 23), ('Josh', 22, 14)):
    print(f'  {b} {c}:{v} N {CS.ink_numbers(CS.verse_words(b, c, v))} O {CS.ink_ordinals(CS.verse_words(b, c, v))} marked {[t for t in CS.verse_words(b, c, v) if t[-1] in "#~^%@|*"]}')
print('  every verse of 34 with a number or a mark:', [(v, CS.ink_numbers(CS.verse_words('Num', 34, v)), CS.ink_ordinals(CS.verse_words('Num', 34, v)), [t for t in CS.verse_words('Num', 34, v) if t[-1] in '#~^%@|*']) for v in range(1, 30) if CS.ink_numbers(CS.verse_words('Num', 34, v)) or CS.ink_ordinals(CS.verse_words('Num', 34, v)) or [t for t in CS.verse_words('Num', 34, v) if t[-1] in '#~^%@|*']])
