import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b — THE COMPILE OF CHAPTER 34, THE DEATH OF MOSES, LEAN (2026-09-30): THE TYPES BY SCRIPT, part B — daemon_dispositions (law_moses_death — given_at
# Deut 34:1, installed_by boot; the watches the six lines IN TWO FORMS with their writes NEW and the three REUSES; the functions block SEVEN WRAPPED: the six cells and the_readback);
# dependency_dispositions (the span's ONE RANGE [[Deut, 34, 1, 12]], TWENTY CALL edges by the ink, all REFERENCE — the census decides the rest; NO owed pointer in the file);
# installation_probes I5 83 -> 84; THE CALENDAR UNTOUCHED (no new clock key — the death date 19b's; the thirty days a duration); THE REGISTER FILE UNTOUCHED HERE — the receipt
# 'Deut 34:9' (class NONE) RE-DECLARED by patch_register_ch34.py AFTER the register gate's own print (the class the gate computes). add_types_ch33_b.py's form; the names READ from the
# spec module beside this file. RUN FROM THE REPO ROOT.
import yaml, subprocess, re, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch34b_spec as S
CHECK = '--check' in sys.argv
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
W = "THE DEUTERONOMY WALK 22b (2026-09-30) | "
R, DM = S.RUNNER, S.DAEMON
CELLS = [S.CELLS['F%d' % i] for i in range(1, 7)] + ['the_readback']
assert len(CELLS) == 7
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
D1 = "at Moses' last day (40, 12, 7) — 19b's marker, no marker here; the thirty days a duration"
NOTE = {'moses_went_up_to_nebo_and_saw_the_land': "Deut 34:1-3 (an ACT — the ascent): Moses went up to Nebo as commanded, the whole land shown Gilead to Zoar — STATUSES (NEW) on moses; 32:49's command a RUN CITATION; the land shown as the future (Sanhedrin 10:1 the case); " + D1,
        'oath_land_shown_not_crossed_declared': "Deut 34:4 (a SPEECH of the LORD — the subject god): the land sworn to the fathers shown at the end — a STATUS (NEW) on moses; see_the_land_from_afar_not_go_there REUSED (a heaven entry — the song's owed pointer PAID, the readback's POINTER ROW 34:4); Exodus 33:1's line taken whole; " + D1,
        'moses_died_and_was_buried': "Deut 34:5-6 (an ACT — the death and the burial): died by the mouth of the LORD, buried by the LORD the grave unknown — STATUSES (NEW) on moses; the three gifts' merits withdrawn at the third death — a STATUS (NEW) on israel_people; gathered_to_his_people REUSED (Aaron's word — the song's owed pointer PAID, the POINTER ROW 34:5); the grave in Gad's portion the blessing's owed pointer PAID (the POINTER ROW 34:6; Sotah 1:7, 1:9 and Tosefta Sotah 4:4 the cases); " + D1,
        'moses_hundred_and_twenty_israel_wept_thirty_days': "Deut 34:7-8 (an ACT — the years and the weeping): died at a hundred and twenty the eye undimmed — a STATUS (NEW) on moses; the days of weeping ended — a STATUS (NEW) on israel_people; mourned_thirty_days REUSED WITHOUT A DUE (the registry's timer op; the design's duration — no timer, the counter unmoved); the parser's 120 and 30 DATA rows, no count; the nazirite's term (Nazir 1:3 the case); " + D1,
        'joshua_full_of_the_spirit_israel_hearkened': "Deut 34:9 (an ACT — the receipt): the spirit of wisdom by the hands laid — a STATUS (NEW) on yehoshua; Israel hearkened to Joshua as the LORD commanded Moses — a STATUS (NEW) on israel_people; the commission Numbers 27:18-23 a RUN CITATION; the register's receipt seat re-declared; Avot 1:1's chain the case; " + D1,
        'no_prophet_like_moses_declared': "Deut 34:10-12 (an ACT — the epilogue, 'there arose not' the narrative past): no prophet like Moses face to face, the signs, the mighty hand and the great terror in the sight of all Israel — STATUSES (NEW) on israel_people; the tablets broken the Sifrei's last row; THE BOOK'S EDGE; " + D1}
assert set(NOTE) == set(S.KINDS)
if f'  {DM}:' not in text:
    lines = []
    for kind, first, rng, claim, cell, form, fields, effs, reuses in S.LINES:
        ws = [e for e, _, _ in effs] + [e for e, _, _ in reuses]
        lines.append('      %s: [%s]   # %s\n' % (kind, ', '.join(ws), NOTE[kind]))
    block = (f'  {DM}:\n    file: cold_run_{R}.py\n    wraps: {R}\n    given_at: Deut 34:1\n'
             '    installed_by: boot   # THE DEUTERONOMY WALK 22b (2026-09-30; THE LEAN PASS): "AND MOSES WENT UP FROM THE PLAINS OF MOAB TO MOUNT NEBO" — the death\'s first verse at Moses\' last day (40, 12, 7), 19b\'s marker at 31:1 (NO MARKER in this chapter — the thirty days of weeping a DURATION by the design\'s ruling, the counter unmoved); installed by boot like law_opening_speech through law_blessing_of_moses (the Deuteronomy daemons\' form; THE INSTALL HYPOTHESIS on the table unchanged); ONE daemon over ONE chapter and one unit — the death of Moses (34:1-12), THE BOOK\'S LAST: the chapter\'s own acts and the LORD\'s oath its NEW family, its writes on moses, israel_people and yehoshua; SIX lines in TWO FORMS (5 act — the ascent, the death and the burial, the years and the weeping, Joshua and the receipt, the epilogue; 1 speech — the oath and the denial); THREE REUSES at their own forward seats (the denial 32:52 -> 34:4, the gathering 32:50 -> 34:5, Aaron\'s thirty days Numbers 20:29 -> 34:8 — the last written without a due); the parser\'s 120 and 30 DATA rows, no count\n'
             '    watches:\n' + ''.join(lines))
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if f'\n  {R}:   # THE DEUTERONOMY WALK 22b' not in text:
    fb = f'  {R}:   # THE DEUTERONOMY WALK 22b (2026-09-30; LEAN — one chapter, one unit, one daemon, no marker, three reuses; THE BOOK\'S LAST)\n' + ''.join('    %s: {status: WRAPPED, by: %s}\n' % (c, DM) for c in CELLS)
    i = text.index('  blessing_of_moses:   # THE DEUTERONOMY WALK 21b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(text)
NW = sum(len(l[7]) + len(l[8]) for l in S.LINES)
assert DM in dd['daemons'] and R in dd['functions'] and len(dd['functions'][R]) == 7 and len(dd['daemons'][DM]['watches']) == 6 and sum(len(v) for v in dd['daemons'][DM]['watches'].values()) == NW == 15, (len(dd['functions'].get(R, [])), len(dd['daemons'].get(DM, {}).get('watches', {})), NW)
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']; ev = yaml.safe_load(open(f"{ROOT}/World/step9/event_vocabulary.yaml", encoding='utf-8'))['events']
for k, v in dd['daemons'][DM]['watches'].items():
    assert k in ev, k
    for e in v: assert e in fx, e
assert {ev[k]['form'] for k in dd['daemons'][DM]['watches']} == {'act', 'speech'}
print('daemons: %d (%s %s); functions blocks: %d; the watches %d writes over 6 lines in two forms' % (len(dd['daemons']), DM, DM in dd['daemons'], len(dd['functions']), NW))
# ---- the dependency span (one range) + the CALL edges by the ink (twenty REFERENCE; the token-demanded edges and the pointers after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
REF = [
 ('song_charge_nebo', "34:1's 'and Moses went up … to Mount Nebo … over against Jericho' is 32:49's command OBEYED word for word (SC.the_summons_to_nebo — go_up_to_nebo_see_the_land_commanded on moses the tape's own line, a RUN CITATION — CALLED); 34:4's 'you shall not cross over there' 32:52's 'there you shall not go' (SC.meribah_and_the_seeing — see_the_land_from_afar_not_go_there REUSED at its own forward seat: THE SONG'S OWED POINTER PAID, the readback's POINTER ROW 34:4); 34:5's death 32:50's sentence executed (SC.DATA moses_death_ahead — THE SONG'S SECOND OWED POINTER PAID, the POINTER ROW 34:5); SC.the_readback's form; the readback rows 34:1, 34:4, 34:5 the kin by CALL"),
 ('covenant_return_charge', "34:7's 'a hundred and twenty years old when he died' is 31:2's number on the marker's day (CR.the_charge_and_the_crossing a_hundred_and_twenty_years_old_this_day — 19b's ONE MARKER; CR.DATA the_death_date_of_moses the seventh of Adar — CALLED, no second marker); 34:9's Joshua 31:7's and 31:23's charge and commission (CR.the_tent_and_the_commission — joshua_charged_to_bring_israel_in, joshua_commissioned_to_bring_israel_in on yehoshua); 34:5's third death CR.DATA the_three_gifts_and_their_merits (the daemon owed there); 31:16's 'you shall sleep with your fathers' (CR.the_apostasy_foretold); the readback rows 34:5, 34:7, 34:9 the kin by CALL"),
 ('blessing_of_moses', "34:6's 'He buried him in the valley … over against Beth-peor' is MOSES' GRAVE IN GAD'S PORTION — Onkelos 33:21 and the Sifrei 355:6 (BL.DATA moses_grave_ahead — THE BLESSING'S OWED POINTER 33:21 -> 34:6 PAID, the readback's POINTER ROW 34:6 — CALLED); 34:9's 'the children of Israel RECEIVED from him' (Onkelos) Avot 1:1's chain (BL.DATA the_chain_of_transmission — the parameter read again); 33:1's 'before his death' THIS day (blessing_given_before_moses_death 1 on israel_people); the readback rows 34:6, 34:9 the kin by CALL"),
 ('gad_reuben', "34:6's grave is Reuben's Nebo and Gad's field (GR.DATA moses_grave — 'reubens_nebo_gads_field', Sotah 13b; GR.the_cities moses_grave — CALLED); 34:1's Nebo Numbers 32:38's (the land east the tape's); the readback rows 34:1, 34:6 the kin by CALL"),
 ('chukat', "34:5's 'by the mouth of the LORD' and 34:8's 'thirty days' are AARON'S DEATH'S WORDS — Numbers 20:24-29 on the tape (CK.edom_and_hor death_dates, succession, thirty_days — gathered_to_his_people REUSED on moses, mourned_thirty_days REUSED on israel_people WITHOUT A DUE; CK.meribah death_by_the_kiss, well_by_merit — the three gifts' first event, Miriam's well — CALLED); barred_from_the_land 2 on Moses and Aaron UNMOVED (the sentence read, not rewritten); the readback rows 34:5, 34:8 the kin by CALL"),
 ('journeys', "34:5's 'by the mouth of the LORD' is Numbers 33:38's (JR.aarons_death_retold by_the_mouth_kiss, the_date, no_write — the retelling that never writes; 34:7's 'when he died' 33:39's one other seat — CALLED); the readback rows 34:5, 34:7 the kin by CALL"),
 ('second_tablets', "34:6's 'and He buried him' is the burial by the LORD Himself — walk after His attributes (ST.the_stations_and_the_death walk_after_his_attributes — Sotah 14a's burying the dead the callee's own row; 10:6 Aaron's 'and he was buried there' — CALLED); 34:12's 'the great terror' is THE TABLETS BROKEN before your eyes (9:17 — the Sifrei 357:44, the export's last row; ST.the_tablets_and_the_ark the_fragments_in_the_ark); the readback rows 34:6, 34:12 the kin by CALL"),
 ('zelophehad', "34:9's 'Moses had laid his hands upon him' is Numbers 27:18-23 on the tape — THE COMMISSION'S RECEIPT (invested_office on yehoshua; ZE.the_daughters the_run, execution — the chapter's runner — CALLED, a RUN CITATION); the readback row 34:9 the kin by CALL"),
 ('opening_speech', "34:1's Pisgah is 3:27's refused then granted (OS.the_plea pisgah, beth_peor — 34:6's Beth-peor 3:29's — CALLED); 34:4's seeing and denial Numbers 27:12-13's debit PAID (OS.the_commission the_debit, the_hand_laid — one hand commanded, two laid: 34:9's receipt); the readback rows 34:1, 34:4, 34:6, 34:9 the kin by CALL"),
 ('beha', "34:5's third death withdraws the three gifts' last merit — the well by Miriam's, the cloud by Aaron's, the manna by Moses' (Taanit 9a — BH.taberah_and_quail three_gifts — CALLED; BH.DATA seven_clouds); 34:10's 'face to face' Numbers 12:8's 'mouth to mouth' the twin by sense (BH.miriam dibbur); the readback rows 34:5, 34:10 the kin by CALL"),
 ('naso', "34:8's 'the days of weeping' TEACHES THE NAZIRITE'S TERM — Numbers 6:4's 'the days' by the verbal analogy (I2; the Sifrei 357:37; Nazir 1:3 the case): NS.DATA nazir_default_days (30) the callee's own row — CALLED, the parameter the_nazirites_term; the readback row 34:8 the kin by CALL"),
 ('courts_prophet', "34:10's 'there arose not a prophet since in Israel like Moses' is 18:15's and 18:18's prophet LIKE Moses promised (CP.the_prophet my_words_in_his_mouth, from_your_midst_of_your_brothers — prophet_like_moses_promised 1 on israel_people — CALLED; the parameter the_prophets_bound); the readback row 34:10 the kin by CALL"),
 ('erection', "34:4's oath is EXODUS 33:1's LINE TAKEN WHOLE (nine tokens in order — the LORD's words after the calf; ER.tablets — CALLED, a RUN CITATION); 34:10's 'face to face' Exodus 33:11's (ER.presence pillar_face); 34:7's undimmed eye Exodus 34:29's shining face (ER.tablets radiance — face_radiant 1 on moses); 34:12's tablets broken (ER.tablets breaking_ratified — 9:17's Sifrei join); the readback rows 34:4, 34:7, 34:10, 34:12 the kin by CALL"),
 ('exodus_story', "34:11-12's signs, wonders, the mighty hand and the great terror are the tape's own Egypt lines (ES.signs count, believed_seats; ES.plagues ten; ES.sea ten_at_sea — the firstborn's plague and the sea, the Sifrei 357:42-43 — CALLED, RUN CITATIONS; signs_in_hand 1 on moses); 34:7's birthday the seventh of Adar (ES.birth birthday — Moses' birthday and death day); the readback rows 34:7, 34:11, 34:12 the kin by CALL"),
 ('joseph', "34:6's burial by the Place is JOSEPH'S BONES MERITED (Sotah 1:9 the case — Joseph buried his father, Moses attended Joseph's bones, the Place attended Moses': JO.the_oath oath_sworn, JO.coffin bones_closed_on_tape — CALLED; bones_oath 1); the three deaths' burials (JO.three_deaths buried_by_both, gathered_seat — gathered_to_his_people's Genesis seats); the readback rows 34:5, 34:6 the kin by CALL"),
 ('family', "34:5's 'gathered to his people' (Aaron's word, REUSED) is the testament's formula (FA.testament gathered, buried_named, burial_command — Jacob's — CALLED); 34:6's grave the purchase's holding (FA.purchase possession_by_burial); the readback rows 34:5, 34:6 the kin by CALL"),
 ('mamre', "34:4's 'which I swore to Abraham' is the promise's roots (MA.abraham_end seed_multiplied_closed, promise_closed_here — Genesis 12:7, 15:18 — CALLED; MA.mamre three_men); 34:1's 'as far as Dan' Genesis 14:14's phrase; the readback rows 34:1, 34:4 the kin by CALL"),
 ('hear_o_israel', "34:4's 'to Abraham, to Isaac and to Jacob' is 6:10's three fathers (HI.the_sons_question the_receipt — the receipt's form; HI.DATA the_oath_by_the_name — CALLED); the readback row 34:4 the kin by CALL"),
 ('obey_horeb', "34:6's 'over against Beth-peor' is 3:29's and 4:46's word — the three seats (OH.the_exhortation baal_peor_seen — CALLED; OH.DATA the_witnesses_chain, the_second_frame); the readback row 34:6 the kin by CALL"),
 ('shelach', "34:9's Joshua is Hoshea renamed (SH.spies joshua_name — Numbers 13:16's new name — CALLED; joshua_caleb_equal; SH.DATA deaths_ceased); the readback row 34:9 the kin by CALL"),
]
assert len(REF) == 20 and len({t for t, _ in REF}) == 20 and [t for t, _ in REF] == S.EDGES, ([t for t, _ in REF][:5], S.EDGES[:5])
if f'\n  {R}:' not in text.split('\nedges:')[0]:
    a = "  blessing_of_moses: [[Deut, 33, 1, 29]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + f"  {R}: [[Deut, 34, 1, 12]]   # THE DEUTERONOMY WALK 22b (2026-09-30; DEUTERONOMY_WALK.md \"Sitting 22b\" — LEAN): chapter 34 in ONE runner over one frozen unit (deu_34_moses_death — the death of Moses 34:1-12, THE BOOK'S LAST): the ascent and the land shown, the oath and the denial, the death and the burial, the years and the thirty days, Joshua and the receipt, the prophet, the signs and the terror; SIX own-day lines in TWO FORMS (5 act, 1 speech) at Moses' last day (40, 12, 7) — NO MARKER (19b's at 31:1; the thirty days a duration); the daemon law_moses_death given_at Deut 34:1, installed_by boot\n" + text[j + 1:]
    edges = ''.join("  - {from: %s, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: %s}\n" % (R, to, q(W + why)) for to, why in REF)
    k = text.rfind('  - {from: blessing_of_moses, to: '); e = text.index('\n', text.index('why:', k)) + 1
    text = text[:e] + edges + text[e:]
if not CHECK: open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(text)
n_ch = sum(1 for e in dep['edges'] if e['from'] == R); n_tr = sum(1 for e in dep['edges'] if e['from'] == R and e.get('link') == 'transfer')
missing = [e['to'] for e in dep['edges'] if e['from'] == R and e['to'] not in dep['spans']]
owed = [p for p in dep['pointers'] if p.get('disposition') == 'OWED']
assert R in dep['spans'] and dep['spans'][R] == [['Deut', 34, 1, 12]] and n_ch == 20 and n_tr == 0 and not missing, (dep['spans'].get(R), n_ch, n_tr, missing)
assert not owed, len(owed)
print('dependency: the span (one range) + %d edges (%s %d CALL — all reference; the token-demanded edges and the pointers after the gate\'s print); OWED pointers in the file: %d; edges %d, pointers %d' % (n_ch, R, n_ch, len(owed), len(dep['edges']), len(dep['pointers'])))
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
old = "len(real) == 83 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): 82 -> 83,"
if old in text:
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 84 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 22b (2026-09-30; LEAN): 83 -> 84, law_moses_death (given_at Deut 34:1 — and Moses went up to Nebo; installed_by boot; one daemon over one chapter and one unit, six lines in two forms, no marker, three reuses — THE BOOK'S LAST); 21b: 82 -> 83,")
    if not CHECK: open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 84" in text
print('installation_probes I5: 84')
# ---- THE CALENDAR UNTOUCHED (no new clock key — the death date 19b's; the thirty days a duration, no timer) ----
cal = yaml.safe_load(open(f"{ROOT}/World/step9/calendar_parameters.yaml", encoding='utf-8'))['parameters']
assert len(cal) == 75 and 'the_death_date_of_moses' in cal and not any('Deut 34:' in str(v.get('source', '')) for k, v in cal.items()), len(cal)
print('calendar: %d parameters, untouched (the_death_date_of_moses 19b\'s — the marker\'s day the runner reads; no Deut 34 source)' % len(cal))
# ---- THE REGISTER FILE — the one seat at Deut 34:9 stands class NONE here; RE-DECLARED after the gate's print (patch_register_ch34.py) ----
rg = yaml.safe_load(open(f"{ROOT}/World/step9/register_dispositions.yaml", encoding='utf-8'))
seats = [(sec, k, v.get('class')) for sec, d in rg.items() if isinstance(d, dict) for k, v in d.items() if isinstance(v, dict) and re.search(r'Deut 34:', str(k))]
assert seats == [('receipts', 'Deut 34:9', 'NONE')], seats
print('register: the one seat %s — to be RE-DECLARED from the gate\'s print (receipts %d, footers %d)' % (seats, len(rg.get('receipts', {})), len(rg.get('footers', {}))))
print('TYPES B OK' + (' (check)' if CHECK else ''))
