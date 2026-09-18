#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 5b (2026-09-18): the sequence file's literals and checkpoints for chapter 7 — the import line (the live registration edge),
# the DAEMON_ORDER entry, RUN (predicted in the design: +3 events, +7 writes, +1 daemon fired; the rest unmoved), PREVIOUS_RUN (4b's RUN EXACTLY —
# NO declared delta: the daemon writes only on its own lines), NEWEST_RUNNER, PLACEMENT and CENSUS READ FROM THE STITCHER'S PRINT (seq_stitch_ch7.out
# — asserted at the design's prediction), the CQ1-CQ9 block after CO9 + the VERDICTS entries; NO retype of the older REST literals (closes 127 and
# markers 167 UNMOVED — checked by the design). Every replacement anchored on the exact prior text; the file asserted to compile after.
# patch_seq_literals_ch6.py's form.
import re, ast, subprocess, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
assert 'import cold_run_seven_nations' not in s, 'already patched'
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 5b (2026-09-18)'
# 0. THE STITCHER'S PRINT — the placement and the census read, never typed
pr = open(SP + '/seq_stitch_ch7.out', encoding='utf-8').read()
PLACEMENT = ast.literal_eval(re.search(r'^PLACEMENT LITERAL: (.*)$', pr, re.M).group(1))
CENSUS = ast.literal_eval(re.search(r'^  CENSUS tuple .*?: (\(.*\))$', pr, re.M).group(1))
PLACEMENT_PREDICTED = {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1143, 'reading_placed': 55}}   # the design: the three lines page_order on the counter's own day, NO marker
assert PLACEMENT == PLACEMENT_PREDICTED, ('THE PLACEMENT MOVED FROM THE DESIGN — read the stitcher\'s print', PLACEMENT, PLACEMENT_PREDICTED)
assert CENSUS[2] == 1307 and CENSUS[9] == 167 and CENSUS[10] == 129 and CENSUS[12] == 23 and CENSUS[13] == 852 and CENSUS[14] == 272, ('THE CENSUS MOVED FROM THE DESIGN — read the stitcher\'s print', CENSUS)
# 1. the import line — the live edge the dependency gate reads
i = s.index('import cold_run_hear_o_israel   # THE DEUTERONOMY WALK 4b'); j = s.index('\n', i)
s = s[:j + 1] + "import cold_run_seven_nations   # %s: chapter 7 (Deut 7:1-26) — THE SEVEN NATIONS: the ban, no favor, no pity and the abomination into the house compiled for the first time (THE CODE'S FOUR HOLES — no runner held a cell), the ban a DEBIT on Israel OPEN to Joshua, covenant_barred and intermarriage_barred (Exodus 23:32's and 34:16's effects) WRITTEN ON THE TAPE FOR THE FIRST TIME, blessings_for_hearing a conditional heaven entry; THE READBACK ON THE KIN — the laws' form run on ANOTHER chapter's code: twenty-one reference rows against the kin's cells by CALL and the tape's lines, no second write; three lines on the counter's day (40, 11, 1), NO marker\n" % W + s[j + 1:]
# 2. DAEMON_ORDER
i = s.index("    ('cold_run_hear_o_israel', 'law_hear_o_israel'),   # THE DEUTERONOMY WALK 4b"); j = s.index('\n', i)
s = s[:j + 1] + "    ('cold_run_seven_nations', 'law_seven_nations'),   # %s; DEUTERONOMY_WALK.md \"Sitting 5b\": chapter 7 — THREE lines (all STATUTE by form, page_order on the counter's own day (40, 11, 1), NO marker), 7 writes (the ban's debit, three blocks, the blessings' heaven entry, the pity's block, the abomination's block — all on Israel; the daemon writes only on its own lines: THE REST drops them, no declared delta), no timer, no close, no new entity, no population row; installed_by boot (the Deuteronomy daemons' form), given_at Deut 7:1\n" % W + s[j + 1:]
# 3. RUN — the design's prediction
rep("RUN = (1304, 96, 88, 0, 12, 1595, 37, 319,   # THE DEUTERONOMY WALK 4b (2026-09-17): PREDICTED",
    "RUN = (1307, 96, 88, 0, 12, 1602, 38, 319,   # %s: PREDICTED in DEUTERONOMY_WALK.md \"Sitting 5b\" (THE PREDICTION'S ARITHMETIC) BEFORE the run — events +3 (the three lines), timers set +0 and fired +0 (no clock walk, no marker), cancels 0, retro-writes 12 UNMOVED, writes +7 (the daemon's watches summed: four at the first line, two at the second, one at the third), daemons fired +1 (law_seven_nations), entities +0 (Israel standing; the seven nations a counterparty string), closes +0; sitting 4b's line follows:   # THE DEUTERONOMY WALK 4b (2026-09-17): PREDICTED" % W)
