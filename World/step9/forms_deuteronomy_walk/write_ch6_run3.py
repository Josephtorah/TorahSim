#!/usr/bin/env python3
# RUN 3 OF CHAPTER 6 CLOSED (THE DEUTERONOMY WALK sitting 4, 2026-09-17): the checkpoint — the state doc's #190 ADDENDUM 2 (naming RUN 4's first
# step), the map's "RUN 3 — AS RUN" paragraph, the memory (the walk note + the index line). Every text built here; the caps asserted before any
# file is opened; --check prints the plan only.
import os, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def read(p): return open(p, encoding='utf-8').read()
U = read(f'{ROOT}/logic/units/deu_06_shema.yaml'); T = read(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'status: frozen' in U and U.count('- op: WITNESS_READ') == 6 and 'assert len(W["units"]) == 220' in T and 'assert len(W["standing"]) == 2203' in T, 'the run as built'
assert os.path.exists(f'{ROOT}/logic/py_units/deu_06_shema.py') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/deu_06_shema_claims.json')
plans = []
# 1. the state doc
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = read(P); assert '#190 ADDENDUM 2' not in s and '#190 ADDENDUM 1' in s
ADD = ('\n\n#190 ADDENDUM 2 (2026-09-17 — RUN 3 OF CHAPTER 6 CLOSED, on the owner\'s "Continue" after run 2 (no compaction between — his choice at 349k); THE DEUTERONOMY WALK sitting 4: the seat, the chain and the fold). '
       'THE DISPLAY LAYER (ch6_patch_overrides.py, sitting 3\'s form; the anchors the last rows of sitting 3\'s two blocks): 33 rows by gloss and 24 by reference under the marker "THE DEUTERONOMY WALK sitting 4 (2026-09-17, Deuteronomy 6)" — by_ref 496, by_gloss 385 after; the ink rerun with PATCHED true, 0 failing (113 asserts); the overrides file lint 0. '
       'THE MANIFEST (write_ch6_manifest.py): SIX claims DV06-01..06 (6:1-3 the header; 6:4-5 the creed and the love; 6:6-9 the words\' four duties; 6:10-15 the gift and the warning; 6:16-19 Massah, keep, the right and the good; 6:20-25 the son\'s question and the answer), every one of the ledger\'s 97 CITE INDEX names used by a claim (asserted), the checks the block\'s longest store-piece whole — 6:1 "the commandment", 6:5 "your might", 6:7 "teach them diligently", 6:13 "swear", 6:16 "Massah", 6:20 "asks you" (6:4\'s two words refused by the script itself); verify_claims 6 VERIFIED / 0 FAILED; claim_labels_census --strict GREEN (385 claims labeled, debt 0). '
       'THE SEATS (seat_ch6.py): six WITNESS_READ operators at 6:1, 4, 6, 10, 16, 20, step E, the scenarios in the anchor form (7); verify_text GREEN (25 steps, 7 scenarios). THE RITUAL (ch6_chain.sh, ROOT from the cwd\'s git, SP from the script\'s own place): 13 PASS — RITUAL COMPLETE for the 220th frozen unit; logic/py_units/deu_06_shema.py written and self-proved; the reading-debt gate\'s standing note as at every walk unit. '
       'THE FOLD (ch6_fold.sh — the tripwire\'s literals set to the prediction BEFORE the bake: units 220, standing 2197 + 6 = 2203, hash unmoved): CORPUS TRUTH GREEN on the unwritten fold — 220 units, 1809 facts, 341 demands (191 open), hash 8b8fff1fa28953af — THE PREDICTION MATCHED; the bake (corpus_world.py) rewrote corpus_world.sqlite and CORPUS_TRUTH.py with the same literals; GREEN again after. build_world ALL GREEN (the one database agrees with the fold); the journal gate GREEN (12 kinds, 9674 rows matching the header — 9660 at sitting 3); the register gate --strict GREEN (no seat in the chapter — unchanged); the home-path gate GREEN. '
       'TWO MISSES OF THE RUN, both forms: the ink\'s ledger-list guard (run 2\'s patch) excluded the new ledger on one side of the compare only — the ink failed at import and the display patch\'s first call wrote nothing (the assert before the write held; fixed, rerun); verify_claims takes the manifest\'s PATH, not the unit id. No engine file changed — the sweep as at 3b\'s close (the tape untouched; the reading adds no line). '
       'NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. Uncommitted since 7c8554e: RESEARCH_LOG, the map, gates_chain.sh, CORPUS_TRUTH.py, word_gloss_overrides.yaml, the state doc, the recovery page\'s line, UNIT_INDEX.html, ALL_UNITS.py, deu_06_shema.yaml (frozen), and new: large_letter_probes.py, the manifest deu_06_shema_claims.json, the ledger deu_06_vaetchanan_2026-09-17.md, UNIT_deu_06_shema.html, py_units/deu_06_shema.py. '
       'THE WORD FOR THE NEXT SITTING — RUN 4 OF CHAPTER 6, its first step: read the sheet World/step9/RECORD_FORMS.md and derive write_ch6_records.py from write_ch5_records.py (the forms folder) by sed, read where it differs; then the records in ONE call — the map\'s "Sitting 4 — AS BUILT", COMPILE_DEBT.md\'s 4b box (the owed list of the design + the tefillin cell\'s open row), the delegated FULL RULE stamp row (logic/findings/STAMP_LEDGER.md), THE_STEPS, THE_BRIEFING (the scoreboard: 220 units), THE_WORLD, World/RESUME.md, MISHNAH_TOPICS (the rows named this sitting), MOVE_CATALOG if a move is new, the recovery page REWRITTEN WHOLE under 10,240 bytes (section 2 to sitting 4\'s close; the walk line), the forms copied (copy_ch6_forms.py from copy_ch5_forms.py — the scratchpad\'s ch6_* and write_ch6_* scripts and the prints), the memory (the walk note, the index line), every lint at its baseline; then #190 addendum 3 — the sitting\'s close, a clean point — and the commit message drafted for his word. '
       'POST-COMPACTION REREADS unchanged: the recovery page, the map\'s Sitting 4 section (its RUN 2 and RUN 3 paragraphs), MEMORY.md.\n')
plans.append((P, s.rstrip('\n') + ADD))
# 2. the map
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
s = read(P); assert 'RUN 3 — AS RUN' not in s and 'RUN 2 — AS RUN' in s
MAP = ('\n\nRUN 3 — AS RUN (2026-09-17, on "Continue" after run 2): the display layer patched (33 by gloss, 24 by reference; by_ref 496, by_gloss 385), the ink rerun\n'
       'PATCHED with 0 failing; the manifest\'s six claims with every CITE INDEX name used, verify_claims 6/0, the labels census GREEN; six WITNESS_READ seats at 6:1, 4, 6, 10,\n'
       '16, 20, step E, seven anchor scenarios, verify_text GREEN; the ritual 13 PASS — the 220th frozen unit and its Python layer; the fold predicted and matched (220 units,\n'
       'standing 2203, hash 8b8fff1fa28953af; 1809 facts, 341 demands) before and after the bake; build_world ALL GREEN; the journal gate GREEN (9674 rows); the register\n'
       'gate --strict GREEN; the home-path gate GREEN. ⚠ LESSONS (run 3): A GUARD THAT FILTERS ONE SIDE OF A COMPARE MUST FILTER BOTH — the ink\'s ledger-list assert,\n'
       'patched at run 2 to ignore the sitting\'s own ledger, appended it to the expected list and failed at import; the display patch\'s first call wrote nothing (its own\n'
       'assert stood before the write — the form held). THE CLAIM VERIFIER TAKES THE MANIFEST\'S PATH. THE FOLD SCRIPT WAITS ON THE FROZEN STATUS (the unit\'s indented\n'
       '"status: frozen"). THE ORDER (RUN 4, the first step): the sheet RECORD_FORMS.md read, write_ch6_records.py from write_ch5_records.py by sed → the records in one\n'
       'call (this section\'s AS BUILT, the 4b debt box, the stamp row, THE_STEPS, THE_BRIEFING, THE_WORLD, RESUME, MISHNAH_TOPICS, the recovery page whole, the forms\n'
       'copied, the memory) → the lints → #190 addendum 3 (the sitting\'s close) → the commit message drafted for the owner\'s word.\n')
plans.append((P, s.rstrip('\n') + MAP))
# 3. the memory note
P = f'{MEM}/deuteronomy-walk.md'
s = read(P); assert 'RUN 3 DONE' not in s and 'RUN 2 DONE' in s
MN = ('\n\nSITTING 4 RUN 3 DONE 2026-09-17 (on "Continue", no compaction between): the display layer patched (by_ref 496, by_gloss 385), the manifest deu_06_shema_claims.json (six claims, verify 6/0, labels GREEN), the seat (six WITNESS_READ, step E), the ritual 13 PASS — deu_06_shema the 220th frozen unit, the fold 220 / 2203 / 8b8fff1fa28953af matched, build_world ALL GREEN, the journal gate GREEN (9674 rows), the register and home gates GREEN. The scripts ch6_patch_overrides.py, write_ch6_manifest.py, seat_ch6.py, ch6_chain.sh, ch6_fold.sh in the scratchpad (copied at run 4). Clean compaction point (#190 addendum 2). NEXT: RUN 4 — the records from the sheet in one call (write_ch6_records.py from write_ch5_records.py), the recovery page rewritten, the forms copied, #190 addendum 3, the commit message for his word.\n')
plans.append((P, s.rstrip('\n') + MN))
# 4. the index line
P = f'{MEM}/MEMORY.md'
s = read(P)
old = 'SITTING 4 (ch 6) RUNS 1-2 DONE 2026-09-17; NEXT: RUN 3 seat, chain, fold'
new = 'SITTING 4 (ch 6) RUNS 1-3 DONE 2026-09-17 (220 units); NEXT: RUN 4 the records'
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8'))
plans.append((P, s2))
for p, s2 in plans: assert s2 != read(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p, len(read(p)), '->', len(s2))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2.encode('utf-8')))
print('run 3 checkpoint written')
