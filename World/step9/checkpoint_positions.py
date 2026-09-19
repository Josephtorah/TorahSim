#!/usr/bin/env python3
"""checkpoint_positions.py — THE FALL OF EVERY CHECKPOINT, MEASURED (THE LOOP item 5, 2026-09-14; THE_LOOP.md "THE CHECKPOINTS AS THEY FALL —
item 5's build": D29 THE FALL IS MEASURED, NEVER TYPED).

    python3 World/step9/checkpoint_positions.py            # measure: the base stepped by MARKER, the block asked at every pause, the table written
    python3 World/step9/checkpoint_positions.py --jobs 8   # THE GATES CUT (2026-09-19; D36): the same measure by N workers — each steps the WHOLE tape
                                                           # in its own journal folder (the live base copied in, so the replay is still the audit) and asks
                                                           # the block at ITS pauses (pause i to worker i mod N); the parent merges the pauses and takes the falls
    python3 World/step9/checkpoint_positions.py --check    # the gate: every checkpoint of the block has a row and no row is stale

THE MEASUREMENT: the stepper walks the whole tape by marker (the marker table's own grain) under its own session name
(cold_run_sequence/positions); before the first line and at every pause cold_run_sequence.checkpoints_partial runs on the stepped world
(D28 — nothing printed, nothing written); a checkpoint FALLS at the first pause from which its verdict and its computed value equal their
final ones and stay so to the end of the tape. The table World/step9/checkpoint_positions.yaml: one row per checkpoint — the pause's verse
(the last verse run before the pause), the ordinal (lines sealed at the pause), the day, the pause index, the final verdict. Regenerated
at every compile sitting whose block gains a checkpoint (THE_STEPS' compile shape), in the background like the sweep. THE COST (measured
2026-09-19): the import of the runners ~140 s once per process, the replay ~2 s, the block ~8 s at each of 169 pauses — so N workers cut the
block's 1,400 s by N and pay the import N times over in parallel; the table is always the WHOLE measure, never a partial one (an incremental
form by regions was built and struck the same day: a region's checkpoints read helpers bound across most of the block, so a partial run was
nearly the whole run — GATES_CHAIN.md).
"""
import re, os, sys, io, time, contextlib, datetime, pickle, shutil, subprocess, tempfile
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


def argv_value(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv and sys.argv.index(flag) + 1 < len(sys.argv) else default


def walk(quiet=False, out_dir=None, pick=None):
    """the whole tape by marker; the block asked at the pauses `pick` admits (all when None); returns (pauses, base) — a pause not asked carries state None"""
    CS, WS = load_modules()
    reg = CS.registry_map()
    with contextlib.redirect_stdout(io.StringIO()):
        st = WS.Stepper(source=SOURCE, out_dir=out_dir)
    pauses = []                                            # (index, verse, ordinal, day, state)

    def ask(verse):
        i = len(pauses)
        if pick is None or pick(i):
            rows, failed = CS.checkpoints_partial(st.w, st.M, reg)
            pauses.append({'pause': i, 'verse': verse, 'ordinal': len(st.sink.seg.events), 'day': st.w.clock.day, 'state': state_of(rows), 'names': {r['name'].split(' ')[0]: r['name'] for r in rows}, 'failed': len(failed)})
            if not quiet:
                print('  pause %3d at %-14s ordinal %5d day %9d: %3d computed, %3d not yet, %2d statements raised' % (
                    i, verse, len(st.sink.seg.events), st.w.clock.day, sum(1 for v in pauses[-1]['state'].values() if v[0] is not None), sum(1 for v in pauses[-1]['state'].values() if v[0] is None), len(failed)))
        else:
            pauses.append({'pause': i, 'verse': verse, 'ordinal': len(st.sink.seg.events), 'day': st.w.clock.day, 'state': None, 'names': None, 'failed': None})
    ask('(before the first line)')
    while not st.done:
        with contextlib.redirect_stdout(io.StringIO()):
            r = st.step('marker')
        last = r['ran'][-1][0] if r['ran'] else (st.next_verse or 'the end')
        ask(last)
    with contextlib.redirect_stdout(io.StringIO()):
        st.close(quiet=True)
    return pauses, (os.path.basename(st.base) if st.base else None)


def falls(pauses, base, t0, jobs=1):
    """the table from the pauses' states (every pause asked): a checkpoint falls at the first pause from which its state equals its final one"""
    final = pauses[-1]['state']
    table = {}
    for pre, fin in final.items():
        p = len(pauses) - 1
        while p > 0 and pauses[p - 1]['state'].get(pre, ('?', '?')) == fin:
            p -= 1
        at = pauses[p]
        table[pre] = {'name': pauses[-1]['names'][pre], 'verse': at['verse'], 'ordinal': at['ordinal'], 'day': at['day'], 'pause': p,
                      'final': 'MATCH' if fin[0] else ('DIVERGE' if fin[0] is False else 'NOT YET')}
    out = {'measured': datetime.date.today().isoformat(), 'base': base, 'pauses': len(pauses),
           'tape_lines': pauses[-1]['ordinal'], 'seconds': round(time.time() - t0, 1), 'jobs': jobs, 'checkpoints': table}
    with open(TABLE, 'w', encoding='utf-8') as f:
        f.write('# checkpoint_positions.yaml — THE FALL OF EVERY CHECKPOINT (THE LOOP item 5, D29): written by checkpoint_positions.py, never by hand.\n'
                '# A checkpoint falls at the first pause (the base stepped by marker) from which its verdict and computed value equal their final ones.\n')
        yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, width=200)
    by_pause = {}
    for row in table.values(): by_pause[row['pause']] = by_pause.get(row['pause'], 0) + 1
    print('THE FALLS: %d checkpoints over %d pauses in %.0f s (%d worker%s); at pause 0 (before any line) %d; the last fall at pause %d (%s); NOT YET at the end %d; the table %s'
          % (len(table), len(pauses), time.time() - t0, jobs, '' if jobs == 1 else 's', by_pause.get(0, 0), max(by_pause), pauses[max(by_pause)]['verse'], sum(1 for r in table.values() if r['final'] == 'NOT YET'), TABLE))
    return out


