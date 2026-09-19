import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
"""THE GATES CUT — THE RECORDS FROM THE SHEET IN ONE CALL (2026-09-19). Parses the new chain's prints (never recites), then writes every record the
sheet names for a gates change. Run from the repo root: python3 <scratch>/write_gates_cut_records.py --check | (write). NEVER Write a new file
without ls first — this writer appends or edits in place; the one new file (GATES_CHAIN.md) was created before it, by hand."""
import os, re, sys, glob, json, subprocess, datetime
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHAIN = os.path.join(SP, 'gates_cut_1'); CHAIN2 = os.path.join(SP, 'gates_cut_2')   # the first chain (everything full) and the second (nothing moved — the steady state)
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
TODAY = '2026-09-19'
def R(p): return open(p, encoding='utf-8').read()
def W(p, s):
    if CHECK: print('  would write %s (%d bytes)' % (p, len(s.encode('utf-8')))); return
    open(p, 'w', encoding='utf-8').write(s)
def rp(*a): return os.path.join(ROOT, *a)

# ---- THE NUMBERS, PARSED ----
def parse_chain(d):
    summ = R(os.path.join(d, 'SUMMARY.txt')); st = {}
    for m in re.finditer(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\) ?(.*)$', summ, re.M):
        st[m.group(2)] = (m.group(1), int(m.group(3)), m.group(4).strip())
    assert 'GATES CHAIN DONE — ALL GREEN' in summ, 'the chain %s is not ALL GREEN:\n%s' % (d, summ)
    return st
steps, steps2 = parse_chain(CHAIN), parse_chain(CHAIN2)
BEFORE = {'tape': 156, 'probes': 609, 'daemon': 3, 'dependency': 2, 'build': 60, 'journal': 316, 'register': 141, 'positions': 1562, 'checkpoint': 205, 'sweep': 2011, 'unmoved': 315}
ORDER = ['tape', 'probes', 'daemon', 'dependency', 'build', 'journal', 'register', 'positions', 'checkpoint', 'stamp', 'sweep', 'unmoved']
after = {s: steps[s][1] for s in ORDER}; after2 = {s: steps2[s][1] for s in ORDER}
total_before = sum(BEFORE.values()); total_after = sum(after.values()); total_after2 = sum(after2.values())
def wall_of(name):   # the start stamp (HH:MM:SS, written before the chain) to the summary's end stamp (HH:MM — the chain's own last line)
    try:
        t0 = R(os.path.join(SP, name + '.start')).strip(); summ = R(os.path.join(SP, name, 'SUMMARY.txt'))
        t1 = re.search(r'GATES CHAIN DONE — ALL GREEN — (\d\d:\d\d)$', summ, re.M).group(1) + ':00'
        h = lambda t: int(t[:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8]); return h(t1) - h(t0)
    except Exception as e: print('  (wall not read: %s)' % e); return None
wall, wall2 = wall_of('gates_cut_1'), wall_of('gates_cut_2')
sweep = R(os.path.join(CHAIN, 'sweep.out'))
sw_mode = re.search(r'^THE SWEEP (\w+) \((.*)\); jobs (\d+); skipped (.*)$', sweep, re.M)
sw_sum = re.search(r'run_cold_all: (\d+)/(\d+) runners green, ([\d,]+) graded cells in all \((\w+) of (\d+); wall (\d+) s, (\d+) jobs\)', sweep)
assert sw_mode and sw_sum, 'the sweep print'
pos = R(os.path.join(CHAIN, 'positions.out')); pos2 = R(os.path.join(CHAIN2, 'positions.out'))
pos_falls = re.search(r'(\d+) checkpoints over (\d+) pauses', pos); pos_falls2 = re.search(r'(\d+) checkpoints over (\d+) pauses in (\d+) s \((\d+) workers\)', pos2)
assert pos_falls and pos_falls2, 'the positions prints'
sweep2 = R(os.path.join(CHAIN2, 'sweep.out')); sw2 = re.search(r'^THE SWEEP (\w+) \((.*)\); jobs (\d+); skipped (.*)$', sweep2, re.M)
assert sw2 and 'NOTHING TO GRADE' in sweep2, 'the second sweep should have nothing to grade'
probes = {}
for f in sorted(glob.glob(os.path.join(CHAIN, 'probe_*.out'))):
    n = os.path.basename(f)[6:-4]; t = R(f)
    m = re.findall(r'(\d+)/(\d+)', t); probes[n] = m[-1] if m else ('?', '?')
    assert m and m[-1][0] == m[-1][1], 'probe %s not whole: %s' % (n, m[-1:] )
