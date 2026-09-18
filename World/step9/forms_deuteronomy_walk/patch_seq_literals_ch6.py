import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 4b (2026-09-17): the sequence file's literals and checkpoints for chapter 6 — the import line (the live registration edge),
# the DAEMON_ORDER entry, RUN (predicted in the design: +2 events, +2 writes, +1 daemon fired; the rest unmoved), PREVIOUS_RUN (3b's RUN EXACTLY —
# NO declared delta: the daemon writes only on its own lines), NEWEST_RUNNER, PLACEMENT and CENSUS READ FROM THE STITCHER'S PRINT (seq_stitch_ch6.out
# — asserted at the design's prediction), the CO1-CO9 block after CI9 + the VERDICTS entries; NO retype of the older REST literals (closes 127 and
# markers 167 UNMOVED — checked by the design). Every replacement anchored on the exact prior text; the file asserted to compile after.
# patch_seq_literals_ch5.py's form.
import re, ast, subprocess, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
assert 'import cold_run_hear_o_israel' not in s, 'already patched'
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 4b (2026-09-17)'
# 0. THE STITCHER'S PRINT — the placement and the census read, never typed
pr = open(SP + '/seq_stitch_ch6.out', encoding='utf-8').read()
PLACEMENT = ast.literal_eval(re.search(r'^PLACEMENT LITERAL: (.*)$', pr, re.M).group(1))
CENSUS = ast.literal_eval(re.search(r'^  CENSUS tuple .*?: (\(.*\))$', pr, re.M).group(1))
PLACEMENT_PREDICTED = {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1140, 'reading_placed': 55}}   # the design: the two lines page_order on the counter's own day, NO marker
assert PLACEMENT == PLACEMENT_PREDICTED, ('THE PLACEMENT MOVED FROM THE DESIGN — read the stitcher\'s print', PLACEMENT, PLACEMENT_PREDICTED)
assert CENSUS[2] == 1304 and CENSUS[9] == 167 and CENSUS[10] == 129 and CENSUS[12] == 23 and CENSUS[13] == 849 and CENSUS[14] == 272, ('THE CENSUS MOVED FROM THE DESIGN — read the stitcher\'s print', CENSUS)
# 1. the import line — the live edge the dependency gate reads
i = s.index('import cold_run_covenant_at_horeb   # THE DEUTERONOMY WALK 3b'); j = s.index('\n', i)
s = s[:j + 1] + "import cold_run_hear_o_israel   # %s: chapter 6 (Deut 6:1-25) — THE SHEMA: the creed and the FOUR DUTIES compiled for the first time (the recitation, the teaching, the tefillin, the mezuzah — no runner held a cell), shema_commanded a STATUS on Israel at the chapter's own line (6:4-9, the counter's day (40, 11, 1), NO marker); the test at Massah a RUN CITATION BY NAME (the tape's Exodus 17:7 line), test_barred a BLOCK at the second line (6:16-19); THE READBACK'S THIRD FORM — the son's answer a retelling INSIDE A LAW, seven rows graded against the tape; the compartments FOUR a parameter with the spellings' open row; the receipt without the Name (6:25) a run citation the register gate's finder is blind to\n" % W + s[j + 1:]
# 2. DAEMON_ORDER
i = s.index("    ('cold_run_covenant_at_horeb', 'law_covenant_at_horeb'),   # THE DEUTERONOMY WALK 3b"); j = s.index('\n', i)
s = s[:j + 1] + "    ('cold_run_hear_o_israel', 'law_hear_o_israel'),   # %s; DEUTERONOMY_WALK.md \"Sitting 4b\": chapter 6 — TWO lines (both STATUTE by form, page_order on the counter's own day (40, 11, 1), NO marker), 2 writes (shema_commanded a status and test_barred a block on Israel — the daemon writes only on its own lines: THE REST drops them, no declared delta), no timer, no close, no new entity, no population row; installed_by boot (the two Deuteronomy daemons' form), given_at Deut 6:4\n" % W + s[j + 1:]
# 3. RUN — the design's prediction
rep("RUN = (1302, 96, 88, 0, 12, 1593, 36, 319,   # THE DEUTERONOMY WALK 3b (2026-09-16): PREDICTED",
    "RUN = (1304, 96, 88, 0, 12, 1595, 37, 319,   # %s: PREDICTED in DEUTERONOMY_WALK.md \"Sitting 4b\" (THE PREDICTION'S ARITHMETIC) BEFORE the run — events +2 (the two lines), timers set +0 and fired +0 (no clock walk, no marker), cancels 0, retro-writes 12 UNMOVED, writes +2 (the daemon's watches summed: shema_commanded at the first line, test_barred at the second), daemons fired +1 (law_hear_o_israel), entities +0 (Israel standing), closes +0; sitting 3b's line follows:   # THE DEUTERONOMY WALK 3b (2026-09-16): PREDICTED" % W)
