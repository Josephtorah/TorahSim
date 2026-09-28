import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — RUN B, THE SECOND RETYPE: CP6 (Numbers 25:19's marker checkpoint — THE NUMBERS WALK 8b's) counts the tape's markers and its F class:
# 172 -> 173 and F 131 -> 132 by 19b's marker at Deut 31:1; missed at the first retype (CP6 taken for one of the eighteen known misses — the checkpoint_check's list read again: the
# nineteenth miss). READ FROM THE TAPE'S SECOND PRINT (ch29_tape_run2.out). patch_tape_retypes_ch29.py's form (the ast walker). --check prints only. RUN FROM THE REPO ROOT.
import re, ast, sys, subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
F = f'{ROOT}/World/step9/cold_run_sequence.py'; src = open(F, encoding='utf-8').read()
PR = open(f'{SP}/ch29_tape_run2.out', encoding='utf-8').read().split('\n')
def read(name):
    i = next(k for k, l in enumerate(PR) if re.match(r'\s*CHECKPOINT ' + re.escape(name) + r'\b', l)); dec = com = None
    for k in range(1, 4):
        s = PR[i + k].strip()
        if s.startswith('declared:') and dec is None: dec = s[9:].strip()
        if s.startswith('computed:') and com is None: com = s[9:].strip()
    return ast.literal_eval(dec), ast.literal_eval(com), PR[i]
M = 'RETYPED THE DEUTERONOMY WALK 19b (2026-09-27; LEAN)'
MK = "markers 172 -> 173 (THE ONE MARKER at Deut 31:1 — Moses' last day (40, 12, 7), sitting 19b's)"
DAY = "the tape's last day (40, 11, 1) -> (40, 12, 7) (the counter moved at 19b's marker for the first time since 1:3)"
NOTES = {
 'CP6': "markers 172 -> 173 and F 131 -> 132 (THE ONE MARKER at Deut 31:1 — Moses' last day (40, 12, 7), sitting 19b's forward marker, reading_placed); the nineteenth miss of checkpoint_check read at the second run — CP6 counts the whole tape's markers",
}
tree = ast.parse(src); lines = src.split('\n'); starts = [0]
for l in lines: starts.append(starts[-1] + len(l) + 1)
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
    e = walk(n.args[1], d, c)
    assert e, (name, 'no change found')
    edits += e
    s0, s1 = boff(n.args[0].lineno, n.args[0].col_offset), boff(n.args[0].end_lineno, n.args[0].end_col_offset); q = src[s1 - 1]; assert q in "'\"", (name, q)
    note_t = note.replace("\\", "\\\\").replace(q, "\\" + q); edits.append((s1 - 1, s1 - 1, '; ' + M + ': ' + note_t))
    report.append((name, [(src[a:b][:50], v[:50]) for a, b, v in e]))
for r in report: print(r)
assert len({(a, b) for a, b, _ in edits}) == len(edits)
new = src
for a, b, v in sorted(edits, key=lambda t: -t[0]): new = new[:a] + v + new[b:]
ast.parse(new); print('edits', len(edits), 'checkpoints', len(report), '| CHECK' if CHECK else '| WRITTEN')
if not CHECK: open(F, 'w', encoding='utf-8').write(new)
