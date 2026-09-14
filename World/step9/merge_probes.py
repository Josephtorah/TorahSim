#!/usr/bin/env python3
"""merge_probes.py — D7'S MERGE fire-probes (2026-09-14; THE_LOOP.md "D7'S MERGE — ONE DATABASE: the design", decisions D19-D21), written
BEFORE the code. Against the unchanged tree every probe must FAIL; after the code every probe must PASS. One build into a temporary folder
is shared by the probes (the fold's 29 s paid once at import). Eight probes:
  M1 THE FOLD LAYER — the build writes L0 and L1_fold.jsonl; the rows per kind equal the fold's list lengths plus one fold.ref per verse and
     one fold.meta; the header carries the counts and the hash; every row's data equals its fold item
  M2 DETERMINISM — a second build in a second process is byte-identical on both segments
  M3 THE VIEWS — over an index of the two segments the fourteen views exist and the reconcile passes: nine counts and the hash
  M4 THE GATE — the header's hash and counts equal CORPUS_TRUTH's pinned tripwires; a header with another hash is refused
  M5 THE ASK TOOL — ask.py's at, open, who, entities, called run over the index and answer
  M6 THE RUNS UNTOUCHED — an index over the fold's segments and one L3 segment holds every L3 row and the five run views MATCH
  M7 THE AUGUST TREE RETIRED — the build removes L1_structure.jsonl and world_tree.json; the register marks the August kinds retired
  M8 THE BIRTHS — the entities view gives the heavens and the earth Gen.1.1 and light Gen.1.3 as their first mention
Not run by the sweep; run by hand at the sitting. Run: python3 World/step9/merge_probes.py
"""
import os, sys, io, json, glob, shutil, sqlite3, tempfile, subprocess, contextlib, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
JOURNAL = os.path.normpath(os.path.join(HERE, '..', 'journal'))
WORLD = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE); sys.path.insert(0, JOURNAL); sys.path.insert(0, ROOT)
import yaml
import corpus_world as cw
from worldledger import canon

results = []
TD = tempfile.mkdtemp(prefix='merge_probes_')
W = cw.fold(write=False)                    # once, for every probe
FOLD_LISTS = ('units', 'facts', 'events', 'demands', 'mentions', 'names', 'standing', 'tests', 'checkpoints', 'ledger')


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the construct is missing: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:240])
        results.append((name, bool(ok), note))
        return fn
    return deco


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


_built = {}


def built():
    """the shared build into TD: (BW module, paths, counts, hash)"""
    if not _built:
        BW = load(os.path.join(JOURNAL, 'build_world.py'), 'journal_build_world')
        open(os.path.join(TD, 'L1_structure.jsonl'), 'w').write('{"segment":"L1"}\n')     # the August tree's files, to be removed by the build (M7)
        open(os.path.join(TD, 'world_tree.json'), 'w').write('{}')
        paths, counts, h = BW.build(out_dir=TD, W=W)
        _built.update(BW=BW, paths=paths, counts=counts, hash=h)
    return _built


def fold_rows(path):
    out = {}
    with open(path, encoding='utf-8') as f:
        head = json.loads(f.readline())
        for line in f:
            ev = json.loads(line); out.setdefault(ev['kind'], []).append(ev)
    return head, out


@probe('M1 the fold layer: L0 and L1_fold.jsonl written; the rows per kind equal the fold; the header carries the counts and the hash; every row equals its item')
def m1():
    b = built()
    l1 = os.path.join(TD, 'L1_fold.jsonl'); l0 = os.path.join(TD, 'L0_scripture.jsonl')
    head, rows = fold_rows(l1)
    counts = {k: len(rows.get(b['BW'].KIND[k], [])) for k in FOLD_LISTS}          # the builder's own kind map (a hand-derived key had misspelled 'standing')
    want = {k: len(W[k]) for k in FOLD_LISTS}
    same = all(canon(ev['data']) == canon(item) for k in FOLD_LISTS for ev, item in zip(rows.get(b['BW'].KIND[k], []), W[k]))
    refs = len({r['ref'] for k in ('facts', 'events', 'demands', 'mentions', 'names', 'standing', 'tests', 'ledger') for r in W[k]})
    ok = (os.path.exists(l0) and counts == want and same and len(rows.get('fold.ref', [])) == refs and len(rows.get('fold.meta', [])) == 1
          and head.get('state_hash') == cw._state_hash(W) == b['hash'] and head.get('units') == 210 and head.get('facts') == 1809)
    return ok, 'counts %s; want %s; rows equal their items %s; refs %d; header hash %s units %s' % (counts, want, same, len(rows.get('fold.ref', [])), head.get('state_hash'), head.get('units'))


@probe('M2 determinism: a second build in a second process is byte-identical on both segments')
def m2():
    built()
    with tempfile.TemporaryDirectory() as d:
        r = subprocess.run([sys.executable, os.path.join(JOURNAL, 'build_world.py')], env=dict(os.environ, WORLD_OUT_DIR=d), capture_output=True, text=True)
        if r.returncode != 0:
            return False, 'the second build failed: %s' % (r.stdout[-200:] + r.stderr[-300:])
        same = all(open(os.path.join(TD, s), 'rb').read() == open(os.path.join(d, s), 'rb').read() for s in ('L0_scripture.jsonl', 'L1_fold.jsonl'))
    return same, 'both segments %s across two processes' % ('IDENTICAL' if same else 'DIFFER')