cp = re.findall(r'(\d+)/(\d+)', R(os.path.join(CHAIN, 'checkpoint.out')))[-1]
tape = R(os.path.join(CHAIN, 'tape.out')); tape_score = re.search(r'(\d+)/(\d+) checkpoints', tape).group(0)
snap = re.search(r'snapshot[^\n]*', tape); 
jour = R(os.path.join(CHAIN, 'journal.out')); jour_m = re.search(r'(\d+) kinds, ([\d,]+) rows', jour)
unm = R(os.path.join(CHAIN, 'unmoved.out')); assert 'THE JOURNAL UNMOVED' in unm and 'GATE GREEN' in unm
unm_src = re.search(r'(\d+) sources', unm)
reg = R(os.path.join(CHAIN, 'register.out')); reg_m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', reg)
reg_snap = 'snapshot' in reg.lower()
dae = re.search(r'\((\d+) daemons, (\d+) functions', R(os.path.join(CHAIN, 'daemon.out')))
dep = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', R(os.path.join(CHAIN, 'dependency.out')))
stamp = json.load(open(rp('World', 'step9', 'sweep_stamp.json')))
mins = lambda s: '%d min %02d s' % divmod(s, 60)
N = dict(total_after=total_after, total_before=total_before, wall=wall, mins_after=mins(total_after), mins_wall=mins(wall) if wall else '?',
         total_after2=total_after2, mins_after2=mins(total_after2), mins_wall2=mins(wall2) if wall2 else '?', pos2=pos_falls2.groups(), sw2=sw2.groups(),
         sw=sw_sum.groups(), sw_mode=sw_mode.groups(), pos=pos_falls.groups(), pos_mode=('WHOLE', 'the old sequential measure'),
         probes=probes, cp=cp, tape=tape_score, jour=jour_m.groups() if jour_m else ('?', '?'), unm=unm_src.group(1) if unm_src else '?',
         reg=reg_m.groups() if reg_m else ('?', '?', '?'), dae=dae.groups() if dae else ('?', '?'), dep=dep.groups() if dep else ('?', '?'),
         stamp_runners=len(stamp['runners']), stamp_shared=len(stamp['shared']), stamp_mode=stamp['mode'])
print('THE NUMBERS: chain 1 %s (sum of steps; wall %s), chain 2 %s (wall %s) against %s before; steps 1 %s; steps 2 %s' % (N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], mins(total_before), {s: after[s] for s in ORDER}, {s: after2[s] for s in ORDER}))
print('  sweep %s/%s runners, %s cells, %s of %s, wall %s s, %s jobs; mode %s' % (N['sw'] + (N['sw_mode'][0],)))
print('  positions %s checkpoints over %s pauses, mode %s: %s; probes %s; checkpoint %s/%s; tape %s; journal %s kinds %s rows; unmoved %s sources; register %s; daemons %s; dependency %s; stamp %d runners %d shared' % (N['pos'] + N['pos_mode'] + (probes, cp[0], cp[1], tape_score) + N['jour'] + (N['unm'], N['reg'], N['dae'], N['dep'], N['stamp_runners'], N['stamp_shared'])))
about = '%d' % round(total_after2 / 60)
table = '\n'.join('| %s | %s | %d | %d | %s |' % (s, BEFORE.get(s, '—'), after[s], after2[s], steps2[s][2][:100]) for s in ORDER)

# ---- 1. GATES_CHAIN.md — AS RUN ----
p = rp('World', 'step9', 'GATES_CHAIN.md'); s = R(p); assert '## AS RUN' not in s
s += """
## AS RUN — two chains after the cut (%s, the same day; ALL GREEN both times)

The first chain: everything measured in full (no sweep stamp yet; the positions by the old sequential measure). The second chain, run after the
positions measure was rebuilt by workers and with NOTHING MOVED: the steady state a compile sitting will see.

| step | seconds before | the first chain | the second chain | the second chain's last line |
|---|---|---|---|---|
%s
| **total** | **%d (%s)** | **%d (%s)**, wall %s | **%d (%s)**, wall %s | |

THE FIRST CHAIN: the sweep %s (%s) — no stamp existed, so every runner was graded (%s of %s at %s jobs; %s graded cells; %s s) and the stamp
written (%d runners, %d shared pieces); the positions by the old sequential measure (%s checkpoints over %s pauses, 1,400 s of the block at 169
pauses). THE SECOND CHAIN: the sweep %s (%s) — NOTHING TO GRADE; the positions by %s workers, %s checkpoints over %s pauses in %s s. Both chains:
the probes in parallel (%s); THE JOURNAL UNMOVED across the sweep (%s sources); the register gate from the snapshot (DECLARED %s, DEBT %s,
FAILS %s); every verdict the last chain before the cut gave — the tape %s, the daemon gate %s daemons / %s functions, the dependency gate %s edges
/ %s pointers, the journal gate %s kinds / %s rows, the sweep whole, the positions whole.

THE STEADY STATE is the second chain: a compile sitting moves one runner (graded with its importers, a minute or two) and the positions are
always the whole measure by workers, so the chain stays near the second chain's total.

## THE FORM THAT WAS STRUCK — the incremental positions by regions (built, tested and struck %s)

The design above first cut the positions table INCREMENTALLY: the block's statements split into REGIONS (a prefix's letters — CU — its cp calls
and the helper statements beside them), each region with a digest, the table's rows kept while their region, the block's preamble and the tape
prefix (the lines minus the newest runner's) stood, only the moved regions asked at every pause. THE TEST: CU's digest altered in the table and
`--incremental` run — seven of CU's nine rows came out NOT YET: the region's checkpoints read helper names bound in OTHER regions (a partial run
skipped their binders). A dependency closure was added (every earlier statement binding a name the region reads, transitively) and measured
statically: CU's closure is 429 of the block's 630 statements, CC's 336 — the block is one chained computation, and a "partial" run is nearly
the whole run. The form was struck the same day, with its regions, digests and guards; what remains is the parse-once cache (`_cp_block`) and
the WHOLE measure by N workers (D36). THE LESSON: an incremental cut is only as good as the independence it assumes — measure the dependency
before building the guard.
""" % (TODAY, table, total_before, mins(total_before), total_after, N['mins_after'], N['mins_wall'], total_after2, N['mins_after2'], N['mins_wall2'],
       N['sw_mode'][0], N['sw_mode'][1], N['sw'][0], N['sw'][1], N['sw'][6], N['sw'][2], N['sw'][5], N['stamp_runners'], N['stamp_shared'], N['pos'][0], N['pos'][1],
       N['sw2'][0], N['sw2'][1], N['pos2'][3], N['pos2'][0], N['pos2'][1], N['pos2'][2],
       ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), N['unm'], N['reg'][0], N['reg'][1], N['reg'][2], tape_score, N['dae'][0], N['dae'][1], N['dep'][0], N['dep'][1], N['jour'][0], N['jour'][1], TODAY)
