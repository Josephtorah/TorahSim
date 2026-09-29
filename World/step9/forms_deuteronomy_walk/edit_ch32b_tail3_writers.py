#!/usr/bin/env python3
"""edit_ch32b_tail3_writers.py — THE DEUTERONOMY WALK 20b's tail, third part (2026-09-29): the records' writers AMENDED for the chain's third pass (green to the
stamp, RED at the sweep's 900 s limit on the song's runner alone) and the fourth pass from the stamp: the facts module reads the third summary, the sweep's
lines, the limit's print and the FOURTH summary (ch32b_gates4); the AS BUILT template gains departure 17 and lessons 20-21; the records writer's NOTE, debt
line, recovery section and memory line; the commit message; the copier's lists. Every anchor asserted unique. Run from the repo root."""
import ast, os, re
SP = os.path.dirname(os.path.abspath(__file__))
def rd(p): return open(p, encoding='utf-8').read()
def sub1(t, old, new, name):
    if t.count(old) == 0 and t.count(new) == 1: return t   # already applied (the script's earlier run wrote this file before a later anchor tripped)
    assert t.count(old) == 1, (name, t.count(old), old[:90]); return t.replace(old, new)
edits = 0
# ---- (1) the facts module ----
f = rd(f'{SP}/ch32b_tail_facts.py')
f = sub1(f, "summ = rd(f'{SP}/ch32b_gates3_SUMMARY.txt'); assert 'FAILURES' not in summ, summ[-300:]\n"
            "STEPS = re.findall(r'^(PASS|FAIL|SKIP) (\\w+)(?: rc=\\d+)? \\((\\d+)s\\)', summ, re.M); assert [n for _, n, _ in STEPS] == ['tape', 'probes', 'daemon', 'dependency', 'build', 'journal', 'register', 'positions', 'checkpoint', 'stamp', 'sweep', 'unmoved'] and all(v == 'PASS' for v, _, _ in STEPS), STEPS\n"
            "CHAIN_S = sum(int(t) for _, _, t in STEPS); GD = f'{SP}/ch32b_gates3'\n",
         "summ3 = rd(f'{SP}/ch32b_gates3_SUMMARY.txt'); STEPS3 = re.findall(r'^(PASS|FAIL|SKIP) (\\w+)(?: rc=\\d+)? \\((\\d+)s\\)', summ3, re.M)\n"
         "assert [(v, n) for v, n, _ in STEPS3] == [('PASS', 'tape'), ('PASS', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register'), ('PASS', 'positions'), ('PASS', 'checkpoint'), ('PASS', 'stamp'), ('FAIL', 'sweep')] and 'SKIP unmoved (an earlier step failed)' in summ3, STEPS3\n"
         "CHAIN3 = sum(int(t) for _, _, t in STEPS3); POS_S = int([t for _, n, t in STEPS3 if n == 'positions'][0]); GD = f'{SP}/ch32b_gates3'\n"
         "sw3 = rd(f'{GD}/sweep.out'); SWEEP3 = R(r'(\\d+/\\d+) runners green', sw3, 'the third pass sweep'); SWT = R(r'^FAIL\\s+cold_run_song_charge_nebo\\.py rc=124\\s+score=rc-only \\(no score line printed\\)\\s+([\\d.]+)s$', sw3, 'the song runner timed out')\n"
         "SW_TOP = sorted(((float(t), n) for n, t in re.findall(r'^PASS\\s+(cold_run_\\w+)\\.py rc=0\\s+score=\\d+/\\d+\\s+([\\d.]+)s$', sw3, re.M)), reverse=True)[:3]; SW_TOP = '; '.join('%s %.1f s' % (n[9:], t) for t, n in SW_TOP)\n"
         "SWTO = R(r'^the sweep limit (900 -> 2400) \\(--timeout N\\); three edits \\| WRITTEN$', rd(f'{SP}/ch32b_sweep_timeout.out'), 'the sweep limit')\n"
         "done3 = rd(f'{SP}/ch32b_tail_chain3.DONE'); assert R(r'^chain rc=(\\d+)$', done3, 'chain rc 3') == '0', done3\n"
         "summ = rd(f'{SP}/ch32b_gates4_SUMMARY.txt'); assert 'FAILURES' not in summ, summ[-300:]\n"
         "STEPS = re.findall(r'^(PASS|FAIL|SKIP) (\\w+)(?: rc=\\d+)? \\((\\d+)s\\)', summ, re.M); assert [(v, n) for v, n, _ in STEPS] == [('PASS', 'stamp'), ('PASS', 'sweep'), ('PASS', 'unmoved')] and summ.count('(before --from)') == 9, STEPS\n"
         "CHAIN4 = sum(int(t) for _, _, t in STEPS); CHAIN_S = CHAIN3 + CHAIN4; NCHAIN = len({n for v, n, _ in STEPS3 + STEPS if v == 'PASS'}); assert NCHAIN == 12, NCHAIN; GD4 = f'{SP}/ch32b_gates4'\n", 'facts summ')
