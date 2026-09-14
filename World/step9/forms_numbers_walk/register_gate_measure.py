#!/usr/bin/env python3
# THE REGISTER GATE sitting (2026-09-11; the owner: "Ok go") — THE MEASUREMENTS BEFORE THE DESIGN (1b's order): the running world built once;
# (0) the shapes — a ledger entry's keys, the ops, the population rows' as_of values; (1) THE COUNT LINES of the ink — a numeral beside the
# count-noun ("the counted") or "souls" on one line, Genesis through Deuteronomy — against the table's counted rows; (2) THE RECEIPTS "as the
# LORD commanded" (58) against the ledger's closes by verse; (3) THE FOOTERS' blocks against the daemons' given_at; (4) the register headers
# (the 68) with the table's rows per chapter.
import sqlite3, sys, io, contextlib, collections, re, yaml
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    reg = CS.registry_map()
    w, M = CS.run_world(CS.PARAMS['sojourn_start']['value'], reg, 'probe')
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(x): return ''.join(ch for ch in x if ch != '/' and not (0x0591 <= ord(ch) <= 0x05C7))
TORAH = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.idx, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut') ORDER BY v.id, w.idx").fetchall()
def base(lm): return lm.split('/')[-1].split(' ')[0]
V0 = {}
for b, c, v, i, he, lm, m in rows: V0.setdefault((b, c, v), []).append((plain(he), base(lm), lm, m))
KEYS = sorted(V0, key=lambda k: (TORAH.index(k[0]), k[1], k[2]))
V = collections.OrderedDict((k, V0[k]) for k in KEYS)
def ref(k): return '%s %d:%d' % k

print('==== (0) THE SHAPES ====')
ledger = [(ent.eid, e) for ent in w.entities.values() for e in ent.ledger]
keys = collections.Counter(kk for _, e in ledger for kk in e.keys())
print('  ledger entries %d; keys %s' % (len(ledger), dict(keys)))
print('  ops %s' % dict(collections.Counter(e['op'] for _, e in ledger)))
print('  a sample entry: %s' % {k: (str(v)[:50]) for k, v in ledger[0][1].items()})
closes = [(eid, e) for eid, e in ledger if e.get('closed_by') is not None]
print('  closed entries %d (a close flips open on the debit and stamps closed_by / closed_day); closed_by samples: %s' % (len(closes), [str(e['closed_by'])[:70] for _, e in closes[:6]]))
print('  closed_by forms: with a verse ref %d, without %d' % (sum(1 for _, e in closes if re.search(r'(Gen|Exod|Lev|Num|Deut) \d+:\d+', str(e['closed_by']))), sum(1 for _, e in closes if not re.search(r'(Gen|Exod|Lev|Num|Deut) \d+:\d+', str(e['closed_by'])))))
T = w.tables['population']
print('  population rows %d; as_of values %s' % (len(T), dict(collections.Counter(r['as_of'] for r in T))))
print('  a counted row: %s' % {k: str(v)[:30] for k, v in next(r for r in T if r['grain'] == 'counted').items()})
LOG_WRITE = [l for l in w.log if l[0] == 'WRITE']
print('  WRITE log lines %d; keys %s' % (len(LOG_WRITE), dict(collections.Counter(kk for l in LOG_WRITE for kk in l[2].keys()))))
print('  a WRITE line: %s' % {k: str(v)[:40] for k, v in LOG_WRITE[0][2].items()})
EV = [l for l in w.log if l[0] == 'EVENT']
print('  EVENT log lines %d; keys %s' % (len(EV), dict(collections.Counter(kk for l in EV for kk in l[2].keys()))))

print('\n==== (1) THE COUNT LINES — a numeral beside "the counted" (6485) or "souls" (5315) on one line; the table\'s counted rows with that count ====')
def span_has(as_of, k):
    m = re.match(r'(\w+) (\d+):(\d+)(?:-(\d+))?$', as_of or '')
    if not m: return False
    b, c, v1, v2 = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3))
    return k[0] == b and k[1] == c and v1 <= k[2] <= v2
tally = collections.Counter()
for k in KEYS:
    ws = V[k]; bl = [x[1] for x in ws]
    if '6485' in bl or '5315' in bl:
        nums = [n for n in N(*k) if isinstance(n, int) and n >= 2]
        if not nums: continue
        noun = 'the counted' if '6485' in bl else 'souls'
        hits = [r for r in T if r['grain'] == 'counted' and r['count'] in nums and span_has(r['as_of'], k)]
        anyrow = [r for r in T if r['grain'] == 'counted' and r['count'] in nums]
        verdict = 'ROW' if hits else ('ROW-ELSEWHERE' if anyrow else 'NONE')
        tally[(k[0], verdict)] += 1
        print('  %-11s %-11s %-28s %s %s' % (ref(k), noun, nums, verdict, [(r['tribe'], r['as_of']) for r in (hits or anyrow)][:2]))
