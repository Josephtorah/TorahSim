import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 3b (2026-09-16): THE RETYPES THE FIRST TAPE RUN READ (tape_run_ch5_1.out — 9/10, the one miss the verdicts): eight older REST
# checkpoints carry the tape's closes as a LITERAL 126 (retyped to 126 at 1b, unmoved at 2b) — CT9, CV2, CV9, CX9, CY9, CZ9, CW9, CR9 — and the charge
# to teach closed inside this sitting's daemon moves it to 127. Each retyped AS OF this sitting with the reason in the text; every replacement
# anchored on the checkpoint's own name (one cp per line); the file asserted to compile after. A miss is evidence, never a retype — read first
# (it was: the eight DIVERGE lines all say 126 declared, 127 computed).
import re, subprocess, py_compile
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
NOTE = "; closes 127 since THE DEUTERONOMY WALK 3b (2026-09-16) — the charge to teach closed inside law_covenant_at_horeb by the prior run"
FIX = [('CT9', r"', \('the_altar_of_moses', True, True, 319, 126\)", "%s', ('the_altar_of_moses', True, True, 319, 127)" % NOTE),
       ('CV2', r"', \(18, 'begin_to_possess_sihons_land', 96, 126\)", "%s', (18, 'begin_to_possess_sihons_land', 96, 127)" % NOTE),
       ('CV9', r"', \(319, True, 126\)", "%s', (319, True, 127)" % NOTE),
       ('CX9', r"', \(319, 126, True\)", "%s', (319, 127, True)" % NOTE),
       ('CY9', r"', \(319, 126, True\)", "%s', (319, 127, True)" % NOTE),
       ('CZ9', r"', \(319, 126, True\)", "%s', (319, 127, True)" % NOTE),
       ('CW9', r"', \(319, 126, True\)", "%s', (319, 127, True)" % NOTE),
       ('CR9', r"', \(319, 126, True, 148\)", "%s', (319, 127, True, 148)" % NOTE)]
for name, lit, new in FIX:
    pat = re.compile(r"(cp\('%s [^\n]*?)%s" % (name, lit))
    s, n = pat.subn(lambda m: m.group(1) + new, s, count=1)
    assert n == 1, (name, n)
open(P, 'w', encoding='utf-8').write(s)
py_compile.compile(P, doraise=True)
print('retyped: CT9, CV2, CV9, CX9, CY9, CZ9, CW9, CR9 — closes 126 -> 127 as of 3b; compiles')
