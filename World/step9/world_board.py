#!/usr/bin/env python3
"""world_board.py — THE BOARD (THE LOOP, item 10's build, 2026-09-14; World/step9/THE_LOOP.md "THE BOARD — item 10's build: the design",
decisions D22-D26). A reader over the one database: a small local server that serves the board page and three routes, and never writes.

    python3 World/step9/world_board.py [--source cold_run_sequence/stepper] [--port 8765] [--db World/journal/data/world.sqlite]
    python3 World/step9/world_board.py --gate [--source S]

    GET /                 the page (world_board.html beside this file)
    GET /api/status       the sources in the database with their row counts; the default source; read_only true
    GET /api/names        every id's English name and group: the registry's `en` first, then board_names.yaml, then a runner's own dashed id
    GET /api/rows?source=S&after=R&known=N&first=F
                          the source's rows after rowid R, shaped as the mockup shaped them (one home for the shape: shape() below), the
                          births due before each row merged in (D23: a thing appears at its first mention, placed before the first marker
                          or event row at or after its verse — and only when the text reaches it; a session that stops short never shows
                          what it did not reach); `last` the newest rowid, `first` the oldest, `count` the source's rows, `reset` true
                          when the source's first rowid is not F or count < N (the session started over: its rows were deleted and
                          written anew with new rowids — the page starts over)

THE BOARD NEVER DRIVES THE ENGINE: the stepper runs beside it (python3 World/step9/world_stepper.py --by verse --pace 1); the database
opened read-only (mode=ro); the page's controls replay what has arrived (D25).
"""
import argparse, json, os, re, sqlite3, sys, threading, time, urllib.parse
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))

DB = os.path.normpath(os.path.join(HERE, '..', 'journal', 'data', 'world.sqlite'))
PAGE = os.path.join(HERE, 'world_board.html')
NAMES = os.path.join(HERE, 'board_names.yaml')
REG = os.path.join(ROOT, 'logic', 'corpus', 'entity_registry.yaml')
MOCK = os.path.join(HERE, 'forms_numbers_walk', 'loop_2026-09-14', 'mockup_board.html')
DEFAULT_SOURCE = 'cold_run_sequence/stepper'
BASE = 'cold_run_sequence/seed_isaac'
BOOK = {'Gen': 1, 'Exod': 2, 'Lev': 3, 'Num': 4, 'Deut': 5}
BOOKN = {v: k for k, v in BOOK.items()}
GROUP = {'person': 'People', 'collective': 'Peoples and groups', 'people': 'Peoples and groups', 'compound': 'Peoples and groups', 'place': 'Places',
         'object': 'Things', 'creature': 'Creatures', 'institution': 'Institutions', 'divine': 'Heaven'}
GROUPS = ['The frame', 'Places', 'Times', 'Plants', 'Creatures', 'Guards', 'People', 'Peoples and groups', 'Things', 'Institutions', 'Heaven', 'Others']


class Unnamed(Exception):
    """a token the board would show without an English name (D24: refused)"""


# ── the shape of a row (the mockup's own functions, one home now) ──────────────────────────────────────────────────────────────────
def vkey(ref):
    m = re.match(r'^(Gen|Exod|Lev|Num|Deut)[ .](\d+)[:.](\d+)', ref or '')
    return (BOOK[m.group(1)], int(m.group(2)), int(m.group(3))) if m else None


def head(ref):
    m = re.match(r'^\s*((?:Gen|Exod|Lev|Num|Deut)\s+\d+:\d+(?:-\d+)?)', ref or '')
    return m.group(1) if m else (ref or '')[:20]


def own(ref):
    if ref and ' — ' in ref:
        w = re.split(r' \(|;', ref.split(' — ', 1)[1])[0].strip()
        return w[:120] + ('…' if len(w) > 120 else '')
    return ''


def words(s):
    return str(s).replace('_', ' ')


def short(v):
    if v is True or v is None:
        return ''
    if isinstance(v, list):
        return ', '.join(words(x) for x in v)[:60]
    s = words(v)
    return s if len(s) <= 60 else s[:60] + '…'


def shape(rowid, seq, op, kind, subj, data, ref):
    """one tape row of the index → the board's row (the mockup's dict, plus id = the rowid the page polls by)"""
    d = json.loads(data); k = kind.replace('run.', '')
    r = {'id': rowid, 's': seq, 'k': k, 'd': op, 'e': subj, 'r': head(ref or ''), 'w': own(ref or '')}
    if k == 'marker':
        r['w'] = re.split(r' — | \(', str(d.get('value') or ''))[0][:70]
    if k == 'event':
        r['a'] = words(d.get('kind', ''))
    if k in ('write', 'retro_write'):
        r.update(f=words(d.get('effect', '')), p=bool(d.get('open')), v=short(d.get('value')), q=d.get('seq'))
    if k == 'timer_set':
        r.update(f=words(d.get('effect', '')), due=d.get('due'))
    if k == 'timer_fire':
        r.update(f=words(d.get('effect', '')))
    if k == 'close':
        r.update(f=words(d.get('effect', '')), q=d.get('entry_seq'), r=head(d.get('note', '')), w=own(d.get('note', '')))
    return r


