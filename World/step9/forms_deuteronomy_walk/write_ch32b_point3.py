import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (LEAN): THE CLEAN COMPACTION POINT AT THE TAIL'S HALF — the state doc's #236 ADDENDUM 1, the recovery page's section-2 last bullet, MEMORY.md's walk
# line's tail — written in ONE call after the chain's first summary was read, the probes retyped and the tail job launched; every number READ FROM ITS PRINT (the first
# SUMMARY, the readback and cache probe prints, the retypes' print, the readback suite alone, the timing table); the caps and the lints asserted. --check prints without writing.
# RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; MM = f'{MEM}/MEMORY.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
summ1 = rd(f'{SP}/ch32b_gates_SUMMARY.txt'); assert 'FAIL probes' in summ1
CHAIN1 = sum(int(t) for _, _, t in re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ1, re.M))
RB1 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_gates/probe_readback.out'), 'readback first'); RB1Q = ', '.join(sorted(re.findall(r'^\s*FAIL (Q\d+) ', rd(f'{SP}/ch32b_gates/probe_readback.out'), re.M), key=lambda q: int(q[1:])))
IC1 = R(r'^(\d+/8 probes)$', rd(f'{SP}/ch32b_gates/probe_ink_cache.out'), 'ink cache first'); assert 'FAIL C6' in rd(f'{SP}/ch32b_gates/probe_ink_cache.out')
ret = rd(f'{SP}/ch32b_probes_retypes.out'); NRET = R(r'^edits (\d+) \(the walker (\d+) \+ RE (\d+) \+ the generator 1\) over (\d+) probes; comment lines \d+ \| WRITTEN$', ret, 'retypes'); NRETW = R(r'^edits \d+ \(the walker (\d+) \+', ret, 'walker'); NRETP = R(r'over (\d+) probes; comment lines', ret, 'probes'); RETQ = R(r"^failing probes read from the print: (\[.*\])$", ret, 'q list')
RBA = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_probes_after_retypes.out'), 'readback alone'); assert RBA.split(': ')[1].split('/')[0] == RBA.split('/')[1], RBA
CLEAR = R(r'^(INK CACHE cleared)', rd(f'{SP}/ch32b_cache_clear.out'), 'cleared')
tsv = rd(f'{SP}/ch32b_timing.tsv'); rows = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('20b')]
RBA_S = [int(r[2]) for r in rows if 'the readback suite alone' in r[1]]; assert len(RBA_S) == 1; RBA_S = RBA_S[0]; NSTEP = len(rows); SECS = sum(int(r[2]) for r in rows)
assert not os.path.exists(f'{SP}/ch32b_tail_chain.DONE'), 'the job has ended — run the records writer, not this point'
for f in ('ch32b_tail_facts.py', 'ch32b_asbuilt.txt', 'write_ch32b_records.py', 'write_ch32b_commit_msg.py'): assert os.path.exists(f'{SP}/{f}'), f
sd = rd(SD); assert '\n#236 (' in sd and '\n#236 ADDENDUM 1 (' not in sd and sd.find('\n#2', sd.index('\n#236 (') + 5) < 0
ADD = ('\n\n#236 ADDENDUM 1 (2026-09-28, at THE TAIL\'s half — sitting 20b, on the owner\'s "Reread and go" after the compaction at #236; A CLEAN COMPACTION POINT WITH THE TAIL JOB RUNNING IN THE BACKGROUND): THE REREADS done (the recovery page, the map\'s newest section — the 20b design whole, MEMORY.md, #236). '
       'THE CHAIN\'S FIRST SUMMARY READ ONCE (ch32b_gates_SUMMARY.txt; %d s): the tape PASS; the probes FAIL on two suites — %s (%s: heaven_and_earth_witness 4 -> 5 on Israel by the chain\'s fifth seat at 32:1 and the last entry\'s source head; the song\'s doctrine as rain in chapter 11\'s two rain lists; 18b\'s kin tuple; 19b\'s reuse count, heaven count and two w59 seats by the heaven reuses) and the import cache %s (C6 — the sharing groups after a partial re-harvest: the three older runners edited at RUN B; 18b\'s lesson 11); every other suite green; the daemon, dependency, build, journal and register --strict gates PASS; the long steps skipped. '
       'THE RETYPES FROM THE PRINT (patch_probes_retypes_ch32b.py by ast — %s edits over %s probes %s: %s by the walker, q48\'s RE number and its w59 seats by name inside the generators — 19b\'s lesson 16 met before the second pass; a 20b comment line above each return). '
       'THE TAIL JOB LAUNCHED in one background wrapper (ch32b_tail_chain.sh; DONE file <scratch>/ch32b_tail_chain.DONE): (1) the readback suite alone — %s in %d s (the snapshot served); (2) %s whole; (3) the chain\'s second pass from the tape into ch32b_gates2 (the positions at four workers) — RUNNING, its SUMMARY copied to ch32b_gates2_SUMMARY.txt when it ends. '
       'THE RECORDS\' WRITERS WRITTEN AND PARSED while the job runs, their prints read when it ends: ch32b_tail_facts.py (every number from its print), ch32b_asbuilt.txt (the AS BUILT template — the departures 1-15, the lessons 1-18, the finds, the timing table), write_ch32b_records.py (the map\'s AS BUILT, this doc\'s NOTE after this addendum, the recovery page, the memory, COMPILE_DEBT\'s line (13)), write_ch32b_commit_msg.py (20b alone — 20 pushed at 7798bee). THE COST FINDING: RUN B\'s window ran to 825k before its compaction — the cap broken; a big-callee compile splits its RUN B (the AS BUILT\'s lesson 17). %d timed steps, %d machine seconds so far. '
       'NEXT: after the compaction, on his word ("Reread", then "Go") — THE REREADS; the job\'s DONE file and SUMMARY read once (cat <scratch>/ch32b_tail_chain.DONE; cat <scratch>/ch32b_gates2_SUMMARY.txt); if ALL GREEN: from the repo root with PYTHONPATH the scratchpad, write_ch32b_records.py --check then without --check, write_ch32b_commit_msg.py, the forms (copy_ch32_forms.py — its lists extended with the tail\'s files), the home-path gate; if a step is RED: the demand read from its print and filed, then a pass from the tape again; THE COMMIT ON HIS WORD ONLY. POST-COMPACTION REREADS: the recovery page, the map\'s newest section, MEMORY.md; then this addendum.'
       % (CHAIN1, RB1, RB1Q, IC1, NRET, NRETP, RETQ, NRETW, RBA, RBA_S, CLEAR, NSTEP, SECS))
