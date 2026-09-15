import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 12b: THE MEASUREMENT PASS ON THE RUNNER'S PROBE TOKENS AND PHRASE SEATS before cold_run_gad_reuben.py is typed (7b's lesson:
# the hand's forms fall; type every token and every seat list from this print). Also the callees' values the runner will assert.
import sys, io, contextlib, re, sqlite3, collections
sys.path.insert(0, (_ROOT + '/World/step9'))
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import cold_run_vows as VW, cold_run_shelach as SL, cold_run_chukat as CK, cold_run_second_census as C2, cold_run_bamidbar as BM
db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))
def strip(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
_V = collections.OrderedDict(); _L = collections.OrderedDict()
for b, c, v, he, lm in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append(lm.split('/')[-1].split(' ')[0] if lm else '')
def seats(phrase, books=None):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def rx(pattern, books=None):
    r = re.compile(pattern)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and r.search(' ' + ' '.join(ws) + ' ')]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
print('==== THE WORDS OF 32:1-42 (plain) ====')
for v in range(1, 43):
    print('%2d: %s' % (v, ' '.join(_V[('Num', 32, v)])))
print('\n==== THE PARSER (numbers | ordinals) at every number verse of 32 and the retellings ====')
for k in [('Num', 32, v) for v in range(1, 43)] + [('Josh', 4, 13), ('1Chr', 5, 18), ('1Chr', 2, 22), ('1Chr', 2, 21), ('1Chr', 2, 23), ('1Kgs', 4, 13), ('Josh', 13, 30), ('Deut', 3, 4), ('Deut', 3, 14), ('Judg', 10, 4), ('Deut', 2, 14), ('Num', 14, 29), ('Num', 26, 7), ('Num', 26, 18), ('Num', 26, 34), ('Josh', 7, 5)]:
    vw = CS.verse_words(*k); n = CS.ink_numbers(vw); o = CS.ink_ordinals(vw)
    if n or o or k[0] != 'Num' or k[1] != 32: print('  %s %d:%d %s %s   %s' % (k[0], k[1], k[2], n, o, ' '.join(_V[k])[:140] if k[0] != 'Num' or k[1] != 32 else ''))
