import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — THE TAIL: Q47's LAST MOVED ELEMENT, hidden inside an expression the ast walker leaves alone — the ninety-one writes of chapters 26-28
# asserted ONE each (`tuple((1, v_) for _, v_ in W91)`); became_the_lords_people_this_day (27:9's) REUSED at 29:12 by this compile now holds TWO entries — the chain's probe print
# (the killed second pass, 47/48) shows (2, 'Deut 27:9') at its seat. RETYPED FROM THAT PRINT: the generator's count reads 2 for that one name. RUN FROM THE REPO ROOT.
import re, ast, subprocess, sys
ROOT = _ROOT
F = f'{ROOT}/World/step9/readback_probes.py'; src = open(F, encoding='utf-8').read()
PR = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r"FAIL Q47 .* = (\(.*\))\s*$", PR, re.M); assert m, 'Q47 not in the print'
got = ast.literal_eval(m.group(1)); w91 = got[6]; two = [(k, p) for k, p in enumerate(w91) if p[0] != 1]
print('the ninety-one writes whose count is not one, from the print:', two); assert two == [(20, (2, 'Deut 27:9'))], two
OLD = "return got == (list(OWN), True, 0, 173, [(40, 11, 1)], 0, tuple((1, v_) for _, v_ in W91), "
NEW = "return got == (list(OWN), True, 0, 173, [(40, 11, 1)], 0, tuple((2 if eff_ == 'became_the_lords_people_this_day' else 1, v_) for eff_, v_ in W91), "
assert src.count(OLD) == 1, src.count(OLD)
NOTE = "    # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): became_the_lords_people_this_day TWO entries — 27:9's and 29:12's REUSE by this compile (the print's (2, 'Deut 27:9') at the twenty-first seat); the ninety others one each; hidden inside the generator, found by the chain's probe pass\n"
i = src.index(OLD); j = src.rfind('\n', 0, i) + 1
new = src[:j] + NOTE + src[j:i] + NEW + src[i + len(OLD):]
ast.parse(new); open(F, 'w', encoding='utf-8').write(new); print('q47 retyped: the one reused name counted 2')
