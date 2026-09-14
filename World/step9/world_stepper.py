#!/usr/bin/env python3
"""world_stepper.py — THE LOOP step 7 THE LOOP THAT WAITS, part (b) THE STEPPER (2026-09-14; the owner: "ok go b"; the design
World/step9/THE_LOOP.md "Step 7 ... part (b) THE STEPPER", decision D15 THE TAPE AS A GENERATOR; the probes step_probes.py written first,
0/8 on the unchanged tree).

THE TAPE AS A GENERATOR: the stitched tape's source (the section of cold_run_sequence.py between the sentinels) is transformed at load —
every engine-call line is prefixed with `yield (<the verse of the call>, <the line's ordinal>); ` — and executed as a generator: each
next() runs exactly one tape line (one outermost engine call, whose lines part (a)'s seal writes to disk and into the database inside
it) and then yields the verse of the NEXT call before running it. The pause is between two next() calls: no thread, no engine change;
the world stands still, every line so far sealed, the database current. Because the generator yields BEFORE a call, the stepper can
stop at the LEFT EDGE of a verse exactly as the cursor does — and, unlike the cursor, resume.

THE SESSION journals under its own source `cold_run_sequence/stepper` (the segment L3_run_cold_run_sequence_stepper.jsonl; its rows under
that source in the one database) — the base run's rows and segment are never touched. A session that ends early seals a PARTIAL segment
(valid: its header counts its lines) and part (a)'s audit runs on it. THE REPLAY IS THE AUDIT: when the base segment of the running
setting is on disk, every line the session seals must equal the base's line at the same ordinal, or the session is REFUSED there, named.

THE GRAINS of a step: call (one tape line) | verse (every line at the current call's verse) | chapter | marker (through the next date
with the timers it fires) | day (until the clock moved) | a verse address (until the NEXT call is at or after it — the left edge).
THE REPORT at every pause: the lines run and sealed, the next call's verse, the clock, the entities, the open entries, the pending
timers; --show reads the rows FROM THE DATABASE through the five views under the session's source — the database is the state.
--pause waits for Enter between steps: a CONTROL word, never a data event (the port of part (c) is the only door for inputs).

Run: python3 World/step9/world_stepper.py [--from <verse>] [--to <verse>] [--by call|verse|chapter|marker|day] [--steps N]
     [--show open|ledger <entity>|custody|timers] [--pause] [--quiet]
"""
import os, re, sys, sqlite3, collections
HERE = os.path.dirname(os.path.abspath(__file__))
JOURNAL = os.path.normpath(os.path.join(HERE, '..', 'journal'))
sys.path.insert(0, HERE)
sys.path.insert(0, JOURNAL)
import world_engine as WE
import world_journal as WJ
from worldledger import canon

SOURCE = 'cold_run_sequence/stepper'
GRAINS = ('call', 'verse', 'chapter', 'marker', 'day')
# the tape writes a string in double quotes when it holds an apostrophe (the stitcher's repr): every pattern reads either quote
_MARKER = re.compile(r"""w\.marker\((['"])(.*?)\1""")
_SOURCE = re.compile(r"""['"]case_source['"]:\s*(['"])(.*?)\1""")
_CLOSE = re.compile(r"""w\.close\((['"]).*?\1,\s*(['"]).*?\2,\s*(['"])(.*?)\3""")
_CALL = re.compile(r"\bw\.(submit|marker|close)\(")
BOOK_NAME = {v: k for k, v in WE.BOOK_ORDER.items()}


def head(s):
    """'Book c:v' — the verse a reference opens with, or the string itself when it opens with none"""
    fv = WE.first_verse(s)
    return '%s %d:%d' % fv if fv else s


def verse_of(line):
    """the verse of a tape line's engine call: a marker's own verse, a submit's case_source, a close's note"""
    for rx, g in ((_MARKER, 2), (_SOURCE, 2), (_CLOSE, 4)):
        m = rx.search(line)
        if m:
            return head(m.group(g))
    return None


