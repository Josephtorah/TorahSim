import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 15b: THE MEASUREMENT PASS ON THE RUNNER'S PROBE TOKENS, PHRASE SEATS, THE CASE TOKENS AND THE DUAL'S SEATS before
# cold_run_refuge.py is typed (7b's lesson: the hand's forms fall; type every token, every seat list and every slice from this print).
# bor_runner_measure.py's form. (A) the words of 35:1-34 plain and pointed with indices; (B) THE PARSER at every verse of 35 and at the kin —
# THE BARE DUAL THOUSAND's 26 seats by the points (patach + dagesh in the pe), each with the parser's CURRENT read and the next word (the probes
# are typed from this print, the expected numbers the ink's own); the plural's seats counted; (C) the phrase seats; (D) the case tokens and the
# verbs; (E) the kin verses.
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
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
def lemma_seats(lm, books=None):
    return ['%s %d:%d' % k for k, ls in _L.items() if (books is None or k[0] in books) and lm in ls]
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
print('==== (A) THE WORDS OF 35:1-34 (plain, with indices) ====')
for v in range(1, 35):
    print('%2d: %s' % (v, ' '.join('%d:%s' % (i, w) for i, w in enumerate(_V[('Num', 35, v)]))))
print('\n==== THE POINTED WORDS OF 35:1-34 (NFC) ====')
for v in range(1, 35):
    print('%2d: %s' % (v, ' '.join('%d:%s' % (i, w) for i, w in enumerate(_P[('Num', 35, v)]))))
print('\n==== (B) THE PARSER at every verse of 35 and the kin verses ====')
KIN = [('Num', 4, 36), ('Num', 4, 40), ('Num', 7, 85), ('Exod', 38, 29), ('Dan', 8, 14), ('Josh', 3, 4), ('Josh', 7, 3), ('Judg', 20, 45), ('1Sam', 13, 2), ('1Kgs', 7, 26), ('2Kgs', 18, 23), ('Isa', 36, 8), ('Exod', 18, 21), ('Num', 1, 46), ('Exod', 32, 28), ('Num', 10, 36), ('Deut', 33, 17), ('Num', 31, 54), ('Ezek', 45, 2), ('Exod', 27, 9), ('Num', 21, 13), ('Num', 26, 54), ('Num', 26, 62), ('Num', 3, 39), ('Josh', 21, 41), ('Josh', 21, 4), ('Josh', 21, 5), ('Josh', 21, 6), ('Josh', 21, 7), ('Deut', 19, 2), ('Deut', 19, 9), ('Deut', 4, 41), ('Exod', 22, 1), ('Exod', 21, 30), ('Deut', 17, 6), ('Deut', 19, 15), ('Num', 36, 1)]
for k in [('Num', 35, v) for v in range(1, 35)] + KIN:
    vw = CS.verse_words(*k); n = CS.ink_numbers(vw); o = CS.ink_ordinals(vw)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    if n or o or marked or k[0] != 'Num' or k[1] != 35: print('  %s %d:%d %s %s marked %s   %s' % (k[0], k[1], k[2], n, o, marked, ' '.join(_V[k])[:140] if k[0] != 'Num' or k[1] != 35 else ''))
print('\n==== THE DUAL "TWO THOUSAND" BY THE POINTS ON THE WHOLE DB — every token whose plain form ends in אלפים, split dual / plural by the pe\'s patach ====')
dual, plur = [], []
for k, ws in _P.items():
    for i, pw in enumerate(ws):
        pl = strip(pw)
        if pl.endswith('אלפים') and pl.lstrip('ובכלמה') == 'אלפים':
            st = pw[pw.rfind('פ'):]
            isdual = 'פַּ' in NF(st) or ('ַ' in st[:3] and 'ּ' in st[:3])
            (dual if isdual else plur).append((k, i, pw))
print('  dual seats %d; plural seats %d' % (len(dual), len(plur)))
for k, i, pw in dual:
    vw = CS.verse_words(*k); n = CS.ink_numbers(vw)
    nxt = _V[k][i + 1] if i + 1 < len(_V[k]) else '<end>'; prv = _V[k][i - 1] if i > 0 else '<start>'
    print('  DUAL %-14s idx %2d %-12s prev %-12s next %-12s current read %s   | %s' % ('%s %d:%d' % k, i, pw, prv, nxt, n, ' '.join(_V[k])[:110]))
