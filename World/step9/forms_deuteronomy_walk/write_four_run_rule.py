import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE FOUR-RUN RULE (owner-ruled 2026-09-16 — "Yes write it", on the proposal after sitting 3b's one run of ~600k tokens): a sitting is FOUR RUNS
# with a clean compaction point after each. Written into the cost rules everywhere they live: the memory (cost-rules-no-polling.md + the index line),
# the recovery page's standing laws (under its 10,240-byte cap), the sheet RECORD_FORMS.md, THE_STEPS, the map's tail, the state doc. Every text
# built here; the caps asserted before any file is opened for writing.
import os, subprocess, sys
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
RULE = ("THE FOUR-RUN RULE (owner-ruled 2026-09-16, \"Yes write it\"): a sitting is FOUR RUNS, a clean compaction point after each — (1) the rereads, the "
        "measurements, the design in the map; (2) the docket (the scan, the verdicts in parts, the writer); (3) the types, the runner, the stitch, the tape "
        "to 10/10; (4) the gates chain, the records, the forms — each near 150-200k tokens, never one run of 600k; a reading sitting split the same way "
        "(the measurements and the ink; the rows and the ledger; the seat, the chain and the fold; the records). Inside a run: the docket's rows read at a "
        "short cut; a prior sitting's form derived by sed and read only where it differs, never whole; the state doc's checkpoint at each run's end names "
        "the next run's first step.")
plans = []
def read(p): return open(p, encoding='utf-8').read()
# 1. the memory file
P = f'{MEM}/cost-rules-no-polling.md'
s = read(P); assert 'THE FOUR-RUN RULE' not in s
plans.append((P, s.rstrip('\n') + '\n\n' + RULE + " **Why:** the owner after 3b's single run of ~600k tokens: \"I don't trust your accuracy when we use a million in one run\" — the context is a second bill beside the turns, and a long one erodes care (today's misses were caught by the instruments, not by memory). **How to apply:** open every sitting by naming its four runs; end each run with the state doc's checkpoint and the words \"a clean compaction point\"; never carry a docket or a runner across a run's edge unwritten. Linked: [[deuteronomy-walk]], [[compaction-protocol]].\n"))
# 2. the memory index — the cost line edited, the walk line shaved to keep the file under 17,000 bytes
P = f'{MEM}/MEMORY.md'
s = read(P)
old = "- [⚠⚠ COST RULES](cost-rules-no-polling.md) — 2026-09-16: turns are the bill — never poll; gates_chain.sh; checkpoint_check.py; RECORD_FORMS.md"
new = "- [⚠⚠ COST RULES](cost-rules-no-polling.md) — turns AND context the bill; never poll; ⚠ FOUR RUNS a sitting, a clean point each, ≤200k; the chain, the fast check, the sheet"
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new)
old2 = "(chapters 1-5 COMPILED; COMMITTED 834602b through 2b, not pushed); NEXT: chapter 6 or the schema sitting, on his word"
new2 = "(chapters 1-5 COMPILED; 834602b not pushed); NEXT: chapter 6 or the schema, on his word"
assert s2.count(old2) == 1; s2 = s2.replace(old2, new2)
assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8'))
plans.append((P, s2))
# 3. the recovery page — the cost bullet rewritten with the rule; the file map shortened to hold the cap
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
s = read(P)
old = ("- THE COST RULES (2026-09-16): every tool call re-sends the whole conversation — the bill is the NUMBER OF TURNS. NEVER POLL a background job\n"
       "  (run_in_background; the harness notifies). The gates step is ONE chain: `sh World/step9/gates_chain.sh <out_dir>`, its SUMMARY read once.\n"
       "  ONE fast check before the tape: `python3 World/step9/checkpoint_check.py <PREFIX>`. The records from the sheet in ONE call. Batch\n"
       "  independent reads into one call.\n")
