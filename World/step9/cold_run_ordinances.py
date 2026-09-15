#!/usr/bin/env python3
"""cold_run_ordinances.py — THE REST OF THE ORDINANCES (Exod 20:19-26; 22:17-30; 23:1-9; 23:20-33)
(2026-09-06, sitting E1 of THE COMPILE DEBT — World/step9/COMPILE_DEBT.md; the
fourth runner compiled under THE DEPENDENCY GATE's rule: span declared, a stub
placed, the census run, three required edges and one homograph dispositioned
BEFORE the first cell, five more edges declared for the live calls the compile
made — and the priesthood runner's OWED edge of sitting L5 closed here: the
firstling's eighth day compiled at 22:29 and fetched by that runner by live call.)

Span: Exod 20:19-26 — THE ALTAR LAW (no gods of silver and gold; the altar of
earth; the burnt and peace offerings on it by the offering engine's rows;
'in every place where I cause My name to be mentioned'; the whole stones, the
sword that profanes, the steps — the decalogue runner's altar rules by live
call, one function at two seats); Exod 22:17-30 — THE CAPITAL TRIAD (the
sorceress, bestiality by the sanctions engine, the sacrifice to gods), THE
STRANGER AND THE WIDOW (the two verbs split, the cry heard, the measure
returned), THE LOAN (the obligatory 'if', the priority ladder, the interest by
the jubilee engine, the five prohibitions), THE PLEDGE (the sunset timer, the
day and night garments), THE CURSE OF JUDGE AND PRINCE (the fork: judge or
blasphemy; the Name gate), THE GIFTS' ORDER (fullness = first fruits, outflow
= terumah; do not delay = do not reorder), THE FIRSTBORN SON (by the Passover
engine; the thirty days; the five sela as data), THE FIRSTLING'S EIGHTH DAY
('with its mother' against Leviticus's 'under'; eighth and onward), THE TORN
FLESH (whatever cannot live; to the dog); Exod 23:1-9 — THE COURTS (the false
report's three warnings, the witness of violence, the asymmetric majority and
the twenty-three built from it, the poor not glorified, the enemy's straying
ox and lying donkey, the judgment not perverted, the acquitted never retried,
the bribe by the holiness engine, the stranger by the holiness engine's second
half); Exod 23:20-33 — THE ESCORT AND THE LAND (the angel with the Name in
him, the hornet, little by little, the borders as data, the pillars broken,
bread and water blessed, no covenant, the snare).

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Sanhedrin 1, 3, 4,
7, Bava Metzia 2 and 5, Bekhorot 8, Chullin 3, Terumot 3, Middot 3, Shevuot 4
read WHOLE (99 rows) + the nine link rows outside + two topic rows — 110 rows,
the ledger logic/oral_triage/ordinances_topic_docket_2026-09-06.md with its
coverage computed; 168 Talmud addresses indexed on the span, opened per gap.

The five motions, in order:
 (1) code from the BARE INK — 'gods of silver' a hapax; 'an altar of earth',
     'in every place', 'I cause My name to be mentioned' each a hapax; 'hewn'
     the Torah's only seat; 'by steps' a hapax; 'sorceress', 'you shall not
     wrong', 'nor oppress him', 'your fullness', 'your outflow', 'on the eighth
     day you shall give', 'with its mother' (against Lev 22:27's 'under its
     mother'), 'a false report', 'after the many', 'lying under its burden',
     'unload, you shall unload', 'from a false matter', 'the innocent and the
     righteous', 'the open-eyed', 'the soul of the stranger', 'the sea of the
     Philistines', 'miscarrying' each a hapax; 'a witness of violence' at
     Exod 23:1 and Deut 19:16 alone; 'until the sun sets' at 22:25 and Exod
     17:12 (Moses' hands) alone; 'you shall not glorify' at 23:3 and Lev 19:15
     alone; 'torn' at four seats (Jacob's speech the first); 'you were
     strangers' at four seats; 'shall not live' at three; 'devoted' at four;
     every quantity a PARAMETER (the five sela, the thirty days, the ris, the
     three days of enmity, the borders);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal typed
     from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Mekhilta of Rabbi
     Yishmael rows (the units' spine, verdicted 2026-09-01) and Onkelos;
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS.

Cross-span receipts, labeled [IMPORT] and CALLED (the edges dispositioned in
dependency_dispositions.yaml): cold_run_decalogue.altar_rules (the hewn stone,
the recipe, the steps); cold_run_offerings.dispatch (the burnt and peace
offerings on the earthen altar); cold_run_sanctions.beast / .outside (the
beast's warning and court; the tent door); cold_run_holiness.conduct (the
deaf's curse, the bribe); cold_run_holiness_b.convert_measures (the stranger
wronged by words; 'you were strangers'); cold_run_yovel.interest /
.interest_scope (the two nouns; the foreigner); cold_run_pesach.firstborn
(the son redeemed, the donkey, the Caesarean). Deut 22:1-4, 24:10-17, 19:16,
16:19, 7:20-22, Lev 24:15-16, 25:36-37, 27:28-29, Num 18:16 stay imports by name.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sqlite3, sys, os, json, io, contextlib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 128, ("the guard counted %d expectations, the tripwire holds 128" % GUARDED)

DB = (_ROOT + '/Data/tanakh.sqlite')
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def toks(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]

SPAN = [(20, v) for v in range(19, 27)] + [(22, v) for v in range(17, 31)] + [(23, v) for v in range(1, 10)] + [(23, v) for v in range(20, 34)]
def seats(pred, rng=SPAN):
    return [(c, v) for c, v in rng if pred(toks('Exod', c, v))]
def has(*ws):
    return lambda t: any(t[i:i + len(ws)] == list(ws) for i in range(len(t) - len(ws) + 1))
def anytok(*ws):
    return lambda t: any(w in t for w in ws)

# the whole-Tanakh token index (23,213 verses)
_ALL = collections.defaultdict(list)
_VERSES = {}
for he, book, ch, vs in db.execute("SELECT w.he, v.book, v.chapter, v.verse FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _ALL[strip(he)].append((book, ch, vs))
    _VERSES.setdefault((book, ch, vs), []).append(strip(he))
def tanakh(tok):
    return sorted(set(_ALL.get(tok, [])))
def tanakh_phrase(words):
    n = len(words)
    return sorted(k for k, t in _VERSES.items() if any(t[i:i + n] == words for i in range(len(t) - n + 1)))
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
N_VERSES = db.execute("SELECT COUNT(*) FROM verses").fetchone()[0]
assert N_VERSES == 23213, N_VERSES

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('gods of SILVER and gods of gold',                 'Exod', 20, 23, 'כסף'),
    ('an altar of EARTH you shall make Me',            'Exod', 20, 24, 'אדמה'),
    ('you shall not build them HEWN',                  'Exod', 20, 25, 'גזית'),
    ('you shall not go up by STEPS',                   'Exod', 20, 26, 'במעלת'),
    ('a SORCERESS you shall not let live',             'Exod', 22, 17, 'מכשפה'),
    ('whoever lies with a BEAST',                      'Exod', 22, 18, 'בהמה'),
    ('one who SACRIFICES to gods shall be devoted',    'Exod', 22, 19, 'יחרם'),
    ('a STRANGER you shall not wrong',                 'Exod', 22, 20, 'תונה'),
    ('every WIDOW and orphan you shall not afflict',   'Exod', 22, 21, 'אלמנה'),
    ('if he CRIES to Me',                              'Exod', 22, 22, 'צעק'),
    ('your wives WIDOWS and your sons orphans',        'Exod', 22, 23, 'אלמנות'),
    ('you shall not set INTEREST on him',              'Exod', 22, 24, 'נשך'),
    ('until the sun SETS you shall return it',         'Exod', 22, 25, 'השמש'),
    ('it is his only COVERING',                        'Exod', 22, 26, 'כסותה'),
    ('elohim you shall not CURSE',                     'Exod', 22, 27, 'תקלל'),
    ('your FULLNESS and your outflow',                 'Exod', 22, 28, 'מלאתך'),
    ('seven days it shall be WITH its mother',         'Exod', 22, 29, 'אמו'),
    ('flesh in the field TORN',                        'Exod', 22, 30, 'טרפה'),
    ('you shall not raise a FALSE report',             'Exod', 23, 1, 'שוא'),
    ('after the MANY',                                 'Exod', 23, 2, 'רבים'),
    ('the POOR you shall not glorify',                 'Exod', 23, 3, 'ודל'),
    ('your enemy\'s ox or his donkey STRAYING',        'Exod', 23, 4, 'תעה'),
    ('lying under its BURDEN',                         'Exod', 23, 5, 'משאו'),
    ('the judgment of your NEEDY',                     'Exod', 23, 6, 'אבינך'),
    ('the INNOCENT and the righteous do not kill',     'Exod', 23, 7, 'ונקי'),
    ('a BRIBE you shall not take',                     'Exod', 23, 8, 'ושחד'),
    ('the SOUL of the stranger',                       'Exod', 23, 9, 'נפש'),
    ('I send an ANGEL before you',                     'Exod', 23, 20, 'מלאך'),
    ('My NAME is in him',                              'Exod', 23, 21, 'שמי'),
    ('their PILLARS you shall break',                  'Exod', 23, 24, 'מצבתיהם'),
    ('He will bless your BREAD and your water',        'Exod', 23, 25, 'לחמך'),
    ('no MISCARRYING or barren in your land',          'Exod', 23, 26, 'משכלה'),
    ('the HORNET before you',                          'Exod', 23, 28, 'הצרעה'),
    ('LITTLE by little I will drive them out',         'Exod', 23, 30, 'מעט'),
    ('the sea of the PHILISTINES',                     'Exod', 23, 31, 'פלשתים'),
    ('you shall not cut a COVENANT',                   'Exod', 23, 32, 'ברית'),
    ('it will be a SNARE to you',                      'Exod', 23, 33, 'למוקש'),
]
fired = 0
for label, book, ch, vs, tok in PROBES:
    if tok in toks(book, ch, vs): fired += 1
    else: print('PROBE FAILED: %s (%s %d:%d lacks %s)' % (label, book, ch, vs, tok))
if fired != len(PROBES):
    sys.exit('zero-report law: the ink scan is not trusted until every probe fires')
print('probes: %d/%d fired (the ink scan is trusted; the whole-Tanakh census holds %d verses)' % (len(PROBES), len(PROBES), N_VERSES))

# ---- the censuses (TRIPWIRES — each a measured literal) ------------
c_silver = tanakh_phrase(['אלהי', 'כסף']);              assert c_silver == [('Exod', 20, 23)], c_silver
c_earth = tanakh_phrase(['מזבח', 'אדמה']);              assert c_earth == [('Exod', 20, 24)], c_earth
c_place = tanakh_phrase(['בכל', 'המקום']);              assert c_place == [('Exod', 20, 24)], c_place
c_mention = tanakh_phrase(['אזכיר', 'את', 'שמי']);      assert c_mention == [('Exod', 20, 24)], c_mention
c_hewn = [k for k in tanakh('גזית') if k[0] in TORAH];  assert c_hewn == [('Exod', 20, 25)], c_hewn
c_profaned = tanakh('ותחללה');                          assert c_profaned == [('Exod', 20, 25)], c_profaned
c_steps = tanakh('במעלת');                              assert c_steps == [('Exod', 20, 26)], c_steps
c_nakedness = tanakh('ערותך');                          assert len(c_nakedness) == 6 and ('Exod', 20, 26) in c_nakedness and ('Lev', 18, 10) in c_nakedness, c_nakedness
c_heaven = tanakh_phrase(['מן', 'השמים', 'דברתי']);     assert c_heaven == [('Exod', 20, 22)], c_heaven
c_sorceress = tanakh('מכשפה');                          assert c_sorceress == [('Exod', 22, 17)], c_sorceress
c_not_live = tanakh_phrase(['לא', 'תחיה']);             assert c_not_live == [('Deut', 20, 16), ('Exod', 22, 17), ('Zech', 13, 3)], c_not_live
c_devoted = tanakh('יחרם');                             assert c_devoted == [('Exod', 22, 19), ('Ezra', 10, 8), ('Lev', 27, 28), ('Lev', 27, 29)], c_devoted
c_wrong = tanakh('תונה');                               assert c_wrong == [('Exod', 22, 20)], c_wrong
c_oppress = tanakh('תלחצנו');                           assert c_oppress == [('Exod', 22, 20)], c_oppress
c_strangers = tanakh_phrase(['גרים', 'הייתם']);         assert c_strangers == [('Deut', 10, 19), ('Exod', 22, 20), ('Exod', 23, 9), ('Lev', 19, 34)], c_strangers
c_widow_orphan = tanakh_phrase(['אלמנה', 'ויתום']);     assert c_widow_orphan == [('Exod', 22, 21), ('Mal', 3, 5)], c_widow_orphan
c_afflict = tanakh('תענון');                            assert c_afflict == [('Exod', 22, 21)], c_afflict
c_cry_doubled = all(w in toks('Exod', 22, 22) for w in ('צעק', 'יצעק', 'שמע', 'אשמע')); assert c_cry_doubled
c_creditor = tanakh('כנשה');                            assert c_creditor == [('Exod', 22, 24), ('Isa', 24, 2)], c_creditor
c_bite = [k for k in tanakh('נשך') if k[0] in TORAH];   assert c_bite == [('Deut', 23, 20), ('Exod', 22, 24), ('Lev', 25, 36), ('Num', 21, 9)], c_bite
c_sunset = tanakh_phrase(['עד', 'בא', 'השמש']);         assert c_sunset == [('Exod', 17, 12), ('Exod', 22, 25)], c_sunset
c_garment = tanakh('שלמת');                             assert c_garment == [('Exod', 22, 25)], c_garment
c_covering = tanakh('כסותה');                           assert c_covering == [('Exod', 21, 10), ('Exod', 22, 26)], c_covering
c_gracious = tanakh_phrase(['חנון', 'אני']);            assert c_gracious == [('Exod', 22, 26)], c_gracious
c_curse = tanakh('תקלל');                               assert c_curse == [('Eccl', 10, 20), ('Exod', 22, 27), ('Job', 24, 18), ('Lev', 19, 14)], c_curse
c_fullness = tanakh('מלאתך');                           assert c_fullness == [('Exod', 22, 28)], c_fullness
c_outflow = tanakh('ודמעך');                            assert c_outflow == [('Exod', 22, 28)], c_outflow
c_delay = tanakh_phrase(['לא', 'תאחר']);                assert c_delay == [('Deut', 23, 22), ('Exod', 22, 28), ('Isa', 46, 13)], c_delay
c_firstborn_sons = tanakh_phrase(['בכור', 'בניך']);     assert c_firstborn_sons == [('Exod', 22, 28), ('Exod', 34, 20)], c_firstborn_sons
c_eighth_give = tanakh_phrase(['ביום', 'השמיני', 'תתנו']); assert c_eighth_give == [('Exod', 22, 29)], c_eighth_give
c_with_mother = tanakh_phrase(['עם', 'אמו']);           assert c_with_mother == [('Exod', 22, 29)], c_with_mother
c_under_mother = tanakh_phrase(['תחת', 'אמו']);         assert c_under_mother == [('Lev', 22, 27)], c_under_mother
c_holy_men = tanakh_phrase(['קדש', 'תהיון']);           assert c_holy_men == [('Exod', 22, 30)], c_holy_men
c_torn = tanakh('טרפה');                                assert c_torn == [('Exod', 22, 30), ('Gen', 31, 39), ('Lev', 7, 24), ('Nah', 2, 13)], c_torn
c_throw = tanakh('תשלכון');                             assert c_throw == [('Exod', 22, 30)], c_throw
c_false_report = tanakh_phrase(['שמע', 'שוא']);         assert c_false_report == [('Exod', 23, 1)], c_false_report
c_violence = tanakh_phrase(['עד', 'חמס']);              assert c_violence == [('Deut', 19, 16), ('Exod', 23, 1)], c_violence
c_wicked = [k for k in tanakh('רשע') if k[0] == 'Exod']; assert c_wicked == [('Exod', 23, 1), ('Exod', 23, 7)], c_wicked
c_many = tanakh_phrase(['אחרי', 'רבים']);               assert c_many == [('Exod', 23, 2)], c_many
c_evil = tanakh('לרעת');                                assert c_evil == [('Exod', 23, 2)], c_evil
c_tilt = tanakh('להטת');                                assert c_tilt == [('Exod', 23, 2)], c_tilt
c_glorify = tanakh('תהדר');                             assert c_glorify == [('Exod', 23, 3), ('Lev', 19, 15)], c_glorify
c_meet = tanakh('תפגע');                                assert c_meet == [('Exod', 23, 4), ('Jer', 7, 16)], c_meet
c_enemy = tanakh('איבך');                               assert len(c_enemy) == 6 and ('Exod', 23, 4) in c_enemy, c_enemy
c_hater = tanakh('שנאך');                               assert c_hater == [('Exod', 23, 5), ('Prov', 25, 21)], c_hater
c_burden = tanakh_phrase(['רבץ', 'תחת', 'משאו']);       assert c_burden == [('Exod', 23, 5)], c_burden
c_unload = tanakh_phrase(['עזב', 'תעזב']);              assert c_unload == [('Exod', 23, 5)], c_unload
c_pervert = tanakh_phrase(['תטה', 'משפט']);             assert c_pervert == [('Deut', 16, 19), ('Deut', 24, 17), ('Exod', 23, 6)], c_pervert
c_needy = tanakh('אבינך');                              assert c_needy == [('Exod', 23, 6)], c_needy
c_falsehood = tanakh_phrase(['מדבר', 'שקר']);           assert c_falsehood == [('Exod', 23, 7)], c_falsehood
c_innocent = tanakh_phrase(['ונקי', 'וצדיק']);          assert c_innocent == [('Exod', 23, 7)], c_innocent
c_bribe = sorted(set(k for k in tanakh('שחד') + tanakh('ושחד') + tanakh('השחד') if k[0] in TORAH)); assert c_bribe == [('Deut', 10, 17), ('Deut', 16, 19), ('Deut', 27, 25), ('Exod', 23, 8)], c_bribe
c_open_eyed = tanakh('פקחים');                          assert c_open_eyed == [('Exod', 23, 8)], c_open_eyed
c_twists = tanakh('ויסלף');                             assert c_twists == [('Deut', 16, 19), ('Exod', 23, 8), ('Prov', 22, 12)], c_twists
c_soul_stranger = tanakh_phrase(['נפש', 'הגר']);        assert c_soul_stranger == [('Exod', 23, 9)], c_soul_stranger
c_angel = tanakh_phrase(['שלח', 'מלאך']);               assert c_angel == [('Exod', 23, 20)], c_angel
c_name_in_him = tanakh_phrase(['שמי', 'בקרבו']);        assert c_name_in_him == [('Exod', 23, 21)], c_name_in_him
c_forgive = tanakh_phrase(['ישא', 'לפשעכם']);           assert c_forgive == [('Exod', 23, 21), ('Josh', 24, 19)], c_forgive
c_demolish = tanakh_phrase(['הרס', 'תהרסם']);           assert c_demolish == [('Exod', 23, 24)], c_demolish
c_miscarry = tanakh('משכלה');                           assert c_miscarry == [('Exod', 23, 26)], c_miscarry
c_barren = tanakh('ועקרה');                             assert c_barren == [('Deut', 7, 14), ('Exod', 23, 26)], c_barren
c_hornet = tanakh('הצרעה');                             assert c_hornet == [('Deut', 7, 20), ('Exod', 23, 28), ('Josh', 24, 12)], c_hornet
c_one_year = tanakh_phrase(['בשנה', 'אחת']);            assert c_one_year == [('1Kgs', 10, 14), ('2Chr', 9, 13), ('Exod', 23, 29)], c_one_year
c_little = tanakh_phrase(['מעט', 'מעט']);               assert c_little == [('Deut', 7, 22), ('Exod', 23, 30)], c_little
c_philistines = tanakh_phrase(['ים', 'פלשתים']);        assert c_philistines == [('Exod', 23, 31)], c_philistines
c_snare = tanakh('למוקש');                              assert len(c_snare) == 8 and ('Exod', 23, 33) in c_snare and ('Exod', 34, 12) in c_snare, c_snare
c_ifs = seats(lambda t: t[0] in ('אם', 'ואם', 'כי', 'וכי'));  assert c_ifs == [(20, 25), (22, 22), (22, 24), (22, 25), (22, 26), (23, 4), (23, 5), (23, 22), (23, 23)], c_ifs
c_doubled = seats(lambda t: any(t[i] == t[i + 1] or (t[i + 1][:1] in ('ת', 'א', 'י') and t[i + 1][1:].startswith(t[i]) and len(t[i]) >= 3) for i in range(len(t) - 1)))
assert c_doubled == [(22, 22), (22, 25), (23, 5), (23, 22), (23, 24), (23, 30)], c_doubled
print('censuses: gods of silver %s · altar of earth %s · in every place %s · hewn (Torah) %s · by steps %s · sorceress %s · "shall not live" %d seats · devoted %d · '
      'wrong / oppress each %s · "you were strangers" %d seats · widow and orphan %s · creditor %s · bite (Torah) %d · "until the sun sets" %s · curse-verb %d · fullness %s outflow %s · '
      '"on the eighth day you shall give" %s · WITH its mother %s vs UNDER its mother %s · torn %d · false report %s · witness of violence %s · after the many %s · glorify %s · '
      'lying under its burden %s · unload doubled %s · from falsehood %s · the innocent and righteous %s · bribe (Torah) %d · open-eyed %s · soul of the stranger %s · '
      'the conditional heads at %s · the doubled verbs at %s'
      % (c_silver, c_earth, c_place, c_hewn, c_steps, c_sorceress, len(c_not_live), len(c_devoted), c_wrong + c_oppress, len(c_strangers), c_widow_orphan, c_creditor, len(c_bite),
         c_sunset, len(c_curse), c_fullness, c_outflow, c_eighth_give, c_with_mother, c_under_mother, len(c_torn), c_false_report, c_violence, c_many, c_glorify, c_burden, c_unload,
         c_falsehood, c_innocent, len(c_bribe), c_open_eyed, c_soul_stranger, c_ifs, c_doubled))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_decalogue as DEC
    import cold_run_offerings as OFF
    import cold_run_sanctions as SA
    import cold_run_holiness as HL
    import cold_run_holiness_b as HB
    import cold_run_yovel as YV
    import cold_run_pesach as PS
DEC_HEWN = DEC.altar_rules({'ask': 'hewn_stones'}, DEC.DATA)[0]; DEC_RECIPE = DEC.altar_rules({'ask': 'build_recipe'}, DEC.DATA)[0]
DEC_STEPS = DEC.altar_rules({'ask': 'steps'}, DEC.DATA)[0]
OLAH_F = OFF.dispatch('olah:flock'); OLAH_H = OFF.dispatch('olah:herd'); SHEL = OFF.dispatch('shelamim')
SA_BEAST_WARN = SA.beast('passive_warning')['v']; SA_BEAST_COURT = SA.beast('court')['v']; SA_WOMAN = SA.beast('woman_warning')['v']
SA_OUT_WHERE = SA.outside('where')['v']; SA_OUT_WHO = SA.outside('who')['v']
HL_DEAF = HL.conduct('curse_deaf')['v']; HL_BRIBE = HL.conduct('bribe')['v']; HL_EQUAL = HL.conduct('equal_treatment')['v']
HB_WORD = HB.convert_measures('word_wrong')['v']; HB_STRANGERS = HB.convert_measures('you_were_strangers')['v']; HB_GER_SEATS = HB.convert_measures('ger_seats')['v']
YV_INT = YV.interest(); YV_BROTHER = YV.interest_scope('brother')['v']; YV_FOREIGN = YV.interest_scope('foreigner')['v']
PS_HUMAN = PS.firstborn({'kind': 'human'}, PS.DATA)[0]; PS_DONKEY = PS.firstborn({'kind': 'donkey'}, PS.DATA)[0]; PS_CAES = PS.firstborn({'kind': 'caesarean_animal'}, PS.DATA)[0]
print('routing receipts: cold_run_decalogue CALLED — hewn %r, recipe %r, steps %r; cold_run_offerings CALLED — olah:flock %r, shelamim window %r; cold_run_sanctions CALLED — '
      'beast warning %r, court %r, woman %r, outside where %r; cold_run_holiness CALLED — deaf %r, bribe %r; cold_run_holiness_b CALLED — word wrong %r, strangers %r, ger seats %r; '
      'cold_run_yovel CALLED — both nouns %r, brother %r, foreigner %r; cold_run_pesach CALLED — human %r, donkey %r, caesarean %r [IMPORT, live calls]'
      % (DEC_HEWN, DEC_RECIPE, DEC_STEPS, OLAH_F['disposition']['v'], SHEL['window']['v'], SA_BEAST_WARN, SA_BEAST_COURT, SA_WOMAN, SA_OUT_WHERE, HL_DEAF, HL_BRIBE,
         HB_WORD, HB_STRANGERS, HB_GER_SEATS, YV_INT['both_nouns']['v'], YV_BROTHER, YV_FOREIGN, PS_HUMAN, PS_DONKEY, PS_CAES))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
MK = 'Mekhilta on Exod '

# =====================================================================
# THE CODE — from the ink of the four spans alone. Mishnah/Talmud appear
# ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE ALTAR LAW (20:19-26) ------------------------------------
def altar(q):
    if q == 'from_heaven':
        return cell('hapax', I, f"20:22 'you have seen that FROM HEAVEN I spoke with you' — the phrase at {c_heaven} alone; the altar law opens on the giving's own witness", [FX.NONE])
    if q == 'silver_gold':
        return cell('no_gods_of_silver_or_gold', I, f"20:23 'you shall not make WITH ME gods of silver, and gods of gold you shall not make for yourselves' — 'gods of silver' at {c_silver} "
                    "alone; the decalogue runner's image-scope machine (the Decalogue's second utterance) by name", ['disqualified'])
    if q == 'earth_altar':
        return cell('attached_to_the_ground', A, f"20:24 'an altar of EARTH you shall make Me' — the phrase at {c_earth} alone; Mishnah Chagigah 3:8 (linked at 20:21): the golden and the "
                    "copper altars need no immersion 'because they are LIKE THE GROUND' (R. Eliezer) — the earth predicate at its Mishnah seat; Mishnah Middot 3:1's dimensions the data channel", [FX.NONE])
    if q == 'olah_on_it':
        return cell(OLAH_F['disposition']['v'], P, f"20:24 'and you shall sacrifice on it your BURNT OFFERINGS and your PEACE OFFERINGS, your flock and your herd' — the two classes by their "
                    f"engines: CALLED cold_run_offerings.dispatch(olah:flock) -> disposition {OLAH_F['disposition']['v']!r}, procedure {OLAH_F['procedure']['v']!r}; (olah:herd) place "
                    f"{OLAH_H['place']['v']!r} [IMPORT, live call]", ['smoked_to_the_lord'])
    if q == 'shelamim_on_it':
        return cell(SHEL['window']['v'], P, f"20:24's peace offerings — CALLED cold_run_offerings.dispatch(shelamim) -> window {SHEL['window']['v']!r}, eater {SHEL['eater']['v']!r} "
                    "(Lev 7:16) [IMPORT, live call]; 'your flock and your herd' the two species the offering engine's fat inventories hold", ['eating_window'])
    if q == 'every_place':
        return cell('hapax_the_name_mentioned', I, f"20:24 'IN EVERY PLACE where I cause My name to be MENTIONED I will come to you and bless you' — 'in every place' at {c_place} "
                    f"and 'I cause My name to be mentioned' at {c_mention} alone; the Name-mention clause's two recorded jobs sit at EX20-19; the eras of the high places "
                    "(Mishnah Zevachim 14:4-8, the eighth day's runner) are the clause's history", ['accepted'])
    if q == 'hewn':
        return cell(DEC_HEWN, P, f"20:25 'if an altar of stones you make Me, you shall not build them HEWN (גזית)' — the token's only Torah seat {c_hewn}; CALLED "
                    f"cold_run_decalogue.altar_rules(hewn_stones) -> {DEC_HEWN!r} (Mishnah Middot 3:4) [IMPORT, live call — one function at two seats]", ['disqualified'])
    if q == 'sword_profanes':
        return cell('iron_profanes_by_touch', I, f"20:25 'for you have lifted your SWORD upon it and PROFANED it' — 'and profaned it' (ותחללה) at {c_profaned} alone; the sword "
                    "= iron, the touch = the profaning (Mishnah Middot 3:4: 'iron disqualifies by touch', 'iron was created to shorten man's days and the altar to lengthen them')", ['disqualified'])
    if q == 'recipe':
        return cell(DEC_RECIPE, P, f"the build that honors the ban — CALLED cold_run_decalogue.altar_rules(build_recipe) -> {DEC_RECIPE!r} (Zevachim 54a:8, Levi's baraita) [IMPORT, live call]", [FX.NONE])
    if q == 'stones_source':
        return cell('whole_stones_from_beit_kerem_valley', A, "Mishnah Middot 3:4: the stones of the ramp and the altar from the valley of Beit Kerem, dug below the virgin soil — WHOLE "
                    "stones on which iron was not lifted; one notched is unfit and the rest fit; whitewashed twice a year", [FX.NONE])
    if q == 'steps':
        return cell(DEC_STEPS, P, f"20:26 'and you shall not go up BY STEPS (במעלת) on My altar' — the token at {c_steps} alone; CALLED cold_run_decalogue.altar_rules(steps) -> "
                    f"{DEC_STEPS!r} (Sanhedrin 7b:12) [IMPORT, live call]", [FX.NONE])
    if q == 'ramp':
        return cell('thirty_two_by_sixteen_south', D, "Mishnah Middot 3:3: the RAMP to the south of the altar, thirty-two long and sixteen wide, with a recess on its west — the ramp's "
                    "measures are the data channel; the ramp is the answer to 'not by steps'", [FX.NONE])
    if q == 'nakedness':
        return cell('the_ramps_reason', I, f"20:26 'that your NAKEDNESS not be uncovered on it' — the token at {len(c_nakedness)} seats (Lev 18:10's forbidden union among them); "
                    "the reason clause the ramp serves: the priest's stride, not the step", [FX.NONE])
    if q == 'obligatory_if':
        return cell('one_of_three_obligatory_ifs', M, MK + "22:24 — 'IF money you lend' is OBLIGATION, one of the Torah's three obligatory if-clauses: the lending, the first fruits' meal "
                    f"offering, and 'IF an altar of stones' (20:25); the conditional heads in this runner's spans at {c_ifs}", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F2: THE CAPITAL TRIAD (22:17-19) ---------------------------------
def capital(q):
    if q == 'sorceress_gender':
        return cell('man_and_woman_alike', M, f"22:17 'a SORCERESS (מכשפה) you shall not let live' — the noun at {c_sorceress} alone in the Tanakh, feminine; " + MK + "22:17: man and "
                    "woman alike — the verse speaks of the common case (Mishnah Sanhedrin 7:4 lists 'the sorcerer', masculine)", ['put_to_death'])
    if q == 'sorceress_mode':
        return cell('stoning', A, "Mishnah Sanhedrin 7:4: THE SORCERER among the stoned; the mode disputed at " + MK + "22:17 — R. Yishmael: the sword, by 'shall not live' with "
                    "Deut 20:16's 'you shall not let any soul live'; R. Akiva: stoning, by Sinai's 'whether beast or man he shall not live' (Exod 19:13 — the round-25 seat); R. Yehuda "
                    f"b. Beteira: stoning by the ov's exit (Lev 20:27); 'shall not live' at {len(c_not_live)} Tanakh seats", ['stoned'])
    if q == 'sorceress_deed':
        return cell('doer_liable_deceiver_exempt', A, "Mishnah Sanhedrin 7:11: the sorcerer who DOES a deed is liable, not the one who deceives the eyes — R. Akiva in R. Yehoshua's "
                    "name: two gather cucumbers, one exempt, one liable", ['stoned'])
    if q == 'sorceress_warning':
        return cell('Deut_18_10', M, MK + "22:17: the warning is Deut 18:10's 'there shall not be found among you... a sorcerer' — the punishment here, the warning there (the "
                    "warning-completion move M-20)", [FX.NONE])
    if q == 'beast_mode':
        return cell(SA_BEAST_WARN, P, f"22:18 'whoever lies with a beast shall surely die' — the sanctions engine compiled the act at Lev 18:23 / 20:15-16 and holds THIS verse as the "
                    f"passive's warning: CALLED cold_run_sanctions.beast(passive_warning) -> {SA_BEAST_WARN!r} [IMPORT, live call]; " + MK + "22:18: stoning by the 'kill'-'kill' analogy "
                    "to Lev 20, the lain-with counted as the lier", ['stoned'])
    if q == 'beast_court':
        return cell(SA_BEAST_COURT, P, f"the court for the beast's case — CALLED cold_run_sanctions.beast(court) -> {SA_BEAST_COURT!r} (Mishnah Sanhedrin 1:4: 'the beast lain with and "
                    "its human by twenty-three') [IMPORT, live call]", [FX.NONE])
    if q == 'beast_woman':
        return cell(SA_WOMAN, P, f"the woman's warning — CALLED cold_run_sanctions.beast(woman_warning) -> {SA_WOMAN!r} [IMPORT, live call]; Mishnah Sanhedrin 7:4 'the woman who "
                    "brings the beast' among the stoned", ['stoned'])
    if q == 'devoted_seats':
        return cell(4, I, f"22:19 'one who sacrifices to gods shall be DEVOTED (יחרם)' — the verb at {c_devoted}: this verse, Lev 27:28-29's devoted things ('shall surely be put to "
                    "death'), Ezra 10:8's devoted property; Onkelos Exod 22:19 renders it 'shall be KILLED'", ['put_to_death'])
    if q == 'service_architecture':
        return cell('temple_services_for_any_idol', M, MK + "22:19: 'sacrificing' was in the general rule and left it to teach — the Temple's inside-services (slaughter and its kin) "
                    "are liable for ANY idol whether or not that is its cult; other services only in the idol's own manner; Mishnah Sanhedrin 7:6 names the four: sacrifices, "
                    "burns incense, pours a libation, bows", ['stoned'])
    if q == 'idolater_row':
        return cell('serves_sacrifices_incense_libation_bows_accepts_says', A, "Mishnah Sanhedrin 7:6: the idolater — one who serves, sacrifices, burns incense, pours, bows, accepts "
                    "it as a god, says 'you are my god'; the embracer and kisser a prohibition; Peor and Merkulis by their own services", ['stoned'])
    if q == 'only_to_the_LORD':
        return cell('save_to_the_LORD_alone', I, "22:19 'SAVE to the LORD ALONE' (בלתי ליהוה לבדו) — the clause that empties every Temple service to the Unique Name (the round-25 "
                    "paradigm); the outside-slaughter engine's tent door beside it: CALLED cold_run_sanctions.outside(where) -> %r [IMPORT, live call]" % SA_OUT_WHERE, [FX.NONE])
    if q == 'joining':
        return cell('R_Shimon_b_Yochai_liable', M, MK + "22:19: joining His name with another (Kings' 'fearing the LORD and serving their gods') — R. Shimon b. Yochai: liable to "
                    "destruction; the mountains verse against the hidden-idolatry excuse", ['put_to_death'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F3: THE STRANGER, THE WIDOW, THE ORPHAN (22:20-23) ---------------
def stranger(q):
    if q == 'two_verbs':
        return cell('wrong_hapax_oppress_hapax', I, f"22:20 'a stranger you shall not WRONG (תונה) nor OPPRESS him (תלחצנו)' — each verb form at {c_wrong + c_oppress} alone", ['exempt'])
    if q == 'words_vs_money':
        return cell(HB_WORD, P, MK + "22:20: the two verbs split — wronging = WORDS, oppression = MONEY; Mishnah Bava Metzia 4:10 quotes this verse for wronging by words ('remember "
                    f"your fathers' deeds' to a convert's son) — CALLED cold_run_holiness_b.convert_measures(word_wrong) -> {HB_WORD!r} (Lev 19:33) [IMPORT, live call]", [FX.NONE])
    if q == 'you_were_strangers':
        return cell(HB_STRANGERS, P, f"22:20 and 23:9 'for you were strangers in the land of Egypt' — the phrase at {c_strangers}: this span's two seats, Lev 19:34, Deut 10:19; "
                    f"CALLED cold_run_holiness_b.convert_measures(you_were_strangers) -> {HB_STRANGERS!r} [IMPORT, live call]; " + MK + "22:20 (R. Natan): a blemish in you, do not "
                    "say to your fellow", [FX.NONE])
    if q == 'ger_seats':
        return cell(HB_GER_SEATS, P, f"the holiness engine's second half counts the stranger's seats in Lev 19 — CALLED cold_run_holiness_b.convert_measures(ger_seats) -> "
                    f"{HB_GER_SEATS!r} [IMPORT, live call]; the two Exodus seats (22:20, 23:9) are the earlier writing of the same law", [FX.NONE])
    if q == 'beloved_census':
        return cell('every_title_israel_carries', M, MK + "22:20: converts carry every title Israel carries — servants, ministers, lovers, covenant, acceptance, guarding (the "
                    "verse-paired list); Abraham circumcised at ninety-nine so the door stays open (the gen_33 seat cited)", [FX.NONE])
    if q == 'widow_orphan_scope':
        return cell('R_Yishmael_all_persons_R_Akiva_the_named', M, f"22:21 'every widow and orphan you shall not afflict' — 'widow and orphan' at {c_widow_orphan} (Malachi 3:5 "
                    f"the other), 'you shall not afflict' (תענון) at {c_afflict} alone; " + MK + "22:21-23: R. Yishmael — ALL persons (the verbs unqualified), R. Akiva — the "
                    "widow and orphan named because their way is to be afflicted", ['cry_heard'])
    if q == 'one_affliction':
        return cell('one_affliction_is_liability', M, MK + "22:21-23: one affliction, great or small, is liability — with the execution narrative: R. Shimon and R. Yishmael led "
                    "out, and R. Yishmael locates the sin in litigants kept waiting while he finished his cup or sandal", ['cry_heard'])
    if q == 'cry_doubled':
        return cell('cry_cry_hear_hear', I, f"22:22 'if you afflict, afflict him — for if he CRIES, CRIES to Me, I will HEAR, HEAR his cry' — three doubled verbs in one verse "
                    f"(the doubled verbs of the spans at {c_doubled}); " + MK + ": heard always, FASTER when he cries", ['cry_heard'])
    if q == 'measure_for_measure':
        return cell('wives_widows_sons_orphans', I, "22:23 'My anger shall burn and I will kill you with the sword, and your wives shall be WIDOWS and your sons ORPHANS' — the "
                    "punishment mirrors the offense word for word; " + MK + ": 'living widowhood' — courts unable to release, sons kept from the estate on the presumption he lives", ['cry_heard', 'put_to_death'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F4: THE LOAN, THE INTEREST, THE PLEDGE (22:24-26) ----------------
def loan(q):
    if q == 'im_obligation':
        return cell('lending_is_obligation', M, MK + "22:24: 'IF money you lend My people' — 'if' here is OBLIGATION (proven from Deut 15:8's 'you shall surely lend'), one of "
                    "three obligatory if-clauses; money for money, not produce for produce", [FX.NONE])
    if q == 'priority_ladder':
        return cell(['my_people_before_gentile', 'poor_before_rich', 'your_poor_before_your_city', 'your_city_before_another'], M, MK + "22:24: 'MY PEOPLE... THE POOR WITH YOU' — "
                    "My people before a gentile, the poor before the rich, your poor before your city's, your city's before another's", [FX.NONE])
    if q == 'creditor_manner':
        return cell('not_seen_at_all_times', M, f"22:24 'you shall not be to him AS A CREDITOR (כנשה)' — the token at {c_creditor} (Isaiah 24:2 the other); " + MK + ": do not show "
                    "yourself to him at all times", [FX.NONE])
    if q == 'bite_noun':
        return cell(4, I, f"22:24 'you shall not set on him INTEREST (נשך)' — the bite noun's Torah seats {c_bite}: this, Lev 25:36 (the jubilee engine's), Deut 23:20 (the "
                    "foreigner), and Num 21:9's biting serpent — the noun is the animal's verb", ['interest_barred'])
    if q == 'interest_spec':
        return cell(YV_INT['both_nouns']['v'], P, f"the two interest nouns compiled at Lev 25:36-37 — CALLED cold_run_yovel.interest() -> both nouns {YV_INT['both_nouns']['v']!r}, "
                    f"definitions {YV_INT['definitions']['v']!r} (Mishnah Bava Metzia 5:1) [IMPORT, live call]; this verse writes the BITE noun alone", ['interest_barred'])
    if q == 'foreigner':
        return cell(YV_FOREIGN, P, f"'My people' — CALLED cold_run_yovel.interest_scope(foreigner) -> {YV_FOREIGN!r}, (brother) -> {YV_BROTHER!r} (Deut 23:21 by import) [IMPORT, "
                    "live call]; Mishnah Bava Metzia 5:6: iron sheep from gentiles, lending to and borrowing from them at interest", ['interest_barred'])
    if q == 'five_prohibitions':
        return cell(['lo_titen_Lev_25_37', 'al_tikach_Lev_25_36', 'ke_nosheh_Exod_22_24', 'neshekh_Exod_22_24', 'lifnei_iver_Lev_19_14'], A, "Mishnah Bava Metzia 5:11: the "
                    "lender transgresses 'you shall not give' (Lev 25:37), 'do not take from him' (25:36), 'do not be to him as a creditor' (THIS VERSE), 'do not set interest on "
                    "him' (THIS VERSE), and 'before the blind do not put a stumbling block' (Lev 19:14) — two of the five are 22:24's two clauses; " + MK + ": the lender's five", ['interest_barred'])
    if q == 'who_transgresses':
        return cell(['lender', 'borrower', 'guarantor', 'witnesses'], A, "Mishnah Bava Metzia 5:11: the lender, the borrower, the guarantor, and the witnesses; the sages: the "
                    "scribe too — " + MK + "22:24: Rebbi permits the scribe; R. Meir bars the dictating lender from the resurrection", ['interest_barred'])
    if q == 'pledge_sunset':
        return cell('until_the_sun_sets', I, f"22:25 'if you take your fellow's garment in pledge, UNTIL THE SUN SETS you shall return it to him' — the phrase at {c_sunset}: this "
                    "and Exod 17:12, Moses' hands held up 'until the sun set' — the day's boundary written once for a battle and once for a garment; 'garment' (שלמת) at "
                    f"{c_garment} alone", ['pledge_returned_by_sunset'])
    if q == 'day_night_garments':
        return cell('day_garment_by_day_night_garment_by_night', M, MK + "22:25-26: paired with Deut 24:13's sunset return — 'they pledge day-clothing by night and night-clothing "
                    "by day, and return each in its time'; Mishnah Bava Metzia 9:13: the pillow returned by night and the plow by day", ['pledge_returned_by_sunset'])
    if q == 'court_only':
        return cell('only_through_the_court_outside_you_stand', A, "Mishnah Bava Metzia 9:13: the lender takes a pledge only through the court and does not enter the house — "
                    "'outside you shall stand' (Deut 24:11 [IMPORT]); two vessels, one taken and one left", ['pledge_returned_by_sunset'])
    if q == 'widow_not_pledged':
        return cell('never_pledged_rich_or_poor', A, "Mishnah Bava Metzia 9:13: a widow, poor or rich, is not pledged (Deut 24:17 [IMPORT]); the millstone not taken, 'for he "
                    "takes a life in pledge' (Deut 24:6)", ['pledge_returned_by_sunset'])
    if q == 'covering_tokens':
        return cell('cloak_shirt_mattress', M, f"22:26 'for it is his only COVERING (כסותה), it is his garment for his skin, in what shall he lie down' — 'covering' at "
                    f"{c_covering}: the maidservant's covering (21:10) and this; " + MK + ": covering = the cloak, garment = the shirt, 'in what shall he lie' brings the hide mattress; "
                    "R. Natan: a hundred owed does not force the sale of the two-hundred cloak", ['pledge_returned_by_sunset'])
    if q == 'gracious':
        return cell('hapax', I, f"22:26 'and it shall be, when he cries to Me, I will hear, for I am GRACIOUS' — 'gracious am I' at {c_gracious} alone; " + MK + ": 'with "
                    "compassion I created My world'", ['cry_heard'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F5: THE CURSE, THE GIFTS, THE FIRSTBORN, THE FIRSTLING, THE TORN (22:27-30) ----
def gifts(q):
    if q == 'elohim_fork':
        return cell('R_Yishmael_judge_R_Akiva_blasphemy_warning', M, "22:27 'ELOHIM you shall not curse' — " + MK + "22:27: elohim = the JUDGE (R. Yishmael; Onkelos writes 'the "
                    "judge') or the warning for BLASPHEMY (R. Akiva — the warning Lev 24:15-16's penalty verse lacked, the lev24 runner's curse gate by name)", ['lashes'])
    if q == 'curse_verb_seats':
        return cell(HL_DEAF, P, f"the curse verb 'you shall not curse' (תקלל) at {c_curse}: this and Lev 19:14's 'the deaf' — the holiness engine's cell imports this verse by "
                    f"name: CALLED cold_run_holiness.conduct(curse_deaf) -> {HL_DEAF!r} [IMPORT, live call]", ['lashes'])
    if q == 'name_gate':
        return cell('liable_only_by_the_Name', A, "Mishnah Sanhedrin 7:5: the blasphemer is not liable until he pronounces the Name; 7:8: the parent-curser not liable until he "
                    "curses by the Name — by an epithet R. Meir liable, the sages exempt; Shevuot 4:13: 'the one who curses by all of these' (the epithets) — R. Meir liable, the "
                    "sages exempt; the curser of himself or his fellow by them transgresses a prohibition", ['lashes'])
    if q == 'four_liabilities':
        return cell(4, M, MK + "22:27: a prince's son cursing his father is liable FOUR ways — as prince, as father, as judge, and 'among your people'; R. Yehuda b. Beteira: "
                    "the judge and the prince each its own liability", ['lashes'])
    if q == 'among_your_people':
        return cell('while_they_act_by_your_peoples_way', M, "22:27 'and a PRINCE among your people you shall not curse' — " + MK + ": 'among your people' — while they act by "
                    "your people's way; 'you shall not curse' (תאר) the second verb of the verse", ['lashes'])
    if q == 'fullness_outflow':
        return cell('first_fruits_and_terumah', M, f"22:28 'your FULLNESS (מלאתך) and your OUTFLOW (ודמעך) you shall not delay' — each noun at {c_fullness + c_outflow} alone in "
                    "the Tanakh; " + MK + "22:28: fullness = first fruits, outflow = terumah; Onkelos Exod 22:28 writes 'your first fruits'", ['gift_order_barred'])
    if q == 'delay_is_reorder':
        return cell('do_not_reorder', M, f"'you shall not DELAY' at {c_delay} (Deut 23:22's vow, Isa 46:13) — " + MK + ": do not REORDER the gifts: first fruits before terumah "
                    "before the first tithe before the second, argued from the four, three, two, one NAMES each gift carries", ['gift_order_barred'])
    if q == 'order_sheet':
        return cell('act_stands_though_forbidden', A, "Mishnah Terumot 3:6: one who separates terumah before the first fruits, the first tithe before terumah, the second before "
                    "the first — though he transgresses a prohibition, WHAT HE DID IS DONE, 'your fullness and your outflow you shall not delay' — THIS VERSE quoted as the "
                    "source", ['gift_order_barred'])
    if q == 'names_count':
        return cell([4, 3, 2, 1], A, "Mishnah Terumot 3:7: the first fruits precede, being 'first of all'; terumah precedes the first tithe, being 'first'; the first tithe "
                    "precedes the second, having 'first' in it — the Mekhilta's count of titles (four, three, two, one) as the sheet's argument", ['gift_order_barred'])
    if q == 'firstborn_son':
        return cell(PS_HUMAN, P, f"22:28 'the FIRSTBORN of your sons you shall give to Me' — the phrase at {c_firstborn_sons} (34:20 restates it); the consecration is Exod "
                    f"13:2's: CALLED cold_run_pesach.firstborn(human) -> {PS_HUMAN!r} [IMPORT, live call]; Onkelos 22:28: 'set apart before Me'", ['consecrated_firstborn'])
    if q == 'five_sela':
        return cell('five_sela_tyrian_maneh', D, "Mishnah Bekhorot 8:7: five sela of the son in Tyrian maneh, in the sanctuary shekel — the data channel (Num 18:16 [IMPORT], "
                    "the pesach engine's 'fetched constant'); redeemed with money or its worth, not with slaves, documents, land, or consecrated things (8:8)", ['consecrated_firstborn'])
    if q == 'thirty_days':
        return cell('day_thirty_is_the_edge', A, "Mishnah Bekhorot 8:6: died within thirty days — though given, returned; after thirty — though not given, given; on the "
                    "thirtieth — as the day before (R. Akiva: doubtful); " + MK + "22:29: thirty days' care for the human and the animal firstborn alike, from the analogy", ['consecrated_firstborn'])
    if q == 'stillbirth':
        return cell('stillbirths_open_the_womb_for_both', M, MK + "22:29: the human and animal firstborn read by analogy both ways — stillbirths open the womb-exemption for "
                    "both; Mishnah Bekhorot 8:1: the one after a miscarried sac or a stillbirth is a firstborn for inheritance, not for the priest", [FX.NONE])
    if q == 'caesarean':
        return cell(PS_CAES, P, f"Mishnah Bekhorot 8:2: a Caesarean and the one after him — neither for inheritance nor the priest (R. Shimon: the first for inheritance, the "
                    f"second for five sela); the pesach engine's predicate 'opener of the womb': CALLED cold_run_pesach.firstborn(caesarean_animal) -> {PS_CAES!r} [IMPORT, live call]", [FX.NONE])
    if q == 'to_any_priest':
        return cell('valid_to_any_priest_anywhere', M, MK + "22:29: the redemption and the gift valid to any priest anywhere — for the human and the animal alike", ['due_to_priest'])
    return cell('no_case', I, '', [FX.NONE])

def firstling(q):
    """22:29 — the firstling of the ox and the sheep: seven days with its mother, on the eighth day given. THE CALLEE the
    priesthood runner owed since sitting L5 (its Lev 22:27 cell joins the two eighth days)."""
    if q == 'run_phrase':
        return cell('hapax', I, f"22:29 'so shall you do with your ox and your sheep: seven days it shall be with its mother, ON THE EIGHTH DAY YOU SHALL GIVE IT TO ME' — "
                    f"'on the eighth day you shall give' at {c_eighth_give} alone", ['eighth_day_fit'])
    if q == 'with_its_mother':
        return cell('with_not_under', M, f"22:29 'WITH its mother' (עם אמו) at {c_with_mother} alone against Lev 22:27's 'UNDER its mother' (תחת אמו) at {c_under_mother} alone — "
                    "the two seats of one timer written with two prepositions; " + MK + "22:29: 'seven days with its mother' = WITH, not under (R. Yosei HaGelili at the Sifra: alive "
                    "with the mother one hour suffices)", ['eighth_day_fit'])
    if q == 'eighth_and_onward':
        return cell('on_the_eighth_day_and_onward', M, MK + "22:29: 'on the eighth day' — the eighth AND ONWARD, by the eighth-eighth analogy to Lev 22:27's 'from the eighth day "
                    "and onward it shall be accepted' (Sifra Emor Section 8 5: its-mother/its-mother carries both readings at both seats); the value the priesthood runner "
                    "fetches by live call (the OWED edge of sitting L5, closed here)", ['eighth_day_fit'])
    if q == 'nursed_from_chullin':
        return cell('nursed_from_common_funds', M, MK + "22:29: consecrated animals' young are nursed from common funds — the sanctified may not be milked", [FX.NONE])
    if q == 'donkey_by_call':
        return cell(PS_DONKEY, P, f"the firstling of the DONKEY is not this verse's (ox and sheep) — Exod 13:13's: CALLED cold_run_pesach.firstborn(donkey) -> {PS_DONKEY!r} "
                    "[IMPORT, live call]; Mishnah Kiddushin 2:9 lists the firstborn donkey among the no-benefit classes", ['redeem_or_break'])
    if q == 'two_seats_one_timer':
        return cell({'exod_22_29': 'on_the_eighth_day', 'lev_22_27': 'from_the_eighth_day_onward'}, I, "the firstling's eighth day (this verse, 'give') and the offering's "
                    "eighth day (Lev 22:27, 'accepted') — one timer at two seats, the priesthood runner's cell holding the join and this runner the callee", ['eighth_day_fit'])
    return cell('no_case', I, '', [FX.NONE])

def torn(q):
    if q == 'holy_men':
        return cell('hapax', I, f"22:30 'and MEN OF HOLINESS you shall be to Me' — 'holiness you shall be' at {c_holy_men} alone; " + MK + "22:30: 'when you are holy, you are "
                    "Mine' (R. Yishmael); Issi b. Yehuda: every new commandment adds holiness", [FX.NONE])
    if q == 'torn_seats':
        return cell(4, I, f"'torn' (טרפה) at {c_torn}: Jacob's 'the torn I did not bring you' (Gen 31:39) the first, Lev 7:24's fat of the torn, this, Nahum 2:13", ['torn_flesh_to_dogs'])
    if q == 'field_common_case':
        return cell('the_common_case_house_included', M, MK + "22:30: 'in the FIELD' = the ordinary case (the verse speaks of what is common — the method named on three "
                    "parallels), the house included by the carcass analogy; Mishnah Bava Kamma 5:7 applies the same rule to 23:4-5's 'ox or donkey'", ['torn_flesh_to_dogs'])
    if q == 'cannot_live':
        return cell('whatever_cannot_live_is_terefah', A, "Mishnah Chullin 3:1: the list — the pierced gullet, the severed windpipe, the pierced membrane... — and THIS IS THE "
                    "RULE: whatever cannot live is a terefah; Onkelos Exod 22:30: 'flesh torn from the living animal'", ['torn_flesh_to_dogs'])
    if q == 'fit_list':
        return cell('the_complement', A, "Mishnah Chullin 3:2: these are fit — the windpipe pierced or split up to an Italian issar, the skull broken without the membrane, the "
                    "liver with an olive left, the spleen and kidneys removed — the rule's complement", [FX.NONE])
    if q == 'to_the_dog':
        return cell('benefit_permitted', M, f"22:30 'TO THE DOG you shall throw it' — 'you shall throw' (תשלכון) at {c_throw} alone; " + MK + ": as the dog, so any benefit "
                    "(a fortiori from the carcass); Mishnah Kiddushin 2:9's no-benefit list does NOT name the terefah", ['torn_flesh_to_dogs'])
    if q == 'dogs_wage':
        return cell('not_a_dog_shall_whet_its_tongue', M, MK + "22:30: the dog's WAGE — 'not a dog shall whet its tongue' (Exod 11:7): 'the Holy One withholds no creature's reward'", ['torn_flesh_to_dogs'])
    if q == 'lashes':
        return cell('lashed', A, "Mishnah Makkot 3:2: the eaters of carcass, TEREFAH, detestables and swarmers among the flogged — the sanctions engine's carcass cell credited", ['lashes'])
    return cell('no_case', I, '', [FX.NONE])

# ---- F6: THE COURTS (23:1-9) ------------------------------------------
def courts(q):
    if q == 'false_report':
        return cell('hapax', I, f"23:1 'you shall not raise a FALSE REPORT (שמע שוא)' — the phrase at {c_false_report} alone; 'wicked' in Exodus at {c_wicked} — this verse "
                    "and 23:7, the chapter's own pair", ['false_report_barred'])
    if q == 'three_warnings':
        return cell(['receiver_of_slander', 'judge_hearing_one_alone', 'litigant_arguing_alone'], M, MK + "23:1: 'do not raise' as THREE warnings — the receiver of slander; "
                    "the judge not hearing one litigant before the other stands; the litigant not arguing to the judge alone (Deut 19:17's 'the two men shall stand'); Abba "
                    "Chanan: the judge's oath requires amen", ['false_report_barred'])
    if q == 'witness_of_violence':
        return cell('robbers_disqualified', M, f"23:1 'do not set your hand with the wicked to be a WITNESS OF VIOLENCE (עד חמס)' — the phrase at {c_violence}: this and Deut "
                    "19:16's scheming witness; " + MK + " (R. Natan): the violent and the robbers disqualified as witnesses; Mishnah Sanhedrin 3:3's list — the dice player, the "
                    "USURER (22:24's man), the pigeon flyer, the seventh-year trader", ['false_report_barred'])
    if q == 'oath_class':
        return cell('fit_not_disqualified', A, "Mishnah Shevuot 4:1: the oath of testimony applies to the fit and not the disqualified, to men not women, to the distant not the "
                    "relatives — the witness of violence outside the class", ['oath_imposed'])
    if q == 'majority_hapax':
        return cell('hapax', I, f"23:2 'you shall not follow AFTER THE MANY for evil... to tilt after the many' — 'after the many' at {c_many} alone, 'for evil' (לרעת) at "
                    f"{c_evil} alone, 'to tilt' (להטת) at {c_tilt} alone: the verse's three rare tokens", ['majority_decides'])
    if q == 'asymmetry':
        return cell('acquit_by_one_convict_by_two', M, MK + "23:2: 'you are not with them for evil but you ARE with them for good' — twelve acquit against eleven, acquitted; "
                    "thirteen convict against ten, convicted; eleven against twelve does not convict: 'execute by witnesses, execute by tilters — as witnesses are two, the "
                    "tilters are two'", ['majority_decides'])
    if q == 'twenty_three':
        return cell(23, A, "Mishnah Sanhedrin 1:6: the small court is twenty-three — a judging and a delivering congregation (Num 35:24-25), ten each; and three more from "
                    "'DO NOT FOLLOW THE MANY FOR EVIL': not for evil as for good — for good by one, for evil by two; no even court, so one added — THIS VERSE the arithmetic's "
                    "last term", ['majority_decides'])
    if q == 'one_vs_two':
        return cell('merit_by_one_liability_by_two', A, "Mishnah Sanhedrin 4:1: money cases tilt by one either way; capital cases tilt by ONE for merit and by TWO for liability; "
                    "reversed for merit, not for liability", ['majority_decides'])
    if q == 'begin_from_side':
        return cell('capital_from_the_side', A, "Mishnah Sanhedrin 4:2: purity cases begin from the greatest, CAPITAL CASES FROM THE SIDE — the link at 23:2's 'do not answer "
                    "on a case' read 'on the master' (the junior speaks first)", ['majority_decides'])
    if q == 'dissenter':
        return cell('bound_and_silent', A, "Mishnah Sanhedrin 3:7: the judge leaving may not say 'I acquitted and my colleagues convicted' — 'do not go talebearing' (Lev 19:16); "
                    "the majority's verdict is the court's own", ['majority_decides'])
    if q == 'onkelos_teaching':
        return cell('teach_what_you_see', M, "Onkelos Exod 23:2 expands the verse into three rulings: 'do not refrain from TEACHING what you see about the judgment; after the "
                    "many the judgment is completed'", ['majority_decides'])
    if q == 'poor_not_glorified':
        return cell('each_verse_its_referent', M, f"23:3 'and the POOR you shall not GLORIFY in his cause' — 'you shall not glorify' (תהדר) at {c_glorify}: this and Lev 19:15's "
                    "'you shall not glorify the great'; " + MK + "23:3: paired against Lev 19's 'you shall not favor the poor' — each verse takes a referent; the holiness "
                    f"engine's equal-treatment cell by call -> {HL_EQUAL!r} [IMPORT, live call]", ['judgment_perverted'])
    if q == 'enemy_ox':
        return cell('return_it', I, f"23:4 'if you MEET your enemy's ox or his donkey straying, you shall surely return it to him' — 'you shall meet' (תפגע) at {c_meet} "
                    f"(Jeremiah 7:16 the other); 'your enemy' (איבך) at {len(c_enemy)} seats; Deut 22:1-4 restates [IMPORT]", ['restores'])
    if q == 'who_is_enemy':
        return cell(['idolater', 'relapsed_convert', 'transgressor', 'son_after_a_quarrel'], M, MK + "23:4: who is 'your enemy' — the idolater (R. Yoshiyah), the relapsed "
                    "convert (R. Eliezer), the Israelite transgressor (R. Yitzchak), R. Natan's son after a quarrel — an enemy for the hour", [FX.NONE])
    if q == 'enemy_three_days':
        return cell('three_days_without_speech', A, "Mishnah Sanhedrin 3:5: the enemy — whoever has not spoken with him three days in enmity (a judge's disqualification; the "
                    "sages: Israel are not suspected as witnesses) — the enemy defined by a clock", [FX.NONE])
    if q == 'straying':
        return cell('outside_the_boundary', M, MK + "23:4: 'straying' = outside the boundary — Gen 37:15's straying Joseph the witness (the gen_60 ink cited)", ['restores'])
    if q == 'return_doubled':
        return cell('even_four_and_five_times', A, "Mishnah Bava Metzia 2:9: returned and it fled, returned and it fled, even four and five times — liable, 'RETURN, you shall "
                    "return' (Deut 22:1; this verse's doubled 'return, you shall return it' the same form)", ['restores'])
    if q == 'sign_and_claimant':
        return cell('signs_and_claimants', A, "Mishnah Bava Metzia 2:5: the garment went out to teach — whatever has SIGNS and CLAIMANTS must be announced; 2:1: sign-less "
                    "finds are the finder's", ['restores'])
    if q == 'deceiver':
        return cell('examine_the_claimant', A, "Mishnah Bava Metzia 2:7: the deceiver, even with the signs, not given — examine your brother whether he deceives; what works and "
                    "eats, works and eats; " + MK + "23:4's return ladder (near, far, unknown — announce, examine)", ['restores'])
    if q == 'announce_duration':
        return cell('R_Meir_neighbors_R_Yehuda_three_pilgrimages', A, "Mishnah Bava Metzia 2:6: until his neighbors know (R. Meir); three pilgrimages and seven days (R. Yehuda)", [FX.NONE])
    if q == 'common_case_animals':
        return cell('ox_or_donkey_names_the_common_case', A, "Mishnah Bava Kamma 5:7: ox and every beast alike for the return of the lost and the unloading; why 'ox or donkey'? "
                    "the verse speaks of the common case — the Mekhilta's method name (22:30) applied by the sheet", ['restores'])
    if q == 'lying_under':
        return cell('hapax', I, f"23:5 'if you see the donkey of one who hates you LYING UNDER ITS BURDEN' — the phrase at {c_burden} alone; 'one who hates you' (שנאך) at "
                    f"{c_hater} (Proverbs 25:21's 'if your enemy hungers' the other)", ['unloading_owed'])
    if q == 'unload_doubled':
        return cell('even_four_and_five_times', A, f"23:5 'UNLOAD, you shall unload with him' (עזב תעזב) at {c_unload} alone; Mishnah Bava Metzia 2:10: unloaded and it loaded, "
                    "even four and five times — liable, 'you shall surely unload'", ['unloading_owed'])
    if q == 'with_him':
        return cell('owner_idle_exempts', A, "Mishnah Bava Metzia 2:10: the owner went and sat, 'since the duty is on you, unload if you wish' — EXEMPT, 'WITH HIM'; old or "
                    "sick — liable; " + MK + "23:5: 'with him' — only if he shares the work", ['unloading_owed'])
    if q == 'measure':
        return cell('a_load_it_can_bear', A, "Mishnah Bava Metzia 2:10 (R. Yosei HaGelili): more than its load — not liable, 'UNDER its burden' = a load it can bear; " + MK +
                    ": 'lying' — not a habitual lier-down", ['unloading_owed'])
    if q == 'unload_load':
        return cell('unloading_torah_loading_disputed', A, "Mishnah Bava Metzia 2:10: unloading is a Torah duty, loading not (R. Shimon: loading too); " + MK + "23:5: R. Yoshiyah "
                    "both in 'unload'; R. Yehuda b. Beteira splits the verses; R. Yishmael: as unloading is Torah so loading", ['unloading_owed'])
    if q == 'ris':
        return cell('one_in_seven_and_a_half_of_a_mil', D, MK + "23:5: 'see' and 'meet' reconciled by MEASURE — the sages measured the RIS, one in seven and a half of a mil, as "
                    "the duty distance; the number is the data channel", [FX.NONE])
    if q == 'father_says_no':
        return cell('do_not_listen', A, "Mishnah Bava Metzia 2:10: his father said 'defile' or 'do not return' — he does not listen; " + MK + ": parents are themselves bound by "
                    "the commandments", ['unloading_owed'])
    if q == 'grudge':
        return cell('leave_what_is_in_your_heart', M, "Onkelos Exod 23:5: 'you shall surely LEAVE what is in your heart against him and unload with him' — the grudge released with "
                    "the load, inside the translation; " + MK + ": 'azov ta'azov' read both ways", ['unloading_owed'])
    if q == 'needy_in_his_cause':
        return cell('hapax_the_wicked_and_worthy_pair', I, f"23:6 'you shall not pervert the judgment of YOUR NEEDY in his cause' — 'your needy' (אבינך) at {c_needy} alone; 'pervert "
                    f"judgment' at {c_pervert} (Deut 16:19, 24:17); " + MK + "23:6-8: do not say 'he is wicked, I will tilt against him' — he is needy IN COMMANDMENTS, the "
                    "judgment stays straight", ['judgment_perverted'])
    if q == 'keep_far':
        return cell('hapax', I, f"23:7 'from a FALSE MATTER keep far' — the phrase at {c_falsehood} alone; " + MK + ": no ignorant colleague on the bench, no advocates beside "
                    "the judge, R. Natan: the warning against heresy", ['false_report_barred'])
    if q == 'no_retrial_acquitted':
        return cell('reversed_for_merit_not_for_liability', A, f"23:7 'and the INNOCENT and the RIGHTEOUS do not kill' — the pair at {c_innocent} alone; Mishnah Sanhedrin 4:1: "
                    "capital cases are reversed for merit, not for liability; " + MK + ": left guilty and merit found — retried; left acquitted — not ('for I will not acquit the "
                    "wicked' — Heaven's court reserved); Onkelos 23:7: 'one who went out ACQUITTED from the court you shall not kill'", ['false_report_barred'])
    if q == 'circumstantial':
        return cell('no_execution_without_witnesses', M, MK + "23:7: the averted-eyes case — the knife dripping and no witnesses, NO EXECUTION (Shimon b. Shetach's narrative and "
                    "the snake); single witnesses do not join across acts (one saw sun-worship, one moon-worship)", ['exempt'])
    if q == 'bribe':
        return cell(HL_BRIBE, P, f"23:8 'and a BRIBE you shall not take, for the bribe blinds the OPEN-EYED (פקחים) and twists the words of the righteous' — 'open-eyed' at "
                    f"{c_open_eyed} alone, the bribe noun's Torah seats {c_bribe}; Mishnah Peah 8:9 quotes this verse (the bribed judge's eyes dim): CALLED cold_run_holiness."
                    f"conduct(bribe) -> {HL_BRIBE!r} [IMPORT, live call]", ['bribe_barred', 'judgment_perverted'])
    if q == 'bribe_absolute':
        return cell('even_to_judge_truly', M, MK + "23:6-8: bribery absolute — even to judge truly; the taker's threefold blindness ladder (R. Natan: Torah confusion, dependence "
                    "on people, loss of eyesight)", ['bribe_barred'])
    if q == 'stranger_repeat':
        return cell(HB_STRANGERS, P, f"23:9 'and a stranger you shall not oppress, for you know THE SOUL OF THE STRANGER, for you were strangers in Egypt' — 'the soul of the "
                    f"stranger' at {c_soul_stranger} alone; the Mekhilta carries 23:9's content at 22:20 (no paragraph of its own); CALLED cold_run_holiness_b.convert_measures"
                    f"(you_were_strangers) -> {HB_STRANGERS!r} [IMPORT, live call]", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- F7: THE ESCORT AND THE LAND (23:20-33) ---------------------------
def land(q):
    if q == 'angel':
        return cell('hapax_the_Name_in_him', I, f"23:20 'behold I SEND AN ANGEL before you' — the phrase at {c_angel} alone; 23:21 'for My NAME IS IN HIM' at {c_name_in_him} "
                    "alone; Onkelos 23:21: 'for his WORD is in My name' — the verse re-seated on the Memra layer", [FX.NONE])
    if q == 'not_forgive':
        return cell('he_will_not_bear_your_transgression', I, f"23:21 'do not rebel against him, for he will NOT BEAR your transgression' — the phrase at {c_forgive}: this and "
                    "Joshua 24:19's 'He will not bear your transgression and your sins' — the same clause at the covenant's renewal", [FX.NONE])
    if q == 'hornet':
        return cell(3, I, f"23:28 'and I will send THE HORNET before you' — the token at {c_hornet}: this, Deut 7:20, Joshua 24:12 ('and I sent the hornet before you' — the run of "
                    "this promise in the Prophets)", [FX.NONE])
    if q == 'little_by_little':
        return cell('not_in_one_year', I, f"23:29-30 'I will not drive him out before you IN ONE YEAR, lest the land be desolate... LITTLE BY LITTLE I will drive him out' — 'little "
                    f"by little' at {c_little} (Deut 7:22 restates), 'in one year' at {c_one_year} (Solomon's gold the other two)", ['land_desolate'])
    if q == 'borders':
        return cell(['sea_of_reeds', 'sea_of_the_philistines', 'the_wilderness', 'the_river'], D, f"23:31 'I will set your border from the Sea of Reeds to the SEA OF THE "
                    f"PHILISTINES, and from the wilderness to the river' — 'sea of the Philistines' at {c_philistines} alone; the four terms are the data channel (the geography)", [FX.NONE])
    if q == 'no_bow':
        return cell('not_bow_not_serve_not_do', I, "23:24 'you shall not BOW to their gods nor SERVE them nor DO as their deeds' — three prohibitions; Onkelos: 'to their errors'", ['covenant_barred'])
    if q == 'break_pillars':
        return cell('demolish_demolish_break_break', I, f"23:24 'for you shall surely DEMOLISH them and surely BREAK their pillars' — 'demolish, demolish' at {c_demolish} alone; "
                    "Onkelos keeps both doubled verbs; Mishnah Avodah Zarah 3:1: the images' test (a staff, a bird, a ball — the sages)", ['demolished'])
    if q == 'serve_before':
        return cell('serve_before_the_LORD', M, "23:25 'and you shall SERVE the LORD your God' — Onkelos: 'serve BEFORE the LORD' (the service preposition), 'your food and "
                    "your drink' for bread and water", ['bread_and_water_blessed'])
    if q == 'bread_water':
        return cell('blessed_sickness_removed', I, "23:25 'and He will BLESS your bread and your water, and I will remove sickness from your midst' — the covenant's blessing side "
                    "(Lev 26:3-13 by name)", ['bread_and_water_blessed'])
    if q == 'no_barren':
        return cell('hapax', I, f"23:26 'there shall be no MISCARRYING (משכלה) or BARREN in your land; the number of your days I will fill' — 'miscarrying' at {c_miscarry} alone, "
                    f"'and barren' at {c_barren} (Deut 7:14 restates)", ['bread_and_water_blessed'])
    if q == 'no_covenant':
        return cell('no_covenant_with_them_or_their_gods', I, "23:32 'you shall not cut a COVENANT with them or with their gods' — Onkelos: 'no covenant with them or with their "
                    "ERRORS'; Exod 34:12-15, Deut 7:2 restate [IMPORT]", ['covenant_barred'])
    if q == 'not_dwell':
        return cell('lest_they_make_you_sin', I, f"23:33 'they shall not dwell in your land lest they make you SIN against Me... it will be a SNARE to you' — 'a snare' (למוקש) at "
                    f"{len(c_snare)} seats (34:12's covenant warning among them); Onkelos: 'they will make you LIABLE before Me' — liability vocabulary for 'sin'", ['covenant_barred'])
    if q == 'spine_silent':
        return cell('onkelos_alone', I, "the Mekhilta of Rabbi Yishmael's running text ENDS at 23:19 — the declared shelf over 23:20-33 is Onkelos alone (the reading ledger of "
                    "2026-09-01 recorded it); the cells above are ink and Onkelos", [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

# ---- (2) the answer sheet — the Mishnah rows as TEST DATA (verified by their own tokens) ----
def load(t):
    d = json.load(open((_ROOT + '/Data/mishnah_%s_he.json') % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
SHELF = {'Sanhedrin': load('sanhedrin'), 'Bava Metzia': load('bava_metzia'), 'Bekhorot': load('bekhorot'), 'Chullin': load('chullin'), 'Terumot': load('terumot'),
         'Middot': load('middot'), 'Shevuot': load('shevuot'), 'Avodah Zarah': load('avodah_zarah'), 'Peah': load('peah'), 'Kiddushin': load('kiddushin'),
         'Makkot': load('makkot'), 'Chagigah': load('chagigah'), 'Bava Kamma': load('bava_kamma')}
def mrow(book, ch, m, must):
    txt = strip(SHELF[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Sanhedrin', 1, 4, 'ושלשה'), ('Sanhedrin', 1, 6, 'לרעת'), ('Sanhedrin', 3, 3, 'ברבית'), ('Sanhedrin', 3, 5, 'באיבה'), ('Sanhedrin', 3, 7, 'רכיל'),
    ('Sanhedrin', 4, 1, 'לזכות'), ('Sanhedrin', 4, 2, 'הצד'), ('Sanhedrin', 7, 4, 'והמכשף'), ('Sanhedrin', 7, 5, 'השם'), ('Sanhedrin', 7, 6, 'הזובח'), ('Sanhedrin', 7, 8, 'בכנוי'), ('Sanhedrin', 7, 11, 'מעשה'),
    ('Bava Metzia', 2, 1, 'שלו'), ('Bava Metzia', 2, 5, 'השמלה'), ('Bava Metzia', 2, 6, 'שכניו'), ('Bava Metzia', 2, 7, 'והרמאי'), ('Bava Metzia', 2, 9, 'תשיבם'), ('Bava Metzia', 2, 10, 'תעזב'),
    ('Bava Metzia', 5, 1, 'נשך'), ('Bava Metzia', 5, 6, 'ברזל'), ('Bava Metzia', 5, 11, 'כנשה'), ('Bava Metzia', 9, 13, 'אלמנה'), ('Bava Metzia', 4, 10, 'תונה'),
    ('Bekhorot', 8, 1, 'לנחלה'), ('Bekhorot', 8, 2, 'דפן'), ('Bekhorot', 8, 6, 'שלשים'), ('Bekhorot', 8, 7, 'סלעים'), ('Bekhorot', 8, 8, 'בעבדים'),
    ('Chullin', 3, 1, 'טרפות'), ('Chullin', 3, 2, 'כשרות'), ('Terumot', 3, 6, 'לבכורים'), ('Terumot', 3, 7, 'בכורים'),
    ('Middot', 3, 1, 'ושתים'), ('Middot', 3, 3, 'וכבש'), ('Middot', 3, 4, 'ברזל'), ('Shevuot', 4, 1, 'בנשים'), ('Shevuot', 4, 13, 'המקלל'),
    ('Avodah Zarah', 3, 1, 'הצלמים'), ('Peah', 8, 9, 'אמת'), ('Kiddushin', 2, 9, 'חמור'), ('Makkot', 3, 2, 'טרפות'), ('Chagigah', 3, 8, 'כקרקע'), ('Bava Kamma', 5, 7, 'בהוה'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows verified by their own tokens (Sanhedrin 1, 3, 4, 7, Bava Metzia 2, 5, Bekhorot 8, Chullin 3, Terumot 3, Middot 3, Shevuot 4 read whole — the topic docket)' % len(SHEET))

# ---- THE WRAP (W1 THE EXODUS LAW, D9-iii, 2026-09-07) — the daemon and the scene --------------
# Twenty-one case heads of the four spans (20:22-26, 22:17-30, 23:1-9, 23:20-33), each a case-form
# type of event_vocabulary.yaml with its witness in the ink; the daemon takes the decalogue runner's
# altar rule at its call site (altar_rules is WRAPPED here — one function, two seats). It writes the
# ledger and never emits an event; the sunset pledge, the firstborn's thirty days, and the firstling's
# eighth day are TIMERS; the gradual conquest holds the land's desolation flag OFF.
import world_engine as WE
def law_ordinances(event, world):
    """Exod 20:22-26, 22:17-30, 23:1-9, 23:20-33 (cold_run_ordinances.py F1-F9)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'altar_built':
        if event['stones'] == 'hewn':
            return [E_('disqualified', event['builder'], value='iron_touched_stone', law="F1 [INK 20:25 'you shall not build them hewn... and profaned it'; CALLED cold_run_decalogue.altar_rules(hewn_stones) -> %s; Mishnah Middot 3:4]" % DEC_HEWN)]
        return [E_('accepted', event['builder'], cp='HEAVEN', value=event['stones'], law="F1 [INK 20:24 'in every place where I cause My name to be mentioned I will come to you and bless you']")]
    if k == 'offered_on_altar':
        if event['offering'] == 'olah':
            return [E_('smoked_to_the_lord', event['offerer'], cp='HEAVEN', value=OLAH_F['disposition']['v'], law="F1 [INK 20:24 'your burnt offerings'; CALLED cold_run_offerings.dispatch(olah:flock)]")]
        return [E_('eating_window', event['offerer'], value=SHEL['window']['v'], law="F1 [INK 20:24 'your peace offerings'; CALLED cold_run_offerings.dispatch(shelamim) -> the window]")]
    if k == 'sorcery_done':
        if event['deed']:
            return [E_('stoned', event['doer'], law="F2 [INK 22:17 'you shall not let live'; Mishnah Sanhedrin 7:4: the sorcerer stoned]")]
        return [E_('exempt', event['doer'], value='deceiver_of_the_eyes', law='F2 [Mishnah Sanhedrin 7:11: the doer of a deed liable, the deceiver of the eyes exempt]')]
    if k == 'lay_with_beast':
        return [E_('put_to_death', event['doer'], value='stoning', law="F2 [INK 22:18 'shall surely be put to death'; Mishnah Sanhedrin 7:4; the beast by twenty-three, 1:4 — CALLED cold_run_sanctions.beast]")]
    if k == 'sacrificed_to_gods':
        return [E_('put_to_death', event['doer'], value=event['service'], law="F2 [INK 22:19 'shall be devoted... save to the LORD alone'; Mishnah Sanhedrin 7:6: the idolater's row]")]
    if k == 'stranger_wronged':
        if event['cried']:
            return [E_('cry_heard', event['victim'], cp='HEAVEN', value=event['victim_class'], law="F3 [INK 22:22 'if he cries at all to Me, I will surely hear his cry']"),
                    E_('put_to_death', event['wronger'], cp='HEAVEN', value='by_the_sword', law="F3 [INK 22:23 'My anger will burn and I will kill you with the sword' — measure for measure, Mekhilta]")]
        return [E_('exempt', event['wronger'], value='wronging_by_words', law='F3 [Mishnah Bava Metzia 4:10: wronging by words — no court remedy; the Heaven clause stands]')]
    if k == 'silver_lent':
        return [E_('interest_barred', event['lender'], cp=event['borrower'], value=bool(event.get('interest')), law="F4 [INK 22:24 'you shall not lay upon him interest'; Mishnah Bava Metzia 5:1, 5:11; CALLED cold_run_yovel.interest]")]
    if k == 'garment_pledged':
        return [E_('pledge_returned_by_sunset', event['creditor'], cp=event['debtor'], due=event['day'] + 1, value=event['garment'], law="F4 [INK 22:25 'until the sun sets you shall return it to him' — the TIMER; Mishnah Bava Metzia 9:13]"),
                E_('cry_heard', event['debtor'], cp='HEAVEN', law="F4 [INK 22:26 'when he cries to Me, I will hear, for I am gracious']")]
    if k == 'god_or_ruler_cursed':
        if event['by_name']:
            return [E_('lashes', event['curser'], value=event['target'], law="F5 [INK 22:27 'a judge you shall not curse, and a ruler among your people you shall not execrate'; Mishnah Shevuot 4:13: by the Name; the four liabilities, Mekhilta]")]
        return [E_('exempt', event['curser'], value='euphemism', law='F5 [Mishnah Shevuot 4:13: by a euphemism — R. Meir liable, the sages exempt; Mishnah Sanhedrin 7:8]')]
    if k == 'fullness_delayed':
        return [E_('gift_order_barred', event['farmer'], value=event['separated_first'], law="F5 [INK 22:28 'your fullness and your outflow you shall not delay'; Mishnah Terumot 3:6-7: the order]")]
    if k == 'firstborn_son':
        return [E_('consecrated_firstborn', event['son'], cp=event['father'], law="F5 [INK 22:28 'the firstborn of your sons you shall give to Me'; Mishnah Bekhorot 8:1; CALLED cold_run_pesach.firstborn(human)]"),
                E_('due_to_priest', event['father'], cp='any-priest', amount=5, due=event['day'] + 30, law='F5 [Mishnah Bekhorot 8:7-8: five sela to any priest; Num 18:16 after thirty days — the TIMER]')]
    if k == 'firstling_born':
        if event['animal'] == 'donkey':
            return [E_('redeem_or_break', event['owner'], value=PS_DONKEY, law="F6 [CALLED cold_run_pesach.firstborn(donkey) -> %r; INK 13:13]" % PS_DONKEY)]
        return [E_('eighth_day_fit', event['owner'], due=event['day'] + 7, value=event['animal'], law="F6 [INK 22:29 'seven days it shall be with its mother; on the eighth day you shall give it to Me'; Lev 22:27 the second seat — one TIMER]"),
                E_('accepted', event['owner'], cp='HEAVEN', due=event['day'] + 7, law="F6 [Lev 22:27 'from the eighth day and onward it is accepted']")]
    if k == 'flesh_torn':
        out = [E_('torn_flesh_to_dogs', event['owner'], cp='the-dog', law="F7 [INK 22:30 'to the dog you shall throw it' — the dog's wage, Mekhilta; Mishnah Chullin 3:1]")]
        if event.get('eaten'):
            out.append(E_('lashes', event['owner'], value='ate_the_torn', law='F7 [Mishnah Makkot 3:2: the eater of the torn lashed]'))
        return out
    if k == 'false_report_carried':
        return [E_('false_report_barred', event['judge'], cp=event['party'], law="F8 [INK 23:1 'you shall not carry a false report'; Sanhedrin 7b: the judge hears no party alone; Mishnah Sanhedrin 3:7]")]
    if k == 'court_split':
        a, c = event['for_acquittal'], event['for_conviction']
        verdict = 'convicted' if (c - a >= 2 if event['capital'] else c > a) else 'acquitted'
        return [E_('majority_decides', event['court'], value=verdict, law="F8 [INK 23:2 'after the many to incline' against 'not after the many for evil'; Mishnah Sanhedrin 4:1: acquittal by one, conviction by two]")]
    if k == 'enemys_animal_met':
        return [E_('restores', event['finder'], cp=event['owner'], value=event['animal'], law="F8 [INK 23:4 'you shall surely return it to him'; Mishnah Bava Metzia 2:9: even a hundred times]")]
    if k == 'donkey_under_burden':
        if event['owner_helps']:
            return [E_('unloading_owed', event['passerby'], cp=event['owner'], law="F8 [INK 23:5 'you shall surely unload WITH HIM'; Mishnah Bava Metzia 2:10]")]
        return [E_('exempt', event['passerby'], value='the_owner_sat_by', law="F8 [Mishnah Bava Metzia 2:10: the owner went and sat and said 'you do it' — exempt: 'with him']")]
    if k == 'acquitted_retried':
        return [E_('exempt', event['accused'], cp=event['court'], value='never_retried', law="F8 [INK 23:7 'the innocent and the righteous you shall not slay'; Sanhedrin 33b; Mishnah Sanhedrin 4:1: reversed to acquittal, never to conviction]")]
    if k == 'bribe_offered':
        return [E_('bribe_barred', event['judge'], cp=event['giver'], law="F8 [INK 23:8 'a bribe you shall not take'; Ketubot 105a: even to judge truly; CALLED cold_run_holiness.conduct(bribe)]"),
                E_('judgment_perverted', event['judge'], cp='HEAVEN', law="F8 [INK 23:6 'you shall not pervert the judgment of your needy'; Mishnah Peah 8:9]")]
    if k == 'entered_the_land':
        return [E_('demolished', 'their-pillars', cp=event['people'], law="F9 [INK 23:24 'you shall surely demolish them and surely break their pillars'; Mishnah Avodah Zarah 3:1]"),
                E_('covenant_barred', event['people'], law="F9 [INK 23:32 'you shall not cut a covenant with them or with their gods']"),
                E_('land_desolate', 'the-land', value=False, law="F9 [INK 23:29-30 'not in one year, lest the land become desolate... little by little' — the flag held OFF by the gradual driving-out]")]
    if k == 'served_the_lord':
        return [E_('bread_and_water_blessed', event['people'], cp='HEAVEN', law="F9 [INK 23:25 'and He will bless your bread and your water, and I will remove sickness from your midst']")]
    return []