print('  the plural\'s seats (first 40): %s' % ['%s %d:%d' % k for k, i, pw in plur][:40])
print('  the plural seats whose NEXT word is a numeral (the current rule\'s 2000 path): %s' % [('%s %d:%d' % k, _V[k][i + 1]) for k, i, pw in plur if i + 1 < len(_V[k]) and CS._bare(_V[k][i + 1].replace('־', '')) is not None][:30])
print('  the plural seats read by the parser NOW (any number containing 2000 as a bare addend): %s' % [('%s %d:%d' % k, CS.ink_numbers(CS.verse_words(*k))) for k, i, pw in plur if any(x == 2000 for x in CS.ink_numbers(CS.verse_words(*k)) if isinstance(x, int))][:30])
print('  THE CODE POINTS of 35:5\'s first dual and of 1:46\'s plural: %s | %s' % ([hex(ord(c)) for c in _P[('Num', 35, 5)][7]], [hex(ord(c)) for c in _P[('Num', 1, 46)][6] if 'אלפים' in strip(_P[('Num', 1, 46)][6])] if 'אלפים' in strip(_P[('Num', 1, 46)][6]) else [(i, w) for i, w in enumerate(_P[('Num', 1, 46)]) if 'אלפים' in strip(w)]))
print('  35:5 the pointed words with indices: %s' % [(i, w) for i, w in enumerate(_P[('Num', 35, 5)])])
print('  35:4 the pointed words: %s' % [(i, w) for i, w in enumerate(_P[('Num', 35, 4)])])
print('  Josh 3:4 the pointed words: %s' % [(i, w) for i, w in enumerate(_P[('Josh', 3, 4)])])
print('  verse_words at 35:5: %s' % CS.verse_words('Num', 35, 5))
print('  verse_words at 35:4: %s' % CS.verse_words('Num', 35, 4))
print('  verse_words at Josh 3:4: %s' % CS.verse_words('Josh', 3, 4))
print('  verse_words at 1Sam 13:2: %s' % CS.verse_words('1Sam', 13, 2))
print('  verse_words at Judg 20:45: %s' % CS.verse_words('Judg', 20, 45))
print('  verse_words at Josh 7:3: %s' % CS.verse_words('Josh', 7, 3))
print('  verse_words at Exod 18:21: %s' % CS.verse_words('Exod', 18, 21))
print('  the cubit tokens: אמה %d seats, באמה %d, אמות %d, האמה %d (Bible); Torah: %s' % (len(tok('אמה')), len(tok('באמה')), len(tok('אמות')), len(tok('האמה')), (len(tok('אמה', T)), len(tok('באמה', T)), len(tok('אמות', T)), len(tok('האמה', T)))))
print('  "באמה" seats: %s' % tok('באמה'))
print('\n==== (C) THE PHRASE SEATS (the whole DB unless the Torah is named) ====')
for label, ph, bk in [('command the children of Israel', 'צו את בני ישראל', None), ('and they shall give to the Levites', 'ונתנו ללוים', None), ('cities to dwell in', 'ערים לשבת', None), ('pasture-land (מגרש)', 'מגרש', None), ('and pasture-land', 'ומגרש', None), ('their pasture-lands', 'מגרשיהן', None), ('the pasture-lands of the cities', 'מגרשי הערים', None), ('from the wall of the city outward', 'מקיר העיר וחוצה', None), ('a thousand cubits', 'אלף אמה', None), ('two thousand by the cubit', 'אלפים באמה', None), ('and you shall measure', 'ומדתם', None), ('the east side', 'פאת קדמה', None), ('the south side', 'פאת נגב', None), ('the west side', 'פאת ים', None), ('the north side', 'פאת צפון', None), ('and the city in the midst', 'והעיר בתוך', None), ('six cities of refuge', 'שש ערי מקלט', None), ('the six cities of refuge', 'שש ערי המקלט', None), ('cities of refuge', 'ערי מקלט', None), ('the cities of refuge', 'ערי המקלט', None), ('forty and two cities', 'ארבעים ושתים עיר', None), ('forty and eight cities', 'ארבעים ושמנה עיר', None), ('forty and eight', 'ארבעים ושמנה', None), ('the many you shall take more', 'מאת הרב תרבו', None), ('the few you shall take less', 'ומאת המעט תמעיטו', None), ('each according to his inheritance', 'כפי נחלתו', None),
                      ('when you cross the Jordan', 'כי אתם עברים את הירדן', None), ('to the land of Canaan (Canaan-ward)', 'ארצה כנען', None), ('and you shall appoint', 'והקריתם', None), ('smites a soul unwittingly', 'מכה נפש בשגגה', None), ('whoever smites a soul', 'כל מכה נפש', None), ('unwittingly', 'בשגגה', None), ('without knowledge', 'בבלי דעת', None), ('the avenger (bare)', 'מגאל', None), ('the avenger of blood', 'גאל הדם', None), ('until he stands before the congregation for judgment', 'עד עמדו לפני העדה למשפט', None), ('the three cities', 'שלש הערים', None), ('three cities', 'שלש ערים', None), ('the stranger and the sojourner', 'לגר ולתושב', None), ('to flee there', 'לנוס שמה', None), ('he shall flee there', 'ינוס שמה', None),
                      ('instrument of iron', 'בכלי ברזל', None), ('a stone of the hand', 'באבן יד', None), ('a wooden instrument', 'בכלי עץ', None), ('whereby he may die', 'אשר ימות בה', None), ('whereby he may die (masc.)', 'אשר ימות בו', None), ('he is a murderer', 'רצח הוא', None), ('the murderer shall surely die', 'מות יומת הרצח', None), ('shall surely die', 'מות יומת', T), ('the smiter shall surely die', 'מות יומת המכה', None), ('the avenger of blood shall put to death', 'גאל הדם ימית', None), ('when he meets him', 'בפגעו בו', None), ('in hatred', 'בשנאה', None), ('in lying-in-wait', 'בצדיה', None), ('in enmity', 'באיבה', None), ('the smiter (participle)', 'המכה', T), ('struck him', 'הכהו', None), ('and he died (וימת)', 'וימת', ('Num',)),
                      ('suddenly', 'בפתע', None), ('without enmity', 'בלא איבה', None), ('without lying-in-wait', 'בלא צדיה', None), ('without seeing', 'בלא ראות', None), ('and he dropped it on him', 'ויפל עליו', None), ('the congregation shall judge', 'ושפטו העדה', None), ('these judgments', 'המשפטים האלה', None), ('the congregation shall deliver', 'והצילו העדה', None), ('until the death of the high priest', 'עד מות הכהן הגדל', None), ('the high priest (plene)', 'הכהן הגדול', None), ('the high priest (defective)', 'הכהן הגדל', None), ('who was anointed with the holy oil', 'אשר משח אתו בשמן הקדש', None), ('going out goes out', 'יצא יצא', None), ('the border of his city of refuge', 'גבול עיר מקלטו', None), ('he has no blood', 'אין לו דם', None), ('he has no bloods (22:1)', 'אין לו דמים', None), ('the land of his possession', 'ארץ אחזתו', None),
                      ('a statute of judgment', 'לחקת משפט', None), ('for your generations in all your dwellings', 'לדרתיכם בכל מושבתיכם', None), ('by the mouth of witnesses', 'לפי עדים', None), ('one witness', 'עד אחד', None), ('shall not testify', 'לא יענה', None), ('you shall not take ransom', 'ולא תקחו כפר', None), ('ransom (כפר)', 'כפר', T), ('wicked to die', 'רשע למות', None), ('you shall not pollute', 'ולא תחניפו', None), ('and for the land no atonement', 'ולארץ לא יכפר', None), ('except by the blood of him who shed it', 'כי אם בדם שפכו', None), ('you shall not defile the land', 'ולא תטמא את הארץ', None), ('in whose midst I dwell', 'אשר אני שכן בתוכה', None), ('I dwell in the midst', 'שכן בתוך', None), ('for I the LORD dwell', 'כי אני יהוה שכן', None), ('two or three witnesses', 'שנים עדים או שלשה', None), ('two witnesses or three', 'שני עדים או שלשה', None),
                      ('and the LORD spoke to Moses in the plains of Moab', 'וידבר יהוה אל משה בערבת מואב', None), ('in the plains of Moab by the Jordan at Jericho', 'בערבת מואב על ירדן ירחו', None), ('and the LORD spoke to Moses saying (Num 35)', 'וידבר יהוה אל משה לאמר', ('Num',)), ('as the LORD commanded Moses (the receipt, Num)', 'כאשר צוה יהוה את משה', ('Num',)), ('by the hand of Moses', 'ביד משה', None), ('Bezer', 'בצר', None), ('Ramoth', 'ראמת', None), ('Golan', 'גולן', None), ('Kedesh', 'קדש', None), ('Shechem', 'שכם', None), ('Hebron', 'חברון', None), ('Kiriath-arba', 'קרית ארבע', None), ('the Levites (הלוים)', 'הלוים', ('Num',)), ('the Levites, to the Levites (ללוים)', 'ללוים', None), ('Eleazar the priest', 'אלעזר הכהן', None), ('Aaron died', 'וימת אהרן', None), ('Eleazar died', 'ואלעזר בן אהרן מת', None)]:
    s = seats(ph, bk); print('  %-60s %d %s' % (label, len(s), s[:30]))
