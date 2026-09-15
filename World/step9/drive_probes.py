#!/usr/bin/env python3
"""THE DRIVE PROBES — THE BOARD DRIVES THE ENGINE (D31-D33, 2026-09-15; the owner: "the buttons should control the engine, it should not
run on auto pilot behind the scenes" and "put a stop button also. if I click autoplay it shoudl change to stop. one button two options.
built it"). Written before the code and run to FAIL. Every probe runs in ITS OWN journal folder (WORLD_JOURNAL_DIR) on its own port —
never over the live session (the lesson of 2026-09-15: a second stepper under the same source name deletes the live session's rows).

X1 the engine in --board mode opens, announces itself beside its database (board_engine.json: listening, waiting, done 0) and takes
   NO step unasked in three seconds
X2 the board's one control route — POST /api/control {"cmd": "step"} — counts an ask (board_asks.json) and the status route reports
   the engine (asked, done, listening)
X3 three asks → exactly three steps: done 3, rows in the database, and no fourth step in three seconds of silence
X4 Ctrl-C (SIGINT) seals the session: the segment file on disk, the engine file says sealed, the status says no engine listens
X5 the page: the one button carries the two words (Auto-play / Stop), Next asks the engine at the live end through the control route,
   the engine's --board mode is named on the page; the board's gate GREEN over the real database (read-only)

Run: python3 World/step9/drive_probes.py
"""
import os, sys, json, time, signal, socket, sqlite3, tempfile, subprocess, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
STEPPER, BOARD, PAGE = os.path.join(HERE, 'world_stepper.py'), os.path.join(HERE, 'world_board.py'), os.path.join(HERE, 'world_board.html')
SOURCE = 'cold_run_sequence/stepper'


def free_port():
    s = socket.socket(); s.bind(('127.0.0.1', 0)); p = s.getsockname()[1]; s.close(); return p


def http(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8') if body is not None else None,
                                 headers={'Content-Type': 'application/json'} if body is not None else {})
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read().decode('utf-8'))


