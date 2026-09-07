#!/usr/bin/env python3
"""cold_run_minchah.py — THE MEAL OFFERING AND THE BIRD BURNT OFFERING
(2026-09-05, sitting B of the audit — REVIEW_LEV1-8 item B: the two
pieces of Leviticus 1-2 that had NO compiled function anywhere).

Spans: Lev 2:1-16 (the offerer's meal offering — five kinds, the
adjuncts, the fistful and its memorial, the remainder, the leaven and
honey bans, the salt, the first-fruits offering) and Lev 1:14-17 (the
bird burnt offering — the species, the pinching, the blood pressed on
the wall, the crop to the ash place, the rending without dividing).
Mishnah Zevachim 5's grid has no row for either (the consolidation's
honest gap): the meal offering's answer sheet is MISHNAH MENACHOT,
routed BY TOPIC under the union rule and read whole (93 rows, the
ledger logic/oral_triage/menachot_topic_docket_2026-09-05.md); the
bird's is Zevachim 6-7 (13 rows, the same ledger).

The five motions, in order:
 (1) code from the BARE INK — the five kinds counted by their own
     tokens, the adjunct verbs censused per kind, the three oil
     forms, the fistful's subject and measure, the memorial token
     three times, 'most holy' twice, the salt token three times in
     one verse, the doubled 'you shall offer' at 2:14, and the bird's
     four verbs; every quantity a PARAMETER (the tenth, the log, the
     sixty are the data channel — and Mishnah Menachot 12:4 labels it
     itself: 'all the measures of the sages are so');
 (2) the Mishnah's rows as TEST DATA, each expected value a literal
     typed from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Sifra's rows
     (this chapter's spine, verdicted 2026-09-03 and re-addressed in
     sitting A) and the Talmud where opened, each labeled [MOVE];
 (5) the graded matrix with per-cell provenance, fractions, and
     EFFECTS on every verdict (eight effects discovered in this
     sitting's verbs: azkarah_to_fire, most_holy, salted, presented,
     pinched, crop_cast_to_ash_place — and two for the sister
     compiles).

Cross-span receipts, labeled [IMPORT] and, where a compiled callee
exists, CALLED: Lev 5:11 (the sinner's meal offering — no oil, no
frankincense, 'it is a sin offering') through cold_run_vayikra5's
graded_offering(); Lev 6:16 (the priest's meal offering wholly
burned); Lev 7:13 and 23:17 (the two leavened exceptions); Lev 23:10-11
(the omer's land and waving); Lev 24:7 (the showbread's frankincense);
Num 15:4 (the libation meal offering's oil); Num 5:25 (the jealousy
offering's waving); Exod 27:20 (pure beaten oil FOR THE LIGHT);
Lev 14:21 (the log); Lev 5:8 (the bird sin offering's 'not divide').
"""
import sqlite3, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def toks(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]

def count(book, ch, vs, tok):
    return sum(1 for w in toks(book, ch, vs) if tok in w)

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    # the caller and the first kind
    ('a SOUL — the singular caller',            'Lev', 2, 1, 'ונפש'),
    ('fine flour (soleth)',                     'Lev', 2, 1, 'סלת'),
    ('he shall POUR oil',                       'Lev', 2, 1, 'ויצק'),
    ('he shall PUT frankincense',               'Lev', 2, 1, 'לבנה'),
    # the fistful
    ('to the PRIESTS (the scooper\'s subject)', 'Lev', 2, 2, 'הכהנים'),
    ('and he shall SCOOP',                      'Lev', 2, 2, 'וקמץ'),
    ('his FULL fist',                           'Lev', 2, 2, 'קמצו'),
    ('with ALL its frankincense',               'Lev', 2, 2, 'לבנתה'),
    ('its MEMORIAL (azkarah) #1',               'Lev', 2, 2, 'אזכרתה'),
    ('the REMAINDER to Aaron and his sons',     'Lev', 2, 3, 'והנותרת'),
    ('MOST HOLY #1',                            'Lev', 2, 3, 'קדשים'),
    # the vessel kinds
    ('the OVEN kind',                           'Lev', 2, 4, 'תנור'),
    ('cakes MIXED with oil',                    'Lev', 2, 4, 'בלולת'),
    ('wafers ANOINTED with oil',                'Lev', 2, 4, 'משחים'),
    ('the GRIDDLE kind',                        'Lev', 2, 5, 'המחבת'),
    ('griddle: mixed',                          'Lev', 2, 5, 'בלולה'),
    ('BREAK it in pieces',                      'Lev', 2, 6, 'פתות'),
    ('griddle: pour oil on it',                 'Lev', 2, 6, 'ויצקת'),
    ('the PAN kind (marcheshet)',               'Lev', 2, 7, 'מרחשת'),
    ('pan: made IN oil',                        'Lev', 2, 7, 'בשמן'),
    ('the offering made OF THESE',              'Lev', 2, 8, 'מאלה'),
    ('PRESENT it to the altar',                 'Lev', 2, 8, 'והגישה'),
    ('memorial #2',                             'Lev', 2, 9, 'אזכרתה'),
    ('MOST HOLY #2',                            'Lev', 2, 10, 'קדשים'),
    # leaven, honey, salt
    ('ALL the meal offering — no leaven',       'Lev', 2, 11, 'חמץ'),
    ('no leaven, no HONEY to the fire',         'Lev', 2, 11, 'דבש'),
    ('an offering of FIRST things',             'Lev', 2, 12, 'ראשית'),
    ('they shall NOT GO UP on the altar',       'Lev', 2, 12, 'יעלו'),
    ('with SALT you shall salt (x3)',           'Lev', 2, 13, 'מלח', 3),
    ('the COVENANT of your God',                'Lev', 2, 13, 'ברית'),
    ('on ALL your offerings',                   'Lev', 2, 13, 'קרבנך'),
    # the first-fruits offering
    ('the FIRST-FRUITS meal offering',          'Lev', 2, 14, 'בכורים'),
    ('PARCHED with fire',                       'Lev', 2, 14, 'קלוי'),
    ('GRITS of fresh grain',                    'Lev', 2, 14, 'גרש'),
    ('you shall offer — DOUBLED',               'Lev', 2, 14, 'תקריב', 2),
    ('oil on it (bikkurim)',                    'Lev', 2, 15, 'שמן'),
    ('frankincense on it (bikkurim)',           'Lev', 2, 15, 'לבנה'),
    ('memorial #3',                             'Lev', 2, 16, 'אזכרתה'),
    # the bird burnt offering
    ('of the BIRDS',                            'Lev', 1, 14, 'העוף'),
    ('TURTLEDOVES',                             'Lev', 1, 14, 'התרים'),
    ('young PIGEONS',                           'Lev', 1, 14, 'היונה'),
    ('he shall PINCH its head',                 'Lev', 1, 15, 'ומלק'),
    ('its blood PRESSED OUT',                   'Lev', 1, 15, 'ונמצה'),
    ('on the WALL of the altar',                'Lev', 1, 15, 'קיר'),
    ('its CROP',                                'Lev', 1, 16, 'מראתו'),
    ('with its FEATHERS',                       'Lev', 1, 16, 'בנצתה'),
    ('EASTWARD',                                'Lev', 1, 16, 'קדמה'),
    ('the ASH place',                           'Lev', 1, 16, 'הדשן'),
    ('he shall REND it',                        'Lev', 1, 17, 'ושסע'),
    ('by its WINGS',                            'Lev', 1, 17, 'בכנפיו'),
    ('he shall NOT DIVIDE',                     'Lev', 1, 17, 'יבדיל'),
    # cross-book receipts
    ('[IMPORT] sinner\'s: NO frankincense',     'Lev', 5, 11, 'לבנה'),
    ('[IMPORT] sinner\'s: it IS a sin offering', 'Lev', 5, 11, 'חטאת', 2),
    ('[IMPORT] the bird sin offering: not divide', 'Lev', 5, 8, 'יבדיל'),
    ('[IMPORT] priest\'s meal offering WHOLE',  'Lev', 6, 16, 'כליל'),
    ('[IMPORT] not baked LEAVENED (6:10)',      'Lev', 6, 10, 'חמץ'),
    ('[IMPORT] the todah\'s LEAVENED loaves',   'Lev', 7, 13, 'חמץ'),
    ('[IMPORT] baked in the OVEN (7:9)',        'Lev', 7, 9, 'בתנור'),
    ('[IMPORT] the two loaves LEAVENED',        'Lev', 23, 17, 'חמץ'),
    ('[IMPORT] the omer: when you come to the LAND', 'Lev', 23, 10, 'הארץ'),
    ('[IMPORT] the omer WAVED',                 'Lev', 23, 11, 'והניף'),
    ('[IMPORT] showbread: pure FRANKINCENSE',   'Lev', 24, 7, 'לבנה'),
    ('[IMPORT] libation meal offering: mixed with OIL', 'Num', 15, 4, 'בלול'),
    ('[IMPORT] the jealousy offering WAVED',    'Num', 5, 25, 'והניף'),
    ('[IMPORT] pure beaten FOR THE LIGHT',      'Exod', 27, 20, 'למאור'),
    ('[IMPORT] a LOG of oil (14:21)',           'Lev', 14, 21, 'ולג'),
]
fired = 0
for row in PROBES:
    label, book, ch, vs, tok = row[:5]
    need = row[5] if len(row) > 5 else 1
    hits = count(book, ch, vs, tok)
    if hits < need:
        sys.exit('ZERO-REPORT LAW: probe %r wanted %d of %r at %s %d:%d, found %d '
                 '— refusing to run' % (label, need, tok, book, ch, vs, hits))
    fired += 1
