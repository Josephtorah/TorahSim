#!/usr/bin/env python3
# THE COST RULES A-B-C (owner-ruled 2026-09-20: "Yes I like a b and c" … "Let's go to 400 a b and c") written into the records from the sheet in ONE call:
# the recovery page's cost bullet rewritten under its cap, RECORD_FORMS, THE_STEPS, GATES_CHAIN.md, the map's newest section, THE_BRIEFING (bullet + entry),
# the state doc's #199 addendum 4, the addenda's section, COST_AUDIT's ruling line, the memory (the cost-rules note; the index line under 17,000).
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip(); os.chdir(ROOT)
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
def R(p): return open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
def sub(p, a, b, s=None):
    s = R(p) if s is None else s; assert s.count(a) == 1, (p, a[:70]); return s.replace(a, b)
RULE = ('THE COST RULES A-B-C (owner-ruled 2026-09-20 after THE COST AUDIT — World/step9/COST_AUDIT_2026-09-20.md, measured from the transcripts: the bill is '
        'CACHE WRITES 45% / CACHE READS 37% / OUTPUT 17%; 169 full re-writes of the context after waits past five minutes were a third of the bill; a third of the '
        'calls ran past 600k context and carried 57% of the reads; the typed prose under 5%): '
        'A. THE CACHE LAW — the cache dies at FIVE MINUTES: no wait past five minutes on a big context. Every long job (the gates chain, the sweep, the positions '
        'table, a reading\'s chain) is LAUNCHED IN THE BACKGROUND AT THE END OF ITS RUN with its readers already written (the records writer, the copier, the message '
        'extender parse the chain\'s prints); the clean point is written and announced; the owner compacts; THE TAIL — a short run on a small context — reads the '
        'SUMMARY once, files the demands (a rerun --from the step, waited on the small context), runs the writers, announces. Before any break: the clean point and '
        'the compaction first. '
        'B. THE 400k CAP — a run ends at the clean point nearest 400k, never past 450k (the two-run rule\'s "near 300k, never 600k" superseded by his word "Let\'s go to 400"). '
        'C. FEWER CALLS — one call per pipeline step; independent reads batched; nothing re-verified that the chain verifies; BATCHING, NEVER SKIPPING (the print-first '
        'law stands). THE SITTING SHAPES AMENDED: a COMPILE sitting is TWO RUNS + THE TAIL (RUN A the rereads, the design, the docket — its own run past ~700 rows; '
        'RUN B the probes to FAIL, the types, the runner, the tape to 10/10, the writers prepared, the chain LAUNCHED; THE TAIL the summary, the demands, the records, '
        'the forms, the message); a READING sitting is ONE run + its tail. Projected: the same work at about a third of the price per chapter.')
# 1. THE RECOVERY PAGE — the cost bullet rewritten, two other lines shortened; the cap asserted
REC = 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; s = R(REC)
OLD = s[s.index('- THE COST RULES (2026-09-16):'):s.index('  ⚠ EVERY SHELF ROW READ WHOLE')]
NEW = ('- THE COST RULES: the bill is CONTEXT × CALLS + RE-WRITES (COST_AUDIT_2026-09-20.md). NEVER POLL. The gates ONE chain (`sh\n'
       '  World/step9/gates_chain.sh <out_dir>`; the SUMMARY read once; GATES_CHAIN.md); the records from the sheet in ONE call. ⚠ OWNER-RULED\n'
       '  2026-09-20: A THE CACHE LAW — the cache dies at FIVE MINUTES: no wait past five minutes on a big context; every long job (the chain, the\n'
       '  sweep, the positions) LAUNCHED at a run\'s END, its readers written first; the clean point announced; the owner compacts; THE TAIL (a small\n'
       '  run) reads the SUMMARY, files demands, runs the writers; compact before a break. B THE 400k CAP — a run ends at the clean point nearest\n'
       '  400k, never past 450k. C FEWER CALLS — one call per step, reads batched, batching never skipping. ⚠ A COMPILE SITTING IS TWO RUNS + THE\n'
       '  TAIL: RUN A the rereads, the design, the docket (its own run past ~700 rows); RUN B the types, the runner, the tape to 10/10, the chain\n'
       '  LAUNCHED; THE TAIL the records, the forms, the message; a READING sitting ONE run + its tail.\n')
