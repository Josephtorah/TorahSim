#!/usr/bin/env python3
"""cursor_probes.py — THE LOOP's step 4 (THE CURSOR) and step 5 (SCENARIOS) fire-probes (2026-09-09, THE TENT sitting 4;
THE_LOOP.md "Step 4 THE CURSOR — the design" and "Step 5 SCENARIOS — the design"), written BEFORE the engine's stop, the
runner's run_to, the journal's cursor_segment and scenario. Against the unchanged engine every probe must FAIL; after the code
every probe must PASS. The base is the running world's segment ON DISK (World/journal/data/L3_run_cold_run_sequence_seed_isaac.jsonl,
written by the last tape run) — read, never rewritten; every append goes to a temporary directory. Six probes:
  K1 run_to(verse) hands back a live world stopped BEFORE the verse (its position in the text below the cursor; the fork = the
     lines replayed) whose replayed prefix is BYTE-IDENTICAL to the base segment's prefix (the audit: same events, same chains)
  K2 a submission after the cursor lands in an APPENDED segment named by the cursor verse whose chain CONTINUES from the base's
     chain at the fork (the first appended line's chain = sha256(base_chain_at_fork + canon(event))[:16]) and whose header names
     the base and the fork; the segment's chain verifies from that start
  K3 a cursor beyond the tape's last line is the whole tape: the fork equals the base's line count and the world's log is the run's
  K4 determinism: two cursors at the same verse with the same submission produce byte-identical appended segments
  K5 the index admits the appended segment as its own source and the four views' counts equal the table's on it (the views gate)
  K6 the scenario mark: a case event submitted through scenario(world, event, label) is journaled with prov.unit 'scenario' and its
     label in the data; the base's bytes are unchanged before and after
Not run by the sweep; run by hand at the sitting and after any engine edit. Run: python3 World/step9/cursor_probes.py
"""
import os, sys, io, json, hashlib, tempfile, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'journal')))
import world_engine as WE
import world_journal as WJ
from worldledger import canon

results = []
BASE = os.path.join(WJ.data_dir(), 'L3_run_cold_run_sequence_seed_isaac.jsonl')
CURSOR = 'Num 27:1'
SUBMIT = {'kind': 'forewarned_before_the_act', 'subject': 'probe-person', 'person': 'probe-person', 'transgression': 'sabbath',
          'warned': False, 'labor_named': False, 'case_source': 'Num 15:33 — the probe\'s warning row (Mishnah Sanhedrin 5:1)'}


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the old engine lacks the construct: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:240])
        results.append((name, bool(ok), note))
        return fn
    return deco


def base_lines():
    with open(BASE, 'rb') as f:
        return f.read().split(b'\n')


def quiet_run_to(verse):
    import cold_run_sequence as CS
    with contextlib.redirect_stdout(io.StringIO()):
        return CS.run_to(verse)


@probe('K1 run_to stops before the verse; the replayed prefix is byte-identical to the base segment\'s prefix')
def k1():
    w, M, fork = quiet_run_to(CURSOR)
    below = w._verse_reached is not None and w._verse_reached < WE.verse_key(CURSOR)
    with tempfile.TemporaryDirectory() as td:
        path, n, coerced = WJ.sink(w, source='cold_run_sequence/seed_isaac', out_dir=td)
        mine = open(path, 'rb').read().split(b'\n')
    base = base_lines()
    same = mine[1:fork + 1] == base[1:fork + 1] and fork == len(w.log) == n
    return below and same and fork > 0, 'fork %d lines; position %r below %s: %s; prefix identical: %s' % (fork, w._verse_reached, CURSOR, below, same)


