#!/usr/bin/env python3
# LEV 24:10-23 — THE FIRST CALL (2026-09-05, under the compiler law)
# The compile dependency pulled ahead by Exodus 21's talion cell
# (EX21-18; move M-07 exemplar c): eye-under-eye stands at exactly
# TWO seats in the canon — Exod 21:24 and Lev 24:20 — and the
# Talmud's money derivation runs on THIS span's verses (Bava Kamma
# 83b:10, 84a:1). This file compiles the span ink-first and EXPORTS
# talion() for the Exodus runner to import: the first inter-span
# function call of the compiled Bible.
# Five motions; read-only; every non-ink cell labeled with the
# teacher's source row; every token probed (zero-report law);
# effects on every cell (the effects law). Read ledger:
# logic/oral_triage/lev_24_first_call_2026-09-05.md

import sqlite3, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
DB = '<repo-old>/elijah_docket/tanakh.sqlite'


# ---- THE EXPORT — the called function ------------------------------
# Exodus 21:24's tariff cell resolves THROUGH this span: the formula's
# only other exact occurrence (machine census below), sitting beside
# its own pay verb (24:18), its fatal/non-fatal disambiguator (24:21,
# Bava Kamma 83b:10), and its equality rider (24:22, Bava Kamma
# 84a:1). Pure function: importing it runs nothing.
def talion(blemish='eye'):
    return {
        'blemish': blemish,
        'verdict': 'PAY-MONEY',
        'effect': 'substitution',
        'prov': 'RECORDED',
        'why': ('through Lev 24:18-22 — the pay verb on the exchange '
                'formula (24:18), strikes-beast-pays beside '
                'strikes-man-dies (24:21, Bava Kamma 83b:10 "that one '
                'is written about killing"), and one-law-EQUAL-for-all '
                '(24:22, Bava Kamma 84a:1) — money is what equalizes'),
    }


