import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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
assert GUARDED == 154, ('the guard counted %d expectations, the tripwire holds 154' % GUARDED)   # the guard's own count on the first run (the hand had typed 150 before the rows were written)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
import effects_layer as FX
import world_engine as WE
import cold_run_bamidbar as BM                   # THE EDGE: beha -> bamidbar CALL, reference (the camp's order; the fitness and the ages; the lots)
import cold_run_pesach as PS                     # THE EDGE: beha -> pesach CALL, reference (8:16-18's firstborn ground)
import cold_run_sanctuary_build as SB            # THE EDGE: beha -> sanctuary_build CALL, reference (8:4's lampstand as the pattern shown)
import cold_run_moadim as MD                     # THE EDGE: beha -> moadim CALL, reference (10:5-6's teruah = Lev 23:24's; the shofar)
import cold_run_negaim as NG                     # THE EDGE: beha -> negaim CALL, reference (12:14-15's shutting-out = the leper's week)
import cold_run_chukat as CK                     # THE EDGE: beha -> chukat CALL, reference (8:7's water of purification = the heifer's water, Num 19:9, 19:17-18; PAID at THE NUMBERS WALK 6b, 2026-09-11)

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
    ('בחצצרות',  10, 8, 'with the trumpets — the second spelling, with its prefix (the first run read the bare stem the hand had typed)'),
    ('הצרר',     10, 9, 'the oppressor'),
    ('שמחתכם',   10, 10, 'your gladness'),
    ('לזכרון',   10, 10, 'for a remembrance'),
    ('בעשרים',   10, 11, 'on the twentieth'),
    ('נעלה',     10, 11, 'was taken up'),
    ('דגל',      10, 14, 'the standard'),
    ('נשאי',     10, 17, 'the bearers of'),
    ('המקדש',    10, 21, 'the sanctuary'),
    ('מאסף',     10, 25, 'the gatherer — the rearguard, without the article (the hand had typed it with one)'),
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
PRAYER = verse_text(12, 13).split()[verse_text(12, 13).split().index('לאמר') + 1:]   # the prayer is what follows 'saying' — the hand had sliced from the first אל, which is 'TO [the LORD]' (אֶל), a consonantal homograph of 'GOD' (אֵל): the first run read it
BNEI_819 = sum(1 for w in [verse_text(8, 19).split()] for i in range(len(w) - 1) if w[i] in ('בני', 'בבני') and w[i + 1] == 'ישראל')
AGE_SEATS = {'Num 4:3': N('Num', 4, 3), 'Num 8:24': AGE_IN, '1Chr 23:24': N('1Chr', 23, 24), '1Chr 23:27': N('1Chr', 23, 27), 'Ezra 3:8': N('Ezra', 3, 8)}
LIKENESS = [(b, c, v) for (b, c, v) in db.execute("SELECT DISTINCT v.book, v.chapter, v.verse FROM verses v WHERE v.book IN ('Gen','Exod','Lev','Num','Deut')").fetchall()
            if any(w.lstrip('וכלב') in ('תמונה', 'תמונת', 'תמנה', 'תמנת') for w in verse_text(c, v, b).split())]   # 12:8's 'likeness' is DEFECTIVE (ותמנת, no vav) — the first run found seven plene seats and missed the beholding
assert LAMPS == [7] and AGE_IN == [25] and AGE_OUT == [50] and TRUMPETS == [2] and DATE == [20] and DATE_ORD == [2], (LAMPS, AGE_IN, AGE_OUT, TRUMPETS, DATE, DATE_ORD)   # the ordinal reader keeps the MASCULINE 'second' (the month) and has no feminine 'second' (the year) — 1b's note at O3; the hand had typed [2, 2] and the first run read it
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
assert all('value' in r and 'settings' in r and 'source' in r for r in DATA.values()) and len(DATA) == 34, len(DATA)   # the hand had counted 33; the first run counted the rows


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
        c = CK.corpse_tumah({'ask': 'sprinkling_water'}, CK.DATA)                                                    # THE CALL (was: the heifer OWED FORWARD — paid at THE NUMBERS WALK 6b, 2026-09-11)
        move('CALLED cold_run_chukat.corpse_tumah(sprinkling_water) -> %s [IMPORT, live]' % c[0], 'the water of purification is the heifer\'s water (Num 19:9, 19:17-18)')
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


