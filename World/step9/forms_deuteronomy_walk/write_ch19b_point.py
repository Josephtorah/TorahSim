import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (LEAN): THE CLEAN COMPACTION POINT at RUN A's end — the state doc's #215, the recovery page (section 2 under its cap), the memory (the
# index line and the walk note) — written in ONE call after the design, the callees, the probe to FAIL, the exam and the types; every number READ FROM ITS PRINT
# (the recon's, the probes', the exam rows', the types', the callees', the map's own section, the exam file's own rows); every text built whole before a file is
# opened; the lints and the caps asserted. --check prints without writing. write_ch17b_point.py's form (RUN A's shape: no runner yet). RUN FROM THE REPO ROOT.
import os, re, sys, subprocess, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
rec_ = rd(f'{SP}/ch19_compile_recon.out'); pr = rd(f'{SP}/ch19_probes_fail.out'); ex = rd(f'{SP}/ch19_exam_rows.out'); ta = rd(f'{SP}/add_types_ch19_a.out'); tb = rd(f'{SP}/add_types_ch19_b.out'); ca = rd(f'{SP}/ch19_callees.out'); m = rd(MAP); exam = rd(f'{ROOT}/logic/oral_triage/deu_19_21_shoftim_ki_teitzei_exam_2026-09-25.md'); tsv = rd(f'{SP}/ch19b_timing.tsv')
RUN = R(r"^\d+: RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),", rec_, 'RUN'); assert RUN == '1349, 96, 88, 0, 12, 1709, 48, 319', RUN
PROBES = R(r'^readback_probes: (\d+/\d+)$', pr, 'the probes'); assert PROBES == '44/45', PROBES
assert "FAIL Q45" in pr and "ModuleNotFoundError: No module named 'cold_run_refuge_war_family'" in pr
NROWS, NCITE = R(r'^CITED AT LEAST TWICE: (\d+) \|', ex, 'the rows'), R(r'\| distinct citations: (\d+) \|', ex, 'the citations'); assert (NROWS, NCITE) == ('28', '56')
KA, KREG = R(r'^kinds: (\d+) added of \d+, registry (\d+)', ta, 'kinds'), R(r'^kinds: \d+ added of \d+, registry (\d+)', ta, 'kinds registry'); EA, EREG = R(r'^effects: (\d+) added \(registry (\d+)\)', ta, 'effects'), R(r'^effects: \d+ added \(registry (\d+)\)', ta, 'effects registry')
assert (KA, KREG, EA, EREG) == ('13', '1192', '45', '1170'), (KA, KREG, EA, EREG)
TYPES = R(r'^(THE TYPES DONE: kinds \d+, effects \d+, daemons \d+, functions blocks \d+, edges from refuge_war_family \d+, I5 \d+)', tb, 'types B'); assert TYPES == 'THE TYPES DONE: kinds 1192, effects 1170, daemons 78, functions blocks 72, edges from refuge_war_family 23, I5 78', TYPES
NFACT, NFAIL = len(re.findall(r'^FACT ', ca, re.M)), len(re.findall(r'^FAIL ', ca, re.M)); assert (NFACT, NFAIL) == (106, 2), (NFACT, NFAIL)
FAILS = re.findall(r'^FAIL ([\w.()]+):', ca, re.M)
i = m.rfind('## Sitting 16b — THE COMPILE OF CHAPTERS 19-21'); assert i > 0 and m.find('\n## ', i + 10) < 0, 'the design is the newest section'
DESIGN_BYTES = len(m[i:].encode())
EXAM_ROWS = len(re.findall(r'^- Mishnah [A-Za-z ]+ \d+:\d+ — LAW\.', exam, re.M)); EXAM_BYTES = len(exam.encode()); assert EXAM_ROWS == 28, EXAM_ROWS   # the rows, not the cite index's lines (the first check read 56 — both; the second lost the byte count to a comment)
NSTEPS = len([l for l in tsv.split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('16b ')]); SECS = sum(int(l.split('\t')[2]) for l in tsv.split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('16b '))
print('THE PRINTS: RUN (%s); the probes %s (Q45 FAIL); the exam rows %s of %s citations (the file %d rows, %d bytes); the types %s/%s kinds, %s/%s effects; %s; the callees %d facts, %d fails %s; the design %d bytes; %d steps, %d machine seconds' % (RUN, PROBES, NROWS, NCITE, EXAM_ROWS, EXAM_BYTES, KA, KREG, EA, EREG, TYPES, NFACT, NFAIL, FAILS, DESIGN_BYTES, NSTEPS, SECS))
# ---- #215 ----
sd = rd(SD); assert '\n#215 ' not in sd
P215 = ('\n\n#215 (2026-09-25, THE DEUTERONOMY WALK sitting 16b — CHAPTERS 19-21\'s COMPILE IN THE LEAN FORM, the lean pass\'s third compile sitting and the first over three chapters; on the owner\'s "Reread and go" after the compaction at #214 — no commit word said, the tree UNCOMMITTED since f730559 with sittings 15, 15b and 16 riding, and 16b opened on it; A CLEAN COMPACTION POINT AT RUN A\'S END, the two-run rule applied to a lean compile for the first time — RUN A: the lean recon over three chapters (ch19_compile_recon.py — the tape at RUN (%s, the four pairs, 127), the dispositions, the probes, the registries, the kin by static scan, the running world), THE TWENTY-EIGHT MISHNAH ROWS THE LEDGER CITES AT LEAST TWICE computed from the reading\'s ledger (%s distinct citations) and read WHOLE from the export, the design in the map ("Sitting 16b — THE COMPILE OF CHAPTERS 19-21 … LEAN", %d bytes — ONE runner cold_run_refuge_war_family.py over the three units, ONE daemon law_refuge_war_family, the span three ranges, THIRTEEN own-day lines one per claim, NINE cells and the readback\'s sixty-four rows, forty-five new effects, twenty-three CALL edges all reference, DJ1-DJ5, the receipt 20:17 to be dispositioned at the tail from the gates\' prints), the callees\' facts printed from twenty-three runners (%d facts, %d fails read — %s: the asks needing a case field, the runner passes it or asks another), the probe Q45 written to FAIL (readback_probes.py %s — ModuleNotFoundError until the runner exists), the lean exam file logic/oral_triage/deu_19_21_shoftim_ki_teitzei_exam_2026-09-25.md (%d rows read whole, the citing rows computed, no segment; %d bytes; lint 0), THE TYPES (add_types_ch19_a.py: %s kinds and %s effects, every `he` found in its verse — the registries %s kinds / %s effects; add_types_ch19_b.py: %s) — a departure from 15b\'s order, the types typed in RUN A so the runner\'s window is kept whole; %d steps, %d machine seconds; NO RUNNER YET, the tape UNMOVED at 15b\'s RUN; the tree UNCOMMITTED. NEXT: RUN B after the compaction — the tape tools and the shells derived from 15b\'s forms, the runner cold_run_refuge_war_family.py in parts (part 1 derived from the chapter 17-18 runner and ch19_ink.py; parts 2-5 typed: the nine cells, the readback\'s sixty-four rows and the DATA, the daemon, the thirteen lines, the narrative), the fast checker, the ask check, the cases generated, the first graded run, the dependency and daemon gates alone, the recorder (INK_CACHE=0), the stitcher, the literals DJ1-DJ5, the tape\'s first run, the scan census extended, the second run to 10/10, the clean point #216, THE GATES CHAIN LAUNCHED at RUN B\'s end; then THE TAIL (the summary read once, the demands and the receipt 20:17 filed from the prints, the records from the sheet in one call, the forms, the message); then the commit on his word ("Commit" = no push; "commit push" = both). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 16b — THE COMPILE OF CHAPTERS 19-21 … LEAN" — the design; THE ORDER paragraph names RUN B\'s steps), MEMORY.md; then this checkpoint.' % (RUN, NCITE, DESIGN_BYTES, NFACT, NFAIL, ', '.join(FAILS), PROBES, EXAM_ROWS, EXAM_BYTES, KA, EA, KREG, EREG, TYPES, NSTEPS, SECS))
# ---- the recovery page ----
rec = rd(REC)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
rec2 = sub1(rec, '## 2. WHERE IT STANDS (2026-09-24; #214 sitting 16 newest)', '## 2. WHERE IT STANDS (2026-09-25; #215 sitting 16b RUN A newest)', 'the header')
rec2 = sub1(rec2, "- NUMBERS CLOSED. DEUTERONOMY 1:1-18:22 ON THE TAPE (PUSHED through f730559 — 1-16); 17-18 compiled, 19-21 READ + FROZEN (uncommitted).", "- NUMBERS CLOSED. DEUTERONOMY 1:1-18:22 ON THE TAPE (PUSHED through f730559 — 1-16); 17-18 compiled, 19-21 READ + FROZEN, their compile DESIGNED + TYPED (uncommitted).", 'the tape line')
rec2 = sub1(rec2, '72 runners, 77 daemons; 1179 kinds / 1125 effects.', '72 runners, %s daemons; %s kinds / %s effects.' % (R(r'daemons (\d+),', TYPES, 'd'), KREG, EREG), 'the counts')
rec2 = sub1(rec2, "- SITTING 15/15b (ch 17-18, LEAN) at #212: 66/66; tape 10/10; chain green; UNCOMMITTED.", "- SITTINGS 15/15b (ch 17-18, LEAN): chain green; UNCOMMITTED.", 'the 15b line')
rec2 = sub1(rec2, "- SITTING 16 (ch 19-21 READ, LEAN, 3 units) DONE at #214: 335 sources; 13 claims; FROZEN; chain green; UNCOMMITTED. NEXT: the commit, then 16b (the compile).", "- SITTING 16 (ch 19-21 READ, LEAN) DONE at #214: 335 sources; 13 claims; chain green; UNCOMMITTED.\n- SITTING 16b RUN A (ch 19-21 COMPILE, LEAN) at #215: designed + typed (one runner refuge_war_family, 9 cells, 13 lines, 45 effects, 23 edges; Q45 FAIL %s; the exam %d rows); NO RUNNER YET. NEXT: RUN B (the runner, the tape, the chain LAUNCHED), the tail, the commit." % (PROBES, EXAM_ROWS), 'the sitting line')
rec2 = sub1(rec2, "## 5. THE SITTING SHAPES (the long forms: the addenda §5; the newest instances the map's \"Sitting 14\" and \"Sitting 14b\", lean)", "## 5. THE SITTING SHAPES (the long forms: the addenda §5)", 'section 5')
rec2 = sub1(rec2, "cold_run_<span>.py (65 runners)", "cold_run_<span>.py (72 runners)", 'the runners count')
rec2 = sub1(rec2, "B THE 600k CAP (his word 2026-09-20, from 400k) — a run ends", "B THE 600k CAP — a run ends", 'the cap clause')
rec2 = sub1(rec2, "; reviews/PORTABLE_repo_2026-09-15.md.", ".", 'the portable review pointer')
rec2 = sub1(rec2, "15b's chain green (sweep 71/71).", "15b's chain green.", 'the sweep count')
rec2 = sub1(rec2, "main-thread-checkpoint-2026-09-18.md; a relayed finding is never a ruling.", "main-thread-checkpoint-2026-09-18.md.", 'the peer clause (the standing law is in MEMORY.md)')
# ---- the memory ----
mm = rd(MM)
OLDL = '16 (ch 19-21 READ, lean, three units — two runs + the tail) DONE 2026-09-24 (335 sources, 13 claims; FROZEN; chain green), UNCOMMITTED; NEXT: the commit, then 16b (the compile of 19-21)'
NEWL = '16 (ch 19-21 READ, lean) DONE 2026-09-24 (335 sources, 13 claims; FROZEN; chain green); 16b RUN A 2026-09-25 (the compile DESIGNED + TYPED — one runner refuge_war_family, 13 lines, 45 effects; the probe Q45 to FAIL %s; the exam %d Mishnah rows; NO runner yet), UNCOMMITTED; NEXT: RUN B (the runner, the tape, the chain launched), the tail, then the commit' % (PROBES, EXAM_ROWS)
mm2 = sub1(mm, OLDL, NEWL, 'the walk line')
mw = rd(MW)
DESC_OLD = 'description: "SITTING 16 DONE 2026-09-24'
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 16b RUN A AT ITS CLEAN POINT 2026-09-25 (chapters 19-21\'s compile DESIGNED and TYPED lean — one runner refuge_war_family, thirteen lines, forty-five effects; the probe Q45 to FAIL; the exam twenty-eight Mishnah rows; no runner yet; UNCOMMITTED; NEXT RUN B then the tail then the commit) — SITTING 16 DONE 2026-09-24', 1)
NOTE = ('\n\nSITTING 16b RUN A AT ITS CLEAN POINT 2026-09-25 — CHAPTERS 19-21\'s COMPILE DESIGNED AND TYPED IN THE LEAN FORM (the third compile sitting of [[lean-pass-ruling]], the first over three chapters; THE TWO-RUN RULE applied to a lean compile for the first time): the recon over three chapters; THE TWENTY-EIGHT MISHNAH ROWS THE LEDGER CITES AT LEAST TWICE computed from the ledger and read whole (Makkot 1-2, Sotah 8-9, Sanhedrin 6 and 8, Bekhorot 8, Bava Batra 8, Parah 1 — the three in the spine\'s own Hebrew among them); the design (ONE runner cold_run_refuge_war_family.py over the three units, ONE daemon, the span three ranges, THIRTEEN own-day lines one per claim, NINE cells — the cities of refuge, the landmark and the witnesses, the priest\'s speech and the officers\' exemptions, the siege, the broken-necked heifer, the captive, the firstborn\'s double, the rebellious son, the hanged — the readback\'s sixty-four rows, forty-five new effects, twenty-three CALL edges all reference, DJ1-DJ5; the receipt 20:17 dispositioned at the tail from the gates\' prints); the callees\' facts from twenty-three runners (%d facts, %d fails read); the probe Q45 to FAIL (%s); the lean exam file (%d rows read whole, the citing rows computed, no segment); the types (%s kinds, %s effects; %s) — the types moved into RUN A so RUN B is the runner\'s window whole. NO RUNNER YET; the tape unmoved. UNCOMMITTED since f730559. NEXT: RUN B after a compaction — the runner in parts, the tape to 10/10, the chain LAUNCHED; then the tail; then the commit on his word.' % (NFACT, NFAIL, PROBES, EXAM_ROWS, KA, EA, TYPES))
mw2 = mw2.rstrip('\n') + NOTE + '\n'
# ---- the caps and the lints ----
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P215 + NOTE + NEWL), 'no Hebrew script in the new texts'
assert os.path.expanduser('~') not in (P215 + NOTE + NEWL + rec2) and SP not in (P215 + NOTE + NEWL + rec2)
print('THE POINT CHECKED: #215 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P215.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P215 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    for f in (SD, REC, MM, MW):
        out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #215, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
