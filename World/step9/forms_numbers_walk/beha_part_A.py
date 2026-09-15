import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 8:1-26 + 10:1-12:16 — BEHA'ALOTCHA: THE LAMPS, THE LEVITES' RITE AND AGES, THE TRUMPETS, THE MARCH AND THE ARK, TABERAH AND THE
# QUAIL, THE SEVENTY, MIRIAM (THE NUMBERS WALK sitting 3b, 2026-09-10; World/step9/NUMBERS_WALK.md "Sitting 3b"; chapter 9 frozen at THE
# TENT sitting 2 and skipped). The third Numbers portion compiled after its walk, on the owner's ruling READ THEN COMPILE: the parser
# taught the dual noun, the suffixed numeral and the half at this sitting (census_probes.py 63/63 after the seven-stem's homographs were
# read off the sitting's own corpus-wide diff — the sin dot, the qubuts, the ordinal's hiriq, Beer-sheba), the camp's order and the
# fitness CALLED from Bamidbar, the firstborn from the pesach engine, the lampstand's spec from the sanctuary engine, the teruah from the
# moadim engine, the leper's week from the negaim engine; THE DAY-STACK of Taanit 29a as three reading-placed markers with the ink's
# three durations as timers. Five motions of the deliverable rule, the wrap the sixth; every cell cites its source; every token probed
# (zero-report law); effects on every cell (the effects law). Reading ledgers: the four logic/oral_triage/num_{08,10,11,12}_*_2026-09-10.md;
# the exam's docket: num_08_12_beha_exam_2026-09-10.md (212 rows).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 150, ('the guard counted %d expectations, the tripwire holds 150' % GUARDED)   # a placeholder before the rows were written — retyped from the first run's print
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
import effects_layer as FX
import world_engine as WE
import cold_run_bamidbar as BM                   # THE EDGE: beha -> bamidbar CALL, reference (the camp's order; the fitness and the ages; the lots)
import cold_run_pesach as PS                     # THE EDGE: beha -> pesach CALL, reference (8:16-18's firstborn ground)
import cold_run_sanctuary_build as SB            # THE EDGE: beha -> sanctuary_build CALL, reference (8:4's lampstand as the pattern shown)
import cold_run_moadim as MD                     # THE EDGE: beha -> moadim CALL, reference (10:5-6's teruah = Lev 23:24's; the shofar)
import cold_run_negaim as NG                     # THE EDGE: beha -> negaim CALL, reference (12:14-15's shutting-out = the leper's week)

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
_INK['_ROOT'] = _ROOT   # THE PORTABLE REPO (2026-09-15): the INK block reads the store through the root; the exec'd namespace must carry it
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, verse_words, ink_ordinals = _INK['ink_numbers'], _INK['verse_words'], _INK['ink_ordinals']

db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs, book='Num'):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

def raw_words(ch, vs, book='Num'):
    return [h for (h,) in db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()]

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('בהעלתך',   8, 2,  'when you raise [the lamps]'),
    ('המנורה',   8, 2,  'the lampstand — plene'),
    ('הנרות',    8, 2,  'the lamps'),
    ('מקשה',     8, 4,  'beaten work'),
    ('הראה',     8, 4,  '[the appearance] He showed'),
    ('חטאת',     8, 7,  '[the water of] purification'),
    ('תער',      8, 7,  'a razor'),
    ('וסמכו',    8, 10, 'and they shall lay [hands]'),
    ('תנופה',    8, 11, 'a wave offering'),
    ('נתנים',    8, 16, 'given — doubled'),
    ('פטרת',     8, 16, 'the opener of [the womb]'),
    ('וינף',     8, 21, 'and he waved — the run'),
    ('ועשרים',   8, 24, 'and twenty — twenty-five'),
    ('חמשים',    8, 25, 'fifty'),
    ('משמרת',    8, 26, 'the charge'),
    ('חצוצרת',   10, 2, 'trumpets — the first spelling'),
    ('כסף',      10, 2, 'silver'),
    ('תרועה',    10, 5, 'a teruah'),
    ('תריעו',    10, 7, 'you shall [not] sound a teruah'),
    ('חצצרות',   10, 8, 'trumpets — the second spelling'),
    ('הצרר',     10, 9, 'the oppressor'),
    ('שמחתכם',   10, 10, 'your gladness'),
    ('לזכרון',   10, 10, 'for a remembrance'),
    ('בעשרים',   10, 11, 'on the twentieth'),
    ('נעלה',     10, 11, 'was taken up'),
    ('דגל',      10, 14, 'the standard'),
    ('נשאי',     10, 17, 'the bearers of'),
    ('המקדש',    10, 21, 'the sanctuary'),
    ('המאסף',    10, 25, 'the gatherer — the rearguard'),
    ('לחבב',     10, 29, 'to Hobab'),
    ('לעינים',   10, 31, 'for eyes'),
    ('שלשת',     10, 33, 'three [days]'),
    ('לתור',     10, 33, 'to spy out'),
    ('קומה',     10, 35, 'rise'),
    ('רבבות',    10, 36, 'the myriads of'),
    ('כמתאננים', 11, 1, 'as murmurers'),
    ('ותשקע',    11, 2, 'and [the fire] sank'),
    ('תבערה',    11, 3, 'Taberah'),
    ('והאספסף',  11, 4, 'and the rabble'),
    ('התאוו',    11, 4, 'lusted'),
    ('למשפחתיו', 11, 10, 'by its families'),
    ('האמן',     11, 12, 'the nursing-father'),
    ('שבעים',    11, 16, 'seventy'),
    ('ואצלתי',   11, 17, 'and I will set apart'),
    ('יומים',    11, 19, 'two days — the dual'),
    ('חדש',      11, 20, 'a month'),
    ('לזרא',     11, 20, 'loathsome'),
    ('רגלי',     11, 21, 'on foot'),
    ('תקצר',     11, 23, 'shortened'),
    ('יספו',     11, 25, 'they [did not] continue'),
    ('אלדד',     11, 26, 'Eldad'),
    ('מידד',     11, 26, 'Medad'),
    ('כלאם',     11, 28, 'restrain them'),
    ('המקנא',    11, 29, 'are you jealous'),
    ('שלוים',    11, 31, 'quail'),
    ('וכאמתים',  11, 31, 'and about two cubits — the dual'),
    ('הממעיט',   11, 32, 'the least-gatherer'),
    ('חמרים',    11, 32, 'homers'),
    ('שניהם',    11, 33, 'their teeth (the homograph of "the two of them": the points decide)'),
    ('התאוה',    11, 34, 'the lust — the graves of'),
    ('חצרות',    11, 35, 'Hazeroth'),
    ('ותדבר',    12, 1, 'and she spoke — the feminine singular'),
    ('הכשית',    12, 1, 'the Cushite'),
    ('ענו',      12, 3, 'humble — written without the yod'),
    ('פתאם',     12, 4, 'suddenly'),
    ('שלשתכם',   12, 4, 'the three of you — the suffixed numeral'),
    ('במראה',    12, 6, 'in a vision'),
    ('בחידת',    12, 8, 'in riddles'),
    ('ותמנת',    12, 8, 'and the likeness of'),
    ('מצרעת',    12, 10, 'leprous'),
    ('כשלג',     12, 10, 'as snow'),
    ('נואלנו',   12, 11, 'we have done foolishly'),
    ('כמת',      12, 12, 'as one dead'),
    ('רפא',      12, 13, 'heal'),
    ('ירק',      12, 14, 'spit'),
    ('תסגר',     12, 14, 'she shall be shut out'),
    ('תאסף',     12, 14, 'she shall be gathered in'),
    ('נסע',      12, 15, '[did not] journey'),
    ('פארן',     12, 16, 'Paran'),
]
for tok, ch, vs, note in PROBES:
    if tok not in verse_text(ch, vs).split():
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Num %d:%d — refusing to run' % (tok, note, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

