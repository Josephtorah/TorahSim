import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 2b — THE COMPILE OF NASO (2026-09-10): THE EXAM DOCKET'S SCAN, sized by script before the docket is written.
# (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of
#     Numbers 4:21-7:89; (2) THE TOPIC ROWS: the Mishnah's rows named BY ADDRESS in the seven reading ledgers' TESTING SHELF lines (the
#     answer sheet); the long Talmud ranges the ledgers name enter through (1) — their remainder is enumerated by count as OUTSIDE
#     DECLARED SCOPE in the docket's header. The dump is the docket script's input (write_naso_docket.py), as at Bamidbar.
import json, re, os, collections
R = (_ROOT + '/Data/sefaria_export')
OUT = '<scratch>/naso_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(4, v) for v in range(21, 50)} | {(5, v) for v in range(1, 32)} | {(6, v) for v in range(1, 28)} | {(7, v) for v in range(1, 90)}
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
    if not cats or cats[0] not in ('Talmud', 'Mishnah', 'Tosefta') or 'Yerushalmi' in cats or 'Commentary' in cats or '_on_' in w: continue   # the three exam shelves only — no commentaries
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

# ---- THE TOPIC ROWS BY ADDRESS: the Mishnah chapters and mishnayot the ledgers name (the answer sheet) ----
TOPIC = [('Mishnah_Sotah', [(c, m) for c in range(1, 7) for m in range(1, 99)] + [(7, 1), (7, 6), (9, 9)]),
         ('Mishnah_Nazir', [(c, m) for c in range(1, 10) for m in range(1, 99)]),
         ('Mishnah_Bava_Kamma', [(9, m) for m in range(5, 13)]),
         ('Mishnah_Nedarim', [(1, 1)]), ('Mishnah_Niddah', [(5, 6)]), ('Mishnah_Kinnim', [(1, 1), (2, 5)]), ('Mishnah_Eduyot', [(5, 6)]),
         ('Mishnah_Parah', [(1, 3), (6, 1)]), ('Mishnah_Tamid', [(7, 2)]), ('Mishnah_Megillah', [(4, m) for m in range(3, 8)]),
         ('Mishnah_Terumot', [(4, 5)]), ('Mishnah_Maaser_Sheni', [(5, m) for m in range(1, 6)]), ('Mishnah_Kelim', [(1, m) for m in range(5, 10)]),
         ('Mishnah_Sanhedrin', [(6, 2)]), ('Mishnah_Makkot', [(3, m) for m in range(1, 99)]), ('Mishnah_Tahorot', [(c, m) for c in (4, 5, 6) for m in range(1, 99)])]
topic = []
linked = {a for a, _, _ in link}
for w, cells in TOPIC:
    d = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))
    T = d['text']
    for c, m in cells:
        if c - 1 < len(T) and m - 1 < len(T[c - 1]):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
print('TOPIC rows %d (Mishnah, by address; link-duplicates dropped)' % len(topic))
print('  ', collections.Counter(a.rsplit(' ', 1)[0] for a, _ in topic))

# ---- THE LONG TALMUD RANGES the ledgers name: sized (their link hits counted; the remainder OUTSIDE by count) ----
RANGES = [('Sotah', '2a', '31a'), ('Sotah', '37b', '40a'), ('Nazir', '2a', '66b'), ('Bava_Kamma', '103a', '111a'), ('Pesachim', '67a', '68a'), ('Yoma', '3b', '4b'),
          ('Berakhot', '19b', '20a'), ('Nazir', '47b', '48b'), ('Nazir', '60a', '61a'), ('Menachot', '90b', '91a'), ('Nedarim', '9b', '10a'), ('Eruvin', '83a', '83b'),
          ('Sotah', '28a', '29a'), ('Shevuot', '35b', '36a'), ('Kiddushin', '27b', '28a'), ('Menachot', '59a', '59b')]
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
print('THE LONG RANGES (segments in the range; of them link rows):')
for w, a, z in RANGES:
    T = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    n = sum(len(T[i]) for i in range(idx(a), min(idx(z), len(T) - 1) + 1))
    l = sum(1 for ad, _, _ in link if ad.startswith(w.replace('_', ' ') + ' ') and idx(a) <= idx(re.match(r'.* (\d+[ab]):', ad).group(1)) <= idx(z))
    print('  %-12s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d\n\n' % (len(link) + len(topic), len(link), len(topic)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s\n%s\n\n' % (a, ' '.join(hits), t))
    for a, t in topic:
        f.write('## [TOPIC] %s  \n%s\n\n' % (a, t))
print('dump', OUT, os.path.getsize(OUT), 'bytes')