print('probes: all %d ink-token probes fired (15 imports receipted) [zero-report law satisfied]' % fired)

# ---- censuses the code runs on (asserted, not recited) --------------
KIND_TOKENS = [('soleth', 2, 1, 'סלת'), ('oven', 2, 4, 'תנור'), ('griddle', 2, 5, 'המחבת'),
               ('pan', 2, 7, 'מרחשת'), ('bikkurim', 2, 14, 'בכורים')]
KINDS = [k for k, ch, vs, tok in KIND_TOKENS if count('Lev', ch, vs, tok)]
assert KINDS == ['soleth', 'oven', 'griddle', 'pan', 'bikkurim'], KINDS
AZKARAH = [vs for vs in range(1, 17) if count('Lev', 2, vs, 'אזכרתה')]
assert AZKARAH == [2, 9, 16], AZKARAH
MOST_HOLY = [vs for vs in range(1, 17) if count('Lev', 2, vs, 'קדשים')]
assert MOST_HOLY == [3, 10], MOST_HOLY
SALT_NOUNS = sum(1 for w in toks('Lev', 2, 13) if w in ('במלח', 'מלח'))
SALT_VERBS = sum(1 for w in toks('Lev', 2, 13) if w == 'תמלח')
SALT_TOKENS = SALT_NOUNS + SALT_VERBS
assert (SALT_NOUNS, SALT_VERBS) == (3, 1), (SALT_NOUNS, SALT_VERBS)   # the root FOUR times: three nouns, one verb
OIL_FORMS = {'pour': [vs for vs in range(1, 17) if count('Lev', 2, vs, 'ויצק') or count('Lev', 2, vs, 'ויצקת')],
             'mix': [vs for vs in range(1, 17) if count('Lev', 2, vs, 'בלול')],
             'in_oil': [vs for vs in range(1, 17) if count('Lev', 2, vs, 'בשמן') and not count('Lev', 2, vs, 'בלול') and not count('Lev', 2, vs, 'משחים')]}
assert OIL_FORMS == {'pour': [1, 6], 'mix': [4, 5], 'in_oil': [7]}, OIL_FORMS
FRANKINCENSE = [vs for vs in range(1, 17) if any(w in ('לבנה', 'לבנתה') for w in toks('Lev', 2, vs))]
assert FRANKINCENSE == [1, 2, 15, 16], FRANKINCENSE
# the census caught its own first draft: the bare substring for frankincense (levonah) also matched
# 'and to his SONS' (u-le-vanav) at 2:3 and 2:10 — the noun's own two forms are the census.
# the phrase 'a fire-offering of pleasing odor' by CLASS in Lev 1-2
def pleasing(ch, vs): return count('Lev', ch, vs, 'ניח') and count('Lev', ch, vs, 'אשה')
ODOR = {'beast_olah': [vs for vs in range(1, 14) if pleasing(1, vs)],
        'bird_olah': [vs for vs in range(14, 18) if pleasing(1, vs)],
        'minchah': [vs for vs in range(1, 17) if pleasing(2, vs)]}
assert ODOR == {'beast_olah': [9, 13], 'bird_olah': [17], 'minchah': [2, 9]}, ODOR
print('censuses: five KINDS by token %s · memorial at %s · most-holy at %s · the salt root x%d at 2:13 (three nouns + the verb) · '
      'oil forms %s · frankincense at %s · pleasing-odor classes %d (beast %s, bird %s, meal %s)'
      % (KINDS, AZKARAH, MOST_HOLY, SALT_TOKENS, OIL_FORMS, FRANKINCENSE, len(ODOR),
         ODOR['beast_olah'], ODOR['bird_olah'], ODOR['minchah']))

# the sinner's meal offering CALLED from the Lev 5 engine (the first-call standard)
import cold_run_vayikra5 as V5
# the bird burnt offering's frame — Lev 1's burnt offering — CALLED from the
# offerings dispatcher (2026-09-06, the dependency-debt sitting)
import io as _io, contextlib as _ctx
with _ctx.redirect_stdout(_io.StringIO()):
    import cold_run_offerings as OFF
OLAH_FRAME = OFF.dispatch('olah:flock')['disposition']['v']
_sin = V5.graded_offering({'trigger': 'utterance_oath', 'act_is_his_option': True, 'tense': 'past',
                           'oath_forgotten': True, 'means': 'reaches_flour'}, V5.DATA)
SINNER_VERDICT = _sin[0] if isinstance(_sin, tuple) else _sin
print('routing receipt: cold_run_vayikra5.graded_offering(reaches_flour) CALLED -> %r' % (SINNER_VERDICT,))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'   # H: THE LINK REVIEW LAW (LR3, 2026-09-07) — an untaught transfer, kept and labeled, never counted as compiled

def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}

# ---- (1) THE MEAL OFFERING — compiled from Lev 2's ink -------------
CROSS = ('Sifra Nedavah Chapter 10 1 — "meal offering": what is said here holds for ALL meal '
         'offerings and what is said of all holds here — THE TEMPLATE BROADCAST (the move '
         'that carries one kind\'s clause across the five)')

def vow(words):
    """The vow parser — what a spoken vow of a meal offering obligates."""
    if words == 'a_meal_offering':
        return cell('whichever_of_the_five', I,
                    'the ink names five kinds and ranks none: soleth 2:1, oven 2:4, griddle '
                    '2:5, pan 2:7, first fruits 2:14 (censused); R. Yehuda\'s arm — the soleth '
                    'one, "the special one" (Menachot 13:1) — recorded beside it', ['consecrated'])
    if words == 'specified_kind_forgot':
        return cell('all_five', I, 'the kinds census = 5 (Menachot 13:2: "brings the five of them")',
                    ['consecrated'])
    if words == 'a_tenth':
        return cell(1, I, 'grammatical number (M-12): singular "a tenth" (Menachot 13:1)', ['consecrated'])
    if words == 'tenths':
        return cell(2, I, 'the plural\'s minimum is two (M-12; Menachot 13:1)', ['consecrated'])
    if words == 'specified_tenths_forgot':
        return cell(60, D, 'the sixty is the sages\' measure — "all the measures of the sages are so" '
                    '(Menachot 12:4 self-labels the data channel); Rabbi\'s arm one-to-sixty beside it',
                    ['consecrated'])
    if words == 'of_barley':
        return cell('wheat', M, 'INK: סלת (soleth, 2:1) — the Sifra fixes soleth = WHEAT from Exod 29:2\'s '
                    'usage (Nedavah Chapter 10 2-3: a gift meal offering only from wheat); the vow '
                    'is normalized toward the spec (Chapter 10 6) — R. Shimon\'s void arm recorded',
                    ['consecrated'])
    if words == 'half_a_tenth':
        return cell('whole_tenth', D, 'the tenth is the data channel (Lev 5:11 / Num 15 state it; Lev 2 '
                    'states no quantity); normalized up (Sifra Chapter 10 6)', ['consecrated'])
    if words == 'without_oil_and_frankincense':
        return cell('with_oil_and_frankincense', I, 'the ink makes both adjuncts part of the kind (2:1 '
                    '"and he shall pour oil on it and put frankincense on it"); the malformed vow is '
                    'normalized (Sifra Chapter 10 6)', ['consecrated'])
    if words == 'griddle_brought_pan':
        return cell('obligation_not_discharged', I, 'griddle (2:5) and pan (2:7) are two KINDS by their own '
                    'tokens; the other kind is a valid offering but not the vow (Menachot 12:2)',
                    ['consecrated', 'not_accepted'])
    if words == 'THIS_in_griddle_brought_pan':
        return cell('invalid', A, 'the designated object bound to its vessel — Menachot 12:2\'s "this" '
                    'clause (the designation logic is the answer sheet\'s)', ['disqualified'])
    if words == 'in_the_oven_brought_stove_or_tiles':
        return cell('not_valid_for_the_vow', M, 'INK: תנור (oven) at 2:4, doubled by 7:9\'s "baked in the '
                    'oven" — the Sifra reads the doubling: not the small stove, not the tiles, not the '
                    'Arab pits (Nedavah Section 10 3; R. Yehuda allows the stove)', ['disqualified'])
    if words == 'baked_offering_half_cakes_half_wafers':
        return cell('not_mixed', M, 'the Sifra\'s vow grammar: "a BAKED meal offering" is one kind — cakes '
                    'or wafers, R. Yehuda; R. Shimon permits the mix as one offering (Nedavah Section '
                    '10 1-2) — the dispute carried', [FX.NONE])
    return cell('no_vow', I, '', [FX.NONE])

