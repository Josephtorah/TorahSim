#!/usr/bin/env python3
# 9b docket — the UNCREDITED rows of the dump printed WHOLE (THE WHOLE-ROW RULE) into chunk files of at most 27,000 bytes each, in dump order; the chunk
# list printed (file, first index, last index, rows, bytes). The credited rows were read whole at their dockets and are carried with their ledgers.
import re, os
SP = os.path.dirname(os.path.abspath(__file__))
t = open(f'{SP}/ch11_docket_dump.txt', encoding='utf-8').read()
blocks = t.split('\n## ')[1:]
CAP = 27000
chunks = []; cur = []; cur_b = 0; first = None
def flush():
    global cur, cur_b, first
    if not cur: return
    n = len(chunks); fn = f'{SP}/ch11_uncred_{n:02d}.txt'
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
    if cur and cur_b + len(line.encode()) + 1 > CAP: flush()
    if first is None: first = i
    last = i; cur.append(line); cur_b += len(line.encode()) + 1
flush()
print('uncredited rows', nu, 'chunks', len(chunks))
for fn, a, z, n, b in chunks: print('  %s rows %d-%d (%d rows, %d bytes)' % (os.path.basename(fn), a, z, n, b))