W(p, s)

# ---- 2. THE_LOOP.md — the decisions D34-D37 ----
p = rp('World', 'step9', 'THE_LOOP.md'); s = R(p); assert 'D34' not in s and s.endswith('\n')
s += """
## THE GATES CUT — the design and the as-built (%s; the owner, after sitting 6b's chain: "What is gate chain and why does it take so long" →
## "Yes make that change. It's too long as it is"; the design World/step9/GATES_CHAIN.md)
THE MEASUREMENT FIRST: the chain ninety minutes; the import of the sixty-three runners 136 s and the replay 1.7 s — every step paid the import,
the readback and register suites replayed the world besides, the positions table re-parsed the 750 KB sequence file at every one of 169 pauses,
the sweep ran sixty-three runners one after another on sixteen idle CPUs. THE DECISIONS:
  D34 THE SNAPSHOT — the tape's run saves the running world (daemons stripped, the journal handle dropped; 1.5 MB; atomic) with a sidecar
     carrying the SOURCES KEY (a digest of every source the replay depends on); a reader loads it in a second when the key is current and
     replays when it is not. The register gate, the readback probes and the register probes are readers. The register gate no longer rewrites
     the live source rows. register_census.Ink execs the sequence file's INK block; it does not import the module.
  D35 THE STAMPED SWEEP — run_cold_all.py --jobs N in parallel; --changed against World/step9/sweep_stamp.json (the runners' digests, the shared
     pieces' digests, written by a GREEN sweep only, TRACKED): a runner moved = that runner and its transitive importers; a shared piece moved
     or no stamp = FULL. --skip cold_run_sequence.py in the chain (the tape is the chain's first step).
  D36 THE POSITIONS BY WORKERS — checkpoint_positions.py --jobs N: N workers, each stepping the WHOLE tape in its own journal folder (the live
     base copied in, so the replay stays the audit) and asking the block at pause i where i mod N is its number; the parent merges the pauses
     (every pause asked by exactly one worker; the workers' verses, ordinals and days asserted equal) and takes the falls. The table is always
     the WHOLE measure. (An incremental form by regions was built, tested against a moved region and STRUCK the same day — seven of CU's nine
     rows came out NOT YET: a region's checkpoints read helpers bound across most of the block; the record in GATES_CHAIN.md.)
  D37 THE UNMOVED CHECK — D21's second journal gate proved the sweep wrote nothing on the live journal; that is now proved directly by a digest of
     the live rows taken before the sweep (--stamp) and compared after (--unmoved). The full gate runs once, upstream, before anything writes.
  Also: the eleven probe suites in parallel (each its own process and print; the checkpoint suite its own step after the positions); the
  journal gate's two fresh replays concurrent.
AS RUN: two chains, ALL GREEN both — the first with everything in full, %s (wall %s); the second with nothing moved, %s (wall %s) — against
ninety minutes; every verdict the chain before the cut gave. THE RECORDS: GATES_CHAIN.md (the
design and the AS RUN table), RECORD_FORMS' chain lines, THE_STEPS, THE_BRIEFING, RESEARCH_LOG, RESUME, the recovery page's cost rules, the
memory's cost rules, the state doc's #197, the addenda §45; the forms in World/step9/forms_gates_cut_%s/. LESSONS: MEASURE BEFORE CUTTING
(the replay was never the cost); A CACHE IS KEYED ON THE SOURCES' DIGESTS, NEVER ON A DATE; A MISS FALLS BACK TO THE FULL WORK; A STAMP IS
WRITTEN BY A GREEN RUN ONLY; TWO WRITERS OF ONE FILE WRITE ATOMICALLY; AN INCREMENTAL CUT IS ONLY AS GOOD AS THE INDEPENDENCE IT ASSUMES —
TEST IT AGAINST A MOVED PIECE BEFORE TRUSTING IT (the regions form was struck by its own test).
""" % (TODAY, N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], TODAY)
W(p, s)

