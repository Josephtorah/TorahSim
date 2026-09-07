#!/usr/bin/env python3
"""cold_run_chatat.py — THE SIN OFFERING RANK TREE AND THE PRIEST'S TABLE
(2026-09-05, sitting L1 of THE COMPILE DEBT — World/step9/COMPILE_DEBT.md).

Spans: Lev 4:1-35 (the sin offering by rank — the anointed priest, the
congregation, the leader, the one soul of the people of the land; the
inner and the outer blood routes; the carcass outside the camp) and
Lev 10:8-20 (the wine ban with its two jobs — to distinguish and to
teach; the day's portions — the meal offering beside the altar, the
breast and thigh in a pure place; the sin-offering inquiry — the goat
burned, the goat eaten, the acute mourner's day).

Answer sheet ROUTED BY TOPIC under the union rule (THE_STEPS Step 2):
Mishnah Horayot whole, Mishnah Keritot whole, Mishnah Zevachim 10-12 —
85 rows read whole, the ledger logic/oral_triage/chatat_topic_docket_
2026-09-05.md with its coverage computed; the 23 link-driven rows all
credits; 340 Talmud segments the motion-4 address index, opened per
gap and named on the cells they fill.

The five motions, in order:
 (1) code from the BARE INK — the four tiers by their own tokens, the
     one tier that carries 'his God', the two inner routes counted by
     'seven times' and 'to the tent of meeting', the five horns and
     five bases, the four atone-and-forgiven closes, the domain phrase
     counted across two chapters, 'female' twice and 'male' once, the
     two 'and if' branch heads of the commoner, 'the FIRST bull', the
     three 'outside the camp' verses; Lev 10's 'wine and strong
     drink... and you shall not die', the two 'to distinguish' pairs,
     'to teach', the HOLY place against the PURE place, 'your
     daughters', the doubled 'inquired', 'not brought inside', 'to
     bear the iniquity'; every quantity a PARAMETER (the quarter-log,
     the olive, the half-loaf, the thirty-six are the data channel);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal
     typed from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Sifra's rows (this
     chapter's spine, verdicted 2026-09-03 and 2026-09-05) and the
     Talmud where opened, each labeled [MOVE];
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS
     on every verdict (six discovered in these spans' own verbs).

Cross-span receipts, labeled [IMPORT] and, where a compiled callee
exists, CALLED: the Lev 5 engine (cold_run_vayikra5 — the sliding
scale's three triggers, the suspended ram, sacrilege, the means ladder);
the offering engine (cold_run_offerings — the outer sin offering's
eater, place and window; the peace offering's window); the meal-
offering engine (cold_run_minchah — the remainder to Aaron and his
sons); Num 15:24-31 (the idolatry column; 'one law for the one who
DOES'; the high hand); Lev 6:18-23 (the sin offering's torah — most
holy, the inner one burned); Lev 16:28-30 (the burner's laundering;
the Day atones); Lev 21:21-22 (the blemished priest eats); Lev 7:2, 7:33
(the guilt offering's 'around'; 'he who offers the blood'); Exod 21:28
(the stoned ox's flesh); Lev 27:11 (the bird has no redemption).
"""
import sqlite3, sys, os, json, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 195, ('the guard counted %d expectations, the tripwire holds 195' % GUARDED)

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
    # the domain (4:2)
    ('a SOUL when it sins',                        'Lev', 4, 2, 'נפש'),
    ('UNWITTINGLY',                                'Lev', 4, 2, 'בשגגה'),
    ('which shall NOT BE DONE (negatives)',        'Lev', 4, 2, 'תעשינה'),
    ('and DOES (the act)',                         'Lev', 4, 2, 'ועשה'),
    ('OF ONE of them (partial acts)',              'Lev', 4, 2, 'מאחת'),
    # the four tiers
    ('the ANOINTED priest',                        'Lev', 4, 3, 'המשיח'),
    ('to the GUILT of the people',                 'Lev', 4, 3, 'לאשמת'),
    ('a bull, son of the herd',                    'Lev', 4, 3, 'פר'),
    ('all the CONGREGATION of Israel',             'Lev', 4, 13, 'עדת'),
    ('a THING hidden',                             'Lev', 4, 13, 'דבר'),
    ('from the eyes of the ASSEMBLY',              'Lev', 4, 13, 'הקהל'),
    ('the ELDERS of the congregation lay hands',   'Lev', 4, 15, 'זקני'),
    ('WHEN a LEADER sins',                         'Lev', 4, 22, 'נשיא'),
    ('the LORD HIS GOD (the leader alone)',        'Lev', 4, 22, 'אלהיו'),
    ('a he-goat, MALE',                            'Lev', 4, 23, 'זכר'),
    ('ONE soul of the people of the land',         'Lev', 4, 27, 'אחת'),
    ('the people of the LAND',                     'Lev', 4, 27, 'הארץ'),
    ('a she-goat, FEMALE',                         'Lev', 4, 28, 'נקבה'),
    ('and if a LAMB',                              'Lev', 4, 32, 'כבש'),
    # knowledge
    ('and the sin be KNOWN (the congregation)',    'Lev', 4, 14, 'ונודעה'),
    ('or his sin be made KNOWN to him',            'Lev', 4, 23, 'הודע'),
    ('wherein he sinned IN IT',                    'Lev', 4, 23, 'בה'),
    ('HIS offering on HIS sin',                    'Lev', 4, 28, 'קרבנו'),
    # the inner route
    ('brought INTO the tent of meeting',           'Lev', 4, 5, 'והביא'),
    ('SEVEN times before the veil',                'Lev', 4, 6, 'שבע'),
    ('the horns of the INCENSE altar',             'Lev', 4, 7, 'קטרת'),
    ('poured at the BASE of the burnt-offering altar', 'Lev', 4, 7, 'יסוד'),
    ('OUTSIDE the camp',                           'Lev', 4, 12, 'מחוץ'),
    ('a PURE place',                               'Lev', 4, 12, 'טהור'),
    ('the ash-pour',                               'Lev', 4, 12, 'הדשן'),
    ('as he burned the FIRST bull',                'Lev', 4, 21, 'הראשון'),
    # the outer route and the close
    ('in the place of the BURNT OFFERING',         'Lev', 4, 24, 'העלה'),
    ('with his FINGER on the horns',               'Lev', 4, 25, 'באצבעו'),
    ('and the priest shall ATONE',                 'Lev', 4, 26, 'וכפר'),
    ('and he shall be FORGIVEN',                   'Lev', 4, 26, 'ונסלח'),
    ('as the fat of the PEACE offering',           'Lev', 4, 26, 'השלמים'),
    # Lev 10
    ('WINE and strong drink',                      'Lev', 10, 9, 'יין'),
    ('STRONG DRINK (that which intoxicates)',      'Lev', 10, 9, 'ושכר'),
    ('when you COME INTO the tent',                'Lev', 10, 9, 'בבאכם'),
    ('and you shall NOT DIE',                      'Lev', 10, 9, 'תמתו'),
    ('an everlasting statute',                     'Lev', 10, 9, 'חקת'),
    ('to DISTINGUISH',                             'Lev', 10, 10, 'ולהבדיל'),
    ('to TEACH',                                   'Lev', 10, 11, 'ולהורת'),
    ('eat it UNLEAVENED beside the altar',         'Lev', 10, 12, 'מצות'),
    ('most holy',                                  'Lev', 10, 12, 'קדשים'),
    ('in a HOLY place (the meal offering)',        'Lev', 10, 13, 'קדש'),
    ('in a PURE place (breast and thigh)',         'Lev', 10, 14, 'טהור'),
    ('and your DAUGHTERS',                         'Lev', 10, 14, 'ובנתיך'),
    ('the breast of the WAVING',                   'Lev', 10, 14, 'התנופה'),
    ('on the fire-portions of the FATS',           'Lev', 10, 15, 'החלבים'),
    ('INQUIRED (doubled)',                         'Lev', 10, 16, 'דרש'),
    ('and behold it was BURNED',                   'Lev', 10, 16, 'שרף'),
    ('to BEAR the iniquity of the congregation',   'Lev', 10, 17, 'לשאת'),
    ('NOT brought inside',                         'Lev', 10, 18, 'הובא'),
    ('inside (the sanctuary)',                     'Lev', 10, 18, 'פנימה'),
    ('had I eaten the sin offering TODAY',         'Lev', 10, 19, 'ואכלתי'),
    ('and it was GOOD in his eyes',                'Lev', 10, 20, 'וייטב'),
]
fired = 0
for name, b, ch, vs, tok in PROBES:
    if count(b, ch, vs, tok) == 0:
        sys.exit('PROBE FAILED: %s — %r not in %s %d:%d' % (name, tok, b, ch, vs))
    fired += 1
print('probes: all %d ink-token probes fired [zero-report law satisfied]' % fired)

# ---- the censuses (asserted: a tripwire, not a recital) -------------
LEV4 = list(range(2, 36))
c_anointed = sum(count('Lev', 4, v, 'המשיח') for v in LEV4)
c_elohav = [v for v in LEV4 if count('Lev', 4, v, 'אלהיו')]
c_seven = [v for v in LEV4 if phrase('Lev', 4, v, ['שבע', 'פעמים'])]
c_into_tent = [v for v in LEV4 if phrase('Lev', 4, v, ['אל', 'אהל', 'מועד']) and count('Lev', 4, v, 'מדם')]
c_horns = [v for v in LEV4 if count('Lev', 4, v, 'קרנ')]
c_base = [v for v in LEV4 if count('Lev', 4, v, 'יסוד')]
c_atone = [v for v in LEV4 if count('Lev', 4, v, 'וכפר')]
c_forgiven = [v for v in LEV4 if count('Lev', 4, v, 'ונסלח')]
c_female = [v for v in LEV4 if count('Lev', 4, v, 'נקבה')]
c_male = [v for v in LEV4 if count('Lev', 4, v, 'זכר')]
c_tamim = [v for v in LEV4 if count('Lev', 4, v, 'תמימ') or count('Lev', 4, v, 'תמים')]
c_outside = [(4, v) for v in LEV4 if phrase('Lev', 4, v, ['מחוץ', 'למחנה'])] + \
            [(6, v) for v in range(1, 24) if phrase('Lev', 6, v, ['מחוץ', 'למחנה'])]
# the domain phrase: a token carrying 'commandments' + the tail 'which shall not be done' — the exact
# five-token string varies its head (4:22 inserts 'his God'; 4:27 says 'of the commandments' without
# 'all'), a first-draft exact match held at three seats only: the census caught it
def has_domain(book, ch, v):
    return phrase(book, ch, v, ['אשר', 'לא', 'תעשינה']) and count(book, ch, v, 'מצות')
c_domain = [(4, v) for v in LEV4 if has_domain('Lev', 4, v)] + \
           [(5, v) for v in range(1, 27) if has_domain('Lev', 5, v)]
c_shegagah = [v for v in LEV4 if count('Lev', 4, v, 'שגג') or count('Lev', 4, v, 'ישגו')]
c_hoda = [v for v in LEV4 if count('Lev', 4, v, 'הודע') or count('Lev', 4, v, 'ונודעה')]
c_veim = [v for v in LEV4 if toks('Lev', 4, v)[0] in ('אם', 'ואם')]   # 4:3 opens bare 'if', the rest 'and if'
c_place_words = (count('Lev', 10, 13, 'קדש'), count('Lev', 10, 14, 'טהור'))
c_darash = count('Lev', 10, 16, 'דרש')
c_havdil_pairs = count('Lev', 10, 10, 'ובין')
assert c_anointed == 3 and c_elohav == [22], (c_anointed, c_elohav)
assert c_seven == [6, 17] and c_into_tent == [5, 16], (c_seven, c_into_tent)
assert c_horns == [7, 18, 25, 30, 34] and c_base == [7, 18, 25, 30, 34], (c_horns, c_base)
assert c_atone == [20, 26, 31, 35] and c_forgiven == [20, 26, 31, 35], (c_atone, c_forgiven)
assert c_female == [28, 32] and c_male == [23], (c_female, c_male)
assert c_tamim == [3, 23, 28, 32], c_tamim
assert c_outside == [(4, 12), (4, 21), (6, 4)], c_outside
assert c_domain == [(4, 2), (4, 13), (4, 22), (4, 27), (5, 17)], c_domain
assert c_shegagah == [2, 13, 22, 27] and c_hoda == [14, 23, 28], (c_shegagah, c_hoda)
assert c_veim == [3, 13, 27, 32], c_veim
assert c_place_words == (1, 1) and c_darash == 2 and c_havdil_pairs == 3, (c_place_words, c_darash, c_havdil_pairs)
print('censuses: the ANOINTED x%d · "his God" at 4:%s alone · seven-times at 4:%s · blood into the tent at 4:%s · '
      'horns at 4:%s · bases at 4:%s · atone/forgiven at 4:%s · FEMALE at 4:%s, MALE at 4:%s · unblemished at 4:%s · '
      'outside-the-camp at %s · THE DOMAIN PHRASE at %s (five seats, two chapters) · unwitting at 4:%s · known at 4:%s · '
      'branch heads "and if" at 4:%s · Lev 10: holy-place/pure-place %s · inquired x%d · distinguish-pairs %d'
      % (c_anointed, c_elohav, c_seven, c_into_tent, c_horns, c_base, c_atone, c_female, c_male, c_tamim,
         c_outside, c_domain, c_shegagah, c_hoda, c_veim, c_place_words, c_darash, c_havdil_pairs))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_vayikra5 as V5
    import cold_run_offerings as OFF
    import cold_run_minchah as MIN
    import cold_run_tzav as TZ
def v5(person):
    r = V5.graded_offering(person, V5.DATA); return r[0] if isinstance(r, tuple) else r
def v5s(case):
    r = V5.sacrilege(case, V5.DATA); return r[0] if isinstance(r, tuple) else r
TALUI = v5s({'kind': 'doubt'})
MEILAH_DOUBT = v5s({'kind': 'doubt', 'doubt_object': 'meilah'})
MEILAH = v5s({'kind': 'meilah', 'unwitting': True, 'benefit': True, 'damage': True, 'value': 4.0})
TUMAH = v5({'trigger': 'tumah', 'aware_at_start': True, 'hidden_in_middle': True, 'aware_at_end': True,
            'touched_sanctum': True, 'means': 'reaches_lamb'})
BIRDS = v5({'trigger': 'utterance_oath', 'act_is_his_option': True, 'oath_forgotten': True, 'means': 'reaches_birds'})
LADDER = {m: v5({'trigger': 'utterance_oath', 'act_is_his_option': True, 'oath_forgotten': True, 'means': m})
          for m in ('reaches_lamb', 'reaches_birds', 'reaches_flour')}
OUTER = OFF.dispatch('outer_chatat'); INNER = OFF.dispatch('inner_chatat_burned'); SHEL = OFF.dispatch('shelamim')
MIN_REM = MIN.remainder('griddle')['v']
# the dependency-debt sitting (2026-09-06): the four "as the fat of the peace
# offering" pointers (4:10, 4:26, 4:31, 4:35) and 10:15's "as the LORD
# commanded" resolve by LIVE CALL — the fat inventory in the offerings
# dispatcher, the breast and thigh in the Tzav engine's dues machine.
FAT = {s: OFF.dispatch('fat:' + s) for s in ('ox', 'lamb', 'goat')}
BREAST_THIGH = TZ.dues_machine({'ask': 'breast_thigh'}, TZ.PARAMS)[0]
print('routing receipts (pointers): cold_run_offerings CALLED — fat:ox tail %r, fat:lamb tail %r, fat:goat tail %r; '
      'cold_run_tzav CALLED — dues_machine(breast_thigh) -> %r [IMPORT, live calls]'
      % (FAT['ox']['tail']['v'], FAT['lamb']['tail']['v'], FAT['goat']['tail']['v'], BREAST_THIGH))
print('routing receipts: cold_run_vayikra5 CALLED — doubt -> %r; sacrilege doubt -> %r; sacrilege -> %r; '
      'tumah trigger -> %r; birds tier -> %r; cold_run_offerings CALLED — outer_chatat eater %r window %r, '
      'shelamim window %r; cold_run_minchah CALLED — remainder -> %r [IMPORT, live calls]'
      % (TALUI, MEILAH_DOUBT, MEILAH[:40], TUMAH[:60], BIRDS, OUTER['eater']['v'], OUTER['window']['v'],
         SHEL['window']['v'], MIN_REM))

I, M, A, D, P = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT'
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
SC = 'Sifra, Vayikra Dibbura DeChovah, '
SS = 'Sifra, Shemini, '
OPEN = 'OPEN (we have not heard)'

