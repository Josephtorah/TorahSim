import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch8_cases_gen.py's form.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_not_righteousness as NR
p2 = open(f'{SP}/ch9_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_frame'), ('F2', 'the_calf_retold'), ('F3', 'the_forty_days'), ('F4', 'aarons_peril'), ('F5', 'the_four_provocations'), ('F6', 'the_intercession')]
REF = {'hear_o_israel': 'Deut 9:1', 'nations_greater': 'Deut 9:1; Deut 4:38, 7:1 by CALL', 'fortified_to_the_heavens': 'Deut 9:1; Deut 1:28 by CALL; Chullin 90b:12', 'the_anakim': 'Deut 9:2; Num 13:22 by CALL', 'consuming_fire': 'Deut 9:3; Deut 4:24 by CALL', 'not_for_your_righteousness': 'Deut 9:4-6; Beitzah 25b:7', 'the_oath_to_the_fathers': 'Deut 9:5; Gen 22:16 (the tape)', 'stiff_necked': 'Deut 9:6; Exod 32:9 by CALL',
       'remember_do_not_forget': 'Deut 9:7; Arakhin 15a:14 by CALL', 'at_horeb_you_provoked': 'Deut 9:8; Exod 32:4 (the tape); Avodah Zarah 52a:4', 'the_tablets_of_the_covenant': 'Deut 9:9; Exod 24:8', 'written_with_the_finger': 'Deut 9:10; Exod 31:18; Deut 4:13 (the tape)', 'gods_word_verbatim': 'Deut 9:12-13; Exod 32:7-9', 'let_me_alone': 'Deut 9:14; Exod 32:10; Berakhot 32a:16, 7a:35', 'the_descent_and_the_sight': 'Deut 9:15-16; Exod 32:15', 'the_breaking_in_my_own_words': 'Deut 9:17; Exod 32:19; Shabbat 87a:5', 'the_fragments_in_the_ark': 'Deut 10:1-2 (forward); Menachot 99a:12', 'the_calf_ground_to_dust': 'Deut 9:21; Exod 32:20; Avodah Zarah 44a:1-2', 'the_calfs_own_day': 'shelf: Shabbat 89a:6 (OPEN)', 'the_calfs_debt': 'shelf: Sanhedrin 102a:15; Berakhot 32b:17', 'the_confession_specified': 'Deut 9:18, 9:21; Yoma 86b:14',
       'forty_days_forty_nights': 'Deut 9:9, 9:11, 9:18, 9:25', 'the_first_forty': 'Deut 9:9, 9:11; Taanit 28b:9; Mishnah Taanit 4:6', 'the_second_forty': 'Deut 9:18, 9:25; Berakhot 32b:8', 'prolong_without_expecting': 'shelf: Berakhot 32b:9', 'bread_i_did_not_eat': 'Deut 9:9, 9:18; Yoma 75b:11', 'i_sat_on_the_mount': 'Deut 9:9; Megillah 21a:17', 'at_the_end_of_forty_days': 'Deut 9:11; Deut 4:13 (the tape)', 'i_fell_down': 'Deut 9:18, 9:25; Devarim Rabbah 2:1',
       'the_peril': 'Deut 9:20 (the sixth form — SUPPLIED with the write)', 'half_the_edict': 'Deut 9:20; Vayikra Rabbah 10:5', 'at_that_time': 'Deut 9:20; Sanhedrin 102a:5', 'i_prayed_for_aaron': 'Deut 9:20 (the act)', 'aarons_report_untranslated': 'Deut 9:20; Mishnah Megillah 4:10 by CALL', 'the_re_acceptance': 'Deut 9:20; Lev 9:2, 9:7 by CALL',
       'taberah': 'Deut 9:22; Num 11:1 (the tape); Arakhin 15a:14', 'massah': 'Deut 9:22; Exod 17:7 (the tape); Deut 6:16 by CALL', 'kibroth_hattaavah': 'Deut 9:22; Num 11:31 (the tape)', 'kadesh_barnea': 'Deut 9:23; Num 14:1 (the tape); Deut 1:26 by CALL', 'the_ten_trials': 'Deut 9:22-24; Avot 5:4; Arakhin 15a:14 by CALL', 'rebellious_from_the_day': 'Deut 9:24; Deut 9:7', 'the_provocations_order': 'Deut 9:22-23 (the order)',
       'i_prayed_and_said': 'Deut 9:26; Devarim Rabbah 2:1', 'do_not_destroy_your_people': 'Deut 9:26; Exod 32:11 (the tape); Berakhot 32a:19', 'remember_your_servants': 'Deut 9:27; Exod 32:13; Shabbat 55a:11', 'the_merit_ceased': 'shelf: Shabbat 55a:13-16', 'lest_the_land_say': 'Deut 9:28; Num 14:16; Exod 32:12; Deut 1:27', 'your_people_and_your_inheritance': 'Deut 9:29; Exod 32:11 (the tape); 1 Kgs 8:51; Neh 1:10', 'the_lord_hearkened': 'Deut 9:19; Exod 32:14 (the tape)', 'the_anger_and_the_wrath': 'Deut 9:19; Nedarim 32a:4', 'the_three_requests': 'shelf: Berakhot 7a:23-25 (Exod 33:12-23 — no line)'}