rep("       127)   # THE DEUTERONOMY WALK 4b (2026-09-17): 127 UNMOVED — no close this sitting; sitting 3b's line follows:",
    "       127)   # %s: 127 UNMOVED — no close this sitting (the ban's debit OPEN to Joshua); sitting 4b's line follows:   # THE DEUTERONOMY WALK 4b (2026-09-17): 127 UNMOVED — no close this sitting; sitting 3b's line follows:" % W)
# 4. PREVIOUS_RUN — 4b's RUN EXACTLY, no declared delta
rep("PREVIOUS_RUN = (1302, 96, 88, 0, 12, 1593, 36, 319,   # THE DEUTERONOMY WALK 4b (2026-09-17): sitting 3b's RUN EXACTLY",
    "PREVIOUS_RUN = (1304, 96, 88, 0, 12, 1595, 37, 319,   # %s: sitting 4b's RUN EXACTLY, read at the design (DEUTERONOMY_WALK.md \"Sitting 5b\", THE PREDICTION'S ARITHMETIC): THE REST drops chapter 7's three lines (inside the declared span [[Deut,7,1,26]]) and the daemon's seven writes with them — law_seven_nations writes only on its own lines, NO declared delta; sitting 4b's line follows:   # THE DEUTERONOMY WALK 4b (2026-09-17): sitting 3b's RUN EXACTLY" % W)
rep("       127)   # THE DEUTERONOMY WALK 4b (2026-09-17): sitting 3b's 127 — no close this sitting, THE REST keeps 3b's;",
    "       127)   # %s: sitting 4b's 127 — no close this sitting, THE REST keeps 4b's; sitting 4b's line follows:   # THE DEUTERONOMY WALK 4b (2026-09-17): sitting 3b's 127 — no close this sitting, THE REST keeps 3b's;" % W)
# 5. NEWEST_RUNNER
rep("NEWEST_RUNNER = 'hear_o_israel'   # THE DEUTERONOMY WALK 4b (2026-09-17): chapter 6's two lines, NO marker",
    "NEWEST_RUNNER = 'seven_nations'   # %s: chapter 7's three lines, NO marker (inside the declared span [[Deut,7,1,26]]) the newest joined (was 'hear_o_israel'); THE REST drops them and reproduces 4b's RUN exactly; sitting 4b's line follows:   # THE DEUTERONOMY WALK 4b (2026-09-17): chapter 6's two lines, NO marker" % W)
# 6. PLACEMENT — predicted in the design, READ at the stitcher's print (asserted equal above)
rep("PLACEMENT = {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1140, 'reading_placed': 55}}   # THE DEUTERONOMY WALK 4b (2026-09-17): PREDICTED",
    "PLACEMENT = %r   # %s: PREDICTED in the design and READ at the stitcher's print (scratchpad seq_stitch_ch7.out) — events page_order 1140 -> 1143 (the three own-day lines after the tape's last Deuteronomy 6 line), markers UNMOVED (no marker this chapter), text_constrained 109 and reading_placed 55 UNMOVED; sitting 4b's line follows:   # THE DEUTERONOMY WALK 4b (2026-09-17): PREDICTED" % (PLACEMENT, W))
