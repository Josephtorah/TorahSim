#!/usr/bin/env python3
# THE NUMBERS WALK sitting 9b — THE COMPILE OF THE OFFERINGS CALENDAR (2026-09-11): THE EXAM DOCKET'S SCAN, sized by script before the docket is
# written (census2_docket_scan.py's form). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports
# whose English cites a verse of Numbers 28:1-29:39; (2) THE TOPIC ROWS by address (the union rule; the three reading ledgers' TESTING SHELF
# lines and COMPILE_DEBT's sitting-9 box (d)); (3) THE PRIOR READS: every address already verdicted in an earlier logic/oral_triage ledger
# (this sitting's three reading ledgers excluded) is listed CREDITED with its ledger — speed ruling (b), credit guard (1): a quick look.
import json, re, os, collections, glob
R = '<repo-old>/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/offerings_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(28, v) for v in range(1, 32)} | {(29, v) for v in range(1, 40)}
CITE = re.compile(r'Numbers?\.? (\d+):(\d+)(?:[-–](\d+))?')

def addr(work, cats, path):
    if 'Talmud' in cats and 'Bavli' in cats and len(path) >= 2:
        i = path[0]; return '%s %d%s:%d' % (work.replace('_', ' '), i // 2 + 1, 'ab'[i % 2], path[1] + 1)
    return '%s %s' % (work.replace('_', ' '), ':'.join(str(x + 1) for x in path))

def walk(x, path):
    if isinstance(x, list):
        for i, v in enumerate(x): yield from walk(v, path + [i])
    elif isinstance(x, str):
        yield path, x

link = []
works = collections.Counter()
for w in sorted(os.listdir(R)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): continue
    try:
        d = json.load(open(p, encoding='utf-8'))
    except Exception:
        continue
    cats = d.get('categories') or [] if isinstance(d, dict) else []
    if not cats or cats[0] not in ('Talmud', 'Mishnah', 'Tosefta') or 'Yerushalmi' in cats or 'Commentary' in cats or '_on_' in w: continue
    for path, s in walk(d['text'], []):
        t = strip(s)
        hits = []
        for m in CITE.finditer(t):
            c, a, z = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2))
            for v in range(a, min(z, a + 40) + 1):
                if (c, v) in SPAN: hits.append('Num %d:%d' % (c, v))
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))

# ---- THE TOPIC ROWS BY ADDRESS ----
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _ in link}
def mishnah_rows(w, cells):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    for c, m in cells:
        if c - 1 < len(T) and m - 1 < len(T[c - 1]):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
        else:
            print('NO SUCH ROW', w, c, m)
MISHNAH = [('Mishnah_Tamid', [(4, 1)]), ('Mishnah_Menachot', [(4, 2), (4, 3), (4, 4), (6, 6), (6, 7), (8, 4), (8, 5), (9, 2), (9, 3), (9, 4), (9, 5), (10, 6)]),
           ('Mishnah_Shekalim', [(4, 1)]), ('Mishnah_Taanit', [(4, 2)]), ('Mishnah_Temurah', [(2, 1)]), ('Mishnah_Pesachim', [(2, 5)]),
           ('Mishnah_Sukkah', [(4, 9)]), ('Mishnah_Beitzah', [(2, 4)]), ('Mishnah_Shevuot', [(1, 4), (1, 5)])]
for w, cells in MISHNAH: mishnah_rows(w, cells)
SIZES = []
def folio_rows(work, a, z):
    p = os.path.join(R, work, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', work); return
    T = json.load(open(p, encoding='utf-8'))['text']
    n_range = 0; l = 0
    for i in range(idx(a), idx(z) + 1):
        if i >= len(T): print('RANGE PAST THE END', work, a, z, i, len(T)); break
        for j, s in enumerate(T[i]):
            ad = '%s %d%s:%d' % (work.replace('_', ' '), i // 2 + 1, 'ab'[i % 2], j + 1)
            n_range += 1
            if ad in linked: l += 1; continue
            topic.append((ad, strip(s)))
    print('%s %s-%s: %d segments in the range, %d of them link rows' % (work, a, z, n_range, l))
    SIZES.append((work, a, z, n_range, l))
RANGES = [('Yoma', '62b', '63a'), ('Yoma', '46a', '46a'), ('Yoma', '85b', '85b'),
          ('Menachot', '44b', '45b'), ('Menachot', '49a', '50a'), ('Menachot', '65b', '66a'), ('Menachot', '68b', '68b'), ('Menachot', '84b', '84b'), ('Menachot', '87a', '88a'), ('Menachot', '89a', '89a'), ('Menachot', '110a', '110a'),
          ('Pesachim', '35a', '35a'), ('Pesachim', '58a', '59a'), ('Pesachim', '66a', '66a'), ('Pesachim', '77a', '77a'), ('Pesachim', '80b', '81a'), ('Pesachim', '95b', '95b'),
          ('Shabbat', '103b', '103b'), ('Shabbat', '132b', '132b'), ('Taanit', '2b', '3a'),
          ('Sukkah', '34a', '34a'), ('Sukkah', '44a', '44a'), ('Sukkah', '47a', '51a'), ('Sukkah', '55b', '55b'), ('Zevachim', '110b', '110b'),
          ('Rosh_Hashanah', '4b', '5a'), ('Rosh_Hashanah', '16a', '16a'), ('Rosh_Hashanah', '32a', '34a'),
          ('Shevuot', '2a', '2b'), ('Shevuot', '9a', '13a'), ('Beitzah', '12a', '12a'), ('Beitzah', '19a', '20b'),
          ('Chagigah', '6a', '6b'), ('Chagigah', '17a', '18a'), ('Berakhot', '26a', '26a'), ('Arakhin', '13a', '13a')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (Mishnah by address + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))

# ---- THE PRIOR READS ----
prior = {}
own = {'num_28_daily_shabbat_rosh_2026-09-11.md', 'num_28_pesach_shavuot_2026-09-11.md', 'num_29_fall_festivals_2026-09-11.md'}
alladdr = list(linked) + [a for a, _ in topic]
for f in sorted(glob.glob('<repo-old>/logic/oral_triage/*.md')):
    if os.path.basename(f) in own: continue
    txt = open(f, encoding='utf-8').read()
    for a in alladdr:
        if re.search(r'(^|[^\w])' + re.escape(a) + r'(?![\d:])', txt, re.M):
            prior.setdefault(a, []).append(os.path.basename(f))
print('PRIOR READS (credited): %d addresses of %d' % (len(prior), len(alladdr)))
byled = collections.Counter(f for fs in prior.values() for f in fs)
print('  by ledger:', byled.most_common(15))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes')
print('THE RANGES SIZED:')
for w, a, z, n, l in SIZES: print('  %-14s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))
