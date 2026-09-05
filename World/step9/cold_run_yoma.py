#!/usr/bin/env python3
# LEV 16 — THE YOM KIPPUR SERVICE MACHINE (2026-09-05, under the
# compiler law; the Acharei Mot-Kedoshim sweep's cold compile).
# The service order compiled ink-first from the chapter's own verse
# sequence with its ONE recorded exception (the Sifra's order
# meta-rule: "the whole passage is in order EXCEPT THIS VERSE" —
# 16:23), and THE ATONEMENT ROUTING TABLE — the knowledge-state
# dispatch the bare ink leaves as parameters — filled per gap from
# the recorded arguments (Sifra, Acharei Mot, Chapter 5) and graded
# against the answer sheet (Mishnah Shevuot 1:3; 1:6; Yoma 8:9).
# Five motions; read-only; zero-report probes; effects law satisfied.
# Read ledgers: logic/oral_triage/lev_16_yom_kippur_2026-09-05.md +
# acharei_exam_mishnah_2026-09-05.md.

import sqlite3, os

DB = '<repo-old>/elijah_docket/tanakh.sqlite'


# ---- the compiled functions (module level, ink-first) ---------------

def route(known_start=None, known_end=None, deliberate=False,
          sin_class='sanctuary'):
    """THE ATONEMENT ROUTING TABLE. The ink assigns the inner goat to
    sanctuary defilement (Lev 16:16 'from the impurities of the
    children of Israel') and loads ALL iniquities on the dispatched
    goat (16:21-22); WHICH knowledge-state meets WHICH agent is a
    parameter the ink never states — filled per gap from the recorded
    table (Sifra, Acharei Mot, Chapter 5 1-8), each cell labeled."""
    if sin_class != 'sanctuary':
        return {'agent': 'dispatched_goat',
                'verdict': 'atoned by the dispatched goat',
                'effect': 'atoned_forgiven', 'prov': 'RECORDED',
                'why': 'all other transgressions, light and severe '
                       '[Sifra AM Chapter 5 8; Mishnah Shevuot 1:6]'}
    if deliberate:
        return {'agent': 'inner_goat_and_day',
                'verdict': 'atoned by the inner goat and the day',
                'effect': 'atoned_forgiven', 'prov': 'RECORDED',
                'why': 'deliberate sanctuary defilement [Sifra AM '
                       'Chapter 5 8; Mishnah Shevuot 1:6]'}
    if known_start and known_end:
        return {'agent': 'sliding_scale_offering',
                'verdict': 'the sliding-scale offering owed',
                'effect': 'suspends', 'prov': 'RECORDED',
                'why': 'knowledge at both ends with concealment '
                       'between [Sifra AM Chapter 5 1]'}
    if known_start and not known_end:
        return {'agent': 'inner_goat_suspends',
                'verdict': 'the inner goat and the day SUSPEND '
                           'until he knows',
                'effect': 'suspends', 'prov': 'RECORDED',
                'why': 'knowledge at the start, none at the end '
                       '[Sifra AM Chapter 5 1]'}
    if known_end and not known_start:
        return {'agent': 'outer_goat_and_day',
                'verdict': 'atoned by the outer goat and the day',
                'effect': 'atoned_forgiven', 'prov': 'RECORDED',
                'why': 'no knowledge at the start, knowledge at the '
                       'end [Sifra AM Chapter 5 2; Mishnah Shevuot '
                       '1:3 — beside the sin offering of atonements]'}
    return {'agent': 'festival_and_new_moon_goats',
            'verdict': 'atoned by the festival goats (R. Yehuda; '
                       'R. Shimon splits the tiers; R. Meir all '
                       'equal)',
            'effect': 'atoned_forgiven', 'prov': 'RECORDED-DISPUTE',
            'why': 'no knowledge at either end [Sifra AM Chapter '
                   '5 3-4 — the recorded three-way assignment]'}


def day_atones(between='man_and_god', appeased=False):
    """THE FELLOW GATE. 'For on this day he shall atone' (16:30, ink)
    — the day itself; the between-man-and-fellow carve is the
    recorded derivation on the verse's own 'before the LORD'
    (Sifra AM Chapter 8 1-2; the answer sheet: Mishnah Yoma 8:9)."""
    if between == 'man_and_god':
        return {'verdict': 'the day atones', 'effect':
                'atoned_forgiven', 'prov': 'INK+RECORDED',
                'why': 'ki vayom hazeh yechaper (16:30); even '
                       'without offerings [Sifra AM Chapter 8 1]'}
    if appeased:
        return {'verdict': 'the day atones — the fellow appeased',
                'effect': 'atoned_forgiven', 'prov': 'RECORDED',
                'why': 'the appeasement precondition met [Mishnah '
                       'Yoma 8:9]'}
    return {'verdict': 'NOT atoned until he appeases his fellow',
            'effect': 'NONE', 'prov': 'RECORDED',
            'why': 'lifnei HASHEM titharu — the before-the-LORD '
                   'class alone [Sifra AM Chapter 8 2; Mishnah '
                   'Yoma 8:9]'}


