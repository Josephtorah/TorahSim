import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# assemble cold_run_release_firstborn.py from the parts (the CASES literal from part 5 when it exists, else an empty table for the generator's pass). ch14_assemble.py's form. RUN FROM THE REPO ROOT.
import os, sys, subprocess, py_compile
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
parts = [open(f'{SP}/ch15_part{n}.py', encoding='utf-8').read() for n in (1, 2, 3, 4)]
p5 = f'{SP}/ch15_part5.py'
tail = open(p5, encoding='utf-8').read() if os.path.exists(p5) and '--empty' not in sys.argv else "\n\nCASES = []\n"
src = ''.join(parts) + tail
if len(sys.argv) > 2 and sys.argv[1] == '--guard':
    src = src.replace("assert GUARDED == 0, (\"the guard counted %d expectations, the tripwire holds 0\" % GUARDED)", "assert GUARDED == %s, (\"the guard counted %%d expectations, the tripwire holds %s\" %% GUARDED)" % (sys.argv[2], sys.argv[2]))
    src = src.replace("   # RETYPED after the generator (the cells' asks summed)", "   # the cells' asks summed by the generator before the first graded run (%s)" % (sys.argv[3] if len(sys.argv) > 3 else ''))
out = f'{ROOT}/World/step9/cold_run_release_firstborn.py'
open(out, 'w', encoding='utf-8').write(src); py_compile.compile(out, doraise=True)
print('assembled', out, len(src), 'bytes; parts', [len(p) for p in parts], 'tail', len(tail))
