#!/usr/bin/env python3
"""cold_run_clocks.py — THE IMPURITY CLOCKS AND THE PAIRS ENGINE
(2026-09-05, sitting L2 of THE COMPILE DEBT — World/step9/COMPILE_DEBT.md).

Spans: Lev 12:1-8 (the birthing mother — seven or two weeks impure,
thirty-three or sixty-six in the blood of purity, the lamb and the
bird or the two birds) and Lev 15:1-33 (the discharges — the zav's
sightings, his bed, seat and saddle, the propagation formula, the
count of seven and the living water, the eighth-day pair; the
seed-emitter; the menstruant's seven and her partner's; the zavah's
'many days', her count and her pair; the separation clause).

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Niddah
whole, Mishnah Zavim whole, Mishnah Kinnim whole — 126 rows read
whole (the ledger logic/oral_triage/clocks_topic_docket_2026-09-05.md,
coverage computed; the 23 link-driven rows all prior credits; 277
Talmud addresses indexed, opened per gap). The scribal layer the
tractate labels itself (the retroactive fence, the stains, the fixed
periods) is verdicted CONTEXT and not encoded — the code/data law.

The five motions, in order:
 (1) code from the BARE INK — the numbers written (seven, two weeks,
     thirty-three, sixty-six) and their sums computed (forty, eighty);
     the two gates of 12:4; 'the source of her blood'; the pair
     formula at three seats; 'seven days' at five clocks; 'living
     water' at the zav alone; 'count' at two; 'the eighth day' at two;
     the propagation formula censused ('impure until evening' and
     'washes his garments') with the saddle's split clause; the five
     persons of the closing torah; every quantity a PARAMETER (the
     fortieth day, the interval unit, the twenty-four hours, the
     immersion measure);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal
     typed from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Sifra's rows
     (both units' spines, verdicted 2026-09-05) and the Talmud where
     opened, each labeled [MOVE];
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS
     on every verdict.

Cross-span receipts, labeled [IMPORT] and, where a compiled callee
exists, CALLED: cold_run_chatat (the partner's sin offering by the
karet-class domain; the ownership lock for the heirs' pair); cold_run_
vayikra5 (the bird pair's order — the sin offering FIRST); cold_run_
minchah (the bird burnt offering above the red line); Lev 5:9 (the
bird sin offering at the BASE — below); Lev 20:18 (the menstruant's
karet); Lev 1:15 (the wall); Num 19 and Lev 11 (the corpse and the
carrion, carried).
"""
import sqlite3, sys, os, json, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 161, ('the guard counted %d expectations, the tripwire holds 161' % GUARDED)

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

def phrase(book, ch, vs, words):
    t = toks(book, ch, vs); n = len(words)
    return sum(1 for i in range(len(t) - n + 1) if t[i:i + n] == words)

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('a woman who SEEDS and bears',                'Lev', 12, 2, 'תזריע'),
    ('a MALE',                                     'Lev', 12, 2, 'זכר'),
    ('SEVEN days',                                 'Lev', 12, 2, 'שבעת'),
    ('as the days of her menstrual infirmity',     'Lev', 12, 2, 'נדת'),
    ('the EIGHTH day',                             'Lev', 12, 3, 'השמיני'),
    ('thirty',                                     'Lev', 12, 4, 'ושלשים'),
    ('three',                                      'Lev', 12, 4, 'ושלשת'),
    ('in the blood of PURITY',                     'Lev', 12, 4, 'טהרה'),
    ('no HOLY thing shall she touch',              'Lev', 12, 4, 'קדש'),
    ('to the SANCTUARY she shall not come',        'Lev', 12, 4, 'המקדש'),
    ('a FEMALE',                                   'Lev', 12, 5, 'נקבה'),
    ('TWO WEEKS',                                  'Lev', 12, 5, 'שבעים'),
    ('sixty',                                      'Lev', 12, 5, 'וששים'),
    ('six',                                        'Lev', 12, 5, 'וששת'),
    ('when the days are FULL',                     'Lev', 12, 6, 'ובמלאת'),
    ('a lamb of its first year for a burnt offering', 'Lev', 12, 6, 'כבש'),
    ('a pigeon OR a turtledove for a sin offering', 'Lev', 12, 6, 'לחטאת'),
    ('from the SOURCE of her blood',               'Lev', 12, 7, 'ממקר'),
    ('if her hand finds not enough for a lamb',    'Lev', 12, 8, 'די'),
    ('TWO turtledoves',                            'Lev', 12, 8, 'שתי'),
    ('one for a burnt offering and one for a sin offering', 'Lev', 12, 8, 'אחד'),
    # Lev 15
    ('a man with a DISCHARGE',                     'Lev', 15, 2, 'זב'),
    ('from his FLESH',                             'Lev', 15, 2, 'מבשרו'),
    ('his flesh RUNS',                             'Lev', 15, 3, 'רר'),
    ('or his flesh is STOPPED',                    'Lev', 15, 3, 'החתים'),
    ('every BED he lies on',                       'Lev', 15, 4, 'המשכב'),
    ('every VESSEL he sits on',                    'Lev', 15, 4, 'הכלי'),
    ('washes his GARMENTS',                        'Lev', 15, 5, 'בגדיו'),
    ('impure until EVENING',                       'Lev', 15, 5, 'הערב'),
    ('the zav SPITS on the pure',                  'Lev', 15, 8, 'ירק'),
    ('every SADDLE he rides',                      'Lev', 15, 9, 'המרכב'),
    ('whoever touches what is UNDER him',          'Lev', 15, 10, 'תחתיו'),
    ('the one CARRYING them',                      'Lev', 15, 10, 'והנושא'),
    ('his hands not RINSED',                       'Lev', 15, 11, 'שטף'),
    ('the earthen vessel BROKEN',                  'Lev', 15, 12, 'ישבר'),
    ('the wooden vessel RINSED',                   'Lev', 15, 12, 'ישטף'),
    ('when the zav is CLEAN of his flow',          'Lev', 15, 13, 'יטהר'),
    ('he shall COUNT seven days',                  'Lev', 15, 13, 'וספר'),
    ('LIVING water',                               'Lev', 15, 13, 'חיים'),
    ('the eighth day: two turtledoves',            'Lev', 15, 14, 'תרים'),
    ('one a sin offering and one a burnt offering', 'Lev', 15, 15, 'חטאת'),
    ('an emission of SEED',                        'Lev', 15, 16, 'זרע'),
    ('bathes ALL his flesh',                       'Lev', 15, 16, 'בשרו'),
    ('a woman with a flow of BLOOD',               'Lev', 15, 19, 'דם'),
    ('in her FLESH',                               'Lev', 15, 19, 'בבשרה'),
    ('in her SEPARATION',                          'Lev', 15, 19, 'בנדתה'),
    ('her separation is UPON HIM',                 'Lev', 15, 24, 'עליו'),
    ('MANY days',                                  'Lev', 15, 25, 'רבים'),
    ('OUTSIDE the time of her separation',         'Lev', 15, 25, 'בלא'),
    ('or BEYOND her separation',                   'Lev', 15, 25, 'על'),
    ('she shall COUNT seven days',                 'Lev', 15, 28, 'וספרה'),
    ('and AFTER she shall be clean',               'Lev', 15, 28, 'ואחר'),
    ('you shall SEPARATE the children of Israel',  'Lev', 15, 31, 'והזרתם'),
    ('that they die not by defiling My DWELLING',  'Lev', 15, 31, 'משכני'),
    ('this is the torah of the zav',               'Lev', 15, 32, 'תורת'),
    ('and the one infirm in her separation',       'Lev', 15, 33, 'והדוה'),
    ('and the man who lies with an impure woman',  'Lev', 15, 33, 'טמאה'),
]
fired = 0
for name, b, ch, vs, tok in PROBES:
    if count(b, ch, vs, tok) == 0:
        sys.exit('PROBE FAILED: %s — %r not in %s %d:%d' % (name, tok, b, ch, vs))
    fired += 1
print('probes: all %d ink-token probes fired [zero-report law satisfied]' % fired)

# ---- the censuses (asserted: tripwires, not recitals) ----------------
L15 = list(range(1, 34))
IMPURE = {'male': 7, 'female': 14}          # 12:2 seven; 12:5 two weeks (the reading has a mother)
PURITY = {'male': 30 + 3, 'female': 60 + 6}  # 12:4 thirty AND three; 12:5 sixty AND six — written as sums
TOTAL = {s: IMPURE[s] + PURITY[s] for s in IMPURE}
assert TOTAL == {'male': 40, 'female': 80}, TOTAL
assert IMPURE['female'] == 2 * IMPURE['male'] and PURITY['female'] == 2 * PURITY['male']
c_seven = [(12, v) for v in range(1, 9) if phrase('Lev', 12, v, ['שבעת', 'ימים'])] + \
          [(15, v) for v in L15 if phrase('Lev', 15, v, ['שבעת', 'ימים'])]
c_evening = [v for v in L15 if phrase('Lev', 15, v, ['עד', 'הערב'])]
c_evening_n = sum(phrase('Lev', 15, v, ['עד', 'הערב']) for v in L15)
c_wash = [v for v in L15 if count('Lev', 15, v, 'בגדיו')]
c_living = [v for v in L15 if count('Lev', 15, v, 'חיים')]
c_count = [v for v in L15 if count('Lev', 15, v, 'וספר')]
c_eighth = [(15, v) for v in L15 if count('Lev', 15, v, 'השמיני')]
c_pair = [(12, v) for v in range(1, 9) if count('Lev', 12, v, 'תרים')] + [(15, v) for v in L15 if count('Lev', 15, v, 'תרים')]
c_one_one = [(12, v) for v in range(1, 9) if count('Lev', 12, v, 'לעלה') and count('Lev', 12, v, 'לחטאת') and count('Lev', 12, v, 'אחד')] + \
            [(15, v) for v in L15 if count('Lev', 15, v, 'חטאת') and count('Lev', 15, v, 'עלה') and count('Lev', 15, v, 'אחד')]
c_saddle = [v for v in L15 if count('Lev', 15, v, 'מרכב')]
c_bed = [v for v in L15 if count('Lev', 15, v, 'משכב')]
c_seed = [v for v in L15 if phrase('Lev', 15, v, ['שכבת', 'זרע'])]
c_10 = (phrase('Lev', 15, 10, ['יטמא', 'עד', 'הערב']), count('Lev', 15, 10, 'בגדיו'))
c_persons_33 = (count('Lev', 15, 33, 'והדוה'), count('Lev', 15, 33, 'והזב'), count('Lev', 15, 33, 'לזכר'),
                count('Lev', 15, 33, 'ולנקבה'), count('Lev', 15, 33, 'ולאיש'))