# ── the names (D24) ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
def load_names():
    """id → {n: the English, g: the group}: the registry's en with its kind's group, then the board's table (a token's name and group)"""
    reg = yaml.safe_load(open(REG, encoding='utf-8'))
    names = {}
    for e in reg.get('entities') or []:
        if isinstance(e, dict) and e.get('id') and e.get('en'):
            en = re.sub(r'\s*\([^)]*—[^)]*\)', '', e['en']).strip()      # the registry's own notes in parentheses with a dash are notes, not the name
            names[e['id']] = {'n': en or e['en'], 'g': GROUP.get(e.get('kind', ''), 'Others')}
    table = yaml.safe_load(open(NAMES, encoding='utf-8')).get('names') or {}
    for k, v in table.items():
        names[k] = {'n': v['en'], 'g': v.get('group', 'Others')}
    return names


def name_of(id, names):
    """the registry or the table; else a runner's own id read as English (the-world → the world); an underscored token refused"""
    if id in names:
        return names[id]
    if '_' in id:
        raise Unnamed(id)
    w = id.replace('-', ' ')
    return {'n': w if w.startswith('the ') else w[:1].upper() + w[1:], 'g': 'Others'}


def subjects(con, source):
    return [r[0] for r in con.execute("SELECT DISTINCT subj FROM events WHERE source=? AND layer='L3' AND subj NOT IN ('clock','world')", (source,))]


def unnamed(con, source, names=None):
    """the ids the source or the births would show without a name: every entity of the view must be named; a subject only if underscored"""
    names = names or load_names()
    view = [r[0] for r in con.execute("SELECT entity FROM entities WHERE first_ref IS NOT NULL")]
    return sorted({e for e in view if e not in names} | {s for s in subjects(con, source) if s not in names and '_' in s})


def all_names(con, names=None):
    """the names the page needs: the registry and the table, plus every subject of every source read by the dashed rule"""
    names = dict(names or load_names())
    for s in con.execute("SELECT DISTINCT subj FROM events WHERE layer='L3' AND subj NOT IN ('clock','world')"):
        if s[0] not in names:
            try:
                names[s[0]] = name_of(s[0], names)
            except Unnamed:
                names[s[0]] = {'n': s[0] + ' (no English name yet — board_names.yaml)', 'g': 'Others'}   # the gate is red for this; the page still says so in English
    return names


# ── the births (D23) ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
_BIRTHS = {}


def births(con, names, db_key=None):
    """every entity of the entities view at its first mention, in the text's own order (the fold's mention rows), as born rows with a key"""
    key = db_key or id(con)
    if key in _BIRTHS:
        return _BIRTHS[key]
    first = dict(con.execute("SELECT entity, first_ref FROM entities WHERE first_ref IS NOT NULL").fetchall())
    order = dict(con.execute("SELECT json_extract(data,'$.entity'), min(rowid) FROM events WHERE kind='fold.mention' GROUP BY 1").fetchall())
    out = []
    for e, ref in first.items():
        k = vkey(ref)
        if k is None:
            continue
        nm = name_of(e, names)
        out.append({'k': 'born', 'e': e, 'r': '%s %d:%d' % (BOOKN[k[0]], k[1], k[2]), 'key': k, 'n': nm['n'], 'g': nm['g'], 'o': order.get(e, 0)})
    out.sort(key=lambda b: b['o'])
    for b in out:
        b.pop('o')
    _BIRTHS[key] = out
    return out


def rows_after(con, source, after=0, known=None, names=None, db_key=None, first=None):
    """the API's answer: the source's rows after a rowid with the births due before each one; last, first, count, reset"""
    names = names or load_names()
    light = con.execute("SELECT rowid, kind, ref FROM events WHERE source=? AND layer='L3' ORDER BY rowid", (source,)).fetchall()
    count = len(light)
    first_now = light[0][0] if light else 0
    reset = (known is not None and known > 0 and count < known) or (first is not None and first > 0 and first_now != first)   # the session started over: fewer rows, or its rows written anew (new rowids)
    if reset:
        after = 0
    born = births(con, names, db_key)
    by_anchor, bi = {}, 0
    for rid, kind, ref in light:
        kk = vkey(head(ref)) if kind in ('run.marker', 'run.event') else None
        while bi < len(born) and kk is not None and born[bi]['key'] <= kk:
            by_anchor.setdefault(rid, []).append(born[bi]); bi += 1
    out = []
    for rid, seq, op, kind, subj, data, ref in con.execute(
            "SELECT rowid, seq, op, kind, subj, data, ref FROM events WHERE source=? AND layer='L3' AND rowid > ? ORDER BY rowid", (source, after)):
        for b in by_anchor.get(rid, []):
            out.append({k: v for k, v in b.items() if k != 'key'})
        out.append(shape(rid, seq, op, kind, subj, data, ref))
    return {'source': source, 'rows': out, 'last': light[-1][0] if light else after, 'first': first_now, 'count': count, 'reset': reset}


