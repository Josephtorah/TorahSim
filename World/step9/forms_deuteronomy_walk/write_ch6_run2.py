#!/usr/bin/env python3
# RUN 2 OF CHAPTER 6 CLOSED (THE DEUTERONOMY WALK sitting 4, 2026-09-17): the checkpoint — the state doc's #190 ADDENDUM 1 (naming RUN 3's first
# step), the map's "RUN 2 — AS RUN" paragraph, a RESEARCH_LOG entry for the spelling divergence, the memory (the walk note + the index line).
# Every text built here; the caps and the lints asserted before any file is opened for writing; --check prints the plan only.
import os, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def read(p): return open(p, encoding='utf-8').read()
LEDGER = 'logic/oral_triage/deu_06_vaetchanan_2026-09-17.md'
L = read(f'{ROOT}/{LEDGER}')
assert '**read: 97 of 97 — COMPLETE**' in L and L.count('\n- Sifrei Devarim ') == 75 and L.count('\n- Onkelos Deut 6:') == 25, 'the ledger as written'
plans = []
# 1. the state doc
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = read(P); assert '#190 ADDENDUM 1' not in s and s.rstrip().endswith(('.', ')'))
ADD = ('\n\n#190 ADDENDUM 1 (2026-09-17 — RUN 2 OF CHAPTER 6 CLOSED, on the owner\'s "go" after the compaction; THE DEUTERONOMY WALK sitting 4, the rows and the ledger). '
       'THE REREADS: the recovery page, the map\'s "Sitting 4 — THE DESIGN", MEMORY.md; then THE_STEPS\' compiler block, Step 2 whole, Step 5\'s head. THE ROWS READ: the spine\'s 67 rows piska by piska '
       'at a short cut (the English capped at 1,500 characters, the Hebrew\'s opening 150 for the cuts — from $SP/ch6_sifrei_spine.txt), the eight outside rows and the excluded 62:4 (ch6_sifrei_outside.txt), '
       'the twenty-five Onkelos rows (ch6_onkelos.txt whole). THE SCRIPTS (the scratchpad; sitting 3\'s forms): ch6_rows_sifrei_31.py (10 rows), ch6_rows_sifrei_32.py (20 + the credited 32:2), '
       'ch6_rows_sifrei_33_36.py (34 + the credited 33:4 and 36:10), ch6_rows_outside.py (8), ch6_rows_onkelos_a.py (6:1-13), ch6_rows_onkelos_b.py (6:14-25), write_ch6_ledger.py — every quotation cut by '
       'consonants (SP_ / HP / AP), ONE miss on the first run (32:13\'s "that-three" one word in the shelf — retyped), FAIL empty; the ink\'s ledger-list assert guarded to ignore the sitting\'s own ledger. '
       f'THE LEDGER: {LEDGER} — 97 sources (25 Onkelos: MATERIAL 19 / CONTEXT 6; the spine 64 fresh: MATERIAL 45 / CONTEXT 19, + 3 CREDITED with quick looks; outside 8: MATERIAL 5 / CONTEXT 3), '
       'coverage COMPUTED (missing 0, extra 0 on both files\' row counts), lint 0, 106,879 bytes, the home-path gate GREEN. TWO FINDS OF THE RUN, both in the ledger\'s crowns: (1) THE TWO FILES OF THE EXPORT '
       'DIVERGE AT 36:10 — the Hebrew\'s row is the parable of the king and his wife (36:9\'s close), the English\'s row is its own 37:2 repeated (Hebron and Zoan); the Genesis credit (gen_29) stands on the '
       'English\'s text, the Hebrew\'s parable read fresh at the quick look — a lesson: a credit is a credit on the file that was read; the two files are compared row by row, not row-counted. '
       '(2) THE COUNT FROM THE SPELLINGS DIVERGES (the Sifrei 35:4; Sanhedrin 4b, Menachot 34b): the shelf\'s four compartments need 11:18 "frontlets" DEFECTIVE; the DB spells 11:18 with the vav '
       '(6:8 defective, Exodus 13:16 plene — the ink\'s FRONT, asserted) — filed to the compile (4b) as the tefillin cell\'s open row; RESEARCH_LOG\'s entry of this date. Also read from the shelf: the creed\'s '
       'first utterance at Jacob\'s deathbed (31:6), the two sets recited and bound with the ten words in neither (34:2-3, 35:1-2), the verbal analogy with two candidates (36:2 — the shelf\'s own exhibit of '
       'I2\'s reception rule), extension after extension on the one-letter pair 6:9 / 11:20 (36:3), the spoil permitted by 6:11 (201:3), singular against plural (41:20). THE MAP: "RUN 2 — AS RUN" paragraph '
       'appended to the Sitting 4 section. THE MEMORY: the walk note and the index line. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. Uncommitted since 7c8554e: the research log, the map, the chain, '
       'the probe, the state doc, the recovery page\'s line, the new ledger. THE WORD FOR THE NEXT SITTING — RUN 3 OF CHAPTER 6, its first step: the display-layer patch — write_ch6_overrides.py from '
       'the ink\'s OVERRIDE_GLOSS (33) and OVERRIDE_REF (24) into logic/glosses/word_gloss_overrides.yaml under the marker "THE DEUTERONOMY WALK sitting 4 (2026-09-17, Deuteronomy 6)" (sitting 3\'s form '
       'in forms_deuteronomy_walk/), the ink rerun with PATCHED true; then write_ch6_manifest.py (six claims DV06-01..06, the checks the block\'s longest store-piece whole — never 6:4\'s two words), '
       'seat_ch6.py (six WITNESS_READ at 6:1, 4, 6, 10, 16, 20, step E), ch6_chain.sh (the ritual), the fold predicted (units 220, standing 2203, hash unmoved) and matched, build_world, the journal gate, '
       'the register gate --strict (GREEN unchanged, no seat in the chapter), the home-path gate; the checkpoint #190 addendum 2. POST-COMPACTION REREADS unchanged: the recovery page, the map\'s Sitting 4 '
       'section, MEMORY.md.\n')
