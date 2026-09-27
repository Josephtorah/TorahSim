import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (2026-09-24): the assembler, the fast checker, the ask checker and the three chain shells DERIVED from 14b's copies in the forms folder by
# asserted substitutions (ch16 -> ch17, 14b -> 15b, festivals_judges -> courts_prophet, FOUR typed parts and the nine cells, DH -> DI, eight own-day lines; the portable
# header made a scratch script's ROOT from git). derive_ch16_shells.py's form. RUN FROM THE REPO ROOT.
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
a = strip_hdr(open(f'{FD}/ch16_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_festivals_judges.py', 'cold_run_courts_prophet.py'); a = sub(a, 'ch16', 'ch17'); a = sub(a, "ch15_assemble.py's form", "ch16_assemble.py's form")
a = sub(a, "for n in (1, 2, 3)]", "for n in (1, 2, 3, 4)]", 1)   # the lean runner over two chapters: FOUR typed parts (the cells of chapter 17; the cells of chapter 18; the readback, the data, the daemon and the narrative) + the generated cases
out['ch17_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch16_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch16', 'ch17'); f = sub(f, "ch15_fastcheck.py's form", "ch16_fastcheck.py's form")
out['ch17_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch16_askcheck.py', encoding='utf-8').read())
k = sub(k, "['ch16_part2.py', 'ch16_part3.py']", "['ch17_part2.py', 'ch17_part3.py', 'ch17_part4.py']", 1); k = sub(k, 'ch16', 'ch17')
out['ch17_askcheck.py'] = k
r = open(f'{FD}/ch16_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '14b', '15b'); r = sub(r, 'ch16', 'ch17'); r = sub(r, 'cold_run_festivals_judges.py', 'cold_run_courts_prophet.py', 1); r = sub(r, "13b's form (ch15_runner_chain.sh)", "14b's form (ch16_runner_chain.sh)", 1)
r = sub(r, '"F1 F2 F3 F4 F5 F6 RB"', '"F1 F2 F3 F4 F5 F6 F7 F8 RB"', 1)
out['ch17_runner_chain.sh'] = r
t = open(f'{FD}/ch16_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '14b', '15b'); t = sub(t, 'ch16', 'ch17'); t = sub(t, '"festivals_judges\\|release_firstborn "', '"courts_prophet\\|festivals_judges "', 1); t = sub(t, 'DH1-DH5; one retype', 'DI1-DI5; the stale literals as read', 1); t = sub(t, 'CHECKPOINT DH', 'CHECKPOINT DI', 1)
t = sub(t, 'five own-day lines', 'eight own-day lines', 1); t = sub(t, "the one stale literal retyped (DB7)", "the stale literals retyped as the grep reads them", 1); t = sub(t, "13b's form (ch15_tape_chain.sh)", "14b's form (ch16_tape_chain.sh)", 1)
t = sub(t, 'DH1-DH5', 'DI1-DI5')
out['ch17_tape_chain.sh'] = t
b = open(f'{FD}/ch16_build_chain.sh', encoding='utf-8').read()
b = sub(b, '14b', '15b'); b = sub(b, 'ch16', 'ch17')
b = sub(b, "derive the runner's part 1, fourth (the holes' pattern anchored at the effect name — two values naming the asherah had matched)", "derive the runner's part 1 (the helpers from the chapter-16 runner, the ink blocks from ch17_ink.py, the scans, the callees' facts)", 1)
b = sub(b, "the fast checker, parts 1-3 (ch17_fastcheck.py)", "the fast checker, parts 1-4 (ch17_fastcheck.py)", 1)
b = sub(b, "'fails 0, part2 fails 0, part3 fails 0'", "'fails 0, part2 fails 0, part3 fails 0, part4 fails 0'", 1)
b = sub(b, "every ask called (ch17_askcheck.py — the six cells and the table with the DATA rows)", "every ask called (ch17_askcheck.py — the eight cells and the table with the DATA rows)", 1)
b = sub(b, "ch17_askcheck.py ch17_part2.py ch17_part3.py", "ch17_askcheck.py ch17_part2.py ch17_part3.py ch17_part4.py", 1)
out['ch17_build_chain.sh'] = b
for name, text in out.items():
    clean = re.sub(r"ch16_\w+\.(?:py|sh)", '', text)   # the form citations name 14b's files on purpose
    assert 'ch16' not in clean and 'festivals_judges.py' not in clean and '14b' not in re.sub(r"14b's form", '', clean), (name, [l for l in clean.split('\n') if 'ch16' in l or '14b' in l][:3])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch17_assemble.py', 'ch17_fastcheck.py', 'ch17_askcheck.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the three python files compile')
