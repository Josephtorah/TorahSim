#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch6_cases_gen.py's form.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_seven_nations as SN
p2 = open(f'{SP}/ch7_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_seven_nations'), ('F2', 'the_holy_people'), ('F3', 'the_faithful_god'), ('F4', 'because_you_hear'), ('F5', 'do_not_fear'), ('F6', 'the_images_and_the_devoted')]
REF = {'the_seven': 'Deut 7:1; the Sifrei 50:4', 'the_ban': 'Deut 7:2; Num 33:52-53 by CALL', 'the_bans_condition': 'shelf: Sotah 35b:10-13, 36a:1', 'no_covenant': 'Deut 7:2; Exod 23:32 by CALL', 'no_favor': 'Deut 7:2; Avodah Zarah 20a:1-4', 'praise_of_the_creator': 'shelf: Avodah Zarah 20a:10-11', 'no_marriage': 'Deut 7:3; Kiddushin 68b:2', 'the_child_follows_the_mother': 'Deut 7:3-4; Kiddushin 68b:3', 'the_four_objects': 'Deut 7:5; Exod 34:13 by CALL', 'the_asherah_shade': 'shelf: Mishnah Avodah Zarah 3:8', 'no_other_way': 'shelf: Avodah Zarah 48b:7-10', 'the_asherah_wood': 'shelf: Makkot 22a:2-3', 'the_write': 'the write',
       'holy_people': 'Deut 7:6; Exod 19:5-6 by CALL', 'chose_you': 'Deut 7:6-7; Deut 4:37 by CALL', 'the_fewest': 'Deut 7:7; Chullin 89a', 'the_oath': 'Deut 7:8; Gen 22:16, 26:3, 50:24 by CALL', 'brought_out_redeemed': 'Deut 7:8; Exod 12:51',
       'he_is_god': 'Deut 7:9; Deut 4:35, 39 by CALL', 'the_faithful': 'Deut 7:9; Shabbat 10b', 'thousand_generations': 'Deut 7:9; Deut 5:10 by CALL', 'the_hater_repaid': 'Deut 7:10; Deut 5:9 by CALL', 'the_triad': 'Deut 7:11; Deut 6:1 by CALL', 'the_written_read_pair': 'Deut 7:9 (the store)',
       'the_heel': 'Deut 7:12; Onkelos', 'covenant_kept': 'Deut 7:12; Exod 19:5', 'the_blessing_list': 'Deut 7:13; Exod 23:25 by CALL', 'no_barren': 'Deut 7:14; Exod 23:26 by CALL', 'the_diseases': 'Deut 7:15; Exod 15:26 by CALL', 'consume_no_pity': 'Deut 7:16; Bava Kamma 113b', 'no_serving_snare': 'Deut 7:16; Exod 23:33 by CALL',
       'the_doubt': 'Deut 7:17; Deut 1:28 by CALL', 'remember_pharaoh': 'Deut 7:18-19; Exod 7:20-12:29', 'the_trials': 'Deut 7:19; Deut 4:34 by CALL', 'the_hornet': 'Deut 7:20; Exod 23:28 by CALL', 'in_your_midst': 'Deut 7:21; Deut 6:15 by CALL', 'little_by_little': 'Deut 7:22; Exod 23:29-30 by CALL', 'the_kings_and_the_name': 'Deut 7:23-24; Exod 23:27, 31 by CALL',
       'burn_the_images': 'Deut 7:25; Mishnah Avodah Zarah 4:4', 'the_gentile_revokes': 'shelf: Avodah Zarah 52a:9-10', 'the_jew_bent_it': 'shelf: Avodah Zarah 42a:12', 'not_covet_silver_gold': 'Deut 7:25; Deut 5:21 by CALL', 'the_money_at_the_head': 'shelf: Mishnah Avodah Zarah 4:2', 'lest_snared': 'Deut 7:25; Exod 23:33 by CALL', 'abomination_to_the_lord': 'Deut 7:25; Deut 27:15', 'into_your_house': 'Deut 7:26; Mishnah Avodah Zarah 1:9', 'devoted_like_it': 'Deut 7:26; Avodah Zarah 54b', 'utterly_detest': 'Deut 7:26; Lev 11:43 by CALL', 'the_readback_table': 'Deut 7:1-26'}
lines = ['\n\n# =====================================================================\n# Motion 2 — THE TEST DATA: the answer sheet\'s rows (the docket\'s LAW rows and the cells\' asks) — GENERATED FROM THE CELLS\' OWN ASKS by ch7_cases_gen.py\n# (1b\'s lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.\n# =====================================================================\nCASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(SN, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, SN.DATA)
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
    print('THE INK: the two number verses %s (the oath\'s noun starred at 7:8); no frame %s, no saying, no imperative %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s, neither %s; the infinitive absolutes %s; the prohibitions second person %d, third %d; the first person %s' % (sorted(PARSED.items()), DIV, IMPER, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH, NEITHER, {v: [x for x, _ in l] for v, l in INFA.items()}, sum(1 for v in PRO for _, m in PRO[v] if 'i2' in m), sum(1 for v in PRO for _, m in PRO[v] if 'i3' in m), {v: [x for x, _ in l] for v, l in ONE_CS.items()}))
    print('THE READBACK ON THE KIN: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); no row open %s; the holes %d: %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), not any(r['open'] for r in READBACK), len(HOLES), [h['hole'].split(' — ')[0] for h in HOLES]))
    print('THE DELTAS (computed): %s' % (DELTA,))
    print('THE SEVEN-NAME LISTS %s; the six-name lists %d; the Girgashite %s' % (SEVEN_LISTS, len(SIX_LISTS), LEMV('1622')))
    print('THE CALLEES: no_covenant %s / not_dwell %s / hornet %s / little %s; the orders %s, the daughters %s, the child %s, the demolition %s; drive_out %s; the visiting %s, the coveting %s; the plagues %s, the treasure %s, the healer %s, the blotting %s; loved %s, shown %s; the triad %s; the murmuring %s; the oath lines %s / %s / %s; the Shittim spec %s; the classifier %s' % (OR_NOCOV['v'], OR_DWELL['v'], OR_HORNET['v'], OR_LITTLE['v'], ER_ORD['v'], ER_DAU['v'], ER_CHILD['v'], ER_GROW['v'], JO_DRIVE[1], CH_VIS[1], CH_COV[1], ES_TEN['v'], ES_TREAS['v'], ES_HEAL['v'], ES_BLOT['v'], OH_LOVED[1], OH_SHOWN[1], HI_TRIAD[1], OS_MURM[1], MA_TEST['v'], MA_FAM['v'], JS_KT['v'], BK_SPEC[1], SH_SWARM[0]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes' % (len(DATA[k]['value']), len(DATA[k]['holes']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 7: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch7_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, SN.SCENE, SN.NARRATIVE))
