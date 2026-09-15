import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 15 — THE REFUGE CITIES (2026-09-13): THE THIRD MEASUREMENT PASS — the prints the second pass lacked: the token-FAMILY
# censuses where the DB's lemma column carries a prefix (מגרש, מקלט, the murder-root, the pollute-root, the enmity-word, the thrust-root, the
# hifil of "happen"), Joshua 21:36's text, the store's 'in-mother' seats, the whole by-reference idx list for the chapter, the homographs by
# morph (the smitten Midianite woman / the smiter; 'seas' / 'days'; 'lie in wait' / 'provisions'; 'until' / 'witness'), the pointed forms the
# asserts will compare on NFC, the dual's misread at 1 Samuel 13:2, the Decalogue's two verbs, the rows' first citations for the head check.
# Nothing asserted. Sitting 14's form (bor_measure2.py).
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m, lem in rows: by.setdefault((b, c, v), []).append((plain(he), m, he, lem))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
C = 35; NV = 34
def words(b, c, v): return [x for x, _, _, _ in by[(b, c, v)]]
def wm(b, c, v): return [(x, m) for x, m, _, _ in by[(b, c, v)]]
def raw(b, c, v): return [(x, m, NF(pointed(r))) for x, m, r, _ in by[(b, c, v)]]
def base(l): return (l or '').split('/')[-1].strip()
def FAM(sub, books=None): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) for x, _, _, _ in ws if sub in x})
def FAMT(sub, books=None): return [(f'{b} {c}:{v}', x, m) for (b, c, v), ws in by.items() if (books is None or b in books) for x, m, _, _ in ws if sub in x]
def LEMB(lem, books=None): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) for x, _, _, l in ws if base(l) == lem})
def LEMT(lem, books=None): return [(f'{b} {c}:{v}', x, m) for (b, c, v), ws in by.items() if (books is None or b in books) for x, m, _, l in ws if base(l) == lem]
def phrase(seq, books=None):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _, _, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def U(*toks, books=None): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if books is None or b in books for x, _, _, _ in ws if x in toks})
def in35(pred): return [(v, x, m) for v in range(1, NV + 1) for x, m, _, _ in by[('Num', C, v)] if pred(x, m)]
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
def arm(c, v): return [plain(x) for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']; sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
def E(p, r): return clean(sif[p - 1][r - 1])
def Hb(p, r): return clean(sif_he[p - 1][r - 1])
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))

print('==== THE ROWS\' FIRST CITATIONS (the head check): EN first "(Book n:m)" per row of 159-161')
for p in (159, 160, 161):
    for r in range(1, len(sif[p - 1]) + 1):
        m = re.search(r'\(([A-Z][a-z]+)\.? ?(\d+):(\d+)', E(p, r)); print(f'  {p}:{r}: {m.groups() if m else None} | HE opens {Hb(p, r)[:28]!r}')
