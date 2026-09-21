import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 5 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch11_cases_gen.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_place_name as PN
p23 = open(f'{SP}/ch12_part2.py', encoding='utf-8').read() + open(f'{SP}/ch12_part3.py', encoding='utf-8').read()
CELLS = [('F1', 'the_header_and_the_demolition'), ('F2', 'the_place_chosen'), ('F3', 'the_burnt_offerings_only_there'), ('F4', 'the_profane_slaughter_the_blood_and_the_gates'), ('F5', 'the_border_enlarged_and_the_altar'), ('F6', 'the_nations_cut_off_and_the_abomination'), ('RB', 'the_readback')]
REF = {'the_headers_twin': 'Deut 12:1; Lev 26:46; Deut 11:32 (the tape — blessing_and_curse_set); TC, BC by CALL', 'the_four_nouns': 'Deut 12:1; the Sifrei 59:1-4', 'the_land_bound_rule': 'Deut 12:1; Mishnah Kiddushin 1:9; the Sifrei 59:5; BR by CALL', 'destroy_you_shall_destroy': 'Deut 12:2; Num 33:52 (the tape); Deut 4:26 by CALL; the Sifrei 60:1-4', 'the_five_verbs': 'Deut 12:3; Deut 7:5 (the tape); Exod 34:13 by CALL (ER demolition_grows); the Sifrei 61:1-4', 'the_renaming': 'Deut 12:3; the Sifrei 61:6-7', 'the_mountains_not_their_gods': 'Deut 12:2; Mishnah Avodah Zarah 3:5; Avodah Zarah 45a-b; the Sifrei 60:4', 'the_three_asherim': 'Deut 12:3; Mishnah Avodah Zarah 3:7-8; the Sifrei 61:5-6; SN by CALL', 'you_shall_not_do_so': 'Deut 12:4 (THE WRITE name_erasure_barred); the Sifrei 61:8; Sanhedrin 90a:3; Shabbat 120b:10', 'the_erasures_lashes': 'Deut 12:4; Makkot 22a:9; Pesachim 48a:7',
       'the_place_which_the_lord_will_choose': 'Deut 12:5 (THE LINE place_chosen_declared; THE WRITE place_chosen_required); Exod 40:17 (the tape — erected); SD by CALL', 'the_name_pronounced_only_there': 'Deut 12:5; Mishnah Sotah 7:6; Sotah 38a:10-11; OR by CALL', 'in_one_of_your_tribes': 'Deut 12:14 [1]; the Sifrei 62:2-3, 70:4; Zevachim 118b:6-12', 'the_seven_offerings': 'Deut 12:6, 12:11, 12:17; Num 18:8 (the tape — gifts_granted); KR, OR by CALL; the Sifrei 63:9, 68:6', 'eat_there_and_rejoice': 'Deut 12:7 (THE WRITE rejoicing_before_the_lord_commanded); the Sifrei 64:1-4; Mishnah Yoma 1:1', 'your_households': 'Deut 12:12, 12:18; Num 18:20 (the tape — portion_declared); Deut 5:14 by CALL (CH); the Sifrei 69:3-4, 74:4-5', 'not_as_we_do_here_today': 'Deut 12:8; Zevachim 117b:3, 114a:13; SA by CALL; Judges 17:6, 21:25', 'the_rest_and_the_inheritance': 'Deut 12:9 (THE STATE ROW), 12:10; Zevachim 119a:9-13, 119b:1-5; BH, TC by CALL', 'the_stations_six_rows': 'Deut 12:9-11; Mishnah Zevachim 14:4-8; Zevachim 112b:9-12, 118b:13-119a:2; SD, SA, JO by CALL', 'the_three_commandments_of_the_entry': 'Deut 12:10-11; Sanhedrin 20b:8-14; the Sifrei 67:1-3', 'the_second_answer_sheet': 'Deut 12:9; Mishnah Megillah 1:10-11; Megillah 10a:2-9', 'the_womans_rejoicing': 'Deut 12:7, 12:12, 12:18; Rosh Hashanah 6b:15-16, 6b:3-13',
       'take_heed_lest_you_offer_in_every_place': 'Deut 12:13 (THE REUSE high_places_banned); Lev 17:8-9 by CALL (SA outside); the Sifrei 70:1-2', 'in_the_place_which_the_lord_will_choose': 'Deut 12:14; SA platform, SD eras by CALL; the Sifrei 70:3-4', 'the_prophets_exception': 'Deut 12:13; the Sifrei 70:3; 1 Kings 18', 'the_karet_matrix': 'Deut 12:13-14; Zevachim 112b:13-113a:2, 119b:10-20; SD, SA by CALL',
       'with_all_the_desire_of_your_soul': 'Deut 12:15 (THE LINE profane_slaughter_permitted; THE WRITE profane_slaughter_permitted); Lev 17:3-5 by CALL (SA outside); Chullin 16b-17a; the Sifrei 71:1-2, 75:3-4', 'the_unclean_and_the_clean': 'Deut 12:15, 12:22; Bekhorot 33a:1-5; the Sifrei 71:3-6', 'the_blemished_consecrated': 'Deut 12:15; Mishnah Bekhorot 2:2-3; Bekhorot 15a:5-16a', 'the_eaters': 'Deut 12:15; Bekhorot 33a:4-11', 'the_blood_like_water': 'Deut 12:16, 12:24; Lev 17:10-14 by CALL (SA blood, covering); Chullin 84a; Pesachim 22a:8; Mishnah Makhshirin 6:4; the Sifrei 71:13-14', 'you_may_not_eat_within_your_gates': 'Deut 12:17 (THE WRITE holy_things_in_the_gates_barred); Num 18:31 by CALL (KR every_place); the Sifrei 72:1-8; Mishnah Makkot 3:3', 'the_ladder_of_a_fortiori': 'Deut 12:17; Makkot 17a:12-18a:2; the Sifrei 72:9-11, 73:1, 74:1', 'the_list_read_backward': 'Deut 12:17; Makkot 17b:9-10', 'the_lashes_outside_the_wall': 'Deut 12:17; Mishnah Makkot 3:3; Makkot 13a-b, 19b:15', 'the_impure_tithes_warning': 'Deut 12:15-17; Makkot 19a:3-10, 19b:3-13', 'the_two_tithes': 'Deut 12:17; Num 18:31 (the tape — tithe_of_the_tithe_commanded); KR by CALL; the Sifrei 77:7-8', 'before_the_lord_you_shall_eat_it': 'Deut 12:18; Deut 5:14 by CALL (CH); the Sifrei 74:2-4; Makkot 19b:15', 'lest_you_forsake_the_levite': 'Deut 12:19 (THE WRITE levite_forsaking_barred); the Sifrei 74:6-7; Pesachim 8b', 'the_levites_scope': 'Deut 12:19; the Sifrei 74:8-9',
       'when_the_lord_enlarges_your_border': 'Deut 12:20 (THE POINTER); Exod 34:24 by CALL (ER repeats); the Sifrei 75:1-2', 'the_wilderness_flesh': 'Deut 12:20-21; Chullin 16b:14-17a:10; the Sifrei 75:3-4 (the parameter the_wilderness_flesh)', 'too_far': 'Deut 12:21; Makkot 19b:9-13; Chullin 16b:17', 'as_i_have_commanded_you': 'Deut 12:21 (THE RECEIPT WITHOUT THE NAME); Exod 23:15 by CALL (CA matzah); Chullin 28a:5; the Sifrei 75:15', 'the_rite_of_slaughter': 'Deut 12:21; Mishnah Chullin 2:1; Chullin 28a:4-13 (the parameter the_rite_of_slaughter)', 'the_civility': 'Deut 12:21; Chullin 84a:18-84b:4; the Sifrei 75:5', 'as_the_gazelle_and_the_hart': 'Deut 12:22; Lev 17:13 by CALL (SA covering); Chullin 28a:4, 17a:10; the Sifrei 75:11-15', 'the_blood_is_the_life': 'Deut 12:23; Gen 9:4 (the tape — limb_barred); Lev 17:11; PS, SA by CALL; the Sifrei 76:1-5; Pesachim 16b:3', 'the_limb_from_the_living': 'Deut 12:23; Chullin 102b-103a; Sanhedrin 74b:9', 'the_bloods_classes': 'Deut 12:16, 12:23; Mishnah Keritot 5:1; Keritot 20b-22a', 'flesh_in_milk': 'Deut 12:25; Chullin 113a-116a; CA kid_in_milk by CALL', 'your_holy_things': 'Deut 12:26; Num 18:8 (the tape — gifts_granted); Temurah 17b:15-17; Mishnah Temurah 3:5; the Sifrei 77:1-8', 'the_sin_offerings_verb': 'Deut 12:27; Lev 4 by CALL (PS shed_homograph); Exod 20:24 by CALL (OR altar); Zevachim 36b-37a, 104a:4, 86a:1-4', 'the_good_and_the_right': 'Deut 12:25, 12:28; Deut 6:18 by CALL (HI); the Sifrei 79:1-5; Mishnah Makkot 3:15; Makkot 23b',
       'when_the_lord_cuts_off_the_nations': 'Deut 12:29; Deut 7:1 (the tape — nations_devoted); Num 33:53 by CALL (JO); the Sifrei 80:1-5', 'lest_you_be_ensnared': 'Deut 12:30; Deut 7:25 by CALL (SN); Exod 23:33 by CALL (OR); the Sifrei 81:1', 'lest_you_inquire_after_their_gods': 'Deut 12:30 (THE LINE nations_cut_off_warned; THE WRITE foreign_rite_inquiry_barred); the Sifrei 81:2-4; Sanhedrin 74a-b', 'you_shall_not_do_so_singular': 'Deut 12:31; Deut 7:25 (the tape — abomination_barred); the Sifrei 81:5', 'their_sons_and_their_daughters': 'Deut 12:31; the Sifrei 81:6; Sanhedrin 74b:1-9', 'no_molech_named': 'Deut 12:31; Lev 18:21, 20:2-5 by CALL (SA molech)',
       'the_table': 'Deut 12:1-31 (the readback table)', 'the_state_row': 'Deut 12:9 (the state row)', 'the_pointer_row': 'Deut 12:20 (the pointer row)', 'the_supplied_law_rows': 'Deut 12:4, 12:7, 12:17, 12:19, 12:30 (the supplied law rows)', 'no_retrograde_row': 'Deut 12:2-31 (no retrograde row)'}
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch12_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p23.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(PN, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, PN.DATA)
        assert v != 'no verdict in span', (name, a)
        assert a in REF, ('an ask without a label', name, a)
        lines.append('    (%r, lambda: %s({\'ask\': %r}, DATA), %r),' % ('%s — %s' % (REF[a], a), name, a, v))
        count += 1
    per_cell[code] = len(asks)
