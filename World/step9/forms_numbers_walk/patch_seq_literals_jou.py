#!/usr/bin/env python3
# THE NUMBERS WALK 13b (2026-09-12): the sequence file's literals and checkpoints for the journeys — the import line (the live registration
# edge), the DAEMON_ORDER entry, RUN (predicted in the design), PREVIOUS_RUN (12b's RUN exactly), NEWEST_RUNNER, PLACEMENT (predicted), and
# the CZ1-CZ9 block after CY9 + the VERDICTS entries. NO global-count checkpoint moves (entities 318 and closes 121 unmoved by design). CENSUS
# is typed in a second pass from the stitcher's print (seq_stitch_jou.out). Every replacement anchored on the exact prior text; the file
# is asserted to compile after. patch_seq_literals_gad.py's form.
import re
P = '<repo-old>/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
# 1. the import line — the live edge the dependency gate reads
i = s.index('import cold_run_gad_reuben   # THE NUMBERS WALK 12b'); j = s.index('\n', i)
s = s[:j + 1] + "import cold_run_journeys   # THE NUMBERS WALK 13b (2026-09-12): the journeys (33:1-56) — three lines: the writing (journeys_recorded on the people, its value THE LIST of forty-two — a data row, no camp written twice), the departure retold with THE RUN OF EXODUS 12:12 (the judgments on the gods a status on Egypt, forty years on; the firstborn's plague OPEN), the command in the divine voice (two debits on Israel OPEN BY DESIGN to Joshua's runs; the lot's debit of 26:52-56 cited, not rewritten); no line for 33:38-40 (the tape's 20:28 and 21:1 checkpointed)\n" + s[j + 1:]
# 2. DAEMON_ORDER
rep("    ('cold_run_gad_reuben', 'law_gad_reuben'),   # THE NUMBERS WALK 12b (2026-09-12; NUMBERS_WALK.md \"Sitting 12b\"): Gad and Reuben — TWELVE lines of 32:1-42 at (40, 6, 1), 13 writes, no timer, one close by value (the build debit), seven entities (the written-on parties); no marker in the chapter; installed_by boot (a stipulation in Moses' voice with no divine frame, the class named)\n",
    "    ('cold_run_gad_reuben', 'law_gad_reuben'),   # THE NUMBERS WALK 12b (2026-09-12; NUMBERS_WALK.md \"Sitting 12b\"): Gad and Reuben — TWELVE lines of 32:1-42 at (40, 6, 1), 13 writes, no timer, one close by value (the build debit), seven entities (the written-on parties); no marker in the chapter; installed_by boot (a stipulation in Moses' voice with no divine frame, the class named)\n"
    "    ('cold_run_journeys', 'law_journeys'),   # THE NUMBERS WALK 13b (2026-09-12; NUMBERS_WALK.md \"Sitting 13b\"): the journeys — THREE lines of 33:1-56 at (40, 6, 1), 4 writes, no timer, no close, no new entity (moses, israel and egypt_people standing); no marker in the chapter (33:3's and 33:38's dates are the tape's markers at Exodus 12:41 and Numbers 20:28 — checkpoints, never second markers); installed_by boot (a law in the divine voice spoken in the plains of Moab, the class named)\n")
# 3. RUN — the design's prediction
rep("RUN = (1271, 66, 52, 0, 12, 1518, 30, 318,   # THE NUMBERS WALK 12b (2026-09-12): PREDICTED",
    "RUN = (1274, 66, 52, 0, 12, 1522, 31, 318,   # THE NUMBERS WALK 13b (2026-09-12): PREDICTED in NUMBERS_WALK.md \"Sitting 13b\" (THE PREDICTION'S ARITHMETIC) BEFORE the run — events +3 (the three lines), timers set 66 / fired 52 / cancels 0 / retro-writes 12 UNMOVED (no timer in the chapter), writes +4 (L1 1, L2 1, L3 2), daemons fired +1 (law_journeys), entities +0 (318 — the written-on parties moses, israel and egypt_people standing), the four pairs unchanged; sitting 12b's line follows:   # THE NUMBERS WALK 12b (2026-09-12): PREDICTED")
rep("       121)   # THE NUMBERS WALK 12b (2026-09-12): 120 -> 121 — ONE close BY VALUE:",
    "       121)   # THE NUMBERS WALK 13b (2026-09-12): 121 UNMOVED — no close on the tape (the gods' judgment had no entry to close; the firstborn's plague stays open, a burial is no removal; the lot's debit of 26:52-56 stays open, cited by 33:54; the two new debits OPEN BY DESIGN to Joshua's runs); sitting 12b's line follows:   # THE NUMBERS WALK 12b (2026-09-12): 120 -> 121 — ONE close BY VALUE:")
