#!/usr/bin/env python3
# 10b docket — the carry's unresolved credited rows (ch12_uncred_unres.txt) split by docket run: D1 the dump's rows before 582 (Avodah Zarah 45a:1 the first D2
# row — the runs' boundary), D2 the rest; the index of each address computed from the dump. Run after ch12_credit_carry.py.
import re, os
SP = os.path.dirname(os.path.abspath(__file__)); SPLIT = 582; SPLIT2 = 933   # D2 split in two runs (D2a before Bekhorot 15a:1, D2b the rest)
d = open(f'{SP}/ch12_docket_dump.txt', encoding='utf-8').read(); blocks = d.split('\n## ')[1:]
idx = {}
for i, b in enumerate(blocks):
    a = re.match(r'\[(LINK|TOPIC)\] (.+?)  (.*)$', b.partition('\n')[0]).group(2).strip(); idx.setdefault(a, i)
U = open(f'{SP}/ch12_uncred_unres.txt', encoding='utf-8').read().rstrip('\n').split('\n')
ix = lambda l: idx[l.split(' | ')[0].split(' ', 2)[2]]
d1 = [l for l in U if ix(l) < SPLIT]; d2 = [l for l in U if ix(l) >= SPLIT]; d2a = [l for l in d2 if ix(l) < SPLIT2]; d2b = [l for l in d2 if ix(l) >= SPLIT2]
for name, rows in (('D1', d1), ('D2', d2), ('D2a', d2a), ('D2b', d2b)): open(f'{SP}/ch12_uncred_unres_{name}.txt', 'w', encoding='utf-8').write('\n'.join(rows) + '\n')
print('unresolved D1', len(d1), sum(len(l.encode()) + 1 for l in d1), 'bytes; D2', len(d2), sum(len(l.encode()) + 1 for l in d2), 'bytes; D2a', len(d2a), sum(len(l.encode()) + 1 for l in d2a), 'bytes; D2b', len(d2b), sum(len(l.encode()) + 1 for l in d2b), 'bytes')
