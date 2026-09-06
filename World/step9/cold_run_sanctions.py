#!/usr/bin/env python3
"""cold_run_sanctions.py — BLOOD, UNIONS, AND SANCTIONS
(2026-09-05, sitting L3 of THE COMPILE DEBT — World/step9/COMPILE_DEBT.md).

Spans: Lev 17:1-16 (outside slaughter and raising, the blood ban and
its atonement clause, the covering, the carcass-eater), Lev 18:1-30
(the frame, the forbidden unions as a kinship list, Molech, the land
that vomits), Lev 20:1-27 (Molech and the ghost-pit, the curser, the
sanctions of the unions by mode, the separation of species).

Answer sheet ROUTED BY TOPIC under the union rule: Mishnah Sanhedrin
7, 9, 11 whole, Makkot 3 whole, Yevamot 1-3 whole, Chullin 6 whole,
Zevachim 13-14 whole, Keritot 1 whole — 95 rows read whole plus the 10
link rows outside them (the ledger logic/oral_triage/sanctions_topic_
docket_2026-09-05.md, coverage computed; 461 Talmud addresses indexed,
opened per gap).

The five motions, in order:
 (1) code from the BARE INK — the sanction tokens censused across
     Lev 20 (stoning named at two seats, burning at one, 'their blood
     is upon them' at six, the bare 'shall be put to death' at nine,
     the cutting-off at ten across the three chapters, 'childless' at
     two, the set face at four); each union LOCATED by its own kinship
     token in Lev 18 (the warning) and Lev 20 (the sanction); the
     kinship list COMPOSED with 'his paternal brother' to compute the
     levirate table; the covering's two nouns and its dust; the two
     outside clauses with their two karet formulas; every quantity a
     PARAMETER (the olive, the appearance of blood, the eras' dates);
 (2) the Mishnah's rows as TEST DATA, each expected value a literal
     typed from the row (the honest-pairing guard runs first);
 (3) run;
 (4) misses filled by NAMED recorded arguments — the Sifra's rows
     (the units' spines, verdicted 2026-09-05) and the Talmud where
     opened, each labeled [MOVE];
 (5) the graded matrix with per-cell provenance, fractions, and EFFECTS
     on every verdict.

Cross-span receipts, labeled [IMPORT] and, where a compiled callee
exists, CALLED: cold_run_chatat (the unwitting union's sin offering
by the karet-class domain; the doubt's suspended ram); cold_run_clocks
(the zav's pair on the eighth day — 'lacking time in its owner');
cold_run_shemini (the pure and impure beast for 20:25's separation);
Deut 25:5 (the brother not in his world; the levirate window), Deut
18:10 (through fire), Lev 24:16 (the Name), Lev 19:31 (the consulter's
warning), Exod 22:18 (the passive's warning), Deut 12:9 (rest and
inheritance — the platform eras).
"""
import sqlite3, sys, os, json, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
from compile_guards import check_honest_pairing
GUARDED = check_honest_pairing(os.path.abspath(__file__))
assert GUARDED == 241, ("the guard counted %d expectations, the tripwire holds 241" % GUARDED)

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def toks(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=?
        ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return [strip(r[0]) for r in rows]

def nverses(book, ch):
    return db.execute("SELECT COUNT(*) FROM verses WHERE book=? AND chapter=?", (book, ch)).fetchone()[0]

def phrase(book, ch, vs, words):
    t = toks(book, ch, vs); n = len(words)
    return sum(1 for i in range(len(t) - n + 1) if t[i:i + n] == words)

SPAN = [(17, v) for v in range(1, nverses('Lev', 17) + 1)] + [(18, v) for v in range(1, nverses('Lev', 18) + 1)] + \
       [(20, v) for v in range(1, nverses('Lev', 20) + 1)]
assert len(SPAN) == 16 + 30 + 27, len(SPAN)

def seats(pred):
    return [(c, v) for (c, v) in SPAN if pred(toks('Lev', c, v))]
def has(*ws):
    return lambda t: any(t[i:i + len(ws)] == list(ws) for i in range(len(t) - len(ws) + 1))
def anytok(*ws):
    return lambda t: any(w in t for w in ws)

# ---- (1) ink probes — each MUST fire or the run refuses -------------
PROBES = [
    ('any man who SLAUGHTERS',                      'Lev', 17, 3, 'ישחט'),
    ('in the camp or outside the camp',             'Lev', 17, 3, 'למחנה'),
    ('to the TENT DOOR he did not bring it',        'Lev', 17, 4, 'הביאו'),
    ('BLOOD shall be reckoned to that man',         'Lev', 17, 4, 'יחשב'),
    ('blood he has SHED',                           'Lev', 17, 4, 'שפך'),
    ('that man shall be CUT OFF',                   'Lev', 17, 4, 'ונכרת'),
    ('on the open FIELD',                           'Lev', 17, 5, 'השדה'),
    ('a pleasing FRAGRANCE',                        'Lev', 17, 6, 'ניחח'),
    ('to the HAIRY ONES (the demons)',              'Lev', 17, 7, 'לשעירם'),
    ('an ETERNAL statute',                          'Lev', 17, 7, 'עולם'),
    ('who RAISES a burnt offering or sacrifice',    'Lev', 17, 8, 'יעלה'),
    ('to PERFORM it to the LORD',                   'Lev', 17, 9, 'לעשות'),
    ('who eats ANY blood',                          'Lev', 17, 10, 'דם'),
    ('I will set My FACE',                          'Lev', 17, 10, 'פני'),
    ('the LIFE of the flesh is in the blood',       'Lev', 17, 11, 'נפש'),
    ('on the ALTAR to atone',                       'Lev', 17, 11, 'המזבח'),
    ('who HUNTS a catch',                           'Lev', 17, 13, 'יצוד'),
    ('WILD ANIMAL or bird',                         'Lev', 17, 13, 'חיה'),
    ('and COVER it',                                'Lev', 17, 13, 'וכסהו'),
    ('with DUST',                                   'Lev', 17, 13, 'בעפר'),
    ('all who eat it shall be cut off',             'Lev', 17, 14, 'יכרת'),
    ('CARCASS and torn',                            'Lev', 17, 15, 'נבלה'),
    ('citizen and CONVERT',                         'Lev', 17, 15, 'ובגר'),
    ('he shall BEAR his iniquity',                  'Lev', 17, 16, 'ונשא'),
    ('as the deeds of the land of EGYPT',           'Lev', 18, 3, 'מצרים'),
    ('in their STATUTES you shall not walk',        'Lev', 18, 3, 'ובחקתיהם'),
    ('and LIVE by them',                            'Lev', 18, 5, 'וחי'),
    ('to all NEAR FLESH you shall not approach',    'Lev', 18, 6, 'שאר'),
    ('your FATHER\'S nakedness',                    'Lev', 18, 7, 'אביך'),
    ('your father\'s WIFE',                         'Lev', 18, 8, 'אשת'),
    ('your SISTER, your father\'s or mother\'s daughter', 'Lev', 18, 9, 'אחותך'),
    ('your son\'s daughter',                        'Lev', 18, 10, 'בנך'),
    ('for they are YOURS (henah)',                  'Lev', 18, 10, 'הנה'),
    ('your father\'s wife\'s daughter, BORN OF your father', 'Lev', 18, 11, 'מולדת'),
    ('your father\'s sister',                       'Lev', 18, 12, 'אחות'),
    ('your mother\'s sister',                       'Lev', 18, 13, 'אמך'),
    ('your father\'s brother... his wife, your AUNT', 'Lev', 18, 14, 'דדתך'),
    ('your DAUGHTER-IN-LAW',                        'Lev', 18, 15, 'כלתך'),
    ('your brother\'s wife',                        'Lev', 18, 16, 'אחיך'),
    ('a woman AND HER DAUGHTER',                    'Lev', 18, 17, 'ובתה'),
    ('it is ZIMAH (a scheme)',                      'Lev', 18, 17, 'זמה'),
    ('a woman to her SISTER',                       'Lev', 18, 18, 'אחתה'),
    ('in her LIFETIME',                             'Lev', 18, 18, 'בחייה'),
    ('in the separation of her impurity',           'Lev', 18, 19, 'בנדת'),
    ('your FELLOW\'s wife',                         'Lev', 18, 20, 'עמיתך'),
    ('to PASS to Molech',                           'Lev', 18, 21, 'להעביר'),
    ('a MALE, the lyings of a woman',               'Lev', 18, 22, 'זכר'),
    ('any BEAST',                                   'Lev', 18, 23, 'בהמה'),
    ('the land VOMITED its inhabitants',            'Lev', 18, 25, 'ותקא'),
    ('the SOULS that do shall be cut off',          'Lev', 18, 29, 'ונכרתו'),
    ('keep My CHARGE',                              'Lev', 18, 30, 'משמרתי'),
    ('the people of the land shall STONE him',      'Lev', 20, 2, 'ירגמהו'),
    ('with STONE',                                  'Lev', 20, 2, 'באבן'),
    ('if they HIDE their eyes',                     'Lev', 20, 4, 'יעלימו'),
    ('against his FAMILY',                          'Lev', 20, 5, 'ובמשפחתו'),
    ('who turns to the GHOST-PITS',                 'Lev', 20, 6, 'האבת'),
    ('who CURSES his father and his mother',        'Lev', 20, 9, 'יקלל'),
    ('his blood is upon him',                       'Lev', 20, 9, 'דמיו'),
    ('the ADULTERER and the adulteress',            'Lev', 20, 10, 'הנאף'),
    ('their blood is upon them',                    'Lev', 20, 11, 'דמיהם'),
    ('in FIRE they shall burn',                     'Lev', 20, 14, 'ישרפו'),
    ('the beast you shall KILL',                    'Lev', 20, 15, 'תהרגו'),
    ('it is CHESED (the homonym)',                  'Lev', 20, 17, 'חסד'),
    ('CHILDLESS they shall die',                    'Lev', 20, 20, 'ערירים'),
    ('she is NIDDAH (set apart)',                   'Lev', 20, 21, 'נדה'),
    ('SEPARATE between the pure beast and the impure', 'Lev', 20, 25, 'והבדלתם'),
    ('a ghost-pit or familiar in them',             'Lev', 20, 27, 'אוב'),
]
missing = [p for p in PROBES if p[4] not in toks(p[1], p[2], p[3])]
if missing:
    for p in missing: print('PROBE FAILED:', p)
    sys.exit('zero-report law: the ink scan is not trusted until every probe fires')
print('probes: %d/%d fired (the ink scan is trusted)' % (len(PROBES), len(PROBES)))

# ---- the censuses (TRIPWIRES — each a measured literal) ------------
c_formula_pl = seats(has('דמיהם', 'בם'))
assert c_formula_pl == [(20, 11), (20, 12), (20, 13), (20, 16), (20, 27)], c_formula_pl
c_formula_sg = seats(has('דמיו', 'בו'))
assert c_formula_sg == [(20, 9)], c_formula_sg
c_stone = seats(anytok('ירגמהו', 'ירגמו'))
assert c_stone == [(20, 2), (20, 27)], c_stone
assert seats(anytok('באבן')) == c_stone
c_burn = seats(has('באש', 'ישרפו'))
assert c_burn == [(20, 14)], c_burn
c_mot = seats(lambda t: any(t[i] == 'מות' and t[i + 1] in ('יומת', 'יומתו') for i in range(len(t) - 1)))
assert c_mot == [(20, 2), (20, 9), (20, 10), (20, 11), (20, 12), (20, 13), (20, 15), (20, 16), (20, 27)], c_mot
c_karet = seats(lambda t: any('כרת' in w for w in t))
assert c_karet == [(17, 4), (17, 9), (17, 10), (17, 14), (18, 29), (20, 3), (20, 5), (20, 6), (20, 17), (20, 18)], c_karet
c_ariri = seats(anytok('ערירים'))
assert c_ariri == [(20, 20), (20, 21)], c_ariri
c_bear = seats(anytok('ונשא', 'ישא', 'ישאו'))
assert c_bear == [(17, 16), (20, 17), (20, 19), (20, 20)], c_bear
c_face = seats(lambda t: 'פני' in t and any(w in t for w in ('ונתתי', 'אתן', 'ושמתי')))
assert c_face == [(17, 10), (20, 3), (20, 5), (20, 6)], c_face
c_zimah = seats(anytok('זמה'))
assert c_zimah == [(18, 17), (20, 14)], c_zimah
c_zimah_19 = 'זמה' in toks('Lev', 19, 29)     # the harlot-daughter clause outside the span, noted
c_henah = seats(anytok('הנה'))
assert c_henah == [(18, 10), (18, 17)], c_henah
c_tegaleh = seats(has('לא', 'תגלה'))
assert c_tegaleh == [(18, v) for v in range(7, 18)] + [(20, 19)], c_tegaleh
c_tikrav = seats(anytok('תקרב', 'תקרבו'))
assert c_tikrav == [(18, 6), (18, 14), (18, 19), (20, 16)], c_tikrav
c_toevah = seats(anytok('תועבה')); c_tevel = seats(anytok('תבל'))
assert c_toevah == [(18, 22), (20, 13)] and c_tevel == [(18, 23), (20, 12)], (c_toevah, c_tevel)
c_tent = seats(has('פתח', 'אהל', 'מועד'))
assert c_tent == [(17, 4), (17, 5), (17, 6), (17, 9)], c_tent
c_ish_ish = seats(has('איש', 'איש'))
assert c_ish_ish == [(17, 3), (17, 8), (18, 6), (20, 2), (20, 9)], c_ish_ish
c_ger = seats(anytok('הגר', 'ובגר'))
assert c_ger == [(17, 8), (17, 10), (17, 12), (17, 13), (17, 15), (18, 26), (20, 2)], c_ger
c_vomit = seats(anytok('ותקא', 'תקיא', 'קאה'))
assert c_vomit == [(18, 25), (18, 28), (20, 22)], c_vomit
c_niddah = seats(anytok('נדה', 'בנדת', 'דוה'))
assert c_niddah == [(18, 19), (20, 18), (20, 21)], c_niddah
c_molech = seats(anytok('למלך'))
assert c_molech == [(18, 21), (20, 2), (20, 3), (20, 4)], c_molech
c_seed = seats(anytok('מזרעו', 'ומזרעך'))
assert c_seed == c_molech, c_seed
c_ov = seats(anytok('האבת', 'אוב'))
assert c_ov == [(20, 6), (20, 27)], c_ov
c_veish = seats(has('ואיש', 'אשר')); c_veishah = seats(has('ואשה', 'אשר'))
assert len(c_veish) == 10 and c_veishah == [(20, 16)], (c_veish, c_veishah)
c_lYHWH17 = {v: toks('Lev', 17, v).count('ליהוה') for v in range(1, 17) if 'ליהוה' in toks('Lev', 17, v)}
assert c_lYHWH17 == {4: 1, 5: 2, 6: 1, 9: 1}, c_lYHWH17
c_cover = (phrase('Lev', 17, 13, ['חיה', 'או', 'עוף']), 'בעפר' in toks('Lev', 17, 13), 'וכסהו' in toks('Lev', 17, 13),
           'בהמה' in toks('Lev', 17, 13))
assert c_cover == (1, True, True, False), c_cover
c_two_clauses = (seats(anytok('ישחט')), seats(anytok('יעלה')))
assert c_two_clauses == ([(17, 3)], [(17, 8)]), c_two_clauses
c_nefesh17 = {v: sum(1 for w in toks('Lev', 17, v) if 'נפש' in w) for v in (10, 11, 12, 14, 15)}
assert c_nefesh17 == {10: 1, 11: 3, 12: 1, 14: 3, 15: 1}, c_nefesh17
c_do = (('יעשה' in toks('Lev', 18, 5)) and ('וחי' in toks('Lev', 18, 5)),
        ('יעשה' in toks('Lev', 18, 29)) and ('העשת' in toks('Lev', 18, 29)))
assert c_do == (True, True), c_do
c_1517 = ('אחתו' in toks('Lev', 20, 17), phrase('Lev', 20, 17, ['בת', 'אביו', 'או', 'בת', 'אמו']))
assert c_1517 == (True, 1), c_1517
print('censuses: the formula "their blood is upon them" at %s + "his blood" at %s · stoning NAMED at %s · burning at %s · '
      'bare "put to death" at %d seats · cutting-off at %d seats across the three chapters · childless at %s · '
      'bear-iniquity at %s · the set face at %s · zimah at %s (19:29 outside the span: %s) · henah at %s · '
      '"you shall not uncover" %d seats · "you shall not approach" at %s · abomination %s / confusion %s · the tent door '
      'at %s · "any man, any man" at %s · the convert at %s · the land vomits at %s · niddah at %s · Molech at %s · the '
      'ghost-pit at %s · "and a man who" %d + "and a woman who" %s · "to the LORD" in 17 %s · 17:13 (wild-or-bird, dust, '
      'cover, beast) %s · the two outside verbs %s · soul tokens in 17 %s'
      % (c_formula_pl, c_formula_sg, c_stone, c_burn, len(c_mot), len(c_karet), c_ariri, c_bear, c_face, c_zimah,
         c_zimah_19, c_henah, len(c_tegaleh), c_tikrav, c_toevah, c_tevel, c_tent, c_ish_ish, c_ger, c_vomit, c_niddah,
         c_molech, c_ov, len(c_veish), c_veishah, c_lYHWH17, c_cover, c_two_clauses, c_nefesh17))

# ---- the callees (cold) --------------------------------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cold_run_chatat as CH
    import cold_run_clocks as CL
    import cold_run_shemini as SH
    import cold_run_offerings as OFF
# 17:5's "slaughter them as PEACE OFFERINGS" and 17:8's "burnt offering or
# sacrifice" name the offering types — resolved by live call (2026-09-06)
SHEL_ROW = OFF.dispatch('shelamim'); OLAH_ROW = OFF.dispatch('olah:flock')
UNWITTING_UNION = CH.domain({'intent': 'unwitting', 'karet_when_intentional': True})['v']
DOUBT_UNION = CH.domain({'intent': 'unknown'})['v']
DELIBERATE_UNION = CH.domain({'intent': 'intentional'})['v']
ZAV_PAIR = CL.zav('pair', sightings=3)['v']
PURE_BEAST = SH.classify({'clazz': 'land', 'hoof': True, 'cud': True})[0]
IMPURE_BEAST = SH.classify({'clazz': 'land', 'hoof': True, 'cud': False})[0]
print('routing receipts: cold_run_chatat CALLED — domain(unwitting) -> %r; domain(unknown) -> %r; domain(intentional) '
      '-> %r; cold_run_clocks CALLED — zav pair -> %r; cold_run_shemini CALLED — classify(hoof+cud) -> %r, (hoof only) '
      '-> %r [IMPORT, live calls]' % (UNWITTING_UNION, DOUBT_UNION, DELIBERATE_UNION, ZAV_PAIR, PURE_BEAST, IMPURE_BEAST))

I, M, A, D, P = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT'
def cell(v, p, why, fx):
    FX.validate(fx)
    return {'v': v, 'p': p, 'why': why, 'fx': fx}
SA = 'Sifra, Acharei Mot, '
SK = 'Sifra, Kedoshim, '

# =====================================================================
# THE CODE — from the ink of Leviticus 17, 18, and 20 alone. Mishnah/
# Talmud appear ONLY on [MOVE] lines (motion 4) and as DATA (motion 2).
# =====================================================================

# ---- F1: THE KINSHIP LIST (18:6-18) as relations from ego ----------
# steps: F father, M mother, W wife, S son, D daughter, SIS sister,
# PB paternal brother, MB maternal brother, B brother (either), FB the
# father's brother. Each relation is LOCATED by its own token in Lev 18.
KIN = [  # (relation, verse, label, locating token)
    (('M',),            7,  'his mother',                      'אמך'),
    (('F', 'W'),        8,  "his father's wife",               'אשת'),
    (('F', 'D'),        9,  'his paternal sister',             'אביך'),
    (('M', 'D'),        9,  'his maternal sister',             'אמך'),
    (('S', 'D'),        10, "his son's daughter",              'בנך'),
    (('D', 'D'),        10, "his daughter's daughter",         'בתך'),
    (('F', 'SIS'),      12, "his father's sister",             'אחות'),
    (('M', 'SIS'),      13, "his mother's sister",             'אחות'),
    (('FB', 'W'),       14, "his father's brother's wife",     'דדתך'),
    (('S', 'W'),        15, 'his daughter-in-law',             'כלתך'),
    (('PB', 'W'),       16, "his paternal brother's wife",     'אחיך'),
    (('MB', 'W'),       16, "his maternal brother's wife",     'אחיך'),
    (('W', 'D'),        17, "his wife's daughter",             'ובתה'),
    (('W', 'S', 'D'),   17, "her son's daughter",              'בנה'),
    (('W', 'D', 'D'),   17, "her daughter's daughter",         'בתה'),
    (('W', 'M'),        17, 'his mother-in-law',               'ובתה'),
    (('W', 'F', 'M'),   17, "his father-in-law's mother",      'בנה'),
    (('W', 'M', 'M'),   17, "his mother-in-law's mother",      'בתה'),
    (('W', 'SIS'),      18, "his wife's sister",               'אחתה'),
]
for rel, vs, label, tok in KIN:
    assert tok in toks('Lev', 18, vs), (label, vs, tok)
# 18:11 'your father's wife's daughter, BORN OF your father' = the paternal sister again (the
# marriage-bond reading, Sifra Kedoshim Chapter 11 13) — located, not a new relation:
assert 'מולדת' in toks('Lev', 18, 11) and 'אחותך' in toks('Lev', 18, 11)
# the pair-ban of 18:17 is SYMMETRIC in the ink ('a woman and her daughter... you shall not take'):
# the wife's three descendants read forward, her three ancestresses read backward — six from one verse.
FORBIDDEN = set(rel for rel, vs, label, tok in KIN) | {('D',)}   # the daughter: by the tradition's
# verbal analogy on the shared tokens (henah at 18:10 and 18:17; zimah at 18:17 and 20:14) — [MOVE]
LABEL = {rel: label for rel, vs, label, tok in KIN}; LABEL[('D',)] = 'his daughter'
VERSE = {rel: vs for rel, vs, label, tok in KIN}; VERSE[('D',)] = 10

def from_paternal_brother(rel):
    """The same woman seen from ego's PATERNAL BROTHER: compose ('PB',)+rel and normalize by the
    ink's own identities — my brother's father is my father; my brother's mother is my father's wife
    (18:8 covers any wife of the father); a daughter of my father's wife by ANOTHER man is not my
    sister (18:11: only 'born of your father'); my brother's maternal brother is my father's wife's
    son (no shared parent with me)."""
    r = ('PB',) + rel
    if r[:2] == ('PB', 'F'):
        return r[1:]                                  # PB.F.x -> F.x
    if r[:2] == ('PB', 'M'):
        rest = r[2:]
        if rest == ():           return ('F', 'W')    # his mother = my father's wife
        if rest == ('D',):       return ('F', 'W', 'D_by_another')   # not 'born of my father'
        if rest == ('SIS',):     return ('F', 'W', 'SIS')
        return ('F', 'W') + rest
    if r[:2] == ('PB', 'PB'):
        return r[1:]                                  # my brother's paternal brother is my paternal brother
    if r[:2] == ('PB', 'FB'):
        return r[1:]                                  # my brother's father's brother is my father's brother (one father)
    if r[:2] == ('PB', 'MB'):
        return ('F', 'W', 'S') + r[2:]                # a stepbrother
    return r                                          # PB.S.x, PB.D.x, PB.W.x — the brother's own house

def levirate(q):
    """Mishnah Yevamot 1:1 and 1:3 — COMPUTED: partition Lev 18's kinship list by one predicate:
    is the same woman ALSO forbidden to a paternal brother? If yes, no brother could have married
    her and no levirate case arises (the six); if no, she can be a brother's widow and an ervah at
    once — she and her rivals are exempt (the fifteen, with one import)."""
    six, fifteen = [], []
    for rel, vs, label, tok in KIN:
        comp = from_paternal_brother(rel)
        (six if comp in FORBIDDEN else fifteen).append(label)
    fifteen.append(LABEL[('D',)])                      # his daughter: PB.D = a niece, permitted [MOVE]
    fifteen.append('the wife of a brother not in his world')   # Deut 25:5 'dwell TOGETHER' [IMPORT]
    if q == 'fifteen':
        return cell(sorted(fifteen), I, '18:6-18 composed with "his paternal brother" — fourteen relations survive the '
                    'composition (not forbidden to the brother: his niece, his stepsister, his father\'s wife\'s '
                    'sister, his nephew\'s wife, his stepbrother\'s wife, his brother\'s wife\'s kin) + the daughter '
                    '[MOVE] + the not-in-his-world brother\'s wife [IMPORT Deut 25:5]; ' + SK + 'Chapter 12 10-11 '
                    '(the upon-her analogy; "from here they said: fifteen")', ['exempt'])
    if q == 'six':
        return cell(sorted(six), I, 'the six whose composition lands back in the list: his mother = the brother\'s '
                    'father\'s wife (18:8); his father\'s wife, his father\'s sister, his paternal sister, his '
                    'father\'s brother\'s wife, his paternal brother\'s wife = the brother\'s own (' + SK +
                    'Chapter 12 12: "married of necessity to OTHERS — their rivals permitted")', ['exempt'])
    if q == 'count':
        return cell((len(fifteen), len(six)), I, 'the partition of the twenty kinship relations + one import', [FX.NONE])
    if q == 'rival_chain':
        return cell('rival_of_rival_exempt_even_a_hundred', I, 'Yevamot 1:2 — the same predicate recursed: the '
                    'rival married a second brother and died — her rival is exempt as she was; ' + SK +
                    'Chapter 12 11 ("their rivals\' rivals to the end of the world")', ['exempt'])
    if q == 'release_timing':
        return cell('ervah_must_stand_at_the_death', M, '18:18 "upon her IN HER LIFETIME" read at the moment of '
                    'the bond (' + SK + 'Chapter 12 10, the upon-her analogy): the daughter who died or was divorced '
                    'BEFORE the brother\'s death frees her rival; whoever could refuse and did not — her rival '
                    'performs release, not levirate (Yevamot 1:2)', ['released'])
    if q == 'not_in_world':
        return cell('exempt_and_her_rival_exempt', P, 'Deut 25:5 "when brothers dwell TOGETHER" [IMPORT] — the bond '
                    'never attached to a brother born after the death; the second wife exits as her rival '
                    '(Yevamot 2:1-2 — the order of birth and levirate does not change it)', ['exempt'])
    if q == 'not_in_world_maamar':
        return cell('release_not_levirate_R._Shimon_either', M, 'Yevamot 2:1-2 — a declaration (maamar) made and he '
                    'died: the second performs release; R. Shimon: he takes or releases whichever he wishes — the '
                    'declaration\'s force is the sheet\'s parameter, the dispute carried', ['released'])
    if q == 'houses':
        return cell(['Beit_Shammai_permit_the_rivals', 'Beit_Hillel_forbid'], A, 'Yevamot 1:4 (= Eduyot 4:8) — the '
                    'houses on the rival wives; the machine\'s verdict is Hillel\'s (the Sifra\'s "from here they '
                    'said", Chapter 12 11); the intermarriage peace kept', ['exempt'])
    raise ValueError(q)

def grade(union):
    """Mishnah Yevamot 2:3 — the three grades: an ervah (this span's karet class) — neither release
    nor levirate; a commandment-ban (the scribes' seconds, self-labeled) or a sanctity-ban (Lev 21,
    Deut 23) — release, not levirate."""
    if union in FORBIDDEN or union in ('menstruant', 'married_woman'):
        return cell('neither_release_nor_levirate', I, '18:29 "the souls that do shall be cut off" — the karet class '
                    'IS the ervah grade; the union takes no marriage, so no bond forms (Yevamot 2:3)', ['exempt'])
    if union == 'second_degree':
        return cell('release_not_levirate', A, 'Yevamot 2:4 — the seconds "from the words of the scribes" '
                    '(self-labeled scribal; verdicted, not encoded)', ['released'])
    if union in ('widow_to_high_priest', 'divorcee_to_priest', 'mamzeret'):
        return cell('release_not_levirate', P, 'Yevamot 2:4 — the sanctity bans: Lev 21:7, 21:14 [IMPORT — sitting '
                    'L5]; Deut 23:3 [IMPORT]', ['released'])
    return cell('release_or_levirate', I, 'no ban — Deut 25:5\'s ordinary case [IMPORT]', [FX.NONE])

def cowives(q, **k):
    if q == 'ervah_sister_free':
        return cell('forbidden_to_her_permitted_to_her_sister', M, 'Yevamot 3:2 — an ervah takes no marriage, so she '
                    'is no "wife" and her sister no "wife\'s sister": 18:18\'s "you shall not TAKE" binds only where '
                    'a taking exists (' + SK + 'Chapter 10 12\'s taking-path reading on the parallel clause)',
                    ['exempt'])
    if q == 'cross':
        return cell('each_forbidden_to_one_permitted_to_the_other', I, 'Yevamot 3:3 — the composition run per '
                    'brother: "her sister who is her yevamah — release or levirate" (2:3)', [FX.NONE])
    if q == 'zikah_sisters':
        return cell('release_not_levirate_married_first_put_out', A, 'Yevamot 3:1 — four brothers, two sisters bound '
                    'to both: the BOND counted as a marriage for 18:18 — the sheet\'s parameter (R. Eliezer: '
                    'Shammai let them keep, Hillel put out)', ['released'])
    if q == 'pair_bans_bound':
        return cell('release_not_levirate_R._Shimon_exempts', I, 'Yevamot 3:4 — two sisters, or a woman and her '
                    'daughter / granddaughter (18:17\'s pairs) bound to one man: release; R. Shimon exempts; an '
                    'ervah among them — her sister permitted', ['released'])
    if q == 'stranger_cases':
        return cell('wifes_sister_exits_and_her_rival', I, 'Yevamot 3:6 — the stranger-married brother took a '
                    'sister\'s husband\'s widow and died: the first exits as the wife\'s sister (18:18), the second '
                    'as her rival; a declaration — release', ['exempt'])
    if q == 'one_hour':
        return cell('forbidden_forever', M, 'Yevamot 3:7, 3:9 — the status AT THE DEATH fixes the verdict: forbidden '
                    'one hour (as the wife\'s sister while the wife lived, 18:18 "in her lifetime") — forbidden '
                    'forever, though the wife has since died', ['exempt'])
    if q == 'divorced_before':
        return cell('rivals_permitted', I, 'Yevamot 3:7 — divorced BEFORE the death: "all who died or were '
                    'divorced, their rivals are permitted" (1:1)', [FX.NONE])
    if q == 'maamar_houses':
        return cell(['Shammai_his_wife_stays', 'Hillel_puts_out_both'], A, 'Yevamot 3:5 — "woe to him for his wife '
                    'and woe for his brother\'s wife": the declaration\'s force disputed', [FX.NONE])
    if q == 'two_bonds':
        return cell('release_not_levirate_one_levir_not_two', P, 'Yevamot 3:9 — "one of them died — her levir shall '
                    'come upon her" (Deut 25:5) [IMPORT]: one bond, not two; R. Shimon takes either', ['released'])
    if q == 'swapped_names':
        names = []
        if k.get('married'):   names.append('married_woman_20:10')
        if k.get('brothers'):  names.append("brother's_wife_18:16")
        if k.get('sisters'):   names.append("wife's_sister_18:18")
        if k.get('niddot'):    names.append('menstruant_18:19')
        return cell(names, I, 'Yevamot 3:10 — THE NAMES STACK: every relation the case supplies is a clause of the '
                    'span, each counted (the same enumeration as Keritot 3:6\'s seven)', ['karet_cut_off'])
    if q == 'swapped_aftermath':
        return cell('separated_three_months_minors_returned_priestesses_barred', A, 'Yevamot 3:10 — the pregnancy '
                    'wait (data), the minors, the terumah bar (Lev 22 — L5)', ['barred_from_holies'])
    raise ValueError(q)

def names(relations):
    """Keritot 3:6 / Yevamot 3:10 — count the liability NAMES one act carries: each relation the case
    supplies that is a clause of the span."""
    named = [r for r in relations if r in FORBIDDEN or r in ('married_woman', 'menstruant')]
    return cell(len(named), I, 'one act, %d clauses of Lev 18/20 (%s) — the enumeration counts each clause the '
                'case\'s woman satisfies' % (len(named), ', '.join(LABEL.get(r, r) for r in named)), ['karet_cut_off'])

def three_are_one():
    return cell(['sages_one_name', 'R._Yochanan_ben_Nuri_three'], A, 'Keritot 3:6 — the mother-in-law, her mother, '
                'the father-in-law\'s mother: "the three are ONE name" — 18:17\'s one clause (the pair-ban read '
                'backward yields all three from one verse); R. Yochanan ben Nuri counts three', [FX.NONE])

# ---- F2: THE SANCTIONS MATRIX (Lev 20 read by its own sanction tokens) ----
# Each union is LOCATED in Lev 20 by its kinship token; the located verse is then read for its
# sanction tokens. Nothing here names a mode the verse does not carry — except where labeled.
UNIONS = {  # union: (warning verse in 18, locating token in 20, label)
    'father_wife':      (8,  ('אשת', 'אביו'),     "his father's wife"),
    'mother':           (7,  ('אשת', 'אביו'),     'his mother'),          # via the father's-wife clause [MOVE]
    'daughter_in_law':  (15, ('כלתו',),           'his daughter-in-law'),
    'male':             (22, ('זכר',),            'the male'),
    'man_beast':        (23, ('שכבתו', 'בבהמה'), 'the man with a beast'),   # 'with a beast' alone also stands at 20:25 (the species clause) — the full phrase locates
    'woman_beast':      (23, ('לרבעה',),          'the woman bringing a beast'),
    'woman_and_mother': (17, ('אשה', 'ואת', 'אמה'), 'a woman and her mother'),
    'adultery':         (20, ('אשת', 'רעהו'),     "a man's wife"),
    'sister':           (9,  ('אחתו',),           'his sister'),
    'menstruant':       (19, ('דוה',),            'the menstruant'),
    'father_sister':    (12, ('ואחות', 'אביך'),   "his father's sister"),
    'mother_sister':    (13, ('אחות', 'אמך'),     "his mother's sister"),
    'uncle_wife':       (14, ('דדתו',),           "his father's brother's wife"),
    'brother_wife':     (16, ('אשת', 'אחיו'),     "his brother's wife"),
    'wife_sister':      (18, None,                "his wife's sister"),      # no Lev 20 seat: 18:29's general
    'molech':           (21, ('יתן', 'מזרעו', 'למלך'), 'the Molech giver'),   # 'to Molech' stands at 20:2, 3, 4 — the giving verb locates the sanction seat
    'ov_bearer':        (None, ('אוב',),          'the ghost-pit or familiar bearer'),   # warning Lev 19:31 [IMPORT]
    'curser':           (None, ('יקלל',),         'the curser of father and mother'),  # warning Exod 21:17 [IMPORT]
}
def locate20(tok):
    if tok is None: return None
    hits = [v for (c, v) in SPAN if c == 20 and has(*tok)(toks('Lev', 20, v))]
    if tok == ('אוב',): hits = [v for v in hits if v == 27]      # 20:6 carries the plural noun (the consulter's clause)
    assert len(hits) == 1, (tok, hits)
    return hits[0]
LOC = {u: locate20(t) for u, (w, t, l) in UNIONS.items()}
assert LOC == {'father_wife': 11, 'mother': 11, 'daughter_in_law': 12, 'male': 13, 'man_beast': 15, 'woman_beast': 16,
               'woman_and_mother': 14, 'adultery': 10, 'sister': 17, 'menstruant': 18, 'father_sister': 19,
               'mother_sister': 19, 'uncle_wife': 20, 'brother_wife': 21, 'wife_sister': None, 'molech': 2,
               'ov_bearer': 27, 'curser': 9}, LOC

def read_sanction(v):
    """The sanction tokens of one verse of Lev 20, as written."""
    t = toks('Lev', 20, v)
    return dict(stoning=any(w in t for w in ('ירגמהו', 'ירגמו')), burning=has('באש', 'ישרפו')(t),
                formula=has('דמיהם', 'בם')(t) or has('דמיו', 'בו')(t),
                mot=any(t[i] == 'מות' and t[i + 1] in ('יומת', 'יומתו') for i in range(len(t) - 1)),
                karet=any('כרת' in w for w in t), ariri='ערירים' in t,
                bear=any(w in ('ישא', 'ישאו') for w in t), beast_killed=any(w in ('תהרגו', 'והרגת') for w in t))

def mode(v):
    """The court mode of a Lev 20 verse. INK where the verse names it; the formula 'their blood is
    upon them' decoded to stoning on the ink's own co-occurrence (20:27 is the only seat where the
    formula stands beside a named mode, and the mode is stoning) — the tradition's building block
    (Sifra Kedoshim Chapter 9 14) grounded on the census; the bare 'put to death' filled as
    strangling by the recorded default [MOVE]."""
    s = read_sanction(v)
    if s['stoning']: return ('stoning', I)
    if s['burning']: return ('burning', I)
    if s['formula']:
        assert (20, 27) in c_formula_pl and read_sanction(27)['stoning']
        return ('stoning', M)
    if s['mot']:     return ('strangling', M)
    return (None, I)

def sanction(u):
    """One union -> (warning verse, sanction verse, court mode, karet) read off the ink."""
    w18, tok, label = UNIONS[u]
    v = LOC[u]
    if u == 'wife_sister':
        return cell((18, None, None, True), I, '18:18 the warning; no Lev 20 seat — the karet by 18:29 "the souls '
                    'that DO these abominations shall be cut off" (the whole list\'s karet; Mishnah Keritot 1:1 '
                    'lists her)', ['karet_cut_off'])
    s = read_sanction(v)
    if u == 'molech':
        s['karet'] = s['karet'] or read_sanction(3)['karet']   # 20:3 'I will cut HIM off' — the clause's own continuation
    md, pv = mode(v)
    if u == 'man_beast':
        md, pv = 'stoning', M    # 20:15 bare 'put to death'; the beast 'killed' — stoning by the killing analogy
    if u == 'mother':
        pv = M                   # the mother not the father's wife: 20:11 via 18:7 (Sifra Kedoshim Chapter 10 9)
    if u == 'ov_bearer':
        s['karet'] = read_sanction(6)['karet']; pv = M   # 20:6's karet assigned to the bearer (Sifra Kedoshim Chapter 10 1)
    karet = s['karet'] or s['bear'] or s['ariri'] or u in ('father_wife', 'mother', 'daughter_in_law', 'male',
                                                           'man_beast', 'woman_beast', 'woman_and_mother', 'adultery')
    why = {
        'father_wife': '20:11 "both shall be put to death, their blood is upon them" — the formula, decoded on 20:27',
        'mother': '20:11 via 18:7 "she is your mother" — the mother who is not the father\'s wife: ' + SK +
                  'Chapter 10 9 (liable QUA MOTHER only — the single-count arm; Sanhedrin 7:4 counts both)',
        'daughter_in_law': '20:12 "both shall be put to death... confusion (tevel) they have done; their blood is upon them"',
        'male': '20:13 "an abomination they have done, both shall be put to death; their blood is upon them"',
        'man_beast': '20:15 "he shall surely be put to death, and the beast you shall kill" — the mode by ' + SK +
                     'Chapter 11 1 (the killing verbal analogy to the enticer\'s stoning) [MOVE]',
        'woman_beast': '20:16 "you shall kill the woman and the beast; they shall surely be put to death; their blood '
                       'is upon them"',
        'woman_and_mother': '20:14 "in FIRE they shall burn him and them" — the one burning clause of the span',
        'adultery': '20:10 "the adulterer and the adulteress shall surely be put to death" — no mode written: ' + SK +
                    'Chapter 10 8 (R. Yonatan: the unspecified is strangling; Rabbi: a death that leaves no mark) [MOVE]',
        'sister': '20:17 "they shall be cut off in the sight of their people... his iniquity he shall bear"',
        'menstruant': '20:18 "both shall be cut off from among their people"',
        'father_sister': '20:19 "their iniquity they shall bear" — bear-iniquity = karet (' + SA + 'Chapter 12 15, the '
                         'Others\' verbal analogy; Keritot 1:1 lists both aunts) [MOVE]',
        'mother_sister': '20:19 — the same clause names both aunts',
        'uncle_wife': '20:20 "their sin they shall bear; childless they shall die"',
        'brother_wife': '20:21 "it is niddah (set apart)... childless they shall be" (Keritot 1:1 lists her)',
        'molech': '20:2 "the people of the land shall stone him with stone"; 20:3 "I will cut him off"',
        'ov_bearer': '20:27 "with stone they shall stone them; their blood is upon them" (the warning at 19:31 '
                     '[IMPORT]; the karet at 20:6 assigned to the bearer by ' + SK + 'Chapter 10 1)',
        'curser': '20:9 "his blood is upon him" — the formula; the warning from Exod 21:17 [IMPORT]',
    }[u]
    fx = []
    if md == 'stoning': fx.append('stoned')
    elif md == 'burning': fx.append('burned_by_court')
    elif md == 'strangling': fx.append('put_to_death')
    if karet: fx.append('karet_cut_off')
    if s['ariri']: fx.append('childless')
    if s['bear']: fx.append('bears_sin')
    if s['beast_killed']: fx.append('beast_killed')
    return cell((w18, v, md, karet), pv, why, fx or [FX.NONE])

def census(q):
    """The derived lists — the answer sheet's censuses recomputed from the matrix."""
    rows = {u: sanction(u)['v'] for u in UNIONS}
    if q == 'stoned':
        return cell(sorted(UNIONS[u][2] for u in rows if rows[u][2] == 'stoning'), I, 'Sanhedrin 7:4 — this '
                    'span\'s members of the stoned census: the formula seats + the two named stonings + the beast '
                    'by analogy', ['stoned'])
    if q == 'burned':
        return cell(sorted(UNIONS[u][2] for u in rows if rows[u][2] == 'burning'), I, 'Sanhedrin 9:1 — the '
                    'burning clause (20:14)', ['burned_by_court'])
    if q == 'strangled':
        return cell(sorted(UNIONS[u][2] for u in rows if rows[u][2] == 'strangling'), M, 'Sanhedrin 11:1 — the '
                    'bare "put to death" of 20:10 filled as strangling', ['put_to_death'])
    if q == 'lashes':
        return cell(sorted(UNIONS[u][2] for u in rows if rows[u][3] and rows[u][2] is None), I, 'Makkot 3:1 — '
                    'the lash list = the karet-grade unions WITHOUT a court death (a death supersedes the lashes; '
                    'the lash itself is Deut 25:2-3\'s [IMPORT])', ['lashes'])
    if q == 'karet_count':
        unions = [u for u in rows if rows[u][3]]   # the census names the mother AND the father's wife
        others = ['blood 17:10', 'slaughter outside 17:4', 'raising outside 17:9']
        # the census lists the fifteen unions by its own grouping: the mother + the father's wife are two entries,
        # the two aunts two, the two beast cases two, adultery one, the pair 'a woman and her daughter' one
        n = len(unions) + len(others)
        return cell(n, I, 'Keritot 1:1 — this span\'s members of the thirty-six: %d karet unions (%s) + Molech and '
                    'the ghost-pit inside them + blood, slaughter outside, raising outside' % (len(unions),
                    ', '.join(UNIONS[u][2] for u in unions)), ['karet_cut_off'])
    if q == 'formula_grounding':
        return cell('20:27_names_stoning_beside_the_formula', I, ('the decoder\'s ground: of the six formula seats %s, '
                    'exactly one carries a named mode — 20:27, stoning; ' + SK + 'Chapter 9 14 generalizes it to '
                    'every seat (the building block)') % (c_formula_pl,), [FX.NONE])
    raise ValueError(q)

def burned_nine():
    """Sanhedrin 9:1 — 'a woman and her daughter' includes nine: computed from 18:17's three pairs
    read both ways (six) + the man's own three (18:10's two by ink, the daughter by the analogy)."""
    six = [LABEL[r] for r in (('W', 'D'), ('W', 'S', 'D'), ('W', 'D', 'D'), ('W', 'M'), ('W', 'F', 'M'), ('W', 'M', 'M'))]
    own = [LABEL[('D',)], LABEL[('S', 'D')], LABEL[('D', 'D')]]
    return cell(sorted(six + own), M, ('18:17\'s pairs (symmetric in the ink: six) + 18:10\'s granddaughters carried '
                'into the zimah set by the shared token henah (18:10, 18:17: %s) and the daughter by the same analogy '
                '(' + SK + 'Chapter 10 13-14; Sanhedrin 76a not opened); the burning by the zimah token shared with '
                '20:14 (%s)') % (c_henah, c_zimah), ['burned_by_court'])

def burning_scope():
    return cell(['R._Yishmael_him_and_one', 'R._Akiva_both', 'Onkelos_plural'], M, SK + 'Chapter 10 15 — "him and '
                'them (ethen)": R. Yishmael one (the second marriage is the crime), R. Akiva both; Onkelos 20:14 '
                'renders the plural — the translation on Akiva\'s side', ['burned_by_court'])

def double_count(u):
    if u == 'mother':
        return cell(['qua_mother', 'qua_fathers_wife'], A, 'Sanhedrin 7:4 — liable on both names; R. Yehuda: the '
                    'mother alone (' + SK + 'Chapter 10 9\'s single-count arm)', ['stoned'])
    if u == 'father_wife':
        return cell(['qua_fathers_wife', 'qua_married_woman', 'in_life_or_after_death', 'from_betrothal_or_marriage'],
                    I, '18:8 "your father\'s wife" — no lifetime clause (contrast 18:18 "in her lifetime"): after the '
                    'father\'s death too; 20:10 counts her as a married woman while he lives', ['stoned'])
    if u == 'daughter_in_law':
        return cell(['qua_daughter_in_law', 'qua_married_woman', 'in_life_or_after_death', 'from_betrothal_or_marriage'],
                    I, '18:15 "your son\'s wife" — no lifetime clause; ' + SK + 'Chapter 10 10: the slave\'s and the '
                    'gentile\'s wife excluded (no marriage bond with the son)', ['stoned'])
    raise ValueError(u)

def beast(q):
    if q == 'why':
        return cell(['stumbling_came_through_it', 'not_walk_the_market_naming_the_sin'], M, SK + 'Chapter 11 5 — "the '
                    'stumbling came to a man through it" (with the a-fortiori to the misleader); Sanhedrin 7:4 adds '
                    'the market reason', ['beast_killed'])
    if q == 'court':
        return cell(23, A, 'Sanhedrin 1:4 — the beast partners by twenty-three FROM OUR VERSES: "you shall kill the '
                    'woman and the beast" (20:16), "the beast you shall kill" (20:15) — a capital docket takes the '
                    'capital court (the size is the sheet\'s: Num 35 / Sanhedrin 1:6)', ['beast_killed'])
    if q == 'passive_warning':
        return cell('Exod_22:18_freed_to_the_passive', P, SK + 'Chapter 11 2 — "whoever lies with a beast shall die" '
                    '(Exod 22:18) [IMPORT] not needed for the active (taught here) — GIVEN to the passive (M-18); '
                    'R. Akiva\'s revocalization of the lying verb (M-16)', ['put_to_death'])
    if q == 'woman_warning':
        return cell('18:23_a_woman_shall_not_stand_before_a_beast', I, '18:23 "a woman shall not stand before a beast '
                    'to mate with it" — her warning written; 20:16 her sanction', ['stoned'])
    raise ValueError(q)

def severity(q, **k):
    ORDER = {'sages': ['stoning', 'burning', 'killing', 'strangling'], 'R._Shimon': ['burning', 'stoning', 'strangling', 'killing']}
    if q == 'orders':
        return cell(ORDER, A, 'Sanhedrin 7:1 — the four handed to the court in two recorded orders; 9:3: the sages — '
                    'stoning severer (given to the blasphemer and idolater); R. Shimon — burning severer (given to '
                    'the priest\'s daughter)', [FX.NONE])
    if q == 'two_deaths':
        o = ORDER[k.get('arm', 'sages')]
        m = min(k['modes'], key=o.index)
        return cell(m, A, 'Sanhedrin 9:4 — liable to two deaths: the SEVERER (R. Yosei: the first bond); the ranking '
                    'is the sheet\'s parameter', ['put_to_death'])
    if q == 'mixed':
        o = ORDER[k.get('arm', 'sages')]
        m = max(k['modes'], key=o.index)
        return cell(m, A, 'Sanhedrin 9:3 — death-liables mixed: judged by the LIGHTEST (the doubt individuated: 17:4 '
                    '"that man" — not the misled, ' + SA + 'Chapter 9 2)', ['put_to_death'])
    if q == 'murderer_mixed':
        return cell(['all_exempt', 'R._Yehuda_confined'], A, 'Sanhedrin 9:3 — a murderer mixed among others', ['exempt'])
    if q == 'procedure':
        return cell({'burning': 'dung_to_the_knees_hard_scarf_in_soft_the_lit_wick_into_the_mouth',
                     'strangling': 'dung_to_the_knees_hard_scarf_in_soft_two_pull_until_the_soul_departs',
                     'stoning': 'one_stone_suffices_not_in_his_clothing'}, M, 'Sanhedrin 7:2-3 (the burning and '
                    'strangling procedures = ' + SK + 'Chapter 10 8\'s own words for the strangling); ' + SK +
                    'Section 4 4: "with STONE" — one stone suffices if he died by it, "shall stone him" — not in his '
                    'clothing; the branches-burning REFUSED (7:2)', ['put_to_death'])
    raise ValueError(q)

# ---- F2b: MOLECH, THE GHOST-PIT, THE CURSER, THE ADULTERER ------------
def molech(q, handed=True, passed=True, fire=True, to_molech=True, **k):
    if q == 'predicate':
        liable = handed and passed and fire and to_molech
        return cell('liable' if liable else 'exempt', I if liable else M, ('20:2-4 "who GIVES of his seed to Molech" '
                    '(three seats %s) + 18:21 "to PASS to Molech": handing and passing and Molech are the span\'s own '
                    'tokens; "through FIRE" is Deut 18:10\'s [IMPORT] by ' + SK + 'Section 4 3\'s verbal analogy — '
                    'the four-condition conjunction (Sanhedrin 7:7: handed-not-passed, passed-not-handed — exempt)')
                    % (c_molech,), ['stoned', 'karet_cut_off'] if liable else ['exempt'])
    if q == 'who_stones':
        return cell('the_people_of_the_land', I, '20:2 "the people of the land shall stone him with stone" — Onkelos: '
                    'the people of the house of Israel; ' + SK + 'Section 4 4: the court lacking strength — the '
                    'people assist', ['stoned'])
    if q == 'seed_scope':
        return cell(['son', 'daughter', 'grandson', 'granddaughter', 'unfit_seed'], M, SK + 'Section 4 6-7 — "of his '
                    'SEED": grandchildren and unfit seed included', ['stoned'])
    if q == 'concealed':
        return cell('karet_by_Heaven_and_his_family', I, '20:4-5 "if the people of the land hide their eyes... I will '
                    'set My face against that man and against his family and cut him off" — the court\'s failure '
                    'routes the case to Heaven\'s docket', ['face_set_against', 'karet_cut_off'])
    if q == 'family':
        return cell('afflictions_not_karet', M, SK + 'Section 4 13-14 — R. Shimon: what did the family sin? THE '
                    'SHELTERING PRINCIPLE (they shield him); bounded: HE is cut off, the family under afflictions '
                    '("him I cut off"); Onkelos 20:5 "his supporters"', ['face_set_against'])
    if q == 'ladder':
        return cell(['one_matter_to_many', 'one_court_to_many', 'lesser_courts_to_the_Sanhedrin_and_capital_law_taken'],
                    M, SK + 'Section 4 9-11 — the concealment ladder, an institutional-decay induction recorded as law',
                    [FX.NONE])
    if q == 'all_who_stray':
        return cell('all_foreign_services_swept_into_the_karet', I, '20:5 "and all who stray after him to stray '
                    'after Molech" — ' + SK + 'Section 4 15', ['karet_cut_off'])
    if q == 'effects_chain':
        return cell(['defiles_the_sanctuary', 'profanes_the_Name', 'removes_the_Presence', 'fells_by_the_sword', 'exiles'],
                    M, '20:3 "to defile My sanctuary and profane My holy Name" — ' + SK + 'Section 4 8\'s five-effect chain',
                    ['face_set_against'])
    if q == 'translation_gate':
        return cell('silenced_with_rebuke', A, 'Megillah 4:9 — rendering 18:21 as "to pass in Aramean-ness" (the '
                    'intermarriage reading) is silenced: the four-condition predicate refuses it; Onkelos keeps the '
                    'literal pass-through', [FX.NONE])
    if q == 'gentile_court':
        return cell('their_unions_by_their_law_Israel_unions_by_Israel_law', M, SK + 'Section 4 2', [FX.NONE])
    raise ValueError(q)

def ov(q):
    if q == 'bearer':
        return cell('stoning', I, '20:27 "a man or woman in whom is a ghost-pit or familiar shall surely be put to '
                    'death; with stone they shall stone them" — the mode NAMED beside the formula', ['stoned'])
    if q == 'consulter':
        return cell('warning_only', M, SK + 'Chapter 9 13 — "in THEM": the bearer, not the consulter; the consulter '
                    'under 19:31\'s warning [IMPORT] (Sanhedrin 7:7)', [FX.NONE])
    if q == 'definitions':
        return cell({'ov': 'the_pitom_speaking_from_the_armpit', 'yidoni': 'speaking_from_the_mouth'}, A, 'Sanhedrin '
                    '7:7 — the two defined (data)', [FX.NONE])
    if q == 'three_verses':
        return cell({'punishment': '20:27', 'warning': '19:31', 'karet': '20:6'}, M, (SK + 'Chapter 10 1 — the '
                    'three-verse completion: the karet of 20:6 ("the soul that turns to the ghost-pits") assigned '
                    'to the bearer; two of the three in this span (%s)') % (c_ov,), ['karet_cut_off', 'stoned'])
    if q == 'persons':
        return cell(['man', 'woman', 'tumtum', 'androgynous'], M, SK + 'Chapter 9 13 — "OR a woman" includes the '
                    'hidden-sexed and double-sexed', [FX.NONE])
    raise ValueError(q)

def curser(q, **k):
    if q == 'mode':
        return cell('stoning', M, ('20:9 "his blood is upon him" — the formula\'s singular seat (%s), decoded on 20:27; '
                    + SK + 'Chapter 9 3') % (c_formula_sg,), ['stoned'])
    if q == 'by_the_name':
        by_name = k.get('by_name', True)
        if by_name:
            return cell('liable', P, 'Sanhedrin 7:8 — not liable until he curses BY THE NAME: ' + SK + 'Chapter 10 6 '
                        'from Lev 24:16 "when he pronounces the NAME" [IMPORT — the first call\'s span]', ['stoned'])
        return cell(['R._Meir_liable', 'sages_exempt'], A, 'Sanhedrin 7:8 — by an appellation (kinnuy): disputed',
                    [FX.NONE])
    if q == 'after_death':
        return cell('liable', M, 'Sanhedrin 11:1 — the curser AFTER DEATH liable, the striker after death exempt: '
                    + SK + 'Chapter 9 3 (20:9\'s doubled "his father and his mother he cursed" read past the death; '
                    'the striker\'s clause needs a wound)', ['stoned'])
    if q == 'one_parent':
        return cell('either_parent_suffices', M, SK + 'Chapter 9 2 / Chapter 10 5 — R. Yonatan\'s default: a '
                    'CONJOINED PAIR MEANS EITHER ONE unless the verse says "together" (the joint-vs-several rule; '
                    'Deut 25:5\'s "together" is the counter-exemplar)', ['stoned'])
    if q == 'which_parent':
        return cell({'grandfather': 'excluded', 'doubtful_parent': 'excluded', 'convert': 'liable_on_the_mother_R._Yosei_HaGelili',
                     'shtuki': 'liable_on_the_mother_alone'}, M, SK + 'Chapter 9 1-2 — HIS father, the certain parent; '
                    'the convert; R. Akiva\'s symmetry rule and his concession on the fatherless-unknown', [FX.NONE])
    if q == 'son_from_anywhere':
        return cell('liable_except_from_maidservant_or_gentile', M, 'Yevamot 2:5 — a son from anywhere is liable for '
                    'his blow and his curse, except the maidservant\'s and the gentile woman\'s (no Israelite '
                    'descent — ' + SK + 'Chapter 9 2\'s convert rule)', ['stoned'])
    if q == 'warning_source':
        return cell('the_common_side_of_judge_prince_deaf', M, SK + 'Chapter 10 7 — THE THREE-SOURCE ARGUMENT: '
                    'judge, prince, deaf each refuted alone, closed by "in your people"; the freed "judge" GIVEN to '
                    'the father (M-18); Exod 21:17 the punishment\'s twin [IMPORT]', [FX.NONE])
    raise ValueError(q)

def adultery(q, **k):
    if q == 'mode':
        return cell('strangling', M, '20:10 "shall surely be put to death" — no mode written: ' + SK + 'Chapter 10 8, '
                    'three routes (R. Yoshiyah — the lightest; R. Yonatan — the unspecified is strangling; Rabbi — '
                    'like death by Heaven, no mark)', ['put_to_death'])
    if q == 'both':
        return cell('the_adulterer_and_the_adulteress', I, '20:10 names both agents (Onkelos keeps the doubled clause)',
                    ['put_to_death'])
    if q == 'whose_wife':
        w = k.get('wife_of')
        if w == 'minor':
            return cell('exempt', M, '20:10 "a MAN\'s wife" — not the minor\'s wife (' + SK + 'Chapter 10 8)', ['exempt'])
        if w == 'gentile':
            return cell('exempt', M, '20:10 "his FELLOW\'s wife" — not the gentile\'s (' + SK + 'Chapter 10 8)', ['exempt'])
        return cell('liable', I, '20:10 the doubled clause — a man\'s wife, his fellow\'s wife', ['put_to_death'])
    if q == 'threshold':
        return cell('from_entry_to_the_husbands_domain_even_before_intercourse', A, 'Sanhedrin 11:6 — once she '
                    'entered the husband\'s domain for marriage; the betrothed stage is Deut 22\'s stoning [ROUTED]',
                    ['put_to_death'])
    if q == 'second_partner':
        return cell('strangling', M, 'Sanhedrin 7:9 — the second who came upon the betrothed maiden: no longer a '
                    'virgin, her status is a married woman\'s — 20:10\'s default runs', ['put_to_death'])
    if q == 'unwitting':
        return cell(UNWITTING_UNION, P, 'Keritot 1:2 — unwitting: CALLED cold_run_chatat.domain (the karet-class '
                    'domain) -> the sin offering', ['atoned_forgiven'])
    if q == 'doubt':
        return cell(DOUBT_UNION, P, 'Keritot 1:2 — unknown: CALLED cold_run_chatat.domain -> the suspended ram',
                    ['suspends'])
    if q == 'deliberate_unwitnessed':
        return cell(DELIBERATE_UNION, P, 'Keritot 1:2 — deliberate without witnesses: CALLED -> karet, no offering',
                    ['karet_cut_off'])
    raise ValueError(q)

def unions_misc(q):
    if q == 'partial_act':
        return cell('partial_counts_as_complete_for_all', M, SK + 'Chapter 12 2 — "her fountain he laid bare" (20:18) '
                    'extended to all the unions by the two-source building block (with 20:19\'s "his kin he laid bare")',
                    ['karet_cut_off'])
    if q == 'aunts_both_sides':
        return cell('mothers_sister_and_fathers_sister_from_either_side', M, SK + 'Chapter 12 4 — the paternal-only '
                    'inference refused by 20:19\'s own naming of both', ['karet_cut_off'])
    if q == 'uncle_wife_bound':
        return cell('fathers_brother_only', M, SK + 'Chapter 12 6 — "his aunt" = the FATHER\'s brother\'s wife by the '
                    'uncle-uncle verbal analogy to Lev 25:49; 18:14 "your father\'s brother" (the ink names the '
                    'father\'s side)', ['childless'])
    if q == 'brother_wife_window':
        return cell('forbidden_with_children_permitted_childless_by_levirate', M, SK + 'Chapter 12 8 — "she is '
                    'niddah": LIKE THE MENSTRUANT, a prohibition with a permitted state (Deut 25:5 [IMPORT]); 20:21 '
                    '"childless" the Sifra\'s two readings, Onkelos ruling "without child"', ['childless'])
    if q == 'chesed':
        return cell(['disgrace_Onkelos', 'lovingkindness_the_Cain_charter_Sifra'], M, '20:17 "it is chesed" — the '
                    'homonym: Onkelos "a disgrace"; ' + SK + 'Chapter 11 11 "the world is built by chesed" (the first '
                    'generations\' sister-marriages chartered)', ['karet_cut_off'])
    if q == 'sister_both_deliberate':
        return cell('both_deliberate_for_the_mutual_penalty', I, '20:17 "he sees her nakedness AND she sees his" — '
                    'the two clauses', ['karet_cut_off'])
    if q == 'sister_scope':
        return cell({'paternal_or_maternal': 'both', 'born_home_or_outside': 'keep_her_or_send_her', 'maidservant_or_gentile_daughter': 'excluded'},
                    I, ('18:9 "your father\'s daughter OR your mother\'s daughter, born at home or born outside" (%s); '
                    '20:17 the same pair; ' + SK + 'Chapter 11 13 (the marriage-bond carve; Onkelos 18:9\'s legal parsing)')
                    % (c_1517,), ['karet_cut_off'])
    if q == 'no_inference':
        return cell(['no_punishing_from_inference', 'no_warning_from_inference'], M, SK + 'Chapter 11 10, 11 12 — the '
                    'sister of both parents needs her own clause (20:17 gives it); ' + SA + 'Chapter 13 14: the '
                    'general-and-particular closes the class', [FX.NONE])
    if q == 'gentile_and_woman_warned':
        return cell(['gentiles_warned', 'the_woman_warned'], M, (SA + 'Chapter 13 1 — "any man, any man" (%s); "you shall '
                    'not approach" plural (%s)') % (c_ish_ish, c_tikrav), [FX.NONE])
    if q == 'father_clause':
        return cell('the_male_lying_with_the_father', M, '18:7 "your father\'s nakedness" — read as the father himself '
                    '(the male clause 18:22 / 20:13; Sanhedrin 54a not opened) — Sanhedrin 7:4 counts him under the male',
                    ['stoned'])
    if q == 'void_betrothal':
        return cell('neither_betrothed', I, 'Kiddushin 2:7 — a woman and her daughter, or two sisters, as one: 18:17-18\'s '
                    'pairs cannot both be taken — the ervah grade voids the act (Yevamot 2:3)', ['exempt'])
    raise ValueError(q)

# ---- F3: OUTSIDE SLAUGHTER AND RAISING (17:3-9; Zevachim 13-14) -------
def outside(q, **k):
    if q == 'two_offenses':
        return cell('liable_for_slaughter_and_liable_for_raising', I, '17:3-4 "who SLAUGHTERS... shall be cut off" and '
                    '17:8-9 "who RAISES... shall be cut off" — two clauses, two karet formulas (%s)' % (c_karet[:2],),
                    ['blood_reckoned', 'karet_cut_off'])
    if q == 'who':
        p = k.get('person')
        if p == 'gentile':
            return cell('not_liable_and_permitted_a_platform', M, SA + 'Section 6 1 — Israel liable; gentiles NOT — '
                        'and permitted to offer to Heaven anywhere', ['exempt'])
        return cell('liable', I, '17:3 "any man of the house of Israel"; 17:8 "and of the convert who sojourns" (%s)'
                    % (c_ger[:1],), ['karet_cut_off'])
    if q == 'where':
        return cell('anywhere_but_the_tent_door', I, ('17:3 "in the camp or outside the camp" + 17:4 "to the tent door '
                    'he did not bring it" (the tent door at %s): the geography is one test — ' + SA + 'Section 6 3 '
                    '(unfit for ANY offering\'s slaughter)') % (c_tent,), ['blood_reckoned'])
    if q == 'agency':
        return cell('reckoned_to_the_slaughterer_not_his_sender', I, '17:4 "blood shall be reckoned TO THAT MAN" — '
                    + SA + 'Chapter 9 1', ['blood_reckoned'])
    if q == 'two_slaughter':
        return cell('exempt', M, '17:4 "he has shed blood" — ONE who slaughters; two together exempt (' + SA +
                    'Chapter 9 1; Zevachim 13:3)', ['exempt'])
    if q == 'two_raise':
        return cell(['liable_R._Shimon', 'exempt_R._Yosei'], M, SA + 'Chapter 10 2 — "any man, any man" includes two '
                    '(R. Shimon); "THAT one" exempts two (R. Yosei); the sheet follows R. Shimon (Zevachim 13:3)',
                    ['karet_cut_off'])
    if q == 'individual':
        return cell('individual_not_community_not_coerced_erring_misled', M, '17:4 "that man shall be cut off" — ' + SA +
                    'Chapter 9 2', ['karet_cut_off'])
    if q == 'bird':
        act = k.get('act')
        if act == 'slaughter':
            return cell('liable', M, SA + 'Section 6 4 — bird SLAUGHTER liable ("or who slaughters")', ['karet_cut_off'])
        return cell('not_liable', M, SA + 'Section 6 4 — bird PINCHING (the inside rite) not; the a-fortiori refused '
                    'by "who SLAUGHTERS"', ['exempt'])
    if q == 'common_inside':
        return cell('not_this_law', I, '17:4 "to offer an OFFERING to the LORD" — common animals inside are not this '
                    'clause (' + SA + 'Section 6 5)', [FX.NONE])
    if q == 'temple_upkeep':
        return cell('excluded', M, SA + 'Section 6 6 — upkeep consecrations never come to the tent door', ['exempt'])
    if q == 'dispatched_goat':
        return cell('exempt', I, ('17:4 "to the LORD" (%s) — the dispatched goat is not designated to the Name on the '
                    'altar (' + SA + 'Section 6 7; Zevachim 14:1: whatever is not fit to come to the tent door)')
                    % (c_lYHWH17,), ['exempt'])
    if q == 'red_cow':
        return cell('exempt', I, 'Zevachim 14:1 — burned outside its pit: "to the tent door he did not bring it" — '
                    'the cow never comes to the door', ['exempt'])
    if q == 'unfit_list':
        return cell('exempt', M, '17:4 "before the tabernacle of the LORD" — the mounting and mounted, set-aside, '
                    'worshipped, hire, price, crossbreed, torn, side-born; the blemished (' + SA + 'Section 6 7; '
                    'Zevachim 14:2)', ['exempt'])
    if q == 'time_deferred':
        return cell(['exempt', 'R._Shimon_plain_negative'], M, SA + 'Section 6 8 — "before the tabernacle" = fit NOW; '
                    'R. Shimon: a negative without karet; the sages: no karet, no negative (Zevachim 14:2)', ['exempt'])
    if q == 'lacking_time_owner':
        who = k.get('offering')
        if who in ('chatat', 'asham'):
            return cell('exempt', P, 'Zevachim 14:3 — the zav, zavah, birther, leper: their sin or guilt offering is '
                        'owed only after the count — CALLED cold_run_clocks.zav(pair) -> %r (the eighth day): before it '
                        'the offering is not receivable, so 17:4\'s "before the tabernacle" exempts' % ZAV_PAIR, ['exempt'])
        return cell('liable', I, 'Zevachim 14:3 — their burnt offerings and shelamim: fit any day', ['karet_cut_off'])
    if q == 'flesh_list':
        return cell('exempt', M, SA + 'Chapter 10 9 — only FIRE-WORTHY classes: sin-offering flesh, guilt flesh, '
                    'most-holy and light-holy flesh, the omer\'s remainder, the two loaves, the showbread, '
                    'meal-offering remainders — "burnt offering" = what is destined for the flames (Zevachim 14:3)',
                    ['exempt'])
    if q == 'ten_acts':
        return cell('exempt', M, SA + 'Chapter 10 10 — the pourer, blender, breaker, salter, waver, presenter, '
                    'table-arranger, lamp-tender, handful-taker, blood-receiver: only an act that COMPLETES a service '
                    '("who raises") is liable (Zevachim 14:3)', ['exempt'])
    if q == 'no_service_offenses':
        return cell('no_liability_for_non_priest_impurity_garments_washing', I, 'Zevachim 14:3 — the Temple-service '
                    'offenses attach inside the door (17:4-6: the priest throws the blood AT the altar)', [FX.NONE])
    if q == 'cross_cases':
        s_in, r_out = k.get('slaughtered'), k.get('raised')
        if s_in == 'inside' and r_out == 'outside':
            return cell(['liable_R._Yosei_HaGelili', 'liable_sages'], M, SA + 'Chapter 10 6 — slaughtered inside, '
                        'raised outside: liable (both)', ['karet_cut_off'])
        return cell(['exempt_R._Yosei_HaGelili', 'liable_sages'], M, SA + 'Chapter 10 6 — slaughtered outside and '
                    'raised outside: R. Yosei the Galilean exempt (he raised the disqualified); the sages liable '
                    '(Zevachim 13:1)', ['karet_cut_off'])
    if q == 'for_commoner':
        act = k.get('act')
        if act == 'slaughter':
            return cell('liable', M, 'Zevachim 13:3 — 17:4\'s reckoning stands without "to the LORD"; the raising '
                        'clause 17:9 "to PERFORM it to the LORD" conditions the raising (the two clauses\' tokens) [MOVE]',
                        ['blood_reckoned'])
        return cell('exempt', M, 'Zevachim 13:3 — raising for a common person: 17:9 "to the LORD" not met', ['exempt'])
    if q == 'per_raising':
        return cell(['per_raising_R._Shimon', 'one_R._Yosei_altar_top_only'], M, SA + 'Chapter 10 11 — raised and '
                    'raised again; R. Yosei: not until the altar-top; R. Shimon: even on a rock (Chapter 9 7)',
                    ['karet_cut_off'])
    if q == 'receivable':
        return cell('liable_if_the_class_is_receivable_inside', M, SA + 'Chapter 10 5 — "to perform it": the lodged, '
                    'the exited, the impure, the wrong-time and wrong-place slaughtered... liable IF receivable inside '
                    '(Zevachim 13:4: disqualified IN sanctity)', ['karet_cut_off'])
    if q == 'olive':
        amt = k.get('amount')
        if amt == 'olive':
            return cell(['liable', 'R._Elazar_until_the_whole'], M, SA + 'Chapter 10 4 + 10 8 — an olive of the burnt '
                        'offering, the fat portions, the handful, the frankincense, the incense, the three meal '
                        'offerings; R. Elazar: the whole (Zevachim 13:4)', ['karet_cut_off'])
        return cell('exempt', M, SA + 'Chapter 10 8 — less than an olive; "it" = the whole (Zevachim 13:4)', ['exempt'])
    if q == 'left_an_olive':
        return cell('liable', M, 'Zevachim 13:4 — offered inside and left an olive, offered outside: the remainder is '
                    'still fire-destined', ['karet_cut_off'])
    if q == 'lacking_any':
        return cell('exempt', M, 'Zevachim 13:4 — lacking any amount: not receivable inside', ['exempt'])
    if q == 'unscooped':
        return cell('exempt', M, 'Zevachim 13:5 — a meal offering not yet scooped: no fire-portion exists (' + SA +
                    'Chapter 10 4, 10 9)', ['exempt'])
    if q == 'scooped_returned':
        return cell('liable', M, 'Zevachim 13:5 — scooped and the handful returned into it: the fire-portion exists',
                    ['karet_cut_off'])
    if q == 'handful_frankincense_one':
        return cell(['liable', 'R._Elazar_until_the_second'], M, 'Zevachim 13:6 — one of the two outside; one in and '
                    'one out — liable', ['karet_cut_off'])
    if q == 'part_of_blood':
        return cell('liable', M, SA + 'Chapter 10 3 — the BLOOD by "or sacrifice" (17:8); Zevachim 13:6: throwing part '
                    'of the blood outside; R. Nechemia: the remainder; R. Elazar: the water libation', ['karet_cut_off'])
    if q == 'fitness_path':
        rite, place = k['rite'], k['place']
        # pinching is the INSIDE rite of the bird; slaughter is its OUTSIDE-liable act (Section 6 4)
        inside_valid = (rite == 'pinched' and place == 'inside')
        outside_act = (rite == 'slaughtered' and place == 'outside')
        if inside_valid:
            return cell('liable', M, 'Zevachim 13:7 — pinched inside, raised outside: a fit bird raised outside '
                        '(the receivable test, ' + SA + 'Chapter 10 5)', ['karet_cut_off'])
        if rite == 'pinched':
            return cell('exempt', M, 'Zevachim 13:7 — pinched outside: nothing (' + SA + 'Chapter 12 10: only the '
                        'inside-pinched permits) — the raised thing is not-in-sanctity disqualified', ['exempt'])
        if outside_act:
            return cell('liable', M, 'Zevachim 13:7 — slaughtered outside (the outside offense, Section 6 4) and '
                        'raised outside: the outside slaughter is that bird\'s fit way, so its raising counts',
                        ['karet_cut_off'])
        return cell('exempt', M, 'Zevachim 13:7 — slaughtered inside (no rite for a bird inside) and raised outside: '
                    '"the way of its fitness outside is its exemption inside"', ['exempt'])
    if q == 'two_cups':
        seq = k['seq']
        if seq == ('outside', 'inside') and k.get('cups') == 1:
            return cell('liable', M, 'Zevachim 13:8 — one cup: the whole was fit to come inside', ['karet_cut_off'])
        if k.get('cups') == 1:
            return cell('liable', M, 'Zevachim 13:8 — one cup, inside then outside: the same', ['karet_cut_off'])
        if seq == ('inside', 'inside'): return cell('exempt', M, 'Zevachim 13:8 — both inside', ['exempt'])
        if seq == ('outside', 'outside'): return cell('liable', M, 'Zevachim 13:8 — both outside', ['karet_cut_off'])
        if seq == ('inside', 'outside'):
            return cell('exempt', M, 'Zevachim 13:8 — inside then outside: the second cup is remainder', ['exempt'])
        return cell('liable_for_the_outer_the_inner_atones', M, 'Zevachim 13:8 — outside then inside: the outer cup '
                    'was fit when thrown; the inner atones (the lost-and-replaced sin offering parable)',
                    ['karet_cut_off', 'atoned_forgiven'])
    raise ValueError(q)

def platform(q, **k):
    ERAS = [('before_the_Tabernacle', 'permitted', 'firstborn'), ('the_Tabernacle', 'forbidden', 'priests'),
            ('Gilgal', 'permitted', 'priests'), ('Shiloh', 'forbidden', 'priests'), ('Nob_and_Gibeon', 'permitted', 'priests'),
            ('Jerusalem', 'forbidden_forever', 'priests')]
    if q == 'eras':
        return cell([(e, s) for e, s, _ in ERAS], P, 'Zevachim 14:4-8 — 17:3-7\'s ban attaches to the tent door\'s '
                    'existence (' + SA + 'Chapter 9 4 the era split; 9 9 "eternal statute" = the eternal house); the '
                    'sequence by Deut 12:9 "the rest and the inheritance" [IMPORT] (Shiloh the rest, Jerusalem the '
                    'inheritance)', ['disqualified'])
    if q == 'service_by':
        return cell(['firstborn_before', 'priests_after'], P, 'Zevachim 14:4 — Exod 24:5 / Num 3:12 [IMPORT]', [FX.NONE])
    if q == 'consecrated_offered':
        c_era, o_era = k['consecrated'], k['offered']
        if c_era == 'ban' and o_era == 'ban':
            return cell('positive_negative_and_karet', M, SA + 'Chapter 9 4-5 — consecrated in the ban era, offered '
                        'outside in the ban era (Zevachim 14:9)', ['karet_cut_off'])
        if c_era == 'permit' and o_era == 'ban':
            return cell('positive_and_negative_no_karet', M, 'Zevachim 14:9 — consecrated under the permit', ['exempt'])
        return cell('positive_only', M, 'Zevachim 14:9 — offered under the permit: "they shall bring them" (17:5)',
                    [FX.NONE])
    if q == 'classes':
        return cell(['sages_burnt_and_shelamim_only', 'R._Meir_whatever_comes_by_vow'], M, (SA + 'Chapter 9 5-6 — 17:5 '
                    '"and slaughter them as SHELAMIM"; the burnt offering amplified; R. Meir adds meal offerings and '
                    'nazirite birds — the two types CALLED cold_run_offerings.dispatch: shelamim window %r, olah '
                    'disposition %r [IMPORT, live call]') % (SHEL_ROW['window']['v'], OLAH_ROW['disposition']['v']),
                    ['accepted'])
    if q == 'no_priest':
        return cell('even_converts_women_slaves_serve', M, SA + 'Chapter 9 7 — priestly throwing AT THE ALTAR only '
                    '(17:6); Zevachim 14:10 lists priesthood among the differences', [FX.NONE])
    if q == 'no_fragrance':
        return cell('not_on_a_platform', M, SA + 'Chapter 9 7 — "a pleasing fragrance" (17:6) at the altar; Onkelos '
                    '"to be received with favor"; Zevachim 14:10', [FX.NONE])
    if q == 'rock':
        return cell(['R._Meir_even_a_rock', 'R._Yishmael_a_built_altar'], M, SA + 'Chapter 9 7', [FX.NONE])
    if q == 'differences':
        return cell(['laying_on', 'north_slaughter', 'blood_around', 'waving', 'presenting', 'priesthood',
                     'service_garments', 'service_vessels', 'pleasing_fragrance', 'blood_partition', 'washing'], A,
                    'Zevachim 14:10 — the individual\'s platform vs the public\'s; R. Yehuda: no meal offering on a '
                    'platform; time, notar, impurity equal', [FX.NONE])
    if q == 'demons':
        return cell('the_demons', I, '17:7 "to the hairy ones" — Onkelos: to the DEMONS; ' + SA + 'Chapter 9 8; '
                    '"after whom they stray" amplifies all foreign worship', [FX.NONE])
    if q == 'no_karet_for_platform':
        return cell('no_karet_for_the_platform_offense_itself', M, SA + 'Chapter 9 9 — "this to them"', [FX.NONE])
    raise ValueError(q)

# ---- F4: THE BLOOD BAN, ITS ATONEMENT, AND THE COVERING (17:10-14; Chullin 6) ----
def blood(q, **k):
    if q == 'ban':
        return cell('karet', I, '17:10 "who eats ANY blood... I will set My face against the soul that eats the blood '
                    'and cut her off"; 17:14 "all who eat it shall be cut off" (soul tokens %s)' % (c_nefesh17,),
                    ['face_set_against', 'karet_cut_off'])
    if q == 'which_blood':
        return cell(['sages_lifeblood_only', 'R._Yehuda_any_blood'], M, SA + 'Section 7 3 — "any blood": R. Yehuda '
                    'lifeblood and exuded, common and consecrated; the sages: karet only on LIFEBLOOD (17:11 "the '
                    'life of the flesh is IN the blood")', ['karet_cut_off'])
    if q == 'eater_not_feeder':
        return cell('the_eater_not_the_feeder', I, '17:10 "the soul that EATS" — ' + SA + 'Section 7 4; 7 6: warn the '
                    'great over the small (no feeding children), but the child not cut off through them', ['karet_cut_off'])
    if q == 'karet_own_eating':
        return cell('karet_rides_only_ones_own_eating', I, '17:14 "ALL WHO EAT IT shall be cut off" — ' + SA +
                    'Section 7 7 (not through the small nor through other great)', ['karet_cut_off'])
    if q == 'atones':
        return cell('one_gift_atones_on_the_altar_exuded_blood_nothing', I, '17:11 "I have given it to you on the '
                    'ALTAR to atone for your souls, for the blood atones BY THE LIFE" — ' + SA + 'Section 7 5: one gift '
                    'atones after the fact; anywhere ON the altar, not its ground; exuded blood achieves nothing; '
                    'Onkelos "the blood FOR the life atones"', ['atoned_forgiven'])
    if q == 'lashes':
        return cell('lashed_when_warned', P, 'Makkot 3:2 — the eater of blood in the lash list: the warned karet-class '
                    'negative is lashed (Deut 25:2-3 [IMPORT]); 3:15: the lashed are discharged of their karet '
                    '(R. Chananya b. Gamliel)', ['lashes'])
    if q == 'convert':
        return cell('convert_bound_as_the_citizen', I, '17:10, 17:12 "and the convert who sojourns among you" (%s)'
                    % (c_ger,), ['karet_cut_off'])
    raise ValueError(q)

def covering(q, **k):
    if q == 'species':
        sp = k.get('species')
        if sp in ('wild', 'bird'):
            return cell('cover_owed', I, '17:13 "who hunts a catch of WILD ANIMAL or BIRD which may be eaten... pour '
                        'out its blood and cover it with dust" — the two nouns (%s)' % (c_cover,), ['cover_owed'])
        if sp == 'beast':
            return cell('no_covering', I, '17:13 — the domestic beast is ABSENT from the clause (%s): its blood goes '
                        'uncovered' % (c_cover[3],), [FX.NONE])
        if sp == 'koy':
            return cell('cover_no_blessing_doubt', D, 'Chullin 6:1 — the koy covered because it is a DOUBT (the '
                        'boundary species: data); not slaughtered on a festival', ['cover_owed'])
        if sp == 'impure_bird':
            return cell('no_covering', M, '17:13 "which may be EATEN" — ' + SA + 'Chapter 11 3: the impure bird '
                        'excluded (re-carved from the garment-defiling beast)', [FX.NONE])
    if q == 'where':
        return cell('everywhere_with_and_without_the_House', I, '17:13 binds the PERSON ("any man... who hunts"), '
                    'where 17:3-9 bind the tent door — Chullin 6:1: in the Land and outside, before the House and '
                    'not', ['cover_owed'])
    if q == 'consecrated':
        return cell('no_covering', M, 'Chullin 6:1 — common, not consecrated: ' + SA + 'Chapter 11 6 (the sages: only '
                    'slaughter fit for eating); the consecrated bird\'s blood is the altar\'s (17:11)', [FX.NONE])
    if q == 'hunted_of_any_kind':
        return cell('bought_inherited_gifted_self_trapped_all_covered', M, '17:13 "a catch" — ' + SA + 'Chapter 11 2: '
                    'from any source (Chullin 6:1 prepared and unprepared); Rabbi\'s conduct rule: flesh by this '
                    'preparation', ['cover_owed'])
    if q == 'failed_slaughter':
        return cell('exempt', M, '17:13 "and POUR OUT" — ' + SA + 'Chapter 11 5: the slaughter that became carrion in '
                    'his hand, the stabber, the wrencher excluded (Chullin 6:2)', ['exempt'])
    if q == 'unfit_slaughter':
        return cell(['R._Meir_liable', 'sages_exempt'], M, SA + 'Chapter 11 6 VERBATIM — found torn, for idolatry, '
                    'common inside, consecrated outside, the stoned bird and beast (Chullin 6:2)', ['cover_owed'])
    if q == 'deaf_imbecile_minor':
        watched = k.get('watched')
        if watched:
            return cell('liable_to_cover', M, 'Chullin 6:3 — others watching: the slaughter stands (Chullin 1 '
                        '[ROUTED]) and "pour out" is met', ['cover_owed'])
        return cell('exempt', M, 'Chullin 6:3 — by themselves: no valid slaughter presumed', ['exempt'])
    if q == 'hundred':
        return cell('one_covering', M, '17:13 "wild animal OR bird" — each of any number: ' + SA + 'Chapter 11 4 '
                    '(a hundred in one place, one covering; beast and bird together, one; R. Yehuda: cover the '
                    'animal\'s first)', ['cover_owed'])
    if q == 'another_saw':
        return cell('liable_to_cover', M, SA + 'Chapter 11 7 — the pourer himself covers, yet all others warned '
                    '("for the life of ALL flesh", 17:14) — Chullin 6:4', ['cover_owed'])
    if q == 'state':
        st = k.get('state')
        if st == 'covered_then_exposed':
            return cell('exempt', M, SA + 'Chapter 11 8 — covered and re-exposed: exempt from re-covering', ['exempt'])
        if st == 'wind_covered':
            return cell('liable_to_cover', M, SA + 'Chapter 11 8 — the WIND covered it: the act must be HIS ("and '
                        'cover it" — the pourer\'s own verb)', ['cover_owed'])
    if q == 'mixed':
        with_ = k.get('with_')
        if with_ == 'water':
            return cell('cover_if_appearance_of_blood', D, 'Chullin 6:5 — the identity test on "ITS blood" with the '
                        'appearance threshold (data)', ['cover_owed'])
        if with_ == 'wine':
            return cell('view_as_water', D, 'Chullin 6:5 — the wine viewed as if water', ['cover_owed'])
        return cell(['view_as_water', 'R._Yehuda_blood_does_not_nullify_blood'], D, 'Chullin 6:5 — a beast\'s or wild '
                    'animal\'s blood', ['cover_owed'])
    if q == 'splashed_knife':
        return cell(['liable', 'R._Yehuda_only_when_no_other_blood'], M, SA + 'Chapter 11 9 — ALL its blood: splashed '
                    'and knife blood (Chullin 6:6)', ['cover_owed'])
    if q == 'materials':
        mat = k.get('material')
        GROWS = {'fine_manure', 'fine_sand', 'lime', 'potters_clay', 'ground_brick', 'ground_stopper', 'ground_stone',
                 'ground_pottery', 'flax_tow', 'sawdust'}
        NOT = {'coarse_manure', 'coarse_sand', 'unground_brick', 'unground_stopper', 'metal_filings', 'flour', 'bran',
               'a_vessel'}
        if mat in GROWS:
            return cell('covers', M, '17:13 "with DUST" — ' + SA + 'Chapter 11 10-11: amplify then restrict, dust-kind '
                        'only; Rabban Shimon ben Gamliel: WHAT GROWS PLANTS covers (Chullin 6:7)', ['cover_owed'])
        if mat in NOT:
            return cell('does_not_cover', M, SA + 'Chapter 11 10 — not vessels or stones, not metal filings, flour, '
                        'bran; the coarse kinds (Chullin 6:7)', [FX.NONE])
    if q == 'not_with_the_foot':
        return cell('not_with_the_foot_the_pourer_covers', M, SA + 'Chapter 11 7 — "that the commandments not be '
                    'despised upon him"', ['cover_owed'])
    if q == 'festival':
        return cell(['Shammai_dig_with_the_spade', 'Hillel_only_with_prepared_dust', 'both_after_the_fact'], A,
                    'Beitzah 1:2 (= Eduyot 4:2) — the covering duty against the festival\'s work ban (Exod 12:16 '
                    '[IMPORT]); the prepared-dust parameter', ['cover_owed'])
    raise ValueError(q)

# ---- F5: THE CARCASS-EATER (17:15-16) ----------------------------------
def carcass(q, **k):
    if q == 'who':
        return cell('citizen_and_convert_not_the_resident_alien', I, ('17:15 "the citizen and the convert" (%s) — ' + SA +
                    'Chapter 12 1 (the covenant member)') % (c_ger[4],), ['impure_until_evening'])
    if q == 'effect':
        return cell('washes_garments_bathes_impure_until_evening_then_pure', I, '17:15 "he shall wash his garments and '
                    'bathe in water and be impure until evening, and be pure"', ['washes_and_bathes', 'impure_until_evening'])
    if q == 'failure':
        organ = k.get('organ')
        if organ == 'body':
            return cell('karet', M, '17:16 "if he does not wash and does not bathe his flesh — he shall bear his '
                        'iniquity" — ' + SA + 'Chapter 12 13, 12 15: the body-wash failure = KARET (the Others\' '
                        'bear-iniquity analogy); the clause speaks of SANCTUARY defilement (12 14)', ['karet_cut_off', 'bears_sin'])
        return cell('forty_lashes', M, SA + 'Chapter 12 13 — failing to launder the GARMENTS = forty: one verse, two '
                    'organs, two sanctions', ['lashes'])
    if q == 'minimum':
        return cell('olive', D, SA + 'Chapter 12 2 — eating = an olive-bulk (the data channel); "carcass" excludes '
                    'beak, claws, wings, feathers, eggs', [FX.NONE])
    if q == 'where_defiles':
        return cell('swallow_house_only', M, SA + 'Chapter 12 3-4 — THE SWALLOW-HOUSE: neither in the bowels nor in '
                    'the mouth, only at the throat ("soul" = where the soul-house is); nor on the way out (Zavim 5:9 '
                    'routed here)', ['defiles_garments'])
    if q == 'beast_carcass':
        return cell('defiles_before_eating_no_swallow_rule', M, SA + 'Chapter 12 5-6 — the beast carcass from Lev '
                    '22:8\'s carve [IMPORT — L5]; "by it" — the bird alone at the throat', ['impure_until_evening'])
    if q == 'impure_species':
        return cell(['excluded_sages_carcass_AND_torn', 'excluded_R._Yehuda'], M, SA + 'Chapter 12 7 — a species that '
                    'HAS a torn-state is meant; the impure bird has none', [FX.NONE])
    if q == 'slaughtered':
        return cell('excluded', M, SA + 'Chapter 12 8 — R. Yehuda: "torn" is never redundant, so "carcass" comes to '
                    'exclude the slaughtered', [FX.NONE])
    if q == 'pinching':
        return cell(['purifies_R._Meir', 'does_not_R._Yosei_dayo'], M, SA + 'Chapter 12 9 — DAYO: enough for the bird '
                    'to be like the beast carcass (slaughter purifies, pinching does not); the inside-pinched excluded '
                    '(12 10: it permits the forbidden)', [FX.NONE])
    if q == 'equality_test':
        return cell('what_binds_citizen_and_convert_equally', M, SA + 'Chapter 12 11 — the Others\' test', [FX.NONE])
    if q == 'garments_boundary':
        return cell('garments_and_vessels_as_garments_yes_man_and_earthenware_no', M, SA + 'Chapter 12 12 — the '
                    'eater with one hand on the oven and one on his fellow: both stay pure (12 13)', ['defiles_garments'])
    if q == 'lashes_for_eating':
        return cell('lashed', P, 'Makkot 3:2 — the eater of carcass and torn: the ban is Deut 14:21 / Exod 22:30 '
                    '[IMPORT]; 17:15 writes the impurity, not the ban', ['lashes'])
    raise ValueError(q)

# ---- F6: THE FRAME, THE LAND, THE SPECIES (18:1-5, 24-30; 20:7-8, 22-26) ----
def frame(q, **k):
    if q == 'nomoi':
        return cell('their_civil_customs_not_their_buildings', M, '18:3 "in their STATUTES you shall not walk" — '
                    'Onkelos: their NOMOI; ' + SA + 'Section 8 8 / Chapter 13 8: theaters, circuses, the Amorite '
                    'ways; NOT their buildings and plantings', [FX.NONE])
    if q == 'amorite_ways':
        return cell(['R._Meir_remedy_permitted', 'sages_forbidden_even_on_a_weekday'], M, 'Shabbat 6:10 — the '
                    'locust\'s egg, the fox\'s tooth, the nail from the crucified: the sages — the ways of the Amorite '
                    '(the customs class of 18:3; the item list the Tosefta\'s, outside scope)', [FX.NONE])
    if q == 'canon_channel':
        return cell({'judgments': 'dinim', 'statutes': 'midrashot', 'keep': 'Mishnah', 'walk_in_them': 'the_deed'}, M,
                    SA + 'Section 8 9 — 18:4 read as the four strata (the data channel\'s self-label)', [FX.NONE])
    if q == 'two_classes':
        return cell({'judgments': 'reason_would_have_written', 'statutes': 'decreed_no_permission_to_object'}, M,
                    SA + 'Chapter 13 9 — 18:4-5: theft, the unions, idolatry, blasphemy, bloodshed vs pig, mixed '
                    'cloth, the levirate release, the leper, the red cow, the dispatched goat', [FX.NONE])
    if q == 'live_by_them':
        pub = k.get('public')
        if pub:
            return cell('sanctify_the_Name', M, '18:5 "and LIVE by them — not die by them" + 22:32 "you shall not '
                        'profane My holy Name" [IMPORT]: ' + SA + 'Chapter 13 13 — in public he sanctifies it', [FX.NONE])
        return cell('transgress_and_live', M, '18:5 — told privately "worship or be killed": he transgresses and '
                    'lives (' + SA + 'Chapter 13 13); Onkelos 18:5 "to eternal life" beside it', [FX.NONE])
    if q == 'sit_and_abstain':
        return cell('rewarded_as_one_who_did_a_commandment', I, 'Makkot 3:15 — R. Shimon FROM ITS OWN PLACE: "the '
                    'souls that DO shall be cut off" (18:29) and "which a man shall DO and live" (18:5) — the two DO '
                    'tokens censused (%s): whoever sits and does not transgress is rewarded' % (c_do,), [FX.NONE])
    if q == 'lashes_discharge_karet':
        return cell(['discharged_R._Chananya_b._Gamliel'], A, 'Makkot 3:15 — "your brother shall be degraded... once '
                    'lashed he is your brother" (Deut 25:3 [IMPORT])', ['lashes'])
    if q == 'land':
        return cell('the_land_vomits_its_inhabitants', I, ('18:25, 18:28, 20:22 — the vomit verb at %s: "I visited its '
                    'iniquity upon it" (Onkelos: I reckoned); ' + SA + 'Chapter 13 16, 13 19 — the opened ledger, the '
                    'land liable to exile; ' + SK + 'Chapter 12 14 the prince\'s stomach') % (c_vomit,), ['land_vomits'])
    if q == 'all_or_any':
        return cell('all_or_any_one', M, '18:24 "defile not yourselves in ALL these" — ' + SA + 'Chapter 13 16, 13 18: '
                    'in all or in any one; the full inclusion census', ['karet_cut_off'])
    if q == 'karet_persons':
        return cell('man_and_woman_the_doers_not_the_approach', I, '18:29 "the SOULS that DO them shall be cut off" — '
                    + SA + 'Chapter 13 20-21: both sexes; the doers, not the mere approach', ['karet_cut_off'])
    if q == 'court_warned':
        return cell('the_court_warned_over_the_charge', M, '18:30 "keep My CHARGE" — ' + SA + 'Chapter 13 22 (Onkelos: '
                    'the charge of My Word); 13 4: "say to them" a warning to the court', [FX.NONE])
    if q == 'disqualified':
        return cell('disqualified_from_following_Me', M, SA + 'Chapter 13 22 — "defile yourselves in them and you are '
                    'DISQUALIFIED"', ['disqualified'])
    if q == 'separate_species':
        kind = k.get('kind')
        v = PURE_BEAST if kind == 'pure' else IMPURE_BEAST
        return cell(v, P, '20:25 "SEPARATE between the pure beast and the impure" — CALLED cold_run_shemini.classify '
                    '(the Lev 11 signs) -> %r' % v, [FX.NONE])
    if q == 'majority_threshold':
        return cell('most_of_the_windpipe_vs_half_a_hairs_breadth', M, SK + 'Chapter 9 9 — "between the pure FOR YOU '
                    'and the impure FOR YOU": most of the windpipe cut vs half — a hair\'s breadth between (the '
                    'transmitted tolerance = data)', [FX.NONE])
    if q == 'compliance':
        return cell('I_can_but_my_Father_decreed', M, SK + 'Chapter 9 12 — R. Elazar ben Azariah; Onkelos 20:26 "to '
                    'be servants before Me"', [FX.NONE])
    if q == 'sanctify_yourselves':
        return cell('the_idolatry_separation', M, SK + 'Chapter 10 2 — 20:7 read of idolatry specifically (19:2 '
                    'carries the all-commandments reading)', [FX.NONE])
    if q == 'festival_reading':
        return cell('Acharei_Mot_on_the_Day', A, 'Megillah 3:5 — the Day of Atonement reads Lev 16 (the parashah\'s '
                    'name; the moadim engine\'s context)', [FX.NONE])
    raise ValueError(q)

# ---- (2) TEST DATA — the Mishnah rows, read whole from the shelf ------
def load(t):
    d = json.load(open('<repo-old>/Data/mishnah_%s_he.json' % t))
    return d['text'] if isinstance(d, dict) and 'text' in d else d
SHELF = {t: load(t.lower()) for t in ('Sanhedrin', 'Makkot', 'Yevamot', 'Chullin', 'Zevachim', 'Keritot', 'Kiddushin',
                                      'Megillah', 'Beitzah', 'Shabbat')}
def mrow(book, ch, m, must):
    txt = strip(SHELF[book][ch - 1][m - 1])
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, book, ch, m)
SHEET = [
    ('Sanhedrin', 1, 4, 'והרגת'), ('Sanhedrin', 7, 1, 'סקילה'), ('Sanhedrin', 7, 2, 'בקי'), ('Sanhedrin', 7, 3, 'הנחנקין'),
    ('Sanhedrin', 7, 4, 'הנסקלין'), ('Sanhedrin', 7, 7, 'למלך'), ('Sanhedrin', 7, 8, 'בשם'), ('Sanhedrin', 7, 9, 'בחנק'),
    ('Sanhedrin', 9, 1, 'הנשרפין'), ('Sanhedrin', 9, 3, 'בקלה'), ('Sanhedrin', 9, 4, 'בחמורה'), ('Sanhedrin', 11, 1, 'הנחנקין'),
    ('Sanhedrin', 11, 6, 'בחנק'),
    ('Makkot', 3, 1, 'הלוקין'), ('Makkot', 3, 2, 'ודם'), ('Makkot', 3, 15, 'כרתות'),
    ('Yevamot', 1, 1, 'עשרה'), ('Yevamot', 1, 2, 'מאה'), ('Yevamot', 1, 3, 'שש'), ('Yevamot', 1, 4, 'הצרות'),
    ('Yevamot', 2, 1, 'בעולמו'), ('Yevamot', 2, 2, 'שירצה'), ('Yevamot', 2, 3, 'ערוה'), ('Yevamot', 2, 5, 'קללתו'),
    ('Yevamot', 3, 1, 'ארבעה'), ('Yevamot', 3, 2, 'באחותה'), ('Yevamot', 3, 3, 'יבמתה'), ('Yevamot', 3, 4, 'פוטר'),
    ('Yevamot', 3, 5, 'אוי'), ('Yevamot', 3, 6, 'נכרית'), ('Yevamot', 3, 7, 'עולמית'), ('Yevamot', 3, 9, 'זקת'),
    ('Yevamot', 3, 10, 'החליפו'), ('Yevamot', 11, 1, 'האנוסה'),
    ('Chullin', 6, 1, 'בכוי'), ('Chullin', 6, 2, 'הנוחר'), ('Chullin', 6, 3, 'חרש'), ('Chullin', 6, 4, 'הרוח'),
    ('Chullin', 6, 5, 'במים'), ('Chullin', 6, 6, 'הסכין'), ('Chullin', 6, 7, 'צמחין'),
    ('Zevachim', 13, 1, 'העליה'), ('Zevachim', 13, 3, 'להדיוט'), ('Zevachim', 13, 4, 'כזית'), ('Zevachim', 13, 5, 'נקמצה'),
    ('Zevachim', 13, 6, 'הלבונה'), ('Zevachim', 13, 7, 'המולק'), ('Zevachim', 13, 8, 'כוסות'), ('Zevachim', 14, 1, 'המשתלח'),
    ('Zevachim', 14, 2, 'הרובע'), ('Zevachim', 14, 3, 'זמן'), ('Zevachim', 14, 4, 'בבכורות'), ('Zevachim', 14, 5, 'לגלגל'),
    ('Zevachim', 14, 6, 'לשילה'), ('Zevachim', 14, 7, 'לנוב'), ('Zevachim', 14, 8, 'לירושלים'), ('Zevachim', 14, 9, 'כרת'),
    ('Zevachim', 14, 10, 'סמיכה'),
    ('Keritot', 1, 1, 'ושש'), ('Keritot', 1, 2, 'תלוי'), ('Keritot', 3, 6, 'חמותו'),
    ('Kiddushin', 2, 7, 'מקדשות'), ('Megillah', 4, 9, 'בארמיותא'), ('Megillah', 3, 5, 'מות'), ('Beitzah', 1, 2, 'בדקר'),
    ('Shabbat', 6, 10, 'האמורי'),
]
for b, ch, m, must in SHEET:
    mrow(b, ch, m, must)
