#!/usr/bin/env python3
# THE DEUTERONOMY WALK 6b — the docket run's close (2026-09-19): the map's "THE DOCKET — AS RUN" paragraph, the state doc's #196 addendum 3, the
# recovery page's section-2 lines, the memory (MEMORY.md's walk line; deuteronomy-walk.md's description and a paragraph). EVERY COUNT PARSED from
# the writer's print (ch8_docket_write.out) and the parts' census, never typed; every text built whole before its file is opened; the size caps
# asserted (the recovery page 10,240; MEMORY.md 17,000). 5b's write_ch7_run2.py's form.
import os, re, subprocess, importlib.util, sys
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SCR)
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
P = open(f'{SCR}/ch8_docket_write.out', encoding='utf-8').read()
m = re.search(r'WROTE (\S+) (\d+) bytes', P); OUTP, NB = m.group(1), int(m.group(2))
m = re.search(r'rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \)', P); NR, NL, NT, NC, NCL, NCT = map(int, m.groups())
m = re.search(r"verdicts (\{.*?\}) link (\{.*?\}) topic (\{.*?\})", P); VALL, VLINK, VTOP = (eval(x) for x in m.groups())
LAWC = eval(re.search(r'LAW by cell (\{.*?\})', P).group(1)); NOUT = eval(re.search(r'OUTSIDE by work (\{.*?\})', P).group(1))
VERSES = eval(re.search(r'verses cited (\[.*?\]) UNCITED', P).group(1)); UNC = eval(re.search(r'UNCITED (\[.*?\])', P).group(1))
m = re.search(r'Berakhot 35a-49b whole (\d+) read (\d+)', P); BKW, BKR = int(m.group(1)), int(m.group(2))
parts = {}
for p in 'ABC':
    spec = importlib.util.spec_from_file_location(f'ch8_docket_{p}', f'{SCR}/ch8_docket_{p}.py'); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    parts[p] = (len(mod.ROWS), dict(sorted(Counter(v for _, v, _ in mod.ROWS).items())), mod.WHOLE_STATS)
assert sum(n for n, _, _ in parts.values()) == NR == 451, parts
assert all(s['corrected'] == 0 for _, _, s in parts.values())
SZ = {p: os.path.getsize(f'{SCR}/ch8_rows_{p}.txt') for p in 'ABC'}
def vs(d): return ', '.join(f'{k} {v}' for k, v in d.items())
verses_s = ', '.join(f'{k.split(":")[1]} ({n})' if n > 1 else k.split(':')[1] for k, n in VERSES)
unc_s = ', '.join(str(v) for v in UNC)
lint0 = 'lint 0 (one flag on the first write — the word for a reciter of the early teaching in one note, retyped in the SPEC and the ledger rewritten by the same writer before any record cited it)'
CROWNS = ('the grace after meals BY TORAH LAW and its four blessings — the verse cut three ways (the baraita\'s 48b:5, the Tosefta 6:1\'s, Rabbi\'s 48b:6), the fourth blessing\'s standing disputed (49a:5); '
          'THE BLESSING BEFORE — every derivation refuted (the praises, the a fortiori, the seven species, "that He gave you", Exodus 23:25, Saul\'s blessing), the rule FOUNDED ON REASON and rabbinic (35a:18-19; 20b:16; 21a:2, 21a:6) — the write names the after alone; '
          'THE MEASURE OF "SATISFIED" a PARAMETER with a Torah edge (20b:14; R. Meir\'s olive against R. Yehuda\'s egg from the two verbs at 49b:9, Pesachim 49b, Yoma 79b, Mishnah 7:2; R. Tzadok; "that is hunger" 42a:2; wine satisfies but no meal is based on it); '
          'THE COMMAND\'S FORM — the grace NOT AN OBLIGATION but conditional on eating (49b:4), not time-bound (20b:7), its persons (women OPEN 20b:11-14; the priests; consecrated food; the zimmun\'s (the invitation\'s) persons), the meal\'s end and the reciter (42a:5-7, 43a:11-12; "Rav is dead and we have not learned the laws of the grace" 43a:1); '
          'the order of blessings by the verse and RAV HAMNUNA\'S TWO "LAND"S (41a:8, 41b:5), the verse\'s other reading — the measures (Eruvin 4a, Sukkah 5b, 41a:9-41b:3; the Rambam: a mnemonic), the seven species\' after-blessing and "A LAND CONCLUDED THE MATTER" — the grace\'s object bread (44a:10), 8:8-10 the paradigm of every blessing (35a:15); '
          'the first fruits from the seven species (Bikkurim 1:3, 1:10; Menachot 84a-b; the seven vessels); '
          '"he afflicted you and let you hunger" — the Day\'s affliction hunger by the analogy with 8:3 and ITS TWO GUARDS (the public\'s from the public\'s, God\'s hand from God\'s hand — Yoma 74b:12-13), the manna\'s forms and tastes, the daily manna\'s reason ("everyone\'s heart to their Father in Heaven every day" 76a:2-3), the sixty cubits, MOSES\' FIRST BLESSING AT THE MANNA (48b:2); '
          'the Land lacks nothing — the pepper (three seats), the stones read builders (Taanit 4a), 28:48\'s inversion (35b:7); the afflictions of love and the Land\'s price (5a:9-23); '
          'arrogance — denial (4b:11), idolatry by 7:26 (4b:10), hewn like an Asherah by 7:5 (5a:10), the eighth of an eighth (5a:16-17), "filling his stomach" (32a); '
          '"BEWARE, LEST, NOT" NOTHING BUT A PROHIBITION at three seats (Sotah 5a:3; Makkot 13b:5; Eruvin 96a:8) and the rule\'s limit (96a:9) — 8:11 a negative command, forgetting_barred a BLOCK; the grace in any language (Sotah 33a); the rock\'s verb in the blessing\'s grammar (38a); 12:21 a receipt seat forward (Yoma 75b:4)')