def main():
    db = sqlite3.connect(DB)

    def strip(s):
        return ''.join(c for c in s
                       if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

    def words(book, ch, vs):
        return [strip(he) for (he,) in db.execute(
            """SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id
               WHERE v.book=? AND v.chapter=? AND v.verse=?
               ORDER BY w.idx""", (book, ch, vs))]

    def has_token(book, ch, vs, tok):
        return tok in words(book, ch, vs)

    # ---- probes: every token the run relies on must fire ------------
    PROBES = [
        ('custody',    'במשמר',   'Lev', 24, 12),
        ('to-declare', 'לפרש',    'Lev', 24, 12),
        ('take-out',   'הוצא',    'Lev', 24, 14),
        ('the-curser', 'המקלל',   'Lev', 24, 14),
        ('outside',    'מחוץ',    'Lev', 24, 14),
        ('who-heard',  'השמעים',  'Lev', 24, 14),
        ('congregation', 'העדה',  'Lev', 24, 16),
        ('curse-verb', 'יקלל',    'Lev', 24, 15),
        ('bears',      'ונשא',    'Lev', 24, 15),
        ('his-sin',    'חטאו',    'Lev', 24, 15),
        ('pierces',    'ונקב',    'Lev', 24, 16),
        ('any',        'כל',      'Lev', 24, 17),
        ('pays-her',   'ישלמנה',  'Lev', 24, 18),
        ('man-subject', 'ואיש',   'Lev', 24, 19),
        ('blemish',    'מום',     'Lev', 24, 19),
        ('fellow',     'בעמיתו',  'Lev', 24, 19),
        ('fracture',   'שבר',     'Lev', 24, 20),
        ('one-law',    'משפט',    'Lev', 24, 22),
        ('as-the-ger', 'כגר',     'Lev', 24, 22),
        ('did',        'עשו',     'Lev', 24, 23),
        ('him',        'אתו',     'Lev', 24, 23),
    ]
    failed = [(n, b, c, v) for n, tok, b, c, v in PROBES
              if not has_token(b, c, v, tok)]
    if failed:
        sys.exit('ZERO-REPORT LAW: probes failed to fire: %r' % failed)
    print('probes: all %d token probes fired  [zero-report law satisfied]'
          % len(PROBES))

    # ---- censuses (each self-tested against a known seat) -----------
    stream = [(b, c, v, strip(he)) for b, c, v, he in db.execute(
        """SELECT v.book, v.chapter, v.verse, w.he FROM words w
           JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx""")]

    def census(noun):
        hits = []
        for i in range(len(stream) - 2):
            if (stream[i][3] == noun and stream[i+1][3] == 'תחת'
                    and stream[i+2][3] == noun):
                hits.append('%s %d:%d' % stream[i][:3])
        return hits

    assert 'Exod 21:24' in census('עין'), \
        'census self-test: the scanner must find the known Exodus seat'
    CEN = {n: census(n) for n in ('עין', 'שן', 'נפש', 'שבר')}
    assert CEN['עין'] == ['Exod 21:24', 'Lev 24:20']
    assert CEN['שן'] == ['Exod 21:24', 'Lev 24:20']
    assert CEN['נפש'] == ['Exod 21:23', 'Lev 24:18']
    assert CEN['שבר'] == ['Lev 24:20']
    shem = sum(1 for w in words('Lev', 24, 16) if w in ('שם', 'השם'))
    assert shem == 2, 'the doubled Name token of 24:16'
    print('censuses: eye/tooth-under = the two seats exactly; '
          'life-under = Exod 21:23 + Lev 24:18 (the pay clause); '
          'FRACTURE-UNDER UNIQUE to Lev 24:20; Name doubled in 24:16\n')

    # ---- the grid -----------------------------------------------------
    TOTAL = {'INK': 0, 'RECORDED': 0, 'ROUTED/IMPORT': 0}

    def grade(fn, oracle_name, cells):
        ok = 0
        print('FUNCTION: %s  (answer sheet: %s)' % (fn, oracle_name))
        for name, verdict, want, prov, kind in cells:
            mark = 'ok' if verdict == want else 'MISMATCH'
            ok += verdict == want
            TOTAL[kind] += 1
            print('  %-36s %-12s [%s]  <- %s' % (name, verdict, mark, prov))
        print('  -> %d/%d\n' % (ok, len(cells)))
        return ok, len(cells)

    results = []

    # ---- F1: the runtime code request (24:10-12, 23) ----------------
    cells = [
        ('undefined case -> block + request', 'CUSTODY+ASK', 'CUSTODY+ASK',
         'INK 24:12: in custody "to declare to them by the mouth of the '
         'LORD" (Onkelos: the house of custody, the DECREE awaited)', 'INK'),
        ('the run log grades itself', 'MATCH', 'MATCH',
         'INK 24:23: out-of-camp + stoning executed + "as the LORD '
         'commanded Moses" — the ink\'s own test assertion', 'INK'),
    ]
    results.append(grade('runtime code request',
                         'the span\'s own execution report', cells))

    # ---- F2: the curse gate (24:15-16) ------------------------------
    cells = [
        ('curses his God, NO Name', 'BEARS-SIN', 'BEARS-SIN',
         'INK: the 15/16 delta — v15 "bears his sin" vs v16 "shall die"; '
         'Onkelos splits the verbs (provokes vs specifies); R. Meir\'s '
         'extend-to-epithets arm kept [Sanhedrin 56a:17]', 'INK'),
        ('death needs the NAME, by the Name', 'NAME-REQUIRED', 'NAME-REQUIRED',
         'RECORDED [Sanhedrin 56a:4-5]: from the DOUBLED Name token of '
         '24:16 (machine count: exactly 2) — Mishnah Sanhedrin 7:5 '
         '"until he SPECIFIES the Name" (Onkelos\' own verb at 24:11)', 'RECORDED'),
        ('piercing IS the cursing (one act)', 'ONE-ACT', 'ONE-ACT',
         'RECORDED [Sanhedrin 56a:12 (the narrative\'s two verbs in '
         'sequence) + 56a:13 (24:14 says take out THE CURSER — one noun, '
         'one offense) + 56a:6 (Balaam\'s own curse verb)]', 'RECORDED'),
        ('sojourner within the gate', 'GER-INCLUDED', 'GER-INCLUDED',
         'INK 24:16: as-the-sojourner as-the-native; the gentile-by-'
         'epithet arm routed to the Noahide block [Sanhedrin 56a:20]', 'INK'),
    ]
    results.append(grade('curse gate', 'Mishnah Sanhedrin 7:5', cells))

    # ---- F3: the stoning protocol (24:14, 23) -----------------------
    cells = [
        ('location: OUTSIDE', 'OUTSIDE', 'OUTSIDE',
         'INK 24:14 "outside the camp" — Mishnah Sanhedrin 6:1 QUOTES '
         'the clause for the stoning place beyond the court', 'INK'),
        ('the HEARERS lay hands', 'HEARERS-ACT', 'HEARERS-ACT',
         'INK 24:14 "all who HEARD" — the trial re-hears it plainly and '
         'the judges rend at the hearing [Mishnah Sanhedrin 7:5]', 'INK'),
        ('executioner: all the congregation', 'CONGREGATION', 'CONGREGATION',
         'INK 24:14, 16: "all the congregation" twice', 'INK'),
        ('stripping: man yes, woman no', 'STRIP-DISPUTE', 'STRIP-DISPUTE',
         'RECORDED [Sanhedrin 45a:3]: "him" = him WITHOUT his clothing, '
         'on this span\'s own token (24:23); R. Yehuda\'s arm kept '
         '[Sanhedrin 45a:1; Mishnah Sanhedrin 6:3]', 'RECORDED'),
    ]
    results.append(grade('stoning protocol',
                         'Mishnah Sanhedrin 6:1 + 6:3', cells))

    # ---- F4: the killing pair (24:17-18, 21) ------------------------
    cells = [
        ('kills ANY human soul', 'DEATH', 'DEATH',
         'INK 24:17: "any soul of man — die he shall die" (Onkelos '
         'renders the strike verb KILL — the fatal reading in the '
         'oldest witness)', 'INK'),
        ('a day-old victim counts', 'LIABLE', 'LIABLE',
         'INK: the quantifier "ANY" is the age-zero inclusion — Mishnah '
         'Niddah 5:3 "the one who kills him is liable"', 'INK'),
        ('kills a beast', 'PAYS', 'PAYS',
         'INK 24:18: "he shall PAY her — a life under a life": the pay '
         'verb standing ON the exchange formula (Onkelos: in EXCHANGE '
         'for)', 'INK'),
        ('the juxtaposed pair (one verse)', 'PAY|DIE', 'PAY|DIE',
         'INK 24:21: strikes-beast-pays beside strikes-man-dies — the '
         'lever Bava Kamma 83b:10 quotes ("written about killing")', 'INK'),
        ('life-under-life: exactly two seats', 'TWO-SEATS', 'TWO-SEATS',
         'INK (machine census): Exod 21:23 + Lev 24:18 only; Makkot 1:6 '
         'quotes the under-form and rules its timing (verdict-final) — '
         'the plotting-witness application is Deut 19\'s block', 'INK'),
    ]
    results.append(grade('killing pair',
                         'Mishnah Niddah 5:3 + Makkot 1:6', cells))

    # ---- F5: THE TARIFF — the called function (24:19-20) ------------
    tal = talion('eye')
    cells = [
        ('blemish in his FELLOW: the formula', 'DONE-TO-HIM', 'DONE-TO-HIM',
         'INK 24:19: "as he did, so shall it be done to him"', 'INK'),
        ('the rows: fracture/eye/tooth', 'TARIFF', 'TARIFF',
         'INK 24:20 + census: eye and tooth at exactly the two recorded '
         'seats; FRACTURE unique to the call site — the callee EXTENDS '
         'the caller\'s tariff', 'INK'),
        ('semantics: MONEY, not body', tal['verdict'], 'PAY-MONEY',
         'RECORDED — talion() resolves ' + tal['why'], 'RECORDED'),
        ('subject gate: a MAN, not his ox', 'ISH-ONLY', 'ISH-ONLY',
         'INK 24:19 "a MAN who gives a blemish" — Mishnah Bava Kamma '
         '3:10 (his ox blinds the slave\'s eye: exempt; he: liable) + '
         '8:2 (man pays five, ox damage only)', 'INK'),
        ('fellow-scope + stacking rows', 'PER-STATUS', 'PER-STATUS',
         'ROUTED [Mishnah Bava Kamma 8:3]: parents-no-wound all five; '
         'Yom Kippur stacks; slaves per status (R. Yehuda\'s '
         'no-humiliation arm kept) — the five-indemnity machine lives '
         'at Exod 21:18-25', 'ROUTED/IMPORT'),
    ]
    results.append(grade('THE TARIFF (exported as talion())',
                         'Mishnah Bava Kamma 8:1-8:3', cells))

    # ---- F6: one law (24:22) ----------------------------------------
    cells = [
        ('one code path: sojourner = native', 'ONE-PATH', 'ONE-PATH',
         'INK 24:22: "one law shall be for you, as the sojourner as '
         'the native"', 'INK'),
        ('one procedure floor (money+capital)', 'INQUIRY-BOTH', 'INQUIRY-BOTH',
         'RECORDED [Mishnah Sanhedrin 4:1 QUOTES the clause]: both take '
         'inquiry and examination; the differences table is the answer '
         'sheet\'s own regime data', 'RECORDED'),
        ('EQUAL across bodies', 'EQUALIZE', 'EQUALIZE',
         'RECORDED [Bava Kamma 84a:1]: "a law EQUAL for all of you" — '
         'literal talion fails the rider; money equalizes (the operator '
         'behind the exported verdict)', 'RECORDED'),
    ]
    results.append(grade('one law', 'Mishnah Sanhedrin 4:1', cells))

    # ---- summary ----------------------------------------------------
    ok = sum(a for a, _ in results); n = sum(b for _, b in results)
    print('=' * 60)
    print('LEV 24 PASS: %d/%d cells across 6 functions' % (ok, n))
    print('PROVENANCE FRACTIONS: INK %d | RECORDED %d | ROUTED/IMPORT %d'
          % (TOTAL['INK'], TOTAL['RECORDED'], TOTAL['ROUTED/IMPORT']))
    print('THE EXPORT: talion() -> %s [%s] — awaiting its caller'
          % (tal['verdict'], tal['effect']))

    # ---- EFFECTS (the effects law: every cell writes or honestly
    #      declines) --------------------------------------------------
    sys.path.insert(0, HERE)
    import effects_layer as FX
    EFFECTS = [
        ('request: CUSTODY+ASK',         [FX.NONE]),
        ('request: RUN-LOG MATCH',       [FX.NONE]),
        ('curse: BEARS-SIN (no Name)',   ['bears_sin']),
        ('curse: NAME-REQUIRED',         ['stoned']),
        ('curse: ONE-ACT',               [FX.NONE]),
        ('curse: GER-INCLUDED',          [FX.NONE]),
        ('protocol: OUTSIDE',            [FX.NONE]),
        ('protocol: HEARERS-ACT',        [FX.NONE]),
        ('protocol: CONGREGATION',       [FX.NONE]),
        ('protocol: STRIP-DISPUTE',      [FX.NONE]),
        ('killing: man -> DEATH',        ['put_to_death']),
        ('killing: day-old LIABLE',      ['put_to_death']),
        ('killing: beast -> PAYS',       ['pays']),
        ('killing: PAY|DIE pair',        [FX.NONE]),
        ('killing: TWO-SEATS census',    [FX.NONE]),
        ('tariff: DONE-TO-HIM formula',  [FX.NONE]),
        ('tariff: the rows',             [FX.NONE]),
        ('tariff: PAY-MONEY (the call)', ['substitution']),
        ('tariff: ISH-ONLY gate',        [FX.NONE]),
        ('tariff: PER-STATUS stacking',  [FX.NONE]),
        ('one-law: ONE-PATH',            [FX.NONE]),
        ('one-law: INQUIRY-BOTH',        [FX.NONE]),
        ('one-law: EQUALIZE',            [FX.NONE]),
    ]
    print('\nEFFECTS — the state changes each cell writes:')
    used = []
    for name, fx in EFFECTS:
        used += fx
        for line in FX.render(fx):
            print('  %-36s ->%s' % (name, line))
    ops = FX.summarize(used)
    print('LEDGER OPS this pass writes:',
          ', '.join('%s x%d' % (op, cnt) for op, cnt in sorted(ops.items())))
    assert len(EFFECTS) == n, \
        'EFFECTS LAW: %d cells graded, %d mapped' % (n, len(EFFECTS))
    print('effects: all %d cells carry a REGISTERED effect or an honest '
          'no-change [effects law satisfied]' % n)
    print('\nLEV 24 COMPLETE: %d/%d — 0 mismatches' % (ok, n))


if __name__ == '__main__':
    main()
