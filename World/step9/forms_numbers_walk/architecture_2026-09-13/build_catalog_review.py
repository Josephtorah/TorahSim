#!/usr/bin/env python3
# FUNCTION_CATALOG.md REBUILT (2026-09-13; the standing order of #165, sitting C; RERUN the same evening at THE PROJECT REVIEW, finding 18,
# on the owner's "Yes": the fourteen hand-written cards of 2026-09-05 no longer kept — their Score lines had aged as later spans called
# their engines — so ALL FIFTY-SEVEN cards are GENERATED from the instruments; the fourteen keep only their 2026-09-05 titles) — catalog_facts.json (the score, fractions and ledger-ops lines the
# runner printed today; the effects its source names; its python imports), runner_heads.json (the runner's own header and its
# daemon's docstring, cut), DEPENDENCY_INDEX.md (the span, the live calls) and DAEMON_INDEX.md (the daemon's row). The cards are
# ordered by the scroll and renumbered. Nothing typed by hand but the section prose.
import json, re, os, glob
ROOT = '<repo-old>'
SP = '<scratch>/'
facts = json.load(open(ROOT + '/ARCHITECTURE/catalog_facts.json', encoding='utf-8'))
heads = json.load(open(SP + 'runner_heads.json', encoding='utf-8'))
old = open(ROOT + '/ARCHITECTURE/FUNCTION_CATALOG.md', encoding='utf-8').read()
dep = open(ROOT + '/World/step9/DEPENDENCY_INDEX.md', encoding='utf-8').read()
dmn = open(ROOT + '/World/step9/DAEMON_INDEX.md', encoding='utf-8').read()

# ---- the indexes ----
spans, calls = {}, {}
for s in re.split(r'\n(?=## cold_run_)', dep):
    m = re.match(r'## (cold_run_\w+)\.py — (.*)', s.split('\n', 1)[0])
    if not m: continue
    spans[m.group(1)] = m.group(2).strip()
    co = re.search(r'- calls out \(live\): (.*)', s); calls[m.group(1)] = co.group(1).strip() if co else 'none'
daemons = {}
for m in re.finditer(r'^- (law_\w+) \((cold_run_\w+|world_engine)\.py; wraps (.*?)\): (\d+) kinds; given_at ([^,]+), installed_by (\w+)', dmn, re.M | re.S):
    daemons.setdefault(m.group(2), []).append((m.group(1), m.group(4), m.group(5), m.group(6)))

# ---- the old cards: only their TITLES are kept (harvested from the file as it stands), every body regenerated ----
old_titles = {}
for m in re.finditer(r'^### \d+\. (cold_run_\w+)\.py — (.*?)\n', old, re.M):
    old_titles[m.group(1).replace('cold_run_', '')] = m.group(2).strip()
old_cards = {}
tail = old[old.index('## Reading the fractions together'):]

HELPERS = {'strip', 'verse_text', 'words', 'raw_words', 'ink', 'move', 'dat', 'hyp', 'out', 'seats', 'tok', 'lemma_seats', 'lemma_tokens', 'N', 'O',
           'seats_of', 'rx', 'name_census', 'kit_order', 'sources', 'delta', 'prince_of', 'lemma_has', 'verse_facts', 'para_outcome', 'put',
           'scene', 'narrative', 'main', 'watches_day', 'hearing_due', 'first_verse', 'lint', 'run', 'grade', 'check', 'assert_seats', 'has_lemma'}
DOCKETS = {'bamidbar': 'num_01_04_bamidbar_exam', 'naso': 'num_04_07_naso_exam', 'beha': 'num_08_12_beha_exam', 'shelach': 'num_13_15_shelach_exam',
           'korach': 'num_16_18_korach_exam', 'chukat': 'num_19_21_chukat_exam', 'balak': 'num_22_25_balak_exam', 'second_census': 'num_26_second_census_exam',
           'musafim': 'num_28_29_musafim_exam', 'vows': 'num_30_vows_exam', 'midian': 'num_31_midian_exam', 'gad_reuben': 'num_32_gad_reuben_exam',
           'journeys': 'num_33_journeys_exam', 'borders': 'num_34_borders_exam', 'refuge': 'num_35_refuge_cities_exam', 'pesach_sheni': 'num_09_pesach_sheni_exam',
           'mekoshesh': 'num_15_mekoshesh_exam', 'zelophehad': 'num_27_inheritance_exam'}