plans.append((P, s.rstrip('\n') + ADD))
# 2. the map — the run's paragraph at the section's end (the file's tail)
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
s = read(P); assert 'RUN 2 — AS RUN' not in s and s.rstrip().endswith('nothing of\nthe engine touched.')
MAP = ('\n\nRUN 2 — AS RUN (2026-09-17, on "go" after the compaction): the rereads (the three files; THE_STEPS\' compiler block, Step 2, Step 5\'s head); the spine\'s 67 rows read piska by piska at a\n'
       'short cut, the eight outside rows, the twenty-five Onkelos rows; six row scripts and the ledger writer on sitting 3\'s forms; the ledger logic/oral_triage/deu_06_vaetchanan_2026-09-17.md —\n'
       '97 sources, coverage computed (missing 0, extra 0), lint 0; one cut missed on the first run (a "that-" prefix fused to its word in the shelf), retyped. ⚠ LESSONS (run 2): THE EXPORT\'S TWO\n'
       'FILES CAN DIVERGE ROW BY ROW — at 36:10 the Hebrew carries the parable of the king\'s wife and the English repeats its own 37:2 (Hebron and Zoan); the Genesis credit stood on the English\'s\n'
       'text; a credit is a credit on the file that was read, and the quick look opens the other file. THE SHELF COUNTS A SPELLING THE INK DOES NOT HAVE — the four compartments (35:4; Sanhedrin 4b,\n'
       'Menachot 34b) need 11:18 "frontlets" defective; the DB (the Leningrad text) writes it with the vav: a divergence of the ink from the shelf on a spelling, filed to the compile as the tefillin\n'
       'cell\'s open row (RESEARCH_LOG of this date). A "THAT-" PREFIX IS PART OF THE SHELF\'S TOKEN — the cut names the fused word. THE ORDER (RUN 3, the first step): write_ch6_overrides.py — the\n'
       'display-layer patch (33 by gloss, 24 by reference) under the sitting\'s marker, the ink rerun PATCHED; then the manifest, the seat, the chain, the fold (220 / 2203 / the hash unmoved),\n'
       'build_world, the journal gate, the register gate --strict, the home-path gate → the checkpoint (#190 addendum 2, a clean point).\n')
