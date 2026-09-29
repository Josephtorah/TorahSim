import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): the assembler, the fast checker, the ask checker, the cases generator, the runner chain, the tape chain, the tape wrap, the gates shell and
# THE SCAN CENSUS DERIVED from 19b's copies in the forms folder by asserted substitutions (ch29 -> ch32, 19b -> 20b, covenant_return_charge -> song_charge_nebo, SIX typed
# parts and the sixteen cells, DM -> DN, sixteen own-day lines in three forms and NO MARKER, the forty-two names read from the spec; the portable header made a scratch script's ROOT from git).
# derive_ch29_shells.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch32b_spec as S
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:70], c, n); return text.replace(old, new)
def sub0(text, old, new):   # a tolerant substitution — the absent anchor printed, not fatal (the form citations differ file to file)
    c = text.count(old)
    if not c: print('  (anchor absent, skipped): %r' % old[:70])
    return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"\Aimport os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1)
    t = sub(t, "ROOT = _ROOT", GIT, 1)
    if 'import subprocess' not in t.split('\n', 12)[0:12].__str__(): t = t.replace('\nimport ', '\nimport subprocess, ', 1)
    return t
OWN42 = list(S.NEW_EFFECTS); assert len(OWN42) == 42 and len(set(OWN42)) == 42
CELLS15 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 RB"'
CELLS16 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 RB"'
out = {}
a = strip_hdr(open(f'{FD}/ch29_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_covenant_return_charge.py', 'cold_run_song_charge_nebo.py'); a = sub(a, 'ch29', 'ch32'); a = sub0(a, "ch26_assemble.py's form", "ch29_assemble.py's form")
out['ch32_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch29_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch29', 'ch32'); f = sub0(f, "ch26_fastcheck.py's form", "ch29_fastcheck.py's form")
out['ch32_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch29_askcheck.py', encoding='utf-8').read())
k = sub(k, 'ch29', 'ch32')
out['ch32_askcheck.py'] = k
g = strip_hdr(open(f'{FD}/ch29_cases_gen.py', encoding='utf-8').read())
g = sub(g, 'cold_run_covenant_return_charge', 'cold_run_song_charge_nebo'); g = sub(g, 'p29 = ', 'p32 = ', 1); g = sub(g, "p29.split(", "p32.split(", 1)
i = g.index('CELLS = ['); j = g.index('\n', i); g = g[:i] + 'CELLS = ' + repr([('F%d' % n, S.CELLS['F%d' % n]) for n in range(1, 17)] + [('RB', 'the_readback')]) + g[j:]
i = g.index('VERSES = {'); j = g.index('\n', i)
VERSES = {'F%d' % (n + 1): 'Deut ' + l[2] for n, l in enumerate(S.LINES)}; VERSES['RB'] = 'Deut 32:1-52 (the readback table)'
g = g[:i] + 'VERSES = ' + repr(VERSES) + g[j:]
g = sub(g, 'ch29', 'ch32')
g = sub0(g, "ch26_cases_gen.py's form over three chapters (fifteen cells in three typed parts)", "ch29_cases_gen.py's form over one chapter (sixteen cells in three typed parts)"); g = sub0(g, "the seven Mishnah and Tosefta rows", "the twenty-six Mishnah and Tosefta rows")
g = g.replace("the fifty-nine on their ledgers", "the forty-two on their ledgers")
out['ch32_cases_gen.py'] = g
r = open(f'{FD}/ch29_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '19b', '20b'); r = sub(r, 'ch29', 'ch32'); r = sub(r, 'cold_run_covenant_return_charge.py', 'cold_run_song_charge_nebo.py', 1); r = sub0(r, "18b's form (ch26_runner_chain.sh)", "19b's form (ch29_runner_chain.sh)")
r = sub(r, CELLS15, CELLS16, 1)
out['ch32_runner_chain.sh'] = r
t = open(f'{FD}/ch29_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '19b', '20b'); t = sub(t, 'ch29', 'ch32'); t = sub(t, '"covenant_return_charge\\|firstfruits_ebal_curses "', '"song_charge_nebo\\|covenant_return_charge "', 1); t = sub(t, 'CHECKPOINT DM', 'CHECKPOINT DN', 1)
t = sub0(t, 'twenty own-day lines in three forms and ONE MARKER', 'sixteen own-day lines in three forms and NO MARKER'); t = sub0(t, "18b's form (ch26_tape_chain.sh)", "19b's form (ch29_tape_chain.sh)"); t = sub(t, 'DM1-DM5', 'DN1-DN5')
t = sub0(t, 'the stitcher (ONE marker at 31:1', 'the stitcher (NO marker'); t = t.replace('(ONE marker at 31:1; ', '(NO marker; ')
out['ch32_tape_chain.sh'] = t
w = open(f'{FD}/ch29_tape_wrap.sh', encoding='utf-8').read()
w = sub(w, '19b', '20b'); w = sub(w, 'ch29', 'ch32'); w = sub(w, 'cold_run_covenant_return_charge.py', 'cold_run_song_charge_nebo.py', 1); w = sub0(w, "ch26_tape_wrap.sh's form", "ch29_tape_wrap.sh's form")
w = sub(w, CELLS15, CELLS16, 1); w = sub(w, 'DM1-DM5', 'DN1-DN5')
out['ch32_tape_wrap.sh'] = w
gs = open(f'{FD}/ch29b_gates.sh', encoding='utf-8').read()
gs = sub(gs, '19b', '20b'); gs = sub(gs, 'ch29', 'ch32'); gs = sub0(gs, "ch26b_gates.sh's form", "ch29b_gates.sh's form")
out['ch32b_gates.sh'] = gs
sc = strip_hdr(open(f'{FD}/ch29_scan_census.py', encoding='utf-8').read())
i = sc.index("NEW = {'"); j = sc.index('}\n', i) + 2
sc = sc[:i] + 'NEW = ' + repr(set(OWN42)) + '\n' + sc[j:]
sc = sub0(sc, "THE DEUTERONOMY WALK 19b (2026-09-27): THE SCAN CENSUS EXTENDED", "THE DEUTERONOMY WALK 20b (2026-09-28): THE SCAN CENSUS EXTENDED")
sc = sub0(sc, "ch26_scan_census.py's form over the fifty-nine names on four ledgers", "ch29_scan_census.py's form over the forty-two names on three ledgers"); sc = sub(sc, "chapters 29-31 present:", "chapter 32 present:", 1)
sc = sub0(sc, "(kept at 19b)", "(kept at 20b)")
out['ch32_scan_census.py'] = sc
for name, text in out.items():
    left = [l[:140] for l in text.split('\n') if "'s form" not in l and ('ch29_part' in l or 'ch29b_gates' in l or re.search(r"\b19b B\b", l) or 'cold_run_covenant_return_charge.py' in l)]   # the form citations name 19b's files on purpose
    assert not left, (name, left[:3])
    rest = [l[:120] for l in text.split('\n') if 'ch29' in l or '19b' in l or 'covenant_return_charge' in l]
    print("%s: %d bytes; the lines still naming ch29 / 19b / covenant_return_charge (the form citations, the tape's grep):" % (name, len(text)), rest[:6])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch32_assemble.py', 'ch32_fastcheck.py', 'ch32_askcheck.py', 'ch32_cases_gen.py', 'ch32_scan_census.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the five python files compile; the census NEW set', len(re.search(r"NEW = (\{.*?\})\n", out['ch32_scan_census.py'], re.S).group(1).split("', '")), 'names')