f = sub1(f, "SWEEP = R(r'(\\d+/\\d+) runners green', rd(f'{GD}/sweep.out'), 'the sweep')", "SWEEP = R(r'(\\d+/\\d+) runners green', rd(f'{GD4}/sweep.out'), 'the sweep'); SWT4 = R(r'^PASS\\s+cold_run_song_charge_nebo\\.py rc=0\\s+score=72/72\\s+([\\d.]+)s$', rd(f'{GD4}/sweep.out'), 'the song runner in the fourth pass')", 'facts SWEEP')
f = sub1(f, 'NCHAIN=len(STEPS)', 'NCHAIN=NCHAIN', 'facts NCHAIN')   # the first form's regex stopped at len(STEPS)'s bracket and left an unmatched one
f = sub1(f, "D = dict(CHAIN2=CHAIN2,", "D = dict(CHAIN3=CHAIN3, POS_S=POS_S, SWEEP3=SWEEP3, SWT=SWT, SW_TOP=SW_TOP, SWTO=SWTO, CHAIN4=CHAIN4, SWT4=SWT4, CHAIN2=CHAIN2,", 'facts D')
ast.parse(f); open(f'{SP}/ch32b_tail_facts.py', 'w', encoding='utf-8').write(f); edits += 4
# ---- (2) the AS BUILT template ----
a = rd(f'{SP}/ch32b_asbuilt.txt')
a = sub1(a, "the cache cleared again, the third pass from the tape ALL GREEN — and these records", "the cache cleared again, the third pass from the tape green to the stamp and red at the sweep's limit (the song's runner past 900 s with the cache off — the limit raised), the fourth pass from the stamp ALL GREEN — and these records", 'asbuilt heading')
a = sub1(a, "THE THIRD PASS FROM THE TAPE ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps — the tape %(TAPE2)s, the probe suites %(PROBES)s, the daemon, dependency, build and journal gates, the register gate --strict %(REG)s, the positions %(POS)s, the checkpoint probes, the stamp, the sweep %(SWEEP)s, the journal unmoved) — no further demand;",
         "THE THIRD PASS FROM THE TAPE (%(CHAIN3)d s) GREEN THROUGH THE STAMP — the tape %(TAPE2)s, the probe suites %(PROBES)s (the cache probe 8/8: the sharing groups kept), the daemon, dependency, build and journal gates, the register gate --strict %(REG)s, the positions %(POS)s (%(POS_S)d s — ten times the 548-657 s of sittings 14b-18b, as 19b's 6043 s at two workers: a finding, OWED a measurement), the checkpoint probes, the stamp — and RED AT THE SWEEP: %(SWEEP3)s runners green, the song's runner alone rc=124 at the sweep's 900 s limit under INK_CACHE=0 (%(SWT)s s; the sweep's times grow with the callees' full loads — %(SW_TOP)s): THE LIMIT RAISED in run_cold_all.py (%(SWTO)s s as --timeout N, a dated comment; no runner, engine or registry moved — the readers' snapshot and the sweep's stamp key neither) and THE FOURTH PASS --from stamp (ch32b_gates4; %(CHAIN4)d s): the journal stamped, the sweep %(SWEEP)s (the song's runner %(SWT4)s s), the journal UNMOVED — no further demand; the two passes %(CHAIN_S)d s over %(NCHAIN)d steps;", 'asbuilt tail')