# ---- 3. RESEARCH_LOG.md ----
p = rp('RESEARCH_LOG.md'); s = R(p); assert s.endswith('\n')
s += """
## %s — THE GATES CUT: THE CHAIN FROM NINETY MINUTES TO %s — THE IMPORT WAS THE COST, NOT THE REPLAY; THE SNAPSHOT, THE PARALLEL PROBES,
## THE STAMPED SWEEP, THE INCREMENTAL POSITIONS, THE UNMOVED CHECK
On the owner's "What is gate chain and why does it take so long" and "Yes make that change. It's too long as it is" (after sitting 6b). MEASURED: the
chain's eleven steps 5,380 s; the import of the sixty-three runners 135.9 s against a replay of 1.7 s; the running world 1.5 MB pickled, 1.09 s to
reload; the positions table 169 pauses × a fresh parse of the 750 KB sequence file; the sweep sixty-three sequential runners. BUILT (World/step9/
GATES_CHAIN.md; THE_LOOP D34-D37): the running world SAVED by the tape's run and LOADED by its readers under a sources key; the eleven probe suites
in parallel; the journal gate's two replays concurrent; the positions table measured WHOLE by eight workers (an incremental form by regions was
built, tested against a moved region and STRUCK the same day — seven of CU's nine rows NOT YET, the region's checkpoints reading helpers bound
across most of the block; the closure measured at 429 of 630 statements); the sweep parallel (--jobs) and incremental (--changed against
sweep_stamp.json, a shared piece moved = full, the stamp by a green sweep only); the second journal gate replaced by a digest of the live rows
before and after the sweep. AS RUN: the first chain %s (wall %s) with everything in full, the second %s (wall %s) with nothing moved — ALL GREEN
both, every verdict the old chain gave (the tape %s; the sweep %s/%s, %s cells; the positions %s over %s pauses; the journal %s kinds, %s rows,
UNMOVED; the register DECLARED %s / DEBT %s / FAILS %s). THE LESSONS: measure before cutting — the obvious cost (the replay) was not the cost; a
cache keyed on a date lies, one keyed on the sources' digests does not; a miss falls back to the full work; an incremental cut is only as good
as the independence it assumes — test it against a moved piece before trusting it.
""" % (TODAY, N['mins_after2'].upper(), N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], tape_score, N['sw'][0], N['sw'][1], N['sw'][2], N['pos'][0], N['pos'][1], N['jour'][0], N['jour'][1], N['reg'][0], N['reg'][1], N['reg'][2])
W(p, s)

# ---- 4. THE_STEPS.md ----
p = rp('THE_STEPS.md'); s = R(p)
anchor = "then the docket as its own run, then the build. Next: the commit on your word; then chapter 9's reading.\n"
assert s.count(anchor) == 1 and 'THE GATES CUT' not in s
s = s.replace(anchor, anchor + """

THE GATES CUT (%s, on Brian's "What is gate chain and why does it take so long" and "Yes make that change. It's too long as it is"; World/step9/
GATES_CHAIN.md). The gates chain is the machine's whole test bench run in order after a compile — the tape, the probes, the daemon and dependency
gates, the fold, the journal gate, the register gate, the positions table, the sweep of every runner. It took ninety minutes, and the measuring
showed where: replaying the three books costs two seconds, but loading the sixty-three runners' code costs two minutes, and every step paid that
loading, some twice. So the tape's run now saves the running world to a file and the readers load it in a second; the probes run side by side;
the sweep runs eight runners at a time and grades only the runners that changed since the last green sweep (a shared piece changed means all of
them); the table of where every checkpoint falls is measured by eight workers at once instead of one. Every guard is a digest of the source,
never a date: if anything moved, the full work runs. One cut was built and thrown out the same day — asking only the changed checkpoints — because
a test showed the checkpoints lean on each other across the whole block, so a partial run was nearly the whole run; the table is always measured
whole. The first chain after the cut took %s with everything in full; the second, with nothing changed, %s; both gave every verdict the old one
gave. Next: the commit on your word; then chapter 9.
""".rstrip('\n') % (TODAY, N['mins_after'], N['mins_after2']) + '\n')
W(p, s)

# ---- 5. THE_BRIEFING.md ----
p = rp('THE_BRIEFING.md'); s = R(p)
sb = '## SCOREBOARD (as of 2026-09-19, latest)\n'; assert s.count(sb) == 1 and 'THE GATES CHAIN CUT' not in s
bullet = '- **THE GATES CHAIN CUT FROM NINETY MINUTES TO %s — THE COST WAS LOADING THE RUNNERS\' CODE, NOT RUNNING THE WORLD; THE RUNNING WORLD SAVED ONCE AND READ BY EVERY GATE, THE PROBES SIDE BY SIDE, THE SWEEP EIGHT AT A TIME AND ONLY WHAT MOVED, THE CHECKPOINT TABLE BY EIGHT WORKERS, EVERY SHORT CUT GUARDED BY A DIGEST OF THE SOURCE AND ONE STRUCK BY ITS OWN TEST** (%s, on your "Yes make that change. It\'s too long as it is"; World/step9/GATES_CHAIN.md).\n' % (N['mins_after2'].upper(), TODAY)
s = s.replace(sb, sb + bullet)
first = s.index('\n### '); 
entry = """
### %s — The test bench got fast without getting looser

You asked what the gates chain is and why it takes so long. It is every test the machine has, run in order after a compile: the tape, eleven
probe suites, the law and dependency censuses, the fold, the journal's replay check, the register gate, the table of where every checkpoint
falls, and a sweep of all sixty-three runners against their answer sheets. Ninety minutes. The measuring said the world itself replays in two
seconds; what costs two minutes is loading the runners' code, and every step was paying that, some of them twice, one after another on a
machine with sixteen idle cores. The cut: the tape saves the running world once and the other gates read it; the probes run side by side; the
sweep runs eight at a time and grades only the runners that changed since the last green sweep; the checkpoint table is measured by eight
workers at once. What keeps it honest: every short cut is guarded by a digest of the source files it depends on, never a date, and a miss falls
back to the full work — change a shared piece and the whole sweep runs. One cut was struck by its own test the same day (asking only the changed
checkpoints — they lean on each other across the whole block), which is the other half of honest: a short cut is tested against a moved piece
before it is trusted. The first chain after the cut took %s with everything in full; the second, with nothing changed, %s; every verdict the same.
""" % (TODAY, N['mins_after'], N['mins_after2'])
s = s[:first] + entry.rstrip('\n') + '\n' + s[first:]
W(p, s)