print('answer sheet: %d Mishnah rows verified by their own tokens (Sanhedrin 7/9/11, Makkot 3, Yevamot 1-3, Chullin 6, '
      'Zevachim 13-14, Keritot 1 read whole — the topic docket)' % len(SHEET))

TESTS = [
 # ---- THE SANCTIONS MATRIX (Lev 18 warning, Lev 20 sanction, mode, karet) ----
 ('Lev 18:8 / 20:11 — the father\'s wife: stoning (the formula), karet', sanction('father_wife'), (8, 11, 'stoning', True)),
 ('Lev 18:7 / 20:11 — the mother: stoning via the father\'s-wife clause', sanction('mother'), (7, 11, 'stoning', True)),
 ('Lev 18:15 / 20:12 — the daughter-in-law: stoning', sanction('daughter_in_law'), (15, 12, 'stoning', True)),
 ('Lev 18:22 / 20:13 — the male: stoning', sanction('male'), (22, 13, 'stoning', True)),
 ('Lev 18:23 / 20:15 — the man with a beast: stoning by analogy', sanction('man_beast'), (23, 15, 'stoning', True)),
 ('Lev 18:23 / 20:16 — the woman with a beast: stoning (the formula)', sanction('woman_beast'), (23, 16, 'stoning', True)),
 ('Lev 18:17 / 20:14 — a woman and her mother: BURNING (named)', sanction('woman_and_mother'), (17, 14, 'burning', True)),
 ('Lev 18:20 / 20:10 — adultery: strangling (the bare death)', sanction('adultery'), (20, 10, 'strangling', True)),
 ('Lev 18:9 / 20:17 — the sister: karet, no court death', sanction('sister'), (9, 17, None, True)),
 ('Lev 18:19 / 20:18 — the menstruant: karet both', sanction('menstruant'), (19, 18, None, True)),
 ('Lev 18:12 / 20:19 — the father\'s sister: bear iniquity = karet', sanction('father_sister'), (12, 19, None, True)),
 ('Lev 18:13 / 20:19 — the mother\'s sister', sanction('mother_sister'), (13, 19, None, True)),
 ('Lev 18:14 / 20:20 — the uncle\'s wife: childless', sanction('uncle_wife'), (14, 20, None, True)),
 ('Lev 18:16 / 20:21 — the brother\'s wife: niddah, childless', sanction('brother_wife'), (16, 21, None, True)),
 ('Lev 18:18 — the wife\'s sister: no Lev 20 seat, 18:29\'s karet', sanction('wife_sister'), (18, None, None, True)),
 ('Lev 18:21 / 20:2-3 — Molech: stoning named + karet', sanction('molech'), (21, 2, 'stoning', True)),
 ('Lev 20:27 — the ghost-pit bearer: stoning named', sanction('ov_bearer'), (None, 27, 'stoning', True)),
 ('Lev 20:9 — the curser: stoning, no karet (Keritot 1:1 does not list him)', sanction('curser'), (None, 9, 'stoning', False)),
 ('the decoder\'s ground: 20:27 alone names a mode beside the formula', census('formula_grounding'), '20:27_names_stoning_beside_the_formula'),
 # ---- the censuses recomputed ----
 ('Sanhedrin 7:4 — this span\'s nine of the stoned census (computed)', census('stoned'),
  ['his daughter-in-law', "his father's wife", 'his mother', 'the Molech giver', 'the curser of father and mother',
   'the ghost-pit or familiar bearer', 'the male', 'the man with a beast', 'the woman bringing a beast']),
 ('Sanhedrin 9:1 — the burned of this span', census('burned'), ['a woman and her mother']),
 ('Sanhedrin 11:1 — the strangled of this span', census('strangled'), ["a man's wife"]),
 ('Makkot 3:1 — THE LASH LIST = the karet unions without a court death (computed)', census('lashes'),
  ["his brother's wife", "his father's brother's wife", "his father's sister", "his mother's sister", 'his sister',
   "his wife's sister", 'the menstruant']),
 ('Keritot 1:1 — this span supplies twenty of the thirty-six (computed)', census('karet_count'), 20),
 ('Sanhedrin 9:1 — "a woman and her daughter" includes NINE (computed from 18:17\'s pairs + 18:10)', burned_nine(),
  ["her daughter's daughter", "her son's daughter", 'his daughter', "his daughter's daughter", "his father-in-law's mother",
   'his mother-in-law', "his mother-in-law's mother", "his son's daughter", "his wife's daughter"]),
 ('Sifra Kedoshim 10 15 / Onkelos 20:14 — the burning\'s scope', burning_scope(), ['R._Yishmael_him_and_one', 'R._Akiva_both', 'Onkelos_plural']),
 ('Sanhedrin 7:4 — the mother\'s double count', double_count('mother'), ['qua_mother', 'qua_fathers_wife']),
 ('Sanhedrin 7:4 — the father\'s wife: two names, in life or after death, betrothal or marriage', double_count('father_wife'),
  ['qua_fathers_wife', 'qua_married_woman', 'in_life_or_after_death', 'from_betrothal_or_marriage']),
 ('Sanhedrin 7:4 — the daughter-in-law likewise', double_count('daughter_in_law'),
  ['qua_daughter_in_law', 'qua_married_woman', 'in_life_or_after_death', 'from_betrothal_or_marriage']),
 ('Sanhedrin 7:4 — why the beast dies (two reasons)', beast('why'), ['stumbling_came_through_it', 'not_walk_the_market_naming_the_sin']),
 ('Sanhedrin 1:4 — the beast partners by twenty-three from our verses', beast('court'), 23),
 ('Sifra Kedoshim 11 2 — Exod 22:18 freed to the passive', beast('passive_warning'), 'Exod_22:18_freed_to_the_passive'),
 ('Lev 18:23 — the woman\'s own warning written', beast('woman_warning'), '18:23_a_woman_shall_not_stand_before_a_beast'),
 ('Sanhedrin 7:1 / 9:3 — the two recorded severity orders', severity('orders'),
  {'sages': ['stoning', 'burning', 'killing', 'strangling'], 'R._Shimon': ['burning', 'stoning', 'strangling', 'killing']}),
 ('Sanhedrin 9:4 — two deaths: the severer (the father\'s wife who is a married woman)', severity('two_deaths', modes=['stoning', 'strangling']), 'stoning'),
 ('Sanhedrin 9:4 — burning and strangling: burning', severity('two_deaths', modes=['burning', 'strangling']), 'burning'),
 ('Sanhedrin 9:3 — the stoned mixed among the burned: the sages — burning (the lightest)', severity('mixed', modes=['stoning', 'burning']), 'burning'),
 ('Sanhedrin 9:3 — R. Shimon\'s arm: stoning is the lighter', severity('mixed', modes=['stoning', 'burning'], arm='R._Shimon'), 'stoning'),
 ('Sanhedrin 9:3 — the killed among the strangled: the sages — strangling', severity('mixed', modes=['killing', 'strangling']), 'strangling'),
 ('Sanhedrin 9:3 — a murderer mixed among others', severity('murderer_mixed'), ['all_exempt', 'R._Yehuda_confined']),
 ('Sanhedrin 7:2-3 + Sifra Kedoshim 4 4 — the three procedures', severity('procedure'),
  {'burning': 'dung_to_the_knees_hard_scarf_in_soft_the_lit_wick_into_the_mouth',
   'strangling': 'dung_to_the_knees_hard_scarf_in_soft_two_pull_until_the_soul_departs',
   'stoning': 'one_stone_suffices_not_in_his_clothing'}),
 # ---- THE LEVIRATE TABLE (computed) ----
 ('Yevamot 1:1 — THE FIFTEEN WOMEN (computed by composition with the paternal brother)', levirate('fifteen'),
  ["her daughter's daughter", "her son's daughter", 'his daughter', "his daughter's daughter", 'his daughter-in-law',
   "his father-in-law's mother", "his maternal brother's wife", 'his maternal sister', "his mother's sister",
   'his mother-in-law', "his mother-in-law's mother", "his son's daughter", "his wife's daughter", "his wife's sister",
   'the wife of a brother not in his world']),
 ('Yevamot 1:3 — THE SIX SEVERER (computed: forbidden to the brother too)', levirate('six'),
  ["his father's brother's wife", "his father's sister", "his father's wife", 'his mother', "his paternal brother's wife",
   'his paternal sister']),
 ('the partition: fifteen and six from twenty relations + one import', levirate('count'), (15, 6)),
 ('Yevamot 1:2 — the rival\'s rival, even a hundred', levirate('rival_chain'), 'rival_of_rival_exempt_even_a_hundred'),
 ('Yevamot 1:2 — the ervah must stand at the death', levirate('release_timing'), 'ervah_must_stand_at_the_death'),
 ('Yevamot 2:1 — the brother not in his world (Deut 25:5 import)', levirate('not_in_world'), 'exempt_and_her_rival_exempt'),
 ('Yevamot 2:1-2 — the declaration case', levirate('not_in_world_maamar'), 'release_not_levirate_R._Shimon_either'),
 ('Yevamot 1:4 — the houses on the rivals', levirate('houses'), ['Beit_Shammai_permit_the_rivals', 'Beit_Hillel_forbid']),
 ('Yevamot 2:3 — an ervah: neither release nor levirate', grade(('W', 'SIS')), 'neither_release_nor_levirate'),
 ('Yevamot 2:3 — the menstruant grade likewise', grade('menstruant'), 'neither_release_nor_levirate'),
 ('Yevamot 2:4 — the seconds (scribal): release, not levirate', grade('second_degree'), 'release_not_levirate'),
 ('Yevamot 2:4 — the sanctity bans: release, not levirate', grade('widow_to_high_priest'), 'release_not_levirate'),
 ('Yevamot 2:3 — no ban: release or levirate', grade('stranger'), 'release_or_levirate'),
 ('Yevamot 3:2 — the ervah\'s sister is free', cowives('ervah_sister_free'), 'forbidden_to_her_permitted_to_her_sister'),
 ('Yevamot 3:3 — cross-forbidden: each permitted to the other', cowives('cross'), 'each_forbidden_to_one_permitted_to_the_other'),
 ('Yevamot 3:1 — four brothers, two sisters: the bond as marriage', cowives('zikah_sisters'), 'release_not_levirate_married_first_put_out'),
 ('Yevamot 3:4 — the pair-bans bound to one man', cowives('pair_bans_bound'), 'release_not_levirate_R._Shimon_exempts'),
 ('Yevamot 3:6 — the stranger-married brother cases', cowives('stranger_cases'), 'wifes_sister_exits_and_her_rival'),
 ('Yevamot 3:7, 3:9 — forbidden one hour, forbidden forever', cowives('one_hour'), 'forbidden_forever'),
 ('Yevamot 3:7 — divorced before the death: rivals permitted', cowives('divorced_before'), 'rivals_permitted'),
 ('Yevamot 3:5 — the declaration and the houses', cowives('maamar_houses'), ['Shammai_his_wife_stays', 'Hillel_puts_out_both']),
 ('Yevamot 3:9 — one levir\'s bond, not two', cowives('two_bonds'), 'release_not_levirate_one_levir_not_two'),
 ('Yevamot 3:10 — the swapped brides: four names stack', cowives('swapped_names', married=True, brothers=True, sisters=True, niddot=True),
  ['married_woman_20:10', "brother's_wife_18:16", "wife's_sister_18:18", 'menstruant_18:19']),
 ('Yevamot 3:10 — strangers only: the married-woman name alone', cowives('swapped_names', married=True), ['married_woman_20:10']),
 ('Yevamot 3:10 — the aftermath', cowives('swapped_aftermath'), 'separated_three_months_minors_returned_priestesses_barred'),
 ('Keritot 3:6 — the mother-in-law\'s SEVEN names (enumerated)', names([('W', 'M'), ('S', 'W'), ('W', 'SIS'), ('PB', 'W'), ('FB', 'W'), 'married_woman', 'menstruant']), 7),
 ('Keritot 3:6 — the three are one name', three_are_one(), ['sages_one_name', 'R._Yochanan_ben_Nuri_three']),
 ('Yevamot 11:1 / Sifra Kedoshim 10 12 — the marriage path: the raped woman\'s kin permitted', unions_misc('void_betrothal'), 'neither_betrothed'),
 # ---- MOLECH, THE GHOST-PIT, THE CURSER, THE ADULTERER ----
 ('Sanhedrin 7:7 — handed and passed through fire to Molech: liable', molech('predicate'), 'liable'),
 ('Sanhedrin 7:7 — handed, not passed: exempt', molech('predicate', passed=False), 'exempt'),
 ('Sanhedrin 7:7 — passed, not handed: exempt', molech('predicate', handed=False), 'exempt'),
 ('Sifra Kedoshim 4 3 — not by fire: exempt', molech('predicate', fire=False), 'exempt'),
 ('Sifra Kedoshim 4 3 — not to Molech: exempt', molech('predicate', to_molech=False), 'exempt'),
 ('Lev 20:2 — who stones: the people of the land', molech('who_stones'), 'the_people_of_the_land'),
 ('Sifra Kedoshim 4 6-7 — the seed\'s scope', molech('seed_scope'), ['son', 'daughter', 'grandson', 'granddaughter', 'unfit_seed']),
 ('Lev 20:4-5 — concealed by the court: Heaven\'s docket and the family', molech('concealed'), 'karet_by_Heaven_and_his_family'),
 ('Sifra Kedoshim 4 13-14 — the family: afflictions, not karet', molech('family'), 'afflictions_not_karet'),
 ('Sifra Kedoshim 4 9-11 — the concealment ladder', molech('ladder'), ['one_matter_to_many', 'one_court_to_many', 'lesser_courts_to_the_Sanhedrin_and_capital_law_taken']),
 ('Lev 20:5 — all who stray after him', molech('all_who_stray'), 'all_foreign_services_swept_into_the_karet'),
 ('Sifra Kedoshim 4 8 — the five-effect chain', molech('effects_chain'), ['defiles_the_sanctuary', 'profanes_the_Name', 'removes_the_Presence', 'fells_by_the_sword', 'exiles']),
 ('Megillah 4:9 — the Aramean-ness rendering silenced', molech('translation_gate'), 'silenced_with_rebuke'),
 ('Sifra Kedoshim 4 2 — gentile jurisdictions', molech('gentile_court'), 'their_unions_by_their_law_Israel_unions_by_Israel_law'),
 ('Lev 20:27 — the bearer: stoning named', ov('bearer'), 'stoning'),
 ('Sanhedrin 7:7 — the consulter: warning only', ov('consulter'), 'warning_only'),
 ('Sanhedrin 7:7 — the two defined', ov('definitions'), {'ov': 'the_pitom_speaking_from_the_armpit', 'yidoni': 'speaking_from_the_mouth'}),
 ('Sifra Kedoshim 10 1 — the three-verse completion', ov('three_verses'), {'punishment': '20:27', 'warning': '19:31', 'karet': '20:6'}),
 ('Sifra Kedoshim 9 13 — the bearers\' persons', ov('persons'), ['man', 'woman', 'tumtum', 'androgynous']),
 ('Lev 20:9 — the curser\'s mode', curser('mode'), 'stoning'),
 ('Sanhedrin 7:8 — by the Name: liable', curser('by_the_name'), 'liable'),
 ('Sanhedrin 7:8 — by an appellation: disputed', curser('by_the_name', by_name=False), ['R._Meir_liable', 'sages_exempt']),
 ('Sanhedrin 11:1 — the curser after death liable', curser('after_death'), 'liable'),
 ('Sifra Kedoshim 10 5 — either parent suffices (the joint-vs-several default)', curser('one_parent'), 'either_parent_suffices'),
 ('Sifra Kedoshim 9 1-2 — which parent', curser('which_parent'),
  {'grandfather': 'excluded', 'doubtful_parent': 'excluded', 'convert': 'liable_on_the_mother_R._Yosei_HaGelili', 'shtuki': 'liable_on_the_mother_alone'}),
 ('Yevamot 2:5 — a son from anywhere', curser('son_from_anywhere'), 'liable_except_from_maidservant_or_gentile'),
 ('Sifra Kedoshim 10 7 — the warning\'s three-source argument', curser('warning_source'), 'the_common_side_of_judge_prince_deaf'),
 ('Lev 20:10 — adultery\'s mode: strangling', adultery('mode'), 'strangling'),
 ('Lev 20:10 — both named', adultery('both'), 'the_adulterer_and_the_adulteress'),
 ('Sifra Kedoshim 10 8 — the minor\'s wife: exempt', adultery('whose_wife', wife_of='minor'), 'exempt'),
 ('Sifra Kedoshim 10 8 — the gentile\'s wife: exempt', adultery('whose_wife', wife_of='gentile'), 'exempt'),
 ('Lev 20:10 — his fellow\'s wife: liable', adultery('whose_wife', wife_of='fellow'), 'liable'),
 ('Sanhedrin 11:6 — the threshold: entry to the husband\'s domain', adultery('threshold'), 'from_entry_to_the_husbands_domain_even_before_intercourse'),
 ('Sanhedrin 7:9 — the second partner of the betrothed maiden: strangling', adultery('second_partner'), 'strangling'),
 ('Keritot 1:2 — unwitting: the sin offering (CALLED)', adultery('unwitting'), 'sin_offering'),
 ('Keritot 1:2 — the doubt: the suspended ram (CALLED)', adultery('doubt'), 'suspended_ram'),
 ('Keritot 1:2 — deliberate: karet, no offering (CALLED)', adultery('deliberate_unwitnessed'), 'karet_no_offering'),
 ('Sifra Kedoshim 12 2 — the partial act counts', unions_misc('partial_act'), 'partial_counts_as_complete_for_all'),
 ('Sifra Kedoshim 12 4 — the aunts from either side', unions_misc('aunts_both_sides'), 'mothers_sister_and_fathers_sister_from_either_side'),
 ('Sifra Kedoshim 12 6 — the aunt = the father\'s brother\'s wife only', unions_misc('uncle_wife_bound'), 'fathers_brother_only'),
 ('Sifra Kedoshim 12 8 — the brother\'s wife: the levirate window', unions_misc('brother_wife_window'), 'forbidden_with_children_permitted_childless_by_levirate'),
 ('Lev 20:17 — chesed: the homonym\'s two layers', unions_misc('chesed'), ['disgrace_Onkelos', 'lovingkindness_the_Cain_charter_Sifra']),
 ('Lev 20:17 — both deliberate', unions_misc('sister_both_deliberate'), 'both_deliberate_for_the_mutual_penalty'),
 ('Lev 18:9 / 20:17 — the sister\'s scope', unions_misc('sister_scope'),
  {'paternal_or_maternal': 'both', 'born_home_or_outside': 'keep_her_or_send_her', 'maidservant_or_gentile_daughter': 'excluded'}),
 ('Sifra Kedoshim 11 10, 11 12 — the anti-inference fence complete', unions_misc('no_inference'), ['no_punishing_from_inference', 'no_warning_from_inference']),
 ('Sifra Acharei 13 1 — gentiles and the woman warned', unions_misc('gentile_and_woman_warned'), ['gentiles_warned', 'the_woman_warned']),
 ('Lev 18:7 — the father clause', unions_misc('father_clause'), 'the_male_lying_with_the_father'),
 # ---- OUTSIDE SLAUGHTER AND RAISING ----
 ('Zevachim 13:1 — two offenses, two clauses', outside('two_offenses'), 'liable_for_slaughter_and_liable_for_raising'),
 ('Sifra Acharei 6 1 — Israel liable', outside('who', person='israel'), 'liable'),
 ('Sifra Acharei 6 1 — gentiles not liable, platforms permitted', outside('who', person='gentile'), 'not_liable_and_permitted_a_platform'),
 ('Lev 17:3-4 — where: anywhere but the tent door', outside('where'), 'anywhere_but_the_tent_door'),
 ('Lev 17:4 — no agency', outside('agency'), 'reckoned_to_the_slaughterer_not_his_sender'),
 ('Zevachim 13:3 — two who held the knife: exempt', outside('two_slaughter'), 'exempt'),
 ('Zevachim 13:3 — two who raised: liable (R. Shimon)', outside('two_raise'), ['liable_R._Shimon', 'exempt_R._Yosei']),
 ('Sifra Acharei 9 2 — the individual, not the coerced', outside('individual'), 'individual_not_community_not_coerced_erring_misled'),
 ('Sifra Acharei 6 4 — bird slaughter liable', outside('bird', act='slaughter'), 'liable'),
 ('Sifra Acharei 6 4 — bird pinching not', outside('bird', act='pinch'), 'not_liable'),
 ('Sifra Acharei 6 5 — common animals inside: not this law', outside('common_inside'), 'not_this_law'),
 ('Sifra Acharei 6 6 — Temple-upkeep consecrations excluded', outside('temple_upkeep'), 'excluded'),
 ('Zevachim 14:1 — the dispatched goat outside: exempt', outside('dispatched_goat'), 'exempt'),
 ('Zevachim 14:1 — the red cow burned outside its pit: exempt', outside('red_cow'), 'exempt'),
 ('Zevachim 14:2 — the unfit list: exempt', outside('unfit_list'), 'exempt'),
 ('Zevachim 14:2 — the time-deferred: exempt, R. Shimon a negative', outside('time_deferred'), ['exempt', 'R._Shimon_plain_negative']),
 ('Zevachim 14:3 — the zav\'s sin offering outside before the eighth day: exempt (CALLED)', outside('lacking_time_owner', offering='chatat'), 'exempt'),
 ('Zevachim 14:3 — their burnt offerings outside: liable', outside('lacking_time_owner', offering='olah'), 'liable'),
 ('Zevachim 14:3 — the flesh list exempt', outside('flesh_list'), 'exempt'),
 ('Zevachim 14:3 — the ten acts exempt', outside('ten_acts'), 'exempt'),
 ('Zevachim 14:3 — no service offenses outside', outside('no_service_offenses'), 'no_liability_for_non_priest_impurity_garments_washing'),
 ('Zevachim 13:1 — slaughtered inside, raised outside', outside('cross_cases', slaughtered='inside', raised='outside'), ['liable_R._Yosei_HaGelili', 'liable_sages']),
 ('Zevachim 13:1 — slaughtered outside, raised outside', outside('cross_cases', slaughtered='outside', raised='outside'), ['exempt_R._Yosei_HaGelili', 'liable_sages']),
 ('Zevachim 13:3 — slaughtering for a commoner: liable', outside('for_commoner', act='slaughter'), 'liable'),
 ('Zevachim 13:3 — raising for a commoner: exempt', outside('for_commoner', act='raise'), 'exempt'),
 ('Zevachim 13:3 — raised and raised again', outside('per_raising'), ['per_raising_R._Shimon', 'one_R._Yosei_altar_top_only']),
 ('Zevachim 13:4 — the receivable test', outside('receivable'), 'liable_if_the_class_is_receivable_inside'),
 ('Zevachim 13:4 — an olive: liable (R. Elazar the whole)', outside('olive', amount='olive'), ['liable', 'R._Elazar_until_the_whole']),
 ('Sifra Acharei 10 8 — less than an olive: exempt', outside('olive', amount='less'), 'exempt'),
 ('Zevachim 13:4 — left an olive and offered it outside: liable', outside('left_an_olive'), 'liable'),
 ('Zevachim 13:4 — lacking any amount: exempt', outside('lacking_any'), 'exempt'),
 ('Zevachim 13:5 — the unscooped meal offering: exempt', outside('unscooped'), 'exempt'),
 ('Zevachim 13:5 — scooped and returned: liable', outside('scooped_returned'), 'liable'),
 ('Zevachim 13:6 — the handful or the frankincense alone', outside('handful_frankincense_one'), ['liable', 'R._Elazar_until_the_second']),
 ('Zevachim 13:6 — part of the blood outside: liable', outside('part_of_blood'), 'liable'),
 ('Zevachim 13:7 — pinched inside, raised outside: liable', outside('fitness_path', rite='pinched', place='inside'), 'liable'),
 ('Zevachim 13:7 — pinched outside, raised outside: exempt', outside('fitness_path', rite='pinched', place='outside'), 'exempt'),
 ('Zevachim 13:7 — slaughtered inside, raised outside: exempt', outside('fitness_path', rite='slaughtered', place='inside'), 'exempt'),
 ('Zevachim 13:7 — slaughtered outside, raised outside: LIABLE', outside('fitness_path', rite='slaughtered', place='outside'), 'liable'),
 ('Zevachim 13:8 — one cup, outside then inside: liable', outside('two_cups', seq=('outside', 'inside'), cups=1), 'liable'),
 ('Zevachim 13:8 — one cup, inside then outside: liable', outside('two_cups', seq=('inside', 'outside'), cups=1), 'liable'),
 ('Zevachim 13:8 — two cups both inside: exempt', outside('two_cups', seq=('inside', 'inside'), cups=2), 'exempt'),
 ('Zevachim 13:8 — two cups both outside: liable', outside('two_cups', seq=('outside', 'outside'), cups=2), 'liable'),
 ('Zevachim 13:8 — inside then outside: exempt (remainder)', outside('two_cups', seq=('inside', 'outside'), cups=2), 'exempt'),
 ('Zevachim 13:8 — outside then inside: liable for the outer, the inner atones', outside('two_cups', seq=('outside', 'inside'), cups=2), 'liable_for_the_outer_the_inner_atones'),
 # ---- THE PLATFORM ERAS ----
 ('Zevachim 14:4-8 — the six eras (Deut 12:9 import)', platform('eras'),
  [('before_the_Tabernacle', 'permitted'), ('the_Tabernacle', 'forbidden'), ('Gilgal', 'permitted'), ('Shiloh', 'forbidden'),
   ('Nob_and_Gibeon', 'permitted'), ('Jerusalem', 'forbidden_forever')]),
 ('Zevachim 14:4 — service by the firstborn, then the priests', platform('service_by'), ['firstborn_before', 'priests_after']),
 ('Zevachim 14:9 — consecrated in the ban, offered in the ban: karet', platform('consecrated_offered', consecrated='ban', offered='ban'), 'positive_negative_and_karet'),
 ('Zevachim 14:9 — consecrated under the permit, offered in the ban: no karet', platform('consecrated_offered', consecrated='permit', offered='ban'), 'positive_and_negative_no_karet'),
 ('Zevachim 14:9 — offered under the permit: a positive only', platform('consecrated_offered', consecrated='ban', offered='permit'), 'positive_only'),
 ('Sifra Acharei 9 6 — the platform classes', platform('classes'), ['sages_burnt_and_shelamim_only', 'R._Meir_whatever_comes_by_vow']),
 ('Sifra Acharei 9 7 — no priest on a platform', platform('no_priest'), 'even_converts_women_slaves_serve'),
 ('Sifra Acharei 9 7 — no fragrance on a platform', platform('no_fragrance'), 'not_on_a_platform'),
 ('Sifra Acharei 9 7 — rock or built altar', platform('rock'), ['R._Meir_even_a_rock', 'R._Yishmael_a_built_altar']),
 ('Zevachim 14:10 — the eleven differences', platform('differences'),
  ['laying_on', 'north_slaughter', 'blood_around', 'waving', 'presenting', 'priesthood', 'service_garments', 'service_vessels',
   'pleasing_fragrance', 'blood_partition', 'washing']),
 ('Lev 17:7 — the demons (Onkelos)', platform('demons'), 'the_demons'),
 ('Sifra Acharei 9 9 — no karet for the platform offense itself', platform('no_karet_for_platform'), 'no_karet_for_the_platform_offense_itself'),
 # ---- THE BLOOD BAN AND THE COVERING ----
 ('Lev 17:10, 14 — the blood ban: karet', blood('ban'), 'karet'),
 ('Sifra Acharei 7 3 — which blood', blood('which_blood'), ['sages_lifeblood_only', 'R._Yehuda_any_blood']),
 ('Lev 17:10 — the eater, not the feeder', blood('eater_not_feeder'), 'the_eater_not_the_feeder'),
 ('Lev 17:14 — karet rides one\'s own eating', blood('karet_own_eating'), 'karet_rides_only_ones_own_eating'),
 ('Lev 17:11 — the atonement clause', blood('atones'), 'one_gift_atones_on_the_altar_exuded_blood_nothing'),
 ('Makkot 3:2 — the blood-eater lashed', blood('lashes'), 'lashed_when_warned'),
 ('Lev 17:10, 12 — the convert bound', blood('convert'), 'convert_bound_as_the_citizen'),
 ('Lev 17:13 — a wild animal: cover owed', covering('species', species='wild'), 'cover_owed'),
 ('Lev 17:13 — a bird: cover owed', covering('species', species='bird'), 'cover_owed'),
 ('Lev 17:13 — the domestic beast: absent from the clause', covering('species', species='beast'), 'no_covering'),
 ('Chullin 6:1 — the koy: covered as a doubt', covering('species', species='koy'), 'cover_no_blessing_doubt'),
 ('Sifra Acharei 11 3 — the impure bird excluded', covering('species', species='impure_bird'), 'no_covering'),
 ('Chullin 6:1 — everywhere, with and without the House', covering('where'), 'everywhere_with_and_without_the_House'),
 ('Chullin 6:1 — consecrated: no covering', covering('consecrated'), 'no_covering'),
 ('Chullin 6:1 / Sifra Acharei 11 2 — hunted of any kind', covering('hunted_of_any_kind'), 'bought_inherited_gifted_self_trapped_all_covered'),
 ('Chullin 6:2 — the failed slaughter, the stabber, the wrencher: exempt', covering('failed_slaughter'), 'exempt'),
 ('Chullin 6:2 — the unfit slaughters: R. Meir vs the sages', covering('unfit_slaughter'), ['R._Meir_liable', 'sages_exempt']),
 ('Chullin 6:3 — the deaf, imbecile, minor watched: liable', covering('deaf_imbecile_minor', watched=True), 'liable_to_cover'),
 ('Chullin 6:3 — by themselves: exempt', covering('deaf_imbecile_minor', watched=False), 'exempt'),
 ('Chullin 6:4 — a hundred in one place: one covering', covering('hundred'), 'one_covering'),
 ('Chullin 6:4 — another saw: liable', covering('another_saw'), 'liable_to_cover'),
 ('Chullin 6:4 — covered and exposed: exempt', covering('state', state='covered_then_exposed'), 'exempt'),
 ('Chullin 6:4 — the wind covered it: liable', covering('state', state='wind_covered'), 'liable_to_cover'),
 ('Chullin 6:5 — mixed with water: the appearance of blood', covering('mixed', with_='water'), 'cover_if_appearance_of_blood'),
 ('Chullin 6:5 — mixed with wine: as water', covering('mixed', with_='wine'), 'view_as_water'),
 ('Chullin 6:5 — mixed with a beast\'s blood', covering('mixed', with_='beast_blood'), ['view_as_water', 'R._Yehuda_blood_does_not_nullify_blood']),
 ('Chullin 6:6 — splashed and knife blood', covering('splashed_knife'), ['liable', 'R._Yehuda_only_when_no_other_blood']),
 ('Chullin 6:7 — fine sand covers', covering('materials', material='fine_sand'), 'covers'),
 ('Chullin 6:7 — lime covers', covering('materials', material='lime'), 'covers'),
 ('Chullin 6:7 — ground brick covers', covering('materials', material='ground_brick'), 'covers'),
 ('Chullin 6:7 — coarse manure does not', covering('materials', material='coarse_manure'), 'does_not_cover'),
 ('Chullin 6:7 — unground brick does not', covering('materials', material='unground_brick'), 'does_not_cover'),
 ('Chullin 6:7 — a vessel over it does not', covering('materials', material='a_vessel'), 'does_not_cover'),
 ('Sifra Acharei 11 10 — metal filings, flour, bran do not', covering('materials', material='flour'), 'does_not_cover'),
 ('Sifra Acharei 11 7 — not with the foot', covering('not_with_the_foot'), 'not_with_the_foot_the_pourer_covers'),
 ('Beitzah 1:2 — the covering on the festival', covering('festival'), ['Shammai_dig_with_the_spade', 'Hillel_only_with_prepared_dust', 'both_after_the_fact']),
 # ---- THE CARCASS-EATER ----
 ('Lev 17:15 — the citizen and the convert', carcass('who'), 'citizen_and_convert_not_the_resident_alien'),
 ('Lev 17:15 — the effect', carcass('effect'), 'washes_garments_bathes_impure_until_evening_then_pure'),
 ('Lev 17:16 — body-wash failure: karet', carcass('failure', organ='body'), 'karet'),
 ('Sifra Acharei 12 13 — garment-wash failure: forty', carcass('failure', organ='garments'), 'forty_lashes'),
 ('Sifra Acharei 12 2 — the minimum', carcass('minimum'), 'olive'),
 ('Sifra Acharei 12 3-4 — the swallow-house', carcass('where_defiles'), 'swallow_house_only'),
 ('Sifra Acharei 12 5-6 — the beast carcass', carcass('beast_carcass'), 'defiles_before_eating_no_swallow_rule'),
 ('Sifra Acharei 12 7 — the impure species', carcass('impure_species'), ['excluded_sages_carcass_AND_torn', 'excluded_R._Yehuda']),
 ('Sifra Acharei 12 8 — the slaughtered excluded', carcass('slaughtered'), 'excluded'),
 ('Sifra Acharei 12 9 — pinching and dayo', carcass('pinching'), ['purifies_R._Meir', 'does_not_R._Yosei_dayo']),
 ('Sifra Acharei 12 11 — the equality test', carcass('equality_test'), 'what_binds_citizen_and_convert_equally'),
 ('Sifra Acharei 12 12-13 — the garments boundary', carcass('garments_boundary'), 'garments_and_vessels_as_garments_yes_man_and_earthenware_no'),
 ('Makkot 3:2 — the eater lashed (the ban imported)', carcass('lashes_for_eating'), 'lashed'),
 # ---- THE FRAME, THE LAND, THE SPECIES ----
 ('Lev 18:3 — the nomoi', frame('nomoi'), 'their_civil_customs_not_their_buildings'),
 ('Shabbat 6:10 — the ways of the Amorite', frame('amorite_ways'), ['R._Meir_remedy_permitted', 'sages_forbidden_even_on_a_weekday']),
 ('Sifra Acharei 8 9 — the canon channel', frame('canon_channel'), {'judgments': 'dinim', 'statutes': 'midrashot', 'keep': 'Mishnah', 'walk_in_them': 'the_deed'}),
 ('Sifra Acharei 13 9 — the two law classes', frame('two_classes'), {'judgments': 'reason_would_have_written', 'statutes': 'decreed_no_permission_to_object'}),
 ('Lev 18:5 — live by them: private', frame('live_by_them', public=False), 'transgress_and_live'),
 ('Lev 18:5 — in public: sanctify the Name', frame('live_by_them', public=True), 'sanctify_the_Name'),
 ('Makkot 3:15 — R. Shimon from its own place: the two DO tokens', frame('sit_and_abstain'), 'rewarded_as_one_who_did_a_commandment'),
 ('Makkot 3:15 — lashes discharge karet', frame('lashes_discharge_karet'), ['discharged_R._Chananya_b._Gamliel']),
 ('Lev 18:25, 28; 20:22 — the land vomits', frame('land'), 'the_land_vomits_its_inhabitants'),
 ('Sifra Acharei 13 16 — all or any one', frame('all_or_any'), 'all_or_any_one'),
 ('Lev 18:29 — the karet persons', frame('karet_persons'), 'man_and_woman_the_doers_not_the_approach'),
 ('Lev 18:30 — the court warned', frame('court_warned'), 'the_court_warned_over_the_charge'),
 ('Sifra Acharei 13 22 — disqualified', frame('disqualified'), 'disqualified_from_following_Me'),
 ('Lev 20:25 — the pure beast (CALLED)', frame('separate_species', kind='pure'), 'pure'),
 ('Lev 20:25 — the impure beast (CALLED)', frame('separate_species', kind='impure'), 'impure'),
 ('Sifra Kedoshim 9 9 — the majority threshold', frame('majority_threshold'), 'most_of_the_windpipe_vs_half_a_hairs_breadth'),
 ('Sifra Kedoshim 9 12 — the compliance crown', frame('compliance'), 'I_can_but_my_Father_decreed'),
 ('Sifra Kedoshim 10 2 — sanctify yourselves', frame('sanctify_yourselves'), 'the_idolatry_separation'),
 ('Megillah 3:5 — the Day reads Acharei Mot', frame('festival_reading'), 'Acharei_Mot_on_the_Day'),
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
print('effects: every cell carries REGISTERED effects — SEVEN discovered in these spans\' own verbs: burned_by_court, '
      'beast_killed (BODY/DESTROY), childless, face_set_against (HEAVEN), cover_owed (DEBIT), land_vomits (TRANSFER), '
      'blood_reckoned (STATUS) [effects law satisfied]')
if ok == n:
    print('BLOOD, UNIONS, AND SANCTIONS COMPILE — the sanction tokens censused and each union located by its own kin '
          'token; the formula decoded on 20:27\'s co-occurrence; the fifteen women and the six computed by composing the '
          'kinship list with the paternal brother; the nine burned from 18:17\'s symmetric pairs; the lash list as the '
          'karet-without-death filter; twenty of the thirty-six enumerated; the two outside clauses with the fitness '
          'path; the covering on its two nouns and its dust; the Lev 4, Lev 12/15, and Lev 11 engines CALLED.')
else:
    print('MISSES (%d):' % len(misses))
    for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
    sys.exit('MISSES REMAIN — consult the Talmud per gap and recompile.')