print('\n==== (D) THE CASE TOKENS AND THE VERBS of 35:9-34 ====')
for v in range(9, 35):
    ws = _V[('Num', 35, v)]; ms = _M[('Num', 35, v)]
    ct = [(i, w) for i, w in enumerate(ws) if w in ('כי', 'ואם', 'אם', 'או', 'וכי')]
    vb = [(i, w, m) for i, (w, m) in enumerate(zip(ws, ms)) if 'V' in m and not m.startswith('HN')]
    print('  35:%-2d case tokens %s' % (v, ct))
    print('        verbs %s' % vb)
print('\n==== (E) THE KIN VERSES (the words) ====')
for k in [('Exod', 21, 12), ('Exod', 21, 13), ('Exod', 21, 14), ('Exod', 22, 1), ('Exod', 22, 2), ('Exod', 21, 30), ('Exod', 30, 12), ('Lev', 24, 17), ('Lev', 24, 21), ('Lev', 21, 10), ('Lev', 25, 34), ('Lev', 3, 17), ('Lev', 18, 25), ('Lev', 18, 28), ('Num', 5, 3), ('Num', 6, 9), ('Num', 15, 27), ('Num', 15, 28), ('Num', 20, 26), ('Num', 20, 28), ('Num', 26, 54), ('Num', 26, 62), ('Num', 27, 11), ('Num', 33, 51), ('Num', 33, 54), ('Num', 34, 2), ('Num', 34, 17), ('Num', 2, 3), ('Num', 2, 10), ('Num', 2, 18), ('Num', 2, 25), ('Gen', 9, 6), ('Gen', 3, 15), ('Gen', 19, 20), ('Deut', 4, 41), ('Deut', 4, 42), ('Deut', 4, 43), ('Deut', 19, 2), ('Deut', 19, 3), ('Deut', 19, 4), ('Deut', 19, 5), ('Deut', 19, 6), ('Deut', 19, 11), ('Deut', 19, 12), ('Deut', 17, 6), ('Deut', 19, 15), ('Deut', 21, 1), ('Deut', 21, 2), ('Deut', 21, 8), ('Josh', 20, 2), ('Josh', 20, 3), ('Josh', 20, 6), ('Josh', 20, 7), ('Josh', 20, 8), ('Josh', 21, 2), ('Josh', 21, 3), ('Josh', 21, 41), ('Josh', 21, 42), ('Josh', 24, 33), ('Ps', 106, 38), ('1Chr', 6, 42), ('2Sam', 14, 11), ('Num', 36, 1), ('Num', 36, 13)]:
    print('  %s %d:%d %s' % (k[0], k[1], k[2], ' '.join(_V[k])))
