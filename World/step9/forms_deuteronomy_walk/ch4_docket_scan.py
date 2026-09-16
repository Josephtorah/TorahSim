import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4 (2026-09-16): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (deu_docket_scan.py's form on chapter 4). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports
# whose English cites a verse of Deuteronomy 4:1-49; (2) THE TOPIC ROWS by address (the union rule; the reading ledger's TESTING paragraph and
# COMPILE_DEBT's sitting-2 box (k)): Rosh Hashanah 28b, Eruvin 96a, Sanhedrin 88b-89a (bal tosif — 4:2); Kiddushin 30a (4:9); Mishnah Avodah
# Zarah 3:1-3 with Rosh Hashanah 24a-24b (the images — 4:16-19); Avodah Zarah 55a (4:19); Ketubot 111b (4:4); Mishnah Makkot 2:4-8 with Makkot
# 9b-10a (4:41-43 — credited from the refuge and opening-speech dockets); Mishnah Pesachim 10:4 (4:34); Berakhot 32b (4:7); (3) THE PRIOR READS credited.
import json, re, os, collections, glob, subprocess
ROOT = _ROOT
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ch4_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(4, v) for v in range(1, 50)}
CITE = re.compile(r'(?:Deuteronomy|Deut\.?|Dt\.?) ?(\d+):(\d+)(?:[-–](\d+))?')

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
scanned = 0
for w in sorted(os.listdir(R)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): continue
    try:
        d = json.load(open(p, encoding='utf-8'))
    except Exception:
        continue
    cats = d.get('categories') or [] if isinstance(d, dict) else []
    if not cats or cats[0] not in ('Talmud', 'Mishnah', 'Tosefta') or 'Yerushalmi' in cats or 'Commentary' in cats or '_on_' in w: continue
    scanned += 1
    for path, s in walk(d['text'], []):
        t = strip(s)
        hits = []
        for m in CITE.finditer(t):
            c, a, z = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2))
            for v in range(a, min(z, a + 60) + 1):
                if (c, v) in SPAN: hits.append('Deut %d:%d' % (c, v))
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('SCANNED %d works (Talmud / Mishnah / Tosefta, no Yerushalmi, no commentary); the forms: Deuteronomy c:v, Deut. c:v, Dt.c:v' % scanned)
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))
print('  the verses cited: %s' % collections.Counter(h for _, hs, _ in link for h in hs).most_common(80))
for a, hs, t in link: print('  LINK %-26s %-22s %s' % (a, ' '.join(hs), t[:140].replace('\n', ' ')))

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
mishnah_rows('Mishnah_Avodah_Zarah', [(3, 1), (3, 2), (3, 3)])
mishnah_rows('Mishnah_Makkot', [(2, m) for m in range(4, 9)])
mishnah_rows('Mishnah_Pesachim', [(10, 4)])
mishnah_rows('Mishnah_Rosh_Hashanah', [(2, 8), (2, 9)])
RANGES = [('Rosh_Hashanah', '28b', '28b'), ('Eruvin', '95b', '96a'), ('Sanhedrin', '88b', '89a'), ('Kiddushin', '30a', '30a'), ('Rosh_Hashanah', '24a', '24b'), ('Avodah_Zarah', '55a', '55a'), ('Ketubot', '111b', '111b'), ('Makkot', '9b', '10a'), ('Berakhot', '32b', '32b')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))

prior = {}
own = {'deu_04_vaetchanan_2026-09-16.md'}
alladdr = list(linked) + [a for a, _ in topic]
for f in sorted(glob.glob(ROOT + '/logic/oral_triage/*.md')):
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
