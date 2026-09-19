import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 6b (2026-09-19): the sequence file's literals and checkpoints for chapter 8 — the import line (the live registration edge), the
# DAEMON_ORDER entry, RUN (predicted in the design: +3 events, +3 writes, +1 daemon fired; the rest unmoved), PREVIOUS_RUN (5b's RUN EXACTLY — NO declared
# delta: the daemon writes only on its own lines), NEWEST_RUNNER, PLACEMENT and CENSUS READ FROM THE STITCHER'S PRINT (seq_stitch_ch8.out — asserted at
# the design's prediction), the CU1-CU9 block after CQ9 + the VERDICTS entries; NO retype of the older REST literals (closes 127 and markers 167
# UNMOVED — checked by the design). Every replacement anchored on the exact prior text (the CENSUS line by its head — its tuple read from the file); the
# file asserted to compile after. patch_seq_literals_ch7.py's form.
import re, ast, subprocess, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
assert 'import cold_run_good_land' not in s, 'already patched'
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 6b (2026-09-19)'
# 0. THE STITCHER'S PRINT — the placement and the census read, never typed
pr = open(SP + '/seq_stitch_ch8.out', encoding='utf-8').read()
PLACEMENT = ast.literal_eval(re.search(r'^PLACEMENT LITERAL: (.*)$', pr, re.M).group(1))
CENSUS = ast.literal_eval(re.search(r'^  CENSUS tuple .*?: (\(.*\))$', pr, re.M).group(1))
PLACEMENT_PREDICTED = {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1146, 'reading_placed': 55}}   # the design: the three lines page_order on the counter's own day, NO marker
assert PLACEMENT == PLACEMENT_PREDICTED, ('THE PLACEMENT MOVED FROM THE DESIGN — read the stitcher\'s print', PLACEMENT, PLACEMENT_PREDICTED)
assert CENSUS[2] == 1310 and CENSUS[9] == 167 and CENSUS[10] == 129 and CENSUS[12] == 23 and CENSUS[13] == 855 and CENSUS[14] == 272, ('THE CENSUS MOVED FROM THE DESIGN — read the stitcher\'s print', CENSUS)
# 1. the import line — the live edge the dependency gate reads
i = s.index('import cold_run_seven_nations   # THE DEUTERONOMY WALK 5b'); j = s.index('\n', i)
s = s[:j + 1] + "import cold_run_good_land   # %s: chapter 8 (Deut 8:1-20) — THE GOOD LAND: the grace after the meal and the forgetting barred compiled for the first time (THE CODE'S HOLES — no runner held the Torah's one command to bless him; 6:12's cell held 'lest you forget' as an ask without a write), the testimony's effect REUSED at its second seat; THE READBACK'S FIFTH FORM — the retelling of a STATE: eighteen reference rows against the tape's lines and the kin's cells, the garment's row (8:4) SUPPLIED with no retrograde write; three lines on the counter's day (40, 11, 1), NO marker\n" % W + s[j + 1:]
# 2. DAEMON_ORDER
i = s.index("    ('cold_run_seven_nations', 'law_seven_nations'),   # THE DEUTERONOMY WALK 5b"); j = s.index('\n', i)
s = s[:j + 1] + "    ('cold_run_good_land', 'law_good_land'),   # %s; DEUTERONOMY_WALK.md \"Sitting 6b\": chapter 8 — THREE lines (all STATUTE by form, page_order on the counter's own day (40, 11, 1), NO marker), 3 writes (the grace's status, the forgetting's block, the testimony's reused entry — all on Israel; the daemon writes only on its own lines: THE REST drops them, no declared delta), no timer, no close, no new entity, no population row; installed_by boot (the Deuteronomy daemons' form), given_at Deut 8:1\n" % W + s[j + 1:]
# 3. RUN — the design's prediction
rep("RUN = (1307, 96, 88, 0, 12, 1602, 38, 319,   # THE DEUTERONOMY WALK 5b (2026-09-18): PREDICTED",
    "RUN = (1310, 96, 88, 0, 12, 1605, 39, 319,   # %s: PREDICTED in DEUTERONOMY_WALK.md \"Sitting 6b\" (THE PREDICTION'S ARITHMETIC) BEFORE the run — events +3 (the three lines), timers set +0 and fired +0 (no clock walk, no marker), cancels 0, retro-writes 12 UNMOVED, writes +3 (the daemon's watches summed: one per line), daemons fired +1 (law_good_land), entities +0 (Israel standing), closes +0; sitting 5b's line follows:   # THE DEUTERONOMY WALK 5b (2026-09-18): PREDICTED" % W)
