#!/usr/bin/env python3
# THE NUMBERS WALK sitting 15b — THE COMPILE OF THE REFUGE CITIES (2026-09-13): THE EXAM DOCKET'S SCAN, sized by script before the docket is
# written (bor_docket_scan.py's form). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports
# whose English cites a verse of Numbers 35:1-34; (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-15 box (k)): Mishnah
# Makkot 2:1-8 with Makkot 7a-13a (the manslayer's tractate), Mishnah Sanhedrin 1:4 with Sanhedrin 2a-2b (the court of twenty-three), Mishnah
# Sanhedrin 9:1-2 with 76b-79a (the murderer), Mishnah Sanhedrin 3:4 with 27b (the kin and the haters disqualified), Sanhedrin 45b, Mishnah Bava
# Kamma 4:5 with 40a-41a (the ox's ransom), Ketubot 37b (no ransom), Mishnah Eruvin 4:3 and 5:1-5 with Eruvin 51a (the two thousand cubits),
# Sotah 27b and Mishnah Sotah 9:7, Mishnah Arakhin 9:8 with Arakhin 33b (the Levites' cities), Mishnah Shevuot 4:1 (one witness), Yoma 23a,
# Megillah 29a, Yevamot 46b; (3) THE PRIOR READS credited.
import json, re, os, collections, glob
R = '<repo-old>/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ref_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(35, v) for v in range(1, 35)}
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
            for v in range(a, min(z, a + 60) + 1):
                if (c, v) in SPAN: hits.append('Num %d:%d' % (c, v))
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))
print('  the verses cited: %s' % collections.Counter(h for _, hs, _ in link for h in hs).most_common(60))
for a, hs, t in link: print('  LINK %-26s %-22s %s' % (a, ' '.join(hs), t[:140].replace('\n', ' ')))

# ---- THE TOPIC ROWS BY ADDRESS ----
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _ in link}
def mishnah_rows(w, refs):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    for c, m in refs:
        a = '%s %d:%d' % (w.replace('_', ' '), c, m)
        if a in linked: print('  %s already a link row' % a); continue
        topic.append((a, strip(T[c - 1][m - 1])))
        print('  %s: %s' % (a, strip(T[c - 1][m - 1])[:200]))
    print('%s single mishnayot: %s' % (w, refs))
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
mishnah_rows('Mishnah_Makkot', [(2, m) for m in range(1, 9)])
mishnah_rows('Mishnah_Sanhedrin', [(1, 4), (9, 1), (9, 2), (3, 4)])
mishnah_rows('Mishnah_Bava_Kamma', [(4, 5)])
mishnah_rows('Mishnah_Eruvin', [(4, 3), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)])
mishnah_rows('Mishnah_Sotah', [(9, 7)])
mishnah_rows('Mishnah_Arakhin', [(9, 8)])
mishnah_rows('Mishnah_Shevuot', [(4, 1)])
RANGES = [('Makkot', '7a', '13a'), ('Sanhedrin', '2a', '2b'), ('Sanhedrin', '76b', '79a'), ('Sanhedrin', '27b', '27b'), ('Sanhedrin', '45b', '45b'), ('Bava_Kamma', '40a', '41a'), ('Ketubot', '37b', '37b'), ('Eruvin', '51a', '51a'), ('Sotah', '27b', '27b'), ('Arakhin', '33b', '33b'), ('Yoma', '23a', '23a'), ('Megillah', '29a', '29a'), ('Yevamot', '46b', '46b')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))

# ---- THE PRIOR READS ----
prior = {}
own = {'num_35_refuge_cities_2026-09-13.md'}
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
print('dump', OUT, os.path.getsize(OUT), 'bytes', sum(1 for _ in open(OUT, encoding='utf-8')), 'lines')
print('THE RANGES SIZED:')
for w, a, z, n, l in SIZES: print('  %-14s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))
