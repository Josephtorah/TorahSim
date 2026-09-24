import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 5 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch15_cases_gen.py's form, cut to the lean pass (no persons list). RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_festivals_judges as FJ
p23 = open(f'{SP}/ch16_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_passover_at_the_place'), ('F2', 'the_weeks_from_the_sickle'), ('F3', 'the_feast_of_booths'), ('F4', 'the_three_pilgrimages'), ('F5', 'the_judges_in_every_gate'), ('F6', 'the_asherah_and_the_pillar'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 16:1-8', 'F2': 'Deut 16:9-12', 'F3': 'Deut 16:13-15', 'F4': 'Deut 16:16-17', 'F5': 'Deut 16:18-20', 'F6': 'Deut 16:21-22', 'RB': 'Deut 16:1-22 (the readback table)'}
REF = FJ.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the eight Mishnah rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch16_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p23.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(FJ, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, FJ.DATA)
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
    print('THE INK: the number verses %s (the ordinals %s; the starred token %s); the register singular-only (the reading\'s frames assert); the negations %s; the Name %d bare tokens; the infinitive absolute %s; the tokens %d' % ({v: PARSE[v][0] for v in NUMV}, {v: PARSE[v][1] for v in ORDV}, {v: PARSE[v][2] for v in STARV}, NEG, NAME_BARE, INF_ABS, TOKN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s; the rows with writes %s; the pointer rows %s; the state rows %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [(r['verses'], r['write']) for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], [r['verses'] for r in READBACK if r['state']], OPEN_ROWS, len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the twenty-nine %s (in the registry %d, in DATA %d)' % (CLOCK, len(PARAMETERS), sum(1 for p in PARAMETERS if p in WE.CAL_PARAMS), sum(1 for p in PARAMETERS if p in DATA)))
    print('THE SCANS on the one database: the fifteen on Israel %s; the bribe %s; the pillars %s; the courts %s; the appearing %s' % (HOLE_SCAN, BRIBE_SCAN, PILLAR_SCAN, COURTS_SCAN, APPEAR_SCAN))
    print('THE CALLEES: MO window %s, morrow %s, count %s, booths %s; PS %s; CA %s; ER %s; MU %s; ES %s; OR %s; HO %s; ST %s; SN %s; CH %s; JR %s; PSH %s' % (MO_WINDOW, MO_MORROW, MO_COUNT, MO_SUK_LEN, PS_EAT, CA_MALE, ER_STAND, MU_REDRESS, ES_SIZES, OR_ONE_TWO, HO_FAVOR, ST_BRIBE[:30], SN_WOOD[1], CH_KEEP[:24], JR_THREE[:24], PSH_DIST))
    print('THE EXAM (lean): the eight Mishnah rows %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the sixteen on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_eight_and_the_two_ordinals', 'the_readback')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 16 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch16_part5.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, FJ.NARRATIVE, len(FJ.DATA), len(FJ.PARAMETERS)))