def docket_rows(short):
    f = DOCKETS.get(short)
    if not f: return None
    ps = glob.glob(ROOT + '/logic/oral_triage/%s_*.md' % f)
    if not ps: return None
    t = open(ps[0], encoding='utf-8').read()
    return (os.path.basename(ps[0]), sum(1 for l in t.split('\n') if l.startswith('- ')))

def book_key(name):
    sp = spans.get(name, '')
    b = sp.split(' ')[0] if sp else 'ZZZ'
    order = {'Gen': 0, 'Exod': 1, 'Lev': 2, 'Num': 3}.get(b, 9)
    m = re.match(r'\w+ (\d+):(\d+)', sp)
    return (order, int(m.group(1)) if m else 999, int(m.group(2)) if m else 999, name)

def cut(s, n):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' …'

TITLES = {
 'pre_sinai': "the pre-Sinai code: the day boundary, the Noahide laws, circumcision", 'primeval': "from Eden to Hagar, the story on the engine",
 'mamre': "from Mamre to the heap, the story on the engine", 'family': "the family code: purchase, commission, the sinew, the levirate, inheritance",
 'joseph': "from the ford to the coffin, the story on the engine", 'exodus_story': "the exodus story, Exodus 1-19 on the engine",
 'ordinances': "the rest of the ordinances", 'mishpatim_3': "the Exodus law's five case heads",
 'sanctuary_build': "the sanctuary spec graded against its construction run", 'vestments': "the vestments' spec graded against their run",
 'incense_shekel': "the investiture, the incense altar, the half shekel and the Sabbath's law layer",
 'erection': "the covenant, the calf, the donation, and the erection as the spec's run", 'minchah': "the meal offering and the bird burnt offering",
 'chatat': "the sin offering rank tree and the priest's table", 'shemini_day': "the eighth day, the run of Leviticus 1-4's spec",
 'clocks': "the impurity clocks and the pairs engine", 'metzora': "the leper's cleansing", 'sanctions': "blood, unions and sanctions",
 'holiness': "the holiness ledger, first half", 'holiness_b': "the holiness ledger, second half", 'priesthood': "the priesthood and its dues",
 'yovel': "the jubilee engine", 'temurah': "consecration, substitution and devotion", 'tochacha': "the covenant cascade",
 'bamidbar': "the census, the camp, the Levites, the firstborn, the Kohathites' burden",
 'naso': "the work-count, the camp's purity, the trespass, the suspected wife, the nazirite, the blessing, the dedication",
 'beha': "the lamps, the Levites' rite, the trumpets, the march, Taberah and the quail, the seventy, Miriam",
 'pesach_sheni': "the second Passover, the tent's second case", 'shelach': "the spies, the decree, the libations, the stranger, the dough, the error and the high hand",
 'mekoshesh': "the wood-gatherer, the tent's third case", 'korach': "the rebellion, the plague and the staffs, the watch, the gifts and the tithe",
 'chukat': "the red heifer, Meribah, Edom, Aaron's death, Arad, the serpents, Sihon and Og", 'balak': "Balak and Balaam, Peor, Phinehas, the Midian command",
 'second_census': "the second census and the population table", 'zelophehad': "the daughters of Zelophehad, the tent's fourth case",
 'musafim': "the offerings calendar", 'vows': "the vows", 'midian': "the war on Midian", 'gad_reuben': "Gad and Reuben's stipulation and grant",
 'journeys': "the journeys", 'borders': "the borders", 'refuge': "the Levite cities and the cities of refuge", 'sequence': "the sequential run, the tape",
}

