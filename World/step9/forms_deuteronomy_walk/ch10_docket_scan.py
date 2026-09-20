#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10 (2026-09-20): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch9_docket_scan.py's form on chapter 10, derived by derive_ch10_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian
# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 10 (the export's chapter 10 = the DB's — the identity, asserted at the
# reading); (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-8 box (n)): the CANDIDATE ranges SIZED here, the design choosing which
# are read whole — Bava Batra 14a-b, Menachot 99a-b, Berakhot 8b (the ark and the fragments); Mishnah Shekalim 6:1-2 (the ark hidden); Berakhot 33b,
# Menachot 43b, Shabbat 31b, Sotah 14a (the demand and the ways); Yoma 69b, Megillah 25a, Berakhot 20b, Niddah 70b, Mishnah Berakhot 9:5 (the
# attributes, the face); Ketubot 105a-b (the bribe); Bava Metzia 59b, Yevamot 47a-b (the stranger); Ketubot 111b (cleave); Shevuot 35b, Temurah 3b-4a,
# Sanhedrin 56a (the Name, the oath); Bava Batra 123a-b (the seventy); Rosh Hashanah 3a, Ta'anit 9a, Seder Olam 6 and 9-10 (Aaron and the forty);
# Mishnah Sotah 7:6 (the blessing in the Name); (3) THE PRIOR READS credited (the Numbers walk's, the erection's and the earlier dockets' rows among them).
import json, re, os, collections, glob, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ch10_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
CITE = re.compile(r'(?:Deuteronomy|Deut\.?|Dt\.?) ?(\d+):(\d+)(?:[-–](\d+))?')
CH, NV = 10, 22

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
mishnah_rows('Mishnah_Shekalim', [(6, 1), (6, 2)])
mishnah_rows('Mishnah_Sotah', [(7, 6)])
mishnah_rows('Mishnah_Berakhot', [(9, 5)])
RANGES = [('Bava_Batra', '14a', '14b'), ('Menachot', '99a', '99b'), ('Berakhot', '8b', '8b'), ('Berakhot', '33b', '33b'), ('Menachot', '43b', '43b'), ('Shabbat', '31b', '31b'), ('Sotah', '14a', '14a'),
          ('Yoma', '69b', '69b'), ('Megillah', '25a', '25a'), ('Berakhot', '20b', '20b'), ('Niddah', '70b', '70b'), ('Ketubot', '105a', '105b'), ('Bava_Metzia', '59b', '59b'), ('Yevamot', '47a', '47b'),
          ('Ketubot', '111b', '111b'), ('Shevuot', '35b', '35b'), ('Temurah', '3b', '4a'), ('Sanhedrin', '56a', '56a'), ('Bava_Batra', '123a', '123b'), ('Rosh_Hashanah', '3a', '3a'), ('Taanit', '9a', '9a')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))
# SEDER OLAM RABBAH 6, 9, 10 (the forties, Aaron's death and the retreat) and TOSEFTA SOTAH 7 whole (the two arks searched in it) — the export's Seder Olam
# text is a dict of two keys, 'Introduction' and '' (the chapters under the EMPTY key): 7b's "unreachable" was the reader's index, not the export
for w, c in (('Seder_Olam_Rabbah', 6), ('Seder_Olam_Rabbah', 9), ('Seder_Olam_Rabbah', 10), ('Tosefta_Sotah', 7)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): print('NOT IN THE EXPORT:', w); continue
    T = json.load(open(p, encoding='utf-8'))['text']
    if isinstance(T, dict):
        print('  %s: the text keys %s; the empty key holds %s of %d' % (w, list(T), type(T['']).__name__, len(T[''])))
        T = T['']
    rows = T[c - 1]; rows = rows if isinstance(rows, list) else [rows]
    for i, x in enumerate(rows): topic.append(('%s %d:%d' % (w.replace('_', ' '), c, i + 1), strip(x if isinstance(x, str) else ' '.join(x))))
    print('%s %d: %d rows; the first: %s' % (w, c, len(rows), strip(rows[0] if isinstance(rows[0], str) else ' '.join(rows[0]))[:120]))
# THE RANGES BY AMUD (segments; the first 90 characters of each amud's first row — the design chooses; the rest enumerated outside declared scope)
for wname, a, z in RANGES:
    TB = json.load(open(os.path.join(R, wname, 'en.json'), encoding='utf-8'))['text']
    for i in range(idx(a), idx(z) + 1):
        print('   %-14s %4s %3d  %s' % (wname, '%d%s' % (i // 2 + 1, 'ab'[i % 2]), len(TB[i]), strip(TB[i][0])[:90].replace('\n', ' ') if TB[i] else ''))
for wname in ('Tosefta_Sotah', 'Seder_Olam_Rabbah', 'Yerushalmi_Shekalim', 'Jerusalem_Talmud_Shekalim'):
    print('  export has %s: %s' % (wname, os.path.exists(os.path.join(R, wname, 'en.json'))))

prior = {}
own = {'deu_10_ekev_2026-09-19.md'}
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