UNPRED = ('(1) the grace CONDITIONAL on eating, not an obligation (Berakhot 49b:4) — a DATA row the_grace_conditional for F3; (2) the first blessing instituted AT THE MANNA before its verse (48b:2) — an install-order note for the table beside THE INSTALL HYPOTHESIS; '
          '(3) Rabbi\'s third division of the verse and the fourth blessing\'s standing disputed (48b:6, 49a:5) — the four blessings\' DATA row carries three divisions; (4) "a land concluded the matter" — the grace\'s object BREAD by the Rabbis (44a:10) — the write\'s object named in F3\'s row; '
          '(5) the analogy\'s two guards — 8:3\'s hunger GOD\'S ACT on the PUBLIC (Yoma 74b:12-13) — the readback row 8:3 TURNED\'s shelf reading, cited in the row; (6) 12:21 "as I have commanded you" a receipt seat for chapter 12\'s compile (Yoma 75b:4) — a note owed forward; '
          '(7) 28:48 "in want of all things" inverts 8:9\'s "lack nothing" (Berakhot 35b:7) — a note for F3 lack_nothing, chapter 28 forward; (8) the quail\'s written/read pair and the 248 counted from a defective spelling (Yoma 75b:6, 75b:10) — the store\'s letters again, notes. '
          'THE DESIGN\'S ONE OPEN DECISION MEASURED ON THE SHELF: 8:4 (the garment and the foot) is cited by NO ROW — the fifth form\'s SUPPLIED grade stands unchallenged by the shelf, the decision the owner\'s')
