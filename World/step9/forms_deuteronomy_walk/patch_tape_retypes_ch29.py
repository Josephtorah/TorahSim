import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — RUN B: THE EARLIER CHECKPOINTS MOVED BY THE NEW LINES AND THE MARKER, RETYPED FROM THE TAPE'S OWN PRINT (ch29_tape_run1.out: 8/10;
# checkpoint_check 346 rows, 75 miss = the eighteen known + fifty-seven). A miss is evidence, never a retype — EACH READ FIRST (the diff of every declared against its computed,
# element by element): (a) THE MARKER — markers 172 -> 173 in twenty-four checkpoints (the CA-DL blocks' THE LINES and THE REST) and the tape's last day (40, 11, 1) -> (40, 12, 7)
# in nineteen (the counter moved for the first time since 1:3; CA1's list of the markers' days gains the new day); (b) THE CLOCK WALK — thirty-six days from Shevat 1 to Adar 7:
# the sabbath timer fired five times and the month's once (TIMER-FIRE 88 -> 94, TIMER-SET 96 -> 102 by the six re-arms — CA3, CT2, CV2), the pending dues moved (the sabbath
# (40, 11, 8) -> (40, 12, 13), the month (40, 12, 1) -> (41, 1, 1)), and CT6's equality of the two arithmetics FALSE: the Calendar's next('sabbath') from the tape's last day is
# a week from that day (12:14) while the timer's due is its fire day plus seven (12:13) — the two agree only when the tape ends on a fire day, as it did at (40, 11, 1): the
# premise named, the literal retyped, the point recorded as a lesson; (c) THE REUSES — heaven_and_earth_witness 2 -> 4 (CC7, CU6 — CU6's last source 'Deut 31:2' is 'Deut 31:28'
# cut at nine characters; DL4), entered_the_covenant 3 -> 4 (DL4), became_the_lords_people_this_day 1 -> 2 (DL2), blessing_and_curse_set 1 -> 2 (DC2, DD6, DL4), cleaving_commanded
# 2 -> 3 (DC6, DE2, DE4), fear_not_promised 4 -> 6 (DJ4 — the eighth count; CA8 — the second on yehoshua), glory_appeared 6 -> 7 (DB2); (d) THE NEW ENTRIES — the Levites' ledger
# 27 -> 28 (CR2 — the book beside the ark); (e) THE SCANS — CU7 and DA6 read the new values naming the garment and the stiff neck: the two values REWORDED in the daemon (the
# checkpoints' holes hold), not retyped here; CC7's fourth element 0 -> 6 the timers fired after the Deut 4 line (the walk's six). DM3 handled apart (its declared third element
# the count of rows by CALL — 56, read from the print; the tape rows' verses retyped in part 5). 18b's form (patch_tape_retypes_ch26.py) by ast: the declared literal's CHANGED
# ELEMENTS ALONE replaced by the print's value; the note appended inside the text. --check prints only. RUN FROM THE REPO ROOT.
import re, ast, sys, subprocess, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
F = f'{ROOT}/World/step9/cold_run_sequence.py'; src = open(F, encoding='utf-8').read()
PR = open(f'{SP}/ch29_tape_run1.out', encoding='utf-8').read().split('\n')
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
 'CA1': "the markers' days gain (40, 12, 7) (19b's marker at 31:1 — the seventh reading-placed day of the walk); " + DAY,
 'CA3': "TIMER-FIRE 88 -> 94 and TIMER-SET 96 -> 102 — the sabbath fired five times and the month once on 19b's thirty-six days' walk from Shevat 1 to Adar 7, six re-arms; the pending sabbath (40, 12, 13) and month (41, 1, 1); the walk's fires 6, the days 42 from (40, 6, 1)",
 'CA8': "fear_not_promised on yehoshua ONE -> TWO (31:8's reuse — Moses' public charge to Joshua at 19b)",
 'CC1': DAY, 'CC7': "heaven_and_earth_witness TWO -> FOUR (30:19 and 31:28 — the chain's third and fourth seats at 19b); the timers fired after the Deut 4 line 0 -> 6 (19b's walk)", 'CC9': MK,
 'CI1': DAY, 'CI9': MK, 'CO1': MK + '; ' + DAY, 'CO9': MK, 'CQ1': MK + '; ' + DAY, 'CQ9': MK, 'CU1': MK + '; ' + DAY,
 'CU6': "heaven_and_earth_witness TWO -> FOUR (30:19 and 31:28 at 19b); the last entry's source 'Deut 31:28' cut at nine characters ('Deut 31:2') — the witness-call at 31:28", 'CU9': MK,
 'CT2': "the pending sabbath (40, 11, 8) -> (40, 12, 13) and the month (40, 12, 1) -> (41, 1, 1) after 19b's thirty-six days' walk; TIMER-SET 96 -> 102 (six re-arms)",
 'CT6': "FALSE after 19b's walk: the Calendar's next('sabbath') from the tape's last day (40, 12, 7) is a week from that day (40, 12, 14) while the timer's pending due is its fire day plus seven (40, 12, 13) — the two arithmetics agree only when the tape ends on a fire day, as it did at (40, 11, 1); the premise named, a lesson for the box",
 'CV2': "timers set 96 -> 102 (19b's walk — the six re-arms)", 'CR2': "the Levites' ledger 27 -> 28 (book_of_the_law_beside_the_ark_commanded at 31:26 — 19b's statute to the Levites)",
 'DA1': MK + '; ' + DAY, 'DA9': MK, 'DB1': MK + '; ' + DAY, 'DB2': "glory_appeared on the tent of meeting FIVE -> SIX (31:15's reuse at 19b — the cloud's last standing; the seventh on the world)", 'DB9': MK,
 'DC1': MK + '; ' + DAY, 'DC2': "blessing_and_curse_set ONE -> TWO (30:19's reuse at 19b — the pair named with the terms life and death)", 'DC6': "cleaving_commanded TWO -> THREE (30:20's reuse at 19b)", 'DC9': MK,
 'DD1': MK + '; ' + DAY, 'DD6': "blessing_and_curse_set ONE -> TWO (30:19's reuse at 19b)", 'DD9': MK,
 'DE1': MK + '; ' + DAY, 'DE2': "cleaving_commanded TWO -> THREE with the third source 30:15 (the line life_and_death_choice_declared — 30:20's reuse at 19b)", 'DE4': "cleaving_commanded TWO -> THREE (30:20's reuse at 19b)", 'DE9': MK,
 'DF1': MK + '; ' + DAY, 'DF9': MK, 'DG1': MK + '; ' + DAY, 'DG6': "the_release_date exercised by release_firstborn AND covenant_return_charge (the types at 19b — the hakhel's clock reads the release's date by CALL)", 'DG9': MK,
 'DH1': MK + '; ' + DAY, 'DH5': MK, 'DI1': MK + '; ' + DAY, 'DI5': MK, 'DJ1': MK + '; ' + DAY, 'DJ4': "fear_not_promised FOUR -> SIX (31:6 on Israel and 31:8 on Joshua — 19b's reuses; the eighth count)", 'DJ5': MK,
 'DK1': MK + '; ' + DAY, 'DK5': MK, 'DL1': MK, 'DL2': "became_the_lords_people_this_day ONE -> TWO on israel_people (29:12's reuse at 19b — the establishing; 27:9's the first)", 'DL4': "entered_the_covenant THREE -> FOUR (29:11), heaven_and_earth_witness TWO -> FOUR (30:19, 31:28), blessing_and_curse_set ONE -> TWO (30:19) — 19b's reuses", 'DL5': MK,
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
