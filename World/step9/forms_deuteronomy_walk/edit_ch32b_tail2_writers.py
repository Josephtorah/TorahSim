#!/usr/bin/env python3
"""edit_ch32b_tail2_writers.py — THE DEUTERONOMY WALK 20b's tail, second half (2026-09-28): the records' writers AMENDED for the chain's second pass (RED on the
cache probe again — the runner's globals() bindings) and the third pass to come: the facts module reads the second summary, the C6 groups, the retype's print,
the fifth graded run and the THIRD summary (ch32b_gates3); the AS BUILT template gains departure 16 and lesson 19 and tells the tail whole; the records
writer's NOTE, debt line, recovery section and memory line; the commit message; the copier's lists. Every anchor asserted unique. Run from the repo root."""
import ast, os, re, sys
SP = os.path.dirname(os.path.abspath(__file__))
def rd(p): return open(p, encoding='utf-8').read()
def sub1(t, old, new, name):
    assert t.count(old) == 1, (name, t.count(old), old[:90]); return t.replace(old, new)
edits = 0
# ---- (1) the facts module ----
f = rd(f'{SP}/ch32b_tail_facts.py')
f = sub1(f, "assert R(r'^probes rc=(\\d+)$', done, 'probes rc') == '0' and R(r'^chain rc=(\\d+)$', done, 'chain rc') == '0', done",
         "assert R(r'^probes rc=(\\d+)$', done, 'probes rc') == '0' and R(r'^chain rc=(\\d+)$', done, 'chain rc') == '1', done   # the first job: the chain's second pass RED on the cache probe\n"
         "summ2 = rd(f'{SP}/ch32b_gates2_SUMMARY.txt'); A2 = re.findall(r'^(PASS|FAIL|SKIP) (\\w+)(?: rc=\\d+)? \\((\\d+)s\\)', summ2, re.M); assert [(v, n) for v, n, _ in A2] == [('PASS', 'tape'), ('FAIL', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register')], A2\n"
         "CHAIN2 = sum(int(t) for _, _, t in A2)\n"
         "ic2 = rd(f'{SP}/ch32b_gates2/probe_ink_cache.out'); IC2 = R(r'^(\\d+/8 probes)$', ic2, 'ink cache second'); C6G2 = R(r'^\\s*FAIL C6 [^\\n]*?: (added: \\[.*\\]; lost: \\[.*\\])$', ic2, 'C6 groups second')\n"
         "RB2 = R(r'(readback_probes: \\d+/\\d+)', rd(f'{SP}/ch32b_gates2/probe_readback.out'), 'the second pass readback'); assert RB2.split(': ')[1].split('/')[0] == RB2.split('/')[1], RB2\n"
         "PROBES2 = re.findall(r'^  (\\w+): (\\d+/\\d+)$', rd(f'{SP}/ch32b_gates2/probes.out'), re.M); assert len(PROBES2) == 12 and [n for n, s_ in PROBES2 for a, b in [s_.split('/')] if a != b] == ['ink_cache'], PROBES2\n"
         "fb = rd(f'{SP}/ch32b_runner_fbind.out'); NFB, FBL1, FBL2 = re.search(r\"^edits (\\d+) over lines (\\d+)-(\\d+); F's globals write removed \\| WRITTEN$\", fb, re.M).groups(); FCALLS = R(r'^F calls in the file: (\\d+); module-level F statements: \\d+', fb, 'F calls'); assert FCALLS == NFB, (FCALLS, NFB)\n"
         "LINT2 = R(r'^gloss_lint: (\\d+) flag\\(s\\)$', rd(f'{SP}/ch32b_runner_lint2.out'), 'the runner lint after'); assert LINT2 == '0', LINT2\n"
         "MATRIX5 = R(r'^MATRIX: (\\d+/\\d+) cells match the answer sheet$', rd(f'{SP}/ch32_runner_run5.out'), 'the fifth graded run'); assert MATRIX5 == '72/72', MATRIX5\n"
         "CLEAR2 = R(r'^(INK CACHE cleared)', rd(f'{SP}/ch32b_cache_clear2.out'), 'the cache cleared again')\n"
         "done2 = rd(f'{SP}/ch32b_tail_chain2.DONE'); assert R(r'^runner rc=(\\d+)$', done2, 'runner rc') == '0' and R(r'^chain rc=(\\d+)$', done2, 'chain rc 2') == '0', done2", 'facts done')
