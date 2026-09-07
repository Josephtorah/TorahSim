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
assert GUARDED == 54, ('the guard counted %d expectations, the tripwire holds 54' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys
import effects_layer as FX
# the callees (cold) — the dependency-debt sitting (2026-09-06): the guilt
# offering's law (7:1-7) resolves its place, blood, fat, and eater through
# the offerings dispatcher; the meal offering's law (6:7-11) its fistful and
# remainder through the meal-offering engine. Until this sitting tzav
# imported nothing and named every offering type at thirty verses.
import io as _io, contextlib as _ctx
with _ctx.redirect_stdout(_io.StringIO()):
    import cold_run_offerings as OFF
    import cold_run_minchah as MIN
ASHAM_ROW = OFF.dispatch('communal_shelamim_and_asham')
ASHAM_FAT = OFF.dispatch('fat:lamb')
MIN_FIST = MIN.fistful('fistful_and_frankincense')
MIN_REM = MIN.remainder('soleth')
MIN_REM_SINNER = MIN.remainder('sinner')
print('routing receipts: cold_run_offerings CALLED — asham row place=%r applications=%r eater=%r; fat:lamb parts=%r tail=%r; '
      'cold_run_minchah CALLED — fistful(fistful_and_frankincense)=%r, remainder(soleth)=%r, remainder(sinner)=%r [IMPORT, live calls]'
      % (ASHAM_ROW['place']['v'], ASHAM_ROW['applications']['v'], ASHAM_ROW['eater']['v'], ASHAM_FAT['parts']['v'],
         ASHAM_FAT['tail']['v'], MIN_FIST['v'], MIN_REM['v'], MIN_REM_SINNER['v']))

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


# ===== F8: THE GUILT OFFERING'S LAW (7:1-7) — added 2026-09-06 ==========
# The dependency audit found 7:1-7 cited by no cell in any runner while
# the sliding-scale engine (Lev 5) and the leper's cleansing (Lev 14:12-13)
# both run on it. Compiled from the ink; the shared procedure fetched by
# LIVE CALL from the offerings dispatcher (the asham's row) and the fat
# inventory (the lamb's list — the asham is a ram, 7:3 names its tail).
def asham_law(case, params):
    del P[:]
    q = case['ask']
    if q == 'grade':
        ink('7:1', '"this is the law of the guilt offering: it is MOST HOLY '
            '(קדש קדשים)"')
        return out('most holy', ['most_holy'])
    if q == 'place':
        ink('7:2', '"in the place where they slaughter the OLAH they shall '
            'slaughter the asham" — the place-link, the verb doubled')
        move('cold_run_offerings.dispatch(communal_shelamim_and_asham) '
             '[IMPORT, live call]', 'place -> %r (Lev 1:11\'s north through '
             'the doubled verb)' % ASHAM_ROW['place']['v'])
        return out('north (CALLED offerings -> %s)' % ASHAM_ROW['place']['v'], ['accepted'])
    if q == 'blood':
        ink('7:2', '"and its blood he shall throw on the altar AROUND '
            '(סביב)"')
        move('cold_run_offerings [IMPORT, live call]', 'applications -> %r '
             '(Zevachim 53b:5\'s around-vs-throw)' % ASHAM_ROW['applications']['v'])
        return out('around = %s (CALLED offerings)' % ASHAM_ROW['applications']['v'], ['accepted'])
    if q == 'fat':
        ink('7:3-4', '"all its fat he shall offer: the FAT TAIL (האליה) and the '
            'fat covering the entrails, the two kidneys with their fat on '
            'the loins, the lobe on the liver" — the ram\'s list, the tail named')
        move('cold_run_offerings.dispatch(fat:lamb) [IMPORT, live call]',
             'parts -> %r, tail -> %r: the guilt offering\'s inventory IS the '
             'lamb\'s of Lev 3:9-10' % (ASHAM_FAT['parts']['v'], ASHAM_FAT['tail']['v']))
        same = ASHAM_FAT['tail']['v'] and 'fat_tail' in ASHAM_FAT['parts']['v']
        return out('the lamb\'s inventory, tail included (CALLED offerings fat:lamb: %s)'
                   % ('match' if same else 'MISMATCH'), ['smoked_to_the_lord'])
    if q == 'smoke':
        ink('7:5', '"and the priest shall turn them to smoke on the altar, a '
            'fire-offering to the LORD; it is an asham"')
        return out('turned to smoke as a fire-offering', ['smoked_to_the_lord'])
    if q == 'eater':
        ink('7:6', '"every MALE among the priests shall eat it, in a HOLY '
            'place shall it be eaten; it is most holy"')
        move('cold_run_offerings [IMPORT, live call]', 'eater -> %r, place -> %r, '
             'window -> %r (Mishnah Zevachim 5:5\'s row)' % (ASHAM_ROW['eater']['v'],
             ASHAM_ROW['eat_place']['v'], ASHAM_ROW['window']['v']))
        return out('%s within the hangings, a day and a night (CALLED offerings)' % ASHAM_ROW['eater']['v'],
                   ['due_to_priest', 'eating_window'])
    if q == 'one_law':
        ink('7:7', '"AS the sin offering, SO the guilt offering — ONE LAW for '
            'them; the priest who atones with it, his shall it be"')
        move('Sifra, Tzav, Chapter 9 1', 'the comparison\'s content: from '
             'profane stock, by day, with the right hand — and "one law" = '
             'HAND-LAYING for both; "the priest who atones" excludes the '
             'tevul yom, the atonement-lacking, the mourner')
        return out('as the sin offering: hand-laying, day, right hand; the atoning priest takes it',
                   ['due_to_priest'])
    if q == 'blood_entered_sanctuary':
        ink('7:7', '"as the sin offering, so the guilt offering" — the clause '
            'R. Eliezer reads')
        move('Mishnah Zevachim 8:11', 'bloods that entered the hall to atone: '
             'R. Akiva — all invalid; the sages — the sin offering alone (Lev '
             '6:23); R. ELIEZER — the guilt offering too, "as the chatat so the '
             'asham": a recorded three-way dispute, all arms carried')
        return out('DISPUTE: invalid for all (R. Akiva) / chatat alone (sages) / '
                   'chatat and asham (R. Eliezer, by 7:7)', ['disqualified'])
    if q == 'wrong_intent':
        ink('7:5', '"it (הוא) is an asham" — the pronoun sits AFTER the smoking')
        move('Sifra, Tzav, Section 5 5-8', 'R. Eliezer\'s analogy to the chatat '
             'refuted by word position: the chatat and the pesach carry "it" '
             'at the SLAUGHTER, the asham after the smoking — slaughtered '
             'wrong-intent it STAYS FIT (Mishnah Zevachim 1:1: valid, not '
             'credited)')
        return out('valid, not credited to the owner', ['accepted', 'not_accepted'])
    if q == 'precedence':
        ink('7:1-2', 'most holy, thrown around (two-that-are-four) — against '
            'the sin offering\'s FOUR HORNS and the base (4:25, 4:30)')
        move('Mishnah Zevachim 10:2, 10:5', 'the sin offering precedes the '
             'guilt offering (its blood on the four horns and the base); '
             'EXCEPT the leper\'s asham, which comes to make him fit')
        return out('chatat first, except the leper\'s asham', [FX.NONE])
    if q == 'age_and_price':
        move('Mishnah Zevachim 10:5', 'all guilt offerings come two years old '
             'and in silver shekels (Lev 5:15\'s "by your valuation in silver '
             'shekels" [IMPORT — cold_run_vayikra5\'s ram floor]) EXCEPT the '
             'nazirite\'s and the leper\'s: a year old, no shekel floor — Lev '
             '14:10\'s "lambs" beside "a ewe of its first year", the shekel '
             'phrase absent from 14:10-12 [the census]')
        return out('two-year-old in silver shekels, except the nazirite\'s and the leper\'s',
                   [FX.NONE])
    if q == 'leper_blood':
        ink('7:1', '"the LAW of the guilt offering" — one law for all guilt '
            'offerings')
        move('Sifra, Tzav, Section 5 1-2', 'the leper\'s asham included: its '
             'blood BELOW the red line like every asham; Lev 14:13\'s "as the '
             'chatat so the asham" defeated for blood placement by "the law"')
        return out('blood below the red line, the leper\'s included', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F9: THE MEAL OFFERING'S LAW (6:7-11) — added 2026-09-06 ===========
def minchah_law(case, params):
    del P[:]
    q = case['ask']
    if q == 'presentation':
        ink('6:7', '"the sons of Aaron shall bring it near BEFORE THE LORD, '
            'to the FRONT of the altar"')
        move('Sifra, Tzav, Section 2 4-5', 'the two clauses intersected — '
             '"before the LORD" and "in front of the altar" = the SOUTHWEST '
             'corner (R. Eliezer\'s two-verse resolution rule); fit priests, '
             'the sons not the daughters, all at once')
        return out('presented at the southwest corner by the sons of Aaron',
                   ['presented'])
    if q == 'fistful':
        ink('6:8', '"he shall lift from it in his FISTFUL (בקמצו) of the fine '
            'flour and of its oil and ALL the frankincense, and turn it to '
            'smoke, a memorial (אזכרתה)"')
        move('cold_run_minchah.fistful(fistful_and_frankincense) [IMPORT, '
             'live call]', '-> %r (Lev 2:2\'s own fistful, graded against '
             'Mishnah Menachot 1-3)' % MIN_FIST['v'])
        return out('the fistful with all the frankincense to the fire (CALLED minchah: %s)' % MIN_FIST['v'],
                   ['azkarah_to_fire'])
    if q == 'remainder':
        ink('6:9', '"the REMAINDER of it Aaron and his sons shall eat; '
            'UNLEAVENED shall it be eaten, in a HOLY place, in the court of '
            'the tent of meeting"')
        move('cold_run_minchah.remainder(soleth) [IMPORT, live call]',
             '-> %r (Lev 2:3, 2:10 — the remainder to the priests, most holy)'
             % MIN_REM['v'])
        return out('eaten unleavened in the court by Aaron and his sons (CALLED minchah: %s)' % MIN_REM['v'],
                   ['due_to_priest', 'most_holy'])
    if q == 'sinner_remainder':
        ink('6:9', 'the remainder eaten — one law for every meal offering '
            '(6:7 "the law of the meal offering")')
        move('cold_run_minchah.remainder(sinner) [IMPORT, live call]',
             '-> %r: Lev 5:13\'s "it shall be the priest\'s AS THE MEAL '
             'OFFERING" resolves here (Mishnah Menachot 6:1 lists the '
             'sinner\'s among the scooped)' % MIN_REM_SINNER['v'])
        return out('the sinner\'s remainder to the priests as every meal offering (CALLED minchah: %s)'
                   % MIN_REM_SINNER['v'], ['due_to_priest'])
    if q == 'leaven':
        ink('6:10', '"it shall NOT be baked LEAVENED"')
        move('Sifra, Tzav, Chapter 3 1', 'baking singled out to teach '
             'PER-OPERATION liability: kneading, rolling, baking each its own')
        return out('leaven barred, liable per operation', ['barred_from_it'])
    if q == 'most_holy_like':
        ink('6:10', '"their portion have I given it from My fire-offerings; '
            'it is MOST HOLY, AS the sin offering and AS the guilt offering"')
        move('Sifra, Tzav, Chapter 3 3-4', 'the two-anchor comparison: from '
             'profane stock, by day, with the right hand (as the chatat); the '
             'fistful taken not-for-its-name stays FIT (as the asham); R. '
             'Shimon partitions — the sinner\'s rides the chatat rule, the '
             'gift the asham rule (dual track)')
        return out('as the chatat in stock, day, hand; as the asham in wrong intent — R. Shimon partitions',
                   ['most_holy'])
    if q == 'every_male':
        ink('6:11', '"every MALE among the sons of Aaron shall eat it — a '
            'statute forever for your generations from the fire-offerings"')
        move('Sifra, Tzav, Chapter 3 5', '"every male" includes the BLEMISHED '
             'for apportionment; eaten only after the fire\'s part is burned')
        return out('every male priest, the blemished sharing, after the burning',
                   ['due_to_priest'])
    if q == 'contact':
        ink('6:11', '"whatever TOUCHES them shall become HOLY (יקדש)"')
        move('Sifra, Tzav, Chapter 3 6', 'absorption required ("in them"); '
             'partial contact taints the touched part only — he cuts it away; '
             '"becomes holy" = becomes LIKE it: unfit to unfit, fit under its '
             'stringencies')
        return out('becomes like it — absorption required, the touched part alone',
                   ['sanctified_by_contact'])
    return out('no verdict in span', [FX.NONE])


# ---- the test data; run, grade, effects -----------------------------
PARAMS = {}

# ---- THE WRAP (W3 THE OFFERING ENGINE, D9-iii, 2026-09-07) — the daemon and the scene --------------
# Nine case heads of the priests' law layer: the altar's fire (6:2, 6:6), the sin offering's blood and
# flesh absorbed (6:20-21), the high priest's perpetual griddle offering (6:13, 6:15), the holy flesh eaten
# (7:15-20 — the windows as TIMERS, the thought that rejects, the impure eater), the blood eaten (7:26-27),
# the priestly due claimed (7:8-9, 7:34 — the sons of Eli's open entry), the guilt offering's law (7:1-7),
# and the SECOND LAYER on the meal offering brought and leavened (6:7-11 beside law_minchah's Lev 2). The
# installation (Lev 8) stays the library's law_installation, registered beside on the scene. Never emits.
import world_engine as WE
def law_tzav(event, world):
    """Lev 6-7 (cold_run_tzav.py — the altar, the vessel purge, the perpetual griddle, the rejection, the karet bans, the dues, the guilt offering's law, the meal offering's law)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'altar_fire_tended':
        if event['act'] == 'extinguished':
            return [E_('perpetual_fire_duty', 'the-altar', value=altar_machine({'ask': 'extinguish'}, PARAMS)[0], law='F1 [INK 6:6 "a continual fire shall burn on the altar; it shall not go out"]'),
                    E_('labor_barred', event['tender'], value='extinguishing', law='F1 [INK 6:6 "it shall not go out" — the negative; Sifra Tzav Chapter 2 7]')]
        if event['act'] == 'limb_dislodged' and event['hour'] == 'before_midnight':
            return [E_('perpetual_fire_duty', 'the-altar', value=altar_machine({'ask': 'dislodged_before_midnight'}, PARAMS)[0], law='F1 [INK 6:2 "all the night until the morning"; Mishnah Zevachim 9:6 — returned to the fire]')]
        return [E_('perpetual_fire_duty', 'the-altar', value=altar_machine({'ask': 'retention'}, PARAMS)[0], law='F1 [INK 6:2 "it is the burnt offering on its pyre"; Mishnah Zevachim 9:1]')]
    if k == 'holy_absorbed':
        v = vessel_purge({'material': event['material']}, PARAMS)[0]
        m = event['material']
        if m == 'garment':
            return [E_('launder_blood_spot', event['vessel'], value=v, law='F2 [INK 6:20 "you shall wash that whereon it was sprinkled in a holy place"]')]
        if m == 'earthenware':
            return [E_('break_earthen_vessel', event['vessel'], value=v, law='F2 [INK 6:21 "the earthen vessel wherein it is boiled shall be broken"]')]
        if m == 'copper':
            return [E_('scour_and_rinse', event['vessel'], value=v, law='F2 [INK 6:21 "scoured and rinsed in water"]')]
        return [E_('sanctified_by_contact', event['vessel'], value=v, law='F2 [INK 6:20 "whatever touches its flesh shall become holy"]')]
    if k == 'perpetual_griddle_brought':
        if event['brought_by'] == 'successor':
            return [E_('burn_remainder', 'the-two-lost-halves', value=chavitin_machine({'ask': 'successor'}, PARAMS)[0], law='F3 [INK 6:15 "the anointed priest in his stead shall offer it"; Sifra Tzav Section 3 8-9 — two halves offered, two lost]')]
        return []                                                # the anointed's own whole tenth divided: nothing burned (Section 3 6) — the silence
    if k == 'holy_flesh_eaten':
        if event['eater_impure']:
            if event['slaughtered_for_impure']:
                return [E_('exempt', event['eater'], value=karet_machine({'ask': 'congregational'}, PARAMS)[0], law='F5 [Sifra Tzav Chapter 14 1 — slaughtered for the unclean: no karet for its unclean eaters]')]
            return [E_('karet_cut_off', event['eater'], cp='HEAVEN', value=karet_machine({'ask': 'tamei_ate'}, PARAMS)[0], law='F5 [INK 7:20 "with his impurity upon him... cut off"]')]
        if event['intent'] == 'time':
            return [E_('not_accepted', event['eater'], value=rejection_machine({'ask': 'piggul_time'}, PARAMS)[0], law='F4 [INK 7:18 "it shall not be accepted... rejected shall it be"]'),
                    E_('karet_cut_off', event['eater'], cp='HEAVEN', law='F4 [INK 7:18 "the soul that eats of it shall bear its sin"; Mishnah Keritot 1:1 — the rejected]')]
        if event['intent'] == 'place':
            return [E_('not_accepted', event['eater'], value=rejection_machine({'ask': 'piggul_place'}, PARAMS)[0], law='F4 [Sifra Tzav Chapter 13 2 — disqualified without karet]')]
        wk = 'window_todah' if event['offering_kind'] == 'todah' else 'window_vow'
        n = 1 if wk == 'window_todah' else 2
        if event['day'] - event['day0'] >= n:
            return [E_('not_accepted', event['eater'], value='eaten_past_the_window', law='F4 [INK 7:18 "on the third day it shall not be accepted"]'),
                    E_('karet_cut_off', event['eater'], cp='HEAVEN', law='F4 [INK 7:18 "shall bear its sin" — the leftover; Mishnah Keritot 1:1]')]
        return [E_('eating_window', event['offering'], due=event['day0'] + n, value=rejection_machine({'ask': wk}, PARAMS)[0], law='F4 [INK 7:15-16 — the TIMER to the window\'s close]'),
                E_('burn_remainder', event['offering'], due=event['day0'] + n, value=rejection_machine({'ask': 'leftover'}, PARAMS)[0], law='F4 [INK 7:17 "on the third day in fire"]'),
                E_('purge_deadline', event['offering'], due=event['day0'] + n, value='by_day_not_night', law='F4 [Sifra Tzav Chapter 12 14-15 — burned by day]')]
    if k == 'blood_eaten':
        if event['species'] in ('bird', 'beast'):
            return [E_('karet_cut_off', event['eater'], cp='HEAVEN', value=karet_machine({'ask': 'blood'}, PARAMS)[0], law='F5 [INK 7:26-27 "of fowl or of beast... cut off"]')]
        return []                                                # fish, locusts, eggs: outside the species criteria (Sifra Tzav Section 10 11) — the silence
    if k == 'priestly_due_claimed':
        if event['due'] == 'breast_thigh' and not event['after_smoking']:
            return []                                            # the sons of Eli's demand BEFORE the smoking (1 Samuel 2:15-17): no due yet — the OPEN entry
        if not event['by_consent']:
            return []                                            # seized, never conveyed (Sifra Tzav Chapter 17 6)
        ask = {'olah_hide': 'olah_hide', 'minchah': 'minchah_due', 'breast_thigh': 'breast_thigh'}[event['due']]
        return [E_('due_to_priest', event['claimant'], cp=event['offerer'], value=dues_machine({'ask': ask}, PARAMS)[0], law='F6 [INK 7:8, 7:9, 7:34 — the dues machine]')]
    if k == 'guilt_offering_brought':
        if event['blood_entered']:
            return [E_('disqualified', event['offering'], value=asham_law({'ask': 'blood_entered_sanctuary'}, PARAMS)[0], law='F8 [Mishnah Zevachim 8:11 — the three arms]')]
        out = [E_('most_holy', event['offering'], law='F8 [INK 7:1 "it is most holy"]'),
               E_('accepted', event['offerer'], cp='HEAVEN', value=asham_law({'ask': 'place'}, PARAMS)[0], law='F8 [INK 7:2 the place-link; the blood around — by call to the offering engine]'),
               E_('smoked_to_the_lord', event['offering'], value=asham_law({'ask': 'fat'}, PARAMS)[0], law='F8 [INK 7:3-5 the ram\'s fat, the tail named]'),
               E_('due_to_priest', 'the-priests', cp=event['offerer'], value=asham_law({'ask': 'eater'}, PARAMS)[0], law='F8 [INK 7:6 "every male among the priests"]'),
               E_('eating_window', event['offering'], due=event['day'] + 1, value='day_night_to_midnight', law='F8 [INK 7:6 with 7:15\'s window; Mishnah Zevachim 5:5]')]
        if event['intent'] == 'wrong':
            out.append(E_('not_accepted', event['offerer'], value=asham_law({'ask': 'wrong_intent'}, PARAMS)[0], law='F8 [Sifra Tzav Section 5 5-8 — valid, not credited]'))
        return out
    if k == 'meal_offering_brought':
        mk = event['meal_kind']
        out = [E_('presented', 'the-meal-offering', value=minchah_law({'ask': 'presentation'}, PARAMS)[0], law='F9 [INK 6:7 "before the LORD, to the front of the altar" — the southwest corner]'),
               E_('azkarah_to_fire', 'the-meal-offering', cp='HEAVEN', value=minchah_law({'ask': 'fistful'}, PARAMS)[0], law='F9 [INK 6:8]'),
               E_('sanctified_by_contact', 'the-meal-offering', value=minchah_law({'ask': 'contact'}, PARAMS)[0], law='F9 [INK 6:11 "whatever touches them shall become holy"]')]
        if mk != 'priests_own':
            out += [E_('due_to_priest', 'the-priests', cp=event['offerer'], value=minchah_law({'ask': 'sinner_remainder' if mk == 'sinner' else 'remainder'}, PARAMS)[0], law='F9 [INK 6:9 "the remainder Aaron and his sons shall eat"]'),
                    E_('most_holy', 'the-meal-offering', value=minchah_law({'ask': 'most_holy_like'}, PARAMS)[0], law='F9 [INK 6:10 "most holy, as the sin offering and as the guilt offering"]')]
        return out
    if k == 'meal_offering_leavened':
        if event['meal_kind'] in ('todah_loaves', 'two_loaves'):
            return []                                            # the leavened exceptions are Lev 7:13's and 23:17's own — nothing barred here
        return [E_('barred_from_it', event['baker'], value=minchah_law({'ask': 'leaven'}, PARAMS)[0], law='F9 [INK 6:10 "it shall not be baked leavened" — per operation: %s]' % event['step'])]
    return []

def scene():
    """THE SCENE — Lev 6-7's rows replayed with the installation's tape on the library daemon (clock unit: days)."""
    with _ctx.redirect_stdout(_io.StringIO()):
        w = WE.World(era='the priests\' law layer: Zevachim 2, 5, 8-9, 11-12, Menachot 4, 6, Keritot 1, 1 Samuel 2 on the engine (clock unit: days)')
        w.laws = [WE.law_installation, law_tzav]
        w.submit({'kind': 'installation_commanded', 'subject': 'aaron-and-sons', 'components': ['bullock', 'ram_olah', 'ram_milluim', 'basket'], 'case_source': 'Lev 8:2 — the take-list (the library daemon: Sifra Tzav Mekhilta DeMiluim I 19)'})
        w.submit({'kind': 'milluim_blood_sprinkled', 'subject': 'aaron-and-sons', 'case_source': 'Lev 8:30 — the commit (DeMiluim I 34)'})
        w.submit({'kind': 'milluim_leftover', 'subject': 'aaron-and-sons', 'case_source': 'Lev 8:32 — the leftover burned'})
        w.advance(1)
        w.submit({'kind': 'altar_fire_tended', 'subject': 'the-altar', 'tender': 'the-priest', 'act': 'kept', 'hour': 'night', 'case_source': 'Mishnah Zevachim 9:1 — once up does not come down'})
        w.submit({'kind': 'altar_fire_tended', 'subject': 'the-altar', 'tender': 'the-priest', 'act': 'limb_dislodged', 'hour': 'before_midnight', 'case_source': 'Mishnah Zevachim 9:6 — dislodged before midnight: returned to the fire'})
        w.submit({'kind': 'altar_fire_tended', 'subject': 'the-altar', 'tender': 'the-extinguisher', 'act': 'extinguished', 'hour': 'day', 'case_source': 'Sifra Tzav Chapter 2 7 — the extinguisher transgresses the negative'})
        for mat, ves, src in (('garment', 'the-garment', 'Mishnah Zevachim 11:1'), ('earthenware', 'the-pot', 'Mishnah Zevachim 11:7'), ('copper', 'the-cauldron', 'Mishnah Zevachim 11:7'), ('touched_food', 'the-touched-flesh', 'Mishnah Zevachim 11:8')):
            w.submit({'kind': 'holy_absorbed', 'subject': ves, 'vessel': ves, 'material': mat, 'case_source': src})
        w.submit({'kind': 'perpetual_griddle_brought', 'subject': 'the-high-priest', 'brought_by': 'the_anointed', 'halves': 'whole_divided', 'case_source': 'Mishnah Menachot 4:5 — a whole tenth divided: the silence'})
        w.submit({'kind': 'perpetual_griddle_brought', 'subject': 'the-successor', 'brought_by': 'successor', 'halves': 'new_whole', 'case_source': 'Mishnah Menachot 4:5 — the successor\'s new whole: two halves burned'})
        base = {'subject': 'the-shelamim', 'offering': 'the-shelamim', 'offering_kind': 'vow', 'day0': 1, 'day': 1, 'intent': 'none', 'eater_impure': False, 'slaughtered_for_impure': False}
        w.submit({'kind': 'holy_flesh_eaten', **base, 'subject': 'the-todah', 'offering': 'the-todah', 'offering_kind': 'todah', 'eater': 'the-todah-eater', 'case_source': 'Mishnah Zevachim 5:6 — a day and a night: the window TIMER'})
        w.submit({'kind': 'holy_flesh_eaten', **base, 'eater': 'the-shelamim-eater', 'case_source': 'Mishnah Zevachim 5:7 — two days and one night: the window TIMER'})
        w.submit({'kind': 'holy_flesh_eaten', **base, 'eater': 'the-late-eater', 'day': 3, 'case_source': 'Lev 7:18 — eaten on the third day: not accepted, karet'})
        w.submit({'kind': 'holy_flesh_eaten', **base, 'eater': 'the-piggul-eater', 'intent': 'time', 'case_source': 'Mishnah Zevachim 2:3 — the thought of time: rejected, karet'})
        w.submit({'kind': 'holy_flesh_eaten', **base, 'eater': 'the-place-thinker', 'intent': 'place', 'case_source': 'Mishnah Zevachim 2:3 — the thought of place: disqualified, no karet'})
        w.submit({'kind': 'holy_flesh_eaten', **base, 'eater': 'the-impure-eater', 'eater_impure': True, 'case_source': 'Lev 7:20; Mishnah Keritot 1:1 — the impure eater cut off'})
        w.submit({'kind': 'holy_flesh_eaten', **base, 'eater': 'the-congregational-eater', 'eater_impure': True, 'slaughtered_for_impure': True, 'case_source': 'Sifra Tzav Chapter 14 1 — slaughtered for the unclean: exempt'})
        w.submit({'kind': 'blood_eaten', 'subject': 'the-blood-eater', 'eater': 'the-blood-eater', 'species': 'beast', 'case_source': 'Mishnah Keritot 1:1 — the blood'})
        w.submit({'kind': 'blood_eaten', 'subject': 'the-fish-eater', 'eater': 'the-fish-eater', 'species': 'fish', 'case_source': 'Sifra Tzav Section 10 11 — fish blood outside: the silence'})
        w.submit({'kind': 'priestly_due_claimed', 'subject': 'the-officiating-priest', 'claimant': 'the-officiating-priest', 'offerer': 'the-offerer', 'due': 'olah_hide', 'after_smoking': True, 'by_consent': True, 'case_source': 'Lev 7:8; Sifra Tzav Chapter 9 4 — the hide to the offering priest'})
        w.submit({'kind': 'priestly_due_claimed', 'subject': 'the-officiating-priest', 'claimant': 'the-officiating-priest', 'offerer': 'the-offerer', 'due': 'breast_thigh', 'after_smoking': True, 'by_consent': True, 'case_source': 'Lev 7:34; Sifra Tzav Chapter 16 4 — after the smoking'})
        w.submit({'kind': 'priestly_due_claimed', 'subject': 'the-sons-of-eli', 'claimant': 'the-sons-of-eli', 'offerer': 'the-offerer', 'due': 'breast_thigh', 'after_smoking': False, 'by_consent': False, 'case_source': '1 Samuel 2:15-17 — raw flesh demanded BEFORE the smoking: no due, the open entry (Sifra Tzav Chapter 16 5)'})
        w.submit({'kind': 'guilt_offering_brought', 'subject': 'the-asham', 'offering': 'the-asham', 'offerer': 'the-guilty', 'intent': 'right', 'blood_entered': False, 'day': 1, 'case_source': 'Mishnah Zevachim 5:5 — the guilt offering\'s row'})
        w.submit({'kind': 'guilt_offering_brought', 'subject': 'the-misnamed-asham', 'offering': 'the-misnamed-asham', 'offerer': 'the-guilty', 'intent': 'wrong', 'blood_entered': False, 'day': 1, 'case_source': 'Mishnah Zevachim 1:1; Sifra Tzav Section 5 5-8 — wrong intent: valid, not credited'})
        w.submit({'kind': 'guilt_offering_brought', 'subject': 'the-entered-asham', 'offering': 'the-entered-asham', 'offerer': 'the-guilty', 'intent': 'right', 'blood_entered': True, 'day': 1, 'case_source': 'Mishnah Zevachim 8:11 — the blood that entered: the three arms'})
        w.submit({'kind': 'meal_offering_brought', 'subject': 'the-meal-offering', 'offerer': 'the-offerer', 'offerers': 'one', 'meal_kind': 'soleth', 'vow_words': 'a_meal_offering', 'case_source': 'Sifra Tzav Section 2 4-5; Mishnah Menachot 6:1 — the priests\' layer on the meal offering'})
        w.submit({'kind': 'meal_offering_brought', 'subject': 'the-meal-offering', 'offerer': 'the-offerer', 'offerers': 'one', 'meal_kind': 'sinner', 'vow_words': 'a_meal_offering', 'case_source': 'Lev 5:13 "as the meal offering" — the sinner\'s remainder (Mishnah Menachot 6:1)'})
        w.submit({'kind': 'meal_offering_leavened', 'subject': 'the-baker', 'baker': 'the-baker', 'meal_kind': 'soleth', 'step': 'kneading', 'case_source': 'Sifra Tzav Chapter 3 1 — per operation'})
        w.advance(8)                                                     # the windows close (days 2 and 3); the installation's seven days RELEASE on day 7
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('aaron-and-sons', 'confined_seven_days'), n('aaron-and-sons', 'invested_office'), n('aaron-and-sons', 'burn_remainder'), n('aaron-and-sons', 'released'),
            n('the-altar', 'perpetual_fire_duty'), n('the-extinguisher', 'labor_barred'), n('the-garment', 'launder_blood_spot'), n('the-pot', 'break_earthen_vessel'), n('the-cauldron', 'scour_and_rinse'), n('the-touched-flesh', 'sanctified_by_contact'),
            n('the-high-priest', 'burn_remainder'), n('the-two-lost-halves', 'burn_remainder'), n('the-todah', 'eating_window'), n('the-shelamim', 'eating_window'), n('the-shelamim', 'burn_remainder'), n('the-shelamim', 'purge_deadline'),
            n('the-late-eater', 'not_accepted'), n('the-late-eater', 'karet_cut_off'), n('the-piggul-eater', 'karet_cut_off'), n('the-place-thinker', 'not_accepted'), n('the-place-thinker', 'karet_cut_off'), n('the-impure-eater', 'karet_cut_off'), n('the-congregational-eater', 'exempt'),
            n('the-blood-eater', 'karet_cut_off'), n('the-fish-eater', 'karet_cut_off'), n('the-officiating-priest', 'due_to_priest'), n('the-sons-of-eli', 'due_to_priest'),
            n('the-asham', 'most_holy'), n('the-guilty', 'accepted'), n('the-guilty', 'not_accepted'), n('the-entered-asham', 'disqualified'), n('the-priests', 'due_to_priest'),
            n('the-meal-offering', 'presented'), n('the-meal-offering', 'sanctified_by_contact'), n('the-meal-offering', 'most_holy'), n('the-baker', 'barred_from_it'), tset, fired, w.clock.year), w
SCENE, _W = scene()

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
    # ---- F8: the guilt offering's law (7:1-7) — 2026-09-06 ----
    ('Lev 7:1 — most holy',
     lambda: asham_law({'ask': 'grade'}, PARAMS), 'most holy'),
    ('Mishnah Zevachim 5:5 — the asham slaughtered in the north (by call)',
     lambda: asham_law({'ask': 'place'}, PARAMS), 'north (CALLED offerings -> north)'),
    ('Mishnah Zevachim 5:5 — two applications that are four (by call)',
     lambda: asham_law({'ask': 'blood'}, PARAMS), 'around = two_that_are_four (CALLED offerings)'),
    ('Lev 7:3-4 against Lev 3:9-10 — the ram\'s fat list is the lamb\'s, tail included (by call)',
     lambda: asham_law({'ask': 'fat'}, PARAMS),
     'the lamb\'s inventory, tail included (CALLED offerings fat:lamb: match)'),
    ('Lev 7:5 — the fat parts to the fire',
     lambda: asham_law({'ask': 'smoke'}, PARAMS), 'turned to smoke as a fire-offering'),
    ('Mishnah Zevachim 5:5 — eaten by male priests within the hangings (by call)',
     lambda: asham_law({'ask': 'eater'}, PARAMS),
     'male_priests within the hangings, a day and a night (CALLED offerings)'),
    ('Sifra Tzav Chapter 9 1 — as the chatat so the asham: one law',
     lambda: asham_law({'ask': 'one_law'}, PARAMS),
     'as the sin offering: hand-laying, day, right hand; the atoning priest takes it'),
    ('Mishnah Zevachim 8:11 — blood that entered the sanctuary: the three arms',
     lambda: asham_law({'ask': 'blood_entered_sanctuary'}, PARAMS),
     'DISPUTE: invalid for all (R. Akiva) / chatat alone (sages) / chatat and asham (R. Eliezer, by 7:7)'),
    ('Mishnah Zevachim 1:1 / Sifra Section 5 8 — slaughtered wrong-intent: valid, not credited',
     lambda: asham_law({'ask': 'wrong_intent'}, PARAMS), 'valid, not credited to the owner'),
    ('Mishnah Zevachim 10:2, 10:5 — the chatat precedes, except the leper\'s asham',
     lambda: asham_law({'ask': 'precedence'}, PARAMS), 'chatat first, except the leper\'s asham'),
    ('Mishnah Zevachim 10:5 — two-year-old in silver shekels, the nazirite\'s and leper\'s excepted',
     lambda: asham_law({'ask': 'age_and_price'}, PARAMS),
     'two-year-old in silver shekels, except the nazirite\'s and the leper\'s'),
    ('Sifra Tzav Section 5 1-2 — the leper\'s asham: blood below like every asham',
     lambda: asham_law({'ask': 'leper_blood'}, PARAMS), 'blood below the red line, the leper\'s included'),
    # ---- F9: the meal offering's law (6:7-11) — 2026-09-06 ----
    ('Sifra Tzav Section 2 4-5 — presented at the southwest corner',
     lambda: minchah_law({'ask': 'presentation'}, PARAMS),
     'presented at the southwest corner by the sons of Aaron'),
    ('Mishnah Menachot 3:5 class — the fistful and the frankincense indispensable to each other (by call)',
     lambda: minchah_law({'ask': 'fistful'}, PARAMS),
     'the fistful with all the frankincense to the fire (CALLED minchah: indispensable_pair)'),
    ('Mishnah Menachot 6:1 — the remainder to the priests, most holy (by call)',
     lambda: minchah_law({'ask': 'remainder'}, PARAMS),
     'eaten unleavened in the court by Aaron and his sons (CALLED minchah: aaron_and_sons_most_holy)'),
    ('Mishnah Menachot 6:1 — the sinner\'s meal offering among the scooped (Lev 5:13 "as the meal offering", by call)',
     lambda: minchah_law({'ask': 'sinner_remainder'}, PARAMS),
     'the sinner\'s remainder to the priests as every meal offering (CALLED minchah: aaron_and_sons_most_holy)'),
    ('Sifra Tzav Chapter 3 1 — leaven barred per operation',
     lambda: minchah_law({'ask': 'leaven'}, PARAMS), 'leaven barred, liable per operation'),
    ('Sifra Tzav Chapter 3 3-4 — most holy as the chatat and as the asham',
     lambda: minchah_law({'ask': 'most_holy_like'}, PARAMS),
     'as the chatat in stock, day, hand; as the asham in wrong intent — R. Shimon partitions'),
    ('Sifra Tzav Chapter 3 5 — every male, the blemished sharing',
     lambda: minchah_law({'ask': 'every_male'}, PARAMS),
     'every male priest, the blemished sharing, after the burning'),
    ('Sifra Tzav Chapter 3 6 — whatever touches them becomes holy',
     lambda: minchah_law({'ask': 'contact'}, PARAMS),
     'becomes like it — absorption required, the touched part alone'),
    # ---- THE WRAP (W3, 2026-09-07) — the priests' law layer on the world engine, the installation's tape on the library daemon ----
    ('THE SCENE — (confined, invested, the leftover burned, RELEASED by the timer; the fire\'s duty x3, the extinguisher barred; the garment, '
     'the pot, the cauldron, the touched flesh; the anointed\'s silence, the successor\'s two halves; the thanksgiving\'s window, the peace '
     'offering\'s window, leftover, purge; the late eater, his karet, the rejected eater\'s karet, the place-thinker, his no-karet, the impure '
     'eater, the congregational exempt; the blood-eater, the fish-eater\'s silence; the priest\'s two dues, the sons of Eli\'s none; the guilt '
     'offering most holy, the guilty accepted twice, once not credited, the entered blood invalid, four dues; presented, contact, most holy, '
     'the baker barred; timers set, fired, the clock)',
     lambda: (SCENE, [FX.NONE], [('INK', 'the tape is the ink: Lev 6-8 and the recorded rows of Zevachim 2, 5, 8-9, 11-12, Menachot 4, 6, Keritot 1, 1 Samuel 2')]),
     (1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 4, 2, 2, 2, 1, 9, 9, 8)),
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
print('SCENE: %r — the daemons\' watch coverage (the library\'s law_installation beside law_tzav):' % (SCENE,))
_W.print_coverage()
if ok == tot:
    print('\nTHE OFFERING-TORAH SPAN COMPILES — the fourth span under '
          'the effects law; the priests\' own law layer runs.')
