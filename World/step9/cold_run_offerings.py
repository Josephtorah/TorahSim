#!/usr/bin/env python3
"""cold_run_offerings.py — THE LEV 1-8 OFFERING-ENGINE CONSOLIDATION
(2026-09-04, owner: "Commit push then 2" — the standing map's item 2).

ONE dispatcher compiled from the whole span's bare ink, graded against
the tradition's own consolidation table: Mishnah Zevachim 5:1-8
(where-is-the-place-of-the-offerings — every offering class, its
slaughter place, blood pattern, eater, place, and clock, in one grid).
The standing per-chapter compiles (cold_run_vayikra5.py 27/27,
cold_run_tzav.py 33/33) remain the case-law layer; THIS run is the
span-wide type dispatcher those chapters share.

The five motions, in order:
 (1) code from the BARE INK of Lev 1-8 alone — provenance [INK] on
     every ink-borne cell; the span's own PLACE LINK is the doubled
     slaughter verb of Lev 6:18 and 7:2 (the chatat and the asham
     are slaughtered "in the place where the OLAH is slaughtered"
     — the verb written TWICE in each verse), and the olah's place
     is Lev 1:11's own tzafona ("northward");
 (2) the Mishnah's grid collected as TEST DATA (Zevachim 5:1-8,
     read whole from the local shelf);
 (3) run;
 (4) misses filled by NAMED recorded arguments, each opened and
     labeled [MOVE ...] — this run's consultations: Zevachim 53b:5
     (two-applications-that-are-four born from the ink's own
     tension between saviv 'around' and ve-zarku 'and THROW', both
     tokens probed at Lev 1:5; R. Yishmael's alternative at 53b:6
     runs a verbal analogy to Lev 8:15 — OUR OWN derived span);
     Zevachim 53b:1 (the inner-chatat remainders to the WESTERN
     base — the school of R. Shimon b. Yochai, with the mnemonic);
     Zevachim 55a:3 (communal shelamim north by the Num 10:10
     pairing); Zevachim 55b:1-2 (light offerings ANYWHERE in the
     courtyard — the shelamim chapter's own TRIPLED tent token:
     petach 'the ENTRANCE' at Lev 3:2, lifnei 'BEFORE' at 3:8 and
     3:13 — one for itself, one for the sides, one for the
     side-of-sides; the probe layer caught the wrong-token guess
     here, the ink writes petach ONCE, and Zevachim 55b:3's own
     question is that very difference, closing with the
     open-doors rider); Zevachim 57a:1-4 (the base requirement
     taught by Lev 4:7's own el-yesod; the two-verses-as-one rule
     BARS extending two-that-are-four to the firstborn — it stays
     at ONE application); Mishnah Berakhot 1:1 (tail): the
     until-midnight cap SELF-LABELED — 'their commandment runs
     until dawn; why did the sages say until midnight? TO DISTANCE
     A MAN FROM TRANSGRESSION' — the fence's own signature, so the
     ink's until-morning bound (Lev 7:15) stands beneath a
     declared fence [FENCE];
 (5) the graded matrix printed with per-cell provenance, fractions,
     and EFFECTS on every verdict (the effects law: the verdict
     writes the LEDGER, never the event stream).

Cross-book receipts (labeled [IMPORT], the Mishpatim routing
pattern): Lev 16:14 (the Yom Kippur between-the-poles station —
that day's own code); Exod 27:2 (the altar's FOUR horns — the
count behind Lev 4:25's plural); Num 18:18 (the firstborn's flesh
to the priest); Lev 27:32 (the tithe, outside this span); the
paschal regime routed to the compiled pesach engine
(cold_run_pesach.py: Exod 12:4 registered, 12:8 night, 12:10
morning-burn) — cross-book grading #3.
Zero-report law: every claimed ink token is probed before anything
runs; the pesach-engine receipt is a LIVE CALL, not a file check.

SITTING A RECOMPILE (2026-09-05, the audit run before Numbers on the
owner's word; REVIEW_LEV1-8 items C, D, E, I, J — the ledger's
appended section names every segment opened):
 C  the todah and shelamim EATER cells are INK — Lev 7:19's own
    "and the flesh: every CLEAN person may eat flesh" (probed);
 D  the firstborn's two-days-one-night window names its segment:
    Zevachim 57a:5 (the baraita on Num 18:18 "LIKE the wave breast
    and LIKE the right thigh" — compared to the shelamim's breast
    and thigh), R. Akiva's restatement 57a:11, R. Yishmael's
    chain-limit objection 57a:14;
 E  the outer chatat's remainder = SOUTHERN base is no longer open
    data: Zevachim 53a:10-11 derives it from Lev 4:7's own el-yesod
    by "let his DESCENT from the ramp be learned from his EXIT from
    the sanctuary — to the base nearest him," and the ramp is SOUTH
    by Lev 1:11's own "on the SIDE of the altar northward" (Sifra
    Nedavah Section 5 8, seated LV01C-02); the R. Yishmael /
    R. Shimon b. Yochai dispute (53a:12) and Rav Asi's geometry
    (53a:14) recorded beside it — a MOVE;
 I  the pesach cell CALLS cold_run_pesach.paschal_procedure() and
    registration() and composes its value from their verdicts (the
    first-call standard of the Mishpatim -> Lev 24 call);
 J  the olah's north is graded TWICE — the flock's own verse (Lev
    1:11, INK) and the herd's, which the Sifra generalizes (Nedavah
    Chapter 7 6-7: "the north obtains in every olah," MOVE) — so the
    two provenances show instead of one label covering both.
The honest-pairing guard (compile_guards.py) runs first on this file.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sqlite3, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
import io as _io, contextlib as _ctx
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))

DB = (_ROOT + '/Data/tanakh.sqlite')
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def toks(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    # the place layer
    ('olah flock NORTHWARD (tzafona)',        'Lev', 1, 11, 'צפנה'),
    ('chatat place-link verb DOUBLED',        'Lev', 6, 18, 'תשחט', 2),
    ('asham place-link verb DOUBLED',         'Lev', 7,  2, 'ישחטו', 2),
    ('shelamim ENTRANCE of the tent (petach)', 'Lev', 3,  2, 'פתח'),
    ('shelamim BEFORE the tent #2 (lifnei)',   'Lev', 3,  8, 'לפני'),
    ('shelamim BEFORE the tent #3 (lifnei)',   'Lev', 3, 13, 'לפני'),
    # the blood layer
    ('olah blood AROUND (saviv)',             'Lev', 1,  5, 'סביב'),
    ('olah blood THROW (ve-zarku)',           'Lev', 1,  5, 'וזרקו'),
    ('shelamim blood around',                 'Lev', 3,  2, 'סביב'),
    ('asham blood around',                    'Lev', 7,  2, 'סביב'),
    ('inner chatat SEVEN sprinklings',        'Lev', 4,  6, 'שבע'),
    ('incense-altar horns (inner)',           'Lev', 4,  7, 'קרנות'),
    ('olah-altar base (el yesod)',            'Lev', 4,  7, 'יסוד'),
    ('outer chatat horns (leader)',           'Lev', 4, 25, 'קרנת'),
    ('outer chatat horns (commoner)',         'Lev', 4, 30, 'קרנת'),
    # disposal and procedure
    ('ash-pour place DOUBLED (shefekh)',      'Lev', 4, 12, 'שפך', 2),
    ('ash-pour: a PURE place',                'Lev', 4, 12, 'טהור'),
    ('olah FLAY (ve-hifshit)',                'Lev', 1,  6, 'והפשיט'),
    ('olah wholly — THE WHOLE (ha-kol)',      'Lev', 1,  9, 'הכל'),
    # the eating layer
    ('chatat eater: every MALE priest',       'Lev', 6, 22, 'זכר'),
    ('chatat eaten in a HOLY place',          'Lev', 6, 19, 'קדש'),
    ('asham eater: every male priest',        'Lev', 7,  6, 'זכר'),
    ('todah clock: nothing until MORNING',    'Lev', 7, 15, 'בקר'),
    ('vow/freewill: the NEXT DAY too',        'Lev', 7, 16, 'וממחרת'),
    ('the THIRD day — burn',                  'Lev', 7, 17, 'השלישי'),
    ('the wave breast (ha-tenufah)',          'Lev', 7, 34, 'התנופה'),
    ('every CLEAN person eats the flesh (C)', 'Lev', 7, 19, 'טהור'),
    ('olah flock: the SIDE of the altar (E)', 'Lev', 1, 11, 'ירך'),
    # cross-book receipts
    ('[IMPORT] YK between-the-poles day',     'Lev', 16, 14, 'הכפרת'),
    ('[IMPORT] the altar horns DOUBLED',      'Exod', 27, 2, 'קרנתיו', 2),
    ('[IMPORT] on its FOUR corners',          'Exod', 27, 2, 'ארבע'),
    ('[IMPORT] firstborn flesh to priest',    'Num', 18, 18, 'ובשרם'),
    ('[IMPORT] LIKE the wave breast (D)',     'Num', 18, 18, 'כחזה'),
    ('[IMPORT] and LIKE the right thigh (D)', 'Num', 18, 18, 'וכשוק'),
    # THE FAT INVENTORY (the dependency-debt sitting, 2026-09-06 — Lev 3:3-17
    # had been cited by no cell in any runner while four Lev 4 pointers named it)
    ('fat: the COVERING fat (the ox, 3:3)',           'Lev', 3,  3, 'המכסה'),
    ('fat: on the ENTRAILS, doubled (3:3)',           'Lev', 3,  3, 'הקרב', 2),
    ('fat: the TWO kidneys (3:4)',                    'Lev', 3,  4, 'הכלית'),
    ('fat: the LOBE on the liver (3:4)',              'Lev', 3,  4, 'היתרת'),
    ('fat: the lamb\'s FAT TAIL whole (3:9)',         'Lev', 3,  9, 'האליה'),
    ('fat: close by the BACKBONE (3:9)',              'Lev', 3,  9, 'העצה'),
    ('fat: the goat\'s covering fat (3:14, no tail)', 'Lev', 3, 14, 'המכסה'),
    ('fat: ALL fat is the LORD\'s (3:16)',            'Lev', 3, 16, 'חלב'),
    ('fat: the BAN — you shall not eat (3:17)',       'Lev', 3, 17, 'תאכלו'),
    ('fat: in ALL your dwellings (3:17)',             'Lev', 3, 17, 'מושבתיכם'),
    ('the asham\'s fat tail — a ram (7:3)',           'Lev', 7,  3, 'האליה'),
    ('the karet on the fat-eater (7:25)',             'Lev', 7, 25, 'ונכרתה'),
    ('blood of FOWL and BEAST (7:26)',                'Lev', 7, 26, 'לעוף'),
    ('4:10 AS lifted from the OX of the peace offering', 'Lev', 4, 10, 'משור'),
    ('4:26 AS the fat of the peace offering',         'Lev', 4, 26, 'כחלב'),
    ('4:35 AS the fat of the LAMB is removed',        'Lev', 4, 35, 'הכשב'),
]
fired = 0
for row in PROBES:
    label, book, ch, vs, tok = row[:5]
    need = row[5] if len(row) > 5 else 1
    ws = toks(book, ch, vs)
    hits = sum(1 for w in ws if tok in w)
    if hits < need:
        sys.exit('ZERO-REPORT LAW: probe %r wanted %d of %r at %s %d:%d, '
                 'found %d — refusing to run' % (label, need, tok, book, ch, vs, hits))
    fired += 1
print('probes: all %d ink-token probes fired (6 imports receipted) '
      '[zero-report law satisfied]' % fired)

# the pesach-engine receipt for row 8's routing — a LIVE CALL (item I):
# the pesach runner's functions import cold under its main guard; the
# cell's value is COMPOSED from the callee's verdicts, never recited.
import cold_run_pesach as PESACH
PESACH_CALLS = {
    'eating_time': PESACH.paschal_procedure({'ask': 'eating_time'}, PESACH.DATA)[0],
    'leftover':    PESACH.paschal_procedure({'ask': 'leftover'}, PESACH.DATA)[0],
    'nonregistrants': PESACH.registration({'ask': 'slaughter_for_nonregistrants'}, PESACH.DATA)[0],
}
print('routing receipt: cold_run_pesach CALLED — paschal_procedure(eating_time)=%r, '
      'paschal_procedure(leftover)=%r, registration(slaughter_for_nonregistrants)=%r'
      % (PESACH_CALLS['eating_time'], PESACH_CALLS['leftover'], PESACH_CALLS['nonregistrants']))

def pesach_regime_from_calls():
    """the cell's value composed from the callee: night-only-to-midnight
    from the eating_time verdict, registered-only from the registration
    verdict; anything else is returned as an honest UNRESOLVED string."""
    if (PESACH_CALLS['eating_time'] == 'night only, until midnight'
            and PESACH_CALLS['nonregistrants'] == 'invalid'):
        return 'night_only_to_midnight_registered'
    return 'UNRESOLVED:%s/%s' % (PESACH_CALLS['eating_time'], PESACH_CALLS['nonregistrants'])

# ---- (1) THE DISPATCHER — compiled from the span's ink --------------
# Provenance tags: INK (bare span ink), MOVE (named recorded argument,
# opened this run), FENCE (the tradition's self-labeled safeguard),
# DATA (transmitted calibration, the second channel), IMPORT
# (cross-book receipt).
I, M, F, D, P, H = 'INK', 'MOVE', 'FENCE', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled

def cell(value, prov, why):
    return {'v': value, 'p': prov, 'why': why}

NORTH_LINK = 'Lev 6:18 + 7:2 doubled slaughter verb -> the olah\'s place; Lev 1:11 tzafona'
TWO_FOUR = 'Zevachim 53b:5 — saviv (around) vs ve-zarku (THROW), both Lev 1:5 ink: like a gamma, two that are four'
ANYWHERE = ('Zevachim 55b:1-2 — the tripled tent token (petach at Lev 3:2; '
            'lifnei at 3:8 + 3:13): itself, the sides, the side-of-sides; '
            '55b:3 asks about the petach/lifnei difference itself')
MIDNIGHT = 'ink bound = until morning (Lev 7:15); Mishnah Berakhot 1:1 tail self-labels the midnight cap: to distance from transgression'
SOUTH_BASE = ('Zevachim 53a:10-11 — the baraita on Lev 4:7\'s own el-yesod: "this is the SOUTHERN base"; '
              '"let his DESCENT from the ramp be learned from his EXIT from the sanctuary — to the base nearest him"; '
              'the ramp is SOUTH by Lev 1:11\'s own al-yerekh... tzafona (Sifra Nedavah Section 5 8, seated LV01C-02); '
              'the dispute beside it — R. Yishmael western, R. Shimon b. Yochai southern (53a:12), Rav Asi\'s geometry (53a:14)')
BEKHOR_WINDOW = ('Zevachim 57a:5 — the baraita on Num 18:18 "and their flesh shall be yours LIKE the wave breast and LIKE the right thigh": '
                 'Scripture compares the firstborn to the shelamim\'s breast and thigh — as they are eaten two days and one night, so the firstborn; '
                 'R. Akiva\'s restatement 57a:11; R. Yishmael\'s chain-limit objection to the todah analogy 57a:14')
CLEAN_EATER = 'Lev 7:19 — "and the flesh: every CLEAN person may eat flesh" — the span\'s own eater clause for the light offerings'
HERD_NORTH = ('Sifra Nedavah Chapter 7 6-7 — valid without flaying, cutting, or hand-laying, INVALID without north, '
              '"for the north obtains in every olah": the flock\'s verse (1:11) generalized to the herd, whose own verses (1:3-9) state no north')

def dispatch(offering):
    o, _, variant = offering.partition(':')
    if o == 'scene':                     # W3 (2026-09-07): the grid replayed on the world engine — the scene as a dispatch key
        return {'scene': cell(SCENE, I, 'THE SCENE — Mishnah Zevachim 5:1-8\'s nine rows slaughtered on day 1 and the fat ban\'s two rows '
                              '(Chullin 8:6), the clock advanced to day 3 so every eating window closes and every leftover burns: '
                              '(accepted, dues to the priests, the bull wholly to the fire, the inner bull burned, the peace offering\'s '
                              'window, its leftover, the thanksgiving\'s leftover, the fat-eater barred, lashed, cut off, the hunter\'s '
                              'silence, timers set, timers fired, the clock)')}
    if o == 'inner_chatat_yk':
        return {
         'place': cell('north', I, NORTH_LINK),
         'stations': cell('poles+curtain+golden_altar', P,
                          'Lev 4:6-7 curtain + incense-altar horns [INK]; between-the-poles = Lev 16:14, that day\'s own code [IMPORT]'),
         'remainder': cell('western_base', M,
                           'Zevachim 53b:1 — school of R. Shimon b. Yochai: this and that, the western base'),
        }
    if o == 'inner_chatat_burned':
        return {
         'place': cell('north', I, NORTH_LINK),
         'stations': cell('curtain+golden_altar', I, 'Lev 4:6-7 / 4:17-18'),
         'remainder': cell('western_base', M, 'Zevachim 53b:1'),
         'burn_place': cell('ash_place', I,
                            'Lev 4:12 — outside the camp, a PURE place, the ash-pour (shefekh ha-deshen, doubled)'),
        }
    if o == 'outer_chatat':
        return {
         'place': cell('north', I, NORTH_LINK),
         'applications': cell('four_horns', P,
                              'Lev 4:25/4:30 horns [INK]; the count four = the altar\'s own build, Exod 27:2 [IMPORT]'),
         'remainder': cell('southern_base', M, SOUTH_BASE),
         'eater': cell('male_priests', I, 'Lev 6:22 kol zachar ba-kohanim'),
         'eat_place': cell('within_hangings', I, 'Lev 6:19 be-makom kadosh — the courtyard'),
         'window': cell('day_night_to_midnight', F, MIDNIGHT),
        }
    if o == 'olah':
        return {
         'place': (cell('north', M, HERD_NORTH) if variant == 'herd'
                   else cell('north', I, 'Lev 1:11 tzafona — the flock\'s own verse states it')),
         'applications': cell('two_that_are_four', M, TWO_FOUR),
         'procedure': cell('flay_and_cut', I, 'Lev 1:6 ve-hifshit ve-nitach'),
         'disposition': cell('wholly_to_fires', I, 'Lev 1:9 ve-hiktir... et ha-KOL'),
        }
    if o == 'communal_shelamim_and_asham':
        return {
         'place': cell('north', M,
                       'asham: Lev 7:2 place-link [INK]; communal shelamim: Zevachim 55a:3, the Num 10:10 pairing [MOVE]'),
         'applications': cell('two_that_are_four', M, TWO_FOUR + ' (asham saviv at Lev 7:2)'),
         'eater': cell('male_priests', I, 'Lev 7:6 kol zachar ba-kohanim'),
         'eat_place': cell('within_hangings', I, 'Lev 7:6 be-makom kadosh'),
         'window': cell('day_night_to_midnight', F, MIDNIGHT),
        }
    if o == 'todah_and_nazir_ram':
        return {
         'place': cell('anywhere_courtyard', M, ANYWHERE),
         'applications': cell('two_that_are_four', M, TWO_FOUR),
         'eater': cell('anyone', I, CLEAN_EATER),
         'eat_place': cell('all_city', D, 'the city boundary = transmitted geography (the camps mapping)'),
         'window': cell('day_night_to_midnight', F,
                        'INK: eaten on the day it is offered, nothing left until morning (Lev 7:15); the midnight cap is the fence'),
         'raised': cell('priests_household', I,
                        'Lev 7:31-34 — the wave breast and the raised thigh to Aaron and his sons, a perpetual due'),
        }
    if o == 'shelamim':
        return {
         'place': cell('anywhere_courtyard', M, ANYWHERE),
         'applications': cell('two_that_are_four', M, TWO_FOUR),
         'eater': cell('anyone', I, CLEAN_EATER),
         'eat_place': cell('all_city', D, 'as the todah row'),
         'window': cell('two_days_one_night', I,
                        'Lev 7:16-17 — eaten on its day AND the morrow; the THIRD day\'s remainder is burned'),
         'raised': cell('priests_household', I, 'Lev 7:31-34'),
        }
    if o == 'bekhor_maaser_pesach':
        return {
         'place': cell('anywhere_courtyard', M, ANYWHERE + ' (light offerings as a class)'),
         'applications': cell('one_against_base', M,
                              'Zevachim 57a:1-4 — el yesod (Lev 4:7) teaches the base; the two-verses-as-one rule BARS extending two-that-are-four: ONE stands'),
         'bekhor_eater': cell('priests', P, 'Num 18:18 — its flesh is yours [IMPORT]'),
         'maaser_eater': cell('anyone', P, 'Lev 27:32 outside this span [IMPORT]; the any-eater boundary as calibration'),
         'window': cell('two_days_one_night', M, BEKHOR_WINDOW),
         'pesach_regime': cell(pesach_regime_from_calls(), P,
                               'CALLED cold_run_pesach.paschal_procedure(eating_time) -> %r; registration(slaughter_for_nonregistrants) -> %r; '
                               'paschal_procedure(leftover) -> %r [IMPORT, live call — the first-call standard]'
                               % (PESACH_CALLS['eating_time'], PESACH_CALLS['nonregistrants'], PESACH_CALLS['leftover'])),
        }
    if o == 'fat':
        return fat_inventory(variant)
    return None

# ---- THE FAT INVENTORY — compiled from Lev 3:3-4 (the ox), 3:9-10 (the
# lamb), 3:14-15 (the goat) — the parts the peace offering's own verses
# name per species; the four Lev 4 pointers ("as it is lifted from the
# OX of the peace offering" 4:10; "as the fat of the peace offering"
# 4:26, 4:31; "as the fat of the LAMB is removed" 4:35) resolve HERE by
# live call (cold_run_chatat), and the guilt offering's list (7:3-4) is
# graded against the lamb's (cold_run_tzav). Added at the dependency-
# debt sitting (2026-09-06): the sub-span had been cited by no cell.
FAT_VERSES = {'ox': (3, 4), 'lamb': (9, 10), 'goat': (14, 15)}
def fat_parts(species):
    a, b = FAT_VERSES[species]
    ws = toks('Lev', 3, a) + toks('Lev', 3, b)
    parts = []
    if any('המכסה' in w for w in ws): parts.append('covering_fat')
    if sum(1 for w in ws if 'הקרב' in w) >= 2: parts.append('fat_on_entrails')
    if any(w in ('הכלית', 'הכליות') for w in ws): parts.append('two_kidneys_with_loin_fat')
    if any('היתרת' in w for w in ws): parts.append('lobe_of_liver')
    if any('האליה' in w for w in ws): parts.append('fat_tail_whole_by_backbone')
    return parts
# the tail token's census across the span: the lamb's verse and the asham's ram, nowhere else
TAIL_SEATS = [(c, v) for c in (3, 4, 7) for v in range(1, 39)
              if any('האליה' in w for w in toks('Lev', c, v))]
assert TAIL_SEATS == [(3, 9), (7, 3)], TAIL_SEATS
def fat_inventory(species):
    if species == 'ban':
        return {
         'sanction': cell('karet_and_lashes', M,
                          'Lev 3:17 "all fat and all blood you shall NOT EAT" [INK, the warning]; Lev 7:25 "the soul that eats... '
                          'shall be CUT OFF" [INK, the karet]; the lashes for the warning are the sheet\'s general rule '
                          '(Mishnah Makkot 3:2 lists the fat-eater; Keritot 1:1 the karet)'),
         'scope': cell('ox_sheep_goat', I, 'Lev 7:23 — "all fat of OX or SHEEP or GOAT you shall not eat": the ban\'s species '
                       'are the offerable three (Mishnah Chullin 8:6: the fat applies only to the pure beast)'),
         'blood_scope': cell('fowl_beast_and_wild', P, 'Lev 7:26 "of FOWL or of BEAST" [INK]; the wild animal from Lev 17:13 '
                             '[IMPORT — cold_run_sanctions.covering]: the blood wider than the fat (Chullin 8:6)'),
         'offered_hence_sacrilege': cell(True, I, 'Lev 3:16 "all fat is the LORD\'s" — the fat is OFFERED, so sacrilege, piggul, '
                                         'leftover, and impurity ride it (Chullin 8:6\'s own reason: "because the fat is offered")'),
         'dwellings': cell('all_dwellings', I, 'Lev 3:17 "in ALL your dwellings" — the eating ban is place-independent where the '
                           'altar acts are place-bound (Sifra Nedavah Chapter 20 6)'),
        }
    parts = fat_parts(species)
    a, b = FAT_VERSES[species]
    return {
     'parts': cell('+'.join(parts), I, 'Lev 3:%d-%d — the parts the %s\'s own verses name, read token by token' % (a, b, species)),
     'tail': cell('fat_tail_whole_by_backbone' in parts, I,
                  'the fat-tail token stands at %s only: the LAMB\'s verse (3:9, "the whole fat tail close by the backbone") and '
                  'the guilt offering\'s ram (7:3); the ox (3:3-4) and the goat (3:14-15 — its own paragraph, Sifra Nedavah '
                  'Chapter 20 1 reads the break as the exemption) have none' % (TAIL_SEATS,)),
     'smoke': cell('fire_offering_bread_pleasing_odor', I,
                   'Lev 3:5 "a fire-offering of pleasing odor"; 3:11 "BREAD of a fire-offering"; 3:16 "bread of a fire-offering '
                   'for a pleasing odor — all fat is the LORD\'s": the three smoke verbs (Sifra Nedavah Section 14 10: it / he / them)'),
     'pointer_4_10': cell(species == 'ox' and not ('fat_tail_whole_by_backbone' in parts), I,
                          'Lev 4:10 "as it is lifted from the OX of the peace offering" — the anointed priest\'s bull takes the ox\'s '
                          'list, no tail (Sifra Chovah Chapter 4 2-3)'),
     'pointer_4_35': cell(species == 'lamb' and ('fat_tail_whole_by_backbone' in parts), I,
                          'Lev 4:35 "as the fat of the LAMB is removed from the peace offering" — the individual\'s ewe takes the '
                          'lamb\'s list, TAIL INCLUDED: the pointer names the species whose inventory carries the tail'),
    }

# ---- THE WRAP (W3 THE OFFERING ENGINE, D9-iii, 2026-09-07) — the daemon and the scene --------------
# Two case heads: the offering slaughtered (Lev 1:2 the span's head; 1:5, 1:11, 3:2, 7:2 the slaughter
# clauses) — the dispatcher's row by kind writes the acceptance, the fire's part, the eater's due, and the
# eating window as a TIMER with the leftover's burning at its close; and the fat eaten (3:17, 7:23-25) —
# the ban's three species barred, lashed and cut off, the wild animal's fat the silence (Chullin 8:6).
# The daemon writes the ledger and never emits an event.
import world_engine as WE
def law_offerings(event, world):
    """Lev 1-7 (cold_run_offerings.py — the dispatcher's grid, the fat inventory, the fat ban)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'offering_slaughtered':
        row = dispatch(event['offering'])                        # the grid's key (olah:flock, shelamim...); the subject is the beast
        beast = event['subject']
        apps = row['applications']['v'] if 'applications' in row else row['stations']['v']
        out = [E_('accepted', event['offerer'], cp='HEAVEN', value='%s:%s' % (row['place']['v'], apps), law='[INK Lev 1:4 "and it shall be accepted for him"; the place and the blood the dispatcher\'s row by call: %s, %s]' % (row['place']['v'], apps))]
        if 'disposition' in row:
            out.append(E_('smoked_to_the_lord', beast, value=row['disposition']['v'], law='[INK Lev 1:9 "and the priest shall turn the whole to smoke on the altar"]'))
        else:
            out.append(E_('smoked_to_the_lord', beast, value='the_fat', law='[INK Lev 3:16 "all fat is the LORD\'s"; 7:5 the guilt offering\'s; 4:10 the sin offering\'s by the pointer]'))
        eater = row['eater']['v'] if 'eater' in row else (row['bekhor_eater']['v'] if 'bekhor_eater' in row else None)
        if eater in ('male_priests', 'priests'):
            out.append(E_('due_to_priest', 'the-priests', cp=event['offerer'], value=eater, law='[INK Lev 6:22, 7:6 "every male among the priests shall eat it"; Num 18:18 the firstling]'))
        elif 'raised' in row:
            out.append(E_('due_to_priest', 'the-priests', cp=event['offerer'], value='breast_and_thigh', law='[INK Lev 7:31-34 the wave breast and the raised thigh]'))
        if 'window' in row:
            n = 2 if row['window']['v'] == 'two_days_one_night' else 1
            out += [E_('eating_window', beast, due=event['day'] + n, value=row['window']['v'], law='[INK Lev 7:15 "on the day of his offering... until morning"; 7:16 "and on the morrow" — the TIMER to the window\'s close]'),
                    E_('burn_remainder', beast, due=event['day'] + n, value='the_leftover_burned', law='[INK Lev 7:17 "what remains of the flesh on the third day shall be burned in fire"; 6:23]')]
        if 'burn_place' in row:
            out.append(E_('burn_remainder', beast, value=row['burn_place']['v'], law='[INK Lev 4:12 "outside the camp to a pure place, to the ash-pour"; 6:23 "burned in fire"]'))
        return out
    if k == 'fat_eaten':
        ban = dispatch('fat:ban')
        if event['species'] in ban['scope']['v'].split('_'):
            return [E_('barred_from_it', event['eater'], value='the_fat_of_%s' % event['species'], law='[INK Lev 3:17, 7:23 "all fat of ox or sheep or goat you shall not eat" — the scope the fat inventory\'s row: %s]' % ban['scope']['v']),
                    E_('lashes', event['eater'], amount=40, law='[Mishnah Makkot 3:2 — the fat-eater among the lashed; the warning Lev 7:23]'),
                    E_('karet_cut_off', event['eater'], cp='HEAVEN', law='[INK Lev 7:25 "the soul that eats shall be cut off from its people"; Mishnah Keritot 1:1]')]
        return []                                                # the wild animal's fat is outside the ban (Mishnah Chullin 8:6) — the silence
    return []

def scene():
    """THE SCENE — Mishnah Zevachim 5:1-8's grid replayed on the world engine (clock unit: days); the fat ban's two rows beside it."""
    with _ctx.redirect_stdout(_io.StringIO()):
        w = WE.World(era='the offerings\' grid: Zevachim 5:1-8 and Chullin 8:6 on the engine (clock unit: days)')
        w.laws = [law_offerings]
        w.advance(1)
        for off, subj, src in (('inner_chatat_yk', 'the-day-of-atonement-goat', 'Mishnah Zevachim 5:1'), ('inner_chatat_burned', 'the-anointed-priests-bull', 'Mishnah Zevachim 5:2'),
                               ('outer_chatat', 'the-she-goat', 'Mishnah Zevachim 5:3'), ('olah:herd', 'the-bull-olah', 'Mishnah Zevachim 5:4'), ('olah:flock', 'the-lamb-olah', 'Mishnah Zevachim 5:4'),
                               ('communal_shelamim_and_asham', 'the-asham', 'Mishnah Zevachim 5:5'), ('todah_and_nazir_ram', 'the-todah', 'Mishnah Zevachim 5:6'),
                               ('shelamim', 'the-shelamim', 'Mishnah Zevachim 5:7'), ('bekhor_maaser_pesach', 'the-firstling', 'Mishnah Zevachim 5:8')):
            w.submit({'kind': 'offering_slaughtered', 'subject': subj, 'offering': off, 'offerer': 'the-offerer', 'day': 1, 'case_source': src + ' — the grid\'s row (%s)' % off})
        w.submit({'kind': 'fat_eaten', 'subject': 'the-fat-eater', 'eater': 'the-fat-eater', 'species': 'ox', 'case_source': 'Mishnah Chullin 8:6 + Keritot 1:1 — the ox\'s fat'})
        w.submit({'kind': 'fat_eaten', 'subject': 'the-hunter', 'eater': 'the-hunter', 'species': 'deer', 'case_source': 'Mishnah Chullin 8:6 — the wild animal\'s fat is permitted: the silence'})
        w.advance(3)                                                     # the day-and-night windows close on day 2, the two-day windows on day 3: the timers FIRE
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-offerer', 'accepted'), n('the-priests', 'due_to_priest'), n('the-bull-olah', 'smoked_to_the_lord'), n('the-anointed-priests-bull', 'burn_remainder'),
            n('the-shelamim', 'eating_window'), n('the-shelamim', 'burn_remainder'), n('the-todah', 'burn_remainder'),
            n('the-fat-eater', 'barred_from_it'), n('the-fat-eater', 'lashes'), n('the-fat-eater', 'karet_cut_off'), n('the-hunter', 'barred_from_it'), tset, fired, w.clock.day), w