P = []  # the provenance trail of the case being run
def ink(ref, note):  P.append(('INK',  'Num %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)

# ---- THE NUMBERS, computed from the ink by the engine's parser (live; the probes' expectations are the ink's) ----
def N(book, ch, vs): return ink_numbers(verse_words(book, ch, vs))
LAMPS = N('Num', 8, 2); AGE_IN = N('Num', 8, 24); AGE_OUT = N('Num', 8, 25); TRUMPETS = N('Num', 10, 2)
DATE = N('Num', 10, 11); DATE_ORD = ink_ordinals(verse_words('Num', 10, 11)); THREE_DAYS = N('Num', 10, 33)
SEVENTY = N('Num', 11, 16); DAY_LADDER = N('Num', 11, 19); SIX_HUNDRED = N('Num', 11, 21); TWO_CUBITS = N('Num', 11, 31)
TEN_HOMERS = N('Num', 11, 32); THREE_OF_YOU = N('Num', 12, 4); SEVEN_SEVEN = N('Num', 12, 14); SEVEN = N('Num', 12, 15)
NAMES = ['נחשון', 'נתנאל', 'אליאב', 'אליצור', 'שלמיאל', 'אליסף', 'אלישמע', 'גמליאל', 'אבידן', 'אחיעזר', 'פגעיאל', 'אחירע']
def prince_of(ch, vs):
    ws = verse_text(ch, vs).split(); hit = [n for n in NAMES if n in ws]; return hit[0] if hit else None
ORDER_10 = [prince_of(10, v) for v in (14, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26, 27)]
ORDER_2 = [prince_of(2, v) for v in (3, 5, 7, 10, 12, 14, 18, 20, 22, 25, 27, 29)]
LETTERS_3536 = sum(len(w) for v in (35, 36) for w in verse_text(10, v).split())
MIRIAM_FIRST = verse_text(12, 1).split()[0]
PRAYER = verse_text(12, 13).split()[verse_text(12, 13).split().index('אל'):]
BNEI_819 = sum(1 for w in [verse_text(8, 19).split()] for i in range(len(w) - 1) if w[i] in ('בני', 'בבני') and w[i + 1] == 'ישראל')
AGE_SEATS = {'Num 4:3': N('Num', 4, 3), 'Num 8:24': AGE_IN, '1Chr 23:24': N('1Chr', 23, 24), '1Chr 23:27': N('1Chr', 23, 27), 'Ezra 3:8': N('Ezra', 3, 8)}
LIKENESS = [(b, c, v) for (b, c, v) in db.execute("SELECT DISTINCT v.book, v.chapter, v.verse FROM verses v WHERE v.book IN ('Gen','Exod','Lev','Num','Deut')").fetchall()
            if any(w.lstrip('וכלב') in ('תמונה', 'תמונת') for w in verse_text(c, v, b).split())]
assert LAMPS == [7] and AGE_IN == [25] and AGE_OUT == [50] and TRUMPETS == [2] and DATE == [20] and DATE_ORD == [2, 2], (LAMPS, AGE_IN, AGE_OUT, TRUMPETS, DATE, DATE_ORD)
assert THREE_DAYS == [3, 3] and SEVENTY == [70] and DAY_LADDER == [1, 2, 5, 10, 20] and SIX_HUNDRED == [600000] and TWO_CUBITS == [2], (THREE_DAYS, SEVENTY, DAY_LADDER, SIX_HUNDRED, TWO_CUBITS)
assert TEN_HOMERS == [10] and THREE_OF_YOU == [3, 3] and SEVEN_SEVEN == [7, 7] and SEVEN == [7], (TEN_HOMERS, THREE_OF_YOU, SEVEN_SEVEN, SEVEN)
assert ORDER_10 == ORDER_2 == NAMES, (ORDER_10, ORDER_2)
assert LETTERS_3536 == 85 and MIRIAM_FIRST == 'ותדבר' and len(PRAYER) == 5 and sum(len(w) for w in PRAYER) == 11 and BNEI_819 == 5, (LETTERS_3536, MIRIAM_FIRST, PRAYER, BNEI_819)
assert AGE_SEATS == {'Num 4:3': [30, 50], 'Num 8:24': [25], '1Chr 23:24': [20], '1Chr 23:27': [20], 'Ezra 3:8': [20]}, AGE_SEATS
assert len(LIKENESS) == 8, LIKENESS   # the likeness-word's eight Torah seats: seven bans on making one, one beholding (12:8) — sitting 3's measurement

# =====================================================================
# Motion 2 — THE DATA: the parameter rows (the tradition's own vocabulary; the running setting first)
# =====================================================================
DATA = {
    'lamps_geometry': {'value': 'six toward the middle, the middle toward the Presence', 'settings': {'six toward the middle, the middle toward the Presence': "Sifrei Bamidbar 59:1; Menachot 98b:18 (R. Natan: the middle preeminent); Megillah 21b:13 (R. Yochanan)"}, 'source': "8:2 'toward the face of the lampstand' against Exod 25:37's 'toward its face'"},
    'lampstand_material': {'value': 'gold beaten; other metals cast, fragments valid', 'settings': {'gold beaten; other metals cast, fragments valid': "Menachot 28a:16 on 8:4 'it was beaten work'"}, 'source': "the 2x2 with the trumpets — Sifrei 61:1"},
    'trumpet_material': {'value': 'silver only; fragments valid', 'settings': {'silver only; fragments valid': "Menachot 28a:18 — 'silver' and 'shall be' indispensable; 'it was beaten' at the lampstand excludes the trumpets"}, 'source': "10:2"},
    'trumpet_scope': {'value': 'instance', 'settings': {'instance': "Menachot 28b:3 — 'for you' twice: Moses' trumpets hidden, the generations make their own", 'generations': "the refuted reading (28b:2 — 'make for you an ark' served the generations)"}, 'source': "10:2 'make for yourself... they shall be for you'"},
    'levite_age': {'value': '25 to learn, 30 to serve, 50 to return; 20 in the Temple', 'settings': {'30': "Num 4:3, 4:47 (seven seats) — the wilderness service", '25': "Num 8:24 alone — Chullin 24a:12 / Sifrei 62:1: twenty-five to apprentice", '20': "1 Chr 23:24, 23:27; 2 Chr 31:17; Ezra 3:8 — 1 Chr 23:26 'they no longer carry the tabernacle': the run re-sets the spec"}, 'source': "the parser at every seat (AGE_SEATS)"},
    'bull_age': {'value': 'up to three years', 'settings': {'up to three years': "the Sages (Mishnah Parah 1:2)", 'up to two years': "R. Yosei HaGelili — 'the SECOND bull' (8:8)", 'up to five years': "R. Meir (old ones not brought, out of respect)"}, 'source': "8:8"},
    'blast_unit': {'value': 'three separate sounds', 'settings': {'three separate sounds': "the Rabbis — a tekiah before and after each teruah, each its own mitzvah (Arakhin 10a:7-8; Sukkah 53b:11-12; Rosh Hashanah 34a:6-7)", 'one unit': "R. Yehuda — tekiah-teruah-tekiah one blast (the tekiah-root verb on the teruah; 'a second time' the second tekiah)"}, 'source': "10:5-7"},
    'teruah_form': {'value': 'a wail — three whimpers', 'settings': {'a wail — three whimpers': "the Targum of Judg 5:28 (Rosh Hashanah 33b); Onkelos 10:5, 10:7, 10:9; Mishnah Rosh Hashanah 4:9 — a teruah = three whimpers, a tekiah = three teruot", 'three sets': "R. Abbahu's ordinance — shevarim, teruah, and both (Rosh Hashanah 34a): the doubt sounded all three ways"}, 'source': "the sound the ink names and never describes"},
    'blast_count_at_journeys': {'value': 'four — one per camp', 'settings': {'four — one per camp': "Sifrei 73:3 — the east and south by the stated teruahs (10:5-6), the west and north by the general clause", 'two — the two stated': "the ink's two teruahs alone (10:5, 10:6)"}, 'source': "10:5-6"},
    'oppression_scope': {'value': 'any oppression', 'settings': {'any oppression': "Sifrei 76:1; Mishnah Ta'anit 3:1-8 — drought, pestilence, blight, locust, beasts, the sword; Taanit 14a", 'war only': "the plain 'when you go to war in your land'"}, 'source': "10:9 'against the oppressor that oppresses you'"},
    'temple_blasts': {'value': [21, 48], 'settings': {'[21, 48]': "Mishnah Sukkah 5:5; Mishnah Arakhin 2:3 — three at the gates, nine at each daily offering; the additional offerings' nine, the Sabbath eve's six; the Sukkot Friday forty-eight"}, 'source': "the Temple's day, the answer sheet's table"},
    'blasts_per_musaf': {'value': 'one set for all', 'settings': {'one set for all': "Rava bar Shmuel's baraita (Sukkah 55a:2) — 'on the day of your gladness, at your appointed times, on your New Moons': one for all that coincide", 'each in itself': "R. Acha b. Chanina (Sukkah 54a:6) — refuted"}, 'source': "10:8 against 10:10"},
    'pestilence_threshold': {'value': '3 dead in 3 days per 500', 'settings': {'3 dead in 3 days per 500': "Mishnah Ta'anit 3:4 — a city of five hundred foot-soldiers, three dead on three consecutive days"}, 'source': "the fasts' table"},
    'seven_clouds': {'value': 7, 'settings': {'7': "Sifrei 83:1 — four sides, above, below, one before them", '13': "R. Yehuda's count", '4': "R. Yoshiya", '2': "Rebbi"}, 'source': "10:34 'the cloud of the LORD was over them by day'"},
    'shekhinah_minimum': {'value': 22000, 'settings': {'22000': "Bava Kamma 83a:7; Yevamot 64a — 'the myriads of the thousands': two myriads and two thousands, the plurals' minimum"}, 'source': "10:36 — the parser reads no numeral (D11): the shelf's datum"},
    'jethro_at_sinai': {'value': 'before the giving', 'settings': {'before the giving': "Zevachim 116a — Jethro came before the Torah was given (R. Yehoshua)", 'after the giving': "R. Elazar HaModai"}, 'source': "10:29's Hobab, Jethro's house"},
    'spies_sent_day': {'value': 29, 'settings': {'29': "Taanit 29a:5 — the baraita: on the twenty-ninth of Sivan Moses sent the spies (the exam's shelf — the running setting)", '28': "Seder Olam Rabbah 8:2 (the shelf's Midrash export)"}, 'source': "the day-stack; 12:16's marker the day before the spies' (Shelach's sitting)"},
    'fire_at_the_edge': {'value': 'the proselytes', 'settings': {'the proselytes': "Sifrei 85:1 — the mixed multitude cast to the edge", 'the officers': "R. Shimon b. Menassia — the great ones at the edge"}, 'source': "11:1 'at the edge of the camp'"},
    'fish_for_nothing': {'value': 'the forbidden relations', 'settings': {'the forbidden relations': "Yoma 75a:6 — 'for nothing': no one ate fish free (Rav / Shmuel, one arm)", 'fish': "'which we ate' — literal fish (the other arm)"}, 'source': "11:5"},
    'five_foods': {'value': 'taste absent', 'settings': {'taste absent': "Yoma 75a:10 (R. Ami / R. Asi, one arm) — the manna gave every taste but these five", 'texture absent': "the other arm — every taste and texture but these five's texture"}, 'source': "11:5 the cucumbers, the melons, the leeks, the onions, the garlic"},
    'manna_taste_word': {'value': 'breast', 'settings': {'breast': "R. Abbahu — shad: every taste, as the milk changes (Yoma 75a:20)", 'demon': "shed — changing forms"}, 'source': "11:8 'the taste of a cake baked with oil'"},
    'wilderness_meat': {'value': 'slaughter', 'settings': {'slaughter': "R. Yishmael — the meat of stabbing forbidden in the wilderness (Chullin 17a:6)", 'stabbing': "R. Akiva — their stabbing was their slaughter"}, 'source': "11:22 'shall flocks and herds be slaughtered for them'"},
    'spread_or_slaughtered': {'value': 'spread', 'settings': {'spread': "the ink's 'spread them out' (11:32)", 'slaughtered': "Reish Lakish's re-reading; R. Yehoshua b. Korcha's birds needing slaughter; Rebbi: Psalm 78:27 says it outright (Yoma 75b:3)"}, 'source': "11:32"},
    'sanhedrin_size': {'value': 71, 'settings': {'71': "the Sages — 'with you': Moses counted (Mishnah Sanhedrin 1:6; Sanhedrin 17a:1-2)", '70': "R. Yehuda — 'with you' for the Presence to rest; Moses not of the court"}, 'source': "11:16 'seventy men... with you'"},
    'lots_mechanism': {'value': '72 ballots, 70 by lot', 'settings': {'72 ballots, 70 by lot': "Sanhedrin 17a:4-5 — six per tribe, seventy written 'elder', two blank, drawn from a box"}, 'source': "11:26 'among the written' — the same box as Bamidbar's 273"},
    'eldad_medad_prophecy': {'value': 'Moses dies and Joshua brings them in', 'settings': {'Moses dies and Joshua brings them in': "Sanhedrin 17a:10 (the first opinion — Joshua's 'imprison them' its reason)", 'the quail': "Abba Chanin in R. Eliezer's name — 'arise, quail'", 'Gog and Magog': "Rav Nachman (17a)"}, 'source': "11:26-29"},
    'continued': {'value': 'the seventy stopped, the two did not', 'settings': {'the seventy stopped, the two did not': "Sanhedrin 17a:13 — 'they prophesied' (11:25) against 'are prophesying' (11:27), the participle", 'did not cease': "Onkelos 11:25 'did not cease' — the spine's other arm (sitting 3); Sanhedrin 17a:12's 'sof' reading, rejected"}, 'source': "11:25 'and did not continue'"},
    'restrain_them': {'value': 'lay the public burden on them', 'settings': {'lay the public burden on them': "Sifrei 96:1 — and they cease of themselves", 'imprison them': "Sanhedrin 17a:14 — as a rebellion (the Moses-dies reading), or a student ruling before his teacher"}, 'source': "11:28"},
    'descents': {'value': 11, 'settings': {'11': "the ink — eleven going-down tokens of the LORD in the Torah (sitting 3's measurement, beha_ink.py)", '10': "Sifrei 93:1 — 'ten descents are written' (the shelf's list not on this shelf)"}, 'source': "11:17, 11:25, 12:5 among them — DIVERGE by one, filed OPEN (CE8)"},
    'aaron_struck': {'value': 'no', 'settings': {'no': "R. Yehuda b. Beteira — 'either way you will answer for it' (Shabbat 97a:2)", 'yes': "R. Akiva — 'against THEM'; 'Aaron turned' = was healed (97a:3)"}, 'source': "12:9-10"},
    'who_declared_miriam': {'value': 'the Holy One Himself', 'settings': {'the Holy One Himself': "Zevachim 102a — the resolution of 101b:19's objection", 'Moses as a priest': "Rav — Moses a priest in the installation week (the objection: a non-priest)", 'Aaron by the Presence': "against Mishnah Negaim 2:5's kin rule (R. Meir)"}, 'source': "12:10"},
    'short_prayer_bounds': {'value': 'five words the floor; forty days the ceiling', 'settings': {'five words the floor; forty days the ceiling': "Berakhot 34a:12 — no briefer than Moses' 'God, heal her, please'; no longer than his forty days"}, 'source': "12:13 (PRAYER computed: five words, eleven letters)"},
    'dayo': {'value': 7, 'settings': {'7': "Bava Kamma 25a:3; Bava Batra 111a:5; Zevachim 69b:6 — the a-fortiori would give fourteen; it suffices that the derived be as its source; Mishnah Bava Kamma 2:5 the answer sheet"}, 'source': "12:14 — the seven of the father's spit"},
    'month_of_days': {'value': 30, 'settings': {'30': "Chagigah 17b:7; Rosh Hashanah 5a:4; Menachot 65b:6 — 'a month of DAYS' counted by days; Megillah 5a:11 — whole days, no hours"}, 'source': "11:20"},
}
assert all('value' in r and 'settings' in r and 'source' in r for r in DATA.values()) and len(DATA) == 33, len(DATA)


# =====================================================================
# Motion 1 — THE FUNCTION, compiled from the ink (F1-F7)
# =====================================================================
# ===== F1: THE LAMPS (Num 8:1-4) =========================================================================
def lamps(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'geometry':
        ink('8:2', '"toward the face of the lampstand shall the seven lamps give light" — against Exod 25:37\'s "toward its face"')
        dat('the row lamps_geometry = %s' % data['lamps_geometry']['value'])
        move('Sifrei Bamidbar 59:1; Menachot 98b:18; Megillah 21b:13', 'the six turned toward the middle, the middle toward the Presence; R. Natan: the middle preeminent')
        return out('six toward the middle, the middle toward the Presence', ['lamp_arranged'])
    if ask == 'western_lamp':
        w = SB.menorah('western_lamp')['v']
        move('cold_run_sanctuary_build.menorah(western_lamp) -> %r [IMPORT]; Shabbat 22b; Mishnah Tamid 6:1' % (w,), 'the western lamp burns continually and the rest are kindled from it')
        return out('the western lamp burns continually; the rest kindled from it', ['lamp_arranged'])
    if ask == 'material':
        m = SB.menorah('material')['v']
        ink('8:4', '"beaten work of gold... it was beaten work"'); move('cold_run_sanctuary_build.menorah(material) -> %r [IMPORT]; Menachot 28a:16' % (m,), 'of gold it must be beaten; of other metals cast, fragments valid')
        dat('the row lampstand_material = %s' % data['lampstand_material']['value'])
        return out('gold beaten; other metals cast, fragments valid', ['lamp_arranged'])
    if ask == 'two_by_two':
        move('Sifrei Bamidbar 61:1; Menachot 28a:16-18', 'the lampstand of gold must be beaten, of other metals need not; the trumpets of silver only — fragments valid for trumpets, unfit for a shofar (Mishnah Rosh Hashanah 3:6)')
        return out('the lampstand: gold beaten, other metals cast; the trumpets: silver only', ['lamp_arranged'])
    if ask == 'count':
        c, i = SB.menorah('lamps')['v'], SB.menorah('indispensable')['v']
        ink('8:2', '"the seven lamps" — %s' % LAMPS); move('cold_run_sanctuary_build.menorah(lamps, indispensable) -> %r, %r [IMPORT]; Mishnah Menachot 3:7' % (c, i), 'seven lamps, each indispensable to the others')
        return out('7 lamps, each indispensable', ['lamp_arranged'])
    if ask == 'flowers':
        f = SB.menorah('flowers_with_numbers')['v']
        ink('8:4', '"to its base, to its flower, beaten work"'); move('cold_run_sanctuary_build.menorah(flowers_with_numbers) -> %r [IMPORT]; Menachot 29a:2 (Rav Shalman)' % (f,), 'the ninth flower near the base from 8:4')
        return out('9 flowers — the ninth near the base', ['lamp_arranged'])
    if ask == 'steps':
        move('Sifrei Bamidbar 59:1 ("make steps"); Mishnah Tamid 3:9', 'a stone with three stairs before the lampstand — eighteen handbreadths high')
        return out('three stairs on the stone before the lampstand', ['lamp_arranged'])
    if ask == 'pattern':
        p = SB.menorah('pattern_numbers')['v']
        ink('8:4', '"according to the appearance the LORD showed Moses" — Exod 25:40'); move('cold_run_sanctuary_build.menorah(pattern_numbers) -> %r [IMPORT]; Menachot 29a:14-15' % (p,), '"THIS is the work" — shown with the finger, an exact replica; one of three things shown')
        return out('shown with the finger — an exact replica (one of three)', ['lamp_arranged'])
    if ask == 'inauguration':
        move('Mishnah Menachot 4:4', 'a new lampstand is inaugurated only by the kindling of its seven lamps in the afternoon')
        return out('inaugurated by the seven lamps at evening', ['lamp_arranged'])
    if ask == 'aaron_unchanged':
        ink('8:3', '"and Aaron did so" — the run'); move('Sifrei Bamidbar 60:1', 'Aaron did not change — his praise')
        return out('Aaron did not change', ['accepted'])
    if ask == 'sons_equated':
        move('Sifrei Bamidbar 60:1; Yoma 24b', 'the sons equated with the father by three shared facets — service in the tent, golden vestments, "continually"')
        return out('the sons equated with the father by three facets', ['accepted'])
    if ask == 'day_spoken':
        move('Gittin 60b:1 (R. Levi)', 'the section of the lamps among the eight said on the erection day, the first of Nisan')
        return out('the first of Nisan by R. Levi', ['lamp_arranged'])
    if ask == 'evening_to_morning':
        move('Lev 24:3; Sifrei 59:1', 'from evening to morning — the tamid lamp; the rest kindled toward evening')
        return out('from evening to morning', ['lamp_arranged'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE LEVITES' RITE AND AGES (Num 8:5-26) =========================================================
def levites_rite(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'purification':
        ink('8:7', '"sprinkle the water of purification on them, and they shall pass a razor over all their flesh and wash their garments"')
        move('Num 19:9 (the heifer OWED FORWARD)', 'the water of purification is the heifer\'s water — no runner compiles chapter 19')
        return out('sprinkled with the water of purification, a razor over all the flesh, the garments washed', ['commanded'])
    if ask == 'razor':
        ink('8:7', '"a razor over all their flesh"'); move('Nazir 40a:8; Mishnah Negaim 14:4', 'three shave by command — the nazirite, the leper, the Levites; without a razor, or two hairs left, nothing is done')
        return out('a razor over all the flesh; two hairs left = nothing', ['commanded'])
    if ask == 'bulls':
        ink('8:8', '"a young bull and its meal offering... and a second young bull for a sin offering"')
        return out('two bulls — a sin offering and a burnt offering with its meal offering', ['commanded'])
    if ask == 'bulls_order':
        move('Zevachim 89b:1-2', '"a SECOND bull for a sin offering" — the sin offering\'s blood first, its portions after the burnt offering\'s limbs')
        return out("the sin offering's blood first, its portions after the burnt offering's limbs", ['accepted'])
    if ask == 'sin_offering_eaten':
        move('Horayot 5b:17 (R. Shimon)', '"a second bull" — second to and like the burnt offering: not eaten')
        return out('not eaten — second to and like the burnt offering', ['accepted'])
    if ask == 'bull_age':
        dat('the row bull_age = %s' % data['bull_age']['value']); move('Mishnah Parah 1:2', 'the Sages: up to three; R. Yosei HaGelili two ("the second bull"); R. Meir five')
        return out('up to three years (the Sages); two (R. Yosei HaGelili); five (R. Meir)', ['accepted'])
    if ask == 'hands_laid':
        ink('8:10, 8:12', '"the children of Israel shall lay their hands on the Levites"; "the Levites shall lay their hands on the heads of the bulls"')
        return out('twice — Israel on the Levites, the Levites on the bulls', ['commanded'])
    if ask == 'wavings':
        ink('8:11, 8:13, 8:15 / 8:21', 'three wavings in the spec — ONE in the run')
        move('M-22 (the run read back into the spec)', 'the spec/run delta — the three wavings one act')
        return out('three in the spec, one in the run', ['waved'])
    if ask == 'waved_bodies':
        ink('8:11', '"Aaron shall wave the Levites as a wave offering"'); move('Menachot 61b-62a; Nazir 40a:11', 'a live wave offering — the Levites\' bodies waved: the stringency the leper lacks')
        return out('a live wave offering — the Levites waved by Aaron', ['waved'])
    if ask == 'given':
        ink('8:16 with 3:9', '"given, given" doubled at BOTH seats (the yod here, the vav there)'); move('M-23 (the second seat\'s delta); NM03A-03 corrected', 'the doubling at two seats, two spellings')
        return out("'given, given' doubled at 3:9 and 8:16", ['given_to_aaron'])
    if ask == 'firstborn_ground':
        v = PS.firstborn({'kind': 'human'}, PS.DATA)[0]
        ink('8:16-18', '"instead of every firstborn... on the day I smote every firstborn in Egypt I sanctified them to Me"')
        move('cold_run_pesach.firstborn(human) -> %r [IMPORT]; Bekhorot 4b:22; Mishnah Bekhorot 1:1' % (v,), 'the firstborn sanctified in three places — the wilderness seat is 8:17; the Levites\' exemption from the exchange')
        return out('the wilderness seat of the firstborn (8:17); the Levites for the firstborn', ['given_to_aaron'])
    if ask == 'five_times':
        ink('8:19', '"the children of Israel" %d times in one verse (computed)' % BNEI_819); move('Sifrei Bamidbar (the reading)', 'the five for the five books — the Sifrei\'s count')
        return out('5 times in 8:19', ['given_to_aaron'])
    if ask == 'age':
        dat('the row levite_age = %s' % data['levite_age']['value']); ink('4:3 / 8:24 / 1 Chr 23:24, 23:27 / Ezra 3:8', 'thirty / twenty-five / twenty — %s' % AGE_SEATS)
        move('Chullin 24a:12; Sifrei 62:1; 1 Chr 23:26', 'twenty-five to apprentice, thirty to serve; twenty in the Temple — "they no longer carry the tabernacle"')
        return out('25 to learn, 30 to serve, 50 to return; 20 in the Temple', ['charge_kept'])
    if ask == 'ages':
        v = BM.charges({'ask': 'ages'}, BM.DATA)[0]
        move('cold_run_bamidbar.charges(ages) -> %r [IMPORT]' % (v,), 'the ages table at its home')
        return out(v, ['appointed_to_serve'])
    if ask == 'fitness':
        v, e, _ = BM.charges({'ask': 'fitness', 'who': case.get('who', 'levite'), 'blemished': case.get('blemished', False), 'age': case.get('age', 40), 'carrying': case.get('carrying', True)}, BM.DATA)
        move('cold_run_bamidbar.charges(fitness) -> %r [IMPORT]; Chullin 24a:9-12; Mishnah Chullin 1:6' % (v,), 'the fitness by years, blemish and carrying at its home')
        return out(v, e)
    if ask == 'chiasm':
        move('Mishnah Chullin 1:6; Chullin 24a:9', '"fit in priests, unfit in Levites; fit in Levites, unfit in priests" — years the Levites\', blemishes the priests\'')
        return out('years disqualify Levites, blemishes priests', ['appointed_to_serve'])
    if ask == 'a_fortiori_refused':
        ink('8:24, 8:26', '"THIS is what pertains to the Levites"; "thus shall you do with the Levites"'); move('Chullin 24a:9; Sifrei Bamidbar 62:1, 63:1', 'two mirror a-fortioris each refused by the verse\'s own clause — blemishes do not disqualify Levites, years do not disqualify priests')
        return out("'this' caps the inference: blemishes do not disqualify Levites; years do not disqualify priests", ['appointed_to_serve'])
    if ask == 'after_fifty':
        ink('8:25-26', '"he shall return from the host of the service... shall minister with his brothers to keep the charge, and shall do no service"')
        move('Chullin 24a; Arakhin 11a', 'the returned Levite closes the gates and loads the wagons; the song and the voice')
        return out('keeps the charge, no service — the gates and the wagons', ['charge_kept'])
    if ask == 'song':
        ink('8:19', '"to do the service... and to make atonement"'); move('Arakhin 11a:7 (R. Meir); Mishnah Arakhin 2:6', 'the song indispensable like the blood\'s atonement; twelve Levites the floor on the platform')
        return out('the song indispensable (R. Meir); twelve Levites the floor', ['appointed_to_serve'])
    if ask == 'chronicles':
        ink('1 Chr 23:24-27; Ezra 3:8', 'twenty — %s' % {k: v for k, v in AGE_SEATS.items() if not k.startswith('Num')}); move('1 Chr 23:26', '"they no longer carry the tabernacle" — the run re-sets the spec\'s parameter in its own words')
        return out('twenty — no more carrying: the run re-sets the spec', ['charge_kept'])
    if ask == 'day_spoken':
        move('Gittin 60a:17 (R. Levi)', 'the section of the Levites among the eight said on the erection day')
        return out('the first of Nisan by R. Levi', ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE TRUMPETS (Num 10:1-10) =====================================================================
def trumpets(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'count':
        ink('10:2', '"two trumpets" — %s' % TRUMPETS); move('Sifrei Bamidbar 72:1; Mishnah Arakhin 2:5', 'two, no more, no less in the wilderness; the Temple\'s floor two, more permitted')
        return out("2 — the wilderness pair; the Temple's floor two, more permitted", ['commanded'])
    if ask == 'material':
        dat('the row trumpet_material = %s' % data['trumpet_material']['value']); ink('10:2', '"of silver, of beaten work"')
        move('Menachot 28a:18; Rosh Hashanah 27a:10', 'silver indispensable; fragments valid; the fast-day shofar silver-plated from it')
        return out('silver only; fragments valid; the fast-day shofar silver-plated from it', ['commanded'])
    if ask == 'scope':
        dat('the row trumpet_scope = %s' % data['trumpet_scope']['value']); ink('10:2', '"make for YOU... they shall be for YOU" — twice')
        move('Menachot 28b:2-3', 'Moses\' trumpets were his alone and hidden; the generations make their own — unlike every other vessel he made')
        return out("instance — Moses' trumpets hidden, the generations make their own", ['commanded'])
    if ask == 'offices':
        ink('10:2', '"for the calling of the congregation and for the journeying of the camps"')
        return out('the calling of the congregation; the journeying of the camps', ['commanded'])
    if ask == 'sounds':
        occ = case.get('occasion', 'journey')
        if occ == 'congregation':
            ink('10:3, 10:7', '"they shall blow with them... you shall blow a tekiah and not sound a teruah"'); move('Rosh Hashanah 34a:6', 'a tekiah is its own sound, a teruah its own')
            return out('a tekiah, no teruah', ['commanded'])
        if occ == 'princes':
            ink('10:4', '"if they blow with ONE, the princes shall gather" — %s' % N('Num', 10, 4))
            return out('one trumpet — the princes', ['commanded'])
        ink('10:5-6', '"you shall sound a teruah... a teruah they shall sound, a second time"'); move('Rosh Hashanah 34a:7-8; Sifrei 73:2', 'a tekiah before and after the teruah — tekiah, teruah, tekiah')
        return out('tekiah, teruah, tekiah', ['commanded'])
    if ask == 'blast_unit':
        dat('the row blast_unit = %s' % data['blast_unit']['value']); move('Arakhin 10a:7-8; Sukkah 53b:11-12', 'R. Yehuda: one unit; the Rabbis: three separate mitzvot — half a mitzvah is never commanded')
        return out('three separate sounds (the Rabbis); one unit (R. Yehuda)', ['commanded'])
    if ask == 'shofar_identity':
        s = MD.rosh_hashanah()['sound']['v']
        ink('10:5-6 / Lev 23:24 / Lev 25:9', '"teruah" here, "teruah" there — the identity')
        move('cold_run_moadim.rosh_hashanah()[sound] -> %r [IMPORT]; Rosh Hashanah 34a:8; Mishnah Rosh Hashanah 4:9' % (s,), 'the shofar\'s tekiah-teruah-tekiah from the trumpets\' verse by the verbal analogy; three sets of three')
        return out("the Rosh Hashanah shofar's order from 10:5-6 — tekiah, teruah, tekiah, three sets", ['sanctify_day'])
    if ask == 'teruah_form':
        dat('the row teruah_form = %s' % data['teruah_form']['value']); move('Rosh Hashanah 33b (the Targum of Judg 5:28); Onkelos 10:5; Mishnah Rosh Hashanah 4:9', 'the teruah a wail — three whimpers; R. Abbahu\'s three sets')
        return out('a wail — three whimpers; the three sets by R. Abbahu', ['sanctify_day'])
    if ask == 'blast_count_at_journeys':
        dat('the row blast_count_at_journeys = %s' % data['blast_count_at_journeys']['value']); move('Sifrei Bamidbar 73:3', 'the east and south by the stated teruahs, the west and north by the general clause')
        return out('four — one per camp (Sifrei); two stated', ['commanded'])
    if ask == 'blemished_priest':
        ink('10:8', '"the sons of Aaron, the priests, shall blow"'); move('Sifrei Bamidbar 75:1 (R. Akiva; Lev 3:2\'s priests / priests)', 'the blemished priest blows — Tarfon saw and forgot, Akiva expounded')
        return out('the blemished priest blows', ['accepted'])
    if ask == 'oppression':
        kind = case.get('kind', 'war'); dat('the row oppression_scope = %s' % data['oppression_scope']['value'])
        ink('10:9', '"when you go to war in your land against the oppressor that oppresses you, you shall sound a teruah"')
        move('Sifrei Bamidbar 76:1; Mishnah Ta\'anit 1:4-1:6, 3:1-3:8; Taanit 14a', 'any oppression — the fasts\' table: the drought\'s ladder, the plague at once, the spreading calamities everywhere, the Sabbath\'s three dangers, the one exclusion')
        table = {'war': 'the alarm — war itself (10:9)', 'drought': 'the fasts\' ladder — individuals from the seventeenth of Marcheshvan, the community from Kislev, the alarm on the last seven', 'drought_plague': 'the alarm at once — forty days between rains', 'partial_rain': 'the alarm at once',
                 'one_city': 'the city sounds and fasts, the neighbors fast (R. Akiva: sound, not fast)', 'pestilence': 'the alarm — three dead in three days per five hundred', 'spreading': 'everywhere — blight, mildew, locust, beasts, the sword', 'sabbath': 'even on the Sabbath — a besieged city, a flooding river, a ship at sea', 'excess_rain': 'no alarm — a blessing'}
        return out(table.get(kind, 'the alarm — any oppression'), ['sanctify_day'] if kind != 'excess_rain' else ['exempt'])
    if ask == 'fast_order':
        move('Mishnah Ta\'anit 2:1-2:5', 'the ark to the square, ashes, the reproof; twenty-four blessings with the six conclusions; the priests\' blasts between the blessings inside the Temple only')
        return out("twenty-four blessings, the six conclusions; the priests' blasts inside the Temple only", ['sanctify_day'])
    if ask == 'days_of_gladness':
        ink('10:10', '"on the day of your gladness, at your appointed times, on your New Moons... over your burnt offerings and your peace offerings"')
        move('Mishnah Sukkah 5:4', 'the water-drawing\'s tekiah-teruah-tekiah at four stations')
        return out('festivals, new moons, over the offerings; sets of three at the water-drawing', ['sanctify_day'])
    if ask == 'temple_blasts':
        lo, hi = data['temple_blasts']['value']; day = 3 + 9 + 9; friday = 3 + 3 + 3 + 3 + 3 + 9 + 9 + 9 + 3 + 3
        dat('the row temple_blasts = %s; the day computed 3 + 9 + 9 = %d, the Sukkot Friday %d' % ((lo, hi), day, friday))
        move('Mishnah Sukkah 5:5; Mishnah Arakhin 2:3', 'no fewer than twenty-one, no more than forty-eight')
        assert day == lo and friday == hi, (day, friday)
        return out('21 / 48 — the day 3 + 9 + 9; the Sukkot Friday 48', ['sanctify_day'])
    if ask == 'daily_service':
        move('Mishnah Tamid 7:3', 'two silver trumpets at the libation — tekiah, teruah, tekiah; a tekiah at each of the psalm\'s three breaks with a prostration')
        return out('nine per daily offering — three at the libation, three at the breaks', ['sanctify_day'])
    if ask == 'musaf_blasts':
        dat('the row blasts_per_musaf = %s' % data['blasts_per_musaf']['value']); move('Sukkah 55a:2 (Rava bar Shmuel); Sukkah 54a:6 refuted', 'one set for all the coinciding additional offerings')
        return out('one set for all the coinciding additional offerings', ['sanctify_day'])
    if ask == 'kingship_verses':
        ink('10:10', '"a remembrance before your God; I AM THE LORD YOUR GOD"'); move('Rosh Hashanah 32a:10 (R. Yosei b. Yehuda); Mishnah Rosh Hashanah 4:5-6', 'the superfluous "I am the LORD your God" — Kingship with every Remembrance; ten verses each')
        return out('remembrance and kingship from one verse; ten verses each', ['sanctify_day'])
    if ask == 'over_offerings':
        ink('10:10', '"over your burnt offerings and over the sacrifices of your peace offerings"'); move('Arakhin 11b:22; Zevachim 55a:3 (Rav Mari b. Rav Kahana)', 'the juxtaposition: the obligatory communal offerings take trumpets and song; the communal peace offerings most holy, in the north')
        return out('the communal obligatory offerings; the communal peace offerings most holy, in the north', ['sanctify_day'])
    if ask == 'with_shofar':
        day = case.get('day', 'rosh_hashanah')
        if day == 'fast':
            move('Mishnah Rosh Hashanah 3:4', 'rams\' horns plated with silver, two trumpets in the middle — the trumpets long: the mitzvah of the day is with the trumpets')
            return out('two trumpets in the middle, the shofarot short — the day is the trumpets\'', ['sanctify_day'])
        move('Mishnah Rosh Hashanah 3:3', 'an ibex horn plated with gold, two trumpets at the sides — the shofar long: the mitzvah of the day is with the shofar')
        return out("two trumpets at the sides, the shofar long — the day is the shofar's", ['sanctify_day'])
    if ask == 'fragments':
        move('Menachot 28a:18; Mishnah Rosh Hashanah 3:6', 'trumpets of fragments valid; a shofar of fragments unfit')
        return out('trumpets of fragments valid; a shofar of fragments unfit', ['accepted'])
    if ask == 'who_discharges':
        move('Mishnah Rosh Hashanah 3:8', 'whoever is not obligated cannot discharge the many')
        return out('the obligated only', ['exempt'])
    if ask == 'hearing':
        move('Mishnah Rosh Hashanah 3:7', 'the sound, not the echo; the heart directed')
        return out('the sound, not the echo; intent required', ['accepted'])
    if ask == 'shofar_kinds':
        i = MD.rosh_hashanah()['instrument']['v']
        move('cold_run_moadim.rosh_hashanah()[instrument] -> %r [IMPORT]; Mishnah Rosh Hashanah 3:2' % (i,), 'all shofarot fit but a cow\'s horn')
        return out("all shofarot fit but a cow's horn", ['sanctify_day'])
    return out('no verdict in span', [FX.NONE])
