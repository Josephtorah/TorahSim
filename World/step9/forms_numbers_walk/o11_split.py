#!/usr/bin/env python3
"""o11_split.py — compact a batch print for reading under the Read tool's 25k-token cap.
Hebrew runs become <h>; whitespace collapsed; the source cut to 70 chars; every row printed WHOLE
(teacher batches) unless --heads N is given (then unflagged ink proposals are cut to N chars).
Usage: python3 o11_split.py <print.txt> <outprefix> <maxchars> [--heads N]
"""
import re, sys

src, pre, maxc = sys.argv[1], sys.argv[2], int(sys.argv[3])
heads = int(sys.argv[sys.argv.index('--heads') + 1]) if '--heads' in sys.argv else None
HEB = re.compile(r'[֐-׿יִ-ﭏ][֐-׿יִ-ﭏ\s־\-\'"״׳,.:;]*[֐-׿יִ-ﭏ]|[֐-׿יִ-ﭏ]')
rows = open(src, encoding='utf-8').read().split('\n')
out, cur, n = [], [], 0
i = 0
recs = []
while i < len(rows):
    head = rows[i]; body = rows[i + 1] if i + 1 < len(rows) else ''
    i += 2
    if not head.strip(): continue
    h = head.split(' | ')
    h[2] = h[2][:70]
    head = ' | '.join(h)
    body = HEB.sub('<h>', body)
    body = re.sub(r'(<h>[ ,.;:]*)+', '<h> ', body)
    body = re.sub(r'\s+', ' ', body).strip()
    if heads and 'PROPOSE ink' in head and 'flags=-' in head:
        body = body[:heads] + (' ...' if len(body) > heads else '')
    recs.append(head + '\n    ' + body)
parts, cur, n = [], [], 0
for r in recs:
    if n + len(r) > maxc and cur:
        parts.append(cur); cur, n = [], 0
    cur.append(r); n += len(r) + 1
if cur: parts.append(cur)
for k, p in enumerate(parts, 1):
    open('%s_p%d.txt' % (pre, k), 'w', encoding='utf-8').write('\n'.join(p) + '\n')
    print('%s_p%d.txt rows %d chars %d' % (pre, k, len(p), sum(len(x) + 1 for x in p)))
print('rows %d parts %d' % (len(recs), len(parts)))
