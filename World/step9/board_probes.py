#!/usr/bin/env python3
"""board_probes.py — THE BOARD fire-probes (2026-09-14; World/step9/THE_LOOP.md "THE BOARD — item 10's build: the design", decisions D22-D26),
written BEFORE the code. Against the tree without world_board.py every probe must FAIL; after the code every probe must PASS. Eight probes:
  B1 THE SHAPING — the board's rows for the base source's first 300 lines equal the mockup's embedded rows field for field, and the forty
     things the mockup called births are placed before the same tape rows
  B2 THE BIRTHS — every entity of the entities view with a first mention is one born row at its verse, placed before the first marker or
     event row at or after that verse (D23); the first three God, the heavens and the earth at Genesis 1:1; light at 1:3 after the four
     things presupposed at 1:2 (the first run found God first and the second found darkness before light — the design had typed the
     mockup's forty; the data's own order stands)
  B3 THE NAMES — every id the base source and the view would show has an English name by D24's rule (the registry's en, the names table,
     or a runner's own dashed id); an underscored token without one is refused
  B4 THE SERVER — the server answers /, /api/status, /api/names and /api/rows over the real database, read-only
  B5 AFTER — /api/rows?after=R returns only rows newer than R, with the births due before them, and equals the tail of the whole
  B6 RESET — a session that started over is reported as a reset and the rows come from the start: fewer rows than the page knows, or
     the same rows written anew with new rowids (the first run on the live board found a new session outrunning the old count between
     two polls, and the page keeping the old lines)
  B7 THE PACE — the stepper runs three steps at --pace 0 with no keyboard and seals (D26)
  B8 THE GATE — world_board.py --gate is green and the page carries no embedded rows
Not run by the sweep; run by hand at the sitting. Run: python3 World/step9/board_probes.py
"""
import os, sys, re, json, time, shutil, sqlite3, tempfile, subprocess, urllib.request, importlib.util, socket
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
DB = os.path.join(HERE, '..', 'journal', 'data', 'world.sqlite')
MOCK = os.path.join(HERE, 'forms_numbers_walk', 'loop_2026-09-14', 'mockup_board.html')
BASE = 'cold_run_sequence/seed_isaac'
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


def board():
    spec = importlib.util.spec_from_file_location('world_board', os.path.join(HERE, 'world_board.py'))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def mock_rows():
    h = open(MOCK, encoding='utf-8').read()
    return json.loads(re.search(r'const ROWS = (\[.*?\]);\n', h).group(1))


def ro():
    return sqlite3.connect('file:%s?mode=ro' % os.path.abspath(DB), uri=True)


KEYS = ('s', 'k', 'd', 'e', 'r', 'w', 'a', 'f', 'p', 'v', 'q', 'due')


def next_tape_s(rows, i):
    for r in rows[i + 1:]:
        if r['k'] != 'born':
            return r['s']
    return None


@probe('B1 the shaping: the base\'s first 300 lines equal the mockup\'s rows field for field; the forty mockup births placed before the same rows')
def b1():
    B = board(); m = mock_rows()
    mt = [r for r in m if r['k'] != 'born']
    forty = {r['e'] for r in m if r['k'] == 'born'}
    out = B.rows_after(ro(), BASE, after=0, known=0)['rows']
    bt = [r for r in out if r['k'] != 'born'][:300]
    same = len(bt) == len(mt) and all({k: a.get(k) for k in KEYS} == {k: b.get(k) for k in KEYS} for a, b in zip(bt, mt))
    diffs = [i for i, (a, b) in enumerate(zip(bt, mt)) if {k: a.get(k) for k in KEYS} != {k: b.get(k) for k in KEYS}][:5]
    mp = [(r['e'], r['r'], next_tape_s(m, i)) for i, r in enumerate(m) if r['k'] == 'born']
    bp = [(r['e'], r['r'], next_tape_s(out, i)) for i, r in enumerate(out) if r['k'] == 'born' and r['e'] in forty]
    return same and mp == bp, 'tape rows equal %s (first differences at %s); the forty births placed alike %s (%d vs %d)' % (same, diffs, mp == bp, len(bp), len(mp))