def index_td(with_l3=False):
    import world_journal as WJ
    built()
    if with_l3:
        shutil.copy(os.path.join(WJ.data_dir(), WJ.BASE_SEGMENT), os.path.join(TD, WJ.BASE_SEGMENT))
    db, n, k = WJ.reindex(TD)
    return WJ, db, n, k


@probe('M3 the views: the fourteen views exist over the index and the reconcile passes on nine counts and the hash')
def m3():
    WJ, db, n, k = index_td()
    c = sqlite3.connect(db)
    views = {r[0] for r in c.execute("select name from sqlite_master where type='view'")}
    c.close()
    want = {'refs', 'units', 'facts', 'fold_events', 'event_themes', 'demands', 'mentions', 'names', 'standing', 'tests', 'checkpoints', 'entities', 'relations', 'entity_state', 'meta'}   # the fold's events are the view fold_events (D20's one exception: `events` is the journal's table)
    BE = load(os.path.join(WORLD, 'build_world.py'), 'world_build_world')
    with contextlib.redirect_stdout(io.StringIO()) as out:
        ok = BE.reconcile_index(db, W)
    return ok and want <= views, 'views present %s; missing %s; reconcile %s' % (len(want & views), sorted(want - views), ok)


@probe('M4 the gate: the header against CORPUS_TRUTH\'s pinned hash and counts; a header with another hash refused')
def m4():
    WJ, db, n, k = index_td()
    ok1, lines1 = WJ.fold_gate(db, TD)
    p = os.path.join(TD, 'L1_fold.jsonl')
    lines = open(p, encoding='utf-8').read().split('\n')
    head = json.loads(lines[0]); good = dict(head); head['state_hash'] = '0000000000000000'
    open(p, 'w', encoding='utf-8').write('\n'.join([canon(head)] + lines[1:]))
    try:
        ok2, lines2 = WJ.fold_gate(db, TD)
    finally:
        open(p, 'w', encoding='utf-8').write('\n'.join([canon(good)] + lines[1:]))
    return ok1 and not ok2, 'good header %s; tampered header %s — %s' % (ok1, ok2, (lines2[-1] if lines2 else '')[:120])


@probe('M5 the ask tool: at, open, who, entities, called run over the index and answer')
def m5():
    WJ, db, n, k = index_td()
    ASK = load(os.path.join(WORLD, 'ask.py'), 'world_ask')
    from pathlib import Path
    ASK.DB = Path(db)
    outs = {}
    for cmd, args in (('at', ['Gen.30.24']), ('open', ['Gen.30.24']), ('who', ['Gen.32.4-Gen.33.17']), ('entities', []), ('called', ['jacob'])):   # the who-span carries the book on both sides: the tool splits on the dash (its own docstring's example lacks it)
        with contextlib.redirect_stdout(io.StringIO()) as out:
            ASK.CMDS[cmd](ASK.con(), args)
        outs[cmd] = len(out.getvalue().strip().split('\n'))
    return all(v >= 3 for v in outs.values()), 'lines answered per question %s' % outs


@probe('M6 the runs untouched: an index over the fold\'s segments and one L3 segment holds every L3 row and the five run views MATCH')
def m6():
    WJ, db, n, k = index_td(with_l3=True)
    seg = os.path.join(TD, WJ.BASE_SEGMENT)
    lines = sum(1 for l in open(seg, encoding='utf-8') if l.strip()) - 1
    c = sqlite3.connect(db); l3 = c.execute("select count(*) from events where layer='L3'").fetchone()[0]; c.close()
    ok, vl = WJ.views_gate(db)
    return l3 == lines and ok, 'L3 rows %d = segment lines %d; the run views %s' % (l3, lines, 'MATCH' if ok else 'DIVERGE')


@probe('M7 the August tree retired: the build removed L1_structure.jsonl and world_tree.json; the register marks the August kinds retired')
def m7():
    built()
    gone = not os.path.exists(os.path.join(TD, 'L1_structure.jsonl')) and not os.path.exists(os.path.join(TD, 'world_tree.json'))
    reg = yaml.safe_load(open(os.path.join(JOURNAL, 'registers', 'event_kinds.yaml'), encoding='utf-8'))
    august = [k for k in reg['kinds'] if k.get('layer') == 'L1' and not k['id'].startswith('fold.')]
    retired = [k for k in august if k.get('retired')]
    fold_kinds = [k['id'] for k in reg['kinds'] if k['id'].startswith('fold.')]
    return gone and august and len(retired) == len(august) and len(fold_kinds) >= 12, 'files gone %s; August kinds %d retired %d; fold kinds %d' % (gone, len(august), len(retired), len(fold_kinds))


@probe('M8 the births: the entities view gives the heavens and the earth Gen.1.1 and light Gen.1.3')
def m8():
    WJ, db, n, k = index_td()
    c = sqlite3.connect(db)
    rows = dict(c.execute("select entity, first_ref from entities where entity in ('shamayim', 'the_earth', 'or')").fetchall())   # the registry maps the token aretz to the_earth; the heavens keep their token as their id
    c.close()
    return rows.get('shamayim') == 'Gen.1.1' and rows.get('the_earth') == 'Gen.1.1' and rows.get('or') == 'Gen.1.3', '%s' % rows


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print("D7'S MERGE — ONE DATABASE: the fire-probes (the shared build in %s)" % TD)
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    shutil.rmtree(TD, ignore_errors=True)
    sys.exit(0 if ok == len(results) else 1)