# =====================================================================
# THE CODE — from the ink of Leviticus 4 and 10 alone. Mishnah/Talmud
# appear ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE DOMAIN (4:2) -------------------------------------------
def domain(c):
    """Who is inside the fixed sin offering at all."""
    if c.get('person') == 'gentile':
        return cell('gentile_outside', M, SC + 'Section 1 1 — Israel brings the sin offering, gentiles do not, '
                    'even for the Noahide commandments', ['exempt'])
    if c.get('law_source') in ('court', 'king'):
        return cell('not_torah_law_outside', M, SC + 'Section 1 5 — "the commandments of the LORD": not the '
                    'king\'s, not the court\'s', ['exempt'])
    if c.get('age') == 'minor' or c.get('state') == 'asleep':
        return cell('exempt', A, 'Mishnah Keritot 2:6 — the minor and the sleeper exempt (no source opened '
                    'beyond the row)', ['exempt'])
    if c.get('commandment_kind') == 'positive':
        return cell('positive_outside', I, '4:2 "which shall NOT be done" — negatives only; the domain phrase '
                    'counted at %s' % c_domain, ['exempt'])
    if not c.get('act', True):
        return cell('no_act_excluded', I, '4:2 "and DOES" (ועשה) — an act is required; Num 15:29 "for the one '
                    'who DOES unwittingly" [IMPORT] — the sages exclude the blasphemer', ['exempt'])
    if c.get('own_offering') == 'sliding_scale':
        return cell('sliding_scale', P, 'Lev 5:2-3 — the sanctuary-impurity class carries its OWN offering: '
                    'CALLED cold_run_vayikra5.graded_offering -> %r' % TUMAH[:50], [FX.NONE])
    if not c.get('karet_when_intentional', True):
        return cell('not_karet_class_outside', P, 'Num 15:29-31 [IMPORT] — "one law for the one who does '
                    'unwittingly... the soul with a high hand shall be CUT OFF": the sin offering\'s unwitting '
                    'is the karet\'s intentional (' + SC + 'Chapter 1 1, the idolatry template)', ['exempt'])
    intent = c.get('intent')
    if intent == 'intentional':
        return cell('karet_no_offering', P, 'Num 15:30 "with a high hand... cut off" [IMPORT]; 4:2 '
                    '"unwittingly" excludes him (' + SC + 'Section 1 2)', ['karet_cut_off'])
    if intent == 'unknown':
        return cell('suspended_ram', P, 'Lev 5:17 — the same domain phrase, "and he knew not": CALLED '
                    'cold_run_vayikra5.sacrilege(doubt) -> %r' % TALUI, ['suspends'])
    return cell('sin_offering', I, '4:2 "a soul when it sins UNWITTINGLY... and does of one of them" — '
                'unwitting at 4:%s' % c_shegagah, ['atoned_forgiven'])

def criterion():
    return cell('karet_intentional_chatat_unwitting', P, 'Num 15:29-31 [IMPORT] read onto 4:2 — the domain '
                'predicate; the tradition\'s census of its members is thirty-six (Mishnah Keritot 1:1)', [FX.NONE])
def karet_census():
    return cell(36, A, 'Mishnah Keritot 1:1 — thirty-six karet cases: the tradition\'s own census across the '
                'books (DATA/ANSWER-SHEET; not recomputed here)', [FX.NONE])
def talui_scope(arm):
    if arm == 'sages':
        return cell('karet_class_only', I, 'Lev 5:17 carries 4:2\'s OWN domain phrase — "of all the commandments '
                    'of the LORD which shall not be done" — counted at %s: the suspended ram runs on the sin '
                    'offering\'s domain; Keritot 25b:4 — Rava: the sages learn "commandments"-"commandments" from '
                    'the fat sin offering, the verbal analogy on this very phrase' % c_domain, [FX.NONE])
    return cell('R._Eliezer_any_day', A, 'Mishnah Keritot 6:3 — the ram of the pious (Bava b. Buta); the '
                'dissent carried', [FX.NONE])

# ---- F2: THE RANK TREE (4:3-35) --------------------------------------
TIER_INK = {
    'anointed':     ('bull', 'male', 3, '4:3 "if the ANOINTED priest sins... a bull, son of the herd, unblemished"'),
    'congregation': ('bull', 'male', 14, '4:14 "the assembly shall offer a bull, son of the herd, for a sin offering"'),
    'leader':       ('he_goat', 'male', 23, '4:23 "his offering: a he-goat, MALE, unblemished"'),
    'commoner':     ('she_goat_or_ewe_lamb', 'female', 28, '4:28 "a she-goat, unblemished, FEMALE"; 4:32 "and if a '
                                                           'LAMB... a female, unblemished"'),
}
def rank(tier, sin='general', species=None):
    if sin == 'idolatry':
        if tier == 'congregation':
            return cell('bull_olah_and_goat_chatat', P, 'Num 15:24 [IMPORT] — "one bull, son of the herd, for a '
                        'BURNT offering... and one he-goat for a SIN offering"', ['accepted'])
        return cell('she_goat', P, 'Num 15:27 [IMPORT] — "one soul... a she-goat of its first year for a sin '
                    'offering"; the leader and the anointed fall to the individual\'s column (Mishnah Horayot '
                    '2:6 — the answer sheet\'s own collapse)', ['accepted'])
    off, sex, vs, why = TIER_INK[tier]
    if tier == 'commoner' and species:
        off = {'goat': 'she_goat', 'lamb': 'ewe_lamb'}[species]
    return cell(off, I, (why + ' — unblemished at 4:%s') % c_tamim, ['accepted'])
def sex(tier):
    return cell(TIER_INK[tier][1], I, 'FEMALE at 4:%s (the commoner\'s two kinds), MALE at 4:%s (the leader\'s '
                'goat); the bulls masculine' % (c_female, c_male), [FX.NONE])
def lamb_goat():
    return cell('equal_branches', I, '4:27 and 4:32 both open with "and if" — parallel branch heads at one '
                'level (branch heads at 4:%s); neither is the fallback of the other' % c_veim, [FX.NONE])
def precedence_bulls():
    return cell('anointed_first', I, '4:21 "as he burned the FIRST bull" — the anointed\'s bull is named first; '
                '4:13\'s "and if" subordinates the section (' + SC + 'Section 4 1)', [FX.NONE])
def identity(who):
    if who == 'leader':
        return cell('the_king', I, '4:22 "the commandments of the LORD HIS GOD" — אלהיו ("his God") stands at '
                    '4:%s alone among the four tiers: the one with none above him but his God' % c_elohav, [FX.NONE])
    if who == 'anointed':
        return cell('anointed_with_oil', M, SC + 'Section 2 6 — "the anointed priest": not the king (priest), not '
                    'the many-garmented (anointed) — the office by the intersection of its tokens; the oil Lev '
                    '8:12 [IMPORT]', [FX.NONE])
    if who == 'anointed_vs_garments':
        return cell('the_bull_for_all_commandments', I, '4:3 — the bull is written on "the ANOINTED" (x%d in the '
                    'chapter); the Day of Atonement bull and the tenth of the ephah separate the serving from the '
                    'former (Lev 16, 6:13 [IMPORT])' % c_anointed, [FX.NONE])
    if who == 'congregation':
        return cell('the_court', M, SC + 'Section 4 2 — "the congregation" = the court, the identity move from '
                    'Num 35\'s assembly; 4:15 "the ELDERS of the congregation" lay the hands', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])
def blood(tier):
    if tier in ('anointed', 'congregation'):
        return cell('inside_tent', I, 'blood brought INTO the tent at 4:%s; seven times before the veil at 4:%s; '
                    'the incense altar\'s horns (4:7) / the altar before the LORD in the tent (4:18); the rest at '
                    'the base of the burnt-offering altar' % (c_into_tent, c_seven), ['accepted'])
    return cell('outer_altar_horns', I, 'the priest takes the blood with his FINGER and puts it on the horns of '
                'the burnt-offering altar (4:25, 30, 34); the rest at the base — horns at 4:%s, bases at 4:%s'
                % (c_horns, c_base), ['accepted'])
def sprinklings(tier):
    return cell(7 if tier in ('anointed', 'congregation') else 0, I, '"SEVEN times" at 4:%s — the two inner '
                'tiers only' % c_seven, [FX.NONE])
def carcass(tier):
    if tier in ('anointed', 'congregation'):
        return cell('burned_outside_camp_ash_pour', I, '4:12 "he shall carry the whole bull OUTSIDE the camp to a '
                    'PURE place, to the ash-pour, and burn it on wood with fire"; 4:21 "as he burned the first"; '
                    'Lev 6:23 [IMPORT] "every sin offering whose blood is brought into the tent... shall not be '
                    'eaten; it shall be burned"', ['burned_outside_camp'])
    return cell(OUTER['eater']['v'], P, 'CALLED cold_run_offerings.dispatch(outer_chatat) -> eater %r, place %r, '
                'window %r [IMPORT, live call]' % (OUTER['eater']['v'], OUTER['eat_place']['v'], OUTER['window']['v']),
                ['due_to_priest', 'eating_window'])
def fat(tier, species=None):
    """The fat parts of each tier's animal, resolved through the chapter's own
    pointers into Lev 3 by LIVE CALL (2026-09-06): 4:10 names the OX of the
    peace offering; 4:26 and 4:31 'as the fat of the peace offering' for the
    goats; 4:35 names the LAMB — whose inventory alone carries the tail."""
    if tier == 'pointer_census':
        seats = [v for v in range(1, 36) if any(count('Lev', 4, v, t) for t in ('יורם', 'כחלב', 'הוסר', 'יוסר'))]
        return cell(seats, I, 'the four pointer verbs — "as it is LIFTED" (4:10), "AS THE FAT" (4:26), "as it was '
                    'REMOVED" (4:31), "as it IS REMOVED" (4:35) — censused across the chapter', [FX.NONE])
    if tier in ('anointed', 'congregation'):
        f = FAT['ox']
        return cell('ox_inventory_no_tail', P, '4:10 "as it is lifted from the OX of the peace offering" (4:20 "as he '
                    'did to the bull of the sin offering" for the congregation\'s) — CALLED cold_run_offerings.dispatch'
                    '(fat:ox): parts %r, tail %r [IMPORT, live call; Sifra Chovah Chapter 4 2-3]'
                    % (f['parts']['v'], f['tail']['v']), ['smoked_to_the_lord'])
    if tier == 'leader' or (tier == 'commoner' and species == 'goat'):
        f = FAT['goat']
        return cell('goat_inventory_no_tail', P, '4:26 / 4:31 "as the fat of the peace offering" — the goat\'s own '
                    'paragraph in Lev 3 (3:12-15) names no tail — CALLED cold_run_offerings.dispatch(fat:goat): parts '
                    '%r, tail %r [IMPORT, live call]' % (f['parts']['v'], f['tail']['v']), ['smoked_to_the_lord'])
    if tier == 'commoner' and species == 'lamb':
        f = FAT['lamb']
        return cell('lamb_inventory_tail_included', P, '4:35 "as the fat of the LAMB (הכשב) is removed from the peace '
                    'offering" — the pointer names the species whose list carries the tail (3:9) — CALLED '
                    'cold_run_offerings.dispatch(fat:lamb): parts %r, tail %r [IMPORT, live call; Tamid 4:3 carries the '
                    'lamb\'s tail, lobe, and kidneys together]' % (f['parts']['v'], f['tail']['v']), ['smoked_to_the_lord'])
    return cell('unknown', I, '', [FX.NONE])
def burn_site(how):
    if how == 'as_commanded':
        return cell('ash_house_defiles_garments', I, ('4:12 "to a pure place, to the ash-pour" [INK]; Lev 16:28 '
                    '"he that BURNS them shall wash his clothes" [IMPORT] — the burner\'s garments; outside '
                    'three camps at %s (' + SC + 'Chapter 5 3-4)') % c_outside, ['burned_outside_camp', 'defiles_garments'])
    return cell('birah_no_defiling', A, 'Mishnah Zevachim 12:5 — not as commanded: burned in the fortress court, '
                'no defiling (the disqualified bull is not "the bull" of 4:12)', ['burned_outside_camp'])
def bearers(case):
    # the ink gives the burn SITE (outside three camps) but not where the
    # defilement BEGINS: consulted per gap at Yoma 68a-b
    if case == 'first_out_of_court':
        return cell('defile_from_first_camp', M, 'Yoma 68a:6-8 — "carry the whole bull outside" = outside THREE '
                    'camps: 4:12\'s "outside the camp" the first, 4:21\'s (already "as the first bull") the second, '
                    'the ash-verse\'s (already "to the ash-pour") the third — the three verses at %s counted; the '
                    'defilement begins at the FIRST camp\'s wall, the court\'s (Mishnah Zevachim 12:6\'s own '
                    'threshold), and the later bearers still inside carry nothing yet' % c_outside,
                    ['defiles_garments'])
    if case == 'flesh_consumed':
        return cell('no_defiling_after_consumed', P, 'Lev 16:28 [IMPORT] "he that BURNS them" — a participle: '
                    'once the flesh is consumed there is no burner; Yoma 68b:2 (R. Eliezer b. Yaakov: the ash-pour '
                    'must be a place where ash is poured)', [FX.NONE])
    return cell('ink_silent', I, '', [FX.NONE])
def atonement(tier):
    return cell('atoned_and_forgiven', I, '"and the priest shall atone for him and he shall be forgiven" at 4:%s '
                '— every tier closes with the pair' % c_atone, ['atoned_forgiven'])

# ---- F3: THE COURT'S ERROR (4:13-21) + THE ANOINTED'S (4:3) ----------
def court(c):
    """c: ruling ('partial'|'whole'), composition ('all_fit'|'dissent'|'mufla_absent'|'unfit_member'),
    court_intent, people_intent, acted ('majority'|'minority'|'one_tribe'), which ('great'|'tribal'),
    matter ('karet_class'|'sliding_scale'|'positive'|'sanctuary'), located (bool)."""
    if c.get('matter') in ('sliding_scale', 'sanctuary'):
        return cell('court_exempt', I, '4:13 "and DO" — the body\'s trigger is an act in the fixed domain; the '
                    'sanctuary-impurity and oath triggers are Lev 5:1-4\'s own offering on "a SOUL": CALLED '
                    'cold_run_vayikra5 -> %r (the court is no soul)' % TUMAH[:40], ['exempt'])
    if c.get('which') == 'tribal':
        return cell('R._Yehuda_that_tribe_sages_only_great_court', I, '4:13 "ALL the congregation of ISRAEL" — '
                    'the sages: not the congregation of one tribe (the Mishnah quotes the verse); R. Yehuda\'s '
                    'arm carried (' + SC + 'Section 4 13-17)', ['exempt'])
    if c.get('ruling') == 'whole':
        return cell('exempt', M, '4:13 "a THING is hidden" [INK: דבר] — ' + SC + 'Section 4 7: a thing, not the '
                    'whole body; the three worked examples Section 4 8', ['exempt'])
    if c.get('composition') in ('dissent', 'mufla_absent', 'unfit_member'):
        return cell('exempt', M, SC + 'Section 4 3-4 — all fit to rule ("congregation" here and at Num 35), '
                    'the chief present, no member saying "you err": the whole court must err', ['exempt'])
    if not c.get('located', True):
        return cell('exempt', M, SC + 'Section 4 12 — "the sin WHEREIN they sinned" (4:14): an unlocatable error '
                    'brings no bull', ['exempt'])
    ci, pi = c.get('court_intent', 'unwitting'), c.get('people_intent', 'unwitting')
    if ci == 'unwitting' and pi == 'intentional':
        return cell('exempt', I, '4:13 "they ERR... and DO" — the people\'s act must itself be unwitting; the '
                    'intentional actor is under Num 15:30 [IMPORT]', ['exempt'])
    if ci == 'intentional' and pi == 'unwitting':
        return cell('individuals_lamb_or_goat', I, '4:13 "a thing is HIDDEN from the eyes of the assembly" — no '
                    'hiddenness in the court, no court bull; each unwitting actor falls to 4:27\'s "one soul"',
                    ['atoned_forgiven'])
    if c.get('acted') == 'minority':
        return cell('individuals_lamb_or_goat', M, SC + 'Section 7 5 (the minority/majority leg): the bull rides '
                    '"all the congregation" or its majority; a minority each their own', ['atoned_forgiven'])
    if c.get('sin') == 'idolatry':
        return cell('bull_and_goat', P, 'Num 15:24 [IMPORT] — the bull for a burnt offering and the goat for a '
                    'sin offering (R. Meir\'s arm; R. Yehuda twelve, R. Shimon thirteen — ' + SC +
                    'Section 4 13-17 carried)', ['accepted'])
    return cell('bull', I, '4:14 "the assembly shall offer a bull" — the court erred in part and the majority '
                'acted on it (both components: ' + SC + 'Section 4 5)', ['atoned_forgiven'])
def tribes(arm):
    return cell({'R._Meir': 'one_bull', 'R._Yehuda': 'twelve_bulls', 'R._Shimon': 'thirteen_bulls'}[arm], M,
                SC + 'Section 4 13-17 — the four recorded positions on one arithmetic; "the assembly" doubled for '
                'R. Shimon\'s thirteenth', ['accepted'])