TRIMS = [(" (the walk's forms — derive by sed)", ''), (' (D7\'s merge)', ''), ('; the two sitting shapes in full: §5', ''), (' (the long forms: the addenda\'s section 5; the newest instances: the map\'s "Sitting 9" and "Sitting 8b")', '')]
s = s.replace(OLD, NEW)
s = sub(REC, '- SITTING 9 (chapter 11 read, one run): THE SPINE BACK ON THE CHAPTER — twenty-two Sifrei sections on 11:10-32, 210 sources whole; the\n  rain conditional (11:13-17) has NO CELL; the frontlets\' three spellings measured; 11:25\'s receipt pointed at Exodus 23:27 by the shelf.\n',
        '- SITTING 9 (chapter 11 read): the Sifrei back on the chapter, 210 sources whole; the rain conditional had NO CELL (paid at 9b).\n', s)
s = sub(REC, "- zsh globs `====` (use `----`); the engine's import ~34 s through THE IMPORT CACHE (step9/ink_cache.py; INK_CACHE=0 = the checks in full,\n  ~168 s — the sweep's and --full's way; ink_cache_probes.py 8/8 in the chain; --status|--clear; the recorder runs with it OFF) — a reader takes the\n  snapshot. The peer thread is never a ruling.\n",
        "- zsh globs `====` (use `----`); THE IMPORT CACHE (step9/ink_cache.py; INK_CACHE=0 the checks in full — the sweep's and the recorder's way; its\n  probes 8/8 in the chain; a runner keeps no raw database scan as a module value). The peer thread is never a ruling.\n", s)
s = sub(REC, '## 2. WHERE IT STANDS (2026-09-20, 9b done; the state doc #199 addendum 2 the newest)', '## 2. WHERE IT STANDS (2026-09-20, 9b done + the cost rules; the state doc #199 addendum 4 the newest)', s)
s = sub(REC, 'the two runs\' edge after the docket.', 'the chain LAUNCHED at RUN B\'s end; THE TAIL after the compaction.', s)
for a, b in TRIMS:
    if len(s.encode('utf-8')) <= 10240: break
    if s.count(a) == 1: s = s.replace(a, b); print('  trimmed:', a[:50])
n = len(s.encode('utf-8')); print('the recovery page would be %d bytes (cap 10240)' % n); assert n <= 10240; W(REC, s)
# 2. RECORD_FORMS — the rule after the two-run rule's paragraph
RF = 'World/step9/RECORD_FORMS.md'; s = R(RF); i = s.index('THE TWO-RUN RULE (owner-ruled 2026-09-18'); j = s.index('\n', i) + 1
W(RF, s[:j] + '\n' + RULE + '\n' + s[j:])
# 3. THE_STEPS — a paragraph in Brian's vocabulary after the two-run rule's paragraph
ST = 'THE_STEPS.md'; s = R(ST); i = s.index('THE TWO-RUN RULE (2026-09-18, on Brian\'s "Yes"'); j = s.index('\n\n', i) + 2
STEPS_PARA = ('THE COST RULES (2026-09-20, on Brian\'s "Yes I like a b and c" and "Let\'s go to 400 a b and c", after the cost audit). Brian asked for an audit of the\n'
              'process: the program had grown and each chapter cost more. The bill was read off the session transcripts, not guessed: nearly half of it was the\n'
              'context being re-written from scratch after a wait longer than five minutes — the gates chain, the sweep, the positions table, a pause — because the\n'
              'cache dies at five minutes; another third was every call re-reading a context that had grown past 600k; the typing was under a fifth, and the paperwork\n'
              'per sitting under a twentieth. So three rules, and none of them touches what is read, typed or gated: A. THE CACHE LAW — no wait past five minutes on a\n'
              'big context; every long job is launched at the end of its run, the clean point is written, Brian compacts, and a short run on a small context reads\n'
              'the result; compact before a break. B. THE 400k CAP — a run ends at the clean point nearest 400k. C. FEWER CALLS — one call per step, batching, never\n'
              'skipping. "One book at a time and then integrate" was weighed and set aside: it trims the paperwork, which is not the cost, and a slip found after ten\n'
              'chapters is ten chapters wide. The record: World/step9/COST_AUDIT_2026-09-20.md.\n\n')
