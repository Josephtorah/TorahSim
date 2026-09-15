import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 1:1-4:20 — BAMIDBAR: THE CENSUS, THE CAMP, THE LEVITES, THE FIRSTBORN, THE KOHATHITES' BURDEN (THE NUMBERS WALK
# sitting 1b, 2026-09-09; World/step9/NUMBERS_WALK.md "Sitting 1b"). The first Numbers portion compiled after its walk:
# the census's arithmetic computed from the ink's own numerals by the ENGINE'S PARSER (taught the census's grammar at
# this sitting — census_probes.py 17/17, every marker on the tape re-verified), the twelve summed against the total on
# three seats in two books, the Levite houses against the total as written (the delta the shelf asks in the same words,
# Bekhorot 5a:8), the excess redeemed at five per skull with the shekel CALLED (Exod 30:13's twenty gerah) and the human
# firstborn's verdict CALLED (Exod 13's clause), the camp and the march as data, the ages as a table, the Kohathites'
# packing with its three death clauses. Five motions of the deliverable rule, the wrap the sixth; every cell cites its
# source; every token probed (zero-report law); effects on every cell (the effects law). Reading ledgers: the nine
# logic/oral_triage/num_0{1,2,3,4}_*_2026-09-09.md; the exam's docket: num_01_04_bamidbar_exam_2026-09-09.md.

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 66, ('the guard counted %d expectations, the tripwire holds 66' % GUARDED)   # the guard's own count on the first run (the hand said 62)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib
import effects_layer as FX
import world_engine as WE
import cold_run_pesach as PS                     # THE EDGE: bamidbar -> pesach CALL, reference (3:12 'opener of the womb' = Exod 13:2, 12)
import cold_run_incense_shekel as IS             # THE EDGE: bamidbar -> incense_shekel CALL, reference (3:47 'twenty gerah' = Exod 30:13)
import cold_run_sanctuary_build as SB            # THE EDGE: bamidbar -> sanctuary_build CALL, reference (the conversion layer; 38:26's count)

HERE = _os.path.dirname(_os.path.abspath(__file__))
# ONE copy of the numeral parser: the sequence runner's INK block executed here (the stitcher's way — no import edge)
_SRC = open(_os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
_INK = {'re': re, 'sqlite3': sqlite3, 'os': _os, 'WE': WE}
_INK['_ROOT'] = _ROOT   # THE PORTABLE REPO (2026-09-15): the INK block reads the store through the root; the exec'd namespace must carry it
exec(_SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1], _INK)
ink_numbers, verse_words = _INK['ink_numbers'], _INK['verse_words']

db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num'
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('באחד',    1, 1,  'on the first — the date stamp'),
    ('שאו',     1, 2,  'lift [the head] — the census idiom'),
    ('שמות',    1, 2,  'names — the count of names'),
    ('לגלגלתם', 1, 2,  'by their skulls — per head'),
    ('עשרים',   1, 3,  'twenty — the first threshold'),
    ('ויתילדו', 1, 18, 'and they declared their pedigrees'),
    ('ויפקדם',  1, 19, 'and he counted them — the run'),
    ('אלף',     1, 46, 'thousand — the total'),
    ('אך',      1, 49, 'only — the exemption'),
    ('והזר',    1, 51, 'and the stranger — the death clause'),
    ('קצף',     1, 53, 'wrath — the guard\'s purpose'),
    ('דגלו',    2, 2,  'his banner'),
    ('מנגד',    2, 2,  'at a distance — the datum'),
    ('ראשנה',   2, 9,  'first — the march'),
    ('יחנו',    2, 17, 'they camp — as they camp so they journey'),
    ('חנו',     2, 34, 'they camped — the run'),
    ('תולדת',   3, 1,  'the generations of'),
    ('ובנים',   3, 4,  'and sons [they had not]'),
    ('הקרב',    3, 6,  'bring near — the tribe'),
    ('נתונם',   3, 9,  'given [given]'),
    ('פטר',     3, 12, 'opener [of the womb] — the firstborn clause'),
    ('חדש',     3, 15, 'a month — the Levite threshold'),
    ('ואהרן',   3, 39, 'and Aaron — the dotted word'),
    ('ויאמר',   3, 40, 'and He said — the one said-frame'),
    ('העדפים',  3, 46, 'who exceed — the excess'),
    ('חמשת',    3, 47, 'five [five] — the distributive'),
    ('גרה',     3, 47, 'gerah — the shekel\'s unit'),
    ('ואלף',    3, 50, 'and a thousand — the addend'),
    ('שלשים',   4, 3,  'thirty — the work threshold'),
    ('הקדשים',  4, 4,  'the holy of holies'),
    ('כליל',    4, 6,  'wholly [of blue]'),
    ('התמיד',   4, 7,  'the continual [bread]'),
    ('ודשנו',   4, 13, 'and they shall remove the ashes'),
    ('ומתו',    4, 15, 'lest they die — the first death clause'),
    ('תכריתו',  4, 18, 'cut off — cut not off'),
    ('כבלע',    4, 20, 'as it is swallowed'),
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
TRIBES = ['reuben', 'simeon', 'gad', 'judah', 'issachar', 'zebulun', 'ephraim', 'manasseh', 'benjamin', 'dan', 'asher', 'naphtali']   # the count's order (1:20-43)
TWELVE = {t: N('Num', 1, v)[0] for t, v in zip(TRIBES, range(21, 44, 2))}
TOTAL = N('Num', 1, 46)[0]; TOTAL_2 = N('Num', 2, 32)[0]; TOTAL_EXOD = N('Exod', 38, 26)[-1]
CAMPS = {'judah': N('Num', 2, 9)[0], 'reuben': N('Num', 2, 16)[0], 'ephraim': N('Num', 2, 24)[0], 'dan': N('Num', 2, 31)[0]}
HOUSES = {'gershon': N('Num', 3, 22)[0], 'kohath': N('Num', 3, 28)[0], 'merari': N('Num', 3, 34)[0]}
LEV_WRITTEN = N('Num', 3, 39)[0]; FIRSTBORN = N('Num', 3, 43)[0]; EXCESS = N('Num', 3, 46)[0]; RATE = N('Num', 3, 47)[0]; GERAH = N('Num', 3, 47)[1]; MONEY = N('Num', 3, 50)[0]
AGES = N('Num', 4, 3)
_snap = sqlite3.connect(('file:' + _ROOT + '/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro'), uri=True)
AARON_DOTTED = any('ׄ' in h for (h,) in _snap.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=3 AND v.verse=39"))
assert sum(TWELVE.values()) == TOTAL == TOTAL_2 == TOTAL_EXOD, (sum(TWELVE.values()), TOTAL, TOTAL_2, TOTAL_EXOD)
assert sum(CAMPS.values()) == TOTAL and FIRSTBORN - LEV_WRITTEN == EXCESS and EXCESS * RATE == MONEY and AGES == [30, 50], (CAMPS, FIRSTBORN, LEV_WRITTEN, EXCESS, RATE, MONEY, AGES)
SHEKEL_SEATS = IS.shekel('twenty_gerah')['v']            # THE CALL: the unit's seats — 3:47 among them
CONVERSION = SB.books('conversion_layer')['v']            # THE CALL: Onkelos' selaim on the erection's accounts
assert 'Num 3:47' in SHEKEL_SEATS and CONVERSION == 'selaim_of_the_sanctuary', (SHEKEL_SEATS, CONVERSION)


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'wilderness_firstborn_sanctity': {
        'value': 'sanctified_and_remained',
        'settings': {
            'sanctified_and_remained': "the firstborn born in the wilderness were sanctified and their sanctity did not cease — R. Yochanan (Bekhorot 4b:11-12, 5a:3: 'Mine they SHALL BE'; Rav Pappa 4b:24: the count of 3:40-43 in the second year includes them)",
            'until_the_census': "sanctified only until the count of 3:40-43, and not again until the land (Exod 13:11-12) — Reish Lakish (Bekhorot 4b:13, 5a:1-2); the attribution reversed in Rav Mordekhai's tradition (5a:5-7)"},
        'source': "the ink counts the firstborn 'from a month old' in the second year (3:40-43) and says nothing of the wilderness-born's sanctity — the dispute is the shelf's (Bekhorot 4b:11-5a:7)"},
    'zar_who_served': {
        'value': 'death_by_heaven',
        'settings': {
            'death_by_heaven': "a non-priest who served in the Temple — the Rabbis: death at the hand of Heaven (Mishnah Sanhedrin 9:6 / Sanhedrin 81b:17)",
            'strangulation': "R. Akiva: strangulation (Mishnah Sanhedrin 9:6)"},
        'source': "the ink writes 'and the stranger who approaches shall be put to death' (1:51, 3:10, 3:38, 18:7) and names no mode — the mode is the shelf's dispute"},
    'showbread_on_the_march': {
        'value': 'not_disqualified',
        'settings': {
            'not_disqualified': "4:7 'and THE CONTINUAL BREAD shall be on it' — continual even on the journey: not disqualified (Menachot 95a:5)",
            'disqualified': "2:17 'as they camp so they journey' — the encampment juxtaposed to the journey: disqualified when it leaves the courtyard (Menachot 95a:4, 95a:8)"},
        'source': "two verses of this span, one on each side (Menachot 95a:4-8); the reading ledger's crown 'the bread travels on the table' is the first arm's ink"},
    'bread_always': {
        'value': 'never_without',
        'settings': {
            'never_without': "handbreadth for handbreadth — the table is never without loaves (Exod 25:30 'before Me always'; Mishnah Menachot 11:7, the first teacher — Menachot 99b:11)",
            'not_a_night': "R. Yosei: removed entirely and replaced is 'always' too, so long as no night passes without bread (Menachot 99b:12)"},
        'source': "4:7's 'continual' on the march and 25:30's 'always' in the sanctuary — the measure of 'always' the shelf's"},
    'threshold_edge': {'value': 'a_month_and_a_day', 'settings': {'a_month_and_a_day': "3:15 'from a month old and UPWARD' — R. Eliezer's verbal analogy to the valuations' 'upward' (Lev 27:7): a month and a day (Arakhin 18b:5)"},
                       'source': "the ink writes 'and upward' at every threshold (1:3, 3:15, 3:40, 4:3) — the edge's day the shelf's"},
    'aaron_not_counted': {'value': True, 'settings': {True: "the dots over 'and Aaron' at 3:39 (the Masorah's puncta, carried by the snapshot store): Aaron NOT counted among the 22,000 (Bekhorot 4a:11)"},
                          'source': "the ink's own mark; the store measured live (AARON_DOTTED)"},
    'the_lots': {'value': '22,000 Levite slips and 273 five-shekel slips', 'settings': {'22,000 Levite slips and 273 five-shekel slips': "Sanhedrin 17a:7-8 — Moses' box: whoever drew 'Levite' was redeemed by a Levite, whoever drew 'five shekels' paid"},
                 'source': "the ink writes the excess (3:46) and the money (3:50) and not the selection — the procedure is the shelf's"},
    'tachash_identity': {'value': 'a_creature_unto_itself', 'settings': {'a_creature_unto_itself': "R. Meir: a creature unto itself, one horn on its forehead, came to Moses for the hour of the building, then hidden (Shabbat 28b:6)", 'sasgona': "Onkelos 4:6-14: a colored hide (sasgona)"},
                         'source': "the ink names the hide (4:6, 8, 10, 11, 12, 14) and not the beast"},
    'num9_command_day': {'value': 'the_first_of_the_first_month', 'settings': {'the_first_of_the_first_month': "Pesachim 6b:6 — Rav Nachman bar Yitzchak: 'wilderness' (9:1) / 'wilderness' (1:1): as 1:1 is the New Moon so 9:1 — a READING-PLACED date with its teacher"},
                         'source': "9:1 writes the month and not the day; the tape's 9:5 marker (the fourteenth) is text-constrained and RETROGRADE after 1:1 (Pesachim 6b:7; Rav Pappa's bound at 6b:8)"},
    'altar_height': {'value': 'ten_cubits', 'settings': {'ten_cubits': "3:26 juxtaposes the altar to the tabernacle — ten cubits (Shabbat 92a:6, R. Elazar; the Kohathites carried above ten handbreadths)", 'three_cubits': "Exod 27:1 'its height three cubits' — the written measure"},
                     'source': "the sanctuary engine's parameter; recorded here as a POINTER from 3:26, not set"},
}


