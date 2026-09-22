import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b — THE TAIL (2026-09-21): THE CHAIN'S FIRST PASS READ ONCE (ch13b_chain_SUMMARY_first.txt; dependency, register and probe_register
# prints kept as *_first) — THREE FAILS, ONE CAUSE AND ONE DEMAND: (1) THE DEPENDENCY GATE's one demand, the one the design predicted (decision 5): the AS_WHEN
# pointer at Deut 13:18 ("as He swore to your fathers") filed RUN_CITATION of the patriarchs' oath — seven_nations.the_holy_people('the_oath') by CALL, the fathers'
# merit not_righteousness.the_intercession('remember_your_servants') by CALL; 10b's patch_tail form (the entry inserted at an anchor asserted unique; the Hebrew from
# the gate's own print, glossed inline; yaml loads after). (2) THE REGISTER GATE's one fail: 'footers Deut 28:69: STALE — declared EMPTY, the world now says DAEMONS'
# — THE HEADER AT 12:1 AND THE FOOTER AT 28:69 SHARE ONE BLOCK (Deut 12:1, Deut 28:69]; law_seducers given_at Deut 13:1 turned BOTH seats DAEMONS; 12:1's EMPTY
# declaration was removed at the types, 28:69's is removed here (the gate's print: DECLARED 98 with the stale one uncounted; footers {'DAEMONS': 8, 'EMPTY': 1}).
# (3) THE PROBES' one fail, register_probes R6 — the gate on the running world returned 1 (the same stale footer) and its EMPTY count held 3: retyped 3 -> 1 from
# the gate's print with the dated note. THE RECORDS RETYPED FROM THE PRINT: the writer's DECLARED expectation 99 -> 98 and its 'footer at 12:1' texts now name both
# seats; the runner's DATA row the_register_seats (not a graded case — no CASES row carries it) says 98 and the second seat; part 4 the same (the assembler's source);
# the register file's 12:1 comment names its twin. RUN FROM THE REPO ROOT.
import os as _os, subprocess, yaml, py_compile
ROOT = _ROOT
SP = _os.environ.get('SP') or _os.path.dirname(_os.path.abspath(__file__))
TAG = 'THE DEUTERONOMY WALK 11b (2026-09-21) | '
def rd(p): return open(p, encoding='utf-8').read()
def wr(p, s): open(p, 'w', encoding='utf-8').write(s)
def sub1(s, old, new, name):
    assert s.count(old) == 1, (name, s.count(old), old[:80]); assert new not in s, (name, 'already patched'); return s.replace(old, new)

# ---- (1) THE POINTER at 13:18
D = f'{ROOT}/World/step9/dependency_dispositions.yaml'; d = rd(D)
R = rd(f'{ROOT}/World/step9/cold_run_seducers.py')
assert "SN.the_holy_people" in R and "NR.the_intercession({'ask': 'remember_your_servants'}" in R and "if ask == 'as_he_swore_to_your_fathers':" in R, 'the runner calls the oath and the merit'
P18 = ('  - {verse: "Deut 13:18", form: AS_WHEN, runner: seducers, disposition: RUN_CITATION, link: reference, why: "' + TAG + '''\'and nothing of the devoted thing shall cleave to your hand, that the LORD may turn from the fierceness of His anger and give you mercy, and have mercy on you and multiply you, AS HE SWORE TO YOUR FATHERS\' (כאשר נשבע לאבתיך — as He swore to your fathers; the gate's own print): a RUN CITATION of THE PATRIARCHS' OATH — seven_nations.the_holy_people('the_oath') by CALL (the callee's own verdict, printed before the runner: 7:8's oath, the noun starred by the parser and the swearing no number, the three oath lines on the tape reached through the Genesis runners by CALL), with THE FATHERS' MERIT — the Sifrei Devarim 96:5's reading of the clause (read whole at the reading): not_righteousness.the_intercession('remember_your_servants') by CALL, 7b's parameter with its four dates; the clause's two Deuteronomy seats 13:18 and 19:8 (the second waits for its sitting — never read ahead); the readback row 13:18 SUPPLIED with its write devoted_thing_cleaving_barred, pointer=; the register gate lists no seat in the chapter (its finder scans 'commanded' — the oath's 'swore' outside its forms, with the third and fourth shapes owed to a gate sitting); no debit paid (R5), the frame writes nothing (R6); the design's predicted pointer (decision 5), the census's own demand — THE ONE DEMAND of the chain's first pass (the registration edge filed before it, at RUN B)"}
''')
A3 = '  - {verse: "Deut 12:22", form: AS_WHEN, runner: place_name, disposition: RUN_CITATION'; assert d.count(A3) == 1, d.count(A3)
assert P18 not in d and 'verse: "Deut 13:18"' not in d
k = d.index(A3); e = d.index('\n', k) + 1; d = d[:e] + P18 + d[e:]
wr(D, d)
y = yaml.safe_load(rd(D)); E = y['edges']; P = y['pointers']
pts = [p for p in P if p.get('runner') == 'seducers']
print('yaml loads: edges %d, pointers %d; seducers pointers %s' % (len(E), len(P), [(p['verse'], p['form'], p['disposition'], p['link']) for p in pts]))
assert len(pts) == 1 and pts[0]['why'].startswith(TAG) and len(P) == 208, (len(pts), len(P))

