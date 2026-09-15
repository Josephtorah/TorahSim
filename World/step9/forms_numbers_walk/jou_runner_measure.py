import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 13b: THE MEASUREMENT PASS ON THE RUNNER'S PROBE TOKENS, PHRASE SEATS AND THE STATIONS before cold_run_journeys.py is typed
# (7b's lesson: the hand's forms fall; type every token, every seat list and every slice from this print). Also the callees' values the runner asserts.
import sys, io, contextlib, re, sqlite3, collections
sys.path.insert(0, (_ROOT + '/World/step9'))
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import cold_run_exodus_story as ES, cold_run_pesach as PS, cold_run_beha as BH, cold_run_shelach as SL, cold_run_chukat as CK, cold_run_balak as BK
    import cold_run_second_census as C2, cold_run_gad_reuben as GR, cold_run_erection as ER, cold_run_holiness as HL, cold_run_zelophehad as ZL
db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))
def strip(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
_V = collections.OrderedDict(); _L = collections.OrderedDict(); _M = collections.OrderedDict()
for b, c, v, he, lm, mo in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he)); _L.setdefault((b, c, v), []).append(lm.split('/')[-1].split(' ')[0] if lm else ''); _M.setdefault((b, c, v), []).append(mo or '')
def seats(phrase, books=None):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def rx(pattern, books=None):
    r = re.compile(pattern)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and r.search(' ' + ' '.join(ws) + ' ')]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
print('==== THE WORDS OF 33:1-56 (plain, with indices) ====')
for v in range(1, 57):
    print('%2d: %s' % (v, ' '.join('%d:%s' % (i, w) for i, w in enumerate(_V[('Num', 33, v)]))))
print('\n==== THE PARSER at every number verse of 33 and the retellings ====')
for k in [('Num', 33, v) for v in range(1, 57)] + [('Exod', 7, 7), ('Deut', 34, 7), ('Deut', 1, 3), ('Exod', 12, 37), ('Exod', 12, 41), ('Exod', 16, 1), ('Exod', 19, 1), ('Exod', 15, 22), ('Exod', 15, 27), ('Num', 10, 11), ('Num', 20, 29), ('Deut', 2, 14), ('Josh', 5, 10), ('1Kgs', 6, 1), ('Num', 14, 33)]:
    vw = CS.verse_words(*k); n = CS.ink_numbers(vw); o = CS.ink_ordinals(vw)
    if n or o or k[0] != 'Num' or k[1] != 33: print('  %s %d:%d %s %s   %s' % (k[0], k[1], k[2], n, o, ' '.join(_V[k])[:120] if k[0] != 'Num' or k[1] != 33 else ''))
print('\n==== THE STATIONS — the verbs\' after-tokens by verse (ויסעו "and they journeyed" FROM; ויחנו "and they camped" AT) ====')
J = {}; C = {}
for v in range(1, 57):
    ws = _V[('Num', 33, v)]
    for i, w in enumerate(ws):
        if w == 'ויסעו': J[v] = ws[i + 1:i + 4]
        if w == 'ויחנו': C[v] = ws[i + 1:i + 5]
print('  journeyed verses %d: %s' % (len(J), sorted(J)))
print('  camped verses %d: %s' % (len(C), sorted(C)))
for v in sorted(set(J) | set(C)):
    print('  33:%-2d from %-28s at %s' % (v, ' '.join(J.get(v, [])), ' '.join(C.get(v, []))))
print('  the Np (proper-name) tokens per verse 33:5-49 with their lemma:')
for v in range(5, 50):
    print('  33:%-2d %s' % (v, [(w, l) for w, l, m in zip(_V[('Num', 33, v)], _L[('Num', 33, v)], _M[('Num', 33, v)]) if 'Np' in m]))