MAP = ('\nTHE DOCKET — AS RUN (2026-09-19, on "Go" after the compaction; ITS OWN RUN under the two-run rule\'s docket clause; the compaction point #196 addendum 2): THE\n'
       'REREADS (the recovery page, this section, the memory index). THE INSTRUMENTS by sed from 5b\'s forms — ch8_docket_common.py (the ADDRS assert reads the dump\n'
       'header\'s ROWS count, never typed; the six cells of cold_run_good_land.py in its head), ch8_docket_rows.py (N huge prints the row whole); the three parts printed\n'
       f'WHOLE to ch8_rows_A-C.txt ({SZ["A"] // 1000}, {SZ["B"] // 1000}, {SZ["C"] // 1000} KB) by the dump\'s order: A rows 0-117 (the 34 link rows; Mishnah Berakhot 6:1-7:5; Mishnah Bikkurim 1:1-1:11; Berakhot 5a;\n'
       '20b-21a), B 118-259 (Berakhot 35a-35b; 41a-44a), C 260-450 (Berakhot 48b-49b; Yoma 74b-76a; Sotah 4b-5a; Makkot 13b; Eruvin 96a) — EVERY ROW READ WHOLE before its\n'
       f'verdict was typed, the parts\' WHOLE dicts empty, apply_whole\'s counts zero (computed): A {parts["A"][0]} rows ({vs(parts["A"][1])}), B {parts["B"][0]} ({vs(parts["B"][1])}),\n'
       f'C {parts["C"][0]} ({vs(parts["C"][1])}). THE WRITER write_ch8_docket.py (write_ch7_docket.py\'s form: the ENUMERATED line parsed for Berakhot 35a-49b, LONG 9 ranges\n'
       f'asserted, MISH 24, the three Berakhot ranges inside 35a-49b asserted to sum to the read count, the verse hits asserted, THE UNCITED VERSES COMPUTED) WROTE\n'
       f'logic/oral_triage/deu_08_ekev_exam_2026-09-19.md ({NB:,} bytes — dated the day it was written, the design having expected 09-18): {NR} rows (link {NL}, topic {NT}), credited {NC}\n'
       f'(link {NCL}, topic {NCT}); the verdicts {vs(VALL)} (link {vs(VLINK)}; topic {vs(VTOP)}); LAW by cell {vs(LAWC)} (no LAW row names F1, F2, F5 or F6 — the chapter\'s\n'
       f'law is the grace and the warning, the rest reference rows and DATA); OUTSIDE by work {vs(NOUT)}; Berakhot 35a-49b whole {BKW}, read {BKR}, the remainder {BKW - BKR} enumerated by amud; the\n'
       f'verses cited {verses_s} — {len(UNC)} cited by no one ({unc_s}); coverage computed, the cite index {NR} addresses, missing 0 extra 0; {lint0}.\n'
       f'THE CROWNS (fourteen in the finds section): {CROWNS}.\n'
       f'WHAT THE DESIGN DID NOT PREDICT, for RUN B: {UNPRED}. NOTHING OF THE ENGINE TOUCHED; the tree: + the exam ledger, + eighteen forms in\n'
       'World/step9/forms_deuteronomy_walk/ (the docket\'s instruments and prints, the scan, the recon and the design\'s writer with their prints). NEXT on the owner\'s word: RUN B per\n'
       'THE ORDER above — the probes Q19-Q21 to FAIL first.\n')
