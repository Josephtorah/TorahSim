#!/usr/bin/env python3
# 13b docket (12b's form, the split rewritten BY ADDRESS) — the UNCREDITED rows of the dump printed WHOLE (THE WHOLE-ROW RULE) into chunk files of at most 64,000 bytes
# each (one chunk one Read page — the cost rules' rule C), in dump order, ONE RUN PER CHUNK SERIES: ch15_uncred_d1_NN.txt for D1 (every address outside the two long
# ranges) and ch15_uncred_d2_NN.txt for D2 (Kiddushin 14b-22b, then Bekhorot 25a-28b — the sets from ch15_docket_common.long_range, computed, never typed); the
# unresolved credited rows (ch15_uncred_unres.txt from the carry) split the same way into _d1 / _d2 files; the chunk list and THE ROSTER printed (per work — and per
# long range — the rows, the credited, the run). The credited rows were read whole at their dockets and are carried with their ledgers.
import re, os, sys
from collections import OrderedDict
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
from ch15_docket_common import ADDRS, long_range, D1, D2
t = open(f'{SP}/ch15_docket_dump.txt', encoding='utf-8').read()
blocks = t.split('\n## ')[1:]; assert len(blocks) == len(ADDRS)
CAP = 64000
rows = []
for i, blk in enumerate(blocks):
    head, _, body = blk.partition('\n')
    m = re.match(r'\[(LINK|TOPIC)\] (.+?)  (.*)$', head)
    kind, addr, rest = m.group(1), m.group(2).strip(), m.group(3).strip()
    rows.append((i, kind, addr, 'CREDITED' in rest, ' '.join(body.split())))
def series(tag, sel):
    chunks, cur, cur_b, first, last = [], [], 0, None, None
    def flush():
        nonlocal cur, cur_b, first
        if not cur: return
        fn = f'{SP}/ch15_uncred_{tag}_{len(chunks):02d}.txt'; open(fn, 'w', encoding='utf-8').write('\n'.join(cur) + '\n')
        chunks.append((os.path.basename(fn), first, last, len(cur), cur_b)); cur, cur_b, first = [], 0, None
    n = 0
    for i, kind, addr, cred, body in rows:
        if cred or not sel(addr): continue
        n += 1; line = '%d %s %s | %s' % (i, kind[0], addr, body)
        if cur and cur_b + len(line.encode()) + 1 > CAP: flush()
        if first is None: first = i
        last = i; cur.append(line); cur_b += len(line.encode()) + 1
    flush(); return n, chunks
n1, c1 = series('d1', lambda a: long_range(a) is None)
n2, c2 = series('d2', lambda a: long_range(a) is not None)
print('rows', len(rows), 'D1', len(D1), 'D2', len(D2), '| uncredited D1', n1, 'chunks', len(c1), '| uncredited D2', n2, 'chunks', len(c2))
for tag, ch in (('D1', c1), ('D2', c2)):
    for fn, a, z, n, b in ch: print('  %s %s rows %d-%d (%d rows, %d bytes)' % (tag, fn, a, z, n, b))
# the unresolved credited rows split by run
unres = open(f'{SP}/ch15_uncred_unres.txt', encoding='utf-8').read().splitlines()
def u_addr(line): return re.match(r'\d+ U ([LT]) (.+?) \| ', line).group(2)
u1 = [l for l in unres if long_range(u_addr(l)) is None]; u2 = [l for l in unres if long_range(u_addr(l)) is not None]
assert len(u1) + len(u2) == len(unres)
open(f'{SP}/ch15_uncred_unres_d1.txt', 'w', encoding='utf-8').write('\n'.join(u1) + ('\n' if u1 else ''))
open(f'{SP}/ch15_uncred_unres_d2.txt', 'w', encoding='utf-8').write('\n'.join(u2) + ('\n' if u2 else ''))
print('unresolved credited rows', len(unres), 'D1', len(u1), sum(len(l.encode()) + 1 for l in u1), 'bytes', 'D2', len(u2), sum(len(l.encode()) + 1 for l in u2), 'bytes')
# THE ROSTER — per (kind, work or long range): rows, credited, uncredited bytes, first-last index, run
ros = OrderedDict()
for i, kind, addr, cred, body in rows:
    lr = long_range(addr); work = lr if lr else addr.rsplit(' ', 1)[0]
    key = (kind, work); r = ros.setdefault(key, [0, 0, 0, i, i, 'D2' if lr else 'D1'])
    r[0] += 1; r[1] += cred; r[2] += 0 if cred else len(body.encode()); r[4] = i
print('THE ROSTER (kind work: rows credited uncredited_bytes idx_first-idx_last run)')
for (kind, work), (n, c, b, a, z, run) in ros.items(): print('  %s %-22s %4d %4d %7d %4d-%-4d %s' % (kind[0], work, n, c, b, a, z, run))
d1u = sum(b for (k, w), (n, c, b, a, z, run) in ros.items() if run == 'D1'); d2u = sum(b for (k, w), (n, c, b, a, z, run) in ros.items() if run == 'D2')
print('uncredited bytes D1', d1u, 'D2', d2u)