lines = ['\n\n# =====================================================================\n# Motion 2 — THE TEST DATA: the answer sheet\'s rows (the docket\'s LAW rows and the cells\' asks) — GENERATED FROM THE CELLS\' OWN ASKS by ch9_cases_gen.py\n# (1b\'s lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.\n# =====================================================================\nCASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(NR, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, NR.DATA)
        assert v != 'no verdict in span', (name, a)
        assert a in REF, ('an ask without a label', name, a)
        lines.append('    (%r, lambda: %s({\'ask\': %r}, DATA), %r),' % ('%s — %s' % (REF[a], a), name, a, v))
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
    print('THE INK: the seven number verses %s; the divine frames inside the retelling %s, "saying" at %s; the imperatives %s; the infinitive absolutes %s; the consecutive perfects %s; NO prohibition; the case tokens %s; the register singular-only %s, plural-only %s, both %s, neither %s; the narrative verbs %d in %d verses; the first person singular in %d verses, plural %s; the Name %d; the tablets\' three spellings %s' % (sorted(PARSED.items()), DIV, [v for v in range(1, 30) if 'לאמר' in W9(v)], IMPER, INFA, WEQATAL_V, CASE_TOK, SG_ONLY, PL_ONLY, BOTH, NEITHER, sum(len(v) for v in WAY.values()), len(WAY), len(ONE_CS), ONE_CP, NAME, TABLETS_FORMS))
    print('THE READBACK OF A STRETCH (the sixth form): %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the stretch rows %s; the SUPPLIED row %s with its write %s; no row open %s; the OPEN rows %s; the holes %d: %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [(r['verses'], r['stretch']['from'], r['stretch']['to'], r['stretch']['days']) for r in READBACK if r['stretch']], [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [r['write'] for r in READBACK if r['grade'] == 'SUPPLIED'], not any(r['open'] for r in READBACK), [o['name'] for o in OPEN_ROWS], len(HOLES), [h['hole'].split(' — ')[0] for h in HOLES]))
    print('THE CLOCK READ BACK (the bare world\'s arithmetic): %s' % (CLOCK,))
    print('THE DELTAS (computed): %s' % (DELTA,))
    print('THE SCANS on the one database: aaron\'s peril %s (this sitting\'s own write excluded); the stiff neck on Israel %s' % (AARON_PERIL_SCAN, STIFF_SCAN))
    print('THE CALLEES: ascent forty %s / 17 tammuz %s / sheet %s; calf saru_stiff %s, seized %s, three_legged %s, vow %s, relent %s, four_verbs %s, fourth %s, dispute %s, surcharge %s, reading %s, boshesh %s, confess %s; tablets ratified %s, fragments %s; trials %s (%s); beha edge %s, sank %s, graves %s; shelach ability %s, offer %s, pardon %s, giants %s; OS murmuring %s; OH nations %s, fire %s, tablets %s, loved %s; CH tablets %s; HI test %s; SN seven %s; SD calf %s; GL forty %s' % (ER_FORTY['v'], ER_17['v'], ER_SHEET['v'], ER_STIFF['v'], ER_SEIZED['v'], ER_CHAIR['v'], ER_VOW['v'], ER_RELENT['v'], ER_VERBS['v'], ER_FOURTH['v'], ER_NULL['v'], ER_SURCHARGE['v'], ER_READING['v'], ER_BOSHESH['v'], ER_CONFESS['v'], ER_RATIFIED['v'], ER_FRAGMENTS['v'], ES_TRIALS['v'], ES_SIX['v'], BH_EDGE[1], BH_SANK[1], BH_GRAVES[1], SL_ABILITY[1], SL_OFFER[1], SL_PARDON[1], SL_GIANTS[1], OS_MURMUR[1], OH_NATIONS[1], OH_FIRE[1], OH_TABLETS[1], OH_LOVED[1], CH_TABLETS[1], HI_TEST[1], SN_SEVEN[1], SD_CALF['v'], GL_FORTY[1]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s (none — no prohibition in the chapter); the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5]))
    print('THE NARRATIVE: %s (the status on aaron dated %s)' % (NARRATIVE, _WN.clock.eras['exodus'].date(_WN.entity('aaron').ledger[0]['dated'])))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 9: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch9_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, NR.SCENE, NR.NARRATIVE))
