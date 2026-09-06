#!/usr/bin/env python3
# THE FESTIVAL CALENDAR (Exod 23:10-19) — the second span compiled
# under the effects law (2026-09-03, same order: "build the skeleton
# then compile the spans"). The span is the code's CLOCK chapter: the
# seventh-year land timer, the seventh-day rest, the three appearings,
# the offering-window clauses, and the kid-in-milk triple. Effects
# from birth, targeting the world_engine contract.
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
assert GUARDED == 16, ('the guard counted %d expectations, the tripwire holds 16' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys
import effects_layer as FX
# the callees (cold) — the dependency-debt sitting (2026-09-06): 23:15's "as I
# commanded you" points to Exod 12-13's matzah law, and 23:10-11's release is
# Lev 25:1-7's — one institution compiled twice with no call between them
# until now. The calendar runner imported nothing.
import io as _io, contextlib as _ctx
with _ctx.redirect_stdout(_io.StringIO()):
    import cold_run_pesach as PS
    import cold_run_yovel as YV
MATZAH = PS.leaven_machine({'ask': 'window_bounds'}, PS.DATA)[0]
PURGE = PS.leaven_machine({'ask': 'purge_deadline'}, PS.DATA)[0]
YOVEL_SAB = YV.sabbatical()
print('routing receipts: cold_run_pesach CALLED — leaven_machine(window_bounds) -> %r, (purge_deadline) -> %r; '
      'cold_run_yovel CALLED — sabbatical()[torah_labors] -> %r [IMPORT, live calls]'
      % (MATZAH, PURGE, YOVEL_SAB['torah_labors']['v']))

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v
        ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND
        v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

PROBES = [
    ('תשמטנה', 'Exod', 23, 11, 'you shall release the land'),
    ('תשבת',   'Exod', 23, 12, 'you shall rest'),
    ('וינפש',  'Exod', 23, 12, 'and be refreshed'),
    ('רגלים',  'Exod', 23, 14, 'three regalim'),
    ('יראה',   'Exod', 23, 17, 'shall appear'),
    ('תזבח',   'Exod', 23, 18, 'you shall not slaughter over leaven'),
    ('ילין',   'Exod', 23, 18, 'shall not remain overnight'),
    ('בכורי',  'Exod', 23, 19, 'the first fruits'),
    ('תבשל',   'Exod', 23, 19, 'you shall not boil'),
    ('גדי',    'Exod', 23, 19, 'a kid'),
    ('אמו',    'Exod', 23, 19, 'its mother'),
    # the triple-mention census — the SAME clause at its two other seats
    ('תבשל',   'Exod', 34, 26, 'the second seat of the kid clause'),
    ('תבשל',   'Deut', 14, 21, 'the third seat of the kid clause'),
]
for tok, bk, ch, vs, note in PROBES:
    if tok not in verse_text(bk, ch, vs):
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at %s %d:%d'
                 % (tok, note, bk, ch, vs))
print('probes: all %d fired (incl. the kid-clause census at its three '
      'seats)  [zero-report law satisfied]\n' % len(PROBES))

