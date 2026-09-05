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
runs; the pesach-engine receipt is asserted, not assumed.
"""
import sqlite3, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
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
    # cross-book receipts
    ('[IMPORT] YK between-the-poles day',     'Lev', 16, 14, 'הכפרת'),
    ('[IMPORT] the altar horns DOUBLED',      'Exod', 27, 2, 'קרנתיו', 2),
    ('[IMPORT] on its FOUR corners',          'Exod', 27, 2, 'ארבע'),
    ('[IMPORT] firstborn flesh to priest',    'Num', 18, 18, 'ובשרם'),
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
print('probes: all %d ink-token probes fired (3 imports receipted) '
      '[zero-report law satisfied]' % fired)

# the pesach-engine receipt for row 8's routing
assert os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),
       'cold_run_pesach.py')), 'pesach engine missing — row 8 cannot route'
print('routing receipt: cold_run_pesach.py present for the paschal regime')

# ---- (1) THE DISPATCHER — compiled from the span's ink --------------
# Provenance tags: INK (bare span ink), MOVE (named recorded argument,
# opened this run), FENCE (the tradition's self-labeled safeguard),
# DATA (transmitted calibration, the second channel), IMPORT
# (cross-book receipt).
I, M, F, D, P = 'INK', 'MOVE', 'FENCE', 'DATA', 'IMPORT'

def cell(value, prov, why):
    return {'v': value, 'p': prov, 'why': why}

NORTH_LINK = 'Lev 6:18 + 7:2 doubled slaughter verb -> the olah\'s place; Lev 1:11 tzafona'
TWO_FOUR = 'Zevachim 53b:5 — saviv (around) vs ve-zarku (THROW), both Lev 1:5 ink: like a gamma, two that are four'
ANYWHERE = ('Zevachim 55b:1-2 — the tripled tent token (petach at Lev 3:2; '
            'lifnei at 3:8 + 3:13): itself, the sides, the side-of-sides; '
            '55b:3 asks about the petach/lifnei difference itself')
MIDNIGHT = 'ink bound = until morning (Lev 7:15); Mishnah Berakhot 1:1 tail self-labels the midnight cap: to distance from transgression'

def dispatch(offering):
    o = offering
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
         'remainder': cell('southern_base', D,
                           'which base is not stated in the span\'s ink; carried as transmitted geometry (open docket: the descent-path derivation)'),
         'eater': cell('male_priests', I, 'Lev 6:22 kol zachar ba-kohanim'),
         'eat_place': cell('within_hangings', I, 'Lev 6:19 be-makom kadosh — the courtyard'),
         'window': cell('day_night_to_midnight', F, MIDNIGHT),
        }
    if o == 'olah':
        return {
         'place': cell('north', I, 'Lev 1:11 tzafona (the flock\'s own verse; the span states it once and the link generalizes)'),
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
         'eater': cell('anyone', D,
                       'the flesh is the offerer\'s table (Lev 7:15 frame); the any-eater boundary carried as calibration'),
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
         'eater': cell('anyone', D, 'as the todah row'),
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
         'window': cell('two_days_one_night', M,
                        'paired to the shelamim clock (Lev 7:16-17) by the recorded analogy in the sugya family'),
         'pesach_regime': cell('night_only_to_midnight_registered', P,
                               'routed to the compiled pesach engine: Exod 12:8 night, 12:4 registered, 12:10 morning-burn + the fence [IMPORT]'),
        }
    return None

# ---- (2) TEST DATA — the Mishnah's own grid, read from the shelf ----
mz = json.load(open('<repo-old>/Data/mishnah_zevachim_he.json'))
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
 ('Zevachim 5:4', 'olah', {
   'place': 'north', 'applications': 'two_that_are_four',
   'procedure': 'flay_and_cut', 'disposition': 'wholly_to_fires'},
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
]

# ---- (3)+(5) run, grade, effects ------------------------------------
print()
total = ok = 0
frac = {'INK': 0, 'MOVE': 0, 'FENCE': 0, 'DATA': 0, 'IMPORT': 0}
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
      'fence %d/%d · data %d/%d · imports %d/%d' % (
      frac['INK'], n, 100 * frac['INK'] // n,
      frac['MOVE'], n, 100 * frac['MOVE'] // n,
      frac['FENCE'], n, frac['DATA'], n, frac['IMPORT'], n))
print('effects: all %d verdict rows carry REGISTERED effects '
      '[effects law satisfied]' % len(TESTS))
if ok == total:
    print()
    print('THE LEV 1-8 OFFERING ENGINE CONSOLIDATES — one dispatcher, '
          'the whole span, the tradition\'s own grid as the answer sheet; '
          'the place-link runs on the doubled verb, the blood counts on '
          'the around-vs-throw tension, and the midnight cap arrives '
          'self-labeled as a fence.')
else:
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')
