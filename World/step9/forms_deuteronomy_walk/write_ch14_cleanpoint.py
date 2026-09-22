import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14: THE CLEAN COMPACTION POINT after the rows, BEFORE the ledger (sitting 11's lesson 4 — the design named it;
# the owner's /context mid-run the signal) — the state doc's #204 block appended, the recovery page's section 2 edited under its cap, the memory index line
# edited under its cap; every text built whole before a file is opened; sizes asserted. write_ch13_cleanpoint.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser('~')
MEM = f'{HOME}/.claude/projects/-Users-Shared-TorahSim/memory'
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
IDX = f'{MEM}/MEMORY.md'
rows = [l.rstrip('\n').split('\t') for l in open(f'{SP}/ch14_timing.tsv', encoding='utf-8') if l[:1].isdigit()]
T12 = [r for r in rows if r[1].startswith('12 ')]; TS = sum(int(r[2]) for r in T12)
BLOCK = f"""
#204 (2026-09-21, THE DEUTERONOMY WALK sitting 12 — CHAPTER 14's READING, ONE RUN + ITS TAIL under THE COST RULES; on the owner's "Go" after 11b's tail — chapter 13 UNCOMMITTED since fb797a1, the commit on his word; A CLEAN COMPACTION POINT TAKEN AFTER THE ROWS, BEFORE THE LEDGER — the design named the point, the owner's /context mid-run the signal; sitting 11's lesson 4 applied): THE STATE: THE READING IS ON DISK, THE LEDGER NOT YET WRITTEN. The rereads (the recovery page, the map's 11b design with its docket paragraph, the memory index; THE_STEPS' compiler block, Step 2's head, Step 5's head; the map's sitting 11 design and AS BUILT; the 11b box's items owed to 14); the measurements (ch14_dump0.py derived from the forms' ch13_dump0.py by 26 asserted substitutions — the derive's own guard tripped once on its own comment; the split with piska 96's tail folded in, 96:10 fetched from the export by its consonants — the consonant tests retyped to strip the points; ch14_measure1.py — chapter 13's helpers and register block by substitution, its sections chapter 14's own; 131 KB of print); THE INK (ch14_ink.py, 100 asserts typed from the prints: 27 fell on the first pass — the instrument's shapes (the word table's pairs, the Aramaic helper's string, the book-alone name DT) and three lists typed from memory; 2 on the second; 0 on the third); THE DESIGN in the map ("Sitting 12 — CHAPTER 14 … THE DESIGN", 17,530 bytes, lint 0; seven claims DV14-01..07 predicted, the fold 227 -> 228 / 2245 -> 2252 / the hash unmoved; the register gate DECLARED 98 unmoved); THE ROWS, EVERY ONE READ WHOLE IN BOTH FILES AND TYPED: the spine's 111 (piska 96's tail 9-12; 97-110) in <scratch>/ch14_rows_sifrei_96_103.py (41 — MATERIAL 31 / CONTEXT 10) and ch14_rows_sifrei_104_110.py (70 — MATERIAL 45 / CONTEXT 25), the three outside rows in ch14_rows_outside.py (76:7 REREAD WHOLE — chapter 12's; 228:5; 312:1), Onkelos 14:1-29 in ch14_rows_onkelos_a.py (1-20) and _b.py (21-29); every quotation CUT by consonants — ONE miss on the first import check (105:16's "casually" spelled without the aleph in the export), retyped from the export; the second check: FAIL [], the spine's keys == READ_ROWS (111), Onkelos == SPAN (29), the outside == OUTSIDE (3); the middot checked in MIDDOT.md before typed (I1 the a fortiori at 101:10, 76:7, 106:3, 106:4, 107:4, 107:7; I2 the analogy at 96:12, 99:2, 103:3, 103:4, 107:16, 109:2; I3 the paradigm at 103:8, 228:5, 105:8, 107:11, 110:1, 110:2; the juxtaposition named without a code at 106:4-5). THE TIMING so far (the sitting's tsv <scratch>/ch14_timing.tsv): {len(T12)} rows, {TS} machine seconds. NOT COMMITTED (since fb797a1): chapter 13's reading and compile, and this sitting's map section. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (compact now). NEXT ON HIS WORD (after the compaction: "Reread", then "Go"): THE TAIL — write_ch14_ledger.py derived from the forms' write_ch13_ledger.py (the five row files; the prior reads marked REREAD WHOLE — 76:7, 104:8, 106:5; coverage computed: the Sifrei 111 + 3, Onkelos 29, the kin's credits by name from the ink), lint 0; then the display patch from the G print (ch14_patch_overrides.py; ch14_ink_body_c.py — the ink rerun PATCHED), write_ch14_manifest.py (seven claims), seat_ch14.py (seven WITNESS_READ at 14:1, 3, 9, 21, 22, 24, 28; step E), the shells derived (ch14_chain.sh, ch14_fold.sh, ch14_gates.sh — the fold 228 / 2252 / the hash), the manifest, verify_claims and the labels census in the foreground, the chain LAUNCHED in the background with write_ch14_records.py and copy_ch14_forms.py written first, the summary read once, the records from the sheet in one call (the map's AS BUILT, COMPILE_DEBT's sitting-12 box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, this doc, the addenda, the recovery page, the memory), the forms copied, the commit message, the timing table. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 12 — CHAPTER 14 … THE DESIGN" (the newest section), MEMORY.md; then this block.
"""
sd = open(SD, encoding='utf-8').read(); assert '#203 ADDENDUM 3' in sd
if '#204 (' not in sd: open(SD, 'a', encoding='utf-8').write(BLOCK)
else: print('#204 already appended — the page and the index alone')
rec = open(REC, encoding='utf-8').read()
def sub_line(t, prefix, new):
    ls = t.split('\n'); hits = [i for i, l in enumerate(ls) if l.startswith(prefix)]; assert len(hits) == 1, (prefix, hits); ls[hits[0]] = new; return '\n'.join(ls)
rec = sub_line(rec, '## 2. WHERE IT STANDS (', '## 2. WHERE IT STANDS (2026-09-21, sitting 12 mid-run; state doc #204 newest)')
rec = sub_line(rec, '- COMMITTED fb797a1', '- COMMITTED fb797a1 (NOT PUSHED); 13 uncommitted. SITTING 12 (ch 14) MID-RUN at #204: 143 rows typed. NEXT ON HIS\n  WORD: THE TAIL (the ledger, the patch, the manifest, the chain).')
def sub1(t, a, b):
    assert t.count(a) == 1, (t.count(a), a[:50]); return t.replace(a, b)
rec = sub1(rec, 'three REUSES (seven count\n  seats retyped); the purge formula at its first seat; four PARAMETERS; 40 persons, 6 exempt, 1 lashed; 12:1 & 28:69 DAEMONS.', 'three REUSES; the purge\n  formula at its first seat; four PARAMETERS; 12:1 & 28:69 DAEMONS.')
assert len(rec.encode('utf-8')) <= 10240, len(rec.encode('utf-8'))
open(REC, 'w', encoding='utf-8').write(rec)
idx = open(IDX, encoding='utf-8').read()
OLD = "11b DONE (56/56; 3 reuses; the purge named); commit next"; NEW = "11b DONE; 12 (ch 14 reading) MID-RUN at #204 — rows typed, ledger next; 13 uncommitted"
assert idx.count(OLD) == 1, idx.count(OLD); idx = idx.replace(OLD, NEW); assert len(idx.encode('utf-8')) <= 17000, len(idx.encode('utf-8'))
open(IDX, 'w', encoding='utf-8').write(idx)
print('THE CLEAN POINT: #204 appended (%d bytes); the recovery page %d bytes; MEMORY.md %d bytes; timing rows %d, %d s' % (len(BLOCK.encode('utf-8')), len(rec.encode('utf-8')), len(idx.encode('utf-8')), len(T12), TS))