# ===== F1: THE CENSUS (Num 1:1-46) ==========================================================================
def census(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'total':
        ink('1:46', '"and all the counted were six hundred thousand and three thousand and five hundred and fifty" — the parser on the ink')
        ink('1:20-43', 'the twelve counts, each from its own numerals: %s' % ', '.join('%s %d' % (t, TWELVE[t]) for t in TRIBES))
        return out('%d = the twelve summed' % TOTAL if sum(TWELVE.values()) == TOTAL else 'the twelve do not sum', ['counted'])
    if ask == 'three_seats':
        ink('1:46', '603,550'); ink('2:32', 'the four camps summed: %s' % ', '.join('%s %d' % kv for kv in CAMPS.items()))
        move('Exod 38:26 [IMPORT by the parser, live]', 'the half-shekel count "for six hundred thousand and three thousand and five hundred and fifty" — the erection\'s seat; Bekhorot 5a:10: 301,775 shekels = 201 talents and eleven maneh')
        return out('one number on three seats: 1:46, 2:32, Exod 38:26' if TOTAL == TOTAL_2 == TOTAL_EXOD else 'the seats differ', ['counted'])
    if ask == 'threshold':
        ink('1:3', '"from twenty years old and upward, everyone going out to the host in Israel" — the first of three thresholds')
        return out('twenty years and upward, the host', ['commanded'])
    if ask == 'by_names':
        ink('1:2', '"by the number of NAMES, every male by their skulls" — names written per head; Onkelos: receive the sum')
        ink('1:18', '"and they declared their pedigrees" — the verb\'s one seat in the Tanakh; the run on the command\'s own day (the date repeated)')
        return out('a count of names per head, the pedigrees declared', ['counted'])
    if ask == 'lineage':
        ink('1:2', '"by their families, by their fathers\' houses"')
        move('Bava Batra 109b:5 (Rava); Bekhorot 47a:13; Nazir 49a:3', 'the father\'s family is the family — lineage follows the father; Kiddushin 69a:9: the mamzeret\'s child follows the mother by "of his" (the exception recorded)')
        return out('lineage follows the father', ['counted'])
    if ask == 'levi':
        ink('1:47', '"and the Levites by the tribe of their fathers were not counted among them" — the narrator before the command')
        ink('1:49', '"only the tribe of Levi you shall not count, and their head you shall not lift among the children of Israel"')
        return out('exempt from the count', ['exempt'])
    if ask == 'orders':
        ink('1:5-15', 'the princes\' order — Gad eleventh'); ink('1:20-43', 'the count\'s order — Gad THIRD (beside Reuben and Simeon, the camp\'s companions)'); ink('2:3-31', 'the camp\'s order — Judah first, Gad under Reuben')
        move('Sotah 36b:1', 'the ephod\'s stones follow Exodus 1\'s order, not this list\'s — a fourth order')
        return out('three orders in the portion; Gad moves from eleventh to third', ['counted'])
    if ask == 'date':
        ink('1:1', '"on the first of the second month, in the second year of their going out of Egypt" — the tape\'s forward marker')
        move('Pesachim 6b:7 (Rav)', '"there is no earlier and later in the Torah" — 9:1 (the first month) precedes 1:1 (the second) in time: the retrograde marker; Rav Pappa 6b:8: across matters only')
        dat('the row num9_command_day = %s: %s' % (data['num9_command_day']['value'], data['num9_command_day']['settings'][data['num9_command_day']['value']]))
        return out('the first of the second month, year two; 9:1 earlier — no earlier and later', ['commanded'])
    if ask == 'designated':
        ink('1:17', '"who were designated (נקבו) by name"')
        move('Sanhedrin 56a:10', 'the blasphemer\'s "nokev" weighed as pronouncing the Name from this verse\'s "designated" — the shared lemma the reading computed, paired on the shelf')
        return out('designate / pronounce — one lemma, two seats', ['counted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE LEVITES AND THE FIRSTBORN (Num 3:1-51) ========================================================
def levites(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'houses':
        ink('3:22, 3:28, 3:34', 'Gershon %d, Kohath %d, Merari %d — each from its own numerals' % (HOUSES['gershon'], HOUSES['kohath'], HOUSES['merari']))
        return out('%d + %d + %d = %d' % (HOUSES['gershon'], HOUSES['kohath'], HOUSES['merari'], sum(HOUSES.values())), ['counted'])
    if ask == 'delta':
        ink('3:39', '"all the counted of the Levites... every male from a month old and upward: TWENTY-TWO THOUSAND" — as written')
        ink('3:22-34', 'the houses sum to %d' % sum(HOUSES.values()))
        move('Bekhorot 5a:8 (Kontrokos to Rabban Yochanan ben Zakkai)', 'the very subtraction: "in the individual count 22,300, in the collective 22,000 — where did the three hundred go?"')
        move('Bekhorot 5a:9', 'THE ANSWER: the three hundred were themselves FIRSTBORN, and a firstborn Levite cannot abrogate a firstborn Israelite (Abaye: it suffices him to abrogate his own)')
        dat('the row aaron_not_counted = %s (the dots over "and Aaron" at 3:39, measured live on the store: %s — Bekhorot 4a:11)' % (data['aaron_not_counted']['value'], AARON_DOTTED))
        return out('delta %d: firstborn Levites, who redeem no one' % (sum(HOUSES.values()) - LEV_WRITTEN), ['counted'])
    if ask == 'excess':
        ink('3:43', 'the firstborn males from a month old: %d' % FIRSTBORN); ink('3:46', '"the redemption of the three and the seventy and the two hundred who exceed the Levites" — %d' % EXCESS)
        return out('%d - %d = %d' % (FIRSTBORN, LEV_WRITTEN, EXCESS) if FIRSTBORN - LEV_WRITTEN == EXCESS else 'the excess does not match', ['counted'])
    if ask == 'rate':
        ink('3:47', '"you shall take five, five shekels per skull, by the shekel of the sanctuary you shall take — twenty gerah the shekel" — the doubled five distributive')
        move('CALLED cold_run_incense_shekel.shekel(twenty_gerah) -> %s [IMPORT, live]' % SHEKEL_SEATS, 'the unit defined at Exod 30:13, this seat among its five; Onkelos: five, five SELA\'IM... twenty MA\'IN the sela (Bekhorot 50a\'s "and we translate")')
        move('CALLED cold_run_sanctuary_build.books(conversion_layer) -> %s [IMPORT, live]' % CONVERSION, 'the translation layer on the accounts (38:24-26): the shekel is the sela')
        move('Mishnah Bekhorot 8:7', 'the five sela in TYRIAN maneh; the sanctuary shekel twenty gera')
        return out('five shekels per skull; twenty gerah the shekel (the sela of twenty ma\'ah)', ['pays'])
    if ask == 'money':
        ink('3:50', '"five and sixty and three hundred and a thousand by the shekel of the sanctuary" — %d, the thousand an addend' % MONEY)
        ink('3:51', '"and Moses gave the redemption money to Aaron and his sons by the mouth of the LORD, as the LORD commanded Moses" — the fifth pair closed with both formulas')
        dat('the row the_lots = %s' % data['the_lots']['value'])
        return out('%d x %d = %d to Aaron and his sons' % (EXCESS, RATE, MONEY) if EXCESS * RATE == MONEY else 'the money does not match', ['redeemed', 'pays'])
    if ask == 'human_firstborn':
        v, e, pr = PS.firstborn({'kind': 'human'}, {})                                                                  # THE CALL
        P.append(('MOVE', 'CALLED cold_run_pesach.firstborn(human) -> %s [%s]' % (v, '; '.join(x[1][:60] for x in pr))))
        ink('3:12', '"instead of every firstborn, OPENER OF THE WOMB" — Exod 13\'s clause at its Numbers seat (five Torah seats, computed)')
        return out(v, e)
    if ask == 'two_heads':
        ink('3:47', '"five, five shekels PER SKULL"')
        move('Menachot 37b:1', 'the redemption depends on the skull — a two-headed firstborn is redeemed twice: ten sela')
        return out('ten sela — by the skull', ['pays'])
    if ask == 'means':
        m = case['means']
        move('Mishnah Bekhorot 8:8', 'not with slaves, notes, land or consecrated items; a note obliges the father but does not redeem the son; the coins lost before reaching the priest — the father liable: redeemed only when the money is in the priest\'s hand (18:15\'s order)')
        if m in ('coins', 'money_worth'):
            return out('redeemed when in the priest\'s hand', ['pays', 'consecrated_firstborn'])
        return out('the father obliged, the son not redeemed', ['pays'])
    if ask == 'age':
        ink('3:40', '"from a month old and upward"')
        move('Bekhorot 49a:6', '"month" / "month" (18:16) — the redemption for the generations after thirty days')
        dat('the row threshold_edge = %s' % data['threshold_edge']['value'])
        return out('after thirty days' if case.get('age_days', 31) >= 30 else 'not yet — before thirty days', ['pays'] if case.get('age_days', 31) >= 30 else ['exempt'])
    if ask == 'partner':
        ink('3:13', '"I sanctified to Me every firstborn IN ISRAEL"')
        move('Mishnah Bekhorot 1:1, 2:1; Bekhorot 2a:1, 13a:9', 'a firstborn owned even partly by a gentile has no firstborn status')
        return out('exempt — a gentile partner', ['exempt'])
    if ask == 'owner':
        o, a = case['owner'], case['animal']
        if o in ('priest', 'levite') and a in ('donkey', 'son'):
            ink('3:45', '"take the Levites instead of every firstborn... and the animal of the Levites instead of their animals"')
            move('Mishnah Bekhorot 1:1; Bekhorot 3b:15 (the a-fortiori); 4b:1 ("shall be" — for the generations)', 'priests and Levites exempt from the son\'s and the donkey\'s redemption')
            return out('exempt — a priest or a Levite (the son and the donkey)', ['exempt'])
        if o in ('priest', 'levite') and a == 'kosher':
            move('Mishnah Bekhorot 2:1; Bekhorot 13a:9', 'obligated in the kosher animal\'s firstborn — exempted only from the son and the donkey')
            return out('obligated — the kosher animal\'s firstborn', ['consecrated_firstborn'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'one_lamb':
        ink('3:46', 'the ink counts a surplus of HUMANS (273) and no surplus of animals')
        move('Bekhorot 4b:6-9 (R. Chanina; Abaye; "behemat" singular)', 'one Levite lamb rendered many Israelite donkeys exempt')
        return out('one lamb for many donkeys', ['exempt'])
    if ask == 'wilderness_sanctity':
        s = data['wilderness_firstborn_sanctity']['value']
        dat('the row wilderness_firstborn_sanctity = %s: %s' % (s, data['wilderness_firstborn_sanctity']['settings'][s]))
        return out('sanctified and remained (R. Yochanan)' if s == 'sanctified_and_remained' else 'sanctified until the census (Reish Lakish)', ['consecrated_firstborn'])
    if ask == 'generations':
        ink('3:1-2', '"these are the generations of Aaron AND MOSES" — then Aaron\'s sons alone')
        move('Sanhedrin 19b:17 (R. Yonatan)', 'whoever teaches another\'s son Torah is as if he sired him — Aaron begot, Moses taught')
        return out('Moses taught them: called by his name', ['counted'])
    if ask == 'no_sons':
        ink('3:4', '"and sons they had not" — the phrase\'s one Tanakh seat')
        move('Yevamot 64a:2 (Abba Chanan in R. Eliezer\'s name)', 'had they had children they would not have died — one who does not procreate is liable to death')
        return out('the sonlessness as the cause', ['exempt'])
    if ask == 'substitution':
        ink('3:12', '"I have taken the Levites... instead of every firstborn" — Onkelos: brought near'); ink('3:13', '"on the day I smote every firstborn in Egypt I sanctified to Me every firstborn in Israel" — the ground dated to the plague\'s night')
        return out('the Levites instead of the firstborn; the ground the plague\'s night', ['substituted_for_the_firstborn'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE CAMP AND THE MARCH (Num 2:1-34) ==============================================================
def camp(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'sides':
        ink('2:3, 2:10, 2:18, 2:25', 'east Judah (Issachar, Zebulun); south Reuben (Simeon, Gad); west Ephraim (Manasseh, Benjamin); north Dan (Asher, Naphtali) — the compass in the ink\'s own words')
        return out('east judah, south reuben, west ephraim, north dan', ['arrayed_by_banners'])
    if ask == 'march':
        ink('2:9, 2:16, 2:24, 2:31', '"first they journey", "second", "third", "last" — the ordinals'); ink('2:17', '"and the tent of meeting shall journey with the camp of the Levites in the midst of the camps; as they camp so they journey"')
        return out('judah, reuben, the tent in the midst, ephraim, dan — as they camp so they journey', ['arrayed_by_banners'])
    if ask == 'tent_on_the_march':
        ink('2:17', '"then the tent of meeting shall journey" — journeying, still the tent')
        move('Zevachim 61b:3, 116b:16-17 (Rav Huna)', 'the sacrificial food not disqualified by the march: the tent is the tent and the camp the camp while traveling')
        return out('still the tent; the meat not disqualified', ['arrayed_by_banners'])
    if ask == 'three_camps':
        move('Zevachim 116b:14-15 (Tosefta Kelim Bava Kamma 1:12)', 'the walls to the Temple Mount = the camp of Israel; the Mount to Nicanor\'s gate = the camp of the Levites; the courtyard = the camp of the Divine Presence (as within the curtains)')
        return out('israel: the walls to the mount; levites: the mount to nicanor; presence: the courtyard', ['arrayed_by_banners'])
    if ask == 'al':
        ink('2:20', '"and BESIDE him [alav] the tribe of Manasseh"')
        move('Menachot 96a:11 (Abba Shaul) — M-22\'s shape: a term of the camp read into the table\'s law', '"al" = beside: the frankincense beside the arrangements (Lev 24:7), not upon them')
        move('Menachot 27a:2', '"upon the wood" — the dilemma stands: TEIKU')
        return out('beside (Abba Shaul); on the wood a TEIKU', ['arrayed_by_banners'])
    if ask == 'showbread':
        s = data['showbread_on_the_march']['value']
        dat('the row showbread_on_the_march = %s: %s' % (s, data['showbread_on_the_march']['settings'][s]))
        return out('not disqualified — the continual bread (4:7)' if s == 'not_disqualified' else 'disqualified — as they camp so they journey (2:17)', ['arrayed_by_banners'])
    if ask == 'distance':
        ink('2:2', '"at a distance, round about the tent of meeting they shall camp" — no measure in the ink; Onkelos: opposite')
        move('Eruvin 51a:7-8 (the docket\'s corrected pointer)', 'the two thousand cubits are derived from Exod 16:29 through Num 35:5 (the Levite cities) — this verse is not their seat')
        return out('a datum; the measure\'s seat Num 35:5', ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE CHARGES, THE STRANGER, THE AGES (Num 1:47-53; 3:5-38; 4:3) ====================================
def charges(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'houses_charges':
        ink('3:25-26', 'Gershon: the tabernacle, the tent, its covering, the screens, the hangings, the cords — the woven'); ink('3:31', 'Kohath: the ark, the table, the lampstand, the altars, the holy vessels, the screen — the furniture'); ink('3:36-37', 'Merari: the boards, bars, pillars, sockets, pegs, cords — the frame')
        return out('gershon the woven, kohath the holy, merari the frame', ['charge_kept'])
    if ask == 'inner_ring':
        ink('3:23, 3:29, 3:35, 3:38', 'west Gershon, south Kohath, north Merari, east Moses and Aaron and his sons — the inner ring matches the outer\'s four sides')
        return out('west gershon, south kohath, north merari, east moses and aaron', ['charge_kept'])
    if ask == 'stranger':
        who = case['who']
        ink('1:51, 3:10, 3:38', '"and the stranger who approaches shall be put to death" — Onkelos: the LAY man; 18:7 the fourth seat')
        if who == 'non_levite':
            ink('1:51', 'the non-Levite at the tabernacle\'s taking down and setting up')
            return out('death — the stranger to the Levites\' office', ['put_to_death'])
        if who == 'non_priest':
            s = data['zar_who_served']['value']
            dat('the row zar_who_served = %s: %s' % (s, data['zar_who_served']['settings'][s]))
            move('Mishnah Sanhedrin 9:6 / Sanhedrin 81b:17', 'a non-priest who served — R. Akiva: strangulation; the Rabbis: death by Heaven')
            return out('death by Heaven (the Rabbis)' if s == 'death_by_heaven' else 'strangulation (R. Akiva)', ['put_to_death'])
        if who == 'levite_in_another_service':
            move('Arakhin 11b:4 (Abaye)', '3:38\'s stranger = a Levite in another Levite\'s service (a singer at the gate) — liable to death; the non-Levite\'s death already at 3:10')
            return out('death — a Levite in another Levite\'s service', ['put_to_death'])
        if who in ('priest', 'levite_in_his_service'):
            return out('exempt — his own service', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'watches':
        ink('3:38', '"Moses and Aaron and his sons keeping the watch of the sanctuary"')
        move('Tamid 26a:5 (Abaye)', 'the priests keep watch in three places (Mishnah Tamid 1:1) — from this verse')
        return out('three watch-places', ['charge_kept'])
    if ask == 'altars':
        ink('3:31', '"the lampstand and THE ALTARS" — plural')
        move('Chagigah 27a:3', 'the golden altar compared to the bronze: like the ground, no impurity (Mishnah Chagigah 3:8)')
        return out('the golden altar like the ground', ['charge_kept'])
    if ask == 'fitness':
        who, blemish, age, carrying = case['who'], case.get('blemished', False), case.get('age', 40), case.get('carrying', True)
        move('Mishnah Chullin 1:6; Chullin 24a:8-12; Sifrei Bamidbar 62:1', 'priests unfit by BLEMISH, never by years; Levites fit with a blemish, unfit by years (thirty to fifty — 4:3, 4:47), and only while the service is carrying on the shoulder (not at Shiloh, not in the Temple); twenty-five to apprentice, thirty to serve')
        if who == 'priest':
            return out('unfit — a blemish', ['exempt']) if blemish else out('fit — years do not disqualify a priest', ['appointed_to_serve'])
        if who == 'levite':
            if not carrying:
                return out('fit — years disqualify only while carrying', ['appointed_to_serve'])
            if age < 30:
                return out('unfit — under thirty (twenty-five to apprentice)', ['exempt'])
            if age > 50:
                return out('unfit — over fifty (8:25 he returns from the service)', ['exempt'])
            return out('fit — a blemish does not disqualify a Levite', ['appointed_to_serve'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'ages':
        ink('4:3', '"from thirty years old and upward until fifty years old" — %s' % AGES)
        move('Chullin 24a:12 (Sifrei Bamidbar 62:1)', 'twenty-five (8:24) to apprentice, thirty (4:3, 4:47) to serve; fifty (8:25) to return')
        return out('25 learn, 30 serve, 50 return', ['appointed_to_serve'])
    if ask == 'thresholds':
        ink('1:3; 3:15; 4:3', 'twenty years; a month; thirty to fifty — the three thresholds')
        dat('the row threshold_edge = %s' % data['threshold_edge']['value'])
        return out('twenty; a month and a day; thirty to fifty', ['commanded'])
    if ask == 'amarkal':
        ink('3:32', '"and the prince of the princes of Levi: Eleazar" — Onkelos: the AMARKAL appointed over the chiefs of the Levites')
        move('Mishnah Shekalim 5:2', 'no fewer than seven amarkalin and three treasurers in the Temple — the office Onkelos reads onto Eleazar')
        return out('one prince of princes in the wilderness; seven amarkalin in the Temple', ['appointed_to_serve'])
    if ask == 'wrath':
        ink('1:53', '"that there be no wrath upon the congregation of the children of Israel" — the guard\'s purpose; 18:5 the parallel')
        return out('the Levite ring a wrath-shield', ['charge_kept'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE KOHATHITES' BURDEN (Num 4:1-20) ==============================================================
def kohath(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'order':
        ink('4:5', '"Aaron and his sons shall come in when the camp journeys and take down the veil of the screen and cover with it the ark"'); ink('4:15', '"Aaron and his sons shall finish covering the holy... and AFTER THAT the sons of Kohath shall come to carry"')
        return out('the priests cover, then the Kohathites carry', ['charge_kept'])
    if ask == 'layers':
        ink('4:6', 'the ark: the veil, the tachash hide, a cloth WHOLLY OF BLUE on top — blue outside only here (the robe\'s phrase)'); ink('4:7-8, 4:9-12, 4:14', 'the table, the lampstand, the golden altar, the vessels: blue under, the hide outermost'); ink('4:13', 'the bronze altar: the ashes removed, PURPLE — the one not blue')
        return out('blue outside only the ark; the bronze altar ashed and purple; the rest hide-outermost', ['charge_kept'])
    if ask == 'bread':
        s = data['bread_always']['value']
        ink('4:7', '"and the continual bread shall be on it" — on the march')
        dat('the row bread_always = %s: %s' % (s, data['bread_always']['settings'][s]))
        return out('never without bread (the first teacher)' if s == 'never_without' else 'not a night without (R. Yosei)', ['charge_kept'])
    if ask == 'vessels_sanctified':
        ink('4:12', '"the service vessels with which they SHALL SERVE in the sanctuary"')
        move('Sanhedrin 16b:7; Shevuot 15a:4 (Rav Pappa)', 'the vessels of the generations are sanctified by their first service (Moses\' by anointing)')
        return out('by service, for the generations', ['charge_kept'])
    if ask == 'vessel_in_vessel':
        move('Yoma 58a:8 (the school of R. Yishmael on 4:12)', 'two vessels, one service — a vessel inside a vessel is a proper manner of service')
        return out('proper', ['charge_kept'])
    if ask == 'kasva':
        ink('4:7', '"the jugs [kesot] of libation" — the kasva, any service vessel'); ink('4:20', '"as the holy is swallowed [kevala]" — read as one who takes')
        move('Sanhedrin 81b:18, 82b:15 (Rav Yehuda; Mishnah Sanhedrin 9:6)', 'the thief of a service vessel is killed by zealots')
        return out('zealots strike him', ['put_to_death'])
    if ask == 'not_to_see':
        ink('4:20', '"and they shall not come in to see as the holy is swallowed, lest they die" — Onkelos: when they cover the vessels')
        move('Yoma 54a:12 (Rav)', 'at the packing even the Levites may not look')
        return out('even the Levites, at the packing', ['charge_kept'])
    if ask == 'death_clauses':
        ink('4:15, 4:19, 4:20', 'touching; approaching unassigned; seeing — three death clauses')
        return out('three: touch, approach unassigned, see', ['charge_kept'])
    if ask == 'cut_not_off':
        ink('4:18', '"cut not off the tribe of the families of the Kohathite from among the Levites" — the guard on the leaders'); ink('4:19', '"set them each man, each man to his service and to his burden"')
        return out('the leaders assign each man his load', ['commanded'])
    if ask == 'tachash':
        s = data['tachash_identity']['value']
        dat('the row tachash_identity = %s: %s' % (s, data['tachash_identity']['settings'][s]))
        return out('a creature unto itself (R. Meir)' if s == 'a_creature_unto_itself' else 'a colored hide (Onkelos)', ['charge_kept'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_census(event, world):
    """Num 1:1-4:20 (cold_run_bamidbar.py F1-F5). installed_by boot — the standing setting for a law spoken at its verse."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'census_commanded':
        return [E_('commanded', event['subject'], value='the_census', law='F1 [INK 1:2-3 "lift the head... from twenty years old and upward" — the spec: the count owed]')]
    if k == 'census_taken':
        world.close(event['subject'], 'commanded', 'Num 1:19 — as the LORD commanded Moses, and he counted them', value='the_census')
        return [E_('counted', event['subject'], value=event.get('total', TOTAL), law='F1 [INK 1:46 — the twelve summed = %d; 2:32; Exod 38:26]' % TOTAL)]
    if k == 'levites_exempted':
        return [E_('exempt', event['subject'], value='from_the_count', law='F1 [INK 1:47-49 "only the tribe of Levi you shall not count"]'),
                E_('charge_kept', event['subject'], value='the_tabernacle_of_the_testimony', law='F4 [INK 1:50-53 — appointed over the tabernacle; carry, serve, camp around, take down, set up; the charge kept]'),
                E_('appointed_to_serve', event['subject'], value='the_tabernacle', law='F4 [INK 1:50 "appoint the Levites" — Onkelos: appoint]'),
                E_('commanded', event['subject'], value='the_guard', law='F4 [INK 1:51, 1:53 — the stranger clause and the wrath-shield: the guard commanded — OPEN until the first march]')]
    if k == 'camp_commanded':
        return [E_('commanded', event['subject'], value='the_camp', law='F3 [INK 2:2-31 — the banners by the compass: the array owed]')]
    if k == 'camp_arrayed':
        world.close(event['subject'], 'commanded', 'Num 2:34 — so they camped by their banners and so they journeyed', value='the_camp')
        return [E_('arrayed_by_banners', event['subject'], value='east judah, south reuben, west ephraim, north dan; the tent in the midst', law='F3 [INK 2:34 — two runs in one report]')]
    if k == 'levites_given':
        return [E_('given_to_aaron', event['subject'], cp='aaron-and-sons', law='F2 [INK 3:6-9 "given, given are they to him" — Onkelos: handed over, given]'),
                E_('substituted_for_the_firstborn', event['subject'], value='the_firstborn_of_israel', law='F2 [INK 3:12-13 "instead of every firstborn, opener of the womb"; the ground the plague\'s night]'),
                E_('commanded', event['subject'], value='the_priesthoods_charge', law='F4 [INK 3:7-8 — his charge and the congregation\'s charge: OPEN, the service\'s own count in Naso]')]
    if k == 'levite_count_commanded':
        return [E_('commanded', event['subject'], value='the_levite_count', law='F2 [INK 3:15 "every male from a month old and upward you shall count them"]')]
    if k == 'levites_counted':
        world.close(event['subject'], 'commanded', 'Num 3:16 — and Moses counted them by the mouth of the LORD', value='the_levite_count')
        return [E_('counted', event['subject'], value=event.get('total_as_written', LEV_WRITTEN), law='F2 [INK 3:39 — %d as written; the houses %d; the delta %d: Bekhorot 5a:9]' % (LEV_WRITTEN, sum(HOUSES.values()), sum(HOUSES.values()) - LEV_WRITTEN))]
    if k == 'firstborn_count_commanded':
        return [E_('commanded', event['subject'], value='the_firstborn_count', law='F2 [INK 3:40 "count every firstborn male... and lift the number of their names"]')]
    if k == 'firstborn_counted':
        world.close(event['subject'], 'commanded', 'Num 3:42 — and Moses counted, as the LORD commanded him', value='the_firstborn_count')
        return [E_('counted', event['subject'], value=event.get('total', FIRSTBORN), law='F2 [INK 3:43 — %d]' % FIRSTBORN)]
    if k == 'redemption_commanded':
        return [E_('commanded', event['subject'], value='the_redemption', law='F2 [INK 3:46-48 — the excess at five per skull, the money to Aaron and his sons]')]
    if k == 'firstborn_redeemed':
        world.close(event['subject'], 'commanded', 'Num 3:51 — and Moses gave the redemption money to Aaron and his sons', value='the_redemption')
        return [E_('redeemed', event['subject'], value='%d at %d' % (EXCESS, RATE), law='F2 [INK 3:46-50 — %d x %d = %d; the shekel CALLED]' % (EXCESS, RATE, MONEY)),
                E_('pays', event['subject'], cp='aaron-and-sons', amount=MONEY, law='F2 [INK 3:50-51 — %d by the shekel of the sanctuary, to Aaron and his sons]' % MONEY)]
    if k == 'kohath_service_commanded':
        return [E_('charge_kept', event['subject'], value='kohath: the holy of holies', law='F5 [INK 4:4, 4:15 — the burden of the sons of Kohath]'),
                E_('commanded', event['subject'], value='the_kohathites_service', law='F5 [INK 4:5-20 — the packing\'s order, the three death clauses: OPEN, the work-count in Naso and the first march]')]
    if k == 'stranger_approached':
        v, e, _ = charges({'ask': 'stranger', 'who': event['who']}, DATA)
        if e == ['put_to_death']:
            return [E_('put_to_death', event['person'], cp='HEAVEN' if event['who'] == 'non_priest' and DATA['zar_who_served']['value'] == 'death_by_heaven' else 'the-court', value=event['who'], law='F4 [%s]' % v)]
        return [E_('exempt', event['person'], value=event['who'], law='F4 [%s]' % v)]
    if k == 'levite_service_case':
        v, e, _ = charges({'ask': 'fitness', 'who': event['who'], 'blemished': event.get('blemished', False), 'age': event.get('age', 40), 'carrying': event.get('carrying', True)}, DATA)
        if e == ['appointed_to_serve']:
            return [E_('appointed_to_serve', event['person'], value=v, law='F4 [Mishnah Chullin 1:6; Chullin 24a — %s]' % v)]
        return [E_('exempt', event['person'], value=v, law='F4 [Mishnah Chullin 1:6; Chullin 24a — %s]' % v)]
    if k == 'firstborn_redemption_case':
        a = event['ask']
        if a == 'two_heads':
            return [E_('pays', event['person'], cp='the-priest', amount=RATE * event.get('heads', 2), law='F2 [Menachot 37b:1 — by the skull]')]
        if a == 'means':
            v, e, _ = levites({'ask': 'means', 'means': event['means']}, DATA)
            if e == ['pays', 'consecrated_firstborn']:
                return [E_('pays', event['person'], cp='the-priest', amount=RATE, law='F2 [Mishnah Bekhorot 8:8 — %s]' % v), E_('consecrated_firstborn', event['person'], value='redeemed_in_the_priests_hand', law='F2 [Mishnah Bekhorot 8:8]')]
            return [E_('pays', event['person'], cp='the-priest', amount=RATE, value='son_not_redeemed', law='F2 [Mishnah Bekhorot 8:8 — %s]' % v)]
        if a == 'partner':
            return [E_('exempt', event['person'], value='gentile_partner', law='F2 [INK 3:13 "in Israel"; Mishnah Bekhorot 1:1, 2:1]')]
        if a == 'owner':
            v, e, _ = levites({'ask': 'owner', 'owner': event['owner'], 'animal': event['animal']}, DATA)
            if e == ['consecrated_firstborn']:
                return [E_('consecrated_firstborn', event['person'], value=event['animal'], law='F2 [Mishnah Bekhorot 2:1 — %s]' % v)]
            return [E_('exempt', event['person'], value='%s_%s' % (event['owner'], event['animal']), law='F2 [Mishnah Bekhorot 1:1; Bekhorot 3b:15, 4b:1 — %s]' % v)]
        if a == 'age':
            v, e, _ = levites({'ask': 'age', 'age_days': event['age_days']}, DATA)
            if e == ['pays']:
                return [E_('pays', event['person'], cp='the-priest', amount=RATE, law='F2 [Bekhorot 49a:6 — %s]' % v)]
            return [E_('exempt', event['person'], value='before_thirty_days', law='F2 [Bekhorot 49a:6 — %s]' % v)]
        if a == 'human':
            v, e, _ = levites({'ask': 'human_firstborn'}, DATA)                                          # the firstborn engine CALLED inside the cell
            return [E_('consecrated_firstborn', event['person'], value='opener_of_the_womb', law='F2 [CALLED cold_run_pesach.firstborn(human) -> %s]' % v), E_('pays', event['person'], cp='the-priest', amount=RATE, law='F2 [CALLED cold_run_pesach.firstborn(human); the five the data channel]')]
        return []
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 1-4: Mishnah Sanhedrin 9:6, Chullin 1:6, Bekhorot 1:1, 2:1, 8:7-8 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_census]
        w.advance(w.clock.day_in('exodus', 2, 2, 1))
        w.submit({'kind': 'stranger_approached', 'subject': 'the-israelite-at-the-boards', 'person': 'the-israelite-at-the-boards', 'who': 'non_levite', 'service': 'the_tabernacle', 'case_source': 'Num 1:51 — the stranger who approaches shall be put to death (the non-Levite)'})
        w.submit({'kind': 'stranger_approached', 'subject': 'the-levite-at-the-altar', 'person': 'the-levite-at-the-altar', 'who': 'non_priest', 'service': 'the_priesthood', 'case_source': 'Mishnah Sanhedrin 9:6; Num 3:10 — a non-priest who served'})
        w.submit({'kind': 'stranger_approached', 'subject': 'the-singer-at-the-gate', 'person': 'the-singer-at-the-gate', 'who': 'levite_in_another_service', 'service': 'the_gate', 'case_source': 'Arakhin 11b:4; Num 3:38 — a Levite in another Levite\'s service'})
        w.submit({'kind': 'stranger_approached', 'subject': 'the-priest-at-the-altar', 'person': 'the-priest-at-the-altar', 'who': 'priest', 'service': 'the_priesthood', 'case_source': 'Num 3:10 — Aaron and his sons keep their priesthood'})
        w.submit({'kind': 'levite_service_case', 'subject': 'the-blemished-priest', 'person': 'the-blemished-priest', 'who': 'priest', 'blemished': True, 'age': 40, 'case_source': 'Mishnah Chullin 1:6 — priests unfit by blemish'})
        w.submit({'kind': 'levite_service_case', 'subject': 'the-old-priest', 'person': 'the-old-priest', 'who': 'priest', 'age': 70, 'case_source': 'Mishnah Chullin 1:6 — years do not disqualify a priest'})
        w.submit({'kind': 'levite_service_case', 'subject': 'the-blemished-levite', 'person': 'the-blemished-levite', 'who': 'levite', 'blemished': True, 'age': 40, 'carrying': True, 'case_source': 'Mishnah Chullin 1:6 — Levites fit with a blemish'})
        w.submit({'kind': 'levite_service_case', 'subject': 'the-apprentice-levite', 'person': 'the-apprentice-levite', 'who': 'levite', 'age': 27, 'carrying': True, 'case_source': 'Chullin 24a:12 — twenty-five to apprentice, thirty to serve; Num 4:3'})
        w.submit({'kind': 'levite_service_case', 'subject': 'the-old-levite', 'person': 'the-old-levite', 'who': 'levite', 'age': 55, 'carrying': True, 'case_source': 'Num 4:3, 8:25 — until fifty; he returns'})
        w.submit({'kind': 'levite_service_case', 'subject': 'the-old-levite-at-shiloh', 'person': 'the-old-levite-at-shiloh', 'who': 'levite', 'age': 55, 'carrying': False, 'case_source': 'Chullin 24a:11 — the years disqualify only while carrying; not at Shiloh'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-two-headed-firstborn', 'person': 'the-two-headed-firstborn', 'ask': 'two_heads', 'heads': 2, 'case_source': 'Menachot 37b:1; Num 3:47 — per skull'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-father-with-a-note', 'person': 'the-father-with-a-note', 'ask': 'means', 'means': 'promissory_note', 'case_source': 'Mishnah Bekhorot 8:8 — a note obliges, does not redeem'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-father-with-coins', 'person': 'the-father-with-coins', 'ask': 'means', 'means': 'coins', 'case_source': 'Mishnah Bekhorot 8:7-8 — five sela, in the priest\'s hand'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-gentiles-partner', 'person': 'the-gentiles-partner', 'ask': 'partner', 'partner': 'gentile', 'case_source': 'Mishnah Bekhorot 1:1; Num 3:13 — in Israel'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-levites-donkey', 'person': 'the-levites-donkey', 'ask': 'owner', 'owner': 'levite', 'animal': 'donkey', 'case_source': 'Mishnah Bekhorot 1:1; Num 3:45 — priests and Levites exempt'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-priests-calf', 'person': 'the-priests-calf', 'ask': 'owner', 'owner': 'priest', 'animal': 'kosher', 'case_source': 'Mishnah Bekhorot 2:1 — obligated in the kosher animal\'s firstborn'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-twenty-day-firstborn', 'person': 'the-twenty-day-firstborn', 'ask': 'age', 'age_days': 20, 'case_source': 'Bekhorot 49a:6; Num 3:40 — from a month old'})
        w.submit({'kind': 'firstborn_redemption_case', 'subject': 'the-firstborn-son', 'person': 'the-firstborn-son', 'ask': 'human', 'case_source': 'Num 3:12; Exod 13:2, 13:13 — the firstborn engine called'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    amt = lambda eid, eff: [e.get('amount') for e in w.entity(eid).ledger if e['effect'] == eff]
    return (n('the-israelite-at-the-boards', 'put_to_death'), n('the-levite-at-the-altar', 'put_to_death'), n('the-singer-at-the-gate', 'put_to_death'), n('the-priest-at-the-altar', 'exempt'),
            n('the-blemished-priest', 'exempt'), n('the-old-priest', 'appointed_to_serve'), n('the-blemished-levite', 'appointed_to_serve'), n('the-apprentice-levite', 'exempt'), n('the-old-levite', 'exempt'), n('the-old-levite-at-shiloh', 'appointed_to_serve'),
            amt('the-two-headed-firstborn', 'pays'), n('the-father-with-a-note', 'consecrated_firstborn'), n('the-father-with-coins', 'consecrated_firstborn'), n('the-gentiles-partner', 'exempt'), n('the-levites-donkey', 'exempt'), n('the-priests-calf', 'consecrated_firstborn'),
            n('the-twenty-day-firstborn', 'exempt'), amt('the-firstborn-son', 'pays'), len(w.entities)), w
SCENE, _W = scene()


def narrative():
    """THE NUMBERS WALK 1b (2026-09-09; NUMBERS_WALK.md "Sitting 1b"): the portion's own acts AS HISTORY — the thirteen lines of Num 1:1-4:20 in
    the text's order on a world with this runner's daemon (eight commands, five runs — the five spec/run pairs as five open-then-closed
    debits), the marker at 1:1 (the first of the second month of the second year); recorded by the sequential run's recorder and stitched
    onto the tape (the marker at 1:1 is the tape's, text-constrained — the stitcher's row). Not a graded cell: the tuple below is a tripwire
    typed from the first run's print; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 1:1-4:20: Bamidbar on the tape — the census, the camp, the Levites, the firstborn, the Kohathites (the exodus epoch)', epoch='exodus')
        w.laws = [law_census]
        w.marker('Num 1:1', w.clock.day_in('exodus', 2, 2, 1), value='on the first of the second month, in the second year of their going out of Egypt (1:1) — the FORWARD marker before 9:1 (Pesachim 6b:7)')
        w.submit({'kind': 'census_commanded', 'subject': 'israel', 'threshold': 20, 'by_names': True, 'aides': 12, 'per_tribe': 1, 'case_source': 'Num 1:1-3 — and the LORD spoke to Moses in the wilderness of Sinai, in the tent of meeting, on the first of the second month in the second year: lift the head of all the congregation of the children of Israel... from twenty years old and upward'})
        w.submit({'kind': 'census_taken', 'subject': 'israel', 'counts': dict(TWELVE), 'total': TOTAL, 'by_names': True, 'date_repeated': True, 'case_source': 'Num 1:17-19 — and Moses and Aaron took these men... and they declared their pedigrees... as the LORD commanded Moses, and he counted them in the wilderness of Sinai; 1:46 six hundred thousand and three thousand and five hundred and fifty'})
        w.submit({'kind': 'levites_exempted', 'subject': 'the-levites', 'duties': ['carry', 'serve', 'camp_around', 'take_down', 'set_up'], 'stranger_clause': True, 'purpose': 'that there be no wrath', 'case_source': 'Num 1:48-53 — and the LORD spoke to Moses saying: only the tribe of Levi you shall not count... and the stranger who approaches shall be put to death... that there be no wrath upon the congregation'})
        w.submit({'kind': 'camp_commanded', 'subject': 'israel', 'banners': {'east': 'judah', 'south': 'reuben', 'west': 'ephraim', 'north': 'dan'}, 'march_order': ['judah', 'reuben', 'ephraim', 'dan'], 'tent_in_the_midst': True, 'distance': 'a datum', 'case_source': 'Num 2:1-2 — and the LORD spoke to Moses and to Aaron saying: each man by his banner with the signs of their fathers\' house shall the children of Israel camp; at a distance round about the tent of meeting'})
        w.submit({'kind': 'camp_arrayed', 'subject': 'israel', 'camps_total': TOTAL_2, 'camped': True, 'journeyed': True, 'case_source': 'Num 2:34 — and the children of Israel did according to all that the LORD commanded Moses: so they camped by their banners and so they journeyed'})
        w.submit({'kind': 'levites_given', 'subject': 'the-levites', 'given_to': 'aaron-and-sons', 'instead_of': 'the-firstborn-of-israel', 'ground_dated': 'the night of the plague', 'charges': ['his charge', 'the congregation\'s charge'], 'case_source': 'Num 3:5-13 — and the LORD spoke to Moses saying: bring near the tribe of Levi... given, given are they to him... I have taken the Levites instead of every firstborn, opener of the womb'})
        w.submit({'kind': 'levite_count_commanded', 'subject': 'the-levites', 'threshold': 'a month', 'by_houses': True, 'case_source': 'Num 3:14-15 — and the LORD spoke to Moses in the wilderness of Sinai saying: count the sons of Levi... every male from a month old and upward'})
        w.submit({'kind': 'levites_counted', 'subject': 'the-levites', 'houses': dict(HOUSES), 'total_as_written': LEV_WRITTEN, 'houses_sum': sum(HOUSES.values()), 'aaron_dotted': AARON_DOTTED, 'case_source': 'Num 3:16 — and Moses counted them by the mouth of the LORD, as he was commanded; 3:39 all the counted of the Levites... twenty-two thousand'})
        w.submit({'kind': 'firstborn_count_commanded', 'subject': 'the-firstborn-of-israel', 'threshold': 'a month', 'beasts_too': True, 'case_source': 'Num 3:40-41 — and the LORD said to Moses: count every firstborn male of the children of Israel from a month old and upward, and lift the number of their names'})
        w.submit({'kind': 'firstborn_counted', 'subject': 'the-firstborn-of-israel', 'total': FIRSTBORN, 'case_source': 'Num 3:42-43 — and Moses counted, as the LORD commanded him, every firstborn among the children of Israel; twenty-two thousand, three and seventy and two hundred'})
        w.submit({'kind': 'redemption_commanded', 'subject': 'the-firstborn-of-israel', 'excess': EXCESS, 'rate': RATE, 'unit': 'twenty gerah the shekel', 'recipients': 'aaron-and-sons', 'case_source': 'Num 3:44-48 — and the LORD spoke to Moses saying: take the Levites instead of every firstborn... and the redemption of the three and the seventy and the two hundred... five, five shekels per skull'})
        w.submit({'kind': 'firstborn_redeemed', 'subject': 'the-firstborn-of-israel', 'excess': EXCESS, 'rate': RATE, 'money': MONEY, 'recipients': 'aaron-and-sons', 'case_source': 'Num 3:49-51 — and Moses took the redemption money... five and sixty and three hundred and a thousand by the shekel of the sanctuary; and Moses gave the redemption money to Aaron and his sons by the mouth of the LORD'})
        w.submit({'kind': 'kohath_service_commanded', 'subject': 'the-levites', 'ages': [30, 50], 'packing_order': 'the priests cover, then the Kohathites carry', 'death_clauses': 3, 'eleazar_charge': ['the oil of the light', 'the incense of spices', 'the continual meal-offering', 'the anointing oil'], 'case_source': 'Num 4:1-20 — and the LORD spoke to Moses and to Aaron saying: lift the head of the sons of Kohath... from thirty years old and upward until fifty... they shall not touch the holy lest they die'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    val = lambda eid, eff: [e.get('value') for e in w.entity(eid).ledger if e['effect'] == eff]
    marker = [l for l in w.log if l[0] == 'MARKER']
    return (n('israel', 'commanded'), is_open('israel', 'commanded'), val('israel', 'counted'), n('israel', 'arrayed_by_banners'),
            n('the-levites', 'commanded'), is_open('the-levites', 'commanded'), n('the-levites', 'exempt'), n('the-levites', 'given_to_aaron'), n('the-levites', 'substituted_for_the_firstborn'), val('the-levites', 'counted'), n('the-levites', 'charge_kept'),
            n('the-firstborn-of-israel', 'commanded'), is_open('the-firstborn-of-israel', 'commanded'), val('the-firstborn-of-israel', 'counted'), val('the-firstborn-of-israel', 'redeemed'), [e.get('amount') for e in w.entity('the-firstborn-of-israel').ledger if e['effect'] == 'pays'],
            len(marker), marker[0][2].get('retrograde') if marker else None, w.clock.eras['exodus'].date(w.clock.day)[1:], len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, [False, False], [603550], 1,
                       4, [True, True, False, True], 1, 1, 1, [22000], 2,
                       2, [False, False], [22273], ['273 at 5'], [1365],
                       1, False, (2, 1), 3)   # NUMBERS_WALK.md "Sitting 1b" + THE FIRST RUN'S READING: the five spec/run pairs closed (two on israel, one on the Levites — the count's debit is the Levites' own, the fourth on them — two on the firstborn); the three open debits (the guard, the priesthood's charge, the Kohathites' service) beside the closed count; the counts as values; the marker forward at month 2 day 1 of year 2 (the date's tuple drops the year); three entities — the hand had typed three debits and the year
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Bamidbar\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the census
    ('Num 1:46 — the twelve summed equal the total (the parser on the ink)', lambda: census({'ask': 'total'}, DATA), '603550 = the twelve summed'),
    ('Num 1:46 = 2:32 = Exod 38:26 — one number on three seats (Bekhorot 5a:10)', lambda: census({'ask': 'three_seats'}, DATA), 'one number on three seats: 1:46, 2:32, Exod 38:26'),
    ('Num 1:3 — the first threshold', lambda: census({'ask': 'threshold'}, DATA), 'twenty years and upward, the host'),
    ('Num 1:2, 1:18 — the count of names; the pedigrees', lambda: census({'ask': 'by_names'}, DATA), 'a count of names per head, the pedigrees declared'),
    ('Bava Batra 109b:5 / Bekhorot 47a:13 / Nazir 49a:3 — 1:2: lineage follows the father', lambda: census({'ask': 'lineage'}, DATA), 'lineage follows the father'),
    ('Num 1:47-49 — Levi exempt from the count', lambda: census({'ask': 'levi'}, DATA), 'exempt from the count'),
    ('Num 1:5-15, 1:20-43, 2:3-31 — the tribes\' three orders (Sotah 36b:1 a fourth)', lambda: census({'ask': 'orders'}, DATA), 'three orders in the portion; Gad moves from eleventh to third'),
    ('Pesachim 6b:6-8 — 1:1\'s date and 9:1\'s: no earlier and later', lambda: census({'ask': 'date'}, DATA), 'the first of the second month, year two; 9:1 earlier — no earlier and later'),
    ('Sanhedrin 56a:10 — 1:17 "designated" and the blasphemer\'s lemma', lambda: census({'ask': 'designated'}, DATA), 'designate / pronounce — one lemma, two seats'),
    # F2 — the Levites and the firstborn
    ('Num 3:22-34 — the houses summed', lambda: levites({'ask': 'houses'}, DATA), '7500 + 8600 + 6200 = 22300'),
    ('Bekhorot 5a:8-9 — the delta: three hundred firstborn Levites', lambda: levites({'ask': 'delta'}, DATA), 'delta 300: firstborn Levites, who redeem no one'),
    ('Num 3:43, 3:46 — the excess', lambda: levites({'ask': 'excess'}, DATA), '22273 - 22000 = 273'),
    ('Num 3:47 — five per skull; the shekel CALLED (Mishnah Bekhorot 8:7)', lambda: levites({'ask': 'rate'}, DATA), 'five shekels per skull; twenty gerah the shekel (the sela of twenty ma\'ah)'),
    ('Num 3:50-51 — the money (Sanhedrin 17a\'s lots)', lambda: levites({'ask': 'money'}, DATA), '273 x 5 = 1365 to Aaron and his sons'),
    ('Num 3:12 / Exod 13:13 — the human firstborn: the firstborn engine called', lambda: levites({'ask': 'human_firstborn'}, DATA), 'redeem (five sela — fetched constant)'),
    ('Menachot 37b:1 — a two-headed firstborn: by the skull', lambda: levites({'ask': 'two_heads'}, DATA), 'ten sela — by the skull'),
    ('Mishnah Bekhorot 8:8 — redeemed with coins, in the priest\'s hand', lambda: levites({'ask': 'means', 'means': 'coins'}, DATA), 'redeemed when in the priest\'s hand'),
    ('Mishnah Bekhorot 8:8 — a promissory note: obliged, not redeemed', lambda: levites({'ask': 'means', 'means': 'promissory_note'}, DATA), 'the father obliged, the son not redeemed'),
    ('Bekhorot 49a:6 — the redemption after thirty days (3:40\'s month)', lambda: levites({'ask': 'age', 'age_days': 31}, DATA), 'after thirty days'),
    ('Bekhorot 49a:6 — before thirty days', lambda: levites({'ask': 'age', 'age_days': 20}, DATA), 'not yet — before thirty days'),
    ('Mishnah Bekhorot 1:1, 2:1 — 3:13 "in Israel": the gentile partner', lambda: levites({'ask': 'partner'}, DATA), 'exempt — a gentile partner'),
    ('Mishnah Bekhorot 1:1 / Bekhorot 3b:15 — a Levite\'s donkey', lambda: levites({'ask': 'owner', 'owner': 'levite', 'animal': 'donkey'}, DATA), 'exempt — a priest or a Levite (the son and the donkey)'),
    ('Bekhorot 4b:1 — a priest\'s son, for the generations ("shall be")', lambda: levites({'ask': 'owner', 'owner': 'priest', 'animal': 'son'}, DATA), 'exempt — a priest or a Levite (the son and the donkey)'),
    ('Mishnah Bekhorot 2:1 / Bekhorot 13a:9 — a priest\'s kosher animal', lambda: levites({'ask': 'owner', 'owner': 'priest', 'animal': 'kosher'}, DATA), 'obligated — the kosher animal\'s firstborn'),
    ('Bekhorot 4b:6-9 — one Levite lamb for many donkeys', lambda: levites({'ask': 'one_lamb'}, DATA), 'one lamb for many donkeys'),
    ('Bekhorot 4b:11-5a:7 — the wilderness-born\'s sanctity: R. Yochanan (the running setting; Reish Lakish recorded)', lambda: levites({'ask': 'wilderness_sanctity'}, DATA), 'sanctified and remained (R. Yochanan)'),
    ('Sanhedrin 19b:17 — the generations of Aaron and Moses', lambda: levites({'ask': 'generations'}, DATA), 'Moses taught them: called by his name'),
    ('Yevamot 64a:2 — "and sons they had not"', lambda: levites({'ask': 'no_sons'}, DATA), 'the sonlessness as the cause'),
    ('Num 3:12-13 — the substitution and its dated ground', lambda: levites({'ask': 'substitution'}, DATA), 'the Levites instead of the firstborn; the ground the plague\'s night'),
    # F3 — the camp
    ('Num 2:3-25 — the four sides', lambda: camp({'ask': 'sides'}, DATA), 'east judah, south reuben, west ephraim, north dan'),
    ('Num 2:9-31, 2:17 — the march', lambda: camp({'ask': 'march'}, DATA), 'judah, reuben, the tent in the midst, ephraim, dan — as they camp so they journey'),
    ('Zevachim 61b:3, 116b:16-17 — the tent on the march', lambda: camp({'ask': 'tent_on_the_march'}, DATA), 'still the tent; the meat not disqualified'),
    ('Zevachim 116b:14-15 — the three camps', lambda: camp({'ask': 'three_camps'}, DATA), 'israel: the walls to the mount; levites: the mount to nicanor; presence: the courtyard'),
    ('Menachot 96a:11 / 27a:2 — "beside him"; the TEIKU', lambda: camp({'ask': 'al'}, DATA), 'beside (Abba Shaul); on the wood a TEIKU'),
    ('Menachot 95a:4-5 — the showbread on the march (the running setting: not disqualified)', lambda: camp({'ask': 'showbread'}, DATA), 'not disqualified — the continual bread (4:7)'),
    ('Num 2:2 / Eruvin 51a:7-8 — the distance a datum; the measure\'s seat', lambda: camp({'ask': 'distance'}, DATA), 'a datum; the measure\'s seat Num 35:5'),
    # F4 — the charges, the stranger, the ages
    ('Num 3:25-37 — the three charges', lambda: charges({'ask': 'houses_charges'}, DATA), 'gershon the woven, kohath the holy, merari the frame'),
    ('Num 3:23-38 — the inner ring', lambda: charges({'ask': 'inner_ring'}, DATA), 'west gershon, south kohath, north merari, east moses and aaron'),
    ('Num 1:51 — the non-Levite', lambda: charges({'ask': 'stranger', 'who': 'non_levite'}, DATA), 'death — the stranger to the Levites\' office'),
    ('Mishnah Sanhedrin 9:6 — the non-priest who served (the Rabbis, the running setting; R. Akiva recorded)', lambda: charges({'ask': 'stranger', 'who': 'non_priest'}, DATA), 'death by Heaven (the Rabbis)'),
    ('Arakhin 11b:4 — a Levite in another Levite\'s service', lambda: charges({'ask': 'stranger', 'who': 'levite_in_another_service'}, DATA), 'death — a Levite in another Levite\'s service'),
    ('Num 3:10 — a priest in his priesthood', lambda: charges({'ask': 'stranger', 'who': 'priest'}, DATA), 'exempt — his own service'),
    ('Tamid 26a:5 — the priests\' three watches', lambda: charges({'ask': 'watches'}, DATA), 'three watch-places'),
    ('Chagigah 27a:3 — "the altars"', lambda: charges({'ask': 'altars'}, DATA), 'the golden altar like the ground'),
    ('Mishnah Chullin 1:6 — a blemished priest', lambda: charges({'ask': 'fitness', 'who': 'priest', 'blemished': True}, DATA), 'unfit — a blemish'),
    ('Mishnah Chullin 1:6 — an old priest', lambda: charges({'ask': 'fitness', 'who': 'priest', 'age': 70}, DATA), 'fit — years do not disqualify a priest'),
    ('Mishnah Chullin 1:6 — a blemished Levite', lambda: charges({'ask': 'fitness', 'who': 'levite', 'blemished': True, 'age': 40}, DATA), 'fit — a blemish does not disqualify a Levite'),
    ('Chullin 24a:12 — a Levite of twenty-seven', lambda: charges({'ask': 'fitness', 'who': 'levite', 'age': 27}, DATA), 'unfit — under thirty (twenty-five to apprentice)'),
    ('Num 4:3, 8:25 — a Levite of fifty-five, carrying', lambda: charges({'ask': 'fitness', 'who': 'levite', 'age': 55}, DATA), 'unfit — over fifty (8:25 he returns from the service)'),
    ('Chullin 24a:11 — a Levite of fifty-five at Shiloh', lambda: charges({'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False}, DATA), 'fit — years disqualify only while carrying'),
    ('Chullin 24a:12 / Sifrei Bamidbar 62:1 — the ages', lambda: charges({'ask': 'ages'}, DATA), '25 learn, 30 serve, 50 return'),
    ('Num 1:3, 3:15, 4:3 / Arakhin 18b:5 — the three thresholds', lambda: charges({'ask': 'thresholds'}, DATA), 'twenty; a month and a day; thirty to fifty'),
    ('Mishnah Shekalim 5:2 — the amarkal (Onkelos on 3:32)', lambda: charges({'ask': 'amarkal'}, DATA), 'one prince of princes in the wilderness; seven amarkalin in the Temple'),
    ('Num 1:53 — the wrath-shield', lambda: charges({'ask': 'wrath'}, DATA), 'the Levite ring a wrath-shield'),
    # F5 — the Kohathites' burden
    ('Num 4:5, 4:15 — the order', lambda: kohath({'ask': 'order'}, DATA), 'the priests cover, then the Kohathites carry'),
    ('Num 4:6-14 — the layers', lambda: kohath({'ask': 'layers'}, DATA), 'blue outside only the ark; the bronze altar ashed and purple; the rest hide-outermost'),
    ('Menachot 99b:11-12 — the bread always (the first teacher; R. Yosei recorded)', lambda: kohath({'ask': 'bread'}, DATA), 'never without bread (the first teacher)'),
    ('Sanhedrin 16b:7 / Shevuot 15a:4 — 4:12: vessels sanctified by service', lambda: kohath({'ask': 'vessels_sanctified'}, DATA), 'by service, for the generations'),
    ('Yoma 58a:8 — a vessel in a vessel', lambda: kohath({'ask': 'vessel_in_vessel'}, DATA), 'proper'),
    ('Sanhedrin 81b:18 — the kasva thief', lambda: kohath({'ask': 'kasva'}, DATA), 'zealots strike him'),
    ('Yoma 54a:12 — not to see, even the Levites', lambda: kohath({'ask': 'not_to_see'}, DATA), 'even the Levites, at the packing'),
    ('Num 4:15-20 — the three death clauses', lambda: kohath({'ask': 'death_clauses'}, DATA), 'three: touch, approach unassigned, see'),
    ('Num 4:18-19 — cut not off', lambda: kohath({'ask': 'cut_not_off'}, DATA), 'the leaders assign each man his load'),
    ('Shabbat 28b:6 — the tachash (R. Meir; Onkelos\' sasgona recorded)', lambda: kohath({'ask': 'tachash'}, DATA), 'a creature unto itself (R. Meir)'),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — the wrap: three strangers put to death and the priest exempt; the ages table six ways; the two-headed firstborn ten; the note obliges without redeeming, the coins redeem; the gentile\'s partner, the Levite\'s donkey exempt; the priest\'s calf obligated; the twenty-day firstborn not yet; the son redeemed by the firstborn engine\'s call',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 1:51, 3:10, 3:38, 3:13, 3:40, 3:45-47, 4:3 — the recorded rows replayed')]),
     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, [10], 0, 1, 1, 1, 1, 1, [5], 18)),
    ('THE NARRATIVE on the world engine — the tape\'s thirteen lines with the marker at 1:1 (the tripwire typed from the first run)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 1:1-4:20 — the eight commands and the five runs')]),
     (2, [False, False], [603550], 1, 4, [True, True, False, True], 1, 1, 1, [22000], 2, 2, [False, False], [22273], ['273 at 5'], [1365], 1, False, (2, 1), 3)),
]

if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA')
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
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE NUMBERS from the ink: the twelve %s; total %d (1:46) = %d (2:32) = %d (Exod 38:26); the houses %s = %d against %d written; the firstborn %d; the excess %d; %d x %d = %d; the ages %s; Aaron dotted in the store: %s' %
          (TWELVE, TOTAL, TOTAL_2, TOTAL_EXOD, HOUSES, sum(HOUSES.values()), LEV_WRITTEN, FIRSTBORN, EXCESS, EXCESS, RATE, MONEY, AGES, AARON_DOTTED))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nBAMIDBAR COMPILES — the census\'s arithmetic from the ink, the delta the shelf asks, the shekel and the firstborn engines called, the five spec/run pairs as five debits opened and closed.')