# ---- (2) THE REGISTER FILE: the footer at 28:69's EMPTY declaration removed; the 12:1 comment names its twin
G = f'{ROOT}/World/step9/register_dispositions.yaml'; g = rd(G)
OLD = ('  Deut 28:69:\n    class: EMPTY\n    why: Deuteronomy is not on the tape (the book not read) — the seat waits for its reading and compile\nregisters:\n')
NEW = ('  # Deut 28:69: ' + TAG + "the footer's EMPTY declaration REMOVED at the tail of chapter 13's compile — the chain's first pass: 'footers Deut 28:69: STALE — declared EMPTY, the world now says DAEMONS (remove the declaration)': the footer SHARES THE BLOCK (Deut 12:1, Deut 28:69] with the header at 12:1 (its declaration removed at the types), and law_seducers given_at Deut 13:1 turned both seats DAEMONS — the gate's print footers {'DAEMONS': 8, 'EMPTY': 1} (Deut 1:1 the one EMPTY left); register_probes' EMPTY count retyped 3 -> 1 from the same print\n"
       'registers:\n')
g = sub1(g, OLD, NEW, 'register 28:69')
g = sub1(g, 'the declaration goes, DECLARED 100 -> 99; the receipt at 12:21', "the declaration goes — and the footer at 28:69's on the SAME block with it (the chain's first pass demanded it, removed at the tail): DECLARED 100 -> 98; the receipt at 12:21", 'register 12:1 comment')
wr(G, g); yg = yaml.safe_load(g); assert 'Deut 28:69' not in yg['footers'] and 'Deut 12:1' not in yg['footers'] and 'Deut 1:1' in yg['footers'], list(yg['footers'])
print('register file: footers declared %d %s' % (len(yg['footers']), list(yg['footers'])))

# ---- (3) THE REGISTER PROBE R6: EMPTY 3 -> 1
Q = f'{ROOT}/World/step9/register_probes.py'; q = rd(Q)
q = sub1(q, "t['footers'].get('EMPTY') == 3, t['footers']   # THE DEUTERONOMY WALK 1b (2026-09-15): EMPTY 4 -> 3",
         "t['footers'].get('EMPTY') == 1, t['footers']   # " + TAG.replace(' | ', ': ') + "EMPTY 3 -> 1 — the header Deut 12:1 and the footer Deut 28:69 DAEMONS by law_seducers (given_at Deut 13:1 inside the one block they share); typed from the gate's print {'DAEMONS': 8, 'EMPTY': 1}; sitting 1b's note follows:   # THE DEUTERONOMY WALK 1b (2026-09-15): EMPTY 4 -> 3", 'register_probes R6')
wr(Q, q); py_compile.compile(Q, doraise=True)

# ---- (4) THE RUNNER'S DATA ROW and PART 4 (the assembler's source): DECLARED 100 -> 98, the second seat named
for F in (f'{ROOT}/World/step9/cold_run_seducers.py', f'{SP}/ch13_part4.py'):
    s = rd(F)
    s = sub1(s, 'the class DAEMONS (green): DECLARED 100 -> 99"', 'the class DAEMONS (green) at BOTH the block\'s seats — the header 12:1 and the footer 28:69, its declaration removed at the tail on the chain\'s first-pass demand: DECLARED 100 -> 98 (the gate\'s print)"', F)
    wr(F, s); py_compile.compile(F, doraise=True)
