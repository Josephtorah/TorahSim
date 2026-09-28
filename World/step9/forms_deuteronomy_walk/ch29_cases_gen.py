import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 7 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch26_cases_gen.py's form over three chapters (fifteen cells in three typed parts). RUN FROM THE REPO ROOT.
import subprocess, os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_covenant_return_charge as PP
p29 = ''.join(open(f'{SP}/ch29_part{n}.py', encoding='utf-8').read() for n in (2, 3, 4, 5, 6))
CELLS = [('F1', 'the_moab_recital'), ('F2', 'the_covenant_and_the_oath'), ('F3', 'the_individuals_curse'), ('F4', 'the_lands_desolation'), ('F5', 'the_hidden_and_the_revealed'), ('F6', 'the_return_and_the_gathering'), ('F7', 'the_heart_circumcised'), ('F8', 'the_commandment_near'), ('F9', 'life_and_death'), ('F10', 'the_charge_and_the_crossing'), ('F11', 'the_law_written_and_the_hakhel'), ('F12', 'the_tent_and_the_commission'), ('F13', 'the_apostasy_foretold'), ('F14', 'the_song_commanded'), ('F15', 'the_book_beside_the_ark_and_the_assembly'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 29:1-8', 'F2': 'Deut 29:9-14', 'F3': 'Deut 29:15-20', 'F4': 'Deut 29:21-27', 'F5': 'Deut 29:28', 'F6': 'Deut 30:1-5', 'F7': 'Deut 30:6-10', 'F8': 'Deut 30:11-14', 'F9': 'Deut 30:15-20', 'F10': 'Deut 31:1-8', 'F11': 'Deut 31:9-13', 'F12': 'Deut 31:14-15, 31:23', 'F13': 'Deut 31:16-18', 'F14': 'Deut 31:19-22', 'F15': 'Deut 31:24-30', 'RB': 'Deut 29:1-31:30 (the readback table)'}
REF = PP.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the seven Mishnah and Tosefta rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch29_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p29.split('\ndef %s(' % name)[1].split('\ndef ')[0]
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
    print('THE SCANS on the one database: the fifty-nine on their ledgers %s; the kin counts %s; the reuses %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, {k: (v if v is None or len(v) <= 3 else len(v)) for k, v in SCANS.items()}))
    print('THE CALLEES: OS %s; GR %s; GL %s; ES %s; CH %s; HI %s; SN %s; OH %s; ST %s; NR %s; BC %s; SE %s; FT %s; RF %s; FJ %s; CP %s; FE %s; RW %s; TC %s; YV %s; CA %s; MD %s; MU %s; MA %s; PV %s; FA %s; ER %s; BH %s; CK %s; JR %s; VE %s; SHL %s; PN %s' % (OS_SHEP[1], GR_COMM[0][:20], GL_R, ES_BIRTH['v'], CH_FOUR[0][:20], HI_HEART[0][:20], SN_OATH[0][:20], OH_CHAIN['value']['the_chain'], ST_ARK['value']['r_yehuda'][:20], NR_STIFF['value']['the_seats'][:2], BC_SEE[0][:20], SE_SWORE[0][:20], FT_REMOVAL[0][:20], RF_END[0][:20], FJ_WHO[1], CP_COPY[0][:20], FE_THREE['value'][1], RW_FEAR[0][:20], TC_C5['stage']['v'], YV_7['v'], CA_MALE[1], MD_SUK['length']['v'], MU_EIGHTH[0][:20], MA_SODOM['v'], PV_120['v'], FA_BURIAL['fx'], ER_PILLAR['v'], BH_CLOUDS['value'], CK_DATES[0][:20], JR_FOUR['value'], VE_END['v'], SH_NAME[0][:20], PN_SIX[0][:20]))
    print('THE EXAM (lean): the seven Mishnah and Tosefta rows %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the sixty-eight on five ledgers — Israel %s; Joshua %s; Moses %s; the Levites %s; the tent %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger], [e['effect'] for e in _WN.entity('yehoshua').ledger], [e['effect'] for e in _WN.entity('moses').ledger], [e['effect'] for e in _WN.entity('the_levites').ledger], [e['effect'] for e in _WN.entity('the_tent_of_meeting').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_hits', 'the_readback', 'the_receipts')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTERS 29-31 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch29_part7.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, PP.NARRATIVE, len(PP.DATA), len(PP.PARAMETERS)))
