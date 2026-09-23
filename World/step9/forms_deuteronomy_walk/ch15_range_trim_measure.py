#!/usr/bin/env python3
# 13b — THE RANGE-TRIM MEASURE (before any ruling): a declared folio range's TWO ENDS trimmed to the stretch bearing the chapter's terms (a row bearing a term, or a
# link row, or within MARGIN segments of one); the middle untouched. Over D1 (verdicted) the SAFETY TEST: every trimmed row's verdict must be CONTEXT or OUTSIDE — a
# LAW / DERIVATION / DISPUTE row in a trim means the window is unsafe. Over D2 (unread) the saving measured. The terms typed generously (the safe direction: a broad
# term keeps rows); the counts computed.
import os, sys, re, importlib.util
from collections import Counter, OrderedDict
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
from ch15_docket_common import ADDRS, KIND_FIRST, long_range
MARGIN = int(sys.argv[1]) if len(sys.argv) > 1 else 2
NARROW = len(sys.argv) > 2 and sys.argv[2] == 'narrow'
TERMS = ['release', 'sabbatical', 'seventh year', 'prosbol', 'firstborn', 'first-born', 'shear', 'blemish', 'hebrew slave', 'maidservant', 'awl', 'pierc', 'six years',
         'jubilee', 'needy', 'poor', 'charity', 'lend', 'loan', 'debt', 'creditor', 'severance', 'furnish', 'gift', 'expert', 'deuteronomy 15', 'deut. 15', 'abrogat',
         'remit', 'cancel', 'brother', 'hired', 'wage', 'slave', 'servant', 'master', 'redeem', 'consecrat', 'sanctif', 'year by year', 'lame', 'blind', 'ear', 'door']
if NARROW: TERMS = ['release', 'sabbatical', 'seventh year', 'prosbol', 'firstborn', 'first-born', 'shear', 'blemish', 'hebrew slave', 'hebrew maidservant', 'awl', 'pierc', 'six years', 'needy', 'charity', 'severance', 'furnish', 'deuteronomy 15', 'deut. 15', 'abrogat', 'remit', 'year by year', 'lame', 'blind', 'expert']
print('TERMS', 'narrow' if NARROW else 'broad', len(TERMS))
dump = open(f'{SP}/ch15_docket_dump.txt', encoding='utf-8').read(); blocks = dump.split('\n## ')[1:]
rows = []
for i, blk in enumerate(blocks):
    head, _, body = blk.partition('\n'); m = re.match(r'\[(LINK|TOPIC)\] (.+?)  (.*)$', head)
    rows.append((i, m.group(1), m.group(2).strip(), 'CREDITED' in m.group(3), ' '.join(body.split())))
def folio(a):
    m = re.match(r'(.+?) (\d+)([ab]):(\d+)$', a); return (m.group(1), int(m.group(2)), m.group(3), int(m.group(4))) if m else None
# the declared ranges from the scan's print
scan = open(f'{SP}/ch15_docket_scan.out', encoding='utf-8').read(); scan_r = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(w.replace('_', ' '), a, z) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) rows,\s+(\d+) link rows', scan_r, re.M)]
def in_range(a, w, lo, hi):
    f = folio(a)
    if not f or f[0] != w: return False
    key = (f[1], f[2]); return (int(lo[:-1]), lo[-1]) <= key <= (int(hi[:-1]), hi[-1])
# D1's verdicts from the parts
V = {}
for p in 'ABCDEF':
    part = f'ch15_docket_{p}'; spec = importlib.util.spec_from_file_location(part, f'{SP}/{part}.py'); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    for a, vd, n in mod.ROWS: V.setdefault(a, vd)
tot_rows = tot_trim = 0; unsafe = []; per = []
for w, lo, hi in LONG:
    rr = [r for r in rows if in_range(r[2], w, lo, hi)]
    # a row is 'on' if it bears a term or is a link row or cites the chapter
    on = [any(t in r[4].lower() for t in TERMS) or r[1] == 'LINK' for r in rr]
    idx = [k for k, o in enumerate(on) if o]
    if not idx: per.append((w, lo, hi, len(rr), 'NO TERM ROW', 0, 0)); continue
    a0, z0 = max(0, idx[0] - MARGIN), min(len(rr) - 1, idx[-1] + MARGIN)
    head_trim = rr[:a0]; tail_trim = rr[z0 + 1:]
    trimmed = head_trim + tail_trim; tot_rows += len(rr); tot_trim += len(trimmed)
    vds = Counter(V.get(r[2], 'UNREAD') for r in trimmed)
    bad = [(r[2], V[r[2]]) for r in trimmed if V.get(r[2]) in ('LAW', 'DERIVATION', 'DISPUTE')]
    unsafe += bad
    run = 'D2' if long_range(rr[0][2]) else 'D1'
    per.append((w, lo, hi, len(rr), run, len(head_trim), len(tail_trim), dict(vds), [r[2] for r in head_trim][:3], [r[2] for r in tail_trim][-3:], bad))
print('MARGIN', MARGIN, 'ranges', len(LONG), 'rows in ranges', tot_rows, 'trimmed', tot_trim, 'UNSAFE (LAW/DERIVATION/DISPUTE in a trim)', len(unsafe), unsafe)
for x in per: print(' ', x)
# the OUTSIDE rows of D1 by position: at an edge (in a trim) or inside
d1_out = [a for a, vd in V.items() if vd == 'OUTSIDE']; in_trim = set()
for w, lo, hi in LONG:
    rr = [r for r in rows if in_range(r[2], w, lo, hi)]
    on = [any(t in r[4].lower() for t in TERMS) or r[1] == 'LINK' for r in rr]; idx = [k for k, o in enumerate(on) if o]
    if idx:
        a0, z0 = max(0, idx[0] - MARGIN), min(len(rr) - 1, idx[-1] + MARGIN); in_trim |= {r[2] for r in rr[:a0] + rr[z0 + 1:]}
print('D1 OUTSIDE rows', len(d1_out), 'of them in a trimmed end', sum(1 for a in d1_out if a in in_trim), 'inside the window (untouched)', sum(1 for a in d1_out if a not in in_trim))
print('D1 CONTEXT rows in a trim', sum(1 for a, vd in V.items() if vd == 'CONTEXT' and a in in_trim))