new = ("- THE COST RULES (2026-09-16): the bill is TURNS and CONTEXT. NEVER POLL a background job (the harness notifies). The gates ONE chain\n"
       "  (`sh World/step9/gates_chain.sh <out_dir>`, the SUMMARY read once); ONE fast check before the tape (`checkpoint_check.py --all`); the\n"
       "  records from the sheet in ONE call; independent reads batched. ⚠ A SITTING IS FOUR RUNS, a clean compaction point after each (owner-ruled\n"
       "  2026-09-16): (1) the rereads, the measurements, the design; (2) the docket; (3) the types, the runner, the stitch, the tape to 10/10; (4) the\n"
       "  gates chain, the records, the forms — each near 150-200k, never 600k; a reading sitting the same; the docket's rows at a short cut; a prior\n"
       "  form by sed, read where it differs.\n")
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new)
cuts = [("COMPILE_DEBT.md, RECORD_FORMS.md (the records sheet), SEQUENTIAL_RUN.md, world_engine.py, cold_run_sequence.py (THE TAPE), cold_run_<span>.py\n(59 runners; cold_run_obey_horeb.py the newest form), the registries (event_vocabulary, effect_vocabulary, daemon_dispositions,\ndependency_dispositions, register_dispositions, calendar_parameters, population_schema), the gates (daemon_census, dependency_census,\nregister_census --strict, world_journal --gate, run_cold_all; gates_chain.sh runs them all), the probes (*_probes.py), checkpoint_check.py,\ncheckpoint_positions.py, world_stepper.py, world_board.py, forms_deuteronomy_walk/ (the walk's scripts and prints — copy the newest sitting's\nform to the scratchpad).",
         "COMPILE_DEBT.md, RECORD_FORMS.md (the records sheet), cold_run_sequence.py (THE TAPE), cold_run_<span>.py (60 runners;\ncold_run_covenant_at_horeb.py the newest form), the registries (*_vocabulary.yaml, *_dispositions.yaml, calendar_parameters, population_schema),\nthe gates (daemon_census, dependency_census, register_census --strict, world_journal --gate, run_cold_all — gates_chain.sh runs them all), the\nprobes (*_probes.py), checkpoint_check.py, world_stepper.py, world_board.py, forms_deuteronomy_walk/ (the walk's scripts and prints — derive the\nnewest sitting's form by sed)."),
        ("He compacts at ~700k-900k tokens; a clean compaction point is announced at every milestone.", "He compacts after each RUN; a clean point is announced at every run's end."),
        ("the gates to FAIL → the runner (parts; the fast checker; the guard; CASES generated; scene and narrative predicted) → the recorder →\nthe stitcher → the literals and checkpoints → `checkpoint_check.py <PREFIX>` (every fault in one print) → the\ntape 10/10 with THE REST → `gates_chain.sh` in the background (one summary) → the records from the sheet in one call.",
         "the gates to FAIL → the runner (parts; the fast checker; CASES generated) → the recorder → the stitcher → the literals → the tape 10/10\nwith THE REST → `gates_chain.sh` (one summary) → the records from the sheet in one call — the four runs' edges after the design, the docket, the tape."),
        ("- THE GATES' READING RULES: the daemon gate reads LITERAL submits only; `import cold_run_X` in the sequence file is the live edge; the token\n  census can demand an edge the runner never imports (CALL / VIA / FALSE / OWED / PARAMETER / REVERSE / RUN_CITATION, a why and a link);\n  the honest-pairing guard reads literals only; a retype covers every line of a literal.\n",
         "- THE GATES READ LITERALS: the daemon gate literal submits; `import cold_run_X` in the sequence file the live edge; the token census demands\n  edges the runner never imports (CALL / VIA / FALSE / OWED / PARAMETER / REVERSE / RUN_CITATION, a why and a link); a retype covers every\n  line of a literal.\n")]
for a, b in cuts:
    assert s2.count(a) == 1, a[:60]
    s2 = s2.replace(a, b)
n = len(s2.encode('utf-8')); assert n <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', n)
plans.append((P, s2))
# 4. the sheet
P = f'{ROOT}/World/step9/RECORD_FORMS.md'
s = read(P); assert 'THE FOUR-RUN RULE' not in s
plans.append((P, s.rstrip('\n') + '\n\n' + RULE + '\n'))
# 5. THE_STEPS — a paragraph after the 3b entry (before Step 6)
P = f'{ROOT}/THE_STEPS.md'
s = read(P); anchor = "\n## Step 6 — Publish\n"; assert s.count(anchor) == 1 and 'THE FOUR-RUN RULE' not in s
para = ("\nTHE FOUR-RUN RULE (2026-09-16, on Brian's \"Yes write it\", after chapter 5's compile ran as one sitting of six hundred thousand tokens). A sitting is\n"
        "no longer one run. It is four, with a clean stopping point after each: first the rereads, the measurements and the design; second the docket;\n"
        "third the runner and the tape to ten of ten; fourth the gates and the records. Each run stays near a fifth of a context, and the state doc's\n"
        "checkpoint at each edge names the next run's first step, so the reread after a compaction is the same three files. Two economies inside a run:\n"
        "the docket's rows are read at a short cut, and a prior sitting's script is derived by substitution and read only where it differs. The reason is\n"
        "his: a million tokens in one run is not to be trusted, and the instruments that caught this sitting's misses are no excuse for a long context.\n")
plans.append((P, s.replace(anchor, para + anchor)))
# 6. the map's tail
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
s = read(P); assert 'THE FOUR-RUN RULE' not in s
plans.append((P, s.rstrip('\n') + "\n\n## THE FOUR-RUN RULE (owner-ruled 2026-09-16 at 3b's close — \"Yes write it\")\n\n" + RULE + " The next sitting (chapter 6's reading, or the schema sitting) opens by naming its four runs; sitting 3b (one run, ~600k) is the case that ruled it.\n"))
# 7. the state doc
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = read(P); assert 'THE FOUR-RUN RULE' not in s
plans.append((P, s.rstrip('\n') + "\n\n#188 ADDENDUM 3 (2026-09-16, after 3b's close — A RULING): " + RULE + " Recorded in the memory (cost-rules-no-polling.md; the index line), the recovery page's cost rules, RECORD_FORMS.md, THE_STEPS, the map's tail. Still a clean compaction point; nothing mid-flight; the tree uncommitted since 834602b.\n"))
for p, s2 in plans:
    assert s2 != read(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p, len(read(p)), '->', len(s2))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2))
print('the four-run rule written')
