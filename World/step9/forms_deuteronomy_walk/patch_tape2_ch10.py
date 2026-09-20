import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): FOUR RETYPES FROM THE TAPE'S SECOND PRINT (ch10_tape2.out, 9/10 — the verdict list's diffs CA1, DB1, DB4, DB7; a miss is
# evidence, read then retyped once): (1) CA1 — chapter 1b's LINES checkpoint LISTS the Deuteronomy markers as a literal (7b's lesson 3): the two retrograde markers
# at Deut 10:2 (2, 1, 1) and 10:6 (40, 5, 1) join the list and the forward markers are SIX (10:12 the pivot) — retyped from the print; (2) DB1 — the own-day line AT
# THE FORWARD MARKER'S OWN VERSE (demand_declared at 10:12) is text_constrained, so the placements set holds three classes (the stitcher's print said so; the
# checkpoint had the design's two); (3) DB4 — the stretch's end is the FIRST TIMER'S FIRE OF tablets_delivered AT OR AFTER the second ascent's marker (the first
# tablets' delivery fired at the breaking (1, 4, 17) — the log's first fire of that effect, forty-one days BEFORE the marker: -41 read); Q25's resolver takes the
# same rule (the fire at or after the stretch's start); (4) DB7 — circumcision_due entries 22 on the running world (the design's 24 was the one database's count,
# which folds the scene worlds' two). Idempotent.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100]); s = s.replace(old, new)
# (1) CA1
rep("[(40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1)], [((2, 2, 20), 'Deut 1:6'), ((1, 2, 16), 'Deut 1:9'), ((40, 6, 1), 'Deut 2:2'), ((1, 3, 7), 'Deut 4:10'), ((1, 4, 17), 'Deut 4:13'), ((1, 3, 7), 'Deut 5:23'), ((1, 4, 18), 'Deut 9:20')], 'text_constrained', ['reading_placed'], (40, 11, 1))",
    "[(40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1), (40, 11, 1)], [((2, 2, 20), 'Deut 1:6'), ((1, 2, 16), 'Deut 1:9'), ((40, 6, 1), 'Deut 2:2'), ((1, 3, 7), 'Deut 4:10'), ((1, 4, 17), 'Deut 4:13'), ((1, 3, 7), 'Deut 5:23'), ((1, 4, 18), 'Deut 9:20'), ((2, 1, 1), 'Deut 10:2'), ((40, 5, 1), 'Deut 10:6')], 'text_constrained', ['reading_placed'], (40, 11, 1))")
i = s.index("FIVE forward (9:21 the stretch"); j = s.index("(9/10)'", i) + len("(9/10)")
s = s[:j] + "; AS OF THE DEUTERONOMY WALK 8b (2026-09-20) NINE retrograde — chapter 10\\'s at 10:2 (2, 1, 1), the fragments in the ark at the erection, and 10:6 (40, 5, 1), Aaron\\'s burial at his death — and SIX forward (10:12 the pivot): the list literal retyped again from the tape\\'s print (the newest sitting\\'s markers join it every time)" + s[j:]
# (2) DB1
rep("(6, ST_KINDS, True, ['page_order', 'reading_placed'], [(2, 1, 1), (40, 5, 1)]", "(6, ST_KINDS, True, ['page_order', 'reading_placed', 'text_constrained'], [(2, 1, 1), (40, 5, 1)]")
rep("then the four own-day lines page_order after the FORWARD marker at Deut 10:12 at (40, 11, 1), no dated field; markers 169 -> 172", "then the four own-day lines after the FORWARD marker at Deut 10:12 at (40, 11, 1), no dated field — demand_declared AT THE MARKER\\'S OWN VERSE text_constrained (the marker\\'s class), the three after it page_order (read at the stitcher\\'s print and the tape\\'s second run); markers 169 -> 172")
# (3) DB4
rep("fire_st = [l for l in w.log if l[0] == 'TIMER-FIRE' and l[2].get('effect') == 'tablets_delivered']", "fire_st = [l for l in w.log if l[0] == 'TIMER-FIRE' and l[2].get('effect') == 'tablets_delivered' and 'Exod 34:4' in mk_cl2 and l[1] >= mk_cl2['Exod 34:4'][1]]   # the first fire of the effect AT OR AFTER the second ascent's marker (the first tablets' delivery fired at the breaking, forty-one days before it — read at the tape's second run)")
rep("(the stretch row 10:10\\'s measure — the end a timer\\'s fire, not a marker)", "(the stretch row 10:10\\'s measure — the end a timer\\'s fire, not a marker: the first fire of tablets_delivered at or after the marker; the log\\'s first fire of that effect is the first tablets\\' at the breaking, -41 read at the tape\\'s second run)")
# (4) DB7
rep("(1, 1, 0, 0, 24, 9), (_n_st('israel', 'shema_commanded')", "(1, 1, 0, 0, 22, 9), (_n_st('israel', 'shema_commanded')")
rep("circumcision_due entries 24 over the world UNMOVED (the flesh\\'s; the heart\\'s a new name)", "circumcision_due entries 22 over the running world UNMOVED (the flesh\\'s; the heart\\'s a new name; the design\\'s 24 the one database\\'s count, which folds the scene worlds\\' two — read at the tape\\'s second run)")
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
# Q25's resolver — the fire at or after the stretch's start
P2 = ROOT + '/World/step9/readback_probes.py'
s = open(P2, encoding='utf-8').read()
old = "    def END(name):   # a stretch's end — a marker's verse, or 'timer:<effect>' the first TIMER-FIRE of that effect on the running world (the third forty ends at the timers' fire (1, 7, 10), not a marker)\n        if name in mk: return mk[name][1]\n        if name.startswith('timer:'):\n            f = [l for l in W.log if l[0] == 'TIMER-FIRE' and l[2].get('effect') == name[6:]]\n            return f[0][1] if f else None\n        return None\n    st_ok = bool(st) and all(r['stretch']['from'] in mk and END(r['stretch']['to']) is not None and END(r['stretch']['to']) - mk[r['stretch']['from']][1] == r['stretch']['days'] for r in st)\n"
assert s.count(old) == 1, s.count(old)
new = "    def END(name, start):   # a stretch's end — a marker's verse, or 'timer:<effect>' the first TIMER-FIRE of that effect AT OR AFTER the stretch's start on the running world (the third forty ends at the timers' fire (1, 7, 10), not a marker; the first tablets' delivery fired at the breaking, before the marker — read at the tape's second run)\n        if name in mk: return mk[name][1]\n        if name.startswith('timer:'):\n            f = [l for l in W.log if l[0] == 'TIMER-FIRE' and l[2].get('effect') == name[6:] and l[1] >= start]\n            return f[0][1] if f else None\n        return None\n    st_ok = bool(st) and all(r['stretch']['from'] in mk and END(r['stretch']['to'], mk[r['stretch']['from']][1]) is not None and END(r['stretch']['to'], mk[r['stretch']['from']][1]) - mk[r['stretch']['from']][1] == r['stretch']['days'] for r in st)\n"
s = s.replace(old, new)
open(P2, 'w', encoding='utf-8').write(s)
py_compile.compile(P2, doraise=True)
print('retyped from the tape\'s second print: CA1 (the markers\' list), DB1 (the placements), DB4 (the fire at or after the marker; Q25 the same), DB7 (circumcision_due 22); both files compile')
