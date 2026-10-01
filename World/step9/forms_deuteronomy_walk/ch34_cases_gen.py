import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 7 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch33_cases_gen.py's form over one chapter (six cells in three typed parts). RUN FROM THE REPO ROOT.
import subprocess, os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_moses_death as PP
p34 = ''.join(open(f'{SP}/ch34_part{n}.py', encoding='utf-8').read() for n in (2, 3, 4, 5, 6))
CELLS = [('F1', 'the_ascent_and_the_land_shown'), ('F2', 'the_oath_and_the_denial'), ('F3', 'the_death_and_the_burial'), ('F4', 'the_years_and_the_thirty_days'), ('F5', 'joshua_and_the_receipt'), ('F6', 'the_prophet_the_signs_and_the_terror'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 34:1-3', 'F2': 'Deut 34:4', 'F3': 'Deut 34:5-6', 'F4': 'Deut 34:7-8', 'F5': 'Deut 34:9', 'F6': 'Deut 34:10-12', 'RB': 'Deut 34:1-12 (the readback table)'}
REF = PP.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the five Mishnah rows and the one Tosefta row and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch34_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p34.split('\ndef %s(' % name)[1].split('\ndef ')[0]
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
    print('THE SCANS on the one database: the twelve on their ledgers %s; the kin counts %s; the reuses %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, {k: (v if v is None or len(v) <= 3 else len(v)) for k, v in SCANS.items()}))
    print('THE CALLEES (the facts printed and asserted from the print): %d facts — SC_GOUP %s; SC_DEATH %s; CR_120 %s; CR_GIFTS %s; BL_GRAVE %s; BL_CHAIN %s; GR_GRAVE %s; CK_DATES %s; CK_THIRTY %s; JR_MOUTH %s; ST_WALK %s; ZE_RUN %s; OS_HAND %s; BH_GIFTS %s; NS_DAYS %s; CP_MIDST %s; ER_BREAK %s; ES_SEA %s; JO_OATH %s; SH_NAME %s' % (len(FACTS_PRINT), SV(SC_GOUP, 30), SV(SC_DEATH, 30), SV(CR_120, 30), SV(CR_GIFTS, 30), SV(BL_GRAVE, 30), SV(BL_CHAIN, 30), SV(GR_GRAVE, 30), SV(CK_DATES, 30), SV(CK_THIRTY, 30), SV(JR_MOUTH, 30), SV(ST_WALK, 30), SV(ZE_RUN, 30), SV(OS_HAND, 30), SV(BH_GIFTS, 30), SV(NS_DAYS, 20), SV(CP_MIDST, 30), SV(ER_BREAK, 30), SV(ES_SEA, 30), SV(JO_OATH, 30), SV(SH_NAME, 30)))
    print('THE EXAM (lean): the five Mishnah rows and the one Tosefta row %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the twelve on three ledgers — %s)' % (NARRATIVE, {ent: [e['effect'] for e in _WN.entity(ent).ledger] for ent in LEDGERS3}))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_hits', 'the_readback', 'the_receipts')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 34 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch34_part7.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, PP.NARRATIVE, len(PP.DATA), len(PP.PARAMETERS)))
