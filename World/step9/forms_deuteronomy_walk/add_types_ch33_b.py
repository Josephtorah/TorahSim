import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b — THE COMPILE OF CHAPTER 33, THE BLESSING, LEAN (2026-09-29): THE TYPES BY SCRIPT, part B — daemon_dispositions (law_blessing_of_moses — given_at
# Deut 33:1, installed_by boot; the watches the eleven lines IN TWO FORMS with their writes NEW (no reuse); the functions block TWELVE WRAPPED: the eleven cells and the_readback);
# dependency_dispositions (the span's ONE RANGE [[Deut, 33, 1, 29]], THIRTY-NINE CALL edges by the ink, all REFERENCE — the census decides the rest; NO owed pointer in the file);
# installation_probes I5 82 -> 83; THE CALENDAR UNTOUCHED (no clock word in the blessing — 33:18's festivals' times Onkelos's, the registry's festival_dates the parameter already);
# THE REGISTER FILE UNTOUCHED (no seat in the chapter). add_types_ch32_b.py's form; the names READ from the spec module beside this file. RUN FROM THE REPO ROOT.
import yaml, subprocess, re, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch33b_spec as S
CHECK = '--check' in sys.argv
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
W = "THE DEUTERONOMY WALK 21b (2026-09-29) | "
R, DM = S.RUNNER, S.DAEMON
CELLS = [S.CELLS['F%d' % i] for i in range(1, 12)] + ['the_readback']
assert len(CELLS) == 12
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
D1 = "at Moses' last day (40, 12, 7) — 19b's marker, no marker here"
NOTE = {'moses_blessed_israel_before_his_death': "Deut 33:1-2 (an ACT — the frame): the blessing given before Moses' death, the LORD from Sinai, Seir and Paran, the fiery law from His right hand — STATUSES (NEW) on Israel; the death 34:5 AHEAD; " + D1,
        'blessing_prologue_law_and_king_declared': "Deut 33:3-5 (a SPEECH — the prologue): the lover of the peoples, the law the inheritance of Jacob, the king in Jeshurun — STATUSES (NEW) on Israel; Avot 1:1's chain, Avot 3:6's ten, Bava Kamma 4:3's ox and Tosefta Eduyot 1:1's dough the cases; the readback's POINTER ROW 33:5; " + D1,
        'blessing_reuben_and_judah_declared': "Deut 33:6-7 (a SPEECH): Reuben to live and not die, Judah's voice heard — STATUSES (NEW) on reuben and judah, the sons' own ledgers; Sanhedrin 10:1's share the case; Simeon under Judah a DATA row, no write; " + D1,
        'blessing_levi_declared': "Deut 33:8-11 (a SPEECH): the Thummim and the Urim proved at Massah, the father and mother unseen, the teaching and the incense, the substance blessed and the risers smitten — STATUSES (NEW) on levi; Massah, Meribah and the calf's sword RUN CITATIONS; Shekalim 1:1 the case; " + D1,
        'blessing_benjamin_declared': "Deut 33:12 (a SPEECH): the beloved dwells in safety between His shoulders — a STATUS (NEW) on benjamin; the sanctuary's tribe an OPEN parameter (352:10's dispute); Eduyot 8:6 the case; " + D1,
        'blessing_joseph_declared': "Deut 33:13-17 (a SPEECH): the land blessed with the precious things, the bush dweller's favor on the crown, the firstling ox's horns with Ephraim's myriads and Manasseh's thousands — STATUSES (NEW) on joseph; Genesis 49:25-26 and 48:19 and the bush RUN CITATIONS; " + D1,
        'blessing_zebulun_and_issachar_declared': "Deut 33:18-19 (a SPEECH): Zebulun in his going out and Issachar in his tents, the peoples called to the mountain — STATUSES (NEW) on zebulun and issachar; Rosh Hashanah 2:8-9 and Keritot 2:1 the cases; " + D1,
        'blessing_gad_declared': "Deut 33:20-21 (a SPEECH): Gad enlarged, the lioness, the first part and the lawgiver's portion, the heads of the people and the righteousness of the LORD — STATUSES (NEW) on gad; Moses' grave the POINTER 33:21 FORWARD to 34:6; Menachot 8:3 and Avot 5:6 the cases; " + D1,
        'blessing_dan_naphtali_asher_declared': "Deut 33:22-25 (a SPEECH): Dan the lion's whelp, Naphtali sated with favor, Asher's foot in oil, the bars of iron and brass — STATUSES (NEW) on dan_son, naphtali and asher; the parser's false seven at 33:23 a DATA row; " + D1,
        'blessing_rider_of_the_heaven_declared': "Deut 33:26-27 (a SPEECH — the coda's praise): none like the God of Jeshurun, the eternal God's everlasting arms and the enemy driven out — STATUSES (NEW) on Israel; the three scrolls in the court a parameter; " + D1,
        'blessing_israel_dwells_alone_declared': "Deut 33:28-29 (a SPEECH — the chapter's close): Israel dwells in safety alone, happy are you Israel — STATUSES (NEW) on Israel; the readback's POINTER ROW 33:28; the necks of the kings FORWARD to Joshua's tape; " + D1}
assert set(NOTE) == set(S.KINDS)
if f'  {DM}:' not in text:
    lines = []
    for kind, first, rng, claim, cell, form, fields, effs, reuses in S.LINES:
        ws = [e for e, _, _ in effs] + [e for e, _, _ in reuses]
        lines.append('      %s: [%s]   # %s\n' % (kind, ', '.join(ws), NOTE[kind]))
    block = (f'  {DM}:\n    file: cold_run_{R}.py\n    wraps: {R}\n    given_at: Deut 33:1\n'
             '    installed_by: boot   # THE DEUTERONOMY WALK 21b (2026-09-29; THE LEAN PASS): "AND THIS IS THE BLESSING WHICH MOSES THE MAN OF GOD BLESSED THE CHILDREN OF ISRAEL BEFORE HIS DEATH" — the blessing\'s first verse at Moses\' last day (40, 12, 7), 19b\'s marker at 31:1 (NO MARKER in this chapter — \'before his death\' THAT day); installed by boot like law_opening_speech through law_song_charge_nebo (the Deuteronomy daemons\' form; THE INSTALL HYPOTHESIS on the table unchanged); ONE daemon over ONE chapter and one unit — the blessing (33:1-29): the blessing\'s own declarations its NEW family, its writes on Israel\'s ledger and THE TRIBES\' OWN (the sons\' entities Genesis 49\'s testament wrote on); ELEVEN lines in TWO FORMS (1 act — the frame; 10 speech — the prologue, the ten blessings at the reading\'s seats, the coda); the parser\'s false seven at 33:23 a DATA row, no count; no reuse\n'
             '    watches:\n' + ''.join(lines))
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if f'\n  {R}:   # THE DEUTERONOMY WALK 21b' not in text:
    fb = f'  {R}:   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN — one chapter, one unit, one daemon, no marker, no reuse)\n' + ''.join('    %s: {status: WRAPPED, by: %s}\n' % (c, DM) for c in CELLS)
    i = text.index('  song_charge_nebo:   # THE DEUTERONOMY WALK 20b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(text)
NW = sum(len(l[7]) + len(l[8]) for l in S.LINES)
assert DM in dd['daemons'] and R in dd['functions'] and len(dd['functions'][R]) == 12 and len(dd['daemons'][DM]['watches']) == 11 and sum(len(v) for v in dd['daemons'][DM]['watches'].values()) == NW == 28, (len(dd['functions'].get(R, [])), len(dd['daemons'].get(DM, {}).get('watches', {})), NW)
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']; ev = yaml.safe_load(open(f"{ROOT}/World/step9/event_vocabulary.yaml", encoding='utf-8'))['events']
for k, v in dd['daemons'][DM]['watches'].items():
    assert k in ev, k
    for e in v: assert e in fx, e
assert {ev[k]['form'] for k in dd['daemons'][DM]['watches']} == {'act', 'speech'}
print('daemons: %d (%s %s); functions blocks: %d; the watches %d writes over 11 lines in two forms' % (len(dd['daemons']), DM, DM in dd['daemons'], len(dd['functions']), NW))
# ---- the dependency span (one range) + the CALL edges by the ink (thirty-nine REFERENCE; the token-demanded edges and the pointers after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
REF = [
 ('song_charge_nebo', "33:1's 'before his death' is the death 32:50 COMMANDED (SC.DATA moses_death_ahead — the command a STATUS on moses, the event 34:5 AHEAD — CALLED); the song's frame the blessing's frame (342:1's order — the hard words first, the blessing after); 33:5's and 33:26's Jeshurun 32:15's (song_jeshurun_fat_kicked_declared the kind — by reference); 33:29's high places 32:13's twin by sense, unlinked; SC.the_readback's fifty-two rows the form the blessing's twenty-nine follow; the readback rows 33:1, 33:5, 33:26 the kin by CALL"),
 ('covenant_return_charge', "33:4's 'Moses commanded us a law, an inheritance' is 31:9's law WRITTEN AND DELIVERED to the priests the sons of Levi (CR's line — the handing-over Onkelos 33:4 names; Avot 1:1's chain the parameter — CALLED); 33:1's 'before his death' 31:14's 'your days approach to die' (the commission's line on yehoshua — a RUN CITATION); the readback rows 33:1, 33:4 the kin by CALL"),
 ('gad_reuben', "33:21's 'for there a portion of a ruler was reserved' is MOSES' GRAVE in Gad's field (GR.DATA moses_grave — 'reubens_nebo_gads_field', Sotah 13b; Onkelos 33:21 and the Sifrei 355:6 — CALLED; THE POINTER 33:21 FORWARD to 34:6, the death's sitting's); 33:20's 'He that enlarges Gad' the land east (GR.the_condition, GR.the_grant — land_possessed 6 UNMOVED); the readback rows 33:20, 33:21 the kin by CALL"),
 ('joseph', "33:13-16 is Genesis 49:25-26 five in order and 49:26's line taken whole (JO — birthright_transferred, portion_added on joseph the tape's own rows; the callee's DATA — CALLED); 33:17's Ephraim before Manasseh Genesis 48:19's crossed hands (younger_set_first, adopted_as_sons on ephraim and manasseh — a RUN CITATION); Benjamin's four merits at 352:16 (benjamin_withheld, five_hands, cup_found the tape's); the readback rows 33:12, 33:13, 33:16, 33:17 the kin by CALL"),
 ('family', "33:1's 'before his death' is Isaac's word at Genesis 27:10 (FA — the blessing before death; Genesis 27:28's dew and corn THE KIN ONKELOS NAMES at 33:28 — blessed_with_dew_and_fat 1 on jacob, a RUN CITATION — CALLED); Reuben's Bilhah (Genesis 35:22 — reuben's ledger, 347:1) and Judah's Tamar (38:26 — 348:1) the tape's own entries; Rachel's grave 35:20 (grave_marked 1) at 352:16; the readback rows 33:1, 33:6, 33:7, 33:28 the kin by CALL"),
 ('chukat', "33:8's 'with whom You strove at the waters of Meribah' is Numbers 20:13 on the tape (CH.meribah — meribah_seats, sentence: barred_from_the_land 2 on Moses and Aaron UNMOVED, the entry read not rewritten; CH.edom_and_hor death_dates — Aaron (40, 5, 1), Moses the seventh of Adar — CALLED); the readback row 33:8 the kin by CALL"),
 ('exodus_story', "33:2's 'the LORD came from Sinai' is the tape's descent (ES.sinai — descended_on_the_mountain 1; a RUN CITATION — CALLED); 33:8's 'whom You proved at Massah' Exodus 17:7 (ES.trials); 33:16's 'Him that dwelt in the bush' Exodus 3:2-4 (appeared_in_the_bush the kind — a RUN CITATION); the readback rows 33:2, 33:8, 33:16 the kin by CALL"),
 ('erection', "33:9's 'who said of his father and of his mother: I have not seen him' is THE CALF'S SWORD Exodus 32:26-29 on the tape (ER.calf — slain_by_sword 2 on the three thousand; a RUN CITATION — CALLED); 349:1's Levi repaid at the calf (Simeon under Judah — the DATA row); the readback row 33:9 the kin by CALL"),
 ('second_tablets', "33:8-11's Levi is Aaron's tribe — Aaron's death and burial the tape's (ST.the_stations_and_the_death — aaron_died_there, and_he_was_buried_there; walk_after_his_attributes Sotah 14a's burying the dead the callee's own row on 34:6, cited never read — CALLED); 33:21's grave the pointer ahead beside it; the readback rows 33:8, 33:21 the kin by CALL"),
 ('incense_shekel', "33:10's 'they shall put incense before You' is the golden altar's continual incense (IS.incense — incense_continual 2; Exodus 30:7-8 — CALLED); 352:14's Shekalim 1:1 the half-shekel's proclamation on the first of Adar (IS.shekel — Exodus 30:13); the readback rows 33:10, 33:11 the kin by CALL"),
 ('balak', "33:17's 'the horns of the wild ox' is Numbers 23:22 and 24:8's word (BA.DATA — by reference); 33:28's 'alone' Numbers 23:9's 'a people that dwells alone' (356:5's three alones — by reference); 349:1's Shittim (Simeon under Judah — the DATA row); the readback rows 33:17, 33:28 the kin by CALL"),
 ('opening_speech', "33:2's Seir and Paran are the tape's stations (OS.the_bypass — by reference); 33:17's 'majesty is his' Joshua's splendor by Numbers 27:20 (OS.the_commission — invested_office on yehoshua; the debit see the land OPEN to 34:1-4 — CALLED); the readback rows 33:2, 33:17 the kin by CALL"),
 ('refuge_war_family', "33:10's 'they shall teach Jacob Your ordinances' is 21:5's 'by their word shall every controversy be' (RW — the priests the sons of Levi; 351:1 EVERY RULING FROM THE LEVITES' MOUTH — CALLED); the readback row 33:10 the kin by CALL"),
 ('courts_prophet', "33:10's teaching is 17:8-11's high court at the place (CP.the_high_court — the_distinguished_judge_and_the_three_grades, the_court_at_yavneh_and_the_priests — the priests a duty not a condition; high_court_at_the_place_commanded 1 — CALLED); 352:6's sanctuary higher than the world with 17:8 at 33:12; the readback rows 33:10, 33:12 the kin by CALL"),
 ('festivals_judges', "33:18's Issachar 'in your tents' is Onkelos's 'to make the times of the festivals in Jerusalem' — the court that fixes the months (FJ.DATA the_intercalation; FJ.the_three_pilgrimages — 16:16's three times; Rosh Hashanah 2:8-9 the cases — CALLED); the readback row 33:18 the kin by CALL"),
 ('good_land', "33:24's 'let him dip his foot in oil' is 8:8's olive oil (GL.DATA the_seven_species_seat — by reference); 33:25's 'iron and brass' 8:9's hills of brass (by reference); the readback rows 33:24, 33:25 the kin by CALL"),
 ('blessing_and_curse', "33:28's 'his heavens drop down dew' is 11:14's rain in its season (BC.rain_dates — by reference; 356:8's dew with 32:2's four rains); 33:13's dew of heaven the same; the readback rows 33:13, 33:28 the kin by CALL"),
 ('release_firstborn', "33:21's 'he executed the righteousness of the LORD' is MOSES' RIGHTEOUSNESS THE POOR LAW of 15:7 (the Sifrei 355:9; RF.DATA the_needy_condition, lend_not_borrow — hand_opening_commanded 1 on Israel — CALLED); the readback row 33:21 the kin by CALL"),
 ('persons_poor_court', "33:21's 'and His ordinances with Israel' — the compiled poor and court laws of chapters 22-25 (PP — the persons of the cases; 355:9-10's righteousness under the throne — by reference); the readback row 33:21 the kin by CALL"),
 ('bamidbar', "33:6's 'let his men be a number' is Reuben's census count (BM.census — counted 22 on israel_people — by reference; 347:5); 33:17's myriads of Ephraim the census's numbers; BM.levites the Levites' strip (352:10's strip named beside it); the readback rows 33:6, 33:17 the kin by CALL"),
 ('naso', "33:16's 'him that is separate from his brethren' is THE NAZIRITE'S HOMOGRAPH named at 353:8 — the crown's word, FALSE for the nazirite's law (NA — by reference, the homograph named); the readback row 33:16 the kin by CALL"),
 ('korach', "33:11's 'those who rise up against him' is KORAH the riser (352:1-4 — KO — put_to_death on korach the tape's entry; the Levites' gifts KO.the_gifts — levites_portion_given 1, inheritance_barred 2, priestly_dues_granted 1 UNMOVED — CALLED); the readback row 33:11 the kin by CALL"),
 ('vestments', "33:8's 'Your Thummim and Your Urim' is Exodus 28:30's breastplate of judgment (VE.breastplate — the Urim's one Torah seat of wearing — by reference); the readback row 33:8 the kin by CALL"),
 ('priesthood', "33:9's 'of his father and of his mother' is Leviticus 21:11's high priest's phrase (PR — by reference); 33:10's whole offering the priests' altar service; the readback rows 33:9, 33:10 the kin by CALL"),
 ('zelophehad', "33:17's 'majesty is his' is Numbers 27:20's 'put of your splendor upon him' (353:9 — ZE.the_succession — invested_office on yehoshua; Avot 1:1's Moses to Joshua the handing at 33:4 — CALLED); the readback rows 33:4, 33:17 the kin by CALL"),
 ('second_census', "33:6's 'a number' is Reuben's second count (SC2 — the tape's own number, no number line here — by reference; the parser silent on the noun); the readback row 33:6 the kin by CALL"),
 ('borders', "33:23's 'possess the sea and the south' and 33:19's 'the abundance of the seas' are the land's borders (BO — by reference; Onkelos's Gennesar 355:14-17); the readback rows 33:19, 33:23 the kin by CALL"),
 ('place_name', "33:12's 'He dwells between his shoulders' is the sanctuary in Benjamin's portion — 12:5's place chosen 'in one of your tribes' (PN.the_place_chosen — in_one_of_your_tribes: BENJAMIN'S STRIP the callee's row, Zevachim 118b; THE SANCTUARY'S TRIBE the OPEN parameter with 352:10's dispute — CALLED); 33:19's mountain Onkelos's sanctuary house; 33:29's high places the ban 12:2's (high_places_banned 3 — FALSE by homograph); the readback rows 33:12, 33:19, 33:29 the kin by CALL"),
 ('obey_horeb', "33:1's 'and this is the blessing' is 4:44's frame 'and this is the law' five in order (OH.DATA the_frame — CALLED); 33:26's 'none like the God of Jeshurun' the creed's kin 4:35, 4:39 (OH.DATA the_creed — a REFERENCE); 33:27's 'destroy' 4:26's word; the readback rows 33:1, 33:26, 33:27 the kin by CALL"),
 ('seven_nations', "33:27's 'He thrust out the enemy from before you, and said: destroy' is 7:1-2's seven nations (SN.the_holy_people — chose_you; nations_dispossessed_as_sihon_and_og_promised 1, kings_smitten 3 UNMOVED; 356:3's two fates — the Girgashites who fled — CALLED); the readback row 33:27 the kin by CALL"),
 ('hear_o_israel', "33:8's 'whom You proved at Massah' is 6:16's 'as you tried Him at Massah' inside the book (HO — by reference); 33:26's 'none like' the creed 6:4's (HO's creed — by reference); the readback rows 33:8, 33:26 the kin by CALL"),
 ('moadim', "33:18's festivals' times (Onkelos) are Leviticus 23's appointed seasons (MO — the registry's festival_dates the parameter already, no clock word — by reference; Rosh Hashanah 2:8-9 the court's proclamation binds); the readback row 33:18 the kin by CALL"),
 ('offerings', "33:10's 'whole burnt offering upon Your altar' is Leviticus 1's burnt offering (OF — 351:3-4's limbs — by reference); 33:19's 'sacrifices of righteousness' the peace offerings; the readback rows 33:10, 33:19 the kin by CALL"),
 ('firstfruits_ebal_curses', "33:2's fiery law is the Torah written on Ebal's stones in seventy tongues (343:5 — Sotah 7:5 the case; FE — six_tribes_on_gerizim_to_bless 1, six_tribes_on_ebal_for_the_curse 1 — CALLED); the readback row 33:2 the kin by CALL"),
 ('shelach', "33:9's covenant kept 'at the spies' (350:3's second reading — SH — by reference); Numbers 14:17's pointer on the chapter's words the recon found (shelach's RUN_CITATION); the readback row 33:9 the kin by CALL"),
 ('journeys', "33:2's Seir and Paran are Numbers 33's stations (JN — by reference; 33:38-40 Aaron's death the retelling that never writes — 20b's find); the readback row 33:2 the kin by CALL"),
 ('midian', "349:1's Simeon borrowed again at Zimri — Numbers 25 and 31 on the tape (MI — by reference; Simeon under Judah the DATA row, no write on simeon); the readback row 33:7 the kin by CALL"),
 ('mamre', "33:29's 'the shield of your help' is Genesis 15:1's 'I am your shield' (shield_promised 1 on abraham — MA — a REFERENCE by the ink's word); 352:9's Abraham seeing the house (Genesis 22:14); the readback row 33:29 the kin by CALL"),
 ('pre_sinai', "33:2's Torah offered to the nations and refused (343:6) is the nations' seven commandments (PS.noahide — Tosefta Avodah Zarah 9:4 the case; the parameter the_seven_commandments_of_the_nations — CALLED); the readback row 33:2 the kin by CALL"),
]
assert len(REF) == 39 and len({t for t, _ in REF}) == 39 and [t for t, _ in REF] == S.EDGES, ([t for t, _ in REF][:5], S.EDGES[:5])
if f'\n  {R}:' not in text.split('\nedges:')[0]:
    a = "  song_charge_nebo: [[Deut, 32, 1, 52]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + f"  {R}: [[Deut, 33, 1, 29]]   # THE DEUTERONOMY WALK 21b (2026-09-29; DEUTERONOMY_WALK.md \"Sitting 21b\" — LEAN): chapter 33 in ONE runner over one frozen unit (deu_33_ve_zot — the blessing 33:1-29): the man of God and the theophany, the law the inheritance and the king in Jeshurun, Reuben and Judah, Levi, Benjamin, Joseph, Zebulun and Issachar, Gad, Dan, Naphtali and Asher, the rider of the heaven, Israel dwelling alone; ELEVEN own-day lines in TWO FORMS (1 act, 10 speech) at Moses' last day (40, 12, 7) — NO MARKER (19b's at 31:1); the daemon law_blessing_of_moses given_at Deut 33:1, installed_by boot\n" + text[j + 1:]
    edges = ''.join("  - {from: %s, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: %s}\n" % (R, to, q(W + why)) for to, why in REF)
    k = text.rfind('  - {from: song_charge_nebo, to: '); e = text.index('\n', text.index('why:', k)) + 1
    text = text[:e] + edges + text[e:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(text)
n_ch = sum(1 for e in dep['edges'] if e['from'] == R); n_tr = sum(1 for e in dep['edges'] if e['from'] == R and e.get('link') == 'transfer')
missing = [e['to'] for e in dep['edges'] if e['from'] == R and e['to'] not in dep['spans']]
owed = [p for p in dep['pointers'] if p.get('disposition') == 'OWED']
assert R in dep['spans'] and dep['spans'][R] == [['Deut', 33, 1, 29]] and n_ch == 39 and n_tr == 0 and not missing, (dep['spans'].get(R), n_ch, n_tr, missing)
assert not owed, len(owed)
print('dependency: the span (one range) + %d edges (%s %d CALL — all reference; the token-demanded edges and the pointers after the gate\'s print); OWED pointers in the file: %d; edges %d, pointers %d' % (n_ch, R, n_ch, len(owed), len(dep['edges']), len(dep['pointers'])))
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
old = "len(real) == 82 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): 81 -> 82,"
if old in text:
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 83 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): 82 -> 83, law_blessing_of_moses (given_at Deut 33:1 — and this is the blessing; installed_by boot; one daemon over one chapter and one unit, eleven lines in two forms, no marker, no reuse); 20b: 81 -> 82,")
    if not CHECK: open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 83" in text
print('installation_probes I5: 83')
# ---- THE CALENDAR UNTOUCHED (no clock word in the blessing; 33:18's festivals' times Onkelos's — the registry's festival_dates the parameter already) ----
cal = yaml.safe_load(open(f"{ROOT}/World/step9/calendar_parameters.yaml", encoding='utf-8'))['parameters']
assert len(cal) == 75 and 'the_death_date_of_moses' in cal and not any('Deut 33:' in str(v.get('source', '')) for k, v in cal.items()), len(cal)
print('calendar: %d parameters, untouched (the_death_date_of_moses 19b\'s — the marker\'s day the runner reads; no Deut 33 source)' % len(cal))
# ---- THE REGISTER FILE UNTOUCHED — no seat in the chapter ----
rg = yaml.safe_load(open(f"{ROOT}/World/step9/register_dispositions.yaml", encoding='utf-8'))
seats = [k for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut 33:', str(k))]
assert seats == [], seats
print('register: untouched (no seat at Deut 33; footers %d)' % len(rg.get('footers', {})))
print('TYPES B OK' + (' (check)' if CHECK else ''))
