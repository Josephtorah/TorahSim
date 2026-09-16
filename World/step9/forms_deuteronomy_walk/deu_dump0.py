import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# DEUTERONOMY chapters 1-3, THE READING — the first look at the spine (the Sifrei on Deuteronomy) BY POSITION: piskaot 1-30 (the heads printed
# earlier: 1-25 on 1:1-1:28, 26-30 on 3:23-3:29, 31 opening at 6:4), both files' row counts per piska, every row's first citation, the rows
# OUTSIDE 1-30 citing chapters 1-3 in the export's forms, and the rows dumped to a file for the reading. Nothing typed.
import json, re, html, os, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
print('piskaot', len(he), len(en), 'rows', sum(len(s) for s in he), sum(len(s) for s in en))
print('row-count mismatches HE/EN over the whole export:', [(p, len(he[p-1]), len(en[p-1])) for p in range(1, len(he)+1) if len(he[p-1]) != len(en[p-1])])
HEB = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100}
def gem(s): return sum(HEB.get(ch, 0) for ch in s)
def he_cites(t): return [(b, gem(c), gem(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
P = list(range(1, 31))
print('---- HEADS 1-32 (HE first citation | EN first quoted words) and row counts')
for p in range(1, 33):
    h = clean(he[p-1][0]) if he[p-1] else ''
    e = clean(en[p-1][0]) if en[p-1] else ''
    m = re.search(r'^\(([^)]+)\)', h)
    eq = re.search(r'“([^”]{0,80})', e)
    print(f'  {p:3d} HE rows {len(he[p-1]):2d} EN rows {len(en[p-1]):2d} | HE head {m.group(1) if m else "NO PAREN — " + h[:40]!r} | EN first quote {eq.group(1)[:60] if eq else e[:60]!r}')
print('---- EVERY ROW of 1-30: HE first paren | EN first quote (the head check: a row whose first citation is not its head\'s chapter is printed marked)')
for p in P:
    for r in range(len(he[p-1])):
        h = clean(he[p-1][r]); e = clean(en[p-1][r]) if r < len(en[p-1]) else '(no EN row)'
        m = re.search(r'^\(([^)]+)\)', h); mm = re.search(r'\(([^)]+)\)', h)
        eq = re.search(r'“([^”]{0,60})', e)
        first = m.group(1) if m else (('later: ' + mm.group(1)) if mm else 'NONE')
        print(f'  {p}:{r+1} HE {len(h):5d} ch | {first!r:34} | EN {len(e):5d} ch | {eq.group(1)[:50] if eq else e[:50]!r}')
print('---- ROWS OUTSIDE 1-30 CITING DEUTERONOMY 1-3 (HE "(דברים א/ב/ג n)" form; EN "(Deut. n:m)" / "Deuteronomy n:m" / "(Ibid. n:m)")')
outside_he = [(p, r+1, c) for p in range(31, len(he)+1) for r, row in enumerate(he[p-1]) for c in he_cites(clean(row)) if c[0] == 'דברים' and c[1] in (1, 2, 3)]
print('  HE rows citing Deut 1-3 outside 1-30:', len(outside_he), outside_he[:80])
en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Devarim) ([123]):(\d+)')
outside_en = [(p, r+1, m.group(1) + ':' + m.group(2)) for p in range(31, len(en)+1) for r, row in enumerate(en[p-1]) for m in en_forms.finditer(clean(row))]
print('  EN rows citing Deut 1-3 outside 1-30:', len(outside_en), outside_en[:80])
sample = clean(en[0][1]); print('  EN citation forms in 1:2 sample:', re.findall(r'\([^)]{2,40}\)', sample)[:12])
print('  EN forms across the export (top 15 book words inside parens):', __import__('collections').Counter(re.findall(r'\(([A-Za-z\.]+) \d+:\d+', ' '.join(clean(r) for s in en for r in s))).most_common(15))
print('  HE forms across the export (top 15 words before the marks):', __import__('collections').Counter(b for s in he for r in s for b, _, _ in he_cites(clean(r))).most_common(15))
# the rows to a file
with open(f'{SP}/deu_sifrei_rows_1_30.txt', 'w', encoding='utf-8') as f:
    for p in P:
        for r in range(max(len(he[p-1]), len(en[p-1]))):
            f.write(f'\n## Sifrei {p}:{r+1} HE\n{clean(he[p-1][r]) if r < len(he[p-1]) else "(no HE row)"}\n')
            f.write(f'\n## Sifrei {p}:{r+1} EN\n{clean(en[p-1][r]) if r < len(en[p-1]) else "(no EN row)"}\n')
print('rows file bytes', os.path.getsize(f'{SP}/deu_sifrei_rows_1_30.txt'))
