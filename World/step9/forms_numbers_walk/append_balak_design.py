#!/usr/bin/env python3
# THE NUMBERS WALK 7b: append the design section to World/step9/NUMBERS_WALK.md after sitting 7's NEXT paragraph (the anchor asserted).
import os
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
p = f'{ROOT}/World/step9/NUMBERS_WALK.md'
text = open(p, encoding='utf-8').read()
anchor = "chapter 26 (the second census), never the next reading first.\n"
assert text.endswith(anchor), repr(text[-200:])
assert '## Sitting 7b — THE COMPILE OF BALAK' not in text
design = open(f'{SCR}/balak_design.md', encoding='utf-8').read()
assert design.startswith('\n## Sitting 7b — THE COMPILE OF BALAK')
open(p, 'w', encoding='utf-8').write(text + design)
print('appended', len(design), 'chars to', p)