rep("       127)   # THE DEUTERONOMY WALK 5b (2026-09-18): 127 UNMOVED — no close this sitting (the ban's debit OPEN to Joshua); sitting 4b's line follows:",
    "       127)   # %s: 127 UNMOVED — no close this sitting (a status, a block and a reused entry have no closer); sitting 5b's line follows:   # THE DEUTERONOMY WALK 5b (2026-09-18): 127 UNMOVED — no close this sitting (the ban's debit OPEN to Joshua); sitting 4b's line follows:" % W)
# 4. PREVIOUS_RUN — 5b's RUN EXACTLY, no declared delta
rep("PREVIOUS_RUN = (1304, 96, 88, 0, 12, 1595, 37, 319,   # THE DEUTERONOMY WALK 5b (2026-09-18): sitting 4b's RUN EXACTLY",
    "PREVIOUS_RUN = (1307, 96, 88, 0, 12, 1602, 38, 319,   # %s: sitting 5b's RUN EXACTLY, read at the design (DEUTERONOMY_WALK.md \"Sitting 6b\", THE PREDICTION'S ARITHMETIC): THE REST drops chapter 8's three lines (inside the declared span [[Deut,8,1,20]]) and the daemon's three writes with them — law_good_land writes only on its own lines, NO declared delta; sitting 5b's line follows:   # THE DEUTERONOMY WALK 5b (2026-09-18): sitting 4b's RUN EXACTLY" % W)
rep("       127)   # THE DEUTERONOMY WALK 5b (2026-09-18): sitting 4b's 127 — no close this sitting, THE REST keeps 4b's;",
    "       127)   # %s: sitting 5b's 127 — no close this sitting, THE REST keeps 5b's; sitting 5b's line follows:   # THE DEUTERONOMY WALK 5b (2026-09-18): sitting 4b's 127 — no close this sitting, THE REST keeps 4b's;" % W)
# 5. NEWEST_RUNNER
rep("NEWEST_RUNNER = 'seven_nations'   # THE DEUTERONOMY WALK 5b (2026-09-18): chapter 7's three lines, NO marker",
    "NEWEST_RUNNER = 'good_land'   # %s: chapter 8's three lines, NO marker (inside the declared span [[Deut,8,1,20]]) the newest joined (was 'seven_nations'); THE REST drops them and reproduces 5b's RUN exactly; sitting 5b's line follows:   # THE DEUTERONOMY WALK 5b (2026-09-18): chapter 7's three lines, NO marker" % W)
# 6. PLACEMENT — predicted in the design, READ at the stitcher's print (asserted equal above)
rep("PLACEMENT = {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1143, 'reading_placed': 55}}   # THE DEUTERONOMY WALK 5b (2026-09-18): PREDICTED",
    "PLACEMENT = %r   # %s: PREDICTED in the design and READ at the stitcher's print (scratchpad seq_stitch_ch8.out) — events page_order 1143 -> 1146 (the three own-day lines after the tape's last Deuteronomy 7 line), markers UNMOVED (no marker this chapter), text_constrained 109 and reading_placed 55 UNMOVED; sitting 5b's line follows:   # THE DEUTERONOMY WALK 5b (2026-09-18): PREDICTED" % (PLACEMENT, W))
# 7. THE VERDICTS entries
rep("            'CQ1 MATCH', 'CQ2 MATCH', 'CQ3 MATCH', 'CQ4 MATCH', 'CQ5 MATCH', 'CQ6 MATCH', 'CQ7 MATCH', 'CQ8 MATCH', 'CQ9 MATCH',   # THE DEUTERONOMY WALK 5b (2026-09-18): chapter 7's nine\n",
    "            'CQ1 MATCH', 'CQ2 MATCH', 'CQ3 MATCH', 'CQ4 MATCH', 'CQ5 MATCH', 'CQ6 MATCH', 'CQ7 MATCH', 'CQ8 MATCH', 'CQ9 MATCH',   # THE DEUTERONOMY WALK 5b (2026-09-18): chapter 7's nine\n            'CU1 MATCH', 'CU2 MATCH', 'CU3 MATCH', 'CU4 MATCH', 'CU5 MATCH', 'CU6 MATCH', 'CU7 MATCH', 'CU8 MATCH', 'CU9 MATCH',   # %s: chapter 8's nine — CU the LAST free two-letter prefix (a note owed forward)\n" % W)
