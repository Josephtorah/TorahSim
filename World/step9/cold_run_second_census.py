#!/usr/bin/env python3
# NUM 25:19-26:65 — THE SECOND CENSUS AND THE POPULATION TABLE (THE NUMBERS WALK sitting 8b, 2026-09-11; World/step9/NUMBERS_WALK.md
# "Sitting 8b"; the speculation ARCHITECTURE/DATABASE_SPECULATION.md). The roll of the plains of Moab compiled against the roll of Sinai:
# the twelve counts at both seats by the ENGINE'S PARSER (1b's census grammar at its second seat — no rule owed), the sums 603,550 and
# 601,730, the deltas DECLARED (never derived) with the tape's explanations by CALL (the Peor plague's 24,000 from Balak, Korach's 14,700 and
# 250) and the remainder labeled; the fifty-seven families with their gentilics keyed to Genesis 46; the roll's named persons; the land's
# law as two functions (the SIZE by count, the PLACE by lot) with the Zelophehad runner's land_divided_among row READ by call; the Levites'
# roll five for eight and 23,000 for 22,000 with the 18:23-24 block READ off the ledger; the two rolls' MEMBERSHIP PREDICATE checked against
# the ledger's death entries and the decree's timer. THE POPULATION TABLE (World.tables — the fifth registry population_schema.yaml) is
# written by this runner's daemon: counted rows at both censuses, named rows, delta rows — rows, not effects; the daughters' row (26:33)
# and Jochebed's row (26:59) its first consumers. Five motions of the deliverable rule, the wrap the sixth; every cell cites its source;
# every token probed (zero-report law); effects on every cell (the effects law); one HYPOTHESIS cell (class H) counted apart.
# Reading ledger: logic/oral_triage/num_26_second_census_2026-09-11.md; the exam's docket: num_26_second_census_exam_2026-09-11.md.

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 70, ('the guard counted %d expectations, the tripwire holds 70' % GUARDED)   # the guard's own count on the first run
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections
import effects_layer as FX
import world_engine as WE
import cold_run_bamidbar as BM                   # THE EDGE: second_census -> bamidbar CALL, reference (the first roll's numbers the deltas are declared against)
import cold_run_balak as CB                      # THE EDGE: second_census -> balak CALL, reference (25:19 'after THE PLAGUE' — its 24,000)
import cold_run_korach as KR                     # THE EDGE: second_census -> korach CALL, reference (26:9-11 recalls the company; the 14,700 and the 250; the death-mode row)
import cold_run_shelach as SH                    # THE EDGE: second_census -> shelach CALL, reference (26:64-65 consumes the decree of 14:29-35)
import cold_run_zelophehad as ZL                 # THE EDGE: second_census -> zelophehad CALL, reference (26:33 the daughters' row; 26:53-56 the land row)
import cold_run_joseph as JO                     # THE EDGE: second_census -> joseph CALL, reference (26:59 'in Egypt' — CJ3b's witness; Genesis 46's roster)
import cold_run_chukat as CK                     # THE EDGE: second_census -> chukat CALL, reference (26:1 Eleazar for Aaron — 20:28's succession)
import cold_run_shemini_day as SD                # THE EDGE: second_census -> shemini_day CALL, reference (26:61 'strange fire' = Lev 10:1)

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, verse_words = _INK['ink_numbers'], _INK['verse_words']

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs, book='Num'):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

