#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7, RUN 2's close (2026-09-18): the checkpoint records — the map's RUN 2 paragraph, the state doc's #194
# addendum 1, the recovery page's two lines, the memory's index line and walk paragraph. Every text built whole before its file is opened; the caps
# asserted (the recovery page under 10,240 bytes, MEMORY.md under 17,000). Sitting 4's form (the run-2 checkpoint of chapter 6).
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
STATE = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
LEDGER = f'{ROOT}/logic/oral_triage/deu_07_vaetchanan_ekev_2026-09-17.md'
led = open(LEDGER, encoding='utf-8').read()
assert '**read: 29 of 29 — COMPLETE**' in led and led.count('⟨MISS⟩') == 0 and len(re.findall(r'^- Onkelos Deut 7:\d+ — ', led, re.M)) == 26 and len(re.findall(r'^- Sifrei Devarim \d+:\d+ — ', led, re.M)) == 3
NB = len(led.encode())
MAT_O = len(re.findall(r'^- Onkelos Deut 7:\d+ — MATERIAL', led, re.M)); CTX_O = len(re.findall(r'^- Onkelos Deut 7:\d+ — CONTEXT', led, re.M))
MAT_S = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — MATERIAL', led, re.M)); CTX_S = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — CONTEXT', led, re.M))
assert (MAT_O, CTX_O, MAT_S, CTX_S) == (19, 7, 2, 1), (MAT_O, CTX_O, MAT_S, CTX_S)

# ---- 1. THE MAP: RUN 2 — AS RUN, after the design's THE ORDER paragraph, before THE INSTALL HYPOTHESIS ----
RUN2 = (f'RUN 2 — AS RUN (2026-09-18, on "go for run 2" after the compaction): the rereads (the recovery page, the map\'s two newest sections, the memory; then THE_STEPS\' compiler block,\n'
        f'Step 2 and Step 5\'s head); the three outside rows and the twenty-six Onkelos rows read WHOLE again from the run-1 prints (ch7_sifrei_outside.txt, ch7_onkelos.txt — the\n'
        f'compaction had emptied them from the window; the whole-row rule); three row scripts and the ledger writer on sitting 4\'s forms with the spine sections dropped (chapter 4\'s\n'
        f'shape on chapter 6\'s form — no CREDITED spine rows, no piska loop); the ledger {os.path.relpath(LEDGER, ROOT)} — 29 sources (Onkelos 26: MATERIAL {MAT_O} / CONTEXT {CTX_O};\n'
        f'the outside rows 3: MATERIAL {MAT_S} / CONTEXT {CTX_S}, 37:1 marked an INTERPOLATION in its own line), coverage computed (missing 0, extra 0; the spine\'s 0 rows on the chapter said\n'
        f'and why), lint 0, NO CUT MISSED on the first run ({NB:,} bytes); the kin\'s spine CREDITED BY NAME in its own section with the counts computed from those ledgers (the angel\'s\n'
        f'clauses 8 Onkelos rows, the renewed covenant 7, the dispossession 7, the erection docket\'s Mishnah Avodah Zarah 3:5 on 7:25; the Mekhilta rows 21) — not this ledger\'s sources,\n'
        f'not in its cite index. ⚠ LESSONS (run 2): A CHAPTER WITHOUT A SPINE HAS A LEDGER WITHOUT A SPINE SECTION — the form drops the spine\'s loop, the credits dict and the\n'
        f'divergence check whole, and the coverage line says "0 rows" with the heads computed, never a blank. THE OUTSIDE ROWS ARE THE SPINE\'S WHOLE VOICE — three rows, one the\n'
        f'translator\'s own: 50:4 reads 7:1\'s count (each of the seven greater than all Israel) and 61:7 reads 7:26\'s doubled verbs as the rule of RENAMING the shrines for the worse — the\n'
        f'shelf\'s two moves on the chapter both by E10, the repetition made to teach. A SINGULAR AND A PLURAL "THAN YOU" — the ink\'s phrase census had the singular\'s three seats (4:38,\n'
        f'7:1, 9:1); the shelf\'s 50:4 puts 11:23\'s PLURAL beside 7:1\'s singular, and the plural\'s one seat was computed at the write (a census by spelling splits what the shelf joins by\n'
        f'sense — the row names the seat). THE ORDER (RUN 3, the first step): write_ch7_overrides.py — the display-layer patch (49 by gloss, 36 by reference) under the sitting\'s marker\n'
        f'"THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)", the ink rerun PATCHED; then the manifest (six claims DV07-01..06, each check the block\'s longest store-piece\n'
        f'whole — 7:9\'s "His commandments" not a check), the seat (six WITNESS_READ operators at 7:1, 6, 9, 12, 17, 25, step E), the chain (the ritual), the fold (221 / 2209 / the hash\n'
        f'unmoved), build_world, the journal gate, the register gate --strict (no seat), the home-path gate → the checkpoint (#194 addendum 2, a clean point).\n')
