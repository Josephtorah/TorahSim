import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 5 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from part 4's
# own PERSONS (the shelf rows each ask grades) and the seven write asks' seats. ch13_cases_gen.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_food_tithe as FT
p23 = open(f'{SP}/ch14_part2.py', encoding='utf-8').read() + open(f'{SP}/ch14_part3.py', encoding='utf-8').read()
CELLS = [('F1', 'the_sons_and_the_cuttings'), ('F2', 'the_beasts'), ('F3', 'the_water_and_the_birds'), ('F4', 'the_carcass_and_the_kid'), ('F5', 'the_second_tithe'), ('F6', 'the_far_place_the_money_the_rejoicing_and_the_levite'), ('F7', 'the_third_year'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 14:1-2', 'F2': 'Deut 14:3-8', 'F3': 'Deut 14:9-20', 'F4': 'Deut 14:21', 'F5': 'Deut 14:22-23', 'F6': 'Deut 14:24-27', 'F7': 'Deut 14:28-29', 'RB': 'Deut 14:1-29 (the readback table)'}
REF = {a: s.split(" — the exam's row")[0] for _, _, a, s in FT.PERSONS}
REF.update({'the_cut_and_the_factions': 'THE WRITE cuttings_for_the_dead_barred; the Sifrei 96:10-11; Yevamot 13b:17-18, 14a:6-8; Leviticus 19:28 by CALL (HB)', 'the_abomination': 'THE WRITE abomination_eating_barred; the Sifrei 99:1-2; Chullin 114b:9-10; Leviticus 11 by CALL (SHM)',
            'any_carcass_the_torn': 'THE WRITE carcass_eating_barred; the Sifrei 104:1; Mishnah Chullin 4:4 at 72b:1-7; SA, OR by CALL', 'named_the_second': 'THE WRITE second_tithe_owed; the Sifrei 105:2; Numbers 18:21-24 by CALL (KO); Deut 12:17 by CALL (PN)',
            'the_rejoicing': 'THE REUSE rejoicing_before_the_lord_commanded; the Sifrei 107:16; Deut 12:7 by CALL (PN)', 'the_levites_ladder': 'THE REUSE levite_forsaking_barred; the Sifrei 108:1; Deut 10:9, 12:19, Numbers 18:20-24 by CALL (ST, PN, KO)',
            'one_tithe_not_two': 'THE WRITE poor_tithe_owed; the Sifrei 109:5, 109:10-11; Rosh Hashanah 12b:1-5; KO by CALL'})
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch14_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p23.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(FT, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, FT.DATA)
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
    print('THE INK: the number verses %s (ordinals none; the starred tithe tokens %s); the register plural-only %s, singular-only %s, both %s, neither %s; the negations %s; the Name %d bare tokens; the infinitive absolutes %s; the tokens %d, the letters %d' % (PARSED, {v: MARKS(14, v) for v in range(1, 30) if MARKS(14, v)}, [v for v, (p, s) in NUM.items() if p and not s], [v for v, (p, s) in NUM.items() if s and not p], [v for v, (p, s) in NUM.items() if p and s], [v for v, (p, s) in NUM.items() if not p and not s], {v: [x for x in W14(v) if x in NEG] for v in range(1, 30) if any(x in NEG for x in W14(v))}, sum(1 for v in range(1, 30) for x in W14(v) if x == 'יהוה'), INF_ABS, TOKN, LETN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s; the rows with writes %s; the pointer rows %s; no row open %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [(r['verses'], r['write']) for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], not any(r['open'] for r in READBACK), OPEN_ROWS, len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the_birds_signs %s; the_carcass_table %s; the_moneys_form %s; the_removal_date %s; the_tithes_new_year %s; the calendar\'s keys passover_7 %s, rosh_hashanah %s' % (CLOCK, sorted(BIRDS), sorted(CARC), sorted(MONEY), sorted(REMOVAL), sorted(NEWYEAR), FEST['passover_7'], FEST['rosh_hashanah']))
    print('THE SCANS on the one database: the five on Israel %s; the two reused effects\' entities %s' % (FOOD_SCAN, REUSE_SCAN))
    print('THE CALLEES: SHM pure %s, camel %s, fish %s, dove %s, clawer %s, touch %s; SA lashes %s (names 14:21 %s), who %s; CA cook %s; ER kid identical %s; OR dog %s, lashes %s; PR marks %s; HO recipients %s, import %s; HB gash %s; MO harvest %s; TM tenth %s; KO liable %s; YO 7 %s; SN holy %s; ST portion %s; PN place %s; PV altars %s; MM tithe %s; SE seal %s' % (SHM_PURE[0], SHM_CAMEL[0], SHM_FISH[0], SHM_DOVE[0], SHM_CLAWER[0], SHM_TOUCH[0], V(SA_LASH), 'Deut 14:21' in SA_LASH['why'], V(SA_WHO), CA_COOK[0], V(ER_KID), V(OR_DOG), V(OR_LASH), V(PR_MARKS), V(HO_RECIP), HO_IMPORT, V(HB_GASH), MO_HARVEST[0]['effect'], V(TM_TEN), str(V(KO_LIABLE))[:30], V(YO_C7), SN_HOLY[0][:24], ST_PORTION[0][:26], PN_PLACE[0][:36], V(PV_ALTARS), V(MM_TITHE), SE_SEAL[0][:24]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s; barred_from_it %s, impure_until_evening %s, torn_flesh_to_dogs %s, left_for_the_poor %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5], SCENE[6], SCENE[7], SCENE[8], SCENE[9]))
    print('THE NARRATIVE: %s (the seven on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_two_and_three', 'the_verses_no_one_cites', 'the_kids_three_seats', 'the_readback')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 14: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch14_part5.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s; DATA rows %d' % (count, per_cell, FT.SCENE, FT.NARRATIVE, len(FT.DATA)))
