import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 11b — THE COMPILE OF MIDIAN (2026-09-12): THE EXAM DOCKET'S SCAN, sized by script before the docket is
# written (vows_docket_scan.py's form). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta
# exports whose English cites a verse of Numbers 31:1-54; (2) THE TOPIC ROWS by address (the union rule; the reading ledger's TESTING
# SHELF line and COMPILE_DEBT's sitting-11 box): Mishnah Avodah Zarah chapter 5 WHOLE (5:12 the vessels of Midian) + the folio ranges
# + the single mishnayot (Kelim 11:1, 15:1; Oholot 1:2-3; Terumot 4:3) + the Jerusalem Talmud Terumot 4:3 (the "one of fifty");
# (3) THE PRIOR READS credited.
import json, re, os, collections, glob
R = (_ROOT + '/Data/sefaria_export')
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/midian_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(31, v) for v in range(1, 55)}
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

# ---- THE TOPIC ROWS BY ADDRESS ----
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _ in link}
def mishnah_chapters(w, chapters):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    for c in chapters:
        n = 0
        for m in range(1, len(T[c - 1]) + 1):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            n += 1
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
        print('%s chapter %d: %d mishnayot' % (w, c, n))
def mishnah_rows(w, refs):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    for c, m in refs:
        a = '%s %d:%d' % (w.replace('_', ' '), c, m)
        if a in linked: print('  %s already a link row' % a); continue
        topic.append((a, strip(T[c - 1][m - 1])))
    print('%s single mishnayot: %s' % (w, refs))
def jt_rows(w, c, h):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    segs = T[c - 1][h - 1]
    for i, s in enumerate(segs):
        topic.append(('%s %d:%d:%d' % (w.replace('_', ' '), c, h, i + 1), strip(s)))
    print('%s %d:%d: %d segments' % (w, c, h, len(segs)))
mishnah_chapters('Mishnah_Avodah_Zarah', [5])
mishnah_rows('Mishnah_Kelim', [(11, 1), (15, 1)])
mishnah_rows('Mishnah_Oholot', [(1, 2), (1, 3)])
mishnah_rows('Mishnah_Terumot', [(4, 3)])
jt_rows('Jerusalem_Talmud_Terumot', 4, 3)
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
RANGES = [('Avodah_Zarah', '75b', '76b'), ('Shabbat', '64a', '64b'), ('Nazir', '53b', '54b'), ('Yevamot', '60b', '61a'), ('Sanhedrin', '106a', '106b'),
          ('Sotah', '43a', '43a'), ('Sanhedrin', '54a', '54a'), ('Makkot', '5b', '5b'), ('Pesachim', '30b', '30b'), ('Pesachim', '44b', '44b'),
          ('Pesachim', '14b', '14b'), ('Chullin', '3a', '3a'), ('Kiddushin', '78a', '78a'), ('Sanhedrin', '105a', '105a'), ('Bava_Kamma', '38a', '38a'),
          ('Pesachim', '66b', '66b'), ('Megillah', '15a', '15a')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (Mishnah Avodah Zarah 5 whole + the single mishnayot + the Jerusalem Talmud's halakhah + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))

# ---- THE PRIOR READS ----
prior = {}
own = {'num_31_midian_2026-09-12.md'}
alladdr = list(linked) + [a for a, _ in topic]
for f in sorted(glob.glob((_ROOT + '/logic/oral_triage/*.md'))):
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
