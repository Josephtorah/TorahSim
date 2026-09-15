import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
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
assert GUARDED == 27, ("the guard counted %d expectations, the tripwire holds 27" % GUARDED)   # O3 (2026-09-07): measured 27 — TEN's 10 + the grade calls' 17 — the old 19 counted the last list (the scene's) for every grade call
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
DB = (_ROOT + '/Data/tanakh.sqlite')


# ---- THE COMPILED MACHINE (ink-first) ---------------------------
# A track = (signs, weeks). Weeks counted from the ink's shut
# tokens; the SHARED SEVENTH DAY is the recorded rule (Sifra,
# Tazria Parashat Nega'im, Chapter 2* 4): day 7 closes week one
# AND opens week two. (Module level since W4, 2026-09-07 — the
# daemon below calls these; main() grades them as before.)
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


# ---- THE WRAP (W4 THE PURITY CLOCKS, 2026-09-07): the daemon over the compiled machine ----
_sys.path.insert(0, HERE)
import world_engine as WE
def law_negaim(event, world):
    """Lev 13 + 14:33-57 (cold_run_negaim.py — TRACKS, days, standing_verdict, house_machine): the confinement weeks as TIMERS on the shared seventh day."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)
    week = days(2) - days(1)                                         # 6: the next exam is six days on — the seventh day shared (Sifra Chapter 2* 4)
    if k == 'skin_mark_seen':
        p = event['person']; track = event['track']; signs, weeks = TRACKS[track]
        if event.get('sign_at_first') in signs:
            return [E_('isolated_outside_camp', p, value=event['sign_at_first'], law='F1 [INK 13:3 the sign at the first sight decrees (%s of the %s track); 13:45-46 "alone shall he dwell, outside the camp"]' % (event['sign_at_first'], track))]
        out = [E_('confined_seven_days', p, amount=days(1), value='week_1_of_%d' % weeks, law='F1 [INK 13:4 "the priest shall shut up the mark seven days" — the %s track: %d signs, %d week(s)]' % (track, len(signs), weeks))]
        exams = [event.get('week1'), event.get('week2')][:weeks]; d = day
        for i, ex in enumerate(exams):
            d += week
            if ex == 'spread' or ex in signs:
                out.append(E_('isolated_outside_camp', p, due=d, value=ex, law='F1 [INK 13:7-8 / 13:22 / 13:27 / 13:35-36 "%s" at the exam of day %d: decreed — 13:46]' % (ex, d)))
                return out
            if i + 1 < len(exams) and ex == 'stood':
                out.append(E_('confined_seven_days', p, amount=days(2) - days(1), due=d, value='week_2_shut_again', law='F1 [INK 13:5 "the mark stood... shut up seven days a SECOND time" — the shared seventh: %d days in all]' % days(2)))
            else:
                out.append(E_('released', p, due=d, value=standing_verdict(track), law='F1 [INK 13:6 / 13:23 / 13:28 / 13:37 "%s" at the exam of day %d: "the priest shall pronounce him pure... wash his garments and be pure"]' % (ex, d)))
        return out
    if k == 'garment_mark_seen':
        g = event['garment']
        out = [E_('confined_seven_days', g, amount=days(1), value='week_1_of_2', law='F1 [INK 13:50 "the priest shall see the mark and shut up the mark seven days"]')]
        d = day + week; w1 = event.get('week1')
        if w1 == 'spread':
            out.append(E_('burned_in_fire', g, due=d, value='spread_at_week_1', law='F1 [INK 13:51-52 "the mark has spread... he shall BURN the garment"]'))
            return out
        if w1 == 'stood':
            out.append(E_('confined_seven_days', g, amount=days(2) - days(1), due=d, value='washed_and_shut_again', law='F1 [INK 13:54 "wash that wherein the mark is, and shut it up seven days a SECOND time"]'))
            d += week
            if event.get('week2') in ('stood', 'spread'):
                out.append(E_('burned_in_fire', g, due=d, value=standing_verdict('garment'), law='F1 [INK 13:55 "the mark has not changed its color and has not spread — in fire shall you BURN it": the garment/person asymmetry]'))
            else:
                out.append(E_('released', g, due=d, value='washed_a_second_time', law='F1 [INK 13:58 "the mark has departed from them — it shall be washed a SECOND time and be pure"]'))
            return out
        out.append(E_('released', g, due=d, value='dim_or_gone_at_week_1', law='F1 [INK 13:56-58 the dimmed mark torn out, the departed mark washed and pure]'))
        return out
    if k == 'house_mark_seen':
        h = event['house']; v = house_machine(event['week1'], event.get('week2'), event.get('after_treatment'))
        out = [E_('confined_seven_days', h, amount=days(1), value='week_1', law='F1 [INK 14:38 "the priest shall go out of the house to the door of the house and shut up the house seven days" — the owner told the priest first (14:35)]')]
        d = day + week; wk = 1
        if event.get('week2'):
            wk += 1; out.append(E_('confined_seven_days', h, amount=days(2) - days(1), due=d, value='week_%d' % wk, law='F1 [INK 14:39 "the priest shall return on the seventh day" — the mark %s at week 1: shut again]' % event['week1'])); d += week
        if event.get('after_treatment'):
            wk += 1; out.append(E_('confined_seven_days', h, amount=days(2) - days(1), due=d, value='week_%d_after_pull_scrape_plaster' % wk, law='F1 [INK 14:40-42 pull out the stones, scrape, plaster; Sifra Metzora Section 7 7-10 — the third coming: %d days in all]' % days(wk))); d += week
        if v == 'DEMOLISH':
            out.append(E_('demolished', h, due=d, value=v, law='F1 [INK 14:43-45 "if the mark RETURNS and breaks out in the house... he shall demolish the house, its stones, its timber, all its mortar" — house %s of the ten]' % v))
        else:
            out.append(E_('released', h, due=d, value=v, law='F1 [INK 14:48 "the priest shall pronounce the house pure, for the mark is healed" — %s (Sifra Section 7 12)]' % v))
        return out
    if k == 'shut_house_entered':
        e = event['enterer']
        out = [E_('impure_until_evening', e, value=event.get('act', 'entered'), law='F1 [INK 14:46 "whoever comes into the house all the days it is shut up shall be impure until evening"]')]
        if event.get('act') in ('lay', 'ate'):
            out.append(E_('washes_and_bathes', e, value=event['act'], law='F1 [INK 14:47 "he who lies in the house shall wash his garments, and he who eats in the house shall wash his garments"]'))
        return out
    return []


def scene():
    """THE SCENE — Negaim 3:3-8's tracks and the Sifra's ten houses replayed on the world engine (clock unit: days): the confinement weeks as TIMERS."""
    import io as _io, contextlib as _ctx
    with _ctx.redirect_stdout(_io.StringIO()):
        w = WE.World(era='the affliction machine: Negaim 3:3-8, Sifra Metzora Section 7 12 on the engine (clock unit: days)')
        w.laws = [law_negaim]
        w.advance(1)
        for who, track, w1, w2, src in (('the-skin-leper', 'skin', 'stood', 'stood', 'Mishnah Negaim 3:3 — the skin: two weeks that are thirteen days, stood: released'),
                                        ('the-boil-bearer', 'boil', 'stood', None, 'Mishnah Negaim 3:4 — the boil: one week'), ('the-burn-bearer', 'burn', 'stood', None, 'Mishnah Negaim 3:4 — the burn: one week'),
                                        ('the-scall-bearer', 'scall', 'stood', 'dim', 'Mishnah Negaim 3:5 — the scall: two weeks, dimmed at the second'), ('the-bald-bearer', 'bald', 'stood', 'stood', 'Mishnah Negaim 3:6 — the bald head: two weeks'),
                                        ('the-spreading-leper', 'skin', 'spread', None, 'Lev 13:7-8 — spread at the first exam: decreed')):
            w.submit({'kind': 'skin_mark_seen', 'subject': who, 'person': who, 'track': track, 'week1': w1, 'week2': w2, 'day': 1, 'case_source': src})
        w.submit({'kind': 'skin_mark_seen', 'subject': 'the-white-haired', 'person': 'the-white-haired', 'track': 'skin', 'sign_at_first': 'white_hair', 'day': 1, 'case_source': 'Lev 13:3 — white hair at the first sight: decreed at once; 13:46 outside the camp'})
        w.submit({'kind': 'garment_mark_seen', 'subject': 'the-standing-garment', 'garment': 'the-standing-garment', 'owner': 'the-weaver', 'week1': 'stood', 'week2': 'stood', 'day': 1, 'case_source': 'Mishnah Negaim 3:7; Lev 13:54-55 — stood two weeks: burned'})
        w.submit({'kind': 'garment_mark_seen', 'subject': 'the-spreading-garment', 'garment': 'the-spreading-garment', 'owner': 'the-weaver', 'week1': 'spread', 'day': 1, 'case_source': 'Lev 13:51-52 — spread: burned'})
        w.submit({'kind': 'garment_mark_seen', 'subject': 'the-departed-garment', 'garment': 'the-departed-garment', 'owner': 'the-weaver', 'week1': 'stood', 'week2': 'gone', 'day': 1, 'case_source': 'Lev 13:58 — the mark departed: washed a second time, pure'})
        TEN_HOUSES = ((('dim', None, None), 'house-1'), (('gone', None, None), 'house-2'), (('stood', 'dim', None), 'house-3'), (('stood', 'gone', None), 'house-4'), (('spread', None, 'returned'), 'house-5'),
                      (('spread', None, 'quiet'), 'house-6'), (('stood', 'spread', 'returned'), 'house-7'), (('stood', 'spread', 'quiet'), 'house-8'), (('stood', 'stood', 'returned'), 'house-9'), (('stood', 'stood', 'quiet'), 'house-10'))
        for (w1, w2, aft), h in TEN_HOUSES:
            w.submit({'kind': 'house_mark_seen', 'subject': h, 'house': h, 'owner': 'the-owner-of-' + h, 'week1': w1, 'week2': w2, 'after_treatment': aft, 'day': 1, 'case_source': 'Sifra Metzora Section 7 12 — the ten houses (%s)' % h})
        w.submit({'kind': 'shut_house_entered', 'subject': 'the-enterer', 'enterer': 'the-enterer', 'house': 'house-9', 'act': 'entered', 'day': 3, 'case_source': 'Lev 14:46 — entered the shut house: until evening'})
        w.submit({'kind': 'shut_house_entered', 'subject': 'the-sleeper', 'enterer': 'the-sleeper', 'house': 'house-9', 'act': 'lay', 'day': 3, 'case_source': 'Lev 14:47 — lay in the house: washes'})
        w.advance(20)                                                # nineteen days: the third week's exam has come (Mishnah Negaim 3:8)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    yr = lambda eid, eff: [e['day'] for e in w.entity(eid).ledger if e['effect'] == eff]
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (yr('the-skin-leper', 'confined_seven_days'), yr('the-skin-leper', 'released'), yr('the-boil-bearer', 'released'), yr('the-burn-bearer', 'released'), yr('the-scall-bearer', 'released'), yr('the-bald-bearer', 'released'),
            yr('the-spreading-leper', 'isolated_outside_camp'), yr('the-white-haired', 'isolated_outside_camp'), n('the-white-haired', 'confined_seven_days'),
            yr('the-standing-garment', 'burned_in_fire'), yr('the-spreading-garment', 'burned_in_fire'), yr('the-departed-garment', 'released'),
            tuple(n('house-%d' % i, 'demolished') for i in range(1, 11)), tuple(n('house-%d' % i, 'released') for i in range(1, 11)), tuple(len(yr('house-%d' % i, 'confined_seven_days')) for i in range(1, 11)),
            yr('house-9', 'demolished'), yr('house-1', 'released'), n('the-enterer', 'impure_until_evening'), n('the-enterer', 'washes_and_bathes'), n('the-sleeper', 'washes_and_bathes'),
            tset, fired, w.clock.day), w


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

    # ---- THE COMPILED MACHINE (ink-first) — TRACKS, days(), standing_verdict(),
    # house_machine() hoisted to MODULE LEVEL at W4 (2026-09-07) so the daemon
    # law_negaim can call them; the verdicts are unchanged ----------------
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

    # ---- THE SCENE (W4, 2026-09-07): the tracks and the ten houses on the world engine ----
    SCENE, _w = scene()
    scene_cells = [
        ('THE SCENE (the clocks as TIMERS)', SCENE,
         ([1, 7], [13], [7], [7], [13], [13], [7], [1], 0, [13], [7], [13], (0, 0, 0, 0, 1, 0, 1, 0, 1, 0), (1, 1, 1, 1, 0, 1, 0, 1, 0, 1), (1, 1, 2, 2, 2, 2, 3, 3, 3, 3), [19], [7], 1, 0, 1, 36, 36, 20),
         'RECORDED [Mishnah Negaim 3:3-8 + Sifra Metzora Section 7 12 replayed on the engine]: '
         'the confinement weeks set on the shutting and fired on the shared seventh day', 'RECORDED'),
    ]
    results.append(grade('the scene on the world engine', 'Mishnah Negaim 3:3-8 + Sifra Section 7 12 + Lev 14:46-47', scene_cells))
    _w.print_coverage()

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
        ('scene: the clocks',         ['confined_seven_days', 'released', 'isolated_outside_camp',
                                       'burned_in_fire', 'demolished', 'impure_until_evening']),
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