# ---- 6. RECORD_FORMS.md ----
p = rp('World', 'step9', 'RECORD_FORMS.md'); s = R(p)
a = "and its `n/59 runners green, n graded cells`."; assert s.count(a) == 1
s = s.replace(a, "and its `run_cold_all: n/m runners green, n graded cells in all (FULL|CHANGED of m; wall n s, n jobs)`. THE GATES CUT (2026-09-19, World/step9/GATES_CHAIN.md): the probe prints are `probe_<suite>.out`, the second journal gate is the `unmoved` step (`THE JOURNAL UNMOVED … GATE GREEN`), the positions print `THE POSITIONS BY n WORKERS` and `THE FALLS: n checkpoints over n pauses in n s (n workers)`, the sweep a mode line `THE SWEEP FULL|CHANGED (why); jobs n; skipped …`; the stamp World/step9/sweep_stamp.json is TRACKED (written by a green sweep only); `--full` for the whole work.")
a = "ONE chain (gates_chain.sh) in the background and read its SUMMARY once when the harness says it ended;"; assert s.count(a) == 1
s = s.replace(a, "ONE chain (gates_chain.sh) in the background and read its SUMMARY once when the harness says it ended — the chain CUT 2026-09-19 from ninety minutes to %s (the snapshot, the parallel probes, the stamped sweep, the positions by eight workers; every short cut keyed on the sources' digests; GATES_CHAIN.md);" % N['mins_after2'])
W(p, s)

# ---- 7. World/RESUME.md ----
p = rp('World', 'RESUME.md'); s = R(p); assert 'THE GATES CUT' not in s
s = "# ⚠ THE GATES CUT (2026-09-19; step9/GATES_CHAIN.md, THE_LOOP D34-D37): the gates chain %s against ninety minutes — the tape saves the running world\n# (World/journal/data/running_world.pickle, keyed on the sources' digests) and the register gate and the readers load it; the probes in parallel; the sweep\n# `--changed --jobs 8` against step9/sweep_stamp.json (a shared piece moved = full); the positions `--jobs 8` (eight workers, the whole measure); the second\n# journal gate the UNMOVED digest; `gates_chain.sh <out> --full` for the full sweep. NEVER a reader's replay under the live source name — the readers take the snapshot.\n" % N['mins_after2'] + s
W(p, s)

# ---- 8. the recovery page (rewritten under its cap) ----
p = rp('logic', 'pre_logic_methods_2026-07-28', 'RECOVERY_new_thread_2026-09-12.md'); s = R(p)
reps = [
 ("## 2. WHERE IT STANDS (2026-09-19, after 6b; the state doc #196 addendum 4 the newest)", "## 2. WHERE IT STANDS (2026-09-19, after 6b and THE GATES CUT; the state doc #197 the newest)"),
 ("- Uncommitted since 29c189b: sitting 6, the two-run rule, 6b; the message at <scratch>/commit_msg_ch8.txt.", "- Uncommitted since 29c189b: sitting 6, the two-run rule, 6b, THE GATES CUT; the message at <scratch>/commit_msg_ch8.txt."),
 ("The gates ONE chain\n  (`sh World/step9/gates_chain.sh <out_dir>`, the SUMMARY read once);", "The gates ONE chain\n  (`sh World/step9/gates_chain.sh <out_dir>`, the SUMMARY read once; CUT 2026-09-19 to %s — the snapshot, the parallel probes, the\n  stamped sweep, the positions by eight workers; GATES_CHAIN.md);" % N['mins_after2']),
 ("- zsh globs `====` (use `----`); importing cold_run_sequence costs 40-90 s. The peer thread is never a ruling.", "- zsh globs `====` (use `----`); the sequence import costs ~140 s — a reader takes the SNAPSHOT (register_census.running_world). The peer\n  thread is never a ruling."),
 ("the gates (daemon_census, dependency_census, register_census --strict, world_journal --gate, run_cold_all — gates_chain.sh runs them all), the", "the gates (gates_chain.sh runs them all; GATES_CHAIN.md the design; sweep_stamp.json the sweep's stamp), the"),
 ("- THE OTHER THREAD (Torah Grok Main — relay and illustration only): its state in the memory folder's main-thread-checkpoint-2026-09-18.md; a relayed finding is never a ruling.", "- THE OTHER THREAD (Torah Grok Main): its state in <memory>/main-thread-checkpoint-2026-09-18.md; a relayed finding is never a ruling."),
 ("the stepper, the port, the board, D1-D33): THE_LOOP.md.", "the stepper, the port, the board, the gates cut, D1-D37): THE_LOOP.md."),
 ("The cost cuts: §35.", "The cost cuts: §35, §45."),
 ("a retrograde stretch runs to the NEXT marker (a forward\n  marker closes it; a chapter after a stretch opens with one); a disagreement an OPEN row;", "a retrograde stretch runs to the NEXT marker; a disagreement an OPEN row;"),
 ("edges the runner never imports (CALL / VIA / FALSE / OWED / PARAMETER / REVERSE / RUN_CITATION, a why and a link); a retype covers every\n  line of a literal.", "edges the runner never imports (seven kinds, each a why and a link); a retype covers every line of a literal."),
 ("The state doc's newest COMPACTION POINT names the step in flight; the scratchpad holds the sitting's scripts. Reread this page, the map's\nnewest section, the memory index — then continue the step named.", "The state doc's newest COMPACTION POINT names the step in flight. Reread this page, the map's newest section, the memory index — then\ncontinue the step named."),
]
for a, b in reps:
    assert s.count(a) == 1, 'recovery page anchor missing: ' + a[:60]; s = s.replace(a, b)