# 4. PREVIOUS_RUN — 12b's RUN exactly
rep("PREVIOUS_RUN = (1259, 66, 52, 0, 12, 1505, 29, 311,   # THE NUMBERS WALK 12b (2026-09-12): sitting 11b's RUN EXACTLY",
    "PREVIOUS_RUN = (1271, 66, 52, 0, 12, 1518, 30, 318,   # THE NUMBERS WALK 13b (2026-09-12): sitting 12b's RUN EXACTLY — the tape minus the journeys' three lines reproduces it (no marker in the span; the four writes go with the lines; no close); sitting 12b's line follows:   # THE NUMBERS WALK 12b (2026-09-12): sitting 11b's RUN EXACTLY")
rep("       120)   # THE NUMBERS WALK 12b (2026-09-12): sitting 11b's 120;",
    "       121)   # THE NUMBERS WALK 13b (2026-09-12): sitting 12b's 121; sitting 12b's line follows:   # THE NUMBERS WALK 12b (2026-09-12): sitting 11b's 120;")
# 5. NEWEST_RUNNER
rep("NEWEST_RUNNER = 'gad_reuben'   # THE NUMBERS WALK 12b (2026-09-12): Gad and Reuben's twelve lines",
    "NEWEST_RUNNER = 'journeys'   # THE NUMBERS WALK 13b (2026-09-12): the journeys' three lines (inside the declared span [[Num,33,1,56]]; no marker row) the newest joined (was 'gad_reuben'); THE REST drops them and reproduces 12b's RUN exactly — the four writes go with the lines, no close; sitting 12b's line follows:   # THE NUMBERS WALK 12b (2026-09-12): Gad and Reuben's twelve lines")
# 6. PLACEMENT — predicted, read at the stitcher's print
rep("PLACEMENT = {'markers': {'text_constrained': 102, 'reading_placed': 40}, 'events': {'text_constrained': 106, 'page_order': 1125, 'reading_placed': 40}}   # THE NUMBERS WALK 12b (2026-09-12): PREDICTED",
    "PLACEMENT = {'markers': {'text_constrained': 102, 'reading_placed': 40}, 'events': {'text_constrained': 106, 'page_order': 1128, 'reading_placed': 40}}   # THE NUMBERS WALK 13b (2026-09-12): PREDICTED in the design and read at the stitcher's print — events page_order 1125 -> 1128 (the three lines at the counter's day), the rest unmoved; sitting 12b's line follows:   # THE NUMBERS WALK 12b (2026-09-12): PREDICTED")
# 7. THE VERDICTS entries
rep("            'CY1 MATCH', 'CY2 MATCH', 'CY3 MATCH', 'CY4 MATCH', 'CY5 MATCH', 'CY6 MATCH', 'CY7 MATCH', 'CY8 MATCH', 'CY9 MATCH',\n",
    "            'CY1 MATCH', 'CY2 MATCH', 'CY3 MATCH', 'CY4 MATCH', 'CY5 MATCH', 'CY6 MATCH', 'CY7 MATCH', 'CY8 MATCH', 'CY9 MATCH',\n            'CZ1 MATCH', 'CZ2 MATCH', 'CZ3 MATCH', 'CZ4 MATCH', 'CZ5 MATCH', 'CZ6 MATCH', 'CZ7 MATCH', 'CZ8 MATCH', 'CZ9 MATCH',   # THE NUMBERS WALK 13b (2026-09-12): the journeys' nine\n")