def who_brings(case):
    if case == 'partners_one_tenth':
        return cell('not_brought', I, 'ונפש (a SOUL, 2:1) — the caller is singular; the Sifra closes it on '
                    'קרבנו (his offering): the individual brings a gift meal offering, partners do not '
                    '(Nedavah Chapter 10 8, 10 12)', [FX.NONE])
    if case == 'partners_bird':
        return cell('brought_even_one_bird', M, 'the Sifra extends the partners\' license to the burnt and '
                    'peace offerings "and of birds even ONE bird" (Nedavah Chapter 10 13; Chapter 8 1)',
                    ['accepted'])
    if case == 'wine_alone':
        return cell('donated', M, 'the standalone menu from "an offering" (Nedavah Section 8 5)', ['consecrated'])
    if case == 'oil_alone':
        return cell('R._Tarfon_yes_R._Akiva_no', M, 'the recorded dispute (Nedavah Section 8 7 / Menachot '
                    '12:5): R. Tarfon by analogy to wine, R. Akiva — oil never comes as its own obligation',
                    [FX.NONE])
    return cell('individual', I, 'a soul', ['consecrated'])

def adjuncts(kind):
    """Which meal offering carries oil, frankincense, both, or neither."""
    if kind == 'soleth':
        return cell('oil_and_frankincense', I, '2:1 — pour oil, put frankincense', [FX.NONE])
    if kind in ('griddle', 'pan', 'cakes', 'wafers'):
        return cell('oil_and_frankincense', M, 'the ink gives each vessel kind its OIL (2:4-7) and '
                    'frankincense only at 2:1 and 2:15; ' + CROSS, [FX.NONE])
    if kind in ('omer', 'bikkurim'):
        return cell('oil_and_frankincense', I, '2:15 — "and you shall put oil on it and set frankincense '
                    'on it"', [FX.NONE])
    if kind == 'sinner':
        v = 'neither' if 'no oil, no frankincense' in str(SINNER_VERDICT) else 'UNRESOLVED:%r' % (SINNER_VERDICT,)
        return cell(v, P, 'CALLED cold_run_vayikra5.graded_offering(reaches_flour) -> %r — Lev 5:11\'s own '
                    'two bans, "for it is a sin offering" [IMPORT, live call]' % (SINNER_VERDICT,), [FX.NONE])
    if kind == 'libation':
        return cell('oil_only', P, 'Num 15:4 "mixed with oil" — no frankincense written [IMPORT]', [FX.NONE])
    if kind == 'showbread':
        return cell('frankincense_only', P, 'Lev 24:7 "pure frankincense on the row" — no oil written [IMPORT]',
                    [FX.NONE])
    return cell('unknown_kind', I, '', [FX.NONE])

def oil_ops(kind):
    if kind in ('griddle', 'pan', 'soleth'):
        return cell(3, I, 'THREE oil forms censused in the chapter — POUR (2:1, 2:6), MIX (2:4, 2:5), '
                    'made IN OIL (2:7): the Mishnah\'s "three applications" (Menachot 6:3) are the '
                    'ink\'s three verbs, broadcast across the vessel kinds by the Sifra\'s rule', [FX.NONE])
    if kind == 'cakes':
        return cell('mixed', I, '2:4 "cakes MIXED with oil"', [FX.NONE])
    if kind == 'wafers':
        return cell('anointed', I, '2:4 "wafers ANOINTED with oil"', [FX.NONE])
    return cell('none', I, '', [FX.NONE])

def oil_grade():
    return cell('not_required_pure_beaten', P, 'Exod 27:20 "pure beaten FOR THE LIGHT" — the grade is '
                'written for the lamp, not the meal offerings (Menachot 8:5 quotes it) [IMPORT]', [FX.NONE])

def oil_scaling(tenths):
    return cell('a_log_per_tenth', D, 'the log is Lev 14:21\'s (data); the SCALING is disputed: the Sages '
                'linear (sixty tenths, sixty logs), R. Eliezer b. Yaakov constant (one log, "a meal '
                'offering and a log of oil") — Menachot 9:3; the Sifra weighed the same choice for the '
                'fistful and picked constant (Nedavah Section 9 3)', [FX.NONE])

def frankincense_quantity():
    return cell('a_fistful', M, 'the ink gives no measure; the Sifra: it requires scooping and requires '
                'frankincense — as the scoop is a full fist, so the frankincense (Nedavah Chapter 10 18; '
                'Menachot 13:3)', [FX.NONE])

def fistful(case):
    """Lev 2:2 — the priests scoop a full fist of the flour and oil, with all the frankincense."""
    if case == 'scooped_by_non_priest':
        return cell('invalid', I, 'הכהנים... וקמץ (2:2) — the priests are the scooper\'s subject; a non-priest\'s '
                    'scoop is no scoop (Menachot 1:2)', ['disqualified'])
    if case == 'left_hand':
        return cell('invalid', A, 'the right hand is the answer sheet\'s (Menachot 1:2; the Talmud\'s Lev 14 '
                    'analogy not opened this sitting)', ['disqualified'])
    if case == 'pebble_salt_grain_frankincense_crumb':
        return cell('invalid', M, 'INK: מלא קמצו מסלתה ומשמנה (his full fist OF ITS FLOUR AND OIL, 2:2); the '
                    'Sifra: a pebble, a grain of salt, a crumb of frankincense in the fist — invalid; the '
                    'frankincense present at scooping and wholly removed (Nedavah Section 9 10)', ['disqualified'])
    if case == 'overflowing_or_fingertips':
        return cell('invalid', M, 'INK: מלא קמצו (his FULL fist); the level measure — not overflowing, not '
                    'fingertips, three fingers over the palm (Nedavah Section 9 6; Menachot 1:2)', ['disqualified'])
    if case == 'fistful_and_frankincense':
        return cell('indispensable_pair', I, 'על כל לבנתה (with ALL its frankincense, 2:2) — the scoop and the '
                    'frankincense are one clause: each holds the other back (Menachot 3:5)', ['azkarah_to_fire'])
    if case == 'flour_and_oil':
        return cell('indispensable_pair', I, '2:1 — "fine flour... and he shall pour oil on it": the kind is '
                    'the pair (Menachot 3:5)', [FX.NONE])
    if case == 'quantity_short':
        return cell('invalid', D, 'the tenth and the log are the data channel; the Sifra: short by ANY '
                    'amount — invalid (Nedavah Section 9 8; Menachot 3:5, 1:3)', ['disqualified'])
    if case == 'remainder_lost_before_burning':
        return cell('R._Eliezer_valid_R._Yehoshua_invalid', M, 'the dependency direction: the fistful is '
                    'burned even if the remainder was lost (Nedavah Section 9 11 = R. Eliezer); R. '
                    'Yehoshua\'s arm carried (Menachot 3:4)', ['azkarah_to_fire'])
    if case == 'two_unscooped_mixed':
        return cell('valid_if_each_scoopable', M, 'Nedavah Section 9 9: not the neighbor\'s flour or oil — '
                    'valid only if a fist can be taken from each by itself (Menachot 3:3)', [FX.NONE])
    if case == 'not_poured_mixed_broken_salted_presented':
        return cell('valid', A, 'the essentials sort: only the fistful and the frankincense are '
                    'indispensable (Menachot 3:2); the ink writes the ops, the answer sheet ranks them',
                    ['accepted'])
    if case == 'not_for_its_name':
        return cell('valid_not_credited', A, 'the general intent rule (Zevachim 1:1 / Menachot 1:1) — valid, '
                    'the owner\'s obligation not discharged', ['not_accepted'])
    if case == 'sinner_not_for_its_name':
        return cell('invalid', P, 'Lev 5:11 "for it IS a sin offering" — the name clause (Menachot 1:1) '
                    '[IMPORT]', ['disqualified'])
    return cell('no_case', I, '', [FX.NONE])

def remainder(kind):
    if kind in ('soleth', 'griddle', 'pan', 'cakes', 'wafers', 'omer', 'sinner', 'jealousy', 'gentile', 'woman'):
        return cell('aaron_and_sons_most_holy', I, 'והנותרת... לאהרן ולבניו קדש קדשים (2:3, 2:10 — twice): the '
                    'remainder to the priests, most holy (Menachot 6:1; Zevachim 6:1)',
                    ['due_to_priest', 'most_holy'])
    if kind in ('priests_own', 'anointed_priest', 'libation'):
        return cell('wholly_to_altar_none_to_priests', P, 'Lev 6:16 "every meal offering of a priest shall be '
                    'WHOLE, it shall not be eaten" [IMPORT] (Menachot 6:2)', ['azkarah_to_fire'])
    if kind in ('two_loaves', 'showbread'):
        return cell('to_priests_none_to_altar', P, 'Lev 23:17 / 24:9 — no memorial burned of the loaves '
                    'themselves [IMPORT] (Menachot 6:2)', ['due_to_priest'])
    return cell('unknown', I, '', [FX.NONE])