W(ST, s[:j] + STEPS_PARA + s[j:])
# 4. GATES_CHAIN.md — the placement
GC = 'World/step9/GATES_CHAIN.md'; W(GC, R(GC).rstrip('\n') + '\n\n## THE CACHE LAW (owner-ruled 2026-09-20; COST_AUDIT_2026-09-20.md)\nThe chain\'s minutes cost nothing; the WAIT across them on a big context does — the prompt cache dies at five minutes and the next call re-writes the whole context (169 such re-writes were a third of nine days\' bill). So the chain is LAUNCHED IN THE BACKGROUND AT THE END OF ITS RUN, with its readers already written (the records writer, the forms copier, the message extender parse its prints); the clean point is written; the owner compacts; THE TAIL — a small run — reads the SUMMARY once, files any demand, reruns `--from` the step (a wait on a small context is cheap), runs the writers. The positions table by eight workers is killed by the session\'s memory watchdog on this machine (7b, 9b): measure it by four (`checkpoint_positions.py --jobs 4`) outside the chain and resume `--from checkpoint`.\n')
# 5. THE MAP — the newest section
MAP = 'World/step9/DEUTERONOMY_WALK.md'; W(MAP, R(MAP).rstrip('\n') + '\n\n## THE COST AUDIT AND THE THREE RULES (2026-09-20, after 9b\'s push; owner-ruled "Let\'s go to 400 a b and c")\n\n' + RULE + '\nTHE FIRST SITTING UNDER THE RULES: chapter 12\'s reading (12:1-32) in one run + its tail — the reading\'s chain launched at the run\'s end.\n')
# 6. THE_BRIEFING — the scoreboard bullet and the entry
BR = 'THE_BRIEFING.md'; s = R(BR)
BA = '- **CHAPTER 11 COMPILED — THE RAIN CONDITIONAL GETS ITS CELL:'; s = sub(BR, BA, '- **THE COST AUDIT AND THE THREE RULES — THE BILL READ OFF THE TRANSCRIPTS: CACHE RE-WRITES AFTER FIVE-MINUTE WAITS A THIRD OF IT, THE FAT CONTEXT ANOTHER THIRD, THE TYPING A SIXTH; RULED: THE CACHE LAW (long jobs at a run\'s end, the clean point before the wait), THE 400k CAP, FEWER CALLS — the same work at about a third of the price per chapter** (2026-09-20; World/step9/COST_AUDIT_2026-09-20.md).\n' + BA, s)
EA = '### 2026-09-20 — CHAPTER 11 COMPILED: THE RAIN GETS ITS CELL'
ENTRY = ('### 2026-09-20 — THE COST AUDIT: WHERE A CHAPTER\'S PRICE GOES, AND THREE RULES\n'
         'Brian asked for a complete audit: the program had grown and each chapter cost more, and he asked whether one book at a time and then integrating\n'
         'would help. The answer came from the transcripts, one usage per API call, not from a guess. The bill splits three ways: cache writes 45%, cache\n'
         'reads 37%, output 17%. Under the writes sat one mechanism: 169 calls that re-wrote the whole context from nothing, 126 of them after a wait of\n'
         'five to sixty minutes — the gates chain, the sweep, the positions table, a pause. The prompt cache dies at five minutes, and on the far side of\n'
         'every longer wait the whole pile is written again. That is a third of nine days\' bill, and it grows with the program because every wait grew.\n'
         'Under the reads sat the context itself: a third of the calls ran past 600k against the rule\'s 300k and carried 57% of the reads. The typing —\n'
         'the runners, the dockets\' verdicts, the records — was a sixth; the paperwork per sitting under a twentieth. So "one book at a time" was set\n'
         'aside: it trims the paperwork, and a slip found after ten chapters is ten chapters wide. Three rules instead, none of which touches what is read,\n'
         'typed or gated: the cache law (every long job launched at the end of its run, the clean point before the wait, compaction before a break; a short\n'
         'run on a small context reads the result), the 400k cap, and fewer calls (batching, never skipping). Projected: the same work at about a third of\n'
         'the price. The record with its numbers: World/step9/COST_AUDIT_2026-09-20.md.\n\n')
