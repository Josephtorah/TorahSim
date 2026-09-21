#!/usr/bin/env python3
# THE COST AUDIT, second cut: per call — the context's size buckets, the cache-write buckets (where the writes come from), the gaps over the cache's hour.
import json, os, glob, collections, datetime
D = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim')
calls = []
for f in sorted(glob.glob(f'{D}/*.jsonl')):
    with open(f, encoding='utf-8', errors='ignore') as fh:
        for line in fh:
            try: o = json.loads(line)
            except Exception: continue
            if o.get('type') != 'assistant': continue
            u = (o.get('message') or {}).get('usage') or {}
            if not u: continue
            try: t = datetime.datetime.fromisoformat(o['timestamp'].replace('Z', '+00:00'))
            except Exception: continue
            calls.append((t, u.get('input_tokens', 0), u.get('cache_creation_input_tokens', 0), u.get('cache_read_input_tokens', 0), u.get('output_tokens', 0)))
calls.sort()
PRICE = {'in': 15, 'cw': 18.75, 'cr': 1.5, 'out': 75}   # $/M — the Opus-class list prices as the yardstick (Fable's own unknown here); the SPLIT is what matters
def dollars(i, cw, cr, out): return (i * PRICE['in'] + cw * PRICE['cw'] + cr * PRICE['cr'] + out * PRICE['out']) / 1e6
print('THE SPLIT BY DAY at the yardstick prices (new input / cache writes / cache reads / output) and the count of calls')
by = collections.defaultdict(list)
for c in calls: by[c[0].date().isoformat()].append(c)
for d in sorted(by):
    L = by[d]; i = sum(c[1] for c in L); cw = sum(c[2] for c in L); cr = sum(c[3] for c in L); out = sum(c[4] for c in L); tot = dollars(i, cw, cr, out)
    print('  %s  calls %4d  $%6.0f  = writes $%5.0f (%2d%%) + reads $%5.0f (%2d%%) + output $%5.0f (%2d%%)   avg ctx %3dk' % (d, len(L), tot, cw * PRICE['cw'] / 1e6, 100 * cw * PRICE['cw'] / 1e6 / tot, cr * PRICE['cr'] / 1e6, 100 * cr * PRICE['cr'] / 1e6 / tot, out * PRICE['out'] / 1e6, 100 * out * PRICE['out'] / 1e6 / tot, (i + cw + cr) // len(L) // 1000))
print('WHERE THE CACHE WRITES COME FROM (calls bucketed by their own write size) — all days')
B = [(0, 5e3), (5e3, 20e3), (20e3, 100e3), (100e3, 300e3), (300e3, 2e6)]
for lo, hi in B:
    L = [c for c in calls if lo <= c[2] < hi]; print('  writes %4dk-%4dk per call: %5d calls, %7.1fM tokens written (%2d%% of all writes)' % (lo / 1e3, hi / 1e3, len(L), sum(c[2] for c in L) / 1e6, 100 * sum(c[2] for c in L) / sum(c[2] for c in calls)))
print('THE BIG WRITES (over 300k in one call): the gap since the call before, in minutes — a gap past the hour is the cache expired; a short gap is a compaction or a changed prefix')
big = [(k, c) for k, c in enumerate(calls) if c[2] >= 300e3]
gaps = [((c[0] - calls[k - 1][0]).total_seconds() / 60 if k else 0) for k, c in big]
print('  %d big writes; gaps over 60 min: %d; gaps under 5 min: %d; their writes %.1fM of %.1fM' % (len(big), sum(1 for g in gaps if g > 60), sum(1 for g in gaps if g < 5), sum(c[2] for _, c in big) / 1e6, sum(c[2] for c in calls) / 1e6))
print('THE CONTEXT PER CALL (cache reads are the context re-read every call) — all days')
for lo, hi in ((0, 300e3), (300e3, 600e3), (600e3, 1.1e6)):
    L = [c for c in calls if lo <= c[1] + c[2] + c[3] < hi]; print('  context %4dk-%4dk: %5d calls (%2d%%), reads %7.1fM (%2d%% of all reads)' % (lo / 1e3, hi / 1e3, len(L), 100 * len(L) / len(calls), sum(c[3] for c in L) / 1e6, 100 * sum(c[3] for c in L) / sum(c[3] for c in calls)))
print('THE OUTPUT PER CALL — all days: calls over 5k output tokens carry what share of the output?')
L = [c for c in calls if c[4] >= 5000]; print('  %d calls over 5k output (of %d) carry %.1fM of %.1fM output (%d%%)' % (len(L), len(calls), sum(c[4] for c in L) / 1e6, sum(c[4] for c in calls) / 1e6, 100 * sum(c[4] for c in L) / sum(c[4] for c in calls)))
