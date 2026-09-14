#!/usr/bin/env python3
# THE NUMBERS WALK 11b: THE MEASUREMENT PASS ON THE RUNNER'S PROBE TOKENS AND PHRASE SEATS before cold_run_midian.py is typed (7b's lesson:
# the hand's forms fall; type every token and every seat list from this print). Also the callees' values the runner will assert.
import sys, io, contextlib, re, sqlite3, collections
sys.path.insert(0, '<repo-old>/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import cold_run_balak as BK, cold_run_beha as BH, cold_run_chukat as CK, cold_run_shemini as SH, cold_run_incense_shekel as IS, cold_run_bamidbar as BM
db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')
def strip(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
_V = collections.OrderedDict()
for b, c, v, he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _V.setdefault((b, c, v), []).append(strip(he))
def seats(phrase, books=None):
    p = phrase.split(); n = len(p)
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and any(ws[i:i + n] == p for i in range(len(ws) - n + 1))]
def tok(t, books=None):
    return ['%s %d:%d' % k for k, ws in _V.items() if (books is None or k[0] in books) and t in ws]
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
print('==== THE WORDS OF 31:1-54 (plain) ====')
for v in range(1, 55):
    print('%2d: %s' % (v, ' '.join(_V[('Num', 31, v)])))
print('\n==== THE PARSER (numbers | ordinals) at every number verse ====')
for v in range(1, 55):
    vw = CS.verse_words('Num', 31, v); n = CS.ink_numbers(vw); o = CS.ink_ordinals(vw)
    if n or o: print('  31:%d %s %s' % (v, n, o))
print('\n==== THE PHRASE SEATS (the whole DB unless the Torah is named) ====')
for label, ph, bk in [('the Midianites with the article', 'המדינים', None), ('avenge the vengeance', 'נקם נקמת', None), ('the vengeance of the LORD', 'נקמת יהוה', None),
                      ('afterward you shall be gathered', 'אחר תאסף', None), ('a thousand to a tribe', 'אלף למטה', None), ('the trumpets of the alarm', 'וחצצרות התרועה', None),
                      ('they warred', 'ויצבאו', None), ('as the LORD commanded Moses (Num 31)', 'כאשר צוה יהוה את משה', ('Num',)), ('they killed every male', 'ויהרגו כל זכר', None),
                      ('the kings of Midian', 'מלכי מדין', None), ('the five kings of Midian', 'חמשת מלכי מדין', None), ('Balaam son of Beor', 'בלעם בן בעור', None),
                      ('by the word of Balaam', 'בדבר בלעם', None), ('treachery against the LORD', 'מעל ביהוה', None), ('in the matter of Peor', 'דבר פעור', None),
                      ('and Moses was wroth', 'ויקצף משה', None), ('the officers of the host', 'פקודי החיל', None), ('lying with a male', 'למשכב זכר', None),
                      ('keep alive for yourselves', 'החיו לכם', None), ('outside the camp seven days', 'מחוץ למחנה שבעת ימים', None), ('on the third day and on the seventh day', 'ביום השלישי וביום השביעי', None),
                      ('you and your captives', 'אתם ושביכם', None), ('all work of goats', 'כל מעשה עזים', None), ('this is the statute of the Torah', 'זאת חקת התורה', None),
                      ('the water of sprinkling', 'במי נדה', None), ('pass through the fire', 'תעבירו באש', None), ('take the sum (singular)', 'שא את ראש', None),
                      ('when you lift the head', 'כי תשא את ראש', None), ('one soul of five hundred', 'אחד נפש מחמש המאות', None), ('one held of the fifty', 'אחד אחז מן החמשים', None),
                      ('the LORD\'s heave-offering', 'תרומת יהוה', None), ('who keep the charge of the tabernacle of the LORD', 'שמרי משמרת משכן יהוה', None),
                      ('the tribute (mekes)', 'מכס', None), ('the prey (malkoach)', 'המלקוח', None), ('the half of the congregation', 'מחצת העדה', None),
                      ('lifted the head (they)', 'נשאו את ראש', None), ('not one man of us is missing', 'ולא נפקד ממנו איש', None), ('to atone for our souls', 'לכפר על נפשתינו', None),
                      ('to atone for your souls', 'לכפר על נפשתיכם', None), ('a memorial for the children of Israel before the LORD', 'זכרון לבני ישראל לפני יהוה', None),
                      ('a memorial before the LORD (Exod 30:16 order)', 'לזכרון לפני יהוה', None), ('the LORD\'s offering', 'קרבן יהוה', None),
                      ('sixteen thousand seven hundred and fifty', 'ששה עשר אלף שבע מאות וחמשים', None), ('the tin', 'הבדיל', None), ('the lead', 'העפרת', None), ('and the lead', 'ואת העפרת', None)]:
    s = seats(ph, bk)
    print('  %-52s %d %s' % (label, len(s), s[:14]))
for label, t, bk in [('the tribute-word tokens (Torah)', 'מכס', T), ('the prey tokens (Torah)', 'המלקוח', T), ('the wrath-verb tokens (Torah)', 'ויקצף', T), ('the purify-verb tokens (Torah): תתחטאו', 'תתחטאו', T), ('יתחטא', 'יתחטא', T), ('the tin token (Torah)', 'הבדיל', T)]:
    s = tok(t, bk); print('  %-52s %d %s' % (label, len(s), s[:14]))
print('  the six metals at 31:22 (lemmas): %s' % [w for w in _V[('Num', 31, 22)]])
print('  Lev 11:32 words: %s' % ' '.join(_V[('Lev', 11, 32)]))
print('\n==== THE CALLEES (the values the runner asserts) ====')
def sh(label, f):
    try: print('  %s -> %r' % (label, f()))
    except BaseException as e: print('  %s RAISED %s %s' % (label, type(e).__name__, str(e)[:120]))
sh('BK midian_not_moab', lambda: BK.phinehas_and_midian({'ask': 'midian_not_moab'}, BK.DATA)[:2])
sh('BK balaam_death', lambda: BK.phinehas_and_midian({'ask': 'balaam_death'}, BK.DATA)[:2])
sh('BK cozbi_and_zur', lambda: BK.phinehas_and_midian({'ask': 'cozbi_and_zur'}, BK.DATA)[:2])
sh('BK DATA', lambda: (BK.DATA['balaam_death']['value'], sorted(BK.DATA['balaam_death']['settings']), BK.DATA['cozbi_and_zur']['value'], BK.DATA['midian_command_run']['value']))
sh('BH oppression war', lambda: BH.trumpets({'ask': 'oppression', 'kind': 'war'}, BH.DATA)[:2])
sh('BH count', lambda: BH.trumpets({'ask': 'count'}, BH.DATA)[:2])
sh('BH DATA oppression_scope', lambda: (BH.DATA['oppression_scope']['value'], sorted(BH.DATA['oppression_scope']['settings'])))
sh('BH TRUMPETS', lambda: BH.TRUMPETS)
sh('CK schedule', lambda: CK.corpse_tumah({'ask': 'schedule', 'third': True, 'seventh': True}, CK.DATA)[:2])
sh('CK seven_days', lambda: CK.corpse_tumah({'ask': 'seven_days'}, CK.DATA)[:2])
sh('CK sword_like_slain', lambda: CK.corpse_tumah({'ask': 'sword_like_slain'}, CK.DATA)[:2])
sh('CK camps', lambda: CK.corpse_tumah({'ask': 'camps'}, CK.DATA)[:2])
sh('CK tent_gentile', lambda: CK.corpse_tumah({'ask': 'tent_gentile'}, CK.DATA)[:2])
sh('CK metal_vessels_decree', lambda: CK.corpse_tumah({'ask': 'metal_vessels_decree'}, CK.DATA)[:2])
sh('CK removes', lambda: CK.corpse_tumah({'ask': 'removes'}, CK.DATA)[:2])
sh('CK SCHEDULE / SEVENS', lambda: (CK.SCHEDULE, CK.SEVENS))
sh('CK DATA', lambda: (CK.DATA['sword_like_slain']['value'], CK.DATA['tent_gentile']['value'], CK.DATA['third_day_fixed']['value']))
sh('SH touch', lambda: (SH.touch_effect('touch_carcass'), SH.touch_effect('carry_carcass')))
sh('IS lift_head', lambda: IS.shekel('lift_head')['v'])
sh('IS atone_souls', lambda: IS.shekel('atone_souls')['v'])
sh('IS plague_clause', lambda: (IS.shekel('plague_clause')['v'], IS.shekel('plague_clause')['fx']))
sh('IS silver_of_atonements', lambda: IS.shekel('silver_of_atonements')['v'])
sh('IS trigger_parameter', lambda: IS.shekel('trigger_parameter')['v'])
sh('BM houses_charges', lambda: BM.charges({'ask': 'houses_charges'}, BM.DATA)[:2])
sh('BM watches', lambda: BM.charges({'ask': 'watches'}, BM.DATA)[:2])
