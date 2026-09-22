import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 5 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch12_cases_gen.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_seducers as SE
p23 = open(f'{SP}/ch13_part2.py', encoding='utf-8').read() + open(f'{SP}/ch13_part3.py', encoding='utf-8').read()
CELLS = [('F1', 'the_header'), ('F2', 'the_prophet_and_the_test'), ('F3', 'the_inciter'), ('F4', 'the_city_heard_of_the_inquiry_and_the_sword'), ('F5', 'the_whole_offering_the_heap_and_the_mercy'), ('F6', 'the_footer'), ('RB', 'the_readback')]
REF = {'the_headers_seal': "Deut 13:1 (THE LINE word_sealed; THE REUSE adding_barred); Deut 4:2 by CALL (OH); add_nothing_commanded 4:1 on the tape", 'the_three_grains': 'Deut 13:1; the Sifrei 82:3-5; Sukkah 34b:3-4; Menachot 41b:12-42a:2; Mishnah Zevachim 8:10 with Zevachim 80a-81a; Rosh Hashanah 28b (carried)', 'keep_and_do': 'Deut 13:1; the Sifrei 82:2, 85:3', 'the_elders_not_adding': 'Deut 13:1; Sanhedrin 88b:14-89a:2 (carried); Mishnah Sanhedrin 11:3; OH by CALL', 'the_festivals_days': 'Deut 13:1; Chagigah 8b:11; OH by CALL',
       'the_prophet_and_the_dreamer': 'Deut 13:2 (THE LINE prophet_test_declared); Numbers 12:6-8 by CALL (BH); Sanhedrin 89b:6-7; Horayot 13a:12; the Sifrei 83:1-2', 'the_sign_and_the_wonder': 'Deut 13:2-3; the Sifrei 83:4-5; 1 Kings 13:3', 'the_signs_status': 'Deut 13:3-4 (THE WRITE false_prophet_hearing_barred; the parameter the_signs_status); the Sifrei 84:1-4; Sanhedrin 90a:10-11; the Rambam 5:3; CH by CALL', 'the_lord_is_testing_you': 'Deut 13:4 (THE WRITE tested_by_the_lord); Gen 22:1 (the tape — tested); MM, GL, HI by CALL; the Sifrei 84:5', 'the_six_verbs': 'Deut 13:5 (THE REUSE cleaving_commanded); Deut 10:20 (the tape); Num 10:11 (the tape — cloud_lifted); ST, HI, ER by CALL; the Sifrei 85:1-6', 'the_false_prophets_table': 'Deut 13:3, 13:6; Sanhedrin 90a:2-6; Mishnah Sanhedrin 11:5-6; SA by CALL', 'the_prophets_death': 'Deut 13:6, 13:11 (THE CASE — put_to_death, evil_purged_from_the_midst; the parameter the_prophets_death); the Sifrei 86:6, 90:2; Sanhedrin 89b:15-21; Mishnah Sanhedrin 11:1; the Rambam 5:2', 'the_exodus_formula_with_redeeming': 'Deut 13:6, 13:11; Deut 5:6, 9:26, 7:8 by CALL (CH, NR, SN); the Sifrei 86:4-5, 90:3', 'the_evil_purged': "Deut 13:6 (THE CASE'S WRITE evil_purged_from_the_midst — the formula's first seat of nine); the Sifrei 86:10", 'the_exemptions': 'Deut 13:6; the Sifrei 86:1-2; Sanhedrin 90a:5', 'elijah_at_carmel': 'Deut 13:5; Yevamot 90b:5-6, 10-11; Sanhedrin 89b:7, 90a:2; the Sifrei 85:4', 'the_oven_of_akhnai': 'Deut 13:2-3; Bava Metzia 59b', 'the_established_prophet': 'Deut 13:2; Sanhedrin 89b:6-7; Horayot 13a:12',
       'the_inciters_kin': 'Deut 13:7 (THE LINE inciter_law_declared); the Sifrei 87:4-11; Sanhedrin 85b:2', 'entice_two_senses': 'Deut 13:7; the Sifrei 87:1-3, 12-13; Kiddushin 80b:6', 'the_entrapment': 'Deut 13:7, 13:9; Mishnah Sanhedrin 7:10 at Sanhedrin 67a:2-5, 12-13; SA by CALL', 'the_fifteen_utterances': 'Deut 13:7, 13:14; Sanhedrin 67a:6; the Sifrei 91:3; Mishnah Sanhedrin 7:6 (carried); OR by CALL', 'the_five_prohibitions': 'Deut 13:9 (THE REUSE pity_barred); Deut 7:16 by CALL (SN); Leviticus 19:16, 19:18 by CALL (HO); Exodus 23:5 by CALL (OR); the Sifrei 89:1-5; Sanhedrin 36b:5', 'the_courts_rule_inverted': 'Deut 13:9-10; the Sifrei 89:6-7; Sanhedrin 33b:7, 36b:5, 43a:21, 61b:3-11, 63b:7; Mishnah Sanhedrin 4:1 at 40a:9-14 by CALL (OR)', 'the_hand_first': 'Deut 13:10; the Sifrei 89:8; Leviticus 24:14 by CALL (L24); Leviticus 20:2 by CALL (SA)', 'the_stoning_rite': "Deut 13:11 (THE CASE — stoned, evil_purged_from_the_midst); Lev 24:23, Num 15:36 (the tape — stoned_as_commanded); MK by CALL; the Sifrei 90:1-2; Sifrei Bamidbar 113-114; Sanhedrin 54b:5", 'the_execution_timing': 'Deut 13:12 (THE WRITE israel_hears_and_fears; the parameter the_execution_timing); the Sifrei 91:1-2; Mishnah Sanhedrin 11:4; Tosefta Sanhedrin 11:3; Sanhedrin 89a:6',
       'one_city_at_a_time': 'Deut 13:13 (THE LINE condemned_city_law_declared) [1]; the Sifrei 92:1-4; Mishnah Sanhedrin 1:5; Sanhedrin 2a, 16b, 111b:16-19; Tosefta Sanhedrin 14:1; PN by CALL', 'to_dwell_there_jerusalem': 'Deut 13:13; the Sifrei 92:5; Bava Kamma 82b:4, 8', 'the_seducers_parameters': 'Deut 13:14 (THE WRITE condemned_city_inquiry_required); the Sifrei 93:1-5; Sanhedrin 111b:6-7, 14-15, 67a:16; Mishnah Sanhedrin 10:4; CH by CALL', 'the_majoritys_procedure': 'Deut 13:14-16; Sanhedrin 112a:2-8', 'the_seven_interrogations': "Deut 13:15 (THE WRITE condemned_city_inquiry_required; the parameter the_inquiries); the Sifrei 93:6-9; 149:1-2; 190:7-8; Mishnah Sanhedrin 5:1-2; Sanhedrin 40a-40b; OR, SA by CALL", 'the_congruence_rule': 'Deut 13:15; Mishnah Sanhedrin 5:2; Sanhedrin 40a:4-7, 41a:18-20', 'the_sword': 'Deut 13:16 (THE CASE — put_to_death); Bava Metzia 31b:3; Sanhedrin 52b:12; the Sifrei 94:1-3; SA by CALL', 'the_property_table': 'Deut 13:16-17; Mishnah Sanhedrin 10:5; Sanhedrin 111b:8-9, 112a:10-17; the Sifrei 94:4-5, 95:1', 'the_devoting': "Deut 13:16 (THE CASE'S WRITE city_devoted); Num 21:3 (the tape); Exodus 22:19, Leviticus 27:28-29, Numbers 21:2-3, Deut 7:2 by CALL (OR, TM, CK, SN)", 'belial_and_naboth': 'Deut 13:14; the Sifrei 93:2, 117:3; Bava Batra 10a:10; Ketubot 68a:2; Berakhot 31b:4; Tosefta Peah 4:19; 1 Kings 21:10', 'the_law_as_a_study_text': 'Deut 13:13-19; Tosefta Sanhedrin 14:1; Sanhedrin 71a:17, 113a:3 (carried), 41a:25',
       'the_whole_offering': 'Deut 13:17; Mishnah Sanhedrin 10:6; Sanhedrin 111b:10-12; the Sifrei 95:2-5; 1 Samuel 7:9', 'heavens_spoil': 'Deut 13:16-17; Sanhedrin 112b:1-113a:2; Temurah 8a:9; Tosefta Sanhedrin 4:5, 14:5; TM by CALL', 'the_heap_forever': 'Deut 13:17; Sanhedrin 111b:13, 113a:4-10; the Sifrei 95:6-7, 96:1; Joshua 6:26; 1 Kings 16:34', 'nothing_shall_cleave': 'Deut 13:18 (THE WRITE devoted_thing_cleaving_barred); Avodah Zarah 12b:7, 34b:15, 43b:19, 44b:1, 49b-50a; Tosefta Avodah Zarah 4:3, 7:5; Pesachim 48a:5; Mishnah Shabbat 9:6; the Sifrei 96:2; Deut 7:26 by CALL (SN)', 'the_citron_of_a_condemned_city': 'Deut 13:18; Sukkah 34b:8; Mishnah Sukkah 3:5', 'the_devoted_things_lashes': 'Deut 13:18; Makkot 22a:2, 22a:9 (carried); SN by CALL', 'the_anger_keyed_to_idolatry': 'Deut 13:18; the Sifrei 96:3; Mishnah Sanhedrin 10:6; Sanhedrin 111b:13, 113b:2-3; Num 25:4 (the tape — hanging_commanded); BK by CALL; Joshua 7:26', 'the_mercy_two_armed': 'Deut 13:18; the Sifrei 96:4; Shabbat 151b:14; Yevamot 79a:3; Beitzah 32b:4; Tosefta Sotah 10:1', 'as_he_swore_to_your_fathers': 'Deut 13:18 (THE POINTER); the Sifrei 96:5; SN, NR by CALL',
       'the_footer_the_condition': 'Deut 13:19 (no line, no write); Deut 12:25, 28 by CALL (PN); Deut 6:18 by CALL (HI); Deut 11:13 by CALL (BC); the Sifrei 96:6-8; 1 Kings 22:43', 'the_light_as_the_weighty': 'Deut 13:1, 13:19; the Sifrei 82:1, 96:7; Avot 2:1 (carried), 3:9, 3:14',
       'the_table': 'Deut 13:1-19 (the readback table)', 'the_supplied_law_rows': 'Deut 13:4, 13:12, 13:15, 13:18 (the supplied law rows with their writes); 13:2, 13:7, 13:13 (the lines); 13:6 (the case)', 'the_pointer_row': 'Deut 13:18 (the pointer row)', 'no_retrograde_row': 'Deut 13:1-19 (no retrograde row)', 'the_two_verbs_of_stoning': 'Deut 13:11 (the DB — the two verbs of stoning)', 'the_purge_formulas_nine_seats': "Deut 13:6 (the DB — the purge formula's nine seats)", 'the_seducers_one_formula': "Deut 13:3, 13:7, 13:14 (the kin by computation — the seducers' one formula)"}
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch13_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p23.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(SE, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, SE.DATA)
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
    print('THE INK: the number verse %s (ordinals none; no starred token); the register singular-only %s, plural-only %s, both %s, neither %s; the negations %s; the Name %d bare tokens; Moses unnamed %s; the one narrative verb %s; the infinitive absolutes %s; the tokens %d, the letters %d' % (PARSED, SG_ONLY, PL_ONLY, BOTH, NEITHER, {v: [x for x in W13(v) if x in NEG] for v in range(1, 20) if any(x in NEG for x in W13(v))}, sum(1 for v in range(1, 20) for x in W13(v) if x == 'יהוה'), DATA['moses_unnamed']['value'], WAYY, INF_ABS, TOKN, LETN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s (the writes %s); the pointer rows %s; no row open %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [r['write'] for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], not any(r['open'] for r in READBACK), [o['name'] for o in OPEN_ROWS], len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the_signs_status %s; the_prophets_death %s; the_execution_timing %s; the_inquiries %s' % (CLOCK, {k: v[:40] for k, v in SIGNS.items()}, {k: v[:40] for k, v in DEATH.items()}, {k: v[:40] for k, v in TIMING.items()}, sorted(INQ)))
    print('THE SCANS on the one database: the five on Israel %s; the three reused effects\' entities %s' % (SEDUCERS_SCAN, REUSE_SCAN))
    print('THE CALLEES: OH add_nothing %s; CH second word %s; HI test %s; SN pity %s, wood %s; ST four %s; PN one %s; OR idolater %s, devoted %s, asymmetry %s; ER four verbs %d; SA strangled %s, who_stones %s; L24 %s; MK stones %s; TM person %s; CK cherem %s; BK anger %s; BH dreams %s; MM test %s; HO rule %s' % (OH_ADD[0][:30], CH_OTHER[0][:30], HI_TEST[0][:30], SN_PITY[0][:30], SN_WOOD[1], ST_FOUR[0][:30], PN_ONE[0][:30], OR_IDOL['v'], OR_DEV['v'], OR_ACQ['v'], len(ER_FOUR['v']), SA_STRANG['v'], SA_WHO['v'], L24_TALION['verdict'], MK_STONES[0][:30], TM_DEV['v'], CK_CHEREM[1], BK_ANGER[1], BH_DREAMS[0][:30], MM_MORIAH['v'], HO_RULE['v'][0]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s (one — the Asherah\'s wood in the plow); stoned %s, put_to_death %s, evil_purged %s, city_devoted %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5], SCENE[6], SCENE[7], SCENE[8], SCENE[9]))
    print('THE NARRATIVE: %s (the eight on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_purge_formulas_seats', 'the_two_verbs_of_stoning', 'the_seven_inquiries', 'the_readback')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 13: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch13_part5.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s; DATA rows %d' % (count, per_cell, SE.SCENE, SE.NARRATIVE, len(SE.DATA)))