SD = ('\n#196 ADDENDUM 3 (2026-09-19 — THE DOCKET OF 6b CLOSED, on the owner\'s "Go" after the compaction; its own run under the two-run rule\'s docket clause): THE REREADS (the recovery page, the map\'s "Sitting 6b … THE DESIGN", MEMORY.md). '
      'THE INSTRUMENTS by sed from 5b\'s forms (ch8_docket_common.py, ch8_docket_rows.py); the three parts printed WHOLE (ch8_rows_A-C.txt) and read whole before any verdict — '
      f'A rows 0-117 ({parts["A"][0]}: {vs(parts["A"][1])}), B 118-259 ({parts["B"][0]}: {vs(parts["B"][1])}), C 260-450 ({parts["C"][0]}: {vs(parts["C"][1])}); every part\'s WHOLE dict empty, apply_whole\'s counts zero (computed). '
      f'write_ch8_docket.py (write_ch7_docket.py\'s form — the ENUMERATED line parsed for Berakhot 35a-49b, LONG 9, MISH 24, the read amudim asserted to sum, the verse hits asserted, the uncited verses computed) WROTE logic/oral_triage/deu_08_ekev_exam_2026-09-19.md ({NB} bytes; dated the writing day, not the design\'s expected 09-18): '
      f'{NR} rows (link {NL}, topic {NT}), credited {NC} (link {NCL}, topic {NCT}); the verdicts {vs(VALL)} (link {VLINK}; topic {VTOP}); LAW by cell {LAWC}; OUTSIDE by work {NOUT}; Berakhot 35a-49b whole {BKW}, read {BKR}, the remainder {BKW - BKR} enumerated by amud; '
      f'the verses cited {verses_s}; {len(UNC)} cited by no one ({unc_s}); coverage computed, the cite index {NR} addresses, missing 0 extra 0; {lint0}. '
      f'THE CROWNS (fourteen in the docket\'s finds section): {CROWNS}. '
      f'WHAT THE DESIGN DID NOT PREDICT, for RUN B: {UNPRED}. '
      'THE TREE: + logic/oral_triage/deu_08_ekev_exam_2026-09-19.md; + eighteen forms in World/step9/forms_deuteronomy_walk/ (ch8_docket_common.py, ch8_docket_rows.py, ch8_docket_A-C.py, write_ch8_docket.py, ch8_docket_dump.txt, ch8_rows_A-C.txt, ch8_docket_write.out, ch8_docket_scan.py, ch8_scan.out, ch8_compile_recon.py, ch8_recon.out, write_ch8b_design.py, ch8b_design_check.out, ch8b_design_write.out — the home-path gate GREEN after the copy); '
      'the map\'s "THE DOCKET — AS RUN" paragraph at the end of the 6b design section; the recovery page\'s section 2; the memory. NOTHING OF THE ENGINE TOUCHED; the tape, the registries, the runners as at #196 addendum 2. NOT COMMITTED (since 29c189b; the reading\'s message at <scratch>/commit_msg_ch8.txt — 6b rides the next message). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. '
      'THE WORD FOR THE NEXT RUN — RUN B OF 6b, its first step: readback_probes.py Q19-Q21 written to FAIL before the runner exists (the design\'s THE PROBES paragraph; Q16-Q18\'s form in World/step9/readback_probes.py), then THE ORDER as the design wrote it: add_types_ch8.py from add_types_ch7.py by sed (the three tape kinds, the case kind, the two effects, the daemon, the functions block, the CALL edges), the recorder and the stitcher (SPAN_ORDER + \'good_land\', no marker row), the runner cold_run_good_land.py in parts (ch8_part1-4.py assembled by cat; the fast checker; CASES generated; the DATA rows the_grace_conditional and the four blessings\' three divisions added from the docket), the literals CU1-CU9, the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, gates_chain.sh in the background (one summary), the records from the sheet in one call (the AS BUILT; COMPILE_DEBT\'s sitting-6 box PAID + the 6b box; MOVE_CATALOG checked; MIDDOT\'s docket entries — the verbal analogies at Yoma 74b:11, Menachot 84b:14, Sanhedrin 99a:5, Berakhot 48b:10, Makkot 13b:12, Sotah 5a:10, the a fortiori at 35a:7 / 48b:5 / 21a:5 / 5a:18, the "do not read" at Taanit 4a:3 / 48b:7 / Sotah 4b:13 — EVERY CODE CHECKED IN MIDDOT.md AGAINST THE ROW\'S OWN WORDS BEFORE IT IS TYPED; MISHNAH_TOPICS Berakhot 6-7 and Bikkurim 1 READ; RESEARCH_LOG; THE_STEPS; THE_BRIEFING; THE_LOOP\'s step-6 row; RESUME; the memory; the state doc\'s addendum; the recovery page rewritten; the addenda\'s section), the forms copied, the commit message. '
      'POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 6b … THE DESIGN" (the newest section — its "THE DOCKET — AS RUN" paragraph at the end), MEMORY.md; then the docket\'s finds section (logic/oral_triage/deu_08_ekev_exam_2026-09-19.md, "## The finds") before the runner is typed.\n')