f = sub1(f, "summ = rd(f'{SP}/ch32b_gates2_SUMMARY.txt'); assert 'FAILURES' not in summ", "summ = rd(f'{SP}/ch32b_gates3_SUMMARY.txt'); assert 'FAILURES' not in summ", 'facts summ')
f = sub1(f, "GD = f'{SP}/ch32b_gates2'", "GD = f'{SP}/ch32b_gates3'", 'facts GD')
f = sub1(f, "assert len(RBA_S) == 1, RBA_S; RBA_S = RBA_S[0]", "assert len(RBA_S) == 1, RBA_S; RBA_S = RBA_S[0]\nRUN5_S = [int(r[2]) for r in TAILROWS if 'fifth graded run' in r[1]]; assert len(RUN5_S) == 1, RUN5_S; RUN5_S = RUN5_S[0]", 'facts RUN5_S')
f = sub1(f, "D = dict(EXAMROWS=EXAMROWS,", "D = dict(CHAIN2=CHAIN2, IC2=IC2, C6G2=C6G2, RB2=RB2, NFB=NFB, FBL1=FBL1, FBL2=FBL2, LINT2=LINT2, MATRIX5=MATRIX5, CLEAR2=CLEAR2, RUN5_S=RUN5_S, EXAMROWS=EXAMROWS,", 'facts D')
ast.parse(f); open(f'{SP}/ch32b_tail_facts.py', 'w', encoding='utf-8').write(f); edits += 5
# ---- (2) the AS BUILT template ----
a = rd(f'{SP}/ch32b_asbuilt.txt')
a = sub1(a, "the chain's second pass from the tape ALL GREEN — and these records", "the chain's second pass from the tape RED ON THE CACHE PROBE AGAIN — the runner's own binding form the cause, read in the cache's code and the runner's source, its callee bindings retyped as assignments, the cache cleared again, the third pass from the tape ALL GREEN — and these records", 'asbuilt heading')
a = sub1(a, "%(CLEAR)s whole, THE SECOND PASS FROM THE TAPE ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps — the tape %(TAPE2)s,",
         "%(CLEAR)s whole, THE SECOND PASS FROM THE TAPE (%(CHAIN2)d s) RED ON THE CACHE PROBE AGAIN — %(IC2)s, C6 with OTHER groups (%(C6G2)s; %(RB2)s and every other suite green; the gates PASS; the long steps skipped): THE CAUSE READ IN THE CACHE'S CODE AND THE RUNNER'S SOURCE — the runner bound its callees' values through F('NAME', value), a helper writing globals(): the import cache's skip reads a statement's ast Store targets and these statements have none, so each RAN on the cached path and held the LIVE callee object while the older runners' names for the same DATA rows (covenant_return_charge's JR_FOUR, JR_DEATH and OH_CHAIN; refuge_war_family's and courts_prophet's RG_ONE — the printed groups two of many, the sets unordered) were restored copies; no cache clear reaches it; THE RETYPE BY AST (patch_runner_fbind_ch32b.py — %(NFB)s F statements over the runner's lines %(FBL1)s-%(FBL2)s became NAME = expr; F('NAME', NAME), F's globals() write removed, a comment above the def; the lint %(LINT2)s flags); THE SECOND TAIL JOB in one background wrapper (ch32b_tail_chain2.sh): the runner's fifth graded run MATRIX %(MATRIX5)s in %(RUN5_S)d s (a miss for its module alone), %(CLEAR2)s whole again, THE THIRD PASS FROM THE TAPE ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps — the tape %(TAPE2)s,", 'asbuilt tail')
a = sub1(a, "(14) THE CHAIN TWICE — four readback probes and the cache probe RED on its first pass, the readback suite run alone before the second (the snapshot served), the cache cleared whole, the second pass from the tape all green; (15)",
         "(14) THE CHAIN THRICE — four readback probes and the cache probe RED on its first pass, the readback suite run alone before the second (the snapshot served), the cache cleared whole; the cache probe RED AGAIN on the second pass (C6 with other groups — the cause the runner's own binding form, read in the cache's code and the runner's source), the callee bindings retyped as assignments and the cache cleared again, the third pass from the tape all green; (15)", 'asbuilt dep 14')