m = open(MAP, encoding='utf-8').read()
ANCHOR = '→ the state doc\'s checkpoint (RUN 2\'s close, a clean point).\n\n## THE INSTALL HYPOTHESIS'
assert m.count(ANCHOR) == 1 and 'RUN 2 — AS RUN (2026-09-18' not in m
m2 = m.replace(ANCHOR, '→ the state doc\'s checkpoint (RUN 2\'s close, a clean point).\n\n' + RUN2 + '\n## THE INSTALL HYPOTHESIS')

# ---- 2. THE STATE DOC: #194 addendum 1 ----
ADD = (f'\n#194 ADDENDUM 1 (2026-09-18, at the close of THE DEUTERONOMY WALK sitting 5 — CHAPTER 7\'s READING, RUN 2 of four — A CLEAN COMPACTION POINT): on the owner\'s\n'
       f'"go for run 2" after the compaction: the rereads (the three files; THE_STEPS\' compiler block, Step 2, Step 5\'s head), the three outside rows and the twenty-six Onkelos rows\n'
       f'read WHOLE (ch7_sifrei_outside.txt, ch7_onkelos.txt), ch7_rows_onkelos_a.py (7:1-13), ch7_rows_onkelos_b.py (7:14-26), ch7_rows_outside.py (37:1, 50:4, 61:7) and\n'
       f'write_ch7_ledger.py on sitting 4\'s forms (the spine sections dropped — no piska on the chapter); THE LEDGER {os.path.relpath(LEDGER, ROOT)} WRITTEN — 29 sources\n'
       f'(Onkelos 26: MATERIAL {MAT_O} / CONTEXT {CTX_O}; the Sifrei\'s three outside rows: MATERIAL {MAT_S} / CONTEXT {CTX_S}, 37:1 an INTERPOLATION marked), coverage computed (missing 0, extra 0;\n'
       f'the spine 0 rows on the chapter, the heads computed), lint 0, no cut missed, {NB:,} bytes; the kin\'s spine credited by name in its own section (the counts computed: 8, 7, 7\n'
       f'Onkelos rows and the erection docket\'s Mishnah Avodah Zarah 3:5; the Mekhilta 21); the home-path gate GREEN. The map\'s "RUN 2 — AS RUN" paragraph is the record (three\n'
       f'lessons: a chapter without a spine has a ledger without a spine section; the outside rows are the spine\'s whole voice — 50:4 the count, 61:7 the renaming; a singular and a\n'
       f'plural "than you" split by the census, joined by the shelf). THE STATE otherwise as #194: the corpus unmoved (220 units, standing 2203, hash 8b8fff1fa28953af — the draft\n'
       f'deu_07_nations_cherem not yet frozen), the tape unmoved since 4b, no gate of the engine run (nothing of the engine touched). THE TREE (uncommitted since 64a8362): #194\'s\n'
       f'list + the ledger, the map\'s RUN 2 paragraph, this addendum, the recovery page\'s two lines, the memory. ⚠ THE SCRATCHPAD adds run 2\'s scripts to run 1\'s (copied at run 4):\n'
       f'ch7_rows_onkelos_a.py, ch7_rows_onkelos_b.py, ch7_rows_outside.py, write_ch7_ledger.py, write_ch7_run2.py. THE WORD FOR THE NEXT SITTING — RUN 3 ON THE OWNER\'S WORD,\n'
       f'its first step: write_ch7_overrides.py from the forms\' write_ch6_overrides.py by sed — the display-layer patch (OVERRIDE_GLOSS 49, OVERRIDE_REF 36 from ch7_ink.py, ALREADY\n'
       f'six left standing) under the marker "THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)", then ch7_ink.py rerun with PATCHED true (0 failing); then\n'
       f'write_ch7_manifest.py (six claims DV07-01..06 at 7:1-5, 6-8, 9-11, 12-16, 17-24, 25-26; the checks the blocks\' longest store-pieces whole — never 7:9\'s "His commandments"),\n'
       f'the seat (six WITNESS_READ operators at 7:1, 6, 9, 12, 17, 25, step E), the chain (verify_claims, the labels census, verify_text, the ritual), the fold predicted and matched\n'
       f'(221 units, standing 2209, hash 8b8fff1fa28953af unmoved — the tripwire\'s literals set before the bake), `python3 World/build_world.py`, the journal gate, the register gate\n'
       f'--strict (DECLARED 100 unmoved), the home-path gate → the checkpoint (#194 addendum 2, RUN 3\'s close). Run 4: the records from the sheet in one call, the forms copied, the\n'
       f'map\'s AS BUILT, the commit message for his word. IF THIS COMPACTS HERE: reread the recovery page, the map\'s "Sitting 5 — CHAPTER 7 … THE DESIGN" (the design and its\n'
       f'"RUN 2 — AS RUN" paragraph — THE ORDER (RUN 3) names the step) and "THE INSTALL HYPOTHESIS", MEMORY.md; nothing is mid-flight.\n')