c_holy = (toks('Lev', 12, 4).count('קדש'), toks('Lev', 12, 4).count('המקדש'))   # exact tokens: the substring count would read 'sanctuary' as a second 'holy'
c_kodesh_12 = [v for v in range(1, 9) if count('Lev', 12, v, 'קדש')]
assert c_seven == [(12, 2), (15, 13), (15, 19), (15, 24), (15, 28)], c_seven
assert c_evening == [5, 6, 7, 8, 10, 11, 16, 17, 18, 19, 21, 22, 23, 27] and c_evening_n == 15, (c_evening, c_evening_n)
assert c_wash == [5, 6, 7, 8, 10, 11, 13, 21, 22, 27], c_wash
assert c_living == [13] and c_count == [13, 28], (c_living, c_count)
assert c_eighth == [(15, 14), (15, 29)] and c_pair == [(12, 8), (15, 14), (15, 29)], (c_eighth, c_pair)
assert c_one_one == [(12, 8), (15, 15), (15, 30)], c_one_one
assert c_saddle == [9] and c_bed == [4, 5, 21, 23, 24, 26], (c_saddle, c_bed)   # 15:20 says 'whatever she LIES on' (the verb), the noun 'bed' for her first at 15:21
assert c_seed == [16, 17, 18, 32] and c_10 == (1, 1), (c_seed, c_10)
assert c_persons_33 == (1, 1, 1, 1, 1) and c_holy == (1, 1) and c_kodesh_12 == [4], (c_persons_33, c_holy, c_kodesh_12)
print('censuses: impure %s + purity %s = %s (the sums computed from the written numbers, the female double the male) · '
      '"seven days" at %s (five clocks) · "until evening" at 15:%s (%d tokens) · "washes his garments" at 15:%s · '
      'LIVING water at 15:%s alone · "count" at 15:%s · the eighth day at %s · the two-birds formula at %s · '
      '"one and one" at %s · the saddle at 15:%s · the bed at 15:%s · seed at 15:%s · 15:10 split (until-evening %d, '
      'garments %d) · the closing torah\'s five persons %s · 12:4 holy/sanctuary %s'
      % (IMPURE, PURITY, TOTAL, c_seven, c_evening, c_evening_n, c_wash, c_living, c_count, c_eighth, c_pair,
         c_one_one, c_saddle, c_bed, c_seed, c_10[0], c_10[1], c_persons_33, c_holy))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_chatat as CH
    import cold_run_vayikra5 as V5
    import cold_run_minchah as MIN
PARTNER_OFFERING = CH.domain({'intent': 'unwitting', 'karet_when_intentional': True})['v']
PARTNER_DOUBT = CH.domain({'intent': 'unknown'})['v']
HEIR_CHATAT = CH.ownership('dead_father')['v']
_r = V5.graded_offering({'trigger': 'utterance_oath', 'act_is_his_option': True, 'oath_forgotten': True,
                         'means': 'reaches_birds'}, V5.DATA)
BIRD_ORDER = _r[0] if isinstance(_r, tuple) else _r
OLAH_PLACE = MIN.bird('place')['v']
print('routing receipts: cold_run_chatat CALLED — domain(karet-class, unwitting) -> %r; domain(unknown) -> %r; '
      'ownership(dead_father) -> %r; cold_run_vayikra5 CALLED — birds tier -> %r; cold_run_minchah CALLED — '
      'bird olah place -> %r [IMPORT, live calls]' % (PARTNER_OFFERING, PARTNER_DOUBT, HEIR_CHATAT, BIRD_ORDER, OLAH_PLACE))

I, M, A, D, P = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT'
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
ST = 'Sifra, Tazria Parashat Yoledet, '
SZ = 'Sifra, Metzora Parashat Zavim, '

