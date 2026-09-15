import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 14b: THE MEASUREMENT PASS ON THE RUNNER'S PROBE TOKENS, PHRASE SEATS, THE BORDER'S POINTS AND THE ROSTER before
# cold_run_borders.py is typed (7b's lesson: the hand's forms fall; type every token, every seat list and every slice from this print).
# jou_runner_measure.py's form. The callees' values the runner asserts come at the compile-measure step (typed from the recon's print).
import sys, io, contextlib, re, sqlite3, collections, unicodedata
sys.path.insert(0, (_ROOT + '/World/step9'))
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))
def strip(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
NF = lambda s: unicodedata.normalize('NFC', s)
_V = collections.OrderedDict(); _L = collections.OrderedDict(); _M = collections.OrderedDict(); _P = collections.OrderedDict()
for b, c, v, he, lm, mo in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append(lm.split('/')[-1].split(' ')[0] if lm else ''); _M.setdefault((b, c, v), []).append(mo or ''); _P.setdefault((b, c, v), []).append(NF(he.replace('/', '')))
def seats(phrase, books=None):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def rx(pattern, books=None):
    r = re.compile(pattern)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and r.search(' ' + ' '.join(ws) + ' ')]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
def lemma_seats(lm, books=None):
    return ['%s %d:%d' % k for k, ls in _L.items() if (books is None or k[0] in books) and lm in ls]
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
print('==== THE WORDS OF 34:1-29 (plain, with indices) ====')
for v in range(1, 30):
    print('%2d: %s' % (v, ' '.join('%d:%s' % (i, w) for i, w in enumerate(_V[('Num', 34, v)]))))
print('\n==== THE POINTED WORDS OF 34:1-29 (NFC) ====')
for v in range(1, 30):
    print('%2d: %s' % (v, ' '.join('%d:%s' % (i, w) for i, w in enumerate(_P[('Num', 34, v)]))))
print('\n==== THE PARSER at every verse of 34 and the kin verses ====')
KIN = [('Josh', 14, 2), ('Josh', 13, 7), ('Josh', 14, 3), ('Josh', 14, 4), ('Josh', 22, 14), ('Josh', 3, 12), ('Josh', 4, 2), ('Josh', 4, 4), ('Num', 13, 2), ('Num', 7, 11), ('Num', 17, 21), ('Num', 26, 53), ('Num', 26, 55), ('Num', 32, 33), ('Num', 1, 4), ('Num', 1, 44), ('Num', 34, 13), ('Num', 34, 15), ('Num', 34, 18), ('Ezek', 47, 13), ('Ezek', 48, 1), ('1Kgs', 8, 65), ('Num', 35, 1)]
for k in [('Num', 34, v) for v in range(1, 30)] + KIN:
    vw = CS.verse_words(*k); n = CS.ink_numbers(vw); o = CS.ink_ordinals(vw)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    if n or o or marked or k[0] != 'Num' or k[1] != 34: print('  %s %d:%d %s %s marked %s   %s' % (k[0], k[1], k[2], n, o, marked, ' '.join(_V[k])[:120] if k[0] != 'Num' or k[1] != 34 else ''))
print('\n==== THE BORDER\'S POINTS — the proper names of 34:3-12 with their lemmas and seats (Joshua 15 / Ezekiel 47 kin computed) ====')
for v in range(3, 13):
    names = [(w, l, m) for w, l, m in zip(_V[('Num', 34, v)], _L[('Num', 34, v)], _M[('Num', 34, v)]) if 'Np' in m]
    for w, l, m in names:
        s = lemma_seats(l)
        print('  34:%-2d %-14s lemma %-6s seats %2d: %s' % (v, w, l, len(s), s[:20]))
print('\n==== THE ROSTER — the names of 34:17-28 with their lemmas and seats ====')
for v in range(17, 29):
    names = [(w, l, m) for w, l, m in zip(_V[('Num', 34, v)], _L[('Num', 34, v)], _M[('Num', 34, v)]) if 'Np' in m]
    print('  34:%-2d %s' % (v, [(w, l, len(lemma_seats(l))) for w, l, m in names]))
