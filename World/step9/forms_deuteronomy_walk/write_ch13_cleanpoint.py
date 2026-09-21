import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13: THE CLEAN COMPACTION POINT after the rows and the ledger (the 600k cap; chapter 12's #200 precedent) — the
# state doc's #202 block appended, the recovery page's section 2 edited under its cap, the memory index line edited under its cap; every text built whole
# before a file is opened; sizes asserted. write_ch12_cleanpoint.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser('~')
MEM = f'{HOME}/.claude/projects/-Users-Shared-TorahSim/memory'
rows = [l.rstrip('\n').split('\t') for l in open(f'{SP}/ch13_timing.tsv', encoding='utf-8') if l.strip()]
TIMING = '; '.join(f'{name} {secs}s (at {hhmm})' for hhmm, name, secs, rc in rows)
# 1. THE STATE DOC — a new compaction block at the file's end
D = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = open(D, encoding='utf-8').read()
assert '#201 ADDENDUM 4 — READY TO COMPACT' in s
DONE = '═══ COMPACTION POINT #202' in s   # never twice
BLOCK = ('═══ COMPACTION POINT #202 (2026-09-21 — INSIDE CHAPTER 13\'s READING, sitting 11 of THE DEUTERONOMY WALK, on the owner\'s "Go" after the reread that followed 10b\'s compaction: '
 'the clean point at the 600k cap after the rows and the ledger — chapter 12\'s #200 precedent). THE STATE: the rereads done; ch13_dump0.py and ch13_measure1.py run (the kin by computation beside the law kin named; the register\'s finder run — no receipt in the chapter); '
 'THE INK ch13_ink.py GREEN ON ITS FIRST TYPED PASS (no form fell; the driver\'s first launch from the scratchpad found no git root — a launch, not a fact; the second pass added the English\'s three citation slips as asserts); THE DESIGN in the map ("Sitting 11 — CHAPTER 13 … THE DESIGN", lint 0); '
 'THE ROWS — the 97 spine rows of piskaot 82-96 (fourteen heads and the headless 88 folded in on its consonants; PISKA 96\'s ROWS 9-12 ARE 14:1\'s AND WAIT FOR CHAPTER 14 — never read ahead) in three files, the 19 Onkelos rows in one, the six outside rows in one, EVERY ROW READ WHOLE; THE LEDGER logic/oral_triage/deu_13_reeh_2026-09-21.md WRITTEN ON ITS FIRST RUN (122 sources — Onkelos 19 MATERIAL; the spine 97: MATERIAL 59 / CONTEXT 38; the outside 6 MATERIAL; coverage computed; NO CUT MISSED; lint 0; 100,667 bytes). '
 'THE TIMING SO FAR (ch13_timing.tsv): ' + TIMING + '. NOT COMMITTED: the ledger, the map\'s design section, this block, the recovery page\'s line, the memory line — beside the four records\' commit-id lines uncommitted since 2b0c9c8. '
 'NEXT (THE TAIL, on a small context after the compaction): ch13_patch_overrides.py derived from ch12_patch_overrides.py (34 by gloss, 139 by reference — the ink\'s own printed counts; the anchors sitting 10\'s last rows — the by_gloss block\'s last row walked from sitting 10\'s marker, the by_ref block\'s "Deut.12.31:19": "they-burn"), the ink rerun PATCHED; write_ch13_manifest.py (six claims DV13-01..06 at 13:1, 2, 7, 13, 17, 19 — the checks "you shall not add" 13:1, "is testing" 13:4, "entices you" 13:7, "diligently" 13:15, "wholly" 13:17, "the right in the eyes of" 13:19; the spine\'s rows by piska from the CITE INDEX); seat_ch13.py; ch13_chain.sh, ch13_fold.sh (226 -> 227, 2239 -> 2245, the hash 8b8fff1fa28953af unmoved), ch13_gates.sh LAUNCHED in the background with write_ch13_records.py and copy_ch13_forms.py written first; the summary read once; the records from the sheet (COMPILE_DEBT\'s sitting-11 box owing 11b the docket named in the design AND chapter 14\'s split the four rows 96:9-12); the forms; the commit message; the timing table and the report. '
 'IF THIS COMPACTS HERE: reread the recovery page, the map\'s "Sitting 11 — CHAPTER 13 … THE DESIGN", MEMORY.md — then the tail\'s first step, the display patch.\n')
assert not re.search(r'/Users/(?!Shared/)', BLOCK) and HOME not in BLOCK
if not DONE: open(D, 'a', encoding='utf-8').write('\n' + BLOCK)
# 2. THE RECOVERY PAGE — section 2 edited under its cap
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
t = open(P, encoding='utf-8').read()
old1 = '- SITTINGS 10/10b (ch 12; EVERY STEP TIMED — 10b 2860 s / 64 steps): the place INSTALLED (high_places_banned REUSED — the eras\n  table\'s ink); the slaughter law a STATUS conditional on the entry; the rite a PARAMETER; four lines, no marker.\n'
assert t.count(old1) == 1; t = t.replace(old1, '')
old2 = '- COMMITTED AND PUSHED 2b0c9c8 (2026-09-21). 10b DONE (65/65; tape 10/10; the docket 1,538 rows). NEXT: ch 13\'s reading on his word.'
new2 = '- SITTING 11 IN FLIGHT (ch 13 read, 122 sources whole, the ledger deu_13_reeh WRITTEN, the ink green first pass, uncommitted): NEXT\n  THE TAIL — the display patch, the manifest, the seat, the chain launched, the records (the state doc #202). Piska 96:9-12 are 14:1\'s.'
assert t.count(old2) == 1; t = t.replace(old2, new2)
old3 = '## 2. WHERE IT STANDS (2026-09-21, 10b done; the state doc #201 add. 4 the newest)'
new3 = '## 2. WHERE IT STANDS (2026-09-21, sitting 11 in flight; the state doc #202 the newest)'
assert t.count(old3) == 1; t = t.replace(old3, new3)
old4 = 'the newest instances: the map\'s "Sitting 10b" and "Sitting 10")'
new4 = 'the newest instances: the map\'s "Sitting 11" and "Sitting 10b")'
assert t.count(old4) == 1; t = t.replace(old4, new4)
assert len(t.encode()) <= 10240, len(t.encode())
open(P, 'w', encoding='utf-8').write(t)
# 3. THE MEMORY INDEX LINE — under 17,000 bytes
M = f'{MEM}/MEMORY.md'
m = open(M, encoding='utf-8').read()
oldm = 'ch 1-11 COMPILED, PUSHED bb62e90; ch 12 READ AND FROZEN (sitting 10, timed); 10b DONE (65/65, the reuse); COMMITTED AND PUSHED 2b0c9c8 (2026-09-21); NEXT: ch 13'
newm = 'ch 1-12 COMPILED, PUSHED 2b0c9c8 (2026-09-21); ch 13 READ (sitting 11, the ledger written, uncommitted); NEXT THE TAIL — the patch, the manifest, the seat, the chain, the records'
assert m.count(oldm) == 1; m = m.replace(oldm, newm)
oldn = 'PUSHED through 2b0c9c8 (2026-09-21); ⚠ THE HISTORY WAS REWRITTEN'
assert m.count(oldn) == 1; m = m.replace(oldn, '⚠ THE HISTORY WAS REWRITTEN')
assert len(m.encode()) < 17000, len(m.encode())
open(M, 'w', encoding='utf-8').write(m)
print('the clean point written: the state doc #202', 'appended' if not DONE else 'already there', '| the recovery page', len(t.encode()), 'bytes | MEMORY.md', len(m.encode()), 'bytes')
