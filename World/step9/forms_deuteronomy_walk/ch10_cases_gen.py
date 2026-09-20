import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CASES GENERATED FROM THE CELLS' OWN ASKS (1b's lesson ii): import the assembled runner (CASES empty), run every ask of every cell, and write
# part 4 with the verdicts as LITERAL expectations (the honest-pairing guard reads literals only) — the report main appended. ch9_cases_gen.py's form.
import os, re, sys, io, contextlib, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_second_tablets as ST
p2 = open(f'{SP}/ch10_part2.py', encoding='utf-8').read()
CELLS = [('F1', 'the_tablets_and_the_ark'), ('F2', 'the_stations_and_the_death'), ('F3', 'the_levites_separated'), ('F4', 'the_third_forty_and_the_go'), ('F5', 'what_the_lord_asks'), ('F6', 'the_god_of_gods_and_the_stranger')]
REF = {'at_that_time_hew': 'Deut 10:1; Exod 34:2 (the tape); Exod 24:12', 'the_words_that_were': 'Deut 10:2; Exod 34:1', 'the_fragments_in_the_ark': 'Deut 10:2, 10:5 (the T2 row — SUPPLIED with the write); Bava Batra 14b:6; Menachot 99a:12', 'what_else_the_ark_held': 'shelf: Bava Batra 14a:12-14b:1', 'the_ark_is_one': 'Deut 10:1-8; Bava Batra 14a:8; Tosefta Sotah 7:9 (DISPUTE)', 'i_made_an_ark': 'Deut 10:3; Exod 37:1 (the tape); Yoma 72b:8', 'like_the_first_writing': 'Deut 10:4; Deut 5:22, 9:10 by CALL; Exod 34:28', 'the_receipt_10_5': 'Deut 10:5; Exod 40:20 (the tape); Deut 4:5 (the register)', 'the_elder_who_forgot': 'shelf: Berakhot 8b:7', 'the_ark_hidden': 'shelf: Mishnah Shekalim 6:1-2; Yoma 52b',
       'the_stations_reversed': 'Deut 10:6-7; Num 33:30-34 by CALL', 'aaron_died_there': 'Deut 10:6; Num 20:28 (the tape)', 'and_he_was_buried_there': 'Deut 10:6 (the T2 row — SUPPLIED with the write buried)', 'the_place_of_the_death': 'Deut 10:6 (OPEN); Seder Olam Rabbah 9:2', 'eleazar_ministered': 'Deut 10:6; Num 3:4; Num 20:26-28 by CALL', 'arad_heard': 'shelf: Rosh Hashanah 3a:1-3; Taanit 9a:9-12', 'aaron_in_av': 'Num 33:38; Seder Olam Rabbah 10:2', 'walk_after_his_attributes': 'Deut 10:12, 13:5; Sotah 14a:3-4',
       'at_that_time_separated': 'Deut 10:8; Exod 32:26 (the tape); Num 16:9', 'to_carry_the_ark': 'Deut 10:8; Num 4:4-15 by CALL', 'to_stand_and_minister': 'Deut 10:8; Num 18:1-7 by CALL; Arakhin 11a:10', 'to_bless_in_his_name': 'Deut 10:8; Num 6:23-27 by CALL; Sotah 38a:5, 38a:8', 'which_time': "Deut 10:8 (the docket's question)", 'levi_has_no_portion': 'Deut 10:9; Num 18:20 (the tape); Deut 18:2', 'as_the_lord_spoke_to_him': "Deut 10:9 (the receipt's third form)",
       'i_stood_on_the_mount': 'Deut 10:10 (the stretch row); Exod 34:4 (the marker); Megillah 21a:17', 'the_second_ascents_date': 'Exod 34:4, 34:28; Seder Olam Rabbah 6:2 (MATCH)', 'hearkened_that_time_also': 'Deut 10:10; Deut 9:19; Exod 32:11 (the tape)', 'not_willing_to_destroy': 'Deut 10:10; Deut 4:31', 'arise_go': 'Deut 10:11; Exod 32:34, 33:1 (no line — the hole outside the span)', 'the_charge_forward': 'Deut 10:11; Deut 31:7; Josh 1:6',
       'and_now_israel': 'Deut 10:12; Deut 4:1 by CALL (the forward marker)', 'what_does_the_lord_ask': 'Deut 10:12-13; Deut 6:5, 6:13, 8:6 by CALL (THE LINE demand_declared)', 'the_fear_of_heaven': 'shelf: Berakhot 33b:23; Megillah 25a:9; Niddah 16b:13', 'a_small_thing': 'shelf: Berakhot 33b:24-25', 'a_hundred_blessings': 'shelf: Menachot 43b:15; Shabbat 31b:1-3', 'for_your_good': 'Deut 10:13; Deut 4:40; Deut 6:3 by CALL', 'the_heaven_of_heavens': 'Deut 10:14; Deut 4:39 by CALL; Chagigah 12b:4', 'delighted_in_your_fathers': 'Deut 10:15; Deut 7:7, 4:37 by CALL', 'circumcise_the_heart': 'Deut 10:16 (THE LINE heart_circumcision_commanded); Sukkah 52a:7', 'the_grammar_guard': 'Deut 10:16; Lev 12:3, 19:23; Shabbat 108a:7', 'stiffen_no_more': 'Deut 10:16 (the one prohibition — stiffening_barred)', 'no_lashes_for_the_neck': 'Deut 10:16; Makkot 13b:6',
       'god_of_gods': 'Deut 10:17; Deut 7:9 by CALL; Ps 136:2-3', 'the_attributes_three': 'Deut 10:17; Yoma 69b:13-16; Berakhot 33b:21-22', 'lifts_no_face': 'Deut 10:17; Num 6:26 by CALL; Rosh Hashanah 17b:17', 'takes_no_bribe': 'Deut 10:17; Exod 23:8 by CALL; Ketubot 105a:10', 'the_permitted_fee': 'shelf: Ketubot 105a:17-19', 'a_salary_voids': 'shelf: Kiddushin 58b; Mishnah Bekhorot 4:6', 'the_bribe_of_words': 'shelf: Ketubot 105b:5, 105b:8-15', 'the_orphan_and_the_widow': 'Deut 10:18; Exod 22:21 by CALL', 'and_you_shall_love_the_stranger': 'Deut 10:19; Lev 19:34 by CALL (THE LINE stranger_love_commanded)', 'the_thirty_six_warnings': 'shelf: Bava Metzia 59b:13-15', 'the_converts_intake': 'shelf: Yevamot 47a:13-47b:15', 'the_private_convert': 'shelf: Yevamot 47a:8-12', 'fear_serve_cleave_swear': 'Deut 10:20; Deut 6:13 by CALL (THE LINE cleaving_commanded); Temurah 4a:2', 'cleave_to_the_scholars': 'shelf: Ketubot 111b:6-8', 'the_et_of_10_20': 'Deut 10:20; Pesachim 22b:11', 'swear_by_his_name': 'Deut 10:20; Shevuot 35b:22-23', 'a_truthful_oath': 'Deut 10:20; Temurah 3b:17-18', 'he_is_your_praise': 'Deut 10:21; Deut 7:19, 4:35 by CALL', 'seventy_persons': 'Deut 10:22; Gen 46:27, Exod 1:5 by CALL; Bava Batra 123b:1'}