# 7. THE VERDICTS entries
rep("            'CO1 MATCH', 'CO2 MATCH', 'CO3 MATCH', 'CO4 MATCH', 'CO5 MATCH', 'CO6 MATCH', 'CO7 MATCH', 'CO8 MATCH', 'CO9 MATCH',   # THE DEUTERONOMY WALK 4b (2026-09-17): chapter 6's nine\n",
    "            'CO1 MATCH', 'CO2 MATCH', 'CO3 MATCH', 'CO4 MATCH', 'CO5 MATCH', 'CO6 MATCH', 'CO7 MATCH', 'CO8 MATCH', 'CO9 MATCH',   # THE DEUTERONOMY WALK 4b (2026-09-17): chapter 6's nine\n            'CQ1 MATCH', 'CQ2 MATCH', 'CQ3 MATCH', 'CQ4 MATCH', 'CQ5 MATCH', 'CQ6 MATCH', 'CQ7 MATCH', 'CQ8 MATCH', 'CQ9 MATCH',   # %s: chapter 7's nine\n" % W)
# 8. CENSUS — read from the stitcher's print
rep("CENSUS = (2487, 1313, 1304, 1158, 6, 10, 9, 0, 71, 167, 129, 15, 23, 849, 272)   # THE DEUTERONOMY WALK 4b (2026-09-17): READ from the stitcher's print",
    "CENSUS = %r   # %s: READ from the stitcher's print (scratchpad seq_stitch_ch7.out) after chapter 7's THREE lines joined — on the tape 1304 -> 1307 AS THE DESIGN PREDICTED, markers 167 UNMOVED (F 129, R 23), kinds 849 -> 852 (the three tape kinds, STATUTE by form — the case kind no tape kind), subjects 272 UNMOVED (Israel standing), closes 71 unmoved, the case rows the exam's fourteen persons; sitting 4b's line follows:   # THE DEUTERONOMY WALK 4b (2026-09-17): READ from the stitcher's print" % (CENSUS, W))