print('\n==== THE PHRASE SEATS (the whole DB unless the Torah is named) ====')
for label, ph, bk in [('these are the journeys (33:1 head)', 'אלה מסעי', None), ('these are the journeys of the children of Israel', 'אלה מסעי בני ישראל', None), ('by their hosts', 'לצבאתם', None), ('by the hand of Moses and Aaron', 'ביד משה ואהרן', None),
                      ('and Moses wrote', 'ויכתב משה', None), ('by the mouth of the LORD', 'על פי יהוה', None), ('by the mouth of the LORD (Torah)', 'על פי יהוה', T), ('by the mouth of the LORD (Num)', 'על פי יהוה', ('Num',)),
                      ('their goings out', 'מוצאיהם', None), ('their journeys', 'מסעיהם', None), ('their journeys (with lamed)', 'למסעיהם', None), ('on the fifteenth day of the first month', 'בחמשה עשר יום לחדש הראשון', None), ('on the fifteenth day of this month', 'בחמשה עשר יום לחדש הזה', None),
                      ('on the morrow of the Passover', 'ממחרת הפסח', None), ('with a high hand', 'ביד רמה', None), ('in the sight of all Egypt', 'לעיני כל מצרים', None), ('was burying', 'מקברים', None), ('every firstborn', 'כל בכור', None), ('executed judgments (perfect)', 'עשה יהוה שפטים', None), ('I will execute judgments', 'אעשה שפטים', None),
                      ('from Rameses', 'מרעמסס', None), ('a way of three days', 'דרך שלשת ימים', None), ('twelve springs of water', 'שתים עשרה עינת מים', None), ('seventy palm trees', 'ושבעים תמרים', None), ('the wilderness of Etham', 'מדבר אתם', None), ('the wilderness of Shur', 'מדבר שור', None),
                      ('the Red Sea (Torah)', 'ים סוף', T), ('in the wilderness of Sinai (Torah)', 'במדבר סיני', T), ('Kibroth-hattaavah', 'קברת התאוה', None), ('Rithmah', 'ברתמה', None), ('that is Kadesh', 'הוא קדש', None), ('in the edge of the land of Edom', 'בקצה ארץ אדום', None), ('on the border of the land of Edom', 'גבול ארץ אדום', None),
                      ('Mount Hor (hor hahar)', 'הר ההר', None), ('in the fortieth year', 'בשנת הארבעים', None), ('of the going out of the children of Israel from the land of Egypt', 'לצאת בני ישראל מארץ מצרים', None), ('in the fifth month', 'בחדש החמישי', None), ('at his death', 'במתו', None),
                      ('the Canaanite king of Arad', 'הכנעני מלך ערד', None), ('and the Canaanite heard', 'וישמע הכנעני', None), ('Dibon Gad', 'דיבן גד', None), ('the mountains of Abarim', 'בהרי העברים', None), ('the mountain of Abarim', 'הר העברים', None), ('the plains of Moab (Torah)', 'ערבת מואב', T), ('by the Jordan at Jericho', 'ירדן ירחו', None),
                      ('Beth-jeshimoth', 'הישמת', None), ('Abel-shittim', 'השטים', None), ('in the plains of Moab by the Jordan at Jericho, saying (the frame)', 'בערבת מואב על ירדן ירחו לאמר', None), ('when you pass over the Jordan', 'עברים את הירדן', None), ('into the land of Canaan (33:51)', 'אל ארץ כנען', None),
                      ('drive out all the inhabitants of the land', 'והורשתם את כל ישבי הארץ', None), ('the inhabitants of the land (Torah)', 'ישבי הארץ', T), ('their figured stones', 'משכיתם', None), ('figured stone (Lev 26:1)', 'משכית', None), ('their molten images', 'צלמי מסכתם', None), ('molten (Torah token)', 'מסכה', T), ('their high places', 'במתם', None), ('your high places', 'במתיכם', None), ('demolish', 'תשמידו', None), ('I will destroy (Lev 26:30)', 'והשמדתי', None),
                      ('and you shall dispossess the land and dwell in it', 'והורשתם את הארץ וישבתם בה', None), ('to you I have given the land', 'לכם נתתי את הארץ', None), ('by lot (Torah)', 'בגורל', T), ('to the many you shall give more', 'לרב תרבו', None), ('to whom the lot goes out', 'אל אשר יצא לו שמה הגורל', None), ('by the tribes of your fathers', 'למטות אבתיכם', None),
                      ('thorns in your eyes', 'לשכים בעיניכם', None), ('pricks in your sides', 'ולצנינם בצדיכם', None), ('pricks in your eyes (Josh 23:13)', 'ולצננים בעיניכם', None), ('for sides (Judg 2:3)', 'לצדים', None), ('leave over (33:55)', 'תותירו', None), ('and they shall harass you', 'וצררו אתכם', None), ('as I thought', 'כאשר דמיתי', None),
                      ('and the LORD spoke to Moses in the plains of Moab', 'וידבר יהוה אל משה בערבת מואב', None), ('the LORD spoke to Moses (33)', 'וידבר יהוה אל משה', ('Num',))]:
    s = seats(ph, bk); print('  %-70s %d %s' % (label, len(s), s[:24]))
