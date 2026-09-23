import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 5 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from part 4's
# own PERSONS (the shelf rows each ask grades) and the nine write asks' seats. ch14_cases_gen.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_release_firstborn as RF
p23 = open(f'{SP}/ch15_part2.py', encoding='utf-8').read() + open(f'{SP}/ch15_part3.py', encoding='utf-8').read()
CELLS = [('F1', 'the_release'), ('F2', 'the_needy_and_the_blessing'), ('F3', 'the_hand_opened'), ('F4', 'the_hebrew_slave'), ('F5', 'the_awl_and_the_double_hire'), ('F6', 'the_firstling'), ('F7', 'the_blemish_and_the_blood'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 15:1-3', 'F2': 'Deut 15:4-6', 'F3': 'Deut 15:7-11', 'F4': 'Deut 15:12-15', 'F5': 'Deut 15:16-18', 'F6': 'Deut 15:19-20', 'F7': 'Deut 15:21-23', 'RB': 'Deut 15:1-23 (the readback table)'}
REF = {a: s.split(" — the exam's row")[0] for _, _, a, s in RF.PERSONS}
REF.update({'the_exaction': 'THE WRITE exaction_barred; the Sifrei 112:8; Makkot 3b:7-10; ordinances.loan by CALL', 'the_heart_before_the_hand': 'THE WRITE hand_shutting_barred; the Sifrei 116:10-11, 117:2; Bava Metzia 31b',
            'the_doubled_verbs': 'THE WRITE hand_opening_commanded; the Sifrei 116:12, 117:6; Bava Metzia 31b:7-12', 'the_base_thought': "THE WRITE base_thought_barred; the Sifrei 117:1-3; Gittin 36a:11; seducers by CALL (the transfer)",
            'the_blessing_on_the_work': 'THE WRITE work_of_the_hand_blessed (the first seat); the Sifrei 117:9-10; Deut 14:29 by CALL (food_tithe)', 'the_empty_sending': 'THE WRITE empty_sending_barred; the Sifrei 119:1; Kiddushin 16b:19; erection.repeats by CALL',
            'the_blessing_beside_the_loss': 'THE WRITE work_of_the_hand_blessed (the second seat); the Sifrei 123:3', 'the_sanctify_for_value': 'THE WRITE firstling_sanctification_commanded; the Sifrei 124:4; Mishnah Arakhin 8:7; temurah.consecrate by CALL',
            'the_work_and_the_shearing': 'THE WRITE firstling_work_and_shearing_barred; the Sifrei 124:6; Bekhorot 9b, 24b, 41b; Chullin 135a-137a'})
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch15_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p23.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(RF, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, RF.DATA)
        assert v != 'no verdict in span', (name, a)
        assert a in REF, ('an ask without a label', name, a)
        lines.append('    (%r, lambda: %s({\'ask\': %r}, DATA), %r),' % ('%s; %s — %s' % (VERSES[code], REF[a], a), name, a, v))
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
    print('THE INK: the number verses %s (the ordinal %s; the starred years tokens %s); the register singular-only %s, none %s; the negations %s; the Name %d bare tokens; the infinitive absolutes %s; the tokens %d, the letters %d' % (PARSED, {v: o for v, o in ORDS.items() if o}, {v: MARKS(15, v) for v in range(1, 24) if MARKS(15, v)}, [v for v, (p, s) in NUM.items() if s and not p], [v for v, (p, s) in NUM.items() if not p and not s], {v: [x for x in W15(v) if x in NEG] for v in range(1, 24) if any(x in NEG for x in W15(v))}, sum(1 for v in range(1, 24) for x in W15(v) if x == 'יהוה'), INF_ABS, TOKN, LETN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s; the rows with writes %s; the pointer rows %s; the state rows %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [(r['verses'], r['write']) for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], [r['verses'] for r in READBACK if r['state']], OPEN_ROWS, len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the twenty-seven %s (in the registry %d, in DATA %d); the_release_date keys %s; the_firstlings_year keys %s' % (CLOCK, len(PARAMETERS), sum(1 for p in PARAMETERS if p in WE.CAL_PARAMS), sum(1 for p in PARAMETERS if p in DATA), sorted(RELDATE), sorted(FYEAR)))
    print('THE SCANS on the one database: the twelve on Israel %s; the four reused effects\' entities %s' % (HOLE_SCAN, REUSE_SCAN))
    print('THE CALLEES: YO cycle(7) %s, jubilee day %s, foreigner %s, valuation %s; CA timer %s; MP F1 %s; M3 exits %s; OR obligation %s, ladder %s; ER empty %s; KO womb %s; TM for value %s; PR table %s; PN place %s; SA ban %s; HO poor %s, hire %s; FT four %s; CH fourth %s; BC hearken %s; ES sent %s; PV firstling %s; GL seats %s; SE belial %s; MZ members %s' % (V(YO_C7), V(YO_JUB['release_day']), V(YO_FOREIGNER), V(YO_VAL_M), CA_TIMER[0], [r[0] for r in MP_F1], V(M3_EXITS), V(OR_IM), V(OR_LADDER), V(ER_EMPTY), str(V(KO_WOMB))[:30], V(TM_FBV), str(V(PR_TABLE))[:40], str(V(PN_PLACE))[:30], V(SA_BAN), V(HO_POOR), V(HO_HIRE), str(V(FT_FOUR))[:24], str(V(CH_FOURTH))[:24], str(V(BC_HEARKEN))[:24], V(ES_SENT), V(PV_FIRSTLING), GL_SEATS, str(V(SE_BELIAL))[:30], V(MZ_MEMBERS)))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s; barred_from_it %s, goes_free %s, severance_gift_owed %s, serves_for_ever %s, consecrated_firstborn %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5], SCENE[6], SCENE[7], SCENE[8], SCENE[9], SCENE[10]))
    print('THE NARRATIVE: %s (the fifteen on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_four_and_the_ordinal', 'the_verses_no_one_cites', 'the_registers_two_near_misses', 'the_readback')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 15: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch15_part5.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s; DATA rows %d' % (count, per_cell, RF.SCENE, RF.NARRATIVE, len(RF.DATA)))
