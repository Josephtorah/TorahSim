import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch5_cases_gen.py's form.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_hear_o_israel as HI
p2 = open(f'{SP}/ch6_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_header'), ('F2', 'the_creed'), ('F3', 'the_four_duties'), ('F4', 'the_gift_and_the_warning'), ('F5', 'the_test_and_the_right'), ('F6', 'the_sons_question')]
REF = {'the_triad': 'Deut 6:1', 'the_charge_executed': 'Deut 6:1', 'hear_and_observe': 'Deut 6:3', 'the_land_flowing': 'Deut 6:3', 'your_sons_son': 'Deut 6:2',
       'hear_o_israel': 'Deut 6:4; Pesachim 56a', 'the_lord_is_one': 'Deut 6:4', 'with_all_your_heart': 'Deut 6:5; Mishnah Berakhot 9:5', 'with_all_your_soul': 'Deut 6:5; Berakhot 61b', 'with_all_your_might': 'Deut 6:5; the Sifrei 32:7', 'love_and_fear': 'Deut 6:5; Sotah 31a',
       'recite_when': 'Deut 6:7; Mishnah Berakhot 1:1-2', 'recite_how': 'Deut 6:7; Mishnah Berakhot 1:3', 'recite_who': 'shelf: Mishnah Berakhot 2:5', 'daughters_exempt': 'shelf: Kiddushin 29b', 'the_passages': 'Deut 6:6; Mishnah Berakhot 2:2', 'teach_your_sons': 'Deut 6:7; Kiddushin 29a-30b', 'tefillin_passages': 'Deut 6:8; Mishnah Menachot 3:7', 'tefillin_compartments': 'Deut 6:8; the Sifrei 35:3-4', 'tefillin_arm': 'Deut 6:8; Menachot 36b-37a', 'tefillin_order': 'Deut 6:8; Menachot 36a', 'tefillin_head': 'Deut 6:8; Menachot 37a-b', 'mezuzah_writing': 'Deut 6:9; Menachot 34a', 'mezuzah_doorpost': 'Deut 6:9; Menachot 33a-34a', 'mezuzah_gates': 'shelf: Yoma 11a', 'the_seven': 'Deut 6:8-9; Menachot 43b', 'the_write': 'the write',
       'the_list': 'Deut 6:10-11', 'lest_you_forget': 'Deut 6:12', 'fear_serve_swear': 'Deut 6:13; Temurah 3b-4a', 'no_other_gods': 'Deut 6:14', 'the_jealous_god': 'Deut 6:15',
       'you_shall_not_test': 'Deut 6:16; Arakhin 15a', 'surely_keep': 'Deut 6:17', 'the_right_and_the_good': 'Deut 6:18; Bava Metzia 108a', 'thrust_out_enemies': 'Deut 6:19',
       'the_four_askings': 'Deut 6:20; Pesachim 116a-b', 'the_answer_rows': 'Deut 6:21-24', 'the_receipt': 'Deut 6:25', 'righteousness_for_us': 'Deut 6:25', 'the_readback_table': 'Deut 6:1-25'}
lines = ['\n\n# =====================================================================\n# Motion 2 — THE TEST DATA: the answer sheet\'s rows (the docket\'s LAW rows and the cells\' asks) — GENERATED FROM THE CELLS\' OWN ASKS by ch6_cases_gen.py\n# (1b\'s lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.\n# =====================================================================\nCASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(HI, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, HI.DATA)
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
    print('THE INK: the one number verse %s; no frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s, the answer\'s first person plural %s; the imperatives %s; the infinitive absolute %s; the two plural prohibitions %s' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH, sorted(ONE_CP), IMPER, INFA, PROHIB))
    print('THE READBACK\'S THIRD FORM: %d rows — %s; every row inside a law %s; the deltas: the header %s; Massah %s; the going out %s; the plagues %s; the oath %s; the charge %s' % (len(READBACK), dict(RB_GRADES), all(r['law'] for r in READBACK), HEADER_DELTA, MASSAH_DELTA, OUT_DELTA, PLAGUE_DELTA, OATH_DELTA, CHARGE_DELTA))
    print('THE SPELLINGS (the open row): %s; the sign\'s four seats %s' % (FRONT, SIGN))
    print('THE RECEIPT WITHOUT THE NAME: %s (the finder blind — CO6)' % (RECEIPT_NO_NAME,))
    print('THE CALLEES: the trials %s / %s; the forgetting %d seats; the vain oath %s; the firstborn %s; the oath lines %s / %s / %s; the charge %s' % (ES_TEN['v'], ES_SIX['v'], len(OH.FORGET), DC_VO[:2], PE_HUMAN[0][:20], MA_TEST['v'], MA_FAM['v'], JS_KT['v'], ER_TORAH['v']))
    print('THE SCENE on the bench: %s; the exempt arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 6: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch6_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, HI.SCENE, HI.NARRATIVE))