print('  33:52 tokens: %s' % _V[('Num', 33, 52)]); print('  Lev 26:1: %s' % ' '.join(_V[('Lev', 26, 1)])); print('  Lev 26:30: %s' % ' '.join(_V[('Lev', 26, 30)])); print('  Exod 34:17: %s' % ' '.join(_V[('Exod', 34, 17)])); print('  Lev 19:4: %s' % ' '.join(_V[('Lev', 19, 4)]))
print('  Josh 23:13: %s' % ' '.join(_V[('Josh', 23, 13)])); print('  Judg 2:3: %s' % ' '.join(_V[('Judg', 2, 3)])); print('  Isa 14:24: %s' % ' '.join(_V[('Isa', 14, 24)])); print('  Josh 5:11: %s' % ' '.join(_V[('Josh', 5, 11)])); print('  Exod 12:12: %s' % ' '.join(_V[('Exod', 12, 12)]))
print('  Exod 13:20: %s' % ' '.join(_V[('Exod', 13, 20)])); print('  Num 33:6: %s' % ' '.join(_V[('Num', 33, 6)])); print('  Exod 15:27: %s' % ' '.join(_V[('Exod', 15, 27)])); print('  Num 33:9: %s' % ' '.join(_V[('Num', 33, 9)])); print('  Num 26:54: %s' % ' '.join(_V[('Num', 26, 54)])); print('  Num 26:55: %s' % ' '.join(_V[('Num', 26, 55)]))
print('  Deut 10:6: %s' % ' '.join(_V[('Deut', 10, 6)])); print('  Deut 10:7: %s' % ' '.join(_V[('Deut', 10, 7)])); print('  Num 10:28: %s' % ' '.join(_V[('Num', 10, 28)])); print('  Ps 77:21: %s' % ' '.join(_V[('Ps', 77, 21)])); print('  1Kgs 6:1: %s' % ' '.join(_V[('1Kgs', 6, 1)])); print('  Exod 19:1: %s' % ' '.join(_V[('Exod', 19, 1)]))
print('  the morph of 33:54 verbs: %s' % [(w, m) for w, m in zip(_V[('Num', 33, 54)], _M[('Num', 33, 54)]) if 'V' in m])
print('  the "these" headings (verse-initial אלה, Torah): %d' % len([k for k, ws in _V.items() if k[0] in T and ws and ws[0] == 'אלה']))
print('  the judgment-noun lemma 8201 seats: %s' % ['%s %d:%d' % k for k, ls in _L.items() if '8201' in ls][:30])
print('  the figured-stone lemma 4906 seats: %s' % ['%s %d:%d' % k for k, ls in _L.items() if '4906' in ls])
print('  the high-place lemma 1116 seats (Torah): %s' % ['%s %d:%d' % k for k, ls in _L.items() if k[0] in T and '1116' in ls])
print('  the molten lemma 4541 seats (Torah): %s' % ['%s %d:%d' % k for k, ls in _L.items() if k[0] in T and '4541' in ls])
print('  the Passover lemma 6453 seats (Num 33 + Josh 5): %s' % ['%s %d:%d' % k for k, ls in _L.items() if '6453' in ls and k[:2] in (('Num', 33), ('Josh', 5))])
print('\n==== THE CALLEES (the values the runner asserts) ====')
def sh(label, f):
    try: print('  %s -> %r' % (label, f()))
    except BaseException as e: print('  %s RAISED %s %s' % (label, type(e).__name__, str(e)[:120]))