lines.append(']')
MAIN = r'''


if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0, 'HYP': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'HYP' if 'HYP' in kinds else ('INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE INK: the number verse %s (ordinals none); the one mark %s; the register singular-only %s, plural-only %s, both %s, neither %s; the negations %s; the Name %d bare tokens; Moses unnamed (the book\'s seats by chapter %s); the tokens %d, the letters %d' % (PARSED, MARKS(12, 17), [v for v, (p, s) in NUM.items() if s and not p], [v for v, (p, s) in NUM.items() if p and not s], [v for v, (p, s) in NUM.items() if p and s], [v for v, (p, s) in NUM.items() if not p and not s], {v: [x for x in W12(v) if x in NEG] for v in range(1, 32) if any(x in NEG for x in W12(v))}, sum(1 for v in range(1, 32) for x in W12(v) if x == 'יהוה'), DATA['moses_unnamed']['value'], TOKN, LETN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s (the state row %s, the writes %s); the pointer rows %s; no row open %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [r['verses'] for r in READBACK if r['state']], [r['write'] for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], not any(r['open'] for r in READBACK), [o['name'] for o in OPEN_ROWS], len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the_rite_of_slaughter %s; the_wilderness_flesh %s' % (CLOCK, {k: v[:40] for k, v in RITE.items()}, {k: v[:40] for k, v in WILDERNESS_FLESH.items()}))
    print('THE SCANS on the one database: the seven on Israel %s; high_places_banned\'s entities %s' % (PLACE_SCAN, HPB_SCAN))
    print('THE CALLEES: SA ban %s, which %s, hunted %s, eras %s; SD table %s, differences %s, ink %s; ER grows %s, as_commanded %s; OR every_place %s; PS shed %s; CA matzah %s; KR every_place %s; TC covenant %s; CH fourth %s; HI right %s; BR bound %s; BH ark %s' % (SA_BAN['v'], SA_WHICH['v'], SA_HUNTED['v'], [p for _, p in SA_ERAS['v']], SD_TABLE['v'], SD_DIFF['v'], SD_INK['v'], ER_GROWS['v'], ER_ASC['v'], OR_EVERY['v'], PS_SHED['v'], CA_ASC[0][:40], KR_EVERY[0][:40], TC_COV['v'], CH_FOURTH[0][:40], HI_RIGHT[0][:40], BR_BOUND[0][:40], BH_ARK[0]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s (two — the erasure, the tithe outside the wall); the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5]))
    print('THE NARRATIVE: %s (the seven on Israel %s; the reuse on the-land %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger], [e['effect'] for e in _WN.entity('the-land').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_eras_table_unmoved', 'the_two_tithes', 'the_five_verbs', 'the_readback')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 12: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch12_part5.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s; DATA rows %d' % (count, per_cell, PN.SCENE, PN.NARRATIVE, len(PN.DATA)))