size = len(s.encode('utf-8')); print('  the recovery page %d bytes (cap 10,240)' % size); assert size <= 10240, 'the recovery page over its cap'
W(p, s)

# ---- 9. the addenda §45 ----
p = rp('logic', 'pre_logic_methods_2026-07-28', 'RECOVERY_addenda_2026-09-12.md'); s = R(p); assert '## 45.' not in s and s.endswith('\n')
s += """
## 45. ADDENDUM (%s, THE GATES CUT — the gates chain from ninety minutes to %s; the owner: "What is gate chain and why does it take so long", "Yes make that change. It's too long as it is"; the state doc's #197)
THE MEASUREMENT: the chain's steps 5,380 s (tape 156, probes 609, journal 316, register 141, positions 1,562, checkpoint 205, sweep 2,011, journal2 315);
the import of the sixty-three runners 135.9 s against a replay of 1.7 s; the running world 1.5 MB pickled, 1.09 s to reload. THE SIX CUTS (World/step9/
GATES_CHAIN.md; THE_LOOP D34-D37): the SNAPSHOT saved by the tape's run and loaded by the readers under a sources key; the eleven probe suites in
parallel; the journal gate's two replays concurrent; the positions table measured WHOLE by eight workers (an incremental form by regions built,
tested against a moved region and STRUCK the same day — seven of CU's nine rows NOT YET; the closure 429 of 630 statements); the sweep parallel and
incremental against its stamp (a shared piece moved = full; the stamp by a green sweep only, tracked); the second journal gate the UNMOVED digest.
AS RUN: the first chain %s (wall %s) with everything in full, the second %s (wall %s) with nothing moved — ALL GREEN both, every verdict the old
chain gave. THE FILES: run_cold_all.py, world_journal.py (sources_key, save/load_snapshot, live_digest, --stamp/--unmoved, the concurrent gate),
register_census.py (Ink by the INK block; running_world from the snapshot), cold_run_sequence.py (save_snapshot in run(); _cp_block the parse-once
cache; checkpoint_names cached), checkpoint_positions.py (--jobs, the workers), gates_chain.sh (the twelve steps; --full). THE RECORDS on the sheet;
the forms in World/step9/forms_gates_cut_%s/. NOT COMMITTED — in the chapter-8 commit on the owner's word.
""" % (TODAY, N['mins_after2'], N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], TODAY)
W(p, s)

# ---- 10. the state doc — #197 ----
p = rp('logic', 'pre_logic_methods_2026-07-28', 'PROMPT_continue_solo_era_2026-08-06.md'); s = R(p); assert 'COMPACTION POINT #197' not in s and s.endswith('\n')
s += """
═══ COMPACTION POINT #197 (%s — after THE GATES CUT, built and run on the owner's "Yes make that change. It's too long as it is" following his "What is gate chain and why does it take so long"; the compaction before it fell at #196 addendum 4) ═══
THE STATE: chapter 8 compiled and on the tape as #196 addendum 4 says (nothing of the tape, the runners, the registries or the records of 6b touched by this work); THE GATES CHAIN CUT from ninety minutes to %s (the wall clock %s; the second chain, nothing moved — the first, everything in full, %s / wall %s) — World/step9/GATES_CHAIN.md the design with the measurements and the AS RUN table, THE_LOOP's D34-D37. THE MEASUREMENT that decided it: the import of the sixty-three runners 135.9 s, the replay 1.7 s — every step paid the import. THE SIX CUTS: (1) the SNAPSHOT — cold_run_sequence.run() saves the running world (World/journal/data/running_world.pickle + .json, daemons stripped, keyed on world_journal.sources_key(), atomic) and register_census.running_world() loads it (the register gate, readback_probes, register_probes); Ink execs the INK block; (2) the eleven probe suites in parallel in gates_chain.sh (probe_<suite>.out); (3) world_journal.gate()'s two replays concurrent; (4) checkpoint_positions.py --jobs 8 — eight workers, each the WHOLE tape in its own journal folder with the live base copied in (the replay still the audit), asking the block at pause i where i mod 8 is its number; the parent merges the pauses and takes the falls; the table always whole (AN INCREMENTAL FORM BY REGIONS WAS BUILT, TESTED AGAINST A MOVED REGION AND STRUCK the same day: seven of CU's nine rows came out NOT YET — a region's checkpoints read helpers bound across most of the block, the closure 429 of 630 statements; the record in GATES_CHAIN.md); cold_run_sequence._cp_block the parse-once cache; (5) run_cold_all.py --changed --jobs 8 --skip cold_run_sequence.py against World/step9/sweep_stamp.json (TRACKED; written by a green sweep only; a shared piece moved or no stamp = FULL; a runner moved = it and its transitive importers); (6) world_journal.py --stamp before the sweep and --unmoved after (the digest of the live L3 rows) in place of the second full gate. THE CHAIN AS RUN TWICE, ALL GREEN BOTH — the first (everything in full, %s, wall %s): tape %s s (%s), probes %s s (%s), daemon %s s, dependency %s s, build %s s, journal %s s (%s kinds, %s rows), register %s s (DECLARED %s / DEBT %s / FAILS %s, from the snapshot), positions %s s (the old sequential measure: %s checkpoints over %s pauses), checkpoint %s s (%s/%s), stamp %s s, sweep %s s (%s: %s/%s runners, %s cells, %s jobs), unmoved %s s (%s sources); the second (nothing moved — THE STEADY STATE, %s, wall %s): tape %s, probes %s, journal %s, register %s, positions %s (%s workers: %s over %s pauses in %s s), checkpoint %s, sweep %s (%s — nothing to grade), unmoved %s; every verdict the chain before the cut gave. THE RECORDS (write_gates_cut_records.py from the sheet, one call): GATES_CHAIN.md's AS RUN, THE_LOOP's section, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the bullet and the entry), RECORD_FORMS (the chain lines), RESUME, the recovery page (the cost rules; under its cap), the addenda §45, this point, the memory (cost-rules-no-polling.md; the index line under 17,000). THE FORMS in World/step9/forms_gates_cut_%s/ (the snapshot test, the writer, the chain's folder). THE TREE: run_cold_all.py, world_journal.py, register_census.py, cold_run_sequence.py (the snapshot line and the block cache — the TAPE section untouched), checkpoint_positions.py, checkpoint_positions.yaml (the new form), gates_chain.sh, GATES_CHAIN.md (new), sweep_stamp.json (new). NOT COMMITTED (since 29c189b): sitting 6, the two-run rule, 6b, and this — the message at <scratch>/commit_msg_ch8.txt extended with the gates-cut paragraph. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word ("commit" = no push; "commit push" = both); then CHAPTER 9's reading (9:1-29) — one run; the next compile (7b) OPENS A NEW CHECKPOINT SERIES (CU the last two-letter prefix); THE INSTALL HYPOTHESIS and THE SUPPLIED GRADE on the table. IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 6b — AS BUILT", MEMORY.md; GATES_CHAIN.md when the chain is next run.
""" % (TODAY, N['mins_after2'], N['mins_wall2'], N['mins_after'], N['mins_wall'], N['mins_after'], N['mins_wall'], after['tape'], tape_score, after['probes'], ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), after['daemon'], after['dependency'], after['build'], after['journal'], N['jour'][0], N['jour'][1], after['register'], N['reg'][0], N['reg'][1], N['reg'][2], after['positions'], N['pos'][0], N['pos'][1], after['checkpoint'], cp[0], cp[1], after['stamp'], after['sweep'], N['sw_mode'][0], N['sw'][0], N['sw'][1], N['sw'][2], N['sw'][6], after['unmoved'], N['unm'],
       N['mins_after2'], N['mins_wall2'], after2['tape'], after2['probes'], after2['journal'], after2['register'], after2['positions'], N['pos2'][3], N['pos2'][0], N['pos2'][1], N['pos2'][2], after2['checkpoint'], after2['sweep'], N['sw2'][0], after2['unmoved'], TODAY)