def transform(source):
    """the tape's source with `yield (verse, ordinal); ` prefixed to every engine-call line — the function becomes a generator that yields
    BEFORE each call the verse it is about to run; returns (source, yields). The stitcher's contract — ONE engine call per line — is
    asserted on every line (measurement 1 of the design: 1,507 calls on 1,507 lines)."""
    out, n = [], 0
    for i, line in enumerate(source.split('\n'), 1):
        stripped = line.lstrip()
        calls = len(_CALL.findall(line.split('#', 1)[0])) if not stripped.startswith('#') else 0
        if calls == 0:
            out.append(line)
            continue
        if calls != 1:
            raise SystemExit('THE STEPPER: line %d of the tape carries %d engine calls — the tape is one call per line (the stitcher\'s contract)' % (i, calls))
        indent = line[:len(line) - len(stripped)]
        out.append('%syield (%r, %d); %s' % (indent, verse_of(line), i, stripped))
        n += 1
    return '\n'.join(out), n


def tape_section(path):
    text = open(path, encoding='utf-8').read()
    return text.split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0].split('\n', 1)[1]


class Stepper:
    """the tape one call at a time: Stepper(...).step(by) → a report; .show(what) → rows from the database; .close() → the seal"""

    def __init__(self, tape_source=None, world=None, out_dir=None, namespace=None, base=None, from_verse=None, source=SOURCE):
        self.source = source
        self.P = {}
        if tape_source is None:                        # THE REAL TAPE: the world built as run_to builds it (the import is the session's fixed price)
            import cold_run_sequence as CS
            self.CS = CS
            tape_source = tape_section(CS.__file__)
            namespace = dict(vars(CS))
            reg = CS.registry_map()
            setting = CS.PARAMS['sojourn_start']['value']
            self.P = dict(CS.PARAMS); self.P['sojourn_start'] = dict(CS.PARAMS['sojourn_start'], value=setting)
            world = WE.World(era='THE STEPPER — the tape one call at a time (clock unit: days; the creation epoch; sojourn_start = %s)' % setting,
                             epoch='creation', registry=reg, installation=True)
            world.laws = CS.daemons()
            del CS._INK_CHECKS[:]
            if base is None:
                cand = os.path.join(WJ.data_dir(out_dir), WJ.BASE_SEGMENT)
                base = cand if os.path.exists(cand) else None
        self.w = world
        self.M = {}
        src, self.calls = transform(tape_source)
        ns = dict(namespace or {})
        exec(compile(src, '<the tape as a generator>', 'exec'), ns)
        self.sink = WJ.attach(self.w, source, out_dir=out_dir)
        self.base, self.base_lines = base, None
        if base:
            with open(base, encoding='utf-8') as f:
                self.base_lines = [l for l in f.read().split('\n')[1:] if l.strip()]
        self.gen = ns['tape'](self.w, self.M, self.P)
        self.done, self.steps, self.audited_n, self._n0 = False, 0, 0, 0
        try:
            self.next_verse, self.next_line = next(self.gen)      # the first call's verse; nothing has run
        except StopIteration:
            self.done, self.next_verse, self.next_line = True, None, None
        self.report = self._report([], 0)
        if from_verse is not None:
            self.report = self.step(from_verse, _replay=True)     # to the LEFT EDGE, no pause

    # ---- the step ----
    def _run_one(self):
        """run the call the generator stands before; the generator then yields the following call's verse; returns (verse, line, lines sealed)"""
        v, i = self.next_verse, self.next_line
        self._n0 = len(self.sink.seg.events)
        try:
            self.next_verse, self.next_line = next(self.gen)
        except StopIteration:
            self.done, self.next_verse, self.next_line = True, None, None
        self._audit(v)
        return v, i, len(self.sink.seg.events) - self._n0

    def _audit(self, v):
        """THE REPLAY IS THE AUDIT: every line sealed by the call equals the base's line at the same ordinal, or the session is refused"""
        if self.base_lines is None:
            return
        evs = self.sink.seg.events
        for k in range(self._n0, len(evs)):
            if k >= len(self.base_lines):
                raise SystemExit('STEPPER REFUSED: the base %s ends at %d lines and this session sealed line %d (the call at %s) — the base is shorter than the tape; rerun the tape (cold_run_sequence.py), then step'
                                 % (os.path.basename(self.base), len(self.base_lines), k + 1, v))
            if canon(evs[k]) != self.base_lines[k]:
                raise SystemExit('STEPPER REFUSED: line %d of this session differs from the base %s at ordinal %d (the call at %s) — the base or the engine has moved; rerun the tape (cold_run_sequence.py), then step'
                                 % (k + 1, os.path.basename(self.base), k + 1, v))
        self.audited_n = len(evs)

    def _pause(self, by, target, v, day0, until_key):
        if self.done:
            return True
        nv = self.next_verse
        nk = WE.verse_key(nv) if nv else None
        if until_key is not None and nk is not None and nk >= until_key:
            return True
        if by == 'call':
            return True
        if by == 'verse':
            return nv != v
        if by == 'chapter':
            return (nk or (None, None))[:2] != (WE.verse_key(v) or (None, None))[:2]
        if by == 'marker':
            return any(e['kind'] == 'run.marker' for e in self.sink.seg.events[self._n0:])
        if by == 'day':
            return self.w.clock.day != day0
        return nk is not None and nk >= target                    # a verse address: the left edge

    def step(self, by='call', until=None, _replay=False):
        """advance until the grain's pause (or the left edge of `until`, whichever first); returns the report"""
        if by not in GRAINS:
            target = WE.verse_key(by)
            if target is None:
                raise SystemExit('THE STEPPER: %r is neither a grain (%s) nor a verse' % (by, ', '.join(GRAINS)))
        else:
            target = None
        until_key = WE.verse_key(until) if until else None
        if until and until_key is None:
            raise SystemExit('THE STEPPER: --to %r is not a verse' % until)
        n0, day0, ran = len(self.sink.seg.events), self.w.clock.day, []
        if not self.done:
            nk = WE.verse_key(self.next_verse) if self.next_verse else None
            at_edge = (target is not None and nk is not None and nk >= target) or (until_key is not None and nk is not None and nk >= until_key)
            if not at_edge:
                while not self.done:
                    v, i, n = self._run_one()
                    ran.append((v, i))
                    if self._pause(by, target, v, day0, until_key):
                        break
        if not _replay:
            self.steps += 1
        self.report = self._report(ran, len(self.sink.seg.events) - n0)
        return self.report

    def run(self, until=None):
        """to the end (or to the left edge of `until`) in one step"""
        return self.step(until or 'Deut 34:13')                  # a verse past the tape's last line: the whole tape

    # ---- the report and the database ----
    def _date(self):
        try:
            C = self.w.clock.calendar
            d = self.w.clock.day
            return (C.year(d),) + tuple(C.date(d)[1:])
        except BaseException:                       # the engine refuses with SystemExit (no era, no epoch): an honest None on a world without one
            return None

    def _era(self, name='exodus'):
        try:
            return self.w.clock.date_in(name)
        except BaseException:                       # the engine refuses with SystemExit (no era, no epoch): an honest None on a world without one
            return None

    def _report(self, ran, sealed):
        w, evs = self.w, self.sink.seg.events
        classes = collections.Counter(e['kind'] for e in evs[len(evs) - sealed:]) if sealed else collections.Counter()
        vr = w._verse_reached
        return {'steps': self.steps, 'ran': ran, 'sealed': sealed, 'sealed_total': len(evs), 'classes': dict(classes),
                'next_verse': self.next_verse, 'done': self.done, 'day': w.clock.day, 'date': self._date(), 'exodus': self._era('exodus'),
                'verse_reached': (BOOK_NAME.get(vr[0], vr[0]), vr[1], vr[2]) if vr else None,
                'entities': len(w.entities), 'open_entries': sum(len(e.open_entries()) for e in w.entities.values()),
                'pending_timers': len(w.timers), 'audited': (self.audited_n == len(evs)) if self.base_lines is not None else None}

    def show(self, what, *args):
        """rows FROM THE DATABASE under the session's source, through the five views: open | ledger <entity> | custody | timers"""
        db = self.sink.db
        if what == 'ledger':
            return WJ.ask(db, 'ledger', args[0], source=self.source)
        if what == 'custody':
            return WJ.ask(db, 'custody', source=self.source)
        c = sqlite3.connect(db)
        try:
            c.row_factory = sqlite3.Row
            if what == 'open':
                sql, a = "select entity, effect, ledger_op, day_written, value, written_by, verse from run_ledger where source = ? and open = 1 order by seq", (self.source,)
            elif what == 'timers':
                sql, a = "select entity, effect, day_set, due, written_by, verse from run_timers where source = ? and outcome = 'pending' order by due, seq", (self.source,)
            else:
                raise SystemExit('THE STEPPER: --show takes open | ledger <entity> | custody | timers')
            return [dict(r) for r in c.execute(sql, a).fetchall()]
        finally:
            c.close()

    def close(self, quiet=True):
        """the session's seal: the partial or whole segment written, part (a)'s audit run"""
        self.done = True
        if getattr(self.w, 'journal', None) is self.sink:
            return self.sink.seal(quiet=quiet)
        return self.sink.path, len(self.sink.seg.events), sum(self.sink.coerced.values())