print('\n==== THE PHRASE SEATS (the whole DB unless the Torah is named) ====')
for label, ph, bk in [('command the children of Israel', 'צו את בני ישראל', None), ('this is the land', 'זאת הארץ', None), ('that shall fall to you', 'אשר תפל לכם', None), ('shall fall (תפל)', 'תפל', None), ('as an inheritance', 'בנחלה', T), ('by its borders', 'לגבלתיה', None), ('the land of Canaan (with the article)', 'ארץ כנען', T),
                      ('the south side', 'פאת נגב', None), ('the wilderness of Zin', 'ממדבר צן', None), ('on the hands of Edom', 'על ידי אדום', None), ('the end of the Salt Sea', 'מקצה ים המלח', None), ('the Salt Sea', 'ים המלח', None), ('eastward', 'קדמה', None), ('the ascent of Akrabbim', 'למעלה עקרבים', None), ('Kadesh-barnea', 'קדש ברנע', None), ('Hazar-addar', 'חצר אדר', None), ('Azmon', 'עצמנה', None), ('Azmon (Josh)', 'עצמונה', None), ('the brook of Egypt', 'נחלה מצרים', None), ('the brook of Egypt (Kings)', 'נחל מצרים', None), ('its goings-out', 'תוצאתיו', None), ('the sea (goings-out at the sea)', 'הימה', None),
                      ('the west border', 'גבול ים', None), ('the great sea', 'הים הגדול', None), ('the great sea (defective)', 'הים הגדל', None), ('and its border', 'וגבול', None), ('the north border', 'גבול צפון', None), ('you shall mark out (Piel)', 'תתאו', None), ('you shall mark out for yourselves (Hitpael)', 'והתאויתם', None), ('Mount Hor', 'הר ההר', None), ('Lebo-hamath', 'לבא חמת', None), ('Zedad', 'צדדה', None), ('Ziphron', 'זפרנה', None), ('Hazar-enan', 'חצר עינן', None), ('Hazar-enan (Ezek)', 'חצר עינון', None),
                      ('the east border', 'לגבול קדמה', None), ('Shepham', 'שפמה', None), ('Riblah', 'הרבלה', None), ('Ain', 'לעין', None), ('the shoulder of the sea of Chinnereth', 'כתף ים כנרת', None), ('the sea of Chinnereth', 'ים כנרת', None), ('and it shall reach (ומחה)', 'ומחה', None), ('to the Jordan', 'הירדנה', None), ('round about', 'סביב', ('Num',)),
                      ('the nine tribes and the half tribe', 'לתשעת המטות וחצי המטה', None), ('the nine tribes (Josh 13:7)', 'לתשעת השבטים וחצי השבט', None), ('nine (construct)', 'תשעת', None), ('the two tribes and the half tribe', 'שני המטות וחצי המטה', None), ('took their inheritance', 'לקחו נחלתם', None), ('took (Reubenite Gadite)', 'מטה בני הראובני', None), ('the Reubenite', 'הראובני', None), ('the Gadite', 'הגדי', None), ('the half tribe of Manasseh (matteh)', 'חצי מטה מנשה', None), ('the half tribe of Manasseh (shevet)', 'חצי שבט מנשה', None), ('beyond the Jordan at Jericho', 'מעבר לירדן ירחו', None), ('eastward toward the sunrise', 'קדמה מזרחה', None), ('by lot', 'בגורל', None), ('you shall inherit (Hitpael)', 'תתנחלו', None), ('by the hand of Moses', 'ביד משה', None), ('as the LORD commanded by the hand of Moses', 'כאשר צוה יהוה ביד משה', None),
                      ('these are the names of the men', 'אלה שמות האנשים', None), ('who shall divide (ינחלו)', 'ינחלו', None), ('shall divide the land (Piel 34:29)', 'לנחל', None), ('to divide the land (Josh 19:49)', 'לנחל את הארץ', None), ('Eleazar the priest and Joshua son of Nun', 'אלעזר הכהן ויהושע בן נון', None), ('one prince one prince from a tribe', 'נשיא אחד נשיא אחד ממטה', None), ('one prince one prince', 'נשיא אחד נשיא אחד', None), ('one man one man', 'איש אחד איש אחד', None), ('Caleb son of Jephunneh', 'כלב בן יפנה', None), ('for the tribe of Judah Caleb son of Jephunneh', 'למטה יהודה כלב בן יפנה', None), ('prince (נשיא)', 'נשיא', ('Num',)), ('Ammihud', 'עמיהוד', None), ('Shemuel', 'שמואל', None), ('Elidad', 'אלידד', None), ('Kemuel', 'קמואל', None), ('Elizaphan', 'אליצפן', None), ('Paltiel', 'פלטיאל', None), ('Ahihud', 'אחיהוד', None), ('Pedahel', 'פדהאל', None), ('Chislon', 'כסלון', None), ('Bukki', 'בקי', None), ('Hanniel', 'חניאל', None), ('Ephod', 'אפד', None), ('Jogli', 'יגלי', None), ('Shiphtan', 'שפטן', None), ('Parnach', 'פרנך', None), ('Azzan', 'עזן', None), ('Shelomi', 'שלמי', None),
                      ('these are they whom the LORD commanded', 'אלה אשר צוה יהוה', None), ('as the LORD commanded Moses (the receipt)', 'כאשר צוה יהוה את משה', ('Num',)), ('and the LORD spoke to Moses saying (Num 34)', 'וידבר יהוה אל משה לאמר', ('Num',)), ('and Moses commanded the children of Israel', 'ויצו משה את בני ישראל', None), ('the tribe of (למטה) + sons', 'ולמטה בני', None), ('shall be to you (יהיה לכם)', 'יהיה לכם', ('Num',)), ('shall be to you (והיה לכם)', 'והיה לכם', None)]:
    s = seats(ph, bk); print('  %-70s %d %s' % (label, len(s), s[:26]))