# ===== F4: THE MARCH AND THE ARK (Num 10:11-36) ==============================================================
def march(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'date':
        ink('10:11', '"in the second year, in the second month, on the twentieth of the month" — ordinals %s, the day %s' % (DATE_ORD, DATE))
        move('Rosh Hashanah 3a:5; Taanit 29a:2', 'Nisan and Iyar in one year — the year does not turn in Iyar; the day-stack opens')
        return out('(2, 2, 20) — the twentieth of Iyar, year two; the year does not turn in Iyar', ['arrayed_by_banners'])
    if ask == 'order':
        v = BM.camp({'ask': 'march'}, BM.DATA)[0]
        ink('10:14-27', 'the twelve princes in the camp\'s order a third time — computed %s' % (ORDER_10 == ORDER_2))
        move('cold_run_bamidbar.camp(march) -> %r [IMPORT]' % (v,), 'the order at its home — Judah, Reuben, the tent, Ephraim, Dan')
        return out(v, ['arrayed_by_banners'])
    if ask == 'levites_places':
        ink('10:17, 10:21', '"the tabernacle was taken down, and the sons of Gershon and the sons of Merari journeyed, bearing the tabernacle"; "the Kohathites journeyed, bearing the sanctuary, and they set up the tabernacle before their coming"')
        return out('Gershon and Merari after Judah bearing the tabernacle; Kohath after Reuben bearing the sanctuary — set up before their coming', ['charge_kept'])
    if ask == 'ark_bearers':
        ink('10:21', '"the Kohathites journeyed, the bearers of the sanctuary" — two plurals'); move('Menachot 98b:3', 'two bearers each — four')
        return out('four bearers (two plurals)', ['charge_kept'])
    if ask == 'sanctuary_name':
        ink('10:21', '"the bearers of the SANCTUARY"'); move('Shevuot 16b:4 against Eruvin 2a:14', '10:21\'s "sanctuary" is the ark and the vessels; the Tabernacle is called Sanctuary from Exod 25:8-9')
        return out("10:21's sanctuary is the ark and the vessels; the Tabernacle's name from Exod 25:8", ['charge_kept'])
    if ask == 'princes_order':
        ink('2:3-31 = 7:12-83 = 10:14-27', 'the twelve in one order at three chapters — computed: %s' % (ORDER_10 == ORDER_2 == NAMES))
        return out('the camp\'s order a third time — 2 = 7 = 10', ['arrayed_by_banners'])
    if ask == 'three_days':
        ink('10:33', '"three days\' journey" twice — %s' % THREE_DAYS); move('Taanit 29a:3 (R. Chama b. Chanina); Shabbat 116a:3', 'that very day they turned from after the LORD — the first punishment; the three days on the tape a TIMER, its fire the reading-placed marker at 11:1')
        return out("three days' journey — the timer; that very day they turned (the first punishment)", ['journey_of_three_days'])
    if ask == 'spy_verb':
        ink('10:33', '"to spy out (latur) for them a resting place" — the spies\' verb of chapters 13-14 (eight seats)')
        return out("the ark's verb is the spies' verb — eight seats", ['journey_of_three_days'])
    if ask == 'clouds':
        dat('the row seven_clouds = %s' % data['seven_clouds']['value']); ink('10:34', '"the cloud of the LORD was over them by day"'); move('Sifrei Bamidbar 83:1', 'seven clouds — four sides, above, below, one before; thirteen, four, two the other counts')
        return out('seven clouds (Sifrei); 13 / 4 / 2 the other settings', ['arrayed_by_banners'])
    if ask == 'shekhinah_minimum':
        dat('the row shekhinah_minimum = %s' % data['shekhinah_minimum']['value']); ink('10:36', '"the myriads of the thousands of Israel" — no numeral on the ink (%s)' % N('Num', 10, 36))
        move('Bava Kamma 83a:7; Yevamot 64a', 'two myriads and two thousands — the plurals\' minimum: the Presence rests on no fewer')
        return out('22,000 — the plurals\' minimum (the shelf\'s datum; no numeral on the ink)', ['arrayed_by_banners'])
    if ask == 'eighty_five':
        ink('10:35-36', 'the section\'s letters computed: %d' % LETTERS_3536); move('Mishnah Yadayim 3:5; Shabbat 115b:4', 'a scroll with eighty-five letters defiles the hands; without them it is not rescued from a fire')
        return out('85 letters — the measure of a scroll (Mishnah Yadayim 3:5)', ['arrayed_by_banners'])
    if ask == 'signs':
        ink('10:34 / 10:36', 'the two inverted nuns as marks on the DB (sitting 3)'); move('Shabbat 115b-116a; Sifrei 84:1', 'Rebbi: a book in itself; R. Shimon b. Gamliel: to separate the two punishments, to be written in the portion of the flags')
        return out('a book in itself (Rebbi) / to separate the two punishments (R. Shimon b. Gamliel)', ['arrayed_by_banners'])
    if ask == 'hobab':
        ink('10:29-32', '"we are journeying... come with us"; "I will not go"; "leave us not, I pray... you shall be to us for eyes"'); move('Sifrei Bamidbar 78:3, 81:1; Judg 1:16, 4:11', 'the three readings of "we are journeying"; the answer not in the ink — the Kenites went')
        return out('asked, refused, asked again — the answer not in the ink (Judg 1:16)', ['plea_made'])
    if ask == 'jethro_at_sinai':
        dat('the row jethro_at_sinai = %s' % data['jethro_at_sinai']['value']); move('Zevachim 116a', 'before the giving (R. Yehoshua) / after (R. Elazar HaModai)')
        return out('before the giving (R. Yehoshua); after (R. Elazar HaModai)', ['plea_made'])
    if ask == 'day_stack':
        dat('the row spies_sent_day = %s' % data['spies_sent_day']['value'])
        move('Taanit 29a:2-5; Seder Olam Rabbah 8:2', '(2, 2, 20) the march; + 3 days = the twenty-third; the month of meat ends the twenty-second of Sivan; Hazeroth with the seven until the twenty-ninth; the spies sent that day')
        return out('the march (2, 2, 20); the three days to the twenty-third; Hazeroth on the twenty-second of Sivan; Paran on the twenty-ninth', ['arrayed_by_banners'])
    if ask == 'year_turns':
        move('Rosh Hashanah 3a:5', '40:17\'s "second year" and 10:11\'s "second year" — Nisan and Iyar in one year')
        return out('not in Iyar — Nisan and Iyar in one year', ['arrayed_by_banners'])
    if ask == 'cloud_and_trumpets':
        ink('9:23 and 10:2', '"by the word of the LORD they journeyed" AND the trumpets for the journeying'); move('Sifrei Bamidbar 72:1, 84:5', 'two verses both kept — the cloud\'s word and the priests\' blast')
        return out('both kept — the cloud and the trumpets', ['arrayed_by_banners'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: TABERAH, THE LUST AND THE QUAIL (Num 11:1-15, 11:31-35) ==========================================
def taberah_and_quail(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_people':
        ink('11:1', '"the people were as murmurers"'); move('Sifrei Bamidbar 85:1', '"the people" everywhere the wicked, "My people" the upright — a lexical rule with proof-seats')
        return out("'the people' the wicked, 'My people' the upright", ['fire_sank'])
    if ask == 'fire_at_edge':
        dat('the row fire_at_the_edge = %s' % data['fire_at_the_edge']['value']); ink('11:1', '"consumed at the edge of the camp"'); move('Sifrei 85:1 (R. Shimon b. Menassia the other arm)', 'the proselytes cast to the edge / the officers')
        return out('the proselytes at the edge (Sifrei); the officers (R. Shimon b. Menassia)', ['fire_sank'])
    if ask == 'fire_sank':
        ink('11:2', '"Moses prayed to the LORD, and the fire sank"'); move('Berakhot 32a:5', '"to the LORD" read "onto the LORD" — Moses spoke impertinently (R. Elazar)')
        return out("sank at Moses' prayer", ['fire_sank'])
    if ask == 'taberah_name':
        ink('11:3', '"he called the name of that place Taberah, for the fire of the LORD burned among them"'); move('Sifrei 86:1; Deut 9:22', 'the name by the event — "because"')
        return out('named by the event — Taberah (Deut 9:22)', ['fire_sank'])
    if ask == 'rabble':
        ink('11:4', '"the rabble that was among them lusted a lust"'); move('Onkelos 11:4; Exod 12:38', 'the mixed multitude')
        return out('the mixed multitude', ['lusted'])
    if ask == 'five_foods':
        dat('the row five_foods = %s' % data['five_foods']['value']); ink('11:5', 'the cucumbers, the melons, the leeks, the onions, the garlic — one seat each'); move('Yoma 75a:10', 'the manna gave every taste but these five (one arm); every taste and texture but these five\'s texture (the other)')
        return out('the manna tasted like all but these five (R. Ami / R. Asi)', ['lusted'])
    if ask == 'fish_for_nothing':
        dat('the row fish_for_nothing = %s' % data['fish_for_nothing']['value']); move('Yoma 75a:6 (Rav / Shmuel)', '"for nothing" — the forbidden relations; "which we ate" — fish')
        return out("the forbidden relations ('for nothing'); fish ('which we ate')", ['lusted'])
    if ask == 'families_weeping':
        ink('11:10', '"weeping by its families"'); move('Yoma 75a:9; Shabbat 130a:13', 'over the forbidden relations newly barred — a mitzvah accepted with contention')
        return out('the forbidden relations', ['lusted'])
    if ask == 'manna_taste':
        ink('11:8 with Exod 16:31', '"the taste of a cake baked with oil" / "wafers in honey" — two seats'); move('Yoma 75b:5 (R. Yosei b. R. Chanina)', 'bread for the youth, oil for the elderly, honey for the children')
        return out('by age — bread, oil, honey', ['lusted'])
    if ask == 'manna_fell':
        move('Yoma 75a:16', '11:9 "fell on it", Exod 16:4 "go out and gather", 11:8 "went about" — by rank: at the door, outside the camp, far off')
        return out('by rank — the righteous at their doors, the average outside the camp, the wicked far off', ['lusted'])
    if ask == 'manna_form':
        move('Yoma 75a:17', '"bread", "cakes", "ground it" — baked, cakes, raw by rank')
        return out('by rank — baked, cakes, raw', ['lusted'])
    if ask == 'dew':
        move('Yoma 75b:9', 'Exod 16:14 over it, 11:9 under it — dew above and below')
        return out('dew above and dew below', ['lusted'])
    if ask == 'manna_taste_word':
        dat('the row manna_taste_word = %s' % data['manna_taste_word']['value']); move('Yoma 75a:20', 'shad = breast (R. Abbahu) / shed = demon')
        return out('breast (R. Abbahu) / demon', ['lusted'])
    if ask == 'day_ladder':
        ink('11:19-20', '"not one day, nor two days, nor five days, nor ten days, nor twenty days — until a month of days" — the parser: %s' % DAY_LADDER)
        return out('1, 2, 5, 10, 20 — then a month', ['flesh_for_a_month'])
    if ask == 'month_of_days':
        dat('the row month_of_days = %s' % data['month_of_days']['value']); move('Chagigah 17b:7; Megillah 5a:11', 'a month of DAYS — thirty, counted by days, no hours')
        return out('thirty days, counted by days, no hours', ['flesh_for_a_month'])
    if ask == 'six_hundred_thousand':
        ink('11:21', '"six hundred thousand on foot" — %s; the exodus\' "about" dropped' % SIX_HUNDRED)
        return out('600000 on foot', ['lusted'])
    if ask == 'shortened_hand':
        ink('11:23', '"is the hand of the LORD shortened?" — with Isa 50:2, 59:1'); move('Onkelos 11:23', '"the Word held back"')
        return out('not shortened — three seats', ['flesh_for_a_month'])
    if ask == 'nursing_father':
        ink('11:12', '"as a nursing-father carries the sucking child"'); move('Sanhedrin 8a:6', 'the judge bears the community\'s burden to this degree')
        return out("the judge's burden measured by Moses' clause", ['lusted'])
    if ask == 'wilderness_meat':
        dat('the row wilderness_meat = %s' % data['wilderness_meat']['value']); move('Chullin 17a:6', 'R. Yishmael: the meat of stabbing forbidden — "slaughtered" literal; R. Akiva: their stabbing was their slaughter')
        return out('slaughter (R. Yishmael); stabbing (R. Akiva)', ['lusted'])
    if ask == 'quail_height':
        ink('11:31', '"about two cubits above the face of the earth" — the dual: %s' % TWO_CUBITS); move('Yoma 75b; Arakhin 15b:3', 'the second quail among the ten trials')
        return out('2 cubits', ['lusted'])
    if ask == 'quail_slaughter':
        ink('11:32', '"gathered the quail"'); move('Chullin 27b:8-9', 'the fish\'s "gathering" is written beside the flocks\' slaughter — birds\' is not: birds need slaughter')
        return out("birds need slaughter — the quail's 'gathered' no exemption", ['lusted'])
    if ask == 'ten_homers':
        ink('11:32', '"he who gathered least gathered ten homers" — %s (Joseph\'s "ten asses" by consonants)' % TEN_HOMERS)
        return out('10 homers the least', ['lusted'])
    if ask == 'meat_between_teeth':
        ink('11:33', '"while the meat was yet between their teeth"'); move('Chullin 105a:8 (Rav Chisda)', 'meat between the teeth is still meat — no cheese until removed')
        return out('still meat — no cheese until removed', ['lusted'])
    if ask == 'two_timers':
        ink('11:33 against 11:19-20', '"between their teeth, before it was chewed" / "a whole month"'); move('Yoma 75b:2; Sifrei Bamidbar 94:1', 'the average died at once, the wicked after a month — one plague, two timers')
        return out('the average at once (11:33), the wicked after a month (11:20) — one plague, two timers', ['put_to_death'])
    if ask == 'graves':
        ink('11:34', '"Kibroth-hattaavah, for there they buried the people that lusted" — plene here, defective at 33:16 and Deut 9:22'); move('Sifrei 98:1', 'the name by the event')
        return out('Kibroth-hattaavah — the graves of lust', ['buried'])
    if ask == 'trials':
        move('Arakhin 15b:3; Pirkei Avot 5:4', 'the quail the second quail-trial among the ten — "these ten times" (Num 14:22)')
        return out('the quail among the ten trials', ['lusted'])
    if ask == 'three_gifts':
        move('Taanit 9a', 'the well by Miriam, the cloud by Aaron, the manna by Moses')
        return out('the well, the cloud, the manna — three gifts by three shepherds', ['lusted'])
    if ask == 'spread_or_slaughtered':
        dat('the row spread_or_slaughtered = %s' % data['spread_or_slaughtered']['value']); move('Yoma 75b:3', 'Reish Lakish: read "slaughtered"; R. Yehoshua b. Korcha: birds needing slaughter; Rebbi: Psalm 78:27')
        return out("spread (the ink); 'slaughtered' by Reish Lakish's re-reading", ['lusted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE SEVENTY AND THE TWO (Num 11:16-30) ===========================================================
def seventy_elders(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'sanhedrin':
        dat('the row sanhedrin_size = %s' % data['sanhedrin_size']['value']); ink('11:16', '"seventy men of the elders" — %s' % SEVENTY); move('Mishnah Sanhedrin 1:6; Sanhedrin 2a:13, 17a:1-2', 'seventy-one with Moses (the Sages); seventy (R. Yehuda)')
        return out('71 (the Sages); 70 (R. Yehuda)', ['appointed_to_serve'])
    if ask == 'lots':
        dat('the row lots_mechanism = %s; Bamidbar\'s the_lots = %s' % (data['lots_mechanism']['value'], BM.DATA['the_lots']['value']))
        ink('11:26', '"among the written"'); move('cold_run_bamidbar.DATA[the_lots] [IMPORT]; Sanhedrin 17a:4-5', 'seventy-two ballots, seventy by lot from a box — the 273\'s mechanism')
        return out('72 ballots, 70 by lot — the box of the 273', ['appointed_to_serve'])
    if ask == 'with_you':
        ink('11:16-17', '"they shall stand there WITH YOU"; "bear the burden WITH YOU"'); move('Horayot 4b:14; Kiddushin 76b:6; Sanhedrin 36b:4, 36b:10, 17a:1-2', 'four readings — counted with them; fit to rule; whole in body; of fit lineage')
        return out('counted with them / fit to rule / whole in body / of fit lineage', ['appointed_to_serve'])
    if ask == 'elder_means':
        ink('11:16', '"whom you know to be the elders of the people"'); move('Kiddushin 32b:8 (R. Yosei HaGelili)', 'an elder is a sage — one who has acquired wisdom')
        return out('a sage — not merely the aged', ['appointed_to_serve'])
    if ask == 'count_when':
        move('Sanhedrin 3b:16', 'from the time of gathering there must be seventy')
        return out('at the gathering', ['appointed_to_serve'])
    if ask == 'spirit':
        ink('11:17, 11:25', '"I will set apart of the spirit that is on you"'); move('Sifrei Bamidbar 93:1; Onkelos 11:17', 'Moses\' lamp undiminished — "make greater"')
        return out("set apart — Moses' spirit undiminished", ['spirit_rested'])
    if ask == 'continued':
        dat('the row continued = %s' % data['continued']['value']); ink('11:25 / 11:27', '"they prophesied and did not continue" / "are prophesying" — the participle'); move('Sanhedrin 17a:12-13; Onkelos 11:25 "did not cease"', 'the seventy stopped, Eldad and Medad did not — the spine\'s two arms settled by the participle')
        return out('the seventy stopped, the two did not', ['spirit_rested'])
    if ask == 'eldad_medad_prophecy':
        dat('the row eldad_medad_prophecy = %s' % data['eldad_medad_prophecy']['value']); move('Sanhedrin 17a:10', 'Moses dies and Joshua brings them in / the quail / Gog and Magog')
        return out('Moses dies and Joshua brings them in; the quail; Gog and Magog — three settings', ['spirit_rested'])
    if ask == 'restrain_them':
        dat('the row restrain_them = %s' % data['restrain_them']['value']); ink('11:28', '"my lord Moses, restrain them"'); move('Sifrei 96:1; Sanhedrin 17a:14', 'lay the public burden on them / imprison them')
        return out('lay the public burden on them (Sifrei); imprison them (Sanhedrin 17a)', ['spirit_rested'])
    if ask == 'joshua_childless':
        move('Eruvin 63a:26 (R. Levi)', 'whoever answers before his teacher goes childless — Joshua')
        return out('answered before his teacher — childless', ['spirit_rested'])
    if ask == 'descents':
        dat('the row descents = %s' % data['descents']['value']); ink('11:17, 11:25, 12:5', '"I will come down"; "the LORD came down" — eleven going-down tokens in the Torah (the reading)'); move('Sifrei Bamidbar 93:1', '"ten descents are written" — the shelf\'s count, the list not on this shelf')
        return out("eleven on the ink against the Sifrei's ten — DIVERGE by one, open", ['spirit_rested'])
    if ask == 'would_that':
        ink('11:29', '"would that all the LORD\'s people were prophets"'); move('Sanhedrin 17a:15', 'fits the two other readings of their prophecy')
        return out("would that all the LORD's people were prophets", ['spirit_rested'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: MIRIAM (Num 12:1-16) =============================================================================
def miriam(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'who_first':
        ink('12:1', '"and Miriam SPOKE, and Aaron" — the feminine singular verb before two subjects: %s' % MIRIAM_FIRST); move('Sifrei Bamidbar 99:1', 'Miriam spoke first — the grammar')
        return out('Miriam first — the feminine singular verb', ['evil_speech_spoken'])
    if ask == 'dibbur':
        move('Sifrei Bamidbar 99:1', 'dibbur harsh, amirah imploring — a lexical rule with proof-seats')
        return out('harsh speech (dibbur)', ['evil_speech_spoken'])
    if ask == 'cushite':
        ink('12:1', '"the Cushite woman... a Cushite woman" — with the article, then without'); move('Moed Katan 16b:19; Sifrei 99:1', 'Zipporah is her name — distinguished by her deeds; beautiful')
        return out('distinguished by her deeds (Zipporah) — beautiful', ['evil_speech_spoken'])
    if ask == 'separation':
        ink('12:8', '"mouth to mouth I speak with him"'); move('Shabbat 87a:4', 'Moses separated from his wife by his own a-fortiori and God agreed — one of three things')
        return out("Moses' own a-fortiori, agreed to by God", ['evil_speech_spoken'])
    if ask == 'suddenly':
        ink('12:4', '"the LORD spoke suddenly" — three Torah seats with 6:9\'s'); move('Keritot 9a:19', '"suddenly" = beyond one\'s control')
        return out('beyond control — the three seats', ['evil_speech_spoken'])
    if ask == 'summons':
        ink('12:5', '"and He called Aaron and Miriam, and the two of them came out" — the order reversed; %s' % N('Num', 12, 5))
        return out('Aaron and Miriam — the summons reversed; the two came out', ['evil_speech_spoken'])
    if ask == 'dreams':
        ink('12:6-8', '"in a vision... in a dream"; "mouth to mouth, and not in riddles"'); move('Yevamot 49b; Berakhot 55b:14', 'the prophets through a dim glass, Moses through a clear one; a good dream not false')
        return out('the prophets in dreams; Moses mouth to mouth, not in riddles', ['evil_speech_spoken'])
    if ask == 'likeness':
        ink('12:8', '"the likeness of the LORD he beholds" — the word\'s eight Torah seats computed: %d (seven bans, one beholding)' % len(LIKENESS)); move('Berakhot 7a:32', 'the reward of the hidden face at the bush')
        return out('seven bans on making one, one beholding (12:8)', ['evil_speech_spoken'])
    if ask == 'aaron_struck':
        dat('the row aaron_struck = %s' % data['aaron_struck']['value']); ink('12:9-10', '"His anger burned against THEM"; "Aaron turned"'); move('Shabbat 97a:2-3', 'R. Akiva: Aaron too; R. Yehuda b. Beteira: either way you will answer for it')
        return out('not struck (R. Yehuda b. Beteira); struck and healed (R. Akiva)', ['stricken_with_leprosy'])
    if ask == 'as_snow':
        ink('12:10', '"leprous as snow" — Moses\' hand (Exod 4:6), Miriam, Gehazi (2 Kgs 5:27)')
        return out("Moses' hand, Miriam, Gehazi — leprous as snow", ['stricken_with_leprosy'])
    if ask == 'who_declared':
        dat('the row who_declared_miriam = %s' % data['who_declared_miriam']['value']); move('Zevachim 101b:19-102a; Mishnah Negaim 2:5, 3:1', 'not Moses the non-priest, not Aaron her kin — the Holy One Himself (or Moses as a priest in the installation week)')
        return out('the Holy One Himself; Moses as a priest in the installation week (Rav); not Aaron her kin', ['stricken_with_leprosy'])
    if ask == 'kin_rule':
        move('Mishnah Negaim 2:5 (R. Meir); 3:1', 'not his own, not his relatives\'; only a priest declares')
        return out("not his own, not his relatives' (R. Meir); only a priest declares", ['stricken_with_leprosy'])
    if ask == 'short_prayer':
        dat('the row short_prayer_bounds = %s' % data['short_prayer_bounds']['value']); ink('12:13', '"God, heal her, please" — %d words, %d letters, two "please"' % (len(PRAYER), sum(len(w) for w in PRAYER)))
        move('Berakhot 34a:12; Mishnah Berakhot 5:5', 'no briefer than Moses; fluency the sign of acceptance')
        return out('five words, the floor; forty days the ceiling; fluency the sign', ['healed'])
    if ask == 'dayo':
        dat('the row dayo = %s' % data['dayo']['value']); ink('12:14', '"if her father had but spit in her face, would she not be ashamed seven days?" — %s' % SEVEN_SEVEN)
        move('Bava Kamma 25a:3, 25a:8; Bava Batra 111a:5; Zevachim 69b:6; Mishnah Bava Kamma 2:5', 'fourteen by the a-fortiori; DAYO — seven: Torah law, general (12:15\'s second verse)')
        return out('7 of 14 — dayo is Torah law', ['confined_seven_days'])
    if ask == 'admonition_days':
        move('Moed Katan 16a:20', 'admonition no less than seven days — an allusion from Miriam')
        return out('seven days — admonition', ['confined_seven_days'])
    if ask == 'quarantine':
        d = NG.days(1)
        ink('12:14-15', '"let her be shut out of the camp seven days" — the leper\'s verb; %s' % SEVEN); move('cold_run_negaim.days(1) -> %r [IMPORT]; Lev 13:4' % (d,), 'the leper\'s week — the negaim engine\'s confinement')
        return out('shut out seven days — the leper\'s week (7)', ['confined_seven_days'])
    if ask == 'grade':
        v = NG.standing_verdict('skin')
        ink('12:10', '"leprous as snow" — the confirmed grade'); move('Yevamot 103b:16; cold_run_negaim.standing_verdict(skin) -> %r [IMPORT]' % (v,), 'the CONFIRMED leper is as one dead — not the quarantined')
        return out('confirmed — as one dead (the confirmed leper only)', ['stricken_with_leprosy'])
    if ask == 'as_one_dead':
        ink('12:12', '"let her not be as one dead"'); move('Nedarim 64b:6; Avodah Zarah 5a:19; Chullin 7b:12; Sanhedrin 47a:10', 'four are as dead — the pauper, the leper, the blind, the childless')
        return out('the leper among the four as dead', ['stricken_with_leprosy'])
    if ask == 'measure_for_measure':
        ink('12:15', '"the people did not journey until Miriam was gathered in"'); move('Mishnah Sotah 1:7, 1:9; Sotah 9b:8', 'an hour at the Nile — seven days\' halt')
        return out("an hour at the Nile, seven days' halt — measure for measure", ['journey_halted'])
    if ask == 'halt':
        ink('12:15-16', '"the people did not journey until Miriam was gathered in; and afterward the people journeyed"')
        return out('the halt until she was gathered; then Paran', ['journey_halted'])
    if ask == 'leper_shaves_on_festival':
        move('Mishnah Moed Katan 3:1; Moed Katan 7b', 'the leper rising to purity shaves on the intermediate days; the leper as one dead')
        return out('the leper shaves on the intermediate days', ['healed'])
    if ask == 'humble':
        ink('12:3', '"the man Moses was very humble" — written without the yod, read with it (the pair)'); move('Nedarim 38a:9; Chullin 89a', 'Moses humble, wise, wealthy')
        return out("humble — written without the yod, read with it", ['evil_speech_spoken'])
    if ask == 'article_blocks_identity':
        ink('12:3 / 27:18', '"THE man Moses" / "a man in whom is spirit"'); move('Yoma 76a:1', '"man" / "man" reads Joshua — "the man" no match: the article blocks the identity')
        return out("'the man' no match for 'man' — the article blocks the identity", ['evil_speech_spoken'])
    if ask == 'foolish':
        ink('12:11', '"we have done foolishly and we have sinned"'); move('Berakhot 63b:12; Makkot 10a:20; Taanit 7a:11', 'no\'alnu = foolish, then sinned')
        return out('foolish, then sinned', ['evil_speech_spoken'])
    if ask == 'remember_miriam':
        move('Deut 24:9; Arakhin 15a-16b', '"remember what the LORD your God did to Miriam" — the paradigm of evil speech')
        return out('the paradigm of evil speech (Deut 24:9)', ['evil_speech_spoken'])
    if ask == 'days':
        ink('12:15', '"shut out of the camp seven days" — %s' % SEVEN)
        return out('7 days', ['confined_seven_days'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_beha(event, world):
    """Num 8:1-26 + 10:1-12:16 (cold_run_beha.py F1-F7). installed_by boot — the standing setting for a law spoken at its verse."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    if k == 'lamps_commanded':
        return [E_('commanded', event['subject'], value='the_lamps', law='F1 [INK 8:2 "when you raise the lamps, toward the face of the lampstand shall the seven lamps give light" — the lighting owed]')]
    if k == 'lamps_raised':
        if not src.startswith('Num 8:'):           # the erection's kind (Exod 40:25) at its second seat — this span's line only; law_erection's own seat is its own
            return []
        world.close('aaron', 'commanded', 'Num 8:3 — and Aaron did so; toward the face of the lampstand he raised its lamps, as the LORD commanded Moses', value='the_lamps')
        return [E_('lamp_arranged', event['subject'], value='toward the face of the lampstand — Aaron did not change (Sifrei 60:1)', law='F1 [INK 8:3 — the run; the lamps\' debit CLOSED]')]
    if k == 'levites_purification_commanded':
        return [E_('commanded', event['subject'], value='the_rite', law='F2 [INK 8:6-7 "take the Levites... and purify them" — the sprinkling, the razor, the garments, the two bulls, the two layings of hands, the three wavings, the giving: owed]')]
    if k == 'levites_purified_and_given':
        world.close(event['subject'], 'commanded', 'Num 8:20-22 — and Moses and Aaron and all the congregation did to the Levites according to all that the LORD commanded', value='the_rite')
        return [E_('waved', event['subject'], value='one waving in the run (8:21) against three in the spec — M-22', law='F2 [INK 8:21 "and Aaron waved them as a wave offering before the LORD"]'),
                E_('given_to_aaron', event['subject'], cp='aaron-and-sons', value='the service entered before Aaron and before his sons', law='F2 [INK 8:22 "the Levites went in to do their service in the tent of meeting before Aaron and before his sons"; the rite\'s debit CLOSED]')]
    if k == 'levite_age_rule':
        return [E_('charge_kept', event['subject'], value='the_age_rule: 25 in (8:24), 50 out to the charge (8:25-26) — the parameter levite_age', law='F2 [INK 8:24-26; Chullin 24a:12; 1 Chr 23:26 the run\'s re-setting]')]
    if k == 'trumpets_commanded':
        return [E_('commanded', event['subject'], value='the_trumpets', law='F3 [INK 10:2 "make for yourself two trumpets of silver" — a command with no narrated making in the span: OPEN, its run Num 31:6]')]
    if k == 'cloud_lifted':
        return []                                  # 10:11-13: the erection's standing rule at its first run — law_erection's own write; this daemon's march line follows
    if k == 'march_in_order':
        return [E_('arrayed_by_banners', event['subject'], value='the first march — Judah, Reuben, the tent in the midst (Gershon and Merari bearing the tabernacle after Judah; Kohath bearing the sanctuary after Reuben), Ephraim, Dan (10:14-28 = 2:3-31)', law='F4 [INK 10:13-28; the camp\'s order CALLED from Bamidbar]'),
                E_('charge_kept', 'the-levites', value='the burdens on the march: Gershon and Merari the tabernacle (10:17), Kohath the sanctuary — set up before their coming (10:21)', law='F4 [INK 10:17, 10:21]')]
    if k == 'hobab_asked':
        return [E_('plea_made', event['subject'], cp='moses', value='asked to come (10:29), refused (10:30), asked again (10:31-32) — the answer not in the ink (Judg 1:16)', law='F4 [INK 10:29-32; Sifrei 78:1-81:1]')]
    if k == 'ark_journeyed':
        return [E_('journey_of_three_days', event['subject'], due=day + 3, value='three days\' journey from the mountain of the LORD — the ark before them (10:33)', law='F4 [INK 10:33; Taanit 29a:3 — the fire at the twenty-third, the reading-placed marker at 11:1]')]
    if k == 'fire_of_the_lord_burned':
        return [E_('fire_sank', event['subject'], value='the fire of the LORD at the edge of the camp, sunk at Moses\' prayer — Taberah (11:1-3)', law='F5 [INK 11:1-3; Sifrei 85:1-86:1]')]
    if k == 'lust_and_weeping':
        return [E_('lusted', event['subject'], value='lusted a lust — the five foods, the manna despised, Israel weeping by families after them (11:4-10)', law='F5 [INK 11:4-15; Yoma 75a; Shabbat 130a]')]
    if k == 'elders_commanded':
        return [E_('commanded', event['subject'], value='the_gathering', law='F6 [INK 11:16-17 "gather to Me seventy men of the elders" — the gathering owed on Moses]'),
                E_('flesh_for_a_month', 'israel', due=day + 30, value='not one day, nor two, nor five, nor ten, nor twenty — until a month of days (11:19-20)', law='F5 [INK 11:18-20; Yoma 75b:2 the two timers; Taanit 29a:3-4 the stack — CE3]')]
    if k == 'elders_prophesied':
        world.close('moses', 'commanded', 'Num 11:24-25 — and Moses gathered seventy men of the elders of the people and set them around the tent; and the LORD came down in the cloud', value='the_gathering')
        return [E_('spirit_rested', event['subject'], value='the spirit rested on the seventy — they prophesied and did not continue (11:25; the setting continued)', law='F6 [INK 11:24-25; Sanhedrin 17a:12-13]'),
                E_('spirit_rested', 'eldad-and-medad', value='the spirit rested on the two in the camp — they prophesied in the camp and did not cease (11:26-27)', law='F6 [INK 11:26-29; Sanhedrin 17a:4, 17a:13]')]
    if k == 'quail_and_plague':
        return [E_('put_to_death', event['subject'], cp='HEAVEN', value='struck with the flesh between their teeth — the very great blow (11:33); the month\'s timer the second arm', law='F5 [INK 11:31-33; Yoma 75b:2 / Sifrei 94:1 one plague, two timers]'),
                E_('buried', event['subject'], value='Kibroth-hattaavah — the graves of lust (11:34)', law='F5 [INK 11:34; Sifrei 98:1]')]
    if k == 'miriam_spoke':
        return [E_('evil_speech_spoken', event['subject'], value='Miriam first — the feminine singular verb; the Cushite woman (12:1-2)', law='F7 [INK 12:1-2; Sifrei 99:1; Arakhin 15a]'),
                E_('evil_speech_spoken', 'aaron', value='and Aaron — with her (12:1); struck too by R. Akiva, not by R. Yehuda b. Beteira', law='F7 [INK 12:1; Shabbat 97a]')]
    if k == 'miriam_stricken_and_shut_out':
        return [E_('stricken_with_leprosy', event['subject'], value='leprous as snow — the confirmed grade (12:10)', law='F7 [INK 12:10; Yevamot 103b; Zevachim 101b-102a who declared]'),
                E_('confined_seven_days', event['subject'], amount=NG.days(1), due=day + NG.days(1), value='shut out of the camp seven days — the leper\'s week (12:14-15)', law='F7 [INK 12:14-15; the negaim engine\'s week CALLED; Taanit 29a:4 — the fire at the twenty-ninth of Sivan, CE4]'),
                E_('journey_halted', 'israel', value='until_miriam_gathered', law='F7 [INK 12:15 "the people did not journey until Miriam was gathered in" — Mishnah Sotah 1:9 measure for measure; closed by 12:16]')]
    if k == 'paran_reached':
        world.close('israel', 'journey_halted', 'Num 12:16 — and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran', value='until_miriam_gathered')
        return []
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'lamps_case':
        v, e, _ = lamps({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'lamp_arranged': E_('lamp_arranged', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'levite_rite_case':
        v, e, _ = levites_rite({'ask': event['ask'], 'who': event.get('who', 'levite'), 'age': event.get('age', 40), 'carrying': event.get('carrying', True), 'blemished': event.get('blemished', False)}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'appointed_to_serve': E_('appointed_to_serve', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'waved': E_('waved', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L),
             'commanded': E_('commanded', s_, value=v, law=L), 'given_to_aaron': E_('given_to_aaron', s_, value=v, law=L), 'charge_kept': E_('charge_kept', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'trumpet_case':
        v, e, _ = trumpets({'ask': event['ask'], 'occasion': event.get('occasion', 'journey'), 'kind': event.get('oppression', 'war'), 'day': event.get('day_kind', 'rosh_hashanah')}, DATA); L = 'F3 [%s]' % v; s_ = event['person']   # the cell's 'kind' is the oppression's; the EVENT's 'kind' is the registry's — the first run's collision (A NAME REUSED IS A MISS)
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'sanctify_day': E_('sanctify_day', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'march_case':
        v, e, _ = march({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'arrayed_by_banners': E_('arrayed_by_banners', s_, value=v, law=L), 'charge_kept': E_('charge_kept', s_, value=v, law=L),
             'journey_of_three_days': E_('journey_of_three_days', s_, value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'elders_case':
        v, e, _ = seventy_elders({'ask': event['ask']}, DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'appointed_to_serve': E_('appointed_to_serve', s_, value=v, law=L), 'spirit_rested': E_('spirit_rested', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'quail_case':
        v, e, _ = taberah_and_quail({'ask': event['ask']}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L), 'lusted': E_('lusted', s_, value=v, law=L), 'fire_sank': E_('fire_sank', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L),
             'exempt': E_('exempt', s_, value=v, law=L), 'flesh_for_a_month': E_('flesh_for_a_month', s_, value=v, law=L), 'buried': E_('buried', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'miriam_case':
        v, e, _ = miriam({'ask': event['ask']}, DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'evil_speech_spoken': E_('evil_speech_spoken', s_, value=v, law=L), 'stricken_with_leprosy': E_('stricken_with_leprosy', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L),
             'exempt': E_('exempt', s_, value=v, law=L), 'healed': E_('healed', s_, value=v, law=L), 'journey_halted': E_('journey_halted', s_, value=v, law=L),
             'confined_seven_days': E_('confined_seven_days', s_, amount=NG.days(1), due=(day + NG.days(1)) if event['ask'] == 'quarantine' else None, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the fitness by age, the trumpets' occasions, the lamps' geometry,
    the seventy-one, the quail's two arms, and Miriam's week as a TIMER (set at the case, fired eight days on)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 8, 10-12: Mishnah Chullin 1, Menachot 3-4, Tamid, Rosh Hashanah 3-4, Ta\'anit, Sukkah 5, Sanhedrin 1, Negaim 2-3, Bava Kamma 2:5 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_beha]
        w.advance(w.clock.day_in('exodus', 2, 2, 1))
        w.submit({'kind': 'lamps_case', 'subject': 'the-priest-at-the-lamps', 'person': 'the-priest-at-the-lamps', 'ask': 'geometry', 'case_source': 'Menachot 98b:18; Num 8:2 — the six toward the middle'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-apprentice-levite', 'person': 'the-apprentice-levite', 'ask': 'fitness', 'who': 'levite', 'age': 27, 'case_source': 'Chullin 24a:12; Num 8:24 — twenty-seven: an apprentice (Bamidbar called)'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-old-levite-at-shiloh', 'person': 'the-old-levite-at-shiloh', 'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False, 'case_source': 'Chullin 24a:11; Num 8:25 — not carrying: fit'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-blemished-levite', 'person': 'the-blemished-levite', 'ask': 'fitness', 'who': 'levite', 'age': 40, 'blemished': True, 'case_source': 'Chullin 24a:9; Mishnah Chullin 1:6; Num 8:24 — a blemish does not disqualify a Levite'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-levites-waved', 'person': 'the-levites-waved', 'ask': 'wavings', 'case_source': 'Menachot 61b; Num 8:11-21 — three wavings in the spec, one in the run'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-priests-at-the-fast', 'person': 'the-priests-at-the-fast', 'ask': 'with_shofar', 'day_kind': 'fast', 'case_source': 'Mishnah Rosh Hashanah 3:4; Num 10:9 — the trumpets the day\'s mitzvah'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-city-with-too-much-rain', 'person': 'the-city-with-too-much-rain', 'ask': 'oppression', 'oppression': 'excess_rain', 'case_source': 'Mishnah Ta\'anit 3:8; Num 10:9 — no alarm for a blessing'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-city-in-pestilence', 'person': 'the-city-in-pestilence', 'ask': 'oppression', 'oppression': 'pestilence', 'case_source': 'Mishnah Ta\'anit 3:4; Num 10:9 — three dead in three days'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-shofar-of-rosh-hashanah', 'person': 'the-shofar-of-rosh-hashanah', 'ask': 'shofar_identity', 'case_source': 'Rosh Hashanah 34a:8; Num 10:5-6 — the identity (the moadim engine called)'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-trumpets-of-moses', 'person': 'the-trumpets-of-moses', 'ask': 'scope', 'case_source': 'Menachot 28b:3; Num 10:2 — for you, twice'})
        w.submit({'kind': 'march_case', 'subject': 'the-camp-on-the-march', 'person': 'the-camp-on-the-march', 'ask': 'order', 'case_source': 'Num 10:14-28; Num 2:3-31 — the camp\'s order (Bamidbar called)'})
        w.submit({'kind': 'march_case', 'subject': 'the-scroll-of-eighty-five', 'person': 'the-scroll-of-eighty-five', 'ask': 'eighty_five', 'case_source': 'Mishnah Yadayim 3:5; Num 10:35-36 — the letters computed'})
        w.submit({'kind': 'elders_case', 'subject': 'the-great-sanhedrin', 'person': 'the-great-sanhedrin', 'ask': 'sanhedrin', 'case_source': 'Mishnah Sanhedrin 1:6; Num 11:16 — seventy-one'})
        w.submit({'kind': 'elders_case', 'subject': 'the-seventy-two-ballots', 'person': 'the-seventy-two-ballots', 'ask': 'lots', 'case_source': 'Sanhedrin 17a:4-5; Num 11:26 — the box (Bamidbar\'s lots called)'})
        w.submit({'kind': 'quail_case', 'subject': 'the-eater-of-the-quail', 'person': 'the-eater-of-the-quail', 'ask': 'two_timers', 'case_source': 'Yoma 75b:2; Num 11:33 — one plague, two timers'})
        w.submit({'kind': 'quail_case', 'subject': 'the-weepers-by-families', 'person': 'the-weepers-by-families', 'ask': 'families_weeping', 'case_source': 'Yoma 75a:9; Num 11:10 — the forbidden relations'})
        w.submit({'kind': 'miriam_case', 'subject': 'the-goring-ox-on-private-ground', 'person': 'the-goring-ox-on-private-ground', 'ask': 'dayo', 'case_source': 'Mishnah Bava Kamma 2:5; Bava Kamma 25a; Num 12:14 — dayo'})
        d0 = w.clock.day
        w.submit({'kind': 'miriam_case', 'subject': 'the-leper-shut-out', 'person': 'the-leper-shut-out', 'ask': 'quarantine', 'case_source': 'Mishnah Negaim 3:1; Num 12:14-15 — the leper\'s week (the negaim engine called)'})
        w.submit({'kind': 'miriam_case', 'subject': 'the-short-prayer', 'person': 'the-short-prayer', 'ask': 'short_prayer', 'case_source': 'Berakhot 34a:12; Num 12:13 — five words'})
        w.submit({'kind': 'miriam_case', 'subject': 'the-confirmed-leper', 'person': 'the-confirmed-leper', 'ask': 'grade', 'case_source': 'Yevamot 103b:16; Num 12:10 — as one dead: the confirmed only'})
        w.advance(d0 + 8)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    L = lambda k: len([l for l in w.log if l[0] == k])
    return (n('the-priest-at-the-lamps', 'lamp_arranged'), n('the-apprentice-levite', 'exempt'), n('the-old-levite-at-shiloh', 'appointed_to_serve'), n('the-blemished-levite', 'appointed_to_serve'), n('the-levites-waved', 'waved'),
            n('the-priests-at-the-fast', 'sanctify_day'), n('the-city-with-too-much-rain', 'exempt'), n('the-city-in-pestilence', 'sanctify_day'), n('the-shofar-of-rosh-hashanah', 'sanctify_day'), n('the-trumpets-of-moses', 'commanded'),
            n('the-camp-on-the-march', 'arrayed_by_banners'), n('the-scroll-of-eighty-five', 'arrayed_by_banners'), n('the-great-sanhedrin', 'appointed_to_serve'), n('the-seventy-two-ballots', 'appointed_to_serve'),
            n('the-eater-of-the-quail', 'put_to_death'), n('the-weepers-by-families', 'lusted'), n('the-goring-ox-on-private-ground', 'confined_seven_days'), n('the-leper-shut-out', 'confined_seven_days'), L('TIMER-SET'), L('TIMER-FIRE'),
            n('the-short-prayer', 'healed'), n('the-confirmed-leper', 'stricken_with_leprosy'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20)   # THE FIRST RUN'S PRINT: one effect per row — the lamps' geometry; the apprentice exempt, the old Levite and the blemished Levite appointed, the wavings; the fast's trumpets, the excess rain exempt, the pestilence's alarm, the shofar's identity, Moses' trumpets commanded; the march's order, the eighty-five; the seventy-one, the lots; the quail's blow, the families' weeping; the goring ox's dayo; THE LEPER'S WEEK — set at the case and FIRED eight days on (TIMER-SET 1, TIMER-FIRE 1); the prayer healed, the confirmed grade; twenty entities
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the Beha scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 3b (2026-09-10; NUMBERS_WALK.md "Sitting 3b"): the portion's own acts AS HISTORY — the eighteen lines of Num 8:1-26 +
    10:1-12:16 in the text's order on a world with this runner's daemon (the erection's cloud_lifted and lamps_raised kinds reused at their
    second seats), the four FORWARD markers — 10:11 the ink's own (2, 2, 20), and Taanit 29a's three reading-placed: 11:1 (2, 2, 23), 11:35
    (2, 3, 22), 12:16 (2, 3, 29) — and the ink's three durations as TIMERS firing on the walks between them. Not a graded cell: the tuple
    below is a tripwire PREDICTED before the first run; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 8, 10-12: Beha\'alotcha on the tape — the lamps, the Levites, the trumpets, the march, Taberah, the quail, the seventy, Miriam (the exodus epoch)', epoch='exodus')
        w.laws = [law_beha]
        w.submit({'kind': 'lamps_commanded', 'subject': 'aaron', 'geometry': 'toward the face', 'count': LAMPS[0], 'pattern': 'as shown', 'case_source': 'Num 8:1-4 — and the LORD spoke to Moses saying: speak to Aaron and say to him: when you raise the lamps, toward the face of the lampstand shall the seven lamps give light; and this is the work of the lampstand: beaten gold... as the pattern the LORD showed Moses'})
        w.submit({'kind': 'lamps_raised', 'subject': 'aaron', 'toward': 'the face of the lampstand', 'case_source': 'Num 8:3 — and Aaron did so: toward the face of the lampstand he raised its lamps, as the LORD commanded Moses'})
        w.submit({'kind': 'levites_purification_commanded', 'subject': 'the-levites', 'water': 'the water of purification', 'razor': True, 'garments': 'washed', 'bulls': 2, 'hands_laid': 2, 'wavings': 3, 'given_doubled': True, 'case_source': 'Num 8:5-19 — and the LORD spoke to Moses saying: take the Levites from among the children of Israel and purify them... for given, given are they to Me from among the children of Israel'})
        w.submit({'kind': 'levites_purified_and_given', 'subject': 'the-levites', 'wavings_in_run': 1, 'atoned': True, 'service_entered': True, 'case_source': 'Num 8:20-22 — and Moses and Aaron and all the congregation did to the Levites according to all that the LORD commanded Moses; and the Levites purified themselves and washed their garments, and Aaron waved them... and afterward the Levites went in to do their service'})
        w.submit({'kind': 'levite_age_rule', 'subject': 'the-levites', 'age_in': AGE_IN[0], 'age_out': AGE_OUT[0], 'after_fifty': 'the charge, no service', 'case_source': 'Num 8:23-26 — and the LORD spoke to Moses saying: this is what belongs to the Levites: from twenty-five years old and upward he shall come to host the host... and from fifty years old he shall return... and shall do no service'})
        w.submit({'kind': 'trumpets_commanded', 'subject': 'moses', 'count': TRUMPETS[0], 'material': 'silver', 'work': 'beaten', 'offices': ['the congregation', 'the camps'], 'sounds': 'tekiah / teruah', 'war': 'the oppressor', 'gladness': 'the festivals, the new moons', 'case_source': 'Num 10:1-10 — and the LORD spoke to Moses saying: make for yourself two trumpets of silver, of beaten work you shall make them... on the day of your gladness... I am the LORD your God'})
        w.marker('Num 10:11', w.clock.day_in('exodus', 2, 2, 20), value='in the second year, in the second month, on the twentieth of the month, the cloud was taken up (10:11) — the ink\'s own date: the tape\'s FORWARD marker after 1:1\'s (2, 2, 1); Rosh Hashanah 3a:5 Nisan and Iyar in one year')
        w.submit({'kind': 'cloud_lifted', 'subject': 'israel', 'from': 'the tabernacle of the testimony', 'to': 'the wilderness of Paran', 'first': True, 'case_source': 'Num 10:11-13 — and the cloud was taken up from over the tabernacle of the testimony; and the children of Israel journeyed by their journeys from the wilderness of Sinai, and the cloud rested in the wilderness of Paran; and they journeyed first by the mouth of the LORD by the hand of Moses'})
        w.submit({'kind': 'march_in_order', 'subject': 'israel', 'order': ORDER_10, 'levites_places': 'Gershon and Merari after Judah; Kohath after Reuben', 'princes': NAMES, 'case_source': 'Num 10:14-28 — and the standard of the camp of the children of Judah journeyed first by their hosts... and the tabernacle was taken down... and the Kohathites journeyed, bearing the sanctuary... these are the journeys of the children of Israel by their hosts, and they journeyed'})
        w.submit({'kind': 'hobab_asked', 'subject': 'hobab', 'three_readings': 'we are journeying', 'answer': 'not in the ink', 'case_source': 'Num 10:29-32 — and Moses said to Hobab son of Reuel the Midianite, Moses\' father-in-law: we are journeying to the place... come with us; and he said: I will not go... and he said: leave us not, I pray'})
        w.submit({'kind': 'ark_journeyed', 'subject': 'the-ark', 'days': THREE_DAYS[0], 'clouds': DATA['seven_clouds']['value'], 'song': 'Rise, LORD / Return, LORD', 'signs': 'two inverted nuns', 'case_source': 'Num 10:33-36 — and they journeyed from the mountain of the LORD three days\' journey, and the ark of the covenant of the LORD journeyed before them... and when the ark journeyed Moses said: Rise, LORD... and when it rested he said: Return, LORD, to the myriads of the thousands of Israel'})
        w.marker('Num 11:1', w.clock.day_in('exodus', 2, 2, 23), value='the three days\' journey elapsed — READING-PLACED by Taanit 29a:3 ("adds to the first twenty days an additional three days\' journey: twenty-three"); the murmuring at Taberah', placement='reading_placed')
        w.submit({'kind': 'fire_of_the_lord_burned', 'subject': 'israel', 'edge': True, 'who': DATA['fire_at_the_edge']['value'], 'prayer': 'Moses prayed', 'name': 'Taberah', 'case_source': 'Num 11:1-3 — and the people were as murmurers, evil in the ears of the LORD; and the LORD heard, and His anger burned, and the fire of the LORD burned among them and consumed at the edge of the camp; and the people cried to Moses, and Moses prayed to the LORD, and the fire sank; and he called the name of that place Taberah'})
        w.submit({'kind': 'lust_and_weeping', 'subject': 'the-rabble', 'foods': ['the fish', 'the cucumbers', 'the melons', 'the leeks', 'the onions', 'the garlic'], 'manna': 'like coriander seed, its taste as a cake baked with oil', 'families': 'weeping by its families', 'moses_cry': 'why have You dealt ill with Your servant', 'case_source': 'Num 11:4-15 — and the rabble that was among them lusted a lust, and the children of Israel also wept again and said: who shall give us flesh to eat?... and Moses heard the people weeping by its families... and Moses said to the LORD: why have You dealt ill with Your servant'})
        w.submit({'kind': 'elders_commanded', 'subject': 'moses', 'seventy': SEVENTY[0], 'spirit': 'set apart', 'day_ladder': DAY_LADDER, 'month': DATA['month_of_days']['value'], 'six_hundred_thousand': SIX_HUNDRED[0], 'case_source': 'Num 11:16-23 — and the LORD said to Moses: gather to Me seventy men of the elders of Israel... and to the people you shall say: sanctify yourselves for tomorrow and you shall eat flesh... not one day, nor two days, nor five days, nor ten days, nor twenty days — until a month of days... is the hand of the LORD shortened?'})
        w.submit({'kind': 'elders_prophesied', 'subject': 'the-seventy-elders', 'seventy': SEVENTY[0], 'two': ['Eldad', 'Medad'], 'continued': DATA['continued']['value'], 'restrain': 'Joshua: my lord Moses, restrain them', 'case_source': 'Num 11:24-30 — and Moses went out and spoke to the people the words of the LORD, and gathered seventy men of the elders of the people and set them around the tent; and the LORD came down in the cloud... and the spirit rested on them and they prophesied and did not continue; and two men remained in the camp... Eldad... Medad... and they prophesied in the camp'})
        w.submit({'kind': 'quail_and_plague', 'subject': 'the-lusters', 'height': TWO_CUBITS[0], 'gathered': TEN_HOMERS[0], 'blow': 'a very great blow', 'graves': 'Kibroth-hattaavah', 'hazeroth': True, 'case_source': 'Num 11:31-35 — and a wind went out from the LORD and brought quail from the sea... about two cubits above the face of the earth... he who gathered least gathered ten homers... the flesh was yet between their teeth... and the LORD struck the people with a very great blow; and he called the name of that place Kibroth-hattaavah... from Kibroth-hattaavah the people journeyed to Hazeroth'})
        w.marker('Num 11:35', w.clock.day_in('exodus', 2, 3, 22), value='the arrival at Hazeroth — READING-PLACED by Taanit 29a:4 (the twenty-ninth of Sivan less the seven days shut out: the twenty-second; Seder Olam Rabbah 8:2\'s stack); the month of flesh ended here on the shelf\'s count', placement='reading_placed')
        w.submit({'kind': 'miriam_spoke', 'subject': 'miriam', 'who_first': MIRIAM_FIRST, 'cushite': 'the Cushite woman', 'answer': 'mouth to mouth, not in riddles', 'aaron_struck': DATA['aaron_struck']['value'], 'case_source': 'Num 12:1-9 — and Miriam spoke, and Aaron, against Moses because of the Cushite woman whom he had taken... and the LORD heard... and the LORD came down in a pillar of cloud and stood at the door of the tent, and called Aaron and Miriam... mouth to mouth I speak with him... and the anger of the LORD burned against them, and He went'})
        w.submit({'kind': 'miriam_stricken_and_shut_out', 'subject': 'miriam', 'stricken': 'leprous as snow', 'prayer': ' '.join(PRAYER), 'dayo': DATA['dayo']['value'], 'days': SEVEN[0], 'halt': True, 'case_source': 'Num 12:10-15 — and the cloud departed from over the tent, and behold Miriam was leprous as snow... and Moses cried to the LORD saying: God, heal her, please... let her be shut out of the camp seven days, and afterward she shall be gathered in; and Miriam was shut out of the camp seven days, and the people did not journey until Miriam was gathered in'})
        w.marker('Num 12:16', w.clock.day_in('exodus', 2, 3, 29), value='the journey from Hazeroth to Paran — READING-PLACED by Taanit 29a:4-5 ("they remained in Hazeroth until the twenty-ninth of Sivan before traveling on to Paran"; the baraita: on the twenty-ninth of Sivan Moses sent the spies); Seder Olam 8:2 the twenty-eighth (the row spies_sent_day)', placement='reading_placed')
        w.submit({'kind': 'paran_reached', 'subject': 'israel', 'from': 'Hazeroth', 'to': 'the wilderness of Paran', 'halt_closed': True, 'case_source': 'Num 12:16 — and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    ex = w.clock.eras['exodus']
    markers = [l for l in w.log if l[0] == 'MARKER']
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    return (n('aaron', 'commanded'), is_open('aaron', 'commanded'), n('aaron', 'lamp_arranged'), n('aaron', 'evil_speech_spoken'),
            n('the-levites', 'commanded'), is_open('the-levites', 'commanded'), n('the-levites', 'waved'), n('the-levites', 'given_to_aaron'), n('the-levites', 'charge_kept'),
            n('moses', 'commanded'), is_open('moses', 'commanded'),
            n('israel', 'arrayed_by_banners'), n('israel', 'fire_sank'), n('israel', 'flesh_for_a_month'), n('israel', 'journey_halted'), is_open('israel', 'journey_halted'),
            n('hobab', 'plea_made'), n('the-ark', 'journey_of_three_days'), n('the-rabble', 'lusted'), n('the-seventy-elders', 'spirit_rested'), n('eldad-and-medad', 'spirit_rested'),
            n('the-lusters', 'put_to_death'), n('the-lusters', 'buried'), n('miriam', 'evil_speech_spoken'), n('miriam', 'stricken_with_leprosy'), n('miriam', 'confined_seven_days'),
            L('TIMER-SET'), L('TIMER-FIRE'), [ex.date(f[1]) for f in fires], len(markers), [m[2].get('retrograde') for m in markers], L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, [False], 1, 1,
                       1, [False], 1, 1, 2,
                       2, [True, False],
                       1, 1, 1, 1, [False],
                       1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1,
                       3, 3, [(2, 2, 23), (2, 3, 24), (2, 3, 29)], 4, [False, False, False, False], 18, 24, 11)   # PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 3b"): the lamps' debit closed by 8:3; the rite's debit closed by 8:20-22 with the one waving and the giving; the Levites' charge twice (the age rule, the march's burdens); Moses' two debits — the trumpets OPEN (their run Num 31:6), the gathering closed; Israel's march, fire, month, halt (closed by 12:16); Hobab's plea; the ark's three days; the rabble; the seventy and the two; the lusters struck and buried; Miriam's three; THREE TIMERS set and fired on the walks — the three days at (2, 2, 23) = the 11:1 marker, the month at (2, 3, 24) two days after the Hazeroth marker (the inclusive count — CE3 DIVERGE expected), Miriam's seven at (2, 3, 29) = the 12:16 marker; four forward markers, none retrograde; eighteen events; twenty-four writes (twenty-one at the lines + the three fires); eleven entities
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Beha\'alotcha\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the lamps
    ('Sifrei 59:1; Menachot 98b:18; Megillah 21b:13 — the geometry', lambda: lamps({'ask': 'geometry'}, DATA), 'six toward the middle, the middle toward the Presence'),
    ('Shabbat 22b; Mishnah Tamid 6:1 — the western lamp (the sanctuary engine CALLED)', lambda: lamps({'ask': 'western_lamp'}, DATA), 'the western lamp burns continually; the rest kindled from it'),
    ('Menachot 28a:16 — the material (the sanctuary engine CALLED)', lambda: lamps({'ask': 'material'}, DATA), 'gold beaten; other metals cast, fragments valid'),
    ('Sifrei 61:1; Menachot 28a:16-18 — the 2x2', lambda: lamps({'ask': 'two_by_two'}, DATA), 'the lampstand: gold beaten, other metals cast; the trumpets: silver only'),
    ('Mishnah Menachot 3:7 — the seven (the sanctuary engine CALLED)', lambda: lamps({'ask': 'count'}, DATA), '7 lamps, each indispensable'),
    ('Menachot 29a:2 — the ninth flower (the sanctuary engine CALLED)', lambda: lamps({'ask': 'flowers'}, DATA), '9 flowers — the ninth near the base'),
    ('Sifrei 59:1; Mishnah Tamid 3:9 — the steps', lambda: lamps({'ask': 'steps'}, DATA), 'three stairs on the stone before the lampstand'),
    ('Menachot 29a:14-15 — the pattern (the sanctuary engine CALLED)', lambda: lamps({'ask': 'pattern'}, DATA), 'shown with the finger — an exact replica (one of three)'),
    ('Mishnah Menachot 4:4 — the inauguration', lambda: lamps({'ask': 'inauguration'}, DATA), 'inaugurated by the seven lamps at evening'),
    ('Sifrei 60:1 — Aaron did not change', lambda: lamps({'ask': 'aaron_unchanged'}, DATA), 'Aaron did not change'),
    ('Sifrei 60:1; Yoma 24b — the sons equated', lambda: lamps({'ask': 'sons_equated'}, DATA), 'the sons equated with the father by three facets'),
    ('Gittin 60b:1 — the day the section was said', lambda: lamps({'ask': 'day_spoken'}, DATA), 'the first of Nisan by R. Levi'),
    ('Lev 24:3; Sifrei 59:1 — evening to morning', lambda: lamps({'ask': 'evening_to_morning'}, DATA), 'from evening to morning'),
    # F2 — the Levites' rite and ages
    ('Num 8:7 — the purification (the chukat engine CALLED — the edge paid at 6b)', lambda: levites_rite({'ask': 'purification'}, DATA), 'sprinkled with the water of purification, a razor over all the flesh, the garments washed'),
    ('Nazir 40a:8; Mishnah Negaim 14:4 — the razor', lambda: levites_rite({'ask': 'razor'}, DATA), 'a razor over all the flesh; two hairs left = nothing'),
    ('Num 8:8 — the two bulls', lambda: levites_rite({'ask': 'bulls'}, DATA), 'two bulls — a sin offering and a burnt offering with its meal offering'),
    ('Zevachim 89b:1-2 — the order', lambda: levites_rite({'ask': 'bulls_order'}, DATA), "the sin offering's blood first, its portions after the burnt offering's limbs"),
    ('Horayot 5b:17 — the sin offering not eaten', lambda: levites_rite({'ask': 'sin_offering_eaten'}, DATA), 'not eaten — second to and like the burnt offering'),
    ('Mishnah Parah 1:2 — the bulls\' age', lambda: levites_rite({'ask': 'bull_age'}, DATA), 'up to three years (the Sages); two (R. Yosei HaGelili); five (R. Meir)'),
    ('Num 8:10, 8:12 — the two layings of hands', lambda: levites_rite({'ask': 'hands_laid'}, DATA), 'twice — Israel on the Levites, the Levites on the bulls'),
    ('Num 8:11-21 — the wavings (M-22)', lambda: levites_rite({'ask': 'wavings'}, DATA), 'three in the spec, one in the run'),
    ('Menachot 61b-62a; Nazir 40a:11 — the bodies waved', lambda: levites_rite({'ask': 'waved_bodies'}, DATA), 'a live wave offering — the Levites waved by Aaron'),
    ('Num 3:9 / 8:16 — given, given (M-23)', lambda: levites_rite({'ask': 'given'}, DATA), "'given, given' doubled at 3:9 and 8:16"),
    ('Bekhorot 4b:22; Mishnah Bekhorot 1:1 — the firstborn ground (the pesach engine CALLED)', lambda: levites_rite({'ask': 'firstborn_ground'}, DATA), 'the wilderness seat of the firstborn (8:17); the Levites for the firstborn'),
    ('Num 8:19 — the five (computed)', lambda: levites_rite({'ask': 'five_times'}, DATA), '5 times in 8:19'),
    ('Chullin 24a:12; 1 Chr 23:24-27 — the age parameter', lambda: levites_rite({'ask': 'age'}, DATA), '25 to learn, 30 to serve, 50 to return; 20 in the Temple'),
    ('Chullin 24a:12 — the ages (Bamidbar CALLED)', lambda: levites_rite({'ask': 'ages'}, DATA), '25 learn, 30 serve, 50 return'),
    ('Chullin 24a:12 — the apprentice of twenty-seven (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'levite', 'age': 27}, DATA), 'unfit — under thirty (twenty-five to apprentice)'),
    ('Chullin 24a:11 — fifty-five at Shiloh, not carrying (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False}, DATA), 'fit — years disqualify only while carrying'),
    ('Chullin 24a:9; Mishnah Chullin 1:6 — the blemished Levite (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'levite', 'age': 40, 'blemished': True}, DATA), 'fit — a blemish does not disqualify a Levite'),
    ('Mishnah Chullin 1:6 — the blemished priest (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'priest', 'blemished': True}, DATA), 'unfit — a blemish'),
    ('Mishnah Chullin 1:6 — the chiasm', lambda: levites_rite({'ask': 'chiasm'}, DATA), 'years disqualify Levites, blemishes priests'),
    ('Chullin 24a:9; Sifrei 62:1, 63:1 — the two a-fortioris refused', lambda: levites_rite({'ask': 'a_fortiori_refused'}, DATA), "'this' caps the inference: blemishes do not disqualify Levites; years do not disqualify priests"),
    ('Num 8:25-26; Chullin 24a — after fifty', lambda: levites_rite({'ask': 'after_fifty'}, DATA), 'keeps the charge, no service — the gates and the wagons'),
    ('Arakhin 11a:7; Mishnah Arakhin 2:6 — the song', lambda: levites_rite({'ask': 'song'}, DATA), 'the song indispensable (R. Meir); twelve Levites the floor'),
    ('1 Chr 23:24-27 — Chronicles re-sets the spec', lambda: levites_rite({'ask': 'chronicles'}, DATA), 'twenty — no more carrying: the run re-sets the spec'),
    ('Gittin 60a:17 — the day the section was said', lambda: levites_rite({'ask': 'day_spoken'}, DATA), 'the first of Nisan by R. Levi'),
    # F3 — the trumpets
    ('Sifrei 72:1; Mishnah Arakhin 2:5 — the count', lambda: trumpets({'ask': 'count'}, DATA), "2 — the wilderness pair; the Temple's floor two, more permitted"),
    ('Menachot 28a:18; Rosh Hashanah 27a:10 — the material', lambda: trumpets({'ask': 'material'}, DATA), 'silver only; fragments valid; the fast-day shofar silver-plated from it'),
    ('Menachot 28b:2-3 — the instance scope', lambda: trumpets({'ask': 'scope'}, DATA), "instance — Moses' trumpets hidden, the generations make their own"),
    ('Num 10:2 — the two offices', lambda: trumpets({'ask': 'offices'}, DATA), 'the calling of the congregation; the journeying of the camps'),
    ('Num 10:3, 10:7; Rosh Hashanah 34a:6 — the congregation', lambda: trumpets({'ask': 'sounds', 'occasion': 'congregation'}, DATA), 'a tekiah, no teruah'),
    ('Num 10:4 — the princes', lambda: trumpets({'ask': 'sounds', 'occasion': 'princes'}, DATA), 'one trumpet — the princes'),
    ('Num 10:5-6; Rosh Hashanah 34a:7 — the journeys', lambda: trumpets({'ask': 'sounds', 'occasion': 'journey'}, DATA), 'tekiah, teruah, tekiah'),
    ('Arakhin 10a:7-8; Sukkah 53b — the blast unit', lambda: trumpets({'ask': 'blast_unit'}, DATA), 'three separate sounds (the Rabbis); one unit (R. Yehuda)'),
    ('Rosh Hashanah 34a:8; Mishnah Rosh Hashanah 4:9 — the identity (the moadim engine CALLED)', lambda: trumpets({'ask': 'shofar_identity'}, DATA), "the Rosh Hashanah shofar's order from 10:5-6 — tekiah, teruah, tekiah, three sets"),
    ('Rosh Hashanah 33b; Onkelos 10:5 — the teruah a wail', lambda: trumpets({'ask': 'teruah_form'}, DATA), 'a wail — three whimpers; the three sets by R. Abbahu'),
    ('Sifrei 73:3 — the blasts at the journeys', lambda: trumpets({'ask': 'blast_count_at_journeys'}, DATA), 'four — one per camp (Sifrei); two stated'),
    ('Sifrei 75:1 — the blemished priest blows', lambda: trumpets({'ask': 'blemished_priest'}, DATA), 'the blemished priest blows'),
    ('Num 10:9 — war', lambda: trumpets({'ask': 'oppression', 'kind': 'war'}, DATA), 'the alarm — war itself (10:9)'),
    ('Mishnah Ta\'anit 1:4-1:6 — drought', lambda: trumpets({'ask': 'oppression', 'kind': 'drought'}, DATA), "the fasts' ladder — individuals from the seventeenth of Marcheshvan, the community from Kislev, the alarm on the last seven"),
    ('Mishnah Ta\'anit 3:1 — forty days between rains', lambda: trumpets({'ask': 'oppression', 'kind': 'drought_plague'}, DATA), 'the alarm at once — forty days between rains'),
    ('Mishnah Ta\'anit 3:2 — partial rain', lambda: trumpets({'ask': 'oppression', 'kind': 'partial_rain'}, DATA), 'the alarm at once'),
    ('Mishnah Ta\'anit 3:3 — one city', lambda: trumpets({'ask': 'oppression', 'kind': 'one_city'}, DATA), 'the city sounds and fasts, the neighbors fast (R. Akiva: sound, not fast)'),
    ('Mishnah Ta\'anit 3:4 — pestilence', lambda: trumpets({'ask': 'oppression', 'kind': 'pestilence'}, DATA), 'the alarm — three dead in three days per five hundred'),
    ('Mishnah Ta\'anit 3:5 — the spreading calamities', lambda: trumpets({'ask': 'oppression', 'kind': 'spreading'}, DATA), 'everywhere — blight, mildew, locust, beasts, the sword'),
    ('Mishnah Ta\'anit 3:7 — the Sabbath', lambda: trumpets({'ask': 'oppression', 'kind': 'sabbath'}, DATA), 'even on the Sabbath — a besieged city, a flooding river, a ship at sea'),
    ('Mishnah Ta\'anit 3:8 — too much rain', lambda: trumpets({'ask': 'oppression', 'kind': 'excess_rain'}, DATA), 'no alarm — a blessing'),
    ('Mishnah Ta\'anit 2:1-2:5 — the fast\'s order', lambda: trumpets({'ask': 'fast_order'}, DATA), "twenty-four blessings, the six conclusions; the priests' blasts inside the Temple only"),
    ('Num 10:10; Mishnah Sukkah 5:4 — the days of gladness', lambda: trumpets({'ask': 'days_of_gladness'}, DATA), 'festivals, new moons, over the offerings; sets of three at the water-drawing'),
    ('Mishnah Sukkah 5:5; Mishnah Arakhin 2:3 — the Temple\'s blasts (computed)', lambda: trumpets({'ask': 'temple_blasts'}, DATA), '21 / 48 — the day 3 + 9 + 9; the Sukkot Friday 48'),
    ('Mishnah Tamid 7:3 — the daily service', lambda: trumpets({'ask': 'daily_service'}, DATA), 'nine per daily offering — three at the libation, three at the breaks'),
    ('Sukkah 55a:2 — the additional offerings', lambda: trumpets({'ask': 'musaf_blasts'}, DATA), 'one set for all the coinciding additional offerings'),
    ('Rosh Hashanah 32a:10; Mishnah Rosh Hashanah 4:5-6 — the kingship verses', lambda: trumpets({'ask': 'kingship_verses'}, DATA), 'remembrance and kingship from one verse; ten verses each'),
    ('Arakhin 11b:22; Zevachim 55a:3 — over the offerings', lambda: trumpets({'ask': 'over_offerings'}, DATA), 'the communal obligatory offerings; the communal peace offerings most holy, in the north'),
    ('Mishnah Rosh Hashanah 3:3 — with the shofar of Rosh Hashanah', lambda: trumpets({'ask': 'with_shofar', 'day': 'rosh_hashanah'}, DATA), "two trumpets at the sides, the shofar long — the day is the shofar's"),
    ('Mishnah Rosh Hashanah 3:4 — with the shofar of the fasts', lambda: trumpets({'ask': 'with_shofar', 'day': 'fast'}, DATA), "two trumpets in the middle, the shofarot short — the day is the trumpets'"),
    ('Menachot 28a:18; Mishnah Rosh Hashanah 3:6 — fragments', lambda: trumpets({'ask': 'fragments'}, DATA), 'trumpets of fragments valid; a shofar of fragments unfit'),
    ('Mishnah Rosh Hashanah 3:8 — who discharges', lambda: trumpets({'ask': 'who_discharges'}, DATA), 'the obligated only'),
    ('Mishnah Rosh Hashanah 3:7 — the hearing', lambda: trumpets({'ask': 'hearing'}, DATA), 'the sound, not the echo; intent required'),
    ('Mishnah Rosh Hashanah 3:2 — the shofar\'s kinds (the moadim engine CALLED)', lambda: trumpets({'ask': 'shofar_kinds'}, DATA), "all shofarot fit but a cow's horn"),
    # F4 — the march and the ark
    ('Num 10:11; Rosh Hashanah 3a:5 — the date', lambda: march({'ask': 'date'}, DATA), '(2, 2, 20) — the twentieth of Iyar, year two; the year does not turn in Iyar'),
    ('Num 10:14-28; Num 2 — the order (Bamidbar CALLED)', lambda: march({'ask': 'order'}, DATA), 'judah, reuben, the tent in the midst, ephraim, dan — as they camp so they journey'),
    ('Num 10:17, 10:21 — the Levites\' places', lambda: march({'ask': 'levites_places'}, DATA), 'Gershon and Merari after Judah bearing the tabernacle; Kohath after Reuben bearing the sanctuary — set up before their coming'),
    ('Menachot 98b:3 — the ark\'s bearers', lambda: march({'ask': 'ark_bearers'}, DATA), 'four bearers (two plurals)'),
    ('Shevuot 16b:4 against Eruvin 2a:14 — the sanctuary\'s name', lambda: march({'ask': 'sanctuary_name'}, DATA), "10:21's sanctuary is the ark and the vessels; the Tabernacle's name from Exod 25:8"),
    ('Num 2 = 7 = 10 — the princes\' order (computed)', lambda: march({'ask': 'princes_order'}, DATA), 'the camp\'s order a third time — 2 = 7 = 10'),
    ('Num 10:33; Taanit 29a:3; Shabbat 116a:3 — the three days', lambda: march({'ask': 'three_days'}, DATA), "three days' journey — the timer; that very day they turned (the first punishment)"),
    ('Num 10:33 — the ark\'s verb', lambda: march({'ask': 'spy_verb'}, DATA), "the ark's verb is the spies' verb — eight seats"),
    ('Sifrei 83:1 — the clouds', lambda: march({'ask': 'clouds'}, DATA), 'seven clouds (Sifrei); 13 / 4 / 2 the other settings'),
    ('Bava Kamma 83a:7; Yevamot 64a — the 22,000', lambda: march({'ask': 'shekhinah_minimum'}, DATA), '22,000 — the plurals\' minimum (the shelf\'s datum; no numeral on the ink)'),
    ('Mishnah Yadayim 3:5; Shabbat 115b:4 — the eighty-five (computed)', lambda: march({'ask': 'eighty_five'}, DATA), '85 letters — the measure of a scroll (Mishnah Yadayim 3:5)'),
    ('Shabbat 115b-116a; Sifrei 84:1 — the signs', lambda: march({'ask': 'signs'}, DATA), 'a book in itself (Rebbi) / to separate the two punishments (R. Shimon b. Gamliel)'),
    ('Num 10:29-32; Sifrei 78:3; Judg 1:16 — Hobab', lambda: march({'ask': 'hobab'}, DATA), 'asked, refused, asked again — the answer not in the ink (Judg 1:16)'),
    ('Zevachim 116a — Jethro at Sinai', lambda: march({'ask': 'jethro_at_sinai'}, DATA), 'before the giving (R. Yehoshua); after (R. Elazar HaModai)'),
    ('Taanit 29a:2-5; Seder Olam 8:2 — the day-stack', lambda: march({'ask': 'day_stack'}, DATA), 'the march (2, 2, 20); the three days to the twenty-third; Hazeroth on the twenty-second of Sivan; Paran on the twenty-ninth'),
    ('Rosh Hashanah 3a:5 — the year does not turn in Iyar', lambda: march({'ask': 'year_turns'}, DATA), 'not in Iyar — Nisan and Iyar in one year'),
    ('Sifrei 72:1, 84:5 — the cloud and the trumpets', lambda: march({'ask': 'cloud_and_trumpets'}, DATA), 'both kept — the cloud and the trumpets'),
    # F5 — Taberah, the lust, the quail
    ('Sifrei 85:1 — the people / My people', lambda: taberah_and_quail({'ask': 'the_people'}, DATA), "'the people' the wicked, 'My people' the upright"),
    ('Sifrei 85:1 — the fire at the edge', lambda: taberah_and_quail({'ask': 'fire_at_edge'}, DATA), 'the proselytes at the edge (Sifrei); the officers (R. Shimon b. Menassia)'),
    ('Num 11:2; Berakhot 32a:5 — the fire sank', lambda: taberah_and_quail({'ask': 'fire_sank'}, DATA), "sank at Moses' prayer"),
    ('Sifrei 86:1; Deut 9:22 — Taberah', lambda: taberah_and_quail({'ask': 'taberah_name'}, DATA), 'named by the event — Taberah (Deut 9:22)'),
    ('Onkelos 11:4 — the rabble', lambda: taberah_and_quail({'ask': 'rabble'}, DATA), 'the mixed multitude'),
    ('Yoma 75a:10 — the five foods', lambda: taberah_and_quail({'ask': 'five_foods'}, DATA), 'the manna tasted like all but these five (R. Ami / R. Asi)'),
    ('Yoma 75a:6 — the fish for nothing', lambda: taberah_and_quail({'ask': 'fish_for_nothing'}, DATA), "the forbidden relations ('for nothing'); fish ('which we ate')"),
    ('Yoma 75a:9; Shabbat 130a:13 — the families\' weeping', lambda: taberah_and_quail({'ask': 'families_weeping'}, DATA), 'the forbidden relations'),
    ('Yoma 75b:5 — the manna\'s taste by age', lambda: taberah_and_quail({'ask': 'manna_taste'}, DATA), 'by age — bread, oil, honey'),
    ('Yoma 75a:16 — how the manna fell', lambda: taberah_and_quail({'ask': 'manna_fell'}, DATA), 'by rank — the righteous at their doors, the average outside the camp, the wicked far off'),
    ('Yoma 75a:17 — the manna\'s form', lambda: taberah_and_quail({'ask': 'manna_form'}, DATA), 'by rank — baked, cakes, raw'),
    ('Yoma 75b:9 — the dew', lambda: taberah_and_quail({'ask': 'dew'}, DATA), 'dew above and dew below'),
    ('Yoma 75a:20 — the taste-word', lambda: taberah_and_quail({'ask': 'manna_taste_word'}, DATA), 'breast (R. Abbahu) / demon'),
    ('Num 11:19-20 — the day-ladder (the parser\'s dual)', lambda: taberah_and_quail({'ask': 'day_ladder'}, DATA), '1, 2, 5, 10, 20 — then a month'),
    ('Chagigah 17b:7; Megillah 5a:11 — a month of days', lambda: taberah_and_quail({'ask': 'month_of_days'}, DATA), 'thirty days, counted by days, no hours'),
    ('Num 11:21 — the six hundred thousand (computed)', lambda: taberah_and_quail({'ask': 'six_hundred_thousand'}, DATA), '600000 on foot'),
    ('Num 11:23 — the hand not shortened', lambda: taberah_and_quail({'ask': 'shortened_hand'}, DATA), 'not shortened — three seats'),
    ('Sanhedrin 8a:6 — the nursing-father', lambda: taberah_and_quail({'ask': 'nursing_father'}, DATA), "the judge's burden measured by Moses' clause"),
    ('Chullin 17a:6 — the wilderness\' meat', lambda: taberah_and_quail({'ask': 'wilderness_meat'}, DATA), 'slaughter (R. Yishmael); stabbing (R. Akiva)'),
    ('Num 11:31; Yoma 75b — two cubits (the parser\'s dual)', lambda: taberah_and_quail({'ask': 'quail_height'}, DATA), '2 cubits'),
    ('Chullin 27b:8-9 — the quail slaughtered', lambda: taberah_and_quail({'ask': 'quail_slaughter'}, DATA), "birds need slaughter — the quail's 'gathered' no exemption"),
    ('Num 11:32 — ten homers (computed)', lambda: taberah_and_quail({'ask': 'ten_homers'}, DATA), '10 homers the least'),
    ('Chullin 105a:8 — the meat between the teeth', lambda: taberah_and_quail({'ask': 'meat_between_teeth'}, DATA), 'still meat — no cheese until removed'),
    ('Yoma 75b:2; Sifrei 94:1 — one plague, two timers', lambda: taberah_and_quail({'ask': 'two_timers'}, DATA), 'the average at once (11:33), the wicked after a month (11:20) — one plague, two timers'),
    ('Num 11:34; Sifrei 98:1 — the graves of lust', lambda: taberah_and_quail({'ask': 'graves'}, DATA), 'Kibroth-hattaavah — the graves of lust'),
    ('Arakhin 15b:3; Pirkei Avot 5:4 — the ten trials', lambda: taberah_and_quail({'ask': 'trials'}, DATA), 'the quail among the ten trials'),
    ('Taanit 9a — the three gifts', lambda: taberah_and_quail({'ask': 'three_gifts'}, DATA), 'the well, the cloud, the manna — three gifts by three shepherds'),
    ('Yoma 75b:3 — spread or slaughtered', lambda: taberah_and_quail({'ask': 'spread_or_slaughtered'}, DATA), "spread (the ink); 'slaughtered' by Reish Lakish's re-reading"),
    # F6 — the seventy and the two
    ('Mishnah Sanhedrin 1:6; Sanhedrin 17a:1-2 — the Sanhedrin', lambda: seventy_elders({'ask': 'sanhedrin'}, DATA), '71 (the Sages); 70 (R. Yehuda)'),
    ('Sanhedrin 17a:4-5 — the lots (Bamidbar\'s box CALLED)', lambda: seventy_elders({'ask': 'lots'}, DATA), '72 ballots, 70 by lot — the box of the 273'),
    ('Horayot 4b; Kiddushin 76b; Sanhedrin 36b — with you', lambda: seventy_elders({'ask': 'with_you'}, DATA), 'counted with them / fit to rule / whole in body / of fit lineage'),
    ('Kiddushin 32b:8 — an elder', lambda: seventy_elders({'ask': 'elder_means'}, DATA), 'a sage — not merely the aged'),
    ('Sanhedrin 3b:16 — the count at the gathering', lambda: seventy_elders({'ask': 'count_when'}, DATA), 'at the gathering'),
    ('Sifrei 93:1 — the spirit set apart', lambda: seventy_elders({'ask': 'spirit'}, DATA), "set apart — Moses' spirit undiminished"),
    ('Sanhedrin 17a:12-13 — did not continue', lambda: seventy_elders({'ask': 'continued'}, DATA), 'the seventy stopped, the two did not'),
    ('Sanhedrin 17a:10 — Eldad and Medad\'s prophecy', lambda: seventy_elders({'ask': 'eldad_medad_prophecy'}, DATA), 'Moses dies and Joshua brings them in; the quail; Gog and Magog — three settings'),
    ('Sifrei 96:1; Sanhedrin 17a:14 — restrain them', lambda: seventy_elders({'ask': 'restrain_them'}, DATA), 'lay the public burden on them (Sifrei); imprison them (Sanhedrin 17a)'),
    ('Eruvin 63a:26 — Joshua childless', lambda: seventy_elders({'ask': 'joshua_childless'}, DATA), 'answered before his teacher — childless'),
    ('Sifrei 93:1 — the ten descents against the ink\'s eleven', lambda: seventy_elders({'ask': 'descents'}, DATA), "eleven on the ink against the Sifrei's ten — DIVERGE by one, open"),
    ('Num 11:29; Sanhedrin 17a:15 — would that', lambda: seventy_elders({'ask': 'would_that'}, DATA), "would that all the LORD's people were prophets"),
    # F7 — Miriam
    ('Sifrei 99:1 — Miriam first (the grammar, computed)', lambda: miriam({'ask': 'who_first'}, DATA), 'Miriam first — the feminine singular verb'),
    ('Sifrei 99:1 — dibbur', lambda: miriam({'ask': 'dibbur'}, DATA), 'harsh speech (dibbur)'),
    ('Moed Katan 16b:19; Sifrei 99:1 — the Cushite', lambda: miriam({'ask': 'cushite'}, DATA), 'distinguished by her deeds (Zipporah) — beautiful'),
    ('Shabbat 87a:4 — the separation', lambda: miriam({'ask': 'separation'}, DATA), "Moses' own a-fortiori, agreed to by God"),
    ('Keritot 9a:19 — suddenly', lambda: miriam({'ask': 'suddenly'}, DATA), 'beyond control — the three seats'),
    ('Num 12:5 — the summons (the parser\'s suffixed numeral)', lambda: miriam({'ask': 'summons'}, DATA), 'Aaron and Miriam — the summons reversed; the two came out'),
    ('Yevamot 49b; Berakhot 55b:14 — dreams and mouth to mouth', lambda: miriam({'ask': 'dreams'}, DATA), 'the prophets in dreams; Moses mouth to mouth, not in riddles'),
    ('Num 12:8; Berakhot 7a:32 — the likeness (computed)', lambda: miriam({'ask': 'likeness'}, DATA), 'seven bans on making one, one beholding (12:8)'),
    ('Shabbat 97a:2-3 — Aaron struck?', lambda: miriam({'ask': 'aaron_struck'}, DATA), 'not struck (R. Yehuda b. Beteira); struck and healed (R. Akiva)'),
    ('Num 12:10 — leprous as snow', lambda: miriam({'ask': 'as_snow'}, DATA), "Moses' hand, Miriam, Gehazi — leprous as snow"),
    ('Zevachim 101b:19-102a; Mishnah Negaim 2:5 — who declared Miriam', lambda: miriam({'ask': 'who_declared'}, DATA), 'the Holy One Himself; Moses as a priest in the installation week (Rav); not Aaron her kin'),
    ('Mishnah Negaim 2:5, 3:1 — the kin rule', lambda: miriam({'ask': 'kin_rule'}, DATA), "not his own, not his relatives' (R. Meir); only a priest declares"),
    ('Berakhot 34a:12; Mishnah Berakhot 5:5 — the short prayer (computed)', lambda: miriam({'ask': 'short_prayer'}, DATA), 'five words, the floor; forty days the ceiling; fluency the sign'),
    ('Bava Kamma 25a; Bava Batra 111a; Zevachim 69b; Mishnah Bava Kamma 2:5 — dayo', lambda: miriam({'ask': 'dayo'}, DATA), '7 of 14 — dayo is Torah law'),
    ('Moed Katan 16a:20 — admonition', lambda: miriam({'ask': 'admonition_days'}, DATA), 'seven days — admonition'),
    ('Num 12:14-15; Lev 13:4 — the quarantine (the negaim engine CALLED)', lambda: miriam({'ask': 'quarantine'}, DATA), 'shut out seven days — the leper\'s week (7)'),
    ('Yevamot 103b:16 — the grade (the negaim engine CALLED)', lambda: miriam({'ask': 'grade'}, DATA), 'confirmed — as one dead (the confirmed leper only)'),
    ('Nedarim 64b:6; Avodah Zarah 5a:19; Chullin 7b:12; Sanhedrin 47a:10 — as one dead', lambda: miriam({'ask': 'as_one_dead'}, DATA), 'the leper among the four as dead'),
    ('Mishnah Sotah 1:7, 1:9; Sotah 9b:8 — measure for measure', lambda: miriam({'ask': 'measure_for_measure'}, DATA), "an hour at the Nile, seven days' halt — measure for measure"),
    ('Num 12:15-16 — the halt', lambda: miriam({'ask': 'halt'}, DATA), 'the halt until she was gathered; then Paran'),
    ('Mishnah Moed Katan 3:1; Moed Katan 7b — the leper shaves on the festival', lambda: miriam({'ask': 'leper_shaves_on_festival'}, DATA), 'the leper shaves on the intermediate days'),
    ('Num 12:3; Nedarim 38a:9 — humble (the written-and-read pair)', lambda: miriam({'ask': 'humble'}, DATA), "humble — written without the yod, read with it"),
    ('Yoma 76a:1 — the article blocks the identity', lambda: miriam({'ask': 'article_blocks_identity'}, DATA), "'the man' no match for 'man' — the article blocks the identity"),
    ('Berakhot 63b; Makkot 10a; Taanit 7a — foolish', lambda: miriam({'ask': 'foolish'}, DATA), 'foolish, then sinned'),
    ('Deut 24:9; Arakhin 15a-16b — remember Miriam', lambda: miriam({'ask': 'remember_miriam'}, DATA), 'the paradigm of evil speech (Deut 24:9)'),
    ('Num 12:15 — the days (computed)', lambda: miriam({'ask': 'days'}, DATA), '7 days'),
]


if __name__ == '__main__':
    ok = 0
    for name, run, want in CASES:
        v, e, pr = run()
        hit = v == want
        ok += hit
        print('  %s  %s\n        -> %s  %s' % ('PASS' if hit else 'MISS', name, v, e))
        if not hit:
            print('        expected: %s' % want)
    print('\nBEHA: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    sys.exit(0 if ok == len(CASES) else 1)