print('==== THE TOKEN FAMILIES (the DB lemma column carries prefixes — the family by substring, then by the base lemma)')
print('  מגרש family Torah:', FAM('מגרש', T), '| Bible count (verses):', len(FAM('מגרש')), '| tokens:', len(FAMT('מגרש')), '| Josh 21 verses:', len([s for s in FAM('מגרש') if s.startswith('Josh 21')]), '| by base lemma 4054:', len(LEMB('4054')), 'verses,', len(LEMT('4054')), 'tokens; Torah:', LEMB('4054', T))
print('  מקלט family: verses', FAM('מקלט'), '| tokens', len(FAMT('מקלט')), '| in Deut:', FAM('מקלט', ('Deut',)), '| by base lemma 4733:', len(LEMT('4733')), LEMB('4733'))
print('  the murder-root by base lemma 7523: Torah tokens', len(LEMT('7523', T)), LEMT('7523', T), '\n     Bible tokens', len(LEMT('7523')), '| Bible verses', len(LEMB('7523')), LEMB('7523'))
print('  the tokens in 35 by base lemma 7523:', len(in35(lambda x, m: False)) or [(v, x, m) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '7523'], '| count:', sum(1 for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '7523'))
print('  plene רוצח tokens anywhere:', FAMT('רוצח'), '| defective in Numbers 35 every one?', all('רוצח' not in x for v in range(1, NV + 1) for x, _, _, _ in by[('Num', C, v)]))
print('  the pollute-root by base lemma 2610:', LEMT('2610'), '| family חנפ / חנף:', FAMT('חנפ') + FAMT('חנף'))
print('  the enmity-word by base lemma 342:', LEMT('342'), '| family איבה:', FAMT('איבה'))
print('  the thrust-root by base lemma 1920:', LEMT('1920'))
print('  "happen" hifil (base 7136 with the hifil morph):', [(s, x, m) for s, x, m in LEMT('7136') if m and 'Vh' in m], '| all base 7136 Torah:', LEMT('7136', T))
print('  the flee-root נוס base 5127 Torah tokens:', len(LEMT('5127', T)), '| in 35:', [(v, x) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '5127'])
print('  the smite-root נכה base 5221 in 35:', [(v, x, m) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '5221'], '| count:', sum(1 for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '5221'))
print('  the die-root מות base 4191 in 35 tokens:', sum(1 for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '4191'), [(v, x, m) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '4191'])
print('  the blood-word דם base 1818 in 35:', [(v, x) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '1818'], '| count:', sum(1 for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '1818'))
print('  the redeem/avenge root גאל base 1350 in 35:', [(v, x, m) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '1350'], '| Torah tokens of 1350:', len(LEMT('1350', T)))
print('  the city-word עיר base 5892 in 35 tokens:', sum(1 for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '5892'), '| the give-verb נתן base 5414 in 35:', [(v, x) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) == '5414'], '| תתנו count in 35:', sum(1 for v in range(1, NV + 1) for x in words('Num', C, v) if x == 'תתנו'))
print('  the atone root כפר base 3722 / the ransom 3724 in 35:', [(v, x, m, base(l)) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if base(l) in ('3722', '3724')], '| the ransom noun base 3724 all seats:', LEMB('3724'))
print('  the pasture-land/refuge/avenger/murderer Onkelos counts vs the Hebrew: מקלט tokens in 35:', sum(1 for v in range(1, NV + 1) for x in words('Num', C, v) if 'מקלט' in x), '| Onkelos שזב tokens in 35:', sum(1 for v in range(1, NV + 1) for x in arm(35, v) if 'שזב' in x), '| הרצח tokens in 35:', sum(1 for v in range(1, NV + 1) for x in words('Num', C, v) if x == 'הרצח'), '| Onkelos קטולא tokens in 35:', sum(1 for v in range(1, NV + 1) for x in arm(35, v) if x == 'קטולא'), '| Onkelos קטול (bare, 35:31):', [(v, x) for v in range(1, NV + 1) for x in arm(35, v) if x == 'קטול'])
print('==== JOSHUA 21:36 AND THE SIX IN JOSHUA 21')
for v in (13, 21, 27, 32, 36, 38): print(f'  Josh 21:{v}:', words('Josh', 21, v))
print('  Josh 21:36-37 present in the DB?', ('Josh', 21, 36) in by, ('Josh', 21, 37) in by, '| verses in Josh 21:', max(v for (b, c, v) in by if b == 'Josh' and c == 21))
print('==== THE HOMOGRAPHS BY MORPH AND LEMMA')
print('  המכה every seat with morph and base lemma:', [(s, m, base(l)) for (b, c, v), ws in by.items() for x, m, _, l in ws if x == 'המכה' for s in [f'{b} {c}:{v}']])
print('  ימים glossed seas — the store:', None, '| צדה tokens with base lemma:', [(f'{b} {c}:{v}', base(l)) for (b, c, v), ws in by.items() for x, m, _, l in ws if x == 'צדה'], '| בצדיה / צדיה base:', [(v, x, base(l)) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if 'צדיה' in x])
print('  עד "until" (5704) vs "witness" (5707) — 35:', [(v, x, base(l)) for v in range(1, NV + 1) for x, m, _, l in by[('Num', C, v)] if x in ('עד', 'ועד', 'עדים')], '| עד אחד seats with base lemma of עד:', [(s, [base(l) for x, m, _, l in by[(s.split()[0], int(s.split()[1].split(':')[0]), int(s.split()[1].split(':')[1]))] if x == 'עד']) for s in phrase(['עד', 'אחד'])])
print('  מגאל at Malachi 1:7 / 1:12 (base lemma) vs Num 35:12 / Josh 20:3:', [(f'{b} {c}:{v}', m, base(l)) for (b, c, v), ws in by.items() for x, m, _, l in ws if x == 'מגאל'])
print('  אשר ימות בו at 2 Kgs 13:14:', words('2Kgs', 13, 14)[:8])
print('  יענה at Gen 41:16 (base) vs 35:30:', [(f'{b} {c}:{v}', base(l)) for (b, c, v), ws in by.items() if b in T for x, m, _, l in ws if x == 'יענה'], '| the answer-verb 6030 with a witness-word in the verse, Torah:', sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T and any(base(l) == '6030' for x, m, _, l in ws) and any(x in ('עד', 'ועד', 'עדים', 'שקר', 'שוא', 'ברעך', 'רב') for x, m, _, l in ws)}))
print('  Exod 20:13 / 20:16 / Deut 5:17 / 5:20:', words('Exod', 20, 13), words('Exod', 20, 16), words('Deut', 5, 17), words('Deut', 5, 20))
print('==== THE POINTED FORMS FOR THE NFC ASSERTS')
print('  35:5 אלפים:', [t[2] for t in raw('Num', 35, 5) if t[0] == 'אלפים'], '| 1 Sam 13:2 both:', [t for t in raw('1Sam', 13, 2) if t[0] == 'אלפים'], '| Exod 18:21 אלפים:', [t for t in raw('Exod', 18, 21) if t[0] == 'אלפים'], '| Num 31:14:', [t for t in raw('Num', 31, 14) if t[0] == 'אלפים'], '| Josh 3:4:', [t for t in raw('Josh', 3, 4) if t[0] == 'כאלפים'])
print('  the dual\'s eleven bare seats — the parser now:', {s: N(s.split()[0], int(s.split()[1].split(':')[0]), int(s.split()[1].split(':')[1])) for s in ('Num 35:5', 'Josh 3:4', 'Josh 7:3', 'Judg 20:45', '1Sam 13:2', '1Kgs 7:26', '2Kgs 18:23', 'Isa 36:8')})
print('  1 Sam 13:2 tokens:', CS.verse_words('1Sam', 13, 2), '| Judg 20:45 tokens:', CS.verse_words('Judg', 20, 45), '| 1 Kgs 7:26:', CS.verse_words('1Kgs', 7, 26))
print('  הגדל at 35:25 / 35:28 / Lev 21:10 הגדול:', [t for t in raw('Num', 35, 25) if t[0] == 'הגדל'], [t for t in raw('Num', 35, 28) if t[0] == 'הגדל'], [t for t in raw('Lev', 21, 10) if t[0] == 'הגדול'])
print('  יחניף / תחניפו pointed:', [t for t in raw('Num', 35, 33) if 'חניפ' in t[0]], '| יכפר pual pointed:', [t for t in raw('Num', 35, 33) if t[0] == 'יכפר'], '| Deut 21:8 ונכפר:', [t for t in raw('Deut', 21, 8) if 'כפר' in t[0]])
print('  רצח participle at 35:11 vs הרצח 35:12 pointed:', [t for t in raw('Num', 35, 11) if t[0] == 'רצח'], [t for t in raw('Num', 35, 12) if t[0] == 'הרצח'], '| ורצח 35:27 (the verb):', [t for t in raw('Num', 35, 27) if t[0] == 'ורצח'], '| ירצח 35:30:', [t for t in raw('Num', 35, 30) if t[0] == 'ירצח'])
print('  אמה at 35:4 pointed (the cubit) vs אמה the maidservant (Exod 21:7) vs אמה her mother (Gen 24:28):', [t for t in raw('Num', 35, 4) if t[0] == 'אמה'], [t for t in raw('Exod', 21, 7) if t[0] == 'אמה'], [t for t in raw('Gen', 24, 28) if t[0] == 'אמה'])
print('  יצא יצא 35:26 pointed:', [t for t in raw('Num', 35, 26) if t[0] == 'יצא'], '| Gen 27:30:', [t for t in raw('Gen', 27, 30) if t[0] == 'יצא'])
print('  מות יומת at 35:16 pointed:', [t for t in raw('Num', 35, 16) if t[0] in ('מות', 'יומת')], '| מות (the noun "death of") at 35:25:', [t for t in raw('Num', 35, 25) if t[0] == 'מות'])
print('==== THE STORE: the in-mother seats, the seas/days, the whole by-reference idx list')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
print('  in-mother seats:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='in-mother' ORDER BY v.id").fetchall())
print('  mother seats (the bare אמה / אם):', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='mother' ORDER BY v.id").fetchall())
print('  seas seats with ימים:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='seas' AND w.he_plain LIKE '%ימים%' ORDER BY v.id").fetchall())
print('  eye seats with the answer-verb:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='eye' AND w.he_plain LIKE '%ענ%' ORDER BY v.id").fetchall())
print('  the-strike seats:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='the-strike' ORDER BY v.id").fetchall())
print('  and-light-upon seats:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='and-light-upon' ORDER BY v.id").fetchall())
print('  concretely seats:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss IN ('concretely','and-concretely') ORDER BY v.id").fetchall())
print('  dash-in-pieces seats (the two roots):', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/',''), w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss IN ('dash-in-pieces','and-dash-in-pieces') ORDER BY v.id").fetchall())
print('  be-the-next-of-kin seats (books):', Counter(b for b, in store.execute("SELECT v.book FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='be-the-next-of-kin'")), '| Numbers seats:', store.execute("SELECT v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='be-the-next-of-kin' AND v.book='Num'").fetchall())
print('  and-snatch-away seats:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='and-snatch-away' ORDER BY v.id").fetchall())
print('  and-judge seats:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='and-judge' ORDER BY v.id").fetchall())
print('  and-stretch measure seats:', store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='and-stretch' AND w.he_plain LIKE '%מד%' ORDER BY v.id").fetchall())
print('  bring-forth seats in Num 35:', store.execute("SELECT v.verse, w.idx, REPLACE(w.he_plain,'/','') FROM words w JOIN verses v ON w.verse_id=v.id WHERE w.gloss='bring-forth' AND v.book='Num' AND v.chapter=35").fetchall())
IDX = [(v, i, t.replace('/', ''), g) for v, i, t, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=35 ORDER BY v.id, w.idx")]
print('  ALL (verse, idx, token, gloss) of Num 35 — for the by-reference rows:')
for v in range(1, NV + 1): print(f'    {v}:', [(i, t, g) for vv, i, t, g in IDX if vv == v])
print('==== THE SHELF\'S QUOTATIONS READ TO THEIR VERSES — the tokens')
print('  Exod 21:18:', words('Exod', 21, 18), '| Exod 21:20:', words('Exod', 21, 20), '| Deut 19:11:', words('Deut', 19, 11), '| Lev 24:22:', words('Lev', 24, 22), '| Exod 22:8 head:', words('Exod', 22, 8)[:8], '| Exod 23:2:', words('Exod', 23, 2), '| Deut 12:29:', words('Deut', 12, 29), '| Deut 19:1:', words('Deut', 19, 1), '| Num 26:3:', words('Num', 26, 3), '| Deut 21:4:', words('Deut', 21, 4), '| Deut 21:1:', words('Deut', 21, 1), '| Lev 16:16:', words('Lev', 16, 16), '| Lev 15:31:', words('Lev', 15, 31), '| Isa 43:14 head:', words('Isa', 43, 14)[:8], '| Jer 49:38:', words('Jer', 49, 38), '| Isa 63:1 head:', words('Isa', 63, 1)[:7], '| Song 4:8 head:', words('Song', 4, 8)[:8], '| Exod 21:30:', words('Exod', 21, 30), '| Exod 21:15:', words('Exod', 21, 15))
print('  the two priests on the ramp — Tosefta / Mishnah local? shelf dirs with Yoma:', sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if 'Yoma' in d or 'Shevuot' in d or 'Makkot' in d or 'Sanhedrin' in d or 'Sotah' in d))
print('==== THE REGISTER GATE\'S SEATS IN 35 (the count lines) — register_dispositions.yaml entries naming Num 35:')
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read()
print('  ', re.findall(r'^([^\n]*Num 35[^\n]*)$', RD, re.M)[:20])
print('  the REGISTER_INDEX lines naming Num 35:', [l[:200] for l in open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read().split('\n') if 'Num 35' in l][:12])