lines = a.split('\n'); assert lines[6].startswith('THE DEPARTURES') and (lines[6].endswith('F recording the fact alone.') or '(17) THE SWEEP' in lines[6]), lines[6][-80:]
if '(17) THE SWEEP' not in lines[6]: lines[6] += " (17) THE SWEEP'S PER-RUNNER LIMIT — 900 s from the gates cut — fell on the song's runner alone under INK_CACHE=0 (%(SWT)s s, rc=124; its forty-two callees' full loads): raised to 2400 s as --timeout N in run_cold_all.py at the tail, the fourth pass from the stamp; and the positions step's %(POS_S)d s (against 548-657 s at sittings 14b-18b; 19b's 6043 s at two workers) — a finding, OWED a measurement."
assert lines[8].startswith('THE LESSONS') and (lines[8].endswith('the sharing groups kept.') or '(20) A RUNNER' in lines[8]), lines[8][-80:]
if '(20) A RUNNER' not in lines[8]: lines[8] += " (20) A RUNNER'S SWEEP TIME IS ITS CALLEES' FULL LOADS — under INK_CACHE=0 every callee's checks run whole in the runner's process: the sweep's slowest lines grow with the callee count (%(SW_TOP)s), and a big-callee runner needs the limit read from the sweep's print and raised before the sweep, not after; (21) A CHAIN STEP'S TIME IS READ AGAINST ITS PREDECESSORS — the positions step ran ten times its 14b-18b measure since 19b's marker: a finding filed with its numbers, not a fix at the tail."
a = '\n'.join(lines); open(f'{SP}/ch32b_asbuilt.txt', 'w', encoding='utf-8').write(a); edits += 4
# ---- (3) the records writer ----
r = rd(f'{SP}/write_ch32b_records.py')
r = sub1(r, "assert '\\n#236 (' in sd and '\\n#236 ADDENDUM 1 (' in sd and '\\n#236 ADDENDUM 2 (' in sd and 'THE TAIL OF 20b (' not in sd", "assert '\\n#236 (' in sd and '\\n#236 ADDENDUM 1 (' in sd and '\\n#236 ADDENDUM 2 (' in sd and '\\n#236 ADDENDUM 3 (' in sd and 'THE TAIL OF 20b (' not in sd", 'records sd assert')
r = sub1(r, "i236 = sd.index('\\n#236 ADDENDUM 2 (')", "i236 = sd.index('\\n#236 ADDENDUM 3 (')", 'records i236')
r = sub1(r, "the records after the compactions at addenda 1 and 2, on his word): the chain's first SUMMARY", "the records after the compactions at addenda 1, 2 and 3, on his word): the chain's first SUMMARY", 'records note words')
r = sub1(r, "THE THIRD PASS FROM THE TAPE ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps — the tape %(TAPE2)s;",
         "THE THIRD PASS FROM THE TAPE (%(CHAIN3)d s) GREEN THROUGH THE STAMP (the cache probe 8/8 — the sharing groups kept; the positions %(POS)s in %(POS_S)d s — ten times the 14b-18b measure, a finding OWED a measurement) and RED AT THE SWEEP — %(SWEEP3)s runners green, the song's runner alone rc=124 at the sweep's 900 s limit under INK_CACHE=0 (%(SWT)s s; the slowest beside it %(SW_TOP)s — a runner's sweep time is its callees' full loads): THE LIMIT RAISED (run_cold_all.py — %(SWTO)s s as --timeout N; the tape's, the probes' and the stamp's keys unmoved) and THE FOURTH PASS --from stamp (ch32b_gates4) ALL GREEN in %(CHAIN4)d s — the journal stamped, the sweep %(SWEEP)s (the song's runner %(SWT4)s s), the journal UNMOVED; the two passes %(CHAIN_S)d s (%(NCHAIN)d steps — the tape %(TAPE2)s;", 'records note tail')
r = sub1(r, "the departures 1-16 and the lessons 1-19), the forms copied, the commit message", "the departures 1-17 and the lessons 1-21), the forms copied, the commit message", 'records note counts')
r = sub1(r, "ALL GREEN on its third pass from the tape (sweep %(SWEEP)s); OWED: the docket whole", "its third pass green to the stamp and red at the sweep's 900 s limit on the song's runner alone (its callees' full loads — raised to 2400); ALL GREEN on its fourth pass from the stamp (sweep %(SWEEP)s); OWED: the positions step's tenfold time since 19b's marker (%(POS_S)d s) a measurement; the docket whole", 'records debt')
r = sub1(r, "the cache probe RED on pass 1 (the reuses, the rain — retyped; cache cleared); the cache probe RED again on pass 2 (the runner bound callees via globals() — retyped as assignments); ALL GREEN on pass 3 (sweep %s); RUN B\\'s window 825k — THE CAP BROKEN: a big-callee compile splits RUN B.",
         "the cache probe RED on pass 1 (retyped; cache cleared); C6 RED again on pass 2 (the runner\\'s globals() bindings — retyped as assignments); pass 3 green to the stamp, the sweep\\'s 900 s limit on the runner (raised); ALL GREEN on pass 4 (sweep %s); RUN B\\'s window 825k — THE CAP BROKEN.", 'records SEC2')
