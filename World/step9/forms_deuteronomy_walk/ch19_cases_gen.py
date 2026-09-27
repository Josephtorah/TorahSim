import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 6 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch17_cases_gen.py's form over three chapters (nine cells in three typed parts). RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_refuge_war_family as RW
p25 = ''.join(open(f'{SP}/ch19_part{n}.py', encoding='utf-8').read() for n in (2, 3, 4, 5))
CELLS = [('F1', 'the_cities_of_refuge'), ('F2', 'the_landmark_and_the_witnesses'), ('F3', 'the_priests_speech'), ('F4', 'the_siege'), ('F5', 'the_broken_necked_heifer'), ('F6', 'the_captive'), ('F7', 'the_firstborns_double'), ('F8', 'the_rebellious_son'), ('F9', 'the_hanged'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 19:1-13', 'F2': 'Deut 19:14-21', 'F3': 'Deut 20:1-9', 'F4': 'Deut 20:10-20', 'F5': 'Deut 21:1-9', 'F6': 'Deut 21:10-14', 'F7': 'Deut 21:15-17', 'F8': 'Deut 21:18-21', 'F9': 'Deut 21:22-23', 'RB': 'Deut 19:1-21:23 (the readback table)'}
REF = RW.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the twenty-eight Mishnah rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch19_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p25.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(RW, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, RW.DATA)
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
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE INK: the number verses %s (no ordinal; the starred tokens at %s; none in chapter 20); the negations %s; the Name %d bare tokens; the tokens %s' % ({'%d:%d' % k: PARSE[k][0] for k in NUMV}, STARV, {'%d:%d' % k: len(v) for k, v in NEG.items()}, NAME_BARE, TOKN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s; the rows with writes %s; the pointer rows %s; the state rows %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [(r['verses'], r['write']) for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], [r['verses'] for r in READBACK if r['state']], OPEN_ROWS, len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the parameters %d (in the registry %d, in DATA %d); DATA rows %d' % (CLOCK, len(PARAMETERS), sum(1 for p in PARAMETERS if p in WE.CAL_PARAMS), sum(1 for p in PARAMETERS if p in DATA), len(DATA)))
    print('THE SCANS on the one database: the forty-five on Israel %s; cities %s; pity %s; hears-and-fears %s; one witness %s; two witnesses %s; hand first %s; abominations %s; fear not %s; captive %s; spoil %s; boundary %s; hanged %s; buried %d; blood %s; atoned %d; firstborn by the head %s; hated %s; stoned %s; put to death %d; purged %s; flees %s; dwells %s; land polluted %s; city devoted %s; driven out %s; lashes %s' % (HOLE_SCAN, CITIES_SCAN, PITY_SCAN, HEARS_SCAN, ONEW_SCAN, TWOW_SCAN, HANDF_SCAN, ABOM_SCAN, FEAR_SCAN, CAPT_SCAN, SPOIL_SCAN, BOUND_SCAN, HANGED_SCAN, len(BURIED_SCAN or []), BLOOD_SCAN, len(ATONED_SCAN or []), FBH_SCAN, HATED_SCAN, STONED_SCAN, len(PUT_SCAN or []), PURGED_SCAN, FLEES_SCAN, DWELLS_SCAN, LANDPOL_SCAN, CITYDEV_SCAN, DRIVEN_SCAN, LASHES_SCAN))
    print('THE CALLEES: PN %s; OH %s; RG %s / %s; OR %s; CP %s; SE %s; FJ %s; L24 %s; SN %s; MD %s; OP %s; CK %s; IS_ %s; PV %s; FA %s; ZL %s; MR %s; RF %s; MK %s; BK %s; SA %s; PS_ %s; GL %s' % (PN_CUT[1], OH_SET[1], RG_SIX[1], RG_ONE['value'], OR_ONE_TWO[0], CP_TWO[1], SE_SEVEN[1], FJ_TIERS[1], L24_EYE['verdict'], SN_COND[1], MD_MALE[1], OP_SIHON[1], CK_YOKE[1], IS_ATONE[0][:1], PV_HAGAR[0], FA_ONE[0][:1], ZL_DBL[1], MR_SHEET[0], RF_WOMB[1], MK_STONES[0][:24], BK_HANG[1], SA_MODE[0], PS_BYMAN[0][:1], GL_R))
    print('THE EXAM (lean): the twenty-eight Mishnah rows %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the forty-five on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_ten_verses', 'the_readback')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTERS 19-21 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch19_part6.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, RW.NARRATIVE, len(RW.DATA), len(RW.PARAMETERS)))
