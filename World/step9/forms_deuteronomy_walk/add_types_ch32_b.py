import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b — THE COMPILE OF CHAPTER 32, THE SONG, LEAN (2026-09-28): THE TYPES BY SCRIPT, part B — daemon_dispositions (law_song_charge_nebo — given_at
# Deut 32:1, installed_by boot; the watches the sixteen lines IN THREE FORMS with their writes NEW AND REUSED (13b's form — a reused effect is the line's write too); the functions block
# SEVENTEEN WRAPPED: the sixteen cells and the_readback); dependency_dispositions (the span's ONE RANGE [[Deut, 32, 1, 52]], FORTY-TWO CALL edges by the ink, all REFERENCE — the census
# decides the rest; NO owed pointer in the file); installation_probes I5 81 -> 82; THE CALENDAR UNTOUCHED (no clock word in the song — 19b's the_death_date_of_moses the marker's day, read by
# the runner, not exercised anew); THE REGISTER FILE UNTOUCHED (no seat in the chapter). add_types_ch29_b.py's form; the names READ from the spec module beside this file. RUN FROM THE REPO ROOT.
import yaml, subprocess, re, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch32b_spec as S
CHECK = '--check' in sys.argv
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
W = "THE DEUTERONOMY WALK 20b (2026-09-28) | "
R, DM = S.RUNNER, S.DAEMON
CELLS = [S.CELLS['F%d' % i] for i in range(1, 17)] + ['the_readback']
assert len(CELLS) == 17
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
D1 = "at Moses' last day (40, 12, 7) — 19b's marker, no marker here"
NOTE = {'song_witnesses_called_declared': "Deut 32:1-4 (a SPEECH — the song's first stanza): the doctrine as rain, the Name proclaimed, the Rock perfect — STATUSES (NEW), heaven_and_earth_witness REUSED at 32:1 (the chain's fifth seat); " + D1,
        'song_crooked_generation_declared': "Deut 32:5-6: the crooked generation, the Father who acquired you — STATUSES (NEW; Sotah 1:7's measure for measure, Avot 6:10's five acquisitions the cases); " + D1,
        'song_nations_divided_lords_portion_declared': "Deut 32:7-9: the days of old, the nations' bounds by the number of Israel, the LORD's portion — STATUSES (NEW; Genesis 11's division and Jacob's seventy by CALL, the references); " + D1,
        'song_found_in_the_desert_declared': "Deut 32:10-12: found in the desert, the apple of His eye, the eagle, the LORD alone — STATUSES (NEW; the tape's own lines RUN CITATIONS — the manna, the rock, the cloud; Tosefta Arakhin 1:4's twelve mil a parameter); " + D1,
        'song_heights_honey_rock_declared': "Deut 32:13-14: the heights ridden and the honey from the rock, the feast — STATUSES (NEW; the qere's fourteenth token at 32:13; Kilayim 3:2 and Peah 3:2 the cases; the conquest FORWARD to Joshua's tape); " + D1,
        'song_jeshurun_fat_kicked_declared': "Deut 32:15-18: Jeshurun fat and kicking, the demons and the new gods, the Rock forgotten — STATUSES (NEW; THE FALSE EIGHT at 32:15 guarded — a DATA row, no count; worded from the Aramaic); " + D1,
        'song_face_hidden_foolish_nation_declared': "Deut 32:19-22: the jealousy by a no-people, the fire to Sheol — HEAVEN entries (NEW; the song's foretellings), face_hidden_and_forsaken_foretold REUSED at 32:20 (the hidden face the third time); " + D1,
        'song_evils_heaped_declared': "Deut 32:23-25: the evils heaped, hunger and beasts and the sword and terror — HEAVEN entries (NEW; the rule of war and famine a parameter, Bava Kamma 60b owed); " + D1,
        'song_enemys_boast_declared': "Deut 32:26-28: the blotting out stayed by the enemy's boast — a HEAVEN entry (NEW; the decree not carried out), the nation void of counsel — a STATUS (NEW; Tosefta Avodah Zarah 9:4's seven commandments the case); " + D1,
        'song_one_chasing_a_thousand_declared': "Deut 32:29-33: one chasing a thousand and their Rock sold them, the vine of Sodom — STATUSES (NEW; THE JOINED THOUSAND at 32:30 guarded — a DATA row; THE STATE ROW at 32:30; Sanhedrin 3:5's enemy neither witness nor judge the case); " + D1,
        'song_vengeance_in_store_declared': "Deut 32:34-38: the cup in store and the vengeance, the LORD judges His people — HEAVEN entries (NEW), where are their gods — a STATUS (NEW; Tosefta Peah 1:1-3's fruit of deeds the cases; 328's misprinted head; the Name profaned at once a parameter); " + D1,
        'song_i_am_he_declared': "Deut 32:39-43: I am He, I kill and make alive, the hand lifted — STATUSES (NEW; the song's creed), the sword whetted, the nations sing and the land atones — HEAVEN entries (NEW; Berakhot 1:1's evening Shema the case; no ransom a DATA row); the unit deu_32_haazinu closes; " + D1,
        'song_spoken_by_moses_and_hoshea': "Deut 32:44-45 (an ACT): the song spoken in the ears of the people — a STATUS (NEW; the song spoken twice — the successor's coming, 334:1), Hoshea beside Moses — a STATUS on yehoshua (NEW; the old name kept, Numbers 13:16 by CALL); " + D1,
        'set_your_heart_no_empty_matter_declared': "Deut 32:46-47 (the STATUTE): set your heart, it is your life — STATUSES (NEW; Chagigah 1:8's mountains by a hair and Peah 1:1's things without measure the cases), length_of_days_on_the_land_promised REUSED at 32:47 (the second entry); " + D1,
        'nebo_summons_die_as_aaron': "Deut 32:48-50 (a SPEECH of the LORD): go up to Nebo, die in the mountain and be gathered, as Aaron died — STATUSES on moses (NEW; the selfsame day 19b's marker's day; the commission's debit OPEN to 34:1-4; Aaron's death the receipt — the pointer 32:50 a run citation); " + D1,
        'meribah_trespass_not_go_there_declared': "Deut 32:51-52 (a SPEECH of the LORD): the trespass at Meribath-kadesh — a STATUS on moses (NEW; Numbers 20:12's sentence read back, barred_from_the_land UNMOVED), see the land from afar, not go there — a HEAVEN entry on moses (NEW; 34:4 ahead cited, never read); the chapter's close; " + D1}
assert set(NOTE) == set(S.KINDS)
if f'  {DM}:' not in text:
    lines = []
    for kind, first, rng, claim, cell, form, fields, effs, reuses in S.LINES:
        ws = [e for e, _, _ in effs] + [e for e, _, _ in reuses]
        lines.append('      %s: [%s]   # %s\n' % (kind, ', '.join(ws), NOTE[kind]))
    block = (f'  {DM}:\n    file: cold_run_{R}.py\n    wraps: {R}\n    given_at: Deut 32:1\n'
             '    installed_by: boot   # THE DEUTERONOMY WALK 20b (2026-09-28; THE LEAN PASS): "GIVE EAR, O HEAVENS, AND I WILL SPEAK" — the song\'s first verse at Moses\' last day (40, 12, 7), 19b\'s marker at 31:1 (NO MARKER in this chapter — 32:48\'s selfsame day THAT day); installed by boot like law_opening_speech through law_covenant_return_charge (the Deuteronomy daemons\' form; THE INSTALL HYPOTHESIS on the table unchanged); ONE daemon over ONE chapter and two units — the song (32:1-43) and its frame (32:44-52): the song\'s own declarations its NEW family; SIXTEEN lines in THREE FORMS (14 speech — the twelve stanzas and the LORD\'s two to Moses, 1 act, 1 statute); the two guards (the false eight at 32:15, the joined thousand at 32:30) DATA rows, no count\n'
             '    watches:\n' + ''.join(lines))
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if f'\n  {R}:   # THE DEUTERONOMY WALK 20b' not in text:
    fb = f'  {R}:   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN — one chapter, two units, one daemon, no marker)\n' + ''.join('    %s: {status: WRAPPED, by: %s}\n' % (c, DM) for c in CELLS)
    i = text.index('  covenant_return_charge:   # THE DEUTERONOMY WALK 19b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(text)
NW = sum(len(l[7]) + len(l[8]) for l in S.LINES)
assert DM in dd['daemons'] and R in dd['functions'] and len(dd['functions'][R]) == 17 and len(dd['daemons'][DM]['watches']) == 16 and sum(len(v) for v in dd['daemons'][DM]['watches'].values()) == NW == 45, (len(dd['functions'].get(R, [])), len(dd['daemons'].get(DM, {}).get('watches', {})), NW)
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']; ev = yaml.safe_load(open(f"{ROOT}/World/step9/event_vocabulary.yaml", encoding='utf-8'))['events']
for k, v in dd['daemons'][DM]['watches'].items():
    assert k in ev, k
    for e in v: assert e in fx, e
assert {ev[k]['form'] for k in dd['daemons'][DM]['watches']} == {'statute', 'act', 'speech'}
print('daemons: %d (%s %s); functions blocks: %d; the watches %d writes over 16 lines in three forms' % (len(dd['daemons']), DM, DM in dd['daemons'], len(dd['functions']), NW))
# ---- the dependency span (one range) + the CALL edges by the ink (forty-two REFERENCE; the token-demanded edges and the pointer 32:50 after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
REF = [
 ('obey_horeb', "32:1's 'give ear, O heavens … let the earth hear' is THE CHAIN OF WITNESSES' FIFTH SEAT (OH.DATA the_witnesses_chain — 4:26, 30:19, 31:28, 32:1 — CALLED; heaven_and_earth_witness REUSED); 32:8's nations' inheritance 4:19's host apportioned (OH.no_image('the_host_apportioned')); 32:22's fire 4:24's consuming fire; 32:39's 'no god with Me' 4:35's 'none else beside Him'; the readback rows 32:1, 32:8, 32:22, 32:39 the kin by CALL"),
 ('covenant_return_charge', "32:1-43 is the song 31:19-22 COMMANDED, WRITTEN AND TAUGHT and 31:30 SPOKE (CR.the_song_commanded, CR.DATA the_song_ahead naming 32:1-43 forward — CALLED; song_spoken_to_the_assembly_to_its_end UNMOVED: 32:44's coming a second act by the Sifrei 334:1); 32:20's hidden face 31:17-18's (CR.the_apostasy_foretold — face_hidden_and_forsaken_foretold REUSED, the third seat); 32:15's satiety 31:20's twin TAUGHT at 318:1; 32:47's length of days 30:20's (length_of_days_on_the_land_promised REUSED); 32:44's Hoshea beside Moses 31:7 and 31:23's commissions; 32:48's selfsame day THE MARKER'S DAY (40, 12, 7) — CR.DATA the_death_date_of_moses, the_three_gifts_and_their_merits (the daemon owed at 34:5); the readback rows 32:15, 32:20, 32:44, 32:46-48 the kin by CALL"),
 ('good_land', "32:10's desert and 32:13's honey from the flinty rock are 8:15-16's wilderness, flint and manna (GL.the_chain_and_the_covenant('the_wilderness', 'the_rock_of_flint', 'the_manna_to_do_you_good') CALLED — GL.DATA the_two_rocks, honey_without_milk; 'in your end' 32:20 and 32:29 the lemma's ten seats); 32:15-18's forgetting 8:11-19's (GL.the_testimony); NO receipt in the chapter (GL.receipt_seats(32) -> []); the readback rows 32:10, 32:13, 32:15, 32:18, 32:20, 32:29 the kin by CALL"),
 ('exodus_story', "32:10-11's desert and eagle are the tape's Exodus 16-19 (ES.sinai — the eagles' wings 19:4 the twin TAUGHT at the Sifrei 314:3, the treasure seats; ES.manna the manna's lines — manna_provided UNMOVED — CALLED); 32:6's 'acquired' Exodus 15:16's 'the people You acquired' (ES.song); 32:48's selfsame day Exodus 12:41's (ES.scene — the tape's own line); 32:39's healing Exodus 15:26's (healed the tape's); the readback rows 32:6, 32:10-11, 32:39, 32:48 the kin by CALL"),
 ('refuge_war_family', "32:1's witnesses carry 19:15's rule (RW.the_landmark_and_the_witnesses('one_witness_for_any_iniquity') CALLED — two_or_three_witnesses_required UNMOVED); 32:2's rain-verb the heifer's homograph (RW.the_broken_necked_heifer — a homograph noted); 32:43's atonement 21:8's innocent blood (innocent_blood_atoned UNMOVED); the readback rows 32:1, 32:2, 32:43 the kin by CALL"),
 ('persons_poor_court', "32:14's feast divided by Kilayim 3:2 stands on 22:9's vineyard (PP.DATA the_vineyards_mixture CALLED); 32:47's things without measure include the nest 22:7 (PP.DATA the_nests_sending); the readback rows 32:14, 32:47 the kin by CALL"),
 ('courts_prophet', "32:1's two witnesses (the Sifrei 306:9) are 17:6's rule (CP.the_idolaters_trial('two_witnesses_for_every_death', 'the_seven_investigations', 'the_three_acts_and_the_associator') CALLED — two_witnesses_required UNMOVED; Mishnah Sanhedrin 5:2's examinations the case); 32:17's demons 17:3's acts; the readback rows 32:1, 32:17 the kin by CALL"),
 ('refuge', "32:30-31's 'our enemies are judges' and the Sifrei 323:5 are Numbers 35:23's enemy neither witness nor judge (RF.DATA the_one_witness, the_case_table CALLED — Mishnah Sanhedrin 3:5 the case); 32:43's 'He atones for His land' Numbers 35:33's atonement by the shedder's blood (RF.DATA the_lands_atonement); 32:39's no ransom Numbers 35:31's (RF.DATA the_ransom_rows); the readback rows 32:30-31, 32:39, 32:43 the kin by CALL"),
 ('ordinances', "32:31's 'our enemies are judges' (pelilim) is Exodus 21:22's word (OR.courts CALLED — a homograph by word, a DATA note); 32:39's 'none delivers' the soul beyond ransom — Exodus 21:30's kofer (the Sifrei 329:4); the readback rows 32:31, 32:39 the kin by CALL"),
 ('chukat', "32:50's 'as Aaron your brother died in Mount Hor' is Numbers 20:22-29's death and succession (CK.edom_and_hor('death_dates', 'succession', 'aaron_age') CALLED — garments_transferred_and_aaron_died at (40, 5, 1) aged 123; gathered_to_his_people and barred_from_the_land UNMOVED; THE POINTER 32:50 AS_WHEN a RUN_CITATION); 32:51's Meribath-kadesh Numbers 20:12-13's sentence (CK.meribah('sentence', 'died_for_sin', 'meribah_seats', 'death_by_the_kiss') — six seats, 32:51 among them; 'you caused them' thrice the Sifrei 340:1); 32:24's serpents Numbers 21:6's (serpents_sent UNMOVED); 32:50's tent law 339:1 (CK.corpse_tumah by reference); the readback rows 32:24, 32:50-51 the kin by CALL"),
 ('opening_speech', "32:49's 'go up into this mountain of Abarim, Mount Nebo … and behold the land' is Numbers 27:12-14's commission RETOLD by the LORD's own mouth (OS.the_commission('the_mountain', 'the_sentence_cited', 'the_receipt', 'the_debit') CALLED — one mountain, three names; the debit see_the_land_from_abarim OPEN BY DESIGN to 34:1-4, the receipt 27:22 CLOSE; 27:14's pointer to chukat's sentence names 32:51); 32:14's Bashan 3:1-14's conquest (OS.sihon_and_og); 32:52's seeing 3:27's Pisgah (the retelling read back); the readback rows 32:14, 32:49, 32:51-52 the kin by CALL"),
 ('journeys', "32:50's Aaron's death is Numbers 33:38-39's retelling (JR.aarons_death_retold — ten asks: the date (40, 5, 1), the age 123, the kiss, moses_seventh_adar, no_write — A RETELLING NEVER WRITES AN ACT TWICE — CALLED; JR.DATA the_four_writings, the_death_date, aarons_age; JR.lemma_seats names 32:13 and 32:49); the readback rows 32:13, 32:49-50 the kin by CALL"),
 ('second_tablets', "32:50's Aaron's death stands beside 10:6's Moserah (ST.the_stations_and_the_death('aaron_died_there', 'the_place_of_the_death') CALLED — the OPEN row against Mount Hor); 32:18's forgetting 10:16's heart; the readback row 32:50 the kin by CALL"),
 ('primeval', "32:8's 'when He separated the sons of man' is Genesis 10:25's Peleg and Genesis 11's division (PV.babel, PV.nations CALLED — the builders scattered, the language confounded: scattered, building_ceased UNMOVED; Genesis 11:8 the measure's twin a labeled HYPOTHESIS — the edge a REFERENCE by the ink's own words); 32:48's selfsame day Genesis 7:13's boarding (PV.flood — the tape's entered_the_ark; the Sifrei 337:1); Genesis 6:5's inclination (PV.prologue); the readback rows 32:8, 32:48 the kin by CALL"),
 ('pre_sinai', "32:28's counsel is the nations' seven commandments (PS.noahide CALLED — Genesis 9's own law on the tape, blood_required UNMOVED; Tosefta Avodah Zarah 9:4 THE CASE at the Sifrei 322:11); 32:48's selfsame day Genesis 17:23, 26's circumcision (PS.circumcision by reference); 32:4's Rock and the 'do not read' rows PS.rows name 32:4 and 32:48; the readback rows 32:4, 32:28, 32:48 the kin by CALL"),
 ('mamre', "32:32's 'vine of Sodom, fields of Gomorrah' is Genesis 19:24-25's overthrow on the tape (MA.sodom CALLED — Sodom's own entry; 29:22's four cities 19b's); 32:6's 'acquired' Genesis 14:19's possessor of heaven and earth (MA.scene — Avot 6:10's five acquisitions); 32:40's lifted hand Genesis 14:22's; the deeds of kindness (32:47's things without measure — Genesis 18's hospitality by reference); the readback rows 32:6, 32:32, 32:40 the kin by CALL"),
 ('family', "32:8's 'by the number of the children of Israel' is Jacob's seventy souls (FA.mrow — Genesis 46:27 the tape's own count — CALLED; the Sifrei 310-311's seventy against seventy); 32:50's 'gathered to his people' Genesis 49:33's form (FA.testament — Jacob's gathering); the readback rows 32:8, 32:50 the kin by CALL"),
 ('balak', "32:12's 'the LORD alone led him' is Numbers 23:9's 'a people that dwells alone' (BK.the_stands CALLED — the Sifrei 356:5's 'alone'; BK.census names 32:8); the readback row 32:12 the kin by CALL"),
 ('beha', "32:10's desert is the three gifts — the well, the cloud, the manna (BH.taberah_and_quail('manna_taste', 'manna_form', 'three_gifts') CALLED — Taanit 9a; the camp round the Presence BH.march by reference); the readback rows 32:10-11 the kin by CALL"),
 ('shelach', "32:44's HOSHEA is Numbers 13:16's old name (SH.spies('joshua_name') CALLED — Hoshea to Joshua, the new name at eight seats before, the old again here alone: the same man, Tosefta Berakhot 1:15); 32:27's 'lest they say' Numbers 14:16's argument (SH.decree — the tape's own); the readback rows 32:27, 32:44 the kin by CALL"),
 ('not_righteousness', "32:27's 'lest they say: our hand is exalted' is 9:28's 'lest the land say' (NR.the_intercession('lest_the_land_say') CALLED); the ten trials 9:22-24's (NR.the_four_provocations('the_ten_trials')); the readback row 32:27 the kin by CALL"),
 ('seven_nations', "32:9's 'the LORD's portion is His people' stands beside 7:6's holy people and 26:18's treasure (SN.the_holy_people('holy_people', 'chose_you', 'the_fewest', 'the_oath') CALLED — treasured_people, lord_declared_israel_treasure_people, became_the_lords_people_this_day UNMOVED; 32:40's oath by God's own life the oath lines by kind); the readback rows 32:9, 32:40 the kin by CALL"),
 ('hear_o_israel', "32:39's 'no god with Me' is 6:4's unity reaffirmed (HI.the_creed('the_lord_is_one') CALLED — shema_commanded UNMOVED); 32:43's land atones by the Shema twice daily (the Sifrei 333:4 — HI.DATA the_recitation_times: Mishnah Berakhot 1:1's evening THE CASE); 32:46's 'command your children' 6:7's teaching (HI.the_four_duties('teach_your_sons')); the readback rows 32:39, 32:43, 32:46 the kin by CALL"),
 ('blessing_and_curse', "32:2's four rains are 11:14's early and latter rain (BC.the_land_watered_by_heaven, BC.DATA rain_dates CALLED — Onkelos's latter rain at 32:2; rain_in_its_season UNMOVED); 32:47's length of days 11:9's five in order (BC's readback row 11:9 — length_of_days_on_the_land_promised REUSED); the readback rows 32:2, 32:47 the kin by CALL"),
 ('firstfruits_ebal_curses', "32:21's foolish nation is 28:49's eagle nation (FE.the_curses_of_the_siege_and_the_exile('a_nation_from_the_end_of_the_earth_as_the_eagle_flies') CALLED — eagle_nation_devours UNMOVED); 32:23-25's evils 28:53-61's siege and plagues (sons_flesh_eaten_in_siege, pestilence_cleaving, sword_blight_mildew_sent, plagues_made_wonderful UNMOVED); 32:30's two arms 28:7 and 28:25 (enemies_flee_seven_ways, smitten_before_enemies_seven_ways — THE STATE ROW); 32:47's things without measure 26:2's first fruits (FE.the_first_fruits, FE.DATA the_things_without_measure — 18b's own row); the readback rows 32:21, 32:23-25, 32:30, 32:47 the kin by CALL"),
 ('tochacha', "32:24's beasts and 32:25's sword are Leviticus 26:22 and 26:25's twins BY SENSE (TC.cascade, TC.measures CALLED — the arms; the twin a labeled HYPOTHESIS, the edge a REFERENCE by the ink's shared words); 32:30's one chasing a thousand Leviticus 26:8's five chase a hundred (the Sifrei 322:12's arithmetic — the joined thousand's kin); the readback rows 32:24-25, 32:30 the kin by CALL"),
 ('seducers', "32:17's 'gods they knew not, new ones that came up of late' is 13:7's 'gods you have not known' (SE.the_inciter CALLED — the inciter's kin; the idolatry predicate's terms); the readback row 32:17 the kin by CALL"),
 ('decalogue', "32:37-38's false rock and the Sifrei 328:4's Name profaned punished at once stand on 5:11's third word (DC.vain_name CALLED — the parameter the_name_profaned_at_once; Yoma 86a owed); the readback rows 32:37-38 the kin by CALL"),
 ('covenant_at_horeb', "32:44's 'in the ears of the people' is Exodus 24:7's and 5:1's assembly (CH.the_assembly_called CALLED — CH.out names 32:40); the readback row 32:44 the kin by CALL"),
 ('naso', "32:5's 'perverse and crooked generation' and 32:15's kicking are Sotah 1:7's measure for measure (NS.sotah, NS.DATA sotah_order CALLED — the Sifrei 308:4 and 318:8: the parameter the_measure_for_measure); the readback rows 32:5, 32:15 the kin by CALL"),
 ('incense_shekel', "32:39's 'none delivers out of My hand' and the Sifrei 329:4's soul beyond ransom stand on Exodus 30:12's ransom of the soul (IS.shekel CALLED — the DATA row the_no_ransom); the readback row 32:39 the kin by CALL"),
 ('festivals_judges', "32:47's things without measure include the appearing (FJ.the_three_pilgrimages('who_appears', 'not_empty', 'the_gift_of_the_hand') CALLED — Mishnah Chagigah 1:1 and 1:5 read whole at 14b; three_pilgrimages_commanded UNMOVED); 32:46's Chagigah 1:8 the festival offerings a mountain by a hair; the readback rows 32:46-47 the kin by CALL"),
 ('holiness', "32:14's Peah 3:2 (the striped field) and 32:47's Peah 1:1 and Tosefta Peah 1:3 (the peah from the beginning) stand on Leviticus 19:9-10's corner (HL.gifts CALLED — the parameters the_striped_field, the_peah_from_the_beginning); the readback rows 32:14, 32:34, 32:47 the kin by CALL"),
 ('vows', "32:3's Name proclaimed carries Nedarim 1:2's substitutes (VW.DATA substitutes_source, konam_measure CALLED — the Sifrei 306:36: the parameter the_vows_substitutes); 32:46's Chagigah 1:8 the dissolution of vows flying in the air (VW.DATA sage_release); the readback rows 32:3, 32:46 the kin by CALL"),
 ('food_tithe', "32:5's 'His children' is 14:1's sonship on the tape (FT.DATA the_sonships_arms CALLED — the two arms); the readback row 32:5 the kin by CALL"),
 ('gad_reuben', "32:49's Nebo is Numbers 32:38's Reubenite city (GR.DATA moses_grave CALLED — Reuben's Nebo, Gad's field, Sotah 13b; the Sifrei 355:6; GR.tok names 32:49); the readback row 32:49 the kin by CALL"),
 ('borders', "32:49's 'the land of Canaan which I give to the children of Israel for a possession' is Numbers 34:2's land by its border (BR.the_land_and_its_fall('the_land_canaan') CALLED — BR.stem names 32:50); the readback row 32:49 the kin by CALL"),
 ('erection', "32:27's 'lest they say' is Exodus 32:12's argument at the calf (ER.calf CALLED — the tape's own line); 32:20's hidden face against the shown face (ER.presence — glory_appeared the two faces of one ledger); the readback rows 32:20, 32:27 the kin by CALL"),
 ('sanctions', "32:4's 'all His ways are justice' carries Sanhedrin 9:1's burned and beheaded (SA.burning_scope CALLED — the Sifrei 307:14: the parameter the_burned_and_the_beheaded); the readback row 32:4 the kin by CALL"),
 ('vayikra5', "32:46's Chagigah 1:8 names the sacrileges among the mountains by a hair (V5.sacrilege CALLED — Leviticus 5:15's one verse); the readback row 32:46 the kin by CALL"),
 ('moadim', "32:46's Chagigah 1:8 names the festival offerings among the mountains by a hair (MD.sukkot CALLED — Leviticus 23's feasts the family); the readback row 32:46 the kin by CALL"),
 ('mekoshesh', "32:46's Chagigah 1:8 names the Sabbath laws among the mountains by a hair (MK.DATA gatherers_labor CALLED — Numbers 15:32's one verse, the thirty-nine labors); the readback row 32:46 the kin by CALL"),
]
assert len(REF) == 42 and len({t for t, _ in REF}) == 42 and [t for t, _ in REF] == S.EDGES, ([t for t, _ in REF][:5], S.EDGES[:5])
if f'\n  {R}:' not in text.split('\nedges:')[0]:
    a = "  covenant_return_charge: [[Deut, 29, 1, 28], [Deut, 30, 1, 20], [Deut, 31, 1, 30]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + f"  {R}: [[Deut, 32, 1, 52]]   # THE DEUTERONOMY WALK 20b (2026-09-28; DEUTERONOMY_WALK.md \"Sitting 20b\" — LEAN): chapter 32 in ONE runner over two frozen units (deu_32_haazinu — the song 32:1-43; deu_32_song_aftermath — the frame 32:44-52): the witnesses called, the Rock, the crooked generation, the nations divided, the desert and the eagle, the heights and the feast, Jeshurun fat, the hidden face, the evils heaped, the enemy's boast, the joined thousand, the cup in store, I am He and the land atones; the song spoken with Hoshea, the charge, the summons to Nebo, Meribah; SIXTEEN own-day lines in THREE FORMS (14 speech, 1 act, 1 statute) at Moses' last day (40, 12, 7) — NO MARKER (19b's at 31:1); the daemon law_song_charge_nebo given_at Deut 32:1, installed_by boot\n" + text[j + 1:]
    edges = ''.join("  - {from: %s, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: %s}\n" % (R, to, q(W + why)) for to, why in REF)
    k = text.rfind('  - {from: covenant_return_charge, to: '); e = text.index('\n', text.index('why:', k)) + 1
    text = text[:e] + edges + text[e:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(text)
n_ch = sum(1 for e in dep['edges'] if e['from'] == R); n_tr = sum(1 for e in dep['edges'] if e['from'] == R and e.get('link') == 'transfer')
missing = [e['to'] for e in dep['edges'] if e['from'] == R and e['to'] not in dep['spans']]
owed = [p for p in dep['pointers'] if p.get('disposition') == 'OWED']
assert R in dep['spans'] and dep['spans'][R] == [['Deut', 32, 1, 52]] and n_ch == 42 and n_tr == 0 and not missing, (dep['spans'].get(R), n_ch, n_tr, missing)
assert not owed, len(owed)
print('dependency: the span (one range) + %d edges (%s %d CALL — all reference; the token-demanded edges and the pointer 32:50 after the gate\'s print); OWED pointers in the file: %d; edges %d, pointers %d' % (n_ch, R, n_ch, len(owed), len(dep['edges']), len(dep['pointers'])))
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
old = "len(real) == 81 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): 80 -> 81,"
if old in text:
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 82 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): 81 -> 82, law_song_charge_nebo (given_at Deut 32:1 — give ear, O heavens; installed_by boot; one daemon over one chapter and two units, sixteen lines in three forms, no marker); 19b: 80 -> 81,")
    if not CHECK: open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 82" in text
print('installation_probes I5: 82')
# ---- THE CALENDAR UNTOUCHED (no clock word in the song; 19b's the_death_date_of_moses THE MARKER'S DAY read by the runner) ----
cal = yaml.safe_load(open(f"{ROOT}/World/step9/calendar_parameters.yaml", encoding='utf-8'))['parameters']
assert len(cal) == 75 and 'the_death_date_of_moses' in cal and not any('Deut 32:' in str(v.get('source', '')) and k.startswith('the_') and 'song' in k for k, v in cal.items()), len(cal)
print('calendar: %d parameters, untouched (the_death_date_of_moses 19b\'s — the marker\'s day the runner reads)' % len(cal))
# ---- THE REGISTER FILE UNTOUCHED — no seat in the chapter ----
rg = yaml.safe_load(open(f"{ROOT}/World/step9/register_dispositions.yaml", encoding='utf-8'))
seats = [k for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut 32:', str(k))]
assert seats == [], seats
print('register: untouched (no seat at Deut 32; footers %d)' % len(rg.get('footers', {})))
print('TYPES B OK' + (' (check)' if CHECK else ''))
