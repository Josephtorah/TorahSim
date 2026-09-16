import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_obey_horeb as OH
p2 = open(f'{SP}/ch4_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_exhortation'), ('F2', 'horeb_retold'), ('F3', 'no_image'), ('F4', 'the_exile_case'), ('F5', 'the_one_god'), ('F6', 'the_cities_and_the_frame')]
REF = {'hear_and_do': 'Deut 4:1', 'add_nothing': 'Deut 4:2', 'diminish_nothing': 'Deut 4:2', 'add_out_of_its_time': 'shelf: Rosh Hashanah 28b:9', 'add_beside': 'shelf: Sanhedrin 89a:2', 'baal_peor_seen': 'Deut 4:3', 'the_cleaving': 'Deut 4:4', 'taught_as_commanded': 'Deut 4:5', 'wisdom_before_the_peoples': 'Deut 4:6', 'god_so_near': 'Deut 4:7', 'righteous_statutes': 'Deut 4:8', 'the_write': 'Deut 4:1-8',
       'take_heed_lest_you_forget': 'Deut 4:9', 'the_daughters_excluded': 'shelf: Kiddushin 30a:6', 'the_day_at_horeb': 'Deut 4:10', 'learn_and_teach': 'Deut 4:10', 'the_mountain_burning': 'Deut 4:11', 'the_voice_and_no_form': 'Deut 4:12', 'the_ten_words_and_the_tablets': 'Deut 4:13', 'commanded_to_teach': 'Deut 4:14',
       'no_form_seen': 'Deut 4:15', 'the_image_list': 'Deut 4:16-18', 'image_for_study': 'shelf: Rosh Hashanah 24b:13', 'image_of_the_host': 'shelf: Rosh Hashanah 24b:8', 'the_host_apportioned': 'Deut 4:19', 'the_iron_furnace': 'Deut 4:20', 'the_bar_third_telling': 'Deut 4:21-22', 'the_covenant_not_forgotten': 'Deut 4:23', 'consuming_fire_jealous_god': 'Deut 4:24',
       'the_case_head': 'Deut 4:25', 'the_witnesses': 'Deut 4:26', 'perish_and_scatter': 'Deut 4:26-27', 'serve_wood_and_stone': 'Deut 4:28', 'seek_and_find': 'Deut 4:29', 'in_your_distress_return': 'Deut 4:30', 'the_merciful_god': 'Deut 4:31',
       'the_former_days': 'Deut 4:32', 'the_voice_and_lived': 'Deut 4:33', 'the_nation_from_a_nation': 'Deut 4:34', 'you_were_shown': 'Deut 4:35', 'from_heaven_the_voice': 'Deut 4:36', 'because_he_loved_your_fathers': 'Deut 4:37', 'to_dispossess_nations': 'Deut 4:38', 'know_this_day': 'Deut 4:39', 'keep_the_statutes': 'Deut 4:40',
       'then_moses_set_apart': 'Deut 4:41', 'not_until_all_six': 'Deut 4:41; Num 35:13-14', 'the_manslayer_defined': 'Deut 4:42', 'the_three_names': 'Deut 4:43', 'the_second_frame': 'Deut 4:44-45', 'the_borders_verbatim': 'Deut 4:46-49', 'the_readback_table': 'Deut 4:3-49'}
lines = ['\n\n# =====================================================================\n# Motion 2 — THE TEST DATA: the answer sheet\'s rows (the docket\'s LAW rows and the cells\' asks) — GENERATED FROM THE CELLS\' OWN ASKS by ch4_cases_gen.py\n# (1b\'s lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.\n# =====================================================================\nCASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(OH, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, OH.DATA)
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
    print('THE INK: numbers %s; the one frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH))
    print('THE READBACK: %d rows — %s; the deltas: Peor %s; Horeb %s; the tablets %s; the bar %s; the instruments %s; the frame %s; the borders %s' % (len(READBACK), dict(RB_GRADES), PEOR_DELTA, HOREB_DELTA, TABLETS_DELTA, BAR_DELTA, INSTR_DELTA, FRAME_DELTA, BORDERS_DELTA))
    print('THE HOLE: the ten words %s seats; the tablets plene %s; the giving\'s day %s (Rabbi Yose); the fortieth day %s' % (TEN_WORDS, TABLETS_PLENE, ES_DAYS['v'], ER_TAMMUZ['v']))
    print('THE CITIES: %s; the debit %s; the manslayer\'s diff %s' % (RF.DATA['the_six_cities']['value']['beyond_the_jordan'], RF_DEBIT[0][:60], MANSLAYER_DIFF[2:4]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 4: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch4_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, OH.SCENE, OH.NARRATIVE))
