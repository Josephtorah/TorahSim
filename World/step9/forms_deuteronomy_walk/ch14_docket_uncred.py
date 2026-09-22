#!/usr/bin/env python3
# 12b docket (11b's form) — the UNCREDITED rows of the dump printed WHOLE (THE WHOLE-ROW RULE) into chunk files of at most 64,000 bytes each (one chunk one Read —
# the cost rules' rule C; 11b's cap, one page each), in dump order; a chunk never spans the two docket runs (SPLIT_AT computed from the dump: D1 the link rows, the
# Mishnah rows and Chullin 59a-66b; D2 from the first Chullin topic row past folio 66); the chunk
# list printed (file, first index, last index, rows, bytes). The credited rows were read whole at their dockets and are carried with their ledgers.
import re, os
SP = os.path.dirname(os.path.abspath(__file__))
t = open(f'{SP}/ch14_docket_dump.txt', encoding='utf-8').read()
blocks = t.split('\n## ')[1:]
CAP = 64000
def _folio(a):
    m = re.match(r'Chullin (\d+)[ab]:\d+$', a); return int(m.group(1)) if m else None
_addrs = [(m.group(1), m.group(2).strip()) for m in (re.match(r'\[(LINK|TOPIC)\] (.+?)  ', b.partition('\n')[0]) for b in blocks)]
_c0 = _addrs.index(('TOPIC', 'Chullin 59a:1'))   # the first Chullin topic row (the design's first range)
_d2 = [i for i, (k, a) in enumerate(_addrs) if k == 'TOPIC' and _folio(a) is not None and _folio(a) > 66]
SPLIT_AT = {_d2[0]}   # TWO docket runs this chapter (the ~700 clause): D1 = the link rows, the Mishnah rows and Chullin 59a-66b; D2 = the rest — the boundary COMPUTED, never typed
assert all(k == 'TOPIC' and 59 <= _folio(a) <= 66 for k, a in _addrs[_c0:_d2[0]]), 'D1 ends with Chullin 59a-66b whole'
assert all(_folio(a) is None or k == 'LINK' for k, a in _addrs[:_c0]), 'no Chullin topic row before 59a:1'
chunks = []; cur = []; cur_b = 0; first = None
def flush():
    global cur, cur_b, first
    if not cur: return
    n = len(chunks); fn = f'{SP}/ch14_uncred_{n:02d}.txt'
    open(fn, 'w', encoding='utf-8').write('\n'.join(cur) + '\n')
    chunks.append((fn, first, last, len(cur), cur_b)); cur = []; cur_b = 0; first = None
nu = 0
for i, blk in enumerate(blocks):
    head, _, body = blk.partition('\n')
    m = re.match(r'\[(LINK|TOPIC)\] (.+?)  (.*)$', head)
    kind, addr, rest = m.group(1), m.group(2), m.group(3).strip()
    if 'CREDITED' in rest: continue
    nu += 1
    body = ' '.join(body.split())
    line = '%d %s %s | %s' % (i, kind[0], addr, body)
    if cur and (cur_b + len(line.encode()) + 1 > CAP or any(first < s <= i for s in SPLIT_AT)): flush()
    if first is None: first = i
    last = i; cur.append(line); cur_b += len(line.encode()) + 1
flush()
print('uncredited rows', nu, 'chunks', len(chunks), 'SPLIT_AT', sorted(SPLIT_AT), 'D1 rows', _d2[0], 'D2 rows', len(_addrs) - _d2[0])
for fn, a, z, n, b in chunks: print('  %s rows %d-%d (%d rows, %d bytes)' % (os.path.basename(fn), a, z, n, b))
