#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7, RUN 3's close (2026-09-18): the checkpoint records — the map's RUN 3 paragraph, the state doc's #194
# addendum 2, the recovery page's three lines, the memory's index line and walk paragraph. THE COUNTS READ FROM THE PRINTS (ch7_fold_check1.out,
# ch7_truth.out, ch7_build.out, ch7_journal.out, ch7_register.out, ch7_ritual_*.out, ch7_vc.out, ch7_labels.out, ch7_vt_*.out, ch7_chain.log,
# ch7_ink_run3.out, the override file, the unit), never typed. Every text built whole before its file is opened; the caps asserted.
# Sitting 4's form (write_ch6_run3.py's shape on the reading's run 3).
import os, re, subprocess, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory'); SP = os.path.dirname(os.path.abspath(__file__))
FORMS = f'{ROOT}/World/step9/forms_deuteronomy_walk'
def rd(p): return open(p, encoding='utf-8').read()
UID = 'deu_07_nations_cherem'
fold1 = rd(f'{SP}/ch7_fold_check1.out'); truth = rd(f'{SP}/ch7_truth.out'); build = rd(f'{SP}/ch7_build.out'); jn = rd(f'{SP}/ch7_journal.out'); reg = rd(f'{SP}/ch7_register.out')
rit = rd(f'{SP}/ch7_ritual_{UID}.out'); vc = rd(f'{SP}/ch7_vc.out'); lab = rd(f'{SP}/ch7_labels.out'); vt = rd(f'{SP}/ch7_vt_{UID}.out'); chain = rd(f'{SP}/ch7_chain.log'); ink3 = rd(f'{SP}/ch7_ink_run3.out')
m = re.search(r'CORPUS TRUTH GREEN — one world, (\d+) units, (\d+) facts, (\d+) demands \((\d+) open\), hash ([0-9a-f]+)', fold1); UN, FA, DE, OP, HASH = m.groups()
m2 = re.search(r'CORPUS TRUTH GREEN — one world, (\d+) units, (\d+) facts, (\d+) demands \((\d+) open\), hash ([0-9a-f]+)', truth); assert m2.groups() == (UN, FA, DE, OP, HASH), (m.groups(), m2.groups())
assert (UN, FA, DE, HASH) == ('221', '1809', '341', '8b8fff1fa28953af'), (UN, FA, DE, HASH)
tr = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); ST = re.search(r'assert len\(W\["standing"\]\) == (\d+)\n', tr).group(1); assert ST == '2209' and f'assert len(W["units"]) == {UN}\n' in tr
assert 'ALL GREEN — the one database agrees with the fold' in build
JK, JR = re.search(r'THE FOLD LAYER: (\d+) kinds, (\d+) rows in the index MATCHING the header', jn).groups(); assert 'GATE GREEN' in jn and JK == '12'
JR6 = re.search(r'THE FOLD LAYER: 12 kinds, (\d+) rows in the index', rd(f'{FORMS}/ch6_journal.out')).group(1); DJ = int(JR) - int(JR6)
assert 'THE REGISTER GATE: GREEN' in reg and re.search(r'^DECLARED 100; DEBT 0; FAILS 0', reg, re.M)
NP = len(re.findall(r'^PASS', rit, re.M)); assert f'RITUAL COMPLETE for {UID} ({UN} frozen units)' in rit and not re.search(r'^FAIL', rit, re.M), NP
assert re.search(r'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check', vc) and 'GATE PASSED (0 failure line(s))' in lab
LN, LL, LD = re.search(r'num\s+(\d+) claims\s+labeled\s+(\d+)\s+debt\s+(\d+)', lab).groups(); assert LN == LL and LD == '0'
assert 'TEXT LAYER GREEN: 26 steps, 7 scenarios' in vt and 'seated 6 operators on 6 steps [1, 6, 9, 12, 17, 25]; scenarios 7 in the anchor form' in chain and 'ALL_DONE' in chain
assert ink3.strip().endswith('0 failing statements')
ov = yaml.safe_load(open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8')); NREF = len(ov['by_ref']); NGL = len(ov['by_gloss'])
D7 = sum(1 for k in ov['by_ref'] if k.startswith('Deut.7.')); assert D7 == 36
ut = rd(f'{ROOT}/logic/units/{UID}.yaml'); assert '  status: frozen' in ut and ut.count('      - op: WITNESS_READ') == 6 and '[claim DV07-06]' in ut
assert os.path.exists(f'{ROOT}/logic/py_units/{UID}.py') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json')
DATE = '2026-09-18'

RUN3 = (f'RUN 3 — AS RUN ({DATE}, on "run 3 go" after run 2): the display layer patched (49 by gloss, 36 by reference; by_ref {NREF}, by_gloss {NGL} — the anchors the last rows of\n'
        f'sitting 4\'s two blocks), the ink rerun PATCHED with 0 failing; the manifest\'s six claims with every CITE INDEX name used (29), verify_claims 6/0, the labels census GREEN\n'
        f'({LN} claims labeled, debt 0); six WITNESS_READ seats at 7:1, 6, 9, 12, 17, 25, step E, seven anchor scenarios (the tree-derived thirty-three rewritten), verify_text GREEN\n'
        f'(26 steps, 7 scenarios); the ritual {NP} PASS — the {UN}st frozen unit and its Python layer; the fold predicted and matched ({UN} units, standing {ST}, hash {HASH}; {FA} facts,\n'
        f'{DE} demands, {OP} open) before and after the bake; build_world ALL GREEN; the journal gate GREEN ({JK} kinds, {JR} rows — {JR6} + {DJ}, the fold layer\'s rows for the new unit; the\n'
        f'tape unmoved); the register gate --strict GREEN (DECLARED 100, DEBT 0, FAILS 0 — no seat in the chapter, as designed); the home-path gate GREEN. ⚠ LESSONS (run 3):\n'
        f'THE FORMS HELD FIRST TIME — five scripts derived from sitting 4\'s by name changes alone (the patch\'s anchors the prior sitting\'s last rows; the manifest\'s checks cut\n'
        f'from the store\'s bytes, 7:9\'s placed on "the faithful" BEFORE the store\'s extra token so the written/read pair stays out of every check; the seat\'s anchors the claims\'\n'
        f'first verses), none retyped: a reading\'s run 3 is a form, not a design. THE FOLD LAYER GROWS WITH A FREEZE WHILE THE TAPE STANDS — the journal\'s index +{DJ} rows on the\n'
        f'{UN}st unit with no line added to the tape; the gate re-pins the header to the unmoved hash. THE ORDER (RUN 4, the first step): the sheet RECORD_FORMS.md read,\n'
        f'write_ch7_records.py from write_ch6_records.py by sed → the records in one call (this section\'s AS BUILT, COMPILE_DEBT\'s sitting-5 box — 5b\'s owed list, MIDDOT\n'
        f'(E10 twice on the chapter: 50:4, 61:7), MISHNAH_TOPICS (the testing shelf routed — Avodah Zarah, Kiddushin 3:12, Makkot), RESEARCH_LOG (the reading\'s entry — the\n'
        f'flock\'s word tagged a name in the morph; the written/read pair at 7:9; the spine silent), THE_STEPS, THE_BRIEFING (the scoreboard {UN} units / standing {ST} + an entry),\n'
        f'THE_WORLD, RESUME, the stamp row, the recovery page whole, the memory, copy_ch7_forms.py) → the lints → #194 addendum 3 (the sitting\'s close) → the commit\n'
        f'message drafted for the owner\'s word.\n')
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; m_ = rd(MAP)
ANCHOR = '→ the checkpoint (#194 addendum 2, a clean point).\n\n## THE INSTALL HYPOTHESIS'
assert m_.count(ANCHOR) == 1 and 'RUN 3 — AS RUN (2026-09-18' not in m_
m2_ = m_.replace(ANCHOR, '→ the checkpoint (#194 addendum 2, a clean point).\n\n' + RUN3 + '\n## THE INSTALL HYPOTHESIS')

ADD = (f'\n#194 ADDENDUM 2 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 5 — CHAPTER 7\'s READING, RUN 3 of four — A CLEAN COMPACTION POINT): on the owner\'s\n'
       f'"run 3 go": ch7_patch_overrides.py (the display layer — 49 by gloss, 36 by reference under the marker "THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)";\n'
       f'by_ref {NREF}, by_gloss {NGL}), ch7_ink.py rerun PATCHED — 0 failing (ch7_ink_run3.out); write_ch7_manifest.py — logic/oral_audit/manifests/{UID}_claims.json, six claims\n'
       f'DV07-01..06 (7:1-5, 6-8, 9-11, 12-16, 17-24, 25-26), every CITE INDEX name used, verify_claims 6 verified / 0 failed, claim_labels_census --strict GATE PASSED ({LN} labeled,\n'
       f'debt 0); seat_ch7.py — six WITNESS_READ operators at 7:1, 6, 9, 12, 17, 25, step E, the scenarios in the anchor form (7); verify_text GREEN (26 steps, 7 scenarios);\n'
       f'freeze_ritual {NP} PASS — {UID} FROZEN, the {UN}st unit, logic/py_units/{UID}.py; ch7_fold.sh — the tripwire set to the prediction (units 220 → {UN}, standing 2203 →\n'
       f'{ST}, the hash unmoved), CORPUS TRUTH GREEN before the bake and after ({UN} units, {FA} facts, {DE} demands, {OP} open, hash {HASH}); build_world ALL GREEN; the journal\n'
       f'gate GREEN ({JK} kinds, {JR} rows — +{DJ} on the fold layer, the tape unmoved); the register gate --strict GREEN (DECLARED 100, DEBT 0, FAILS 0); the home-path gate GREEN.\n'
       f'The map\'s "RUN 3 — AS RUN" paragraph is the record (two lessons: the forms held first time — a reading\'s run 3 is a form; the fold layer grows with a freeze while the\n'
       f'tape stands). THE STATE: {UN} frozen units, standing {ST}, hash {HASH}; the tape unmoved since 4b (RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127),\n'
       f'markers 167, closes 127); 61 runners, 66 daemons, 454 functions; the registries 1125 / 1025. THE TREE (uncommitted since 64a8362): #194\'s and addendum 1\'s lists +\n'
       f'logic/units/{UID}.yaml (frozen), logic/py_units/{UID}.py (new), the manifest (new), logic/glosses/word_gloss_overrides.yaml (the two blocks), logic/corpus/CORPUS_TRUTH.py\n'
       f'and corpus_world.sqlite (the bake), the map\'s RUN 3 paragraph, this addendum, the recovery page, the memory; World/journal/data/ regenerated (gitignored). ALSO IN THE\n'
       f'TREE, from the design thread on the owner\'s word (its message of this date; not this thread\'s work, nothing of it touched here): ARCHITECTURE/THE_BOOKS_AS_A_PROGRAM.md\n'
       f'(new) and ARCHITECTURE/README.md (a section "The discussion documents") — ARCHITECTURE rides every commit. ⚠ THE SCRATCHPAD adds run 3\'s scripts and prints (copied\n'
       f'at run 4): ch7_patch_overrides.py, ch7_ink_run3.out, write_ch7_manifest.py, ch7_vc.out, ch7_labels.out, seat_ch7.py, ch7_chain.sh, ch7_chain.log, ch7_vt_{UID}.out,\n'
       f'ch7_ritual_{UID}.out, ch7_fold.sh, ch7_fold_check1.out, ch7_bake.out, ch7_truth.out, ch7_build.out, ch7_journal.out, ch7_register.out, write_ch7_run3.py.\n'
       f'THE WORD FOR THE NEXT SITTING — RUN 4 ON THE OWNER\'S WORD, its first step: the sheet World/step9/RECORD_FORMS.md read; write_ch7_records.py from the forms\'\n'
       f'write_ch6_records.py by sed (the counts from the prints — never typed) → the records in ONE call: the map\'s "Sitting 5 — CHAPTER 7 — AS BUILT" (the design stands;\n'
       f'the departures named; the lessons of runs 1-3 gathered), COMPILE_DEBT\'s sitting-5 box (5b\'s owed list from the design\'s OWED TO THE COMPILE), MOVE_CATALOG checked,\n'
       f'MIDDOT (E10 at 50:4 and 61:7), MISHNAH_TOPICS (the routed tractates), RESEARCH_LOG (the reading\'s entry), THE_STEPS, THE_BRIEFING (the scoreboard {UN} / {ST} + the\n'
       f'entry), THE_WORLD, World/RESUME.md, the stamp row, the state doc\'s addendum 3, the recovery page REWRITTEN whole, the addenda\'s section 41, the memory; copy_ch7_forms.py\n'
       f'(copy_ch6b_forms.py the form — every scratchpad script and print named in the three TREE lists); the lints at their baselines; the commit message for his word\n'
       f'(64a8362\'s form) — NO commit without it, no push without "push". IF THIS COMPACTS HERE: reread the recovery page, the map\'s "Sitting 5 — CHAPTER 7 … THE DESIGN" (the\n'
       f'design with its "RUN 2 — AS RUN" and "RUN 3 — AS RUN" paragraphs — THE ORDER (RUN 4) names the step) and "THE INSTALL HYPOTHESIS", MEMORY.md; nothing is mid-flight.\n')
STATE = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(STATE)
assert '#194 ADDENDUM 1' in s and '#194 ADDENDUM 2' not in s
s2 = s.rstrip('\n') + '\n' + ADD

REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; r = rd(REC)
SUBS = [('- 220 frozen units, standing 2203, hash 8b8fff1fa28953af.', f'- {UN} frozen units, standing {ST}, hash {HASH}.'),
        ('- IN FLIGHT: SITTING 5 — CHAPTER 7\'s reading (7:1-26): RUNS 1-2 DONE (the ink 119/0, the design; the ledger 29 sources, lint 0); NEXT: RUN 3 the\n  display layer, the manifest, the seat, the fold, the gates.',
         f'- IN FLIGHT: SITTING 5 — CHAPTER 7\'s reading (7:1-26): RUNS 1-3 DONE (the ledger 29 sources; the {UN}st unit frozen; the fold matched; gates GREEN);\n  NEXT: RUN 4 the records from the sheet, the forms, the commit message.'),
        ('- Uncommitted since 64a8362: runs 1-2\'s records, the ledger, the tutorial ARCHITECTURE/DEUTERONOMY_SO_FAR.md (+ epub).',
         '- Uncommitted since 64a8362: runs 1-3\'s records, the ledger, the unit, the tutorial (+ epub), the design thread\'s two ARCHITECTURE files.')]
for a, b in SUBS: assert r.count(a) == 1, a[:60]; r = r.replace(a, b)
assert len(r.encode()) < 10240, len(r.encode())

MI = f'{MEM}/MEMORY.md'; mi = rd(MI)
a, b = 'SITTING 5 (ch 7) RUNS 1-2 DONE 2026-09-18; the INSTALL hypothesis ON THE TABLE; NEXT: RUN 3 the seat, the fold', 'SITTING 5 (ch 7) RUNS 1-3 DONE 2026-09-18; the INSTALL hypothesis ON THE TABLE; NEXT: RUN 4 records, forms'
assert mi.count(a) == 1; mi2 = mi.replace(a, b); assert len(mi2.encode()) < 17000, len(mi2.encode())
DW = f'{MEM}/deuteronomy-walk.md'; dw = rd(DW)
a = 'SITTING 5 (chapter 7) RUNS 1-2 DONE 2026-09-18'; assert dw.count(a) == 1; dw = dw.replace(a, 'SITTING 5 (chapter 7) RUNS 1-3 DONE 2026-09-18')
lines = dw.split('\n'); idx = [k for k, l in enumerate(lines) if l.startswith('SITTING 5 — CHAPTER 7 (7:1-26')]; assert len(idx) == 1
L = lines[idx[0]]; j = L.index('NEXT: RUN 3 — '); assert j > 0
TAIL = (f'RUN 3 DONE {DATE} on "run 3 go" (the display layer patched — 49 by gloss, 36 by reference; the ink rerun 0 failing; the manifest\'s six claims DV07-01..06 verified 6/0, the '
        f'labels census green; six WITNESS_READ seats at 7:1, 6, 9, 12, 17, 25 step E; verify_text green; the ritual {NP} PASS — {UID} the {UN}st frozen unit; the fold predicted and '
        f'matched ({UN} / {ST} / hash unmoved); build_world, the journal gate (+{DJ} rows on the fold layer), the register gate --strict and the home gate GREEN; the state doc #194 '
        f'addendum 2 — a clean compaction point; the map\'s "RUN 3 — AS RUN" the record, two lessons). NEXT: RUN 4 — the sheet RECORD_FORMS.md, write_ch7_records.py from '
        f'write_ch6_records.py (the records in one call: the AS BUILT, COMPILE_DEBT\'s 5 box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_WORLD, RESUME, the '
        f'stamp row, the recovery page whole, the addenda §41, the memory), copy_ch7_forms.py, the lints, #194 addendum 3, the commit message for his word.')
lines[idx[0]] = L[:j] + TAIL; dw2 = '\n'.join(lines)

for path, txt in ((MAP, m2_), (STATE, s2), (REC, r), (MI, mi2), (DW, dw2)):
    assert txt != rd(path), path
    open(path + '.tmp', 'w', encoding='utf-8').write(txt); os.replace(path + '.tmp', path)
    print(f'wrote {path.replace(ROOT, "<repo>").replace(MEM, "<memory>")}: {len(txt.encode()):,} bytes')
print(f'RUN 3 checkpoint written: units {UN}, standing {ST}, hash {HASH}; ritual {NP} PASS; journal {JR} (+{DJ}); overrides by_ref {NREF} / by_gloss {NGL}; labels {LN}')
