import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b — THE COMPILE OF CHAPTERS 29-31, LEAN (2026-09-27): THE TYPES BY SCRIPT, part B — daemon_dispositions (law_covenant_return_charge — given_at
# Deut 29:1, installed_by boot; the watches the twenty lines IN THREE FORMS with their writes NEW AND REUSED (13b's form — a reused effect is the line's write too); the functions block
# SIXTEEN WRAPPED: the fifteen cells and the_readback); dependency_dispositions (the span's THREE RANGES [[Deut, 29, 1, 28], [Deut, 30, 1, 20], [Deut, 31, 1, 30]], THIRTY-THREE CALL edges by
# the ink, all REFERENCE — the census decides the rest; NO owed pointer in the file — 15b's owed pointer row for 31:10 lives in COMPILE_DEBT's lean box, PAID by the hakhel's line and the
# readback row at the tail); installation_probes I5 80 -> 81; TWO calendar rows (the_hakhel_time, the_death_date_of_moses — the received channel, clock data on the calendar's keys; the
# death date THE MARKER'S DAY) and the_release_date's exercised_by extended (the hakhel reads the release's date by CALL); THE REGISTER FILE UNTOUCHED (no seat in the three chapters).
# add_types_ch26_b.py's form; the names READ from the spec module beside this file. RUN FROM THE REPO ROOT.
import yaml, subprocess, re, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch29b_spec as S
CHECK = '--check' in sys.argv
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
W = "THE DEUTERONOMY WALK 19b (2026-09-27) | "
R, DM = S.RUNNER, S.DAEMON
CELLS = [S.CELLS['F%d' % i] for i in range(1, 16)] + ['the_readback']
assert len(CELLS) == 16
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
NOTE = {'moab_recital_declared': "Deut 29:1-8: the recital a RETELLING (the plagues, the manna, the garment and the foot, Sihon and Og — reference rows), keep the words of this covenant — a STATUS (NEW); at the counter's day (40, 11, 1), before the marker",
        'covenant_oath_entered_declared': "Deut 29:9-14: standing before the LORD, the covenant's oath, the covenant with those not here — STATUSES (NEW; the four classes, Onkelos's momata), entered_the_covenant REUSED at 29:11 (a fourth entry) and became_the_lords_people_this_day at 29:12 (a second); at the counter's day, before the marker",
        'hidden_idolater_curse_declared': "Deut 29:15-20: the heart turning, the stubborn self-blessing — BLOCKS (NEW), unpardoned, the book's curses, the name blotted, separated for evil — HEAVEN entries (NEW; conditional — the individual under the nation's curse); at the counter's day, before the marker",
        'land_desolation_answer_declared': "Deut 29:21-27: brimstone and salt like Sodom, the nations' answer, uprooted and cast out — HEAVEN entries (NEW; conditional; the ketiv and the qere a DATA row; 'like the overthrow' a comparative pointer FALSE); at the counter's day, before the marker",
        'hidden_and_revealed_declared': "Deut 29:28: the hidden the LORD's, the revealed ours — STATUSES (NEW; the dotted letters a DATA row, Sanhedrin 43b owed); at the counter's day, before the marker",
        'return_and_gathering_declared': "Deut 30:1-5: the return the condition — a STATUS (NEW), the captivity returned, gathered from the peoples and from the end of heaven, brought in and multiplied — HEAVEN entries (NEW; conditional on the return; the exile case's recovery arm by call); at the counter's day, before the marker",
        'heart_circumcised_declared': "Deut 30:6-10: the heart circumcised by the LORD, the curses on the enemies, abounding, rejoiced over — HEAVEN entries (NEW; 10:16's command made the act; the false six guarded at 30:9, the pointer FALSE), return and hearken and do — a STATUS (NEW); at the counter's day, before the marker",
        'commandment_near_declared': "Deut 30:11-14: not too hard nor far, not in heaven nor beyond the sea, in the mouth and the heart — STATUSES (NEW; the court on earth by call; Bava Metzia 59b owed); at the counter's day, before the marker",
        'life_and_death_choice_declared': "Deut 30:15-20: life and death set, choose life — STATUSES (NEW), living and multiplying, perishing, the length of days — HEAVEN entries (NEW; THE STATE ROW's two arms), heaven_and_earth_witness REUSED at 30:19 (a third entry), blessing_and_curse_set at 30:19 (a second), cleaving_commanded at 30:20 (a third); at the counter's day, before the marker",
        'crossing_charge_declared': "Deut 31:1-6: Joshua to cross, be strong and courageous — STATUSES (NEW), the nations dispossessed as Sihon and Og — a HEAVEN entry (NEW; the second and third AS_WHEN pointers run citations), fear_not_promised REUSED at 31:6 on Israel (a fifth entry — the first on Israel's ledger); THE MARKER'S DAY (40, 12, 7) — 31:2's hundred and twenty, the marker placed at 31:1",
        'joshua_charged_before_israel': "Deut 31:7-8 (an ACT): Joshua charged to bring Israel in — a STATUS on yehoshua (NEW; Moses' public charge), fear_not_promised REUSED at 31:8 on yehoshua (a sixth entry); at the marker's day",
        'law_written_given': "Deut 31:9 (an ACT): the law written and given to the priests and the elders — a STATUS (NEW; the second of the four writings; the ark's bearers by call); at the marker's day",
        'hakhel_reading_declared': "Deut 31:10-13: the hakhel's reading, the assembly of all, the children to hear and learn — STATUSES (NEW; the clock the calendar parameter the_hakhel_time — Sotah 7:8; the reader the king, the text Deuteronomy, the portions lines on the tape; 15b's owed pointer row for 31:10 PAID); at the marker's day",
        'tent_summons_cloud_appeared': "Deut 31:14-15 (an ACT): Moses' days approach to die — a STATUS on moses (NEW; Berakhot 9:2's blessing a parameter), glory_appeared REUSED at 31:15 on the_tent_of_meeting (a seventh entry — the cloud's last standing; the three gifts' daemon owed to 34:5); at the marker's day",
        'apostasy_and_hidden_face_foretold': "Deut 31:16-18 (a SPEECH of the LORD): Moses to sleep with the fathers — a STATUS on moses (NEW), the whoring, the covenant broken, the face hidden, the evils — HEAVEN entries (NEW; the foreknowledge as conditional state; Onkelos 'I will remove My Shekhinah'); at the marker's day",
        'song_witness_commanded': "Deut 31:19-21 (a SPEECH of the LORD): the song's writing, its teaching, its witness office — STATUSES (NEW; the song chapter 32's — sitting 20's; 'sated' the seven's homograph guarded); at the marker's day",
        'song_written_taught': "Deut 31:22 (an ACT): the song written and taught by Moses — a STATUS (NEW; the fourth of the four writings; 'the same day' the marker's); at the marker's day",
        'joshua_commissioned_at_tent': "Deut 31:23 (a SPEECH of the LORD): Joshua commissioned to bring Israel in — a STATUS on yehoshua (NEW; the second commission, by the LORD's mouth), the LORD with Joshua — a HEAVEN entry on yehoshua (NEW; Joshua 1:5 the run, a pointer ahead owed); at the marker's day",
        'book_beside_the_ark_declared': "Deut 31:24-27: the book beside the ark — a STATUS on the_levites (NEW; the_books_place two arms — Bava Batra 14a-b on the kin), the book a witness — a STATUS (NEW; the stiff neck's seventh seat at 31:27); at the marker's day",
        'assembly_and_song_spoken_declared': "Deut 31:28-30: the elders and the officers assembled, the song spoken to its end — STATUSES (NEW), the corruption after Moses' death — a HEAVEN entry (NEW; Moses' foretelling the LORD's twin), heaven_and_earth_witness REUSED at 31:28 (a fourth entry — the chain's fourth seat); at the marker's day"}
assert set(NOTE) == set(S.KINDS)
if f'  {DM}:' not in text:
    lines = []
    for kind, first, rng, claim, cell, form, fields, effs, reuses in S.LINES:
        ws = [e for e, _, _ in effs] + [e for e, _, _ in reuses]
        lines.append('      %s: [%s]   # %s\n' % (kind, ', '.join(ws), NOTE[kind]))
    block = (f'  {DM}:\n    file: cold_run_{R}.py\n    wraps: {R}\n    given_at: Deut 29:1\n'
             '    installed_by: boot   # THE DEUTERONOMY WALK 19b (2026-09-27; THE LEAN PASS): "AND MOSES CALLED TO ALL ISRAEL … YOU HAVE SEEN ALL THAT THE LORD DID" — the three chapters\' first verse at the counter\'s day (40, 11, 1); installed by boot like law_opening_speech through law_firstfruits_ebal_curses (the Deuteronomy daemons\' form; THE INSTALL HYPOTHESIS on the table unchanged); ONE daemon over THREE chapters and three units — the covenant in Moab, the return and the choice, the charge, the hakhel, the Tent, the song and the book; the hakhel, the song as a witness and the book beside the ark its three NEW families; TWENTY lines in THREE FORMS (13 statute, 4 act, 3 speech of the LORD); the 9 lines of chapters 29-30 BEFORE the marker at (40, 11, 1), the 11 of chapter 31 AFTER THE ONE MARKER at 31:1 (the number\'s verse 31:2 — Moses\' hundred and twenty; the day (40, 12, 7) the 7th of Adar by the answer sheet, Tosefta Sotah 11:3)\n'
             '    watches:\n' + ''.join(lines))
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if f'\n  {R}:   # THE DEUTERONOMY WALK 19b' not in text:
    fb = f'  {R}:   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN — three chapters, three units, one daemon, one marker)\n' + ''.join('    %s: {status: WRAPPED, by: %s}\n' % (c, DM) for c in CELLS)
    i = text.index('  firstfruits_ebal_curses:   # THE DEUTERONOMY WALK 18b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(text)
NW = sum(len(l[7]) + len(l[8]) for l in S.LINES)
assert DM in dd['daemons'] and R in dd['functions'] and len(dd['functions'][R]) == 16 and len(dd['daemons'][DM]['watches']) == 20 and sum(len(v) for v in dd['daemons'][DM]['watches'].values()) == NW == 68, (len(dd['functions'].get(R, [])), len(dd['daemons'].get(DM, {}).get('watches', {})), NW)
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']; ev = yaml.safe_load(open(f"{ROOT}/World/step9/event_vocabulary.yaml", encoding='utf-8'))['events']
for k, v in dd['daemons'][DM]['watches'].items():
    assert k in ev, k
    for e in v: assert e in fx, e
assert {ev[k]['form'] for k in dd['daemons'][DM]['watches']} == {'statute', 'act', 'speech'}
print('daemons: %d (%s %s); functions blocks: %d; the watches %d writes over 20 lines in three forms' % (len(dd['daemons']), DM, DM in dd['daemons'], len(dd['functions']), NW))
# ---- the dependency span (three ranges) + the CALL edges by the ink (thirty-three REFERENCE; the token-demanded edges and the five AS_WHEN pointers after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
REF = [
 ('opening_speech', "31:14 and 31:23's commission is Numbers 27:12-23's compiled there (OS.the_commission('the_shepherd', 'the_hand_laid', 'the_honor', 'the_urim', 'the_receipt', 'the_debit') CALLED — 31:2's 'go out and come in' the shepherd's phrase; the debit OPEN to 34:1-4); 29:4's forty years 2:7's (OS.the_bypass); 29:6-7 and 31:4's Sihon and Og 2:26-3:17's retelling (OS.sihon_and_og — the eleven asks); 31:28's officers 1:15's; 31:2-3 and 31:7-8 against moses_besought and joshua_encouraged (3:21-28 — the tape's own lines, the second AS_WHEN pointer's referent); the readback rows 29:4, 29:6-7, 31:2-4, 31:7-8, 31:14, 31:23, 31:28 the kin by CALL"),
 ('gad_reuben', "29:7's 'the Reubenite, the Gadite and the half tribe of Manasseh' is Numbers 32:28-33's holding east (GR.the_acceptance_and_the_charge CALLED — the dividers, Joshua among them; holding_given on the half tribe the tape's); the readback row 29:7 the kin by CALL"),
 ('good_land', "29:4's garment and foot are 8:4's STATE told again in the plural (GL.the_way_of_forty_years('the_garment_and_the_foot', 'keep_walk_fear') CALLED — no line on the tape, the SUPPLIED row referenced); 30:16's 'walk in His ways … live and multiply' 8:1 and 8:6's; 30:17-18 and 29:25's 'serve and bow' 8:19-20's testimony (GL.the_testimony('other_gods_serve_bow', 'if_you_forget')); 31:20's satiety before rebellion 8:12-14's (GL.take_heed_lest_you_forget); NO receipt in the three chapters (GL.receipt_seats(29), (30), (31) -> [], [], []); the readback rows 29:4, 29:25, 30:16-18, 31:20 the kin by CALL"),
 ('exodus_story', "29:1-2's signs and wonders retell the plagues and the going out (ES.plagues, ES.sinai CALLED — plague_struck THIRTEEN the tape's UNMOVED); 29:5's no bread the manna's forty years (Exodus 16:35); 31:2's hundred and twenty checked against Exodus 7:7's 'Moses was eighty' (the tape's own line — THE MARKER'S YEAR); 31:15's pillar of cloud Exodus 13:21's (pillar_leads ONE UNMOVED); 31:23's 'I will be with you' Exodus 3:12's form; the readback rows 29:1-2, 29:5, 31:2, 31:15, 31:23 the kin by CALL"),
 ('covenant_at_horeb', "29:1's opening is 5:1's seven in order and 31:12's four verbs 5:1's (CH.the_assembly_called('hear_learn_keep_do', 'not_with_our_fathers') CALLED — 5:3's 'not with our fathers' the DATA note against 29:13-14, no link of our own); 31:12's 'the day of the assembly' 9:10's Horeb verb (the hakhel's model — a reference); 29:15-17's other gods the second word's block (other_gods_barred ONE UNMOVED); the readback rows 29:1, 29:13-14, 29:17, 31:12 the kin by CALL"),
 ('hear_o_israel', "30:2, 30:6 and 30:10's 'with all your heart and with all your soul' are 6:5's pair (HI.the_creed('with_all_your_heart') CALLED — the two inclinations at 31:21); 30:20's oath of the land 6:10's (HI.the_gift_and_the_warning — a relative clause, no pointer); 31:19's 'teach it' 6:7's; the readback rows 30:2, 30:6, 30:20, 31:19, 31:21 the kin by CALL"),
 ('seven_nations', "29:12's 'as He swore to your fathers' is the oath by kind — the three lines on the tape (SN.the_holy_people('the_oath') CALLED — the first AS_WHEN pointer a RUN CITATION); 29:19's 'blot out his name from under heaven' 7:24's (SN.DATA the_name_from_under_heaven); 30:7's curses on the enemies 7:15's diseases (SN.because_you_hear('the_diseases')); 31:3's 'He will destroy these nations' 7:1-2's ban and 31:5's 'all the commandment' 7:2's; the readback rows 29:12, 29:19, 30:7, 31:3, 31:5 the kin by CALL"),
 ('obey_horeb', "30:1-10's return is 4:29-31's recovery arm told fully — THE CELL READ THESE VERSES FORWARD ('30:2's kin', '30:10's kin'; OH.the_exile_case('in_your_distress_return', 'seek_and_find', 'perish_and_scatter', 'serve_wood_and_stone', 'the_merciful_god', 'the_case_head') CALLED); 30:19 and 31:28's heaven and earth 4:26's — the chain of witnesses (OH.DATA the_witnesses_chain — 4:26, 30:19, 31:28, 32:1; heaven_and_earth_witness REUSED twice); 29:25's 'whom He had not apportioned' 4:19's host (OH.no_image('the_host_apportioned', 'consuming_fire_jealous_god') — the Sifrei 148:8's pair); 29:16's wood and stone 4:28's; 31:29's corruption 4:25's case head; the readback rows 29:16, 29:19-20, 29:25, 30:1-4, 30:10, 30:17-19, 31:6, 31:17-18, 31:28-29 the kin by CALL"),
 ('second_tablets', "31:9 and 31:25's Levites who carry the ark are 10:8's office (ST.the_levites_separated('to_carry_the_ark') CALLED); 31:26's 'beside the ark' the two arms on the kin (ST.DATA the_arks_contents_two_arms — R. Meir inside, R. Yehuda beside — Bava Batra 14a-b; ST.DATA kings_reads_the_ark; fragments_in_the_ark ONE UNMOVED); 31:7's charge 10:11's seven tokens (ST.the_third_forty_and_the_go('the_charge_forward'); ST.DATA the_charge_to_joshua — 'THE RUN IS JOSHUA'); 30:6's circumcised heart 10:16's command (heart_circumcision_commanded ONE UNMOVED — its ink names '30:6 the passive form'); 31:27's stiff neck 10:16's block (stiffening_barred ONE UNMOVED — '31:27 forward'); 30:20's cleaving 10:20's (cleaving_commanded REUSED a third time); the readback rows 30:6, 30:20, 31:7, 31:9, 31:23, 31:25-27 the kin by CALL"),
 ('not_righteousness', "31:27's 'your neck the stiff' is the stiff neck's SEVENTH SEAT in a new word order (NR.DATA the_stiff_necks_six_seats CALLED — 9:6, 9:13, Exodus 32:9, 33:3, 33:5, 34:9 the calf's six); 31:27's 'your rebellion' 9:7 and 9:24's; 29:12's oath to the three fathers 9:5's (NR.DATA the_merit_of_the_fathers); 31:29's 'turn aside' 9:12's; the readback rows 29:12, 31:27, 31:29 the kin by CALL"),
 ('blessing_and_curse', "30:15's 'see, I have set before you this day' is 11:26's form — THE CELL READ THESE VERSES FORWARD ('30:15-20 the run forward'; BC.the_blessing_and_the_curse('see_i_set_before_you', 'the_curse_if') CALLED; BC.narrative names 30:15); 30:1 and 30:19's 'the blessing and the curse' 11:26's pair (blessing_and_curse_set REUSED a second time); 31:29's 'turn aside from the way' 11:28's; the readback rows 30:1, 30:15, 30:19, 31:29 the kin by CALL"),
 ('seducers', "29:17's individual whose heart turns is 13:7's inciter in secret (SE.the_inciter CALLED — the kin of the hidden idolater); 29:12's 'as He swore to your fathers' 13:18's pointer row the form (SE.the_whole_offering_the_heap_and_the_mercy('as_he_swore_to_your_fathers')); 30:20's cleaving 13:5's second seat; the readback rows 29:12, 29:17, 30:20 the kin by CALL"),
 ('food_tithe', "31:10's 'at the end' is the source seat of the removal's end analogy (FT.the_third_year('the_removal_date') CALLED — 'the Sifrei 109:1-3 — I2 with 31:10': the spine's own transfer runs FROM this verse; a reference for us; FT.effect_scan names 31:10 an expected seat — censused); the readback row 31:10 the kin by CALL"),
 ('release_firstborn', "31:10's 'at the end of seven years, at the set time of the year of release' is 15:1's release at the year's end (RF.the_release('the_release_at_the_years_end') CALLED — \"'end' is the year's end by I2 with 31:10 (the Sifrei 111:1; Rosh Hashanah 8b)\": the spine's own analogy FROM 31:10, a reference for us; the release's date the calendar row the_release_date read by CALL — 'no count' on the bare world; RF.effect_scan names 29:12 and 31:10 — censused before the fast checker); the readback row 31:10 the kin by CALL"),
 ('festivals_judges', "31:10's 'at the feast of booths' and 31:11's 'to appear before the LORD' are 16:13-16's (FJ.the_feast_of_booths('the_seven_days'), FJ.the_three_pilgrimages('the_three_times', 'who_appears', 'the_exempt_from_appearing') CALLED — booths_at_the_place_commanded ONE UNMOVED, its ink naming '31:10-11 ahead'; the hakhel's assembly WIDER than the pilgrimage's — Chagigah 1:1's exempt come); the readback rows 31:10-12 the kin by CALL"),
 ('courts_prophet', "31:11's reader is the king and the text his copy of 17:18 (CP.the_king('from_among_your_brothers_and_agrippas', 'the_copy_of_the_law') CALLED — 157:10 = Mishnah Sotah 7:8 read whole there; law_copy_commanded ONE UNMOVED, its ink naming '31:9-13 ahead': THE POINTER ROW 15b OWED FOR 31:10 PAID by this line); 30:11-14's 'not in heaven' the court on earth (CP.the_high_court — 17:8-11); the readback rows 30:11-14, 31:9-11 the kin by CALL"),
 ('firstfruits_ebal_curses', "29:19's 'all the curse written in this book' and 30:7's curses on the enemies are chapter 28's (FE.the_curses_of_the_house_and_the_field, FE.the_curses_of_the_siege_and_the_exile CALLED — curses_for_not_hearkening ONE UNMOVED); 30:9's three fruits 28:11's (FE.the_blessings('plenteous_in_goods_womb_beast_and_ground')); 30:9's 'rejoiced' THE FALSE SIX's twin (FE.DATA the_false_six — '30:9's twin ahead'; the pointer FALSE); 29:27 and 30:3's scattering 28:64's; 29:8's 'the words of this covenant' 28:69's footer (FE.DATA the_three_covenants); 29:28 and 31:12's 'all the words of this law' 28:58's; 31:20's milk and honey 26:9, 26:15's; 31:9's elders 27:1's; the readback rows 29:8, 29:19, 29:27-28, 30:3, 30:7, 30:9, 31:9, 31:12, 31:20 the kin by CALL"),
 ('refuge_war_family', "31:6's 'fear not nor be dismayed' is the war chapter's priest's speech 20:3-4 (RW.the_priests_speech('when_you_go_out_to_war') CALLED — 7:18's rule paid there); 31:5's 'according to all the commandment' the ban 20:16-18; the readback rows 31:5-6 the kin by CALL"),
 ('tochacha', "29:22's desolation, 29:27 and 30:3's scattering, 31:16 and 31:20's 'break My covenant' and 31:17's devouring are Leviticus 26:15, 26:32-33, 26:38's twins (TC.covenant, TC.cascade CALLED — land_desolate ZERO, scattered_among_nations ZERO on the world: the transfers never fired); 30:2's return Leviticus 26:40-42's confession and remembering (TC.covenant — the recovery branch's predicates); the readback rows 29:22, 29:27, 30:2-3, 31:16-17, 31:20 the kin by CALL"),
 ('yovel', "31:10's year of release is the sabbatical cycle's seventh (YV.cycle(7) CALLED — the year's class sabbath_of_the_land; the count not begun on the bare world — 'no count', 13b's precedent: the era asked for before its method); the readback row 31:10 the kin by CALL"),
 ('calendar', "31:10's release year and 31:11's appearing are Exodus 23:10-11's sabbatical and 23:14-17's pilgrimages (CA.sabbatical, CA.pilgrimages CALLED — appearance_owed ZERO on the world: Exodus 23:17's heaven entry never written on Israel, a find for the docket); the readback rows 31:10-11 the kin by CALL"),
 ('moadim', "31:10's feast of booths is Leviticus 23:34-43's seven days (MD.sukkot() CALLED — the fifteenth of the seventh month the key sukkot_1 of the_hakhel_time); the readback row 31:10 the kin by CALL"),
 ('musafim', "31:10's feast of booths' days are Numbers 29:12-38's with the eighth its own festival (MU.sukkot('the_eighth') CALLED — the hakhel the night after the FIRST day, Sotah 7:8, not the eighth); the readback row 31:10 the kin by CALL"),
 ('mamre', "29:22's 'like the overthrow of Sodom and Gomorrah' is Genesis 19:24-25's (MA.scene CALLED — sodom's two heaven entries the tape's; 'brimstone' at Genesis 19:24 and here alone in the Torah; 'like the overthrow' a comparative — the pointer FALSE); the readback row 29:22 the kin by CALL"),
 ('primeval', "31:2's hundred and twenty is Genesis 6:3's number (PV.prologue CALLED — reprieve_of_a_hundred_and_twenty ONE UNMOVED, a TIMER on the flood's generation whose ink names 31:2 and 34:7 'book-bound': a reference, no transfer); 31:21's 'their inclination' Genesis 6:5 and 8:21's (PV.scene); the readback rows 31:2, 31:21 the kin by CALL"),
 ('family', "31:16's 'you shall sleep with your fathers' is Genesis 47:30's 'I will lie with my fathers' — Jacob's testament (FA.testament CALLED — the narrative def naming 31:16); 29:21's later generation FA.mrow; the readback row 31:16 the kin by CALL"),
 ('erection', "31:15's pillar of cloud at the door is Exodus 33:9-10's four in order (ER.presence CALLED); 29:19's blotting Exodus 32:33's book (blotted_from_the_book ONE UNMOVED); 31:16's 'whore after' Exodus 34:15-16's form; 31:27's stiff neck Exodus 32:9's; the readback rows 29:19, 31:15-16, 31:27 the kin by CALL"),
 ('beha', "31:14's 'present yourselves in the tent' is Numbers 11:16's elders' summons and 31:15's cloud at the door Numbers 12:5's (BH.narrative, BH.miriam CALLED — the_seventy_elders the tape's entity, spirit_rested); the readback rows 31:14-15 the kin by CALL"),
 ('chukat', "31:2's death date is the shelf's on the kin — 'Moses the seventh of Adar (Seder Olam 10:2)' (CK.edom_and_hor('death_dates', 'succession', 'thirty_days') CALLED — Aaron's death at (40, 5, 1) the eras' precedent; THE MARKER'S DAY (40, 12, 7) the Tosefta's computation read whole at the design); 31:4's Sihon and Og Numbers 21:21-35's (CK.well_and_kings('og_lore', 'joshua_refrain') — the refrain born at 21:35); the readback rows 31:2, 31:4 the kin by CALL"),
 ('journeys', "31:9 and 31:22's writings are the second and fourth of THE FOUR WRITINGS (JR.DATA the_four_writings CALLED — Exodus 24:4, Numbers 33:2, Deut 31:9, Deut 31:22; JR.lemma_seats names 31:9, 31:22, 34:7); Aaron's death date the eras' stamp (JR.DATA the_death_date); the readback rows 31:9, 31:22 the kin by CALL"),
 ('vestments', "31:14 and 31:23's commission at the Tent stands on Numbers 27:21's Urim (VE.breastplate CALLED — the commission's judgment final at the first commission; the second by the LORD's own mouth); the readback rows 31:14, 31:23 the kin by CALL"),
 ('shelach', "31:1's 'and Moses spoke these words to all Israel' is Numbers 14:39's; 31:17's 'our God is not among us' Numbers 14:42's; 32:44's Hoshea the old name (SH.spies('joshua_name') CALLED — Numbers 13:16 Hoshea to Joshua, the same man); the readback rows 31:1, 31:17, 31:30 the kin by CALL"),
 ('place_name', "31:11's 'the place which He shall choose' is 12:5's (PN.the_place_chosen('the_stations_six_rows', 'the_three_commandments_of_the_entry') CALLED — the hakhel at the place: Shiloh and the House; the Name pronounced only there); the readback row 31:11 the kin by CALL"),
]
assert len(REF) == 33 and len({t for t, _ in REF}) == 33 and [t for t, _ in REF] == S.EDGES, ([t for t, _ in REF][:5], S.EDGES[:5])
if f'\n  {R}:' not in text.split('\nedges:')[0]:
    a = "  firstfruits_ebal_curses: [[Deut, 26, 1, 19], [Deut, 27, 1, 26], [Deut, 28, 1, 69]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + f"  {R}: [[Deut, 29, 1, 28], [Deut, 30, 1, 20], [Deut, 31, 1, 30]]   # THE DEUTERONOMY WALK 19b (2026-09-27; DEUTERONOMY_WALK.md \"Sitting 19b\" — LEAN): chapters 29-31 in ONE runner over three frozen units (deu_29_moab_covenant, deu_30_teshuvah_choice, deu_31_charge_torah) — the covenant in Moab, the return and the choice, the charge, the hakhel, the Tent, the song and the book; TWENTY own-day lines in THREE FORMS (13 statute, 4 act, 3 speech); ONE MARKER at 31:1 (the number's verse 31:2 — Moses' hundred and twenty; the day (40, 12, 7) the 7th of Adar); the daemon law_covenant_return_charge given_at Deut 29:1, installed_by boot\n" + text[j + 1:]
    edges = ''.join("  - {from: %s, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: %s}\n" % (R, to, q(W + why)) for to, why in REF)
    k = text.rfind('  - {from: firstfruits_ebal_curses, to: '); e = text.index('\n', text.index('why:', k)) + 1
    text = text[:e] + edges + text[e:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(text)
n_ch = sum(1 for e in dep['edges'] if e['from'] == R); n_tr = sum(1 for e in dep['edges'] if e['from'] == R and e.get('link') == 'transfer')
missing = [e['to'] for e in dep['edges'] if e['from'] == R and e['to'] not in dep['spans']]
owed = [p for p in dep['pointers'] if p.get('disposition') == 'OWED']
assert R in dep['spans'] and dep['spans'][R] == [['Deut', 29, 1, 28], ['Deut', 30, 1, 20], ['Deut', 31, 1, 30]] and n_ch == 33 and n_tr == 0 and not missing, (dep['spans'].get(R), n_ch, n_tr, missing)
assert not owed, len(owed)
print('dependency: the span (three ranges) + %d edges (%s %d CALL — all reference; the token-demanded edges and the five AS_WHEN pointers after the gate\'s print); OWED pointers in the file: %d; edges %d, pointers %d' % (n_ch, R, n_ch, len(owed), len(dep['edges']), len(dep['pointers'])))
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
old = "len(real) == 80 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 18b (2026-09-26; LEAN): 79 -> 80,"
if old in text:
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 81 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): 80 -> 81, law_covenant_return_charge (given_at Deut 29:1 — Moses called to all Israel; installed_by boot; one daemon over three chapters and three units, twenty lines in three forms, one marker); 18b: 79 -> 80,")
    if not CHECK: open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 81" in text
print('installation_probes I5: 81')
# ---- THE TWO CALENDAR PARAMETERS (the received channel — clock data on the calendar's keys; the death date THE MARKER'S DAY) + the_release_date's exercised_by ----
path = f"{ROOT}/World/step9/calendar_parameters.yaml"
text = open(path, encoding='utf-8').read()
if '\n  the_hakhel_time:' not in text:
    rows = ('''  the_hakhel_time:   # THE DEUTERONOMY WALK 19b (2026-09-27): 'at the end of every seven years, at the set time of the year of release, at the feast of booths … you shall read this law before all Israel' (Deut 31:10-11) — THE HAKHEL'S TIME A CLOCK DATUM: the night after the first festival day of booths in the year after the release year, on the release's and the booths' own keys; no marker, no timer on the tape
    era: exodus
    idiom: the_hakhel_time
    value:
      the_night: "AT THE CONCLUSION OF THE FIRST FESTIVAL DAY OF THE FEAST — the key sukkot_1 (the fifteenth of the seventh month), its night's close (Mishnah Sotah 7:8 — 'at the conclusion of the first festival day of the feast, in the eighth, at the end of the seventh')"
      the_year: "IN THE EIGHTH YEAR, AT THE END OF THE SEVENTH — the year AFTER the release year (the_release_date's year by CALL to release_firstborn; the cycle's seventh by yovel.cycle(7)): 'at the end of seven years' the release's end, the Sifrei 111:1's analogy running FROM this verse (I2, checked in MIDDOT.md — a reference for us)"
      the_reading: "THE KING READS DEUTERONOMY from 1:1 — the seven portions of Sotah 7:8 (1:1 to 6:4; 6:4-9; 11:13-21; 14:22-29; 26:12-15; 17:14-20; 28) — every one a LINE ON THE TAPE (the runner's DATA row the_portions_on_the_tape); on a wooden platform in the court; the eight blessings with the festivals' in place of the forgiveness of iniquity"
      the_assembly: "THE MEN, THE WOMEN, THE CHILDREN AND THE STRANGER (31:12 — 29:10's four classes): wider than the pilgrimage's appearing (Chagigah 1:1's exempt come — festivals_judges by CALL); the men to learn, the women to hear, the children for the reward of those who bring them (Chagigah 3a — OWED)"
    boundary: "a clock datum, not a marker — the night after sukkot_1 in the eighth year by the calendar's own keys, the release year's class read by call; on the bare world before the entry the count is not begun — 'no count' (13b's precedent); the first firing Joshua's run, off the tape"
    channel: received
    source: "Deut 31:10-13, 15:1, 16:13-16, 17:18-19; Mishnah Sotah 7:8; the Sifrei on Deuteronomy 109:2, 111:1, 157:10, 160:4, 302:1"
    teacher: "Mishnah Sotah 7:8"
    exercised_by: [covenant_return_charge]
  the_death_date_of_moses:   # THE DEUTERONOMY WALK 19b (2026-09-27): 'I am a hundred and twenty years old THIS DAY' (Deut 31:2) — MOSES' LAST DAY A CLOCK DATUM AND THE ONE MARKER OF CHAPTERS 29-31: the year the ink's (Exodus 7:7's eighty at the exodus + forty), the month and the day the answer sheet's (the 7th of Adar); the counter's day moves to (40, 12, 7)
    era: exodus
    idiom: the_death_date_of_moses
    value:
      the_year: "THE FORTIETH YEAR OF THE EXODUS ERA — THE INK'S: 'Moses was eighty years old when he spoke to Pharaoh' (Exodus 7:7 — the tape's own line) + the forty years of the wilderness = the hundred and twentieth year (31:2's [120] the parser's own number; 34:7's the death's — sitting 22's); Genesis 6:3's hundred and twenty the number's Genesis seat (a reference, no transfer)"
      the_day: "THE SEVENTH OF ADAR — THE ANSWER SHEET'S: Tosefta Sotah 11:3 read whole at the design — 'this day' teaches his years were completed to the day; computed BACKWARD from Joshua 4:19's tenth of Nisan (the people up from the Jordan) by the thirty days' weeping (34:8) and the three days' preparation (Joshua 1:11) — thirty-three days; Seder Olam 10:2 as chukat.edom_and_hor('death_dates') holds it; the Sifrei 2:3's 'completed to the hour'"
      the_month: "ADAR THE TWELFTH MONTH AS THE CLOCK COUNTS IT — whether the fortieth year was intercalated the shelf does not say (the_intercalated_month a PARAMETER — 2:3's row: 1 Kings 4:19's one officer; sitting 14b's intercalation parameter the kin)"
      the_marker: "THE STITCHER'S ROW — placed AT 31:1 (the line crossing_charge_declared's first verse; Genesis 7:1's precedent: the number at 7:4, the position 7:1), the number's verse 31:2 named in its value; the 9 lines of chapters 29-30 at (40, 11, 1) before it, the 11 of chapter 31 at (40, 12, 7) after it; 32:48's 'that same day' and 34:5's death stand on this day"
    boundary: "THE MARKER — the counter's day moves from 1:3's (40, 11, 1) to (40, 12, 7), the first forward date in Deuteronomy since 1:3 and the first marker of the walk since chapter 10's retrograde pair; markers 172 -> 173 (read from the print)"
    channel: received
    source: "Deut 31:2, 31:14, 31:16, 31:22 (the same day), 32:48, 34:5-8; Exodus 7:7; Genesis 6:3; Joshua 1:11, 4:19; Tosefta Sotah 11:3; Seder Olam 10:2; the Sifrei on Deuteronomy 2:3"
    teacher: "Tosefta Sotah 11:3"
    exercised_by: [covenant_return_charge]
''')
    i = text.index('\neras:\n')
    text = text[:i + 1] + rows + text[i + 1:]
old = "    teacher: \"the Sifrei 111:1-11; Rosh Hashanah 8b-9a\"\n    exercised_by: [release_firstborn]\n"
if old in text:
    assert text.count(old) == 1
    text = text.replace(old, "    teacher: \"the Sifrei 111:1-11; Rosh Hashanah 8b-9a\"\n    exercised_by: [release_firstborn, covenant_return_charge]   # THE DEUTERONOMY WALK 19b (2026-09-27): 31:10's hakhel reads the release's date by CALL — the runner exercises the row (31:10 the source seat of the row's own end analogy)\n")
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
cal = yaml.safe_load(text)['parameters']
assert 'the_hakhel_time' in cal and 'the_death_date_of_moses' in cal and cal['the_release_date']['exercised_by'] == ['release_firstborn', 'covenant_return_charge'] and cal['the_hakhel_time']['channel'] == 'received' and cal['the_death_date_of_moses']['exercised_by'] == [R], (cal['the_release_date']['exercised_by'], [k for k in cal if k.startswith('the_')][-4:])
print('calendar: %d parameters (the_hakhel_time, the_death_date_of_moses added; the_release_date exercised_by %s)' % (len(cal), cal['the_release_date']['exercised_by']))
# ---- THE REGISTER FILE UNTOUCHED — no seat in the three chapters (the footer at 28:69 closed the statutes' block) ----
rg = yaml.safe_load(open(f"{ROOT}/World/step9/register_dispositions.yaml", encoding='utf-8'))
seats = [k for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut (29|30|31):', str(k))]
assert seats == [], seats
print('register: untouched (no seat at Deut 29-31; footers %d)' % len(rg.get('footers', {})))
print('TYPES B OK' + (' (check)' if CHECK else ''))
