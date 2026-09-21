import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12: THE CLEAN COMPACTION POINT after the rows and the ledger (the 400k cap; chapter 11's #198 precedent) —
# the state doc's #200 block appended, the recovery page's section 2 edited under its cap, the memory index line edited under its cap; every text built whole
# before a file is opened; sizes asserted.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser('~')
MEM = f'{HOME}/.claude/projects/-Users-Shared-TorahSim/memory'
rows = [l.rstrip('\n').split('\t') for l in open(f'{SP}/ch12_timing.tsv', encoding='utf-8') if l.strip()]
start = int(rows[0][2]); steps = rows[1:]
TIMING = '; '.join(f'{name} {secs}s (at {hhmm})' for hhmm, name, secs, rc in steps)
# 1. THE STATE DOC — a new compaction block at the file's end
D = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = open(D, encoding='utf-8').read()
assert '═══ COMPACTION POINT #199' in s
DONE = '═══ COMPACTION POINT #200' in s   # the first run appended the block before the page's assert fell — never twice
BLOCK = ('═══ COMPACTION POINT #200 (2026-09-20 — INSIDE CHAPTER 12\'s READING, sitting 10 of THE DEUTERONOMY WALK, the first sitting under THE COST RULES A-B-C, on the owner\'s "Monitor how long each step takes and report when the chapter is done": '
 'the clean point at the 400k cap after the rows and the ledger — chapter 11\'s #198 precedent). THE STATE: the rereads done; ch12_dump0.py and ch12_measure1.py run (THE KIN FOUND BY COMPUTATION for the first time, beside the law kin named; the register\'s finder run on the chapter); '
 'THE INK ch12_ink.py green on its second pass (five forms fell on the first — the English\'s unopened "Dt.13:29)" at 179:2, 138:1\'s head citation, the "how?" gloss, the kin asserted before its computation, the by-gloss count sixty-nine; none a fact); THE DESIGN in the map ("Sitting 10 — CHAPTER 12 … THE DESIGN", lint 0); '
 'THE ROWS — the 159 spine rows of piskaot 59-81 (twenty heads and the three headless 68, 73, 74 folded in on their consonants) in six files, the 31 Onkelos rows in two, the seven outside rows in one, EVERY ROW READ WHOLE; THE LEDGER logic/oral_triage/deu_12_reeh_2026-09-20.md WRITTEN (197 sources — Onkelos 31: MATERIAL 30 / CONTEXT 1; the spine 159: MATERIAL 102 / CONTEXT 57; the outside 7: MATERIAL 6 / CONTEXT 1; coverage computed; lint 0; the writer\'s first run fell on fourteen cuts — the Name token, Jerusalem\'s defective spelling, "partition" without its yod, "common" with its vav, one cut moved — retyped from the FAIL print, the second run clean; 149,777 bytes). '
 'THE TIMING SO FAR (the owner\'s ask; ch12_timing.tsv): ' + TIMING + '; the sitting opened 17:34:53. NOT COMMITTED: the ledger, the map\'s design section, this block, the recovery page\'s line, the memory line — beside the twenty-one files uncommitted since bb62e90. '
 'NEXT (THE TAIL, on a small context after the compaction): ch12_patch_overrides.py derived from ch11_patch_overrides.py (69 by gloss, 124 by reference; the anchors sitting 9\'s last rows — "Deut.11.32:11": "today"), the ink rerun PATCHED; write_ch12_manifest.py (six claims DV12-01..06 at 12:1, 5, 13, 15, 20, 29 — the checks "you shall destroy" 12:2, "His dwelling" 12:5, "in one of" 12:14, "as the gazelle" 12:15, "I have commanded you" 12:21, "be ensnared" 12:30; the spine\'s rows by piska from the CITE INDEX); seat_ch12.py; ch12_chain.sh, ch12_fold.sh (225 -> 226, 2233 -> 2239, the hash unmoved), ch12_gates.sh LAUNCHED in the background with write_ch12_records.py and copy_ch12_forms.py written first; the summary read once; the records from the sheet; the forms; the commit message; the timing table and the report. '
 'IF THIS COMPACTS HERE: reread the recovery page, the map\'s "Sitting 10 — CHAPTER 12 … THE DESIGN", MEMORY.md — then the tail\'s first step, the display patch.\n')
assert not re.search(r'/Users/(?!Shared/)', BLOCK) and HOME not in BLOCK
if not DONE: open(D, 'a', encoding='utf-8').write('\n' + BLOCK)
# 2. THE RECOVERY PAGE — section 2 edited under its cap
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
t = open(P, encoding='utf-8').read()
old1 = '- SITTING 9 (chapter 11 read): the Sifrei back on the chapter, 210 sources whole; the rain conditional had NO CELL (paid at 9b).\n'
assert t.count(old1) == 1; t = t.replace(old1, '')
old2 = '2f4ec5b (the cache, 7b, 8, 8b, 9) pushed with it. NEXT: chapter 12\'s reading on his word.'
new2 = '2f4ec5b pushed with it.\n- SITTING 10 IN FLIGHT (ch 12 read, 197 sources whole, the ledger deu_12_reeh WRITTEN, uncommitted): NEXT THE TAIL — the display patch, the manifest, the seat, the chain launched, the records (the state doc #200).'
assert t.count(old2) == 1; t = t.replace(old2, new2)
old3 = '## 2. WHERE IT STANDS (2026-09-20, 9b done + the cost rules; the state doc #199 addendum 4 the newest)'
new3 = '## 2. WHERE IT STANDS (2026-09-20, sitting 10 in flight; the state doc #200 the newest)'
assert t.count(old3) == 1; t = t.replace(old3, new3)
old4 = 'the newest instances: the map\'s "Sitting 9" and "Sitting 8b")'
new4 = 'the newest instances: the map\'s "Sitting 10" and "Sitting 9b")'
assert t.count(old4) == 1; t = t.replace(old4, new4)
assert len(t.encode()) <= 10240, len(t.encode())
open(P, 'w', encoding='utf-8').write(t)
# 3. THE MEMORY INDEX LINE — under 17,000 bytes
M = f'{MEM}/MEMORY.md'
m = open(M, encoding='utf-8').read()
oldm = 'ch 1-11 COMPILED, PUSHED bb62e90; NEXT chapter 12\'s reading'
newm = 'ch 1-11 COMPILED, PUSHED bb62e90; ch 12 READ (sitting 10, the ledger written, uncommitted); NEXT THE TAIL — the patch, the manifest, the seat, the chain, the records'
assert m.count(oldm) == 1; m = m.replace(oldm, newm)
oldt = ' (a second history rewrite purged a copyrighted book; DATA_SOURCES.md; SETUP.md)'
assert m.count(oldt) == 1; m = m.replace(oldt, ' (DATA_SOURCES.md; SETUP.md)')
oldc = 'the bill is CONTEXT × CALLS + RE-WRITES (COST_AUDIT_2026-09-20.md); '
assert m.count(oldc) == 1; m = m.replace(oldc, '(COST_AUDIT_2026-09-20.md) ')
assert len(m.encode()) < 17000, len(m.encode())
open(M, 'w', encoding='utf-8').write(m)
print('state doc +', len(BLOCK.encode()), '| recovery page', len(t.encode()), '| MEMORY.md', len(m.encode()))
print(TIMING)
