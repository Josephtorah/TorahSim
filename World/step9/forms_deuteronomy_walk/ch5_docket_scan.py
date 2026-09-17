import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5 (2026-09-16): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch4_docket_scan.py's form on chapter 5). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports
# whose English cites a verse of Deuteronomy 5 — THE CITATIONS ARE THE EXPORT'S NUMBERS (Sefaria's Deuteronomy 5 has thirty verses; the DB
# thirty-three — sitting 3's alignment: 1-16 = 1-16, 17 = 17-20, 18 = 21, 19-30 = 22-33) and are MAPPED to the DB's verses here, the export's
# number kept beside; (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-3 box (j)): Mishnah Shevuot 3:8-9; Shabbat 88a;
# Sanhedrin 17a; Makkot 24a; Berakhot 12a; Kiddushin 30b-31b; Sanhedrin 86a; Bava Metzia 5b; Yoma 4b; Sotah 37b; (3) THE PRIOR READS credited
# (the Decalogue exam's ledger exodus_block_decalogue_2026-09-04.md among them).
import json, re, os, collections, glob, subprocess
ROOT = _ROOT
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ch5_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
EXP2DB = {e: [e] for e in range(1, 17)}; EXP2DB[17] = [17, 18, 19, 20]; EXP2DB[18] = [21]
for e in range(19, 31): EXP2DB[e] = [e + 3]
assert sorted(v for vs in EXP2DB.values() for v in vs) == list(range(1, 34))
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
exp_cited = collections.Counter()
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
        hits = []; exps = []
        for m in CITE.finditer(t):
            c, a, z = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2))
            if c != 5: continue
            for e in range(a, min(z, a + 60) + 1):
                if e in EXP2DB:
                    exps.append(e); exp_cited[e] += 1
                    hits += ['Deut 5:%d' % v for v in EXP2DB[e]]
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), sorted(set(exps)), t))
            works[w] += 1
print('SCANNED %d works (Talmud / Mishnah / Tosefta, no Yerushalmi, no commentary); the forms: Deuteronomy c:v, Deut. c:v, Dt.c:v; chapter 5 only' % scanned)
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))
print('  the EXPORT verses cited: %s' % sorted(exp_cited.items()))
print('  the DB verses cited: %s' % collections.Counter(h for _, hs, _, _ in link for h in hs).most_common(80))
for a, hs, es, t in link: print('  LINK %-26s exp %-8s %-22s %s' % (a, ','.join(str(e) for e in es), ' '.join(hs), t[:150].replace('\n', ' ')))
# THE DIVISION CHECK: a row citing the export's 17 or 18 must quote a short commandment or the covet clause; a row citing 5:12 the sabbath
print('  DIVISION CHECK — rows citing the export\'s 17 (the four short words) and 18 (covet): %s' % [(a, t[:100]) for a, hs, es, t in link if 17 in es or 18 in es][:8])

def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _, _ in link}
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
mishnah_rows('Mishnah_Shevuot', [(3, 8), (3, 9)])
mishnah_rows('Mishnah_Sanhedrin', [(7, 6)])   # THE DESIGN'S (b): the second word's own answer sheet — the idolater's acts
RANGES = [('Shabbat', '88a', '88a'), ('Sanhedrin', '17a', '17a'), ('Makkot', '24a', '24a'), ('Berakhot', '12a', '12a'), ('Kiddushin', '30b', '31b'), ('Sanhedrin', '86a', '86a'), ('Bava_Metzia', '5b', '5b'), ('Yoma', '4b', '4b'), ('Sotah', '37b', '37b'),
          ('Sanhedrin', '60b', '60b')]   # THE DESIGN'S (b): the four services — the second word's rows, read where the debt is paid
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))

prior = {}
own = {'deu_05_vaetchanan_2026-09-16.md'}
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
    for a, hits, es, t in link:
        f.write('## [LINK] %s  %s (export %s)%s\n%s\n\n' % (a, ' '.join(hits), ','.join(str(e) for e in es), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes', sum(1 for _ in open(OUT, encoding='utf-8')), 'lines')
print('THE RANGES SIZED:')
for w, a, z, n, l in SIZES: print('  %-14s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))
