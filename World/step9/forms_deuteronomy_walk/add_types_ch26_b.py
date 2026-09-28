import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b — THE COMPILE OF CHAPTERS 26-28, LEAN (2026-09-26): THE TYPES BY SCRIPT, part B — daemon_dispositions (law_firstfruits_ebal_curses — given_at
# Deut 26:1, installed_by boot; the watches the twenty-one lines with their writes NEW AND REUSED (13b's form — a reused effect is the line's write too); the functions block ELEVEN
# WRAPPED: the ten cells and the_readback); dependency_dispositions (the span's THREE RANGES [[Deut, 26, 1, 19], [Deut, 27, 1, 26], [Deut, 28, 1, 69]], THIRTY-FOUR CALL edges by
# the ink, all REFERENCE — the census decides the rest; THE OWED POINTER Deut 15:6 PAID — REDISPOSITIONED RUN_CITATION reference (the design's word REVERSE is an EDGE disposition, not
# a pointer's — the gate's pointer branch admits CALL, OWED, INTERNAL, RUN_CITATION, PARAMETER, FALSE; a departure recorded): the receipt's referent 28:3 now spoken, the Sifrei 116:1
# the teacher); installation_probes I5 79 -> 80; TWO calendar rows (the_first_fruits_window, the_confessions_hour — the received channel, clock data on the calendar's keys) and
# the_removal_date's exercised_by extended; THE REGISTER FILE UNTOUCHED (no seat in the three chapters — good_land.receipt_seats(26..28) -> [], [], []; the footer at 28:69 computed).
# add_types_ch22_b.py's form; the names READ from the spec module beside this file. RUN FROM THE REPO ROOT.
import yaml, subprocess, re, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch26b_spec as S
CHECK = '--check' in sys.argv
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
W = "THE DEUTERONOMY WALK 18b (2026-09-26) | "
R, DM = S.RUNNER, S.DAEMON
CELLS = [S.CELLS['F%d' % i] for i in range(1, 11)] + ['the_readback']
assert len(CELLS) == 11
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
NOTE = {'first_fruits_declared': "Deut 26:1-11: the basket, the declaration, the recital, the setting before the altar — STATUSES (NEW; Bikkurim 1-3, Terumot 11:3, Peah 1:1 the parameters), the rejoicing REUSED at 26:11 (a third entry); at the counter's day, no marker",
        'tithe_confession_declared': "Deut 26:12-15: the removal, the confession — STATUSES (NEW; Maaser Sheni 5:10-14, Peah 8:5, Sotah 7:1 the parameters), in mourning, in uncleanness, for the dead — BLOCKS (NEW; Maaser Sheni 5:12), the poor tithe REUSED at 26:12 (a second entry); at the counter's day, no marker",
        'covenant_formula_declared': "Deut 26:16-19: the statutes this day, the mutual declaration — STATUSES (NEW; no spine row, Onkelos and the ink), high above all nations, a holy people — HEAVEN entries (NEW; conditional in blessings_for_hearing's form; the two AS_WHEN pointers run citations); at the counter's day, no marker",
        'stones_altar_declared': "Deut 27:1-8: the great stones, the plaster and the writing, the whole stones, the offerings, very plainly — STATUSES (NEW; the command ours, the act Joshua's off the tape; Sotah 7:5's seventy languages a parameter), iron on the altar — a BLOCK (NEW; Exodus 20:25's second seat), the rejoicing REUSED at 27:7 (the source seat — a fourth entry); at the counter's day, no marker",
        'people_this_day_declared': "Deut 27:9-10: became the LORD's people this day, hearken and do — STATUSES (NEW; the second frame the speaker); at the counter's day, no marker",
        'gerizim_ebal_tribes_declared': "Deut 27:11-13: the six on Gerizim to bless, the six on Ebal for the curse — STATUSES (NEW; the ink's own lists the fields; the ceremony's form and the place three ways by call to blessing_and_curse; gerizim_ebal_ceremony_owed the DEBIT UNMOVED, open to Joshua's run); at the counter's day, no marker",
        'twelve_curses_declared': "Deut 27:14-26: the Levites' loud voice, the twelve cursed, Amen answered — fourteen STATUSES (NEW; each curse a reference to a compiled law by call; the persons no entities, the bench scene owed; Sotah 7:2, 7:5); at the counter's day, no marker",
        'blessings_condition_declared': "Deut 28:1-6: the city and the field, the womb, the ground and the beast, the basket and the trough, coming in and going out — HEAVEN entries (NEW; the state row's first arm; 28:3 the receipt's referent — the pointer 15:6 PAID), blessings_for_hearing REUSED at 28:1 (a third entry); at the counter's day, no marker",
        'enemies_storehouses_blessing_declared': "Deut 28:7-8: the enemies flee seven ways, the storehouses blessed — HEAVEN entries (NEW; Leviticus 26:7-8 by call); at the counter's day, no marker",
        'holy_people_fear_declared': "Deut 28:9-10: established a holy people, the peoples fear — HEAVEN entries (NEW; 'as He swore to you' a run citation of the oath by kind); at the counter's day, no marker",
        'heavens_treasure_lending_declared': "Deut 28:11-14: the heavens' treasure, lend not borrow, the head not the tail — HEAVEN entries (NEW), turning aside — a BLOCK (NEW; 148:7's row), rain_in_its_season REUSED at 28:12 (a second entry — the rain state's blessing seat); at the counter's day, no marker",
        'curses_condition_declared': "Deut 28:15-19: the curses for not hearkening and the four twins — HEAVEN entries (NEW; the state row's second arm, 28:1's negation sixteen in order); at the counter's day, no marker",
        'curse_diseases_brass_declared': "Deut 28:20-24: the curse, the confusion and the rebuke, the pestilence, the seven diseases, the brass heavens, the rain to dust — HEAVEN entries (NEW; Leviticus 26:16 and 26:19 by call; the curses' scope a parameter by 43:28); at the counter's day, no marker",
        'defeat_carcass_boil_madness_declared': "Deut 28:25-29: smitten before the enemies, the carcass, the boil of Egypt, the madness — HEAVEN entries (NEW; Exodus 9's boil by call; the ketiv and the qere a DATA row); at the counter's day, no marker",
        'wife_house_vineyard_king_taken_declared': "Deut 28:30-37: the wife, the house and the vineyard, the ox, the ass and the flock, the sons and daughters, the fruit, the sore boils, the king exiled, the byword — HEAVEN entries (NEW; 20:5-7's exemptions inverted, 17:14's king exiled by call); at the counter's day, no marker",
        'harvests_failed_stranger_head_declared': "Deut 28:38-44: the seed, the vines and the olives, the captivity, the stranger the head — HEAVEN entries (NEW; 7:13's list undone; 28:12-13 and 15:6 inverted by call); at the counter's day, no marker",
        'curses_pursue_iron_yoke_declared': "Deut 28:45-48: the curses pursue, the iron yoke, the enemies served in want — HEAVEN entries (NEW; Leviticus 26:13 inverted; the labor's third state a parameter by 42:8); at the counter's day, no marker",
        'eagle_nation_siege_declared': "Deut 28:49-52: the eagle nation, the siege in all the gates — HEAVEN entries (NEW; 20:19-20's siege law turned; Leviticus 26:25 by call); at the counter's day, no marker",
        'sons_flesh_siege_declared': "Deut 28:53-57: the sons' flesh in the siege — a HEAVEN entry (NEW; Leviticus 26:29's twin by call; Jeremiah 19:9 a pointer ahead owed); at the counter's day, no marker",
        'plagues_scattered_declared': "Deut 28:58-64: the plagues made wonderful, the diseases of Egypt returned, few in number, scattered among all peoples, serving wood and stone — HEAVEN entries (NEW; Exodus 15:26 turned, Leviticus 26:33 and 4:27-28 by call; the false six a DATA row); at the counter's day, no marker",
        'trembling_ships_covenant_declared': "Deut 28:65-69: the trembling heart, the life in doubt, the ships, sold and none buys — HEAVEN entries (NEW; 28:68 the run citation of 17:16), the covenant's words in Moab — a STATUS (NEW; the register's footer, its block's class DAEMONS computed); at the counter's day, no marker"}
assert set(NOTE) == set(S.KINDS)
if f'  {DM}:' not in text:
    lines = []
    for kind, first, rng, claim, cell, fields, effs, reuses in S.LINES:
        ws = [e for e, _ in effs] + [e for e, _ in reuses]
        lines.append('      %s: [%s]   # %s\n' % (kind, ', '.join(ws), NOTE[kind]))
    block = (f'  {DM}:\n    file: cold_run_{R}.py\n    wraps: {R}\n    given_at: Deut 26:1\n'
             '    installed_by: boot   # THE DEUTERONOMY WALK 18b (2026-09-26; THE LEAN PASS): "WHEN YOU COME INTO THE LAND … AND POSSESS IT AND DWELL IN IT" — the three chapters\' first verse at the counter\'s day (40, 11, 1); installed by boot like law_opening_speech through law_persons_poor_court (the Deuteronomy daemons\' form; THE INSTALL HYPOTHESIS on the table unchanged); ONE daemon over THREE chapters and five units — the first fruits\' recital, the tithe\'s confession and the twelve curses its three NEW families; the watches the twenty-one lines\' writes, new and reused (13b\'s form)\n'
             '    watches:\n' + ''.join(lines))
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if f'\n  {R}:   # THE DEUTERONOMY WALK 18b' not in text:
    fb = f'  {R}:   # THE DEUTERONOMY WALK 18b (2026-09-26; LEAN — three chapters, five units, one daemon)\n' + ''.join('    %s: {status: WRAPPED, by: %s}\n' % (c, DM) for c in CELLS)
    i = text.index('  persons_poor_court:   # THE DEUTERONOMY WALK 17b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(text)
NW = sum(len(l[6]) + len(l[7]) for l in S.LINES)
assert DM in dd['daemons'] and R in dd['functions'] and len(dd['functions'][R]) == 11 and len(dd['daemons'][DM]['watches']) == 21 and sum(len(v) for v in dd['daemons'][DM]['watches'].values()) == NW == 96, (len(dd['functions'].get(R, [])), len(dd['daemons'].get(DM, {}).get('watches', {})), NW)
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']; ev = yaml.safe_load(open(f"{ROOT}/World/step9/event_vocabulary.yaml", encoding='utf-8'))['events']
for k, v in dd['daemons'][DM]['watches'].items():
    assert k in ev, k
    for e in v: assert e in fx, e
print('daemons: %d (%s %s); functions blocks: %d; the watches %d writes over 21 lines' % (len(dd['daemons']), DM, DM in dd['daemons'], len(dd['functions']), NW))
# ---- the dependency span (three ranges) + the CALL edges by the ink (thirty-four REFERENCE; the token-demanded edges and the five AS_WHEN pointers after the gate's print) + THE OWED POINTER PAID ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
REF = [
 ('food_tithe', "26:12-15's removal and confession are 14:22-29's third year — THE CELL READ THESE VERSES FORWARD ('26:12 ahead the confession's seat'; FT.the_third_year('the_removal_date', 'the_measures', 'the_four_in_want', 'one_tithe_not_two') CALLED — the parameter on file, this runner exercising it); 26:11's rejoicing FT.the_far_place('the_rejoicing') by I2 with 27:7 (the Sifrei 107:16); 26:14's dead FT.the_sons_and_the_cuttings('for_the_dead') — 14:1 and 26:14 the book's two seats; 28:43's sojourner ('the_resident_alien_at_the_gate'); 26:18-19's holy people ('the_holy_people'); the readback rows 26:11-15, 28:43 the kin by CALL"),
 ('release_firstborn', "28:1's hearkening is 15:5's fourteen of seventeen in order (RF.the_needy_and_the_blessing('the_hearkening') CALLED — blessings_for_hearing REUSED a third time); 28:12's lending 15:6's twin with 'lend' for 'pledge' and 28:44 the reversal ('lend_not_borrow'); 28:3 THE RECEIPT'S REFERENT ('the_receipts_referent_ahead' — 'answered by 28:3 … a verse not yet spoken'): THE POINTER 15:6 PAID here, its H row graded up to a reference by CALL; 28:68's 'sold and none buys' 15:12's slave inverted (RF.the_hebrew_slave); the readback rows 28:1-3, 28:12, 28:44, 28:68 the kin by CALL"),
 ('blessing_and_curse', "27:11-13's Gerizim and Ebal are 11:29-30's — THE CELL READ THIS SEAT FORWARD ('27:11-13 the form's seat ahead'; BC.the_blessing_and_the_curse('gerizim_and_ebal', 'the_ceremonys_form', 'the_ceremonys_tongue', 'the_ceremonys_day', 'the_place_three_ways') CALLED — the parameters on file; gerizim_ebal_ceremony_owed the DEBIT UNMOVED); 28:12's rain and 28:24's dust the rain state's two arms (BC.the_second_paragraph('the_rain_in_its_season', 'the_heavens_shut', 'the_rains_dates') — rain_in_its_season REUSED); 28:15's condition ('the_curse_if'); the readback rows 27:2, 27:11-14, 28:12, 28:15, 28:24 the kin by CALL"),
 ('seven_nations', "26:18-19's treasured and holy people are 7:6's (SN.the_holy_people('holy_people', 'the_oath') CALLED — treasured_people UNMOVED; 28:9's 'as He swore' the oath by kind); 28:4, 11, 18, 51's list is 7:13's (SN.because_you_hear('the_blessing_list', 'no_barren', 'covenant_kept') — blessings_for_hearing's own row '28:4, 11, 18, 51 forward'); 28:22 and 28:60's diseases 7:15's turned ('the_diseases' — '28:60 forward'); 27:15's abomination 7:25-26's formula; the readback rows 26:18-19, 28:4, 28:9, 28:11, 28:18, 28:22, 28:51, 28:60 the kin by CALL"),
 ('place_name', "26:2 and 26:11's place, the eating and the rejoicing are 12:5-7's (PN.the_place_chosen('the_three_commandments_of_the_entry', 'the_stations_six_rows', 'eat_there_and_rejoice') CALLED — rejoicing_before_the_lord_commanded's FIRST entry, the reference; the Sifrei 63:9 naming the first fruits in 12:6's 'offering of your hand'); 26:14's warning 12:17's grounded by 26:14 (PN.the_profane_slaughter('the_impure_tithes_warning') — the Sifrei 72:5); the readback rows 26:2, 26:11, 26:14 the kin by CALL"),
 ('festivals_judges', "26:11 and 27:7's rejoicing are 16:11 and 16:14's (FJ.the_three_pilgrimages('the_three_times', 'not_empty') CALLED — Peah 1:1's appearing without measure; the Sifrei 138:1 borrowing 27:7 by I2); 27:19 and 27:25's judgment and bribe 16:19's (FJ.the_judges_in_every_gate('wrest_no_judgment', 'take_no_bribe') — bribe_barred ONE UNMOVED); the readback rows 26:11, 27:7, 27:19, 27:25 the kin by CALL"),
 ('persons_poor_court', "27:19's triad is 24:17's (PP.fathers_and_sons('the_strangers_and_the_orphans_justice') CALLED — stranger_orphan_justice_commanded ONE UNMOVED); 27:20's father's wife 23:1's own words (PP.the_fathers_wife_and_the_assembly('his_fathers_wife_and_his_fathers_skirt') — fathers_wife_barred ONE UNMOVED); 27:14's tongue lent to 25:9's formula by I2 (the Sifrei 291:5); 28:31's ox 22:1-4's lost ox inverted; the readback rows 27:19-20, 28:31 the kin by CALL"),
 ('refuge_war_family', "27:17's landmark is 19:14's (RW.the_landmark_and_the_witnesses('the_landmark_of_the_first_ones') CALLED — landmark_removal_barred ONE UNMOVED); 28:30's wife, house and vineyard 20:5-7's exemptions INVERTED (RW.the_priests_speech('the_four_exemptions')); 27:24's secret smiter and 27:25's innocent blood 19:10-13 and 21:8's (RW.the_murderer); 28:26's carcass 21:23's burial inverted; 28:52's siege 20:19-20's turned; the readback rows 27:17, 27:24-25, 28:26, 28:30, 28:52 the kin by CALL"),
 ('sanctions', "27:20-23's four unions are Leviticus 18:8, 18:23, 18:9 and 18:17's with 20:11-17's grades (SA.grade('fathers_wife', 'sister', …) CALLED — neither release nor levirate, the karet class); 27:16's dishonorer the curser's mode (SA.curser('mode', 'one_parent') — stoning, either parent suffices); the readback rows 27:16, 27:20-23 the kin by CALL"),
 ('mishpatim_3', "27:16's dishonorer of father and mother is Exodus 21:17's curser at its first seat (M3.parent_curser CALLED — the first seat of Leviticus 20:9's clause, into sanctions); 27:24's secret smiter Exodus 21:12's killer (M3.killer); the readback rows 27:16, 27:24 the kin by CALL"),
 ('holiness', "27:18's blind misled is Leviticus 19:14's stumbling block (HO.conduct('stumbling') CALLED — the one blind IN THE MATTER, the corrupt advice; the plain blind on the road this seat's own); 27:19's judgment Leviticus 19:15's; the readback rows 27:18-19 the kin by CALL"),
 ('second_tablets', "27:19's orphan and widow are 10:18's (ST.the_god_of_gods_and_the_stranger('the_orphan_and_the_widow') CALLED); 26:5 and 28:62's 'few in number' 10:22's seventy (ST('seventy_persons') — the Joseph runner's count by CALL); 28:69's 'words of the covenant' Exodus 34:28's other seat (ST.the_second_tablet); the readback rows 26:5, 27:19, 28:62, 28:69 the kin by CALL"),
 ('courts_prophet', "28:36's king exiled is 17:14-15's king (CP.the_king('the_three_limits_for_himself', 'the_copy_of_the_law') CALLED — king_from_the_brothers_commanded the tape's); 28:68's return to Egypt THE RUN CITATION OF 17:16 (return_to_egypt_barred ONE UNMOVED — the fifth AS_WHEN pointer); 27:3, 27:26 and 28:58's 'words of this law' 17:19's copy; 28:14's 'right or left' 17:11 and 17:20's; the readback rows 27:3, 27:26, 28:14, 28:36, 28:58, 28:68 the kin by CALL"),
 ('obey_horeb', "28:36 and 28:64's wood and stone are 4:28's — THE CELL READ THESE VERSES FORWARD ('28:36 and 28:64 forward'; OH.the_exile_case('serve_wood_and_stone', 'perish_and_scatter') CALLED — Leviticus 26:33's scattering by CALL, no entry written there); 27:15's image 4:16-18's list (OH.no_image); 28:69's covenant 4:10's declared; the readback rows 27:15, 28:36, 28:64, 28:69 the kin by CALL"),
 ('good_land', "28:15, 45 and 62's 'not hearken to the voice' are 8:19-20's testimony (GL.the_testimony('hearken_plural', 'like_the_nations') CALLED — its own forward reading; perishing_testified and forgetting_warned the tape's); 28:3-6's eating and satisfaction 8:10's (bless_after_eating_commanded ONE UNMOVED); 27:3's milk and honey GL.narrative; the receipt finder's own count receipt_seats(26..28) -> [], [], [] — NO receipt in the three chapters, the register file untouched; the readback rows 27:3, 28:15, 28:20, 28:45, 28:62 the kin by CALL"),
 ('covenant_at_horeb', "27:16's honor of father and mother is 5:16's fifth word (CH.the_second_tablet('the_fifth_word', 'the_reward_clause') CALLED — the honor and the fear by holiness.frame); 27:15's image 5:8's second word; 27:10's four verbs 5:1's (CH.the_assembly_called('hear_learn_keep_do')); 26:8's mighty hand and outstretched arm 5:15's; 28:69's Horeb 5:2's covenant; the readback rows 26:8, 27:10, 27:15-16, 28:69 the kin by CALL"),
 ('hear_o_israel', "27:3's 'as the LORD God of your fathers spoke to you' is 6:3's kin eight in order — the third AS_WHEN pointer, a RUN CITATION (HI.the_creed CALLED); 26:16's 'with all your heart and all your soul' 6:5's pair; 27:2-4's stones REFUSED as a source for the doorposts (HI.the_four_duties('mezuzah_writing') — 'not the stones', the Sifrei 36:2 — the stones an act for the hour); the readback rows 26:16, 27:2-4 the kin by CALL"),
 ('decalogue', "27:5-6's altar of stones without iron is Exodus 20:24-25's (DC.altar_rules('hewn_stones', 'build_recipe', 'steps') CALLED — WRAPPED by law_ordinances: iron-touched stone DISQUALIFIED, Mishnah Middot 3:4; the frame, the whole stones, the lime); 27:15's graven image Exodus 20:4's one shared token; the readback rows 27:5-6, 27:15 the kin by CALL"),
 ('ordinances', "28:3-6's house blessed is Exodus 23:25-26's bread and water blessed, no barren (OR.land CALLED — the innards, no worm nor rot); 28:31's ox slain and ass robbed Exodus 23:4-5's returned beasts inverted (OR.courts); 27:25's bribe Exodus 23:8's block written at 16:19; the readback rows 28:3-6, 28:31 the kin by CALL"),
 ('exodus_story', "26:6-8's recital retells Exodus 1:11-14's bondage, 2:23's cry and 12:51's going out (ES.sinai, ES.plagues CALLED — enslaved TWO, cry_heard TWO, plague_struck THIRTEEN the tape's UNMOVED: a retelling is a reference row, never a second act); 26:18's treasured people Exodus 19:5-6's offer (covenant_offered the tape's — the first AS_WHEN pointer); 28:27 and 28:35's boil Exodus 9:9-10's; 28:60's diseases Exodus 15:26's healer turned (healer_promised the tape's); the readback rows 26:5-8, 26:18, 28:27, 28:35, 28:60 the kin by CALL"),
 ('korach', "26:2 and 26:10's first fruits are Numbers 18:13's grant to the priest (KO.the_gifts('bikkurim', 'the_best_triad') CALLED — holy while attached, partners liable, outside the land exempt, Chullin 136a); 26:13's Levite's tithe and the order of the tithes Numbers 18:21-32's (KO.the_tithe('confession', 'wrong_order', 'from_it', 'kind_for_kind') — the same Mishnah at the Numbers seat); the readback rows 26:2, 26:10, 26:13 the kin by CALL"),
 ('calendar', "26:2's 'the first of all the fruit' is Exodus 23:19's first fruits' first-ness (CA.first_fruits CALLED — 'the ink here states first-ness, not the species table: WHICH species is the transmitted list', Mishnah Bikkurim 1:3 — the_species a PARAMETER fetched); the two calendar parameters the_first_fruits_window and the_confessions_hour on the calendar's keys (atzeret, sukkot_1, passover_7); the readback rows 26:2, 26:10 the kin by CALL"),
 ('chukat', "26:7's 'and we cried to the LORD' is Numbers 20:16's clause in the Edom letter — the two seats alone (CK.edom_and_hor('firstfruits_clauses') CALLED — 'at Num 20:16 and Deut 26:7 alone'); the readback row 26:7 the kin by CALL"),
 ('tochacha', "28:15-68's curses restate Leviticus 26 — THE TWIN DIFFED AT EVERY INVERSION (TC.cascade(refusals) CALLED — the five gates with the seven's multiplier: 26:16's consumption and fever at 28:22, 26:19's iron heavens INVERTED at 28:23, 26:25's gathered cities at 28:52, 26:26's eating unsatisfied at 28:19, 26:29's sons' flesh at 28:53, 26:33's scattering at 28:64 — land_desolate and scattered_among_nations ZERO UNMOVED, the transfer never fired; TC.covenant(walk, keep, do) — the blessing branch's terms: 26:7-8's five and a hundred at 28:7, 26:13's yoke broken INVERTED at 28:48; TC.measures — the good and harsh measures); the readback rows 28:7, 28:19, 28:22-23, 28:33, 28:38-42, 28:48-53, 28:64-65 the T4 rows against the Leviticus cells"),
 ('naso', "27:12's 'to bless' with 27:14's 'answer and say' is the priests' blessing in the holy tongue by bless/bless (NS.blessing('language') CALLED — Mishnah Sotah 7:2, Babylonian Talmud Sotah 33b: the same row the recital and the ceremony share; Numbers 6:22-27's Name); the readback rows 27:12, 27:14 the kin by CALL"),
 ('joseph', "26:5's 'few in number' is Genesis 46:27's seventy (JO.seventy CALLED — the recital's descent; 47:4's sojourn 'to sojourn in the land'; 28:62's echo); the readback rows 26:5, 28:62 the kin by CALL"),
 ('primeval', "27:12's Gerizim by Shechem and the oaks of Moreh is Genesis 12:6's — THE MISHNAH'S OWN ANALOGY (Sotah 7:5 with 11:30 by I2; PV.call CALLED for Abram's Shechem); 28:62's stars Genesis 15:5's (seed_as_stars THREE the tape's UNMOVED); the readback rows 27:12, 28:62 the kin by CALL"),
 ('seducers', "27:15 and 27:24's 'in secret' are 13:7's inciter in secret — the curses' KEY (SE.the_inciter CALLED — what no court sees; 28:57 the book's fourth); 28:54 and 28:56's 'wife of his bosom' 13:7's phrase (Onkelos 'the wife of his covenant'); the readback rows 27:15, 27:24, 28:54-57 the kin by CALL"),
 ('borders', "27:12-13's two lists of six against Numbers 34:16-29's roster — the tribes' orders compared as a DATA row, no link of our own (BR.the_roster CALLED — Reuben first on Ebal, Simeon first on Gerizim; Dan no entity on the tape); the readback rows 27:12-13 the kin by CALL"),
 ('priesthood', "26:13's 'the holy' removed from the house and 26:14's holy things are the priests' portions' class (PR.holy_food CALLED — Leviticus 22's holy food; the terumah and the terumah of the tithe to the priest, Maaser Sheni 5:6); 26:3-4's priest 'who is in those days'; the readback rows 26:3-4, 26:13 the kin by CALL"),
 ('chatat', "26:14's 'I have not eaten of it in my mourning' grounds the mourner's share by the a fortiori — Leviticus 10:19's Aaron (CT.share('onen') CALLED — 'the a fortiori from 26:14 for the holy of the generations'; the Sifrei 303:15); the readback row 26:14 the kin by CALL"),
 ('opening_speech', "27:8's 'very plainly' is 1:5's root 'Moses began to explain this law' — the book's two seats (OS.lemma_seats CALLED — Onkelos 'explained well' at both); the readback row 27:8 the kin by CALL"),
 ('journeys', "27:15's graven and molten image against Numbers 33:52's 'destroy all their images' — the images' word on the tape's own line at the entry (JR.the_command CALLED — the land's images at the border); the readback row 27:15 the kin by CALL"),
 ('sanctuary_build', "27:5-6's altar of whole stones against Exodus 27:1-8's bronze altar — THE CONTRAST (SB.altar CALLED — the Tabernacle's spec, this the field altar of the hour; no wood, no bronze, whole stones); the readback rows 27:5-6 the kin by CALL"),
]
assert len(REF) == 34 and len({t for t, _ in REF}) == 34 and [t for t, _ in REF] == S.EDGES, ([t for t, _ in REF][:5], S.EDGES[:5])
if f'\n  {R}:' not in text.split('\nedges:')[0]:
    a = "  persons_poor_court: [[Deut, 22, 1, 29], [Deut, 23, 1, 26], [Deut, 24, 1, 22], [Deut, 25, 1, 19]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + f"  {R}: [[Deut, 26, 1, 19], [Deut, 27, 1, 26], [Deut, 28, 1, 69]]   # THE DEUTERONOMY WALK 18b (2026-09-26; DEUTERONOMY_WALK.md \"Sitting 18b\" — LEAN): chapters 26-28 in ONE runner (the span three ranges — persons_poor_court's four-range form read for three) — THE FIRST FRUITS, THE REMOVAL AND THE CONFESSION, THE COVENANT FORMULA, THE STONES AND THE ALTAR, THE PEOPLE THIS DAY, THE SIX AND THE SIX, THE TWELVE CURSES, THE BLESSINGS, THE CURSES OF THE HOUSE AND THE FIELD, THE CURSES OF THE SIEGE AND THE EXILE — twenty-one own-day lines at the counter's day (40, 11, 1), no marker; the daemon law_firstfruits_ebal_curses given_at Deut 26:1, installed_by boot; the five units deu_26_bikkurim_close, deu_27_ebal_curses, deu_28_blessings, deu_28_curses_a, deu_28_curses_b\n" + text[j + 1:]
    edges = ''.join("  - {from: %s, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: %s}\n" % (R, to, q(W + why)) for to, why in REF)
    k = text.rfind('  - {from: persons_poor_court, to: '); e = text.index('\n', text.index('why:', k)) + 1
    text = text[:e] + edges + text[e:]
# THE OWED POINTER PAID — Deut 15:6 AS_WHEN (release_firstborn) OWED hypothesis -> RUN_CITATION reference: the referent 28:3 now on the tape as this runner's heaven entry blessed_in_city_and_field
old = '{verse: "Deut 15:6", form: AS_WHEN, runner: release_firstborn, disposition: OWED, link: hypothesis, why: "THE RECEIPT\'S THIRD AND FOURTH SHAPES | THE DEUTERONOMY WALK 13b (2026-09-23):'
if old in text:
    assert text.count(old) == 1
    text = text.replace(old, '{verse: "Deut 15:6", form: AS_WHEN, runner: release_firstborn, disposition: RUN_CITATION, link: reference, why: "' + W + 'PAID at chapters 26-28\'s compile: the receipt\'s referent 28:3 \'blessed shall you be in the city and blessed in the field\' is NOW SPOKEN — cold_run_firstfruits_ebal_curses.py writes blessed_in_city_and_field on Israel at 28:1\'s line; the Sifrei on Deuteronomy 116:1 (read whole at sittings 13 and 18) the teacher: \'and what did He speak to you? blessed are you in the city\'; the readback\'s POINTER ROW at 28:3 grades 15:6\'s H row up to a reference by CALL (release_firstborn.the_needy_and_the_blessing(\'the_receipts_referent_ahead\')); the disposition RUN_CITATION — the receipt citing its spec ahead of it (the design\'s word REVERSE is an edge\'s disposition, the gate\'s pointer branch admits none — a departure recorded); the hypothesis CLOSED, OWED 0 in the file | THE RECEIPT\'S THIRD AND FOURTH SHAPES | THE DEUTERONOMY WALK 13b (2026-09-23):')
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(text)
n_ch = sum(1 for e in dep['edges'] if e['from'] == R); n_tr = sum(1 for e in dep['edges'] if e['from'] == R and e.get('link') == 'transfer')
missing = [e['to'] for e in dep['edges'] if e['from'] == R and e['to'] not in dep['spans']]
p156 = [p for p in dep['pointers'] if p.get('verse') == 'Deut 15:6' and p.get('runner') == 'release_firstborn']
owed = [p for p in dep['pointers'] if p.get('disposition') == 'OWED']
assert R in dep['spans'] and dep['spans'][R] == [['Deut', 26, 1, 19], ['Deut', 27, 1, 26], ['Deut', 28, 1, 69]] and n_ch == 34 and n_tr == 0 and not missing, (dep['spans'].get(R), n_ch, n_tr, missing)
assert len(p156) == 1 and p156[0]['disposition'] == 'RUN_CITATION' and p156[0]['link'] == 'reference' and not owed, (p156, len(owed))
print('dependency: the span (three ranges) + %d edges (%s %d CALL — all reference; the token-demanded edges and the five AS_WHEN pointers after the gate\'s print); THE OWED POINTER Deut 15:6 PAID: RUN_CITATION reference (OWED pointers in the file: %d); edges %d, pointers %d' % (n_ch, R, n_ch, len(owed), len(dep['edges']), len(dep['pointers'])))
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
old = "len(real) == 79 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 17b (2026-09-26; LEAN): 78 -> 79,"
if old in text:
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 80 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 18b (2026-09-26; LEAN): 79 -> 80, law_firstfruits_ebal_curses (given_at Deut 26:1 — when you come into the land and dwell in it; installed_by boot; one daemon over three chapters and five units); 17b: 78 -> 79,")
    if not CHECK: open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 80" in text
print('installation_probes I5: 80')
# ---- THE TWO CALENDAR PARAMETERS (the received channel — clock data on the calendar's keys, no marker, no timer) + the_removal_date's exercised_by ----
path = f"{ROOT}/World/step9/calendar_parameters.yaml"
text = open(path, encoding='utf-8').read()
if '\n  the_first_fruits_window:' not in text:
    rows = ('''  the_first_fruits_window:   # THE DEUTERONOMY WALK 18b (2026-09-26): 'you shall take of the first of all the fruit of the ground … and say: I declare this day' (Deut 26:2-3) — THE WINDOW OF THE FIRST FRUITS A CLOCK DATUM: from Shavuot to the Feast brings and recites, from the Feast to Chanukah brings and does not recite, not before Shavuot; on the calendar's own keys; no marker, no timer on the tape
    era: exodus
    idiom: the_first_fruits_window
    value:
      recites: "FROM SHAVUOT TO THE FEAST — the key atzeret (the fiftieth day from the omer) to the key sukkot_1 (the fifteenth of the seventh month): brings and recites (Mishnah Bikkurim 1:6, 1:10; the Sifrei 299:1-4 — 'I declare this day' once a year)"
      brings_without_reciting: "FROM THE FEAST TO CHANUKAH — from sukkot_1 to the twenty-fifth of the ninth month (the answer sheet's season, no key of the ink's): brings and does not recite; R. Judah ben Betera — recites (the two arms recorded, Bikkurim 1:6)"
      not_before: "NOT BEFORE SHAVUOT — the men of Mount Zevoim brought before Shavuot and were refused (Bikkurim 1:3); the species by the two loaves' analogy (I2, checked in MIDDOT.md — the Sifrei 297:4-5)"
      the_year: "the tithes' new year beside it — the_tithes_new_year (food_tithe's row) by CALL; the seventh year's fruit no first fruits (the sabbatical by CALL to yovel)"
    boundary: "a clock datum, not a marker — the window read on the calendar's own keys (atzeret, sukkot_1) in the count's year; on the bare world before the entry the count is not begun — the cell's verdict 'no count' (13b's precedent)"
    channel: received
    source: "Deut 26:1-11; Exodus 23:19, 34:26; Numbers 18:13; Mishnah Bikkurim 1:3, 1:6, 1:10; the Sifrei on Deuteronomy 297:4-9, 299:1-4"
    teacher: "Mishnah Bikkurim 1:6, 1:10"
    exercised_by: [firstfruits_ebal_curses]
  the_confessions_hour:   # THE DEUTERONOMY WALK 18b (2026-09-26): 'when you have finished tithing … you shall say before the LORD your God: I have removed the holy from the house' (Deut 26:12-13) — THE CONFESSION'S HOUR A CLOCK DATUM: at minchah on the last festival day of Passover of the fourth and the seventh year, on the removal's own keys; no marker, no timer on the tape
    era: exodus
    idiom: the_confessions_hour
    value:
      the_hour: "AT MINCHAH ON THE LAST FESTIVAL DAY — the key passover_7 (the removal's own key, the_removal_date's eve the day before) in the count's fourth and seventh year (Mishnah Maaser Sheni 5:10 — 'at minchah on the last festival day they would confess')"
      the_date_by_call: "the removal's date READ BY CALL to food_tithe.the_third_year('the_removal_date') — the row the_removal_date on this file (Maaser Sheni 5:6; the Sifrei 302:1 — the end-analogy with 31:10 REFUSED by the verse's own 'finished')"
      the_tongue: "IN ANY LANGUAGE (Mishnah Sotah 7:1 — the confession among the seven said in any tongue; the recital in the holy tongue, 7:2 — one parameter two arms)"
      the_confessors: "Israelites and mamzerim confess, not converts nor freed slaves (no share in the land); R. Meir — not priests and Levites; R. Yose — the Levitical cities (Maaser Sheni 5:14 — three arms)"
    boundary: "a clock datum, not a marker — the hour minchah of passover_7 by the calendar's own keys in the count's fourth and seventh year, the year's class read by call; on the bare world before the entry the count is not begun — 'no count'"
    channel: received
    source: "Deut 26:12-15, 14:28-29; Mishnah Maaser Sheni 5:6, 5:10-14; Mishnah Sotah 7:1; the Sifrei on Deuteronomy 302:1, 303:1-20"
    teacher: "Mishnah Maaser Sheni 5:10"
    exercised_by: [firstfruits_ebal_curses]
''')
    i = text.index('\neras:\n')
    text = text[:i + 1] + rows + text[i + 1:]
old = "    teacher: \"Mishnah Maaser Sheni 5:6; Rosh Hashanah 12b:1-5\"\n    exercised_by: [food_tithe]\n"
if old in text:
    assert text.count(old) == 1
    text = text.replace(old, "    teacher: \"Mishnah Maaser Sheni 5:6; Rosh Hashanah 12b:1-5\"\n    exercised_by: [food_tithe, firstfruits_ebal_curses]   # THE DEUTERONOMY WALK 18b (2026-09-26): 26:12-15's confession reads the removal's date by CALL — the runner exercises the row\n")
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
cal = yaml.safe_load(text)['parameters']
assert 'the_first_fruits_window' in cal and 'the_confessions_hour' in cal and cal['the_removal_date']['exercised_by'] == ['food_tithe', 'firstfruits_ebal_curses'] and cal['the_first_fruits_window']['channel'] == 'received' and cal['the_confessions_hour']['exercised_by'] == [R], (cal['the_removal_date']['exercised_by'], [k for k in cal if k.startswith('the_')][-4:])
print('calendar: %d parameters (the_first_fruits_window, the_confessions_hour added; the_removal_date exercised_by %s)' % (len(cal), cal['the_removal_date']['exercised_by']))
# ---- THE REGISTER FILE UNTOUCHED — no seat in the three chapters (the footer at 28:69 computed DAEMONS, undeclared) ----
rg = yaml.safe_load(open(f"{ROOT}/World/step9/register_dispositions.yaml", encoding='utf-8'))
seats = [k for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut 2[678]:', str(k))]
assert seats == [], seats
print('register: untouched (no seat at Deut 26-28; footers %d)' % len(rg.get('footers', {})))
print('TYPES B OK' + (' (check)' if CHECK else ''))
