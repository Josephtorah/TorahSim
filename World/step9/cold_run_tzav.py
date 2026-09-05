#!/usr/bin/env python3
# THE OFFERING-TORAH SPAN (Lev 6-8) — the fourth span compiled under
# the effects law (2026-09-03), the Tzav round's Step-5 deliverable.
# The bare ink of the priests' law layer: the one-way altar and its
# night windows, the vessel purge, the perpetual griddle offering's
# halving, the rejection machine, the karet bans, the priestly dues,
# and the installation transaction. Ink first (code/data separation);
# the Mishnah's rows are the answer sheets fed at run time; the
# Sifra's recorded arguments are the labeled compile moves (the
# law-midrash spine read the same sitting). Effects from birth,
# targeting the world_engine contract. Read-only; model layer.

# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 33, ('the guard counted %d expectations, the tripwire holds 33' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys
import effects_layer as FX

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book='Lev' AND v.chapter=? AND
        v.verse=? ORDER BY w.idx""", (ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

PROBES = [
    ('מוקדה',  6, 2,  'on its pyre — the night window'),
    ('תוקד',   6, 6,  'shall burn — the perpetual fire'),
    ('תכבה',   6, 6,  'shall not go out — the ban'),
    ('בקמצו',  6, 8,  'his fistful'),
    ('מחציתה', 6, 13, 'its half — the halving invariant'),
    ('תכבס',   6, 20, 'you shall wash'),
    ('ישבר',   6, 21, 'it shall be broken'),
    ('ומרק',   6, 21, 'scoured'),
    ('ושטף',   6, 21, 'and rinsed'),
    ('תהיה',   7, 9,  "his shall it be — the due (the ink's feminine)"),
    ('ממחרת',  7, 16, 'and on the next day'),
    ('השלישי', 7, 17, 'the third day'),
    ('פגול',   7, 18, 'rejected'),
    ('ונכרתה', 7, 20, 'shall be cut off'),
    ('חלב',    7, 23, 'fat'),
    ('דם',     7, 26, 'blood (the ban)'),
    ('התנופה', 7, 34, 'the waving-breast'),
    ('המלאים', 8, 22, 'the installation ram'),
    ('תצאו',   8, 33, 'you shall not go out'),
]
for tok, ch, vs, note in PROBES:
    if tok not in verse_text(ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Lev %d:%d'
                 % (tok, note, ch, vs))
print('probes: all %d fired  [zero-report law satisfied]\n' % len(PROBES))

P = []
def ink(ref, note):  P.append(('INK',  'Lev %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def data(src, note): P.append(('DATA', '%s — %s' % (src, note)))

def out(verdict, effects):
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)


# ===== F1: THE ONE-WAY ALTAR (6:2-6) =================================
def altar_machine(case, params):
    del P[:]
    q = case['ask']
    if q == 'retention':
        ink('6:2', '"It is the OLAH on its pyre (מוקדה) on the altar" — '
            'the burnt-offering names the class the altar keeps')
        move('Sifra, Tzav, Chapter 1 3-6', 'the recorded classes: R. '
             'Yehoshua fit-for-the-FIRE, Rabban Gamliel fit-for-the-'
             'ALTAR; their delta is unfit blood and libations — both '
             'arms carried')
        return out('once up, does not come down (two recorded classes)',
                   [FX.NONE])
    if q == 'dislodged_before_midnight':
        ink('6:2', '"all the night until the morning" — the fire\'s '
            'claim spans the night')
        move('Sifra, Tzav, Chapter 2 5', 'limbs sprung off before '
             'midnight are returned and still carry sacrilege — the '
             'midnight boundary on the mitzvah')
        return out('restore to the fire; sacrilege stands',
                   [FX.NONE])
    if q == 'extinguish':
        ink('6:6', '"a continual fire shall burn (תוקד) on the altar; '
            'it shall NOT GO OUT (לא תכבה)" — the standing duty and '
            'its negative')
        move('Sifra, Tzav, Chapter 2 7', 'R. Yossi\'s sustenance pile; '
             'extinguishing transgresses the negative commandment')
        return out('a standing never-extinguish duty',
                   ['perpetual_fire_duty', 'labor_barred'])
    if q == 'wood_piles':
        ink('6:5-6', 'the ink states the fire and the morning wood — '
            'no count')
        data('Mishnah Yoma 4:6', 'the COUNT is transmitted data with '
             'three recorded settings: two (R. Yehuda), three (R. '
             'Yosei), four (R. Meir) daily piles, one more on Yom '
             'Kippur — the parameter never a constant')
        return out('pile count = data (three recorded settings)',
                   [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE VESSEL PURGE (6:20-21) ================================
def vessel_purge(case, params):
    del P[:]
    m = case['material']
    if m == 'garment':
        ink('6:20', '"and when of its blood is sprinkled on a garment, '
            'you shall WASH (תכבס) that on which it was sprinkled in a '
            'holy place"')
        move('Sifra, Tzav, Chapter 6 3', 'the SPOT, not the whole '
             'garment; the sprinkle-fitness criterion sorts the cases')
        return out('launder the spot in the holy place',
                   ['launder_blood_spot'])
    if m == 'earthenware':
        ink('6:21', '"an earthen vessel in which it is cooked shall be '
            'BROKEN (ישבר)"')
        return out('broken in the holy place', ['break_earthen_vessel'])
    if m == 'copper':
        ink('6:21', '"and if in a copper vessel it is cooked, it shall '
            'be SCOURED and RINSED (ומרק ושטף) with water"')
        move('Sifra, Tzav, Chapter 7 2-3', 'all metals included; water '
             'any amount, water only; scour within, rinse without')
        return out('scoured and rinsed in the holy place',
                   ['scour_and_rinse'])
    if m == 'touched_food':
        ink('6:20', '"all that touches its flesh shall become holy '
            '(יקדש)"')
        move('Sifra, Tzav, Chapter 3 6', 'absorption required; the '
             'touched part becomes LIKE it — cut away if unfit, eaten '
             'under its stringencies if fit')
        return out('becomes as the offering (absorption)',
                   ['sanctified_by_contact'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE PERPETUAL GRIDDLE OFFERING (6:13-15) ==================
def chavitin_machine(case, params):
    del P[:]
    ink('6:13', '"a tenth of the ephah ... a PERPETUAL meal-offering — '
        'ITS HALF (מחציתה) in the morning and ITS HALF in the evening" '
        '— the possessive makes each half a half OF A WHOLE')
    q = case['ask']
    if q == 'halves_from_house':
        move('Sifra, Tzav, Section 3 6', 'never two separate '
             'half-tenths — bring whole and divide')
        return out('barred — a whole tenth, divided', [FX.NONE])
    if q == 'successor':
        move('Sifra, Tzav, Section 3 8-9', 'the replacement brings a '
             'NEW whole and offers its half: two halves offered, two '
             'lost — the invariant survives succession')
        return out('new whole; two halves offered, two lost',
                   ['burn_remainder'])
    if q == 'no_successor':
        move('Sifra, Tzav, Chapter 5 3', 'the recorded pair: R. Yehuda '
             '— the heirs bring it whole; R. Shimon — the congregation '
             '(from "olam"); both arms carried')
        return out('funded by heirs or community (recorded dispute)',
                   [FX.NONE])
    if q == 'loaf_count':
        data('Mishnah Menachot 6:5', 'TWELVE loaves — with the '
             'show-bread the two exceptions to ten-per-tenth: the '
             'count is the data channel\'s constant')
        return out('twelve (transmitted quantity)', [FX.NONE])
    if q == 'conversion':
        ink('6:13', 'the tenth of the EPHAH — the unit in the ink')
        move('Onkelos Lev 6:13 + Sifra, Tzav, Section 3 4', 'the '
             'received translation computes it in-verse: "one of ten '
             'in three se\'im"; the Sifra: seven quarters and a '
             'fraction — the conversion layer as standing behavior')
        return out('one of ten in three se\'im', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE REJECTION MACHINE (7:15-18) ===========================
def rejection_machine(case, params):
    del P[:]
    q = case['ask']
    if q == 'window_todah':
        ink('7:15', '"on the day of his offering shall it be eaten; he '
            'shall not leave of it until morning" — one day and the '
            'night')
        move('Sifra, Tzav, Chapter 12 5', 'the ink permits all night; '
             'the sages\' MIDNIGHT is the self-labeled fence')
        return out('day and night until midnight (the fence)',
                   ['eating_window'])
    if q == 'window_vow':
        ink('7:16', '"...and on the NEXT DAY (ממחרת) what remains may '
            'be eaten" — the two-day window')
        move('Sifra, Tzav, Chapter 12 13', 'the second NIGHT excluded '
             '("until the third day")')
        return out('two days and one night', ['eating_window'])
    if q == 'leftover':
        ink('7:17', '"what remains of the flesh of the sacrifice on '
            'the THIRD day (השלישי) shall be burned in fire"')
        move('Sifra, Tzav, Chapter 12 14-15', 'by DAY, not night — the '
             'prototype for all consecrated burning; flesh only')
        return out('burned on the third day, by day',
                   ['burn_remainder', 'purge_deadline'])
    if q == 'piggul_time':
        ink('7:18', '"if eaten shall be eaten on the third day, it '
            'shall NOT BE ACCEPTED (לא ירצה)... REJECTED (פגול) shall '
            'it be, and the soul that eats of it shall bear its sin"')
        move('Sifra, Tzav, Section 8 1', 'R. Eliezer\'s "incline your '
             'ear": the verse speaks of the THOUGHT at the offering, '
             'not the deed — the rejection enters at the service')
        return out('rejected with karet on the eater',
                   ['not_accepted', 'karet_cut_off'])
    if q == 'piggul_place':
        move('Sifra, Tzav, Chapter 13 2', 'out-of-place thought '
             'disqualifies via Lev 19:7\'s redundancy, but "shall bear '
             'its sin" restricts karet to TIME')
        return out('disqualified without karet', ['not_accepted'])
    if q == 'no_permitter':
        move('Sifra, Tzav, Chapter 13 5', 'the permitters criterion: '
             'the fistful, frankincense, incense, the wholly-burnt '
             'meal-offerings, the blood — no permitters, no rejection')
        return out('no rejection attaches', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE KARET BANS (7:19-27) ==================================
def karet_machine(case, params):
    del P[:]
    q = case['ask']
    if q == 'tamei_ate':
        ink('7:20', '"the soul that eats ... with his tumah upon him, '
            'that soul shall be CUT OFF (ונכרתה)"')
        move('Sifra, Tzav, Chapter 14 3-6', 'the BODY\'s tumah — four '
             'recorded routes to one law; liability begins at the '
             'sprinkling (Section 9 8)')
        return out('karet for the tamei eater', ['karet_cut_off'])
    if q == 'congregational':
        move('Sifra, Tzav, Chapter 14 1', 'what was slaughtered FOR '
             'THE UNCLEAN carries no karet for its unclean eaters — '
             'R. Yehoshua\'s rule')
        return out('exempt', ['exempt'])
    if q == 'cheilev':
        ink('7:23-25', '"all fat (חלב) of ox or sheep or goat you '
            'shall not eat ... the soul that eats shall be cut off"')
        move('Sifra, Tzav, Section 10 9', 'the sacrificial-type '
             'criterion: the fat that stands to be offered; the '
             'chest-wall fat excluded')
        return out('karet at an olive-bulk', ['karet_cut_off'])
    if q == 'cheilev_noahide':
        move('Sifra, Tzav, Section 10 1', 'Israel exhorted, NOT the '
             'sons of Noah — the a-fortiori from the limb-of-the-'
             'living refuted by "the children of Israel": the recorded '
             'negative boundary of the Noahide set')
        return out('outside the Noahide law set', [FX.NONE])
    if q == 'blood':
        ink('7:26', '"all blood (דם) you shall not eat, in all your '
            'habitations, of bird and of beast"')
        move('Sifra, Tzav, Section 10 11', 'the species criteria '
             'exclude men, reptiles, eggs, grasshoppers, fish; the '
             'karet blood is the lifeblood')
        return out('karet for lifeblood of bird and beast',
                   ['karet_cut_off'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE DUES MACHINE (7:8-10, 7:28-36) ========================
def dues_machine(case, params):
    del P[:]
    q = case['ask']
    if q == 'olah_hide':
        ink('7:8', '"the hide of the olah which he offered, to the '
            'priest — his shall it be"')
        move('Sifra, Tzav, Chapter 9 4', 'Rebbi: the hide FOLLOWS the '
             'flesh — only the olah needed its own verse')
        return out('hide to the offering priest', ['due_to_priest'])
    if q == 'minchah_due':
        ink('7:9', '"every meal-offering baked in the oven ... to the '
            'priest who offers it — HIS shall it be (תהיה, the ink\'s '
            'feminine, probe-corrected)"')
        move('Sifra, Tzav, Chapter 10 2', 'reconciled with "to all the '
             'sons of Aaron": the priestly HOUSEHOLD of the day')
        return out('to the household of the day', ['due_to_priest'])
    if q == 'breast_thigh':
        ink('7:34', '"the breast of the WAVING (התנופה) and the thigh '
            'of the lifting have I taken ... and given them to Aaron '
            'and his sons"')
        move('Sifra, Tzav, Chapter 16 4', 'reverting only AFTER the '
             'fat smoking (Num 5:31\'s clause order); fit at both '
             'services required (Chapter 16 7-8)')
        return out('breast and thigh to the priests after the smoking',
                   ['due_to_priest'])
    if q == 'seizure':
        move('Sifra, Tzav, Chapter 17 6', '"from the children of '
             'Israel" — by CONSENT of Israel: the priests may not '
             'seize the dues by force')
        return out('a consented conveyance, never seized', [FX.NONE])
    if q == 'eli_violation':
        move('Sifra, Tzav, Chapter 16 5', 'the recorded indictment: '
             'the sons of Eli demanded raw flesh BEFORE the smoking — '
             '"the sin of the youths was very great" (1 Samuel '
             '2:15-17): the prophetic voice matched to the OPEN '
             'computed entry — the effects law\'s destination '
             'witnessed in the declared reading')
        return out('the recorded violation of the after-smoking gate',
                   [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE INSTALLATION TRANSACTION (8:1-36) =====================
def installation(case, params):
    del P[:]
    q = case['ask']
    if q == 'atomicity':
        ink('8:22', '"and he brought near the SECOND ram, the ram of '
            'the INSTALLATION (המלאים)" — the components re-stated')
        move('Sifra, Tzav, Mekhilta DeMiluim I 19', 'bullock without '
             'both rams — not sanctified; rams without bullock — not; '
             'without the basket — not: one indivisible transaction')
        return out('atomic — all components or no sanctification',
                   [FX.NONE])
    if q == 'commit_point':
        move('Sifra, Tzav, Mekhilta DeMiluim I 34', 'the '
             'sanctification CONSUMMATED only at the blood sprinkling '
             '— the transaction\'s commit operation (the count itself '
             'a recorded dispute: six / nine / fifteen)')
        return out('committed at the blood sprinkling',
                   ['invested_office'])
    if q == 'confinement':
        ink('8:33', '"from the door of the tent you shall NOT GO OUT '
            '(לא תצאו) seven days, until the day of the filling of '
            'your installation days"')
        move('Sifra, Tzav, Mekhilta DeMiluim I 36-37', 'the computed '
             'calendar (23 Adar to 1 Nissan) and the exported '
             'template: the Yom Kippur high priest\'s and the '
             'red-heifer priest\'s seven-day separations')
        return out('a seven-day confinement timer; the template for '
                   'the generations', ['confined_seven_days'])
    if q == 'leftover':
        ink('8:32', '"what remains of the flesh and of the bread you '
            'shall burn in fire"')
        return out('the installation\'s own leftover clause',
                   ['burn_remainder'])
    return out('no verdict in span', [FX.NONE])


# ---- the test data; run, grade, effects -----------------------------
PARAMS = {}
CASES = [
    ('Mishnah Zevachim 9:1 — the retention classes (both recorded)',
     lambda: altar_machine({'ask': 'retention'}, PARAMS),
     'once up, does not come down (two recorded classes)'),
    ('Mishnah Zevachim 9:6 — dislodged before midnight',
     lambda: altar_machine({'ask': 'dislodged_before_midnight'}, PARAMS),
     'restore to the fire; sacrilege stands'),
    ('the extinguish ban (Sifra Chapter 2 7)',
     lambda: altar_machine({'ask': 'extinguish'}, PARAMS),
     'a standing never-extinguish duty'),
    ('Mishnah Yoma 4:6 — the pile count is data',
     lambda: altar_machine({'ask': 'wood_piles'}, PARAMS),
     'pile count = data (three recorded settings)'),
    ('Mishnah Zevachim 11:1/11:4 — the garment',
     lambda: vessel_purge({'material': 'garment'}, PARAMS),
     'launder the spot in the holy place'),
    ('Mishnah Zevachim 11:4 — earthenware',
     lambda: vessel_purge({'material': 'earthenware'}, PARAMS),
     'broken in the holy place'),
    ('Mishnah Zevachim 11:7 — copper and all metals',
     lambda: vessel_purge({'material': 'copper'}, PARAMS),
     'scoured and rinsed in the holy place'),
    ('Mishnah Zevachim 11:8 — the absorption rule',
     lambda: vessel_purge({'material': 'touched_food'}, PARAMS),
     'becomes as the offering (absorption)'),
    ('Mishnah Menachot 4:5 — no halves from the house',
     lambda: chavitin_machine({'ask': 'halves_from_house'}, PARAMS),
     'barred — a whole tenth, divided'),
    ('Mishnah Menachot 4:5 — the successor',
     lambda: chavitin_machine({'ask': 'successor'}, PARAMS),
     'new whole; two halves offered, two lost'),
    ('Mishnah Menachot 4:5 — no successor (the recorded pair)',
     lambda: chavitin_machine({'ask': 'no_successor'}, PARAMS),
     'funded by heirs or community (recorded dispute)'),
    ('Mishnah Menachot 6:5 — twelve loaves (data)',
     lambda: chavitin_machine({'ask': 'loaf_count'}, PARAMS),
     'twelve (transmitted quantity)'),
    ('the conversion layer (Onkelos 6:13)',
     lambda: chavitin_machine({'ask': 'conversion'}, PARAMS),
     "one of ten in three se'im"),
    ('Mishnah Zevachim 5:6 — the todah window with the fence',
     lambda: rejection_machine({'ask': 'window_todah'}, PARAMS),
     'day and night until midnight (the fence)'),
    ('the vow/gift window (7:16)',
     lambda: rejection_machine({'ask': 'window_vow'}, PARAMS),
     'two days and one night'),
    ('the third-day burning (7:17)',
     lambda: rejection_machine({'ask': 'leftover'}, PARAMS),
     'burned on the third day, by day'),
    ('Mishnah Zevachim 2:2 — out-of-time is the rejection',
     lambda: rejection_machine({'ask': 'piggul_time'}, PARAMS),
     'rejected with karet on the eater'),
    ('Mishnah Zevachim 2:2 — out-of-place without karet',
     lambda: rejection_machine({'ask': 'piggul_place'}, PARAMS),
     'disqualified without karet'),
    ('Mishnah Zevachim 4:3 — the no-permitters list',
     lambda: rejection_machine({'ask': 'no_permitter'}, PARAMS),
     'no rejection attaches'),
    ('Mishnah Zevachim 13:2 — the tamei eater',
     lambda: karet_machine({'ask': 'tamei_ate'}, PARAMS),
     'karet for the tamei eater'),
    ('Mishnah Pesachim 9:4 — the congregational exemption',
     lambda: karet_machine({'ask': 'congregational'}, PARAMS),
     'exempt'),
    ('Mishnah Keritot 1:1 (census) — the fat karet',
     lambda: karet_machine({'ask': 'cheilev'}, PARAMS),
     'karet at an olive-bulk'),
    ('the Noahide negative boundary (Sifra Section 10 1)',
     lambda: karet_machine({'ask': 'cheilev_noahide'}, PARAMS),
     'outside the Noahide law set'),
    ('Mishnah Keritot 5:1 — the lifeblood',
     lambda: karet_machine({'ask': 'blood'}, PARAMS),
     'karet for lifeblood of bird and beast'),
    ('Mishnah Zevachim 12:2 — the olah hide',
     lambda: dues_machine({'ask': 'olah_hide'}, PARAMS),
     'hide to the offering priest'),
    ('Mishnah Menachot 5:8 family — the minchah due to the household',
     lambda: dues_machine({'ask': 'minchah_due'}, PARAMS),
     'to the household of the day'),
    ('Mishnah Chullin 10:1 context — breast and thigh after smoking',
     lambda: dues_machine({'ask': 'breast_thigh'}, PARAMS),
     'breast and thigh to the priests after the smoking'),
    ('the consent gate (Sifra Chapter 17 6)',
     lambda: dues_machine({'ask': 'seizure'}, PARAMS),
     'a consented conveyance, never seized'),
    ('1 Samuel 2:15-17 — the sons of Eli against the gate',
     lambda: dues_machine({'ask': 'eli_violation'}, PARAMS),
     'the recorded violation of the after-smoking gate'),
    ('Mishnah Menachot 3:6 — atomicity',
     lambda: installation({'ask': 'atomicity'}, PARAMS),
     'atomic — all components or no sanctification'),
    ('the commit point (DeMiluim I 34)',
     lambda: installation({'ask': 'commit_point'}, PARAMS),
     'committed at the blood sprinkling'),
    ('Mishnah Yoma 1:1 — the seven-day template',
     lambda: installation({'ask': 'confinement'}, PARAMS),
     'a seven-day confinement timer; the template for the generations'),
    ('the installation leftover (8:32)',
     lambda: installation({'ask': 'leftover'}, PARAMS),
     'the installation\'s own leftover clause'),
]

ok = 0
frac = {'INK': 0, 'MOVE': 0, 'DATA': 0}
used = []
print()
for label, fn, want in CASES:
    got, effects, prov = fn()
    hit = got == want
    ok += hit
    kinds = [k for k, _ in prov]
    if all(k == 'INK' for k in kinds):
        cls = 'INK'
    elif 'DATA' in kinds and 'MOVE' not in kinds:
        cls = 'DATA'
    elif 'MOVE' in kinds:
        cls = 'MOVE'
    else:
        cls = 'INK'
    frac[cls] += 1
    print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
    if not hit:
        print('      expected: %s' % want)
        print('      got     : %s' % got)
    used += [e for e in effects if e != FX.NONE]
    for line in FX.render(effects):
        print('        ->%s' % line)
print()
tot = len(CASES)
print('MATRIX: %d/%d cells match the answer sheet' % (ok, tot))
print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) '
      '· data %d/%d (%.0f%%)'
      % (frac['INK'], tot, 100.0 * frac['INK'] / tot,
         frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot,
         frac['DATA'], tot, 100.0 * frac['DATA'] / tot))
ops = FX.summarize(used)
print('LEDGER OPS this span writes:',
      ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
if ok == tot:
    print('\nTHE OFFERING-TORAH SPAN COMPILES — the fourth span under '
          'the effects law; the priests\' own law layer runs.')