print('\n==== THE MURDER-ROOT (7523) and THE REFUGE-WORD (4733), THE AVENGER (1350), THE RANSOM (3724), THE POLLUTE-ROOT (2610), THE WITNESS (5707) by lemma ====')
for lm, label in (('7523', 'murder-root'), ('4733', 'refuge'), ('1350', 'avenger/redeemer'), ('3724', 'ransom'), ('2610', 'pollute'), ('5707', 'witness'), ('4054', 'pasture-land'), ('7684', 'unwittingly'), ('342', 'enmity'), ('6660', 'lying-in-wait'), ('1234', 'iron'), ('5307', 'fall/drop')):
    s = lemma_seats(lm); sT = lemma_seats(lm, T); s35 = [x for x in s if x.startswith('Num 35:')]
    print('  %-20s lemma %-5s Bible verses %3d, Torah %2d, Num 35 %2d: Torah %s' % (label, lm, len(s), len(sT), len(s35), sT[:30]))
print('  the tokens of lemma 7523 in Num 35 with morph: %s' % [(v, w, m) for v in range(9, 35) for w, l, m in zip(_V[('Num', 35, v)], _L[('Num', 35, v)], _M[('Num', 35, v)]) if l == '7523'])
print('  the lemma of "מכה" at 35:11 / 35:15 / 35:16 / 35:21 / 35:24 / 35:30: %s' % [(v, [(w, l, m) for w, l, m in zip(_V[('Num', 35, v)], _L[('Num', 35, v)], _M[('Num', 35, v)]) if w in ('מכה', 'המכה', 'הכהו', 'הכה')]) for v in (11, 15, 16, 17, 18, 21, 24, 30)])
print('\n==== THE FRAMES / NARRATIVE VERBS of 35 ====')
for v in range(1, 35):
    vs = [(w, m) for w, m in zip(_V[('Num', 35, v)], _M[('Num', 35, v)]) if 'Vqw' in m or 'Vpw' in m or 'Vhw' in m]
    if vs: print('  35:%d wayyiqtol %s' % (v, vs))
print('  35:1 / 35:9 / 36:1 frames: %s | %s | %s' % (' '.join(_V[('Num', 35, 1)]), ' '.join(_V[('Num', 35, 9)]), ' '.join(_V[('Num', 36, 1)])))
