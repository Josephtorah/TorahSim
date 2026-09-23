#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15 (2026-09-22): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch14_docket_scan.py's form on chapter 15, derived by derive_ch15_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian
# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 15 (the export's chapter 15 = the DB's 15:1-23 — the identity, asserted at
# the reading; no fold); (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-13 box (o)): the CANDIDATE ranges SIZED here, the design
# choosing which are read whole — Mishnah Sheviit 10 whole with Gittin 36a-37b (the prozbul; the release by decree) and Arakhin 32b-33a (the jubilee's
# condition); Makkot 3b (the loan's witnesses); Rosh Hashanah 8b-9a (the year's edge); Mishnah Kiddushin 1:2-3 with Kiddushin 14b-22b (the Hebrew slave and
# the maidservant; the awl); Bava Metzia 31b (the pledge), 71a (the ranks of the poor); Mishnah Peah 8:7-9 with Ketubot 67b (the measure of need); Mishnah
# Bekhorot 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6, 6 whole with Bekhorot 25a-28b (the shearing and the work; the year), 33a-37b (the blemishes), 53b (the
# firstling outside the Land); Mishnah Temurah 3:5; Mishnah Arakhin 8:7 (sanctify for its value); Mishnah Shekalim 5:6 (the secret gift); Mishnah Chullin
# 2:9 (the blood on the ground); Tosefta Sheviit 8, Tosefta Kiddushin 1, Tosefta Bekhorot 1-2 sized;
# (3) THE PRIOR READS credited (the earlier dockets' and ledgers' rows — the Sifra on Leviticus 25 and the Mekhilta on Exodus 21 from their sittings).
import json, re, os, collections, glob, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ch15_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
CITE = re.compile(r'(?:Deuteronomy|Deut\.?|Dt\.?) ?(\d+):(\d+)(?:[-–](\d+))?')
CH, NV = 15, 23

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
            # the export's chapter 15 = the DB's 15:1-23 (the identity, asserted at the reading): no fold
            if c != CH: continue
            for v in range(a, min(z, a + 60) + 1):
                if 1 <= v <= NV:
                    hits.append('Deut %d:%d' % (CH, v)); cited[v] += 1
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('SCANNED %d works (Talmud / Mishnah / Tosefta, no Yerushalmi, no commentary); the forms: Deuteronomy c:v, Deut. c:v, Dt.c:v; chapter %d only' % (scanned, CH))
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))
print('  the DB verses cited: %s' % sorted(cited.items()))
print('  the verses NOT cited by anyone: %s' % [v for v in range(1, NV + 1) if v not in cited])
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
mishnah_chapters('Mishnah_Sheviit', [10])
mishnah_rows('Mishnah_Kiddushin', [(1, 2), (1, 3)])
mishnah_rows('Mishnah_Peah', [(8, 7), (8, 8), (8, 9)])
mishnah_rows('Mishnah_Bekhorot', [(1, 1), (1, 2), (2, 6), (2, 7), (2, 8), (2, 9), (3, 3), (3, 4), (4, 1), (4, 2), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)])
mishnah_chapters('Mishnah_Bekhorot', [6])
mishnah_rows('Mishnah_Temurah', [(3, 5)])
mishnah_rows('Mishnah_Arakhin', [(8, 7)])
mishnah_rows('Mishnah_Shekalim', [(5, 6)])
mishnah_rows('Mishnah_Chullin', [(2, 9)])
RANGES = [('Gittin', '36a', '37b'), ('Arakhin', '32b', '33a'), ('Makkot', '3b', '3b'), ('Rosh_Hashanah', '8b', '9a'), ('Kiddushin', '14b', '22b'), ('Bava_Metzia', '31b', '31b'), ('Bava_Metzia', '71a', '71a'), ('Ketubot', '67b', '67b'), ('Bekhorot', '25a', '28b'), ('Bekhorot', '33a', '37b'), ('Bekhorot', '53b', '53b')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))
# TOSEFTA SHEVIIT 8 (the release and the prozbul beside Mishnah Sheviit 10), TOSEFTA KIDDUSHIN 1 (the Hebrew slave's acquisitions and exits beside Mishnah Kiddushin 1:2-3), TOSEFTA BEKHOROT 1-2 (the firstling) SIZED — the design chooses; a dict-text export read under its empty key
for w, c in (('Tosefta_Sheviit', 8), ('Tosefta_Kiddushin', 1), ('Tosefta_Bekhorot', 1), ('Tosefta_Bekhorot', 2)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): print('NOT IN THE EXPORT:', w); continue
    T = json.load(open(p, encoding='utf-8'))['text']
    if isinstance(T, dict):
        print('  %s: the text keys %s; the empty key holds %s of %d' % (w, list(T), type(T['']).__name__, len(T[''])))
        T = T['']
    if c - 1 >= len(T): print('CHAPTER PAST THE END OF THE EXPORT: %s %d (the export holds %d top-level entries)' % (w, c, len(T))); continue
    rows = T[c - 1]; rows = rows if isinstance(rows, list) else [rows]
    if not rows: print('EMPTY CHAPTER IN THE EXPORT: %s %d (the dict-text export holds no rows there — the design reads it from this print)' % (w, c)); continue
    for i, x in enumerate(rows): topic.append(('%s %d:%d' % (w.replace('_', ' '), c, i + 1), strip(x if isinstance(x, str) else ' '.join(x))))
    print('%s %d: %d rows; the first: %s' % (w, c, len(rows), strip(rows[0] if isinstance(rows[0], str) else ' '.join(rows[0]))[:120]))
# THE RANGES BY AMUD (segments; the first 90 characters of each amud's first row — the design chooses; the rest enumerated outside declared scope)
for wname, a, z in RANGES:
    TB = json.load(open(os.path.join(R, wname, 'en.json'), encoding='utf-8'))['text']
    for i in range(idx(a), idx(z) + 1):
        print('   %-14s %4s %3d  %s' % (wname, '%d%s' % (i // 2 + 1, 'ab'[i % 2]), len(TB[i]), strip(TB[i][0])[:90].replace('\n', ' ') if TB[i] else ''))
for wname in ('Tosefta_Sheviit', 'Tosefta_Kiddushin', 'Tosefta_Bekhorot', 'Mishnah_Sheviit', 'Mishnah_Kiddushin', 'Mishnah_Peah', 'Mishnah_Bekhorot', 'Mishnah_Temurah', 'Mishnah_Arakhin', 'Mishnah_Shekalim', 'Mishnah_Chullin', 'Gittin', 'Arakhin', 'Makkot', 'Rosh_Hashanah', 'Kiddushin', 'Bava_Metzia', 'Ketubot', 'Bekhorot', 'Sifra', 'Sifrei_Devarim'):
    print('  export has %s: %s' % (wname, os.path.exists(os.path.join(R, wname, 'en.json'))))

prior = {}
own = {'deu_15_reeh_2026-09-22.md'}
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
print('  the Mishnah rows credited: %s' % sorted(a for a in prior if a.startswith('Mishnah')))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes', sum(1 for _ in open(OUT, encoding='utf-8')), 'lines')
print('THE RANGES SIZED:')
for w, a, z, n, l in SIZES: print('  %-22s %6s-%-6s %4d rows, %3d link rows' % (w, a, z, n, l))
