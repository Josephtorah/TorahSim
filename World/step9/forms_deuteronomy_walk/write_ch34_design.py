import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22 (LEAN, 2026-09-30): the design section appended to the map from ch34_design.txt (write_ch33_design.py's form) — the newest section; no Hebrew script in the map (its lint 0); the header unique. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT; SP = os.path.dirname(os.path.abspath(__file__))
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
d = open(f'{SP}/ch34_design.txt', encoding='utf-8').read(); m = open(MAP, encoding='utf-8').read()
assert not re.search('[' + chr(0x5d0) + '-' + chr(0x5ea) + ']', d), 'no Hebrew script in the map'
assert '## Sitting 22 — CHAPTER 34' not in m and m.rstrip('\n').endswith('|') and m.rfind('## Sitting 21b — CHAPTER 33 — AS BUILT — LEAN') > 0 and m.rfind('## Sitting 21b — CHAPTER 33 — AS BUILT — LEAN') > m.rfind('## Sitting 21b — THE COMPILE OF CHAPTER 33')
assert os.path.expanduser('~') not in d and SP not in d
assert d.startswith('\n\n## Sitting 22 — CHAPTER 34') and d.endswith('\n')
open(MAP, 'w', encoding='utf-8').write(m.rstrip('\n') + d)
out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', MAP], capture_output=True, text=True).stdout.strip().split('\n')[-1]
print('the design appended:', len(d.encode()), 'bytes; the map', os.path.getsize(MAP), 'bytes;', out)
