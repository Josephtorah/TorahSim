#!/usr/bin/env python3
"""patch_sweep_line.py — THE LOOP step 7 (a): the sweep's line into the three records that waited for it (2026-09-14)."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
SWEEP = "57/57 runners green, 6,378 graded cells (unchanged from 15b's close; the dependency gate 251 required edges / 174 pointers, 338 live import edges, 482 + 173 on file; the daemon gate 62 daemons, 427 WRAPPED, open aliases 3)"
def patch(path, old, new):
    t = open(path, encoding='utf-8').read(); n = t.count(old)
    if n == 0 and new in t: print('%s: already' % path); return
    assert n == 1, (path, n); open(path, 'w', encoding='utf-8').write(t.replace(old, new)); print('%s: patched' % path)
patch((_ROOT + '/World/step9/THE_LOOP.md'),
      "THE SWEEP: running in the background at the close; its line is appended below when it lands.",
      "THE SWEEP: %s." % SWEEP)
patch((_ROOT + '/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'),
      "the sweep in the background at the close (its line in THE_LOOP.md's as-built and the\nstate doc when it lands)",
      "the sweep %s" % SWEEP)
p = (_ROOT + '/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md')
t = open(p, encoding='utf-8').read()
line = "═══ ADDENDUM to #171 (2026-09-14, the sweep landed): THE SWEEP %s. #171 IS A CLEAN COMPACTION POINT.\n" % SWEEP
if line not in t:
    open(p, 'w', encoding='utf-8').write(t + line); print('state doc: addendum appended')
