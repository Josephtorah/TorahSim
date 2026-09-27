import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (2026-09-25): THE MISHNAH ROWS THE LEDGER CITES AT LEAST TWICE (computed from the reading's ledger by the citation regex — the three cited
# in the spine's own Hebrew among them: Makkot 2:8, Sotah 9:9, Sotah 9:2), each printed WHOLE from the export (Hebrew and English) for the reading at the design.
# Nothing typed: the list is the ledger's own count. RUN FROM THE REPO ROOT.
import json, re, html, collections, subprocess, os
ROOT = _ROOT
L = open(ROOT + '/logic/oral_triage/deu_19_21_shoftim_ki_teitzei_2026-09-24.md', encoding='utf-8').read()
TR = r'(Makkot|Sotah|Sanhedrin|Bava Batra|Bekhorot|Parah|Yevamot|Negaim|Bava Kamma|Kiddushin|Shevuot|Niddah|Keritot|Chullin|Zevachim|Sukkah|Berakhot|Pesachim|Menachot|Temurah|Arakhin|Horayot|Avodah Zarah|Bava Metzia|Peah|Nedarim|Nazir|Ketubot|Gittin|Shabbat|Eruvin|Yoma|Rosh Hashanah|Taanit|Megillah|Moed Katan|Chagigah|Eduyot|Kelim|Oholot|Tohorot|Mikvaot|Zavim|Yadayim|Uktzin|Tamid|Middot|Kinnim|Meilah|Bikkurim|Orlah|Kilayim|Sheviit|Demai|Challah|Terumot|Maaser Sheni|Maasrot|Machshirin|Tevul Yom|Avot|Makhshirin)'
cites = collections.Counter(re.findall(TR + r' (\d+):(\d+)\b', L))
rows = sorted([(t, int(c), int(p), n) for (t, c, p), n in cites.items() if n >= 2], key=lambda x: (x[0], x[1], x[2]))
print('CITED AT LEAST TWICE:', len(rows), '| distinct citations:', len(cites), '| the rows:', [(t, c, p, n) for t, c, p, n in rows])
def clean(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html.unescape(s))).strip()
def row(tr, c, p):
    d = f'{ROOT}/Data/sefaria_export/Mishnah_{tr.replace(" ", "_")}'
    he = json.load(open(f'{d}/he.json', encoding='utf-8')); en = json.load(open(f'{d}/en.json', encoding='utf-8'))
    g = lambda x: (x['text'] if isinstance(x, dict) and 'text' in x else x)
    return clean(g(he)[c - 1][p - 1]), clean(g(en)[c - 1][p - 1])
tot = 0
for t, c, p, n in rows:
    he, en = row(t, c, p); tot += len(he) + len(en)
    print('\n==== Mishnah %s %d:%d (cited %d times by the ledger\'s rows) ====\nHE: %s\nEN: %s' % (t, c, p, n, he, en))
print('\nTOTAL CHARS', tot)
