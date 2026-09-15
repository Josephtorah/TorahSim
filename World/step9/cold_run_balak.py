import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 22:1-25:19 — BALAK: THE CALL, THE SHE-ASS AND THE ANGEL, THE THREE STANDS AND THE FOUR PARABLES, PEOR, PHINEHAS AND THE MIDIAN
# COMMAND (THE NUMBERS WALK sitting 7b, 2026-09-11; World/step9/NUMBERS_WALK.md "Sitting 7b"). The seventh Numbers portion compiled after its
# walk, on the owner's ruling READ THEN COMPILE: the parser taught THE PLENE "THREE" (22:32's vav-spelled numeral; Deut 16:16, 19:2) and THE
# CONSTRUCT "THOUSANDS OF" after a unit (Exod 32:28's "about three thousands of men" = 3,000, read 3 since the parser's first day) at this
# sitting (census_probes.py 159/159 after four rows failed first; the corpus diff moved the four probed verses and nothing else); the spec of
# Exod 34:15-16 CALLED from the erection engine at its Peor run, the judges' 78,600 from the exodus story, Aaron's incense and the plague's
# count from the Korach engine, the hanging from the wood-gatherer's court, the priesthood's addressees from the priesthood engine, the
# parable-tellers from Chukat, the census total from Bamidbar, Isaac's blessing clauses from Mamre, Judah's lion and the gentile mother from the
# family engine, the promise ladder from the primeval engine, the idolatry principle from Shelach; the forty-one lines on the tape with no
# marker (the stretch undated in the ink and on the shelf); THE ZEALOTS' RULE INSTALLED BY A DEED — rule_installed on the tent at the covenant's
# output, the second seat of THE TENT's form with no halt and no docket. Six motions of the deliverable rule, the wrap the sixth; every cell
# cites its source; every token probed (zero-report law); effects on every cell (the effects law). Reading ledgers: the four
# logic/oral_triage/num_{22,23,24,25}_*_2026-09-11.md; the exam's docket: num_22_25_balak_exam_2026-09-11.md (199 rows — 67 LAW, 7 DISPUTE,
# 30 DERIVATION, 95 CONTEXT; 20 credited).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 105, ('the guard counted %d expectations, the tripwire holds 105' % GUARDED)   # the guard's own count, read off the first run (2026-09-11; typed 118 as a placeholder, retyped from the guard's print)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
import effects_layer as FX
import world_engine as WE
import cold_run_erection as ER                   # THE EDGE: balak -> erection CALL, reference (25:1-2 — Exod 34:15-16's spec run; 25:13 — Exod 40:15's clause narrowed)
import cold_run_exodus_story as EX               # THE EDGE: balak -> exodus_story CALL, reference (25:5 — the judges of Israel: Exod 18:21's 78,600)
import cold_run_korach as KR                     # THE EDGE: balak -> korach CALL, reference (25:8, 25:13 — Aaron's incense clause and verb, 17:12-14; the twenty-four gifts)
import cold_run_mekoshesh as MK                  # THE EDGE: balak -> mekoshesh CALL, reference (25:4 — the hanging, Deut 21:22-23's procedure)
import cold_run_priesthood as PR                 # THE EDGE: balak -> priesthood CALL, reference (25:13 — the addressees row Phinehas is the exception to)
import cold_run_chukat as CK                     # THE EDGE: balak -> chukat CALL, reference (23:7 — the parable-tellers' word of 21:27)
import cold_run_bamidbar as BM                   # THE EDGE: balak -> bamidbar CALL, reference (25:9 — the count against the census)
import cold_run_mamre as MM                      # THE EDGE: balak -> mamre CALL, reference (24:9 — Isaac's blessing clauses, Gen 27:29 reversed)
import cold_run_family as FM                     # THE EDGE: balak -> family CALL, reference (24:9 — Judah's lion, Gen 49:9; 25:6 — the gentile mother's rule)
import cold_run_primeval as PV                   # THE EDGE: balak -> primeval CALL, reference (22:6, 24:9 — the promise ladder's two clauses, Gen 12:3)
import cold_run_shelach as SH                    # THE EDGE: balak -> shelach CALL, reference (25:2-3 — the community's idolatry, 15:22-31's principle)
import cold_run_offerings as OF                  # THE EDGE: balak -> offerings CALL, reference (23:3, 23:6, 23:15, 23:17 'your burnt offering' — the olah's institution at Balak's altars)

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

_BYV = {}
for _b, _c, _v, _he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx"):
    _BYV.setdefault((_b, _c, _v), []).append(strip(_he))

def seats_of(tok, books=('Gen', 'Exod', 'Lev', 'Num', 'Deut')):
    return sorted(('%s %d:%d' % k for k, ws in _BYV.items() if k[0] in books and tok in ws), key=lambda s: (s.split()[0], int(s.split()[1].split(':')[0]), int(s.split(':')[1])))

