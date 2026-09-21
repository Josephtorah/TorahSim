#!/usr/bin/env python3
# THE COST AUDIT, third cut: WHAT TRIGGERS A FULL CACHE RE-WRITE — for every call whose cache write exceeds 300k, the gap since the call before,
# whether the reads went to zero (the whole prefix missed), and the head of the user-side entry just before it (a tool result, a notification, a reminder).
import json, os, glob, collections, datetime, re
D = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim')
E = []
for f in sorted(glob.glob(f'{D}/*.jsonl')):
    with open(f, encoding='utf-8', errors='ignore') as fh:
        for line in fh:
            try: o = json.loads(line)
            except Exception: continue
            if o.get('type') not in ('assistant', 'user'): continue
            try: t = datetime.datetime.fromisoformat(o['timestamp'].replace('Z', '+00:00'))
            except Exception: continue
            E.append((t, o))
E.sort(key=lambda x: x[0])
def head(o):
    m = o.get('message') or {}; c = m.get('content')
    if isinstance(c, str): return c[:110].replace('\n', ' ')
    parts = []
    for b in (c or []):
        if not isinstance(b, dict): continue
        if b.get('type') == 'text': parts.append('TEXT:' + b['text'][:90].replace('\n', ' '))
        elif b.get('type') == 'tool_result':
            cc = b.get('content'); s = cc if isinstance(cc, str) else ' '.join(x.get('text', '') for x in (cc or []) if isinstance(x, dict)); parts.append('RESULT(%dch):%s' % (len(s), s[:60].replace('\n', ' ')))
        elif b.get('type') == 'tool_use': parts.append('USE:' + b.get('name', ''))
    return ' | '.join(parts)[:150]
gapH = collections.Counter(); trig = collections.Counter(); zero = 0; n = 0; last_t = None; shown = 0
for k, (t, o) in enumerate(E):
    if o.get('type') == 'assistant':
        u = (o.get('message') or {}).get('usage') or {}
        cw, cr = u.get('cache_creation_input_tokens', 0), u.get('cache_read_input_tokens', 0)
        if cw >= 300e3:
            n += 1; gap = (t - last_t).total_seconds() / 60 if last_t else 0
            gapH['<1' if gap < 1 else '1-5' if gap < 5 else '5-60' if gap < 60 else '>60'] += 1
            if cr < 20e3: zero += 1
            prev = next((E[j][1] for j in range(k - 1, -1, -1) if E[j][1].get('type') == 'user'), None); h = head(prev) if prev else '?'
            key = 'compaction-summary' if 'This session is being continued' in h or 'summary' in h.lower()[:40] else 'system-reminder' if 'system-reminder' in h else 'task-notification' if 'task-notification' in h else 'tool-result' if 'RESULT(' in h else 'owner-text' if h.startswith('TEXT:') or not h.startswith('RESULT') else 'other'
            trig[key] += 1
            if shown < 24 and t.date().isoformat() in ('2026-09-20', '2026-09-19'): shown += 1; print('  %s gap %5.1fm cw %4dk cr %4dk  %s: %s' % (t.strftime('%m-%d %H:%M'), gap, cw // 1000, cr // 1000, key, h[:100]))
        last_t = t
print('BIG WRITES:', n, '| gaps', dict(gapH), '| reads near zero (the whole prefix missed):', zero, '| the entry before them:', dict(trig))