rep("       127)   # THE DEUTERONOMY WALK 3b (2026-09-16): 126 -> 127 — ONE close, inside the daemon",
    "       127)   # %s: 127 UNMOVED — no close this sitting; sitting 3b's line follows:   # THE DEUTERONOMY WALK 3b (2026-09-16): 126 -> 127 — ONE close, inside the daemon" % W)
# 4. PREVIOUS_RUN — 3b's RUN EXACTLY, no declared delta
rep("PREVIOUS_RUN = (1300, 96, 88, 0, 12, 1590, 36, 319,   # THE DEUTERONOMY WALK 3b (2026-09-16): sitting 2b's RUN WITH ONE DECLARED DELTA",
    "PREVIOUS_RUN = (1302, 96, 88, 0, 12, 1593, 36, 319,   # %s: sitting 3b's RUN EXACTLY, read at the design (DEUTERONOMY_WALK.md \"Sitting 4b\", THE PREDICTION'S ARITHMETIC): THE REST drops chapter 6's two lines (inside the declared span [[Deut,6,1,25]]) and the daemon's two writes with them — law_hear_o_israel writes only on its own lines, NO declared delta; sitting 3b's line follows:   # THE DEUTERONOMY WALK 3b (2026-09-16): sitting 2b's RUN WITH ONE DECLARED DELTA" % W)
rep("       126)   # THE DEUTERONOMY WALK 3b (2026-09-16): sitting 2b's 126 — the one close is this runner's own line's, dropped with it",
    "       127)   # %s: sitting 3b's 127 — no close this sitting, THE REST keeps 3b's; sitting 3b's line follows:   # THE DEUTERONOMY WALK 3b (2026-09-16): sitting 2b's 126 — the one close is this runner's own line's, dropped with it" % W)
# 5. NEWEST_RUNNER
rep("NEWEST_RUNNER = 'covenant_at_horeb'   # THE DEUTERONOMY WALK 3b (2026-09-16): chapter 5's two lines and two markers",
    "NEWEST_RUNNER = 'hear_o_israel'   # %s: chapter 6's two lines, NO marker (inside the declared span [[Deut,6,1,25]]) the newest joined (was 'covenant_at_horeb'); THE REST drops them and reproduces 3b's RUN exactly; sitting 3b's line follows:   # THE DEUTERONOMY WALK 3b (2026-09-16): chapter 5's two lines and two markers" % W)
# 6. PLACEMENT — predicted in the design, READ at the stitcher's print (asserted equal above)
rep("PLACEMENT = {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1138, 'reading_placed': 55}}   # THE DEUTERONOMY WALK 3b (2026-09-16): PREDICTED",
    "PLACEMENT = %r   # %s: PREDICTED in the design and READ at the stitcher's print (scratchpad seq_stitch_ch6.out) — events page_order 1138 -> 1140 (the two own-day lines after the tape's last Deuteronomy 5 line), markers UNMOVED (no marker this chapter), text_constrained 109 and reading_placed 55 UNMOVED; sitting 3b's line follows:   # THE DEUTERONOMY WALK 3b (2026-09-16): PREDICTED" % (PLACEMENT, W))
# 7. THE VERDICTS entries
rep("            'CI1 MATCH', 'CI2 MATCH', 'CI3 MATCH', 'CI4 MATCH', 'CI5 MATCH', 'CI6 MATCH', 'CI7 MATCH', 'CI8 MATCH', 'CI9 MATCH',   # THE DEUTERONOMY WALK 3b (2026-09-16): chapter 5's nine\n",
    "            'CI1 MATCH', 'CI2 MATCH', 'CI3 MATCH', 'CI4 MATCH', 'CI5 MATCH', 'CI6 MATCH', 'CI7 MATCH', 'CI8 MATCH', 'CI9 MATCH',   # THE DEUTERONOMY WALK 3b (2026-09-16): chapter 5's nine\n            'CO1 MATCH', 'CO2 MATCH', 'CO3 MATCH', 'CO4 MATCH', 'CO5 MATCH', 'CO6 MATCH', 'CO7 MATCH', 'CO8 MATCH', 'CO9 MATCH',   # %s: chapter 6's nine\n" % W)
