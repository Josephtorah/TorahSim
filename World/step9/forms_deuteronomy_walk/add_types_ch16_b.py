import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b — THE COMPILE OF CHAPTER 16, LEAN (2026-09-23): THE TYPES BY SCRIPT, part B — daemon_dispositions (law_festivals_judges — given_at
# Deut 16:1, installed_by boot; the functions block SEVEN WRAPPED: the six cells and the_readback — 10b's lesson 4); dependency_dispositions (the span
# [[Deut, 16, 1, 22]] and FIFTEEN CALL edges by the ink, all REFERENCE — the census decides the rest); installation_probes I5 75 -> 76; NO calendar row (the
# festivals' dates and the intercalation on file); THE REGISTER FILE UNTOUCHED (no seat at Deut 16 — the reading's finder). add_types_ch15_p3.py's form. RUN FROM THE REPO ROOT.
import yaml, subprocess
ROOT = _ROOT
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
W = "THE DEUTERONOMY WALK 14b (2026-09-23) | "
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_festivals_judges:' not in text:
    block = '''  law_festivals_judges:
    file: cold_run_festivals_judges.py
    wraps: festivals_judges
    given_at: Deut 16:1
    installed_by: boot   # THE DEUTERONOMY WALK 14b (2026-09-23; THE LEAN PASS): "OBSERVE THE MONTH OF AVIV AND KEEP THE PASSOVER" — the chapter's first verse at the counter's day (40, 11, 1); installed by boot like law_opening_speech through law_release_firstborn (the Deuteronomy daemons' form; THE INSTALL HYPOTHESIS on the table unchanged); THE COURTS NOT A SECOND DAEMON in the lean form (the three tiers a parameter of F5; the second daemon owed to the full process); FIVE OWN-DAY LINES, NO marker; the readback's rows one per verse graded against the kin's cells by CALL and the tape's lines by kind and first verse; no bench scene, no case kind (the lean form — the Mishnah rows the cells' asks)
    watches:
      passover_at_the_place_declared: [passover_at_the_place_commanded, passover_in_the_gates_barred, leaven_with_the_passover_barred, flesh_till_morning_barred, seventh_day_assembly_commanded]   # Deut 16:1-8: the place added to the Passover — a STATUS (NEW), 'you may not sacrifice within your gates', 'you shall not eat leaven with it', 'nor shall the flesh remain until the morning' — BLOCKS (NEW), the seventh day's assembly — a STATUS (NEW; the intermediate days' work the sages' parameter); at the counter's day, no marker
      weeks_and_booths_declared: [weeks_at_the_place_commanded, booths_at_the_place_commanded]   # Deut 16:9-15: the feast of weeks from the sickle's count and the feast of booths at the gathering, each at the place — STATUSES (NEW); the omer's count and the booths' seven by CALL (moadim), the rejoicing by CALL (place_name), the slave remembered by CALL (covenant_at_horeb) — no second write; at the counter's day, no marker
      three_pilgrimages_declared: [three_pilgrimages_commanded, empty_appearance_barred]   # Deut 16:16-17: all the males appear three times at the place — a STATUS (NEW; the exempt list a parameter), 'none shall appear empty' — a BLOCK (NEW; the two amounts and the gift of the hand parameters); the appearing owed and the appearance gift by CALL (calendar, erection); at the counter's day, no marker
      judges_in_every_gate_commanded: [judges_and_officers_commanded, judgment_wresting_barred, person_respecting_barred, bribe_barred, justice_pursuit_commanded]   # Deut 16:18-20: the courts in every gate by the tribes — a STATUS (NEW; the three tiers a parameter), 'you shall not wrest judgment', 'you shall not respect persons' — BLOCKS (NEW), 'you shall not take a bribe' — bribe_barred REUSED, ITS FIRST ENTRY ANYWHERE (Exodus 23:8's block declared at the ordinances' cell, never written — DB7), 'justice, justice you shall pursue' — a STATUS (NEW; the acquittal final a parameter); at the counter's day, no marker
      asherah_and_pillar_barred: [asherah_beside_the_altar_barred, pillar_barred]   # Deut 16:21-22: no asherah beside the altar, no pillar — BLOCKS (NEW; the pillars' change of state read from the tape's own entries on Jacob's pillars); at the counter's day, no marker
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  festivals_judges:   # THE DEUTERONOMY WALK 14b' not in text:
    fb = '''  festivals_judges:   # THE DEUTERONOMY WALK 14b (2026-09-23; LEAN)
    the_passover_at_the_place: {status: WRAPPED, by: law_festivals_judges}
    the_weeks_from_the_sickle: {status: WRAPPED, by: law_festivals_judges}
    the_feast_of_booths: {status: WRAPPED, by: law_festivals_judges}
    the_three_pilgrimages: {status: WRAPPED, by: law_festivals_judges}
    the_judges_in_every_gate: {status: WRAPPED, by: law_festivals_judges}
    the_asherah_and_the_pillar: {status: WRAPPED, by: law_festivals_judges}
    the_readback: {status: WRAPPED, by: law_festivals_judges}
'''
    i = text.index('  release_firstborn:   # THE DEUTERONOMY WALK 13b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_festivals_judges' in dd['daemons'] and 'festivals_judges' in dd['functions'] and len(dd['functions']['festivals_judges']) == 7, (list(dd)[:5])
print('daemons: %d (law_festivals_judges %s); functions blocks: %d' % (len(dd['daemons']), 'law_festivals_judges' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + the CALL edges by the ink (fifteen REFERENCE; the token-demanded edges and any pointer after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  festivals_judges:' not in text.split('\nedges:')[0]:
    a = "  release_firstborn: [[Deut, 15, 1, 23]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  festivals_judges: [[Deut, 16, 1, 22]]   # THE DEUTERONOMY WALK 14b (2026-09-23; DEUTERONOMY_WALK.md \"Sitting 14b\" — LEAN): chapter 16 — THE PASSOVER AT THE PLACE, THE WEEKS FROM THE SICKLE, THE FEAST OF BOOTHS, THE THREE PILGRIMAGES, THE JUDGES IN EVERY GATE, THE ASHERAH AND THE PILLAR: the readback's rows one per verse graded against the kin's cells by CALL; FIVE OWN-DAY LINES at the counter's day, no marker; the exam the eight Mishnah rows the spine cites (no docket — the lean pass); fifteen CALL edges, all REFERENCE\n" + text[j + 1:]
    REF = [
     ('pesach', "16:1-2, 5-7's Passover is Exodus 12's by name — PS.paschal_procedure('for_its_sake', 'eating_time', 'preparation', 'leftover') CALLED (the name's requirement — 128:1; the eating night until midnight — 133:2's third phrase; roasted only against 16:7's 'cook' — 134:1 with 2 Chronicles 35:13; the remainder burned on the 16th — 16:4's flesh), PS.leaven_machine('window_bounds', 'purge_deadline') for 16:3-4's leaven (the window 14th evening to 21st evening; Mishnah Pesachim 3:7's road); the readback rows 16:1-8 the kin by CALL"),
     ('moadim', "16:8's seventh day, 16:9's count and 16:13's seven days are Leviticus 23's by name — MO.passover(), MO.omer(), MO.sukkot(), MO.work_class('passover_7') CALLED (the slaughter window after midday — 130:1's sixth hour; the morrow the festival and the count 49 — 136:8's reaping by night; the booths' seven and the dwelling; the seventh day's work class servile_only — 135:3's hand-off to the sages); counts_omer and dwells_in_booths the moadim engine's timers on its case world, NONE on the tape UNMOVED; the readback rows 16:8-9, 16:13-15 the kin by CALL"),
     ('musafim', "16:8's seventh and 16:13-16's feasts are Numbers 28-29's by name — MU.pesach_shavuot('the_dates', 'the_seventh', 'redress_days') and MU.sukkot('the_dates', 'the_eighth') CALLED (the seventh a convocation of the same class; Shavuot's seven days of redress by DEUT 16:16's OWN ANALOGY — the callee already names this chapter; the eighth its own festival); the readback rows 16:8, 16:13-16 the kin by CALL"),
     ('calendar', "16:16's 'three times in the year all your males shall appear' is Exodus 23:14-17's by name — CA.pilgrimage({'kind': 'able_male' / 'woman' / 'lame' / 'blind_one_eye'}) CALLED (the able male owes the three appearings — appearance_owed the calendar's heaven entry on its case world, NONE on the tape; the exempt arms Mishnah Chagigah 1:1's class), CA.matzah('as_commanded') for 16:3's seven days (Exodus 23:15's own pointer into pesach), CA.offering_windows('leaven_beside_offering', 'fat_overnight') for 16:4; the readback rows 16:3-4, 16:16 the kin by CALL"),
     ('erection', "16:16's 'none shall appear empty', 16:4's flesh till morning, 16:13's ingathering and 16:21's asherah are Exodus 34:18-26 and 34:13's by name — ER.repeats('empty_where_it_stands', 'empty_two_seats', 'chagigah_overnight', 'purge_before_slaughter', 'graze_ban_presence') and ER.covenant(the asherah's cells) CALLED (the standing liability like the appearance offering — Bekhorot 51b; the fourteenth's festival offering not overnight — Pesachim 70a; the cow grazes unharmed — 52:4's guard of the land; the asherah forbidden because a hand made it — Mishnah Avodah Zarah 3:5); appearance_gift_owed the erection's debit on its case world, NONE on the tape UNMOVED; the readback rows 16:4, 16:16-17, 16:21 the kin by CALL"),
     ('place_name', "16:2, 6, 7, 11, 15, 16's 'the place which the LORD will choose' is chapter 12's formula (the book's eleven seats — six here) and 16:11, 14's rejoicing chapter 12's law — PN.the_place_chosen('the_place_which_the_lord_will_choose', 'eat_there_and_rejoice', 'your_households', 'the_womans_rejoicing'), PN.the_profane_slaughter_the_blood_and_the_gates('you_may_not_eat_within_your_gates'), PN.the_header_and_the_demolition('the_three_asherim') CALLED (place_chosen_required ONE and rejoicing_before_the_lord_commanded TWO on israel_people UNMOVED — referenced, not reused: their count seats DD2, DF2, Q32, Q38 would move); the readback rows 16:2, 16:5-7, 16:11, 16:14-16, 16:21 the kin by CALL"),
     ('opening_speech', "16:18-19's judges and 'you shall not respect persons' are Deut 1:16-17's charge by name — OS.the_officers_and_the_judges('the_qualities', 'the_charge', 'no_faces', 'judge_righteously', 'the_court_of_three', 'the_perverting_judge') CALLED (judges_charged ONE on the_court the tape's reference at (1, 2, 16); the qualities, the faces disputed, the court of three by the answer sheet); the readback rows 16:18-20 the kin by CALL"),
     ('exodus_story', "16:18's courts in every gate are Exodus 18:21-25's founding by name — ES.jethro('judges', 'denominations', 'sanhedrin_sizes') CALLED (78,600 judges over the four denominations; Mishnah Sanhedrin 1:6's (71, 23) — the three tiers' sizes); courts_established ONE on israel_people (Exodus 18:25's line) the tape's reference, never a second write; the readback row 16:18 by CALL"),
     ('ordinances', "16:19's 'you shall not wrest judgment' and 'you shall not take a bribe' are Exodus 23:6-8's by name (the phrase's three seats; the bribe's twin) — OR.courts('poor_not_glorified', 'asymmetry', 'twenty_three', 'one_vs_two', 'dissenter', 'bribe', 'bribe_absolute') CALLED (23:3 against Leviticus 19:15 each verse its referent; acquit by one, convict by two; the small court twenty-three; Mishnah Sanhedrin 4:1's tilts — THE ACQUITTAL FINAL, 144:12; bribery absolute even to judge truly — the Mekhilta); bribe_barred THE ORDINANCES' BLOCK, declared at its cell and NEVER WRITTEN ON ANY ENTITY (DB7) — WRITTEN HERE FOR THE FIRST TIME at 16:19's line; the readback rows 16:19-20 the kin by CALL"),
     ('holiness', "16:19's two faces and the wresting are Leviticus 19:15's by name — HO.conduct('no_favor', who='poor'), HO.conduct('scale_of_merit', 'five_effects', 'judge_is_measurer', 'bribe', 'equal_treatment') CALLED (the poor's face and the great's; the judge's five effects — judgment_perverted the holiness engine's heaven entry, NONE on the tape UNMOVED; the bribed judge's eyes dim — Peah 8:9); the readback row 16:19 the kin by CALL"),
     ('second_tablets', "16:19's 'you shall not take a bribe' answers 10:17's 'who lifts no face and takes no bribe' — ST.the_god_of_gods_and_the_stranger('takes_no_bribe', 'the_permitted_fee', 'lifts_no_face', 'a_salary_voids') CALLED (DB7's declaration: Exodus 23:8's block never written on the tape, '16:19 the command's seat forward' the callee's own words; the permitted fee for evident loss — Ketubot 105a:17-19; a salary voids — Bekhorot 4:6); the readback row 16:19 the kin by CALL"),
     ('seven_nations', "16:21's asherah is 7:5's 'their asherim' by name — SN.the_seven_nations('the_asherah_shade', 'the_asherah_wood', 'the_four_objects') CALLED (the sitter in its shade barred — Mishnah Avodah Zarah 3:8; the wood-burner lashed — Makkot 22a; the four verbs where 34:13 had three); the readback row 16:21 the kin by CALL"),
     ('covenant_at_horeb', "16:12's 'and you shall remember that you were a slave in Egypt' is 5:15's clause by name (the book's five seats — 5:15, 15:15, 16:12, 24:18, 24:22) — CH.the_first_tablet('the_fourth_word', 'keep_and_remember', 'the_servants_rest') CALLED (the Sabbath word's memory clause and the servants' rest — 16:11's household the same list without the ox and the ass); the readback row 16:12 VERBATIM in kind by CALL"),
     ('journeys', "16:22's pillar is Leviticus 26:1's 'you shall not raise up a pillar' by name at Numbers 33:52's figured stones — JR.the_command('figured_stones', 'high_places', 'three_objects_own', 'private_altar_eras') CALLED (Leviticus 26:1's word at its ban's seat; the three objects the iconoclasm lists name — altars, pillars, asherim); the readback row 16:22 the kin by CALL"),
     ('pesach_sheni', "16:1's 'keep the Passover' in the month of Aviv is the Passover in its season (Numbers 9:2-3 — passover_in_its_time ONE on israel_people the tape's entry at Num 9:5) — PSH.second_passover('distance') CALLED (the distant way's measure — from Modi'im and beyond — the pilgrim's road to the place, 16:5-6's gates against the place); the readback row 16:1 by CALL"),
    ]
    edges = ''.join("  - {from: festivals_judges, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: %s}\n" % (to, q(W + why)) for to, why in REF)
    a = "  - {from: release_firstborn, to: metzora, disposition: CALL, link: transfer,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'festivals_judges'); n_tr = sum(1 for e in dep['edges'] if e['from'] == 'festivals_judges' and e.get('link') == 'transfer')
missing = [e['to'] for e in dep['edges'] if e['from'] == 'festivals_judges' and e['to'] not in dep['spans']]
assert 'festivals_judges' in dep['spans'] and n_ch == 15 and n_tr == 0 and not missing, (n_ch, n_tr, missing)
print('dependency: span + %d edges (festivals_judges %d CALL — all reference; the token-demanded edges and any pointer after the gate\'s print)' % (n_ch, n_ch))
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 75 and all(" in text:
    old = "len(real) == 75 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 13b (2026-09-23): 74 -> 75,"
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 76 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 14b (2026-09-23; LEAN): 75 -> 76, law_festivals_judges (given_at Deut 16:1 — the month of Aviv; installed_by boot); 13b: 74 -> 75,")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 76" in open(path, encoding='utf-8').read()
print('installation_probes I5: 76')
# ---- THE REGISTER FILE UNTOUCHED — no seat at Deut 16 (the reading's finder; the recon) ----
rg = yaml.safe_load(open(f"{ROOT}/World/step9/register_dispositions.yaml", encoding='utf-8'))
assert not [k for sec in rg.values() if isinstance(sec, dict) for k in sec if 'Deut 16' in str(k)], 'no seat at Deut 16'
cal = yaml.safe_load(open(f"{ROOT}/World/step9/calendar_parameters.yaml", encoding='utf-8'))['parameters']
assert 'festival_dates' in cal and 'omer_day' in cal and 'intercalated_month' in cal, 'the festivals and the intercalation on file — no row added'
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']; ev = yaml.safe_load(open(f"{ROOT}/World/step9/event_vocabulary.yaml", encoding='utf-8'))['events']
print('THE TYPES DONE: kinds %d, effects %d, daemons %d, functions blocks %d, edges from festivals_judges %d, I5 76, calendar parameters %d (none added)' % (len(ev), len(fx), len(dd['daemons']), len(dd['functions']), n_ch, len(cal)))