lines = a.split('\n'); assert lines[6].startswith('THE DEPARTURES') and lines[6].endswith("(19b's lesson 2 widened)."), lines[6][-80:]
lines[6] += " (16) THE RUNNER BOUND ITS CALLEES' VALUES THROUGH A HELPER WRITING globals() (F('NAME', value) — the derive's own form for the facts' print), not by assignment as the older runners do: the import cache's skip could not see the binding; retyped at the tail to NAME = expr; F('NAME', NAME) (%(NFB)s statements), F recording the fact alone."
assert lines[8].startswith('THE LESSONS') and lines[8].endswith('the records after the compaction.'), lines[8][-80:]
lines[8] += " (19) A MODULE-LEVEL NAME IS BOUND BY ASSIGNMENT, NEVER THROUGH A CALL THAT WRITES globals() — the import cache's skip reads a statement's ast Store targets: a name bound through a call RUNS on the cached path and holds the LIVE callee object while the older runners' names for the same DATA rows are restored copies; the cache probe C6 falls and no cache clear reaches it (18b's lesson 11 is the harvest's half of the rule, this its binding half; C6's printed groups are two of many — the sets unordered, the groups differ between passes); the form NAME = expr; F('NAME', NAME) — the fact recorded beside the binding, the sharing groups kept."
a = '\n'.join(lines); open(f'{SP}/ch32b_asbuilt.txt', 'w', encoding='utf-8').write(a); edits += 5
# ---- (3) the records writer ----
r = rd(f'{SP}/write_ch32b_records.py')
r = sub1(r, "assert '\\n#236 (' in sd and '\\n#236 ADDENDUM 1 (' in sd and 'THE TAIL OF 20b (' not in sd", "assert '\\n#236 (' in sd and '\\n#236 ADDENDUM 1 (' in sd and '\\n#236 ADDENDUM 2 (' in sd and 'THE TAIL OF 20b (' not in sd", 'records sd assert')
r = sub1(r, "i236 = sd.index('\\n#236 ADDENDUM 1 (')", "i236 = sd.index('\\n#236 ADDENDUM 2 (')", 'records i236')
r = sub1(r, "the records after the compaction at addendum 1, on his word): the chain's first SUMMARY", "the records after the compactions at addenda 1 and 2, on his word): the chain's first SUMMARY", 'records note words')
r = sub1(r, "the import cache cleared whole (18b's lesson 11), THE SECOND PASS FROM THE TAPE ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps — the tape %(TAPE2)s;",
         "the import cache cleared whole (18b's lesson 11), THE SECOND PASS FROM THE TAPE (%(CHAIN2)d s) RED ON THE CACHE PROBE AGAIN (%(IC2)s — C6 with other groups: %(C6G2)s; %(RB2)s and every other suite green; the gates PASS; the long steps skipped): THE CAUSE READ IN THE CACHE'S CODE AND THE RUNNER'S SOURCE — its callees' values bound through F('NAME', value), a helper writing globals(): the cache's skip reads a statement's ast Store targets and these statements have none, so each RAN on the cached path and held the LIVE callee object while the older runners' names for the same DATA rows (covenant_return_charge's JR_FOUR, JR_DEATH, OH_CHAIN; refuge_war_family's and courts_prophet's RG_ONE) were restored copies — no cache clear reaches it; THE RETYPE BY AST (patch_runner_fbind_ch32b.py — %(NFB)s F statements over the runner's lines %(FBL1)s-%(FBL2)s became NAME = expr; F('NAME', NAME), F's globals() write removed; the lint %(LINT2)s flags); THE SECOND TAIL JOB in one wrapper (ch32b_tail_chain2.sh): the runner's fifth graded run MATRIX %(MATRIX5)s in %(RUN5_S)d s, %(CLEAR2)s whole again, THE THIRD PASS FROM THE TAPE ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps — the tape %(TAPE2)s;", 'records note tail')