def reliance(c):
    """Horayot 1:1-1:2 — the individual who acted on the court's ruling."""
    if c.get('knew_error') or c.get('fit_to_rule'):
        return cell('liable', M, SC + 'Section 7 1 — "in doing IT" (4:27): the OWN act; one who relied on '
                    'himself (a member who knew, a student fit to rule) is liable', ['atoned_forgiven'])
    if c.get('court_retracted'):
        if c.get('where') == 'overseas':
            return cell('exempt', A, 'Mishnah Horayot 1:2 — went overseas: could not have heard (ben Azzai); '
                        'R. Akiva concedes', ['exempt'])
        if c.get('where') == 'at_home':
            return cell('liable', A, 'Mishnah Horayot 1:2 — sat at home: could have heard', ['atoned_forgiven'])
        return cell('R._Shimon_exempt_R._Eliezer_doubt', M, (SC + 'Section 7 3 — R. Shimon\'s retraction edge: '
                    'he relied on the standing law; R. Eliezer: a doubt, the suspended ram (CALLED -> %r)') % TALUI,
                    ['exempt', 'suspends'])
    return cell('exempt_relied_on_court', M, SC + 'Section 7 2 — with them, after them, before them: every '
                'combination exempt individually; the court\'s bull covers ("one who relies on the court")',
                ['exempt'])
def anointed_ruling(c):
    """Horayot 2:1-2:2 — the anointed priest's own ruling."""
    ri, ai = c.get('ruling_intent'), c.get('act_intent')
    if ri == 'unwitting' and ai == 'unwitting':
        if c.get('with_public'):
            return cell('atoned_with_public', M, SC + 'Chapter 2 7 (the sinned-with-the-congregation leg): ruled '
                        'with them and acted with them — atoned with them', ['atoned_forgiven'])
        return cell('bull', M, '4:3 "to the guilt of the people" [INK] — ' + SC + 'Chapter 2 1: likened to the '
                    'congregation, liable only for his own erroneous RULING acted on unwittingly', ['atoned_forgiven'])
    return cell('exempt', M, SC + 'Chapter 2 1 — a slip of deed without a ruling, or a ruling acted on '
                'deliberately, brings no bull (the two components as the court\'s)', ['exempt'])
def binds_others():
    return cell('himself_only', M, SC + 'Chapter 2 5 — "which HE sinned": others who acted on his ruling are '
                'not his liability; his court is not the court', [FX.NONE])
def sliding_scale_by_tier(tier, trigger):
    if tier == 'court':
        return cell('exempt', I, 'Lev 5:1-4 opens on "a SOUL" — the body is no soul; CALLED cold_run_vayikra5 '
                    '-> %r for the person' % TUMAH[:40], ['exempt'])
    if tier == 'leader':
        if trigger == 'hearing':
            return cell('R._Yosei_HaGelili_exempt_R._Akiva_exempt', P, 'Mishnah Sanhedrin 2:2 [IMPORT] — the king '
                        'neither judges nor testifies: no testimony oath can find him', ['exempt'])
        return cell('R._Yosei_HaGelili_exempt_R._Akiva_liable', A, 'Mishnah Horayot 2:5 — the leader "like them" '
                    '(R. Yosei HaGelili) / liable in all but hearing (R. Akiva)', ['exempt', 'atoned_forgiven'])
    if tier == 'anointed' and trigger == 'sanctuary_impurity':
        return cell('R._Shimon_exempt', A, 'Mishnah Horayot 2:7 — the high priest not liable for sanctuary '
                    'impurity (R. Shimon)', ['exempt'])
    return cell('sliding_scale', P, 'CALLED cold_run_vayikra5.graded_offering -> %r' % LADDER['reaches_lamb'][:40],
                ['atoned_forgiven'])
def talui_by_tier(tier):
    if tier in ('individual', 'leader'):
        return cell('liable', M, (SC + 'Section 5 8 — "and he be guilty" (4:22): the leader DOES bring the '
                    'suspended ram; the individual by Lev 5:17\'s "a soul" (CALLED -> %r)') % TALUI, ['suspends'])
    return cell('exempt', M, SC + 'Chapter 2 1 — the anointed is likened to the court (4:3 "to the guilt of the '
                'people"); the court brings no ram at all (no "soul")', ['exempt'])
def vadai_by_tier(tier):
    if tier == 'court':
        return cell('exempt', I, 'Lev 5:15, 5:21 open on "a SOUL" — the body is no soul', ['exempt'])
    return cell('liable', P, 'Lev 5:15-26 — CALLED cold_run_vayikra5.sacrilege -> %r' % MEILAH[:30], ['accepted'])

# ---- F4: TIMING AND OFFICE (Horayot 3:1-3:3) --------------------------
def timing(c):
    tier, when = c['tier'], c['when']
    if when == 'sinned_then_removed':
        return cell({'anointed': 'bull', 'leader': 'he_goat'}[tier], M, SC + 'Chapter 2 6 — he brings the bull '
                    'even after removal: the obligation follows the man who held it (Section 5 2 at the leader)',
                    ['atoned_forgiven'])
    if when == 'removed_then_sinned':
        if tier == 'anointed':
            return cell('bull', I, '4:3 "the ANOINTED priest" — a completed act written on the man (המשיח, '
                        'x%d), not a standing office; the oil once poured (Lev 8:12 [IMPORT])' % c_anointed,
                        ['atoned_forgiven'])
        return cell('commoner', M, '4:22 "WHEN a leader sins" [INK: the office at the time of the sin] — ' + SC +
                    'Section 5 2: "if he sin" is the present tense of office; Horayot 11a:20-11b:1 fixes the '
                    'office itself ("the LORD his God" here and at Deut 17:19 — none above him but his God), and '
                    '11b:2-3 tests the parameter on Rabbi against the exilarch', ['atoned_forgiven'])
    if when == 'sinned_before_appointment':
        if c.get('arm') == 'R._Shimon':
            return cell('known_before_liable_known_after_exempt', M, SC + 'Section 2 7 + Section 5 3 — R. '
                        'Shimon: the offense is dated by when it became KNOWN (4:23 "made known to him")',
                        ['atoned_forgiven', 'exempt'])
        return cell('commoner', M, SC + 'Section 5 2 — "if he sin" (4:22): present tense of office; pre-'
                    'appointment sins are the commoner\'s', ['atoned_forgiven'])
    return cell('unknown', I, '', [FX.NONE])

# ---- F5: THE AGGREGATION (4:2 "of one of them"; 4:22 "one of") --------
def aggregate(lapses, knowledge_between=False, arm=None):
    """lapses: a list of lists of sin NAMES (each inner list = one lapse of awareness).
    Returns the count of sin offerings by the ink's key: one per NAME per LAPSE."""
    n = 0
    for lapse in lapses:
        n += len(set(lapse))
    return cell(n, M, '4:2 "of ONE of them" / 4:22 "ONE of all the commandments" [INK] — ' + SC + 'Section 5 4-5: '
                'two kinds in one lapse — two offerings; one kind in two lapses — two; Chapter 1 7: the count is '
                'keyed to the missing knowledge', ['atoned_forgiven'] if n else ['exempt'])
def half_olive(kinds):
    if kinds == 1:
        return cell('liable', D, 'the OLIVE is the data channel; two halves of ONE kind in one eating-time join '
                    '(Mishnah Keritot 3:2 — the measure\'s own rule)', ['atoned_forgiven'])
    return cell('exempt', D, 'two halves of TWO kinds do not join to one name', ['exempt'])
def emmaus(q):
    if q == 'three_sisters_one_lapse':
        return cell(OPEN, M, SC + 'Chapter 1 8 — R. Akiva\'s Emmaus question, asked of R. Gamliel and R. '
                    'Yehoshua, UNANSWERED: the recorded open node', [FX.NONE])
    if q == 'five_niddah_wives':
        return cell(5, A, 'Mishnah Keritot 3:7 — "but we have heard": five menstruant wives in one lapse, liable '
                    'for each (one name, five bodies)', ['atoned_forgiven'])
    if q == 'five_slaughters_outside':
        return cell(OPEN, M, (SC + 'Chapter 1 10-12 — "we have not heard"; R. Yehoshua\'s five-dishes sacrilege '
                    'analogy (each liable — CALLED -> %r), R. Shimon\'s leftover version, R. Akiva\'s method note: '
                    '"if a ruling, we accept it; if an argument, there is a reply" — and the reply: sacrilege '
                    'counts the feeder as the eater and joins over time') % MEILAH[:20], [FX.NONE])
    if q == 'many_labors_many_sabbaths_one_kind':
        return cell('R._Eliezer_each_R._Akiva_refutes', M, SC + 'Chapter 1 13 — R. Eliezer: one per derivative '
                    '(the a-fortiori from the menstruant); Chapter 1 7: aware of the day, not the labor — one per '
                    'labor-kind; R. Akiva\'s three refutations carried', ['atoned_forgiven'])
    return cell('unknown', I, '', [FX.NONE])
def names_one_act(names, arm=None):
    if arm == 'R._Yochanan_b._Nuri':
        return cell(len(names), A, 'Mishnah Keritot 3:6 — three names for the mother-in-law alone', ['atoned_forgiven'])
    if arm == 'sages_one_name':
        return cell('one_name', A, 'Mishnah Keritot 3:6 — "the three are ONE name" (mother-in-law, her mother, '
                    'his father-in-law\'s mother)', [FX.NONE])
    return aggregate([names])
def four_and_one(names):
    chatat = [n for n in names if n != 'consecrated']
    asham = 1 if 'consecrated' in names else 0
    return cell('%d chatat + %d asham' % (len(chatat), asham), M, (SC + 'Section 5 4 — per name; the consecrated '
                'piece is sacrilege: CALLED cold_run_vayikra5.sacrilege -> %r') % MEILAH[:30],
                ['atoned_forgiven', 'accepted'])
def witnesses(c):
    """Keritot 3:1 — the epistemic trigger (4:23 'his sin be made KNOWN to him')."""
    w = c['witnesses']
    if w == 'two_say_ate_no_denial':
        return cell('chatat', M, '4:23 "made KNOWN to him" [INK] — ' + SC + 'Chapter 7 2: informed by two and not '
                    'refuting — liable', ['atoned_forgiven'])
    if w == 'one_vs_one':
        return cell('talui', P, 'the doubt case — CALLED cold_run_vayikra5.sacrilege(doubt) -> %r' % TALUI, ['suspends'])
    if w == 'one_vs_his_denial':
        return cell('exempt', M, SC + 'Chapter 7 1 — self-knowledge, not being told: "become known TO HIM"',
                    ['exempt'])
    if w == 'two_vs_his_denial':
        return cell('R._Meir_liable_sages_exempt', M, SC + 'Chapter 7 3 — R. Meir: if two bring him to death '
                    'they bring him to an offering; R. Yehuda refutes: the offering rides his own knowledge '
                    '("what if he says I was deliberate")', ['atoned_forgiven', 'exempt'])
    return cell('unknown', I, '', [FX.NONE])
def which_sin(c):
    """4:23 'wherein he sinned IN IT' (בה) — the required knowledge."""
    if c == 'mitasek':
        return cell('exempt', I, '4:23 "wherein he sinned IN IT" (בה) — excludes the one occupied with another '
                    'thing (Mishnah Keritot 4:3 quotes the token)', ['exempt'])
    if c == 'same_name':
        return cell('liable', M, SC + 'Chapter 7 9 — same-name doubt (which fig tree): liable, both agree',
                    ['atoned_forgiven'])
    if c == 'two_names':
        return cell('R._Eliezer_chatat_R._Yehoshua_exempt', M, SC + 'Chapter 7 6-7 — the wife-and-sister case: '
                    'R. Yehoshua exempts (the offering needs a named object), R. Eliezer liable either way',
                    ['atoned_forgiven', 'exempt'])
    if c == 'twilight':
        return cell('exempt_both', M, SC + 'Chapter 7 8 — R. Yosei: the twilight-spanning labor, part today part '
                    'tomorrow — no single day to name; both agree', ['exempt'])
    if c == 'figs_grapes':
        return cell('R._Eliezer_chatat_R._Yehoshua_exempt', M, SC + 'Chapter 7 10 — the worked case table; '
                    'R. Yehuda wonders if R. Yehoshua exempts', ['atoned_forgiven', 'exempt'])
    return cell('unknown', I, '', [FX.NONE])

# ---- F6: THE DOUBT — the suspended ram and the pieces (Lev 5:17 on 4:2's domain) ----
def pieces(a, b, ate='one_unknown', arm=None):
    """a, b: piece types among 'hullin', 'kodesh', 'fat', 'kodesh_fat', 'notar_fat'.
    Certain karet-name -> a sin offering per name; doubtful karet-name -> the suspended ram (CALLED);
    certain sacrilege -> the certain ram (CALLED); doubtful sacrilege -> the recorded dispute."""
    sin_names = {'hullin': set(), 'kodesh': set(), 'fat': {'fat'}, 'kodesh_fat': {'fat'}, 'notar_fat': {'fat', 'notar'}}
    meilah = {'hullin': False, 'kodesh': True, 'fat': False, 'kodesh_fat': True, 'notar_fat': False}
    A_, B_ = sin_names[a], sin_names[b]
    certain = A_ & B_                     # names both pieces carry: the sin is certain whichever was eaten
    doubtful = (A_ | B_) - certain        # names only one piece carries
    m_certain = meilah[a] and meilah[b]
    m_doubt = (meilah[a] or meilah[b]) and not m_certain
    if ate == 'one_unknown':
        out = []
        out += ['chatat'] * len(certain)
        if doubtful: out.append('talui')
        if m_doubt: out.append('R._Akiva_talui_sages_exempt')
        if m_certain: out.append('asham_vadai')
        v = ' + '.join(out) if out else 'exempt'
        fx = (['atoned_forgiven'] if certain else []) + (['suspends'] if doubtful else []) + ([] if out else ['exempt'])
        return cell(v, P, 'certain names %s -> Lev 4\'s own sin offering; doubtful names %s -> Lev 5:17 CALLED '
                    '(-> %r); sacrilege doubt -> CALLED (-> %r)' % (sorted(certain), sorted(doubtful), TALUI,
                    MEILAH_DOUBT[:40]), fx or [FX.NONE])
    if ate == 'both':
        out = ['chatat'] * (len(A_) + len(B_))
        if meilah[a] or meilah[b]: out.append('asham_vadai')
        return cell(' + '.join(out), P, ('both eaten: every name certain — per name (' + SC + 'Section 5 4); '
                    'the consecrated piece: CALLED cold_run_vayikra5.sacrilege -> %r') % MEILAH[:30],
                    ['atoned_forgiven'] + (['accepted'] if meilah[a] or meilah[b] else []))
    if ate == 'two_persons':
        one = pieces(a, b, 'one_unknown')['v']
        if arm == 'R._Shimon':
            shared = 'one asham' if (m_doubt or m_certain) else 'one chatat'
            return cell('each_%s; together %s' % ('chatat' if certain else 'talui', shared), A,
                        'Mishnah Keritot 5:4-8 — R. Shimon: the two bring ONE offering together', ['suspends'])
        if arm == 'R._Yosei':
            return cell('each; never two for one', A, 'Mishnah Keritot 5:4-8 — R. Yosei: two never bring one '
                        'sin offering that comes for a sin, nor one ram', ['suspends'])
        return cell('each: ' + one, P, 'R. Akiva / the first tanna: each person carries his own doubt — the same '
                    'call per person', ['suspends'])
    return cell('unknown', I, '', [FX.NONE])
def resolution(c):
    """Keritot 6:1-6:2 — the suspended ram (and the certain ram) when the doubt resolves."""
    kind, stage = c['kind'], c['stage']
    if kind == 'talui':
        if stage == 'before_slaughter':
            return cell('R._Meir_pasture_sages_blemish_sell_R._Eliezer_offer', A, 'Mishnah Keritot 6:1 — the '
                        'three arms; the ram never became an offering (Lev 5:18 "for his error which he erred '
                        'AND HE KNEW IT NOT" — no not-knowing, no ram)', [FX.NONE])
        if stage == 'after_slaughter':
            return cell('blood_poured_flesh_burned', M, SC + 'Chapter 21 3 at Lev 5:19 — resolution mid-rite: '
                        'slaughtered, then resolved — the flesh path; the blood not thrown', ['burn_remainder'])
        if stage == 'after_zerikah':
            return cell('flesh_eaten', M, SC + 'Chapter 21 3 — blood sprinkled, THEN the doubt resolved: the rite '
                        'completes; R. Yosei: even blood in the cup is thrown', ['due_to_priest'])
    if kind == 'vadai':
        return cell({'before_slaughter': 'pasture', 'after_slaughter': 'buried', 'after_zerikah': 'flesh_burned'}[stage],
                    A, 'Mishnah Keritot 6:2 — the certain ram is not so', [FX.NONE])
    if kind == 'stoned_ox':
        if stage == 'before_stoning':
            return cell('pasture', A, 'Mishnah Keritot 6:2', [FX.NONE])
        return cell('benefit_permitted', P, 'Exod 21:28 [IMPORT] "and its flesh shall not be EATEN" — the ban is '
                    'on eating; the Mishnah reads benefit permitted after the stoning', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])