for k, v in old_titles.items():
    TITLES.setdefault(k, v)

def cut_safe(s, n):
    """cut at n, but never inside a Hebrew phrase before its gloss: extend to the closing parenthesis after the last Hebrew run"""
    s = re.sub(r'\s+', ' ', s or '').strip()
    if len(s) <= n: return s
    c = s[:n].rsplit(' ', 1)[0]
    if re.search(r'[\u0590-\u05FF]', c):
        i = s.find(')', len(c) - 1)
        if i != -1 and i - len(c) < 200: c = s[:i + 1]
    return c + ' …'

def gen_card(name):
    short = name.replace('cold_run_', '')
    f = facts['spans'].get(name, {}); h = heads.get(name, {})
    header = re.sub(r'^!/usr/bin/env python3\s*', '', h.get('header', '')).strip()
    desc = h.get('doc') or header
    title = TITLES.get(short, cut(re.sub(r'^cold_run_\w+\.py — ', '', re.split(r'\s+\(', desc, 1)[0]), 120))
    cells = [d for d in h.get('defs', []) if d not in HELPERS and not d.startswith('_') and not d.startswith('law_')]
    dlist = daemons.get(name, [])
    lines = []
    lines.append('### %%N. %s.py — %s\n' % (name, title))
    lines.append('- **Span and compile.** %s. %s' % (spans.get(name, 'the tape') if spans.get(name) else 'The tape itself — every runner\'s lines in verse order on one world', cut_safe(desc, 560)))
    if cells:
        lines.append('- **Functions.** %s.' % ', '.join('`%s`' % c for c in cells[:24]) + (' — and %d more.' % (len(cells) - 24) if len(cells) > 24 else ''))
    for dn, doc in h.get('daemons', {}).items():
        lines.append('- **The daemon `%s`.** %s' % (dn, cut_safe(doc, 420)))
    if f.get('score_line'): lines.append('- **Score (rerun 2026-09-13).** %s' % f['score_line'])
    if f.get('fractions_line'): lines.append('- **Provenance.** %s' % f['fractions_line'])
    if f.get('ledger_ops_line'): lines.append('- **Ledger ops.** %s' % f['ledger_ops_line'].replace('LEDGER OPS this span writes: ', '').replace('LEDGER OPS this run writes: ', ''))
    effs = f.get('effects_named_in_source', [])
    if effs: lines.append('- **Effects named in the source.** %s%s' % (', '.join(effs[:36]), ' — and %d more' % (len(effs) - 36) if len(effs) > 36 else '') + '.')
    lines.append('- **Imports.** Calls out (live, the dependency gate): %s.' % calls.get(name, 'none'))
    if h.get('moves'): lines.append('- **Moves.** %s.' % ', '.join(h['moves']))
    for dn, kinds, given, inst in dlist:
        lines.append('- **Engine.** `%s` watches %s kinds; given at %s, installed by %s.' % (dn, kinds, given, inst))
    dr = docket_rows(short)
    if dr: lines.append('- **Docket.** `logic/oral_triage/%s` — %d entries, built by the union rule.' % dr)
    return '\n'.join(lines) + '\n'

