#!/usr/bin/env python3
# THE LEAN PASS — OWNER-RULED 2026-09-23 ("Let's do this and make a note. At some point in the future we will complete these last chapters with a full process."):
# chapters 16-34 of Deuteronomy in the LEAN FORM to finish the book in about four days and study the architecture whole; THE FULL PROCESS OWED to these chapters later.
# The note made in the records the owner reads: the memory (a file + the index line), the state doc (#208), the recovery page, the map (the newest section), COMPILE_DEBT
# (the lean pass box), THE_STEPS, THE_BRIEFING; the chain's positions step set to four workers (item 4 of the plan). Every replacement asserted once; the caps asserted;
# the lint counts unmoved. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def W(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
def lint(p):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p if p.startswith('/') else f'{ROOT}/{p}'], capture_output=True, text=True); m = re.search(r'(\d+) flag', r.stdout + r.stderr); return int(m.group(1)) if m else None
RULING = ("THE LEAN PASS — OWNER-RULED 2026-09-23 (\"Let's do this and make a note. At some point in the future we will complete these last chapters with a full process.\"): "
          "chapters 16-34 (509 verses) in the LEAN FORM, to finish the book in about four days and study the architecture whole. THE FORM: (1) THE SHELF — the spine (the Sifrei on Deuteronomy) "
          "and Onkelos read WHOLE per verse (the whole-row rule stands); the Mishnah rows the answer sheet; the Talmud NOT read whole — a folio SEGMENT only when a Mishnah verdict is disputed and a cell "
          "needs it, read whole at the segment grain; no docket runs — the exam file lists the Mishnah rows and the segments read, coverage computed. (2) THE RECORDS per sitting FOUR — the map's "
          "AS BUILT (short: the departures and the lessons), the state doc's checkpoint, the recovery page, the memory — and the commit message; the other ten (COMPILE_DEBT's box, MIDDOT, "
          "MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the addenda) ONCE at the book's close. (3) THE GRAIN — eight sittings where the text is one unit: "
          "16; 17-18; 19-21; 22-25; 26-28; 29-31; 32; 33-34 (CHAPTER NUMBERS, as ruled); each sitting one reading window (the ink, the shelf, the ledger, the freeze) + one compile window (the design, "
          "the runner, the tape, the chain launched) + a short tail. (4) THE CHAIN in ONE pass — the dependency demands filed at the design, the positions step at FOUR workers inside the chain "
          "(POSARGS --jobs 4, set by this ruling). (5) THE EXAM — the Mishnah rows as cases; the Talmud's cases only for the segments read. WHAT STAYS: every verse from its spine; every law a cell "
          "with effects on the ledger; the tape's lines and markers; the gates green each sitting; a commit each sitting; Hebrew never without its English; the link review law; the cost rules "
          "(one run per phase, the clean point, the compaction, the reread). THE DEBT: chapters 16-34 ARE OWED THE FULL PROCESS LATER — the docket whole (every folio range read whole, the exam at its "
          "full size), the full records — recorded in COMPILE_DEBT's lean-pass box sitting by sitting. THE SCHEDULE (a target, not a law): day 1 — 16, then 17-18; day 2 — 19-21, then 22-25; "
          "day 3 — 26-28 (Leviticus 26's curses already a runner), then 29-31; day 4 — 32, then 33-34 and the book's close; chapters 27-34 narrative and poetry with new forms carry the risk.")
