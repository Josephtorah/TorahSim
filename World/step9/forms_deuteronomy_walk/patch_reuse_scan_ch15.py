import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15: THE TAPE'S SECOND RUN REFUSED AT THE RUNNER'S IMPORT — effect_scan read the fold WHOLE, and the
# tape's first run had folded this daemon's own bears_sin line under four sources (checkpoint_check, covenant_pieces, descent_literal, seed_isaac): the scan
# found ['israel_people'] where the design's ground was [] (bears_sin the first reuse with NO prior entry — 11b's and 12b's reuses were already on Israel, so
# the growth never bit). THE GROUND IS THE FOLD BEFORE THIS DAEMON'S LINES (the runner's own words at every move): the scan now excludes written_by =
# 'law_release_firstborn' — TRUE on the bare fold and after any run. Patched in the part (ch15_part1.py) and the assembled runner alike, asserted once each.
# RUN FROM THE REPO ROOT.
import subprocess, os, py_compile
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
OLD = ('    """the entities holding an effect in the one database — None where the database is not built"""\n'
       '    if not _os.path.exists(_WDB): return None\n'
       "    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)\n"
       '    return sorted({e for (e,) in c_.execute("SELECT DISTINCT entity FROM run_ledger WHERE effect=?", (effect,)).fetchall()})\n')
NEW = ('    """the entities holding an effect in the one database BEFORE THIS DAEMON\'S LINES (its own writes excluded by written_by — the fold carries them after the tape\'s first run) — None where the database is not built"""\n'
       '    if not _os.path.exists(_WDB): return None\n'
       "    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)\n"
       '    return sorted({e for (e,) in c_.execute("SELECT DISTINCT entity FROM run_ledger WHERE effect=? AND written_by<>\'law_release_firstborn\'", (effect,)).fetchall()})   # 13b (2026-09-23): the tape\'s second run refused itself here — bears_sin (the first reuse with NO prior entry) folded by the first run under four sources; the ground is the fold before this daemon\'s lines\n')
for f in (SP + '/ch15_part1.py', ROOT + '/World/step9/cold_run_release_firstborn.py'):
    s = open(f, encoding='utf-8').read(); assert s.count(OLD) == 1, (f, s.count(OLD))
    s = s.replace(OLD, NEW); open(f, 'w', encoding='utf-8').write(s); py_compile.compile(f, doraise=True)
    print('patched', f.split('/')[-1], len(s), 'bytes')
import sqlite3
c = sqlite3.connect('file:%s/World/journal/data/world.sqlite?mode=ro' % ROOT, uri=True)
print('the scan now:', [sorted({e for (e,) in c.execute("SELECT DISTINCT entity FROM run_ledger WHERE effect=? AND written_by<>'law_release_firstborn'", (eff,))}) for eff in ('blessings_for_hearing', 'cry_heard', 'bears_sin', 'holy_things_in_the_gates_barred')])
