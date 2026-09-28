import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): THE MISHNAH ROWS THE LEDGER CITES (ch29_exam_rows.py's form over chapter 32 — the song; the Tosefta's rows read from the Tosefta export where the ledger names them) (computed from the reading's ledger by the citation regex — EVERY distinct citation,
# the count printed here and read at the design; the rows cited IN THE SPINE'S OWN HEBREW by name among them — Peah 1:1 at 336:2, Chagigah 1:8 at 335:1),
# each printed WHOLE from the export (Hebrew and English) for the reading at the design. ch29_exam_rows.py's form. Nothing typed: the list is the ledger's own count.
# A citation with no row in the Mishnah export is printed as such (a Jerusalem Talmud or Tosefta seat wearing a tractate's name). RUN FROM THE REPO ROOT.
import json, re, html, collections, subprocess, os
ROOT = _ROOT
L = open(ROOT + '/logic/oral_triage/deu_32_haazinu_2026-09-27.md', encoding='utf-8').read()
TR = r'(Tosefta Sotah|Tosefta Ketubot|Tosefta Shekalim|Makkot|Sotah|Sanhedrin|Bava Batra|Bekhorot|Parah|Yevamot|Negaim|Bava Kamma|Kiddushin|Shevuot|Niddah|Keritot|Chullin|Zevachim|Sukkah|Berakhot|Pesachim|Menachot|Temurah|Arakhin|Horayot|Avodah Zarah|Bava Metzia|Peah|Nedarim|Nazir|Ketubot|Gittin|Shabbat|Eruvin|Yoma|Rosh Hashanah|Taanit|Megillah|Moed Katan|Chagigah|Eduyot|Kelim|Oholot|Tohorot|Mikvaot|Zavim|Yadayim|Uktzin|Tamid|Middot|Kinnim|Meilah|Bikkurim|Orlah|Kilayim|Sheviit|Demai|Challah|Terumot|Maaser Sheni|Maasrot|Machshirin|Tevul Yom|Avot|Makhshirin|Shekalim)'
cites = collections.Counter(re.findall(TR + r' (\d+):(\d+)\b', L))
rows = sorted([(t, int(c), int(p), n) for (t, c, p), n in cites.items()], key=lambda x: (x[0], x[1], x[2]))
print('DISTINCT CITATIONS:', len(rows), '| cited at least twice:', sum(1 for r in rows if r[3] >= 2), '| the rows:', [(t, c, p, n) for t, c, p, n in rows])
# the seats of each citation in the ledger (the row lines that carry it — the spine's own Hebrew names Bikkurim etc. by name; the seat's line prefix printed)
for t, c, p, n in rows:
    seats = [m.start() for m in re.finditer(re.escape(f'{t} {c}:{p}') + r'\b', L)]
    pre = []
    for s in seats:
        ls = L.rfind('\n', 0, s) + 1
        pre.append(L[ls:ls + 60].replace('\n', ' '))
    print(f'  SEATS {t} {c}:{p}: {pre}')
def clean(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html.unescape(s))).strip()
def row(tr, c, p):
    d = f'{ROOT}/Data/sefaria_export/' + (('Tosefta_' + tr[8:].replace(' ', '_')) if tr.startswith('Tosefta ') else ('Mishnah_' + tr.replace(' ', '_')))
    if not os.path.isdir(d): return None
    he = json.load(open(f'{d}/he.json', encoding='utf-8')); en = json.load(open(f'{d}/en.json', encoding='utf-8'))
    g = lambda x: (x['text'] if isinstance(x, dict) and 'text' in x else x)
    H, E = g(he), g(en)
    if c - 1 >= len(H) or p - 1 >= len(H[c - 1]): return ('NO SUCH ROW IN THE EXPORT (chapters %d; chapter %d has %d rows)' % (len(H), c, len(H[c - 1]) if c - 1 < len(H) else 0), '')
    return clean(H[c - 1][p - 1]), clean(E[c - 1][p - 1])
tot = 0
for t, c, p, n in rows:
    r = row(t, c, p)
    if r is None: print('\n==== Mishnah %s %d:%d — NO EXPORT FOLDER ====' % (t, c, p)); continue
    he, en = r; tot += len(he) + len(en)
    print('\n==== Mishnah %s %d:%d (cited %d time%s by the ledger\'s rows) ====\nHE: %s\nEN: %s' % (t, c, p, n, '' if n == 1 else 's', he, en))
print('\nTOTAL CHARS', tot)

print('CHAPTER-ONLY CITATIONS (no paragraph — the Tosefta chapters the rows name):', sorted(set(re.findall(TR + r' (\d+)(?![:\d])', L))))
