#!/usr/bin/env python3
"""shelf_grep.py — search one work's English export on the local shelf; print matching segments with their address.
Usage: python3 shelf_grep.py <Work_Dir> <regex> [maxchars]   (Talmud index 0 = 2a; midrash = chapter:paragraph)"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import json, re, sys, os
work, rx = sys.argv[1], re.compile(sys.argv[2], re.I)
maxc = int(sys.argv[3]) if len(sys.argv) > 3 else 420
p = (_ROOT + '/Data/sefaria_export/%s/en.json') % work
d = json.load(open(p, encoding='utf-8'))
text = d['text'] if isinstance(d, dict) else d
TALMUD = isinstance(d, dict) and 'Talmud' in str(d.get('categories', '')) and 'Jerusalem' not in work
def addr(path):
    if TALMUD and len(path) >= 2:
        i = path[0]; return '%s %d%s:%d' % (work.replace('_', ' '), i // 2 + 1, 'ab'[i % 2], path[1] + 1)
    return '%s %s' % (work.replace('_', ' '), ':'.join(str(x + 1) for x in path))
strip = lambda s: re.sub(r'<[^>]+>', '', s)
n = 0
def walk(x, path):
    global n
    if isinstance(x, list):
        for i, v in enumerate(x): walk(v, path + [i])
    elif isinstance(x, str):
        s = strip(x)
        if rx.search(s):
            n += 1; m = rx.search(s); a = max(0, m.start() - 160)
            print('%s | %s' % (addr(path), s[a:a + maxc].replace('\n', ' ')))
walk(text, [])
print('-- %d matches in %s (talmud=%s)' % (n, work, TALMUD))