def day_of_atonement(c):
    if c == 'chatat_owed':
        return cell('bring_after', M, (SC + 'Section 3 1 — "he shall bring" (4:4): even after the Day of Atonement; '
                    'Section 6 1 at the leader (4:23); Keritot 26a:19 (R. Zeira: "knowledge" written at the three '
                    'tiers, 4:%s — the known sin outlives the Day)') % c_hoda, ['atoned_forgiven'])
    if c == 'talui_owed':
        return cell('exempt', M, 'Lev 16:30 "on this day he shall atone for you... from ALL your sins" [IMPORT] — '
                    'Keritot 26a:19: a sin that none but the Omnipresent knows, the Day atones; and R. Zeira\'s '
                    'own reason why the CERTAIN sin offering is not cleared: KNOWLEDGE is written at the sin '
                    'offering, the leader, and the congregation — the ink census at 4:%s' % c_hoda, ['exempt'])
    if c == 'doubt_on_the_day':
        return cell('exempt', A, 'Mishnah Keritot 6:4 — even at dusk, for the WHOLE day atones (Lev 16:30 '
                    '"on this DAY")', ['exempt'])
    return cell('unknown', I, '', [FX.NONE])
def ownership(c):
    if c == 'dead_father':
        return cell('no_discharge', I, '4:28 "HIS offering on HIS sin" (קרבנו על חטאתו) — two possessives; ' + SC +
                    'Section 6 1-4: not his dead father\'s beast nor his monies', ['disqualified'])
    if c == 'sin_to_sin':
        return cell('no_discharge', I, '4:28 "on HIS sin which he sinned" — for the name of that sin; ' + SC +
                    'Section 6 5: fat set aside, blood eaten — no discharge', ['disqualified'])
    return cell('unknown', I, '', [FX.NONE])
def conversion(c):
    if c == 'became_poor':
        return cell('birds', P, 'CALLED cold_run_vayikra5 ladder at reaches_birds -> %r' % LADDER['reaches_birds'][:30],
                    ['consecrated'])
    if c == 'became_poorer':
        return cell('flour', P, 'CALLED at reaches_flour -> %r' % LADDER['reaches_flour'][:30], ['consecrated'])
    if c == 'became_rich':
        return cell('lamb_or_goat', P, 'CALLED at reaches_lamb -> %r' % LADDER['reaches_lamb'][:30], ['consecrated'])
    if c == 'blemished_lamb':
        return cell('bird_from_its_price', P, 'Lev 27:11-13 [IMPORT] — the blemished beast is redeemed; its price '
                    'buys the next rung', ['consecrated'])
    if c == 'blemished_bird':
        return cell('no_flour_from_its_price', P, 'Lev 27:11 [IMPORT] "and if any unclean BEAST" — only a beast is '
                    'redeemed; a bird has no redemption (the consecration engine\'s cell)', ['disqualified'])
    return cell('unknown', I, '', [FX.NONE])