# 8. CENSUS — read from the stitcher's print; the prior line found by its head (its tuple read from the file, never typed)
m = re.search(r"^CENSUS = (\(.*?\))   # THE DEUTERONOMY WALK 5b \(2026-09-18\): READ from the stitcher's print", s, re.M); assert m, 'the CENSUS line'
OLD_CENSUS = ast.literal_eval(m.group(1)); assert OLD_CENSUS[2] == 1307 and OLD_CENSUS[13] == 852, OLD_CENSUS
s = s[:m.start()] + ("CENSUS = %r   # %s: READ from the stitcher's print (scratchpad seq_stitch_ch8.out) after chapter 8's THREE lines joined — on the tape 1307 -> 1310 AS THE DESIGN PREDICTED, markers 167 UNMOVED (F 129, R 23), kinds 852 -> 855 (the three tape kinds, STATUTE by form — the case kind no tape kind), subjects 272 UNMOVED (Israel standing), closes 71 unmoved, the case rows the exam's thirteen persons; sitting 5b's line follows:   # THE DEUTERONOMY WALK 5b (2026-09-18): READ from the stitcher's print" % (CENSUS, W)) + s[m.end():]
# 9. THE CU BLOCK after CQ9
CU = '''    # ---- THE DEUTERONOMY WALK 6b (2026-09-19; DEUTERONOMY_WALK.md "Sitting 6b" THE CHECKPOINTS): chapter 8's three lines, NO marker — CU the prefix measured free, THE LAST of the two-letter series (the next compile opens a new series: a note owed forward) ----
    GL_KINDS = ['grace_commanded', 'forgetting_warned', 'perishing_testified']
    ev_gl = [(i, l) for i, l in enumerate(w.log) if l[0] == 'EVENT' and l[2]['kind'] in GL_KINDS]
    i_last_d7 = max(i for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 7:'))
    cp('CU1 THE LINES — three events of the sitting\\'s kinds on the tape in the ink\\'s order, all AFTER the tape\\'s last Deuteronomy 7 line, all page_order on the counter\\'s own day (40, 11, 1) with NO dated day, NO marker added (markers 167 unmoved); the counter ends at (40, 11, 1)', (3, GL_KINDS, True, ['page_order'], [(40, 11, 1)], [None], 167, (40, 11, 1)), (len(ev_gl), [l[2]['kind'] for _, l in ev_gl], bool(ev_gl) and ev_gl[0][0] > i_last_d7, sorted(set(l[2].get('placement') for _, l in ev_gl)), sorted(set(ex.date(l[1]) for _, l in ev_gl)), sorted(set(l[2].get('dated') for _, l in ev_gl), key=str), len(markers), ex.date(w.clock.day)))
    bl_gl = [e for e in LG('israel') if e['effect'] == 'bless_after_eating_commanded']; dd_gl = yaml.safe_load(open(os.path.join(HERE, 'daemon_dispositions.yaml'), encoding='utf-8'))
    cp('CU2 THE BLESSING — bless_after_eating_commanded on israel_people ONE (a status), source beginning "Deut 8:7" (the line\\'s first verse — the design wrote 8:10; the effect carries its line\\'s source, 5b\\'s form); law_good_land registered, given_at Deut 8:1, installed_by boot; the functions block\\'s six cells WRAPPED', (1, 'Deut 8:7', 'Deut 8:1', 'boot', 6), (len(bl_gl), str(bl_gl[0].get('case_source', ''))[:8] if bl_gl else None, (dd_gl['daemons'].get('law_good_land') or {}).get('given_at'), str((dd_gl['daemons'].get('law_good_land') or {}).get('installed_by', '')).split()[0], sum(1 for v_ in (dd_gl.get('functions', {}).get('good_land') or {}).values() if v_.get('status') == 'WRAPPED')))
    fb_gl = [e for e in LG('israel') if e['effect'] == 'forgetting_barred']
    cp('CU3 THE FORGETTING — forgetting_barred on israel_people ONE (a block; its first tape write — 6:12\\'s cell called, no write there), source beginning "Deut 8:11"', (1, 'Deut 8:11'), (len(fb_gl), str(fb_gl[0].get('case_source', ''))[:9] if fb_gl else None))
    RB_gl = cold_run_good_land.READBACK; EVk_gl = [l[2] for l in events]
    found_tape_gl = sum(1 for r_ in RB_gl if r_['tape_kind'] and any(e['kind'] == r_['tape_kind'] and WE.first_verse(e.get('case_source')) == WE.first_verse(r_['tape_verse']) for e in EVk_gl))
    by_call_gl = sum(1 for r_ in RB_gl if r_['cell'] and r_['cell_found'])
    sup_gl = [r_ for r_ in RB_gl if r_['grade'] == 'SUPPLIED']
    cp('CU4 THE READBACK OF A STATE — the_readback\\'s rows EIGHTEEN, every reference row\\'s entry FOUND: ten on the tape by kind and first verse (decree_declared at Num 14:26, manna_fell at Exod 16:13 thrice, brought_out at Exod 12:51, fiery_serpents_sent at Num 21:6, rock_struck at Exod 17:6, sworn_by_himself at Gen 22:16, witnesses_called at Deut 4:25, nations_devoted at Deut 7:1), seven in the kin\\'s cells by CALL (obey_horeb, opening_speech, hear_o_israel, covenant_at_horeb); the grades\\' census typed from the runner\\'s print (VERBATIM 6, VARIANT 5, EXPANDED 4, TURNED 2, SUPPLIED 1); the one SUPPLIED row the garment\\'s (8:4) with its ledger scan EMPTY; the three holes named; no row OPEN', (18, 10, 7, {'VERBATIM': 6, 'VARIANT': 5, 'EXPANDED': 4, 'TURNED': 2, 'SUPPLIED': 1}, 3, [], ['Deut 8:4'], [[]]), (len(RB_gl), found_tape_gl, by_call_gl, dict(cold_run_good_land.RB_GRADES), len(cold_run_good_land.HOLES), [r_['verses'] for r_ in RB_gl if r_['open']], [r_['verses'] for r_ in sup_gl], [r_['ledger_scan'] for r_ in sup_gl]))
    def _n_gl(eff): return len([e for e in LG('israel') if e['effect'] == eff])
    cp('CU5 THE KIN STANDS — on israel_people manna_provided ONE, water_from_the_rock TWO, serpents_sent ONE UNMOVED (the readback references, no second write); shema_commanded ONE and test_barred ONE UNMOVED; other_gods_barred ONE UNMOVED (the cell CALLED); blessings_for_hearing ONE UNMOVED; treasured_people ONE UNMOVED', (1, 2, 1, 1, 1, 1, 1, 1), (_n_gl('manna_provided'), _n_gl('water_from_the_rock'), _n_gl('serpents_sent'), _n_gl('shema_commanded'), _n_gl('test_barred'), _n_gl('other_gods_barred'), _n_gl('blessings_for_hearing'), _n_gl('treasured_people')))
    hw_gl = [e for e in LG('israel') if e['effect'] == 'heaven_and_earth_witness']
    cp('CU6 THE TESTIMONY — heaven_and_earth_witness on israel_people TWO: the 4:26 entry UNMOVED (source beginning "Deut 4:25" — the line\\'s first verse) and the reuse at source "Deut 8:19" (no new effect)', (2, 'Deut 4:25', 'Deut 8:19'), (len(hw_gl), str(hw_gl[0].get('case_source', ''))[:9] if hw_gl else None, str(hw_gl[-1].get('case_source', ''))[:9] if hw_gl else None))
    st_gl = sorted({e['effect'] for e in LG('israel') if re.search(cold_run_good_land.STATE_WORDS, '%s %s' % (e['effect'], e.get('value', '')), re.I)})
    cp('CU7 THE STATE — no effect naming a garment, clothing, a shoe or a swelling on israel_people (the SUPPLIED grade\\'s assertion, run on the running world with the runner\\'s own word list); the readback\\'s SUPPLIED row 8:4', ([], 'Deut 8:4'), (st_gl, sup_gl[0]['verses'] if sup_gl else None))
    cp('CU8 THE WILDERNESS READ BACK — brought_out ONE, manna_fell ONE, rock_struck ONE, rock_struck_twice ONE, fiery_serpents_sent ONE, decree_declared ONE, witnesses_called ONE, nations_devoted ONE UNMOVED on the tape; nothing written on Egypt or Pharaoh from chapter 8 (0 entries sourced "Deut 8")', (1, 1, 1, 1, 1, 1, 1, 1, 0), tuple(sum(1 for l in events if l[2]['kind'] == k_) for k_ in ('brought_out', 'manna_fell', 'rock_struck', 'rock_struck_twice', 'fiery_serpents_sent', 'decree_declared', 'witnesses_called', 'nations_devoted')) + (sum(1 for e in LG('egypt_people') + LG('pharaoh') if str(e.get('case_source', '')).startswith('Deut 8')),))
    cp('CU9 THE REST — entities 319 UNMOVED (Israel the written-on party, standing), closes 127 UNMOVED, the population table 148 UNMOVED, the three kinds present, markers 167 UNMOVED (no marker this chapter); the other counts 5b\\'s exactly with the three lines and the daemon\\'s three writes dropped (THE REST test below — NO declared delta)', (319, 127, 148, True, 167), (len(w.entities), closes_done, len(w.tables['population']), all(k in {l[2]['kind'] for l in events} for k in GL_KINDS), len(markers)))
'''
anchor = "    print('    the story\\'s dates: Moses born %r"
assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, CU + anchor)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: import, DAEMON_ORDER, RUN, PREVIOUS_RUN (no declared delta), NEWEST_RUNNER, PLACEMENT (read %r), VERDICTS CU, CENSUS (read %r), CU1-CU9; compiles' % (PLACEMENT, CENSUS))
