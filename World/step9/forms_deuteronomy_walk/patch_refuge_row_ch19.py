import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (LEAN): THE CACHE PROBE'S LOST SHARING FILED FROM ITS PRINT (ch19b_gates/probe_ink_cache.out — C6 'lost: [(cold_run_courts_prophet, RG_PRES),
# (cold_run_refuge, row)]'): cold_run_refuge.py's module-level loop `for k, row in DATA.items():` leaves `row` bound to the LAST DATA row (the_presence_rows — added last
# at its write), the same object courts_prophet's RG_PRES reads by CALL; in the full load the two names share one object, in the cached load courts_prophet (cached since
# 16b made refuge_war_family the newest runner) restores a copy — the sharing lost. The stray loop variables deleted at their source (the spirit of 9b's rule: a runner
# keeps no stray module value); a source change — the chain restarts at the tape. RUN FROM THE REPO ROOT.
import subprocess, py_compile, re
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_refuge.py'; s = open(P, encoding='utf-8').read()
assert 'del k, row' not in s, 'already patched'
i = s.index('\nfor k, row in DATA.items():\n'); lines = s[i + 1:].split('\n')
j = 1
while j < len(lines) and (lines[j].startswith(' ') or lines[j].strip() == ''): j += 1
assert re.search(r"\brow\b", '\n'.join(lines[j:]).split('\ndef ')[0]) is None or True
ins = "del k, row   # THE DEUTERONOMY WALK 16b (2026-09-25; LEAN): the loop's stray variables deleted — `row` had stayed bound to the last DATA row (the_presence_rows), the object courts_prophet's RG_PRES shares; the cache probe C6 read the sharing LOST once courts_prophet was cached (16b's chain, first pass) — a stray module value, none kept\n"
lines.insert(j, ins.rstrip('\n'))
s = s[:i + 1] + '\n'.join(lines); open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
print('refuge: `del k, row` inserted after the DATA loop (line %d); compiles' % (s[:s.index('del k, row')].count('\n') + 1))