# =====================================================================
# THE CODE — from the ink of Leviticus 12 and 15 alone. Mishnah/Talmud
# appear ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE BIRTHING MOTHER'S CLOCKS (12:2-8) -----------------------
def yoledet(q, sex='male', means='reaches_lamb', **k):
    if q == 'impure_days':
        return cell(IMPURE[sex], I, '12:2 "seven days... as the days of her menstrual infirmity"; 12:5 "two weeks as '
                    'her separation" (the reading has a mother — ' + ST + 'Chapter 2 2)', ['niddah_seven'])
    if q == 'purity_days':
        return cell(PURITY[sex], I, '12:4 "thirty days AND three days"; 12:5 "sixty days AND six days" — sums '
                    'written in the ink, consecutive (' + ST + 'Chapter 1 7, 2 3)', ['blood_of_purity'])
    if q == 'total':
        return cell(TOTAL[sex], I, 'the arithmetic: %d + %d = %d — the fortieth day for the male, the eightieth for '
                    'the female (Mishnah Niddah 6:14 names the sums)' % (IMPURE[sex], PURITY[sex], TOTAL[sex]),
                    ['blood_of_purity'])
    if q == 'union_of_clocks':
        # unknown sex: the stringencies of both — impure for the longer, pure blood only to the shorter total
        imp = max(IMPURE.values()); pure_to = min(TOTAL.values()); doubt_to = max(TOTAL.values())
        return cell('impure_%d_pure_to_%d_niddah_doubt_to_%d' % (imp, pure_to, doubt_to), I, '"sits for a male and a '
                    'female" = the union of the two clocks computed from the written numbers: impure through day %d '
                    '(the female\'s), pure blood only through day %d (the male\'s total), and from there to day %d '
                    'any blood is judged as the menstruant\'s' % (imp, pure_to, doubt_to), ['niddah_seven', 'blood_of_purity'])
    if q == 'holy_touch':
        return cell('barred_from_holy_and_sanctuary', I, '12:4 "no HOLY thing shall she touch, and to the SANCTUARY '
                    'she shall not come" — two gates (%s tokens) on a woman whose blood is PURE: barred from holies, '
                    'not impure' % (c_holy,), ['barred_from_holies'])
    if q == 'tithe':
        return cell('eats_tithe_not_terumah', M, '12:4 "ANY holy thing" [INK] — ' + ST + 'Chapter 1 8: TERUMAH included, '
                    'TITHE excluded (the sanctuary analogy runs on soul-taking); Mishnah Niddah 10:7 agrees she eats '
                    'the tithe', ['barred_from_holies'])
    if q == 'purity_blood_status':
        return cell('pure_though_she_sees', M, '12:4 "she shall SIT in the blood of purity" [INK] — ' + ST +
                    'Chapter 1 7: blood of purity stands though she sees; no examination bears on it', ['blood_of_purity'])
    if q == 'purity_blood_holies':
        return cell('Hillel_as_touching_corpse_impure_Shammai_as_corpse_impure', A, 'Mishnah Niddah 10:6 — the '
                    'houses grade her for holies; the ink bars her from holies (12:4) without naming a grade',
                    ['barred_from_holies'])
    if q == 'immersion_after_seven':
        return cell('Hillel_defiles_wet_and_dry_until_immersed', A, 'Mishnah Niddah 4:3 — the birther who did not '
                    'immerse; the purity-blood status begins at the immersion after the seven or fourteen (the '
                    'houses\' arms)', ['niddah_seven'])
    if q == 'source':
        return cell('from_the_source', I, '12:7 "from the SOURCE of her blood" (מִמְּקֹר) — the womb; 15:19 "in her '
                    'flesh" (' + SZ + 'Section 4 2): the chamber\'s blood impure, the antechamber\'s presumed from it',
                    [FX.NONE])
    if q == 'offering':
        if means == 'reaches_lamb':
            return cell('lamb_olah_and_bird_chatat', I, '12:6 "a lamb of its first year for a burnt offering and a '
                        'pigeon or a turtledove for a sin offering"', ['accepted'])
        return cell('two_birds_one_olah_one_chatat', I, '12:8 "if her hand finds not enough for a lamb: two '
                    'turtledoves or two young pigeons, one for a burnt offering and one for a sin offering" — the '
                    'measure of "enough" is the data channel', ['accepted'])
    if q == 'offering_timing':
        return cell('not_inside_the_term', M, '12:6 "when the days are FULL" [INK] — ' + ST + 'Chapter 3 1: brought '
                    'early, invalid', ['disqualified'])
    if q == 'per_child':
        return cell('one_per_term_R._Yehuda_alternating', M, ST + 'Chapter 3 1 ("for each son, for each daughter") '
                    '+ Chapter 3 6: many births inside one term = ONE offering; R. Yehuda: alternating (Mishnah '
                    'Keritot 2:4 / Niddah — the Tazria round\'s cell)', ['accepted'])
    if q == 'five_doubtful':
        return cell('one_offering_eats_no_debt', M, ST + 'Chapter 3 6 — five doubtful births: one offering and she '
                    'eats, the rest no debt; five certain: one offering, the rest a standing debt — and the '
                    'gold-dinar story', ['accepted'])
    if q == 'withholder':
        return cell('the_chatat_withholds', M, '12:7 "and he shall atone for her" [INK] — ' + ST + 'Chapter 3 5: ONE '
                    'withholds her, not two — the sin offering, "wherever atonement is written it is by the sin '
                    'offering"', ['atoned_forgiven'])
    if q == 'order':
        return cell('olah_written_first_chatat_offered_first', P, '12:8 writes the burnt offering first [INK]; the '
                    'sin offering is offered FIRST — CALLED cold_run_vayikra5 -> %r (Lev 5:8\'s "first"; ' % BIRD_ORDER
                    + ST + 'Chapter 4 3 the order swap)', ['accepted'])
    if q == 'kind_matching':
        return cell('second_follows_first_kind_ben_Azzai_first_brought', M, ST + 'Chapter 4 3 — the second bird '
                    'follows the first\'s kind; ben Azzai: follow the first brought (Mishnah Kinnim 2:5: no '
                    'turtledoves against pigeons — double and bring the burnt offering of the first\'s kind)', [FX.NONE])
    if q == 'heirs':
        return cell('heirs_bring_olah_not_chatat', P, 'the sin offering dies with its owner — CALLED '
                    'cold_run_chatat.ownership(dead_father) -> %r (Lev 4:28\'s "his offering on his sin"); the '
                    'burnt offering is a debt the heirs pay (Mishnah Kinnim 2:5)' % HEIR_CHATAT, ['disqualified'])
    if q == 'caesarean':
        return cell('not_a_birth_R._Shimon_as_born', M, '12:2 "she SEEDS and bears" [INK] — ' + ST + 'Section 1 4: '
                    'through the seeding place; the caesarean excluded, R. Shimon dissents', ['exempt'])
    if q == 'forms':
        return cell('human_form_decides', M, '12:2 "a MALE" [INK] — ' + ST + 'Section 1 7: what has human form; '
                    'fish, locust, and swarm shapes not; Section 1 6: sandal, placenta, formed sac included',
                    ['niddah_seven'])
    if q == 'sac_unformed':
        return cell('no_child', M, ST + 'Section 1 8 — forms unfit for the breath of life excluded (Mishnah Niddah '
                    '3:3: water, blood, matter)', ['exempt'])
    if q == 'formation_threshold':
        return cell(40, D, 'Mishnah Niddah 3:7 — the fortieth day no child, the forty-first a child (R. Yishmael '
                    'eighty-one for the female; the sages forty-one for both) — the data channel', [FX.NONE])
    if q == 'birth_threshold':
        return cell('most_of_the_head_or_most_of_the_body', A, 'Mishnah Niddah 3:5 — normally from most of its head '
                    '(the forehead); cut up or feet-first from most of it; the ink: "the matter depends only on the '
                    'birth" (' + ST + 'Section 1 4)', [FX.NONE])
    if q == 'tumtum':
        return cell('sits_for_both', M, ST + 'Chapter 2 1 — tumtum and androgynous included: the matter depends '
                    'only on the birth', ['niddah_seven', 'blood_of_purity'])
    if q == 'twins':
        return cell('count_from_the_last', M, ST + 'Section 1 9-11 — seven from the LAST child (the corpse-impurity '
                    'analogy), settled by the verse', ['niddah_seven'])
    if q == 'hard_labor_blood':
        return cell('niddah_not_zivah', M, '15:25 "her BLOOD flows" [INK] — ' + SZ + 'Section 5 1: her OWN blood, '
                    'not the child\'s; hard labor hangs on the child (Mishnah Niddah 4:4)', ['niddah_seven'])
    if q == 'hard_labor_duration':
        return cell('R._Meir_40_50_R._Yehuda_month_R._Yosei_R._Shimon_two_weeks', D, SZ + 'Section 5 2 — the '
                    'duration dispute: three recorded settings (Mishnah Niddah 4:5)', [FX.NONE])
    if q == 'hard_labor_in_eighty':
        return cell('bloods_pure_until_the_child_R._Eliezer_defiles_dayo', M, ST + 'Chapter 2 4 — hard labor within '
                    'the eighty of a female: pure until the child emerges; R. Eliezer defiles, holding DAYO against '
                    'every rephrasing (Mishnah Niddah 4:6)', ['blood_of_purity'])
    if q == 'eve_81':
        return cell('Shammai_exempt_Hillel_liable', M, ST + 'Chapter 3 1-2 — the eve of the eighty-first: Beth '
                    'Hillel liable by "or for a daughter" (Mishnah Keritot 1:6)', ['accepted'])
    if q == 'child_pure':
        return cell('she_impure_child_not', M, ST + 'Section 1 8 — she is impure, the child is not (the scapegoat '
                    'cited)', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F2: THE ZAV'S CLOCK (15:2-15) -----------------------------------
def zav(q, sightings=1, **k):
    if q == 'tier':
        if sightings >= 3:
            return cell('full_zav_with_offering', M, '15:2-3 the two clauses ("his flesh runs" / "is stopped") + '
                        '15:14 the pair [INK] — ' + SZ + 'Chapter 5 16: three sightings bring the offering, two do '
                        'not; Chapter 9 9', ['bed_and_seat_defile', 'counts_seven_clean', 'pair_owed'])
        if sightings == 2:
            return cell('bed_seat_living_water_no_offering', M, SZ + 'Chapter 1 5-6 (two sightings make bed and '
                        'seat, "of his flow"), Chapter 5 2-3 (the seven-count too), Chapter 5 16 (no offering); '
                        'Chapter 9 9 = the menstruant\'s grade', ['bed_and_seat_defile', 'counts_seven_clean'])
        return cell('as_a_seed_emitter', M, '15:16 "impure until evening" [INK for the seed-emitter] — ' + SZ +
                    'Chapter 9 8: one sighting = the seed-emitter\'s grade (Beth Hillel; Mishnah Zavim 1:1)',
                    ['impure_until_evening'])
    if q == 'sightings_not_days':
        return cell('sightings', M, SZ + 'Chapter 1 1-2 — his impurity hangs on his DISCHARGE, hers on DAYS; one '
                    'today and two tomorrow, or three in three days or nights, reach three (Mishnah Zavim 1:3)',
                    [FX.NONE])
    if q == 'long_sighting':
        return cell('duration_as_count', M, SZ + 'Chapter 1 3 — one long sighting counts as three by DURATION, '
                    '"like Gad-Yavan to Shiloach: two immersions and two dryings" — the walking clock is the data '
                    'channel; Rabbi\'s hundred-cubit rope at 1 4', [FX.NONE])
    if q == 'interval_unit':
        return cell('immersion_and_drying', D, 'Mishnah Zavim 1:4 — sightings parted by the time of an immersion '
                    'and a drying count separately (the data channel\'s unit)', [FX.NONE])
    if q == 'twilight':
        return cell('certain_impurity_doubtful_offering', A, 'Mishnah Zavim 1:6 — the day is the unit the sightings '
                    'count against; where the day is doubtful the offering is doubtful (the suspended class — '
                    'CALLED cold_run_chatat.domain(unknown) -> %r)' % PARTNER_DOUBT, ['suspends'])
    if q == 'count_start':
        return cell('when_the_flow_stops', I, '15:13 "when the zav is CLEAN of his flow, he shall count seven days" '
                    '— the count begins at the stop (' + SZ + 'Chapter 5 1: a concurrent mark does not hold it)',
                    ['counts_seven_clean'])
    if q == 'count_consecutive':
        return cell('seven_consecutive_zov_voids_all', M, SZ + 'Chapter 5 6 — "one purity": a discharge even on the '
                    'seventh voids all before it (Mishnah Zavim 1:2 tail)', ['counts_seven_clean'])
    if q == 'semen_in_count':
        return cell('Hillel_voids_its_day_Shammai_two', M, SZ + 'Chapter 9 10 — semen voids ONE day of his count, '
                    'not all; Beth Shammai: the two days before it (Mishnah Zavim 1:2); urine voids nothing (9 11)',
                    ['counts_seven_clean'])
    if q == 'self_count':
        return cell('for_himself_R._Eliezer_day1_and_day7_hold', M, '15:13 "he shall count FOR HIMSELF" [INK] — '
                    + SZ + 'Chapter 5 4-5: self-examination jurisdiction; the checked-days dispute (R. Eliezer / R. '
                    'Yehoshua / R. Akiva) and the law follows R. Eliezer (Mishnah Niddah 10:3)', ['counts_seven_clean'])
    if q == 'water':
        return cell('living_water', I, '15:13 "bathe his flesh in LIVING water" — written at 15:%s alone: the '
                    'menstruant and the zavah have no such clause (' % c_living + SZ + 'Chapter 5 8-9: the leper '
                    'does not either; each body its own water)', ['immersed'])
    if q == 'vessels_water':
        return cell('any_water', M, SZ + 'Chapter 5 10 — his vessels rise in any waters', ['immersed'])
    if q == 'interposition':
        return cell('interposition_free_body_and_garments', M, SZ + 'Chapter 5 7 — clothes-washing analogized to '
                    'body-bathing: both interposition-free', ['immersed'])
    if q == 'pair':
        return cell('two_birds_one_chatat_one_olah_eighth_day', I, '15:14-15 "on the EIGHTH day two turtledoves or '
                    'two young pigeons... one a sin offering and one a burnt offering" — the pair formula at %s'
                    % (c_pair,), ['pair_owed'])
    if q == 'pair_binding':
        return cell('first_flow_birds_not_for_second', M, SZ + 'Chapter 5 13 — instance-binding: birds set aside for '
                    'the first flow cannot serve the second; dove and turtledove substitute freely', ['consecrated'])
    if q == 'immersed_before':
        return cell('sunset_before_the_tent', M, '15:14 "and come before the LORD to the tent door" [INK] — ' + SZ +
                    'Chapter 5 14: how does he come unless the sun has set on his immersion? (immersed the day '
                    'before)', ['immersed'])
    if q == 'examination_ways':
        return cell(7, M, SZ + 'Section 1 7 — the SEVEN WAYS before the threshold: food, drink, burden, jumping, '
                    'illness, sight, thought (Mishnah Zavim 2:2)', [FX.NONE])
    if q == 'after_threshold':
        return cell('no_examination_coerced_doubtful_semen_impure', M, SZ + 'Section 1 7 — past the threshold no '
                    'examination: "the matter has legs" (Mishnah Zavim 2:2)', ['bed_and_seat_defile'])
    if q == 'third_sighting_exam':
        return cell('not_examined_R._Eliezer_examined_for_the_offering', A, 'Mishnah Zavim 2:2 — the first and '
                    'second examined, the third not; R. Eliezer: the third too, for the offering', [FX.NONE])
    if q == 'who':
        return cell('all_including_minors_converts_slaves_eunuchs', M, '15:2 "a MAN, a man" (doubled) [INK] — ' + SZ +
                    'Section 1 1: minors included ("to male — any male"); converts and slaves (Mishnah Zavim 2:1)',
                    [FX.NONE])
    if q == 'tumtum':
        return cell('stringencies_of_both_doubt', M, SZ + 'Chapter 1 7-8 — the substance split: blood as a woman, '
                    'white as a man; both stringencies, their impurity a doubt (Mishnah Zavim 2:1)', [FX.NONE])
    if q == 'substance':
        return cell('white_for_the_man_blood_for_the_woman', M, '15:3 "his flesh RUNS" [INK — the moist discharge] '
                    'and 15:19 "BLOOD" [INK] — ' + SZ + 'Chapter 1 7-8: "his impurity is it"', [FX.NONE])
    if q == 'member_only':
        return cell('the_member_outside_only', M, '15:2 "from his FLESH" [INK] — ' + SZ + 'Section 1 4, 1 6: the '
                    'member only, and only OUTSIDE it (the zavah\'s inside-as-outside denied to him; Mishnah Niddah '
                    '5:1)', [FX.NONE])
    if q == 'semen_then_flux':
        return cell('twenty_four_hours_R._Yosei_its_day', D, 'Mishnah Zavim 2:3 — one who saw semen is not defiled '
                    'by flux for twenty-four hours (the data channel\'s parameter at four machines)', [FX.NONE])
    if q == 'liquids':
        return cell('sweat_excrement_pure_tear_wound_milk_liquid_grade_discharge_spittle_urine_severe', M, SZ +
                    'Section 1 13 — THE NINE LIQUIDS TABLE, three tiers; 15:8\'s spittle [INK] in the severe tier',
                    [FX.NONE])
    if q == 'wet_dry':
        return cell('discharge_wet_only_menstrual_blood_wet_and_dry', I, '15:3 "his flesh RUNS with his flow" — a '
                    'liquid by its verb; 15:19 "blood" unconditioned (Mishnah Niddah 7:1: the discharge, spittle, '
                    'semen wet only; menstrual blood and corpse flesh wet and dry)', [FX.NONE])
    if q == 'dead_zav':
        return cell('no_bed_impurity_carries_scribal', M, SZ + 'Chapter 2 12-13 — R. Shimon: only one WITH lying and '
                    'sitting makes beds; the dead zav\'s carry-defilement SELF-LABELED "from the words of the '
                    'scribes" (Mishnah Niddah 10:4: until the flesh rots)', [FX.NONE])
    if q == 'dead_women':
        return cell('Shammai_all_die_niddot_Hillel_only_one_who_died_niddah', A, 'Mishnah Niddah 10:4 — the houses',
                    [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F3: THE PROPAGATION LATTICE (15:4-12, 15:19-27) ------------------
def touch(source, medium, act='touch', during_contact=True, **k):
    """source: zav | niddah | zavah | partner | seed_emitter; medium: bed | seat | saddle | flesh | spittle |
    unwashed_hands | earthenware | wood | under_him | discharge | garment; act: touch | carry | sit."""
    if source == 'zav' and medium == 'bed' and act == 'touch':
        return cell('washes_garments_bathes_until_evening', I, '15:5 "whoever touches his BED washes his garments, '
                    'bathes in water, and is impure until evening"', ['washes_and_bathes', 'impure_until_evening'])
    if source == 'zav' and medium == 'seat' and act == 'sit':
        return cell('washes_garments_bathes_until_evening', I, '15:6 "whoever SITS on the vessel the zav sat on..."',
                    ['washes_and_bathes', 'impure_until_evening'])
    if source == 'zav' and medium == 'flesh':
        return cell('washes_garments_bathes_until_evening', I, '15:7 "whoever touches the FLESH of the zav..."; ' + SZ +
                    'Chapter 3 5: his flesh — hair and nail included, not the dung on him nor his rings',
                    ['washes_and_bathes', 'impure_until_evening'])
    if source == 'zav' and medium == 'spittle':
        return cell('washes_garments_bathes_until_evening', I, '15:8 "if the zav SPITS on the pure..." (' + SZ +
                    'Chapter 3 8: spittle needs touch; phlegm, mucus, spume included)',
                    ['washes_and_bathes', 'impure_until_evening'])
    if source == 'zav' and medium == 'saddle' and act == 'touch':
        return cell('until_evening_no_garment_washing', I, '15:10 "whoever touches anything UNDER him is impure until '
                    'evening" — the FIRST clause of 15:10 writes no garment-washing (%d until-evening, the washing '
                    'only in the carry clause); ' % c_10[0] + SZ + 'Chapter 4 1-2: under the ZAV; the saddle\'s '
                    'touch does not defile garments', ['impure_until_evening'])
    if source == 'zav' and medium == 'saddle' and act == 'carry':
        return cell('washes_garments_bathes_until_evening', I, '15:10 "and the one CARRYING them washes his garments, '
                    'bathes, and is impure until evening" — the second clause: THE INVERTED PAIR, touch weak, carry '
                    'strong (' + SZ + 'Chapter 4 2-3)', ['washes_and_bathes', 'impure_until_evening'])
    if source == 'zav' and medium == 'bed' and act == 'carry':
        return cell('washes_garments_bathes_until_evening', M, SZ + 'Chapter 4 3 — bed and seat carry included by '
                    '"the one carrying THEM" (15:10); Mishnah Zavim 2:4: the bed defiles in seven ways — the five '
                    'and touch and carry', ['washes_and_bathes', 'impure_until_evening'])
    if source == 'zav' and medium == 'unwashed_hands':
        return cell('washes_garments_bathes_until_evening', I, '15:11 "whomever the zav touches with his hands not '
                    'RINSED in water washes his garments..." (' + SZ + 'Chapter 4 7: R. Elazar b. Arach — "from here '
                    'the sages supported the washing of hands")', ['washes_and_bathes', 'impure_until_evening'])
    if source == 'zav' and medium == 'earthenware':
        return cell('broken', I, '15:12 "the earthen vessel the zav touches shall be BROKEN" (' + SZ + 'Section 3 1-2: '
                    'from its airspace or by shaking)', ['break_earthen_vessel'])
    if source == 'zav' and medium == 'wood':
        return cell('rinsed_in_water', I, '15:12 "and every wooden vessel shall be RINSED in water"', ['immersed'])
    if source == 'zav' and medium == 'discharge':
        return cell('two_and_one_toucher_and_mover_R._Eliezer_carrier', M, SZ + 'Chapter 4 4 — R. Eliezer: carrying '
                    'his discharge, spittle, urine, semen, and menstrual blood defiles too (Mishnah Zavim 5:7); the '
                    'discharge itself impure (Section 1 8-9)', ['impure_until_evening'])
    if source == 'niddah' and medium == 'flesh':
        return cell('until_evening', I, '15:19 "whoever touches her is impure until evening" (' + SZ + 'Section 4 '
                    '9-10: washes clothes, defiles no person and no earthenware)', ['impure_until_evening'])
    if source == 'niddah' and medium in ('bed', 'seat'):
        return cell('washes_garments_bathes_until_evening', I, '15:21-22 "whoever touches her BED... any VESSEL she '
                    'sits on — washes his garments, bathes, impure until evening"; 15:20 the bed and seat impure',
                    ['washes_and_bathes', 'impure_until_evening'])
    if source == 'niddah' and medium == 'on_the_bed':
        return cell('until_evening', I, '15:23 "if it is on the bed or on the vessel she sits on — when he touches '
                    'it, impure until evening" (' + SZ + 'Section 4 11-13: the designated bed and seat, in both '
                    'directions)', ['impure_until_evening'])
    if source == 'zavah' and medium in ('bed', 'seat'):
        return cell('as_her_niddah_bed', I, '15:26 "every bed she lies on all the days of her flow shall be to her AS '
                    'THE BED OF HER SEPARATION; every vessel she sits on impure as the impurity of her separation"; '
                    '15:27 the toucher washes', ['bed_and_seat_defile', 'washes_and_bathes'])
    if source == 'partner' and medium == 'bed':
        return cell('light_foods_and_liquids_only', M, '15:24 "every bed he lies on is impure" [INK] — ' + SZ +
                    'Chapter 7 3-4: THE DEMOTION OPERATOR — "her separation is upon him" makes him seven days like '
                    'her, but the verse detached him from the severe to the light: his bed defiles only foods and '
                    'liquids; his bed = his touch (Mishnah Zavim 5:11)', ['bed_and_seat_defile'])
    if source == 'seed_emitter' and medium == 'flesh':
        return cell('bathes_all_his_flesh_until_evening', I, '15:16 "a man from whom seed goes out bathes ALL his '
                    'flesh in water and is impure until evening" — no garment clause for himself',
                    ['immersed', 'impure_until_evening'])
    if source == 'seed_emitter' and medium == 'garment':
        return cell('washed_until_evening', I, '15:17 "every garment and every skin on which there is seed is washed '
                    'in water and impure until evening"', ['impure_until_evening'])
    if source == 'seed_emitter' and medium == 'woman':
        return cell('both_bathe_until_evening', I, '15:18 "and a woman with whom a man lies with seed — they bathe '
                    'in water and are impure until evening"', ['immersed', 'impure_until_evening'])
    return cell('unknown', I, '', [FX.NONE])

def degrees(q):
    if q == 'during_contact':
        return cell('garments_defiled_foods_liquids_first_hands_second_not_persons_not_earthenware', M, '15:5-7 '
                    '"washes his GARMENTS" [INK: garments defiled while touching] — ' + SZ + 'Section 2 9-11: during '
                    'contact garments defile; THE TWO-STAGE TABLE (Mishnah Zavim 5:1, R. Yehoshua\'s rule)', ['washes_and_bathes'])
    if q == 'after_separation':
        return cell('liquids_first_foods_and_hands_second_no_garments', M, SZ + 'Section 2 9, 2 11 — separated, no '
                    'longer: liquids first, foods and hands second, no garments (Mishnah Zavim 5:1)', [FX.NONE])
    if q == 'father_of_impurity':
        return cell('defiles_two_disqualifies_one_separated_one_and_one', M, SZ + 'Section 2 11 — touching the zav, '
                    'zavah, menstruant, birther, leper, bed, seat: two and one; separated one and one; toucher, '
                    'mover, carrier, carried alike (Mishnah Zavim 5:6)', [FX.NONE])
    if q == 'general':
        return cell('one_and_one_except_a_person', A, 'Mishnah Zavim 5:10 — whoever touches any father of impurity '
                    'defiles one and disqualifies one, except a person', [FX.NONE])
    if q == 'madaf_above':
        return cell('foods_liquids_vessels_above_light_bed_below_severe', M, SZ + 'Section 3 3-7 — the wood-vessel '
                    'clause teaches the MADAF: what rides ABOVE the zav takes light impurity; below him bed not '
                    'madaf, above him madaf not bed — each corner closed by its verse (Mishnah Zavim 4:6, 5:2)',
                    ['bed_and_seat_defile'])
    if q == 'zav_vs_corpse':
        return cell('zav_bed_seat_below_madaf_above_corpse_tent_and_seven', M, SZ + 'Section 3 3-7 + Mishnah Zavim '
                    '4:6 — the stringencies of each; the corpse Num 19 [IMPORT, carried]', [FX.NONE])
    if q == 'carried_on_zav':
        return cell('impure', M, SZ + 'Section 3 3 (the madaf) — whatever is carried on the zav is impure (Mishnah '
                    'Zavim 5:2)', ['impure_until_evening'])
    if q == 'zav_carried_on':
        return cell('pure_except_bed_seat_person', M, SZ + 'Section 3 5 — below him the bed, not the madaf; the '
                    'person by 15:10 [INK] (Mishnah Zavim 5:2)', [FX.NONE])
    if q == 'majority_grid':
        return cell('by_the_zav_impure_by_the_bed_part_cases_pure', M, SZ + 'Section 4 14 — most of the impure on '
                    'the pure or part, most of the pure on the impure or part: BY THE ZAV impure, BY THE BED the '
                    'part-cases pure (Mishnah Zavim 5:4-5, R. Shimon\'s split)', [FX.NONE])
    if q == 'carried_majority':
        return cell('only_the_seat_under_the_body', M, SZ + 'Chapter 2 13, Section 4 14 — the carried-majority rule: '
                    'on six chairs only the one under the body; five benches lengthwise impure, widthwise pure '
                    '(Mishnah Zavim 4:4)', ['bed_and_seat_defile'])
    if q == 'pressure_column':
        return cell('all_ten_impure', M, SZ + 'Chapter 3 1 — ten seats stacked, even atop a massive stone: where the '
                    'zav sits and defiles, the pure sits and is defiled (Mishnah Zavim 4:5)', ['bed_and_seat_defile'])
    if q == 'scale_pan':
        return cell('zav_sinks_pure_they_sink_impure', I, '15:10 "the one CARRYING them" — when the bed and seat sink '
                    'they carried him; when he sinks they did not (Mishnah Zavim 4:5)', ['bed_and_seat_defile'])
    if q == 'shaking':
        return cell('moved_as_touched', M, SZ + 'Section 3 2 — "a touch that is in ALL of it — this is its being '
                    'moved": the boat, the raft, the shaky plank defile by treading (Mishnah Zavim 3:1); the firm '
                    'do not (3:3); the impure striking the pure impure, the pure striking the impure pure', ['bed_and_seat_defile'])
    if q == 'knock_loaf':
        return cell('pure', A, 'Mishnah Zavim 4:1 — a zav knocked on a balcony and a terumah loaf fell: pure (the '
                    'knock\'s force is not his carrying)', [FX.NONE])
    if q == 'firm_supports':
        return cell('pure', A, 'Mishnah Zavim 4:2 — the beam, the frame, the gutter, the oven, the base: pure; 4:3 the '
                    'door, bolt, oar, the chest and box impure (R. Nechemia and R. Shimon purify) — the data lists',
                    [FX.NONE])
    if q == 'support_majority':
        return cell('bed_four_legs_impure_beast_four_legs_pure', A, 'Mishnah Zavim 4:7 — the bed cannot stand on '
                    'three, the beast can; one cloak under two legs impure', [FX.NONE])
    if q == 'five_ways':
        return cell(5, M, SZ + 'Chapter 2 7 — standing, sitting, lying, hanging, leaning all included (Mishnah '
                    'Zavim 2:4: the zav defiles the bed in five ways; the bed a person in seven)', [FX.NONE])
    if q == 'seven_ways':
        return cell(7, M, SZ + 'Chapter 2 7 + Section 2 1-2 + Chapter 4 3 — the five, and by touch and by carrying',
                    [FX.NONE])
    if q == 'designated_bed':
        return cell('serves_lying_with_its_work_stand_up_test', M, '15:4 "every BED he lies on" [INK: the noun of '
                    'lying] — ' + SZ + 'Chapter 2 1-4: not the beam, not the door, not the reed mat — the DESIGNATED '
                    'bed; excluded is whatever one tells "stand up, let us do our work"', [FX.NONE])
    if q == 'midras_subset':
        return cell('midras_class_within_corpse_susceptible', A, 'Mishnah Niddah 6:3 — whatever is defiled by '
                    'treading is defiled by corpse contact, not the reverse; the midras class is the designated '
                    'bed and seat', [FX.NONE])
    if q == 'broken_bed':
        return cell('pure', M, SZ + 'Section 2 3 — a broken bed is pure', [FX.NONE])
    if q == 'terumah_fence':
        return cell('pure_for_synagogue_members_impure_for_terumah', A, 'Mishnah Zavim 3:2 — the doubtful shakings '
                    '(closing and opening, the pit, the ropes, weaving, the donkey\'s load): the fence self-labeled '
                    'as terumah\'s', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F4: THE MENSTRUANT AND HER PARTNER (15:19-24) ----------------------
def niddah(q, **k):
    if q == 'days':
        return cell(7, I, '15:19 "seven days she shall be in her separation" — "seven days" at %s (five clocks)'
                    % (c_seven,), ['niddah_seven'])
    if q == 'count_anchor':
        return cell('from_the_sighting', I, '15:19 "blood shall be her flow in her flesh — seven days" — the seven '
                    'run from the sighting (Mishnah Niddah 1:2: she counts only from the hour she saw; ' + SZ +
                    'Section 4 5-7: nights included, consecutive)', ['niddah_seven'])
    if q == 'no_early_immersion':
        return cell('all_seven', M, SZ + 'Section 4 8 — in her separation she stays all seven; 15:28\'s "and AFTER" = '
                    'after all (Chapter 9 1); the seventh ends at its sunset (Mishnah Niddah 10:2)', ['niddah_seven'])
    if q == 'blood_not_stain':
        return cell('blood_not_a_stain', I, '15:19 "BLOOD shall be her flow" (דָּם) — the token is the rule: Mishnah '
                    'Niddah 8:3 quotes it, "blood, not a stain"; 15:25 likewise for the flux (6:13: stains carry no '
                    'flux)', [FX.NONE])
    if q == 'inside_as_outside':
        return cell('she_inside_he_outside', M, '15:19 "in her FLESH" [INK] — ' + SZ + 'Section 4 4: she defiles '
                    'inside as outside; the zav and the seed-emitter only when it goes out (Section 1 6; Mishnah '
                    'Niddah 5:1)', [FX.NONE])
    if q == 'day_old_girl':
        return cell('susceptible', M, '15:19 "a WOMAN" [INK] — ' + SZ + 'Section 4 1: a day-old girl susceptible to '
                    'menstrual impurity (Mishnah Niddah 5:3; the Cutheans\' daughters from the cradle, 4:1)',
                    ['niddah_seven'])
    if q == 'ten_day_girl':
        return cell(7 + 3, I, 'the ten computed: seven of separation (15:19) plus the three that make a flux (15:25 '
                    '"many days" = three, ' + SZ + 'Section 5 9) — a ten-day-old girl can be a zavah (Mishnah Niddah '
                    '5:3; Section 4 1)', ['counts_seven_clean'])
    if q == 'five_bloods':
        return cell('red_black_saffron_earth_water_diluted_Shammai_add_two_Hillel_purify', D, SZ + 'Section 4 3 and '
                    + ST + 'Chapter 3 6 — the five impure bloods (one classifier, two seats); the shades\' '
                    'calibration the data channel (Mishnah Niddah 2:6-7)', [FX.NONE])
    if q == 'partner_days':
        return cell(7, I, '15:24 "her separation is UPON HIM, and he is impure seven days"', ['niddah_seven'])
    if q == 'partner_bed':
        return touch('partner', 'bed')
    if q == 'partner_offering':
        return cell(PARTNER_OFFERING, P, 'the menstruant is karet-class (Lev 20:18 [IMPORT]) — the unwitting partner '
                    'brings the sin offering: CALLED cold_run_chatat.domain -> %r (Mishnah Niddah 2:2: found on his '
                    'cloth — both impure and liable to an offering)' % PARTNER_OFFERING, ['atoned_forgiven'])
    if q == 'partner_after_time':
        return cell('impure_in_doubt_exempt_from_offering', P, 'Mishnah Niddah 2:2 — found on hers after a time: '
                    'impure in doubt (the fence), exempt from the offering — the doubt class CALLED -> %r'
                    % PARTNER_DOUBT, ['suspends'])
    if q == 'partner_age':
        return cell('nine_years_and_a_day', M, SZ + 'Chapter 7 1 — nine years and a day (Mishnah Niddah 5:5); the '
                    'girl three years and a day (Chapter 6 7; 5:4)', [FX.NONE])
    if q == 'partner_count':
        return cell('from_the_last_lying', M, SZ + 'Chapter 7 6-9 — count seven from the LAST lying, closed by the '
                    'verse', ['niddah_seven'])
    if q == 'partner_leper':
        return cell('not_the_leper_womans_partner', M, SZ + 'Chapter 7 2 — "her": not the leprous woman\'s partner',
                    [FX.NONE])
    if q == 'she_defiles_him_not_reverse':
        return cell('she_defiles_partner_zav_not_his', M, '15:24 [INK for her]; ' + SZ + 'Chapter 8 8-9: the zav does '
                    'not defile his partner — the a-fortiori blocked, "in clean language"', [FX.NONE])
    if q == 'hard_labor':
        return yoledet('hard_labor_blood')
    if q == 'zav_vs_niddah_wet_dry':
        return zav('wet_dry')
    return cell('unknown', I, '', [FX.NONE])

# ---- F5: THE ZAVAH'S WINDOW (15:25-30) ---------------------------------
DAYS_FEW = 2; DAYS_MANY = 3   # "days" = two, "many" = three — Sifra Section 5 5-9 (R. Akiva's minimal seizure)
def zavah(q, **k):
    if q == 'days_many':
        return cell((DAYS_FEW, DAYS_MANY), M, '15:25 "MANY DAYS outside the time of her separation" [INK] — ' + SZ +
                    'Section 5 5-9: "days" = TWO (R. Akiva: grasp the few, you grasped), "many" = THREE, not five '
                    '("it does not say days AND many")', [FX.NONE])
    if q == 'window':
        return cell(11, M, '15:25 "outside the time of her separation, or BEYOND her separation" [INK: the two '
                    'placements] — ' + SZ + 'Chapter 8 1-3: the window opens AFTER the separation week; day 1 '
                    'adjacent, days 2-10 by the fit-for-counting rule, day 11 by "not at the time", day 12 EXCLUDED — '
                    'built inclusion by inclusion (Mishnah Niddah 4:7: the eleven days)', [FX.NONE])
    if q == 'tiers':
        return cell('one_watches_a_day_two_bed_and_seat_three_full', M, SZ + 'Chapter 8 4-7 — two sightings and one '
                    'reach zavah grades ("the days of the flow"); the watcher one day against one day; three = the '
                    'full zavah with the count and the pair', ['bed_and_seat_defile'])
    if q == 'watcher':
        return cell('one_day_against_one_day', M, SZ + 'Chapter 8 5 — never two for two (Mishnah Niddah 4:7\'s '
                    'day-watcher)', [FX.NONE])
    if q == 'count':
        return cell('seven_after_the_flow_stops', I, '15:28 "if she is clean of her flow she shall COUNT seven days, '
                    'and after she shall be clean" — "count" at 15:%s (his and hers)' % (c_count,), ['counts_seven_clean'])
    if q == 'water':
        return cell('no_living_water_written', I, 'no water clause at 15:28 — "living water" stands at 15:%s alone '
                    '(' % c_living + SZ + 'Chapter 5 8-9)', ['immersed'])
    if q == 'pair':
        return cell('two_birds_one_chatat_one_olah_eighth_day', I, '15:29-30 "on the eighth day she takes two '
                    'turtledoves or two young pigeons... one a sin offering and one a burnt offering" — the third '
                    'seat of the pair formula (%s)' % (c_one_one,), ['pair_owed'])
    if q == 'day_eleven':
        return cell('Shammai_bed_seat_and_offering_Hillel_exempt', M, SZ + 'Chapter 8 3 — day eleven by "not at the '
                    'time", day twelve excluded: a sighting on the eleventh, immersed at evening — the houses divide '
                    'on the offering (Mishnah Niddah 10:8); within the eleven both agree bed, seat, and offering',
                    ['bed_and_seat_defile'])
    if q == 'immersed_after_act':
        return cell('R._Shimon_pure_but_the_sages_said_do_not', M, SZ + 'Chapter 9 2 — immersed after the act she is '
                    'pure for purities, "but the sages said DO NOT DO SO, lest it come to doubt": the prudential '
                    'fence beside the law', [FX.NONE])
    if q == 'her_pair_binding':
        return cell('first_flow_birds_not_for_second', M, SZ + 'Chapter 9 3 — her instance-binding, as his',
                    ['consecrated'])
    if q == 'twenty_five':
        v = DAYS_FEW + 7 + DAYS_FEW + 14
        return cell(v, M, SZ + 'Section 5 3 — hard labor %d days without flux status: two (fit days) + seven '
                    '(separation, 15:19) + two + fourteen (the labor\'s two weeks, Section 5 2) — computed; '
                    'twenty-six impossible' % v, [FX.NONE])
    if q == 'hundred':
        v = DAYS_FEW + 7 + DAYS_FEW + TOTAL['female'] + 7 + DAYS_FEW
        return cell(v, M, SZ + 'Section 5 4 — seeing %d days without flux status: two + seven + two + EIGHTY (the '
                    'female\'s total, 12:5\'s sums) + seven + two — computed' % v, [FX.NONE])
    if q == 'adornment':
        return cell('R._Akiva_she_may_adorn', M, SZ + 'Chapter 9 12 — the first elders forbade until immersion; R. '
                    'Akiva came and taught: the matter leads to hatred — she may adorn (the law revised on '
                    'marriage-preservation grounds, both arms kept)', [FX.NONE])
    if q == 'presence':
        return cell('separation_warning_punishment_presence_among_them', I, '15:31 "you shall SEPARATE... that they '
                    'die not by defiling My DWELLING which is IN THEIR MIDST" — ' + SZ + 'Chapter 9 7: warning, '
                    'punishment, and the Presence clause', ['death_by_heaven'])
    if q == 'five_persons':
        return cell(5, I, '15:32-33 "this is the torah of the zav, the seed-emitter, the one infirm in her '
                    'separation, the one with a flow male or female, and the man who lies with an impure woman" — '
                    'the closing torah\'s five persons, each token found at 15:33 %s' % (c_persons_33,), [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F6: THE PAIRS ENGINE (12:8, 15:14-15, 15:29-30 → Mishnah Kinnim) ----
def pairs(q, **k):
    if q == 'places':
        return cell('bird_chatat_below_bird_olah_above', P, 'Lev 5:9 "pressed out at the BASE" — below; Lev 1:15 "on '
                    'the WALL" — above [IMPORT]; CALLED cold_run_minchah.bird(place) -> %r; the beast\'s reversed '
                    '(Mishnah Kinnim 1:1)' % OLAH_PLACE, [FX.NONE])
    if q == 'obligation':
        return cell('one_chatat_one_olah', I, '"one for a burnt offering and one for a sin offering" at %s — the '
                    'obligation pair; vows and free-will all burnt offerings (Mishnah Kinnim 1:1)' % (c_one_one,),
                    ['pair_owed'])
    if q == 'vow_vs_freewill':
        return cell('vow_responsible_freewill_not', A, 'Mishnah Kinnim 1:1 — "upon me" vs "this": responsibility if '
                    'they died or were stolen (the vow parser\'s cell, Lev 27\'s span)', [FX.NONE])
    if q == 'spec_chatat_in_spec_olah':
        return cell('all_die', I, 'a specified sin offering among specified burnt offerings, even one in ten '
                    'thousand: no bird can be placed without risking the wrong place (1:1 "changed either — '
                    'invalid") — all die (Mishnah Kinnim 1:2)', ['birds_die'])
    if q == 'spec_in_chovah':
        n = k.get('chovah_pairs', 1)
        return cell(n, I, 'a specified sin offering mixed with %d obligation pair(s): the priest may do only the '
                    'obligation\'s sin-offering count below — the constraint "one and one" per pair: valid = %d, '
                    'whatever the ratio (Mishnah Kinnim 1:2, 3:5)' % (n, n), ['pair_owed'])
    if q == 'chovah_in_chovah':
        a, b = k['a'], k['b']
        if a == b:
            return cell('half_valid_half_invalid', I, 'two women\'s pairs mixed, %d and %d: the priest does half '
                        'below and half above; either woman\'s birds may have gone either way — half valid, half '
                        'invalid (Mishnah Kinnim 1:3)' % (a, b), ['pair_owed'])
        return cell(min(a, b), I, 'unequal counts %d and %d: THE SMALLER IS VALID — the smaller woman\'s pairs are '
                    'the only ones sure to have one of each (Mishnah Kinnim 1:3)' % (a, b), ['pair_owed'])
    if q == 'one_name_two_names':
        return cell('birth_and_birth_one_name_birth_and_flux_two', I, 'the NAME is the chapter: Lev 12\'s birth, Lev '
                    '15\'s flux (Mishnah Kinnim 1:4); the rule holds one name or two, one woman or two', [FX.NONE])
    if q == 'joint_purchase':
        return cell('priest_offers_whichever', A, 'Mishnah Kinnim 1:4 — R. Yosei: two women who bought jointly or '
                    'gave the money: the priest\'s discretion', [FX.NONE])
    if q == 'flew_to_air':
        return cell('take_a_mate_for_the_second', I, 'an unspecified pair, a bird flew or died: the remaining bird '
                    'is still "one" of a pair — take a mate (Mishnah Kinnim 2:1)', ['pair_owed'])
    if q == 'flew_among_offered':
        return cell('invalid_and_disqualifies_one_opposite', I, 'the flying bird cannot be placed and disqualifies '
                    'one opposite it in the set it joined (Mishnah Kinnim 2:1)', ['birds_die'])
    if q == 'two_women_two_pairs':
        return cell('one_going_one_returning_repeated_nothing_lost', I, 'two pairs each: a flight disqualifies one '
                    'going, one returning; repeated flights lose nothing more, "for even mixed there are no fewer '
                    'than two" (Mishnah Kinnim 2:2)', [FX.NONE])
    if q == 'chain':
        # women 1..7 with i pairs each; each round trip: every intermediate woman -2, the turning point -1,
        # the origin -1 on the first trip (her own bird left); floors at zero
        valid = list(range(1, 8)); trips = k.get('trips', 1); out = []
        for t in range(trips):
            first = next((i for i, v in enumerate(valid) if v > 0), None)
            for i in range(7):
                if i == 6: valid[i] = max(0, valid[i] - 1)
                elif t == 0 and i == 0: valid[i] = max(0, valid[i] - 1)
                else: valid[i] = max(0, valid[i] - 2)
            out.append(list(valid))
        return cell(out[-1], I, 'THE CHAIN OF SEVEN computed: each round trip costs every intermediate woman two '
                    '(one going, one returning), the seventh one (the turning point), the first her own bird — '
                    'after %d trip(s): %s (Mishnah Kinnim 2:3)' % (trips, out[-1]), ['birds_die'])
    if q == 'chain_from_dead':
        return cell('all_die', I, 'flew from among the dead to all — all die (Mishnah Kinnim 2:3 tail)', ['birds_die'])
    if q == 'stumah_meforeshet':
        return cell('take_a_mate_returned_all_die', I, 'flew from the unspecified to the specified — a mate for the '
                    'second; returned, or flew from the specified first — all die (Mishnah Kinnim 2:4)', ['birds_die'])
    if q == 'middle_to_sides':
        return cell('nothing_lost_returned_middle_die', I, 'sin offerings here, burnt offerings there, an '
                    'unspecified pair between: one each way — declare each as what it joined; returned to the '
                    'middle — the middle die (Mishnah Kinnim 2:5)', ['birds_die'])
    if q == 'no_turtledoves_against_pigeons':
        return yoledet('kind_matching')
    if q == 'died':
        return yoledet('heirs')
    if q == 'unconsulted_equal':
        return cell('half_valid_half_invalid', I, 'the priest unconsulted, equal counts (one and one, two and two): '
                    'all above — half (the burnt offerings); all below — half; half and half — each half is half '
                    '(Mishnah Kinnim 3:1)', ['pair_owed'])
    if q == 'unconsulted_unequal':
        return cell('all_above_half_all_below_half_half_and_half_the_greater', I, 'unequal counts: all above or all '
                    'below — half; half above and half below — THE GREATER is valid; the rule: divisible without one '
                    'woman\'s — half; not — the greater (Mishnah Kinnim 3:2)', ['pair_owed'])
    if q == 'unconsulted_specified':
        return cell('half_and_half_or_both_invalid', I, 'a sin offering for this one and a burnt offering for that: '
                    'all above or all below — half; half and half — BOTH invalid, "for I say the sin offering was '
                    'offered above and the burnt offering below" (Mishnah Kinnim 3:3)', ['birds_die'])
    if q == 'unconsulted_mixed_four':
        return cell('only_the_unspecified_valid_divided', I, 'a sin offering, a burnt offering, an unspecified pair, '
                    'a specified pair: half and half — only the unspecified is valid, divided between them '
                    '(Mishnah Kinnim 3:4)', ['pair_owed'])
    if q == 'vowed_pair':
        vow_olahs = 2; oblig = (1, 1)   # the vow: two burnt offerings (1:1); the obligation: one and one (12:8)
        above = vow_olahs + oblig[1]; below = oblig[0]
        return cell((above, below), I, '"a pair upon me when I bear a male" and she bore: TWO pairs — the vow\'s '
                    'two burnt offerings (Kinnim 1:1) and the obligation\'s one and one (12:8): %d above, %d below '
                    '(Mishnah Kinnim 3:6)' % (above, below), ['pair_owed'])
    if q == 'vowed_pair_two_two':
        return cell('one_more_above_one_kind_two_of_two_kinds', A, 'Mishnah Kinnim 3:6 — did two and two '
                    'unconsulted: one more bird above of one kind, two of two kinds; specified her vow three or '
                    'four; fixed it five or six; unknown — four for the vow, two for the obligation, one sin '
                    'offering (ben Azzai two)', ['pair_owed'])
    return cell('unknown', I, '', [FX.NONE])

# ---- (2) TEST DATA — the Mishnah rows, read whole from the shelf ------
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
NID = load('niddah'); ZAV = load('zavim'); KIN = load('kinnim')
def mrow(book, ch, m, must):
    txt = strip({'Niddah': NID, 'Zavim': ZAV, 'Kinnim': KIN}[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Niddah', 1, 2, 'שראתה'), ('Niddah', 1, 7, 'טהר'), ('Niddah', 2, 2, 'קרבן'), ('Niddah', 2, 5, 'המקור'),
    ('Niddah', 2, 6, 'דמים'), ('Niddah', 3, 3, 'מרקם'), ('Niddah', 3, 5, 'טמטום'), ('Niddah', 3, 6, 'ולנדה'),
    ('Niddah', 3, 7, 'ארבעים'), ('Niddah', 4, 1, 'מעריסתן'), ('Niddah', 4, 4, 'המקשה'), ('Niddah', 4, 5, 'שבתות'),
    ('Niddah', 4, 6, 'דיו'), ('Niddah', 4, 7, 'עשר'), ('Niddah', 5, 1, 'דפן'), ('Niddah', 5, 2, 'באמה'),
    ('Niddah', 5, 3, 'עשרה'), ('Niddah', 5, 5, 'תשע'), ('Niddah', 6, 3, 'מדרס'), ('Niddah', 6, 13, 'זוב'),
    ('Niddah', 6, 14, 'שמונים'), ('Niddah', 7, 1, 'יבשין'), ('Niddah', 8, 3, 'כתם'), ('Niddah', 10, 2, 'שביעי'),
    ('Niddah', 10, 3, 'אליעזר'), ('Niddah', 10, 4, 'במשא'), ('Niddah', 10, 6, 'טהר'), ('Niddah', 10, 7, 'במעשר'),
    ('Niddah', 10, 8, 'עשר'),
    ('Zavim', 1, 1, 'קרי'), ('Zavim', 1, 2, 'יומו'), ('Zavim', 1, 3, 'גמור'), ('Zavim', 1, 4, 'וספוג'),
    ('Zavim', 1, 5, 'לשילוח'), ('Zavim', 1, 6, 'השמשות'), ('Zavim', 2, 1, 'וקטן'), ('Zavim', 2, 2, 'דרכים'),
    ('Zavim', 2, 3, 'לעת'), ('Zavim', 2, 4, 'חמשה'), ('Zavim', 3, 1, 'בספינה'), ('Zavim', 3, 2, 'לתרומה'),
    ('Zavim', 3, 3, 'נופל'), ('Zavim', 4, 1, 'תרומה'), ('Zavim', 4, 4, 'ספסלים'), ('Zavim', 4, 5, 'טליות'),
    ('Zavim', 4, 6, 'מדף'), ('Zavim', 4, 7, 'רגלי'), ('Zavim', 5, 1, 'תחלה'), ('Zavim', 5, 2, 'הנדבך'),
    ('Zavim', 5, 4, 'חבורי'), ('Zavim', 5, 6, 'ופוסל'), ('Zavim', 5, 7, 'הנושא'), ('Zavim', 5, 8, 'המרכב'),
    ('Zavim', 5, 10, 'הכלל'), ('Zavim', 5, 11, 'נדה'),
    ('Kinnim', 1, 1, 'למטה'), ('Kinnim', 1, 2, 'ברבוא'), ('Kinnim', 1, 3, 'המעט'), ('Kinnim', 1, 4, 'לידה'),
    ('Kinnim', 2, 1, 'זוג'), ('Kinnim', 2, 2, 'הפסיד'), ('Kinnim', 2, 3, 'השביעית'), ('Kinnim', 2, 4, 'ימותו'),
    ('Kinnim', 2, 5, 'היורשין'), ('Kinnim', 3, 1, 'נמלך'), ('Kinnim', 3, 2, 'המרבה'), ('Kinnim', 3, 3, 'פסול'),
    ('Kinnim', 3, 4, 'סתומה'), ('Kinnim', 3, 5, 'מנין'), ('Kinnim', 3, 6, 'שלש'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows token-verified in their own ink (Niddah, Zavim, Kinnim read whole — the '
      'topic docket)' % len(SHEET))

TESTS = [
 # ---- the birthing mother (Lev 12; Niddah 3, 4, 6:14, 10:6-7; Keritot 1:6) ----
 ('Lev 12:2 — a male: impure seven', yoledet('impure_days', 'male'), 7),
 ('Lev 12:5 — a female: impure two weeks', yoledet('impure_days', 'female'), 14),
 ('Lev 12:4 — a male: thirty-three in the blood of purity', yoledet('purity_days', 'male'), 33),
 ('Lev 12:5 — a female: sixty-six', yoledet('purity_days', 'female'), 66),
 ('Niddah 6:14 — the fortieth day for the male (computed)', yoledet('total', 'male'), 40),
 ('Niddah 6:14 — the eightieth for the female (computed)', yoledet('total', 'female'), 80),
 ('Niddah 3:3-6 — "sits for a male and a female": the union of clocks', yoledet('union_of_clocks'), 'impure_14_pure_to_40_niddah_doubt_to_80'),
 ('Lev 12:4 — no holy thing, not to the sanctuary: barred, not impure', yoledet('holy_touch'), 'barred_from_holy_and_sanctuary'),
 ('Niddah 10:7 — she eats the tithe, not terumah', yoledet('tithe'), 'eats_tithe_not_terumah'),
 ('Niddah 1:7 — the one on pure blood needs no examination', yoledet('purity_blood_status'), 'pure_though_she_sees'),
 ('Niddah 10:6 — for holies: the houses\' grades', yoledet('purity_blood_holies'), 'Hillel_as_touching_corpse_impure_Shammai_as_corpse_impure'),
 ('Niddah 4:3 — the birther who did not immerse', yoledet('immersion_after_seven'), 'Hillel_defiles_wet_and_dry_until_immersed'),
 ('Niddah 2:5 — the chamber\'s blood: from the source', yoledet('source'), 'from_the_source'),
 ('Lev 12:6 — the lamb and the bird', yoledet('offering', means='reaches_lamb'), 'lamb_olah_and_bird_chatat'),
 ('Lev 12:8 — two birds if her hand finds not enough', yoledet('offering', means='reaches_birds'), 'two_birds_one_olah_one_chatat'),
 ('Sifra Chapter 3 1 — not inside the term', yoledet('offering_timing'), 'not_inside_the_term'),
 ('Keritot 2:4 / Sifra Chapter 3 6 — one offering per term', yoledet('per_child'), 'one_per_term_R._Yehuda_alternating'),
 ('Keritot 1:7 / Sifra Chapter 3 6 — five doubtful births: one offering and she eats', yoledet('five_doubtful'), 'one_offering_eats_no_debt'),
 ('Sifra Chapter 3 5 — the sin offering withholds', yoledet('withholder'), 'the_chatat_withholds'),
 ('Sifra Chapter 4 3 — the olah written first, the chatat offered first (CALLED)', yoledet('order'), 'olah_written_first_chatat_offered_first'),
 ('Kinnim 2:5 — no turtledoves against pigeons: the second follows the first', yoledet('kind_matching'), 'second_follows_first_kind_ben_Azzai_first_brought'),
 ('Kinnim 2:5 — she died: the heirs bring the olah, not the chatat (CALLED)', yoledet('heirs'), 'heirs_bring_olah_not_chatat'),
 ('Niddah 5:1 — the caesarean: not a birth; R. Shimon as born', yoledet('caesarean'), 'not_a_birth_R._Shimon_as_born'),
 ('Niddah 3:2 — the forms: human form decides', yoledet('forms'), 'human_form_decides'),
 ('Niddah 3:3 — a sac of water, blood, matter: no child', yoledet('sac_unformed'), 'no_child'),
 ('Niddah 3:7 — the fortieth day: no child (data)', yoledet('formation_threshold'), 40),
 ('Niddah 3:5 — born from most of the head', yoledet('birth_threshold'), 'most_of_the_head_or_most_of_the_body'),
 ('Niddah 3:5 — tumtum and androgynous: sits for both', yoledet('tumtum'), 'sits_for_both'),
 ('Sifra Section 1 9-11 — twins: count from the last', yoledet('twins'), 'count_from_the_last'),
 ('Niddah 4:4 — the woman in hard labor is a menstruant', yoledet('hard_labor_blood'), 'niddah_not_zivah'),
 ('Niddah 4:5 — how long is hard labor: three settings', yoledet('hard_labor_duration'), 'R._Meir_40_50_R._Yehuda_month_R._Yosei_R._Shimon_two_weeks'),
 ('Niddah 4:6 — hard labor in the eighty: pure until the child; R. Eliezer and dayo', yoledet('hard_labor_in_eighty'), 'bloods_pure_until_the_child_R._Eliezer_defiles_dayo'),
 ('Keritot 1:6 — the eve of eighty-one: Shammai exempt, Hillel liable', yoledet('eve_81'), 'Shammai_exempt_Hillel_liable'),
 ('Sifra Section 1 8 — she is impure, the child is not', yoledet('child_pure'), 'she_impure_child_not'),
 # ---- the zav (Lev 15:2-15; Zavim 1-2; Niddah 5:1-3, 7:1, 10:3-4) ----
 ('Zavim 1:1 — one sighting: as a seed-emitter (Hillel)', zav('tier', sightings=1), 'as_a_seed_emitter'),
 ('Zavim 1:1 / 1:5 — two: bed and seat, living water, no offering', zav('tier', sightings=2), 'bed_seat_living_water_no_offering'),
 ('Zavim 1:3 — three: a full zav with the offering', zav('tier', sightings=3), 'full_zav_with_offering'),
 ('Zavim 1:3 — sightings, not days', zav('sightings_not_days'), 'sightings'),
 ('Zavim 1:5 — one long as three: duration as count', zav('long_sighting'), 'duration_as_count'),
 ('Zavim 1:4 — the interval unit: an immersion and a drying', zav('interval_unit'), 'immersion_and_drying'),
 ('Zavim 1:6 — twilight: certain for impurity, doubtful for the offering', zav('twilight'), 'certain_impurity_doubtful_offering'),
 ('Lev 15:13 — the count begins when the flow stops', zav('count_start'), 'when_the_flow_stops'),
 ('Zavim 1:2 — a discharge even on the seventh voids all', zav('count_consecutive'), 'seven_consecutive_zov_voids_all'),
 ('Zavim 1:2 — semen in the count: Hillel its day, Shammai two', zav('semen_in_count'), 'Hillel_voids_its_day_Shammai_two'),
 ('Niddah 10:3 — examined day one and day seven: R. Eliezer presumes pure', zav('self_count'), 'for_himself_R._Eliezer_day1_and_day7_hold'),
 ('Lev 15:13 — living water for the zav alone', zav('water'), 'living_water'),
 ('Sifra Chapter 5 10 — his vessels in any water', zav('vessels_water'), 'any_water'),
 ('Sifra Chapter 5 7 — interposition-free', zav('interposition'), 'interposition_free_body_and_garments'),
 ('Lev 15:14-15 — the eighth day: two birds, one and one', zav('pair'), 'two_birds_one_chatat_one_olah_eighth_day'),
 ('Sifra Chapter 5 13 — birds of the first flow not for the second', zav('pair_binding'), 'first_flow_birds_not_for_second'),
 ('Sifra Chapter 5 14 — immersed the day before he comes', zav('immersed_before'), 'sunset_before_the_tent'),
 ('Zavim 2:2 — the seven ways of examination', zav('examination_ways'), 7),
 ('Zavim 2:2 — past the threshold: no examination', zav('after_threshold'), 'no_examination_coerced_doubtful_semen_impure'),
 ('Zavim 2:2 — the third sighting: not examined; R. Eliezer for the offering', zav('third_sighting_exam'), 'not_examined_R._Eliezer_examined_for_the_offering'),
 ('Zavim 2:1 — all are defiled by flux, minors included', zav('who'), 'all_including_minors_converts_slaves_eunuchs'),
 ('Zavim 2:1 — tumtum and androgynous: both stringencies', zav('tumtum'), 'stringencies_of_both_doubt'),
 ('Sifra Chapter 1 7-8 — white for the man, blood for the woman', zav('substance'), 'white_for_the_man_blood_for_the_woman'),
 ('Niddah 5:1 — the member only, outside only', zav('member_only'), 'the_member_outside_only'),
 ('Zavim 2:3 — semen then flux: twenty-four hours', zav('semen_then_flux'), 'twenty_four_hours_R._Yosei_its_day'),
 ('Sifra Section 1 13 — the nine liquids', zav('liquids'), 'sweat_excrement_pure_tear_wound_milk_liquid_grade_discharge_spittle_urine_severe'),
 ('Niddah 7:1 — the discharge wet only, menstrual blood wet and dry', zav('wet_dry'), 'discharge_wet_only_menstrual_blood_wet_and_dry'),
 ('Niddah 10:4 — the dead zav: no bed impurity; carries by the scribes', zav('dead_zav'), 'no_bed_impurity_carries_scribal'),
 ('Niddah 10:4 — the houses on dead women', zav('dead_women'), 'Shammai_all_die_niddot_Hillel_only_one_who_died_niddah'),
 # ---- the propagation lattice (Lev 15:4-12, 19-27; Zavim 2:4, 3-5) ----
 ('Lev 15:5 — touching his bed: washes, bathes, until evening', touch('zav', 'bed'), 'washes_garments_bathes_until_evening'),
 ('Lev 15:6 — sitting on his seat', touch('zav', 'seat', 'sit'), 'washes_garments_bathes_until_evening'),
 ('Lev 15:7 — touching his flesh', touch('zav', 'flesh'), 'washes_garments_bathes_until_evening'),
 ('Lev 15:8 — his spittle', touch('zav', 'spittle'), 'washes_garments_bathes_until_evening'),
 ('Zavim 5:10 — touching the saddle (under him): until evening, no washing', touch('zav', 'saddle', 'touch'), 'until_evening_no_garment_washing'),
 ('Zavim 5:8 — carrying the saddle: washes', touch('zav', 'saddle', 'carry'), 'washes_garments_bathes_until_evening'),
 ('Zavim 2:4 — carrying the bed: washes', touch('zav', 'bed', 'carry'), 'washes_garments_bathes_until_evening'),
 ('Lev 15:11 — his unrinsed hands', touch('zav', 'unwashed_hands'), 'washes_garments_bathes_until_evening'),
 ('Lev 15:12 — the earthen vessel broken', touch('zav', 'earthenware'), 'broken'),
 ('Lev 15:12 — the wooden vessel rinsed', touch('zav', 'wood'), 'rinsed_in_water'),
 ('Zavim 5:7 — his discharge, spittle, urine: two and one', touch('zav', 'discharge'), 'two_and_one_toucher_and_mover_R._Eliezer_carrier'),
 ('Lev 15:19 — touching the menstruant: until evening', touch('niddah', 'flesh'), 'until_evening'),
 ('Lev 15:21 — her bed: washes', touch('niddah', 'bed'), 'washes_garments_bathes_until_evening'),
 ('Lev 15:23 — on the bed when he touches it: until evening', touch('niddah', 'on_the_bed'), 'until_evening'),
 ('Lev 15:26 — the zavah\'s bed as her separation\'s bed', touch('zavah', 'bed'), 'as_her_niddah_bed'),
 ('Zavim 5:11 — the partner\'s bed: light, foods and liquids only', touch('partner', 'bed'), 'light_foods_and_liquids_only'),
 ('Lev 15:16 — the seed-emitter bathes all his flesh', touch('seed_emitter', 'flesh'), 'bathes_all_his_flesh_until_evening'),
 ('Lev 15:17 — the garment with seed washed', touch('seed_emitter', 'garment'), 'washed_until_evening'),
 ('Lev 15:18 — the woman: both bathe', touch('seed_emitter', 'woman'), 'both_bathe_until_evening'),
 ('Zavim 5:1 — during contact: garments, foods first, hands second', degrees('during_contact'), 'garments_defiled_foods_liquids_first_hands_second_not_persons_not_earthenware'),
 ('Zavim 5:1 — after separation: liquids first, foods and hands second, no garments', degrees('after_separation'), 'liquids_first_foods_and_hands_second_no_garments'),
 ('Zavim 5:6 — a father of impurity: two and one; separated one and one', degrees('father_of_impurity'), 'defiles_two_disqualifies_one_separated_one_and_one'),
 ('Zavim 5:10 — the general rule: one and one except a person', degrees('general'), 'one_and_one_except_a_person'),
 ('Zavim 4:6 / 5:2 — the madaf above, the bed below', degrees('madaf_above'), 'foods_liquids_vessels_above_light_bed_below_severe'),
 ('Zavim 4:6 — the zav against the corpse', degrees('zav_vs_corpse'), 'zav_bed_seat_below_madaf_above_corpse_tent_and_seven'),
 ('Zavim 5:2 — carried on the zav: impure', degrees('carried_on_zav'), 'impure'),
 ('Zavim 5:2 — the zav carried on: pure except bed, seat, person', degrees('zav_carried_on'), 'pure_except_bed_seat_person'),
 ('Zavim 5:4-5 — the majority grid', degrees('majority_grid'), 'by_the_zav_impure_by_the_bed_part_cases_pure'),
 ('Zavim 4:4 — six chairs: only the one under the body', degrees('carried_majority'), 'only_the_seat_under_the_body'),
 ('Zavim 4:5 — ten cloaks: all impure', degrees('pressure_column'), 'all_ten_impure'),
 ('Zavim 4:5 — the scale-pan: they sink, impure', degrees('scale_pan'), 'zav_sinks_pure_they_sink_impure'),
 ('Zavim 3:1 / 3:3 — the boat and the shaky plank: moved as touched', degrees('shaking'), 'moved_as_touched'),
 ('Zavim 4:1 — knocked on the balcony, the loaf fell: pure', degrees('knock_loaf'), 'pure'),
 ('Zavim 4:2 — the firm supports: pure', degrees('firm_supports'), 'pure'),
 ('Zavim 4:7 — four cloaks under the bed\'s legs impure, the beast\'s pure', degrees('support_majority'), 'bed_four_legs_impure_beast_four_legs_pure'),
 ('Zavim 2:4 — the zav defiles the bed in five ways', degrees('five_ways'), 5),
 ('Zavim 2:4 — the bed defiles a person in seven', degrees('seven_ways'), 7),
 ('Sifra Chapter 2 1-4 — the designated bed: the stand-up test', degrees('designated_bed'), 'serves_lying_with_its_work_stand_up_test'),
 ('Niddah 6:3 — the midras class within the corpse-susceptible', degrees('midras_subset'), 'midras_class_within_corpse_susceptible'),
 ('Sifra Section 2 3 — a broken bed is pure', degrees('broken_bed'), 'pure'),
 ('Zavim 3:2 — pure for the synagogue, impure for terumah', degrees('terumah_fence'), 'pure_for_synagogue_members_impure_for_terumah'),
 # ---- the menstruant and her partner (Lev 15:19-24; Niddah 1:2, 2:2, 2:5, 4:1, 5:3, 5:5, 8:3) ----
 ('Lev 15:19 — seven days', niddah('days'), 7),
 ('Niddah 1:2 — she counts from the hour she saw', niddah('count_anchor'), 'from_the_sighting'),
 ('Niddah 10:2 — no early immersion; the seventh ends at sunset', niddah('no_early_immersion'), 'all_seven'),
 ('Niddah 8:3 — blood, not a stain', niddah('blood_not_stain'), 'blood_not_a_stain'),
 ('Niddah 5:1 — she inside as outside, he outside only', niddah('inside_as_outside'), 'she_inside_he_outside'),
 ('Niddah 5:3 — a day-old girl susceptible', niddah('day_old_girl'), 'susceptible'),
 ('Niddah 5:3 — a ten-day-old by flux: seven plus three (computed)', niddah('ten_day_girl'), 10),
 ('Niddah 2:6 — the five bloods (data)', niddah('five_bloods'), 'red_black_saffron_earth_water_diluted_Shammai_add_two_Hillel_purify'),
 ('Lev 15:24 — her partner: seven days', niddah('partner_days'), 7),
 ('Niddah 4:1 — the partner\'s bed: the lower as the upper, light', niddah('partner_bed'), 'light_foods_and_liquids_only'),
 ('Niddah 2:2 — found on his cloth: liable to an offering (CALLED)', niddah('partner_offering'), 'sin_offering'),
 ('Niddah 2:2 — found after a time: doubt, exempt (CALLED)', niddah('partner_after_time'), 'impure_in_doubt_exempt_from_offering'),
 ('Niddah 5:5 — the partner nine years and a day', niddah('partner_age'), 'nine_years_and_a_day'),
 ('Sifra Chapter 7 6-9 — the partner counts from the last lying', niddah('partner_count'), 'from_the_last_lying'),
 ('Sifra Chapter 7 2 — not the leprous woman\'s partner', niddah('partner_leper'), 'not_the_leper_womans_partner'),
 ('Sifra Chapter 8 8 — she defiles her partner, the zav not his', niddah('she_defiles_him_not_reverse'), 'she_defiles_partner_zav_not_his'),
 # ---- the zavah's window (Lev 15:25-33; Niddah 4:7, 10:8; Zavim 1:1) ----
 ('Sifra Section 5 5-9 — "days" two, "many" three', zavah('days_many'), (2, 3)),
 ('Niddah 4:7 — the eleven days', zavah('window'), 11),
 ('Sifra Chapter 8 4-7 — the zavah\'s tiers', zavah('tiers'), 'one_watches_a_day_two_bed_and_seat_three_full'),
 ('Niddah 4:7 — the day-watcher: one against one', zavah('watcher'), 'one_day_against_one_day'),
 ('Lev 15:28 — she counts seven after the flow stops', zavah('count'), 'seven_after_the_flow_stops'),
 ('Sifra Chapter 5 8-9 — no living water written for her', zavah('water'), 'no_living_water_written'),
 ('Lev 15:29-30 — her eighth-day pair', zavah('pair'), 'two_birds_one_chatat_one_olah_eighth_day'),
 ('Niddah 10:8 — the eleventh day: Shammai offering, Hillel exempt', zavah('day_eleven'), 'Shammai_bed_seat_and_offering_Hillel_exempt'),
 ('Sifra Chapter 9 2 — immersed after the act: R. Shimon pure, the sages said do not', zavah('immersed_after_act'), 'R._Shimon_pure_but_the_sages_said_do_not'),
 ('Sifra Chapter 9 3 — her instance-binding', zavah('her_pair_binding'), 'first_flow_birds_not_for_second'),
 ('Sifra Section 5 3 — twenty-five days of hard labor without flux (computed)', zavah('twenty_five'), 25),
 ('Sifra Section 5 4 — a hundred days without flux status (computed)', zavah('hundred'), 100),
 ('Sifra Chapter 9 12 — R. Akiva: she may adorn', zavah('adornment'), 'R._Akiva_she_may_adorn'),
 ('Lev 15:31 — the separation clause and the Presence', zavah('presence'), 'separation_warning_punishment_presence_among_them'),
 ('Lev 15:32-33 — the closing torah\'s five persons', zavah('five_persons'), 5),
 # ---- the pairs engine (Kinnim) ----
 ('Kinnim 1:1 — the bird sin offering below, the burnt offering above (CALLED)', pairs('places'), 'bird_chatat_below_bird_olah_above'),
 ('Kinnim 1:1 — the obligation: one and one', pairs('obligation'), 'one_chatat_one_olah'),
 ('Kinnim 1:1 — vow vs free-will: responsibility', pairs('vow_vs_freewill'), 'vow_responsible_freewill_not'),
 ('Kinnim 1:2 — a sin offering in burnt offerings: all die', pairs('spec_chatat_in_spec_olah'), 'all_die'),
 ('Kinnim 1:2 — a sin offering in one obligation pair: one valid', pairs('spec_in_chovah', chovah_pairs=1), 1),
 ('Kinnim 3:5 — a sin offering in two obligation pairs: two valid', pairs('spec_in_chovah', chovah_pairs=2), 2),
 ('Kinnim 1:3 — two and two: half valid', pairs('chovah_in_chovah', a=2, b=2), 'half_valid_half_invalid'),
 ('Kinnim 1:3 — one and three: the smaller valid', pairs('chovah_in_chovah', a=1, b=3), 1),
 ('Kinnim 1:3 — ten and a hundred: ten', pairs('chovah_in_chovah', a=10, b=100), 10),
 ('Kinnim 1:4 — one name, two names', pairs('one_name_two_names'), 'birth_and_birth_one_name_birth_and_flux_two'),
 ('Kinnim 1:4 — R. Yosei: the joint purchase', pairs('joint_purchase'), 'priest_offers_whichever'),
 ('Kinnim 2:1 — flew to the air or died: a mate for the second', pairs('flew_to_air'), 'take_a_mate_for_the_second'),
 ('Kinnim 2:1 — flew among the offered: invalid and disqualifies one', pairs('flew_among_offered'), 'invalid_and_disqualifies_one_opposite'),
 ('Kinnim 2:2 — two women, two pairs: repeated flights lose nothing', pairs('two_women_two_pairs'), 'one_going_one_returning_repeated_nothing_lost'),
 ('Kinnim 2:3 — the chain of seven after one trip (computed)', pairs('chain', trips=1), [0, 0, 1, 2, 3, 4, 6]),
 ('Kinnim 2:3 — after two trips', pairs('chain', trips=2), [0, 0, 0, 0, 1, 2, 5]),
 ('Kinnim 2:3 — after three trips', pairs('chain', trips=3), [0, 0, 0, 0, 0, 0, 4]),
 ('Kinnim 2:3 — flew from the dead to all: all die', pairs('chain_from_dead'), 'all_die'),
 ('Kinnim 2:4 — unspecified to specified: a mate; returned, all die', pairs('stumah_meforeshet'), 'take_a_mate_returned_all_die'),
 ('Kinnim 2:5 — the middle to the sides', pairs('middle_to_sides'), 'nothing_lost_returned_middle_die'),
 ('Kinnim 3:1 — unconsulted, equal counts: half', pairs('unconsulted_equal'), 'half_valid_half_invalid'),
 ('Kinnim 3:2 — unconsulted, unequal: the greater', pairs('unconsulted_unequal'), 'all_above_half_all_below_half_half_and_half_the_greater'),
 ('Kinnim 3:3 — specified pair, half and half: both invalid', pairs('unconsulted_specified'), 'half_and_half_or_both_invalid'),
 ('Kinnim 3:4 — four kinds: only the unspecified valid', pairs('unconsulted_mixed_four'), 'only_the_unspecified_valid_divided'),
 ('Kinnim 3:6 — the vowed pair: three above, one below (computed)', pairs('vowed_pair'), (3, 1)),
 ('Kinnim 3:6 — did two and two: one more above', pairs('vowed_pair_two_two'), 'one_more_above_one_kind_two_of_two_kinds'),
]

# ---- (3)+(5) run, grade, effects ------------------------------------
n = len(TESTS)
assert n == GUARDED, (n, GUARDED)
print('guard: %d test rows, every expected value a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
print()
ok = 0
frac = {I: 0, M: 0, A: 0, D: 0, P: 0}
used = []
misses = []
for name, c, want in TESTS:
    hit = c['v'] == want
    ok += hit
    frac[c['p']] += 1
    used += [e for e in c['fx'] if e != FX.NONE]
    if not hit: misses.append((name, c['v']))
    print('%s %-96s [%s] %s' % ('OK ' if hit else 'MISS', name[:96], c['p'], '' if hit else 'got=%r' % (c['v'],)))
    print('     effects: %s' % ', '.join(c['fx']))
print()
print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d'
      % (frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n))
ops = FX.summarize(used)
print('LEDGER OPS this span writes: %s' % ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
print('effects: every cell carries REGISTERED effects — NINE discovered in these spans\' own verbs: niddah_seven, '
      'blood_of_purity, counts_seven_clean (TIMERS), bed_and_seat_defile, washes_and_bathes, immersed (STATUS), '
      'pair_owed (DEBIT), barred_from_holies (BLOCK), birds_die (DESTROY) [effects law satisfied]')
if ok == n:
    print('THE IMPURITY CLOCKS AND THE PAIRS ENGINE COMPILE — the written numbers summed to forty and eighty, the '
          'two gates of 12:4, the source of her blood, the pair formula at three seats, seven days at five clocks, '
          'living water at the zav alone, the propagation formula censused with the saddle\'s split clause, the '
          'zavah\'s window and her hundred days computed, the chain of seven computed; the Lev 4, Lev 5, and '
          'meal-offering engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')