def words(ch, vs, book='Num'):
    return verse_text(ch, vs, book).split()

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed) ----------------
PROBES = [
    ('המגפה',  25, 19, 'the plague — the half-verse, the marker'),
    ('אלעזר',  26, 1,  'Eleazar — the son for the father'),
    ('שאו',    26, 2,  'lift [the head] — 1:2\'s idiom'),
    ('וידבר',  26, 3,  'and spoke — the verb without its object'),
    ('אתם',    26, 3,  'them — the object without its verb'),
    ('היצאים', 26, 4,  'who came out — the exodus generation'),
    ('בכור',   26, 5,  'firstborn — plene (1:20 and Gen 46:8 defective)'),
    ('ובני',   26, 8,  'and the sons of [Pallu: Eliab] — the plural for one'),
    ('אליאב',  26, 8,  'Eliab'),
    ('הוא',    26, 9,  'this is [Dathan and Abiram]'),
    ('בהצתם',  26, 9,  'when they strove — the verb\'s one Torah seat'),
    ('ותבלע',  26, 10, 'and swallowed'),
    ('לנס',    26, 10, 'for a sign — the pole-word'),
    ('מתו',    26, 11, '[did not] die — the sons of Korach'),
    ('ומאתים', 26, 14, 'and two hundred — Simeon\'s bare summary'),
    ('וימת',   26, 19, 'and died — Er and Onan'),
    ('הוליד',  26, 29, 'begot — Machir, the full spelling'),
    ('בנות',   26, 33, 'daughters — the daughters\' row'),
    ('שרח',    26, 46, 'Serah'),
    ('ואלף',   26, 51, 'and a thousand — the addend'),
    ('בנחלה',  26, 53, 'for an inheritance'),
    ('במספר',  26, 53, 'by the number [of names] — 1:2\'s phrase'),
    ('תרבה',   26, 54, 'you shall increase'),
    ('אך',     26, 55, 'only — the restrictor'),
    ('בגורל',  26, 55, 'by lot'),
    ('פי',     26, 56, 'the mouth of [the lot]'),
    ('הולד',   26, 58, 'begot — Kohath, the defective spelling'),
    ('ילדה',   26, 59, 'she bore — subjectless'),
    ('זרה',    26, 61, 'strange [fire]'),
    ('נחלה',   26, 62, 'inheritance — none given them'),
    ('איש',    26, 64, 'a man — not a man of those'),
    ('כלב',    26, 65, 'Caleb'),
    ('משפחת',  26, 5,  'the family of — the roll\'s word'),
    ('הימנה',  26, 44, 'the Imnah — the one family without its yod'),
    ('השוחמי', 26, 43, 'the Shuhamite — Dan\'s one family'),
]
for tok, ch, vs, note in PROBES:
    if tok not in words(ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Num %d:%d — refusing to run' % (tok, note, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

P = []  # the provenance trail of the case being run
def ink(ref, note):  P.append(('INK',  'Num %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))
def hyp(note):       P.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)

# ---- THE NUMBERS, computed from the ink by the engine's parser (live; the probes' expectations are the ink's) ----
def N(ch, vs, book='Num'): return ink_numbers(verse_words(book, ch, vs))
TRIBES = ['reuben', 'simeon', 'gad', 'judah', 'issachar', 'zebulun', 'manasseh', 'ephraim', 'benjamin', 'dan', 'asher', 'naphtali']   # the roll's order (26:5-50) — Manasseh before Ephraim
COUNT_VERSE = dict(zip(TRIBES, (7, 14, 18, 22, 25, 27, 34, 37, 41, 43, 47, 50)))
C26 = {t: N(26, v)[0] for t, v in COUNT_VERSE.items()}
C1 = dict(BM.TWELVE)                                          # THE CALL: the first roll's twelve, the parser's at 1:20-43
TOTAL26, TOTAL1 = N(26, 51)[0], BM.TOTAL
DELTA = {t: C26[t] - C1[t] for t in TRIBES}
LEV26, LEV1, HOUSES = N(26, 62)[0], BM.LEV_WRITTEN, dict(BM.HOUSES)
PLAGUE, K_PLAGUE, K250, TWENTY = CB.COUNT[0], KR.PLAGUE, N(26, 10)[0], (N(26, 2), N(26, 4))
PEOR_COUNT = CB.peor({'ask': 'plague_count'}, CB.DATA)[0]          # THE CALL (the live edge the dependency gate demands — a constant read alone is not a call form): Balak's count cell
assert sum(C26.values()) == TOTAL26 and sum(C1.values()) == TOTAL1, (sum(C26.values()), TOTAL26, sum(C1.values()), TOTAL1)
assert TOTAL1 - TOTAL26 == 1820 and DELTA['simeon'] == -37100 and TWENTY == ([20], [20]) and K250 == 250 and PLAGUE == 24000 and K_PLAGUE == 14700, (DELTA, TWENTY, K250, PLAGUE, K_PLAGUE)
FELL = [t for t in TRIBES if DELTA[t] < 0]; ROSE = [t for t in TRIBES if DELTA[t] > 0]

# THE FAMILIES BY THE INK'S PATTERN: 'the family of' + the gentilic inside each tribe's span; the three tribe-gentilic summaries and Dan's
# 'all the families of' summary set aside; the one yod-less gentilic ('the family of THE IMNAH', 26:44) kept — the reading's fifty-seven
TSPAN = {'reuben': (5, 6), 'simeon': (12, 13), 'gad': (15, 17), 'judah': (19, 21), 'issachar': (23, 24), 'zebulun': (26, 26), 'manasseh': (29, 33), 'ephraim': (35, 36), 'benjamin': (38, 40), 'dan': (42, 43), 'asher': (44, 46), 'naphtali': (48, 49)}
def gentilics(lo, hi):
    out_ = []
    for v in range(lo, hi + 1):
        ws = words(26, v)
        for i, x in enumerate(ws):
            if x == 'משפחת' and i + 1 < len(ws) and i >= 1 and ws[i - 1] != 'כל':
                g = ws[i + 1]
                if g.startswith('ה') and g not in ('הראובני', 'השמעני', 'הזבולני'):
                    out_.append((v, g))
    return out_
GENT = {t: gentilics(*TSPAN[t]) for t in TRIBES}
FAMILIES = {'reuben': ['Hanoch', 'Pallu', 'Hezron', 'Carmi'], 'simeon': ['Nemuel', 'Jamin', 'Jachin', 'Zerah', 'Shaul'],
            'gad': ['Zephon', 'Haggi', 'Shuni', 'Ozni', 'Eri', 'Arod', 'Areli'], 'judah': ['Shelah', 'Perez', 'Zerah', 'Hezron', 'Hamul'],
            'issachar': ['Tola', 'Puvah', 'Jashub', 'Shimron'], 'zebulun': ['Sered', 'Elon', 'Jahleel'],
            'manasseh': ['Machir', 'Gilead', 'Iezer', 'Helek', 'Asriel', 'Shechem', 'Shemida', 'Hepher'], 'ephraim': ['Shuthelah', 'Becher', 'Tahan', 'Eran'],
            'benjamin': ['Bela', 'Ashbel', 'Ahiram', 'Shephupham', 'Hupham', 'Ard', 'Naaman'], 'dan': ['Shuham'],
            'asher': ['Imnah', 'Ishvi', 'Beriah', 'Heber', 'Malchiel'], 'naphtali': ['Jahzeel', 'Guni', 'Jezer', 'Shillem']}
for t in TRIBES:
    assert len(GENT[t]) == len(FAMILIES[t]), (t, GENT[t], FAMILIES[t])       # the typed names against the ink's gentilic count, tribe by tribe
NFAM = sum(len(FAMILIES[t]) for t in TRIBES)
assert NFAM == 57, NFAM
FAM_OF = sum(1 for v in range(1, 66) for x in words(26, v) if x == 'משפחת'); FAM_OF_1 = sum(1 for v in range(1, 55) for x in words(1, v) if x == 'משפחת')
assert (FAM_OF, FAM_OF_1) == (78, 0), (FAM_OF, FAM_OF_1)
LEV_HOUSES = ['Gershon', 'Kohath', 'Merari']; LEV_FAM26 = ['Libni', 'Hebron', 'Mahli', 'Mushi', 'Korah']; LEV_FAM3 = ['Libni', 'Shimei', 'Amram', 'Izhar', 'Hebron', 'Uzziel', 'Mahli', 'Mushi']
assert [g for _, g in gentilics(57, 57)] == ['הגרשני', 'הקהתי', 'המררי'] and len(gentilics(58, 58)) == 5, (gentilics(57, 57), gentilics(58, 58))
LEV_GONE = [f for f in LEV_FAM3 if f not in LEV_FAM26]; LEV_IN = [f for f in LEV_FAM26 if f not in LEV_FAM3]
assert LEV_GONE == ['Shimei', 'Amram', 'Izhar', 'Uzziel'] and LEV_IN == ['Korah'], (LEV_GONE, LEV_IN)
# GENESIS 46 AGAINST 26 — the tokens: five absent, nine renamed (the Genesis form absent, the Numbers form present), two moved a generation
def has(tok, lo, hi, ch=26, book='Num'): return any(tok in words(ch, v, book) for v in range(lo, hi + 1))
ABSENT = [('Ohad', 'ואהד', 'simeon'), ('Becher', 'ובכר', 'benjamin'), ('Gera', 'גרא', 'benjamin'), ('Rosh', 'וראש', 'benjamin'), ('Ishvah', 'וישוה', 'asher')]
for name, tok, t in ABSENT:
    assert not has(tok, *TSPAN[t]) and not has(tok.lstrip('ו'), *TSPAN[t]), (name, tok)
RENAMED = [('Jemuel', 'ימואל', 'Nemuel', 'לנמואל', 'simeon'), ('Zohar', 'וצחר', 'Zerah', 'לזרח', 'simeon'), ('Ziphion', 'צפיון', 'Zephon', 'לצפון', 'gad'), ('Ezbon', 'ואצבן', 'Ozni', 'לאזני', 'gad'),
           ('Iob', 'ויוב', 'Jashub', 'לישוב', 'issachar'), ('Ehi', 'אחי', 'Ahiram', 'לאחירם', 'benjamin'), ('Muppim', 'מפים', 'Shephupham', 'לשפופם', 'benjamin'), ('Huppim', 'וחפים', 'Hupham', 'לחופם', 'benjamin'), ('Hushim', 'חשים', 'Shuham', 'לשוחם', 'dan')]
for g, gt, n, nt, t in RENAMED:
    assert not has(gt, *TSPAN[t]) and has(nt, *TSPAN[t]), (g, n, t)
MOVED = [('Ard', 'וארד', 'ארד', 40), ('Naaman', 'ונעמן', 'לנעמן', 40)]   # 26:40 "the sons of Bela: ARD and Naaman... of Naaman" — Ard bare, Naaman with the preposition at its family (measured: the first run's assert)
for n, gt, nt, v in MOVED:
    assert gt in words(46, 21, 'Gen') and nt in words(26, v), (n, v)     # Benjamin's sons at 46:21, 'the sons of Bela' at 26:40
BECHER_EPHRAIM = 'לבכר' in words(26, 35)
assert BECHER_EPHRAIM
ER_ONAN = words(26, 19)[1:] ; ER_ONAN_GEN = words(46, 12, 'Gen')
assert 'וימת' in ER_ONAN and 'ער' in ER_ONAN and 'ואונן' in ER_ONAN and 'וימת' in ER_ONAN_GEN, (ER_ONAN, ER_ONAN_GEN)
SEVENS = JO.seventy('subtotals_parsed')['v']; LIVING = JO.seventy('leah_living_named')['v']; JOCHEBED_CELL = JO.seventy('jochebed')['v']; DIVERGE_CELL = JO.seventy('diverge')['v']   # THE CALL
assert SEVENS == (33, 16, 14, 7) and LIVING == 32, (SEVENS, LIVING)
LAND_ROW = ZL.DATA['land_divided_among']                                                                  # THE CALL: the row READ, never re-declared
PLEA = ZL.the_daughters({'ask': 'plea'}, ZL.DATA)[0]; HEIR = ZL.heir_of({'daughter': True, 'son': False, 'sons_line': False, 'brothers': True})[0]   # THE CALL
NAMES_ORDER = ZL.the_daughters({'ask': 'names_order'}, ZL.DATA)[0]; TEN_PARTS = ZL.the_daughters({'ask': 'the_run'}, ZL.DATA)[0]; THREE = ZL.the_daughters({'ask': 'three_portions'}, ZL.DATA)[0]
UNCERTAIN = ZL.the_daughters({'ask': 'uncertainty'}, ZL.DATA)[0]; REACH = ZL.the_daughters({'ask': 'reach'}, ZL.DATA)[0]; LAPSE = ZL.the_daughters({'ask': 'lapse'}, ZL.DATA)[0]
FIRSTBORN_DOUBLE = ZL.inheritance_order({'ask': 'firstborn_double', 'property': 'fathers'}, ZL.DATA)[0]
DECREE_SET = SH.decree({'ask': 'set'}, SH.DATA)[0]; EXCEPTIONS = SH.decree({'ask': 'exceptions'}, SH.DATA)[0]; CEASED = SH.decree({'ask': 'deaths_ceased'}, SH.DATA)[0]; CEASED_DAY = SH.DATA['deaths_ceased']['value']   # THE CALL
K_MODE = KR.DATA['korach_death_mode']; K_DISPUTE = KR.DATA['maintaining_a_dispute']['value']; K_MOUTH = KR.DATA['earth_mouth']['value']; K_SONS = KR.DATA['sons_of_korach']['value']   # THE CALL
K_COUNT = KR.plague_and_staffs({'ask': 'plague_count'}, KR.DATA)[0]; K_250 = KR.rebellion({'ask': 'two_hundred_fifty'}, KR.DATA)[0]
SUCCESSION = CK.edom_and_hor({'ask': 'succession'}, CK.DATA)[0]                                            # THE CALL
STRANGE_FIRE = SD.fire('fire_status')['v']                                                                 # THE CALL
LINEAGE = BM.census({'ask': 'lineage'}, BM.DATA)[0]; LEV_DELTA = BM.levites({'ask': 'delta'}, BM.DATA)[0]  # THE CALL
def _me(ws):
    return any((ws[i] == 'משה' and i + 2 < len(ws) and ws[i + 1] == 'ואל' and ws[i + 2] == 'אלעזר') or (ws[i] == 'משה' and i + 1 < len(ws) and ws[i + 1] == 'ואלעזר') for i in range(len(ws)))
ME_SEATS = [(c, v) for c in range(1, 37) for v in range(1, 90) if verse_text(c, v) and _me(words(c, v))]   # 'Moses and Eleazar' ADJACENT in Numbers (measured on the DB before it was typed)
assert ME_SEATS[:2] == [(20, 28), (26, 1)] and len(ME_SEATS) == 10, ME_SEATS   # the pair's first seat the succession's own verse (20:28), the second the census's command
FOURTEEN_30 = words(14, 30)[-7:]; assert FOURTEEN_30 == words(26, 65)[-7:], (FOURTEEN_30, words(26, 65)[-7:])   # 14:30's last seven words verbatim at 26:65


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'plague_tribe': {'value': 'simeon_by_the_shelf', 'settings': {
        'simeon_by_the_shelf': "the 24,000 of 25:9 read as Simeon's — the reading's SIMEON'S CENSUS FALLS (Onkelos Num 25:9 at sitting 7): Zimri a prince of Simeon (25:14), the tribe's fall 59,300 -> 22,200 the largest; the ink names Zimri's tribe and never the dead's",
        'unassigned_by_the_ink': "the ink writes 'the dead in the plague were twenty and four thousand' (25:9) with no tribe: the delta row's explanation carries the shelf's arm, the ink's silence the other"},
        'source': "25:9 and 26:14 — the ink gives the count and the fall, not the join"},
    'spies_protesters_portions': {'value': 'juxtaposed', 'settings': {
        'juxtaposed': "one sage juxtaposes the protesters to the spies — Joshua and Caleb took the spies' AND the protesters' portions (Bava Batra 118b:4, 118b:6); Abaye: the protesters = Korach's two hundred and fifty (118b:7); their sons took by the grandfathers on the left-Egypt arm (117b:2, 119a:2)",
        'not_juxtaposed': "one sage does not: the protesters had no portion at all (118b:4, 118b:6); on the entrants' arm the sons took in their own merit (119a:2; Tosefta 7:10)"},
        'source': "26:64-65 names the dead of the first roll and the two exceptions; who bequeathed among the dead is the shelf's"},
    'compensation_mode': {'value': 'money', 'settings': {'money': "R. Eliezer: the tribes compensated with money — near Jerusalem against far (Bava Batra 122a:10-11)", 'land': "R. Yehoshua: with land (122a:11)"},
                          'source': "26:56 'between the many and the few' read as value (122a:2, 122a:10)"},
    'division_by': {'value': 'tribes', 'settings': {'tribes': "twelve equal wholes, the individuals' shares within a tribe by its numbers — 'according to the lot... between the many and the few' (26:56; Bava Batra 122a:1, 122a:8)", 'skulls': "a measure per man, the tribe's size its population — the dilemma's other horn (121b:12), refused"},
                    'source': "26:53-56 gives both rules (by count, by lot) and names no order between the levels"},
    'decree_age_edges': {'value': 'twenty_to_sixty_levi_outside', 'settings': {'twenty_to_sixty_levi_outside': "the decree of 14:29 on 'twenty years old and upward' — the census's count: Levi outside, counted from thirty (Rav Hamnuna, Bava Batra 121b:8); under twenty and over sixty outside by 'and upward' / 'and upward' with the valuations, Lev 27:7 (Rav Acha bar Yaakov, 121b:11)"},
                         'source': "26:64's predicate is on 'those counted by Moses and Aaron' (1:2-3's twenty and upward); the Levites apart (26:62)"},
    'wilderness_survivors': {'value': 'yair_machir_nobah_serah_jochebed', 'settings': {'yair_machir_nobah_serah_jochebed': "Yair and Machir sons of Manasseh born in Jacob's days, died after the entry — Josh 7:5 'about thirty-six' (Bava Batra 121b:9-10: R. Yehuda thirty-six literally / R. Nechemya Yair alone); Nobah; Serah on both rolls (Gen 46:17, Num 26:46) and Jochebed (26:59) — Seder Olam Rabbah 9:2; Sotah 13a:14"},
                             'source': "26:65 'not a man of them except Caleb and Joshua' — the shelf's exceptions beyond the ink's two"},
    'jochebed_age': {'value': 130, 'settings': {130: "210 years in Egypt, Moses eighty at the exodus, Jochebed born within the walls — 130 at Moses' birth; 'a daughter' (Exod 2:1) by her youth reborn (Bava Batra 120a:2; Sotah 12a:15 — Rav Yehuda bar Zevida / R. Yehuda)"},
                     'source': "26:59 'whom she bore to Levi in Egypt' — born in Egypt, conceived on the way (Bava Batra 123b:1; Sotah 12a:14)"},
    'hu_rule': {'value': 'same_from_beginning_to_end', 'settings': {'same_from_beginning_to_end': "'this is [hu] Dathan and Abiram' (26:9) — the formula marks one unchanged in wickedness from beginning to end: Esau (Gen 36:43), Ahaz, Ahasuerus (Megillah 11a:17)"}, 'source': "26:9's 'hu'"},
    'single_son_plural': {'value': 'sons_for_one_not_grandson', 'settings': {'sons_for_one_not_grandson': "'the sons of Pallu: Eliab' (26:8) proves 'sons' for ONE son (Rava, Bava Batra 143b:6; Gen 46:23's Hushim disputed); a grandson is not called a son (Mar bar Rav Ashi, 143b:7) — Ard and Naaman under Bela (26:40) where Gen 46:21 lists them as Benjamin's"}, 'source': "26:8, 26:40"},
    'thirteen_tribes': {'value': 'twelve_now_thirteen_to_come', 'settings': {'twelve_now_thirteen_to_come': "initially twelve tribes (Levi no portion — 26:62); thirteen in the future, the thirteenth the king's (Ezek 48:19-21; Bava Batra 122a:2, 122a:9)"}, 'source': "26:53-56 with 26:62"},
    'urim_judgment': {'value': 'final', 'settings': {'final': "a prophet's decree may be retracted, the Urim's not — 'by the JUDGMENT of the Urim' (27:21; Yoma 73b:3); the lot's mouth is the Urim's (Bava Batra 122a:3): 27:21 outside this span (Joshua's appointment, 27:12-23, not compiled at THE TENT — a readback line)"}, 'source': "26:56 'by the mouth of the lot'"},
    'levite_families_delta': {'value': 'four_gone_one_in', 'settings': {'four_gone_one_in': "26:58's five (Libni, Hebron, Mahli, Mushi, Korah) against 3:17-20's eight (Libni, Shimei; Amram, Izhar, Hebron, Uzziel; Mahli, Mushi): Shimei, Amram, Izhar and Uzziel gone, Korah's in — the ink states no reason; the tradition silent on the four"}, 'source': "26:57-58 against 3:17-20 — the table's own delta"},
}


# ===== F1: THE COMMAND (Num 25:19-26:4) =====================================================================
def the_command(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'addressees':
        ink('26:1', '"and the LORD said to Moses AND TO ELEAZAR son of Aaron the priest" — the son for the father (1:1 to Moses alone; 1:3 "you and Aaron")')
        move('CALLED cold_run_chukat.edom_and_hor(succession) -> %s [IMPORT, live]' % SUCCESSION, '"Moses and Eleazar" adjacent at %d seats in Numbers — the first 20:28 (the succession\'s own verse), the second here (computed: %s)' % (len(ME_SEATS), ME_SEATS))
        return out('to Moses and to Eleazar — the son for the father since 20:28', ['accepted'])
    if ask == 'lift_the_head':
        ink('26:2', '"lift the head of all the congregation of the children of Israel from twenty years old and upward by their fathers\' houses, everyone going out to the host in Israel" — 1:2-3\'s formula with FIVE clauses dropped (by their families; by the number of names; every male; by their skulls; you and Aaron); the threshold %s' % TWENTY[0])
        move('M-23 exemplar 16 (MOVE_CATALOG.md)', 'the second seat\'s delta — the first count\'s clauses dropped at the second')
        return out('twenty and upward, the host — 1:2-3 shortened by five', ['commanded'])
    if ask == 'spoke_them':
        ink('26:3', '"and Moses and Eleazar the priest spoke THEM in the plains of Moab" — the object without its verb; Onkelos supplies "to count them" (the reading\'s cut)')
        return out('the verb supplied by the translation: to count them', ['accepted'])
    if ask == 'after_the_plague':
        ink('25:19', '"and it was after the plague" — the half-verse (the export joins it into 26:1); no day in the ink')
        move('Seder Olam Rabbah 9:2', 'the ORDER after Og — Arvot Moab, the plague, the census, the daughters; no day: the marker READING-PLACED at the counter\'s own day (40, 6, 1)')
        return out('after the plague — the order the shelf\'s, the day the counter\'s: reading-placed', ['accepted'])
    if ask == 'exodus_generation':
        ink('26:4', '"as the LORD commanded Moses and the children of Israel WHO CAME OUT of the land of Egypt" — the first roll\'s generation named at the second\'s head; the predicate at 26:64 closes on them')
        return out('the exodus generation named at the second roll\'s head', ['counted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE ROLL (Num 26:5-51) ============================================================================
def the_roll(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'twelve_counts':
        ink('26:7-50', 'the twelve counts by the parser: %s' % ', '.join('%s %d' % (t, C26[t]) for t in TRIBES))
        move('CALLED cold_run_bamidbar.TWELVE [IMPORT, live]', 'the first roll\'s twelve: %s' % ', '.join('%s %d' % (t, C1[t]) for t in TRIBES))
        return out('twelve at both seats, the parser\'s', ['counted'])
    if ask == 'total':
        ink('26:51', '"these are the counted of the children of Israel: six hundred thousand AND A THOUSAND seven hundred and thirty" — %d, the thousand an addend (1b\'s rule at its second census); the twelve sum to it' % TOTAL26)
        move('CALLED cold_run_bamidbar.census(total) -> %s [IMPORT, live]' % BM.census({'ask': 'total'}, BM.DATA)[0], '1:46\'s %d' % TOTAL1)
        return out('%d = the twelve summed; 603,550 at the first roll' % TOTAL26, ['counted'])
    if ask == 'deltas':
        ink('26:7-50 against 1:20-43', 'the deltas %s' % ', '.join('%s %+d' % (t, DELTA[t]) for t in TRIBES))
        dat('DECLARED numbers: the ink gives two counts and no births or deaths between them — five fell (%s: %d), seven rose (%s: %+d), the whole %+d; nothing derivable' % (', '.join(FELL), sum(DELTA[t] for t in FELL), ', '.join(ROSE), sum(DELTA[t] for t in ROSE), TOTAL26 - TOTAL1))
        return out('five fell, seven rose, the whole -1820 — declared, not derived', ['counted'])
    if ask == 'simeons_gap':
        ink('26:14', '"the families of the Simeonite: twenty and two thousand and two hundred" — %d, the ONE summary without the count-word; 1:23\'s %d' % (C26['simeon'], C1['simeon']))
        move('CALLED cold_run_balak.peor(plague_count) -> %s [IMPORT, live]' % PEOR_COUNT, '25:9\'s dead in the plague — the parser\'s %d' % PLAGUE)
        dat('the row plague_tribe = %s: %s' % (data['plague_tribe']['value'], data['plague_tribe']['settings'][data['plague_tribe']['value']]))
        return out('-37100 against the plague\'s 24000: 13100 unexplained', ['counted'])
    if ask == 'korachs_dead':
        ink('26:10', '"when the fire consumed the two hundred and fifty men" — %d by the parser; 17:14\'s plague 14,700 not recalled here' % K250)
        move('CALLED cold_run_korach.plague_and_staffs(plague_count) -> %s; rebellion(two_hundred_fifty) -> %s [IMPORT, live]' % (K_COUNT, K_250), 'no tribe in the ink for either — Dathan and Abiram Reubenites, Korah a Levite, the 14,700 unassigned')
        return out('14700 and 250 carry no tribe — no delta row explained by them', ['counted'])
    if ask == 'families':
        ink('26:5-50', '"of Hanoch, the family of the Hanochite" — the pattern %d times in the twelve tribes: %s' % (NFAM, ', '.join('%s %d' % (t, len(FAMILIES[t])) for t in TRIBES)))
        ink('26 against 1', '"family of" %d tokens in chapter 26, %d in chapter 1 (computed)' % (FAM_OF, FAM_OF_1))
        move('CALLED cold_run_bamidbar.census(lineage) -> %s [IMPORT, live]' % LINEAGE, 'the family is the father\'s (Bava Batra 109b) — the roll\'s registers keyed to the fathers')
        return out('57 families in twelve tribes; the family of 78 against 0', ['accepted'])
    if ask == 'genesis_46':
        ink('26:5-50 against Gen 46:8-25', 'five absent (%s), nine renamed (%s), two moved a generation (%s — Benjamin\'s sons at 46:21, "the sons of Bela" at 26:40); a Becher under Ephraim (26:35)' % (', '.join(n for n, _, _ in ABSENT), ', '.join('%s/%s' % (g, n) for g, _, n, _, _ in RENAMED), ', '.join(n for n, _, _, _ in MOVED)))
        move('CALLED cold_run_joseph.seventy(subtotals_parsed) -> %s; (leah_living_named) -> %s [IMPORT, live]' % (SEVENS, LIVING), 'the descent\'s registers')
        dat('the row single_son_plural = %s' % data['single_son_plural']['value'])
        return out('5 absent, 9 renamed, 2 moved — the table keyed to Genesis 46', ['souls_counted'])
    if ask == 'er_and_onan':
        ink('26:19', '"and Er and Onan died in the land of Canaan" — Gen 46:12\'s clause verbatim on the roll')
        return out('died in the land of Canaan — 46:12 verbatim', ['souls_counted'])
    if ask == 'korach_recalled':
        ink('26:9-10', '"who strove against Moses and against Aaron in the company of Korach when they strove against the LORD; and the earth opened its mouth and swallowed them WITH KORACH when that company died, when the fire consumed the two hundred and fifty men" — both deaths in one verse; "who strove" the verb\'s one Torah seat')
        move('CALLED cold_run_korach.DATA[korach_death_mode] = %s [IMPORT, live]' % K_MODE['value'], 'Sanhedrin 110a:13 (R. Yochanan: neither — the plague; 26:10 read to EXCLUDE him from the fire) against 110a:14 (the outside teaching: both — 26:10 "with Korach"); CK4 OPEN')
        dat('the row hu_rule = %s' % data['hu_rule']['value'])
        return out('both deaths on one verse; the mode the Korach runner\'s open row', ['accepted'])
    if ask == 'sons_of_korach':
        ink('26:11', '"and the sons of Korach did not die" — the roll\'s one negation of a death')
        move('CALLED cold_run_korach.DATA[sons_of_korach] = %s [IMPORT, live]' % K_SONS, 'Sanhedrin 110a:17 — a place fortified for them; the eleven psalms the reading\'s count')
        return out('the sons of Korach did not die', ['accepted'])
    if ask == 'single_son_plural':
        ink('26:8', '"and the SONS of Pallu: Eliab" — one son under the plural; 26:40 "the sons of Bela: Ard and Naaman" — grandsons under "sons"')
        move('Bava Batra 143b:6 (Rava); 143b:7 (Mar bar Rav Ashi)', '"sons" for one son proved from this verse; a grandson not called a son')
        return out('sons for one son (26:8); a grandson not a son — the roll\'s Ard and Naaman', ['accepted'])
    if ask == 'hu_dathan':
        ink('26:9', '"THIS IS Dathan and Abiram, the called of the congregation" — 1:16\'s pair reversed here (the written and read forms)')
        move('Megillah 11a:17', '"this is" — the same from beginning to end')
        return out('this is Dathan and Abiram — the same from beginning to end', ['accepted'])
    if ask == 'daughters_row':
        ink('26:33', '"and Zelophehad son of Hepher had no sons, only daughters; and the names of the daughters of Zelophehad: Mahlah, Noah, Hoglah, Milcah and Tirzah" — the case\'s premise as a census row BEFORE the plea (27:1); the order = 27:1\'s')
        move('CALLED cold_run_zelophehad.the_daughters(plea) -> %s; heir_of(daughter only) -> %s; the_daughters(names_order) -> %s [IMPORT, live]' % (PLEA, HEIR, NAMES_ORDER), 'the inheritance engine answers from the roll\'s premise')
        return out('no sons, only daughters — the premise on the roll; the heir the daughter', ['holding_owed'])
    if ask == 'serah':
        ink('26:46', '"and the name of the daughter of Asher was Serah" — Gen 46:17 and 1 Chr 7:30 the other two rosters')
        move('Sotah 13a:14; Seder Olam Rabbah 9:2', 'remained from the descent\'s generation — showed Moses Joseph\'s grave; on both rolls')
        dat('the row wilderness_survivors = %s' % data['wilderness_survivors']['value'])
        return out('Serah on three rosters — the shelf\'s survivor of both rolls', ['souls_counted'])
    if ask == 'reuben_firstborn':
        ink('26:5', '"Reuben the firstborn of Israel" — plene here, defective at 1:20 and Gen 46:8 (the reading\'s crown)')
        move('Bava Batra 123a:4-5', '1 Chr 5:1-2: the birthright given to Joseph\'s sons — the roll keeps Reuben\'s title')
        return out('the firstborn kept on the roll; the birthright Joseph\'s by Chronicles', ['accepted'])
    if ask == 'ephraim_manasseh_order':
        ink('26:28-37', '"the sons of Joseph by their families: Manasseh and Ephraim" — Manasseh FIRST here (%d), Ephraim first at 1:32-35; Joseph\'s two counted as tribes among the twelve while Levi stands apart' % C26['manasseh'])
        move('Bava Batra 123a:10 (Abaye)', '"Ephraim and Manasseh as Reuben and Simeon" (Gen 48:5) — two full portions: Joseph\'s double on the census\'s face')
        return out('Joseph\'s two as tribes — Manasseh first at the second roll', ['counted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE LAND (Num 26:52-56) ============================================================================
def the_land(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'by_number_of_names':
        ink('26:53-54', '"to these the land shall be divided for an inheritance BY THE NUMBER OF NAMES; to the many you shall increase their inheritance and to the few you shall diminish, to each according to his counted" — the SIZE by the count; 1:2\'s counting phrase returned as the land\'s (33:54, 35:8 the plural)')
        return out('the size by the count of names — to the many increase, to the few diminish', ['commanded'])
    if ask == 'by_lot':
        ink('26:55', '"ONLY by lot shall the land be divided; by the names of the tribes of their fathers they shall inherit" — the PLACE by lot; Joshua 14-19 the run')
        move('Sanhedrin 43b:6', 'Joshua to Achan: do not slander the lots, the land will be divided by them (26:55)')
        return out('the place by lot — Joshua 14-19 the run', ['commanded'])
    if ask == 'lots_mouth':
        ink('26:56', '"BY THE MOUTH OF THE LOT shall its inheritance be divided between the many and the few" — the lot has a mouth; Onkelos keeps it')
        move('Bava Batra 122a:3-6', 'only by lot AND only with the Urim: Eleazar in the Urim, two receptacles (the tribes, the boundaries), the Spirit naming the pair before the lots emerge')
        dat('the row urim_judgment = %s' % data['urim_judgment']['value'])
        return out('the lot\'s mouth is the oracle\'s — two receptacles before Eleazar', ['accepted'])
    if ask == 'land_divided_among':
        ink('26:53 against 26:55', '"to these" against "by the names of the tribes of their fathers" — two verses, no rule between them')
        move('CALLED cold_run_zelophehad.DATA[land_divided_among] = %s [IMPORT, live] — the row READ, never re-declared' % LAND_ROW['value'], 'the arms: %s (Sifrei 132:1; Bava Batra 117a:2-117b:1; Rebbi\'s parable 117a:4)' % ', '.join(LAND_ROW['settings']))
        return out('left_egypt (the running setting) — entered and both recorded; the dead inherit the living', ['accepted'])
    if ask == 'only_excludes':
        ink('26:55', '"ONLY by lot" — the restrictor')
        move('Sifrei Bamidbar 132:3 (E2); Bava Batra 122a:12, 122b:2', '"only" excludes Joshua and Caleb — Joshua by the LORD\'s word at Timnath-serah (Josh 19:50), Caleb\'s Hebron as Moses had spoken (Judg 1:20) with its outskirts (Josh 21:12): the same two 26:65 excepts')
        return out('Joshua and Caleb excluded from the lot — 26:65\'s two', ['exempt'])
    if ask == 'tribes_or_skulls':
        ink('26:56', '"between the many and the few"')
        move('Bava Batra 121b:12 -> 122a:1-2, 122a:8', 'the dilemma resolved: BY TRIBES — twelve equal wholes, the individuals within by their numbers')
        dat('the row division_by = %s' % data['division_by']['value'])
        return out('by tribes, then by numbers within — the table\'s two levels', ['accepted'])
    if ask == 'compensation':
        move('Bava Batra 122a:2, 122a:10-11', '"between the many and the few" as value — near Jerusalem against far; R. Eliezer money / R. Yehoshua land')
        dat('the row compensation_mode = %s' % data['compensation_mode']['value'])
        return out('compensated — money (R. Eliezer; land recorded)', ['accepted'])
    if ask == 'spies_portions':
        ink('26:64-65', 'the first roll\'s dead; the two exceptions')
        move('Bava Batra 117b:2, 118b:3-7', 'Joshua and Caleb took the spies\' portions (14:38 "lived"); the protesters and Korach\'s assembly — juxtaposed or not; Abaye: the protesters = the %s' % K_250.split(' — ')[0])
        dat('the row spies_protesters_portions = %s' % data['spies_protesters_portions']['value'])
        return out('the spies\' portions to Joshua and Caleb; the protesters\' by the row', ['holding_owed'])
    if ask == 'children_excluded':
        ink('26:53', '"to these" — the counted, twenty and upward (26:2)')
        move('Bava Batra 117a:2; 119a:3', '"to these" = like these, above twenty: the children excluded; on the entrants\' arm twenty at the entry')
        return out('the children excluded — like these, above twenty', ['exempt'])
    if ask == 'the_estimate':
        ink('26:54', '"to the many... to the few"')
        move('Sifrei Bamidbar 132:4; Mishnah Bava Batra 7:1-4', '"between many and few" read as worth — a kor\'s-space against a seah\'s-space; the sale by measure the vocabulary; no measure in the ink')
        return out('the estimate by worth — a kor\'s-space against a seah\'s-space', ['accepted'])
    if ask == 'joseph_protest':
        ink('26:34 against 1:35', 'Manasseh %+d — the roll\'s largest rise' % DELTA['manasseh'])
        move('Bava Batra 118a:4-7', 'Joshua 17:14 "one lot and one part" — on left-Egypt they had multiplied; the evil eye')
        return out('Joseph\'s protest grounded on the roll\'s rise', ['accepted'])
    if ask == 'ten_parts':
        ink('26:29-33', 'Manasseh\'s eight families with Hepher among them; the daughters')
        move('CALLED cold_run_zelophehad.the_daughters(the_run) -> %s; (three_portions) -> %s [IMPORT, live]' % (TEN_PARTS, THREE), 'Bava Batra 118b:8-10: six houses + four of the daughters = Josh 17:5\'s ten')
        return out('ten parts — six houses and the daughters\' four', ['holding_owed'])
    if ask == 'possession_before_assignment':
        move('Bava Batra 119a:1, 119a:5 (Rabba)', 'the land in possession before it is assigned — the firstborn\'s double on Hepher\'s portion')
        move('CALLED cold_run_zelophehad.inheritance_order(firstborn_double) -> %s [IMPORT, live]' % FIRSTBORN_DOUBLE, 'the double on the father\'s property')
        return out('in possession before assignment — the rows are holdings before the lot', ['holding_owed'])
    if ask == 'morasha':
        move('CALLED cold_run_zelophehad.the_daughters(uncertainty) -> %s [IMPORT, live]' % UNCERTAIN, 'Exod 6:8 "for a heritage"')
        move('Bava Batra 117b:3, 119b:3-4', 'resolved BOTH — an inheritance from the fathers in the exodus generation\'s possession, and the generation bequeaths without inheriting (Exod 15:17 "bring THEM in")')
        return out('morasha both ways — they bequeath and do not inherit', ['accepted'])
    if ask == 'thirteen_tribes':
        ink('26:62', '"for no inheritance was given them" — twelve portions, Levi none')
        dat('the row thirteen_tribes = %s' % data['thirteen_tribes']['value'])
        return out('twelve now, thirteen to come', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE LEVITES (Num 26:57-62) =========================================================================
def the_levites(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'five_for_eight':
        ink('26:57-58', 'three houses (%s) and FIVE families (%s) against 3:17-20\'s eight (%s): gone %s, in %s' % (', '.join(LEV_HOUSES), ', '.join(LEV_FAM26), ', '.join(LEV_FAM3), ', '.join(LEV_GONE), ', '.join(LEV_IN)))
        dat('the row levite_families_delta = %s' % data['levite_families_delta']['value'])
        return out('five for eight: Shimei, Amram, Izhar, Uzziel gone; Korah in', ['counted'])
    if ask == 'count':
        ink('26:62', '"and their counted were twenty and three thousand, every male from a month old and upward" — %d against 3:39\'s %d: %+d' % (LEV26, LEV1, LEV26 - LEV1))
        move('CALLED cold_run_bamidbar.levites(delta) -> %s [IMPORT, live]' % LEV_DELTA, 'the houses\' 22,300 against the 22,000 written — the shelf\'s three hundred')
        return out('23000 for 22000: +1000 unexplained', ['counted'])
    if ask == 'no_inheritance':
        ink('26:62', '"for they were not counted among the children of Israel, for no inheritance was given them among the children of Israel" — the two "for"s; the block of 18:20-24 on the Levites\' ledger since Korach, READ here, not rewritten')
        return out('not counted among — no inheritance: the 18:23-24 block read', ['inheritance_barred'])
    if ask == 'jochebed':
        ink('26:59', '"and the name of Amram\'s wife was Jochebed the daughter of Levi, WHOM SHE BORE — HER — TO LEVI IN EGYPT" — the verb perfect feminine with its object and no subject; "in Egypt" the datum')
        move('CALLED cold_run_joseph.seventy(jochebed) -> %s; (diverge) -> %s [IMPORT, live]' % (JOCHEBED_CELL, DIVERGE_CELL), 'Bava Batra 120a:1, 123b:1; Sotah 12a:14 — the seventy\'s missing one; CJ3b stays DIVERGE: the row is the witness, not a resolution')
        return out('born to Levi in Egypt — CJ3b\'s ink witness; the verdict stays DIVERGE', ['souls_counted'])
    if ask == 'jochebed_age':
        dat('the row jochebed_age = %s: %s' % (data['jochebed_age']['value'], data['jochebed_age']['settings'][130]))
        return out('130 at Moses\' birth — a daughter by her youth reborn', ['accepted'])
    if ask == 'amram_remarriage':
        ink('26:59', '"Amram\'s wife" — Exod 2:1\'s "took a daughter of Levi", 6:20 "his father\'s sister"')
        move('Sotah 12a:9-13; Bava Batra 120a:3', 'divorced at the decree, remarried by Miriam\'s counsel — the palanquin')
        return out('the remarriage the shelf\'s — the ink names the wife', ['accepted'])
    if ask == 'miriam':
        ink('26:59', '"and Miriam their sister" — the one woman inside the Levite roster')
        move('Sotah 12a:2-7', 'Azubah, Jerioth, Helah, Naarah — Miriam\'s names in Chronicles')
        return out('Miriam on the roll — her sister-clause', ['accepted'])
    if ask == 'nadab_abihu':
        ink('26:60-61', '"and Nadab and Abihu died when they brought near strange fire before the LORD" — 3:4 shortened by four clauses; Lev 10:1\'s clause')
        move('CALLED cold_run_shemini_day.fire(fire_status) -> %s [IMPORT, live]' % STRANGE_FIRE, 'the eighth day\'s fire; no entity for the two on the tape — the gap named')
        return out('died at the strange fire — Lev 10:1 recalled; no entity on the tape', ['accepted'])
    if ask == 'kohath_begot':
        ink('26:58', '"and Kohath BEGOT Amram" — the Torah\'s one defective token of the verb (26:29 Machir\'s full)')
        return out('Kohath begot Amram — the defective spelling', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE TWO ROLLS (Num 26:63-65) =======================================================================
def the_rolls(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'one_sentence_twice':
        ink('26:63-64', '"these are the counted by Moses and ELEAZAR the priest... in THE PLAINS OF MOAB" / "those counted by Moses and AARON the priest... in THE WILDERNESS OF SINAI" — one sentence twice, the priest and the place the deltas')
        return out('one sentence twice — the priest and the place', ['accepted'])
    if ask == 'membership_predicate':
        ink('26:64', '"and among these there was NOT A MAN of those counted by Moses and Aaron" — no name on both rolls; the table\'s named rows carry the ink\'s statuses')
        move('CALLED cold_run_shelach.decree(set) -> %s [IMPORT, live]' % DECREE_SET, 'the decree of 14:29-35 consumed; Deut 2:14-16 the retelling')
        return out('not a man of the first roll on the second — the decree consumed', ['accepted'])
    if ask == 'except_caleb_joshua':
        ink('26:65', '"and there was not left a man of them EXCEPT CALEB SON OF JEPHUNNEH AND JOSHUA SON OF NUN" — 14:30\'s last seven words verbatim (computed)')
        move('CALLED cold_run_shelach.decree(exceptions) -> %s [IMPORT, live]' % EXCEPTIONS, 'Bava Batra 118b:3 — "lived" = the spies\' portions')
        return out('Caleb and Joshua — 14:30\'s seven words', ['exempt'])
    if ask == 'decree_consumed':
        move('CALLED cold_run_shelach.decree(deaths_ceased) -> %s; DATA deaths_ceased = %s [IMPORT, live]' % (CEASED, CEASED_DAY), 'Bava Batra 121a:9, 121b:1 — the fifteenth of Av; the timer\'s fire at (40, 5, 9) before the census\'s (40, 6, 1)')
        return out('the dying ceased before the census — the timer fired, the day the shelf\'s', ['accepted'])
    if ask == 'levi_outside':
        ink('26:62 against 26:2', '"every male from a month old" against "from twenty years old and upward"')
        move('Bava Batra 121b:8 (Rav Hamnuna)', 'the decree\'s "twenty and upward" is the census\'s count — Levi outside')
        dat('the row decree_age_edges = %s' % data['decree_age_edges']['value'])
        return out('Levi outside the decree — its own threshold', ['exempt'])
    if ask == 'age_edges':
        move('Bava Batra 121b:11 (Rav Acha bar Yaakov); 121b:9-10', 'under twenty and over sixty outside — "and upward" with the valuations (Lev 27:7); Yair and Machir the survivors')
        dat('the row wilderness_survivors = %s' % data['wilderness_survivors']['value'])
        return out('under twenty and over sixty outside; Yair and Machir', ['exempt'])
    if ask == 'seven_spanned':
        ink('26:59', 'Amram on the roll')
        move('Bava Batra 121b:6', 'seven spanned the world — Amram saw Jacob, Ahijah saw Amram: the roll\'s Amram the chain\'s fourth link')
        return out('Amram the fourth link of the seven', ['accepted'])
    if ask == 'serah_jochebed_both_rolls':
        ink('26:46, 26:59', 'Serah; Jochebed')
        move('Seder Olam Rabbah 9:2; Sotah 13a:14', 'the two women on both rolls — the predicate\'s shelf exceptions beside the ink\'s two')
        return out('Serah and Jochebed on both rolls — the shelf\'s exceptions', ['accepted'])
    if ask == 'ark_roster_hypothesis':
        ink('26:64', '"not a man of those counted" — a membership predicate on a roll')
        hyp('the reading set 26:64 beside the ark\'s exit roster "all that came out of the ark" (Gen 9:10) — a shared PHRASE, no teacher on the shelf: a HYPOTHESIS (class H), the primeval runner NOT called (the link review law)')
        return out('the ark\'s roster at national scale — a hypothesis, not a compiled link', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ---- THE NAMED ROWS the roll writes (the persons the ink names beyond the family list; every status a clause of the ink) --------------
NAMED_ROLL = [
    ('eliab', 'Eliab', 'reuben', 'Pallu', 'Pallu', 'the sons of Pallu: Eliab', 'Num 26:8'),
    ('nemuel-son-of-eliab', 'Nemuel', 'reuben', 'Pallu', 'Eliab', 'the sons of Eliab: Nemuel and Dathan and Abiram', 'Num 26:9'),
    ('dathan', 'Dathan', 'reuben', 'Pallu', 'Eliab', 'strove against the LORD; the earth swallowed them with Korach', 'Num 26:9-10'),
    ('abiram', 'Abiram', 'reuben', 'Pallu', 'Eliab', 'strove against the LORD; the earth swallowed them with Korach', 'Num 26:9-10'),
    ('korach', 'Korach', 'levi', 'Korah', 'Izhar', 'swallowed with them; the fire consumed the two hundred and fifty — both deaths in one verse', 'Num 26:10'),
    ('the-sons-of-korach', 'the sons of Korach', 'levi', 'Korah', 'Korach', 'did not die', 'Num 26:11'),
    ('er', 'Er', 'judah', 'Shelah', 'Judah', 'died in the land of Canaan', 'Num 26:19'),
    ('onan', 'Onan', 'judah', 'Shelah', 'Judah', 'died in the land of Canaan', 'Num 26:19'),
    ('machir', 'Machir', 'manasseh', 'Machir', 'Manasseh', 'Machir begot Gilead', 'Num 26:29'),
    ('gilead', 'Gilead', 'manasseh', 'Gilead', 'Machir', 'the sons of Gilead — the six families', 'Num 26:29-32'),
    ('hepher', 'Hepher', 'manasseh', 'Hepher', 'Gilead', 'the father of Zelophehad', 'Num 26:32-33'),
    ('zelophehad', 'Zelophehad', 'manasseh', 'Hepher', 'Hepher', 'had no sons, only daughters', 'Num 26:33'),
    ('the-daughters-of-zelophehad', 'Mahlah', 'manasseh', 'Hepher', 'Zelophehad', 'had no sons, only daughters', 'Num 26:33'),
    ('the-daughters-of-zelophehad', 'Noah', 'manasseh', 'Hepher', 'Zelophehad', 'had no sons, only daughters', 'Num 26:33'),
    ('the-daughters-of-zelophehad', 'Hoglah', 'manasseh', 'Hepher', 'Zelophehad', 'had no sons, only daughters', 'Num 26:33'),
    ('the-daughters-of-zelophehad', 'Milcah', 'manasseh', 'Hepher', 'Zelophehad', 'had no sons, only daughters', 'Num 26:33'),
    ('the-daughters-of-zelophehad', 'Tirzah', 'manasseh', 'Hepher', 'Zelophehad', 'had no sons, only daughters', 'Num 26:33'),
    ('serah', 'Serah', 'asher', None, 'Asher', 'the name of the daughter of Asher was Serah', 'Num 26:46'),
]
NAMED_LEVI = [
    ('amram', 'Amram', 'levi', 'Kohath', 'Kohath', 'and Kohath begot Amram', 'Num 26:58'),
    ('jochebed', 'Jochebed', 'levi', 'Levi', 'Levi', 'born to Levi in Egypt', 'Num 26:59'),
    ('aaron', 'Aaron', 'levi', 'Kohath', 'Amram', 'she bore to Amram Aaron', 'Num 26:59'),
    ('moses', 'Moses', 'levi', 'Kohath', 'Amram', 'she bore to Amram Moses', 'Num 26:59'),
    ('miriam', 'Miriam', 'levi', 'Kohath', 'Amram', 'and Miriam their sister', 'Num 26:59'),
    ('nadab', 'Nadab', 'levi', 'Kohath', 'Aaron', 'died when they brought near strange fire', 'Num 26:60-61'),
    ('abihu', 'Abihu', 'levi', 'Kohath', 'Aaron', 'died when they brought near strange fire', 'Num 26:60-61'),
    ('eleazar', 'Eleazar', 'levi', 'Kohath', 'Aaron', 'to Aaron were born', 'Num 26:60'),
    ('ithamar', 'Ithamar', 'levi', 'Kohath', 'Aaron', 'to Aaron were born', 'Num 26:60'),
]
NAMED_ROLLS = [
    ('caleb', 'Caleb', 'judah', None, 'Jephunneh', 'excepted — not a man was left of them except Caleb son of Jephunneh', 'Num 26:65'),
    ('joshua', 'Joshua', 'ephraim', None, 'Nun', 'excepted — and Joshua son of Nun', 'Num 26:65'),
]
DEAD_STATUS = ('died', 'swallowed')
NAMED_TOTAL = len(NAMED_ROLL) + len(NAMED_LEVI) + len(NAMED_ROLLS)


def _named(world, rows, as_of, src):
    for subj, person, tribe, fam, father, status, verse in rows:
        world.row('population', {'grain': 'named', 'as_of': as_of, 'subject': subj, 'person': person, 'tribe': tribe, 'family': fam, 'father': father, 'status': status, 'source': src, 'note': verse})


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_second_census(event, world):
    """Num 25:19-26:65 (cold_run_second_census.py F1-F5) AND THE POPULATION TABLE's writer. installed_by boot — the census a command executed
    at its verse (law_census's form). The two SHARED kinds (census_taken, levites_counted) are consumed for their ROWS alone — no effect."""
    k, src = event['kind'], event['case_source']
    as_of = src.split(' — ')[0]
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'census_taken':                                   # Num 1:17-19 — SHARED with law_census: the twelve tribe rows of the first roll, no effect
        for t, n in event['counts'].items():
            world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': t, 'tribe': t, 'family': None, 'count': n, 'threshold': 'twenty years old and upward', 'source': src})
        return []
    if k == 'levites_counted':                                # Num 3:16 — SHARED: the three houses and the Levites' total as written, no effect
        for h, n in event['houses'].items():
            world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': 'the-levites', 'tribe': 'levi', 'family': h, 'level': 'house', 'count': n, 'threshold': 'a month old and upward', 'source': src})
        world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': 'the-levites', 'tribe': 'levi', 'family': None, 'count': event['total_as_written'], 'threshold': 'a month old and upward', 'source': src})
        return []
    if k == 'second_census_commanded':
        return [E_('commanded', event['subject'], value='the_second_census', law='F1 [INK 25:19-26:4 "lift the head... from twenty years old and upward" — 1:2-3 shortened by five; to Moses AND Eleazar: the count owed]')]
    if k == 'second_census_taken':
        world.close(event['subject'], 'commanded', 'Num 26:51 — these are the counted of the children of Israel: six hundred thousand and a thousand seven hundred and thirty', value='the_second_census')
        prior = {r['tribe']: r for r in world.population(grain='counted', family=None) if r['tribe'] in TRIBES}
        for t, n in event['counts'].items():
            world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': t, 'tribe': t, 'family': None, 'count': n, 'threshold': 'twenty years old and upward', 'source': src})
        for t, fams in event['families'].items():
            for name, gent in fams:
                world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': t, 'tribe': t, 'family': name, 'gentilic': gent, 'level': 'family', 'count': None, 'source': src})
        for t, n in event['counts'].items():
            if t in prior:
                d = n - prior[t]['count']
                explained = [{'source': 'Num 25:9', 'count': PLAGUE, 'tribe_by': 'the shelf — the row plague_tribe (%s)' % DATA['plague_tribe']['value']}] if t == 'simeon' else []
                world.row('population', {'grain': 'delta', 'as_of': as_of, 'subject': t, 'tribe': t, 'from_verse': prior[t]['as_of'], 'to_verse': as_of, 'delta': d, 'explained': explained, 'unexplained': d + sum(x['count'] for x in explained), 'source': src})
        _named(world, NAMED_ROLL, as_of, src)
        return [E_('counted', event['subject'], value=event.get('total', TOTAL26), law='F2 [INK 26:51 — the twelve summed = %d; the deltas declared against 1:20-43 (%d); the table\'s rows]' % (TOTAL26, TOTAL1))]
    if k == 'land_division_commanded':
        return [E_('commanded', event['subject'], value='divide_the_land', law='F3 [INK 26:52-56 — the size by the number of names, the place by lot, the lot\'s mouth: the division owed; OPEN — Joshua 14-19 the run]')]
    if k == 'levites_counted_second':
        prior = [r for r in world.population(grain='counted', tribe='levi', family=None)]
        world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': 'the-levites', 'tribe': 'levi', 'family': None, 'count': event['total'], 'threshold': 'a month old and upward', 'source': src})
        for h in event['houses']:
            world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': 'the-levites', 'tribe': 'levi', 'family': h, 'level': 'house', 'count': None, 'source': src})
        for f in event['families']:
            world.row('population', {'grain': 'counted', 'as_of': as_of, 'subject': 'the-levites', 'tribe': 'levi', 'family': f, 'level': 'family', 'count': None, 'source': src})
        if prior:
            d = event['total'] - prior[-1]['count']
            world.row('population', {'grain': 'delta', 'as_of': as_of, 'subject': 'the-levites', 'tribe': 'levi', 'from_verse': prior[-1]['as_of'], 'to_verse': as_of, 'delta': d, 'explained': [], 'unexplained': d, 'source': src})
        _named(world, NAMED_LEVI, as_of, src)
        barred = [e for e in world.entity('the-levites').ledger if e['effect'] == 'inheritance_barred']
        return [E_('counted', event['subject'], value=event['total'], law='F4 [INK 26:62 — %d from a month old; "for no inheritance was given them": the block on this ledger %s]' % (event['total'], ('READ — %s' % barred[0].get('case_source', '')[:40]) if barred else 'NOT FOUND on this world'))]
    if k == 'rolls_compared':
        _named(world, NAMED_ROLLS, as_of, src)
        return []                                  # the predicate the checkpoint's (26:63-65); nothing written
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'census_command_case':
        v, e, _ = the_command({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'counted': E_('counted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'census_roll_case':
        v, e, _ = the_roll({'ask': event['ask']}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'counted': E_('counted', s_, value=v, law=L), 'holding_owed': E_('holding_owed', s_, cp='the-court', value=v, law=L), 'souls_counted': E_('souls_counted', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'land_division_case':
        v, e, _ = the_land({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'holding_owed': E_('holding_owed', s_, cp='the-court', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'levite_roll_case':
        v, e, _ = the_levites({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'counted': E_('counted', s_, value=v, law=L), 'inheritance_barred': E_('inheritance_barred', s_, cp='HEAVEN', value=v, law=L), 'souls_counted': E_('souls_counted', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'two_rolls_case':
        v, e, _ = the_rolls({'ask': event['ask']}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


FAMS_EVENT = {t: [(FAMILIES[t][i], GENT[t][i][1]) for i in range(len(FAMILIES[t]))] for t in TRIBES}
CS_1 = 'Num 1:17-19 — and Moses and Aaron took these men... and they declared their pedigrees... as the LORD commanded Moses, and he counted them in the wilderness of Sinai; 1:46 six hundred thousand and three thousand and five hundred and fifty'
CS_3 = 'Num 3:16 — and Moses counted them by the mouth of the LORD, as he was commanded; 3:39 all the counted of the Levites... twenty-two thousand'
LINES = [
    ('second_census_commanded', 'israel', {'addressees': ['moses', 'eleazar'], 'threshold': 20, 'after': 'the plague'}, 'Num 25:19-26:4 — and it was after the plague; and the LORD said to Moses and to Eleazar son of Aaron the priest, saying: lift the head of all the congregation of the children of Israel from twenty years old and upward by their fathers\' houses, everyone going out to the host in Israel; and Moses and Eleazar the priest spoke [them] in the plains of Moab by the Jordan of Jericho, saying: from twenty years old and upward, as the LORD commanded Moses and the children of Israel who came out of the land of Egypt'),
    ('second_census_taken', 'israel', {'counts': dict(C26), 'total': TOTAL26, 'families': FAMS_EVENT, 'named': [p for _, p, *_ in NAMED_ROLL]}, 'Num 26:5-51 — Reuben the firstborn of Israel: the sons of Reuben — of Hanoch, the family of the Hanochite... these are the families of the Reubenites, and their counted were forty and three thousand and seven hundred and thirty... these are the counted of the children of Israel: six hundred thousand and a thousand seven hundred and thirty'),
    ('land_division_commanded', 'israel', {'by_names': True, 'by_lot': True, 'lots_mouth': True}, 'Num 26:52-56 — and the LORD spoke to Moses, saying: to these the land shall be divided for an inheritance by the number of names; to the many you shall increase their inheritance and to the few you shall diminish their inheritance, to each according to his counted shall his inheritance be given; only by lot shall the land be divided, by the names of the tribes of their fathers they shall inherit; by the mouth of the lot shall its inheritance be divided between the many and the few'),
    ('levites_counted_second', 'the-levites', {'families': list(LEV_FAM26), 'houses': list(LEV_HOUSES), 'total': LEV26, 'threshold': 'a month', 'named': [p for _, p, *_ in NAMED_LEVI]}, 'Num 26:57-62 — and these are the counted of the Levites by their families: of Gershon the family of the Gershonite, of Kohath the family of the Kohathite, of Merari the family of the Merarite; these are the families of Levi: the Libnite, the Hebronite, the Mahlite, the Mushite, the Korahite; and Kohath begot Amram; and the name of Amram\'s wife was Jochebed the daughter of Levi, whom she bore to Levi in Egypt; and she bore to Amram Aaron and Moses and Miriam their sister; and to Aaron were born Nadab and Abihu, Eleazar and Ithamar; and Nadab and Abihu died when they brought near strange fire before the LORD; and their counted were twenty-three thousand, every male from a month old and upward, for they were not counted among the children of Israel, for no inheritance was given them among the children of Israel'),
    ('rolls_compared', 'israel', {'priest': 'eleazar', 'place': 'the plains of Moab', 'exceptions': ['caleb', 'joshua']}, 'Num 26:63-65 — these are the counted by Moses and Eleazar the priest, who counted the children of Israel in the plains of Moab by the Jordan of Jericho; and among these there was not a man of those counted by Moses and Aaron the priest, who counted the children of Israel in the wilderness of Sinai; for the LORD had said of them: they shall surely die in the wilderness; and there was not left a man of them except Caleb son of Jephunneh and Joshua son of Nun'),
]


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the five case kinds on the exam's persons."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 25:19-26:65: Bava Batra 117a-123a, 143b, Sotah 12a-13a, Sanhedrin 110a, Yoma 73b, Seder Olam 9 and Mishnah Bava Batra 8:1-2, 7:1-4 on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_second_census]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # LITERAL submits (the daemon gate parses no loop — 5b's and 7b's lesson): eighteen of the exam's persons through the five case kinds
        w.submit({'kind': 'census_command_case', 'subject': 'the-son-for-the-father', 'person': 'the-son-for-the-father', 'ask': 'addressees', 'case_source': 'Num 26:1 — the exam\'s row addressees (the Chukat runner\'s succession)'})
        w.submit({'kind': 'census_command_case', 'subject': 'the-count-owed', 'person': 'the-count-owed', 'ask': 'lift_the_head', 'case_source': 'Num 26:2 — the exam\'s row lift_the_head (1:2-3 shortened by five)'})
        w.submit({'kind': 'census_command_case', 'subject': 'the-after-the-plague', 'person': 'the-after-the-plague', 'ask': 'after_the_plague', 'case_source': 'Num 25:19 — the exam\'s row after_the_plague (Seder Olam 9:2)'})
        w.submit({'kind': 'census_roll_case', 'subject': 'the-twelve', 'person': 'the-twelve', 'ask': 'twelve_counts', 'case_source': 'Num 26:7-50 — the exam\'s row twelve_counts'})
        w.submit({'kind': 'census_roll_case', 'subject': 'the-simeonite', 'person': 'the-simeonite', 'ask': 'simeons_gap', 'case_source': 'Num 26:14 — the exam\'s row simeons_gap (25:9 by CALL)'})
        w.submit({'kind': 'census_roll_case', 'subject': 'the-daughters-on-the-roll', 'person': 'the-daughters-on-the-roll', 'ask': 'daughters_row', 'case_source': 'Num 26:33 — the exam\'s row daughters_row (Mishnah Bava Batra 8:2)'})
        w.submit({'kind': 'census_roll_case', 'subject': 'the-serah', 'person': 'the-serah', 'ask': 'serah', 'case_source': 'Num 26:46 — the exam\'s row serah (Sotah 13a:14)'})
        w.submit({'kind': 'land_division_case', 'subject': 'the-many', 'person': 'the-many', 'ask': 'by_number_of_names', 'case_source': 'Num 26:53-54 — the exam\'s row by_number_of_names'})
        w.submit({'kind': 'land_division_case', 'subject': 'the-lot', 'person': 'the-lot', 'ask': 'by_lot', 'case_source': 'Num 26:55 — the exam\'s row by_lot (Sanhedrin 43b:6)'})
        w.submit({'kind': 'land_division_case', 'subject': 'the-excepted-two', 'person': 'the-excepted-two', 'ask': 'only_excludes', 'case_source': 'Num 26:55 — the exam\'s row only_excludes (Bava Batra 122a:12, 122b:2)'})
        w.submit({'kind': 'land_division_case', 'subject': 'the-ten-parts', 'person': 'the-ten-parts', 'ask': 'ten_parts', 'case_source': 'Num 26:29-33 — the exam\'s row ten_parts (Bava Batra 118b:8; Josh 17:5)'})
        w.submit({'kind': 'land_division_case', 'subject': 'the-children', 'person': 'the-children', 'ask': 'children_excluded', 'case_source': 'Num 26:53 — the exam\'s row children_excluded (Bava Batra 117a:2)'})
        w.submit({'kind': 'levite_roll_case', 'subject': 'the-levite-roll', 'person': 'the-levite-roll', 'ask': 'count', 'case_source': 'Num 26:62 — the exam\'s row count (23,000 for 22,000)'})
        w.submit({'kind': 'levite_roll_case', 'subject': 'the-levite-without-inheritance', 'person': 'the-levite-without-inheritance', 'ask': 'no_inheritance', 'case_source': 'Num 26:62 — the exam\'s row no_inheritance (18:23-24 read)'})
        w.submit({'kind': 'levite_roll_case', 'subject': 'the-jochebed', 'person': 'the-jochebed', 'ask': 'jochebed', 'case_source': 'Num 26:59 — the exam\'s row jochebed (Bava Batra 123b:1)'})
        w.submit({'kind': 'two_rolls_case', 'subject': 'the-first-roll', 'person': 'the-first-roll', 'ask': 'membership_predicate', 'case_source': 'Num 26:64 — the exam\'s row membership_predicate (14:29-35 by CALL)'})
        w.submit({'kind': 'two_rolls_case', 'subject': 'the-caleb-and-joshua', 'person': 'the-caleb-and-joshua', 'ask': 'except_caleb_joshua', 'case_source': 'Num 26:65 — the exam\'s row except_caleb_joshua (14:30 verbatim)'})
        w.submit({'kind': 'two_rolls_case', 'subject': 'the-levite-under-the-decree', 'person': 'the-levite-under-the-decree', 'ask': 'levi_outside', 'case_source': 'Num 26:62 — the exam\'s row levi_outside (Bava Batra 121b:8)'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    return (n('the-son-for-the-father', 'accepted'), n('the-count-owed', 'commanded'), n('the-after-the-plague', 'accepted'),
            n('the-twelve', 'counted'), n('the-simeonite', 'counted'), n('the-daughters-on-the-roll', 'holding_owed'), n('the-serah', 'souls_counted'),
            n('the-many', 'commanded'), n('the-lot', 'commanded'), n('the-excepted-two', 'exempt'), n('the-ten-parts', 'holding_owed'), n('the-children', 'exempt'),
            n('the-levite-roll', 'counted'), n('the-levite-without-inheritance', 'inheritance_barred'), n('the-jochebed', 'souls_counted'),
            n('the-first-roll', 'accepted'), n('the-caleb-and-joshua', 'exempt'), n('the-levite-under-the-decree', 'exempt'), len(w.entities), len(w.tables['population'])), w
SCENE, _W = scene()


def narrative():
    """THE NUMBERS WALK 8b (2026-09-11): the portion's own acts AS HISTORY — the first roll's two SHARED events replayed first (at (2, 2, 1), the
    table's chapter-1 rows), then the marker at 25:19 (reading-placed at (40, 6, 1)) and the five lines of 25:19-26:65 in the text's order on a
    world with this runner's daemon. Recorded by the sequential run's recorder and stitched onto the tape (the two shared events DEDUPED against
    Bamidbar's at their verses; the marker the stitcher's row). Not a graded cell: the tuple below is a tripwire typed from the first run's
    print; the sequence world's RUN tuple and CP1-CP9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 25:19-26:65: the second census on the tape — the command, the roll, the land, the Levites, the two rolls; THE POPULATION TABLE (the exodus epoch)', epoch='exodus')
        w.laws = [law_second_census]
        w.advance(w.clock.day_in('exodus', 2, 2, 1))
        w.submit({'kind': 'census_taken', 'subject': 'israel', 'counts': dict(C1), 'total': TOTAL1, 'by_names': True, 'date_repeated': True, 'case_source': CS_1})
        w.submit({'kind': 'levites_counted', 'subject': 'the-levites', 'houses': dict(HOUSES), 'total_as_written': LEV1, 'houses_sum': sum(HOUSES.values()), 'aaron_dotted': BM.AARON_DOTTED, 'case_source': CS_3})
        w.marker('Num 25:19', w.clock.day_in('exodus', 40, 6, 1), value='and it was after the plague (25:19) — READING-PLACED at the counter\'s own day (40, 6, 1): no day in the ink or on the shelf; the ORDER Seder Olam Rabbah 9:2\'s (Arvot Moab, the plague, the census, the daughters)', placement='reading_placed')
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY (7b's lesson, relearned at this sitting's first gate run: a loop over LINES read as '?UNRESOLVED?') — the five lines typed out
        w.submit({'kind': 'second_census_commanded', 'subject': 'israel', 'addressees': ['moses', 'eleazar'], 'threshold': 20, 'after': 'the plague', 'case_source': LINES[0][3]})
        w.submit({'kind': 'second_census_taken', 'subject': 'israel', 'counts': dict(C26), 'total': TOTAL26, 'families': FAMS_EVENT, 'named': [p for _, p, *_ in NAMED_ROLL], 'case_source': LINES[1][3]})
        w.submit({'kind': 'land_division_commanded', 'subject': 'israel', 'by_names': True, 'by_lot': True, 'lots_mouth': True, 'case_source': LINES[2][3]})
        w.submit({'kind': 'levites_counted_second', 'subject': 'the-levites', 'families': list(LEV_FAM26), 'houses': list(LEV_HOUSES), 'total': LEV26, 'threshold': 'a month', 'named': [p for _, p, *_ in NAMED_LEVI], 'case_source': LINES[3][3]})
        w.submit({'kind': 'rolls_compared', 'subject': 'israel', 'priest': 'eleazar', 'place': 'the plains of Moab', 'exceptions': ['caleb', 'joshua'], 'case_source': LINES[4][3]})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    val = lambda eid, eff: [e.get('value') for e in w.entity(eid).ledger if e['effect'] == eff]
    T = w.tables['population']
    by = collections.Counter((r['grain'], r['as_of']) for r in T)
    marker = [l for l in w.log if l[0] == 'MARKER']
    dsim = [r for r in T if r['grain'] == 'delta' and r['tribe'] == 'simeon']
    return (n('israel', 'commanded'), is_open('israel', 'commanded'), val('israel', 'counted'), val('the-levites', 'counted'),
            by[('counted', 'Num 1:17-19')], by[('counted', 'Num 3:16')], by[('counted', 'Num 26:5-51')], by[('counted', 'Num 26:57-62')], by[('delta', 'Num 26:5-51')], by[('delta', 'Num 26:57-62')],
            by[('named', 'Num 26:5-51')], by[('named', 'Num 26:57-62')], by[('named', 'Num 26:63-65')], len(T),
            dsim[0]['delta'] if dsim else None, dsim[0]['unexplained'] if dsim else None, sum(1 for l in w.log if l[0] == 'ROW'),
            len(marker), marker[0][2].get('placement') if marker else None, w.clock.eras['exodus'].date(w.clock.day)[1:], len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, [False, True], [601730], [23000],
                       12, 4, 69, 9, 12, 1,
                       18, 9, 2, 136,
                       -37100, -13100, 136,
                       1, 'reading_placed', (6, 1), 2)   # NUMBERS_WALK.md "Sitting 8b": the two debits (the census closed, the land OPEN); the two counted values; the rows by grain and census — 12 + 4 (three houses + the total) at the first roll, 12 + 57 = 69 tribes and families at the second, 1 + 3 + 5 = 9 for the Levites, 12 + 1 deltas, 18 + 9 + 2 = 29 named (Eliab and Nemuel son of Eliab beside the design's twenty-seven — persons the roll names beside the family list); 136 rows = 136 ROW lines; Simeon's delta and its unexplained; one marker reading-placed; the date (6, 1) of the fortieth year; two entities (israel, the-levites)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the second census\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the command
    ('Num 26:1 — to Moses AND to Eleazar: the son for the father (the Chukat runner\'s succession called)', lambda: the_command({'ask': 'addressees'}, DATA), 'to Moses and to Eleazar — the son for the father since 20:28'),
    ('Num 26:2 — lift the head: 1:2-3 shortened by five (M-23 exemplar 16)', lambda: the_command({'ask': 'lift_the_head'}, DATA), 'twenty and upward, the host — 1:2-3 shortened by five'),
    ('Num 26:3 — spoke [them]: the verb supplied', lambda: the_command({'ask': 'spoke_them'}, DATA), 'the verb supplied by the translation: to count them'),
    ('Num 25:19 / Seder Olam 9:2 — after the plague: the marker reading-placed', lambda: the_command({'ask': 'after_the_plague'}, DATA), 'after the plague — the order the shelf\'s, the day the counter\'s: reading-placed'),
    ('Num 26:4 — the exodus generation named', lambda: the_command({'ask': 'exodus_generation'}, DATA), 'the exodus generation named at the second roll\'s head'),
    # F2 — the roll
    ('Num 26:7-50 / 1:20-43 — the twelve at both seats', lambda: the_roll({'ask': 'twelve_counts'}, DATA), 'twelve at both seats, the parser\'s'),
    ('Num 26:51 — 601,730 = the twelve summed; 1:46 by CALL', lambda: the_roll({'ask': 'total'}, DATA), '601730 = the twelve summed; 603,550 at the first roll'),
    ('Num 26 against 1 — the deltas declared', lambda: the_roll({'ask': 'deltas'}, DATA), 'five fell, seven rose, the whole -1820 — declared, not derived'),
    ('Num 26:14 / 25:9 — Simeon\'s gap: the plague by CALL, 13,100 unexplained', lambda: the_roll({'ask': 'simeons_gap'}, DATA), '-37100 against the plague\'s 24000: 13100 unexplained'),
    ('Num 26:10 / 17:14 — Korach\'s dead carry no tribe (the Korach runner called)', lambda: the_roll({'ask': 'korachs_dead'}, DATA), '14700 and 250 carry no tribe — no delta row explained by them'),
    ('Num 26:5-50 — fifty-seven families; "family of" 78 against 0 (Bava Batra 109b by CALL)', lambda: the_roll({'ask': 'families'}, DATA), '57 families in twelve tribes; the family of 78 against 0'),
    ('Gen 46 against Num 26 — five absent, nine renamed, two moved', lambda: the_roll({'ask': 'genesis_46'}, DATA), '5 absent, 9 renamed, 2 moved — the table keyed to Genesis 46'),
    ('Num 26:19 = Gen 46:12 — Er and Onan', lambda: the_roll({'ask': 'er_and_onan'}, DATA), 'died in the land of Canaan — 46:12 verbatim'),
    ('Sanhedrin 110a:13-14 — Korach recalled: both deaths on one verse', lambda: the_roll({'ask': 'korach_recalled'}, DATA), 'both deaths on one verse; the mode the Korach runner\'s open row'),
    ('Sanhedrin 110a:17 — the sons of Korach did not die', lambda: the_roll({'ask': 'sons_of_korach'}, DATA), 'the sons of Korach did not die'),
    ('Bava Batra 143b:6-7 — sons for one son; a grandson not a son', lambda: the_roll({'ask': 'single_son_plural'}, DATA), 'sons for one son (26:8); a grandson not a son — the roll\'s Ard and Naaman'),
    ('Megillah 11a:17 — this is Dathan and Abiram', lambda: the_roll({'ask': 'hu_dathan'}, DATA), 'this is Dathan and Abiram — the same from beginning to end'),
    ('Num 26:33 / Mishnah Bava Batra 8:2 — the daughters\' row (the Zelophehad runner called)', lambda: the_roll({'ask': 'daughters_row'}, DATA), 'no sons, only daughters — the premise on the roll; the heir the daughter'),
    ('Num 26:46 / Sotah 13a:14 — Serah on three rosters', lambda: the_roll({'ask': 'serah'}, DATA), 'Serah on three rosters — the shelf\'s survivor of both rolls'),
    ('Num 26:5 / Bava Batra 123a:4-5 — Reuben the firstborn kept', lambda: the_roll({'ask': 'reuben_firstborn'}, DATA), 'the firstborn kept on the roll; the birthright Joseph\'s by Chronicles'),
    ('Num 26:28 / Bava Batra 123a:10 — Joseph\'s two as tribes, Manasseh first', lambda: the_roll({'ask': 'ephraim_manasseh_order'}, DATA), 'Joseph\'s two as tribes — Manasseh first at the second roll'),
    # F3 — the land
    ('Num 26:53-54 — the size by the number of names', lambda: the_land({'ask': 'by_number_of_names'}, DATA), 'the size by the count of names — to the many increase, to the few diminish'),
    ('Num 26:55 / Sanhedrin 43b:6 — the place by lot', lambda: the_land({'ask': 'by_lot'}, DATA), 'the place by lot — Joshua 14-19 the run'),
    ('Num 26:56 / Bava Batra 122a:3-6 — the lot\'s mouth is the Urim', lambda: the_land({'ask': 'lots_mouth'}, DATA), 'the lot\'s mouth is the oracle\'s — two receptacles before Eleazar'),
    ('Bava Batra 117a:2-117b:1 / Sifrei 132:1 — to these: the row READ by CALL', lambda: the_land({'ask': 'land_divided_among'}, DATA), 'left_egypt (the running setting) — entered and both recorded; the dead inherit the living'),
    ('Bava Batra 122a:12, 122b:2 / Sifrei 132:3 — only excludes the two', lambda: the_land({'ask': 'only_excludes'}, DATA), 'Joshua and Caleb excluded from the lot — 26:65\'s two'),
    ('Bava Batra 121b:12-122a:8 — by tribes, then by numbers within', lambda: the_land({'ask': 'tribes_or_skulls'}, DATA), 'by tribes, then by numbers within — the table\'s two levels'),
    ('Bava Batra 122a:10-11 — the compensation (money; land recorded)', lambda: the_land({'ask': 'compensation'}, DATA), 'compensated — money (R. Eliezer; land recorded)'),
    ('Bava Batra 117b:2, 118b:3-7 — the spies\' and the protesters\' portions', lambda: the_land({'ask': 'spies_portions'}, DATA), 'the spies\' portions to Joshua and Caleb; the protesters\' by the row'),
    ('Bava Batra 117a:2, 119a:3 — the children excluded', lambda: the_land({'ask': 'children_excluded'}, DATA), 'the children excluded — like these, above twenty'),
    ('Sifrei 132:4 / Mishnah Bava Batra 7:1-4 — the estimate by worth', lambda: the_land({'ask': 'the_estimate'}, DATA), 'the estimate by worth — a kor\'s-space against a seah\'s-space'),
    ('Bava Batra 118a:4-7 / Josh 17:14 — Joseph\'s protest on the roll\'s rise', lambda: the_land({'ask': 'joseph_protest'}, DATA), 'Joseph\'s protest grounded on the roll\'s rise'),
    ('Bava Batra 118b:8-10 / Josh 17:5 — ten parts (the Zelophehad runner called)', lambda: the_land({'ask': 'ten_parts'}, DATA), 'ten parts — six houses and the daughters\' four'),
    ('Bava Batra 119a:1, 119a:5 — the land in possession before assignment', lambda: the_land({'ask': 'possession_before_assignment'}, DATA), 'in possession before assignment — the rows are holdings before the lot'),
    ('Bava Batra 119b:3-4 / Exod 6:8 — morasha both ways', lambda: the_land({'ask': 'morasha'}, DATA), 'morasha both ways — they bequeath and do not inherit'),
    ('Bava Batra 122a:2, 122a:9 — twelve now, thirteen to come', lambda: the_land({'ask': 'thirteen_tribes'}, DATA), 'twelve now, thirteen to come'),
    # F4 — the Levites
    ('Num 26:57-58 against 3:17-20 — five for eight', lambda: the_levites({'ask': 'five_for_eight'}, DATA), 'five for eight: Shimei, Amram, Izhar, Uzziel gone; Korah in'),
    ('Num 26:62 against 3:39 — 23,000 for 22,000 (Bekhorot 5a by CALL)', lambda: the_levites({'ask': 'count'}, DATA), '23000 for 22000: +1000 unexplained'),
    ('Num 26:62 / 18:23-24 — no inheritance: the block READ', lambda: the_levites({'ask': 'no_inheritance'}, DATA), 'not counted among — no inheritance: the 18:23-24 block read'),
    ('Num 26:59 / Bava Batra 123b:1 — Jochebed in Egypt: CJ3b\'s witness (the Joseph runner called)', lambda: the_levites({'ask': 'jochebed'}, DATA), 'born to Levi in Egypt — CJ3b\'s ink witness; the verdict stays DIVERGE'),
    ('Bava Batra 120a:2 / Sotah 12a:15 — 130 at Moses\' birth', lambda: the_levites({'ask': 'jochebed_age'}, DATA), '130 at Moses\' birth — a daughter by her youth reborn'),
    ('Sotah 12a:9-13 — Amram\'s remarriage', lambda: the_levites({'ask': 'amram_remarriage'}, DATA), 'the remarriage the shelf\'s — the ink names the wife'),
    ('Num 26:59 / Sotah 12a:2-7 — Miriam on the roll', lambda: the_levites({'ask': 'miriam'}, DATA), 'Miriam on the roll — her sister-clause'),
    ('Num 26:61 / Lev 10:1 — Nadab and Abihu (the eighth-day runner called)', lambda: the_levites({'ask': 'nadab_abihu'}, DATA), 'died at the strange fire — Lev 10:1 recalled; no entity on the tape'),
    ('Num 26:58 — Kohath begot: the defective spelling', lambda: the_levites({'ask': 'kohath_begot'}, DATA), 'Kohath begot Amram — the defective spelling'),
    # F5 — the two rolls
    ('Num 26:63-64 — one sentence twice', lambda: the_rolls({'ask': 'one_sentence_twice'}, DATA), 'one sentence twice — the priest and the place'),
    ('Num 26:64 / 14:29-35 — the membership predicate (the Shelach runner called)', lambda: the_rolls({'ask': 'membership_predicate'}, DATA), 'not a man of the first roll on the second — the decree consumed'),
    ('Num 26:65 = 14:30 — Caleb and Joshua', lambda: the_rolls({'ask': 'except_caleb_joshua'}, DATA), 'Caleb and Joshua — 14:30\'s seven words'),
    ('Bava Batra 121a:9-121b:1 — the dying ceased before the census', lambda: the_rolls({'ask': 'decree_consumed'}, DATA), 'the dying ceased before the census — the timer fired, the day the shelf\'s'),
    ('Bava Batra 121b:8 — Levi outside the decree', lambda: the_rolls({'ask': 'levi_outside'}, DATA), 'Levi outside the decree — its own threshold'),
    ('Bava Batra 121b:9-11 — the age edges; Yair and Machir', lambda: the_rolls({'ask': 'age_edges'}, DATA), 'under twenty and over sixty outside; Yair and Machir'),
    ('Bava Batra 121b:6 — the seven who spanned', lambda: the_rolls({'ask': 'seven_spanned'}, DATA), 'Amram the fourth link of the seven'),
    ('Seder Olam 9:2 / Sotah 13a:14 — Serah and Jochebed on both rolls', lambda: the_rolls({'ask': 'serah_jochebed_both_rolls'}, DATA), 'Serah and Jochebed on both rolls — the shelf\'s exceptions'),
    ('Gen 9:10 beside 26:64 — the ark\'s roster: a HYPOTHESIS (class H), no teacher', lambda: the_rolls({'ask': 'ark_roster_hypothesis'}, DATA), 'the ark\'s roster at national scale — a hypothesis, not a compiled link'),
    # THE NUMBERS from the ink (the parser at both seats, the table's arithmetic)
    ('THE PARSER at 26:51 and 1:46 — the two totals', lambda: ((TOTAL26, TOTAL1), [FX.NONE], [('INK', 'Num 26:51, 1:46 — the parser')]), (601730, 603550)),
    ('THE DELTAS — five fell, seven rose, the whole', lambda: ((len(FELL), sum(DELTA[t] for t in FELL), len(ROSE), sum(DELTA[t] for t in ROSE), TOTAL26 - TOTAL1), [FX.NONE], [('INK', 'Num 26 against 1 — the parser at both seats')]), (5, -61020, 7, 59200, -1820)),
    ('THE FAMILIES — fifty-seven in twelve tribes, "family of" 78 against 0; Levi five for eight', lambda: ((NFAM, FAM_OF, FAM_OF_1, len(LEV_FAM26), len(LEV_FAM3)), [FX.NONE], [('INK', 'Num 26:5-58, 3:17-20 — the gentilic pattern computed')]), (57, 78, 0, 5, 8)),
    ('GENESIS 46 against 26 — the tokens: 5 absent, 9 renamed, 2 moved', lambda: ((len(ABSENT), len(RENAMED), len(MOVED), BECHER_EPHRAIM), [FX.NONE], [('INK', 'Gen 46:8-25 against Num 26:5-50 — computed')]), (5, 9, 2, True)),
    ('THE LEVITES — 23,000 against 22,000; the houses 22,300', lambda: ((LEV26, LEV1, sum(HOUSES.values())), [FX.NONE], [('INK', 'Num 26:62, 3:39, 3:22-34')]), (23000, 22000, 22300)),
    ('SIMEON — the plague 24,000 against the fall 37,100 (the Balak runner called)', lambda: ((PLAGUE, -DELTA['simeon'], -DELTA['simeon'] - PLAGUE), [FX.NONE], [('MOVE', 'CALLED cold_run_balak.COUNT')]), (24000, 37100, 13100)),
    ('KORACH — 14,700 and 250 by CALL; no tribe', lambda: ((K_PLAGUE, K250), [FX.NONE], [('MOVE', 'CALLED cold_run_korach')]), (14700, 250)),
    ('THE THRESHOLD — twenty at 26:2 and 26:4', lambda: (TWENTY, [FX.NONE], [('INK', 'Num 26:2, 26:4')]), ([20], [20])),
    ('"MOSES AND ELEAZAR" adjacent — ten seats in Numbers, the first 20:28, the second 26:1', lambda: ((len(ME_SEATS), ME_SEATS[0], ME_SEATS[1]), [FX.NONE], [('INK', 'Numbers — computed on the DB')]), (10, (20, 28), (26, 1))),
    ('14:30\'s last seven words at 26:65 — verbatim', lambda: (FOURTEEN_30 == words(26, 65)[-7:], [FX.NONE], [('INK', 'Num 14:30, 26:65')]), True),
    ('THE JOSEPH RUNNER\'s seventy — the sub-totals and the living named (CJ3b)', lambda: ((SEVENS, LIVING), [FX.NONE], [('MOVE', 'CALLED cold_run_joseph.seventy')]), ((33, 16, 14, 7), 32)),
    ('THE ZELOPHEHAD RUNNER\'s land row — the running setting and the three arms', lambda: ((LAND_ROW['value'], sorted(LAND_ROW['settings'])), [FX.NONE], [('MOVE', 'CALLED cold_run_zelophehad.DATA')]), ('left_egypt', ['both', 'entered', 'left_egypt'])),
    ('THE SHELACH RUNNER\'s decree — the set and the dying ceased', lambda: ((DECREE_SET.split(' ')[0], CEASED_DAY), [FX.NONE], [('MOVE', 'CALLED cold_run_shelach.decree')]), ('603550', (40, 5, 15))),
    ('THE NAMED ROWS — 18 + 9 + 2', lambda: ((len(NAMED_ROLL), len(NAMED_LEVI), len(NAMED_ROLLS), NAMED_TOTAL), [FX.NONE], [('INK', 'Num 26:8-11, 19, 29-33, 46, 58-61, 65')]), (18, 9, 2, 29)),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — the wrap: eighteen of the exam\'s persons through the five case kinds; no table row on the bench (no census event submitted there)',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 25:19-26:65 — the recorded rows replayed')]),
     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 18, 0)),
    ('THE NARRATIVE on the world engine — the two shared events, the marker and the five lines; THE POPULATION TABLE\'s 136 rows (the tripwire typed from the first run)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 25:19-26:65 — the five lines; Num 1:17-19, 3:16 the shared events')]),
     (2, [False, True], [601730], [23000], 12, 4, 69, 9, 12, 1, 18, 9, 2, 136, -37100, -13100, 136, 1, 'reading_placed', (6, 1), 2)),
]

if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0, 'HYP': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'HYP' if 'HYP' in kinds else ('INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE NUMBERS from the ink: the twelve at 26 %s; total %d (26:51) against %d (1:46); the deltas %s; the Levites %d against %d (the houses %d); the plague %d; Korach\'s %d and %d' %
          (C26, TOTAL26, TOTAL1, DELTA, LEV26, LEV1, sum(HOUSES.values()), PLAGUE, K_PLAGUE, K250))
    print('THE POPULATION TABLE on the narrative world: %d rows — %s' % (len(_WN.tables['population']), dict(collections.Counter(r['grain'] for r in _WN.tables['population']))))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA; land_divided_among the Zelophehad runner\'s, read by call)')
    if ok == len(CASES):
        print('\nTHE SECOND CENSUS COMPILES — the two rolls as tables with their deltas declared, the land\'s two functions, the Levites five for eight, the membership predicate on the table, the daughters\' and Jochebed\'s rows the table\'s first consumers.')
