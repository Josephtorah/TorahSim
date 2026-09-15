import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE ARCHITECTURE TOOLS TAUGHT THE FOURTH BOOK (2026-09-13; the standing order of #165, sitting D). Every replacement asserted;
# refuses to run twice. build_summary's BLOCKS gain ten Numbers rows (numbers_blocks.txt); build_program_outline's BOOK / COMPILED /
# by_book / loops / anchors / dates; build_plain_outline's loops / anchors / dates; build_linked's BOOK_REPORTS / PARASHAH_GLOSS /
# anchors / date; build_diagrams' typed layer numbers and a new 08_numbers_runners.svg; NARRATIVE.md's ten blocks appended.
import re, json, os
A = (_ROOT + '/ARCHITECTURE/')
SP = '<scratch>/'

def load(p): return open(p, encoding='utf-8').read()
def save(p, t): open(p, 'w', encoding='utf-8').write(t)
def rep(t, old, new, count=1):
    n = t.count(old); assert n == count, ('count', n, count, old[:70]); return t.replace(old, new)

# ---- the scores for the COMPILED notes: from catalog_facts.json where its rerun holds them, else the records' prints ----
facts = json.load(open(A + 'catalog_facts.json', encoding='utf-8'))['spans']
FALLBACK = {'bamidbar': '66/66', 'naso': '274/274', 'beha': '154/154', 'shelach': '172/172', 'mekoshesh': '34/34', 'korach': '155/155',
            'chukat': '159/159', 'balak': '105/105', 'second_census': '70/70', 'zelophehad': '55/55', 'musafim': '110/110', 'vows': '147/147',
            'midian': '99/99', 'gad_reuben': '74/74', 'journeys': '53/53', 'borders': '56/56', 'refuge': '51/51', 'pesach_sheni': None}
SWEEP = dict(re.findall(r'PASS\s+cold_run_(\w+)\.py\s+rc=0\s+score=(\d+/\d+)', open(SP + 'ref_sweep.out', encoding='utf-8').read()))
def score(short):
    if short in SWEEP: return SWEEP[short]
    sl = (facts.get('cold_run_' + short) or {}).get('score_line') or ''
    m = re.search(r'(\d+/\d+)', sl)
    return m.group(1) if m else FALLBACK.get(short)
def note(*shorts):
    parts = []
    for s in shorts:
        sc = score(s); parts.append('cold_run_%s.py%s' % (s, (' ' + sc) if sc else ''))
    return '; '.join(parts)
PREFIX_RUNNER = [('num_01', ('bamidbar',)), ('num_02', ('bamidbar',)), ('num_03', ('bamidbar',)), ('num_04_kehat', ('bamidbar',)),
    ('num_04_gershon_merari', ('naso',)), ('num_05', ('naso',)), ('num_06', ('naso',)), ('num_07', ('naso',)),
    ('num_08', ('beha',)), ('num_09', ('pesach_sheni',)), ('num_10', ('beha',)), ('num_11', ('beha',)), ('num_12', ('beha',)),
    ('num_13', ('shelach',)), ('num_14', ('shelach',)), ('num_15_offerings_laws', ('shelach',)), ('num_15_wood_tzitzit', ('mekoshesh',)),
    ('num_16', ('korach',)), ('num_17', ('korach',)), ('num_18', ('korach',)), ('num_19', ('chukat',)), ('num_20', ('chukat',)), ('num_21', ('chukat',)),
    ('num_22', ('balak',)), ('num_23', ('balak',)), ('num_24', ('balak',)), ('num_25', ('balak',)), ('num_26', ('second_census',)),
    ('num_27', ('zelophehad',)), ('num_28', ('musafim',)), ('num_29', ('musafim',)), ('num_30', ('vows',)), ('num_31', ('midian',)),
    ('num_32', ('gad_reuben',)), ('num_33', ('journeys',)), ('num_34', ('borders',)), ('num_35', ('refuge',)), ('num_36', ('zelophehad',))]
compiled_lines = ''.join('    ("%s", "%s"),\n' % (p, note(*r)) for p, r in PREFIX_RUNNER)

# ---- build_summary.py ----
P = A + 'tools/build_summary.py'; t = load(P); assert '"Numbers", "Bamidbar"' not in t
blocks = load(SP + 'numbers_blocks.txt')
t = rep(t, ']\n\nCOUNT_OPS = {', blocks + ']\n\nCOUNT_OPS = {')
t = rep(t, 'Vayakhel and Pekudei by the spec executed.\nThe per-block operator counts', 'Vayakhel and Pekudei by the spec executed; the Numbers blocks\n(added 2026-09-13) by the acts run and the laws installed together.\nThe per-block operator counts')
save(P, t); print('build_summary patched')

# ---- build_program_outline.py ----
P = A + 'tools/build_program_outline.py'; t = load(P); assert '"num": "Numbers"' not in t
t = rep(t, 'BOOK = {"gen": "Genesis", "exo": "Exodus", "lev": "Leviticus"}', 'BOOK = {"gen": "Genesis", "exo": "Exodus", "lev": "Leviticus", "num": "Numbers"}')
t = rep(t, '    ("lev_24_blasphemer", "cold_run_lev24.py 23/23 (exports talion(), called by Mishpatim)"),\n]',
        '    ("lev_24_blasphemer", "cold_run_lev24.py 23/23 (exports talion(), called by Mishpatim)"),\n    # the fourth book (2026-09-13), the scores from catalog_facts.json\'s rerun\n' + compiled_lines + ']')
t = rep(t, 'by_book = {"Genesis": [], "Exodus": [], "Leviticus": []}', 'by_book = {"Genesis": [], "Exodus": [], "Leviticus": [], "Numbers": []}')
t = rep(t, 'for book in ("Genesis", "Exodus", "Leviticus"):', 'for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):', count=3)
t = rep(t, '<a href="#Leviticus">Leviticus</a> ', '<a href="#Leviticus">Leviticus</a><a href="#Numbers">Numbers</a> ')
t = rep(t, '"[Leviticus](PROGRAM_LEVITICUS.md); or all at once', '"[Leviticus](PROGRAM_LEVITICUS.md), [Numbers](PROGRAM_NUMBERS.md); or all at once')
t = rep(t, '% ("2026-09-05", tot["units"]', '% ("2026-09-13", tot["units"]')
t = rep(t, 'generated 2026-09-05 from the frozen units in canonical order.</p>', 'generated 2026-09-13 from the frozen units in canonical order.</p>')
t = rep(t, '<title>Program Outline, Genesis through Leviticus</title>', '<title>Program Outline, Genesis through Numbers</title>')
t = rep(t, 'Walks every FROZEN unit in canonical order (Genesis 1:1 through the last\nfrozen Leviticus span)', 'Walks every FROZEN unit in canonical order (Genesis 1:1 through the last\nfrozen Numbers span; the fourth book added 2026-09-13)')
save(P, t); print('build_program_outline patched')

# ---- build_plain_outline.py ----
P = A + 'tools/build_plain_outline.py'; t = load(P); assert '"Numbers": []' not in t
t = rep(t, 'by_book = {"Genesis": [], "Exodus": [], "Leviticus": []}', 'by_book = {"Genesis": [], "Exodus": [], "Leviticus": [], "Numbers": []}')
t = rep(t, 'for book in ("Genesis", "Exodus", "Leviticus"):', 'for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):', count=3)
t = rep(t, '<a href="#Leviticus">Leviticus</a> ', '<a href="#Leviticus">Leviticus</a><a href="#Numbers">Numbers</a> ')
t = rep(t, '"[Leviticus](PLAIN_LEVITICUS.md), or all at once', '"[Leviticus](PLAIN_LEVITICUS.md), [Numbers](PLAIN_NUMBERS.md), or all at once')
t = t.replace('Generated 2026-09-05 from the frozen units', 'Generated 2026-09-13 from the frozen units').replace('generated 2026-09-05 from the frozen units', 'generated 2026-09-13 from the frozen units')
save(P, t); print('build_plain_outline patched')

# ---- build_linked.py ----
P = A + 'tools/build_linked.py'; t = load(P); assert '"Bamidbar": "in the wilderness"' not in t
t = rep(t, '    "Leviticus": ["CODE_EXECUTION"],\n}', '    "Leviticus": ["CODE_EXECUTION"],\n    "Numbers": [],\n}')
m = re.search(r'"Bechukotai": "in My statutes",?', t); assert m, 'Bechukotai gloss'
t = t[:m.end()] + ('\n    "Bamidbar": "in the wilderness", "Naso": "take a count", "Beha\'alotcha": "when you raise", "Shelach": "send",\n'
                   '    "Korach": "Korah", "Chukat": "the statute", "Balak": "Balak", "Pinchas": "Phinehas", "Matot": "tribes", "Masei": "journeys",') + t[m.end():]
t = rep(t, '<a href="#Leviticus">Leviticus</a> ', '<a href="#Leviticus">Leviticus</a><a href="#Numbers">Numbers</a> ')
t = rep(t, "'Generated 2026-09-05 from the frozen units: %d units, %d verses.</p>'", "'Generated 2026-09-13 from the frozen units: %d units, %d verses.</p>'")
save(P, t); print('build_linked patched')

# ---- build_diagrams.py ----
P = A + 'tools/build_diagrams.py'; t = load(P); assert 'def numbers_runners' not in t
for old, new in [
    ('"158 frozen: Genesis 73, Exodus 41, Leviticus 44",', '"210 frozen: Genesis 73, Exodus 41, Leviticus 49, Numbers 47",'),
    ('"158 units -> 1,809 facts, 557 events,",', '"210 units -> 1,809 facts,",'),
    ('"341 demands (191 open), standing 1,608",', '"341 demands (191 open), standing 2,163",'),
    ('"14 spans, 59 compiled functions",', '"57 runners, 427 compiled functions",'),
    ('"294/294 cells on the latest run",', '"6,378 graded cells, 57/57 on the sweep",'),
    ('"45 rounds, 1,317/1,317",', '"47 rounds, 1,595/1,595; the union-rule dockets",'),
    ('"41 rules modules, 45 case files",', '"43 rules modules, 47 case files",'),
    ('"timers, the diff engine",', '"timers, the calendar, the journal, the diff engine",'),
    ('"5 daemons wrapped, 6 recorded scenes"], BLUE)', '"62 daemons; one tape, 1,279 events, 157 dates"], BLUE)'),
    ('"effect_vocabulary.yaml (58 effects, 8 ledger ops)  ·  MOVE_CATALOG.md (M-01..M-18)  ·  "', '"effect_vocabulary.yaml (1,012 effects, 8 ledger ops)  ·  MOVE_CATALOG.md (M-01..M-30)  ·  "'),
    ('s.text(490, 30, "The six layers of the compiled code, and how data moves between them",', 's.text(490, 30, "The six layers of the compiled code, and how data moves between them (counts of 2026-09-13)",'),
    ('s.text(605, 28, "The 14 compiled spans and every cross-span edge the code or its reports name",', 's.text(605, 28, "The 14 compiled spans of 2026-09-05 and every cross-span edge named then (the 57 of 2026-09-13: DEPENDENCIES.md)",'),
]:
    t = rep(t, old, new)
NUMBERS_FN = '''

# ----------------------------------------------- 8. the fourth book's runners
def numbers_runners():
    """The eighteen runners of the book of Numbers in scroll order, each with its span, its score as printed on the
    2026-09-13 rerun (catalog_facts.json), and the earlier programs it calls live (DEPENDENCY_INDEX.md)."""
    import json, re
    facts = json.load(open(os.path.join(os.path.dirname(HERE), "catalog_facts.json"), encoding="utf-8"))["spans"]
    dep = open(os.path.join(os.path.dirname(os.path.dirname(HERE)), "World", "step9", "DEPENDENCY_INDEX.md"), encoding="utf-8").read()
    calls = {}
    for sec in re.split(r"\\n(?=## cold_run_)", dep):
        m = re.match(r"## (cold_run_\\w+)\\.py — (.*)", sec.split("\\n", 1)[0])
        if not m: continue
        co = re.search(r"- calls out \\(live\\): (.*)", sec)
        calls[m.group(1)] = (m.group(2).strip(), co.group(1).strip() if co else "none")
    order = ["bamidbar", "naso", "beha", "pesach_sheni", "shelach", "mekoshesh", "korach", "chukat", "balak", "second_census",
             "zelophehad", "musafim", "vows", "midian", "gad_reuben", "journeys", "borders", "refuge"]
    cols, w, h, gx, gy = 3, 380, 96, 400, 112
    rows = (len(order) + cols - 1) // cols
    s = SVG(40 + cols * gx, 70 + rows * gy + 30)
    s.text(s.w / 2, 28, "The fourth book's eighteen runners, in scroll order: span, score on the 2026-09-13 rerun, and the programs each calls live", 13.5, INK, bold=True)
    for i, k in enumerate(order):
        r, c = divmod(i, cols)
        x, y = 20 + c * gx, 50 + r * gy
        name = "cold_run_%s" % k
        span, co = calls.get(name, ("", "none"))
        sl = (facts.get(name) or {}).get("score_line") or ""
        m = re.search(r"(\\d+/\\d+)", sl)
        span_short = span if len(span) <= 52 else span[:49] + "..."
        callees = [c_.strip() for c_ in co.split(",")] if co != "none" else []
        line1 = "calls: " + ", ".join(callees[:6]) + (" ..." if len(callees) > 6 else "") if callees else "calls: none"
        line2 = "      " + ", ".join(callees[6:12]) + (" ..." if len(callees) > 12 else "") if len(callees) > 6 else ""
        lines = [span_short, "%s cells" % m.group(1) if m else "(no matrix line)", line1] + ([line2] if line2 else [])
        s.box(x, y, w, h, name, lines, GOLD, title_size=12, line_size=10)
    s.text(s.w / 2, s.h - 12, "Every call is a live import the dependency gate verified; the labels and teachers are in DEPENDENCIES.md and THE_LINKS.md.", 10.5, SOFT, italic=True)
    s.write("08_numbers_runners.svg")
'''
t = rep(t, '\n\nif __name__ == "__main__":\n    layers(); dependencies(); ox(); slave(); affliction(); installation(); yoma()',
        NUMBERS_FN + '\n\nif __name__ == "__main__":\n    layers(); dependencies(); ox(); slave(); affliction(); installation(); yoma(); numbers_runners()')
save(P, t); print('build_diagrams patched')

# ---- NARRATIVE.md ----
P = A + 'NARRATIVE.md'; t = load(P); assert '## Bamidbar' not in t
t = t.rstrip('\n') + '\n' + load(SP + 'numbers_narrative.md')
save(P, t); print('NARRATIVE appended', len(t.split('\n')), 'lines')
