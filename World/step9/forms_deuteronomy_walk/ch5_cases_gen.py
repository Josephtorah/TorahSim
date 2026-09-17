import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch4_cases_gen.py's form.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_covenant_at_horeb as CH
p2 = open(f'{SP}/ch5_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_assembly_called'), ('F2', 'the_second_word'), ('F3', 'the_first_tablet'), ('F4', 'the_second_tablet'), ('F5', 'the_tenth_word'), ('F6', 'the_voice_and_the_request'), ('F7', 'the_answer_and_the_charge')]
REF = {'hear_learn_keep_do': 'Deut 5:1', 'the_covenant_at_horeb': 'Deut 5:2', 'not_with_our_fathers': 'Deut 5:3', 'face_in_face': 'Deut 5:4', 'i_stood_between': 'Deut 5:5',
       'no_other_gods': 'Deut 5:7', 'no_image': 'Deut 5:8', 'bow_and_serve': 'Deut 5:9; Mishnah Sanhedrin 7:6', 'in_its_way': 'shelf: Sanhedrin 60b:3', 'the_embracer': 'shelf: Sanhedrin 60b:2', 'the_visiting': 'Deut 5:9-10', 'the_ketiv': 'Deut 5:10', 'the_write': 'the write',
       'the_first_word': 'Deut 5:6', 'the_second_word_row': 'Deut 5:7-10', 'the_third_word': 'Deut 5:11', 'the_fourth_word': 'Deut 5:12-15', 'keep_and_remember': 'Deut 5:12; Shevuot 20b', 'the_ox_and_the_ass': 'Deut 5:14; Bava Kamma 54b', 'the_servants_rest': 'Deut 5:14; Yevamot 48b', 'the_two_grounds': 'Deut 5:15', 'the_receipt_5_12': 'Deut 5:12; Sanhedrin 56b',
       'the_fifth_word': 'Deut 5:16', 'the_sixth_word': 'Deut 5:17', 'the_seventh_word': 'Deut 5:18', 'the_eighth_word': 'Deut 5:19; Sanhedrin 86a', 'the_ninth_word': 'Deut 5:20', 'the_tenth_word_row': 'Deut 5:21', 'the_reward_clause': 'Deut 5:16; Bava Kamma 55a', 'the_receipt_5_16': 'Deut 5:16; Sanhedrin 56b', 'the_counts': 'Deut 5:6-21',
       'covet_and_desire': 'Deut 5:21', 'the_wife_first': 'Deut 5:21', 'the_coveter_who_pays': 'shelf: Bava Metzia 5b:19-20',
       'added_no_more': 'Deut 5:22', 'the_tablets_given_to_me': 'Deut 5:22', 'you_came_near': 'Deut 5:23', 'the_request': 'Deut 5:24-27', 'hear_and_do': 'Deut 5:27; Shabbat 88a',
       'the_lord_heard': 'Deut 5:28', 'done_well': 'Deut 5:28', 'who_would_give': 'Deut 5:29; Avodah Zarah 4b-5a', 'return_to_your_tents': 'Deut 5:30; Beitzah 5a-b', 'stand_here_with_me': 'Deut 5:31', 'the_charge': 'Deut 5:32-33', 'the_readback_table': 'Deut 5:1-33', 'the_register_seats': 'Deut 5:12, 16, 32'}
lines = ['\n\n# =====================================================================\n# Motion 2 — THE TEST DATA: the answer sheet\'s rows (the docket\'s LAW rows and the cells\' asks) — GENERATED FROM THE CELLS\' OWN ASKS by ch5_cases_gen.py\n# (1b\'s lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.\n# =====================================================================\nCASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(CH, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, CH.DATA)
        assert v != 'no verdict in span', (name, a)
        lines.append('    (%r, lambda: %s({\'ask\': %r}, DATA), %r),' % ('%s — %s' % (REF.get(a, name), a), name, a, v))
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
    print('THE INK: numbers %s; the one frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s; the ketiv at 5:10' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH))
    print('THE LAWS\' READBACK: %d rows — %s; the law rows %d (the cells named %d, NO CELL %s); the deltas: the frame %s; the voice %s; the request %s; hear and do %s; the answer %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['law']), sum(1 for r in READBACK if r['law'] and r['cell'] != 'NO CELL'), [r['verses'] for r in READBACK if r['cell'] == 'NO CELL'], FRAME_DIFF, VOICE_DELTA, REQUEST_DELTA, HEAR_DO_DELTA, ANSWER_DELTA))
    print('THE TWO COPIES: %s (tokens, letters) — Exodus 20:2-17 against Deuteronomy 5:6-21; per word %s' % (COPIES, WORD_TOK))
    print('THE HOLES: the tape\'s first (2b) %s; the second — Exodus 20:18-21 no line (this sitting); the code\'s — the second and the tenth words compiled here')
    print('THE CALLEES: the honor %s; the fear %s; the days %s; we will do %s; Marah %s' % (HO_HONOR['v'], HO_FEAR['v'], ES_DAYS['v'], ES_SEATS['v'], ES_MARAH['v']))
    print('THE SCENE on the bench: %s; the exempt and stoned arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 5: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
MAIN = MAIN.replace("%s; the second — Exodus 20:18-21 no line (this sitting); the code\\'s — the second and the tenth words compiled here')", "%s; the second — Exodus 20:18-21 no line (this sitting); the code\\'s — the second and the tenth words compiled here' % (OH_HOLE,))")
open(f'{SP}/ch5_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, CH.SCENE, CH.NARRATIVE))
