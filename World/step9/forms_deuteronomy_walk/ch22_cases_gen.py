import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 8 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended; the labels from the runner's
# own ASK_LABELS (the Mishnah row or the spine's rows each ask grades). ch19_cases_gen.py's form over four chapters (sixteen cells in four typed parts). RUN FROM THE REPO ROOT.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_persons_poor_court as PP
p27 = ''.join(open(f'{SP}/ch22_part{n}.py', encoding='utf-8').read() for n in (2, 3, 4, 5, 6, 7))
CELLS = [('F1', 'the_lost_thing'), ('F2', 'the_garments_nest_parapet_and_mixtures'), ('F3', 'the_slandered_bride'), ('F4', 'the_adulterer_the_betrothed_girl_and_the_seducer'), ('F5', 'the_fathers_wife_and_the_assembly'), ('F6', 'the_camp'), ('F7', 'the_slave_the_hire_and_the_interest'), ('F8', 'the_vows_and_the_laborer'), ('F9', 'the_divorce'), ('F10', 'the_newlywed_the_millstone_the_kidnapper_and_the_leprosy'), ('F11', 'the_pledge_and_the_wage'), ('F12', 'fathers_and_sons_the_stranger_and_the_gleanings'), ('F13', 'the_lashes_and_the_muzzle'), ('F14', 'the_levirate'), ('F15', 'the_wrestlers_and_the_weights'), ('F16', 'amalek'), ('RB', 'the_readback')]
VERSES = {'F1': 'Deut 22:1-4', 'F2': 'Deut 22:5-12', 'F3': 'Deut 22:13-21', 'F4': 'Deut 22:22-29', 'F5': 'Deut 23:1-9', 'F6': 'Deut 23:10-15', 'F7': 'Deut 23:16-21', 'F8': 'Deut 23:22-26', 'F9': 'Deut 24:1-4', 'F10': 'Deut 24:5-9', 'F11': 'Deut 24:10-15', 'F12': 'Deut 24:16-22', 'F13': 'Deut 25:1-4', 'F14': 'Deut 25:5-10', 'F15': 'Deut 25:11-16', 'F16': 'Deut 25:17-19', 'RB': 'Deut 22:1-25:19 (the readback table)'}
REF = PP.ASK_LABELS
lines = ['', '', '# =====================================================================', "# Motion 2 — THE TEST DATA: the answer sheet's rows (the forty-four Mishnah rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch22_cases_gen.py", "# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.", '# =====================================================================', 'CASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p27.split('\ndef %s(' % name)[1].split('\ndef ')[0]
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
    print('THE SCANS on the one database: the seventy-nine on Israel %s; the kin counts %s; the entities %s' % (HOLE_SCAN, KIN_COUNTS, {k: (v if v is None or len(v) <= 3 else len(v)) for k, v in SCANS.items()}))
    print('THE CALLEES: OR %s; M2 %s; MI %s; HO %s; HB %s; SA %s; PR %s; YV %s; VW %s; MU %s; NS %s; NG %s; MT %s; BH %s; BK %s; ES %s; FA %s; ZL %s; JO %s; PV %s; MK %s; SE %s; RW %s; CP %s; FJ %s; ST %s; RF %s; CH %s; SN %s; PN %s; HI %s; L24 %s; GL %s' % (OR_OX[0], M2_SEDUCER[1][0], 'IMPORT Deut 25:11-12' in MI_SRC, HO_KINDS[0][:2], HB_VINE[0], SA_COUNT[0], PR_ZONAH[0]['sages'][:1], YV_FOREIGN[0], VW_DELAY[1], bool(MU_DEADLINE), NS_EMITTER[0], NG_SKIN, MT_MEMBERS[0][:20], BH_REMEMBER[1], BK_CURSE[1], ES_BLOT[0], FA_NOSON[0], ZL_CHILD[1], JO_MOHAR[0], PV_MUZZLED[0][:20], MK_STONING[1], SE_NINE[1], RW_TALION[1], CP_HIRE[1], FJ_WREST[1], ST_LOVE[1], bool(RF_CRY), CH_KEEP[1], SN_ABOM[1], PN_INQ[1], HI_SEVEN[1], L24_HAND['verdict'], GL_R))
    print('THE EXAM (lean): the forty-four Mishnah rows %s; segments read 0' % (EXAM_ROWS,))
    print('THE NARRATIVE: %s (the seventy-nine on Israel %s)' % (NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger]))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA if k in ('the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_fifteen_hits', 'the_readback', 'the_receipts')) + ' (the other settings recorded in DATA — %d rows)' % len(DATA))
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTERS 22-25 (LEAN): the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch22_part8.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the narrative %s; DATA rows %d; parameters %d' % (count, per_cell, PP.NARRATIVE, len(PP.DATA), len(PP.PARAMETERS)))
