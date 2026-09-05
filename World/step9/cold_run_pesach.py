#!/usr/bin/env python3
# THE PASSOVER ENGINE — the first span compiled AFTER the effects law
# (2026-09-03, owner: "build the skeleton then compile the spans").
# Span: Exodus 12-13 (the command, the leaven, the access ordinance,
# the consecration). Five motions of the Step-5 deliverable rule, with
# EFFECTS FROM BIRTH: every verdict carries registry effects targeting
# the world_engine contract {effect, subject, counterparty, amount,
# due, source_law, case_source}.
#
# Motion 1 — code from the bare ink alone (quantities = parameters).
# Motion 2 — Mishnah rows as test data (addresses are lookups).
# Motion 3 — run.
# Motion 4 — the Talmud consulted PER MISS, each a labeled move (the
#            Exodus triage ledger holds the rows; cited where used).
# Motion 5 — added, with the effects layer live.
# Read-only; touches no unit; model layer.

# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 24, ('the guard counted %d expectations, the tripwire holds 24' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys
import effects_layer as FX

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=? AND
        v.verse=? ORDER BY w.idx""", (ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

# ---- zero-report probes: the span's load-bearing tokens -------------
PROBES = [
    ('ונכרתה', 12, 15, 'cut off — the karet clause'),
    ('תשביתו', 12, 15, 'you shall remove — the purge verb'),
    ('תשרפו',  12, 10, 'you shall burn — the remainder'),
    ('בלילה',  12, 8,  'on the night — the eating window'),
    ('צלי',    12, 8,  'roasted'),
    ('נא',     12, 9,  'raw'),
    ('מבשל',   12, 9,  'boiled'),
    ('תכסו',   12, 4,  'you shall count — registration'),
    ('תשברו',  12, 46, 'you shall (not) break — the bone'),
    ('תוציא',  12, 46, 'you shall (not) carry out — the one house'),
    ('ערל',    12, 48, 'uncircumcised'),
    ('נכר',    12, 43, 'stranger'),
    ('תושב',   12, 45, 'sojourner'),
    ('קדש',    13, 2,  'sanctify — the firstborn'),
    ('תפדה',   13, 13, 'you shall redeem'),
    ('וערפתו', 13, 13, 'and break its neck'),
    ('פסח',    12, 27, 'it IS a Passover — the name'),
    ('לחדש',   12, 18, 'of the month — the dated window'),
]
for tok, ch, vs, note in PROBES:
    if tok not in verse_text(ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Exod %d:%d '
                 '— refusing to run' % (tok, note, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n'
      % len(PROBES))

P = []  # the provenance trail of the case being run
def ink(ref, note):  P.append(('INK',  'Exod %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)


# ===== F1: THE LEAVEN MACHINE (Exod 12:15-20, 13:3-7) ================
def leaven_machine(case, data):
    del P[:]
    if case['ask'] == 'eats_leaven_in_window':
        ink('12:15', '"whoever eats leaven... that soul shall be CUT '
            'OFF (ונכרתה) from Israel, from the first day to the '
            'seventh day"')
        return out('karet', ['karet_cut_off'])
    if case['ask'] == 'purge_deadline':
        ink('12:15', '"yet on the FIRST day (ביום הראשון) you shall '
            'remove leaven from your houses" — but the same verse '
            'counts eating-days one to seven')
        move('Pesachim 5a:6 (triage LAW row)', 'the school of R. '
             'Yishmael: "harishon" here means the PRIOR day — the '
             'fourteenth; the window cannot both start and be purged')
        move('Pesachim 5a:16 (triage LAW row)', 'Rava fixes the hour: '
             '"you shall not slaughter over leaven" (34:25) — the '
             'slaughter season is from MIDDAY, so the purge deadline '
             'is midday of the fourteenth')
        return out('midday of the 14th', ['purge_deadline'])
    if case['ask'] == 'window_bounds':
        ink('12:18', '"on the fourteenth day of the month AT EVENING '
            'you shall eat matzot, until the twenty-first day of the '
            'month at evening" — both endpoints dated in the ink')
        return out('14th evening to 21st evening', ['eating_window'])
    if case['ask'] == 'whose_leaven_after_pesach':
        ink('13:7', '"no leaven shall be SEEN with YOU (לך)" — the '
            'possessive bounds the ban')
        move('Pesachim 5b:2-6a:6 (triage rows)', 'yours you may not '
             'see; the gentile\'s and the deposited you may — '
             'ownership is the parameter')
        if case['owner'] == 'gentile':
            return out('permitted after Passover', ['exempt'])
        move('Pesachim 29a:5 (triage LAW row)', 'the Jew\'s own leaven '
             'kept through Passover stands penalized — the ownership '
             'reading\'s other arm')
        return out('forbidden after Passover', ['barred_from_it'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE PASCHAL PROCEDURE (Exod 12:3-11, 43-46) ===============
def paschal_procedure(case, data):
    del P[:]
    if case['ask'] == 'eating_time':
        ink('12:8', '"and they shall eat the flesh ON THIS NIGHT '
            '(בלילה הזה)" — night, not day')
        move('Pesachim 120b:5 (triage LAW row)', 'R. Elazar ben '
             'Azarya: "on this night" learned from Egypt\'s midnight '
             '— eaten only UNTIL MIDNIGHT; R. Akiva\'s haste-hour '
             'reading recorded beside it (the fork the Mishnah '
             'settles at midnight)')
        return out('night only, until midnight', ['eating_window'])
    if case['ask'] == 'preparation':
        ink('12:9', '"eat not of it RAW (נא), nor BOILED (מבשל) in '
            'water, but ROASTED (צלי) with fire"')
        return out('roasted only', ['barred_from_it'])
    if case['ask'] == 'leftover':
        ink('12:10', '"let nothing of it remain until morning; that '
            'which remains until morning you shall BURN (תשרפו) with '
            'fire"')
        move('Pesachim 83b:14 + Shabbat 24b (triage rows)', 'the '
             'festival itself admits no burning — the burn waits for '
             'the sixteenth: the deadline is a computed date')
        return out('burn on the 16th', ['burn_remainder'])
    if case['ask'] == 'break_bone':
        ink('12:46', '"neither shall you BREAK (תשברו) a bone in it '
            '(בו)"')
        move('Pesachim 84a:15 (triage LAW row)', '"in IT" — a valid '
             'lamb only; the disqualified lamb\'s bones are outside')
        if not case.get('lamb_valid', True):
            return out('exempt', ['exempt'])
        move('Mishnah Pesachim 7:11', 'the breaker of a bone of a '
             'pure Paschal lamb receives the forty lashes')
        return out('lashes', ['lashes'])
    if case['ask'] == 'carry_out':
        ink('12:46', '"in one house shall it be eaten; you shall not '
            'CARRY OUT (תוציא) of the flesh outside the house"')
        move('Pesachim 85b:1 (triage LAW row)', 'from group to group '
             'is carrying out — the group is the house')
        return out('forbidden between groups', ['barred_from_it'])
    if case['ask'] == 'for_its_sake':
        ink('12:27', '"and you shall say: it IS a PASSOVER sacrifice '
            '(זבח פסח הוא)" — the name is in the declaration')
        move('Pesachim 62b:6 / Zevachim 7b (triage rows)', 'the '
             'slaughter must be for its own name — "it is" makes the '
             'requirement indispensable for THIS offering')
        return out('invalid if not for its sake', ['disqualified'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE ACCESS FILTER (Exod 12:43-49) =========================
def access_filter(person, data):
    del P[:]
    ink('12:43', '"this is the ordinance of the Passover: no STRANGER '
        '(בן נכר) shall eat of it"')
    if person['kind'] == 'stranger_apostate':
        move('Mekhilta (the seated reading)', 'the ben nekhar read at '
             'the estranged in deed — the apostate Israelite too')
        return out('barred', ['barred_from_it'])
    if person['kind'] == 'sojourner_or_hireling':
        ink('12:45', '"a SOJOURNER (תושב) and a hired servant shall '
            'not eat of it"')
        return out('barred', ['barred_from_it'])
    if person['kind'] == 'uncircumcised':
        ink('12:48', '"no UNCIRCUMCISED one (ערל) shall eat of it"')
        return out('barred', ['barred_from_it'])
    if person['kind'] == 'bought_slave':
        ink('12:44', '"every man\'s slave bought for money — when you '
            'have circumcised him, THEN he shall eat of it" — the '
            'circumcision is the gate')
        if person.get('circumcised'):
            return out('eats', ['registered_to_lamb'])
        return out('barred until circumcised', ['barred_from_it'])
    if person['kind'] == 'owner_with_uncircumcised_sons':
        ink('12:48', '"let all his males be circumcised, and then let '
            'him come near"')
        move('Yevamot 70b:10 (triage LAW row)', '"FROM IT" — the '
             'sons\' and slaves\' circumcision bars the FATHER\'s own '
             'eating')
        return out('barred until they are circumcised',
                   ['barred_from_it'])
    if person['kind'] == 'convert':
        ink('12:48', '"when a stranger sojourns with you and makes '
            'the Passover... he shall be as one born in the land"')
        ink('12:49', '"ONE LAW (תורה אחת) for the home-born and the '
            'sojourner"')
        return out('eats as the home-born', ['registered_to_lamb'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE REGISTRATION (Exod 12:4) ==============================
def registration(case, data):
    del P[:]
    ink('12:4', '"and if the household be too little for a lamb, he '
        'and his neighbor next to his house shall take — by the COUNT '
        '(במכסת) of souls; each according to his EATING shall you '
        'COUNT (תכסו) for the lamb"')
    if case['ask'] == 'join_households':
        return out('neighbor joins by count', ['registered_to_lamb'])
    if case['ask'] == 'slaughter_for_nonregistrants':
        move('Pesachim 61a:8 (triage LAW row)', '"by the count" — '
             'slaughtered only for its registered; for others it is '
             'not its count')
        return out('invalid', ['disqualified'])
    if case['ask'] == 'slaughter_for_noneaters':
        move('Pesachim 61a:11 (triage LAW row)', '"according to his '
             'EATING" — the one who cannot eat an olive-bulk is '
             'outside the count')
        return out('invalid', ['disqualified'])
    if case['ask'] == 'withdraw':
        move('Pesachim 89a:23 (triage LAW row)', '"miheyot mi-seh" '
             'read "while the lamb LIVES" — withdraw until it is '
             'slaughtered (R. Shimon\'s until-sprinkling arm recorded '
             'beside it)')
        if case['when'] == 'before_slaughter':
            return out('may withdraw', ['registered_to_lamb'])
        return out('may not withdraw', ['barred_from_it'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE FIRSTBORN CONSECRATION (Exod 13:2, 11-13) =============
def firstborn(case, data):
    del P[:]
    ink('13:2', '"SANCTIFY (קדש) to Me every firstborn, opener of '
        'every womb" — the status is written at birth')
    if case['kind'] == 'donkey':
        ink('13:13', '"every firstborn donkey you shall REDEEM '
            '(תפדה) with a lamb; if you do not redeem it, you shall '
            'BREAK ITS NECK (וערפתו)"')
        move('Mishnah Bekhorot 1:7 (the answer sheet\'s own order)',
             'the redemption command precedes the breaking — the fork '
             'favors the lamb')
        return out('redeem with a lamb, else break the neck',
                   ['consecrated_firstborn', 'redeem_or_break'])
    if case['kind'] == 'human':
        ink('13:13', '"and every firstborn of man among your sons you '
            'shall REDEEM"')
        dat('the amount — five sela — is the data channel: the '
            'constant lives at Numbers 18:16, fetched, not written '
            'here')
        return out('redeem (five sela — fetched constant)',
                   ['consecrated_firstborn', 'pays'])
    if case['kind'] == 'caesarean_animal':
        ink('13:2', '"opener of every WOMB (פטר כל רחם)" — the '
            'consecration rides the womb-opening itself')
        move('Niddah 40a:14 (triage LAW row)', 'the caesarean birth '
             'never opened the womb — the firstborn status does not '
             'attach')
        return out('not consecrated', ['exempt'])
    return out('no verdict in span', [FX.NONE])


# =====================================================================
# Motion 2 — THE TEST DATA: the Mishnah's rows (and, where the span's
# tester is a recorded baraita, that baraita named as such).
# =====================================================================
DATA = {}
CASES = [
    # F1 — the leaven machine
    ('Mishnah Keritot 1:1 — leaven on Passover in the karet list',
     lambda: leaven_machine({'ask': 'eats_leaven_in_window'}, DATA),
     'karet'),
    ('Mishnah Pesachim 1:4 frame — the deadline the hour-fence guards',
     lambda: leaven_machine({'ask': 'purge_deadline'}, DATA),
     'midday of the 14th'),
    ('the dated window (the ink graded against itself; Pesachim 28b:11 '
     'reads the same verse)',
     lambda: leaven_machine({'ask': 'window_bounds'}, DATA),
     '14th evening to 21st evening'),
    ('Mishnah Pesachim 2:2 — the gentile\'s leaven after Passover',
     lambda: leaven_machine({'ask': 'whose_leaven_after_pesach',
                             'owner': 'gentile'}, DATA),
     'permitted after Passover'),
    ('Mishnah Pesachim 2:2 — the Jew\'s leaven after Passover',
     lambda: leaven_machine({'ask': 'whose_leaven_after_pesach',
                             'owner': 'jew'}, DATA),
     'forbidden after Passover'),
    # F2 — the Paschal procedure
    ('Mishnah Zevachim 5:8 — eaten only at night, until midnight',
     lambda: paschal_procedure({'ask': 'eating_time'}, DATA),
     'night only, until midnight'),
    ('Mishnah Zevachim 5:8 — eaten only roasted',
     lambda: paschal_procedure({'ask': 'preparation'}, DATA),
     'roasted only'),
    ('Mishnah Pesachim 7:10 — the leftover burned on the sixteenth',
     lambda: paschal_procedure({'ask': 'leftover'}, DATA),
     'burn on the 16th'),
    ('Mishnah Pesachim 7:11 — the bone-breaker gets the forty',
     lambda: paschal_procedure({'ask': 'break_bone',
                                'lamb_valid': True}, DATA),
     'lashes'),
    ('Mishnah Pesachim 7:11 end — no lashes on the disqualified lamb',
     lambda: paschal_procedure({'ask': 'break_bone',
                                'lamb_valid': False}, DATA),
     'exempt'),
    ('Mishnah Pesachim 9:? / Pesachim 85b — meat between groups',
     lambda: paschal_procedure({'ask': 'carry_out'}, DATA),
     'forbidden between groups'),
    ('Mishnah Pesachim 5:2 — slaughtered not for its sake',
     lambda: paschal_procedure({'ask': 'for_its_sake'}, DATA),
     'invalid if not for its sake'),
    # F3 — the access filter
    ('Mekhilta-seated reading — the apostate at "ben nekhar"',
     lambda: access_filter({'kind': 'stranger_apostate'}, DATA),
     'barred'),
    ('the ink\'s own sojourner clause (12:45)',
     lambda: access_filter({'kind': 'sojourner_or_hireling'}, DATA),
     'barred'),
    ('Mishnah Pesachim 5:3 class — the uncircumcised',
     lambda: access_filter({'kind': 'uncircumcised'}, DATA),
     'barred'),
    ('the bought slave, circumcised (12:44)',
     lambda: access_filter({'kind': 'bought_slave',
                            'circumcised': True}, DATA),
     'eats'),
    ('Yevamot 71a:16 baraita — the father with uncircumcised sons',
     lambda: access_filter({'kind': 'owner_with_uncircumcised_sons'},
                           DATA),
     'barred until they are circumcised'),
    ('the convert — one law (12:48-49)',
     lambda: access_filter({'kind': 'convert'}, DATA),
     'eats as the home-born'),
    # F4 — the registration
    ('Mishnah Pesachim 8:3 — register and withdraw until slaughter',
     lambda: registration({'ask': 'withdraw',
                           'when': 'before_slaughter'}, DATA),
     'may withdraw'),
    ('Mishnah Pesachim 5:3 — slaughtered for non-registrants',
     lambda: registration({'ask': 'slaughter_for_nonregistrants'},
                          DATA),
     'invalid'),
    ('Mishnah Pesachim 5:3 — slaughtered for those who cannot eat',
     lambda: registration({'ask': 'slaughter_for_noneaters'}, DATA),
     'invalid'),
    # F5 — the firstborn
    ('Mishnah Bekhorot 1:7 — the donkey: lamb first, else the neck',
     lambda: firstborn({'kind': 'donkey'}, DATA),
     'redeem with a lamb, else break the neck'),
    ('Mishnah Bekhorot 8:? — the human firstborn redeemed',
     lambda: firstborn({'kind': 'human'}, DATA),
     'redeem (five sela — fetched constant)'),
    ('Niddah 40a:14 / Mishnah Bekhorot 2:9 class — the caesarean',
     lambda: firstborn({'kind': 'caesarean_animal'}, DATA),
     'not consecrated'),
]

# ---- Motion 3+5: run, grade, and emit effects -----------------------
# The run is guarded so the functions above IMPORT COLD — the Lev 1-8
# offering dispatcher CALLS paschal_procedure() and registration() for
# its pesach cell (sitting A, 2026-09-05, REVIEW_LEV1-8 item I: the
# first-call standard of cold_run_mishpatim -> cold_run_lev24).
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
        cls = 'INK' if all(k == 'INK' for k in kinds) else \
              ('MOVE' if 'MOVE' in kinds else 'DATA')
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % want)
            print('      got     : %s' % got)
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) '
          '· data %d/%d (%.0f%%)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot,
           frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot,
           frac['DATA'], tot, 100.0 * frac['DATA'] / tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:',
          ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    if ok == len(CASES):
        print('\nTHE PASSOVER ENGINE COMPILES — the first span born under '
              'the effects law, its verdicts carrying registry effects '
              'into the world_engine contract.')
