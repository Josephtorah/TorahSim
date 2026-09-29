import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28; LEAN) — RUN B: THE EARLIER CHECKPOINTS RETYPED FROM THE TAPE'S FIRST PRINT (ch32_tape_run1.out — 9/10; checkpoint_check 351 rows, 24 miss:
# the eighteen known and SIX new — CC7, CU6, DC4, DL4, DM2 the older sittings' counts moved by THIS sitting's reuse and its rain, DN3 this sitting's own tape row fixed in part 5):
# CC7 and CU6 (chapters 4 and 8 — heaven_and_earth_witness on israel_people 4 -> 5 by the chain's fifth seat at 32:1; CU6's newest seat 'Deut 31:2' -> 'Deut 32:1'), DC4 (chapter 11's
# rain hole — the song's doctrine as rain (32:2) names the rain: doctrine_as_rain_and_dew_likened joins the two lists), DL4 (18b's forty references — heaven_and_earth_witness 4 -> 5),
# DM2 (19b's nine reuses — heaven_and_earth_witness 4 -> 5 after 32:1). The literals REPLACED BY THE AST WALKER at the differing leaves (declared vs computed READ FROM THE PRINT, never
# typed), a RETYPED note appended to each name. patch_tape_retypes_ch29b.py's form. --check prints only. RUN FROM THE REPO ROOT.
import re, ast, sys, subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
F = f'{ROOT}/World/step9/cold_run_sequence.py'; src = open(F, encoding='utf-8').read()
PR = open(f'{SP}/ch32_tape_run1.out', encoding='utf-8').read().split('\n')
def read(name):
    i = next(k for k, l in enumerate(PR) if re.match(r'\s*CHECKPOINT ' + re.escape(name) + r'\b', l)); dec = com = None
    for k in range(1, 4):
        s = PR[i + k].strip()
        if s.startswith('declared:') and dec is None: dec = s[9:].strip()
        if s.startswith('computed:') and com is None: com = s[9:].strip()
    return ast.literal_eval(dec), ast.literal_eval(com), PR[i]
M = 'RETYPED THE DEUTERONOMY WALK 20b (2026-09-28; LEAN)'
W5 = "heaven_and_earth_witness on israel_people 4 -> 5 (THE CHAIN OF WITNESSES' FIFTH SEAT at Deut 32:1 — give ear, O heavens; sitting 20b's reuse, the song's first stanza)"
NOTES = {
 'CC7': W5 + " — the world's count of the effect, every seat counted (4:26, 8:19, 30:19, 31:28, 32:1)",
 'CU6': W5 + "; the newest seat's source Deut 31:2 -> Deut 32:1 (the song's line at Moses' last day)",
 'DC4': "the rain's hole gains the song's own row — doctrine_as_rain_and_dew_likened (32:2 'my doctrine shall drop as the rain', the four rains words of Torah — the Sifrei 306:16-35; blessing_and_curse's RAIN_SCAN excludes it, CH32_RAIN): the two lists carry it, the rain effects on Israel now four",
 'DL4': W5 + " — the fifteenth of the forty references (18b's count read at its recon)",
 'DM2': W5 + " — the third of 19b's seven reused effects (its after 4, now 5 by 32:1)",
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
    report.append((name, [(src[a:b][:60], v[:60]) for a, b, v in e]))
for r in report: print(r)
assert len({(a, b) for a, b, _ in edits}) == len(edits)
new = src
for a, b, v in sorted(edits, key=lambda t: -t[0]): new = new[:a] + v + new[b:]
ast.parse(new); print('edits', len(edits), 'checkpoints', len(report), '| CHECK' if CHECK else '| WRITTEN')
if not CHECK: open(F, 'w', encoding='utf-8').write(new)
