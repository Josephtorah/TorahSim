import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 5 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch16_cases_gen.py's form over two chapters (eight cells in two typed parts). RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_courts_prophet as CP
p23 = open(f'{SP}/ch17_part2.py', encoding='utf-8').read() + open(f'{SP}/ch17_part3.py', encoding='utf-8').read() + open(f'{SP}/ch17_part4.py', encoding='utf-8').read()
CELLS = [('F1', 'the_blemished_sacrifice'), ('F2', 'the_idolaters_trial'), ('F3', 'the_high_court'), ('F4', 'the_king'), ('F5', 'the_priests_dues'), ('F6', 'the_levite_at_the_place'), ('F7', 'the_diviners'), ('F8', 'the_prophet'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 17:1', 'F2': 'Deut 17:2-7', 'F3': 'Deut 17:8-13', 'F4': 'Deut 17:14-20', 'F5': 'Deut 18:1-5', 'F6': 'Deut 18:6-8', 'F7': 'Deut 18:9-14', 'F8': 'Deut 18:15-22', 'RB': 'Deut 17:1-18:22 (the readback table)'}
REF = CP.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the eight Mishnah rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch17_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p23.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(CP, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, CP.DATA)
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
    print('THE INK: the number verses %s (no ordinal, no starred token; 18:6\'s one behind its prefix unread); the negations %s; the Name %d bare tokens; the tokens %s' % ({k: PARSE[k][0] for k in NUMV}, NEG, NAME_BARE, TOKN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s; the rows with writes %s; the pointer rows %s; the state rows %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [(r['verses'], r['write']) for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], [r['verses'] for r in READBACK if r['state']], OPEN_ROWS, len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the thirty %s (in the registry %d, in DATA %d)' % (CLOCK, len(PARAMETERS), sum(1 for p in PARAMETERS if p in WE.CAL_PARAMS), sum(1 for p in PARAMETERS if p in DATA)))
    print('THE SCANS on the one database: the thirty-seven on Israel %s; hears-and-fears %s; the false prophet %s; the inheritance %s; the kings %s; the prophet %s; the wholeness %s; the courts %s; the judges %s; the bribe %s; stoned %s; put to death %d; purged %s' % (HOLE_SCAN, HEARS_SCAN, FALSEP_SCAN, INHERIT_SCAN, KINGS_SCAN, PROPHET_SCAN, WHOLE_SCAN, COURTS_SCAN, JUDGES_SCAN, BRIBE_SCAN, STONED_SCAN, len(PUT_SCAN or []), PURGED_SCAN))
    print('THE CALLEES: SE %s; FJ %s; OP %s; ES %s; OR %s; SA %s; HB %s; PR %s; RF %s; KO %s; ST %s; PN %s; SN %s; CH %s; OH %s; RG %s; MK %s; GL %s; BK %s; PS_ %s' % (SE_PDEATH[1], FJ_TIERS[1], OP_THREE[:24], ES_SIZES, OR_ONE_TWO, SA_DEFS['ov'], HB_BEAR, PR_PASS, RF_PASS[1], KO_24[0][:2], ST_STAND[:24], PN_PLACE[1], SN_ABOM[1], CH_REQ[1], OH_DAY[1], RG_ONE['value'], MK_STONES[0][:24], str(GL_TOK['value'])[:24], BK_MOUTH[1], PS_WHOLE[0][0]))
    print('THE EXAM (lean): the eight Mishnah rows %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the thirty-seven on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_two_verses', 'the_readback')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTERS 17-18 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch17_part5.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, CP.NARRATIVE, len(CP.DATA), len(CP.PARAMETERS)))