print('  tally %s' % dict(tally))

print('\n==== (2) THE RECEIPTS — "as the LORD commanded" (k/834 + 6680 + 3068) against the ledger\'s closes by verse ====')
REC = []
for k in KEYS:
    s = [x[2] for x in V[k]]
    for i, lm in enumerate(s):
        if lm.startswith('k/834') and i + 1 < len(s) and s[i + 1].startswith('6680') and any(x.startswith('3068') for x in s[i + 2:i + 4]):
            REC.append(k); break
def spans(text):
    # every 'Book c:v' or 'Book c:v-v2' inside a case_source / closed_by string -> [(book, chapter, v1, v2)]
    out = []
    for m in re.finditer(r'(Gen|Exod|Lev|Num|Deut) (\d+):(\d+)(?:-(\d+))?', str(text or '')):
        out.append((m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3))))
    return out
def contains(text, k):
    return any(b == k[0] and c == k[1] and v1 <= k[2] <= v2 for b, c, v1, v2 in spans(text))
def chapter_of(text, k):
    return any(b == k[0] and c == k[1] for b, c, v1, v2 in spans(text))
rt = collections.Counter()
for k in REC:
    ev = [l[2]['kind'] for l in EV if contains(l[2].get('case_source'), k)]
    cl = [(eid, e['effect']) for eid, e in closes if contains(e.get('closed_by'), k) or contains(e.get('case_source'), k)]
    wr = [(eid, e['effect'], e['op']) for eid, e in ledger if contains(e.get('case_source'), k)]
    ch = [(eid, e['effect']) for eid, e in closes if chapter_of(e.get('closed_by'), k) or chapter_of(e.get('case_source'), k)]
    verdict = 'CLOSE-AT-VERSE' if cl else ('WRITE-AT-VERSE' if wr else ('EVENT-AT-VERSE' if ev else ('CLOSE-IN-CHAPTER' if ch else 'NONE')))
    rt[verdict] += 1
    print('  %-11s %-15s events %s | closes %s | writes %s | chapter-closes %d' % (ref(k), verdict, ev[:3], cl[:3], wr[:3], len(ch)))
print('  tally %s (receipts %d)' % (dict(rt), len(REC)))

print('\n==== (3) THE FOOTERS — the law blocks\' boundaries against the daemons\' given_at ====')
DISP = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml'))
GA = {d: (spec.get('given_at'), spec.get('installed_by')) for d, spec in DISP['daemons'].items()}
def vkey(s):
    m = re.match(r'(\w+) (\d+):(\d+)', s or '')
    return (TORAH.index(m.group(1)), int(m.group(2)), int(m.group(3))) if m and m.group(1) in TORAH else None
FOOT = [k for k in KEYS if V[k][0][1] == '428' and len(V[k]) > 1 and V[k][1][1] in ('2706', '4687', '4941', '1697', '5713')]
prev = (0, 0, 0)
for k in FOOT:
    kk = (TORAH.index(k[0]), k[1], k[2])
    inside = sorted((d for d, (g, ib) in GA.items() if vkey(g) and prev < vkey(g) <= kk), key=lambda d: vkey(GA[d][0]))
    print('  %-11s block (%s, %s] daemons %d: %s' % (ref(k), '%s %d:%d' % (TORAH[prev[0]], prev[1], prev[2]) if prev != (0, 0, 0) else 'start', ref(k), len(inside), ' '.join('%s@%s' % (d, GA[d][0]) for d in inside)[:200]))
    prev = kk
print('  daemons with given_at after the last footer: %s' % [d for d, (g, ib) in GA.items() if vkey(g) and vkey(g) > prev])
print('  daemons %d; given_at by book %s; installed_by %s' % (len(GA), dict(collections.Counter(TORAH[vkey(g)[0]] for g, _ in GA.values() if vkey(g))), dict(collections.Counter(str(ib).split()[0] for _, ib in GA.values()))))

print('\n==== (4) THE REGISTER HEADERS — the 68 on the five nouns; the table\'s rows in that chapter ====')
NOUNS = {'8435': 'generations', '8034': 'names', '1121': 'sons', '4940': 'families', '6485': 'the counted'}
for k in KEYS:
    ws = V[k]
    if ws and ws[0][1] == '428' and len(ws) > 1 and ws[1][1] in NOUNS:
        nums = [n for n in N(*k) if isinstance(n, int)]
        inch = [r for r in T if r['as_of'] and r['as_of'].startswith('%s %d:' % (k[0], k[1]))]
        print('  %-11s %-12s %-6s numerals %-18s rows in the chapter %d' % (ref(k), NOUNS[ws[1][1]], 'CLOSE' if nums else 'OPEN', nums, len(inch)))