P = []
def ink(ref, note):  P.append(('INK',  '%s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))

def out(verdict, effects):
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)


# ===== F1: THE SEVENTH-YEAR RELEASE (23:10-11) =======================
def sabbatical(case, data):
    del P[:]
    ink('Exod 23:10-11', '"six years you shall sow... but the SEVENTH '
        'you shall RELEASE it (תשמטנה) and let it lie (ונטשתה), that '
        'the poor of your people may eat" — a six-plus-one timer on '
        'the LAND, its produce reassigned')
    if case['ask'] == 'timer':
        return out('land released in year 7',
                   ['land_release'])
    if case['ask'] == 'work_scope':
        move('Sukkah 44b:7 (triage LAW row)', '"release" and "let '
             'lie" split — rest from hoeing, rest from clearing '
             'stones: the worked-land verbs enter the ban')
        return out('hoeing barred in the seventh', ['barred_from_it'])
    if case['ask'] == 'home_engine':
        move('cold_run_yovel.sabbatical() [IMPORT, live call]', 'Lev 25:1-7 '
             'is the same release written in full — %d labor verbs (sow, '
             'prune, reap, gather), the aftergrowth, the eaters: one '
             'institution at two seats, ONE function called from both'
             % YOVEL_SAB['torah_labors']['v'])
        return out('the same release: Lev 25 holds %d labor verbs (CALLED yovel)'
                   % YOVEL_SAB['torah_labors']['v'], ['land_release'])
    return out('no verdict in span', [FX.NONE])


# ===== F1b: THE MATZAH POINTER (23:15) — added 2026-09-06 =============
def matzah(case, data):
    del P[:]
    ink('Exod 23:15', '"the feast of unleavened bread you shall keep: SEVEN '
        'DAYS you shall eat unleavened bread AS I COMMANDED YOU (כאשר '
        'צויתך), at the appointed time of the month of Aviv" — the ink\'s '
        'own pointer to the command already written')
    if case['ask'] == 'as_commanded':
        move('cold_run_pesach.leaven_machine [IMPORT, live call]', 'the '
             'command pointed to — Exod 12:15-20, 13:6-7: window -> %r, '
             'purge -> %r' % (MATZAH, PURGE))
        return out('seven days of unleavened bread = %s (CALLED pesach)' % MATZAH,
                   ['purge_deadline'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE SEVENTH-DAY REST (23:12) ==============================
def weekly_rest(case, data):
    del P[:]
    ink('Exod 23:12', '"six days you shall do your deeds and on the '
        'SEVENTH day you shall REST (תשבת), that your ox and your '
        'donkey may rest, and the son of your maidservant and the '
        'STRANGER (הגר) be REFRESHED (וינפש)" — the rest names the '
        'beasts and the resident stranger')
    if case['ask'] == 'who_rests':
        move('Yevamot 48b:6 (triage LAW row)', '"the stranger" here '
             'is the RESIDENT stranger — the uncircumcised sojourner '
             'rests too; the righteous convert is covered elsewhere')
        return out('ox, donkey, slave, resident stranger',
                   ['rest_required'])
    if case['ask'] == 'recurrence':
        return out('every seventh day', ['rest_required'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE THREE APPEARINGS (23:14-17) ===========================
def pilgrimage(person, data):
    del P[:]
    ink('Exod 23:14', '"three REGALIM (רגלים) you shall keep festival '
        'to Me in the year"')
    ink('Exod 23:17', '"three times in the year all your MALES shall '
        'APPEAR (יראה) before the Lord GOD"')
    if person['kind'] == 'able_male':
        return out('owes the three appearings', ['appearance_owed'])
    if person['kind'] == 'woman':
        ink('Exod 23:17', '"all your MALES (זכורך)" — the duty is '
            'written at the males')
        return out('exempt', ['exempt'])
    if person['kind'] == 'lame':
        move('Yevamot 103a:11 (triage LAW row)', 'REGALIM read at the '
             'feet — the pilgrimage asks for legs; the lame man is '
             'outside (Mishnah Chagigah 1:1\'s list)')
        return out('exempt', ['exempt'])
    if person['kind'] == 'blind_one_eye':
        move('Sanhedrin 4b:15 (triage LAW row)', 'yireh/yera\'eh — '
             '"shall see / shall be seen" read both ways: as He comes '
             'to see, He comes to be seen — with both eyes '
             '(Yochanan ben Dahavai; Mishnah Chagigah 1:1 class)')
        return out('exempt', ['exempt'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE OFFERING-WINDOW CLAUSES (23:18) =======================
def offering_windows(case, data):
    del P[:]
    if case['ask'] == 'leaven_beside_offering':
        ink('Exod 23:18', '"you shall not SLAUGHTER (תזבח) the blood '
            'of My offering over leaven"')
        move('Mishnah Pesachim 5:4 + Pesachim 63a-64a (triage rows)',
             'MY offering = the Paschal lamb: the slaughterer with '
             'leaven still in possession transgresses; whose '
             'possession counts is argued at 63b')
        return out('the slaughterer with leaven transgresses',
                   ['barred_from_it'])
    if case['ask'] == 'fat_overnight':
        ink('Exod 23:18', '"neither shall the FAT (חלב) of My feast '
            'REMAIN OVERNIGHT (ילין) until morning" — the altar '
            'portions carry a night deadline')
        move('Pesachim 59b:6 (triage LAW row)', 'Rav Kahana\'s '
             'contradiction resolved: left overnight OFF the altar it '
             'is disqualified by morning; on the altar the night '
             'burns it')
        return out('disqualified at morning off the altar',
                   ['disqualified'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: FIRST FRUITS (23:19a) =====================================
def first_fruits(case, data):
    del P[:]
    ink('Exod 23:19', '"the FIRST (ראשית) of the FIRST FRUITS '
        '(בכורי) of your land you shall bring to the house of the '
        'LORD your God" — a transfer duty on the land\'s first yield')
    dat('WHICH species — the seven kinds — is the transmitted list '
        '(Mishnah Bikkurim 1:3: only from the seven); the ink here '
        'states first-ness, not the species table')
    return out('bring to the house (seven kinds — fetched list)',
               ['restores'])


# ===== F6: THE KID IN ITS MOTHER'S MILK (23:19b) =====================
def kid_in_milk(case, data):
    del P[:]
    ink('Exod 23:19', '"you shall not BOIL (תבשל) a KID (גדי) in its '
        'MOTHER\'S (אמו) milk"')
    move('Chullin 115b / Pesachim 24b:11 (triage rows)', 'the clause '
         'stands WRITTEN THREE TIMES (23:19, 34:26, Deut 14:21 — the '
         'census machine-verified in this run\'s probes): one for '
         'cooking, one for eating, one for benefit')
    if case['ask'] == 'cook':
        return out('barred', ['barred_from_it'])
    if case['ask'] == 'eat':
        return out('barred', ['barred_from_it'])
    if case['ask'] == 'benefit':
        return out('barred', ['barred_from_it'])
    return out('no verdict in span', [FX.NONE])


# ---- Motion 2: the test data; Motion 3+5: run, grade, effects -------
DATA = {}
CASES = [
    ('the seventh-year land timer (Mishnah Sheviit frame)',
     lambda: sabbatical({'ask': 'timer'}, DATA),
     'land released in year 7'),
    ('rest-from-hoeing (the Sukkah 44b verbs split)',
     lambda: sabbatical({'ask': 'work_scope'}, DATA),
     'hoeing barred in the seventh'),
    ('who rests (the resident stranger of Yevamot 48b)',
     lambda: weekly_rest({'ask': 'who_rests'}, DATA),
     'ox, donkey, slave, resident stranger'),
    ('the recurrence — every seventh day',
     lambda: weekly_rest({'ask': 'recurrence'}, DATA),
     'every seventh day'),
    ('Mishnah Chagigah 1:1 — the able male owes the appearings',
     lambda: pilgrimage({'kind': 'able_male'}, DATA),
     'owes the three appearings'),
    ('Mishnah Chagigah 1:1 — women exempt (the ink\'s own "males")',
     lambda: pilgrimage({'kind': 'woman'}, DATA),
     'exempt'),
    ('Mishnah Chagigah 1:1 — the lame exempt (regalim at the feet)',
     lambda: pilgrimage({'kind': 'lame'}, DATA),
     'exempt'),
    ('Mishnah Chagigah 1:1 class — blind in one eye exempt',
     lambda: pilgrimage({'kind': 'blind_one_eye'}, DATA),
     'exempt'),
    ('Mishnah Pesachim 5:4 — slaughtering the Paschal over leaven',
     lambda: offering_windows({'ask': 'leaven_beside_offering'}, DATA),
     'the slaughterer with leaven transgresses'),
    ('the fat-overnight boundary (Pesachim 59b)',
     lambda: offering_windows({'ask': 'fat_overnight'}, DATA),
     'disqualified at morning off the altar'),
    ('Mishnah Bikkurim 1:3 — first fruits to the house, seven kinds',
     lambda: first_fruits({}, DATA),
     'bring to the house (seven kinds — fetched list)'),
    ('Mishnah Chullin 8:4 — cooking barred',
     lambda: kid_in_milk({'ask': 'cook'}, DATA), 'barred'),
    ('Mishnah Chullin 8:4 — eating barred',
     lambda: kid_in_milk({'ask': 'eat'}, DATA), 'barred'),
    ('Mishnah Chullin 8:4 — benefit barred',
     lambda: kid_in_milk({'ask': 'benefit'}, DATA), 'barred'),
    # ---- the pointers, live (2026-09-06) ----
    ('Exod 23:15 "as I commanded you" — the matzah window by call into the Passover engine',
     lambda: matzah({'ask': 'as_commanded'}, DATA),
     'seven days of unleavened bread = 14th evening to 21st evening (CALLED pesach)'),
    ('Lev 25:1-7 is the same release — one function at two seats (by call into the jubilee engine)',
     lambda: sabbatical({'ask': 'home_engine'}, DATA),
     'the same release: Lev 25 holds 4 labor verbs (CALLED yovel)'),
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
    cls = 'INK' if all(k == 'INK' for k in kinds) else \
          ('MOVE' if 'MOVE' in kinds else 'DATA')
    frac[cls] += 1
    print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
    if not hit:
        print('      expected: %s' % want)
        print('      got     : %s' % got)
    used += effects
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
ops = FX.summarize(used)
print('LEDGER OPS this span writes:',
      ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
if ok == len(CASES):
    print('\nTHE CALENDAR COMPILES — the clock chapter\'s own span, '
          'with the first LAND-entity timer and the standing '
          'appearance duty on Heaven\'s docket.')
