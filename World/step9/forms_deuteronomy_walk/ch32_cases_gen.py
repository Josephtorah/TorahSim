import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 7 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch29_cases_gen.py's form over one chapter (sixteen cells in three typed parts). RUN FROM THE REPO ROOT.
import subprocess, os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_song_charge_nebo as PP
p32 = ''.join(open(f'{SP}/ch32_part{n}.py', encoding='utf-8').read() for n in (2, 3, 4, 5, 6))
CELLS = [('F1', 'the_witnesses_and_the_rock'), ('F2', 'the_crooked_generation'), ('F3', 'the_nations_divided_and_the_portion'), ('F4', 'the_desert_and_the_eagle'), ('F5', 'the_heights_and_the_feast'), ('F6', 'jeshurun_fat_and_the_demons'), ('F7', 'the_hidden_face_and_the_fire'), ('F8', 'the_evils_heaped'), ('F9', 'the_enemys_boast'), ('F10', 'the_joined_thousand_and_the_vine_of_sodom'), ('F11', 'the_cup_in_store_and_the_vengeance'), ('F12', 'i_am_he_and_the_land_atones'), ('F13', 'the_song_spoken_with_hoshea'), ('F14', 'the_charge_after_the_song'), ('F15', 'the_summons_to_nebo'), ('F16', 'meribah_and_the_seeing'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 32:1-4', 'F2': 'Deut 32:5-6', 'F3': 'Deut 32:7-9', 'F4': 'Deut 32:10-12', 'F5': 'Deut 32:13-14', 'F6': 'Deut 32:15-18', 'F7': 'Deut 32:19-22', 'F8': 'Deut 32:23-25', 'F9': 'Deut 32:26-28', 'F10': 'Deut 32:29-33', 'F11': 'Deut 32:34-38', 'F12': 'Deut 32:39-43', 'F13': 'Deut 32:44-45', 'F14': 'Deut 32:46-47', 'F15': 'Deut 32:48-50', 'F16': 'Deut 32:51-52', 'RB': 'Deut 32:1-52 (the readback table)'}
REF = PP.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the twenty-six Mishnah and Tosefta rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch32_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p32.split('\ndef %s(' % name)[1].split('\ndef ')[0]
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
    print('THE SCANS on the one database: the forty-two on their ledgers %s; the kin counts %s; the reuses %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, {k: (v if v is None or len(v) <= 3 else len(v)) for k, v in SCANS.items()}))
    print('THE CALLEES (the facts printed and asserted from the print): %d facts — OH_CHAIN %s; CR_HIDE %s; GL_FLINT %s; ES_TREASURE %s; CP_TWO %s; RF_ATONE %s; CK_DATES %s; OS_MTN %s; JR_NOWRITE %s; SH_NAME %s; HI_ONE %s; FE_EAGLE %s; FJ_WHO %s; GR_GRAVE %s; BR_LAND %s' % (len(FACTS_PRINT), SV(OH_CHAIN, 40), SV(CR_HIDE, 30), SV(GL_FLINT, 30), SV(ES_TREASURE, 20), SV(CP_TWO, 30), SV(RF_ATONE, 30), SV(CK_DATES, 30), SV(OS_MTN, 30), SV(JR_NOWRITE, 30), SV(SH_NAME, 30), SV(HI_ONE, 30), SV(FE_EAGLE, 30), SV(FJ_WHO, 30), SV(GR_GRAVE, 30), SV(BR_LAND, 30)))
    print('THE EXAM (lean): the twenty-six Mishnah and Tosefta rows %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the forty-five on three ledgers — Israel %s; Joshua %s; Moses %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger], [e['effect'] for e in _WN.entity('yehoshua').ledger], [e['effect'] for e in _WN.entity('moses').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_hits', 'the_readback', 'the_receipts')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 32 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch32_part7.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, PP.NARRATIVE, len(PP.DATA), len(PP.PARAMETERS)))