print('\n==== THE PHRASE SEATS (the whole DB unless the Torah is named) ====')
for label, ph, bk in [('the sons of Gad and the sons of Reuben', 'בני גד ובני ראובן', None), ('the sons of Reuben and the sons of Gad', 'בני ראובן ובני גד', None), ('much cattle', 'מקנה רב', None), ('a place for cattle', 'מקום מקנה', None),
                      ('the land of Jazer', 'ארץ יעזר', None), ('the land of Gilead', 'ארץ גלעד', None), ('the land of Gilead (with article)', 'ארץ הגלעד', None), ('to Moses and to Eleazar the priest and to the princes', 'אל משה ואל אלעזר הכהן ואל נשיאי', None),
                      ('before Moses and before Eleazar the priest and before the princes', 'לפני משה ולפני אלעזר הכהן ולפני הנשיאם', None), ('for a possession (laachuzza)', 'לאחזה', None), ('the possession of our inheritance', 'אחזת נחלתנו', None), ('a possession of an inheritance', 'אחזת נחלה', None),
                      ('shall your brothers go to war', 'האחיכם יבאו למלחמה', None), ('why do you discourage', 'ולמה תנואון', None), ('Kadesh-barnea (Num)', 'קדש ברנע', ('Num',)), ('Kadesh-barnea (all)', 'קדש ברנע', None), ('the valley of Eshcol', 'נחל אשכול', None),
                      ('the anger of the LORD burned (that day)', 'ויחר אף יהוה ביום ההוא', None), ('the anger of the LORD burned against Israel', 'ויחר אף יהוה בישראל', None), ('and he swore saying', 'וישבע לאמר', None), ('from twenty years old and upward', 'מבן עשרים שנה ומעלה', None),
                      ('which I swore to Abraham, to Isaac and to Jacob', 'אשר נשבעתי לאברהם ליצחק וליעקב', None), ('followed Me fully', 'מלאו אחרי', None), ('followed the LORD fully', 'מלאו אחרי יהוה', None), ('the Kenizzite', 'הקנזי', None), ('son of Kenaz', 'בן קנז', None),
                      ('forty years (Num 32)', 'ארבעים שנה', ('Num',)), ('until all the generation was consumed', 'עד תם כל הדור', None), ('did evil in the eyes of the LORD (the formula)', 'הרע בעיני יהוה', None), ('a brood of', 'תרבות', None), ('sinful men', 'אנשים חטאים', None),
                      ('to add', 'לספות', None), ('the fierce anger of the LORD', 'חרון אף יהוה', None), ('folds for sheep', 'גדרת צאן', None), ('cities for our little ones', 'וערים לטפנו', None), ('cities for your little ones', 'ערים לטפכם', None),
                      ('we will not return to our houses', 'לא נשוב אל בתינו', None), ('until the LORD gives rest', 'עד אשר יניח יהוה', None), ('before the LORD (Num 32)', 'לפני יהוה', ('Num',)), ('before the LORD for the war', 'לפני יהוה למלחמה', None),
                      ('the land is subdued before the LORD', 'ונכבשה הארץ לפני יהוה', None), ('the land is subdued before you', 'ונכבשה הארץ לפניכם', None), ('clear before the LORD and before Israel', 'נקיים מיהוה ומישראל', None), ('clear from the LORD', 'נקי מיהוה', None),
                      ('your sin which will find you', 'חטאתכם אשר תמצא אתכם', None), ('God has found out the iniquity of your servants', 'מצא את עון עבדיך', None), ('that which has gone out of your mouth you shall do', 'והיצא מפיכם תעשו', None), ('all that goes out of his mouth he shall do', 'ככל היצא מפיו יעשה', None),
                      ('your servants will do as my lord commands', 'עבדיך יעשו כאשר אדני מצוה', None), ('my lord (Num)', 'אדני', ('Num',)), ('Eleazar the priest and Joshua son of Nun (Num 32:28 form)', 'אלעזר הכהן ואת יהושע בן נון ואת ראשי אבות המטות', None),
                      ('Eleazar the priest and Joshua son of Nun (Josh form)', 'אלעזר הכהן ויהושע בן נון וראשי אבות המטות', None), ('they shall take possessions among you', 'ונאחזו בתככם', None), ('and Hamor: take possessions in it', 'והאחזו בה', None), ('we (short form)', 'נחנו', None),
                      ('the kingdom of Sihon', 'ממלכת סיחן', None), ('the kingdom of Og', 'ממלכת עוג', None), ('half the tribe of Manasseh (regex)', None, None), ('their names being changed', 'מוסבת שם', None), ('Dibon Gad', 'דיבן גד', None),
                      ('the sons of Machir son of Manasseh', 'בני מכיר בן מנשה', None), ('Machir son of Manasseh', 'מכיר בן מנשה', None), ('Havvoth-jair', 'חות יאיר', None), ('Jair son of Manasseh', 'יאיר בן מנשה', None), ('its daughters (Num)', 'בנתיה', ('Num',)),
                      ('Nobah', 'נבח', None), ('Jogbehah', 'יגבהה', None), ('Kenath', 'קנת', None), ('went and took (Num 32)', 'וילך וילכד', None), ('the Amorite who was in it', 'האמרי אשר בה', None), ('to see the land', 'לראות את הארץ', None), ('to spy out (Deut 1:22)', 'ויחפרו', None), ('to scout (Deut 1:24)', 'וירגלו', None), ('to tour (Num 13)', 'לתור', ('Num',)),
                      ('he made them wander', 'ויניעם', None), ('you will destroy all this people', 'ושחתם לכל העם הזה', None)]:
    if ph is None:
        s = rx(r' חצי (ה)?שבט (ה)?מנשה ')
    else:
        s = seats(ph, bk)
    print('  %-62s %d %s' % (label, len(s), s[:20]))
print('\n---- the hinder-root token set (the reading\'s: הניא יניא תנואון ויניאו + the nouns) ----')
for t in ('הניא', 'יניא', 'תנואון', 'ויניאו', 'תנואתי', 'תנואתו'):
    print('  %-10s %s' % (t, tok(t)))
print('---- the arm-root tokens in Num 32 (regex on חלץ) ----')
for v in range(1, 43):
    hits = [w for w in _V[('Num', 32, v)] if re.search(r'חל[וּ]?צ', w)]
    if hits: print('  32:%d %s' % (v, hits))
