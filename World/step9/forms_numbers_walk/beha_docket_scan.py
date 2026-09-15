import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 3b — THE COMPILE OF BEHA'ALOTCHA (2026-09-10): THE EXAM DOCKET'S SCAN, sized by script before the docket is written.
# (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of
#     Numbers 8:1-26 + 10:1-12:16; (2) THE TOPIC ROWS: the Mishnah's rows named BY ADDRESS in the four reading ledgers' TESTING SHELF lines (the
#     answer sheet); the long Talmud ranges the ledgers name enter through (1) — their remainder is enumerated by count as OUTSIDE
#     DECLARED SCOPE in the docket's header. The dump is the docket script's input (write_beha_docket.py), as at Naso.
import json, re, os, collections
R = (_ROOT + '/Data/sefaria_export')
OUT = '<scratch>/beha_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(8, v) for v in range(1, 27)} | {(10, v) for v in range(1, 37)} | {(11, v) for v in range(1, 36)} | {(12, v) for v in range(1, 17)}
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
TOPIC = [('Mishnah_Menachot', [(3, 7), (4, 4)]), ('Mishnah_Tamid', [(3, 9), (6, 1), (7, 3)]), ('Mishnah_Chullin', [(1, 6)]), ('Mishnah_Arakhin', [(2, m) for m in range(3, 7)]),
         ('Mishnah_Rosh_Hashanah', [(3, m) for m in range(1, 9)] + [(4, m) for m in range(1, 10)]), ('Mishnah_Ta_anit', [(c, m) for c in (1, 2, 3) for m in range(1, 99)]),
         ('Mishnah_Sukkah', [(5, m) for m in range(1, 9)]), ('Mishnah_Yadayim', [(3, 5)]), ('Mishnah_Sanhedrin', [(1, m) for m in range(1, 7)]), ('Mishnah_Sotah', [(1, m) for m in range(7, 10)]),
         ('Mishnah_Bava_Kamma', [(2, 5)]), ('Mishnah_Negaim', [(2, m) for m in range(1, 6)] + [(3, m) for m in range(1, 3)]), ('Mishnah_Moed_Katan', [(3, 1), (3, 2)]), ('Mishnah_Berakhot', [(5, 5)]),
         ('Pirkei_Avot', [(5, 4)]), ('Mishnah_Bekhorot', [(1, 1)])]
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
RANGES = [('Menachot', '28a', '29a'), ('Menachot', '98b', '98b'), ('Shabbat', '22b', '22b'), ('Menachot', '61b', '62a'), ('Yoma', '24b', '25a'), ('Chullin', '24a', '24b'), ('Arakhin', '11a', '11b'),
          ('Bekhorot', '4a', '5a'), ('Sanhedrin', '17a', '17a'), ('Rosh_Hashanah', '26b', '27a'), ('Rosh_Hashanah', '32a', '32a'), ('Rosh_Hashanah', '33b', '34a'), ('Taanit', '14a', '16b'), ('Sukkah', '53b', '54b'),
          ('Nedarim', '78a', '78a'), ('Shabbat', '115b', '116a'), ('Yevamot', '64a', '64a'), ('Zevachim', '116a', '116a'), ('Sotah', '35a', '35a'), ('Yoma', '75a', '76a'), ('Chullin', '27b', '27b'), ('Arakhin', '15a', '16b'),
          ('Taanit', '9a', '9a'), ('Shabbat', '130a', '130a'), ('Shabbat', '87a', '87a'), ('Shabbat', '97a', '97a'), ('Yevamot', '49b', '49b'), ('Berakhot', '34a', '34a'), ('Bava_Kamma', '25a', '25a'),
          ('Sotah', '9b', '13a'), ('Zevachim', '101b', '102a'), ('Moed_Katan', '7b', '7b'), ('Nedarim', '38a', '38a'), ('Chullin', '89a', '89a'), ('Taanit', '29a', '29a')]
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