print('\n==== JOSHUA 15:1-4 AGAINST 34:3-5 — the shared tokens (computed) ====')
J = [w for v in range(1, 5) for w in _V[('Josh', 15, v)]]; Nm = [w for v in range(3, 6) for w in _V[('Num', 34, v)]]
print('  Num 34:3-5 tokens %d; Josh 15:1-4 tokens %d; shared (Num tokens present in Josh) %d: %s' % (len(Nm), len(J), sum(1 for w in Nm if w in J), [w for w in Nm if w in J]))
for v in range(1, 5): print('  Josh 15:%d %s' % (v, ' '.join(_V[('Josh', 15, v)])))
print('  Josh 15:12 %s' % ' '.join(_V[('Josh', 15, 12)]))
print('  Josh 18:20 %s' % ' '.join(_V[('Josh', 18, 20)])); print('  Josh 19:49 %s' % ' '.join(_V[('Josh', 19, 49)])); print('  Josh 19:51 %s' % ' '.join(_V[('Josh', 19, 51)])); print('  Josh 14:1 %s' % ' '.join(_V[('Josh', 14, 1)])); print('  Josh 14:2 %s' % ' '.join(_V[('Josh', 14, 2)])); print('  Josh 13:7 %s' % ' '.join(_V[('Josh', 13, 7)])); print('  Josh 13:32 %s' % ' '.join(_V[('Josh', 13, 32)]))
print('  Josh 21:5 %s' % ' '.join(_V[('Josh', 21, 5)])); print('  Josh 21:6 %s' % ' '.join(_V[('Josh', 21, 6)])); print('  Josh 22:14 %s' % ' '.join(_V[('Josh', 22, 14)]))
print('\n==== EZEKIEL 47:13-20, 48:1, 48:28 — the tokens and the shared names ====')
E = []
for v in range(13, 21): E += _V[('Ezek', 47, v)]; print('  Ezek 47:%d %s' % (v, ' '.join(_V[('Ezek', 47, v)])))
print('  Ezek 48:1 %s' % ' '.join(_V[('Ezek', 48, 1)])); print('  Ezek 48:28 %s' % ' '.join(_V[('Ezek', 48, 28)]))
NA = [w for v in range(1, 30) for w in _V[('Num', 34, v)]]
print('  Num 34 tokens present in Ezek 47:13-20 (set): %s' % sorted(set(w for w in NA if w in E)))
print('\n==== THE KIN VERSES (the words) ====')
for k in [('Num', 13, 2), ('Num', 13, 6), ('Num', 13, 21), ('Num', 7, 11), ('Num', 17, 21), ('Num', 1, 4), ('Num', 1, 10), ('Num', 26, 52), ('Num', 26, 53), ('Num', 26, 55), ('Num', 26, 56), ('Num', 27, 18), ('Num', 27, 19), ('Num', 27, 22), ('Num', 32, 28), ('Num', 32, 33), ('Num', 33, 51), ('Num', 33, 54), ('Num', 20, 22), ('Num', 5, 23), ('Exod', 27, 9), ('Exod', 27, 13), ('Gen', 14, 3), ('Gen', 15, 18), ('Exod', 23, 31), ('Deut', 1, 7), ('Deut', 11, 24), ('Josh', 1, 4), ('Deut', 34, 4), ('Deut', 29, 19), ('Isa', 25, 8), ('Prov', 23, 3), ('1Kgs', 8, 65), ('2Kgs', 14, 25), ('Num', 36, 5), ('Num', 34, 13)]:
    print('  %s %d:%d %s' % (k[0], k[1], k[2], ' '.join(_V[k])))
