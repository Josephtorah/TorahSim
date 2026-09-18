import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6 (2026-09-17): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch5_docket_scan.py's form on chapter 6). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose
# English cites a verse of Deuteronomy 6 (the export's chapter 6 = the DB's — the identity, asserted at the reading); (2) THE TOPIC ROWS by address
# (the union rule; COMPILE_DEBT's sitting-4 box (l)): the CANDIDATE ranges SIZED here, the design choosing which are read whole — Mishnah Berakhot
# 1-3 whole and 9:5, Pesachim 10:4, Sotah 7:1, Maaser Sheni 3:8, Menachot 3:7; Berakhot 2a-16a, 61b; Menachot 31b-37b, 43b; Kiddushin 29a-30b;
# Pesachim 56a, 116a-b; Sanhedrin 4b, 74a; Shabbat 103b; Yoma 11a; Bava Metzia 108a; Temurah 3b-4a; (3) THE PRIOR READS credited.
import json, re, os, collections, glob, subprocess
ROOT = _ROOT
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ch6_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
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
cited = collections.Counter()
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
            if c != 6: continue
            for v in range(a, min(z, a + 60) + 1):
                if 1 <= v <= 25:
                    hits.append('Deut 6:%d' % v); cited[v] += 1
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('SCANNED %d works (Talmud / Mishnah / Tosefta, no Yerushalmi, no commentary); the forms: Deuteronomy c:v, Deut. c:v, Dt.c:v; chapter 6 only' % scanned)
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))
print('  the DB verses cited: %s' % sorted(cited.items()))
for a, hs, t in link: print('  LINK %-26s %-22s %s' % (a, ' '.join(hs), t[:140].replace('\n', ' ')))

def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _ in link}
SIZES = []
def mishnah_rows(w, refs):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    n = 0; l = 0
    for c, m in refs:
        a = '%s %d:%d' % (w.replace('_', ' '), c, m)
        n += 1
        if a in linked: l += 1; continue
        topic.append((a, strip(T[c - 1][m - 1])))
    print('%s mishnayot %s: %d rows, %d link rows' % (w, refs if len(refs) < 8 else f'{refs[0]}..{refs[-1]} ({len(refs)})', n, l))
    SIZES.append((w, str(refs[0]), str(refs[-1]), n, l))
def mishnah_chapters(w, chapters):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    mishnah_rows(w, [(c, m + 1) for c in chapters for m in range(len(T[c - 1]))])
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
mishnah_chapters('Mishnah_Berakhot', [1, 2, 3])
mishnah_rows('Mishnah_Berakhot', [(9, 5)])
mishnah_rows('Mishnah_Pesachim', [(10, 4)])
mishnah_rows('Mishnah_Sotah', [(7, 1)])
mishnah_rows('Mishnah_Maaser_Sheni', [(3, 8)])
mishnah_rows('Mishnah_Menachot', [(3, 7)])
RANGES = [('Berakhot', '2a', '2b'), ('Berakhot', '10b', '11a'), ('Berakhot', '13a', '13b'), ('Berakhot', '15a', '16a'), ('Berakhot', '61b', '61b'),   # THE DESIGN (4b): the verse-anchored amudim of 2a-16a; the remainder enumerated outside declared scope
           ('Menachot', '31b', '37b'), ('Menachot', '43b', '43b'), ('Kiddushin', '29a', '30b'), ('Pesachim', '56a', '56a'),
          ('Pesachim', '116a', '116b'), ('Sanhedrin', '4b', '4b'), ('Sanhedrin', '74a', '74a'), ('Shabbat', '103b', '103b'), ('Yoma', '11a', '11a'), ('Bava_Metzia', '108a', '108a'), ('Temurah', '3b', '4a')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))

prior = {}
own = {'deu_06_vaetchanan_2026-09-17.md'}
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
print('  credited per range: %s' % [(w, a, z, sum(1 for ad in prior if ad.startswith(w.replace('_', ' ') + ' ') and (re.match(r'\d+[ab]', a) and idx(a) <= idx(re.match(r'(\d+[ab])', ad.split(' ')[-1].split(':')[0]).group(1)) <= idx(z) if re.match(r'\d+[ab]', a) and re.match(r'\d+[ab]', ad.split(' ')[-1].split(':')[0]) else True))) for w, a, z, n, l in SIZES if re.match(r'\d+[ab]', a)])

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes', sum(1 for _ in open(OUT, encoding='utf-8')), 'lines')
print('ENUMERATED OUTSIDE DECLARED SCOPE — Berakhot 2a-16a whole: %d rows; the amudim read here: %d' % (sum(len(json.load(open(os.path.join(R, 'Berakhot', 'en.json'), encoding='utf-8'))['text'][i]) for i in range(idx('2a'), idx('16a') + 1)), sum(n for w, a, z, n, l in SIZES if w == 'Berakhot' and a != '61b')))
print('THE RANGES SIZED:')
for w, a, z, n, l in SIZES: print('  %-20s %6s-%-6s %4d rows, %3d link rows' % (w, a, z, n, l))