sh('ES stations', lambda: (ES.night('stations')['v'], ES.night('stations')['fx']))
sh('ES by_day', lambda: (ES.night('by_day')['v'], ES.night('by_day')['fx']))
sh('ES plagues ten / removed', lambda: (ES.plagues('ten')['v'], ES.plagues('removed')['v'], ES.plagues('removed')['fx']))
sh('ES marah three_days / sinai new_moon / manna forty_years', lambda: (ES.marah('three_days')['v'], ES.sinai('new_moon')['v'], ES.manna('forty_years')['v']))
sh('ES PLAGUES / REMOVED keys', lambda: (ES.PLAGUES, sorted(ES.REMOVED)))
sh('PS firstborn human', lambda: PS.firstborn({'kind': 'human'}, PS.DATA)[:2])
sh('BH graves', lambda: BH.taberah_and_quail({'ask': 'graves'}, BH.DATA)[:2])
sh('BH day_stack / year_turns', lambda: (BH.march({'ask': 'day_stack'}, BH.DATA)[:2], BH.march({'ask': 'year_turns'}, BH.DATA)[:2]))
sh('SL high_hand_posture', lambda: SL.high_hand({'ask': 'high_hand_posture'}, SL.DATA)[:2])
sh('SL forty_days / count_from / deaths_ceased', lambda: (SL.spies({'ask': 'forty_days'}, SL.DATA)[0], SL.decree({'ask': 'count_from'}, SL.DATA)[0], SL.decree({'ask': 'deaths_ceased'}, SL.DATA)[0]))
sh('CK AARON_DATE / AARON_AGE / DAYS30 / D_AARON / D_HOR / D_ZIN / D_DEPART', lambda: (CK.AARON_DATE, CK.AARON_AGE, CK.DAYS30, CK.D_AARON, CK.D_HOR, CK.D_ZIN, CK.D_DEPART))
for q in ('death_dates', 'aaron_age', 'arad_heard', 'moserah', 'two_mount_hors', 'thirty_days', 'succession', 'seder_olam_walk'):
    sh('CK edom_and_hor %s' % q, lambda q=q: CK.edom_and_hor({'ask': q}, CK.DATA)[:2])
sh('CK meribah death_by_the_kiss', lambda: CK.meribah({'ask': 'death_by_the_kiss'}, CK.DATA)[:2])
sh('CK DATA moserah / arad_heard / death_by_the_kiss / miriam_death_day values', lambda: (CK.DATA['moserah']['value'], CK.DATA['arad_heard']['value'], CK.DATA['death_by_the_kiss']['value'], CK.DATA['miriam_death_day']['value']))
sh('BK last_camp / shittim_name', lambda: (BK.the_call({'ask': 'last_camp'}, BK.DATA)[:2], BK.peor({'ask': 'shittim_name'}, BK.DATA)[:2]))
sh('BK DATA shittim_name value', lambda: BK.DATA['shittim_name']['value'])
for q in ('by_lot', 'lots_mouth', 'by_number_of_names', 'land_divided_among', 'possession_before_assignment'):
    sh('C2 the_land %s' % q, lambda q=q: C2.the_land({'ask': q}, C2.DATA)[:2])
sh('C2 DATA division_by / land_divided_among', lambda: (C2.DATA['division_by']['value'], C2.the_land({'ask': 'land_divided_among'}, C2.DATA)[0][:40]))
sh('GR dibon_gad / not_by_lot / negative_arm_outcome', lambda: (GR.the_cities({'ask': 'dibon_gad'}, GR.DATA)[:2], GR.the_grant({'ask': 'not_by_lot'}, GR.DATA)[0][:60], GR.DATA['negative_arm_outcome']['value']))
sh('ER molten_two_seats / molten_calf / demolition_grows', lambda: (ER.covenant('molten_two_seats')['v'], ER.calf('molten_calf')['v'], ER.covenant('demolition_grows')['v'], ER.covenant('demolition_grows')['fx']))
sh('HL molten_warnings / idols_look', lambda: (HL.frame('molten_warnings')['v'], HL.frame('idols_look')['v']))
sh('ZL eretz_yisrael_status', lambda: ZL.DATA['eretz_yisrael_status']['value'])
sh('CS day_in (40,5,1) (40,11,1) (2,1,1) (2,2,20) (1,1,15) (1,2,16) and the era year of each', lambda: None)
w0 = CS.build_world() if hasattr(CS, 'build_world') else None
print('  CS has build_world:', w0 is not None, '; CS names with clock/day_in:', [n for n in dir(CS) if re.search(r'day_in|era|clock|calendar', n)][:12])