names = sorted(facts['spans'].keys(), key=book_key)
BOOK_TITLE = {0: 'Genesis', 1: 'Exodus', 2: 'Leviticus', 3: 'Numbers', 9: 'The tape'}
out = []
head = """# FUNCTION CATALOG — one card per compiled span

Fifty-seven files in `World/step9/` compile law spans and story
stretches cold from the ink and grade themselves against the Mishnah's
rows and the union-rule dockets. Written 2026-09-05 with fourteen cards;
brought to the fourth book 2026-09-13, and the same evening, at the
project review, the fourteen cards of 2026-09-05 were regenerated too —
their scores had aged as later spans called their engines — so every one
of the fifty-seven cards is BUILT FROM THE INSTRUMENTS — `catalog_facts.json`
(rerun today over every runner: the score, provenance and ledger-ops
lines each printed, the effects its source names, its imports), the
runner's own header and its daemon's docstring, the dependency gate's
index (the span, the live calls) and the daemon gate's index (the
daemon's row). Nothing in a card was typed by hand but its title. Verse
numbering is the Hebrew numbering the word database uses.

**Card fields.** Span and compile: the verses, and the runner's own
account of what it compiles. Functions: the cells the file defines.
The daemon: the wrapper's own docstring. Score: the printed matrix line.
Provenance: how many cells come from ink, from a named recorded move,
from data, from routing or import. Ledger ops: what the run writes.
Effects: the registry effects the source names. Imports: the live calls
the gate verified. Moves: the catalog moves the file's labels name.
Engine: the daemon's row. Docket: the portion's answer table.

**Provenance vocabulary.** INK: read from the span's own tokens. MOVE or
RECORDED: a recorded argument replayed with its source row. DATA: a
transmitted quantity the ink leaves unstated. FENCE: a rabbinic boundary
the answer sheet itself labels. ROUTED: an input class filed onto an
existing branch as the answer sheet files it. IMPORT: a rule from another
span or book. H: a hypothesis, counted apart and never as compiled.

Totals across the fifty-seven: 427 compiled functions wrapped as 62
daemons, 6,378 graded cells, all matching on the latest sweep
(`run_cold_all` 57/57, 2026-09-13).

---
"""
out.append(head)
n = 0; cur = None
reverified = []
for name in names:
    b = book_key(name)[0]
    if b != cur:
        cur = b; out.append('\n## %s\n' % BOOK_TITLE[b])
    n += 1
    if name in old_cards:
        title, body = old_cards[name]
        out.append('### %d. %s.py — %s\n%s' % (n, name, title, body))
        sl = facts['spans'][name].get('score_line')
        reverified.append((name, sl))
    else:
        out.append(gen_card(name).replace('%N', str(n)))
out.append('\n## The fourteen cards of 2026-09-05\n\nThe cards for pesach, decalogue, mishpatim, mishpatim_2, guardians, calendar, offerings, vayikra5, tzav, shemini, negaim, yoma, moadim and lev24 were written by hand on 2026-09-05 and kept verbatim when the catalog was brought to the fourth book; the project review of 2026-09-13 (reviews/REVIEW_project_2026-09-13.md, finding 18) found thirteen of their Score lines aged — the cells had grown as later spans called these engines (calendar 14 to 17, tzav 33 to 54, offerings 40 to 58) — so on the owner\'s word they were regenerated by the same script as the other forty-three, keeping their titles. The 2026-09-05 prose stands in git history at commit 632790c.\n')
out.append('\n' + tail)
text = ''.join(out)
JARGON = {'patach': 'the vowel point', 'sheva': 'the vowel point', 'qamats': 'the vowel point', 'qamatz': 'the vowel point', 'hiriq': 'the vowel point',
          'chiriq': 'the vowel point', 'tsere': 'the vowel point', 'tzere': 'the vowel point', 'segol': 'the vowel point', 'cholam': 'the vowel point',
          'dagesh': 'the doubling dot', 'midrash': 'the rabbinic reading', 'word-database': 'the lemma database', 'etnachta': 'the mid-verse pause', 'tevir': 'the accent', 'maqqef': 'the joining stroke', 'wayyiqtol': 'the narrative verb form'}
for j, g in JARGON.items():
    text = re.sub(r'\b(%s)\b(?!\s*\()' % j, r'\1 (%s)' % g, text)
open(os.environ.get('CATALOG_OUT', ROOT + '/ARCHITECTURE/FUNCTION_CATALOG.md'), 'w', encoding='utf-8').write(text)
print('written', len(text.split('\n')), 'lines; cards', n, '; generated', n - len(reverified), '; old kept', len(reverified))