def breaking(kind, offerer='israelite'):
    if kind == 'griddle':
        base = cell('break_in_pieces', I, 'פתות אתה פתים (BREAK it in pieces, 2:6) — the griddle\'s own verse',
                    [FX.NONE])
    elif kind in ('pan', 'cakes', 'wafers'):
        base = cell('break_in_pieces', M, 'all vessel-made — ' + CROSS + ' (Menachot 6:4)', [FX.NONE])
    else:
        return cell('no_breaking', I, '', [FX.NONE])
    if offerer == 'israelite':
        base['v'] = 'fold_to_two_and_four_and_separate'
    elif offerer == 'priests':
        base['v'] = 'fold_not_separate'; base['p'] = M
    elif offerer == 'anointed_priest':
        base['v'] = 'not_folded'; base['p'] = M
    if offerer != 'israelite' or base['p'] == M:
        base['why'] += '; the three execution paths by offerer class — the Sifra\'s role table (Nedavah ' \
                       'Chapter 12 4: the Israelite\'s separated, the priests\' not, the high priest\'s unfolded)'
    return base

def leaven(case):
    if case == 'any_meal_offering_leavened':
        return cell('transgression', I, 'כל המנחה... לא תעשה חמץ (ALL the meal offering... shall not be made '
                    'leavened, 2:11) — Menachot 5:2 quotes the clause', ['barred_from_it', 'lashes'])
    if case == 'per_step':
        return cell('kneading_shaping_baking_each', M, 'the ink bans the WHOLE ("shall not be made"); Lev 6:10 '
                    '"it shall not be BAKED leavened" singles baking out [IMPORT] — the Sifra: therefore '
                    'every step is its own transgression (Nedavah Section 12 3; Menachot 5:2)', ['lashes'])
    if case == 'todah_loaves':
        return cell('leavened', P, 'Lev 7:13 "with cakes of LEAVENED bread" [IMPORT] — the exception in the '
                    'compiled Tzav span (Menachot 5:1)', ['accepted'])
    if case == 'two_loaves':
        return cell('leavened', P, 'Lev 23:17 "baked LEAVENED" [IMPORT] — the Emor span (Menachot 5:1)',
                    ['accepted'])
    if case == 'honey_to_the_fire':
        return cell('barred', I, '"nor any HONEY shall you burn as a fire-offering" (2:11)', ['barred_from_it'])
    if case == 'first_fruits_of_leaven_or_honey':
        return cell('brought_as_first_offering_not_ascending', I, '2:12 — "an offering of FIRST things you may '
                    'bring them, but to the altar they shall NOT GO UP"', ['barred_from_it'])
    return cell('no_case', I, '', [FX.NONE])

def salt(case):
    if case == 'meal_offering':
        return cell('required', I, 'במלח תמלח (with SALT you shall SALT, 2:13) — the token three times in one '
                    'verse, and "on ALL your offerings"', ['salted'])
    if case == 'bird_olah':
        return cell('rubbed_with_salt', I, 'על כל קרבנך תקריב מלח (on ALL your offerings you shall offer salt, '
                    '2:13) — the bird is an offering; Zevachim 6:5 "rubs it with salt" twice', ['salted'])
    if case == 'not_salted_post_facto':
        return cell('valid', A, 'Menachot 3:2 — the non-essential op (the essentials sort)', ['accepted'])
    if case == 'which_salt':
        return cell('any_salt_any_place_even_sabbath', M, 'ברית (COVENANT, 2:13; Onkelos: "you shall not ANNUL '
                    'the salt of the covenant") — the Sifra: Sodom or Astrakhan, from anywhere, even on the '
                    'Sabbath, even in uncleanness (Nedavah Chapter 14 7)', ['salted'])
    return cell('no_case', I, '', [FX.NONE])

def presentation(kind):
    if kind in ('soleth', 'griddle', 'pan', 'cakes', 'wafers'):
        return cell('required', I, 'והבאת את המנחה אשר יעשה מאלה... והגישה אל המזבח (the meal offering made OF '
                    'THESE... present it to the altar, 2:8) — the five kinds by the deictic', ['presented'])
    if kind in ('omer', 'jealousy'):
        return cell('waving_and_presentation', P, 'the presentation from 2:8\'s rule (Sifra Chapter 13 5-6 '
                    'brings the sinner\'s and jealousy offering under it); the WAVING from Lev 23:11 / '
                    'Num 5:25 [IMPORT] (Menachot 5:6)', ['presented'])
    if kind in ('showbread', 'libation'):
        return cell('neither', M, 'excluded from "of these" — the Sifra\'s include-then-exclude (Nedavah '
                    'Chapter 13 6-8; Menachot 5:6)', [FX.NONE])
    if kind == 'priests_own':
        return cell('required_R._Shimon_no', M, 'the Sifra includes it (Chapter 13 8 excludes only after '
                    'including); R. Shimon: no fistful, no presentation (Menachot 5:5)', ['presented'])
    return cell('unknown', I, '', [FX.NONE])