s = sub(BR, EA, ENTRY + EA, s); W(BR, s)
# 7. THE STATE DOC — #199 addendum 4; 8. THE ADDENDA; 9. COST_AUDIT's ruling
SD = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
W(SD, R(SD).rstrip('\n') + '\n\n#199 ADDENDUM 4 (2026-09-20, after the push bb62e90 — THE COST AUDIT on the owner\'s "Do a complete audit of our process … I can\'t pay $1000 a chapter", then his rulings "Yes I like a b and c" and "Let\'s go to 400 a b and c"; A CLEAN COMPACTION POINT): ' + RULE + ' THE RECORDS: COST_AUDIT_2026-09-20.md (the numbers, the options, the ruling), the recovery page\'s cost bullet rewritten (10,2xx bytes under the cap), RECORD_FORMS, THE_STEPS, GATES_CHAIN.md, the map\'s newest section, THE_BRIEFING (the bullet and an entry), the addenda §53, the memory (cost-rules-no-polling.md; the index line). UNCOMMITTED since bb62e90: the post-push commit-state lines and these records. NEXT ON THE RULING: CHAPTER 12\'s reading (12:1-32) in ONE run + its tail under the three rules — the reading\'s chain launched at the run\'s end. POST-COMPACTION REREADS: the recovery page, the map\'s newest section (THE COST AUDIT AND THE THREE RULES; the AS BUILT of 9b above it), MEMORY.md.\n')
AD = 'logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md'; a = R(AD); ns = [int(x) for x in re.findall(r'^## §(\d+)', a, re.M)]; N = max(ns) + 1
W(AD, a.rstrip('\n') + '\n\n## §%d — THE COST AUDIT AND THE THREE RULES (2026-09-20): World/step9/COST_AUDIT_2026-09-20.md; the state doc\'s #199 addendum 4\n' % N + RULE + '\n')
CA = 'World/step9/COST_AUDIT_2026-09-20.md'; W(CA, R(CA).rstrip('\n') + '\n\n## 6. THE RULING (2026-09-20)\n"Yes I like a b and c. Do you agree? Will that save money not lose quality" — agreed: the three change WHEN things happen and HOW MANY calls, not what is read, typed or gated. "What if we remove the cap for B" — the pile keeps its rent (reads 37%%); the cap at 400k recommended as one compaction per sitting. **"Let\'s go to 400 a b and c" — RULED: A THE CACHE LAW, B THE 400k CAP, C FEWER CALLS.** Written into the recovery page, RECORD_FORMS, THE_STEPS, GATES_CHAIN.md, the map, THE_BRIEFING, the state doc (#199 addendum 4), the addenda §%d, the memory.\n' % N)
# 10. THE MEMORY — the cost-rules note and the index line
CR = f'{MEM}/cost-rules-no-polling.md'; W(CR, R(CR).rstrip('\n') + '\n\n**RULED 2026-09-20 ("Yes I like a b and c" … "Let\'s go to 400 a b and c"):** ' + RULE + '\n\n**Why:** the audit\'s numbers (a third of the bill the re-writes after five-minute waits; a third the fat context). **How to apply:** write the chain\'s readers BEFORE launching it; launch it in the background at the run\'s end; write the clean point; announce; the owner compacts; the tail reads the summary on a small context. Watch the context: at ~400k end the run at its next clean point. One call per step; batch reads; never a call to re-verify what a gate verifies.\n')
IDX = f'{MEM}/MEMORY.md'; s = R(IDX)
OLDL = [l for l in s.split('\n') if l.startswith('- [⚠⚠ COST RULES](cost-rules-no-polling.md)')]; assert len(OLDL) == 1
s = s.replace(OLDL[0], '- [⚠⚠ COST RULES](cost-rules-no-polling.md) — the bill is CONTEXT × CALLS + RE-WRITES (the audit 2026-09-20: World/step9/COST_AUDIT_2026-09-20.md); ⚠ RULED 2026-09-20: A THE CACHE LAW (the cache dies at 5 min — long jobs launched at a run\'s END, the clean point before the wait, compact before a break, THE TAIL reads the summary), B THE 400k CAP, C FEWER CALLS (batching, never skipping); TWO RUNS + the tail a compile, ONE + the tail a reading; never poll; the chain ~18 min; the import cache')
n = len(s.encode('utf-8')); print('MEMORY.md would be %d bytes (cap 17000)' % n); assert n <= 17000; W(IDX, s)
print('written: the recovery page, RECORD_FORMS, THE_STEPS, GATES_CHAIN.md, the map, THE_BRIEFING, the state doc, the addenda §%d, COST_AUDIT, the memory note, the index' % N)