SCENE, _W = scene()

# ---- (2) TEST DATA — the Mishnah's own grid, read from the shelf ----
mz = json.load(open((_ROOT + '/Data/mishnah_zevachim_he.json')))
mzt = mz['text'] if isinstance(mz, dict) and 'text' in mz else mz
ch5 = mzt[4]
assert len(ch5) == 8, 'Zevachim ch.5 must hold eight rows'
GRID_CHECKS = [  # (mishnah 1-based, token that must stand in its ink)
    (1, 'הבדים'), (1, 'מערבי'),          # between the poles; western base
    (2, 'הדשן'),                          # the ash house
    (3, 'קרנות'), (3, 'דרומי'), (3, 'חצות'),  # four horns; southern; midnight
    (4, 'ארבע'), (4, 'הפשט'),             # two-that-are-four; flaying
    (5, 'אשמות'), (5, 'חצות'),            # the ashamot list; midnight
    (6, 'העיר'), (6, 'חצות'),             # all the city; midnight
    (7, 'ימים'),                          # two days
    (8, 'אחת'), (8, 'חצות'), (8, 'למנויו'),  # one application; midnight; registered
]
for m1, tok in GRID_CHECKS:
    assert tok in strip(ch5[m1 - 1]), 'answer-grid check failed: %r not in Zevachim 5:%d' % (tok, m1)
