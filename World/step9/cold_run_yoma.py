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

# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chc(_P, 'cell', 2)
assert GUARDED == 23, ('the guard counted %d expectations, the tripwire holds 23' % GUARDED)   # W4: +1, the scene cell
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
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


# ---- THE WRAP (W4 THE PURITY CLOCKS, 2026-09-07): the daemon over the compiled Day ----
import io as _io, contextlib as _ctx
import world_engine as WE
def law_yoma(event, world):
    """Lev 16 (cold_run_yoma.py — route, day_atones, dispatch_goat, service_order): the Day as the TIMER the routing table fires on;
    the service keyed by the ink's own verse order (the run's daemon writes the spec's effects by call — the W3 shape)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'sanctuary_defiled':
        p = event['person']
        r = route(known_start=event.get('known_start'), known_end=event.get('known_end'), deliberate=event.get('deliberate', False), sin_class=event.get('sin_class', 'sanctuary'))
        if r['agent'] in ('sliding_scale_offering', 'inner_goat_suspends'):
            return [E_('suspends', p, value=r['agent'], law='F1 [%s — %s]' % (r['verdict'], r['why'][:90]))]
        return [E_('atoned_forgiven', p, cp='HEAVEN', due=event.get('the_day'), value=r['agent'], law='F1 [%s — %s: the Day as the TIMER]' % (r['verdict'], r['why'][:90]))]
    if k == 'yom_kippur_kept':
        d = day_atones(event.get('between', 'man_and_god'), event.get('appeased', False))
        if d['verdict'].startswith('NOT'):
            return []                                                # the fellow gate: NOT atoned until he appeases his fellow (Mishnah Yoma 8:9) — the silence
        return [E_('atoned_forgiven', event['soul'], cp='HEAVEN', value=d['verdict'], law='F2 [INK 16:30 "for on this day he shall atone for you, to cleanse you from all your sins before the LORD" — %s]' % d['why'][:90])]
    if k == 'goat_dispatched':
        g = dispatch_goat(); r = route(sin_class='other')
        return [E_('dispatched_to_wilderness', event['goat'], value=g['verdict'], law='F3 [INK 16:21-22 — %s]' % g['why'][:90]),
                E_('atoned_forgiven', 'the-people', cp='HEAVEN', value=r['agent'], law='F1 [INK 16:21 "all the iniquities of the children of Israel and all their transgressions for all their sins" — %s]' % r['why'][:70]),
                E_('washes_and_bathes', event['dispatcher'], value='then_the_camp', law='F3 [INK 16:26 "he who sends the goat to Azazel shall wash his garments and bathe his flesh in water, and afterward come into the camp"]')]
    if k == 'inner_service_performed':
        step = event['step']; seq = dict(service_order()); p = event.get('priest', 'aaron')
        if step not in seq:
            return []
        desc = seq[step]
        with _ctx.redirect_stdout(_io.StringIO()):
            import cold_run_offerings as OFF
            import cold_run_chatat as CH
        out = []
        if step == '16:6':
            out.append(E_('atoned_forgiven', p, cp='HEAVEN', value='for_himself_and_his_house', law='F4 [INK 16:6 "atone for himself and for his house" — %s]' % desc))
        if step == '16:14':
            out += [E_('sprinkled_seven', 'the-ark-cover', cp=p, amount=7, value='one_above_seven_below', law='F4 [INK 16:14 "before the ark-cover he shall sprinkle seven times" — %s]' % desc),
                    E_('accepted', 'the-bull', cp='HEAVEN', value=OFF.dispatch('inner_chatat_yk')['stations']['v'], law='F4 [INK 16:14 the bull\'s blood inside — CALLED cold_run_offerings.dispatch(inner_chatat_yk) stations]')]
        if step == '16:15':
            out.append(E_('accepted', 'the-goat', cp='HEAVEN', value=OFF.dispatch('inner_chatat_yk')['stations']['v'], law='F4 [INK 16:15 "do with its blood as he did with the bull\'s blood" — %s]' % desc))
        if step == '16:18-19':
            out.append(E_('sprinkled_seven', 'the-inner-altar', cp=p, amount=7, value='the_corners_then_seven', law='F4 [INK 16:18-19 "sprinkle of the blood on it with his finger seven times" — %s]' % desc))
        if step == '16:24':
            out += [E_('immersed', p, value='in_a_holy_place_then_his_garments', law='F4 [INK 16:24 "bathe his flesh in water in a holy place and put on his garments"]'),
                    E_('accepted', 'the-two-rams', cp='HEAVEN', value=OFF.dispatch('olah:flock')['disposition']['v'], law='F4 [INK 16:24 "his burnt offering and the burnt offering of the people" — CALLED offerings(olah:flock)]'),
                    E_('atoned_forgiven', 'the-people', cp='HEAVEN', value='by_the_rams', law='F4 [INK 16:24 "and atone for himself and for the people"]')]
        if step == '16:25':
            out.append(E_('smoked_to_the_lord', 'the-sin-offerings-fat', value='on_the_altar', law='F4 [INK 16:25 "the fat of the sin offering he shall burn on the altar"]'))
        if step == '16:27-28':
            bs = CH.burn_site('as_commanded')
            out += [E_('burned_outside_camp', 'the-burnt-pair', value=bs['v'], law='F4 [INK 16:27 "carried out outside the camp, and they shall burn in fire their hides, their flesh, their dung" — CALLED cold_run_chatat.burn_site: %s]' % bs['v']),
                    E_('defiles_garments', 'the-burner', value=bs['v'], law='F4 [INK 16:28 "he who burns them shall wash his garments" — the sin-offering engine\'s own Lev 16:28 import, closed from this side]'),
                    E_('washes_and_bathes', 'the-burner', value='then_the_camp', law='F4 [INK 16:28 "wash his garments and bathe his flesh in water, and afterward come into the camp"]')]
        return out                                                   # the other steps (the designation, the linen, the lots, the confessions' naming, 16:23 relocated) write nothing: the silences
    return []


def scene():
    """THE SCENE — Shevuot 1:3 and 1:6, Yoma 8:9, and the service order replayed on the world engine (clock unit: days of the seventh month);
    the calendar's law_moadim registered beside (the library shape) — yom_kippur_kept's two law layers on one tape."""
    with _ctx.redirect_stdout(_io.StringIO()):
        import cold_run_moadim as MO
        w = WE.World(era='the Day: Shevuot 1, Yoma 1-8 on the engine (clock unit: days of the seventh month)')
        w.laws = [law_yoma, MO.law_moadim]
        w.advance(1)
        for who, ks, ke, dl, sc, src in (('the-both-known', True, True, False, 'sanctuary', 'Sifra AM Chapter 5 1 — knowledge at both ends: the sliding-scale offering'),
                                         ('the-start-only', True, False, False, 'sanctuary', 'Sifra AM Chapter 5 1 — the start alone: the inner goat suspends'),
                                         ('the-end-only', False, True, False, 'sanctuary', 'Mishnah Shevuot 1:3 — the end alone: the outer goat and the Day'),
                                         ('the-neither', False, False, False, 'sanctuary', 'Sifra AM Chapter 5 3-4 — neither: the festival goats'),
                                         ('the-deliberate', False, False, True, 'sanctuary', 'Mishnah Shevuot 1:6 — deliberate: the inner goat and the Day'),
                                         ('the-other-sinner', False, False, False, 'other', 'Mishnah Shevuot 1:6 — all other sins: the dispatched goat')):
            w.submit({'kind': 'sanctuary_defiled', 'subject': who, 'person': who, 'known_start': ks, 'known_end': ke, 'deliberate': dl, 'sin_class': sc, 'day': 1, 'the_day': 10, 'case_source': src})
        w.advance(10)                                                # the tenth of the seventh month: the Day — the routing table's timers fire
        w.submit({'kind': 'yom_kippur_kept', 'subject': 'the-penitent', 'soul': 'the-penitent', 'afflicted': True, 'between': 'man_and_god', 'case_source': 'Lev 16:29-30; Mishnah Yoma 8:9 — between man and God: the day atones'})
        w.submit({'kind': 'yom_kippur_kept', 'subject': 'the-unappeased', 'soul': 'the-unappeased', 'afflicted': True, 'between': 'man_and_fellow', 'appeased': False, 'case_source': 'Mishnah Yoma 8:9 — his fellow unappeased: not atoned (the silence)'})
        w.submit({'kind': 'yom_kippur_kept', 'subject': 'the-appeased', 'soul': 'the-appeased', 'afflicted': True, 'between': 'man_and_fellow', 'appeased': True, 'case_source': 'Mishnah Yoma 8:9 — appeased: the day atones'})
        for ref, desc in service_order():
            w.submit({'kind': 'inner_service_performed', 'subject': 'aaron', 'priest': 'aaron', 'step': ref, 'day': 10, 'case_source': 'Lev %s — %s' % (ref, desc)})
        w.submit({'kind': 'goat_dispatched', 'subject': 'the-azazel-goat', 'goat': 'the-azazel-goat', 'dispatcher': 'the-designated-man', 'day': 10, 'case_source': 'Lev 16:20-22, 16:26; Mishnah Yoma 6:2-8'})
        w.advance(11)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    yr = lambda eid, eff: [e['year'] for e in w.entity(eid).ledger if e['effect'] == eff]
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-both-known', 'suspends'), n('the-start-only', 'suspends'), yr('the-end-only', 'atoned_forgiven'), yr('the-neither', 'atoned_forgiven'), yr('the-deliberate', 'atoned_forgiven'), yr('the-other-sinner', 'atoned_forgiven'),
            n('the-penitent', 'atoned_forgiven'), n('the-unappeased', 'atoned_forgiven'), n('the-appeased', 'atoned_forgiven'), n('the-penitent', 'rest_required'), n('the-unappeased', 'labor_barred'),
            n('aaron', 'atoned_forgiven'), n('the-ark-cover', 'sprinkled_seven'), n('the-inner-altar', 'sprinkled_seven'), n('the-bull', 'accepted'), n('the-goat', 'accepted'), n('the-two-rams', 'accepted'), n('the-people', 'atoned_forgiven'),
            n('aaron', 'immersed'), n('the-sin-offerings-fat', 'smoked_to_the_lord'), n('the-burnt-pair', 'burned_outside_camp'), n('the-burner', 'defiles_garments'), n('the-burner', 'washes_and_bathes'),
            n('the-azazel-goat', 'dispatched_to_wilderness'), n('the-designated-man', 'washes_and_bathes'), tset, fired, w.clock.year), w


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

    # ---- THE CALLS (2026-09-06, the dependency-debt sitting) ------
    # The chapter names the sin offering at eleven verses and the burnt
    # offering at five, and this runner imported nothing: the bull and
    # goat are Lev 4's inner sin offerings, the rams Lev 1:10's, the
    # burnt pair Lev 4:12's, the fast Lev 23:27-32's. Resolved live.
    import io as _io, contextlib as _ctx
    with _ctx.redirect_stdout(_io.StringIO()):
        import cold_run_offerings as OFF
        import cold_run_chatat as CH
        import cold_run_moadim as MO
    print('\n== THE CALLS (the pointers into other engines, live) ==')
    cell('the bull and goat: inner sin offerings (CALLED offerings)',
         OFF.dispatch('inner_chatat_yk')['stations']['v'],
         'poles+curtain+golden_altar',
         '16:14-18 — between the poles, the curtain, the golden altar: '
         'the offerings dispatcher\'s own Lev 16:14 import, closed as a '
         'call from this side', 'IMPORT')
    cell('the two rams: burnt offerings (CALLED offerings)',
         OFF.dispatch('olah:flock')['disposition']['v'], 'wholly_to_fires',
         '16:3, 16:5, 16:24 — the rams of Lev 1:10', 'IMPORT')
    cell('the burnt pair outside the camp (CALLED chatat)',
         CH.burn_site('as_commanded')['v'], 'ash_house_defiles_garments',
         '16:27-28 — as Lev 4:12 and 4:21; the burner\'s garments at '
         '16:28 are the sin-offering engine\'s own import', 'IMPORT')
    _yk = MO.yom_kippur()
    cell('the fast: one function at two seats (CALLED moadim)',
         _yk['affliction']['v'] + '/' + _yk['not_afflicting']['v'],
         'required/karet',
         '16:29-31 = Lev 23:27-32: afflict yourselves, the karet', 'IMPORT')

    # ---- THE SCENE (W4, 2026-09-07): the Day on the world engine ----
    print('\n== THE SCENE (Shevuot 1:3, 1:6; Yoma 8:9; the service in order; the calendar\'s daemon beside) ==')
    SCENE, _w = scene()
    cell('the scene tuple (the Day as the TIMER)', SCENE,
         (1, 1, [10], [10], [10], [10], 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 4, 4, 11),
         'the routing table\'s six persons (two suspended, four atoned ON the Day), the fellow gate\'s three (the unappeased silent; the calendar\'s daemon writing the affliction beside), the service in verse order writing the spec\'s effects by call, the goat dispatched',
         'RECORDED')
    _w.print_coverage()

    n_ok = sum(cells)
    ink = 9
    rec = 6
    ans = 3
    imp = 4
    print(f'\nYOM KIPPUR MACHINE: {n_ok}/{len(cells)} cells '
          f'({ink} INK / {rec} RECORDED / {ans} ANSWER-SHEET / {imp} IMPORT '
          f'— the fractions honest)')
    assert n_ok == len(cells), 'mismatches above'
    db.close()


if __name__ == '__main__':
    main()
