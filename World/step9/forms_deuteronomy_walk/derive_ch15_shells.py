#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b (2026-09-23): the assembler, the fast checker and the two chain shells DERIVED from 12b's copies in the forms folder by asserted
# substitutions (ch14 -> ch15, 12b -> 13b, food_tithe -> release_firstborn, the seven cells, DF -> DG, the four stale literals; the portable header made a scratch
# script's ROOT from git). derive_ch14_shells.py's form. RUN FROM THE REPO ROOT.
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
a = strip_hdr(open(f'{FD}/ch14_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_food_tithe.py', 'cold_run_release_firstborn.py'); a = sub(a, 'ch14', 'ch15'); a = sub(a, "ch13_assemble.py's form", "ch14_assemble.py's form")
out['ch15_assemble.py'] = a
f = open(f'{FD}/ch14_fastcheck.py', encoding='utf-8').read()
f = sub(f, "ROOT = _ROOT", GIT, 1) if '_ROOT = _os.path.normpath' not in f else strip_hdr(f)
f = sub(f, 'ch14', 'ch15'); f = sub(f, "ch13_fastcheck.py's form", "ch14_fastcheck.py's form")
out['ch15_fastcheck.py'] = f
r = open(f'{FD}/ch14_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '12b', '13b'); r = sub(r, 'ch14', 'ch15'); r = sub(r, 'cold_run_food_tithe.py', 'cold_run_release_firstborn.py', 1); r = sub(r, "11b's form (ch13_runner_chain.sh)", "12b's form (ch14_runner_chain.sh)", 1)
out['ch15_runner_chain.sh'] = r
t = open(f'{FD}/ch14_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '12b', '13b'); t = sub(t, 'ch14', 'ch15'); t = sub(t, '"food_tithe\\|seducers "', '"release_firstborn\\|food_tithe "', 1); t = sub(t, 'DF1-DF9; one retype', 'DG1-DG9; four retypes', 1); t = sub(t, 'CHECKPOINT DF', 'CHECKPOINT DG', 1)
t = sub(t, 'five own-day lines', 'four own-day lines', 1); t = sub(t, "the one stale literal retyped (DD2)", "the four stale literals retyped (CQ6, DC6, DD2, DF5)", 1); t = sub(t, "11b's form (ch13_tape_chain.sh)", "12b's form (ch14_tape_chain.sh)", 1)
out['ch15_tape_chain.sh'] = t
for name, text in out.items():
    clean = re.sub(r"ch14_\w+\.(?:py|sh)", '', text)   # the form citations name 12b's files on purpose
    assert 'ch14' not in clean and 'food_tithe.py' not in clean, (name, [l for l in clean.split('\n') if 'ch14' in l][:2])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
py_compile.compile(f'{SP}/ch15_assemble.py', doraise=True); py_compile.compile(f'{SP}/ch15_fastcheck.py', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the two python files compile')