s = open(STATE, encoding='utf-8').read()
assert s.rstrip().endswith('THE_STEPS\' three blocks at run 2\'s first step.') and '#194 ADDENDUM 1' not in s
s2 = s.rstrip('\n') + '\n' + ADD

# ---- 3. THE RECOVERY PAGE: §2's two lines ----
r = open(REC, encoding='utf-8').read()
OLD_A = ('- IN FLIGHT: SITTING 5 — CHAPTER 7\'s reading (7:1-26): RUN 1 DONE (the measurements, the ink 119/0, the design in the map); NEXT: RUN 2 the rows\n'
         '  WHOLE and the ledger. ON THE TABLE, not rulings: the Decalogue-schema question; THE INSTALL HYPOTHESIS (the map\'s tail).\n')
NEW_A = ('- IN FLIGHT: SITTING 5 — CHAPTER 7\'s reading (7:1-26): RUNS 1-2 DONE (the ink 119/0, the design; the ledger 29 sources, lint 0); NEXT: RUN 3 the\n'
         '  display layer, the manifest, the seat, the fold, the gates. ON THE TABLE, not rulings: the Decalogue-schema question; THE INSTALL HYPOTHESIS (the map\'s tail).\n')
OLD_B = '- Uncommitted since 64a8362: run 1\'s records, the tutorial ARCHITECTURE/DEUTERONOMY_SO_FAR.md (+ epub).\n'
NEW_B = '- Uncommitted since 64a8362: runs 1-2\'s records, the ledger, the tutorial ARCHITECTURE/DEUTERONOMY_SO_FAR.md (+ epub).\n'
assert r.count(OLD_A) == 1 and r.count(OLD_B) == 1
r2 = r.replace(OLD_A, NEW_A).replace(OLD_B, NEW_B)
assert len(r2.encode()) < 10240, len(r2.encode())

# ---- 4. THE MEMORY: the index line and the walk file ----
mi = open(f'{MEM}/MEMORY.md', encoding='utf-8').read()
OLD_I = 'SITTING 5 (ch 7) RUN 1 DONE 2026-09-18; the INSTALL hypothesis ON THE TABLE; NEXT: RUN 2 the rows, the ledger'
NEW_I = 'SITTING 5 (ch 7) RUNS 1-2 DONE 2026-09-18; the INSTALL hypothesis ON THE TABLE; NEXT: RUN 3 the seat, the fold'
assert mi.count(OLD_I) == 1
mi2 = mi.replace(OLD_I, NEW_I)
assert len(mi2.encode()) < 17000, len(mi2.encode())
dw = open(f'{MEM}/deuteronomy-walk.md', encoding='utf-8').read()
OLD_D = 'SITTING 5 (chapter 7) RUN 1 DONE 2026-09-18'
NEW_D = 'SITTING 5 (chapter 7) RUNS 1-2 DONE 2026-09-18'
assert dw.count(OLD_D) == 1
lines = dw.split('\n')

idx = [k for k, l in enumerate(lines) if l.startswith('SITTING 5 — CHAPTER 7 (7:1-26')]
assert len(idx) == 1
L = lines[idx[0]]
j = L.index('NEXT: RUN 2 — ')
NEW_TAIL = (f'RUN 2 DONE 2026-09-18 on "go for run 2" (the rereads; the three outside rows and the twenty-six Onkelos rows WHOLE; ch7_rows_onkelos_a/b.py, ch7_rows_outside.py, '
            f'write_ch7_ledger.py on sitting 4\'s forms with the spine sections dropped; the ledger {os.path.relpath(LEDGER, ROOT)} — 29 sources, Onkelos MATERIAL {MAT_O} / CONTEXT {CTX_O}, '
            f'the outside rows MATERIAL {MAT_S} / CONTEXT {CTX_S} with 37:1 an interpolation, coverage computed, lint 0, no cut missed; the kin\'s spine credited by name with the counts computed; '
            f'the state doc #194 addendum 1 — a clean compaction point; the map\'s "RUN 2 — AS RUN" the record and its three lessons). NEXT: RUN 3 — write_ch7_overrides.py (49 by gloss, 36 by '
            f'reference, the marker "THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)"), the ink rerun PATCHED, the manifest (DV07-01..06), the seat (7:1, 6, 9, 12, 17, 25 step E), '
            f'the chain, the fold (221 / 2209 / the hash unmoved), build_world, the journal gate, the register gate --strict, the home-path gate; then RUN 4 the records, the forms, the commit message for his word.')
lines[idx[0]] = L[:j] + NEW_TAIL
dw2 = '\n'.join(lines).replace(OLD_D, NEW_D)

for path, txt in ((MAP, m2), (STATE, s2), (REC, r2), (f'{MEM}/MEMORY.md', mi2), (f'{MEM}/deuteronomy-walk.md', dw2)):
    open(path + '.tmp', 'w', encoding='utf-8').write(txt); os.replace(path + '.tmp', path)
    print(f'wrote {path.replace(ROOT, "<repo>").replace(MEM, "<memory>")}: {len(txt.encode()):,} bytes')