# 9. THE CQ BLOCK after CO9
CQ = '''    # ---- THE DEUTERONOMY WALK 5b (2026-09-18; DEUTERONOMY_WALK.md "Sitting 5b" THE CHECKPOINTS): chapter 7's three lines, NO marker — CQ the prefix measured free ----
    SN_KINDS = ['nations_devoted', 'hearing_blessed', 'abomination_barred']
    ev_sn = [(i, l) for i, l in enumerate(w.log) if l[0] == 'EVENT' and l[2]['kind'] in SN_KINDS]
    i_last_d6 = max(i for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 6:'))
    cp('CQ1 THE LINES — three events of the sitting\\'s kinds on the tape in the ink\\'s order, all AFTER the tape\\'s last Deuteronomy 6 line, all page_order on the counter\\'s own day (40, 11, 1) with NO dated day, NO marker added (markers 167 unmoved); the counter ends at (40, 11, 1)', (3, SN_KINDS, True, ['page_order'], [(40, 11, 1)], [None], 167, (40, 11, 1)), (len(ev_sn), [l[2]['kind'] for _, l in ev_sn], bool(ev_sn) and ev_sn[0][0] > i_last_d6, sorted(set(l[2].get('placement') for _, l in ev_sn)), sorted(set(ex.date(l[1]) for _, l in ev_sn)), sorted(set(l[2].get('dated') for _, l in ev_sn), key=str), len(markers), ex.date(w.clock.day)))
    ban_sn = [e for e in LG('israel') if e['effect'] == 'commanded' and e.get('value') == 'devote_the_seven_nations']; dd_sn = yaml.safe_load(open(os.path.join(HERE, 'daemon_dispositions.yaml'), encoding='utf-8'))
    cp('CQ2 THE BAN — commanded on israel_people valued devote_the_seven_nations ONE, OPEN (no closer — the run is Joshua\\'s), source beginning "Deut 7:1"; law_seven_nations registered, given_at Deut 7:1, installed_by boot; the functions block\\'s six cells WRAPPED', (1, True, 'Deut 7:1', 'Deut 7:1', 'boot', 6), (len(ban_sn), bool(ban_sn) and not ban_sn[0].get('closed_by'), str(ban_sn[0].get('case_source', ''))[:8] if ban_sn else None, (dd_sn['daemons'].get('law_seven_nations') or {}).get('given_at'), str((dd_sn['daemons'].get('law_seven_nations') or {}).get('installed_by', '')).split()[0], sum(1 for v_ in (dd_sn.get('functions', {}).get('seven_nations') or {}).values() if v_.get('status') == 'WRAPPED')))
    cb_sn = [e for e in LG('israel') if e['effect'] == 'covenant_barred']; fb_sn = [e for e in LG('israel') if e['effect'] == 'favor_barred']; ib_sn = [e for e in LG('israel') if e['effect'] == 'intermarriage_barred']
    cp('CQ3 THE BORDER BLOCKS — covenant_barred on israel_people ONE (its first tape write; the case kind entered_the_land ABSENT from the tape), favor_barred ONE, intermarriage_barred ONE valued BOTH directions — all three sourced at the chapter\\'s first line "Deut 7:1"', (1, 1, 1, False, 2, 'Deut 7:1', 'Deut 7:1', 'Deut 7:1'), (len(cb_sn), len(fb_sn), len(ib_sn), any(l[2]['kind'] == 'entered_the_land' for l in events), len(ib_sn[0]['value']['directions']) if ib_sn and isinstance(ib_sn[0].get('value'), dict) else None, str(cb_sn[0].get('case_source', ''))[:8] if cb_sn else None, str(fb_sn[0].get('case_source', ''))[:8] if fb_sn else None, str(ib_sn[0].get('case_source', ''))[:8] if ib_sn else None))
    RB_sn = cold_run_seven_nations.READBACK; EVk_sn = [l[2] for l in events]
    found_tape_sn = sum(1 for r_ in RB_sn if r_['tape_kind'] and any(e['kind'] == r_['tape_kind'] and WE.first_verse(e.get('case_source')) == WE.first_verse(r_['tape_verse']) for e in EVk_sn))
    by_call_sn = sum(1 for r_ in RB_sn if r_['cell'] and r_['cell_found'])
    cp('CQ4 THE READBACK ON THE KIN — the_readback\\'s rows TWENTY-ONE, every row\\'s entry FOUND: six on the tape by kind and first verse (covenant_offered at Exod 19:5 twice, brought_out at Exod 12:51, stand_here_commanded at Deut 5:28, healer_promised at Exod 15:26, plague_struck at Exod 7:20), fifteen in the kin\\'s cells by CALL (ordinances.land, erection.covenant, journeys.the_command, covenant_at_horeb.the_second_word and the_tenth_word); the grades\\' census typed from the runner\\'s print (VERBATIM 4, VARIANT 5, EXPANDED 8, TURNED 3, SHORTENED 1); the four holes named; no row OPEN', (21, 6, 15, {'VERBATIM': 4, 'VARIANT': 5, 'EXPANDED': 8, 'TURNED': 3, 'SHORTENED': 1}, 4, []), (len(RB_sn), found_tape_sn, by_call_sn, dict(cold_run_seven_nations.RB_GRADES), len(cold_run_seven_nations.HOLES), [r_['verses'] for r_ in RB_sn if r_['open']]))
    og_sn = [e for e in LG('israel') if e['effect'] == 'other_gods_barred']; cv_sn = [e for e in LG('israel') if e['effect'] == 'coveting_barred']; tp_sn = [e for e in LG('israel') if e['effect'] == 'treasured_people']
    dsp_sn = [e for e in LG('israel') if e['effect'] == 'commanded' and (str(e.get('value', '')).startswith('dispossess') or e.get('value') == 'destroy_their_images')]
    hp_sn = any(e['effect'] == 'high_places_banned' for ent in w.entities.values() for e in ent.ledger)
    cp('CQ5 THE KIN STANDS — other_gods_barred on israel_people ONE UNMOVED (7:16 no second write — the cell CALLED), coveting_barred ONE UNMOVED (7:25 the turn a readback row), treasured_people ONE UNMOVED and OPEN (a heaven entry), high_places_banned present, the dispossession\\'s two debits (dispossess_the_inhabitants_and_possess_the_land, destroy_their_images) OPEN UNMOVED — the demolition a reference row, no second debit', (1, 1, 1, True, True, 2, 0), (len(og_sn), len(cv_sn), len(tp_sn), bool(tp_sn) and not tp_sn[0].get('closed_by'), hp_sn, len(dsp_sn), sum(1 for e in dsp_sn if e.get('closed_by'))))
    bf_sn = [e for e in LG('israel') if e['effect'] == 'blessings_for_hearing']; pb_sn = [e for e in LG('israel') if e['effect'] == 'pity_barred']
    cp('CQ6 THE BLESSINGS AND THE PITY — blessings_for_hearing on israel_people ONE (a conditional heaven entry, OPEN; NOT blessing_promised — Abram\\'s ladder entry, the registry decided the name), pity_barred ONE (a block — the ink alone, no row on the shelf), both sourced at the chapter\\'s second line "Deut 7:12"', (1, True, 1, 'Deut 7:12', 'Deut 7:12'), (len(bf_sn), bool(bf_sn) and not bf_sn[0].get('closed_by'), len(pb_sn), str(bf_sn[0].get('case_source', ''))[:9] if bf_sn else None, str(pb_sn[0].get('case_source', ''))[:9] if pb_sn else None))
    hab_sn = [e for e in LG('israel') if e['effect'] == 'house_abomination_barred']
    cp('CQ7 THE ABOMINATION — house_abomination_barred on israel_people ONE (a block), sourced at the chapter\\'s third line "Deut 7:25"; coveting_barred ONE UNMOVED (the object\\'s turn a readback row, not a second write)', (1, 'Deut 7:25', 1), (len(hab_sn), str(hab_sn[0].get('case_source', ''))[:9] if hab_sn else None, len(cv_sn)))
    pl_sn = [e for e in LG('egypt_people') if e['effect'] == 'plague_struck']
    cp('CQ8 THE EXODUS READ BACK — the ten plague_struck lines and their closes UNMOVED (ten entries on egypt_people, four closed by their removals); brought_out ONE; sea_split ONE; healer_promised ONE; nothing written on Egypt, Pharaoh or Amalek from chapter 7 (0 entries sourced "Deut 7"); no entity for the seven nations', (10, 4, 1, 1, 1, 0, False), (len(pl_sn), sum(1 for e in pl_sn if e.get('closed_by')), sum(1 for l in events if l[2]['kind'] == 'brought_out'), sum(1 for l in events if l[2]['kind'] == 'sea_split'), sum(1 for l in events if l[2]['kind'] == 'healer_promised'), sum(1 for e in LG('egypt_people') + LG('pharaoh') + LG('amalek') if str(e.get('case_source', '')).startswith('Deut 7')), any(k_ in w.entities for k_ in ('the-nations', 'the-seven-nations', 'the-hittite', 'the-girgashite', 'the-canaanite', 'the-perizzite', 'the-hivite', 'the-jebusite'))))
    cp('CQ9 THE REST — entities 319 UNMOVED (Israel the written-on party, standing; the seven nations a counterparty string), closes 127 UNMOVED, the population table 148 UNMOVED, the three kinds present, markers 167 UNMOVED (no marker this chapter); the other counts 4b\\'s exactly with the three lines and the daemon\\'s seven writes dropped (THE REST test below — NO declared delta)', (319, 127, 148, True, 167), (len(w.entities), closes_done, len(w.tables['population']), all(k in {l[2]['kind'] for l in events} for k in SN_KINDS), len(markers)))
'''
anchor = "    print('    the story\\'s dates: Moses born %r"
assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, CQ + anchor)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: import, DAEMON_ORDER, RUN, PREVIOUS_RUN (no declared delta), NEWEST_RUNNER, PLACEMENT (read %r), VERDICTS CQ, CENSUS (read %r), CQ1-CQ9; compiles' % (PLACEMENT, CENSUS))