assert not re.search('[\\u0590-\\u05FF]', RULING) and '/Users/' not in RULING
before = {p: lint(p) for p in ('World/step9/DEUTERONOMY_WALK.md', 'World/step9/COMPILE_DEBT.md', 'THE_STEPS.md', 'THE_BRIEFING.md', 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', f'{MEM}/MEMORY.md')}
# ---- the memory: the file and the index ----
memf = f'{MEM}/lean-pass-ruling.md'   # written whole (a rerun rewrites the same text)
W(memf, '---\nname: lean-pass-ruling\ndescription: OWNER-RULED 2026-09-23 — Deuteronomy 16-34 in the LEAN FORM (core shelf, four records per sitting, eight sittings, one-pass chain); the full process owed to these chapters later\nmetadata:\n  type: feedback\n---\n\n' + RULING + '\n\n**Why:** the full process ran a chapter a day (chapter 15: seven context windows, the docket three of them); the owner needs the book finished to study the architecture whole and determine its purpose.\n\n**How to apply:** every sitting of 16-34 follows THE FORM above; name the sitting LEAN in its AS BUILT; keep the lean-pass box in COMPILE_DEBT current; never treat a lean sitting as the full process done. See [[deuteronomy-walk]], [[cost-rules-no-polling]], [[full-oral-torah-law]].\n')
idx = read(f'{MEM}/MEMORY.md')
if '[[lean-pass-ruling]]' in idx: print('the index already holds the ruling')
else:
  stale = "; then DEUTERONOMY (chapters 1-3, the reading); #184 the current tail (2026-09-16; NEXT: chapter 4's reading); NUMBERS' OPENING BLOCK"; assert idx.count(stale) == 1
  idx = idx.replace(stale, "; then DEUTERONOMY (the walk line); NUMBERS' OPENING BLOCK")
  stale2 = "(reviews/PORTABLE_repo_2026-09-15.md P1-P5; portable_pass.py 367 files; Data/fetch_shelf.py the shelf from Sefaria's bucket + --stores the 154 MB snapshot from the release stores-2026-09-15; Data/tanakh.sqlite tracked; SETUP.md; portable_probes.py 5/5; the sweep 57/57; the journal gate green)"; assert idx.count(stale2) == 1
  idx = idx.replace(stale2, "(reviews/PORTABLE_repo_2026-09-15.md holds the measurements; Data/fetch_shelf.py; SETUP.md)")
  old = "(13b: 91/91; 4 lines; 4 reuses; 27 params); NEXT: ch 16's reading"; assert idx.count(old) == 1
  idx = idx.replace(old, "(13b: 91/91); LEAN PASS RULED 2026-09-23 ([[lean-pass-ruling]]); NEXT: ch 16, lean")
  anchor = "- [⚠⚠ COST RULES](cost-rules-no-polling.md)"; assert idx.count(anchor) == 1
  idx = idx.replace(anchor, "- [⚠⚠ THE LEAN PASS](lean-pass-ruling.md) — RULED 2026-09-23: Deut 16-34 lean (core shelf, 4 records, 8 sittings, chain once); full process OWED later\n" + anchor)
  assert len(idx.encode('utf-8')) <= 17000, len(idx.encode('utf-8')); W(f'{MEM}/MEMORY.md', idx)
# ---- the state doc: #208 ----
D = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = read(D)
if '#208' not in s: W(D, s.rstrip('\n') + "\n\n#208 — THE LEAN PASS RULED (2026-09-23, after 13b's commit e824e52 and the push; the owner's plan question and the ruling \"Let's do this and make a note\"): " + RULING + " THE STATE: nothing mid-flight; the tree holds the commit's own records (the post-commit edits, this checkpoint, the map's lean-pass section, COMPILE_DEBT's box, THE_STEPS', THE_BRIEFING's entry, gates_chain.sh's POSARGS). NEXT ON HIS WORD (after a compaction: \"Reread\", then \"Go\"): CHAPTER 16's reading (16:1-22) IN THE LEAN FORM — the first sitting of the lean pass. POST-COMPACTION REREADS: the recovery page, the map's newest section (\"THE LEAN PASS\"), MEMORY.md; then this checkpoint.\n")
# ---- the recovery page ----
R = 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; r = read(R)
if 'THE LEAN PASS RULED' in r: print('the recovery page already holds the ruling')
else:
 old = "- 13b DONE, COMMITTED e824e52 AND PUSHED (#207 add. 5). NEXT ON HIS WORD: ch 16's reading (16:1-22), two runs + the tail."; assert r.count(old) == 1
 r = r.replace(old, "- 13b DONE, PUSHED e824e52. ⚠ THE LEAN PASS RULED (#208; the map's newest section): 16-34 in 8 lean sittings (16; 17-18; 19-21;\n  22-25; 26-28; 29-31; 32; 33-34) — core shelf, 4 records, chain once; full process OWED later. NEXT: ch 16's reading, LEAN.")
 old = "- SITTING 13 (ch 15 read, frozen): 132 sources; 7 claims. 13b: the docket 974 rows; RUN B DONE — release_firstborn 91/91 first\n  run; 4 lines, 15 writes (4 reuses), 27 parameters; the tape 10/10 on its 3rd run (CU5; the scan)."; assert r.count(old) == 1
 r = r.replace(old, "- SITTING 13/13b (ch 15 read, compiled): 132 sources; the docket 974 rows; release_firstborn 91/91; 4 lines, 15 writes (4 reuses), 27 parameters.")
 old = "## 2. WHERE IT STANDS (2026-09-23, 13b done; #207 add. 5 newest)"; assert r.count(old) == 1; r = r.replace(old, "## 2. WHERE IT STANDS (2026-09-23; #208 THE LEAN PASS newest)")
 assert len(r.encode('utf-8')) <= 10240, len(r.encode('utf-8')); W(R, r)
# ---- the map: the newest section ----
M = 'World/step9/DEUTERONOMY_WALK.md'; m = read(M)
if '## THE LEAN PASS' not in m: W(M, m.rstrip('\n') + "\n\n## THE LEAN PASS — CHAPTERS 16-34 IN THE LEAN FORM (OWNER-RULED 2026-09-23, after sitting 13b's commit e824e52; the state doc's #208; the memory's lean-pass-ruling)\n\n" + RULING + "\n\nTHE SITTINGS OF THE LEAN PASS are numbered on from 14 (14 — chapter 16; 15 — chapters 17-18; 16 — 19-21; 17 — 22-25; 18 — 26-28; 19 — 29-31; 20 — 32; 21 — 33-34), each with its compile sitting 14b … 21b, each AS BUILT headed LEAN. NEXT on the owner's word: sitting 14 — chapter 16's reading, lean.\n")
# ---- COMPILE_DEBT: the lean-pass box ----
C = 'World/step9/COMPILE_DEBT.md'; c = read(C)
if 'THE LEAN PASS BOX' not in c: W(C, c.rstrip('\n') + "\n\n## THE LEAN PASS BOX (OWNER-RULED 2026-09-23; DEUTERONOMY_WALK.md \"THE LEAN PASS\"; the state doc's #208) — CHAPTERS 16-34 COMPILED IN THE LEAN FORM ARE OWED THE FULL\n## PROCESS LATER: the docket whole (every folio range the union rule names, read whole; the exam at its full size — the Talmud's cases beside the Mishnah's), the full records\n## (the ten records per sitting the lean form defers), the register and readback census at the full grain. THE LEDGER OF THE LEAN SITTINGS (one line per sitting as it closes —\n## the chapters, the Mishnah rows read, the segments read, the cells, the runner's score, the commit): (none yet — sitting 14, chapter 16, next).\n")
# ---- THE_STEPS: a paragraph before Step 6 ----
S = 'THE_STEPS.md'; st = read(S); a = "\n## Step 6 — Publish\n"; assert st.count(a) == 1
if 'THE LEAN PASS' not in st: W(S, st.replace(a, "\n**THE LEAN PASS (ruled 2026-09-23):** Deuteronomy 16 to 34 are done in a lean form so the book can be finished in about four days and the whole architecture studied: every verse is still\nread from its spine with the Sifrei and Onkelos rows whole, every law still becomes a cell with effects on the ledger, the tape and the gates and the commit are unchanged — but the Talmud\nfolios are read only where a Mishnah verdict is disputed and a cell needs them, ten of the fourteen records wait for the book's close, the sittings take two or three chapters where the text\nis one unit, and the gates chain runs once. These chapters are owed the full process later; the debt is kept in COMPILE_DEBT.md's lean-pass box.\n" + a))
# ---- THE_BRIEFING: a bullet and an entry ----
B = 'THE_BRIEFING.md'; b = read(B)
if 'THE LEAN PASS' in b: print('the briefing already holds the ruling')
else:
 bul = [l for l in b.split('\n') if l.startswith('- **CHAPTER 15 COMPILED')]; assert len(bul) == 1
 ent = [l for l in b.split('\n') if l.startswith('### 2026-09-23 — CHAPTER 15 COMPILED')]; assert len(ent) == 1
 b = b.replace(bul[0], "- **THE LEAN PASS RULED — DEUTERONOMY 16 TO 34 IN A LEAN FORM TO FINISH THE BOOK IN ABOUT FOUR DAYS: THE SPINE STILL READ WHOLE, EVERY LAW STILL A CELL, THE TALMUD ONLY WHERE A VERDICT IS DISPUTED, FOUR RECORDS PER SITTING, EIGHT SITTINGS, THE CHAIN ONCE; THE FULL PROCESS OWED LATER (2026-09-23)** — after chapter 15's compile ran seven context windows for one chapter (the docket three of them), the owner ruled the lean form for the rest of the book so the architecture can be studied whole; COMPILE_DEBT.md keeps the debt.\n" + bul[0], 1)
 b = b.replace(ent[0], "### 2026-09-23 — THE LEAN PASS: THE LAST NINETEEN CHAPTERS IN A LEAN FORM, THE FULL PROCESS OWED\nChapter 15 cost seven context windows — three of them the docket, the Talmud's folio ranges read whole. At that rate the remaining 509 verses were nineteen days away. The owner ruled a\nlean form for chapters 16 to 34: every verse still read from its spine with the Sifrei and Onkelos whole, every law still a cell writing effects to the ledger, the tape, the gates and the\ncommit unchanged; but the Talmud read only where a Mishnah verdict is disputed and a cell needs it, ten of the fourteen records deferred to the book's close, the sittings two or three\nchapters where the text is one unit (16; 17-18; 19-21; 22-25; 26-28; 29-31; 32; 33-34), the gates chain once with the positions step at four workers. The purpose: finish the book, then study the\narchitecture whole and determine what it is for. The debt is written down: these chapters get the full process later.\n\n" + ent[0], 1)
 W(B, b)
# ---- gates_chain.sh: the positions step at four workers ----
G = 'World/step9/gates_chain.sh'; g = read(G); old = 'POSARGS="--jobs 8"; SWEEPARGS='
if g.count(old) == 1: W(G, g.replace(old, 'POSARGS="--jobs 4"; SWEEPARGS='))
g = read(G)
if 'THE LEAN PASS' not in g:
 old = "# --full forces the full sweep and the full loads (INK_CACHE=0 for every step; the positions table is always the whole measure)."; assert g.count(old) == 1
 W(G, g.replace(old, old + "\n# THE LEAN PASS (owner-ruled 2026-09-23; DEUTERONOMY_WALK.md \"THE LEAN PASS\"): the positions step at FOUR workers — eight were killed by the session's memory watchdog at 7b, 8b, 10b, 11b, 12b and 13b, and the table was measured by four outside the chain each time (477 s at 13b)."))
after = {p: lint(p) for p in before}
for p in before: print('  lint', p.replace(MEM, '<memory>').split('/')[-1], before[p], '->', after[p])
assert all(after[p] == before[p] for p in before), 'a record moved the gloss lint'
print('THE NOTE MADE: the memory (lean-pass-ruling.md + the index, %d bytes), the state doc #208, the recovery page (%d bytes), the map\'s newest section, COMPILE_DEBT\'s lean-pass box, THE_STEPS, THE_BRIEFING, gates_chain.sh POSARGS --jobs 4' % (len(idx.encode('utf-8')), len(r.encode('utf-8'))))
