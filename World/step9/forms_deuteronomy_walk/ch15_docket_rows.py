#!/usr/bin/env python3
# print the docket dump's rows [a, b) with each text cut to N chars — N huge prints the row WHOLE (THE WHOLE-ROW RULE; one chunk per verdict part)
import sys, re, os
SCR = os.path.dirname(os.path.abspath(__file__))
a, b, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
t = open(f'{SCR}/ch15_docket_dump.txt', encoding='utf-8').read()
blocks = t.split('\n## ')[1:]
print('rows %d of %d' % (min(b, len(blocks)) - a, len(blocks)))
for i, blk in enumerate(blocks):
    if i < a or i >= b: continue
    head, _, body = blk.partition('\n')
    m = re.match(r'\[(LINK|TOPIC)\] (.+?)  (.*)$', head)
    kind, addr, rest = m.group(1), m.group(2), m.group(3).strip()
    cred = 'C' if 'CREDITED' in rest else ' '
    body = ' '.join(body.split())
    print('%3d %s%s %-24s %s' % (i, kind[0], cred, addr, body[:N]))