# 8. CENSUS — read from the stitcher's print
rep("CENSUS = (2471, 1311, 1302, 1144, 6, 10, 9, 0, 71, 167, 129, 15, 23, 847, 272)   # THE DEUTERONOMY WALK 3b (2026-09-16): READ from the stitcher's print",
    "CENSUS = %r   # %s: READ from the stitcher's print (scratchpad seq_stitch_ch6.out) after chapter 6's TWO lines joined — on the tape 1302 -> 1304 AS THE DESIGN PREDICTED, markers 167 UNMOVED (F 129, R 23), kinds 847 -> 849 (the two tape kinds, STATUTE by form — the case kind no tape kind), subjects 272 UNMOVED (Israel standing), closes 71 unmoved, the case rows the exam's fourteen persons; sitting 3b's line follows:   # THE DEUTERONOMY WALK 3b (2026-09-16): READ from the stitcher's print" % (CENSUS, W))
# 9. THE CO BLOCK after CI9
CO = '''    # ---- THE DEUTERONOMY WALK 4b (2026-09-17; DEUTERONOMY_WALK.md "Sitting 4b" THE CHECKPOINTS): chapter 6's two lines, NO marker — CO the prefix measured free ----
    HI_KINDS = ['shema_declared', 'testing_barred']
    ev_hi = [(i, l) for i, l in enumerate(w.log) if l[0] == 'EVENT' and l[2]['kind'] in HI_KINDS]
    i_last_d5 = max(i for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 5:'))
    cp('CO1 THE LINES — two events of the sitting\\'s kinds on the tape in the ink\\'s order, both AFTER the tape\\'s last Deuteronomy 5 line, both page_order on the counter\\'s own day (40, 11, 1) with NO dated day, NO marker added (markers 167 unmoved); the counter ends at (40, 11, 1)', (2, HI_KINDS, True, ['page_order'], [(40, 11, 1)], [None], 167, (40, 11, 1)), (len(ev_hi), [l[2]['kind'] for _, l in ev_hi], bool(ev_hi) and ev_hi[0][0] > i_last_d5, sorted(set(l[2].get('placement') for _, l in ev_hi)), sorted(set(ex.date(l[1]) for _, l in ev_hi)), sorted(set(l[2].get('dated') for _, l in ev_hi), key=str), len(markers), ex.date(w.clock.day)))
    sc_hi = [e for e in LG('israel') if e['effect'] == 'shema_commanded']; dd_hi = yaml.safe_load(open(os.path.join(HERE, 'daemon_dispositions.yaml'), encoding='utf-8'))
    cp('CO2 THE FOUR DUTIES — shema_commanded on israel_people ONE (a status), source beginning "Deut 6:4", its value naming the four duties and the head\\'s FOUR compartments (the parameter); law_hear_o_israel registered, given_at Deut 6:4, installed_by boot; the functions block\\'s six cells WRAPPED', (1, 'Deut 6:4', 4, 4, 'Deut 6:4', 'boot', 6), (len(sc_hi), str(sc_hi[0].get('case_source', ''))[:8] if sc_hi else None, len(sc_hi[0]['value']['duties']) if sc_hi and isinstance(sc_hi[0].get('value'), dict) else None, sc_hi[0]['value']['compartments']['head'] if sc_hi and isinstance(sc_hi[0].get('value'), dict) else None, (dd_hi['daemons'].get('law_hear_o_israel') or {}).get('given_at'), str((dd_hi['daemons'].get('law_hear_o_israel') or {}).get('installed_by', '')).split()[0], sum(1 for v_ in (dd_hi.get('functions', {}).get('hear_o_israel') or {}).values() if v_.get('status') == 'WRAPPED')))
    tb_hi = [e for e in LG('israel') if e['effect'] == 'test_barred']
    fv_hi = lambda kind, b, c, v: sum(1 for l in events if l[2]['kind'] == kind and WE.first_verse(l[2].get('case_source')) == (b, c, v))
    cp('CO3 THE TEST BARRED — test_barred on israel_people ONE (a block), source beginning "Deut 6:16"; the tape\\'s Rephidim lines FOUND by kind and first verse: murmured at Exod 17:2 ONE, rock_struck at Exod 17:6 ONE, named at Exod 17:7 ONE ("Massah and Meribah" in its name)', (1, 'Deut 6:1', 1, 1, 1, True), (len(tb_hi), str(tb_hi[0].get('case_source', ''))[:8] if tb_hi else None, fv_hi('murmured', 'Exod', 17, 2), fv_hi('rock_struck', 'Exod', 17, 6), fv_hi('named', 'Exod', 17, 7), any(l[2]['kind'] == 'named' and 'Massah' in str(l[2].get('name', '')) for l in events)))
    RB_hi = cold_run_hear_o_israel.READBACK; EVk_hi = [l[2] for l in events]
    found_hi = sum(1 for r_ in RB_hi if any(e['kind'] == r_['tape_kind'] and WE.first_verse(e.get('case_source')) == WE.first_verse(r_['tape_verse']) for e in EVk_hi))
    cp('CO4 THE READBACK\\'S THIRD FORM — the_readback\\'s rows SEVEN (the answer\\'s five, the header\\'s, the test\\'s), every row inside a law (T1), every row\\'s tape entry FOUND on the running world by kind and first verse (rows n = found n); the grades\\' census typed from the runner\\'s own print (VERBATIM 3, EXPANDED 3, SHORTENED 1); the ten plague_struck lines on the tape; no row OPEN', (7, 7, True, {'VERBATIM': 3, 'EXPANDED': 3, 'SHORTENED': 1}, 10, []), (len(RB_hi), found_hi, all(r_['law'] for r_ in RB_hi), dict(cold_run_hear_o_israel.RB_GRADES), sum(1 for l in events if l[2]['kind'] == 'plague_struck'), [r_['verses'] for r_ in RB_hi if r_['open']]))
    og_hi = [e for e in LG('israel') if e['effect'] == 'other_gods_barred']; cv_hi = [e for e in LG('israel') if e['effect'] == 'coveting_barred']
    cp('CO5 THE SECOND WORD STANDS — other_gods_barred on israel_people ONE UNMOVED (no second write at 6:14 — the cell CALLED), coveting_barred ONE unmoved; both sourced at the giving\\'s line "Deut 4:10"', (1, 1, 'Deut 4:1', 'Deut 4:1'), (len(og_hi), len(cv_hi), str(og_hi[0].get('case_source', ''))[:8] if og_hi else None, str(cv_hi[0].get('case_source', ''))[:8] if cv_hi else None))
    with _ctx.redirect_stdout(_io.StringIO()):
        rg_cr_hi = RG.class_receipts(rg_ink, w)
    dep_hi = yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))
    cp('CO6 THE RECEIPT WITHOUT THE NAME — the register gate\\'s own finder (register_census.class_receipts, by CALL) lists NO seat at Deut 6:25 nor any seat in chapter 6 (the blindness measured, asserted); the RUN_CITATION pointer "Deut 6:25" AS_WHEN on file for hear_o_israel, with 6:3, 6:16 and 6:19 (four)', (False, [], ['Deut 6:3', 'Deut 6:16', 'Deut 6:19', 'Deut 6:25']), ('Deut 6:25' in rg_cr_hi, [k_ for k_ in rg_cr_hi if str(k_).startswith('Deut 6:')], [p_['verse'] for p_ in dep_hi['pointers'] if p_.get('runner') == 'hear_o_israel' and p_.get('disposition') == 'RUN_CITATION' and p_.get('form') == 'AS_WHEN']))
    tc_hi = [e for e in LG('moses') if e['effect'] == 'commanded' and e.get('value') == 'teach_the_commandment']
    cp('CO7 THE CHARGE EXECUTED — commanded on moses valued teach_the_commandment ONE, CLOSED, closed_by beginning "Deut 1:" UNMOVED (6:1 a reference row, no write, no second close); closes 127', (1, False, 'Deut 1:', 127), (len(tc_hi), bool(tc_hi) and bool(tc_hi[0].get('open')), str(tc_hi[0].get('closed_by', ''))[:7] if tc_hi else None, closes_done))
    pl_hi = [e for e in LG('egypt_people') if e['effect'] == 'plague_struck']
    cp('CO8 THE EXODUS READ BACK — the ten plague_struck lines and their closes UNMOVED (ten entries on egypt_people, four closed by their removals — frogs, swarms, hail, locusts); brought_out ONE; sea_split ONE; nothing written on Egypt or Pharaoh from chapter 6 (0 entries sourced "Deut 6")', (10, 4, 1, 1, 0), (len(pl_hi), sum(1 for e in pl_hi if e.get('closed_by')), sum(1 for l in events if l[2]['kind'] == 'brought_out'), sum(1 for l in events if l[2]['kind'] == 'sea_split'), sum(1 for e in LG('egypt_people') + LG('pharaoh') if str(e.get('case_source', '')).startswith('Deut 6'))))
    cp('CO9 THE REST — entities 319 UNMOVED (Israel the written-on party, standing), closes 127 UNMOVED, the population table 148 UNMOVED, the two kinds present, markers 167 UNMOVED (no marker this chapter); the other counts 3b\\'s exactly with the two lines and the daemon\\'s two writes dropped (THE REST test below — NO declared delta)', (319, 127, 148, True, 167), (len(w.entities), closes_done, len(w.tables['population']), all(k in {l[2]['kind'] for l in events} for k in HI_KINDS), len(markers)))
'''
anchor = "    print('    the story\\'s dates: Moses born %r"
assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, CO + anchor)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: import, DAEMON_ORDER, RUN, PREVIOUS_RUN (no declared delta), NEWEST_RUNNER, PLACEMENT (read %r), VERDICTS CO, CENSUS (read %r), CO1-CO9; compiles' % (PLACEMENT, CENSUS))