plans.append((P, s.rstrip('\n') + MAP))
# 3. the research log
P = f'{ROOT}/RESEARCH_LOG.md'
s = read(P); assert 'THE FRONTLETS\' THIRD SPELLING' not in s
RL = ('\n\n## 2026-09-17 — THE FRONTLETS\' THIRD SPELLING: THE SHELF\'S COUNT AGAINST THE INK\'S LETTER (THE DEUTERONOMY WALK sitting 4, run 2)\n\n'
      'THE FINDING. The Sifrei on Deuteronomy 35:4 (on 6:8) counts the tefillin\'s four compartments from the word "frontlets" at its three seats — two defective\n'
      'spellings (one each) and one plene (two): לטטפת ("for frontlets", Deuteronomy 6:8), טטפת read defective again at 11:18, and טוטפת ("frontlets", Exodus\n'
      '13:16) plene — "behold four". The Talmud counts the same way (Sanhedrin 4b; Menachot 34b). THE INK AS THE MACHINE HOLDS IT (Data/tanakh.sqlite, the Open\n'
      'Scriptures Hebrew Bible = the Leningrad codex; asserted in the sitting\'s ink script, FRONT): 6:8 לטטפת ("for frontlets", defective), 11:18 לטוטפת ("for\n'
      'frontlets", WITH THE VAV), Exodus 13:16 ולטוטפת ("and for frontlets", with the vav) — the shelf\'s middle seat is plene in the codex. The English translator\n'
      'of the export transliterates 11:18 as the shelf reads it ("totaft"), not as the codex spells it. WHAT IT MEANS FOR THE COMPILE: the count of four is the\n'
      'shelf\'s reading of a text whose 11:18 differs from ours by one letter; the machine cannot reproduce "four" from its own ink by the shelf\'s rule (its count\n'
      'would be 1 + 2 + 2). Filed as the tefillin cell\'s OPEN ROW for the compile of chapter 6 (sitting 4b): the compartments\' number a PARAMETER taught by the\n'
      'shelf, its derivation from the spellings a recorded argument that reads a different witness. The witness question itself (the Talmud\'s Torah text against\n'
      'the Masoretic codex on this word — a known discrepancy in the tradition\'s own literature) is NOT ours to rule; recorded, not resolved. The ledger:\n'
      'logic/oral_triage/deu_06_vaetchanan_2026-09-17.md (the row 35:4 and the crown).\n')
plans.append((P, s.rstrip('\n') + RL))
# 4. the memory note
P = f'{MEM}/deuteronomy-walk.md'
s = read(P); assert 'RUN 2 DONE' not in s
MN = ('\n\nSITTING 4 RUN 2 DONE 2026-09-17 (on "go" after the compaction): the ledger logic/oral_triage/deu_06_vaetchanan_2026-09-17.md — 97 sources (25 Onkelos, the spine\'s 64 fresh + 3 credited, 8 outside), coverage computed, lint 0; the row scripts ch6_rows_sifrei_31/32/33_36.py, ch6_rows_outside.py, ch6_rows_onkelos_a/b.py and write_ch6_ledger.py in the scratchpad (the forms copied at run 4). TWO FINDS: the export\'s two files DIVERGE at Sifrei 36:10 (the Hebrew\'s parable, the English\'s own 37:2 repeated — a credit is a credit on the file read); the shelf\'s four compartments (35:4) need 11:18 "frontlets" DEFECTIVE where the DB spells it plene — RESEARCH_LOG 2026-09-17, the compile\'s open row. Clean compaction point (#190 addendum 1). NEXT: RUN 3 — write_ch6_overrides.py (the display layer, 33 + 24, the marker), the manifest (six claims), seat_ch6.py, ch6_chain.sh, the fold 220 / 2203 / hash unmoved, build_world, the journal gate, the register gate --strict, the home-path gate; then RUN 4 the records.\n')
plans.append((P, s.rstrip('\n') + MN))
# 5. the index line
P = f'{MEM}/MEMORY.md'
s = read(P)
old = 'SITTING 4 (ch 6) RUN 1 DONE 2026-09-17; NEXT: RUN 2 the rows, the ledger'
new = 'SITTING 4 (ch 6) RUNS 1-2 DONE 2026-09-17; NEXT: RUN 3 seat, chain, fold'
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8'))
plans.append((P, s2))
for p, s2 in plans: assert s2 != read(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p, len(read(p)), '->', len(s2))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2.encode('utf-8')))
print('run 2 checkpoint written')
