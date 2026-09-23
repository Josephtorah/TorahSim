#!/usr/bin/env python3
# 13b docket D2 — THE D2 SERIES RE-CHUNKED BY WORK (the design: Kiddushin 14b-22b WHOLE, THE CLEAN POINT after it UNCONDITIONALLY, then Bekhorot 25a-28b WHOLE — the
# dump-order series ch15_uncred_d2_NN.txt mixes the two ranges in one file, so the uncredited rows are printed again WHOLE (THE WHOLE-ROW RULE) into one series per
# long range: ch15_uncred_d2k_NN.txt (Kiddushin 14b-22b) and ch15_uncred_d2b_NN.txt (Bekhorot 25a-28b), each chunk at most 64,000 bytes (one Read page); the
# unresolved credited rows of D2 (ch15_uncred_unres_d2.txt) split the same way into _d2k / _d2b. The sets from ch15_docket_common.long_range — computed, never typed.
# The rows are byte-identical to the dump-order series' (asserted: the union of the two new series equals the old series' rows).
import re, os, sys
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
from ch15_docket_common import ADDRS, long_range, D2
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
    chunks, cur, cur_b, first, last, lines = [], [], 0, None, None, []
    def flush():
        nonlocal cur, cur_b, first
        if not cur: return
        fn = f'{SP}/ch15_uncred_{tag}_{len(chunks):02d}.txt'; open(fn, 'w', encoding='utf-8').write('\n'.join(cur) + '\n')
        chunks.append((os.path.basename(fn), first, last, len(cur), cur_b)); cur, cur_b, first = [], 0, None
    for i, kind, addr, cred, body in rows:
        if cred or not sel(addr): continue
        line = '%d %s %s | %s' % (i, kind[0], addr, body); lines.append(line)
        if cur and cur_b + len(line.encode()) + 1 > CAP: flush()
        if first is None: first = i
        last = i; cur.append(line); cur_b += len(line.encode()) + 1
    flush(); return lines, chunks
lk, ck = series('d2k', lambda a: long_range(a) == 'Kiddushin 14b-22b')
lb, cb = series('d2b', lambda a: long_range(a) == 'Bekhorot 25a-28b')
old = []
for fn in sorted(f for f in os.listdir(SP) if re.match(r'ch15_uncred_d2_\d\d\.txt$', f)): old += open(f'{SP}/{fn}', encoding='utf-8').read().splitlines()
assert sorted(old) == sorted(lk + lb), (len(old), len(lk), len(lb))   # the same rows, whole, re-split by work
print('D2', len(D2), 'uncredited', len(old), '| Kiddushin 14b-22b', len(lk), 'chunks', len(ck), '| Bekhorot 25a-28b', len(lb), 'chunks', len(cb))
for tag, ch in (('K', ck), ('B', cb)):
    for fn, a, z, n, b in ch: print('  %s %s rows %d-%d (%d rows, %d bytes)' % (tag, fn, a, z, n, b))
unres = open(f'{SP}/ch15_uncred_unres_d2.txt', encoding='utf-8').read().splitlines()
def u_addr(line): return re.match(r'\d+ U ([LT]) (.+?) \| ', line).group(2)
uk = [l for l in unres if long_range(u_addr(l)) == 'Kiddushin 14b-22b']; ub = [l for l in unres if long_range(u_addr(l)) == 'Bekhorot 25a-28b']
assert len(uk) + len(ub) == len(unres)
open(f'{SP}/ch15_uncred_unres_d2k.txt', 'w', encoding='utf-8').write('\n'.join(uk) + ('\n' if uk else ''))
open(f'{SP}/ch15_uncred_unres_d2b.txt', 'w', encoding='utf-8').write('\n'.join(ub) + ('\n' if ub else ''))
print('unresolved credited rows D2', len(unres), '| Kiddushin', len(uk), sum(len(l.encode()) + 1 for l in uk), 'bytes | Bekhorot', len(ub), sum(len(l.encode()) + 1 for l in ub), 'bytes')
# the roster of the two ranges — link/topic rows, credited, by folio
from collections import OrderedDict
for name in ('Kiddushin 14b-22b', 'Bekhorot 25a-28b'):
    fol = OrderedDict()
    for i, kind, addr, cred, body in rows:
        if long_range(addr) != name: continue
        f = addr.rsplit(':', 1)[0]; r = fol.setdefault(f, [0, 0, 0, 0]); r[0] += 1; r[1] += kind == 'LINK'; r[2] += cred; r[3] += 0 if cred else len(body.encode())
    print(name, 'folios', len(fol), '| folio: rows link credited uncredited_bytes')
    print('  ' + '; '.join('%s %d/%d/%d/%d' % (f, *v) for f, v in fol.items()))