def scene():
    """THE SCENE — the recorded cases replayed on the world engine (clock unit: days; the answer sheet's rows as the tape)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the ordinances: Sanhedrin, Bava Metzia, Bekhorot, Chullin, Terumot, Middot, Shevuot on the engine (clock unit: days)')
        w.laws = [law_ordinances]
        w.advance(1)
        w.submit({'kind': 'altar_built', 'subject': 'the-builder', 'builder': 'the-builder', 'stones': 'hewn', 'case_source': 'Mishnah Middot 3:4 — iron touched the stone'})
        w.submit({'kind': 'altar_built', 'subject': 'the-builder', 'builder': 'the-builder', 'stones': 'whole', 'case_source': 'Mishnah Middot 3:4 — whole stones from Beit Kerem'})
        w.submit({'kind': 'offered_on_altar', 'subject': 'the-offerer', 'offerer': 'the-offerer', 'offering': 'olah', 'case_source': 'Exod 20:24 — the burnt offering on it'})
        w.submit({'kind': 'offered_on_altar', 'subject': 'the-offerer', 'offerer': 'the-offerer', 'offering': 'shelamim', 'case_source': 'Exod 20:24 — the peace offering on it'})
        w.advance(2)
        w.submit({'kind': 'sorcery_done', 'subject': 'the-sorcerer', 'doer': 'the-sorcerer', 'deed': True, 'case_source': 'Mishnah Sanhedrin 7:4, 7:11 — the doer of a deed'})
        w.submit({'kind': 'sorcery_done', 'subject': 'the-illusionist', 'doer': 'the-illusionist', 'deed': False, 'case_source': 'Mishnah Sanhedrin 7:11 — the deceiver of the eyes'})
        w.submit({'kind': 'lay_with_beast', 'subject': 'the-bestialist', 'doer': 'the-bestialist', 'case_source': 'Mishnah Sanhedrin 7:4'})
        w.submit({'kind': 'sacrificed_to_gods', 'subject': 'the-idolater', 'doer': 'the-idolater', 'service': 'sacrifices', 'case_source': "Mishnah Sanhedrin 7:6 — the idolater's row"})
        w.advance(3)
        w.submit({'kind': 'stranger_wronged', 'subject': 'the-oppressor', 'wronger': 'the-oppressor', 'victim': 'the-widow', 'victim_class': 'widow', 'cried': True, 'case_source': 'Mekhilta 22:22-23 — the cry heard, measure for measure'})
        w.submit({'kind': 'stranger_wronged', 'subject': 'the-word-wronger', 'wronger': 'the-word-wronger', 'victim': 'the-stranger', 'victim_class': 'stranger', 'cried': False, 'case_source': 'Mishnah Bava Metzia 4:10 — wronging by words'})
        w.submit({'kind': 'silver_lent', 'subject': 'the-lender', 'lender': 'the-lender', 'borrower': 'the-poor-man', 'interest': True, 'case_source': 'Mishnah Bava Metzia 5:1 — the bite'})
        w.submit({'kind': 'garment_pledged', 'subject': 'the-creditor', 'creditor': 'the-creditor', 'debtor': 'the-debtor', 'garment': 'day-garment', 'day': 3, 'case_source': 'Mishnah Bava Metzia 9:13 — returned by sunset'})
        w.advance(4)                                              # the sun sets: the pledge timer FIRES
        w.advance(5)
        w.submit({'kind': 'god_or_ruler_cursed', 'subject': 'the-curser', 'curser': 'the-curser', 'target': 'ruler', 'by_name': True, 'case_source': 'Mishnah Shevuot 4:13 — by the Name'})
        w.submit({'kind': 'god_or_ruler_cursed', 'subject': 'the-euphemist', 'curser': 'the-euphemist', 'target': 'judge', 'by_name': False, 'case_source': 'Mishnah Shevuot 4:13 — by a euphemism, the sages exempt'})
        w.submit({'kind': 'fullness_delayed', 'subject': 'the-farmer', 'farmer': 'the-farmer', 'separated_first': 'terumah-before-first-fruits', 'case_source': 'Mishnah Terumot 3:6 — the order'})
        w.submit({'kind': 'firstborn_son', 'subject': 'the-father', 'father': 'the-father', 'son': 'the-son', 'day': 5, 'case_source': 'Mishnah Bekhorot 8:7-8 — five sela after thirty days'})
        w.submit({'kind': 'firstling_born', 'subject': 'the-herdsman', 'owner': 'the-herdsman', 'animal': 'sheep', 'day': 5, 'case_source': 'Exod 22:29 + Lev 22:27 — the eighth day'})
        w.submit({'kind': 'firstling_born', 'subject': 'the-herdsman', 'owner': 'the-herdsman', 'animal': 'donkey', 'day': 5, 'case_source': 'Exod 13:13 — the donkey redeemed or its neck broken'})
        w.submit({'kind': 'flesh_torn', 'subject': 'the-eater', 'owner': 'the-eater', 'eaten': True, 'case_source': 'Mishnah Chullin 3:1 + Makkot 3:2 — the torn, eaten'})
        w.advance(6)
        w.submit({'kind': 'false_report_carried', 'subject': 'the-judge', 'judge': 'the-judge', 'party': 'the-litigant', 'case_source': 'Sanhedrin 7b — one party heard alone'})
        w.submit({'kind': 'court_split', 'subject': 'the-court', 'court': 'the-court', 'for_acquittal': 11, 'for_conviction': 12, 'capital': True, 'case_source': 'Mishnah Sanhedrin 4:1 — conviction needs a majority of two'})
        w.submit({'kind': 'court_split', 'subject': 'the-court', 'court': 'the-court', 'for_acquittal': 10, 'for_conviction': 13, 'capital': True, 'case_source': 'Mishnah Sanhedrin 4:1 — thirteen against ten'})
        w.submit({'kind': 'court_split', 'subject': 'the-court', 'court': 'the-court', 'for_acquittal': 11, 'for_conviction': 12, 'capital': False, 'case_source': 'Mishnah Sanhedrin 4:1 — a money case by a majority of one'})
        w.submit({'kind': 'enemys_animal_met', 'subject': 'the-finder', 'finder': 'the-finder', 'owner': 'his-enemy', 'animal': 'ox', 'case_source': 'Mishnah Bava Metzia 2:9 — returning'})
        w.submit({'kind': 'donkey_under_burden', 'subject': 'the-passerby', 'passerby': 'the-passerby', 'owner': 'the-hater', 'owner_helps': True, 'case_source': 'Mishnah Bava Metzia 2:10 — with him'})
        w.submit({'kind': 'donkey_under_burden', 'subject': 'the-second-passerby', 'passerby': 'the-second-passerby', 'owner': 'the-hater', 'owner_helps': False, 'case_source': 'Mishnah Bava Metzia 2:10 — the owner sat by'})
        w.submit({'kind': 'acquitted_retried', 'subject': 'the-court', 'court': 'the-court', 'accused': 'the-accused', 'case_source': 'Mishnah Sanhedrin 4:1 + Sanhedrin 33b — never retried'})
        w.submit({'kind': 'bribe_offered', 'subject': 'the-judge', 'judge': 'the-judge', 'giver': 'the-litigant', 'case_source': 'Mishnah Peah 8:9 + Ketubot 105a — the bribe'})
        w.advance(7)
        w.submit({'kind': 'entered_the_land', 'subject': 'israel', 'people': 'israel', 'year': 7, 'case_source': 'Exod 23:23-33 + Mishnah Avodah Zarah 3:1 — the entry'})
        w.submit({'kind': 'served_the_lord', 'subject': 'israel', 'people': 'israel', 'case_source': 'Exod 23:25 — served before the LORD (Onkelos)'})
        w.advance(40)                                             # the eighth day (12) and the thirty days (35) pass: the timers FIRE
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    vals = lambda eid, eff: tuple(e['value'] for e in w.entity(eid).ledger if e['effect'] == eff)
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-builder', 'disqualified'), n('the-builder', 'accepted'), n('the-offerer', 'smoked_to_the_lord'), n('the-offerer', 'eating_window'),
            n('the-sorcerer', 'stoned'), n('the-illusionist', 'exempt'), n('the-bestialist', 'put_to_death'), n('the-idolater', 'put_to_death'),
            n('the-widow', 'cry_heard'), n('the-oppressor', 'put_to_death'), n('the-word-wronger', 'exempt'), n('the-lender', 'interest_barred'),
            n('the-creditor', 'pledge_returned_by_sunset'), n('the-debtor', 'cry_heard'),
            n('the-curser', 'lashes'), n('the-euphemist', 'exempt'), n('the-farmer', 'gift_order_barred'), n('the-son', 'consecrated_firstborn'), n('the-father', 'due_to_priest'),
            n('the-herdsman', 'eighth_day_fit'), n('the-herdsman', 'accepted'), n('the-herdsman', 'redeem_or_break'), n('the-eater', 'torn_flesh_to_dogs'), n('the-eater', 'lashes'),
            n('the-judge', 'false_report_barred'), vals('the-court', 'majority_decides'), n('the-finder', 'restores'), n('the-passerby', 'unloading_owed'), n('the-second-passerby', 'exempt'),
            n('the-accused', 'exempt'), n('the-judge', 'bribe_barred'), n('the-judge', 'judgment_perverted'),
            n('their-pillars', 'demolished'), n('israel', 'covenant_barred'), n('the-land', 'land_desolate'), w.entity('the-land').status.get('land_desolate'), n('israel', 'bread_and_water_blessed'),
            tset, fired, w.clock.day), w
SCENE, _W = scene()

TESTS = [
 # ---- THE ALTAR LAW (20:19-26) ----
 ('Exod 20:22 — "from heaven I spoke" a hapax', altar('from_heaven'), 'hapax'),
 ('Exod 20:23 — no gods of silver or gold (a hapax phrase)', altar('silver_gold'), 'no_gods_of_silver_or_gold'),
 ('Mishnah Chagigah 3:8 — the altar of earth is like the ground', altar('earth_altar'), 'attached_to_the_ground'),
 ('Exod 20:24 — the burnt offering on it (offerings engine by call)', altar('olah_on_it'), 'wholly_to_fires'),
 ('Exod 20:24 — the peace offering on it (by call)', altar('shelamim_on_it'), 'two_days_one_night'),
 ('Exod 20:24 — "in every place... I cause My name to be mentioned" (two hapaxes)', altar('every_place'), 'hapax_the_name_mentioned'),
 ('Exod 20:25 — hewn: the decalogue runner\'s altar rule by call', altar('hewn'), 'iron-touched stone disqualified'),
 ('Exod 20:25 — the sword profanes (a hapax)', altar('sword_profanes'), 'iron_profanes_by_touch'),
 ('Zevachim 54a:8 — the build recipe by call', altar('recipe'), 'whole stones, frame and lime'),
 ('Mishnah Middot 3:4 — whole stones from Beit Kerem', altar('stones_source'), 'whole_stones_from_beit_kerem_valley'),
 ('Exod 20:26 — steps: the decalogue runner\'s rule by call', altar('steps'), 'a ramp; and temperance beside it'),
 ('Mishnah Middot 3:3 — the ramp\'s measures (data)', altar('ramp'), 'thirty_two_by_sixteen_south'),
 ('Exod 20:26 — the nakedness clause, the ramp\'s reason', altar('nakedness'), 'the_ramps_reason'),
 ('Mekhilta 22:24 — "if an altar of stones" one of three obligatory ifs', altar('obligatory_if'), 'one_of_three_obligatory_ifs'),
 # ---- THE CAPITAL TRIAD (22:17-19) ----
 ('Mekhilta 22:17 — the sorceress: man and woman alike', capital('sorceress_gender'), 'man_and_woman_alike'),
 ('Mishnah Sanhedrin 7:4 — the sorcerer stoned (the Mekhilta\'s three arms)', capital('sorceress_mode'), 'stoning'),
 ('Mishnah Sanhedrin 7:11 — the doer liable, the deceiver of eyes exempt', capital('sorceress_deed'), 'doer_liable_deceiver_exempt'),
 ('Mekhilta 22:17 — the warning at Deut 18:10', capital('sorceress_warning'), 'Deut_18_10'),
 ('Exod 22:18 — the beast: the sanctions engine holds this verse as the passive\'s warning (by call)', capital('beast_mode'), 'Exod_22:18_freed_to_the_passive'),
 ('Mishnah Sanhedrin 1:4 — the beast\'s court of twenty-three (by call)', capital('beast_court'), 23),
 ('the woman\'s warning (by call)', capital('beast_woman'), '18:23_a_woman_shall_not_stand_before_a_beast'),
 ('Exod 22:19 — "devoted" at four Tanakh seats', capital('devoted_seats'), 4),
 ('Mekhilta 22:19 — the service architecture: Temple services for any idol', capital('service_architecture'), 'temple_services_for_any_idol'),
 ('Mishnah Sanhedrin 7:6 — the idolater\'s row', capital('idolater_row'), 'serves_sacrifices_incense_libation_bows_accepts_says'),
 ('Exod 22:19 — "save to the LORD alone"; the tent door by call', capital('only_to_the_LORD'), 'save_to_the_LORD_alone'),
 ('Mekhilta 22:19 — joining His name with another', capital('joining'), 'R_Shimon_b_Yochai_liable'),
 # ---- THE STRANGER, THE WIDOW, THE ORPHAN (22:20-23) ----
 ('Exod 22:20 — wrong / oppress each a hapax', stranger('two_verbs'), 'wrong_hapax_oppress_hapax'),
 ('Mishnah Bava Metzia 4:10 — wronging by words (holiness_b by call)', stranger('words_vs_money'), 'yesterday_an_idolater_banned'),
 ('Exod 22:20 / 23:9 — "you were strangers" at four seats (by call)', stranger('you_were_strangers'), 'know_the_strangers_soul_from_your_own'),
 ('the stranger\'s Lev 19 seats (by call)', stranger('ger_seats'), [10, 33, 34]),
 ('Mekhilta 22:20 — the beloved converts census', stranger('beloved_census'), 'every_title_israel_carries'),
 ('Mekhilta 22:21 — the scope fork: R. Yishmael all / R. Akiva the named', stranger('widow_orphan_scope'), 'R_Yishmael_all_persons_R_Akiva_the_named'),
 ('Mekhilta 22:21-23 — one affliction is liability', stranger('one_affliction'), 'one_affliction_is_liability'),
 ('Exod 22:22 — three doubled verbs', stranger('cry_doubled'), 'cry_cry_hear_hear'),
 ('Exod 22:23 — measure for measure', stranger('measure_for_measure'), 'wives_widows_sons_orphans'),
 # ---- THE LOAN, THE INTEREST, THE PLEDGE (22:24-26) ----
 ('Mekhilta 22:24 — "if" is obligation', loan('im_obligation'), 'lending_is_obligation'),
 ('Mekhilta 22:24 — the priority ladder', loan('priority_ladder'), ['my_people_before_gentile', 'poor_before_rich', 'your_poor_before_your_city', 'your_city_before_another']),
 ('Exod 22:24 — "as a creditor" (two Tanakh seats)', loan('creditor_manner'), 'not_seen_at_all_times'),
 ('Exod 22:24 — the bite noun at four Torah seats', loan('bite_noun'), 4),
 ('Lev 25:36-37 — the two nouns (jubilee engine by call)', loan('interest_spec'), 'barred'),
 ('Mishnah Bava Metzia 5:6 — the foreigner (by call)', loan('foreigner'), 'permitted'),
 ('Mishnah Bava Metzia 5:11 — the five prohibitions, two of them this verse\'s', loan('five_prohibitions'), ['lo_titen_Lev_25_37', 'al_tikach_Lev_25_36', 'ke_nosheh_Exod_22_24', 'neshekh_Exod_22_24', 'lifnei_iver_Lev_19_14']),
 ('Mishnah Bava Metzia 5:11 — who transgresses', loan('who_transgresses'), ['lender', 'borrower', 'guarantor', 'witnesses']),
 ('Exod 22:25 — "until the sun sets" (with Exod 17:12 alone)', loan('pledge_sunset'), 'until_the_sun_sets'),
 ('Mekhilta 22:25-26 — day garment by day, night garment by night', loan('day_night_garments'), 'day_garment_by_day_night_garment_by_night'),
 ('Mishnah Bava Metzia 9:13 — only through the court', loan('court_only'), 'only_through_the_court_outside_you_stand'),
 ('Mishnah Bava Metzia 9:13 — the widow never pledged', loan('widow_not_pledged'), 'never_pledged_rich_or_poor'),
 ('Mekhilta 22:26 — the covering tokens', loan('covering_tokens'), 'cloak_shirt_mattress'),
 ('Exod 22:26 — "for I am gracious" a hapax', loan('gracious'), 'hapax'),
 # ---- THE CURSE, THE GIFTS, THE FIRSTBORN (22:27-28) ----
 ('Mekhilta 22:27 — elohim: judge or blasphemy\'s warning', gifts('elohim_fork'), 'R_Yishmael_judge_R_Akiva_blasphemy_warning'),
 ('Lev 19:14 — the curse verb\'s other seat (holiness engine by call)', gifts('curse_verb_seats'), 'all_your_people_the_deaf_carves_the_living'),
 ('Mishnah Sanhedrin 7:5, 7:8; Shevuot 4:13 — the Name gate', gifts('name_gate'), 'liable_only_by_the_Name'),
 ('Mekhilta 22:27 — four liabilities in one utterance', gifts('four_liabilities'), 4),
 ('Mekhilta 22:27 — "among your people"', gifts('among_your_people'), 'while_they_act_by_your_peoples_way'),
 ('Exod 22:28 — fullness and outflow (two hapaxes) = first fruits and terumah', gifts('fullness_outflow'), 'first_fruits_and_terumah'),
 ('Mekhilta 22:28 — "do not delay" = do not reorder', gifts('delay_is_reorder'), 'do_not_reorder'),
 ('Mishnah Terumot 3:6 — the act stands though forbidden (this verse quoted)', gifts('order_sheet'), 'act_stands_though_forbidden'),
 ('Mishnah Terumot 3:7 — the count of names', gifts('names_count'), [4, 3, 2, 1]),
 ('Exod 22:28 — the firstborn son (Passover engine by call)', gifts('firstborn_son'), 'redeem (five sela — fetched constant)'),
 ('Mishnah Bekhorot 8:7 — five sela (data)', gifts('five_sela'), 'five_sela_tyrian_maneh'),
 ('Mishnah Bekhorot 8:6 — day thirty is the edge', gifts('thirty_days'), 'day_thirty_is_the_edge'),
 ('Mekhilta 22:29 / Bekhorot 8:1 — stillbirths open the womb for both', gifts('stillbirth'), 'stillbirths_open_the_womb_for_both'),
 ('Mishnah Bekhorot 8:2 — the Caesarean (Passover engine by call)', gifts('caesarean'), 'not consecrated'),
 ('Mekhilta 22:29 — valid to any priest anywhere', gifts('to_any_priest'), 'valid_to_any_priest_anywhere'),
 # ---- THE FIRSTLING'S EIGHTH DAY (22:29) — the callee the priesthood owed ----
 ('Exod 22:29 — "on the eighth day you shall give" a hapax', firstling('run_phrase'), 'hapax'),
 ('Exod 22:29 WITH its mother vs Lev 22:27 UNDER its mother (each a hapax)', firstling('with_its_mother'), 'with_not_under'),
 ('Mekhilta 22:29 — the eighth and onward (the priesthood runner fetches this)', firstling('eighth_and_onward'), 'on_the_eighth_day_and_onward'),
 ('Mekhilta 22:29 — nursed from common funds', firstling('nursed_from_chullin'), 'nursed_from_common_funds'),
 ('Exod 13:13 — the donkey by call', firstling('donkey_by_call'), 'redeem with a lamb, else break the neck'),
 ('one timer at two seats', firstling('two_seats_one_timer'), {'exod_22_29': 'on_the_eighth_day', 'lev_22_27': 'from_the_eighth_day_onward'}),
 # ---- THE TORN FLESH (22:30) ----
 ('Exod 22:30 — "men of holiness" a hapax phrase', torn('holy_men'), 'hapax'),
 ('"torn" at four Tanakh seats (Jacob\'s first)', torn('torn_seats'), 4),
 ('Mekhilta 22:30 — "in the field" the common case', torn('field_common_case'), 'the_common_case_house_included'),
 ('Mishnah Chullin 3:1 — whatever cannot live is a terefah', torn('cannot_live'), 'whatever_cannot_live_is_terefah'),
 ('Mishnah Chullin 3:2 — the fit list', torn('fit_list'), 'the_complement'),
 ('Exod 22:30 — to the dog: benefit permitted (Kiddushin 2:9 silent)', torn('to_the_dog'), 'benefit_permitted'),
 ('Mekhilta 22:30 — the dog\'s wage', torn('dogs_wage'), 'not_a_dog_shall_whet_its_tongue'),
 ('Mishnah Makkot 3:2 — the terefah eater lashed', torn('lashes'), 'lashed'),
 # ---- THE COURTS (23:1-9) ----
 ('Exod 23:1 — "a false report" a hapax; "wicked" twice in Exodus', courts('false_report'), 'hapax'),
 ('Mekhilta 23:1 — three warnings', courts('three_warnings'), ['receiver_of_slander', 'judge_hearing_one_alone', 'litigant_arguing_alone']),
 ('Exod 23:1 / Deut 19:16 — the witness of violence; Sanhedrin 3:3\'s list', courts('witness_of_violence'), 'robbers_disqualified'),
 ('Mishnah Shevuot 4:1 — the fit, not the disqualified', courts('oath_class'), 'fit_not_disqualified'),
 ('Exod 23:2 — three rare tokens', courts('majority_hapax'), 'hapax'),
 ('Mekhilta 23:2 — the asymmetric majority', courts('asymmetry'), 'acquit_by_one_convict_by_two'),
 ('Mishnah Sanhedrin 1:6 — twenty-three from this verse', courts('twenty_three'), 23),
 ('Mishnah Sanhedrin 4:1 — merit by one, liability by two', courts('one_vs_two'), 'merit_by_one_liability_by_two'),
 ('Mishnah Sanhedrin 4:2 — capital cases begin from the side', courts('begin_from_side'), 'capital_from_the_side'),
 ('Mishnah Sanhedrin 3:7 — the dissenter bound and silent', courts('dissenter'), 'bound_and_silent'),
 ('Onkelos Exod 23:2 — teach what you see', courts('onkelos_teaching'), 'teach_what_you_see'),
 ('Exod 23:3 / Lev 19:15 — "you shall not glorify" at two seats; the holiness engine by call', courts('poor_not_glorified'), 'each_verse_its_referent'),
 ('Exod 23:4 — the enemy\'s ox returned', courts('enemy_ox'), 'return_it'),
 ('Mekhilta 23:4 — who is your enemy (four readings)', courts('who_is_enemy'), ['idolater', 'relapsed_convert', 'transgressor', 'son_after_a_quarrel']),
 ('Mishnah Sanhedrin 3:5 — the enemy by a three-day clock', courts('enemy_three_days'), 'three_days_without_speech'),
 ('Mekhilta 23:4 — straying = outside the boundary (Gen 37:15)', courts('straying'), 'outside_the_boundary'),
 ('Mishnah Bava Metzia 2:9 — even four and five times', courts('return_doubled'), 'even_four_and_five_times'),
 ('Mishnah Bava Metzia 2:5 — signs and claimants', courts('sign_and_claimant'), 'signs_and_claimants'),
 ('Mishnah Bava Metzia 2:7 — the deceiver examined', courts('deceiver'), 'examine_the_claimant'),
 ('Mishnah Bava Metzia 2:6 — how long to announce', courts('announce_duration'), 'R_Meir_neighbors_R_Yehuda_three_pilgrimages'),
 ('Mishnah Bava Kamma 5:7 — ox or donkey names the common case', courts('common_case_animals'), 'ox_or_donkey_names_the_common_case'),
 ('Exod 23:5 — "lying under its burden" a hapax', courts('lying_under'), 'hapax'),
 ('Mishnah Bava Metzia 2:10 — unload even four and five times', courts('unload_doubled'), 'even_four_and_five_times'),
 ('Mishnah Bava Metzia 2:10 — "with him": the idle owner exempts', courts('with_him'), 'owner_idle_exempts'),
 ('Mishnah Bava Metzia 2:10 — a load it can bear', courts('measure'), 'a_load_it_can_bear'),
 ('Mishnah Bava Metzia 2:10 — unloading Torah, loading disputed', courts('unload_load'), 'unloading_torah_loading_disputed'),
 ('Mekhilta 23:5 — the ris (data)', courts('ris'), 'one_in_seven_and_a_half_of_a_mil'),
 ('Mishnah Bava Metzia 2:10 — the father\'s word not obeyed', courts('father_says_no'), 'do_not_listen'),
 ('Onkelos Exod 23:5 — the grudge released', courts('grudge'), 'leave_what_is_in_your_heart'),
 ('Exod 23:6 — "your needy" a hapax; the wicked-and-worthy pair', courts('needy_in_his_cause'), 'hapax_the_wicked_and_worthy_pair'),
 ('Exod 23:7 — "from a false matter" a hapax', courts('keep_far'), 'hapax'),
 ('Mishnah Sanhedrin 4:1 — no retrial after acquittal (Onkelos 23:7)', courts('no_retrial_acquitted'), 'reversed_for_merit_not_for_liability'),
 ('Mekhilta 23:7 — no execution without witnesses', courts('circumstantial'), 'no_execution_without_witnesses'),
 ('Exod 23:8 — the bribe (holiness engine by call; Peah 8:9 quotes this verse)', courts('bribe'), 'the_bribed_judges_eyes_dim'),
 ('Mekhilta 23:8 — bribery absolute', courts('bribe_absolute'), 'even_to_judge_truly'),
 ('Exod 23:9 — the soul of the stranger (holiness_b by call)', courts('stranger_repeat'), 'know_the_strangers_soul_from_your_own'),
 # ---- THE ESCORT AND THE LAND (23:20-33) ----
 ('Exod 23:20-21 — the angel; the Name in him (hapaxes; Onkelos\'s Memra)', land('angel'), 'hapax_the_Name_in_him'),
 ('Exod 23:21 / Josh 24:19 — "he will not bear your transgression"', land('not_forgive'), 'he_will_not_bear_your_transgression'),
 ('Exod 23:28 — the hornet at three seats', land('hornet'), 3),
 ('Exod 23:29-30 — not in one year; little by little', land('little_by_little'), 'not_in_one_year'),
 ('Exod 23:31 — the four border terms (data)', land('borders'), ['sea_of_reeds', 'sea_of_the_philistines', 'the_wilderness', 'the_river']),
 ('Exod 23:24 — not bow, not serve, not do', land('no_bow'), 'not_bow_not_serve_not_do'),
 ('Exod 23:24 — demolish and break (doubled verbs); Avodah Zarah 3:1', land('break_pillars'), 'demolish_demolish_break_break'),
 ('Onkelos Exod 23:25 — serve before the LORD', land('serve_before'), 'serve_before_the_LORD'),
 ('Exod 23:25 — bread and water blessed', land('bread_water'), 'blessed_sickness_removed'),
 ('Exod 23:26 — no miscarrying (a hapax) or barren', land('no_barren'), 'hapax'),
 ('Exod 23:32 — no covenant', land('no_covenant'), 'no_covenant_with_them_or_their_gods'),
 ('Exod 23:33 — they shall not dwell; the snare', land('not_dwell'), 'lest_they_make_you_sin'),
 ('the spine silent over 23:20-33 — Onkelos alone', land('spine_silent'), 'onkelos_alone'),
 # ---- THE WRAP (W1) ----
 ('THE SCENE on the world engine — the wrap (W1): twenty-one case heads on the recorded rows', cell(SCENE, A, "THE SCENE: the hewn stone disqualified and the whole accepted; the two offerings by their engines; the sorcerer stoned, the illusionist exempt; the beast and the idolater's row; the widow's cry heard and the oppressor on Heaven's docket, the word-wronger exempt; the bite barred; the pledge's sunset TIMER set on day 3 and FIRED at 4 with the debtor's cry; the ruler cursed by the Name lashed, the euphemist exempt; the gifts' order; the firstborn consecrated and the five sela's thirty-day TIMER (fired at 35); the firstling's eighth-day TIMER (fired at 12) and the donkey's fork; the torn to the dog and its eater lashed; the judge blocked; the court split three ways (12-11 capital ACQUITTED, 13-10 CONVICTED, 12-11 money CONVICTED); the return, the unloading with him and the sitting owner's exemption, the acquitted never retried, the bribe and Heaven's entry; the pillars demolished, the covenant barred, the land's desolation flag held OFF; bread and water blessed; four timers set, four fired; the clock ABSOLUTE: %r" % (SCENE,), ['pledge_returned_by_sunset', 'due_to_priest', 'eighth_day_fit', 'accepted', 'land_desolate']),
  (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ('acquitted', 'convicted', 'convicted'), 1, 1, 1, 1, 1, 1, 1, 1, 1, False, 1, 4, 4, 40)),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print('guard: %d test rows, every expected value a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0, H: 0}
used = []
misses = []
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    used += [e for e in c['fx'] if e != FX.NONE]
    if not hit: misses.append((name, c['v']))
    print('%s %-96s [%s] %s' % ('OK ' if hit else 'MISS', name[:96], c['p'], '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
print()
print('WATCH COVERAGE (the wrap):')
_W.print_coverage()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d'
      % (frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n, frac[H], n))
ops = FX.summarize(used)
print('LEDGER OPS this span writes: %s' % ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
print('effects: every cell carries REGISTERED effects — TEN discovered in these verses\' own verbs: pledge_returned_by_sunset (TIMER), cry_heard, bread_and_water_blessed (HEAVEN), '
      'gift_order_barred, bribe_barred, false_report_barred, covenant_barred (BLOCK), torn_flesh_to_dogs (TRANSFER), majority_decides (STATUS), unloading_owed (DEBIT) [effects law satisfied]')
if ok == n:
    print('THE REST OF THE ORDINANCES COMPILE — the altar rules by call, the capital triad against the sanctions engine, the stranger by the holiness engine\'s second half, '
          'the interest by the jubilee engine, the pledge\'s sunset timer, the curse\'s fork and Name gate, the gifts\' order off two hapaxes, the firstborn by the Passover '
          'engine, the firstling\'s eighth day compiled as the callee the priesthood owed, the torn to the dog, the twenty-three built from "for evil", the enemy\'s load, '
          'the acquitted never retried, the bribe by call, the land\'s covenant barred; the decalogue, offering, sanctions, holiness, holiness_b, jubilee, and Passover engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')
