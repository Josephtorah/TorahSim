#!/usr/bin/env python3
"""checkpoint_probes.py — THE CHECKPOINTS AS THEY FALL fire-probes (2026-09-14; World/step9/THE_LOOP.md "THE CHECKPOINTS AS THEY FALL —
item 5's build: the design", decisions D27-D30), written BEFORE the code. Against the unchanged tree every probe must FAIL; after the code
every probe must PASS. The whole base world and one partial world are built once (in memory, the cursor's way) and shared. Seven probes:
  K1 THE FUNCTION — cold_run_sequence.checkpoints(w, M, reg) exists; on the whole base world its verdict list equals VERDICTS (the tape's own
     pinned expectation) and every row carries (name, declared, computed, ok); as built it returns (rows, exported) — the names run() reads
     after the block ride back with the rows (the probes' first run against the code read the pair as the rows: three of my own misses)
  K2 THE EXECUTOR ON A WHOLE WORLD — checkpoints_partial gives the same verdicts as K1 on the whole world (faithful when nothing is missing)
  K3 THE EXECUTOR ON A PARTIAL WORLD — at the left edge of Genesis 7:11 (the flood's marker not yet run) it never raises; the flood's C1 is
     NOT YET and Genesis 5's C0 (pure ink) is computed (the design's first draft said 8:5 — there the ark-rested marker HAS run and C1 is
     computed, a DIVERGE as the tape's own gap says; the first run of the executor taught it)
  K4 THE TABLE — checkpoint_positions.yaml has one row per checkpoint of the block (K1's names) and no other; every row a verse, an
     ordinal within the base, a pause index, a final verdict
  K5 THE POSITIONS OFF THE BASE — C1 falls no earlier than the ark-rested marker's line (Gen 8:4) in the base segment; CR1 no earlier than
     the refuge chapter's first event line (Num 35); C0 at the first pause
  K6 THE STEPPER SHOWS THEM — a session stepped to the left edge of Genesis 8:5 shows exactly the table's checkpoints at or before that
     ordinal, each with a live verdict; C1 among them, MATCH or DIVERGE as the table's final says, never NOT YET
  K7 ASKING WRITES NOTHING — a call of checkpoints() leaves the world's log and the sink's lines unchanged
Not run by the sweep; run by hand at the sitting. Run: python3 World/step9/checkpoint_probes.py
"""
import os, sys, io, json, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'journal'))); sys.path.insert(0, ROOT)
import yaml
TABLE = os.path.join(HERE, 'checkpoint_positions.yaml')
BASE = os.path.join(HERE, '..', 'journal', 'data', 'L3_run_cold_run_sequence_seed_isaac.jsonl')
results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the construct is missing: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:240])
        results.append((name, bool(ok), note))
        return fn
    return deco


with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_stepper as WS
_W = {}


