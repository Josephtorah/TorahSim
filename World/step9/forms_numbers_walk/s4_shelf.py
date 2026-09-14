#!/usr/bin/env python3
"""s4_shelf.py — O8 S4: the shelf census by script — every row of Bereshit Rabbah and of the local Babylonian tractates that
quotes a verse of Genesis 33-37, 39-47, 50:15-26 (a run of four or more consecutive consonantal words of the verse found in
the row), printed per verse with the row's address and its first 120 characters. Located, never recited."""
import json, re, sqlite3, glob, os, collections
R = '<repo-old>'; S = '<scratch>/'
def bare(s): return re.sub(r'[֑-ׇ]', '', s or '')
def clean(s): return re.sub(r'<[^>]+>', '', s)
t = sqlite3.connect('file:%s/elijah_docket/tanakh.sqlite?mode=ro' % R, uri=True)
verses = []
for ch in list(range(33, 38)) + list(range(39, 48)) + [50]:
    for vs, vid in t.execute("select verse, id from verses where book='Gen' and chapter=? order by verse", (ch,)):
        if ch == 50 and vs < 15: continue
        ws = [bare(h).replace('/', '') for (h,) in t.execute('select he from words where verse_id=? order by idx', (vid,))]
        verses.append((ch, vs, ws))
# the index: every 4-word run of every verse -> the verse
runs = {}
for ch, vs, ws in verses:
    for i in range(len(ws) - 3):
        runs.setdefault(' '.join(ws[i:i+4]), set()).add((ch, vs))
def scan(text):
    hits = set(); ws = bare(clean(text)).replace('־', ' ').split()
    for i in range(len(ws) - 3):
        k = ' '.join(ws[i:i+4])
        if k in runs: hits |= runs[k]
    return hits
out = collections.defaultdict(list)
BR = json.load(open(R + '/Data/bereshit_rabbah_he.json', encoding='utf-8'))
BRt = BR['text'] if isinstance(BR, dict) and 'text' in BR else BR
for pi, par in enumerate(BRt):
    for ri, row in enumerate(par):
        if not isinstance(row, str): continue
        for h in scan(row): out[h].append(('Bereshit Rabbah %d:%d' % (pi + 1, ri + 1), clean(row)[:120]))
n_bav = 0
for f in sorted(glob.glob(R + '/Data/bavli_*_he.json')):
    tr = os.path.basename(f)[6:-8]
    J = json.load(open(f, encoding='utf-8')); T = J['text'] if isinstance(J, dict) and 'text' in J else J
    for di, daf in enumerate(T):
        for ri, row in enumerate(daf):
            if not isinstance(row, str): continue
            for h in scan(row):
                out[h].append(('%s %d%s:%d' % (tr, di // 2 + 1, 'ab'[di % 2], ri + 1), clean(row)[:120])); n_bav += 1
ms = 0
for f in sorted(glob.glob(R + '/Data/mishnah_*_he.json')):
    tr = os.path.basename(f)[8:-8]
    J = json.load(open(f, encoding='utf-8')); T = J['text'] if isinstance(J, dict) and 'text' in J else J
    for ci, chp in enumerate(T):
        for mi, row in enumerate(chp):
            if not isinstance(row, str): continue
            for h in scan(row): out[h].append(('Mishnah %s %d:%d' % (tr, ci + 1, mi + 1), clean(row)[:120])); ms += 1
lines = []
for ch, vs, ws in verses:
    hs = out.get((ch, vs), [])
    if hs:
        lines.append('Gen %d:%d  (%d rows)' % (ch, vs, len(hs)))
        for a, s in hs[:14]: lines.append('    %s — %s' % (a, s))
open(S + 'o8_s4_shelf.txt', 'w', encoding='utf-8').write('\n'.join(lines))
print('verses with shelf rows: %d of %d; rows: BR+Bavli+Mishnah = %d (Bavli hits %d, Mishnah hits %d)' % (sum(1 for v in verses if out.get((v[0], v[1]))), len(verses), sum(len(v) for v in out.values()), n_bav, ms))