r = sub1(r, "the departures 1-15 and the lessons 1-18), the forms copied, the commit message", "the departures 1-16 and the lessons 1-19), the forms copied, the commit message", 'records note counts')
r = sub1(r, "(the cache cleared whole), ALL GREEN on its second pass from the tape (sweep %(SWEEP)s)", "(the cache cleared whole); the cache probe RED AGAIN on its second pass — the runner bound its callees through a helper writing globals(), a binding the import cache's skip cannot see: %(NFB)s bindings retyped as assignments by ast, the cache cleared again; ALL GREEN on its third pass from the tape (sweep %(SWEEP)s)", 'records debt')
r = sub1(r, "chain: four readback probes + the cache probe RED once (the reuses, the rain — retyped from the print; the cache cleared), then ALL GREEN (sweep %s)", "chain THRICE: 4 readback probes + the cache probe RED on pass 1 (the reuses, the rain — retyped; cache cleared); the cache probe RED again on pass 2 (the runner bound callees via globals() — retyped as assignments); ALL GREEN on pass 3 (sweep %s)", 'records SEC2')
rl = r.split('\n'); k = [i for i, l in enumerate(rl) if l.startswith('NEWL = "20b DONE')]; assert len(k) == 1, k
rl[k[0]] = ('NEWL = "20b DONE 2026-09-28 at #236 + its NOTE (the compile — the 77th runner song_charge_nebo %s in six parts + the generated cases; %s kinds in three forms / %s effects + %s seats; NO MARKER; the tape %s on its second run; %d edges; the chain THRICE: pass 1 four readback probes + the cache probe RED (the reuses, the rain — retyped from the print; the cache cleared), pass 2 the cache probe RED AGAIN (C6 — the runner bound its callees via a helper writing globals(), unseen by the cache\'s skip: %s bindings retyped as assignments), pass 3 from the tape ALL GREEN; RUN B\'s window 825k — THE CAP BROKEN: a big-callee compile splits RUN B), UNCOMMITTED since 7798bee; NEXT: the commit on his word (20b alone), then 21 (the reading of 33, lean) after a compaction" % (MATRIX, KADD, EADD, SEATS, VS[-1], MINE, NFB)')
r = '\n'.join(rl)
r = sub1(r, "the chain ALL GREEN on its second pass; RUN B\\'s window 825k", "the chain ALL GREEN on its third pass; RUN B\\'s window 825k", 'records description')
r = sub1(r, "(the tail, after the compaction at #236, on \\\"Reread and go\\\"; the records after the compaction at addendum 1)", "(the tail, after the compaction at #236, on \\\"Reread and go\\\"; the records after the compactions at addenda 1 and 2)", 'records mw words')
r = sub1(r, "ONE background job — the readback suite alone %(RBA)s in %(RBA_S)d s, the cache cleared whole, the second pass from the tape ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps;",
         "TWO background jobs — the first: the readback suite alone %(RBA)s in %(RBA_S)d s, the cache cleared whole, the second pass from the tape (%(CHAIN2)d s) RED on the cache probe again (%(IC2)s — C6: the runner bound its callees' values through a helper writing globals(), a binding the cache's skip cannot see — those statements ran live on the cached path beside the older runners' restored copies of the same DATA rows); %(NFB)s bindings retyped as assignments by ast (the lint %(LINT2)s); the second: the fifth graded run MATRIX %(MATRIX5)s, the cache cleared again, the third pass from the tape ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d steps;", 'records mw jobs')
r = sub1(r, "the departures 1-15, the lessons 1-18), the forms copied, the message built", "the departures 1-16, the lessons 1-19), the forms copied, the message built", 'records mw counts')
r = sub1(r, "after editing older runners the import cache is cleared whole before the chain (C6);", "after editing older runners the import cache is cleared whole before the chain (C6); a module-level name is bound by assignment, never through a call writing globals() — the cache's skip reads ast Store targets (C6 a second time, after the clear);", 'records mw lesson')
ast.parse(r); open(f'{SP}/write_ch32b_records.py', 'w', encoding='utf-8').write(r); edits += 13
# ---- (4) the commit message writer ----
c = rd(f'{SP}/write_ch32b_commit_msg.py')
c = sub1(c, "THE CHAIN TWICE — FOUR OLDER PROBES AND THE CACHE PROBE RED ON THE FIRST PASS BY THE REUSES AND THE RAIN, RETYPED FROM THE PRINT AND THE CACHE CLEARED, ALL GREEN ON THE SECOND — THE FULL PROCESS OWED)",
         "THE CHAIN THRICE — FOUR OLDER PROBES AND THE CACHE PROBE RED ON THE FIRST PASS BY THE REUSES AND THE RAIN, RETYPED FROM THE PRINT AND THE CACHE CLEARED; THE CACHE PROBE RED AGAIN ON THE SECOND — THE RUNNER BOUND ITS CALLEES THROUGH A HELPER WRITING globals(), A BINDING THE CACHE'S SKIP CANNOT SEE, RETYPED AS ASSIGNMENTS AND THE CACHE CLEARED AGAIN; ALL GREEN ON THE THIRD — THE FULL PROCESS OWED)", 'commit head')
