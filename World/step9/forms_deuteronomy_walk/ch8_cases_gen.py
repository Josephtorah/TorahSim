#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch6_cases_gen.py's form.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_good_land as SN
p2 = open(f'{SP}/ch8_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_frame'), ('F2', 'the_way_of_forty_years'), ('F3', 'the_good_land'), ('F4', 'take_heed_lest_you_forget'), ('F5', 'the_chain_and_the_covenant'), ('F6', 'the_testimony')]
REF = {'all_the_commandment': 'Deut 8:1', 'live_and_possess': 'Deut 8:1; Deut 4:1 by CALL', 'the_oath_seats': 'Deut 8:1, 8:18; Deut 7:8 by CALL', 'no_receipt': 'Deut 8:1-20 (the register gate\'s finder)',
       'forty_years': 'Deut 8:2, 8:4; Num 14:34 by CALL', 'the_test': 'Deut 8:2; Exod 16:4', 'the_humbling': 'Deut 8:2-3; Yoma 74b:11-13', 'the_manna': 'Deut 8:3, 8:16; Exod 16:13-15 by CALL', 'not_by_bread_alone': 'Deut 8:3; the Sifrei 48:10', 'the_garment_and_the_foot': 'Deut 8:4 (the fifth form)', 'the_discipline': 'Deut 8:5; Deut 1:31 by CALL', 'keep_walk_fear': 'Deut 8:6', 'the_messianic_forty': 'Deut 8:3; Sanhedrin 99a',
       'the_good_land': 'Deut 8:7, 8:10; Deut 6:3, 6:10-11 by CALL', 'the_waters': 'Deut 8:7; the Sifrei 39:8', 'the_seven_species': 'Deut 8:8; Berakhot 41a-b', 'the_measures_seat': 'Deut 8:8; Eruvin 4a', 'honey_without_milk': 'Deut 8:8', 'lack_nothing': 'Deut 8:9; Deut 2:7 by CALL', 'iron_and_copper': 'Deut 8:9; Taanit 4a', 'eat_be_satisfied_bless': 'Deut 8:10; Berakhot 21a, 48b', 'the_measure_of_satisfied': 'Deut 8:10; Berakhot 49b:9', 'less_than_an_egg_bulk': 'shelf: Mishnah Sukkah 2:5', 'the_blessing_before': 'Deut 8:10; Berakhot 35a', 'the_four_blessings': 'Deut 8:10; Berakhot 48b', 'the_grace_conditional': 'shelf: Berakhot 49b:4', 'the_sabbath_forgotten': 'shelf: Berakhot 49b:5', 'the_persons': 'shelf: Berakhot 20b', 'the_meals_base': 'shelf: Berakhot 44a:10, 35b:20', 'the_first_fruits': 'Deut 8:8; Mishnah Bikkurim 1:3', 'the_grace_in_any_language': 'shelf: Sotah 33a', 'the_meals_end': 'shelf: Berakhot 42a:7, 43a:11',
       'take_heed_lest': 'Deut 8:11; Deut 6:12 by CALL', 'no_action_no_lashes': 'shelf: Makkot 13b:6', 'the_triad': 'Deut 8:11; Deut 7:11 by CALL', 'the_growth_list': 'Deut 8:12-13; Deut 6:10-11 by CALL', 'the_heart_lifted': 'Deut 8:14; Sotah 4b', 'the_eighth_of_an_eighth': 'shelf: Sotah 5a:16-17', 'the_exodus_formula': 'Deut 8:14; Deut 5:6 by CALL',
       'the_wilderness': 'Deut 8:15; Deut 1:19', 'the_serpents': 'Deut 8:15; Num 21:6 by CALL', 'the_rock_of_flint': 'Deut 8:15; Exod 17:6', 'the_manna_to_do_you_good': 'Deut 8:16; Exod 16:13-15 by CALL', 'my_power_my_hand': 'Deut 8:17-18', 'the_covenant_established': 'Deut 8:18; Gen 22:16, 26:3, 50:24 by CALL',
       'if_you_forget': 'Deut 8:19; the Sifrei 48:8', 'other_gods_serve_bow': 'Deut 8:19; Deut 5:9 by CALL', 'i_testify': 'Deut 8:19; Deut 4:26 by CALL', 'like_the_nations': 'Deut 8:20; Deut 7:1 by CALL', 'the_heel': 'Deut 8:20; Deut 7:12 by CALL', 'hearken_plural': 'Deut 8:20', 'the_readback_table': 'Deut 8:1-20', 'the_write': 'the write'}
lines = ['\n\n# =====================================================================\n# Motion 2 — THE TEST DATA: the answer sheet\'s rows (the docket\'s LAW rows and the cells\' asks) — GENERATED FROM THE CELLS\' OWN ASKS by ch8_cases_gen.py\n# (1b\'s lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.\n# =====================================================================\nCASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(SN, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, SN.DATA)
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
    print('THE INK: the two number verses %s (the sated verb starred at 8:10 and 8:12); no frame %s, no saying, no imperative %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s, neither %s; the infinitive absolutes %s; the prohibitions second person %d, third %d; the first person %s' % (sorted(PARSED.items()), DIV, IMPER, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH, NEITHER, {v: [x for x, _ in l] for v, l in INFA.items()}, sum(1 for v in PRO for _, m in PRO[v] if 'i2' in m), sum(1 for v in PRO for _, m in PRO[v] if 'i3' in m), {v: [x for x, _ in l] for v, l in ONE_CS.items()}))
    print('THE READBACK OF A STATE (the fifth form): %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); no row open %s; the holes %d: %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), not any(r['open'] for r in READBACK), len(HOLES), [h['hole'].split(' — ')[0] for h in HOLES]))
    print('THE DELTAS (computed): %s' % (DELTA,))
    print('THE STATE\'S SCAN on the one database: %s; the receipt seats %s (chapter 5: %s)' % (GARMENT_SCAN, receipt_seats(8), receipt_seats(5)))
    print('THE CALLEES: hear_and_do %s / take_heed %s / the_witnesses %s; forty_years %s, day_by_day %s, trials %s; day_for_year %s; bite_and_burn %s, meribah_seats %s; the_land_flowing %s, the_list %s, lest_you_forget %s (no write); lacking_nothing %s, the_carrying %s; no_other_gods %s, bow_and_serve %s, the_first_word %s; the_oath %s, the_triad %s, the_heel %s, the_ban %s; bread_water %s; live_by_them %s; the oath lines %s / %s / %s' % (OH_HEAR[1], OH_HEED[1], OH_WIT[1], ES_FORTY['v'], ES_DAY['v'], ES_SIX['v'], SL_DAY[0][:8], CK_BITE[1], CK_SEATS[0][:20], HI_FLOW[1], HI_LIST[1], HI_FORGET[1], OS_LACK[1], OS_CARRY[1], CH_NOG[1], CH_BOW[1], CH_FIRST[1], SN_OATH[1], SN_TRIAD[1], SN_HEEL[1], SN_BAN[1], OR_BREAD['v'], SA_LIVE['v'], MA_TEST['v'], MA_FAM['v'], JS_KT['v']))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s (none — a prohibition without an action); the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes' % (len(DATA[k]['value']), len(DATA[k]['holes']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 8: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch8_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, SN.SCENE, SN.NARRATIVE))