def status(con, db, default):
    srcs = [{'source': s, 'rows': n} for s, n in con.execute("SELECT source, count(*) FROM events WHERE layer='L3' GROUP BY source ORDER BY min(rowid)")]
    return {'db': db, 'read_only': True, 'writes': 'one signal — board_asks.json beside the database; never the database', 'default_source': default, 'sources': srcs,
            'engine': engine_state(db)}


# ── THE BOARD DRIVES THE ENGINE (D31-D33, 2026-09-15; the owner: "the buttons should control the engine, it should not run on auto pilot") ──
# THE STEP SIGNAL: two files beside the database, one writer each way — board_asks.json (this server: a count of asks) and board_engine.json
# (the stepper in --board mode: its heartbeat, the next verse, the steps done). The page's Next and Auto-play ask one step at a time through
# the one control route; the engine takes exactly one step per ask and waits. The database stays read-only here.
_ASK_LOCK = threading.Lock()


def control_paths(db):
    d = os.path.dirname(os.path.abspath(db))
    return os.path.join(d, 'board_asks.json'), os.path.join(d, 'board_engine.json')


def _read_json(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def engine_state(db):
    """what the page shows as ENGINE: listening (a heartbeat within five seconds, not sealed), waiting, done, asked, pending, the next verse"""
    asks_p, eng_p = control_paths(db)
    a, e = _read_json(asks_p), _read_json(eng_p)
    asked = int(a.get('asked', 0) or 0)
    done, opened = int(e.get('done', 0) or 0), int(e.get('opened_at', 0) or 0)
    listening = bool(e) and not e.get('sealed') and (time.time() - float(e.get('beat', 0) or 0)) < 5.0
    return {'listening': listening, 'sealed': bool(e.get('sealed')), 'end': bool(e.get('end')), 'waiting': bool(e.get('waiting')),
            'done': done, 'asked': asked, 'pending': max(0, asked - opened - done) if e else 0, 'next': e.get('next'), 'pid': e.get('pid'), 'source': e.get('source')}


def ask_step(db):
    """one more ask on file (read, add one, write whole, replace) — the only thing the board ever writes"""
    asks_p, _ = control_paths(db)
    with _ASK_LOCK:
        n = int(_read_json(asks_p).get('asked', 0) or 0) + 1
        tmp = asks_p + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump({'asked': n, 't': time.time()}, f)
        os.replace(tmp, asks_p)
    return n


def connect(db):
    con = sqlite3.connect('file:%s?mode=ro' % urllib.parse.quote(os.path.abspath(db)), uri=True, check_same_thread=False)
    con.execute('PRAGMA busy_timeout = 2000')
    return con


# ── the server (D22) ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
def make_handler(db, default):
    names = load_names()

    class Handler(BaseHTTPRequestHandler):
        def _send(self, body, ctype='application/json; charset=utf-8', code=200):
            data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode('utf-8')
            self.send_response(code); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store'); self.end_headers(); self.wfile.write(data)

        def do_GET(self):
            u = urllib.parse.urlsplit(self.path); q = urllib.parse.parse_qs(u.query)
            try:
                if u.path == '/':
                    self._send(open(PAGE, 'rb').read(), 'text/html; charset=utf-8'); return
                con = connect(db)
                try:
                    if u.path == '/api/status':
                        self._send(status(con, db, default))
                    elif u.path == '/api/names':
                        self._send({'names': all_names(con, names), 'groups': GROUPS})
                    elif u.path == '/api/rows':
                        src = q.get('source', [default])[0]; after = int(q.get('after', ['0'])[0]); known = int(q.get('known', ['0'])[0]); first = int(q.get('first', ['0'])[0])
                        body = rows_after(con, src, after, known, names, db_key=db, first=first); body['engine'] = engine_state(db)
                        self._send(body)
                    elif u.path == '/api/engine':
                        self._send({'engine': engine_state(db)})
                    else:
                        self._send({'error': 'no such route'}, code=404)
                finally:
                    con.close()
            except Exception as e:
                self._send({'error': '%s: %s' % (type(e).__name__, e)}, code=500)

        def do_POST(self):                                   # D31: the one control route — a step asked; nothing else is written
            u = urllib.parse.urlsplit(self.path)
            try:
                n = int(self.headers.get('Content-Length') or 0)
                body = json.loads(self.rfile.read(n).decode('utf-8') or '{}') if n else {}
                if u.path == '/api/control' and body.get('cmd') == 'step':
                    asked = ask_step(db)
                    self._send({'asked': asked, 'engine': engine_state(db)})
                elif u.path == '/api/control':
                    self._send({'error': 'the control route takes {"cmd": "step"} and nothing else'}, code=400)
                else:
                    self._send({'error': 'no such route'}, code=404)
            except Exception as e:
                self._send({'error': '%s: %s' % (type(e).__name__, e)}, code=500)

        def log_message(self, fmt, *args):
            if '/api/rows' not in (args[0] if args else '') and '/api/control' not in (args[0] if args else ''):
                sys.stderr.write('  %s\n' % (fmt % args))
    return Handler


def serve(host, port, db, source):
    srv = ThreadingHTTPServer((host, port), make_handler(db, source))
    print('THE BOARD (THE LOOP item 10): http://%s:%d/  — the database %s read-only; the source %s (the page follows it; ?source=<other> for another world)' % (host, port, db, source))
    print('  run the engine beside it: python3 World/step9/world_stepper.py --board     (the page\'s Next and Auto-play step it; Ctrl-C stops the board)')
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print('\nthe board closed')


# ── the gate ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
def gate(db, source):
    lines, bad = [], 0
    con = connect(db); names = load_names()
    for src in sorted({source, BASE}):
        miss = unnamed(con, src, names)
        bad += bool(miss)
        lines.append('  names for %-34s %s' % (src + ':', 'every id named' if not miss else 'UNNAMED %d: %s' % (len(miss), ', '.join(miss[:10]))))
    mock = json.loads(re.search(r'const ROWS = (\[.*?\]);\n', open(MOCK, encoding='utf-8').read()).group(1))
    KEYS = ('s', 'k', 'd', 'e', 'r', 'w', 'a', 'f', 'p', 'v', 'q', 'due')
    out = rows_after(con, BASE, 0, 0, names, db_key=db)['rows']
    mt = [r for r in mock if r['k'] != 'born']; bt = [r for r in out if r['k'] != 'born'][:len(mt)]
    same = len(bt) == len(mt) and all({k: a.get(k) for k in KEYS} == {k: b.get(k) for k in KEYS} for a, b in zip(bt, mt))
    bad += (not same)
    lines.append('  the shaping of the base\'s first %d lines against the mockup\'s rows: %s' % (len(mt), 'EQUAL field for field' if same else 'DIFFER'))

    def nxt(rows, i):
        return next((r['s'] for r in rows[i + 1:] if r['k'] != 'born'), None)
    forty = {r['e'] for r in mock if r['k'] == 'born'}
    mp = [(r['e'], r['r'], nxt(mock, i)) for i, r in enumerate(mock) if r['k'] == 'born']
    bp = [(r['e'], r['r'], nxt(out, i)) for i, r in enumerate(out) if r['k'] == 'born' and r['e'] in forty]
    bad += (mp != bp)
    lines.append('  the mockup\'s %d births placed before the same rows: %s' % (len(mp), 'YES' if mp == bp else 'NO'))
    born = [r for r in out if r['k'] == 'born']
    f3 = [(r['e'], r['r']) for r in born[:3]]
    ok3 = f3 == [('god', 'Gen 1:1'), ('shamayim', 'Gen 1:1'), ('the_earth', 'Gen 1:1')]   # the data's own order: God is mentioned first at 1:1 (the design had typed the mockup's forty)
    bad += (not ok3)
    lines.append('  the births: %d things appear over the base (the view %d); the first three %s %s' % (len(born), len(births(con, names, db)), f3, 'ok' if ok3 else 'WRONG'))
    page = open(PAGE, encoding='utf-8').read() if os.path.exists(PAGE) else ''
    okp = bool(page) and 'const ROWS = [' not in page and 'api/rows' in page
    bad += (not okp)
    lines.append('  the page: %s' % ('reads the routes, no embedded rows' if okp else 'MISSING or carries embedded rows'))
    con.close()
    lines.append('THE BOARD GATE: %s' % ('GREEN' if not bad else 'RED (%d)' % bad))
    return bad == 0, lines


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', default=DB); ap.add_argument('--source', default=DEFAULT_SOURCE)
    ap.add_argument('--host', default='127.0.0.1'); ap.add_argument('--port', type=int, default=8765)
    ap.add_argument('--gate', action='store_true')
    a = ap.parse_args(argv)
    if a.gate:
        ok, lines = gate(a.db, a.source)
        print('\n'.join(lines)); sys.exit(0 if ok else 1)
    serve(a.host, a.port, a.db, a.source)


if __name__ == '__main__':
    main()