rec = rd(REC); old = [l for l in rec.split('\n') if l.startswith('- SITTING 20b RUN B (ch 32 COMPILE, LEAN) at #236:')]; assert len(old) == 1, old
NEWB = ('- SITTING 20b TAIL (ch 32 COMPILE, LEAN) at #236 + add. 1: chain pass 1 — %s + cache %s RED, retyped (%s edits); THE TAIL JOB RUNNING (readback alone %s; cache cleared; pass 2 from the tape; DONE <scratch>/ch32b_tail_chain.DONE). NEXT: its SUMMARY once; write_ch32b_records.py --check, then write; the message; the forms; commit on his word.' % (RB1.replace('readback_probes: ', 'readback '), IC1.replace(' probes', ''), NRET, RBA.replace('readback_probes: ', '')))
rec2 = rec.replace(old[0], NEWB); rec2 = rec2.replace('## 2. WHERE IT STANDS (2026-09-28; #236 — sitting 20b RUN B, newest)', '## 2. WHERE IT STANDS (2026-09-28; #236 + add. 1 — sitting 20b TAIL, newest)'); assert rec2 != rec
mm = rd(MM); OLDT = "THE GATES CHAIN LAUNCHED, its summary unread); NEXT: THE TAIL (the summary read once, the demands, the records, COMPILE_DEBT's line, the forms, the message), then the commit on his word"; assert mm.count(OLDT) == 1
NEWT = "the chain's first pass: %s + the cache probe %s RED (the reuses, the rain) — retyped from the print, the cache cleared, the second pass from the tape RUNNING in the background); NEXT: THE TAIL's second half after a compaction (the job's SUMMARY once, the records, the message, the forms), then the commit on his word" % (RB1.replace('readback_probes: ', 'readback '), IC1.replace(' probes', ''))
mm2 = mm.replace(OLDT, NEWT)
for t in (ADD, NEWB, NEWT): assert not re.search(r'[֐-׿]', t) and os.path.expanduser('~') not in t and SP not in t
assert len(rec2.encode()) <= 10240 and len(mm2.encode()) < 17000, (len(rec2.encode()), len(mm2.encode()))
LINT = {}
for p in (SD, REC, MM):
    r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); LINT[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
print('THE POINT %s: addendum %d bytes; the recovery page %d; MEMORY.md %d; the lints before %s' % ('CHECKED' if CHECK else 'WRITTEN', len(ADD.encode()), len(rec2.encode()), len(mm2.encode()), LINT))
if not CHECK:
    open(SD, 'a', encoding='utf-8').write(ADD); open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2)
    L2 = {}
    for p in (SD, REC, MM):
        r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); L2[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
    assert L2 == LINT, (LINT, L2); print('every lint unmoved:', L2)