c = sub1(c, '"Reread and go" (THE TAIL, after the compaction at #236; the records after the compaction at its addendum 1, on his word), 2026-09-28;', '"Reread and go" (THE TAIL, after the compaction at #236), "Reread and go" (its second half, after the compaction at addendum 1) and his word after the compaction at addendum 2 (its third part — these records), 2026-09-28;', 'commit words')
c = sub1(c, "the state doc's #235, #236, its addendum 1 and its NOTE", "the state doc's #235, #236, its addenda 1-2 and its NOTE", 'commit state doc')
c = sub1(c, "one background job — the readback suite alone %(RBA)s, the cache cleared whole, the second pass from the tape ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d s",
         "two background jobs — the readback suite alone %(RBA)s, the cache cleared whole, the second pass from the tape (%(CHAIN2)d s) RED ON THE CACHE PROBE AGAIN (%(IC2)s — C6 with other groups: the runner bound its callees' values through F('NAME', value), a helper writing globals(), a binding the cache's skip cannot see — the statements ran live on the cached path beside the older runners' restored copies of the same DATA rows; %(NFB)s bindings retyped as assignments by ast, F's globals() write removed, the lint %(LINT2)s), the fifth graded run MATRIX %(MATRIX5)s, the cache cleared again, the third pass from the tape ALL GREEN in %(CHAIN_S)d s (%(NCHAIN)d s", 'commit jobs')
c = sub1(c, "the departures 1-15 and the lessons 1-18, the state doc", "the departures 1-16 and the lessons 1-19, the state doc", 'commit counts')
ast.parse(c); open(f'{SP}/write_ch32b_commit_msg.py', 'w', encoding='utf-8').write(c); edits += 5
# ---- (5) the copier's lists, by ast (the list literal's closing bracket) ----
cp = rd(f'{SP}/copy_ch32_forms.py'); b = cp.encode('utf-8'); t = ast.parse(cp); starts = [0]
for line in b.split(b'\n'): starts.append(starts[-1] + len(line) + 1)
ADDS = {'PY': ['patch_runner_fbind_ch32b.py', 'edit_ch32b_tail2_writers.py', 'write_ch32b_point4.py'],
        'OUT': ['ch32b_runner_fbind_check.out', 'ch32b_runner_fbind.out', 'ch32b_runner_lint2.out', 'ch32b_tail_chain2.sh', 'ch32b_tail_chain2.log', 'ch32b_tail_chain2.DONE', 'ch32_runner_run5.out', 'ch32b_cache_clear2.out', 'ch32b_gates3_SUMMARY.txt', 'ch32b_gates3.log', 'ch32b_writers_edit.out', 'ch32b_point4_check.out', 'ch32b_point4_write.out', 'ch32b_forms5.out', 'ch32b_home5.out']}
ins = []
for n in t.body:
    if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ADDS:
        v = n.value
        while isinstance(v, ast.BinOp): v = v.left
        assert isinstance(v, ast.List), (n.targets[0].id, type(v).__name__)
        end = starts[v.end_lineno - 1] + v.end_col_offset - 1; assert b[end:end + 1] == b']', b[end - 20:end + 2]
        present = {e.value for e in v.elts if isinstance(e, ast.Constant)}; new = [x for x in ADDS[n.targets[0].id] if x not in present]
        ins.append((end, (', ' + ', '.join(repr(x) for x in new)).encode('utf-8'), n.targets[0].id, len(new)))
assert len(ins) == 2, ins
for end, txt, nm, k in sorted(ins, reverse=True): b = b[:end] + txt + b[end:]; edits += k
cp2 = b.decode('utf-8'); ast.parse(cp2)
t2 = ast.parse(cp2); got = {n.targets[0].id: [e.value for e in ast.walk(n.value) if isinstance(e, ast.Constant) and isinstance(e.value, str)] for n in t2.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ADDS}
assert all(x in got[k] for k in ADDS for x in ADDS[k]) and 'ch32_spine_p{p}.txt' in got['OUT'], 'the copier lists'
open(f'{SP}/copy_ch32_forms.py', 'w', encoding='utf-8').write(cp2)
for p in ('ch32b_tail_facts.py', 'write_ch32b_records.py', 'write_ch32b_commit_msg.py', 'copy_ch32_forms.py', 'ch32b_asbuilt.txt'):
    x = rd(f'{SP}/{p}'); assert not re.search(r'[֐-׿]', x) and os.path.expanduser('~') not in x and SP not in x, p
print('THE WRITERS AMENDED: %d edits over five files; the AS BUILT template %d bytes, %d placeholders; the copier lists +%d +%d | WRITTEN' % (edits, len(a.encode()), len(re.findall(r'%\((\w+)\)[sd]', a)), ins[0][3], ins[1][3]))