W(p, s)

# ---- 11. the memory ----
p = os.path.join(MEM, 'cost-rules-no-polling.md'); s = R(p); assert 'THE GATES CUT' not in s
s = s.replace('the gates as ONE chain (World/step9/gates_chain.sh);', 'the gates as ONE chain (World/step9/gates_chain.sh — CUT 2026-09-19 from ninety minutes to %s, GATES_CHAIN.md);' % N['mins_after'], 1)
s += """
THE GATES CUT (owner-ruled 2026-09-19 after sitting 6b: "What is gate chain and why does it take so long" → "Yes make that change. It's too long as it is"): the chain measured at ninety minutes; the import of the sixty-three runners 136 s against a replay of 1.7 s — every step paid the import. BUILT (World/step9/GATES_CHAIN.md; THE_LOOP D34-D37): the tape's run SAVES the running world (World/journal/data/running_world.pickle, keyed on the sources' digests) and the register gate, readback_probes and register_probes LOAD it (`register_census.running_world()`); the eleven probe suites in parallel; the journal gate's two replays concurrent; `checkpoint_positions.py --jobs 8` (the whole measure by eight workers — an incremental form by regions was struck by its own test); `run_cold_all.py --changed --jobs 8 --skip cold_run_sequence.py` against World/step9/sweep_stamp.json (tracked; a shared piece moved = full); `world_journal.py --stamp/--unmoved` around the sweep in place of the second full gate. The first chain after the cut (everything in full): %s; the second (nothing moved): %s — ALL GREEN both, every verdict the old chain gave. **Why:** the wall clock was the owner's complaint, and the wait turns ride on it. **How to apply:** the chain as before (`sh World/step9/gates_chain.sh <out_dir>` in the background, the SUMMARY once); `--full` when a guard is in doubt; NEVER a reader's replay under the live source name — the readers take the snapshot; the stamp is written by a green sweep only, never by hand; a short cut is TESTED AGAINST A MOVED PIECE before it is trusted.
""" % (N['mins_after'], N['mins_after2'])
W(p, s)
p = os.path.join(MEM, 'MEMORY.md'); s = R(p)
a = "a clean point each; the chain, the sheet"; assert s.count(a) == 1
s = s.replace(a, "a clean point each; the chain CUT to ~%s min (GATES_CHAIN.md), the sheet" % about)
a = "ch 1-8 COMPILED (1-7 at 29c189b PUSHED; 8 UNCOMMITTED, sittings 6/6b); NEXT: commit on his word, then ch 9 (7b a new series)"; assert s.count(a) == 1
s = s.replace(a, "ch 1-8 COMPILED (1-7 PUSHED 29c189b; 8 + the gates cut UNCOMMITTED); NEXT: commit, then ch 9 (7b a new series)")
for a, b in [('message "Torah Grok Main" (= "Claude old") via SendMessage;', 'message "Torah Grok Main" via SendMessage;'),
             ('(ch6 70/747; 2b 6/114 + one cell retyped; 1b 1/215; 3b, sitting 4 clean); LESSON', '(ch6 70/747; 2b 6/114 + one cell retyped; 1b 1/215); LESSON'),
             (' — moved Macs mid-run; recovered', ' — moved Macs mid-run')]:
    assert s.count(a) == 1, a[:40]; s = s.replace(a, b)   # the index trimmed to stay under its cap (the words dropped are in the files they point to)