lines = ['\n\n# =====================================================================\n# Motion 2 — THE TEST DATA: the answer sheet\'s rows (the docket\'s LAW rows and the cells\' asks) — GENERATED FROM THE CELLS\' OWN ASKS by ch10_cases_gen.py\n# (1b\'s lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.\n# =====================================================================\nCASES = [']
count = 0; per_cell = {}
for code, name in CELLS:
    body = p2.split('\ndef %s(' % name)[1].split('\ndef ')[0]
    asks = re.findall(r"if ask == '([a-z_0-9]+)':", body)
    lines.append('    # %s — %s' % (code, name))
    fn = getattr(ST, name)
    for a in asks:
        v, e, prov = fn({'ask': a}, ST.DATA)
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
    print('THE INK: the five number verses %s with the one ordinal %s; the divine frame %s; the imperatives God\'s to Moses %s; the consecutive perfects %s; the ONE prohibition %s; the register singular-only %s, plural-only %s, both %s, neither %s; the narrative verbs %d in %d verses; the Name %d bare tokens; the ark-lemma\'s book seats %s' % (sorted(PARSED.items()), {v: o for v, o in ORDS.items() if o}, [v for v in range(1, 23) if any(W10(v)[i:i + 2] in (['ויאמר', 'יהוה'], ['וידבר', 'יהוה']) for i in range(len(W10(v)) - 1))], {v: [x for x, m in wm('Deut', 10, v) if m and re.match(r'^HV.?.?v', m)] for v in (1, 11)}, {v: [x for x, m in wm('Deut', 10, v) if m and re.search(r'^HC/V.q', m)] for v in (1, 2, 16, 19)}, [(v, by[('Deut', 10, v)][i + 1][0]) for v in range(1, 23) for i, (x, _) in enumerate(by[('Deut', 10, v)][:-1]) if x in ('לא', 'ולא') and by[('Deut', 10, v)][i + 1][1] and re.match(r'^HV.i2', by[('Deut', 10, v)][i + 1][1])], [v for v, (p, s) in NUM.items() if s and not p], [v for v, (p, s) in NUM.items() if p and not s], [v for v, (p, s) in NUM.items() if p and s], [v for v, (p, s) in NUM.items() if not p and not s], sum(len(v) for v in WAY.values()), len(WAY), sum(1 for v in range(1, 23) for x in W10(v) if x in NAME), [s for s, x, _ in LEMT('727', books=('Deut',))]))
    print('THE READBACK — THE FORMS COMBINED, NO SEVENTH: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); the stretch rows %s; the SUPPLIED rows %s with their writes %s; no row open %s; the OPEN rows %s; the holes %d: %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), [(r['verses'], r['stretch']['from'], r['stretch']['to'], r['stretch']['days']) for r in READBACK if r['stretch']], [r['verses'] for r in READBACK if r['grade'] == 'SUPPLIED'], [r['write'] for r in READBACK if r['grade'] == 'SUPPLIED'], not any(r['open'] for r in READBACK), [o['name'] for o in OPEN_ROWS], len(HOLES), [h['hole'].split(' — ')[0] for h in HOLES]))
    print('THE CLOCK READ BACK (the bare world\'s arithmetic): %s' % (CLOCK,))
    print('THE SCANS on the one database: the fragments on the ark %s; the burial on aaron %s; the laws on Israel %s; love_owed anywhere %s; bribe_barred anywhere %s; the buried before Aaron %s' % (FRAG_SCAN, AARON_BURIED_SCAN, LAW_SCAN, LOVE_OWED_SCAN, BRIBE_SCAN, BURIED_ENTITIES))
    print('THE CALLEES: ER fragments %s, ratified %s, forty %s; SB both %s, maker %s, hands %s, dims %s; CH tablets %s; OH loved %s, shown %s, cleave %s; NR fragments %s, forty %s, hearkened %s; JO seven %s; CK moserah %s, succession %s; BM order %s; BH bearers %s; KR places %s; NS name %s, face %s; JS seventy %s, jochebed %s; HI heart %s, might %s, fss %s; GL kwf %s; SN chose %s, god %s; OR bribe %s, absolute %s, widow %s; HB love %s, seats %s' % (ER_FRAG['v'], ER_RATIFIED['v'], ER_FORTY['v'], SB_BOTH['v'], SB_MAKER['v'], SB_HANDS['v'], SB_DIM['v'], CH_TABLETS[1], OH_LOVED[1], OH_SHOWN[1], OH_CLEAVE[1], NR_FRAG[1], NR_FORTY[1], NR_HEARK[1], JO_SEVEN[1], CK_MOSERAH[1], CK_SUCC[1], BM_ORDER[1], BH_BEARERS[1], KR_PLACES[1], NS_NAME[1], NS_FACE[1], JS_70['v'], JS_JOCH['v'], HI_HEART[1], HI_MIGHT[1], HI_FSS[1], GL_KWF[1], SN_CHOSE[1], SN_GOD[1], OR_BRIBE['v'], OR_ABS['v'], OR_WIDOW['v'], HB_LOVE['v'], HB_SEATS['v']))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s (none — the one prohibition has no action); the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5]))
    print('THE NARRATIVE: %s (the status on the ark dated %s, on aaron %s)' % (NARRATIVE, _WN.clock.eras['exodus'].date(_WN.entity('the_ark').ledger[0]['dated']), _WN.clock.eras['exodus'].date(_WN.entity('aaron').ledger[0]['dated'])))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes, %d open rows' % (len(DATA[k]['value']), len(DATA[k]['holes']), len(DATA[k]['open_rows']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 10: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
'''
open(f'{SP}/ch10_part4.py', 'w', encoding='utf-8').write('\n'.join(lines) + MAIN)
print('CASES generated: %d (per cell %s); the scene %s; the narrative %s' % (count, per_cell, ST.SCENE, ST.NARRATIVE))