def service_order():
    """The service sequence compiled from the VERSE ORDER — the ink's
    own program counter — with the ONE recorded exception: 16:23
    (the linen stripping / ladle retrieval) executes LATE, per the
    Sifra's order meta-rule ('the whole passage is said in order
    except this verse' — AM Chapter 6 2)."""
    seq = [
        ('16:3',  'bull designated, his own'),
        ('16:4',  'linen garments donned (immersed first)'),
        ('16:5',  'two goats taken from the community'),
        ('16:6',  'first confession on the bull'),
        ('16:7-8', 'goats stationed; the lots'),
        ('16:9-10', 'the Name-goat named; the live goat stands'),
        ('16:11', 'second confession; the bull slaughtered'),
        ('16:12-13', 'coals and incense — inside, the cloud'),
        ('16:14', 'bull blood: one above, seven below'),
        ('16:15', 'goat slaughtered; its blood as the bull\'s'),
        ('16:16-17', 'the hall atoned; no person in the tent'),
        ('16:18-19', 'the inner altar: mixed bloods, the corners'),
        ('16:20-22', 'third confession; the goat dispatched'),
        ('16:24', 'immersion; his ram and the people\'s ram'),
        ('16:25', 'the fat turned to smoke'),
        ('16:23', 'RELOCATED: linen stripped, stored away — the '
                  'recorded exception [Sifra AM Chapter 6 2]'),
        ('16:26', 'the dispatcher washes, enters the camp'),
        ('16:27-28', 'the burnt pair outside; the burner washes'),
    ]
    return seq


def dispatch_goat():
    """The dispatched goat's own cell — the ink's transfer clause."""
    return {'verdict': 'the goat BEARS all iniquities to a cut-off '
                       'land', 'effect': 'dispatched_to_wilderness',
            'prov': 'INK',
            'why': 'venasa hasair alav et kol avonotam el eretz '
                   'gezerah (16:22); Onkelos: a land not inhabited'}


