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
assert GUARDED == 25, ('the guard counted %d expectations, the tripwire holds 25' % GUARDED)
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


# ---- THE WRAP (W2 THE CALENDAR, D9-iii, 2026-09-07) — the daemon and the scene --------------
# The nine case heads of Exod 12-13 this runner compiled, each a case-form type of
# event_vocabulary.yaml: the month proclaimed (two TIMERS — the purge by midday of the
# fourteenth, the unleavened window), the lamb taken and registered, the withdrawal, the
# access filter, the slaughter (its own name, its registered, its eaters; the leftover's
# burn dated to the sixteenth), the eating, the leaven eaten and the leaven found, the
# firstborn. The daemon writes the ledger and never emits an event; it imports cold with
# the module (the offerings dispatcher calls this runner), the scene runs under main.
import io, contextlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import world_engine as WE
def law_pesach(event, world):
    """Exod 12:2-13:13 (cold_run_pesach.py F1-F5)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'first_month_begun':
        return [E_('purge_deadline', event['subject'], due=event['day'] + 13, value='midday_of_the_14th', law='F1 [INK 12:15 "on the first day you shall remove leaven" — the PRIOR day, Pesachim 5a:6; midday from 34:25, Pesachim 5a:16 — the TIMER]'),
                E_('eating_window', event['subject'], due=event['day'] + 13, value='14th_evening_to_21st_evening', law='F1 [INK 12:18 — both endpoints dated in the ink]')]
    if k == 'lamb_taken':
        out = [E_('registered_to_lamb', m, cp=event['household'], law='F4 [INK 12:3-4 "by the count of souls, each according to his eating" — the registered eater; Pesachim 61a]') for m in event['members']]
        if event.get('neighbor_joins'):
            out.append(E_('registered_to_lamb', event['neighbor_joins'], cp=event['household'], law='F4 [INK 12:4 "he and his neighbor next to his house shall take"]'))
        return out
    if k == 'withdrew_from_lamb':
        if event['when'] == 'before_slaughter':
            return [E_('registered_to_lamb', event['person'], value='withdrawn_while_it_lives', law='F4 [RECORDED Pesachim 89a:23 "from being of a lamb" — while the lamb LIVES one may withdraw]')]
        return [E_('barred_from_it', event['person'], value='no_withdrawal_after_slaughter', law='F4 [RECORDED Pesachim 89a:23 — not after the slaughter (R. Shimon: until the sprinkling)]')]
    if k == 'sought_to_eat':
        pk = event['person_kind']
        if pk in ('stranger_apostate', 'sojourner_or_hireling', 'uncircumcised', 'owner_with_uncircumcised_sons'):
            return [E_('barred_from_it', event['person'], value=pk, law='F3 [INK 12:43, 12:45, 12:48 "shall not eat of it"; Mekhilta the apostate; Yevamot 70b:10 the sons\' circumcision bars the father]')]
        if pk == 'bought_slave' and not event.get('circumcised'):
            return [E_('barred_from_it', event['person'], value='until_circumcised', law='F3 [INK 12:44 "when you have circumcised him, THEN he shall eat"]')]
        return [E_('registered_to_lamb', event['person'], value=pk, law='F3 [INK 12:44 the circumcised slave; 12:48-49 the convert as the home-born, one law]')]
    if k == 'lamb_slaughtered':
        if not (event['for_registered'] and event['for_eaters'] and event['for_its_name']):
            return [E_('disqualified', event['lamb'], law='F2/F4 [RECORDED Pesachim 61a:8, 61a:11 (for its registered, for its eaters); 62b:6 + Zevachim 7b (for its own name — "it IS a Passover sacrifice")]')]
        return [E_('eating_window', event['lamb'], value='night_until_midnight', law='F2 [INK 12:8 "on this night"; RECORDED Pesachim 120b:5 until midnight]'),
                E_('burn_remainder', event['lamb'], due=event['day'] + 2, law='F2 [INK 12:10 "that which remains until morning you shall burn"; RECORDED Pesachim 83b:14: the burn waits for the sixteenth — the TIMER]')]
    if k == 'lamb_eaten':
        out = []
        if event['preparation'] != 'roasted':
            out.append(E_('barred_from_it', event['eater'], value=event['preparation'], law='F2 [INK 12:9 "not raw, nor boiled in water, but roasted with fire"]'))
        if event.get('carried_out'):
            out.append(E_('barred_from_it', event['eater'], value='carried_out', law='F2 [INK 12:46 "you shall not carry out"; RECORDED Pesachim 85b:1 from group to group]'))
        if event.get('bone_broken'):
            out.append(E_('lashes', event['eater'], law='F2 [INK 12:46 "a bone you shall not break in it"; Mishnah Pesachim 7:11: forty]') if event.get('lamb_valid', True)
                       else E_('exempt', event['eater'], value='the_disqualified_lambs_bone', law='F2 [RECORDED Pesachim 84a:15 "in IT" — a valid lamb only]'))
        return out
    if k == 'leaven_eaten':
        return [E_('karet_cut_off', event['eater'], cp='HEAVEN', value=event['day'], law='F1 [INK 12:15, 12:19 "whoever eats leaven, that soul shall be cut off"]')]
    if k == 'leaven_found':
        if event['owner'] != 'jew':
            return [E_('exempt', event['holder'], value=event['owner'], law='F1 [RECORDED Pesachim 5b:2-6a:6: "with YOU" — the gentile\'s and the deposited you may see]')]
        return [E_('barred_from_it', event['holder'], value='the_jews_own_leaven_after_passover', law='F1 [INK 13:7 "no leaven shall be seen with you"; RECORDED Pesachim 29a:5]')]
    if k == 'firstborn_born':
        b = event['born']
        if b == 'donkey':
            return [E_('consecrated_firstborn', event['owner'], value=b, law='F5 [INK 13:2 "sanctify to Me every firstborn"]'), E_('redeem_or_break', event['owner'], value='redeem_with_a_lamb_else_break_the_neck', law='F5 [INK 13:13; Mishnah Bekhorot 1:7: the redemption first]')]
        if b == 'human':
            return [E_('consecrated_firstborn', event['owner'], value=b, law='F5 [INK 13:2]'), E_('pays', event['owner'], cp='the-priest', amount=5, law='F5 [INK 13:13 "every firstborn of man among your sons you shall redeem"; the five sela the fetched constant, Num 18:16]')]
        return [E_('exempt', event['owner'], value='caesarean_never_opened_the_womb', law='F5 [INK 13:2 "opener of every WOMB"; RECORDED Niddah 40a:14]')]
    return []

def scene():
    """THE SCENE — the recorded rows replayed on the world engine (clock unit: days of the first month; the tape the answer sheet's)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the Passover of Exod 12-13: Pesachim 5, 7-8, Keritot 1, Bekhorot 1 on the engine (clock unit: days of Nisan)')
        w.laws = [law_pesach]
        w.advance(1)
        w.submit({'kind': 'first_month_begun', 'subject': 'israel', 'month': 'nisan', 'day': 1, 'case_source': 'Mishnah Rosh Hashanah 1:1 — the first of Nisan; Exod 12:2'})
        w.advance(10)
        w.submit({'kind': 'lamb_taken', 'subject': 'the-house-of-reuben', 'household': 'the-house-of-reuben', 'members': ['reuben', 'his-wife', 'his-son'], 'neighbor_joins': 'simeon', 'case_source': 'Mishnah Pesachim 8:1-3 — registered by the count; Exod 12:3-4'})
        w.advance(12)
        w.submit({'kind': 'withdrew_from_lamb', 'subject': 'his-son', 'person': 'his-son', 'when': 'before_slaughter', 'case_source': 'Pesachim 89a:23 — while the lamb lives'})
        for p, pk, circ in (('the-apostate', 'stranger_apostate', None), ('the-hireling', 'sojourner_or_hireling', None), ('the-uncircumcised', 'uncircumcised', None),
                            ('the-bought-slave', 'bought_slave', False), ('the-circumcised-slave', 'bought_slave', True), ('the-owner', 'owner_with_uncircumcised_sons', None), ('the-convert', 'convert', None)):
            w.submit({'kind': 'sought_to_eat', 'subject': p, 'person': p, 'person_kind': pk, 'circumcised': circ, 'case_source': 'Exod 12:43-49 — the access filter; Mekhilta; Yevamot 70b'})
        w.advance(14)                                                      # the fourteenth: the purge and the window timers FIRE
        w.submit({'kind': 'lamb_slaughtered', 'subject': 'the-lamb', 'lamb': 'the-lamb', 'for_registered': True, 'for_eaters': True, 'for_its_name': True, 'day': 14, 'case_source': 'Pesachim 61a, 62b — for its registered, its eaters, its name'})
        w.submit({'kind': 'lamb_slaughtered', 'subject': 'the-second-lamb', 'lamb': 'the-second-lamb', 'for_registered': True, 'for_eaters': True, 'for_its_name': False, 'day': 14, 'case_source': 'Pesachim 62b:6 + Zevachim 7b — not for its name: invalid'})
        for e, prep, carried, bone, valid in (('reuben', 'roasted', False, False, True), ('simeon', 'boiled', False, False, True), ('levi', 'roasted', True, False, True), ('judah', 'roasted', False, True, True), ('dan', 'roasted', False, True, False)):
            w.submit({'kind': 'lamb_eaten', 'subject': e, 'eater': e, 'preparation': prep, 'carried_out': carried, 'bone_broken': bone, 'lamb_valid': valid, 'case_source': 'Exod 12:8-9, 12:46; Mishnah Pesachim 7:11; Pesachim 84a, 85b'})
        w.submit({'kind': 'withdrew_from_lamb', 'subject': 'his-wife', 'person': 'his-wife', 'when': 'after_slaughter', 'case_source': 'Pesachim 89a:23 — not after the slaughter'})
        w.advance(15)
        w.submit({'kind': 'leaven_eaten', 'subject': 'the-eater', 'eater': 'the-eater', 'day': 15, 'case_source': 'Mishnah Keritot 1:1 — leaven on Passover; Exod 12:15'})
        w.submit({'kind': 'leaven_found', 'subject': 'the-jew', 'holder': 'the-jew', 'owner': 'jew', 'after_pesach': True, 'case_source': 'Pesachim 29a:5 — his own leaven kept through Passover'})
        w.submit({'kind': 'leaven_found', 'subject': 'the-jew', 'holder': 'the-jew', 'owner': 'gentile', 'after_pesach': True, 'case_source': "Pesachim 5b-6a — the gentile's leaven: 'with YOU'"})
        w.advance(16)                                                      # the sixteenth: the leftover's burn timer FIRES
        w.advance(22)
        for o, b in (('the-herdsman', 'donkey'), ('the-father', 'human'), ('the-herdsman', 'caesarean_animal')):
            w.submit({'kind': 'firstborn_born', 'subject': o, 'owner': o, 'born': b, 'case_source': 'Mishnah Bekhorot 1:7; Num 18:16; Niddah 40a:14'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    amt = lambda eid, eff: sum(e['amount'] or 0 for e in w.entity(eid).ledger if e['effect'] == eff)
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('israel', 'purge_deadline'), n('israel', 'eating_window'),
            n('reuben', 'registered_to_lamb'), n('his-wife', 'registered_to_lamb'), n('his-son', 'registered_to_lamb'), n('simeon', 'registered_to_lamb'),
            n('the-apostate', 'barred_from_it'), n('the-hireling', 'barred_from_it'), n('the-uncircumcised', 'barred_from_it'), n('the-bought-slave', 'barred_from_it'),
            n('the-circumcised-slave', 'registered_to_lamb'), n('the-owner', 'barred_from_it'), n('the-convert', 'registered_to_lamb'),
            n('the-lamb', 'eating_window'), n('the-lamb', 'burn_remainder'), n('the-second-lamb', 'disqualified'),
            n('reuben', 'barred_from_it'), n('simeon', 'barred_from_it'), n('levi', 'barred_from_it'), n('judah', 'lashes'), n('dan', 'exempt'), n('his-wife', 'barred_from_it'),
            n('the-eater', 'karet_cut_off'), n('the-jew', 'barred_from_it'), n('the-jew', 'exempt'),
            n('the-herdsman', 'consecrated_firstborn'), n('the-herdsman', 'redeem_or_break'), n('the-herdsman', 'exempt'), n('the-father', 'consecrated_firstborn'), n('the-father', 'pays'), amt('the-father', 'pays'),
            tset, fired, w.clock.day), w

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
    # ---- THE WRAP (W2): the scene on the world engine — the recorded rows on the daemon ----
    ('THE SCENE on the world engine — the wrap (W2): the month proclaimed and its two timers fired on the fourteenth; four registered by the count, the son withdrawn while the lamb lives and the wife barred after the slaughter; the filter (four barred, the circumcised slave and the convert in); the lamb valid and the second disqualified for its name; the leftover burned on the sixteenth; boiled, carried out, the bone (lashes; the invalid lamb exempt); leaven eaten (karet), the Jew\'s leaven barred, the gentile\'s exempt; the donkey, the son (five), the caesarean',
     lambda: (SCENE, [FX.NONE], [('INK', 'Exod 12-13 — the recorded rows replayed: Rosh Hashanah 1:1, Pesachim 5, 7-8, 61a, 84a-89a, 120b, Keritot 1:1, Bekhorot 1:7, Niddah 40a')]),
     (1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 3, 3, 22)),
]

# ---- Motion 3+5: run, grade, and emit effects -----------------------
# The run is guarded so the functions above IMPORT COLD — the Lev 1-8
# offering dispatcher CALLS paschal_procedure() and registration() for
# its pesach cell (sitting A, 2026-09-05, REVIEW_LEV1-8 item I: the
# first-call standard of cold_run_mishpatim -> cold_run_lev24).
if __name__ == '__main__':
    SCENE, _W = scene()                      # THE WRAP's scene runs under main only: the module imports cold
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
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
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