def where(op):
    if op == 'presentation':
        return cell('west', A, 'Menachot 5:6 "waving in the east, presentation in the WEST" — the SW corner\'s '
                    'lower service (Zevachim 6:2); geography the ink does not state', [FX.NONE])
    if op == 'order':
        return cell('wavings_precede_presentations', A, 'Menachot 5:6', [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

def omer(case):
    """Lev 2:14-16 — the first-fruits meal offering (the omer, by the Sifra's reading)."""
    if case == 'parching':
        return cell('R._Meir_singed_Sages_perforated_tube', M, 'INK: אביב קלוי באש (fresh ears PARCHED WITH '
                    'FIRE, 2:14) — both arms satisfy the fire token; the DEVICE is disputed: R. Meir singes '
                    'it in the fire, the Sages beat it with reeds and put it in a PERFORATED tube so the '
                    'fire rules all of it (Nedavah Section 13 6 — verbatim at Menachot 10:4)', [FX.NONE])
    if case == 'grinding':
        return cell('grits_mill', I, 'גרש כרמל (GRITS of fresh grain, 2:14) — Menachot 10:4\'s "mill of '
                    'grits"', [FX.NONE])
    if case == 'after_the_tenth':
        return cell('oil_frankincense_pour_mix_wave_present_scoop_burn_rest_to_priests', I,
                    '2:15-16: "put oil on it, set frankincense on it... the priest burns its memorial of its '
                    'grits and its oil with all its frankincense"; the presentation from 2:8; the WAVING '
                    'from Lev 23:11 [IMPORT] — Menachot 10:4\'s closing sentence in the ink\'s order',
                    ['azkarah_to_fire', 'presented', 'due_to_priest'])
    if case == 'no_standing_grain':
        return cell('from_sheaves', M, 'תקריב doubled at 2:14 ("you shall offer... you shall offer") — the '
                    'Sifra reads the repeat as the fallback: not found from standing grain, bring from the '
                    'sheaves (Nedavah Chapter 15 1; Menachot 10:9)', ['accepted'])
    if case == 'no_moist_grain':
        return cell('dry', M, 'the same doubled verb: not found soft (כרמל) — bring it dry (Nedavah Chapter '
                    '15 1; Menachot 10:9)', ['accepted'])
    if case == 'source':
        return cell('new_and_from_the_land', P, 'בכורים (FIRST fruits, 2:14) — new by its name; the LAND from '
                    'Lev 23:10 "when you come into the land... the first of your harvest" [IMPORT] '
                    '(Menachot 8:1)', [FX.NONE])
    if case == 'grain':
        return cell('barley', M, 'the Sifra: אביב — from barley, by the Egypt-plague usage (Nedavah Section '
                    '13 4); the ink names no grain', [FX.NONE])
    return cell('no_case', I, '', [FX.NONE])

def odor_classes():
    return cell(3, I, 'the phrase "a fire-offering of pleasing odor" censused by CLASS in Lev 1-2: the beast '
                'burnt offering (1:9, 1:13), the bird burnt offering (1:17), the meal offering (2:2, 2:9) '
                '— three classes, five tokens; Menachot 13:11: "the one who does much and the one who does '
                'little are alike, provided he directs his heart to Heaven"', [FX.NONE])

# ---- (1) THE BIRD BURNT OFFERING — compiled from Lev 1:14-17 --------
def bird(case, **k):
    if case == 'species':
        return cell('turtledoves_or_young_pigeons', I, 'מן התרים או מן בני היונה (1:14)', [FX.NONE])
    if case == 'age':
        sp, age = k['species'], k['age']
        bad = (sp == 'turtledove' and age == 'young') or (sp == 'pigeon' and age == 'grown')
        return cell('invalid' if bad else 'valid', M, 'the ink writes TURTLEDOVES and YOUNG pigeons (בני '
                    'יונה, 1:14); the Sifra reads the windows: turtledoves large only, pigeons small only, '
                    'the shining-neck stage excluded for both (Nedavah Chapter 8 4-5; Zevachim 7:5)',
                    ['disqualified'] if bad else ['accepted'])
    if case == 'blemish':
        return cell('invalid', M, 'no "unblemished male" is written for birds (Lev 22:19 binds herd and flock); '
                    'the Sifra\'s floor: a dried wing, a dug-out eye, a cut leg still invalidate — a '
                    'missing limb (Nedavah Section 6 3; Zevachim 7:5)', ['disqualified'])
    if case == 'instrument':
        return cell('fingernail_not_knife', M, 'ומלק (he shall PINCH, 1:15) — the Sifra: by the fingernail, '
                    'not a knife (Nedavah Section 7 3); Zevachim 7:5: pinched with a knife — disqualified',
                    ['pinched'])
    if case == 'left_hand_or_night':
        return cell('not_a_pinching_at_all', A, 'Zevachim 7:5 — no gullet impurity: the act is not melikah',
                    ['disqualified'])
    if case == 'how_many':
        return cell('even_one', M, 'והקריבו (and he shall bring IT, 1:15) — the Sifra: even one bird; the pair '
                    'of 1:14 is not a floor (Nedavah Section 7 1; Menachot 12:5)', ['accepted'])
    if case == 'place':
        return cell('above_the_red_line_south_east_corner', M, 'the ink says "to the altar" (1:15); the Sifra '
                    'ties the pinching to the burning\'s place by the shared "upon the altar" — ABOVE the '
                    'red line (Nedavah Section 7 4), and records the walk: up the ramp, to the ledge, the '
                    'south-east corner (Section 7 8; Zevachim 6:5)', [FX.NONE])
    if case == 'head':
        return cell('divided_and_burned_by_itself', M, 'ומלק את ראשו והקטיר המזבחה (pinch its head and burn '
                    'on the altar, 1:15) — the head has its own burn verb: the Sifra reads two smoke ops, '
                    'head and body (Nedavah Section 7 6); so the olah\'s head is DIVIDED (Zevachim 6:5-6: '
                    '"did not divide in the burnt offering — invalid"), where the sin offering\'s is not '
                    '(Lev 5:8 "he shall not divide" [IMPORT])', ['pinched', 'accepted'])
    if case == 'blood':
        return cell('pressed_on_the_wall', I, 'ונמצה דמו על קיר המזבח (its blood PRESSED OUT on the WALL of '
                    'the altar, 1:15)', [FX.NONE])
    if case == 'blood_head_only':
        return cell('invalid', M, 'the majority-blood rule: the body\'s blood is the greater part — "it is a '
                    'burnt offering" (Nedavah Chapter 9 7; Zevachim 6:6)', ['disqualified'])
    if case == 'blood_body_only':
        return cell('valid', M, 'the same rule\'s other arm (Nedavah Chapter 9 7; Zevachim 6:6)', ['accepted'])
    if case == 'crop':
        return cell('cast_beside_the_altar_eastward_to_the_ash_place', I, 'והסיר את מראתו בנצתה והשליך אתה '
                    'אצל המזבח קדמה אל מקום הדשן (1:16) — the crop WITH its feathers, EASTWARD, the ASH '
                    'place: every token in the verse; the entrails that come out with it are the Sifra\'s '
                    '(Nedavah Section 7 9)', ['crop_cast_to_ash_place'])
    if case == 'rend':
        return cell('rend_by_the_wings_not_divide', I, 'ושסע אתו בכנפיו לא יבדיל (rend it by its wings, he '
                    'shall not divide, 1:17)', [FX.NONE])
    if case == 'divided_anyway':
        return cell('valid', M, '"and the priest shall burn it" (1:17) after the rending clause — the Sifra: '
                    'divided after all, still valid (Nedavah Chapter 9 6; Zevachim 6:5)', ['accepted'])
    if case == 'skipped_crop_or_salt_after_blood':
        return cell('valid', M, 'deviation severity: any change AFTER the blood is pressed does not kill '
                    'the run — the blood-press is the permitter (Nedavah Chapter 9 6; Zevachim 6:6)',
                    ['accepted'])
    if case == 'not_for_its_name':
        return cell('valid_not_credited', A, 'the intent rule for the olah (Zevachim 6:7, as 1:1)', ['not_accepted'])
    if case == 'done_below_as_sin_offering_procedure':
        return cell('invalid', M, 'the olah is ABOVE (Section 7 4) and divides (Section 7 6); below and '
                    'undivided is the sin offering\'s form — Lev 5:8-9 [IMPORT] (Zevachim 7:2)', ['disqualified'])
    if case == 'done_above_as_olah_for_olah':
        return cell('valid', M, 'Zevachim 7:2 — the procedure and the name both its own', ['accepted'])
    if case == 'burn':
        return cell('wholly_burned_on_the_wood', I, 'והקטיר אתו הכהן המזבחה על העצים אשר על האש (1:17) — a burnt '
                    'offering, a fire-offering of pleasing odor; the bird is an OLAH under Lev 1\'s frame: CALLED '
                    'cold_run_offerings.dispatch(olah:flock) disposition -> %r [IMPORT, live call]' % OLAH_FRAME,
                    ['accepted'])
    return cell('no_case', I, '', [FX.NONE])

# ---- THE WRAP (W3 THE OFFERING ENGINE, D9-iii, 2026-09-07) — the daemon and the scene --------------
# Five case heads: the meal offering brought (2:1, 2:4, 2:8, 2:13; 6:7 the priests' seat under law_tzav) —
# the vow parsed, the salt, the presentation, the memorial, the remainder; the fistful scooped (2:2; 6:8);
# the leavening (2:11; 6:10); the omer as Lev 2:14's first-fruits meal offering — THE SECOND SEAT of the
# calendar's omer_brought, one type under two daemons; the bird burnt offering (1:14-17). Never emits an event.
import world_engine as WE
def law_minchah(event, world):
    """Lev 2 + 1:14-17 (cold_run_minchah.py — the vow, the fistful, the leaven, the salt, the presentation, the omer, the bird)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'meal_offering_brought':
        if event['offerers'] == 'partners':
            return []                                            # Menachot 12:5 — two do not donate one tenth: the silence (who_brings)
        vc = vow(event['vow_words'])
        out = [E_('consecrated', event['offerer'], value=vc['v'], law='[INK Lev 2:1 "when a soul brings a meal offering" — the vow parsed: %s]' % vc['why'][:70])]
        if 'not_accepted' in vc['fx']:
            out.append(E_('not_accepted', event['offerer'], value=vc['v'], law='[Mishnah Menachot 12:2 — the other kind a valid offering, the vow not discharged]'))
        if 'disqualified' in vc['fx']:
            out.append(E_('disqualified', event['offerer'], value=vc['v'], law='[Mishnah Menachot 12:2 — "THIS in a griddle" bound to its vessel]'))
            return out
        mk = event['meal_kind']
        out += [E_('salted', 'the-meal-offering', value=salt('meal_offering')['v'], law='[INK Lev 2:13 "with salt you shall salt"]'),
                E_('presented', 'the-meal-offering', value=presentation(mk)['v'], law='[INK Lev 2:8 "present it to the altar"]'),
                E_('azkarah_to_fire', 'the-meal-offering', cp='HEAVEN', value=fistful('fistful_and_frankincense')['v'], law='[INK Lev 2:2 "the priest shall burn its memorial"]')]
        rem = remainder(mk)
        if 'due_to_priest' in rem['fx']:
            out += [E_('due_to_priest', 'the-priests', cp=event['offerer'], value=rem['v'], law='[INK Lev 2:3, 2:10 "the remainder to Aaron and his sons"]'),
                    E_('most_holy', 'the-meal-offering', law='[INK Lev 2:3 "most holy of the fire-offerings of the LORD"]')]
        return out
    if k == 'fistful_scooped':
        if event['by'] != 'priest' or event['hand'] == 'left' or event['contents'] != 'flour_and_oil' or event['quantity'] == 'short':
            case = 'scooped_by_non_priest' if event['by'] != 'priest' else 'left_hand' if event['hand'] == 'left' else 'pebble_salt_grain_frankincense_crumb' if event['contents'] != 'flour_and_oil' else 'quantity_short'
            return [E_('disqualified', 'the-meal-offering', value=fistful(case)['v'], law='[INK Lev 2:2 "the priests... his full fist of its flour and oil" — %s]' % case)]
        if not event['for_its_name']:
            if event['sinner']:
                return [E_('disqualified', 'the-meal-offering', value=fistful('sinner_not_for_its_name')['v'], law='[Lev 5:11 "for it IS a sin offering"; Mishnah Menachot 1:1]')]
            return [E_('accepted', 'the-meal-offering', cp='HEAVEN', value=fistful('not_for_its_name')['v'], law='[Mishnah Menachot 1:1 — valid]'),
                    E_('not_accepted', event['offerer'], value='obligation_not_discharged', law='[Mishnah Menachot 1:1 — not credited to the owner]')]
        return [E_('accepted', 'the-meal-offering', cp='HEAVEN', value='the_fistful', law='[INK Lev 2:2]'),
                E_('azkarah_to_fire', 'the-meal-offering', cp='HEAVEN', value=fistful('fistful_and_frankincense')['v'], law='[INK Lev 2:2 "with all its frankincense"; Mishnah Menachot 3:5]')]
    if k == 'meal_offering_leavened':
        lv = leaven(event['meal_kind']) if event['meal_kind'] in ('todah_loaves', 'two_loaves') else leaven('any_meal_offering_leavened')
        if 'accepted' in lv['fx']:
            return [E_('accepted', 'the-loaves', cp='HEAVEN', value=lv['v'], law='[Lev 7:13 / 23:17 the leavened exceptions — CALLED leaven(%s) -> %s]' % (event['meal_kind'], lv['v']))]
        return [E_('barred_from_it', event['baker'], value='leaven', law='[INK Lev 2:11 "shall not be made leavened"]'),
                E_('lashes', event['baker'], amount=40, value=leaven('per_step')['v'], law='[Mishnah Menachot 5:2 — liable for its kneading, its shaping, its baking: the step %s]' % event['step'])]
    if k == 'omer_brought':
        om = omer('no_standing_grain') if not event['standing_grain'] else (omer('no_moist_grain') if not event['moist'] else omer('source'))
        return [E_('accepted', event['bringer'], cp='HEAVEN', value=om['v'], law='[INK Lev 2:14 "and if you bring a meal offering of first fruits" — THE SECOND SEAT of the omer; the doubled "you shall offer": %s]' % om['why'][:70]),
                E_('azkarah_to_fire', 'the-omer', cp='HEAVEN', value=omer('after_the_tenth')['v'], law='[INK Lev 2:16 "the priest shall burn its memorial"]'),
                E_('presented', 'the-omer', value=presentation('omer')['v'], law='[INK Lev 2:8 through the deictic; the waving Lev 23:11]'),
                E_('due_to_priest', 'the-priests', cp=event['bringer'], value=remainder('omer')['v'], law='[INK Lev 2:3 — the rest to the priests (Mishnah Menachot 10:4)]')]
    if k == 'bird_offering_brought':
        age = bird('age', species=event['species'], age=event['age'])
        if 'disqualified' in age['fx'] or event['blemish'] or event['instrument'] != 'fingernail' or event['hand'] == 'left' or event['blood_pressed'] == 'head_only':
            why = 'age' if 'disqualified' in age['fx'] else 'blemish' if event['blemish'] else 'instrument' if event['instrument'] != 'fingernail' else 'left_hand_or_night' if event['hand'] == 'left' else 'blood_head_only'
            return [E_('disqualified', event['subject'], value=age['v'] if why == 'age' else bird(why)['v'], law='[Mishnah Zevachim 6:6, 7:5 — %s: CALLED bird(%s)]' % (why, why))]
        out = [E_('pinched', event['subject'], value=bird('instrument')['v'], law='[INK Lev 1:15 "and pinch off its head"]'),
               E_('crop_cast_to_ash_place', event['subject'], value=bird('crop')['v'], law='[INK Lev 1:16 "cast it beside the altar eastward, to the place of the ashes"]'),
               E_('salted', event['subject'], value=salt('bird_olah')['v'], law='[INK Lev 2:13 "on all your offerings you shall offer salt"; Mishnah Zevachim 6:5]')]
        if not event['for_its_name']:
            return out + [E_('not_accepted', event['offerer'], value=bird('not_for_its_name')['v'], law='[Mishnah Zevachim 6:7 — valid, not credited]')]
        return out + [E_('accepted', event['offerer'], cp='HEAVEN', value=bird('burn')['v'], law='[INK Lev 1:17 "a burnt offering, a fire-offering of pleasing odor" — the frame CALLED offerings(olah:flock)]')]
    return []

def scene():
    """THE SCENE — the meal offering's and the bird's rows replayed on the world engine (clock unit: days)."""
    with _ctx.redirect_stdout(_io.StringIO()):
        w = WE.World(era='the meal offering and the bird: Menachot 1, 5, 10, 12-13, Zevachim 6-7 on the engine (clock unit: days)')
        w.laws = [law_minchah]
        w.advance(1)
        w.submit({'kind': 'meal_offering_brought', 'subject': 'the-vower', 'offerer': 'the-vower', 'offerers': 'one', 'meal_kind': 'soleth', 'vow_words': 'a_meal_offering', 'case_source': 'Mishnah Menachot 13:1 — "a meal offering": whichever of the five'})
        w.submit({'kind': 'meal_offering_brought', 'subject': 'the-griddle-vower', 'offerer': 'the-griddle-vower', 'offerers': 'one', 'meal_kind': 'pan', 'vow_words': 'griddle_brought_pan', 'case_source': 'Mishnah Menachot 12:2 — vowed a griddle, brought a pan: not discharged'})
        w.submit({'kind': 'meal_offering_brought', 'subject': 'the-this-vower', 'offerer': 'the-this-vower', 'offerers': 'one', 'meal_kind': 'pan', 'vow_words': 'THIS_in_griddle_brought_pan', 'case_source': 'Mishnah Menachot 12:2 — "THIS in a griddle," brought in a pan: invalid'})
        w.submit({'kind': 'meal_offering_brought', 'subject': 'the-partners', 'offerer': 'the-partners', 'offerers': 'partners', 'meal_kind': 'soleth', 'vow_words': 'a_meal_offering', 'case_source': 'Mishnah Menachot 12:5 — two do not donate one tenth: the silence'})
        w.submit({'kind': 'meal_offering_brought', 'subject': 'the-priest', 'offerer': 'the-priest', 'offerers': 'one', 'meal_kind': 'priests_own', 'vow_words': 'a_meal_offering', 'case_source': 'Mishnah Menachot 6:2 — the priests\' own: wholly to the altar, none to the priests'})
        w.submit({'kind': 'fistful_scooped', 'subject': 'the-meal-offering', 'offerer': 'the-vower', 'by': 'non_priest', 'hand': 'right', 'contents': 'flour_and_oil', 'for_its_name': True, 'sinner': False, 'quantity': 'full', 'case_source': 'Mishnah Menachot 1:2 — scooped by a non-priest: invalid'})
        w.submit({'kind': 'fistful_scooped', 'subject': 'the-meal-offering', 'offerer': 'the-vower', 'by': 'priest', 'hand': 'right', 'contents': 'flour_and_oil', 'for_its_name': False, 'sinner': False, 'quantity': 'full', 'case_source': 'Mishnah Menachot 1:1 — not for its name: valid, not credited'})
        w.submit({'kind': 'fistful_scooped', 'subject': 'the-meal-offering', 'offerer': 'the-sinner', 'by': 'priest', 'hand': 'right', 'contents': 'flour_and_oil', 'for_its_name': False, 'sinner': True, 'quantity': 'full', 'case_source': 'Mishnah Menachot 1:1 — the sinner\'s not for its name: invalid'})
        w.submit({'kind': 'fistful_scooped', 'subject': 'the-meal-offering', 'offerer': 'the-vower', 'by': 'priest', 'hand': 'right', 'contents': 'flour_and_oil', 'for_its_name': True, 'sinner': False, 'quantity': 'full', 'case_source': 'Mishnah Menachot 3:5 — the fistful and the frankincense to the fire'})
        w.submit({'kind': 'meal_offering_leavened', 'subject': 'the-baker', 'baker': 'the-baker', 'meal_kind': 'soleth', 'step': 'baking', 'case_source': 'Mishnah Menachot 5:2 — leavened: transgression, per step'})
        w.submit({'kind': 'meal_offering_leavened', 'subject': 'the-todah-bringer', 'baker': 'the-todah-bringer', 'meal_kind': 'todah_loaves', 'step': 'baking', 'case_source': 'Mishnah Menachot 5:1 — the todah\'s loaves come leavened'})
        w.advance(16)
        w.submit({'kind': 'omer_brought', 'subject': 'israel', 'bringer': 'israel', 'day': 16, 'standing_grain': False, 'moist': True, 'case_source': 'Mishnah Menachot 10:9 — no standing grain: from the sheaves (Lev 2:14\'s doubled verb)'})
        w.submit({'kind': 'bird_offering_brought', 'subject': 'the-bird', 'offerer': 'the-bird-bringer', 'species': 'turtledove', 'age': 'grown', 'blemish': False, 'instrument': 'fingernail', 'hand': 'right', 'for_its_name': True, 'blood_pressed': 'body_and_head', 'case_source': 'Mishnah Zevachim 6:5 — the bird olah\'s walk'})
        w.submit({'kind': 'bird_offering_brought', 'subject': 'the-young-turtledove', 'offerer': 'the-bird-bringer', 'species': 'turtledove', 'age': 'young', 'blemish': False, 'instrument': 'fingernail', 'hand': 'right', 'for_its_name': True, 'blood_pressed': 'body_and_head', 'case_source': 'Mishnah Zevachim 7:5 — turtledoves before their time: disqualified'})
        w.submit({'kind': 'bird_offering_brought', 'subject': 'the-knifed-bird', 'offerer': 'the-bird-bringer', 'species': 'pigeon', 'age': 'young', 'blemish': False, 'instrument': 'knife', 'hand': 'right', 'for_its_name': True, 'blood_pressed': 'body_and_head', 'case_source': 'Mishnah Zevachim 7:5 — pinched with a knife: disqualified'})
        w.submit({'kind': 'bird_offering_brought', 'subject': 'the-misnamed-bird', 'offerer': 'the-bird-bringer', 'species': 'pigeon', 'age': 'young', 'blemish': False, 'instrument': 'fingernail', 'hand': 'right', 'for_its_name': False, 'blood_pressed': 'body_and_head', 'case_source': 'Mishnah Zevachim 6:7 — not for its name: valid, not credited'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    return (n('the-vower', 'consecrated'), n('the-griddle-vower', 'not_accepted'), n('the-this-vower', 'disqualified'), n('the-partners', 'consecrated'), n('the-priests', 'due_to_priest'),
            n('the-meal-offering', 'most_holy'), n('the-meal-offering', 'salted'), n('the-meal-offering', 'presented'), n('the-meal-offering', 'azkarah_to_fire'), n('the-meal-offering', 'disqualified'),
            n('the-meal-offering', 'accepted'), n('the-vower', 'not_accepted'), n('the-baker', 'lashes'), n('the-loaves', 'accepted'), n('israel', 'accepted'), n('the-omer', 'azkarah_to_fire'),
            n('the-bird', 'pinched'), n('the-bird', 'crop_cast_to_ash_place'), n('the-bird', 'salted'), n('the-bird-bringer', 'accepted'), n('the-young-turtledove', 'disqualified'),
            n('the-knifed-bird', 'disqualified'), n('the-bird-bringer', 'not_accepted'), w.clock.day), w
SCENE, _W = scene()

# ---- (2) TEST DATA — the Mishnah rows, read whole from the shelf ----
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
MEN = load('menachot'); ZEV = load('zevachim')
def mrow(book, ch, m, must):
    txt = strip((MEN if book == 'Menachot' else ZEV)[ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Menachot', 1, 1, 'חוטא'), ('Menachot', 1, 2, 'זר'), ('Menachot', 1, 2, 'צרור'), ('Menachot', 1, 3, 'לבונתה'),
    ('Menachot', 3, 2, 'מלח'), ('Menachot', 3, 3, 'לקמץ'), ('Menachot', 3, 4, 'אליעזר'), ('Menachot', 3, 5, 'הלבונה'),
    ('Menachot', 5, 1, 'מצה'), ('Menachot', 5, 2, 'חמץ'), ('Menachot', 5, 3, 'לבונה'), ('Menachot', 5, 5, 'הגשה'),
    ('Menachot', 5, 6, 'במזרח'), ('Menachot', 5, 8, 'כסוי'), ('Menachot', 5, 9, 'כפח'), ('Menachot', 6, 1, 'לכהנים'),
    ('Menachot', 6, 2, 'למזבח'), ('Menachot', 6, 3, 'יציקה'), ('Menachot', 6, 4, 'ומבדיל'), ('Menachot', 8, 1, 'החדש'),
    ('Menachot', 8, 5, 'למאור'), ('Menachot', 9, 3, 'ששים'), ('Menachot', 10, 4, 'אבוב'), ('Menachot', 10, 9, 'הקמה'),
    ('Menachot', 12, 2, 'במרחשת'), ('Menachot', 12, 3, 'השערין'), ('Menachot', 12, 4, 'ששים'), ('Menachot', 12, 5, 'פרידה'),
    ('Menachot', 13, 1, 'ששים'), ('Menachot', 13, 2, 'חמשתן'), ('Menachot', 13, 3, 'מקמץ'), ('Menachot', 13, 11, 'הממעיט'),
    ('Zevachim', 6, 5, 'ומבדיל'), ('Zevachim', 6, 5, 'הדשן'), ('Zevachim', 6, 6, 'הגוף'), ('Zevachim', 6, 7, 'עלתה'),
    ('Zevachim', 7, 2, 'למעלה'), ('Zevachim', 7, 5, 'בסכין'), ('Zevachim', 7, 5, 'גפה'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows token-verified in their own ink (Menachot 1-13 and Zevachim 6-7 read '
      'whole — the topic docket)' % len(SHEET))

TESTS = [
 # ---- the vow parser (Menachot 12-13) ----
 ('Menachot 13:1 — "a meal offering": whichever he wants (R. Yehuda: the fine-flour one)', vow('a_meal_offering'), 'whichever_of_the_five'),
 ('Menachot 13:2 — specified a kind and forgot: brings the five of them', vow('specified_kind_forgot'), 'all_five'),
 ('Menachot 13:1 — "a tenth": one', vow('a_tenth'), 1),
 ('Menachot 13:1 — "tenths": two', vow('tenths'), 2),
 ('Menachot 13:1-2 — specified tenths and forgot: sixty', vow('specified_tenths_forgot'), 60),
 ('Menachot 12:3 — "of barley": brings from wheat', vow('of_barley'), 'wheat'),
 ('Menachot 12:3 — "half a tenth": a whole tenth', vow('half_a_tenth'), 'whole_tenth'),
 ('Menachot 12:3 — "without oil and frankincense": brings with them', vow('without_oil_and_frankincense'), 'with_oil_and_frankincense'),
 ('Menachot 12:2 / 5:8 — vowed griddle, brought pan: obligation not discharged', vow('griddle_brought_pan'), 'obligation_not_discharged'),
 ('Menachot 12:2 — "THIS in a griddle," brought in a pan: invalid', vow('THIS_in_griddle_brought_pan'), 'invalid'),
 ('Menachot 5:9 — "in the oven": not the stove, the tiles, the Arab pits', vow('in_the_oven_brought_stove_or_tiles'), 'not_valid_for_the_vow'),
 ('Menachot 5:9 — a baked offering: not half cakes half wafers (R. Shimon permits)', vow('baked_offering_half_cakes_half_wafers'), 'not_mixed'),
 ('Menachot 12:5 — two do not donate one tenth', who_brings('partners_one_tenth'), 'not_brought'),
 ('Menachot 12:5 — but a bird, even one', who_brings('partners_bird'), 'brought_even_one_bird'),
 ('Menachot 12:5 — wine donated alone', who_brings('wine_alone'), 'donated'),
 ('Menachot 12:5 — oil alone: R. Tarfon yes, R. Akiva no', who_brings('oil_alone'), 'R._Tarfon_yes_R._Akiva_no'),
 # ---- the adjuncts (Menachot 5:3, 6:3, 8:5, 9:3, 13:3) ----
 ('Menachot 5:3 — the fine-flour offering: oil and frankincense', adjuncts('soleth'), 'oil_and_frankincense'),
 ('Menachot 5:3 — the griddle offering: oil and frankincense', adjuncts('griddle'), 'oil_and_frankincense'),
 ('Menachot 5:3 — the wafers: oil and frankincense', adjuncts('wafers'), 'oil_and_frankincense'),
 ('Menachot 5:3 — the omer: oil and frankincense', adjuncts('omer'), 'oil_and_frankincense'),
 ('Menachot 5:3 — the sinner\'s: neither (CALLED from the Lev 5 engine)', adjuncts('sinner'), 'neither'),
 ('Menachot 5:3 — the libation meal offering: oil, no frankincense', adjuncts('libation'), 'oil_only'),
 ('Menachot 5:3 — the showbread: frankincense, no oil', adjuncts('showbread'), 'frankincense_only'),
 ('Menachot 6:3 — vessel-made: three oil applications', oil_ops('griddle'), 3),
 ('Menachot 6:3 — the cakes mixed', oil_ops('cakes'), 'mixed'),
 ('Menachot 6:3 — the wafers anointed', oil_ops('wafers'), 'anointed'),
 ('Menachot 8:5 — pure beaten is for the light, not the meal offerings', oil_grade(), 'not_required_pure_beaten'),
 ('Menachot 9:3 — sixty tenths, sixty logs (R. Eliezer b. Yaakov: one)', oil_scaling(60), 'a_log_per_tenth'),
 ('Menachot 13:3 — frankincense not less than a fistful', frankincense_quantity(), 'a_fistful'),
 # ---- the fistful (Menachot 1-3) ----
 ('Menachot 1:2 — scooped by a non-priest: invalid', fistful('scooped_by_non_priest'), 'invalid'),
 ('Menachot 1:2 — scooped with the left hand: invalid', fistful('left_hand'), 'invalid'),
 ('Menachot 1:2 — a pebble, a grain of salt, a crumb of frankincense: invalid', fistful('pebble_salt_grain_frankincense_crumb'), 'invalid'),
 ('Menachot 1:2 — overflowing or by the fingertips: invalid', fistful('overflowing_or_fingertips'), 'invalid'),
 ('Menachot 3:5 — the fistful and the frankincense hold each other back', fistful('fistful_and_frankincense'), 'indispensable_pair'),
 ('Menachot 3:5 — the flour and the oil hold each other back', fistful('flour_and_oil'), 'indispensable_pair'),
 ('Menachot 3:5 / 1:3 — short of the tenth or the log: invalid', fistful('quantity_short'), 'invalid'),
 ('Menachot 3:4 — remainder lost: R. Eliezer valid, R. Yehoshua invalid', fistful('remainder_lost_before_burning'), 'R._Eliezer_valid_R._Yehoshua_invalid'),
 ('Menachot 3:3 — two unscooped mixed: valid if each can be scooped', fistful('two_unscooped_mixed'), 'valid_if_each_scoopable'),
 ('Menachot 3:2 — did not pour, mix, break, salt, present: valid', fistful('not_poured_mixed_broken_salted_presented'), 'valid'),
 ('Menachot 1:1 — scooped not for its name: valid, not credited', fistful('not_for_its_name'), 'valid_not_credited'),
 ('Menachot 1:1 — the sinner\'s not for its name: invalid', fistful('sinner_not_for_its_name'), 'invalid'),
 # ---- the remainder and the breaking (Menachot 6:1-2, 6:4) ----
 ('Menachot 6:1 / Zevachim 6:1 — the remainder to the priests, most holy', remainder('griddle'), 'aaron_and_sons_most_holy'),
 ('Menachot 6:2 — the priests\' own: to the altar, none to the priests', remainder('priests_own'), 'wholly_to_altar_none_to_priests'),
 ('Menachot 6:2 — the two loaves: to the priests, none to the altar', remainder('two_loaves'), 'to_priests_none_to_altar'),
 ('Menachot 6:4 — the Israelite\'s griddle offering: folded to two and four and separated', breaking('griddle'), 'fold_to_two_and_four_and_separate'),
 ('Menachot 6:4 — the priests\': folded, not separated', breaking('pan', 'priests'), 'fold_not_separate'),
 ('Menachot 6:4 — the anointed priest\'s: not folded', breaking('pan', 'anointed_priest'), 'not_folded'),
 # ---- leaven, honey, salt (Menachot 5:1-2, 3:2) ----
 ('Menachot 5:2 — a leavened meal offering: transgression (2:11 quoted)', leaven('any_meal_offering_leavened'), 'transgression'),
 ('Menachot 5:2 — liable for its kneading, its shaping, its baking', leaven('per_step'), 'kneading_shaping_baking_each'),
 ('Menachot 5:1 — the todah\'s loaves come leavened', leaven('todah_loaves'), 'leavened'),
 ('Menachot 5:1 — the two loaves come leavened', leaven('two_loaves'), 'leavened'),
 ('Zevachim 6:5 — the bird rubbed with salt', salt('bird_olah'), 'rubbed_with_salt'),
 ('Menachot 3:2 — did not salt: valid post facto', salt('not_salted_post_facto'), 'valid'),
 # ---- presentation (Menachot 5:5-6) ----
 ('Menachot 5:5 — the five kinds require presentation', presentation('pan'), 'required'),
 ('Menachot 5:6 — the omer: waving and presentation', presentation('omer'), 'waving_and_presentation'),
 ('Menachot 5:6 — the showbread: neither', presentation('showbread'), 'neither'),
 ('Menachot 5:6 — presentation in the west', where('presentation'), 'west'),
 ('Menachot 5:6 — wavings precede presentations', where('order'), 'wavings_precede_presentations'),
 # ---- the first-fruits offering (Menachot 10:4, 10:9, 8:1) ----
 ('Menachot 10:4 — parching: R. Meir singes, the Sages the perforated tube', omer('parching'), 'R._Meir_singed_Sages_perforated_tube'),
 ('Menachot 10:4 — ground in a grits mill', omer('grinding'), 'grits_mill'),
 ('Menachot 10:4 — oil, frankincense, pour, mix, wave, present, scoop, burn, the rest to the priests', omer('after_the_tenth'), 'oil_frankincense_pour_mix_wave_present_scoop_burn_rest_to_priests'),
 ('Menachot 10:9 — no standing grain: from the sheaves', omer('no_standing_grain'), 'from_sheaves'),
 ('Menachot 10:9 — no moist grain: dry', omer('no_moist_grain'), 'dry'),
 ('Menachot 8:1 — the omer from the new and from the land only', omer('source'), 'new_and_from_the_land'),
 ('Menachot 13:11 — pleasing odor said of the beast olah, the bird olah, the meal offering: three', odor_classes(), 3),
 # ---- the bird burnt offering (Zevachim 6:5-7, 7:2, 7:5; Menachot 12:5) ----
 ('Zevachim 7:5 — turtledoves and young pigeons (the species)', bird('species'), 'turtledoves_or_young_pigeons'),
 ('Zevachim 7:5 — turtledoves before their time: disqualified', bird('age', species='turtledove', age='young'), 'invalid'),
 ('Zevachim 7:5 — pigeons past their time: disqualified', bird('age', species='pigeon', age='grown'), 'invalid'),
 ('Zevachim 7:5 — a dried wing, a blinded eye, a cut leg: disqualified', bird('blemish'), 'invalid'),
 ('Zevachim 7:5 — pinched with a knife: disqualified (the fingernail)', bird('instrument'), 'fingernail_not_knife'),
 ('Zevachim 7:5 — pinched with the left hand or at night: not a pinching', bird('left_hand_or_night'), 'not_a_pinching_at_all'),
 ('Menachot 12:5 — a bird, even one', bird('how_many'), 'even_one'),
 ('Zevachim 6:5 — up the ramp, to the ledge, the south-east corner (above)', bird('place'), 'above_the_red_line_south_east_corner'),
 ('Zevachim 6:5-6 — the head pinched and DIVIDED, burned by itself', bird('head'), 'divided_and_burned_by_itself'),
 ('Zevachim 6:5 — its blood pressed on the wall', bird('blood'), 'pressed_on_the_wall'),
 ('Zevachim 6:6 — pressed the head\'s blood only: invalid', bird('blood_head_only'), 'invalid'),
 ('Zevachim 6:6 — pressed the body\'s blood only: valid', bird('blood_body_only'), 'valid'),
 ('Zevachim 6:5 — the crop, the feathers, the entrails to the ash place', bird('crop'), 'cast_beside_the_altar_eastward_to_the_ash_place'),
 ('Zevachim 6:5 — rends and does not divide', bird('rend'), 'rend_by_the_wings_not_divide'),
 ('Zevachim 6:5 — if he divided: valid', bird('divided_anyway'), 'valid'),
 ('Zevachim 6:6 — skipped the crop or the salt after the blood: valid', bird('skipped_crop_or_salt_after_blood'), 'valid'),
 ('Zevachim 6:7 — the bird olah not for its name: valid, not credited', bird('not_for_its_name'), 'valid_not_credited'),
 ('Zevachim 7:2 — done below as a sin offering\'s procedure: invalid', bird('done_below_as_sin_offering_procedure'), 'invalid'),
 ('Zevachim 7:2 — done above as an olah for an olah: valid', bird('done_above_as_olah_for_olah'), 'valid'),
 # ---- THE WRAP (W3, 2026-09-07) — the meal offering and the bird on the world engine ----
 ('THE SCENE — (the vower consecrated, the griddle-vower not credited, the THIS-vower invalid, the partners\' silence, dues to the priests, '
  'most holy, salted, presented, memorials, fistfuls disqualified, fistfuls accepted, the vower not credited, the baker lashed, the loaves '
  'accepted, the omer accepted, its memorial, the bird pinched, its crop cast, salted, its bringer accepted, the young turtledove, the knife, '
  'the misnamed bird not credited, the clock)',
  cell(SCENE, I, 'THE SCENE on the world engine: Menachot 13:1, 12:2, 12:5, 6:2, 1:1-2, 3:5, 5:1-2, 10:9 and Zevachim 6:5-7, 7:5 replayed on '
       'law_minchah — the vow parser, the fistful, the leaven, the omer at its SECOND SEAT (Lev 2:14) and the bird, every value the '
       'daemon\'s by call into this file\'s own cells', ['consecrated', 'not_accepted', 'disqualified', 'salted', 'presented', 'azkarah_to_fire',
       'due_to_priest', 'most_holy', 'accepted', 'barred_from_it', 'lashes', 'pinched', 'crop_cast_to_ash_place']),
  (1, 1, 1, 0, 3, 2, 3, 3, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16)),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print('guard: %d test rows, every expected value a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0, H: 0}
used = []
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    used += [e for e in c['fx'] if e != FX.NONE]
    print('%s %-88s [%s] %s' % ('OK ' if hit else 'MISS', name[:88], c['p'], '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d'
      % (frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n, frac[H], n))
print('computed, not graded: salt from any place even on the Sabbath (MOVE, Sifra Chapter 14 7); the '
      'first-fruits of leaven or honey brought but not ascending (INK 2:12); honey barred from the fire '
      '(INK 2:11); the omer from barley (MOVE, Section 13 4); the burn of the whole bird (INK 1:17) — %s'
      % ', '.join(str(x['v']) for x in (salt('which_salt'), leaven('first_fruits_of_leaven_or_honey'),
                                         leaven('honey_to_the_fire'), omer('grain'), bird('burn'))))
ops = FX.summarize(used)
print('LEDGER OPS this span writes: %s' % ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
print('SCENE: %r — the daemon\'s watch coverage:' % (SCENE,))
_W.print_coverage()
print('effects: every cell carries REGISTERED effects — six discovered in this span\'s own verbs: '
      'azkarah_to_fire (HEAVEN), most_holy (STATUS), salted, presented, pinched (BODY), '
      'crop_cast_to_ash_place (DESTROY) [effects law satisfied]')
if ok == n:
    print()
    print('THE MEAL OFFERING AND THE BIRD BURNT OFFERING COMPILE — the five kinds counted by their own '
          'tokens, the three oil forms censused, the fistful\'s subject and measure read off 2:2, the '
          'memorial three times and most-holy twice, the salt root four times in one verse, the doubled '
          '"you shall offer" carrying the omer\'s fallback, and the bird\'s four verbs — pinch, press, '
          'cast, rend — against Zevachim 6-7\'s walk; the sinner\'s adjuncts answered by a CALL into '
          'the Lev 5 engine.')
else:
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')
