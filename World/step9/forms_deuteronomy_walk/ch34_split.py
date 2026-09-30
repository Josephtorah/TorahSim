import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 22 — CHAPTER 34, THE DEATH OF MOSES (LEAN, 2026-09-30): THE SPLIT BY PISKA — one piska on the chapter (357, the export's last), its rows and
# bytes counted from the export (never typed), the run plan by bytes under 90,000 a slice (sitting 21's plan, printed inline there; a script here), THE EDGES (356's last
# rows before, 357:1's opening, 357's last row and NOTHING AFTER — the export ends), the words of 34:1 sought in 356 (no tail folded), the outside rows' heads and cites.
# The piska file ch34_spine_p357.txt in the split's format (the dump's spine file carries the same rows). RUN FROM THE REPO ROOT.
import json, re, html, os, subprocess
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
HEB = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100}
def gem(s): return sum(HEB.get(ch, 0) for ch in s)
heads = {}
for p in range(1, len(he) + 1):
    m = re.match(r'\(דברים ([א-ת]+),? ([א-ת]+)(?:-[א-ת]+)?\)', clean(he[p-1][0]) if he[p-1] else '')
    heads[p] = (gem(m.group(1)), gem(m.group(2))) if m else None
CH = 34
SPINE = sorted(p for p, h in heads.items() if h and h[0] == CH)
rows = {p: len(he[p - 1]) for p in SPINE}
assert all(len(he[p - 1]) == len(en[p - 1]) for p in SPINE)
def he_cites(t): return [(b, gem(c), gem(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
files = {}
for p in SPINE:
    fn = f'{SP}/ch{CH}_spine_p{p}.txt'
    with open(fn, 'w', encoding='utf-8') as f:
        for r in range(len(he[p - 1])): f.write(f'--- {p}:{r + 1} (head {heads[p]})\nHE: {clean(he[p - 1][r])}\nEN: {clean(en[p - 1][r])}\n')
    files[p] = os.path.getsize(fn)
print('spine piskaot', SPINE[0], '-', SPINE[-1], len(SPINE), '| rows per piska', rows, '| totals', {CH: sum(rows.values())}, sum(rows.values()))
print('bytes per piska file', files, '| total', sum(files.values()))
plan, cur, cb, cn = [], [], 0, 0
for p in SPINE:
    if cur and cb + files[p] > 90000: plan.append(((cur[0], cur[-1]), cn, cb)); cur, cb, cn = [], 0, 0
    cur.append(p); cb += files[p]; cn += 1
plan.append(((cur[0], cur[-1]), cn, cb))
print('the run plan under 90000 bytes a slice:', plan, '| slices', len(plan))
def HB(p, r): return plain(clean(he[p - 1][r - 1]))
before = SPINE[0] - 1
print('THE EDGES — the last rows before and the first rows after (first 70 chars HE):')
print(f'  {before} last two rows:', [HB(before, r)[:70] for r in range(max(1, len(he[before - 1]) - 1), len(he[before - 1]) + 1)], f'| {SPINE[0]}:1 opens:', HB(SPINE[0], 1)[:110])
print(f'  {SPINE[-1]} last two rows:', [HB(SPINE[-1], r)[:70] for r in range(len(he[SPINE[-1] - 1]) - 1, len(he[SPINE[-1] - 1]) + 1)], '| after:', 'NO PISKA — the export ends at', len(he), '(heads.get(%d) = %r)' % (SPINE[-1] + 1, heads.get(SPINE[-1] + 1)))
print(f'{SPINE[0]}:1 opens (the death\'s piska):', HB(SPINE[0], 1)[:100], '| rows', rows[SPINE[0]])
print(f'{SPINE[-1]}:{rows[SPINE[-1]]} (the chapter\'s last piska, its last row — THE EXPORT\'S LAST ROW):', HB(SPINE[-1], rows[SPINE[-1]]))
print(f'the words of {CH}:1 ("and Moses went up") in {before} / a piska after {SPINE[-1]}:', any('ויעל משה' in HB(before, r) for r in range(1, len(he[before - 1]) + 1)), (SPINE[-1] + 1) in heads and heads[SPINE[-1] + 1] is not None, [r for r in range(1, len(he[before - 1]) + 1) if 'ויעל משה' in HB(before, r)])
t = open(f'{SP}/ch{CH}_dump0.out', encoding='utf-8').read()
import ast
OUT = ast.literal_eval(re.search(r'^  the rows OUTSIDE the spine piskaot [^:]*: \d+ (\[.*?\]) \|', t, re.M).group(1))
ob = sum(len(clean(he[p - 1][r - 1]).encode()) + len(clean(en[p - 1][r - 1]).encode()) for p, r in OUT)
print('the outside rows', OUT, len(OUT), '| bytes', ob, '| their heads and cites', {(p, r): (str(heads[p]), sorted({c[2] for c in he_cites(clean(he[p - 1][r - 1])) if c[0] == 'דברים' and c[1] == CH}) or [CH]) for p, r in OUT})
print('first 80 chars HE', {(p, r): HB(p, r)[:80] for p, r in OUT})
print('the rows of 357 citing a chapter-34 verse in the Hebrew (the seat rule by row):', [(r, sorted({c[2] for c in he_cites(clean(he[356][r - 1])) if c[0] == 'דברים' and c[1] == CH})) for r in range(1, rows[357] + 1) if any(c[0] == 'דברים' and c[1] == CH for c in he_cites(clean(he[356][r - 1])))])
print('the rows of 357 opening with a bold lemma (the export marks the verse quoted):', [(r, re.search(r'<b>([^<]{0,60})', he[356][r - 1]).group(1) if re.search(r'<b>', he[356][r - 1]) else None) for r in range(1, rows[357] + 1)])