@probe('K2 the appended segment continues the base\'s chain at the fork and names the base and the fork')
def k2():
    w, M, fork = quiet_run_to(CURSOR)
    base = base_lines()
    at_fork = json.loads(base[fork])['chain']
    with tempfile.TemporaryDirectory() as td:
        w.submit(dict(SUBMIT))
        path, n = WJ.cursor_segment(w, fork, CURSOR, out_dir=td)
        lines = open(path, 'rb').read().split(b'\n')
        head = json.loads(lines[0]); first = json.loads(lines[1])
        ev = {k: first[k] for k in ('s', 'op', 'layer', 'kind', 'subj', 'data', 'prov')}
        want = hashlib.sha256((at_fork + canon(ev)).encode('utf-8')).hexdigest()[:16]
        ok = (first['chain'] == want and head.get('fork') == fork and head.get('start_chain') == at_fork
              and os.path.basename(BASE) in str(head.get('base')) and 'cursor@' in head.get('source', '') and WJ.verify(path))
    return ok, 'appended %d lines; first chain %s (want %s); header fork %s start %s; verified %s' % (n, first['chain'], want, head.get('fork'), head.get('start_chain'), WJ.verify(path) if os.path.exists(path) else 'gone')


@probe('K3 a cursor beyond the tape\'s last line is the whole tape')
def k3():
    w, M, fork = quiet_run_to('Deut 34:12')
    base = base_lines()
    n_base = len([l for l in base[1:] if l.strip()])
    return fork == n_base == len(w.log), 'fork %d, base events %d, log %d' % (fork, n_base, len(w.log))


@probe('K4 two cursors at the same verse with the same submission produce byte-identical appended segments')
def k4():
    outs = []
    for _ in range(2):
        w, M, fork = quiet_run_to(CURSOR)
        with tempfile.TemporaryDirectory() as td:
            w.submit(dict(SUBMIT))
            path, n = WJ.cursor_segment(w, fork, CURSOR, out_dir=td)
            outs.append(open(path, 'rb').read())
    return outs[0] == outs[1] and len(outs[0]) > 0, 'two appended segments, %d bytes each, %s' % (len(outs[0]), 'IDENTICAL' if outs[0] == outs[1] else 'DIFFER')


@probe('K5 the index admits the appended segment as its own source and the views gate counts it')
def k5():
    w, M, fork = quiet_run_to(CURSOR)
    with tempfile.TemporaryDirectory() as td:
        import shutil
        shutil.copy(BASE, os.path.join(td, os.path.basename(BASE)))
        w.submit(dict(SUBMIT))
        path, n = WJ.cursor_segment(w, fork, CURSOR, out_dir=td)
        db, rows, segs = WJ.reindex(td)
        vc = WJ.view_counts(db)
        src = [s for s in vc if 'cursor@' in s]
        ok, lines = WJ.views_gate(db)
        mine = [l for l in lines if 'cursor@' in l]
    return bool(src) and ok and segs == 2 and all('MATCH' in l for l in mine), 'sources %s; segments %d; views gate %s; %s' % (src, segs, ok, mine[:1])


@probe('K6 a scenario event is journaled with prov.unit scenario and its label; the base is untouched')
def k6():
    before = open(BASE, 'rb').read()
    w, M, fork = quiet_run_to(CURSOR)
    with tempfile.TemporaryDirectory() as td:
        fired = WJ.scenario(w, dict(SUBMIT), 'K6 — the probe\'s labeled hypothetical (Mishnah Sanhedrin 5:1: no warning, exempt)')
        path, n = WJ.cursor_segment(w, fork, CURSOR, out_dir=td)
        lines = open(path, 'rb').read().split(b'\n')
        ev = [json.loads(l) for l in lines[1:] if l.strip() and json.loads(l)['kind'] == 'run.event']
    after = open(BASE, 'rb').read()
    ok = (len(ev) == 1 and ev[0]['prov']['unit'] == 'scenario' and ev[0]['data'].get('scenario', '').startswith('K6') and before == after
          and w.log[-1][0] == 'WRITE' and w.log[-1][2]['effect'] == 'exempt')
    return ok, 'event lines %d; prov.unit %s; label %r; base unchanged %s; the answer %s' % (len(ev), ev[0]['prov']['unit'] if ev else None, (ev[0]['data'].get('scenario') if ev else None), before == after, w.log[-1][2].get('effect') if w.log else None)


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print('THE LOOP — STEP 4 THE CURSOR / STEP 5 SCENARIOS: the fire-probes (base %s)' % BASE)
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