print('answer sheet: Mishnah Zevachim 5:1-8 read whole; %d grid tokens verified in its own ink' % len(GRID_CHECKS))

TESTS = [
 ('Zevachim 5:1', 'inner_chatat_yk', {
   'place': 'north', 'stations': 'poles+curtain+golden_altar',
   'remainder': 'western_base'}, ['accepted']),
 ('Zevachim 5:2', 'inner_chatat_burned', {
   'place': 'north', 'stations': 'curtain+golden_altar',
   'remainder': 'western_base', 'burn_place': 'ash_place'},
   ['accepted', 'burn_remainder']),
 ('Zevachim 5:3', 'outer_chatat', {
   'place': 'north', 'applications': 'four_horns',
   'remainder': 'southern_base', 'eater': 'male_priests',
   'eat_place': 'within_hangings', 'window': 'day_night_to_midnight'},
   ['accepted', 'due_to_priest', 'eating_window']),
 ('Zevachim 5:4', 'olah:flock', {
   'place': 'north', 'applications': 'two_that_are_four',
   'procedure': 'flay_and_cut', 'disposition': 'wholly_to_fires'},
   ['accepted']),
 ('Zevachim 5:4', 'olah:herd', {
   'place': 'north'},
   ['accepted']),
 ('Zevachim 5:5', 'communal_shelamim_and_asham', {
   'place': 'north', 'applications': 'two_that_are_four',
   'eater': 'male_priests', 'eat_place': 'within_hangings',
   'window': 'day_night_to_midnight'},
   ['accepted', 'due_to_priest', 'eating_window']),
 ('Zevachim 5:6', 'todah_and_nazir_ram', {
   'place': 'anywhere_courtyard', 'applications': 'two_that_are_four',
   'eater': 'anyone', 'eat_place': 'all_city',
   'window': 'day_night_to_midnight', 'raised': 'priests_household'},
   ['accepted', 'due_to_priest', 'eating_window']),
 ('Zevachim 5:7', 'shelamim', {
   'place': 'anywhere_courtyard', 'applications': 'two_that_are_four',
   'eater': 'anyone', 'eat_place': 'all_city',
   'window': 'two_days_one_night', 'raised': 'priests_household'},
   ['accepted', 'due_to_priest', 'eating_window', 'burn_remainder']),
 ('Zevachim 5:8', 'bekhor_maaser_pesach', {
   'place': 'anywhere_courtyard', 'applications': 'one_against_base',
   'bekhor_eater': 'priests', 'maaser_eater': 'anyone',
   'window': 'two_days_one_night',
   'pesach_regime': 'night_only_to_midnight_registered'},
   ['accepted', 'due_to_priest', 'eating_window']),
 # ---- THE FAT INVENTORY (2026-09-06, the dependency-debt sitting) ----
 ('Tamid 4:3', 'fat:lamb', {
   'parts': 'covering_fat+fat_on_entrails+two_kidneys_with_loin_fat+lobe_of_liver+fat_tail_whole_by_backbone',
   'tail': True, 'smoke': 'fire_offering_bread_pleasing_odor', 'pointer_4_35': True},
   ['smoked_to_the_lord']),
 ('Sifra Nedavah Ch 20 1', 'fat:goat', {
   'parts': 'covering_fat+fat_on_entrails+two_kidneys_with_loin_fat+lobe_of_liver',
   'tail': False, 'pointer_4_10': False, 'pointer_4_35': False},
   ['smoked_to_the_lord']),
 ('Sifra Chovah Ch 4 2-3', 'fat:ox', {
   'parts': 'covering_fat+fat_on_entrails+two_kidneys_with_loin_fat+lobe_of_liver',
   'tail': False, 'pointer_4_10': True},
   ['smoked_to_the_lord']),
 ('Chullin 8:6', 'fat:ban', {
   'sanction': 'karet_and_lashes', 'scope': 'ox_sheep_goat',
   'blood_scope': 'fowl_beast_and_wild', 'offered_hence_sacrilege': True,
   'dwellings': 'all_dwellings'},
   ['barred_from_it', 'karet_cut_off', 'lashes']),
 # ---- THE WRAP (W3, 2026-09-07) — the grid replayed on the world engine: (accepted, dues, the bull wholly, the inner bull burned,
 # the peace offering's window, its leftover, the thanksgiving's leftover, the fat-eater barred, lashed, cut off, the hunter's silence,
 # timers set, timers fired, the clock)
 ('THE SCENE', 'scene', {
   'scene': (9, 5, 1, 1, 1, 1, 1, 1, 1, 1, 0, 10, 10, 3)},
   ['accepted', 'smoked_to_the_lord', 'due_to_priest', 'eating_window', 'burn_remainder', 'barred_from_it', 'lashes', 'karet_cut_off']),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
assert len(TESTS) == GUARDED, 'guard counted %d tests, table holds %d' % (GUARDED, len(TESTS))
print('guard: %d test rows, every expected value a literal from the answer sheet '
      '[honest-pairing guard satisfied]' % GUARDED)
print()
total = ok = 0
frac = {'INK': 0, 'MOVE': 0, 'FENCE': 0, 'DATA': 0, 'IMPORT': 0, 'HYPOTHESIS': 0}
effects_used = []
for src, off, expected, effs in TESTS:
    got = dispatch(off)
    assert got is not None, 'no dispatch row for %r' % off
    line_ok = True
    for field, want in expected.items():
        total += 1
        c = got.get(field)
        hit = c is not None and c['v'] == want
        ok += hit
        line_ok &= hit
        if c:
            frac[c['p']] += 1
        mark = 'OK ' if hit else 'MISS'
        print('%s %-11s %-28s [%s] %s' % (mark, src, field + '=' + str(want),
              c['p'] if c else '??', '' if hit else 'got=%r' % (c and c['v'])))
    FX.validate(effs)
    effects_used += effs
    print('     %-11s effects: %s' % (src, ', '.join(effs)))
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, total))
n = total
print('FRACTIONS: pure ink %d/%d (%d%%) · named moves %d/%d (%d%%) · '
      'fence %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d' % (
      frac['INK'], n, 100 * frac['INK'] // n,
      frac['MOVE'], n, 100 * frac['MOVE'] // n,
      frac['FENCE'], n, frac['DATA'], n, frac['IMPORT'], n, frac['HYPOTHESIS'], n))
print('effects: all %d verdict rows carry REGISTERED effects '
      '[effects law satisfied]' % len(TESTS))
print('SCENE: %r — the grid on the engine; the daemon\'s watch coverage:' % (SCENE,))
_W.print_coverage()
if ok == total:
    print()
    print('THE LEV 1-8 OFFERING ENGINE CONSOLIDATES — one dispatcher, '
          'the whole span, the tradition\'s own grid as the answer sheet; '
          'the place-link runs on the doubled verb, the blood counts on '
          'the around-vs-throw tension, the midnight cap arrives '
          'self-labeled as a fence, the eater is the ink\'s own CLEAN '
          'person, the southern base descends the ramp, and the pesach '
          'cell is answered by a call into its own engine.')
else:
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')
