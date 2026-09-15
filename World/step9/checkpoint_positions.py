#!/usr/bin/env python3
"""checkpoint_positions.py — THE FALL OF EVERY CHECKPOINT, MEASURED (THE LOOP item 5, 2026-09-14; THE_LOOP.md "THE CHECKPOINTS AS THEY FALL —
item 5's build": D29 THE FALL IS MEASURED, NEVER TYPED).

    python3 World/step9/checkpoint_positions.py            # measure: the base stepped by MARKER, the block asked at every pause, the table written
    python3 World/step9/checkpoint_positions.py --check    # the gate: every checkpoint of the block has a row and no row is stale

THE MEASUREMENT: the stepper walks the whole tape by marker (the marker table's own grain) under its own session name
(cold_run_sequence/positions); before the first line and at every pause cold_run_sequence.checkpoints_partial runs on the stepped world
(D28 — nothing printed, nothing written); a checkpoint FALLS at the first pause from which its verdict and its computed value equal their
final ones and stay so to the end of the tape. The table World/step9/checkpoint_positions.yaml: one row per checkpoint — the pause's verse
(the last verse run before the pause), the ordinal (lines sealed at the pause), the day, the pause index, the final verdict. Regenerated
at every compile sitting whose block gains a checkpoint (THE_STEPS' compile shape), in the background like the sweep.
"""
import os, sys, io, time, contextlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'journal'))); sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '..')))
import yaml
TABLE = os.path.join(HERE, 'checkpoint_positions.yaml')
SOURCE = 'cold_run_sequence/positions'


def load_modules():
    with contextlib.redirect_stdout(io.StringIO()):
        import cold_run_sequence as CS
        import world_stepper as WS
    return CS, WS


def state_of(rows):
    """per prefix: (ok, computed) — what a fall compares"""
    return {r['name'].split(' ')[0]: (r['ok'], r['computed']) for r in rows}


def measure(quiet=False):
    CS, WS = load_modules()
    reg = CS.registry_map()
    t0 = time.time()
    with contextlib.redirect_stdout(io.StringIO()):
        st = WS.Stepper(source=SOURCE)
    pauses = []                                            # (index, verse, ordinal, day, state)

    def ask(verse):
        rows, failed = CS.checkpoints_partial(st.w, st.M, reg)
        pauses.append({'pause': len(pauses), 'verse': verse, 'ordinal': len(st.sink.seg.events), 'day': st.w.clock.day, 'state': state_of(rows), 'names': {r['name'].split(' ')[0]: r['name'] for r in rows}, 'failed': len(failed)})
        if not quiet:
            print('  pause %3d at %-14s ordinal %5d day %9d: %3d computed, %3d not yet, %2d statements raised' % (
                len(pauses) - 1, verse, len(st.sink.seg.events), st.w.clock.day, sum(1 for v in pauses[-1]['state'].values() if v[0] is not None), sum(1 for v in pauses[-1]['state'].values() if v[0] is None), len(failed)))
    ask('(before the first line)')
    while not st.done:
        with contextlib.redirect_stdout(io.StringIO()):
            r = st.step('marker')
        last = r['ran'][-1][0] if r['ran'] else (st.next_verse or 'the end')
        ask(last)
    with contextlib.redirect_stdout(io.StringIO()):
        st.close(quiet=True)
    final = pauses[-1]['state']
    table = {}
    for pre, fin in final.items():
        p = len(pauses) - 1
        while p > 0 and pauses[p - 1]['state'].get(pre, ('?', '?')) == fin:
            p -= 1
        at = pauses[p]
        table[pre] = {'name': pauses[-1]['names'][pre], 'verse': at['verse'], 'ordinal': at['ordinal'], 'day': at['day'], 'pause': p,
                      'final': 'MATCH' if fin[0] else ('DIVERGE' if fin[0] is False else 'NOT YET')}
    out = {'measured': datetime.date.today().isoformat(), 'base': os.path.basename(st.base) if st.base else None, 'pauses': len(pauses),
           'tape_lines': pauses[-1]['ordinal'], 'seconds': round(time.time() - t0, 1), 'checkpoints': table}
    with open(TABLE, 'w', encoding='utf-8') as f:
        f.write('# checkpoint_positions.yaml — THE FALL OF EVERY CHECKPOINT (THE LOOP item 5, D29): written by checkpoint_positions.py, never by hand.\n'
                '# A checkpoint falls at the first pause (the base stepped by marker) from which its verdict and computed value equal their final ones.\n')
        yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, width=200)
    by_pause = {}
    for pre, r in table.items():
        by_pause.setdefault(r['pause'], []).append(pre)
    print('THE FALLS: %d checkpoints over %d pauses in %.0f s; at pause 0 (before any line) %d; the last fall at pause %d (%s); NOT YET at the end %d; the table %s'
          % (len(table), len(pauses), time.time() - t0, len(by_pause.get(0, [])), max(by_pause), table[by_pause[max(by_pause)][0]]['verse'], sum(1 for r in table.values() if r['final'] == 'NOT YET'), TABLE))
    return out


def check():
    CS, WS = load_modules()
    lits = [n.split(' ')[0] for n in CS.checkpoint_names()]
    if not os.path.exists(TABLE):
        print('CHECKPOINT POSITIONS: RED — no table at %s (run without --check)' % TABLE); return False
    t = yaml.safe_load(open(TABLE, encoding='utf-8'))
    have = set(t['checkpoints'])
    missing = [n for n in lits if n not in have]
    stale = sorted(have - set(lits) - {k for k in have if k.startswith('C3d-')})
    ok = not missing and not stale
    print('CHECKPOINT POSITIONS: %s — the block names %d literal checkpoints, the table %d rows (measured %s over %d pauses, %s lines); missing %s; stale %s'
          % ('GREEN' if ok else 'RED', len(lits), len(have), t.get('measured'), t.get('pauses'), t.get('tape_lines'), missing[:6] or 'none', stale[:6] or 'none'))
    return ok


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(0 if check() else 1)
    measure(quiet='--quiet' in sys.argv)
