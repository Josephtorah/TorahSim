import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 7 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch22_cases_gen.py's form over three chapters (ten cells in three typed parts). RUN FROM THE REPO ROOT.
import subprocess, os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_firstfruits_ebal_curses as PP
p26 = ''.join(open(f'{SP}/ch26_part{n}.py', encoding='utf-8').read() for n in (2, 3, 4, 5, 6))
CELLS = [('F1', 'the_first_fruits'), ('F2', 'the_removal_and_the_confession'), ('F3', 'the_covenant_formula'), ('F4', 'the_stones_and_the_altar'), ('F5', 'the_people_this_day'), ('F6', 'the_six_and_the_six'), ('F7', 'the_twelve_curses'), ('F8', 'the_blessings'), ('F9', 'the_curses_of_the_house_and_the_field'), ('F10', 'the_curses_of_the_siege_and_the_exile'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 26:1-11', 'F2': 'Deut 26:12-15', 'F3': 'Deut 26:16-19', 'F4': 'Deut 27:1-8', 'F5': 'Deut 27:9-10', 'F6': 'Deut 27:11-13', 'F7': 'Deut 27:14-26', 'F8': 'Deut 28:1-14', 'F9': 'Deut 28:15-44', 'F10': 'Deut 28:45-69', 'RB': 'Deut 26:1-28:69 (the readback table)'}
REF = PP.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the twenty-six Mishnah rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch26_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p26.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(PP, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, PP.DATA)
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
    print('THE INK: the number verses %s, the ordinals %s (the starred tokens at %s); the negations %s; the Name %d bare tokens; the tokens %s' % ({'%d:%d' % k: PARSE[k][0] for k in NUMV}, {'%d:%d' % k: PARSE[k][1] for k in ORDV}, STARV, {'%d:%d' % k: len(v) for k, v in NEG.items()}, NAME_BARE, TOKN))
    print('THE READBACK — THE FORMS ON FILE, NO NEW FORM: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the SUPPLIED rows %s; the rows with writes %s; the pointer rows %s; the state rows %s; the OPEN rows %s; the holes %d' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [(r['verses'], r['write']) for r in READBACK if r['write']], [r['verses'] for r in READBACK if r['pointer']], [r['verses'] for r in READBACK if r['state']], OPEN_ROWS, len(HOLES)))
    print('THE COUNTER AND THE PARAMETERS: %s; the parameters %d (in the registry %d, in DATA %d); DATA rows %d' % (CLOCK, len(PARAMETERS), sum(1 for p in PARAMETERS if p in WE.CAL_PARAMS), sum(1 for p in PARAMETERS if p in DATA), len(DATA)))
    print('THE SCANS on the one database: the ninety-one on Israel %s; the kin counts %s; the reuses %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, {k: (v if v is None or len(v) <= 3 else len(v)) for k, v in SCANS.items()}))
    print('THE CALLEES: FT %s; RF %s; BC %s; SN %s; PN %s; FJ %s; PP %s; RW %s; SA %s / %s; M3 %s; HO %s; ST %s; CP %s; OH %s; GL %s; CH %s; HI %s; DC %s; SB %s; OR %s; ES %s; KO %s; CA %s; CK %s; TC %s / %s; NS %s; JO %s; PV %s; BR %s; PR %s; CT %s; SE %s; JR %s; OS %s' % (FT_REMOVAL[0][:30], RF_RECEIPT[0][:30], BC_GE[1], SN_HOLY[1], PN_REJ[1], FJ_TIMES[1], PP_JUST[1], RW_LAND[1], SA_KARET['v'], SA_MODE['v'], M3_MODE['v'], HO_GIFTS['v'][:2], ST_70[1], CP_COPY[1], OH_WOOD[0][:30], GL_R, CH_FOUR[1], HI_MEZ[1], DC_HEWN[0], SB_HEWN['v'], OR_OX['v'], ES_TREASURE['v'], KO_BIK[1], CA_FF[0][:20], CK_CLAUSES[1], TC_COV_T['v'], TC_C4['stage']['v'], NS_LANG[0], JO_70, PV_STATIONS['v'], BR_ORDER[1], PR_STRANGER['v']['seats'], CT_ONEN['v'], SE_KIN[1], JR_MOLTEN[1], OS_BAER))
    print('THE EXAM (lean): the twenty-six Mishnah rows %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the ninety-six on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_hits', 'the_readback', 'the_receipts')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTERS 26-28 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch26_part7.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, PP.NARRATIVE, len(PP.DATA), len(PP.PARAMETERS)))
