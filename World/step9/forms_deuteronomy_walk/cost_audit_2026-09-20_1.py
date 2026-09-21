#!/usr/bin/env python3
# THE COST AUDIT (2026-09-20, on the owner's "Do a complete audit of our process"): the bill read from the session transcripts — every assistant
# message's usage (new input, cache writes, cache reads, output) summed by day and by session; the context per turn = input + cache_read + cache_write.
import json, os, glob, collections, datetime
D = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim')
by_day = collections.defaultdict(lambda: [0, 0, 0, 0, 0, 0])   # turns, input, cache_write, cache_read, output, max_context
by_sess = collections.defaultdict(lambda: [0, 0, 0, 0, 0, 0, '', ''])
for f in sorted(glob.glob(f'{D}/*.jsonl')):
    sid = os.path.basename(f)[:8]
    with open(f, encoding='utf-8', errors='ignore') as fh:
        for line in fh:
            try: o = json.loads(line)
            except Exception: continue
            if o.get('type') != 'assistant': continue
            u = (o.get('message') or {}).get('usage') or {}
            if not u: continue
            ts = o.get('timestamp', '')[:10]
            i, cw, cr, out = u.get('input_tokens', 0), u.get('cache_creation_input_tokens', 0), u.get('cache_read_input_tokens', 0), u.get('output_tokens', 0)
            ctx = i + cw + cr
            for k, row in ((ts, by_day[ts]), (sid, by_sess[sid])):
                row[0] += 1; row[1] += i; row[2] += cw; row[3] += cr; row[4] += out; row[5] = max(row[5], ctx)
            if not by_sess[sid][6]: by_sess[sid][6] = ts
            by_sess[sid][7] = ts
def M(n): return '%6.1fM' % (n / 1e6)
print('BY DAY (assistant turns; new input; cache writes; cache reads; output; the largest context seen)')
T = [0] * 5
for d in sorted(by_day):
    r = by_day[d]; T = [T[k] + r[k] for k in range(5)]
    print('  %s  turns %5d  input %s  cache_w %s  cache_r %s  output %s  max_ctx %4dk' % (d, r[0], M(r[1]), M(r[2]), M(r[3]), M(r[4]), r[5] // 1000))
print('  TOTAL       turns %5d  input %s  cache_w %s  cache_r %s  output %s' % (T[0], M(T[1]), M(T[2]), M(T[3]), M(T[4])))
print('BY SESSION (first day .. last day)')
for s, r in sorted(by_sess.items(), key=lambda kv: kv[1][6]):
    print('  %s  %s..%s  turns %5d  input %s  cache_w %s  cache_r %s  output %s  max_ctx %4dk' % (s, r[6], r[7], r[0], M(r[1]), M(r[2]), M(r[3]), M(r[4]), r[5] // 1000))