# 8. THE CZ BLOCK after CY9
CZ = '''    # ---- THE NUMBERS WALK 13b (2026-09-12; NUMBERS_WALK.md "Sitting 13b" THE CHECKPOINTS): the journeys' three lines — CZ the prefix measured free ----
    JO_KINDS = ['journeys_written', 'gods_judged_at_the_departure', 'dispossession_commanded']
    ev_jo = [(i, l) for i, l in enumerate(w.log) if l[0] == 'EVENT' and l[2]['kind'] in JO_KINDS]
    cp('CZ1 THE LINES — three events of the chapter\\'s kinds on the tape in the ink\\'s order, every one page_order at (40, 6, 1) = the counter\\'s day, AFTER Gad and Reuben\\'s last line (32:42) and BEFORE the tribes\\' plea (36:1-4); no marker inside Num 33', (3, ['page_order'], [(40, 6, 1)], JO_KINDS, True, 0), (len(ev_jo), sorted(set(l[2].get('placement') for _, l in ev_jo)), sorted(set(ex.date(l[1]) for _, l in ev_jo)), [l[2]['kind'] for _, l in ev_jo], bool(ev_jo) and bool(ev_gr) and bool(i36v) and ev_gr[-1][0] < ev_jo[0][0] and ev_jo[-1][0] < i36v[0], sum(1 for l in markers if WE.first_verse(l[2].get('verse')) and WE.first_verse(l[2].get('verse'))[0] == 'Num' and (33, 1) <= WE.first_verse(l[2].get('verse'))[1:] <= (33, 56))))
    jo_rec = [e for e in LG('israel') if e['effect'] == 'journeys_recorded']
    camps = [e for e in LG('israel') if e['effect'] == 'encamped_at']
    camp_heads = [re.split(r'[,;(\\u2014]', str(e.get('value', '')))[0].strip() for e in camps]
    camps_matched = [h for h in camp_heads if h in cold_run_journeys.PLACES_EN]; camps_unmatched = [h for h in camp_heads if h not in cold_run_journeys.PLACES_EN]
    cp('CZ2 THE FORTY-TWO — journeys_recorded on israel_people ONE entry valued "42 places"; the DATA row\\'s forty-two (Rameses and forty-one camps; eighteen named nowhere else); the tape\\'s sixteen encamped_at statuses read against the list — eleven matched by the itinerary\\'s names, five not (Goshen before Rameses; the wilderness of Shur — 33:8 says Etham; the Red Sea way of 21:4 a road; Mattanah to Pisgah absent from the itinerary; Shittim = 33:49\\'s extent)', (1, True, 42, 18, 16, 11, ['Goshen', 'Shittim', 'from Mount Hor by the way of the Red Sea', 'from the wilderness Mattanah', 'the wilderness of Shur']), (len(jo_rec), str(jo_rec[0].get('value', '')).startswith('42 places') if jo_rec else None, len(cold_run_journeys.STATIONS), sum(1 for x in cold_run_journeys.STATIONS if x['only_here']), len(camps), len(camps_matched), sorted(camps_unmatched)))
    mk_exodus = [l for l in markers if l[2].get('verse') == 'Exod 12:41']
    cp('CZ3 THE DEPARTURE\\'S DATE — 33:3\\'s [15] with the ordinals [1, 1] = (1, 1, 15) = the exodus marker at Exodus 12:41 (ONE marker line, its date read); the runner\\'s DEPARTURE_DATE by CALL; a retelling\\'s date a checkpoint, never a second marker', (1, (1, 1, 15), (1, 1, 15), 15, [1, 1]), (len(mk_exodus), ex.date(mk_exodus[0][1]) if mk_exodus else None, cold_run_journeys.DEPARTURE_DATE, cold_run_journeys.FIFTEEN, cold_run_journeys.ORDS[3]))
    eg_judg = [e for e in LG('egypt_people') if e['effect'] == 'judgments_executed_on_their_gods']
    eg_struck = [e for e in LG('egypt_people') if e['effect'] == 'plague_struck']; eg_fb = [e for e in eg_struck if e.get('value') == 'the_firstborn']; eg_rem = [e for e in LG('egypt_people') if e['effect'] == 'plague_removed']
    any_judg = [(ent_.eid, e['effect']) for ent_ in w.entities.values() for e in ent_.ledger if 'judgments' in e['effect']]
    cp('CZ4 THE RUN OF EXODUS 12:12 — ONE status judgments_executed_on_their_gods on egypt_people (the act\\'s first telling, at 33:4), its source the chapter\\'s line and its law note citing 12:12; NO other entry on the tape names the judgments; the firstborn\\'s plague_struck OPEN (ten struck, four removed — a burial is no removal)', (1, True, True, [('egypt_people', 'judgments_executed_on_their_gods')], 10, 1, True, 4), (len(eg_judg), str(eg_judg[0].get('case_source', '')).startswith('Num 33:3-4') if eg_judg else None, '12:12' in str(eg_judg[0].get('source_law', '')) if eg_judg else None, any_judg, len(eg_struck), len(eg_fb), eg_fb[0].get('open') if eg_fb else None, len(eg_rem)))
    mk_aaron = [l for l in markers if l[2].get('verse') == 'Num 20:28']
    ev_aaron = [l for l in w.log if l[0] == 'EVENT' and l[2]['kind'] == 'garments_transferred_and_aaron_died']
    cp('CZ5 THE DEATH DATE — the marker at Num 20:28 = (40, 5, 1) = 33:38\\'s ordinals [40, 5] and number [1] (the runner\\'s AARON_DATE and the chukat runner\\'s CK.AARON_DATE by CALL); the 20:28 event\\'s date field [40, 5, 1] and age 123; 123 = Exodus 7:7\\'s 83 + 40 and Deuteronomy 34:7\\'s 120 = 80 + 40 by the same parser', (1, (40, 5, 1), (40, 5, 1), (40, 5, 1), 1, [40, 5, 1], 123, 123, 83, 120, 80), (len(mk_aaron), ex.date(mk_aaron[0][1]) if mk_aaron else None, cold_run_journeys.AARON_DATE, cold_run_journeys.CK.AARON_DATE, len(ev_aaron), ev_aaron[0][2].get('date') if ev_aaron else None, ev_aaron[0][2].get('age') if ev_aaron else None, cold_run_journeys.AGE, cold_run_journeys.AARON_83, cold_run_journeys.MOSES_120, cold_run_journeys.MOSES_80))
    ev_arad = [l for l in w.log if l[0] == 'EVENT' and l[2]['kind'] == 'arad_fought_and_took_captives']
    arad_dest = [e for e in LG('the-king-of-arad') if e['effect'] == 'destroyed']; isr_capt = [e for e in LG('israel') if e['effect'] == 'taken_captive']
    cp('CZ6 ARAD — the arad_fought_and_took_captives event (21:1) ONE at (40, 5, 1), the run 33:40 cites; the king\\'s destroyed ONE, OPEN; israel_people\\'s taken_captive ONE, OPEN — both untouched by the retelling', (1, (40, 5, 1), 1, True, 1, True), (len(ev_arad), ex.date(ev_arad[0][1]) if ev_arad else None, len(arad_dest), arad_dest[0].get('open') if arad_dest else None, len(isr_capt), isr_capt[0].get('open') if isr_capt else None))
    isr_cmd = [e for e in LG('israel') if e['effect'] == 'commanded']
    disp = [e for e in isr_cmd if e.get('value') == 'dispossess_the_inhabitants_and_possess_the_land']; imgs = [e for e in isr_cmd if e.get('value') == 'destroy_their_images']; lot = [e for e in isr_cmd if e.get('value') == 'divide_the_land']
    cp('CZ7 THE COMMAND\\'S DEBITS — commanded dispossess_the_inhabitants_and_possess_the_land on israel_people ONE entry OPEN (its law note naming Joshua 23:13 and Judges 2:3 as the negative arm\\'s runs) and destroy_their_images ONE entry OPEN (the three objects); the lot\\'s divide_the_land debit (26:52-56) ONE entry OPEN — none added by 33:54', (1, True, True, True, 1, True, 1, True, 'Num 26:52-56'), (len(disp), disp[0].get('open') if disp else None, 'Joshua 23:13' in str(disp[0].get('source_law', '')) if disp else None, 'Judges 2:3' in str(disp[0].get('source_law', '')) if disp else None, len(imgs), imgs[0].get('open') if imgs else None, len(lot), lot[0].get('open') if lot else None, str(lot[0].get('case_source', ''))[:12] if lot else None))
    with _ctx.redirect_stdout(_io.StringIO()):
        rg_cc33 = RG.class_counts(rg_ink, w); rg_cr33 = RG.class_receipts(rg_ink, w); rg_cf33 = RG.class_footers(rg_ink)
    cp('CZ8 THE REGISTER GATE BY CALL — no count line and no receipt in Num 33 on this world (the chapter\\'s five numbers a date, a way, the springs and palms, the death\\'s date and age; "by the mouth of the LORD" at 33:2 and 33:38 not a class the gate censuses); the footer Num 36:13 DAEMONS (law_journeys now in its block)', ([], [], 'DAEMONS'), ([k for k in rg_cc33 if k.startswith('Num 33:')], [k for k in rg_cr33 if k.startswith('Num 33:')], (rg_cf33.get('Num 36:13') or {}).get('class') if isinstance(rg_cf33.get('Num 36:13'), dict) else rg_cf33.get('Num 36:13')))
    cp('CZ9 THE REST — entities 318 UNMOVED (no new party: moses, israel_people and egypt_people standing), closes 121 UNMOVED (no close on the tape); the three kinds present; the other counts 12b\\'s exactly with the three lines dropped (THE REST test below)', (318, 121, True), (len(w.entities), closes_done, all(k in {l[2]['kind'] for l in w.log if l[0] == 'EVENT'} for k in JO_KINDS)))
'''
anchor = "    print('    the story\\'s dates: Moses born %r"
assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, CZ + anchor)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: import, DAEMON_ORDER, RUN, PREVIOUS_RUN, NEWEST_RUNNER, PLACEMENT, VERDICTS CZ, CZ1-CZ9; compiles')
