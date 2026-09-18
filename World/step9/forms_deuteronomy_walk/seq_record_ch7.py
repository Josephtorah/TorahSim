import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
"""seq_record.py — THE RECORDER (the sequential run's first instrument, 2026-09-07): import every cold_run_*.py with
the world engine's submit/advance/close/cancel_timers INSTRUMENTED, so every scene's events are captured with their
full literal values (the loops expanded at runtime) and attributed to the runner whose scene submitted them (the
first cold_run_*.py frame on the stack — a leaf caller's import of another runner is attributed to the callee).
Prints the census: per runner, submits by the registry's FORM (act / speech / statute / case) and by source class
(a Torah verse of the three books first = HISTORY; a tractate/Sifra/Onkelos/Mishnah first = a CASE row), and
writes the recording to seq_recording.json for the stitcher."""
import os as _os
import subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sys, os, io, glob, json, re, contextlib, importlib, collections, traceback
HERE = (_ROOT + '/World/step9')
sys.path.insert(0, HERE)
os.chdir(HERE)
import yaml
import world_engine as WE

REC = []                       # (runner, world_key, op, day, payload)
_worlds = {}

def _runner_of_stack():
    f = sys._getframe(2)
    while f is not None:
        fn = os.path.basename(f.f_code.co_filename)
        if fn.startswith('cold_run_') and fn.endswith('.py'):
            return fn[9:-3]
        f = f.f_back
    return '<engine>'

def _wkey(w):
    if id(w) not in _worlds:
        _worlds[id(w)] = (len(_worlds), w.clock.era)
    return _worlds[id(w)][0]

_submit, _advance, _close, _cancel = WE.World.submit, WE.World.advance, WE.World.close, WE.World.cancel_timers
def submit(self, event):
    REC.append((_runner_of_stack(), _wkey(self), 'submit', self.clock.day, json.loads(json.dumps(event, default=str))))
    return _submit(self, event)
def advance(self, to_day):
    REC.append((_runner_of_stack(), _wkey(self), 'advance', self.clock.day, to_day))
    return _advance(self, to_day)
def close(self, eid, effect, note, value=None):   # O8 S1 (2026-09-08): the engine's close(value=) — the plague closes by name
    if getattr(self, '_consuming', None):             # THE TENT sitting 1 (2026-09-09): a close made INSIDE a daemon's call is the daemon's own write, replayed on any world — never a tape line; only a scene's close is the text's act
        return _close(self, eid, effect, note, value=value)
    REC.append((_runner_of_stack(), _wkey(self), 'close', self.clock.day, [eid, effect, note] + ([value] if value is not None else [])))
    return _close(self, eid, effect, note, value=value)
def cancel_timers(self, subject, effect, note):
    REC.append((_runner_of_stack(), _wkey(self), 'cancel', self.clock.day, [subject, effect, note]))
    return _cancel(self, subject, effect, note)
WE.World.submit, WE.World.advance, WE.World.close, WE.World.cancel_timers = submit, advance, close, cancel_timers

failed = []
for f in sorted(glob.glob(os.path.join(HERE, 'cold_run_*.py'))):
    mod = os.path.basename(f)[:-3]
    if mod in sys.modules:
        continue
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            importlib.import_module(mod)
    except BaseException as e:
        failed.append((mod, repr(e)[:200]))
# the five runners whose scenes run under main() alone: call scene() explicitly so the census scans them too
for mod in ('cold_run_pesach', 'cold_run_negaim', 'cold_run_yoma', 'cold_run_vayikra5', 'cold_run_guardians'):
    m = sys.modules.get(mod)
    if m is not None and hasattr(m, 'scene'):
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                m.scene()
        except BaseException as e:
            failed.append((mod + '.scene', repr(e)[:200]))
print('recorder: %d runner modules imported, %d failed: %s' % (len([m for m in sys.modules if m.startswith('cold_run_')]), len(failed), failed))

ev = yaml.safe_load(open(os.path.join(HERE, 'event_vocabulary.yaml'), encoding='utf-8'))
E = ev.get('events') or ev
FORM = {k: v.get('form') for k, v in E.items()}
VERSE = re.compile(r'^(Gen|Exod|Lev|Num|Deut)\s+(\d+):(\d+)')

def source_class(cs):
    m = VERSE.match(cs or '')
    if m:
        return 'torah3' if m.group(1) in ('Gen', 'Exod', 'Lev', 'Num', 'Deut') else 'torah_other'   # THE DEUTERONOMY WALK 1b (2026-09-15): the fifth book joins the tape's books; THE TENT sitting 2 (2026-09-09): Numbers joined
    return 'case_row'

def key_of(rec):
    return rec[0]

by_runner = collections.OrderedDict()
worlds_by_runner = collections.defaultdict(set)
for runner, wk, op, day, payload in REC:
    if op != 'submit':
        continue
    worlds_by_runner[runner].add(wk)
    c = by_runner.setdefault(runner, collections.Counter())
    form = FORM.get(payload.get('kind'), '?')
    sc = source_class(payload.get('case_source'))
    c[(form, sc)] += 1
    c['total'] += 1
    if form in ('act', 'speech') and sc == 'torah3':
        c['HISTORY'] += 1
print('\nCENSUS (form x source): runner | worlds | total | act/speech on a three-book verse = HISTORY | case rows | statute | act/speech sourced to a tractate')
tot = collections.Counter()
for r, c in by_runner.items():
    hist = c['HISTORY']; total = c['total']
    case_rows = sum(v for (k, v) in c.items() if isinstance(k, tuple) and k[0] == 'case')
    statute = sum(v for (k, v) in c.items() if isinstance(k, tuple) and k[0] == 'statute')
    act_tract = sum(v for (k, v) in c.items() if isinstance(k, tuple) and k[0] in ('act', 'speech') and k[1] != 'torah3')
    unk = sum(v for (k, v) in c.items() if isinstance(k, tuple) and k[0] == '?')
    print('  %-18s worlds %d  total %3d  HISTORY %3d  case %3d  statute %2d  act/speech-on-tractate %3d  unregistered %d' % (r, len(worlds_by_runner[r]), total, hist, case_rows, statute, act_tract, unk))
    tot['total'] += total; tot['hist'] += hist; tot['case'] += case_rows; tot['statute'] += statute; tot['act_tract'] += act_tract
print('  TOTAL submits %d; HISTORY %d; case rows %d; statute %d; act/speech-on-tractate %d' % (tot['total'], tot['hist'], tot['case'], tot['statute'], tot['act_tract']))
json.dump({'rec': REC, 'worlds': {str(k): v for k, v in _worlds.items()}}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seq_recording.json'), 'w'), ensure_ascii=False, indent=0)
print('recording: %d records written' % len(REC))