r = sub1(r, "the 77th runner song_charge_nebo %s in six parts + the generated cases; %s kinds in three forms / %s effects + %s seats; NO MARKER; the tape %s on its second run; %d edges; the chain THRICE:", "the 77th runner song_charge_nebo %s in six parts; %s kinds in three forms / %s effects + %s seats; NO MARKER; the tape %s on its second run; %d edges; the chain FOUR PASSES:", 'records NEWL head')
r = sub1(r, "pass 2 the cache probe RED AGAIN (C6 — the runner bound its callees via a helper writing globals(), unseen by the cache's skip: %s bindings retyped as assignments), pass 3 from the tape ALL GREEN;", "pass 2 the cache probe RED AGAIN (C6 — the runner's globals() bindings, %s retyped as assignments), pass 3 green to the stamp — the sweep's 900 s limit fell on the song's runner alone (its callees' full loads; raised to 2400), pass 4 from the stamp ALL GREEN;", 'records NEWL tail')   # NEWL is a double-quoted string: plain apostrophes
r = sub1(r, "the chain ALL GREEN on its third pass; RUN B\\'s window 825k", "the chain ALL GREEN on its fourth pass; RUN B\\'s window 825k", 'records description')
r = sub1(r, "the records after the compactions at addenda 1 and 2)", "the records after the compactions at addenda 1, 2 and 3)", 'records mw words')
r = sub1(r, "the third pass from the tape ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps;", "the third pass from the tape green to the stamp (the cache probe 8/8) and RED at the sweep — the song's runner alone past the 900 s limit under INK_CACHE=0 (its callees' full loads; raised to 2400 as --timeout N), the fourth pass from the stamp ALL GREEN; the two %(CHAIN_S)d s (%(NCHAIN)d steps;", 'records mw passes')
r = sub1(r, "the departures 1-16, the lessons 1-19), the forms copied, the message built", "the departures 1-17, the lessons 1-21), the forms copied, the message built", 'records mw counts')
r = sub1(r, "(C6 a second time, after the clear);", "(C6 a second time, after the clear); a runner's sweep time is its callees' full loads — the limit read from the print and raised; a chain step's time read against its predecessors (the positions tenfold since 19b — a finding);", 'records mw lesson')
ast.parse(r); open(f'{SP}/write_ch32b_records.py', 'w', encoding='utf-8').write(r); edits += 14
# ---- (4) the commit message writer ----
c = rd(f'{SP}/write_ch32b_commit_msg.py')
c = sub1(c, "RETYPED AS ASSIGNMENTS AND THE CACHE CLEARED AGAIN; ALL GREEN ON THE THIRD — THE FULL PROCESS OWED)", "RETYPED AS ASSIGNMENTS AND THE CACHE CLEARED AGAIN; GREEN TO THE STAMP ON THE THIRD AND RED AT THE SWEEP'S LIMIT — THE SONG'S RUNNER PAST 900 SECONDS WITH THE CACHE OFF, ITS CALLEES' FULL LOADS, THE LIMIT RAISED; ALL GREEN ON THE FOURTH FROM THE STAMP — THE FULL PROCESS OWED)", 'commit head')
c = sub1(c, "and his word after the compaction at addendum 2 (its third part — these records)", "his word \"Continue\" in addendum 2's window (its third part — the sweep's limit) and his word after the compaction at addendum 3 (its fourth part — these records)", 'commit words')
c = sub1(c, "its addenda 1-2 and its NOTE", "its addenda 1-3 and its NOTE", 'commit state doc')
c = sub1(c, "the third pass from the tape ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d s", "the third pass from the tape (%(CHAIN3)d s) green to the stamp — the cache probe 8/8, the positions %(POS)s in %(POS_S)d s (tenfold since 19b, a finding OWED a measurement) — and RED at the sweep: the song's runner alone rc=124 at the 900 s limit under INK_CACHE=0 (%(SWT)s s; %(SW_TOP)s beside it — a runner's sweep time is its callees' full loads), the limit raised to 2400 s as --timeout N in run_cold_all.py, the fourth pass from the stamp ALL GREEN in %(CHAIN4)d s (the sweep %(SWEEP)s, the song's runner %(SWT4)s s); the two passes %(CHAIN_S)d s (%(NCHAIN)d s", 'commit passes')
c = sub1(c, "the departures 1-16 and the lessons 1-19, the state doc", "the departures 1-17 and the lessons 1-21, the state doc", 'commit counts')
ast.parse(c); open(f'{SP}/write_ch32b_commit_msg.py', 'w', encoding='utf-8').write(c); edits += 5
# ---- (5) the copier's lists, by ast ----
cp = rd(f'{SP}/copy_ch32_forms.py'); b = cp.encode('utf-8'); t = ast.parse(cp); starts = [0]
for line in b.split(b'\n'): starts.append(starts[-1] + len(line) + 1)
ADDS = {'PY': ['patch_sweep_timeout_ch32b.py', 'edit_ch32b_tail3_writers.py', 'write_ch32b_point5.py'],
        'OUT': ['ch32b_sweep_timeout_check.out', 'ch32b_sweep_timeout.out', 'ch32b_tail_chain3.sh', 'ch32b_tail_chain3.log', 'ch32b_tail_chain3.DONE', 'ch32b_gates4_SUMMARY.txt', 'ch32b_gates4.log', 'ch32b_writers_edit3.out', 'ch32b_point5_check.out', 'ch32b_point5_write.out', 'ch32b_forms6.out', 'ch32b_home6.out']}