assert 'DECLARED' not in rd(f'{SP}/ch13_part5.py'), 'a CASES row carries the DATA text — regenerate'

# ---- (5) THE WRITER: the expectation and the texts retyped from the print
W = f'{SP}/write_ch13b_records.py'; w = rd(W)
EDITS = [
 ("RG[0] == 99, RG", "RG[0] == 98, RG   # the tail: 98 — the first pass's print with the stale 28:69 uncounted; its removal moves nothing"),
 ("(3) THE FOOTER TURNED DAEMONS BY THE CHAPTER'S OWN DAEMON — law_seducers given_at Deut 13:1\nsits inside (Deut 12:1, Deut 28:69] and the gate's verify refuses a declared green as STALE: the EMPTY declaration REMOVED (10b's why had said 'chapter 13's the first\ncandidate'), DECLARED 100 -> {RG[0]} where the design said 'unmoved';",
  "(3) THE BLOCK'S TWO SEATS TURNED DAEMONS BY THE CHAPTER'S OWN DAEMON — law_seducers given_at Deut 13:1\nsits inside (Deut 12:1, Deut 28:69], the one block the header at 12:1 and the footer at 28:69 SHARE, and the gate's verify refuses a declared green as STALE: 12:1's EMPTY declaration REMOVED at the types (10b's why had said 'chapter 13's the first\ncandidate'), 28:69's demanded by the chain's first pass and removed at the tail, register_probes' EMPTY 3 -> 1 retyped from the gate's print; DECLARED 100 -> {RG[0]} where the design said 'unmoved';"),
 ("FAILS {RG[2]} — the footer at 12:1 DAEMONS by the\nchapter's own daemon),", "FAILS {RG[2]} — the header at 12:1 and the footer at 28:69 DAEMONS by the\nchapter's own daemon, their two EMPTY declarations on the one block removed),"),
 ("(2) A DAEMON GIVEN INSIDE A DECLARED-EMPTY FOOTER'S BLOCK TURNS THE DECLARATION STALE — the gate's own rule refuses a declared green: the declaration goes,\nDECLARED moves down;",
  "(2) A DAEMON GIVEN INSIDE A DECLARED-EMPTY BLOCK TURNS EVERY DECLARATION ON THAT BLOCK STALE — a header and a footer share one block (12:1 and 28:69); the gate's own rule refuses a declared green: both declarations go, the probe's EMPTY count with them,\nDECLARED moves down;"),
 ("the register's finder (no seat — the footer at 12:1 DAEMONS by this daemon)", "the register's finder (no seat — 12:1 and 28:69 DAEMONS by this daemon)"),
 ("FAILS {RG[2]} — the footer at\n12:1's declaration removed, DAEMONS by the chapter's own daemon;", "FAILS {RG[2]} — the header at 12:1's and the footer at\n28:69's declarations removed, both DAEMONS by the chapter's own daemon;"),
 ("the register's\nfooter at 12:1 turned DAEMONS (its EMPTY declaration STALE by the gate's rule — removed);", "the register's\nblock (Deut 12:1, Deut 28:69] turned DAEMONS at both its seats (the two EMPTY declarations STALE by the gate's rule — 12:1's removed at the types, 28:69's at the tail on the chain's demand; register_probes' EMPTY 3 -> 1);"),
 ("FAILS {RG[2]} (12:1's footer DAEMONS by this daemon).", "FAILS {RG[2]} (12:1 and 28:69 DAEMONS by this daemon — their two EMPTY declarations removed)."),
 ("FAILS {RG[2]} (12:1's footer DAEMONS — its declaration removed);", "FAILS {RG[2]} (12:1 and 28:69 DAEMONS — the two declarations removed, the probe's EMPTY 3 -> 1);"),
 ("a daemon inside a\ndeclared-EMPTY footer's block turns the declaration STALE (remove it — DECLARED down);", "a daemon inside a\ndeclared-EMPTY block turns EVERY declaration on it STALE (12:1's and 28:69's — remove both; DECLARED down; the probe's count retyped);"),
]
for old, new in EDITS: w = sub1(w, old, new, 'writer')
wr(W, w); py_compile.compile(W, doraise=True)
print('THE TAIL FILED — 1 RUN_CITATION pointer (13:18); the footer 28:69 removed (the block\'s twin); register_probes EMPTY 3 -> 1; the runner\'s DATA row and part 4 retyped 98; the writer %d edits' % len(EDITS))
