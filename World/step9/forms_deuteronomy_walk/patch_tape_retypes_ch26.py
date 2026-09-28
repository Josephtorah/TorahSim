import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 18b (2026-09-26; LEAN) — RUN B: THE EARLIER CHECKPOINTS MOVED BY THE NEW LINES, RETYPED FROM THE TAPE'S OWN PRINT (ch26_tape_run1.out: 9/10;
# checkpoint_check 341 rows, 33 miss = the eighteen known + fifteen). A miss is evidence, never a retype — EACH READ FIRST: thirteen earlier checkpoints count a reused
# effect's entries (blessings_for_hearing 2 -> 3 at 28:1; rejoicing 2 -> 4 at 26:11 and 27:7; poor_tithe_owed 1 -> 2 at 26:12; rain_in_its_season 1 -> 2 at 28:12 — the
# design's REUSE_AFTER exactly), DF6 reads the_removal_date's exercised_by (the types added the runner), DA6's word scan for 'neck' finds iron_yoke_on_neck (28:48 — a curse,
# not the stiff neck), DL1's events' day is the creation count's (2489, 11, 1) not the design's era-relative (40, 11, 1); DL3 handled apart (its one row read). 13b's form
# ("since THE DEUTERONOMY WALK 13b" in CQ6) by ast: the declared literal's CHANGED ELEMENT ALONE replaced by the print's value; the note appended inside the text.
import re, ast, sys, subprocess
ROOT = _ROOT
SP = sys.path[0] if sys.argv[0].startswith('/') else '.'
import os; SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
F = f'{ROOT}/World/step9/cold_run_sequence.py'; src = open(F, encoding='utf-8').read()
PR = open(f'{SP}/ch26_tape_run1.out', encoding='utf-8').read().split('\n')
def read(name):
    i = next(k for k, l in enumerate(PR) if re.match(r'\s*CHECKPOINT ' + name + r'\b', l)); dec = com = None
    for k in range(1, 4):
        s = PR[i + k].strip()
        if s.startswith('declared:') and dec is None: dec = s[9:].strip()
        if s.startswith('computed:') and com is None: com = s[9:].strip()
    return ast.literal_eval(dec), ast.literal_eval(com), PR[i]
M = 'RETYPED THE DEUTERONOMY WALK 18b (2026-09-26; LEAN)'
NOTES = {
 'CQ6': "blessings_for_hearing THREE — 28:1's third entry on the line blessings_condition_declared (the reuse; TWO at 13b)",
 'CU5': "blessings_for_hearing THREE (28:1's third entry on blessings_condition_declared — the reuse)",
 'DA6': "the word scan finds iron_yoke_on_neck (28:48's curse — the yoke of iron on the neck, a new effect naming the neck; not the stiff neck of Exodus 32:9, whose hole holds — the design's HOLE_WORDS did not carry this checkpoint's three words: a lesson)",
 'DC2': "rain_in_its_season TWO — 28:12's second entry on the line heavens_treasure_lending_declared (the reuse; ONE at 10b)",
 'DC6': "blessings_for_hearing THREE (28:1's third entry — the reuse)",
 'DD2': "rejoicing_before_the_lord_commanded FOUR — 26:11's third and 27:7's fourth entries on the lines first_fruits_declared and stones_altar_declared (the reuses; TWO at 12b)",
 'DF2': "poor_tithe_owed TWO — 26:12's second entry on the line tithe_confession_declared (the reuse); rejoicing FOUR with the sources 26:1 and 27:1 (the lines' first verses; the seats 26:11 and 27:7)",
 'DF4': "rejoicing FOUR (26:11 and 27:7 — the reuses)",
 'DF6': "the_removal_date exercised by food_tithe AND firstfruits_ebal_curses (the types at 18b — the confession's removal date read by the new runner's clock)",
 'DG2': "blessings_for_hearing THREE with the third source 28:1 (the reuse)",
 'DG4': "blessings_for_hearing THREE (28:1's third entry — the reuse)",
 'DH4': "rejoicing FOUR (26:11 and 27:7 — the reuses)",
 'DK4': None,   # built from the print's own 34th name
 'DL1': "the events' day by ex.date (17b's DK1 form) — the first run computed it by D(), the creation count's (2489, 11, 1) against the literal (40, 11, 1): the patcher's slip, the literal KEPT and the helper corrected",
}
DL1_OLD, DL1_NEW = 'sorted({D(l[1]) for _, l in ev_cp})', 'sorted({ex.date(l[1]) for _, l in ev_cp})'   # DL1: the day helper — DK1's form; the declared (40, 11, 1) stands
tree = ast.parse(src); lines = src.split('\n'); starts = [0]
for l in lines: starts.append(starts[-1] + len(l) + 1)
def off(ln, col): return starts[ln - 1] + len(lines[ln - 1][:col].encode('utf-8')[:0]) + col   # col_offset is in UTF-8 BYTES in ast — converted below
def boff(ln, col):   # ast columns are utf-8 byte offsets: convert to a str index
    b = lines[ln - 1].encode('utf-8'); return starts[ln - 1] + len(b[:col].decode('utf-8'))
def walk(node, d, c):
    if d == c: return []
    if isinstance(node, (ast.Tuple, ast.List)) and isinstance(d, (tuple, list)) and isinstance(c, (tuple, list)) and len(node.elts) == len(d) == len(c):
        out = []
        for e, a, b in zip(node.elts, d, c): out += walk(e, a, b)
        return out
    return [(boff(node.lineno, node.col_offset), boff(node.end_lineno, node.end_col_offset), repr(c))]
edits = []; report = []
calls = {n.args[0].value.split()[0]: n for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, 'id', None) == 'cp' and n.args and isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str)}
for name, note in NOTES.items():
    d, c, line = read(name); n = calls[name]
    if name == 'DK4':
        names = re.findall(r'([a-z_]+) (\d+)\b', line); j = [k for k, (a, b) in enumerate(zip(d[0], c[0])) if a != b]; assert j == [33], j
        assert names[33][0] == 'blessings_for_hearing', names[33]; note = "blessings_for_hearing THREE — the thirty-fourth count (28:1's third entry — the reuse; the print's own order)"
    e = walk(n.args[1], d, c) if name != 'DL1' else []
    assert e or name == 'DL1', (name, 'no change found')
    edits += e
    s0, s1 = boff(n.args[0].lineno, n.args[0].col_offset), boff(n.args[0].end_lineno, n.args[0].end_col_offset); q = src[s1 - 1]; assert q in "'\"", (name, q)
    note_t = note.replace("\\", "\\\\").replace(q, "\\" + q); edits.append((s1 - 1, s1 - 1, '; ' + M + ': ' + note_t))
    report.append((name, [(src[a:b][:60], v[:60]) for a, b, v in e] if name != 'DL1' else [('D(l[1])', 'ex.date(l[1])')]))
for r in report: print(r)
assert len({(a, b) for a, b, _ in edits}) == len(edits)
new = src
for a, b, v in sorted(edits, key=lambda t: -t[0]): new = new[:a] + v + new[b:]
assert new.count(DL1_OLD) == 1 and src.count('ex.date(l[1]) for _, l in ev_cp') >= 1, (new.count(DL1_OLD),); new = new.replace(DL1_OLD, DL1_NEW)   # DL1's helper corrected to DK1's
ast.parse(new); print('edits', len(edits), 'checkpoints', len(report), '| CHECK' if CHECK else '| WRITTEN')
if not CHECK: open(F, 'w', encoding='utf-8').write(new)