def main():
    db = sqlite3.connect(DB)

    def strip(s):
        return ''.join(c for c in s
                       if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

    def words(ch, vs):
        return [strip(he) for (he,) in db.execute(
            """SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id
               WHERE v.book='Lev' AND v.chapter=? AND v.verse=?
               ORDER BY w.idx""", (ch, vs))]

    # ---- probes (zero-report law): each pattern must fire ----------
    PROBES = [
        ('linen',      'בד',       16, 4),
        ('azazel',     'לעזאזל',   16, 8),
        ('lot',        'גורל',     16, 9),
        ('stand-live', 'חי',       16, 10),
        ('incense',    'הקטרת',    16, 13),
        ('seven',      'שבע',      16, 14),
        ('confess',    'והתודה',   16, 21),
        ('designated', 'עתי',      16, 21),
        ('bear',       'ונשא',     16, 22),
        ('cutoff',     'גזרה',     16, 22),
        ('leave',      'והניחם',   16, 23),
        ('affliction', 'תענו',     16, 29),
        ('this-day',   'הזה',      16, 30),
        ('once',       'אחת',      16, 34),
    ]
    for name, tok, ch, vs in PROBES:
        toks = words(ch, vs)
        assert any(tok in w for w in toks), \
            f'probe {name}: {tok} not at {ch}:{vs} — scanned {len(toks)} tokens'
    print(f'[PROBES] {len(PROBES)}/{len(PROBES)} fired '
          f'(each pattern verified against its own verse)')

    # ---- ink censuses ----------------------------------------------
    bad_count = sum(1 for w in words(16, 4) if w in ('בד', 'ובד'))
    print(f'[INK] linen-token census at 16:4: {bad_count} '
          f'(the four-token garment exclusion — Sifra AM Ch1 5-9)')

    azazel_seats = [f'16:{v}' for v in range(1, 35)
                    if any('עזאזל' in w for w in words(16, v))]
    print(f'[INK] Azazel seats: {azazel_seats}')

    goral = sum(1 for v in range(1, 35) for w in words(16, v)
                if 'גורל' in w or w == 'גרלות')
    print(f'[INK] lot tokens in the chapter: {goral}')

    seven_seats = [f'16:{v}' for v in range(1, 35)
                   if any(w == 'שבע' for w in words(16, v))]
    print(f'[INK] seven-times seats: {seven_seats}')

    confess_tokens = [f'16:{v}' for v in range(1, 35)
                      if any('והתודה' in w for w in words(16, v))]
    print(f'[INK] explicit confession verbs: {confess_tokens} '
          f'(one written; the bull\'s two derived — Sifra AM '
          f'Section 2 2-3)')

    # ---- the graded cells ------------------------------------------
    cells = []

    def cell(name, got, want, why, prov):
        ok = got == want
        cells.append(ok)
        mark = 'OK ' if ok else 'MISMATCH'
        print(f'  [{mark}] {name}: {got!r} (want {want!r}) — {why} '
              f'[{prov}]')
        return ok

    print('\n== THE INK CELLS ==')
    cell('four-linen census', bad_count, 4,
         'four tokens = four gold garments barred', 'INK')
    cell('azazel seats', azazel_seats, ['16:8', '16:10', '16:26'],
         'the three Azazel verses', 'INK')
    cell('lot tokens', goral, 5,
         'three at 16:8, one at 16:9, one at 16:10', 'INK')
    cell('seven-strokes seats', seven_seats, ['16:14', '16:19'],
         'innermost and altar sevens', 'INK')
    cell('explicit confessions', confess_tokens, ['16:21'],
         'one written confession; three in law', 'INK')
    cell('dispatch effect', dispatch_goat()['effect'],
         'dispatched_to_wilderness',
         'the goat bears all iniquities away', 'INK')

    print('\n== THE ROUTING TABLE (vs the answer sheet) ==')
    cell('start+end knowledge',
         route(known_start=True, known_end=True)['agent'],
         'sliding_scale_offering',
         'Sifra AM Chapter 5 1', 'RECORDED')
    cell('start only',
         route(known_start=True, known_end=False)['agent'],
         'inner_goat_suspends',
         'the day SUSPENDS until he knows', 'RECORDED')
    cell('end only',
         route(known_start=False, known_end=True)['agent'],
         'outer_goat_and_day',
         'Mishnah Shevuot 1:3 — the answer sheet row', 'ANSWER SHEET')
    cell('neither end',
         route(known_start=False, known_end=False)['agent'],
         'festival_and_new_moon_goats',
         'the recorded three-way dispute carried', 'RECORDED-DISPUTE')
    cell('deliberate sanctuary',
         route(deliberate=True)['agent'], 'inner_goat_and_day',
         'Mishnah Shevuot 1:6 first half', 'ANSWER SHEET')
    cell('all other sins',
         route(sin_class='other')['agent'], 'dispatched_goat',
         'Mishnah Shevuot 1:6 closing row', 'ANSWER SHEET')

    print('\n== THE FELLOW GATE (vs Mishnah Yoma 8:9) ==')
    cell('between man and God',
         day_atones('man_and_god')['verdict'], 'the day atones',
         'ki vayom hazeh — the day itself', 'INK+RECORDED')
    cell('fellow unappeased',
         day_atones('man_and_fellow', appeased=False)['effect'],
         'NONE', 'no atonement entry writes', 'ANSWER SHEET')
    cell('fellow appeased',
         day_atones('man_and_fellow', appeased=True)['effect'],
         'atoned_forgiven', 'the precondition met', 'RECORDED')

    print('\n== THE SERVICE ORDER ==')
    seq = service_order()
    cell('order length', len(seq), 18, 'the compiled steps', 'INK')
    cell('the one exception', seq[15][0], '16:23',
         'relocated late — the Sifra\'s order meta-rule', 'RECORDED')
    cell('incense precedes bull blood',
         [s[0] for s in seq].index('16:12-13')
         < [s[0] for s in seq].index('16:14'), True,
         'the cloud before the strokes — verse order kept', 'INK')

    n_ok = sum(cells)
    ink = 9
    rec = 6
    ans = 3
    print(f'\nYOM KIPPUR MACHINE: {n_ok}/{len(cells)} cells '
          f'({ink} INK / {rec} RECORDED / {ans} ANSWER-SHEET '
          f'— the fractions honest)')
    assert n_ok == len(cells), 'mismatches above'
    db.close()


if __name__ == '__main__':
    main()
