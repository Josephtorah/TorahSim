#!/usr/bin/env python3
"""shelf_seg.py — print whole segments from a Talmud work on the local shelf by STANDARD address (daf = index//2 + 1: the export's
index 0 is folio 1a — measured 2026-09-09). Usage: python3 shelf_seg.py <Work_Dir> <daf><a|b>:<seg>[-<seg>] ..."""
import json, re, sys
work = sys.argv[1]
d = json.load(open('<repo-old>/Data/sefaria_export/%s/en.json' % work, encoding='utf-8'))
text = d['text']
strip = lambda s: re.sub(r'<[^>]+>', '', s)
for a in sys.argv[2:]:
    m = re.match(r'(\d+)([ab]):(\d+)(?:-(\d+))?$', a)
    daf, side, s1, s2 = int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
    i = (daf - 1) * 2 + (0 if side == 'a' else 1)
    for s in range(s1, s2 + 1):
        print('%s %d%s:%d | %s\n' % (work.replace('_', ' '), daf, side, s, strip(text[i][s - 1])))