print('  the arm-root tokens in Josh 1:14 / 4:12 / 4:13 / Deut 3:18: %s' % [(k, [w for w in _V[k] if re.search(r'חל[ו]?צ|חמש', w)]) for k in (('Josh', 1, 14), ('Josh', 4, 12), ('Josh', 4, 13), ('Deut', 3, 18))])
print('---- the city names: 32:3 the nine; 32:34-38 Gad\'s and Reuben\'s (the words) ----')
for v in (3, 34, 35, 36, 37, 38): print('  32:%d %s' % (v, _V[('Num', 32, v)]))
print('  Josh 13:17 %s' % ' '.join(_V[('Josh', 13, 17)]))
print('  Josh 13:26 %s' % ' '.join(_V[('Josh', 13, 26)]))
print('  Josh 13:20 %s' % ' '.join(_V[('Josh', 13, 20)]))
print('  Num 33:45 %s | 33:46 %s' % (' '.join(_V[('Num', 33, 45)]), ' '.join(_V[('Num', 33, 46)])))
print('  1Chr 2:21 %s' % ' '.join(_V[('1Chr', 2, 21)]))
print('  1Chr 2:22 %s' % ' '.join(_V[('1Chr', 2, 22)]))
print('  1Chr 2:23 %s' % ' '.join(_V[('1Chr', 2, 23)]))
print('  1Chr 5:18 %s' % ' '.join(_V[('1Chr', 5, 18)]))
print('  Judg 8:11 %s' % ' '.join(_V[('Judg', 8, 11)]))
print('  Josh 14:1 %s' % ' '.join(_V[('Josh', 14, 1)]))
print('  Josh 21:1 %s' % ' '.join(_V[('Josh', 21, 1)]))
print('  Josh 22:4 %s' % ' '.join(_V[('Josh', 22, 4)]))
print('  Josh 22:9 %s' % ' '.join(_V[('Josh', 22, 9)]))
print('  Gen 50:23 %s' % ' '.join(_V[('Gen', 50, 23)]))
print('  Num 26:29 %s' % ' '.join(_V[('Num', 26, 29)]))
print('  Num 30:3 %s' % ' '.join(_V[('Num', 30, 3)]))
print('  Gen 44:16 %s' % ' '.join(_V[('Gen', 44, 16)]))
print('  Num 14:24 %s' % ' '.join(_V[('Num', 14, 24)]))
print('  Num 14:29 %s' % ' '.join(_V[('Num', 14, 29)]))
print('  Deut 2:14 %s' % ' '.join(_V[('Deut', 2, 14)]))
print('  Num 21:32 %s' % ' '.join(_V[('Num', 21, 32)]))
print('  Gen 47:11 %s' % ' '.join(_V[('Gen', 47, 11)]))
print('---- the lemma sequence of the utterance phrase (32:24 vs 30:3) ----')
for k in (('Num', 32, 24), ('Num', 30, 3)):
    ws = _V[k]; ls = _L[k]
    print('  %s: %s' % (k, list(zip(ws, ls))))
print('  the seats of the lemma pair 3318 (go out) + 6310 (mouth) adjacent: %s' % ['%s %d:%d' % k for k, ls in _L.items() if any(ls[i] == '3318' and ls[i + 1] == '6310' for i in range(len(ls) - 1))])
print('\n==== THE CALLEES (the values the runner asserts) ====')
def sh(label, f):
    try: print('  %s -> %r' % (label, f()))
    except BaseException as e: print('  %s RAISED %s %s' % (label, type(e).__name__, str(e)[:120]))