# ---- zero-report probes: the span's load-bearing tokens (every one measured on the DB before it was typed) ----
PROBES = [
    ('ויסעו', 22, 1, 'and they journeyed'), ('בערבות', 22, 1, 'in the plains of'), ('מואב', 22, 1, 'Moab'), ('וירא', 22, 2, 'and he saw'), ('בלק', 22, 2, 'Balak'), ('ויגר', 22, 3, 'and he feared'), ('ויקץ', 22, 3, 'and he loathed'),
    ('ילחכו', 22, 4, 'will lick up'), ('מדין', 22, 4, 'Midian'), ('פתורה', 22, 5, 'to Pethor'), ('ארה', 22, 6, 'curse'), ('וקסמים', 22, 7, 'and divinations'), ('לינו', 22, 8, 'lodge'), ('אלהים', 22, 9, 'God'), ('תאר', 22, 12, 'you shall curse'), ('ברוך', 22, 12, 'blessed'),
    ('מאן', 22, 13, 'refuses'), ('אכבדך', 22, 17, 'I will honor you'), ('כסף', 22, 18, 'silver'), ('וזהב', 22, 18, 'and gold'), ('ואך', 22, 20, 'but only'), ('ויחבש', 22, 21, 'and he saddled'), ('אתנו', 22, 21, 'his she-ass'), ('לשטן', 22, 22, 'as an adversary'),
    ('שלופה', 22, 23, 'drawn'), ('רגל', 22, 25, 'the foot of'), ('ותרבץ', 22, 27, 'and she crouched'), ('ויפתח', 22, 28, 'and He opened'), ('התעללת', 22, 29, 'you have made sport'), ('מעודך', 22, 30, 'from your existence'), ('ויגל', 22, 31, 'and He uncovered'),
    ('שלוש', 22, 32, 'three (plene)'), ('חטאתי', 22, 34, 'I have sinned'), ('ואפס', 22, 35, 'and nothing but'), ('ארנן', 22, 36, 'Arnon'), ('אוכל', 22, 38, 'am I able'), ('ויזבח', 22, 40, 'and he sacrificed'), ('במות', 22, 41, 'Bamoth'),
    ('מזבחת', 23, 1, 'altars'), ('יקרה', 23, 3, 'will chance to meet'), ('ויקר', 23, 4, 'and He met'), ('וישם', 23, 5, 'and He put'), ('משלו', 23, 7, 'his parable'), ('אקב', 23, 8, 'shall I curse'), ('לבדד', 23, 9, 'alone'), ('רבע', 23, 10, 'the fourth part'),
    ('אשמר', 23, 12, 'I keep'), ('אפס', 23, 13, 'only'), ('הפסגה', 23, 14, 'Pisgah'), ('ויתנחם', 23, 19, 'and repent'), ('ותרועת', 23, 21, 'and the shout of'), ('מוציאם', 23, 22, 'brings them out'), ('נחש', 23, 23, 'divination'), ('קסם', 23, 23, 'sorcery'),
    ('כלביא', 23, 24, 'like a lioness'), ('הפעור', 23, 28, 'Peor'), ('נחשים', 24, 1, 'divinations'), ('לשבטיו', 24, 2, 'by its tribes'), ('נאם', 24, 3, 'the utterance of'), ('מחזה', 24, 4, 'the vision of'), ('שדי', 24, 4, 'Shaddai'), ('אהליך', 24, 5, 'your tents'),
    ('כאהלים', 24, 6, 'like aloes'), ('מדליו', 24, 7, 'from his buckets'), ('מאגג', 24, 7, 'than Agag'), ('וחציו', 24, 8, 'and his arrows'), ('שכב', 24, 9, 'he lay down'), ('כארי', 24, 9, 'like a lion'), ('ויספק', 24, 10, 'and he clapped'), ('ברח', 24, 11, 'flee'),
    ('מלבי', 24, 13, 'from my own heart'), ('איעצך', 24, 14, 'I will counsel you'), ('עליון', 24, 16, 'the Most High'), ('כוכב', 24, 17, 'a star'), ('שבט', 24, 17, 'a scepter'), ('וירד', 24, 19, 'and shall rule'), ('עמלק', 24, 20, 'Amalek'), ('הקיני', 24, 21, 'the Kenite'),
    ('אל', 24, 23, 'El'), ('וצים', 24, 24, 'and ships'), ('כתים', 24, 24, 'Kittim'), ('וישב', 24, 25, 'and he returned'), ('בשטים', 25, 1, 'in Shittim'), ('ויחל', 25, 1, 'and began'), ('ותקראן', 25, 2, 'and they called'), ('ויצמד', 25, 3, 'and he yoked himself'),
    ('והוקע', 25, 4, 'and hang'), ('שפטי', 25, 5, 'the judges of'), ('ויקרב', 25, 6, 'and he brought near'), ('רמח', 25, 7, 'a spear'), ('הקבה', 25, 8, 'the alcove'), ('וידקר', 25, 8, 'and he pierced'), ('ותעצר', 25, 8, 'and was stayed'), ('במגפה', 25, 9, 'in the plague'),
    ('קנאתי', 25, 11, 'My zeal'), ('שלום', 25, 12, 'peace'), ('ויכפר', 25, 13, 'and he atoned'), ('זמרי', 25, 14, 'Zimri'), ('כזבי', 25, 15, 'Cozbi'), ('צור', 25, 15, 'Zur'), ('צרור', 25, 17, 'harass'), ('בנכליהם', 25, 18, 'with their wiles'),
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
PLENE = N('Num', 22, 32); assert PLENE == [3], ('the plene "three" at 22:32 — rule (21)', PLENE)
PLENE_KIN = [N('Deut', 16, 16), N('Deut', 19, 2)]; assert PLENE_KIN == [[3], [3]], PLENE_KIN
THREE = [N('Num', 22, 28), N('Num', 22, 33), N('Num', 24, 10)]; assert THREE == [[3], [3], [3]], THREE
THREE_THOUSAND = N('Exod', 32, 28); assert THREE_THOUSAND == [3000], ('the construct "thousands of" — rule (22)', THREE_THOUSAND)
TWO_YOUNG_MEN = N('Num', 22, 22); assert TWO_YOUNG_MEN == [2], TWO_YOUNG_MEN
SEVENS = [N('Num', 23, 1), N('Num', 23, 4), N('Num', 23, 14), N('Num', 23, 29)]; assert SEVENS == [[7, 7, 7], [7], [7], [7, 7, 7]], SEVENS
BOTH = N('Num', 25, 8); assert BOTH == [2], BOTH
COUNT = N('Num', 25, 9); assert COUNT == [24000], COUNT
KORACH_COUNT = N('Num', 17, 14); assert KORACH_COUNT == [14700], KORACH_COUNT
SIMEON = (N('Num', 1, 23), N('Num', 26, 14)); assert SIMEON == ([59300], [22200]), SIMEON
JUDGES_TIERS = N('Exod', 18, 21); assert JUDGES_TIERS == [100, 50, 10], JUDGES_TIERS
ALTARS_TOTAL = sum(SEVENS[0]) // 3 * 3 + 0; assert sum(SEVENS[0]) == 21 and sum(SEVENS[3]) == 21
BEASTS = (SEVENS[0][1] + SEVENS[0][2]) * 3; assert BEASTS == 42, BEASTS                       # seven bulls and seven rams at each of three stands
# ---- THE CROWNS, computed on the ink ----
FORMULA = {(22, 20): ['ואך', 'תעשה'], (22, 35): ['ואפס', 'תדבר'], (22, 38): ['אדבר'], (23, 12): ['אשמר'], (23, 26): ['אעשה'], (24, 13): ['אדבר']}
for (c, v), toks in FORMULA.items():
    assert all(t in verse_text(c, v).split() for t in toks), (c, v, toks)
RESTRICTORS = {(22, 20): 'akh (only)', (22, 35): 'efes (nothing but)', (23, 13): 'efes (only its edge — the restrictor\'s third seat, not a formula seat)'}
assert 'אפס' in verse_text(23, 13).split()
def census(chs, forms):
    return [(c, v, w) for c in chs for v in range(1, 42) if ('Num', c, v) in _BYV for w in _BYV[('Num', c, v)] if w in forms]
ARAR = census((22, 23, 24), {'ארה', 'תאר', 'יואר', 'וארריך', 'ארור'}); assert len(ARAR) == 7, ARAR   # 24:9's 'and those who curse you' carries the vav — the first run's miss
QABAB = census((22, 23, 24), {'קבה', 'לקב', 'אקב', 'וקבנו', 'קב', 'תקבנו', 'וקבתו'}); assert len(QABAB) == 10, QABAB          # 'קבתה' (her belly, 25:8) and 'הקבה' (the alcove) the homographs — the same skin, four pointings
ZAAM = census((22, 23, 24), {'זעמה', 'אזעם', 'זעם'}); assert len(ZAAM) == 3, ZAAM
THEIR_GODS_FEM = sorted(k for k, ws in _BYV.items() if 'לאלהיהן' in ws or 'אלהיהן' in ws); assert [k for k in THEIR_GODS_FEM if k[0] in ('Gen', 'Exod', 'Lev', 'Num', 'Deut')] == [('Exod', 34, 16), ('Num', 25, 2)], THEIR_GODS_FEM   # 1 Kgs 11:8 the Writings' one
DWELT = sorted((k[0], k[1], k[2]) for k, ws in _BYV.items() if 'וישב' in ws and ws.index('וישב') + 1 < len(ws) and ws[ws.index('וישב') + 1] in ('ישראל', 'יעקב', 'יהודה') and k[0] in ('Gen', 'Num', '1Kgs'))
assert {('Num', 25, 1), ('Gen', 37, 1), ('Gen', 47, 27), ('1Kgs', 5, 5)} <= set(DWELT), DWELT          # Sanhedrin 106a:15's four seats (Num 21:25, 21:31 the conquest's, not the rule's)
STANDS = [('Bamoth', 'במות', (22, 41)), ('Pisgah', 'הפסגה', (23, 14)), ('Peor', 'הפעור', (23, 28))]
for name, tok, (c, v) in STANDS: assert tok in verse_text(c, v).split(), (name, c, v)
assert 'במות' in verse_text(21, 19).split() and 'הפסגה' in verse_text(21, 20).split()                         # the first two stands are 21:19-20's last stations
assert 'הנשקף' in verse_text(23, 28).split() and 'ונשקפה' in verse_text(21, 20).split()                        # 23:28 = 21:20's clause with Peor for Pisgah
CURSE_TURNED = 'הקללה' in verse_text(23, 6, book='Deut').split() and 'לברכה' in verse_text(23, 6, book='Deut').split(); assert CURSE_TURNED
MOST_HIGH = seats_of('עליון'); assert 'Num 24:16' in MOST_HIGH and 'Gen 14:18' in MOST_HIGH and 'Deut 32:8' in MOST_HIGH, MOST_HIGH
SPEAR = seats_of('רמח'); assert SPEAR == ['Num 25:7'], SPEAR
ATONED_FOR = [k for k, ws in _BYV.items() if k[0] == 'Num' and 'ויכפר' in ws]; assert sorted(ATONED_FOR) == [('Num', 8, 21), ('Num', 17, 12), ('Num', 25, 13)], ATONED_FOR   # the first run read THREE: 8:21 'and Aaron atoned for THEM' (the Levites' purification) beside the two 'for the people / the children of Israel' seats the reading paired — the token's census, the pairing the reading's
STAYED = [k for k, ws in _BYV.items() if k[0] == 'Num' and 'ותעצר' in ws]; assert sorted(STAYED) == [('Num', 17, 13), ('Num', 25, 8)], STAYED   # the first run read TWO — 17:15's 'was stayed' is another form (the hand had typed three)
PEOR_MATTER = sum(1 for k, ws in _BYV.items() if k[0] == 'Num' and k[1:] in ((25, 18), (31, 16)) for i in range(len(ws) - 1) if ws[i] == 'דבר' and ws[i + 1] == 'פעור'); assert PEOR_MATTER == 3, PEOR_MATTER
# ---- THE CALLEES, measured live at import (the edges) ----
ER_EAT = ER.covenant('eat_sacrifice')['v']; ER_DAUGHTERS = ER.covenant('daughters_two_seats')['v']; ER_PRIESTHOOD = ER.command('everlasting_priesthood')['v']
assert ER_EAT == 1 and ER_DAUGHTERS[0] == [('Exod', 34, 16)] and ER_PRIESTHOOD == 1, (ER_EAT, ER_DAUGHTERS, ER_PRIESTHOOD)
EX_JUDGES = EX.jethro('judges')['v']; assert EX_JUDGES == 78600, EX_JUDGES
KR_INCENSE = KR.plague_and_staffs({'ask': 'incense_atones'}, KR.DATA)[0]; KR_COUNT = KR.plague_and_staffs({'ask': 'plague_count'}, KR.DATA)[0]; assert '14,700' in KR_COUNT, KR_COUNT
KR_24 = KR.DATA['the_twenty_four']['value']; assert len(KR_24['sanctuary']) + len(KR_24['borders']) == 24, KR_24
MK_HANGING = MK.capital_procedure({'ask': 'hanging'}, MK.DATA)[0]; assert MK_HANGING.startswith('not hanged'), MK_HANGING
PR_ADDRESSEES = PR.family('addressees')['v']; assert PR_ADDRESSEES['sons_of_aaron'] == 'bound', PR_ADDRESSEES
CK_TELLERS = CK.well_and_kings({'ask': 'parable_tellers'}, CK.DATA)[0]; assert 'Balaam' in CK_TELLERS, CK_TELLERS
BM_TOTAL = BM.census({'ask': 'total'}, BM.DATA)[0]; assert BM_TOTAL.startswith('603550'), BM_TOTAL
MM_CLAUSES = MM.blessing('blessing_clauses')['v']; assert MM_CLAUSES[-1] == 'cursers_cursed', MM_CLAUSES
FM_LIONS = FM.testament('lions_six_names')['v']; FM_MOTHER = FM.levirate('gentile_mother_rule')['v']; assert FM_LIONS == 2 and FM_MOTHER == 'the_child_follows_her', (FM_LIONS, FM_MOTHER)
PV_LADDER = PV.call('ladder')['v']; assert 'bless_your_blessers' in PV_LADDER and 'curse_your_curser' in PV_LADDER, PV_LADDER
SH_IDOL = SH.error({'ask': 'idolatry_principle'}, SH.DATA)[0]   # the ask lives in shelach's error cell (15:22-29), not the high hand's — read at the first run (KeyError)
OF_OLAH = OF.dispatch('olah'); assert isinstance(OF_OLAH, dict) and 'place' in OF_OLAH, list(OF_OLAH)[:8]   # the burnt offering's cells — the institution 23:3's 'your burnt offering' names (Zevachim 116a: accepted from gentiles)
print('callees live: the spec (Exod 34:15-16) %s / %s; the priesthood clause %s; the judges %d; the incense; the twenty-four; the hanging; the addressees; the tellers; the total; Isaac\'s clauses %d; Judah\'s lion %d; the ladder; the idolatry principle' % (ER_EAT, ER_DAUGHTERS[0], ER_PRIESTHOOD, EX_JUDGES, len(MM_CLAUSES), FM_LIONS))

# =====================================================================
# THE DATA — the parameter rows (the tradition's own vocabulary; the running setting first)
# =====================================================================
DATA = {
    'curse_roots': {'value': {'arar': len(ARAR), 'qabab': len(QABAB), 'zaam': len(ZAAM)}, 'source': 'computed on 22-24 — twenty curse-tokens, no curse spoken (the reading BK22A-03)'},
    'word_formula': {'value': [(c, v, FORMULA[(c, v)][-1], RESTRICTORS.get((c, v), 'none')) for (c, v) in sorted(FORMULA)], 'source': 'computed — the six seats with verb and restrictor (BK22A-05)'},
    'gentile_prophets': {'value': 'balaam_among_them', 'settings': {'balaam_among_them': 'the four who prophesied among the nations — Balaam first (Sanhedrin 105a); Bava Batra 15b'}, 'source': 'Sanhedrin 105a:9'},
    'balaam_blind': {'value': 'one_eye', 'settings': {'one_eye': "'whose eye is open' — blind in one eye (Sanhedrin 105a:16; Niddah 31a:21 the reason)", 'lame_too': "'he went limping' (23:3) — lame in one leg (Sanhedrin 105a:16; Sotah 10a:9)"}, 'source': 'Sanhedrin 105a:16'},
    'balaam_and_the_ass': {'value': 'diviner_by_his_member', 'settings': {'diviner_by_his_member': "Mar Zutra — 'fallen' as Haman fallen (Sanhedrin 105a:17)", 'bestiality': "Mar son of Ravina — 'he crouched, he lay' (Sanhedrin 105a:17; Avodah Zarah 4b:3)"}, 'source': 'Sanhedrin 105a:17'},
    'moment_of_anger': {'value': 'one_58888th_of_an_hour_in_the_first_three_hours', 'settings': {'one_58888th_of_an_hour_in_the_first_three_hours': "Berakhot 7a:8 the measure; Sanhedrin 105b:8 the hour (the rooster's crest); 105b:10 the cause (R. Meir: the kings crown themselves to the sun)", 'none_in_balaams_days': "R. Elazar — God was not angry all those days (Avodah Zarah 4b:5; Berakhot 7a:13; Sanhedrin 105b:6-7)"}, 'source': 'Berakhot 7a:8; Avodah Zarah 4b:4'},
    'house_of_silver': {'value': {'22:18': ('small or great', 'the LORD my God'), '24:13': ('good or bad', 'from my own heart', 'no my God')}, 'source': 'computed — the two seats\' deltas (BK22A-05, BK24A-06)'},
    'stands': {'value': [s[0] for s in STANDS], 'source': "computed — 21:19-20's last stations Bamoth and Pisgah, and Peor (23:28 = 21:20's clause)"},
    'altars_total': {'value': (21, BEASTS), 'source': "the parser's 7, 7, 7 at three stands — Sanhedrin 105b:12 Ruth the reward of the forty-two; Nazir 23b:4"},
    'gentile_olah': {'value': 'accepted_from_gentiles', 'settings': {'accepted_from_gentiles': "Zevachim 116a — burnt offerings accepted from gentiles (Balak's, Jethro's)"}, 'source': 'Zevachim 116a; the exodus story\'s jethro row'},
    'tents_doors': {'value': 'not_aligned', 'settings': {'not_aligned': "R. Yochanan — the entrances not opposite one another: the privacy rule's source (Bava Batra 60a:5)"}, 'source': 'Bava Batra 60a:5'},
    'shema_candidate': {'value': '24:9_lie_down_rise', 'settings': {'24:9_lie_down_rise': "R. Yosei bar Avin — 'he lay down... who shall rouse him' (Berakhot 12b:16); not the Exodus mention (12b:15)"}, 'source': 'Berakhot 12b:15-16'},
    'star_reading': {'value': 'r_akiva_bar_koziba', 'settings': {'r_akiva_bar_koziba': "'a star out of Jacob' — Koziba out of Jacob: this is King Messiah (Jerusalem Talmud Taanit 4:5:13)", 'r_yochanan_ben_torta': "'grass will grow from your jaws and David's son will not have come' (the same)"}, 'source': 'Jerusalem Talmud Taanit 4:5:13; Onkelos Num 24:17 (the KING and the MESSIAH)'},
    'balaam_share': {'value': 'none', 'settings': {'none': "Mishnah Sanhedrin 10:2 — the four commoners; his own sign: 'let me die the death of the upright' / 'I go to my people' (Sanhedrin 105a:12)"}, 'source': 'Mishnah Sanhedrin 10:2; Jerusalem Talmud Sanhedrin 10:2:1-2'},
    'gentile_share': {'value': 'r_yehoshua_god_fearers_have', 'settings': {'r_yehoshua_god_fearers_have': "the mishnah's opinion (Sanhedrin 105a:10-11)", 'r_eliezer_none': "'all the nations that forget God' (Ps 9:18)"}, 'source': 'Sanhedrin 105a:11'},
    'balaam_disciples': {'value': ('an evil eye', 'a haughty spirit', 'a limitless appetite'), 'source': 'Pirkei Avot 5:19'},
    'fourth_part': {'value': 'the_couplings', 'settings': {'the_couplings': "R. Abbahu — God counts the couplings of Israel for the righteous drop (Niddah 31a:20); Balaam's eye blinded (31a:21)"}, 'source': 'Niddah 31a:20-21'},
    'teruah_verse_class': {'value': 'kingship_and_shofarot', 'settings': {'kingship_and_shofarot': 'R. Yosei (Rosh Hashanah 32b:11)', 'kingship_only': 'R. Yehuda'}, 'source': 'Rosh Hashanah 32b:11; 32b:15 the Torah\'s three Kingship verses'},
    'word_in_mouth_mode': {'value': 'an_angel', 'settings': {'an_angel': 'R. Elazar — an angel spoke from his mouth (Sanhedrin 105b:16)', 'a_hook': 'R. Yonatan — a hook in his mouth'}, 'source': 'Sanhedrin 105b:16'},
    'curses_turned': {'value': ('synagogues', 'the Presence', 'the kingdom', 'olives and vineyards', 'fragrance', 'kings of stature', 'a king son of a king', 'rule over nations', 'fierce', 'feared'), 'source': "R. Yochanan's table (Sanhedrin 105b:17-18); R. Abba bar Kahana: all reverted but the synagogues (105b:19; Deut 23:6 'the curse' singular)"},
    'shittim_name': {'value': 'the_place', 'settings': {'the_place': 'R. Eliezer (Bekhorot 5b:5; Sanhedrin 106a:12)', 'nonsense': 'R. Yehoshua — matters of nonsense, harlotry and idolatry'}, 'source': 'Bekhorot 5b:5'},
    'called_the_people': {'value': 'naked_women', 'settings': {'naked_women': 'R. Eliezer (Bekhorot 5b:6; Sanhedrin 106a:13)', 'emissions': 'R. Yehoshua'}, 'source': 'Bekhorot 5b:6'},
    'peor_service': {'value': 'baring', 'settings': {'baring': "one who defecates before Baal-peor is liable — that is its worship (Mishnah Sanhedrin 7:6; Sanhedrin 106a:11; Jerusalem Talmud Sanhedrin 10:2:15; the Sifrei 131:2 at the reading)"}, 'source': 'Mishnah Sanhedrin 7:6'},
    'wine_decree_date': {'value': 'after_peor', 'settings': {'after_peor': "'neither Ammonite wine nor gentile wine had been prohibited yet' (Sanhedrin 106a:10; Jerusalem Talmud 10:2:15; the Sifrei 131:2) — Avodah Zarah 36b's decree later"}, 'source': 'Sanhedrin 106a:10; Avodah Zarah 36b'},
    'hanging_by_courts': {'value': 'the_heads_as_judges_by_day', 'settings': {'the_heads_as_judges_by_day': "'take the heads and hang them' = install the heads as judges and execute by day (Sanhedrin 34b:21, 35a:2; Jerusalem Talmud 10:2:17; Onkelos 'judge and kill')"}, 'source': 'Sanhedrin 35a:2'},
    'each_his_two': {'value': 2, 'source': "the Sifrei 131:2; Jerusalem Talmud 10:2:17 — each judge executes two: 157,200"},
    'zealot_rule': {'value': 'zealots_strike_him', 'settings': {'zealots_strike_him': 'Mishnah Sanhedrin 9:6 — one who cohabits with an Aramean woman; no court death written', 'during_the_act': 'Sanhedrin 82a:10 — separated, the zealot is executed', 'self_defense': "Sanhedrin 82a:10 — the pursued may kill the zealot (a pursuer)", 'not_taught': "Sanhedrin 82a:12 — the law eluded Moses; one who asks is not instructed", 'sinai_law': 'Avodah Zarah 36b:9 — a law to Moses from Sinai, not a decree'}, 'source': 'Mishnah Sanhedrin 9:6; Sanhedrin 81b-82b'},
    'aramean_woman': {'value': FM_MOTHER, 'source': "the family engine's Kiddushin 3:12 row by CALL — the child follows the gentile mother"},
    'cozbi_and_zur': {'value': 'zur_of_the_five_kings', 'source': "31:8's five kings — Evi, Rekem, Zur, Hur, Reba (Josh 13:21); the father dies in the war his daughter's death opens"},
    'high_priest_count': {'value': 'twelve_and_eighty', 'settings': {'twelve_and_eighty': 'the Sifrei 131:4 — twelve in the first Temple, eighty in the second', 'more_than_three_hundred': 'Yoma 9a — the second Temple\'s high priests'}, 'source': 'Sifrei Bamidbar 131:4; Yoma 9a'},
    'atone_tense': {'value': 'future_by_the_sifrei', 'settings': {'future_by_the_sifrei': "'not to atone but AND HE WILL ATONE — he stands and atones until the revival of the dead' (Sifrei 131:5; Sanhedrin 82b:6 forever)", 'past_by_the_morphology': "the tag's narrative past; Onkelos renders a past (the reading BK25A-08)"}, 'source': 'Sifrei Bamidbar 131:5'},
    'twenty_four_gifts': {'value': KR_24, 'source': "korach's DATA by CALL — Bava Kamma 110b; the Sifrei 131:5"},
    'midian_command_run': {'value': ('31:2', '31:7'), 'source': "the debit's run at Matot — 'avenge the vengeance' and the war"},
    'balaam_death': {'value': 'by_the_sword_at_midian', 'settings': {'by_the_sword_at_midian': "31:8; Josh 13:22 — to collect his wages for the twenty-four thousand (Sanhedrin 106a:16; Jerusalem Talmud 10:2:18)", 'four_modes': 'Rav — all four court executions (Sanhedrin 106b:1)'}, 'source': 'Num 31:8; Sanhedrin 106a:16'},
    'phinehas_miracles': {'value': 'twelve', 'settings': {'twelve': 'the Sifrei 131:2 (Sanhedrin 82b)', 'six': 'the Jerusalem Talmud 10:2:17'}, 'source': 'Sifrei Bamidbar 131:2'},
    'vav_of_shalom': {'value': 'severed_by_tradition', 'source': "Rav Nachman (Kiddushin 66b:13) — a letter's shape the DB's bytes cannot carry"},
}

# =====================================================================
# Motion 1 — THE CODE FROM THE VERSES: five cells, every clause cited (INK), every parameter a DATA row, every callee a live CALL
# =====================================================================
# ===== F1: THE CALL (Num 22:1-20) ===========================================================================
def the_call(case, data):
    q = case['ask']; P.clear()
    if q == 'last_camp':
        ink('22:1', "'and camped in the plains of Moab across the Jordan of Jericho' — the book's last camp: nine datelines to 36:13, Moses climbs from them (Deut 34:1)")
        return out('the plains of Moab — the last camp; the book never moves again (22:1; 36:13; Deut 34:1)', ['encamped_at'])
    if q == 'midian_joined':
        ink('22:4, 22:7', "'Moab said to the elders of Midian' (one seat); 'the elders of Moab and the elders of Midian' — Midian enters at 22:4 and 22:7, vanishes, returns at 25:6-18"); move('Sanhedrin 105a:13', 'never at peace before — the two dogs and the wolf')
        return out('Midian joined Moab at 22:4 and 22:7 and returns with Cozbi (25:6-18) — the thread to chapter 31 (Sanhedrin 105a:13)', [FX.NONE])
    if q == 'curse_roots':
        ink('22:6-24:9', 'arar %d, qabab %d, zaam %d — twenty tokens, no curse spoken' % (len(ARAR), len(QABAB), len(ZAAM))); dat('the row curse_roots computed')
        return out('three curse-roots, twenty tokens (arar 7, qabab 10, zaam 3) — and no curse spoken (22:12; Deut 23:6)', [FX.NONE])
    if q == 'blessing_formula':
        ink('22:6, 24:9', "'whom you bless is blessed and whom you curse is cursed' / 'those who bless you are blessed, and those who curse you are cursed'"); move('Gen 12:3 by the primeval engine (CALL)', 'the promise ladder: %s' % ', '.join(PV_LADDER)); move('Gen 27:29 by the mamre engine (CALL)', "Isaac's clauses: %s — the curse first there" % ', '.join(MM_CLAUSES))
        return out("the patriarchs' formula — Gen 12:3 blesses first (the primeval engine's ladder), Gen 27:29 curses first (the mamre engine's clauses); 24:9 returns Isaac's reversed", [FX.NONE])
    if q == 'word_formula':
        ink('22:20, 22:35, 22:38, 23:12, 23:26, 24:13', 'the six seats: %s' % data['word_formula']['value'])
        return out("the word-formula at six seats — do (22:20, akh 'only'), speak (22:35, efes 'nothing but'), speak (22:38), keep (23:12), do (23:26), speak (24:13)", ['bound_to_the_word'])
    if q == 'restrictors':
        ink('22:20, 22:35, 23:13', "akh at 22:20; efes at 22:35 and 23:13 ('only its edge')"); move('THE NUMBERS WALK 4b — 13:5 the export operator', "the restrictor class: 'only' narrows the permission to the word")
        return out("the restrictors — akh 'only' (22:20), efes 'nothing but' (22:35), efes 'only its edge' (23:13): the permission narrowed to the word", ['bound_to_the_word'])
    if q == 'way_one_wishes':
        ink('22:12, 22:20', "'you shall not go with them' then 'rise, go with them'"); move('Makkot 10b:6; Sanhedrin 105a:15', 'in the way a man wishes to go he is led; impudence effective even toward Heaven')
        return out("led in the way he wishes — 'you shall not go' (22:12) then 'rise, go' (22:20): Makkot 10b; Isa 48:17; Prov 3:34", ['cursing_barred'])
    if q == 'cursing_barred':
        ink('22:12', "'you shall not curse the people, for it is blessed' — HEAVEN's block, never closed"); ink('Deut 23:6', 'the curse turned into a blessing — the run citation (%s)' % CURSE_TURNED)
        return out("cursing barred — 'you shall not curse the people, for it is blessed' (22:12): a block never closed; Deut 23:6 the run", ['cursing_barred'])
    if q == 'refuses_spelling':
        ink('22:13-14', "'the LORD refuses' (me'en) — Pharaoh's verb (Exod 7:14, 10:3), Edom's (20:21)"); move('Kiddushin 4a:8', "'Balaam refuses' and 'my yavam refuses' (Deut 25:7) both without a yod — the yod of 'ein' expounded")
        return out("'Balaam refuses' (22:14) written without a yod — Kiddushin 4a's ground for expounding the yod elsewhere; the refusal-verb Pharaoh's", ['refused'])
    if q == 'midian_elders_left':
        ink('22:7-8', "'the elders of Moab and the elders of Midian' at 22:7; 'the princes of Moab stayed' at 22:8 — Midian's elders gone"); move('Sanhedrin 105a:14', "'if he asks the LORD he will not join us'")
        return out("Midian's elders left between 22:7 and 22:8 — the ink's delta the shelf reads (Sanhedrin 105a:14)", [FX.NONE])
    if q == 'beno_form':
        ink('24:3, 24:15, 23:18', "'his son Beor' (beno) for 'son of' — the archaic construct three times"); move('Sanhedrin 105a:9', "R. Yochanan: his father was his son in prophecy")
        return out("'his son Beor' (24:3, 24:15) — the archaic construct the shelf reads as 'his son': Balaam greater than his father (Sanhedrin 105a:9)", [FX.NONE])
    if q == 'balaam_name':
        move('Sanhedrin 105a:7', "belo am (without a nation) / bila am (wore down the nation); Beor — be'ir (bestiality)"); move('Sanhedrin 105a:8', 'Beor = Cushan-Rishathaim = Laban the Aramean')
        return out("Balaam's name expounded — without a nation / wore down the nation; his father Beor read as Laban the Aramean (Sanhedrin 105a:7-8)", [FX.NONE])
    if q == 'prophet_then_diviner':
        ink('22:7', "'divinations in their hand'"); ink('Josh 13:22', "'Balaam the diviner'"); move('Sanhedrin 106a:17', 'first a prophet, at the end a diviner')
        return out("first a prophet, at the end a diviner (Josh 13:22 — Sanhedrin 106a:17); 'divinations in their hand' at 22:7 the noun's Torah four", [FX.NONE])
    if q == 'mimmul':
        ink('22:5', "'they dwell adjacent to me [mimmuli]'"); move('Chullin 19b:14', "'adjacent to' sees the thing and is not it — the slaughter's 'adjacent to its nape' read from Balak's word")
        return out("'adjacent to me' (22:5) — the slaughter law's 'adjacent to the nape' defined from Balak's message (Chullin 19b)", [FX.NONE])
    if q == 'gentile_prophecy_by_night':
        ink('22:9, 22:20', "'and God came to Balaam' — the clause's four Bible seats: Abimelech (Gen 20:3), Laban (31:24), Balaam twice, all by night"); dat('the row gentile_prophets = %s' % data['gentile_prophets']['value'])
        return out("'God came to' — three gentiles by night (Gen 20:3, 31:24; Num 22:9, 22:20), never an Israelite in that clause", [FX.NONE])
    if q == 'house_of_silver':
        ink('22:18, 24:13', 'the clause twice with its deltas: %s' % data['house_of_silver']['value'])
        return out("'his house full of silver and gold' at 22:18 (small or great; the LORD my God) and 24:13 (good or bad; from my own heart; no 'my God')", [FX.NONE])
    if q == 'honor_promised':
        ink('22:17, 24:11', "'I will surely honor you greatly' — revoked: 'the LORD has held you back from honor'")
        return out("the honor promised at 22:17 is revoked at 24:11 in its own words — the debit closed by the revocation", ['honor_owed'])
    if q == 'embassies':
        ink('22:5-6, 22:15-17', "two embassies — 'come, curse this people for me'; 'princes more and weightier'")
        return out("two embassies (22:5-6, 22:15-17) — Balak's pleas to Balaam; the second with the honor", ['plea_made', 'honor_owed'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE SHE-ASS AND THE ANGEL (Num 22:21-41) =======================================================
def the_ass_and_the_angel(case, data):
    q = case['ask']; P.clear()
    if q == 'saddling':
        ink('22:21-22', "'Balaam rose in the morning and saddled his she-ass' and 'his two young men with him' — Gen 22:3's verse (the parser's %s young men)" % TWO_YOUNG_MEN); move('Sanhedrin 105b:11', 'love and hatred upset the conduct of the great — Abraham and Balaam')
        return out("the Akedah's morning at Balaam's (22:21-22 = Gen 22:3): love and hatred upset the conduct of the great (Sanhedrin 105b:11)", [FX.NONE])
    if q == 'three_strikes':
        ink('22:23-27', 'the ass sees three times, Balaam strikes three times; 22:28 counts them: %s' % THREE[0])
        return out('struck three times (22:23, 22:25, 22:27) — the parser\'s 3 at 22:28 and 22:33, the plene three at 22:32', ['beaten'])
    if q == 'mouth_of_the_ass':
        ink('22:28', "'and the LORD opened the mouth of the she-ass' — the one seat"); move('Mishnah Avot 5:6', 'the mouth of the donkey the third of the ten things of twilight')
        return out('the mouth of the she-ass created at twilight — the third of the ten (Avot 5:6); opened at 22:28', ['mouth_opened'])
    if q == 'yarat':
        ink('22:32', "'the way is contrary [yarat] before me'"); move('Menachot 66b:6; Shabbat 105a:4', 'notarikon (an abbreviation reading): feared, saw, turned')
        return out("'yarat' (22:32) read as an abbreviation: the ass feared, saw, turned (Menachot 66b; Shabbat 105a)", ['adversary_in_the_way'])
    if q == 'eyes_uncovered':
        ink('22:31, 24:4, 24:16', "'the LORD uncovered Balaam's eyes' — his title afterward: 'fallen and with uncovered eyes'")
        return out("the eyes uncovered at 22:31 — Balaam's own title at 24:4 and 24:16", ['eyes_uncovered'])
    if q == 'confession':
        ink('22:34', "'I have sinned' — Pharaoh's confession (Exod 9:27, 10:16)")
        return out("'I have sinned' (22:34) — Pharaoh's confession at Balaam's mouth, the Torah's two gentile confessions", ['confessed'])
    if q == 'sword_spelling':
        ink('22:23, 22:31', "'his sword drawn' plene at the ass's seeing, defective at Balaam's")
        return out("'drawn' plene at 22:23 and defective at 22:31 — the ass's seeing and Balaam's, eight verses apart", [FX.NONE])
    if q == 'times_word':
        ink('22:28, 22:32, 22:33, 24:10', "'three TIMES' as regalim (feet) for the ass, pe'amim for the blessings — two times-words; the plene at 22:32 read %s" % PLENE)
        return out("two times-words — the ass's 'three feet' (regalim, 22:28, 22:32 plene, 22:33) and Balak's 'three times' (pe'amim, 24:10): the festivals' two words", [FX.NONE])
    if q == 'stands_stations':
        ink('22:41, 23:14, 23:28', 'the three stands: %s' % data['stands']['value']); ink('21:19-20', "Bamoth and Pisgah the well-song's last stations; 23:28 = 21:20's clause with Peor for Pisgah")
        return out("the three stands are chapter 21's last stations — Bamoth (22:41 = 21:19), Pisgah (23:14 = 21:20), Peor (23:28 = 21:20's clause): the third the god of 25:3", [FX.NONE])
    if q == 'adversary':
        ink('22:22, 22:32', "'as an adversary' — the satan-word's two Torah seats, both here")
        return out("the angel as an adversary (22:22, 22:32) — the satan-word's two Torah seats; God's anger the first of three", ['adversary_in_the_way', 'mark_of_anger'])
    if q == 'anger_mark':
        move('Zevachim 102a', "every anger leaves a mark"); ink('22:22, 24:10, 25:3', 'the three angers — the adversary, the honor revoked, the plague')
        return out("three angers, three marks — God's at Balaam (the adversary, 22:22), Balak's at Balaam (the honor revoked, 24:10), the LORD's at Israel (the plague, 25:3)", ['mark_of_anger'])
    if q == 'balaam_and_the_ass':
        dat('the row balaam_and_the_ass = %s' % data['balaam_and_the_ass']['value']); move('Sanhedrin 105a:17; Avodah Zarah 4b:2-3', "the ass's rebuke; the night service — the dispute")
        return out("a diviner by his member (Mar Zutra) / bestiality with his ass (Mar son of Ravina) — DISPUTE (Sanhedrin 105a:17)", [FX.NONE])
    if q == 'edge_of_the_people':
        ink('22:41, 23:13', "'he saw from there the edge of the people'; 'only its edge you will see'")
        return out("the edge of the people seen from Bamoth (22:41), 'only its edge' at 23:13 — the restrictor's third seat", [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE THREE STANDS AND THE FOUR PARABLES (Num 23:1-24:25) ===========================================
def the_stands(case, data):
    q = case['ask']; P.clear()
    if q == 'forty_two_offerings':
        ink('23:1-2, 23:14, 23:29-30', 'seven altars three times, a bull and a ram on each — the parser\'s %s; %d altars, %d beasts' % (SEVENS[0], data['altars_total']['value'][0], data['altars_total']['value'][1])); move('Sanhedrin 105b:12; Nazir 23b:4', 'Ruth the reward of the forty-two')
        return out('twenty-one altars, forty-two beasts (7, 7, 7 × 3) — Ruth the reward (Sanhedrin 105b:12; Nazir 23b)', ['altars_built', 'offered_burnt_and_sacrifices'])
    if q == 'gentile_olah':
        dat('the row gentile_olah = %s' % data['gentile_olah']['value']); move('Zevachim 116a', "burnt offerings accepted from gentiles — Balak's and Jethro's"); move('cold_run_offerings (CALL)', "the olah's cells: place %s" % OF_OLAH['place']['v'] if isinstance(OF_OLAH.get('place'), dict) else str(OF_OLAH.get('place'))[:60])
        return out("Balak's burnt offerings accepted from a gentile (Zevachim 116a) — Jethro's row the exodus engine's", ['offered_burnt_and_sacrifices'])
    if q == 'most_high_knowledge':
        ink('24:16', "'and knows the knowledge of the Most High'"); move('Avodah Zarah 4b:1-4; Sanhedrin 105b:2-5; Berakhot 7a:8', "not God's thoughts (he did not know his animal's) — the moment of anger"); dat('the row moment_of_anger = %s' % data['moment_of_anger']['value'])
        return out("'knows the knowledge of the Most High' = fixes the moment of God's anger (one 58,888th of an hour) — Berakhot 7a; Avodah Zarah 4b", [FX.NONE])
    if q == 'no_anger_those_days':
        ink('23:8', "'how shall I curse whom El has not cursed'"); move('Avodah Zarah 4b:5; Berakhot 7a:13; Sanhedrin 105b:6-7', 'God was not angry all those days — Micah 6:5')
        return out("no anger in Balaam's days — 'how shall I curse whom El has not cursed' (23:8); Micah 6:5 'know the righteous acts'", ['oracle_blessed'])
    if q == 'moment_of_anger':
        dat('the row moment_of_anger: the measure Berakhot 7a:8, the hour Sanhedrin 105b:8, the cause 105b:10')
        return out("God's anger a moment daily — the first three hours, when the kings crown themselves to the sun and the rooster's crest whitens (Sanhedrin 105b:8-10)", [FX.NONE])
    if q == 'death_of_the_upright':
        ink('23:10, 24:14', "'let me die the death of the upright' / 'I go to my people'"); move('Sanhedrin 105a:12; Avodah Zarah 25a:1', "his own sign; the book of Yashar = Genesis, the book of the upright patriarchs")
        return out("'the death of the upright' — the patriarchs' (the book of Yashar, Avodah Zarah 25a); Balaam's sign for himself, 'I go to my people' the other arm (Sanhedrin 105a:12)", [FX.NONE])
    if q == 'balaam_share':
        dat('the row balaam_share = %s' % data['balaam_share']['value']); move('Mishnah Sanhedrin 10:2; Jerusalem Talmud Sanhedrin 10:2:1-2', 'the four commoners; all invented new sins')
        return out('no share in the world to come — Balaam among the four commoners (Mishnah Sanhedrin 10:2)', [FX.NONE])
    if q == 'gentile_share':
        dat('the row gentile_share = %s' % data['gentile_share']['value']); move('Sanhedrin 105a:10-11', "R. Yehoshua against R. Eliezer on Ps 9:18")
        return out("gentiles who fear God have a share — R. Yehoshua's, the mishnah's opinion (Sanhedrin 105a:11); Balaam alone excluded", [FX.NONE])
    if q == 'balaam_disciples':
        dat('the row balaam_disciples = %s' % (data['balaam_disciples']['value'],)); move('Pirkei Avot 5:19', "an evil eye, a haughty spirit, a limitless appetite")
        return out("Balaam's disciples — an evil eye, a haughty spirit, a limitless appetite — inherit Gehinnom (Avot 5:19)", [FX.NONE])
    if q == 'curses_turned':
        ink('24:5-7', "the clauses — tents, dwellings, streams, gardens, aloes, cedars, buckets, many waters, Agag, exalted"); move('Sanhedrin 105b:17-19', "R. Yochanan's table; R. Abba bar Kahana: all reverted but the synagogues — Deut 23:6 'the curse' singular")
        return out("each clause of 24:5-7 the curse he intended (Sanhedrin 105b:17-18); all reverted but the synagogues — Deut 23:6's singular 'curse' (105b:19)", ['oracle_blessed'])
    if q == 'reed_and_cedar':
        ink('24:6', "'as cedars beside the waters'"); move('Taanit 20a:15; Sanhedrin 105b:20-106a:2', "Ahijah's reed-curse better than Balaam's cedar-blessing")
        return out("the cedar-blessing worse than Ahijah's reed-curse — the reed bends and yields the quill; the cedar falls to the south wind (Taanit 20a; Sanhedrin 105b-106a)", [FX.NONE])
    if q == 'shema_candidate':
        ink('24:9', "'he couched, he lay down like a lion... who shall rouse him'"); move('Berakhot 12b:15-16', "the Sages sought to fix Balak's portion in the Shema for 24:9's lying down and rising; not for the Exodus mention")
        return out("Balak's portion nearly fixed in the Shema — for 24:9's 'lay down... rouse him' (Berakhot 12b:16), not for 23:22's Exodus (12b:15)", [FX.NONE])
    if q == 'tents_doors':
        ink('24:2', "'he saw Israel dwelling by its tribes'"); move('Bava Batra 60a:5', "the entrances not aligned — the privacy rule's source")
        return out("the tents' doors not aligned — 'dwelling by its tribes' (24:2) the source that one may not open an entrance opposite another's (Bava Batra 60a)", ['spirit_rested'])
    if q == 'tents_aloes':
        ink('24:5-6', "'your tents' (ohalekha) and 'like aloes' (ahalim) — one consonantal skin"); move('Berakhot 16a:1', 'tents juxtaposed to streams — read ohalim')
        return out("the tents and the aloes one skin (24:5-6) — Berakhot 16a reads the aloes as tents of Torah beside the purifying streams", [FX.NONE])
    if q == 'motzi_tense':
        ink('23:22', "'El who brought them out [motziam] of Egypt'"); move('Berakhot 38a:14', "Rava: motzi is past — the bread blessing's word argued from it")
        return out("'motzi' past tense from 23:22 — the bread blessing's 'who brings forth' argued from Balaam's verse (Berakhot 38a)", [FX.NONE])
    if q == 'blood_of_the_slain':
        ink('23:24', "'and drinks the blood of the slain'"); move('Chullin 35b:14; Keritot 22a:14; Niddah 19b:10, 55b:21', 'blood after death a liquid that renders susceptible; the spurting blood excluded; the wound\'s blood too')
        return out("'the blood of the slain' (23:24) — the blood that flows at death is the liquid that renders food susceptible; not the spurting blood; a wound's blood too (Chullin 35b; Keritot 22a; Niddah 19b, 55b)", [FX.NONE])
    if q == 'fourth_part':
        ink('23:10', "'the fourth part [rova] of Israel' — the quarter's consonants, Reba's, the bestiality-verb's (the reading BK23A-04)"); move('Niddah 31a:20', "R. Abbahu: God counts the couplings")
        return out("'the fourth part of Israel' read as the couplings God counts (Niddah 31a:20) — the homograph the reading told by the points", [FX.NONE])
    if q == 'opened_eye':
        ink('24:3', "'the man of the opened eye'"); move('Sanhedrin 105a:16; Niddah 31a:21', 'blind in one eye — the other blinded for objecting'); dat('the row balaam_blind = %s' % data['balaam_blind']['value'])
        return out("blind in one eye — 'the man of the opened eye' (24:3): Sanhedrin 105a:16; Niddah 31a:21 the reason", [FX.NONE])
    if q == 'shefi':
        ink('23:3', "'he went limping [shefi]' — the bare height, Onkelos 'alone'"); move('Sanhedrin 105a:16; Sotah 10a:9', 'lame in one leg; Samson in both')
        return out("lame in one leg — 'shefi' (23:3): Sanhedrin 105a:16 (the reading's 'bare height', Onkelos's 'alone')", [FX.NONE])
    if q == 'teruah_of_a_king':
        ink('23:21', "'the teruah of a king is among him' — the teruah-word's Torah seven; Onkelos the Shekhinah"); move('Rosh Hashanah 32b:11-15', "a Kingship verse of the Torah's three; with shofarot too (R. Yosei) / Kingship alone (R. Yehuda)"); dat('the row teruah_verse_class = %s' % data['teruah_verse_class']['value'])
        return out("23:21 one of the Torah's three Kingship verses (with Deut 33:5, Exod 15:18); recited with the shofarot too (R. Yosei) — DISPUTE (Rosh Hashanah 32b)", [FX.NONE])
    if q == 'no_divination':
        ink('23:23', "'no divination in Jacob and no sorcery in Israel' — the serpent's word in the diviner's mouth"); move('Nedarim 32a:12-13', 'the plain sense kept; one who does not divine is brought within the partition')
        return out("'no divination in Jacob' (23:23) — the plain sense kept against Rebbi's reading; the non-diviner brought within the partition (Nedarim 32a)", [FX.NONE])
    if q == 'dwells_alone':
        ink('23:9', "'a people that dwells alone and is not reckoned among the nations' — the leper's two words (Lev 13:46)"); move('Sanhedrin 39b:1', "where a verse says 'the nations', Israel is not included")
        return out("'not reckoned among the nations' (23:9) — the definition rule: 'the nations' excludes Israel (Sanhedrin 39b)", [FX.NONE])
    if q == 'kabbo_curse':
        ink('23:8', "'how shall I curse [ekkov] whom El has not cursed [kabbo]'"); move('Sanhedrin 56a:6, 92a:1; Sotah 41b:13', "nokev / kov = cursing — the blasphemer's verb and Proverbs' defined from Balaam's")
        return out("the qabab-root's definition seat — 'kabbo' = a curse (23:8): the blasphemer's 'nokev' read from it (Sanhedrin 56a; lev24's first call)", [FX.NONE])
    if q == 'eitan':
        ink('24:21', "'firm [eitan] is your dwelling, and your nest set in the sela' — Meribah's rock-word"); move('Rosh Hashanah 11a:8; Sotah 46b:1', 'eitan = mighty (the patriarchs as mountains) / hard / old')
        return out("'eitan' (24:21) = mighty (Rosh Hashanah 11a), hard as a rock or old (Sotah 46b) — the Kenite's nest in the sela, sitting 6's rock-word", [FX.NONE])
    if q == 'who_shall_live':
        ink('24:23', "'alas, who shall live when El appoints this'"); move('Sanhedrin 106a:5', "Reish Lakish: woe to him who lives in God's name; R. Yochanan: woe to the nation hindering the redemption")
        return out("'who shall live when El appoints this' (24:23) — two readings: the indulgent in God's name; the nation between the lion and the lioness (Sanhedrin 106a:5)", [FX.NONE])
    if q == 'kittim':
        ink('24:24', "'ships from the hand of Kittim... afflict Asshur and afflict Eber' — Daniel 11:30 quotes; Onkelos the Romans"); move('Sanhedrin 106a:6', "Rav: the Roman legion against Assyria — kill, then enslave")
        return out("Kittim's ships = the Roman legion (Sanhedrin 106a:6; Onkelos 'the Romans'); Daniel 11:30 the quotation", [FX.NONE])
    if q == 'counsel_inverted':
        ink('24:14', "'what this people will do to your people' — the reverse expected"); move('Sanhedrin 106a:7', 'he curses himself obliquely')
        return out("'what this people will do to your people' (24:14) — the inverted clause: Balaam curses himself obliquely (Sanhedrin 106a:7)", ['counsel_given'])
    if q == 'counsel':
        ink('24:14, 31:16, 25:18', "'come, I will counsel you' — 'in the matter of Peor' %d times, 'by the word of Balaam' at 31:16" % PEOR_MATTER); move('Sifrei Bamidbar 131:1', "R. Akiva's adjacency to 25:1 against Rebbi — the ink's own back-reference at 31:16")
        return out("the counsel (24:14) named as Peor's cause by the ink at 31:16 ('by the word of Balaam... in the matter of Peor'); the Sifrei's adjacency dispute beside it", ['counsel_given'])
    if q == 'star_reading':
        ink('24:17', "'a star steps forth from Jacob and a scepter rises from Israel' — Judah's scepter (Gen 49:10); Onkelos a KING and the MESSIAH"); dat('the row star_reading = %s' % data['star_reading']['value']); move('Jerusalem Talmud Taanit 4:5:13', "R. Akiva: Koziba out of Jacob — this is King Messiah; R. Yochanan ben Torta: grass will grow from your jaws")
        return out("the star applied to bar Koziba by R. Akiva and refused by R. Yochanan ben Torta (Jerusalem Talmud Taanit 4:5) — Onkelos's KING and MESSIAH the translation's text", [FX.NONE])
    if q == 'word_in_mouth_mode':
        ink('23:5, 23:16', "'the LORD put a word in Balaam's mouth' — Deut 18:18's prophet-clause"); dat('the row word_in_mouth_mode = %s' % data['word_in_mouth_mode']['value']); move('Sanhedrin 105b:16', 'an angel from his mouth / a hook in his mouth')
        return out("a word put in his mouth (23:5, 23:16) — an angel spoke from it (R. Elazar) / a hook held it (R. Yonatan): DISPUTE (Sanhedrin 105b:16)", ['word_put_in_mouth'])
    if q == 'judah_blessing':
        ink('24:9', "'he crouched, lay down like a lion and like a lioness — who will rouse him' = Gen 49:9 with two words exchanged (shakhav for ravatz, ari for aryeh)"); move("Gen 49:9 by the family engine (CALL)", "the lion's six names — %d of them here" % FM_LIONS)
        return out("Jacob's blessing of Judah in Balaam's mouth (24:9 = Gen 49:9 but two words) — the family engine's lion (two of the six names)", ['oracle_blessed'])
    if q == 'isaac_formula':
        ink('24:9', "'those who bless you are blessed, and those who curse you are cursed' — Gen 27:29 reversed (the curse first there)"); move('Gen 27:29 by the mamre engine (CALL)', "Isaac's six clauses, the last 'cursers_cursed'")
        return out("Isaac's formula reversed at 24:9 — Gen 27:29 curses first (the mamre engine's clauses), Balaam blesses first", ['oracle_blessed'])
    if q == 'promise_ladder':
        move('Gen 12:3 by the primeval engine (CALL)', "the ladder: %s" % ', '.join(PV_LADDER))
        return out("the promise ladder of Gen 12:2-3 — 'bless your blessers, curse your curser' — the formula's first seat (the primeval engine)", [FX.NONE])
    if q == 'one_letter':
        ink('23:22, 24:8', "'El brings THEM out of Egypt' / 'El brings HIM out' — one letter (a mem for a vav)")
        return out("23:22 -> 24:8 with one letter changed — 'brings them out' to 'brings him out'", [FX.NONE])
    if q == 'parables':
        ink('23:7, 23:18, 24:3, 24:15, 24:20, 24:21, 24:23', "'he took up his parable' seven times — 21:27's parable-tellers' word"); move('cold_run_chukat (CALL)', 'the parable-tellers: %s' % CK_TELLERS)
        return out("seven parables taken up — the parable-tellers' word of 21:27 (chukat's row PAID: Balaam and Beor the tellers, Chullin 60b)", ['oracle_blessed'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: PEOR — THE SIN, THE HANGING, THE JUDGES, THE ZEALOT (Num 25:1-9) ================================
def peor(case, data):
    q = case['ask']; P.clear()
    if q == 'spec_run':
        ink('25:1-2', "'the people began to whore after the daughters of Moab; and they called the people to the sacrifices of their gods, and the people ate and bowed to their gods' — Exod 34:15-16 clause by clause; the feminine 'their gods' at %s alone" % [k for k in THEIR_GODS_FEM if k[0] != '1Kgs']); move('Exod 34:15-16 by the erection engine (CALL)', "covenant('eat_sacrifice') = %s; ('daughters_two_seats') names %s" % (ER_EAT, ER_DAUGHTERS[0])); move('M-22 the run teaches the spec', 'the Numbers exemplar (MOVE_CATALOG.md)')
        return out("Exod 34:15-16's spec RUN at 25:1-2 — whored after their daughters, ate of their sacrifices, bowed to their gods; the feminine 'their gods' at the two seats alone (the erection engine CALLED)", ['whored_after', 'bowed_to_their_gods'])
    if q == 'shittim_name':
        dat('the row shittim_name = %s' % data['shittim_name']['value']); move('Bekhorot 5b:5; Sanhedrin 106a:12', "the place's name (R. Eliezer) / nonsense (R. Yehoshua)"); ink('25:1', "'Shittim' — the tabernacle's acacia timber, the last camp (33:49)")
        return out("Shittim the place's name (R. Eliezer) / an allusion to nonsense, harlotry and idolatry (R. Yehoshua) — DISPUTE (Bekhorot 5b)", ['encamped_at'])
    if q == 'called_the_people':
        dat('the row called_the_people = %s' % data['called_the_people']['value']); move('Bekhorot 5b:6; Sanhedrin 106a:13', 'naked women met them (R. Eliezer) / emissions (R. Yehoshua)')
        return out("'and they called the people' (25:2) — naked women met them (R. Eliezer) / they all had emissions (R. Yehoshua): DISPUTE (Bekhorot 5b)", [FX.NONE])
    if q == 'dwelt_is_pain':
        ink('25:1', "'and Israel dwelt in Shittim'"); move('Sanhedrin 106a:15', "every 'and he dwelt' is pain — the four seats computed: %s" % [k for k in DWELT if k in {('Num', 25, 1), ('Gen', 37, 1), ('Gen', 47, 27), ('1Kgs', 5, 5)}])
        return out("'and Israel dwelt' — every 'and he dwelt' announces pain: Shittim, Jacob (Gen 37:1), Goshen (47:27), Judah and Israel (1 Kgs 5:5) — Sanhedrin 106a:15, the four seats computed", [FX.NONE])
    if q == 'peor_service':
        dat('the row peor_service = %s' % data['peor_service']['value']); move('Mishnah Sanhedrin 7:6; Sanhedrin 106a:11; Jerusalem Talmud Sanhedrin 10:2:15; Sifrei Bamidbar 131:2', "'you do not bow, you only strip for it' — the Sages: baring is its worship")
        return out("baring oneself to Peor is its worship — liable as an idolater (Mishnah Sanhedrin 7:6): the Sifrei's rule at the reading, the answer sheet here", ['stoned'])
    if q == 'wine_decree_date':
        dat('the row wine_decree_date = %s' % data['wine_decree_date']['value']); move('Sanhedrin 106a:10; Jerusalem Talmud 10:2:15; Sifrei 131:2', "'neither Ammonite wine nor gentile wine had been prohibited yet' — Avodah Zarah 36b's decree later")
        return out("the decree on gentile wine is later than Peor — 'not yet forbidden' at Shittim (Sanhedrin 106a:10; the Sifrei; the Jerusalem Talmud): a law's installation dated by the shelf", [FX.NONE])
    if q == 'yoked_like_the_lid':
        ink('25:3, 25:5, 19:15', "'yoked' (nitzmad) — its noun 19:15's cord-bound lid (tzamid patil)"); move('Sanhedrin 64a:11', "like a tightly bound cover on a vessel — against 'cleave to the LORD' like two dates")
        return out("yoked to Baal-peor like a cord-bound lid on a vessel (Sanhedrin 64a:11 — 19:15's word, the reading's crown); Israel to the LORD like two dates lightly touching", ['yoked_to_baal_peor'])
    if q == 'hang_before_the_sun':
        ink('25:4', "'take all the heads of the people and hang them to the LORD before the sun' — Saul's sons' verb (2 Sam 21:6)"); move('Sanhedrin 34b:21, 35a:2; Jerusalem Talmud 10:2:17', 'judged by day; the heads as judges hang the sinners; Onkelos: judge and kill'); move('Deut 21:22-23 by the wood-gatherer\'s court (CALL)', 'the hanging after the stoning: %s' % MK_HANGING)
        return out("'hang them before the sun' — the heads installed as judges, the sinners judged by day and hanged (Sanhedrin 34b-35a; the Jerusalem Talmud); the wood-gatherer's court: the idolater hanged after stoning", ['commanded'])
    if q == 'judges_count':
        move('Exod 18:21 by the exodus engine (CALL)', 'the judges of Israel %d' % EX_JUDGES); dat('the row each_his_two = %d — %d executed (the Jerusalem Talmud 10:2:17)' % (data['each_his_two']['value'], EX_JUDGES * data['each_his_two']['value']))
        return out("the judges of Israel 78,600 (Exod 18:21's tiers by the exodus engine) — each executing two = 157,200 (the Jerusalem Talmud Sanhedrin 10:2:17; the Sifrei 131:2)", ['commanded'])
    if q == 'zealot_rule':
        arm = case.get('arm', 'in_the_act')
        dat('the row zealot_rule = %s; the arms: %s' % (data['zealot_rule']['value'], sorted(data['zealot_rule']['settings'])))
        move('Mishnah Sanhedrin 9:6', "one who cohabits with an Aramean woman — zealots strike him"); move('Sanhedrin 82a:10', 'during the act only; the pursued may kill the zealot; not taught'); ink('25:6-8', 'the bringing-near and the spear — the act and its end')
        if arm == 'in_the_act':
            return out("zealots strike him — Zimri in the act (Mishnah Sanhedrin 9:6; Sanhedrin 82a); the cohabits entry OPEN from 25:6 to the spear", ['cohabits_with_an_aramean', 'slain'])
        if arm == 'separated':
            return out("separated — the zealot who then strikes is a murderer, executed (Sanhedrin 82a:10)", ['exempt'])
        if arm == 'self_defense':
            return out("Zimri turning and killing Phinehas — not executed: the zealot is a pursuer (Sanhedrin 82a:10)", ['exempt'])
        if arm == 'asks_the_court':
            return out("one who asks the court is not instructed — the law is not taught (Sanhedrin 82a:12; Moses forgot it)", ['exempt'])
        return out('no arm named', [FX.NONE])
    if q == 'halakha_forgotten':
        ink('25:6', "'before the eyes of Moses... and they were weeping at the door of the tent'"); move('Sanhedrin 82a:12', "'is she forbidden? who permitted Jethro's daughter?' — the law eluded Moses; the Sanhedrin wept; Phinehas saw")
        return out("the law forgotten by Moses at 25:6 — the Sanhedrin wept, the zealot remembered (Sanhedrin 82a:12): the rule not taught, installed by the deed", ['wept'])
    if q == 'no_weapon_in_the_hall':
        ink('25:7', "'he rose from the midst of the congregation and took a spear' — the spear the Torah's one (%s)" % SPEAR); move('Sanhedrin 82a:15', 'one does not enter the study hall armed; the blade hidden')
        return out("the spear taken only after rising from the assembly (25:7) — one does not enter the study hall armed (Sanhedrin 82a:15); the Torah's one spear", [FX.NONE])
    if q == 'cast_before_god':
        ink('25:8-9', "'and the plague was stayed' — Aaron's clause; 'the dead in the plague' — Korach's formula; the count %s" % COUNT); move('Sanhedrin 44a:14, 82b:3', "Phinehas cast them before God: 'for these shall twenty-four thousand fall?' — Ps 106:30 'executed judgment'")
        return out("cast before God — 'shall twenty-four thousand fall for these?' (Sanhedrin 82b:3; Ps 106:30): the plague stayed at the spear, the count 24,000 by the parser", ['plague_struck', 'slain'])
    if q == 'for_its_sake':
        move('Horayot 10b:15; Nazir 23b:4', "Tamar for a mitzvah — kings and prophets; Zimri for a transgression — twenty-four thousand fell")
        return out("Zimri's licentiousness not for its own sake — twenty-four thousand fell (Nazir 23b; Horayot 10b); Tamar's for a mitzvah bore kings", [FX.NONE])
    if q == 'plague_count':
        ink('25:9, 17:14', "'the dead in the plague were' — 24,000 here, 14,700 at Korach (the parser's %s, %s)" % (COUNT, KORACH_COUNT)); move('cold_run_korach (CALL)', KR_COUNT); move('cold_run_bamidbar (CALL)', 'the total %s; Simeon %s -> %s (1:23, 26:14)' % (BM_TOTAL.split()[0], SIMEON[0], SIMEON[1]))
        return out("the plague's dead 24,000 (25:9) — Korach's formula and 14,700 (17:14); Simeon 59,300 -> 22,200 the checkpoint at the second census; the total 603,550 (bamidbar CALLED)", ['plague_struck'])
    if q == 'aaron_and_phinehas':
        ink('25:8, 25:13, 17:12-13', "'and the plague was stayed' at %s; 'and he atoned for' at %s — the father's censer and the son's spear one clause and one verb" % (sorted(STAYED), sorted(ATONED_FOR))); move('cold_run_korach (CALL)', KR_INCENSE); move('Sifrei Bamidbar 131:3', 'turner-away of wrath, son of a turner-away')
        return out("Aaron's incense clause and verb at Phinehas's spear — 'the plague was stayed' (17:13, 25:8) and 'he atoned for' (17:12, 25:13): the Sifrei's father-son title measured on the ink; korach's incense cell CALLED", ['plague_struck'])
    if q == 'idolatry_principle':
        move('cold_run_shelach (CALL)', SH_IDOL); ink('25:2-3', "the community ate, bowed and yoked itself — 15:22-31's class")
        return out("the Peor congregation under 15:22-31's principle — the shelach engine's idolatry_principle row CALLED (its error cell)", ['yoked_to_baal_peor'])
    if q == 'anger_third':
        ink('25:3', "'and the anger of the LORD burned against Israel' — the third anger; 32:13-14 Moses retells it"); move('Zevachim 102a', 'the mark: the plague')
        return out("the third anger (25:3) — its mark the plague, stayed by the spear (25:8)", ['mark_of_anger', 'plague_struck'])
    if q == 'aramean_woman':
        dat('the row aramean_woman = %s' % data['aramean_woman']['value']); move('Kiddushin 3:12 by the family engine (CALL)', "the child follows the gentile mother")
        return out("the Midianite woman's child would follow her (Kiddushin 3:12 by the family engine) — the case the zealots strike in (Mishnah Sanhedrin 9:6)", ['cohabits_with_an_aramean'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: PHINEHAS AND MIDIAN (Num 25:10-19) ================================================================
def phinehas_and_midian(case, data):
    q = case['ask']; P.clear()
    if q == 'priesthood_by_the_deed':
        ink('25:13', "'a covenant of everlasting priesthood' — written after the deed; Phinehas born Exod 6:25, silent until 25:7"); move('Zevachim 101b:10', 'Phinehas did not become a priest until he killed Zimri'); move('cold_run_priesthood (CALL)', 'the addressees row: %s — the grandson the named exception' % PR_ADDRESSEES)
        return out("Phinehas not a priest until he killed Zimri — 'a covenant of everlasting priesthood' written only after (Zevachim 101b); the priesthood engine's addressees bind the sons of Aaron, this grandson the exception", ['invested_office'])
    if q == 'covenant_of_peace':
        ink('25:12', "'behold, I give him My covenant of peace' — one seat; Malachi's covenant with Levi (2:5)"); move('Sanhedrin 82b:6', 'greet Phinehas first with peace; the atonement forever')
        return out("the covenant of peace (25:12) — HEAVEN's entry in force forever; God to Moses: greet him first with peace (Sanhedrin 82b:6)", ['covenant_of_peace'])
    if q == 'seed_after_him':
        ink('25:13', "'for him and for his seed after him'"); move('Ketubot 13b:16; Yevamot 100b:8', "a priest whose seed is attributed to him — the shetuki (father unknown) silenced from the service")
        return out("'his seed after him' — the priest's descendants must be attributed to him: the shetuki serves not, marries yes (Ketubot 13b; Yevamot 100b)", [FX.NONE])
    if q == 'unfit_seed_service':
        move('Kiddushin 66b:10', "'his seed after him' includes unfit seed — the divorcee's son's service valid after the fact")
        return out("the disqualified priest's service valid after the fact — 'his seed after him' includes unfit seed (Kiddushin 66b:10)", ['accepted'])
    if q == 'blemished_service':
        ink('25:12', "'My covenant of peace [shalom]' — read whole [shalem]"); dat('the row vav_of_shalom = %s' % data['vav_of_shalom']['value']); move('Kiddushin 66b:13', "the blemished priest's service retroactively invalid; Rav Nachman: the vav severed by tradition")
        return out("the blemished priest's service invalid — 'peace' read 'whole' (Kiddushin 66b:13); the severed vav a letter's shape the DB's bytes cannot carry", ['disqualified'])
    if q == 'lineage_answer':
        ink('25:7, 25:11', "'Phinehas son of Eleazar son of Aaron the priest' — the three-generation title twice"); move('Sanhedrin 82b:5; Sifrei Bamidbar 131:3', "the tribes' taunt 'son of Puti'; the verse answers with the lineage — three generations as three deeds")
        return out("the lineage answers the taunt — 'son of Eleazar son of Aaron the priest' (25:11): priest son of priest, zealot son of zealot, turner-away son of turner-away (the Sifrei 131:3; Sanhedrin 82b:5)", [FX.NONE])
    if q == 'covenant_salt_priesthood':
        move('Menachot 20a:1', "'covenant' at the salt (18:19) and at the priesthood (25:13) — salting indispensable as the priesthood (R. Shimon)"); move('cold_run_korach (CALL)', "the covenant of salt korach's row")
        return out("'covenant' at 18:19 and 25:13 — the salt as indispensable as the priesthood (Menachot 20a; korach's covenant_of_salt row)", [FX.NONE])
    if q == 'twenty_four_gifts':
        move('cold_run_korach (CALL)', 'the twenty-four: %d in the sanctuary, %d at the borders' % (len(KR_24['sanctuary']), len(KR_24['borders']))); move('Sifrei Bamidbar 131:5; Bava Kamma 110b', "the priesthood's twenty-four gifts")
        return out("the twenty-four priestly gifts (the Sifrei 131:5; Bava Kamma 110b) — korach's row CALLED: the priesthood Phinehas's covenant confers", [FX.NONE])
    if q == 'high_priest_count':
        dat('the row high_priest_count = %s against %s' % (data['high_priest_count']['value'], 'more_than_three_hundred'))
        return out("twelve high priests in the first Temple and eighty in the second (the Sifrei 131:4) against Yoma 9a's more than three hundred — the shelf disagreeing with itself, recorded: DISPUTE", [FX.NONE])
    if q == 'atone_tense':
        ink('25:13', "'and he atoned for' — the morphology tags the narrative past; Onkelos a past"); dat('the row atone_tense = %s' % data['atone_tense']['value']); move('Sifrei Bamidbar 131:5; Sanhedrin 82b:6', "'not to atone but and he will atone — he stands and atones until the revival of the dead'")
        return out("'and he atoned' read future by the Sifrei against the morphology's past — the atonement forever (Sanhedrin 82b:6): DISPUTE on the tense of one word", ['atoned_forgiven'])
    if q == 'midian_not_moab':
        ink('25:17', "'harass the Midianites and strike them' — Moab not named"); move('Bava Kamma 38a:16', "Moses' a fortiori from Midian to Moab — Deut 2:9 had to forbid it")
        return out("Midian harassed, Moab spared — Moses' own a fortiori needed Deut 2:9's bar (Bava Kamma 38a); the debit on Israel toward Midian OPEN to 31:7", ['commanded'])
    if q == 'balaam_death':
        dat('the row balaam_death = %s' % data['balaam_death']['value']); ink('31:8', "'Balaam son of Beor they slew with the sword' — the ass's sword-clause (22:29) closed there"); move('Sanhedrin 106a:16-17, 106b:1; Jerusalem Talmud 10:2:18', 'to collect his wages for the 24,000; all four modes (Rav); on their slain four ways')
        return out("Balaam killed by the sword at Midian (31:8) — come for his wages for the twenty-four thousand (Sanhedrin 106a:16); all four court modes in him (Rav, 106b:1)", [FX.NONE])
    if q == 'everlasting_priesthood':
        ink('25:13, Exod 40:15', "'everlasting priesthood' at two seats — the sons' clause narrowed to one son's line"); move('Exod 40:15 by the erection engine (CALL)', "command('everlasting_priesthood') = %s" % ER_PRIESTHOOD)
        return out("'everlasting priesthood' at Exod 40:15 (all Aaron's sons — the erection engine's clause) and 25:13 (Phinehas's line): the clause narrowed", ['invested_office'])
    if q == 'cozbi_and_zur':
        ink('25:15, 25:18, 31:8', "'Cozbi daughter of Zur, head of the peoples' — Zur one of the five kings (Josh 13:21); 'their sister'"); dat('the row cozbi_and_zur = %s' % data['cozbi_and_zur']['value'])
        return out("Cozbi daughter of Zur — Zur one of Midian's five kings killed beside Balaam (31:8): the father dies in the war his daughter's death opens", [FX.NONE])
    if q == 'harass_root':
        ink('25:17-18, 10:9', "'harass... for they harass you' — the trumpets' enemy-word (10:9), Esther's title for Haman the Agagite (3:10); 'their wiles' Joseph's brothers' verb (Gen 37:18)"); ink('24:7', "'higher than Agag' — Haman's ancestor")
        return out("the harass-root (25:17-18) — the trumpets' enemy (10:9) and Haman the Agagite's title in Esther; 24:7's Agag and this command meet in one root", ['commanded'])
    if q == 'rule_installed':
        move('Mishnah Sanhedrin 9:6; Sanhedrin 82a:12', "the halakha (the law) not taught — installed by the deed (25:7-8), ratified by the output (25:10-13)"); ink('25:10-13', "the covenant and the priesthood — the deed's reward, the ink's own output")
        return out("the zealots' rule installed by the deed and ratified by the covenant's speech — rule_installed on the tent (law_balak:zealot), no halt and no docket: THE TENT's form at a second seat", ['rule_installed'])
    if q == 'atoned_forever':
        ink('25:13', "'and he atoned for the children of Israel' — Aaron's verb at 17:12"); move('Sanhedrin 82b:6', 'worthy of atoning forever')
        return out("'and he atoned for the children of Israel' (25:13) — Aaron's incense verb (17:12); the atonement forever (Sanhedrin 82b:6)", ['atoned_forgiven'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_balak(event, world):
    """Num 22:1-25:19 (cold_run_balak.py F1-F5). installed_by boot — the portion's lines are acts, no statute spoken; THE ZEALOTS' RULE is
    installed by the deed (25:7-8) and ratified by the covenant's output (25:10-13): rule_installed on the tent, value law_balak:zealot —
    THE TENT's form at a second seat with no halt and no docket (the zealot asks no court; the law is not taught — Sanhedrin 82a). No timer.
    THREE closes, all the daemon's own: the honor debit at 24:11 (revoked), Zimri's cohabits entry and the plague at 25:8 (the spear). The
    exam's five case kinds dispatch to the cells with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    C_ = lambda ev: {f: ev[f] for f in ('ask', 'arm') if f in ev}
    # ---- chapter 22: the call, the she-ass, the arrival ----
    if k == 'encamped_in_the_plains_of_moab':
        return [E_('encamped_at', 'israel', value='the plains of Moab across the Jordan of Jericho (22:1) — the last camp: nine datelines to 36:13, Moses climbs from them (Deut 34:1)', law='F1 [INK 22:1]')]
    if k == 'moab_feared_and_loathed':
        return [E_('feared', 'the-moabites', cp='israel', value='Moab feared greatly before the people, for it was many (22:3) — the sojourn-verb\'s skin (Gen 20:1)', law='F1 [INK 22:3]'),
                E_('loathed', 'the-moabites', cp='israel', value='Moab loathed the children of Israel (22:3) — the manna\'s verb (21:5)', law='F1 [INK 22:3]')]
    if k == 'balak_sent_for_balaam':
        return [E_('plea_made', 'balak', cp='balaam', value='come, curse this people for me, for it is mightier than I... for I know that whom you bless is blessed and whom you curse is cursed (22:5-6) — the locusts\' clause, the first curse-root', law='F1 [INK 22:5-6; Exod 10:5; Gen 12:3]')]
    if k == 'elders_came_with_divinations':
        return []                                  # the divinations and the lodging the value (22:7-8); Midian's elders gone at 22:8 (Sanhedrin 105a:14)
    if k == 'god_came_to_balaam_first':
        return [E_('cursing_barred', 'balaam', cp='HEAVEN', value='you shall not go with them; you shall not curse the people, for it is blessed (22:12) — HEAVEN\'s block, never closed', law='F1 [INK 22:9-12; Makkot 10b:6]')]
    if k == 'balaam_refused_the_first':
        return [E_('refused', 'balaam', cp='balak', value='the LORD refuses to let me go with you (22:13); Balaam refuses to come with us (22:14) — Pharaoh\'s verb', law='F1 [INK 22:13-14; Exod 7:14; Kiddushin 4a:8]')]
    if k == 'balak_sent_again':
        return [E_('plea_made', 'balak', cp='balaam', value='princes more and weightier: do not be held back from coming to me... come, curse this people for me (22:15-17)', law='F1 [INK 22:15-17]'),
                E_('honor_owed', 'balak', cp='balaam', value='I will surely honor you greatly, and all that you say to me I will do (22:17) — the debit Balak lays on himself; REVOKED at 24:11', law='F1 [INK 22:17; 24:11]')]
    if k == 'balaam_answered_house_of_silver':
        return []                                  # the clause the value (22:18-19): 'if Balak gave me his house full of silver and gold' — 24:13's deltas the cell's
    if k == 'god_came_at_night_go':
        return [E_('bound_to_the_word', 'balaam', cp='HEAVEN', value='rise, go with them; but ONLY (akh) the word that I speak to you, that you shall DO (22:20) — the formula\'s first', law='F1 [INK 22:20; Sanhedrin 105a:15]')]
    if k == 'balaam_saddled_and_went':
        return []                                  # the Akedah's morning the value (22:21 = Gen 22:3; Sanhedrin 105b:11)
    if k == 'angel_stood_as_adversary':
        return [E_('mark_of_anger', 'balaam', cp='HEAVEN', value='God\'s anger burned because he was going (22:22) — the first of three angers; the mark: the adversary in the way', law='F2 [INK 22:22; Zevachim 102a]'),
                E_('adversary_in_the_way', 'balaam', cp='HEAVEN', value='the angel of the LORD stationed himself in the way as an adversary to him (22:22); I have come out as an adversary (22:32)', law='F2 [INK 22:22, 22:32]')]
    if k == 'ass_saw_the_angel_thrice':
        return [E_('beaten', 'the-she-ass', cp='balaam', amount=THREE[0][0], value='the she-ass saw the angel three times and was struck three times — the field, the wall, the crouch (22:23-27); the parser\'s 3 at 22:28', law='F2 [INK 22:23-27, 22:28]')]
    if k == 'mouth_of_the_ass_opened':
        return [E_('mouth_opened', 'the-she-ass', cp='HEAVEN', value='the LORD opened the mouth of the she-ass: what have I done to you that you have struck me these three times? (22:28) — Avot 5:6 created at twilight', law='F2 [INK 22:28-30; Mishnah Avot 5:6]')]
    if k == 'balaams_eyes_uncovered':
        return [E_('eyes_uncovered', 'balaam', cp='HEAVEN', value='the LORD uncovered Balaam\'s eyes and he saw the angel (22:31) — his title at 24:4, 24:16; the plene three at 22:32 read %s' % PLENE, law='F2 [INK 22:31-33]')]
    if k == 'balaam_confessed_and_sent_on':
        return [E_('confessed', 'balaam', value='I have sinned, for I did not know that you stood against me in the way (22:34) — Pharaoh\'s confession', law='F2 [INK 22:34; Exod 9:27]'),
                E_('bound_to_the_word', 'balaam', cp='HEAVEN', value='go with the men, and NOTHING BUT (efes) the word that I speak to you, that you shall SPEAK (22:35) — the formula\'s second', law='F2 [INK 22:35]')]
    if k == 'balak_met_balaam_at_arnon':
        return [E_('sacrifice_offered', 'balak', value='Balak sacrificed oxen and sheep and sent to Balaam and to the princes (22:40) — the portion\'s first offerings', law='F2 [INK 22:40]'),
                E_('bound_to_the_word', 'balaam', cp='HEAVEN', value='the word that God puts in my mouth, that I speak (22:38) — the formula\'s third', law='F2 [INK 22:38]')]
    if k == 'balaam_brought_to_bamoth_baal':
        return []                                  # the first stand the value (22:41 — Bamoth, the well-song's station 21:19)
    # ---- chapters 23-24: the three stands and the four parables ----
    if k == 'seven_altars_built_first':
        return [E_('altars_built', 'balak', amount=SEVENS[0][0], value='build me here seven altars and prepare me here seven bulls and seven rams; and Balak did as Balaam had spoken (23:1-2) — the first stand, Bamoth', law='F3 [INK 23:1-2 — the parser\'s [7, 7, 7]]'),
                E_('offered_burnt_and_sacrifices', 'balak', value='Balak and Balaam offered up a bull and a ram on the altar (23:2) — Onkelos: on every altar', law='F3 [INK 23:2; Zevachim 116a]')]
    if k == 'god_met_balaam_first':
        return [E_('word_put_in_mouth', 'balaam', cp='HEAVEN', value='God met Balaam... and the LORD put a word in Balaam\'s mouth: return to Balak and thus you shall speak (23:4-5)', law='F3 [INK 23:3-6; Deut 18:18; Sanhedrin 105b:16]')]
    if k == 'first_parable_taken_up':
        return [E_('oracle_blessed', 'israel', cp='HEAVEN', value='how shall I curse whom El has not cursed... a people that dwells alone... who has counted the dust of Jacob (23:7-10) — the first parable', law='F3 [INK 23:7-10; Sanhedrin 39b:1; Niddah 31a:20]')]
    if k == 'balak_protested_first':
        return [E_('bound_to_the_word', 'balaam', cp='HEAVEN', value='what the LORD puts in my mouth, that I KEEP to speak (23:12) — the formula\'s fourth', law='F3 [INK 23:11-12]')]
    if k == 'taken_to_pisgah_second_stand':
        return [E_('altars_built', 'balak', amount=SEVENS[2][0], value='the field of Zophim, the top of Pisgah: he built seven altars (23:14) — the second stand, the well-song\'s station 21:20 and Moses\' death-view', law='F3 [INK 23:13-15 — the parser\'s [7]]'),
                E_('offered_burnt_and_sacrifices', 'balak', value='and offered up a bull and a ram on the altar (23:14)', law='F3 [INK 23:14]')]
    if k == 'the_lord_met_balaam_second':
        return [E_('word_put_in_mouth', 'balaam', cp='HEAVEN', value='the LORD met Balaam and put a word in his mouth (23:16) — 23:4 said God', law='F3 [INK 23:16-17]')]
    if k == 'second_parable_taken_up':
        return [E_('oracle_blessed', 'israel', cp='HEAVEN', value='El is not a man that He should lie... to bless I have received; He has blessed, and I cannot turn it back... the shout of a king is among him... no divination in Jacob (23:18-24) — the second parable', law='F3 [INK 23:18-24; 1 Sam 15:29; Rosh Hashanah 32b:15]')]
    if k == 'balak_protested_second':
        return [E_('bound_to_the_word', 'balaam', cp='HEAVEN', value='all that the LORD speaks, that I DO (23:26) — the formula\'s fifth', law='F3 [INK 23:25-26]')]
    if k == 'taken_to_peor_third_stand':
        return [E_('altars_built', 'balak', amount=SEVENS[3][0], value='the top of Peor that looks down on the Jeshimon: build me here seven altars (23:28-29) — the third stand, 21:20\'s clause with Peor for Pisgah: the god of 25:3', law='F3 [INK 23:27-30 — the parser\'s [7, 7, 7]]'),
                E_('offered_burnt_and_sacrifices', 'balak', value='Balak did as Balaam had said and offered up a bull and a ram on the altar (23:30)', law='F3 [INK 23:30]')]
    if k == 'spirit_of_god_upon_balaam':
        return [E_('spirit_rested', 'balaam', cp='HEAVEN', value='he did not go, as time after time, to meet divinations... he saw Israel dwelling by its tribes, and the spirit of God was upon him (24:1-2) — Onkelos: a spirit of prophecy; Bava Batra 60a the tents\' doors', law='F3 [INK 24:1-2; Bava Batra 60a:5]')]
    if k == 'third_parable_taken_up':
        return [E_('oracle_blessed', 'israel', cp='HEAVEN', value='how goodly are your tents, Jacob... his king shall be higher than Agag... he crouched, lay down like a lion — who will rouse him? those who bless you are blessed (24:3-9) — the third parable: Judah\'s blessing and Isaac\'s formula reversed', law='F3 [INK 24:3-9; Gen 49:9, 27:29; Sanhedrin 105b:17-19]')]
    if k == 'balak_clapped_and_dismissed':
        world.close('balak', 'honor_owed', 'Num 24:11 — I said I would surely honor you, and behold, the LORD has held you back from honor: the debit of 22:17 REVOKED in its own words')
        return [E_('mark_of_anger', 'balaam', cp='balak', value='Balak\'s anger burned against Balaam, and he clapped his hands (24:10) — the second anger; the mark: the honor revoked (24:11)', law='F3 [INK 24:10-11; Zevachim 102a]')]
    if k == 'balaam_counselled_balak':
        return [E_('bound_to_the_word', 'balaam', cp='HEAVEN', value='what the LORD speaks, that I speak (24:13) — the formula\'s sixth and last', law='F3 [INK 24:12-13]'),
                E_('counsel_given', 'balak', cp='balaam', value='come, I will counsel you what this people will do to your people in the end of days (24:14) — the fruit at 25:1, named at 31:16', law='F3 [INK 24:14; 31:16; Sifrei Bamidbar 131:1]')]
    if k == 'fourth_parable_taken_up':
        return [E_('oracle_blessed', 'israel', cp='HEAVEN', value='a star steps forth from Jacob and a scepter rises from Israel... Edom a possession... Amalek the first of nations... the Kenite\'s nest in the sela... ships from Kittim (24:15-24) — the fourth parable and the seven small ones', law='F3 [INK 24:15-24; Gen 49:10; Jer 48:45; Dan 11:30]')]
    if k == 'balaam_and_balak_parted':
        return []                                  # the parting the value (24:25); Balaam's death at 31:8 the row balaam_death
    # ---- chapter 25: Peor, the judges, the zealot, the covenant, Midian ----
    if k == 'people_whored_and_bowed_at_shittim':
        return [E_('encamped_at', 'israel', value='Shittim (25:1) — the last camp\'s name (33:49 Abel-shittim); the tabernacle\'s timber', law='F4 [INK 25:1]'),
                E_('whored_after', 'israel', cp='the-moabites', value='the people began to whore after the daughters of Moab (25:1) — Exod 34:16\'s verb; the spec\'s run', law='F4 [INK 25:1; Exod 34:16]'),
                E_('bowed_to_their_gods', 'israel', value='they called the people to the sacrifices of their gods, and the people ate and bowed to their gods (25:2) — the feminine "their gods" at the two seats alone; the erection engine\'s clause: %s' % ER_EAT, law='F4 [INK 25:2; Exod 34:15]')]
    if k == 'israel_yoked_to_baal_peor':
        return [E_('yoked_to_baal_peor', 'israel', value='Israel yoked itself to Baal-peor (25:3) — 19:15\'s lid the noun (Sanhedrin 64a:11)', law='F4 [INK 25:3; 19:15]'),
                E_('mark_of_anger', 'israel', cp='HEAVEN', value='the anger of the LORD burned against Israel (25:3) — the third anger; the mark: the plague', law='F4 [INK 25:3; Zevachim 102a]'),
                E_('plague_struck', 'israel', cp='HEAVEN', value='the_plague_of_peor', law='F4 [INK 25:3, 25:8-9 — the plague OPEN at the anger, CLOSED at 25:8 by the spear with 25:9\'s count in the note; the VALUE names the plague so the close finds THIS entry (O8 S1\'s frogs lesson: the first tape run closed Korach\'s open plague of 17:8-15 instead — that entry law_korach never closed, filed to COMPILE_DEBT); Sanhedrin 82b:3]')]
    if k == 'hanging_commanded':
        return [E_('commanded', 'moses', value='hang_the_heads', law='F4 [INK 25:4 "take all the heads of the people and hang them to the LORD before the sun" — the debit on Moses; the heads as judges by day (Sanhedrin 34b-35a); OPEN forever: the ink narrates no hanging]')]
    if k == 'judges_commanded_to_slay':
        return [E_('commanded', 'the-court', value='slay_the_yoked', law='F4 [INK 25:5 "and Moses said to the judges of Israel: slay each his men who were yoked to Baal-peor" — the debit on the court; the 78,600 by the exodus engine, each two (the Sifrei 131:2); OPEN: the deed at 25:6 interrupts the ink]')]
    if k == 'midianite_brought_near':
        return [E_('cohabits_with_an_aramean', 'zimri', cp='cozbi', value='a man of the children of Israel came and brought near to his brothers the Midianite woman before the eyes of Moses (25:6) — the Mishnah\'s term (Sanhedrin 9:6); a BODY entry OPEN to the spear (retyped from status at the first tape run: a status is never opened and cannot close)', law='F4 [INK 25:6; Mishnah Sanhedrin 9:6; Sanhedrin 82a:12]'),
                E_('wept', 'israel', value='they were weeping at the door of the tent of meeting (25:6) — the Sanhedrin wept, the law eluded Moses (Sanhedrin 82a:12)', law='F4 [INK 25:6]')]
    if k == 'phinehas_pierced_both':
        world.close('zimri', 'cohabits_with_an_aramean', 'Num 25:8 — and pierced both of them: the act ended by the spear (Sanhedrin 82a:10 — during the act only)')
        world.close('israel', 'plague_struck', 'Num 25:8 — and the plague was stayed from the children of Israel: Aaron\'s incense clause (17:13); the dead in the plague %d (25:9, the parser\'s)' % COUNT[0], value='the_plague_of_peor')
        return [E_('slain', 'zimri', cp='pinchas', value='pierced both of them, the man of Israel (25:8) — Zimri son of Salu, prince of a father\'s house of Simeon (25:14): named after the deed', law='F4 [INK 25:7-8, 25:14; Mishnah Sanhedrin 9:6]'),
                E_('slain', 'cozbi', cp='pinchas', value='and the woman through her belly (25:8) — Cozbi daughter of Zur (25:15): the curse-word\'s skin (the alcove, her belly)', law='F4 [INK 25:8, 25:15]')]
    if k == 'plague_dead_counted':
        return []                                  # the count the value (25:9 — the closed plague entry carries it; Simeon's fall the checkpoint at 26:14)
    if k == 'covenant_of_peace_given':
        return [E_('covenant_of_peace', 'pinchas', cp='HEAVEN', value='behold, I give him My covenant of peace (25:12) — in force forever; Sanhedrin 82b:6', law='F5 [INK 25:12; Mal 2:5]'),
                E_('invested_office', 'pinchas', value='a covenant of everlasting priesthood (25:13) — the priesthood by the deed (Zevachim 101b): the addressees row\'s named exception (%s)' % PR_ADDRESSEES['sons_of_aaron'], law='F5 [INK 25:13; Exod 40:15; Zevachim 101b:10]'),
                E_('atoned_forgiven', 'israel', cp='HEAVEN', value='and he atoned for the children of Israel (25:13) — Aaron\'s verb (17:12); the Sifrei\'s future, the tag\'s past', law='F5 [INK 25:13; Sifrei Bamidbar 131:5]'),
                E_('rule_installed', 'the-tabernacle', value='law_balak:zealot', law='F5 [INK 25:10-13 — THE ZEALOTS\' RULE INSTALLED BY THE DEED (25:7-8) and ratified by this output: "one who cohabits with an Aramean woman, zealots strike him" (Mishnah Sanhedrin 9:6 — the rule\'s text TEST DATA; the ink\'s own output the reward); not taught (Sanhedrin 82a); THE TENT\'s form at a second seat — no halt, no docket]')]
    if k == 'midian_harassment_commanded':
        return [E_('commanded', 'israel', cp='the-midianites', value='harass_the_midianites', law='F5 [INK 25:16-18 "harass the Midianites and strike them, for they harass you with their wiles" — the debit on Israel; OPEN to 31:7 (Matot); Moab spared (Bava Kamma 38a)]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'call_case':
        v, e, _ = the_call(C_(event), DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'refused': E_('refused', s_, value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L),
             'cursing_barred': E_('cursing_barred', s_, cp='HEAVEN', value=v, law=L), 'bound_to_the_word': E_('bound_to_the_word', s_, cp='HEAVEN', value=v, law=L), 'honor_owed': E_('honor_owed', s_, value=v, law=L), 'encamped_at': E_('encamped_at', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'ass_case':
        v, e, _ = the_ass_and_the_angel(C_(event), DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'beaten': E_('beaten', s_, amount=THREE[0][0], value=v, law=L), 'mouth_opened': E_('mouth_opened', s_, cp='HEAVEN', value=v, law=L),
             'eyes_uncovered': E_('eyes_uncovered', s_, cp='HEAVEN', value=v, law=L), 'confessed': E_('confessed', s_, value=v, law=L), 'adversary_in_the_way': E_('adversary_in_the_way', s_, cp='HEAVEN', value=v, law=L), 'mark_of_anger': E_('mark_of_anger', s_, cp='HEAVEN', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'stands_case':
        v, e, _ = the_stands(C_(event), DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'altars_built': E_('altars_built', s_, amount=SEVENS[0][0], value=v, law=L), 'offered_burnt_and_sacrifices': E_('offered_burnt_and_sacrifices', s_, value=v, law=L),
             'word_put_in_mouth': E_('word_put_in_mouth', s_, cp='HEAVEN', value=v, law=L), 'oracle_blessed': E_('oracle_blessed', s_, cp='HEAVEN', value=v, law=L), 'spirit_rested': E_('spirit_rested', s_, cp='HEAVEN', value=v, law=L), 'counsel_given': E_('counsel_given', s_, value=v, law=L), 'mark_of_anger': E_('mark_of_anger', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'peor_case':
        v, e, _ = peor(C_(event), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'stoned': E_('stoned', s_, value=v, law=L), 'whored_after': E_('whored_after', s_, value=v, law=L), 'bowed_to_their_gods': E_('bowed_to_their_gods', s_, value=v, law=L),
             'yoked_to_baal_peor': E_('yoked_to_baal_peor', s_, value=v, law=L), 'plague_struck': E_('plague_struck', s_, cp='HEAVEN', value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'cohabits_with_an_aramean': E_('cohabits_with_an_aramean', s_, value=v, law=L),
             'slain': E_('slain', s_, cp='pinchas', value=v, law=L), 'wept': E_('wept', s_, value=v, law=L), 'mark_of_anger': E_('mark_of_anger', s_, cp='HEAVEN', value=v, law=L), 'encamped_at': E_('encamped_at', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'phinehas_case':
        v, e, _ = phinehas_and_midian(C_(event), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'covenant_of_peace': E_('covenant_of_peace', s_, cp='HEAVEN', value=v, law=L),
             'invested_office': E_('invested_office', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, cp='HEAVEN', value=v, law=L), 'rule_installed': E_('rule_installed', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the seer bound to the word, the barred curser, the beaten ass and
    its opened mouth, the builder of the altars, the blessed people, the counselled king, the whorer at Shittim, the yoked, the hanged-by-court,
    the judge, Zimri in the act, the zealot's blessed priest, the disqualified blemished priest, the harassed Midian. No timer: the stretch is undated."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 22-25: Mishnah Sanhedrin 7:6, 9:6, 10:2, Avot 5:6, 5:19 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_balak]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        w.submit({'kind': 'call_case', 'subject': 'the-seer', 'person': 'the-seer', 'ask': 'word_formula', 'case_source': 'Num 22:20, 22:35, 22:38, 23:12, 23:26, 24:13 — the formula\'s six seats'})
        w.submit({'kind': 'call_case', 'subject': 'the-barred-curser', 'person': 'the-barred-curser', 'ask': 'cursing_barred', 'case_source': 'Makkot 10b:6; Num 22:12 — you shall not curse the people'})
        w.submit({'kind': 'call_case', 'subject': 'the-refuser', 'person': 'the-refuser', 'ask': 'refuses_spelling', 'case_source': 'Kiddushin 4a:8; Num 22:13-14 — Balaam refuses'})
        w.submit({'kind': 'call_case', 'subject': 'the-honored', 'person': 'the-honored', 'ask': 'embassies', 'case_source': 'Num 22:5-6, 22:15-17 — the two embassies and the honor'})
        w.submit({'kind': 'ass_case', 'subject': 'the-beaten-ass', 'person': 'the-beaten-ass', 'ask': 'three_strikes', 'case_source': 'Num 22:23-28 — struck three times'})
        w.submit({'kind': 'ass_case', 'subject': 'the-opened-mouth', 'person': 'the-opened-mouth', 'ask': 'mouth_of_the_ass', 'case_source': 'Mishnah Avot 5:6; Num 22:28 — created at twilight'})
        w.submit({'kind': 'ass_case', 'subject': 'the-uncovered-eyes', 'person': 'the-uncovered-eyes', 'ask': 'eyes_uncovered', 'case_source': 'Num 22:31 — the LORD uncovered his eyes'})
        w.submit({'kind': 'ass_case', 'subject': 'the-confessor', 'person': 'the-confessor', 'ask': 'confession', 'case_source': 'Num 22:34 — I have sinned'})
        w.submit({'kind': 'ass_case', 'subject': 'the-adversary-met', 'person': 'the-adversary-met', 'ask': 'adversary', 'case_source': 'Num 22:22, 22:32 — as an adversary'})
        w.submit({'kind': 'stands_case', 'subject': 'the-altar-builder', 'person': 'the-altar-builder', 'ask': 'forty_two_offerings', 'case_source': 'Sanhedrin 105b:12; Nazir 23b:4; Num 23:1-2 — seven altars three times'})
        w.submit({'kind': 'stands_case', 'subject': 'the-blessed-people', 'person': 'the-blessed-people', 'ask': 'curses_turned', 'case_source': 'Sanhedrin 105b:17-19; Num 24:5-7 — the curses turned'})
        w.submit({'kind': 'stands_case', 'subject': 'the-mouth-with-the-word', 'person': 'the-mouth-with-the-word', 'ask': 'word_in_mouth_mode', 'case_source': 'Sanhedrin 105b:16; Num 23:5 — an angel or a hook'})
        w.submit({'kind': 'stands_case', 'subject': 'the-tents-seen', 'person': 'the-tents-seen', 'ask': 'tents_doors', 'case_source': 'Bava Batra 60a:5; Num 24:2 — dwelling by its tribes'})
        w.submit({'kind': 'stands_case', 'subject': 'the-counselled-king', 'person': 'the-counselled-king', 'ask': 'counsel', 'case_source': 'Sifrei Bamidbar 131:1; Num 24:14, 31:16 — the counsel'})
        w.submit({'kind': 'peor_case', 'subject': 'the-whorer-at-shittim', 'person': 'the-whorer-at-shittim', 'ask': 'spec_run', 'case_source': 'Exod 34:15-16 by the erection engine; Num 25:1-2 — the spec\'s run'})
        w.submit({'kind': 'peor_case', 'subject': 'the-barer-to-peor', 'person': 'the-barer-to-peor', 'ask': 'peor_service', 'case_source': 'Mishnah Sanhedrin 7:6; Num 25:3 — baring is its worship'})
        w.submit({'kind': 'peor_case', 'subject': 'the-yoked', 'person': 'the-yoked', 'ask': 'yoked_like_the_lid', 'case_source': 'Sanhedrin 64a:11; Num 25:3, 19:15 — like a cord-bound lid'})
        w.submit({'kind': 'peor_case', 'subject': 'the-heads-to-hang', 'person': 'the-heads-to-hang', 'ask': 'hang_before_the_sun', 'case_source': 'Sanhedrin 35a:2; Num 25:4 — hang them before the sun'})
        w.submit({'kind': 'peor_case', 'subject': 'the-judges', 'person': 'the-judges', 'ask': 'judges_count', 'case_source': 'Jerusalem Talmud Sanhedrin 10:2:17; Exod 18:21 by the exodus engine; Num 25:5 — 78,600 each two'})
        w.submit({'kind': 'peor_case', 'subject': 'zimri-in-the-act', 'person': 'zimri-in-the-act', 'ask': 'zealot_rule', 'arm': 'in_the_act', 'case_source': 'Mishnah Sanhedrin 9:6; Sanhedrin 82a:10; Num 25:6-8 — zealots strike him'})
        w.submit({'kind': 'peor_case', 'subject': 'zimri-separated', 'person': 'zimri-separated', 'ask': 'zealot_rule', 'arm': 'separated', 'case_source': 'Sanhedrin 82a:10 — separated, the zealot is a murderer'})
        w.submit({'kind': 'peor_case', 'subject': 'the-plague-stayed', 'person': 'the-plague-stayed', 'ask': 'cast_before_god', 'case_source': 'Sanhedrin 82b:3; Num 25:8-9 — shall twenty-four thousand fall'})
        w.submit({'kind': 'peor_case', 'subject': 'the-weeping-court', 'person': 'the-weeping-court', 'ask': 'halakha_forgotten', 'case_source': 'Sanhedrin 82a:12; Num 25:6 — the law eluded Moses'})
        w.submit({'kind': 'phinehas_case', 'subject': 'the-zealous-priest', 'person': 'the-zealous-priest', 'ask': 'priesthood_by_the_deed', 'case_source': 'Zevachim 101b:10; Num 25:13 — not a priest until he killed Zimri'})
        w.submit({'kind': 'phinehas_case', 'subject': 'the-covenanted', 'person': 'the-covenanted', 'ask': 'covenant_of_peace', 'case_source': 'Sanhedrin 82b:6; Num 25:12 — My covenant of peace'})
        w.submit({'kind': 'phinehas_case', 'subject': 'the-blemished-priest', 'person': 'the-blemished-priest', 'ask': 'blemished_service', 'case_source': 'Kiddushin 66b:13; Num 25:12 — peace read whole'})
        w.submit({'kind': 'phinehas_case', 'subject': 'the-unfit-seed', 'person': 'the-unfit-seed', 'ask': 'unfit_seed_service', 'case_source': 'Kiddushin 66b:10; Num 25:13 — his seed after him'})
        w.submit({'kind': 'phinehas_case', 'subject': 'the-atoner', 'person': 'the-atoner', 'ask': 'atone_tense', 'case_source': 'Sifrei Bamidbar 131:5; Num 25:13 — and he will atone'})
        w.submit({'kind': 'phinehas_case', 'subject': 'the-rule-on-the-tent', 'person': 'the-rule-on-the-tent', 'ask': 'rule_installed', 'case_source': 'Mishnah Sanhedrin 9:6; Sanhedrin 82a:12; Num 25:10-13 — the zealots\' rule installed by the deed'})
        w.submit({'kind': 'phinehas_case', 'subject': 'the-harassed-midian', 'person': 'the-harassed-midian', 'ask': 'midian_not_moab', 'case_source': 'Bava Kamma 38a:16; Num 25:17 — harass the Midianites'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    L = lambda kk: len([l for l in w.log if l[0] == kk])
    return (n('the-seer', 'bound_to_the_word'), n('the-barred-curser', 'cursing_barred'), n('the-refuser', 'refused'), n('the-honored', 'plea_made'), n('the-honored', 'honor_owed'),
            n('the-beaten-ass', 'beaten'), n('the-opened-mouth', 'mouth_opened'), n('the-uncovered-eyes', 'eyes_uncovered'), n('the-confessor', 'confessed'), n('the-adversary-met', 'adversary_in_the_way'), n('the-adversary-met', 'mark_of_anger'),
            n('the-altar-builder', 'altars_built'), n('the-altar-builder', 'offered_burnt_and_sacrifices'), n('the-blessed-people', 'oracle_blessed'), n('the-mouth-with-the-word', 'word_put_in_mouth'), n('the-tents-seen', 'spirit_rested'), n('the-counselled-king', 'counsel_given'),
            n('the-whorer-at-shittim', 'whored_after'), n('the-whorer-at-shittim', 'bowed_to_their_gods'), n('the-barer-to-peor', 'stoned'), n('the-yoked', 'yoked_to_baal_peor'), n('the-heads-to-hang', 'commanded'), n('the-judges', 'commanded'),
            n('zimri-in-the-act', 'cohabits_with_an_aramean'), n('zimri-in-the-act', 'slain'), n('zimri-separated', 'exempt'), n('the-plague-stayed', 'plague_struck'), n('the-plague-stayed', 'slain'), n('the-weeping-court', 'wept'),
            n('the-zealous-priest', 'invested_office'), n('the-covenanted', 'covenant_of_peace'), n('the-blemished-priest', 'disqualified'), n('the-unfit-seed', 'accepted'), n('the-atoner', 'atoned_forgiven'), n('the-rule-on-the-tent', 'rule_installed'), n('the-harassed-midian', 'commanded'),
            L('TIMER-SET'), L('TIMER-FIRE'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1,
                   0, 0, 30)   # PREDICTED from the design BEFORE the first run: one effect per declared row — thirty-six ledger counts of one; NO timer (the stretch undated); thirty entities (the subjects; HEAVEN, Balaam, Balak, Phinehas and the Midianites counterparties, not entities until written on)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the Balak scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 7b (2026-09-11; NUMBERS_WALK.md "Sitting 7b"): the portion's own acts AS HISTORY — the forty-one lines of Num 22:1-25:18 in
    the text's order on a world with this runner's daemon, at the counter Chukat left, (40, 6, 1): no marker in the stretch (undated in the ink
    and on the shelf), no timer. Not a graded cell: the tuple below is a tripwire PREDICTED before the first run; the sequence world's RUN
    tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 22-25: Balak on the tape — the call, the she-ass, the stands, Peor, Phinehas, Midian (the exodus epoch)', epoch='exodus')
        w.laws = [law_balak]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        w.submit({'kind': 'encamped_in_the_plains_of_moab', 'subject': 'israel', 'at': 'the plains of Moab across the Jordan of Jericho', 'case_source': 'Num 22:1 — and the children of Israel journeyed and camped in the plains of Moab across the Jordan of Jericho'})
        w.submit({'kind': 'moab_feared_and_loathed', 'subject': 'the-moabites', 'saw': 'all that Israel had done to the Amorite', 'feared': True, 'said_to': 'the elders of Midian', 'case_source': 'Num 22:2-4 — and Balak son of Zippor saw all that Israel had done to the Amorite; and Moab feared greatly before the people, for it was many; and Moab loathed the children of Israel; and Moab said to the elders of Midian: now the assembly will lick up all our surroundings as the ox licks the green of the field'})
        w.submit({'kind': 'balak_sent_for_balaam', 'subject': 'balak', 'to': 'Balaam son of Beor at Pethor', 'words': 'come, curse this people for me', 'case_source': 'Num 22:5-6 — and he sent messengers to Balaam son of Beor, to Pethor which is by the river of the land of the sons of his people, to call him, saying: behold, a people has come out of Egypt; behold, it has covered the eye of the land, and it dwells opposite me; and now come, curse this people for me, for it is mightier than I; perhaps I will be able to strike it and drive it from the land, for I know that whom you bless is blessed and whom you curse is cursed'})
        w.submit({'kind': 'elders_came_with_divinations', 'subject': 'balak', 'divinations': True, 'lodged': 'the princes of Moab', 'case_source': "Num 22:7-8 — and the elders of Moab and the elders of Midian went with divinations in their hand, and they came to Balaam and spoke to him Balak's words; and he said to them: lodge here the night, and I will bring you back word as the LORD speaks to me; and the princes of Moab stayed with Balaam"})
        w.submit({'kind': 'god_came_to_balaam_first', 'subject': 'balaam', 'words': 'who are these men with you', 'verdict': 'you shall not go with them; you shall not curse the people, for it is blessed', 'case_source': 'Num 22:9-12 — and God came to Balaam and said: who are these men with you? and Balaam said to God: Balak son of Zippor, king of Moab, sent to me: behold, the people that has come out of Egypt has covered the eye of the land; now come, curse it for me; perhaps I will be able to fight against it and drive it out; and God said to Balaam: you shall not go with them; you shall not curse the people, for it is blessed'})
        w.submit({'kind': 'balaam_refused_the_first', 'subject': 'balaam', 'words': 'the LORD refuses to let me go with you', 'case_source': "Num 22:13-14 — and Balaam rose in the morning and said to Balak's princes: go to your land, for the LORD refuses to let me go with you; and the princes of Moab rose and came to Balak and said: Balaam refuses to come with us"})
        w.submit({'kind': 'balak_sent_again', 'subject': 'balak', 'words': 'do not be held back from coming to me', 'honor': 'I will surely honor you greatly', 'case_source': 'Num 22:15-17 — and Balak sent yet again princes, more and weightier than these; and they came to Balaam and said to him: thus says Balak son of Zippor: do not be held back from coming to me, for I will surely honor you greatly, and all that you say to me I will do; and come, curse this people for me'})
        w.submit({'kind': 'balaam_answered_house_of_silver', 'subject': 'balaam', 'words': 'if Balak gave me his house full of silver and gold I could not pass over the mouth of the LORD my God', 'case_source': "Num 22:18-19 — and Balaam answered and said to Balak's servants: if Balak gave me his house full of silver and gold I could not pass over the mouth of the LORD my God to do small or great; and now, stay here you too the night, that I may know what the LORD will add to speak to me"})
        w.submit({'kind': 'god_came_at_night_go', 'subject': 'balaam', 'words': 'rise, go with them', 'restrictor': 'only the word that I speak to you, that you shall do', 'case_source': 'Num 22:20 — and God came to Balaam at night and said to him: if the men have come to call you, rise, go with them; but only the word that I speak to you, that you shall do'})
        w.submit({'kind': 'balaam_saddled_and_went', 'subject': 'balaam', 'saddled': 'his she-ass', 'with': 'the princes of Moab', 'case_source': 'Num 22:21 — and Balaam rose in the morning and saddled his she-ass and went with the princes of Moab'})
        w.submit({'kind': 'angel_stood_as_adversary', 'subject': 'balaam', 'anger': "God's anger burned because he was going", 'adversary': 'the angel of the LORD in the way', 'case_source': "Num 22:22 — and God's anger burned because he was going, and the angel of the LORD stationed himself in the way as an adversary to him; and he was riding on his she-ass and his two young men with him"})
        w.submit({'kind': 'ass_saw_the_angel_thrice', 'subject': 'the-she-ass', 'saw': 'the angel of the LORD with his sword drawn', 'struck': True, 'times': 3, 'case_source': "Num 22:23-27 — and the she-ass saw the angel of the LORD standing in the way with his sword drawn in his hand, and she turned from the way and went into the field; and Balaam struck the she-ass to turn her to the way; and the angel of the LORD stood in a path of the vineyards, a fence on this side and a fence on that; and the she-ass saw the angel of the LORD and pressed against the wall and pressed Balaam's foot to the wall, and he struck her again; and the angel of the LORD went further and stood in a narrow place where there was no way to turn right or left; and the she-ass saw the angel of the LORD and crouched under Balaam, and Balaam's anger burned and he struck the she-ass with the staff"})
        w.submit({'kind': 'mouth_of_the_ass_opened', 'subject': 'the-she-ass', 'words': 'what have I done to you that you have struck me these three times', 'answer': 'because you have made sport of me; would there were a sword in my hand', 'case_source': 'Num 22:28-30 — and the LORD opened the mouth of the she-ass, and she said to Balaam: what have I done to you that you have struck me these three times? and Balaam said to the she-ass: because you have made sport of me; would there were a sword in my hand, for now I would kill you; and the she-ass said to Balaam: am I not your she-ass on which you have ridden from your existence until this day? was I ever accustomed to do so to you? and he said: no'})
        w.submit({'kind': 'balaams_eyes_uncovered', 'subject': 'balaam', 'saw': 'the angel of the LORD standing in the way with his sword drawn', 'words': 'why have you struck your she-ass these three times', 'case_source': "Num 22:31-33 — and the LORD uncovered Balaam's eyes and he saw the angel of the LORD standing in the way with his sword drawn in his hand, and he bowed and prostrated himself to his face; and the angel of the LORD said to him: why have you struck your she-ass these three times? behold, I have come out as an adversary, for the way is contrary before me; and the she-ass saw me and turned from before me these three times; had she not turned from before me, now I would have killed you and let her live"})
        w.submit({'kind': 'balaam_confessed_and_sent_on', 'subject': 'balaam', 'confession': 'I have sinned', 'words': 'go with the men, and nothing but the word that I speak to you, that you shall speak', 'restrictor': 'nothing but', 'case_source': "Num 22:34-35 — and Balaam said to the angel of the LORD: I have sinned, for I did not know that you stood against me in the way; and now, if it is evil in your eyes I will return; and the angel of the LORD said to Balaam: go with the men, and nothing but the word that I speak to you, that you shall speak; and Balaam went with Balak's princes"})
        w.submit({'kind': 'balak_met_balaam_at_arnon', 'subject': 'balak', 'at': 'the city of Moab on the border of the Arnon', 'words': 'the word that God puts in my mouth, that I speak', 'sacrificed': 'oxen and sheep', 'case_source': 'Num 22:36-40 — and Balak heard that Balaam had come, and he went out to meet him to the city of Moab which is on the border of the Arnon at the edge of the border; and Balak said to Balaam: did I not surely send to you to call you? why did you not come to me? am I truly not able to honor you? and Balaam said to Balak: behold, I have come to you; now, am I at all able to speak anything? the word that God puts in my mouth, that I speak; and Balaam went with Balak and they came to Kiriath-huzoth; and Balak sacrificed oxen and sheep and sent to Balaam and to the princes with him'})
        w.submit({'kind': 'balaam_brought_to_bamoth_baal', 'subject': 'balak', 'stand': 'Bamoth-baal', 'saw': 'the edge of the people', 'case_source': 'Num 22:41 — and it was in the morning, and Balak took Balaam and brought him up to Bamoth-baal, and he saw from there the edge of the people'})
        w.submit({'kind': 'seven_altars_built_first', 'subject': 'balak', 'altars': 7, 'beasts': 'seven bulls and seven rams', 'case_source': 'Num 23:1-2 — and Balaam said to Balak: build me here seven altars and prepare me here seven bulls and seven rams; and Balak did as Balaam had spoken, and Balak and Balaam offered up a bull and a ram on the altar'})
        w.submit({'kind': 'god_met_balaam_first', 'subject': 'balaam', 'met': 'God met Balaam', 'word': 'return to Balak and thus you shall speak', 'case_source': "Num 23:3-6 — and Balaam said to Balak: stand by your burnt offering and I will go; perhaps the LORD will chance to meet me, and whatever He shows me I will tell you; and he went to a bare height; and God met Balaam, and he said to Him: the seven altars I have arranged and I have offered up a bull and a ram on the altar; and the LORD put a word in Balaam's mouth and said: return to Balak and thus you shall speak; and he returned to him, and behold, he was standing by his burnt offering, he and all the princes of Moab"})
        w.submit({'kind': 'first_parable_taken_up', 'subject': 'israel', 'parable': 1, 'clauses': ['from Aram Balak led me', 'how shall I curse whom El has not cursed', 'a people that dwells alone', 'who has counted the dust of Jacob', 'let me die the death of the upright'], 'case_source': 'Num 23:7-10 — and he took up his parable and said: from Aram Balak led me, the king of Moab from the mountains of the east: come, curse Jacob for me, and come, denounce Israel; how shall I curse whom El has not cursed, and how shall I denounce whom the LORD has not denounced? for from the top of the rocks I see it and from the hills I behold it: behold, a people that dwells alone and is not reckoned among the nations; who has counted the dust of Jacob or numbered the fourth part of Israel? let my soul die the death of the upright, and let my end be like his'})
        w.submit({'kind': 'balak_protested_first', 'subject': 'balak', 'words': 'what have you done to me? to curse my enemies I took you, and behold, you have surely blessed', 'answer': 'what the LORD puts in my mouth, that I keep to speak', 'case_source': 'Num 23:11-12 — and Balak said to Balaam: what have you done to me? to curse my enemies I took you, and behold, you have surely blessed; and he answered and said: what the LORD puts in my mouth, that I keep to speak'})
        w.submit({'kind': 'taken_to_pisgah_second_stand', 'subject': 'balak', 'stand': 'the field of Zophim, the top of Pisgah', 'altars': 7, 'case_source': 'Num 23:13-15 — and Balak said to him: come with me to another place from where you will see it; only its edge you will see, all of it you will not see, and curse it for me from there; and he took him to the field of Zophim, to the top of Pisgah, and he built seven altars and offered up a bull and a ram on the altar; and he said to Balak: stand here by your burnt offering, and I will be met there'})
        w.submit({'kind': 'the_lord_met_balaam_second', 'subject': 'balaam', 'met': 'the LORD met Balaam', 'word': 'return to Balak and thus you shall speak', 'case_source': 'Num 23:16-17 — and the LORD met Balaam and put a word in his mouth and said: return to Balak and thus you shall speak; and he came to him, and behold, he was standing by his burnt offering and the princes of Moab with him; and Balak said to him: what has the LORD spoken?'})
        w.submit({'kind': 'second_parable_taken_up', 'subject': 'israel', 'parable': 2, 'clauses': ['El is not a man that He should lie', 'to bless I have received', 'the shout of a king is among him', 'El brings them out of Egypt', 'no divination in Jacob', 'a people rises like a lioness'], 'case_source': 'Num 23:18-24 — and he took up his parable and said: rise, Balak, and hear; give ear to me, son of Zippor: El is not a man that He should lie, nor a son of man that He should repent; has He said and will He not do it, or spoken and will He not make it good? behold, to bless I have received; He has blessed, and I cannot turn it back; He has not beheld iniquity in Jacob nor seen toil in Israel; the LORD his God is with him, and the shout of a king is among him; El brings them out of Egypt, like the horns of the wild ox to Him; for there is no divination in Jacob and no sorcery in Israel; at this time it shall be said to Jacob and to Israel what El has wrought; behold, a people rises like a lioness and lifts itself like a lion; it shall not lie down until it eats prey and drinks the blood of the slain'})
        w.submit({'kind': 'balak_protested_second', 'subject': 'balak', 'words': 'neither curse him at all nor bless him at all', 'answer': 'all that the LORD speaks, that I do', 'case_source': 'Num 23:25-26 — and Balak said to Balaam: neither curse him at all nor bless him at all; and Balaam answered and said to Balak: did I not speak to you, saying: all that the LORD speaks, that I do?'})
        w.submit({'kind': 'taken_to_peor_third_stand', 'subject': 'balak', 'stand': 'the top of Peor that looks down on the Jeshimon', 'altars': 7, 'case_source': 'Num 23:27-30 — and Balak said to Balaam: come, I will take you to another place; perhaps it will be right in the eyes of God that you curse it for me from there; and Balak took Balaam to the top of Peor that looks down on the Jeshimon; and Balaam said to Balak: build me here seven altars and prepare me here seven bulls and seven rams; and Balak did as Balaam had said and offered up a bull and a ram on the altar'})
        w.submit({'kind': 'spirit_of_god_upon_balaam', 'subject': 'balaam', 'saw': 'Israel dwelling by its tribes', 'spirit': 'the spirit of God was upon him', 'case_source': 'Num 24:1-2 — and Balaam saw that it was good in the eyes of the LORD to bless Israel, and he did not go, as time after time, to meet divinations, and he set his face toward the wilderness; and Balaam lifted his eyes and saw Israel dwelling by its tribes, and the spirit of God was upon him'})
        w.submit({'kind': 'third_parable_taken_up', 'subject': 'israel', 'parable': 3, 'clauses': ['the utterance of the man of the opened eye', 'how goodly are your tents, Jacob', 'his king shall be higher than Agag', 'El brings him out of Egypt', 'he crouched, lay down like a lion', 'those who bless you are blessed'], 'case_source': 'Num 24:3-9 — and he took up his parable and said: the utterance of Balaam son of Beor, and the utterance of the man of the opened eye; the utterance of him who hears the words of El, who sees the vision of Shaddai, fallen, and with uncovered eyes: how goodly are your tents, Jacob, your dwellings, Israel; like streams stretched out, like gardens by the river, like aloes the LORD planted, like cedars by the waters; water flows from his buckets and his seed is in many waters, and his king shall be higher than Agag, and his kingdom exalted; El brings him out of Egypt, like the horns of the wild ox to Him; he devours the nations his adversaries and crushes their bones, and his arrows pierce; he crouched, lay down like a lion and like a lioness — who will rouse him? those who bless you are blessed, and those who curse you are cursed'})
        w.submit({'kind': 'balak_clapped_and_dismissed', 'subject': 'balak', 'anger': "Balak's anger burned against Balaam", 'times': 3, 'honor': 'the LORD has held you back from honor', 'case_source': "Num 24:10-11 — and Balak's anger burned against Balaam, and he clapped his hands; and Balak said to Balaam: to curse my enemies I called you, and behold, you have surely blessed these three times; and now, flee to your place; I said I would surely honor you, and behold, the LORD has held you back from honor"})
        w.submit({'kind': 'balaam_counselled_balak', 'subject': 'balaam', 'words': 'what the LORD speaks, that I speak', 'counsel': 'come, I will counsel you what this people will do to your people in the end of days', 'case_source': 'Num 24:12-14 — and Balaam said to Balak: did I not speak also to your messengers whom you sent to me, saying: if Balak gave me his house full of silver and gold, I cannot pass over the mouth of the LORD to do good or bad from my own heart; what the LORD speaks, that I speak; and now, behold, I am going to my people; come, I will counsel you what this people will do to your people in the end of days'})
        w.submit({'kind': 'fourth_parable_taken_up', 'subject': 'israel', 'parable': 4, 'clauses': ['a star steps forth from Jacob', 'a scepter rises from Israel', 'Edom shall be a possession', 'Amalek the first of nations', "the Kenite's nest in the sela", 'ships from Kittim'], 'case_source': 'Num 24:15-24 — and he took up his parable and said: the utterance of Balaam son of Beor, and the utterance of the man of the opened eye; the utterance of him who hears the words of El and knows the knowledge of the Most High, who sees the vision of Shaddai, fallen, and with uncovered eyes: I see it, but not now; I behold it, but not near: a star steps forth from Jacob and a scepter rises from Israel, and crushes the corners of Moab and breaks down all the sons of Sheth; and Edom shall be a possession, and Seir a possession of his enemies, and Israel does valiantly; and one from Jacob shall rule and destroy the survivor from the city; and he saw Amalek and took up his parable and said: Amalek was the first of nations, and his end is destruction; and he saw the Kenite and took up his parable and said: firm is your dwelling, and your nest set in the sela; yet Kayin shall be for wasting — how long until Asshur takes you captive; and he took up his parable and said: alas, who shall live when El appoints this? and ships from the hand of Kittim afflict Asshur and afflict Eber, and he too is to destruction'})
        w.submit({'kind': 'balaam_and_balak_parted', 'subject': 'balaam', 'returned': 'to his place', 'case_source': 'Num 24:25 — and Balaam rose and went and returned to his place, and Balak too went his way'})
        w.submit({'kind': 'people_whored_and_bowed_at_shittim', 'subject': 'israel', 'at': 'Shittim', 'whored': 'after the daughters of Moab', 'bowed': 'to their gods', 'case_source': 'Num 25:1-2 — and Israel dwelt in Shittim, and the people began to whore after the daughters of Moab; and they called the people to the sacrifices of their gods, and the people ate and bowed to their gods'})
        w.submit({'kind': 'israel_yoked_to_baal_peor', 'subject': 'israel', 'yoked': 'to Baal-peor', 'anger': 'the anger of the LORD burned against Israel', 'case_source': 'Num 25:3 — and Israel yoked itself to Baal-peor, and the anger of the LORD burned against Israel'})
        w.submit({'kind': 'hanging_commanded', 'subject': 'moses', 'words': 'take all the heads of the people and hang them to the LORD before the sun', 'command': 'hang_the_heads', 'case_source': 'Num 25:4 — and the LORD said to Moses: take all the heads of the people and hang them to the LORD before the sun, and the burning anger of the LORD will turn back from Israel'})
        w.submit({'kind': 'judges_commanded_to_slay', 'subject': 'the-court', 'words': 'slay each his men who were yoked to Baal-peor', 'command': 'slay_the_yoked', 'case_source': 'Num 25:5 — and Moses said to the judges of Israel: slay each his men who were yoked to Baal-peor'})
        w.submit({'kind': 'midianite_brought_near', 'subject': 'zimri', 'brought_near': 'the Midianite woman', 'before': 'the eyes of Moses and of the whole congregation', 'weeping': 'at the door of the tent of meeting', 'case_source': 'Num 25:6 — and behold, a man of the children of Israel came and brought near to his brothers the Midianite woman before the eyes of Moses and before the eyes of the whole congregation of the children of Israel, and they were weeping at the door of the tent of meeting'})
        w.submit({'kind': 'phinehas_pierced_both', 'subject': 'pinchas', 'saw': True, 'spear': 'a spear in his hand', 'pierced': 'both of them', 'names': ['Zimri son of Salu', 'Cozbi daughter of Zur'], 'case_source': "Num 25:7-8 — and Phinehas son of Eleazar son of Aaron the priest saw, and he rose from the midst of the congregation and took a spear in his hand; and he went after the man of Israel into the alcove and pierced both of them, the man of Israel and the woman through her belly, and the plague was stayed from the children of Israel (25:14-15: and the name of the slain man of Israel was Zimri son of Salu, prince of a father's house of the Simeonites; and the name of the slain Midianite woman was Cozbi daughter of Zur)"})
        w.submit({'kind': 'plague_dead_counted', 'subject': 'israel', 'dead': 24000, 'case_source': 'Num 25:9 — and the dead in the plague were twenty and four thousand'})
        w.submit({'kind': 'covenant_of_peace_given', 'subject': 'pinchas', 'words': 'behold, I give him My covenant of peace', 'covenant': 'a covenant of everlasting priesthood', 'installs': 'law_balak:zealot', 'case_source': 'Num 25:10-13 — and the LORD spoke to Moses saying: Phinehas son of Eleazar son of Aaron the priest has turned back My wrath from the children of Israel in his being zealous with My zeal among them, so that I did not consume the children of Israel in My zeal; therefore say: behold, I give him My covenant of peace; and it shall be for him and for his seed after him a covenant of everlasting priesthood, because he was zealous for his God and he atoned for the children of Israel'})
        w.submit({'kind': 'midian_harassment_commanded', 'subject': 'israel', 'words': 'harass the Midianites and strike them', 'command': 'harass_the_midianites', 'case_source': 'Num 25:16-18 — and the LORD spoke to Moses saying: harass the Midianites and strike them, for they harass you with their wiles with which they beguiled you in the matter of Peor and in the matter of Cozbi daughter of a prince of Midian their sister, who was slain on the day of the plague in the matter of Peor'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda kk: len([l for l in w.log if l[0] == kk])
    return (n('israel', 'encamped_at'), n('the-moabites', 'feared'), n('the-moabites', 'loathed'), n('balak', 'plea_made'), n('balaam', 'cursing_barred'), is_open('balaam', 'cursing_barred'), n('balaam', 'refused'),
            n('balak', 'honor_owed'), is_open('balak', 'honor_owed'), n('balaam', 'bound_to_the_word'), n('balaam', 'mark_of_anger'), n('balaam', 'adversary_in_the_way'), n('the-she-ass', 'beaten'), n('the-she-ass', 'mouth_opened'),
            n('balaam', 'eyes_uncovered'), n('balaam', 'confessed'), n('balak', 'sacrifice_offered'), n('balak', 'altars_built'), n('balak', 'offered_burnt_and_sacrifices'), n('balaam', 'word_put_in_mouth'), n('israel', 'oracle_blessed'),
            n('balaam', 'spirit_rested'), n('balak', 'counsel_given'), n('israel', 'whored_after'), n('israel', 'bowed_to_their_gods'), n('israel', 'yoked_to_baal_peor'), n('israel', 'mark_of_anger'), n('israel', 'plague_struck'), is_open('israel', 'plague_struck'),
            n('moses', 'commanded'), is_open('moses', 'commanded'), n('the-court', 'commanded'), is_open('the-court', 'commanded'), n('zimri', 'cohabits_with_an_aramean'), is_open('zimri', 'cohabits_with_an_aramean'), n('israel', 'wept'),
            n('zimri', 'slain'), n('cozbi', 'slain'), n('pinchas', 'covenant_of_peace'), n('pinchas', 'invested_office'), n('israel', 'atoned_forgiven'), n('the-tabernacle', 'rule_installed'), n('israel', 'commanded'), is_open('israel', 'commanded'),
            L('TIMER-SET'), L('TIMER-FIRE'), L('MARKER'), L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, 1, 1, 2, 1, [False], 1,   # THE FIRST RUN'S READING: the block's entry carries open=False — a BLOCK is never opened nor closed (6b's lesson applied the wrong way round in the prediction: the hand typed [True] for 'never closed'); every other slot as predicted
                       1, [False], 6, 2, 1, 1, 1,
                       1, 1, 1, 3, 3, 2, 4,
                       1, 1, 1, 1, 1, 1, 1, [False],
                       1, [True], 1, [True], 1, [False], 1,
                       1, 1, 1, 1, 1, 1, 1, [True],
                       0, 0, 0, 41, 53, 11)   # PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 7b"): Israel encamped twice (the plains, Shittim); Moab feared and loathed; Balak's two pleas; the block on Balaam OPEN forever; the refusal; the honor debit CLOSED at 24:11; the formula's SIX; the two marks of anger on Balaam and one on Israel; the ass beaten and its mouth opened; the eyes uncovered, the confession; Balak's sacrifice, three altar-buildings, three offerings; the word put twice; the FOUR parables; the spirit; the counsel; the spec's two clauses; the yoking; the plague OPENED and CLOSED at 25:8; Moses' and the court's debits OPEN; Zimri's cohabiting CLOSED; the weeping; Zimri and Cozbi slain; the covenant, the office, the atonement, the rule; the Midian debit OPEN; no timer, no marker (an advance); forty-one events; fifty-three writes; eleven entities (israel, the moabites, balak, balaam, the she-ass, moses, the court, zimri, cozbi, pinchas, the tabernacle)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Balak\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW and DISPUTE rows; the expected string = the cell's verdict, typed).
# =====================================================================
CASES = [
    # F1 — the call
    ('Num 22:1; 36:13; Deut 34:1 — the last camp (computed)', lambda: the_call({'ask': 'last_camp'}, DATA), 'the plains of Moab — the last camp; the book never moves again (22:1; 36:13; Deut 34:1)'),
    ('Sanhedrin 105a:13; Num 22:4, 22:7, 25:6-18 — Midian joined', lambda: the_call({'ask': 'midian_joined'}, DATA), 'Midian joined Moab at 22:4 and 22:7 and returns with Cozbi (25:6-18) — the thread to chapter 31 (Sanhedrin 105a:13)'),
    ('Num 22:6-24:9 — the three curse-roots (computed)', lambda: the_call({'ask': 'curse_roots'}, DATA), 'three curse-roots, twenty tokens (arar 7, qabab 10, zaam 3) — and no curse spoken (22:12; Deut 23:6)'),
    ('Gen 12:3, 27:29 at Num 22:6, 24:9 — the blessing formula (the primeval and mamre engines CALLED)', lambda: the_call({'ask': 'blessing_formula'}, DATA), "the patriarchs' formula — Gen 12:3 blesses first (the primeval engine's ladder), Gen 27:29 curses first (the mamre engine's clauses); 24:9 returns Isaac's reversed"),
    ('Num 22:20-24:13 — the word-formula\'s six seats (computed)', lambda: the_call({'ask': 'word_formula'}, DATA), "the word-formula at six seats — do (22:20, akh 'only'), speak (22:35, efes 'nothing but'), speak (22:38), keep (23:12), do (23:26), speak (24:13)"),
    ('Num 22:20, 22:35, 23:13 — the restrictors (the export operator\'s kin)', lambda: the_call({'ask': 'restrictors'}, DATA), "the restrictors — akh 'only' (22:20), efes 'nothing but' (22:35), efes 'only its edge' (23:13): the permission narrowed to the word"),
    ('Makkot 10b:6; Sanhedrin 105a:15 — the way one wishes', lambda: the_call({'ask': 'way_one_wishes'}, DATA), "led in the way he wishes — 'you shall not go' (22:12) then 'rise, go' (22:20): Makkot 10b; Isa 48:17; Prov 3:34"),
    ('Num 22:12; Deut 23:6 — cursing barred (the block)', lambda: the_call({'ask': 'cursing_barred'}, DATA), "cursing barred — 'you shall not curse the people, for it is blessed' (22:12): a block never closed; Deut 23:6 the run"),
    ('Kiddushin 4a:8; Num 22:13-14 — the refusal\'s spelling', lambda: the_call({'ask': 'refuses_spelling'}, DATA), "'Balaam refuses' (22:14) written without a yod — Kiddushin 4a's ground for expounding the yod elsewhere; the refusal-verb Pharaoh's"),
    ('Sanhedrin 105a:14; Num 22:7-8 — Midian\'s elders left', lambda: the_call({'ask': 'midian_elders_left'}, DATA), "Midian's elders left between 22:7 and 22:8 — the ink's delta the shelf reads (Sanhedrin 105a:14)"),
    ('Sanhedrin 105a:9; Num 24:3, 24:15 — his son Beor', lambda: the_call({'ask': 'beno_form'}, DATA), "'his son Beor' (24:3, 24:15) — the archaic construct the shelf reads as 'his son': Balaam greater than his father (Sanhedrin 105a:9)"),
    ('Sanhedrin 105a:7-8 — Balaam\'s name', lambda: the_call({'ask': 'balaam_name'}, DATA), "Balaam's name expounded — without a nation / wore down the nation; his father Beor read as Laban the Aramean (Sanhedrin 105a:7-8)"),
    ('Sanhedrin 106a:17; Josh 13:22; Num 22:7 — prophet then diviner', lambda: the_call({'ask': 'prophet_then_diviner'}, DATA), "first a prophet, at the end a diviner (Josh 13:22 — Sanhedrin 106a:17); 'divinations in their hand' at 22:7 the noun's Torah four"),
    ('Chullin 19b:14; Num 22:5 — adjacent to me', lambda: the_call({'ask': 'mimmul'}, DATA), "'adjacent to me' (22:5) — the slaughter law's 'adjacent to the nape' defined from Balak's message (Chullin 19b)"),
    ('Gen 20:3, 31:24; Num 22:9, 22:20 — God came to (computed)', lambda: the_call({'ask': 'gentile_prophecy_by_night'}, DATA), "'God came to' — three gentiles by night (Gen 20:3, 31:24; Num 22:9, 22:20), never an Israelite in that clause"),
    ('Num 22:18, 24:13 — the house of silver (computed)', lambda: the_call({'ask': 'house_of_silver'}, DATA), "'his house full of silver and gold' at 22:18 (small or great; the LORD my God) and 24:13 (good or bad; from my own heart; no 'my God')"),
    ('Num 22:17, 24:11 — the honor promised and revoked', lambda: the_call({'ask': 'honor_promised'}, DATA), "the honor promised at 22:17 is revoked at 24:11 in its own words — the debit closed by the revocation"),
    ('Num 22:5-6, 22:15-17 — the two embassies', lambda: the_call({'ask': 'embassies'}, DATA), "two embassies (22:5-6, 22:15-17) — Balak's pleas to Balaam; the second with the honor"),
    # F2 — the she-ass and the angel
    ('Sanhedrin 105b:11; Num 22:21-22; Gen 22:3 — the saddling', lambda: the_ass_and_the_angel({'ask': 'saddling'}, DATA), "the Akedah's morning at Balaam's (22:21-22 = Gen 22:3): love and hatred upset the conduct of the great (Sanhedrin 105b:11)"),
    ('Num 22:23-28 — three strikes (the parser\'s 3)', lambda: the_ass_and_the_angel({'ask': 'three_strikes'}, DATA), 'struck three times (22:23, 22:25, 22:27) — the parser\'s 3 at 22:28 and 22:33, the plene three at 22:32'),
    ('Mishnah Avot 5:6; Num 22:28 — the mouth of the ass', lambda: the_ass_and_the_angel({'ask': 'mouth_of_the_ass'}, DATA), 'the mouth of the she-ass created at twilight — the third of the ten (Avot 5:6); opened at 22:28'),
    ('Menachot 66b:6; Shabbat 105a:4; Num 22:32 — yarat', lambda: the_ass_and_the_angel({'ask': 'yarat'}, DATA), "'yarat' (22:32) read as an abbreviation: the ass feared, saw, turned (Menachot 66b; Shabbat 105a)"),
    ('Num 22:31, 24:4, 24:16 — the eyes uncovered', lambda: the_ass_and_the_angel({'ask': 'eyes_uncovered'}, DATA), "the eyes uncovered at 22:31 — Balaam's own title at 24:4 and 24:16"),
    ('Num 22:34; Exod 9:27 — the confession', lambda: the_ass_and_the_angel({'ask': 'confession'}, DATA), "'I have sinned' (22:34) — Pharaoh's confession at Balaam's mouth, the Torah's two gentile confessions"),
    ('Num 22:23, 22:31 — the sword\'s spelling (the reading\'s bytes)', lambda: the_ass_and_the_angel({'ask': 'sword_spelling'}, DATA), "'drawn' plene at 22:23 and defective at 22:31 — the ass's seeing and Balaam's, eight verses apart"),
    ('Num 22:28, 22:32, 22:33, 24:10 — the two times-words (the taught parser)', lambda: the_ass_and_the_angel({'ask': 'times_word'}, DATA), "two times-words — the ass's 'three feet' (regalim, 22:28, 22:32 plene, 22:33) and Balak's 'three times' (pe'amim, 24:10): the festivals' two words"),
    ('Num 22:41, 23:14, 23:28 against 21:19-20 — the three stands (computed)', lambda: the_ass_and_the_angel({'ask': 'stands_stations'}, DATA), "the three stands are chapter 21's last stations — Bamoth (22:41 = 21:19), Pisgah (23:14 = 21:20), Peor (23:28 = 21:20's clause): the third the god of 25:3"),
    ('Num 22:22, 22:32 — the adversary', lambda: the_ass_and_the_angel({'ask': 'adversary'}, DATA), "the angel as an adversary (22:22, 22:32) — the satan-word's two Torah seats; God's anger the first of three"),
    ('Zevachim 102a; Num 22:22, 24:10, 25:3 — the three angers', lambda: the_ass_and_the_angel({'ask': 'anger_mark'}, DATA), "three angers, three marks — God's at Balaam (the adversary, 22:22), Balak's at Balaam (the honor revoked, 24:10), the LORD's at Israel (the plague, 25:3)"),
    ('Sanhedrin 105a:17; Avodah Zarah 4b:2-3 — Balaam and the ass (DISPUTE)', lambda: the_ass_and_the_angel({'ask': 'balaam_and_the_ass'}, DATA), "a diviner by his member (Mar Zutra) / bestiality with his ass (Mar son of Ravina) — DISPUTE (Sanhedrin 105a:17)"),
    ('Num 22:41, 23:13 — the edge of the people', lambda: the_ass_and_the_angel({'ask': 'edge_of_the_people'}, DATA), "the edge of the people seen from Bamoth (22:41), 'only its edge' at 23:13 — the restrictor's third seat"),
    # F3 — the three stands and the four parables
    ('Sanhedrin 105b:12; Nazir 23b:4; Num 23:1-30 — the forty-two (the parser\'s 7, 7, 7)', lambda: the_stands({'ask': 'forty_two_offerings'}, DATA), 'twenty-one altars, forty-two beasts (7, 7, 7 × 3) — Ruth the reward (Sanhedrin 105b:12; Nazir 23b)'),
    ('Zevachim 116a — the gentile\'s burnt offering (DATA)', lambda: the_stands({'ask': 'gentile_olah'}, DATA), "Balak's burnt offerings accepted from a gentile (Zevachim 116a) — Jethro's row the exodus engine's"),
    ('Berakhot 7a:8; Avodah Zarah 4b:1-4; Num 24:16 — the knowledge of the Most High', lambda: the_stands({'ask': 'most_high_knowledge'}, DATA), "'knows the knowledge of the Most High' = fixes the moment of God's anger (one 58,888th of an hour) — Berakhot 7a; Avodah Zarah 4b"),
    ('Avodah Zarah 4b:5; Berakhot 7a:13; Num 23:8 — no anger those days', lambda: the_stands({'ask': 'no_anger_those_days'}, DATA), "no anger in Balaam's days — 'how shall I curse whom El has not cursed' (23:8); Micah 6:5 'know the righteous acts'"),
    ('Sanhedrin 105b:8-10 — the moment of anger (DATA)', lambda: the_stands({'ask': 'moment_of_anger'}, DATA), "God's anger a moment daily — the first three hours, when the kings crown themselves to the sun and the rooster's crest whitens (Sanhedrin 105b:8-10)"),
    ('Avodah Zarah 25a:1; Sanhedrin 105a:12; Num 23:10, 24:14 — the death of the upright', lambda: the_stands({'ask': 'death_of_the_upright'}, DATA), "'the death of the upright' — the patriarchs' (the book of Yashar, Avodah Zarah 25a); Balaam's sign for himself, 'I go to my people' the other arm (Sanhedrin 105a:12)"),
    ('Mishnah Sanhedrin 10:2 — Balaam\'s share', lambda: the_stands({'ask': 'balaam_share'}, DATA), 'no share in the world to come — Balaam among the four commoners (Mishnah Sanhedrin 10:2)'),
    ('Sanhedrin 105a:10-11 — the gentiles\' share', lambda: the_stands({'ask': 'gentile_share'}, DATA), "gentiles who fear God have a share — R. Yehoshua's, the mishnah's opinion (Sanhedrin 105a:11); Balaam alone excluded"),
    ('Pirkei Avot 5:19 — Balaam\'s disciples', lambda: the_stands({'ask': 'balaam_disciples'}, DATA), "Balaam's disciples — an evil eye, a haughty spirit, a limitless appetite — inherit Gehinnom (Avot 5:19)"),
    ('Sanhedrin 105b:17-19; Deut 23:6; Num 24:5-7 — the curses turned', lambda: the_stands({'ask': 'curses_turned'}, DATA), "each clause of 24:5-7 the curse he intended (Sanhedrin 105b:17-18); all reverted but the synagogues — Deut 23:6's singular 'curse' (105b:19)"),
    ('Taanit 20a:15; Sanhedrin 105b:20-106a:2; Num 24:6 — the reed and the cedar', lambda: the_stands({'ask': 'reed_and_cedar'}, DATA), "the cedar-blessing worse than Ahijah's reed-curse — the reed bends and yields the quill; the cedar falls to the south wind (Taanit 20a; Sanhedrin 105b-106a)"),
    ('Berakhot 12b:15-16; Num 24:9 — the Shema\'s candidate', lambda: the_stands({'ask': 'shema_candidate'}, DATA), "Balak's portion nearly fixed in the Shema — for 24:9's 'lay down... rouse him' (Berakhot 12b:16), not for 23:22's Exodus (12b:15)"),
    ('Bava Batra 60a:5; Num 24:2 — the tents\' doors', lambda: the_stands({'ask': 'tents_doors'}, DATA), "the tents' doors not aligned — 'dwelling by its tribes' (24:2) the source that one may not open an entrance opposite another's (Bava Batra 60a)"),
    ('Berakhot 16a:1; Num 24:5-6 — the tents and the aloes', lambda: the_stands({'ask': 'tents_aloes'}, DATA), "the tents and the aloes one skin (24:5-6) — Berakhot 16a reads the aloes as tents of Torah beside the purifying streams"),
    ('Berakhot 38a:14; Num 23:22 — motzi\'s tense', lambda: the_stands({'ask': 'motzi_tense'}, DATA), "'motzi' past tense from 23:22 — the bread blessing's 'who brings forth' argued from Balaam's verse (Berakhot 38a)"),
    ('Chullin 35b:14; Keritot 22a:14; Niddah 19b:10, 55b:21; Num 23:24 — the blood of the slain', lambda: the_stands({'ask': 'blood_of_the_slain'}, DATA), "'the blood of the slain' (23:24) — the blood that flows at death is the liquid that renders food susceptible; not the spurting blood; a wound's blood too (Chullin 35b; Keritot 22a; Niddah 19b, 55b)"),
    ('Niddah 31a:20; Num 23:10 — the fourth part', lambda: the_stands({'ask': 'fourth_part'}, DATA), "'the fourth part of Israel' read as the couplings God counts (Niddah 31a:20) — the homograph the reading told by the points"),
    ('Sanhedrin 105a:16; Niddah 31a:21; Num 24:3 — the opened eye', lambda: the_stands({'ask': 'opened_eye'}, DATA), "blind in one eye — 'the man of the opened eye' (24:3): Sanhedrin 105a:16; Niddah 31a:21 the reason"),
    ('Sanhedrin 105a:16; Sotah 10a:9; Num 23:3 — shefi', lambda: the_stands({'ask': 'shefi'}, DATA), "lame in one leg — 'shefi' (23:3): Sanhedrin 105a:16 (the reading's 'bare height', Onkelos's 'alone')"),
    ('Rosh Hashanah 32b:11-15; Num 23:21 — the teruah of a king (DISPUTE)', lambda: the_stands({'ask': 'teruah_of_a_king'}, DATA), "23:21 one of the Torah's three Kingship verses (with Deut 33:5, Exod 15:18); recited with the shofarot too (R. Yosei) — DISPUTE (Rosh Hashanah 32b)"),
    ('Nedarim 32a:12-13; Num 23:23 — no divination', lambda: the_stands({'ask': 'no_divination'}, DATA), "'no divination in Jacob' (23:23) — the plain sense kept against Rebbi's reading; the non-diviner brought within the partition (Nedarim 32a)"),
    ('Sanhedrin 39b:1; Num 23:9 — dwells alone', lambda: the_stands({'ask': 'dwells_alone'}, DATA), "'not reckoned among the nations' (23:9) — the definition rule: 'the nations' excludes Israel (Sanhedrin 39b)"),
    ('Sanhedrin 56a:6, 92a:1; Sotah 41b:13; Num 23:8 — kabbo', lambda: the_stands({'ask': 'kabbo_curse'}, DATA), "the qabab-root's definition seat — 'kabbo' = a curse (23:8): the blasphemer's 'nokev' read from it (Sanhedrin 56a; lev24's first call)"),
    ('Rosh Hashanah 11a:8; Sotah 46b:1; Num 24:21 — eitan', lambda: the_stands({'ask': 'eitan'}, DATA), "'eitan' (24:21) = mighty (Rosh Hashanah 11a), hard as a rock or old (Sotah 46b) — the Kenite's nest in the sela, sitting 6's rock-word"),
    ('Sanhedrin 106a:5; Num 24:23 — who shall live', lambda: the_stands({'ask': 'who_shall_live'}, DATA), "'who shall live when El appoints this' (24:23) — two readings: the indulgent in God's name; the nation between the lion and the lioness (Sanhedrin 106a:5)"),
    ('Sanhedrin 106a:6; Dan 11:30; Num 24:24 — Kittim', lambda: the_stands({'ask': 'kittim'}, DATA), "Kittim's ships = the Roman legion (Sanhedrin 106a:6; Onkelos 'the Romans'); Daniel 11:30 the quotation"),
    ('Sanhedrin 106a:7; Num 24:14 — the counsel inverted', lambda: the_stands({'ask': 'counsel_inverted'}, DATA), "'what this people will do to your people' (24:14) — the inverted clause: Balaam curses himself obliquely (Sanhedrin 106a:7)"),
    ('Sifrei Bamidbar 131:1; Num 24:14, 31:16, 25:18 — the counsel (computed)', lambda: the_stands({'ask': 'counsel'}, DATA), "the counsel (24:14) named as Peor's cause by the ink at 31:16 ('by the word of Balaam... in the matter of Peor'); the Sifrei's adjacency dispute beside it"),
    ('Jerusalem Talmud Taanit 4:5:13; Num 24:17 — the star (DISPUTE)', lambda: the_stands({'ask': 'star_reading'}, DATA), "the star applied to bar Koziba by R. Akiva and refused by R. Yochanan ben Torta (Jerusalem Talmud Taanit 4:5) — Onkelos's KING and MESSIAH the translation's text"),
    ('Sanhedrin 105b:16; Num 23:5, 23:16 — the word in the mouth (DISPUTE)', lambda: the_stands({'ask': 'word_in_mouth_mode'}, DATA), "a word put in his mouth (23:5, 23:16) — an angel spoke from it (R. Elazar) / a hook held it (R. Yonatan): DISPUTE (Sanhedrin 105b:16)"),
    ('Gen 49:9 at Num 24:9 — Judah\'s blessing (the family engine CALLED)', lambda: the_stands({'ask': 'judah_blessing'}, DATA), "Jacob's blessing of Judah in Balaam's mouth (24:9 = Gen 49:9 but two words) — the family engine's lion (two of the six names)"),
    ('Gen 27:29 at Num 24:9 — Isaac\'s formula reversed (the mamre engine CALLED)', lambda: the_stands({'ask': 'isaac_formula'}, DATA), "Isaac's formula reversed at 24:9 — Gen 27:29 curses first (the mamre engine's clauses), Balaam blesses first"),
    ('Gen 12:2-3 — the promise ladder (the primeval engine CALLED)', lambda: the_stands({'ask': 'promise_ladder'}, DATA), "the promise ladder of Gen 12:2-3 — 'bless your blessers, curse your curser' — the formula's first seat (the primeval engine)"),
    ('Num 23:22, 24:8 — one letter (the reading\'s delta)', lambda: the_stands({'ask': 'one_letter'}, DATA), "23:22 -> 24:8 with one letter changed — 'brings them out' to 'brings him out'"),
    ('Num 23:7-24:23; 21:27 — seven parables (chukat CALLED)', lambda: the_stands({'ask': 'parables'}, DATA), "seven parables taken up — the parable-tellers' word of 21:27 (chukat's row PAID: Balaam and Beor the tellers, Chullin 60b)"),
    # F4 — Peor
    ('Exod 34:15-16 at Num 25:1-2 — the spec\'s run (the erection engine CALLED; M-22)', lambda: peor({'ask': 'spec_run'}, DATA), "Exod 34:15-16's spec RUN at 25:1-2 — whored after their daughters, ate of their sacrifices, bowed to their gods; the feminine 'their gods' at the two seats alone (the erection engine CALLED)"),
    ('Bekhorot 5b:5; Sanhedrin 106a:12 — Shittim\'s name (DISPUTE)', lambda: peor({'ask': 'shittim_name'}, DATA), "Shittim the place's name (R. Eliezer) / an allusion to nonsense, harlotry and idolatry (R. Yehoshua) — DISPUTE (Bekhorot 5b)"),
    ('Bekhorot 5b:6; Sanhedrin 106a:13 — they called the people (DISPUTE)', lambda: peor({'ask': 'called_the_people'}, DATA), "'and they called the people' (25:2) — naked women met them (R. Eliezer) / they all had emissions (R. Yehoshua): DISPUTE (Bekhorot 5b)"),
    ('Sanhedrin 106a:15 — and he dwelt is pain (the four seats computed)', lambda: peor({'ask': 'dwelt_is_pain'}, DATA), "'and Israel dwelt' — every 'and he dwelt' announces pain: Shittim, Jacob (Gen 37:1), Goshen (47:27), Judah and Israel (1 Kgs 5:5) — Sanhedrin 106a:15, the four seats computed"),
    ('Mishnah Sanhedrin 7:6; Sanhedrin 106a:11 — Peor\'s service', lambda: peor({'ask': 'peor_service'}, DATA), "baring oneself to Peor is its worship — liable as an idolater (Mishnah Sanhedrin 7:6): the Sifrei's rule at the reading, the answer sheet here"),
    ('Sanhedrin 106a:10; Avodah Zarah 36b — the wine\'s decree dated', lambda: peor({'ask': 'wine_decree_date'}, DATA), "the decree on gentile wine is later than Peor — 'not yet forbidden' at Shittim (Sanhedrin 106a:10; the Sifrei; the Jerusalem Talmud): a law's installation dated by the shelf"),
    ('Sanhedrin 64a:11; Num 25:3, 19:15 — yoked like the lid', lambda: peor({'ask': 'yoked_like_the_lid'}, DATA), "yoked to Baal-peor like a cord-bound lid on a vessel (Sanhedrin 64a:11 — 19:15's word, the reading's crown); Israel to the LORD like two dates lightly touching"),
    ('Sanhedrin 34b:21, 35a:2; Num 25:4 — hang before the sun (the wood-gatherer\'s court CALLED)', lambda: peor({'ask': 'hang_before_the_sun'}, DATA), "'hang them before the sun' — the heads installed as judges, the sinners judged by day and hanged (Sanhedrin 34b-35a; the Jerusalem Talmud); the wood-gatherer's court: the idolater hanged after stoning"),
    ('Jerusalem Talmud Sanhedrin 10:2:17; Exod 18:21 — the judges\' count (the exodus engine CALLED)', lambda: peor({'ask': 'judges_count'}, DATA), "the judges of Israel 78,600 (Exod 18:21's tiers by the exodus engine) — each executing two = 157,200 (the Jerusalem Talmud Sanhedrin 10:2:17; the Sifrei 131:2)"),
    ('Mishnah Sanhedrin 9:6; Sanhedrin 82a:10 — the zealots\' rule: in the act', lambda: peor({'ask': 'zealot_rule', 'arm': 'in_the_act'}, DATA), "zealots strike him — Zimri in the act (Mishnah Sanhedrin 9:6; Sanhedrin 82a); the cohabits entry OPEN from 25:6 to the spear"),
    ('Sanhedrin 82a:10 — separated', lambda: peor({'ask': 'zealot_rule', 'arm': 'separated'}, DATA), "separated — the zealot who then strikes is a murderer, executed (Sanhedrin 82a:10)"),
    ('Sanhedrin 82a:10 — self-defense', lambda: peor({'ask': 'zealot_rule', 'arm': 'self_defense'}, DATA), "Zimri turning and killing Phinehas — not executed: the zealot is a pursuer (Sanhedrin 82a:10)"),
    ('Sanhedrin 82a:12 — one who asks', lambda: peor({'ask': 'zealot_rule', 'arm': 'asks_the_court'}, DATA), "one who asks the court is not instructed — the law is not taught (Sanhedrin 82a:12; Moses forgot it)"),
    ('Sanhedrin 82a:12; Num 25:6 — the law forgotten', lambda: peor({'ask': 'halakha_forgotten'}, DATA), "the law forgotten by Moses at 25:6 — the Sanhedrin wept, the zealot remembered (Sanhedrin 82a:12): the rule not taught, installed by the deed"),
    ('Sanhedrin 82a:15; Num 25:7 — no weapon in the hall', lambda: peor({'ask': 'no_weapon_in_the_hall'}, DATA), "the spear taken only after rising from the assembly (25:7) — one does not enter the study hall armed (Sanhedrin 82a:15); the Torah's one spear"),
    ('Sanhedrin 44a:14, 82b:3; Ps 106:30; Num 25:8-9 — cast before God', lambda: peor({'ask': 'cast_before_god'}, DATA), "cast before God — 'shall twenty-four thousand fall for these?' (Sanhedrin 82b:3; Ps 106:30): the plague stayed at the spear, the count 24,000 by the parser"),
    ('Horayot 10b:15; Nazir 23b:4 — for its own sake', lambda: peor({'ask': 'for_its_sake'}, DATA), "Zimri's licentiousness not for its own sake — twenty-four thousand fell (Nazir 23b; Horayot 10b); Tamar's for a mitzvah bore kings"),
    ('Num 25:9, 17:14, 1:23, 26:14 — the plague\'s count (korach and bamidbar CALLED)', lambda: peor({'ask': 'plague_count'}, DATA), "the plague's dead 24,000 (25:9) — Korach's formula and 14,700 (17:14); Simeon 59,300 -> 22,200 the checkpoint at the second census; the total 603,550 (bamidbar CALLED)"),
    ('Num 25:8, 25:13 against 17:12-13 — Aaron and Phinehas (computed; korach CALLED)', lambda: peor({'ask': 'aaron_and_phinehas'}, DATA), "Aaron's incense clause and verb at Phinehas's spear — 'the plague was stayed' (17:13, 25:8) and 'he atoned for' (17:12, 25:13): the Sifrei's father-son title measured on the ink; korach's incense cell CALLED"),
    ('Num 15:22-31 at 25:2-3 — the idolatry principle (shelach CALLED)', lambda: peor({'ask': 'idolatry_principle'}, DATA), "the Peor congregation under 15:22-31's principle — the shelach engine's idolatry_principle row CALLED (its error cell)"),
    ('Num 25:3, 32:13-14 — the third anger', lambda: peor({'ask': 'anger_third'}, DATA), "the third anger (25:3) — its mark the plague, stayed by the spear (25:8)"),
    ('Kiddushin 3:12 by the family engine; Num 25:6 — the Aramean woman', lambda: peor({'ask': 'aramean_woman'}, DATA), "the Midianite woman's child would follow her (Kiddushin 3:12 by the family engine) — the case the zealots strike in (Mishnah Sanhedrin 9:6)"),
    # F5 — Phinehas and Midian
    ('Zevachim 101b:10; Num 25:13 — the priesthood by the deed (the priesthood engine CALLED)', lambda: phinehas_and_midian({'ask': 'priesthood_by_the_deed'}, DATA), "Phinehas not a priest until he killed Zimri — 'a covenant of everlasting priesthood' written only after (Zevachim 101b); the priesthood engine's addressees bind the sons of Aaron, this grandson the exception"),
    ('Sanhedrin 82b:6; Num 25:12 — the covenant of peace', lambda: phinehas_and_midian({'ask': 'covenant_of_peace'}, DATA), "the covenant of peace (25:12) — HEAVEN's entry in force forever; God to Moses: greet him first with peace (Sanhedrin 82b:6)"),
    ('Ketubot 13b:16; Yevamot 100b:8; Num 25:13 — his seed after him', lambda: phinehas_and_midian({'ask': 'seed_after_him'}, DATA), "'his seed after him' — the priest's descendants must be attributed to him: the shetuki serves not, marries yes (Ketubot 13b; Yevamot 100b)"),
    ('Kiddushin 66b:10 — the unfit seed\'s service', lambda: phinehas_and_midian({'ask': 'unfit_seed_service'}, DATA), "the disqualified priest's service valid after the fact — 'his seed after him' includes unfit seed (Kiddushin 66b:10)"),
    ('Kiddushin 66b:13; Num 25:12 — the blemished priest\'s service', lambda: phinehas_and_midian({'ask': 'blemished_service'}, DATA), "the blemished priest's service invalid — 'peace' read 'whole' (Kiddushin 66b:13); the severed vav a letter's shape the DB's bytes cannot carry"),
    ('Sanhedrin 82b:5; Sifrei Bamidbar 131:3; Num 25:7, 25:11 — the lineage answer', lambda: phinehas_and_midian({'ask': 'lineage_answer'}, DATA), "the lineage answers the taunt — 'son of Eleazar son of Aaron the priest' (25:11): priest son of priest, zealot son of zealot, turner-away son of turner-away (the Sifrei 131:3; Sanhedrin 82b:5)"),
    ('Menachot 20a:1; Num 18:19, 25:13 — the covenant of salt and of the priesthood (korach\'s row)', lambda: phinehas_and_midian({'ask': 'covenant_salt_priesthood'}, DATA), "'covenant' at 18:19 and 25:13 — the salt as indispensable as the priesthood (Menachot 20a; korach's covenant_of_salt row)"),
    ('Sifrei Bamidbar 131:5; Bava Kamma 110b — the twenty-four gifts (korach CALLED)', lambda: phinehas_and_midian({'ask': 'twenty_four_gifts'}, DATA), "the twenty-four priestly gifts (the Sifrei 131:5; Bava Kamma 110b) — korach's row CALLED: the priesthood Phinehas's covenant confers"),
    ('Sifrei Bamidbar 131:4; Yoma 9a — the high priests\' count (DISPUTE)', lambda: phinehas_and_midian({'ask': 'high_priest_count'}, DATA), "twelve high priests in the first Temple and eighty in the second (the Sifrei 131:4) against Yoma 9a's more than three hundred — the shelf disagreeing with itself, recorded: DISPUTE"),
    ('Sifrei Bamidbar 131:5; Sanhedrin 82b:6; Num 25:13 — the tense of he atoned (DISPUTE)', lambda: phinehas_and_midian({'ask': 'atone_tense'}, DATA), "'and he atoned' read future by the Sifrei against the morphology's past — the atonement forever (Sanhedrin 82b:6): DISPUTE on the tense of one word"),
    ('Bava Kamma 38a:16; Deut 2:9; Num 25:17 — Midian not Moab', lambda: phinehas_and_midian({'ask': 'midian_not_moab'}, DATA), "Midian harassed, Moab spared — Moses' own a fortiori needed Deut 2:9's bar (Bava Kamma 38a); the debit on Israel toward Midian OPEN to 31:7"),
    ('Sanhedrin 106a:16-17, 106b:1; Num 31:8 — Balaam\'s death', lambda: phinehas_and_midian({'ask': 'balaam_death'}, DATA), "Balaam killed by the sword at Midian (31:8) — come for his wages for the twenty-four thousand (Sanhedrin 106a:16); all four court modes in him (Rav, 106b:1)"),
    ('Exod 40:15 at Num 25:13 — everlasting priesthood (the erection engine CALLED)', lambda: phinehas_and_midian({'ask': 'everlasting_priesthood'}, DATA), "'everlasting priesthood' at Exod 40:15 (all Aaron's sons — the erection engine's clause) and 25:13 (Phinehas's line): the clause narrowed"),
    ('Num 25:15, 25:18, 31:8; Josh 13:21 — Cozbi and Zur', lambda: phinehas_and_midian({'ask': 'cozbi_and_zur'}, DATA), "Cozbi daughter of Zur — Zur one of Midian's five kings killed beside Balaam (31:8): the father dies in the war his daughter's death opens"),
    ('Num 25:17-18, 10:9, 24:7; Esther 3:10 — the harass-root', lambda: phinehas_and_midian({'ask': 'harass_root'}, DATA), "the harass-root (25:17-18) — the trumpets' enemy (10:9) and Haman the Agagite's title in Esther; 24:7's Agag and this command meet in one root"),
    ('Mishnah Sanhedrin 9:6; Sanhedrin 82a:12; Num 25:10-13 — the rule installed by the deed', lambda: phinehas_and_midian({'ask': 'rule_installed'}, DATA), "the zealots' rule installed by the deed and ratified by the covenant's speech — rule_installed on the tent (law_balak:zealot), no halt and no docket: THE TENT's form at a second seat"),
    ('Sanhedrin 82b:6; Num 25:13, 17:12 — atoned forever', lambda: phinehas_and_midian({'ask': 'atoned_forever'}, DATA), "'and he atoned for the children of Israel' (25:13) — Aaron's incense verb (17:12); the atonement forever (Sanhedrin 82b:6)"),
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
    print('\nBALAK: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    sys.exit(0 if ok == len(CASES) else 1)