def rd(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def rows_of(db):
    if not os.path.exists(db):
        return 0
    con = sqlite3.connect('file:%s?mode=ro' % db, uri=True)
    try:
        return con.execute("SELECT count(*) FROM events WHERE layer='L3' AND source=?", (SOURCE,)).fetchone()[0]
    except sqlite3.Error:
        return 0
    finally:
        con.close()


def wait_for(cond, seconds, every=0.2):
    t0 = time.time()
    while time.time() - t0 < seconds:
        v = cond()
        if v:
            return v
        time.sleep(every)
    return cond()


def main():
    tmp = tempfile.mkdtemp(prefix='drive_probes_')
    env = dict(os.environ, WORLD_JOURNAL_DIR=tmp)
    db, eng_p, asks_p = os.path.join(tmp, 'world.sqlite'), os.path.join(tmp, 'board_engine.json'), os.path.join(tmp, 'board_asks.json')
    port = free_port(); base = 'http://127.0.0.1:%d/' % port
    results, log = [], open(os.path.join(tmp, 'stepper.log'), 'w')
    stepper = subprocess.Popen([sys.executable, '-u', STEPPER, '--board', '--by', 'verse'], env=env, stdout=log, stderr=subprocess.STDOUT,
                               stdin=subprocess.DEVNULL, cwd=ROOT)
    server = None

    def ok(name, cond, detail):
        results.append((name, bool(cond)))
        print('  %s  %s' % ('PASS' if cond else 'FAIL', name)); print('        %s' % detail)

    try:
        # X1 — the engine announces itself and waits (the import of the tape is the fixed price: up to four minutes)
        ann = wait_for(lambda: (rd(eng_p) if rd(eng_p).get('beat') else None) or (stepper.poll() is not None and {'exited': stepper.returncode}), 240)
        time.sleep(3)
        e = rd(eng_p); r0 = rows_of(db)
        ok('X1 the engine in --board mode announces itself and takes no step unasked',
           ann and 'exited' not in (ann or {}) and e.get('waiting') and e.get('done') == 0 and time.time() - e.get('beat', 0) < 5 and r0 == 0,
           'engine file %s; rows unasked %d; process %s' % ({k: e.get(k) for k in ('waiting', 'done', 'next', 'pid')} if e else 'absent', r0,
                                                         'running' if stepper.poll() is None else 'exited %s' % stepper.returncode))
        # X2 — the control route counts an ask; the status reports the engine
        server = subprocess.Popen([sys.executable, BOARD, '--db', db, '--port', str(port)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=ROOT)
        st = wait_for(lambda: (lambda: http(base + 'api/status'))() if _up(base) else None, 20)
        try:
            c = http(base + 'api/control', {'cmd': 'step'})
        except Exception as ex:                      # an old server closes the connection on a POST — that is a FAIL, not a crash
            c = {'error': '%s: %s' % (type(ex).__name__, ex)}
        a = rd(asks_p); st2 = http(base + 'api/status') if _up(base) else {}
        eng = st2.get('engine') or {}
        ok('X2 POST /api/control step counts an ask and the status reports the engine',
           c.get('asked') == 1 and a.get('asked') == 1 and eng.get('asked') == 1 and eng.get('listening') is True,
           'control answered %s; asks file %s; status engine %s' % (c, a, {k: eng.get(k) for k in ('asked', 'done', 'listening', 'waiting', 'next')}))
        # X3 — three asks, three steps, no fourth
        done1 = wait_for(lambda: rd(eng_p).get('done') == 1, 10)
        for _ in range(2):
            try: http(base + 'api/control', {'cmd': 'step'})
            except Exception: pass
            wait_for(lambda: rd(eng_p).get('done') >= 2, 10)
        done3 = wait_for(lambda: rd(eng_p).get('done') == 3, 10)
        r3 = rows_of(db); time.sleep(3); e3 = rd(eng_p); r3b = rows_of(db)
        ok('X3 three asks are exactly three steps, and the engine waits after them',
           done1 and done3 and e3.get('done') == 3 and r3 > 0 and r3b == r3 and e3.get('waiting'),
           'done after the first ask %s; done %s; rows %d then %d after 3 s of silence; waiting %s; next %s' % (done1, e3.get('done'), r3, r3b, e3.get('waiting'), e3.get('next')))
        # X4 — Ctrl-C seals
        if stepper.poll() is None:
            stepper.send_signal(signal.SIGINT)
        try:
            stepper.wait(timeout=60)
        except subprocess.TimeoutExpired:
            stepper.kill()
        e4 = rd(eng_p); seg = os.path.join(tmp, 'L3_run_cold_run_sequence_stepper.jsonl'); st4 = http(base + 'api/status') if _up(base) else {}
        ok('X4 Ctrl-C seals the session and the board sees no engine',
           e4.get('sealed') is True and os.path.exists(seg) and (st4.get('engine') or {}).get('listening') is False,
           'sealed %s; segment %s; status listening %s; exit %s' % (e4.get('sealed'), os.path.exists(seg), (st4.get('engine') or {}).get('listening'), stepper.returncode))
    finally:
        log.close()
        if stepper.poll() is None:
            stepper.kill()
        if server is not None:
            server.terminate()
    # X5 — the page and the gate
    page = open(PAGE, encoding='utf-8').read()
    has = {'Stop': "'Stop'" in page, 'control route': 'api/control' in page, '--board named': '--board' in page, 'no Follow': 'id="follow"' not in page,
           'Next asks the engine': 'askStep' in page}
    gate = subprocess.run([sys.executable, BOARD, '--gate'], capture_output=True, text=True, cwd=ROOT)
    ok('X5 the page carries Stop, the control route and --board; the gate green', all(has.values()) and gate.returncode == 0,
       '%s; the gate exit %d (%s)' % (has, gate.returncode, (gate.stdout.strip().split('\n') or [''])[-1]))
    n = sum(1 for _, v in results if v)
    print('%d/%d probes  (the probes\' folder %s)' % (n, len(results), tmp))
    sys.exit(0 if n == len(results) else 1)


def _up(base):
    try:
        urllib.request.urlopen(base + 'api/status', timeout=2).read(); return True
    except Exception:
        return False


if __name__ == '__main__':
    main()