print('\n==== THE TRIBE-NOUNS in 34 and the neighbours (matteh 4294 / shevet 7626 by lemma) ====')
for k in [('Num', 34, v) for v in range(13, 30)] + [('Num', 32, 33), ('Num', 36, 3), ('Num', 36, 4), ('Josh', 13, 7), ('Josh', 14, 2)]:
    ms = [(w, l) for w, l in zip(_V[k], _L[k]) if l in ('4294', '7626')]
    if ms: print('  %s %d:%d %s' % (k[0], k[1], k[2], ms))
print('  matteh 4294 in Num 34: %d tokens; shevet 7626 in Num 34: %d tokens' % (sum(1 for v in range(1, 30) for l in _L[('Num', 34, v)] if l == '4294'), sum(1 for v in range(1, 30) for l in _L[('Num', 34, v)] if l == '7626')))
print('\n==== THE ROSTER ORDER against the Torah\'s twelve (computed on the Np tokens by lemma; the tribe lemmas) ====')
TRIBE = {'3063': 'judah', '8095': 'simeon', '1144': 'benjamin', '1835': 'dan', '4519': 'manasseh', '669': 'ephraim', '2074': 'zebulun', '3485': 'issachar', '836': 'asher', '5321': 'naphtali', '7205': 'reuben', '1410': 'gad', '3878': 'levi', '3130': 'joseph'}
def order(rng):
    out = []
    for k in rng:
        for w, l in zip(_V[k], _L[k]):
            if l in TRIBE and TRIBE[l] not in out: out.append(TRIBE[l])
    return out
LISTS = {'Gen 29-30 births': [('Gen', 29, v) for v in range(31, 36)] + [('Gen', 30, v) for v in range(1, 25)], 'Gen 35:23-26': [('Gen', 35, v) for v in range(23, 27)], 'Gen 46:8-25': [('Gen', 46, v) for v in range(8, 26)], 'Gen 49': [('Gen', 49, v) for v in range(3, 28)], 'Exod 1:2-4': [('Exod', 1, v) for v in range(2, 5)], 'Num 1:5-15': [('Num', 1, v) for v in range(5, 16)], 'Num 1:20-43': [('Num', 1, v) for v in range(20, 44)], 'Num 2': [('Num', 2, v) for v in range(3, 32)], 'Num 7:12-83': [('Num', 7, v) for v in range(12, 84)], 'Num 10:14-27': [('Num', 10, v) for v in range(14, 28)], 'Num 13:4-15': [('Num', 13, v) for v in range(4, 16)], 'Num 26:5-50': [('Num', 26, v) for v in range(5, 51)], 'Num 34:19-28': [('Num', 34, v) for v in range(19, 29)], 'Deut 27:12-13': [('Deut', 27, v) for v in (12, 13)], 'Deut 33': [('Deut', 33, v) for v in range(6, 25)], 'Josh 13-19 lots': [('Josh', c, v) for c in range(13, 20) for v in range(1, 60) if ('Josh', c, v) in _V], 'Ezek 48:1-7,23-27': [('Ezek', 48, v) for v in list(range(1, 8)) + list(range(23, 28))]}
for n, rng in LISTS.items(): print('  %-18s %s' % (n, order(rng)))
print('\n==== THE CHAPTER\'S DIVINE FRAMES / NARRATIVE VERBS ====')
for v in range(1, 30):
    vs = [(w, m) for w, m in zip(_V[('Num', 34, v)], _M[('Num', 34, v)]) if m.startswith('HVq') or 'Vqw' in m or 'Vpw' in m]
    if vs: print('  34:%d wayyiqtol %s' % (v, vs))
print('  34:1 / 34:16 / 35:1 frames: %s | %s | %s' % (' '.join(_V[('Num', 34, 1)]), ' '.join(_V[('Num', 34, 16)]), ' '.join(_V[('Num', 35, 1)])))
