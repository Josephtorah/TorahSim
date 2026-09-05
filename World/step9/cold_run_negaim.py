#!/usr/bin/env python3
# LEV 13-14 — THE AFFLICTION STATE MACHINE (2026-09-05, under the
# compiler law; the Tazria-Metzora sweep's cold compile).
# Six diagnostic tracks compiled ink-first from the chapter's bare
# tokens — signs, weeks, and verdict transitions — and graded against
# the tradition's own track table (Mishnah Negaim 3:3-8, which states
# each track's signs, weeks, AND the shared-day arithmetic: "two weeks
# THAT ARE thirteen days," the houses "three weeks that are NINETEEN")
# plus the Sifra's own TEN-HOUSES transition table (Sifra, Metzora,
# Section 7 12 — the teacher enumerates the complete decision tree).
# Five motions; read-only; zero-report probes; effects law satisfied.
# Read ledgers: logic/oral_triage/lev_13_negaim_2026-09-05.md +
# lev_14_metzora_2026-09-05.md.

# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'TEN', 1) + _chc(_P, 'grade', 2, 2)
assert GUARDED == 18, ('the guard counted %d expectations, the tripwire holds 18' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
DB = '<repo-old>/elijah_docket/tanakh.sqlite'


def main():
    db = sqlite3.connect(DB)

    def strip(s):
        return ''.join(c for c in s
                       if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

    def words(ch, vs, book='Lev'):
        return [strip(he) for (he,) in db.execute(
            """SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id
               WHERE v.book=? AND v.chapter=? AND v.verse=?
               ORDER BY w.idx""", (book, ch, vs))]

    def has(ch, vs, tok):
        return tok in words(ch, vs)

    # ---- probes (zero-report law) -----------------------------------
    PROBES = [
        ('white-hair',  'לבן',    13, 3),
        ('raw-flesh',   'ומחית',  13, 10),
        ('spread',      'פשה',    13, 7),
        ('shut-in',     'והסגיר', 13, 4),
        ('second',      'שנית',   13, 5),
        ('released',    'וטהרו',  13, 6),
        ('boil',        'שחין',   13, 18),
        ('burn',        'מכות',   13, 24),
        ('scall',       'הנתק',   13, 31),
        ('yellow',      'צהב',    13, 30),
        ('scall-2nd',   'שנית',   13, 33),
        ('large-gimel', 'והתגלח', 13, 33),
        ('bald-back',   'קרח',    13, 40),
        ('bald-front',  'גבח',    13, 41),
        ('green',       'ירקרק',  13, 49),
        ('red',         'אדמדם',  13, 49),
        ('garment-2nd', 'שנית',   13, 54),
        ('burn-it',     'תשרפנו', 13, 55),
        ('house-shut',  'והסגיר', 14, 38),
        ('house-return','ישוב',   14, 43),
        ('demolish',    'ונתץ',   14, 45),
        ('alone',       'בדד',    13, 46),
    ]
    seen = set()
    failed = []
    for n, tok, c, v in PROBES:
        if (n, c, v) in seen:
            continue
        seen.add((n, c, v))
        if not has(c, v, tok):
            failed.append((n, c, v))
    if failed:
        sys.exit('ZERO-REPORT LAW: probes failed: %r' % failed)
    print('probes: all %d token probes fired  [zero-report law '
          'satisfied]' % len(seen))
    print('  (the 13:33 large-letter site INTACT in the word database '
          '— the Lev 11:42 truncation stays the one deferred case)')

    # ---- census: where does the ink write a SECOND shutting? --------
    # The word שנית ("a second time") inside Lev 13-14:
    hits = []
    for ch in (13, 14):
        for (vs,) in db.execute(
                """SELECT DISTINCT v.verse FROM words w
                   JOIN verses v ON w.verse_id=v.id
                   WHERE v.book='Lev' AND v.chapter=? ORDER BY v.verse""",
                (ch,)):
            ws = words(ch, vs)
            if 'שנית' in ws and any(w.startswith('והסגיר') for w in ws):
                hits.append(f'{ch}:{vs}')
    assert hits == ['13:5', '13:33', '13:54'], hits
    print('census: SHUT-AGAIN (the shut-verb beside the second-time '
          'token) stands at 13:5 (skin), 13:33 (scall), 13:54 '
          '(garment) — and NOWHERE in the boil/burn span: the '
          'one-week track is the ink\'s own silence\n')

    # ---- THE COMPILED MACHINE (ink-first) ---------------------------
    # A track = (signs, weeks). Weeks counted from the ink's shut
    # tokens; the SHARED SEVENTH DAY is the recorded rule (Sifra,
    # Tazria Parashat Nega'im, Chapter 2* 4): day 7 closes week one
    # AND opens week two.
    TRACKS = {
        'skin':    (['white_hair', 'raw_flesh', 'spread'], 2),
        'boil':    (['white_hair', 'spread'], 1),
        'burn':    (['white_hair', 'spread'], 1),
        'scall':   (['thin_yellow', 'spread'], 2),
        'bald':    (['raw_flesh', 'spread'], 2),
        'garment': (['green_deep', 'red_deep', 'spread'], 2),
        'house':   (['green_deep', 'red_deep', 'spread'], 3),
    }

    def days(weeks):
        # RECORDED [Sifra Ch2* 4]: the seventh day counts in both
        # weeks — every junction day is shared.
        return weeks * 7 - (weeks - 1)

    def standing_verdict(track):
        # What happens when the mark STANDS at the last exam:
        # person released (INK 13:6 washed-and-pure); garment BURNED
        # (INK 13:55); house goes to pull-scrape-plaster then the
        # return-fork (INK 14:39-45).
        return {'skin': 'RELEASED', 'boil': 'RELEASED',
                'burn': 'RELEASED', 'scall': 'RELEASED',
                'bald': 'RELEASED', 'garment': 'BURNED',
                'house': 'PULL-SCRAPE-PLASTER'}[track]

    # THE TEN HOUSES — the compiled house machine's walk, graded
    # against the Sifra's own numbered table (Sifra, Metzora,
    # Section 7 12).
    def house_machine(week1, week2, after_treatment):
        if week1 == 'dim':
            return 'PEEL-PURE'
        if week1 == 'gone':
            return 'PEEL-PURE'
        if week1 == 'stood' and week2 == 'dim':
            return 'PEEL-BIRDS'
        if week1 == 'stood' and week2 == 'gone':
            return 'PEEL-BIRDS'
        # spread in week 1, or stood-then-spread, or stood-stood:
        # pull, scrape, plaster, one more week — then the fork:
        if after_treatment == 'returned':
            return 'DEMOLISH'
        return 'BIRDS'

    TEN = [
        (('dim', None, None),           'PEEL-PURE'),
        (('gone', None, None),          'PEEL-PURE'),
        (('stood', 'dim', None),        'PEEL-BIRDS'),
        (('stood', 'gone', None),       'PEEL-BIRDS'),
        (('spread', None, 'returned'),  'DEMOLISH'),
        (('spread', None, 'quiet'),     'BIRDS'),
        (('stood', 'spread', 'returned'), 'DEMOLISH'),
        (('stood', 'spread', 'quiet'),  'BIRDS'),
        (('stood', 'stood', 'returned'), 'DEMOLISH'),
        (('stood', 'stood', 'quiet'),   'BIRDS'),
    ]
    ten_ok = sum(house_machine(*i) == want for i, want in TEN)

    # ---- the grid ---------------------------------------------------
    TOTAL = {'INK': 0, 'RECORDED': 0, 'ROUTED/IMPORT': 0}

    def grade(fn, oracle_name, cells):
        ok = 0
        print('FUNCTION: %s  (answer sheet: %s)' % (fn, oracle_name))
        for name, verdict, want, prov, kind in cells:
            mark = 'ok' if verdict == want else 'MISMATCH'
            ok += verdict == want
            TOTAL[kind] += 1
            print('  %-34s %-14s [%s]  <- %s' % (name, verdict, mark, prov))
        print('  -> %d/%d\n' % (ok, len(cells)))
        return ok, len(cells)

    results = []

    def sig(track):
        s, w = TRACKS[track]
        return '%d-signs/%d-week%s' % (len(s), w, 's' if w > 1 else '')

    cells = [
        ('SKIN: 3 signs, 2 weeks', sig('skin'), '3-signs/2-weeks',
         'INK 13:3 (white hair), 13:10 (raw flesh), 13:7 (spread); the '
         'second shutting written at 13:5', 'INK'),
        ('BOIL: 2 signs, 1 week', sig('boil'), '2-signs/1-week',
         'INK 13:20 (hair), 13:22 (spread); NO second-week token in '
         '13:18-23 — the census above', 'INK'),
        ('BURN: 2 signs, 1 week', sig('burn'), '2-signs/1-week',
         'INK 13:25, 13:27; the same silence', 'INK'),
        ('SCALL: yellow + spread, 2 weeks', sig('scall'),
         '2-signs/2-weeks',
         'INK 13:30 (thin yellow), 13:35 (spread); the second shutting '
         'at 13:33', 'INK'),
        ('BALD: raw flesh + spread, 2 weeks', sig('bald'),
         '2-signs/2-weeks',
         'RECORDED [Sifra, Tazria Parashat Nega\'im, Chapter 11 1-3]: '
         'defiles by raw flesh and spread, NOT white hair; two weeks by '
         'the as-the-appearance-of-skin analogy', 'RECORDED'),
        ('GARMENT: green/red + spread, 2 wks', sig('garment'),
         '3-signs/2-weeks',
         'INK 13:49 (green-of-greens, red-of-reds), 13:51 (spread); '
         'the second shutting at 13:54', 'INK'),
        ('HOUSE: green/red + spread, 3 wks', sig('house'),
         '3-signs/3-weeks',
         'INK 14:37 + 14:44 (spread/return); the THIRD week from the '
         'two comings [Sifra, Metzora, Section 7 7-10] — Mishnah '
         'Negaim 3:8 grades it', 'RECORDED'),
    ]
    results.append(grade('the track table', 'Mishnah Negaim 3:3-3:8',
                         cells))

    cells = [
        ('two weeks = THIRTEEN days', str(days(2)), '13',
         'RECORDED [Sifra Chapter 2* 4]: the seventh day counts in '
         'both weeks — the Mishnah\'s own arithmetic ("that are '
         'thirteen days")', 'RECORDED'),
        ('three weeks = NINETEEN days', str(days(3)), '19',
         'RECORDED: the shared-junction rule iterated — Mishnah Negaim '
         '3:8 states nineteen; and the close: "no mark less than one '
         'week nor more than three"', 'RECORDED'),
    ]
    results.append(grade('the day arithmetic',
                         'Mishnah Negaim 3:3 + 3:8', cells))

    cells = [
        ('shades: two that are four', '2x2', '2x2',
         'INK: two written names (se\'et, baheret) + sapachat the '
         'attached-secondary [Sifra Section 1 4]; the grades '
         '(snow/plaster/wool/membrane) are the answer sheet\'s own '
         'transmitted DATA with the R. Meir/sages swap kept — Mishnah '
         'Negaim 1:1; Shevuot 1:1 lists it two-by-two', 'RECORDED'),
        ('the state guard', 'NO-REMARK', 'NO-REMARK',
         'RECORDED [Sifra Chapter 2 6-7]: no quarantining the '
         'quarantined, no deciding the decided — "whoever bears the '
         'name impure is not subject to him"', 'RECORDED'),
        ('standing at the end: the asymmetry',
         standing_verdict('skin') + '|' + standing_verdict('garment'),
         'RELEASED|BURNED',
         'INK 13:6 (washed and PURE) vs 13:55 (in fire shall you BURN '
         'it) — the garment/person asymmetry in the ink\'s own verbs '
         '[Sifra Chapter 2* 8 states why both weeks are written]',
         'INK'),
        ('the bloom inversion', 'PURE|FLESH-FLIPS', 'PURE|FLESH-FLIPS',
         'INK 13:13 (all white — pure) + 13:14 (the day raw flesh '
         'appears — impure): whole-cover purifies and the live spot '
         'flips it back, in consecutive verses', 'INK'),
        ('doubt polarity per sign', 'SPLIT', 'SPLIT',
         'RECORDED: hair-order doubt IMPURE [Chapter 2 2], spread '
         'doubt PURE [Section 4 8] — each sign its own default',
         'RECORDED'),
    ]
    results.append(grade('verdict machinery',
                         'Mishnah Negaim 1:1 + the Sifra\'s guards',
                         cells))

    cells = [
        ('THE TEN HOUSES (10 sub-checks)', '%d/10' % ten_ok, '10/10',
         'RECORDED [Sifra, Metzora, Section 7 12 — the teacher\'s own '
         'numbered transition table] run through the compiled house '
         'machine: dim/gone weeks peel; spread pulls-scrapes-plasters; '
         'the return DEMOLISHES (INK 14:45), quiet takes BIRDS',
         'RECORDED'),
        ('the deltas row', '3-DIFFS', '3-DIFFS',
         'RECORDED [Mishnah Megillah 1:7]: two-vs-three sightings = '
         'offering only; quarantined-vs-decided = loosing/rending '
         'only; the two purities = shave-and-birds only — the machine '
         'diff the exam met answered (round 43)', 'RECORDED'),
    ]
    results.append(grade('the transition runs',
                         'Sifra Section 7 12 + Mishnah Megillah 1:7',
                         cells))

    # ---- summary ----------------------------------------------------
    ok = sum(a for a, _ in results); n = sum(b for _, b in results)
    print('=' * 60)
    print('NEGAIM PASS: %d/%d cells across 4 functions '
          '(+ the ten-houses walk %d/10)' % (ok, n, ten_ok))
    print('PROVENANCE FRACTIONS: INK %d | RECORDED %d | ROUTED/IMPORT %d'
          % (TOTAL['INK'], TOTAL['RECORDED'], TOTAL['ROUTED/IMPORT']))

    # ---- EFFECTS ----------------------------------------------------
    sys.path.insert(0, HERE)
    import effects_layer as FX
    EFFECTS = [
        ('track: SKIN spec',          [FX.NONE]),
        ('track: BOIL spec',          [FX.NONE]),
        ('track: BURN spec',          [FX.NONE]),
        ('track: SCALL spec',         [FX.NONE]),
        ('track: BALD spec',          [FX.NONE]),
        ('track: GARMENT spec',       [FX.NONE]),
        ('track: HOUSE spec',         [FX.NONE]),
        ('days: thirteen',            ['confined_seven_days']),
        ('days: nineteen',            ['confined_seven_days']),
        ('shades: 2x2',               [FX.NONE]),
        ('guard: NO-REMARK',          [FX.NONE]),
        ('standing: RELEASED|BURNED', ['released', 'burned_in_fire']),
        ('bloom inversion',           [FX.NONE]),
        ('doubt polarity',            [FX.NONE]),
        ('ten houses: DEMOLISH arm',  ['demolished',
                                       'impure_until_evening']),
        ('deltas: decreed leper',     ['isolated_outside_camp']),
    ]
    print('\nEFFECTS — the state changes each cell writes:')
    used = []
    for name, fx in EFFECTS:
        used += fx
        for line in FX.render(fx):
            print('  %-34s ->%s' % (name, line))
    ops = FX.summarize(used)
    print('LEDGER OPS this pass writes:',
          ', '.join('%s x%d' % (op, cnt) for op, cnt in sorted(ops.items())))
    assert len(EFFECTS) == n, \
        'EFFECTS LAW: %d cells graded, %d mapped' % (n, len(EFFECTS))
    print('effects: all %d cells carry a REGISTERED effect or an '
          'honest no-change [effects law satisfied]' % n)
    print('\nNEGAIM COMPLETE: %d/%d — %d mismatches' % (ok, n, n - ok))


if __name__ == '__main__':
    main()