def measure(quiet=False, jobs=1):
    t0 = time.time()
    if jobs <= 1:
        pauses, base = walk(quiet)
        return falls(pauses, base, t0)
    # THE GATES CUT (2026-09-19; D36): N workers, each the whole tape in its own journal folder (the live base copied in — the replay stays the audit),
    # each asking at pause i where i mod N is its number; the parent merges the pauses (every pause asked by exactly one worker) and takes the falls
    import world_journal as WJ
    live = os.path.join(WJ.data_dir(None), WJ.BASE_SEGMENT)
    tmp = tempfile.mkdtemp(prefix='positions_')
    procs = []
    for k in range(jobs):
        d = os.path.join(tmp, 'w%d' % k); os.makedirs(d)
        if os.path.exists(live): shutil.copy(live, os.path.join(d, WJ.BASE_SEGMENT))
        out = os.path.join(tmp, 'w%d.pickle' % k)
        procs.append((k, out, subprocess.Popen([sys.executable, os.path.abspath(__file__), '--worker', str(k), str(jobs), '--out-dir', d, '--out', out, '--quiet'],
                                                stdout=open(os.path.join(tmp, 'w%d.out' % k), 'w'), stderr=subprocess.STDOUT)))
    print('THE POSITIONS BY %d WORKERS (each the whole tape in its own folder %s; pause i asked by worker i mod %d)' % (jobs, tmp, jobs))
    merged, base = None, None
    for k, out, p in procs:
        rc = p.wait()
        if rc != 0 or not os.path.exists(out):
            print('worker %d FAILED (rc %s): %s' % (k, rc, open(os.path.join(tmp, 'w%d.out' % k)).read()[-600:])); sys.exit(1)
        pauses, b = pickle.load(open(out, 'rb'))
        if merged is None: merged, base = [dict(p_) for p_ in pauses], b
        else:
            assert len(pauses) == len(merged), 'worker %d walked %d pauses, worker 0 %d' % (k, len(pauses), len(merged))
            for i, (a, b_) in enumerate(zip(merged, pauses)):
                assert (a['verse'], a['ordinal'], a['day']) == (b_['verse'], b_['ordinal'], b_['day']), 'the workers disagree at pause %d: %s vs %s' % (i, (a['verse'], a['ordinal'], a['day']), (b_['verse'], b_['ordinal'], b_['day']))
                if b_['state'] is not None: a['state'], a['names'], a['failed'] = b_['state'], b_['names'], b_['failed']
    missing = [i for i, p_ in enumerate(merged) if p_['state'] is None]
    assert not missing, 'pauses no worker asked: %s' % missing[:8]
    shutil.rmtree(tmp, ignore_errors=True)
    return falls(merged, base, t0, jobs)


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
    if '--worker' in sys.argv:
        k, n = int(argv_value('--worker')), int(sys.argv[sys.argv.index('--worker') + 2])
        pauses, base = walk(quiet=True, out_dir=argv_value('--out-dir'), pick=lambda i: i % n == k)
        pickle.dump((pauses, base), open(argv_value('--out'), 'wb')); sys.exit(0)
    measure(quiet='--quiet' in sys.argv, jobs=int(argv_value('--jobs', '1')))