size = len(s.encode('utf-8')); print('  MEMORY.md %d bytes (cap 17,000)' % size); assert size < 17000
W(p, s)
p = os.path.join(MEM, 'deuteronomy-walk.md'); s = R(p)
a = "the docket 451 rows whole; UNCOMMITTED)"; assert s.count(a) == 1
s = s.replace(a, "the docket 451 rows whole; UNCOMMITTED, with THE GATES CUT of 2026-09-19 — see cost-rules-no-polling)")
W(p, s)

# ---- 12. the commit message ----
p = os.path.join(SP, 'commit_msg_ch8.txt'); s = R(p); assert 'THE GATES CUT' not in s
head, rest = s.split('\n', 1)
head = head.rstrip('.') + '. AND, THE SAME DAY, THE GATES CHAIN CUT FROM NINETY MINUTES TO %s — THE IMPORT WAS THE COST, NOT THE REPLAY: THE RUNNING WORLD SAVED ONCE AND READ BY THE GATES, THE PROBES IN PARALLEL, THE SWEEP EIGHT AT A TIME AND ONLY WHAT MOVED, THE CHECKPOINT TABLE BY EIGHT WORKERS, EVERY SHORT CUT KEYED ON THE SOURCES\' DIGESTS AND ONE STRUCK BY ITS OWN TEST.' % N['mins_after2'].upper()
i = rest.index('\nCo-Authored-By:')
para = """
ALSO IN THIS COMMIT: THE GATES CUT (%s; on the owner's "What is gate chain and why does it take so long" and "Yes make that change. It's too long as it is"; World/step9/GATES_CHAIN.md the design with the measurements and the AS RUN table; THE_LOOP's D34-D37; the state doc's #197). MEASURED FIRST: the chain's steps 5,380 s (ninety minutes); the import of the sixty-three runners 135.9 s against a replay of 1.7 s — every step paid the import, the readback and register suites replayed the world besides, the positions table re-parsed the 750 KB sequence file at every one of 169 pauses, the sweep ran sixty-three runners one after another on sixteen idle CPUs. THE SIX CUTS: the SNAPSHOT — the tape's run saves the running world (daemons stripped; atomic; keyed on a digest of every source the replay depends on) and the register gate, the readback probes and the register probes load it in a second, replaying only on a stale key (the register gate no longer rewrites the live source rows; register_census.Ink execs the INK block instead of importing the runners); the eleven probe suites in parallel, each its own process and print; the journal gate's two replays concurrent; the positions table measured WHOLE by eight workers (each the tape in its own folder with the live base copied in, asking the block at its own pauses; the checkpoints block parsed and compiled once — AN INCREMENTAL FORM BY REGIONS WAS BUILT, TESTED AGAINST A MOVED REGION AND STRUCK THE SAME DAY: seven of CU's nine rows came out NOT YET, the region's checkpoints reading helpers bound across most of the block, the closure 429 of 630 statements); the sweep PARALLEL (--jobs 8) and INCREMENTAL (--changed against World/step9/sweep_stamp.json, tracked, written by a green sweep only: a runner moved = it and its transitive importers, a shared piece moved or no stamp = FULL; --skip cold_run_sequence.py, the chain's first step); the second journal gate replaced by a digest of the live rows taken before the sweep and compared after (D21's gate still runs once, upstream). THE CHAIN AS RUN TWICE, ALL GREEN BOTH — the first with everything in full in %s (wall %s), the second with nothing moved in %s (wall %s), the steady state — the tape %s, the probes %s, the daemon gate %s daemons / %s functions, the dependency gate %s edges / %s pointers, the journal gate %s kinds / %s rows and UNMOVED across the sweep, the register gate DECLARED %s / DEBT %s / FAILS %s from the snapshot, the positions %s checkpoints over %s pauses (the second chain by %s workers in %s s), the sweep %s/%s at %s graded cells (%s; the second chain NOTHING TO GRADE) — every verdict the chain before the cut gave. THE FILES: run_cold_all.py, world_journal.py, register_census.py, cold_run_sequence.py (the snapshot line and the block cache; the TAPE untouched), checkpoint_positions.py and its table's new form, gates_chain.sh (twelve steps; --full), GATES_CHAIN.md (new), sweep_stamp.json (new). THE RECORDS on the sheet; the forms in World/step9/forms_gates_cut_%s/.
""" % (TODAY, N['mins_after'], N['mins_wall'], N['mins_after2'], N['mins_wall2'], tape_score, ', '.join('%s %s/%s' % (k, v[0], v[1]) for k, v in probes.items()), N['dae'][0], N['dae'][1], N['dep'][0], N['dep'][1], N['jour'][0], N['jour'][1], N['reg'][0], N['reg'][1], N['reg'][2], N['pos'][0], N['pos'][1], N['pos2'][3], N['pos2'][2], N['sw'][0], N['sw'][1], N['sw'][2], N['sw_mode'][0], TODAY)
s = head + '\n' + rest[:i].rstrip('\n') + '\n' + para + rest[i:]
W(p, s)
print('RECORDS %s' % ('CHECKED (nothing written)' if CHECK else 'WRITTEN'))