def beyond_the_tape():
    """THE DEUTERONOMY WALK 2b (2026-09-16): the first verse of the chapter AFTER the tape's last line, read from the sequence file's own tape section
    and checked against the Tanakh DB (a verse beyond the tape runs the whole tape); at a book's last chapter the next book's 1:1 in the tape's order;
    past the fifth book the last verse itself (then run_to needs a whole-tape form — filed)."""
    import re as _re, sqlite3 as _sq
    src = open(os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
    tape = src[src.find('# ==== TAPE BEGIN'):src.find('# ==== TAPE END ====')]
    refs = _re.findall(r"'case_source': '(Gen|Exod|Lev|Num|Deut) (\d+):(\d+)", tape)
    order = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']
    last = max(refs, key=lambda r: (order.index(r[0]), int(r[1]), int(r[2])))
    db = _sq.connect('file:' + os.path.join(ROOT, 'Data', 'tanakh.sqlite') + '?mode=ro', uri=True)
    def exists(b, c, v): return bool(db.execute('SELECT 1 FROM verses WHERE book=? AND chapter=? AND verse=?', (b, c, v)).fetchone())
    b, c = last[0], int(last[1])
    if exists(b, c + 1, 1): return '%s %d:1' % (b, c + 1)
    if order.index(b) + 1 < len(order): return '%s 1:1' % order[order.index(b) + 1]
    return '%s %s:%s' % last


def whole():
    if 'w' not in _W:
        with contextlib.redirect_stdout(io.StringIO()):
            w, M, n = CS.run_to(beyond_the_tape())          # THE DEUTERONOMY WALK 2b (2026-09-16): the verse COMPUTED from the tape — the first verse of the chapter after the tape's last line (lesson xiii's second half; 'Deut 4:1' became a position on the tape when chapter 4 joined it); beyond the tape's last line: the whole tape, in memory — THE DEUTERONOMY WALK 1b (2026-09-16): the tape ends at Deut 3:23-26 now, so 'Deut 1:1' became a position ON the tape (the speech's marker) and the 'whole' world stopped at its left edge (KeyError on the speech's marker keys, 3/7); the verse moved past the tape's last line — a probe's 'beyond the tape' verse moves when the tape grows
        _W['w'], _W['M'] = w, M
    return _W['w'], _W['M']


def partial():
    if 'pw' not in _W:
        with contextlib.redirect_stdout(io.StringIO()):
            w, M, n = CS.run_to('Gen 7:11')
        _W['pw'], _W['pM'], _W['pn'] = w, M, n
    return _W['pw'], _W['pM'], _W['pn']


def verdicts_of(rows):
    return ['%s %s' % (r['name'].split(' ')[0], 'MATCH' if r['ok'] else 'DIVERGE') for r in rows]


def base_lines():
    lines = open(BASE, encoding='utf-8').read().split('\n')[1:]
    return [json.loads(l) for l in lines if l.strip()]


@probe('K1 the function: checkpoints(w, M, reg) on the whole base world gives the tape\'s pinned verdicts; rows carry name, declared, computed, ok')
def k1():
    w, M = whole()
    with contextlib.redirect_stdout(io.StringIO()):
        rows, _cx = CS.checkpoints(w, M, CS.registry_map())
    shape = all({'name', 'declared', 'computed', 'ok'} <= set(r) for r in rows)
    v = verdicts_of(rows)
    return shape and v == CS.VERDICTS, 'rows %d; shape %s; verdicts equal the pinned list %s (first difference %s)' % (len(rows), shape, v == CS.VERDICTS, next((i for i, (a, b) in enumerate(zip(v, CS.VERDICTS)) if a != b), None))


@probe('K2 the executor on a whole world: checkpoints_partial gives the same verdicts as the function')
def k2():
    w, M = whole()
    with contextlib.redirect_stdout(io.StringIO()):
        rows, _cx = CS.checkpoints(w, M, CS.registry_map()); prows, failed = CS.checkpoints_partial(w, M, CS.registry_map())
    same = verdicts_of(rows) == verdicts_of(prows) and not failed
    return same, 'verdicts equal %s; statements that raised %d' % (verdicts_of(rows) == verdicts_of(prows), len(failed))


@probe('K3 the executor on a partial world (the left edge of Genesis 7:11): never raises; C1 NOT YET; C0 computed')
def k3():
    w, M, n = partial()
    with contextlib.redirect_stdout(io.StringIO()):
        rows, failed = CS.checkpoints_partial(w, M, CS.registry_map())
    by = {r['name'].split(' ')[0]: r for r in rows}
    c1 = by.get('C1'); c0 = by.get('C0')
    ok = c1 is not None and c1['ok'] is None and c0 is not None and c0['ok'] is True
    return ok, 'rows %d; statements that raised %d; C1 %s; C0 %s' % (len(rows), len(failed), (c1 or {}).get('ok', 'absent'), (c0 or {}).get('ok', 'absent'))


@probe('K4 the table: one row per checkpoint of the block, no other; a verse, an ordinal within the base, a pause index, a final verdict')
def k4():
    w, M = whole()
    with contextlib.redirect_stdout(io.StringIO()):
        names = [r['name'].split(' ')[0] for r in CS.checkpoints(w, M, CS.registry_map())[0]]
    t = yaml.safe_load(open(TABLE, encoding='utf-8'))['checkpoints']
    nb = len(base_lines())
    good = all(isinstance(r.get('verse'), str) and 0 <= r.get('ordinal', -1) <= nb and isinstance(r.get('pause'), int) and r.get('final') in ('MATCH', 'DIVERGE') for r in t.values())
    return sorted(t) == sorted(set(names)) and good and len(names) == len(set(names)), 'rows %d vs checkpoints %d (distinct %d); rows well-formed %s; missing %s; extra %s' % (
        len(t), len(names), len(set(names)), good, sorted(set(names) - set(t))[:5], sorted(set(t) - set(names))[:5])


@probe('K5 the positions off the base: C1 no earlier than Gen 8:4\'s marker line; CR1 no earlier than Num 35\'s first event line; C0 at the first pause')
def k5():
    t = yaml.safe_load(open(TABLE, encoding='utf-8'))['checkpoints']
    L = base_lines()
    ark = next(i + 1 for i, e in enumerate(L) if e['kind'] == 'run.marker' and str(e['prov'].get('ref', '')).startswith('Gen 8:4'))
    ref = next(i + 1 for i, e in enumerate(L) if e['kind'] == 'run.event' and str(e['prov'].get('ref', '')).startswith('Num 35:'))
    ok = t['C1']['ordinal'] >= ark and t['CR1']['ordinal'] >= ref and t['C0']['pause'] == 0
    return ok, 'C1 at %s (the ark-rested marker line %d); CR1 at %s (Num 35\'s first event line %d); C0 pause %s' % (t['C1']['ordinal'], ark, t['CR1']['ordinal'], ref, t['C0']['pause'])


@probe('K6 the stepper shows them: stepped to the left edge of Genesis 8:5, exactly the table\'s checkpoints at or before that ordinal, live verdicts, C1 not NOT YET')
def k6():
    t = yaml.safe_load(open(TABLE, encoding='utf-8'))['checkpoints']
    with contextlib.redirect_stdout(io.StringIO()):
        st = WS.Stepper(from_verse='Gen 8:5')
        rows = st.show('checkpoints')
        st.close(quiet=True)
    n = st.report['sealed_total'] if isinstance(st.report, dict) else None
    want = sorted(k for k, r in t.items() if r['ordinal'] <= n)
    got = sorted(r['name'] for r in rows)
    c1 = next((r for r in rows if r['name'] == 'C1'), None)
    ok = got == want and all(r['verdict'] in ('MATCH', 'DIVERGE', 'NOT YET') for r in rows) and c1 is not None and c1['verdict'] != 'NOT YET'
    return ok, 'ordinal %s; shown %d, the table says %d; equal %s; C1 %s' % (n, len(got), len(want), got == want, (c1 or {}).get('verdict', 'absent'))


@probe('K7 asking writes nothing: the world\'s log and the sink\'s lines unchanged by a call')
def k7():
    w, M = whole()
    n0, s0 = len(w.log), len(w.journal.seg.events) if getattr(w, 'journal', None) else None
    with contextlib.redirect_stdout(io.StringIO()):
        CS.checkpoints(w, M, CS.registry_map())
    n1, s1 = len(w.log), len(w.journal.seg.events) if getattr(w, 'journal', None) else None
    return n0 == n1 and s0 == s1, 'log %d -> %d; sink lines %s -> %s' % (n0, n1, s0, s1)


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print('THE CHECKPOINTS AS THEY FALL: the fire-probes')
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
