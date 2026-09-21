#!/usr/bin/env python3
# THE COST AUDIT, fourth cut — DEDUPED BY THE API MESSAGE ID: one response with N content blocks is N transcript entries carrying the SAME usage
# (the third cut's clusters); one usage per message id. Then the split by day, the full re-writes and what precedes them, the context buckets.
import json, os, glob, collections, datetime
D = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim')
E = []; seen = set()
for f in sorted(glob.glob(f'{D}/*.jsonl')):
    with open(f, encoding='utf-8', errors='ignore') as fh:
        for line in fh:
            try: o = json.loads(line)
            except Exception: continue
            if o.get('type') not in ('assistant', 'user'): continue
            try: t = datetime.datetime.fromisoformat(o['timestamp'].replace('Z', '+00:00'))
            except Exception: continue
            if o['type'] == 'assistant':
                mid = (o.get('message') or {}).get('id') or o.get('uuid')
                if mid in seen: continue
                seen.add(mid)
            E.append((t, o))
E.sort(key=lambda x: x[0])
PRICE = {'in': 15, 'cw': 18.75, 'cr': 1.5, 'out': 75}
calls = [(t, (o['message'].get('usage') or {})) for t, o in E if o['type'] == 'assistant' and (o.get('message') or {}).get('usage')]
def U(u): return u.get('input_tokens', 0), u.get('cache_creation_input_tokens', 0), u.get('cache_read_input_tokens', 0), u.get('output_tokens', 0)
by = collections.defaultdict(list)
for t, u in calls: by[t.date().isoformat()].append(U(u))
print('DEDUPED — THE SPLIT BY DAY at the yardstick prices (Opus-class list: $15 in / $18.75 cache write / $1.5 cache read / $75 out per M)')
G = [0, 0, 0, 0]
for d in sorted(by):
    L = by[d]; i, cw, cr, out = (sum(x[k] for x in L) for k in range(4)); G = [G[0] + i, G[1] + cw, G[2] + cr, G[3] + out]
    tot = (i * 15 + cw * 18.75 + cr * 1.5 + out * 75) / 1e6
    print('  %s  calls %4d  $%5.0f = writes $%4.0f (%2d%%) + reads $%4.0f (%2d%%) + output $%4.0f (%2d%%)  avg ctx %3dk  output %4.1fM' % (d, len(L), tot, cw * 18.75 / 1e6, 100 * cw * 18.75 / 1e6 / tot, cr * 1.5 / 1e6, 100 * cr * 1.5 / 1e6 / tot, out * 75 / 1e6, 100 * out * 75 / 1e6 / tot, (i + cw + cr) // len(L) // 1000, out / 1e6))
i, cw, cr, out = G; tot = (i * 15 + cw * 18.75 + cr * 1.5 + out * 75) / 1e6
print('  TOTAL       calls %4d  $%5.0f = writes $%4.0f (%2d%%) + reads $%4.0f (%2d%%) + output $%4.0f (%2d%%)' % (len(calls), tot, cw * 18.75 / 1e6, 100 * cw * 18.75 / 1e6 / tot, cr * 1.5 / 1e6, 100 * cr * 1.5 / 1e6 / tot, out * 75 / 1e6, 100 * out * 75 / 1e6 / tot))
print('THE FULL RE-WRITES (a call writing over 300k): count, their share of all writes, the gaps, the entry before')
big = []; last = None
for k, (t, o) in enumerate(E):
    if o['type'] != 'assistant': last = t if last is None else last; continue
    u = o['message'].get('usage') or {}
    if not u: continue
    _, cw_, cr_, _ = U(u)
    if cw_ >= 300e3:
        gap = (t - last).total_seconds() / 60 if last else 0
        prev = next((E[j][1] for j in range(k - 1, -1, -1) if E[j][1]['type'] == 'user'), None)
        c = (prev or {}).get('message', {}).get('content'); h = c if isinstance(c, str) else ' '.join((b.get('text') or (b.get('content') if isinstance(b.get('content'), str) else ' '.join(x.get('text', '') for x in (b.get('content') or []) if isinstance(x, dict))) or '') for b in (c or []) if isinstance(b, dict))
        h = h[:120].replace('\n', ' ')
        key = 'output-limit-continuation' if 'Output token limit hit' in h else 'compaction' if 'This session is being continued' in h else 'owner-text' if isinstance(c, str) else 'after-a-tool-result'
        big.append((t, gap, cw_, cr_, key))
    last = t
W = sum(U(u)[1] for _, u in calls)
print('  %d full re-writes = %.0fM of %.0fM written (%d%%); gaps: <1m %d, 1-5m %d, 5-60m %d, >60m %d; before them: %s' % (len(big), sum(b[2] for b in big) / 1e6, W / 1e6, 100 * sum(b[2] for b in big) / W, sum(1 for b in big if b[1] < 1), sum(1 for b in big if 1 <= b[1] < 5), sum(1 for b in big if 5 <= b[1] < 60), sum(1 for b in big if b[1] >= 60), dict(collections.Counter(b[4] for b in big))))
print('  the reads on those calls: min %dk, median %dk (a full miss reads only the system prompt)' % (min(b[3] for b in big) // 1000, sorted(b[3] for b in big)[len(big) // 2] // 1000))
print('THE CONTEXT PER CALL (deduped)')
for lo, hi in ((0, 300e3), (300e3, 600e3), (600e3, 1.1e6)):
    L = [U(u) for _, u in calls if lo <= sum(U(u)[:3]) < hi]; print('  context %4dk-%4dk: %5d calls (%2d%%), reads %6.0fM (%2d%%), writes %5.0fM (%2d%%)' % (lo / 1e3, hi / 1e3, len(L), 100 * len(L) / len(calls), sum(x[2] for x in L) / 1e6, 100 * sum(x[2] for x in L) / cr, sum(x[1] for x in L) / 1e6, 100 * sum(x[1] for x in L) / cw))
L = [U(u) for _, u in calls if U(u)[3] >= 5000]; print('OUTPUT: %d calls over 5k output tokens (of %d) carry %.1fM of %.1fM (%d%%); the largest %dk' % (len(L), len(calls), sum(x[3] for x in L) / 1e6, out / 1e6, 100 * sum(x[3] for x in L) / out, max(U(u)[3] for _, u in calls) // 1000))