# ---- F7: PRECEDENCE (Zevachim 10) -------------------------------------
def precedence(q):
    if q == 'chatat_blood_vs_olah_blood':
        return cell('chatat_blood_first', I, 'the sin offering PROPITIATES — "atone... forgiven" at 4:%s (four '
                    'closes); the burnt offering\'s blood carries no such close in Lev 1' % c_atone, [FX.NONE])
    if q == 'olah_limbs_vs_chatat_innards':
        return cell('olah_limbs_first', P, 'Lev 1:9 [IMPORT] "the WHOLE to the fires"', [FX.NONE])
    if q == 'chatat_vs_asham':
        return cell('chatat_first', I, 'horns AND base at 4:%s (four horns and the base); the guilt offering\'s '
                    'blood "AROUND" (Lev 7:2 [IMPORT]) — more applications, more holy' % c_horns, [FX.NONE])
    if q == 'asham_vs_todah':
        return cell('asham_first', P, 'Lev 7:1 [IMPORT] "it is most holy"', [FX.NONE])
    if q == 'todah_vs_shelamim':
        return cell('todah_first', P, 'Lev 7:12-15 [IMPORT] — one day and bread', [FX.NONE])
    if q == 'shelamim_vs_bekhor':
        return cell('shelamim_first', P, 'Lev 3:2, 3:8, 7:30 [IMPORT] — four applications, laying, libations, '
                    'the waving of breast and thigh', [FX.NONE])
    if q == 'chatat_vs_asham_all':
        return cell('chatat_first_except_leper', P, 'as chatat_vs_asham; the leper\'s ram comes for FITNESS — '
                    'Lev 14:14 [IMPORT], the affliction engine', [FX.NONE])
    if q == 'asham_age_price':
        return cell('two_years_silver_shekels', P, 'Lev 5:15 "silver SHEKELS" [INK there] — CALLED '
                    'cold_run_vayikra5.DATA ram_floor = %r; the two years from the ram (Lev 5:15 "a ram")'
                    % V5.DATA['ram_floor'][:12], [FX.NONE])
    if q == 'nazir_leper_asham':
        return cell('yearlings_no_shekels', P, 'Num 6:12, Lev 14:10 [IMPORT] — "a lamb of its first year"', [FX.NONE])
    if q == 'bird_chatat_vs_bird_olah':
        return cell('chatat_first', P, 'Lev 5:8 "the sin offering FIRST" — CALLED cold_run_vayikra5 -> %r' % BIRDS,
                    [FX.NONE])
    if q == 'sinner_minchah_vs_voluntary':
        return cell('sinner_first', P, 'Lev 5:11 "for it is a SIN offering" — it comes for sin; CALLED -> %r'
                    % LADDER['reaches_flour'][:30], [FX.NONE])
    if q == 'yesterday_shelamim_vs_today_chatat':
        return cell('R._Meir_shelamim_sages_chatat', P, 'R. Meir: the peace offering\'s window is closing — CALLED '
                    'cold_run_offerings shelamim window %r; the sages: Lev 6:18 "it is MOST HOLY" [IMPORT]'
                    % SHEL['window']['v'], ['eating_window'])
    if q == 'eating_manner':
        return cell('roasted_boiled_cooked', A, 'Mishnah Zevachim 10:7 — Lev 10:12-14\'s "eat it" verbs state no '
                    'manner; the heave-offering spice member is Lev 22\'s (sitting L5)', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F8: THE SHARE (Zevachim 12:1) ------------------------------------
def share(who):
    if who == 'onen':
        return cell('touches_not_offers_not_shares', M, 'Lev 10:19 [INK] — the mourner\'s DAY: "had I eaten the '
                    'sin offering TODAY, would it be good?" — he does not eat that day (' + SS + 'Chapter 2 11); '
                    'the sons did not OFFER either — Zevachim 101a:9, 14: "did THEY offer? I offered," Moses '
                    'himself; and 101a:10-11 the a-fortiori from the tithe (Deut 26:14 "I have not eaten of it in '
                    'my mourning" [IMPORT]) for the holy of the generations', ['barred_from_it'])
    if who == 'blemished':
        return cell('shares_and_eats_not_offers', P, 'Lev 21:21-22 [IMPORT] — "he shall not approach to offer... '
                    'the bread of his God, of the most holy and of the holy, he may EAT"', ['due_to_priest'])
    if who == 'tevul_yom':
        return cell('no_share_at_evening', P, 'Lev 22:6-7 [IMPORT, sitting L5] — "and when the sun sets he is '
                    'clean, and afterward he may eat"', ['barred_from_it'])
    if who == 'impure_at_zerikah':
        return cell('no_share', P, 'Lev 7:33 [IMPORT] "he who OFFERS the blood... to him shall be the right '
                    'thigh" — the share rides the offering', ['barred_from_it'])
    return cell('unknown', I, '', [FX.NONE])

# ---- F9: THE PRIEST'S TABLE (10:12-15) ---------------------------------
def table(q):
    if q == 'minchah_remainder':
        return cell('unleavened_beside_altar_most_holy', I, '10:12 "eat it UNLEAVENED beside the altar, for it is '
                    'MOST HOLY"; CALLED cold_run_minchah.remainder -> %r' % MIN_REM, ['due_to_priest', 'most_holy'])
    if q == 'minchah_place':
        return cell('holy_place', I, '10:13 "in a HOLY place" (x%d)' % c_place_words[0], [FX.NONE])
    if q == 'breast_thigh_place':
        return cell('pure_place', I, '10:14 "in a PURE place" (x%d) — the ink CHANGES the place-word between the '
                    'meal offering and the breast and thigh' % c_place_words[1], [FX.NONE])
    if q == 'pure_place_is':
        return cell('inside_jerusalem', M, SS + 'Chapter 1 9 — R. Nechemia: a purity not of impurity\'s kind, '
                    'pure of the LEPER\'s impurity: inside Jerusalem', [FX.NONE])
    if q == 'daughters':
        return cell('daughters_eat_breast_thigh_not_minchah', I, '10:14 "you and your sons and your DAUGHTERS" '
                    '(ובנתיך) against 10:13 "your due and your SONS\' due"; ' + SS + 'Chapter 1 7, 1 10: sons in '
                    'the share, daughters in the gifts', ['due_to_priest'])
    if q == 'breast_thigh_due':
        return cell('to_the_priests_after_smoking', P, '10:15 "the thigh of the heave and the breast of the waving... '
                    'shall be yours and your sons\' with you, a perpetual due, AS THE LORD COMMANDED (כאשר צוה)" — the '
                    'pointer to Lev 7:30-34; CALLED cold_run_tzav.dues_machine(breast_thigh) -> %r [IMPORT, live call]'
                    % BREAST_THIGH, ['due_to_priest'])
    if q == 'fats_position':
        return cell('fats_below', M, '10:15 "ON the fire-portions of the fats" [INK] — ' + SS + 'Chapter 1 11: '
                    'the fats BELOW at the carrying', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F10: THE INQUIRY (10:16-20) --------------------------------------
def inquiry(q):
    if q == 'blood_not_inside':
        return cell('eaten_in_holy_place', I, '10:18 "behold its blood was NOT brought inside the sanctuary — you '
                    'should have eaten it in the holy place"; Lev 6:19, 6:23 [IMPORT]', ['eaten_to_atone', 'due_to_priest'])
    if q == 'blood_inside':
        return cell('burned', P, '10:18 read in its negative: brought inside — not eaten, "AS I COMMANDED (כאשר '
                    'צויתי)" — the pointer to Lev 6:23 "shall not be eaten; it shall be burned"; CALLED '
                    'cold_run_offerings.dispatch(inner_chatat_burned) burn_place -> %r [IMPORT, live call]'
                    % INNER['burn_place']['v'], ['burned_outside_camp'])
    if q == 'eating_atones':
        return cell('priests_eat_owners_atoned', I, '10:17 "He gave it to you to BEAR the iniquity of the '
                    'congregation, to atone for them" — the eating IS the atonement (' + SS + 'Chapter 2 4)',
                    ['eaten_to_atone'])
    if q == 'which_goat_burned':
        return cell('new_moon_goat', M, (SS + 'Chapter 2 1-2 — three goats that day; the doubled "inquired" = two '
                    'inquiries (דרש x%d at 10:16); the burned one: the New Moon\'s, "given to bear the assembly\'s '
                    'sin" — Zevachim 101b:6-7 holds the Sifra\'s row word for word ("goat" Nachshon\'s, "sin '
                    'offering" the eighth day\'s, "inquired" the New Moon\'s; "behold it was burned" — ONE burned)') % c_darash, [FX.NONE])
    if q == 'why_burned':
        return cell('R._Nechemia_mourning_R._Yehuda_R._Shimon_impurity', M, SS + 'Chapter 2 8 (for the '
                    'mourning — "such things have befallen me") / Chapter 2 10 (for impurity, three refutations)',
                    [FX.NONE])
    if q == 'high_priest_onen':
        return cell('offers_not_eats', I, '10:19 "they OFFERED their sin offering and burnt offering today... and had '
                    'I EATEN the sin offering today, would it be good?" — offered, did not eat; 10:20 Moses agreed '
                    '(Zevachim 101a:6, Rava: the holy of the HOUR eaten in mourning, the holy of the generations '
                    'not; 101a:12: "I heard and forgot")', ['barred_from_it'])
    if q == 'mourner_day_night':
        return cell('day_torah_night_R._Yehuda_torah_Rabbi_scribes', M, SS + 'Chapter 2 11 — "had I eaten TODAY": '
                    'the Torah bars the day; the night — R. Yehuda: day and night for the generations; Rabbi: the '
                    'night from the scribes (the immersed mourner eats his Passover at evening)', ['barred_from_it'])
    if q == 'moses_admitted':
        return cell('admitted_at_once', I, '10:20 "Moses heard and it was GOOD in his eyes" (' + SS + 'Chapter 2 12: '
                    '"I heard and forgot")', [FX.NONE])
    return cell('unknown', I, '', [FX.NONE])

# ---- F11: THE WINE BAN (10:9-11) --------------------------------------
def wine(c):
    """c: drink ('wine'|'other_intoxicant'|'water'), amount ('quarter_log'|'less'|'more'), diluted, interrupted,
    act ('enter_tent'|'serve'|'rule'|'teach'|'none'), who ('priest'|'israelite'|'profaned_priest')."""
    if c.get('who') == 'profaned_priest':
        return cell('outside_the_ban', M, SS + 'Section 1 3 — "you and your sons WITH you": profaned and '
                    'blemished priests excluded from the ban\'s scope', [FX.NONE])
    if c.get('who') == 'israelite':
        if c.get('act') == 'rule':
            return cell('no_death', M, SS + 'Section 1 6 — "you and your sons... and you shall not die": YOU in '
                        'death, Israel not (ruling while drunk)', [FX.NONE])
        return cell('outside_the_ban', I, '10:9 "you and your sons with you" — the addressee is Aaron\'s house',
                    [FX.NONE])
    if c.get('drink') == 'water' or c.get('act') == 'none':
        return cell('no_ban', I, '10:9 "when you COME INTO the tent of meeting" — the ban rides the entry', [FX.NONE])
    if c.get('diluted') or c.get('interrupted'):
        return cell('R._Eliezer_exempt', M, SS + 'Section 1 2 — R. Eliezer: only drunk in its manner; diluted with '
                    'any water — exempt (Mishnah Keritot 3:3\'s arm)', ['exempt'])
    if c.get('amount') == 'less':
        return cell('warned_not_death', M, SS + 'Section 1 1-2 — "strong drink" = ENOUGH TO INTOXICATE, a '
                    'quarter-log (DATA); "wine" warned even at any amount', [FX.NONE])
    if c.get('act') in ('enter_tent', 'serve'):
        if c.get('drink') == 'other_intoxicant':
            return cell('R._Yehuda_warning_not_death', M, SS + 'Section 1 2 — R. Yehuda: wine carries death, other '
                        'intoxicants a warning', [FX.NONE])
        return cell('liable_death', I, '10:9 "wine and strong drink do not drink... when you come into the tent of '
                    'meeting, AND YOU SHALL NOT DIE" — death by Heaven; the quarter-log the data channel (' + SS +
                    'Section 1 1)', ['death_by_heaven'])
    if c.get('act') == 'teach':
        return cell('teaching_barred', M, '10:11 "and to TEACH the children of Israel" [INK — the job named beside '
                    'the ban] — Keritot 13b:16-18: "to distinguish... to teach" = the rulings, and "could even the '
                    'Mishnah? the verse says to teach" (R. Yosei b. R. Yehuda: even the Talmud); 13b:19: the plain '
                    'ruling (a creeping thing impure, a frog pure) a drunk MAY teach — "go read it at the school"; '
                    '13b:20: Rav, who ruled wherever he sat, set no expositor on a festival\'s morrow', ['teaching_barred'])
    return cell('unknown', I, '', [FX.NONE])
def wine_service_validity():
    return cell('service_invalid', M, (('10:10 "to DISTINGUISH between the holy and the profane" [INK, %d pairs] — '
                'Zevachim 17b:7: "from where that a drunk who served has PROFANED? wine and strong drink do not '
                'drink... and to distinguish between the holy and the profane"; 18a:1-5: the missing-garmented '
                'and the unwashed joined by the statute-statute analogy (10:9 / Exod 29:9); Sanhedrin 22b:14 (Rav '
                'Ashi: wine-drinkers profane service) — ') + SS + 'Section 1 8 holds it verbatim') % c_havdil_pairs,
                ['service_profaned'])
def wine_today():
    return cell('Rabbi_forbidden_forever_remedy_is_ruin', M, '10:9 "an everlasting statute for your generations" '
                '[INK] — Sanhedrin 22b:11-12: Rabbi: priests are forbidden wine FOREVER (the House may be rebuilt '
                'at once and a fit priest be needed) — "but what can I do, its ruin is its remedy"; Abaye: the '
                'priests drink today as Rabbi — so the sages forbid', [FX.NONE])
def wine_dissipation():
    return cell('quarter_log_dissipates_more_does_not', D, 'Sanhedrin 22b:13 — Rav Acha: a mil\'s walk and any '
                'sleep dissipate the wine; Rav Nachman: only for a QUARTER-LOG — more than that, the road disturbs '
                'him and sleep intoxicates him (the data channel\'s quantity at a third machine)', [FX.NONE])
def curriculum():
    return cell('valuations_purity_rulings_expositions_halachot_scripture', M, SS + 'Section 1 9 — the '
                'curriculum verse: "to distinguish holy/profane" = the valuations; "impure/pure" = the purity '
                'laws; "to teach" = the rulings; "all the statutes" = the expositions; "which the LORD spoke" '
                '= the halachot; "by the hand of Moses" = Scripture — and "could even the TRANSLATION?" bounded '
                'on the page', [FX.NONE])

# ---- THE WRAP (W3 THE OFFERING ENGINE, D9-iii, 2026-09-07) — the daemon and the scene --------------
# Nine case heads: the soul sinning unwittingly (4:2 with its tiers 4:3, 4:22, 4:27, 4:32 — the domain, the
# rank, the two blood routes, the fat by the chapter's pointers, the carcass, the atonement), the court's error
# and the anointed's ruling (4:13-14, 4:3), the individual who acted on the ruling (4:27 "in doing IT"), the sin
# made known (4:23, 4:28), the doubtful sin (5:17-18 — the pieces and the resolution; law_vayikra5's seat too),
# the sin offering designated (4:28, 4:23), the priest's table (10:12-17), the inquiry (10:16-19), the wine ban
# (10:9-10). The daemon writes the ledger and never emits an event.
import world_engine as WE
def law_chatat(event, world):
    """Lev 4 + 10:8-20 (cold_run_chatat.py — the domain, the rank tree, the two routes, the court, the doubt, the table, the inquiry, the wine)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'sinned_unwittingly':
        d = domain({'intent': event['intent'], 'person': event.get('person'), 'commandment_kind': event.get('commandment_kind'), 'act': event.get('act', True),
                    'law_source': event.get('law_source'), 'age': event.get('age'), 'state': event.get('state')})
        if 'exempt' in d['fx']:
            return [E_('exempt', event['sinner'], value=d['v'], law='F1 [INK 4:2 — the domain: %s]' % d['why'][:80])]
        if 'karet_cut_off' in d['fx']:
            return [E_('karet_cut_off', event['sinner'], cp='HEAVEN', value=d['v'], law='F1 [Num 15:30 "with a high hand... cut off"; 4:2 "unwittingly" excludes him]')]
        if 'suspends' in d['fx']:
            return [E_('suspends', event['sinner'], value=d['v'], law='F1 [Lev 5:17 — the suspended ram, CALLED cold_run_vayikra5.sacrilege(doubt)]')]
        tier, sp = event['tier'], event.get('species')
        out = [E_('accepted', event['sinner'], cp='HEAVEN', value=rank(tier, event.get('sin', 'general'), sp)['v'], law='F2 [INK 4:3, 4:14, 4:23, 4:28, 4:32 — the rank by tier]'),
               E_('smoked_to_the_lord', 'the-sin-offering', value=fat(tier, sp)['v'], law='F2 [INK 4:10, 4:26, 4:31, 4:35 — the fat by the chapter\'s own pointers into Lev 3, by call]')]
        if tier in ('anointed', 'congregation'):
            out += [E_('burned_outside_camp', 'the-sin-offering', value=carcass(tier)['v'], law='F2 [INK 4:12, 4:21 "outside the camp to the ash-pour"; Lev 6:23]'),
                    E_('defiles_garments', 'the-burner', value=burn_site('as_commanded')['v'], law='F2 [Lev 16:28 "he that burns them shall wash his clothes"; Yoma 68a]')]
        else:
            out += [E_('due_to_priest', 'the-priests', cp=event['sinner'], value=carcass(tier)['v'], law='F2 [Lev 6:19, 6:22 — the male priests within the hangings, by call to the offering engine]'),
                    E_('eating_window', 'the-sin-offering', due=event['day'] + 1, value=OUTER['window']['v'], law='F2 [Mishnah Zevachim 5:3 — a day and a night to midnight: the TIMER]')]
        n_off = aggregate(event['lapses'])['v'] if event.get('lapses') else 1
        out.append(E_('atoned_forgiven', event['sinner'], cp='HEAVEN', amount=n_off, value=atonement(tier)['v'], law='F2 [INK 4:20, 4:26, 4:31, 4:35 "and the priest shall atone for him and he shall be forgiven"; the count by 4:2 "of one of them": %d]' % n_off))
        return out
    if k == 'court_ruled_in_error':
        if event['body'] == 'anointed':
            a = anointed_ruling({'ruling_intent': event['ruling_intent'], 'act_intent': event['act_intent'], 'with_public': event.get('with_public')})
            if 'exempt' in a['fx']:
                return [E_('exempt', 'the-anointed-priest', value=a['v'], law='F3 [Sifra Chovah Chapter 2 1 — a slip without a ruling, or a ruling acted on deliberately]')]
            return [E_('atoned_forgiven', 'the-anointed-priest', cp='HEAVEN', value=a['v'], law='F3 [INK 4:3 "to the guilt of the people" — likened to the congregation]')]
        if event['body'] == 'tribes':
            return [E_('accepted', 'the-tribes', cp='HEAVEN', value=tribes(event['arm'])['v'], law='F3 [Sifra Chovah Section 4 13-17 — the arithmetic by arm]')]
        c = court({'ruling': event.get('ruling', 'partial'), 'composition': event.get('composition', 'all_fit'), 'court_intent': event.get('court_intent', 'unwitting'),
                   'people_intent': event.get('people_intent', 'unwitting'), 'acted': event.get('acted', 'majority'), 'which': event.get('which', 'great'),
                   'matter': event.get('matter', 'karet_class'), 'located': event.get('located', True), 'sin': event.get('sin', 'general')})
        if 'exempt' in c['fx']:
            return [E_('exempt', 'the-court', value=c['v'], law='F3 [INK 4:13 — %s]' % c['why'][:80])]
        if 'accepted' in c['fx']:
            return [E_('accepted', 'the-court', cp='HEAVEN', value=c['v'], law='F3 [Num 15:24 — the bull and the goat]')]
        return [E_('atoned_forgiven', 'the-court' if c['v'] == 'bull' else 'the-individuals', cp='HEAVEN', value=c['v'], law='F3 [INK 4:14 "the assembly shall offer a bull" / 4:27 each his own]')]
    if k == 'acted_on_ruling':
        r = reliance({'knew_error': event.get('knew_error'), 'fit_to_rule': event.get('fit_to_rule'), 'court_retracted': event.get('court_retracted'), 'where': event.get('where')})
        out = []
        if 'exempt' in r['fx']:
            out.append(E_('exempt', event['relier'], value=r['v'], law='F3 [Sifra Chovah Section 7 2 — he relied on the court: its bull covers him]'))
        if 'atoned_forgiven' in r['fx']:
            out.append(E_('atoned_forgiven', event['relier'], cp='HEAVEN', value=r['v'], law='F3 [INK 4:27 "in doing IT" — his own act]'))
        if 'suspends' in r['fx']:
            out.append(E_('suspends', event['relier'], value=r['v'], law='F3 [Sifra Chovah Section 7 3 — R. Eliezer: the doubt, the suspended ram]'))
        return out
    if k == 'sin_became_known':
        if event.get('after_yom_kippur'):
            return [E_('atoned_forgiven', event['sinner'], cp='HEAVEN', value=day_of_atonement('chatat_owed')['v'], law='F6 [INK 4:4 "he shall bring" — even after the Day; Keritot 26a:19]')]
        if event.get('which'):
            ws = which_sin(event['which'])
            if 'exempt' in ws['fx'] and 'atoned_forgiven' not in ws['fx']:
                return [E_('exempt', event['sinner'], value=ws['v'], law='F5 [INK 4:23 "wherein he sinned IN IT"]')]
            return [E_('atoned_forgiven', event['sinner'], cp='HEAVEN', value=ws['v'], law='F5 [Sifra Chovah Chapter 7]')]
        wt = witnesses({'witnesses': event['witnesses']})
        out = []
        if 'atoned_forgiven' in wt['fx']:
            out.append(E_('atoned_forgiven', event['sinner'], cp='HEAVEN', value=wt['v'], law='F5 [INK 4:23 "made KNOWN to him"; Sifra Chovah Chapter 7 2]'))
        if 'suspends' in wt['fx']:
            out.append(E_('suspends', event['sinner'], value=wt['v'], law='F5 [the doubt — CALLED cold_run_vayikra5.sacrilege(doubt)]'))
        if 'exempt' in wt['fx']:
            out.append(E_('exempt', event['sinner'], value=wt['v'], law='F5 [Sifra Chovah Chapter 7 1, 7 3]'))
        return out
    if k == 'doubtful_sin':
        if event.get('stage'):
            r = resolution({'kind': event['doubt_object'], 'stage': event['stage']})
            out = []
            if 'burn_remainder' in r['fx']:
                out.append(E_('burn_remainder', 'the-suspended-ram', value=r['v'], law='F6 [Sifra Chovah Chapter 21 3 at Lev 5:19 — resolved after the slaughter: the flesh burned]'))
            if 'due_to_priest' in r['fx']:
                out.append(E_('due_to_priest', 'the-priests', cp=event['sinner'], value=r['v'], law='F6 [Sifra Chovah Chapter 21 3 — resolved after the sprinkling: the flesh eaten]'))
            return out
        if event.get('on_the_day'):
            return [E_('exempt', event['sinner'], value=day_of_atonement('talui_owed')['v'], law='F6 [Lev 16:30 "from ALL your sins" — the Day clears the doubt; Keritot 26a:19]')]
        p = pieces(event['pieces'][0], event['pieces'][1], event.get('ate', 'one_unknown'), event.get('arm'))
        out = []
        if 'atoned_forgiven' in p['fx']:
            out.append(E_('atoned_forgiven', event['sinner'], cp='HEAVEN', value=p['v'], law='F6 [INK 4:2 — the certain names: a sin offering each (Sifra Chovah Section 5 4)]'))
        if 'suspends' in p['fx']:
            out.append(E_('suspends', event['sinner'], value=p['v'], law='F6 [INK 5:17 "and knew it not" — the doubtful name: the suspended ram, CALLED vayikra5]'))
        if 'accepted' in p['fx']:
            out.append(E_('accepted', event['sinner'], cp='HEAVEN', value=p['v'], law='F6 [Lev 5:15 — the consecrated piece: the certain ram, CALLED vayikra5.sacrilege]'))
        if 'exempt' in p['fx']:
            out.append(E_('exempt', event['sinner'], value=p['v'], law='F6 [Mishnah Keritot 5:4 — two pieces of the profane: exempt]'))
        return out
    if k == 'sin_offering_designated':
        if event.get('source') == 'dead_father' or event.get('for_sin') == 'other':
            o = ownership('dead_father' if event.get('source') == 'dead_father' else 'sin_to_sin')
            return [E_('disqualified', event['owner'], value=o['v'], law='F6 [INK 4:28 "HIS offering on HIS sin"]')]
        if event.get('means_changed') or event.get('blemished'):
            c = conversion(event.get('means_changed') or event.get('blemished'))
            if 'disqualified' in c['fx']:
                return [E_('disqualified', event['owner'], value=c['v'], law='F6 [Lev 27:11 — a bird has no redemption]')]
            return [E_('consecrated', event['owner'], value=c['v'], law='F6 [the rung by his means — CALLED cold_run_vayikra5\'s ladder / Lev 27:11-13]')]
        return [E_('consecrated', event['owner'], value='his_offering_for_his_sin', law='F6 [INK 4:28 "he shall bring his offering... for his sin which he sinned"]')]
    if k == 'priest_ate_holy':
        if event['who'] != 'priest':
            s = share(event['who'])
            if 'barred_from_it' in s['fx']:
                return [E_('barred_from_it', event['eater'], value=s['v'], law='F8 [Lev 10:19 the mourner\'s day; Lev 22:6-7 the immersed]')]
        if event['what'] == 'minchah':
            if event.get('daughters'):
                return []                                        # 10:13 "your due and your SONS' due" — the daughters outside the meal offering's share: the silence
            return [E_('due_to_priest', event['eater'], value=table('minchah_remainder')['v'], law='F9 [INK 10:12 "eat it unleavened beside the altar"]'),
                    E_('most_holy', 'the-meal-offering', law='F9 [INK 10:12 "for it is most holy"]')]
        if event['what'] == 'breast_thigh':
            return [E_('due_to_priest', event['eater'], value=table('daughters')['v'] if event.get('daughters') else table('breast_thigh_due')['v'], law='F9 [INK 10:14 "you and your sons and your daughters"; 10:15 "as the LORD commanded" — CALLED tzav.dues_machine]')]
        return [E_('eaten_to_atone', event['eater'], cp='HEAVEN', value=inquiry('eating_atones')['v'], law='F10 [INK 10:17 "to bear the iniquity of the congregation, to atone for them" — the eating IS the atonement]')]
    if k == 'sin_offering_inquired':
        if event['eater_onen']:
            return [E_('barred_from_it', 'aaron', value=inquiry('high_priest_onen')['v'], law='F10 [INK 10:19 "had I eaten the sin offering today" — offers, does not eat]')]
        if event['blood_inside']:
            return [E_('burned_outside_camp', event['goat'], value=inquiry('blood_inside')['v'], law='F10 [INK 10:18 in its negative; Lev 6:23 — CALLED offerings(inner_chatat_burned)]')]
        return [E_('eaten_to_atone', 'the-priests', cp='HEAVEN', value=inquiry('blood_not_inside')['v'], law='F10 [INK 10:18 "its blood was not brought inside — you should have eaten it in the holy place"]'),
                E_('due_to_priest', 'the-priests', value=inquiry('which_goat_burned')['v'], law='F10 [Sifra Shemini Chapter 2 1-2 — the New Moon\'s goat the burned one; the eighth day\'s eaten]')]
    if k == 'wine_drunk_before_service':
        wv = wine({'who': event['who'], 'drink': event['drink'], 'amount': event['amount'], 'diluted': event.get('diluted'), 'interrupted': event.get('interrupted'), 'act': event['act']})
        if 'death_by_heaven' in wv['fx']:
            return [E_('death_by_heaven', event['who_id'], value=wv['v'], law='F11 [INK 10:9 "that you die not" — the quarter-log the data channel]'),
                    E_('service_profaned', event['who_id'], value=wine_service_validity()['v'], law='F11 [INK 10:10 "to distinguish"; Zevachim 17b:7]')]
        if 'teaching_barred' in wv['fx']:
            return [E_('teaching_barred', event['who_id'], value=wv['v'], law='F11 [INK 10:11 "and to teach"; Keritot 13b]')]
        if 'exempt' in wv['fx']:
            return [E_('exempt', event['who_id'], value=wv['v'], law='F11 [Sifra Shemini Section 1 2 — R. Eliezer: diluted or interrupted]')]
        return []                                                # the Israelite, the profaned priest, less than the measure, no entry: outside the ban's write
    return []

def scene():
    """THE SCENE — Lev 4's and Lev 10's recorded rows replayed on the world engine (clock unit: days)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the sin offering: Keritot 1-6, Horayot 1-3, Zevachim 10-12, Sifra Chovah and Shemini on the engine (clock unit: days)')
        w.laws = [law_chatat]
        w.advance(1)
        base = {'intent': 'unwitting', 'day': 1}
        w.submit({'kind': 'sinned_unwittingly', **base, 'subject': 'the-commoner', 'sinner': 'the-commoner', 'tier': 'commoner', 'species': 'goat', 'case_source': 'Mishnah Horayot 2:6; Zevachim 5:3 — the individual\'s she-goat: outer horns, eaten within the hangings'})
        w.submit({'kind': 'sinned_unwittingly', **base, 'subject': 'the-anointed', 'sinner': 'the-anointed', 'tier': 'anointed', 'case_source': 'Mishnah Horayot 2:6; Zevachim 5:2 — the anointed\'s bull: inside, burned at the ash-pour'})
        w.submit({'kind': 'sinned_unwittingly', **base, 'subject': 'the-deliberate', 'sinner': 'the-deliberate', 'tier': 'commoner', 'intent': 'intentional', 'case_source': 'Mishnah Keritot 1:2 — intentional: karet, no offering'})
        w.submit({'kind': 'sinned_unwittingly', **base, 'subject': 'the-doubter', 'sinner': 'the-doubter', 'tier': 'commoner', 'intent': 'unknown', 'case_source': 'Mishnah Keritot 1:2 — unknown: the suspended ram'})
        w.submit({'kind': 'sinned_unwittingly', **base, 'subject': 'the-gentile', 'sinner': 'the-gentile', 'tier': 'commoner', 'person': 'gentile', 'case_source': 'Sifra Chovah Section 1 1 — gentiles bring none'})
        w.submit({'kind': 'sinned_unwittingly', **base, 'subject': 'the-sleeper', 'sinner': 'the-sleeper', 'tier': 'commoner', 'state': 'asleep', 'case_source': 'Mishnah Keritot 2:6 — the sleeper exempt'})
        w.submit({'kind': 'sinned_unwittingly', **base, 'subject': 'the-twice-lapsed', 'sinner': 'the-twice-lapsed', 'tier': 'commoner', 'species': 'lamb', 'lapses': [['fat'], ['fat']], 'case_source': 'Sifra Chovah Section 5 4-5 — one kind in two lapses: two offerings'})
        w.submit({'kind': 'court_ruled_in_error', 'subject': 'the-court', 'body': 'court', 'case_source': 'Mishnah Horayot 1:1; Lev 4:14 — the court erred in part, the majority acted: the bull'})
        w.submit({'kind': 'court_ruled_in_error', 'subject': 'the-court', 'body': 'court', 'ruling': 'whole', 'case_source': 'Mishnah Horayot 1:3 — to uproot the whole body: exempt'})
        w.submit({'kind': 'court_ruled_in_error', 'subject': 'the-court', 'body': 'court', 'sin': 'idolatry', 'case_source': 'Mishnah Horayot 1:5; Num 15:24 — idolatry: the bull and the goat'})
        w.submit({'kind': 'court_ruled_in_error', 'subject': 'the-tribes', 'body': 'tribes', 'arm': 'R._Shimon', 'case_source': 'Mishnah Horayot 1:5 — R. Shimon: thirteen bulls'})
        w.submit({'kind': 'court_ruled_in_error', 'subject': 'the-anointed-priest', 'body': 'anointed', 'ruling_intent': 'unwitting', 'act_intent': 'unwitting', 'case_source': 'Mishnah Horayot 2:1 — the anointed ruled and acted unwittingly: the bull'})
        w.submit({'kind': 'court_ruled_in_error', 'subject': 'the-anointed-priest', 'body': 'anointed', 'ruling_intent': 'unwitting', 'act_intent': 'intentional', 'case_source': 'Mishnah Horayot 2:1 — acted deliberately on his ruling: exempt'})
        w.submit({'kind': 'acted_on_ruling', 'subject': 'the-relier', 'relier': 'the-relier', 'case_source': 'Mishnah Horayot 1:1 — relied on the court: covered by its bull'})
        w.submit({'kind': 'acted_on_ruling', 'subject': 'the-student', 'relier': 'the-student', 'fit_to_rule': True, 'case_source': 'Mishnah Horayot 1:1 — a student fit to rule: liable'})
        w.submit({'kind': 'acted_on_ruling', 'subject': 'the-overseas', 'relier': 'the-overseas', 'court_retracted': True, 'where': 'overseas', 'case_source': 'Mishnah Horayot 1:2 — went overseas: exempt (ben Azzai)'})
        w.submit({'kind': 'acted_on_ruling', 'subject': 'the-retraction-relier', 'relier': 'the-retraction-relier', 'court_retracted': True, 'case_source': 'Sifra Chovah Section 7 3 — R. Shimon exempt, R. Eliezer the doubt'})
        w.submit({'kind': 'sin_became_known', 'subject': 'the-informed', 'sinner': 'the-informed', 'witnesses': 'two_say_ate_no_denial', 'case_source': 'Mishnah Keritot 3:1 — two say he ate, he does not deny: liable'})
        w.submit({'kind': 'sin_became_known', 'subject': 'the-one-vs-one', 'sinner': 'the-one-vs-one', 'witnesses': 'one_vs_one', 'case_source': 'Mishnah Keritot 3:1 — one against one: the suspended ram'})
        w.submit({'kind': 'sin_became_known', 'subject': 'the-self-denier', 'sinner': 'the-self-denier', 'witnesses': 'one_vs_his_denial', 'case_source': 'Mishnah Keritot 3:1 — one against his denial: exempt'})
        w.submit({'kind': 'sin_became_known', 'subject': 'the-occupied', 'sinner': 'the-occupied', 'witnesses': None, 'which': 'mitasek', 'case_source': 'Mishnah Keritot 4:3 — the occupied one: exempt ("in it")'})
        w.submit({'kind': 'sin_became_known', 'subject': 'the-after-the-day', 'sinner': 'the-after-the-day', 'witnesses': None, 'after_yom_kippur': True, 'case_source': 'Mishnah Keritot 6:4; Keritot 26a — the known sin outlives the Day'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-piece-eater', 'sinner': 'the-piece-eater', 'pieces': ['fat', 'hullin'], 'case_source': 'Mishnah Keritot 4:1 — fat and profane fat, one eaten: the suspended ram'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-both-fat', 'sinner': 'the-both-fat', 'pieces': ['fat', 'fat'], 'case_source': 'Mishnah Keritot 5:4 — two pieces of fat: the sin offering is certain'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-profane-eater', 'sinner': 'the-profane-eater', 'pieces': ['hullin', 'hullin'], 'case_source': 'Mishnah Keritot 5:4 — two profane pieces: exempt'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-consecrated-fat', 'sinner': 'the-consecrated-fat', 'pieces': ['kodesh_fat', 'notar_fat'], 'case_source': 'Mishnah Keritot 5:5-6 — consecrated fat and leftover fat: certain, doubtful, and the sacrilege doubt'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-resolved-after-slaughter', 'sinner': 'the-resolved-after-slaughter', 'pieces': ['fat', 'hullin'], 'doubt_object': 'talui', 'stage': 'after_slaughter', 'case_source': 'Sifra Chovah Chapter 21 3 — resolved after the slaughter: the flesh burned'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-resolved-after-sprinkling', 'sinner': 'the-resolved-after-sprinkling', 'pieces': ['fat', 'hullin'], 'doubt_object': 'talui', 'stage': 'after_zerikah', 'case_source': 'Sifra Chovah Chapter 21 3 — resolved after the sprinkling: the flesh eaten'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-day-doubter', 'sinner': 'the-day-doubter', 'pieces': ['fat', 'hullin'], 'on_the_day': True, 'case_source': 'Mishnah Keritot 6:4 — the Day of Atonement clears the doubt'})
        w.submit({'kind': 'sin_offering_designated', 'subject': 'the-heir', 'owner': 'the-heir', 'source': 'dead_father', 'case_source': 'Mishnah Keritot 6:7 — his dead father\'s beast: no discharge'})
        w.submit({'kind': 'sin_offering_designated', 'subject': 'the-poorer', 'owner': 'the-poorer', 'means_changed': 'became_poor', 'case_source': 'Mishnah Keritot 6:8 — became poor: the birds (CALLED vayikra5)'})
        w.submit({'kind': 'sin_offering_designated', 'subject': 'the-blemished-bird-owner', 'owner': 'the-blemished-bird-owner', 'blemished': 'blemished_bird', 'case_source': 'Mishnah Keritot 6:8 — a bird has no redemption'})
        w.submit({'kind': 'sin_offering_designated', 'subject': 'the-designator', 'owner': 'the-designator', 'case_source': 'Lev 4:28 — his offering for his sin'})
        w.submit({'kind': 'priest_ate_holy', 'subject': 'the-priest-eater', 'eater': 'the-priest-eater', 'who': 'priest', 'what': 'minchah', 'case_source': 'Lev 10:12-13 — the meal offering\'s remainder, unleavened, beside the altar'})
        w.submit({'kind': 'priest_ate_holy', 'subject': 'the-daughter', 'eater': 'the-daughter', 'who': 'priest', 'what': 'breast_thigh', 'daughters': True, 'case_source': 'Lev 10:14 — the daughters in the breast and thigh'})
        w.submit({'kind': 'priest_ate_holy', 'subject': 'the-daughter', 'eater': 'the-daughter', 'who': 'priest', 'what': 'minchah', 'daughters': True, 'case_source': 'Lev 10:13 — the daughters outside the meal offering: the silence'})
        w.submit({'kind': 'priest_ate_holy', 'subject': 'the-onen', 'eater': 'the-onen', 'who': 'onen', 'what': 'chatat', 'case_source': 'Mishnah Zevachim 12:1 — the acute mourner does not share'})
        w.submit({'kind': 'priest_ate_holy', 'subject': 'the-tevul-yom', 'eater': 'the-tevul-yom', 'who': 'tevul_yom', 'what': 'chatat', 'case_source': 'Mishnah Zevachim 12:1 — the immersed-that-day: no share at evening'})
        w.submit({'kind': 'priest_ate_holy', 'subject': 'the-eating-priest', 'eater': 'the-eating-priest', 'who': 'priest', 'what': 'chatat', 'case_source': 'Lev 10:17; Sifra Shemini Chapter 2 4 — the priests eat, the owners are atoned'})
        w.submit({'kind': 'sin_offering_inquired', 'subject': 'the-eighth-days-goat', 'goat': 'the-eighth-days-goat', 'blood_inside': False, 'eater_onen': False, 'case_source': 'Lev 10:16-18; Sifra Shemini Chapter 2 1-2 — outer blood: to be eaten'})
        w.submit({'kind': 'sin_offering_inquired', 'subject': 'the-inner-goat', 'goat': 'the-inner-goat', 'blood_inside': True, 'eater_onen': False, 'case_source': 'Lev 10:18 in its negative; Lev 6:23 — burned'})
        w.submit({'kind': 'sin_offering_inquired', 'subject': 'aaron', 'goat': 'the-new-moon-goat', 'blood_inside': False, 'eater_onen': True, 'case_source': 'Lev 10:19; Mishnah Horayot 3:5 — the acute mourner offers, does not eat'})
        w.submit({'kind': 'wine_drunk_before_service', 'subject': 'the-drunk-priest', 'who_id': 'the-drunk-priest', 'who': 'priest', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'enter_tent', 'case_source': 'Mishnah Keritot 3:3 — a quarter-log and entered: liable'})
        w.submit({'kind': 'wine_drunk_before_service', 'subject': 'the-diluted-drinker', 'who_id': 'the-diluted-drinker', 'who': 'priest', 'drink': 'wine', 'amount': 'quarter_log', 'diluted': True, 'act': 'enter_tent', 'case_source': 'Mishnah Keritot 3:3 — R. Eliezer: diluted, exempt'})
        w.submit({'kind': 'wine_drunk_before_service', 'subject': 'the-drunk-teacher', 'who_id': 'the-drunk-teacher', 'who': 'priest', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'teach', 'case_source': 'Keritot 13b — the drunk may not teach'})
        w.submit({'kind': 'wine_drunk_before_service', 'subject': 'the-israelite', 'who_id': 'the-israelite', 'who': 'israelite', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'rule', 'case_source': 'Sifra Shemini Section 1 6 — an Israelite ruling while drunk: no death (the silence)'})
        w.advance(3)                                                     # the commoner's eating window closes: the timer FIRES
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    amt = lambda eid, eff: sum(e['amount'] or 0 for e in w.entity(eid).ledger if e['effect'] == eff)
    return (n('the-commoner', 'accepted'), n('the-commoner', 'atoned_forgiven'), n('the-priests', 'due_to_priest'), n('the-sin-offering', 'eating_window'), n('the-sin-offering', 'smoked_to_the_lord'),
            n('the-sin-offering', 'burned_outside_camp'), n('the-burner', 'defiles_garments'), n('the-deliberate', 'karet_cut_off'), n('the-doubter', 'suspends'), n('the-gentile', 'exempt'), n('the-sleeper', 'exempt'),
            amt('the-twice-lapsed', 'atoned_forgiven'), n('the-court', 'atoned_forgiven'), n('the-court', 'exempt'), n('the-court', 'accepted'), n('the-tribes', 'accepted'),
            n('the-anointed-priest', 'atoned_forgiven'), n('the-anointed-priest', 'exempt'), n('the-relier', 'exempt'), n('the-student', 'atoned_forgiven'), n('the-overseas', 'exempt'),
            n('the-retraction-relier', 'exempt'), n('the-retraction-relier', 'suspends'), n('the-informed', 'atoned_forgiven'), n('the-one-vs-one', 'suspends'), n('the-self-denier', 'exempt'),
            n('the-occupied', 'exempt'), n('the-after-the-day', 'atoned_forgiven'), n('the-piece-eater', 'suspends'), n('the-both-fat', 'atoned_forgiven'), n('the-profane-eater', 'exempt'),
            n('the-consecrated-fat', 'atoned_forgiven'), n('the-consecrated-fat', 'suspends'), n('the-suspended-ram', 'burn_remainder'), n('the-day-doubter', 'exempt'),
            n('the-heir', 'disqualified'), n('the-poorer', 'consecrated'), n('the-blemished-bird-owner', 'disqualified'), n('the-designator', 'consecrated'),
            n('the-priest-eater', 'due_to_priest'), n('the-meal-offering', 'most_holy'), n('the-daughter', 'due_to_priest'), n('the-onen', 'barred_from_it'), n('the-tevul-yom', 'barred_from_it'), n('the-eating-priest', 'eaten_to_atone'),
            n('the-priests', 'eaten_to_atone'), n('the-inner-goat', 'burned_outside_camp'), n('aaron', 'barred_from_it'),
            n('the-drunk-priest', 'death_by_heaven'), n('the-drunk-priest', 'service_profaned'), n('the-diluted-drinker', 'exempt'), n('the-drunk-teacher', 'teaching_barred'), n('the-israelite', 'death_by_heaven'),
            tset, fired, w.clock.year), w
SCENE, _W = scene()

# ---- (2) TEST DATA — the Mishnah rows, read whole from the shelf ------
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
HOR = load('horayot'); KER = load('keritot'); ZEV = load('zevachim')
def mrow(book, ch, m, must):
    txt = strip({'Horayot': HOR, 'Keritot': KER, 'Zevachim': ZEV}[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Horayot', 1, 1, 'שתלה'), ('Horayot', 1, 2, 'הים'), ('Horayot', 1, 3, 'הגוף'), ('Horayot', 1, 4, 'מפלא'),
    ('Horayot', 1, 5, 'רבן'), ('Horayot', 2, 1, 'לעצמו'), ('Horayot', 2, 3, 'כרת'), ('Horayot', 2, 4, 'שבמקדש'),
    ('Horayot', 2, 5, 'הקול'), ('Horayot', 2, 6, 'ושעירה'), ('Horayot', 2, 7, 'תלוי'), ('Horayot', 3, 1, 'ממשיחותו'),
    ('Horayot', 3, 2, 'כהדיוט'), ('Horayot', 3, 3, 'המלך'), ('Horayot', 3, 4, 'המשחה'), ('Horayot', 3, 5, 'אונן'),
    ('Horayot', 3, 6, 'קודם'),
    ('Keritot', 1, 1, 'ושש'), ('Keritot', 1, 2, 'תלוי'), ('Keritot', 2, 3, 'ויורד'), ('Keritot', 2, 4, 'בנקבה'),
    ('Keritot', 2, 6, 'הישן'), ('Keritot', 3, 1, 'תלוי'), ('Keritot', 3, 2, 'זית'), ('Keritot', 3, 3, 'רביעית'),
    ('Keritot', 3, 4, 'ארבע'), ('Keritot', 3, 5, 'שש'), ('Keritot', 3, 6, 'שלשתן'), ('Keritot', 3, 7, 'שמענו'),
    ('Keritot', 3, 9, 'הלכה'), ('Keritot', 3, 10, 'כשבת'), ('Keritot', 4, 1, 'תלוי'), ('Keritot', 4, 2, 'השמשות'),
    ('Keritot', 4, 3, 'למתעסק'), ('Keritot', 5, 2, 'מעילות'), ('Keritot', 5, 3, 'מנה'), ('Keritot', 5, 4, 'פטור'),
    ('Keritot', 5, 5, 'חטאת'), ('Keritot', 5, 6, 'ודאי'), ('Keritot', 5, 7, 'שתי'), ('Keritot', 5, 8, 'שלש'),
    ('Keritot', 6, 1, 'וירעה'), ('Keritot', 6, 2, 'הנסקל'), ('Keritot', 6, 3, 'חסידים'), ('Keritot', 6, 4, 'מכפר'),
    ('Keritot', 6, 7, 'חטאתו'), ('Keritot', 6, 8, 'פדיון'), ('Keritot', 6, 9, 'שקולין'),
    ('Zevachim', 10, 2, 'קרנות'), ('Zevachim', 10, 4, 'חוטא'), ('Zevachim', 10, 5, 'שקלים'), ('Zevachim', 10, 6, 'אמש'),
    ('Zevachim', 10, 7, 'צלויים'), ('Zevachim', 12, 1, 'אונן'), ('Zevachim', 12, 5, 'הדשן'), ('Zevachim', 12, 6, 'במוטות'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows token-verified in their own ink (Horayot, Keritot, Zevachim 10-12 read '
      'whole — the topic docket)' % len(SHEET))

TESTS = [
 # ---- the domain (Keritot 1:1-2, 2:6, 6:3; Horayot 2:3-4) ----
 ('Keritot 1:2 — intentional: karet, no sin offering', domain({'intent': 'intentional'}), 'karet_no_offering'),
 ('Keritot 1:2 — unwitting: the sin offering', domain({'intent': 'unwitting'}), 'sin_offering'),
 ('Keritot 1:2 — unknown: the suspended ram (CALLED)', domain({'intent': 'unknown'}), 'suspended_ram'),
 ('Keritot 1:2 — the sanctuary-defiler: the sliding scale (CALLED)', domain({'intent': 'unwitting', 'own_offering': 'sliding_scale'}), 'sliding_scale'),
 ('Keritot 1:2 — the blasphemer, no act: the sages exclude', domain({'intent': 'unwitting', 'act': False}), 'no_act_excluded'),
 ('Keritot 1:1 — the criterion: karet when intentional, the sin offering when unwitting', criterion(), 'karet_intentional_chatat_unwitting'),
 ('Keritot 1:1 — the census: thirty-six', karet_census(), 36),
 ('Keritot 2:6 — the minor exempt', domain({'intent': 'unwitting', 'age': 'minor'}), 'exempt'),
 ('Keritot 2:6 — the sleeper exempt', domain({'intent': 'unwitting', 'state': 'asleep'}), 'exempt'),
 ('Horayot 2:3 — a positive commandment: outside', domain({'intent': 'unwitting', 'commandment_kind': 'positive'}), 'positive_outside'),
 ('Horayot 2:4 — the sanctuary\'s impurity class: its own offering', domain({'intent': 'unwitting', 'own_offering': 'sliding_scale'}), 'sliding_scale'),
 ('Horayot 2:4 — the menstruant: inside', domain({'intent': 'unwitting', 'karet_when_intentional': True}), 'sin_offering'),
 ('Horayot 2:3 — not karet-class: outside', domain({'intent': 'unwitting', 'karet_when_intentional': False}), 'not_karet_class_outside'),
 ('Keritot 6:3 — the sages: the suspended ram only for the karet class', talui_scope('sages'), 'karet_class_only'),
 ('Keritot 6:3 — R. Eliezer: any day, the ram of the pious', talui_scope('R._Eliezer'), 'R._Eliezer_any_day'),
 ('Sifra Section 1 1 — gentiles bring none', domain({'intent': 'unwitting', 'person': 'gentile'}), 'gentile_outside'),
 ('Sifra Section 1 5 — the court\'s or king\'s commandments: outside', domain({'intent': 'unwitting', 'law_source': 'court'}), 'not_torah_law_outside'),
 # ---- the rank table (Horayot 2:6, 3:3-3:4, 3:6; Keritot 2:4, 6:9) ----
 ('Horayot 2:6 — the anointed: a bull', rank('anointed'), 'bull'),
 ('Horayot 2:6 — the court: a bull', rank('congregation'), 'bull'),
 ('Horayot 2:6 — the leader: a he-goat', rank('leader'), 'he_goat'),
 ('Horayot 2:6 — the individual: a ewe-lamb or a she-goat', rank('commoner'), 'she_goat_or_ewe_lamb'),
 ('Horayot 2:6 — idolatry, the individual: a she-goat (IMPORT Num 15:27)', rank('commoner', 'idolatry'), 'she_goat'),
 ('Horayot 2:6 — idolatry, the leader: a she-goat', rank('leader', 'idolatry'), 'she_goat'),
 ('Horayot 2:6 — idolatry, the anointed: a she-goat', rank('anointed', 'idolatry'), 'she_goat'),
 ('Horayot 2:6 — idolatry, the court: a bull for olah and a goat for chatat (IMPORT Num 15:24)', rank('congregation', 'idolatry'), 'bull_olah_and_goat_chatat'),
 ('Keritot 2:4 — the individual\'s sin offering is FEMALE', sex('commoner'), 'female'),
 ('Keritot 2:4 — the leader\'s is male', sex('leader'), 'male'),
 ('Keritot 6:9 — lamb and goat equal: "and if a lamb"', lamb_goat(), 'equal_branches'),
 ('Horayot 3:6 — the anointed\'s bull precedes the congregation\'s', precedence_bulls(), 'anointed_first'),
 ('Horayot 3:3 — who is the leader: the king ("his God")', identity('leader'), 'the_king'),
 ('Horayot 3:4 — who is the anointed: with the oil, not the garments', identity('anointed'), 'anointed_with_oil'),
 ('Horayot 3:4 — the only difference: the bull for all the commandments', identity('anointed_vs_garments'), 'the_bull_for_all_commandments'),
 ('Horayot 1:4 — the congregation is the court', identity('congregation'), 'the_court'),
 # ---- the two routes ----
 ('Zevachim 5:1-2 (the consolidation\'s grid) — the anointed\'s blood goes inside', blood('anointed'), 'inside_tent'),
 ('the congregation\'s blood goes inside', blood('congregation'), 'inside_tent'),
 ('the leader\'s blood on the outer altar\'s horns', blood('leader'), 'outer_altar_horns'),
 ('the commoner\'s blood on the outer altar\'s horns', blood('commoner'), 'outer_altar_horns'),
 ('seven sprinklings for the inner tiers', sprinklings('anointed'), 7),
 ('none for the outer', sprinklings('leader'), 0),
 ('Zevachim 12:5 / Lev 6:23 — the inner carcass burned outside the camp', carcass('anointed'), 'burned_outside_camp_ash_pour'),
 ('Zevachim 5:3 — the outer sin offering eaten by the male priests (CALLED)', carcass('commoner'), 'male_priests'),
 ('Zevachim 12:5 — burned as commanded: the ash house, garments defiled', burn_site('as_commanded'), 'ash_house_defiles_garments'),
 ('Zevachim 12:5 — not as commanded: the fortress court, no defiling', burn_site('not_as_commanded'), 'birah_no_defiling'),
 ('Zevachim 12:6 — the first bearers out of the court\'s wall defile', bearers('first_out_of_court'), 'defile_from_first_camp'),
 ('Zevachim 12:6 — the flesh consumed: the burner no longer defiles', bearers('flesh_consumed'), 'no_defiling_after_consumed'),
 ('every tier closes atoned and forgiven', atonement('commoner'), 'atoned_and_forgiven'),
 # ---- the court's error (Horayot 1:1-1:5, 2:1-2:3, 2:5, 2:7) ----
 ('Horayot 1:1 — acted on the court\'s ruling: exempt', reliance({}), 'exempt_relied_on_court'),
 ('Horayot 1:1 — a member who knew they erred: liable', reliance({'knew_error': True}), 'liable'),
 ('Horayot 1:1 — a student fit to rule: liable', reliance({'fit_to_rule': True}), 'liable'),
 ('Horayot 1:2 — the court retracted: R. Shimon exempt, R. Eliezer a doubt', reliance({'court_retracted': True}), 'R._Shimon_exempt_R._Eliezer_doubt'),
 ('Horayot 1:2 — sat at home: liable', reliance({'court_retracted': True, 'where': 'at_home'}), 'liable'),
 ('Horayot 1:2 — went overseas: exempt', reliance({'court_retracted': True, 'where': 'overseas'}), 'exempt'),
 ('Horayot 1:3 — uprooted the whole body: exempt', court({'ruling': 'whole'}), 'exempt'),
 ('Horayot 1:3 — annulled part, kept part: the bull', court({'ruling': 'partial'}), 'bull'),
 ('Horayot 1:4 — one member said "you err": exempt', court({'composition': 'dissent'}), 'exempt'),
 ('Horayot 1:4 — the chief absent: exempt', court({'composition': 'mufla_absent'}), 'exempt'),
 ('Horayot 1:4 — a convert, mamzer, natin, or childless elder on the bench: exempt', court({'composition': 'unfit_member'}), 'exempt'),
 ('Horayot 1:4 — court unwitting, people unwitting: the bull', court({'court_intent': 'unwitting', 'people_intent': 'unwitting'}), 'bull'),
 ('Horayot 1:4 — court intentional, people unwitting: each a lamb or goat', court({'court_intent': 'intentional', 'people_intent': 'unwitting'}), 'individuals_lamb_or_goat'),
 ('Horayot 1:4 — court unwitting, people intentional: exempt', court({'court_intent': 'unwitting', 'people_intent': 'intentional'}), 'exempt'),
 ('Horayot 1:5 — the majority acted: the bull', court({'acted': 'majority'}), 'bull'),
 ('Horayot 1:5 — a minority acted: each their own', court({'acted': 'minority'}), 'individuals_lamb_or_goat'),
 ('Horayot 1:5 — idolatry: a bull and a goat (R. Meir)', court({'sin': 'idolatry'}), 'bull_and_goat'),
 ('Horayot 1:5 — R. Yehuda: twelve bulls', tribes('R._Yehuda'), 'twelve_bulls'),
 ('Horayot 1:5 — R. Shimon: thirteen', tribes('R._Shimon'), 'thirteen_bulls'),
 ('Horayot 1:5 — one tribe\'s court: R. Yehuda that tribe; the sages only the Great Court', court({'which': 'tribal'}), 'R._Yehuda_that_tribe_sages_only_great_court'),
 ('Sifra Section 4 12 — an unlocatable error: no bull', court({'located': False}), 'exempt'),
 ('Horayot 2:1 — the anointed ruled and acted unwittingly: the bull', anointed_ruling({'ruling_intent': 'unwitting', 'act_intent': 'unwitting'}), 'bull'),
 ('Horayot 2:1 — ruled unwittingly, acted deliberately: exempt', anointed_ruling({'ruling_intent': 'unwitting', 'act_intent': 'intentional'}), 'exempt'),
 ('Horayot 2:1 — ruled deliberately, acted unwittingly: exempt', anointed_ruling({'ruling_intent': 'intentional', 'act_intent': 'unwitting'}), 'exempt'),
 ('Horayot 2:2 — ruled with the public, acted with the public: atoned with them', anointed_ruling({'ruling_intent': 'unwitting', 'act_intent': 'unwitting', 'with_public': True}), 'atoned_with_public'),
 ('Sifra Chapter 2 5 — his ruling binds himself only', binds_others(), 'himself_only'),
 ('Horayot 2:5 — the court on hearing of the voice: exempt', sliding_scale_by_tier('court', 'hearing'), 'exempt'),
 ('Horayot 2:5 — the court on sanctuary impurity: exempt', court({'matter': 'sanctuary'}), 'court_exempt'),
 ('Horayot 2:5 — the leader on hearing of the voice: exempt both arms (the king does not testify)', sliding_scale_by_tier('leader', 'hearing'), 'R._Yosei_HaGelili_exempt_R._Akiva_exempt'),
 ('Horayot 2:5 — the leader on utterance: R. Yosei HaGelili exempt, R. Akiva liable', sliding_scale_by_tier('leader', 'utterance'), 'R._Yosei_HaGelili_exempt_R._Akiva_liable'),
 ('Horayot 2:7 — the individual on utterance: the sliding scale (CALLED)', sliding_scale_by_tier('individual', 'utterance'), 'sliding_scale'),
 ('Horayot 2:7 — the high priest on sanctuary impurity: R. Shimon exempt', sliding_scale_by_tier('anointed', 'sanctuary_impurity'), 'R._Shimon_exempt'),
 ('Horayot 2:7 — the suspended ram: the individual liable', talui_by_tier('individual'), 'liable'),
 ('Horayot 2:7 — the suspended ram: the leader liable', talui_by_tier('leader'), 'liable'),
 ('Horayot 2:7 — the suspended ram: the anointed exempt', talui_by_tier('anointed'), 'exempt'),
 ('Horayot 2:7 — the suspended ram: the court exempt', talui_by_tier('court'), 'exempt'),
 ('Horayot 2:7 — the certain ram: the court exempt', vadai_by_tier('court'), 'exempt'),
 ('Horayot 2:7 — the certain ram: the anointed liable', vadai_by_tier('anointed'), 'liable'),
 # ---- timing (Horayot 3:1-3:3) ----
 ('Horayot 3:1 — the anointed sinned then left office: the bull', timing({'tier': 'anointed', 'when': 'sinned_then_removed'}), 'bull'),
 ('Horayot 3:1 — the leader sinned then left: the he-goat', timing({'tier': 'leader', 'when': 'sinned_then_removed'}), 'he_goat'),
 ('Horayot 3:2 — the anointed left office then sinned: the bull', timing({'tier': 'anointed', 'when': 'removed_then_sinned'}), 'bull'),
 ('Horayot 3:2 — the leader left then sinned: as a commoner', timing({'tier': 'leader', 'when': 'removed_then_sinned'}), 'commoner'),
 ('Horayot 3:3 — sinned before appointment: as commoners', timing({'tier': 'leader', 'when': 'sinned_before_appointment'}), 'commoner'),
 ('Horayot 3:3 — R. Shimon: known before — liable; from appointment — exempt', timing({'tier': 'leader', 'when': 'sinned_before_appointment', 'arm': 'R._Shimon'}), 'known_before_liable_known_after_exempt'),
 # ---- the aggregation (Keritot 3:1-3:10, 4:2-4:3) ----
 ('Keritot 3:2 — fat and fat in one lapse: one', aggregate([['fat', 'fat']]), 1),
 ('Keritot 3:2 — fat, blood, leftover, refuse in one lapse: four', aggregate([['fat', 'blood', 'notar', 'piggul']]), 4),
 ('Keritot 3:2 / 4:2 — knowledge between: one for each', aggregate([['fat'], ['fat']]), 2),
 ('Keritot 3:2 — half an olive and half an olive of one kind: liable', half_olive(1), 'liable'),
 ('Keritot 3:2 — of two kinds: exempt', half_olive(2), 'exempt'),
 ('Keritot 3:4 — one eating: four sin offerings and one guilt offering', four_and_one(['impure_eating_holy', 'fat', 'notar', 'consecrated', 'day_of_atonement']), '4 chatat + 1 asham'),
 ('Keritot 3:5 — his daughter: six names, six sin offerings', names_one_act(['daughter', 'sister', 'brothers_wife', 'uncles_wife', 'married_woman', 'niddah']), 6),
 ('Keritot 3:5 — his daughter\'s daughter: seven', names_one_act(['granddaughter', 'daughter_in_law', 'wifes_sister', 'brothers_wife', 'uncles_wife', 'married_woman', 'niddah']), 7),
 ('Keritot 3:6 — his mother-in-law: seven', names_one_act(['mother_in_law', 'daughter_in_law', 'wifes_sister', 'brothers_wife', 'uncles_wife', 'married_woman', 'niddah']), 7),
 ('Keritot 3:6 — R. Yochanan b. Nuri: three names for the mother-in-law alone', names_one_act(['mother_in_law', 'her_mother', 'father_in_laws_mother'], 'R._Yochanan_b._Nuri'), 3),
 ('Keritot 3:6 — the sages: the three are one name', names_one_act(['mother_in_law'], 'sages_one_name'), 'one_name'),
 ('Keritot 3:7 — R. Akiva\'s Emmaus question: OPEN', emmaus('three_sisters_one_lapse'), 'OPEN (we have not heard)'),
 ('Keritot 3:7 — five menstruant wives in one lapse: five', emmaus('five_niddah_wives'), 5),
 ('Keritot 3:9 — five slaughters outside in one lapse: OPEN, with the analogy and its reply', emmaus('five_slaughters_outside'), 'OPEN (we have not heard)'),
 ('Keritot 3:10 — many labors on many Sabbaths of one kind: R. Eliezer each, R. Akiva refutes', emmaus('many_labors_many_sabbaths_one_kind'), 'R._Eliezer_each_R._Akiva_refutes'),
 ('Keritot 3:1 — two said "you ate fat": the sin offering', witnesses({'witnesses': 'two_say_ate_no_denial'}), 'chatat'),
 ('Keritot 3:1 — one says ate, one says not: the suspended ram (CALLED)', witnesses({'witnesses': 'one_vs_one'}), 'talui'),
 ('Keritot 3:1 — one says ate, he says not: exempt', witnesses({'witnesses': 'one_vs_his_denial'}), 'exempt'),
 ('Keritot 3:1 — two say ate, he says not: R. Meir liable, the sages exempt', witnesses({'witnesses': 'two_vs_his_denial'}), 'R._Meir_liable_sages_exempt'),
 ('Keritot 4:3 — "wherein he sinned in it": the occupied one exempt', which_sin('mitasek'), 'exempt'),
 ('Keritot 4:3 — one name: liable, both agree', which_sin('same_name'), 'liable'),
 ('Keritot 4:2 — two names (his wife and his sister): R. Eliezer a sin offering, R. Yehoshua exempt', which_sin('two_names'), 'R._Eliezer_chatat_R._Yehoshua_exempt'),
 ('Keritot 4:2 — at twilight: both agree exempt (R. Yosei)', which_sin('twilight'), 'exempt_both'),
 ('Keritot 4:3 — figs and grapes (R. Yehuda): the same dispute', which_sin('figs_grapes'), 'R._Eliezer_chatat_R._Yehoshua_exempt'),
 # ---- the doubt: the pieces (Keritot 4:1, 5:2-5:8, 6:1-6:4, 6:7-6:8) ----
 ('Keritot 4:1 — doubt whether he ate fat: the suspended ram (CALLED)', pieces('hullin', 'fat'), 'talui'),
 ('Keritot 5:2 — doubtful sacrilege: R. Akiva the ram, the sages exempt (CALLED)', pieces('hullin', 'kodesh'), 'R._Akiva_talui_sages_exempt'),
 ('Keritot 5:4 — common and consecrated, ate the second: the certain ram', pieces('hullin', 'kodesh', 'both'), 'asham_vadai'),
 ('Keritot 5:5 — common and fat, ate the second: a sin offering', pieces('hullin', 'fat', 'both'), 'chatat'),
 ('Keritot 5:6 — fat and consecrated, one unknown: the suspended ram', pieces('fat', 'kodesh'), 'talui + R._Akiva_talui_sages_exempt'),
 ('Keritot 5:6 — fat and consecrated, the second: a sin offering and a certain ram', pieces('fat', 'kodesh', 'both'), 'chatat + asham_vadai'),
 ('Keritot 5:7 — fat and consecrated fat, one unknown: a sin offering (R. Akiva adds the ram)', pieces('fat', 'kodesh_fat'), 'chatat + R._Akiva_talui_sages_exempt'),
 ('Keritot 5:7 — the second: two sin offerings and a certain ram', pieces('fat', 'kodesh_fat', 'both'), 'chatat + chatat + asham_vadai'),
 ('Keritot 5:8 — fat and leftover fat, one unknown: a sin offering and the suspended ram', pieces('fat', 'notar_fat'), 'chatat + talui'),
 ('Keritot 5:8 — the second: three sin offerings', pieces('fat', 'notar_fat', 'both'), 'chatat + chatat + chatat'),
 ('Keritot 5:5 — two persons, common and fat: each the suspended ram', pieces('hullin', 'fat', 'two_persons'), 'each: talui'),
 ('Keritot 5:5 — R. Shimon: both bring one sin offering', pieces('hullin', 'fat', 'two_persons', 'R._Shimon'), 'each_talui; together one chatat'),
 ('Keritot 5:8 — R. Yosei: two never bring one sin offering', pieces('fat', 'notar_fat', 'two_persons', 'R._Yosei'), 'each; never two for one'),
 ('Keritot 5:3 — R. Akiva concedes on a small sacrilege', cell('R._Akiva_concedes', M, SC + 'Section 12 2 — on a hundred-maneh doubt he prefers the two-sela ram', [FX.NONE]), 'R._Akiva_concedes'),
 ('Keritot 6:1 — learned before slaughter that he had not sinned: three arms', resolution({'kind': 'talui', 'stage': 'before_slaughter'}), 'R._Meir_pasture_sages_blemish_sell_R._Eliezer_offer'),
 ('Keritot 6:1 — after slaughter: the blood poured, the flesh burned', resolution({'kind': 'talui', 'stage': 'after_slaughter'}), 'blood_poured_flesh_burned'),
 ('Keritot 6:1 — the blood thrown: the flesh eaten', resolution({'kind': 'talui', 'stage': 'after_zerikah'}), 'flesh_eaten'),
 ('Keritot 6:2 — the certain ram after slaughter: buried', resolution({'kind': 'vadai', 'stage': 'after_slaughter'}), 'buried'),
 ('Keritot 6:2 — the certain ram, blood thrown: the flesh burned', resolution({'kind': 'vadai', 'stage': 'after_zerikah'}), 'flesh_burned'),
 ('Keritot 6:2 — the stoned ox after stoning: benefit permitted (IMPORT Exod 21:28)', resolution({'kind': 'stoned_ox', 'stage': 'after_stoning'}), 'benefit_permitted'),
 ('Keritot 6:4 — a sin offering owed over the Day of Atonement: bring after', day_of_atonement('chatat_owed'), 'bring_after'),
 ('Keritot 6:4 — a suspended ram owed: exempt', day_of_atonement('talui_owed'), 'exempt'),
 ('Keritot 6:4 — a doubt on the Day itself, even at dusk: exempt', day_of_atonement('doubt_on_the_day'), 'exempt'),
 ('Keritot 6:7 — the dead father\'s sin offering: no discharge', ownership('dead_father'), 'no_discharge'),
 ('Keritot 6:7 — from sin to sin: no discharge', ownership('sin_to_sin'), 'no_discharge'),
 ('Keritot 6:8 — became poor: birds (CALLED)', conversion('became_poor'), 'birds'),
 ('Keritot 6:8 — became poorer: the tenth of the ephah (CALLED)', conversion('became_poorer'), 'flour'),
 ('Keritot 6:8 — became rich: a lamb or goat (CALLED)', conversion('became_rich'), 'lamb_or_goat'),
 ('Keritot 6:8 — a blemished lamb: a bird from its price', conversion('blemished_lamb'), 'bird_from_its_price'),
 ('Keritot 6:8 — a blemished bird: no flour from its price', conversion('blemished_bird'), 'no_flour_from_its_price'),
 # ---- precedence (Zevachim 10:2-10:7) ----
 ('Zevachim 10:2 — the sin offering\'s blood before the burnt offering\'s: it propitiates', precedence('chatat_blood_vs_olah_blood'), 'chatat_blood_first'),
 ('Zevachim 10:2 — the burnt offering\'s limbs before the sin offering\'s innards', precedence('olah_limbs_vs_chatat_innards'), 'olah_limbs_first'),
 ('Zevachim 10:2 — the sin offering before the guilt offering: four horns and the base', precedence('chatat_vs_asham'), 'chatat_first'),
 ('Zevachim 10:2 — the guilt offering before the thanksgiving', precedence('asham_vs_todah'), 'asham_first'),
 ('Zevachim 10:2 — the thanksgiving before the peace offerings', precedence('todah_vs_shelamim'), 'todah_first'),
 ('Zevachim 10:2 — the peace offerings before the firstborn', precedence('shelamim_vs_bekhor'), 'shelamim_first'),
 ('Zevachim 10:5 — all sin offerings precede guilt offerings except the leper\'s', precedence('chatat_vs_asham_all'), 'chatat_first_except_leper'),
 ('Zevachim 10:5 — guilt offerings two years old at silver shekels (CALLED)', precedence('asham_age_price'), 'two_years_silver_shekels'),
 ('Zevachim 10:5 — the nazirite\'s and the leper\'s: yearlings, no shekels', precedence('nazir_leper_asham'), 'yearlings_no_shekels'),
 ('Zevachim 10:4 — the bird sin offering before the bird burnt offering (CALLED)', precedence('bird_chatat_vs_bird_olah'), 'chatat_first'),
 ('Zevachim 10:4 — the sinner\'s meal offering before the voluntary (CALLED)', precedence('sinner_minchah_vs_voluntary'), 'sinner_first'),
 ('Zevachim 10:6 — yesterday\'s peace offerings against today\'s sin offering: R. Meir / the sages', precedence('yesterday_shelamim_vs_today_chatat'), 'R._Meir_shelamim_sages_chatat'),
 ('Zevachim 10:7 — the manner of eating: roasted, boiled, cooked', precedence('eating_manner'), 'roasted_boiled_cooked'),
 # ---- the share (Zevachim 12:1) and the priest's table (10:12-15) ----
 ('Zevachim 12:1 / Horayot 3:5 — the acute mourner touches, does not offer, does not share', share('onen'), 'touches_not_offers_not_shares'),
 ('Zevachim 12:1 — the blemished share and eat, do not offer (IMPORT Lev 21:22)', share('blemished'), 'shares_and_eats_not_offers'),
 ('Zevachim 12:1 — the immersed-that-day: no share at evening', share('tevul_yom'), 'no_share_at_evening'),
 ('Zevachim 12:1 — impure at the blood-throwing: no share (Lev 7:33 quoted)', share('impure_at_zerikah'), 'no_share'),
 ('Lev 10:12 — the meal offering\'s remainder: unleavened beside the altar, most holy (CALLED)', table('minchah_remainder'), 'unleavened_beside_altar_most_holy'),
 ('Lev 10:13 — in a HOLY place', table('minchah_place'), 'holy_place'),
 ('Lev 10:14 — the breast and thigh in a PURE place', table('breast_thigh_place'), 'pure_place'),
 ('Sifra Shemini Chapter 1 9 — the pure place: inside Jerusalem', table('pure_place_is'), 'inside_jerusalem'),
 ('Lev 10:14 — the daughters eat the breast and thigh, not the meal offering', table('daughters'), 'daughters_eat_breast_thigh_not_minchah'),
 ('Lev 10:15 — the fats below at the carrying', table('fats_position'), 'fats_below'),
 # ---- the inquiry (10:16-20) ----
 ('Lev 10:18 — the blood not brought inside: eaten in the holy place', inquiry('blood_not_inside'), 'eaten_in_holy_place'),
 ('Lev 6:23 — the blood brought inside: burned', inquiry('blood_inside'), 'burned'),
 ('Lev 10:17 — the priests eat and the owners are atoned', inquiry('eating_atones'), 'priests_eat_owners_atoned'),
 ('Sifra Shemini Chapter 2 1-2 — which goat was burned: the New Moon\'s', inquiry('which_goat_burned'), 'new_moon_goat'),
 ('Sifra Shemini Chapter 2 8, 2 10 — why burned: mourning / impurity', inquiry('why_burned'), 'R._Nechemia_mourning_R._Yehuda_R._Shimon_impurity'),
 ('Horayot 3:5 — the high priest offers as an acute mourner and does not eat', inquiry('high_priest_onen'), 'offers_not_eats'),
 ('Sifra Shemini Chapter 2 11 — the mourner\'s day and night', inquiry('mourner_day_night'), 'day_torah_night_R._Yehuda_torah_Rabbi_scribes'),
 ('Lev 10:20 — Moses admitted at once', inquiry('moses_admitted'), 'admitted_at_once'),
 # ---- the wine ban (10:9-11) ----
 ('Keritot 3:3 — a quarter-log of wine and entered the sanctuary: liable', wine({'who': 'priest', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'enter_tent'}), 'liable_death'),
 ('Keritot 3:3 — R. Eliezer: interrupted or watered: exempt', wine({'who': 'priest', 'drink': 'wine', 'amount': 'quarter_log', 'diluted': True, 'act': 'enter_tent'}), 'R._Eliezer_exempt'),
 ('Sifra Shemini Section 1 1 — less than the measure: warned, not death', wine({'who': 'priest', 'drink': 'wine', 'amount': 'less', 'act': 'enter_tent'}), 'warned_not_death'),
 ('Sifra Shemini Section 1 2 — R. Yehuda: other intoxicants a warning', wine({'who': 'priest', 'drink': 'other_intoxicant', 'amount': 'quarter_log', 'act': 'serve'}), 'R._Yehuda_warning_not_death'),
 ('Sifra Shemini Section 1 3 — the profaned priest outside the ban', wine({'who': 'profaned_priest', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'serve'}), 'outside_the_ban'),
 ('Sifra Shemini Section 1 6 — an Israelite ruling while drunk: no death', wine({'who': 'israelite', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'rule'}), 'no_death'),
 ('Lev 10:9 — no entry, no ban', wine({'who': 'priest', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'none'}), 'no_ban'),
 ('Sifra Shemini Section 1 8 / Zevachim 17b — a drunk priest\'s service: invalid', wine_service_validity(), 'service_invalid'),
 ('Keritot 13b — the drunk may not teach', wine({'who': 'priest', 'drink': 'wine', 'amount': 'quarter_log', 'act': 'teach'}), 'teaching_barred'),
 ('Sanhedrin 22b — the ban today: Rabbi forbids forever, its remedy is its ruin', wine_today(), 'Rabbi_forbidden_forever_remedy_is_ruin'),
 ('Sanhedrin 22b — a mil\'s walk and sleep dissipate a quarter-log, not more', wine_dissipation(), 'quarter_log_dissipates_more_does_not'),
 ('Sifra Shemini Section 1 9 — the curriculum verse', curriculum(), 'valuations_purity_rulings_expositions_halachot_scripture'),
 # ---- THE POINTERS RESOLVED BY LIVE CALL (2026-09-06, the dependency-debt sitting) ----
 ('the four "as the fat of the peace offering" pointer verses censused', fat('pointer_census'), [10, 26, 31, 35]),
 ('Lev 4:10 — the anointed priest\'s bull: the OX\'s inventory, no tail (CALLED offerings fat:ox)', fat('anointed'), 'ox_inventory_no_tail'),
 ('Lev 4:20 — the congregation\'s bull "as the bull of the sin offering": the ox\'s again', fat('congregation'), 'ox_inventory_no_tail'),
 ('Lev 4:26 — the leader\'s he-goat "as the fat of the peace offering": the goat\'s, no tail', fat('leader'), 'goat_inventory_no_tail'),
 ('Lev 4:31 — the commoner\'s she-goat: the goat\'s, no tail', fat('commoner', species='goat'), 'goat_inventory_no_tail'),
 ('Lev 4:35 — the commoner\'s ewe "as the fat of the LAMB is removed": TAIL INCLUDED (Tamid 4:3)', fat('commoner', species='lamb'), 'lamb_inventory_tail_included'),
 ('Lev 10:15 "as the LORD commanded" — the breast and thigh by call into the Tzav engine', table('breast_thigh_due'), 'to_the_priests_after_smoking'),
 # ---- THE WRAP (W3, 2026-09-07) — the sin offering on the world engine ----
 ('THE SCENE — (the commoner accepted, atoned; four dues; two windows; three fats; the anointed\'s bull burned, the burner\'s garments; the '
  'deliberate\'s karet, the doubter\'s ram, the gentile and the sleeper exempt; the twice-lapsed\'s TWO; the court\'s bull, its whole-body '
  'exemption, its idolatry pair, R. Shimon\'s thirteen; the anointed\'s bull and his exemption; the relier, the student, the overseas, the '
  'retraction\'s two arms; the informed, one against one, the self-denier, the occupied, after the Day; the pieces: the doubtful, the certain, '
  'the profane, the consecrated pair\'s two; the ram burned after the slaughter, the Day\'s clearing; the heir, the poorer, the bird, the '
  'designator; the priest\'s table, most holy, the daughter\'s breast and thigh, the mourner and the immersed barred, the eating that atones; '
  'the eighth day\'s goat eaten, the inner goat burned, Aaron barred; the drunk priest\'s death and profaned service, the diluted exempt, the '
  'teacher barred, the Israelite\'s silence; timers set, fired, the clock)',
  cell(SCENE, I, 'THE SCENE on the world engine: Keritot 1-6, Horayot 1-3, Zevachim 10-12 and Sifra Chovah and Shemini replayed on law_chatat — '
       'the domain, the rank, the two routes, the court, the reliance, the knowledge, the pieces and the resolution, the designation, the table, '
       'the inquiry, the wine; every value the daemon\'s by call into this file\'s own cells', ['atoned_forgiven', 'exempt', 'karet_cut_off',
       'suspends', 'accepted', 'smoked_to_the_lord', 'burned_outside_camp', 'defiles_garments', 'due_to_priest', 'eating_window', 'disqualified',
       'consecrated', 'most_holy', 'barred_from_it', 'eaten_to_atone', 'burn_remainder', 'death_by_heaven', 'service_profaned', 'teaching_barred']),
  (1, 1, 4, 2, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 3)),
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
print('SCENE: %r — the daemon\'s watch coverage:' % (SCENE,))
_W.print_coverage()
print('effects: every cell carries REGISTERED effects — six discovered in these spans\' own verbs: '
      'burned_outside_camp (DESTROY), defiles_garments (STATUS), eaten_to_atone, death_by_heaven (HEAVEN), '
      'service_profaned, teaching_barred (BLOCK) [effects law satisfied]')
if ok == n:
    print('THE SIN OFFERING RANK TREE AND THE PRIEST\'S TABLE COMPILE — the four tiers by their own tokens, the '
          'one tier carrying "his God", the two inner routes counted, five horns and five bases, the domain '
          'phrase at five seats across two chapters, the acute mourner\'s day, the wine ban\'s two jobs; the '
          'Lev 5 engine, the offering engine, and the meal-offering engine CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')