@probe('B2 the births: every entity of the view one born row at its first mention, placed by the rule; God, the heavens, the earth first at Gen 1:1; light at 1:3 after the four of 1:2')
def b2():
    B = board(); c = ro()
    view = dict(c.execute("select entity, first_ref from entities where first_ref is not null").fetchall())
    out = B.rows_after(c, BASE, after=0, known=0)['rows']
    born = [(i, r) for i, r in enumerate(out) if r['k'] == 'born']
    ids = [r['e'] for _, r in born]
    one_each = sorted(ids) == sorted(view) and len(ids) == len(set(ids))
    placed = True
    for i, r in born:
        nxt = next((x for x in out[i + 1:] if x['k'] in ('marker', 'event')), None)
        prv = next((x for x in reversed(out[:i]) if x['k'] in ('marker', 'event')), None)
        if nxt is None or B.vkey(nxt['r']) < B.vkey(r['r']) or (prv is not None and B.vkey(prv['r']) >= B.vkey(r['r'])):
            placed = False; break
    first8 = [(r['e'], r['r']) for _, r in born[:8]]
    light_ok = first8[:3] == [('god', 'Gen 1:1'), ('shamayim', 'Gen 1:1'), ('the_earth', 'Gen 1:1')] and first8[7] == ('or', 'Gen 1:3') and all(r == 'Gen 1:2' for _, r in first8[3:7])
    return one_each and placed and light_ok, 'one per entity %s (%d of %d); placed by the rule %s; the first eight %s' % (one_each, len(ids), len(view), placed, first8)


@probe('B3 the names: every id of the base and the view named by D24\'s rule; an underscored token without a name refused')
def b3():
    B = board(); c = ro()
    missing = B.unnamed(c, BASE)
    try:
        B.name_of('tohu_va_vohu', B.load_names()); refused = False
    except B.Unnamed:
        refused = True
    return not missing and refused, 'unnamed ids %s; a made-up token refused %s' % (missing[:8], refused)


def free_port():
    s = socket.socket(); s.bind(('127.0.0.1', 0)); p = s.getsockname()[1]; s.close(); return p


def serve(port, db=None, source=BASE):
    args = [sys.executable, os.path.join(HERE, 'world_board.py'), '--port', str(port), '--source', source] + (['--db', db] if db else [])
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for _ in range(40):
        try:
            urllib.request.urlopen('http://127.0.0.1:%d/api/status' % port, timeout=1).read(); return p
        except Exception:
            if p.poll() is not None:
                raise SystemExit('the server died: %s' % p.stdout.read()[-300:])
            time.sleep(0.25)
    p.terminate(); raise SystemExit('the server did not answer in 10 s')


def get(port, path):
    with urllib.request.urlopen('http://127.0.0.1:%d%s' % (port, path), timeout=5) as r:
        body = r.read().decode('utf-8'); ct = r.headers.get('Content-Type', '')
    return body, ct


@probe('B4 the server: /, /api/status, /api/names, /api/rows answered over the real database read-only')
def b4():
    port = free_port(); p = serve(port)
    try:
        page, ct0 = get(port, '/')
        st = json.loads(get(port, '/api/status')[0]); nm = json.loads(get(port, '/api/names')[0]); rw = json.loads(get(port, '/api/rows?source=%s&after=0&known=0' % urllib.request.quote(BASE, safe=''))[0])
    finally:
        p.terminate(); p.wait(timeout=5)
    srcs = {s['source']: s['rows'] for s in st.get('sources', [])}
    ok = ('api/rows' in page and 'text/html' in ct0 and srcs.get(BASE) == 3362 and st.get('default_source') == BASE and st.get('read_only') is True
          and 'the_human' in nm.get('names', {}) and rw.get('count') == 3362 and len(rw.get('rows', [])) > 3362 and rw.get('reset') is False)
    return ok, 'page %d bytes (%s); sources %s; names %d; rows %d of count %s; reset %s' % (len(page), ct0, len(srcs), len(nm.get('names', {})), len(rw.get('rows', [])), rw.get('count'), rw.get('reset'))


