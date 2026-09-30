import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29): the assembler, the fast checker, the ask checker, the cases generator, the runner chain, the tape chain, the tape wrap, the gates shell and
# THE SCAN CENSUS DERIVED from 20b's copies in the forms folder by asserted substitutions (ch32 -> ch33, 20b -> 21b, song_charge_nebo -> blessing_of_moses, SIX typed
# parts and the eleven cells, DN -> DO, eleven own-day lines in two forms and NO MARKER, the twenty-eight names read from the spec; the portable header made a scratch script's ROOT from git).
# derive_ch32_shells.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch33b_spec as S
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
OWN28 = list(S.NEW_EFFECTS); assert len(OWN28) == 28 and len(set(OWN28)) == 28
CELLS16 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 RB"'
CELLS11 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 RB"'
out = {}
a = strip_hdr(open(f'{FD}/ch32_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_song_charge_nebo.py', 'cold_run_blessing_of_moses.py'); a = sub(a, 'ch32', 'ch33'); a = sub0(a, "ch29_assemble.py's form", "ch32_assemble.py's form")
out['ch33_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch32_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch32', 'ch33'); f = sub0(f, "ch29_fastcheck.py's form", "ch32_fastcheck.py's form")
out['ch33_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch32_askcheck.py', encoding='utf-8').read())
k = sub(k, 'ch32', 'ch33')
out['ch33_askcheck.py'] = k
g = strip_hdr(open(f'{FD}/ch32_cases_gen.py', encoding='utf-8').read())
g = sub(g, 'cold_run_song_charge_nebo', 'cold_run_blessing_of_moses'); g = sub(g, 'p32 = ', 'p33 = ', 1); g = sub(g, "p32.split(", "p33.split(", 1)
i = g.index('CELLS = ['); j = g.index('\n', i); g = g[:i] + 'CELLS = ' + repr([('F%d' % n, S.CELLS['F%d' % n]) for n in range(1, 12)] + [('RB', 'the_readback')]) + g[j:]
i = g.index('VERSES = {'); j = g.index('\n', i)
VERSES = {'F%d' % (n + 1): 'Deut ' + l[2] for n, l in enumerate(S.LINES)}; VERSES['RB'] = 'Deut 33:1-29 (the readback table)'
g = g[:i] + 'VERSES = ' + repr(VERSES) + g[j:]
g = sub(g, 'ch32', 'ch33')
g = sub0(g, "ch29_cases_gen.py's form over one chapter (sixteen cells in three typed parts)", "ch32_cases_gen.py's form over one chapter (eleven cells in three typed parts)"); g = sub0(g, "the twenty-six Mishnah and Tosefta rows", "the fifteen Mishnah and Tosefta rows")
g = g.replace("the forty-two on their ledgers", "the twenty-eight on their ledgers")
out['ch33_cases_gen.py'] = g
r = open(f'{FD}/ch32_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '20b', '21b'); r = sub(r, 'ch32', 'ch33'); r = sub(r, 'cold_run_song_charge_nebo.py', 'cold_run_blessing_of_moses.py', 1); r = sub0(r, "19b's form (ch29_runner_chain.sh)", "20b's form (ch32_runner_chain.sh)")
r = sub(r, CELLS16, CELLS11, 1)
out['ch33_runner_chain.sh'] = r
t = open(f'{FD}/ch32_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '20b', '21b'); t = sub(t, 'ch32', 'ch33'); t = sub(t, '"song_charge_nebo\\|covenant_return_charge "', '"blessing_of_moses\\|song_charge_nebo "', 1); t = sub(t, 'CHECKPOINT DN', 'CHECKPOINT DO', 1)
t = sub0(t, 'sixteen own-day lines in three forms and NO MARKER', 'eleven own-day lines in two forms and NO MARKER'); t = sub0(t, "19b's form (ch29_tape_chain.sh)", "20b's form (ch32_tape_chain.sh)"); t = sub(t, 'DN1-DN5', 'DO1-DO5')
out['ch33_tape_chain.sh'] = t
w = open(f'{FD}/ch32_tape_wrap.sh', encoding='utf-8').read()
w = sub(w, '20b', '21b'); w = sub(w, 'ch32', 'ch33'); w = sub(w, 'cold_run_song_charge_nebo.py', 'cold_run_blessing_of_moses.py', 1); w = sub0(w, "ch29_tape_wrap.sh's form", "ch32_tape_wrap.sh's form")
w = sub(w, CELLS16, CELLS11, 1); w = sub(w, 'DN1-DN5', 'DO1-DO5')
out['ch33_tape_wrap.sh'] = w
gs = open(f'{FD}/ch32b_gates.sh', encoding='utf-8').read()
gs = sub(gs, '20b', '21b'); gs = sub(gs, 'ch32', 'ch33'); gs = sub0(gs, "ch29b_gates.sh's form", "ch32b_gates.sh's form")
out['ch33b_gates.sh'] = gs
sc = strip_hdr(open(f'{FD}/ch32_scan_census.py', encoding='utf-8').read())
i = sc.index("NEW = {'"); j = sc.index('}\n', i) + 2
sc = sc[:i] + 'NEW = ' + repr(set(OWN28)) + '\n' + sc[j:]
sc = sub0(sc, "THE DEUTERONOMY WALK 20b (2026-09-28): THE SCAN CENSUS EXTENDED", "THE DEUTERONOMY WALK 21b (2026-09-29): THE SCAN CENSUS EXTENDED")
sc = sub0(sc, "ch29_scan_census.py's form over the forty-two names on three ledgers", "ch32_scan_census.py's form over the twenty-eight names on twelve ledgers"); sc = sub(sc, "chapter 32 present:", "chapter 33 present:", 1)
sc = sub0(sc, "(kept at 20b)", "(kept at 21b)")
out['ch33_scan_census.py'] = sc
for name, text in out.items():
    left = [l[:140] for l in text.split('\n') if "'s form" not in l and ('ch32_part' in l or 'ch32b_gates' in l or re.search(r"\b20b B\b", l) or 'cold_run_song_charge_nebo.py' in l)]   # the form citations name 20b's files on purpose
    assert not left, (name, left[:3])
    rest = [l[:120] for l in text.split('\n') if 'ch32' in l or '20b' in l or 'song_charge_nebo' in l]
    print("%s: %d bytes; the lines still naming ch32 / 20b / song_charge_nebo (the form citations, the tape's grep):" % (name, len(text)), rest[:6])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch33_assemble.py', 'ch33_fastcheck.py', 'ch33_askcheck.py', 'ch33_cases_gen.py', 'ch33_scan_census.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the five python files compile; the census NEW set', len(re.search(r"NEW = (\{.*?\})\n", out['ch33_scan_census.py'], re.S).group(1).split("', '")), 'names')
