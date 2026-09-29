import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): THE DESIGN WRITER — assembles the three parts (ch32b_design_part1/2/3.py, the counts from ch32b_spec.py), checks the text
# (no Hebrew script — the map carries none; the gloss lint 0 on the assembled text; the header once; no home path), and with --write APPENDS it to World/step9/DEUTERONOMY_WALK.md
# after the map's newest section (sitting 20's AS BUILT), then reruns the lint on the map (0). AN APPEND BUILDS ITS WHOLE TEXT BEFORE OPENING THE FILE.
# write_ch29b_design.py's form. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SP)
import ch32b_spec as S, ch32b_design_part1 as P1, ch32b_design_part2 as P2, ch32b_design_part3 as P3
MAP = ROOT + '/World/step9/DEUTERONOMY_WALK.md'
text = P1.text(S) + '\n\n' + P2.text(S) + '\n\n' + P3.text(S) + '\n'
HEAD = '## Sitting 20b — THE COMPILE OF CHAPTER 32, THE SONG, Deuteronomy 32:1-52 — LEAN'
assert text.startswith(HEAD), text[:120]
heb = re.findall(r'[֐-׿]', text); assert not heb, ('HEBREW SCRIPT IN THE MAP TEXT', len(heb))
home = os.path.expanduser('~'); assert home not in text and SP not in text and '/Users/' not in text.replace('/Users/Shared', '')
tmp = SP + '/ch32b_design_assembled.md'; open(tmp, 'w', encoding='utf-8').write(text)
lint = subprocess.run([sys.executable, ROOT + '/logic/solo_tools/gloss_lint.py', tmp], capture_output=True, text=True)
print('assembled bytes', len(text.encode()), '| paragraphs', text.count('\n\n') + 1, '| lint rc', lint.returncode, '|', (lint.stdout + lint.stderr).strip()[-400:])
paras = [p for p in text.split('\n\n') if p.strip()]
for p in paras: print('  para', len(p), repr(p[:70]))
m = open(MAP, encoding='utf-8').read()
assert m.count(HEAD) == 0, 'the design is already in the map'
last = m.rfind('\n## '); print('the map\'s newest header:', m[last + 1:last + 90].replace('\n', ' '), '| map bytes', len(m.encode()))
if '--write' in sys.argv:
    new = m.rstrip('\n') + '\n\n' + text
    open(MAP + '.tmp', 'w', encoding='utf-8').write(new); os.replace(MAP + '.tmp', MAP)
    m2 = open(MAP, encoding='utf-8').read(); assert m2.count(HEAD) == 1
    lint2 = subprocess.run([sys.executable, ROOT + '/logic/solo_tools/gloss_lint.py', MAP], capture_output=True, text=True)
    heb2 = re.findall(r'[֐-׿]', m2)
    print('WRITTEN: map bytes', len(m2.encode()), '| the map lint rc', lint2.returncode, '|', (lint2.stdout + lint2.stderr).strip()[-300:], '| Hebrew script in the map:', len(heb2))
else:
    print('CHECK ONLY — pass --write to append')