def print_report(r, label='STEP'):
    ran = r['ran']
    where = ('%d line(s) at %s' % (len(ran), ran[0][0]) if ran and all(v == ran[0][0] for v, _ in ran) else
             '%d line(s) from %s to %s' % (len(ran), ran[0][0], ran[-1][0]) if ran else 'nothing ran')
    classes = ', '.join('%s %d' % (k.replace('run.', ''), n) for k, n in sorted(r['classes'].items()))
    print('%s %-4d ran %s -> %d sealed%s; %s' % (label, r['steps'], where, r['sealed'], (' (%s)' % classes) if classes else '',
                                                 'THE END OF THE TAPE' if r['done'] else 'the world stands before %s' % r['next_verse']))
    print('        day %d = %s (creation year, month, day); the exodus era %s; reached %s; entities %d, open entries %d, pending timers %d; %d lines in all; audited against the base: %s'
          % (r['day'], r['date'], r['exodus'], r['verse_reached'], r['entities'], r['open_entries'], r['pending_timers'], r['sealed_total'],
             {True: 'yes', False: 'NO', None: 'no base on disk'}[r['audited']]))


def main(argv):
    def opt(name, default=None):
        return argv[argv.index(name) + 1] if name in argv else default
    frm, to, by, steps = opt('--from'), opt('--to'), opt('--by', 'verse'), opt('--steps')
    show = argv[argv.index('--show') + 1:argv.index('--show') + 3] if '--show' in argv else None
    if show and show[0] != 'ledger':
        show = show[:1]
    pause, quiet = '--pause' in argv, '--quiet' in argv
    print('THE STEPPER (THE LOOP step 7 b): the tape one call at a time; the session journals as %s; --by %s%s%s' % (SOURCE, by, (' --from %s' % frm) if frm else '', (' --to %s' % to) if to else ''))
    st = Stepper(from_verse=frm)
    print('the base: %s' % (os.path.basename(st.base) if st.base else 'none on disk — no audit'))
    if frm:
        print_report(st.report, 'REPLAY')
    n, limit = 0, int(steps) if steps else None
    while not st.done and (limit is None or n < limit):
        if to and st.next_verse and WE.verse_key(st.next_verse) is not None and WE.verse_key(st.next_verse) >= WE.verse_key(to):
            print('the left edge of %s reached — the session stops there' % to)
            break
        r = st.step(by, until=to)
        n += 1
        print_report(r)
        if show:
            rows = st.show(*show)
            print('        --show %s: %d row(s) from the database' % (' '.join(show), len(rows)))
            for row in rows[:40]:
                print('          ' + ' | '.join('%s=%s' % (k, v) for k, v in row.items() if v is not None and k not in ('source', 'kind')))
        if pause and not st.done:
            try:
                word = input('        [Enter] to step, q to quit: ').strip().lower()
            except EOFError:
                word = 'q'
            if word == 'q':
                break
    path, nl, coerced = st.close(quiet=quiet)
    print('SESSION SEALED: %s (%d lines, coerced %d; %s); ask it: python3 World/step9/world_journal.py --ask ledger <entity> --world %s'
          % (path, nl, coerced, 'the whole tape' if st.done and st.next_verse is None and nl == len(st.base_lines or []) else 'a partial segment', SOURCE))


if __name__ == '__main__':
    main(sys.argv[1:])