@probe('B5 after: rows after a rowid are only the newer ones, with the births due before them, and equal the tail of the whole')
def b5():
    B = board(); c = ro()
    whole = B.rows_after(c, BASE, after=0, known=0)
    tape = [r for r in whole['rows'] if r['k'] != 'born']
    R = tape[99]['id']
    part = B.rows_after(c, BASE, after=R, known=100)
    idx = next(i for i, r in enumerate(whole['rows']) if r['k'] != 'born' and r['id'] == R)
    j = idx + 1
    while j < len(whole['rows']) and whole['rows'][j]['k'] == 'born':      # births anchored to the row after R ride with that row
        j += 1
    # the births right after R belong to the next tape row's block: they must come first in the part
    tail = whole['rows'][idx + 1:]
    only_newer = all(r['id'] > R for r in part['rows'] if r['k'] != 'born')   # a born row rides with its anchor and carries no rowid
    return only_newer and part['rows'] == tail and part['last'] == whole['last'] and part['reset'] is False, 'only newer %s; equals the tail %s (%d vs %d); last %s = %s' % (only_newer, part['rows'] == tail, len(part['rows']), len(tail), part['last'], whole['last'])


@probe('B6 reset: a session that started over is reported as a reset and the rows come from the start')
def b6():
    B = board()
    with tempfile.TemporaryDirectory() as d:
        db = os.path.join(d, 'world.sqlite'); shutil.copy(DB, db)
        c = sqlite3.connect(db)
        whole = B.rows_after(c, BASE, after=0, known=0)
        cut = c.execute("select rowid from events where source=? order by rowid limit 1 offset 1000", (BASE,)).fetchone()[0]
        c.execute("delete from events where source=? and rowid >= ?", (BASE, cut)); c.commit()
        again = B.rows_after(c, BASE, after=whole['last'], known=whole['count'], first=whole['first'])
        # the same rows written anew, and more of them: the count rule is blind, the first-rowid rule sees it
        c.execute("CREATE TEMP TABLE keep AS SELECT seq, op, layer, kind, subj, data, unit, ref, chain, source FROM events WHERE source=? ORDER BY rowid", (BASE,))
        c.execute("DELETE FROM events WHERE source=?", (BASE,))
        c.execute("INSERT INTO events SELECT * FROM keep"); c.execute("INSERT INTO events SELECT * FROM keep LIMIT 5"); c.commit()
        anew = B.rows_after(c, BASE, after=again['last'], known=again['count'], first=again['first'])
        c.close()
    ok = again['reset'] is True and again['count'] == 1000 and again['rows'] and again['rows'][0] == whole['rows'][0] and len([r for r in again['rows'] if r['k'] != 'born']) == 1000
    ok2 = anew['reset'] is True and anew['count'] == 1005 and anew['rows'][0] == whole['rows'][0]
    return ok and ok2, 'fewer rows: reset %s, count %s, from the start %s; written anew with more: reset %s, count %s, from the start %s' % (again['reset'], again['count'], again['rows'][:1] == whole['rows'][:1], anew['reset'], anew['count'], anew['rows'][:1] == whole['rows'][:1])


@probe('B7 the pace: the stepper runs three steps at --pace 0 with no keyboard and seals')
def b7():
    r = subprocess.run([sys.executable, os.path.join(HERE, 'world_stepper.py'), '--by', 'verse', '--steps', '3', '--pace', '0', '--quiet'],
                       stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=600)
    out = r.stdout
    ok = r.returncode == 0 and 'THE PACE' in out and 'SESSION SEALED' in out and 'no keyboard behind this run' not in out
    return ok, 'exit %d; THE PACE line %s; sealed %s; %s' % (r.returncode, 'THE PACE' in out, 'SESSION SEALED' in out, (out.strip().split('\n')[-1] if out.strip() else r.stderr[-200:])[:160])


@probe('B8 the gate: world_board.py --gate green; the page carries no embedded rows')
def b8():
    r = subprocess.run([sys.executable, os.path.join(HERE, 'world_board.py'), '--gate'], capture_output=True, text=True, timeout=600)
    page = open(os.path.join(HERE, 'world_board.html'), encoding='utf-8').read()
    return r.returncode == 0 and 'const ROWS = [' not in page and 'GREEN' in r.stdout, 'exit %d; %s' % (r.returncode, (r.stdout.strip().split('\n')[-1] if r.stdout.strip() else r.stderr[-200:])[:200])


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print('THE BOARD: the fire-probes')
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