sh('VW all_that_proceeds', lambda: VW.the_man({'ask': 'all_that_proceeds'}, VW.DATA)[:2])
sh('VW frame', lambda: VW.the_man({'ask': 'frame'}, VW.DATA)[:2])
sh('VW DATA vow_support_base', lambda: VW.DATA['vow_support_base'])
sh('SL set', lambda: SL.decree({'ask': 'set'}, SL.DATA)[:2])
sh('SL exceptions', lambda: SL.decree({'ask': 'exceptions'}, SL.DATA)[:2])
sh('SL due', lambda: SL.decree({'ask': 'due'}, SL.DATA)[:2])
sh('SL count_from', lambda: SL.decree({'ask': 'count_from'}, SL.DATA)[:2])
sh('SL day_for_year', lambda: SL.decree({'ask': 'day_for_year'}, SL.DATA)[:2])
sh('SL caleb_entitlement', lambda: SL.decree({'ask': 'caleb_entitlement'}, SL.DATA)[:2])
sh('SL deaths_ceased', lambda: SL.decree({'ask': 'deaths_ceased'}, SL.DATA)[:2])
sh('SL pardon', lambda: SL.decree({'ask': 'pardon'}, SL.DATA)[:2])
sh('SL set_edges', lambda: SL.decree({'ask': 'set_edges'}, SL.DATA)[:2])
sh('SL joshua_childless', lambda: SL.decree({'ask': 'joshua_childless'}, SL.DATA)[:2])
sh('SL spies joshua_name', lambda: SL.spies({'ask': 'joshua_name'}, SL.DATA)[:2])
sh('SL spies joshua_caleb_equal', lambda: SL.spies({'ask': 'joshua_caleb_equal'}, SL.DATA)[:2])
sh('SL spies send_for_yourself', lambda: SL.spies({'ask': 'send_for_yourself'}, SL.DATA)[:2])
sh('SL spies eshcol', lambda: SL.spies({'ask': 'eshcol'}, SL.DATA)[:2])
sh('SL spies hebron_visitor', lambda: SL.spies({'ask': 'hebron_visitor'}, SL.DATA)[:2])
sh('SL FORTY_YEARS / DUE_38', lambda: (SL.FORTY_YEARS, SL.DUE_38))
sh('SL DATA count_from value / deaths_ceased value / spies_share', lambda: (SL.DATA['count_from']['value'], SL.DATA['deaths_ceased']['value'], SL.DATA['spies_share']['value']))
sh('CK land_east', lambda: CK.well_and_kings({'ask': 'land_east'}, CK.DATA)[:2])
sh('CK deut3_delta', lambda: CK.well_and_kings({'ask': 'deut3_delta'}, CK.DATA)[:2])
sh('CK og_lore', lambda: CK.well_and_kings({'ask': 'og_lore'}, CK.DATA)[:2])
sh('CK sihon_purified', lambda: CK.well_and_kings({'ask': 'sihon_purified'}, CK.DATA)[:2])
sh('CK spy_verb', lambda: CK.well_and_kings({'ask': 'spy_verb'}, CK.DATA)[:2])
sh('CK DATA og_lore value / sihon_purified value', lambda: (CK.DATA['og_lore']['value'], CK.DATA['sihon_purified']['value']))
sh('C2 total', lambda: C2.the_roll({'ask': 'total'}, C2.DATA)[:2])
sh('C2 by_lot', lambda: C2.the_land({'ask': 'by_lot'}, C2.DATA)[:2])
sh('C2 thirteen_tribes', lambda: C2.the_land({'ask': 'thirteen_tribes'}, C2.DATA)[:2])
sh('C2 ten_parts', lambda: C2.the_land({'ask': 'ten_parts'}, C2.DATA)[:2])
sh('C2 morasha', lambda: C2.the_land({'ask': 'morasha'}, C2.DATA)[:2])
sh('C2 except_caleb_joshua', lambda: C2.the_rolls({'ask': 'except_caleb_joshua'}, C2.DATA)[:2])
sh('C2 C26 reuben gad manasseh', lambda: (C2.C26['reuben'], C2.C26['gad'], C2.C26['manasseh']))
sh('C2 FAMILIES manasseh', lambda: C2.FAMILIES['manasseh'])
sh('C2 DATA thirteen_tribes value / division_by value', lambda: (C2.DATA['thirteen_tribes']['value'], C2.DATA['division_by']['value']))
sh('BM threshold', lambda: BM.census({'ask': 'threshold'}, BM.DATA)[:2])
sh('BM orders', lambda: BM.census({'ask': 'orders'}, BM.DATA)[:2])
sh('BM TRIBES index of gad / reuben / manasseh', lambda: (BM.TRIBES.index('gad'), BM.TRIBES.index('reuben'), BM.TRIBES.index('manasseh')))