ins = []
for n in t.body:
    if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ADDS:
        v = n.value
        while isinstance(v, ast.BinOp): v = v.left
        assert isinstance(v, ast.List); end = starts[v.end_lineno - 1] + v.end_col_offset - 1; assert b[end:end + 1] == b']'
        present = {e.value for e in v.elts if isinstance(e, ast.Constant)}; new = [x for x in ADDS[n.targets[0].id] if x not in present]
        ins.append((end, (', ' + ', '.join(repr(x) for x in new)).encode('utf-8') if new else b'', n.targets[0].id, len(new)))   # nothing inserted when every name is present (a rerun)
assert len(ins) == 2, ins
for end, txt, nm, k in sorted(ins, reverse=True): b = b[:end] + txt + b[end:]; edits += k
cp2 = b.decode('utf-8'); t2 = ast.parse(cp2)
got = {n.targets[0].id: n.value for n in t2.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ADDS}
consts = {k: {e.value for e in ast.walk(v) if isinstance(e, ast.Constant) and isinstance(e.value, str)} for k, v in got.items()}
assert all(x in consts[k] for k in ADDS for x in ADDS[k]) and any(isinstance(e, ast.JoinedStr) for e in ast.walk(got['OUT'])), 'the copier lists'
open(f'{SP}/copy_ch32_forms.py', 'w', encoding='utf-8').write(cp2)
for p in ('ch32b_tail_facts.py', 'write_ch32b_records.py', 'write_ch32b_commit_msg.py', 'copy_ch32_forms.py', 'ch32b_asbuilt.txt'):
    x = rd(f'{SP}/{p}'); assert not re.search('[' + chr(0x5d0) + '-' + chr(0x5ea) + ']', x) and os.path.expanduser('~') not in x and SP not in x, p
ph = set(re.findall(r'%\((\w+)\)[sd]', a)); keys = set(re.findall(r'(\w+)=', re.search(r'^D = dict\((.*)\)\s*$', f, re.M).group(1)))
used = set(re.findall(r'%\((\w+)\)[sd]', r)) | set(re.findall(r'%\((\w+)\)[sd]', c)); assert not (ph - keys) and not (used - keys - {'VSL', 'REG60'}), (ph - keys, used - keys)
print('THE WRITERS AMENDED AGAIN: %d edits over five files; the AS BUILT template %d bytes, %d placeholders, all in D; the copier lists +%d +%d | WRITTEN' % (edits, len(a.encode()), len(ph), ins[0][3], ins[1][3]))
