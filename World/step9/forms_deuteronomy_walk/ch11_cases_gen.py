import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch10_cases_gen.py's form.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_blessing_and_curse as BC
p2 = open(f'{SP}/ch11_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_discipline_retold'), ('F2', 'the_land_watered_by_heaven'), ('F3', 'the_second_paragraph'), ('F4', 'the_borders_and_the_dread'), ('F5', 'the_blessing_and_the_curse'), ('F6', 'the_readback')]
REF = {'love_and_keep': 'Deut 11:1; Deut 10:12 (the tape), 6:5 by CALL', 'the_discipline_seen': 'Deut 11:2; Deut 8:5 by CALL; Num 26:9 by CALL', 'signs_and_deeds': 'Deut 11:3; Exod 12:29 (the tape); Mishnah Avot 5:4', 'the_sea_flowed': 'Deut 11:4; Exod 14:27-28 (the tape); Josh 2:10', 'the_wilderness_state': 'Deut 11:5 (THE STATE ROW — SUPPLIED, no write); Deut 8:2-4 by CALL', 'dathan_and_abiram': 'Deut 11:6; Num 16:31-34 (the tape); Num 26:9-11 by CALL', 'korah_unnamed': 'Deut 11:6; Num 16:32; Pesachim 119a:12; Sanhedrin 110a:11', 'every_living_thing': 'Deut 11:6; Gen 7:21-23 (the tape); Sanhedrin 37b', 'your_eyes_have_seen': 'Deut 11:7; Deut 7:19 by CALL; Josh 24:31; Judg 2:7',
       'all_the_commandment': 'Deut 11:8; Deut 8:1 by CALL', 'the_oath_to_the_fathers': 'Deut 11:9; Deut 8:1, 6:3 by CALL; Num 16:13-14', 'not_like_egypt': 'Deut 11:10; Gen 13:10 (the tape); Shabbat 85a:3', 'drinks_by_the_rain_of_heaven': 'Deut 11:11; Taanit 9b:10-11; Bava Batra 19a:18', 'the_land_watered_first': 'Deut 11:11-12; Taanit 10a:2-3', 'the_eyes_from_the_years_beginning': 'Deut 11:12; Rosh Hashanah 8a:16, 16b:3, 16b:12', 'the_decree_and_the_season': 'Deut 11:12, 11:14; Rosh Hashanah 17b:11-13',
       'if_you_hearken': 'Deut 11:13 (THE LINE second_paragraph_declared); Deut 6:5 by CALL', 'the_yoke_of_the_commandments': 'Deut 11:13-21; Mishnah Berakhot 2:2; Berakhot 14b:11-14 (THE WRITE yoke_of_the_commandments_accepted)', 'the_rain_in_its_season': 'Deut 11:14; Lev 26:4 by CALL; Deut 7:13 by CALL (THE WRITE rain_in_its_season)', 'the_early_and_the_late': 'Deut 11:14; Taanit 6a:3-7', 'the_rains_dates': 'Deut 11:14; Mishnah Taanit 1:1-5; Taanit 2a:1-3, 10a:11-16 (the parameter rain_dates)', 'the_prayer_from_the_clause': 'Deut 11:13-14; Taanit 2a:11; Berakhot 33a:11, 33a:29', 'the_cattle_first': 'Deut 11:15; Berakhot 40a:1; Gittin 62a:16', 'take_heed_lest': 'Deut 11:16; Deut 5:9, 8:19 by CALL; Deut 4:23', 'the_heavens_shut': 'Deut 11:17; Lev 26:19-20 by CALL; Taanit 3b:6 (THE WRITE heavens_shut_for_turning)', 'the_shuttings_threshold': 'Deut 11:17; Taanit 6b:8, 8a:18, 8b:1-3', 'the_shuttings_causes': 'Deut 11:16-17; Taanit 7b:5-8a:8, 8b:16, 10a:16', 'perish_quickly': 'Deut 11:17; Josh 23:16; 1 Kgs 8:35-36; Taanit 7b:4', 'these_my_words': 'Deut 11:18; Deut 6:4 (the tape); Sotah 32b:19-33a:4', 'the_frontlets_plural': 'Deut 11:18; Deut 6:8 by CALL; Kiddushin 36a:9', 'teach_your_sons': 'Deut 11:19; Deut 6:7 by CALL; Bava Batra 21a:2', 'the_doorposts_plural': 'Deut 11:20; Deut 6:9 by CALL; Kiddushin 34a:2, 34a:8; Yoma 11b:8', 'the_days_multiplied': 'Deut 11:21; Deut 6:2 by CALL; Sanhedrin 90b:12, 99a:10; Berakhot 8a:6', 'the_class_rule': 'Deut 11:18-20; Mishnah Kiddushin 1:7; Rosh Hashanah 17a:10',
       'keep_and_cleave': 'Deut 11:22; Deut 10:20 (the tape); Deut 4:4, 8:6 by CALL; Josh 22:5', 'nations_greater_than_you': 'Deut 11:23; Deut 7:1 (the tape); Deut 9:1, 4:38 by CALL', 'every_place_the_sole_treads': 'Deut 11:24; Num 34:1-12 (the tape); Num 34:6, Exod 23:31, Gen 15:18 by CALL; Josh 1:3-4', 'the_returners_line': 'Deut 11:24; Mishnah Sheviit 6:1; Gittin 8a; Tosefta Sheviit 4:5 (the parameter)', 'no_man_shall_stand': 'Deut 11:25; Deut 7:24 by CALL; Exod 23:27-30 by CALL; Josh 1:5', 'as_he_spoke_to_you': 'Deut 11:25 (THE POINTER); Exod 23:27; the Sifrei 52:4; Tosefta Sotah 8:6', 'the_pilgrims_guard': 'Deut 11:25; Exod 34:24; Pesachim 8b:7-9',
       'see_i_set_before_you': 'Deut 11:26 (THE LINE blessing_and_curse_set); Deut 7:12 (the tape); Deut 30:15-20', 'the_blessing_if': 'Deut 11:27; Deut 7:12 by CALL; the Sifrei 53:1', 'the_curse_if': 'Deut 11:28; Deut 8:20, 9:12 by CALL; the Sifrei 54:4', 'gerizim_and_ebal': 'Deut 11:29 (THE WRITE gerizim_ebal_ceremony_owed); Deut 27:11-13; Josh 8:30-35', 'the_ceremonys_form': 'Deut 11:29; Mishnah Sotah 7:5; Sotah 32a:11-13, 37a:7-9; Tosefta Sotah 8:7', 'the_ceremonys_tongue': 'Deut 11:29; Mishnah Sotah 7:2; Sotah 32a:6-8, 33a:13-14, 33b:1-2', 'forty_eight_covenants': 'Deut 11:26-29; Tosefta Sotah 8:7; Sotah 37b:1-6', 'the_place_three_ways': 'Deut 11:30; Sotah 33b:4-10 (the parameter gerizim_ebal_place)', 'the_samaritan_shechem': 'Deut 11:30; Gen 12:6 (the tape); Sotah 33b:6, 32a:10', 'the_ceremonys_day': 'Deut 11:29-31; Tosefta Sotah 8:1-6', 'possess_and_dwell': 'Deut 11:31; Kiddushin 26a:10; Ketubot 110b:7-111a:21', 'keep_to_do': 'Deut 11:32; Deut 4:8 by CALL', 'study_and_deed': 'Deut 11:13; Kiddushin 40b:8-12; the Sifrei 41:12',
       'the_table': 'Deut 11:1-32 (the readback table)', 'the_state_row': 'Deut 11:5 (the state row)', 'the_pointer_row': 'Deut 11:25 (the pointer row)', 'the_supplied_law_row': 'Deut 11:29 (the supplied law row)', 'no_retrograde_row': 'Deut 11:2-7 (no retrograde row)'}
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch11_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(BC, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, BC.DATA)
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
    print('THE INK: no number verse %s (ordinals %s); the one mark %s; the register singular-only %s, plural-only %s, both %s, neither %s; the consecutive perfects %d in %d verses; the negations %s; the Name %d bare tokens; Moses unnamed (the book\'s seats by chapter %s); the tokens %d, the letters %d' % (PARSED, {v: o for v, o in ORDS.items() if o}, [t for t in verse_words('Deut', 11, 15) if t[-1] in '#~^%@|*'], [v for v, (p, s) in NUM.items() if s and not p], [v for v, (p, s) in NUM.items() if p and not s], [v for v, (p, s) in NUM.items() if p and s], [v for v, (p, s) in NUM.items() if not p and not s], sum(len(v) for v in WEQ.values()), len(WEQ), {v: [x for x in W11(v) if x in NEG] for v in range(1, 33) if any(x in NEG for x in W11(v))}, sum(1 for v in range(1, 33) for x in W11(v) if x == 'יהוה'), DATA['moses_unnamed']['value'], TOK, LET))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s (the state row %s, the write %s); the pointer rows %s; no row open %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [r['verses'] for r in READBACK if r['state']], [r['write'] for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], not any(r['open'] for r in READBACK), [o['name'] for o in OPEN_ROWS], len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; rain_dates %s; gerizim_ebal_place %s' % (CLOCK, {k: v[:40] for k, v in RAIN_DATES.items()}, {k: v[:40] for k, v in GERIZIM_EBAL_PLACE.items()}))
    print('THE SCANS on the one database: the rain, the heavens, the yoke, the pair and the ceremony on Israel %s; the ceremony on other entities %s; the vocabulary\'s rain effects %s' % (RAIN_SCAN, CEREMONY_SCAN, RAIN_VOCAB))
    print('THE CALLEES: ES plagues %s, saved %s, ten %s; PR remnant %s; OR angel %s, hornet %s, little %s, borders %s; TC covenant %s / %s, cascade stage %s span %s; KR swallowed %s, mode %s; SC hu %s; BR extents %s; HI daughters %s, gates %s, compartments %s; CH bow %s' % (ES_PLAGUES['v'], ES_SAVED['v'], ES_TEN['v'], PR_REM['v'], OR_ANGEL['v'], OR_HORNET['v'], OR_LBL['v'], OR_BORDERS['v'], TC_COV['v'], TC_COV['fx'], TC_CASC['stage']['v'], TC_CASC['span']['v'], KR_SWAL[1], KR_MODE[0][:30], SC_HU[0][:40], BR_EXT[0][:50], HI_DAUGHTERS[1], HI_MEZ_GATES[1], HI_TEF_COMP[0][:50], CH_BOW[1]))
    print('THE SCENE on the bench: %s; the exempt arm %s; the lashes %s (none — 11:16\'s warning has no prohibition of its own); the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5]))
    print('THE NARRATIVE: %s (the five on Israel %s; the debit open toward %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger], _WN.entity('israel_people').ledger[4].get('counterparty')))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_open_debits_nine_to_ten', 'no_number_verse', 'the_readback')) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 11: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch11_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, BC.SCENE, BC.NARRATIVE))
