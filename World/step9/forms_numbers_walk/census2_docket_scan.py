#!/usr/bin/env python3
# THE NUMBERS WALK sitting 8b — THE COMPILE OF THE SECOND CENSUS (2026-09-11): THE EXAM DOCKET'S SCAN, sized by script before the docket is
# written (balak_docket_scan.py's form). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports
# whose English cites Numbers 25:19 or a verse of 26:1-65; (2) THE TOPIC ROWS by address (the union rule; the reading ledger's TESTING SHELF
# lines and COMPILE_DEBT's sitting-8 box): Mishnah Bava Batra 8:1-2 (the inheritance order), 7:1-4 (the sale by measure — the estimate's row,
# Sifrei 132:4); BAVA BATRA 117a-123a WHOLE (the land's division: the exodus generation against the entrants, the lot and the Urim, the
# daughters, Jochebed, Bekhorot's double); 143b; SOTAH 12a-13a WHOLE (Amram, Jochebed, Miriam); SANHEDRIN 110a WHOLE ("the sons of Korah did not
# die"); YOMA 73b WHOLE (the Urim and the lot); SEDER OLAM RABBAH 9-10 by address (the year); (3) THE PRIOR READS: every address already
# verdicted in an earlier logic/oral_triage ledger (this sitting's own reading ledger excluded) is listed CREDITED with its ledger — speed
# ruling (b), credit guard (1): a quick look, not a blind credit.
import json, re, os, collections, glob
R = '<repo-old>/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/census2_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(26, v) for v in range(1, 66)} | {(25, 19)}
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

link = []   # (addr, cites, text)
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
    T = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    for c, m in cells:
        if c - 1 < len(T) and m - 1 < len(T[c - 1]):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
        else:
            print('NO SUCH ROW', w, c, m)
mishnah_rows('Mishnah_Bava_Batra', [(8, 1), (8, 2), (7, 1), (7, 2), (7, 3), (7, 4)])
def folio_rows(work, a, z):
    T = json.load(open(os.path.join(R, work, 'en.json'), encoding='utf-8'))['text']
    n_range = 0
    for i in range(idx(a), idx(z) + 1):
        for j, s in enumerate(T[i]):
            ad = '%s %d%s:%d' % (work.replace('_', ' '), i // 2 + 1, 'ab'[i % 2], j + 1)
            n_range += 1
            if ad in linked: continue
            topic.append((ad, strip(s)))
    print('%s %s-%s: %d segments in the range' % (work, a, z, n_range))
folio_rows('Bava_Batra', '117a', '123a')
folio_rows('Bava_Batra', '143b', '143b')
folio_rows('Sotah', '12a', '13a')
folio_rows('Sanhedrin', '110a', '110a')
folio_rows('Yoma', '73b', '73b')
# Seder Olam Rabbah chapters 9-10 by address (the export: chapters of segments)
d = json.load(open(os.path.join(R, 'Seder_Olam_Rabbah', 'en.json'), encoding='utf-8'))
SO = d['text']
if isinstance(SO, dict):
    SO = SO.get('') or next(v for v in SO.values() if isinstance(v, list) and v)   # the export's chapters sit under the EMPTY key beside 'Introduction' (measured 2026-09-11)
for c in (9, 10):
    node = SO[c - 1] if isinstance(SO, list) and c - 1 < len(SO) else None
    if node is None:
        print('NO SUCH NODE Seder_Olam_Rabbah', c, type(SO)); continue
    segs = list(walk(node, []))
    print('Seder Olam Rabbah %d — %d segments' % (c, len(segs)))
    for path, s in segs:
        a = 'Seder Olam Rabbah %d:%s' % (c, ':'.join(str(x + 1) for x in path))
        if a in linked: continue
        topic.append((a, strip(s)))
print("TOPIC rows %d (Mishnah by address + the five folio ranges whole + Seder Olam 9-10; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(12))

# ---- THE PRIOR READS ----
prior = {}
own = {'num_26_second_census_2026-09-11.md'}
alladdr = list(linked) + [a for a, _ in topic]
for f in sorted(glob.glob('<repo-old>/logic/oral_triage/*.md')):
    if os.path.basename(f) in own: continue
    txt = open(f, encoding='utf-8').read()
    for a in alladdr:
        if re.search(r'(^|[^\w])' + re.escape(a) + r'(?![\d:])', txt, re.M):
            prior.setdefault(a, []).append(os.path.basename(f))
print('PRIOR READS (credited): %d addresses' % len(prior))
byled = collections.Counter(f for fs in prior.values() for f in fs)
print('  by ledger:', byled.most_common(10))

# ---- THE LONG TALMUD RANGES the box names: sized ----
RANGES = [('Bava_Batra', '117a', '123a'), ('Bava_Batra', '143b', '143b'), ('Sotah', '12a', '13a'), ('Sanhedrin', '110a', '110a'), ('Yoma', '73b', '73b'), ('Bava_Batra', '121b', '122a'), ('Bava_Batra', '109b', '109b'), ('Bekhorot', '5a', '5a'), ('Sanhedrin', '108b', '108b')]
print('THE LONG RANGES (segments in the range; of them link rows):')
for w, a, z in RANGES:
    TT = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    n = sum(len(TT[i]) for i in range(idx(a), min(idx(z), len(TT) - 1) + 1))
    l = sum(1 for ad, _, _ in link if ad.startswith(w.replace('_', ' ') + ' ') and idx(a) <= idx(re.match(r'.* (\d+[ab]):', ad).group(1)) <= idx(z))
    print('  %-12s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes')