# ---- the map
mp = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; t = open(mp, encoding='utf-8').read()
assert t.endswith('THE ORDER above — the probes Q19-Q21 to FAIL first.\n') is False and t.rstrip().endswith('the commit message for the owner\'s word.'), t[-120:]
assert 'THE DOCKET — AS RUN (2026-09-19' not in t
open(mp, 'w', encoding='utf-8').write(t + MAP)
# ---- the state doc
sp = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; t = open(sp, encoding='utf-8').read()
assert t.endswith('\n') and '#196 ADDENDUM 2 (' in t and '#196 ADDENDUM 3 (' not in t
open(sp, 'w', encoding='utf-8').write(t + SD)
# ---- the recovery page (section 2 rewritten in place; the cap asserted)
rp = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; t = open(rp, encoding='utf-8').read()
subs = [('## 2. WHERE IT STANDS (2026-09-18, after sitting 6; the state doc #196 addendum 1 the newest point)', '## 2. WHERE IT STANDS (2026-09-19, after 6b\'s docket; the state doc #196 addendum 3 the newest point)'),
        ('8:1-20 READ AND FROZEN (sitting 6, one run).', '8:1-20 READ AND FROZEN (sitting 6).'),
        ('- Uncommitted since 29c189b: sitting 6 whole and the two-run rule\'s records; the message at <scratch>/commit_msg_ch8.txt.', '- Uncommitted since 29c189b: sitting 6, the two-run rule, 6b so far; the message at <scratch>/commit_msg_ch8.txt.'),
        ('- IN FLIGHT: 6b RUN A DONE (the design in the map); NEXT: the docket WHOLE (its own run), then RUN B. The commit on his word.', '- IN FLIGHT: 6b RUN A AND THE DOCKET DONE (2026-09-19, 451 rows whole); NEXT: RUN B, the probes to FAIL first. The commit on his word.'),
        ('the newest instances: the map\'s "Sitting 6" and "Sitting 5b")', 'the newest instances: the map\'s "Sitting 6b" and "Sitting 6")')]
for a, b in subs:
    assert t.count(a) == 1, a; t = t.replace(a, b)
assert len(t.encode('utf-8')) <= 10240, len(t.encode('utf-8'))
open(rp, 'w', encoding='utf-8').write(t)
# ---- the memory
mm = f'{MEM}/MEMORY.md'; t = open(mm, encoding='utf-8').read()
a = 'map World/step9/DEUTERONOMY_WALK.md; chapters 1-7 COMPILED (29c189b PUSHED); SITTING 6 DONE 2026-09-18 (ch 8 FROZEN, 222 units); 6b RUN A DONE; NEXT: the docket'
b = 'map World/step9/DEUTERONOMY_WALK.md; ch 1-7 COMPILED (29c189b PUSHED); SITTING 6 DONE (ch 8 FROZEN, 222 units); 6b RUN A + DOCKET DONE 2026-09-19; NEXT: RUN B'
assert t.count(a) == 1; t = t.replace(a, b); assert len(t.encode('utf-8')) < 17000, len(t.encode('utf-8'))
open(mm, 'w', encoding='utf-8').write(t)
dw = f'{MEM}/deuteronomy-walk.md'; t = open(dw, encoding='utf-8').read()
a = 'description: "COMMITTED THROUGH 29c189b (2026-09-18; PUSHED) — '
assert t.count(a) == 1; t = t.replace(a, a + '6b DOCKET DONE 2026-09-19 (451 rows whole, deu_08_ekev_exam_2026-09-19.md; UNCOMMITTED) — ')
para = (f'\nSITTING 6b THE DOCKET DONE 2026-09-19 (on "Go" after the compaction; its own run): the 451 rows read WHOLE in three parts on 5b\'s instruments by sed; '
        f'write_ch8_docket.py WROTE logic/oral_triage/deu_08_ekev_exam_2026-09-19.md ({NB} bytes; {vs(VALL)}; credited {NC}; the uncited verses computed: {unc_s}; lint 0). '
        f'The crowns: the grace by Torah law and its four blessings (the verse cut three ways); the blessing BEFORE every derivation refuted, founded on reason — rabbinic; the measure of "satisfied" a PARAMETER with a Torah edge; the grace CONDITIONAL on eating (49b:4 — unpredicted, a DATA row); the two "land"s; "a land concluded the matter" — bread the grace\'s object; the analogy\'s two guards on 8:3 (God\'s act on the public); "beware, lest, not" nothing but a prohibition at three seats; the first blessing instituted at the manna before its verse (an install-order note). '
        '8:4 cited by no row — the SUPPLIED grade stands unchallenged. The forms copied (eighteen). Clean point (#196 addendum 3). NEXT: RUN B — the probes Q19-Q21 to FAIL first, then the types, the runner, the tape, the chain, the records.\n')
open(dw, 'w', encoding='utf-8').write(t + para)
print('MAP +%d chars; SD +%d; RP %d bytes; MEMORY.md %d bytes; deuteronomy-walk.md +%d' % (len(MAP), len(SD), os.path.getsize(rp), os.path.getsize(mm), len(para)))
