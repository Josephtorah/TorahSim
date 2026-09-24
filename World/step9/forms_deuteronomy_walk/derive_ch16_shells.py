import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (2026-09-23): the assembler, the fast checker, the ask checker and the two chain shells DERIVED from 13b's copies in the forms folder by
# asserted substitutions (ch15 -> ch16, 13b -> 14b, release_firstborn -> festivals_judges, the six cells, DG -> DH, the one stale literal; the portable header made a
# scratch script's ROOT from git). derive_ch15_shells.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:60], c, n); return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"^import os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1, flags=re.M)
    return sub(t, "ROOT = _ROOT", GIT, 1)
out = {}
a = strip_hdr(open(f'{FD}/ch15_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_release_firstborn.py', 'cold_run_festivals_judges.py'); a = sub(a, 'ch15', 'ch16'); a = sub(a, "ch14_assemble.py's form", "ch15_assemble.py's form")
a = sub(a, "for n in (1, 2, 3, 4)]", "for n in (1, 2, 3)]", 1)   # the lean runner: three typed parts (the cells; the readback, the data, the daemon and the narrative) + the generated cases
out['ch16_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch15_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch15', 'ch16'); f = sub(f, "ch14_fastcheck.py's form", "ch15_fastcheck.py's form")
out['ch16_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch15_askcheck.py', encoding='utf-8').read())
k = sub(k, 'ch15', 'ch16')
out['ch16_askcheck.py'] = k
r = open(f'{FD}/ch15_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '13b', '14b'); r = sub(r, 'ch15', 'ch16'); r = sub(r, 'cold_run_release_firstborn.py', 'cold_run_festivals_judges.py', 1); r = sub(r, "12b's form (ch14_runner_chain.sh)", "13b's form (ch15_runner_chain.sh)", 1)
r = sub(r, '"F1 F2 F3 F4 F5 F6 F7 RB"', '"F1 F2 F3 F4 F5 F6 RB"', 1)
out['ch16_runner_chain.sh'] = r
t = open(f'{FD}/ch15_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '13b', '14b'); t = sub(t, 'ch15', 'ch16'); t = sub(t, '"release_firstborn\\|food_tithe "', '"festivals_judges\\|release_firstborn "', 1); t = sub(t, 'DG1-DG9; four retypes', 'DH1-DH5; one retype', 1); t = sub(t, 'CHECKPOINT DG', 'CHECKPOINT DH', 1)
t = sub(t, 'four own-day lines', 'five own-day lines', 1); t = sub(t, "the four stale literals retyped (CQ6, DC6, DD2, DF5)", "the one stale literal retyped (DB7)", 1); t = sub(t, "12b's form (ch14_tape_chain.sh)", "13b's form (ch15_tape_chain.sh)", 1)
t = sub(t, 'DE1-DE9', 'DH1-DH5', 1)
out['ch16_tape_chain.sh'] = t
for name, text in out.items():
    clean = re.sub(r"ch15_\w+\.(?:py|sh)", '', text)   # the form citations name 13b's files on purpose
    assert 'ch15' not in clean and 'release_firstborn.py' not in clean, (name, [l for l in clean.split('\n') if 'ch15' in l][:2])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch16_assemble.py', 'ch16_fastcheck.py', 'ch16_askcheck.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the three python files compile')
