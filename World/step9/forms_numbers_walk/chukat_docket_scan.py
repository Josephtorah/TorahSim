import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 6b — THE COMPILE OF CHUKAT (2026-09-11): THE EXAM DOCKET'S SCAN, sized by script before the docket is written.
# (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of
#     Numbers 19:1-21:35; (2) THE TOPIC ROWS: the Mishnah's rows named BY ADDRESS in the three reading ledgers' TESTING SHELF lines and the
#     COMPILE_DEBT box — Parah whole, Oholot whole, Kelim 1-2 and 9-10, Mikvaot 1-2, Keritot 1, Shevuot 1-2, Eduyot 1:14 and 6:2-3, Rosh
#     Hashanah 3:8, Avot 5:6 — and the two Seder Olam Rabbah segments the ledgers name (9:2, 10:2 — the fortieth year's chronology, the
#     Midrash shelf; the long Talmud ranges the ledgers name enter through (1), their remainder enumerated by count as OUTSIDE DECLARED
#     SCOPE in the docket's header). (3) THE PRIOR READS: every address already verdicted in an earlier logic/oral_triage ledger (this
#     sitting's own three reading ledgers excluded) is listed as CREDITED with its ledger — speed ruling (b), credit guard (1): a quick look,
#     not a blind credit. The dump is the docket script's input (write_chukat_docket.py), as at Korach.
import json, re, os, collections, glob
R = (_ROOT + '/Data/sefaria_export')
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/chukat_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(19, v) for v in range(1, 23)} | {(20, v) for v in range(1, 30)} | {(21, v) for v in range(1, 36)}
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
def whole(w, chapters=None):
    T = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    chs = chapters or range(1, len(T) + 1)
    return [(c, m) for c in chs if c - 1 < len(T) for m in range(1, len(T[c - 1]) + 1)]
TOPIC = [('Mishnah_Parah', whole('Mishnah_Parah')), ('Mishnah_Oholot', whole('Mishnah_Oholot')), ('Mishnah_Kelim', whole('Mishnah_Kelim', [1, 2, 9, 10])),
         ('Mishnah_Mikvaot', whole('Mishnah_Mikvaot', [1, 2])), ('Mishnah_Keritot', whole('Mishnah_Keritot', [1])), ('Mishnah_Shevuot', whole('Mishnah_Shevuot', [1, 2])),
         ('Mishnah_Eduyot', [(1, 14), (6, 2), (6, 3)]), ('Mishnah_Rosh_Hashanah', [(3, 8)]), ('Pirkei_Avot', [(5, 6)])]
topic = []
linked = {a for a, _, _ in link}
for w, cells in TOPIC:
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); continue
    d = json.load(open(p, encoding='utf-8'))
    T = d['text']
    for c, m in cells:
        if c - 1 < len(T) and m - 1 < len(T[c - 1]):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
# the two Seder Olam segments (the Midrash shelf — named by the ledgers; the export's text is a dict keyed '' after an empty Introduction)
SO = json.load(open(os.path.join(R, 'Seder_Olam_Rabbah', 'en.json'), encoding='utf-8'))['text']['']
for ch, i in ((9, 2), (10, 2)):
    t = strip(SO[ch - 1][i - 1])
    t = re.sub(r'\d(?:Guggenheimer|R\. Jacob Emdin|R\. Eliyahu from Vilna|The meaning here)[^.]*(?:\.[^.]*){0,12}?\.\s{2}', ' ', t)   # the translator's footnotes trimmed where they run to a double space; the row is read whole in the dump
    topic.append(('Seder Olam Rabbah %d:%d' % (ch, i), strip(SO[ch - 1][i - 1])))
print('TOPIC rows %d (Mishnah by address + Seder Olam 9:2, 10:2; link-duplicates dropped)' % len(topic))
print('  ', collections.Counter(a.rsplit(' ', 1)[0] for a, _ in topic))

# ---- THE PRIOR READS: addresses already verdicted in an earlier ledger (this sitting's three reading ledgers excluded) ----
prior = {}
own = {'num_19_parah_2026-09-11.md', 'num_20_meribah_edom_aaron_2026-09-11.md', 'num_21_snakes_conquest_2026-09-11.md'}
for f in sorted(glob.glob((_ROOT + '/logic/oral_triage/*.md'))):
    if os.path.basename(f) in own: continue
    txt = open(f, encoding='utf-8').read()
    for a in list(linked) + [a for a, _ in topic]:
        if re.search(r'(^|[^\w])' + re.escape(a) + r'(?![\d:])', txt, re.M):
            prior.setdefault(a, []).append(os.path.basename(f))
print('PRIOR READS (credited): %d addresses' % len(prior))
for a, fs in sorted(prior.items()): print('   %-32s %s' % (a, ', '.join(fs)[:120]))

# ---- THE LONG TALMUD RANGES the ledgers name: sized (their link hits counted; the remainder OUTSIDE by count) ----
RANGES = [('Yoma', '2a', '8b'), ('Yoma', '14a', '14a'), ('Yoma', '42b', '43b'), ('Zevachim', '93a', '93b'), ('Menachot', '27a', '27a'), ('Menachot', '51b', '52a'), ('Chullin', '11a', '11a'), ('Chullin', '25a', '25a'),
          ('Chullin', '71b', '72b'), ('Chullin', '128b', '129b'), ('Pesachim', '14b', '19b'), ('Nazir', '42b', '43a'), ('Nazir', '53b', '54a'), ('Berakhot', '19b', '19b'), ('Sotah', '16b', '16b'), ('Yevamot', '72b', '74b'),
          ('Rosh_Hashanah', '31a', '31a'), ('Taanit', '9a', '9a'), ('Shabbat', '35a', '35a'), ('Rosh_Hashanah', '3a', '3a'), ('Moed_Katan', '28a', '28a'), ('Yoma', '86b', '86b'), ('Sanhedrin', '101b', '101b'), ('Bava_Batra', '17a', '17a'),
          ('Bekhorot', '5b', '5b'), ('Sotah', '13b', '14a'), ('Sanhedrin', '110a', '110a'), ('Yoma', '75a', '75a'), ('Megillah', '14a', '14a'), ('Berakhot', '54a', '54b'), ('Avodah_Zarah', '44a', '44a'), ('Chullin', '6b', '7a'),
          ('Pesachim', '56a', '56a'), ('Bava_Batra', '14b', '14b'), ('Nedarim', '55a', '55a'), ('Eruvin', '54a', '54a'), ('Avodah_Zarah', '25a', '25a'), ('Chullin', '60b', '60b'), ('Gittin', '38a', '38a'), ('Bava_Kamma', '38b', '38b'),
          ('Niddah', '24b', '24b'), ('Niddah', '61a', '61a'), ('Sanhedrin', '91b', '91b')]
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
print('THE LONG RANGES (segments in the range; of them link rows):')
for w, a, z in RANGES:
    T = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    n = sum(len(T[i]) for i in range(idx(a), min(idx(z), len(T) - 1) + 1))
    l = sum(1 for ad, _, _ in link if ad.startswith(w.replace('_', ' ') + ' ') and idx(a) <= idx(re.match(r'.* (\d+[ab]):', ad).group(1)) <= idx(z))
    print('  %-12s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes')
