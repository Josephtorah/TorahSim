import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9 (2026-09-19): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch8_docket_scan.py's form on chapter 9). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose
# English cites a verse of Deuteronomy 9 (the export's chapter 9 = the DB's — the identity, asserted at the reading); (2) THE TOPIC ROWS by address
# (the union rule; COMPILE_DEBT's sitting-6 box (n)): the CANDIDATE ranges SIZED here, the design choosing which are read whole — Mishnah Berakhot 6-7
# whole, Mishnah Bikkurim 1; Berakhot 5a, 20b-21a, 35a-35b, 41a-44a, 48b-49b; Yoma 74b-76a; Sotah 4b-5a; Makkot 13b; Eruvin 96a; (3) THE PRIOR READS
# credited (the Numbers walk's and the earlier dockets' Berakhot rows among them).
import json, re, os, collections, glob, subprocess
ROOT = _ROOT
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ch9_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
CITE = re.compile(r'(?:Deuteronomy|Deut\.?|Dt\.?) ?(\d+):(\d+)(?:[-–](\d+))?')
CH, NV = 9, 29

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
mishnah_chapters('Mishnah_Avodah_Zarah', [3])
mishnah_rows('Mishnah_Ta_anit', [(4, 6), (4, 7)])
mishnah_rows('Pirkei_Avot', [(5, 4), (5, 6)])
mishnah_rows('Mishnah_Megillah', [(4, 10)])
mishnah_rows('Mishnah_Yoma', [(8, 8), (8, 9)])
RANGES = [('Taanit', '26a', '26a'), ('Berakhot', '32a', '32b'), ('Berakhot', '7a', '7a'), ('Shabbat', '87a', '89a'), ('Menachot', '99a', '99b'), ('Bava_Batra', '14b', '14b'), ('Taanit', '28b', '29a'),
          ('Avodah_Zarah', '43b', '44a'), ('Sanhedrin', '102a', '102a'), ('Beitzah', '25b', '25b'), ('Shabbat', '55a', '55a'), ('Arakhin', '15a', '15a'), ('Yoma', '86b', '86b')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))
# THE MIDRASHIM NAMED IN THE BOX (Vayikra Rabbah 10:5 — Aaron's sons; Devarim Rabbah 2:1 — the ten names of prayer): sized if the export holds them
for w, c, m in (('Vayikra_Rabbah', 10, 5), ('Devarim_Rabbah', 2, 1), ('Seder_Olam_Rabbah', 6, 0)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): print('MIDRASH NOT IN THE EXPORT:', w); continue
    T = json.load(open(p, encoding='utf-8'))['text']
    if isinstance(T, dict): T = list(T.values())   # Seder Olam Rabbah's chapters keyed by name in the export
    try: seg = T[c - 1][m - 1] if m else T[c - 1]; rows = seg if isinstance(seg, list) else [seg]
    except Exception as e: print('MIDRASH RANGE', w, c, m, e); continue
    for i, s in enumerate(rows): topic.append((('%s %d:%d' % (w.replace('_', ' '), c, i + 1)) if not m else ('%s %d:%d:%d' % (w.replace('_', ' '), c, m, i + 1) if len(rows) > 1 else '%s %d:%d' % (w.replace('_', ' '), c, m)), strip(s)))
    print('%s %d:%d: %d rows' % (w, c, m, len(rows)))
# THE AMUDIM OF Shabbat 86b-89b SIZED ONE BY ONE (the giving's chapter — R. Yosei's days, the forty days; the design chooses; the rest enumerated outside declared scope)
TB = json.load(open(os.path.join(R, 'Shabbat', 'en.json'), encoding='utf-8'))['text']
print('SHABBAT 86b-89b BY AMUD (segments; the first 90 characters of each amud):')
for i in range(idx('86b'), idx('89b') + 1):
    print('   %4s %3d  %s' % ('%d%s' % (i // 2 + 1, 'ab'[i % 2]), len(TB[i]), strip(TB[i][0])[:90].replace('\n', ' ') if TB[i] else ''))
TY = json.load(open(os.path.join(R, 'Berakhot', 'en.json'), encoding='utf-8'))['text']
print('BERAKHOT 32a-32b BY AMUD: %s' % [('%d%s' % (i // 2 + 1, 'ab'[i % 2]), len(TY[i])) for i in range(idx('32a'), idx('32b') + 1)])

prior = {}
own = {'deu_09_ekev_2026-09-19.md'}
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
