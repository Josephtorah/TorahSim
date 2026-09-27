import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b — THE COMPILE OF CHAPTERS 19-21, LEAN (2026-09-25): THE TYPES BY SCRIPT, part B — daemon_dispositions (law_refuge_war_family — given_at
# Deut 19:1, installed_by boot; the functions block TEN WRAPPED: the nine cells and the_readback); dependency_dispositions (the span's THREE RANGES
# [[Deut, 19, 1, 21], [Deut, 20, 1, 20], [Deut, 21, 1, 23]] and TWENTY-THREE CALL edges by the ink, all REFERENCE — the census decides the rest); installation_probes
# I5 77 -> 78; NO calendar row; THE REGISTER FILE UNTOUCHED HERE (the one seat Deut 20:17 dispositioned at the tail from the gate's print — the class as the world says).
# add_types_ch17_b.py's form. RUN FROM THE REPO ROOT.
import yaml, subprocess, re
ROOT = _ROOT
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
W = "THE DEUTERONOMY WALK 16b (2026-09-25) | "
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_refuge_war_family:' not in text:
    block = '''  law_refuge_war_family:
    file: cold_run_refuge_war_family.py
    wraps: refuge_war_family
    given_at: Deut 19:1
    installed_by: boot   # THE DEUTERONOMY WALK 16b (2026-09-25; THE LEAN PASS): "WHEN THE LORD YOUR GOD CUTS OFF THE NATIONS" — the three chapters' first verse at the counter's day (40, 11, 1); installed by boot like law_opening_speech through law_courts_prophet (the Deuteronomy daemons' form; THE INSTALL HYPOTHESIS on the table unchanged); ONE daemon over THREE chapters and three units (courts_prophet's two-range form extended); THIRTEEN OWN-DAY LINES, NO marker; the readback's sixty-four rows one per verse graded against the kin's cells by CALL and the tape's lines by kind and first verse; no bench scene, no case kind (the lean form — the twenty-eight Mishnah rows the cells' asks)
    watches:
      refuge_cities_declared: [three_cities_separated_commanded, way_prepared_commanded, land_divided_in_three_commanded, three_more_cities_conditioned]   # Deut 19:1-3, 7-10: the three cities, the way, the border in three, the three more — STATUSES (NEW; the fourth a condition unmet); at the counter's day, no marker
      manslayer_and_murderer_declared: [manslayer_flight_permitted, murderer_extradition_commanded, murderer_pity_barred, innocent_blood_purge_commanded]   # Deut 19:4-6, 11-13: the flight, the extradition, the purge of the innocent blood — STATUSES (NEW), 'your eye shall not pity' — a BLOCK (NEW); the murderer's own verdict put_to_death (reused); at the counter's day, no marker
      landmark_declared: [landmark_removal_barred]   # Deut 19:14: the landmark — a BLOCK (NEW); at the counter's day, no marker
      witnesses_law_declared: [two_or_three_witnesses_required, witnesses_inquiry_commanded, plotting_witness_talion_commanded, talion_pity_barred]   # Deut 19:15-21: two or three, the inquiry, as he plotted — STATUSES (NEW), the talion's pity — a BLOCK (NEW); the plotting witnesses' own verdict the body effect of their plot; israel_hears_and_fears 13:12's the reference; at the counter's day, no marker
      war_speech_declared: [war_fear_barred, priest_war_speech_commanded, officers_exemptions_commanded, fearful_exemption_commanded, captains_appointed_commanded]   # Deut 20:1-9: 'fear them not' — a BLOCK (NEW); the priest's speech, the exemptions, the fearful, the captains — STATUSES (NEW; the exemptions' kinds parameters graded by Sotah 8); at the counter's day, no marker
      siege_law_declared: [peace_call_commanded, tribute_service_commanded, siege_males_smitten_commanded, spoil_permitted, far_cities_scope_declared]   # Deut 20:10-15: the peace call, the tribute, the males, the spoil, the far cities — STATUSES (NEW); at the counter's day, no marker
      seven_nations_herem_declared: [nothing_alive_left_commanded, abominations_teaching_barred]   # Deut 20:16-18: no breath left — a STATUS (NEW), the teaching — a BLOCK (NEW); the receipt 20:17 a run citation behind (nations_devoted 7:1-5); at the counter's day, no marker
      siege_trees_declared: [fruit_tree_cutting_barred, siege_works_permitted]   # Deut 20:19-20: the fruit tree — a BLOCK (NEW), the siege-work — a STATUS (NEW); at the counter's day, no marker
      heifer_rite_declared: [slain_found_measuring_commanded, heifer_neck_broken_commanded, priests_approach_commanded, elders_hands_washed_commanded, elders_declaration_commanded, innocent_blood_atoned]   # Deut 21:1-9: the measuring, the neck, the priests, the hands, the declaration — STATUSES (NEW), 'and the blood shall be atoned' — a HEAVEN entry (NEW; the Holy Spirit's answer); 21:9's purge 19:13's write referenced; at the counter's day, no marker
      captive_wife_declared: [captive_wife_permitted, captive_mourning_month_commanded, captive_sale_barred, captive_release_commanded]   # Deut 21:10-14: the wife, the month, the release — STATUSES (NEW), the sale — a BLOCK (NEW); at the counter's day, no marker
      firstborn_portion_declared: [firstborn_double_portion_commanded, firstborn_right_transfer_barred]   # Deut 21:15-17: the double — a STATUS (NEW; Bekhorot 8:9's measure), the transfer — a BLOCK (NEW; Bava Batra 8:5); at the counter's day, no marker
      rebellious_son_declared: [rebellious_son_seized_commanded, rebellious_son_stoning_commanded]   # Deut 21:18-21: the seizing, the stoning — STATUSES (NEW; Sanhedrin 8's parameters); the son's own verdict stoned with the evil purged (reused); israel_hears_and_fears the reference; at the counter's day, no marker
      hanged_burial_declared: [hanging_after_death_commanded, corpse_overnight_barred, same_day_burial_commanded, land_defilement_barred]   # Deut 21:22-23: the hanging after death, the burial — STATUSES (NEW), the night, the land — BLOCKS (NEW; Sanhedrin 6:4-5); the reviler's own verdict stoned, hanged and buried (reused); at the counter's day, no marker
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  refuge_war_family:   # THE DEUTERONOMY WALK 16b' not in text:
    fb = '''  refuge_war_family:   # THE DEUTERONOMY WALK 16b (2026-09-25; LEAN — three chapters, one daemon)
    the_cities_of_refuge: {status: WRAPPED, by: law_refuge_war_family}
    the_landmark_and_the_witnesses: {status: WRAPPED, by: law_refuge_war_family}
    the_priests_speech: {status: WRAPPED, by: law_refuge_war_family}
    the_siege: {status: WRAPPED, by: law_refuge_war_family}
    the_broken_necked_heifer: {status: WRAPPED, by: law_refuge_war_family}
    the_captive: {status: WRAPPED, by: law_refuge_war_family}
    the_firstborns_double: {status: WRAPPED, by: law_refuge_war_family}
    the_rebellious_son: {status: WRAPPED, by: law_refuge_war_family}
    the_hanged: {status: WRAPPED, by: law_refuge_war_family}
    the_readback: {status: WRAPPED, by: law_refuge_war_family}
'''
    i = text.index('  courts_prophet:   # THE DEUTERONOMY WALK 15b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_refuge_war_family' in dd['daemons'] and 'refuge_war_family' in dd['functions'] and len(dd['functions']['refuge_war_family']) == 10 and len(dd['daemons']['law_refuge_war_family']['watches']) == 13 and sum(len(v) for v in dd['daemons']['law_refuge_war_family']['watches'].values()) == 45, (list(dd)[:5])
print('daemons: %d (law_refuge_war_family %s); functions blocks: %d' % (len(dd['daemons']), 'law_refuge_war_family' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span (three ranges) + the CALL edges by the ink (twenty-three REFERENCE; the token-demanded edges and any pointer after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  refuge_war_family:' not in text.split('\nedges:')[0]:
    a = "  courts_prophet: [[Deut, 17, 1, 20], [Deut, 18, 1, 22]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  refuge_war_family: [[Deut, 19, 1, 21], [Deut, 20, 1, 20], [Deut, 21, 1, 23]]   # THE DEUTERONOMY WALK 16b (2026-09-25; DEUTERONOMY_WALK.md \"Sitting 16b\" — LEAN): chapters 19-21 in ONE runner (the span three ranges — courts_prophet's two-range form extended) — THE CITIES OF REFUGE, THE LANDMARK AND THE WITNESSES, THE PRIEST'S SPEECH AND THE OFFICERS' EXEMPTIONS, THE SIEGE, THE BROKEN-NECKED HEIFER, THE CAPTIVE, THE FIRSTBORN'S DOUBLE, THE REBELLIOUS SON, THE HANGED: the readback's rows one per verse graded against the kin's cells by CALL; THIRTEEN OWN-DAY LINES at the counter's day, no marker; the exam the twenty-eight Mishnah rows the ledger cites at least twice (no docket — the lean pass); twenty-three CALL edges, all REFERENCE\n" + text[j + 1:]
    REF = [
     ('place_name', "19:1 restates 12:29's opening seven words (the reading's kin assert; the Sifrei 179:1-2 — PN.the_nations_cut_off_and_the_abomination('when_the_lord_cuts_off_the_nations') CALLED); 21:9's 'what is right in the eyes of the LORD' 12:25's clause; the tape's nations_cut_off_warned at 12:29 the readback's REFERENCE"),
     ('obey_horeb', "19:2's three cities are 4:41-43's three beyond the Jordan by name (the Sifrei 180:1-4 with Makkot 2:4 — OH.the_cities_and_the_frame('then_moses_set_apart', 'not_until_all_six', 'the_manslayer_defined', 'the_three_names') CALLED; OH.DATA['the_three_cities'], ['the_manslayer_definition'] read); 19:4 = 4:42's words with 'smites' for 'slays'; cities_set_apart ONE on israel_people UNMOVED — referenced, not reused; the tape's three_cities_set_apart the readback's REFERENCE"),
     ('refuge', "19:1-13 is Numbers 35's law in Deuteronomy's words (the Sifrei 180-187 — RG.the_refuge_law('six_cities', 'for_whom', 'unwittingly', 'until_he_stands'), RG.the_murderer('the_iron', 'the_smiter', 'the_mode', 'the_intents', 'the_manners', 'the_avengers_hand'), RG.the_manslayer('the_border', 'the_return', 'not_his_enemy', 'the_deliverance', 'the_levite_exiled', 'the_honor') CALLED — the live calls; RG.DATA['the_one_witness'], ['the_avengers_hand'], ['the_lands_atonement'], ['the_court_of_twenty_three'], ['the_blind_killer'] read); flees_to_refuge, dwells_in_refuge, land_polluted_by_blood 0 on the running world UNMOVED (no killer on the tape); the readback rows 19:2-13 the kin by CALL"),
     ('ordinances', "19:4's 'from yesterday and the day before' is Exodus 21:29's goring-ox clock (the Bible's two seats — OR.courts('enemy_ox', 'who_is_enemy') CALLED for the hater); 19:16's 'a violent witness' Exodus 23:1's (OR.courts('witness_of_violence', 'false_report', 'one_vs_two', 'twenty_three') CALLED); the readback rows 19:4, 19:16 the kin by CALL"),
     ('courts_prophet', "19:15's one witness and two or three are 17:6-7's rule built as a father (the Sifrei 188:4-9, 190:3, 190:7 — CP.the_idolaters_trial('found_means_witnesses', 'the_seven_investigations', 'two_witnesses_for_every_death', 'one_witness_and_the_disciple_silent', 'the_witnesses_hand_first') CALLED; 15b's design named 19:15 forward — PAID here); 21:5's 'every dispute and every stroke' the high court's pairs (CP.the_high_court('the_pairs', 'the_three_courts')); 21:5's Levite who is a priest 208:1 = 168:1 (CP.the_levite_at_the_place('the_levite_who_is_a_priest')); 20:18's teaching 18:9's learning (CP.the_diviners('learn_to_understand_not_to_do')); one_witness_barred, two_witnesses_required, witnesses_hand_first_commanded, abominations_learning_barred ONE each on israel_people UNMOVED — referenced, not reused; the readback rows 19:15, 20:18, 21:5, 21:21 the kin by CALL"),
     ('seducers', "19:18's 'well' is 13:15's questionnaire (the Sifrei 190:7 — SE.the_city_heard_of_the_inquiry_and_the_sword('the_seven_interrogations', 'the_sword') CALLED); 21:21's stoning 13:10-11's rite and hand (SE.the_inciter('the_hand_first', 'the_stoning_rite')); the purge formula's fourth and fifth seats of nine (SE.the_readback('the_purge_formulas_nine_seats', 'the_two_verbs_of_stoning')); israel_hears_and_fears ONE on israel_people UNMOVED — 13:12's line the reference at 19:20 and 21:21 (the formula's third and fourth seats); the readback rows 19:18-20, 21:21 the kin by CALL"),
     ('festivals_judges', "19:17's 'the judges of those days' and 21:19's 'the elders of his city' are 16:18's courts and their three tiers (FJ.the_judges_in_every_gate('the_court_for_all_israel', 'the_three_tiers') CALLED — the three and the twenty-three of Sanhedrin 8:4); the readback rows 19:17, 21:19 the kin by CALL"),
     ('lev24', "19:21's 'eye in eye' is Leviticus 24:20's 'eye in place of eye' with the preposition changed (the reading's twin assert; the Sifrei 190:14-15 — LV.talion('eye') CALLED: PAY-MONEY, the substitution operator); the readback row 19:21 the kin by CALL"),
     ('seven_nations', "20:1's 'fear them not' is 7:18's (SN.do_not_fear('the_doubt', 'remember_pharaoh') CALLED); 20:16-17's six are 7:1-2's seven and their ban (SN.the_seven_nations('the_seven', 'the_ban', 'the_bans_condition')); 20:18's abominations 7:25-26's (SN.the_images_and_the_devoted('abomination_to_the_lord')); THE RECEIPT 20:17 'as the LORD your God commanded you' -> 7:1-5's nations_devoted BEHIND, a run citation; pity_barred TWO on israel_people UNMOVED (7:16's the first); the readback rows 20:1, 20:16-18 the kin by CALL"),
     ('midian', "20:2's priest anointed for war is Phinehas at Numbers 31:6 (Sotah 8:1 — MD.the_vengeance('phinehas_anointed_for_war', 'the_trumpets', 'war_clause') CALLED); 20:13-14's males and spoil Numbers 31:7-18's (MD.the_war('every_male', 'captives', 'spoil'), MD.the_sentence('every_female_kept', 'the_sentence', 'deuteronomy_20') — the cell's own ask naming this chapter); 20:11's tribute against 31:28's (MD.the_division('tribute_rate')); 21:10's captives Numbers 31:9's; taken_captive THREE and spoil_taken TWO UNMOVED; the readback rows 20:2, 20:11-14, 21:10 the kin by CALL"),
     ('opening_speech', "20:10's peace call is Sihon's messengers (the Sifrei 199:5 reread — 2:26's retelling of Numbers 21:21; OP.the_bypass('sihon_commanded', 'the_speech_resumed') CALLED; OP.DATA['the_ban'] read); the tape's sihon_war_commanded at 2:24 and messengers_sent_to_sihon at Numbers 21:21 the readback's REFERENCES; the readback row 20:10 the kin by CALL"),
     ('chukat', "21:3's heifer 'which has not been worked, which has not pulled in a yoke' is Numbers 19:2's red cow's twin 'which … no' (the reading's kin assert; the Sifrei 207 with Sotah 9:5 and Parah 1:1 — CK.heifer_rite('yoke', 'blemish', 'age') CALLED: a blemish disqualifies the cow, not the heifer); the tape's heifer_statute_given the readback's REFERENCE; the readback row 21:3 the kin by CALL"),
     ('incense_shekel', "21:8's 'atone for Your people' carries the ransom's word (Numbers 35:31-32, Deuteronomy 21:8 the seats — IS.shekel('atone_souls', 'ransom') CALLED: 'to atone for your souls' Exodus 30:15-16's); the readback row 21:8 the kin by CALL"),
     ('primeval', "21:14's 'since you have humbled her' is Genesis 16:6's word on Hagar (PV.hagar('affliction_reading') CALLED); the tape's afflicted at Genesis 16:6 the readback's REFERENCE; the readback row 21:14 the kin by CALL"),
     ('family', "21:17's double is Jacob's one portion to Joseph and Reuben's 'first of my strength' (the Sifrei 217:2-5 citing Genesis 48:22 and 1 Chronicles 5:1 — TAUGHT BY THE SPINE; FM.inheritance('one_portion', 'given_as_gift', 'gift_returns_dispute', 'held_not_due', 'birthright_run', 'firstborn_by_call'), FM.testament('firstborn_my_strength', 'excess_named_denied') CALLED); the tape's portion_given at 48:22 and testament at 49:3 the readback's REFERENCES; the readback rows 21:16-17 the kin by CALL"),
     ('zelophehad', "21:16-17's firstborn's double sits in Numbers 27:8-11's ladder (ZL.inheritance_order('source_of_rule', 'firstborn_double') CALLED — 'double in the father's property, in the held'); the tape's statute_declared at Numbers 27:6 the readback's REFERENCE; inheritance_stayed_in_tribe ONE UNMOVED; the readback row 21:17 the kin by CALL"),
     ('mamre', "21:17's 'the right of the firstborn' has its earliest run at Genesis 25:31-34's birthright sold (MM.twins('firstborn_sheet', 'sale_with_oath') CALLED — Bekhorot 8:1's firstborn by the head); firstborn_by_the_head TWO (esau, perez) UNMOVED; the readback row 21:17 the kin by CALL"),
     ('release_firstborn', "21:15's firstborn for inheritance is not 15:19's firstling for the priest — Bekhorot 8:1's four kinds (RF.the_firstling('consecrated_from_the_womb') CALLED: the priest's firstborn opens the womb, the inheritance's is the father's first); the readback row 21:15 the kin by CALL"),
     ('mekoshesh', "21:21's stoning is Numbers 15:35-36's rite — the stones and the stone, the hanging after (the Sifrei 220:1-2, 221:3 — MK.capital_procedure('stones_and_a_stone', 'hanging', 'burial', 'mode') CALLED); stoned TWO UNMOVED (the blasphemer, the wood-gatherer); the readback rows 21:21-22 the kin by CALL"),
     ('balak', "21:22's hanging is Numbers 25:4's 'hang them before the sun' (the idolaters after stoning — BK.peor('hang_before_the_sun', 'judges_count') CALLED); the tape's hanging_commanded at Numbers 25:4 the readback's REFERENCE; the readback row 21:22 the kin by CALL"),
     ('sanctions', "21:23's 'a curse of God' is the reviler's — Leviticus 24:15-16's blasphemer by the Name (the Sifrei 221:8 with Sanhedrin 6:4 — SA.curser('mode', 'by_the_name') CALLED); the tape's sentence_declared and stoned_as_commanded at Leviticus 24 the readback's REFERENCES; the readback row 21:23 the kin by CALL"),
     ('pre_sinai', "21:23's hanged man's blood is Genesis 9:6's 'by man shall his blood be shed' — the court's death (PS.noahide('bloodshed_seats', 'by_man') CALLED); blood_required ONE on noach UNMOVED (Genesis 9:5's heaven entry the readback's REFERENCE); the readback row 21:23 the kin by CALL"),
     ('good_land', "20:17 is the one receipt of the three chapters by the finder's own count (GL.receipt_seats(19) [], (20) [17], (21) [] CALLED — the register's seat); 19:8's 'as He swore to your fathers' the oath formula, no seat; the readback row 20:17 the receipt behind"),
    ]
    edges = ''.join("  - {from: refuge_war_family, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: %s}\n" % (to, q(W + why)) for to, why in REF)
    a = "  - {from: courts_prophet, to: family, disposition: FALSE, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'refuge_war_family'); n_tr = sum(1 for e in dep['edges'] if e['from'] == 'refuge_war_family' and e.get('link') == 'transfer')
missing = [e['to'] for e in dep['edges'] if e['from'] == 'refuge_war_family' and e['to'] not in dep['spans']]
assert 'refuge_war_family' in dep['spans'] and dep['spans']['refuge_war_family'] == [['Deut', 19, 1, 21], ['Deut', 20, 1, 20], ['Deut', 21, 1, 23]] and n_ch == 23 and n_tr == 0 and not missing, (dep['spans'].get('refuge_war_family'), n_ch, n_tr, missing)
print('dependency: the span (three ranges) + %d edges (refuge_war_family %d CALL — all reference; the token-demanded edges and any pointer after the gate\'s print)' % (n_ch, n_ch))
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 77 and all(" in text:
    old = "len(real) == 77 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 15b (2026-09-24; LEAN): 76 -> 77,"
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 78 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 16b (2026-09-25; LEAN): 77 -> 78, law_refuge_war_family (given_at Deut 19:1 — the nations cut off; installed_by boot; one daemon over three chapters); 15b: 76 -> 77,")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 78" in open(path, encoding='utf-8').read()
print('installation_probes I5: 78')
# ---- THE REGISTER FILE UNTOUCHED HERE — the one seat at Deut 20:17 (class NONE on file) dispositioned at the tail from the register gate's print ----
rg = yaml.safe_load(open(f"{ROOT}/World/step9/register_dispositions.yaml", encoding='utf-8'))
seats = [k for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut (?:19|2[01]):', str(k))]
assert seats == ['Deut 20:17'] and rg['receipts']['Deut 20:17']['class'] == 'NONE', seats
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']; ev = yaml.safe_load(open(f"{ROOT}/World/step9/event_vocabulary.yaml", encoding='utf-8'))['events']
print('THE TYPES DONE: kinds %d, effects %d, daemons %d, functions blocks %d, edges from refuge_war_family %d, I5 78; the register seat Deut 20:17 NONE (the tail)' % (len(ev), len(fx), len(dd['daemons']), len(dd['functions']), n_ch))
